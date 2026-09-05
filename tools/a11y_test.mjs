/**
 * a11y_test.mjs — axe-core against the built page, in both themes.
 *
 * Separate from smoke_test.mjs on purpose. The smoke test asserts that specific
 * behaviour still works and is expected to pass on every commit; this one runs
 * a third-party rule set that can legitimately grow new rules between versions,
 * and mixing the two would make a smoke failure ambiguous.
 *
 * What it checks, and where it stops:
 *
 *   * The shell at load, in dark and light. This is what every visitor sees
 *     first and it must be clean.
 *   * One opened domain with a topic expanded — the accordion, the tool
 *     buttons, the tables and the code blocks — again in both themes.
 *   * A study modal, because a dialog is where keyboard and focus problems
 *     actually live.
 *
 * It does *not* sweep all thirty domains. Content markup is generated from the
 * same conventions everywhere, so the thirtieth domain tests the same rules as
 * the first at thirty times the cost — and `lint_content.py` is what keeps the
 * conventions uniform.
 *
 * Usage:
 *   npm install axe-core playwright && node tools/a11y_test.mjs
 *   node tools/a11y_test.mjs --all      # every violation, not just serious+
 */

import { readFileSync } from "node:fs";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const PAGE = "file://" + process.cwd() + "/index.html";
const ALL = process.argv.includes("--all");

// Same resolution dance as the smoke test: a local install in CI, a global one
// on a developer machine.
const chromium = await (async () => {
  try {
    return (await import("playwright")).chromium;
  } catch {
    // Same list as smoke_test.mjs — this project has no package.json to hang a
    // dependency off, so both scripts look in the usual global roots.
    const bases = [
      "/opt/node22/lib/node_modules",
      "/usr/lib/node_modules",
      "/usr/local/lib/node_modules",
    ];
    for (const base of bases) {
      try {
        return (await import(`${base}/playwright/index.mjs`)).chromium;
      } catch { /* try the next one */ }
    }
    console.error("Could not find playwright. Run: npm install playwright");
    process.exit(2);
  }
})();

const axeSource = (() => {
  const roots = ["", "/opt/node22/lib/node_modules/", "/usr/lib/node_modules/",
                 "/usr/local/lib/node_modules/"];
  for (const root of roots) {
    try {
      return readFileSync(root ? `${root}axe-core/axe.min.js`
                               : require.resolve("axe-core/axe.min.js"), "utf-8");
    } catch { /* try the next root */ }
  }
  {
    console.error("Could not find axe-core. Run: npm install axe-core");
    process.exit(2);
  }
})();

const results = [];
const record = (name, violations) => {
  const kept = ALL ? violations
    : violations.filter(v => v.impact === "serious" || v.impact === "critical");
  results.push({ name, violations: kept });
  const mark = kept.length ? "FAIL" : "ok  ";
  console.log(`${mark} : ${name}` + (kept.length ? `  — ${kept.length} violation(s)` : ""));
  kept.forEach(v => {
    console.log(`        [${v.impact}] ${v.id}: ${v.help}`);
    v.nodes.slice(0, 3).forEach(n => console.log(`          ${n.target.join(" ")}`));
    if (v.nodes.length > 3) console.log(`          …and ${v.nodes.length - 3} more`);
  });
};

const browser = await chromium.launch();
const page = await browser.newPage();

const scan = async () => {
  await page.evaluate(axeSource);
  return page.evaluate(async () => {
    // Colour-contrast needs real rendering; the rest are structural.
    const r = await window.axe.run(document, {
      resultTypes: ["violations"],
      rules: { "color-contrast": { enabled: true } },
    });
    return r.violations.map(v => ({
      id: v.id, impact: v.impact, help: v.help,
      nodes: v.nodes.map(n => ({ target: n.target })),
    }));
  });
};

const setTheme = t => page.evaluate(theme => {
  document.documentElement.setAttribute("data-theme", theme);
}, t);

for (const theme of ["dark", "light"]) {
  await page.goto(PAGE, { waitUntil: "load" });
  await setTheme(theme);
  await page.waitForTimeout(200);
  record(`shell at load (${theme})`, await scan());

  await page.evaluate(() => {
    const first = document.querySelector(".domain-section").dataset.domain;
    openDomain(domainSection(first));
  });
  await page.waitForTimeout(300);
  await page.evaluate(() => document.querySelector(".domain-body.open .topic-header")?.click());
  await page.waitForTimeout(300);
  record(`an open domain with an expanded topic (${theme})`, await scan());

  await page.evaluate(() => stOpenProgress());
  await page.waitForTimeout(300);
  record(`a study dialog (${theme})`, await scan());
}

// ── the dialog's focus contract, which axe cannot see ───────────────────────
// axe reads the static properties of a page; it cannot press Tab. `aria-modal`
// was already set here and passed every scan while the keyboard walked straight
// out of the dialog into the page behind it — the worst combination there is,
// because assistive technology is told the background does not exist.
//
// Measured before this was fixed: **Shift+Tab escaped on the first press**, and
// forward Tab escaped after 31, which is just how many focusable things the
// progress dialog happens to hold. Sixty presses here for that reason — a trap
// test shorter than the dialog's own focusable count proves nothing, and the
// first version of this probe said "trapped" at twenty.
{
  const kb = await browser.newPage();
  await kb.goto(PAGE, { waitUntil: "load" });
  await kb.evaluate(() => document.querySelector("#study-fab").focus());
  await kb.evaluate(() => stOpenProgress());
  await kb.waitForTimeout(400);

  const inside = () => kb.evaluate(() => {
    const m = document.getElementById("st-modal");
    return !!m && m.contains(document.activeElement);
  });

  const openedInside = await inside();
  let out = 0;
  for (let i = 0; i < 60; i++) { await kb.keyboard.press("Tab"); if (!await inside()) out++; }
  for (let i = 0; i < 12; i++) { await kb.keyboard.press("Shift+Tab"); if (!await inside()) out++; }

  await kb.keyboard.press("Escape");
  await kb.waitForTimeout(250);
  const restored = await kb.evaluate(() => ({
    closed: document.getElementById("st-overlay").hidden,
    focus: document.activeElement?.id || document.activeElement?.tagName,
  }));

  record("opening a dialog moves focus into it", openedInside ? [] :
         [{ id: "focus-on-open", impact: "serious", nodes: [],
            help: "focus stayed outside #st-modal when the dialog opened" }]);
  record("Tab and Shift+Tab stay inside the dialog", out === 0 ? [] :
         [{ id: "focus-trap", impact: "serious", nodes: [],
            help: `${out} of 72 Tab presses left the dialog` }]);
  record("closing it puts focus back where it was", restored.closed && restored.focus === "study-fab" ? [] :
         [{ id: "focus-restore", impact: "serious", nodes: [],
            help: `closed=${restored.closed} focus=${restored.focus}` }]);
  await kb.close();
}

// ── the launcher menu, which is the way in to all of it ─────────────────────
// #study-menu is written *before* #study-fab in the DOM, so forward Tab from
// the button walked past the whole menu into the page header. Measured before
// this was fixed: Enter opened the menu, focus stayed on the button, and the
// next four Tab presses reached body and the three header buttons — no menu
// item at all. Escape closed nothing, because the global handler only knew
// about the dialog. Every study tool was unreachable by keyboard in the
// direction anyone would try first.
{
  const kb = await browser.newPage();
  await kb.goto(PAGE, { waitUntil: "load" });
  const state = () => kb.evaluate(() => {
    const menu = document.getElementById("study-menu");
    const el = document.activeElement;
    return { open: menu && !menu.hidden,
             expanded: document.getElementById("study-fab")?.getAttribute("aria-expanded"),
             inMenu: !!menu && menu.contains(el),
             id: el?.id || "",
             label: (el?.textContent || "").trim().slice(0, 18) };
  });
  const bad = (id, help) => [{ id, impact: "serious", nodes: [], help }];

  await kb.evaluate(() => document.getElementById("study-fab").focus());
  await kb.keyboard.press("Enter");
  await kb.waitForTimeout(200);
  const opened = await state();
  record("opening the study menu focuses its first item",
         opened.open && opened.inMenu && opened.expanded === "true" ? []
           : bad("menu-focus-on-open", `open=${opened.open} inMenu=${opened.inMenu} focus=${opened.id}`));

  await kb.keyboard.press("ArrowDown");
  const second = await state();
  await kb.keyboard.press("ArrowUp");
  const back = await state();
  await kb.keyboard.press("End");
  const last = await state();
  record("arrow keys walk the menu",
         second.inMenu && back.inMenu && last.inMenu && second.label !== back.label
           && last.label !== back.label ? []
           : bad("menu-arrows", `${second.label} / ${back.label} / ${last.label}`));

  await kb.keyboard.press("Escape");
  await kb.waitForTimeout(200);
  const closed = await state();
  record("Escape closes the menu and returns focus to the launcher",
         !closed.open && closed.expanded === "false" && closed.id === "study-fab" ? []
           : bad("menu-escape", `open=${closed.open} focus=${closed.id}`));
  await kb.close();
}

// ── the domain filter chips ─────────────────────────────────────────────────
// Thirty-one <div>s with a pointer cursor, no role, no tabindex and no label.
// Tab went from the search controls straight to the first domain header, so the
// filter bar — the site's primary navigation — could not be reached, operated
// or announced at all. They are <button>s now, and the visual test is what
// proves the conversion changed no pixels.
{
  const kb = await browser.newPage();
  await kb.goto(PAGE, { waitUntil: "load" });
  const shape = await kb.evaluate(() => {
    const chips = [...document.querySelectorAll(".chip")];
    return {
      total: chips.length,
      focusable: chips.filter(c => c.matches('a[href],button,[tabindex]:not([tabindex="-1"])')).length,
      pressedSet: chips.filter(c => c.hasAttribute("aria-pressed")).length,
      pressedMatchesActive: chips.every(c =>
        (c.getAttribute("aria-pressed") === "true") === c.classList.contains("active")),
    };
  });
  record("every domain chip is a real control",
         shape.total > 0 && shape.focusable === shape.total && shape.pressedSet === shape.total ? []
           : [{ id: "chip-controls", impact: "serious", nodes: [],
                help: `${shape.focusable}/${shape.total} focusable, ${shape.pressedSet} with aria-pressed` }]);
  record("the pressed chip is the active one",
         shape.pressedMatchesActive ? []
           : [{ id: "chip-pressed", impact: "serious", nodes: [],
                help: "aria-pressed and .active disagree" }]);

  // And genuinely in the tab order, not merely focusable in principle. From the
  // top of the document, because the filter bar sits *above* the search box —
  // the first version of this assertion tabbed forward from the search input
  // and failed on a page where the chips work perfectly, which is a wrong
  // premise about the DOM rather than a finding about the page.
  await kb.evaluate(() => { document.body.focus(); });
  let reached = false, steps = 0;
  for (; steps < 12 && !reached; steps++) {
    await kb.keyboard.press("Tab");
    reached = await kb.evaluate(() => !!document.activeElement?.classList?.contains("chip"));
  }
  record("tabbing from the top of the page reaches the filter bar",
         reached ? [] : [{ id: "chip-taborder", impact: "serious", nodes: [],
                           help: `${steps} Tab presses from the top never landed on a chip` }]);
  await kb.close();
}

// ── the card-link affordance on every concept card ──────────────────────────
// A `.concept-label` copies a link to that card. It was a bare <div> with a
// pointer cursor and a hover colour: no tab stop, no accessible name, nothing
// announced as actionable — the same shape as the chips, on every card on the
// site. Annotated rather than rewritten as a <button>, because the kicker text
// is authored in the domain files and read back by the markdown exporter.
{
  const kb = await browser.newPage();
  await kb.goto(PAGE, { waitUntil: "load" });
  await kb.evaluate(async () => {
    openDomain(domainSection(document.querySelector(".domain-section").dataset.domain));
    await new Promise(r => setTimeout(r, 400));
    document.querySelector(".domain-body.open .topic-header")?.click();
    await new Promise(r => setTimeout(r, 350));
  });
  const shape = await kb.evaluate(() => {
    const all = [...document.querySelectorAll(".domain-body.open .concept-label")];
    return { total: all.length,
             annotated: all.filter(l => l.getAttribute("role") === "button"
                                     && l.getAttribute("tabindex") === "0"
                                     && (l.getAttribute("aria-label") || "").length > 0).length };
  });
  record("every card label is an announced control",
         shape.total > 0 && shape.annotated === shape.total ? []
           : [{ id: "card-label-role", impact: "serious", nodes: [],
                help: `${shape.annotated}/${shape.total} annotated` }]);

  // role="button" is a promise about the keyboard; this is the promise kept.
  await kb.evaluate(() => document.querySelector(".domain-body.open .concept-label").focus());
  await kb.keyboard.press("Enter");
  await kb.waitForTimeout(250);
  const fired = await kb.evaluate(() =>
    document.querySelector(".domain-body.open .concept-label").classList.contains("copied"));
  record("Enter on a card label copies its link",
         fired ? [] : [{ id: "card-label-enter", impact: "serious", nodes: [],
                         help: "Enter did nothing on a role=button element" }]);
  await kb.close();
}

// ── does the page ever say what it just did? ────────────────────────────────
// axe checks that a live region is *well formed*; it cannot check that one
// exists where a result appears. Before this pass the whole app had two, and
// one of them (the service-worker bar) is populated before insertion, which
// many AT/browser pairs do not announce. Everything else — search counts, quiz
// answers, exam scores, the notepad's storage-full warning, the card-link
// confirmation — wrote into a bare element and said nothing.
{
  const kb = await browser.newPage();
  await kb.goto(PAGE, { waitUntil: "load" });
  const bad = (id, help) => [{ id, impact: "serious", nodes: [], help }];
  const liveShape = sel => kb.evaluate(s => {
    const e = document.querySelector(s);
    return e && e.getAttribute("aria-live") === "polite"
        && (e.getAttribute("role") === "status" || e.getAttribute("role") === "alert");
  }, sel);

  record("the shared announcer exists and is polite",
         await liveShape("#a11y-announcer") ? [] : bad("announcer", "#a11y-announcer is not a live region"));

  // Search is the highest-traffic result in the app: debounced, and it fires
  // without focus ever leaving the input.
  const searchLive = await liveShape("#search-count");
  await kb.evaluate(() => searchContent("kerberos"));
  await kb.waitForTimeout(400);
  const searchText = await kb.evaluate(() => document.getElementById("search-count").textContent)
    .catch(() => "");
  record("search announces its result",
         searchLive && /match/.test(searchText) ? []
           : bad("search-live", `live=${searchLive} text="${searchText}"`));

  // The announcer has to re-announce the same string twice — pressing the same
  // button again is a new event to the reader even if the text is identical.
  const repeated = await kb.evaluate(async () => {
    const el = document.getElementById("a11y-announcer");
    announce("same message");
    await new Promise(r => requestAnimationFrame(r));
    const first = el.textContent;
    announce("same message");
    const cleared = el.textContent;          // must go empty before it is re-set
    await new Promise(r => requestAnimationFrame(r));
    return { first, cleared, second: el.textContent };
  }).catch(e => ({ error: String(e.message || e).split("\n")[0] }));
  record("the announcer re-announces an identical message",
         repeated.first === "same message" && repeated.cleared === ""
           && repeated.second === "same message" ? []
           : bad("announcer-repeat", JSON.stringify(repeated)));

  // Every dialog announced "Study tools" whatever it was.
  await kb.evaluate(() => stOpenProgress());
  await kb.waitForTimeout(400);
  const named = await kb.evaluate(() => {
    const m = document.getElementById("st-modal");
    const id = m.getAttribute("aria-labelledby");
    return { id, label: m.getAttribute("aria-label"),
             name: id ? (document.getElementById(id)?.textContent || "").trim() : "" };
  });
  record("a dialog announces its own name, not the launcher's",
         named.id && /Progress/.test(named.name) && !named.label ? []
           : bad("dialog-name", JSON.stringify(named)));
  await kb.close();
}

// ── prefers-reduced-motion has to reach JavaScript ──────────────────────────
// The CSS block covers every transition and animation on the page, but a
// `behavior: "smooth"` passed in a scroll-options object overrides the
// `scroll-behavior` property, so five programmatic scrolls ignored the
// preference entirely. script.js had no matchMedia call at all.
{
  const motion = await browser.newPage();
  await motion.goto(PAGE, { waitUntil: "load" });
  const normal = await motion.evaluate(() => scrollBehavior())
    .catch(e => `error: ${String(e.message || e).split("\n")[0]}`);
  await motion.close();

  const reduced = await browser.newContext({ reducedMotion: "reduce" });
  const rp = await reduced.newPage();
  await rp.goto(PAGE, { waitUntil: "load" });
  const asked = await rp.evaluate(() => scrollBehavior())
    .catch(e => `error: ${String(e.message || e).split("\n")[0]}`);
  await reduced.close();

  record("a reduced-motion reader gets no smooth scrolling",
         normal === "smooth" && asked === "auto" ? []
           : [{ id: "reduced-motion", impact: "serious", nodes: [],
                help: `default=${normal} reduced=${asked}` }]);
}

// ── the heading outline ─────────────────────────────────────────────────────
// The page was `h1` → nothing → the occasional orphan `h4`: domains and topics
// were buttons, never headings, so a screen-reader user could not move through
// 30 domains or 1,534 topics by heading at all. axe's heading-order rule fires
// on headings in the wrong order, never on headings that are absent, so this
// was invisible to every scan the suite already ran.
{
  const kb = await browser.newPage();
  await kb.goto(PAGE, { waitUntil: "load" });
  await kb.evaluate(async () => {
    openDomain(domainSection(document.querySelector(".domain-section").dataset.domain));
    await new Promise(r => setTimeout(r, 450));
    document.querySelector(".domain-body.open .topic-header")?.click();
    await new Promise(r => setTimeout(r, 350));
  });
  const outline = await kb.evaluate(() => {
    const level = el => {
      const m = /^H([1-6])$/.exec(el.tagName);
      if (m) return +m[1];
      return el.getAttribute("role") === "heading" ? +(el.getAttribute("aria-level") || 0) : 0;
    };
    const all = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6,[role="heading"]')]
      .filter(e => e.offsetParent !== null || e.classList.contains("sr-only"));
    const levels = all.map(level);
    const counts = {};
    levels.forEach(l => { counts[l] = (counts[l] || 0) + 1; });
    const skips = [];
    for (let i = 1; i < levels.length; i++) {
      if (levels[i] > levels[i - 1] + 1) skips.push(`${levels[i - 1]}->${levels[i]}`);
    }
    return { counts, skips, domains: document.querySelectorAll(".domain-section").length };
  }).catch(e => ({ error: String(e.message || e).split("\n")[0] }));

  const c = outline.counts || {};
  record("the outline runs h1 → h2 → h3 → h4 with no level skipped",
         c[1] === 1 && c[2] === outline.domains && c[3] > 0 && c[4] > 0
           && (outline.skips || []).length === 0 ? []
           : [{ id: "heading-outline", impact: "serious", nodes: [],
                help: JSON.stringify(outline) }]);

  // A heading's name is computed from everything inside it, and a topic header
  // also holds a badge, a read time and four tool buttons. Unnamed, the rotor
  // entry came out twenty-five words long, which is worse than no heading.
  const names = await kb.evaluate(async () => {
    const h = document.querySelector(".domain-body.open .topic-header");
    const nameEl = h?.querySelector(".topic-name");
    return { label: h?.getAttribute("aria-label") || "",
             title: (nameEl?.textContent || "").replace(/\s+/g, " ").trim(),
             iconHidden: h?.querySelector(".topic-icon")?.getAttribute("aria-hidden") };
  }).catch(() => ({}));
  record("a topic heading is named by its title alone",
         names.label && names.label === names.title && names.iconHidden === "true" ? []
           : [{ id: "heading-name", impact: "serious", nodes: [],
                help: `label="${names.label}" title="${names.title}" icon-hidden=${names.iconHidden}` }]);
  await kb.close();
}

// ── do the toggle buttons say they are on? ──────────────────────────────────
// The star and tick are toggles, and their state lived only as a class on the
// parent .topic, which paints CSS. A screen reader read "Save topic to study
// list, button" whether the topic was already saved or not, and pressing it
// produced nothing audible — the state existed purely as a colour. axe cannot
// see this: a button with no aria-pressed is a perfectly valid button.
//
// Four places move these flags. Three of them are nowhere near the tool
// handler, so this drives the two that are reachable from the keyboard and the
// one that is easiest to forget: removing an entry from the study list.
{
  const kb = await browser.newPage();
  await kb.goto(PAGE, { waitUntil: "load" });
  const bad = (id, help) => [{ id, impact: "serious", nodes: [], help }];

  await kb.evaluate(() => openDomain(document.querySelector(".domain-section")));
  await kb.waitForTimeout(400);

  const pressed = sel => kb.evaluate(s => {
    const t = document.querySelector(".domain-body.open .topic");
    return t?.querySelector(`:scope > .topic-header ${s}`)?.getAttribute("aria-pressed");
  }, sel);
  const press = sel => kb.evaluate(async s => {
    const t = document.querySelector(".domain-body.open .topic");
    t.querySelector(`:scope > .topic-header ${s}`).click();
  }, sel);
  const announced = () => kb.evaluate(() =>
    (document.getElementById("a11y-announcer")?.textContent || "").trim());

  const b0 = await pressed(".topic-bookmark");
  await press(".topic-bookmark");
  await kb.waitForTimeout(120);
  const b1 = await pressed(".topic-bookmark");
  const bSaid = await announced();
  await press(".topic-bookmark");
  await kb.waitForTimeout(120);
  const b2 = await pressed(".topic-bookmark");

  record("the star button carries its own pressed state",
         b0 === "false" && b1 === "true" && b2 === "false" ? []
           : bad("bookmark-pressed", `aria-pressed went ${b0} -> ${b1} -> ${b2}`));
  record("starring a topic says so",
         /study list/i.test(bSaid) ? [] : bad("bookmark-announce", `announcer said "${bSaid}"`));

  const r0 = await pressed(".topic-review");
  await press(".topic-review");
  await kb.waitForTimeout(120);
  const r1 = await pressed(".topic-review");
  const rSaid = await announced();
  await press(".topic-review");
  await kb.waitForTimeout(120);
  const r2 = await pressed(".topic-review");

  record("the tick button carries its own pressed state",
         r0 === "false" && r1 === "true" && r2 === "false" ? []
           : bad("review-pressed", `aria-pressed went ${r0} -> ${r1} -> ${r2}`));
  record("marking a topic reviewed says so",
         /review/i.test(rSaid) ? [] : bad("review-announce", `announcer said "${rSaid}"`));

  // The study list un-stars a topic without going through the tool handler.
  // A fix applied only where the button lives would leave this one stale, and
  // the button would keep claiming pressed after the star had gone.
  await press(".topic-bookmark");
  await kb.waitForTimeout(120);
  const viaList = await kb.evaluate(async () => {
    const t = document.querySelector(".domain-body.open .topic");
    stOpenStudyList();
    await new Promise(r => setTimeout(r, 300));
    document.querySelector(`.st-list-remove[data-id="${t.id}"]`)?.click();
    await new Promise(r => setTimeout(r, 200));
    return t.querySelector(":scope > .topic-header .topic-bookmark")
            ?.getAttribute("aria-pressed");
  }).catch(e => `threw: ${String(e.message || e).split("\n")[0]}`);

  record("un-starring from the study list clears the button too",
         viaList === "false" ? []
           : bad("bookmark-list-sync", `aria-pressed was ${viaList} after removal`));
  await kb.close();
}

await browser.close();

const failed = results.filter(r => r.violations.length);
const total = results.reduce((n, r) => n + r.violations.length, 0);
console.log(`\n${results.length - failed.length}/${results.length} scans clean` +
            (total ? `, ${total} violation(s)` : "") + ".");
process.exit(failed.length ? 1 : 0);
