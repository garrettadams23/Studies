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
 * KNOWN_MISSES are queries a reader plausibly types that the search still does
 * not answer, recorded rather than hidden. They fail no build: they are the
 * search-improvement backlog, and the harness prints them so the backlog cannot
 * quietly grow. A miss that starts working is reported too — it should be
 * promoted into FIXTURES.
 *
 * **A miss carries the topic it should reach, and "works" means reaching it.**
 * Counting results alone was the first version and it lied on first contact:
 * the widened-search change made "three way handshake" return three loosely
 * related cards and the harness called it fixed, when the card that answers the
 * question — the site writes "3-way", with a digit — was not among them. Four
 * of the original six misses were genuinely fixed by that change and are now
 * fixtures; this one was not, and the third field is why the harness can tell.
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
  // T7's level operator. The counts are the point: `beginner` is a real layer
  // of the site and `advanced` is eight cards, because eight badges say so.
  ["level:beginner domain:net", "net/wireless-security-80211-standards-wi-fi-hardening", 20],
  ["level:beginner subnetting", "net/subnetting-without-the-headache-cidr-notation-made-practical", 10],
  // T8's since: operator, which the what's-new banner drives through the
  // search box rather than a private code path.
  ["since:2026-07 domain:net", "net/network-topologies", 60],
  // The four the widened fallback promoted. They exercise both of its stages:
  // "wifi 6" and "POAM" are the ordered phrase with its separators folded,
  // "tcp handshake" and "page loads halfway" are all-your-words-anywhere.
  ["tcp handshake",        "net/tcp-vs-udp-transport-layer", 26],
  ["wifi 6",               "net/wireless-networking-80211-standards-security", 8],
  ["page loads halfway",   "net/mtu-fragmentation-the-half-loading-website", 6],
  ["POAM",                 "grc/fedramp-nist-800-53-control-baselines-and-the-ato", 6],
  // The sixth miss was never a search problem. No card contained the words
  // "laptop" and "slow" together, because the site had nothing on the single
  // most common ticket a service desk takes. Writing it closed the query.
  ["why is my laptop slow", "ops/why-is-my-laptop-slow-the-commonest-ticket-worked-properly", 6],
  ["my computer is slow",   "ops/why-is-my-laptop-slow-the-commonest-ticket-worked-properly", 8],
  // A question, not a phrase. It exercises both halves of the widened stage:
  // the function words are dropped, and "fine tune" is rejoined to reach a card
  // that writes it "fine-tune".
  ["should we fine tune or use rag",
   "ai/fine-tuning-vs-prompting-vs-rag-picking-the-right-tool", 8],
  ["explaining to a non technical manager",
   "ops/explaining-technical-things-to-non-technical-people-a-repeat", 20],
  // The last of the original six. The site writes "3-way handshake" with a
  // digit; ten number-word pairs bridge that, and nothing larger is wanted.
  ["three way handshake",  "net/tcp-vs-udp-transport-layer", 12],
  ["the 5 whys",           "ops/writing-a-postmortem-people-actually-learn-from", 6],
];

// Queries a reader plausibly types that still find nothing. Not failures — the
// backlog. Search tries the query as typed, then the same words in order with
// their separators folded, then all of the words anywhere in one card; a query
// survives on this list only when none of the three reaches the right topic.
//
// A third field, the topic the query *should* reach, is what makes this list
// honest. Counting results alone said "three way handshake" had started working
// the moment the widened search returned three loosely-related cards — none of
// them the TCP card, which the site writes as "3-way handshake". A miss that
// returns the wrong answer is still a miss, and now the harness can say so.
// Empty, for the first time since the harness was written. Six queries came in
// with it; four fell to the widened stages, one was a content gap that became a
// card, and the last needed ten number-word pairs. The list is the backlog, so
// an empty one means the next reader question that misses gets added here — not
// that the search is finished.
const KNOWN_MISSES = [];

// Queries with no single right answer that must simply stay narrow. These are
// the index-hygiene guard: chrome rendered into a topic — a badge, a reading
// time, a tooltip — becomes searchable text if the index is built from the raw
// block, and the symptom is one common word matching the whole site. Stamping
// reading times (T6) did exactly that: "min" went from 27 topics to 1,337.
//
// A probe has to be a string that appears *only* in markup. `"class"` was the
// first attempt and is not one: it is an English word, it is over the
// four-character substring threshold, and it legitimately matches 275 topics
// through "classes", "classic" and "classification". A ceiling that fails on
// correct behaviour teaches people to raise ceilings.
const CEILINGS = [
  ["min",           40, "reading-time chrome leaking into the index"],
  ["concept-desc",   0, "card markup leaking into the index"],
  ["topic-header",   0, "header markup leaking into the index"],
  ["data-read",      0, "the T6 attribute itself leaking into the index"],
  ["level:nonsense", 0, "an unknown level must match nothing, not everything"],
  ["since:2099-01",  0, "a future month must match nothing, not everything"],
  // The widened stage's own hygiene. Dropping function words is what lets a
  // question be answered at all, and it is also what makes a vague question
  // wide: "find" and "file" are two real words and a great many cards contain
  // both. Wide is acceptable; the whole site is not.
  ["how do i find a file",       120, "the widened stage losing its remaining nouns"],
  ["why is my domain controller", 90, "the widened stage losing its remaining nouns"],
  // The other end of the same rule. These keep one very common content word —
  // work, time, good — and widening them covers a third to a half of the site.
  // A widened answer that large carries no information, so the cap turns them
  // into "too broad to widen" and they must report nothing at all.
  ["how does it work", 0, "the widened stage answering a question it cannot answer"],
  ["time time time",   0, "the widened stage answering a question it cannot answer"],
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

console.log("\nindex hygiene — a common word must not match the whole site\n");
for (const [q, ceiling, why] of CEILINGS) {
  const hits = await hitsFor(q);
  const ok = hits.length <= ceiling;
  if (!ok) failed++;
  console.log(`${ok ? "ok  " : "FAIL"} : ${JSON.stringify(q).padEnd(24)} ` +
              `${String(hits.length).padStart(4)} result(s)` +
              (ok ? "" : `  — over ceiling ${ceiling}: ${why}`));
}

console.log("\nknown misses — the backlog, reported and not gated\n");
let promoted = 0;
for (const [q, why, want] of KNOWN_MISSES) {
  const hits = await hitsFor(q);
  // "Works" means it reaches the card, not that it returned something. Where
  // no expected card is recorded, any result is progress worth looking at.
  const works = want ? hits.includes(want) : hits.length > 0;
  if (works) {
    promoted++;
    console.log(`  now works : ${JSON.stringify(q)} — ${hits.length} result(s). ` +
                `Move it into FIXTURES with its expected topic.`);
  } else {
    const noise = hits.length ? ` (${hits.length} result(s), none of them ${want})` : "";
    console.log(`  miss      : ${JSON.stringify(q).padEnd(24)} ${why}${noise}`);
  }
}

await browser.close();

const total = FIXTURES.length + CEILINGS.length;
console.log(`\n${total - failed}/${total} search checks passed · ` +
            `${KNOWN_MISSES.length - promoted} known miss(es) still missing.`);
process.exit(failed ? 1 : 0);
