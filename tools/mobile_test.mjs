/**
 * mobile_test.mjs — the page must not scroll sideways on a phone.
 *
 * The other browser tests, and the visual baseline, all run at desktop width, so
 * a layout that overflows only on a narrow screen has nowhere to be caught. This
 * renders at 375px — a common phone width — opens each of a spread of
 * table- and widget-heavy domains, expands every topic so the deferred content is
 * actually in the layout, and asserts the document is no wider than the viewport.
 *
 * The bug this was written for: wide reference tables have a nowrap first column
 * and sat in no scroll container, so a five-column table dragged the whole page
 * ~100px past the viewport. Anything that reintroduces an unconfined wide element
 * — a table, a diagram, a fixed-width widget — trips this.
 *
 * It does not open all 29 domains: the layout rules are shared, so a representative
 * spread that includes the historically-widest content tests the same CSS at a
 * fraction of the cost. A couple of pixels of slack absorbs sub-pixel rounding.
 *
 * Usage:
 *   npm install playwright && node tools/mobile_test.mjs
 */

const PAGE = "file://" + process.cwd() + "/index.html";
const WIDTH = 375;
const SLACK = 2; // px — sub-pixel rounding, not a real overflow

// Table- and widget-heavy domains, plus a couple of prose ones for contrast.
const DOMAINS = ["script", "net", "sec", "math", "data", "linux", "cs", "grc", "hw"];

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

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: WIDTH, height: 780 } });
await page.goto(PAGE, { waitUntil: "load" });

const results = [];
for (const dom of DOMAINS) {
  const opened = await page.evaluate((d) => {
    if (typeof openDomain !== "function" || typeof domainSection !== "function") return false;
    const sec = domainSection(d);
    if (!sec) return false;
    openDomain(sec);
    return true;
  }, dom);
  if (!opened) { results.push({ dom, skipped: true }); continue; }
  await page.waitForTimeout(250);
  // Expand every topic so tables and widgets are actually laid out.
  await page.evaluate(() => {
    document.querySelectorAll(".domain-body.open .topic-header").forEach((h) => {
      if (!h.parentElement.classList.contains("open")) h.click();
    });
  });
  await page.waitForTimeout(350);

  const overflow = await page.evaluate(() => {
    const de = document.documentElement;
    const px = de.scrollWidth - de.clientWidth;
    let worst = null;
    if (px > 2) {
      // Name the widest element not sitting inside a horizontal scroller, to make
      // a failure diagnosable rather than a bare number.
      const vw = window.innerWidth;
      for (const el of document.querySelectorAll(".domain-body.open *")) {
        if (el.getBoundingClientRect().right <= vw + 1) continue;
        let a = el.parentElement, contained = false;
        while (a && a !== document.body) {
          const o = getComputedStyle(a).overflowX;
          if (o === "auto" || o === "scroll") { contained = true; break; }
          a = a.parentElement;
        }
        if (!contained) {
          worst = el.tagName + (el.className ? "." + String(el.className).split(" ")[0] : "");
          break;
        }
      }
    }
    return { px, worst };
  });

  const ok = overflow.px <= SLACK;
  results.push({ dom, px: overflow.px, worst: overflow.worst, ok });
  console.log(`${ok ? "ok  " : "FAIL"} : ${dom}  (page ${overflow.px}px past ${WIDTH}px viewport)` +
              (ok || !overflow.worst ? "" : `  — widest uncontained: ${overflow.worst}`));

  // Collapse the domain again to keep each measurement independent.
  await page.evaluate((d) => { const s = domainSection(d); if (s) openDomain(s); }, dom);
  await page.waitForTimeout(80);
}

await browser.close();

const failed = results.filter((r) => r.ok === false);
const checked = results.filter((r) => !r.skipped).length;
console.log(`\n${checked - failed.length}/${checked} domains fit the ${WIDTH}px viewport` +
            (failed.length ? `, ${failed.length} overflow` : "") + ".");
process.exit(failed.length ? 1 : 0);
