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
 * The PNG carries its own inputs in a tEXt chunk — the two numbers and a hash
 * of the HTML it was rendered from — so `--check` compares *what the card was
 * made from*, not the pixels it came out as. That check needs no browser and
 * cannot fail on a Chromium upgrade; see the note beside `claim` below.
 *
 * Usage:
 *   node tools/gen_og_image.mjs          # writes Img/og-card.png
 *   node tools/gen_og_image.mjs --check  # fail if the sources have moved on
 *   strings Img/og-card.png | head -2    # read what the committed card claims
 */

import { readFileSync, writeFileSync, existsSync, readdirSync } from "node:fs";
import { resolve } from "node:path";
import { createHash } from "node:crypto";

const ROOT = resolve(new URL("..", import.meta.url).pathname);
const OUT = `${ROOT}/Img/og-card.png`;
const CHECK = process.argv.includes("--check");

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

// ── what the committed PNG claims ───────────────────────────────────────────
// `--check` used to compare the rendered bytes against the committed ones. That
// is a gate on the *rasteriser*: two Chromium builds disagree on glyph edges by
// a thousand pixels, so the check fails on a browser upgrade with no content
// change, and the fix it prints ("regenerate and commit") is the fix for a real
// staleness too. A gate that cries wolf is a gate nobody reads — and this one
// went unread for long enough that the card said 1,519 topics while the site had
// 1,534, on every link anyone shared.
//
// So the card carries its own inputs, in a PNG tEXt chunk: the two numbers plus
// a hash of the HTML it was rendered from. `--check` recomputes those from the
// current sources and compares strings. It catches a changed count, changed
// copy, changed CSS — anything that would change the picture — and needs no
// browser at all, which is why it now runs in `make check` beside the linter
// instead of at the end of a Chromium job.
const KEYWORD = "og-card";

// ROOT is baked into the card: the font faces are rewritten to file:// URLs so
// Chromium can load them off disk. Hashing the string as-is makes the claim
// machine-dependent — this repo is /home/user/Studies here and
// /home/runner/work/Studies/Studies on a runner, so a card stamped on one
// machine reads as stale on the other, forever. The first push after this check
// went in failed on exactly that, which is the check working: it took thirteen
// seconds to say so instead of a fortnight.
const stableCard = card.split(ROOT).join("{ROOT}");
const claim = `topics=${topics};domains=${domains.length};` +
              `card=${createHash("sha256").update(stableCard).digest("hex").slice(0, 16)}`;
if (claim.includes(ROOT)) {
  console.error("error: the card's fingerprint still contains an absolute path.");
  process.exit(1);
}

const CRC_TABLE = Array.from({ length: 256 }, (_, n) => {
  let c = n;
  for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
  return c >>> 0;
});
const crc32 = buf => {
  let c = 0xffffffff;
  for (const b of buf) c = CRC_TABLE[(c ^ b) & 0xff] ^ (c >>> 8);
  return (c ^ 0xffffffff) >>> 0;
};

/** Insert a tEXt chunk directly after IHDR, which is where PNG allows one. */
function stamp(png, keyword, text) {
  const body = Buffer.concat([Buffer.from(keyword, "latin1"), Buffer.from([0]),
                              Buffer.from(text, "latin1")]);
  const chunk = Buffer.alloc(body.length + 12);
  chunk.writeUInt32BE(body.length, 0);
  chunk.write("tEXt", 4, "latin1");
  body.copy(chunk, 8);
  chunk.writeUInt32BE(crc32(chunk.subarray(4, 8 + body.length)), 8 + body.length);
  // 8-byte signature, then IHDR: 4 length + 4 type + 13 data + 4 crc = 25.
  const at = 8 + 25;
  return Buffer.concat([png.subarray(0, at), chunk, png.subarray(at)]);
}

/** Read back the tEXt chunk with this keyword, or "" if the file has none. */
function stamped(png, keyword) {
  let at = 8;
  while (at + 8 <= png.length) {
    const len = png.readUInt32BE(at);
    const type = png.toString("latin1", at + 4, at + 8);
    if (type === "IEND") break;
    if (type === "tEXt") {
      const data = png.subarray(at + 8, at + 8 + len);
      const nul = data.indexOf(0);
      if (nul > 0 && data.toString("latin1", 0, nul) === keyword)
        return data.toString("latin1", nul + 1);
    }
    at += len + 12;
  }
  return "";
}

if (CHECK) {
  const was = existsSync(OUT) ? stamped(readFileSync(OUT), KEYWORD) : "";
  if (was === claim) {
    console.log(`Img/og-card.png is current — ${claim}.`);
    process.exit(0);
  }
  console.error(`::error::Img/og-card.png is stale. It was rendered from ` +
                `${was || "an unstamped build"}; the sources now say ${claim}. ` +
                `Run 'node tools/gen_og_image.mjs' and commit the result.`);
  process.exit(1);
}

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

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
await page.setContent(card, { waitUntil: "load" });
await page.evaluate(() => document.fonts.ready);
const buf = stamp(await page.screenshot({ type: "png" }), KEYWORD, claim);
await browser.close();

writeFileSync(OUT, buf);
console.log(`Wrote Img/og-card.png (${(buf.length / 1024).toFixed(0)} KB, ${claim}).`);
