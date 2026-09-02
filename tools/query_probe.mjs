#!/usr/bin/env node
/**
 * query_probe.mjs — what does a reader get when they type what they would type?
 *
 * `search_test.mjs` is the gate: fixtures that must keep working, ceilings that
 * must not be breached. This is the census beside it. It asks a different and
 * softer question — **if a real person came to this site with a real question,
 * would they find the card that answers it?** — over a standing list of queries
 * grouped by who is asking.
 *
 * It exits 0 whatever it finds. A zero here is a finding, not a failure.
 *
 * ## Why this is worth a file
 *
 * Two batches of these queries, run by hand, found five things nothing else on
 * the site could have found: two content gaps that became cards, four places
 * where the site names something one way and readers name it the other, and two
 * structural limits in the matcher. None of them are visible to the depth
 * report, the orphan report, the duplicate census or the linter, because all of
 * those look at what is *there*. This looks at what a reader asked for.
 *
 * Run by hand it also evaporated: the queries lived in a scratch file. Checked
 * in, the zero count is a tracked number like the thin count and the orphan
 * count, and the next session starts from what this one learned.
 *
 * ## The three kinds of zero, and only one is a missing card
 *
 * This is the discipline, and it matters more than the list:
 *
 *   1. **The site says it in the other word.** `impostor syndrome` found
 *      nothing while two cards covered it, because the site spells it
 *      *imposter*. `log4j`, `writing a cv` and `non technical manager` were the
 *      same shape. **Fix in prose** — name both words. It is better writing
 *      anyway, and cheaper than any matcher.
 *   2. **The question is real and the card was not there.** `phishing email
 *      reported` returned nothing against eleven phishing topics, none of which
 *      was "somebody just told me, what now". **Write the card** — but verify
 *      with `near_duplicates.py --title` first.
 *   3. **The question is real and the answer is a phrase, not a card.**
 *      `wifi keeps dropping`, `git detached head`, `terraform state locked`.
 *      The site has the technology card for each and phrases none of them as a
 *      symptom. **Leave these alone.** Seeding symptom phrases into cards is
 *      keyword stuffing with a rationalisation attached; a symptom index is a
 *      different product from a reference, and this is a reference.
 *
 * Kind three is the majority and it is the one that tempts. If a pass over this
 * report produces edits to more than two or three cards, it has stopped being
 * an audit.
 *
 * Usage:
 *   node tools/query_probe.mjs              # every query, grouped by reader
 *   node tools/query_probe.mjs --zero       # only the ones that found nothing
 *   node tools/query_probe.mjs --reader "service desk"
 */

import { existsSync } from "fs";
import { resolve } from "path";

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
    process.exit(2);
  }
})();

const ROOT = resolve(new URL("..", import.meta.url).pathname);
const PAGE = `file://${ROOT}/index.html`;
if (!existsSync(`${ROOT}/index.html`)) {
  console.error("error: index.html does not exist — run 'python build.py' first.");
  process.exit(2);
}

const args = process.argv.slice(2);
const ONLY_ZERO = args.includes("--zero");
const READER = args.includes("--reader") ? args[args.indexOf("--reader") + 1] : "";

// Grouped by who is asking, because that is how the gaps cluster. A query that
// has been investigated and left alone deliberately carries `keep`, naming which
// kind of zero it is — otherwise every future session re-derives it.
const READERS = [
  ["a service desk engineer", [
    ["my computer is slow"],
    ["why is my laptop slow"],
    ["printer offline"],
    ["user forgot password"],
    ["shared drive not mapping"],
    ["account keeps locking out"],
    ["group policy not applying"],
    ["mailbox full"],
    ["onboarding a new starter"],
    ["leaver checklist"],
    ["asset tagging"],
    ["writing a ticket"],
    ["angry user on the phone"],
    ["explaining to a non technical manager"],
    ["wifi keeps dropping", "kind 3 — the site has the wireless cards; none phrases a symptom"],
    ["vpn keeps disconnecting", "kind 3 — same shape as the wireless one"],
    ["laptop won't turn on", "kind 3 — hw covers POST and beep codes, not the symptom"],
    ["outlook won't connect", "kind 3"],
  ]],
  ["a SOC analyst or defender", [
    ["phishing email reported"],
    ["ransomware first hour"],
    ["someone clicked the link", "kind 3 — the response card exists and does not use these words"],
    ["password sprayed"],
    ["usb found in car park"],
    ["log4j"],
    ["what does this alert mean"],
    ["writing a detection"],
    ["chain of custody"],
  ]],
  ["a learner meeting a subject", [
    ["what is a subnet mask"],
    ["what is a default gateway"],
    ["why do we need nat"],
    ["how does a vpn actually work"],
    ["difference between a hub and a switch", "kind 3 — both are covered; the comparison is not phrased"],
    ["what is idempotency"],
    ["what is technical debt"],
    ["why do we use containers"],
    ["why does caching break things"],
    ["what is an embedding"],
    ["should we fine tune or use rag"],
    ["spaced repetition"],
    ["how do adults learn"],
  ]],
  ["a Linux or platform engineer", [
    ["permission denied"],
    ["what is a symlink"],
    ["kill a process"],
    ["cron not running"],
    ["check disk space"],
    ["why is my query slow"],
    ["memory leak in production"],
    ["flaky test"],
    ["merge conflict"],
    ["certificate expired"],
    ["kubernetes pod crashloop"],
    ["s3 bucket public"],
    ["git detached head", "kind 3 — the Git cards do not phrase this state"],
    ["terraform state locked", "kind 3"],
    ["docker image too big", "kind 3"],
  ]],
  ["somebody looking for a job", [
    ["writing a cv"],
    ["asking for a raise"],
    ["impostor syndrome"],
    ["first week as a manager"],
    ["how to study for an exam"],
    ["leaving a job well"],
  ]],
  ["somebody answerable to an auditor", [
    ["do we need iso 27001"],
    ["what is a dpia"],
    ["evidence for an audit"],
    ["third party risk"],
    ["records retention schedule"],
  ]],
];

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto(PAGE, { waitUntil: "load" });

const hitsFor = q => page.evaluate(query => {
  runSearch(query);
  const out = [];
  _searchHits.forEach((set, dom) => set.forEach(id => out.push(`${dom}/${id}`)));
  return { hits: out, note: document.getElementById("search-count")?.textContent || "" };
}, q);

let total = 0, zeros = 0, explained = 0, wide = 0;
const unexplained = [];

for (const [reader, queries] of READERS) {
  if (READER && !reader.toLowerCase().includes(READER.toLowerCase())) continue;
  const rows = [];
  for (const [q, keep] of queries) {
    const { hits } = await hitsFor(q);
    total++;
    if (!hits.length) {
      zeros++;
      if (keep) explained++; else unexplained.push([reader, q]);
    }
    // Wide is not wrong — the widened stage is labelled where it runs — but a
    // query returning a tenth of the site is a query nobody can use.
    if (hits.length > 60) wide++;
    rows.push([q, hits, keep]);
  }
  const show = ONLY_ZERO ? rows.filter(r => !r[1].length) : rows;
  if (!show.length) continue;
  console.log(`\n${reader}\n`);
  for (const [q, hits, keep] of show) {
    const mark = !hits.length ? (keep ? "kept" : "ZERO") : hits.length > 60 ? "wide" : "ok  ";
    const tail = hits.length ? hits[0] : (keep || "nothing — investigate");
    console.log(`  ${mark}  ${JSON.stringify(q).padEnd(40)} ${String(hits.length).padStart(3)}  ${tail.slice(0, 72)}`);
  }
}

await browser.close();

console.log(`\n${total} quer(ies) · ${total - zeros} answered · ` +
            `${zeros} found nothing, of which ${explained} are recorded as deliberate` +
            (wide ? ` · ${wide} returned more than 60` : "") + ".");
if (unexplained.length) {
  console.log(`\n${unexplained.length} unexplained zero(s) — read this file's docstring before ` +
              `acting, then either fix the prose, write the card, or record which kind it is:`);
  unexplained.forEach(([r, q]) => console.log(`  ${JSON.stringify(q)}  (${r})`));
}
console.log("\nA census, not a gate — see this file's docstring.");
