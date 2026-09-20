# Plan — the live file

> The roadmap history lives in [`plan-archive.md`](plan-archive.md). This file is what a
> session reads before it starts: how the work is done, what the good cards look like, what
> is being measured, and the most recent records.

## Where things are

This file was 22,745 lines, and its own risk register named that as the problem:
*"the plan outgrows its own readability — the useful part is the last few hundred lines"*,
scored **open, and now acute**. It named the fix too, and the trigger: *option 1 when the
live queue next empties.* The queue emptied — every census clean — so the closed programmes
and 242 session records moved to **`plan-archive.md`**, line for line, nothing edited.

**It has now happened a second time, and on a condition rather than a judgement.** The
threshold the register set for itself — 8,000 lines, reported by `check_plan_numbers.py` on
every run — fired at 8,020, and 45 more records moved the same way. Lines conserved exactly:
28,992 before, 4,227 + 24,765 after. The number that made the first split acute was somebody
noticing; the number that made the second one happen was a tool printing a warning.

What is left here is what a session actually reads.

| Section | What it is | State |
|---|---|---|
| **The session operating manual** | The loop, the ordering constraints, and ten failures with their guards | 📘 **start here** |
| **The card rubric** | What the good cards have, measured from forty written in one session | 📘 reference |
| **Phase 11 — the verification debt** | What is dated, and why the denominator is not countable. A standing discipline, not a queue | 📘 living |
| **The risk register, revisited** | Four accumulation risks that only a measurement could find | 📘 living |
| Domain shape | The connectivity graph: hubs, broadcasters, islands. Both navigation layers complete — 0 hand-written orphans, 0 hand-written topics off a path, and **both halves now derived**: the second was prose for weeks while three topics were off one | 📘 reference |
| Session records | The recent ones. The rest are in `plan-archive.md`, oldest first — **the counts are the *Session records* row of the measured-state table**, and were a second copy here that had been wrong by five since the split | 📘 living |

**Everything closed is in [`plan-archive.md`](plan-archive.md)** — the July 2026 review,
the content roadmaps, Phases 3 to 10, the Execution Handbook, the calculus track and the
worked specifications. It is kept rather than deleted because this file's most-quoted
passages are the ones explaining why something was *rejected*, and nobody would write those
twice.

**The measured state, as of the last session record.** Every number below is produced by a
tool in `tools/`, not by anybody's recollection, and `make census` prints the first four.
Eleven of the fifteen rows are now *checked* by `check_plan_numbers.py` in `make check` —
when it was first run, **nine of those eleven were wrong**, the page budget by a factor of
twelve. The four it cannot derive need a browser or a stopwatch, and it names them on every
run rather than letting them pass as verified:

| Measure | Value | Tool |
|---|---|---|
| Topics | **1,557** across 30 domains | `depth_report.py` |
| Thin (one card, under 1,800 chars) | **7**, 0% — and `--thin` prints badge, position and xref count beside each, because the ones left are short by design. Three of the eight were not: two military lookup cards and a domain preamble each had a judgement they were not making | `depth_report.py` |
| Mean chars per concept card | **1,394**, or **1,124 excluding verdicts** — the second is the padding counter-metric. It has tracked the first within two across every wave this session, which is the shape to want: the two numbers moving together | `depth_report.py` |
| Orphans | **60**, every one generated, **0 deep** | `orphan_report.py` |
| Near-duplicate pairs | **95** (41 by overlap, 54 by containment) — 78 explained by §3, 17 read and recorded, **0 unread** | `near_duplicates.py` |
| Reader questions answered | **255 of 273**, **0 unexplained** — sixteen batches. The two subject-shaped ones opened at a third missing; the nine symptom-shaped ones at **two thirds**, and that gap is the census's most repeated finding. The 17 remaining zeros, the 1 wrong-card and the 4 wide results are recorded verdicts — and those three sub-counts had drifted to 10, 1 and 3 while the headline beside them was kept current, because this row is one of the four nothing derives. The staleness check reports a verdict that has stopped describing its row, and it has now caught two, both on a note of its own author's: the first time the note was right and the check was wrong — `\bzeros?\b` was matching *zero* inside **zero-touch** — and the second time the note was simply out of date, which is what it is for. The wrong-card one is kept on purpose: `the intern deleted the wrong thing` asks the site to contain a word it has no reason to contain, and writing one in is the keyword stuffing the census exists to refuse | `query_probe.mjs` |
| Learning paths | **102 paths, 1,595 steps, 1,497 of 1,557 topics, 0 hand-written topics off a path** | `check_paths.py` |
| Related links | **1,497 topics, 4,860 links, 0 one-way** — one mainland of **1,481 (98%)** and **one** island: `math`, 16 of 16, which is a decision rather than a backlog. It read *three reference-domain islands* until somebody measured how much of each island's domain was already connected — 29 of `shortcut`'s 36 and 3 of `quotes`' 6 — and `orphan_report.py` prints that figure now | `suggest_related.py --check` |
| Page budget | **34% raw** headroom — room for ~791 more topics | `page_budget.py` |
| Throttled load | **~3.0 s** = 0.5 s shell + 1.0 s script.js + ~190 ms/MB — *this container only* | `measure_load.mjs` |
| Search &amp; heap at 3x the content | **86 ms · 93 MB** at 4,602 indexed topics — search is not the constraint, load is | `measure_load.mjs --synthetic` |
| Depth tail | **10th percentile 2,142 chars**, median 3,740 — the number a deepening wave has to move | `depth_report.py` |
| Dated claims | **47 volatile spans and 12 fact anchors: 59 dated claims**, and **3** console candidates — all three read and recorded as false positives in `context()`'s docstring. The denominator is still not countable and that is Phase 11 §3's whole finding; the numerator always was, and spent a year in prose because nobody noticed the difference. It rose by two in the V2 pass, against §6's counter-discipline that a rising count is not automatically progress — both are limits a card **designs around**, which is the one case §5 says a span is right for, and the same pass rewrote nothing because the other ten claims were never facts about the world | `check_volatility.py` |
| Gates | **42**, and the same 42 in `make all` and in CI | `check_gates.py` |
| Gate results | check · smoke **163** · search **58** · resilience **64** · axe 31/31 · mobile 15/15 · visual 2/2 · backup 3/3 | `make all` |
| Cards ending on a table with no verdict | **10**, all deliberate lookup tables in `military` — two of the original twelve turned out to have a judgement their table was carrying silently | `lint_content.py` |
| Session records | **42** here, **287** in `plan-archive.md` | `check_plan_numbers.py` |

**`make all` is the contract.** If it passes, CI passes — `check_gates.py` fails the build
if the two lists ever diverge again. Before this was true, the workflow had been red on
every push for nine commits and `make check` had been green the whole time.

**Where new work comes from now.** The content programmes (Phases 7–10) are closed and the
navigation ones are complete, so the queue is no longer a list — it is whichever census
reports something a human should read. In practice this session that meant: a reader
question returning nothing (two new cards), a duplicate pair with no stated difference (two
retitles), an acronym expanded wrongly (three fixes), a flashcard with a blank back, a quiz
that answered itself, a search returning half the site, and a stray `%` that killed every
link on the page. **None of those were on any list before the tool that found them ran.**

**If you read three things:** the session operating manual, the card rubric, and the
docstring of whichever census last reported something. Line numbers drift as records are
appended — the headings are stable, the numbers are a hint.
# The session operating manual

> Derived from one long session that shipped fifteen commits and moved the site from 1,401 to
> 1,432 topics. Not a description of how work *should* go — a record of the loop that
> actually worked, the order the tools must run in and why, and the ten specific ways this
> session got something wrong. The failure list is the valuable half.

## 1. The loop

```
 1  AUDIT      probe titles → verify each zero against the domain's real title list
 2  READ       open the two or three nearest existing cards, including their
               concept-card titles — not just their topic titles
 3  DRAFT      write to scratchpad, one file per card, named
 4  SPLICE     an EXPLICIT file list into data/<domain>.html, before the marker
 5  ANNOTATE   make acronyms          ← rewrites content; must precede the build
 6  LINT       python3 tools/lint_content.py   ← fastest signal, run it before building
 7  BUILD      make build
 8  CHECK      make check             ← every static gate, fails fast
 9  BROWSER    make test · make a11y · make visual
10  LINK       add bidirectional pairs to data/related.json, by hand
11  REBUILD    make build && make check       ← the link edit changes the payload
12  SOCIAL     make og                ← the card embeds the topic count
13  RECORD     append a session record to plan.md while the reasons are still in mind
14  COMMIT     one wave, one commit, message says what was found as well as what shipped
15  PUSH       git push -u origin <branch>
```

## 2. Ordering constraints that are not preferences

| Must run before | Because |
|---|---|
| `gen_acronym_domain.py` → `annotate_acronyms.py` | The annotator reads the dictionary the generator emits from |
| `annotate_acronyms.py` → `build.py` | The annotator rewrites `data/*.html`; building first ships unannotated content |
| `lint_content.py` → `build.py` | Not required, but the linter finds cross-reference and slug errors in two seconds that the build takes ninety to surface |
| any content change → `make og` | The social card renders the topic count into the image |
| `related.json` edit → `make build` | The related map is a substituted payload, not a runtime fetch |
| `make build` → `make visual` | The visual test screenshots `index.html` |

**`make check` runs the gates in fail-fastest order** and that ordering is deliberate: markup
before lint before the expensive determinism and budget checks.

## 3. The ten failures this session, and the guard for each

| # | What happened | Guard |
|---|---|---|
| 1 | A scratchpad **glob** picked up two cards from a session two days earlier and shipped two topics twice | **Never glob a scratchpad.** Name the files. The duplicate-slug guard caught it by name with line numbers |
| 2 | **Five invented cross-references** — titles reconstructed from memory: "Long-Term Memory" for "Access to Your Own Data", "Has to Mean" for "Actually Means", "SPF, DKIM & DMARC" for the comma version | The linter names the correction every time. It is cheaper to run the linter than to check the title, so run the linter |
| 3 | Wrote **"whitelist"** where house style is "allowlist" | `check_renames.py`, already in `make check`. First time it caught same-session writing |
| 4 | A stray `<div class="topic-icon-none">` typed into a header | **Nothing catches this.** Re-read the first ten lines of each new card before splicing |
| 5 | A regex audit found `DP` inside `UDP`, `RA` inside `YARA`, `SCP` inside `OSCP` — half a 77-row finding was the regex looking at itself | `(?<![A-Za-z0-9])`. A token boundary is not a word boundary when the tokens are acronyms |
| 6 | Used `class="c-yellow"`, which does not exist | Grep `style.css` for the utility class before using one. Six exist; the rest are `style="color: var(--…)"` |
| 7 | Wrote a related-map target from memory; **slugs truncate at 60 characters** and the real id ended `…funds-i` | `suggest_related.py --check` names the missing target and the resulting one-way edge in the same run |
| 8 | Filed a new acronym under `"c": "Military"` — the acronym domain is generated **by category**, so one entry created a whole `By Area — Military` topic and moved the site count | Check the neighbours before inventing a category. A category field in a generated taxonomy is a structural decision |
| 9 | Probe zeros were **~60% phrasing misses**, including two cards written an hour earlier | Step 1 of the loop. Verify every zero against the real title list |
| 10 | Two wrong acronym expansions shipped in earlier sessions and were found by **reading**, not by any check — `IR` in a compiler card's title, `SMB` in "a home-lab / SMB choice" | The breadth census now surfaces the candidates. It cannot decide them |

**Six of ten were caught by a tool, three by reading, one by nothing.** That ratio is the
argument for both halves: the gates are worth their maintenance, and they are not a substitute
for re-reading what you wrote.

## 4. Session shape

| | Observed this session |
|---|---|
| Cards per commit | 2–5. Five is comfortable; more makes the commit message dishonest about what was checked |
| Time per card | Roughly 20 minutes of writing for a five-concept-card topic, plus the shared verification pass |
| Commit granularity | **One wave, one commit.** A wave is a domain and a theme. Mixing two domains in one commit makes the record useless later |
| What goes in the message | What was *found*, not only what shipped. The `ops` probe that returned nothing is in a commit message, and it is the most reusable line in it |
| When to stop a wave | When the audit's verified list is empty, not when the card count feels round |

## 5. The three habits that produced the good cards

1. **Read the neighbours' concept-card titles, not their topic titles.** An ADHD card was
   dropped before it was written because `productivity`'s *Study Systems That Survive a Brain
   That Won't Cooperate* already carried "design for the bad day" and body doubling — visible
   only from inside the card.
2. **Write the one sentence first.** The rubric's §1 test. Every good card this session had a
   sentence that was the reason it existed, and the ones that came out flat did not.
3. **Verify by measurement, not by assertion.** The 1,142 inline-margin conversion was proved
   with before-and-after screenshots: two byte-identical PNGs and one taller by exactly 10px,
   which was 5 × 2px and the predicted number. "This should be a no-op" is not the same claim
   as "this was".

## 6. What to do at the start of a session

In order, and none of them takes more than a minute:

```
git log --oneline -5              what did the last session do
tail -120 plan.md                 what did it say about why
make check                        is the tree clean before you touch it
python3 tools/lint_content.py     the census lines: thin counters, breadth, ai-tables
python3 tools/check_volatility.py the vendor-console queue
```

The last two exist because **a census nobody reads is decoration**, and this file has made
that mistake once already with a counter that rose 39% while being "tracked".


---

# The card rubric — what the good ones have, measured from what shipped

> Written after roughly forty cards in one session, by looking at which ones came out well
> and asking what they had in common. Not a style guide — the conventions live in
> `CONTRIBUTING.md`. This is about **what makes a card worth reading**, which no file here
> has ever stated, and which is the thing a future session most needs and is least likely to
> reconstruct.

## 1. The one test

**A card earns its place when it says something the reader could not have assembled from the
table alone.**

Every good card this session has one sentence that is the reason it exists:

| Card | The sentence |
|---|---|
| BEC | Every control you bought looks for a payload, and there isn't one |
| MFA Bypass | MFA authenticates a login, not a session |
| Infostealers | Revoke before reset, or the reset locks the door behind the intruder |
| Spanning Tree | An IP packet has a time-to-live; an Ethernet frame has nothing |
| MTU | Small things work and large things hang |
| Mainframe | The specification is the code |
| i18n | It is not translation, it is removing the assumptions that make translation impossible |
| Hallucination | A fabricated citation is formatted exactly as carefully as a real one |
| Anxiety | Avoidance is what keeps it alive |
| Risk register | The test is whether the entry can be wrong |
| Typography | Amateur design is usually not ugly — it is undecided |

If you cannot write that sentence for the card you are about to write, **you do not yet know
what the card is**, and writing it will produce a summary of the subject rather than a
contribution to it.

## 2. The five that all the good ones do

| | Property | What it looks like |
|---|---|---|
| 1 | **Names the inversion** | Says the thing that is true and contrary to instinct. "Call the bank before touching the mailbox." "Security advises and never approves." "A takedown is a window, not a fix" |
| 2 | **Gives the failure a fingerprint** | One-way audio. Solid port lights. Small things work, large things hang. A reader who meets the symptom recognises it, which is the whole return on reading |
| 3 | **Ranks honestly, with the limits** | Not a list of mitigations but a ranked one, each with what it does *not* do. The ranking is the content; an unranked list is a search result |
| 4 | **Says what it is not** | The scope sentence. "This is not a diagnosis." "DMARC is worth doing and is not a BEC control." Naming the boundary is what makes the rest trustworthy |
| 5 | **Ends on a decision** | The verdict is an instruction or a judgement, never a summary. If the last sentence restates the card, delete it and promote the second-to-last |

## 3. The failure modes, with their tells

| Failure | Tell | Fix |
|---|---|---|
| **Encyclopaedia card** | Reads like a definition. Could have been written without ever having used the thing | Find the failure mode. Every subject has one and it is always more interesting than the definition |
| **Listicle** | Seven items, none ranked, no verdict | Rank them. If they cannot be ranked they are not comparable and the table is wrong |
| **Restated verdict** | The closing sentence says what the table said | Cut it. A missing verdict is better than a redundant one |
| **Borrowed authority** | Cites a framework instead of making an argument | Say what the framework is *for*, and when it does not apply |
| **Padding** | Longer, and the concept-card count did not change | Phase 8 §7. Stop at three cards and ship |
| **Invented cross-reference** | A title reconstructed from memory | The linter catches it every time and names the correction. It caught five this session |

## 4. Length, honestly

The good cards this session ran **6,000 to 15,000 characters of source**, four to six concept
cards. That is not a target. The relationship runs the other way: a subject with four real
arguments produces four concept cards, and one with a single argument produces one and is
finished.

**Write until the material runs out, then stop.** The 330 thin cards in Phase 8 are not thin
because someone stopped early — they are thin because they were written to a form that only
had room for one idea.

## 5. What the tooling checks, and what it cannot

Worth stating so nobody assumes a green build means a good card.

| Checked mechanically | Not checked, ever |
|---|---|
| Markup, nesting, duplicate slugs | Whether the card is interesting |
| Cross-reference targets exist | Whether the cross-reference is apt |
| Acronym expansions match the dictionary | Whether the expansion is right *here* — six were wrong this session |
| No hard-coded colours; the verdict class is used | Whether the verdict says anything |
| Contradictions against other cards | Whether the claim is true |
| Freshness stamps, volatile claims dated | Whether the claim was ever verified |

**The checks protect the conventions. Nothing protects the content except the writing.** That
asymmetry is the reason this rubric exists in the same file as the tooling record.


---

# Phase 11 — the verification debt, and a measurement that did not work

Phases 8–10 all begin with a number. This one begins with a **failed attempt at a number**,
which is recorded in full because the failure is more useful than the estimate would have
been.

## 1. What is actually dated

The site carries two conventions for claims that age — `<span class="volatile"
data-checked="…">` for the claim itself, and `<!-- fact: … | source: … | checked: … -->` for
where a number came from. Together they cover the site's dated claims — **the count is the
*Dated claims* row of the measured-state table**, and is not repeated here.

It used to be repeated here, as *46 volatile spans and 5 fact anchors: 51 dated claims
across 1,432 topics*, and every figure in that sentence was wrong by the time anybody
read it. The register three sections down states the rule this section needed — *no number
is repeated here; each row points at the row of the measured-state table that carries its
figure, because a second copy would only be a second thing to go stale* — and wrote it
after being wrong in exactly this way. Phase 11 never got the fix, which is this file's
most-recorded shape: **a rule written for a category tends not to be applied to the case
that motivated it.**

The obvious next question is: 51 out of how many?

## 2. Three attempts to find the denominator, and why each was wrong

**Attempt one — pattern-match anything that looks like a fact.** Percentages, money,
durations, sizes, ports, version numbers, "up to N". Code blocks excluded. Result:
**1,206 matches**, of which 527 were "version numbers".

Reading a sample killed it immediately. The version pattern was matching IP addresses
(`192.168.0.0/16`), protocol names (`802.11`, `TLS 1.3`), availability figures (`99.999%`),
and pinned dependencies in example snippets. Almost none of it ages.

**Attempt two — narrow it.** Strip IP-like strings, availability nines, and standard
identifiers (`802.x`, `TLS 1.x`, `HTTP/2`, `IPv6`, `SHA-256`). Result: **584 matches**, which
looked defensible.

Reading a sample killed that one too. `money` was matching **shell variables** — `$1`, `$0`,
`awk -F:` — from prose that discusses scripting outside a `<pre>` block. `size/rate` was
matching **historical Wi-Fi rates**: "11 Mbps, 2.4 GHz, 1999" is a fact about 802.11b that
will be true forever.

**Attempt three — narrow again.** Not attempted, and that is the finding.

## 3. The conclusion, stated plainly

**There is no mechanical way to count ageing claims on this site at useful precision.** The
distinguishing property is not the *shape* of the text — it is whether the world can change
underneath it, and nothing in the markup carries that.

This is the same failure this file has recorded three times before, and the pattern is now
unmistakable:

| Check | First version matched | Fixed by |
|---|---|---|
| Hard-coded colours | Invoice numbers, ticket numbers, CSS examples | Requiring a colour *context* — a style or paint attribute |
| Ambiguous acronyms | Every note containing "also", including synonyms | Requiring evidence of *real use* in two domains |
| Vendor consoles | MMC, "cloud console", `old-admin.example.com` | Word boundaries and dropping generic phrases |
| **Ageing claims** | IP addresses, Wi-Fi standards, shell variables | **Nothing. There is no property to require** |

The first three had a narrowing available. This one does not, and **the right response to a
check that cannot be narrowed is to not ship it**, rather than to ship it with a footnote
that nobody will read.

## 4. What to do instead — enumerate the classes, not the instances

Ageing claims are not evenly distributed. They cluster in a small number of *kinds*, and
those kinds are enumerable by hand in a way the instances are not.

| Class | Ages because | Where it lives |
|---|---|---|
| **Console names and paths** | Vendors rename consoles every few years | `m365`, `cloud`, `endpoint` — already covered by `check_volatility.py`'s queue; the count is the *Dated claims* row |
| **Console hostnames** | They move — `endpoint.microsoft.com` became `intune.microsoft.com` | Same three domains; the enumerated-host rule added this session catches these |
| **Service limits and quotas** | Raised, lowered, or made configurable | `cloud`, `m365`, `data` — "5,000 items", "93 days", "20 requests per batch" |
| **Tier gating** | "Requires E5" is a licensing decision, not a technical fact | `m365` especially, and it is the class most likely to be quietly wrong |
| **Prices and ranges** | Obviously | `career` (salary and rates), `hw` (build budgets), `cloud` (commitment discounts) |
| **Default retention** | Changed by vendors without announcement | `m365`, `cloud`, `blueteam` |
| **Product names** | Rebranded — `check_renames.py` already guards a list of these | Everywhere; the guard exists and catches the ones it knows |

**The work is a pass per class, not a pass per domain.** Searching the site for "requires E5"
finds every tier-gating claim in one query, and each either gets a dated span or gets
rewritten to remove the dependency — "check the current gating for your tier" is a sentence
that never ages.

## 5. The rewrite that beats dating

Worth stating because it is cheaper than the convention and the convention exists partly
because nobody has said this:

> A claim that is rewritten to not depend on a fact does not need a date.

| Ages | Does not |
|---|---|
| "Retention is 93 days" | "Retention is a tier-dependent default, currently around three months — check it, because it changes" |
| "Requires E5" | "Gated to the higher tiers; the exact gating moves and is worth confirming before designing around it" |
| "Costs about $80–150" | "Used enterprise mini PCs are the cheapest capable option; price them, because the market moves" |

**Dating a claim promises to re-check it. Rewriting it removes the promise.** The volatile
span is right where the specific number is the point — a limit you must design around. It is
the wrong tool where the number was only ever illustrative, and a good share of the 584
near-matches in §2 are that second kind.

## 6. The queue

| Wave | Class | Method |
|---|---|---|
| **V1** | Tier gating | Search for tier names and "requires"; rewrite or date. Highest wrongness risk on the site |
| **V2** | Service limits | Search for numbers followed by "items", "days", "requests", "GB"; date the ones that are designed around, rewrite the rest |
| **V3** | Prices | `career`, `hw`, `cloud`. Almost all should be rewritten rather than dated |
| **V4** | Default retention | Cross-check `m365`, `cloud` and `blueteam` against each other first — §9's contradiction pass applies here |
| **V5** | Re-audit console paths | `check_volatility.py` already reports this, and the count is the *Dated claims* row. It grows with each `m365` or `cloud` wave — it has, from 2 to 3 |

**And the counter-discipline:** every wave should *reduce* the number of dated claims where
it can, by rewriting. A rising volatile-span count is not automatically progress — it can
mean the site is accumulating promises to re-check things that never needed a number.

## 7. Audit pass — V1, V3 and V5 read after Phase 7 closed

A pass over the three most concrete waves, done the way §4 prescribes — per class, by hand —
and the finding is the same one this phase opened with: **the site is already disciplined, and
the mechanical search over-matches exactly as predicted.**

| Wave | What the grep returned | What was actually actionable |
|---|---|---|
| **V1 — tier gating** | `E5`/`E3`/`P1`/`P2` across `m365`, `endpoint`, `eng`, `ops`, `productivity` | **~none.** `ops`/`productivity` `P1`/`P2` are incident priorities; `eng` `(E3)` is a footnote marker; `m365`'s `E3`/`E5` are the *subject* of the licensing card, not a gating claim. The one real claim — `m365`'s litigation-hold tier note — is already written in the §5 style: *"holds generally require the enterprise tier … find out which you have before promising counsel a capability."* |
| **V3 — prices** | `career` home-lab budgets, salary figures | The budget **tiers** (`$0` / `$0–50` / `$100–500`) are pedagogical anchors that do not age; the only genuinely volatile detail is the used-mini-PC range, already hedged with `~`. Rewriting the tier labels would damage the table it organises. Left as-is. |
| **V5 — console paths** | `check_volatility.py`'s 2 candidates (`Teams Voice`, `Reporting & Usage Analytics`) | **False positives.** The flagged mentions are generic prose — *"wired in through the admin center"*, *"data the admin center has never heard of"* — not console-path claims. The real console names in those cards (`Teams admin center`, `Entra admin center`) already carry `volatile` spans. |

Two things this pass also settled. **This session's 46 new cards are freshness-clean by
construction** — they were written mechanism-first, per the card rubric, and introduce no
undated price, limit or version claim, and `check_volatility.py`'s console candidates are all
pre-existing `m365` cards. A third has joined the two named above since this pass —
*Exchange Server On-Prem*, on the phrase **every Exchange admin meets**, where `admin` is a
job title rather than a console. It is read and recorded in `context()`'s docstring, which
is the right home for it: the regex cannot separate the two senses without evidence it does
not have, so the report prints the sentence and a person decides in a second. And the phase stays
**open as a standing discipline, not a queue** — §6's V5 grows with every `m365`/`cloud` wave,
so there is nothing to mark closed. The right output of a Phase 11 pass is this table, not a
pile of edits — which is the whole argument of §3.

## 8. Audit pass — V2 and V4, the two waves §7 did not read

§7 is titled *V1, V3 and V5* and nothing since said why the other two were
skipped. They were the queue's only genuinely outstanding items, so they were
read the way §4 prescribes: per class, by hand, with the instances enumerated
rather than pattern-matched.

**V4 — default retention.** Eighteen duration claims sit in a retention context
across the whole site. Five are vendor defaults and **all five already carry a
date**: the SharePoint recycle bin, Microsoft 365 Group soft delete, the Teams
expiry window, the audit-log horizon, and Azure Monitor's platform metrics. The
other thirteen are not claims about the world at all:

| What they are | Examples |
|---|---|
| Command and config examples | `--vacuum-time=7d`, `MaxRetentionSec=1month`, `find -mtime +30`, an SQL `INTERVAL '90 days'` |
| A sample policy inside a sample document | `grc`'s *delete after 3 years per schedule DR-014* |
| Advice about what **you** should set | `cloud`'s *14 or 30 days for application logs* |
| A rhetorical quote being challenged | `cloud`'s *"We keep 90 days"*, immediately answered with *Analytics vs Basic vs Archive behave differently* |
| A rule of thumb about money | `career`'s *3–6 months of expenses* |

The §9 cross-check V4 asks for also came back clean: `m365`, `cloud` and
`blueteam` do not contradict each other, and the two 93-day figures are
different subjects that happen to share a number.

**V2 — service limits.** Twelve limit-shaped claims outside code blocks, and
**two were real and undated**:

| Claim | Why it is a limit and not a fact |
|---|---|
| MongoDB's **16 MB** document ceiling | The card designs around it — *model as a separate collection* — which is §5's exact test for when a span is right |
| Entra Connect's **500-object** deletion threshold | A vendor default that is configurable, in a sentence whose durable half was already written: *know the threshold exists before you meet it* |

Both now carry a `volatile` span. The other ten are back-of-envelope anchors
(`eng` says so in the card title), a worked capacity example in quotes, a dry-run
output, a contract size band, and **SATA III's ~600 MB/s ceiling — which is a
standard, and therefore the Wi-Fi-rates case from §2 in different clothing.** A
number fixed by a published specification does not age however product-shaped it
looks.

### What the two passes together say

Five waves have now been read and the score is **four real edits across the
whole queue** — three in §7's reckoning and two here. Phase 11 opened by failing
to count the denominator and concluding the site was probably more disciplined
than a mechanical check could show. Two hand passes over five classes are the
evidence for that, and they cost an afternoon each rather than a permanent check
nobody trusts.

**The ratio is the finding.** Thirty claims examined, two actionable: the
mechanical searches over-match by roughly fifteen to one, exactly as §2 predicted
and for the same reason — the shape of a number says nothing about whether the
world can move underneath it. What separates them is always the sentence around
it, and reading that is a minute's work per instance and not automatable at all.

So V2 and V4 join V1, V3 and V5 as **read, not closed.** §6's waves are a
standing discipline: V5 grows with every `m365` or `cloud` wave, and V2 grows
with every card that designs around a vendor number.


---

# The risk register, revisited — four risks that only a measurement could find

The register in the Execution Handbook was written from imagination: *what could go wrong
with a project like this?* It was a good list and four of its entries are now mitigated. But
every risk on it is one somebody could think of without looking at the repository.

Phases 8–11 looked. These four were invisible until something was counted, and none of them
appears on the original list.

| Risk | Evidence when it was written | Where the number lives now | Reopens when | State |
|---|---|---|---|---|
| **Silent style drift** — the house form improves and earlier content is never revisited, so the site becomes two sites wearing one theme | 330 topics (23%) single-concept and under 1,800 chars, concentrated in domains written early. `data` was 93% thin | the **Thin** row of the measured state | `depth_report.py` puts thin above **2%**, or any one domain above 10% | ✅ **closed** |
| **Blind duplication** — the audit method governs new cards and has never looked backwards, so two sessions months apart both cover a subject and both cards ship | 36 title pairs at ≥50% token overlap. Two `script` cards on regular expressions, three Kubernetes cards across two domains | the **Near-duplicate pairs** row | `near_duplicates.py --unexplained` returns anything at all | ✅ **closed** |
| **Unreachable quality** — good cards exist and nothing links to them, so the reader who would benefit never arrives | 902 topics with no related-topic link, **159 of them with 3+ cards and 3,000+ chars** | the **Orphans** row | `orphan_report.py` reports a single **deep** orphan | ✅ **closed** |
| **Unfalsifiable freshness** — the site can state what it has dated and cannot state what it has not | Three attempts to count the denominator failed on IP addresses, Wi-Fi standards and shell variables | the **Dated claims** row carries the numerator; the denominator lives nowhere, and *that* is the risk — this row used to repeat the total inline, breaking the rule stated below it | never; there is no condition to watch, which is the finding | **Accepted, not mitigable.** Phase 11 §3 |

**Three of these were closed by a session that did not close them here.** The record
*"closing 'unreachable quality', the third open accumulation risk"* re-measured all four and
found the first three had fallen to 1%, 0 disagreements and 0 deep dead ends. It wrote that
down as a session record and left this table saying **Open**, so the register a session reads
to decide what to work on went on advertising three solved problems for weeks. Exactly the
defect the measured-state table above had, in the tool for deciding what to do about it.

**No number is repeated here.** Each row points at the row of the measured-state table that
carries its figure, because that table is checked by `check_plan_numbers.py` and a second
copy would only be a second thing to go stale — which is how this table got wrong in the
first place.

## What these four have in common

All four are **accumulation** risks rather than event risks. Nothing goes wrong on a
particular day; a small cost is paid per session and never collected. The original register
is full of event risks — a domain lapsing, data being cleared, a build breaking — and those
are the ones a person imagines, because they have a moment attached.

That suggests a habit rather than a mitigation: **once a phase, measure something nobody has
measured.** All four of these came from a single afternoon of counting things the repository
already contained, and every one of them was cheaper to find than it would have been to
predict.

### And a second habit, which the fifth risk demonstrated by accident

An accumulation risk has no moment attached, so it never becomes today's problem. The habit
above finds them. It does not say when to act on one, and "act when it gets bad" fails
precisely because *bad* has no threshold — the plan sat at 22,745 lines, nearly double the
length that made it acute, and no session ever decided that was the day.

The fifth risk was the only one that carried a **trigger**: *option 1 when the live queue
next empties.* That is a condition a session can evaluate by running the censuses it runs
anyway, and the session that found it true is the session that acted. It is the only risk in
this register that the file closed by its own instruction rather than by a person noticing.

So each row above now carries a **reopens when** column: not a target, a *condition*, phrased
so that a tool already in `make check` or `make census` decides it. A closed risk with no
reopen condition is a risk that will come back unannounced, which is how three of these came
to be advertised as open long after they were fixed — and how the fourth, which genuinely
cannot be measured, is honestly marked as having no condition at all.

## The fifth, which is about this file

| Risk | Reopens when | State |
|---|---|---|
| **The plan outgrows its own readability** — 11,600 lines, and the useful part is the last few hundred | `check_plan_numbers.py` reports the live file past **8,000 lines** | ✅ **Closed, reopened, and closed again.** Option 3 shipped, then option 1 at 22,745 lines by somebody noticing. The condition then fired on its own at **8,020**, and option 1 ran again — 45 records moved, 8,020 → 4,227, lines conserved. **The reopen condition is the only part of this register that has ever been tested, and it worked** |

§6 of the backlog reality check said this in a milder form: *most of those 935 will never be
built, and the useful part of this file is the last two hundred lines*. That was true at
5,000 lines. At 11,600 it is more true, and this session added 1,300 of them.

Three honest options, and the file has already picked one before:

1. **Split it** — `plan.md` for the live queue, `plan-archive.md` for the phases that closed.
   Cheap, and it makes the live file scannable again.
2. **Prune it** — delete closed tracks outright, since Git holds them. The file's own advice
   in §6: *if it ever becomes discouraging, delete a track wholesale rather than carrying it
   as debt.*
3. **Leave it and index it** — a table of contents at the top with a one-line state per phase,
   so the reader can jump.

**Option 3 first, then option 1 when the live queue next empties.** Deleting is the option
that loses the record of *why* things were decided, and this file's most-quoted sections are
the ones explaining why something was rejected — which nobody would have written twice.

### Both were done, and the trigger is what made it decidable

Option 3 — the index — went in when this was written. Option 1 waited on a condition rather
than on somebody's judgement about when the file *felt* long, and that is the part worth
copying. The condition was **the live queue empties**, and it was checkable: every census
run and none of them reporting anything a person should read. The session that found that
true is the session that split the file, at 22,745 lines, nearly double the 11,600 that
made this risk acute.

**The split conserved lines rather than summarising them.** Every line of the original is in
exactly one of the two files, asserted by counting before either was written — because the
one thing that would make this a bad trade is losing a paragraph of reasoning to a tidy-up.

The one thing that was *not* moved is the superseded *"What's in this file"* table, which
still describes Phases 4–6 as planned and quotes ~828 remaining cards. It went to the
archive uncorrected. A plan that records what it expected beside what happened is worth more
than one that records only the outcome, and that table is the primary evidence for this
archive's most repeated lesson: **the backlog count was badly inflated.**

### And then it was marked Closed with no reopen condition

Which is the defect the section directly above diagnoses, in the one row that had earned the
right not to have it. The four accumulation risks each got a *reopens when* column and an
argument for why a closed risk without one **comes back unannounced**. The fifth — the only
risk here that the file closed by following its own instruction — was written up as a
success story and left with a State column and nothing else.

It went unnoticed because the evidence for it is the file you are reading, and a file does
not look long from inside a session that is adding to it. **This one added 1,353 lines, a
31% increase, without anybody thinking about length once.** That is precisely the accumulation
shape: a small cost per session, never collected, no day on which it becomes today's problem.

So the row has a condition now, and `check_plan_numbers.py` prints the line count on every
`make check` and warns past the threshold. It reports rather than fails, because a long plan
is not a broken build and gating it would mean a session that wrote a good record could not
commit it.

**8,000 is measured rather than chosen**: double the ~4,000 the split left, and a third of
the 22,745 that made it acute. Far enough away not to nag, close enough that the file is
still comfortably splittable on the day it fires.

The general form, which is the fourth instance this session of the same thing: **a rule
written for a category tends not to be applied to the case that motivated it.**
`check_renames` matched case-sensitively because its own example was lower case;
`check_css_vars` read only the stylesheet because its own example was in the stylesheet;
`script.js` was the one file missing a convention three others had; and the register's
reopen-condition rule was applied to every risk except the one that proved it was needed.


# Domain shape — the connectivity measurement, and what it says

Phases 7–10 treat the site as a set of cards. This treats it as a **graph**, which is what a
reader actually moves through. Two numbers per domain: cross-domain cross-references out and
in, and steps in a learning path.

```
domain        xref-out xref-in  self  path        domain        xref-out xref-in  self  path
sec                 15      27    19     3        cs                 15       1     6     0
ops                  9      20    12     8        m365               21       1    10     1
script               4      14     3     1        web                 4       0     8     0
grc                  1      10     9     0        hw                  9       0     4     2
blueteam             2       9     7     3        philosophy          3       0     0     0
devops               0       8     0     2        math                0       0     0     0
career               4       8    12     7        quotes              0       0     0     0
net                  3       5    10    25        shortcut            0       0     0     1
```

## 1. Three shapes, and what each means

| Shape | Domains | Reading |
|---|---|---|
| **Hub** — high in, moderate out | `sec` 27 in · `ops` 20 in · `script` 14 in | The site's centers of gravity. Other domains reach for them, which is correct: they are the shared vocabulary |
| **Broadcaster** — high out, near-zero in | `m365` 21 out / 1 in · `cs` 15 out / 1 in · `hw` 9 out / 0 in | These reference the rest of the site and nothing references them back. Not wrong, but it means a reader arriving anywhere else never learns they exist |
| **Island** — near-zero both ways | `math`, `quotes`, `philosophy`, `productivity`, `web` (0 in) | Reachable only by clicking the chip. `web` at **8 self-references and 0 inbound** is the surprising one: a large technical domain nothing else points at |

## 2. The finding worth acting on

`cs` sends fifteen cross-references outward and receives **one**. It is the domain that
explains *why* things work — hash collisions, percentiles, consensus, memory hierarchy — and
almost nothing in the operational domains says "the reason is in `cs`".

That is a one-line fix per card and it is the highest-value linking work available:
**an inbound reference from an operational card to the theory card underneath it** teaches
something the operational card cannot. Phase 7's W1 (Little's Law) was chosen partly for
this reason — `ops`, `data` and `cs` all need it and none of them currently connects.

**Acted on this session (See-also layer).** Rather than edit prose in fifty cards, the inbound
edge was added to `related.json`, bidirectionally, in two batches covering **fourteen `cs`
theory cards** and the operational cards that rest on them:

- queue / capacity / backpressure → *Little's Law & Queueing*
- latency / observability / load-testing → *Percentiles & Latency*
- sharding / blast-radius / load-balancers → *Consistent Hashing*
- detection quality → *Bayes' Theorem & Base Rates*; C / Rust → *Undefined Behaviour & Memory Safety*
- rounding gotchas → *Number Representation*; failover quorum → *Consensus*; saga & streaming ordering → *Time in Distributed Systems*; Redis → *Caches & the Memory Hierarchy*
- embeddings/RAG → *Vectors & Embeddings*; ML fundamentals → *Derivatives & Gradient Descent*; ER modelling → *Sets & Relations*; data-structure choice & back-of-envelope → *Big-O in Practice*; hash-table choice → *Hash Tables & the DoS*

`cs` went from **one inbound reference to a See-also connection on fourteen of its centers of
gravity**, and because the edges are bidirectional, each operational card now surfaces the
theory beneath it. Hand-curated, not term-overlap (§3), so the strip carries them without
filling with noise. (The batch-2 pass also re-caught the acro-span title-truncation trap: three
targets whose titles carry a *mid-title* acronym slugged short until resolved through build's
own `topic_label` — the same trap the SOC-metrics duplicate sprang, and the reason ids must
come from the stamper, never a naive `topic-name` match.)

The mirror finding: `m365` at 21 out and 1 in is the most self-sufficient domain on the site,
and the least discoverable from anywhere else.

### The two mirror findings, worked

The graph's §1 named two under-connected shapes to fix, and both took a wave this session, by
the same bidirectional See-also method as `cs`:

- **`web`, the island (0 inbound).** A large technical domain nothing pointed at. Thirteen
  high-confidence pairs now link its security, auth, storage, edge, performance and testing
  cards inbound from the operational and security domains that rest on them — Frontend Security
  from the injection/WAF/pentest cards, Frontend Auth from OAuth and sessions, Web Storage from
  the cookie-consent card, edge rendering from caching and cloud networking, Core Web Vitals
  from load testing.
- **`m365`, the broadcaster (21 out / 1 in).** The most self-sufficient, least discoverable
  domain. Eleven pairs now point at it from the compliance and identity cards that share its
  subjects — DLP labels ↔ data classification, retention ↔ deletion, eDiscovery ↔ subject-access
  requests, PIM ↔ privileged access management, EOP/Defender ↔ BEC and email authentication,
  M365 joiner-mover-leaver ↔ offboarding, Multi-Geo ↔ the new cloud data-residency card, Power
  BI governance ↔ the data semantic-layer card, Teams call quality ↔ QoS, M365 backup ↔ the
  3-2-1-1-0 backup strategy.

A final pass took the **near-duplicate census** (the third `make census` report) and read it
the way it is meant to be read — not as a merge queue but as a list of *pairs that should at
least point at each other*. Ten cross-domain twins that were similar and unlinked are now
cross-linked, non-destructively: `pentest`/`redteam` **sqlmap**, `net`/`blueteam` **packet
analysis / Wireshark**, `threat`/`blueteam` **email authentication**, `devops`/`linux`
**container security / Docker**, `pentest`/`redteam` **vulnerability scanning**, `grc`/`ops`
**risk vs vulnerability lifecycle**, the two `data` **schema-design** cards, the two `ai`
**machine-learning** cards, `devops`/`eng` **event-driven architecture**, and `script`/`eng`
**clean code**. This is the Phase-9 duplication finding resolved the safe way: a 0.5–0.6
similarity means *distinct-but-related*, so a link beats a merge and keeps every permalink.

`related.json` finished the session at **1,216 links across 690 topics, still 0 one-way**, and
the orphan census fell from **898 to the mid-800s** — the See-also layer now carries the
writer's own cross-references, the graph's two structural gaps, and the near-duplicate twins,
without the term-overlap default ever shipping.

## 3. The See-also layer, filled from the writer's own cross-references

The graph above counts cross-references authored in prose. Those same `<span class="xref">`
edges are also the highest-quality seed for the *related-topics* strip — a writer saying
"these two belong together", already proven to resolve by the linter — and
`suggest_related.py --xrefs` exists precisely to emit them, both directions, in
`related.json`'s own format.

This session ran that mode and merged its output into `related.json` as a **union**: every
existing curated link kept, **+122 writer-authored links added (976 → 1,098), all
bidirectional (`--check`: 0 one-way), nothing removed.** The orphan census moved **898 → 866**
topics with no inbound link and **151 → 148** deep dead-ends. The point of the wave was the 46
new Phase 7 cards, which arrived carrying outbound xrefs and no inbound links: they are now
reachable from every card they reference. The term-overlap *default* stays unshipped, exactly
as the tool's docstring insists — only the deliberate edges were promoted, so the strip does
not fill with the same four cards on every page.

Two further passes after the named-broadcaster work: the **near-duplicate twins** the
`near_duplicates` census flags (0.5–0.6 pairs — distinct-but-related, not merge candidates)
were read as a link list and cross-linked both ways, and a **deep-orphan** pass connected the
highest-confidence dead-ends the `orphan_report` still named — container internals ↔ container
hardening, the two malware-analysis cards, privilege escalation ↔ its scanners, load balancers
↔ sharding, AD 101 ↔ AD structure, MCP ↔ function calling. `related.json` reached **1,238
links** (from 976 at the session's start), all bidirectional. The remaining deep orphans are
scattered singles with no obvious high-confidence home; forcing links there would be the
term-overlap noise the tool refuses, so the pass stops where confidence does.

## 3. Learning paths are one domain's story

**`net` held 25 of the 75 path steps.** `cs`, `eng`, `grc`, `web`, `ai`, `data`,
`philosophy`, `mind` and `productivity` held **none**.

Six paths existed and they were, in effect, network-and-operations paths. That was a
legitimate first cut and it became the constraint: a reader whose interest is data or study
skills had no path at all. **Acted on this session:** two of the three paths §3 named were
added — **`data-from-first-principles`** (18 steps: how a database works → the relational
model → SQL from joins to window functions → the performance layer → the NoSQL/analytics
landscape) and **`study-that-sticks`** (15 steps drawing on `productivity` and `mind`:
retrieval and spacing → memory and attention → study systems → the mindset that sustains
them). The defender path §3 also named already exists as `soc-analyst-starter`, so it was not
duplicated. Paths went **6 → 8, 75 → 108 steps**, and `data` (18) and `productivity` (13) now
have the entry point they lacked. `check_paths.py` green: 108 distinct topics, every step
resolves.

A second paths pass extended the same §3 logic to the other large zero-path domains:
**`frontend-from-the-browser-up`** (19 steps: render pipeline and DOM → grid/flexbox layout →
the JavaScript that trips people up → a component framework → data, auth, security,
performance, accessibility, testing and deploy) and **`cs-for-working-engineers`** (18 steps:
complexity → the data structures and algorithms worth knowing cold → scheduling, concurrency
and memory → the distributed-systems and latency facts that decide real designs), then a third
adding **`llms-from-prompt-to-production`** (15 steps: what a model is → tokens and prompting →
RAG → tools and structured output → the production concerns) and **`grc-end-to-end`** (15
steps: risk from first principles → frameworks and the controls universe → classification and
audit → the major regimes → the governance machinery). Paths went **6 → 12, 75 → 175 steps**;
`web`, `data`, `cs`, `ai`, `grc` and the `productivity`/`mind` learning-science pair all gained
the entry point they lacked. The remaining zero-path domains are either small enough that the
chip is entry enough or are the islands §4 says want prose, not a forced sequence — so the
paths programme, like the connectivity one, stops where a genuine reader-sequence does.

## 4. What this does not mean

Connectivity is not quality. `philosophy`, `mind` and `productivity` are among the
best-written domains and are the least connected, because their subjects genuinely sit apart
from the technical graph. The action for them is a **path**, not forced cross-references —
manufacturing a link from a Kubernetes card to Stoicism would be worse than the island.

## 5. New content after the structural sweep — one card from a two-round probe

With connectivity and paths at their floor, a fresh new-content audit ran the Phase-7 method:
probe durable subjects across all 30 domains, then **verify every apparent gap against the
real content** rather than the title. Two rounds, ~130 probe terms. The verification did what
the file always predicts it will — it killed most candidates as phrasing misses or
already-covered:

| Apparent gap | Verdict on reading the content |
|---|---|
| DDoS / SYN flood / amplification | Covered — the `threat` DoS card already tables SYN flood, Smurf, Slowloris and DNS/NTP amplification with defences |
| The air gap | Covered — `sec`'s OT card already makes the erosion argument (*"USB is how air-gapped plants still get hit"*, data diodes), and the backup cards carry the offline/air-gapped copy |
| break-glass, saga, canary, confidential computing | All present under a different phrasing than the probe used |
| dead-letter queue, SPIFFE, TOCTOU, RED method | Real but narrow — sub-points of existing cards, not their own |

**One genuine, foundational gap survived: `cs` had hashing and consistent hashing but no
Merkle tree** — the structure under git, blockchains, Certificate Transparency, backup
dedup and anti-entropy. Written to the rubric (*prove two copies of a terabyte match by
comparing 32 bytes; when they differ, find where in log n*), and linked to consistent hashing,
hash tables and git. Site **1,512 → 1,513**. The audit's real output is the table above: the
site is saturated at the level a broad probe reaches, and the honest yield of a careful pass
is a card or two, not a wave — which is exactly the closing note below.

A second-round probe on advanced distributed-systems topics found the neighbouring gap:
`cs` had ordering (clocks, causality) and consensus (Raft/Paxos) but not **CRDTs** — the
conflict-free replicated data types that let offline replicas merge without coordination
(collaborative editors, offline-first apps). It is genuinely distinct from both neighbours —
convergence, not ordering; eventual consistency, not consensus — and the card is built around
that boundary (a CRDT cannot enforce a global invariant like &ldquo;no double-booking&rdquo;;
for that you still need coordination). Site **1,513 → 1,514**.

A third round refined the finding. Probing *advanced* topics — not fundamentals — turned up two
more genuine gaps, this time outside `cs`: `net` taught the TCP handshake but not **congestion
control** (why a fast link can still be slow — the congestion window, the sawtooth, bufferbloat,
the bandwidth-delay product), and `data` taught **B-tree** indexes but not the **LSM tree** that
is their write-optimised opposite (append-only storage, read/write/space amplification, the
engine under Cassandra and RocksDB). Both are foundational, both were absent, both link cleanly
into the existing graph (TCP congestion to Little's Law and percentiles; LSM to B-tree indexes
and wide-column stores). Site **1,514 → 1,516**.

So the sharpened conclusion: the site is saturated at the level of *fundamentals* — a broad
probe of common subjects finds only phrasing misses — but the *depth* frontier of a mature
technical domain still holds real gaps, and they surface only when the probe targets the
advanced layer and every hit is verified against the content. A fourth round added **Amdahl's
Law** — `cs` had Little's Law for latency but not the parallelism ceiling (why more cores stop
helping; the serial fraction sets the limit; Gustafson as the counterpoint). A fifth round added **Byzantine Fault Tolerance** — `cs` had crash-fault consensus (Raft/Paxos)
but not the Byzantine fault model (agreement when nodes lie; the Byzantine generals problem and
its one-third bound; 3f+1 vs 2f+1; why blockchains need it and a trusted data center does not),
linked to Consensus and FLP. **Six cards from five careful rounds** (Merkle, CRDT, TCP
congestion, LSM, Amdahl, BFT), each a foundational structure a neighbour merely gestured at —
and five of the six clustered in `cs` and its neighbours, because the theory domain is where a
mature site's remaining depth-gaps concentrate. That is the durable shape of new content on a
site this size: not waves, but a handful of real gaps per deliberate audit, thinning as the vein
is worked — which is exactly the loop the scheduled Routine runs. Site **1,512 → 1,518** over the six.

A seventh round probed the *less-mined* domains — engineering, architecture, ops, security — and
**came back empty**, which is the finding that stops the pass. Every strong candidate verified as
already covered: SOLID has its own `eng` card (Dependency Inversion included), dependency injection
is `script`'s *Inject Dependencies* card, and strangler-fig, hexagonal, bounded-context,
domain-driven, graceful-degradation, golden-signals and secure-by-default are all present. What
was left absent — anti-corruption layer, dark launch, YAGNI, game day, key rotation — are narrow
sub-topics of existing cards, not standalone gaps. So the honest stop: **the foundational level is
saturated across every domain, and the depth-gaps that remain concentrate in the theory domain and
are now largely worked.** Six genuine cards, then a round that finds none, is the signal to hand
the increasingly-niche long tail to the scheduled Routine's periodic fresh-context audits rather
than manufacture borderline cards — the counter-discipline this file has stated since Phase 8:
*a rising count is not automatically progress.*

**An eighth round, run later with fresh context — the same loop the scheduled Routine runs —**
probed the distributed-systems depth frontier once more and returned a single survivor. `cs`
taught consensus (Raft/Paxos), logical clocks, CRDTs, Merkle trees / anti-entropy and FLP
failure detection, but never the **gossip / epidemic dissemination** primitive all five lean on:
the propagation-and-membership mechanism under Cassandra, Consul, Serf and DynamoDB, where each
node tells a few random peers and a fact reaches the whole cluster in O(log n) rounds — no
coordinator, no critical path, eventual and probabilistic with no completion signal. A content
grep confirmed the gap was real, not phrasing: **zero hits for `gossip` anywhere on the site**,
while the round's other candidates verified as already covered — rate limiting is `sec`'s *API
Abuse & Rate Limiting* (token and leaky bucket both), distributed transactions are `eng`'s *Saga
& Outbox* (2PC named), and Lamport/vector clocks live inside the `cs` *Time in Distributed
Systems* card. The one card was written to the rubric — the inversion (spread like a rumour, not
a broadcast), the fingerprint (O(log n), unkillable, but no receipt), the scope line (gossip
disseminates and detects; it does not agree or order) — and linked bidirectionally to its five
neighbours (consensus, FLP, Merkle, CRDTs, consistent hashing). This does **not** reopen the
pass. One genuine card from a careful, fully-verified round, on the exact vein the previous six
worked, *is* the predicted yield — the durable shape is a handful per audit, thinning — not a new
wave. Site **1,518 → 1,519**. Check PASS · smoke **142/142** · axe **6/6** · visual **2/2** ·
related **1,266 links, 0 one-way**.

And then the confirming sweep, so the next audit does not re-probe this slice. Immediately after
gossip, two more verification passes were run and **both stopped clean**. The database-concurrency
frontier is covered — `data`'s isolation card already carries MVCC, read-committed / repeatable-read,
and dirty / phantom reads — and the classic-structures frontier yields only the niche tail: skip
lists, two-phase locking, snapshot isolation, write skew, bitmap indexes and the Chandy-Lamport
snapshot are each either a sub-point of an existing card or genuinely advanced, none the
five-cards-leaned-on-it gap gossip was. A final broad cross-domain sweep of ~21 durable
&ldquo;a reference must have this&rdquo; subjects — QUIC, BGP, NAT, ARP, MTU, CDC, columnar/OLAP,
STRIDE, zero-trust, eBPF, cgroups, namespaces, CDN, idempotency — returned **coverage on every one**;
the sole 0-hit was `io_uring`, advanced Linux async I/O, which is niche tail by any honest reading.
So gossip stands as the last *foundational* gap the site had, and the frontier is now worked out at
that level. The remaining niche tail is the scheduled Routine's job, on its periodic fresh-context
cadence — not this session's to manufacture.

---

## Session — three cards the probe named, and none of them was a synonym

The previous record left twelve named misses and called them "mostly kind 1:
the card says it in the other word, which is a prose wave". That framing was
half wrong, and reading the three best ones is what showed it.

**Kind 1 says name both words. Two of these three had no word to name** — they
had a hole where the reader's question goes, and the probe found the hole by
looking for the word.

| Miss | What the card already had | What was missing |
|---|---|---|
| `merge conflict` | `bisect`, `rebase -i`, `reflog`, `stash`, `cherry-pick`, `worktree`, `blame`, four kinds of undo | **Conflicts.** A card that teaches rebase and cherry-pick and never says what happens when they stop |
| `cron not running` | PATH, redirect output, `chmod +x`, crontab.guru | The symptom. Four bullets of causes with no statement of what the reader is looking at |
| `printer offline` | Technologies, deployment models, secure release, a six-step triage | The single commonest printer ticket there is |

### The inversions each one turned out to have

None of these were reachable by adding a word, and each has the shape the
rubric asks for — the sentence that is true and contrary to instinct:

* **A merge conflict is git declining to guess, and "ours" and "theirs" swap
  meaning between a merge and a rebase.** A merge replays their commits into
  your branch, so *ours* is yours. A rebase replays *your* commits onto their
  branch, so while it runs *ours* is everyone else's work and *theirs* is your
  own commit. Resolving a rebase by the reflex learned from merges deletes your
  own change and leaves a clean-looking history that silently dropped it. Git
  checks the markers are gone, not that the result makes sense.
* **A cron job that "did not run" almost always ran.** The fingerprint is *it
  works when you type it and not when cron types it*, which is one sentence
  about the environment — and `env -i /bin/sh -c '/path/to/job'` reproduces it
  in one line and is right far more often than the expression is wrong. The
  `%` that cron reads as a newline and the dot that makes `run-parts` skip a
  file are in the table now; both were missing and both are silent.
* **"The printer is offline" is a claim by the client, not a report from the
  device.** A device printing its configuration page for somebody standing
  beside it can show offline on every desk in the building, because the queue
  is reporting that *this computer* did not get an answer it expected. Which
  makes power-cycling the printer a reboot of the one component that was never
  at fault.

### Why this is not keyword stuffing, and how to tell next time

The probe's own rule is that seeding symptom phrases into cards is *"keyword
stuffing with a rationalisation attached"*, and it is right. The test that
separates the two is not whether the word appears afterwards — it is
**whether the card was incomplete without the thing the word names**:

> A card that teaches `git rebase -i` and never mentions conflicts is missing
> content. A card that lists cron's PATH gotcha without naming the symptom is
> missing a sentence. Adding "merge conflict" to a card that genuinely has no
> conflict material would have been the stuffing.

Three of nine remaining misses are still the synonym shape — *joiner* against
*new starter*, *spacing* against *spaced repetition* — and they are a smaller,
different edit. Two more, `kill a process` and `writing a detection`, are the
matcher limit recorded last session and not a content problem at all.

```
probe 63 of 78 answered · 9 unexplained, named · 3 concept cards added
depth mean 1,382 -> 1,383 · excluding verdicts 1,117, unmoved
39 gates green · check · smoke 163 · search 51 · a11y 31 · resilience 64
mobile 15 · visual 2 · backup 3
```

---

## Session — two symptoms infra described without naming, and a stale verdict

Four more of the probe's misses, and the most useful thing this wave produced
was not a card. It was catching a `keep` note that had gone false.

### The two infra cards

Both had the mechanism and neither had the ticket.

**Processing Order & Precedence** explains LSDOU, Enforced, Block Inheritance,
the computer/user split and loopback — and never says what the reader types.
The missing card is the one the rest of the topic implies: *"it is not applying"
usually means something else won*, because **precedence working correctly looks
exactly like a policy that did not arrive**. Five reports, five causes, and only
one of them is a fault. The verdict is `gpresult /h` run as the affected user on
the affected machine, with its limit stated in the same breath — it reports what
*did* happen and has nothing to say about what *should* have, so it settles "did
something else win" and never "is this policy right".

**File Services** had share-versus-NTFS, DFS and quotas, and nothing about the
drive letter. *A mapped drive is an intention, not a connection* — re-established
at every sign-in, in whatever security context the process doing the asking
holds, which is why one letter can be present, absent and unreachable on one
machine at one moment. The red cross that is cosmetic, the map that loses a race
with the network, the elevated process holding a different token, one credential
set per server name, and the address that authenticates differently from the
name. Five tickets that read as one.

### The stale verdict, which is the part worth keeping

`someone clicked the link` carried this note:

> kind 3 — the response card exists and does not use these words

It had been true. It was not true any more: the query stopped being a zero when
the matcher gained its relaxation stage, and it was returning four cards — none
of them the phishing-response card — while a note said it returned none. **A
recorded verdict decays when the thing it describes changes underneath it**, and
nothing checks a `keep` note the way `check_plan_numbers.py` checks a table row.

Reading the card settled it, and the answer was smaller than the note: it says
`clicked` three times, `someone` twice, `URL` twice and **`link` not once**. A
phishing response card that never uses the word the person reporting it will use
is not being precise, it is using the technical word where both belong. Two
words changed.

The general form, which is the thing to carry: **a verdict recorded against a
zero is only valid while the query is still a zero.** Every `keep` note in that
file asserts a state, and the ones asserting "returns nothing" are the ones a
matcher change can silently falsify. The probe reports zeros and misses
separately; it does not check that a note still describes the row it sits on.

### And two recorded rather than fixed

`kill a process` and `writing a detection` are the matcher limit from the
previous session, now written into the file instead of reappearing as
unexplained every run. Both have every word of the query in the wanted card; a
literal phrase in a worse card answers first and stops the search. Preferring a
later stage needs ranking, and this matcher is a filter.

```
probe 78 · 66 answered · 5 unexplained, named · zeros 5 -> 4
5 concept cards this wave and last · mean 1,384 / 1,118 excluding verdicts, both +2
39 gates green · check · smoke 163 · search 51 · a11y 31 · resilience 64
mobile 15 · visual 2 · backup 3
```

---

## Session — the check that already existed, one file over

The previous record ended on a general statement and did not act on it:

> A verdict recorded against a zero is only valid while the query is still a
> zero. The probe reports zeros and misses separately; it does not check that a
> note still describes the row it sits on.

It does now. And the first thing the work turned up is the part worth keeping:
**`near_duplicates.py` has had exactly this check for as long as it has had
verdicts.**

```
# A verdict whose pair no longer scores is a verdict about content that has
```

Its docstring even argues the case — *"a verdict whose pair no longer scores is
reported as stale, so the queue is worked"*. Two files in the same `tools/`
directory store a human's recorded judgement about a measurement. One checked
that the judgement still had something to be about. The other did not, and the
one that did not is where a note went false and stayed false.

**The lesson is not "add staleness checks".** It is that a convention invented
once for a good reason does not travel to the next file that needs it unless
somebody carries it, and the thing that made this visible was a *defect*, not a
review. Looking for the same shape elsewhere costs a grep: `search_test.mjs`
also holds recorded misses, and it already handles the same decay in the same
direction — *"a miss that starts working is reported too — it should be promoted
into FIXTURES"*. Two of three had it. Nobody had noticed the third.

### What is checkable, and what deliberately is not

A `keep` note is prose, and most of what it says is an argument. Two assertions
in it are not:

| Claim | Check |
|---|---|
| The note says the query **returns nothing** | It either returns nothing or it does not. "zero", "found nothing", "returns nothing", "no results" |
| The note explains why a query **misses its `want`** | It either still misses or it reaches the card, in which case the reason has been answered and the note is hiding finished work |

No threshold, nothing for a reader to overrule — the sharp shape
`check_css_vars.py` argues for. What it will not do is judge whether the prose
is *right*: a note reading "the comparison is not phrased" could be wrong about
the corpus and this cannot tell. It checks the one assertion a machine can
evaluate and leaves the argument to a person, which is the division this file
draws everywhere else.

### It reports; its logic gates

The probe is a census and stays one — gating it would make a content wave's
findings break the build, which is the whole reason it exits 0. But the
staleness decision is ordinary logic, so `--self-test` runs it against eight
fixtures in `make check` and in CI, with no browser. **Gates 39 → 40**, the
same 40 in both lists.

Proved twice, because a check that has never fired is a check nobody has tested:
the fixtures, and then the live path, by falsifying a real note on a copy of the
file and watching it name the row.

```
  "printer offline"  (a service desk engineer)
      the note says this returns nothing; it returns 1
```

The stale report prints **before** the findings and again after them, because a
note that has gone false is a defect in the file rather than a fact about the
site, and every count on the page is read through it.

```
gates 39 -> 40 · probe self-test 8 fixtures · 78 queries · 66 answered
0 stale verdicts · smoke 163 · search 51 · a11y 31 · resilience 64
mobile 15 · visual 2 · backup 3
```

---

## Session — the queue emptied, and the number it emptied to is lower than the one it started at

```
72 of 78 answered   ← counting results
57 of 78 answered   ← counting whether the right card came back
71 of 78 answered   ← after the matcher stage and eleven cards
 0 unexplained
```

The middle number is the honest one and it is the reason the last is worth
anything. A census that went **up** from 72 would have been the same lie in a
better mood.

### The last five, and what each turned out to be

| Miss | Verdict |
|---|---|
| `outlook won't connect` | **A hole.** The M365 troubleshooting playbook is five abstract layers and a symptom table written in categories — it never names one product. A playbook whose examples are "one user, one feature" cannot be found by a ticket that says *Outlook won't connect*, and cannot be used by the person holding that ticket either |
| `spaced repetition` | **A wrong `want`.** The card I pointed it at names Spacing in its *title* and covers it in one table row about teaching other people. The card that teaches the technique is in `productivity`, which then turned out not to name it in running text — it says "spaced-repetition software" in a verdict and nowhere else |
| `why does caching break things` | Synonym, with something worth adding underneath it |
| `first week as a manager` | Synonym, same |
| `onboarding a new starter` | Synonym — the card says *joiner* three times and *onboarding* never |

### The correction is the part to keep

`spaced repetition` was pointed at the wrong card by me, in the same session
that argued a `want` should only be written where one card is the defensible
answer. Two cards had the word in scope and I picked the one whose **title**
matched instead of the one whose **content** did. The probe caught it the only
way it could — by continuing to report a miss after a change that should have
closed it.

**Title-matching is how a `want` goes wrong**, and it is worth writing down
because it is the cheap, plausible move: the career card is called *How Adults
Actually Learn — Relevance, Practice, Feedback & Spacing* and is about running
training for other people. The reader typing "spaced repetition" wants to study,
not to teach. Same word, different subject, and the slug is no help at all.

### Three synonyms, and what they were covering

None of the three was worth only a word, which has now happened often enough
this session to be the rule rather than the exception:

* **Caching breaks things in one direction only.** It never makes the source
  wrong; it serves an answer that *used to be* correct — which is why a cache
  bug reproduces perfectly for one person and is invisible to everybody else,
  including whoever is trying to fix it.
* **The first week as a manager is not phase one, it is the week that decides
  whether you get one.** A new manager who spends it answering the technical
  questions has told the team precisely what they intend to be for.
* **Every M365 report arrives phrased as a client problem, because the client
  is the only layer the user can see.** Four of the five layers are invisible
  from a desk, so a tenant incident, an expired token, a disabled service plan
  and a Conditional Access policy all surface as one sentence. Which is why the
  instinct is to repair the thing the sentence names, and why that instinct is
  wrong four times out of five.

### Where the probe stands

Every one of the 78 now carries the topic it should reach or a recorded reason
why it cannot, and the seven recorded ones are: four zeros a previous session
reasoned about and kept, and three misses that are matcher limits rather than
corpus gaps. **The backlog is empty and the file says why for every row in it.**

The next session should not read this as "the probe is finished". It is finished
*against its own 78 questions*, and those were written by people who know the
site. The measurement that would move now is more queries, not more fixes — and
the honest expectation is that a fresh 78 would open at something like 57 again.

```
probe 78 · 71 answered · 0 unexplained · 11 concept cards and prose edits
across 9 domains this session · 40 gates green · smoke 163 · search 51
a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```

---

## Session — the prediction, tested: a fresh 29 questions opened at the same third

The last record made a claim and it was cheap to check:

> The probe is finished *against its own 78 questions*, and those were written by
> people who know the site. The honest expectation is that a fresh 78 would open
> at something like 57 again.

**Twenty-nine new questions opened with ten misses.** The original 78 opened
with fifteen. Both are about a third, and the agreement is the useful part: the
miss rate is a property of writing a reference, not of this particular batch or
of the people who wrote it. A site that answers its own questions is not the
same as a site that answers a reader's.

### What the ten were

Three of them were **holes**, and each hole sits directly under a heading that
promised to cover it:

* **`"The Disk Is Full"` never mentioned inodes.** Its step 1 is `df -h`, and
  inode exhaustion is precisely the case where `df -h` tells you there is no
  emergency while every write fails with the *"No space left on device"* the
  card opens on. The shape underneath is worth the card on its own: the more
  often a job fails, the faster it exhausts the thing that would let it report
  the failure.
* **The SSH card never quoted `Permission denied (publickey)`.** The most common
  SSH error there is, and the message misleads in a specific direction — it
  almost never means the key is wrong. The cause that outranks all the others is
  a group-writable **home directory**, which the card's own `chmod` block does
  not cover because it stops at `~/.ssh`.
* **Subject Access Requests at Scale never said "GDPR" or "data subject".** The
  card is about a right, and it named neither the right's holder nor the
  regulation that creates it.

Four were synonyms with something real underneath — *penetration test* against
*pentest*, *screen sharing* against *Screen Shares*, *on call* against
*on-call*, the leaver's *files* against *the OneDrive*. And three are the
matcher.

### Two `want` values that were wrong, both mine, both caught the same way

`spaced repetition` last session, and `port already in use` this one. The second
is the more instructive: I pointed it at Process Management because the phrase
has "process" in it, and the commands that answer *what is holding this port*
live in the performance-debugging card's `lsof`/`fuser` section. **The probe
caught both by continuing to report a miss after a change that should have
closed it** — which is the only way a wrong target can announce itself, and an
argument for fixing the card *and* re-running rather than fixing and assuming.

### The stage-stop class now has four members

`kill a process`, `writing a detection`, `incident postmortem`, `penetration
test report`. In every one of them **the wanted card contains every word of the
query**, and a single other card containing the words *adjacent* answers first
and stops the search:

```
penetration test report   1 match in 1 domain
incident postmortem       1 match in 1 domain · matched ignoring hyphens
kill a process            1 match in 1 domain
writing a detection       1 match in 1 domain
```

All four return **exactly one result**, and that is a signal rather than a
coincidence. Recorded here rather than acted on, because the fix is a change to
the stage order and that deserves its own measurement.

```
probe 105 questions · 95 answered · 3 unexplained, named · 8 concept cards
and prose edits across 7 domains · 40 gates green · smoke 163 · search 51
a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```

---

## Session — a single result is a coincidence, except when it is the answer

The previous record left four misses with one fingerprint and declined to act:

```
penetration test report   1 match in 1 domain
incident postmortem       1 match in 1 domain · matched ignoring hyphens
kill a process            1 match in 1 domain
writing a detection       1 match in 1 domain
```

In all four the card the reader wanted contains **every word of the query**, and
a single unrelated card containing those words *adjacent* answers first and
stops the search. Being adjacent is the whole of its claim.

So a single result escalates now. It is safe in the strict direction because
each stage is a superset of the one before: a card containing the query as a
phrase necessarily contains the query's words, so widening cannot lose the hit
it started from.

### The guard, and the three discriminators that did not work

The first version broke two gated fixtures, both of which had exactly one result
and the *right* one. `why is my laptop slow` returned the card called **"Why Is
My Laptop Slow?"** and widening it to sixteen serves nobody.

Three candidate rules were measured before one worked:

| Rule | Why not |
|---|---|
| Result count after widening | The four good cases land at 12, 16, 22 and 30; the two bad ones at 10 and 16. No cap separates them |
| Word rarity | `penetration` is in 1.0% of topics, `revoke` in 2.6%. The word that should have been protected is the *commoner* one |
| **The lone hit's own slug carries a word of the query** | **This works**, and it is not a coincidence that it does — a slug is built from a title, and a title is a claim about the subject rather than a mention of it |

That leaves one fixture genuinely worse: `revoke before reset` goes from one
perfect hit to ten containing it, because the phrase is the card's *thesis* and
not its title, and no rule reaches that. **Its ceiling moved 8 → 20 and the
fixture table says in full that this is a cost paid rather than a stale number
corrected** — the one exception to a rule that file states plainly, written down
beside the number so nobody later reads 20 as generosity.

### The staleness check earned its keep two waves after it was written

It fired for the first time on this change, unprompted, naming three rows:

```
"writing a detection"   the note explains a miss that no longer misses
"kill a process"        the note explains a miss that no longer misses
"standups"              the note explains a miss that no longer misses
```

`standups` is the one worth pausing on. Its note is **the reason the probe grew
a `want` field at all**, it had survived several sessions, and it ended with a
refusal: *writing 'standups' into the prose to close it is the keyword stuffing
this file forbids.* The escalation closed it without a word of prose being bent,
which is exactly what that note was holding out for — and without the check,
three verdicts describing a world that no longer exists would have sat there
until somebody happened to re-read them.

### And one word

`explain oauth` returned **nothing** against a domain full of OAuth cards. The
conjunction required a word the OAuth card has no reason to contain, and the
query is two words long, so the relaxation stage's floor of two could not drop
it. `explain` is an instruction to the site, never a subject, and it joins
`how what why when where`. Only that one: **`show` is a Cisco command here**,
and `define` and `describe` are ordinary content verbs in a reference.
`explained` and `explains` are separate tokens and stay, which is what keeps
*Load Balancers Explained* reachable by its own title.

```
probe 105 questions · 101 answered · 0 unexplained · 0 wrong-card · 0 stale
4 zeros, all recorded · search 51/51 with one ceiling moved and the reason
written beside it · 40 gates green · smoke 163 · a11y 31 · resilience 64
mobile 15 · visual 2 · backup 3
```

---

## Session — the guard this file credits with catching "whitelist" was not catching it

Found by reading, not by a tool, and while doing something else entirely. The
SSH card was open for a different reason and one of its rows said:

```
AllowUsers   alice bob   Whitelist who can SSH in
```

`data/renames.json` has listed **whitelist → allowlist since 2020-06**.
`check_renames.py` runs in `make check` and in CI. The build had been green
throughout. And the session operating manual at the top of this file names that
exact rename as failure #3, with the guard column reading *"`check_renames.py`,
already in `make check`. First time it caught same-session writing."*

It caught that one. It could not have caught these:

```
whitelist   Whitelist who can SSH in                       linux
whitelist   Whitelists exactly where scripts may load from sec
whitelist   Whitelist which executables are allowed to run sec
whitelist   Application whitelisting, EDR                  threat
whitelist   a whitelisted domain added to fix one          m365
blacklist   Check your IP against blacklists regularly     linux
```

### Two characters of regex, and both of them hid the same class

```python
re.finditer(r"\b" + re.escape(old) + r"\b", text)
```

**No `re.I`.** A rename is a rename whatever the capitalisation, and a
sentence-initial capital is the single likeliest place for one to hide, because
that is exactly where prose puts the word it is about. Four of the six were
capitalised.

**A trailing `\b`.** `\bwhitelist\b` does not match *whitelisting*, and the word
most often appears as a gerund. Five of the six were inflected; four were both.

Inflection is opt-in per entry — `"inflect": true` — because a product name does
not pluralise into a different product, and `(?:s|d|ed|ing)?` hung on "Azure AD"
is noise looking for somewhere to happen. Case-insensitivity is not opt-in,
because there is no entry for which it is wrong.

### What this is actually an instance of

The register's fifth risk is *this file believing its own record*. This is the
tooling version of it: **a guard's entry in a table says what it is for, not
what it does**, and the table is the thing everyone reads. The manual's failure
list has a column called "Guard", one row of which has been quietly wrong since
it was written.

Two cheap habits fall out of it, and the second is the one worth keeping:

1. A check whose registry is *data* wants a self-test over that data's shapes,
   not over the one case that motivated it. This one now has twelve fixtures —
   lowercase, capitalised, gerund, plural, participle, historical, beside-the-
   new-name, allow-listed suffix, wrong case on a product, and a non-inflecting
   entry that must not inflect. **Gates 40 → 41.**
2. **Grep for what a guard claims to cover before trusting the claim.** One
   `grep -rin whitelist data/` would have found this at any point in five years.
   Nobody ran it, because the check existed and the build was green — which is
   the precise failure mode a green build creates.

```
renames 6 fixed across 4 domains · check_renames self-test 12 fixtures
gates 40 -> 41 · probe 105 · 101 answered · smoke 163 · search 51 · a11y 31
resilience 64 · mobile 15 · visual 2 · backup 3
```

---

## Session — applying the last finding to the next guard, and the port list nothing read

The previous record ended on a habit rather than a fix:

> **Grep for what a guard claims to cover before trusting the claim.**

So it was applied to the other guards, and the interesting result is that
**most of them survived it.** `lint_content.py` claims to find hard-coded
colours; sweeping every hex literal in `data/` outside code blocks turns up
exactly two, and both are the cases its own docstring says it deliberately
excludes — *"deploy #4521"* and a card teaching hex notation. That check does
what its row says.

`check_contradictions.py` did not.

### Fifteen services, fourteen of them from one domain

Its port half reads prose — *"SSH on port 22"*, *"port 22 (SSH)"*, *"22/tcp"* —
and prose is where a port gets **mentioned**. It is not where a reference
**states** one. `net` carries *Common Ports — Protocol Reference*, a table whose
header row reads `Port(s) | Protocol | Transport | Security Notes`, and the
check could not read a table. A wrong number in that table is simultaneously
the likeliest port error on this site and the least likely to be caught by eye.

Reading by **header** rather than by shape — a table qualifies when one header
cell names a port and another names a protocol or service, and no other table
qualifies — took the count from **15 services to 44**.

### The combined row, which is where a naive reader invents a finding

The first prototype reported **IMAPS on 993 and 995**. The row is:

```
993 / 995   IMAPS / POP3S
```

The row is correct and the reader was wrong, which is the exact failure this
file exists to avoid committing. Three shapes, and only one needs a rule:

| Row | Reading |
|---|---|
| `20 / 21` · `FTP (data/control)` | one service, two ports — both are FTP |
| `22` · `SSH / SFTP / SCP` | one port, three services — all three |
| `993 / 995` · `IMAPS / POP3S` | two and two — paired positionally |
| `80 / 443 / 8080` · `HTTP / HTTPS` | **skipped.** Which goes with which is not in the row, and guessing is how a check starts inventing findings |

Parentheticals are stripped before splitting, so the slash inside *FTP
(data/control)* is not read as a separator.

### The second rule was found by the injection test, not by the fixtures

The fixtures passed with only the first and third rules. Then a wrong port was
injected into the real table — and **nothing happened**, because `22 | SSH /
SFTP / SCP` is three names and one port, which the rule skipped as ambiguous.
It is not ambiguous; it is how a reference writes a family, and skipping it lost
the site's only tabular statement of the most quoted port on it.

With the rule added, the same injection reads:

```
SSH: 22 in net; 2222 in net
```

and the multi-port count returns to eight on restore. **A fixture suite proves
the rules you thought of.** Running the check against the real file, having
deliberately broken it, is what finds the rule you did not — and this is the
second time this session that the difference has produced the finding.

The eight services now reported with more than one port are all legitimate
pairs — DHCP 67/68, FTP 20/21, IPsec 500/1701/4500, NetBIOS 137/139, SIP
5060/5061, SNMP 161/162, DNS 53/853, TLS 443/853 — which is the report doing
its job: it says *read this list, do not automate it*, and the list is readable.

```
port table 15 -> 44 services · self-test 17 -> 18 fixtures · 41 gates green
smoke 163 · search 51 · a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```

---

## Session — do the gates actually fire, and the thousand reads nobody checked

Two sessions of auditing guards by reading them. This one asked the cruder
question instead: **break the file on purpose and see whether the check
notices.** Six injections, each in a place awkward enough to be a plausible
blind spot — a cross-reference inside a table cell, a hex literal in a `style`
attribute on a `<td>`, an unclosed `div` mid-card, an undefined custom property,
a `data-checked` in the future, an old product name in a table:

```
xref: a broken cross-reference inside a table cell          FIRED
colour: a hex literal in a style attr on a table cell       FIRED
markup: an unclosed div at the end of a concept card        FIRED
css-vars: an undefined custom property                      FIRED
volatility: a data-checked in the future                    FIRED
renames: an old product name in a table cell                FIRED
```

Six for six, which is the answer you want and is worth the ten minutes it took
to be sure of rather than confident about.

### The gap was not in what a guard checked. It was in where it looked

`check_css_vars.py` exists because of `var(--bg1)` — a name nothing declares,
which CSS handles by discarding the declaration and **inheriting**, so the
symptom is a plausible wrong colour rather than a missing one. Its docstring
scopes it to `style.css` and gives a reason:

> The `data/*.html` corpus mentions `var(--gap)` and `var(--spacing-md)` inside
> code samples that *teach* custom properties, and flagging a teaching example
> would be the instrument being wrong about what it is reading.

That is right about the corpus and wrong about the scope. A `var()` inside a
**style attribute** is not a teaching example — it is a live declaration with
exactly that bug available to it. The counts settle it:

| Where | Reads |
|---|---|
| `style.css` | 17 names, checked since the file was written |
| `style="…"` in `data/*.html` | **1,061**, checked by nothing |
| `script.js`, written into generated markup | **10**, checked by nothing |
| `var()` anywhere else in `data/` | **4** — the teaching examples, and scoping to the attribute excludes them by construction rather than by exemption |

All 1,071 are clean today. That is the point: the check now holds them there,
and it needs no allow-list to do it.

### The boundary was the shape of the bug, not the shape of the class

Worth stating because it is the second time this session:
`check_renames.py` matched case-sensitively because the rename that motivated it
was written in lower case. `check_css_vars.py` read only the stylesheet because
the `var()` that motivated it was in the stylesheet. **A guard written from one
defect inherits that defect's accidents**, and the accidents are invisible
afterwards because the check is green and the row in the table says what it is
for.

The rule this file should have had from the start, and now does: *every place
the site names a custom property, the name is declared or it is not.*

```
css-vars now covers style.css + 1,061 attribute reads + 10 in script.js
self-test 7 -> 13 fixtures · 6 injections, 6 fired · 41 gates green
smoke 163 · search 51 · a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```

---

## Session — the half of the acronym check that was written backwards

The breadth census in `lint_content.py` has said the same thing for many
sessions — *64 single-meaning acronyms rendered in 6+ domains; breadth is the
only signal that a second meaning has been borrowed somewhere* — and the manual
lists the matching failure: **two wrong acronym expansions shipped and were
found by reading, not by any check.** So the queue was read.

It found something one layer down from where it was looking.

### The site writes definitions both ways round; the check reads one

`check_contradictions.py` has `INLINE_EXP_RE`, which matches `ACRO
(Expansion)`. The site also writes `Expansion (ACRO)` — *"Tech companies
borrowed the **Incident Command System (ICS)** from emergency services"* — and
there are **85 of those**, none of them ever in front of the check that exists
to compare them with the dictionary.

Reading the reversed form needed two normalisations, both mechanical:

* **A leading article belongs to the sentence.** "…is An Architecture Decision
  Record (ADR)" defines the same thing as "Architecture Decision Record".
* **A trailing `s` is the sentence's, not the expansion's.** "Web Application
  Firewalls (WAF)" is not a disagreement with "Web Application Firewall".

Without those, five of the fifteen findings would have been the instrument being
wrong about what it was reading, which is this file's oldest rule.

### And a dictionary with two entries missing from it

```python
return {e["a"].upper(): [m["e"] for m in e["m"]] for e in entries}
```

The dictionary deliberately distinguishes **`SOC` from `SoC`** and **`IOC` from
`IoC`**. Upper-casing collides them, and a dict comprehension lets the later one
win — so this check had been reading a dictionary with *Security Operations
Center* and *Indicator of Compromise* silently absent. Nothing noticed, because
**the check's job is to find disagreements and a meaning it cannot see produces
none.** Merged now, which is right rather than merely safe: the comparison is
case-insensitive anyway.

### What the ten real findings were

Two were spellings — one card writing *Approximate Nearest Neighbor* two lines
from an annotation saying *Neighbour*, and *Organisational Unit* against the
dictionary's *Organizational*. Aligned to the dictionary, which is what a single
source of truth is for.

The other eight were **meanings the site uses and the dictionary does not
carry**: Language Server Protocol, Internal Developer Platform, Top Secret, EFI
System Partition, Tuition Assistance, Global Catalog, Incident Command System.
Three of them were sitting in a `n` note reading *"Also: Incident Command
System"* — recorded as a remark where the reader of the acronym page sees one
meaning and the card means the other. They are meanings now.

### The change immediately made another gate fire, correctly

Giving ICS a second meaning turned it into an ambiguous acronym, and
`lint_content.py` **failed the build** for `sec` and `threat`:

> ICS renders in 'sec' with no byDomain decision, so it annotates as 'Industrial
> Control System'. Add "sec" to that entry's byDomain.

Which is the guard working: an implicit choice became an explicit one the moment
a second meaning existed to choose between. `ops` is the Incident Command
System; `sec` and `threat` are industrial control. **The ambiguous-acronym
counter fell 4 → 3**, the first time it has moved.

`check_plan_numbers.py` then caught the README, which states the dictionary's
size and had not been told about the new entry. Both guards did in one run what
this session has spent three waves discovering by hand.

### And the dictionary disagreeing with itself

Aligning *Organisational Unit* to the dictionary did not take in `infra`,
because the annotator kept putting it back — from the dictionary. **`LSDOU`
expands to "Local, Site, Domain, Organisational Unit" and `OU` expands to
"Organizational Unit".** Two entries in the single source of truth, one term,
two spellings, and no check looks *inside* the dictionary: `check_contradictions`
compares the content against it and takes it as given.

Fixed by hand rather than by a tool, because n is one and a check for "no two
entries spell the same term differently" needs a notion of "same term" that this
repository would have to invent. Worth knowing it is unguarded, though: the file
every other acronym check treats as authoritative is the one file nothing
checks. The remaining British spellings in `ops` are *Organisationally* and
*Organisational Memory* — ordinary prose, not the product term, and correctly
left alone.

```
reversed-form definitions now read: 85 · dictionary merge fixes 2 lost entries
8 meanings added, 2 spellings aligned · ambiguous acronyms 4 -> 3
dictionary 1,102 -> 1,103 · 41 gates green · probe 105 · 101 answered
smoke 163 · search 51 · a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```

---

## Session — checking the file every other check treats as authoritative

The previous record ended on a sentence that was meant as an observation and
turned out to be a queue:

> The file every other acronym check treats as authoritative is the one file
> nothing checks.

So it was checked, seven ways. **Four came back clean and two of the checks I
designed were wrong**, which is most of what this session was worth.

### The two that should not exist

**Spelling consistency.** The dictionary is British-spelled prose, so a word
appearing in both conventions looked like a defect worth finding. It finds two
pairs and both are correct:

```
neighbour (ANN)  vs  neighbor (NDP)    — Neighbor Discovery Protocol, RFC 4861
fibre (FCoE)     vs  fiber (FDDI)      — Fibre Channel, and Fiber Distributed
                                          Data Interface, each a registered name
```

Two findings, two false positives. A check with that record does not get
written.

**Dead per-domain configuration.** 34 of 204 `byDomain` decisions name a domain
the acronym never appears in, which reads like stale config until you look: they
are *anticipatory*, pre-answering the question for the day the term arrives, and
deleting them would silently hand that day's writer the default meaning. The
first version of the measurement was also simply wrong — it borrowed the
annotator's rule that skips slash compounds, so **`CI/CD` did not count as `CD`
appearing anywhere** and inflated the finding to 51. The instrument was wrong
about what it was reading, twice in one wave.

### The three that were worth writing, and what they found

The fields that steer the annotator are the quietest possible place for a
defect: `annotate` falls through to `m[0]` when it is misspelled, a misspelled
`byDomain` key is simply never consulted, and the build stays green while the
wrong expansion ships **site-wide**. That is failure #10's exact shape arriving
through configuration instead of prose. Four rules, all passing today, all now
held there.

Then two rules about the meanings themselves, and these found things:

| Entry | Carried | Reading |
|---|---|---|
| `ATT&CK` | *Adversarial Tactics, Techniques, and Common Knowledge* **and** *…Techniques and Common Knowledge* | An Oxford comma is not a second meaning. The dictionary page listed both |
| `DPAPI` | *Data Protection Application Programming Interface* **and** *Data Protection API* | One of them leaves an acronym short. The differing tail's initials spell it, which is the definition of being the same phrase |

Both are decidable, which is why they are rules and not a similarity score. And
**seven entries carried `annotate` beside `noAnnotate`** — a value the annotator
can never reach, naming in every case the meaning it would have defaulted to.
A comment wearing a setting's clothes, removed.

### The pattern across three waves now

```
check_renames      matched case-sensitively    because the rename was lower case
check_css_vars     read only style.css         because the var() was in style.css
check_acronyms     read only the prose         because the wrong expansion was prose
```

**A guard written from one defect inherits that defect's accidents.** The
accidents are invisible afterwards, because the check exists, the build is
green, and the table in this file says what the guard is *for* rather than what
it *does*. The cheap counter-habit, which has now paid three times: when a
guard's row says it covers a class, spend ten minutes proving it covers the
class and not the instance.

```
check_acronyms self-test 12 -> 24 fixtures · 7 inert fields removed
2 duplicate meanings collapsed · 1,180 -> 1,178 meanings · 41 gates green
smoke 163 · search 51 · a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```

---

## Session — asking the question the reader asks, not the one the writer filed it under

Three batches of reader questions now, and the third was written differently on
purpose. Batches one and two asked about **subjects** — *what is a subnet mask*,
*third party risk*, *incident postmortem* — and opened at about a third missing.
Batch three asked about **symptoms**, aimed at the domains the first two barely
touched:

```
my query returns duplicates          the load balancer says unhealthy
my regex is too slow                 why is my cloud bill so high
my tests pass individually but       my lambda times out
  fail together
```

**Six of the nine missed.** Two thirds, against a third for the subject-shaped
questions, and every one of the six was a card that covers its mechanism
thoroughly and had never written down the sentence a reader would type.

That is the pattern this session has been finding one instance at a time — cron,
printers, SSH, inodes, Group Policy, mapped drives, the M365 playbook — arriving
as a measured rate rather than an anecdote. **A reference is written from the
subject outwards and read from the symptom inwards**, and nothing in a normal
review notices the gap, because from inside the card the subject is obviously
covered.

### What each one turned out to be missing

None of the six needed a word. All six needed the sentence the word belongs to:

* **SQL Joins** explains fan-out and never says *duplicates* — which is what
  people call it. The tell is that the row count is a clean multiple of what you
  expected, and the fix is aggregating the many side, not `DISTINCT`, which
  hides the fan-out and leaves `SUM()` just as inflated.
* **Load Balancers** covers health checks well and never says *unhealthy*. So
  the causes are ranked now, and three of the four are the check rather than the
  server: unreachable from the balancer's own subnet, a `401` or a redirect
  where `200` was expected, a timeout shorter than the endpoint's own dependency
  call. Curl the health path from the balancer's side of the network first — if
  it answers and the console still says unhealthy, the disagreement is the
  finding.
* **FinOps** is an answer to *"why is the bill so high?"* and never asks it.
  A bill with no attribution is a single large number, and a single large number
  can only be negotiated, not reduced.
* **AWS Serverless** describes Lambda's scale-to-zero and never its ceiling.
  *"My Lambda times out"* is usually the design saying it is not a function.
* **Test Data** names order-dependent failures; *"they pass individually and
  fail together"* is that sentence said out loud, and hearing it as a diagnosis
  rules out timing and environment in one go.
* **Catastrophic Backtracking** needed nothing at all — see below.

### One of the six was the matcher, and it took two words to prove

```
regex slow       →  Catastrophic Backtracking — When a Regular Expression Is a
                    Denial of Service
regex too slow   →  nothing
```

The card is right there. `too` was a hard requirement, and a card about a regex
that takes minutes has no reason to contain it — and the query is two content
words, so the relaxation stage's floor of two cannot drop it. **A comparative
intensifier is never a subject**, so it joins `explain` and the question words.

`only` at 55.6% of topics and `just` at 22.1% were measured beside it and left
alone: both are load-bearing here — *only the first hop*, *just enough* — and a
stop list earns its entries one at a time.

```
probe 105 -> 116 questions · 112 answered · 0 unexplained · 5 cards given their
symptom · 41 gates green · smoke 163 · search 51 · a11y 31 · resilience 64
mobile 15 · visual 2 · backup 3
```

---

## Session — the domain with thirty-nine topics and nothing on the cascade

Batch four, same shape as batch three and aimed at the domains still barely
probed — `script`, `web`, `ai`, `endpoint`. The rate held: **six of nine
symptom-phrased questions missed**, against a third for subject-phrased ones.
Five were sentences a card had never written down. One was a whole card that
did not exist.

### `my css is not applying` returned nothing at all

`web` carries 39 topics — Flexbox, Grid, Responsive, Modern CSS, the DOM, the
event loop, React, bundlers, Design Systems — and **nothing on the cascade**.
No specificity, no origin order, no layers-versus-`!important`. The foundation
every other CSS card sits on was the one thing missing, and the domain's own
shape made it invisible: each CSS topic pairs a "what it is" card with a named
failure mode, and none of the five failure modes was *the rule did not apply*.

Written to that shape, with the part worth carrying being the ladder:

| # | The question | What wins |
|---|---|---|
| 1 | Origin and importance | A *user* `!important` beats an author one — how a reader's accessibility stylesheet overrides yours |
| 2 | Cascade layer | Unlayered beats layered, later beats earlier — **and for `!important` the whole order reverses** |
| 3 | Specificity | A tuple compared left to right, not a three-digit number. Eleven classes never add up to one id |
| 4 | Source order | Only here. This is the rung people think is rung one |

And the failure card's first row is the one that matters: **a struck-through
declaration and a missing declaration are completely different bugs, and they
look identical from the editor.** Open the inspector before the stylesheet.

### The thing found by chasing an anomaly

`the model keeps making things up` reached its card and returned **thirty**
results, with the card's exact phrase in exactly one of them. The single-result
escalation was firing on a perfect hit, because the named-topic guard compares
the query's words against the slug's words *literally* — and the query says
`model` where the slug says `models`. It now runs both through the same plural
fold as the conjunction, and the query returns one.

That guard was written two waves ago to stop exactly this, and it had a hole in
it the width of a plural. **A guard you added to protect a case can still miss
that case**, and the only way to know is the anomaly: thirty results for a query
whose phrase exists once.

### The rest

*"The model keeps making things up"* is a fair description of the symptom and a
misleading one of the cause — nothing is being made *up*, in the sense of a
decision to invent; the same machinery produced the true sentence with the same
confidence. The endpoint card says *a device that shows as non-compliant* now,
which is what the console says. And `script`'s file-handling card already
answered the encoding question.

```
probe 116 -> 124 questions · 120 answered · 0 unexplained
topics 1,551 -> 1,552 · related 4,790 -> 4,798 links, mainland 1,466
41 gates green · smoke 163 · search 51 · a11y 31 · resilience 64 · mobile 15
visual 2 · backup 3
```

---

## Session — forty-seven topic names with a space in the wrong place

Batch five of reader questions, aimed at `hw`, `infra`, `threat`, `cs` and
`mind`. The rate held a third time — six of eleven missed — and the fixes are
the usual shape, three of them worth repeating:

* **"The computer randomly restarts"** is the commonest intermittent-fault
  report, and it splits in one question: a machine that reboots *without* a stop
  screen was never asked to reboot — it lost power long enough to drop out,
  which is supply, thermals or a connector. One that shows a stop screen crashed,
  and that is a different investigation entirely.
* **"No signal" is the monitor reporting on the cable, not on the computer.**
  Five of the six checks are outside the monitor, and the monitor is the part
  the ticket names — because it is the part with a screen to say something on.
  Swap the cable rather than reseating it: reseating fixes a connection and
  tells you nothing about a cable that failed internally, which is the one that
  comes back next week.
* **A process that vanishes with nothing in its own log** did not crash — it was
  killed, and a process cannot log its own `SIGKILL`. `dmesg` has the verdict,
  and the trap is that the killed process is frequently not the one that
  consumed the memory: the kernel picks by score, so the database dies and the
  batch job that caused it carries on.

### And then the gate caught something none of that was looking for

Adding a per-domain decision so `POST` expands correctly in `hw` made a smoke
check fail:

```
FAIL : every landing card's 'start here' names resolve, in all domains
       — hw: POST, Beep Codes & Diagnostic LEDs — Reading a Machine That Will Not Boot
```

The name the page had was **`POST , Beep Codes`**. The annotator writes
` <span class="acro-exp">(…)</span>` after an acronym, and the code that strips
it back out to recover "the title as written" left the leading space stranded in
front of whatever punctuation followed. Scanning every topic: **forty-seven
names carried it.** `SPF, DKIM , DMARC`. `MTU , Fragmentation`. `SSRF , XXE &
Deserialization`.

Not cosmetic: that text is the name the search index, the study list, the jump
lists and the start-here resolver all compare against. It had been there for as
long as the annotator had, and the only reason it surfaced now is that one of
the forty-eight happened to be named in a landing card.

### The fix was wrong twice, and the second time was the interesting one

**Attempt one** tidied every space-before-punctuation in the title. That looked
obviously safe — slugs drop punctuation and collapse whitespace, so `POST , Beep`
and `POST, Beep` have always produced the same slug. They do. But:

```
Custom Properties, :has() & Layers
```

That space is nowhere near an acronym, and closing it merges `Properties` and
`has` into one word, moving the Modern CSS permalink. `suggest_related.py
--check`, `check_paths.py` and two smoke checks all failed on the same moved
slug within a single run.

**Attempt two** added a lookahead — tidy only when no word character follows.
It worked, and it was still the wrong shape, because it operates on the whole
title and can touch text that had nothing to do with any acronym. The near miss
was not bad luck; it was the surface.

**The actual fix is one character, and it was already written three times in
this repository.** The annotator emits ` <span class="acro-exp">(…)</span>`, and
the space belongs to the span:

```
lint_content.py      \s*<span class="acro-exp">…      correct since it was written
gen_cheatsheet.py    \s*<span class="acro-exp">…      correct
stamp_freshness.py   \s*<span class="acro-exp">…      correct
script.js               <span class="acro-exp">…      the odd one out
```

In the pair that is supposed to be byte-for-byte identical. Taking the space
with the span cannot touch anything that was not adjacent to something removed,
so `:has()`, `.NET` and `.intunewin` are safe by construction rather than by
lookahead. `labelText()` needed the DOM version of the same idea — that space is
a separate text node, so it survives `remove()` — and trims only the node
immediately before each span.

**The reason to write this down is the sequence.** A content wave touched an
acronym's configuration; that exposed a long-standing defect in unrelated code;
the obvious fix moved a permalink; three separate gates caught it before it
could ship; and the correct fix turned out to be a convention the repository
already followed everywhere else. None of those five steps was planned, and the
middle two are the argument for the other three existing.

The transferable part is the last step. **When a fix needs a special case, check
whether the codebase already solved the general one somewhere.** It had, in
three files, and the version that needed no special case was one character
long.

```
probe 124 -> 135 questions · 131 answered · 0 unexplained
47 topic names corrected · 41 gates green · smoke 163 · search 51 · a11y 31
resilience 64 · mobile 15 · visual 2 · backup 3
```

---

## Session — the sentence a card is an answer to, and never asks

Batch six, aimed at `script`, `eng`, `ops` and `blueteam`. The rate held a
fourth time, and the five fixes share a shape sharper than "the symptom is not
named". In each one **the card is an answer to a question it never states**:

| The reader types | The card | What it was missing |
|---|---|---|
| `too many alerts` | *Alert Fatigue as a Reliability Problem* | The complaint it is an answer to. "Too many alerts" is not about volume — it reports that the ratio crossed the point where reading carefully stopped being rational |
| `our estimates are always wrong` | *Planning Without Theatre — Honest Estimates* | Its own premise. The estimate was a range read as a date, and **a range is not wrong when the outcome lands inside it** |
| `circular import` | *Modules, Packages & pip* | The failure, which appears nowhere on the site. The error names the innocent module — the one that was half-built when the loop came back round |
| `we got a vulnerability report from a stranger` | *Responsible Disclosure & Bug Bounties* | Nothing, as it turned out — see below |

Both of the first two now return **exactly one card**, which is the best result
this measurement produces.

### The one that was already covered, found by reading the whole card

`we got a vulnerability report from a stranger` looked like the biggest gap of
the batch: the disclosure card is written entirely from the researcher's side,
title included. Writing the receiving-side card was the obvious move.

It is in the card already — compressed into the closing verdict, which is this
site's convention for *the same subject arriving from the other direction*:
*"publish a policy and a contact address, acknowledge within days, never
threaten a good-faith reporter, and give credit."*

So the edit was one clause naming the moment, plus the sentence that verdict was
missing: **the first reply, not the patch, decides whether this becomes an
incident or a story.** **Reading to the end of the card before writing a new one
is the cheapest habit in this file**, and it is the third time this session it
has turned a proposed card into a sentence.

### The query is still a zero, and that is the right answer

It stays at zero because `got` is a verb no reference card has reason to
contain, and a zero is never relaxed — `script.js` settled that with four
measured examples of relaxation turning honest zeros into confident wrong cards.
**A recorded zero on a card that answers the question is a better outcome than a
sentence bent to reach it**, and the note now says which of the two it is.

```
probe 135 -> 143 questions · 138 answered · 0 unexplained · 5 recorded zeros
41 gates green · smoke 163 · search 51 · a11y 31 · resilience 64 · mobile 15
visual 2 · backup 3
```

---

## Session — the one risk that closed itself, and was then left without a condition

This session has added **1,353 lines to this file — a 31% increase** — and at no
point did anybody think about its length. Which is the fifth risk exactly, so it
was worth checking what the register says about it.

It says **Closed**, and nothing else. No *reopens when* column, in the one row
that had earned the right to have one: the fifth risk is the only entry here
that the file closed **by following its own instruction** rather than by
somebody happening to notice. The section directly above it spends four
paragraphs arguing that *a closed risk with no reopen condition is a risk that
will come back unannounced*, gives all four accumulation risks a condition, and
then writes the fifth up as a success story with a State column and nothing else.

### Why it went unnoticed, which is the interesting half

**The evidence for this risk is the file you are reading, and a file does not
look long from inside a session that is adding to it.** Every other row in the
register points at a number in a table a tool checks. This one points at a
property of the document doing the pointing.

That is the accumulation shape in its purest form: a small cost per session,
never collected, and no day on which it becomes today's problem. The register's
own text says *"act when it gets bad" fails precisely because bad has no
threshold* — and then the row demonstrating that was the row left without one.

### The condition

`check_plan_numbers.py` prints the live file's line count on every `make check`
and warns past **8,000**. Measured, not chosen: double the ~4,000 the split left,
and a third of the 22,745 that made the risk acute. Far enough not to nag, close
enough that the file is still comfortably splittable on the day it fires.

It reports and does not fail. A long plan is not a broken build, and gating it
would mean a session that wrote a good record could not commit it.

### The fourth instance of one pattern

```
check_renames      case-sensitive        its own example was lower case
check_css_vars     style.css only        its own example was in style.css
script.js          missing the \s*       three sibling files had it
the risk register  no reopen condition   on the risk that proved they were needed
```

**A rule written for a category tends not to be applied to the case that
motivated it.** Four times in one session, in four unrelated places, found four
different ways — by a grep, by an injection, by a smoke failure, and by noticing
that the file had grown while nobody was watching. The rule is written down now;
the habit it wants is to apply a new rule backwards to its own origin before
applying it forwards to everything else.

```
plan.md 4,323 -> 5,705 lines · reopen condition at 8,000, evaluated by make check
41 gates green · smoke 163 · search 51 · a11y 31 · resilience 64 · mobile 15
visual 2 · backup 3
```

---

## Session — five zeros, four of them one word apart from their own card

Batch seven, across `sec`, `grc`, `devops`, `productivity` and `eng`. Five
queries returned **nothing at all**, and four of those had a card sitting right
there:

```
i keep procrastinating          →  a card titled Procrastination
my terraform destroyed something →  Terraform — Infrastructure as Code in Practice
my code review comments ignored  →  Code Review — Doing It Well
an employee is leaving and we
  think they took data           →  Offboarding as a Security Control
```

Every one of them an **inflection**: `procrastinating` against
*procrastination*, `destroyed` against *destroy*, `ignored` against *ignore*,
and an offboarding card that never says *leaving* or *employee* — it says
*departing person* and *leaver record* throughout, which is better prose and
worse findability.

All four now return **exactly one card**, and none of the edits was a word
dropped in. Each turned out to have something to say:

* **"I keep procrastinating" is said about one task while a great deal else gets
  done that day**, and *keep* is the useful half — a recurring avoidance points
  at a feeling attached to that task rather than at a character flaw.
* **"Terraform destroyed something" is almost never `destroy` run by mistake.**
  It is an `apply` whose plan contained a red line nobody read, because a
  rename, a moved resource or a changed immutable attribute all replace rather
  than update.
* **A comment answered with a reason is not ignored**; one silently left
  unaddressed reads as a judgement about the reviewer. That is what the
  *respond to every comment* row is for, and it is the row that gets skipped.
* **"They took data" is answerable only by telemetry collected before the
  suspicion arose** — which is the real argument for offboarding being a control
  rather than an errand.

### The inflection class, recorded rather than solved

Four instances in one batch, and this session has now seen ten: `sharing` against
*Screen Shares*, `report` against *Reporting*, `spaced` against *spacing*,
`models` against *model*, and these four. `plurals()` folds a trailing `s` and
nothing else, deliberately — the file's own note says a real stemmer needs a
tokenised index and this matcher reads raw text.

A prefix rule would close most of them: `procrastinating` and `procrastination`
share thirteen characters, `destroyed` and `destroy` seven. It would also match
`string` to `str` unless the threshold is high, and a threshold is exactly the
soft, arguable shape this toolchain keeps rejecting in favour of sharp ones.

**So it is written down rather than built**, with its ten instances, because the
next session to consider stemming should decide it with a list and not an
intuition — and because every one of the ten was closable in prose, by a
sentence the card was better for having.

```
probe 143 -> 151 questions · 146 answered · 0 unexplained · 5 recorded zeros
41 gates green · smoke 163 · search 51 · a11y 31 · resilience 64 · mobile 15
visual 2 · backup 3
```

---

## Session — the topic named Vim could not be found by searching for Vim

Batch eight ended on one query the probe would not let go of: `how do i use
vim` missed `shortcut/vim`. So did `vim`. So did every query containing the
word. The topic is *named* Vim, its first sentence is *Vim starts in Normal
mode*, and the search index held both — as `…modal editingvim starts in normal
mode…`.

### An element boundary is a word boundary, and the index did not know

`plainText` drops a tag rather than replacing it with a space, and says why:

> Tags become nothing, not a space. That looks like the more dangerous choice
> and is the correct one: it is what `textContent` does, and the source already
> carries a newline between anything that needs separating.

The first half is true. The second half is a fact about the files that existed
when it was written, and it stopped being true the moment a topic was authored
on one line. `shortcut/vim` is. So is every generated acronym page, because the
generator writes one line per topic.

The word survives the fusion only if it is long enough to be matched as a
substring. `vim` is three characters, and `matcher()` requires a word boundary
below `SHORT_TERM` — for a good reason of its own, the one that stopped `IR`
matching *requires*, *first* and *directory*. Two correct rules, each blameless,
and between them a topic nobody could find by its own name.

The fix is the distinction the original note was reaching for: **block tags
become a space, inline tags still become nothing.** The acronym expansion the
note was protecting — `CIDR (Classless Inter-Domain Routing)` rather than
`CIDR ( Classless Inter-Domain Routing )` — is inline and is untouched.

A census over the built page afterwards: **1,233 of 1,552 topics** were losing
at least one short term to a fused boundary, 6,621 terms in all. Almost all were
reachable by another route — an acronym's expansion is long enough to match as a
substring, which is why `sacl`, `abac` and `ahci` all worked and the defect
stayed invisible for as long as anybody spot-checked it. `vim` had no other
route, and so was the one that showed.

### The `ss` exception was right about `class` and wrong about why

`my tests pass locally but fail in ci` missed the flaky-test card that says, in
its verdict, that the tests **pass** on your machine. `tests`/`test` folded.
`fail`/`fails` folded. `pass`/`passes` could not, because `plurals()` folds one
character and excepted `ss` endings — on the stated ground that *class* is not
the plural of *clas*.

True, and the wrong conclusion. The plural of `class` is not `clas`; it is
`classes`. The exception marked exactly the words that take `-es` and then did
nothing with them, so the rule produced a non-word in both directions:
`switches` offered `switche`, `processes` offered `processe`, and `pass`,
`switch` and `process` offered nothing at all.

Going back the other way, `-es` is two plurals wearing one spelling — `cases` is
`case` + s, `passes` is `pass` + es, and the string does not say which. Both
singulars are offered rather than guessed at: **a wrong alternate is a regex
that matches nothing, a wrong guess is a card the reader never sees.** `-ies` is
the one that *is* decidable and is handled first.

This is not the prefix rule the last session wrote down and declined to build.
That decision stands — a prefix rule needs a threshold, and a threshold is the
arguable shape this toolchain keeps refusing. Two more plural rules are still
rules.

### One first draft, caught by the census it was written for

The first version of `plurals()` returned the term unchanged for anything three
characters or shorter — a guard the old code applied only when *stripping*. It
also stopped `use` offering `uses`, and `why do we use containers`, answered for
eight batches, went to a miss. The probe named it on the next run. A census kept
green is a regression test that nobody had to write.

### Four zeros, four cards that were already there

```
teams meeting audio not working  →  Teams Call Quality — the card says "calls are bad"
laptop battery drains fast       →  Batteries: What Wears Them Out
my ssh key stopped working       →  "Permission denied (publickey)"
my tests pass locally, fail in ci→  Flaky Tests — a Reliability Problem
```

Each gained the sentence naming the symptom it already answers, and each had
something to say once it was written:

* **"The audio was bad in that meeting" is two investigations, and how many
  people said it decides which one** — one call is per-user analytics, a pattern
  is the dashboard.
* **"It drains fast now" is a capacity complaint, not a settings one**, which is
  why the answer is chemistry and not a power plan.
* **"My key stopped working" is how `Permission denied (publickey)` arrives as a
  ticket** — and the error almost never means the key is wrong.
* **The test that passes on your machine and fails in CI is a timing
  assumption**, and the local machine is too fast to violate it.

### The one that was a gap: a page that came out wrong

`the printer prints blank pages` found nothing, and the printer topic covers
offline queues, drivers, deployment and secure release — every way *nothing*
comes out. It had nothing for a page that came out and is wrong, which is the
opposite investigation and an easier one: the path worked end to end, so the
fault is in what was sent or in what put it on the paper.

Six symptoms, ranked by what they actually mean, each with the test that settles
it — and the same first step as the triage order above it, for the opposite
reason. There it proves the device works; here it separates the device from
everything upstream, because the config page is the one page in the building
that no driver, queue or application touched.

### The fifth instance, and the sharpest

```
check_renames      case-sensitive        its own example was lower case
check_css_vars     style.css only        its own example was in style.css
script.js          missing the \s*       three sibling files had it
the risk register  no reopen condition   on the risk that proved they were needed
plainText          tags become nothing   "the source already carries a newline"
plurals()          one character         "class is not the plural of clas"
```

The first four were a rule not applied to the case that motivated it. The last
two are a step past that: **a rule that writes down its own assumption is still
only as true as the assumption, and neither of these was ever checked against
the corpus.** Both notes are careful, both are cited approvingly by later code,
and both were false — one about the files, one about English. The habit the
first four wanted was to apply a new rule backwards. The habit these two want is
to go and measure the sentence that begins *because*.

```
probe 151 -> 164 questions · 159 answered · 0 unexplained · 5 recorded zeros
1,233 of 1,552 topics were fusing words at an element boundary; 0 now
41 gates green · smoke 163 · search 53 · a11y 31 · resilience 64 · mobile 15
visual 2 · backup 3
```

---

## Session — the note that reasoned from a fact it had not measured

The last record ended on a habit: *go and measure the sentence that begins
`because`.* This one is that habit, run once, on the nearest available target.

`script.js` carries a note explaining why its tag pattern is `</?[a-zA-Z][^>]*>`
and not `<[^>]+>`:

> `<[^>]+>` looks equivalent and is not — `WHERE created_at < now()` inside a
> code block has a `>` somewhere after it, so the loose pattern swallows the
> comparison operator and everything up to it.

`lint_content._CODE_TAG` has the same rule, with the same one-line reason. Six
Python tools had the loose pattern, each with its own copy of it.

### Eight spans, four files

```
math.html                  < 0 and f(1) = 1 >          erased outright
script.01-references.html  < <span class="num">        a shell redirect and the tag after it
career.html                <!-- Four cards did not      the comment ends at its own >=,
philosophy.html   ×2         clear the >=15-card bar     and the rest becomes card text
```

Two kinds. Content the loose pattern eats, and comments it only half-eats.

### The paragraph that was wrong

The comment half was already known. `lint_content.gt_in_comment` gates it, and
the note above that gate is careful, specific, and reasons from a measurement:

> Three such comments exist. All three sit *between* topics, so nothing measures
> them and no number on this site is currently wrong.

The first sentence is true. The second does not follow, and checking took one
command. `depth_report.topics()` takes each block from one topic's start to the
**next one's start**, so whatever sits between two topics is measured as part of
the topic above it. All three comments were being counted: **112, 112 and 102
characters of phantom content on three real cards.**

No number was wrong, which is exactly why it stayed invisible for as long as it
did. The mean moves by 0.2 characters across 1,552 topics, and checking every
one of the eight disputed spans against the thin threshold and the deep
threshold, in both directions, gives **zero crossings**. The invariant held. It
held by luck, which is what the note said about the *content* and had not
checked about itself.

### One definition, six imports

`TAG_RE` now lives once, in `lint_content.py`, and `acronym_drift`,
`check_contradictions`, `check_renames`, `depth_report`, `near_duplicates`,
`orphan_report` and `build.py` import it. Three of them already imported
`domain_files` from that file, so the dependency is not new — only the second
thing crossing it.

The gate's own note argued the other way: *gating the condition is cheaper and
more complete than hardening sixteen regexes*. That was true of sixteen copies
and false of one definition, and it was never true of the content half — no
comment rule reaches `< 0 and f(1) = 1 >`. The gate stays, with its reasoning
corrected in place, because the inline `<[^>]+>` calls that read a single
already-narrow match are still there and still cheap to protect.

**Every census output is byte-identical before and after.** That is the result,
not a disappointment: a latent defect closed, nothing to re-verify, and one
paragraph in the repository that now says something true.

```
6 tools + build.py share one TAG_RE · 6 census outputs byte-identical
0 threshold crossings, checked both ways across all 8 disputed spans
41 gates green · smoke 163 · search 53 · a11y 31 · resilience 64 · mobile 15
visual 2 · backup 3
```

---

## Session — the stop word that was rare, and the accents nobody could type

Batch ten, and two matcher changes that both had to argue against the evidence
that admitted the last ones.

### `got`, which fails the frequency test and joins anyway

`WIDE_STOP` has been grown one word at a time, each with a measured
justification, and the measurement has always been frequency: `actually` at
39.1% of topics is filler; `only` at 55.6% and `just` at 22.1% are load-bearing
in this corpus and stayed out.

`got` is at **3.5%**. By that test it is a rare word, and a rare word is
normally precious — it narrows. It joins on the other half of the test, the one
the note stated and never named as the test: **it is never a subject.** Nobody
searches for `got`. It arrives attached to the thing that happened — `i got
paged at 3am again`, `we got a vulnerability report from a stranger` — and a
card describing that thing has no reason to narrate its arrival. Requiring it
requires a word the corpus cannot supply, which is a guaranteed zero and not a
narrow answer.

The second of those queries had been sitting in `query_probe.mjs` for eight
batches as a recorded, unsolvable kind-3 zero, **with the diagnosis already
written out**:

> `got` is a verb no reference card has reason to contain, and a zero cannot be
> relaxed.

Both clauses true, conclusion backwards. A verb no card has reason to contain is
the argument for stopping it. And the thing that noticed was the staleness check
added two sessions ago: the verdict said the query returns nothing, the query
returned six, and the harness said so on the next run.

### 17 accented words, and an English keyboard

`ubermensch` returned nothing. The card names it in a table, spelled
**Übermensch**, and no keyboard a reader is likely to have types that.

A census of the whole corpus: **17 distinct accented words, 31 occurrences** —
Niccolò, Übermensch, Schrödinger, ásatrú, façade, café. Three were unreachable
(`ubermensch`, `schrodinger`, `niccolo machiavelli`); `machiavelli` alone worked,
because the surname carries no accent.

Folding diacritics is a rule and not a threshold, which is the only reason it is
here: NFD splits a letter from its combining marks and the marks are dropped. It
runs on **both sides** — the index at parse, the query where the query is
lowercased. Folding one side would move the bug rather than fix it: the reader
who *does* have the umlaut would become the one who finds nothing. Both
spellings are gated fixtures for exactly that reason.

It costs a highlight. The marker searches the live DOM, where the accent is
still there, so a hit on one of those 31 occurrences opens its topic and marks
nothing in it. A card a reader can reach and has to skim beats a card they
cannot reach.

### The experiment that was run and thrown away

The last session recorded an **inflection class** — ten queries whose word was
one suffix away from the card's — and declined to build a stemmer, asking that
whoever next considered it decide "with a list and not an intuition".

`i got paged at 3am again` was the eleventh, so the list was long enough.
`check_renames.py` already folds `(?:s|d|ed|ing)?`, so the rule existed in this
repository and had not been applied to its sibling — the shape this session has
found five times.

It was built, measured, and reverted:

```
search_test   51/53   "should we fine tune or use rag"  9 > ceiling 8
                      "how do i find a file"          178 > ceiling 140
probe         one more query over 60, and `i got paged at 3am again`
              still returned nothing — "again" is the word that breaks it
```

**The change did not fix the case that motivated it and widened two gated
queries by a third.** The recorded decision stands, now with a measurement
underneath it instead of a prediction. That is worth more than the feature would
have been: the next session to consider stemming has a number.

What fixed the query was the card. *On-Call Done Humanely* said "pages at 3am
for non-issues drive burnout"; it now says being **paged** at 3am for a
non-issue, **and then again the next night**, is what drives it — the recurrence
rather than any one night, which is both the reader's phrasing and the truer
sentence.

### Three more cards that already answered the question

```
what should i put on my resume  →  Your CV — the question is the wrong one,
                                   and the card can say why
my manager wants an estimate    →  Estimates People Can Trust
the printer prints blank pages  →  (the card written last wave, now indexed)
```

*Your CV* opened on "the question is not what to include — it is what earns the
top third". It now names the question first: **"what should I put on my CV" is
the wrong question and a comforting one — the answer to it is "everything", and
everything is what nobody reads.** *Estimates People Can Trust* now opens on who
is asking: **when a manager wants an estimate, what they almost always want is a
date to repeat to somebody else**, which is why the padding cycle starts.

```
probe 164 -> 170 questions · 166 answered · 0 unexplained · 4 recorded zeros
WIDE_STOP +1 (measured against its own frequency rule, and against it)
41 gates green · smoke 163 · search 56 · a11y 31 · resilience 64 · mobile 15
visual 2 · backup 3
```

---

## Session — three cards that were carrying a judgement in a table

The thin counter has sat at eight for several waves with a note beside it
saying seven of the eight are short by design. That note was written from the
badges, which is a reasonable way to triage a list and not a way to read a card.
Read properly, three of the eight had something to say.

### The list first, because the list is the interesting part

The `military` domain has **ten** topics on staff codes. Six are substantial —
prefixes, functional numbers, sub-designators, branch comparison, the
cross-matrix, and how the three parts combine. Four are short, and the learning
path shows why: they are steps 1–4 and 10 of *Reading Military Structure*, an
on-ramp deliberately placed before the deep versions.

So the first instinct — these are duplicates, retire them into the deep cards —
was wrong, and `paths.json` said so in one grep. **A short card placed before a
long one is scaffolding, not redundancy.** What was wrong with them was
different: two of the four had no sentence at all.

### `Common Codes Decoded` — 342 characters, zero concept cards

A bare table of ten codes, eight of which the cross-matrix covers better. The
two it did not cover were the card's actual subject and nobody had noticed:
**XO and NCO are not staff codes.** They sit in that table because they sit in
the same sentences — an org chart says *S4*, *XO* and *SNCO* in one breath — and
a reader who tries to parse *XO* as letter-plus-number gets nothing back. That
failure is the fastest way to learn where the code system stops and the
vocabulary of rank and appointment begins. The card now says so, and the table
that was the whole topic is now the evidence for it.

### `Staff Functions 1–9` — and the contradiction inside it

Same shape, and this one had a factual disagreement with its own deep version:
the thin card listed **S7** among the examples for function 7; *Functional
Numbers 1 through 9* lists J7 · G7 · A7 and notes that usage varies by branch.
One of them was over-claiming, and the careful one is the deep one.

Fixing the row exposed the card's missing sentence, which was sitting in the
table's last column all along: **the gaps are the useful part.** One through six
appear at every level; seven and eight generally start at division. A battalion
holds no budget of its own and has no force-generation role, so there is no S8
and, in most structures, no S7. The number tells you the function; whether the
number exists at all tells you how large the headquarters is.

### `Rules of Engagement — Read This First`

The redteam domain's preamble, and the one every other card in that domain
cross-references. It said *always work inside a signed scope* and stopped there
— which is the advice everybody gives and nobody expands.

It now names what the document has to contain, with the usual omission beside
each line, and ends on the two that actually matter: **the third-party line and
the stop condition.** A client can authorise testing of their own systems and
cannot authorise testing of their provider's, so an engagement that drifts onto
a platform's shared infrastructure has no permission behind it however carefully
the rest was scoped. And the moment a test causes an outage, the only thing that
matters is whether somebody can be reached and told to stop.

### The ceiling that came down

`lint_content`'s "table with no verdict" ceiling has been 12 for many waves,
with the twelve recorded as deliberate: *lookup tables where a judgement would
be filler*. Two of them were not. The ceiling is now 10, lowered in the commit
that earned it, as the note above it requires.

**"A judgement would be filler" is a verdict about a card, and it expires.** It
was true of those two when it was written — they were tables nobody had looked
at — and stopped being true the moment somebody read them. A recorded verdict on
a backlog is a snapshot of attention, not a property of the thing.

### Two measurements that came back clean

Both were run in the habit the last wave set: go and measure the sentence that
begins *because*.

* `lint_content.bare_tables` fires on a table that is the **first** child of
  `.topic-body`. **84 tables sit directly in `.topic-body` and not one of them
  is first**, so the check has never fired on real content. That is not a
  defect: the note above it already records that the highlighting reason was
  fixed in `script.js` instead, that widening this to all 84 was considered and
  rejected, and that what remains is a narrow layout rule. Measured, correct,
  left alone.
* `check_volatility`'s console queue is three rows and **all three are false
  positives** — two generic uses of "the admin center" and one job title. The
  bare `<vendor> admin` alternatives look redundant with `admin cent(er|re)` and
  are not: they catch a table of console names where the word *center* is in the
  heading. The note already says the regex cannot separate *Exchange admin* the
  console from *Exchange admin* the person and prints the sentence so a reader
  can. Measured, correct, left alone.

Two clean results are worth recording next to the two that were not. The habit
is not "the notes are wrong"; it is "the notes are checkable".

```
thin 8 -> 7 · depth tail 2,122 -> 2,135 · verdictless tables 12 -> 10
site's two thinnest topics: 317 and 500 chars -> 1,205 and 1,056
41 gates green · smoke 163 · search 56 · a11y 31 · resilience 64 · mobile 15
visual 2 · backup 3
```

---

## Session — the tail is short on purpose, and the counter-example worth keeping

### Reading the rest of the thin list, because the last wave's note said to

The thin row now reads *the ones left are short by design*, and the last wave
put that sentence there after reading three of the eight. This wave read the
other four, because a claim made from three cases is the shape of claim this
file keeps catching.

They hold. *The Data Interview*, *The Full-Stack Picture*, *Cert Roadmaps* and
*Software Supply Chain Security* are map cards: each one's job is to connect a
domain to the rest of the site, each ends on a judgement, and each would be
worse for being longer. The two `linux` entries below them — *File Ops & Text
Processing*, *Networking (CLI)* — are Linux+ objective references, the same form
the duplicate census already records as deliberate.

Below the thin line the tail is almost entirely the `script` beginner series:
eighteen cards of 600–1,100 characters, three or four concept cards each, and
**zero `.verdict` spans between them**. That reads like a gap and is not one.
Those cards end on judgements — *keep variables as local as possible*, *bugs
love the edges, test there* — inside the concept description, because they have
no tables for a verdict to follow. The `.verdict` class marks a sentence after a
table, not the presence of a sentence worth reading.

**So the deepening wave the depth row asks for has no work in it right now**,
and that is the finding. `Cert Roadmaps` gained one row — an Azure track, absent
from a cert map on a site whose cloud, endpoint and m365 domains are largely
Microsoft — and nothing else in the tail needed a word.

### Two more cards that already answered the question

`my email went to spam` returned **nothing**, against a card titled *Email
Authentication — SPF, DKIM, DMARC* that contains both "spam" and "junk". The
blocker was `went`, and the fix was the opening sentence the card should have
had anyway: **"our email went to spam" and "somebody is sending mail as us" are
the same problem read from opposite ends, and the same three DNS records answer
both.** One card, one hit, and the reader who arrives from either end lands in
the same place.

`somebody deleted the wrong thing` reached seventeen cards and not the
postmortem one, which is about exactly that and never says it. It now opens on
the archetype: *somebody deleted the wrong thing, or shipped the wrong config,
and the only question that matters now is which question the room asks next.*

### The counter-example, recorded rather than fixed

`the intern deleted the wrong thing` is the same query with one extra word, and
it still returns seven cards about nothing. The relaxation stage is working
exactly as designed: `intern` is the rarest word, so it is the one kept.

There is no honest fix. The site has no reason to name an intern, and writing
one in to catch the query is the keyword stuffing this census exists to refuse.
So it is checked in **with a `want` as well as a verdict**, which makes the
harness score it as a wrong-card miss and count it as explained rather than
quietly passing on its result count — the same distinction that caught
`standups` four waves ago.

It is the first entry in the census's wrong-card column, and it is there to stay
visible. **A relaxation rule that keeps the rarest word is right almost always,
and this is what its failure looks like** — worth one row that a future session
reads before proposing to change the rule.

```
probe 170 -> 175 questions · 170 answered · 0 unexplained · 4 zeros · 1 wrong card
thin 7, unchanged and read in full · one Azure track added to the cert map
41 gates green · smoke 163 · search 56 · a11y 31 · resilience 64 · mobile 15
visual 2 · backup 3
```

## Session — the card I wrote to close a query used the site's words, not the reader's

### The queue was empty, so the questions had to be new

Every census came back clean: thin 7 at 0%, 0 deep orphans, 0 unread
duplicate pairs, 0 unexplained probe rows, 41 gates green. That is the state
this file says means *the queue is no longer a list* — so the work had to come
from asking something nobody had asked. **Batch twelve: 27 fresh reader
questions**, spread across all nine reader groups rather than concentrated,
because the previous eleven batches' split by reader is the only thing that has
reliably predicted where the gaps are.

Seven came back zero. The split, after ruling the matcher out on each — retype
with contractions expanded, then with the rarest word alone, *before* concluding
the corpus is at fault:

| Query | Verdict |
|---|---|
| `the certificate renewed and the site still says expired` | **kind 2.** Real gap, written |
| `usb device not recognised` | **kind 2.** Real gap, written |
| `retrospectives are a waste of time` | **kind 1.** The card answers it and never says it |
| `a laptop is beaconing out` | kind 3 — `beaconing` alone reaches 11 cards |
| `nat gateway is the biggest line on the bill` | kind 3 — `cloud` already states the hourly-plus-per-GB-per-AZ billing |
| `floating point rounding is wrong` | kind 3 — the card says *it is not a bug in your code*; `wrong` is one word too many |
| `the meeting invite is an hour out` | **kind 2, named and not written** — see below |

### The best finding was a card that had already ruled out what I found

`sec`'s TLS card carries a four-row *Errors You'll See* table, and under it a
verdict claiming the incomplete chain is **"the only failure in this table that
does not announce itself."** That is a falsifiable claim sitting in prose, and
it is false: the table had no row for the certificate that was renewed on disk
and never reloaded into the running process. It is the second-commonest cert
ticket after plain expiry, and the table's own first row is what causes it —
*Renew/replace cert (Let's Encrypt auto-renews)* is the sentence that makes
people stop at the renewal.

So the row went in, and **the verdict had to be rewritten, not appended to**,
because the claim it made no longer held. The two failures turn out to be
mirror images, which is the sentence the card now leads on: the incomplete
chain works on your machine and fails for everybody else; the renewed-and-not-
reloaded cert fails for everybody while the file on disk says it is fine.
*Renewal is not deployment.* One command settles both, and `ops`'s web-server
card already had it — `openssl s_client … | openssl x509 -noout -dates` — which
is the argument for reading the neighbours before writing: the fix was already
on the site, one domain over, unattached to the failure it diagnoses.

### And then I made the exact mistake I had just written down

Two of the seven zeros were recorded as **kind 1 — the site names the
practitioner's concept and the reader types the symptom**: `data is leaving
over dns` misses because the site says *exfiltration*, and `setting up a new
laptop` misses because the site says *provisioning* and *zero-touch*. I wrote
that pattern into the probe as two verdicts, in this session, before writing
the cards.

Then I wrote the USB card using *enumerate*, *descriptor exchange* and
*unnamed or unknown device* — and re-ran the probe, and `usb device not
recognised` **still returned zero**. The card was correct, mechanism-first, and
unreachable by the person it was written for.

The fix was not a compromise, which is the part worth keeping: *"USB device not
recognised"* is not a keyword to stuff, it is **the string the operating system
puts on the user's screen**, and a card about a failure should quote the words
the reader is looking at. Naming it is the rubric's second property — give the
failure a fingerprint — not an accommodation to a matcher. It now returns
exactly one card, the right one.

**The general form:** *writing down a pattern does not install it.* This file
has recorded that shape four times for rules applied to every case but the one
that motivated them. This is the same defect one step earlier — the rule was
written **for** the case in front of me and still did not reach the card I wrote
ninety seconds later.

### The staleness checker caught its own author, and was right to

`--self-test`'s verdict-staleness check reported my note on `setting up a new
laptop` as claiming a zero on a query returning six. The note does not claim a
zero. It says *"the card is provisioning and zero-touch"* — and `\bzeros?\b`
matched **zero** inside **zero-touch**, because a hyphen is a word boundary.

This is the token-boundary failure this file already records for `DP` inside
`UDP` and `RA` inside `YARA`, arriving in a different alphabet. The guard is the
same shape — `(?<!-)\bzeros?\b(?!-)` — and it matters more than it looks,
because *zero-trust*, *zero-day* and *zero-touch* are three subjects this site
writes about at length, so the false-positive rate was going to climb with every
security wave. Two fixtures added; the self-test fails without the guard.

**The rule about rules holds here too.** The check was written because a note
went false and nothing noticed. The first thing it did once it had a real
corpus of notes to read was report a true note as false — and the temptation was
to reword the note, which would have been bending the record to fit the tool.

### Left named rather than guessed at

`the meeting invite is an hour out` is a genuine kind 2 and is **not** written.
`m365` has 42 topics and says *time zone* **zero times**; the two cards that
cover time zones are `script`'s, and both are written for somebody storing a
timestamp, not for somebody whose room mailbox disagrees with the organiser's
client. The causes — client versus mailbox time zone, a room with its own, a
recurring series created before a DST rule changed, an external iCal with a
floating time — return nothing in that domain. It is named here with its
evidence rather than written in a wave that had already spent its three cards,
because this file's own audit rule says a probe pass producing more than two or
three card edits has stopped being an audit.

The same applies to the two kind-1 rows above: both now carry a `want` and a
verdict, so the next session starts from the finding rather than re-deriving it.

```
probe 175 -> 202 questions · 190 answered · 0 unexplained · 9 zeros · 3 wrong cards
3 cards edited: sec TLS (row + verdict rewritten), hw docks (concept card), career retros (prose)
1 tool fix: CLAIMS_ZERO guarded against hyphenated compounds, +2 fixtures
41 gates green · smoke 163 · search 56 · a11y 31 · resilience 64 · mobile 15
visual 2 · backup 3 · mean/card 1,389 -> 1,390, excluding verdicts 1,122 unchanged
```

## Session — closing the three things the last wave named rather than wrote

### The queue was a list this time, because the last session left one

The previous record ends by naming three findings it deliberately did not act
on: one kind-2 gap with its evidence, and two kind-1 misses each carrying a
`want` and a verdict. That was the whole point of writing them down — **a wave
that stops at its audit limit is only disciplined if the next one starts there**,
and this file has a history of naming work that then waited weeks.

All three are closed. It cost one new topic and two paragraphs.

### `m365` had forty-two topics and said *time zone* zero times

The new card is **Calendar Time Zones — Why the Invite Lands an Hour Out**, and
the sentence it exists for is that *a meeting has no time*. It has one stored
instant and one rendering per mailbox, so "the invite is an hour out" is never a
question about the meeting — the instant is almost always right, and the ticket
is a disagreement between two renderings of it.

That reframing does the diagnostic work, which is why it leads. It makes one
question obvious — **who sees it wrong?** — and that question partitions the
causes in a way nothing else does: one attendee points at a client or mailbox
zone, everybody points at the organiser or a room object, only the panel points
at the room mailbox's own zone, set at creation and never touched again. The
reflex the card argues against is the one a service desk actually uses: walking
the caller through their own Outlook settings, which confirms nothing in three
of the five rows because the wrong object belongs to somebody else.

The second card is the recurring series that is right until the clocks change,
and it carries the one row on the page that is **nobody's mistake** — two
countries changing clocks on different weekends genuinely puts a call an hour
out for a fortnight twice a year, and the calendar is telling the truth. A
troubleshooting card that cannot say *this one is not a fault* teaches people to
keep fixing it.

It closes by naming what it is **not**: the storing-timestamps problem, which
`script` already covers and which the calendar already gets right. Store the
instant, render late — the calendar does that. What is left is a configuration
disagreement between objects that each hold an opinion, and no amount of
correctness in the store prevents it.

### The two kind-1 fixes, and the one that was an inflection rather than a word

`data is leaving over dns` reached seven cards and not the exfiltration one.
The card's own first concept is titled *How Data Leaves* — so the site was not
using a different **word**, it was using a different **inflection**, and the
matcher does not relate *leaving* to *leaves*.

That distinction decided the fix. A stemmer is the obvious answer and this
project already tried one and reverted it, which is a recorded result and not a
thing to re-litigate on a single query. So it was fixed in prose, and the
sentence earns its place independently: *exfiltration is the attacker's word for
it; the defender meets the same event as a question — why is data leaving over
DNS at three in the morning*. Two vocabularies for one event is exactly why that
table is read from both ends, and the card claims to be a detection skill in its
second sentence without ever saying what detection looks like from the inside.

`setting up a new laptop` missed Autopilot the same way. The fix names the
ticket and then inverts it — the point of Autopilot is that **nobody sets one
up** — with the honest cost attached: a profile that is wrong is wrong on every
machine at once, and there is no technician in the loop to notice.

### The new topic was a deep orphan for about four minutes

`orphan_report.py` reported **1 deep orphan** immediately after the splice,
which is the precise condition the register's *unreachable quality* row says
reopens the risk. It was doing its job on the first new hand-written topic since
the risk was closed.

Five bidirectional pairs fixed it, chosen by hand and not from the tool's
ranking — `suggest_related.py` put *Windows DNS Administration*, *Landing Zones*
and *Firewall Policy Design* in the top six, all of them matching on the word
**zones**, which is three different meanings of the word in one list. The tool
scores lexically and says so; the reason the loop's step 10 says *by hand* is
sitting in that output.

It also went onto the `m365-administration` path, after the mailbox-types step
rather than at the end, because the room mailbox is where the fault comes from
and the general playbook is already the last step. Mainland went 1,466 → 1,467,
so it joined the graph rather than starting a fourth island.

### One ordering constraint earned its row in the table again

`make check` failed on a stale social card, because the topic count is rendered
into the image and the count moved. That is constraint #4 in the manual — *any
content change → `make og`* — and it is the second-cheapest thing on the list to
forget, because nothing about editing a data file suggests an image is
downstream of it. The gate caught it in nine seconds.

### And one thing that was checked rather than assumed

The scratch query runner used for diagnosis returned 6 for one query and 34 for
a near-identical one, which looked like state leaking between queries in a
shared page. It is not: they were two different strings, and a **longer** query
returning **more** cards is the staged matcher falling through to a wider stage
when the conjunction finds nothing. Verified by running the pair isolated and
batched and comparing — identical both ways.

Worth a paragraph because the alternative was to quietly discard a session's
worth of measurements on a hunch, and the check cost one command. The file's
third habit is *verify by measurement, not by assertion*, and that applies to
suspecting your own instruments as much as to trusting them.

```
probe 202 questions · 193 answered (was 190) · 0 unexplained · 8 zeros · 1 wrong card
1 topic added (m365, 1,552 -> 1,553) · 2 prose fixes · 5 related pairs · 1 path step
41 gates green · smoke 163 · search 56 · a11y 31 · resilience 64 · mobile 15
visual 2 · backup 3 · mean/card 1,390 -> 1,391, excluding verdicts 1,122 -> 1,123
```

## Session — one navigation layer was gated and the other was only asserted

### Measuring something nobody had measured, which is the register's own habit

The register says it plainly: *once a phase, measure something nobody has
measured*, and all four accumulation risks came from an afternoon of counting
things the repository already contained. The queue was clear again after the
last two waves, so this wave counted.

The claim chosen was the **domain-shape row**, because it is the only row in the
opening table that makes two assertions in one sentence:

> Both navigation layers complete — **0 hand-written orphans, 0 hand-written
> topics off a path**

The first half is measured. `orphan_report.py` names deep orphans, the register
reopens the *unreachable quality* risk on a single one, and the previous wave
watched it fire on a new topic within four minutes of the splice.

The second half had never been checked by anything. **It was false.**

| Topic | Added by | Related links | Path step |
|---|---|---|---|
| `mind` CBT and DBT — What Each One Trains | `6bec6c0` | ✅ | ❌ |
| `philosophy` Qigong — The Three Regulations | `6bec6c0` | ✅ | ❌ |
| `web` The Cascade & Specificity | `65b5c5b` | ✅ | ❌ |

Two content waves, both of which linked their new topics into `related.json`
and neither of which added a path step. That is not carelessness — it is
**exactly what differential enforcement produces**. One layer has a gate that
fails a build; the other has a sentence in a plan. Every session did the half
that was checked.

### Why the coverage line could not show it

`check_paths.py` was already printing *1,490 distinct topics of 1,553*. The
three were in that gap the whole time and invisible, because **60 generated
acronym pages are off every path by design** and swamp them. A reader of the
bare count has no way to tell three strays from the deliberate sixty, and would
have had none at any site size.

So the fix is the move `depth_report.py --thin` already makes for cards that are
short on purpose: when the deliberate cases dominate a count, stop printing the
count and print **the ones a person has to judge**. `check_paths.py` now names
hand-written topics on no path, and says how many generated pages it excluded so
the two numbers reconcile in the output rather than in the reader's head.

### The comment that asserted a fact about two other files

`orphan_report.py` carried this, and it is worth quoting because it is the
mechanism:

> *The same 60 are the whole of the gap in `suggest_related.py --check` and in
> `check_paths.py`, so three reports were each re-deriving the same exclusion in
> the reader's head. One line here says it once.*

True when written. False by the time anybody counted — the path gap was 63. A
comment in one file making a numeric claim about two others is a measurement
written in the one place nothing can check it, and the sentence that makes it
dangerous is the last one: it tells future readers **not to re-derive it**.

Corrected there, and the claim now lives where it can be seen to be true.

### What changed, and the row that makes it stick

Four path steps: CBT/DBT after the anxiety card, qigong after taoism, and the
cascade card in **two** paths — before grid and flexbox in *Frontend, From the
Browser Up*, which jumped from the DOM straight to layout, and after the
selectors card in *The Front of the Web*. Shared steps are established here;
`surviving-on-call` has been in two paths for a long time.

Then the part that matters more than the four steps: **the stranded count is now
a checked row.** `check_plan_numbers.py` derives it, so the plan cannot say zero
while three topics sit off a path, and `check_paths.py` gained a `--self-test`
over the five set-arithmetic cases that decide the split. Gates 41 → 42, and
`check_gates.py` made me add it to CI in the same commit, which is what it is
for.

**It reports and never fails.** A topic does not owe a path, and a gate here
would teach people to pad a syllabus to clear a build — the same argument
`check_volatility.py` makes for never failing its console candidates.

### The general form, and it is not the one this file usually records

The recurring lesson here has been *a rule written for a category tends not to be
applied to the case that motivated it*. This is a different shape and worth
naming separately:

> **Where two obligations are stated in one sentence and only one is gated, the
> ungated half is not half-enforced. It is unenforced, and it decays at full
> speed while the sentence keeps claiming both.**

Nobody skipped the path step on purpose. They did the half that would have
stopped them, which is the only half that was ever going to happen.

```
3 stranded topics found, 4 path steps added, 0 off-path now
check_paths: --self-test + 5 fixtures, names its own strays
check_plan_numbers: Learning paths row now carries the stranded count
gates 41 -> 42, Makefile and CI in the same commit
41 -> 42 gates green · smoke 163 · search 56 · a11y 31 · resilience 64
mobile 15 · visual 2 · backup 3 · probe 193 of 202, 0 unexplained
```

## Session — the register wrote the rule, and Phase 11 never got it

### Applying the last wave's lens to the rest of the file

The previous record ends on a general form: *where two obligations are stated in
one sentence and only one is gated, the ungated half is unenforced and decays at
full speed while the sentence keeps claiming both.* A form like that is only
worth writing down if the next session points it at something, so this one did —
at every remaining number in this file that a tool produces and nothing checks.

**Phase 11 is where they all live**, and every one of them had drifted:

| Claim, as written | Today |
|---|---|
| *46 volatile spans and 5 fact anchors: 51 dated claims* | **45 spans, 12 anchors, 57 claims** |
| *across 1,432 topics* | **1,553** |
| *now down to 2 candidates* | **3** |
| *it is 2 candidates today* | **3** |
| *`check_volatility.py` still reports 46 spans* | **45** |
| *its only two console candidates* | **three** |

Six sentences, none of them checked, all of them wrong. The phase is marked
**📘 living** in the index, which is the part that stings: it was the section a
reader was most invited to trust.

### The rule already existed, three sections down, written for this exact defect

The risk register says it, and says why:

> *No number is repeated here. Each row points at the row of the measured-state
> table that carries its figure, because that table is checked by
> `check_plan_numbers.py` and a second copy would only be a second thing to go
> stale — **which is how this table got wrong in the first place.***

The register learned it the hard way, wrote the rule, and applied it to itself.
Phase 11 sat directly above it carrying six inline copies. That is **the fourth
instance this file has recorded of the same shape** — a rule written for a
category and not applied to the case that motivated it — and the first one where
the rule and the violation are in the same document, eighty lines apart.

Worse: the register **broke its own rule in one row**. The *unfalsifiable
freshness* row repeated *51 dated claims* inline, and its own *where the number
lives now* column said **nowhere — that is the risk**. It knew the figure had no
checked home and wrote a copy anyway, because there was nowhere to point.

### So the fix was to give it somewhere to point

A **Dated claims** row now sits in the measured-state table, derived by
`check_plan_numbers.py` from `check_volatility.py`: spans, anchors, their total,
and the console-candidate count. Thirteen derivable rows, up from twelve.

Phase 11 §1 and §4, the V5 wave, and the register row now all point at it and
carry no copies. §7's audit record is **left as a record** — what that pass
found is history and history does not get edited — but its present-tense
parenthetical is replaced with what is true now, including the third candidate
and why it is a false positive.

The distinction Phase 11 §3 makes survives intact and is now stated where it
cannot be confused: **the numerator was always countable and the denominator
never will be.** The phase's whole argument is about the denominator. Nobody
noticed the numerator was sitting beside it, uncounted, for a year.

### Proved rather than assumed

The row was checked by breaking it: 45 changed to 44 in the table, the tool
reported *Dated claims: the row does not carry 45, 57* and exited 1, then the
file was restored and it exited 0. Adding a row to a checker and not confirming
it can fail is the *asserts it did not throw* row of this file's own three-shapes
table, and it would have been particularly funny here.

```
13 derivable rows (was 12) · 0 drifted · 6 stale prose numbers retired
Phase 11 §1 §4, V5, and the register row now point at the checked row
42 gates green · plan.md 6,670 lines, reopens at 8,000
```

## Session — the front door was the most-read file and the least-checked one

### Pointing the lens at the two documents that are not this one

Two waves ago the lens was *one navigation layer gated, the other asserted*. Last
wave it found six stale numbers in Phase 11. This wave pointed it outward, at
`README.md` and `CONTRIBUTING.md` — the files a **stranger** reads, where this
file is what a returning session reads.

`check_plan_numbers.py` already had a README check. It covered the Domains
table, the icons, the dictionary size, and any bare *N domains*. Everything else
on the page was unchecked, and three of those had drifted:

| README said | Actually |
|---|---|
| measured at **1,545** topics | 1,553 |
| 475 elements at rest instead of **140,926** | 142,790 |
| the closed programmes and **241** session records | 242 |

The existing check's own docstring calls this *"the fifth place this repository
has found the same defect: prose quoting a number about the repo, maintained by
hand, drifting."* It then fixed the one instance in front of it and left the rest
of the page alone — which is the same shape as everything else this run has
found, in the tool written to stop it.

### The check is built so a rewrite is legal

This is the part worth copying, because the obvious implementation is worse.

Each figure is located **by the sentence that makes the claim** — *measured at N
topics*, *instead of N\*\**, *and N session records* — not by scanning the page for
integers. A figure the README no longer states returns `None` and is skipped.

So deleting a sentence is a legal edit and only a **surviving, wrong** number
fails. A check that forces a file to keep saying something has stopped checking
the file and started writing it, and a front door should be free to stop quoting
a number without a build going red.

Both halves proved rather than asserted: 1,553 changed to 1,500 in the README
produced *says 1,500 topics, the tools say 1,553* and one problem; deleting the
clause entirely produced **zero**; restoring gave zero. The sequence matters more
than either result, because the second property is the one an implementation
silently loses.

### And the claim that was better off with no number in it

`CONTRIBUTING.md` said `.ai-table` was *used in 360 tables across 18 domains*. It
is 358 across 16.

The reflex, three waves deep into this, is to derive it and check it. That would
be wrong, and Phase 11 §5 says why — written about freshness, and the argument
was never about freshness:

> **A claim that is rewritten to not depend on a fact does not need a date.**
> Dating a claim promises to re-check it. Rewriting it removes the promise.

Nothing on that page turns on 358 versus 360. The sentence exists to tell a
contributor that `.ai-table` is a real alternative in wide use and not
deprecated, and *"used across most of the site, and the linter reports the live
count"* says that without promising anything. The count now lives in exactly one
place — the tool that derives it — and the page points at the tool.

So this wave added a check to one file and **removed the need for one** from the
other, and the difference between the two cases is a single question: does a
reader's decision turn on the number? The README's topic count is the site's
headline claim about itself. The table count was trivia with a maintenance bill.

### A third instance of one lesson, stated once

Three waves, three files, one shape:

| Where | The gated half | The asserted half |
|---|---|---|
| Navigation | orphans, by `orphan_report.py` | topics off a path |
| Phase 11 | nothing | six numbers |
| Front door | the Domains table | topics, elements, records |

In every case the asserted half was wrong and the gated half was fine, and in
every case a tool that covered part of the claim already existed. **The failure
is never that nobody built the check. It is that the check was scoped to the
instance that prompted it.**

```
README: 3 figures now checked, located by sentence so a rewrite stays legal
CONTRIBUTING: one count removed rather than checked — Phase 11 §5, outside freshness
verified both ways: wrong number fails, deleted sentence passes, restored passes
42 gates green · smoke 163 · search 56 · a11y 31 · resilience 64 · mobile 15
```

## Session — three inflection misses in one batch, and the copula that was missing one form

### Batch thirteen, and a 20% zero rate

Twenty-five fresh questions, five zeros. The split after ruling the matcher out
on each:

| Query | Verdict |
|---|---|
| `permission denied but i am root` | **kind 2**, written — and the zero was a stop word |
| `we outsourced it who is responsible` | **kind 1**, the card says *Outsource the Work, Not the Risk* and never names the question |
| `the screen is flickering` | **kind 1**, the symptom table says *flicker* |
| `the user says the file is gone` | kind 3 — the ladder is real and spread across three `m365` cards |
| `a service account signed in from another country` | **kind 2, named and not written** |

### The card that was missing, and it is a good one

`linux` had five cards on permissions and nothing on **being refused while
root**, which is one of the few Linux faults that genuinely stops people. The
sentence it exists for: *root is the answer to one check, and it is not the
check that failed.* Being root satisfies the discretionary check on the mode
bits. Five mechanisms sit outside it — a read-only mount, the immutable
attribute, mandatory access control, NFS root squash, a dropped capability —
and none consults your uid.

What makes the ticket expensive is that **all five produce identical words.**
`EPERM`, *Permission denied*, and nothing naming the layer. So the diagnostic is
not reading the error harder; it is asking which layer is in play, and four of
the five answer to a read-only command that needs no privileges.

The causes were not evenly absent, which is what made this kind 2 rather than
kind 3. Mandatory access control has a whole topic and says *even root is
constrained*; `strace`'s card names `EACCES` and says to check the path. But
`chattr`, `root_squash`, `remount` and `read-only mount` returned **zero** in
`linux`, and nothing anywhere put the five in one place.

Two judgements in it worth keeping. The read-only row goes **first and not
because it is commonest** — it is the only one that might mean the disk is
dying, and a filesystem the kernel remounted itself is reporting an I/O error.
And the verdict refuses `chmod 777` on the grounds that it *cannot work*: every
row in the table sits outside the bits it changes, so it fails and leaves a
world-writable file behind. **A fix that could not have worked and did not get
reverted is the worst outcome available, and it is the commonest one.**

### The linter caught an invented cross-reference, again, within a minute

The xref was written as *SELinux (Security-Enhanced Linux) & AppArmor —
Mandatory Access Control*, copied from the rendered page where the annotator had
already inserted the expansion. The source title has no expansion in it. Failure
#2 in the manual — *titles reconstructed from memory* — except this one was
reconstructed from the **rendered output**, which is a new way to get it wrong
and the same fix: run the linter, it names the correction.

### Three inflection misses, and why the answer was not a stemmer

`leaves`/`leaving` last wave, and this wave `flicker`/`flickering` and
`outsource`/`outsourced`. Three independent instances is where this file usually
stops calling something a coincidence.

**The stemmer is still the wrong answer, and that is not a guess.** `b90bd2b`
built one, measured it, and reverted it: it breached two ceilings
(`how do i find a file` 129 → 178) and *did not fix the query that motivated
it*. A recorded measurement beats three new anecdotes, so the fix stayed in prose
both times — and both prose edits were better writing independent of the search:
a column headed **Symptom** exists to be recognised in the reader's words, so
*Flickering, or an occasional momentary black* is simply the correct entry, and
naming the question a third-party-risk card is an answer to is the rubric's
first property.

### The one that was a stop word, and the shape it came in

`permission denied but i am root` returned nothing while `permission denied
root` returned eight including the new card. The blocker was **`am`**.

`WIDE_STOP` contains *is are was were be been*. It did not contain *am*. The
copula was complete except for the first person singular — which is **this
file's most-recorded shape, in a list of function words**: a rule applied to a
category with one member missed.

It is the cheapest entry the list will ever take. 61 occurrences in the corpus,
every one a copula — *who am I*, *what am I automating*, *Am I allowed to do
it?* — no acronym claims the letters, and nobody searches for it. The cost of
missing it fell entirely on **first-person symptom queries**, which is how a
reader describing their own problem phrases it. Search gates unchanged at 56/56
with no ceiling moved. `being` was measured beside it (466 occurrences,
load-bearing in titles) and left alone, because the list's own note says entries
are earned one at a time.

### Named and not written

`a service account signed in from another country`. Both halves exist and the
join does not: `sec` governs non-human identity, `blueteam` covers impossible
travel **for people**, and nothing says the obvious thing — *a service account
has no travel to be impossible*, so a geo anomaly on one is a different alarm and
a louder one. Recorded with its evidence rather than written, because the wave
had spent its three cards.

```
probe 202 -> 227 questions · 216 answered · 0 unexplained · 10 zeros · 1 wrong card
1 topic added (linux, 1,553 -> 1,554) · 2 prose fixes · 5 related pairs · 1 path step
matcher: `am` joins WIDE_STOP — search 56/56, no ceiling moved
42 gates green · smoke 163 · a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```

## Session — I filed a kind-2 from a grep, and the card refuted it

### The correction first, because it is the finding

Last wave named `a service account signed in from another country` as **kind 2,
a real gap, not written** — the two halves exist apart and the join does not.
That verdict was reached from a grep over `sec` and `blueteam`. Reading the card
took two minutes and refuted it: `Non-Human Identity` already carries both
alerting rows, *alert on interactive sign-in by a service account* and *alert on
use from a new address, region or client*.

The probe's docstring warns about the inverse of this and has for a long time:

> a kind-3 call is a decision not to write something, and it was being made
> from a topic list.

**A kind-2 call made from a grep is the same error pointed the other way, and it
is the more expensive one**, because a wrong kind-3 leaves a gap and a wrong
kind-2 ships a duplicate. The rule generalises: *neither verdict is safe until
the nearest card has been read*, and the card is the unit, not the domain and
not the grep.

What was actually missing was a sentence. Both rows were carrying a judgement
the prose never made — the *three cards that were carrying a judgement in a
table* shape, again — so it is stated now: **a person's location varies
legitimately and a workload's does not.** Impossible travel is probabilistic for
a human, who flies and uses VPNs, and nearly deterministic here, because a
service account has no travel to be impossible. The query reaches the card
first now.

Then the tool corrected me a second time. With the query answered, its note
became *"a miss that no longer misses"* by the staleness rule's own definition,
so the note had to go and the correction had to live here instead. That is the
rule working exactly as designed: **the probe records defects, not history.**

### `wide` was the one outcome with no verdict trail

Zeros carry a `keep` and are counted explained or unexplained. Wrong-cards do
too. **Wide was incremented into a headline number and forgotten** — for
thirteen batches, three queries sat in it and nothing recorded whether that was
acceptable or whether nobody had looked. Same shape as the navigation claim and
Phase 11's numbers, arriving in the census that found both.

It is scored like the other two now, and the three have verdicts. Two are
inherent and say so: `what is a hash` reaches 126 because *hash* is in a ninth
of the site and every use of it is correct, and `how does dns work` reaches 67
for the same reason. Ranking would fix them; this matcher is a filter by design
and says so.

### The third had a cause, and the fix did not survive contact

`what is big o for` returns **114 cards — a fourteenth of the site — because it
collapses to the single word `big`.** The `o` is one character and dropped as a
free-floating requirement, which is correct and deliberate: a one-character word
narrows nothing.

The measurements that make it a defect rather than a fact of life: `big o`
returns **10** and `big o notation` returns **2**, both correct, because a short
query is answered by the phrase stage and never reaches this one. **A reader who
wraps the term in a question gets a different search from one who does not.**

There is a mechanism in the matcher for exactly this — `joined`, which pairs a
word with its neighbour because `fine-tune` folds to `finetune`. It could not
see this case, because it is computed from the list the one-character word has
already been removed from. So the fix looked obvious: require the pair joined
rather than dropping the short word.

**Built, measured, reverted.** It broke `the 5 whys`, a gated fixture, which
needs the number kept as its own token rather than fused. Narrowing the rule to
letters does not save it either: `what is a c pointer` needs `pointer` and
would get `cpointer`, which is nothing. Nothing in a query says whether a
one-character word is part of a compound or a word in its own right, and that
is Phase 11 §3's conclusion in a different file — **the right response to a rule
that cannot be narrowed is not to ship it.**

One narrowing is left and is *decidable*, which is why it is named rather than
dismissed: keep the join only where the joined form actually occurs in the
folded corpus. `bigo` does, `cpointer` and `5whys` do not. It is not attempted
because it costs a corpus sweep on every query rather than only inside
relaxation, and that is a real budget rather than a guess.

### The fixture that caught the interaction I introduced

Scoring `wide` broke the staleness check within the hour. Its rule — *a note
explaining a miss that now reaches its topic is stale* — fired on all three new
verdicts, because **a wide query does reach its want. That is the definition of
wide**: the answer present inside a set nobody can read.

The rule was right for the case it was written for and had no way to know a
second existed. It now retires a note only when the query is *otherwise
healthy*, and the two new fixtures cover both directions — a wide set that still
reaches its want is not stale, a set that has since narrowed is.

Twelve fixtures, and the guard is real: without it the first fails.

```
probe 227 questions · 217 answered · 0 unexplained · 9 zeros · 1 wrong · 3 wide, all recorded
wide is now a scored outcome with a verdict trail; staleness distinguishes it from solved
one matcher fix built, measured against the gates, and reverted
42 gates green · smoke 163 · search 56 · a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
mean/card 1,391 -> 1,392, excluding verdicts 1,123 unchanged — this wave's prose was a verdict
```

## Session — the two Phase 11 waves that had never been read

### §7 is titled "V1, V3 and V5", and nothing ever said why

Phase 11 §6 lists five verification waves. §7 records an audit pass over three of
them and its own heading names the three it did. **Nothing anywhere explains the
omission of V2 and V4**, and the phase sits in the index marked *📘 living*, so a
reader takes the pass for complete.

They were the only genuinely outstanding items in the file's only remaining
queue, so this wave read them. The full result is Phase 11 §8; what follows is
what the reading was like, which the table there cannot carry.

### Thirty claims, two actionable

**V4 — default retention.** Eighteen duration claims in a retention context. All
five that are vendor defaults already carry a date. The other thirteen are not
claims about the world: `--vacuum-time=7d` and `MaxRetentionSec=1month` are
config examples, *delete after 3 years per schedule DR-014* is a sample policy
inside a sample document, *14 or 30 days for application logs* is advice about
what the reader should set, and *3–6 months of expenses* is a rule of thumb about
money. One is a **quote being argued with** — `cloud`'s *"We keep 90 days"*,
answered in the same row by *Analytics vs Basic vs Archive behave differently* —
and a mechanical check would have flagged the sentence whose entire point is
that the number is not the answer.

The §9 cross-check V4 asks for came back clean too. The two 93-day figures in
`m365` and `cloud` are different subjects that happen to share a number, which is
the shape a contradiction check has to be able to not fire on.

**V2 — service limits.** Twelve limit-shaped claims outside code blocks, two
real: MongoDB's 16 MB document ceiling and Entra Connect's 500-object deletion
threshold. Both now carry a span.

### Both additions are the case §5 says a span is *for*, and that matters

§6 ends on a counter-discipline that is easy to skip: *every wave should reduce
the number of dated claims where it can. A rising volatile-span count is not
automatically progress.* This wave raised it from 45 to 47 and rewrote nothing,
which looks like the failure that warning describes.

It is not, and the distinction is the phase's own:

> The volatile span is right **where the specific number is the point — a limit
> you must design around.** It is the wrong tool where the number was only ever
> illustrative.

The MongoDB card's next words after the number are *model as a separate
collection* — a schema decision taken **because** of that ceiling. Entra
Connect's sentence already carried its durable half, *know the threshold exists
before you meet it*, and the number is what tells you whether your nightly run is
near it. Neither is illustrative. And nothing was rewritten because there was
nothing to rewrite: the other ten were never facts about the world.

### The ratio, which is the actual finding

**Thirty claims examined, two actionable.** The mechanical searches over-match by
about fifteen to one, exactly as §2 predicted, and for the reason §3 gives:
**the shape of a number says nothing about whether the world can move underneath
it.** What separates a limit from an illustration is always the sentence around
it.

`hw`'s *SATA III ceiling ~600 MB/s* is the cleanest example. It looks exactly
like a product limit — a vendor name, a unit, a number — and it is a **published
standard**, fixed forever. It is §2's Wi-Fi-rates case in different clothing, and
it is the fourth time this file has caught the same pattern-matcher on the same
mistake.

Five waves read across two passes, **four real edits in total.** Phase 11 opened
by failing to count the denominator and guessing the site was more disciplined
than a check could show. That guess now has thirty read instances under it, which
is a better answer than the number it set out to produce.

```
V2 and V4 read: 30 claims, 2 dated, 0 rewritten, 0 contradictions
dated claims 57 -> 59 — both limits a card designs around, which is §5's test
V1–V5 now all read, none closed: §6 is a standing discipline, not a queue
42 gates green · smoke 163 · search 56 · a11y 31 · resilience 64 · mobile 15
```

## Session — American spelling, and the dictionary the prose had been disagreeing with

### The request, and the thing that made it more than a preference

The site is written for a Northeast American reader and was spelling *centre*
the British way in **93 places across 22 files**.

The part worth recording is what turned up on the way to checking scope. The
site ships `data/acronyms.json`, and that dictionary has **always** expanded the
same word the American way:

| Acronym | Expansion, as the dictionary has always had it |
|---|---|
| KDC | Key Distribution **Center** |
| NOC | Network Operations **Center** |
| ISAC | Information Sharing and Analysis **Center** |
| CIS | **Center** for Internet Security |
| AZ | an isolated **datacenter** within a cloud region |

So `sec` wrote *Key Distribution Centre* in prose while the dictionary the same
page loads expanded KDC as *Key Distribution Center*. **The prose had been
disagreeing with the reference it ships for as long as both existed**, and no
check could see it because the acronym checker compares expansions against the
dictionary and never the surrounding sentence.

That makes this a correctness fix that happened to arrive as a preference.

### One brand, and the anchor that protects it for free

`Lenovo ThinkCentre` is a product name and must not move. It needs no special
case, and the reason is the same one that decides how the guard is built:
`\bcentre\b` requires a word boundary, and there is none between *Think* and
*Centre*.

The same anchor is why **one registry row is not enough**. `datacentre` has no
boundary before *centre* either, so a single `centre → center` rule would have
silently left every compound behind. Two rows, and a note in the registry saying
why, because the next person adding a spelling rule will hit this exact edge.

### Made a rule rather than an edit

A one-time replace would drift back on the first card somebody writes. So the
convention went into `data/renames.json`, which `check_renames.py` fails the
build on — **the same mechanism that has enforced *allowlist* over *whitelist*
since 2020**, and the registry now says out loud that it holds two kinds of
entry rather than only vendor renames.

**Proved rather than assumed, in both directions.** A `centre` and a
`datacentre` were reintroduced into two domains; the guard named both with line
numbers and exited 1. Restoring them gave 0. Adding a rule to a checker without
confirming it can fail is the *asserts it did not throw* row of this file's own
three-shapes table, and it is the second time this run that habit has been worth
the minute it costs.

### The generated file, which is the whole reason for the ordering table

`CALCULUS-CHEAT-SHEET.md` still said *centre* after the pass, because it is
**generated from `data/math.html`** and the sweep had already fixed the source.
Editing the artefact would have been undone by the next build, and
`gen_cheatsheet.py --check` would have gone red on the next commit rather than
this one. The manual's ordering table exists for exactly this, and this is the
second constraint in it to earn its row this run — `make og` did in wave 2.

```
93 occurrences, 22 files, 1 brand untouched
2 registry rows — a spelling needs the compound form as well as the word
verified both directions: reintroduce -> exit 1 with line numbers, restore -> exit 0
CONTRIBUTING documents it; cheat sheet regenerated from source, not edited
42 gates green · smoke 163 · search 56 · a11y 31 · resilience 64 · mobile 15
```

## Session — "whole reference domains" was true of one of the three

### The claim, and why it was worth testing rather than accepting

`orphan_report.py` has computed islands for a long time, and its docstring
settles them:

> The islands that remain are **whole reference domains** whose neighbours are
> legitimately their own kind: the calculus track, the keyboard-shortcut tables,
> the quotes collection. Requiring every component to be connected would mean
> inventing a link out of `math`, and an invented "See also" is worse than a
> short one.

That is a good argument and it is the reason the census is not a gate. It was
also a verdict on three islands reached from the strongest of the three, which
is the shape this run has now found in the navigation claim, in Phase 11, in the
front door, and in a stop list. So it got measured:

| Island | Islanded | Already on the mainland |
|---|---|---|
| `math` | 16 | **0** — whole, and the argument holds exactly |
| `shortcut` | 7 | **29** |
| `quotes` | 3 | **3** |

**Two of the three were not domains standing apart. They were the cards nobody
got to.** A link from `shortcut/windows` to *Windows Administration
Fundamentals* is not invented when twenty-nine of its siblings already reach
`endpoint`, `linux`, `script`, `sec` and `military` — and the three connected
`quotes` cards are the Stoic, Existentialist and Eastern collections, all
pointing at `philosophy`, while the three islanded ones are the *meta* cards
about sourcing and misattribution.

### One link per card, not one link per component

Worth stating because the cheap version is wrong and looks right. A **single**
link from any island member to any mainland member merges the whole component,
and the census would go quiet.

It would do nothing for a reader. The "See also" strip is per topic: someone
sitting on `shortcut/macos` sees `macos`'s links, not the component's. **Graph
connectivity is a property of the graph and not of the page anybody is on**, so
seven bridges went in, one per card that had an honest target:

| Card | Now also reaches | Why |
|---|---|---|
| `windows` | Windows Administration Fundamentals | the shortcuts, then the job |
| `macos` | macOS for Windows Admins | same, and the translation table is what a Windows person needs next |
| `Microsoft Office (Excel/Word)` | Data Analysis with pandas — Spreadsheets in Code | the step after the spreadsheet stops being enough |
| `Universal Shortcuts` | Desk, Body, Eyes, Wrists, Back | keyboard over mouse is an **ergonomics** move before it is a speed one |
| `Text Editing & Window Shortcuts` | Intermediate Vim — Editing as a Language | the deep end of the same subject |
| `Sourcing a Quotation` | How You Know — Evidence, Certainty, Changing Your Mind | provenance of a claim, which is what both cards are about |
| `Misattributed — Famous Lines` | the same | a quote that survives because nobody checked |

`spotify-media` and `system-general` got none, and that is the discipline
working rather than failing: no honest target existed, and a short strip beats a
padded one. They stay reachable because their neighbours now lead out.

**Mainland 1,467 → 1,478 (98%), three islands → one.**

### The number the judgement turned on was the one not printed

The report named each island and its domain spread and **never said how much of
that domain was already connected** — so the two cases are indistinguishable in
its output, and the verdict written from it treated them as one thing for as
long as it stood.

It prints it now: `math 16 islanded, 0 on the mainland`. **An island whose
domain is wholly islanded is a decision. An island beside twenty-nine connected
siblings is a backlog.** The words are identical without the figure.

### And the slug truncated, exactly where the manual says it does

The macOS bridge was written from the title as
`…the-translation-table-security-model`. The real id ends `-mode`: slugs
truncate at 60 characters, which is failure #7 in the operating manual and cost
a session a one-way edge once. Caught by checking the target against
`related.json` before writing it rather than after — thirty seconds, and the
only reason this record does not have a broken link in it.

```
7 bridges, one per card that had an honest target; 2 cards left deliberately short
islands 3 -> 1 · mainland 1,467 -> 1,478 (98%) · links 4,818 -> 4,832 · 0 one-way
orphan_report now prints mainland coverage per island — the number the call needs
42 gates green · smoke 163 · search 56 · a11y 31 · resilience 64 · mobile 15
```

## Session — three tools nothing runs, and the one that is a census

### The question nobody had asked of `tools/`

Every checker here is wired into `make check` and into CI, and
`check_gates.py` fails the build if the two lists diverge. **Three files in
`tools/` are in neither**, and nothing had ever asked why:

| File | What it is | Verdict |
|---|---|---|
| `retire_topic.py` | Merges a topic and records the alias, so five `localStorage` prefixes survive | A **manual operation**, correctly unwired — it edits content on request |
| `patch_chrome_shortcuts.py` | A one-shot injector from an earlier wave | Same shape, spent |
| `acronym_drift.py` | A **census** — capitalised tokens the dictionary has never heard of | Should be read, and was not |

Two of three are fine. The third is a census, and this file's operating manual
§6 has a rule about those: *a census nobody reads is decoration*, written after a
counter rose 39% while being "tracked". The start-of-session list names
`lint_content.py` and `check_volatility.py` and does not name this one.

### Read, and measured against the bar the repository already set

`check_volatility.py` states the standard in its own comment, and it is the only
place here that puts a number on it: its first version was **21% precise**, and
*"a candidate list that noisy is not a work queue, it is wallpaper."* It was
tuned in one pass over its own output.

`acronym_drift.py` had never been given that pass. It reported **1,485 rows**,
and the largest false-positive class was one rule away:

> **A run of three lowercase letters means the capitals are word starts, not
> initials.**

PowerShell, JavaScript, SharePoint, GraphQL, DynamoDB, PostgreSQL,
CloudFormation, BigQuery, LinkedIn, AppArmor — **344 rows removed, and not one
true acronym among them.**

Three rather than two, and measured rather than picked: `SaaS`, `PaaS` and
`IaaS` are S-**aa**-S, a two-letter middle the dictionary itself uses, and a
threshold of one would take `GHz`, `IPv6` and `10GbE`.

### The 1,141 that are left cannot be narrowed, and that is the finding

The survivors include `GitHub`, `DevOps`, `MySQL`, `NoSQL`, `MITRE`, `Win32` and
`M365` — proper nouns whose shape is **identical** to `GB`, `GHz`, `EU`, `CV` and
`L3`. An initialism's letters are the initials of an expansion and a product
name's are not, and you need the expansion to tell, which is the thing that is
missing by definition.

That is **Phase 11 §3 in a fourth place**: *the distinguishing property is not
the shape of the text.* The list there is now:

| Check | First version matched | Fixed by |
|---|---|---|
| Hard-coded colors | invoice numbers, CSS examples | a color *context* |
| Ambiguous acronyms | every note containing "also" | evidence of real use in two domains |
| Vendor consoles | MMC, `old-admin.example.com` | word boundaries |
| Ageing claims | IP addresses, Wi-Fi standards | **nothing** |
| **Capitalised drift** | **product names** | **a compound-word rule, then nothing** |

The difference from the ageing-claims row is that this one **had a narrowing
available and had never been given it**. So the 344 ship, and the honest label
for the rest ships in the same breath: sorted by frequency the first screen is
where the real ones are, and past that it is product names all the way down.

### And it stays out of the start-of-session list

Which is the decision the §6 rule actually asks for. A census belongs on that
list when reading it changes what a session does; this one, at 1,141 rows whose
top entries are `GitHub` and `DevOps`, would be the decoration the rule was
written against. **It is a reading list before a dictionary wave, and the
docstring now says so rather than implying a queue.**

The alternative — adding it and letting sessions skim it — is exactly how the
counter that rose 39% while "tracked" came to rise.

```
tools/ audited: 3 unwired, 2 correctly so, 1 a census that had never been read
acronym_drift 1,485 -> 1,141 rows; 344 product names removed, 0 true acronyms lost
threshold measured, not picked: 3 keeps SaaS/PaaS/IaaS, 1 would lose GHz/IPv6/10GbE
the remainder hits Phase 11 §3's wall — no property left to require
42 gates green · make check clean
```

## Session — the color check was reading an empty set, and zero looked like health

### Starting somewhere else entirely

The lead was the linter's `401 inline style attribute (ceiling 401)`, a counter
that has not moved in a long time. The theory — `color: var(--cyan)` appears 400
times and `.c-cyan` already exists, so hundreds could become classes — was
**wrong, and measuring took two minutes**: of the 401 *avoidable* attributes,
**7** are a pure color with a matching class, all on `<th>`. The cyan ones are
nearly all in the 757 `.ref-table` first cells where a `c-*` class loses on
specificity, exactly as that comment says.

What the measurement turned up instead was three rows further down the list.

### 168 color literals the check could not see

`lint_content.py` fails the build on a hard-coded color, with this message:

> *hard-coded colour {literal} — it keeps its dark-mode value in light mode.*

Its detector is `HEX_RE = #[0-9a-fA-F]{3,8}` — **hex notation only**. The content
carries **168 `rgba()` literals across ten domains**, and the hex count is
**zero**. The check had been passing on an empty set for as long as it existed,
and a green line that says nothing is wrong is indistinguishable from one that
says *I am not looking*.

It is the defect its own message describes, precisely. `--cyan` is `#00d4ff`
in dark and `#0274af` in light, so `rgba(0, 212, 255, 0.3)` in a card kept the
dark value in daylight.

### Fourteen of them were worse than stale

`rgba(168, 85, 247, …)` appears fourteen times, and `style.css` says what that
number is:

```css
--purple: #ad5ff7;   /* was #a855f7, 4.47:1 on --bg3 — just under */
```

**`#a855f7` is the superseded purple.** A contrast fix was applied to the
variable and fourteen hardcoded copies kept the failing value — so the
accessibility problem the change was made to solve was still on the page,
fourteen times, in the one form the fix could not reach.

### All 168 mapped, which is what made the fix mechanical

154 matched a current theme variable exactly; the other 14 were the purple
above. None was an arbitrary color. So each became
`color-mix(in srgb, var(--X) N%, transparent)` — already house style, used 20
times in `style.css`.

### The proof, which is the part worth copying

`make equiv` exists to say whether a styling change rendered identically, and
this change **should not be identical** — in light mode that is the entire
point. So it was run against dark mode and the output checked numerically rather
than read:

```
154,566 elements compared across 30 domains, 33 properties each
192 colour pairs · 187 numerically identical · 5 genuinely different
```

The 187 are a **serialisation** change and nothing else: Chrome prints a
`color-mix()` result as `color(srgb 1 0.690196 0.12549 / 0.3)` where it printed
`rgba(255, 176, 32, 0.3)`, and 176/255 = 0.690196. Byte-identical rendering,
different string.

The 5 are `rgb(168, 85, 247) → rgb(173, 95, 247)`. That is `#a855f7 → #ad5ff7`:
**the only elements whose appearance changed are the fourteen that were carrying
the pre-fix purple**, and they now carry the corrected one.

A diff of 45 rows read by eye would have been "all the same, fine". Parsing it
turned one number into the finding.

### And the check had no fixtures at all

Which is why nothing noticed. Every other rule in that file has a fixture group;
the color rule had none, so there was never a case asserting *this input must be
reported*. **A check with no fixture cannot tell "nothing is wrong" from "I am
not looking", and this one had been unable to tell since it was written.**

Nine fixtures now: hex, `rgba`, `rgb`, `hsl`, an SVG paint attribute, a ticket
number that looks like hex, a CSS sample inside `<pre>`, and the two forms that
must **not** report — `var()` and `color-mix()` over a variable, because the
point is a color that cannot follow the theme rather than the mention of one.
55 fixtures in the file, 0 failures.

```
168 literals converted in 10 domains · 14 of them the superseded --purple
equiv: 192 pairs, 187 identical, 5 changed — and the 5 are the contrast fix landing
lint_content: FUNC_RE added, 9 colour fixtures where there were none, 55 total
42 gates green · smoke 163 · search 56 · a11y 31 both themes · visual 2 · mobile 15
```

## Session — the triage card had no word for the commonest alert in a modern SOC

### Batch fourteen

Twenty-three questions, four zeros (17%), and one of them was a real gap in a
card this file would have called finished.

`blueteam`'s **Alert Triage — Working the Queue From Alert to Verdict** is a
good card: three concepts, an inversion worth the price of entry (*an alert is a
rule matching, not a thing that happened*), and a cost-ordered question list.
Grepped for the words a prevented alert arrives as:

```
blocked 0 · prevent 0 · quarantin 0 · contained 0 · stopped 0
```

**Zero.** A card about turning alerts into verdicts, in an estate where EDR
blocks hundreds a week, with no word for the shape most of them have.

### The sentence it was missing

*A block is a detection, not a resolution.* The control did its job on this
attempt on this host, and the queue reads that as the end of the matter — but a
block is **evidence of arrival**. Something reached that machine and tried.

The distinction that makes it workable is **delivery versus execution**:
execution was stopped, delivery succeeded, and delivery is the finding. A
payload that reached an endpoint reached it through a path, and that path is
still open when the alert closes.

Which produces one question rather than a full investigation — *what was the
delivery path, and is it still open?* — answerable in about a minute from the
telemetry the card's own third row already uses.

The second card is the part that keeps it honest. **This is not an argument for
working every blocked alert**; there are hundreds a week and treating them as
incidents is how a queue dies, because the analyst stops reading any of them —
strictly worse than auto-closing them on purpose. So it gives a promotion rule
(the same indicator on a host without the control; an unexplained delivery path;
a target that does not receive commodity malware by accident; a second block on
one host in a week; a block late in a chain) and ends on the decision:
**auto-close the rest deliberately, and write down that you did.** A documented
suppression is revisitable; an analyst who has quietly stopped reading a category
is the same outcome with nobody accountable for it.

### Written, reachable, and still a zero

`blocked alert` returns exactly one card. `prevented alert` returns exactly one
card. Both are this one.

`the alert says it was blocked do i still care` still returns **nothing**,
because of `says` and `care` — filler a card about prevention has no reason to
contain, and the relaxation stage deliberately never runs on a zero. Recorded,
not papered over. The content gap was real and is closed; the query is a matcher
limit already documented three times in this file.

### Two more named rather than written

The wave had spent its cards, so both carry their evidence instead:

- **`we found crypto mining on a server`** — `mining` appears **six times
  site-wide**, every one a passing mention in a findings list. The card would
  have one sentence: *mining is a symptom of access, not the incident.* Somebody
  had enough access to run a process, and what they chose to monetise it with is
  the least interesting thing about that.
- **`the autoscaler keeps flapping`** — autoscaling is covered in `cloud`,
  `devops` and `eng`; the oscillation fault is not. **`cooldown` and
  `hysteresis` each return zero across the whole site**, and they are the two
  words the answer is made of.

Naming the missing *words* rather than the missing subject is what makes these
two pickable up by a session that has not read this record — the same form that
got `m365`'s calendar gap written two waves after it was found.

### And the printer already had the card, in the wrong word

`the printer is printing garbage` reached nothing against a concept card titled
*It Printed, and the Page Is Wrong — Blank, **Garbled** or Streaked*, whose
second row is the PostScript-driver-against-a-PCL-device answer. Garbled is the
technician's word; **garbage**, gibberish and *it printed junk* are the user's.
The card now says both, which is the fourth time this run that naming the
reader's word has been the whole fix.

```
probe 227 -> 250 questions · 237 answered · 0 unexplained · 12 zeros · 1 wrong · 3 wide
2 concept cards added to Alert Triage · 1 prose fix · 2 gaps named with their evidence
42 gates green · smoke 163 · search 56 · a11y 31 · resilience 64 · mobile 15 · visual 2
```

## Session — writing the two cards the last wave named, and the verb that cost one its query

### Both gaps written

The previous record named two and wrote neither, with the missing **words**
rather than the missing subject — which is the form that makes a finding
pickable up cold. Both are cards now.

**`eng` — Autoscaling in Practice.** The sentence: *an autoscaler is a control
loop, and every control loop can oscillate.* The delay in the loop is not the
decision, which is instant; it is the time from deciding to having capacity
that is **actually serving** — boot, runtime start, cold cache, two passing
health checks. Two to five minutes is ordinary, and for that whole window the
metric still says what it said before you acted.

So flapping is a **lag problem wearing a threshold costume**, and the reflex —
widening thresholds — treats the symptom and slows every genuine response. The
second card is about metric choice, and its verdict is the one that decides
configurations: **scale on the thing that fills up, alert on the thing users
feel.** Queue depth leads, CPU lags, p99 lags badly; using one metric for both
jobs is where most bad autoscaling comes from.

`cooldown` and `hysteresis` were the two words that returned zero site-wide when
the gap was named. That was the whole diagnosis, and it survived contact with
the writing.

**`threat` — Cryptojacking.** The sentence the last wave predicted: *mining is a
symptom of access, not the incident.* A process ran on your server as some user,
reached the internet, and stayed — and **every one of those facts is true of a
ransomware operator on the same box.** The finding is not *we have a miner*, it
is *somebody can run code here and we did not know*.

The verdict is the part worth keeping: **it is the cheapest true positive you
will get all year.** A miner is an intrusion that volunteered its own detection
by burning a metered resource, and an estate that finds one and cleans it up has
spent the evidence without reading it. Work it as an intrusion and let the mining
be the timestamp — most investigations never get a reliable moment when the
attacker was definitely present.

### And `found` joined the stop list, on a rule already written

`we found crypto mining on a server` returned **nothing** on the day the card was
written, while `cryptojacking` returned it alone and `crypto mining on a server`
returned it among six. The blocker was **`found`**.

This file already settled the test, for `got`:

> a rare word is normally a *narrowing* word and precious. The reason it joins is
> the other half of the test: **it is never a subject.** It arrives attached to
> the thing that happened, and a card describing that thing has no reason to
> narrate its arrival.

`found` is a **reporting verb** of exactly that shape — the reader narrating
their own discovery. 7% of topics, **zero topic titles**, and requiring it
requires a word the corpus cannot reliably supply.

Measured before shipping, not after: search **56/56 with no ceiling moved**, and
`usb found in car park` — a query that has been in the census since batch one —
returns the same two cards it always did. `find`, `finds` and `finding` stay,
because *Finding What Detection Missed*, *Finding and Fixing Weaknesses* and
*Finding Your First IDOR* are titles here.

**This is the opposite of the failure this run keeps recording.** Every other
instance was a rule not applied to the case that motivated it; this is a rule
written for one word being applied to the next word of the same shape, which is
what the rule was for.

### The depth tail moved, which it had not for a while

Two cards of five and six concept cards each moved the **10th percentile from
2,135 to 2,142** — the number the measured-state table calls *what a deepening
wave has to move*. A recent record concluded that the deepening wave had no work
in it, and it was right about the tail: the way to move that number turned out
not to be lengthening thin cards but adding deep ones, because the percentile is
a position in a distribution and new mass at the top pushes it.

The padding counter-metric behaved too — mean 1,392 → 1,393 and
excluding-verdicts 1,123 → 1,124, moving **together**, which is the shape the
row asks for.

```
2 topics added (1,554 -> 1,556) · 9 related pairs · 3 path steps
probe 250 questions · 239 answered · 0 unexplained · 10 zeros · 1 wrong · 3 wide
`found` joins WIDE_STOP on the `got` test — 56/56, no ceiling moved
10th percentile 2,135 -> 2,142 · mean/card and excl-verdicts both +1
42 gates green · smoke 163 · a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```

## Session — the decks were fine, and the isolation table stopped one row short

### Two censuses that came back clean, which is worth the paragraph

The plan records *a flashcard with a blank back* and *a quiz that answered
itself* as things found **by reading**, and nothing has ever counted them. So
they were counted.

**The decks are in good shape.** 1,556 index entries: **1,487** carry both a
concept title and a description, **5** carry a title alone, **0** carry a
description alone, and **64** are excluded — 60 of them the generated acronym
dictionary. The blank-back problem was already solved properly, by a rule about
*shape* rather than domain, so the next lookup card somebody writes is excluded
without anyone remembering to add it.

The one thing the measurement corrected was the comment beside that rule, which
names **six** topics that build an empty card. It is **four**: the AI glossary
and the military code list have since gained prose and the shape test lets them
back in. The comment is now explicit that the six are the evidence that produced
the rule and the live count is whatever `stIsStudyable` says — the distinction
Phase 11 §8 drew between a record and a claim.

### Then `data`, which is comprehensive and stops one row short

Forty-four topics covering vacuum, bloat, isolation levels, repeatable read,
serializable, phantoms, stale statistics and deadlocks. Three phrases return
**zero across the whole site**: `write skew`, `parameter sniffing`, and
`long-running transaction`. The first and third are the two findings.

**Write skew.** The ACID card teaches the four isolation levels against *the
three anomalies — dirty, non-repeatable, phantom*, which is the textbook set and
is what the levels were historically defined against. **None of them is why
anybody needs `SERIALIZABLE`.**

Write skew is: two transactions read the same rows, each checks an invariant
across them, each writes a *different* row. Nothing was overwritten, nothing was
re-read, both commit, and the invariant both checked is now false. Two doctors
each confirming another is on call before going off, both seeing the other, both
going off.

The reason an isolation table cannot express it is the interesting part and it is
now the card's verdict: **the table describes what each level permits, and write
skew is a relationship between two transactions rather than a property of
either.** Snapshot isolation allows it precisely because each transaction is
individually well-behaved. The rule that replaces the table: *if a transaction
reads rows to decide whether it may write, the rows it read are part of what it
is writing.*

**The idle transaction.** The MVCC card says *keep transactions short* and
explains the lock-contention half. The expensive half was missing: an open
transaction pins a snapshot, and **nothing older than the oldest live snapshot
can be reclaimed anywhere in the database** — not just in the tables that
transaction touched.

Which produces the symptom that sends people to the wrong place entirely:
**autovacuum running, on schedule, succeeding — and bloat growing.** It is not
failing. It is finding nothing it is allowed to remove. So the verdict is a
reordering of the investigation: *ask what the oldest transaction is before you
ask anything about vacuum*, which is one query against `pg_stat_activity`, and
`idle in transaction` is the answer more often than any vacuum setting is.

Both cards state the thing the surrounding material implies and never says,
which is the same shape as *three cards that were carrying a judgement in a
table* — except here the judgement was not in the table either. It was absent.

### And the reader's word, for the fifth time this run

`why is my table bloated` returned **nothing** against a card written twenty
minutes earlier whose first symptom row read *Table and index bloat rising*.
`bloat` is the noun the documentation uses; **bloated** is the adjective a person
types, and it appeared twice on the site, both in unrelated domains.

The row now opens *The table is bloated*. Fifth instance this run, and the first
where the card it failed to reach was one I had just written — which is the same
correction as the USB card in the first wave, arriving after the lesson had been
written down twice.

```
deck census: 1,487 strong · 5 title-only · 0 blank · 64 excluded (60 generated)
2 concept cards added to `data`; topics unchanged at 1,556, mean/card unchanged
probe 250 -> 254 · 243 answered · 0 unexplained
42 gates green · smoke 163 · search 56 · a11y 31 · resilience 64 · mobile 15
```

## Session — the diagnosis I had reached by hand five times, printed

### Five is where a tool earns its keep

`usb device not recognised`, `the screen is flickering`, `we outsourced it who is
responsible`, `why is my table bloated`, `data is leaving over dns`. Five zeros
in this run, five identical investigations, and the same three commands every
time: retype the query with its rarest word, grep the corpus for each word, find
the one that is not there.

The fifth was against a card written twenty minutes earlier, by the session that
had already written the lesson down twice.

This file's operating manual settles what to do with that. **Six of ten failures
were caught by a tool, and the ratio is the argument for the tools** — a
diagnosis re-derived five times is a diagnosis that should be printed.

### What it prints, and why it needs no judgement to read

Under every unexplained zero, the probe now shows how many topics contain each
word of the query, one word at a time. The two kinds of zero separate at a
glance:

```
ZERO  "the laptop smells of burning"             0  nothing — investigate
      in the corpus: laptop 106 · smells 0 · burning 8
      → "smells" is not on the site — the reader's word, not a missing card

ZERO  "the same query is fast sometimes and slow other times"   0
      in the corpus: same 711 · query 244 · fast 414 · sometimes 90 · slow 304 · other 684 · times 263
      → every word is here; the conjunction is what failed
```

A word at **0** is kind 1 — *fix in prose, it is better writing anyway*. Every
word present and still a zero is the matcher, and the relaxation stage
deliberately does not run on a zero. No threshold, nothing for a reader to
overrule.

It runs **only on a zero with no recorded verdict**, because it costs a corpus
sweep per query and a zero somebody has already explained has had this done once.

**It is deliberately not a suggestion engine.** It names the absent word; whether
the card should use it is a judgement, and the difference between naming a
symptom a reader recognises and keyword stuffing is exactly that judgement.

### Both of its first two findings were real, and one was a safety gap

The `fast sometimes` one is **kind 3**, and the tool said so before any grep:
every word present. `data` has a concept card titled *The Query That Was Fast and
Went Slow: Stale Statistics and the Plan Flip*. The narrower gap beside it is
recorded — `parameter sniffing` and `cardinality estimat` each return zero
site-wide, and they are the *intermittent* case rather than the one-way flip.

The other one mattered more. `hw` covers a burning smell properly — *Smell of
burnt electronics, no visible damage → power it down* — in **Components &
Schematics**, which is the card for somebody holding a board. The card a person
with a laptop lands on is *Laptops — Batteries, Thermals & What Is Actually
Replaceable*, and it had **zero** mentions of smell or burning. It covers
swelling carefully, including that swelling is a safety issue.

Swelling and a burning smell are not the same urgency, and the card said one and
not the other:

> **Stop.** A burning or sharp chemical smell is not a wear symptom — power down,
> unplug, and do not charge it again. **Swelling gives you days; a smell does
> not.**

The query reaches both cards now. **The tool found a missing safety instruction
on its first run**, from a query written to test whether the tool worked.

### And the `want` was wrong, which the measurement caught

The verdict first pointed at *Systematic Hardware Troubleshooting* — a guess from
the subject rather than from the search. The probe put the row in **Components &
Schematics**, and the card a reader actually needs was a third one. Three
candidates, and the one that mattered was not the guess or the hit.

```
query_probe: per-word corpus counts under every unexplained zero
probe 254 -> 257 · 245 answered · 0 unexplained
2 prose fixes, one of them a missing safety instruction
42 gates green · smoke 163 · search 56 · a11y 31 · resilience 64 · mobile 15
```

## Session — a number I incremented fifteen times, and it was wrong every time

### The register's rule, broken in the index of the file that states it

Two rows carried the session-record count. The measured-state table's row is
derived by `check_plan_numbers.py`. The index table's row at the top of the file
was maintained by hand — and they disagreed **by five, in every version of this
file since the split**: 62 against 67, then 63 against 68, all the way to 78
against 83.

The register three sections down states the rule this breaks, and states why:

> **No number is repeated here.** Each row points at the row of the
> measured-state table that carries its figure, because that table is checked by
> `check_plan_numbers.py` and a second copy would only be a second thing to go
> stale — **which is how this table got wrong in the first place.**

The index row was a second copy. It went stale immediately and stayed stale.

### The part that is about me rather than the file

I incremented it **fifteen times in this run**, once per wave, alongside the
checked one. Every increment was correct arithmetic on a wrong number, and the
wrongness was one subtraction away the whole time: `83 − 242` against
`78 − 242`. I never did it, because the row *looked like* a thing that needed
incrementing and incrementing it made `make check` pass — the check was
satisfied by the other row, so the ritual felt verified.

**A hand-maintained duplicate beside a checked original is worse than a
hand-maintained number alone**, because the green build is evidence about the
copy that is checked and reads as evidence about both.

So the row carries no count now. It points at the checked one, the way every
register row does.

### And the trigger the file set for itself is about to fire

`check_plan_numbers.py` prints the live file's length on every run, and the
fifth risk reopens at **8,000 lines**. At the start of this wave the file was at
**7,861**, and this record was written expecting to cross it.

**It did not.** The file is at **7,922** — the record came to 61 lines and the
threshold is 78 away. So the sentence above was wrong when it was written, and
correcting it is a better demonstration of this section's own argument than
being right would have been: **I forecast a threshold crossing while standing
next to a tool that reports the number, and missed by 78 lines.** The condition
is still false. The split waits for the wave that makes it true, and that wave
will know because the tool will say so rather than because somebody judged the
file long.

That number was chosen carefully — *double the ~4,000 the split left, and a
third of the 22,745 that made it acute* — and the reason the file's most-quoted
passage is about this risk is that it is the only one that ever carried a
**condition** rather than a judgement about when something feels too long:

> That is a condition a session can evaluate by running the censuses it runs
> anyway, and **the session that found it true is the session that acted.**

It was not true when this wave started, at 7,861 lines, and acting then would
have been acting on a forecast — which is the thing this file criticises in
*"act when it gets bad"*, because a forecast has no threshold either. So the
work went first, the record went in, and the condition is now true on its own
terms.

```
the index row's count removed rather than corrected — it points at the checked row now
13 derivable rows · 0 drifted
plan.md 7,861 -> 7,922 · the fifth risk reopens at 8,000 and did NOT fire
the crossing was forecast in this record's own first draft and missed by 78 lines
```

## Session — the diagnostic was wrong twice, and both corrections made it useful

### Batch sixteen, and a first result worth stating

Sixteen questions, eight zeros, and **not one of them was a vocabulary gap.**
Every zero came back *every word is here*. After five kind-1 fixes in this run,
a fresh batch produced no missing-word misses at all.

That reading turned out to be worth about ninety seconds, because the tool that
produced it was wrong twice.

### First: it was not folding, and the matcher is

`the wifi adapter disappeared` reported **`wifi 4`**. The site writes **Wi-Fi**,
53 times in `net` alone. The diagnostic was comparing raw lowercase text while
the search folds separators on both sides of its own comparison, so every
hyphenated term in the corpus was undercounted by roughly tenfold.

**A diagnostic that undercounts is worse than none**, because it turns a matcher
problem into a false *the reader's word is missing* and sends the next session to
write prose that was already there. Folded on both sides now, with the same
function the search uses: `wifi 4` → **`wifi 44`**.

### Second: "every word is here" was true and useless

`the handover was useless` — *handover 14 · useless 30 · every word is here*.
True, and it says nothing about where to look. The conjunction needs every word
in **one** card, so the rarest word is the binding constraint — which is the
reasoning the relaxation stage already uses when it keeps the rarest and drops
the rest.

It names it now: *“useless” at 30 is the binding one, and no card carries it with
the rest.*

### Third, and this is the one that made it actionable

A word can be all over the site and absent from **the one card that should
answer**, and the corpus count cannot see that. `the meeting room screen is
blank` reported *every word is here* — `screen` 116, `blank` 29 — while the
conference-room card said **neither**, describing the same fault as *wrong input
selected* and *check the display's input source*.

Where a query carries a `want`, that question is computable, and it is the
question that matters. So four zeros now read like this:

```
in hw/conference-room-technology…: “screen”, “blank” are not in the card that should answer
in redteam/data-exfiltration-channels…: “exfiltrating” is not in the card that should answer
in sec/phishing-beyond-email-smishing…: “weird” is not in the card that should answer
in blueteam/shift-handover-in-a-soc: “useless” is not in the card that should answer
```

**Four investigations replaced by four lines, and only one of them is a fix.**

### Which is the judgement the tool cannot make, made easy

The conference-room card is about displays and never says *screen* or *blank*.
That is a genuine prose gap and it is fixed — the Display row now opens
*Screen blank, or “No Signal” on an otherwise working display*.

The other three are the reader's **editorial** vocabulary, not the card's
subject. `exfiltrating` is an inflection of the card's own title. `weird` is the
reader's verdict on the message, and a card describing a smishing attempt has no
reason to call it weird. `useless` is the same shape.

**`useless` was tested properly and refused**, which is the counter-case that
gives the stop-word rule teeth. It blocks three queries — standups, handover,
stack trace — and looked exactly like `got` and `found`. It cannot join:
*The Risk Register in Practice — Wording, Ownership & Why Most Are Useless* is a
topic title, and stopping it would cost that card its own name. That is the
`get`/`gets` guard from the `got` note, firing for the first time.

### One real gap, named

`should i specialise or generalise` is the only content finding in the batch.
`specialise` 6 and `generalise` 8 are scattered across domains, `specialist or
generalist` returns zero, `t-shaped` returns four and none of them is `career`.
**One of the commonest questions in an IT career, and the domain has 45 topics
without it.**

```
probe 257 -> 273 · 254 answered · 0 unexplained · 18 zeros · 1 wrong · 4 wide
the per-word diagnostic corrected twice: folds like the matcher, names the binding word
and checks the wanted card — three lines that replaced four investigations
1 prose fix · 8 verdicts recorded · 1 stop-word candidate tested and refused
42 gates green · smoke 163 · search 56 · a11y 31 · resilience 64 · mobile 15
```

## Session — the condition fired, and the file did what it says

### 8,020

The previous record forecast this crossing and missed by 78 lines. This one did
not forecast anything: it appended, and `make check` said

```
plan.md is 8,020 lines. The fifth risk reopens at 8,000.
::warning::plan.md has passed 8,000 lines — the fifth risk in the register has
reopened. Read 'The fifth, which is about this file': the options are on record
and so is the reason option 1 was chosen last time.
```

**That is the whole point of the row**, and it is worth being precise about what
just happened, because this register has five risks and only one of them has ever
been tested.

The first split happened at 22,745 lines — nearly double the 11,600 that made the
risk *acute* — because somebody eventually noticed. The file wrote down why that
was a failure even though the outcome was fine: *"act when it gets bad" fails
precisely because **bad** has no threshold*, and the plan sat at double the
acute length with no session ever deciding that was the day.

This time nobody decided. The tool printed a number, the number crossed a line
somebody had set in advance, and the warning named the section to read.

### What was actually done

Option 1, the way the first split did it and for the same stated reason: **line
conserving, nothing deleted, reordered or edited.**

| | before | after |
|---|---|---|
| `plan.md` | 8,020 | **4,227** |
| `plan-archive.md` | 20,972 | **24,765** |
| total | 28,992 | **28,992** |

45 records moved, oldest first, to the end of the archive — where they land in
chronological order because both files were already chronological. 40 remain
here. The assertion ran **before** either file was written, which is the habit
the first split recorded: *the one thing that would make this a bad trade is
losing a paragraph of reasoning to a tidy-up.*

**4,227 is not a chosen number either.** The threshold was set as *double the
~4,000 the split left*, so landing near 4,000 is what keeps 8,000 meaningful for
the next firing. Keeping the last 40 records was the option that did that; 35
would have left 3,863 and 45 would have left 4,713, and both were measured before
picking.

### The row now says it was tested

A closed risk with a reopen condition that has never fired is a closed risk with
an untested condition, and this register makes that argument about the other
four. This one has fired, and been acted on, and the row records both — because
*"✅ Closed"* on a risk that reopened and closed again is a less useful sentence
than the story of the reopening.

### And the thing the first split could not have known

The first split's own record ends by noticing that the fifth risk was written up
as a success story and **left with no reopen condition** — the exact defect the
four accumulation risks above it had been given a column to prevent. The
condition was added afterwards, at 8,000, and described as *"far enough away not
to nag, close enough that the file is still comfortably splittable on the day it
fires."*

It was 68 lines away when the previous wave started and fired on the next
record. **The estimate was good**, which is not something a session can usually
say about a threshold it set for itself two hundred records earlier.

```
plan.md 8,020 -> 4,227 · archive 20,972 -> 24,765 · 28,992 lines before and after
45 records moved, 40 kept · nothing deleted, reordered or edited
the fifth risk: reopened by its own condition, acted on, and closed again
```

## Session — the card the census named, and the two fixes it took after that

### The gap was real, and writing it was a third of the work

`should i specialise or generalise` had carried a **kind 2** verdict since batch
sixteen — *named and not written, the only genuine content gap in batch sixteen* —
with the evidence already filed: `specialist or generalist` returned zero,
`t-shaped` returned four and none of them was `career`, and the domain had 45
topics without one on the commonest question in an IT career.

Verified before writing, the way step 1 of the loop says: `Growing Into Senior`
carries a concept card titled **Two Valid Ladders**, which is the
individual-contributor-or-manager axis and a different question. The four
`t-shaped` hits are `cloud`, `data`, `infra` and `web`, and every one is a JSON
shape or a traversal. Nothing covered the choice.

**`career` — Specialist or Generalist.** Five concept cards. The sentence:
*nobody gets to choose this in year one, and when the choice arrives it is much
narrower than the debate.* The two failure modes are the content —
the specialist's arrives all at once and has a date, the generalist's never
arrives at all — and the verdict is which one that makes dangerous: **the one
with no date is the one that gets left**, because a skill that stops being
bought produces a bad month and a bad month produces a plan.

The last card is the one that changes what a reader does: the shape is mostly an
**employer decision wearing a study plan**. Under ~50 people you are a
generalist by enforcement; at 500+ you are a specialist by org chart. *If you
want to be broader, change employers; if you want to be deeper, change teams* —
a curriculum is competing with forty hours a week and loses.

### Then the query was still zero, which this file has already recorded once

The previous time was verbatim: *"I wrote the USB card using enumerate,
descriptor exchange and unnamed or unknown device — and re-ran the probe, and
`usb device not recognised` **still returned zero**. The card was correct,
mechanism-first, and unreachable by the person it was written for."*

Same shape here, one word narrower. The card said `specialist` eleven times and
`specialization` twice and **never the verb**. That is an ordinary kind 1, and
the kind-1 rule is *fix in prose, it is better writing anyway* — so the opening
sentence became the reader's question rather than a paraphrase of it:

> *Should I specialize or generalize?* is asked as though it were a fork in the
> road at the start, and it is not.

`should i specialize or generalize` went from 0 to **1, the right card and
nothing else**. The British spelling stayed at 0.

### And the third fix is the one worth keeping

That residual is a clean claim, because everything else had been ruled out: same
card, same words, same matcher, one letter apart. The site is written in
American English by convention, `CONTRIBUTING.md` says so, and
`check_renames.py` enforces it — for `centre` and `datacentre`, which are the two
rows the registry has.

**Kind 1's own example is a spelling** — the site writes *imposter*, the reader
types *impostor* — and its remedy is to name both words in the card. That works
because it is one word, chosen once, in one place. It does not work here, and
the reason is the test this session added to the probe's docstring:

> could the writer have chosen the reader's word without changing anything
> else? If yes it is kind 1 and belongs in the prose. If the reader's word is
> the site's own word under a spelling **rule**, the card is not the place.

Naming both spellings in one card closes exactly one query; doing it everywhere
is the keyword stuffing kind 3 forbids, wearing an accommodation to readers as a
costume. So it went where `3-way`/`three-way` already lives: `dialectForms` in
`script.js`, beside `numberForms`, for the same stated reason — **the site and
the reader disagree and neither of them is wrong.**

### What joined, and the two families that did not

| Family | Joins | Why |
|---|---|---|
| `-ise`/`-ize`, `-isation`, `-yse`/`-yze` | **yes** | No English word means one thing with an `s` and another with a `z`. A stem that only looks like the suffix — *advise*, *exercise*, *franchise* — offers `advize`, which matches nothing: one wasted alternate, the bargain `plurals()` already makes |
| `-our`/`-or` | **no** | `four`→`for` and `tour`→`tor` are real words, so a wrong guess **widens** instead of missing, and widening is what this matcher recovers from worst. A length floor that excludes them also excludes `color` and `favor`, which are five characters |
| `-ce`/`-se` | **no** | `advice`→`advise` is a different word. A wrong card the reader never sees is worse than a miss they can retype |

Six characters is the floor, and it is what keeps `prize`/`prise` out — two
words, not one word twice, and the only pair short enough to collide.

### Proved in both directions, because a check that cannot fail is not a check

The 56 gated search fixtures were captured with the rule and again with
`dialectForms` stubbed to a no-op, and the two runs are **byte-identical** —
every count, every fixture. The rule is purely additive at the gate. Then the
two new fixtures were run against the stub: `should i specialise or generalise`
**FAIL, 0 results, NOT FOUND**, and 57/58. Restored: 58/58.

Both spellings are fixtures, and the comment says why: the American one passes
on the prose fix alone, so a rule that widened in only one direction would pass
it and look finished.

### The staleness check caught its own author again

The note written for this query two hours earlier said it returns nothing. By
then it returned 1, and the census said so by name. The note was retired rather
than reworded — the query is answered, so it keeps a `want` and no verdict.

**That is the second time this check has reported a note by the person who wrote
it, and the two outcomes are opposite**: the first time the note was right and
the check was wrong, and the guard was fixed. This time the note was simply out
of date, which is the case it exists for.

### And the row it reads through had drifted the same way

`Reader questions answered` is one of the four rows `check_plan_numbers.py`
names as **not checked here — they need a browser or a stopwatch**. Its headline
had been kept current at *254 of 273*. The three sub-counts in the same sentence
had not: they said **10 zeros, 1 wrong-card, 3 wide** while the tool was printing
**18, 1 and 4**. The last record to touch them incremented the zeros by one, from
9 to 10, on a run that reported 18.

So the row is both halves of this file's own argument in one sentence: the number
a tool checks stayed right, and the number beside it, in the same cell, drifted
eight. It is corrected here. **Making it derivable is the next wave**, and it is
tractable — `query_probe.mjs` already has every one of those numbers at the
moment it prints them.

```
1 topic added (1,556 -> 1,557) · 5 related pairs · 1 path step
probe 273 questions · 254 -> 255 answered · 0 unexplained · 17 zeros · 1 wrong · 4 wide
dialectForms joins script.js: -ise/-ize only, 6-char floor, -our/-or and -ce/-se refused
search 56 -> 58 · the 56 byte-identical with the rule stubbed out · new fixture fails without it
plan row corrected: 10/1/3 -> 17/1/4, the sub-counts of an unchecked row
42 gates green · smoke 163 · search 58 · a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```
