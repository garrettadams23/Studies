#!/usr/bin/env node
/**
 * smoke_test.mjs — Drives the built index.html in a real browser.
 *
 * plan.md has claimed "verified headless (Chromium)" since the first review, and
 * every session that changed structure re-derived a throwaway script to justify
 * it. That is the same shape as the cheat sheet's "Generated from the Math
 * domain" header: a capability asserted in prose with nothing checking it. This
 * is the check.
 *
 * It is deliberately about *behaviour a structural change can break* — decks
 * built per domain, permalinks derived from titles, progress keyed by slug —
 * rather than pixels. Folding a domain or moving a card between domains touches
 * every one of those.
 *
 * Since only one domain's content is in the document at a time, most of these
 * checks have to say which domain they mean and open it first. That is not
 * ceremony: a check that reads `document.querySelectorAll(".topic")` now
 * answers for a twenty-ninth of the site and passes, which is precisely the
 * silent-partial-result failure the design has to be held away from. Anything
 * page-wide is asserted against the inlined topic index instead.
 *
 * Usage:
 *   node tools/smoke_test.mjs                 # build first; this only reads
 *   node tools/smoke_test.mjs --url <file://> # non-default page
 */

import { existsSync } from "fs";
import { resolve } from "path";
import { createRequire } from "module";

// Resolve playwright from wherever it is: a local node_modules (CI does
// `npm install playwright`), or a global install (developer machines, and this
// project has no package.json to hang a dependency off).
const chromium = await (async () => {
  try {
    return (await import("playwright")).chromium;
  } catch {
    const require = createRequire(import.meta.url);
    for (const base of ["/opt/node22/lib/node_modules", "/usr/lib/node_modules",
                        "/usr/local/lib/node_modules"]) {
      try {
        return (await import(`${base}/playwright/index.mjs`)).chromium;
      } catch { /* try the next one */ }
    }
    console.error("error: playwright not found. Install it with 'npm install playwright'.");
    process.exit(1);
  }
})();

const ROOT = resolve(new URL("..", import.meta.url).pathname);
const argUrl = process.argv.indexOf("--url");
const PAGE = argUrl > -1 ? process.argv[argUrl + 1] : `file://${ROOT}/index.html`;

if (PAGE.startsWith("file://") && !existsSync(PAGE.slice(7))) {
  console.error(`error: ${PAGE.slice(7)} does not exist — run 'python build.py' first.`);
  process.exit(1);
}

const results = [];
const check = (name, pass, detail = "") => {
  results.push({ name, pass, detail });
  console.log(`${pass ? "ok  " : "FAIL"} : ${name}${detail ? `  — ${detail}` : ""}`);
};

/** Run a step that drives the page; a broken page must fail a check, not crash.
 *  Without this a missing #study-fab throws a 30s TimeoutError and the run ends
 *  with a stack trace and no summary — unreadable exactly when it matters. */
const step = async (name, fn, fallback = null) => {
  try {
    return await fn();
  } catch (e) {
    check(name, false, String(e.message || e).split("\n")[0].slice(0, 90));
    return fallback;
  }
};

const browser = await chromium.launch();
const context = await browser.newContext();
const page = await context.newPage();
const consoleErrors = [];
const offsite = [];
page.on("console", m => { if (m.type() === "error") consoleErrors.push(m.text()); });
page.on("pageerror", e => consoleErrors.push(`pageerror: ${e.message}`));
page.on("request", r => { if (!r.url().startsWith("file://")) offsite.push(r.url()); });

await page.goto(PAGE, { waitUntil: "load" });

/** Open one domain by clicking its header, and wait for the content to arrive.
 *  "attached", not "visible": during a search the domain's non-matching topics
 *  are hidden, and the first one usually is. */
const openDomain = async (id) => {
  // The header toggles, so clicking an already-open domain would close it —
  // and a deep link or a search may have opened it before this call.
  const already = await page.evaluate(d =>
    document.querySelector(`.domain-section[data-domain="${d}"]`)?.dataset.hydrated === "1", id);
  if (!already) await page.locator(`.domain-section[data-domain="${id}"] .domain-header`).click();
  await page.waitForSelector(`.domain-section[data-domain="${id}"] .topic`,
    { state: "attached", timeout: 5000 });
};

// ── structure ───────────────────────────────────────────────────────────────
const structure = await page.evaluate(() => {
  const chips = [...document.querySelectorAll(".chip[data-domain]")].map(c => c.dataset.domain);
  const sections = [...document.querySelectorAll(".domain-section[data-domain]")]
    .map(e => e.dataset.domain);
  const index = JSON.parse(document.getElementById("topic-index").textContent);
  return {
    chips, sections, index,
    indexed: Object.values(index).reduce((n, v) => n + v.length, 0),
    inDom: document.querySelectorAll(".topic").length,
    deferred: document.querySelectorAll("script.domain-src").length,
  };
});
// Every chip must have a section and vice versa: a domain removed from one and
// left in the other is exactly the breakage a fold causes, and it is silent.
const chipSet = new Set(structure.chips.filter(d => d !== "all"));
const secSet = new Set(structure.sections);
const orphanChips = [...chipSet].filter(d => !secSet.has(d));
const orphanSections = [...secSet].filter(d => !chipSet.has(d));
check("every filter chip has a domain section", orphanChips.length === 0, orphanChips.join(", "));
check("every domain section has a filter chip", orphanSections.length === 0, orphanSections.join(", "));
check("topics present", structure.indexed > 0,
  `${structure.indexed} topics, ${secSet.size} domains`);

// ── the deferral itself ─────────────────────────────────────────────────────
// The point of the build: every domain ships its content, none of it is markup
// until asked for. A regression here is silent — the page looks identical and
// simply costs what it used to.
check("no domain content in the document at load", structure.inDom === 0,
  `${structure.inDom} topic elements before any domain is opened`);
check("every domain has a deferred content block",
  structure.deferred === structure.sections.length,
  `${structure.deferred} blocks for ${structure.sections.length} domains`);

const [firstDomain, secondDomain] = structure.sections;
await step("opening a domain renders exactly that domain", async () => {
  await openDomain(firstDomain);
  const one = await page.evaluate(() => ({
    hydrated: [...document.querySelectorAll('.domain-section[data-hydrated="1"]')].map(s => s.dataset.domain),
    topics: document.querySelectorAll(".topic").length,
  }));
  check("opening a domain renders exactly that domain",
    one.hydrated.length === 1 && one.hydrated[0] === firstDomain && one.topics > 0,
    `${one.hydrated.join(", ") || "none"} · ${one.topics} topics`);

  // The eviction is the feature. Without it the page grows back to its old size
  // over a browsing session, one domain at a time, and nothing would say so.
  await openDomain(secondDomain);
  const two = await page.evaluate(() => ({
    hydrated: [...document.querySelectorAll('.domain-section[data-hydrated="1"]')].map(s => s.dataset.domain),
    stale: document.querySelectorAll(".domain-section:not([data-hydrated]) .topic").length,
  }));
  check("opening a second domain drops the first",
    two.hydrated.length === 1 && two.hydrated[0] === secondDomain && two.stale === 0,
    `${two.hydrated.join(", ")} live · ${two.stale} orphaned topics`);
});

// The ids the page routes on are stamped at build time; the ones the browser
// sees have to be the same ones, or every permalink resolves to a domain and
// then finds nothing in it.
const domIds = await page.evaluate(d =>
  [...document.querySelectorAll(`.domain-section[data-domain="${d}"] .topic`)].map(t => t.id),
  secondDomain);
const indexIds = structure.index[secondDomain] || [];
check("rendered topic ids match the inlined index",
  domIds.length === indexIds.length && domIds.every((id, i) => id === indexIds[i]),
  `${secondDomain}: ${domIds.length} rendered vs ${indexIds.length} indexed`);
await page.goto(PAGE, { waitUntil: "load" });

// ── every topic has a unique, non-empty id (permalinks depend on it) ────────
// From the index, which is the page-wide answer; the previous check confirmed
// the index and the rendered markup agree.
const ids = Object.values(structure.index).flat();
const dupes = ids.filter((id, i) => id && ids.indexOf(id) !== i);
check("every topic has an id", ids.every(Boolean), `${ids.filter(x => !x).length} missing`);
check("topic ids are unique", dupes.length === 0, [...new Set(dupes)].slice(0, 3).join(", "));

// ── permalinks: cold-load a hash and confirm it expands the right card ──────
const sample = ids.filter(Boolean).filter((_, i) => i % Math.ceil(ids.length / 5) === 0).slice(0, 5);
let permalinkFails = [];
for (const id of sample) {
  await page.goto(`${PAGE}#${id}`, { waitUntil: "load" });
  await page.waitForTimeout(450);
  const ok = await page.evaluate(i => {
    const t = document.getElementById(i);
    const body = t?.querySelector(".topic-body");
    return !!t && !!body && body.classList.contains("open") && body.offsetParent !== null;
  }, id);
  if (!ok) permalinkFails.push(id);
}
check("permalinks expand their topic", permalinkFails.length === 0, permalinkFails.join(", "));

// ── card-level permalinks: #topic/2 lands on that card, not just the topic ───
// Both halves matter. Landing on the wrong card is a silent wrong answer, and
// an index past the end has to fall back to the topic rather than doing
// nothing — links outlive the cards they were written against.
// Pick a topic that actually has several concept cards. The id map only knows
// ids, and card counts live in the deferred text, so a domain is opened and
// asked. Choosing the first id blindly picked a single-card topic and let the
// check pass without exercising anything.
await page.goto(PAGE, { waitUntil: "load" });
const cardProbeDomain = await page.evaluate(() =>
  document.querySelector(".domain-section")?.dataset.domain || null);
await openDomain(cardProbeDomain);
await page.waitForTimeout(250);
const cardTarget = await page.evaluate(() => {
  const t = [...document.querySelectorAll(".topic")]
    .find(x => x.id && x.querySelectorAll(".topic-body > .concept-card").length >= 3);
  return t ? t.id : null;
});
check("found a multi-card topic to test card links against", !!cardTarget, cardTarget || "none");
if (cardTarget) {
  await page.goto(`${PAGE}#${cardTarget}/2`, { waitUntil: "load" });
  await page.waitForTimeout(600);
  const hit = await page.evaluate(id => {
    const t = document.getElementById(id);
    const cards = t ? [...t.querySelectorAll(".topic-body > .concept-card")] : [];
    return { cards: cards.length, marked: cards.findIndex(c => c.classList.contains("card-linked")) };
  }, cardTarget);
  check("a card-level link marks that card",
    hit.cards >= 3 && hit.marked === 1,
    `${cardTarget}: ${hit.cards} cards, marked index ${hit.marked}`);

  await page.waitForTimeout(2400);   // let the mark expire before the next case
  await page.goto(`${PAGE}#${cardTarget}/99`, { waitUntil: "load" });
  await page.waitForTimeout(600);
  const over = await page.evaluate(id => ({
    open: !!document.getElementById(id)?.querySelector(".topic-body.open"),
    marked: !!document.querySelector(".concept-card.card-linked"),
  }), cardTarget);
  check("an out-of-range card index falls back to the topic",
    over.open && !over.marked, `open=${over.open} marked=${over.marked}`);
}

// ── per-domain size hints ───────────────────────────────────────────────────
// build.py computes these from the real word count; a missing or zero-topic
// meta means the stats function stopped seeing the body it measures.
const meta = await page.evaluate(() =>
  [...document.querySelectorAll(".domain-section")].map(s => ({
    domain: s.dataset.domain,
    text: s.querySelector(".domain-meta")?.textContent.trim() || null,
  })));
const missing = meta.filter(m => !m.text).map(m => m.domain);
const zero = meta.filter(m => m.text && /^0 topics/.test(m.text)).map(m => m.domain);
check("every domain has a size hint", missing.length === 0, missing.join(", "));
check("no domain reports 0 topics", zero.length === 0, zero.join(", "));

// ── search ──────────────────────────────────────────────────────────────────
// Search reads the deferred text, so it still covers all 29 domains while only
// one of them is rendered. Both halves are checked: the open domain shows its
// hits, and the domains that are not open still report theirs. A search that
// silently shrank to the open domain would pass the first half alone.
await page.goto(PAGE, { waitUntil: "load" });
await page.fill("#search-input", "kerberos");
await page.waitForTimeout(400);
const search = await page.evaluate(() => ({
  visible: [...document.querySelectorAll(".topic")].filter(t => t.offsetParent !== null).length,
  live: document.querySelectorAll('.domain-section[data-hydrated="1"]').length,
  badged: [...document.querySelectorAll(".domain-section:not(.search-hidden) .domain-matches")].length,
  count: document.getElementById("search-count")?.textContent || "",
}));
check("search narrows the page", search.visible > 0 && search.visible < 200,
  `${search.visible} visible`);
check("search still reaches unopened domains", search.badged > 1 && search.live === 1,
  `${search.badged} domains matched, ${search.live} rendered · ${search.count}`);

// Opening one of those collapsed domains has to land on the same result the
// count promised, not on the whole domain.
const otherDomain = await page.evaluate(() => {
  const live = document.querySelector('.domain-section[data-hydrated="1"]')?.dataset.domain;
  return [...document.querySelectorAll(".domain-section:not(.search-hidden)")]
    .map(s => s.dataset.domain).find(d => d !== live) || null;
});
if (otherDomain) {
  await openDomain(otherDomain);
  await page.waitForTimeout(250);
  const crossed = await page.evaluate(d => {
    const sec = document.querySelector(`.domain-section[data-domain="${d}"]`);
    const shown = [...sec.querySelectorAll(".topic")].filter(t => !t.classList.contains("search-hidden"));
    const promised = parseInt(sec.querySelector(".domain-matches")?.textContent || "0", 10);
    return { shown: shown.length, promised, marks: sec.querySelectorAll("mark.sh").length };
  }, otherDomain);
  check("a domain opened during a search shows its matches",
    crossed.shown === crossed.promised && crossed.promised > 0 && crossed.marks > 0,
    `${otherDomain}: ${crossed.shown} shown of ${crossed.promised} promised, ${crossed.marks} highlights`);
}
// ── search operators ────────────────────────────────────────────────────────
// `domain:` and quoted phrases narrow a 1,300-topic site to something a reader
// can use. The cases worth protecting are the ones that fail quietly: an
// operator that is ignored answers a different question than the one asked, and
// looks like a result rather than a mistake.
const ops = await page.evaluate(async () => {
  const el = document.getElementById("search-input");
  const probe = async q => {
    el.value = q;
    el.dispatchEvent(new Event("input", { bubbles: true }));
    await new Promise(r => setTimeout(r, 350));
    const n = document.getElementById("search-count")?.textContent || "";
    const m = n.match(/^(\d+) match/);
    return { text: n, hits: m ? Number(m[1]) : 0,
             domains: [...document.querySelectorAll(".domain-section:not(.search-hidden)")].length };
  };
  const out = {};
  out.bare      = await probe("firewall");
  out.scoped    = await probe("domain:net firewall");
  out.unknownDm = await probe("domain:nosuchdomain firewall");
  out.phrase    = await probe('"shuffle sharding"');
  out.nonsense  = await probe('"shuffle sharding" biscuits');
  out.shortText = await probe("domain:hw x");
  // The widened fallback: nothing on the site says "wifi 6", plenty says
  // "Wi-Fi 6". It must find them, and say that it had to fold the hyphen.
  out.folded    = await probe("wifi 6");
  // All the words, none of them adjacent.
  out.allWords  = await probe("tcp handshake");
  // And when even the widest pass finds nothing, the page must end hidden
  // behind the "no matches" line rather than in the reset the fallback needed.
  out.hopeless  = await probe("kumquat trombone");
  return out;
});
check("domain: narrows the search", ops.scoped.hits > 0 && ops.scoped.hits < ops.bare.hits
  && ops.scoped.domains === 1,
  `${ops.bare.hits} unscoped -> ${ops.scoped.hits} in ${ops.scoped.domains} domain`);
check("an unknown domain: yields nothing, not everything", ops.unknownDm.hits === 0,
  ops.unknownDm.text);
check("a quoted phrase matches", ops.phrase.hits > 0, ops.phrase.text);
check("phrase and free text are combined, not merged", ops.nonsense.hits === 0,
  ops.nonsense.text);
check("free text too short to use rejects the query rather than dropping it",
  ops.shortText.hits === 0, ops.shortText.text || "(cleared)");
check("a query the site only hyphenates still finds it, and says it widened",
  ops.folded.hits > 0 && /hyphen/.test(ops.folded.text), ops.folded.text);
check("words that are never adjacent still find the card",
  ops.allWords.hits > 0 && /all your words/.test(ops.allWords.text), ops.allWords.text);
check("a query nothing answers leaves the page hidden, not reset",
  ops.hopeless.hits === 0 && ops.hopeless.domains === 0, ops.hopeless.text);

await page.fill("#search-input", "");
await page.waitForTimeout(250);

// ── study decks: one option per studyable domain, plus the three special ────
const deck = await step("study tools open", async () => {
  await page.click("#study-fab", { timeout: 5000 });
  await page.click('.study-mi[data-act="cards"]', { timeout: 5000 });
  await page.waitForTimeout(350);
  return page.evaluate(() => {
    const sel = document.querySelector("#st-modal select");
    return sel ? {
      n: sel.options.length,
      values: [...sel.options].map(o => o.value),
      labels: [...sel.options].map(o => o.textContent.trim()),
    } : null;
  });
});
check("flashcard deck picker exists", !!deck);
if (deck) {
  const domainOpts = deck.values.filter(v => !v.startsWith("__"));
  const missing = [...secSet].filter(d => d !== "acronym" && !domainOpts.includes(d));
  const extra = domainOpts.filter(d => !secSet.has(d));
  check("a deck for every studyable domain", missing.length === 0, missing.join(", "));
  check("no deck for a domain that is gone", extra.length === 0, extra.join(", "));
  // A deck labelled (0) means the domain's cards did not reach the deck builder.
  const empty = deck.labels.filter(l => /\(0\)$/.test(l));
  check("no empty decks", empty.length === 0, empty.join(", "));
}

// Every card in every deck must have something on its back. Six topics used to
// fail this — four `shortcut` keystroke tables, the AI glossary and the military
// code list — all of them lookup surfaces with no prose anywhere in the topic,
// which is the same species as the acronym dictionary the deck builder already
// excludes by name. The rule is about shape now, so this is what guards it.
const backs = await page.evaluate(() =>
  stIndex().filter(stIsStudyable)
           .filter(t => !((t.title || "").trim() || (t.desc || "").trim()))
           .map(t => `${t.domainId}/${t.id}`));
check("every studyable topic has something on the back of its card",
  backs.length === 0, backs.slice(0, 5).join(", "));
await page.keyboard.press("Escape");
await page.waitForTimeout(200);

// ── progress round-trip, on a real card ─────────────────────────────────────
const target = ids.find(Boolean);
const persisted = await step("reviewed state persists across reload", async () => {
  await page.goto(`${PAGE}#${target}`, { waitUntil: "load" });
  await page.waitForTimeout(500);
  // Attribute selector, not `#id`: slugs are ASCII but may start with a digit,
  // which is a valid id and an invalid bare CSS id selector.
  await page.locator(`[id="${target}"] .topic-review`).first().click({ timeout: 5000 });
  await page.waitForTimeout(200);
  await page.reload({ waitUntil: "load" });
  await page.waitForTimeout(500);
  return page.evaluate(
    id => localStorage.getItem(`reviewed:${id}`) === "1" &&
          document.getElementById(id)?.classList.contains("reviewed"), target);
}, "threw");
if (persisted !== "threw") check("reviewed state persists across reload", persisted, target);

// ── acronym expansion density ───────────────────────────────────────────────
// Three modes on a class on <body>, with a stored preference. Worth a check
// because the failure is silent in both directions: a mode that stops applying
// leaves expansions on for a reader who turned them off, and a preference that
// stops persisting resets on every visit without erroring.
const acro = await step("acronym density toggle cycles and persists", async () => {
  await page.goto(PAGE, { waitUntil: "load" });
  await page.waitForTimeout(400);
  const seen = [];
  for (let i = 0; i < 4; i++) {
    seen.push(await page.evaluate(() =>
      document.body.className.match(/acro-(hover|off)/)?.[1] || "always"));
    await page.click("#hdr-acro-btn");
    await page.waitForTimeout(120);
  }
  const cycled = seen.join(">") === "always>hover>off>always";
  // The stored preference has to survive a reload, which is the whole point of
  // storing it rather than keeping it in a variable.
  await page.evaluate(() => localStorage.setItem("acro-density", "off"));
  await page.reload({ waitUntil: "load" });
  await page.waitForTimeout(400);
  const kept = await page.evaluate(() => document.body.classList.contains("acro-off"));
  return { cycled, kept, seen: seen.join(" > ") };
});
if (acro !== "threw") {
  check("acronym density cycles always > hover > off", acro.cycled, acro.seen);
  check("acronym density preference survives a reload", acro.kept, acro.kept ? "acro-off" : "lost");
}
await page.evaluate(() => localStorage.removeItem("acro-density")).catch(() => {});

// ── recently viewed in the quick-jump palette ───────────────────────────────
// The palette opens on an empty query, and what it shows first is the only
// thing most readers ever see of it. Checked because both halves fail quietly:
// visits that stop being recorded leave an arbitrary list, and recent rows that
// leak into a filtered query put the wrong topics above the matches.
const recent = await step("quick jump leads with recently viewed", async () => {
  await page.goto(PAGE, { waitUntil: "load" });
  await page.evaluate(() => localStorage.removeItem("recent-topics"));
  await page.waitForTimeout(300);
  const visited = await page.evaluate(() => {
    const idx = typeof topicIndex === "function" ? topicIndex() : {};
    return Object.values(idx).flat().slice(0, 3);
  });
  for (const id of visited) {
    await page.evaluate(i => { location.hash = i; }, id);
    await page.waitForTimeout(400);
  }
  const stored = await page.evaluate(() => JSON.parse(localStorage.getItem("recent-topics") || "[]"));
  await page.evaluate(() => stOpenJump());
  await page.waitForTimeout(300);
  const led = await page.evaluate(n => {
    const rows = [...document.querySelectorAll(".st-jump-item")].slice(0, n);
    return rows.length === n && rows.every(r => !!r.querySelector(".st-jump-recent"));
  }, visited.length);
  await page.fill("#st-jump-input", "kerberos");
  await page.waitForTimeout(250);
  const leaked = await page.evaluate(() => !!document.querySelector(".st-jump-recent"));
  return { newestFirst: stored[0] === visited[visited.length - 1], count: stored.length, led, leaked };
});
if (recent !== "threw") {
  check("visits are recorded newest-first", recent.newestFirst && recent.count === 3,
    `${recent.count} recorded`);
  check("the palette's empty query leads with them", recent.led, recent.led ? "all badged" : "not led");
  check("recent rows do not leak into a filtered query", !recent.leaked,
    recent.leaked ? "badge present under query" : "none");
}
await page.evaluate(() => localStorage.removeItem("recent-topics")).catch(() => {});

// ── theming: every marked volatile claim, and the topology diagrams ─────────
// Both live inside domain content, so the domain that owns them has to be open
// to have anything to measure. Which domain that is comes from the deferred
// text rather than a hard-coded name — these move between waves, and a check
// that silently measures nothing is worse than one that fails.
const domainWith = async (needle) => page.evaluate(sel =>
  [...document.querySelectorAll("script.domain-src")]
    .find(s => s.textContent.includes(sel))?.dataset.domain || null, needle);
const topoDomain = await domainWith('class="topo-svg"');
const volDomain = await domainWith('class="volatile"');

const themed = async () => {
  const out = { body: null, line: null, circle: null, volatile: null };
  out.body = await page.evaluate(() => getComputedStyle(document.body).backgroundColor);
  if (topoDomain) {
    await openDomain(topoDomain);
    Object.assign(out, await page.evaluate(() => {
      const g = el => el ? getComputedStyle(el) : null;
      return {
        line: g(document.querySelector(".topo-svg line"))?.stroke,
        circle: g(document.querySelector(".topo-svg circle"))?.fill,
      };
    }));
  }
  if (volDomain) {
    await openDomain(volDomain);
    out.volatile = await page.evaluate(() => {
      const el = document.querySelector(".volatile");
      return el ? getComputedStyle(el).borderBottomColor : undefined;
    });
  }
  return out;
};
check("the themed elements are in some domain", !!topoDomain && !!volDomain,
  `topo-svg in ${topoDomain}, volatile in ${volDomain}`);
const darkT = await themed();
await page.evaluate(() => document.documentElement.setAttribute("data-theme", "light"));
await page.waitForTimeout(250);
const lightT = await themed();
// Assert presence separately from behaviour. Skipping a check when its element
// is missing is how a harness reports success on a page that lost the feature:
// renaming .topo-svg once took this file from 21 checks to 19, all passing.
for (const k of ["body", "line", "circle", "volatile"]) {
  if (darkT[k] == null) {
    check(`'${k}' element is present to theme`, false, "selector matched nothing");
    continue;
  }
  check(`'${k}' follows the theme`, darkT[k] !== lightT[k], `${darkT[k]} -> ${lightT[k]}`);
}

// ── nothing hard-coded survived into a style attribute ──────────────────────
const rawHex = await page.evaluate(() =>
  [...document.querySelectorAll("[style*='#']")]
    .filter(e => /#[0-9a-fA-F]{3,8}\b/.test(e.getAttribute("style"))).length);
check("no raw hex colour in a style attribute", rawHex === 0, `${rawHex} found`);

// ── keyboard: Enter opens a domain, then a topic ────────────────────────────
await page.goto(PAGE, { waitUntil: "load" });
await page.locator(".domain-header").first().focus();
await page.keyboard.press("Enter");
await page.waitForTimeout(300);
const kbDomain = await page.evaluate(() =>
  document.querySelector(".domain-body")?.classList.contains("open"));
check("Enter opens a domain", !!kbDomain);
// The header is layout; the control inside it is a real <button>, so that the
// per-topic tool buttons beside it are not nested inside another control.
await page.locator(".domain-body.open .topic-toggle").first().focus();
await page.keyboard.press("Enter");
await page.waitForTimeout(300);
const kbTopic = await page.evaluate(() => {
  const toggle = document.querySelector(".domain-body.open .topic-toggle");
  return {
    expanded: toggle?.getAttribute("aria-expanded"),
    isButton: toggle?.tagName,
    headerHasRole: document.querySelector(".domain-body.open .topic-header")?.hasAttribute("role"),
    bodyOpen: !!toggle?.parentElement.parentElement
      .querySelector(":scope > .topic-body")?.classList.contains("open"),
  };
});
check("Enter opens a topic and sets aria-expanded",
  kbTopic.expanded === "true" && kbTopic.bodyOpen, `aria-expanded=${kbTopic.expanded}`);
// The violation this replaced: role="button" on a header that contains four
// real buttons is a control inside a control, and axe reports it as serious.
check("the topic toggle is a real button and the header claims no role",
  kbTopic.isButton === "BUTTON" && kbTopic.headerHasRole === false,
  `${kbTopic.isButton}, header role=${kbTopic.headerHasRole}`);

// ── domain landing cards ────────────────────────────────────────────────────
// The card is data, not content: it must render above the topics, link only to
// topics that exist, and stay out of everything that counts .topic elements.
await page.goto(PAGE, { waitUntil: "load" });
const introPayload = await page.evaluate(() => {
  const el = document.getElementById("domain-intros");
  try { return el ? JSON.parse(el.textContent) : null; } catch { return null; }
});
const domainIds = await page.evaluate(() =>
  [...document.querySelectorAll(".domain-section")].map(s => s.dataset.domain));
check("every domain has a landing card in the payload",
  !!introPayload && domainIds.every(d => introPayload[d]),
  `${introPayload ? Object.keys(introPayload).length : 0} intros for ${domainIds.length} domains`);

const introDomain = domainIds[0];
await page.evaluate(d => openDomain(domainSection(d)), introDomain);
await page.waitForTimeout(300);
const intro = await page.evaluate(d => {
  const body = domainSection(d).querySelector(".domain-body");
  const card = body.querySelector(":scope > .domain-intro");
  if (!card) return null;
  return {
    first: body.firstElementChild === card,
    rows: [...card.querySelectorAll(".di-label")].map(l => l.textContent),
    // Scoped to the "Start here" row: the "Updated" row below it reuses
    // .di-link, and counting both would make this check pass for the wrong
    // reason the moment either row changed.
    links: [...card.querySelectorAll(".di-start .di-link")].map(b => b.textContent),
    updated: card.querySelector(".di-updated .di-when")?.textContent || "",
    updatedLinks: card.querySelectorAll(".di-updated .di-link").length,
    topics: body.querySelectorAll(".topic").length,
    indexed: (topicIndex()[d] || []).length,
    introIsTopic: card.classList.contains("topic"),
  };
}, introDomain);
check("the landing card renders above the topics",
  !!intro && intro.first, intro ? `first=${intro.first}` : "no .domain-intro");
check("the landing card carries its rows",
  !!intro && intro.rows.length >= 3, intro ? intro.rows.join(",") : "");
// Names are resolved at render time, so a link that survived is a link that
// points at a topic actually in this domain. A count short of the payload's
// means a topic was renamed and the card silently lost a signpost.
const wantStarts = introPayload?.[introDomain]?.start?.length ?? 0;
check("every 'start here' name resolved to a real topic",
  !!intro && intro.links.length === wantStarts,
  `${intro ? intro.links.length : 0}/${wantStarts} resolved`);
check("the landing card is not counted as a topic",
  !!intro && !intro.introIsTopic && intro.topics === intro.indexed,
  intro ? `${intro.topics} in DOM vs ${intro.indexed} indexed` : "");

// Clicking a start link must land on that topic, open.
// The landing card says when the domain was last reviewed and what was
// reviewed then, from the freshness stamps — a reference site should answer
// "is anyone still maintaining this?" without being asked.
check("the landing card says when the domain was last updated",
  !!intro && /^[A-Z][a-z]+ \d{4}$/.test(intro.updated) && intro.updatedLinks > 0,
  intro ? `${intro.updated}, ${intro.updatedLinks} topics` : "");

const startJump = await page.evaluate(async () => {
  const card = document.querySelector(".domain-body.open > .domain-intro");
  const btn = card?.querySelector(".di-start .di-link");
  if (!btn) return null;
  const want = btn.textContent;
  btn.click();
  await new Promise(r => setTimeout(r, 350));
  const t = document.getElementById(location.hash.slice(1));
  // The heading carries its inline acronym expansions; the card stores the
  // title as written. Compare like for like by dropping the expansion spans,
  // which is exactly what plainLabel() does when the card's names are matched.
  const name = t?.querySelector(".topic-name")?.cloneNode(true);
  name?.querySelectorAll(".acro-exp").forEach(e => e.remove());
  const got = (name?.textContent || "").replace(/\s+/g, " ").trim();
  return { want, got,
           open: !!t?.querySelector(".topic-body")?.classList.contains("open") };
});
check("a 'start here' link opens its topic",
  !!startJump && startJump.open && startJump.got === startJump.want,
  startJump ? `${startJump.want} -> ${startJump.got} (open=${startJump.open})` : "no link");

// The check above only exercises one domain. A rename in any of the other
// twenty-nine costs that card a signpost just as quietly, so resolve the whole
// payload the same way the renderer does.
const unresolved = await page.evaluate(() => {
  const intros = domainIntros();
  const bad = [];
  Object.keys(intros).forEach(d => {
    const names = new Set(domainTopics(d).map(t => t.name));
    (intros[d].start || []).forEach(n => { if (!names.has(n)) bad.push(`${d}: ${n}`); });
  });
  return bad;
});
// The changelog is generated from the freshness stamps, so a domain missing
// from it means the stamps are missing — worth failing on, not shrugging at.
const logCoverage = await page.evaluate(() => {
  const log = changelog();
  const ids = [...document.querySelectorAll(".domain-section")].map(s => s.dataset.domain);
  const byId = new Set(stIndex().map(t => t.id));
  const missing = ids.filter(d => !log[d]);
  const dead = Object.keys(log).flatMap(d => (log[d].topics || []).filter(t => !byId.has(t)));
  const badMonth = Object.keys(log).filter(d => !/^\d{4}-\d{2}$/.test(log[d].month || ""));
  return { domains: ids.length, logged: Object.keys(log).length, missing, dead, badMonth };
});
check("every domain with stamped topics has a changelog entry",
  logCoverage.missing.length <= 1, `missing: ${logCoverage.missing.join(", ") || "none"}`);
check("every changelog entry names real topics and a real month",
  logCoverage.dead.length === 0 && logCoverage.badMonth.length === 0,
  `${logCoverage.dead.length} dead, ${logCoverage.badMonth.length} bad months`);

check("every landing card's 'start here' names resolve, in all domains",
  unresolved.length === 0, unresolved.slice(0, 3).join(" | "));

// A search asked for topics; the front matter should get out of the way, and
// come back when the query is cleared.
await page.evaluate(() => runSearch("subnet"));
await page.waitForTimeout(300);
const introDuringSearch = await page.evaluate(() =>
  [...document.querySelectorAll(".domain-body.open > .domain-intro")]
    .every(c => getComputedStyle(c).display === "none"));
await page.evaluate(() => runSearch(""));
await page.waitForTimeout(300);
const introAfterSearch = await page.evaluate(() => {
  const c = document.querySelector(".domain-body.open > .domain-intro");
  return c ? getComputedStyle(c).display !== "none" : null;
});
check("the landing card hides while a search is filtering", introDuringSearch === true);
check("the landing card comes back when the search is cleared", introAfterSearch === true);

// ── see also ────────────────────────────────────────────────────────────────
// The strip renders on open, links only to topics that resolve, and following
// one lands on that topic — including when it lives in another domain, which is
// half of them and the case a within-domain test would never exercise.
await page.goto(PAGE, { waitUntil: "load" });
const saProbe = await page.evaluate(async () => {
  const rel = relatedTopics();
  // Pick a topic whose strip crosses a domain boundary.
  const src = Object.keys(rel).find(id =>
    topicDomain(id) && rel[id].some(t => topicDomain(t) && topicDomain(t) !== topicDomain(id)));
  if (!src) return null;
  location.hash = src;
  openHashTarget();
  await new Promise(r => setTimeout(r, 400));
  const topic = document.getElementById(src);
  const strip = topic?.querySelector(":scope > .topic-body > .see-also");
  return {
    src,
    wanted: rel[src].length,
    rendered: strip ? strip.querySelectorAll(".sa-link").length : 0,
    label: strip?.querySelector(".sa-label")?.textContent || "",
    tagged: strip ? strip.querySelectorAll(".sa-domain").length : 0,
    lastChild: strip ? topic.querySelector(":scope > .topic-body").lastElementChild === strip : false,
  };
});
check("a related topic renders its see-also strip",
  !!saProbe && saProbe.rendered === saProbe.wanted && saProbe.label === "See also",
  saProbe ? `${saProbe.rendered}/${saProbe.wanted} links on ${saProbe.src}` : "no cross-domain pair");
check("the strip sits below the last concept card",
  !!saProbe && saProbe.lastChild);
check("a link out of the domain says so",
  !!saProbe && saProbe.tagged > 0, saProbe ? `${saProbe.tagged} tagged` : "");

const saJump = await page.evaluate(async () => {
  const btn = document.querySelector(".topic-body.open .see-also .sa-link");
  if (!btn) return null;
  const want = btn.childNodes[0].textContent.trim();
  btn.click();
  await new Promise(r => setTimeout(r, 400));
  const t = document.getElementById(location.hash.slice(1));
  const name = t?.querySelector(".topic-name")?.cloneNode(true);
  name?.querySelectorAll(".acro-exp").forEach(e => e.remove());
  return { want, got: (name?.textContent || "").replace(/\s+/g, " ").trim(),
           open: !!t?.querySelector(".topic-body")?.classList.contains("open") };
});
check("following a see-also link opens that topic",
  !!saJump && saJump.open && saJump.got === saJump.want,
  saJump ? `${saJump.want} -> ${saJump.got}` : "no link");

// The strip is rendered once per topic however the topic was opened, and every
// id in the payload has to resolve — a dead id would render a link to nothing.
const saOnce = await page.evaluate(async () => {
  const id = location.hash.slice(1);
  const topic = document.getElementById(id);
  const header = topic?.querySelector(".topic-header");
  header?.click(); await new Promise(r => setTimeout(r, 150));
  header?.click(); await new Promise(r => setTimeout(r, 150));
  return topic?.querySelectorAll(".see-also").length ?? -1;
});
check("the strip is rendered once, not once per open", saOnce <= 1, `${saOnce} strips`);

const relDead = await page.evaluate(() => {
  const rel = relatedTopics();
  const bad = [];
  Object.keys(rel).forEach(src => {
    if (!topicDomain(src)) bad.push(src);
    rel[src].forEach(t => { if (!topicDomain(t)) bad.push(`${src} -> ${t}`); });
  });
  return bad;
});
check("every related id resolves to a real topic",
  relDead.length === 0, relDead.slice(0, 3).join(" | "));

// ── clickable cross-references ──────────────────────────────────────────────
// build.py resolves every <span class="xref"> title to a topic id. The span has
// to reach that topic on a click and on Enter, and every stamped id has to
// resolve — an id that does not is a link to nothing.
await page.goto(PAGE, { waitUntil: "load" });
const xrefIds = await page.evaluate(() =>
  [...document.querySelectorAll("script.domain-src")]
    .flatMap(s => [...s.textContent.matchAll(/data-xref="([^"]+)"/g)].map(m => m[1])));
check("cross-references are stamped with a topic id", xrefIds.length > 100,
  `${xrefIds.length} stamped`);
const xrefDead = await page.evaluate(ids => ids.filter(id => !topicDomain(id)), xrefIds);
check("every stamped cross-reference resolves", xrefDead.length === 0,
  xrefDead.slice(0, 3).join(" | "));

const xrefJump = await page.evaluate(async () => {
  // Open the domain that owns the first stamped cross-reference, then find it
  // in the live DOM — the spans live inside topic bodies, so the topic has to
  // be open before one is clickable.
  const src = [...document.querySelectorAll("script.domain-src")]
    .find(s => s.textContent.includes("data-xref="));
  const d = src.closest(".domain-section").dataset.domain;
  openDomain(domainSection(d));
  await new Promise(r => setTimeout(r, 200));
  document.querySelectorAll(".domain-body.open .topic-header")
    .forEach(h => { h.classList.add("open"); h.nextElementSibling.classList.add("open"); });
  const span = document.querySelector(".domain-body.open .xref[data-xref]");
  if (!span) return null;
  const want = span.dataset.xref;
  const focusable = span.getAttribute("tabindex") === "0" && span.getAttribute("role") === "link";
  span.click();
  await new Promise(r => setTimeout(r, 400));
  return { want, got: location.hash.slice(1), focusable,
           open: !!document.getElementById(want)?.querySelector(".topic-body")?.classList.contains("open") };
});
check("clicking a cross-reference opens the topic it names",
  !!xrefJump && xrefJump.got === xrefJump.want && xrefJump.open,
  xrefJump ? `${xrefJump.want} -> ${xrefJump.got} (open=${xrefJump.open})` : "none found");
check("a cross-reference is reachable by keyboard",
  !!xrefJump && xrefJump.focusable);

const xrefKey = await page.evaluate(async () => {
  const span = document.querySelector(".domain-body.open .topic-body.open .xref[data-xref]");
  if (!span) return null;
  const want = span.dataset.xref;
  // The click check above left the hash pointing at a topic. Clearing it first
  // is what makes this an assertion rather than a formality: with the hash
  // still set, a keydown handler that did nothing at all would pass.
  history.replaceState(null, "", location.pathname);
  span.focus();
  span.dispatchEvent(new KeyboardEvent("keydown",
    { key: "Enter", bubbles: true, cancelable: true }));
  await new Promise(r => setTimeout(r, 400));
  return { want, got: location.hash.slice(1) };
});
check("Enter on a focused cross-reference follows it",
  !!xrefKey && !!xrefKey.want && xrefKey.got === xrefKey.want,
  xrefKey ? `${xrefKey.want} -> ${xrefKey.got}` : "none found");

// ── study tooling: scheduler, acronym quiz, distractors, backup ─────────────
// Four features that shipped without any coverage. Each has a failure that is
// silent: a scheduler that stops writing records looks like "nothing is due",
// a quiz whose distractors come from the wrong pool looks like an easy quiz,
// and an export that drops a key looks like a smaller export.
await page.goto(PAGE, { waitUntil: "load" });

const srs = await page.evaluate(() => {
  localStorage.clear();
  const id = stIndex()[0].id;
  const first = srsGrade(id, "good");
  const second = srsGrade(id, "good");
  const third = srsGrade(id, "good");
  const badge = document.querySelector("#study-fab .study-badge")?.textContent ?? null;
  // A card graded three times is scheduled well past today, so it must not be
  // in the due count — that is the whole point of the interval.
  const dueAfter = srsDueCount();
  const failed = srsGrade(id, "again");
  return {
    id, first, second, third, badge, dueAfter,
    known: localStorage.getItem("known:" + id),
    failedInterval: failed.i, failedEase: failed.e, thirdEase: third.e,
    failedDue: failed.d, tomorrow: srsToday(1),
    dueNow: srsDueCount(),
  };
});
check("grading a card writes a scheduler record",
  !!srs && srs.first.i === 1 && typeof srs.first.d === "string" && srs.first.n === 1,
  JSON.stringify(srs?.first));
check("the interval grows across gradings",
  srs.second.i === 6 && srs.third.i > srs.second.i,
  `${srs.first.i} -> ${srs.second.i} -> ${srs.third.i} days`);
check("a graded card counts as known", srs.known === "1");
check("a scheduled card is not due today", srs.dueAfter === 0, `${srs.dueAfter} due`);
// The scheduler works in whole days, so "again" means tomorrow rather than
// later in this session — asserted as written, not as an SRS purist would want
// it. If that is ever changed, this is the check that should change with it.
check("'again' resets the interval and lowers the ease",
  srs.failedInterval === 1 && srs.failedEase < srs.thirdEase
  && srs.failedDue === srs.tomorrow && srs.dueNow === 0,
  `i=${srs.failedInterval}, ease ${srs.thirdEase} -> ${srs.failedEase}, due ${srs.failedDue}`);

const acroQ = await page.evaluate(() => {
  const qs = acroQuestions("__all", 8);
  const areas = acroAreas();
  const bad = qs.filter(q =>
    q.options.length !== 4 ||
    new Set(q.options.map(o => o.toLowerCase())).size !== 4 ||
    !q.options.includes(q.answer));
  // Same-area distractors are the claim the code makes; check it on an area
  // big enough that the fallback to the whole dictionary never kicks in.
  const big = areas.map(a => ({ a, n: acroQuestions(a, 3).length }))
    .filter(r => r.n === 3).slice(0, 3);
  return { count: qs.length, areas: areas.length, bad: bad.length, big: big.map(r => r.a) };
});
check("the acronym quiz builds questions from the dictionary",
  acroQ.count === 8 && acroQ.areas > 10, `${acroQ.count} questions, ${acroQ.areas} areas`);
check("every acronym question has four distinct options, one of them right",
  acroQ.bad === 0, `${acroQ.bad} malformed`);
check("a single subject area can fill a quiz on its own",
  acroQ.big.length === 3, acroQ.big.join(", "));

const distract = await page.evaluate(() => {
  const domain = [...document.querySelectorAll(".domain-section")]
    .map(s => s.dataset.domain).find(d => stTopicsForScope(d).length >= 8);
  if (!domain) return null;
  const stage = document.createElement("div");
  stStartQuiz(domain, stage);
  const ids = [...stage.querySelectorAll(".st-q-opt")].map(b => b.dataset.id);
  const owner = new Set(stTopicsForScope(domain).map(t => t.id));
  return { domain, options: ids.length, foreign: ids.filter(id => !owner.has(id)).length };
});
check("quiz distractors come from the scope that was chosen",
  !!distract && distract.options === 4 && distract.foreign === 0,
  distract ? `${distract.options} options, ${distract.foreign} from outside ${distract.domain}` : "no domain");

// The check above cannot fail on the "All domains" scope, which is the default
// and the one that was broken: inside one domain every option is same-domain by
// construction. This exercises the whole pool, where three names used to be
// drawn at random and a Kubernetes question came with tmux, GDPR and Ohm's law.
const spread = await page.evaluate(() => {
  const pool = stTopicsForScope("__all");
  let mixed = 0, dupes = 0;
  for (const q of pool) {
    const d = stDistractors(pool, q);
    if (d.length !== 3 || d.some(x => x.domainId !== q.domainId)) mixed++;
    if (d.some(x => x.id === q.id)) dupes++;
  }
  return { n: pool.length, mixed, dupes };
});
check("across all domains, a question's wrong answers are from its own subject",
  spread.mixed === 0 && spread.dupes === 0,
  `${spread.n} questions · ${spread.mixed} mixed · ${spread.dupes} with the answer as a distractor`);

const backup = await page.evaluate(() => {
  localStorage.clear();
  const ids = stIndex().slice(0, 3).map(t => t.id);
  localStorage.setItem("reviewed:" + ids[0], "1");
  localStorage.setItem("bookmark:" + ids[1], "1");
  srsGrade(ids[2], "good");
  localStorage.setItem("unrelated-key", "should not travel");
  const payload = bkExport();
  const text = JSON.stringify(payload);
  localStorage.clear();
  const vetted = bkValidate(text);
  const { kept, skipped } = bkSanitise(vetted.data);
  bkApply(kept, "replace");
  return {
    counts: payload.counts,
    carriedUnrelated: Object.keys(payload.data).includes("unrelated-key"),
    skipped,
    restored: {
      reviewed: localStorage.getItem("reviewed:" + ids[0]),
      bookmark: localStorage.getItem("bookmark:" + ids[1]),
      srs: !!localStorage.getItem("srs:" + ids[2]),
    },
  };
});
check("an export carries the progress keys and nothing else",
  backup.counts.reviewed === 1 && backup.counts.bookmark === 1 && backup.counts.srs === 1
  && !backup.carriedUnrelated,
  JSON.stringify(backup.counts));
check("an import restores what was exported",
  backup.restored.reviewed === "1" && backup.restored.bookmark === "1" && backup.restored.srs,
  JSON.stringify(backup.restored));

const rejects = await page.evaluate(() => {
  const out = {};
  const tryIt = (name, text) => {
    try { bkValidate(text); out[name] = "accepted"; }
    catch (e) { out[name] = "rejected"; }
  };
  tryIt("garbage", "not json at all");
  tryIt("wrongFormat", JSON.stringify({ format: "something-else", version: 1, data: {} }));
  tryIt("wrongVersion", JSON.stringify({ format: "techref-progress", version: 99, data: {} }));
  // A well-formed file carrying a key we do not own, and a malformed record.
  const { kept, skipped } = bkSanitise({ "evil-key": "x", "srs:abc": { d: "not-a-date" } });
  out.sanitised = `${Object.keys(kept).length} kept, ${skipped} refused`;
  return out;
});
check("a file that is not a progress export is refused",
  rejects.garbage === "rejected" && rejects.wrongFormat === "rejected"
  && rejects.wrongVersion === "rejected", JSON.stringify(rejects));
check("an import refuses keys and shapes it does not own",
  rejects.sanitised === "0 kept, 2 refused", rejects.sanitised);

await page.evaluate(() => localStorage.clear());

// ── learning paths ──────────────────────────────────────────────────────────
// A path drops steps it cannot resolve, so a broken path renders as a *shorter*
// path. That is the failure to guard: the rendered step count has to match the
// payload, and the progress has to track the same reviewed state the ✓ sets.
await page.goto(PAGE, { waitUntil: "load" });
const pathPayload = await page.evaluate(() => {
  const el = document.getElementById("learning-paths");
  try { return el ? JSON.parse(el.textContent) : null; } catch { return null; }
});
check("learning paths are inlined", Array.isArray(pathPayload) && pathPayload.length > 0,
  `${pathPayload ? pathPayload.length : 0} paths`);

const pathResolve = await page.evaluate(() => {
  const byId = new Set(stIndex().map(t => t.id));
  const bad = [];
  learningPaths().forEach(p =>
    (p.steps || []).forEach(s => { if (!byId.has(s)) bad.push(`${p.id}: ${s}`); }));
  return { bad, total: learningPaths().reduce((n, p) => n + p.steps.length, 0) };
});
check("every step in every path resolves to a topic",
  pathResolve.bad.length === 0, pathResolve.bad.slice(0, 3).join(" | "));

const pathUI = await page.evaluate(async () => {
  localStorage.clear();
  const p = learningPaths()[0];
  // Mark the first two steps reviewed, so progress has something to report.
  localStorage.setItem("reviewed:" + p.steps[0], "1");
  localStorage.setItem("reviewed:" + p.steps[1], "1");
  stOpenPaths();
  await new Promise(r => setTimeout(r, 200));
  const card = document.querySelector(`.st-path[data-id="${p.id}"]`);
  const listCount = card?.querySelector(".st-path-count")?.textContent || "";
  card?.querySelector(".st-path-open").click();
  await new Promise(r => setTimeout(r, 200));
  const steps = [...document.querySelectorAll(".st-path-step")];
  return {
    id: p.id,
    listCount,
    rendered: steps.length,
    declared: p.steps.length,
    done: steps.filter(li => li.classList.contains("done")).length,
    hereIndex: steps.findIndex(li => li.classList.contains("here")),
    hasContinue: !!document.getElementById("st-path-next"),
  };
});
check("a path renders every step it declares",
  pathUI.rendered === pathUI.declared, `${pathUI.rendered}/${pathUI.declared}`);
check("reviewed steps count as done",
  pathUI.done === 2 && pathUI.listCount.startsWith("2/"),
  `${pathUI.done} done, list said ${pathUI.listCount}`);
check("the first unreviewed step is marked as where you are",
  pathUI.hereIndex === 2 && pathUI.hasContinue, `here at index ${pathUI.hereIndex}`);

const pathJump = await page.evaluate(async () => {
  const btn = document.getElementById("st-path-next");
  const want = learningPaths()[0].steps[2];
  btn.click();
  await new Promise(r => setTimeout(r, 400));
  return { want, got: location.hash.slice(1),
           open: !!document.getElementById(want)?.querySelector(".topic-body")?.classList.contains("open") };
});
check("Continue opens the step you are on",
  pathJump.got === pathJump.want && pathJump.open,
  `${pathJump.want} -> ${pathJump.got}`);
await page.evaluate(() => localStorage.clear());

// ── per-topic notes ─────────────────────────────────────────────────────────
// A note that saves but never reappears, or reappears but never exports, are
// both silent — the reader only finds out when the note is gone.
await page.goto(PAGE, { waitUntil: "load" });
const note = await page.evaluate(async () => {
  localStorage.clear();
  const first = [...document.querySelectorAll(".domain-section")][0].dataset.domain;
  openDomain(domainSection(first));
  await new Promise(r => setTimeout(r, 250));
  const topic = document.querySelector(".domain-body.open .topic");
  topic.querySelector(".topic-note-btn").click();
  await new Promise(r => setTimeout(r, 150));
  const input = topic.querySelector(".topic-note .tn-input");
  const opened = !!input && !input.hidden;
  input.value = "check this against the lab build";
  input.dispatchEvent(new Event("blur"));
  await new Promise(r => setTimeout(r, 100));
  return {
    id: topic.id, opened,
    stored: localStorage.getItem("note:" + topic.id),
    shown: topic.querySelector(".topic-note .tn-text")?.textContent,
    inputHidden: topic.querySelector(".topic-note .tn-input")?.hidden,
    flagged: topic.classList.contains("noted"),
    // The note must be the first thing in the body, above the concept cards.
    first: topic.querySelector(":scope > .topic-body").firstElementChild
             ?.classList.contains("topic-note"),
  };
});
check("the note button opens an editor on the topic", note.opened);
check("a note is saved, shown and flagged on the topic",
  note.stored === "check this against the lab build"
  && note.shown === note.stored && note.inputHidden && note.flagged,
  `stored=${JSON.stringify(note.stored)} flagged=${note.flagged}`);
check("the note sits above the concept cards", note.first === true);

const noteBack = await page.evaluate(async () => {
  const id = [...document.querySelectorAll(".topic")].find(t => t.classList.contains("noted"))?.id;
  // Close and reopen the domain: the note lives in storage, not in the DOM that
  // just got thrown away.
  const section = domainSection(topicDomain(id));
  closeDomain(section);
  openDomain(section);
  await new Promise(r => setTimeout(r, 250));
  document.getElementById(id).querySelector(".topic-header").click();
  await new Promise(r => setTimeout(r, 200));
  return document.getElementById(id)?.querySelector(".topic-note .tn-text")?.textContent || "";
});
check("a note survives the domain being evicted and reopened",
  noteBack === "check this against the lab build", noteBack);

const noteBackup = await page.evaluate(() => {
  const payload = bkExport();
  const noteKeys = Object.keys(payload.data).filter(k => k.startsWith("note:"));
  localStorage.clear();
  const { kept } = bkSanitise(bkValidate(JSON.stringify(payload)).data);
  bkApply(kept, "replace");
  const restored = noteKeys.map(k => localStorage.getItem(k));
  // And a note shape the page does not accept must be refused, like any other.
  const bad = bkSanitise({ "note:x": 42, "note:y": "   " });
  return { counted: payload.counts.topicNote, noteKeys: noteKeys.length,
           restored, refused: bad.skipped };
});
check("notes travel in the progress export",
  noteBackup.counted === 1 && noteBackup.noteKeys === 1,
  `counted ${noteBackup.counted}, ${noteBackup.noteKeys} keys`);
check("notes come back on import",
  noteBackup.restored[0] === "check this against the lab build", noteBackup.restored[0]);
check("a note that is not a usable string is refused on import",
  noteBackup.refused === 2, `${noteBackup.refused} refused`);

const noteGone = await page.evaluate(async () => {
  const id = [...document.querySelectorAll(".topic")].find(t => t.classList.contains("noted"))?.id;
  const topic = document.getElementById(id);
  topic.querySelector(".topic-note .tn-edit").click();
  topic.querySelector(".topic-note .tn-clear").click();
  await new Promise(r => setTimeout(r, 120));
  return { stored: localStorage.getItem("note:" + id),
           block: !!topic.querySelector(".topic-note"),
           flagged: topic.classList.contains("noted") };
});
check("deleting a note removes the block and the flag",
  noteGone.stored === null && !noteGone.block && !noteGone.flagged,
  JSON.stringify(noteGone));
await page.evaluate(() => localStorage.clear());

// ── progress dashboard and streak ───────────────────────────────────────────
// The dashboard has to report on all thirty domains while at most one is in
// the DOM — a version that counted rendered .topic elements would report on a
// thirtieth of the site and look perfectly healthy.
await page.goto(PAGE, { waitUntil: "load" });
const dash = await page.evaluate(async () => {
  localStorage.clear();
  const idx = topicIndex();
  const domains = Object.keys(idx);
  // Plant state in three domains, none of which is open.
  const planted = domains.slice(0, 3);
  planted.forEach((d, i) => {
    idx[d].slice(0, i + 1).forEach(id => localStorage.setItem("reviewed:" + id, "1"));
  });
  localStorage.setItem("bookmark:" + idx[planted[0]][0], "1");
  localStorage.setItem("note:" + idx[planted[1]][0], "a note");
  const stats = progressStats();
  const byId = Object.fromEntries(stats.rows.map(r => [r.id, r]));
  return {
    domains: stats.rows.length,
    siteTotal: stats.all.total,
    indexedTotal: Object.values(idx).reduce((n, a) => n + a.length, 0),
    reviewed: stats.all.reviewed,
    perDomain: planted.map(d => byId[d].reviewed),
    starred: stats.all.bookmarked,
    noted: stats.all.noted,
    inDom: document.querySelectorAll(".domain-body .topic").length,
  };
});
check("the dashboard covers every domain and every topic",
  dash.domains > 25 && dash.siteTotal === dash.indexedTotal,
  `${dash.domains} domains, ${dash.siteTotal} topics`);
check("it reports state from domains that are not in the DOM",
  dash.reviewed === 6 && dash.perDomain.join(",") === "1,2,3" && dash.inDom === 0,
  `${dash.reviewed} reviewed with ${dash.inDom} topics rendered`);
check("stars and notes are counted too",
  dash.starred === 1 && dash.noted === 1, `${dash.starred} starred, ${dash.noted} noted`);

const streak = await page.evaluate(async () => {
  localStorage.clear();
  const out = {};
  // A fresh day: any action starts a run of one, and repeating it does not
  // inflate the count.
  streakTouch(); streakTouch();
  out.today = streakCurrent();
  // Yesterday's run continues; a gap starts over; an old run is not "current".
  localStorage.setItem("study-streak", JSON.stringify({ last: srsToday(-1), n: 4, best: 9 }));
  streakTouch();
  out.continued = streakGet().n;
  localStorage.setItem("study-streak", JSON.stringify({ last: srsToday(-5), n: 4, best: 9 }));
  out.staleReads = streakCurrent();
  streakTouch();
  out.afterGap = streakGet().n;
  out.best = streakGet().best;
  return out;
});
check("a day of activity counts once", streak.today === 1, `${streak.today}`);
check("yesterday's streak continues", streak.continued === 5, `${streak.continued}`);
check("a lapsed streak reads as zero and starts over",
  streak.staleReads === 0 && streak.afterGap === 1,
  `current ${streak.staleReads}, restarted at ${streak.afterGap}`);
check("the best run is remembered", streak.best === 9, `${streak.best}`);

const streakTravel = await page.evaluate(() => {
  localStorage.clear();
  localStorage.setItem("study-streak", JSON.stringify({ last: srsToday(), n: 3, best: 11 }));
  const payload = bkExport();
  localStorage.clear();
  const { kept } = bkSanitise(bkValidate(JSON.stringify(payload)).data);
  bkApply(kept, "replace");
  const bad = bkSanitise({ "study-streak": { last: "yesterday", n: 3 } });
  return { restored: streakGet(), refused: bad.skipped };
});
check("the streak survives an export and import",
  streakTravel.restored.n === 3 && streakTravel.restored.best === 11,
  JSON.stringify(streakTravel.restored));
check("a malformed streak record is refused on import",
  streakTravel.refused === 1, `${streakTravel.refused} refused`);
await page.evaluate(() => localStorage.clear());

// ── exam mode ───────────────────────────────────────────────────────────────
// The mode is defined by what it withholds, so that is what gets asserted:
// a fixed length, no marking until the end, and a report that names the topics
// to go back to.
await page.goto(PAGE, { waitUntil: "load" });
const exam = await page.evaluate(async () => {
  localStorage.clear();
  stOpenExam();
  await new Promise(r => setTimeout(r, 150));
  document.getElementById("st-ex-count").value = "10";
  document.getElementById("st-ex-start").click();
  await new Promise(r => setTimeout(r, 200));
  const stage = document.getElementById("st-ex-stage");
  const clock = document.getElementById("st-ex-clock")?.textContent || "";
  const first = stage.querySelector(".st-q-opt");
  const optionCount = stage.querySelectorAll(".st-q-opt").length;
  // Answer the first question deliberately wrong, and check nothing is marked.
  const wrong = [...stage.querySelectorAll(".st-q-opt")]
    .find(b => b.dataset.id !== _examState.questions[0].answer);
  wrong.click();
  await new Promise(r => setTimeout(r, 100));
  const marked = stage.querySelectorAll(".correct, .incorrect, .st-q-feedback").length;
  return { clock, optionCount, length: _examState.questions.length, marked,
           movedOn: _examState.i === 1, hasFirst: !!first };
});
check("an exam is a fixed number of questions with a clock",
  exam.length === 10 && /^\d+:\d\d$/.test(exam.clock), `${exam.length} questions, clock ${exam.clock}`);
check("each question offers four options", exam.optionCount === 4, `${exam.optionCount}`);
check("answering marks nothing and moves on",
  exam.marked === 0 && exam.movedOn, `${exam.marked} marks shown`);

const examDistract = await page.evaluate(() => {
  // With "all domains" selected, distractors still have to come from the
  // question's own domain — otherwise the odd one out is obvious.
  const qs = examBuild("__all", 20);
  const foreign = qs.filter(q => {
    const home = q.domainId;
    return q.options.filter(o => topicDomain(o.id) !== home).length > 0;
  });
  return { built: qs.length, foreign: foreign.length };
});
check("distractors come from the question's own domain",
  examDistract.built === 20 && examDistract.foreign === 0,
  `${examDistract.foreign} of ${examDistract.built} questions drew from elsewhere`);

const examReport = await page.evaluate(async () => {
  // Answer the rest: every question right except the first, which is already
  // wrong, plus one left blank.
  const s = _examState;
  for (let i = 1; i < s.questions.length - 1; i++) s.answers[i] = s.questions[i].answer;
  const r = stExamFinish();
  await new Promise(res => setTimeout(res, 150));
  const stage = document.getElementById("st-ex-stage");
  const rows = stage.querySelectorAll(".st-ex-table tbody tr").length;
  const missedLinks = [...stage.querySelectorAll(".st-list-link")].map(b => b.dataset.id);
  stage.querySelector("#st-ex-star").click();
  await new Promise(res => setTimeout(res, 100));
  return {
    score: r.score, total: r.total, missed: r.missed.length,
    skipped: r.missed.filter(m => m.skipped).length,
    rows, missedLinks,
    starred: missedLinks.filter(id => localStorage.getItem("bookmark:" + id) === "1").length,
    timerStopped: _examState.timer === null,
    // Weakest domain first — the report is a to-do list, not a scoreboard.
    ordered: r.domains.every((d, i, a) =>
      i === 0 || (a[i - 1].right / a[i - 1].n) <= (d.right / d.n)),
  };
});
check("the exam scores what was answered and counts what was skipped",
  examReport.score === examReport.total - 2 && examReport.missed === 2
  && examReport.skipped === 1,
  `${examReport.score}/${examReport.total}, ${examReport.missed} missed, ${examReport.skipped} blank`);
check("the report breaks down by domain, weakest first",
  examReport.rows > 0 && examReport.ordered, `${examReport.rows} domain rows`);
check("every missed topic is linked back",
  examReport.missedLinks.length === examReport.missed, `${examReport.missedLinks.length} links`);
check("'star all of these' adds the missed topics to the study list",
  examReport.starred === examReport.missed, `${examReport.starred} starred`);
check("finishing stops the clock", examReport.timerStopped);

const examClosed = await page.evaluate(async () => {
  stOpenExam();
  await new Promise(r => setTimeout(r, 120));
  document.getElementById("st-ex-start").click();
  await new Promise(r => setTimeout(r, 150));
  const running = _examState?.timer !== null;
  stClose();
  await new Promise(r => setTimeout(r, 120));
  return { running, cleared: _examState === null };
});
// An interval outlives the modal that owns it; left running it would submit a
// paper nobody is sitting.
check("closing the modal stops the exam clock",
  examClosed.running && examClosed.cleared, JSON.stringify(examClosed));
await page.evaluate(() => localStorage.clear());

// ── the study index reaches every topic ─────────────────────────────────────
// stIndex() drops any topic it cannot parse a name for, and everything the
// study tools offer is built from it: decks, quizzes, the palette, paths,
// related topics. A topic that falls out is not broken — it is *absent*, from
// every one of those, silently. 41 topics in this repo write their name span
// across two lines (`<span class="topic-name"\n  >…`), which is exactly the
// shape a naive parser misses.
await page.goto(PAGE, { waitUntil: "load" });
const indexReach = await page.evaluate(() => {
  const idx = topicIndex();
  const have = new Map(stIndex().map(t => [t.id, t]));
  const missing = [];
  const unnamed = [];
  Object.keys(idx).forEach(d => idx[d].forEach(id => {
    const row = have.get(id);
    if (!row) missing.push(`${d}:${id}`);
    else if (!row.name || !row.name.trim()) unnamed.push(`${d}:${id}`);
  }));
  return {
    total: Object.values(idx).reduce((n, a) => n + a.length, 0),
    indexed: have.size, missing: missing.slice(0, 5), missingN: missing.length,
    unnamed: unnamed.slice(0, 5), unnamedN: unnamed.length,
  };
});
check("every indexed topic reaches the study index",
  indexReach.missingN === 0 && indexReach.indexed === indexReach.total,
  `${indexReach.indexed}/${indexReach.total}` +
  (indexReach.missingN ? ` — missing ${indexReach.missing.join(", ")}` : ""));
check("every topic in the study index has a name",
  indexReach.unnamedN === 0, indexReach.unnamed.join(", "));

// ── markdown export ─────────────────────────────────────────────────────────
// The conversion runs over the deferred blocks, so it has to work for a domain
// that has never been opened — which is the case a live-DOM implementation
// would silently fail on.
await page.goto(PAGE, { waitUntil: "load" });
const md = await page.evaluate(() => {
  // A topic with a table and one with a code block, from a domain nobody opened.
  // A real table, not a `<table` inside a code sample — which is what the
  // first match on the bare string turned out to be.
  const withTable = stIndex().find(t => topicHtml(t.id).includes('class="ref-table"'));
  const withCode = stIndex().find(t => /<pre[^>]*>/.test(topicHtml(t.id)));
  const one = mdForTopicHtml(topicHtml(withTable.id));
  const code = withCode ? mdForTopicHtml(topicHtml(withCode.id)) : "";
  return {
    domainsInDom: document.querySelectorAll(".domain-body .topic").length,
    name: withTable.name,
    heading: one.split("\n").find(l => l.startsWith("## ")) || "",
    hasCardHeading: /^### /m.test(one),
    hasTable: /^\| .* \|$/m.test(one) && /^\| ---/m.test(one),
    // Per contiguous run: a topic legitimately holds several tables of
    // different widths, and lumping their rows together only proves that.
    // Per contiguous run: a topic legitimately holds several tables of
    // different widths, and lumping their rows together only proves that.
    tableRowsSquare: (() => {
      const runs = [];
      let run = null;
      one.split("\n").forEach(l => {
        if (l.startsWith("|")) { if (!run) { run = []; runs.push(run); } run.push(l); }
        else run = null;
      });
      const real = runs.filter(r => r.length > 2);
      return real.length > 0 && real.every(r => new Set(r.map(x => x.split("|").length)).size === 1);
    })(),
    tableHeaderFilled: (() => {
      const lines = one.split("\n");
      const sep = lines.findIndex(l => /^\| ---/.test(l));
      return sep > 0 && /[A-Za-z0-9]/.test(lines[sep - 1]);
    })(),
    hasFence: /```/.test(code),
    noTags: !/<[a-z][^>]*>/i.test(one),
    noChevron: !one.includes("▶"),
  };
});
check("markdown export works on domains that are not in the DOM",
  md.domainsInDom === 0 && md.heading.length > 3, `${md.domainsInDom} topics rendered`);
// The heading keeps its inline acronym expansions on purpose: an exported file
// has no hover, so the expansion has to be in the text or it is lost.
check("a topic exports as a heading with its concept cards",
  md.heading.startsWith("## ") && md.heading.includes(md.name.split(" ")[0])
  && md.hasCardHeading, md.heading);
check("reference tables become markdown tables with square rows",
  md.hasTable && md.tableRowsSquare);
// Most tables here have no <thead>; the header is a bare <tr> of <th>. Keying
// off <thead> silently emitted an empty header row on every table on the site.
check("a table's header row carries its headings",
  md.tableHeaderFilled);
check("code blocks become fenced blocks", md.hasFence);
check("no markup or chrome survives the conversion",
  md.noTags && md.noChevron, `tags=${!md.noTags} chevron=${!md.noChevron}`);

const mdScope = await page.evaluate(async () => {
  stOpenExport();
  await new Promise(r => setTimeout(r, 200));
  const sel = document.getElementById("st-md-scope");
  const domain = [...sel.options].map(o => o.value).find(v => !v.startsWith("__"));
  sel.value = domain;
  document.getElementById("st-md-go").click();
  await new Promise(r => setTimeout(r, 400));
  const text = document.getElementById("st-md-out").value;
  const expected = stTopicsForScope(domain).length;
  return {
    domain, expected,
    headings: (text.match(/^## /gm) || []).length,
    size: text.length,
    sizeLine: document.getElementById("st-md-size").textContent,
    copyEnabled: !document.getElementById("st-md-copy").disabled,
  };
});
check("exporting a domain emits one heading per topic",
  mdScope.headings === mdScope.expected,
  `${mdScope.headings}/${mdScope.expected} in ${mdScope.domain}`);
check("the export reports its size and enables the buttons",
  /\d+ topics · \d+ KB/.test(mdScope.sizeLine) && mdScope.copyEnabled, mdScope.sizeLine);

// ── update toast ────────────────────────────────────────────────────────────
// The service worker only runs over http(s) and these tests run over file://,
// so the registration path cannot be exercised here. What can be — and what
// actually breaks — is the toast itself: that it renders once, asks the waiting
// worker to take over, and can be dismissed.
await page.goto(PAGE, { waitUntil: "load" });
const toast = await page.evaluate(() => {
  const messages = [];
  const fakeWorker = { postMessage: m => messages.push(m) };
  const first = showUpdateToast(fakeWorker);
  const second = showUpdateToast(fakeWorker);      // must not stack
  const bar = document.getElementById("update-toast");
  const out = {
    rendered: !!first, secondSuppressed: second === null,
    count: document.querySelectorAll("#update-toast").length,
    role: bar.getAttribute("role"),
    text: bar.querySelector(".ut-text").textContent,
  };
  bar.querySelector(".ut-go").click();
  out.messages = messages;
  out.buttonBusy = bar.querySelector(".ut-go").textContent;
  bar.querySelector(".ut-dismiss").click();
  out.dismissed = !document.getElementById("update-toast");
  return out;
});
check("the update toast renders once, not once per event",
  toast.rendered && toast.secondSuppressed && toast.count === 1, `${toast.count} toasts`);
check("it is announced to assistive tech", toast.role === "status", toast.role);
check("accepting asks the waiting worker to take over",
  JSON.stringify(toast.messages) === '[{"type":"skip-waiting"}]' && /Reloading/.test(toast.buttonBusy),
  JSON.stringify(toast.messages));
check("it can be dismissed", toast.dismissed);

// ── print packs ─────────────────────────────────────────────────────────────
// The pack is generated into a container of its own, because only one domain
// is ever hydrated and a learning path spans several — "print what is
// rendered" could never produce the pack most worth printing.
await page.goto(PAGE, { waitUntil: "load" });
const pack = await page.evaluate(() => {
  // A path that actually crosses domains — the first one is all `net`, and
  // testing on that would prove nothing about the case this design exists for.
  const path = learningPaths().find(p =>
    new Set(pathSteps(p).map(t => t.domainId)).size > 1) || learningPaths()[0];
  const rows = pathSteps(path);
  const domains = new Set(rows.map(t => t.domainId));
  buildPrintPack(rows, path.name);
  const host = document.getElementById("print-pack");
  const out = {
    steps: rows.length,
    domainsSpanned: domains.size,
    inDom: document.querySelectorAll(".domain-body .topic").length,
    sections: host.querySelectorAll(".pp-topic").length,
    openBodies: host.querySelectorAll(".topic-body.open").length,
    closedBodies: host.querySelectorAll(".topic-body:not(.open)").length,
    numbered: host.querySelector(".pp-n")?.textContent,
    printingClass: document.body.classList.contains("printing"),
    hiddenOnScreen: getComputedStyle(host).display,
  };
  clearPrintPack();
  out.cleared = !document.getElementById("print-pack")
    && !document.body.classList.contains("printing");
  return out;
});
check("a print pack spans a whole learning path",
  pack.sections === pack.steps && pack.domainsSpanned > 1,
  `${pack.sections}/${pack.steps} topics across ${pack.domainsSpanned} domains`);
check("it is built without hydrating those domains",
  pack.inDom === 0, `${pack.inDom} topics rendered`);
check("every card in the pack is open",
  pack.openBodies === pack.steps && pack.closedBodies === 0,
  `${pack.openBodies} open, ${pack.closedBodies} closed`);
check("steps are numbered, and the pack is invisible on screen",
  pack.numbered === "1" && pack.hiddenOnScreen === "none" && pack.printingClass,
  `n=${pack.numbered} display=${pack.hiddenOnScreen}`);
check("the pack is removed after printing", pack.cleared);

// ── link preview metadata ───────────────────────────────────────────────────
// The counts in the description are written by hand and the ones on the card
// are generated, so they can drift apart. A preview that advertises a number
// the site no longer has is the kind of wrong nobody notices for a year.
const preview = await page.evaluate(() => {
  const get = sel => document.querySelector(sel)?.getAttribute("content") || "";
  return {
    description: get('meta[name="description"]'),
    ogTitle: get('meta[property="og:title"]'),
    ogImage: get('meta[property="og:image"]'),
    ogDesc: get('meta[property="og:description"]'),
    twitter: get('meta[name="twitter:card"]'),
    topics: Object.values(topicIndex()).reduce((n, a) => n + a.length, 0),
    domains: document.querySelectorAll(".domain-section").length,
  };
});
check("the page carries link preview metadata",
  preview.ogTitle && preview.ogImage.endsWith("/Img/og-card.png")
  && preview.twitter === "summary_large_image" && preview.description.length > 60,
  preview.ogImage);
const asWritten = n => n.toLocaleString("en");
check("the preview text quotes the site's real size",
  preview.description.includes(asWritten(preview.topics))
  && preview.description.includes(`${preview.domains} domains`)
  && preview.ogDesc.includes(asWritten(preview.topics)),
  `${asWritten(preview.topics)} topics, ${preview.domains} domains`);

// ── the alias map moves progress, including notes ───────────────────────────
// Both halves of this were broken and neither was covered. `note:` was missing
// from the migrated prefixes, so a merged topic silently discarded the one
// piece of progress a reader writes by hand; and the run-once flag was a
// boolean, so an alias added later never migrated on a device that had already
// visited — which is every device, for every future topic merge.
await step("the alias map migrates progress onto the current id", async () => {
  const outcome = await page.evaluate(() => {
    const aliases = JSON.parse(document.getElementById("slug-aliases").textContent);
    const [old] = Object.keys(aliases);
    if (!old) return { skipped: true };
    const now = aliases[old];
    const prefixes = ["reviewed:", "bookmark:", "known:", "srs:", "note:"];
    prefixes.forEach(p => { localStorage.removeItem(p + old); localStorage.removeItem(p + now); });
    Object.keys(localStorage)
      .filter(k => k.startsWith("migrated:slug-aliases"))
      .forEach(k => localStorage.removeItem(k));

    localStorage.setItem("reviewed:" + old, "2026-01");
    localStorage.setItem("note:" + old, "a note the reader wrote");
    const moved = migrateAliasedProgress();

    const result = {
      moved,
      reviewed: localStorage.getItem("reviewed:" + now),
      note: localStorage.getItem("note:" + now),
      oldCleared: localStorage.getItem("note:" + old) === null,
      // A second call with the same map must do nothing.
      secondRun: migrateAliasedProgress(),
      flags: Object.keys(localStorage).filter(k => k.startsWith("migrated:slug-aliases")).length,
    };
    prefixes.forEach(p => localStorage.removeItem(p + now));
    return result;
  });
  if (outcome.skipped) return check("the alias map migrates progress onto the current id",
    true, "no aliases to test");
  check("the alias map migrates progress onto the current id",
    outcome.reviewed === "2026-01" && outcome.oldCleared, `moved ${outcome.moved}`);
  check("a note survives the move, which is the one it used to lose",
    outcome.note === "a note the reader wrote", outcome.note || "lost");
  check("a second run with an unchanged map is a no-op",
    outcome.secondRun === 0 && outcome.flags === 1, `${outcome.secondRun} moved, ${outcome.flags} flag(s)`);
});

// ── what's new since your last visit ────────────────────────────────────────
// plan.md Phase 10 T8. Four behaviours, and the first is the one most likely to
// be got wrong: a reader with nothing stored must be told nothing at all.
await step("what's new stays quiet on a first visit and records the month", async () => {
  const first = await page.evaluate(() => {
    localStorage.removeItem("seen-through");
    initWhatsNew();
    return { hidden: document.getElementById("whatsnew").hidden,
             seen: localStorage.getItem("seen-through") };
  });
  check("a first-time reader is not told the whole site is new",
    first.hidden === true && /^\d{4}-\d{2}$/.test(first.seen || ""),
    `hidden ${first.hidden}, stored ${first.seen}`);

  const back = await page.evaluate(() => {
    localStorage.setItem("seen-through", "2026-06");
    document.getElementById("whatsnew").hidden = true;
    initWhatsNew();
    return { hidden: document.getElementById("whatsnew").hidden,
             text: document.getElementById("whatsnew-text").textContent };
  });
  check("a returning reader is told how many topics changed",
    back.hidden === false && /\d+ topics? updated since /.test(back.text), back.text);

  const shown = await page.evaluate(() => {
    document.getElementById("whatsnew-show").click();
    return document.getElementById("search-input").value;
  });
  check("'show them' puts an editable query in the search box",
    shown === "since:2026-06", shown);

  const seen = await page.evaluate(() => {
    document.getElementById("whatsnew-seen").click();
    const s = localStorage.getItem("seen-through");
    localStorage.removeItem("seen-through");
    return { hidden: document.getElementById("whatsnew").hidden, seen: s };
  });
  check("'mark as seen' advances the stored month and hides the banner",
    seen.hidden === true && seen.seen > "2026-06", `stored ${seen.seen}`);
});

// ── hygiene ─────────────────────────────────────────────────────────────────
check("no console errors", consoleErrors.length === 0, consoleErrors.slice(0, 2).join(" | "));
check("no off-site requests", offsite.length === 0, offsite.slice(0, 2).join(" | "));

await browser.close();

const failed = results.filter(r => !r.pass);
console.log(`\n${results.length - failed.length}/${results.length} checks passed.`);
process.exit(failed.length ? 1 : 0);
