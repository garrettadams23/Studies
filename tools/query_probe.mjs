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
 * ## What the count was worth before every query carried a `want`
 *
 * The third field below existed for a year and was filled in for **one** of the
 * seven reader groups. The other 66 queries were scored by result count alone —
 * the middle row of the three-shapes table this project wrote down a session
 * earlier and then did not apply here:
 *
 *   | Asserts                     | Passes when                 |
 *   | it did not throw            | the feature is broken       |
 *   | it returned something       | the something is wrong      |
 *   | it returned the right thing | —                           |
 *
 * Filling `want` in for all of them moved the headline from **72 of 78
 * answered** to **57**, and the fifteen it exposed are the whole value of the
 * exercise. `printer offline` returned exactly one card — *Bettercap — The MITM
 * Framework* — and had been scored as answered since the file was written. `how
 * do adults learn` missed a topic **titled** *How Adults Actually Learn*.
 *
 * A `want` is only written where one card is the defensible answer. Six queries
 * have none — `user forgot password`, `account keeps locking out`, `log4j`,
 * `what is a symlink`, `memory leak in production`, `leaving a job well`,
 * `evidence for an audit` — and those stay scored by count, because inventing a
 * target to make the number move would be the measurement lying in the other
 * direction. Two of them are content gaps worth a card and are named in
 * plan.md rather than guessed at here.
 *
 * ## The fifteen split three ways, and only one way was the corpus
 *
 * Read one at a time against the wanted card's own text:
 *
 *   1. **One word too many** (9). The subject word is in the card and a filler
 *      word beside it is not. `do we need iso 27001` missed a card titled ISO
 *      27001 over *need*; `check disk space` missed *"The Disk Is Full"* over
 *      *check*. Fixed in the matcher — see the relaxation stage in `script.js`,
 *      which closed three of the nine and left the rest to prose because the
 *      word it would have had to drop was the reader's subject.
 *   2. **The strict stage stopped on a worse card** (2). `kill a process` and
 *      `writing a detection` are in one card each as a literal phrase, so the
 *      search never widens to the card actually about them. That is the
 *      documented "stopped at the first stage that finds anything", meeting a
 *      case where the first stage is right about the words and wrong about the
 *      subject. Recorded, not fixed: preferring a later stage needs ranking,
 *      and this matcher is a filter.
 *   3. **The card does not use the reader's word** (4, and rising as the
 *      matcher takes work off the pile). The Git advanced-workflows card never
 *      says *merge conflict*; the adult-learning card says *spacing* and never
 *      *spaced repetition*; the JML card says *joiner* and never *new starter*.
 *      This is kind 1 above, and the rule for it has not changed: **fix in
 *      prose, because it is better writing anyway.**
 *
 * The split is the finding. Before `want` was filled in, all fifteen looked
 * like the same thing — and twelve of them looked like nothing at all.
 *
 * Usage:
 *   node tools/query_probe.mjs              # every query, grouped by reader
 *   node tools/query_probe.mjs --zero       # only the ones that found nothing
 *   node tools/query_probe.mjs --reader "service desk"
 *   node tools/query_probe.mjs --self-test   # the staleness check, on fixtures
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
    ["my computer is slow", "", "ops/why-is-my-laptop-slow-the-commonest-ticket-worked-properly"],
    ["why is my laptop slow", "", "ops/why-is-my-laptop-slow-the-commonest-ticket-worked-properly"],
    ["printer offline", "", "hw/printers-mfps-technologies-drivers-print-servers-secure-rele"],
    ["user forgot password"],
    ["shared drive not mapping", "", "infra/file-services-share-vs-ntfs-permissions-dfs-quotas"],
    ["account keeps locking out"],
    ["group policy not applying", "", "infra/processing-order-precedence-lsdou-enforcement-loopback"],
    ["mailbox full", "", "m365/retention-litigation-hold-archiving-legals-requirements-in-m"],
    ["onboarding a new starter", "", "m365/joiner-mover-leaver-in-m365-terms-the-process-that-prevents-"],
    ["leaver checklist", "", "m365/joiner-mover-leaver-in-m365-terms-the-process-that-prevents-"],
    ["asset tagging", "", "infra/labelling-asset-tagging-the-boring-discipline-that-pays-out-"],
    ["writing a ticket", "", "ops/writing-a-ticket-someone-else-can-solve"],
    ["angry user on the phone", "", "ops/difficult-conversations-angry-users-vip-pressure-saying-no"],
    ["explaining to a non technical manager", "",
     "ops/explaining-technical-things-to-non-technical-people-a-repeat"],
    ["wifi keeps dropping", "", "net/wireless-troubleshooting-roaming-sticky-clients-its-slow"],
    ["vpn keeps disconnecting", "", "net/vpns-tunneling-secure-connections-over-untrusted-networks"],
    ["laptop won't turn on", "", "hw/post-beep-codes-diagnostic-leds-reading-a-machine-that-will-"],
    ["outlook won't connect", "", "m365/the-m365-troubleshooting-playbook-tenant-identity-licence-po"],
    // ── batch two ──
    ["bitlocker recovery key", "", "endpoint/bitlocker-at-scale-silent-enablement-key-escrow-recovery"],
    ["reset a user's mfa"],
    ["user left who gets their files", "", "m365/joiner-mover-leaver-in-m365-terms-the-process-that-prevents-"],
    ["why is the wifi slow in one room", "", "net/wireless-troubleshooting-roaming-sticky-clients-its-slow"],
    ["screen sharing with a user", "", "ops/remote-support-skills-screen-shares-phone-only-diagnosis-gui"],
  ]],
  ["a SOC analyst or defender", [
    ["phishing email reported", "", "blueteam/a-user-reported-a-phishing-email-the-first-ten-minutes"],
    ["ransomware first hour", "",
     "threat/ransomware-how-it-spreads-and-why-backups-arent-the-whole-st"],
    ["someone clicked the link", "",
     "blueteam/a-user-reported-a-phishing-email-the-first-ten-minutes"],
    ["password sprayed", "", "blueteam/identity-threat-detection-response-itdr"],
    ["usb found in car park", "", "sec/the-hardware-attack-surface-what-physical-access-to-a-device"],
    ["log4j"],
    ["what does this alert mean", "", "blueteam/alert-triage-working-the-queue-from-alert-to-verdict"],
    ["writing a detection", "",
     "blueteam/what-detection-engineering-is-and-why-it-split-off-from-soc-"],
    ["chain of custody", "", "blueteam/chain-of-custody-evidence-handling"],
    // ── batch two ──
    ["is this domain malicious"],
    ["mfa prompt i did not request", "",
     "threat/mfa-bypass-in-practice-adversary-in-the-middle-push-fatigue-"],
    ["how long to keep logs", "", "blueteam/log-retention-as-a-design-decision"],
  ]],
  ["a learner meeting a subject", [
    ["what is a subnet mask", "", "net/ip-addresses-subnets-gently"],
    ["what is a default gateway", "", "net/ip-addresses-subnets-gently"],
    ["why do we need nat", "", "net/nat-port-forwarding-how-private-networks-reach-the-internet"],
    ["how does a vpn actually work", "",
     "net/vpns-tunneling-secure-connections-over-untrusted-networks"],
    ["difference between a hub and a switch", "kind 3 — both are covered; the comparison is not phrased"],
    ["what is idempotency", "",
     "script/scheduling-scripts-the-right-way-cron-timers-and-idempotency"],
    ["what is technical debt", "", "eng/technical-debt-recognize-pay-it-down"],
    ["why do we use containers", "", "linux/docker-containers-package-once-run-anywhere"],
    ["why does caching break things", "", "devops/caching-strategies-from-app-to-cdn"],
    ["what is an embedding", "", "ai/embeddings-rag-giving-ai-access-to-your-own-data"],
    ["should we fine tune or use rag", "",
     "ai/fine-tuning-vs-prompting-vs-rag-picking-the-right-tool"],
    // The first `want` written for this was wrong, and the correction is the
    // rule working: the card that *teaches* the technique — the forgetting
    // curve, the interval ladder, why the software exists — is in productivity.
    // The career card names Spacing in its title and covers it in one table row
    // about teaching other people, which is a different subject with the same
    // word in it.
    ["spaced repetition", "", "productivity/retrieval-practice-why-testing-yourself-beats-rereading"],
    ["how do adults learn", "", "career/how-adults-actually-learn-relevance-practice-feedback-spacin"],
    // ── batch two ──
    ["what is a hash", "", "sec/passwords-hashing-how-logins-are-stored-safely"],
    ["how does dns work", "", "net/dns-the-internets-phone-book"],
    ["what is a load balancer", "", "net/load-balancers-explained-spreading-the-work-around"],
    ["explain oauth", "", "sec/oauth-20-oidc-saml-federated-identity"],
  ]],
  ["a Linux or platform engineer", [
    ["permission denied", "", "linux/linux-file-permissions-model"],
    ["what is a symlink"],
    ["kill a process", "", "linux/process-management-finding-and-taming-runaway-processes"],
    ["cron not running", "", "linux/cron-jobs-scheduling-tasks-in-linux"],
    ["check disk space", "",
     "linux/the-disk-is-full-diagnosing-storage-problems-like-a-calm-pro"],
    ["why is my query slow", "", "data/reading-query-plans-explain-analyze"],
    ["memory leak in production"],
    ["flaky test", "", "devops/flaky-tests-a-reliability-problem-in-the-test-suite"],
    ["merge conflict", "", "script/git-advanced-workflows-beyond-add-commit-push"],
    ["certificate expired", "", "sec/tls-https-how-secure-connections-work"],
    ["kubernetes pod crashloop", "",
     "devops/pods-that-will-not-run-reading-the-status-before-the-logs"],
    ["s3 bucket public", "", "devops/object-storage-s3-the-cloud-storage-model"],
    ["git detached head", "", "script/git-advanced-workflows-beyond-add-commit-push"],
    ["terraform state locked", "kind 1, fixed in prose and still zero — the state card now covers a lock outliving a killed run and force-unlock. The matcher wants the three words adjacent; tuning prose to that is the keyword stuffing this file forbids"],
    ["docker image too big", "kind 3, checked at fault level — devops covers multi-stage builds, .dockerignore, layer caching and image size",
     "devops/docker-deep-multi-stage-builds-image-slimming"],
    // ── batch two ──
    ["ssh permission denied publickey", "", "linux/ssh-secure-remote-access-done-right"],
    // Second `want` this session that was wrong before it was measured: the
    // commands that answer "what is holding this port" live in the performance
    // debugging card's lsof/fuser section, not in process management.
    ["port already in use", "", "linux/performance-debugging-when-you-need-to-go-deeper"],
    ["container exits immediately", "",
     "devops/pods-that-will-not-run-reading-the-status-before-the-logs"],
    ["rotate a secret", "", "sec/secrets-management-stop-hardcoding-passwords"],
    ["out of disk inodes", "",
     "linux/the-disk-is-full-diagnosing-storage-problems-like-a-calm-pro"],
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
    // This row is why the third field exists, and it stayed a recorded miss for
    // several sessions: one incidental literal hit in an unrelated card blocked
    // the widening that would have folded the plural. The single-result
    // escalation in script.js closed it without a word of prose being bent,
    // which is what that note was holding out for.
    ["standups", "", "eng/scrum-three-accountabilities-five-events-three-artifacts"],
    ["our standups are useless",
     "kind 3, same cause — 'standups' carries the query and misses for the reason above; 'our standup is useless' reaches the Daily Scrum row that answers it",
     "eng/scrum-three-accountabilities-five-events-three-artifacts"],
    // ── batch two ──
    ["estimating", "", "eng/planning-without-theatre-roadmaps-velocity-honest-estimates"],
    ["incident postmortem", "", "ops/writing-a-postmortem-people-actually-learn-from"],
    ["on call", "", "ops/on-call-done-humanely"],
  ]],
  ["somebody looking for a job", [
    ["writing a cv", "", "career/your-cv-the-six-second-scan-the-ats-and-what-actually-gets-r"],
    ["asking for a raise", "", "career/asking-for-a-raise-the-case-not-the-conversation"],
    ["impostor syndrome", "", "mind/imposter-syndrome-you-belong-here"],
    ["first week as a manager", "",
     "eng/the-first-90-days-leading-a-team-listen-map-stabilise-then-c"],
    ["how to study for an exam", "",
     "productivity/retrieval-practice-why-testing-yourself-beats-rereading"],
    ["leaving a job well"],
    // ── batch two ──
    ["salary negotiation", "", "career/interview-preparation-getting-the-job"],
    ["technical interview", "", "career/interview-preparation-getting-the-job"],
    ["burnout", "", "mind/burnout-recognizing-it-before-it-breaks-you"],
    ["career change into it", "", "career/breaking-into-it-from-zero-to-hired"],
  ]],
  ["somebody answerable to an auditor", [
    ["do we need iso 27001", "", "grc/nist-csf-iso-27001-grc-frameworks-explained"],
    ["what is a dpia", "", "grc/privacy-law-gdpr-ccpa-for-it-professionals"],
    ["evidence for an audit"],
    ["third party risk", "",
     "grc/third-party-risk-your-security-is-only-as-strong-as-your-ven"],
    ["records retention schedule", "",
     "grc/data-governance-retention-ediscovery-owning-data-on-purpose"],
    // ── batch two ──
    ["gdpr data subject request", "",
     "grc/subject-access-requests-at-scale-building-a-process-that-doe"],
    ["business continuity plan", "",
     "grc/business-continuity-disaster-recovery-keeping-the-lights-on"],
    ["penetration test report", "",
     "pentest/pentest-reporting-the-skill-that-makes-or-breaks-your-career"],
  ]],
];

/**
 * A recorded verdict is only valid while the thing it describes still holds.
 *
 * `someone clicked the link` carried the note *"kind 3 — the response card
 * exists and does not use these words"* long after it stopped being a zero. A
 * matcher change had moved it to four cards, none of them the one it wanted,
 * while a note in this file said it returned none. Nothing noticed, because
 * nothing checks a `keep` note the way `check_plan_numbers.py` checks a table
 * row — and a `keep` note is exactly a claim about a measured state, written in
 * prose, sitting next to the measurement.
 *
 * Only the sharp half of that is checkable, and it is the half that decays:
 *
 *   * A note that **says the query returns nothing** sits on a query that
 *     returns nothing, or it is false. "zero", "found nothing", "returns
 *     nothing", "no results" — the note either makes the claim or it does not,
 *     and the query either is a zero or it is not. No threshold and nothing for
 *     a reader to overrule, which is the shape `check_css_vars.py` argues for.
 *   * A note explaining why a query **misses its `want`** sits on a query that
 *     misses it. One that now reaches the wanted card has had its reason
 *     answered, and leaving the note there hides that the work is done.
 *
 * What it deliberately does not do is judge whether the prose is *right*. A
 * note reading "the comparison is not phrased" could be wrong about the corpus
 * and this cannot tell. It checks the one assertion a note makes that a machine
 * can evaluate and leaves the argument to a reader, which is the division the
 * rest of this file already draws.
 *
 * It reports rather than fails, because this file is a census and gating it
 * would make a content wave's findings break the build. A stale note is worse
 * than a finding, though, so it prints before them and again after.
 */
const CLAIMS_ZERO = /\bzeros?\b|found nothing|returns? nothing|no results|nothing back/i;

function staleReason(keep, hits, want) {
  if (!keep) return null;
  if (hits.length && CLAIMS_ZERO.test(keep))
    return `the note says this returns nothing; it returns ${hits.length}`;
  if (want && hits.includes(want))
    return "the note explains a miss that no longer misses — it reaches its topic";
  return null;
}

const stale = [];

// ── self-test ───────────────────────────────────────────────────────────────
// The staleness check exists because a note went false and nothing noticed. A
// check written for that reason had better be able to catch it, and the only
// way to know is to hand it one. No browser: these are the decision's inputs.
if (args.includes("--self-test")) {
  const F = [
    ["a note claiming a zero on a query that answers", "kind 3 — still zero", ["a/b"], "", true],
    ["…even when the word is plural", "two zeros recorded here", ["a/b"], "", true],
    ["…and when it is spelled out", "it found nothing and was kept", ["a/b", "c/d"], "", true],
    ["a note claiming a zero on a query that is one", "kind 1, still zero", [], "", false],
    ["a note explaining a miss that still misses", "the comparison is not phrased", ["a/b"], "x/y", false],
    ["a note explaining a miss that now reaches", "matcher limit", ["x/y"], "x/y", true],
    ["no note at all", "", ["a/b"], "x/y", false],
    ["a note with no claim this can check", "kind 3, checked at fault level", ["a/b"], "", false],
  ];
  let bad = 0;
  for (const [name, keep, hits, want, expect] of F) {
    const got = Boolean(staleReason(keep, hits, want));
    if (got !== expect) { bad++; console.log(`FAIL : ${name} — expected ${expect}, got ${got}`); }
  }
  console.log(`query_probe self-test: ${F.length} fixtures, ${bad} failure(s).`);
  process.exit(bad ? 1 : 0);
}

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
    const why = staleReason(keep, hits, want);
    if (why) stale.push([reader, q, why]);
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

// Before any finding: a note that has gone false is a defect in this file, not
// a fact about the site, and every number below is read through it.
if (stale.length) {
  console.log(`\n${stale.length} recorded verdict(s) no longer describe the row they sit on — ` +
              `re-read the query, then correct or delete the note:`);
  stale.forEach(([r, q, why]) => console.log(`  ${JSON.stringify(q)}  (${r})\n      ${why}`));
}

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
if (stale.length) {
  console.log(`\n${stale.length} of the recorded verdicts above are stale, and they are the ` +
              `first thing to fix: the counts on this page are read through them.`);
}
console.log("\nA census, not a gate — see this file's docstring.");
