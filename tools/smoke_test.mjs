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

// ── structure ───────────────────────────────────────────────────────────────
const structure = await page.evaluate(() => {
  const chips = [...document.querySelectorAll(".chip[data-domain]")].map(c => c.dataset.domain);
  const sections = [...document.querySelectorAll("[data-domain]")]
    .filter(e => !e.classList.contains("chip")).map(e => e.dataset.domain);
  return { chips, sections, topics: document.querySelectorAll(".topic").length };
});
// Every chip must have a section and vice versa: a domain removed from one and
// left in the other is exactly the breakage a fold causes, and it is silent.
const chipSet = new Set(structure.chips.filter(d => d !== "all"));
const secSet = new Set(structure.sections);
const orphanChips = [...chipSet].filter(d => !secSet.has(d));
const orphanSections = [...secSet].filter(d => !chipSet.has(d));
check("every filter chip has a domain section", orphanChips.length === 0, orphanChips.join(", "));
check("every domain section has a filter chip", orphanSections.length === 0, orphanSections.join(", "));
check("topics present", structure.topics > 0, `${structure.topics} topics, ${secSet.size} domains`);

// ── every topic has a unique, non-empty id (permalinks depend on it) ────────
const ids = await page.evaluate(() =>
  [...document.querySelectorAll(".topic")].map(t => t.id));
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
await page.goto(PAGE, { waitUntil: "load" });
await page.fill("#search-input", "kerberos");
await page.waitForTimeout(350);
const searchHits = await page.evaluate(() =>
  [...document.querySelectorAll(".topic")].filter(t => t.offsetParent !== null).length);
check("search narrows the page", searchHits > 0 && searchHits < 200, `${searchHits} visible`);
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

// ── theming: every marked volatile claim, and the topology diagrams ─────────
const themed = async () => page.evaluate(() => {
  const g = el => el ? getComputedStyle(el) : null;
  const line = g(document.querySelector(".topo-svg line"));
  const circ = g(document.querySelector(".topo-svg circle"));
  const vol = g(document.querySelector(".volatile"));
  return {
    body: getComputedStyle(document.body).backgroundColor,
    line: line?.stroke, circle: circ?.fill, volatile: vol?.borderBottomColor,
  };
});
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
await page.locator(".domain-body.open .topic-header").first().focus();
await page.keyboard.press("Enter");
await page.waitForTimeout(300);
const kbTopic = await page.evaluate(() =>
  document.querySelector(".domain-body.open .topic-header")?.getAttribute("aria-expanded"));
check("Enter opens a topic and sets aria-expanded", kbTopic === "true", `aria-expanded=${kbTopic}`);

// ── hygiene ─────────────────────────────────────────────────────────────────
check("no console errors", consoleErrors.length === 0, consoleErrors.slice(0, 2).join(" | "));
check("no off-site requests", offsite.length === 0, offsite.slice(0, 2).join(" | "));

await browser.close();

const failed = results.filter(r => !r.pass);
console.log(`\n${results.length - failed.length}/${results.length} checks passed.`);
process.exit(failed.length ? 1 : 0);
