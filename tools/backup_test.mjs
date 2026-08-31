/**
 * backup_test.mjs — a backup must restore exactly what it saved.
 *
 * The export (bkCollect) parses JSON-valued keys — the SRS schedules, the
 * notepad, the streak — so the downloaded file reads as nested JSON instead of
 * escaped strings. localStorage only holds strings, so the import (bkApply) has
 * to re-serialise them. It once did not: it wrote the parsed object straight to
 * setItem, which coerces to the literal "[object Object]", so restoring a backup
 * silently destroyed every spaced-repetition schedule, the notepad and the
 * streak — the data most expensive to recreate, and the whole reason to back up.
 *
 * This seeds one of every key kind, round-trips it through
 * export → JSON string → wipe → import, and asserts each key comes back byte for
 * byte. It also exercises merge mode, whose rule is that the later SRS due date
 * wins, so an import never pulls a card forward unexpectedly.
 *
 * Usage:
 *   npm install playwright && node tools/backup_test.mjs
 */

const PAGE = "file://" + process.cwd() + "/index.html";

const chromium = await (async () => {
  try { return (await import("playwright")).chromium; }
  catch {
    for (const base of ["/opt/node22/lib/node_modules", "/usr/lib/node_modules", "/usr/local/lib/node_modules"]) {
      try { return (await import(`${base}/playwright/index.mjs`)).chromium; }
      catch { /* next */ }
    }
    console.error("Could not find playwright. Run: npm install playwright");
    process.exit(2);
  }
})();

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto(PAGE, { waitUntil: "load" });

const results = [];
const check = (name, ok, detail = "") => {
  results.push({ name, ok });
  console.log(`${ok ? "ok  " : "FAIL"} : ${name}${ok || !detail ? "" : `  — ${detail}`}`);
};

// 1. Replace-mode round-trip preserves every key exactly, JSON ones included.
const replace = await page.evaluate(() => {
  const seed = {
    "reviewed:osi-model": "1",
    "bookmark:subnetting": "1",
    "known:dns": "1",
    "note:vpns": "a note, with, commas",
    "study-streak": JSON.stringify({ last: "2026-08-31", n: 5, best: 9 }),
    "srs:topic-x": JSON.stringify({ d: "2026-09-05", ivl: 6, ease: 2.5, reps: 3 }),
  };
  const npKey = (typeof NP_STORE_KEY === "string") ? NP_STORE_KEY : "shared-notepad-notes";
  seed[npKey] = JSON.stringify([{ id: "a", text: "hello", ts: 123 }]);
  Object.entries(seed).forEach(([k, v]) => localStorage.setItem(k, v));

  const fileJson = JSON.stringify(bkCollect());          // export → download
  bkOwnedKeys().forEach(k => localStorage.removeItem(k)); // lose everything
  bkApply(JSON.parse(fileJson), "replace");              // upload → import

  const bad = [];
  for (const [k, v] of Object.entries(seed)) {
    const got = localStorage.getItem(k);
    if (got !== v) bad.push(`${k}: ${JSON.stringify(got)} != ${JSON.stringify(v)}`);
  }
  return bad;
});
check("replace round-trip restores every key byte for byte", replace.length === 0, replace[0]);

// 2. The exported file is genuine nested JSON for the JSON keys (readable), not
//    an escaped string — the reason the parse/re-serialise pair exists at all.
const readable = await page.evaluate(() => {
  localStorage.setItem("srs:topic-y", JSON.stringify({ d: "2026-10-01", ivl: 3 }));
  const exp = bkCollect();
  return exp["srs:topic-y"] && typeof exp["srs:topic-y"] === "object" &&
         exp["srs:topic-y"].d === "2026-10-01";
});
check("export keeps JSON values as objects (a readable file)", readable);

// 3. Merge keeps the later SRS due date — an import must not pull a card forward.
const merge = await page.evaluate(() => {
  localStorage.clear();
  localStorage.setItem("srs:card", JSON.stringify({ d: "2026-12-01", ivl: 30 })); // local: far future
  const incoming = { "srs:card": { d: "2026-09-01", ivl: 2 } };                    // file: sooner
  bkApply(incoming, "merge");
  const got = JSON.parse(localStorage.getItem("srs:card"));
  return got && got.d === "2026-12-01"; // local (later) wins
});
check("merge keeps the later SRS due date", merge);

await browser.close();

const failed = results.filter(r => !r.ok);
console.log(`\n${results.length - failed.length}/${results.length} checks passed` +
            (failed.length ? `, ${failed.length} failed` : "") + ".");
process.exit(failed.length ? 1 : 0);
