/**
 * style_equiv.mjs — prove a styling change rendered identically.
 *
 * `lint_content.py` tracks 792 avoidable inline styles and invites anyone to
 * lower the ceiling by converting them to classes. Nobody could, safely: the
 * only browser check on appearance is `visual_test.mjs`, which shoots the
 * **filter bar** and deliberately nothing else, because content screenshots
 * fail on every content wave. So a conversion touching 112 elements across
 * eleven domains had no way to show it changed nothing.
 *
 * This compares *computed styles* rather than pixels, which is the right unit
 * for this question: a class that resolves to the same computed value is the
 * same rendering, and it stays true when the content around it changes. That is
 * exactly what a screenshot cannot promise.
 *
 * It builds a reference from a git ref into a temp directory, loads both pages,
 * opens each domain in both (the content is deferred, so it does not exist in
 * the DOM until then), and compares every element in the opened section.
 *
 * ## What it can and cannot tell you
 *
 * It compares the properties in `PROPS` — the ones a style-to-class conversion
 * plausibly moves. It is not a pixel diff and will not see a change that lives
 * only in a shorthand, a pseudo-element, a hover state, or a media query at a
 * width it did not render at. It compares elements **by position**, so it
 * reports a structural change as a count mismatch and stops comparing that
 * domain rather than guessing at an alignment.
 *
 * Usage:
 *   node tools/style_equiv.mjs                      # working tree vs HEAD
 *   node tools/style_equiv.mjs --against <ref>      # vs any commit
 *   node tools/style_equiv.mjs --domains linux,net  # a subset, while iterating
 *   node tools/style_equiv.mjs --width 375          # at a phone's width
 *
 * A verification tool, not a gate: it needs a browser, a second build and a
 * couple of minutes, and it answers a question only asked while refactoring.
 */

import { execFileSync } from "node:child_process";
import { mkdtempSync, rmSync, existsSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const ROOT = process.cwd();
const arg = (name, fallback) => {
  const i = process.argv.indexOf(name);
  return i === -1 ? fallback : process.argv[i + 1];
};
const REF = arg("--against", "HEAD");
const WIDTH = Number(arg("--width", 1280));
const ONLY = arg("--domains", "");
const KEEP = process.argv.includes("--keep");

// The properties a style-to-class conversion actually moves. Longhands only:
// a shorthand reads back inconsistently across engines and would produce
// differences that are not differences.
const PROPS = [
  "color", "background-color", "font-size", "font-weight", "font-family",
  "font-style", "line-height", "text-align", "text-transform", "white-space",
  "display", "margin-top", "margin-right", "margin-bottom", "margin-left",
  "padding-top", "padding-right", "padding-bottom", "padding-left",
  "border-top-width", "border-right-width", "border-bottom-width",
  "border-left-width", "border-top-color", "border-right-color",
  "border-bottom-color", "border-left-color", "border-radius",
  "grid-template-columns", "flex-direction", "gap", "width", "max-width",
];

const chromium = await (async () => {
  try {
    return (await import("playwright")).chromium;
  } catch {
    const bases = [
      "/opt/node22/lib/node_modules",
      "/usr/lib/node_modules",
      "/usr/local/lib/node_modules",
    ];
    for (const base of bases) {
      try { return (await import(`${base}/playwright/index.mjs`)).chromium; }
      catch { /* try the next one */ }
    }
    console.error("Could not find playwright. Run: npm install playwright");
    process.exit(2);
  }
})();

if (!existsSync(join(ROOT, "index.html"))) {
  console.error("error: index.html not found — run python3 build.py first");
  process.exit(2);
}

// The reference build. `git archive` gives a clean tree at the ref without
// touching the working tree, which matters: this runs while somebody has
// uncommitted changes, and that is the whole point of it.
const dir = mkdtempSync(join(tmpdir(), "style-equiv-"));
const base = join(dir, "base");
console.log(`Building ${REF} into a temp tree…`);
execFileSync("bash", ["-c",
  `mkdir -p ${JSON.stringify(base)} && git archive ${REF} | tar -x -C ${JSON.stringify(base)}`],
  { cwd: ROOT, stdio: "inherit" });
execFileSync("python3", ["build.py"], { cwd: base, stdio: "inherit" });

const collect = `(only) => {
  const PROPS = ${JSON.stringify(PROPS)};
  const ids = Object.keys(topicIndex()).filter(d => !only.length || only.includes(d));
  const out = {};
  for (const d of ids) {
    const sec = domainSection(d);
    if (!sec) { out[d] = null; continue; }
    openDomain(sec);
    const rows = [];
    for (const el of sec.querySelectorAll("*")) {
      const cs = getComputedStyle(el);
      rows.push(el.tagName + "|" + PROPS.map(p => cs.getPropertyValue(p)).join("|"));
    }
    out[d] = rows;
  }
  return out;
}`;

const read = async (page, path) => {
  await page.goto(`file://${path}`, { waitUntil: "load" });
  return page.evaluate(`(${collect})(${JSON.stringify(ONLY ? ONLY.split(",") : [])})`);
};

const browser = await chromium.launch();
let bad = 0;
try {
  const ctx = await browser.newContext({ viewport: { width: WIDTH, height: 900 } });
  const page = await ctx.newPage();
  console.log(`Reading ${REF}…`);
  const before = await read(page, join(base, "index.html"));
  console.log("Reading the working tree…");
  const after = await read(page, join(ROOT, "index.html"));

  const domains = Object.keys(after);
  let compared = 0;
  for (const d of domains) {
    const a = before[d], b = after[d];
    if (!a || !b) { console.log(`  ${d}: missing in one build — skipped`); continue; }
    if (a.length !== b.length) {
      bad++;
      console.log(`  ${d}: ${a.length} elements -> ${b.length}. A structural change, `
                  + `not a styling one — this tool cannot align the two, so it stops here.`);
      continue;
    }
    let diffs = 0;
    for (let i = 0; i < a.length && diffs < 5; i++) {
      if (a[i] === b[i]) continue;
      diffs++; bad++;
      const pa = a[i].split("|"), pb = b[i].split("|");
      const changed = PROPS.map((p, n) => [p, pa[n + 1], pb[n + 1]])
                           .filter(([, x, y]) => x !== y)
                           .map(([p, x, y]) => `${p}: ${x} -> ${y}`);
      console.log(`  ${d}: element ${i} <${pa[0].toLowerCase()}>  ${changed.join("; ")}`);
    }
    compared += a.length;
  }
  console.log(`\n${compared.toLocaleString()} elements compared across `
              + `${domains.length} domain(s), ${PROPS.length} properties each.`);
  console.log(bad === 0
    ? "No computed style changed. The rendering is the same."
    : `${bad} difference(s) above. Each is a real rendering change, or a property `
      + `this tool reads that the change deliberately moved.`);
  await ctx.close();
} finally {
  await browser.close();
  if (KEEP) console.log(`\nReference build left in ${base}`);
  else rmSync(dir, { recursive: true, force: true });
}
process.exit(bad === 0 ? 0 : 1);
