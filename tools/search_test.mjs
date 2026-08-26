#!/usr/bin/env node
/**
 * search_test.mjs — does searching for a thing find it?
 *
 * plan.md Phase 10 T5. The site has search, acronym-aware search and a quiz
 * built on the same index, and until this file nothing checked whether a query
 * a reader would actually type reaches the card that answers it. Every other
 * user-facing behaviour has a smoke test.
 *
 * ## What T5 asked for, and what is actually measurable
 *
 * The plan specified "expected topic in the top three". **There is no top
 * three.** The search is substring matching over a per-domain index and returns
 * an unordered Set; nothing ranks. Scoring against a ranking that does not
 * exist would have been a check measuring something adjacent to its claim,
 * which this repo has now shipped five times and caught five times.
 *
 * So the two things that *are* true of an unranked result set:
 *
 *   1. **Found** — the expected topic is in the hits. This is the regression
 *      test: a content change that renames a card or moves a phrase breaks it.
 *   2. **Scan cost** — how many results the reader must read to find it. With
 *      no ranking, result-set size *is* the quality metric, and a ceiling per
 *      fixture is what stops a query quietly widening to half the site.
 *
 * ## The known misses are the point of the file, not a failure of it
 *
 * KNOWN_MISSES are queries a reader plausibly types that currently return
 * nothing, recorded rather than hidden. They fail no build: they are the
 * search-improvement backlog, and the harness prints them so the backlog cannot
 * quietly grow. A miss that starts working is reported too — it should be
 * promoted into FIXTURES.
 *
 * Usage:
 *   node tools/search_test.mjs                 # build first; this only reads
 *   node tools/search_test.mjs --url <file://>
 */

import { existsSync } from "fs";
import { resolve } from "path";
import { createRequire } from "module";

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

// [query, expected "domain/id", scan ceiling]
//
// The ceiling is generous — roughly double what the query returns today — so it
// catches a query widening to half the site without failing on ordinary growth.
// A fixture whose real count approaches its ceiling wants a narrower query or a
// better search, not a bigger number.
const FIXTURES = [
  ["kerberos",             "sec/kerberos-authentication-flow", 60],
  ["spanning tree",        "net/spanning-tree-why-a-loop-is-catastrophic-and-what-stp-does-a", 25],
  ["subnetting",           "net/subnetting-cidr", 25],
  ["mtu",                  "net/mtu-fragmentation-the-half-loading-website", 12],
  ["one-way audio",        "net/voice-real-time-traffic-why-the-network-is-fine-and-the-call", 8],
  ["wi-fi 6",              "net/wireless-networking-80211-standards-security", 10],
  ["revoke before reset",  "threat/infostealers-the-malware-that-runs-once-and-sells-the-result", 8],
  ["kubernetes rbac",      "cloud/kubernetes-rbac-deep-the-escalation-paths-people-miss", 10],
  ["raid",                 "linux/raid-levels-reference", 25],
  ["systemd",              "linux/systemd-managing-linux-services", 55],
  ["burnout",              "mind/burnout-recognizing-it-before-it-breaks-you", 25],
  ["imposter syndrome",    "mind/imposter-syndrome-you-belong-here", 10],
  ["prompt injection",     "ai/prompt-injection-the-sql-injection-of-the-ai-world", 18],
  ["big o",                "cs/big-o-in-practice-what-the-notation-hides", 20],
  ["binary search",        "cs/sorting-searching-why-your-language-picked-the-one-it-did", 25],
  ["regular expressions",  "script/regular-expressions-regex", 12],
  ["risk register",        "grc/the-risk-register-in-practice-wording-ownership-why-most-are", 20],
  ["salary negotiation",   "career/interview-preparation-getting-the-job", 8],
  ["zero trust",           "sec/zero-trust-never-trust-always-verify", 32],
  ["sql injection",        "pentest/sqlmap-sql-injection-tool-reference", 40],
  ["incident response",    "ops/incident-response-lifecycle-picerl", 110],
];

// Queries a reader plausibly types that find nothing today. Not failures — the
// backlog. Search is whole-string substring matching, so a natural-language
// query only lands if the site happens to contain that exact run of words.
const KNOWN_MISSES = [
  ["tcp handshake",         "two words that never appear adjacent"],
  ["three way handshake",   "the site writes it 'three-way'"],
  ["wifi 6",                "the site writes it 'Wi-Fi 6'; only the hyphenated form matches"],
  ["why is my laptop slow", "a whole sentence; nothing matches it as a substring"],
  ["page loads halfway",    "the MTU card says 'half-loading'"],
  ["POAM",                  "the dictionary entry is 'POA&M' and the map keys on that"],
];

const browser = await chromium.launch();
const page = await (await browser.newContext()).newPage();
await page.goto(PAGE, { waitUntil: "load" });

const hitsFor = q => page.evaluate(q => {
  runSearch(q);
  const out = [];
  _searchHits.forEach((set, dom) => set.forEach(id => out.push(`${dom}/${id}`)));
  return out;
}, q);

let failed = 0;
console.log("fixtures — the expected topic must be found, within its scan ceiling\n");
for (const [q, want, ceiling] of FIXTURES) {
  const hits = await hitsFor(q);
  const found = hits.includes(want);
  const within = hits.length <= ceiling;
  const ok = found && within;
  if (!ok) failed++;
  const why = !found ? "NOT FOUND" : !within ? `${hits.length} > ceiling ${ceiling}` : "";
  console.log(`${ok ? "ok  " : "FAIL"} : ${JSON.stringify(q).padEnd(24)} ` +
              `${String(hits.length).padStart(4)} result(s)${why ? "  — " + why : ""}`);
}

console.log("\nknown misses — the backlog, reported and not gated\n");
let promoted = 0;
for (const [q, why] of KNOWN_MISSES) {
  const hits = await hitsFor(q);
  if (hits.length) {
    promoted++;
    console.log(`  now works : ${JSON.stringify(q)} — ${hits.length} result(s). ` +
                `Move it into FIXTURES with its expected topic.`);
  } else {
    console.log(`  miss      : ${JSON.stringify(q).padEnd(24)} ${why}`);
  }
}

await browser.close();

console.log(`\n${FIXTURES.length - failed}/${FIXTURES.length} search fixtures passed · ` +
            `${KNOWN_MISSES.length - promoted} known miss(es) still missing.`);
process.exit(failed ? 1 : 0);
