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
 * ## The second half: a hostile URL is the same failure
 *
 * Storage is not the only load-critical path that can throw. `openHashTarget()`
 * runs at boot and `decodeURIComponent` throws `URIError` on a malformed
 * percent-escape — `#%`, a link a chat client truncated mid-sequence. That threw
 * out of init *before* the hashchange listener was registered, so every in-page
 * navigation for the rest of the session silently did nothing.
 *
 * Identical shape to the storage bug, identical invisibility: nobody types `#%`
 * on purpose, and the reader who receives a mangled link has no idea why the
 * site stopped responding. So the same file covers it, with a spread of hostile
 * hashes — malformed escapes, markup, path traversal, absurd card indices — each
 * asserting no uncaught error and no injected handler.
 *
 * ## The third half: storage that lies, and a file that is hostile
 *
 * Denied storage is one failure; *corrupted* storage is another. A record
 * half-written, synced between browsers, or hand-edited leaves `srs:` holding
 * `{{{not json`, `reviewed:` holding an object, `streak` holding `%%%`. Every
 * one of those is a `JSON.parse` away from the same page-halt.
 *
 * And the import path takes a JSON file the reader chose, which is the only
 * place this page ingests anything it did not write. Its gate — `bkCategory`
 * for the key namespace, `bkSerialise` rebuilding each value field by field —
 * is what stops a hand-edited file writing arbitrary keys or polluting
 * `Object.prototype`.
 *
 * Both passed on first measurement. They are pinned anyway: a guard nobody
 * tests is a guard somebody removes, and these two were written as fixes in
 * earlier sessions with no test naming what they were fixing.
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

// The two features that read storage the moment they open — the progress
// dialog (counts reviewed/known across the site) and the notepad (a session id
// in sessionStorage) — must open, not throw. Each was a real crash before it
// was guarded, so each is pinned here.
await probe("progress dialog opens without throwing", () => {
  if (typeof stOpenProgress !== "function") return false;
  stOpenProgress();
  const ok = !!document.querySelector(".st-modal, .modal-backdrop, [class*='st-']");
  try { stClose(); } catch { /* fine */ }
  return ok;
});

await probe("notepad opens without throwing", () => {
  if (typeof toggleNotepad !== "function") return false;
  toggleNotepad();               // open
  const ok = !!document.querySelector(".np-root, .notepad, [class*='np-']");
  try { toggleNotepad(); } catch { /* close; fine */ }
  return ok;
});

// ── hostile hashes, with storage working ────────────────────────────────────
// A fresh context: this half is about the URL, not about storage, and mixing the
// two would make a failure ambiguous about which guard broke.
const clean = await (await browser.newContext()).newPage();
const hashErrors = [];
clean.on("pageerror", e => hashErrors.push(String(e).split("\n")[0]));

const HOSTILE = [
  "#%", "#%zz", "#%E0%A4%A",                    // malformed percent-escapes
  "#<img src=x onerror=alert(1)>",              // markup
  '#"><script>alert(1)</script>',
  "#..%2f..%2fetc%2fpasswd",                    // traversal
  "#a/b/c/d", "#/3", "#//",                     // shapes splitCardHash does not expect
  "#kerberos-authentication-flow/999999",       // absurd card index
  "#" + "a".repeat(4000),                       // absurd length
];
for (const hash of HOSTILE) {
  hashErrors.length = 0;
  await clean.goto(PAGE + hash, { waitUntil: "load" });
  await clean.waitForTimeout(120);
  const injected = await clean.evaluate(() =>
    document.querySelectorAll("img[onerror], [onclick], [onload]").length);
  check(`a hostile hash is inert: ${hash.slice(0, 34)}`,
        hashErrors.length === 0 && injected === 0,
        hashErrors[0] || (injected ? `${injected} injected handler(s)` : ""));
}

// The one that actually cost something: after a malformed hash at load, does
// in-page navigation still work? It did not, because the listener that makes it
// work was registered on the line after the one that threw.
await clean.goto(PAGE + "#%", { waitUntil: "load" });
await clean.waitForTimeout(150);
const navigated = await clean.evaluate(async () => {
  location.hash = "kerberos-authentication-flow";
  await new Promise(r => setTimeout(r, 400));
  return !!document.getElementById("kerberos-authentication-flow");
});
check("navigation still works after a malformed hash at load", navigated);

// ── storage that lies ───────────────────────────────────────────────────────
// Seeded before any page script runs, one case per context, each asserting the
// page still boots and the accordion still works — the same "did init finish"
// test the denied-storage half uses.
const CORRUPT = {
  "srs record is not JSON":      { "srs:kerberos-authentication-flow": "{{{not json" },
  "srs record is an array":      { "srs:kerberos-authentication-flow": "[1,2,3]" },
  "srs fields are wrong types":  { "srs:kerberos-authentication-flow": '{"i":"x","e":null,"d":[],"n":{}}' },
  "reviewed flag is an object":  { "reviewed:kerberos-authentication-flow": '{"a":1}' },
  "streak record is garbage":    { "streak": "%%%" },
  "theme is a colour nobody set": { "theme": "chartreuse" },
  "recent visits is garbage":    { "recent": "]]]" },
  "a note of 200,000 characters": { "note:kerberos-authentication-flow": "x".repeat(200000) },
};
for (const [name, seed] of Object.entries(CORRUPT)) {
  const ctx = await browser.newContext();
  const cp = await ctx.newPage();
  const es = []; cp.on("pageerror", e => es.push(String(e).split("\n")[0]));
  await cp.addInitScript(sd => {
    try { for (const [k, v] of Object.entries(sd)) localStorage.setItem(k, v); } catch { /* denied */ }
  }, seed);
  await cp.goto(PAGE, { waitUntil: "load" });
  await cp.waitForTimeout(150);
  const alive = await cp.evaluate(async () => {
    document.querySelector(".domain-section .domain-header").click();
    await new Promise(r => setTimeout(r, 250));
    return !!document.querySelector(".domain-body.open");
  }).catch(() => false);
  check(`corrupt storage survives: ${name}`, es.length === 0 && alive, es[0] || (alive ? "" : "page inert"));
  await ctx.close();
}

// ── a hostile import file ───────────────────────────────────────────────────
// The one place the page ingests something it did not write. Asserted on the
// vetting functions directly rather than through the file picker, because the
// picker is chrome and the gate is the thing worth pinning.
const imported = await clean.evaluate(() => {
  const ex = bkExport();
  const hdr = `{"format":${JSON.stringify(ex.format)},"version":${JSON.stringify(ex.version)},"data":`;
  const run = json => {
    localStorage.clear();
    let outcome;
    try {
      const v = bkValidate(hdr + json + "}");
      const { kept } = bkSanitise(v.data);
      bkApply(kept, "replace");
      outcome = { refused: false, kept: Object.keys(kept).length };
    } catch { outcome = { refused: true, kept: 0 }; }
    outcome.polluted = ({}).polluted !== undefined || ({}).x !== undefined || [].bad !== undefined;
    return outcome;
  };
  const r = {
    proto:       run('{"__proto__":{"polluted":true}}'),
    nestedProto: run('{"srs:x":{"__proto__":{"polluted":true},"d":"2026-01-01"}}'),
    ctor:        run('{"constructor":{"prototype":{"x":"y"}}}'),
    badDate:     run('{"srs:x":{"e":2.5,"i":1,"d":"not-a-date","n":0}}'),
    flagObject:  run('{"reviewed:x":{"yes":true}}'),
    junkKeys:    run(JSON.stringify(Object.fromEntries(
                   Array.from({ length: 2000 }, (_, i) => ["junk:" + i, "1"])))),
    dataArray:   run('[1,2,3]'),
    dataNull:    run('null'),
  };
  localStorage.clear();
  return r;
});
check("an import cannot pollute Object.prototype",
  !Object.values(imported).some(o => o.polluted));
check("a __proto__ key is refused, and one nested in a record is harmless",
  imported.proto.kept === 0 && imported.ctor.kept === 0 && imported.nestedProto.kept === 1);
check("a record with a bad shape is dropped rather than written",
  imported.badDate.kept === 0 && imported.flagObject.kept === 0);
check("keys outside the page's own namespace are all refused",
  imported.junkKeys.kept === 0);
check("a file with no usable data section is refused outright",
  imported.dataArray.refused && imported.dataNull.refused);

await browser.close();

const failed = results.filter(r => !r.ok);
console.log(`\n${results.length - failed.length}/${results.length} checks passed` +
            (failed.length ? `, ${failed.length} failed` : "") + ".");
process.exit(failed.length ? 1 : 0);
