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
 * ## The one kind-1 zero whose kind-1 remedy is wrong
 *
 * Kind 1's example is a spelling — the site writes *imposter*, the reader types
 * *impostor* — and its remedy is to name both words in the card. That works
 * because it is **one word**, chosen once, in one place.
 *
 * `should i specialise or generalise` looks identical and is not. The site is
 * written in American English by convention (`CONTRIBUTING.md`, enforced through
 * `data/renames.json`), so the disagreement is not a word the writer picked; it
 * is an orthographic rule applied to every word of its shape. Naming both
 * spellings in the card closes exactly this query and no other, and doing it
 * everywhere is the keyword stuffing kind 3 forbids, dressed as an accommodation
 * to readers.
 *
 * So the test that separates them: **could the writer have chosen the reader's
 * word without changing anything else?** If yes it is kind 1 and belongs in the
 * prose. If the reader's word is the site's own word under a spelling rule, the
 * card is not the place — the matcher is, and `script.js` carries the
 * `-ise`/`-ize` equivalence for the same reason it carries `3-way`/`three-way`:
 * the site and the reader disagree and neither of them is wrong.
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

import { existsSync, readFileSync } from "fs";
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
// Checking the plan row against a filtered run would compare the whole row to
// part of a census, and pass or fail for the wrong reason.
const CHECK_PLAN = args.includes("--check-plan");
const READER_ARG = args.includes("--reader");
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
    ["asset tagging", "", "infra/labeling-asset-tagging-the-boring-discipline-that-pays-out-a"],
    ["writing a ticket", "", "ops/writing-a-ticket-someone-else-can-solve"],
    ["angry user on the phone", "", "ops/difficult-conversations-angry-users-vip-pressure-saying-no"],
    ["explaining to a non technical manager", "",
     "ops/explaining-technical-things-to-non-technical-people-a-repeat"],
    ["wifi keeps dropping", "", "net/wireless-troubleshooting-roaming-sticky-clients-its-slow"],
    ["vpn keeps disconnecting", "", "net/vpns-tunneling-secure-connections-over-untrusted-networks"],
    ["laptop won't turn on", "", "hw/post-beep-codes-diagnostic-leds-reading-a-machine-that-will-"],
    ["outlook won't connect", "", "m365/the-m365-troubleshooting-playbook-tenant-identity-license-po"],
    // ── batch two ──
    ["bitlocker recovery key", "", "endpoint/bitlocker-at-scale-silent-enablement-key-escrow-recovery"],
    ["reset a user's mfa"],
    ["user left who gets their files", "", "m365/joiner-mover-leaver-in-m365-terms-the-process-that-prevents-"],
    ["why is the wifi slow in one room", "", "net/wireless-troubleshooting-roaming-sticky-clients-its-slow"],
    ["screen sharing with a user", "", "ops/remote-support-skills-screen-shares-phone-only-diagnosis-gui"],
    // ── batch nine ──
    ["teams meeting audio not working", "",
     "m365/teams-call-quality-cqd-the-network-requirements-the-real-cul"],
    // ── batch eleven ──
    ["my email went to spam", "", "threat/email-authentication-spf-dkim-dmarc"],
    ["is this email a scam", "",
     "sec/phishing-beyond-email-smishing-vishing-and-qr-code-scams"],
    // ── batch twelve ──
    ["shared mailbox or distribution list", "",
     "m365/microsoft-365-groups-the-object-underneath-teams-sharepoint-"],
    ["the meeting invite is an hour out", "",
     "m365/calendar-time-zones-why-the-invite-lands-an-hour-out"],
    ["setting up a new laptop", "",
     "endpoint/windows-autopilot-zero-touch-provisioning"],
    // ── batch thirteen ──
    ["onedrive is not syncing"],
    ["teams keeps signing me out"],
    ["the user says the file is gone",
     "kind 3 — the recovery ladder is real and spread across three m365 cards (site recycle bin, retention, backup); no single card is the defensible want"],
    // ── batch fourteen ──
    ["the printer is printing garbage", "",
     "hw/printers-mfps-technologies-drivers-print-servers-secure-rele"],
    ["i cannot install software"],
    ["my password expired and i cannot change it"],
    // ── batch sixteen ──
    ["the user cannot sign in on their phone"],
    ["the meeting room screen is blank", "",
     "hw/conference-room-technology-the-av-stack-and-why-it-always-br"],
    // ── batch seventeen ──
    ["how do i prove it is not the network",
     "wide and inherent, and the widest noun this site has: `network` is the only word left after the stop list drops `how do i prove it is not the`, and it is in a fifth of the corpus. The answer is inside the set — `ops` *Troubleshooting Like a Pro* and `net`'s own troubleshooting cards are all in the 83. Ranking would pick between them; this matcher is a filter"],
    ["the user has two accounts"],
    ["the software installed but does not appear"],
    // ── batch eighteen ──
    ["the user changed their name"],
    ["everyone in one office cannot print"],
    ["the new starter is missing from teams",
     "kind 3 — `starter` at 12 is the binding word and it is the reader's noun for a joiner. `m365` covers the fault as a mechanism: group-based licensing, license assignment, and the joiner half of joiner-mover-leaver. The lag between an account existing and Teams showing it is licensing, and the card says so in the site's words"],
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
    // ── batch five ──
    ["nmap shows filtered", "", "net/nmap-scan-types-reference"],
    // ── batch seven ──
    ["we failed a phishing test", "",
     "grc/security-awareness-turning-people-into-a-defense-layer"],
    ["an employee is leaving and we think they took data", "",
     "sec/offboarding-as-a-security-control-the-checklist-and-its-fail"],
    ["we have no idea what is on our network"],
    ["how do i escalate privileges on linux", "",
     "pentest/privilege-escalation-from-foothold-to-full-control"],
    ["my payload keeps getting caught"],
    // ── batch six ──
    ["too many false positives", "",
     "blueteam/writing-a-good-rule-specificity-false-positive-analysis-the-"],
    // Recorded as an unsolvable kind 3 for eight batches, with the diagnosis
    // exactly right: "'got' is a verb no reference card has reason to contain,
    // and a zero cannot be relaxed". The conclusion it drew — leave it — was
    // the wrong one: the verb never being in a card is the argument for
    // stopping it, not for accepting the zero. WIDE_STOP learned `got`, and
    // this reaches its card. The staleness check is what said so.
    ["we got a vulnerability report from a stranger", "",
     "pentest/responsible-disclosure-bug-bounties-reporting-a-flaw-without"],
    // ── batch two ──
    ["is this domain malicious"],
    ["mfa prompt i did not request", "",
     "threat/mfa-bypass-in-practice-adversary-in-the-middle-push-fatigue-"],
    ["how long to keep logs", "", "blueteam/log-retention-as-a-design-decision"],
    // ── batch twelve ──
    ["is the attacker still in"],
    ["a laptop is beaconing out",
     "kind 3 — 'beaconing' alone reaches 11 cards; 'laptop' and 'out' are the reader's words"],
    ["data is leaving over dns", "",
     "redteam/data-exfiltration-channels-dns-icmp-https"],
    // ── batch thirteen ──
    ["what is this powershell doing"],
    ["impossible travel alert"],
    ["a service account signed in from another country", "",
     "sec/non-human-identity-service-accounts-workloads-and-the-sprawl"],
    // ── batch fourteen ──
    ["the alert says it was blocked do i still care",
     "kind 2, written and still zero. The Alert Triage card had zero mentions of blocked/prevented/contained and now carries two concept cards on it; `blocked alert` and `prevented alert` each return exactly that card. The full sentence fails on `says` and `care`, which a card about prevention has no reason to contain, and the relaxation stage never runs on a zero",
     "blueteam/alert-triage-working-the-queue-from-alert-to-verdict"],
    ["we found crypto mining on a server", "",
     "threat/cryptojacking-mining-is-a-symptom-of-access-not-the-incident"],
    // ── batch sixteen ──
    ["someone is exfiltrating over https",
     "kind 3 — the per-word line names it: the card lacks `exfiltrating`, an inflection of its own title. Writing the participle in would be bending a sentence to the matcher, which the rules above forbid, and the stemmer that would fix it was built and reverted in `b90bd2b`",
     "redteam/data-exfiltration-channels-dns-icmp-https"],
    ["a user got a weird text message",
     "kind 3 — the card lacks only `weird`, which is the reader's **verdict on** the message rather than anything about it. A card describing a smishing attempt has no reason to call it weird, and the card already says `text messages`",
     "sec/phishing-beyond-email-smishing-vishing-and-qr-code-scams"],
    // ── batch seventeen ──
    ["the alert has no hostname"],
    ["which of these two alerts do i work first",
     "wide and inherent — `work` and `first` are function-shaped words this site uses constantly, and `alerts` alone reaches most of `blueteam`. The wanted card is in the set: `alert-triage-working-the-queue-from-alert-to-verdict`, which is about exactly this decision",
     "blueteam/alert-triage-working-the-queue-from-alert-to-verdict"],
    ["a domain admin logged in at 2am",
     "kind 3 — `2am` at 15 is the binding word and it is the reader's detail rather than the site's. The fault is covered as a mechanism: UEBA *baselines normal activity per user/host, then scores deviations*, and `off-hours` and `out of hours` appear ten times across `blueteam` and `threat`. Writing `2am` into a card would be the keyword stuffing kind 3 forbids"],
    // ── batch eighteen ──
    ["the same alert fires every night at the same time"],
    ["we have no logs from before last week"],
    ["the malware sample is password protected"],
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
    // ── batch eight ──
    ["the trolley problem", "",
     "philosophy/ethics-the-three-families-and-using-them-on-a-real-decision"],
    ["what does opsec actually mean", "",
     "military/opsec-operational-security-in-cyber-real-life"],
    ["how do i use vim", "", "shortcut/vim"],
    ["what is big o for",
     "wide, and the one of the three with a cause rather than a corpus: `o` is one character, dropped as a free-floating requirement because a one-character word narrows nothing, so the query collapses to `big` — 114 cards. `big o` returns 10 and `big o notation` returns 2, because a short query is answered by the phrase stage and never reaches this one. The join-instead-of-drop fix was built and reverted: it broke `the 5 whys`, a gated fixture, and narrowing it to letters fails on `what is a c pointer`, which needs `pointer` and not `cpointer`. A corpus-aware version — join only where the joined form exists in the folded text — is decidable and not attempted, because it costs a sweep on every query",
     "cs/big-o-in-practice-what-the-notation-hides"],
    ["i cannot do integrals", "",
     "math/unit-3-integrals-series-area-techniques-differential-equatio"],
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
    ["what is a hash",
     "wide and inherent — `hash` is in a ninth of the site and every use is correct. Eight genuinely relevant cards are in the set, including the wanted one. Only ranking would fix this, and this matcher is a filter by design",
     "sec/passwords-hashing-how-logins-are-stored-safely"],
    ["how does dns work",
     "wide and inherent, same shape as `what is a hash` — relaxes to `dns` + `work`, and DNS is load-bearing across the whole site. Four DNS cards are in the set",
     "net/dns-the-internets-phone-book"],
    ["what is a load balancer", "", "net/load-balancers-explained-spreading-the-work-around"],
    ["explain oauth", "", "sec/oauth-20-oidc-saml-federated-identity"],
    // ── batch ten ──
    ["ubermensch", "", "philosophy/philosophy-schools-of-thought"],
    // ── batch eleven ──
    ["i cannot remember any of this", "",
     "productivity/retrieval-practice-why-testing-yourself-beats-rereading"],
    // ── batch twelve ──
    ["authentication vs authorization"],
    ["what is a race condition"],
    ["what is an api gateway"],
    // ── batch thirteen ──
    ["what is a cve"],
    ["why is udp faster"],
    ["what does a 502 mean"],
    // ── batch fourteen ──
    ["what is a webhook"],
    ["why do certificates expire"],
    ["what is a reverse proxy"],
    // ── batch sixteen ──
    ["what does stateless mean"],
    ["what is a container registry"],
    // ── batch seventeen ──
    ["what is a semaphore"],
    ["what is a foreign key"],
    ["why do we need message queues"],
    ["what is a null pointer"],
    // ── batch eighteen ──
    ["why is base64 not encryption"],
    ["what is a service principal"],
    ["what is dns propagation"],
    ["what is a bloom filter"],
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
    // ── batch nine ──
    ["my ssh key stopped working", "", "linux/ssh-secure-remote-access-done-right"],
    // ── batch twelve ──
    ["disk is full but du shows nothing"],
    ["too many open files"],
    ["the clock on the server is wrong"],
    ["dns works on the host but not in the container"],
    // ── batch thirteen ──
    ["systemd service will not start"],
    ["the pod is pending"],
    ["why is my container using so much memory"],
    // ── batch fourteen ──
    ["how do i find what is using a port"],
    ["the log file is huge"],
    ["the service starts then dies"],
    // ── batch fifteen ──
    ["why is my table bloated", "",
     "data/locking-mvcc-concurrency-without-chaos"],
    ["autovacuum is running but bloat keeps growing", "",
     "data/locking-mvcc-concurrency-without-chaos"],
    // ── batch sixteen ──
    ["how do i see what changed on this server"],
    ["i cannot find the big files"],
    // ── batch seventeen ──
    ["the mount disappeared after reboot",
     "kind 3, checked at fault level rather than keyword level — `linux` covers the whole fault: *make it permanent, add to /etc/fstab*, UUIDs over `/dev/sdb1` because *device names can change between boots*, `mount -a` to test without rebooting, and `nofail` on non-essential mounts so a missing disk is not a boot failure. `disappeared` at 2 is the binding word and it is the reader's verb for a mount that was never persisted"],
    ["my container image is not updating"],
    ["which process is writing to the disk"],
    // ── batch eighteen ──
    ["sudo stopped working"],
    // kind 2, and written: `defunct` returned zero site-wide, and every one of
    // the nine `zombie` mentions was a cloud-cost zombie — an unattached disk,
    // not a process. The card is in `Processes & Signals`, where the signals
    // table already ends on "keep SIGKILL for the process that has already
    // ignored a polite request", which is the one case where it does nothing.
    ["the process is defunct", "",
     "linux/processes-signals-running-programs-in-linux"],
    ["too many redirects"],
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
    // ── batch six ──
    ["our estimates are always wrong", "",
     "eng/planning-without-theater-roadmaps-velocity-honest-estimates"],
    ["nobody reads the documentation", "",
     "career/documentation-types-docs-as-code-four-kinds-and-why-mixing-t"],
    ["too many alerts", "",
     "ops/alert-fatigue-as-a-reliability-problem-and-testing-runbooks-"],
    ["our standups are useless",
     "kind 3, same cause — 'standups' carries the query and misses for the reason above; 'our standup is useless' reaches the Daily Scrum row that answers it",
     "eng/scrum-three-accountabilities-five-events-three-artifacts"],
    // ── batch two ──
    ["estimating", "", "eng/planning-without-theater-roadmaps-velocity-honest-estimates"],
    ["incident postmortem", "", "ops/writing-a-postmortem-people-actually-learn-from"],
    ["on call", "", "ops/on-call-done-humanely"],
    // ── batch nine ──
    ["nobody writes documentation", "",
     "ops/knowledge-management-kcs-in-practice-and-keeping-articles-fr"],
    // ── batch ten ──
    ["my manager wants an estimate", "",
     "eng/planning-without-theater-roadmaps-velocity-honest-estimates"],
    // ── batch eleven ──
    ["somebody deleted the wrong thing", "",
     "ops/writing-a-postmortem-people-actually-learn-from"],
    // The same question with one extra word, kept as the counter-example.
    // `intern` is rare, so the relaxation stage keeps it and drops the rest —
    // correctly, by its own rule, and the answer is seven cards about nothing.
    // The site has no reason to name an intern, and writing one in to catch
    // the query is the keyword stuffing this file exists to refuse. Kind 3.
    ["the intern deleted the wrong thing",
     "kind 3 — the reader's incidental noun. The generic phrasing above reaches the card; this one asks the site to contain a word it has no reason to contain",
     "ops/writing-a-postmortem-people-actually-learn-from"],
    // ── batch twelve ──
    ["retrospectives are a waste of time", "",
     "career/facilitating-retrospectives-tabletops-neutrality-and-the-har"],
    ["we have too many meetings"],
    // ── batch thirteen ──
    ["we keep missing deadlines"],
    ["how do i say no to a stakeholder"],
    // ── batch fourteen ──
    ["the person who knew left"],
    ["how do i push back on a deadline"],
    // ── batch sixteen ──
    ["the handover was useless",
     "kind 3 — the card lacks only `useless`, the same editorial word that blocks `our standups are useless`. It cannot join WIDE_STOP: `The Risk Register in Practice — Wording, Ownership & Why Most Are Useless` is a topic title, so stopping it would cost that card its own name — the `get`/`gets` case, measured rather than assumed",
     "blueteam/shift-handover-in-a-soc"],
    ["nobody owns this service",
     "wide and inherent — `service` is in a fifth of the site and every use is correct. The subject is real and covered from three sides: `ops` asset and configuration management, `eng` on ownership, and `sec` non-human identity on the population nobody owns. Ranking would pick between them; this matcher is a filter"],
    // ── batch seventeen ──
    ["we have a process and nobody follows it"],
    ["everything is urgent who decides"],
    ["the change board blocks everything"],
    // ── batch eighteen ──
    ["the ticket bounces between teams"],
    ["nobody comes to the postmortem"],
    ["we approve everything because saying no is hard"],
  ]],
  // ── batch three ──────────────────────────────────────────────────────────
  // Aimed at the domains the first two batches barely touched — data, web, cs,
  // cloud — and phrased as the symptom a reader arrives with rather than the
  // subject a writer files it under. That phrasing is the point: five of these
  // reached a card that covered the mechanism thoroughly and never named the
  // sentence the reader would type.
  ["somebody debugging their own code", [
    ["my query returns duplicates", "", "data/sql-joins-every-type-and-the-null-traps"],
    ["deadlock in the database", "", "data/locking-mvcc-concurrency-without-chaos"],
    ["cors error", "", "web/fetch-rest-cors-in-practice"],
    ["my regex is too slow", "",
     "cs/catastrophic-backtracking-when-a-regular-expression-is-a-den"],
    ["my tests pass individually but fail together", "",
     "devops/test-data-the-constraint-that-shapes-every-environment"],
    ["the build works locally but not in ci"],
    // ── batch four ──
    ["my css is not applying", "",
     "web/the-cascade-specificity-why-the-rule-you-wrote-is-not-applyi"],
    ["the page is blank", "", "web/how-the-browser-renders-a-page"],
    ["encoding error reading a file", "",
     "script/working-with-files-reading-writing-and-paths"],
    ["the script hangs and never exits"],
    // ── batch five ──
    ["my program uses too much memory"],
    // ── batch six ──
    ["circular import", "", "script/modules-packages-pip-using-other-peoples-code"],
    ["list index out of range", "",
     "script/exception-handling-writing-code-that-doesnt-crash"],
    ["my function returns none"],
    // ── batch seven ──
    ["my terraform destroyed something", "",
     "devops/terraform-infrastructure-as-code-in-practice"],
    ["the pipeline is too slow", "",
     "devops/build-caches-incremental-builds-where-the-minutes-actually-g"],
    ["my code review comments are ignored", "", "eng/code-review-doing-it-well"],
    // ── batch nine ──
    ["my tests pass locally but fail in ci", "",
     "devops/flaky-tests-a-reliability-problem-in-the-test-suite"],
    // ── batch ten ──
    ["the database is slow", "", "data/query-optimization-sargability-n1"],
    // ── batch twelve ──
    ["floating point rounding is wrong",
     "kind 3 — the card says 'it is not a bug in your code'; 'wrong' is the one word too many, and the relaxation stage deliberately never runs on a zero"],
    ["off by one"],
    ["the api returns 500 and nothing is logged"],
    // ── batch thirteen ──
    ["permission denied but i am root", "",
     "linux/permission-denied-as-root-the-layers-that-outrank-a-mode-bit"],
    ["it works in dev and breaks in prod"],
    // ── batch fourteen ──
    ["my change broke something unrelated"],
    ["the bug only happens in production"],
    // ── batch fifteen ──
    ["two transactions both checked and both committed", "",
     "data/acid-transactions-isolation-levels"],
    ["do i need serializable", "",
     "data/acid-transactions-isolation-levels"],
    ["the same query is fast sometimes and slow other times",
     "kind 3 — every word is in the corpus and no card carries them together, which is what the per-word line under a zero is for. `data` has a concept card titled *The Query That Was Fast and Went Slow: Stale Statistics and the Plan Flip*. The nearby gap is real and narrower: `parameter sniffing` and `cardinality estimat` each return zero site-wide, and they are the intermittent case rather than the one-way flip"],
    ["my sql is slow only for one customer"],
    // ── batch sixteen ──
    ["i cannot reproduce the bug"],
    ["the stack trace is useless",
     "kind 3, same binding word as the handover row — `useless` is the reader's verdict and cannot be stopped. The nearby subject is real and narrower: a trace that points only at framework or async frames"],
    // ── batch seventeen ──
    ["it works the first time and fails after that",
     "wide and inherent — every word is a function word or nearly one. **And the `want` is not decidable, which is the honest half:** the symptom spans `eng` *Idempotency & Exactly-Once*, configuration-management idempotence in `script`, and plain leftover state, and idempotency alone is in ten files. Naming one target to make the number move would be the measurement lying in the other direction"],
    ["the error points at the wrong line"],
    ["my unit test passes but the feature is broken"],
    // ── batch eighteen ──
    ["the test suite takes forty minutes"],
    ["i changed one line and fifty tests failed",
     "kind 3, and the thinnest of the five — `eng` has *Over-mocking* and *Test Doubles*, which is the cause, but the site names it from the writer's side (a test coupled to the implementation) and never from the reader's (fifty red tests after a one-line change). The nearby gap is narrower than a card: the symptom sentence is missing from a subject that is otherwise covered"],
    ["the log says success and the data is wrong"],
  ]],
  ["somebody in front of the machine itself", [
    ["computer randomly restarts", "",
     "hw/intermittent-faults-heat-vibration-marginal-power-how-to-rep"],
    ["no display on the monitor", "",
     "hw/displays-panel-types-scaling-color-the-multi-monitor-pitfall"],
    ["raid array degraded", "",
     "infra/raid-erasure-coding-what-redundancy-buys-and-the-rebuild-win"],
    ["the server is out of memory", "",
     "linux/performance-debugging-when-you-need-to-go-deeper"],
    ["backup job failed"],
    ["blue screen"],
    // ── batch nine ──
    ["laptop battery drains fast", "",
     "hw/laptops-batteries-thermals-what-is-actually-replaceable"],
    ["the printer prints blank pages", "",
     "hw/printers-mfps-technologies-drivers-print-servers-secure-rele"],
    // ── batch twelve ──
    ["usb device not recognised"],
    ["the fans are always loud"],
    // ── batch thirteen ──
    ["the screen is flickering", "",
     "hw/displays-panel-types-scaling-color-the-multi-monitor-pitfall"],
    ["it will not boot from usb"],
    // ── batch fourteen ──
    ["the keyboard types the wrong characters"],
    ["slow since the update"],
    ["the laptop smells of burning", "",
     "hw/laptops-batteries-thermals-what-is-actually-replaceable"],
    // ── batch sixteen ──
    ["the wifi adapter disappeared",
     "kind 3 — `disappeared` at 2 is the binding word and it is the reader's narration. `wifi` reads 44 once folded, which the per-word line reported as 4 until it folded both sides the way the matcher does"],
    // ── batch seventeen ──
    ["one stick of ram or two"],
    ["the drive is clicking"],
    // ── batch eighteen ──
    ["it posts but windows will not start"],
    ["the usb ports on one side stopped working",
     "kind 3 — the reader's fault is *a whole controller or front-panel header, not a port*, which is the right diagnosis and is the shape `hw` teaches throughout: isolate, swap, halve. `usb` at 31 and `header` at 33 are both in the corpus; no card carries them with `side`, which is the reader's word for a physical grouping the site describes electrically"],
  ]],
  ["somebody with a cloud bill and a pager", [
    ["my lambda times out", "", "cloud/aws-serverless-containers-lambda-ecs-eks-fargate"],
    ["why is my cloud bill so high", "", "devops/finops-cloud-cost-management"],
    ["the load balancer says unhealthy", "",
     "net/load-balancers-explained-spreading-the-work-around"],
    ["iam permission denied", "", "cloud/aws-iam-deep-assumerole-sts-boundaries"],
    ["i deleted something in production"],
    // ── batch four ──
    ["the device shows non compliant", "",
     "endpoint/compliance-policies-deep-settings-grace-periods-what-non-com"],
    ["the model keeps making things up", "",
     "ai/hallucination-why-models-fabricate-and-what-actually-reduces"],
    ["rag returns irrelevant chunks", "",
     "ai/retrieval-augmented-generation-rag-explained-simply"],
    ["my prompt works sometimes", "", "ai/using-ai-well-prompting-responsibility"],
    // ── batch nine ──
    ["kubernetes pod crashloopbackoff", "",
     "devops/pods-that-will-not-run-reading-the-status-before-the-logs"],
    // ── batch ten ──
    ["i got paged at 3am again", "", "ops/on-call-done-humanely"],
    // ── batch twelve ──
    ["image pull backoff"],
    ["the certificate renewed and the site still says expired",
     "still zero after the card was fixed, and deliberately — the renewed-and-not-reloaded row went into the TLS card because its table was missing a failure and its verdict claimed the incomplete chain was the only one; 'site' and 'says' are the reader's filler, and the conjunction cannot drop them because the relaxation stage never runs on a zero",
     "sec/tls-https-how-secure-connections-work"],
    ["nat gateway is the biggest line on the bill",
     "kind 3 — cloud states the NAT gateway is billed hourly plus per GB per AZ; the ranking is the reader's framing"],
    // ── batch thirteen ──
    ["s3 access denied"],
    ["the alert fired and nothing was wrong"],
    ["terraform plan shows changes i did not make"],
    // ── batch fourteen ──
    // Scored answered by count alone since it was added, and it reached five cards
    // none of which was about a deploy that did not deploy. It has a target now,
    // and the card that answers it was written the day this was noticed.
    ["the deploy succeeded but nothing changed", "",
     "devops/artifact-registry-management"],
    ["the autoscaler keeps flapping", "",
     "eng/autoscaling-in-practice-the-metric-the-lag-and-why-it-oscill"],
    // ── batch sixteen ──
    ["my costs doubled overnight",
     "kind 3 — `doubled` at 4 is the binding word. `devops` FinOps and `cloud` cover cost spikes; nothing has a reason to say a bill doubled"],
    // ── batch seventeen ──
    ["we are paying for something nobody uses"],
    ["the alert pages the wrong person"],
    ["staging costs as much as production"],
    // ── batch eighteen ──
    ["we cannot tell which team owns this spend"],
    ["the pager fires for things nobody fixes"],
    // kind 2, named in one wave and written in the next. `cloud`'s *Commitment
    // Discounts* was thorough on **buying** — a commitment is a bet on your own
    // forecast, commit the floor and never the ceiling — and had nothing on the
    // other end. Expiry is a diary problem rather than a forecast one, and it
    // is diagnosed as a technical incident for days because the usage graph is
    // flat across the step.
    ["our reserved instances expired", "",
     "cloud/commitment-discounts-reserved-savings-plans-the-forecast-the"],
  ]],
  ["somebody looking for a job", [
    ["writing a cv", "", "career/your-cv-the-six-second-scan-the-ats-and-what-actually-gets-r"],
    ["asking for a raise", "", "career/asking-for-a-raise-the-case-not-the-conversation"],
    ["impostor syndrome", "", "mind/imposter-syndrome-you-belong-here"],
    ["first week as a manager", "",
     "eng/the-first-90-days-leading-a-team-listen-map-stabilize-then-c"],
    ["i keep procrastinating", "",
     "productivity/procrastination-what-it-actually-is-and-the-moves-that-work"],
    ["which cert should i do first", "",
     "career/certification-roadmap-charting-a-path-through-the-alphabet-s"],
    ["how to study for an exam", "",
     "productivity/retrieval-practice-why-testing-yourself-beats-rereading"],
    ["leaving a job well"],
    ["my manager micromanages me", "",
     "mind/a-manager-you-cannot-fix-what-is-yours-to-change-and-what-is"],
    // ── batch two ──
    ["salary negotiation", "", "career/interview-preparation-getting-the-job"],
    ["technical interview", "", "career/interview-preparation-getting-the-job"],
    ["burnout", "", "mind/burnout-recognizing-it-before-it-breaks-you"],
    ["career change into it", "", "career/breaking-into-it-from-zero-to-hired"],
    // ── batch nine ──
    ["should i get a degree or certs", "", "career/breaking-into-it-from-zero-to-hired"],
    // ── batch ten ──
    ["what should i put on my resume", "",
     "career/your-cv-the-six-second-scan-the-ats-and-what-actually-gets-r"],
    // ── batch twelve ──
    ["tell me about yourself"],
    ["no experience but i want the job"],
    // ── batch thirteen ──
    ["how do i explain a gap in my cv"],
    ["i failed the interview"],
    // ── batch fourteen ──
    ["rejected with no feedback"],
    ["how long should i stay in a job"],
    // ── batch sixteen ──
    // Batch sixteen's one genuine content gap, and it took three fixes to
    // close rather than the one it looked like. The card was written; the
    // query stayed at zero because the card said `specialist` and
    // `specialization` and never the verb — ordinary kind 1, fixed in prose.
    // It stayed at zero in *this* spelling after that, which is the dialect
    // case the docstring sets out. Kept in the reader's spelling on purpose:
    // it is the half the site cannot fix in prose, so it is the half worth
    // watching.
    ["should i specialise or generalise", "",
     "career/specialist-or-generalist-the-choice-and-when-you-actually-ge"],
    // ── batch seventeen ──
    ["i have no portfolio"],
    ["should i take a pay cut to change field"],
    // ── batch eighteen ──
    // kind 1, fixed in prose: `mind` has a whole topic on it and said *goes
    // through this*, while `laid` returned zero site-wide. It now says what the
    // reader says, which is also the plainer sentence.
    ["i got laid off", "",
     "mind/layoffs-job-loss-the-first-week-and-the-ones-after"],
    ["the job ad wants ten years of a five year old tool",
     "kind 3 — every word is in the corpus, `job description` and `years of experience` both appear, and `career` covers reading an advert as a wish list rather than a specification. The query is a joke with a real question inside it, and the joke is what carries it: no card has a reason to contain `ten` and `five` about the same tool"],
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
    // ── batch ten ──
    ["our backups have never been tested", "",
     "ops/backup-disaster-recovery-surviving-the-worst-case"],
    // ── batch twelve ──
    ["how long do we keep backups"],
    ["what is soc 2", "",
     "grc/soc-2-trust-service-criteria-for-cloud-service-providers"],
    // ── batch thirteen ──
    ["what evidence proves mfa is on"],
    ["we outsourced it who is responsible"],
    // ── batch fourteen ──
    ["who approved this change"],
    ["we have no asset inventory"],
    // ── batch sixteen ──
    ["what is our data retention policy"],
    // ── batch seventeen ──
    ["the auditor wants a screenshot"],
    ["we cannot prove who had access last year"],
    ["the policy says one thing and we do another"],
    // ── batch eighteen ──
    ["who signed off on this exception"],
    ["the vendor will not fill in the questionnaire",
     "kind 3, checked at fault level — `grc` has the whole answer and files it under the phase where the leverage is created rather than the phase where it is missed: *bake security requirements into the contract — SLAs, breach notification, right to audit*. It also ranks the alternative evidence a refusing vendor can still be held to, with what each one is worth. `questionnaire` at 13 is the reader's word for the artefact; the site's word is the clause"],
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
// `\bzeros?\b` matched **zero-touch**, in a note reading "the card is provisioning
// and zero-touch". A hyphen is a word boundary, so the word *zero* inside a
// hyphenated compound satisfied it and a correct note was reported stale — the
// same token-boundary-is-not-a-word-boundary failure `annotate_acronyms.py`
// records for `DP` inside `UDP`, arriving here in a different alphabet. The
// guard is the same shape: require that nothing hyphenates onto either side,
// because *zero-touch*, *zero-trust* and *zero-day* are all subjects this site
// writes about and none of them is a claim about a result count.
// A tenth of the site, near enough, and the number this file has always used.
// Named because it is now a scoring threshold rather than a display one.
const WIDE = 60;

const CLAIMS_ZERO = /(?<!-)\bzeros?\b(?!-)|found nothing|returns? nothing|no results|nothing back/i;

function staleReason(keep, hits, want) {
  if (!keep) return null;
  if (hits.length && CLAIMS_ZERO.test(keep))
    return `the note says this returns nothing; it returns ${hits.length}`;
  // Reaching the wanted card only retires a note when the query is otherwise
  // healthy. A **wide** query reaches its want and is still broken — that is
  // the whole definition of wide, the answer present inside a set nobody can
  // read — so its note is describing the live defect, not a solved one.
  //
  // Found by the rule firing on the three notes written the hour `wide` became
  // a scored outcome. The rule was correct for the case it was written for and
  // had no way to know a second case existed, which is this project's most
  // repeated shape and the reason the fixtures below now cover both.
  if (want && hits.includes(want) && hits.length <= WIDE)
    return "the note explains a miss that no longer misses — it reaches its topic";
  return null;
}

/**
 * The plan row that quotes this census, checked against what it just counted.
 *
 * `check_plan_numbers.py` derives thirteen rows of plan.md's measured-state
 * table and names the four it cannot, *rather than letting them pass as
 * verified*. **Naming is not checking**, and this row proved it: its headline
 * was kept current at *254 of 273* while the three sub-counts in the same
 * sentence said **10 zeros, 1 wrong-card and 3 wide** against a tool printing
 * 18, 1 and 4. The last record to touch them incremented the zeros from 9 to
 * 10 on a run that reported 18.
 *
 * Nothing could see it because the row needs a browser, and `make check` has
 * none by design. But the browser is here, seventeen seconds after this file
 * starts, holding every one of those numbers at the moment it prints them — so
 * the check belongs beside the count, not in the tool that cannot take one.
 *
 * Containment, on digit boundaries, exactly as `present()` does it in the
 * sibling tool: the row is prose and the wording should stay free. That does
 * mean a number the cell mentions for another reason would satisfy it, which is
 * why the drift narrative for this row lives in its session record and the cell
 * carries only the current state. A measured-state row that quotes its own
 * history is a row that can be right about the past and wrong about now.
 */
const PLAN = `${ROOT}/plan.md`;
const PLAN_ROW = "Reader questions answered";

function planCell(text) {
  const header = "| Measure | Value | Tool |";
  const start = text.indexOf(header);
  if (start < 0) return null;
  for (const line of text.slice(start).split("\n").slice(2)) {
    if (!line.startsWith("|")) break;
    const cells = line.trim().replace(/^\||\|$/g, "").split("|").map(c => c.trim());
    if (cells[0] === PLAN_ROW) return cells[1];
  }
  return null;
}

// 6 must not satisfy 60, and 17 must not satisfy 173.
function carries(cell, value) {
  const forms = [String(value), value.toLocaleString("en-US")];
  return forms.some(f => new RegExp(`(?<![\\d,])${f.replace(/,/g, ",")}(?![\\d,])`).test(cell));
}

const stale = [];

// ── self-test ───────────────────────────────────────────────────────────────
// The staleness check exists because a note went false and nothing noticed. A
// check written for that reason had better be able to catch it, and the only
// way to know is to hand it one. No browser: these are the decision's inputs.
if (args.includes("--self-test")) {
  const F = [
    ["a note claiming a zero on a query that answers", "kind 3 — still zero", ["a/b"], "", true],
    ["…but not the word inside a hyphenated compound", "the card is provisioning and zero-touch", ["a/b"], "", false],
    ["…in either direction", "a zero-day is not a result count", ["a/b"], "", false],
    ["…even when the word is plural", "two zeros recorded here", ["a/b"], "", true],
    ["…and when it is spelled out", "it found nothing and was kept", ["a/b", "c/d"], "", true],
    ["a note claiming a zero on a query that is one", "kind 1, still zero", [], "", false],
    ["a note explaining a miss that still misses", "the comparison is not phrased", ["a/b"], "x/y", false],
    ["a note explaining a miss that now reaches", "matcher limit", ["x/y"], "x/y", true],
    ["…but not when the set is still too wide to read", "wide and inherent",
     [...Array(WIDE + 1).keys()].map(n => `d/t${n}`).concat("x/y"), "x/y", false],
    ["…and a wide note on a set that has since narrowed is stale", "wide and inherent",
     ["x/y", "d/t1"], "x/y", true],
    ["no note at all", "", ["a/b"], "x/y", false],
    ["a note with no claim this can check", "kind 3, checked at fault level", ["a/b"], "", false],
  ];
  let bad = 0;
  for (const [name, keep, hits, want, expect] of F) {
    const got = Boolean(staleReason(keep, hits, want));
    if (got !== expect) { bad++; console.log(`FAIL : ${name} — expected ${expect}, got ${got}`); }
  }

  // The row reader, on fixtures, for the same reason: `--check-plan` exists
  // because a number nothing derived drifted by eight, and a deriver nobody
  // has watched fail is a deriver nobody should trust. The digit-boundary
  // cases are the ones that would make it pass while the row was wrong.
  const TABLE = [
    "| Measure | Value | Tool |",
    "|---|---|---|",
    "| Topics | **1,557** across 30 domains | `depth_report.py` |",
    `| ${PLAN_ROW} | **255 of 273** — 17 zeros, 1 wrong-card, 4 wide | \`query_probe.mjs\` |`,
    "| Gates | **42** | `check_gates.py` |",
  ].join("\n");
  const G = [
    ["the row is found in the table", () => planCell(TABLE).startsWith("**255 of 273**")],
    ["a table without the row reads null", () => planCell(TABLE.replace(PLAN_ROW, "Something else")) === null],
    ["a file without the table reads null", () => planCell("nothing here") === null],
    ["the row stops at the table's end", () => planCell(TABLE + "\n\nprose\n| x | y | z |") !== null],
    ["a number the row carries", () => carries(planCell(TABLE), 17)],
    ["a number it does not", () => !carries(planCell(TABLE), 18)],
    ["a thousands-separated number", () => carries("**1,557** across 30", 1557)],
    ["4 must not be satisfied by 42", () => !carries("| **42** |", 4)],
    ["17 must not be satisfied by 173", () => !carries("173 things", 17)],
    ["nor by 2,173", () => !carries("2,173 things", 173)],
    ["0 is a value like any other", () => carries("**0 unexplained**", 0)],
  ];
  for (const [name, fn] of G) {
    let got;
    try { got = fn(); } catch (e) { got = `threw ${e.message}`; }
    if (got !== true) { bad++; console.log(`FAIL : ${name} — got ${got}`); }
  }

  console.log(`query_probe self-test: ${F.length + G.length} fixtures, ${bad} failure(s).`);
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

/**
 * How many topics contain each word of a query, one word at a time.
 *
 * Built after the same diagnosis was reached **by hand five times in one run** —
 * `usb device not recognised`, `the screen is flickering`, `we outsourced it who
 * is responsible`, `why is my table bloated` and `data is leaving over dns` were
 * each a zero because one word of the query is not in the corpus while the
 * subject plainly is. Every one of them took the same three commands to find,
 * and the fifth was against a card written twenty minutes earlier.
 *
 * That is the point at which this file's own argument applies: **six of ten
 * failures were caught by a tool, and the ratio is the case for the tools.** A
 * diagnosis re-derived five times is a diagnosis that should be printed.
 *
 * It separates the two kinds of zero at a glance and needs no judgement to read:
 *
 *   * a word at **0** is the corpus missing the reader's word — kind 1, and the
 *     rule for it is *fix in prose, it is better writing anyway*
 *   * every word present, and still a zero, is the conjunction failing on words
 *     no single card carries together — a matcher limit, and the relaxation
 *     stage deliberately does not run on a zero
 *
 * Deliberately *not* a suggestion engine. It says which word is absent; whether
 * the card should use it is a judgement, and the difference between naming a
 * symptom the reader recognises and keyword stuffing is exactly that judgement.
 */
const wordsFor = (q, want) => page.evaluate(([query, wanted]) => {
  const stop = typeof WIDE_STOP !== "undefined" ? WIDE_STOP : new Set();
  const words = query.split(/\s+/).filter(w => w.length >= 2 && !stop.has(w.toLowerCase()));
  // Folded on both sides, because the matcher is. The first version compared
  // raw lowercase text and reported **`wifi 4`** against a corpus that writes
  // *Wi-Fi* — 40 times in `net` alone. A diagnostic that undercounts is worse
  // than no diagnostic, because it turns a matcher problem into a false "the
  // reader's word is missing" and sends the next session to write prose that
  // was already there.
  //
  // `foldSeparators` is the same function the search uses on both sides of its
  // own comparison, so this counts what the conjunction would have counted.
  const fold = s => foldSeparators(s.toLowerCase());
  const corpus = [];
  domainSections().forEach(section =>
    domainTopics(section.dataset.domain).forEach(t => corpus.push(fold(t.text))));
  // A word can be all over the site and absent from the one card that should
  // answer, which is the case the corpus count cannot see and the commonest
  // shape of a kind-1 miss. `the meeting room screen is blank` reported *every
  // word is here* — `screen` 116, `blank` 29 — while the conference-room card
  // said neither, describing the same fault as *wrong input selected* and
  // *check the display's input source*.
  //
  // Where a query carries a `want`, the useful question is not whether the site
  // has the word. It is whether **that card** does, and that is computable for
  // exactly the queries somebody has already decided the answer for.
  let inWant = null;
  if (wanted) {
    const [dom, id] = [wanted.slice(0, wanted.indexOf("/")), wanted.slice(wanted.indexOf("/") + 1)];
    const t = (domainTopics(dom) || []).find(x => x.id === id);
    if (t) inWant = words.map(w => [w, fold(t.text).includes(fold(w))]);
  }
  return {
    corpus: words.map(w => {
      const needle = fold(w);
      return [w, corpus.reduce((n, text) => n + (text.includes(needle) ? 1 : 0), 0)];
    }),
    inWant,
  };
}, [q, want || ""]);

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
    } else if (hits.length > WIDE) {
      // Wide is not wrong — the widened stage is labelled where it runs — but a
      // query returning a tenth of the site is a query nobody can use, and for
      // thirteen batches this was the one outcome here with **no verdict
      // trail**. Zeros carry a `keep` and are counted explained or not; so do
      // wrong-cards. Wide was incremented into a headline number and forgotten,
      // so three queries sat in it for a year with nothing recorded about
      // whether that was acceptable or nobody had looked.
      //
      // It is now scored like the other two. The difference stays real — a wide
      // result contains the answer and a zero does not — so it is counted
      // separately in the summary and never called a miss.
      if (!keep) unexplained.push([reader, q, want]);
      else explained++;
    }
    const why = staleReason(keep, hits, want);
    if (why) stale.push([reader, q, why]);
    if (hits.length > WIDE) wide++;
    // Only for a zero, and only when nobody has already written the verdict:
    // it costs a corpus sweep per query and a recorded zero has had its
    // diagnosis done once already.
    const absent = (!hits.length && !keep) ? await wordsFor(q, want) : null;
    rows.push([q, hits, keep, missed, want, absent]);
  }
  // A gate prints what failed, not 273 lines of what did not.
  const show = CHECK_PLAN ? []
    : ONLY_ZERO ? rows.filter(r => !r[1].length || r[3] || r[1].length > WIDE)
    : rows;
  if (!show.length) continue;
  console.log(`\n${reader}\n`);
  for (const [q, hits, keep, missed, want, absent] of show) {
    const mark = !hits.length ? (keep ? "kept" : "ZERO")
               : missed       ? (keep ? "kept" : "MISS")
               : hits.length > WIDE ? (keep ? "wide" : "WIDE") : "ok  ";
    const tail = missed ? (keep || `wanted ${want}`)
               : hits.length > WIDE ? (keep || "a tenth of the site — investigate")
               : hits.length ? hits[0]
               : (keep || "nothing — investigate");
    console.log(`  ${mark}  ${JSON.stringify(q).padEnd(40)} ${String(hits.length).padStart(3)}  ${tail.slice(0, 72)}`);
    if (absent && absent.corpus.length) {
      const gone = absent.corpus.filter(([, n]) => n === 0);
      // "every word is here" is true and unhelpful when one of them is here
      // four times. The conjunction requires every word of the query in one
      // card, so the rarest is the binding constraint — the same reasoning the
      // relaxation stage uses when it keeps the rarest word and drops the rest.
      // Naming it turns "investigate" into a place to start.
      const rarest = absent.corpus.slice().sort((a, b) => a[1] - b[1])[0];
      console.log(`        in the corpus: ` +
        absent.corpus.map(([w, n]) => `${w} ${n}`).join(" · ") +
        (gone.length
          ? `\n        → ${gone.map(([w]) => `“${w}”`).join(", ")} ` +
            `${gone.length > 1 ? "are" : "is"} not on the site — the reader's word, not a missing card`
          : `\n        → every word is here; “${rarest[0]}” at ${rarest[1]} is the binding one, ` +
            `and no card carries it with the rest`));
      if (absent.inWant) {
        const missing = absent.inWant.filter(([, ok]) => !ok).map(([w]) => `“${w}”`);
        console.log(`        in ${want}: ` +
          (missing.length
            ? `${missing.join(", ")} ${missing.length > 1 ? "are" : "is"} not in the card that should answer`
            : `every word is in the wanted card — the matcher, not the prose`));
      }
    }
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
if (CHECK_PLAN) {
  if (READER_ARG) {
    console.log("\n::error::--check-plan cannot run with --reader: the row describes the whole census.");
    process.exit(2);
  }
  const cell = planCell(readFileSync(PLAN, "utf-8"));
  if (cell === null) {
    console.log(`\n::error::plan.md no longer has a ${JSON.stringify(PLAN_ROW)} row to check.`);
    process.exit(2);
  }
  const expected = [
    ["answered", total - zeros - wrong],
    ["queries", total],
    ["unexplained", unexplained.length],
    ["zeros", zeros],
    ["wrong-card", wrong],
    ["wide", wide],
  ];
  const gone = expected.filter(([, v]) => !carries(cell, v));
  if (gone.length) {
    console.log(`\n${JSON.stringify(PLAN_ROW)}: the row does not carry ` +
                gone.map(([n, v]) => `${v} (${n})`).join(", "));
    console.log(`    row says  ${cell}`);
    console.log(`    this run  ${expected.map(([n, v]) => `${n} ${v}`).join(" · ")}`);
    console.log("\nThe row is one of the four `check_plan_numbers.py` cannot derive. " +
                "This is where it is derived.");
    process.exit(1);
  }
  console.log(`\nplan.md's ${JSON.stringify(PLAN_ROW)} row carries all six of this run's numbers.`);
  process.exit(0);
}
console.log("\nA census, not a gate — see this file's docstring.");
