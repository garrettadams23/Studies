/**
 * gen_og_image.mjs — render Img/og-card.png, the link preview for the site.
 *
 * A social card has to be a raster image at a fixed size, which is the one
 * thing a self-contained HTML page cannot produce on its own. Playwright is
 * already a dependency for the tests, so the card is rendered from an HTML
 * template here rather than maintained by hand in an image editor — which
 * means the numbers on it come from the content and cannot go stale.
 *
 * Deliberately *one* card for the site rather than one per domain. Domains are
 * hash fragments (`#net`), and no crawler distinguishes `/#net` from `/` or
 * runs the JavaScript that would render it — per-domain cards would be thirty
 * images that nothing ever requests.
 *
 * Usage:
 *   node tools/gen_og_image.mjs          # writes Img/og-card.png
 *   node tools/gen_og_image.mjs --check  # fail if it would change
 */

import { readFileSync, writeFileSync, existsSync, readdirSync } from "node:fs";
import { resolve } from "node:path";

const ROOT = resolve(new URL("..", import.meta.url).pathname);
const OUT = `${ROOT}/Img/og-card.png`;
const CHECK = process.argv.includes("--check");

const chromium = await (async () => {
  try {
    return (await import("playwright")).chromium;
  } catch {
    for (const base of ["/opt/node22/lib/node_modules", "/usr/lib/node_modules",
                        "/usr/local/lib/node_modules"]) {
      try {
        return (await import(`${base}/playwright/index.mjs`)).chromium;
      } catch { /* try the next one */ }
    }
    console.error("error: playwright not found. Run: npm install playwright");
    process.exit(1);
  }
})();

// Counted from the sources, so the card cannot claim a number the site no
// longer has.
const domains = JSON.parse(readFileSync(`${ROOT}/data/domains.json`, "utf-8"));
const files = readdirSync(`${ROOT}/data`).filter(f => f.endsWith(".html"));
const topics = files.reduce((n, f) =>
  n + (readFileSync(`${ROOT}/data/${f}`, "utf-8").match(/<div class="topic"/g) || []).length, 0);

const fontCss = readFileSync(`${ROOT}/Img/fonts.css`, "utf-8")
  .replace(/url\((["']?)(?!data:)/g, `url($1file://${ROOT}/Img/`);

const card = `<!doctype html><html><head><meta charset="utf-8"><style>
${fontCss}
* { margin: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 630px; display: flex; flex-direction: column;
  justify-content: center; gap: 26px; padding: 72px;
  background: radial-gradient(circle at 18% 20%, #16233f 0%, #07090f 62%);
  color: #cdd9f0; font-family: "Outfit", system-ui, sans-serif;
}
.kicker { font-family: "Share Tech Mono", monospace; font-size: 26px;
  letter-spacing: 7px; color: #00d4ff; text-transform: uppercase; }
h1 { font-size: 82px; line-height: 1.04; font-weight: 700; letter-spacing: -1.5px; }
h1 em { font-style: normal; color: #00d4ff; }
p { font-size: 31px; line-height: 1.35; color: #8296b3; max-width: 34ch; }
.stats { display: flex; gap: 44px; margin-top: 8px; }
.stat b { display: block; font-family: "Share Tech Mono", monospace;
  font-size: 46px; color: #00ff99; line-height: 1; }
.stat span { font-size: 21px; color: #8296b3; }
.rule { height: 5px; width: 132px; background: #00d4ff; border-radius: 3px; }
</style></head><body>
<div class="kicker">Free · Offline · No tracking</div>
<div class="rule"></div>
<h1>Tech &amp; Life <em>Reference</em></h1>
<p>An interactive study guide for IT and CompTIA.</p>
<div class="stats">
  <div class="stat"><b>${topics.toLocaleString("en")}</b><span>topics</span></div>
  <div class="stat"><b>${domains.length}</b><span>domains</span></div>
  <div class="stat"><b>0</b><span>third-party requests</span></div>
</div>
</body></html>`;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
await page.setContent(card, { waitUntil: "load" });
await page.evaluate(() => document.fonts.ready);
const buf = await page.screenshot({ type: "png" });
await browser.close();

if (CHECK) {
  const same = existsSync(OUT) && Buffer.compare(readFileSync(OUT), buf) === 0;
  console.log(same ? "Img/og-card.png is up to date."
                   : "Img/og-card.png is stale — run node tools/gen_og_image.mjs");
  process.exit(same ? 0 : 1);
}

writeFileSync(OUT, buf);
console.log(`Wrote Img/og-card.png (${(buf.length / 1024).toFixed(0)} KB, ` +
            `${topics} topics, ${domains.length} domains)`);
