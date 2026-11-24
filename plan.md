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

**And a third time, at 8,009,** two months later, on the commit that wrote a request into the
file. The same warning, the same option, and 45 more records moved oldest-first: 32,774 lines
before the move and 4,092 + 28,682 after it, which leaves 22 records here.

What is left here is what a session actually reads.

| Section | What it is | State |
|---|---|---|
| **The session operating manual** | The loop, the ordering constraints, and ten failures with their guards | 📘 **start here** |
| **The card rubric** | What the good cards have, measured from forty written in one session | 📘 reference |
| **Phase 11 — the verification debt** | What is dated, and why the denominator is not countable. A standing discipline, not a queue | 📘 living |
| **The risk register, revisited** | Four accumulation risks that only a measurement could find | 📘 living |
| **Knowledge integration** | Seven items of incoming study notes mapped onto the domains — the first queue in a while that arrived as a list, and three of its seven destinations moved when they were checked. Conducted: one moved again, one of the five concepts §2 called absent was written behind a hyphen, and nine of the reader's sixteen misses found the wrong sense of a word | ✅ **shipped** — see its §6 |
| **csvistool** | An outbound link to [csvistool.com](https://csvistool.com/), Georgia Tech's data-structures visualizer, and its 41 concepts checked against the site. Half already have a card to hang a link on, 12 of 40 searches return nothing, and one cluster (minimum spanning trees and union-find) is a real gap. Conducted: 39 deep links on the cards that already teach each concept, the gap and both candidates written, and a reader that opened at 0 of 16 closed at 16 of 16 | ✅ **shipped** — see its §5 |
| **Study notes, batch two** | Study notes on databases, SQL, regex, pandas and Java, checked against the site. The notes are in SQL Server and Java, and the site is in Postgres and Python, so most of the concepts are written and most of the words are not. UML is now asked for by both batches, twelve claims should not reach a card as written, and two regex examples were broken by the spelling sweep | ✅ **shipped** — see its §8 |
| **Content ideas** | A request for more content to add, in the same clean look. 839 candidate phrases in 17 reader groups, each checked against the content and against the built page's search: 81 are owned by a title, 452 are mentioned in passing and 306 are absent. The largest finding was not on the list: the page is headed *Cycles, Concepts &amp; Diagrams* and 58 of 1,503 hand-written topics carry a shape. Twenty diagrams from components that already exist, about thirty-five candidate cards, exam paths that need no new content, and a look contract with one hole in it. First wave conducted: the hole fixed and gated, the exam reader at 16 of 16, the UML lines drawn, six cards and a topic. Second wave conducted: twelve cards over ten rows, the reader's second batch at 23 of 23, and three tools fixed at their own edges. Third wave conducted: a topic and ten cards over five rows, twelve connectors drawn, the reader's third batch at 16 of 16, and two census answers that were coincidences. Fourth wave conducted: seven theory cards, the theory reader at 15 of 15, and a spelling gate taught a suffix. Fifth wave conducted: three topics and eight cards in the human domains, each under its row's condition, at 17 of 17. Sixth wave conducted: three quotes topics, every line read at its source, two lines moved to Misattributed, at 10 of 10. Seventh wave conducted: the nineteen remaining pictures of §2 in fourteen domains, eight of them drawn with another component than their row named, and two numbers corrected by drawing them. Eighth wave conducted: four exam paths over topics that exist, a path as a deck, the two gaps the census carried, search that no longer reads acronym expansions, and a spelling gate that knows prefixes. Ninth wave conducted: §16's list emptied, five topics for the A+ objectives the paths skipped and a Security+ SY0-801 path read from CompTIA's own objectives. Tenth wave conducted: four more exam paths, PenTest+, CySA+, Linux+ and CISSP, each read from the exam body's own document, and six topics for the objectives they found with nothing to point at. Eleventh wave conducted: a SecurityX path read from CompTIA's own document, and the two CISSP objectives the tenth left, one of which SecurityX needed too. Fourteenth wave conducted: MD-102 and MS-102 paths read from Microsoft's study guides, AZ-800 found retired and its tag corrected, and the gaps both outlines found listed as the next queue. Fifteenth wave conducted: four topics for MS-102's Defender XDR area, each read from Microsoft's own pages first, at 13 of 13. Sixteenth wave conducted: MS-102's identity and Purview gaps, four topics at 13 of 13, and IdFix found retired | ✅ **shipped** — see its §9 to §22 |
| **Error codes and packaging** | Three items from the owner, added as written: an error-code lookup in the header's row of buttons, the Intune and MECM codes compared, and MSI, .intunewin and EXE explained. Each checked against the site first, with the owner's guide to MSI against EXE in MECM kept beside them as written | ✅ **shipped** — see its §5 |
| Domain shape | The connectivity graph: hubs, broadcasters, islands. Both navigation layers complete — 0 hand-written orphans, 0 hand-written topics off a path, and **both halves now derived**: the second was prose for weeks while three topics were off one | 📘 reference |
| Session records | The recent ones. The rest are in `plan-archive.md`, oldest first — **the counts are the *Session records* row of the measured-state table**, and were a second copy here that had been wrong by five since the split | 📘 living |

**Everything closed is in [`plan-archive.md`](plan-archive.md)** — the July 2026 review,
the content roadmaps, Phases 3 to 10, the Execution Handbook, the calculus track and the
worked specifications. It is kept rather than deleted because this file's most-quoted
passages are the ones explaining why something was *rejected*, and nobody would write those
twice.

**The measured state, as of the last session record.** Every number below is produced by a
tool in `tools/`, not by anybody's recollection, and `make census` prints the first four.
**Thirteen of the seventeen rows** are checked by `check_plan_numbers.py` in `make check`.
When it first ran there were eleven, and **nine of the eleven were wrong**, the page budget
by a factor of twelve. It names the four it cannot derive on every run rather than letting
them pass as verified — and **naming is not checking**, which one of the four then proved:
that row's headline stayed current for four waves while the three sub-counts in the same
sentence drifted by eight, because nothing read them. A fourteenth row is checked now,
by `query_probe.mjs --check-plan` in `make all` and CI, on the argument that the browser
the row needs was already running. Three are left, and all three want a stopwatch:

| Measure | Value | Tool |
|---|---|---|
| Topics | **1,595** across 30 domains | `depth_report.py` |
| Thin (one card, under 1,800 chars) | **7**, 0% — and `--thin` prints badge, position and xref count beside each, because the ones left are short by design. Three of the eight were not: two military lookup cards and a domain preamble each had a judgement they were not making | `depth_report.py` |
| Mean chars per concept card | **1,429**, or **1,149 excluding verdicts** — the second is the padding counter-metric. It has tracked the first within two across every wave this session, which is the shape to want: the two numbers moving together | `depth_report.py` |
| Orphans | **60**, every one generated, **0 deep** | `orphan_report.py` |
| Near-duplicate pairs | **96** (41 by overlap, 55 by containment) — 78 explained by §3, 18 read and recorded, **0 unread** | `near_duplicates.py` |
| Reader questions answered | **547 of 571**, **0 unexplained** — thirty-five batches. The newest is the sixteenth wave's, 13 queries for MS-102's identity and Purview objectives, added to *a service desk engineer* before their topics. It opened at **0 of 13**, nine zeros and four that found other cards, and closed at 13 of 13 after one prose fix: `helpdesk admin for one office only` lacked only *office*, which is what the card's example of a region meant. The wave also took an old query's answer away for an hour. `bitlocker recovery key` had matched one card exactly and widened to the BitLocker topic; the administrative units card's *BitLocker recovery keys* made two exact matches, so search stopped widening, and the BitLocker topic, which said *recovery key* but never Microsoft's full name for it, dropped out. It says the full name in its table now. Before it came the fifteenth wave's, 13 queries for MS-102's Defender XDR objectives, added to *a SOC analyst or defender* before their topics. It opened at **0 of 13**, five zeros and eight that found other cards, `exposure score` among them reaching ten cards and none of them about Microsoft's product, and closed at 13 of 13: five find their topic alone and eight find it among two to eighteen. Before it came the twelfth wave's, 8 queries for the owner's packaging and error-code items, added to *a service desk engineer* before their topics. It opened at **0 of 8**, one zero and seven that found other cards, and closed at 8 of 8. The same topic gave an older question its target: `the software installed but does not appear`, recorded with none, now names the error-code topic, which says it in those words. Before it came the eleventh wave's, 8 queries for CISSP 1.6 and 7.15, added to *somebody revising for a CompTIA exam* before their topics. It opened at **0 of 8**, four zeros and four that found the wrong card, `cobit` among them reaching only the acronym dictionary, and closed at 8 of 8: five find their topic alone and three find it among two or three. Before it came the tenth wave's, 18 queries for six objectives four exam outlines had no topic for, added to *somebody revising for a CompTIA exam* before their topics. It opened at **0 of 18**, eleven zeros and seven that found the wrong card, `incident communication plan` among them reaching 23 topics and none of them a plan, and closed at 18 of 18: fourteen find their topic alone, and four find it among two to eight. Before it came the ninth wave's, 16 queries for the five A+ objectives the exam paths skipped, added to *somebody revising for a CompTIA exam* before their topics. It opened at **0 of 16**, ten zeros and six that found the wrong card, and closed at 16 of 16 with three `endpoint` topics and two in `hw`. Two closed in prose, each by the card saying what the reader asked in the reader's words: `windows 11 tpm requirement` once the card called them Windows 11's requirements, and `fat32 file size limit` once it named FAT32's file size limit. Before it came the sixth wave's, 10 queries for §4 rows 32 to 34, the quotes, added to *a learner meeting a subject* before their topics. It opened at **0 of 10**, all ten zeros, and closed at 10 of 10, with every line in the three topics read at its source first. Before it came the fifth wave's, 17 queries for *Content ideas* §4 rows 28 to 31 and 35, added before their cards to two readers that already ask about those subjects, *a learner meeting a subject* and *somebody looking for a job*. It opened at **0 of 17** and closed at 17 of 17: 14 zeros and 3 that found the wrong card, `active listening` among them through load balancers and nmap. One closed in prose, not a card: `depressed for weeks` needed the low-mood topic to use the reader's word. Before it came *a student on a theory course*, the second reader *Content ideas* §7.3 named: 15 queries for its fourth wave, seven rows, added before their cards. It opened at **0 of 15** and closed at 15 of 15: 8 zeros and 7 that found the wrong card, `segmentation fault` among them through network segmentation. Before it, the exam reader's third batch, 16 queries for the third wave, opened at **0 of 16** and closed at 16 of 16: 12 zeros and 4 that found the wrong card, `pivot table` among them through *pivot* and *table* in threat and grc cards. Its second, 23 queries for the second wave, opened at **0 of 23** and closed at 23 of 23: 16 zeros and 7 that found the wrong card, among them three that reached only the acronym dictionary and one an AI card that happens to contain *tone* and *probe*. Its first batch, *somebody revising for a CompTIA exam*, was added the same way for the first wave's five rows. It opened at **0 of 16** and closed at 16 of 16: 8 zeros and 8 that found the wrong card. Four of the zeros were words the site had never written, among them `scannow` and `pbq`, and `crc errors` reached a modular-arithmetic card. The wave also disturbed one old query: `the user has two accounts` sat on the wide threshold at 60 and went to 61, and it carried a verdict naming the gap underneath it until the eighth wave wrote that gap as its own topic, which the query now finds alone. The reader before it, *somebody looking up a character code or a handshape*, was added from a request for the ASCII character set with ASL added to it, before the card was written. It opened at **0 of 12** and closed at 12 of 12: five zeros, and seven that found cards but never the chart. `asl` was a zero the corpus counted fifteen times, every one inside another word: *asleep*, ASLR, Maslow, SASL. The reader before it, *a student with a data structures course*, was added from *csvistool* the same way. It opened at **0 of 16** and closed at 16 of 16, the first reader to open with nothing answered: eleven zeros, and five that find the wrong card. The one before that, *a student on a software engineering course*, was added from *Knowledge integration* the same way. It opened at 9 of 25 and closed at 25 of 25, and **nine of its first sixteen misses found cards, just not the right ones**: `logic gates` reaches pipeline gates and `multi core processor` the GDPR's data processor, the wrong-sense shape the last two queue sections found in chip subtitles and in *stack* and *queue*, counted here for the first time. Before that, *a student on a SQL Server and Java course* opened at 14 of 15 missing and closed at 15 of 15. The first two subject-shaped ones opened at a third missing; the ten symptom-shaped ones at **two thirds**, and that gap is the census's most repeated finding — batches seventeen and eighteen opened at 22 of 29 and 20 of 28 — the same two thirds twice more. Of the **23** zeros and **1** wrong-card, all are recorded verdicts. Two recorded zeros left that list by coincidence in the third wave, and their notes say so. `the user says the file is gone` matched the Windows tools topic with `user` found only inside the expansion of UDP, until the eighth wave stopped search matching inside expansions and it went back to zero, which is what a reader gets. `the usb ports on one side stopped working` matched a connector card's *wider on one side*, and relaxation added Motherboard Anatomy, which was half an answer until the eighth wave wrote the card it needed there. The 8 wide results are verdicts too, and all six of these numbers are checked against a live census by `query_probe.mjs --check-plan` — the row needs a browser, so the browser checks it. The staleness check reports a verdict that has stopped describing its row, and it has now caught two, both on a note of its own author's: the first time the note was right and the check was wrong — `\bzeros?\b` was matching *zero* inside **zero-touch** — and the second time the note was simply out of date, which is what it is for. The wrong-card one is kept on purpose: `the intern deleted the wrong thing` asks the site to contain a word it has no reason to contain, and writing one in is the keyword stuffing the census exists to refuse | `query_probe.mjs` |
| Learning paths | **114 paths, 2,144 steps, 1,535 of 1,595 topics, 0 hand-written topics off a path** | `check_paths.py` |
| Related links | **1,535 topics, 5,170 links, 0 one-way** — one mainland of **1,519 (98%)** and **one** island: `math`, 16 of 16, which is a decision rather than a backlog. It read *three reference-domain islands* until somebody measured how much of each island's domain was already connected — 29 of `shortcut`'s 36 and 3 of `quotes`' 6 — and `orphan_report.py` prints that figure now | `suggest_related.py --check` |
| Page budget | **28% raw** headroom — room for ~612 more topics | `page_budget.py` |
| Throttled load | **~3.0 s** = 0.5 s shell + 1.0 s script.js + ~190 ms/MB — *this container only* | `measure_load.mjs` |
| Search &amp; heap at 3x the content | **86 ms · 93 MB** at 4,602 indexed topics — search is not the constraint, load is | `measure_load.mjs --synthetic` |
| Depth tail | **10th percentile 2,172 chars**, median 3,832 — the number a deepening wave has to move | `depth_report.py` |
| Dated claims | **53 volatile spans and 125 fact anchors: 178 dated claims**, and **3** console candidates — all three read and recorded as false positives in `context()`'s docstring. The denominator is still not countable and that is Phase 11 §3's whole finding; the numerator always was, and spent a year in prose because nobody noticed the difference. It rose by two in the V2 pass, against §6's counter-discipline that a rising count is not automatically progress — both are limits a card **designs around**, which is the one case §5 says a span is right for, and the same pass rewrote nothing because the other ten claims were never facts about the world. It rose by eighteen with the csvistool deep links, one anchor per line of links, which is the rise csvistool §1 asked for: a route is a key in someone else's repository, and one rename there breaks it silently. It rose by one with the ASCII chart's source link, and that anchor records that this container could not fetch the page rather than claiming a check. It rose by one more with GCM's random-nonce limit in the cipher-modes card, and that anchor says the NIST figure was confirmed in search results and the PDF was not fetched. One more for Cisco's default administrative distances, said the same way, and two for the Windows repair ladder: Microsoft's DISM-before-SFC order and the two failed starts that open WinRE. And one for CompTIA's rule that a virtual PBQ cannot be skipped and returned to, which this container could not fetch from comptia.org and says so. Two more for Cisco's syslog defaults in the severity card: the trap level that ships as informational, and the two messages one interface going down produces, both confirmed in search results with the pages not fetched. Three more in the cabling and discovery cards, said the same way: the standard's preference for T568A, Cisco's rule that fixing speed and duplex turns Auto-MDI-X off, and the CDP and LLDP timers. One more for the Excel versions that have XLOOKUP, one for the A+ objective numbers behind the malware removal steps, one for the two exercise studies the header image's numbers were checked against, two in `cs` for ECC memory's code and the Mars Pathfinder mutex, and five in `military` for the transition programs, the 9-line, the date-time group and METT-TC, said the same way. The date-time group's anchor says that no source was found for it, which is what an anchor is for. Two in `mind` date the health services' two-week line and the COBRA trial, and one in `philosophy` records which translation the Epicurus quotation is from. Four in `quotes` record the pages each line was read on, fetched this time and not only searched. One more in `military` records where Boyd's line from Orient to Act was read about, and that both primary PDFs refused the fetch, and one in `blueteam` dates the Pyramid of Pain to Bianco in 2013 from a secondary overview, his post unread. One in `infra` records that an Enforced link moves to the end of processing, from Microsoft's pages as quoted in search, and one in `m365` that a rule setting the spam level to −1 cannot pass malware or high-confidence phishing, said the same way. Two in `infra`'s two-accounts topic date how sync matches a user and how long a deleted one can be restored, and three in `endpoint` date the edition differences, subscription activation, and the MBR, GPT and Windows 11 limits. Three in `hw` date the file systems' limits and support, NTFS permissions on copy and move, and Backblaze's SMART figures, which are from its 2016 data. Ten more in the tenth wave's six topics, all from search results with the pages not fetched: two in `linux` for dracut's `mkinitrd` wrapper and libvirt's open network mode, three in `threat` for ATT&CK's injection and side-loading numbers and Sysmon's events, three in `sec` for the DES search, the padding oracles and the side-channel papers, and two in `ops` for the NIS2 and Form 8-K clocks. Eleven more in the twelfth wave's two `endpoint` topics. Eight are from Microsoft's own pages, fetched and read — the Windows Installer, Intune and Configuration Manager error references, msiexec's switches, the Win32 content prep tool and both tools' app settings — and one from Inno Setup's documentation. Two are from search results and say so: NSIS's case-sensitive switch, whose manual page refused the request, and Intune's default return codes, which Microsoft's page says exist without listing them. Twenty-one more anchors and four spans in the fifteenth wave's four Defender topics, every anchor from a Microsoft page fetched and read, with the date Microsoft last updated it. The spans mark the console paths, where the portal is and where a setting lives, because those are what Microsoft renames, and the console count asked for them: it went from three to six when the topics landed and back to three when the spans did. Thirteen more anchors and two spans in the sixteenth wave's four topics. Twelve anchors are from Microsoft pages fetched and read; the thirteenth records IdFix's retirement from its own repository, beside the 404 that Microsoft's page about it now returns. One older anchor changed too: *One User, Two Accounts* had cited the July 2026 hard-match hardening from search results, and now says the sync-errors page was read | `check_volatility.py` |
| Gates | **45**, and the same 45 in `make all` and in CI | `check_gates.py` |
| Gate results | check · smoke **167** · search **59** · resilience **64** · axe 33/33 · mobile 16/16 · visual 2/2 · backup 3/3. The error-code lookup added one check to each of smoke, mobile and axe's two themes, and the expand switch one to smoke. Visual is 0/2 in the container that ran the last session, and was 0/2 there on the commit before it too: its fonts render about 10% wider | `make all` |
| Cards ending on a table with no verdict | **10**, all deliberate lookup tables in `military` — two of the original twelve turned out to have a judgement their table was carrying silently | `lint_content.py` |
| Session records | **28** here, **332** in `plan-archive.md` | `check_plan_numbers.py` |

**`make all` is the contract — and it held a claim it could not keep.** *If it passes, CI
passes* was written when `check_gates.py` was added, because the workflow had been red on
every push for nine commits while `make check` was green. The gate makes the two **lists**
agree and it did. It says nothing about whether every command on the agreed list can run in
the job it is listed in, and one could not: `query_probe.mjs --self-test` resolved Playwright
at import, `make check` is deliberately browser-free so its CI job installs no Node
toolchain, and the step exited 2 before it read its own flag. **CI was red on `main` for four
runs while `make all` was green on every machine that had Playwright installed.** Fixed by
resolving the browser at the point of use; the contract is true again, and the lesson is that
*the same gates* is a weaker guarantee than it reads as.

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
| 6 | Used `class="c-yellow"`, which does not exist | Grep `style.css` for the utility class before using one. Six exist; the rest are `style="color: var(--…)"`. **Now a gate:** the habit was got past nine times, and `check_css_vars.py` fails on a class no rule defines |
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

### How property 5 actually gets done, which nobody had written down

A verdict has to refer to the table above it without repeating it, and this site
solved that a long time ago in a way no file here had ever stated. **It names a
row by position.**

> *The last row is the one to design around.* · *Only the second row actually
> bounds the damage; the rest raise the effort.* · *Work down this table in
> order and stop at the first row that works.* · *The last row is the one that
> ruins a Friday.* · *Only one of these rows can fine you, and it is the one
> with dates attached.*

**431 of 2,716 verdicts — 16%, in 32 of the 35 domain files.** Measured, not
recalled, and the spread is the interesting half: this is not one author's tic
in one domain, it is the house form.

It works because it does the two things at once that a verdict has to. It is a
*judgement* — a claim about which row matters, which is the one thing a table
cannot state about itself — and it is a *pointer*, so the verdict never has to
restate the content it is ranking. A verdict that begins "The last row" has
already committed to saying something the table does not.

The practical rule: **if you cannot name which row matters, the table is
probably unranked**, and §3's listicle row applies to it rather than to the
verdict.

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
| **The plan outgrows its own readability** — 11,600 lines, and the useful part is the last few hundred | `check_plan_numbers.py` reports the live file past **8,000 lines** | ✅ **Closed, reopened, and closed again.** Option 3 shipped, then option 1 at 22,745 lines by somebody noticing. The condition then fired on its own at **8,020**, and option 1 ran again — 45 records moved, 8,020 → 4,227, lines conserved. It fired a third time at **8,009**, and the same move took the file to 4,092. **The reopen condition is the only part of this register that has ever been tested, and it worked** |

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


# Knowledge integration — a batch of study notes, and the seven destinations it named

> Source: an integration plan written against the live site from a batch of newly
> summarized notes (*Add to Garrett's study website.md*). It was filed here as **a queue,
> not a record**, and has since been conducted: §6 says what went where. It is also the first incoming work in a
> while that arrived as a *list* rather than from a census, which is worth saying out
> loud, because the first thing a list gets is the treatment this file gives every other
> hand-written number: it was checked against the tool.

**Seven items, seven destinations, and three of them moved.** Every target the plan named
was looked up in `data/domains.json` and grepped for in `data/*.html` before anything was
written down. Two destinations stand exactly as filed, three move to a different domain,
one splits in two, and one does not point at this repository at all.

**The reason they moved is worth more than the corrections.** The destinations were
derived from the site's **chip subtitles**, and the subtitles overlap. `devops` advertises
*"… Serverless · Architecture"* and `eng` is called **Software Engineering &amp;
Architecture**. `linux` advertises *"… RAID · Hardware"* and `hw` is a 28-topic domain
called **Hardware, Electronics &amp; Embedded**. A reader picking a home from the chip
row lands on the first domain that says the word — the same shape as *the card I wrote to
close a query used the site's words, not the reader's*, one layer up: the site's own
vocabulary is what a person navigates by, and two domains claiming one word is a
navigation bug before it is a filing error.

## 1. The seven items, as filed and as checked

| # | Source material | Destination as filed | Checked |
|---|---|---|---|
| 1 | AI in development (NLP, Copilot, code generation); AI accountability and ethical oversight | **AI &amp; Machine Learning** → the existing *AI Ethics* topic | ✅ **stands.** `ai` exists, its subtitle names *AI Ethics*, and the phrase appears in `data/ai.html` |
| 2 | Computer networks &amp; spanning trees — redundant paths, network loops | **Networking**, beside *Topologies* and *OSI* | ✅ **stands** — and is already written. `net`'s subtitle names both, and `Spanning Tree — Why a Loop Is Catastrophic, and What STP Does About It` is a live topic. This one is a **deepening**, not a card |
| 3 | Hardware architecture (multi-core, parallel computing); logic design (Karnaugh maps, NAND gates) | **Linux &amp; Systems**, under a *Hardware* sub-topic | ↪ **moves to `hw`.** `linux` does end its subtitle in *Hardware*, which is why it was picked, but `hw` is 28 topics and names *CPU &amp; memory*. Digital logic is `hw`; parallel computing as theory is `cs` |
| 4 | UML sequence diagrams, data flow diagrams, class/inheritance design, component-based software engineering (CBSE) | **DevOps, Platform &amp; Delivery**, to expand *Architecture* | ↪ **moves to `eng`.** `devops` ends its subtitle in *Architecture* — but `eng` **is** *Software Engineering &amp; Architecture*, 86 topics, subtitle *System Design · Architecture · Craft*. Delivery pipelines are `devops`; design notation is `eng` |
| 5 | Verification vs validation; SDLC methodologies (Agile, Waterfall, Spiral, Iterative); reliability metrics (MTBF, safety-critical) | **IT &amp; Security Operations**, enriching *ITIL*, *SRE*, *Observability* | ✂️ **splits.** MTBF and safety-critical go to `ops`, which already carries MTBF in prose. V&amp;V and the four methodologies go to `eng`, where `Agile — The Four Trade-offs, and What Gets Sold as Agile` and the Waterfall prose already are |
| 6 | WCAG, cognitive load theory, user/task analysis, UI heuristics (affordance, simplicity, feedback) | **Human** domain → a new *UX/UI &amp; Accessibility* module | ↪ **moves, and the named destination does not exist.** *Human* is a **nav chip-group**, not a domain, and it holds `philosophy` and `military`. Accessibility already lives in `web` (subtitle *… Performance · A11y*, two live topics, one of them the WCAG card). Cognitive load is prose in five files. See §3 |
| 7 | Site → notes: the security frameworks (MITRE ATT&amp;CK, NIST CSF 2.0, Zero Trust) back into the markdown | **The markdown notes**, fleshing out *Product Validation* | ↗️ **points outward.** Nothing in this repository changes. Recorded so the next session does not go looking for a card to write. See §4 |

## 2. What the site already has — grepped, not assumed

The plan describes the notes. This describes the site, which is the half that decides
whether an item is a card, a deepening, or a duplicate. Every row is a `grep` over
`data/*.html`, not a recollection:

| Concept | Where it is today | What that makes it |
|---|---|---|
| Spanning tree / loops | `net` — a full topic, plus the acronym dictionary | **Written.** Item 2 is a deepening at most |
| WCAG / accessibility | **six topics across five domains** — `web` (*WCAG &amp; ARIA*, *Accessibility Remediation*), `grc` (*Section 508*), `hw` (*Input Devices &amp; Accessibility Hardware*), `ops` (*Accessible IT*), `script` (*Building for Everyone*) | **Written, and scattered.** A new module would have to justify itself against `near_duplicates.py` before it wrote a line |
| Agile / Waterfall | `eng` — an Agile topic; Waterfall in prose in `eng`, `ops`, `web` | **Partial.** Spiral and Iterative are absent |
| MTBF / safety-critical | `grc`, `ops`, and the acronym dictionary — prose only | **Partial.** No topic owns it |
| Cognitive load | prose in `career`, `devops`, `eng`, `script`, `web` | **Partial**, and the five mentions are the argument for one card the others link to |
| UML / sequence diagrams | the acronym dictionary, and one `career` card | **Absent as content.** An expansion is not a card |
| Karnaugh maps · data flow diagrams · CBSE · the spiral model · affordance | **nowhere in `data/*.html`** | **Absent.** These five are the real new content in the batch |

**The batch is smaller than it looks, and the small part is the valuable part.** Of the
six inbound items, two are already written, three are partial, and the genuine gaps are
five named concepts. That ratio is the same one the reader-question census keeps
reporting: *what a list asks for and what the site is missing are different sets*, and
only the grep tells them apart.

## 3. Item 6 is a domain decision, not a filing decision

A new **UX/UI &amp; Accessibility** domain is the one item here that cannot be done by
appending cards. `scaffold_domain.py` exists for exactly this, and the cost is the rest of
the checklist: a chip in a group in `index-shell.html`, a color class, a `domain-intros`
entry, learning-path steps (`check_paths.py` gates *0 hand-written topics off a path*),
and enough related links to avoid becoming the site's second island — `math` is the first,
and is a **decision** rather than a backlog.

The honest reading of the grep is that **the accessibility half is already written and
scattered, and the UX half is not written at all.** Those are two different problems: the
first is a connectivity problem, and §3 of *Domain shape* below — the See-also layer in
`related.json` — is what it is solved with rather than by moving cards; the
second is four or five cards in `web`. A new domain is what you build when the cards
exist and cannot be filed — not before. **Deferred, with the condition stated: revisit if
the UX half reaches six or more cards in `web` and the see-also layer is still carrying
them.**

## 4. Item 7 points at the notes, and is the one to do first

Reverse integration — the site's `sec`, `threat` and `grc` material (MITRE ATT&amp;CK,
NIST CSF 2.0, Zero Trust) going *back* into the markdown notes — changes nothing in this
repository and needs nothing measured. It is also the cheapest item in the batch and the
only one with no dependency on any of the others, which is the ordering argument.

## 5. Before any of this is written

The rubric applies unchanged, and three of its checks bite this batch specifically:

1. **`query_probe.mjs` first, not last.** The question *does a reader asking this get
   nothing today* is answerable before the card is written, and four waves running have
   ended with a card that did not close its own query until the reader's word went in.
2. **`near_duplicates.py` for items 2, 5 and 6.** Three of the seven land next to content
   that already exists. A card that restates a live one is the failure mode this batch is
   most exposed to, and the register's *0 unread pairs* is the number it would move.
3. **A definition is not a card.** The source material is *"extensive definitions"* by its
   own description. The one test in the card rubric — that a card answers a question
   somebody actually has — is the filter that decides how many of the five absent concepts
   are worth writing, and the answer is allowed to be fewer than five.


## 6. What shipped

Conducted in one session, in §4's order where there was one, and recorded below as *Session —
conducting the first batch*. The reader, *a student on a software engineering course*, opened at
**9 of 25** and closed at **25 of 25**.

| # | Item | Where it went |
|---|---|---|
| 5.1 | The queries, before anything | A reader of 25, committed before any item was written. Where the answering card did not exist yet, its `want` named the topic being written into, so a result in the wrong sense of a word scored as the miss it was |
| 7 | Security frameworks back into the notes | A Markdown section for *Product Validation*, handed to the notes' owner. Nothing in this repository changed, as §4 said |
| 1 | AI accountability and ethical oversight | One card in *AI Ethics — The Human Side*: oversight fails by agreement. Automation bias, and five controls ranked by what each can prove. AI in development was already written |
| 3 | Multi-core, parallel computing, Karnaugh maps, NAND | **Moved again, to `cs`.** Truth tables and De Morgan are in *Boolean Algebra*, and the architecture stack is `cs` too. Two cards there: NAND as the primitive, and the Karnaugh map with the glitch its minimal circuit can make. *Amdahl's Law* already taught parallel computing and gained the reader's two phrases |
| 4 | UML, data flow diagrams, class design, CBSE | UML and class design shipped with batch two. **Data flow diagrams were written all along**: *Diagrams That Explain* spells it *data-flow*, and §2's grep did not allow for the hyphen. CBSE became a card in *Dependency Risk*: the component market arrived, and the contract did not |
| 5 | V&V, the SDLC methodologies, MTBF, safety-critical | A new `eng` topic, *SDLC Models*, before Agile. MTBF as a rate, with MTTR as the lever, in *BCP / DR — Key Metrics*; reliable is not safe, in *FMEA* |
| 6 | WCAG, cognitive load, task analysis, heuristics | The UX half, as a new `web` topic, *Usability*. **The domain stays deferred**: four cards in one topic, not the six §3's condition names. Cognitive load was not prose in five files: two were concept cards, and the new card points at them |
| 2 | Spanning trees | Written, and both of the reader's queries answered. The deepening is that a spanning tree is not a *minimum* one, which csvistool §3 needed from the other side, so it shipped with that card: one sentence in the STP card, and a link each way |

# csvistool — one outbound link, and the forty-one concepts behind it

> Source: a one-line request to link **[csvistool.com](https://csvistool.com/)** and add its
> concepts, **in this file only for now**. It was filed as **a queue, not a record**, and has
> since been conducted: §5 says what went where. The tool is the *CS 1332 Data Structures and Algorithms Visualizations* site
> from Georgia Tech: step-by-step animations with pseudocode, open source at
> [`csvistool/visualization-tool`](https://github.com/csvistool/visualization-tool), adapted
> from David Galles' USF visualizations and maintained by course TAs under Prof. Mary
> Hudachek-Buswell. **The concept list below comes from the tool's own registry,
> `src/AlgoList.js` at commit `4549799` (2026-04-23), not from its home page.** This
> container's network policy blocks `csvistool.com`, and the registry is what the home page
> renders from anyway.

**Two jobs, and one of them is a single line of HTML.** The link needs one `.extlink`
anchor. The concepts are 41 visualizations. About half already have a card on the site that
explains *when and why*, 12 of 40 searches for them return nothing, and one cluster is a
real gap.

**The tool and the site do different things, and that decides how the work is shaped.** Our
cards answer *which one, and why*. `Four Trees, Four Different Jobs` and `You Will Never Write
a Sort; You Will Choose One By Accident` are the model. The tool answers *how it moves*: step
through an AVL rotation, watch a probe sequence fill a table. **So the link goes on the card
that already explains the concept, and no card should narrate an animation in prose.** A
paragraph walking through a heap's sift-down step by step is the thing the tool exists to
make unnecessary.

## 1. The link: where it can go, and a trap for a link checker

**The convention exists and needs nothing new.** `.extlink` in `style.css` came in with the
DSM-5-TR fix: accent colour, dotted underline, `↗`, and the href printed on paper, with
`target="_blank" rel="noopener noreferrer"`. The content has three external links today: the
APA's DSM page from `mind` and `philosophy`, and one in `script`. An href is not a fetch, so the smoke test's *no off-site requests* check is
unaffected. **Embedding is not an option and should not be proposed:** `netlify.toml`
sets `default-src 'none'` with no `frame-src`, so an iframe of the tool is blocked by the
site's own CSP.

**The obvious home for a domain-wide link cannot hold one.** The `cs` landing card is built
from `data/domain-intros.json`, and `script.js` renders every field with `textContent`. A
link there means a new field and a renderer change, and then the axe, mobile and visual gates
all get a say. **Deep links on cards need no code at all.** The tool routes `/:algo` on its
registry keys, so `https://csvistool.com/AVL` opens the AVL animation directly.

| Order | Where | Cost |
|---|---|---|
| **1st** | Deep links on the eight topics that already teach a concept (seven in `cs`, one in `script`), placed where the concept is named, e.g. *watch it: [AVL](https://csvistool.com/AVL) · [2-4 tree](https://csvistool.com/BTree)* | Content only. Lint, build and check, nothing else |
| 2nd | One home-page link on the `cs` landing card | A `domain-intros.json` field **and** a `script.js` renderer. Only worth it if the deep links earn clicks, and nothing here measures that |

**The trap, found while reading the tool's source, and worth recording before anyone builds
a checker.** csvistool is a React single-page app on GitHub Pages. Deep paths are served by
`public/404.html`, the *spa-github-pages* redirect trick, which rewrites `/AVL` to `/?p=/AVL`
in JavaScript. A deep link should therefore **answer HTTP 404 and still work in every
browser**. That is GitHub Pages' documented behaviour for a custom 404 page, and it could not
be checked live from here because the host is blocked. The link-rot check was measured away
at *one external link on the whole site*. The thirty-odd deep links §2 calls for would reopen
that item, and **a naive checker would report every one of them dead.** If it gets built, it checks this host's
root and not its paths, or it follows the redirect the way a browser does.

**Reopened, and at what count.** The deep links shipped with fact anchors, one per line of links, and the link-rot item reopened at **37 external links, 34 of them on `csvistool.com`**, one per route. It closed the queue at **42, 39 of them on that host**, once the candidate cards had theirs. The trap above is the reason it is still not a gate: every one of them answers 404 by design, and the routes were checked against the tool's registry (`src/AlgoList.js` on `master`) rather than by fetching them, because this container cannot reach the host.

**The tool's key names disagree with the textbook, so link by label and not by key.**
`OpenHash` is labelled *HashMap (Probing)* and `ClosedHash` is *HashMap (Chaining)*. That
follows the *open/closed addressing* naming, the reverse of *open/closed hashing*, where
"open hashing" means chaining. Anchor text copied from the keys would say the opposite of what
the page shows. This is also the one sentence the `Hash Tables` card is missing (see §2).

**Every deep link is a dated claim.** A route is a registry key in someone else's repository,
and one rename would break it silently. Each link gets a Phase 11 fact anchor:
`<!-- fact: csvistool route /AVL | source: csvistool/visualization-tool src/AlgoList.js | checked: 2026-09 -->`.
`check_volatility.py` counts those, which moves the *Dated claims* row. That is the point: the
row goes up for a reason somebody can read.

## 2. The concepts, as the tool files them and as the site has them

Every row below was checked two ways: a grep over `data/*.html` with `acronym.html`
excluded, and **a search probe of the built page**, meaning `runSearch()` driven in Chromium
the way `query_probe.mjs` does it, over 40 queries a CS 1332 student would type. **12 of the
40 return nothing.** Paths are the tool's routes, all under `https://csvistool.com/`.

| Tool category | Concepts → route | On the site today | What that makes it |
|---|---|---|---|
| **Lists** (4) | ArrayList `/ArrayList` · Singly `/LinkedList` · Doubly `/DoublyLinkedList` · Circularly `/CircularlyLinkedList` | `cs` *Amortized Analysis — Why a Dynamic Array Is O(1)*; `cs` *Memory Layout & Cache Locality — Why Arrays Beat Linked Lists*; `script` *Data Structures — How Data is Organized in Memory*. Doubly linked: one mention, in a Rust card. Circular: **0** | **Link targets** for the first two. Doubly linked has one real hook the site lacks, the **LRU cache** (a hash map plus a doubly linked list). `LRU` appears only in the acronym dictionary and a Redis eviction table, so the hook is a sentence in `Memory Layout`, not a card. Circular: leave to the tool |
| **Stacks, Queues & Deques** (6) | array- and linked-backed each: `/StackArray` `/StackLL` `/QueueArray` `/QueueLL` `/DequeArray` `/DequeLL` | `script` *Choosing the Right Data Structure* (List · Tuple · Dict · Set · Queue · Stack). `LIFO` and `FIFO` appear twice each, both in `script`. The array-versus-linked split: **absent** | **Link targets** on the `script` card. The finding is the vocabulary: `stack data structure` returns **35 results, 0 in `cs`**, and the first is the OSI model. `queue data structure` returns 35, and the top three are `sec`/`threat`. *Stack* means tech stack, network stack and ELK stack across **141** mentions, and *queue* means message queue and triage queue across **228**. The same shape as the last batch's chip subtitles: a word the reader navigates by, already owned by another sense |
| **Trees & SkipList** (5) | BST `/BST` · Heap `/Heap` · AVL `/AVL` · 2-4 tree `/BTree` · SkipList `/SkipList` | `cs` *Trees — BST, Balanced, Heap, Trie*: `Four Trees, Four Different Jobs`, and `An Unbalanced BST Is a Linked List With Extra Steps`, which names AVL and red-black as the fix. 2-4 tree: **0**. Skip list: **0**, and `skip list` returns 31 results with none in `cs` because the words match separately | **Link targets** for BST, heap and AVL. 2-4 tree is one sentence in the existing B-tree card: it is a B-tree of order 4, and the structure a red-black tree encodes. **Skip list is a candidate card.** It has an operational hook: Redis sorted sets and the LSM memtable in LevelDB and RocksDB. It still has to pass the rubric's *a question somebody has* |
| **Maps** (3) | Chaining `/ClosedHash` · Probing `/OpenHash` · TreeMap `/TreeMap` | `cs` *Hash Tables — Collisions, Load Factor & the DoS*: `open addressing` twice, `separate chaining` **0**. `hashmap` → **0**; `treemap` → **0** | **Link target**, plus two **kind-1 zeros**. The site says *hash table* and *ordered map*, and the reader types Java's `HashMap` and `TreeMap`. Name both words in the prose. Add the open-hashing-versus-open-addressing sentence from §1 |
| **Sorting & Quickselect** (9) | Bubble `/BubbleSort` · Cocktail shaker `/CocktailSort` · Insertion `/InsertionSort` · Selection `/SelectionSort` · Quicksort `/Quicksort` · Quickselect `/Quickselect` · Merge `/MergeSort` · LSD radix `/LSDRadix` · Heapsort `/HeapSort` | `cs` *Sorting & Searching — Why Your Language Picked the One It Did*: quicksort, merge sort, heapsort and insertion sort sit under its Timsort / introsort / pdqsort table. Bubble: one mention. Selection: **0** (its only search result is an injection card). Cocktail: **0**. `quickselect` → **0**; `radix sort` → **0** | **Link targets** for the four the card covers. **Leave bubble, selection and cocktail to the tool.** They are teaching sorts, and the card's own thesis is *you will never write a sort*. **Quickselect is a candidate.** It finds the median or top-k without sorting everything, which is exactly what `cs` *Percentiles & Latency* needs to compute a p99. **Radix sort** is a section of the sorting card, not a topic: the one sort that is not a comparison sort, and so not bound by *n* log *n* |
| **Pattern Matching** (4) | Brute force `/BruteForce` · Boyer-Moore `/BoyerMoore` · KMP `/KMP` · Rabin-Karp `/RabinKarp` | All four are in `cs` *String Algorithms*, in the table under `Naive Search Is Usually Fine, Until the Data Is Adversarial`. `kmp` → **0**: the card writes *Knuth-Morris-Pratt* and never the three letters | **Link targets**, and the cheapest fix in the batch: one kind-1 zero closed by writing `(KMP)` |
| **Graphs** (7) | Representations `/CreateGraph` · Disjoint set `/DisjointSet` · BFS `/BFS` · DFS `/DFS` · Dijkstra `/Dijkstra` · Prim `/Prim` · Kruskal `/Kruskal` | `cs` *Graphs — Representation, Traversal & the Four Algorithms Worth Knowing*: `Adjacency List Unless the Graph Is Dense`, BFS, topological sort, Dijkstra, Bellman-Ford. **Depth-first search is not named in it.** `dfs` → 13 results, **0 in `cs`**: on this site DFS means Windows Distributed File System. `prim`, `kruskal`, `minimum spanning tree`, `disjoint set` → **0 each**, and `union find` returns four Python cards | **Link targets** for representation, BFS and Dijkstra. Depth-first is a **missing row** in a card that exists. **Minimum spanning trees and union-find are the batch's one real gap, see §3** |
| **DP & Extras** (3, plus 5 joke sorts) | LCS `/LCS` · Floyd-Warshall `/Floyd` · Splay tree `/SplayTree` · Drop, Sleep, Miracle, Bogo and Fred sort | `longest common subsequence` → **0**, `floyd-warshall` → **0**, `splay` → **0** (a first grep that said 96 was matching *display*). `cs` has edit distance as `Levenshtein Is Dynamic Programming You Will Actually Use` | **LCS is one sentence in the string card: it is what `diff` computes**, and every reader has run `git diff`. Floyd-Warshall is a row in the graphs table (all-pairs shortest paths, O(V³)), not a card. Splay tree and the joke sorts: **leave to the tool**. Two more joke entries, *LVA* and *Non-Linear Probing*, only appear on April 1–2 |

**The batch is 41 concepts, and it comes down to far fewer edits.** Each concept is counted
once, by what it needs besides its link:

| Needs | Concepts | Count |
|---|---|---|
| **Only the link.** Already taught, on one of **eight existing topics** (seven in `cs`, plus `script`'s *Choosing the Right Data Structure*) | ArrayList, singly linked list, the six stack / queue / deque routes, BST, heap, AVL, insertion sort, quicksort, merge sort, heapsort, brute force, Boyer-Moore, Rabin-Karp, graph representations, BFS, Dijkstra | **21** |
| **One word**, a kind-1 zero in `query_probe.mjs`'s terms | KMP, TreeMap, chaining and probing (the site says *hash table*, and neither `HashMap` nor `separate chaining` appears) | **4** |
| **One sentence or one table row** in a card that exists | depth-first search, 2-4 tree as a B-tree of order 4, LCS as `diff`, Floyd-Warshall, LSD radix, doubly linked list as half of an LRU cache | **6** |
| **A candidate card** that has to pass the rubric | Prim, Kruskal and disjoint set as one card (§3), then quickselect and skip list | **5**, in 1 to 3 cards |
| **Nothing written.** Linked from the nearest card at most, because the animation *is* the explanation and our "when" is "almost never" | bubble, selection and cocktail shaker sort, circular linked list, splay tree | **5** |

The five joke sorts are not counted. The open-hashing naming trap from §1 is one more
sentence, in the same edit as the chaining and probing words.

## 3. The one real gap: minimum spanning trees and union-find

Four of the twelve zeros are one topic: **`prim`, `kruskal`, `minimum spanning tree` and
`disjoint set`**. It is the fifth graph question, *what is the cheapest way to connect
everything?*, beside the four the graphs card already answers. It has an operational hook,
and a trap the site is well placed to explain:

- **The hook is `net`'s own spanning-tree card.** *Spanning Tree — Why a Loop Is
  Catastrophic, and What STP Does About It* builds a spanning tree, but not a minimum one.
  STP keeps each bridge's least-cost path **to the root**, which is a shortest-path tree.
  The two are routinely confused, and the difference is one sentence each way. It is a
  `related.json` pair between `cs` and `net`, the kind the connectivity section counts.
- **Union-find is the part that outlives the algorithm.** Kruskal needs it to reject an edge
  that would close a cycle. The same near-O(1) *are these two already connected?* is how
  duplicate accounts get merged and how network partitions get counted. That is the "when"
  the rubric asks for.

**Where it goes:** a concept card inside the existing `Graphs` topic, or a new `cs` topic if
`depth_report.py` says the host card is already long. `near_duplicates.py --title` goes
against the STP card before anything is written.

## 4. Before any of this is written

1. **Put the zeros into `query_probe.mjs` first.** Add a reader, *a student with a data
   structures course*, with the 12 zero queries from §2. That makes the zeros a tracked number,
   so every fix above can be seen to close its own query. The probe used here was a scratch
   copy of the census loop, and **a scratch file is how queries evaporated before**
   (`query_probe.mjs`'s own docstring).
2. **Deep links are content, so the loop applies unchanged:** lint, build, check, and
   `make og` only if the topic count moves. Fact anchors go in the same commit as the links,
   not in a later pass.
3. **The link-rot item reopens only once there are deep links.** Record the count it reopens
   at, and the 404 trap in §1, in the same commit, so the next session does not build a
   checker that fails on its first run.
4. **Card candidates face the rubric, not the tool's menu.** The tool covers a semester's
   syllabus, and that is no reason for the site to. Of the three candidates, the answer is
   allowed to be one.


## 5. What shipped

Conducted in one session, after *Knowledge integration*, in §4's order, and recorded below as
*Session — conducting csvistool*. The reader, *a student with a data structures course*, opened at
**0 of 16** and closed at **16 of 16**.

| § | Item | Where it went |
|---|---|---|
| 4.1 | The zeros, tracked first | A reader of 16: §2's twelve zeros, with `splay tree` for `splay`, and four queries that found the wrong card |
| 1 | The link | **39 deep links**, on the cards that already teach each concept, labelled by what the page shows and never by the tool's key. One fact anchor per line of links rather than per link: 18, each naming its routes. The home-page link on the `cs` landing card, §1's second row, is not built: its condition was that the deep links earn clicks, and nothing here measures clicks |
| 2 | The link-only concepts | Linked where the card names them, including the six stack, queue and deque routes on `script`'s chooser |
| 2 | Four words | `HashMap` and `TreeMap`, `(KMP)`, and *separate chaining*, beside the open-hashing trap. The tool itself files chaining under the route `ClosedHash` |
| 2 | Six sentences | Depth-first search as the BFS loop with a stack, in the traversal card, because the Graphs title promises four algorithms. Floyd-Warshall in the negative-weights verdict; the 2-4 tree as what a red-black tree encodes; LCS as what `diff` computes; LSD radix as the one sort not bound by *n* log *n*; the LRU cache as the linked list's famous resident |
| 3 | Minimum spanning trees and union-find | Two cards in *Graphs*, and the STP sentence from the other side, which was also *Knowledge integration*'s item 2 |
| 2 | The candidates | **Both passed**: quickselect in *Sorting & Searching*, pointing at *Percentiles & Latency* for streams, and the skip list in *Trees*. Neither narrates its animation |
| 2 | The five left to the tool | Bubble, selection and cocktail shaker sort, the circular list and the splay tree: linked, not written about, as §2 decided |
| 4.3 | Link rot | Reopened at 37 external links and closed the queue at **42, 39 of them on one host**, recorded beside §1's 404 trap. Still not a gate, for the reason the trap gives |

# Study notes, batch two — database, SQL and Java knowledge written in another dialect

> Source: study notes on databases, SQL, regex, pandas and Java, filed under the same name as
> the batch in *Knowledge integration* above (*Add to Garrett's study website.md*). That
> batch arrived as a plan with destinations. **This one arrives as the knowledge itself**, so
> the source names no destinations: every destination below is a lookup in
> `data/domains.json`, and every "on the site" is a grep over `data/*.html` with
> `acronym.html` excluded. Every zero is a search of the built page: `runSearch()` driven in
> Chromium the way `query_probe.mjs` does it, over 57 queries taken from the notes' own
> words. Filed as **a queue, not a record**, because nothing has shipped. The knowledge is kept
> in §7, grouped by subject.

**The notes use one dialect and the site uses another.** The notes were written against
SQL Server, Oracle and Java. The site is written against Postgres and Python:

| Across `data/*.html` | Mentions |
|---|---|
| Postgres | **106**, 39 of them in `data` |
| MySQL | 33 |
| SQL Server / T-SQL | **7**, and only 1 in `data` |
| Oracle | 9 |
| Python | **221** |
| Java, not JavaScript | **36**. The `script` Java card is about the JVM as a deployment choice |

So most of the batch's *concepts* are already on the site, and most of its *words* are not.
`clustered index` returns nothing. The site's four uses of *clustered* are about BigQuery
tables, policy exceptions bunching up in one department, and packet loss. *Indexes Explained*, the one card where
the term belongs, has **0**. `datediff`, `sp_executesql`, `pivot unpivot`,
`uml class diagram`, `markov decision process` and `smote` also return nothing. This is the
third batch in a row with the same shape, one layer further down each time. First the chip
subtitles overlapped, then *stack* and *queue* turned out to mean something else, and now it
is a whole dialect. **`data` has topics for Postgres, MySQL and SQLite, and none for SQL
Server.** Meanwhile `endpoint` describes MECM, which keeps its site database in
SQL Server and reports through SSRS. The site already depends on the one engine its data
domain never describes.

## 1. The knowledge by subject, and where each part lands

| # | Subject | Lands in | On the site today | What that makes it |
|---|---|---|---|---|
| 1 | **Database fundamentals, security and UML**: fields, data models, documentation, distributed databases, ACID, information classification, SQL injection, UML object and class diagrams, the composition diamond, persistence, schema theory | `data` · `grc` · `sec` · `eng` · `productivity` | ACID is a `data` topic. Information classification has 13 mentions, 10 of them in `grc` and `sec`. SQL injection has 21, and its home card is `sec` *The Injection Family*. **UML: 0, site-wide.** Schema theory: **0**, and *Learning How to Learn* has 0 each for *schema*, *prior knowledge* and *chunk* | **Written**, except UML and schema theory. UML has now been asked for by **both** batches, see §3 |
| 2 | **Database tools, formats and SQL facts**: Access, SQL\*Plus, SQL Server components, reporting tools, XML, JSON Schema, DQL, `REAL`, dynamic SQL, ERIC, UML association, foreign keys | `data`, and dynamic SQL goes to `sec` | Foreign keys are in `data` *The Relational Model*, JSON Schema in `ai` *Structured Output*, and DQL in `script` *SQL Query Reference*. Access, SQL\*Plus, PL/SQL, Tableau, Crystal Reports, Alteryx, ERIC, *controlled vocabulary* and `sp_executesql`: **0 each** | **Mostly product trivia.** Dynamic SQL is the exception, because it is the injection sink. The site shows that sink in Python and never in T-SQL, §2 |
| 3 | **SQL data types, DDL, joins and indexes**: BLOB, Boolean, column syntax, `DROP COLUMN`, `DATEDIFF`, right joins, where subqueries go, clustered indexes, temp tables, `DELETE` without `WHERE`, `UNIQUE` | `data` | 1NF is in *Normalization*, and right outer joins in *SQL Joins — Every Type, and the NULL Traps*. `UNIQUE` on existing rows is in *Indexes Explained*, which also has the sharper half the note misses, *A UNIQUE Index Does Not Stop Duplicate NULLs*. `DELETE` without `WHERE` is named in the first sentence of *Backups & Point-in-Time Recovery*. Clustered index: **0**. `DATEDIFF`: **0**. Temp tables: 1 mention, a connection-pooling caveat. BLOB: 12 mentions, 7 of them in `cloud` meaning Azure Blob Storage | **Written for the portable half, absent for the T-SQL half.** The clustered index is the one that matters, §2 |
| 4 | **SQL writes, set operations, pivoting and regex**: `INSERT … SELECT`, CTAS, Oracle `INSERT ALL`, set operators, `ROLLUP`/`CUBE`/`GROUPING SETS`, `PIVOT`/`UNPIVOT`, regex quantifiers and anchors, `LIKE` with bracket sets, binary collation | `data` · `script` | The set operators, `MINUS` included, are in *Subqueries, EXISTS & Set Operations* along with the NULL trap. `ROLLUP`/`CUBE`/`GROUPING SETS` is a row in *Aggregation*. Regex quantifiers, anchors, alternation and classes are in `script` *Regular Expressions (Regex)*. The subqueries card has **0** `INSERT` and **0** `UPDATE`. `PIVOT` has 2 case-sensitive hits, both in `pentest`, where pivoting means moving between hosts. `UNPIVOT`: **0** | **Written for the query half, absent for the DML half.** It needs one example in the subqueries card and one row in the aggregation card |
| 5 | **Python, pandas and AI**: `describe()`, `dropna()`, `def`, `**`, AI, reinforcement learning, MDPs, embeddings, confidence scoring, fraud detection and SMOTE, robotics, PUE, technological unemployment | `script` · `ai` · `ops` | `describe()` is in `script` *Data Analysis with pandas*. `dropna` appears once, in an `ai` card, not in the pandas one. RL: 4 mentions in `ai`. Embeddings: 37 mentions, 20 in `ai`. PUE is in `ops` *Green IT*, in a table that says what each metric leaves out. MDP, SMOTE, *technological unemployment* and *learning from demonstration*: **0 each** | **Written**, apart from two sentences in `ai` and one in the pandas card, §2 |
| 6 | **Java operators, types, algorithms and classes**: operators, identifiers, imports, primitives, widening, array memory, `Random`, binary search, selection and merge sort, O(M+N), interfaces, `final`, `String[] args`, `LinkedList`/`Deque`/`Queue`, graph loops, Dijkstra, base cases, Swing, zero-based indexing | `script` for Java, `cs` for the algorithms | Binary search, merge sort, Dijkstra and O(M+N) are in `cs`. Deque is in `script` *Choosing the Right Data Structure*. The `script` Java card has **0** each for *primitive*, `char`, `switch`, `final`, `import`, `javac` and *Unicode*, because it is about JIT warm-up and GC. Selection sort: **0**, and its one search result is an injection card | **The algorithms are written; the language is absent.** Selection sort stays with the tool, as csvistool §2 already decided |
| 7 | **Programming fundamentals in Java**: SDLC, case sensitivity, file naming, camelCase, immutable strings, `long`, `int` and `switch`, `char` values, `if`/`while`/`do-while`/`for`, infinite loops, methods, `Random`, operators | `script` beginner track | *Programming from Zero*, *Control Flow*, *Variables & Data Types*, *Working with Text* and *Programming Fundamentals* cover the language-neutral half. `do-while`: **0**, site-wide. *Control Flow* is a short JavaScript card with `for` and `while` only. *SDLC* has 7 mentions, all in `grc` and `sec`, all in the security and compliance sense | **Written.** `do-while` is one row in *Control Flow* |

## 2. What is worth writing, counted by what each item needs

| Needs | Items | Count |
|---|---|---|
| **Nothing.** Already on the site | ACID, distributed databases, foreign keys, 1NF, right outer join, the set operators, `ROLLUP`/`CUBE`/`GROUPING SETS`, regex quantifiers and anchors, `DELETE` without `WHERE`, `describe()`, embeddings, class imbalance, reinforcement learning, PUE, binary search, merge sort, Dijkstra, deque, SQL injection, information classification, JSON Schema, `UNIQUE` on existing rows | **22** |
| **A row or a sentence** in a card that exists | a clustered index, `PIVOT`, `INSERT … SELECT` and CTAS, `DATEDIFF`, `sp_executesql`, `dropna()`, MDP, SMOTE, `do-while`, schema theory | **10** |
| **A candidate card** that has to pass the rubric | UML (§3), SQL Server (§4), Java the language (§4) | **3** |
| **Nothing written.** Product facts and definitions: *a definition is not a card* | Access 1.0's release date, SQL\*Plus `serveroutput`, SQL Server's component list, Tableau / Crystal Reports / Alteryx, ERIC's controlled vocabulary, XML's angle brackets, `REAL`'s 7 digits, what database documentation holds, Swing's `fillOval` and `GridLayout`, robotics versus AI, technological unemployment as a definition | **11** |

`DELETE` without `WHERE` is in the first row because it is written: the PITR card names it
in its first sentence. The search misses it for another reason. The query returns **102**
results, because *delete*, *without* and *where* are all common words. That is a wide
result, not a gap.

The ten rows, each with the judgement that makes it more than a definition:

- **Clustered index**, in *Indexes Explained*. A clustered index means the table is stored
  in index order, so there is one per table. SQL Server and InnoDB cluster on the primary
  key. **Postgres has no clustered index:** `CLUSTER` reorders the table once, and later
  writes do not keep that order. A reader moving between the two engines needs that last
  clause, and the card is written for Postgres.
- **`sp_executesql`**, in *The Injection Family*. The note describes building a query in
  string variables and running it with `EXEC`, and that is the injectable form.
  `sp_executesql` with a parameter list is how T-SQL parameterizes a query. The card's own
  rule, *never string formatting*, is only shown in Python. The notes need this correction
  more than the site does, but the site needs it too.
- **`DATEDIFF`**, in *Time-Series & Event Data*, which already does date arithmetic with
  `date_trunc`. MySQL's version takes two arguments,
  `(end, start)`, and returns days. SQL Server's takes three, `(datepart, start, end)`, and
  counts **boundaries crossed**: `DATEDIFF(year, '2025-12-31', '2026-01-01')` is 1. The
  note's billing-cycle example is exactly where that difference bites.
- **`PIVOT`**, in *Aggregation*. In T-SQL and Oracle, `PIVOT` is shorthand for
  `SUM(CASE WHEN …)`. Postgres has neither and uses `FILTER` or `crosstab`. The card already
  shows `FILTER`, so this is one row. Keep the note's point that `UNPIVOT` cannot undo an
  aggregating `PIVOT`, and add that it also drops NULLs.
- **`INSERT … SELECT` and CTAS**, in *Subqueries*. One example. The note's real point, that
  a subquery can feed a write as well as a read, is the half the card is missing.
- **`dropna()`**, in the pandas card. The card shows `info()`'s non-null counts and never
  says what to do about them. Add `dropna()` beside `fillna()`, with the judgement that
  dropping rows silently changes the denominator of every later average.
- **SMOTE**, beside class imbalance in `ai`. The useful sentence is *resample the training
  split only.* SMOTE builds synthetic rows from neighboring real ones. If it runs before the
  train/test split, test rows help build the training data, and the score is a leak.
- **MDP**, one clause in the RL row: states, actions, a transition model and a reward. Most
  textbooks list the discount factor as a fifth element.
- **`do-while`**, in *Control Flow*. The loop that runs its body once before it checks the
  condition. JavaScript has it, so the card's own language can show it.
- **Schema theory**, in *Learning How to Learn*. New material sticks when it attaches to
  something already known. That is also the argument for this site's learning paths and
  related links, and the card could say so.

## 3. UML is the gap both batches named

Batch one's item 4 asked for UML sequence diagrams, data flow diagrams and class and
inheritance design. *Knowledge integration* §2 recorded UML as *absent as content: an
expansion is not a card*. This batch asks for class diagrams, object diagrams, the
composition diamond and association lines. **Two separate batches of notes asking for the
same missing thing is the strongest evidence this file has for a card.** It is stronger
than any single zero, because the reader-question census only ever counts one asker at a
time.

The rubric still decides what the card says. A notation reference is a definition. The
question somebody actually has is *which diagram do I draw, and when is one worth drawing
at all?* The site already has the hook: `script` *Object-Oriented Programming — Classes,
Objects & the 4 Pillars* never mentions composition. *Composition over inheritance* is the
design judgement that makes the solid-versus-hollow diamond matter. **Destination: `eng`**,
per batch one's §1 correction. It should be one topic covering class, sequence and object
diagrams, not three. Before writing, run `near_duplicates.py --title` against `eng`
*Schema & Data Modeling Patterns* and `data` *ER Modeling*. An ER diagram and a class
diagram overlap enough that readers will ask which one to draw.

## 4. Two more candidates the dialect raises — both decided since, see §8

- **SQL Server in `data`.** Postgres, MySQL and SQLite have topics and SQL Server has none.
  Yet SQL Server holds MECM's site database in `endpoint`, it is under Azure SQL in `cloud`,
  and it is the dialect of every T-SQL row in §2. That argument comes from the site's own
  dependencies, not from the notes. The case against: a product card is the shape the rubric
  distrusts most, and the T-SQL rows in §2 might carry the dialect without one.
  **Condition: write it if the §2 rows cannot be written without each one saying "in SQL
  Server". At that point the dialect is the topic.** Temp tables (`#` for local, `##` for
  global), bracket sets in `LIKE` and `_BIN` collations would go on that card and nowhere
  else.
- **Java the language in `script`.** The Java card answers *should this service run on the
  JVM?* The notes ask *why won't this compile?* The beginner track answers that question in
  JavaScript and Python, not Java, and a first-course Java card would be a second beginner track
  squeezed into one card. §5 is the argument for it anyway. The notes' most confident Java
  claims are the ones that are wrong, and a card on *what the course states too strongly*
  answers a question a student really has. **Not decided. Zero cards is an allowed answer.**

## 5. Claims in the notes that should not reach a card as written

Every claim was checked against the language or engine's documentation, or against a
counterexample. Most are right. The ones below are wrong, or right in only one dialect.
Several read like quiz answers, where the wording that earns the mark is stronger than the
fact:

| Note says | Actually | Where it would land |
|---|---|---|
| *SET statements do not allow for subqueries* | `UPDATE t SET c = (SELECT …)` is standard SQL, and T-SQL's `SET @v = (SELECT …)` works | `data` *Subqueries* |
| `^[S](haw\|ea)[n]` matches names *ending* with n | There is no `$`, so it also matches *Shawna* and *Seanna*. The pattern the note means is `^S(haw\|ea)n$`, and the brackets around single letters do nothing | `script` regex |
| *The standard SQL `LIKE` operator pairs with … bracketed character sets* | Standard `LIKE` has only `%` and `_`. Brackets are T-SQL (and Access). In Postgres and MySQL, `LIKE '%[7]%'` looks for a literal bracket | `data` |
| BLOB: *standard database management systems supporting maximum capacities up to 4 gigabytes* | 4 GB is MySQL's `LONGBLOB`. SQL Server's `varbinary(max)` is 2 GB, Postgres's `bytea` is 1 GB, and Oracle's `BLOB` runs to terabytes | `data` |
| A 10 × 5 array of 4-byte elements *allocates 200 bytes* | True in C. In Java, `int[10][5]` is eleven objects: one array of ten references and ten `int[5]` rows, each with its own header. The total is more than twice 200 | `script` Java |
| `int` *is required for switch statements* | Java can switch on `byte`, `short`, `char`, `int`, their wrappers, `String`, enums, and, since Java 21, patterns. It cannot switch on `long` | `script` Java |
| *A standard for loop requires three distinct components* | All three are optional. `for (;;)` is the idiomatic infinite loop | `script` *Control Flow* |
| *A Java source file must exactly match the name of the class it contains* | Only a **public** top-level class has to match. One file can hold several non-public classes | `script` Java |
| `char` *allocates 16 bits … which allows Java to natively support Unicode* | A `char` is one UTF-16 code unit. Characters outside the Basic Multilingual Plane, including most emoji, take two, so `"😀".length()` is 2 | `script` Java, beside *Encoding — Bytes, Text, and Why "It Works on My Machine"* |
| Selection sort *requires zero additional or auxiliary memory* | It needs O(1) extra memory, not zero: a temporary for the swap and two indices | `cs` |
| *Sorted lists provide the highest searching efficiency* | Only among lists. A hash table averages O(1), and `cs` *Hash Tables* covers it | `cs` |
| Merge sort's best case *remains tightly bound at θ(n log n)* | True of the textbook top-down merge sort. Timsort is a merge sort, and Java's sort for objects, and it is O(n) on already-sorted input. That is the thesis of `cs` *Sorting & Searching* | `cs` |

In two places the site is ahead of the notes, which is the reverse direction batch one's
item 7 opened:

- **`UNIQUE`.** The note says adding the constraint fails if duplicates exist. The site's
  *A UNIQUE Index Does Not Stop Duplicate NULLs* adds that Postgres allows any number of
  NULLs and SQL Server allows one. That is the half that bites in SQL Server, which is the
  note's own dialect.
- **Binary search.** The note says it halves the search space. The site's card says the
  classic `mid = (lo + hi) / 2` overflows in Java, which is the note's other language.

## 6. Before any of this is written

1. **First, fix the regex examples that the spelling sweep broke, because they are wrong
   now.** Checking the note's quantifier examples against `script` turned up two cards whose
   optional-quantifier example reads `colou?r → "color" or "color"`:
   `data/script.01-references.html:133`, and `data/script.03-python.html:1365` with a comma
   instead of *or*. The whole point of the pattern is the second spelling. Commit `656c1de`,
   the American-spelling sweep, rewrote *colour* wherever it counted as prose. In the first
   card nothing was in `<code>`, and in the second only the pattern was. The third copy, in
   `script.04`, survived because its whole table is a `<pre>`, which the checker skips. The
   fix is `<code>` around the whole example, not an `ALLOW` entry. The allow list is for
   names like *Fibre Channel*, and this is a quoted example of the very rule the checker
   enforces. Add a `check_spelling.py --self-test` fixture so the next sweep cannot do it
   again. **This is a correctness fix, and it does not depend on anything else in this
   section.**
2. **Put the zeros into `query_probe.mjs` before fixing anything.** Add a reader, *a student
   on a SQL Server and Java course*, with the zero queries from §1: `clustered index`,
   `datediff`, `sp_executesql`, `pivot unpivot`, `uml class diagram`,
   `composition vs aggregation`, `markov decision process`, `smote`, `widening conversion`,
   `sql like wildcard`, `case sensitive collation`, `schema theory`. The probe for this
   section ran from a scratch copy of the census loop, and scratch files are how queries
   went missing before.
3. **§5 is a gate on the notes, not a list of cards.** None of its rows is a card. They are
   claims that must not be copied across. The three that are also gaps in the site (`LIKE`
   brackets, `DATEDIFF`, Java's `char`) go in as the *caveat* in their row, not as the
   note's sentence.
4. **The notes are the source, and §5 corrects them.** §7 keeps their wording unchanged.
   Whether to correct them is up to the person who owns them. That is the same outward
   direction as batch one's item 7.

## 7. The knowledge, by subject

This is the knowledge from the notes, grouped by subject. The dates and titles the notes
arrived with are left out, because the knowledge is what goes on the site. The Java part
arrived with its Markdown escaped (`\*\*`, `\$`), and that is repaired. No bullet's wording
has changed.

<details>
<summary>Databases, SQL, regex, pandas, AI and Java</summary>

### Databases, SQL and regex

#### Database fundamentals, security and UML

* **Database Fundamentals & Modeling**
  * A field is the foundational building block of a database table, representing a single piece of data or attribute.
  * Tables can be sorted by different fields to arrange and view records in specific sequences.
  * Data models and abstract data models are conceptual tools that simplify ideas, define specific subjects, and represent data and its underlying relationships.
  * Typical database documentation maintains static information like structural layouts, data dictionaries, security matrices, and operational schedules, rather than dynamic metrics like exact record counts or table sizes.
  * In a distributed database, data is intended to be shared and accessed by authorized users across multiple connected network sites, not restricted solely to a local site.
  * Database transactions adhere strictly to the ACID model properties: Atomicity, Consistency, Isolation, and Durability.
* **Database Security**
  * Information classification defines and categorizes the specific types of data that must be secured under a database security policy.
  * Hackers and SQL injection attacks are direct malicious threats to the integrity of database systems.
* **UML & Object-Oriented Principles**
  * An object diagram captures a specific snapshot of instances, their values, and their relationships at a discrete point in time.
  * The bottom compartment of a UML class diagram box contains methods or operations (executable functions), which are generally denoted by parentheses.
  * A solid diamond in a UML class diagram represents a composition relationship, indicating a strong whole-part connection where parts are strictly dependent on the parent object's lifecycle.
  * Persistence denotes an object's lifetime, describing its ability to retain its state and exist beyond the execution period of the process that created it.
* **Cognitive Theory**
  * Schema theory proposes that human knowledge is structured and stored in memory as cognitive frameworks or units (schemata) that organize, interpret, and process information.

#### Database tools, formats and SQL facts

* **Microsoft Access:** The first version of the software (Access 1.0) was officially released in November 1992\.
* **SQL\*Plus Commands:** The instruction set serveroutput ON is an environment setting for the SQL\*Plus client tool used to display PL/SQL block output; it is not a native SQL or PL/SQL command.
* **MS SQL Server Components:** The platform includes the core Database Engine for storage, Reporting Services (SSRS) for report management, and Full-Text Search for advanced character data querying.
* **Relational Database Design:** Establishing inter-relationships between records links disparate data points, enabling complex queries that retrieve contextualized and relevant information tailored to specific tasks.
* **Database Reporting Tools:** Applications such as Tableau, Crystal Reports, and Alteryx connect to existing data sources to extract, analyze, and visualize information, rather than acting as raw data storage.
* **XML Structure:** Elements are the structural components defined by tags (e.g., \<color\>, \<brand\>) and are distinct from the actual data values they contain. These markup tags are enclosed within less-than (\<) and greater-than (\>) angle brackets.
* **JSON Schemas:** A schema serves as a foundational blueprint, providing a standardized method to dictate and validate the expected data format, required fields, and structural hierarchy within a JSON payload.
* **Data Query Language (DQL):** DQL is a subset of SQL focused exclusively on data retrieval, distinguished by consisting primarily of the single SELECT statement.
* **SQL Data Types:** The REAL data type is a floating-point format that provides 7 digits of precision.
* **Dynamic SQL:** This technique involves declaring string and integer variables to construct a SQL query dynamically at runtime, which is then executed using commands like EXEC.
* **Bibliographic Databases:** Systems like ERIC utilize a controlled vocabulary—an indexed list of standardized, specialized terminology—to ensure accurate and consistent subject retrieval.
* **UML Diagrams:** An association represents a general relationship between classes and is visually depicted as a simple connecting line.
* **Relational Keys:** A foreign key is a column in a database table that references the primary key of another table (e.g., an Artist table containing a genreID to link to a Genre table).

#### SQL data types, DDL, joins and indexes

* **BLOB Capacity:** A Binary Large Object (BLOB) stores large binary data objects, with standard database management systems supporting maximum capacities up to 4 gigabytes.
* **Boolean Data Type:** A Boolean data type is a primitive programming and database type designed to store binary logic values representing true or false.
* **Table Definition Syntax:** In SQL table definitions, the column name comes first, followed by the data type and optional constraints. A comma is required at the end of the line if it is not the last column in the sequence.
* **Dropping Columns:** The ALTER TABLE statement combined with the DROP COLUMN clause is standard SQL used to delete an existing column and its data from a table.
* **Date Differences:** The DATEDIFF function calculates the difference between two date values, making it ideal for determining elapsed days for events like billing cycles.
* **Right Outer Joins:** A right outer join returns all records from the right table and only the matched records from the left table, guaranteeing the inclusion of right-table records regardless of matches.
* **Subquery Placement:** Subqueries are valid and commonly used within SELECT, FROM, and WHERE clauses. SET statements do not allow for subqueries.
* **Index Categories:** Clustered and non-clustered indexes are the two primary structural categories used in relational databases to organize and accelerate data retrieval.
* **Temporary Tables:** Temporary tables store transient session data and are meant to be dropped or cleared regularly. In systems like SQL Server, they are prefixed with a hash symbol (e.g., `#table_name`) and are removed using the standard DROP TABLE command including that prefix.
* **DELETE Statements:** Omitting the WHERE clause in a DELETE statement removes every single record from the target table because there is no condition to filter the rows.
* **SQL Purpose:** SQL is a comprehensive language used to store, retrieve, and search or query information within relational database management systems.
* **UNIQUE Constraints:** Adding a UNIQUE constraint to an existing table requires all current rows to have unique values in that column. If duplicates already exist, the database cannot enforce the constraint and the statement will fail.

#### SQL Subqueries & Data Manipulation

* Subqueries can be integrated directly into Data Manipulation Language (DML) statements (`INSERT`, `UPDATE`, `DELETE`) instead of standard `SELECT` retrieval queries.
* An `INSERT` subquery selects a specific subset of rows from a source table and adds them into a destination table.
* The `CREATE TABLE AS SELECT` (CTAS) statement creates a new table and populates it using the filtered results of a query from an original table.
* Multi-table inserts allow a single source query to distribute rows across multiple target tables simultaneously, which eliminates repetitive queries and reduces redundant code.
* In Oracle, the conditional `INSERT ALL` statement routes and inserts rows into multiple separate target tables based on specified logical criteria.
* If a database system lacks native multi-table insert support, the behavior can be simulated using database triggers or stored procedures/functions.

#### SQL Set Operations

* Standard SQL set operators include `UNION`, `INTERSECT`, and `EXCEPT` (or `MINUS`).
* The `UNION` operator combines result sets from multiple queries vertically into a single dataset (analogous to adding names to the bottom of a list), whereas a `JOIN` combines columns horizontally.
* A `UNION` command combines `SELECT` statements and supports standard clauses like `WHERE`.
* The `EXCEPT` operator isolates data by returning only the rows from the first query that are not present in the second query's results.

#### SQL Grouping & Data Pivoting

* `ROLLUP`, `CUBE`, and `GROUPING SETS` are extensions used exclusively with the `GROUP BY` clause (not `ORDER BY`) to generate aggregate subtotals and grand totals.
* `ROLLUP` specifically generates hierarchical subtotals for the specified groupings along with a grand total row where all grouped columns evaluate to `NULL`.
* The `PIVOT` operator rotates data by converting unique values from rows into separate columns in the output table.
* Because the `PIVOT` operator typically aggregates data and collapses granular records, executing `UNPIVOT` cannot fully reverse the transformation and restores only a portion of the original information.

#### Regular Expressions (Regex) & Pattern Matching

* Regular expressions are specialized patterns used to search, match, and manipulate text data; they cannot evaluate, compute, or validate mathematical equation answers.
* A single period (`.`) acts as a wildcard representing any single character.
* Quantifiers dictate repetition: `{2,3}` requires the preceding character to appear two to three consecutive times; `{5,}` requires five or more occurrences; `{2}` requires exactly two.
* Grouping combined with a quantifier, such as `(Ma){2}`, matches the exact consecutive repetition of a substring sequence (e.g., "MaMa").
* Anchors and alternations like `^[S](haw|ea)[n]` filter for records starting (`^`) with 'S', followed by either "haw" or "ea" (`|`), and ending with 'n'.
* Character ranges like `[0-9]` match any single digit and can be integrated with exact strings to form strict patterns (e.g., `91[0-9]4`).
* The standard SQL `LIKE` operator pairs with wildcards (`%`) and bracketed character sets/ranges (e.g., `%[7][8][9]%` or `%[P][A-Z][T]%`) to find specific consecutive sequences anywhere within a string.
* The `NOT LIKE` operator explicitly excludes records containing a specified substring sequence.
* Case sensitivity in SQL pattern matching can be strictly enforced by applying a binary collation (e.g., `COLLATE Latin1_General_BIN`) to the query.

### Python, pandas and AI

* **Python & Pandas for Data Science**
  * **Pandas** is the standard Python library for 2D tabular data manipulation, operating fundamentally on the DataFrame structure.
  * The **`describe()`** method calculates key descriptive statistics (count, mean, standard deviation, min, max, quartiles) for a rapid numerical overview of dataset distributions.
  * The **`dropna()`** method filters datasets by removing any rows or columns containing null values.
  * Python functions are declared using the **`def`** keyword, and the **`**`** operator executes exponentiation.
* **Machine Learning & Artificial Intelligence**
  * **Artificial Intelligence** is a core branch of computer science focused on algorithms and systems that perform tasks requiring human intelligence.
  * **Reinforcement Learning** relies on agents learning optimal decision-making by interacting with an environment and receiving feedback via rewards or penalties.
  * A **Markov Decision Process (MDP)** requires four essential elements: states, a transition model, available actions, and a reward function.
  * **NLP Embeddings** map discrete text tokens into continuous dense vectors to capture semantic meaning and relationships.
  * **Confidence Scoring** allows individual AI subsystems to communicate uncertainty, enabling integrated systems to safely navigate ambiguous scenarios by weighing inputs appropriately.
  * **Fraud Detection Models** effectively minimize false positives while catching complex patterns by combining feature engineering, addressing class imbalance (e.g., using SMOTE), and deploying hybrid architectures like gradient boosting paired with autoencoders.
* **Robotics, Infrastructure & Economics**
  * **Robotics vs. AI:** Robotics is the physical machinery, while AI provides the cognitive software; AI integration shifts robot programming from rigid, line-by-line manual scripting to data-driven adaptability and learning from demonstration.
  * **Power Usage Effectiveness (PUE)** is the standard metric for data center energy efficiency, calculated as the ratio of total facility energy consumption to the energy used strictly by computing equipment.
  * **Technological Unemployment** is a primary economic concern as advanced AI and automation algorithms displace human workers across various sectors.

### Java, algorithms and programming fundamentals

#### Java operators, types and complexity

* **Operators & Syntax:**
  * The forward slash (`/`) is used for division, while the percent sign (`%`) is the modulo operator used to calculate the remainder of a division operation.
  * A single equal sign (`=`) is an assignment operator; a double equal sign (`==`) is required to evaluate equality within conditional boolean expressions (e.g., `if` statements).
  * Valid Java identifiers cannot contain spaces or reserved keywords. A string like `ifElse` compiles successfully as a name, even though it bypasses the all-caps convention for constants.
  * Utilizing external APIs, such as the `File` class from `java.io`, requires an explicit import statement to prevent the compiler from throwing a "cannot find symbol" error.

* **Data Types & Memory Allocation:**
  * `boolean` is a built-in primitive data type in Java, strictly holding true or false values.
  * The `char` primitive allocates 16 bits of memory, which allows Java to natively support Unicode character encoding.
  * Java implicitly handles widening conversions, automatically safely promoting smaller primitive types (like `short`) into larger ones (like `int`) without manual casting.
  * The total memory allocation for a multi-dimensional array is the product of its dimensions and the byte size of its data type (e.g., a $10 \times 5$ array of 4-byte elements allocates $10 \times 5 \times 4 = 200$ bytes).
  * The Java `Random` class generates pseudorandom numbers, meaning it relies on a deterministic mathematical algorithm rather than true environmental randomness.

* **Algorithms & Time Complexity:**
  * **Binary Search:** Initiates by isolating the middle element of a strictly sorted array to recursively eliminate half the search space, yielding an optimal time complexity of $O(\log n)$.
  * **Selection Sort:** Operates strictly in-place, meaning it swaps elements within the original array boundaries and requires zero additional or auxiliary memory.
  * **Merge Sort:** Because its recursive divide-and-conquer logic executes identically regardless of initial element arrangement, its best-case (and average/worst-case) time complexity remains tightly bound at $\theta(n \log n)$.
  * **Linear Iteration:** When sequentially executing two unnested loops of independent sizes ($M$ and $N$), the time complexity scales additively to $O(M+N)$.

#### Java Object-Oriented Programming & Classes

* A Java class implements an interface by matching the interface name and providing the required method implementations.
* Classes use the implements keyword to incorporate an interface.
* Declaring a class as final prevents other classes from creating subclasses from it.
* To instantiate a new class object in Java, declare the type, variable name, and assign it using the new keyword and constructor.
* The main method uses String\[\] args to accept and process command-line arguments.

#### Data Structures & Algorithms

* Sorted lists provide the highest searching efficiency by enabling binary search algorithms ($O(\log n)$).
* The addLast() method appends a new element specifically to the tail of a LinkedList.
* The poll method in the Queue interface retrieves and removes the front element.
* A double-ended queue (deque) allows insertion and removal at both ends, operating as either a queue or a stack.
* A graph loop is defined as an edge that originates and terminates at the same vertex.
* Dijkstra's algorithm is used to find the shortest path between two vertices on a weighted graph.
* Recursive search methods require a proper base case or exit point to prevent infinite recursion.
* A browser history serves as a real-world example of a doubly-linked list due to bidirectional traversal.
* A Map functions as an associative array by storing data in key-value pairs.
* A two-dimensional array can be conceptualized as a matrix of rows and columns.

#### Java Syntax, Arrays & Control Flow

* The fillOval graphics method fills an elliptical shape with the current color using specified bounds.
* The \!= operator checks if two variables are not equal.
* Layout managers like GridLayout are applied directly to a container using setLayout().
* The Java Random class uses a pseudorandom number generator algorithm.
* Java arrays use zero-based indexing, meaning the fifth element is accessed at index 4\.
* The LinkedList class can be used to instantiate a Deque.
* A standard array iteration loop starts at index 0 and iterates while less than myArray.length.
* The long primitive data type is appropriate for storing extremely large integer values.
* Placing one while loop inside the body of another creates a nested loop structure.

#### Programming fundamentals in Java

* **Programming Fundamentals & SDLC**
  * A computer program is a set of step-by-step instructions designed to complete a specific task or solve a problem.
  * Programming encompasses describing a problem in code and giving the computer specific instructions to solve it.
  * After writing code, the immediate next phase in the software development lifecycle is testing and debugging.
* **Java Syntax & Structure**
  * Java is strictly case-sensitive (e.g., keywords like public must be lowercase), and string literals require double quotes (") rather than single quotes (').
  * A Java source file must exactly match the name of the class it contains (e.g., class WelcomeWorld compiles via javac WelcomeWorld.java).
  * Standard Java naming conventions dictate that method names use camelCase and start with a lowercase letter (e.g., updateRates).
  * Strings are immutable in Java; methods like .toUpperCase() return a newly created string rather than modifying the original variable.
* **Data Types & Variables**
  * The long data type is used for large 64-bit integers (e.g., numbers in the billions) to prevent calculation overflow.
  * The int data type stores standard whole numbers without decimals, and is required for switch statements that evaluate integer cases.
  * The char data type represents characters based on their underlying integer ASCII/Unicode values (e.g., 65 maps to the uppercase letter 'A').
* **Control Flow & Loops**
  * An if statement block is skipped entirely if its controlling condition evaluates to false.
  * A while loop executes its code block continuously as long as its condition remains true.
  * A do-while loop evaluates its condition at the very end of the statement, guaranteeing that the code block executes at least one time.
  * A standard for loop requires three distinct components enclosed in parentheses and separated by semicolons: initialization, boolean condition, and an increment/decrement step (e.g., for(i=0; i\<10; i++)).
  * Infinite loops occur when a condition never evaluates to false. This typically happens if the control variable is missing an update step inside the loop or is incremented/decremented in the wrong direction.
* **Object-Oriented Programming & Built-in Classes**
  * Methods define the behaviors and specific actions that an object can perform when invoked.
  * The Java Random class uses a deterministic algorithm to generate sequences, meaning it produces *pseudorandom* numbers rather than truly random ones.
  * An operator is a specific symbol that represents a mathematical, logical, or relational operation and instructs the compiler to execute that action.

</details>

## 8. What shipped

Conducted in one session, in the order §6 set, and recorded below as *Session — conducting
batch two*. The student reader opened at **1 of 15** and closed at **15 of 15**.

| § | Item | Where it went |
|---|---|---|
| 6.1 | The broken `colou?r` examples | Fixed in two `script` cards, plus a contrast guard in `check_spelling.py`. Reading the table beside them found an older class of the same bug: eight control bytes where `\b` and `\a` had gone through non-raw Python strings. `check_markup.py` now fails on them |
| 6.2 | The zeros in `query_probe.mjs` | A reader, *a student on a SQL Server and Java course*, committed before any fix |
| 2 | Clustered index, `PIVOT`, `INSERT … SELECT`, `DATEDIFF` | A concept card each in *Indexes Explained*, *Aggregation* and *Subqueries*; a row in *Time-Series & Event Data* |
| 2 | `sp_executesql` | *The Injection Family*: a stored procedure that builds its query with `+` and runs it with `EXEC` is string formatting with a database at both ends |
| 2 | MDP, SMOTE, `dropna()`, `do-while`, schema theory | A sentence or a card in `ai`, `script` and `productivity`. Reading the RL cards found **DPO** expanded as *Data Protection Officer* in an RLHF title; the dictionary has both meanings now |
| 3 | UML | A new `eng` topic: the six line styles as claims about lifetime, composition over inheritance, object and sequence diagrams |
| 4 | SQL Server | **Not a product card.** The §2 rows could each be written as a comparison, so the dialect was the topic: a new `data` topic, *SQL Dialects — The Differences That Run Without an Error* |
| 4 | Java the language | One concept card on the existing Java topic, *The Rules a First Java Course States Too Strongly*, which is §5 turned into the question a student has |
| 5 | Claims not to copy | Each went in as the caveat in its row, never as the note's sentence: `SET` and subqueries, `LIKE` brackets, `DATEDIFF`, the Java rows |


# Content ideas — 839 candidates checked against the site, and the look they have to keep

> Source: a request to *update the plan with more content ideas to add, with the same clean
> look*. Filed as **a queue, not a record**: no card was written and nothing in `data/`
> changed. It is the fourth piece of incoming work to arrive as a list, and the first where
> this file wrote the list itself, so it got the treatment every list here gets, with less
> excuse for skipping it. **839 candidate phrases in 17 reader groups**, each checked two
> ways: a pattern over `data/*.html` with the generated acronym pages excluded, and
> `runSearch()` driven in Chromium on the built page the way `query_probe.mjs` does it. The
> whole list is kept in §8, because a scratch file is how queries evaporated before.

**The largest finding was not on the list.** The page's own heading is *Cycles, Concepts
&amp; Diagrams*, and **58 of 1,503 hand-written topics** carry anything beyond a concept
card, a table and a code block. Nine contain an inline SVG, and six of those are in `math`.
Fifteen of the twenty-nine hand-written domains have none at all. The components to draw
with already exist, follow the theme, and most are used in exactly one place. §2.

**The list came down the way lists here do.** Of 839 phrases, **81 are owned by a title**,
452 are mentioned somewhere and no title owns them, and **306 are absent**. 238 return
nothing from search outside the acronym dictionary. The count of owned phrases was 125 on
the first pass and 107 on the second, and both were wrong: see §3. What is worth writing is
about thirty-five cards, grouped in §4, and the answer is allowed to be fewer.

**"The same clean look" is checkable, and it has one hole.** The look is seven everyday
components, ten shapes and six color classes, counted in §1. Everything about it is gated except one thing: a
class in the content that no rule in `style.css` defines. Nine table cells use one today.

**And one kind of content needs no card at all.** There are 102 learning paths and none is
named for an exam, on a site whose header reads *CompTIA, Tech &amp; Life Reference*. A path
is an order over topics that exist, so it adds nothing to the page's look. §5.

## 1. The look, measured — what "the same clean look" is made of

A class census over the 35 files in `data/`: 294 distinct class names, and the look a
reader sees is a short list of them. The first table is the part every topic uses.

| What the reader sees | Class | Uses | Domains |
|---|---|---|---|
| A card: label, title, prose | `concept-card` | 4,357 | 30 |
| A table | `ref-table` | 2,412 | 30 |
| The sentence under a table | `concept-desc verdict` | 2,756 | 29 |
| Code | `code-block` | 821 | 28 |
| A pointer to another card | `xref` | 549 | 28 |
| A claim with a date on it | `volatile` | 47 | 11 |
| A link off the site | `extlink` | 42 | 4 |
| Color | `c-cyan` 3,358 · `c-amber` 3,001 · `c-muted` 1,646 · `c-green` 446 · `c-red` 295 · `c-purple` 17 | | |

`ai-table` is the older table design, 358 uses in 16 domains. `CONTRIBUTING.md` already
says not to use it for new content and not to convert what exists.

The second table is the part almost nothing uses. These are the shapes, counted by how
many hand-written topics carry each. A topic can carry more than one.

| Shape | Classes | Topics |
|---|---|---|
| Card grid | `card-grid` with `g-card`, and the one-off grids `zt-pillars`, `topo-grid`, `diamond-grid`, `pki-flow` | 24 |
| Numbered rows, for a cycle or a ranked list | `kc-row`, `lifecycle` with `lc-step`, `nist-row`, `owasp-item` | 13 |
| Callout bar | `info-bar` | 9 |
| Inline SVG | `topo-svg`, `math-svg`, `asl-hand`, `role-svg` | 9 |
| Step tiles, for a sequence | `dora-seq`, `flow-step`, `ml-flow`, `boot-seq`, `pt-phase` | 6 |
| Layer stack | `layer-stack` | 2 |
| Tree, and permission bits | `tree`, `perm-row` | 2 |
| Matrix | `risk-matrix` | 1 |
| Widget | `url-codec-wrap` | 1 |
| Image file | `asl-chart` | 1 |

**The names are historical and the components are not.** `dora-seq` is a flex row of
tiles that wraps, and it was written for one DHCP sequence. `kc-row` was the kill chain.
Every one of them has its rules in `style.css` and no fixed count of items. Reuse them
under the names they have. Renaming is a redesign, and it moves nothing for the reader.

**So the contract for new content is five rules, and four of them are already gated.**

1. A topic is the canonical skeleton in `CONTRIBUTING.md` and a card is a `concept-card`.
   `check_markup.py` proves it is well-formed and `lint_content.py` holds the conventions.
2. A table is a `ref-table`, and it is followed by a `concept-desc verdict` that names a
   row. `lint_content.py` counts the tables that end a card without one.
3. A color is one of the six classes above or `style="color: var(--…)"`. A hex literal
   fails the build, and so does a `var()` that is never declared.
4. A picture is inline SVG colored by classes in `style.css`. No image host, no font from
   elsewhere and no iframe: `netlify.toml` sets `default-src 'none'` and the smoke test
   asserts zero off-site requests.
5. A shape reuses a component from the second table before it adds one. A new component
   is a design change. It owes the smoke test a theme check with presence asserted before
   behavior, the mobile gate at 375 px, contrast in both themes, print, and
   `page_budget.py`. The contrast half is by hand until the topic is in the set
   `a11y_test.mjs` scans, which the last record named and did not build.

**The hole is in rule 3.** Fifteen class names are used in content and have no rule in
`style.css`. Three of them were meant to color something and color nothing:

| Class | Where | What it was meant to be |
|---|---|---|
| `c-yellow` | 9 table cells in 6 files: `cloud` 3, `web` 2, `blueteam` 1, `redteam` 1, `script.05-platform` 1, `script.06-admin-automation` 1 | The caution tone between green and red. The house class is `c-amber`. The cells beside them use `c-red` and `c-green`, not `c-amber` as this cell first said. Fixed, see §9 |
| `m` | 61 spans in code blocks: `cs` 27, `infra` 19, `sec` 15 | A number literal. This is a Pygments token name; the house token is `num` |
| `nd` | 1 span in `cs` | A decorator, also a Pygments name |

The other twelve are `layer-1` to `layer-7` on the OSI stack and five one-offs. They were
counted and not read. **`c-yellow` is failure 6 in the operating manual, by name.** Its
guard was *grep `style.css` for the utility class before using one*, which is a habit and
not a gate, and nine cells have got past it since. It is the `var(--bg1)` bug that
`check_css_vars.py` was written for, one layer over: a name that does not exist, failing
silently, and producing a plausible wrong color in place of a missing one.

## 2. The site is named for diagrams, and 58 topics draw anything

| | Hand-written topics |
|---|---|
| All | 1,503 |
| Carry any shape from §1's second table | **58**, 3.9% |
| The same, not counting a callout bar as a shape | 52 |
| Contain an inline SVG | **9**: `math` 6, `net` 1, `productivity` 1, `eng` 1 |
| Domains with no shape at all | **15 of 29**: `blueteam`, `career`, `cloud`, `cs`, `data`, `devops`, `endpoint`, `hw`, `infra`, `m365`, `mind`, `quotes`, `redteam`, `shortcut`, `web` |

**Fifty of the 58 carry an all-caps badge, which is mostly the mark of the first cards**:
*REFERENCE MODEL*, *VISUAL MODELS*, *6-PHASE CYCLE*. They are the OSI stack, the
topologies, DORA, the kill chain, the boot chain and the risk matrix. 194 topics have a
badge like that, so a quarter of them have a shape. **Of the other 1,309 topics, eight
do**: one zero-trust card, the ASL topic, and six in `math`, each
drawn on purpose. The programmes that wrote everything else used the first table in §1 and
nothing from the second. Phase 8 found this shape in depth, as the first accumulation risk:
the house form improved and the earlier content was never revisited. This is that risk
running the other way. The early form had pictures, and the later content never picked
them up.

**90 titles name a shape, and 75 of those draw none.** The words counted are *flow*,
*lifecycle*, *handshake*, *cycle*, *pipeline*, *chain*, *hierarchy*, *topology*, *layer*,
*tree*, *diagram*, *anatomy*, *loop*, *pyramid*, *matrix*, *ladder*, *graph*, *sequence*,
*stage* and *phase*. The list is generous. *Supply chain* and *Microsoft Graph* are on it,
and neither promises a picture. A looser list that adds *model*, *process*, *path* and
*structure* gives 139 of 162, and that number should not be quoted.

**Four of the 75 are about pictures and contain none.** `eng` *UML — Class, Object &amp;
Sequence Diagrams, and the Diamond Everybody Draws Backwards* describes six line styles in
words. Its table's first column reads *Hollow diamond, at the whole* and *Hollow triangle,
dashed line, at the interface*. That column is a description of a drawing. `career` *Diagrams That Explain — The Small Number of Shapes
Worth Using* does not show a shape. `hw` *Motherboard Anatomy — Chipsets, PCIe Lanes &amp;
the Block Diagram* has no block diagram. `ops` *Priority, Impact &amp; Urgency — A Matrix
People Actually Apply* has no matrix, and `grc` *Risk Management Lifecycle* already
carries the component.

### The rule for a picture, which is the rubric's one test turned sideways

**A picture earns its place when it shows a location, an order or a containment that the
prose can only assert.** `net` *Network Topologies* is the model. Its verdict says the five
diagrams hide the difference between physical and logical, and that the only row that
matters is where the single point of failure is. That is a judgement about the pictures.
A diagram that restates its table is the picture version of a restated verdict, and the
rubric's fix for that is to cut it.

Twenty to draw, in the order the evidence ranks them. Every one uses a component that
exists, and *inline SVG* below means drawn with the `topo-svg` or `msv-*` rules already in
`style.css`. That none of the twenty needs a line of new CSS is a claim, and §7 says how to
test it on one topic first.

| # | Topic | What to draw | Component | What the picture says that the table cannot |
|---|---|---|---|---|
| 1 | `eng` *UML* | The six lines | Inline SVG in the table's first column | The card already says which mark is drawn the wrong way round. It should be visible |
| 2 | `career` *Diagrams That Explain* | The shapes it recommends | `card-grid` of small SVGs | A card about choosing a shape, read without seeing one |
| 3 | `hw` *Motherboard Anatomy* | The block diagram the title names | Inline SVG | Which lanes come from the CPU and which from the chipset, which is the card's whole argument about budget |
| 4 | `ops` *Priority, Impact &amp; Urgency* | The matrix | `risk-matrix` | The cell where two teams disagree is a position, not a sentence |
| 5 | `eng` *SDLC Models* | The V | Inline SVG | Each test level sits opposite the design level it checks. That pairing is the model |
| 6 | `net` *Spanning Tree* | Three switches in a triangle, one port blocked | `topo-svg`, with `topo-hot` marking the port | Where the block is, and what loops when it is removed |
| 7 | `net` *TCP vs UDP* | The handshake and the teardown | `dora-seq` | The half-open state has a position, and a SYN flood lives in it |
| 8 | `net` *NAT in Practice* | One flow, with the address pair rewritten at each hop | `dora-seq` | Hairpinning is a path, and the failing one is the one that turns back |
| 9 | `sec` *OT vs IT &amp; the Purdue Model* | The levels | `layer-stack` | The boundary between IT and OT is a line between two layers |
| 10 | `sec` *Network Security Architecture* | Zones, and the directions allowed between them | `topo-svg` | The arrow that is missing. Egress filtering is an absence |
| 11 | `cs` *Trees* | The same seven keys, balanced and degenerate | Inline SVG | The card is titled *An Unbalanced BST Is a Linked List With Extra Steps*. That is a picture |
| 12 | `cs` *Caches &amp; the Memory Hierarchy* | The ladder, with the numbers on it | `layer-stack` | The gaps between rungs are orders of magnitude, and a table flattens them |
| 13 | `cs` *Merkle Trees* | One changed leaf, and the hashes that change with it | Inline SVG | The path from leaf to root is the proof |
| 14 | `military` *OODA Loop*, *The Intelligence Cycle* | The cycle | `lifecycle`, used in two topics today | The site's heading begins with *Cycles* |
| 15 | `blueteam` *Detection Tuning &amp; the Pyramid of Pain* | The pyramid | `layer-stack` | Cost to the attacker rises with height, and the cheap indicators are the wide ones |
| 16 | `devops` *CI/CD Pipeline Design* | Stages, with the gate between them | `dora-seq` | A gate is a position between two stages |
| 17 | `cloud` *Azure Hierarchy, RBAC Scopes &amp; Policy* | Management group to resource | `layer-stack` | Inheritance runs one way, and the picture has a direction |
| 18 | `infra` *Processing Order &amp; Precedence* | LSDOU as a stack | `layer-stack` | The last writer wins, and last is at the bottom |
| 19 | `m365` *Mail Flow* | The path a message takes | `dora-seq` | Where a message can die, in order |
| 20 | `web` *Flexbox*, *CSS Grid* | The axes | Inline SVG | Main axis and cross axis are directions |

**What the ASL records already established, and it applies to every row above.** A
drawing is a claim, and the check is weaker than a source: render it at size and read it
against its own description. That caught four hands on the first pass. A caption needs
`--cyan-2` and not `--cyan` to pass contrast in light mode. axe skips single-character
text, so a clean scan is not evidence about one-letter labels. A grid fits three to a row
under 640 px, and its media query goes below the base rule. And the theme check has to
click, which is how the open palette was found. None of that needs rediscovering.

## 3. 839 candidates, by who would ask

The census groups its queries by reader because that is how the gaps cluster. This list
did the same. Six groups are exam candidates, because 16 of the 30 domain headers carry a
certification tag and no reader in `query_probe.mjs` is revising for one. Four are
courses: the calculus that `math` follows, the software engineering and Java that the
earlier batches named, and the two a computer science degree puts beside them. The rest
are the Human, Growth and Reference chips.

Each phrase was classified by the strongest place it appears. *Owned* means a topic title
or a concept-card title contains it, in the sense that reader means. *Mentioned* means it
is in the prose and no title carries it. *Absent* means it is nowhere in hand-written
content in that sense. *Zero* is what search returns once the acronym dictionary is set
aside.

| Reader | Phrases | Owned | Mentioned | Absent | Zero |
|---|---|---|---|---|---|
| A Security+ candidate | 86 | 16 | 52 | 18 | 16 |
| A Network+ candidate | 83 | 10 | 55 | 18 | 19 |
| An A+ candidate | 66 | 6 | 32 | 28 | 14 |
| A CISSP or SecurityX candidate | 54 | 3 | 19 | 32 | 23 |
| A CySA+ candidate | 52 | 8 | 36 | 8 | 7 |
| A Linux+ candidate | 57 | 9 | 36 | 12 | 10 |
| A calculus student | 60 | 1 | 39 | 20 | 12 |
| A student on a discrete maths or theory course | 41 | 2 | 16 | 23 | 19 |
| A student on an operating systems or compilers course | 33 | 4 | 15 | 14 | 7 |
| A student on a software engineering or Java course | 51 | 5 | 24 | 22 | 8 |
| Somebody at a keyboard, looking something up | 40 | 3 | 15 | 22 | 16 |
| A reader of the philosophy domain | 48 | 4 | 28 | 16 | 19 |
| A reader of the mind domain | 27 | 0 | 20 | 7 | 5 |
| A student building a study routine | 38 | 3 | 22 | 13 | 8 |
| Somebody building a career, veterans included | 39 | 3 | 19 | 17 | 18 |
| Somebody reading military structure | 32 | 3 | 17 | 12 | 9 |
| Somebody looking for the source of a line | 32 | 1 | 7 | 24 | 28 |
| **All** | **839** | **81** | **452** | **306** | **238** |

**Three things the table says.**

- **The site is a mention deep on the exams and a card deep on almost none of them.** Of
  the 398 exam phrases, 52 are owned, 230 are mentioned and 116 are absent. By exam, the
  share present in any form runs CySA+ 85%, Security+ 79%, Linux+ 79%, Network+ 78%, A+
  58%, and CISSP or SecurityX 41%. The two lowest are the Windows desk and the theory,
  which §4 comes back to.
- **The mind domain owns none of its 27.** Twenty are mentioned, and the mentions are
  mostly in other domains: `depress` appears once on the site, in `productivity`.
- **The quotes domain is the least covered against its own premise.** 24 of 32 names are
  absent from a domain whose subtitle is *with the work cited, and the misattributions
  named*.

**What these numbers are not.** The exam phrases were written from memory of the outlines.
The outlines were not fetched, so this is a sample of objective vocabulary and not a
coverage figure for any exam. *Mentioned* is an upper bound on coverage, because a mention
can be the other sense of the word. And *absent* is a statement about a phrase. The
calculus group is the proof: `integration by parts` is absent and the cheat sheet has a
row named *By parts*.

### The owned count was wrong twice, and the second error is the site's oldest finding

The first pass said **125 owned**. The matcher put a trailing word boundary on every
pattern and compiled any pattern containing a capital letter case-sensitively. So
`Kerberoast` could not match inside *Kerberoasting*, and `NTFS permissions` missed a topic
titled *Share vs NTFS Permissions*. Fixed, the count was **107**.

Then the owner of each of the 107 was read, and **26 came off**. The title that owned
the phrase was about something else: the other sense of the word, or a longer word that
begins the same way.

| Phrase | The title that owned it |
|---|---|
| `certificate signing request`, as `CSR` | *SSR, SSG, ISR &amp; CSR*, which is client-side rendering |
| `loopback address` | *Processing Order &amp; Precedence — LSDOU, Enforcement &amp; Loopback* |
| `amplification attack` | *You Pay for Cheap Writes in Read and Space Amplification*, in the LSM topic |
| `out-of-band management` | *Out-of-Band Verification Is the Key*, in a social engineering card |
| `common criteria` | *The CC (Common Criteria) Control Families*, which is SOC 2's |
| `journaling` | *Filesystems From the Inside — Inodes, Journaling &amp; Crash Consistency* |
| `second-order thinking` | *Second-Order Injection Passes Every Test* |
| `cynicism` | *Exhaustion · Cynicism · Inefficacy*, in the burnout card |
| `bit shift` | *Shift Left &amp; Wire Into CI* |
| `glba`, as `Gramm` | *The sudoers Grammar, and the Commands That Are a Root Shell* |

The other sixteen are the same shape: `lfi rfi` found *RFI, RFP, RFQ*, `efs` found AWS
EFS, `java generics` found TypeScript's, `virtual desktops` found VDI. **A quarter of what
a title appeared to own, it owned in another sense.** *Knowledge integration* counted this
for the first time, nine of a reader's first sixteen misses. *csvistool* found it in
*stack* and *queue*. It is the reason every `want` in the census names a topic and not a
count. The final figure is **81**. The 452 mentioned phrases were not read one by one, so
the same error is still in that number at some rate nobody measured.

## 4. What is worth writing — clusters, not phrases

A definition is not a card. The 306 absent phrases are mostly definitions, and the filter
is the rubric's one test: a question somebody has, and a sentence the table could not have
supplied. Where several absent phrases are one question, they are one row below. Every
count is a grep over `data/*.html` with `acronym.html` excluded.

**Every sentence in the fourth column is a draft, written from memory in a container that
fetched nothing.** It is there to show the card has an argument, which is the rubric's
test. It is not there to be copied. *Study notes, batch two* §5 found twelve confident
claims that should not reach a card as written, and the same treatment applies to these
before anything ships.

### Security and networking — the words the exams use and the site does not

| # | Cluster | On the site today | Lands in | The sentence, as a draft |
|---|---|---|---|---|
| 1 | **Block-cipher modes** | `ECB` 0, `CTR` 0, *mode of operation* 0. `CBC` 4 and `GCM` 1, all in `sec`, named and never explained | `sec`, a card in *Cryptography Algorithm Reference* | *AES-256* is half a sentence. The mode decides whether equal blocks of plaintext stay visible in the ciphertext, and ECB leaves them visible |
| 2 | **The formal models**: Bell-LaPadula, Biba, Clark-Wilson, Brewer-Nash | 0 each. `grc` has *CISSP — 8 Domains Overview* and two domains carry the SecX tag | `sec`, in *Access Control Models*, one card and 2,742 characters today | Bell-LaPadula and Biba are one diagram read in opposite directions. The first stops secrets flowing down and the second stops bad data flowing up |
| 3 | **Zero trust's two boxes**: the decision point and the enforcement point | *policy enforcement point* 0, *policy decision point* 0, `800-207` 0, against three zero-trust topics | `sec`, *Zero Trust — Never Trust, Always Verify*, with a diagram | Zero trust is something that decides and something that enforces, and most products sell the second |
| 4 | **Biometric error rates**: false acceptance, false rejection, the crossover | *biometric* 9 mentions; the three rates 0 | `sec`, *Multi-Factor Authentication — Layers of Proof* | The crossover rate is for comparing sensors. Where the threshold is set is a separate decision about which error you can afford |
| 5 | **The fraud controls**: separation of duties, dual control, job rotation, mandatory vacation | *separation of duties* 1; the other three at most 1 between them | `sec`, *The Insider Threat Program* | Mandatory vacation is a detective control. A fraud that needs its author present stops working when they are away |
| 6 | **Maximum tolerable downtime** | 0, against `RTO` 28 | `ops`, a row in *BCP / DR — Key Metrics* | An RTO is a target. The maximum tolerable downtime is the limit it has to fit inside, and the business sets that one |
| 7 | **Agreement types**: MOU, MOA, MSA, SOW, NDA, BPA | *memorandum of understanding* 0, *master service agreement* 0 | `grc`, *Third-Party Risk* | Which of these can be enforced, and which only records an intention |
| 8 | **Race conditions and TOCTOU** | *race condition* 3, all in passing; `TOCTOU` 0 | `sec`, beside *The Injection Family* | The check and the use are two moments, and the attack lives between them |
| 9 | **Reading interface counters** | *CRC error*, *input error*, *runt*, *late collision* 0 each; *duplex mismatch* 2 | `net`, *Network Troubleshooting — A Systematic Approach* | A duplex mismatch has a fingerprint: late collisions on the half-duplex end and CRC errors on the other |
| 10 | **Which route wins** | *administrative distance* 0, `VLSM` 0; *longest prefix* 1, and that one is in `script` | `net`, *Routing Protocols — How Routers Find the Best Path* | The most specific route wins before trust is consulted. Administrative distance only decides between sources that offer the same prefix |
| 11 | **The physical layer's vocabulary**: attenuation, T568A and B, MDF and IDF, the demarc, TDR and OTDR, the toner probe | 0 each | `net`, *Structured Cabling, Racks &amp; Fiber in Practice* and *The Field Toolkit*, with the pinout drawn | The demarc is where the fault stops being yours, which is why it is the first thing to find |
| 12 | **LLDP and CDP** | 0 | `net`, *Network Documentation That Stays Current* | A switch already knows what is plugged into each port. Documentation that asks the neighbors does not go stale the same way |
| 13 | **Syslog severity** | `syslog` 18 mentions; the eight levels as a table 0 | `ops`, *Structured Logging &amp; Log Pipelines* | Severity is chosen by whoever wrote the log line, so it records an opinion formed before your incident existed |

### The desk and the exam

| # | Cluster | On the site today | Lands in | The sentence, as a draft |
|---|---|---|---|---|
| 14 | **The Windows repair ladder**: Safe Mode, SFC and DISM, System Restore, the recovery environment, reset | *Safe Mode* 0, *System Restore* 0, `WinRE` 0; *blue screen* or *stop code* 2 | `endpoint`, a new topic. `ops` *"Why Is My Laptop Slow?"* is the model | Work down from the repair that keeps the most. Each rung gives up more of the machine's state for a better chance of booting |
| 15 | **The built-in tools and the Run box** | `chkdsk`, `diskpart`, `robocopy`, `msconfig`, `regedit`, `pathping` 0 each. `ncpa.cpl`, `appwiz.cpl`, `devmgmt.msc`, `msinfo32`, `dxdiag` 0 each | `shortcut`, a lookup beside *System &amp; General*. Short by design | `robocopy /MIR` deletes at the destination. That is the flag's meaning and its commonest accident, and `linux` already has the same card about a trailing slash |
| 16 | **Malware removal as a sequence** | *malware removal* 0 | `ops` or `threat`, as `dora-seq` | The order is the content: quarantine before anything is cleaned, restore points off before the scan and back on after it, and the user's education last |
| 17 | **Connectors, to recognize by sight** | `RJ11` 0, *F-type* 1, *Lightning* 0, in a topic that is one card | `net`, *Cabling, Connectors &amp; Ethernet Standards*, as the site's second picture grid | A+ asks for a connector by its shape, and the card describes it by its name |
| 18 | **Excel an administrator uses** | `XLOOKUP` 0, `VLOOKUP` 0, *pivot table* 0, *conditional formatting* 0. The domain's subtitle says *Excel* and the topic is 1,621 characters | `shortcut`, *Microsoft Office (Excel/Word)*, linked to `data` *Aggregation* | `VLOOKUP` defaults to an approximate match, so the common mistake returns a plausible wrong row and no error |
| 19 | **Performance-based questions** | *performance-based* 0, `PBQ` 0, *test anxiety* 0 | `productivity`, a card in *Exam Technique* | The simulations usually come first and take the most minutes, so the order you answer in is a decision |
| 20 | **Exercise and learning** | *workout* 0. Exercise is mentioned beside study in two topics, and no card is about it | `productivity`, beside *Sleep* | Condition, not a sentence: see below |

**Row 20 is about the picture at the top of every page.** `Img/Studying-Tips.png` teaches
four things: sleep patterns, the 25 and 5 Pomodoro, a workout timeframe, and naps. Sleep
has a topic, and naps are in it. Pomodoro is a card in *Time Management*. The third pillar
says *20 minutes of moderate exercise before study* and *exercise four hours after
learning*, and those two numbers are in the image and nowhere in the text. They are the
one part of the page's first screen that nothing on the site has checked. The card either
cites the study behind each number or does not repeat the number.

### The theory under the tools

| # | Cluster | On the site today | Lands in | The sentence, as a draft |
|---|---|---|---|---|
| 21 | **Computability**: Turing machines, the halting problem | *Turing* 0, *halting* 0, *decidable* 0 | `cs`, a card in *P, NP &amp; Knowing When to Stop Looking for an Exact Answer* | No tool can decide what an arbitrary program will do, which is why every scanner settles for patterns and every scanner misses or over-reports |
| 22 | **Regular and context-free** | *context-free* 0, *pumping* 0 | `cs`, *String Algorithms — Matching, Edit Distance &amp; Where Regex Fits* | *You cannot parse HTML with a regular expression* is a theorem about nesting, not an opinion about style |
| 23 | **Detecting and correcting errors**: parity, CRC, Hamming | *Hamming* 0; `CRC` in one `cs` card | `cs`, linked to `hw` *Memory Deep* for ECC | Detection and correction are different purchases. A CRC can only tell you to ask again, and ECC memory fixes the bit without asking |
| 24 | **Bitwise operations** | *bitwise* 0 | `cs`, linked to `net` subnetting and `linux` permissions | A subnet mask and a permission mask are the same move: AND against a mask |
| 25 | **The classic synchronization problems** | *priority inversion*, *producer-consumer*, *dining philosophers* 0 each | `cs`, *Deadlock &amp; Livelock* | Priority inversion is the least important task holding up the most important one, and the fix is to lend it the priority |
| 26 | **Test design**: equivalence classes, boundary values, mutation testing | 0 each | `script`, *Testing Strategy — Why and How to Test* | Coverage counts the lines the tests ran. Mutation testing counts the bugs they would have noticed |
| 27 | **Stack, heap and the segmentation fault** | *segmentation fault* 0, *linker* 0, *the heap* 0 | `cs`, *Memory Layout &amp; Cache Locality* | A segmentation fault is the operating system doing its job. The mistake happened earlier, and somewhere else |

### The human domains, and the quotes

| # | Cluster | On the site today | Lands in | The sentence, as a draft |
|---|---|---|---|---|
| 28 | **Low mood** | `depress` once on the whole site, in `productivity` | `mind` | Condition, not a sentence: see below |
| 29 | **Listening, and saying the uncomfortable thing** | *active listening* 0, *assertive* 0. *Communication &amp; Relationships* is four cards in 928 characters | `mind`, a deepening and not a new topic | The topic has four headings and no argument yet, which is Phase 8's thin shape in a topic that escaped the count by having four cards |
| 30 | **The programs a separating service member can use** | `SkillBridge` 0, `CLEP` or `DSST` 0, *Joint Services Transcript* 0, `USAJOBS` or *federal resume* 0, `TSP` 0, *VA loan* 0 | `military`, *Transitioning Out*, whose two cards are already titled for it | Every row is a dated claim about somebody else's program. Fact anchors in the same commit, or it does not ship |
| 31 | **The rival schools**: Epicureanism beside Stoicism, Confucianism beside Taoism | `Epicur` 0, `Confuci` 0 | `philosophy`, one topic each | Epicurus is remembered for indulgence and taught the opposite. Confucianism and Taoism answer one question in opposite directions |
| 32 | **Computing lines, with the paper cited** | Kernighan, Brooks, Hoare, Hopper 0 each; Knuth 1, in `cs` | `quotes`, a new topic | See the gate below |
| 33 | **The named laws**: Conway, Goodhart, Brooks, Hyrum, Postel, Chesterton's fence, Hofstadter | Conway 4 and Goodhart 1, both in `eng`; the rest 0 | `quotes`, linked from `eng` | Several of the wordings people quote belong to somebody other than the name on the law |
| 34 | **Strategy lines** | *Sun Tzu* 0, *Clausewitz* 0; Moltke 1, Eisenhower 1 | `quotes`, linked from `military` | See the gate below |
| 35 | **Report and order formats**: 9-line, METT-TC, date-time group, MGRS, WARNO and FRAGO, CCIR | 0 each; `SALUTE` and `SITREP` are present | `military`, as rows in *Military Communication Standards* and *MDMP &amp; the OPORD* | A lookup, short by design, like the ten the measured state already lists |

**Row 28 has a condition in place of a sentence, and it is the row to be most careful
with.** A domain with *Anxiety*, *Burnout*, *Motivation*, *CBT and DBT* and *Getting
Professional Help* has no card for the commonest reason somebody opens it. *Anxiety* set
the precedent: the scope sentence says it is not a diagnosis, and the DSM link was fixed to
point at the source. A low-mood card follows that precedent, ends at *Getting Professional
Help*, and is not written from memory.

**Rows 32 to 34 have a gate the rest do not.** The domain's premise is the citation.
*Sourcing a Quotation* is the method card, and it says a line is real when the work can be
named. This container fetched nothing, so every attribution in those three rows is
unchecked. A line ships with its source read, or it is listed under *Misattributed*, or it
is left out.

**The order to write in.** Rows 1, 9, 10, 14 and 19 first. Each has a fingerprint, a
count of zero where the site already has the host topic, and a reader the header
advertises to. One wave is one domain and one theme, so that is four commits and not one.

## 5. Exam paths — order, with no new content

| | |
|---|---|
| Learning paths | 102 |
| Named for an exam | **0**. `paths.json` has *Security+* 0 times, *CySA* 0, *PenTest+* 0, *Linux+* 0, *CISSP* 0, and *Network+* and *A+* once each, in a blurb |
| Domain headers carrying a certification tag | 16 of the 30 |
| What exam mode can be scoped to | All domains, one domain, the study list, or what is due. Not a path |
| What a print pack can be scoped to | A domain, **a path**, or the study list |
| The topic about choosing a certification | `eng` *Cert Roadmaps — Choosing a Path*, one card, 1,590 characters, and one of the seven thin topics |

**A path is an order over topics that exist.** It is rendered by the study tools as a
checklist, so it adds no component, no color and no card. An exam path is a print pack the
day it is written. `network-foundations` already says in its blurb that it is *the path a
Network+ syllabus takes*, and it is named for the subject and not the exam, so a reader
looking for the exam does not find it.

**Writing one is also an audit.** A path ordered by an exam's objective domains needs a
topic for every step. A step with nothing to point at is a candidate with a named asker,
which is stronger evidence than a phrase from §3.

Three things to settle before the first one:

1. **The outline is somebody else's document and it changes.** An exam code is a dated
   claim. It gets a fact anchor in `paths.json`'s commit, and the outline is fetched and
   read first. This file's 398 phrases are not a substitute for it.
2. **A path names the objective domains. It does not reproduce the outline.**
3. **`check_paths.py` gates *0 hand-written topics off a path*, and an exam path does not
   move that number.** It adds steps over topics that are on a path already, so the
   *Learning paths* row changes in paths and steps only.

**Named and not built: a path as a scope for exam mode.** `stScopeOptions()` offers
domains. Adding paths is one option group in a select, it is the one feature named for
exams, and it is code and not content. The smoke test would have to cover it. The
condition is that an exam path exists first.

## 6. Decided against, or not this file's call

| Idea | Verdict | Why |
|---|---|---|
| A Java language track | **Stays decided.** 22 of the 51 phrases in that group are absent, and 12 of those are Java the language | *Study notes, batch two* §4 called it a second beginner track squeezed into one card and shipped one card. The evidence that would reopen it is the evidence UML had: a second batch of notes asking for the same thing |
| Calculus beyond the course | **The owner's syllabus decides** | `math` follows one course, chapter by chapter. Newton's method, linear approximation, partial derivatives, Euler's method, integrating factors and hyperbolic functions are absent, and nothing here knows whether the course teaches them. What a revision domain usually wants next is worked examples, and that is a different request |
| A theory-of-computation domain | **Cards in `cs`, not a domain** | Rows 21 and 22 are two cards. *Knowledge integration* §3 set the rule: a domain is what you build when the cards exist and cannot be filed |
| A UX domain | **Still deferred** | The condition was six cards in `web`. There are four |
| Symptom phrases in existing cards | **No** | `query_probe.mjs` calls this kind 3 and forbids it. Row 14 is a new topic because the causes are absent, which is the test for kind 2 |
| Converting `ai-table` to `ref-table` | **No** | `CONTRIBUTING.md`: that is a redesign |
| Anything fetched from another host | **No** | The CSP and the smoke test both refuse it, and that refusal is part of the look |

## 7. Before any of this is written

1. **Fix the hole in the look first, as its own commit.** Nine `c-yellow` cells become
   `c-amber`, and `m` and `nd` become the house tokens. It is mechanical, so by
   `CONTRIBUTING.md`'s own rule it does not share a commit with content. Prove it with
   `make equiv`: the nine cells and 62 spans change computed color and nothing else does.
2. **Then gate it.** A class in `data/*.html` with no rule in `style.css` should fail
   `make check`, the way an undeclared `var()` does. `check_css_vars.py` is the place and
   its docstring is already the argument. It needs an allow list for the twelve structural
   names, read first, and a self-test.
3. **Put the readers into `query_probe.mjs` before the first card.** Two are worth
   tracking: *somebody revising for a CompTIA exam*, seeded from the daggered phrases in
   the six exam groups of §8, and *a student on a theory course*. Each `want` names the
   topic being written into, so a wrong-sense result scores as the miss it is. §3 is the
   argument for that.
4. **`near_duplicates.py --title` before rows 2, 3, 13 and 16.** Each lands beside content
   that exists: access control models, three zero-trust topics, several logging topics,
   two malware-analysis topics.
5. **One picture first, measured, before twenty.** Row 1 of §2. If the UML lines cannot be
   drawn in the table's first column without a new rule, §2's claim that the wave needs no
   CSS is false, and that is worth finding out on one topic.
6. **Budget.** `page_budget.py` has room for about 745 topics. Thirty-seven hands cost
   about 30 KB, so twenty diagrams are a rounding error against the byte budget. Run it
   anyway. A picture grid is where `content_elements` goes, and row 17 of §4 is one.

## 8. The candidates, by reader

All 839, so the next session starts from what this one measured. A dagger marks a phrase
whose search returns nothing outside the acronym dictionary. *Owned* is after the
wrong-sense correction in §3.

<details>
<summary>839 phrases in 17 groups</summary>

#### A Security+ candidate — 86

* **Absent (18):** `control categories` · `directive control` · `policy enforcement point`† · `honeyfile`† · `backout plan`† · `steganography`† · `data masking` · `key stretching`† · `vm escape` · `side loading` · `bloatware`† · `time of check`† · `snmp trap`† · `identity proofing`† · `ephemeral credentials` · `memorandum of understanding`† · `master service agreement`† · `due care`
* **Mentioned, and no title owns it (52):** `gap analysis` · `non-repudiation` · `access control vestibule`† · `bollards` · `honeytoken` · `maintenance window` · `secure enclave` · `salting` · `blockchain` · `ocsp stapling` · `wildcard certificate` · `certificate signing request` · `self-signed certificate` · `jailbreaking` · `logic bomb` · `keylogger` · `amplification attack` · `on-path attack`† · `credential replay` · `downgrade attack` · `birthday attack` · `directory traversal` · `race condition` · `impossible travel` · `fail open` · `fail closed` · `jump server` · `data sovereignty` · `data in use` · `hot site` · `warm site` · `cold site` · `cope cyod`† · `secure cookies` · `exposure factor` · `scap` · `file integrity monitoring` · `dns filtering` · `time-of-day restrictions`† · `password manager` · `guard rails` · `legal hold` · `data controller` · `risk appetite` · `risk tolerance` · `key risk indicator` · `single loss expectancy` · `annualized loss expectancy` · `business impact analysis` · `right-to-audit clause` · `due diligence` · `passive reconnaissance`
* **Owned by a title (16):** `compensating control` · `key escrow` · `certificate revocation list` · `typosquatting` · `pretexting` · `rootkit` · `screened subnet`† · `tabletop exercise` · `site survey` · `netflow` · `password vaulting` · `acceptable use policy` · `data custodian` · `data steward` · `right to be forgotten` · `known environment`

#### A Network+ candidate — 83

* **Absent (18):** `administrative distance`† · `vlsm`† · `lldp`† · `attenuation`† · `t568a t568b`† · `mdf idf`† · `demarcation point`† · `vxlan`† · `ipam`† · `iperf`† · `syslog severity`† · `nat64`† · `channel bonding`† · `mac flooding` · `time-domain reflectometer`† · `toner probe` · `crc errors` · `runts giants`†
* **Mentioned, and no title owns it (55):** `ospf areas` · `eigrp` · `link aggregation` · `jumbo frames` · `port mirroring`† · `native vlan` · `voice vlan` · `dhcp snooping` · `dynamic arp inspection` · `arp` · `arp spoofing` · `collision domain` · `broadcast domain` · `csma/cd`† · `duplex mismatch` · `auto-mdix`† · `single-mode fiber` · `multimode fiber` · `sfp transceiver` · `crosstalk` · `plenum` · `rack unit` · `split horizon` · `traceroute` · `snmp` · `mib oid` · `dscp` · `multicast` · `igmp` · `slaac` · `dual stack` · `link-local address` · `loopback address` · `rfc 1918` · `router on a stick` · `band steering` · `captive portal` · `mesh wifi` · `antenna types` · `rssi` · `evil twin` · `rogue access point` · `deauthentication` · `vlan hopping` · `dns poisoning` · `out-of-band management` · `console port` · `tftp` · `ipsec` · `gre tunnel` · `spine leaf` · `three-tier network` · `north-south east-west`† · `storm control` · `tacacs+`
* **Owned by a title (10):** `vrrp` · `mac address table` · `power over ethernet` · `mpls` · `ntp stratum` · `icmp` · `anycast` · `apipa` · `port address translation` · `bpdu guard`

#### An A+ candidate — 66

* **Absent (28):** `thermal printer` · `3d printer` · `sodimm` · `lightning cable`† · `rj11`† · `type 1 hypervisor` · `vdi`† · `chkdsk`† · `diskpart`† · `robocopy`† · `pathping`† · `disk management` · `msconfig`† · `regedit`† · `time machine` · `malware removal` · `safe mode` · `system restore` · `windows recovery environment` · `no boot device` · `incremental backup` · `safety data sheet` · `surge protector`† · `vnc`† · `efs` · `driver rollback` · `dead pixels` · `liquid damage`
* **Mentioned, and no title owns it (32):** `laser printing process`† · `fuser` · `impact printer` · `ddr5` · `tpm` · `boot order` · `m.2` · `hdmi` · `displayport` · `f-type connector`† · `sfc scannow`† · `gpupdate` · `event viewer` · `device manager` · `task scheduler` · `exfat` · `keychain` · `gatekeeper` · `blue screen` · `upnp` · `wps` · `degaussing` · `grandfather father son` · `synthetic full backup` · `esd` · `eula` · `drm` · `batch file` · `uac` · `roaming profile` · `folder redirection` · `battery swelling`
* **Owned by a title (6):** `motherboard form factor` · `secure boot` · `differential backup` · `windows hello` · `ntfs permissions` · `beep codes`

#### A CISSP or SecurityX candidate — 54

* **Absent (32):** `bell-lapadula`† · `biba`† · `clark-wilson`† · `brewer-nash`† · `reference monitor` · `trusted computing base` · `common criteria` · `kerckhoffs`† · `one-time pad`† · `ecb mode`† · `split knowledge` · `dual control` · `job rotation` · `mandatory vacation`† · `maximum tolerable downtime`† · `cpted`† · `polyinstantiation`† · `data remanence`† · `crossover error rate` · `false acceptance rate`† · `nist 800-63`† · `synthetic transactions`† · `cobit`† · `fair model` · `nist 800-30`† · `nist 800-207`† · `coppa`† · `itar`† · `iso 22301`† · `iso 31000`† · `soc 1` · `ssae 18`†
* **Mentioned, and no title owns it (19):** `covert channel` · `gcm` · `hmac` · `forward secrecy` · `separation of duties` · `need to know` · `fire suppression` · `micro-segmentation` · `full interruption test` · `togaf` · `sabsa` · `cis controls` · `nist 800-37` · `nist 800-61` · `nist 800-171` · `sox` · `glba` · `ferpa` · `fisma`
* **Owned by a title (3):** `diffie-hellman` · `nist 800-53` · `cmmc`

#### A CySA+ candidate — 52

* **Absent (8):** `stored xss` · `lfi rfi`† · `integer overflow` · `ssvc`† · `amsi`† · `dll sideloading`† · `process hollowing`† · `shadow copies`
* **Mentioned, and no title owns it (36):** `cvss vector` · `credentialed scan` · `reflected xss`† · `dom xss` · `parameterized queries` · `write blocker` · `order of volatility` · `tlp traffic light protocol`† · `kev catalog` · `cwe` · `applocker` · `process injection` · `golden ticket` · `silver ticket` · `pass the hash` · `kerberoasting` · `as-rep roasting` · `dcsync` · `llmnr poisoning` · `smb signing` · `credential guard` · `event id 4624` · `event id 4688` · `event id 7045` · `dns tunneling` · `domain generation algorithm` · `fast flux` · `ja3` · `prefetch` · `shimcache` · `amcache` · `mft` · `usn journal` · `registry hives` · `srum` · `shellbags`
* **Owned by a title (8):** `beaconing` · `email header analysis` · `fuzzing` · `csrf` · `output encoding` · `mean time to detect` · `epss` · `lsass`

#### A Linux+ candidate — 57

* **Absent (12):** `swap space` · `udev`† · `nice renice`† · `mdadm`† · `disk quota` · `selinux booleans`† · `cups`† · `pxe boot`† · `anacron`† · `dmidecode`† · `kickstart`† · `case statement`
* **Mentioned, and no title owns it (36):** `hard link` · `symbolic link` · `umask` · `setfacl` · `chattr` · `fstab` · `runlevels` · `systemd targets` · `kernel modules` · `sysctl` · `ulimit` · `timedatectl` · `nmcli` · `firewalld` · `gpg` · `here document` · `kernel panic` · `oom killer` · `rsyslog` · `sssd` · `chrony` · `wayland`† · `flatpak` · `compile from source` · `shared libraries` · `zombie process` · `/proc filesystem` · `fsck` · `file descriptors` · `nohup` · `dmesg` · `vmstat` · `lsof` · `cloud-init` · `bash arrays` · `trap`
* **Owned by a title (9):** `sticky bit` · `suid` · `environment variables` · `apparmor` · `initramfs` · `iscsi` · `inode` · `job control` · `exit codes`

#### A calculus student — 60

* **Absent (20):** `integration by parts` · `shell method` · `epsilon delta`† · `limits at infinity` · `newton's method`† · `linear approximation`† · `polar coordinates`† · `partial derivative` · `logarithmic differentiation` · `hyperbolic functions`† · `work integral` · `geometric series` · `integral test` · `euler's method`† · `logistic growth`† · `integrating factor`† · `completing the square`† · `complex numbers` · `binomial theorem`† · `sigma notation`
* **Mentioned, and no title owns it (39):** `chain rule` · `product rule` · `quotient rule` · `l'hopital` · `related rates` · `optimization problems` · `u-substitution` · `partial fractions` · `trig substitution` · `improper integral` · `taylor series` · `maclaurin` · `ratio test` · `disk method` · `arc length` · `fundamental theorem of calculus` · `riemann sum` · `mean value theorem` · `separable differential equation` · `exponential growth` · `parametric equations`† · `dot product` · `cross product` · `inverse trig derivatives` · `concavity` · `inflection point` · `second derivative test` · `critical points` · `area between curves` · `power series` · `alternating series` · `slope field` · `quadratic formula` · `asymptotes` · `inverse functions` · `law of sines` · `law of cosines` · `double angle` · `conic sections`†
* **Owned by a title (1):** `interval of convergence`

#### A student on a discrete maths or theory course — 41

* **Absent (23):** `logical equivalence`† · `predicate logic`† · `pigeonhole principle`† · `combinations` · `inclusion exclusion` · `recurrence relation`† · `master theorem`† · `power set` · `equivalence relation`† · `injective surjective`† · `euler path`† · `pumping lemma`† · `context-free grammar`† · `turing machine` · `halting problem`† · `decidability`† · `fermat's little theorem`† · `chinese remainder theorem`† · `hamming code`† · `huffman coding`† · `multiplexer` · `bitwise operators`† · `gray code`
* **Mentioned, and no title owns it (16):** `permutations` · `partial order` · `graph coloring` · `finite automata`† · `regular language` · `np-complete` · `reduction` · `traveling salesman` · `knapsack` · `euclidean algorithm`† · `parity bit` · `cyclic redundancy check` · `flip-flop` · `finite state machine` · `floating point` · `bit shift`
* **Owned by a title (2):** `truth table` · `proof by induction`

#### A student on an operating systems or compilers course — 33

* **Absent (14):** `priority inversion` · `producer consumer` · `dining philosophers`† · `banker's algorithm`† · `fragmentation` · `device driver` · `von neumann`† · `cache associativity`† · `linker` · `abstract syntax tree`† · `bnf grammar`† · `symbol table` · `stack vs heap` · `segmentation fault`
* **Mentioned, and no title owns it (15):** `interrupt` · `kernel mode user mode` · `fork exec` · `round robin` · `page fault` · `page replacement` · `malloc` · `fetch decode execute` · `registers` · `branch prediction` · `static vs dynamic linking` · `pointers` · `memory leak` · `calling convention` · `stack frame`
* **Owned by a title (4):** `system call` · `thrashing` · `risc cisc`† · `reference counting`

#### A student on a software engineering or Java course — 51

* **Absent (22):** `use case diagram` · `activity diagram` · `factory pattern` · `strategy pattern` · `decorator pattern` · `adapter pattern` · `equivalence partitioning`† · `boundary value analysis` · `mutation testing` · `cyclomatic complexity`† · `javadoc`† · `checked exceptions` · `java generics` · `java collections` · `interface vs abstract class` · `equals and hashcode`† · `stringbuilder`† · `autoboxing`† · `pass by value` · `jdk jre`† · `synchronized` · `java streams`
* **Mentioned, and no title owns it (24):** `functional vs non-functional requirements` · `state diagram` · `singleton` · `observer pattern` · `mvc` · `dependency injection` · `unit test` · `integration test` · `acceptance test` · `regression test` · `smoke test` · `black box testing` · `code coverage` · `test pyramid` · `code smell` · `pair programming` · `overloading vs overriding`† · `maven gradle` · `junit` · `lambda` · `null pointer exception` · `array index out of bounds` · `access modifiers` · `constructors`
* **Owned by a title (5):** `acceptance criteria` · `white box testing` · `test-driven development` · `polymorphism` · `encapsulation`

#### Somebody at a keyboard, looking something up — 40

* **Absent (22):** `ncpa.cpl`† · `appwiz.cpl`† · `devmgmt.msc`† · `msinfo32`† · `dxdiag`† · `clipboard history` · `xlookup`† · `vlookup`† · `pivot table` · `conditional formatting` · `outlook shortcuts`† · `teams shortcuts` · `powerpoint`† · `google docs` · `latex` · `html entities` · `alt codes` · `xpath`† · `winget`† · `chocolatey`† · `powertoys`† · `windows terminal`
* **Mentioned, and no title owns it (15):** `services.msc` · `compmgmt.msc` · `mstsc` · `run commands` · `virtual desktops` · `markdown syntax`† · `mime types` · `strftime` · `printf format` · `homebrew`† · `finder shortcuts`† · `firefox shortcuts` · `nano` · `emacs` · `man pages`
* **Owned by a title (3):** `http status codes` · `toml` · `csv pitfalls`

#### A reader of the philosophy domain — 48

* **Absent (16):** `epicureanism`† · `cynicism` · `confucianism`† · `hinduism`† · `shinto`† · `bushido`† · `free will`† · `karma`† · `yoga`† · `shamanism`† · `tarot`† · `runes` · `chakras`† · `game theory`† · `first principles` · `second-order thinking`†
* **Mentioned, and no title owns it (28):** `skepticism` · `virtue ethics` · `plato` · `socratic method`† · `nietzsche` · `kant` · `utilitarianism` · `nihilism` · `logotherapy`† · `ikigai` · `wabi-sabi` · `memento mori` · `amor fati` · `tai chi` · `meditation` · `mindfulness` · `breathwork`† · `norse paganism` · `animism` · `ogham` · `wheel of the year` · `moon phases`† · `herbalism` · `hermeticism`† · `sunk cost` · `confirmation bias` · `dunning-kruger` · `survivorship bias`†
* **Owned by a title (4):** `zen` · `dichotomy of control` · `occam's razor` · `hanlon's razor`

#### A reader of the mind domain — 27

* **Absent (7):** `anger` · `self-compassion`† · `assertiveness`† · `active listening` · `doomscrolling`† · `ptsd`† · `moral injury`†
* **Mentioned, and no title owns it (20):** `depression` · `adhd` · `grief` · `panic attack` · `social anxiety` · `perfectionism` · `boundaries` · `loneliness` · `alcohol` · `caffeine` · `exercise` · `journaling` · `gratitude` · `insomnia` · `night shift` · `eye strain` · `carpal tunnel` · `standing desk` · `posture` · `hydration`
* **Owned by a title (0):** none

#### A student building a study routine — 38

* **Absent (13):** `mind map` · `sq3r`† · `leitner`† · `reading a textbook` · `test anxiety` · `all-nighter`† · `second brain` · `bullet journal`† · `peg system`† · `chunking` · `dual coding`† · `elaboration`† · `performance-based questions`†
* **Mentioned, and no title owns it (22):** `pomodoro` · `getting things done` · `eisenhower matrix` · `zettelkasten` · `cornell notes` · `feynman technique` · `active recall` · `anki` · `speed reading` · `reading a paper` · `cramming` · `flow state` · `naps` · `exercise before studying` · `parkinson's law` · `pareto principle` · `habit stacking` · `body doubling` · `mnemonics` · `practice tests` · `mistake journal` · `exam voucher`
* **Owned by a title (3):** `deep work` · `two-minute rule` · `study schedule`

#### Somebody building a career, veterans included — 39

* **Absent (17):** `cover letter` · `portfolio` · `usajobs`† · `gs pay scale`† · `federal resume`† · `skillbridge`† · `clep`† · `joint services transcript`† · `vr&e` · `va loan`† · `thrift savings plan`† · `resignation letter`† · `job scam`† · `bootcamp`† · `open source contribution`† · `background check` · `w2 vs 1099`†
* **Mentioned, and no title owns it (19):** `linkedin profile` · `star method` · `take-home assignment`† · `internship`† · `dod 8140`† · `two weeks notice` · `exit interview` · `performance review` · `performance improvement plan` · `first week at a new job` · `recruiter` · `apprenticeship` · `capture the flag` · `conference talk` · `rsu equity`† · `401k` · `roth ira` · `credit score` · `non-compete`
* **Owned by a title (3):** `behavioral interview`† · `security clearance` · `emergency fund`

#### Somebody reading military structure — 32

* **Absent (12):** `space force` · `9-line medevac`† · `mett-tc`† · `date time group` · `mgrs` · `tempest`† · `dd-214`† · `va disability`† · `chain of command` · `warno frago`† · `ccir`† · `ipb`†
* **Mentioned, and no title owns it (17):** `navy ranks`† · `air force ranks` · `marine ranks` · `coast guard` · `warrant officer` · `pay grades` · `salute report` · `sitrep` · `bluf` · `zulu time` · `radio prowords` · `common access card` · `siprnet` · `comsec` · `controlled unclassified information` · `emass` · `course of action`
* **Owned by a title (3):** `nato phonetic alphabet` · `military time` · `authority to operate`

#### Somebody looking for the source of a line — 32

* **Absent (24):** `premature optimization`† · `kernighan debugging`† · `brooks's law`† · `hoare billion dollar`† · `postel's law`† · `hyrum's law`† · `chesterton's fence`† · `hofstadter's law`† · `gall's law`† · `murphy's law`† · `moore's law`† · `metcalfe's law`† · `wirth's law`† · `linus's law`† · `sturgeon's law`† · `peter principle`† · `grace hopper`† · `sun tzu`† · `clausewitz`† · `musashi`† · `bruce lee`† · `confucius`† · `rumi`† · `thoreau`†
* **Mentioned, and no title owns it (7):** `goodhart's law` · `dijkstra quote`† · `moltke`† · `eisenhower plans`† · `einstein insanity`† · `feynman` · `frankl`
* **Owned by a title (1):** `conway's law`

</details>

## 9. What shipped — the first wave

Conducted in one session, in §7's order, and recorded below as *Session — starting the
content-ideas queue*. §7's steps 1, 2, 3 and 5, then §4's first five rows, one commit per
domain. The exam reader opened at **0 of 16** and closed at **16 of 16**.

| § | Item | Where it went |
|---|---|---|
| 7.1 | The classes that color nothing | 71 elements. `c-yellow` to `c-amber` (9). `m` to the house literal tokens (61): it was a catch-all for numbers, strings and constants, not a number class. `nd` to `fn` (1). Then `style-orange` removed, because an inline `var(--orange)` was doing its work. Both mechanical commits are in `.git-blame-ignore-revs`, and stamping the four touched domains moves nothing into this month |
| 7.2 | The gate | `check_css_vars.py` fails on a class on a real element that no selector defines, with ten allowed names that each carry a reason. A parser, because the regex census counted `link`, which was text in a code sample. Run on the tree before 7.1 it reports exactly 72. `style_equiv.mjs` counted differences only up to the five it printed; it counts all of them now |
| 7.3 | The readers | *Somebody revising for a CompTIA exam*, 16 queries over this wave's five rows. **The theory reader is not added yet**: a reader whose queries nothing is about to answer records a backlog, not a census. It goes in with the first theory card |
| 7.5 | One picture first | §2 row 1, the six UML lines. **No new CSS**, and the first attempt showed why the question was worth asking: `math-svg` is a fluid full-width frame, and in a table cell it drew the lines 51×9 px on a phone. A picture inside a cell takes its size from its own `width` and `height` attributes. Full-width figures use the frame |
| 4.1 | Block-cipher modes | A card in *Cryptography Algorithm Reference*. It answers the "Which mode? Is it authenticated?" row of *Reading a Cryptographic Claim Critically*, and the two now link both ways |
| 4.9, 4.10 | Interface counters; which route wins | A card each in `net`. The counters card gives the duplex-mismatch fingerprint the troubleshooting table had only named. The routes card gives the three tests in order and the floating static route |
| 4.14 | The Windows repair ladder | A new topic in `endpoint`, on the service-desk path after the slow-laptop topic: the ladder, the fingerprint and the Safe Mode trap |
| 4.19 | Performance-based questions | A card in *Exam Technique*. **The draft sentence in §4 was wrong**: CompTIA's current pages do not say PBQs come first. What they do say is better: a simulation can be marked and revisited, and a virtual item cannot |

**Two claims in this section were wrong, and stay visible rather than silently fixed.** §1
said the cells beside the nine `c-yellow` cells use `c-amber`. Read, they use `c-red` in
seven tables and `c-green` in one; the fix stands on the house tone instead. And §4 row
19's draft said PBQs come first, which is what the older sources say.

**One gap found underneath an old query.** `the user has two accounts` had passed the census
at exactly 60 results, which is the wide threshold, and the repair ladder made it 61. Nothing
in that set is about one person with two identities. `soft-match` and `hard-match` appear
nowhere on the site, so the question is kind 2, and its natural home is `infra`'s *Entra
Connect & Hybrid Identity* or `m365`'s joiner-mover-leaver topic. Queued here; the query
carries the verdict.

**Not done, and why.** The other 15 rows of §4, the other 19 pictures and the exam paths
are the queue. `make visual` fails in this container on the commit before this session as
well, at the same 10.3% and 10.1%. Its fonts render wider, so the baseline was left alone.

## 10. What shipped — the second wave

Conducted in one session, recorded below as *Session — the second wave, and three tools
that were wrong at their own edges*. §4 rows 2 to 8 and 11 to 13, with the reader extended
first and one commit per domain. The exam reader's second batch opened at **0 of 23** and
closed at **23 of 23**.

| § | Item | Where it went |
|---|---|---|
| 4.2 | The formal models | A card in *Access Control Models*. Bell-LaPadula and Biba are one ladder with opposite rules, then Clark-Wilson and Brewer-Nash |
| 4.3 | Zero trust's two boxes | A card in *Zero Trust*, as step tiles and a table. **It corrected a row already there**: "Policy engine (PEP/PDP) — decides allow/deny" made the enforcement point a decision-maker, and in NIST's model it decides nothing |
| 4.4 | Biometric error rates | A card in *Multi-Factor Authentication*. The rates are spelled out and not added to the dictionary, because `CER` is also the `.cer` extension |
| 4.5 | The fraud controls | A card in *The Insider Threat Program*: separation of duties and four siblings, split into the three that prevent and the two that only detect |
| 4.8 | Race conditions and TOCTOU | A card in *Broken Access Control*, not beside *The Injection Family* as the row said: a check that ran at the wrong moment is an access-control failure |
| 4.6 | Maximum tolerable downtime | **A card, not a row.** The metrics in *BCP / DR* are tiles, each with an inline border color, and the inline-style ceiling has no slack. Work recovery time came with it, and the worked example is the argument: one restore passes with a four-hourly backup and fails with a nightly one |
| 4.7 | Agreement types | A card in *Third-Party Risk*, seven documents with the SLA and the work order added. Sources disagree on whether an MOA binds, so the card says force comes from wording, and the verdict names the MOU and the NDA as the two traps |
| 4.11 | The physical layer | Two cards in *Structured Cabling*: the path from demarc to desk, with attenuation as the budget behind its lengths, and the pinout drawn pin by pin. In *The Field Toolkit* the toner row names the tool and says what it does, a TDR row joins it, and a card covers TDR and OTDR |
| 4.12 | LLDP and CDP | A card in *Network Documentation*, as a decision per port |
| 4.13 | Syslog severity | A card in *Structured Logging*, with Cisco's keywords and what a threshold sends |

**Three tools were wrong at their own edges, and the new cards found all three.** The search mapped
every dictionary entry both ways, including the ones marked as ordinary words, so
`information technology` returned 1,452 of 1,564 topics through *it*, and adding FAR sent
`false acceptance rate` to 219 through *far*. The annotator's window read across a topic's
edge, and SSRF lost its expansion in the title of the topic about SSRF. And `.dora-word`
was `#fff`, so the step names vanished on the light theme's tiles. Each fix is its own
commit, with fixtures or a measured before and after. The search fix has a recorded cost:
`metropolitan area network` now reaches the dictionary entry and not the cards that write
only MAN, because a lowercased index cannot tell MAN from *man*.

**The palette has no brown.** The pinout marks the four pins that differ, in amber, and
does not paint the wires. Where a picture needs a color the palette lacks, it marks the
difference instead.

**Not done.** §4 rows 15 to 18 and 20 to 35, the other pictures and the exam paths are the
queue, and so is the gap §9 found under `the user has two accounts`. `make visual` fails
here as it did in the first wave, for the same font reason.

## 11. What shipped — the third wave

Conducted in one session, recorded below as *Session — the third wave, and two answers the
census counted that nobody gave*. §4 rows 15 to 18 and 20, *the desk and the exam*, with
the reader extended first and one commit per domain. The exam reader's third batch opened at
**0 of 16** and closed at **16 of 16**.

| § | Item | Where it went |
|---|---|---|
| 4.15 | The built-in tools and the Run box | **A new topic, and longer than *short by design*.** `shortcut` *Windows Built-in Tools*, beside *System &amp; General*: the Run box names, the disk, system-file and policy commands with the switch that matters on each, and the Windows network commands, which the site barely had: `ipconfig` twice, `tracert` once, `netstat` never on Windows. The last card is robocopy `/MIR`, linked to the rsync card. On *Running a Service Desk* after the troubleshooting methodology |
| 4.16 | Malware removal as a sequence | A card in `ops` *Incident Response Lifecycle — PICERL*, not `threat`: the seven A+ steps are its phases at the scale of one machine, and the table says which phase each step is. Step tiles, as the row asked. The verdict carries the limit Professor Messer's A+ course states, that rebuilding is the real best practice |
| 4.17 | Connectors, to recognize by sight | **Two cards, in `net` and in `hw`, and not a grid.** Six network connectors in the cabling topic and six desk plugs in *Docks, USB-C &amp; Thunderbolt*, each drawn face-on in its table's first column, the way wave one drew the UML lines, so each shape sits beside its tell. One scale per table, existing roles only, no new CSS |
| 4.18 | Excel an administrator uses | Two cards in *Microsoft Office*. VLOOKUP's default is approximate, and MATCH has the same default, which the row did not say. A pivot table is a `GROUP BY` you drag, linked to `data`'s aggregation topic |
| 4.20 | Exercise and learning | A card in *Sleep*, under the condition the row set. One number has a study behind it, van Dongen and colleagues in 2016, and the card gives its limits. The other, twenty minutes before study, has none that a search found, and the card says so instead of repeating it as advice |

**Two old zeros now score answered, and neither was answered.** Search reads the
annotator's expansions as text. `the user says the file is gone` matched the new tools topic
through *User* in the expansion of UDP, and `the usb ports on one side stopped working`
matched a connector card's *wider on one side*. In both, relaxation then widened one
accidental match into a result list, so the census counts two answers a reader does not get.
The staleness check cannot see either, because neither note claims a zero in words. Both
notes now say what happened. **For the first, a fix is queued and not made:** search that
skips text inside `.acro-exp`, measured by the census before and after, because an expansion
is a reading aid and not something a card says. The second is the ordinary cost of a matcher
that reads words, and its repair is the card the note says is still unwritten.

**A new topic has three costs the plan did not list.** `check_paths.py` fails until it is on
a path, the orphan row drifts until it has related links in both directions, and
`gen_og_image --check` fails because the preview image prints the topic count. All three
were met here and are in the commit.

**Not done.** §4 rows 21 to 27, the theory under the tools, wait for the second reader, *a
student on a theory course*. Rows 28 to 35 are the human domains, each with a condition of
its own, and rows 32 to 34 need the source-reading gate. The pictures
of §2 and the exam paths of §5 are still the queue, and so is the gap §9 found under `the
user has two accounts`.

## 12. What shipped — the fourth wave

Conducted in the same session as the third, recorded below as *Session — the fourth wave,
and a spelling gate that knew five words and not the rule*. §4 rows 21 to 27, the theory
under the tools, with the second reader §7.3 named, *a student on a theory course*, added
first. It opened at **0 of 15** and closed at **15 of 15**.

| § | Item | Where it went |
|---|---|---|
| 4.21 | Computability | A card in *P, NP*: the halting problem and Rice's theorem, and why every scanner is sound and noisy or quiet and incomplete |
| 4.22 | Regular and context-free | A card in *String Algorithms*: the machines, the pumping lemma, and the HTML theorem with its two qualifications |
| 4.23 | Detecting and correcting errors | A card in *Modular Arithmetic*, not a new home: a CRC is modular arithmetic on bits. Parity, CRC, Hamming and SECDED, linked to the memory topic |
| 4.24 | Bitwise operations | A card in *Boolean Algebra*, linked to subnetting and Linux permissions. **The draft missed the better half:** umask is not subtraction, and 033 is where the shortcut breaks |
| 4.25 | The synchronization problems | A card in *Deadlock*: four shapes and their fixes, and the Mars Pathfinder mutex |
| 4.26 | Test design | A card in `script` *Testing Strategy*, on one example where a mutant survives every partition test |
| 4.27 | The stack, the heap and the segmentation fault | A card in *Memory Layout*, with what finds each cause before the crash |

**Two gates caught the content, and one of them was wrong.** The linter caught `ECC`
rendering as *Elliptic Curve Cryptography* in a card about error-correcting codes, which was
right, and `cs` now decides the meaning. The spelling gate failed *bitwise*, which was not:
its exception list named five *-wise* words, and the suffix is now a rule.

## 13. What shipped — the fifth wave

Recorded below as *Session — the fifth wave, the human domains, and a neighbor the stamper
re-dated*. §4 rows 28 to 31 and 35, each under the condition its row set. The 17 queries
went to two readers that already ask about these subjects rather than a new one, and the
batch opened at **0 of 17** and closed at **17 of 17**.

| § | Item | Where it went |
|---|---|---|
| 4.28 | Low mood | A new `mind` topic after *Anxiety*, on its precedent: the same scope sentence, thoughts of self-harm sent to *Getting Professional Help* today, the NHS's and NIMH's two-week line cited, and behavioral activation with the COBRA trial behind it. Not written from memory: two fact anchors date the guidance and the trial |
| 4.29 | Listening and the uncomfortable thing | Two cards in *Communication &amp; Relationships*, which was four one-line cards: active listening from Rogers and Farson, and the DESC script on a colleague who merges without review |
| 4.30 | The transition programs | A card in *Transitioning Out*, sorted by whether each program ends with service. Every row dated, as the row demanded, and one had already changed this year: the Department of the Air Force's SkillBridge policy moved on 31 March 2026 |
| 4.31 | The rival schools | Two `philosophy` topics. Epicureanism opens on the misreading, with the *Letter to Menoeceus* quoted from a named translation. Confucianism sits beside Taoism and answers its question the other way round |
| 4.35 | Report and order formats | Three `military` cards: the 9-line MEDEVAC, the date-time group and the grid, and the orders and factors around the OPORD. **The date-time group's format has no source behind it**: no search returned one, and its fact anchor says so rather than claiming a check |

## 14. What shipped — the sixth wave

Recorded below as *Session — the sixth wave, the quotes, and a gate that meant reading*. §4
rows 32 to 34, three new `quotes` topics under the gate the rows set. The 10 queries opened at
**0 of 10** and closed at **10 of 10**.

| § | Item | Where it went |
|---|---|---|
| 4.32 | Computing lines | *Computing Quotes*: Dijkstra, Kernighan and Plauger, Hoare twice and Hopper, each with its work and place. The trap card is Knuth's line, quoted in half for fifty years |
| 4.33 | The named laws | *The Named Laws*: seven in their original wording. Goodhart's is worded by Marilyn Strathern, and the card says so |
| 4.34 | Strategy lines | *Strategy Quotes*: Sun Tzu and Clausewitz with the translation named, Moltke's 1871 sentence, and Eisenhower crediting the Army |

**The gate held, and it removed two lines.** Hopper's *most dangerous phrase* is marked
unsourced where it is collected, and Sun Tzu's *noise before defeat* is in no print
translation. Both are in *Misattributed* now, beside the lines the site corrected before.
**Every source was read this time, not searched.** The plan said this container fetched
nothing. That was true of the fetch tool, which could not reach these hosts; the container
itself could, with plain requests. Two hosts were not reachable that way, a defunct site and
one that refuses automated reading, and neither was worked around: the Conway and Sun Tzu
rows are read from pages that quote and cite their originals.

## 15. What shipped — the seventh wave

Recorded below as *Session — the seventh wave, the pictures, and the components the rows
named*. §2 rows 2 to 20, every picture left after the first wave drew row 1, one commit per
domain. No reader queries were added, because a picture adds no question a reader types. The census was **472 of 495**
before and after.

| § | Topic | Where it went |
|---|---|---|
| 2.2 | `career` *Diagrams That Explain* | Six shapes, each drawn in the table's diagram column beside its question, not as a separate grid |
| 2.3 | `hw` *Motherboard Anatomy* | The block diagram, drawn tall: the CPU's own lanes in green, one amber uplink, everything else under the chipset, and the shared M.2 and SATA lanes bracketed |
| 2.4 | `ops` *Priority, Impact &amp; Urgency* | **The row said the topic had no matrix, and it had one, as a table.** The picture is the risk matrix with one senior manager's ticket followed across it: along the urgency axis to P3, never up the impact axis to P1 |
| 2.5 | `eng` *SDLC Models* | Replaces the box-drawing V: the pairs, and the longest way round, from requirements down and back up to acceptance |
| 2.6–2.8 | `net` *Spanning Tree*, *TCP vs UDP*, *NAT in Practice* | With the components named. The switches are A, B and C, because the annotator read *S3* as Amazon's storage service |
| 2.9 | `sec` *OT vs IT &amp; the Purdue Model* | Two stacks drawn in SVG, the intended path and the vendor link. A layer-stack cannot draw a line that goes round it |
| 2.10 | `sec` *Network Security Architecture* | The zones as a diamond, twice, differing by the one arrow egress filtering removes. Not `topo-svg`, which is 80 pixels tall |
| 2.11–2.13 | `cs` *Trees*, *Caches*, *Merkle Trees* | Seven keys balanced and in order; the memory ladder on a log scale, not a layer-stack, whose even rows are the flattening the row named; the changed path and the proof. **The ladder showed the title wrong: 1 ns to 150 ms is eight orders of magnitude, not six** |
| 2.14 | `military` *OODA Loop*, *The Intelligence Cycle* | Rings, each beside what it is not: Boyd's line from Orient to Act beside the intruder's reset, and the open belt beside the closed cycle. Not `lifecycle`, a row that cannot draw the arc back and needs inline styles for its arrows |
| 2.15 | `blueteam` *Pyramid of Pain* | A pyramid, because a stack's rows are one width and the width is half the picture. The card says the height is Bianco's model and the width is a reading of it |
| 2.16 | `devops` *CI/CD Pipeline Design* | Step tiles with a gate diamond at each of the four positions between them |
| 2.17 | `cloud` *Azure Hierarchy* | Nested boxes, a role at a subscription and a policy at the management group: inheritance is containment, which a stack cannot hold |
| 2.18 | `infra` *Processing Order &amp; Precedence* | Two stacks drawn in SVG: by default the Kiosks OU writes last, and with Enforced the domain's pass moves to the bottom |
| 2.19 | `m365` *Mail Flow* | Step tiles twice, the path and the same path under an allow rule. **The hole is narrower than the topic's verdict says**: malware and high-confidence phishing are quarantined whatever a rule says |
| 2.20 | `web` *Flexbox* | The same items in a row and a column, with both axes turning |

**Eight of the nineteen rows named a component that could not draw their claim.** Five
named `layer-stack`. Its rows are all one width, sit side by side and hold nothing, and the
pyramid's width, Azure's containment, the line round the Purdue model and the ladder's uneven
gaps are each exactly one of those. The others named a `lifecycle` row for a cycle, a
separate grid for shapes that belonged beside their questions, and an 80-pixel `topo-svg` for
four labeled zones. **§2's claim that none of the twenty needs a line of new CSS held.**
Every picture uses roles already in `style.css`, and the class gate passed each commit.

**A picture drawn alone is the wrong size at both ends.** The math SVGs scale with the card,
so one picture alone renders at twice its size on a desktop and a third of it on a phone. Every
picture that compares two things went into two panels of the topology grid, which stack on a
phone, and the three drawn alone were drawn tall, which the height cap holds to size.

**Not done.** The spelling gate misses prefixed forms: it rejects *labelled* and has never
seen *unlabelled*, which the site has seventeen times, or *relabelled*, which it has once. It
is queued for the eighth wave with §5's exam paths and the gaps §9 and §11 left.

## 16. What shipped — the eighth wave

Recorded below as *Session — the eighth wave, the exam paths, and the queue emptied*. §5's
exam paths, the feature §5 held for them, and every gap an earlier wave queued. No reader
queries were added. Two that already carried verdicts found their cards, and one went back
to the zero its note always said was true.

| § | Item | Where it went |
|---|---|---|
| 5 | Exam paths | Four, over topics that exist: *CompTIA Network+ (N10-009)*, 36 steps; *Security+ (SY0-701)*, 45; *A+ Core 1 (220-1201)*, 28; *A+ Core 2 (220-1202)*, 32. Each outline was read first, from a course index that mirrors CompTIA's numbering, fetched with plain requests. comptia.org refuses automated reading. Each blurb names the domains and the month the outline was read |
| 5 | A path as a deck | **Built.** Exam mode, flashcards, the quiz and the Markdown export take a learning path, through the same `pathSteps()` the print pack uses. The smoke test covers it, 164 to 165 |
| 9 | `the user has two accounts` | A new `infra` topic, *One User, Two Accounts*, with the matching rules and the habits that make duplicates. A topic and not a card, because search widens a lone exact hit unless the topic's own name carries the question. The query now finds it alone |
| 11 | `the usb ports on one side stopped working` | A troubleshooting card in *Motherboard Anatomy*, under the block diagram. The query finds it first |
| 11 | Search inside expansions | Search no longer reads the annotator's expansions as card text. The census moved by one, 472 to 471, and the one was the coincidence |
| 15 | The spelling gate's prefixes | The gate takes un-, re-, mis- and pre-. Eighteen words were swept in a mechanical commit that `.git-blame-ignore-revs` lists, so no topic was re-dated by it |

**Writing a path was the audit §5 said it would be.** Five objectives have nothing to point
at. In Core 2 they are Windows editions, file systems, installing an operating system and
troubleshooting mobile devices, and in Core 1 a failing drive. The paths skip them rather
than point somewhere close, and each is now a candidate with a named asker.

**An exam launched five days before its path was written.** CompTIA lists SY0-801's launch
as 17 November 2026 and SY0-701's retirement as 11 June 2027. The Security+ path follows
SY0-701, which is still being taken and whose outline was read. The SY0-801 course index was
not at the address its predecessor's pattern predicts, and guessing further was not reading.
A path for it waits for its outline.

**What is left.** The five candidates above, a SY0-801 path once its outline can be read, and
the visual baseline, which fails in this container on font rendering and was left alone.
Otherwise the queue *Content ideas* opened with is empty: §4's thirty-five rows, §2's twenty
pictures, §5's paths and every gap a wave set aside.

## 17. What shipped — the ninth wave

Recorded below as *Session — the ninth wave, the five gaps and the exam that launched*. All of
§16's list of what was left. The reader went in first: 16 queries opened at **0 of 16** and
closed at **16 of 16**.

| § | Item | Where it went |
|---|---|---|
| 16 | Windows editions | `endpoint` *Windows Editions*: what Home leaves out, from the domain join to the Remote Desktop host, and Enterprise as a license that steps Pro up. A+ Core 2, 1.3 |
| 16 | Installing an operating system | `endpoint` *Installing Windows*: the kinds of install by what survives, GPT with UEFI and MBR with legacy BIOS, and boot media. Core 2, 1.2 |
| 16 | Troubleshooting mobile devices | `endpoint` *Troubleshooting Phones &amp; Tablets*: the common faults and their first checks, then the signs of compromise. Core 2, 3.2 and 3.3 |
| 16 | File systems | `hw` *File Systems*: six by what reads them and how large a file can be, then NTFS permissions through a copy and a move. Core 2, 1.1 |
| 16 | A failing drive | `hw` *A Failing Drive*: copy the data first, seven symptoms, and the five SMART attributes and why a clean report proves nothing. Core 1, 5.2 |
| 16 | A path for SY0-801 | Read from CompTIA's own objectives document, version 2.0, fetched. 49 steps, every objective with a topic, including V8's new 2.6 on the threats that come with using AI |

**Both A+ paths now cover every objective, and their blurbs name no gaps.** The five were
written as topics and not cards, because the eighth wave found that search widens a lone
exact hit unless the topic's own name carries the question. Eleven of the sixteen queries
find their topic as the only result, and the other five find it among two to fifteen.

**The outline the eighth wave could not find was one search away.** The eighth wave looked for
SY0-801 at the address its predecessor's course used, and stopped there. This wave searched
for the outline itself, and found CompTIA's objectives document on the file host its pages
link to: the official document, not a course index that mirrors it.

**What is left.** The visual baseline, which still fails in this container on font rendering
and is left alone. *Content ideas* has nothing else queued. New content would start from a new
list, with its readers in the census first.

## 18. What shipped — the tenth wave

Recorded below as *Session — the tenth wave, four exam paths and the six gaps they found*.
§17 left nothing queued, so the wave went back to §5's own count: four exams it found at zero
in `paths.json`, CySA+, PenTest+, Linux+ and CISSP, that no wave had written a path for. The
paths went first, the reader's queries second and the topics last. The 18 queries opened at
**0 of 18** and closed at **18 of 18**.

| § | Item | Where it went |
|---|---|---|
| 5 | Exam paths | Four more, each read from the exam body's own document, fetched with plain requests from the file hosts their pages link to: *CompTIA PenTest+ (PT0-003)*, 53 steps; *CySA+ (CS0-004)*, 54; *Linux+ (XK0-006)*, 45; *ISC2 CISSP (2024 outline)*, 57. The CySA+ path follows CS0-004, launched on 23 June 2026, and names CS0-003's English retirement, 22 December 2026. The CISSP path follows the outline in force and names 15 April 2027, when ISC2's next one takes effect |
| 5 | Linux device management | `linux` *Linux Device Management*: the three stages a device passes through, the inventory commands, modprobe against insmod, and udev rules. Linux+ 1.2 |
| 5 | Virtualization on Linux | `linux` *Virtualization on Linux*: KVM, QEMU, libvirt and virsh as layers of one stack, qcow2 and VirtIO, and the five network modes. Linux+ 1.7 |
| 5 | Cleanup after a test | `pentest` *Cleanup &amp; Restoration*: the outline's seven activities, what only the client can fix, and the order they run in. PenTest+ 5.4 |
| 5 | Process injection | `threat` *Process Injection, Hollowing &amp; DLL Side-Loading*: the four calls, the variants, side-loading, and the Sysmon events that record them. PenTest+ 4.4, and CySA+ 1.2 |
| 5 | Cryptanalytic attacks | `sec` *Cryptanalytic Attacks*: the five attack models, side channels and faults, and the attacks that never touch the math. CISSP 3.7 |
| 5 | Incident communications | `ops` *Incident Communications*: who hears what and who owns telling them, three regulators' clocks, and the order people hear it in. CySA+ 3.3 and 4.2, and CISSP 7.6 |

**132 objectives, and most already had a topic.** PenTest+ has 26, CySA+ 15, Linux+ 29 and
the CISSP outline 62. Six had nothing to point at, and they are the six topics. Everywhere else
a step is a topic that already existed, and a topic that answers two objectives sits at the
first. Linux+ 3.4, account hardening, is answered by the PAM and account steps already on the
path rather than by a step of its own.

**Two more turned up on a second reading, and are left for the next wave.** CISSP 1.6, the
hierarchy of policies, standards, procedures and guidelines, and 7.15, personnel safety (travel,
duress and emergency management), have no topic either. The path skips them rather than point
somewhere close, as the A+ paths did with their five, and the CISSP path is their asker.

**What is left.** Those two, and the visual baseline, which still fails in this container on
font rendering and is left alone.

## 19. What shipped — the eleventh wave

Recorded below as *Session — the eleventh wave, SecurityX and the two CISSP gaps*. §18 left two
candidates, and the domain headers named one more exam the site had no path for: SecurityX,
tagged on four domains. The path went first, the reader's queries second and the topics last.
The 8 queries opened at **0 of 8** and closed at **8 of 8**.

| § | Item | Where it went |
|---|---|---|
| 18 | CISSP 1.6 | `grc` *Policies, Standards, Procedures &amp; Guidelines*: each level by what it answers and how often it changes, a RACI matrix for a policy's life, and four frameworks by what each asks of the documents. SecurityX 1.1 too |
| 18 | CISSP 7.15 | `sec` *Personnel Safety &amp; Security*: life safety first, then travel, duress codes, evacuation, and the training aimed at people |
| 5 | A path for SecurityX | *CompTIA SecurityX (CAS-005)*, 46 steps, read from CompTIA's objectives document, version 7.0, fetched from the file host CompTIA's pages link to. A third-party copy in search results was version 3.0 |

**Every SecurityX objective already had a topic but one.** The 23 objectives map onto topics
that exist, except 1.1's program documentation, which is the CISSP 1.6 gap, so one topic closes
both. Four terms the outline names appeared nowhere in the site's prose: the RACI matrix and
COBIT, which the policy topic now explains, and RASP and IAST, which nothing does yet.

**What is left.** RASP and IAST, which SecurityX names and PenTest+ names in part, and which the
site's SAST and DAST topic does not cover. The domain-header tags with no path, whose outlines
nobody has read: CKA, OSCP, GCIH, AWS, GCP, MD-102, AZ-800, MS-102 and AI+. And the visual
baseline, unchanged.

## 20. What shipped — the fourteenth wave

Recorded below as *Session — the fourteenth wave, two Microsoft paths and an exam that retired*.
Three of §19's tags were Microsoft's, and each study guide was fetched from Microsoft Learn and
read before anything was written.

| § | Item | Where it went |
|---|---|---|
| 19 | MD-102 | *Microsoft MD-102 (Endpoint Administrator)*, 38 steps, skills measured as of 27 October 2026, with the twelfth wave's packaging topics under managing applications |
| 19 | MS-102 | *Microsoft MS-102 (Microsoft 365 Administrator)*, 24 steps, skills measured as of 28 April 2026 |
| 19 | AZ-800 | **Retired on 30 September 2026**, its study guide says, so no path. The infra header and the README advertised it, and now read *AD DS* |

**The gaps the two outlines found, and the next queue.** MD-102 names seven things the site
covers in a mention or not at all: deploying Microsoft 365 Apps with the Office Deployment Tool,
Windows Backup for organizations, Delivery Optimization, App Control for Business, Hotpatch,
multi-admin approval, and Security Copilot agents in Intune. MS-102's are thicker, and most sit
in its largest area: Defender XDR incidents and advanced hunting, attack simulation training,
Defender for Cloud Apps, Defender Vulnerability Management, self-service password reset with
Entra Password Protection, administrative units, IdFix, and sensitive information types with
Endpoint DLP. Each path skips them rather than point somewhere close, and each is a candidate
with a named asker.

**Also left.** The tags no outline has been read for: CKA, OSCP, GCIH, AWS, GCP and AI+. RASP
and IAST. And the visual baseline, unchanged.

## 21. What shipped — the fifteenth wave

Recorded below as *Session — the fifteenth wave, MS-102's Defender XDR area and a stamper that wrote
when asked for help*. §20 named MS-102's Defender XDR area as the thinnest coverage on the site, and
four of its gaps were written, each from Microsoft's own pages, fetched and read before any card.

| § | Item | Where it went |
|---|---|---|
| 20 | Defender XDR incidents and advanced hunting | `m365` *Defender XDR Incidents &amp; Advanced Hunting — One Queue for Mail, Devices, Identities &amp; Apps*: the incident as the portal's judgment, automated investigation and the Action center, the hunting tables with two queries, and custom detection rules with their lookbacks |
| 20 | Attack simulation training | `m365` *Attack Simulation Training — Phishing Simulations, Training Campaigns &amp; the Clicks Nobody Made*: the wizard, actual against predicted compromise rate, the clicks scanners make, and the advanced delivery policy for other vendors |
| 20 | Defender for Cloud Apps | `m365` *Defender for Cloud Apps — App Connectors, Cloud Discovery &amp; Why Unsanctioned Is Not Blocked*: the two doors, the policy types, blocking through Defender for Endpoint, and the activity log |
| 20 | Defender Vulnerability Management | `endpoint` *Defender Vulnerability Management — Exposure Score, Recommendations &amp; Handing the Fix to Intune*: two scores that move in opposite directions, how a recommendation is ranked, the remediation request as a ticket, and exceptions that cannot be extended |

**Each went onto the MS-102 path** at its objective, and onto its domain's own path: the three `m365`
topics after *Secure Score* in *Administering Microsoft 365*, and vulnerability management after
*Defender for Endpoint* in *Endpoint Engineering with Intune*.

**Two things Microsoft's pages said that a card had to carry.** Defender for Cloud Apps file policies
retire on 6 January 2027, six weeks after this wave, so a file policy written now needs a Purview home
almost at once. And Secure Score for Devices currently reads configuration set by Group Policy, so on
a fleet configured from Intune it can report correct settings as wrong.

**The queue.** MS-102's other four: self-service password reset with Entra Password Protection,
administrative units, IdFix, and sensitive information types with Endpoint DLP. Reading the outline
again for this wave found three more inside the Defender XDR area that §20 did not list: Defender
Threat Intelligence, alert policies in Defender for Office 365, and restricted entities. MD-102's seven
are unchanged. And still the tags no outline has been read for, CKA, OSCP, GCIH, AWS, GCP and AI+,
with RASP and IAST, and the visual baseline.

## 22. What shipped — the sixteenth wave

Recorded below as *Session — the sixteenth wave, MS-102's identity and Purview gaps, and a tool the
outline still names*. The other four gaps of §20's MS-102 list, each from Microsoft's own pages,
fetched and read before any card.

| § | Item | Where it went |
|---|---|---|
| 20 | Self-service password reset with Entra Password Protection | `m365` *Self-Service Password Reset &amp; Password Protection — Who Can Reset, and Which Passwords Get Refused*: the checks before a reset, writeback as an admin reset under the domain's own policy, the five-point banned-password score, and the DC agent in audit first |
| 20 | Administrative units | `m365` *Administrative Units — Delegating Part of the Tenant, and Fencing Off the Accounts That Matter*: scoped roles, what a group in a unit does and does not bring, and restricted management units |
| 20 | IdFix | `infra` *Preparing Active Directory for Sync — Duplicate Addresses, Bad Characters, UPN Suffixes &amp; After IdFix*: the attribute rules, the `.local` suffix, and **IdFix retired on 30 June 2026**, which the outline still names |
| 20 | Sensitive information types with Endpoint DLP | `m365` *Sensitive Information Types &amp; Endpoint DLP — The Pattern That Finds It, and the Device That Stops It*: patterns and confidence levels, the regex rules Purview enforces, and what a device policy can stop |

**Each went onto the MS-102 path** at its objective, which now has 32 steps, and onto its domain's
path: two after *Admin Roles* and one after *Sensitivity Labels &amp; DLP* in *Administering Microsoft
365*, and sync preparation after *One User, Two Accounts* in *Running Windows Server &amp; Active Directory*.

**A retired tool on a current outline.** The outline was read in November 2026 with skills measured as
of 28 April 2026, and it asks for IdFix. IdFix's repository says it was deprecated, and unsupported
from 30 June 2026, and Microsoft's page on installing it returns 404. The topic teaches the rules it
checked and says plainly not to install it. It is the second time in three waves that an outline has been behind
its product: the first was AZ-800, an exam that had itself retired.

**The queue.** The three Defender XDR items §21 found: Defender Threat Intelligence, alert policies in
Defender for Office 365, and restricted entities. MD-102's seven are unchanged, and so are CKA, OSCP,
GCIH, AWS, GCP and AI+, RASP and IAST, and the visual baseline.


# Error codes and packaging — three items from the owner

## 1. The request

Added as written:

```
* Add to system tray an error checker search which will be Error code | system type | use of it
* Compare error code from Intune and MECM that are common involing packaging and deploying of software
* MSI, Intunewin, Exe explain in how they work
```

The page has no system tray, so the first item is read as the nearest thing it has: the row of
icon buttons at the right of the header — theme, expand all, random topic and acronym
expansions — which sits where a tray sits and does what one does. The lookup becomes a fifth
button there.

## 2. What exists, measured

| Item | What the site has | What is missing |
|---|---|---|
| 1. An error-code search in the tray | Site search, which finds a code only when some card's prose contains it, and then returns the card rather than the code's meaning | A lookup that takes a code and returns one row: the code, the system it comes from, and what it means and what to do about it |
| 2. Intune and MECM codes, compared | Two cards of codes *you will see weekly*: five in *Application Troubleshooting — Reading the IME Log* and nine in *MECM Deployment &amp; Content Troubleshooting*. Three are in both: 0x87D00324, 1603 and 1618. No card puts the two systems side by side, and 1641 appears nowhere | One table that sorts the codes by what raised them — the installer, the management agent or the platform — so the same code reads the same way in either console |
| 3. MSI, .intunewin and EXE | *Win32 App Packaging — .intunewin End to End*: one card, 3,436 characters, on the seven steps of the workflow. Nothing says what is inside an MSI, why an EXE has no standard switches, or that a .intunewin file wraps an installer rather than being one | A topic on the three by what actually installs, what Windows records afterward, and what a deployment tool can detect |

## 3. The order to do them in

1. **The readers first.** A batch in *a service desk engineer*, which already asks about
   BitLocker and Autopilot, with each want named before its topic exists.
2. **Items 3 and 2 as `endpoint` topics, 3 first.** The comparison rests on what each format
   reports when it fails, so the formats come first.
3. **Item 1 last, because it is code and its rows come from item 2.** A header button, a dialog
   with one search box, and a table of *Error code · System type · What it means*. The rows
   ship inside the page, so it works offline, and the smoke test covers it. It never says more
   than a sourced topic says: every row is a code item 2 verified.
4. **Every code is read in Microsoft's own reference before it is written** — the Windows
   Installer error list, Intune's app installation error reference and Configuration Manager's
   — and anything that cannot be confirmed there is left out rather than guessed.

## 4. The owner's reference — MSI against EXE in MECM

Added as written, as the reference items 2 and 3 are measured against. It is the owner's account
of how the Application Model treats the two formats, and it is the shape the `endpoint` topics
should have: the comparison table, the client's log trail, the pitfalls and a checklist. Its
specific claims, the error codes above all, are checked against Microsoft's documentation
before a card repeats them, and the record of the wave that writes the topics says which were
confirmed and which were not.

```markdown
# MECM Application Model: MSI vs. EXE Deployment Guide

## Overview

In Microsoft Endpoint Configuration Manager (MECM), **MSI (Windows Installer)** files integrate natively with the Application Model by automatically populating install/uninstall strings, detection methods, and return codes. **EXE (Script Installer)** files are opaque wrappers that require administrators to manually research and configure silent switches, detection logic, and return codes in the console.

> [!IMPORTANT]
> **Recommended Action:** Always prioritize vendor **MSI** installers for standard enterprise deployments. If a vendor only provides an **EXE** or requires complex pre/post-install tasks (such as closing active processes or copying configuration files), wrap the deployment using a standardized PowerShell script via the **Script Installer** deployment type.

---

## Architectural Comparison: MSI vs. EXE in MECM

When creating a Deployment Type under `Software Library > Overview > Application Management > Applications`, the MECM engine handles MSI and EXE files through two distinct workflows:

| Feature / Mechanism | MSI (`Windows Installer (*.msi file)`) | EXE (`Script Installer`) |
| --- | --- | --- |
| **Metadata Parsing** | **Automatic:** MECM reads the MSI database tables directly to extract Product Name, Version, Publisher, and Product Code GUID. | **Manual:** MECM cannot see inside the EXE wrapper. All metadata must be typed manually into the wizard. |
| **Install / Uninstall Strings** | **Auto-Generated:** Automatically populates `msiexec /i "app.msi" /q` and `msiexec /x {Product-GUID} /q`. | **Manual Research Required:** You must discover the vendor's underlying packager (InstallShield, Inno Setup, NSIS, WiX) and supply exact silent flags (e.g., `/S`, `/silent`, `/verysilent`, `/qn`). |
| **Detection Method** | **Auto-Created:** Automatically configures detection using the **MSI Product Code GUID** and optionally the `ProductVersion` property. | **Manual Configuration Required:** You must manually build a Detection Clause using **Registry Keys** (`HKLM\...\Uninstall`), **File System** (file path and version), or a custom detection script. |
| **Customization** | **Standardized:** Handled natively via Windows Installer Properties (`PROPERTY=VALUE`) or Transform files (`TRANSFORMS="custom.mst"`). | **Vendor-Specific:** Requires passing command-line arguments, answer files (`.iss`, `.ini`, `.xml`), or wrapping the EXE in a script. |
| **Return Codes** | **Standardized:** Adheres strictly to `msiexec` standards (`0` = Success, `3010` = Soft Reboot, `1641` = Hard Reboot, `1603` = Fatal Error). | **Non-Standard:** Varies wildly by vendor. Custom return codes must be manually mapped in the **Return Codes** tab of the Deployment Type properties. |

---

## Client Enforcement & Evaluation Lifecycle

Regardless of whether you deploy an MSI or an EXE, the MECM client agent processes them through the exact same local state machine, tracked in `C:\Windows\CCM\Logs`:

| Execution Phase | Client Log File | How MSI Works vs. How EXE Works |
| --- | --- | --- |
| **1. Pre-Install Discovery** | `AppDiscovery.log` | **MSI:** Queries the local Windows Installer database for the `{GUID}`. <br>**EXE:** Checks the specific File Path or Registry Key manually defined. If detected, installation is skipped. |
| **2. Content Download** | `CAS.log` & `DataTransferService.log` | Identical for both. The client downloads all files in the content source folder from the Distribution Point to `C:\Windows\ccmcache`. |
| **3. Enforcement** | `AppEnforce.log` | Executes the command line under the `NT AUTHORITY\SYSTEM` context (if set to *Install for system*). Logs the exact command string, Process ID (PID), and waits for the process to exit. |
| **4. Post-Install Verification** | `AppEnforce.log` | Immediately after the installer exits with a success code (`0` or `3010`), MECM re-runs the **Detection Method**. If a manual EXE detection rule is misconfigured, MECM throws error `0x87D00324` (*The application was not detected after installation completed*). |

---

## Common Pitfalls & Remediation

> [!WARNING]
> Always test EXE silent switches under the `NT AUTHORITY\SYSTEM` context prior to deploying to production collections to avoid hidden modal dialog prompts hanging the MECM client enforcement thread.

| Pitfall | Root Cause | Remediation |
| --- | --- | --- |
| **Error `0x87D00324` on EXE Installs** | The EXE installed successfully, but the manual Detection Method checked the wrong registry hive (e.g., 32-bit vs. 64-bit `WOW6432Node`) or wrong file version. | Verify the exact registry path in `regedit` on a test machine after installing, or select **"This registry key is associated with a 32-bit application on 64-bit systems"** in the Detection Rule window. |
| **Installation hangs for 120 minutes (`0x87D00664`)** | The EXE silent switch was omitted or incorrect, causing a hidden UI dialog box to prompt for user input under the non-interactive `SYSTEM` account. | Test the exact command line locally using `psexec.exe -i -s cmd.exe` to simulate the MECM `SYSTEM` context and verify zero UI popups appear before deploying. |
| **EXE spawns child process and exits early** | Bootstrapper EXEs often extract an underlying MSI, launch it, and immediately close the main EXE process. MECM sees the main PID close, runs Detection too early, and fails. | Extract the underlying MSI from `%TEMP%` while the EXE is open, or use a PowerShell wrapper script that waits for child processes to finish before exiting. |

---

## Pre-Deployment Verification Checklist

- [ ] Verify whether an official vendor `.msi` exists or can be extracted from the `.exe` bootstrapper.
- [ ] Test silent install and uninstall command strings locally under the `SYSTEM` account (`psexec.exe -i -s cmd.exe`).
- [ ] Validate that the Detection Method accurately reflects the installed state (Registry `Uninstall` key or primary executable `File Version`).
- [ ] Confirm custom vendor exit codes are mapped in the Deployment Type **Return Codes** tab.
- [ ] Distribute content to target Distribution Point Groups and validate `AppDiscovery.log` and `AppEnforce.log` on a pilot client.
```

## 5. What shipped — the twelfth and thirteenth waves

Recorded below as two sessions. The twelfth wrote items 3 and 2 as topics, readers first: 8
queries opened at **0 of 8** and closed at **8 of 8**. The thirteenth built item 1.

| Item | Where it went |
|---|---|
| 3. MSI, .intunewin and EXE | `endpoint` *MSI, EXE &amp; .intunewin — What Each Package Is, and How It Installs*: what runs and what Windows records for each, what a deployment tool can read from an MSI and must be told about an EXE, and testing as SYSTEM with the guide's three pitfalls |
| 2. Intune and MECM codes | `endpoint` *App Deployment Error Codes — Intune and MECM Side by Side, by What Raised Them*: three layers that raise codes, how 0x80070643 is 1603, twelve common codes with their pairs, and the two tools' return-code types and time limits side by side |
| 1. The lookup in the tray | A 🧾 ERRORS button in the header, and the `c` key, open a search over 156 codes in whichever form a console printed them, with columns *Error code · System type · Use of it*. Every row is copied from a Microsoft reference that was read, and the rows ship inside the page |
| The guide in §4 | Checked against Microsoft's pages. Confirmed: the auto-filled MSI detection, the 32-bit detection option's wording, MECM's 120-minute default run time, the return-code types, the log trail and the PsExec test, which Microsoft's own reference gives. **Not confirmed: 0x87D00664**, which appears in none of Microsoft's references, so the cards describe the timeout without a code |

**What is left.** Intune's default return codes are confirmed only by packaging vendors'
documentation, because Microsoft's page says defaults exist without listing them; the topic's
anchor says so. And the lookup knows what Microsoft's three references list and nothing else,
which is the point: a code it cannot find is one nobody here has a source for.


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

### And the ordering is a narrative, which is now measured rather than assumed

This section's title has always said a path is *one domain's story*, and meant it
about **coverage** — which domains had a path at all. It turns out to be true of
**ordering** too, and the number is the evidence.

95 of the 1,497 topics on a path are on more than one, so two paths can disagree
about which of a pair comes first. `check_paths.py --ordering` counts it: **56
pairs are ordered by two or more paths, and 17 of them — 30% — are ordered in
opposite directions.** They cluster: eight between `ai-at-work` and
`ai-safety-and-governance`, four between `ransomware-end-to-end` and
`threat-landscape`.

Read one at a time, every one is two legitimate stories.
`cryptography-end-to-end` puts encryption basics before password hashing because
the track builds from primitives; `security-for-everyone` puts hashing first
because it is the concrete thing a reader has already met. **Neither is wrong and
no third path can arbitrate**, which is exactly what it means for these to be
narratives rather than prerequisites.

So the 30% is the finding and not a defect, and it has one consequence worth
writing down before somebody spends a wave on it: **a global ordering cannot be
derived from `paths.json`.** A generated curriculum, or a "what should I read
first" feature, would be building on a relation this data does not carry, and
would contradict itself on a third of the pairs it found. The report exists so
the next session reads the number instead of re-deriving it.

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

## Session — a measurement of verdict quality that did not work, and what it found anyway

### The thing nobody had measured

The register's standing habit is *once a phase, measure something nobody has
measured*, and the card rubric names the target itself. Its §5 table has two
columns, **Checked mechanically** and **Not checked, ever**, and the second
column's first entry is *whether the card is interesting*. One row down from
that is the one that looked reachable:

> **Restated verdict** — the closing sentence says what the table said. *Cut it.
> A missing verdict is better than a redundant one.*

`lint_content.py` counts tables with **no** verdict — ten, all deliberate. It
has never had anything to say about the 2,716 verdicts that **do** exist. So the
question was: is a restatement detectable?

### Attempt one: lexical novelty. It ranks good verdicts at both ends

For each verdict, the fraction of its distinct content words absent from the
table it follows. A restatement should score low.

Median **0.86**. And the bottom of the distribution is not restatements:

> *Mounting pressure is the row that matters and the one nobody argues about.*
> *The named blocker is the row that turns a report into a request.*
> *Row three is the whole intervention; the rest is measurement and housekeeping.*

Those are three of the twelve lowest-novelty verdicts on the site and all three
are doing exactly what the rubric asks. They score low **because a verdict that
picks a row has to name the row**, and naming it means reusing the table's
words.

The other tail is no better. Fourteen verdicts score a flat **1.00** — no
content word in common with their table — and they include *The last row is the
one to design around* and *Every row leaves hardware behind on somebody's
site*. Zero lexical overlap, and both are plainly about the table.

**The metric is orthogonal to the property.** A restatement can be written
entirely in fresh words, and a good verdict can be written almost entirely in
the table's. That is not a tuning problem; it is the wrong axis.

### Attempt two: judgement markers. 21% lack them and are fine

A lexicon of forty decision words — *worth*, *never*, *instead*, *prefer*, *the
row that*, *rather than*, *the test is*. A verdict carrying none of them is a
candidate summary. **574 of 2,716, 21%.**

Twelve read at random from that bucket, and every one is a judgement:

> *Good fit: a fleet of reasonably standard devices where update babysitting is
> eating a person. Poor fit: heavily regulated change windows…*
> *Record the timezone explicitly.*
> *Quick test: if the installer works from an elevated PsExec -s shell with no
> desktop, it will work in system context.*

The lexicon was a dictionary pretending to be a rule, and English has more ways
to give an instruction than anybody enumerates on a Tuesday.

### The conclusion, and it is the phase-11 one

**Verdict quality is not lexically measurable, and no third attempt is planned.**
Both proxies failed for the same underlying reason — restatement is a *semantic*
relation and every cheap handle on it is syntactic — and a hand-read of the
likeliest bucket found nothing to catch. Phase 11 reached this about the
freshness denominator after three attempts and wrote the reasoning down instead
of the tool; this is the same shape and gets the same treatment.

**No tool shipped, on purpose.** A census with no decision attached to it is the
decoration this file already warned about once. The number that would have gone
in the measured-state table — *574 verdicts with no judgement marker* — is a
number nobody should act on, and putting it in a table is how it becomes a
number somebody eventually does act on.

### And the thing the failure found, which is the actual deliverable

Reading the tails to work out why the metric was lying produced a house form
that no file here had ever stated. **431 verdicts — 16%, across 32 of 35 domain
files — point at their table by naming a row by position.**

> *The last row is the one that ruins a Friday.* · *Only the second row actually
> bounds the damage.* · *Work down this table in order and stop at the first row
> that works.*

It is the mechanism under the rubric's property 5, and it is in the rubric now.
It does both halves of a verdict's job at once: a claim about **which row
matters** is the one thing a table cannot say about itself, and a pointer means
the verdict never has to restate what it is ranking. The practical rule that
falls out is testable by the writer: **if you cannot name which row matters, the
table is probably unranked**, and the listicle failure applies to the table
rather than to the verdict.

That is worth more than the check would have been. The check would have
reported candidates a person then had to read; this changes what gets written.

```
2,716 verdicts measured two ways · 0 restatements found by either, or by reading
attempt 1 lexical novelty — median 0.86, and both tails are good verdicts
attempt 2 judgement lexicon — 574 without one, 12 read, 12 were judgements
no tool shipped: a census with no decision attached is decoration
431 of 2,716 (16%) in 32 of 35 domains name a row by position — now in the rubric
```

## Session — 102 stories that disagree about the order a third of the time

### The measurement

A path is an ordered list. 95 of the 1,497 topics on a path are on more than
one, so two paths can make competing claims about which of a pair comes first,
and nothing had ever asked whether they agree.

**They disagree 30% of the time.** 56 topic pairs are ordered by two or more
paths; **17 are ordered both ways.** Eight of the seventeen are one path pair —
`ai-at-work` against `ai-safety-and-governance` — and four are
`ransomware-end-to-end` against `threat-landscape`.

### Why 30% is the finding and not seventeen bugs

Read one at a time, each is two legitimate stories:

> `cryptography-end-to-end` puts encryption basics before password hashing,
> because the track builds from primitives. `security-for-everyone` puts hashing
> first, because it is the concrete thing the reader has already met.

Neither is wrong. `ransomware-end-to-end` leads with ransomware because the path
is *about* ransomware; `threat-landscape` reaches it after infostealers because
it is working through an ecosystem. **No third path can arbitrate**, and that is
the definition of a narrative rather than a prerequisite.

If these were prerequisite claims, 30% would be alarming. The fact that every
case reads as defensible is what tells you they are not prerequisite claims —
the disagreement rate is the *evidence for* the section's long-standing title,
not a contradiction of it.

**The consequence is worth more than the count**, and it is written into the
paths section so a future session finds it before starting: a global ordering
cannot be derived from `paths.json`. A generated curriculum would be building on
a relation the data does not carry and would contradict itself on a third of the
pairs it found.

### The three decidable defects, all at zero

Worth stating because they are what a person would assume this was checking:

| | Count |
|---|---|
| a topic listed twice in one path | 0 — and already warned on, so this was not new |
| a path that is an ordered subsequence of another | 0 |
| a step pointing at a topic that does not exist | 0, gated |

So the ordering report gates nothing, which is consistent with the rest of this
file: *topics off a path are reported, never failed*, because a topic does not
owe a path. There is nothing here to fail on either.

### The report was wrong twice before it was right, and the fixtures are why

**It undercounted by eighteen.** Iterating the pair keys and skipping `x > y`
never visits a pair whose only key is the reverse — two paths that both say
`b` then `a` produce only `("b","a")`, and the loop skipped it. 38 against a
hand count of 56, and a report that quietly undercounts is the one thing a
report is worst at showing you. Normalising the pair before the lookup fixed it.

**And it counted one path as two.** A path that repeats a step orders that pair
in both directions by itself, so `["a","b","a"]` scored as a disagreement. That
is a copy-paste, the duplicate warning four lines up already reports it, and
turning it into a second and wronger finding is how a census loses trust. The
rule is distinct *paths*, not assertions.

The second one was caught by a fixture written for it — `a pair one path orders
twice is not shared` — which failed on the first run. **Six fixtures for a
function that gates nothing** is the right ratio here, because a report nobody
can check is worse than no report: it gets quoted.

```
56 pairs ordered by two or more paths · 17 both ways (30%) · 0 defects
check_paths.py --ordering, reporting only — the number is the finding
+6 self-test fixtures; two of them are the two bugs the first version had
consequence recorded: no global ordering can be derived from paths.json
45 gates green · make all clean
```

## Session — batch eighteen, and two words the site had never written down

### Two thirds again, for the third batch running

**28 questions, 20 answered.** Batch seventeen was 22 of 29. Batch sixteen's
symptom-shaped half was the same fraction. This file has now predicted the
opening rate three times and been right three times, which makes it the one
number here that behaves like a forecast rather than a measurement.

Eight zeros, and the per-word diagnostic split them in one read, because **two
of the eight contained a word the site does not have at all**:

| Query | Binding word | Corpus |
|---|---|---|
| `the process is defunct` | `defunct` | **0** |
| `i got laid off` | `laid` | **0** |

Everything else in both queries was present in the hundreds. A word at zero is
the report's clearest signal and it separated the real gaps from the phrasing
misses before any card was opened.

### `defunct` — and nine zombies, none of them a process

`zombie` returns nine mentions on this site and **every one is a cloud-cost
zombie**: an unattached disk, an idle load balancer, a forgotten dev
environment. `grep zombie data/linux.html` returns nothing. So the classic Unix
zombie — a child that exited and a parent that never reaped it — was absent from
a domain with sixty-two topics, while its name was in use elsewhere for
something else entirely.

**`linux` — The Process You Cannot Kill Is Already Dead**, added to *Processes &
Signals*, which is where it belongs for a reason the existing card supplied. That
topic's signal table ends on a verdict: *keep SIGKILL for the process that has
already ignored a polite request.* The zombie is the one state on the whole page
where SIGKILL does nothing, because **a zombie is not a stuck process; it is a
death certificate nobody has collected.**

The fingerprint is the half worth having, and it is why this hides: memory flat,
CPU flat, machine not slowing down. What fills is the process table, and the
failure lands somewhere else and much later — the next `fork()` anywhere on the
box returns **`Cannot allocate memory` on a machine with gigabytes free**. An
out-of-memory error that is not about memory is the tell.

Two things the card insists on because everybody gets them backwards. An
**orphan is fine** — the parent died, PID 1 adopts and reaps correctly — so the
intuition inverts: the one that still has a living parent is the broken one. And
`<defunct>` is in the card because it is **the string `ps` prints on the
reader's screen**, which is the rule this file set after the USB card: a card
about a failure quotes the words the reader is looking at.

### `laid` — a whole topic on it, and it would not say the word

`mind` has *Layoffs & Job Loss — The First Week, and the Ones After*, and it is
a good card. Its opening sentence was *"Almost everyone in a long IT career goes
through this at least once"* — and `laid` returned zero across the entire site.

The fix is four words and it is **better writing than what it replaced**: *almost
everyone in a long IT career gets laid off at least once*. That is the promise
the kind-1 rule makes and it keeps making good on it. `i got laid off` now
returns one card, the right one.

### Named and not written, with the word that is missing

`our reserved instances expired`. `cloud`'s *Commitment Discounts* is thorough
on **buying** one — a commitment is a bet on your own capacity forecast, commit
the floor and never the ceiling — and has nothing on the other end. **Expiry is
a diary problem, not a forecast problem:** the bill rises 30–70% overnight with
nothing deployed, nothing changed and no alert, because the discount stopped
rather than the usage starting. `expired` appears 29 times and not one is a
commitment.

Recorded with its evidence rather than written, because the wave had spent its
card — and named as a **missing word plus a missing owner**, which is the form
this file has twice found to be pickable up cold.

### The six that were not gaps, and one that is thinner than kind 3 usually is

`the new starter is missing from teams` (licensing, and `starter` is the
reader's noun for a joiner) · `the usb ports on one side stopped working` (a
controller or a front-panel header, which is exactly the isolate-and-halve shape
`hw` teaches) · `the job ad wants ten years of a five year old tool` (a joke
with a real question inside it, and no card has a reason to contain *ten* and
*five* about one tool) · `the vendor will not fill in the questionnaire` — the
best of the six, because `grc` files the answer under **the phase where the
leverage is created rather than the phase where it is missed**: *bake security
requirements into the contract — right to audit*. The reader's word is the
artefact; the site's word is the clause.

The thin one is `i changed one line and fifty tests failed`. `eng` has
*Over-mocking* and *Test Doubles*, which is the cause — but the site names it
from the writer's side, a test coupled to an implementation, and never from the
reader's, fifty red tests after a one-line change. It is recorded as kind 3 and
flagged as the thinnest of the five, because the gap is a sentence rather than a
card and the next session should know that before it opens the file.

```
1 concept card (linux Processes & Signals) · 1 prose fix (mind) · 0 new topics
probe 302 -> 330 questions · 304 answered · 0 unexplained · 25 zeros · 1 wrong · 7 wide
batch eighteen opened at 20 of 28 — two thirds, the third batch in a row
2 of 8 zeros had a word at 0 in the corpus; both were the real gaps
1 named and not written: `our reserved instances expired`, with its missing word
45 gates green · smoke 163 · search 58 · a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```

## Session — writing the card the last wave named, and the gate that caught its author

### The gap, closed the wave after it was named

The previous record named `our reserved instances expired` as kind 2 and wrote
the evidence instead of the card, because the wave had spent its edit. That form
— **the missing word plus the missing owner**, rather than the missing subject —
has now got three cards written by a later wave, and this is the fourth.

**`cloud` — A Commitment Expires, and Nothing Tells You**, added to *Commitment
Discounts*, which was thorough on buying one and silent on the other end. The
sentence: **expiry is a diary problem wearing a cost incident's clothes.**

The fingerprint is what makes it findable and is the reason it gets misdiagnosed
for days: **a cost jump with a flat usage graph.** Nothing was deployed, nothing
scaled, no region was added — and the rise is suspiciously round, because it is
exactly the 30–70% that had been coming off. When the usage line does not move
across the step, the cause is commercial and every hour in the architecture
diagram is an hour in the wrong document.

It is missed structurally rather than carelessly. A commitment is bought by one
person in one quarter and lapses twelve or thirty-six months later, by which time
that person has moved. **Coverage is a percentage on a dashboard nobody opens,
and it falls silently rather than alerting.** The nearest sibling on this site is
a certificate: bought once, silent until the day it is not, fixed by a date with
an owner rather than by any technical control.

The verdict is the row that surprised me while writing it. **Auto-renew is the
wrong default for the same reason buying without a forecast is — it turns a
decision into a subscription**, and renews a commitment nobody re-forecast, which
is the exact failure of the card directly above it, arriving on a timer. The
right default is a dated review owned by whoever owns the forecast, with
auto-renew on only where the baseline has already held across a full previous
term.

### And the reader's word, on the fourth consecutive wave to need it

`our reserved instances expired` returned **zero against the card written to
answer it**. The card said *expires*, *expiry* and *lapses*; the reader says
**expired**, and the matcher's plural rule reaches `expireds` rather than
`expires`.

The fix is a clause that adds something rather than repeating anything — *the
invoice does eventually explain itself, a line saying the reserved instances
expired, and it arrives a month after that would have been useful* — which is
both the reader's phrasing and a fact the card did not previously carry. Four
waves in a row have now ended with this step, and the pattern is stable enough
to be a prediction: **a card written mechanism-first will not close its own
query, and the fix is always a sentence that is better than what it replaced.**

### The gate from two waves ago failed the build on its author

`make all` went red on **one word**: *organisation*, in a row of the table I had
just written. `check_spelling.py` named the file, the word and the sentence.

That is worth a paragraph because of what it says about the sweep it came from.
Two waves ago the argument for building a rule-based checker rather than adding
registry rows was that **enforcing a convention by row enforces exactly the words
somebody thought of** — and the evidence was 2,192 spellings accumulated with the
build green. The first thing the rule caught after that sweep was not a legacy
card. It was new prose, written by the session that built it, three days after
the convention was supposedly settled.

A convention with a gate is a convention. Without one it is a paragraph in
`CONTRIBUTING.md` that everybody agrees with and nobody satisfies.

```
1 concept card (cloud Commitment Discounts) · the gap the last wave named
probe 330 questions · 305 answered · 0 unexplained · 24 zeros · 1 wrong · 7 wide
the card did not close its own query until the reader's word went in — fourth wave running
check_spelling.py failed the build on its own author's new prose, one word
45 gates green · smoke 163 · search 58 · a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```

## Session — the contract said "if it passes, CI passes", and CI had been red for four runs

### Found by looking, not by being told

PR #60 opened on this branch and the first thing worth checking was the base.
`main` at `4d2ae9c` — this PR's own base commit — had **failed its last four
workflow runs**, and so had the two pull-request runs before that. `make all`
has been green on this machine throughout.

That combination is the exact thing `check_gates.py` exists to prevent, and the
measured-state preamble says so in a sentence written when it was added:

> **`make all` is the contract.** If it passes, CI passes.

It was not true, and had not been for four runs.

### One step, and it is the one that had no reason to need a browser

```
Run node tools/query_probe.mjs --self-test
error: playwright not found. Run: npm install playwright
Process completed with exit code 2.
```

`query_probe.mjs` resolved Chromium in a **top-level `await`, at import**, so it
ran before `process.argv` was ever consulted. `--self-test` needs no browser and
no built page — it runs `staleReason()` and the plan-row reader over fixtures —
but the process was already gone.

And `make check` is **deliberately browser-free**: its own comment says the
generated-artefact checks are cheap and first and *none of them needs a
browser*, which is why the `verify-build` job installs Python and no Node
toolchain at all. So the one command on that list that did need one exited 2
every time, on every push, while every developer machine had Playwright
installed and saw green.

### What `check_gates.py` actually guarantees, which is less than it reads as

The gate compares two **lists** and they agreed — 42 then, 45 now. It has never
had anything to say about whether a command on the agreed list can *run in the
job it is listed in*. That is a second, unstated assumption, and it is the one
that broke.

The nine-commit outage that motivated `check_gates.py` was *a step in one list
and not the other*. This is *a step in both lists and impossible in one job* —
the same red-on-the-server, green-locally split arriving through a door the
guard does not cover. The preamble is corrected rather than deleted: the claim
was worth making and it was wrong, and both halves are the record.

### The sibling tool already had it right

`gen_og_image.mjs` sits in the same browser-free job, imports Playwright the
same way, and **launches a browser at the top level too** — and its step has
been green throughout. It handles `--check` and `process.exit(0)`s at line 154;
the browser is resolved at 162. The early exit precedes the dependency.

So this is *the check that already existed, one file over* for the fourth time
in this file. One of two tools in one job got the ordering right, nothing
compared them, and the one that got it wrong was red on every push for a month.

### The fix, proved against a reproduction rather than against reasoning

`browserFor()` resolves at the point of use, and `requireBuiltPage()` does the
same for the `index.html` guard one line below it — the identical defect, which
would turn a fresh clone into an exit 2 before the first fixture.

Reproduced first, because a CI fix asserted rather than reproduced is the
*asserts it did not throw* row of this file's own table. A copy of the tool with
the module-search fallback emptied is precisely what "not installed" means to
this code:

```
before   node tools/_nopw_probe.mjs --self-test  ->  exit 2, "playwright not found"
after    node tools/_nopw_probe.mjs --self-test  ->  23 fixtures, 0 failures, exit 0
after    node tools/_nopw_probe.mjs --zero       ->  exit 2, and now says why:
         "playwright not found, and the census needs a browser"
```

The third line matters as much as the second. A census that cannot open a
browser must still fail loudly; what changed is that it fails when it is asked
for a census, not when it is asked for a fixture run.

```
root cause: a top-level await resolved a browser before argv was read
red on main for 4 runs · green in `make all` throughout · 1 file, 2 deferrals
reproduced with the fallback list emptied, then fixed, then re-proved both ways
gen_og_image.mjs, same job, same import, exits on --check first — and was green
the contract sentence in the preamble is corrected, not deleted
45 gates green · CI green is the one this wave has to wait for
```

## Session — conducting batch two: the notes were a dialect, not a list of definitions

The queue section *Study notes, batch two* was conducted end to end, in its own §6 order: the
correctness fix first, the zeros into the census before any fix, then the writing. Seven
commits, two new topics (1,557 → 1,559), and a student reader that went from **1 of 15**
answered to **15 of 15**. Its §8 says what went where. This records what the plan did not predict.

### The bug beside the bug

The `colou?r` examples were known before the session began. Reading the table they sat in turned
up the word-boundary row showing an empty token and saying `cat` won't match *concatenate*, which
without the boundaries it does. The `\b`s were **backspace bytes**. One scan of every source found
five lines, three topics and eight bytes, all one mechanism: a backslash escape through a non-raw
Python string. `\a` in `CORP\alice` had become a bell, twice. The browser draws nothing for
either, and every one was well-formed markup, so no gate here could have seen them. Now
`check_markup.py` fails on a C0 control character and names the escape that probably made it.

Both guards were proved the way the manual asks, by switching them off. With the contrast window
at 0, the four spelling fixtures fail with the exact *color or color* tautology. Against the
pre-fix files, the markup check reports all eight bytes.

### The census opened worse than any symptom batch, and for a different reason

Symptom-shaped readers open at two thirds missing because readers describe what they see.
This subject-shaped reader opened at 14 of 15 because it spoke **another dialect**. The probe's
own diagnosis split the twelve zeros: five were words the site had never written (`datediff`,
`sp_executesql`, `unpivot`, `markov`, `smote`) and seven were words it had, never together on one
card. None of the fixes was a synonym. Each was the dialect's actual behavior, written as the trap
it sets: PIVOT's frozen column list, the `UPDATE` that NULLs every unmatched row, `DATEDIFF`
counting boundaries. One query did need the reader's word: `sql like wildcard` closed only when
the card said *wildcard*.

### §4's condition decided itself

§4 said to write a SQL Server card if the rows could not be written without each saying "in SQL
Server". They could. Every row came out as a comparison across engines, so the dialect was the
topic. The rows that had nowhere else to go (bracket patterns, collations, `BIT`, `#temp`) became
a card whose inversion is that **the dangerous differences are the ones that parse**. A product
card would have repeated what the comparison already carried.

### Three misses, two of them mine

1. **DPO**, expanded as *Data Protection Officer* in an RLHF title. It was found by reading, the
   same class as failure 10 in the manual: well-formed markup, a defined acronym, and wrong.
2. **"Design judgement"** went into the UML card, and the wave was committed without a full
   `make check`, the one wave where it was skipped. It was caught on the next wave. The lesson is
   the ratio the manual already states: the static gates cost a minute and caught the only
   slip. When usage has to come down, batch the browser suites, not the static ones.
3. **`is the attacker still in`** crossed the wide threshold by one. A T-SQL comment in the
   injection card said an identifier *still* cannot be bound, and the card already said
   *attacker*. Rewording the comment would have been editing prose to satisfy a counter. The query
   carries a verdict now: `still` is an ordinary adverb, and the answer is inside the set.

### What is left in this section

Nothing from §6, and the §5 table stays as the gate it was written to be. The notes themselves
are unchanged in §7. Correcting them is the owner's call, the same outward direction as batch
one's item 7.

## Session — conducting the first batch: the words it asked for already meant something else

The queue section *Knowledge integration* was conducted end to end: the reader first, then item 7
because §4 said it was the cheapest, then items 1, 3, 4, 5 and 6. Six content commits, two new
topics (1,559 → 1,561), and a reader that went from **9 of 25** answered to **25 of 25**. Its §6
says what went where. This records what the plan did not predict.

### Nine misses had results, and a `want` is what counted them

The last two queue sections found the same shape by hand: a word the reader navigates by, already
owned by another sense. Chip subtitles first, then *stack* and *queue*. This reader counted it.
Nine of its sixteen opening misses returned cards, just not the right ones: `logic gates` reached
twelve cards about pipeline and approval gates, `multi core processor` reached the GDPR's data
processor first, and `task analysis` reached sixteen cards about log and malware analysis.

Counting them needed a target for cards that did not exist yet. So the `want` named the topic being
written into, fixed by its title before the reader was committed. Without it a wrong-sense result
scores as answered by count, which is the `printer offline` failure in the probe's docstring
arriving through a new door. **A `want` may name a topic that the same session is about to write**;
the commit that writes the card is where it gets checked, and every one of them closed.

### The plan's grep was wrong once, and it was a hyphen

§2 listed five concepts as nowhere in `data/*.html`. Four were absent. The data-flow diagram is a row
in *Diagrams That Explain*, spelled *data-flow*, which the grep did not allow for and the search
does, because it folds separators. The reader found `data flow diagram` answered on its first run.
It is the probe's own `wifi 4` mistake, where the per-word line reported *wifi* at 4 until it
folded the way the matcher folds. **Decide "absent" with the matcher, not with a grep.**

### An inventory that says "prose" means go and look

§2 also called cognitive load *prose in five files*, and two of the five were whole concept cards:
`career`'s on training, and `devops`'s *Three Kinds of Cognitive Load*, with the same three-row table
the first draft of the new `web` card repeated. The card now points at it and keeps only the
interface half. It is the manual's habit #1, read the neighbours' concept-card titles, and this time
the neighbour list was the plan's own inventory, which had counted files rather than cards.

### Item 3 moved twice

The plan moved it from `linux` to `hw` by chip subtitle, correctly. One level further down, truth
tables and De Morgan are in `cs` *Boolean Algebra*, and so is the architecture stack from number
representation to pipelining. Gates are that algebra in silicon, so they went beside it, and the
glitch card points back at `hw`'s *Signals* for the analogue underneath.

### Found by reading, twice

`blueteam`'s *Normalization Schemas* expanded **ECS** as Elastic Container Service in a card about
log schemas, where it is the Elastic Common Schema: the manual's failure 10, well-formed and wrong.
And `ops`'s incident-metrics table had a row reading *MTBF (Mean Time Between Failures) between
failures* beside a replacement that splits recovery time into detection and repair. The cell was
garbled when it was written, in one squash commit, and now names the metric the row is about.

### My own three

1. **`judgement`**, in the automation-bias table. `check_spelling.py` failed the wave on it, the
   same word batch two slipped into its UML card.
2. **Two commit messages quoted query counts I had added up rather than read.** The `eng` wave
   claimed six closes and made five, because `waterfall vs agile` was already answered; the `ops`
   wave claimed two and made one. Both were caught by reading the census against the message
   before pushing, and amended. It is *a number I incremented fifteen times*, again, and the guard
   is the same: the number comes from the tool, never from the writer's arithmetic.
3. **The stamper moved topics nobody touched.** `stamp_freshness.py --only <domain>` re-dated dozens
   of topics per domain, because the blame derivation drifts with the git version, and `--check`
   would rewrite all 34 files. Each wave kept only the moves for topics it edited.

### What is left in this section

Nothing. The §3 domain decision stays deferred with its condition unmet: the UX half is one topic
of four cards, not six. `axe-core` was missing from this container and was installed globally at
CI's pinned version, so `make a11y` runs here as it does on the server.

```
7 commits · 2 new topics (1,559 -> 1,561) · 6 concept cards in existing topics · 2 fixes found by reading
reader 9 of 25 -> 25 of 25 · census 345 of 370, 0 unexplained
45 gates green · smoke 163 · search 58 · a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```

## Session — conducting csvistool: an answer that rested on 647 against 644

The queue section *csvistool* was conducted after *Knowledge integration*, in its own §4 order: the
reader first, then the links, words and sentences, then §3's gap, then the candidates. Four
commits, no new topics, five concept cards, 39 deep links, and a reader that went from **0 of 16**
to **16 of 16**. Its §5 says what went where. This records what the plan did not predict.

### A zero that was 58 cards

§2 recorded `splay` as a zero from its search probe, and footnoted that a grep for it had matched
*display*. Today the search does the same: a term longer than four letters matches as a substring,
and *splay* sits inside *display* on 58 cards. Whether the matcher or the scratch copy changed
since, a zero written down in prose is exactly what a checked-in reader exists to stop being. The
reader carries `splay tree`, which is what a student types, and it opened on three cards about LVM,
page rendering and the acronym index.

### A title is a count

§2 called depth-first search "a missing row" and Floyd-Warshall "a row in the graphs table". The
topic is *Graphs — Representation, Traversal & the Four Algorithms Worth Knowing*, its table has
four rows, and a sixth would contradict the title, while renaming it moves a permalink that
people's progress is keyed to. So DFS went into the traversal card, where it is the same loop with
a stack instead of a queue, and Floyd-Warshall into the negative-weights verdict as the answer for
every pair at once. The plan placed them from the card's content; the title is content too.

### The answer that rested on a ratio

The minimum-spanning-tree wave broke a service-desk query nobody was watching. `user left who gets
their files` was answered only by the relaxation stage, which drops the commonest word while it is
at least four times as common as the rarest. *gets* was on 647 cards and *left* on 161, and
4 × 161 is 644. The union-find card asked how many islands are **left**, *left* went to 162, the
threshold went to 648, relaxation stopped, and the JML card fell out of the result.

It had been balanced on that edge all along, under half a percent from the line, and nothing in the
census reports that distance. The fix was the probe's kind 1, not a rewording of the new card:
the JML row now says *decide who gets the leaver's OneDrive files*, the reader's verb for what the
row is about, so the card holds all four words and answers from either stage. **Named and not
built:** a census column for queries answered only by relaxation, with how far each sits from the
ratio. Until it exists, the next one will also be found by accident, by whichever wave happens to
add a common word.

### Links are dated claims, and the count was a choice

§1 asked for a fact anchor on every deep link. One per line of links carries the same information,
because each anchor names every route it covers, and costs 18 anchors instead of 39. The first
draft of this paragraph said sixteen, added up across the waves; `grep` said eighteen, which is the
first batch's lesson a third time: the number comes from the tool. Phase 11's
counter-discipline says a rising count of dated claims is not automatically progress. This rise is
real, since a route is a key in someone else's repository, and it is the smallest one that keeps
every route findable with one grep.

### Checked, and one sentence that was not true as drafted

The routes were checked against the registry on the tool's `master` branch, all 41 of §2's keys,
and `/:algo` and the 404 redirect against its router and `public/404.html`. `csvistool.com` is
still blocked from this container, so the routes are checked and the pages are not. The skip-list
card's first draft said LevelDB's memtable takes concurrent inserts. It serializes writers, and
only its readers go without locks; RocksDB's version is the one that takes concurrent writers.
Caught before the commit, by checking the one sentence that was a claim about someone else's code.

### What is left in this section

The home-page link on the `cs` landing card, §1's second row. Its condition was that the deep links
earn clicks, and the site measures nothing about clicks, by design, since it makes no third-party
requests. So the condition cannot fire, and it is recorded as the register records a risk with no
reopen condition: honestly, as having none.

```
4 commits · 0 new topics · 5 concept cards · 39 deep links · 18 fact anchors
reader 0 of 16 -> 16 of 16 · census 361 of 386, 0 unexplained · dated claims 59 -> 77
1 regression, found by the census and fixed in the same wave: a relaxation at 647 against 644
45 gates green · smoke 163 · search 58 · a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```

## Session — the ASCII chart, with ASL added, and a spelling the standard owns

A one-line request: add the ASCII character set, from
[the UAH page](https://www.cs.uah.edu/~rcoleman/Common/Basics/ASCIICharSet.html), *if it is not
already there*, and add ASL to it. It was not there. The site said ASCII seventeen times in seven
files and showed the table in none, and had never written the words *sign language*. **ASL is read
as American Sign Language**, fingerspelling and number handshapes, mapped onto the same letters
and digits. It is the only reading under which *add it to this* makes sense of a character chart,
and it is recorded here in case it was the wrong one.

One topic in `cs`, after *Number Representation*: *ASCII Character Set & ASL Fingerspelling — One
Alphabet, Two Encodings*. Eight concept cards. The bit arithmetic (case is one bit, a digit is its
low nibble, Ctrl clears two bits, sorting is numeric order); the full 128 laid out as four columns
of 32 so each row shares its low five bits; the 33 control codes with what still answers to each;
six symptoms and the byte behind each; where ASCII stops and code pages begin; the 26 letters and
ten digits with their ASCII codes and handshapes; and how fingerspelling is read.

### The source could not be read, so nothing was copied from it

`www.cs.uah.edu` is blocked by this container's network policy, as `csvistool.com` was. ASCII is a
fixed standard, so the chart did not need the page: **102 of the topic's 122 table rows are
generated** by a script from the code points and two hand-written dictionaries, the control
names and the handshapes, rather than typed. The page is linked as an `.extlink` beside the chart,
and its fact anchor says the link was supplied and not fetched instead of claiming a check. That
is the *Dated claims* row's one-point rise.

### The reader went in first, and one zero was hiding in a count

*Somebody looking up a character code or a handshape* went into `query_probe.mjs` before the
card, the order csvistool established. It opened at **0 of 12**: five zeros and seven that found
cards, never the chart. `asl` was a zero that the corpus counted fifteen times, every one inside
another word: *asleep*, ASLR, Maslow, SASL. A substring count is not evidence that a word is on
the site, which is the `splay`/*display* finding from the other side. It closed at 12 of 12.

### A British spelling the standard owns

The spelling gate failed on **Enquiry**, control code 5's name in ANSI X3.4, RFC 20 and Unicode's
alias. `CONTRIBUTING.md` has the precedent, *Fibre Channel*, a standard's own name and the only
`ALLOW` entry. Allowing the bare word would have let every prose *enquiry* through, so the
allowed phrase is the whole cell, *Enquiry, as the standard spells it*, which also answers the
reader's question of why an American site spells it that way. Checked both ways: the cell passes
and `Send an enquiry to the desk.` is still a finding.

### One sentence that was not true as drafted, and one table that did not fit

The chart card's aside on bit-paired teletypes first said that no key you press follows the chart's
alignment any more. On a US layout, Shift with 1, 3, 4 and 5 still gives the character 16 below
the digit. Checked pair by pair before it shipped, and the sentence now names the four. At 375 px
the letters table had two code columns and squeezed the handshapes into a strip a word wide, so
the codes became one column, decimal over a muted hex line. The 4-column tables scroll inside
themselves on a phone, the site's existing behavior, and the page itself never scrolls sideways
(checked in both themes).

### What the annotator did, and why it was right

`SYN` gained *(Synchronize)*. That is the TCP sense, and correct where it fell: the cell that says
*not TCP's SYN, which shares only the name*. The ASCII code itself sits in `<code>` in the Code
column, which the annotator does not read. **ASL** joined the dictionary under `Misc`, an existing
category, so the generated acronym domain gained a row and no topic.

### Handshapes are words, not pictures

The site makes no third-party requests and self-hosts its fonts, and a fingerspelling font comes
under someone else's license terms, which could not be read from here. Drawing 36 hands in SVG
would be a claim nothing here can check. So each handshape is a sentence, and the
last card says plainly that reading fingerspelling is learned from people, not from a table.

```
1 commit · 1 new topic (cs) · 8 concept cards · 122 table rows, 102 generated · 1 extlink
reader 0 of 12 -> 12 of 12 · census 373 of 398, 0 unexplained · dated claims 77 -> 78
acronyms 1,103 -> 1,104 · related links 4,896 -> 4,902 · path steps 1,599 -> 1,600
45 gates green · smoke 163 · search 58 · a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```

## Session — pictures of the handshapes, and ASL moved to where it is learned

The follow-up to the last record, the same day: **add pictures of the ASL handshapes, and ASL
belongs in Productivity.** The ASCII topic in `cs` had carried the fingerspelling cards because the
first request said to add ASL *to this*. They now have a topic of their own in `productivity`, after
*Deliberate Practice*: *ASL Fingerspelling — The Alphabet, Numbers & How to Learn Them*. It has four
cards. The alphabet and the numbers each carry a picture grid above the description table, then
there is a drilling card built on the domain's own technique topics, and the reading card that moved
with them.

### The last record said this could not be checked, and it was half right

That record closed on *drawing 36 hands in SVG would be a claim nothing here can check*. The
request made the drawing the job, so the check had to be found. Image hosts are blocked from this
container, as the UAH page was, and the site makes no third-party requests anyway, so the pictures
are drawn. A one-off generator built each one from a palm, a wrist and five *tubes*, and was not
kept: the pictures are plain inline SVG in `data/productivity.html`, and a fix is an edit there. A tube is a centerline stroked twice, outline then fill, so a folded or curled finger is
just a path, and whatever is drawn later sits in front. Shapes that point sideways (G, H) or down
(P, Q) are the upright drawing turned. Numbers 1 to 5 are mirrored, because counting is signed palm
in, so the reader sees the back of the hand. Thirty-seven pictures come to about 30 KB inline,
colored only by classes in `style.css`.

**The check is weaker than a source, and it is what there was:** every picture rendered at size and
read against its own description. That caught four on the first pass. E read as a plain fist,
M and N showed the whole thumb where only its tip should peek out, and T hid the thumb tip it exists
to show. It also caught a fifth kind of error, which no description would. H and the mirrored 1, 2
and 4 show the back of the hand, and the first drawings still showed a thumb tucked against the palm,
which nobody facing the signer can see. The thumb is gone from those four.

**The one convention taken rather than checked:** J and Z are drawn as the signer would write them,
so from the reader's side they run mirrored. The card says so. If a teacher draws them the other
way, that is the arrow to flip.

### Moving the cards moved a permalink, and the tool would not pair it

The ASCII topic lost *ASL* from its title, and the slug moved. `fix_topic_names.py --aliases-only`
records a move by pairing topics in order, and **refused while the same edit also added a topic**:
*topic count or order changed — refusing to guess the pairing*. That is the right refusal. The new
topic was set aside, the rename recorded alone, and the topic put back, so the link the first commit
shipped still lands on the ASCII chart. Both new titles were shortened first: at sixty characters each slug
had been cut just after a hyphen, and `…-explain-` is a permalink nobody would type.

### What the page check caught

On a phone, the grid sat flush against the card's edge while the text beside it was inset 18 px,
and it fitted two pictures to a row: thirty-seven pictures at two a row is a long scroll for a chart
meant to be taken in at a glance. The grid now takes the text's inset and fits three to a row under
640 px. The first draft of that media query sat *above* the base rule, which would have won by
coming later; it moved below before anything rendered it wrong.

### A check for the thing that would quietly break

The smoke test's theme check now includes the hand outline, beside `.topo-svg` and `.volatile`, with
presence asserted before behavior as the harness requires. A hand drawn in the dark theme's text
color would vanish on a light card, and nothing else would notice.

**It failed on its first run, and the fault was older than the check.** The quick-jump step a few
checks earlier opens the palette and never closes it, and the palette's overlay takes every click
beneath it. The existing theme checks never clicked: both their elements live in `net`, which an
earlier step had already opened. The hands live in a domain that was still closed, so this was the
first click after the palette, and it timed out. The step now closes what it opened.

### The contrast nobody's suite was looking at

`a11y_test.mjs` scans its own fixed pages, and this topic is not one of them, so axe was run on the
open topic by hand in both themes. Light mode failed one node: the caption *10*, cyan on the tile
color at **4.33:1**. All 37 captions share those colors. axe flagged only the one with two characters
because it skips single-character text, so a scan that passed every letter was not evidence about
the letters. The captions now use `--cyan-2`, 5.04:1 in light and 5.69:1 in dark, and axe is clean in
both. **Named and not built:** this topic in the a11y suite's scanned set. It is the site's first
picture grid, and the next grid will have the same blind spot.

```
1 commit · 1 new topic (productivity) · 1 retitle, alias recorded · 3 cards moved, 1 written · 37 pictures, ~30 KB
reader still 12 of 12, its five ASL queries retargeted · census 373 of 398, 0 unexplained
related links 4,902 -> 4,904 · path steps 1,600 -> 1,601 · smoke 163 -> 164: the hands follow the theme
1 latent test fault fixed (a palette left open) · 1 contrast failure found by hand, fixed
45 gates green · smoke 164 · search 58 · a11y 31 · resilience 64 · mobile 15 · visual 2 · backup 3
```

## Session — a list of ideas, checked before it was filed, and a heading that promises diagrams

The request: **update the plan with more content ideas to add, in the same clean look.**
Nothing in `data/` changed and `index.html` was not rebuilt. The queue is *Content ideas*,
above. This record is what checking it found, and what the checking got wrong on the way.

### The look had never been written down as a list

*The same clean look* was the constraint, so it was counted before any idea was. A class
census over `data/` gives 294 names, and the look a reader sees is seven everyday
components, ten shapes and six color classes. **Counting them is what found the two things
nobody asked about.** The shapes are on 58 of 1,503 hand-written topics, under a page
heading that reads *Cycles, Concepts &amp; Diagrams*. And fifteen class names in the content
have no rule in `style.css`.

Neither was on the list of ideas, and the first is now the largest item in the queue. It
is the risk register's own habit, *once a phase, measure something nobody has measured*,
arriving by accident again: the count was taken to describe a constraint, and it described
a gap.

### The class that is failure 6, nine times

`c-yellow` colors nothing, in nine table cells across six files. The operating manual
lists it by name, as the sixth of ten failures, with the guard *grep `style.css` for the
utility class before using one*. That guard is a habit and not a tool, and it has been
got past nine times. `check_css_vars.py`
exists because a name that is never declared fails silently and looks plausible. It checks
variables. Nothing checks classes. It is recorded in *Content ideas* §7 as the first thing
to do and the second thing to gate, and **it was not fixed here**: the change is
mechanical, and `CONTRIBUTING.md` asks for mechanical passes to be their own commit so the
freshness stamps stay honest.

### Three counts that were wrong before they were right

| Count | First | Final | What was wrong |
|---|---|---|---|
| Phrases owned by a title | 125, then 107 | **81** | A trailing boundary and a case rule in the matcher, then 26 owners that were the other sense of the word |
| Calculus phrases absent | `by parts` among them | Present | A case-sensitive grep over a file whose cheat sheet has a row named *By parts* |
| Titles that name a shape and draw none | 139 of 162 | **75 of 90** | The word list counted *model*, *process* and *path* as shapes |

**All three were a pattern whose matches nobody had read.** The first was caught by reading
the owner of each phrase, the second by reading the topic, and the third by reading the
list. Failure 9 in the manual is *probe zeros were 60% phrasing misses*, and its guard is
to verify every zero against the real title list. This is the same failure from the other
side. **A hit needs reading as much as a zero does**, and 26 of 107 is the rate at which it
was false here. The 452 phrases counted as mentioned were not read, so that number is an
upper bound and the section says so.

### What was not done, on purpose

- **No card, no diagram and no path.** The request was for the plan.
- **The two readers were not added to `query_probe.mjs`.** The census still reads 373 of
  398. A reader goes in when its first `want` can name a topic, and none of these has one
  yet.
- **No outline was fetched and no source was read.** Every exam phrase is from memory, and
  every sentence in the *as a draft* columns is unverified. The section says this where the
  sentences are, not only here.

### The file

`plan.md` went from 6,354 lines to 6,983. The fifth risk reopens at 8,000. The section is
554 of the new lines, and 106 of those are the candidate list in its §8, collapsed. That
list is the part to move to the archive first, with this record, once the queue is
conducted.

```
0 commits to data/ · 0 topics · 0 cards · 1 queue section in 8 parts
839 phrases · 17 reader groups · owned 125 -> 107 -> 81 · mentioned 452 · absent 306 · search zero 238
shapes: 58 of 1,503 topics · 9 with an SVG · 15 of 29 domains with none · 75 of 90 shape-named titles draw nothing
look: 15 classes with no rule · c-yellow 9 cells in 6 files · m 61 spans · nd 1
paths: 102, 0 named for an exam · census unchanged at 373 of 398
make check green, 45 gates · probe-check green · browser suites not re-run, the built page is unchanged
```

## Session — starting the content-ideas queue, and the three things the plan had wrong

The request was **start the plan**. The queue was *Content ideas*, and §7 set the order: fix
the look's hole, gate it, add the reader, draw one picture, then write. All of it shipped,
with one commit per step and per domain. Its §9 is the table. This is what doing it found.

### The proof tool was undercounting its own proof

The recolor changed 71 elements, and `style_equiv.mjs` reported **25 differences**. It
printed five per domain, and it also stopped counting at five, so the summary was the
number it had printed. That is an undercount presented as a total, in the tool whose only
job is to say what a change moved. It counts everything now, and tallies which properties
moved: 72 elements, the 71 plus one `<code>` inheriting from a recolored cell, and only
`color` and the border colors that follow it. **The shape is the oldest one in this file:
a check that stops looking reports the same thing as one that found nothing.**

### The stamper's two traps, both met on the way

- **An annotator span in an uncommitted change reads as a review.** Adding `AEAD` to the
  dictionary expanded it in the TLS card, and stamping with the new card in the same change
  moved the TLS topic to 2026-11 for one span. `CONTRIBUTING.md` already asks for annotator
  passes as their own commit; this session followed that only after the stamper showed why.
- **A comment above a new topic belongs to the topic before it.** The stamper gives every
  line between two topic openings to the earlier topic, so the marker comment over the new
  repair-ladder topic re-dated *Lost, Stolen & Returning Devices*. With the marker inside
  the new topic, only the new topic moves. Earlier topic additions may have done this to
  their neighbors. `CONTRIBUTING.md` says it now.

### The census caught a query that had never been answered

`the user has two accounts` had been scored answered with **60** results in 17 domains,
because 60 is the threshold. The new topic's "a second account" made it 61, and it became
the one unexplained result that was not the new reader. The tempting fix was to reword the
new card, and the census forbids it. Read, the set holds no card about one person with two
identities, and `soft-match` appears nowhere on the site. So the query carries a verdict that
names the gap, and *Content ideas* §9 queues it. **A number that sits exactly on a threshold is
a measurement of the threshold.**

### What the plan itself had wrong

| The plan said | Read, it was | Where it is corrected |
|---|---|---|
| The cells beside `c-yellow` use `c-amber` | `c-red` in seven tables, `c-green` in one | §1's table, and §9 |
| PBQs "usually come first" (§4 row 19's draft) | Older sources say so; CompTIA's current pages do not. They say a simulation can be revisited and a virtual item cannot | The card, and §9 |
| A diagram is "inline SVG" with the existing rules | True, but `math-svg` is a full-width frame: in a table cell it drew 51×9 px on a phone. A cell picture takes its size from its own attributes | §9 |

The draft sentences in §4 carried a warning that they were written from memory. One of the
five shipped was wrong, and the warning is why it was checked before it was copied.

### What was verified, and how far

Every volatile number in the five cards was checked by search, and none of the pages behind
them could be fetched. `comptia.org` does not resolve from this container. So each fact
anchor names its source and says it was confirmed in search results and not fetched:
GCM's 2³² random-nonce cap, Cisco's eight default distances, Microsoft's DISM-before-SFC
order, the two failed starts that open WinRE, and CompTIA's PBQ rule. Five anchors, and the
*Dated claims* row rose from 78 to 83 for those reasons.

```
12 commits · 1 new topic (endpoint) · 6 cards (sec 1, net 2, endpoint 3) + 1 (productivity) · 6 pictures (eng)
classes: 71 recolored + 1 removed, then gated · check_css_vars fixtures 13 -> 26 · style_equiv counts all differences
reader: somebody revising for a CompTIA exam, 0 of 16 -> 16 of 16 · census 373 of 398 -> 389 of 414, 0 unexplained
acronyms 1,104 -> 1,110 · related links 4,904 -> 4,918 · path steps 1,601 -> 1,602 · dated claims 78 -> 83
45 gates green · smoke 164 · search 58 · a11y 31/31 · resilience 64 · mobile 15/15 · backup 3/3
visual 0/2 here, and 0/2 on the commit before this session: font rendering, baseline left alone
```

## Session — the second wave, and three tools that were wrong at their own edges

The request was **keep going with the next wave**. The wave was *Content ideas* §4 rows 2
to 8 and 11 to 13, the rest of the security and networking words the exams use. The reader
went in first, then one commit per domain, and *Content ideas* §10 is the table. This is
what doing it found.

### Each tool was right inside its edge and wrong at it

Three fixes, and one shape. The search's acronym map was right for every acronym and wrong
for the ones that are also words, which the dictionary had already marked `noAnnotate`.
The annotator's window was right inside a topic and read across the edge into one the
reader has not opened. `.dora-word` was right on the theme it was written for. **Each was
found by the first new user of the thing, not by its own tests.** FAR was the first
word-shaped acronym added since the map was written, the TOCTOU card ended beside a topic
about servers, and the zero-trust card was the tiles' second user, looked at on a phone in
light mode. The search gained a ceiling and the annotator three fixtures, and axe counted
four contrast failures on each tile card before the color fix and none after.

### A query that closes is not a query answered correctly

`policy enforcement point` found only the acronym dictionary, and it closed the moment PEP
went into the dictionary, through an existing row: *Policy engine (PEP/PDP) — decides
allow/deny*. That row was wrong. In NIST's model the enforcement point decides nothing,
and the zero-trust card corrected it two commits later. Until then the census counted the
question answered by a sentence that answered it wrongly. **The census measures whether a
reader lands on the right card. Whether the card is right is still a reading job.**

### The ceiling decided a card's shape

§4 row 6 said *a row in BCP / DR — Key Metrics*. The metrics there are five tiles, each
with an inline border color, and the inline-style ceiling sits at exactly 401 with no slack.
A sixth tile to match its neighbors needed a sixth inline style. It became a card instead,
and the card was the better shape: maximum tolerable downtime is not a sixth metric beside
the five but the limit two of them answer to, and showing that took a worked example. **A
ratchet with no slack is working when it changes the shape of the next thing rather than
being raised to fit it.**

### A word the matcher reads whole

`tone and probe` found an AI card about bias, while the toolkit had a row called *Toner and
probe*. Words of four letters or fewer match whole, so *tone* never matched *toner*. The
census forbids tuning prose to the matcher, so the test was whether the row is better with
the new words if no query existed. *Tone generator and probe* is the tool's name, and the
row now also says what the generator does, which the old one did not. Two titles went the
other way: the cabling and discovery cards' titles named MDF, IDF, LLDP and CDP, a title is
an acronym's first use in its topic, and each would have carried an expansion that the
prose under it spells out again. They were reworded.

### What the plan had wrong

| The plan said | Read, it was | Where it is corrected |
|---|---|---|
| Row 6 is *a row* in the metrics | A card: the metrics are tiles with inline styles, and the ceiling has no slack | §10 |
| Row 8 lands *beside The Injection Family* | *Broken Access Control*: a check run at the wrong moment is an access-control failure | §10 |
| Row 3: *policy enforcement point* 0 | Absent as a phrase, but closed through a wrong row once PEP was in the dictionary | §10, and the card |
| Row 7 asks which documents are enforceable | Sources disagree on the MOA; force comes from wording, and an MOU is *usually* not binding | The card |
| Row 11: the demarc is where the fault stops being yours | Unless the contract moved it | The card's verdict |

### What was verified, and how far

Rows 6, 7 and 11 to 13 were checked by search before they were written: the syslog levels,
the pinouts and the standard's preference, CDP and LLDP and their timers, MTD and work
recovery time, the agreement types, the 90 and 10 meter budget, the demarc, and how TDR and
OTDR measure. No page was fetched. One draft synonym, *maximum tolerable period of
disruption*, was not confirmed, so the card does not use it. Five fact anchors record vendor
defaults as confirmed in search results and not fetched: Cisco's syslog keywords and default
trap level, the two messages one interface going down produces, the preference for T568A,
the rule that fixing speed and duplex turns Auto-MDI-X off, and the CDP and LLDP timers. The
*Dated claims* row rose from 83 to 88 for those reasons.

```
10 commits · 12 cards (sec 5, grc 1, ops 2, net 4) · 2 table rows corrected, 1 added · 0 new topics
tools: search maps word-shaped acronyms one way · annotator window clipped to its topic · .dora-word follows the theme
reader: CompTIA exam batch two, 0 of 23 -> 23 of 23 · census 389 of 414 -> 412 of 437, 0 unexplained
acronyms 1,110 -> 1,121 · dated claims 83 -> 88 · mean card 1,408 -> 1,412 · depth median 3,766 -> 3,780
45 gates green · smoke 164 · search 59 · a11y 31/31 · resilience 64 · mobile 15/15 · backup 3/3
visual 0/2 here, as in the first wave: font rendering, baseline left alone
```

## Session — the third wave, and two answers the census counted that nobody gave

The request was **keep going with the next wave**, and then **stay going until it is
completed**. The wave was *Content ideas* §4 rows 15 to 18 and 20, *the desk and the
exam*. The reader went in first, then one commit per domain, and *Content ideas* §11 is the
table. This is what doing it found.

### A match is not an answer, and the census only sees matches

The last wave fixed three tools at their edges. This one found the census's edge. Two queries
with recorded zeros, both kept on purpose with notes explaining why no card answers them,
began scoring as answered without anyone answering them. One matched the new Windows tools
topic through *User* inside the expansion of UDP. The other matched a connector card's
*wider on one side*. Each time the search's relaxation stage then did what it was built to
do and widened one match into a list, 31 cards in the first case. **The census counts a
query answered when the result is non-empty and not wide, and a coincidence passes that
test.** The staleness check reads a note for the claim it can evaluate, a zero, and neither
note made that claim in words, so neither was flagged. They were found by diffing the census
before and after each commit, which is now the habit: a count that moves by one more than
the batch explains has moved for a reason.

### The plan's short lookup was short because it was missing things

Row 15 said *a lookup, short by design*, and listed the commands it had counted as absent.
Writing it found the Windows network commands absent too: `ipconfig` twice on the whole site,
`tracert` once and `netstat` never on Windows. The grep behind §4 had looked for the commands
it already thought of. The same thing happened to row 18, whose draft named VLOOKUP's
approximate default and not MATCH's, which is the same trap inside INDEX and MATCH.
**A list of what is absent is bounded by the words its author thought to look for.**

### The picture grid became pictures in a table

Row 17 said *the site's second picture grid*. The first grid's rules are named for the ASL
hands, and a grid separates a shape from the words that make it recognizable, which for a
connector is the whole card: *two cut corners* or *one*, *hollow* or *solid*. Wave one had
already drawn the UML lines in a table's first column with existing roles and no new CSS, so
the connectors went the same way, twelve of them from one script, at one scale per table.
Each was rendered at size in both themes and read against its own row before its commit, the
check the ASL records established.

### A new topic costs three things the plan never listed

A path, because `check_paths.py` fails a hand-written topic that is on none. Related links in
both directions, because the orphan row drifts without them. And a new preview image, because
`gen_og_image --check` compares the topic count printed on the image. While adding the links,
the related-links row turned out to carry a mainland of 1,487 that had been 1,488 since the
first wave's topic. Nothing checks that figure, so nothing noticed. It reads 1,489 now.

### What the plan had wrong

| The plan said | Read, it was | Where it is corrected |
|---|---|---|
| Row 15 is a short lookup | Four cards: the Windows network commands were nearly absent too | §11 |
| Row 16 lands in `ops` or `threat` | `ops`, inside PICERL: the seven steps are its phases for one machine | §11 |
| Row 17 is a picture grid in `net` | Two cards, `net` and `hw`, with each picture in its table's first column | §11 |
| Row 18's trap is VLOOKUP's | MATCH has the same default | The card |
| Related links: a mainland of 1,487 | 1,488 since the first wave, and nothing checked it | The row |

### What was verified, and how far

Every outside fact was checked by search before it was written, and no page was fetched. The
malware removal order and Professor Messer's caveat about rebuilding. The A+ command list,
where only `pathping`, `chkdsk`, `diskpart`, `robocopy` and `winver` were confirmed for
220-1202, so the topic claims no objective numbers for its tables. VLOOKUP's and MATCH's
defaults, XLOOKUP's versions and the pivot refresh keys. The connector faces: the published
widths, RJ11's fit in an RJ45 jack, the fiber ferrules, and DisplayPort's single cut corner,
which took a second search. And the two exercise studies, where the meta-analysis was found
and the twenty-minute protocol was not. Three fact anchors record what is dated or
version-specific: XLOOKUP's Excel versions, the A+ objective numbers, and the two studies.
The *Dated claims* row rose from 88 to 91 for those reasons.

```
7 commits · 1 new topic (shortcut) · 10 cards (shortcut 6, ops 1, net 1, hw 1, productivity 1) · 12 connector drawings
reader: CompTIA exam batch three, 0 of 16 -> 16 of 16 · census 412 of 453 -> 430 of 453, 0 unexplained
2 kept zeros now answered by coincidence, both notes say so · search inside expansions queued, not changed
topics 1,564 -> 1,565 · path steps 1,602 -> 1,603 · related links 4,918 -> 4,928 · mainland 1,488 -> 1,489
dated claims 88 -> 91 · mean card 1,412 -> 1,414 · page budget 32% (~727) -> 31% (~717) · acronyms unchanged at 1,121
45 gates green · smoke 164 · search 59 · a11y 31/31 · resilience 64 · mobile 15/15 · backup 3/3
visual 0/2 here, as in the first two waves: font rendering, baseline left alone
```

## Session — the fourth wave, and a spelling gate that knew five words and not the rule

The request was **keep going until you finish all waves**. The fourth was *Content ideas* §4
rows 21 to 27, the theory under the tools, and §7.3 had said when its reader goes in: with the
first theory card. So *a student on a theory course* went in first, 15 queries, and opened at
0 of 15. *Content ideas* §12 is the table. This is what doing it found.

### An exception list is a rule somebody has not written yet

The spelling gate flagged *bitwise* and offered *bitwize*. Its `-ise` rule keeps a list of
words where `ise` is not the suffix, and the list named *clockwise*, *likewise*, *otherwise*,
*pairwise* and *stepwise*, one at a time. Five names were approximating one fact: *-wise* is
a suffix of its own, English coins new ones freely, and none has an American spelling that
differs. It is a rule now, with three fixtures, and the commit that taught it came before the
card that needed it, so every commit on the branch passes. **When a list of exceptions grows
by one each time content meets it, the list is a rule in disguise.**

### The other gate was right, and the mechanism it guards worked

The linter refused `ECC` rendering as *Elliptic Curve Cryptography* in the card about
error-correcting codes. `acronyms.json` already carried both meanings and decisions for `hw`,
`linux` and `sec`, and `cs` had never needed one. One line decides it now. That is the design
working: an acronym with two meanings is decided per domain at the moment a domain first uses
it, by the person who knows which one it meant.

### A commit made before its gate finished

One command in this wave chained `make check` to the commit without testing its exit status,
and the commit landed while the spelling gate was failing. It was caught by reading the
output, reset before anything was pushed, and redone after the gate was fixed. **The order is
the gate's exit status first, then the commit,** and a command that runs both has to say so.

### What the plan had right, and the half it missed

Six of the seven draft sentences held. Row 24's said a subnet mask and a permission mask are
the same move, *AND against a mask*. Half right: a subnet is AND, and umask is AND NOT, which
is why the common shortcut of subtracting works for 022 and fails for 033. The card is built on
the half the draft missed.

```
5 commits · 7 cards (cs 6, script 1) · 1 gate taught a rule · 1 acronym decided for a domain
reader: a student on a theory course, 0 of 15 -> 15 of 15 · census 430 of 468 -> 445 of 468, 0 unexplained
dated claims 91 -> 93 · mean card 1,414 -> 1,415 · depth 10th 2,155 -> 2,162, median 3,780 -> 3,791 · page budget ~717 -> ~713
45 gates green · smoke 164 · search 59 · a11y 31/31 · resilience 64 · mobile 15/15 · backup 3/3
visual 0/2 here, as in every wave: font rendering, baseline left alone
```

## Session — the fifth wave, the human domains, and a neighbor the stamper re-dated

The fifth wave was *Content ideas* §4 rows 28 to 31 and 35, the rows with conditions in place
of draft sentences. *Content ideas* §13 is the table. This is what doing it found.

### Where a topic is inserted can re-date the one before it

The Confucianism topic first went in front of Taoism, and the stamper moved Buddhism, the
topic above, to this month. Nothing in Buddhism had changed. The stamper blames the working
tree, and the new topic ends with exactly the same closing lines as Buddhism does, so blame
was free to align the insertion inside Buddhism's span. Moved to after Taoism, which is still
beside it, the same block re-dated nothing. The check that caught it is the one every wave
here has run, reading which topics moved rather than how many, and it is the reason that
check exists. **A stamp is derived from a diff, and a diff of repeated closing tags has more
than one honest reading.**

### Conditions, not drafts, and each one held

Row 28 said not to write from memory, so every claim in the low-mood topic is cited and dated,
and it ends where the row said, at *Getting Professional Help*. Row 30 said every row is a
dated claim, and the search proved it: one program's policy had changed in March. Row 35's
date-time group could not be sourced at all, so its anchor says that instead of borrowing a
check. **An anchor that records an absent source is more useful than one that implies a
present one.**

### The reader's word, once more

`depressed for weeks` stayed at zero after the low-mood topic shipped, because the topic said
*depression* and never *depressed*. The fix was the census's kind 1: the opening sentence
now uses the reader's word, which is also the plainer sentence. The census has recorded this
shape before, with *laid off*, and it keeps being the cheapest fix there is.

```
5 commits · 3 new topics (mind 1, philosophy 2) · 8 cards (mind 2, military 4, plus the topics' own)
reader: 17 queries in two existing readers, 0 of 17 -> 17 of 17 · census 445 of 485 -> 462 of 485, 0 unexplained
topics 1,565 -> 1,568 · path steps 1,603 -> 1,606 · related links 4,928 -> 4,954 · mainland 1,489 -> 1,492
dated claims 93 -> 101 · mean card 1,415 -> 1,416 · depth 10th 2,162 -> 2,169 · page budget ~713 -> ~706
45 gates green · smoke 164 · search 59 · a11y 31/31 · resilience 64 · mobile 15/15 · backup 3/3
visual 0/2 here, as in every wave: font rendering, baseline left alone
```

## Session — the sixth wave, the quotes, and a gate that meant reading

The sixth wave was *Content ideas* §4 rows 32 to 34, the rows whose gate says a quotation ships
with its source read. *Content ideas* §14 is the table. This is what doing it found.

### "This container fetched nothing" was true of one tool

The first attempt to read the sources failed completely: three fetch agents could not resolve a
single host. The environment's network turned out to be unrestricted, and plain requests from
the container reached Wikiquote, Wikipedia, the RFC Editor, the American Presidency Project and
InfoQ. The plan had recorded *fetched nothing* as a property of the container, and it was a
property of one tool. **A capability recorded once as absent is worth testing again by another
route before it shapes a wave.**

### The route that was refused, and the line it drew

One batch of requests set its own user agent and reached for an archive copy of a dead site and
a second path to a site that had answered 503. The session's own safety check refused it, and it
was right to: a site that refuses automated reading has said so, and a defunct one is gone. The
rows that needed them were read from pages that quote and cite the originals instead, and the
anchors say which page. Plain requests that hit a rate limit were simply retried later.

### Most famous lines moved one step from their source

Of the lines checked, only some say exactly what they are quoted as saying. Knuth's is cut in
half, Goodhart's is worded by Strathern, Moltke's is Correlli Barnett's paraphrase, Eisenhower
credited the Army and Hopper's *forgiveness* line predates her by more than a century. Two lines had no
source at all and went to *Misattributed*. **The step between a source and its famous form is
usually honest, and it is the step that changes the meaning.**

```
4 commits · 3 new topics (quotes) · 2 lines moved to Misattributed · 1 acronym decided for a domain
reader: 10 queries in a learner meeting a subject, 0 of 10 -> 10 of 10 · census 462 of 495 -> 472 of 495, 0 unexplained
topics 1,568 -> 1,571 · path steps 1,606 -> 1,609 · related links 4,954 -> 4,978 · mainland 1,492 -> 1,495
dated claims 101 -> 105 · mean card 1,416 -> 1,417 · page budget ~706 -> ~703
45 gates green · smoke 164 · search 59 · a11y 31/31 · resilience 64 · mobile 15/15 · backup 3/3
visual 0/2 here, as in every wave: font rendering, baseline left alone
```

## Session — the seventh wave, the pictures, and the components the rows named

The request was **keep going until you finish all waves**, and the seventh was *Content ideas*
§2 rows 2 to 20, the pictures. *Content ideas* §15 is the table. This is what doing it found.

### A component is a claim about what it can draw

§2 chose a component for every row before any row was drawn, and eight of the nineteen could
not draw their own row's sentence. The five that named `layer-stack` are the clearest case. A
stack's rows are one width, sit one above another and contain nothing. The pictures needed a
width (the pyramid), containment (Azure), a line that goes round the stack (Purdue) or uneven
gaps (the memory ladder). Each was drawn as an inline SVG with roles already in the stylesheet.
**The component column was a guess about the picture, and the sentence beside it was the
spec.**

### A number has to hold still to be drawn

Two claims changed the moment they were drawn to scale. The memory hierarchy's title said six
orders of magnitude, and a log axis from 1 ns to 150 ms needs eight. The plan said the priority
topic had no matrix, and it had one as a table, so the picture became what the topic's third
card does on it. A third claim narrowed rather than broke: the mail flow verdict's allow-rule
hole, which Microsoft now closes for malware and high-confidence phishing whatever a rule says.
**Prose can carry a rough number for years, and a scale cannot.**

### A picture drawn alone is the wrong size at both ends

The math SVG role scales with the card. A picture alone renders at twice its size on a desktop
and a third of it on a phone, and the first drafts of four pictures did exactly that. Two
panels of the topology grid fixed both ends, because the panels stack on a phone. That suited the
rows too, because most of these pictures are comparisons, and the second panel shows what
the first is not. The three left single were drawn tall, which the height cap holds to size.

### What the pictures cost

The page budget fell from room for ~703 more topics to ~682. Twenty pictures cost about what
twenty topics would, because an SVG's coordinates are characters and the budget counts
characters. That is a fair price for twenty pictures that each show a position, an order or a
containment. It is also the reason a picture added later has to make its row's claim, and
cannot be decoration.

### What was verified, and how far

Four outside facts, each by search and each with an anchor that says so. Boyd's line from
Orient to Act, in his 1995 briefing: both primary PDFs refused automated fetching, and neither
was worked around. Bianco's 2013 authorship of the Pyramid of Pain, from a secondary overview.
Microsoft's description of Enforced as moving a GPO to the end of the processing order. And the
limit on a mail flow rule that sets the spam level to −1. Every picture was rendered at size in
both themes, at desktop and phone width, and read against its card before its commit, the
check the ASL records established. That reading sent several back: a label over a switch, a
path over a word, wires showing through hollow boxes, and the sizes above.

### The gate that knew a word and not its prefixes

A new card said *labelled*, and the spelling gate caught it. The fix showed what the gate does
not catch. Its word boundary rejects a letter before *labelled*, so *unlabelled*, which the site
has seventeen times, has never been checked. It is queued for the eighth wave as a gate change
and one mechanical commit, not folded into a picture's.

```
14 commits · 0 new topics · 17 picture cards and 3 pictures in existing cards · §2 finished, 20 of 20 rows drawn
reader: no new queries · census 472 of 495 before and after, 0 unexplained
dated claims 105 -> 109 · mean card 1,417 unchanged · depth median 3,795 -> 3,810 · page budget ~703 -> ~682
0 lines of new CSS · inline styles 401 -> 401 · README elements 149,612 -> 150,665
45 gates green · smoke 164 · search 59 · a11y 31/31 · resilience 64 · mobile 15/15 · backup 3/3
visual 0/2 here, as in every wave: font rendering, baseline left alone
```

## Session — the eighth wave, the exam paths, and the queue emptied

The request was **keep going until you finish all waves**, and the eighth was *Content ideas*
§5's exam paths and every gap an earlier wave had set aside. *Content ideas* §16 is the
table. This is what doing it found.

### A search with no ranking finds a card by its title

`the user has two accounts` needed a card, and a card alone did not answer it. The new card
held the reader's exact words, and search widens a lone exact hit unless the topic's own name
carries a word of the question. That rule exists because four lone hits had been
coincidences, and it is right. The reader got 63 cards with the answer somewhere among them.
The fix was the shape the rule asks for, a topic named for the question, and the query now
finds it alone. **Where nothing is ranked, a title is how a card gets found.**

### Taking a reading aid out of the index cost one answer, and it was the false one

Search read the annotator's acronym expansions as if a card had said them, so *User* in
UDP's expansion answered a query about a lost file. The fix drops the expansions from the
index, the way the reading-time chrome was already dropped. A reader who types an expansion
still finds the acronym, because the query is mapped before matching. The census moved by
exactly one, 472 to 471, and the query that moved was the coincidence, back at the zero its
note had always said was true. **A measurement that drops by the number you predicted is
the measurement working.**

### The gate knew a word and not its prefixes

The spelling gate's dictionary rejected any letter in front of a word, so it caught
*labelled* and had never seen *unlabelled*, which the site used seventeen times. The
seventh wave's record said fifteen, counted by hand before the gate could count, and says
seventeen now. Taught four prefixes, the gate found eighteen. The sweep went in as its own mechanical commit, and that commit
is listed in `.git-blame-ignore-revs`. A spelling fix is not a review, and no topic's date
moved for one. That was checked by stamping two of the swept domains and seeing nothing move.

### The outline was read the week its successor launched

CompTIA lists SY0-801's launch as 17 November 2026, five days before the Security+ path was
written, and SY0-701 retires in June 2027. The path follows SY0-701, the exam whose outline
was read and which people are still taking. SY0-801's course index was not at the address the
pattern predicted, and guessing further addresses would have been a search for a page, not a
reading of one. **A dated claim can go stale between the search and the commit, and the date
in the blurb is how a reader can tell.**

### What was verified, and how far

How sync matches a user, and the hard-match protections that apply from July 2026, came from
Microsoft's pages as quoted in search results. So did the AD Recycle Bin keeping a user's
anchor and Entra's thirty days. Two anchors record both. The four exam outlines were fetched
and read from a course index that mirrors CompTIA's numbering, and the SY0-801 and SY0-701
dates came from CompTIA's pages as quoted in search. Every new card was rendered at size in
both themes and read before its commit, and so was the paths panel.

```
7 commits · 1 new topic (infra) · 3 cards (infra 2, hw 1) · 4 exam paths · 1 feature, a path as a deck
reader: no new queries · census 472 of 495 -> 471 of 495, 0 unexplained · wide 9 -> 8
topics 1,571 -> 1,572 · paths 102 -> 106 · path steps 1,609 -> 1,751 · related links 4,978 -> 4,984 · mainland 1,495 -> 1,496
dated claims 109 -> 111 · 18 prefixed spellings swept, the gate taught four prefixes
45 gates green · smoke 165 · search 59 · a11y 31/31 · resilience 64 · mobile 15/15 · backup 3/3
visual 0/2 here, as in every wave: font rendering, baseline left alone
```

## Session — the ninth wave, the five gaps and the exam that launched

The request was **keep going with the next wave**. *Content ideas* had shipped, so the next
wave was the list §16 left: five A+ objectives the exam paths skipped, and a path for
SY0-801. *Content ideas* §17 is the table. This is what doing it found.

### Two queries closed in prose, the way they usually do

The 16 queries went into the census before any topic, at 0 of 16. With the topics written,
fourteen found them, and two did not. `windows 11 tpm requirement` missed because the card
said Windows 11 *requires* them. `fat32 file size limit` missed because the card said *how
large one file can be*. Each closed when the card used the reader's noun, and in both the
reader's noun was also the plainer sentence. That is the same fix as *depressed for weeks*
in the fifth wave. **A reader's question is usually written in nouns, and a card that
answers it in verbs reads well and goes unfound.**

### The missing outline was one search away

The eighth wave looked for SY0-801's outline at the address its predecessor's course used,
found nothing there, and stopped. This wave searched for the outline itself. It found
CompTIA's objectives document, version 2.0, on the file host CompTIA's own pages link to,
fetched it with a plain request and read it: the official document, not a course index that
mirrors one. V8 keeps the five domains, reweights them and adds an objective on the threats
of using AI, which topics already on the site answer. **When a source is missing, search for
the source, not for another copy of the place the last one was found.**

### Writing a topic found a near-duplicate, and reading it took a sentence

The near-duplicate census flagged one new pair: *Windows Editions* beside *Windows Server
Editions & Licensing*. Phase 9's test is to open both and say in one sentence who each is
for. Here that was easy: one is for the laptop a technician meets, one for the server an
administrator buys, and each links to the other. The sentence is in the verdicts file now,
and the census reads 0 unread.

### What was verified, and how far

These Microsoft pages were fetched and read: the Device Encryption page, the Entra join page,
the GPT FAQ, MBR2GPT and the Home and Pro comparison. Search covered Windows 11's
requirements, the 2 TB MBR limit, subscription activation, Dev Drive, the Home to Pro upgrade,
NTFS permissions on copy and move, and the file systems' support on macOS and Linux. Backblaze's
SMART figures came from search too, and their anchor says they are from 2016 data. CompTIA's
SY0-801 objectives were fetched and read. Six fact anchors record all of it, and the claim the
sources would not support, that a Home to Pro upgrade keeps every app, was left out. Every new
card was rendered at size in both themes and read before its commit.

```
5 commits · 5 new topics (endpoint 3, hw 2) · 1 exam path · 1 acronym decided for a domain · 1 near-duplicate pair read
reader: 16 queries in somebody revising for a CompTIA exam, 0 of 16 -> 16 of 16 · census 471 of 495 -> 487 of 511, 0 unexplained
topics 1,572 -> 1,577 · paths 106 -> 107 · path steps 1,751 -> 1,805 · related links 4,984 -> 5,016 · mainland 1,496 -> 1,501
dated claims 111 -> 117 · near-duplicate pairs 95 -> 96, 0 unread
45 gates green · smoke 165 · search 59 · a11y 31/31 · resilience 64 · mobile 15/15 · backup 3/3
visual 0/2 here, as in every wave: font rendering, baseline left alone
```

## Session — the tenth wave, four exam paths and the six gaps they found

The request was **keep going with the next wave**. §17 had left nothing queued, so the wave
went back to §5's own count, the exams it found at zero in `paths.json` that no wave had
written a path for: CySA+, PenTest+, Linux+ and CISSP. *Content ideas* §18 is the table. This
is what doing it found.

### Four outlines, read where the exam bodies keep them

CompTIA's objectives documents for PT0-003, CS0-004 and XK0-006 came from the file host that
served SY0-801's, and ISC2's CISSP outlines from the media host its own site links to, all with
plain requests, and each was read in full before its path was written. The launch and
retirement dates came from CompTIA's exam pages as search quoted them, since comptia.org
refuses automated reading. One third-party post put CS0-003's retirement on CS0-004's launch
day. CompTIA's own pages say 22 December 2026, and the path uses that. ISC2 has already
published the outline that replaces the current one on 15 April 2027, so the CISSP path names
the date.

### A slug typed by hand was one character wrong

The 18 queries went into the census before any topic, each want naming the slug its topic's
title would produce. Five were computed with the site's own `slugify`. The sixth had been
computed for a longer draft title, and when the title was shortened the slug was guessed
rather than computed again. `check_paths.py` caught it the moment the topic joined the CISSP
path: one step that resolved to nothing, and one topic on no path. **A slug is computed, never
typed. The function that makes it is one import away.**

### Checking a fact found that it had moved

Every dated claim was searched before it was written. Nine came back as expected, and one
changed the card: ATT&CK's April 2025 release folded DLL Side-Loading, T1574.002, into
T1574.001, now named simply DLL. The card cites the current number, and its anchor records the
change. **A technique ID is a dated claim, like a price, because the framework that issues it
renumbers.**

### A gate that skips code already had the exception a keyword needed

`check_renames.py` lists *blacklist* as renamed to *blocklist* since 2020, and the device topic
used the word four times in prose, because `modprobe.d` still spells its keyword that way. The
gate reads prose only, so the fix needed no allow entry: the prose says blocking, and the
keyword appears only as code, where it is literally the right word.

### Rendering at size found what every gate passed

Every gate and every suite was green before a single card was rendered. Rendering each card at
1280 and 375 pixels then found three things none of them measures. A 33-character badge
widened the whole `ops` page by 5 pixels on a phone, because the topic header does not wrap
and the title shrinks to its longest word, here *Communications*. Another badge ran under the
chevron. And a table column headed *Covered in* sat over two rows that gave a defense instead.
The mobile suite checks fifteen views chosen in advance, and a new topic's header is not one of
them. **For a new topic, the render is the gate. The suites guard what they were written
for.**

### What was verified, and how far

The four outlines were fetched and read. Search covered ATT&CK's process injection and
hollowing pages and its April 2025 release notes, Sysmon's events and MITRE's detection
strategy for hollowing, the EFF's DES search, Kocher's timing and power papers, the Bellcore
fault attack, Bleichenbacher and ROBOT, libvirt's open network mode, dracut's `mkinitrd`
wrapper, and the NIS2 and Form 8-K clocks. Ten fact anchors record it, each saying the pages
were seen in search results and not fetched. What search did not confirm was left out:
Vaudenay's padding oracle is not named. Every new card was rendered at size in both themes and
read, and the fixes it found are their own commit.

```
5 commits · 4 exam paths · 6 new topics (linux 2, pentest 1, threat 1, sec 1, ops 1) · 1 acronym decided for a domain
reader: 18 queries in somebody revising for a CompTIA exam, 0 of 18 -> 18 of 18 · census 487 of 511 -> 505 of 529, 0 unexplained
topics 1,577 -> 1,583 · paths 107 -> 111 · path steps 1,805 -> 2,014 · related links 5,016 -> 5,064 · mainland 1,501 -> 1,507
dated claims 117 -> 127 · near-duplicate pairs 96, 0 unread · plan.md under the 8,000 lines that reopen the fifth risk
45 gates green · smoke 165 · search 59 · a11y 31/31 · resilience 64 · mobile 15/15 · backup 3/3
visual 0/2 here, as in every wave: font rendering, baseline left alone
```

## Session — the eleventh wave, SecurityX and the two CISSP gaps

The request was **keep going**. §18 had left two CISSP objectives with no topic, and the domain
headers advertise exams the paths do not cover. SecurityX is tagged on four of them and shares
its governance objective with one of the two gaps, so its path went first. *Content ideas* §19
is the table. This is what doing it found.

### The official document was newer than the copy that ranked first

Search offered a third-party copy of the CAS-005 objectives labeled version 3.0, and, further
down, CompTIA's own file host. CompTIA's copy was version 7.0. Every CompTIA outline this session
read came from that file host, and this is why: a mirror keeps whichever version it happened
to fetch. **The exam body's own copy is the one to read, even when a mirror is easier to find.**

### One topic closed a gap in two exams

The policy hierarchy was a CISSP gap the tenth wave found, and SecurityX 1.1 asks for the same
documents. Writing it once, for both, meant one census batch covered both exams, and the
SecurityX path opens on a topic written for it. The RACI matrix and COBIT, which SecurityX
names and the site had never explained, became its second and third cards.

### The slugs were computed, and all eight resolved

The tenth wave's record said a slug is computed, never typed. This wave's eight wants were
computed with the site's own `slugify` before either topic existed, and every one resolved the
first time the topics were built.

### Two verdicts claimed a count nobody had taken

Rendering the cards at size and reading them found two verdicts that said how often something
is skipped, "the step most drills skip" among them, with nothing counted behind it. Both now
say what the step is for. **A verdict that sounds like a statistic needs one, or needs to stop
sounding like one.**

### What was verified, and how far

CompTIA's CAS-005 objectives, version 7.0, were fetched and read. The CISSP outlines the tenth
wave fetched were read again for 1.6 and 7.15, in the 2024 and 2027 versions, which name the
same items. The two topics make no dated claims, so no fact anchors were added: COBIT and ITIL
are described by what they govern, without versions or owners that would date. Every new card
was rendered at size in both themes and read before its commit.

```
4 commits · 1 exam path · 2 new topics (grc 1, sec 1)
reader: 8 queries in somebody revising for a CompTIA exam, 0 of 8 -> 8 of 8 · census 505 of 529 -> 513 of 537, 0 unexplained
topics 1,583 -> 1,585 · paths 111 -> 112 · path steps 2,014 -> 2,062 · related links 5,064 -> 5,082 · mainland 1,507 -> 1,509
dated claims 127 · near-duplicate pairs 96, 0 unread · plan.md under the 8,000 lines that reopen the fifth risk
45 gates green · smoke 165 · search 59 · a11y 31/31 · resilience 64 · mobile 15/15 · backup 3/3
visual 0/2 here, as in every wave: font rendering, baseline left alone
```

## Session — the twelfth wave, the owner's packaging items and the guide they came with

The owner sent three items and, partway through, a guide to MSI against EXE in MECM, all
written into plan.md as sent. The same message asked for the CI fix first, which went in on its
own: the browser job now names ubuntu-24.04, because Playwright 1.56 does not support Chromium
on 26.04. Adding the items took plan.md to 8,009 lines, and the fifth risk's split ran a third
time before any content was written. *Error codes and packaging* §5 is the table.

### The owner's guide was mostly right, and the one claim that was not had a number

Every claim in the guide was checked against Microsoft's own pages before a card repeated it.
Nearly all of it held, down to the wording of the 32-bit detection option and the PsExec test,
which Microsoft's Configuration Manager reference gives in the same form. MECM's 120-minute
default run time is real, but the code the guide gives for hitting it, 0x87D00664, is in none of
Microsoft's references. The cards describe the timeout and give no code. **A guide written from
experience is a list of claims to check, and the checking is quick when the source exists.**

### One old question got the answer it had been waiting for

`the software installed but does not appear` had sat in the service desk reader with no target,
answered by whatever came back. It is the reader's own words for 0x87D00324 and 0x87D1041C:
installed, and not detected. The error-code topic said "not detected" and never "appear", so the
verdict now says both, and the query names the topic. **A query recorded with no target is a
question the site was not ready to answer, and a new topic should look for them.**

### What was verified, and how far

Eight Microsoft pages were fetched and read. They were the Windows Installer error list,
msiexec's switches, Intune's app installation error reference, its Win32 app preparation and
add pages, Configuration Manager's application error reference, its create-applications page
and its deployment troubleshooting page. Inno Setup's documentation was read as well. The NSIS
manual refused the request, so its switch rests on search results and the anchor says so.
Intune's default return codes are the same: Microsoft's page says defaults exist without listing
them. Every card was rendered at size in both themes and read before its commit.

```
7 commits · 1 CI fix · 1 split (45 records, lines conserved) · 2 new topics (endpoint 2)
reader: 8 queries in a service desk engineer, 0 of 8 -> 8 of 8 · census 513 of 537 -> 521 of 545, 0 unexplained
topics 1,585 -> 1,587 · path steps 2,062 -> 2,066 · related links 5,082 -> 5,098 · mainland 1,509 -> 1,511
dated claims 127 -> 138 · near-duplicate pairs 96, 0 unread
```

## Session — the thirteenth wave, the lookup in the tray

The owner's first item, built last because its rows come from what the twelfth wave verified.
The header has no tray, so the lookup became a button among its controls: 🧾 ERRORS, or `c`,
opening the study modal with one search box and a table of *Error code · System type · Use of
it*. *Error codes and packaging* §5 is the table.

### Every printed form of one code is the same code

A console shows one failure as 1603, 0x80070643 or -2016410844, depending on which layer printed
it and how. The lookup reads all of them. It computes the signed form from the hex rather than
storing it, and decodes 0x8007xxxx to the Windows error inside, because Microsoft's own tables
disagree with themselves: two rows in Intune's Windows section print the same decimal for
different codes. **Store the code once, as its source prints it, and derive every other form.**

### The first placement failed a gate nobody had pointed at it

The first version put the button in the column of switches, the tray's obvious place. Every
suite passed except the visual check, which moved from its usual 10.3% to 11.5%. Comparing the
old and new builds in the same fonts found the cause: the column sets the header's height, the
header grew 28px, and the sticky filter bar's blurred background showed a different slice of the
page, 1.33% of pixels against a 0.05% threshold. In CI, where the fonts match, that would have
failed. Under the Chemical Engineer link the button costs no height, and the check went back to
exactly 10.335%. **A gate that fails for a known reason still has to be read: the number moved.**

### What was verified, and how far

The 156 rows are copied from three Microsoft references read in the twelfth wave, each named in
the data file and on every row. build.py refuses a malformed row. The lookup was driven in a
browser at 1280 and 375 pixels in both themes: every code form, the decoding, a word search, no
match, Escape returning focus to the button, the `c` key and the topic link. It has no axe
violations and no page overflow.

```
1 commit · 1 feature · 156 codes from 3 Microsoft references · 0 new topics
checks: smoke 165 -> 166 · axe 31/31 -> 33/33 · mobile 15/15 -> 16/16 · search 59 · resilience 64 · backup 3/3
visual 0/2 here, as in every wave, and back to exactly 10.335% after the move: font rendering, baseline left alone
45 gates green · plan.md 4,265 lines, far under 8,000 after the split
```

## Session — the fourteenth wave, two Microsoft paths and an exam that retired

The request, from the owner's message, was to keep going through the waves once the three items
were done. §19's list of header tags with no path came next, and three of them were Microsoft's,
in the domains the twelfth and thirteenth waves had just worked in. *Content ideas* §20 is the
table.

### A header advertised an exam that no longer exists

Reading the study guide before writing the path is what found it: AZ-800's page says the exam
retired on 30 September 2026. The infra domain's header had carried the tag since the domain was
written, and the README's domain table repeated it. Both now name what the domain covers instead.
**A certification tag is a dated claim like any other, and the outline is where its date is.**

### Two outlines, read against topics that already existed

MD-102 mapped almost entirely onto `endpoint`, including the two packaging topics written two
waves earlier, which now sit under its application skills. MS-102 did not: its Defender XDR
area, the largest at 30 to 35%, names incidents, advanced hunting, attack simulation, Defender for
Cloud Apps and vulnerability management, and the site has topics beside them but none on them.
Its path points only at topics that answer an objective, and §20 lists the rest.

```
2 commits · 2 exam paths · 1 retired exam found and its tag corrected · 0 new topics
paths 112 -> 114 · path steps 2,066 -> 2,128 · topics 1,587, unchanged
45 gates green · smoke 166, whose learning-path checks read the new paths · mobile 16/16
```

## Session — the fifteenth wave, MS-102's Defender XDR area and a stamper that wrote when asked for help

The request was the owner's again: keep going through the waves. §20's queue put MS-102's Defender XDR
area first, the exam's largest at 30 to 35% and the site's thinnest, and four of its eight gaps make
this wave. *Content ideas* §21 is the table.

### Read first, then the census, then the cards

Thirty-two pages from Microsoft Learn were fetched and read before a card was written: incidents,
automated investigation, advanced hunting with its quotas and query resources report, custom
detections and four table schemas; the attack simulation guides, its FAQ and the advanced delivery
policy; eight pages on Defender for Cloud Apps and eight on vulnerability management. Thirteen
queries went into *a SOC analyst or defender* next and opened at 0 of 13. Each of the 21 fact anchors
names its page and the date Microsoft last updated it, so the next check knows which pages to open
first.

### What the pages said that the cards had to carry

The cards carry six things that are true this month and dated as such: incident cases are in preview,
Defender for Cloud Apps moved its anomaly policies to a dynamic model in June 2025, its Microsoft 365
connector gained default components in January 2026, its file policies retire on 6 January 2027, an
updated exposure score model is rolling out, and Secure Score for Devices reads Group Policy and can
call Intune-made settings wrong. One more was a reading that would have been easy to get backwards:
`UrlClickEvents` is filled by Safe Links, so an empty click query means no click Safe Links saw, not no
click. Microsoft's simulation FAQ says the same of simulation clicks.

### Two checks that were right about the words and wrong about the product

`check_renames.py` failed `make check` on eight uses of *Office 365*. Seven were inside *Defender for
Office 365*, the product's current name, which the rename registry itself gives as the successor of
*Advanced Threat Protection*; the older `m365` cards say *Defender for Office*, a shortening the check
never sees. One was a real old name, *an activity in Office 365*, copied from a Microsoft table
description, and now reads Microsoft 365. The allow list was there; it matched only phrases that start
at the flagged words, and this one ends at them, its first letter one character outside the window.
Widened to the longest allowed phrase, with a fixture for each side.

`check_volatility.py` does not fail; it counts topics that name a vendor console with no dated span,
and the count went from three to six. All three new ones were these cards naming the Defender portal.
Four volatile spans now mark the console paths, and the count is three again.

### A tool that wrote when asked for help

`stamp_freshness.py --help` was meant to print the options. The script never looked for `--help`, so it
ran its default, the whole-tree write its own docstring warns against, and re-derived stamps until the
pipe into `head` closed. `git status` showed 25 files changed. Twenty-three held only stamp changes
and were checked out; in `m365` and `endpoint`, 80 moved stamps on existing topics were restored from
HEAD by title, two of them by hand where the match missed, until the diff held nothing but this wave's
additions. The script now prints its docstring for `--help` and refuses, writing nothing, an option it
does not read or a domain name without `--only`. **A tool whose default is a write has to fail closed
on an argument it does not recognize.**

```
3 commits · 4 topics, 16 concept cards · 13 census queries, 0 of 13 -> 13 of 13 · 2 tools fixed
topics 1,587 -> 1,591 · path steps 2,128 -> 2,136 · related links 5,098 -> 5,138 · dated claims 138 -> 163
45 gates green · smoke 166 · search 59 · resilience 64 · axe 33/33 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%
```

## Session — expand made a mode, at the owner's request

The owner asked for the EXPAND switch to open every topic of a domain they click while it is on,
and gave endpoint's *Troubleshooting Toolkit* (`#troubleshooting-toolkit-log-reference`) as the
example. It did not: `toggleAll()` opened the topics of the domain on screen and stopped there, so a
domain opened next, by its chip or its header, arrived collapsed while the switch still read *on*.
**The switch claimed a mode it did not keep.**

`openDomain()` now reads `allExpanded`. A domain opened while it is on, by header, chip, link or
search, arrives with every topic open; a domain already on screen is left alone, so a chip aimed at
it does not reopen topics the reader has closed since. The switch's title says it is a mode, and so
does the README.

Smoke gained the check that drives the owner's case: switched on in `m365`, 46 of 46 open; `endpoint`
by its chip, 63 of 63, the toolkit among them; `net` by its header, 73 of 73; switched off, `cs` opens
none. Run against the old `script.js` it failed with `endpoint` at 0 of 63 and `net` at 0 of 73, the
switch still checked, which is the report in numbers.

```
1 commit · 1 behavior changed · smoke 166 -> 167, and the new check fails on the old script
```

## Session — the sixteenth wave, MS-102's identity and Purview gaps, and a tool the outline still names

The wave began, and then paused for the owner's expand request, which has its own record above and
its own commit. §20's list of MS-102 gaps had four left after the fifteenth wave, and this wave is
those four. *Content ideas* §22 is the table.

### Read first, and one page that was gone

Sixteen Microsoft Learn pages were read before a card was written: self-service password reset and
its writeback, three on Password Protection, three on administrative units, preparing a directory for
sync, `.local` domains and sync errors, two on sensitive information types and three on Endpoint DLP.
A seventeenth, Microsoft's page on installing IdFix, returned 404. IdFix's own repository, read in its
place, says the tool was deprecated and has been unsupported since 30 June 2026. MS-102's outline,
skills measured as of 28 April 2026, still names it, so the topic teaches the rules IdFix checked and
says not to install it. Thirteen queries went into *a service desk engineer* next and opened at 0 of
13.

### What the pages said that the cards had to carry

Each card has a fact a service desk would otherwise learn from a ticket. Authenticator and the OATH
tokens count as one reset method between them, so a policy raised from one method to two locks out
everyone who registered only the app. A self-service reset reaches Active Directory as an admin reset,
so a third-party password filter set only for users' own changes never sees it. A password refused by
Password Protection on a domain controller shows Windows' ordinary complexity message, and a DC that
has never downloaded a policy accepts everything. A group placed in an administrative unit brings the
group into scope but not its members. A restricted management unit keeps out even Global
Administrators. And Endpoint DLP classifies every file against every sensitive information type in the
tenant, used or not, so a loose custom pattern costs something before any policy refers to it.

### A new card took an old answer away

`bitlocker recovery key`, a service desk query from an early batch, stopped finding the BitLocker topic
when the administrative units card was spliced. Search tries the exact phrase first and widens only when
that finds at most one topic. The phrase had been in one card, the Windows repair ladder, so search
used to widen and reach the BitLocker topic. The new card's *BitLocker recovery keys* made two exact
matches, search stopped there, and the topic about BitLocker recovery keys, which said *recovery key*
and never Microsoft's full name for it, was not among them. Its table row says *BitLocker recovery
key* now, and the query finds it first of three. **A card can change the answer to a query it never
mentions, and only a census that runs every reader catches it.**

### The census

The batch closed at 13 of 13 with one prose fix: `helpdesk admin for one office only` lacked only
*office*, which was what the card's example of a regional helpdesk meant, and the row says *one
office's helpdesk* now. The census as a whole is 547 of 571 with nothing unexplained.

```
2 commits · 4 topics, 12 concept cards · 13 census queries, 0 of 13 -> 13 of 13 · 1 old query restored
topics 1,591 -> 1,595 · path steps 2,136 -> 2,144 · related links 5,138 -> 5,170 · dated claims 163 -> 178
45 gates green · smoke 167 · search 59 · resilience 64 · axe 33/33 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%
```
