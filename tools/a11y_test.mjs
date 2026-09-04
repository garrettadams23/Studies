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

await browser.close();

const failed = results.filter(r => r.violations.length);
const total = results.reduce((n, r) => n + r.violations.length, 0);
console.log(`\n${results.length - failed.length}/${results.length} scans clean` +
            (total ? `, ${total} violation(s)` : "") + ".");
process.exit(failed.length ? 1 : 0);
