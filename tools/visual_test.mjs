/**
 * visual_test.mjs — pixel diff of the page shell against committed baselines.
 *
 * Deliberately narrow. A visual regression suite that screenshots content is a
 * suite that fails on every content wave, and a check that fails constantly is
 * a check people learn to ignore — which is worse than not having it. So this
 * captures **only the filter bar** — thirty coloured chips in a row — in both
 * themes, at one fixed viewport. That is the part every visitor sees
 * first, the part that changes rarely, and the part where an accidental CSS
 * change is otherwise invisible until someone notices in production.
 *
 * It would have flagged the light-mode chip colours as a change — which is
 * exactly right: they were an intentional fix, so the baseline gets updated
 * with the commit that made them.
 *
 * Comparison is done in the browser on a canvas rather than with an image
 * library, because this project has no package.json to hang one off and
 * Playwright is already here. A small per-pixel tolerance absorbs antialiasing;
 * the threshold is on the *fraction of pixels* that differ.
 *
 * Usage:
 *   node tools/visual_test.mjs            # compare against tools/baseline/
 *   node tools/visual_test.mjs --update   # accept the current rendering
 */

import { readFileSync, writeFileSync, existsSync, mkdirSync } from "node:fs";
import { createRequire } from "node:module";
import { resolve } from "node:path";

const ROOT = resolve(new URL("..", import.meta.url).pathname);
const BASELINE = `${ROOT}/tools/baseline`;
const PAGE = `file://${ROOT}/index.html`;
const UPDATE = process.argv.includes("--update");

// A pixel counts as different if any channel moves by more than this. Font
// antialiasing moves single channels by a few units between runs.
const CHANNEL_TOLERANCE = 12;
// And the shot fails if more than this fraction of pixels differ.
//
// Calibrated, not guessed. Repeated runs in one environment differ by exactly
// zero pixels, and changing a single chip's colour back to its old value moves
// **0.111%** — one chip's text is a small share of a bar of thirty. So 0.002
// would have watched that bug go past. 0.0005 catches it with room to spare and
// still absorbs antialiasing.
//
// If this ever turns noisy on a runner whose font rendering differs from a
// developer's, the fix is to raise this number or drop the shot — not to
// silence the job. A visual check that fails constantly gets ignored, and an
// ignored check is worse than no check.
const MAX_DIFF_FRACTION = 0.0005;

/** The playwright module and its version, wherever it is installed. */
const { chromium, version } = await (async () => {
  try {
    const mod = await import("playwright");
    let v = null;
    try { v = createRequire(import.meta.url)("playwright/package.json").version; } catch { /* unknown */ }
    return { chromium: mod.chromium, version: v };
  } catch {
    for (const base of ["/opt/node22/lib/node_modules", "/usr/lib/node_modules",
                        "/usr/local/lib/node_modules"]) {
      try {
        const mod = await import(`${base}/playwright/index.mjs`);
        let v = null;
        try { v = JSON.parse(readFileSync(`${base}/playwright/package.json`, "utf8")).version; } catch { /* unknown */ }
        return { chromium: mod.chromium, version: v };
      } catch { /* try the next one */ }
    }
    console.error("error: playwright not found. Run: npm install playwright");
    process.exit(1);
  }
})();

// The baselines are CI's rendering, and CI pins Playwright in its workflow.
// Each Playwright release brings its own Chromium, and text rendering moves
// between them: under Playwright 1.63.0 (Chromium 153) the chip labels draw
// about 10% wider than under the pinned 1.56.0 (Chromium 141), and 10% of the
// bar's pixels differ with nothing on the page changed. CI's own run on
// 2026-10-11 matched these baselines 2/2. So a run under another Playwright
// says so, and --update refuses to accept its rendering: a baseline taken
// there would make CI fail on every push until someone took it back.
const PINNED = (() => {
  try {
    return readFileSync(`${ROOT}/.github/workflows/build-check.yml`, "utf8")
      .match(/npm install playwright@(\d+\.\d+\.\d+)/)?.[1] ?? null;
  } catch { return null; }
})();
const FOREIGN = Boolean(PINNED && version && version !== PINNED);
if (UPDATE && FOREIGN && !process.argv.includes("--any-playwright")) {
  console.error(`error: this is Playwright ${version}; the baselines belong to ${PINNED}, the version ` +
                `.github/workflows/build-check.yml pins. Update them under ${PINNED}, or pass ` +
                `--any-playwright and change the pin in the same commit.`);
  process.exit(2);
}

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
await page.goto(PAGE, { waitUntil: "load" });
await page.evaluate(() => document.fonts.ready);

/** Fraction of pixels that differ, computed on a canvas inside the browser. */
async function diffFraction(a, b) {
  return page.evaluate(async ([one, two, tol]) => {
    const load = src => new Promise((res, rej) => {
      const img = new Image();
      img.onload = () => res(img);
      img.onerror = rej;
      img.src = "data:image/png;base64," + src;
    });
    const [x, y] = await Promise.all([load(one), load(two)]);
    if (x.width !== y.width || x.height !== y.height) return 1;
    const draw = img => {
      const c = document.createElement("canvas");
      c.width = img.width; c.height = img.height;
      c.getContext("2d").drawImage(img, 0, 0);
      return c.getContext("2d").getImageData(0, 0, img.width, img.height).data;
    };
    const [p, q] = [draw(x), draw(y)];
    let differing = 0;
    for (let i = 0; i < p.length; i += 4) {
      if (Math.abs(p[i] - q[i]) > tol || Math.abs(p[i + 1] - q[i + 1]) > tol ||
          Math.abs(p[i + 2] - q[i + 2]) > tol) differing++;
    }
    return differing / (p.length / 4);
  }, [a, b, CHANNEL_TOLERANCE]);
}

const results = [];
if (!existsSync(BASELINE)) mkdirSync(BASELINE, { recursive: true });

for (const theme of ["dark", "light"]) {
  await page.evaluate(t => document.documentElement.setAttribute("data-theme", t), theme);
  await page.waitForTimeout(250);
  // The filter bar, not the whole header. Two reasons, both learned by looking
  // at the first baseline: the header contains a large static illustration that
  // dominates the file and can never regress, and it contains a *rotating
  // quote*, which would have made this check fail at random. The filter bar is
  // thirty coloured chips in a row — compact, deterministic, and the exact
  // place the light-mode contrast bug lived.
  const shot = await page.locator(".filter-bar").first().screenshot();
  const name = `chips-${theme}.png`;
  const file = `${BASELINE}/${name}`;

  if (UPDATE || !existsSync(file)) {
    const verb = existsSync(file) ? "updated" : "created";
    writeFileSync(file, shot);
    console.log(`${verb} : ${name}`);
    results.push({ name, ok: true });
    continue;
  }
  const fraction = await diffFraction(readFileSync(file).toString("base64"),
                                      shot.toString("base64"));
  const ok = fraction <= MAX_DIFF_FRACTION;
  results.push({ name, ok, fraction });
  console.log(`${ok ? "ok  " : "FAIL"} : ${name}` +
              (fraction ? `  — ${(fraction * 100).toFixed(3)}% of pixels differ` : ""));
  if (!ok) {
    writeFileSync(`${BASELINE}/${name.replace(".png", ".actual.png")}`, shot);
    console.log(`        wrote ${name.replace(".png", ".actual.png")} beside the baseline`);
  }
}

const engine = `Playwright ${version ?? "(version unknown)"}, Chromium ${browser.version()}`;
await browser.close();

const failed = results.filter(r => !r.ok);
console.log(`\n${results.length - failed.length}/${results.length} shots match (${engine}).`);
if (failed.length && FOREIGN) {
  console.log(`These baselines are CI's rendering under Playwright ${PINNED}, the version its workflow pins.\n` +
              `This run used ${version}, whose Chromium draws text differently, so a mismatch here is not\n` +
              `by itself a regression. Read the .actual.png files, then let CI decide.`);
} else if (failed.length) {
  console.log("If the change was intended, run: node tools/visual_test.mjs --update");
}
process.exit(failed.length ? 1 : 0);
