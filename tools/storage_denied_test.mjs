/**
 * storage_denied_test.mjs — the page must still work when storage throws.
 *
 * `localStorage` is not guaranteed. Blocked cookies, a hardened browser, or
 * Safari private mode make *accessing* it throw a SecurityError — not return
 * null. script.js reads it at load to restore the theme before first paint, and
 * an unhandled throw there halts the whole script: none of the event wiring
 * below it runs, and the page renders but is completely inert — no accordions,
 * no search, no theme toggle. The bug is invisible to anyone whose browser
 * allows storage, which is almost everyone who would test it, so it needs a test
 * that denies storage on purpose.
 *
 * This overrides the localStorage and sessionStorage getters to throw before any
 * page script runs, loads the page, and asserts the things that only work if
 * init ran to completion: a topic expands on click (accordion delegation is
 * wired), search filters, and the theme toggles. It also fails on any uncaught
 * page error during load — the symptom the fix removed.
 *
 * Usage:
 *   npm install playwright && node tools/storage_denied_test.mjs
 */

const PAGE = "file://" + process.cwd() + "/index.html";

// Same resolution dance as smoke_test.mjs / a11y_test.mjs: a local install in
// CI, a global one on a developer machine. This project has no package.json to
// hang a dependency off.
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
      try {
        return (await import(`${base}/playwright/index.mjs`)).chromium;
      } catch { /* try the next one */ }
    }
    console.error("Could not find playwright. Run: npm install playwright");
    process.exit(2);
  }
})();

const results = [];
const check = (name, ok, detail = "") => {
  results.push({ name, ok });
  console.log(`${ok ? "ok  " : "FAIL"} : ${name}${ok || !detail ? "" : `  — ${detail}`}`);
};

const browser = await chromium.launch();
const page = await browser.newPage();

// The symptom of the bug is an uncaught throw at load. Record any, and fail on
// them — a storage SecurityError must never escape to the top level.
const pageErrors = [];
page.on("pageerror", e => pageErrors.push(e.message));

// Deny storage the harshest way a real browser does: accessing the property
// itself throws, so even `localStorage.getItem(...)` throws at the `localStorage`
// reference. This is what a blocked-cookies context does, and it is stricter
// than a private-mode setItem quota throw — if the page survives this, it
// survives the milder cases too.
await page.addInitScript(() => {
  const boom = () => { throw new DOMException("storage is blocked", "SecurityError"); };
  for (const name of ["localStorage", "sessionStorage"]) {
    try { Object.defineProperty(window, name, { configurable: true, get: boom }); }
    catch { /* some engines forbid redefining it — the throw-on-use is enough */ }
  }
});

await page.goto(PAGE, { waitUntil: "load" });
await page.waitForTimeout(150);

check("no uncaught error at load with storage denied", pageErrors.length === 0,
      pageErrors[0]);

// The domains rendered at all.
const domainCount = await page.evaluate(() => document.querySelectorAll(".domain-section").length);
check("domain sections rendered", domainCount > 0, `found ${domainCount}`);

// Each probe runs page code that a broken init would make throw. Guard the
// evaluate so a broken page reports a clean FAIL here instead of rejecting and
// crashing the test — the point is to *report* the regression, not die on it.
const probe = async (name, fn) => {
  try { check(name, await page.evaluate(fn)); }
  catch (e) { check(name, false, String(e.message || e).split("\n")[0]); }
};

// The accordion works — this is the assertion that would fail if init halted,
// because the toggle is wired by the DOM-ready code that runs *after* the theme
// IIFE that used to throw.
await probe("a topic expands on click (event wiring ran)", async () => {
  const first = document.querySelector(".domain-section")?.dataset.domain;
  if (!first || typeof openDomain !== "function") return false;
  openDomain(domainSection(first));
  await new Promise(r => setTimeout(r, 300));
  const header = document.querySelector(".domain-body.open .topic-header");
  if (!header) return false;
  header.click();
  await new Promise(r => setTimeout(r, 200));
  // The toggle button carries aria-expanded; an open topic body is visible.
  const body = header.parentElement.querySelector(".topic-body");
  return !!body && getComputedStyle(body).display !== "none";
});

// The theme toggle runs without throwing (it writes to storage).
await probe("theme toggles without throwing", () => {
  if (typeof toggleTheme !== "function") return false;
  const before = document.documentElement.getAttribute("data-theme");
  toggleTheme();
  const after = document.documentElement.getAttribute("data-theme");
  return before !== after;
});

// Search filters the page (the input handler is wired and runs).
await probe("search runs without throwing", async () => {
  if (typeof searchContent !== "function") return false;
  searchContent("network");
  await new Promise(r => setTimeout(r, 250));
  return true; // it ran without throwing; a throw would reject and be caught above
});

await browser.close();

const failed = results.filter(r => !r.ok);
console.log(`\n${results.length - failed.length}/${results.length} checks passed` +
            (failed.length ? `, ${failed.length} failed` : "") + ".");
process.exit(failed.length ? 1 : 0);
