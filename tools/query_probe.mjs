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
 *      `laptop won't turn on`, `git detached head`, `terraform state locked`.
 *      The site has the technology card for each and phrases none of them as a
 *      symptom. **Leave these alone.** Seeding symptom phrases into cards is
 *      keyword stuffing with a rationalisation attached; a symptom index is a
 *      different product from a reference, and this is a reference.
 *
 * Kind three is the majority and it is the one that tempts. If a pass over this
 * report produces edits to more than two or three cards, it has stopped being
 * an audit.
 *
 * ## Telling kind 2 from kind 3, because the first version of this got one wrong
 *
 * `wifi keeps dropping` was listed above as kind 3 — *the site has the
 * technology card*. It had five wireless topics, so that was true at the level
 * it was checked. It was false one level down: the troubleshooting card covered
 * roaming and "it's slow", and its table's one drop row is *drops during a call
 * while walking*. A client that drops while **stationary** is a different fault,
 * and grepping the domain for its causes returned **zero** for radar events,
 * Protected Management Frames, RADIUS `Session-Timeout` and rekeying.
 *
 * So the test is not *does a card on this technology exist*. It is:
 *
 *     name the specific fault the question implies, then grep the domain for
 *     its causes. Kind 3 is when they are there and only the reader's word is
 *     missing. Kind 2 is when the count comes back zero.
 *
 * Every remaining zero has now been through it, and the results split three ways:
 *
 *   * **kind 3, confirmed** — `docker image too big` (multi-stage builds,
 *     `.dockerignore`, layer caching and image size are all in `devops`). The
 *     answer is written out; only the phrasing is absent.
 *   * **kind 3, and wrong.** `laptop won't turn on` and `outlook won't connect`
 *     were recorded here as kind 3 and were nothing of the kind. Their zeros
 *     were the *matcher*: `won't` is not the string `will`, so it survived into
 *     the all-your-words conjunction as a hard requirement almost no card can
 *     satisfy. `laptop will not turn on` returned twenty-five cards the whole
 *     time. Both answer now, and neither needed a word of prose changed — see
 *     the contraction note on `WIDE_STOP` in `script.js`.
 *
 *     The lesson is a rule, and it belongs beside the three kinds above:
 *     **a kind-3 call is a decision not to write something, and it is only sound
 *     once the matcher has been ruled out.** Retype the query with its
 *     contractions expanded, and with its rarest word alone, before concluding
 *     the corpus is at fault.
 *   * **kind 2** — `wifi keeps dropping` and `vpn keeps disconnecting`, above.
 *   * **kind 1** — `git detached head` and `terraform state locked`. The site
 *     *described* both states and named neither: the reflog card tells you to
 *     run `git checkout HEAD@{1}` without saying it detaches HEAD, and then goes
 *     looking for the "dangling" commits that causes. Fixed in prose, which the
 *     rules above call the right answer for kind 1 and better writing anyway.
 *
 * `git detached head` now answers. `terraform state locked` still does not: the
 * matcher wants its three words near each other, and the prose says "a lock held
 * by nothing" and `force-unlock`. **It is left that way on purpose.** The edit
 * was worth making because a lock outliving a killed run was missing from the
 * corpus — `force-unlock` appeared zero times in it — and rewording a sentence
 * to sit better with this matcher is the keyword stuffing the rules above
 * forbid. A zero that stays zero after a justified fix is a better record than a
 * sentence bent to close it.
 *
 * The correction matters more than the two cards did. A kind-3 call is a
 * decision not to write something, and it was being made from a topic list.
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
//
// A third field, `want`, names the topic the query should reach. It is optional
// and filled in as queries are revisited, but where it is present it changes the
// verdict: a query that comes back with cards, none of them the one it was
// asking for, is a miss wearing a result count. `standups` returned one card
// about remote work and was scored as answered for as long as counting was the
// only test — the same failure `search_test.mjs` fixed in its known-miss list,
// arriving here later for the same reason.
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
    ["wifi keeps dropping"],
    ["vpn keeps disconnecting"],
    ["laptop won't turn on"],
    ["outlook won't connect"],
  ]],
  ["a SOC analyst or defender", [
    ["phishing email reported"],
    ["ransomware first hour"],
    ["someone clicked the link", "kind 3 — the response card exists and does not use these words; password reset and session revocation are covered in threat and sec"],
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
        ["git detached head"],
    ["terraform state locked", "kind 1, fixed in prose and still zero — the state card now covers a lock outliving a killed run and force-unlock. The matcher wants the three words adjacent; tuning prose to that is the keyword stuffing this file forbids"],
    ["docker image too big", "kind 3, checked at fault level — devops covers multi-stage builds, .dockerignore, layer caching and image size"],
  ]],
  ["somebody handed a process nobody chose", [
    ["agile",              "", "eng/agile-the-four-trade-offs-and-what-gets-sold-as-agile"],
    ["scrum",              "", "eng/scrum-three-accountabilities-five-events-three-artifacts"],
    ["kanban",             "", "eng/kanban-flow-why-limiting-work-in-progress-is-the-whole-idea"],
    ["sprint planning",    "", "eng/scrum-three-accountabilities-five-events-three-artifacts"],
    ["daily standup",      "", "eng/scrum-three-accountabilities-five-events-three-artifacts"],
    ["user stories",       "", "eng/user-stories-refinement-splitting-work-until-the-estimate-st"],
    ["splitting stories",  "", "eng/user-stories-refinement-splitting-work-until-the-estimate-st"],
    ["definition of done", "", "eng/scrum-three-accountabilities-five-events-three-artifacts"],
    ["product backlog",    "", "eng/scrum-three-accountabilities-five-events-three-artifacts"],
    ["agile isn't working", "", "eng/agile-the-four-trade-offs-and-what-gets-sold-as-agile"],
    ["standups",
     "kind 3, and the reason this file grew a third field. The singular reaches the Scrum card; the plural does not, because the matcher stops at the first stage that finds anything and one incidental literal hit in an unrelated card blocks the widening that would fold the s. A matcher limit, recorded rather than papered over — writing 'standups' into the prose to close it is the keyword stuffing this file forbids",
     "eng/scrum-three-accountabilities-five-events-three-artifacts"],
    ["our standups are useless",
     "kind 3, same cause — 'standups' carries the query and misses for the reason above; 'our standup is useless' reaches the Daily Scrum row that answers it",
     "eng/scrum-three-accountabilities-five-events-three-artifacts"],
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

let total = 0, zeros = 0, explained = 0, wide = 0, wrong = 0;
const unexplained = [];

for (const [reader, queries] of READERS) {
  if (READER && !reader.toLowerCase().includes(READER.toLowerCase())) continue;
  const rows = [];
  for (const [q, keep, want] of queries) {
    const { hits } = await hitsFor(q);
    total++;
    // A query that comes back with cards, none of them the one it was asking
    // for, is a miss wearing a result count. Only a query carrying `want` can
    // be judged that way; the rest are reported by count alone, as before.
    const missed = Boolean(want) && hits.length > 0 && !hits.includes(want);
    if (!hits.length) {
      zeros++;
      if (keep) explained++; else unexplained.push([reader, q, ""]);
    } else if (missed) {
      wrong++;
      if (!keep) unexplained.push([reader, q, want]);
      else explained++;
    }
    // Wide is not wrong — the widened stage is labelled where it runs — but a
    // query returning a tenth of the site is a query nobody can use.
    if (hits.length > 60) wide++;
    rows.push([q, hits, keep, missed, want]);
  }
  const show = ONLY_ZERO ? rows.filter(r => !r[1].length || r[3]) : rows;
  if (!show.length) continue;
  console.log(`\n${reader}\n`);
  for (const [q, hits, keep, missed, want] of show) {
    const mark = !hits.length ? (keep ? "kept" : "ZERO")
               : missed       ? (keep ? "kept" : "MISS")
               : hits.length > 60 ? "wide" : "ok  ";
    const tail = missed ? (keep || `wanted ${want}`)
               : hits.length ? hits[0]
               : (keep || "nothing — investigate");
    console.log(`  ${mark}  ${JSON.stringify(q).padEnd(40)} ${String(hits.length).padStart(3)}  ${tail.slice(0, 72)}`);
  }
}

await browser.close();

console.log(`\n${total} quer(ies) · ${total - zeros - wrong} answered · ` +
            `${zeros} found nothing` +
            (wrong ? ` · ${wrong} found the wrong card` : "") +
            `, of which ${explained} are recorded as deliberate` +
            (wide ? ` · ${wide} returned more than 60` : "") + ".");
if (unexplained.length) {
  console.log(`\n${unexplained.length} unexplained miss(es) — read this file's docstring before ` +
              `acting, then either fix the prose, write the card, or record which kind it is:`);
  unexplained.forEach(([r, q, want]) =>
    console.log(`  ${JSON.stringify(q)}  (${r})${want ? `  — wanted ${want}` : ""}`));
}
console.log("\nA census, not a gate — see this file's docstring.");
