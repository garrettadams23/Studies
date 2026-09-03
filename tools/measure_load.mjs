/**
 * measure_load.mjs — how long does the page take to load, and what happens to
 * that number if the library keeps growing?
 *
 * tools/page_budget.py enforces a size. This produces the measurement that size
 * is supposed to stand for, so "8 MB" can be argued with rather than inherited.
 * Its docstring told the next person to re-measure and left them no way to do
 * it, so the table nobody could reproduce went on being quoted — including its
 * claim that load is linear in raw size, which it is not.
 *
 * ## The model
 *
 * build.py ships each domain's content inside <script type="text/html"
 * class="domain-src">, which the browser tokenises but never parses as markup
 * or builds. Duplicating those blocks therefore models "the same page with N
 * times the cards" without inventing a single card. Multiplier 0 strips them
 * instead, which prices the shell on its own, so the rest of the table reads as
 * what the content adds.
 *
 * ## What this model does not measure — read this before quoting a number
 *
 * The duplication multiplies the *markup*. It does not touch the id map build.py
 * inlines as JSON, which is what topicIndex() — and therefore search — reads.
 * The `indexed` and `blocks` columns are printed to keep that honest: blocks
 * triples while indexed does not move. So **the search and heap columns are flat
 * by construction and say nothing about a page with three times the topics.**
 * Sizing those needs a different model: real extra topics, or a synthetic index.
 *
 * Nor are the millisecond figures portable. The same script on the same commit
 * gives ~1.2 s here and ~2.9 s in a CI container, and neither machine is a
 * reader's phone. **Only the shape of the curve transfers between machines.**
 * Comparing a row measured here against a row someone else measured elsewhere
 * is the mistake this file exists to stop.
 *
 * Everything is timed inside the page via the Navigation Timing API, never by
 * wrapping the Playwright call — the round trip is tens of milliseconds and has
 * already once been mistaken for a regression.
 *
 * Usage:
 *   node tools/measure_load.mjs                 # 0x, 1x, 2x, 3x at 4x CPU throttle
 *   node tools/measure_load.mjs --mult 0,1      # only these multipliers
 *   node tools/measure_load.mjs --throttle 1    # no throttle (a fast desktop)
 *   node tools/measure_load.mjs --keep          # leave the generated pages behind
 *
 * A measurement, not a gate: it is deliberately outside `make all`, it never
 * fails on a number, and it needs a browser and a couple of minutes.
 */

import { readFileSync, writeFileSync, mkdtempSync, symlinkSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const ROOT = process.cwd();
const arg = (name, fallback) => {
  const i = process.argv.indexOf(name);
  return i === -1 ? fallback : process.argv[i + 1];
};
const MULTS = String(arg("--mult", "0,1,2,3")).split(",").map(Number);
const THROTTLE = Number(arg("--throttle", 4));
const KEEP = process.argv.includes("--keep");

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

const src = readFileSync(join(ROOT, "index.html"), "utf-8");
const BLOCK = /<script[^>]*class="domain-src"[^>]*>[\s\S]*?<\/script>/g;
const blocks = src.match(BLOCK) || [];
if (!blocks.length) {
  console.error("error: no deferred domain blocks in index.html — run python3 build.py first");
  process.exit(2);
}
const last = blocks[blocks.length - 1];
const lastEnd = src.lastIndexOf(last) + last.length;

// The variants live in a temp directory with the page's assets symlinked beside
// them: a copy of index.html anywhere else cannot resolve script.js, and a
// silently script-less page would measure a shell that does nothing.
const dir = mkdtempSync(join(tmpdir(), "measure-load-"));
for (const asset of ["script.js", "style.css", "sw.js", "Img"]) {
  try { symlinkSync(join(ROOT, asset), join(dir, asset)); } catch { /* absent is fine */ }
}

const variants = MULTS.map(mult => {
  const html = mult === 0
    ? src.replace(BLOCK, '<script type="text/html" class="domain-src" data-domain="empty"></script>')
    : src.slice(0, lastEnd) + (mult === 1 ? "" : blocks.join("").repeat(mult - 1)) + src.slice(lastEnd);
  const path = join(dir, `idx-${mult}x.html`);
  writeFileSync(path, html);
  return { mult, path, mb: Buffer.byteLength(html) / 1024 / 1024 };
});

const browser = await chromium.launch();
try {
  console.log(`Chromium at ${THROTTLE}x CPU throttle, ${ROOT}\n`);
  console.log("mult   raw MB   domInt(ms)   load(ms)   search(ms)   heap(MB)   indexed   blocks");
  for (const v of variants) {
    const ctx = await browser.newContext();
    const page = await ctx.newPage();
    if (THROTTLE !== 1) {
      const cdp = await ctx.newCDPSession(page);
      await cdp.send("Emulation.setCPUThrottlingRate", { rate: THROTTLE });
    }
    await page.goto(`file://${v.path}`, { waitUntil: "load" });

    const nav = await page.evaluate(() => {
      const n = performance.getEntriesByType("navigation")[0];
      return { dom: Math.round(n.domInteractive - n.startTime),
               load: Math.round(n.loadEventEnd - n.startTime) };
    });
    // Warm: one run to prime whatever caches, then the median of three.
    const search = await page.evaluate(() => {
      if (typeof runSearch !== "function") return NaN;
      runSearch("kubernetes");
      const times = [];
      for (let i = 0; i < 3; i++) {
        const s = performance.now();
        runSearch(i % 2 ? "certificate" : "kubernetes");
        times.push(performance.now() - s);
      }
      return times.sort((a, b) => a - b)[1];
    });
    const shape = await page.evaluate(() => ({
      heap: performance.memory ? performance.memory.usedJSHeapSize / 1024 / 1024 : NaN,
      indexed: typeof topicIndex === "function"
        ? Object.values(topicIndex()).reduce((n, a) => n + a.length, 0) : NaN,
      blocks: document.querySelectorAll("script.domain-src").length,
    }));

    const col = (x, w, d = 0) => (Number.isFinite(x) ? x.toFixed(d) : "—").padStart(w);
    console.log(`${v.mult}x   ${col(v.mb, 6, 1)}   ${col(nav.dom, 10)}   ${col(nav.load, 8)}   ` +
                `${col(search, 10)}   ${col(shape.heap, 8)}   ${col(shape.indexed, 7)}   ` +
                `${col(shape.blocks, 6)}`);
    await ctx.close();
  }
  console.log("\nindexed does not move while blocks multiplies: this model grows the markup,");
  console.log("not the search index. Read the search and heap columns as flat by construction,");
  console.log("and do not compare the millisecond columns against a run on another machine.");
} finally {
  await browser.close();
  if (KEEP) console.log(`\nGenerated pages left in ${dir}`);
  else rmSync(dir, { recursive: true, force: true });
}
