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

What is left here is what a session actually reads.

| Section | What it is | State |
|---|---|---|
| **The session operating manual** | The loop, the ordering constraints, and ten failures with their guards | 📘 **start here** |
| **The card rubric** | What the good cards have, measured from forty written in one session | 📘 reference |
| **Phase 11 — the verification debt** | 51 dated claims, and why the denominator is not countable. A standing discipline, not a queue | 📘 living |
| **The risk register, revisited** | Four accumulation risks that only a measurement could find | 📘 living |
| Domain shape | The connectivity graph: hubs, broadcasters, islands. Both navigation layers complete — 0 hand-written orphans, 0 hand-written topics off a path | 📘 reference |
| Session records | The last **42**. The other **242** are in `plan-archive.md`, oldest first | 📘 living |

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
| Topics | **1,549** across 30 domains | `depth_report.py` |
| Thin (one card, under 1,800 chars) | **8**, 1% — and `--thin` now prints badge, position and xref count beside each, because seven of the eight are short by design | `depth_report.py` |
| Mean chars per concept card | **1,381**, or **1,116 excluding verdicts** — the second is the padding counter-metric: it rose 1 while the first rose 1, so the growth is not all verdict | `depth_report.py` |
| Orphans | **60**, every one generated, **0 deep** | `orphan_report.py` |
| Near-duplicate pairs | **95** (41 by overlap, 54 by containment) — 78 explained by §3, 17 read and recorded, **0 unread** | `near_duplicates.py` |
| Reader questions answered | **72 of 78**, 5 zeros and 1 wrong-card miss, all 6 recorded, 0 unexplained | `query_probe.mjs` |
| Learning paths | **102 paths, 1,585 steps, 1,489 of 1,549 topics** | `check_paths.py` |
| Related links | **1,489 topics, 4,776 links, 0 one-way** — one mainland of 1,463, three reference-domain islands | `suggest_related.py --check` |
| Page budget | **35% raw** headroom — room for ~826 more topics | `page_budget.py` |
| Throttled load | **~3.0 s** = 0.5 s shell + 1.0 s script.js + ~190 ms/MB — *this container only* | `measure_load.mjs` |
| Search &amp; heap at 3x the content | **86 ms · 93 MB** at 4,602 indexed topics — search is not the constraint, load is | `measure_load.mjs --synthetic` |
| Depth tail | **10th percentile 2,117 chars**, median 3,705 — the number a deepening wave has to move | `depth_report.py` |
| Gates | **39**, and the same 39 in `make all` and in CI | `check_gates.py` |
| Gate results | check · smoke **163** · search **51** · resilience **63** · axe 31/31 · mobile 14/14 · visual 2/2 · backup 3/3 | `make all` |
| Cards ending on a table with no verdict | **12**, all deliberate lookup tables in `military` | `lint_content.py` |
| Session records | **42** here, **242** in `plan-archive.md` | `check_plan_numbers.py` |

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
where a number came from. Together they cover **46 volatile spans and 5 fact anchors: 51
dated claims** across 1,432 topics.

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
| **Console names and paths** | Vendors rename consoles every few years | `m365`, `cloud`, `endpoint` — already covered by `check_volatility.py`'s queue, now down to 2 candidates |
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
| **V5** | Re-audit console paths | `check_volatility.py` already reports this; it is 2 candidates today and will grow with each `m365` or `cloud` wave |

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
| **V5 — console paths** | `check_volatility.py`'s 2 candidates (`Teams Voice`, `Reporting & Usage Analytics`) | **False positives.** The flagged mentions are generic prose — *"wired in through the admin centre"*, *"data the admin centre has never heard of"* — not console-path claims. The real console names in those cards (`Teams admin centre`, `Entra admin centre`) already carry `volatile` spans. |

Two things this pass also settled. **This session's 46 new cards are freshness-clean by
construction** — they were written mechanism-first, per the card rubric, and introduce no
undated price, limit or version claim (`check_volatility.py` still reports 46 spans, and its
only two console candidates are the pre-existing `m365` cards above). And the phase stays
**open as a standing discipline, not a queue** — §6's V5 grows with every `m365`/`cloud` wave,
so there is nothing to mark closed. The right output of a Phase 11 pass is this table, not a
pile of edits — which is the whole argument of §3.


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
| **Unfalsifiable freshness** — the site can state what it has dated and cannot state what it has not | 51 dated claims. Three attempts to count the denominator failed on IP addresses, Wi-Fi standards and shell variables | nowhere — that is the risk | never; there is no condition to watch, which is the finding | **Accepted, not mitigable.** Phase 11 §3 |

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

| Risk | State |
|---|---|
| **The plan outgrows its own readability** — 11,600 lines, and the useful part is the last few hundred | ✅ **Closed.** Option 3 shipped, then option 1 at 22,745 lines |

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
| **Hub** — high in, moderate out | `sec` 27 in · `ops` 20 in · `script` 14 in | The site's centres of gravity. Other domains reach for them, which is correct: they are the shared vocabulary |
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

`cs` went from **one inbound reference to a See-also connection on fourteen of its centres of
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
its one-third bound; 3f+1 vs 2f+1; why blockchains need it and a trusted data centre does not),
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

## Session record — the code axis: 90 headers with no expand chevron, and the gate that ends it

With the content frontier worked out, an engineering pass over the P1–P5 backlog (all 24 items
marked applied) verified the applied fixes still hold — `DISORDER_DATA` is gone, the search is
debounced, `highlightIn` walks text nodes — and then found something the backlog never named.

**A structural audit of every `.topic-header` on the site found 90, across 15 domains, missing
their `topic-chev` span entirely** — a different defect from P1 §4 (which was `topic-chevron`
vs `topic-chev`, a *misnamed* class). These 90 are an older difficulty-badge card style
(`Beginner`/`Intermediate`/`Advanced`, badge-first, no icon) that shipped before the header
skeleton settled. The click handler is on the header, so they *did* still expand — but with no
chevron there was no visual cue that they open, and nothing for `.topic-header.open .topic-chev`
to rotate. A reader could not tell the card was expandable. The JS already tolerated the gap
(`chev?.setAttribute`, and a ternary on insertion), which is exactly why it stayed invisible.

The fix was mechanical and uniform: append `<span class="topic-chev">▶</span>` to each of the
90 headers, giving `badge · name · chev` — the chevron lands on the right (name is `flex: 1`),
the badge sits in the icon's slot, and every topic on the site now shows that it opens.

**And the gate, so it cannot return.** `check_markup.py` proves a header is *well-formed*;
nothing proved it was *complete*. `lint_content.py` now requires every `topic-header` to carry
a `topic-chev` — an **error**, because the count is now zero and this file's discipline is that
a warning graduates to an error the moment it reaches zero. The missing *icon* on those same 90
is tracked as a **warning** (`header without topic-icon: 90`), not an error: an icon is a
per-topic judgement and a wrong one is worse than a clean badge-led header, so it graduates the
day someone gives them all a real icon. The gate was proved to have teeth the way every check
in this repo must be — strip one chevron from a real domain file and lint reports
`topic-header has no <span class="topic-chev">` and exits 1; restore, and it is clean. (The
first negative test was invalid — a `_zzz`-named fixture is skipped because lint builds its file
list from `domains.json`. A validator that passes because it never looked is the failure this
file has recorded four times; the real test uses a real domain file.)

```
topics          1,519 → 1,519   (no new topics — 90 existing headers completed)
headers w/o chev    90 → 0       (now an error-level lint gate)
headers w/o icon    90 → 90      (tracked warning; graduates at zero)
index.html      +11.6 KB (90 chevron spans, post-minify)
```

Check PASS · smoke **142/142** · axe **6/6** · visual **2/2** · determinism reproducible. The
visual baseline is the filter-bar chips, which the collapsed-header change does not touch.

### And then finishing the same 90 headers — the icons, and the gate closed

The 90 headers were also the only topics on the site with no `topic-icon` — the same incomplete
older style. Having restored the chevron, the honest thing was to finish them, not leave them
half-normalised. Each got a **subject-appropriate icon**, chosen by keyword (`☸️` Kubernetes,
`🐘` PostgreSQL, `🎣` phishing, `🦠` malware analysis, `⛓️` the kill chain, `🧨` ransomware,
`🎛️` fine-tuning) with a per-domain fallback for the rest — a mapping dry-run and eyeballed
before applying, which caught two substring collisions that are worth recording: `nist` matched
*admi**nist**ration* (PostgreSQL's card), and `retrieval-augmented` matched the RAG expansion
inside the *Fine-Tuning vs Prompting vs RAG* title. Both are the same lesson as failure #5 — a
keyword is not a word boundary — and both were fixed by making the key more specific before a
single file was written.

With the count at zero, the icon check **graduated from warning to error** too, exactly as the
chevron did. So the header skeleton — icon · name · badge · chevron — is now enforced whole:
`lint_content.py` rejects a topic-header missing either the icon or the chevron, and both gates
were proved to bite on a real domain file before being trusted.

```
headers w/o icon   90 → 0   (now an error-level lint gate, alongside the chevron)
TREND line          header=90 warning retired — the skeleton is complete and enforced
```

### The one real bug the code audit found — a page that dies when storage is blocked

The markup audits (headers aside) came back clean — concept-card skeletons intact, no duplicate
topic ids, and the one table flagged for uneven row widths was a **false positive**: it uses
`rowspan`, which the audit did not model, and "fixing" it would have broken a correct table.
That is the same discipline as every probe in this file: a finding is a hypothesis until it is
read.

The genuine defect was in `script.js`. Storage access is not guaranteed — blocked cookies, a
hardened browser, or Safari private mode make `localStorage` **throw on access**, not merely
return null. Most of the file already guards it (28 `try` blocks), but the **load-time theme
IIFE did not**:

```js
(function () {
  const saved = localStorage.getItem("theme") || "dark";   // throws → unhandled
  ...
})();
```

At the top level, an unhandled throw there halts the rest of the script — so none of the event
wiring below it runs, and for a storage-blocked visitor **the entire page is inert**: no
accordions, no search, no theme toggle. This is the worst kind of bug, invisible to everyone
whose browser allows storage, which is almost everyone testing it.

The fix matches the code's own convention: a small `safeLS` {get,set,remove} helper that
swallows the throw, defined before its first (parse-time) use, with the **load-critical and
core-render/interaction** paths routed through it — the theme IIFE and toggle, the acronym-density
mode, the per-topic reviewed/bookmark/note reads in `enhanceDomain` (which run on every domain
open), the domain progress counter, and the bookmark/review toggles. The boundary is deliberate:
the optional feature handlers (export/import, quiz, stats) reach `localStorage.length` and
`.key(i)` directly, so a mechanical `getItem` swap would give false safety — the loop bound
throws first. Hardening those is a separate, per-function effort and is left as such rather than
half-done. `build.py` hashes `script.js` into the service-worker cache version, so the bump
reaches returning visitors.

```
load-time / core storage paths guarded via safeLS · smoke 142/142 (normal path unchanged)
optional-feature storage coupling documented, out of scope for this fix
```

### The test that caught the fix's own gap — `make resilience`

The right response to a bug the existing tests could not see is a test that can — the same
discipline as the lint gates above. `tools/storage_denied_test.mjs` overrides the `localStorage`
and `sessionStorage` getters to **throw on access** before any page script runs, loads the page,
and asserts the things that only work if init ran to completion: a topic expands on click, the
theme toggles, search runs, and — the sharpest assertion — **no uncaught error at load**.

It earned its place immediately. Against the `safeLS` fix above it reported **4 of 5**: the page
was interactive, but one uncaught `SecurityError` still escaped at load. The stack was swallowed
by the getter, so the site had to be found by instrumenting every access — and it was
`srsDueCount()`, which drives the study-button badge at load and loops on
`localStorage.length` / `.key(i)`. That is the exact trap the commit above called out and
deferred: `srsGet` inside the loop is guarded, but **the loop bound throws first**, before any
guard runs. One `try` around the loop, and the count is zero instead of a crash. This is why the
"out of scope" boundary was drawn honestly rather than silently — and the one place it reached
into load-critical territory, the test caught.

The test was then proved to bite the way `check_markup`'s self-test insists: reintroduce the
original unguarded theme read and it fails with `ReferenceError: Cannot access 'REVIEWED_PREFIX'
before initialization` — the top-level `const`s after the throwing IIFE never initialise, which
is the page-halt symptom in one line. Wired into the Makefile as `resilience` and into
`make all`.

```
resilience 5/5 · a new browser gate: the page survives a storage-denied browser, forever
```

### Retiring the "out of scope" — the feature handlers, hardened for real

The commit above drew an honest boundary: load and core reading were fixed, the optional feature
handlers deferred. Rather than leave that boundary as prose, the resilience test's own method was
turned on the features — open each dialog under storage denial and see which throw. Two did:
**the progress dialog** (`progressStats` loops topic ids but reads `localStorage` unguarded inside)
and **the notepad** (`npSessionId` reads `sessionStorage`, which throws in the same cases). Neither
is load-critical, but both crash the moment a storage-blocked reader clicks the button.

Both are now fixed, and the fix was generalised rather than sprinkled: `safeLS` gained a `keys()`
that returns `[]` instead of letting `localStorage.length` throw at a loop bound (the srsDueCount
trap, now also covering `bkCollect` and `bkOwnedKeys` in export/import), and a `safeSS` mirror
covers the notepad's `sessionStorage`. Every remaining feature read — quiz results, learning-path
progress, the study list, bookmark removal — was routed through the same helpers. What is left
raw is genuinely safe: each remaining call sits inside a `try`, or behind the alias-migration's
early-exit guard that returns before any unguarded access when storage is blocked.

The resilience gate grew two assertions to pin the two that broke — it opens the progress dialog
and the notepad under denial and requires both to mount without throwing. So the storage-blocked
story is now whole and enforced end to end: load, reading, and every feature, none of them able to
regress silently.

```
progress dialog + notepad: THREW → open cleanly · safeLS.keys() + safeSS added
resilience 7/7 · every raw storage access is now guarded or provably unreachable when blocked
```

### The big one the minifier audit uncovered — hundreds of code blocks rendering collapsed

Reviewing `build.py`'s minifier (does stripping indentation corrupt anything?) turned up something
much larger than a minifier bug — the minifier is correct. A `<pre>` has `white-space: pre` by
default and is protected verbatim; a `<div>` has `white-space: normal` and **collapses its
newlines**. And the site had **422 `<div class="code-block">`** against 381 `<pre class="code-block">`
— the same class on two different tags, one of which throws the layout away.

The proof was stark: `script.03-python.html` used **97 `<div>` code-blocks and zero `<pre>`**. An
eighteen-line Python example — with syntactic four- and eight-space indentation — was rendering as
six wrapped lines of run-on text, its structure destroyed. A YAML reference with column-aligned
keys, box-drawing dividers and nested mappings was a single collapsed smear. This had shipped
because it is invisible to anyone reading the source and only wrong in the browser.

The fix is a tag swap, but not a blind one — the distinction that matters is whether a block's line
breaks are **semantic** (code, commands, diagrams) or **cosmetic** (prose wrapped to the file
width). The tell is indentation: content authored as code sits **flush-left** in the data file
(its only indentation is its own, real, structure); content authored as flowing prose is
**file-indented**, nested under the div because the author knew it would collapse. So the safe,
correct set is the flush-left multi-line blocks — **318 of them** — converted verbatim to
`<pre class="code-block">` (flush-left means the swap needs no dedent, and a `<pre>` drops one
leading newline, so nothing shifts). Every sampled one was genuine code: `kubectl get nodes`
command references, `systemctl` blocks, the Python examples, the YAML card. None was prose.

Verified by rendering, not assertion: the Python `dataclass` block went from **6 collapsed lines
to 24 real ones**, `white-space` from `normal` to `pre`. Markup stayed balanced (the swap changes
both tags together), determinism held, and every browser gate passed.

**The second pass — the 105 file-indented ones — went further than the first note expected.** The
worry was flowing-prose callouts that would render worse as `<pre>`; reading them, there were
none. Even the most prose-like by line length were code with **column-aligned inline comments**
(`rsync -a /src/data/ /dest/     # copies its CONTENTS`, a big-endian/little-endian table with
aligned `=` columns) — alignment that is *only* meaningful preformatted and is destroyed by
collapse. The TCP handshake that prompted the caution turned out to *want* `<pre>` too: its
decorative `──────` underline is meaningless except in a monospace block, which is the author
telling you the intended layout. So all 104 multi-line file-indented blocks were converted, each
**dedented by its own common indent** first (they are nested under the div, so a verbatim swap
would have shown the file-nesting as real indentation) — the byte-order table came out with its
columns intact. **Every `<div class="code-block">` on the site is now a `<pre>`.**

```
div.code-block 422 → 0 · pre.code-block 381 → 803 · the class now lives on one tag, the right one
python reference & every command/config/diagram: collapsed → real code · check PASS · gates green
```

And a gate, because the count is zero and this file's discipline is that a zero graduates: `lint_content.py`
now rejects `<div … class="code-block">` outright. It earned its keep on the first run — it caught **one
last block the conversion had missed**, a `<div class="code-block" style="margin-bottom: 14px">` whose
extra attribute slipped past the exact-match rewrite. The gate's pattern is attribute-tolerant where the
rewrite was not, which is exactly the asymmetry you want: convert conservatively, forbid broadly.

### The phone was scrolling sideways — wide tables pushing the whole page

The desktop gates are green because the desktop gates are all there are: `visual_test.mjs` screenshots the
filter bar, and nothing renders the page at a phone's width. Doing so found a real defect nobody had
measured. At **375px**, the `script` domain's body was **127px wider than the viewport** and `net`'s 43px —
the page scrolled sideways, the jarring kind where the text drifts under your thumb. The cause was tables:
an `ai-table` has a `white-space: nowrap` first column of labels and lives in no scroll container, so a
five-column table simply overran the screen and dragged the page with it. `<pre>` code blocks did **not** do
this — they already carry `overflow-x: auto`, so the same phone that overflowed on `script` was clean on
`linux` and `cs`, which is what ruled the fresh conversion out as the cause.

The fix is the standard responsive-table one, and it is CSS-only — no wrapper div, no build change. Under
`@media (max-width: 640px)`, `.ai-table` / `.ref-table` become `display: block; overflow-x: auto`. A
block-level table still has table-row and table-cell descendants, so the browser wraps them in an anonymous
table box — the columns stay aligned (verified: two cells in a column share a left edge to the pixel) while
the block itself scrolls. It is scoped to phones because the tables fit natively from ~700px up (measured 0
overflow at 768, 900, 1024), so desktop layout is untouched and the visual baseline never moves.

```
375px page overflow: script 127px → 0 · net 43px → 0 · every domain 0 · columns stay aligned
scoped to ≤640px (fits unaided at 768px+) · desktop untouched · gates green
```

And the coverage gap that let it hide is now closed: `tools/mobile_test.mjs` (`make mobile`) renders at
375px, opens a spread of table-heavy domains, expands every topic and asserts the document is no wider than
the viewport — naming the widest uncontained element on a failure. Proved to bite: with the CSS rule removed
it fails `script` (127px), `net` (43px) and `sec` (62px), each pointing at `TABLE.ref-table`; with it, 9/9
domains fit. Wired into `make all`.

### The worst bug of the session: restoring a backup destroyed the data it restored

A round-trip check — seed progress, export, wipe, import, compare — turned up a **silent data-loss bug** in
the backup feature, the one feature whose entire job is not to lose data. `bkCollect` exports the JSON-valued
keys (the SRS schedules, the notepad, the streak) **parsed into objects**, deliberately, so the downloaded
file reads as nested JSON rather than a wall of escaped quotes. `localStorage` holds only strings, so the
import has to re-serialise them — and it did not. `bkApply` wrote the object straight to
`localStorage.setItem`, which stringifies it to the literal **`"[object Object]"`**. So importing your own
backup overwrote every spaced-repetition schedule, every note and your streak with that string. The data
most expensive to rebuild, erased by the act meant to protect it. `bkDiff`'s preview was wrong for the same
reason — it compared a stored string against an exported object and reported every JSON key as an overwrite.

The fix is a symmetric pair, `bkStored` (→ the string storage holds) and `bkObj` (→ the object a merge
compares), each tolerant of a value already in the other form, applied at the three sites that had assumed a
value was one or the other. And a regression test that would have caught it at birth: `tools/backup_test.mjs`
(`make backup`) round-trips one of every key kind and asserts each returns byte for byte, checks the export
is still a readable object file, and checks merge keeps the later SRS due date. It bites — revert the
`setItem` fix and it fails with `study-streak: "[object Object]" != {…}` — and it is in `make all`.

```
backup import: SRS + notepad + streak → "[object Object]"  →  restored byte-for-byte
make all now runs seven browser/gate suites; the two written today guard a phone and a backup
```

### Content — the enterprise-Microsoft depth pass (MECM / Intune / Azure / Exchange)

A requested deep pass on enterprise Microsoft management. The audit found the estate already
deep — endpoint carries MECM (distribution points, boundary groups, task sequences, SUP), Intune,
Autopilot and co-management; m365 the full Exchange/Teams/Purview surface; infra AD/GPO/AD CS;
cloud the Azure hierarchy, networking, Monitor and Sentinel. So the method was the usual one:
probe the durable subjects, verify each apparent gap against the *content*, keep only the zeros.

The genuine zeros clustered in hybrid and cloud-side management, not the on-prem estate:

- **Azure Arc** (`cloud`) — the control-plane extension that projects an on-prem or other-cloud
  server into Resource Manager so Policy, RBAC, Defender, Monitor and Update Manager reach it
  without moving the workload. The card's spine is the honest boundary: Arc governs the machine,
  it does not migrate, network or SLA it, and a *Disconnected* agent is an unmonitored machine, not
  a compliant one. Its decision line is &ldquo;will this box still be off-Azure in two years&rdquo;.
- **Azure Automation &amp; Update Manager** (`cloud`) — runbooks (managed identity, never a stored
  password; Hybrid Runbook Worker for on-prem reach) and agentless server patching whose reach
  through Arc covers cloud and data-centre servers on one schedule. Its decision table sorts the
  patch tools by estate — Autopatch for Intune clients, Update Manager for servers, MECM SUP for the
  ConfigMgr estate — and the automation tools by job — runbook vs Function vs Logic App.

Both are `cloud` cards, linked bidirectionally to each other and to the Azure hierarchy, Defender
and Monitor cards they extend. Check PASS · smoke 142/142 · axe 6/6 · mobile 9/9 · visual 2/2 ·
1,286 links, 0 one-way. Site 1,519 → 1,521.

The second wave took the remaining verified zeros across Intune, identity and Exchange — four
cards, each turning on a real operational truth rather than a feature list:

- **Endpoint Analytics &amp; Proactive Remediations** (`endpoint`) — measure the fleet on what users
  feel (startup, app reliability) and self-heal with a detection/remediation script pair, with the
  discipline that a fix every device needs is an image or policy bug, not a remediation.
- **Windows 365 &amp; Azure Virtual Desktop** (`endpoint`) — the two cloud-desktop models named and
  priced: Cloud PC as a fixed-price per-user SKU you assign, AVD as pooled infrastructure you
  operate — and the reminder that either is still a full endpoint to manage, not one fewer.
- **Entra ID Protection** (`cloud`) — Conditional Access that branches on *risk*, with the elegance
  of self-remediation (MFA clears sign-in risk, a password change clears user risk) and the
  non-negotiable excluded break-glass account.
- **Exchange Server On-Prem** (`m365`) — the &ldquo;last Exchange server&rdquo; you keep for
  recipient management when AD is authoritative, the DAG and transport pipeline, and the security
  edge that an unpatched on-prem Exchange is a perennial internet target.

The audit's headline holds: the enterprise-Microsoft estate was already deep, and the genuine gaps
were not in the on-prem tooling everyone documents but at the **hybrid and cloud-management seam** —
Arc, Update Manager, cloud desktops, risk-based identity, and the on-prem shim a cloud migration
cannot quite delete. Six cards, all verified against content first, none manufactured. Site
1,519 → 1,525 · 1,304 links, 0 one-way · every gate green.

A follow-on broad probe of the professional territory next door — SASE, SCIM, passkeys, SOAR,
UEBA, vector databases, OpenTelemetry, GitOps, service mesh, SBOM, WAF, chaos engineering, SLOs —
came back **covered on every one**, which is the saturation signal again. The lone verified zero
was **data mesh** (`data`): the storage question was answered (warehouse / lake / lakehouse) but
not the *ownership* one. The card is written around its honest critique — data mesh is an org
restructure sold as an architecture, it pays off only where a central data team is a provable
bottleneck and domains can carry ownership, and most teams need a lakehouse and data-product
discipline, not a mesh. Site 1,525 → 1,526. With that, the deliberate content pass is again at
its floor: seven genuine cards across this session, and the next probe finds none — the long tail
is the scheduled Routine's.

---

## Session — the toggle buttons that never said they were on

The last accessibility pass closed this one out as *"a genuine gap, but it
belongs with a wider pass over per-topic state; note it in plan.md rather than
half-doing it."* This is that pass.

The star and the tick in every topic header are toggles. Their state lived
entirely as a class on the parent `.topic` — `bookmarked`, `reviewed` — which
paints CSS and nothing else. A screen reader announced *"Save topic to study
list, button"* whether the topic was already saved or not, and pressing it
produced nothing audible at all. The state existed purely as a colour. axe
cannot see this: a button with no `aria-pressed` is a perfectly valid button.

### Why the fix is a helper and not five `setAttribute` calls

Five places move these flags, and only two are anywhere near the button:

```
639,660  hydration, restoring from localStorage
1367     the tool handler — star
1377     the tool handler — tick
3536     the exam's "star everything I missed"
4134     removing an entry from the study list
```

A fix applied where the button lives would have left the last two stale, and
the button would go on claiming pressed after the star had gone. So the class
stays the single source of truth and `syncTopicFlag(topic, flag)` mirrors it
onto the button; every site that moves a class calls it after. The sync in the
hydration pass sits **outside** the creation guard on purpose — a section can be
hydrated again after its flags have moved.

Both toggles also now announce, because `aria-pressed` states the new value and
does not say a press landed: *"Saved to study list"*, *"Marked as reviewed"*, and
their inverses.

### What was deliberately left alone

The note button is not a toggle. `toggleTopicNote` only ever opens, and the panel
is removed when the note is emptied — so `aria-expanded` there would go `true`
and never come back, which is worse than absent. It is an action button that
reveals an editor, and it is already correctly labelled as one.

### The revert test

Five new assertions, each checked against a faithful revert of `script.js`
rather than only against the fix:

```
FAIL : the star button carries its own pressed state    aria-pressed went null -> null -> null
FAIL : starring a topic says so                         announcer said ""
FAIL : the tick button carries its own pressed state    aria-pressed went null -> null -> null
FAIL : marking a topic reviewed says so                 announcer said ""
FAIL : un-starring from the study list clears the button too   aria-pressed was null after removal
```

The last one is the one worth having. It drives the study list, not the header
button, so it fails for a fix that only covers the obvious call site — and it
returned a value rather than throwing on the pre-fix code, which is how I know
the probe actually reached the removal path instead of erroring somewhere
harmless.

```
a11y suite 24 -> 29 checks · browser 296 -> 301 · 31 gates green
```

## Session — closing "unreachable quality", the third open accumulation risk

The risk register's four measured risks, re-measured today rather than assumed:

| Risk | Recorded state | Measured today |
|---|---|---|
| Silent style drift | 330 topics (23%) thin | **11 of 1,542 (1%)**, and those eleven were already judged deliberate |
| Blind duplication | 36 title pairs ≥50% overlap | **92 near-duplicate pairs, 0 disagreements** |
| Unreachable quality | 902 unlinked, **159 of them deep** | 68 unlinked, **8 deep** — and all eight were mine |
| Unfalsifiable freshness | accepted, not mitigable | unchanged |

The first two closed themselves through later work. The third had not, and its
entire remaining population was the eight topics written yesterday. I fixed the
*paths* half of reachability and left the *links* half — the same "half a job"
I had named in that very commit message.

### Two mechanisms, both needed

An inline `<span class="xref">` is a writer saying these two belong together, and
it earns its place only if the sentence around it was worth writing anyway. All
eight had an obvious home, because each topic exists precisely where an older one
named the thing and stopped:

```
certificate delivery ← "the certificate row is the one that fails silently"
GPO to Intune        ← "the leftovers are the project"
Azure-native IaC     ← "Bicep is worth knowing — a clean DSL"
scope tags           ← "RBAC roles + scope tags (limit which admins see what)"
the Intune Suite     ← the EPM verdict, EPM being one component of it
PaaS compute         ← the SKU table's three PaaS rows
Azure databases      ← the storage card, drawing the storage/database line
workload identity    ← the RBAC verdict, which governs people only
```

`related.json` is the other half — the "See also" strip — and 1,474 of 1,542
topics had one, so the eight were the exception rather than a design choice.

### Two things the file taught me by being edited badly

**It is not sorted.** My first write used `sorted()` and moved several thousand
entries; the diff was 7,610 lines for eight additions. Key order is the file's
own, and preserving it makes the same change a 110-line diff.

**Every edge is reciprocal.** The baseline is *0 one-way links across 4,612* —
an invariant nothing states in prose and no gate enforces, visible only because
`--check` reports the count. Eight one-directional entries would have introduced
32 one-way edges and nothing would have failed. Each new link is now added in
both directions; 36 entries touched, still 0 one-way.

The suggester was almost no help here and says so in its own docstring: ranked by
term overlap it offered *DORA Metrics* and *USB-C Power Delivery* for a topic
about certificate delivery, and internet-scale port scanning for one about
porting Group Policy. One genuine hit in twelve. Curation by hand was the job.

```
deep dead ends 8 -> 0 · related.json 1,474 -> 1,482 entries · 4,612 -> 4,678 links
31 gates green · 301 browser checks green
```

## Session — the sequel to the div → pre fix, which nobody had measured

Taking this file's own advice — *once a phase, measure something nobody has
measured* — I extracted all 805 `<pre class="code-block">` bodies and tried to
compile the Python ones. 110 of 132 compiled. The 22 that did not were mostly my
crude language guess catching Go, JavaScript and a pdb session, but five were
real, and reading them found something larger.

### What broke, and why the previous fix caused it

Commit `a968164` converted 318 `<div class="code-block">` to `<pre>`, correctly:
a `div` collapses newlines, so those blocks rendered as one run-on line. But a
`<pre>` *renders* its newlines — which means the conversion made the source
newlines meaningful for the first time. They had never been meaningful before, so
nothing had ever put them in the right places. In 21 blocks they sat
mid-statement, and the language quick-reference — the part of a study site people
copy from — rendered like this:

```
name =
"Alice"
active =
True
# bool (capital T/F)
print(f"Hello {name}, age
  {age}") print(f"PI = {pi:.2f}") # format spec
```

`[int]$n =` / `10 [string]$s =` in PowerShell; `func main()` with its whole body
flush left in Go; a `match`/`case` statement with every token on its own line.

### Two hypotheses discarded before the right one

**Fixed-width wrapping** — the obvious cause. Wrong: source lines inside blocks
run to 477 characters, so nothing wrapped them at a column.

**A generic "suspect line ending" heuristic** — 635 hits across 25 files, and
almost all false. `client.messages.create(` followed by `model=...,` is correct
multi-line Python; wrapped comments end in `or` and `and` legitimately. A number
that large was evidence the detector was wrong, not that the corpus was.

The decidable test is narrower and holds: **Python has no line continuation at a
bare `=`**, so a Python line ending in one cannot be what anyone wrote. That
returned 18 hits, all in one file, all real.

### The repair, and the invariant that made it safe

Every block was rewritten by hand — indentation restored, statements separated,
trailing comments put back on their lines. What made that safe rather than risky
is a property checked on each one before it was applied:

```python
re.sub(r'\s+', '', old_html) == re.sub(r'\s+', '', new_html)
```

Strip all whitespace and the markup must be *identical*. That permits exactly the
edit intended — moving newlines and adding indentation — and forbids everything
else, including a dropped span or a silently reworded comment. It caught two
mistakes: an `&&` I had escaped to `&amp;&amp;`, and a verification bug of my own
where `<[^>]+>` ate `< <span` in `n < 2` and made a correct block look broken.

Two `net.html` blocks had the same corruption in reference text rather than code
— a subnet calculation and a VLAN plan run together into paragraphs. Reflowed the
same way, one fact per line.

`linux.html:3978` is left alone deliberately: `smtpd_relay_restrictions =`
followed by an indented value is correct Postfix syntax, which is exactly why the
gate is restricted to blocks that are unmistakably Python.

### The gate

`lint_content.py` already bans `<div class="code-block">`. The new check sits
directly beneath it, because it is the same defect one step later, and carries
seven fixtures: the corruption, the corrected form, the Postfix case a looser
rule would have failed the build over, `==`, `+=`, a comment, and a block with
two offences to prove it reports all of them.

Proved against a faithful revert of the file, not only against the fix:

```
ERRORS (18):
  script.01-references.html:1002: a Python line in a code block ends in a bare '=' ('name =') …
```

```
21 blocks reflowed in script.01-references.html + 2 in net.html
lint fixtures 9 -> 16 · 31 gates green · 301 browser checks green
```

## Session — the same corruption, in the languages the first test could not see

The Python check that found 18 broken lines could only see Python. Blocks in
shell, Splunk and Go were damaged the same way and passed it silently. Two more
decidable signals found them.

**Broken string literals.** A code line with an odd number of double quotes has
opened a string it never closed. 51 hits — and most were *legitimate*: quoted
dialogue in scenario blocks, a triple-quoted SQL string my counter read as three
quotes, a regex character class `[^\s"'<>]+`, a tmux `unbind '"'`. Three were
real, and the same defect:

```
sh -c
"$(curl -fsSL
  https://raw.githubusercontent.com/.../install.sh)"
```

**Wrapped comments.** The stronger signal, and the one that generalises: a
comment span may hold several lines, but each carries its own `#`. A continuation
*without* a marker is the source's wrap showing through, and it renders as a line
that reads like code and is not. 42 hits in 18 blocks across five files.

My first version of that check counted 146 and was wrong: `ai.html` writes real
multi-line commentary where every line has a `#`. Requiring the marker on the
continuation is what makes the signal decisive.

### Where automation stopped being safe

Joining wrapped comments is mechanical, so I automated it under the same
whitespace invariant, and it was right 38 times out of 39. The one it got wrong:

```
# Connection established
  ──────────────────────────────
```

A horizontal rule, not a wrapped sentence. Joining it is defensible and reads
fine, so it stayed joined — but the block it sits in needed hand work anyway, and
that is the point. The auto-join found the block; it could not fix it:

```
Client → Server SYN seq=100 Server        Client → Server   SYN       seq=100
→ Client SYN-ACK seq=200, ack=101    →    Server → Client   SYN-ACK   seq=200, ack=101
Client → Server ACK seq=101,              Client → Server   ACK       seq=101, ack=201
ack=201
```

The eight TCP flags had run into one paragraph the same way. Reviewing all twelve
blocks the automation touched, rendered before against rendered after, is what
turned "the invariant held" into "and every change is an improvement" — those are
different claims and only the second one matters to a reader.

### The second gate

Beside the first, with six fixtures: the corruption, the joined form, a real
multi-line comment in `#` and `//`, an indented marker, and a block with two
offences. Nested comment spans are skipped rather than guessed at — `grc.html`
opens a few one inside another, which renders correctly because the class is the
same, and unpicking them is churn with no reader on the other end.

Proved against a faithful revert of four files: 30 findings, exit 1.

```
39 comments joined + 6 code blocks reflowed by hand · 5 files
lint fixtures 16 -> 22 · 31 gates green · 301 browser checks green
```

## Session — the symmetry test, run backwards

The Azure waves used a test that worked twice: build the provider × service-area
matrix from topic titles, then check it at content level. Now that Azure is
complete, the same test run in the other direction has something to say.

Fifteen areas across three providers. Fourteen rows are complete. One is not:

```
                        AWS   GCP   Azure
  getting started        ✓     ✓      ✓
  IAM / workload id      ✓✓    ✓✓     ✓✓
  networking, LB & DNS   ✓     ✓      ✓
  compute, serverless    ✓✓    ✓✓     ✓✓
  storage, databases     ✓✓    ✓✓     ✓✓
  security, secrets      ✓✓    ✓✓     ✓✓
  native IaC             ✓     ✓      ✓
  observability          ✓     ✓      ✓
  troubleshooting        ✗     ✗      ✓
```

The corpus holds eleven troubleshooting playbooks — network, hardware, GPO,
MECM, virtualisation, M365, Azure — so this is not a case of the form being
unusual. Two of three providers simply never got one.

### Written as counterparts, not copies

The three-card shape is shared (method, toolkit, error reference) because the
reader benefits from the shape being the same. What goes in it is not, because
the platforms fail differently, and that is the whole content of the topics.

**AWS** puts *"am I in the account and region I think I am"* first, because the
credential chain resolves in an order few people can recite and every later step
is wasted if the identity is wrong. Its policy question is the hard one — a deny
in any of five policy types wins — so the verdict argues for the simulator over
reading five documents by eye. The error table carries the S3 404-where-you-
expected-403 (no `ListBucket`, so S3 will not confirm the object exists) and the
NACL asymmetry that lets a request out and blocks the reply. It closes on service
control policies: something that worked yesterday, broken by a grant made above
the account, leaving no trace in the account's own IAM.

**GCP** inverts the order, because two things are off by default that engineers
assume are on: the API, and billing. Both produce errors that read like
permission problems, so the natural response — widen a role — does not help and
leaves a broader grant behind. Hence its verdict: *a permission error on this
platform is a hypothesis, not a diagnosis*. Three causes wear the same denial and
only one is fixed by granting anything.

### Reachability, this time in the same commit

The last wave's lesson applied without being re-learned: both topics went into
their provider's end-to-end path (ending on the playbook, exactly as *Running
Azure* does) and into `related.json` in both directions, before the wave was
committed rather than a day later.

```
cloud 78 -> 80 topics · 1,542 -> 1,544 · paths 1,579 -> 1,581 steps
related 4,678 -> 4,696 links, still 0 one-way · deep dead ends: 0
31 gates green · 301 browser checks green
```

### A third heuristic that did not converge, recorded rather than pursued

Looking for code-block damage in languages the two decidable signals cannot see,
I tried "a continuation line indented by exactly two spaces where the block uses
no other two-space indentation". 343 hits, and the first ten were all legitimate
— pretty-printed JSON, a Suricata rule with a backslash continuation. Two
heuristics have now failed the same way (635 hits, then 343), and both failed by
being *plausible*. The rule that keeps working is narrower: only signals a
language's grammar makes impossible are worth acting on.

## Session — three measurements that came back clean, and one that did not

Following this file's own habit, four things nobody had measured. Three returned
nothing, which is worth recording as carefully as a finding:

**Table row widths.** A `<tr>` whose cell count differs from its header renders
short or overflowing — decidable, no judgement. 14 hits, and after honouring
`colspan` and `rowspan`, **zero**. The tables are correct; the checker was naive.
A section divider using `colspan` and a four-row `rowspan` in the SQL-injection
table produced every false positive.

**Path reachability by depth.** 59 topics are in no learning path, and **none of
them is deep** — no 3-card, 3,000-character topic is unreachable from a path.

**Prose that defers.** Searching for the phrasings that admit a gap — *"beyond
the scope"*, *"deserves its own"*, *"a topic in itself"* — returned 13 hits, of
which twelve were rhetorical (*"row two deserves its own emphasis"*). One was
real.

### The one that was real

`infra`'s DR topic ends a verdict with:

> **Failback is the forgotten half.** Runbooks lovingly document the failover and
> stop there; getting production back to primary afterward, without losing the
> data written while you ran on the DR site, is its own procedure — write it
> before you need it.

Counted across the corpus: `failover` appears 65 times in 11 files. `failback`
appears **once** — in that sentence. The site says the word for the only time in
order to say it is not covering it.

One card, placed directly after the verdict that defers it rather than at the end
of the topic, because that verdict is now a promise the next card keeps. The
inversion is that failback moves data in the *harder* direction: the DR site
holds the newest copy and primary holds the stale one, which is why failback and
not failover is where work is usually lost. Then what changed while you were on
DR and why each thing bites on the way home — data written since cutover,
replication still pointing the wrong way, a primary nobody re-verified, TTLs,
hardware-bound licences, and the accounts and certificates created only on DR.

The verdict gives a test rather than a procedure: **a DR plan that states an RTO
for failover and none for failback has never been exercised end to end.** The
second number decides whether you go back this weekend or run on DR for a month,
and a plan without it makes that call at two in the morning, in favour of whoever
is loudest.

```
infra: the DR topic 3 -> 4 cards · 31 gates green · 301 browser checks green
```

### On measurements that return nothing

Three clean results in one session is not wasted effort, and recording them
matters more than it looks: the next person to wonder whether the tables are
malformed now has an answer and the reason the obvious check misleads. The cost
of re-deriving a negative is the same as deriving it the first time.

## Session — the freshness stamp I forgot, and what running the tool revealed

The failback card went into a topic stamped `2026-08` and I did not re-stamp it.
`data-reviewed` is derived from git history rather than remembered, so the fix is
to run `stamp_freshness.py` — and doing that turned a small omission into a
finding about the tool.

`--check` over the whole tree proposed updating **all 34 files**, which is the
hazard its own docstring names. So `--only infra`, as the docstring advises. That
moved **twelve** topics from `2026-08` to `2026-09`:

```
Windows Server Editions & Licensing        Storage Fundamentals
Server Manager, RSAT                       RAID
AD                                         Storage Performance — IOPS
Hyper-V, vSphere & the Open-Source Stack   Thin Provisioning, Dedup & Tiering
Snapshots Are Not Backups                  P2V & V2V
Backup Strategy — 3-2-1-1-0
Restore Testing & DR Design   ← the only one I touched
```

The commit that prompted the stamp was `32 insertions, 0 deletions` — one card,
in one topic. Eleven of those twelve moves have no edit behind them.

**So `--only` narrows the blast radius to a file and does not eliminate it.** The
docstring warns that a whole-tree write invents freshness across the site; this is
the same failure at file scope, and it is worth writing down because the advice
"prefer `--only`" reads as though it solves the problem rather than shrinking it.
Ten commits in that file's history are classified mechanical and ignored, so the
blame that remains is real-commit blame, and a real commit that adds lines is
enough to pull neighbouring topics forward.

The stamp was therefore set by hand, on the one topic whose content changed:

```
data/infra.html | 2 +-
1484 topics carry a valid freshness stamp (newest allowed: 2026-09)
```

A one-line diff instead of a twelve-line one, and eleven topics keep the date of
the month somebody actually reviewed them. The rule this leaves behind: **run the
stamper to find out what it would say, then write the stamp you can defend.** Its
output is a proposal, not an answer — which is exactly how the tool's author
already treats the whole-tree mode, and now also how the single-file mode should
be treated.

## Session — the one failure whose guard column said "nothing catches this"

The session operating manual lists ten failures and a guard for each. Nine name
a tool. Failure #10 does not:

> Two wrong acronym expansions shipped in earlier sessions and were found by
> **reading**, not by any check — `IR` in a compiler card's title, `SMB` in "a
> home-lab / SMB choice". *The breadth census now surfaces the candidates. It
> cannot decide them.*

A dictionary of 1,101 acronyms and 1,172 meanings, and nothing had ever checked
that an expansion is an expansion of the acronym beside it.

### Two detectors that were wrong before one was right

**Matching initials.** The obvious rule: the capital letters of the expansion
should spell the acronym. It fires on **247 of 1,172 meanings — 21%** — and
reading the first fifty, essentially all are legitimate. `Antivirus` yields AV
from inside one word; `Demilitarized Zone` yields DMZ the same way. This is the
third heuristic in this repository to fail by being *plausible*, after the 635
"line ends mid-statement" hits and the 343 two-space continuations.

**A number-word substitution of my own.** The second attempt mapped spelled
cardinals to digits so `B2B` would read. I included `one` and `second`, which
broke `OTP` (*One-Time Password* → "1timepassword") and `QPS` (*Queries Per
Second* → "queriesper2"). Four of the 39 findings were my detector, not the
data. The substitution list is now short, documented, and deliberately excludes
ordinals — because `EXT4` is a version suffix rather than a spelled-out
"fourth", and letting the reading swallow that would hide the distinction.

**The rule that holds** is not about initials at all:

> the acronym's letters must appear, **in order**, somewhere in its expansion

An acronym is by construction a compression of a phrase. If its letters are not
even a subsequence of that phrase's letters, the pairing cannot be a compression
of it. That is a property of the words rather than a guess about house style,
and it fires on **28 meanings — 2.4%**, a list short enough to read.

### The dictionary already had the mechanism, applied to five entries

Of the 28, nineteen carried a note. Five of those notes explain the letters:

```
K8s   "Numeronym: K, eight letters, s"
UTC   "The letters match neither the English nor the French word order, by agreement"
```

The other fourteen are descriptive — `EC2` says "AWS virtual machines", which is
true and answers a different question. So the convention existed and had been
applied to five entries out of twenty-eight, which is the shape of every
accumulation risk this file has found: a good habit, never collected.

### Why a new field and not the note

A gate that accepts any note teaches people to write any note. `check_volatility.py`
names that failure in its own docstring — *"a gate would only teach people to add
a span they do not mean"* — and it is the reason its console list reports and
never fails. So the requirement is a dedicated `l` field: the only thing it can
say is how the letters are formed, and a vacuous one is visible as such.

It earns its place by being **content, not metadata**. `gen_acronym_domain.py`
renders it in the dictionary beside the expansion, so the reader who stopped to
wonder why accessibility is spelled with an 11 in it gets an answer:

```
a11y   Accessibility
       Letters: Numeronym: a, eleven letters, y
```

Twenty-seven meanings now carry one, on both the A–Z and the by-subject topics.

### The one that was a real error

**`NBT-NS` — "NetBIOS Name Service".** NBT is *NetBIOS over TCP/IP*, RFC 1001
and 1002. Dropping "over TCP/IP" leaves the **T with no source**, which is
exactly what the check reports and why the check is a subsequence test rather
than a spellcheck. Corrected to *NetBIOS over TCP/IP Name Service*, which
propagated to the one card that uses it, in `redteam`.

Three others were read and kept, and the reading is the deliverable:

- **`ADMX` — "Administrative Template".** The X is the file's XML format, and
  Microsoft's own documentation expands it exactly this way. Inventing "XML" as
  a fourth word would be *less* accurate than the gap. Recorded, not fixed.
- **`CCM` — "Configuration Manager Client".** The letters run C-C-M from the
  SMS-era *Client Configuration Manager*; the product now says "the Configuration
  Manager client". The expansion is the modern order and stays.
- **`MSIX`.** Not an initialism at all — MSI, the installer it succeeds, plus X.

### The check runs in both directions

An `l` on a meaning that *derives cleanly* is also an error. That is the failure
mode a file like this actually has: the expansion gets corrected and the
explanation of the old one is left behind, still rendering to readers, now
false. Injecting one on `SSH` exits 1 and names it.

Proved against the pre-fix dictionary rather than only against fixtures:

```
pre-fix dictionary          → exit=1, 28 unexplained
stale-explanation injection → exit=1, "SSH: 'Secure Shell' derives cleanly"
current dictionary          → exit=0
```

Twelve fixtures, and the true ones matter more than the false ones — `AV`,
`DMZ`, `OTP`, `QPS` are the shapes an initials-matching check would have failed,
and they are in the suite so nobody re-derives that rule.

### A second measurement, which came back clean

The site's own *Common Ports — Protocol Reference* table makes port claims
internally decidable: it is the authority, and every other mention in 35 files
can be checked against it without an external list. Built the service → port map
from the table and scanned the corpus for five claim shapes — `NAME (N)`,
`NAME … port N`, `NAME on N`, `NAME/N`, `port N (NAME)`.

**Two hits, both false positives**, and both the same shape: two adjacent
`tcpdump` commands read as one claim. No port anywhere on the site contradicts
the site's own table. Recorded because the cost of re-deriving a negative is the
same as deriving it the first time — and because the next person to wonder now
knows the table is the authority and that the authority holds.

```
acronyms.json: 27 meanings explain their letters · 1 expansion corrected
gates 31 -> 33 · check_acronyms fixtures 12 + both directions
301 browser checks green
```

## Session — the table that said its numbers came from tools, and did not

The headline table at the top of this file opens by claiming something about
itself:

> **The measured state, as of the last session record.** Every number below is
> produced by a tool in `tools/`, not by anybody's recollection.

It was, once. After that it was maintained by hand. Re-derived all fifteen rows:
**nine of the eleven derivable ones were wrong.**

| Row | The table said | The tools say |
|---|---|---|
| Topics | 1,534 | **1,544** |
| Thin | 13 | **11** |
| Mean chars per card | 1,369 / 1,109 | **1,377 / 1,113** |
| Depth tail | p10 2,090, median 3,658 | **2,097 / 3,690** |
| Near-duplicate pairs | 92 (38 overlap) | **95 (41 overlap)** |
| Learning paths | 1,570 steps, 1,474 of 1,534 | **1,581 steps, 1,484 of 1,544** |
| Related links | 1,472 topics, 4,592 links | **1,484 / 4,696** |
| **Page budget** | **4% raw — room for ~66 more topics** | **35% — room for ~840** |
| Gates | 30 | **33** |

Most of those are a wave or two of drift and cost a reader nothing. One is not.

### The row that mattered

*Page budget: 4% raw headroom — room for ~66 more topics.*

The budget was raised in *"the budget was raised, and the number is not the one
on offer"*, two dozen records above, and this row never moved. So the file's
headline constraint **understated its own headroom by a factor of twelve** —
66 topics against 840. A reader deciding whether there was room to keep writing
would have concluded there was not, and the whole "where new work comes from
now" paragraph sits directly beneath it.

That is the same defect this repository has now shipped three times, and every
time in something that **reports rather than gates**:

- the social card telling everyone the site had 1,519 topics when it had 1,534;
- four generated artefacts checked only on the server, three of them stale;
- and now the plan's own census, in the paragraph that says it is not.

The pattern is not carelessness. It is that a number with no check on it has a
half-life, and prose is where numbers go to be unchecked.

### What the gate does, and the two rows it will not touch

`check_plan_numbers.py` re-derives every row a script can produce today and
requires those numbers to appear in the row, matched on digit boundaries so that
`6` does not satisfy a row reading `60` — a fixture, because that is exactly the
false pass a naive substring check would give on the orphans row.

Rows are found by their **Measure** cell rather than by position, so inserting a
row cannot silently shift the checks onto their neighbours.

Four rows are **not** checked and are named as unchecked on every run:

```
Reader questions answered   query_probe.mjs drives a real browser
Throttled load              a timing run — the row itself says "this container only"
Search & heap at 3x         a synthetic timing run
Gate results                the per-suite counts come from a full `make all`
```

Deriving the timing rows here would either make a static gate need Chromium or,
worse, make it quietly assert whatever hardware CI happened to allocate that
morning. Printing them as unchecked is the honest option: their status is
visible rather than assumed. Two of them were re-measured by hand this session
anyway — `resilience` had grown 32 → 63 checks and `axe` 6 → 29 while the table
recorded the old counts.

### A parse that stops matching must fail, not pass

Every derivation asserts it found what it was looking for and exits with the
pattern that stopped matching. Without that, a tool rewording one line would
turn this into a gate that reports "0 drifted" forever — and a validator
reporting zero because it stopped looking is indistinguishable from one that
found nothing wrong. That distinction is the reason half the tools here carry a
self-test, and it is the one failure mode a checker of checkers can actually
have.

### Its first catch was itself

Adding the gate added two commands to `make check`, so `check_gates.py` went
33 → 35, so the Gates row it had just corrected was wrong again — and it said
so on the next run. A gate that catches its own installation is a small thing,
but it is the difference between a check that runs and a check that works.

```
plan.md: 9 rows corrected · gates 33 -> 35
check_plan_numbers fixtures 8 + table parsing · 301 browser checks green
```

## Session — the corruption in the languages a grammar could not prove

Three checks now catch the div → pre newline damage, and the first two share a
blind spot. Both are grammar arguments: Python has no continuation at a bare
`=`; a comment continuation carries its own marker. They are decisive *because*
a language's rules make the shape impossible — and that is exactly why they see
nothing in CSS, Go, Bash, PowerShell or JSON, where every one of those shapes is
legal.

Two attempts at a general rule are already recorded as failures, and both failed
the same way — by being plausible. 635 hits for "a line that looks like it ends
mid-statement". 343 for "a continuation indented by exactly two spaces". Reading
the first ten of each found them legitimate.

### The signal is the cause, not the symptom

A `<div>` collapses leading whitespace. So a block authored inside one **never
carried indentation at all** — there was nothing for the `<pre>` conversion to
restore. Both earlier heuristics were looking at where the newlines landed. The
newlines are the symptom. The missing indentation is the defect itself.

> a block of 5+ lines that opens a bracket **twice or more** and has **not one
> indented line anywhere**

**18 hits across 706 multi-line blocks. All in `script.01-references.html`, and
every one real.** The first heuristic in this file's history at 100% precision,
and it got there by describing what the damage *is* rather than what it looks
like.

Two openers are required rather than one, because a single trailing `{` is how a
one-line body or a heredoc opener is written and says nothing about indentation.
That is a fixture, along with flat SQL that never nests.

### What was in them

The language quick reference — the part of a study site people copy from:

```
.flex-container {          {                     func
display: flex;             "string":            divide(a,
flex-direction: row;       "hello world",       b
/* row|column|row-reverse */  "number":         float64) (float64, error) {
```

Eight CSS blocks, three Go, two Bash, one ZSH, one PowerShell, two JSON. The
JSON pair is the one worth pausing on: it is the card that **teaches the JSON
format**, and it had been rendering every key on one line and its value on the
next since the conversion.

### JSON's grammar is too permissive to see its own corruption

The obvious check — parse every JSON block — was written first and finds
nothing, because **JSON is whitespace-insensitive**: a newline between a key and
its value is valid JSON. Stripping `//` comments (string-aware, so a URL
survives) and parsing all twelve JSON-shaped blocks leaves two failures, and
both are deliberate **JSON Lines** — a chat transcript and a JSON-RPC exchange.

So the parser is silent on the two blocks that are actually broken and speaks
only about the two that are fine. Worth recording as a negative: the permissive
grammar is not a weaker version of the signal, it is the wrong instrument.

### The repair could not break the markup even if the target were wrong

Both mechanisms are whitespace-only **by construction** rather than by checking
afterwards:

- **the CSS reflow** tokenises markup into tags, text and whitespace runs, copies
  tags and text byte for byte, and recomputes only the whitespace;
- **`retarget`** takes a hand-written plain-text layout and re-emits the original
  markup with that layout's whitespace, after comparing both **character by
  character with all whitespace removed**. A target that drops, adds or reorders
  one character cannot be applied at all — it raises, naming the character and
  its context.

`retarget` round-trips all 81 blocks in the file unchanged before being used on
any of them, which is the test that it preserves what it claims to preserve.

### Three things the automation got wrong, all worth keeping

1. **`&gt;` ends in a semicolon.** A declaration-ends-here rule split `div > p`
   across two lines. Entities have to be unescaped before any punctuation rule
   reads them.
2. **An empty rule body.** `div p { }` with a trailing comment is how the
   combinator table is written; a naive rule put the braces on three lines.
3. **Whether a comment belongs to the rule above or below is judgement.** The
   original line structure is the very thing that was corrupted, so it cannot
   answer. Section headers are therefore named explicitly rather than guessed.

### Proved against the file, not only against fixtures

```
before the wave      18 findings, exit 1
after the CSS commit 10 findings, exit 1
after this commit     0 findings, exit 0
```

Six new fixtures: the corruption, the same block correctly indented, a block too
short to judge, a single-opener heredoc, flat SQL, and Go — the language the two
existing checks cannot see.

```
18 blocks reflowed · lint fixtures 22 -> 28 · 35 gates green
301 browser checks green
```

## Session — the file did the thing it told itself to do

Every census clean: depth, orphans, duplicates, the reader-question probe, the
volatility queue read and explained in its own docstring. Two new measurements
of my own came back clean as well — **3,850 concept-card titles, 3,840 of them
distinct**, the ten repeats being the deliberate three-card troubleshooting-
playbook shape and four beginner/advanced level splits; and the card-level floor,
where the 111 cards under 200 characters are `philosophy` and `pentest` index
cards that are short by design.

An empty queue is not nothing to do. It is a **trigger**, and this file wrote it
down:

> **Option 3 first, then option 1 when the live queue next empties.**

Option 1 is the split. The condition was met, so the split happened.

### The trigger is the part worth copying

The risk was scored **open, and now acute** at 11,600 lines. The file was
**22,745** — nearly double — and nobody had noticed, because "this file is too
long" is a feeling and feelings do not have a moment attached.

What made it decidable was that the previous session had written a *condition*
rather than a *deadline*: not "split it soon" but "split it when the live queue
empties". That is checkable by running the censuses, which is a thing a session
does anyway. Every other accumulation risk in the register below has the same
shape and none of them has a trigger yet.

### What moved, and the one thing that deliberately did not

`plan-archive.md` gets the July 2026 review, the content roadmaps, Phases 3–10,
the Execution Handbook, the calculus track, the worked specifications, and 242
session records. `plan.md` keeps the operating manual, the card rubric, Phase 11,
the risk register, the domain-shape reference and the last dozen records: **1,833
lines against 22,745.**

**The split conserved lines rather than summarising them.** Every line of the
original is in exactly one of the two files, asserted by comparing a multiset of
every line before either file was written. Summarising would have been easier and
is how the reasoning gets lost.

The one thing not corrected on the way out is the superseded *"What's in this
file"* table, which still describes Phases 4–6 as planned and quotes ~828
remaining cards over a site of 1,008 topics. It is the primary evidence for this
archive's most-repeated lesson — *the backlog count was badly inflated* — and a
plan that keeps what it expected beside what happened is worth more than one that
keeps only the outcome.

### 23 references now pointed at the wrong file

Eleven tools, the Makefile, the workflow and the README cite *plan.md Phase 8*,
*Phase 9 §3*, *Phase 10 T4*, *CALCULUS TRACK section 3*. Every one of those
sections had just moved. `near_duplicates.py` prints its citation **at runtime**,
so that one would have sent a reader to a file that no longer contained the
section, from the tool's own output.

A split is not a file operation. It is a rename of two dozen cross-references,
and the only reason none of them broke silently is that they were grepped for
before the commit rather than after.

### The bookkeeping was wrong within the hour

The first index written for the split said **"241 records moved, the last twelve
kept"**. The real numbers are **242 and 11** — wrong in both halves, written by
the session that was at that moment three commits into fixing nine other
hand-maintained numbers in the table directly above it.

So the record counts are now a derived row in `check_plan_numbers.py` like
everything else, and the fifth risk is closed:

| Risk | Was | Now |
|---|---|---|
| The plan outgrows its own readability | Open, and now acute — 22,745 lines | ✅ Closed — 1,833 live, 20,972 archived |

```
plan.md 22,745 -> 1,833 lines · plan-archive.md 20,972 · 253 records preserved
23 cross-references repointed · derivable rows 11 -> 12 · 35 gates green
```

## Session — the register said Open about three problems that were solved

The measured-state table was wrong because it was hand-maintained. That fix is
two commits old. This is the same defect one level up: **the risk register**, the
table a session reads to decide what to work on, still scored three of its four
risks **Open**.

They had been closed weeks earlier. The record *"closing 'unreachable quality',
the third open accumulation risk"* re-measured all four and found:

| Risk | Register said | Had actually been |
|---|---|---|
| Silent style drift | 330 topics (23%) thin | **11 of 1,544 — 1%** |
| Blind duplication | 36 pairs at ≥50% overlap | **95 pairs, 0 unread** |
| Unreachable quality | 902 unlinked, 159 deep | **60 unlinked, 0 deep** |

That session wrote the re-measurement into a **session record** and left the
register alone. The finding was recorded where findings go and not where
decisions get made, so the register went on advertising three solved problems.

### The fifth risk was the only one with a trigger, and the only one that closed itself

That is not a coincidence and it is the reusable part.

An accumulation risk has no moment attached — nothing goes wrong on a particular
day. *"Act when it gets bad"* fails because **bad has no threshold**: this file
sat at 22,745 lines, nearly double the length at which its own register called it
*acute*, and no session ever decided that was the day. The fifth risk carried
*option 1 when the live queue next empties* — a condition evaluated by running
the censuses a session runs anyway — and the session that found it true is the
session that acted.

So every row now carries a **reopens when** column. Not a target; a condition,
phrased so a tool already in `make check` or `make census` decides it:

```
Silent style drift      depth_report.py puts thin above 2%, or a domain above 10%
Blind duplication       near_duplicates.py --unexplained returns anything at all
Unreachable quality     orphan_report.py reports a single deep orphan
Unfalsifiable freshness never — there is no condition, which is the finding
```

The fourth row is the honest one. It is *accepted, not mitigable*, and giving it
a fake trigger to make the column look complete would be the worse error.

### No number appears twice

Each row points at the row of the measured-state table that carries its figure
instead of repeating it. A second copy is a second thing to go stale, which is
precisely how this table got wrong — and the measured-state table is the one
`check_plan_numbers.py` already checks.

### The same defect, a third time, in a tool's own docstring

`near_duplicates.py` opens with *"Of 95 pairs, 76 differ on something §3 calls
deliberate and 19 differ on nothing"*. The live run says **78 and 17**. Somebody
had updated the 95 and not the two numbers beside it.

Scanning every tool docstring for embedded figures found this to be the only
present-tense claim that had drifted. The rest are dated on purpose — *"At 1,534
topics there were 1,549 attributes"*, *"288 of 1,432 (20%) when this was
written"* — and that phrasing is the reason they cannot rot. A snapshot says when
it was taken; a bare number claims to be now.

The docstring also conflated two different things, which the register's new
column made visible: `--unexplained` lists pairs with **no recorded verdict**,
currently none, not the 17 that differ on nothing and have all been read.

```
4 register rows re-measured and given reopen conditions · 1 stale docstring
35 gates green
```

## Session — nine deliberate zeros that were one gap

`query_probe.mjs` asks 66 questions a reader might actually type and reports which
return nothing. Nine returned nothing, and all nine had been read and marked
**deliberate** — each with a note, each defensible:

```
wifi keeps dropping         kind 3 — the site has the wireless cards; none phrases a symptom
vpn keeps disconnecting     kind 3 — same shape as the wireless one
laptop won't turn on        kind 3 — hw covers POST and beep codes, not the symptom
outlook won't connect       kind 3
someone clicked the link    kind 3 — the response card exists and does not use these words
git detached head           kind 3 — the Git cards do not phrase this state
```

Read one at a time, every one of those is a fair call. Read as a list, they are
**not nine decisions. They are one.** Every single zero is a *symptom* phrasing,
and every note says some version of *the subject is covered, the symptom is not*.

The site is organised the way somebody who understands a subject would organise
it. A reader in trouble arrives the other way round — with what is happening to
them, not with the name of the thing that is broken.

### Why the "deliberate" marking hid it

The verdict field is per query. Nine separate rows each got a reason, and the
reason was correct nine times. Nothing in the census asks *do these nine
dismissals rhyme*, and nobody was going to notice by reading one row a session.

That is a general shape worth naming: **a list of individually justified
exceptions is where a systematic gap hides.** The near-duplicate census has the
same structure — 78 pairs "differ on something §3 calls deliberate" — and it has
never been asked whether those 78 rhyme either.

### The first wave: `net`

The manual's rule is one wave, one domain, so this is two cards in `net`, and
both are real content rather than a symptom phrase bolted onto an existing card.

**Wireless Troubleshooting** already had a strong roaming card whose table has a
row for *drops during a call while walking*. A client that drops **while
stationary** is a different fault, and the card that was missing is the one that
says the diagnosis is not in the signal strength — it is in *who* drops and
*when*. Everyone on one AP at once is a DFS radar event; everyone at a fixed
interval on an 802.1X SSID is a session timeout hitting a slow RADIUS server; one
device model is a driver; and *stays connected, loses the network* is a DHCP
scope with no free leases and not wireless at all. Coverage is the last
hypothesis on that list and the only one that costs a site visit.

**VPNs** had five conceptual cards — what a tunnel is, protocols, proxies, SSH
forwarding, ZTNA — and nothing about operating one. A tunnel is a long-lived flow
across equipment that reaps idle sessions and rewrites addresses, none of which
knows it is carrying a tunnel, so the clock is the diagnostic: a constant interval
is a rekey, an idle period is a timeout on the path, a change of network is
mobility. Two of that card's six rows are not the VPN failing and one of them is
not a disconnection.

### Checked by the probe, not by assertion

```
before   66 queries · 57 answered · 9 found nothing
after    66 queries · 59 answered · 7 found nothing
```

The two questions that closed are exactly the two aimed at. That is the whole
argument for a probe that phrases questions the way a reader would rather than
the way the site does — the same wave without it would have ended in "this should
help".

`check_plan_numbers.py` also caught three rows moving from two cards: mean chars
per card 1,377 → 1,378, the median 3,690 → 3,693, and the page budget's room from
~840 topics to ~838. The non-verdict mean did not move, which is the counter-metric
saying the growth is body text and not verdict.

### The remaining seven

`laptop won't turn on` and `outlook won't connect` (`hw`, `m365`), `someone
clicked the link` (`blueteam`), `difference between a hub and a switch` (`net`,
and a comparison rather than a symptom), `git detached head`, `terraform state
locked`, `docker image too big` (`devops`). Five more domains, five more waves —
and the point of writing the shape down is that the next session does not have to
rediscover that they are one thing.

```
net: 2 cards · reader questions 57 -> 59 of 66 · zeros 9 -> 7
1,544 topics · 35 gates green · 301 browser checks green
```

## Session — a correction: the last wave overrode a standing instruction without reading it

The previous record treats nine probe zeros as one gap and writes two cards.
The cards stand, and the reasoning for them was wrong in a way worth recording.

`query_probe.mjs` does not merely report zeros. Its docstring carries a
**standing instruction** about them, in three kinds, and kind 3 says:

> `wifi keeps dropping`, `git detached head`, `terraform state locked`. The site
> has the technology card for each and phrases none of them as a symptom.
> **Leave these alone.** Seeding symptom phrases into cards is keyword stuffing
> with a rationalisation attached.

`wifi keeps dropping` is named there explicitly. I wrote a card for it. The
operating manual's own start-of-session list says to read *the docstring of
whichever census last reported something*, and the census had reported this, and
I read the output and not the docstring.

### The cards survive the check, on evidence gathered afterwards

The right question is not whether I was allowed to, but whether the zero was
really kind 3. Kind 3 means the answer exists and only the reader's word is
missing. Grepping `net.html` **before** the wave for the causes of a stationary
drop:

```
radar (DFS events)              0
Protected Management Frames     0
Session-Timeout (802.1X reauth) 0
MOBIKE                          0
rekey                           0
band steering                   1   — one cell of the roaming card's fix column
```

The existing card's only drop row is *drops during a call while walking*, which
is a roaming failure. Five of the six causes of a stationary drop appeared
nowhere in the domain. That is kind 2 — *the question is real and the card was
not there* — and the cards would have earned their place with no probe at all.
`near_duplicates.py --title` returns only the topic itself, and card titles are
still 7 reused across 3,842, unchanged by the wave.

### What was actually wrong, and the test that replaces it

The kind-3 call had been made from a **topic list**. Five wireless topics exist,
so "the site has the technology card" read as true. It was true one level up
from where the question lives. A reader's symptom implies a specific *fault*, and
the topic that owns the subject can be missing it entirely.

So the docstring now carries the test rather than the verdict:

> name the specific fault the question implies, then grep the domain for its
> causes. Kind 3 is when they are there and only the reader's word is missing.
> Kind 2 is when the count comes back zero.

Applied to the rest: **`laptop won't turn on` is genuinely kind 3 and stays.**
`hw` has *The Order That Resolves Most No-Boot Machines* — the answer written
out, missing only the reader's phrasing — so the symptom wave stops there rather
than continuing through five domains as the last record proposed. `git detached
head` and `terraform state locked` have not been re-checked at fault level and
are not reclassified until they are.

### The part that generalises

A kind-3 call is **a decision not to write something**, and it was being made
from a topic list. Dismissals get less evidence than actions do, because nothing
is produced to review. The previous record found that nine individually
justified dismissals hid one gap; this one is the same lesson turned on the
instruction that produced them — the rule was right and the classification
feeding it was not.

```
query_probe.mjs docstring: kind 2 vs kind 3 now has a test · 0 cards written
the symptom wave stops at net · 35 gates green
```

## Session — running the test on the six zeros it was written for

The correction above added a test for telling a real gap from a phrasing gap:
*name the fault the question implies, then grep the domain for its causes.* This
is that test, run on every remaining zero, and it splits them three ways rather
than the two the census had.

| Query | Fault-level grep | Kind |
|---|---|---|
| `laptop won't turn on` | `hw` has *The Order That Resolves Most No-Boot Machines* | **3** — answer written out |
| `outlook won't connect` | the M365 playbook's *Symptom → Layer* card routes it: one device, one app → Client | **3** |
| `docker image too big` | multi-stage 8, `.dockerignore`, layer caching, image size — all in `devops` | **3** |
| `someone clicked the link` | password reset and session revocation across `threat` and `sec` | **3** |
| `git detached head` | `detached` **0**, and the reflog card sends you into the state without naming it | **1** |
| `terraform state locked` | `force-unlock` **0** corpus-wide; locking covered as a practice, never as a failure | **1** |

Four confirmed kind 3 and left alone. The two that moved did not move to kind 2
— they moved to **kind 1**, *the site says it in the other word*, whose remedy
the rules already call better writing anyway.

### The reflog card sends the reader into the state it is protecting them from

*git reflog — Your Undo Button for Almost Anything* says to run:

```
git checkout HEAD@{1}
```

That detaches HEAD. The card does not say so — and three commands later it goes
looking for *"dangling commits not referenced by any branch"*, which is precisely
what you create by committing in the state the earlier line just put you in. The
card describes both ends of the hazard and never names the middle.

So it names it now, and the code block creates a branch instead of leaving the
reader on a commit that belongs to nothing. **That is not a symptom phrase bolted
on; it is a missing warning in a recovery procedure.**

The Terraform state card had the same shape: *lock it to prevent concurrent
applies*, and nothing about the lock outliving the run that took it. A cancelled
pipeline leaves it held by nothing and every later apply stops on it.
`force-unlock` appeared **zero** times in the corpus.

### One of them is still a zero, deliberately

`git detached head` now answers. **`terraform state locked` does not.** The
matcher wants its three words near each other; the prose says *"a lock held by
nothing"* and `force-unlock`.

It is left that way. The edit was worth making because the failure mode was
absent from the corpus, not because a probe wanted it, and rewording a sentence
so it sits better with this particular matcher is exactly the keyword stuffing
the census forbids. **A zero that stays zero after a justified fix is a better
record than a sentence bent to close it.**

### The standing list is a regression corpus, and I nearly shrank it

Having closed three queries, my first edit **deleted them** from the query list —
which took the total from 66 to 63 and would have removed the only thing that
would notice if a future edit broke them again. They are back, without a `kept`
note, so a regression shows up as `ZERO` rather than as a dismissal somebody
already blessed.

Every remaining zero now carries the evidence of its own dismissal in the list
itself, so the next session inherits the greps instead of repeating them.

```
2 cards edited — the docstring's own budget · reader questions 59 -> 60 of 66
zeros 7 -> 6 · 35 gates green · 301 browser checks green
```

## Session — 101 paths, and nobody had ever compared two of them

The duplication programme compared **topic titles**. The navigation programme
checked that every path step **resolves**. Neither asks the question a reader
asks, which is *these two paths have different names — are they different?*

Three path measurements. Two came back clean and are worth the line they take:
**0 paths with a repeated step**, **0 paths under 4 steps**, no duplicate path
names, median 15 steps. The third did not.

### One pair, at 92%

```
92% contained (Jaccard 0.42) · 11 of 12 steps shared
    Thinking Clearly  [12 steps]
    How to Think      [25 steps]
```

Their first **nine steps are identical, in the same order.** And the audience is
declared twice in different words:

> *for:* Anyone who has to decide something with incomplete information
> *for:* Anyone making decisions on incomplete information, which is the job.

A reader browsing 101 paths sees two names and two blurbs and has nothing to
choose on. Whichever they pick, they get the same nine cards first.

**Containment, not Jaccard** — and this pair is the argument for it. By Jaccard
it scores **0.42** and never appears in any top-of-list. The short path is
invisible inside the long one precisely because the long one is long.

### The fix is a boundary, not a deletion

Each path had a real job and was doing the other's as well:

- **Thinking Clearly** is now the **reasoning kit** — argument, evidence, biases,
  models, deciding, ethics on a real decision, and arguing against your own plan
  before reality does. Eight steps, all instrumental.
- **How to Think** is now the **traditions** — the Greek schools, the Eastern
  ones, the pagan revivals, the realists, and (because half of what they are
  quoted as saying they never said) how to source a quotation. Eighteen steps.

Each blurb now names the other, which is how a reader tells them apart on the
screen where they choose. Deleting one would have left a 25-step sprawl with no
entry point for somebody who only wants to decide something today.

**Shared steps after: zero.** No topic lost path coverage — the check that
matters is that *distinct topics reachable from a path* held at **1,484 of
1,544** while total steps fell 1,581 → 1,570. Eleven steps removed, none of them
the last route to anything.

### What the threshold is not for

The highest remaining pair is **56%** — five steps shared between *AI Safety,
Security & Governance* and *AI at Work*. That is two subjects that genuinely
meet, and a step belongs in every path it belongs in. The census is looking for
a path with **no job of its own**, not for overlap.

Committed as `near_duplicates.py --paths` rather than written down as a number,
for the reason this file gives every time: the figure goes stale and the script
does not.

```
paths 1,581 -> 1,570 steps · 1,484 of 1,544 topics still reachable
path pairs at 60%+ containment: 1 -> 0 · 35 gates green
```

## Session — a topic with no concept cards, and the three defects behind it

The depth report's bottom row is `military — Common Codes Decoded`, **0 cards**,
317 characters. Every other topic on the site has concept cards. Counting them
found **six** topics that do not: the four `shortcut` OS tables, `military`'s
code list and `ai`'s glossary — the site's oldest flat lookup tables, while the
other 32 `shortcut` topics have used `.concept-card` for years.

That is a structural oddity, not a defect. Pulling on it found three defects.

### 1. Search opens the topic and highlights nothing

`script.js` highlights hits inside a fixed list — `.topic-name, .concept-title,
.concept-label, .concept-desc, .dw, .dt, .code-block`. A table sitting straight
in a `.topic-body` is in none of them.

Proved in a browser rather than argued, and the evidence is as clean as this
gets — one query, one page, two topics:

```
"Joint Comms"   Sub-Designators — The Third Digit    5 highlights
                Common Codes Decoded                 0 highlights
"Emoji picker"  Windows                              0 highlights   (1 topic matched)
"Kill Chain"    control                             13 highlights across 7 topics
```

The reader is handed an opened lookup table and left to find by eye the word the
page had already located. Wrapping each table in `.dw` — one element, no content
invented — takes all three probes from 0 highlights to 1.

`lint_content.py` now fails on a table that is a direct child of `.topic-body`,
with four fixtures and proved against the pre-fix files: **6 findings, exit 1.**

### 2. A verdict describing a table two topics away

`ai`'s glossary — AGI, Embedding, Token, Hallucination — ended with this:

> **Only one of these rows can fine you, and it is the one with dates attached.**
> …the regulation is, and its obligations depend on which risk tier a system
> falls into…

None of those rows can fine anybody. It belongs to *AI Governance & Frameworks*,
the topic immediately before it, whose table ends **`EU AI Act · Risk-tier
regulation`** — and which the linter had been reporting for months as one of the
twelve tables with no verdict. The census knew a table was missing its verdict
and the verdict was one topic away.

Moved, and the glossary got one of its own — about the collision the next defect
is made of.

### 3. `ANN (Approximate Nearest Neighbour) · Artificial Neural Network`

One row, contradicting itself across two cells. The dictionary holds both
meanings and `byDomain.ai` picks the vector-search one, which is right almost
everywhere in `ai` and wrong in the one row whose next cell spells out the other.

The annotator's existing guard skips a term when **its own** expansion is
already nearby. The failure is what it does when a **different listed meaning**
is spelled out beside the match and its own is not: that is the text
disambiguating itself, in the other direction, and inserting the domain default
there can only produce a contradiction on one line.

Measured across the corpus for other instances: **1**, the one found by reading.
A high-precision signal — and my first two attempts to measure it returned 0
because the window `already_expanded` builds *includes the injected span's own
text*, so every annotation looked self-confirming. Third detector of mine this
session to be wrong before it was right.

Guarded in `annotate_acronyms.py` with four fixtures, and they check both
directions: the row is left alone, the domain's own sense is still annotated,
its own nearby expansion still suppresses it, and a single-meaning acronym is
unaffected. Re-running the annotator removed the span.

### What the three have in common

None was on any list. They were reached by asking why one topic had zero cards —
a question with no defect in it at all. The depth report has printed that row
every session for months as a length, which is the one thing about it that does
not matter.

```
6 tables wrapped · 1 verdict moved · 1 verdict written · 1 contradiction removed
lint fixtures 28 -> 32 · annotator fixtures 2 -> 6 · 35 gates green
```

## Session — the front door described a site nine domains smaller than it is

Four places have now been caught quoting a number about this repository that had
drifted: the measured-state table, the risk register, a tool's own docstring, and
the query probe's classification. The fifth is the one a visitor reads first.

**`README.md`'s Domains table listed 21 domains. The site has 30.**

```
♾️  DevOps, Platform & Delivery          50 topics
🏢  Windows Server & Infrastructure      52
🧮  Computer Science Fundamentals        66
🔧  Hardware, Electronics & Embedded     28
🚀  IT Career & Craft                    45
⏱️  Productivity & Learning Systems      22
🧠  Mind & Wellbeing                     20
📐  Mathematics — Calculus               16
❝   Quotes — Sourced & Corrected          6
```

**305 topics, a fifth of the site, missing from its own front page** — and four
of those nine are the Phase 5 tracks whose completion the archive celebrates at
length. The table was written when the site had 21 domains and nine were added
without it. It also advertised *"980+ acronyms"* against a dictionary of
**1,101**: not false, which is how it survived.

### Written from the domains, not from memory

Each new row's key topics come from that domain's actual topic titles, read out
of `data/*.html` rather than recalled — the manual's failure #2 is five invented
cross-references produced exactly that way, and a README is the one file where
nobody would check.

### Counted, not title-matched

The check is on **count**, plus every domain's icon appearing somewhere in the
table. Titles deliberately differ: the README says *Sec Operations* where
`domains.json` says *IT & Security Operations*, and *Security Core* for *Security
Core Concepts*. Forcing those to match would mean a worse README for a tidier
check. Icons cannot be the key either — two pairs of domains share one (🌐 for
`net` and `web`, 🏛️ for `eng` and `grc`).

Count is enough, because it catches the failure that actually happened: **a
domain is added to the site and the README is not.** Proved against the pre-fix
file — *"the Domains table lists 21 domains, data/domains.json has 30"*, plus
nine named icons, exit 1.

### The pattern, now that there are five

Every one of them is prose *about* the repository, kept by hand, in a document
whose readers cannot tell it has drifted. None of them was ever wrong when
written. The counter-measure that keeps working is not care — it is that the
number has to be derived somewhere a build can compare it.

`check_plan_numbers.py` has therefore stopped being about `plan.md` and is about
the repository's own prose. Its name stays, because renaming it means touching
the Makefile, the workflow, and `check_gates.py`'s two lists, for nothing a
reader gains.

### And a sixth, found by grepping for the shape rather than the number

`CONTRIBUTING.md`: *"…which is why they still cover all **29** domains while one
is rendered."* Thirty. It has been thirty for a while, and the sentence is a good
one about a real design property — the deferred-domain architecture — which is
exactly why nobody re-read it.

Found by grepping the two present-tense documents for `\d+ domains`, which is
now the check: any such claim in `README.md` or `CONTRIBUTING.md` must equal
`data/domains.json`. **Deliberately not applied to `plan.md` or the archive** —
those are full of counts that were true when written and are the *record* rather
than a claim, and a gate that could not tell the difference would force history
to be rewritten every time the site grew.

```
README domains 21 -> 30 · acronym claim 980+ -> 1,101
CONTRIBUTING 29 -> 30 domains · 35 gates green
```

## Session — fourteen Kubernetes topics and none about a pod that will not start

The playbook symmetry test, run across all 30 domains: which have a
troubleshooting-shaped topic and which do not. `cloud` has four, `ops` six, `hw`
five, `net` four, `endpoint` four. **`devops` has none** — 50 topics, and the
cert tag on the domain is **CKA**.

Checked at content level before believing it, which is the rule the Azure waves
left behind:

```
CrashLoopBackOff   0    ImagePullBackOff  0    OOMKilled       0
pending pod        0    readiness probe   0 (devops)           1 (cloud)
```

Fourteen Kubernetes topics across `devops`, `cloud` and `redteam` — objects,
networking, storage, RBAC, secrets, multi-tenancy, the threat model, incident
response, container escape — and **not one about a pod that will not run.** The
architecture is covered and the first hour of operating it is not.

`near_duplicates.py --title` first this time, rather than after: nothing at or
above 0.50, closest 0.40. Clear to write.

### Three cards, and each one is a distinction rather than a list

**The status field is a diagnosis, not an error message.** The instinct is
`kubectl logs`, and half the time there are none because the container never
started — which half you are in is already in the status. `Pending` is the
scheduler and rules out your image and your code entirely; `ImagePullBackOff` is
the registry; `CrashLoopBackOff` means the image is *fine* and the app ran, so
the logs exist but only under `--previous`; `Running, not Ready` is nothing
failing at all, it is a readiness probe withholding traffic on purpose. Three of
six rows are not your application and one is not a fault.

**The two probes do opposite things.** Liveness restarts the container; readiness
removes it from the Service endpoints and restarts nothing. Point a liveness
probe at a dependency and a slow database becomes a cluster-wide restart storm —
every replica fails at once, every replica restarts cold, and the outage is now
yours rather than the database's.

**Requests and limits decide different things, and memory is not CPU.** One
asymmetry explains the whole table: memory is incompressible, so the only
enforcement available is killing the process; CPU is compressible, so the
enforcement is slowing it down. That is why a memory limit fails loudly and
correctly-diagnosed, and a CPU limit fails quietly and gets misdiagnosed for
weeks.

### The reopen condition fired on my own content, two sessions after I wrote it

The risk register's *unreachable quality* row says it reopens when
**`orphan_report.py` reports a single deep orphan.** Building the topic did
exactly that:

```
orphans 60 -> 61, of which deep 0 -> 1
```

A three-card, 4,591-character topic that nothing linked to — the same "half a
job" the archive names, caught this time by a condition rather than by somebody
remembering. Four reciprocal `related.json` links and a step in *Kubernetes, End
to End*, placed after *Kubernetes Objects* because that card ends on **"The Field
That Decides Which Pod Dies at 3am"** and this is what happens next. Deep
orphans back to **0**.

### And failure #7, exactly as written

The manual's seventh failure is *"wrote a related-map target from memory; slugs
truncate at 60 characters"*. I took the slug from `orphan_report.py`'s output —
which **truncates its display column** — and wrote
`…before-the-log` for a topic whose id ends `…before-the-logs`. Four one-way
edges and five "no such topic" errors, named by `suggest_related.py --check` in
one run. The lesson survives with one word changed: do not take an id from
anything that formats for a terminal.

```
devops 50 -> 51 topics · 1,544 -> 1,545 · paths 1,570 -> 1,571 steps
related 4,696 -> 4,704 links, 0 one-way · deep orphans 0 · 35 gates green
```

## Session — the one reader that cannot tell it is being lied to

`sitemap.xml` said `lastmod 2026-07-31` through months of daily edits. It is the
seventh thing in this repository found quoting a fact about itself that was true
once, and it is the only one whose reader is a **crawler** — a person notices a
stale README eventually; a crawler adjusts its recrawl interval and says nothing.

Nothing derived it, so it could only ever be right by accident.

### Three sources, and two of them are wrong for reasons this repo already knows

| Source | Why not |
|---|---|
| A build timestamp | Every build would differ from the last, which `check_determinism.py` exists to forbid: two runs over unchanged sources must produce identical bytes |
| The last commit date | Circular — the commit that writes the date changes the date, so the file is dirty the moment it is committed |
| **The newest `data-reviewed` stamp** | Content-derived, stable across rebuilds, and it moves exactly when the site's own claim about its freshness moves |

The third is what `lastmod` is supposed to *mean*, and the site already maintains
it: `stamp_freshness.py` puts a month on every topic and `--verify` gates it.

Written as **`YYYY-MM`**, a complete W3C Datetime and the precision the content
actually has. `2026-07-31` implied a day; nobody reviewed the site on the 31st.
Padding a month to a day is inventing evidence, which is the thing this file
keeps catching.

### Gated three ways, because a generated file that nobody checks is where this started

- `check_determinism.py` now watches it — **3 outputs reproducible**, not 2.
- The workflow fails if it is stale, the same shape as the `index.html` and
  `sw.js` steps.
- `build.py` raises rather than shrugs if the `<lastmod>` element is gone.

Proved by putting the old value back and rebuilding: `+ sitemap lastmod ->
2026-09`, a one-line diff, and `make check` green either side.

### The deployment surface, read once, since nothing else reads it

The rest holds up and is worth recording so the next session does not re-derive
it. `netlify.toml`'s CSP is `default-src 'none'` with no `unsafe-inline` on
scripts — which is only possible because every handler is wired in `script.js`
via `addEventListener`, and the smoke test's *no off-site requests* check is what
keeps it true. `_redirects` sends unknown paths to the themed 404 and does no
path rewriting, correct for a site whose deep links are `#hash` fragments
resolved client-side. `robots.txt` points at the sitemap. The single `<url>` is
right for the same reason the redirects are: hash fragments are not separate URLs
to a crawler, so a sitemap listing 1,545 of them would be listing one page 1,545
times.

```
sitemap lastmod: hand-written 2026-07-31 -> derived 2026-09
determinism watches 2 -> 3 outputs · 35 gates green
```

## Session — one badge, spelled two ways, in one domain

A structural question with no defect in it: **is the badge vocabulary a
vocabulary?** It is not, and that is the right answer — 608 distinct badges over
1,485 topics, 391 used exactly once, and 1,359 distinct concept labels over
3,857 cards. Both are free-form kickers written per topic, and a controlled
vocabulary would flatten a deliberate device: reference topics *shout*
(`5-STEP CYCLE`, `OS CORE`, `COMPLETE REFERENCE`).

So the census gives nothing. Normalising it does. Strip case and punctuation, and
**nine badge strings appear with more than one spelling.**

### Four are one domain disagreeing with itself

```
linux      LINUX • Ops ×2          vs  Linux • Ops ×1
linux      LINUX • Security ×1     vs  Linux+ • Security ×1
endpoint   Endpoint • Operations   vs  ENDPOINT • Operations   (0% of endpoint is uppercase)
ai         LLMOps ×2               vs  LLM Ops ×1
```

Each resolved to the domain's own form, established by counting rather than by
taste: `linux` writes `LINUX •` for topic areas eight times and reserves
`Linux+` for its beginner layer; `endpoint` has **no** fully-uppercase badge
among 56; `LLMOps` is the industry spelling and the majority.

### Two are different domains, and are left alone

`grc` has one `ARCHITECTURE`; `eng` has ten `Architecture`. They normalise alike
and are **never on screen together** — the page renders one domain at a time.
Forcing them to agree would be a style rule wearing a correctness rule's
clothes, so the check is scoped to a single domain and says so.

### The other three were a series quietly breaking its own rule

Of 28 `Start Here` badges — the beginner layer — fifteen name a certification
and thirteen shout a domain code. That split is not arbitrary: `GRC`, `MIL`,
`QUOTES`, `SCRIPT` and `General` have **no CompTIA certification to name**.

Four did:

```
net        NET • Start Here        beside two  Net+ • Start Here
sec        SEC • Start Here        beside two  Sec+ • Start Here
pentest    PENTEST • Start Here    beside two  PenTest+ • Start Here
threat     THREAT • Start Here     beside two  Sec+ • Start Here
```

Three of those are spelling clashes and the gate catches them. **The `threat`
one is not** — `THREAT` and `Sec+` do not normalise alike, so no mechanical rule
sees it. It was found by reading the series, fixed by reading the series, and it
is recorded here because the gate cannot claim it.

### What the check is careful not to be

`lint_content.py` now fails on one badge spelled several ways **within one
domain**, with four fixtures — including `Sec+` versus `SEC`, because dropping a
`+` is a punctuation difference that renames a certification. Proved against the
pre-fix files: seven findings, exit 1.

Badges drive `data-level` (`\bbeginner\b` → beginner, `advanced|expert|deep` →
advanced), so a badge edit can silently move a topic between teaching levels.
Checked either side: **core 1,415 · beginner 121 · advanced 9**, unmoved.

```
8 badges normalised · lint fixtures 32 -> 36 · 35 gates green
```

## Session — eleven islands the orphan census could not see

An orphan is a topic nothing points at, and the site has 60, all generated. An
**island** is subtler and no census had asked for it: a group of topics that link
to each other — so *not one of them is an orphan* — and to nothing else. The
"See also" strip never leads out. A reader who arrives can circle indefinitely
without being offered the rest of the site.

Connected components of `related.json`:

```
1,485 linked topics · 12 components · mainland 1,432 (96%)
   53 topics across eleven islands
```

### The composition was the finding, not the count

```
16  math      the entire calculus track
 7  script    API design · GraphQL · gRPC · WebSockets · webhooks · sockets · REST
 7  shortcut  the OS keyboard tables
 5  script    JSON ×3 · serialisation · URL encoding
 4  script    Kafka · Spark · pandas · OLTP vs OLAP
 3  quotes
 3  sec/threat  Security Basics in Plain English · Threats Explained Simply ·
                Everyday Security Hygiene
 2  script    HTML ×2       2  script  CSS ×2
 2  shortcut  browser       2  shortcut  DoD ×2
```

**Five of the eleven are `script`'s language-reference layer**, and every one of
them has a twin on the mainland it was never linked to: *GraphQL — Ask For
Exactly What You Need* sat in an island while *GraphQL on the Backend* sat in the
mainland; the same for WebSockets, for API design against *API-First &
Contract-Driven Design*, and for `OLTP vs OLAP`, which is a **recorded
near-duplicate pair** in `duplicate-verdicts.json` whose two halves had no link
between them. The layer was linked internally when it was written and never
connected outward.

**The one that matters most for a reader is the three-topic one.** The beginner
security layer offered a beginner *only the other two beginner cards*. Finish
*Security Basics in Plain English* and the site's entire core security layer is
one click away and is never mentioned.

### Sixteen bridges, each a pair that already belonged together

Not link-padding to move a metric: every bridge is a topic and its twin, or a
beginner card and the core card it introduces — `Security Basics` → *CIA Triad*,
`Threats Explained Simply` → *How Attacks Actually Work*, `Everyday Security
Hygiene` → *MFA* and *Passkeys*, `Serialization` → *SSRF, XXE & Deserialization*,
`Kafka` → *Message Queues* and *Streaming Pipelines*, `DoD` → the military staff
system.

```
components 12 -> 4 · mainland 1,432 -> 1,459 (96% -> 98%) · links 4,704 -> 4,736
```

### The three that remain, and why a gate would be wrong

`math` (16), the `shortcut` OS tables (7), `quotes` (3). Each is a whole
reference domain whose neighbours genuinely are its own kind, and each is
reachable by a learning path — *Calculus, Start to Finish* and *How to Think*.
Requiring every component to connect would mean **inventing** a "See also" out of
the calculus track, and an invented link is worse than a short strip.

So `orphan_report.py --islands` is a census and says so in its own output. It
sits beside the orphan count because they are the same question at two scales:
*can a reader get here*, and *can a reader get out*.

```
16 bridges · related 4,704 -> 4,736 links, still 0 one-way · 35 gates green
```

## Session — a change I made three waves ago put a hollow card back in the deck

Chasing a content×code interaction: the flashcard deck is built from parsed
topics, so a content edit can change what the study tools do without touching a
line of `script.js`. `script.js` already knows this and says so:

> Six topics outside `acronym` build a flashcard whose back is **completely
> empty** — `shortcut`'s *Windows*, *macOS*, *Terminal / Bash* and *VS Code*, the
> AI glossary, and the military code list. … There is no question a table of
> keystrokes answers, and turning one over reveals nothing.

`stIsStudyable` therefore excludes a topic with no `title` and no `desc`. Those
six were excluded by **shape**, which is the right unit — the next lookup table
somebody writes is excluded without anyone remembering.

**Then I gave the AI glossary a verdict.** Three waves ago, moving the EU AI Act
verdict off it and writing it one of its own. `desc` is parsed from the topic's
first `.concept-desc`, and a verdict carries that class — so the glossary
satisfied `title || desc` on the verdict alone and walked straight back into the
deck.

Confirmed in a browser rather than reasoned about:

```
ai-glossary-quick-reference   title: ""   desc: "A glossary exists to stop…"   studyable: true
common-codes-decoded          title: ""   desc: ""                            studyable: false
windows · macos · terminal-bash · vs-code                                     studyable: false
```

### The card it produced

The front is always `t.name`. The back's heading is `t.title || t.name`. With no
concept title, **both sides read "AI Glossary (Quick Reference)"** and the body
was a verdict about acronym collisions. A reader flipped it and was shown the
words they had just read.

The existing smoke check — *every studyable topic has something on the back of
its card* — passed, because there **was** something on the back. It asserts
`title || desc`, which is what `stIsStudyable` asserts, so it can only fail on a
whitespace-only field.

### Two fixes, and the second is the one that lasts

**The structure.** The glossary is now a proper `.concept-card` — label, title,
an introduction, the table in its `.dw`, then the verdict — like every other
topic on the site. That was the half of the earlier wave I left undone: I wrapped
its bare table in a `.dw` so search could highlight in it and stopped there.
The card now reads *"The Words You Will Meet in Every AI Conversation"* on the
back, which is an answer to the front rather than an echo of it.

**The assertion.** A new smoke check: **no card turns over to a heading that
repeats its front** — no studyable topic without a concept title. Currently 0 of
1,480. Proved by stashing the fix: `FAIL : ai/ai-glossary-quick-reference`,
151/152.

### What this is really about

Three waves ago's commit message claimed the verdict move was a clean fix, and
it was — for the reader of that topic. The cost landed in a subsystem the diff
never mentioned, and nothing failed, because the guard that existed asserted the
same thing the code asserted. **A check that restates the implementation cannot
catch the implementation being satisfied for the wrong reason.**

```
thin 11 -> 10 · smoke 151 -> 152 checks · 35 gates green
```

## Session — five places that said "see" and then made the reader go and look

`<span class="xref">` is the site's cross-reference: `build.py` resolves it to
the target's id and `.xref[data-xref]` renders a dotted-underline link. There are
501 of them and `lint_content.py` proves every one resolves.

Nothing had ever asked the other question: **is there prose that names a topic
exactly and is not one?**

Scanning all 35 domain files for any of the 1,353 topic titles of 28+ characters,
outside an existing xref, found **5** — and every one is a sentence that says
*see* and then names the topic:

```
endpoint      … see MECM Deployment & Content Troubleshooting in this domain
grc           … see Web Accessibility (a11y) — WCAG & ARIA in the Web domain
grc           … and Web Accessibility (a11y) — Building for Everyone in Scripting
math          … See Trigonometry — The Unit Circle, Identities & Inverses for the circle side
productivity  … Fold the cue answers into the Hansei prompts — see Hansei — The 15 Minutes…
```

Four were wrapped in `<strong>`. **Emphasis is not navigation**: the reader was
handed a title in bold and left to scroll a domain looking for it, while the
mechanism that would have made it a link was one span away. All five now resolve
— checked in the built page, not assumed: `506 of 506` content xrefs carry a
`data-xref`.

### The narrow version is 3× faster and finds the same five

The first check scanned every title against all prose: **2.6 s**, and it answers
a slightly different question, because a title can appear in a sentence without
the writer meaning to link it. Restricting it to the 240 characters after the
word *see* — the writer's own signal — takes **0.8 s** and finds the identical
five.

It had to stop reporting only the first title per *see*, though: `grc` names two
in one sentence, and the first version quietly found four.

The 28-character floor is the other half. Short titles — *Beginner*, *RAID* —
are ordinary English and would fire on every page.

### Two things this cost, both of which are the system working

Converting the `math` one changed a generated artefact: `gen_cheatsheet.py
--check` failed the build with *"CALCULUS-CHEAT-SHEET.md is out of date"*. The
cheat sheet is built from `math` content and I had edited it — exactly the gate
that exists because three generated artefacts once went stale unnoticed.

And my first conversion in `productivity` matched `<strong>Hansei</strong>`
somewhere earlier in the file rather than the full title, producing a
cross-reference to *"Hansei"*. The linter named it in the next run with the
correction: *did you mean 'The Japanese Mastery Loop — Kata, Poka-Yoke, Hansei,
Kaizen, Shokunin'?* Failure #2 in the operating manual is inventing a
cross-reference from memory; this is the same defect from the other direction —
a regex too eager — and the same tool caught it.

```
xrefs 501 -> 506 · lint fixtures 36 -> 41 · 35 gates green · 152 smoke checks
```

## Session — the one claim on the front page that nothing tested

Seven browser gates run against this repository — smoke, search, axe, visual,
resilience, mobile, backup — and **not one of them loads the service worker.**
`sw.js` is what makes the README's *"Offline-first"* true, and it was the only
user-facing claim on the front page with nothing behind it.

Two ways it breaks, and the first is worse than it looks.

**`cache.addAll()` is atomic.** One 404 in `PRECACHE` rejects the whole promise,
the install fails, and *nothing* is cached. A single mistyped filename does not
cost a font — it costs the entire offline mode, silently, on a site that still
works perfectly online. Nothing would ever look wrong to anyone with a network.

**An asset the page needs but does not precache** resolves from the network, so
it passes every test anyone runs and fails only for the reader who is offline.

Both are decidable from the files, so this needs no browser at all.

### The measurement came back clean, twice over

```
13 precached · 10 referenced · 0 missing on disk · 0 needed but uncached
```

Every precached path exists, and every asset the page or its stylesheets pull is
precached — including the three self-hosted `woff2` faces, whose URLs live in
`Img/fonts.css` and are relative to *the stylesheet*, not to the page.

### The false positive that shaped the rule

A first pass reported `/sha256(code_verifier` as an uncached asset. It came from
`url(` matching inside a card explaining **OAuth PKCE**. So a reference is
believed only if it also *looks like a file* — a path ending in an extension —
which is the same lesson as the two failed code-block heuristics: a pattern that
merely resembles the thing will find the prose that resembles it too.

### Proved by breaking it, in both directions

```
mistype one path      → 1 missing on disk, 1 needed-but-uncached, exit 1
drop /style.css       → 1 needed but uncached, exit 1
restore               → exit 0
```

Five fixtures cover the parsers — an off-site asset, a `data:` payload, a
fragment, prose that looks like a `url()`, and a stylesheet-relative font — plus
a guard that raises if the `PRECACHE` array itself stops being findable, so this
cannot quietly become a check that passes because it stopped looking.

```
gates 35 -> 37 · 13 precached paths verified both ways
```

## Session — the checker I wrote yesterday had the defect one file away

The precache check shipped clean: *13 precached · 10 referenced · 0 missing · 0
uncached*. Then I opened `site.webmanifest`, which is one of the files it
precaches, and read it:

```json
"icons": [
  { "src": "web-app-manifest-192x192.png", "sizes": "192x192" },
  { "src": "web-app-manifest-512x512.png", "sizes": "512x512" }
]
```

**Both exist on disk. Neither was precached.** The site declares
`"display": "standalone"` and offers itself for installation, and the icons an
install shows came from the network — so a PWA installed offline, or on a
connection that dropped at the wrong second, gets no icon. It is the one missing
asset a reader sees on **their own home screen**.

### Why the check missed it, which is the actual finding

It followed stylesheets into their `url()` references — because that is where the
fonts were, and the fonts were the case I was thinking about. A manifest is
exactly the same shape of problem: a precached file naming further files, with
paths relative to itself. The check knew about one nested reference type and not
the other.

**A checker's scope is where the next defect hides.** Not its logic — its logic
was right, and it correctly reported zero for everything it looked at. It simply
was not looking at a file it had itself listed as needing to be cached.

The widened version found both immediately, before `PRECACHE` was touched:

```
13 precached · 12 referenced · 0 missing on disk · 2 needed but uncached   exit 1
15 precached · 12 referenced · 0 missing on disk · 0 needed but uncached   exit 0
```

Four more fixtures — icons relative to the manifest, an off-site icon, a manifest
with no icons, and a manifest that does not parse — because a manifest that fails
to parse must yield *nothing* rather than crash a build gate.

### One thing deliberately not changed

`CACHE_VERSION` is hashed from `index.html`, `style.css` and `script.js`, so
editing `PRECACHE` does not move it. That is correct rather than a bug: the
browser byte-compares `sw.js` itself, installs the new worker because the file
changed, and `addAll` tops up the *same* named cache with the two icons.
Invalidating the cache would throw away 8 MB of correctly cached page to add two
PNGs.

```
PRECACHE 13 -> 15 · check_precache fixtures 5 -> 9 · 37 gates green
```

## Session — a security pass over the two places a reader's own data is rendered

Every other session here measures content. This one measures `script.js`, because
the site takes input in two places and nothing had been written down about
either: **notes** the reader types, and a **progress export** they import back.

Four paths, checked rather than assumed. All four hold.

**Search highlighting** builds `<mark>` with `createElement` and `textContent`
and splices text nodes with `createTextNode`. A query is never parsed as markup,
so `<img onerror=…>` in the search box is 32 characters that match nothing.

**Notes** render through a static `innerHTML` skeleton with the text going in via
`.textContent`, and the file already says why: *"Build the static skeleton with
textContent-safe DOM (no innerHTML of data)."*

**Every `innerHTML` interpolation.** Scanned all 45 assignment sites for a `${…}`
not wrapped in `esc()`: **13 hits, all safe.** Eleven are counts and clock
values. `areas` is built as `esc(a)` per `<option>`. `q.q` is a pre-rendered
quiz prompt whose data parts were escaped at construction — `esc(e[0])`,
`esc(e[1][0])` — which is the one case where reading the assignment alone is not
enough.

**The import.** An allowlist with per-type shape checks, not a merge: a key that
does not match a known prefix is refused and counted; SRS numbers are coerced,
bounded and rounded; flags are whitelisted down to the literal `"1"`; a note must
be a string and is truncated to `NOTE_MAX`. Nothing an imported file says can
create a key the site does not own.

### The one change: a character `esc()` did not escape

It covered `& < > "` and not `'`. That is **safe today** — grepping every
attribute it feeds found `0` built with single quotes, so an apostrophe cannot
break out of one. It is safe by a property of the surrounding code rather than
by the function, and the next single-quoted attribute somebody writes would be
the exception.

`'` is now in the set. `&#39;` renders as an apostrophe in text and in
attributes, so nothing on screen moves — confirmed across the full browser
suite: **152 smoke · 44 search · 29 axe · 63 resilience · 9 mobile · 2 visual ·
3 backup**.

### Recording a clean result, deliberately

Three other measurements this stretch also came back clean and are worth the
lines so nobody re-derives them: reading times span 210–1,426 chars per stated
minute, which is rounding on a label that says *rough*, not a bug; cross-domain
xrefs are 42% of 506 with every domain both emitting and receiving; and the only
duplicated flashcard titles are the three cloud playbooks and the three quote
collections, both deliberate shared shapes, with topic **names** — what the quiz
actually asks — unique across all 1,545.

```
esc() covers 5 characters · 0 unescaped interpolations · 0 unowned import keys
37 gates green · 301 browser checks green
```

## Session — the button that printed on every handout

`README.md` claims the site *"prints cleanly"*. Like the service worker two
sessions ago, nothing tested it: seven browser gates and not one of them
emulates print media.

Emulating it and asking what still renders:

```
on screen   #study-fab ✓   .filter-bar ✓   #search-input ✓   #back-to-top ✓
in print    #study-fab ✓   .filter-bar ✗   #search-input ✗   #back-to-top ✗
```

**`#study-fab-wrap` is `position: fixed`**, so it does not merely appear — it
pins itself to the first printed page, over the content, on every handout anyone
has ever printed. A sweep for anything else found nothing: it is the only fixed
or sticky element that survives, and the only interactive control besides the
topic headers, which print as headings and should.

### The codebase had already written down why this would happen

`style.css` hides print chrome by naming each thing — `.filter-bar`,
`.notepad-tab`, `#back-to-top`, `.topic-tools`, `.topic-chev`, `#snap-quote`.
The study FAB was added later and never joined the list.

Four hundred lines below, the print-pack block says exactly this, about itself:

> Hiding by child selector, not by naming each thing, **so a new header or panel
> added later does not silently start printing.**

That comment is a prediction. The block it is written in is immune; the block
that needed it is the one that failed.

### So the gate asserts the rule, not the list

`smoke_test.mjs` now emulates print and asserts **nothing fixed or sticky
renders**. That catches the next floating control without anybody remembering to
add a selector — which is the whole argument the other block already made.

Proved against the old stylesheet:

```
FAIL : nothing floats over the page in print — DIV#study-fab-wrap
152/153 checks passed
```

### A storage question, raised rather than decided

Auditing what the site stores, five keys are outside the progress export:
`theme`, `acro-density`, `seen-through`, `recent-topics` and two internal
migration flags. The last two are correctly excluded. Whether a **preference**
belongs in a file whose dialog says *"Export a file to move it to another
browser"* is a product decision, not a defect, and it is the owner's to make —
so it is written here rather than changed.

One thing did turn up along the way: `"theme"` is the only storage key written as
a bare string literal instead of a named constant, which is why an audit that
enumerated the constants did not see it at all.

```
smoke 152 -> 153 checks · 1 print rule · 37 gates green
```

## Session — the accessibility promise that was kept, and the detector that said otherwise

`README.md` makes two media-query promises. The last session found the print one
broken. This is the other: *"Respects `prefers-reduced-motion`."*

The first measurement said it was **worse than broken**:

```
no-preference   19 elements with a non-zero duration
reduce          82
```

Emulating the preference *tripled* the number of animated elements. That is not
a bug in the site. `style.css` carries the standard universal reset, which is
written as `animation-duration: 0.01ms !important` rather than `0` — because a
true zero can cancel an `animationend` event that page logic may be waiting on.
So under `reduce` **every element on the page** acquires a tiny non-zero
duration, and a detector asking *"does anything still have a duration"* answers
*more, everywhere.*

The question had to be whether anything still **moves**. Above 20 ms:

```
no-preference   25 perceptible · scroll-behavior: smooth
reduce           0 perceptible · scroll-behavior: auto
```

The promise is kept exactly. **This is the sixth detector this run to be wrong
before it was right**, and the fifth to be wrong by measuring a property that
merely correlates with the thing.

### Gated anyway, because a kept promise is the easy one to break

Two assertions in `smoke_test.mjs`: nothing animates for 20 ms or longer under
`reduce`, and smooth scrolling is off. Proved by changing the reset's `0.01ms` to
`999s`:

```
FAIL : reduced motion stops everything that moves — HEADER., DIV.header-inner, …
154/155 checks passed
```

The threshold is the interesting part of the check and the reason it is written
down: a future maintainer who "tidies" `0.01ms` to `0`, or who adds a transition
that beats the universal selector on specificity, gets told. A check for
`duration === 0` would have failed on the correct stylesheet and passed on a
broken one.

```
smoke 153 -> 155 checks · 37 gates green
```

## Session — the README understated the site's own best number

The README's headline design claim:

> Opening another releases the last, so the page costs **404 elements at rest
> instead of 92,330** and loads in a third of the time.

`page_budget.py` measures both: **475** and **140,926**. `page_budget.py`'s own
docstring says where the README's pair came from — *"92,330 → 404 measured at
1,080 topics"* — and the site has 1,545.

So this is the eighth stale number found this run, and the first that makes the
project look **worse than it is**. The ratio it sells is 228×. The real one is
296×, and it widens with every card added, because that is exactly what the
architecture is for.

### Not gated, and that is the decision worth recording

`content_elements` moves on **every content wave**. Gating an exact figure in the
README would mean a README edit in every content commit — which is not
discipline, it is the friction that produces stale numbers in the first place.
`dom_elements` is different (it grows per *domain*, not per topic, and the
domains-table check already fires when a domain is added), but the two live in
one sentence.

So the sentence adopts the convention this run already established for tool
docstrings, four sessions ago:

> The rest are dated on purpose — *"At 1,534 topics there were 1,549
> attributes"*, *"288 of 1,432 (20%) when this was written"* — and that phrasing
> is the reason they cannot rot. A snapshot says when it was taken; a bare number
> claims to be now.

It now reads *"475 elements at rest instead of 140,926 — measured at 1,545
topics, and the gap widens with every card added"*. That is true today, true in a
year, and needs no gate to stay true.

### Where the line actually falls

| Claim | Mechanism |
|---|---|
| Domains table, acronym count | **Gated** — they change when something is *added*, which is rare and deliberate |
| Topic and domain counts in `<meta>` | **Generated** — `build.py` substitutes `<!-- TOPIC_COUNT -->` |
| Element counts, timings | **Dated** — they move continuously, so the honest form is a snapshot |

Three mechanisms, and the choice between them is *how often the number moves*,
not how important it is. That is the rule the previous seven instances were each
missing.

```
README: 404 -> 475, 92,330 -> 140,926, both dated · 37 gates green
```

## Session — the notepad is tested three ways, and never the one it advertises

`README.md`: *"Notepad — Slide-out scratchpad backed by `localStorage`, **synced
live across your open tabs**."*

Three suites touch the notepad. `storage_denied_test.mjs` exercises it with
storage blocked — 15 references, the largest notepad coverage on the site.
`backup_test.mjs` round-trips it through an export. `a11y_test.mjs` scans the
open dialog. **Not one of them opens a second tab**, which is the only thing that
sentence claims.

Nothing had ever opened two.

### It works over `file://`, which is the part worth writing down

The obvious objection is that cross-tab sync needs a web server, and every gate
here runs against `file:///…/index.html`. It does not: Chromium treats `file:`
pages as one storage origin **and** still fires `storage` between them. Measured
before anything was built on the assumption:

```
localStorage shared across pages   "hello"
storage event key seen by the other  "__probe2"
```

So the test needed no server, no new fixture, and no change to how the suite
runs — just a second page in the context that already exists.

### My first probe said the feature was broken

```
storage event key seen by the other page: "timeout"
```

Because I `await`ed the listener promise in tab B *before* writing from tab A, so
the write happened four seconds after the wait had already given up. The feature
was fine; the harness was serialised wrong. **Seventh detector this run to be
wrong before it was right**, and the first whose fault was ordering rather than
the signal.

### The check, and proof it can fail

Driven through the UI rather than through `localStorage` — post a note in tab A
with the real compose box and the real POST button, then read tab B's rendered
list — because writing the key directly would test the listener and skip
everything that makes the note appear.

```
storage listener renamed → FAIL : the other tab's list did not contain it;
                                  its count reads "0 notes"     155/156
restored                 → ok                                   156/156
```

One thing the first version got wrong and is worth keeping in mind for any check
here: the failure detail printed on **success** too, so a passing run read
*"ok : … — list did not contain it"*. A detail string is for the failing case;
on a pass it should be empty or a fact.

```
smoke 155 -> 156 checks · 37 gates green
```

---

## Session — the site had thirty domains and nothing on how software is actually run

A reader asked for Agile. The right first move was not to write, it was to check
whether the corpus already had it under another name, and the check needed to be
run carefully enough to be believed.

### The audit, and the two terms that lied

```
grep -ic 'agile\|scrum\|SAFe\|XP' data/*.html   → hundreds of hits
```

Both false. `SAFe` matched **safe**, and `XP` matched **experience** and **expert**
— case-insensitive substring matching on a two-letter acronym is not a search, it
is a coincidence generator. Re-run with word boundaries in Python:

```
(?<![A-Za-z])term(?![A-Za-z])

Agile                 0        story point           0
Scrum                 0        SAFe                  0
user stor             0        extreme programming   0
epic                  0        planning poker        0
backlog refinement    0
```

Genuinely absent. Thirty domains, 1,545 topics, sixteen cards on being a manager
— and nothing on the working agreement the manager's team runs under.

### What the neighbours already owned

The gap was real but not empty around the edges, and writing without reading
first would have produced a duplicate with a different title. **Planning Without
Theatre — Roadmaps, Velocity & Honest Estimates** already carries *"Velocity Is a
Capacity Signal, and It Dies When Aimed At"*. So velocity-as-target is taken, and
the Agile card must not re-argue it. `near_duplicates.py --title` cleared all
three planned titles before a word was written.

### The acronym that could not be used

`data/acronyms.json` has exactly one meaning for `DoD` — **Department of
Defense** — and the annotator expands it everywhere. Writing *"DoD"* for
Definition of Done would have shipped a card reading *"DoD (Department of
Defense)"* in a paragraph about a checklist. The constraint was cheap to obey
once known: **write it out, never abbreviate it**, and the wave was planned
around that rather than around adding a second meaning nobody outside this topic
would want.

### The card

Three cards, and the shape came from the manifesto itself rather than from a
summary of it. The load-bearing observation is that each of the four values names
**two goods and ranks them**, and that the sentence saying the right-hand side
still has value is the sentence that gets dropped in every retelling. Read
without it, *"working software over comprehensive documentation"* becomes *"we do
not write things down"* — which is how an adoption arrives at no written
decisions, no plan finance can budget against, and a contract nobody may vary.

The third card is the one that earns the topic: what gets adopted (the events,
the iterations, the estimate, the team structure, the retrospective) against what
gets left behind (the decisions, the release, the conversation, the authority to
change scope, the mandate to change anything). It ends on the one question that
settles it — **can the team change what is being built?** — and on the position
that plan-driven is a legitimate way to run a project. The dishonest part is
keeping ceremonies that imply otherwise.

### The orphan the risk register predicted

```
orphan_report.py  →  1 deep orphan   [eng] agile-the-four-trade-offs-…
```

Exactly the failure the register names: a deep new topic lands unreachable
because the two navigation layers are hand-maintained. Five bidirectional
`related.json` links and one step in the *From Engineer to Manager* path, placed
before **Planning Without Theatre** because that is the order the ideas build in.

```
deep orphans  1 -> 0 · related 1,485 -> 1,486 topics · paths 1,571 -> 1,572 steps
mainland 1,459 -> 1,460 of 1,486 (98%)
```

### One thing worth copying

`related.json` round-trips exactly through `json.dumps(indent=2,
ensure_ascii=False)` but its keys are **not sorted**. Re-serialising with
`sorted()` produced a 3,926-line diff for a five-line change. Sorting a file
whose order carries no meaning still destroys the reviewability of every future
diff against it — preserve the order you found, and insert next to the neighbour
the new entry belongs beside.

```
1,545 -> 1,546 topics · 37 gates green · smoke 156 · search 44 · resilience 63
```

---

## Session — the two frameworks, and reading the neighbours before writing a word

Agile was one topic; the request was for the concept, and the concept is three:
the manifesto, the framework most teams are handed, and the method that is not a
framework. Written as three commits because each is a separate claim that can be
wrong on its own.

### Scrum, written as decisions rather than as a glossary

The temptation with Scrum is a list — three roles, five events, three artifacts —
which is what every summary already is and what no reader needs a fourth of. The
card is built on a different spine: **every event is a container for exactly one
decision**, and the failure is legible from the outside because you can name the
missing decision by what the meeting turned into.

```
Sprint Planning   why is this Sprint valuable?   → capacity arithmetic
Daily Scrum       do we change today's plan?     → status, read to the senior person
Sprint Review     what should the backlog be?    → a demo, applauded, changing nothing
Retrospective     which one thing changes?       → a grievance list, re-filed
```

The third card sorts six failure modes into **fatal** and **degrading**, because
the useful thing to know before spending political capital is which three
actually remove the feedback loop. All three fatal ones turn out to have the same
shape as the question the Agile card ends on — they remove the ability to change
what is being built while leaving the ceremony that implies it can.

### Kanban had to be written around what the site already knew

Three separate topics were already standing in this space, and none of them was
findable from a search for Agile:

```
[cs]      Little's Law & Queueing — Why the Wait Explodes Before the Server Is Full
[devops]  Value Stream Mapping — Find the Bottleneck
[devops]  DORA Metrics — Measuring Delivery Performance
```

The first draft of the flow card re-derived queueing and re-stated value stream
mapping's best line — *"waiting dwarfs working, and the fix is not typing
faster"* — in slightly different words. That is not a duplicate the near-duplicate
census would have caught: **the titles are unrelated, so only reading the
neighbours finds it.** The verdict was rewritten to name the actual distinction
instead:

> Value Stream Mapping answers this for a whole pipeline and finds the one
> constraint; a work-in-progress limit answers it inside a single team and needs
> no map — the limit *refuses* the work rather than measuring it afterwards. One
> is an exercise you run, the other is a policy that holds while nobody is
> running exercises.

Three cross-references out of one card, all to topics in other domains, is the
right density for a topic sitting on top of work the site had already done.

### The path was the point

Three topics that only link to each other are three topics. The wave ends with a
**Ways of Working** path that puts them in front of the material that decides
whether any of it survives a schedule — the queueing law under the limit, the
bottleneck map, then estimation, planning, goals and the two delivery-measurement
topics.

```
102 paths (+1) · 1,584 steps (+12) · 1,488 of 1,548 topics reachable
```

### What this wave is evidence for

The audit that opens a content wave has two halves and only one of them is
mechanical. **Does the term appear** is a grep, and a careless one lies — `SAFe`
matches *safe*, `XP` matches *experience*. **Does the idea appear under another
name** is not a grep at all; it is reading the topics a reader would land on
instead, and it is the half that changes what gets written. Both halves ran here;
the second one rewrote a verdict, moved a card's claim, and turned what would
have been a restatement into three cross-references.

```
1,546 -> 1,548 topics · 511 cross-references · 37 gates green
smoke 156 · search 44 · resilience 63 · axe 29 · mobile 9 · visual 2 · backup 3
```

---

## Session — asking the reader's question found the fourth topic and two wrong words

Three Agile topics were committed and the wave looked finished. It was not, and
what finished it was not a report — it was typing eighteen queries a real person
would type into the site's own search box.

```
user stories        1  ops/escalation-functional-vs-hierarchical…   ← wrong card
daily standup       1  career/remote-work-working-well-from-anywhere ← wrong card
standup             2  career/remote-work · eng/one-to-ones          ← not Scrum
our standups are useless   0
```

Three of the site's `query_probe.mjs` kinds, in one run, on a topic committed an
hour earlier.

### Kind 1 — the site said it in the other word

The Scrum card is the site's answer to *"our standup is useless"* and could not
be reached by the word **standup**, because the card only ever said *Daily
Scrum*. Fixed in prose, which the probe's rules call the right answer and better
writing anyway: the events table now reads *Daily Scrum (the daily standup)* and
the verdict opens *"the standup, or stand-up, in every team that has never read
the guide"*.

```
standup        2 -> 3   (now reaches Scrum)
stand-up       1 -> 2   (now reaches Scrum)
daily standup  1 -> 2   (now reaches Scrum)
```

The line between this and keyword stuffing is worth stating, because the same
edit could be either. **Naming the thing the way readers name it is writing;
rewording a sentence so a matcher's proximity window closes is stuffing.** *Daily
Scrum (the daily standup)* is what the meeting is actually called in every team
that has one. `terraform state locked` is still deliberately zero for the other
reason.

### Kind 2 — the question was real and the card was not there

`user stories` returned one hit and it was about escalation handovers. The
word-bounded audit confirmed it:

```
user story  0 · vertical slice  0 · INVEST  0 · three amigos  0
Gherkin     0 · walking skeleton 0 · grooming 0 · acceptance criteria 5 (grc, career)
```

So the wave had covered the manifesto, the framework and the method, and skipped
**the unit of work all three operate on**. The fourth topic is the splitting
skill: what a story is (a promise to have a conversation, with acceptance
criteria as the actual contract), how to cut one (vertically, six patterns), and
the payoff — that a team whose items are all roughly the same size can forecast
by counting and stop needing the estimate at all.

That last claim is the one worth the card. Getting better at estimating is a
decade of work with a known ceiling; getting better at cutting is visible in a
quarter and improves the forecast as a side effect.

### The gate caught a real defect in the new card

```
FAIL : an exported table cell cannot be swallowed as raw HTML
       eng: The template — _As a <role>, I want <capability>, so that <r
```

The story template is written with angle brackets, so the Markdown export emitted
`<role>` as bare markup — a renderer would eat it and the reader would get *"As
a , I want , so that "*. The check exempts backticked spans, and the site's
exporter maps `<code>` to backticks, so wrapping the template fixed it properly
rather than by rephrasing around the gate.

**This is what the smoke suite is for.** The card looked right in the browser,
read right in the print pack, and was broken in exactly one of the five output
paths — the one nobody looks at while writing.

### INVEST, added to the dictionary rather than spelled out

`INVEST` was absent from a 1,101-entry acronym dictionary. Added, which
`check_acronyms.py` accepts because the letters are a subsequence of
*Independent, Negotiable, Valuable, Estimable, Small, Testable*.

One thing this changed about the prose: the first draft read *"the six INVEST
properties"*, and the annotator turned that into *"the six INVEST (Independent,
Negotiable, …) properties"* — an expansion wedged mid-phrase. Reworded to *"the
six properties named by INVEST"*, so the injected span lands at the end of the
sentence where a parenthesis belongs. **An annotated corpus rewards writing
acronyms in positions where a parenthetical can follow them**, and that is not a
constraint you notice until you read the built page rather than the source.

### What the wave is evidence for

The content audit that opens a wave asks *does the term appear*. This one asked
*what does a reader get when they type it*, and that question found a missing
topic, two unreachable cards and a broken export — after three commits that all
passed every gate.

```
1,548 -> 1,549 topics · 1,101 -> 1,102 acronyms · 513 cross-references
102 paths, 1,585 steps · related 1,489 topics, 4,776 links · 0 deep orphans
37 gates green · smoke 156 · search 44 · resilience 63 · axe 29 · mobile 9
```

---

## Session — the matcher was eating contractions, and two verdicts were wrong because of it

The Agile wave ended by typing reader queries into the search box. One of them,
`agile isn't working`, returned a single card about on-call pager duty while
`agile not working` returned eight including the right one. That gap is not about
Agile at all.

### The defect

`WIDE_STOP` is the short list of function words the all-your-words fallback must
not insist on — every word in that stage is a hard requirement, so a question's
`we`, `the` and `is` would otherwise narrow the result to nothing. The list had
`is`, `not`, `will`, `did` and `can`. It did not have `isn't`, `won't`, `didn't`
or `can't`, because those are different strings.

So a reader typing the way readers type got their contraction promoted to a
content word:

```
laptop won't turn on        0     laptop will not turn on     25
certificate didn't renew    0     certificate did not renew   15
why won't my vpn connect    0     why will not my vpn connect 22
dns isn't resolving         0     dns not resolving            3
```

Four of seven realistic contraction queries returned **nothing**, and their
spelled-out twins returned fifteen to twenty-five cards. The corpus was fine
every time.

### Two recorded verdicts were wrong

`laptop won't turn on` and `outlook won't connect` were both sitting in
`query_probe.mjs` with a `keep` note reading *kind 3 — the answer is written out,
only the phrasing is absent*. They were nothing of the kind. Removing four
characters from either query returns twenty-five cards and two cards
respectively; the phrasing was never the problem.

That is the second time this file's kind-3 category has been used to close a
question that deserved a fix, and the correction is now written into it as a
rule:

> **A kind-3 call is a decision not to write something, and it is only sound once
> the matcher has been ruled out.** Retype the query with its contractions
> expanded, and with its rarest word alone, before concluding the corpus is at
> fault.

### The fix, and why it is a list rather than a rule

Membership is now tested against the *folded* word, so `won't`, `won’t` and
`wont` all arrive as `wont` and one entry covers the straight apostrophe, the
typographic one a phone substitutes, and the reader who omitted it. `’` was
added to `RE_INTRAWORD` for the same reason.

The entries are hand-picked, and that is the interesting part. A mechanical rule
— strip the contraction, check the base — looks obviously right and is wrong on
this site:

```
I'd  -> id      and the site is full of Entra ID, user IDs, IDs
I'm  -> im      instant messaging
I'll -> ill
we'd -> wed
```

Silently dropping `id` from `entra id` would be a worse bug than the one being
fixed. The list keeps only the folded forms that are *never* anything but
function words, and `entra id` is now a gate fixture standing guard over exactly
that.

`vs` and `versus` joined them separately. The site titles a dozen topics *X vs
Y*, so the as-typed pass answers those before the fallback runs — but `agile vs
waterfall`, which no single card contains verbatim, was requiring the literal
word `vs` and returning nothing. Both directions are now fixtures, because the
change is only safe if the second one keeps passing.

### The census had the same blind spot the gate had already fixed

`standups` returned one card about remote work and `query_probe.mjs` scored it
**answered**. Counting results is not a test of whether the reader got what they
asked for — which is exactly what `search_test.mjs` learned when *three way
handshake* "started working" by returning three loosely-related cards and not the
TCP one. It grew a third field naming the wanted topic; the census had not.

It has one now. `want` is optional and filled in as queries are revisited, and
where present it flips the verdict:

```
before   ok    "standups"   1  career/remote-work-working-well-from-anywhere
after    kept  "standups"   1  kind 3 — the singular reaches the Scrum card…

78 queries · 72 answered · 5 found nothing · 1 found the wrong card
```

Both new paths were proved by breaking them: a bogus `want` on `scrum` produced
`MISS … wanted eng/nonexistent-topic-that-proves-the-check` and an unexplained-miss
report, and removing `wont` from the stop list dropped the search gate to 47/49.

### The rule this run adds

Three sessions in a row have now found the same shape: **an instrument that
scores by counting will call a wrong answer a right one.** The duplicate census
counts pairs, the orphan report counts links, the query probe counted hits. Two
of the three have since learned to name the thing they expected. The third —
`near_duplicates.py` — is the one left, and it is worth knowing that before the
next session trusts it.

```
search 44 -> 51 checks · probe 66 -> 78 queries · 37 gates green
smoke 156 · resilience 63 · axe 29 · mobile 9 · visual 2 · backup 3
```

---

## Session — I built the detector the last session asked for, and it should not ship

The record above ended on a rule: *an instrument that scores by counting will
call a wrong answer a right one*, and it named `near_duplicates.py` as the last
one that still does. Acting on my own finding meant building something. Most of
this session's value is in why the thing I built is not in the repo.

### What a sharp signal would have to look like

Body-similarity scoring is the obvious idea and the obvious trap: over 1,549
topics, shared vocabulary fires everywhere, and this file's oldest rule says a
plausible detector that fires broadly is the instrument being wrong. The version
worth testing is the one whose signal a language's grammar makes near-impossible:
**a long verbatim phrase in two topics.** Two independently written cards do not
produce the same fourteen-word sequence by accident.

```
N=8   prose+code   1,625 shared grams · 3,136 pairs     ← unusable
N=10  prose only     346 shared grams · 1,089 pairs
N=12  prose only     130 shared grams ·   701 pairs
N=14  prose only      49 shared grams ·    24 topic-sets
```

Forty-nine phrases is a list a person can read. So I read it.

### The two loudest findings were both the instrument

**First:** one 14-gram appears in **34 topics** —

> *"You can't make someone make the right choice — but you can pick up the
> pieces"*

That is a house maxim, deliberately threaded through the site, and three of the
34 write it *"yet you can"* instead. Not duplication. The detector's strongest
signal was the corpus working as designed.

**Second:** a phrase shared by a career negotiation topic and a Druidism topic —

> *"15 card bar they split three ways rather than folding to one home which"*

Which is not prose at all. It is an **HTML comment**:

```html
<!-- Four cards did not clear the >=15-card bar. They split three ways
     rather than folding to one home, which is why this took a decision. -->
```

`re.sub(r"<[^>]+>", "", …)` stops at the first `>` it meets, so the `>` in
`>=15` ends the tag early and the rest of the comment becomes plain text. My
extractor read a bookkeeping note as card content in two domains.

### The real question that opened

Sixteen tools in this repo strip markup with that exact regex. So: **is any
shipped number wrong?**

Three comments in the corpus contain a `>`. All three sit *between* topics —
`career.html:1397`, `philosophy.html:1272`, `philosophy.html:1808`. Nothing
measures them, nothing indexes them, and `folded in from the former` and
`did not clear the` both return zero results in the live search. No number on
this site is wrong.

But it is wrong **by luck**. One comment written inside a card body with a `>`
in it would move `depth_report`'s character counts and `near_duplicates`'
overlap scores — two numbers that appear in the measured-state table at the top
of this file — with nothing anywhere to say it had happened.

### One gate instead of sixteen hardenings

The fix is not to teach sixteen regexes about comments. It is to make the
condition that breaks them impossible: `lint_content.py` now fails on a comment
inside a `.topic` containing `>`. A comment that cannot contain `>` cannot break
any stripper, present or future, and the correction is always trivial — write
*at least 15* or `&gt;=15`.

Getting the scope right took a fixture failure. `topic_blocks()` runs from one
topic's line to the *next* topic's line, so its tail holds precisely the
between-topic comments that are fine — the first version flagged all three real
ones. The check now balances divs from the opening tag to find the element
itself, which `check_markup.py` already guarantees is balanced.

```
fixture "outside a topic, where nothing measures it"  found 1, expected 0
after balancing                                       46 fixtures, 0 failures
in-card comment planted in eng.html                   eng.html:6388  exit 1
removed                                               clean
```

### Why the detector itself is not checked in

Strip the house maxim and the comment artifact and the residual is about three
pairs of genuinely reused sentences — two BCP/DR cards sharing an
RTO/RPO definition, a printers card and a media-sanitisation card sharing a line
about leased drives. Real, minor, and already inside `near_duplicates.py`'s
existing reach by title.

So the honest answer to the last session's rule is: **the sharp version of a
body detector finds one deliberate device, one bug in itself, and three pairs
worth a shrug.** A tool checked in for that yield teaches the next session to
skim its output, which is worse than not having it. What survives is the
measurement, written down here so nobody spends another session deriving it, and
one gate on the defect the measurement actually found.

The lesson generalises past this repo. *An instrument that finds nothing is a
result.* Reporting it as one — rather than lowering the threshold until it finds
something — is the difference between a census and a horoscope.

```
lint 41 -> 46 fixtures · 37 gates green · smoke 156 · search 51 · resilience 63
```

---

## Session — eighty topics highlighted nothing, and the wrapper was never the point

The depth census flags ten thin topics. Chasing the first one did not produce a
deepening wave; it produced a reader-facing search defect that had been shipping
for as long as the highlighter has existed.

### The thin topic was not thin

`linux` *Package Management*, 933 chars, one concept card. Reading its seven
siblings settled it in a minute:

```
1090  cards=2  [Linux+ • FHS]       Filesystem & Navigation
 444  cards=2  [Linux+ • CLI]       File Ops & Text Processing
1188  cards=2  [LINUX • Security]   Permissions & Ownership
1023  cards=2  [Linux+ • IAM]       Users, Groups & Privilege
1100  cards=2  [Linux+ • A+]        Processes & Services
 933  cards=1  [Linux+ • Distros]   Package Management   ← "thin"
 514  cards=2  [Linux+ • Net]       Networking (CLI)
1246  cards=3  [Linux+ • SecOps]    Shell, Cron & Hardening
```

A deliberately short Linux+ quick-reference series, and the flagged member is
mid-range for it. The thin rule is *one card AND under 1,800 chars*, and this
one trips it only because its second block is a table rather than a card.
Nothing to deepen. **A census row is a question, not an instruction**, and the
answer here was "the series is the unit, not the topic".

### But the shape it had was a real bug

That table sits directly in the `.topic-body`, which `lint_content.py` has a
check for — and the check did not fire, because its regex only matches a table
*immediately* after `<div class="topic-body">`. This one follows a closed
`.concept-card`. Same defect, invisible shape.

Balancing divs across the whole corpus:

```
1,549 topics · 80 with a table outside every highlightable wrapper
```

The first version of that analyser said **0**, because its wrapper stack popped
on the wrong condition. Worth noting only because the correct answer and the
comfortable answer were one buggy loop apart, and 0 is the answer that ends the
investigation.

Then the browser, because a static count is not evidence about a reader:

```
search "pacman"   →  topic opens · 0 marks · 0 in the table
search "flatpak"  →  topic opens · 1 mark  · 0 in the table
```

`pacman` occurs exactly once in that topic, in a table cell. The page found it,
opened the topic, and marked nothing.

### The wrapper was never the point

The obvious fix is to wrap all 80 in `.dw`. The reason not to is one line of CSS:

```css
.dw { padding: 0 18px 18px; }
```

That is the whole of `.dw`. The highlight list was the only thing making it
structural, and **coupling "can be highlighted" to "has a padding wrapper" is
the bug**, not the 80 topics that failed to observe it. `table` went into the
highlight list. All 80 fixed, and every future one, with no content edited.

That has a hazard: a table nested inside a `.dw` is now visited twice, and the
second pass would wrap already-marked words again. `highlightIn()` is now
idempotent — text inside a `mark.sh` is rejected by the tree walker — which is
worth having on its own terms, and the failure it prevents is not theoretical:

```
guard removed →  FAIL : 48 marks, 15 nested
table removed →  FAIL : 0 mark(s) in the table
both restored →  159/159
```

### What the check becomes

`bare_tables` was introduced with the words *"Not a style rule"*. After this it
is one — the highlight argument now lives in `script.js` and is gated from the
reader's side in `smoke_test.mjs`, and what remains is eighteen pixels of
padding. Its docstring says so, in place of the old argument, and the check is
deliberately **not** widened to the 80: failing a build over padding is exactly
the style-rule-in-correctness-clothing this file warns about two sections up.

There is a general shape here worth keeping. **When a check's real justification
is fixed at the source, the check does not automatically become worthless — but
it does become a different check, and leaving the old reasoning in the docstring
is how a style rule keeps borrowing a correctness rule's authority.** Rewrite the
reason or retire the check; do not leave it quoting an argument that no longer
holds.

```
smoke 156 -> 159 checks · 80 topics now highlight their tables
37 gates green · search 51 · resilience 63 · axe 29 · mobile 9
```

---

## Session — the thin list was seven-eighths short on purpose

Having found the census's blind spot from the outside last time, this session
read all ten thin topics rather than deepening the first one. Two got cards. The
other eight are the finding.

### What the ten actually were

| | Topic | Why it is short |
|---|---|---|
| ✓ | `script` Building a REST API | **Genuinely under-served** — a FastAPI hello world and nothing on what to return |
| ✓ | `endpoint` Update Compliance Reporting | **A card missing** — the four-source map with no reconciliation step |
| | `military` Common Codes Decoded | Beginner reference card, one of a series |
| | `military` Staff Functions 1–9 | Same series |
| | `linux` Package Management | Member of an eight-topic Linux+ quick-reference run, mid-range for it |
| | `redteam` Rules of Engagement | The domain's authorised-use preamble. A wall of text is a disclaimer nobody reads |
| | `data` The Data Interview | Lookup table |
| | `eng` Cert Roadmaps | Lookup table |
| | `web` The Full-Stack Picture | A deliberate zoom-out at the end of a domain |
| | `devops` Software Supply Chain Security | An overview whose job is to route into `eng`'s eight-topic supply-chain series — and it already carries the cross-reference that does it |

Two of ten. **The thin count is not a queue**, and no session should treat it as
one without reading the rows.

### The two that were real

*Building a REST API* taught how to start a FastAPI server and stopped. The
consuming side of the same subject is three topics deep — auth, pagination,
retries, 429 — while the serving side had no status codes, no error shape and no
operational traps. Two cards, and the first one gets to correct the topic's own
example: it returns `200 {"created": …}` from a POST, which works and is wrong.

The trap card's second row is the one worth having written down: **`async def`
is a promise that nothing inside the function blocks**, and one ordinary
synchronous database driver breaks that promise for every concurrent request on
the process rather than just its own.

*Update Compliance Reporting* had the four-source map and not the thing anyone
actually does with it — reconciling two dashboards that disagree. Denominator,
then clock, then definition, in that order, because every later comparison is a
ratio against the first. And the row that resolves most arguments: a device that
has installed a patch and not rebooted is running the vulnerable code, so Intune
reporting success and the scanner reporting a hole are both correct.

### What the census learned

Not a threshold change — the threshold is right, and eight of the eight
remaining are correctly *short*. What was missing is that the report gave a
length and a title, so classifying the list cost nine file reads. It now prints
three facts the block already carries:

```
 chars  domain         #  xref  badge                  title
   317  military       8     0  Military • Reference   Common Codes Decoded
  1134  redteam        0     0  Ethics                 Rules of Engagement — Read This First
  1769  devops        32     1  Supply Chain           Software Supply Chain Security — SBOM …
```

`#0` reads as a preamble at a glance. `xref 1` reads as an overview that routes
onward. A run of short topics sharing a badge prefix reads as a series. None of
the three decides anything, and the footer says so — *the columns are context,
not a verdict.*

That restraint is the point and it is the opposite of the last two sessions'
fixes. The query probe and the search harness both got a field that **changes
the verdict**, because in both cases the tool could know the right answer and was
not being told it. Here the tool cannot know: whether a 475-character card is a
lapse or a deliberate reference row is an editorial judgement, and a classifier
that guessed would be a plausible detector firing broadly — the thing this file
has warned about since the beginning.

**Give the instrument a verdict field when it can be right. Give it context
columns when only a person can be.** Deciding which of the two a case is, is the
whole skill.

```
1,549 topics · thin 10 -> 8 · 515 cross-references · 37 gates green
smoke 159 · search 51 · resilience 63 · axe 29 · mobile 9 · visual 2 · backup 3
```

---

## Session — twenty-four matches in twelve domains, and no way to tell which one

This site renders one domain at a time. That is its architectural bet and it is
the right one — 475 elements at rest instead of 140,926. The cost lands on
search: a query answered in twelve domains gives the reader twelve badged chips
and no reason to prefer any of them. Typing `agile` returns 24 cards across 12
domains, and the topic actually called *Agile* is one of them, unmarked.

### The measurement that shaped the feature

Over the 85 standing queries in `query_probe.mjs`:

```
85 queries
  15 have a topic whose slug carries every content word
   5 of those spread across 3+ domains — the reader has to guess which
  61 have hits but no slug match — nothing to point at
```

Five of 85 is six percent, which sounds like nothing until you look at which
five: `agile` (24 hits, 12 domains), `chain of custody` (9 in 8), `what is an
embedding` (16 in 6), `third party risk` (5 in 3), `how do adults learn` (6 in
4). **They are precisely the queries where the reader is most lost**, and in all
five the topic named after the query is the one they wanted.

So the feature is one line under the search bar — *The site has a topic called
…* — linking to it. `openHashTarget()` already opens the domain, reveals the
topic, scrolls and moves focus, so the whole thing is an anchor with the right
`href`.

### The loosening that looked principled and was wrong

The strict rule is: every content word of the query appears in the topic's slug,
and **exactly one** topic qualifies. That declines `kerberos`, `subnetting` and
`what is technical debt`, where several topics carry the word.

Breaking ties by preferring the slug that *starts* with the query is the obvious
next step, reads as principled, and buys two more:

```
what is idempotency   3 candidates → idempotency-exactly-once-safe-retries   ✓
what is an embedding  2 candidates → embeddings-rag-giving-ai-access-to-…    ✗
```

The second is wrong. A reader asking what an embedding *is* wants the vectors
and cosine-distance card; the tiebreak picked the retrieval one because its title
happens to begin with the word. **A pointer that is right half the time is worse
than no pointer**, because the reader cannot tell which half they are in and
stops reading the line. Kept strict. `what is technical debt` staying silent
between the craft card and the financial-argument card is the rule working.

### Where it lives, and why not in the counter

`.search-count` is a 60-pixel `nowrap` counter pinned to the right of the input.
A topic title in it pushes the search box off a phone. The line is its own row
under the bar, **built on demand and removed when it has nothing to say**, so the
at-rest DOM is unchanged — still 475 elements, which is the number the README
sells the architecture on.

### What it turned up on the way out

Checking the new row at 375px found something that is not the row's fault and is
worth more than the row:

```
no search                    0px past 375
search "kerberos"            0
search "subnetting"          0
search "third party risk"   98   ← SPAN.chevron
search "raid"              238   ← a TBODY
```

Two of five searches scroll a phone sideways, identically with the new row
removed. `mobile_test.mjs` passes 9/9 because **it opens domains and never
searches**, and searching is a different layout: topics that were collapsed are
forced open, so tables that never rendered on a phone suddenly do.

A gate that tests the state nobody is in is the running theme of this whole run,
and this is the fourth instance. Next wave.

```
smoke 159 -> 163 checks · 37 gates green · search 51 · dom at rest 475
```

---

## Session — fifty-two of eighty-five searches scrolled a phone sideways

The last record ended by noticing this and calling it the next wave. It took one
measurement to find and one media query to fix, and the interesting part is
neither.

### The measurement

```
85 standing reader queries, rendered at 375px
  52 scroll the page sideways
  overshoot clusters at 198–223px, almost never anything else
```

A number that constant is one element, not a content problem. Ruling out the
obvious first: opening every topic in five domains **by hand** overflows by 0px.
So it is not tables, not code blocks, not the deferred content — it is something
search does that browsing does not.

### Two false leads, both my own instrument

The first probe named `DIV.filter-inner` at 3,890px wide. That is the domain chip
strip, which lives inside an `overflow-x: auto` parent and scrolls correctly —
my "widest element" search had simply not asked whether anything contained it.

The second, with containment checked, named `DIV.notepad-panel` at right=750.
Also wrong: the off-canvas panel is parked past the right edge and clipped, and
it is there identically when nothing is being searched and the overflow is zero.

The answer was the third row, and the arithmetic gives it away:

```
search "wifi keeps dropping"   over=198   SPAN.search-count  right=573   573-375 = 198
search "raid"                  over=238   SPAN.search-count  right=613   613-375 = 238
```

**Exactly the overshoot, every time.** When a number matches to the pixel, stop
looking for a second cause.

### The bug

`.search-count` is `white-space: nowrap`, which is right for what it usually
holds — *"9 matches in 3 domains"* should not wrap mid-phrase beside the input.
But the same element also carries the long branches:

> `no exact match, so these contain all your words`
> `also matching "Transmission Control Protocol"`

345 pixels of unbreakable text in a 375-pixel viewport, inside a flex row that
was not allowed to wrap. Below 600px the row wraps now and the counter takes its
own line, left-aligned, where there is room for it. 52 → 0.

### The part worth keeping

`mobile_test.mjs` has passed 9/9 for as long as it has existed, and its docstring
is precise about what it does: opens a spread of table-heavy domains, expands
every topic, measures. **It never types.** Browsing and searching are different
layouts and it only ever tested the first.

That is the fourth instrument this run to be measuring the state nobody is in:

```
query_probe    counted hits, so one wrong card scored as answered
search_test    fixed that years ago with a wanted-topic field — the census had not
lint_content   the bare-table check saw one shape of a defect that had two
mobile_test    tested browsing, on a page whose other half is searching
```

None of the four was wrong about what it measured. Each was wrong about what a
reader does. **The generalisable question is not "does this check pass" but
"which of the reader's states does it never enter"** — and it is answerable in
about a minute per tool, which is much cheaper than it sounds and has now found
four real defects.

The new pass picks its queries by the *shape of the message* rather than the
subject — one that widens, one that lists acronym alternates, one with an
operator scope, one that finds nothing — because a subject-based list drifts with
the corpus while the branches that write to that element do not.

```
mobile 9/9 -> 14/14 · 52 overflowing queries -> 0 · 37 gates green
smoke 163 · search 51 · resilience 63 · axe 29 · visual 2 · backup 3
```

---

## Session — the question found three more, and one of them was a typo

The last record turned an accident into a question: **which of the reader's
states does this check never enter?** Asked of the four remaining gates, it
answered immediately for `a11y_test.mjs`, whose docstring is admirably precise
about its coverage — the shell, an open domain with an expanded topic, a study
dialog, in both themes. Not a page mid-search.

Searching builds elements that exist in no other state: `mark.sh` highlights
inside prose, code and tables; the see-also strips and note composers that open
with each matched topic; the per-domain match badges; and, as of two records
ago, the named-topic link. None of it had ever been scanned.

Adding one line — `runSearch("agile")` before a scan — turned up **three real
contrast failures**, in three layers.

### One: the code-comment colour was already failing

```
.code-block .com   #4a6080 on #070c18   3.05:1     — under AA for normal text
```

Not a search bug at all. It has been failing since the colour was chosen, and
the a11y gate never saw it because the topic it expands happens to contain no
code comments. Searching opens topics that do.

One value cannot serve both grounds — `#4a6080` is a comfortable 6.13:1 on the
light code block — so it is two now, `#6b83a8` in dark at 5.06:1.

### Two: the highlighter made what it found harder to read

```
mark.sh { color: inherit }   dim comment on the mark's tint   1.80:1
```

`inherit` hands a highlight the contrast of whatever text it wrapped, so
marking the dimmest thing on the page produced the least legible thing on the
page. **A search that makes its own hit harder to read is worse than one that
misses it.** Stated explicitly now: 9.8:1 dark, 14.3:1 light, whatever it wraps.
The cost is a marked word losing its accent colour for the seconds it is marked,
which is the right trade.

### Three: a variable that does not exist

```css
.domain-matches { color: var(--bg1); background: var(--accent); }
```

**There is no `--bg1` on this site.** The three are `--bg`, `--bg2`, `--bg3`.

This is the one worth internalising, because CSS handles it in the worst
possible way: an undefined custom property with no fallback makes the
declaration *invalid at computed-value time*, which does not fall back to the
property's initial value — it **inherits**. So the badge quietly took the domain
header's light text and drew it on a bright accent, failing contrast on ten of
the thirty domains, and looked entirely deliberate while doing it. No console
warning, no missing colour, no visual "something is broken" — just a plausible
wrong answer, in a state nothing scanned.

Fixing the name left exactly one accent of thirty still short: `.domain-eng` at
`#6366f1` gives 4.46:1, four hundredths under. Three steps lighter to `#7173f4`
clears it at 5.18 — and lifts the same accent's contrast *as text* on `--bg2`
from 4.20 to 4.88, a second reading that was also under AA and that nothing had
asked about.

### The gate, and why static is the right shape

`a11y_test.mjs` now finds this class of bug in the states it visits.
`check_css_vars.py` finds it in every rule in the file, whether or not anything
renders it today, and it is the sharp kind of signal rather than the plausible
kind: **a name is declared somewhere in the file or it is not.** No threshold,
no score, nothing for a reader to overrule. A `var(--x, fallback)` is exempt —
naming a fallback is how you deliberately read a maybe-unset property, which
`var(--accent, var(--cyan))` does thirty times over.

Scoped to `style.css`, because `data/*.html` contains `var(--gap)` and
`var(--spacing-md)` inside code samples that *teach* custom properties, and
flagging a teaching example would be the instrument being wrong about what it is
reading.

One fixture was written expecting 0 and corrected to 1 when the check disagreed,
because the check was right: in `var(--b, var(--c))` the innermost name is the
one with nowhere left to fall back to, and if neither is declared the
declaration can never resolve.

### And a dead block, deleted with proof

The same sweep found `var(--text-muted)` inside a `[data-domain="mental-disorders"]`
block — a domain that does not exist, under a `body.light` selector this site has
never used. Dead twice over, 23 lines. `style_equiv.mjs` compared 153,187
elements across all thirty domains against the previous commit and found exactly
two changes, both intended:

```
650 × rgb(74,96,128) -> rgb(107,131,168)     the comment colour
  9 × rgb(99,102,241) -> rgb(113,115,244)    the eng accent
```

Nothing from the deletion. That is the tool doing precisely what it was built
for, and it is worth remembering it exists: **a refactor with a proof attached
is a different object from a refactor.**

```
gates 37 -> 39 · axe 29 -> 31 scans · lint 46 fixtures · css-vars 7 fixtures
smoke 163 · search 51 · resilience 63 · mobile 14 · visual 2 · backup 3
```
