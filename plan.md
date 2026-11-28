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
| **Content ideas** | A request for more content to add, in the same clean look. 839 candidate phrases in 17 reader groups, each checked against the content and against the built page's search: 81 are owned by a title, 452 are mentioned in passing and 306 are absent. The largest finding was not on the list: the page is headed *Cycles, Concepts &amp; Diagrams* and 58 of 1,503 hand-written topics carry a shape. Twenty diagrams from components that already exist, about thirty-five candidate cards, exam paths that need no new content, and a look contract with one hole in it. First wave conducted: the hole fixed and gated, the exam reader at 16 of 16, the UML lines drawn, six cards and a topic. Second wave conducted: twelve cards over ten rows, the reader's second batch at 23 of 23, and three tools fixed at their own edges. Third wave conducted: a topic and ten cards over five rows, twelve connectors drawn, the reader's third batch at 16 of 16, and two census answers that were coincidences. Fourth wave conducted: seven theory cards, the theory reader at 15 of 15, and a spelling gate taught a suffix. Fifth wave conducted: three topics and eight cards in the human domains, each under its row's condition, at 17 of 17. Sixth wave conducted: three quotes topics, every line read at its source, two lines moved to Misattributed, at 10 of 10. Seventh wave conducted: the nineteen remaining pictures of §2 in fourteen domains, eight of them drawn with another component than their row named, and two numbers corrected by drawing them. Eighth wave conducted: four exam paths over topics that exist, a path as a deck, the two gaps the census carried, search that no longer reads acronym expansions, and a spelling gate that knows prefixes. Ninth wave conducted: §16's list emptied, five topics for the A+ objectives the paths skipped and a Security+ SY0-801 path read from CompTIA's own objectives. Tenth wave conducted: four more exam paths, PenTest+, CySA+, Linux+ and CISSP, each read from the exam body's own document, and six topics for the objectives they found with nothing to point at. Eleventh wave conducted: a SecurityX path read from CompTIA's own document, and the two CISSP objectives the tenth left, one of which SecurityX needed too. Fourteenth wave conducted: MD-102 and MS-102 paths read from Microsoft's study guides, AZ-800 found retired and its tag corrected, and the gaps both outlines found listed as the next queue. Fifteenth wave conducted: four topics for MS-102's Defender XDR area, each read from Microsoft's own pages first, at 13 of 13. Sixteenth wave conducted: MS-102's identity and Purview gaps, four topics at 13 of 13, and IdFix found retired. Seventeenth wave conducted: MS-102's last three Defender objectives, three topics at 13 of 13, and the standalone Defender Threat Intelligence portal found retired. Eighteenth wave conducted: four of MD-102's seven gaps at 13 of 13, the Semi-Annual Enterprise Channel found merged into Monthly Enterprise and Windows Backup for Organizations found renamed. Nineteenth wave conducted: MD-102's last three gaps at 13 of 13, and three of the four Security Copilot agents in Intune found retired. Twentieth wave conducted: RASP and IAST from NIST's catalog, and a CKA path read from the Linux Foundation's outline with its three gaps, at 15 of 15, and Ingress NGINX found retired. Twenty-first wave conducted: a GCIH path read from GIAC's objectives and a topic for SANS's DAIR, at 5 of 5, and two statements about NIST SP 800-61 corrected. Twenty-second wave conducted: an AWS SAA-C03 path read from AWS's exam guide, topics for its three gaps, and two AWS services found closed to new customers. Twenty-third wave conducted: seven services the guide gives as examples and the site had never mentioned, at 15 of 15. Twenty-fourth wave conducted: the guide's remaining examples and in-scope services, at 17 of 17, and a discovery service found closed. Twenty-fifth wave conducted: cards inside the AWS topics that already owned each subject, and purpose-built databases, at 15 of 15. Twenty-sixth wave conducted: the NAT instance and AWS's regional NAT gateway, after which every service the SAA-C03 task statements name is on the site. Twenty-seventh wave conducted: a Google Cloud Associate Cloud Engineer path read from Google's exam guide, three gap topics, and Cloud Functions found renamed. Twenty-eighth wave conducted: Deployment Manager's retirement written as a retirement, and two more groups of the guide's items, at 12 of 12. Twenty-ninth wave conducted: the guide's operations and storage items, as cards in the topics that owned them, at 10 of 10. Thirtieth wave conducted: the AI+ tag found to name no CompTIA exam, replaced with SecAI+ and a 30-step path. Thirty-first wave conducted: OWASP's 2026 lists for LLM applications and for agents, and the EU AI Act's dates after the AI Omnibus. Thirty-second wave conducted: NIST AI RMF's seven characteristics and its Generative AI Profile, and a card that had put NIST's name on somebody else's list. Thirty-third wave conducted: OWASP Top 10:2025 in the three topics that teach it, with a map from 2021. Thirty-fourth wave conducted: NIST CSF 2.0's six functions wherever `grc` named five, in NIST's own colors. Thirty-fifth wave conducted: SecAI+'s words for what two `blueteam` topics already taught, and a PenTest+ badge two exams old. Thirty-sixth wave conducted: ATT&amp;CK version 19's fifteen tactics. Thirty-seventh wave conducted: NIST IR 8547's post-quantum dates, HQC, and AES-128 as NIST rates it. Thirty-eighth wave conducted: public TLS certificate lifetimes falling to 47 days, and revocation after Let's Encrypt ended OCSP. Thirty-ninth wave conducted: the EU Cyber Resilience Act, a regulation the site had never named. Fortieth wave conducted: the CIS Controls named at version 8.1, and Kerberos RC4 against Microsoft's current defaults. Forty-first wave conducted: how a package repository is trusted, in the thinnest topic on the site, and Netlify Functions at the owner's request. Forty-second wave conducted: three thin topics deepened from FM 6-0, NVD and GitHub's documentation, and the visual baseline's failure traced to a Playwright version. Forty-third wave conducted: the last three thin topics, a SQL puzzle run on PostgreSQL 16, HTTP errors read by the layer that sends them and what certifications cost to keep, and a gate taught to check a row's headline. Forty-fourth wave conducted: the twelve oldest dated claims re-checked against their owners' current pages, seven corrected, and CI green on the first pull request since the runner pin. Forty-fifth wave conducted: the twenty-two `m365` claims from September re-checked, four corrected. Forty-sixth wave conducted: the seventeen `endpoint`, `infra` and `cloud` claims from September, two corrected and six given their owners' pages in place of secondhand sources. Forty-seventh wave conducted: September's last twenty-six claims, the csvistool routes confirmed against the live site, and no dated claim left older than October. Forty-eighth wave conducted: the October claim's page read at last, and every dated claim on the site checked this month. Forty-ninth wave conducted: Phase 11's tier-gating pass redone against Microsoft's pages, two of three claims corrected. Fiftieth wave conducted: the product-names class, eight stale names corrected in seventeen topics from their owners' pages, and the rename guard's own current names found aged. Fifty-first wave conducted: the registry's other twenty-three current names re-checked on their owners' pages, all twenty-three current, and each entry now dated. Fifty-second wave conducted: the thirty comparison tables read, two cells corrected on their owners' pages, and a census query the fiftieth wave broke put back. Fifty-fourth wave conducted: Microsoft's 2026 certification retirements, AZ-500 gone and MS-102 going, corrected on the roadmap and the MS-102 path. Fifty-fifth wave conducted: an AB-650 path read from Microsoft's study guide, the header tags moved off MS-102 and MEM, and AB-650's gaps listed as the next queue. Fifty-sixth wave conducted: Microsoft 365 Copilot's settings, the first AB-650 gap, read from six Microsoft pages, at 5 of 5. Fifty-seventh wave conducted: agents in Microsoft 365, the agent registry, Entra Agent ID and Conditional Access for agents, at 5 of 5. Fifty-eighth wave conducted: running Copilot, its credits, spending policies, usage reports and release timing, and Microsoft 365 E7 in the licensing table, at 6 of 6. Fifty-ninth wave conducted: Copilot's data readiness and Purview for AI, as cards in the two topics that own them, at 5 of 5. Sixtieth wave conducted: AB-650's last three gaps, Microsoft 365 Backup, Copilot in Teams meetings and network connectivity, as cards, at 3 of 3, and every gap the guide showed now answered. Sixty-first wave conducted: an AZ-802 path read from Microsoft's study guide, the exam that replaced AZ-800 and AZ-801, with the infra header tag moved to it and its gaps listed. Sixty-second wave conducted: read-only domain controllers and domain controllers in Azure, AZ-802's first gap, at 4 of 4, and a stamping tool taught where a topic ends. Sixty-third wave conducted: Azure Files and Azure File Sync, AZ-802's second gap, as a card in File Services, at 3 of 3. Sixty-fourth wave conducted: Hyper-V's own features, AZ-802's third gap, as a card in the Hyper-V topic, at 4 of 4. Sixty-fifth wave conducted: Windows Server storage, AZ-802's fourth gap, as two cards, at 3 of 3 | ✅ **shipped** — see its §9 to §109 |
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
| Topics | **1,639** across 30 domains | `depth_report.py` |
| Thin (one card, under 1,800 chars) | **0**, 0% — and `--thin` prints badge, position and xref count beside each, because a short topic can be short by design. Three of the eight were not: two military lookup cards and a domain preamble each had a judgement they were not making. The forty-first wave took a seventh off the list: `linux`'s *Package Management*, the thinnest topic on the site, which had a table of commands and nothing on how a repository is trusted. The forty-second wave took three more: the two military lookup topics, neither of which said that their numbers name only one of FM 6-0's three kinds of staff officer, and `devops`'s supply-chain overview, which never named the pipeline's own dependencies. The forty-third wave took the last three: `data`'s interview topic, `web`'s full-stack overview and `eng`'s certification roadmap, each given the card its table implied and never wrote. When those cards landed the row still read **3** while the tool printed 0, and `check_plan_numbers.py` passed it on the 0 of *0%*; it checks each row's headline now | `depth_report.py` |
| Mean chars per concept card | **1,460**, or **1,171 excluding verdicts** — the second is the padding counter-metric. It has tracked the first within two across every wave this session, which is the shape to want: the two numbers moving together | `depth_report.py` |
| Orphans | **60**, every one generated, **0 deep** | `orphan_report.py` |
| Near-duplicate pairs | **97** (41 by overlap, 56 by containment) — 78 explained by §3, 19 read and recorded, **0 unread** | `near_duplicates.py` |
| Reader questions answered | **995 of 1,017**, **0 unexplained** — one hundred and twenty-one batches. The newest is the hundred-and-third wave's, 6 queries for SC-200's last gaps, answered by a card in `blueteam`'s *Threat Hunting — Assume Breach, Go Looking* and one in `m365`'s *eDiscovery, Content Search &amp; the Audit Log* and added before them. It opened at **0 of 6**, two zeros and four that found other cards, and closed at 6 of 6 once the Graph card asked, in the reader's words, which app called the Graph API. Before it came the hundred-and-second wave's, 6 queries for SC-200's Sentinel gaps, answered by two cards in `cloud`'s *Microsoft Sentinel* and added before them. It opened at **0 of 6**, two zeros and four that found other cards, and closed at 6 of 6 with no query replaced. Before it came the hundred-and-first wave's, 4 queries for SC-200's Windows Event Forwarding, answered by a card in `blueteam`'s *Windows Event Logs — The IDs That Matter* and added before it. Two first-draft queries, *windows event forwarding* and *windows event collector*, already reached that topic, whose existing card says to forward logs to a collector, and were replaced before the card with *wef subscription* and *read existing events*. It opened at **0 of 4**, three zeros and one that found other cards, and closed at 4 of 4. Before it came the hundredth wave's, past a thousand queries, 5 queries for SC-200's Defender for Endpoint gaps, answered by two cards in `endpoint`'s *Defender for Endpoint &amp; Intune* and added before them. It opened at **0 of 5**, one zero and four that found other cards, after a first-draft query, *live response*, was replaced before the cards: its two words already met in 60 topics, and the card would have made it 61, wide. Its replacement, *live response session*, is the button's own name. Before it came the ninety-ninth wave's, 6 queries for SC-200's Defender XDR gaps, answered by three cards in `m365`'s *Defender XDR Incidents &amp; Advanced Hunting* and added before them. It opened at **0 of 6**, three zeros and three that found other cards, and closed at 6 of 6 once two cards used the words Microsoft and the reader share: *case management*, which the cases card had not said, and *natural language*, where it had said plain language. Before it came the ninety-seventh wave's, 5 queries for SC-300's last gap, answered by a card in `m365`'s *Secure Score &amp; the Tenant Baseline* and one in `cloud`'s *Entra ID — Sign-In &amp; Conditional Access Troubleshooting* and added before them. It opened at **0 of 5**, two zeros and three that found other cards, and closed at 5 of 5 once the provisioning card said in the reader's words that a user was not provisioned. Before it came the ninety-sixth wave's, 5 queries for SC-300's attribute and governance gaps, answered by a card in `cloud`'s *Azure Hierarchy, RBAC Scopes &amp; Policy* and one in `m365`'s *Entra ID Governance* and added before them. It opened at **0 of 5**, all five finding other cards, and closed at 5 of 5 with no query replaced. Before it came the ninety-fifth wave's, 5 queries for SC-300's authentication gaps and Application Proxy, answered by two cards in `sec`, one in *Multi-Factor Authentication* and one in *ZTNA*, and added before them. It opened at **0 of 5**, two zeros and three that found other cards, and closed at 5 of 5 with no query replaced and no word changed. `application proxy` finds its card among 38, because 37 other topics hold both words, as the baseline showed; the census lists hits in domain order, not by rank. Before it came the ninety-fourth wave's, 5 queries for SC-300's role and tenant gaps, answered by two cards in `m365`, one in *Admin Roles &amp; Least Privilege* and one in *External Collaboration*, and added before them. It opened at **0 of 5**, one zero and four that found other cards, after a first-draft query for administrative units, which an existing topic already answers, was replaced, and closed at 5 of 5 once the cross-tenant card said in plain words that it keeps users in sync between tenants; that query finds its card among 13. Before it came the ninety-second wave's, 5 queries for AZ-104's Azure DNS and Advisor, answered by a card in `cloud`'s *Azure Networking* and one in its *Cloud Cost Control* and added before them. It opened at **0 of 5**, three zeros and two that found other cards, after one first-draft query that already matched was replaced, and closed at 5 of 5. Before it came the ninety-first wave's, 5 queries for AZ-104's Azure Monitor alerting, answered by a card in `cloud`'s *Azure Monitor, Log Analytics &amp; KQL* and added before it. It opened at **0 of 5**, one zero and four that found other cards, and closed at 5 of 5 once the card used Microsoft's names for its alert types and its heading for maintenance windows. Before it came the ninetieth wave's, 5 queries for AZ-104's storage access and tools, answered by two cards in `cloud`'s *Azure Compute &amp; Storage* and one in `infra`'s *File Services* and added before them. It opened at **0 of 5**, one zero and four that found other cards, and closed at 5 of 5. Before it came the eighty-ninth wave's, 5 queries for AZ-104's blob and file data protection, answered by a card in `cloud`'s *Azure Compute &amp; Storage* and one in `infra`'s *File Services* and added before them. It opened at **0 of 5**, one zero and four that found other cards, and closed at 5 of 5. Before it came the eighty-eighth wave's, 5 queries for AZ-104's backup and recovery, answered by a new `cloud` topic and added before it. It opened at **0 of 5**, one zero and four that found other cards, and closed at 5 of 5. Before it came the eighty-sixth wave's, 3 queries for MD-102's device query, answered by a card in `endpoint`'s *Microsoft Intune* and added before it. It opened at **0 of 3**, one zero and two that found other cards, and closed at 3 of 3 once the card's verdict used Microsoft's own words for the checks it replaces. Before it came the eighty-fifth wave's, 5 queries for SC-500's data controls, answered by a card in `cloud`'s *Azure Databases* and one in its *Azure Compute &amp; Storage* and added before them. It opened at **0 of 5**, one zero and four that found other cards, and closed at 5 of 5. Before it came the eighty-fourth wave's, 5 queries for SC-500's VM security, answered by a card in `cloud`'s *Azure Compute &amp; Storage* and one in its *Azure Arc* and added before them. It opened at **0 of 5**, three zeros and two that found other cards, and closed at 5 of 5. Before it came the eighty-third wave's, 5 queries for SC-500's network services, answered by a card in `cloud`'s *Azure Networking* and one in `sec`'s *ZTNA* and added before them. It opened at **0 of 5**, two zeros and three that found other cards, and closed at 5 of 5. Before it came the eighty-second wave's, 5 queries for SC-500's AI workloads in Azure, answered by a new `cloud` topic and added before it. It opened at **0 of 5**, three zeros and two that found other cards, and closed at 5 of 5. Before it came the eighty-first wave's, 5 queries for SC-500's Microsoft Sentinel items, answered by a new `cloud` topic and added before it. It opened at **0 of 5**, four zeros and one that found other cards, and closed at 5 of 5. Before it came the eightieth wave's, 5 queries for SC-500's Defender for Cloud plans, answered by a new `cloud` topic and added before it. It opened at **0 of 5**, two zeros and three that found other cards, and closed at 5 of 5. Before it came the seventy-seventh wave's, 3 queries for MD-102's specialty devices, answered by a card in `endpoint`'s shared and kiosk devices topic and added before it. It opened at **0 of 3**, all three zeros, and closed at 3 of 3 after one wording fix: the card said *LifeGuard Over-the-Air* and the reader typed `ota`. Before it came the seventy-sixth wave's, 3 queries for MD-102's enrollment time grouping and Samsung Knox Mobile Enrollment, answered by cards in two `endpoint` topics and added before them. It opened at **0 of 3**, all three zeros, and closed at 3 of 3. Before it came the seventy-fifth wave's, 3 queries for MD-102's custom compliance, BitLocker key rotation and troubleshooting pane, answered by cards in three `endpoint` topics and added before them. It opened at **0 of 3**, two zeros and one that found other cards, and closed at 3 of 3. Before it came the seventy-third wave's, 4 queries for AZ-802's AD delegation and DNS policies, answered by cards in two existing topics and added before them. It opened at **1 of 4**, `ad delegation service administrators` already answered, two zeros and one that found other cards, and closed at 4 of 4. Before it came the seventy-second wave's, 4 queries for the Hyper-V VM's own configuration, answered by a card in the Hyper-V topic and added before it. It opened at **0 of 4**, two zeros and two that found other cards, and closed at 4 of 4. Before it came the seventy-first wave's, 3 queries for PowerShell remoting's second hop, answered by a card in the JEA topic and added before it. It opened at **0 of 3**, two zeros and one that found another card, and closed at 3 of 3; the card's own words also took `protected users group` from the sixty-sixth wave's topic, until that topic said *the Protected Users group* itself. Before it came the seventieth wave's, 4 queries for AZ-802's SMB Direct, Storage QoS and connection security rules, answered by cards in three existing topics and added before them. It opened at **1 of 4**, `smb direct rdma` already answered by the SMB topic's version table, one zero and two that found other cards, and closed at 4 of 4. Before it came the sixty-ninth wave's, 4 queries for the Hyper-V items AZ-802 lists and the sixty-fourth wave left, answered by a card in the Hyper-V topic and added before it. It opened at **0 of 4**, three zeros and one that found other cards, and closed at 4 of 4. Before it came the sixty-eighth wave's, 3 queries for AZ-802's access to Azure VMs, answered by a card in `cloud`'s Azure networking topic and added before it. It opened at **0 of 3**, two zeros and one that found another card, and closed at 3 of 3. Before it came the sixty-seventh wave's, 6 queries for AZ-802's monitoring tools and SmartScreen, answered by a new topic and a card and added before them. It opened at **0 of 6**, four zeros and two that found other cards, and closed at 6 of 6 with no wording fix. Before it came the sixty-sixth wave's, 4 queries for AZ-802's Windows Server security, answered by a new topic and added before it. It opened at **0 of 4**, two zeros and two that found other cards, and closed at 4 of 4 after one wording fix: the topic said *Local Security Authority* and *isolated*, and the reader typed `lsa` and `isolation`. Before it came the sixty-fifth wave's, 3 queries for AZ-802's Windows Server storage, answered by cards in two existing topics and added before them. It opened at **0 of 3**, all three finding other cards, and closed at 3 of 3. Before it came the sixty-fourth wave's, 4 queries for AZ-802's Hyper-V features, answered by a card in the Hyper-V topic and added before it. It opened at **0 of 4**, two zeros and two that found other cards, and closed at 4 of 4, `powershell direct` among twenty-seven. Before it came the sixty-third wave's, 3 queries for AZ-802's Azure Files and Azure File Sync, answered by a card in *File Services* and added before it. It opened at **0 of 3**, one zero and two that found other cards, and closed at 3 of 3, each among two to thirteen. Before it came the sixty-second wave's, 4 queries for AZ-802's read-only domain controllers and domain controllers in Azure, added before the topic. It opened at **0 of 4**, two zeros and two that found other cards, and closed at 4 of 4 after one wording fix: the card described administrator role separation without using Microsoft's name for it. Before it came the sixtieth wave's, 3 queries for AB-650's last gaps, answered by cards in three existing topics and added before them. It opened at **0 of 3**, one zero and two that found other cards, and closed at 3 of 3 with no wording fix. Before it came the fifty-ninth wave's, 5 queries for AB-650's data readiness and Purview for AI, answered by cards in two existing topics and added before them. It opened at **0 of 5**, one zero and four that found other cards, and closed at 5 of 5 with no wording fix. Before it came the fifty-eighth wave's, 6 queries for AB-650's monitoring of AI services and for Microsoft 365 E7, added to *a service desk engineer* before the topic. It opened at **0 of 6**, three zeros and three that found other cards, and closed at 6 of 6 after one wording fix: Microsoft's page says Targeted release *will be retired*, and the card had said *retires*, which does not contain the reader's *retired*. Before it came the fifty-seventh wave's, 5 queries for AB-650's agents, added to *a service desk engineer* before the topic. It opened at **0 of 5**, two zeros and three that found other cards, `agent registry` among thirteen, and closed at 5 of 5 after one wording fix: the card said an agent *loses its owner*, and Microsoft's page and the reader say *ownerless*. Four find the topic alone. Before it came the fifty-sixth wave's, 5 queries for AB-650's Copilot settings, added to *a service desk engineer* before the topic. It opened at **0 of 5**, all zeros, on a site that had never said how Copilot's controls work, and closed at 5 of 5: four alone, and `turn off web search in copilot` among eight, behind a general card on AI tools. Before it came the fifty-fourth wave's, 3 queries for Microsoft's 2026 certification retirements, added to *somebody looking for a job* before the roadmap was corrected. It opened at **1 of 3**: `what replaces ms-102` reached the roadmap on the exam's code, and `az-500 retired` and `sc-500 certification` were zeros, the second a code the site had never written. It closed at 3 of 3, two alone. Before it came the fifty-second wave's, 2 queries for the comparison-table cells it corrected, added to *somebody with a cloud bill and a pager* before the edits. It opened at **2 of 2**, both alone, because the cells were wrong rather than missing, and it closed the same: the census measures whether a reader arrives, and this wave fixed what they found. Before it came the fiftieth wave's three, 7 queries for product names measured against the page before the renames: 3 added to *a service desk engineer*, 1 to *a Linux or platform engineer* and 3 to *somebody with a cloud bill and a pager*. They opened at **3 of 7**: `wdac`, `msonline retired` and `google cloud observability` already reached their topics on the old wording, `hcp terraform` was a zero, a name the site had never written, and three found other cards, `microsoft configuration manager` among sixteen because the topic still carried the 2019 name. They closed at 7 of 7 with no wording fix, three alone. Before them came the forty-ninth wave's, 2 queries for the licensing claims it rewrote, added to *a service desk engineer* and measured against the page before the rewrite. It opened at **0 of 2**, both finding other cards, and closed at 2 of 2 after two wording fixes, *includes* and *requirement*, the words the reader types. Before it came the forty-seventh wave's two: 1 query for the DSM's next edition, added to *a learner meeting a subject*, and 1 for how long cloud credentials last, added to *somebody with a cloud bill and a pager*, both measured against the page before the corrections were built. They opened at **0 of 2** and closed at 2 of 2, both alone, with no wording fix. Before them came the forty-sixth wave's, 2 queries for the endpoint and infra claims it corrected, added to *a service desk engineer* and measured against the page before the corrections were built. It opened at **0 of 2**, both zeros, and closed at 2 of 2, one alone, after one wording fix: the reader asks what is *included* in E3, and the card said E3 *includes*. Before it came the forty-fifth wave's, 3 queries for the m365 claims it re-checked, added to *a service desk engineer* before the corrections. It opened at **1 of 3**: `admin.cloud.microsoft` already reached the tenant topic, which named the address in passing, and two were zeros. It closed at 3 of 3, two alone, after three wording fixes: Microsoft's own terms, *quarantine retention period* and *expiration policy*, and *auto-renews*, because a four-letter word must match a whole word and *automatically* does not contain the word *auto*. Before it came the forty-fourth wave's two: 4 queries for the Microsoft claims it re-checked, added to *a service desk engineer*, and 1 for a price the memory shortage moved, added to *somebody looking for a job*, all before the corrections. They opened at **2 of 5**: `shared mailbox size limit` and `gmsa password length` already reached their topics on ordinary words, around claims that were vague or wrong, and three were zeros. They closed at 5 of 5, one alone, after one wording fix: the Pi line said *dearer*, and the reader asks what it *costs*. Before them came the forty-third wave's three: 3 queries for the second-highest-salary puzzle added to *somebody looking for a job*, 3 for which layer sent an HTTP error added to *somebody debugging their own code*, and 3 for what certifications cost to keep added to *somebody revising for a CompTIA exam*, all before the cards. They opened at **1 of 9**, four zeros and four that found other cards; `second highest salary` already reached the interview topic, whose table named the puzzle without doing it. They closed at 9 of 9, two alone and seven among two to nine, after three wording fixes that put the reader's words in the cards: each status code's name, *Gateway Timeout* among them, *CEUs* beside continuing education units, and *requirements*. Before them came the forty-second wave's two: 6 queries for the staff officers FM 6-0 describes added to *a learner meeting a subject*, and 4 for a CI pipeline's own dependencies added to *a Linux or platform engineer*, all before the cards. They opened at **0 of 10**, six zeros and four that found other cards, `what does the s-3 do` among them reaching forty on its letters, and closed at 10 of 10: five alone, and five among two to forty-one. Before them came the forty-first wave's, 3 queries for how a package repository is trusted, added to *a Linux or platform engineer* before the card. It opened at **0 of 3** and closed at 3 of 3, all alone. Before it came the fortieth wave's two: 2 queries for the CIS Controls' version and parts added to *somebody answerable to an auditor*, and 2 for Kerberos after CVE-2026-20833 added to *a SOC analyst or defender*, all before the fixes. They opened at **0 of 4**, all zeros, and closed at 4 of 4, all four alone; the two Kerberos terms closed only once they were in the row's visible text and not just its fact anchor, which search does not read. Before them came the thirty-ninth wave's, 3 queries for the EU Cyber Resilience Act, added to *somebody answerable to an auditor* before the card. It opened at **1 of 3**, and that one by coincidence: `cyber resilience act` reached the regulatory topic through *cyber*, *resilience* and *act* in three unrelated sentences, on a site that had never named the regulation. It closed at 3 of 3, the regulation's name alone. Before it came the thirty-eighth wave's, 4 queries for public TLS certificate lifetimes and the end of OCSP at Let's Encrypt, added to *a Linux or platform engineer* before the cards. It opened at **0 of 4**, all zeros, and closed at 4 of 4: two alone, and `47 day certificates` and `ocsp turned off` among five and six. Before it came the thirty-seventh wave's, 4 queries for NIST's post-quantum transition report and HQC, added to *somebody revising for a CompTIA exam* before the cards. It opened at **1 of 4**: `post-quantum migration deadline` reached the topic on ordinary words, and `nist ir 8547`, `hqc` and `is aes-128 quantum safe` were zeros, the first two words the site had never written. It closed at 4 of 4, three alone. Before it came the thirty-sixth wave's, 3 queries for ATT&CK version 19's fifteen tactics, added to *a SOC analyst or defender* before the cards. It opened at **1 of 3**: the old name, `defense evasion`, already reached the framework topic, and the two new names were zeros. It closed at 3 of 3, each among two. Before it came the thirty-fifth wave's, 6 queries for the rest of SecAI+'s summary terms, added to *somebody revising for a CompTIA exam*. It opened at **4 of 6**: four already reached a fitting topic, and two found other cards, `alert correlation` because the correlation topic never says *alert*, and `behavior analysis` because the UEBA topic says *analytics*. It closed at 6 of 6, those two alone, with one sourced sentence in each topic. Before it came the thirty-fourth wave's, 3 queries for NIST CSF 2.0, added to *somebody answerable to an auditor* before the fixes. It opened at **2 of 3**: the two about the functions were already answered, because the errors were inside cards the reader could find, and only `technology infrastructure resilience`, one of NIST's category names, was a zero. It closed at 3 of 3, that one alone. A census measures whether the reader reaches a card, not whether the card is right, and this wave was the second kind. Before it came the thirty-third wave's, 5 queries for OWASP Top 10:2025, added to *somebody revising for a CompTIA exam* before the cards. It opened at **0 of 5**, one zero, `mishandling of exceptional conditions`, and four that found other cards. It closed at 5 of 5, all five among three to six topics, after one wording fix: the first closing run found `security logging and alerting failures` in two topics but not the one it wanted, which wrote the category with an ampersand, as OWASP's introduction does, and now writes *and*, as OWASP's list does. Before it came the thirty-second wave's, 6 queries for NIST's AI RMF and its Generative AI Profile, added to *somebody revising for a CompTIA exam* before the cards. It opened at **0 of 6**, five zeros, every one a term NIST uses and the site never had, and `valid and reliable` reaching twelve cards on ordinary words. It closed at 6 of 6: three alone, two among two, and `valid and reliable` among thirteen, because a phrase found in one topic whose address holds neither word widens, and TCP's reliability comes first in page order. Before it came the thirty-first wave's two: 8 queries for OWASP's 2026 lists added to *somebody revising for a CompTIA exam*, and 4 for the EU AI Act's dates after the AI Omnibus added to *somebody answerable to an auditor*, both before the cards. They opened at **0 of 12**, ten zeros and two that found other cards by coincidence: `unbounded consumption` reached the Azure Functions card, whose cheapest plan is called Consumption and whose dearest runs unbounded, and `denial of wallet` the observability topic's card on attacker-controlled cardinality, which is one. They closed at 12 of 12, three alone and nine among two to four. Before them came the thirtieth wave's, 7 queries for CompTIA's SecAI+, added to *somebody revising for a CompTIA exam* before its path. It opened at **5 of 7**, because the site had the subjects and lacked two of the exam's words: CompTIA's name for its largest domain, `securing ai systems`, and the field's standard term, `adversarial machine learning`, each of which found other cards. It closed at 7 of 7 with a sentence in each topic using the term; one finds its topic alone and six among two to ten, `data poisoning attack` behind DNS cache poisoning in first place. Before it came the twenty-ninth wave's, 10 queries for the ACE guide's operations and storage items, answered by cards in existing GCP topics. It opened at **1 of 10**, four zeros, five that found other cards and one already reaching its topic on ordinary words, and closed at 10 of 10, five alone and five among two to eleven. Before it came the twenty-eighth wave's, 12 queries for Deployment Manager's retirement and two more of the ACE guide's gaps, added to *somebody with a cloud bill and a pager* before the topics. It opened at **0 of 12**, five zeros and seven that found other cards, and closed at 12 of 12, five alone and seven among two to ten. On the way it briefly answered an old recorded zero by accident: `terraform state locked` matched the Deployment Manager card's *new users blocked*, because search matches inside words and *blocked* holds *locked*; the census reported the note as stale, and the row now says *refused*. Before it came the twenty-seventh wave's, 12 queries for gaps Google's Associate Cloud Engineer guide shows, added to *somebody with a cloud bill and a pager* before their topics. It opened at **0 of 12**, five zeros, `eventarc` and `workforce identity federation` among words the site had never written, and seven that found other cards, `cloud run functions` reaching 30 and none of them about the product, which the site still called by its old name; it closed at 12 of 12, four alone and eight among two to fifteen. Before it came the twenty-sixth wave's, 3 queries for task 4.4's NAT instance and per-zone gateways, a card added to the AWS VPC topic. It opened at **2 of 3**: two reached the VPC topic on ordinary words, a topic that priced NAT gateways and never named the NAT instance, and `regional nat gateway` found one other card, because AWS had added the regional kind since the topic was written. It closed at 3 of 3. Before it came the twenty-fifth wave's, 15 queries for the guide's last task-statement examples and five in-scope databases, most of them answered by cards added to existing topics. It opened at **3 of 15**, the first batch to open above zero: three reached their existing topic on ordinary words without it naming the thing asked for, nine were zeros and three found other cards. It closed at 15 of 15, twelve alone and three among two to five. The wave also answered an old recorded zero: `nat gateway is the biggest line on the bill` reaches the cost control topic, whose new Compute Optimizer card names NAT gateways among what it rightsizes, beside the card on finding which resource a bill line comes from; it is recorded as answered, with a note that the per-GB reason the line is large is in another topic the query does not reach. Before it came the twenty-fourth wave's, 17 queries for the SAA-C03 guide's remaining examples and in-scope gaps, added to *somebody with a cloud bill and a pager* before their topics. It opened at **0 of 17**, eleven zeros, `rekognition`, `sagemaker` and `appflow` among words the site had never written, and six that found other cards, `aws config rules` reaching 31 and none of them about AWS Config, and closed at 17 of 17 after two wording fixes made before the first run, each giving a card AWS's own words: *AWS DMS* beside the service's full name, and *migrate* where the Classic Load Balancer card had said *migrating*, because search matches inside words and *migrate* is not inside *migrating*. Twelve find their topic alone and five among two to seven. Before it came the twenty-third wave's, 15 queries for seven services the SAA-C03 guide names as examples, added to *somebody with a cloud bill and a pager* before their topics. It opened at **0 of 15**, twelve zeros, `valkey` and `quicksight` among words the site had never written, and three that found other cards, `aws backup vault lock` reaching six and none of them about AWS Backup, and closed at 15 of 15 with no prose fix: eight find their topic alone and seven among two to six. The three Cognito queries return five cards each because search matches inside words, and `cognito` is inside *incognito*, which the browser shortcut and web cards use for private windows. Before it came the twenty-second wave's, 14 queries for the AWS SAA-C03 outline's gaps added to *somebody with a cloud bill and a pager* before their topics. It opened at **0 of 14**, seven zeros, `eventbridge`, `kinesis` and `datasync` among words the site had never written, and seven that found other cards, and closed at 14 of 14 after one prose fix: `step functions express` reached 27 cards on ordinary words until the Express verdict named the service in full, and it finds its topic alone now. Eight find their topic alone and six among two to six. Before it came the twenty-first wave's, 5 queries for DAIR and NIST's 2025 revision added to *a SOC analyst or defender* before the topic. It opened at **0 of 5**, two zeros and three that found other cards, and closed at 5 of 5 once one query's want moved to the card that actually answered it: `nist 800-61 rev 3` had been aimed at the PICERL topic, and the DAIR topic's third card is about that revision. Before it came the twentieth wave's two: 4 queries for RASP and IAST added to *somebody revising for a CompTIA exam*, which opened at **0 of 4**, all zeros, and 11 for the CKA outline's gaps added to *a Linux or platform engineer*, which opened at **0 of 11**, seven zeros and four that found other cards. Both closed in full, 15 of 15, after two prose fixes that put the reader's form of a word in a card, `expired` beside the certificates and `throttling` beside the CPU limit; ten find their topic alone. The wave also pushed two old queries over the wide line, `i cannot install software` and `why do we use containers`, each to 61 by ordinary words in the new Kubernetes topics, and both now carry verdicts; the Docker card the second wants is still among its answers. Before them came the nineteenth wave's, 13 queries for MD-102's last three gaps, added to *a service desk engineer* before their topics. It opened at **0 of 13**, seven zeros and six that found other cards, `policy configuration agent` among them reaching 21 cards and none of them about Intune, and closed at 13 of 13 after two prose fixes: `vbs not running` is the name of Autopatch's own alert, which the Hotpatch card mentioned without naming, and `approval request expired` stopped at a governance card holding all three words until the approval card used Microsoft's status name, *Expired*. Six find their topic alone and seven among two to sixteen. Before it came the eighteenth wave's, 13 queries for four of MD-102's gaps, added to *a service desk engineer* before their topics. It opened at **0 of 13**, four zeros and nine that found other cards, `app control for business` among them reaching 34 cards and none of them about App Control, and closed at 13 of 13: eight find their topic alone and five find it among two to twenty. The old zero `the user says the file is gone` was answered by coincidence a second wave running, this time by the Microsoft 365 Apps topic's *the slow lane is gone*; the phrase was reworded, and the query's note now records that its words are common enough for this to recur. Before it came the seventeenth wave's, 13 queries for MS-102's last three Defender objectives, added to *a SOC analyst or defender* before their topics. It opened at **0 of 13**, eight zeros and five that found other cards, `alert policy email notifications` among them reaching fourteen cards and none of them about alert policies, and closed at 13 of 13: seven find their topic alone and six find it among two to fifteen. The wave also gave an old zero an answer it should not have had: `the user says the file is gone` reached the threat intelligence topic, which held *users*, *says*, *files* and *gone* in four unrelated sentences, and relaxation widened that one match to 33 cards. *A portal that is gone* became *a portal that no longer exists*, and the query is back to the zero its note records. Before it came the sixteenth wave's, 13 queries for MS-102's identity and Purview objectives, added to *a service desk engineer* before their topics. It opened at **0 of 13**, nine zeros and four that found other cards, and closed at 13 of 13 after one prose fix: `helpdesk admin for one office only` lacked only *office*, which is what the card's example of a region meant. The wave also took an old query's answer away for an hour. `bitlocker recovery key` had matched one card exactly and widened to the BitLocker topic; the administrative units card's *BitLocker recovery keys* made two exact matches, so search stopped widening, and the BitLocker topic, which said *recovery key* but never Microsoft's full name for it, dropped out. It says the full name in its table now. Before it came the fifteenth wave's, 13 queries for MS-102's Defender XDR objectives, added to *a SOC analyst or defender* before their topics. It opened at **0 of 13**, five zeros and eight that found other cards, `exposure score` among them reaching ten cards and none of them about Microsoft's product, and closed at 13 of 13: five find their topic alone and eight find it among two to eighteen. Before it came the twelfth wave's, 8 queries for the owner's packaging and error-code items, added to *a service desk engineer* before their topics. It opened at **0 of 8**, one zero and seven that found other cards, and closed at 8 of 8. The same topic gave an older question its target: `the software installed but does not appear`, recorded with none, now names the error-code topic, which says it in those words. Before it came the eleventh wave's, 8 queries for CISSP 1.6 and 7.15, added to *somebody revising for a CompTIA exam* before their topics. It opened at **0 of 8**, four zeros and four that found the wrong card, `cobit` among them reaching only the acronym dictionary, and closed at 8 of 8: five find their topic alone and three find it among two or three. Before it came the tenth wave's, 18 queries for six objectives four exam outlines had no topic for, added to *somebody revising for a CompTIA exam* before their topics. It opened at **0 of 18**, eleven zeros and seven that found the wrong card, `incident communication plan` among them reaching 23 topics and none of them a plan, and closed at 18 of 18: fourteen find their topic alone, and four find it among two to eight. Before it came the ninth wave's, 16 queries for the five A+ objectives the exam paths skipped, added to *somebody revising for a CompTIA exam* before their topics. It opened at **0 of 16**, ten zeros and six that found the wrong card, and closed at 16 of 16 with three `endpoint` topics and two in `hw`. Two closed in prose, each by the card saying what the reader asked in the reader's words: `windows 11 tpm requirement` once the card called them Windows 11's requirements, and `fat32 file size limit` once it named FAT32's file size limit. Before it came the sixth wave's, 10 queries for §4 rows 32 to 34, the quotes, added to *a learner meeting a subject* before their topics. It opened at **0 of 10**, all ten zeros, and closed at 10 of 10, with every line in the three topics read at its source first. Before it came the fifth wave's, 17 queries for *Content ideas* §4 rows 28 to 31 and 35, added before their cards to two readers that already ask about those subjects, *a learner meeting a subject* and *somebody looking for a job*. It opened at **0 of 17** and closed at 17 of 17: 14 zeros and 3 that found the wrong card, `active listening` among them through load balancers and nmap. One closed in prose, not a card: `depressed for weeks` needed the low-mood topic to use the reader's word. Before it came *a student on a theory course*, the second reader *Content ideas* §7.3 named: 15 queries for its fourth wave, seven rows, added before their cards. It opened at **0 of 15** and closed at 15 of 15: 8 zeros and 7 that found the wrong card, `segmentation fault` among them through network segmentation. Before it, the exam reader's third batch, 16 queries for the third wave, opened at **0 of 16** and closed at 16 of 16: 12 zeros and 4 that found the wrong card, `pivot table` among them through *pivot* and *table* in threat and grc cards. Its second, 23 queries for the second wave, opened at **0 of 23** and closed at 23 of 23: 16 zeros and 7 that found the wrong card, among them three that reached only the acronym dictionary and one an AI card that happens to contain *tone* and *probe*. Its first batch, *somebody revising for a CompTIA exam*, was added the same way for the first wave's five rows. It opened at **0 of 16** and closed at 16 of 16: 8 zeros and 8 that found the wrong card. Four of the zeros were words the site had never written, among them `scannow` and `pbq`, and `crc errors` reached a modular-arithmetic card. The wave also disturbed one old query: `the user has two accounts` sat on the wide threshold at 60 and went to 61, and it carried a verdict naming the gap underneath it until the eighth wave wrote that gap as its own topic, which the query now finds alone. The reader before it, *somebody looking up a character code or a handshape*, was added from a request for the ASCII character set with ASL added to it, before the card was written. It opened at **0 of 12** and closed at 12 of 12: five zeros, and seven that found cards but never the chart. `asl` was a zero the corpus counted fifteen times, every one inside another word: *asleep*, ASLR, Maslow, SASL. The reader before it, *a student with a data structures course*, was added from *csvistool* the same way. It opened at **0 of 16** and closed at 16 of 16, the first reader to open with nothing answered: eleven zeros, and five that find the wrong card. The one before that, *a student on a software engineering course*, was added from *Knowledge integration* the same way. It opened at 9 of 25 and closed at 25 of 25, and **nine of its first sixteen misses found cards, just not the right ones**: `logic gates` reaches pipeline gates and `multi core processor` the GDPR's data processor, the wrong-sense shape the last two queue sections found in chip subtitles and in *stack* and *queue*, counted here for the first time. Before that, *a student on a SQL Server and Java course* opened at 14 of 15 missing and closed at 15 of 15. The first two subject-shaped ones opened at a third missing; the ten symptom-shaped ones at **two thirds**, and that gap is the census's most repeated finding — batches seventeen and eighteen opened at 22 of 29 and 20 of 28 — the same two thirds twice more. Of the **22** zeros and **1** wrong-card, all are recorded verdicts. Two recorded zeros left that list by coincidence in the third wave, and their notes say so. `the user says the file is gone` matched the Windows tools topic with `user` found only inside the expansion of UDP, until the eighth wave stopped search matching inside expansions and it went back to zero, which is what a reader gets. `the usb ports on one side stopped working` matched a connector card's *wider on one side*, and relaxation added Motherboard Anatomy, which was half an answer until the eighth wave wrote the card it needed there. The 11 wide results are verdicts too, and all six of these numbers are checked against a live census by `query_probe.mjs --check-plan` — the row needs a browser, so the browser checks it. The staleness check reports a verdict that has stopped describing its row, and it has now caught two, both on a note of its own author's: the first time the note was right and the check was wrong — `\bzeros?\b` was matching *zero* inside **zero-touch** — and the second time the note was simply out of date, which is what it is for. The wrong-card one is kept on purpose: `the intern deleted the wrong thing` asks the site to contain a word it has no reason to contain, and writing one in is the keyword stuffing the census exists to refuse | `query_probe.mjs` |
| Learning paths | **126 paths, 2,542 steps, 1,579 of 1,639 topics, 0 hand-written topics off a path** | `check_paths.py` |
| Related links | **1,579 topics, 5,596 links, 0 one-way** — one mainland of **1,563 (98%)** and **one** island: `math`, 16 of 16, which is a decision rather than a backlog. It read *three reference-domain islands* until somebody measured how much of each island's domain was already connected — 29 of `shortcut`'s 36 and 3 of `quotes`' 6 — and `orphan_report.py` prints that figure now | `suggest_related.py --check` |
| Page budget | **21% raw** headroom — room for ~425 more topics | `page_budget.py` |
| Throttled load | **~3.0 s** = 0.5 s shell + 1.0 s script.js + ~190 ms/MB — *this container only* | `measure_load.mjs` |
| Search &amp; heap at 3x the content | **86 ms · 93 MB** at 4,602 indexed topics — search is not the constraint, load is | `measure_load.mjs --synthetic` |
| Depth tail | **10th percentile 2,313 chars**, median 3,957 — the number a deepening wave has to move | `depth_report.py` |
| Dated claims | **78 volatile spans and 556 fact anchors: 634 dated claims**, and **3** console candidates — all three read and recorded as false positives in `context()`'s docstring. The denominator is still not countable and that is Phase 11 §3's whole finding; the numerator always was, and spent a year in prose because nobody noticed the difference. It rose by two in the V2 pass, against §6's counter-discipline that a rising count is not automatically progress — both are limits a card **designs around**, which is the one case §5 says a span is right for, and the same pass rewrote nothing because the other ten claims were never facts about the world. It rose by eighteen with the csvistool deep links, one anchor per line of links, which is the rise csvistool §1 asked for: a route is a key in someone else's repository, and one rename there breaks it silently. It rose by one with the ASCII chart's source link, and that anchor records that this container could not fetch the page rather than claiming a check. It rose by one more with GCM's random-nonce limit in the cipher-modes card, and that anchor says the NIST figure was confirmed in search results and the PDF was not fetched. One more for Cisco's default administrative distances, said the same way, and two for the Windows repair ladder: Microsoft's DISM-before-SFC order and the two failed starts that open WinRE. And one for CompTIA's rule that a virtual PBQ cannot be skipped and returned to, which this container could not fetch from comptia.org and says so. Two more for Cisco's syslog defaults in the severity card: the trap level that ships as informational, and the two messages one interface going down produces, both confirmed in search results with the pages not fetched. Three more in the cabling and discovery cards, said the same way: the standard's preference for T568A, Cisco's rule that fixing speed and duplex turns Auto-MDI-X off, and the CDP and LLDP timers. One more for the Excel versions that have XLOOKUP, one for the A+ objective numbers behind the malware removal steps, one for the two exercise studies the header image's numbers were checked against, two in `cs` for ECC memory's code and the Mars Pathfinder mutex, and five in `military` for the transition programs, the 9-line, the date-time group and METT-TC, said the same way. The date-time group's anchor says that no source was found for it, which is what an anchor is for. Two in `mind` date the health services' two-week line and the COBRA trial, and one in `philosophy` records which translation the Epicurus quotation is from. Four in `quotes` record the pages each line was read on, fetched this time and not only searched. One more in `military` records where Boyd's line from Orient to Act was read about, and that both primary PDFs refused the fetch, and one in `blueteam` dates the Pyramid of Pain to Bianco in 2013 from a secondary overview, his post unread. One in `infra` records that an Enforced link moves to the end of processing, from Microsoft's pages as quoted in search, and one in `m365` that a rule setting the spam level to −1 cannot pass malware or high-confidence phishing, said the same way. Two in `infra`'s two-accounts topic date how sync matches a user and how long a deleted one can be restored, and three in `endpoint` date the edition differences, subscription activation, and the MBR, GPT and Windows 11 limits. Three in `hw` date the file systems' limits and support, NTFS permissions on copy and move, and Backblaze's SMART figures, which are from its 2016 data. Ten more in the tenth wave's six topics, all from search results with the pages not fetched: two in `linux` for dracut's `mkinitrd` wrapper and libvirt's open network mode, three in `threat` for ATT&CK's injection and side-loading numbers and Sysmon's events, three in `sec` for the DES search, the padding oracles and the side-channel papers, and two in `ops` for the NIS2 and Form 8-K clocks. Eleven more in the twelfth wave's two `endpoint` topics. Eight are from Microsoft's own pages, fetched and read — the Windows Installer, Intune and Configuration Manager error references, msiexec's switches, the Win32 content prep tool and both tools' app settings — and one from Inno Setup's documentation. Two are from search results and say so: NSIS's case-sensitive switch, whose manual page refused the request, and Intune's default return codes, which Microsoft's page says exist without listing them. Twenty-one more anchors and four spans in the fifteenth wave's four Defender topics, every anchor from a Microsoft page fetched and read, with the date Microsoft last updated it. The spans mark the console paths, where the portal is and where a setting lives, because those are what Microsoft renames, and the console count asked for them: it went from three to six when the topics landed and back to three when the spans did. Thirteen more anchors and two spans in the sixteenth wave's four topics. Twelve anchors are from Microsoft pages fetched and read; the thirteenth records IdFix's retirement from its own repository, beside the 404 that Microsoft's page about it now returns. One older anchor changed too: *One User, Two Accounts* had cited the July 2026 hard-match hardening from search results, and now says the sync-errors page was read. Sixteen more anchors and three spans in the seventeenth wave's three topics, every anchor from a Microsoft page fetched and read, among them the cmdlet reference that documents `Set-ProtectionAlert`'s `NotifyUser` as reserved for Microsoft's own use. The console count went from three to six when the topics landed, all three new ones naming the Defender portal, and back to three when the spans did, the same as in the fifteenth wave. Seventeen more anchors and two spans in the eighteenth wave's four `endpoint` topics, every anchor from a Microsoft page fetched and read; two record changes a deployment guide may predate, the Semi-Annual Enterprise Channel unified into Monthly Enterprise from Version 2606 in July 2026, and Windows Backup for Organizations renamed *Windows settings backup and restore*. Ten more anchors and three spans in the nineteenth wave's three `endpoint` topics, one of them recording the retirement dates of three Security Copilot agents from the agents' own pages, which Microsoft's overview of Copilot in Intune still lists. The console count went to four when the Copilot topic named the Intune admin center, and back to three with a span. Seventeen more anchors in the twentieth wave's four topics: two in `sec` from NIST SP 800-53's own catalog, read as the OSCAL JSON NIST publishes, one recording that SecurityX names RASP and IAST, one from OWASP, and thirteen in `devops` from kubernetes.io, among them the etcd page's fix of 27 October 2026 to its restore steps and the November 2025 notice retiring Ingress NGINX. Seven more in the twenty-first wave: six in the DAIR topic, from SANS's announcement of 15 September 2026, its poster of 13 October, NIST's page for SP 800-61 Revision 3 and GIAC's GCIH page, and one beside the PICERL card's corrected account of where its six steps came from. Eighteen more in the twenty-second wave's three `cloud` topics, every one from an AWS page fetched and read, among them two closures the SAA-C03 guide predates: Snowball Edge and FSx File Gateway are no longer available to new customers, and the guide's in-scope list still names the Snow Family. Twenty-two more in the twenty-third wave's five `cloud` topics, every one from an AWS page fetched and read, among them the AWS Quick guide's own history recording QuickSight's rename on 9 October 2025. Twenty-three more in the twenty-fourth wave's five `cloud` topics, all from AWS pages fetched and read, among them Application Discovery Service's closure to new customers on 7 November 2025 and SageMaker's rename to SageMaker AI on 3 December 2024. Fourteen more in the twenty-fifth wave's eight cards in six existing `cloud` topics and one new one, all from AWS pages fetched and read, among them gp3's ceiling of 80,000 IOPS and the rule that hibernation cannot be turned on after launch. Five more in the twenty-sixth wave's NAT card, among them AWS's regional NAT gateway, which spreads across zones by itself, and the NAT AMI's end of maintenance on 31 December 2023. Thirteen more in the twenty-seventh wave's three Google Cloud topics, from Google's pages fetched and read, among them the blog post of 21 August 2024 that renamed Cloud Functions. Twelve more in the twenty-eighth wave, two of them Google's notice that Deployment Manager's support ended on 31 March 2026 and its description of Infrastructure Manager. Ten more in the twenty-ninth wave's five cards in existing GCP topics, among them the 30-day default log retention and the charge for keeping logs longer, applied since 1 April 2023. Two more in the thirtieth wave's `ai` topics: SecAI+'s domain weights from CompTIA's exam page, and the date of NIST's adversarial machine learning taxonomy, AI 100-2 E2025, from NIST's publication page, both fetched and read. Five more in the thirty-first wave's three `ai` topics, all from pages fetched and read: OWASP's 2026 list of LLM risks twice, where the governance topic names it and where the security topic's table explains it; its 2023/24 and 2025 editions, for what changed between them; its agentic list; and the Commission's AI Act page, last updated 19 October 2026, for the dates the AI Omnibus moved. Five more in the thirty-second wave's two `ai` topics, all from NIST's own pages fetched and read: the AI RMF's seven characteristics and its four functions from NIST's AI Resource Center, the framework page's dates twice, where the ethics topic and the governance topic give them, and the Generative AI Profile's twelve risks from its PDF. Six more in the thirty-third wave's three OWASP topics, all from OWASP's pages fetched and read: the 2025 list three times, once in each topic that teaches it; the introduction's account of what changed since 2021; four category pages' details; and the foundation's about page for its current name. Four more in the thirty-fourth wave's three `grc` topics, all from NIST's CSF documents fetched and read: version 2.0's six functions twice, its 22 categories, and version 1.1's categories, for the names a list carried over from 2018. Two more in the thirty-fifth wave's two `blueteam` topics, both CompTIA's SecAI+ page, for the exam's words for what those topics already taught. Two more in the thirty-sixth wave's two `threat` cards, both from MITRE's ATT&CK pages fetched and read, for version 19's split of Defense Evasion. Two more in the thirty-seventh wave's post-quantum topic, both NIST's: IR 8547 as published in October 2026, read as its PDF, and the March 2025 release that chose HQC. Two more in the thirty-eighth wave's PKI topic: the CA/Browser Forum's Baseline Requirements 2.3.1 for the lifetime schedule, read as its PDF, and Let's Encrypt's two posts on ending OCSP. One more in the thirty-ninth wave's regulatory landscape topic, from the Commission's two pages on the Cyber Resilience Act. Two more in the fortieth wave: CIS's pages for the Controls' version and parts, and Microsoft's KB5073381 with its Kerberos guidance for the end of RC4 as a domain controller's default. Three more in the forty-first wave's *Package Management*, from Debian's apt-key(8) and sources.list(5) and DNF's configuration reference. Five more in the forty-second wave: three in `military`, two from FM 6-0 read as its PDF and one recording the Joint Staff's J-7 from search results, because jcs.mil refused the fetch; and two in `devops`, from NVD's record of CVE-2025-30066 and GitHub's pages on pinning actions and on workflow lockfiles. Four more in the forty-third wave: two in `data`, PostgreSQL's documentation on how nulls sort and a record of the queries run on PostgreSQL 16 that fill the card's table; one in `web` from RFC 9110 and RFC 6585; and one in `eng` from six certification bodies' renewal pages, all fetched and read. The forty-fourth wave re-checked the twelve claims last checked in August, the oldest on the site, and found seven that had moved or were wrong. It re-dated eleven, removed one span, a used-hardware price no authority publishes, and added nine anchors, each saying what its claim was checked against: Microsoft's pages for gMSA passwords, shared mailboxes, message trace, holds and the What If tool; NIST's SP 800-57 PDF; the eCFR; Fortinet's product matrix; LangChain's and LlamaIndex's own pages; and Raspberry Pi's price posts. The forty-fifth wave re-checked the twenty-two `m365` claims from September, re-dated all of them and added nine anchors: the admin consoles' addresses, requested one by one, and Microsoft's pages for quarantine, SharePoint's limits, group expiry, Graph batching and guest access. The forty-sixth wave re-checked the seventeen `endpoint`, `infra` and `cloud` claims from September, re-dated them, replaced six anchors' secondhand sources with the owners' pages and added four. The forty-seventh wave re-checked September's last twenty-six claims, eighteen of them csvistool routes, confirmed against the live site's own bundle because its repository is outside this session's GitHub scope; it added three anchors, and no claim on the site is now older than October. The forty-eighth wave read the one October claim's page, a link an earlier container could not fetch, and every dated claim on the site has now been checked this month. The forty-ninth wave redid Phase 11's tier-gating pass against Microsoft's own pages and added three anchors, one per licensing claim it corrected or confirmed. The fiftieth wave added eight beside the product names it corrected, each from the owner's page: Google's for Deployment Manager's end, the SecOps rebrand and Google Cloud Observability, AWS's for Security Hub CSPM, HashiCorp's for HCP Terraform, and Microsoft's for Configuration Manager's name and release cadence, App Control for Business and the PowerShell modules' retirement. The fifty-second wave added two beside the comparison-table cells it corrected: Microsoft's retirement notice for Azure CDN (classic) and Google's page on cost anomaly detection. The fifty-fourth wave added one beside the certification roadmap, from Microsoft's credentials roundup and the certification pages for AZ-500, MS-102, SC-500 and AB-650. The fifty-sixth wave's Copilot settings topic added six anchors and two spans, every anchor from a Microsoft page fetched and read: the settings page, web search, the AI providers' terms, Cowork, Copilot Search and connectors, and the spans on the two menu paths a rename would move. The fifty-seventh wave's agents topic added four anchors and a span, from Agent 365's overview, the agent registry, Entra's governance of agent identities and Conditional Access for agents. The fifty-eighth wave added eight and a span: seven in its topic on running Copilot, from Microsoft's pages on usage-based billing, spending policies, monitoring spend, the usage report, Copilot controls, the AI disclaimer and release options, and one beside the licensing table's new E7 row. The fifty-ninth wave added five anchors and a span in two cards, from Microsoft's pages on SharePoint Advanced Management, Restricted Content Discovery, Restricted SharePoint Search's retirement, DLP for Copilot and DSPM for AI; the span is on the SharePoint admin center, which the console census counted as a fourth candidate until it was dated. The sixtieth wave added three anchors and two spans in AB-650's last three cards, from Microsoft's pages on Microsoft 365 Backup, Copilot in Teams meetings and network connectivity; one span went on the admin center the Backup card names, the census's fourth candidate a second time. The sixty-second wave added three in its topic on read-only domain controllers and domain controllers in Azure, from Microsoft's security groups reference, its RODC installation page and the Azure Architecture Center. The sixty-third wave added three in its Azure File Sync card, from Microsoft's pages on Azure Files, Azure File Sync and cloud tiering. The sixty-fourth wave added four in its Hyper-V card, from Microsoft's pages on PowerShell Direct, nested virtualization, checkpoints and Hyper-V Replica. The sixty-fifth wave added three in two storage cards, from Microsoft's pages on Storage Spaces Direct, Storage Replica and SMB over QUIC. The sixty-sixth wave added five in its server-hardening topic, from Microsoft's pages on Credential Guard, the Protected Users group, the Windows Server 2025 security baseline, Defender for Servers and exploit protection; the row's sentence for it was missed then and written in the sixty-seventh. The sixty-seventh wave added nine anchors and a span: two in a SmartScreen card, from Microsoft's SmartScreen overview and its settings page, and seven in its monitoring topic, from Microsoft's pages on logman, `logman create counter`, Windows Admin Center's server tools, System Insights and managing it, data collection rules and monitoring Azure VMs. The span is on Windows Admin Center, a name the console census matches. The sixty-eighth wave added three in its card on reaching Azure VMs, from Microsoft's pages on just-in-time VM access, Azure Bastion and Bastion's configuration settings. The sixty-ninth wave added four in its Hyper-V hardware card, from Microsoft's pages on enhanced session mode, Discrete Device Assignment and GPU partitioning, and the Azure Local host network page that its Windows Server docs link for Switch Embedded Teaming. The seventieth wave added three in three cards, from Microsoft's pages on SMB Direct, Storage Quality of Service and managing Windows Firewall from the command line. The seventy-first wave added one in its second-hop card, from the PowerShell team's page on the second hop. The seventy-second wave added five in its card on the Hyper-V VM's own settings, from Microsoft's pages on creating a virtual switch, Hyper-V's overview, `New-VHD`, integration services and `Set-VMMemory`. The seventy-third wave added two, one in each of its cards, from Microsoft's pages on delegating administration through OUs and on DNS policies. The seventy-fifth wave added three anchors and two spans in MD-102's device-operations cards, from Microsoft's pages on BitLocker with Intune, custom compliance and the troubleshooting dashboard; the spans date the two console paths the cards name. The seventy-sixth wave added two in its enrollment cards, from Microsoft's pages on enrollment time grouping and Samsung Knox Mobile Enrollment. The seventy-seventh wave added four anchors and a span in its specialty devices card, from Microsoft's pages on Teams Rooms' supported policies, Windows Holographic, Zebra's Mobility Extensions and Zebra LifeGuard Over-the-Air; the span dates the connector's console path. The eightieth wave added six anchors and a span in its Defender for Cloud topic, from Microsoft's pages on Defender for Cloud, its two CSPM plans, regulatory compliance, and Defender for Storage, Key Vault and AI threat protection; the span dates the move into the Defender portal, which a fact anchor had named first and the console census counted. The eighty-first wave added seven anchors and a span: six in its Microsoft Sentinel topic, from Microsoft's pages on Sentinel's roles, its content, syslog and CEF through the Azure Monitor agent, automation rules, and tables, tiers and retention, and one in *Azure Security*'s Sentinel card, where the tiers it named were out of date; the span dates the end of Sentinel in the Azure portal on 31 March 2027. The eighty-second wave added five anchors and three spans in its topic on securing AI workloads in Azure, from Microsoft's pages on the AI gateway in API Management, configuring a gateway for Foundry, Foundry's guardrails, Copilot Studio's external threat detection and the Data and AI security dashboard; the spans date how Foundry now reaches API Management, the guardrails still in preview with groundedness detection's retirement on 30 April 2027, and the Power Platform admin center path for Copilot Studio's threat detection. The eighty-third wave added six in two cards: four in *Azure Networking*, from Microsoft's pages on Virtual Network Manager, its security admin rules, the secured virtual hub and Virtual WAN's routing intent, and two in *ZTNA*, from its pages on Entra Private Access and Quick Access. The eighty-fourth wave added two anchors and a span: one in *Azure Compute &amp; Storage*'s trusted launch card, from Microsoft's trusted launch page, and one in *Azure Arc*'s Machine Configuration card, from its overview, where the span dates the Linux upgrade that page announces for November 2026. The eighty-fifth wave added five in two cards: three in *Azure Databases*' auditing card, from Microsoft's pages on SQL Database auditing, server- and database-level policies and Managed Instance auditing, and two in *Azure Compute &amp; Storage*'s access policies card, from its pages on stored access policies and shared access signatures. The eighty-sixth wave added one anchor and a span in *Microsoft Intune*'s device query card, from Microsoft's device query page, at its new address under Intune's advanced analytics; the span dates where the admin center puts it. The eighty-eighth wave added five in its Azure Backup and Site Recovery topic, from Microsoft's pages on Azure Backup, the Recovery Services vault and the Backup vault, Azure Backup's security and cyber recovery, and Site Recovery. The eighty-ninth wave added four in two cards: two in *Azure Compute &amp; Storage*'s blob data protection card, from Microsoft's data protection overview and its object replication page, and two in *File Services*' Azure Files card, from its pages on share snapshots and share soft delete. The ninetieth wave added four in three cards: one for the storage firewall's network rules and two for AzCopy and Storage Explorer in *Azure Compute &amp; Storage*, and one for Azure Files' identity-based access in *File Services*, all from Microsoft's own pages; Storage Explorer's anchor says its page still carries a 2019 date while describing 2026 releases. The ninety-first wave added four in *Azure Monitor, Log Analytics &amp; KQL*'s alerting card, from Microsoft's pages on alert types, action groups, alert processing rules and Connection monitor. The ninety-second wave added four in two cards: two in *Azure Networking*'s Azure DNS card, from Microsoft's DNS overview and its Private DNS page, and two in *Cloud Cost Control*, from its budgets tutorial and the Advisor introduction. The ninety-fourth wave added three in two `m365` cards: two in *Admin Roles &amp; Least Privilege*'s card on narrowing a role, from Microsoft's pages on PIM for Groups and protected actions, and one in *External Collaboration*'s card on its own tenants, from its page on cross-tenant synchronization. The ninety-fifth wave added three in two `sec` cards: two in *Multi-Factor Authentication*, from Microsoft's overview of certificate-based authentication and its page on registration campaigns, and one in *ZTNA*, from its page on publishing apps with Application Proxy. The ninety-sixth wave added three in two cards: one in `cloud`'s *Azure Hierarchy, RBAC Scopes &amp; Policy*, from Microsoft's page on custom security attributes, and two in `m365`'s *Entra ID Governance*, from its pages on terms of use and connected organizations. The console count went to four when that card's table named the admin center, and back to three when the cell was reworded, since where an administrator clicks was not the point. The ninety-seventh wave added two, one in `m365`'s *Secure Score &amp; the Tenant Baseline*, from Microsoft's page on the Identity Secure Score, and one in `cloud`'s *Entra ID — Sign-In &amp; Conditional Access Troubleshooting*, from its page on the provisioning logs. The ninety-ninth wave added four in `m365`'s *Defender XDR Incidents &amp; Advanced Hunting*: three from Microsoft's pages on automatic attack disruption, case management and Security Copilot in Defender, and one in the topic's automated investigation card, from two Defender for Endpoint pages that record a change the Defender XDR overview does not yet mention, automated investigation and response no longer running as a separate investigation experience from 1 September 2026. The hundredth wave added four in two `endpoint` cards in *Defender for Endpoint &amp; Intune*, from Microsoft's pages on response actions on a device, live response, device groups and automation levels; the response actions anchor records that its page still lists starting an automated investigation by hand. The hundred-and-first wave added two in `blueteam`'s *Windows Event Logs*, from Microsoft's page on Windows Event Forwarding and Sentinel's data connector reference. The hundred-and-second wave added four in two cards in `cloud`'s *Microsoft Sentinel*, from Microsoft's pages on threat detection, threat intelligence, custom tables and SOC optimization. The hundred-and-third wave added five: four in `blueteam`'s *Threat Hunting — Assume Breach, Go Looking*, from Microsoft's pages on the hunting graph, the Sentinel graph, Jupyter notebooks and Sentinel's MCP server, and one in `m365`'s *eDiscovery, Content Search &amp; the Audit Log*, from its page on Microsoft Graph activity logs | `check_volatility.py` |
| Gates | **45**, and the same 45 in `make all` and in CI | `check_gates.py` |
| Gate results | check · smoke **167** · search **59** · resilience **64** · axe 33/33 · mobile 16/16 · visual 2/2 · backup 3/3. The error-code lookup added one check to each of smoke, mobile and axe's two themes, and the expand switch one to smoke. Visual is 0/2 in the container that ran the last session, and that is not a regression: its Playwright is 1.63.0, whose Chromium 153 draws the chip labels about 10% wider than the 1.56.0 CI pins (Chromium 141), and CI matched the same baselines 2/2 on 2026-10-11. `visual_test.mjs` names both versions now, and refuses `--update` under any Playwright but the pinned one | `make all` |
| Cards ending on a table with no verdict | **10**, all deliberate lookup tables in `military` — two of the original twelve turned out to have a judgement their table was carrying silently | `lint_content.py` |
| Session records | **71** here, **377** in `plan-archive.md` | `check_plan_numbers.py` |

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
| 10 | Three wrong acronym expansions shipped in earlier sessions and were found by **reading**, not by any check — `IR` in a compiler card's title, `SMB` in "a home-lab / SMB choice", and `DAG` in the Exchange Server topic's title, expanded as a directed acyclic graph | The breadth census now surfaces the candidates. It cannot decide them |

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
| **Product names** | Rebranded — `check_renames.py` already guards a list of these | Everywhere; the guard exists and catches the ones it knows, and §10 is what the fiftieth wave found it knew |

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
| **V6** | Product names | Added by §10. Read the site for old names, re-check `data/renames.json`'s current names against their owners' pages, and register every rename or closure a wave finds in the commit that records it |

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

## 9. What re-checking found that reading did not

§7 and §8 read the classes and judged the site disciplined: thirty claims examined, two actionable. Waves 44 to 48
then re-checked every dated claim against its owner's current page, and the yield was different in kind. **Of 78
claims re-checked, 14 had moved or were wrong**, and when wave 49 redid V1 the same way, two of the three tier-gating
claims it checked needed correcting. Reading asks whether a claim is the kind that ages; re-checking asks whether it
is true today, and only the second question finds a wrong one.

Two of the findings correct this phase's own advice.

**§5's rewrite can be wrong too.** *Holds generally require the enterprise tier* was written in §5's style, and §7
held it up as the model. It was false: Business Premium has Litigation Hold, and so do the cheaper plans with an
add-on. A rewrite that softens a fact still asserts it. The rule is to remove the dependency, not to blur it: *check
which of your plans includes holds* makes no claim, and *the enterprise tier* does.

**The vague claims did not age better than the precise ones.** Roughly half of the fourteen were precise claims the
world moved under: a price, a console address, a menu path, a framework's structure, a retention default. The other
half had overstated from the day they were written: *the enterprise tier*, *most platforms*, *any modern domain*, *the
whole mechanism*. A vague claim is harder to falsify, which is not the same as more likely to be right.

So the standing discipline gains a step. Reading a class finds the claims; re-checking each against its owner's page
is what finds the wrong ones, and `check_volatility.py`'s oldest-first list is the order to do it in.

## 10. The guard's own names were dated claims

§4 listed product names, and §6 never gave them a wave, because `check_renames.py` already guarded the class. The
fiftieth wave read it anyway, then re-checked what it read the way §9 says, and found the guard was two things that age.

**Its list had stopped growing.** Twenty-seven renames were on record, the newest from October 2025. A census of 330
candidate names and version strings, written from memory and matched in prose with the guard's own rule for what counts
as explained, found eight still used as though current, in seventeen topics. Two of them the site had already recorded
as changed somewhere else: Deployment Manager's retirement had its own topic from the twenty-eighth wave, and the App
Control topic of the eighteenth said what WDAC is called now. The tables that named them in passing never heard. A
rename written into one topic does not travel. The registry is what makes it travel, and the waves that found renames
had stopped adding them to it.

**Its current names had aged.** Each entry's `new` is a claim that a name is current, and nothing re-checked those
claims. The wave checked four, and all four were wrong, though each was checked because something had flagged it. Two
gave MECM's generation of names as current, four years after Microsoft moved on. Facebook Workplace's pointed at a
product that closed in May 2026. Docker Swarm mode's ran backwards, from the name Docker uses to the one it retired, and
could never fire, because the old name contains the new one. A guard with wrong data does worse than a missing one: it
offers the stale name as the fix. The fifty-first wave re-checked the other twenty-three, and every one held: the
wrong entries were exactly the ones something had already flagged. §57 has the likely reason.

So the class gets its wave after all, and it is §9's discipline turned on the guard: read the site for old names,
re-check the registry's current names against their owners' pages, and give the registry every rename a wave finds in
the same commit as the card that records it. The registry can now hold a closure as well as a rename, which is what
most of the waves' findings were.

## 11. Claims that announce their own expiry

§3 found no property that marks an ageing claim. There is a narrower one that can be required: a sentence in the
future tense about a year already reached, a deadline (*until*, *through*, *by*) in such a year, or a state that ends,
a preview, a *coming soon*, a *latest*. `check_volatility.py --expiry` reports those sentences, and the fifty-third
wave read every one. Fourteen came back. Ten were real claims, among them Deployment Manager's end, Ingress NGINX's
last maintenance, three agents in preview, the DSM's next edition and the TLS lifetime schedule, and all ten were right
and carried fact anchors checked this month. The other four were examples, a rhetorical *don't judge it by 2005*, and
a generic *latest version of an app*.

So the class a pattern can find is the class a careful writer already dates: a sentence that names its own deadline
invites the date beside it. The report is cheap and worth running with each dated-claims pass, because a claim of this
shape written undated would be the easiest error on the site to catch. It is not where the errors were. §9's fourteen
were defaults, limits, menu paths and overstatements, and none of them announced when it would expire.


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
| **The plan outgrows its own readability** — 11,600 lines, and the useful part is the last few hundred | `check_plan_numbers.py` reports the live file past **8,000 lines** | ✅ **Closed, reopened, and closed again.** Option 3 shipped, then option 1 at 22,745 lines by somebody noticing. The condition then fired on its own at **8,020**, and option 1 ran again — 45 records moved, 8,020 → 4,227, lines conserved. It fired a third time at **8,009**, and the same move took the file to 4,092. It fired a fourth time at **8,044**, in the seventy-ninth wave, and moving the oldest 45 records took it to 5,486. **The reopen condition is the only part of this register that has ever been tested, and it worked** |

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

## 23. What shipped — the seventeenth wave

Recorded below as *Session — the seventeenth wave, MS-102's last Defender objectives and a portal that
retired*. The three Defender XDR items §21 found, each from Microsoft's own pages, fetched and read
before any card. With them every gap §20 and §21 listed for MS-102 has a topic.

| § | Item | Where it went |
|---|---|---|
| 21 | Restricted entities, including blocked users | `m365` *Restricted Entities &amp; Outbound Spam — Why a Mailbox Stops Sending, and Unblocking It Safely*: the limits and the 5.1.8 bounce, Microsoft's order for securing the account before unblocking it, and the connector and tenant restrictions with the bounce code for each |
| 21 | Alert policies in Defender for Office 365 | `m365` *Alert Policies in Defender for Office 365 — The Default Alerts, Who Gets Them &amp; Writing Your Own*: the three ways a policy fires and what each needs, the defaults that signal a taken-over mailbox, and the forwarding-rule alert's blind spot for rules made in Outlook itself |
| 21 | Defender Threat Intelligence | `m365` *Defender Threat Intelligence — Threat Analytics, Intel Explorer &amp; What a Reputation Score Means*: **the standalone portal retired on 1 August 2026**, threat analytics reports tab by tab, and the reputation score's four bands |

**Each went onto the MS-102 path** at its objective, which now has 35 steps, and onto *Administering
Microsoft 365*: restricted entities after *Message Trace*, and alert policies and threat intelligence on
either side of *Defender XDR Incidents*, the order they have on the page.

**A third outline behind its product.** MS-102 asks for *Microsoft Defender Threat Intelligence*, by that
name. Microsoft's page for it now describes *Threat intelligence* in the Defender portal, and the Intel
explorer page says the standalone portal and its Intel Explorer were retired on 1 August 2026. AZ-800
had retired as an exam and IdFix as a tool; this is a product renamed into a page of another.

**Two things the pages said that a card had to carry.** The default *Creation of forwarding/redirect
rule* alert watches rules made in Outlook on the web or PowerShell only, and the audit log files a rule
made in the Outlook client under another operation, so a custom policy is the only alert on it. And the
recipients of a default alert are changed in the portal: the cmdlet parameter that looks like it does
that is documented as reserved for Microsoft's own use.

**Also fixed.** `DAG` in *Exchange Server On-Prem*'s title was expanded as a directed acyclic graph,
found while reading the m365 topic list for this wave. It has its Exchange meaning there now, scoped
to `m365` in the dictionary, and keeps the graph meaning in the Airflow card that uses it that way.

**The queue.** MD-102's seven: deploying Microsoft 365 Apps with the Office Deployment Tool, Windows
Backup for organizations, Delivery Optimization, App Control for Business, Hotpatch, multi-admin
approval, and Security Copilot agents in Intune. Then CKA, OSCP, GCIH, AWS, GCP and AI+, RASP and
IAST, and the visual baseline.

## 24. What shipped — the eighteenth wave

Recorded below as *Session — the eighteenth wave, four MD-102 gaps, a renamed feature and a merged
channel*. Four of §20's seven MD-102 gaps, each from Microsoft's own pages, fetched and read before any
card, all in `endpoint`.

| § | Item | Where it went |
|---|---|---|
| 20 | Microsoft 365 Apps with the Office Deployment Tool | *Microsoft 365 Apps Deployment — The Office Deployment Tool, Intune's App Type &amp; Update Channels*: the configuration file and its three modes, Intune's app type and why Autopilot wants Office wrapped as Win32, **the Semi-Annual Enterprise Channel unified into Monthly Enterprise in July 2026**, and Cloud Policy |
| 20 | Windows Backup for organizations | *Windows Backup for Organizations — Settings Restore on a New PC, and What It Leaves Behind*: what the backup holds and what it does not, the two restore switches and which devices each reaches, and five privacy policies that silently turn backup off. **Renamed *Windows settings backup and restore***, and on by default from Windows 11 26H2 |
| 20 | Delivery Optimization | *Delivery Optimization — Download Modes, Peer Groups &amp; Where Windows Gets Its Updates*: what it downloads, the download modes and who counts as a peer, and the four causes of zero bytes from peers |
| 20 | App Control for Business | *App Control for Business — Managed Installers, Audit Mode &amp; the AppLocker Policy That Can Stop Sign-In*: against AppLocker, the managed installer and the AppLocker merge Microsoft warns can stop sign-in, and the built-in controls in audit first |

**Each went onto the MD-102 path** at its objective, which now has 42 steps, and onto *Endpoint
Engineering with Intune*: backup after the ESP, Office after Store and catalog apps, Delivery
Optimization after Autopatch, and App Control after local admin rights.

**A renamed feature and a merged channel.** MD-102's outline, skills measured as of 27 October 2026,
says *Windows Backup*, and Microsoft's documentation now calls the feature *Windows settings backup and
restore*, warning that the old name will linger on some pages and policies during the change. And the
Semi-Annual Enterprise Channel, the slow lane Office deployment guides have long recommended for tested
devices, became Monthly Enterprise from Version 2606 in July 2026 without any administrator changing a
policy. Microsoft's own channel overview, last updated in May, still tabulates it with features twice a
year, under a banner announcing the change. Neither makes the outline wrong; both can make a guide
written before them wrong.

**The queue.** MD-102's other three: Hotpatch, multi-admin approval, and Security Copilot agents in
Intune. Then CKA, OSCP, GCIH, AWS, GCP and AI+, RASP and IAST, and the visual baseline.

## 25. What shipped — the nineteenth wave

Recorded below as *Session — the nineteenth wave, MD-102's last gaps and three agents that retired*.
The last three of §20's MD-102 gaps, each from Microsoft's own pages, fetched and read before any card,
all in `endpoint`. With them every gap §20 listed for both Microsoft outlines has a topic.

| § | Item | Where it went |
|---|---|---|
| 20 | Hotpatch | *Hotpatch — Security Updates Without a Restart, and the Quarterly Baselines That Still Need One*: the eight-and-four calendar, the requirements a device must meet or quietly restart instead, and Microsoft's six troubleshooting steps |
| 20 | Multi admin approval | *Multi Admin Approval — A Second Administrator Before a Wipe, a Script or a Role Change*: what an access policy holds, the request that the requestor has to complete after approval, and the approver group that fails without saying so |
| 20 | Security Copilot agents in Intune | *Security Copilot in Intune — Copilot, the Agents, and the Three That Retired in 2026*: Copilot as Security Copilot with the asker's permissions, **three of the four agents retired in 2026**, and the one left, which ignores scope tags in preview |

**Each went onto the MD-102 path** at its objective, which now has 45 steps, and onto *Endpoint
Engineering with Intune*: Hotpatch after Autopatch, the agents after Endpoint Analytics, and approval
after RBAC and scope tags.

**An outline asking for tools that are gone.** MD-102's outline, skills measured as of 27 October 2026,
asks candidates to investigate threats identified by Security Copilot agents in Intune, to analyze
device performance with them, and to respond to their recommendations. Microsoft's own pages say the
Device Offboarding Agent was removed on 1 June 2026 and the Policy Configuration and Change Review Agents
on 31 August, which leaves the Vulnerability Remediation Agent, in preview; none of the four was about
device performance. Microsoft's overview of Copilot in Intune, last updated in May, still lists all four.
It is the fourth case in six waves of an outline or overview behind its product.

**Also added.** `VBS` to the acronym dictionary, as Virtualization-Based Security: the Hotpatch card
needed it, and a `redteam` card had been using it unexpanded.

**The queue.** Every Microsoft gap is written. What remains is the older list: the header tags no
outline has been read for, CKA, OSCP, GCIH, AWS, GCP and AI+, then RASP and IAST, and the visual
baseline.

## 26. What shipped — the twentieth wave

Recorded below as *Session — the twentieth wave, RASP and IAST, a CKA path, and a controller that
retired*. §19's RASP and IAST, and the first of the header tags with no outline read, CKA, whose outline
the Linux Foundation publishes on its exam page.

| § | Item | Where it went |
|---|---|---|
| 19 | RASP and IAST | `sec` *IAST &amp; RASP — Testing and Defending an Application From Inside It While It Runs*: both as instrumentation inside the running application, IAST's sensors and what they see, and RASP against a firewall, from NIST SP 800-53's controls SA-11(9) and SI-7(17) and OWASP's guideline |
| 20 | A path for CKA | *Linux Foundation CKA (Certified Kubernetes Administrator)*, 15 steps, in the order of its five domains, read from the Linux Foundation's exam page for Kubernetes v1.37 |
| — | CKA gap: cluster lifecycle | `devops` *kubeadm Cluster Lifecycle — Upgrading One Minor at a Time, Renewing Certificates &amp; Backing Up etcd*: the upgrade order and why the skew policy fixes it, the one-year certificates that upgrades renew, and etcd snapshots, with the restore step Kubernetes' page fixed on 27 October 2026 |
| — | CKA gap: scheduling | `devops` *Scheduling &amp; Autoscaling — Requests and Limits, Taints, Tolerations, Affinity &amp; the HPA* |
| — | CKA gap: traffic and names | `devops` *Ingress, Gateway API &amp; CoreDNS — Getting Traffic In, and the Controller That Retired*: **Ingress NGINX retired in March 2026**, the Gateway API's three roles, and DNS debugging from inside a Pod |

**Every CKA competency now has a topic.** The outline's five domains map onto the site's existing
Kubernetes topics except for the three above: nothing on the site mentioned kubeadm, tolerations, etcd
backup, version skew, static Pods, the HorizontalPodAutoscaler or CoreDNS before this wave. The three went
onto *Kubernetes, End to End* as well, and IAST and RASP onto *Application &amp; API Security*.

**A recommendation corrected.** Two `devops` tables named nginx as an example Ingress controller. The
community Ingress NGINX project stopped receiving fixes in March 2026, and Kubernetes recommends the
Gateway API, so both now say so.

**The queue.** OSCP, GCIH, AWS, GCP and AI+, the header tags still without a path, and the visual
baseline. GitHub's web pages refused this container (403), so outlines published only there need
another source.

## 27. What shipped — the twenty-first wave

Recorded below as *Session — the twenty-first wave, GCIH, DAIR, and a lifecycle NIST retired*. The
second header tag with no outline read, GCIH, whose objectives GIAC publishes on its certification page.

| § | Item | Where it went |
|---|---|---|
| 26 | A path for GCIH | *GIAC GCIH (Certified Incident Handler)*, 23 steps, its fifteen objectives in working order rather than GIAC's alphabetical one |
| — | GCIH gap: DAIR | `ops` *DAIR — SANS's Dynamic Approach to Incident Response, and the Loop That Replaced the Line*: PICERL against DAIR's waypoints, the Response Actions Loop and its signed exit, and where it sits beside NIST's 2025 revision |

**Every GCIH objective but one already had a topic.** Fourteen of the fifteen map onto topics in `blueteam`,
`redteam`, `sec`, `cloud`, `ai`, `infra` and `ops`. The fifteenth asks for PICERL and DAIR, and nothing on
the site had mentioned DAIR, which SANS published as a book on 15 September 2026.

**Two statements corrected.** The PICERL card said NIST SP 800-61 *defines* four phases and that
CompTIA expanded them to PICERL; NIST superseded that revision with Revision 3 in April 2025, and the six
steps were SANS's own original process, which SANS's announcement of DAIR names as the one it replaces.
The second incident response topic called the four-phase lifecycle *the industry standard*. Both now say
what replaced what, with a fact anchor beside the first.

**The queue.** OSCP, AWS, GCP and AI+, the header tags still without a path, and the visual baseline.
AWS splits its exam guide across several pages and Google's guide renders by script, so both need their
documents read page by page.


## 28. What shipped — the twenty-second wave

Recorded below as *Session — the twenty-second wave, SAA-C03, and two AWS services closed to new
customers*. The third header tag with no outline read, AWS, whose SAA-C03 exam guide AWS publishes across
several pages, one per domain.

| § | Item | Where it went |
|---|---|---|
| 27 | A path for SAA-C03 | *AWS Certified Solutions Architect – Associate (SAA-C03)*, 35 steps, in the order of its four domains, ending on the Well-Architected Framework |
| — | SAA-C03 gap: application integration | `cloud` *AWS Application Integration — SQS, SNS, EventBridge &amp; Step Functions*: standard and FIFO queues and the visibility timeout, dead-letter queues and the retention clock a standard queue does not reset, and fanout, routing and orchestration side by side |
| — | SAA-C03 gap: data ingestion and analytics | `cloud` *AWS Data Ingestion &amp; Analytics — Kinesis, Firehose, Glue, Athena &amp; EMR*: stream consumers against queue consumers, Firehose's buffering as a latency setting, and when serverless analysis should give way to a cluster |
| — | SAA-C03 gap: hybrid storage and transfer | `cloud` *AWS Hybrid Storage &amp; Data Transfer — Storage Gateway, DataSync, Transfer Family &amp; the Devices That Closed*: the gateway types by the protocol the old system speaks, DataSync against Transfer Family, and the arithmetic behind shipping data instead of sending it |

**Every SAA-C03 task now has a topic; not every service it names does.** The guide's four domains map
onto the site's AWS, networking, architecture and cost topics, except where it names services nothing on
the site had mentioned: SQS, SNS, EventBridge and Step Functions under application integration; Kinesis,
Firehose, Glue, Athena and EMR under analytics; and Storage Gateway, DataSync, Transfer Family and the Snow
Family under storage and transfer. The path also takes in eight topics from outside `cloud`, among them
WAF and DDoS for the first domain and columnar formats for the third, whose task 3.5 asks for *.csv to
.parquet*. Seven services the guide names still appeared nowhere on the site when searched for by name:
Amazon Cognito and AWS Shield in task 1.2, RDS Proxy in 2.2 and 3.3, AWS Global Accelerator in 3.4, AWS
Lake Formation and Amazon Quick in 3.5, and AWS Backup in the in-scope list. That search was of a list of
names, not of every example the guide gives, and this paragraph first said it was; the twenty-third wave
checked every example and found more, which §29 records.

**Two services the guide still lists are closed.** AWS's own pages say Snowball Edge and FSx File Gateway
are no longer available to new customers; existing customers keep them. The guide's in-scope list still
names the Snow Family. The card teaches what the exam asks, data over bandwidth against a courier, and
names what AWS points new accounts to instead.

**The queue.** The seven SAA-C03 example services above, then OSCP, GCP and AI+, the header tags still
without a path, and the visual baseline. Google's exam guide renders by script, so its outline needs
another source, such as the guide's PDF.

## 29. What shipped — the twenty-third wave

Recorded below as *Session — the twenty-third wave, seven services the exam names and a dashboard with
three names*. §28's queue: the services SAA-C03 gives as examples that nothing on the site mentioned.

| § | Item | Where it went |
|---|---|---|
| 28 | Cognito | `cloud` *Amazon Cognito — User Pools, Identity Pools &amp; the Two Questions They Answer*: who the user is against what they may touch in AWS, the three tokens and why decoding one is not verifying it, and guest credentials scoped as if public |
| 28 | Shield and Global Accelerator | `cloud` *AWS Shield &amp; Global Accelerator — DDoS Protection and Fixed Entry Points at the Edge*: Standard and where the perimeter sits, Advanced protecting only what you add, and Global Accelerator against CloudFront in AWS's own words |
| 28 | RDS Proxy | `cloud` *RDS Proxy &amp; ElastiCache — What Sits Between an Application and Its Database*: pooling and pinning, lazy loading and write-through with a TTL, and proxy, replica or cache chosen by symptom |
| 28 | AWS Backup | `cloud` *AWS Backup — Plans, Vault Lock &amp; the Air-Gapped Copy an Attacker Cannot Delete*: plans assigned by tag, Vault Lock's two modes, and the logically air-gapped vault |
| 28 | Lake Formation and Amazon Quick | `cloud` *Lake Formation &amp; AWS Quick — Governing the Data Lake and Showing What Is In It*: grants on catalog objects, data filters and LF-Tags, and QuickSight's rename |

**The seven are covered, and the count that found them was incomplete.** The twenty-second wave searched
the site for a list of names. This wave took every example the four domain pages give, 154 phrases, and
searched for each service among them. Seven more task-statement examples appear nowhere on the site: Amazon
Comprehend and Amazon Polly in task 2.2, AWS Batch in 3.2, Provisioned IOPS in 3.3, Requester Pays and the
Cost and Usage Report in 4.1, and the Gateway Load Balancer in 4.2. The in-scope list adds Amazon MQ,
AppFlow, Amazon MSK, Kinesis Video Streams, Application Discovery Service, Client VPN and the
Well-Architected Tool. Systems Manager looked absent and is not: one card names its Parameter Store. Both
AWS paths take the five, and *AWS, End to
End* takes the twenty-second wave's three as well, which it had been missing, so it runs from 19 steps to
27 in the same order it had: account, identity, network, compute, storage, data, security, IaC and
observability.

**A product named three ways.** AWS's own guide records Amazon QuickSight's rename on 9 October 2025, and
its documentation now calls the product AWS Quick, with the dashboards continuing as Quick Sight; the exam
guide says Amazon Quick. The card gives all three and says which is current. *Amazon QuickSight* joined the
renames registry, and the gate's first run caught the card's own two mentions: *rebranded* is not one of
the words it reads as historical, so the card says *renamed*, which is what AWS's guide calls it in the same
entry.

**A table corrected.** The AWS Databases topic listed ElastiCache as managed Redis and Memcached; AWS's page
names three engines, Valkey first, and the table now does.

**The queue.** The task-statement examples above first, then the in-scope services, then OSCP, GCP and
AI+, the header tags still without a path, and the visual baseline. Google's exam guide renders by script,
so its outline needs another source, such as the guide's PDF.

## 30. What shipped — the twenty-fourth wave

Recorded below as *Session — the twenty-fourth wave, the guide's remaining examples, and a discovery service
that closed*. §29's queue: the task-statement examples and in-scope services that nothing on the site
mentioned.

| § | Item | Where it went |
|---|---|---|
| 29 | Comprehend and Polly, and the AI services beside them | `cloud` *AWS AI Services — Rekognition, Textract, Comprehend, Polly &amp; When to Train Your Own*: images and documents, the five language and speech services, the opt-out policy for stored content, and SageMaker AI for models that have to be your own |
| 29 | Gateway Load Balancer | `cloud` *Elastic Load Balancing — ALB, NLB &amp; Gateway Load Balancer, and the Cross-Zone Default*: the three by OSI layer, AWS's cross-zone arithmetic, and inspection put in the path by a route |
| 29 | Amazon MQ, MSK, AppFlow | `cloud` *Amazon MQ, MSK &amp; AppFlow — When the Protocol or the Partner Is Already Chosen* |
| 29 | Application Discovery Service, Application Migration Service, DMS | `cloud` *AWS Migration — AWS Transform MGN, DMS &amp; a Discovery Service That Closed* |
| — | AWS Config | `cloud` *AWS Config — What Every Resource Looked Like, and Whether It Was Allowed To*: in the in-scope list, and nowhere on the site, a security reference without the service that records configuration history |

**Two more changes the exam guide predates.** AWS closed Application Discovery Service to new customers on
7 November 2025 and points them to AWS Transform. Application Migration Service is documented now as AWS
Transform MGN; its own document history does not record when the name changed, so the card gives both names
and no date. SageMaker's rename is dated: on 3 December 2024 it became SageMaker AI, and *SageMaker* moved to
a wider platform that contains it.

**Both AWS paths take the five**: *SAA-C03* runs to 45 steps and *AWS, End to End* to 32.

**The queue.** The task-statement examples still unmentioned: AWS Batch, Provisioned IOPS, Requester Pays and
the Cost and Usage Report. Then in-scope services with no mention, among them DocumentDB, Keyspaces, Aurora
Serverless, Compute Optimizer, Kinesis Video Streams, Client VPN and the Well-Architected Tool. Then OSCP, GCP
and AI+, the header tags still without a path, and the visual baseline. The page budget fell to 25% raw this
wave, room for about 545 more topics at the current average, so the in-scope list is better served by cards
in existing topics than by a topic per service.

## 31. What shipped — the twenty-fifth wave

Recorded below as *Session — the twenty-fifth wave, cards inside topics that already owned the subject*.
§30's queue, taken as §30 advised: the budget is 25% raw, so most of it went into existing topics as cards.

| § | Item | Where it went |
|---|---|---|
| 30 | Provisioned IOPS, and the EBS volume types around it | A card in `cloud` *AWS Storage — S3 Classes, EBS &amp; EFS*, which had been a single card |
| 30 | Requester Pays | A second card in the same topic |
| 30 | The Cost and Usage Report | A card in `cloud` *Cloud Cost Control*, with CUR 2.0 in Data Exports |
| 30 | Compute Optimizer | A card in the same topic |
| — | EC2 hibernation, a task 4.2 example the name search missed, because *hibernate* already appeared for Windows | A card in `cloud` *AWS Compute — EC2, AMIs &amp; Auto Scaling* |
| 30 | AWS Batch | A card in `cloud` *AWS Serverless &amp; Containers* |
| 30 | Client VPN | A card in `cloud` *Hybrid Connectivity* |
| 30 | The Well-Architected Tool | A card in `cloud` *Well-Architected &amp; the Architecture Framework*, with the Agent AWS has in preview beside it |
| 30 | DocumentDB, Keyspaces, Aurora Serverless, and Neptune with them | `cloud` *Purpose-Built Databases on AWS — DocumentDB, Keyspaces, Neptune &amp; Aurora Serverless* |

**Every service the task statements name is now on the site but one.** Counted the way the twenty-third wave
corrected the count to be: every service among the 154 example phrases, searched for by name, 68 of them. The
exception is the NAT instance, which task 4.4 sets against the NAT gateway, along with one shared NAT gateway
against one per Availability Zone; the site prices NAT gateways and never mentions the alternative. Three more
phrases matched no text but are covered under other words: *EC2 Auto Scaling*, *EC2 hibernation* and *EC2
instance types*. In-scope services with no mention remain, among them Kinesis Video Streams, Amazon Managed Grafana and Managed Service for
Prometheus, AWS Proton, License Manager, Amplify, Device Farm and the Anywhere editions of ECS and EKS; the
guide lists them as services that may appear, not as things its tasks ask for.

**Six older topics changed review date**, because each gained a card and was read again around it. The AWS
Storage topic's first card still calls the archive classes *Glacier / Deep Archive*, and its FSx row names two of
FSx's four file systems; both are short rather than wrong, and are left for a pass over that topic.

**The queue.** The NAT instance against the NAT gateway, and shared against per-zone gateways, as a card in
*AWS VPC*. Then OSCP, GCP and AI+, the header tags still without a path, and the visual baseline. The in-scope
remainder above can wait for a reader who asks. Google's exam guide renders by script, so its outline needs
another source, such as the guide's PDF.

## 32. What shipped — the twenty-sixth wave

Recorded below as *Session — the twenty-sixth wave, the NAT instance and a gateway that spans zones*. §31's
queue, its first item.

| § | Item | Where it went |
|---|---|---|
| 31 | The NAT instance against the NAT gateway, and one shared gateway against one per zone | A card in `cloud` *AWS VPC — Subnets, Security Groups &amp; NACLs*, with AWS's newer regional NAT gateway as the third answer |

**Every service the SAA-C03 task statements name is now on the site**, by the count §31 used: the 68 services
among the guide's 154 example phrases, each searched for by name. The last, the NAT instance, appears now in
the card that sets it against the gateway.

**A row corrected.** The VPC topic's table said a NAT gateway sits in a public subnet. That is still true of
the zonal kind; the regional kind needs none, and the row says so.

**The queue.** GCP and AI+, the header tags still without a path, then the visual baseline. OSCP stays off
the queue. The in-scope services with no mention, listed in §31, wait for a reader who asks. Google's exam guide renders by script, so
its outline needs another source, such as the guide's PDF.

## 33. What shipped — the twenty-seventh wave

Recorded below as *Session — the twenty-seventh wave, an ACE path and a product renamed two years ago*. The
first of the header tags with a script-rendered outline, GCP, read from Google's exam guide as a PDF.

| § | Item | Where it went |
|---|---|---|
| 32 | A path for GCP | *Google Cloud Associate Cloud Engineer*, 29 steps, in the guide's four sections |
| — | ACE gap: organization setup | `cloud` *Google Cloud Organization Setup — Organization Policies, Cloud Identity, Workforce Federation &amp; Billing Export* |
| — | ACE gap: network design | `cloud` *Google Cloud Network Design — Shared VPC, Cloud NGFW Policies, Secure Tags &amp; Network Tiers* |
| — | ACE gap: Cloud Run operations | `cloud` *Cloud Run in Operation — Revisions, Traffic Splitting, Eventarc &amp; Cloud Run Functions* |

**A product renamed two years ago.** Google renamed Cloud Functions *Cloud Run functions* on 21 August 2024,
and the site used the old name in four places, as if current; the renames registry, which would have caught
it, had no entry. Both are fixed, and the registry allows the API names Google kept, such as the Cloud
Functions v2 API.

**The guide names much more than three topics cover.** Counted the same way as the AWS guide, by searching
every domain for each name, these ACE items still appear nowhere: OS Login, VM Manager, Hyperdisk and
regional Persistent Disk; AlloyDB, Memorystore, Dataflow and Managed Service for Apache Kafka; NetApp Volumes,
Managed Lustre and Storage Transfer Service; Cloud Workstations and Database Center; Managed Service for
Prometheus, Active Assist, Cloud Hub, Personalized Service Health and log routers; and Google's AI tooling,
Gemini Cloud Assist, the Gemini CLI, Antigravity and Application Design Center. The guide also renames Vertex
AI's agent and notebook products into the Gemini Enterprise Agent Platform, which the site never mentioned
under either name.

**The queue.** The ACE items above, a few topics at a time and cards where a topic already owns the
subject. The site's GCP infrastructure-as-code topic names Deployment Manager in its title, and Google's
Deployment Manager documentation address now redirects to a page that returns 404; find Google's own
statement of what happened to it before building on that topic. Then AI+, and the visual baseline.

## 34. What shipped — the twenty-eighth wave

Recorded below as *Session — the twenty-eighth wave, a retired product described as retiring*. §33's queue:
Deployment Manager first, then two more groups of the ACE guide's items.

| § | Item | Where it went |
|---|---|---|
| 33 | Deployment Manager | `cloud` *GCP-Native IaC*, retitled *Infrastructure Manager, Config Controller &amp; Deployment Manager's End*: the table's row corrected, Infrastructure Manager added, and a dated card on the retirement |
| 33 | OS Login, VM Manager, Spot VMs, Hyperdisk, regional Persistent Disk | `cloud` *Compute Engine in Operation — OS Login, VM Manager, Spot VMs, Hyperdisk &amp; Regional Disks* |
| 33 | AlloyDB, Bigtable, Memorystore, Pub/Sub, Dataflow | `cloud` *Google Cloud Data Products — AlloyDB, Bigtable, Memorystore, Pub/Sub &amp; Dataflow* |

**A retired product described as retiring.** The IaC topic called Deployment Manager *legacy; being retired*,
which was true when written. Google's notice says support ended on 31 March 2026, new users have been refused
since 30 June 2026, and the service is turned down after 30 June 2027. The retitle moved the topic's slug, and
`fix_topic_names.py --aliases-only` recorded the move so old links and stored progress follow it.

**Both GCP paths take the two new topics**: the ACE path runs to 31 steps and *Google Cloud, End to End* to 21.

**The queue.** The ACE items §33 listed that these two topics do not cover: Managed Service for Apache Kafka,
NetApp Volumes, Managed Lustre and Storage Transfer Service; Cloud Workstations and Database Center; Managed
Service for Prometheus, Active Assist, Cloud Hub, Personalized Service Health and log routers; and Google's AI
tooling. Then AI+, and the visual baseline. The page budget is at 24% raw, so cards in existing topics before
new topics.

## 35. What shipped — the twenty-ninth wave

Recorded below as *Session — the twenty-ninth wave, operations and storage, inside topics that owned them*.
§34's queue, as cards, because the budget is at 24% raw.

| § | Item | Where it went |
|---|---|---|
| 34 | Log routers and log buckets | A card in `cloud` *GCP Observability — Cloud Monitoring, Logging &amp; Trace* |
| 34 | Managed Service for Prometheus, with the Ops Agent | A second card in the same topic |
| 34 | Personalized Service Health and Active Assist | A third card in the same topic |
| 34 | Storage Transfer Service, NetApp Volumes, Managed Lustre | A card in `cloud` *GCP Storage — Cloud Storage, Persistent Disk &amp; Filestore* |
| 34 | Managed Service for Apache Kafka | A card in `cloud` *Google Cloud Data Products* |

**What is left of the ACE guide's list** is Cloud Workstations, Database Center and Cloud Hub, three consoles
more than three concepts, and Google's AI tooling: Gemini Cloud Assist, the Gemini CLI, Antigravity,
Application Design Center and the Gemini Enterprise Agent Platform that Vertex AI's agent and notebook products
now sit under. Those change faster than anything else in the guide, and a card about them would need a date on
every sentence.

**The queue.** AI+, the last header tag without a path, then the visual baseline. The ACE guide's AI tooling
waits for a reader who asks, and is read from Google's pages on the day it is written.

## 36. What shipped — the thirtieth wave

Recorded below as *Session — the thirtieth wave, a tag for an exam that does not exist*. §35's queue: AI+.

| § | Item | Where it went |
|---|---|---|
| 35 | AI+ | The header tag, two badges and the dictionary entry now name *CompTIA SecAI+*, because AI+ named no CompTIA exam |
| 35 | A path for the AI tag | *CompTIA SecAI+ (CY0-001)*, 30 steps, in the order of the exam's four domains |
| — | CompTIA's name for its largest domain | A sentence in `ai` *AI Security — Attacking and Defending AI Systems*'s first card |
| — | The field's standard term | A sentence in `ai` *Adversarial AI &amp; AI Threats (Red Team)*'s first card, dated to NIST AI 100-2 E2025 |

**A tag for an exam that does not exist.** Reading the exam's page before writing its path found no exam
called AI+. CompTIA's certification list, read in November 2026, has SecAI+, launched on 17 February 2026,
and several AI courses whose names end in *Essentials*, and nothing called AI+. No gate could have caught it:
the renames registry knows products that changed names, and this was a name with no product behind it in
CompTIA's list. Reading the issuer's page before the path caught it, as reading Google's pages for the ACE
path caught Cloud Functions' rename.

**An exam path with no gap topic.** All 30 steps existed: 24 in `ai`, two in `cs` for the
statistics behind anomaly detection and base rates, and one each in `blueteam`, `ops`, `threat` and `grc`.
The exam's summary names threat modeling under AI-assisted security, which is why the threat modeling topic
is a step. What the site lacked was two of the exam's words, and each went into a topic as one sentence.

**The queue.** The visual baseline, which still fails in this container on font rendering and is left
alone. The ACE guide's AI tooling waits for a reader who asks, and OSCP stays off the queue. SecAI+'s full
objectives come from CompTIA through a short form on the exam's page, so the path follows the summary
printed there; the terms that summary names are the next thing to count against the corpus.

## 37. What shipped — the thirty-first wave

Recorded below as *Session — the thirty-first wave, a threat list two editions old*. §36's queue: the terms
SecAI+'s summary names, counted against the corpus, which led first to the lists those terms come from.

| § | Item | Where it went |
|---|---|---|
| 36 | OWASP's Top 10 for LLM Applications, current edition | `ai` *AI Security — Attacking and Defending AI Systems*: the risk table is the 2026 order, with what changed since 2023/24 and 2025; the governance topic's OWASP card names the 2026 edition |
| — | OWASP's Top 10 for Agentic Applications 2026 | A card in `ai` *Agent Safety &amp; Sandboxing*, ASI01 to ASI10 read against the topic's controls |
| — | The EU AI Act's dates | A card in `ai` *AI Governance &amp; Frameworks*, from the Commission's page as updated on 19 October 2026 |
| — | The jailbreak card's *insecure output handling* | *Improper output handling*, OWASP's name for it since 2025 |

**A threat list two editions old.** The governance topic gave OWASP's list as *the canonical LLM threat list*
and named ten entries; they were the 2023/24 edition's, entry for entry. OWASP has published two editions since,
and its page for the 2026 one is dated 27 October 2026, four weeks before this wave. Six of the ten entries the
site named are gone or renamed. No gate could have seen it: the list carried no date, and nothing on the site
said which edition it was. Both cards that name it now carry fact anchors with the date, so the next edition
will find a dated claim to check rather than a sentence that sounds timeless.

**A regulation whose dates moved after they were written down.** The governance topic's verdict said the AI
Act is *the one with dates attached*, and gave none. The dates it would have given in 2025 are no longer the
dates: the AI Omnibus, in force from 27 July 2026, moved the high-risk rules later, to December 2027 and
August 2028, and added a ninth prohibited practice from December 2026. The new card gives the dates and
names the page they came from.

**The queue.** First the AI ethics topic, whose card calls six pillars *trustworthy AI characteristics*
under a title naming NIST's AI RMF: NIST's own list has seven, puts *valid and reliable* beneath the rest, and
has no sustainability. Then the rest of SecAI+'s summary terms, alert correlation and behavior analysis among
them, counted the same way. The visual baseline stays left alone, the ACE guide's AI tooling waits for a
reader who asks, and OSCP stays off the queue.

## 38. What shipped — the thirty-second wave

Recorded below as *Session — the thirty-second wave, a framework's name over somebody else's list*. §37's
queue: the AI ethics topic first.

| § | Item | Where it went |
|---|---|---|
| 37 | The pillars card's claim to be NIST's characteristics | `ai` *AI Ethics &amp; Responsible AI (NIST AI RMF)*: retitled *Six Goals for a Policy to Name*, with a sentence on how NIST groups them |
| 37 | NIST's seven characteristics | A card in the same topic, with the four functions and NIST's note that 1.0 is being revised |
| — | NIST AI 600-1 | A card in the same topic: the Generative AI Profile's twelve risks, confabulation among them |
| — | The framework's dates | A sentence in `ai` *AI Governance &amp; Frameworks*'s RMF card |

**A framework's name over somebody else's list.** The topic's title names NIST's AI RMF, and its card called
six pillars *trustworthy AI characteristics*, which is NIST's phrase. The six were a reasonable grouping and
not NIST's: sustainability is not among NIST's seven, and valid and reliable, which NIST draws as the base the
others stand on, was not among the six. A reader revising for SecAI+, whose summary names the NIST AI RMF,
would have learned the wrong list under the right name. The pillars stay, under a title that claims less.

**Sustainability had a home after all.** NIST's Generative AI Profile counts environmental impacts among its
twelve risks, so the goal the pillars named is in NIST's work, as a risk of one kind of system rather than a
characteristic of every one. The pillars card now says so.

**The queue.** OWASP's web Top 10: three topics teach the 2021 edition, one of them titled with the year, and
OWASP's project page calls the 2025 edition the current release. Then the rest of SecAI+'s summary terms. The
visual baseline stays left alone, the ACE guide's AI tooling waits for a reader who asks, and OSCP stays off
the queue.

## 39. What shipped — the thirty-third wave

Recorded below as *Session — the thirty-third wave, a year in a title*. §38's queue: OWASP's web Top 10.

| § | Item | Where it went |
|---|---|---|
| 38 | The reference list | `pentest` *OWASP Top 10 (2025)*, retitled from *(2021)*: the ten in 2025 order |
| — | Old findings cite 2021 numbers | A card in the same topic mapping each 2021 category to its 2025 place |
| 38 | The essential explainer | `sec` *OWASP Top 10 — The Most Critical Web Security Risks*: the table follows 2025, and the card calls OWASP by its current name |
| 38 | The beginner list | `sec` *OWASP Top 10 – The Web Vulnerabilities Everyone Must Know*: the 2025 list with analogies, the injection example renumbered A05 |
| — | The API topic's pointer | *The web list, in its 2025 edition*, where it had said the 2021 list *remains correct* |

**A year in a title.** One of the three topics carried *2021* in its name, so the retitle moved its address.
`fix_topic_names.py --aliases-only` recorded the move, paths and related links follow it, and a near-duplicate
verdict keyed by the old title was re-read and re-keyed rather than deleted. The landing card for `pentest`
listed the old title among its start-here topics in `data/domain-intros.json`, which no gate in `make check`
reads for titles; the smoke suite's start-here check caught it on the first run, and that suite was run again
after the fix.

**An old name on the card that introduces the list.** The essential topic's card was titled *Open Web
Application Security Project*; OWASP's about page calls the foundation the Open Worldwide Application Security
Project, as the site's own acronym dictionary already did.

**The queue.** NIST CSF 2.0 in `grc`: a Start Here card counts five functions and mentions Govern in brackets,
a compliance table lists five, and a code block colors the six functions in a way NIST's own figure does not,
four of the six wrong. Then the rest of SecAI+'s summary terms. The visual baseline stays left alone, the ACE
guide's AI tooling waits for a reader who asks, and OSCP stays off the queue.

## 40. What shipped — the thirty-fourth wave

Recorded below as *Session — the thirty-fourth wave, colors nobody had checked*. §39's queue: NIST CSF 2.0 in
`grc`.

| § | Item | Where it went |
|---|---|---|
| 39 | Five functions, Govern in brackets | `grc` *Frameworks Without the Jargon*: six, with Govern in the table |
| 39 | The compliance table's five | `grc` *Compliance Frameworks — Playing by the Rules*: six |
| 39 | The functions' colors | `grc` *NIST CSF &amp; ISO 27001 – GRC Frameworks Explained*: the colors of NIST's own figure, under *Color* |
| — | Categories carried over or invented | `grc` *NIST Cybersecurity Framework 2.0*: NIST's 22 categories by name |

**Colors nobody had checked.** A code block gave each function a color, and four of the six disagreed with
NIST's figure of the six in the CSF 2.0 document: Govern is yellow there, Identify blue, Protect purple, Detect
orange, Respond red and Recover green. No text extraction shows a color, so the check meant rendering the PDF's
page and looking at it. The colored rows in the CSF 2.0 topic are the page's own styling and claim nothing, so
they were left alone.

**A census that could not see the problem.** The two queries about the functions opened answered: readers
reached the cards, and the cards were wrong. The census measures whether a reader arrives, not what they find,
and every fix in this wave came from reading NIST's documents against the cards.

**The queue.** SecAI+'s summary terms, counted: of six, four reach a fitting topic and two do not.
`alert correlation` misses the correlation topic, which never says *alert*, and `behavior analysis` misses the
UEBA topic, which says *analytics*. The visual baseline stays left alone, the ACE guide's AI tooling waits for
a reader who asks, and OSCP stays off the queue.

## 41. What shipped — the thirty-fifth wave

Recorded below as *Session — the thirty-fifth wave, the exam's words for what was already there*. §40's queue:
SecAI+'s summary terms.

| § | Item | Where it went |
|---|---|---|
| 40 | `alert correlation` | A sentence in `blueteam` *Correlation &amp; Sequencing*'s first card |
| 40 | `behavior analysis` | A sentence in `blueteam` *User &amp; Entity Behavior Analytics*'s first card |
| — | A badge two exams old | `pentest` *Methodology &amp; Phases*: PT0-003, which CompTIA launched on 17 December 2024 |

**The exam's words for what was already there.** Six of SecAI+'s summary terms were counted. Four reached a
topic that covers them on the words the site already used; two reached other cards because the right topics
said *correlation* without *alert* and *analytics* where the exam says *analysis*. Each now carries one sentence
naming the exam's term and what it changes for the topic, which is nothing: the costs of a correlation rule and
the inversion in a learned baseline are the same whoever, or whatever, writes them.

**The queue.** MITRE ATT&amp;CK: version 19, in April 2026, split Defense Evasion into Stealth and Defense
Impairment, and Enterprise has fifteen tactics; the `threat` topic's badge says fourteen and two cards list the
old tactic. The visual baseline stays left alone, the ACE guide's AI tooling waits for a reader who asks, and
OSCP stays off the queue.

## 42. What shipped — the thirty-sixth wave

Recorded below as *Session — the thirty-sixth wave, a tactic split in two*. §41's queue: ATT&amp;CK version 19.

| § | Item | Where it went |
|---|---|---|
| 41 | Fourteen tactics | `threat` *MITRE ATT&amp;CK Framework*: badge, first card and grid at fifteen, Stealth and Defense Impairment where Defense Evasion was |
| 41 | The beginner card's tactic list | Fifteen in ATT&amp;CK's order, where it had named eleven |
| — | The eleven technique IDs the site cites | Checked against ATT&amp;CK's pages: ten current, and T1574.002's revocation already recorded |

**A tactic split in two.** ATT&amp;CK v19, in April 2026, renamed TA0005 from Defense Evasion to Stealth, for
concealment that leaves the defenses alone, and created TA0112, Defense Impairment, for breaking them. The grid's
old description, *obfuscation, log clearing, process injection*, turned out to belong wholly to Stealth:
Indicator Removal, which holds log clearing, stayed there, and the impairment side is disabling tools,
firewalls and command-history logging. The beginner card's list had a second, older fault: it named eleven of the
fourteen tactics, without Reconnaissance, Resource Development or Command and Control.

**A ceiling that held.** The new grid card first carried an inline color, and the lint's ceiling on inline style
attributes, which may fall and may not rise, stopped the check at 402 against 401. It uses a color class instead.

**The queue.** Post-quantum cryptography: NIST published IR 8547 as final in October 2026, deprecating
quantum-vulnerable public-key algorithms after 2030 and disallowing them after 2035, with earlier federal
deadlines, and chose HQC as ML-KEM's backup in March 2025; the PQC topic stops at the 2024 standards. The visual
baseline stays left alone, the ACE guide's AI tooling waits for a reader who asks, and OSCP stays off the queue.

## 43. What shipped — the thirty-seventh wave

Recorded below as *Session — the thirty-seventh wave, a report a month old*. §42's queue: post-quantum
cryptography.

| § | Item | Where it went |
|---|---|---|
| 42 | NIST's transition dates | A card in `sec` *Post-Quantum Cryptography — Harvest Now, Decrypt Later*: deprecated after 2030, disallowed after 2035, and the earlier federal deadlines |
| 42 | HQC | A sentence in the same topic's standards card |
| — | AES-128 *effective 64-bit, move to AES-256* | The same topic's table row, as NIST's report rates it: Category 1, and not on its retirement list |

**A report a month old.** NIST published IR 8547 as final in October 2026, nearly two years after its draft.
It keeps the draft's two dates for quantum-vulnerable public-key algorithms and adds the federal deadlines that
came since: Executive Order 14412 and OMB Memorandum M-26-15 move the most sensitive federal systems to
post-quantum key establishment by the end of 2030 and signatures by the end of 2031.

**A row that said more than NIST does.** The threat card's table told readers to move AES-128 to AES-256 because
Grover's algorithm halves its effective strength. NIST's report counts every approved symmetric primitive of at
least 128-bit strength as meeting its lowest post-quantum category and retires only the 112-bit ones. The row now
follows NIST, and leaves AES-256 to policies that ask for the margin.

**The queue.** Public TLS certificates: the CA/Browser Forum's Baseline Requirements cut the maximum lifetime
from 398 days to 200 on 15 March 2026, with 100 and then 47 to come, and the PKI topic says CRL and OCSP give
real-time revocation while Let's Encrypt turned its OCSP service off in August 2025. The visual baseline stays
left alone, the ACE guide's AI tooling waits for a reader who asks, and OSCP stays off the queue.

## 44. What shipped — the thirty-eighth wave

Recorded below as *Session — the thirty-eighth wave, a limit that changed in March*. §43's queue: public TLS
certificate lifetimes.

| § | Item | Where it went |
|---|---|---|
| 43 | The lifetime schedule | A card in `sec` *PKI &amp; Certificate Lifecycle*: 398, 200, 100 and 47 days, and the domain-validation reuse beside them |
| 43 | *CRL and OCSP enable real-time revocation checking* | The same topic's diagram card: clients check unreliably, and Let's Encrypt publishes CRLs only since August 2025 |

**A limit that changed in March.** The CA/Browser Forum's Baseline Requirements cut the longest validity a
public TLS certificate may have from 398 days to 200 on 15 March 2026, with 100 to follow in March 2027 and 47
in March 2029, and the window for reusing a domain check shrinks to 10 days. The site had never stated the limit,
so nothing was wrong in the old sense; a reader would simply not have learned that renewal is about to become
something no person does by hand.

**Revocation as it is.** The PKI diagram said CRLs and OCSP give real-time revocation, while the cryptography
topic, elsewhere in the same domain, already said revocation checks fail open. The diagram now agrees with it,
and adds that Let's Encrypt has turned its OCSP service off.

**The queue.** The EU's Cyber Resilience Act, which the site never names, though its reporting obligations
began on 11 September 2026: a 24-hour early warning for actively exploited vulnerabilities in products with
digital elements. The visual baseline stays left alone, the ACE guide's AI tooling waits for a reader who asks,
and OSCP stays off the queue.

## 45. What shipped — the thirty-ninth wave

Recorded below as *Session — the thirty-ninth wave, a regulation the site had never named*. §44's queue: the
EU Cyber Resilience Act.

| § | Item | Where it went |
|---|---|---|
| 44 | The Cyber Resilience Act | A row and a card in `grc` *The Regulatory Landscape — DORA, NIS2 &amp; Cyber Disclosure Rules* |

**A regulation the site had never named.** The regulatory topic's table ran from DORA to state breach laws and
had no row for the one regulation that applies to products rather than organizations. Its reporting clock has
run since 11 September 2026: 24 hours for an early warning of an actively exploited vulnerability, 72 for the
notification, through ENISA's Single Reporting Platform. The census's only opening answer was a coincidence of
three ordinary words, which is the kind of answer the census exists to notice.

**The queue.** Other numbered frameworks the site cites, starting with the CIS Controls. The visual baseline
stays left alone, the ACE guide's AI tooling waits for a reader who asks, and OSCP stays off the queue.

## 46. What shipped — the fortieth wave

Recorded below as *Session — the fortieth wave, defaults that moved under the cards*. §45's queue: numbered
frameworks, which led to one wrong word and, through the dictionary, to Kerberos.

| § | Item | Where it went |
|---|---|---|
| 45 | *18 prioritized safeguards* | `blueteam` *CIS Benchmarks &amp; CIS-CAT*: CIS Controls v8.1, 18 Controls made of Safeguards, in IG1 to IG3 |
| — | *Crack the RC4-encrypted ticket offline* | `sec` *Active Directory — Structure, Objects &amp; Attacks*: RC4 tickets only where RC4 is configured, since April 2026 |
| — | RC4 *disabled everywhere* | The dictionary's note, saying what changed for Kerberos and when |

**Defaults that moved under the cards.** The Kerberoasting row described the attack as it worked for twenty
years, against RC4 tickets a domain controller handed out by default. Microsoft's updates for CVE-2026-20833
changed that default this year, in three steps from January to July, and the row now says where RC4 tickets still
come from and how to find those places. The dictionary's note had the opposite fault, claiming RC4 was gone
everywhere while the attack table still depended on it.

**Search does not read fact anchors.** The two Kerberos census queries stayed at zero after the first fix,
because the CVE number and the registry value were only in the anchor, a comment the search never indexes. They
are in the row's text now, where a defender holding Microsoft's KB would look for them.

**The queue.** Microsoft's other recent defaults were checked the same way and needed nothing: the site makes no
claim about SMB signing or NTLM defaults, and its LAPS cards already separate the built-in LAPS from the legacy
one. Next, the seven topics `depth_report.py --thin` lists, starting with `linux`'s *Package Management*, the
thinnest on the site. The visual baseline stays left alone, the ACE guide's AI tooling waits for a reader who
asks, and OSCP stays off the queue.

## 47. What shipped — the forty-first wave, and Netlify Functions at the owner's request

Recorded below as *Session — the forty-first wave, a thin topic and a first function*. §46's queue: the thin
topics, thinnest first; and, mid-wave, the owner asked for Netlify's Functions feature to be turned on.

| § | Item | Where it went |
|---|---|---|
| 46 | The thinnest topic | `linux` *Package Management*: a card on how a repository is trusted, from Debian's and DNF's manuals |
| — | Netlify Functions, asked for by the owner | `netlify/functions/health.mts`, a read-only status function at `/.netlify/functions/health` |
| — | The service worker caching function responses | `sw.js` skips `/.netlify/` paths |

**A thin topic, deepened rather than padded.** *Package Management* had a table of commands and a verdict about
snaps. It gained the one thing a Linux+ reader most needs and the table never said: how a repository earns trust,
why `apt-key` went, and what `Signed-By` scopes. The thin count fell from seven to six.

**A first function.** The owner sent Netlify's Functions page for the `garrettstudies` project, showing the empty
state, and asked for the feature to be enabled. Netlify turns Functions on for a project by deploying one, so the
site now ships a status function written to Netlify's current handler shape: it reports the serving deploy, its
context and region, makes no outbound requests and holds no secret. Two things needed care. The service worker is
cache-first for every same-origin request, and would have frozen the function's first answer; it now leaves
`/.netlify/` alone. And the publish directory is the repository root, so the function's source is also served as a
static file, which is harmless for this one and a rule for every later one: no secret in that directory, ever.

**How it reaches production.** The project builds `main`, and its current production deploy, of 23 November,
reports no functions. The function is on `claude/charming-pascal-efiq4m` and goes live when that branch next
reaches `main`. Function metrics then fill as the endpoint is called; nothing on the site calls it on its own.

**The queue.** The six thin topics left, two military lookup cards first. The visual baseline stays left alone,
the ACE guide's AI tooling waits for a reader who asks, and OSCP stays off the queue.

## 48. What shipped — the forty-second wave, three thin topics and the visual baseline's cause

Recorded below as *Session — the forty-second wave, the officers with no number*. §47's queue: the six thin topics,
two military lookup cards first, and the visual baseline.

| § | Item | Where it went |
|---|---|---|
| 47 | The visual baseline | `tools/visual_test.mjs` names the Playwright that drew the baselines and the one running, and refuses `--update` under another |
| 47 | *Staff Functions 1–9* | `military`: a card on FM 6-0's three kinds of staff officer, and the verdict's claims corrected to the manual |
| 47 | *Common Codes Decoded* | `military`: a card on the executive officer and the chief of staff, and on the hyphen in S-3 |
| 47 | *Software Supply Chain Security* | `devops`: a card on the pipeline's own dependencies, CVE-2025-30066 and GitHub's workflow lockfile |
| — | An action pinned to a branch | `sec` *Container Security 101*: the Trivy example's `@master` is a commit SHA |

**The visual baseline, closed.** It failed in this container on every wave of this session, at exactly 10.335% and
10.106%, and was carried as font rendering. It is not fonts: Share Tech Mono and Outfit both load here, and blocking
them moves the diff to 13.15%. It is the browser. CI pins Playwright 1.56.0, whose Chromium 141 drew the baselines,
and CI's last run to reach the step, on 11 October 2026, matched them 2/2; this container has Playwright 1.63.0 and
Chromium 153, which draws the chip labels about 10% wider. The two runs since, on 23 November, stopped before the
step, because `ubuntu-latest` had become 26.04, which the pinned Playwright cannot install on; the job has been
pinned to 24.04 since the next day and has not run, because no pull request has been opened. So the baseline is
right where it is, and the test now says why it fails here and refuses to accept this container's rendering, which
would turn CI red on every push.

**Three thin topics, and two claims the sources did not support.** *Staff Functions 1–9*'s verdict said one through
six appear at every level and seven and eight start at division. FM 6-0 lists S-1 to S-6 and S-9 but says most
battalions and brigades plan inside the S-3 rather than in an S-5, and it lists no 7 at any echelon. *Common Codes*
called the XO the deputy commander; the manual makes the executive officer the principal staff officer, and second in
command only usually, only below division. The `devops` overview named every control for what you ship and none for
what builds it, and GitHub's advice there had moved: a workflow lockfile now comes before SHA pinning.

**Closed as decisions, not as work.** Two items have sat at the end of every queue since the twenty-ninth wave, and
they leave it here as decisions. The ACE guide's AI tooling is written when a reader asks for it, read from Google's
pages on the day, because those products change faster than anything else in the guide and a card on them would need
a date on every sentence. OSCP stays off the queue; *Cert Roadmaps* names it in the red-team track and needs nothing
more.

**The queue.** The three thin topics left, in `data`, `web` and `eng`.

## 49. What shipped — the forty-third wave, and the thin list empty

Recorded below as *Session — the forty-third wave, the cards the tables implied*. §48's queue: the three thin topics
left, in `data`, `web` and `eng`.

| § | Item | Where it went |
|---|---|---|
| 48 | *The Data Interview* | `data`: the second-highest-salary puzzle, three answers against three inputs, every result run on PostgreSQL 16 |
| 48 | *The Full-Stack Picture* | `web`: the status codes by the layer that sends them, from RFC 9110 and RFC 6585, and the table's dead labels replaced with links |
| 48 | *Cert Roadmaps* | `eng`: what each certification on the table costs to keep, from six bodies' own pages |
| — | A row whose headline could be wrong and pass | `tools/check_plan_numbers.py` checks each row's first bold run against the tool's first number |

**The thin list is empty.** Each of the six topics §46 left had a table that implied a card it never wrote. *The
Data Interview* named the puzzle every SQL round asks and did not do it; doing it found a dialect trap worth the
card, because Postgres sorts a NULL as larger than any value, so under `DESC` two of the three usual answers return
the top salary again, where SQLite returns the right one. *The Full-Stack Picture* sent readers to *I4*, *I5* and
*H\**, labels from an organization of the site that no longer exists, and never said what happens when the request
in its diagram fails. *Cert Roadmaps* laid out tracks without saying that every rung expires, at different rates
and prices, or that climbing within one body renews the rungs below for one fee.

**A gate that passed a wrong headline.** When the three cards landed, the Thin row still read **3** over a tool
printing 0, and `check_plan_numbers.py` passed it: every number it derived appeared somewhere in the row, and the 0
of *0%* was one of them. It checks each row's first bold run for the tool's first number now, with three fixtures for
the case, and all thirteen rows pass it as they stand.

**The queue.** Nothing this file has queued is left. Every item is shipped, or closed as a decision §48 records: the
ACE guide's AI tooling waits for a reader who asks, and OSCP stays off the queue. New work comes from whichever census
next reports something, as *Where new work comes from now* says at the top. One thing waits on the owner rather than
on a session: this branch reaches CI only through a pull request, so the browser job's Ubuntu 24.04 pin, the Netlify
function and the waves since the last merge have been verified in this container and not yet in CI.

## 50. What shipped — the forty-fourth wave, the oldest dated claims

Recorded below as *Session — the forty-fourth wave, twelve claims from August*. §49's queue was empty, so the work
came from a census, as *Where new work comes from now* says it should: `check_volatility.py` prints the dated claims
last checked longest ago, and twelve were from August.

| Topic | The claim | What its owner's page said |
|---|---|---|
| `infra` *Service Accounts — gMSA* | A 240-character password | 240 bytes, randomly generated, rotated every 30 days unless another interval was set at creation |
| `m365` *eDiscovery* and *Retention* | Holds are gated to the enterprise tiers | Business Premium has Litigation Hold as well as E3, E5 and Exchange Online Plan 2; the other plans get it with the Exchange Online Archiving add-on |
| `net` *Vendor Firewall Concepts* | TLS decryption is the heaviest feature on most platforms | Fortinet's matrix takes a FortiGate 40F from 5 Gbps to 310 Mbps with SSL inspection, but threat protection is the lower figure on three of the eight models on its first page; now *among the heaviest* |
| `career` *Home Lab* | A Pi cluster at about $150 for 3-4 nodes | A 2GB Pi 5 is $77.50 since 1 October 2026, after two memory-driven rises; the used mini PC price, which no authority publishes, is gone |
| `cloud` *Entra ID — Sign-In* | The What If tool's path | Under Entra ID and Policies now |
| `ai` *Agent Frameworks* | LangChain and LlamaIndex as described | LangChain 1.0 runs its agents on LangGraph and moved its chains to a legacy package; LlamaIndex leads with document parsing |
| `m365` *Mailbox Types* and *Message Trace* | A size ceiling, and a window of days and months | Right, and now exact: 50 GB, and 90 days queried 10 at a time |
| `cs` *Primes &amp; Factoring*, `grc` *The Regulatory Landscape* | Key sizes, and the regulatory snapshot | Confirmed: SP 800-57 Part 1 Rev. 5 is still current, and Item 106 is in force; the key-size table gains the 2048-bit row it skipped |

**CI, at last.** The pull request §49 waited on was opened as
[garrettadams23/Studies#70](https://github.com/garrettadams23/Studies/pull/70), and CI's first run since the runner
pin passed every step: the browser job on Ubuntu 24.04, the visual check 2/2 under the pinned Playwright, and the
census row against a live census. That settles the visual baseline by the measurement §48 could only predict.

**What a re-check finds.** Seven of twelve claims had moved or were wrong, in two kinds about equally common: a
claim that had overstated from the day it was written (*the enterprise tier*, *most platforms*, a 240-character
password) and a precise one the world moved under (a price, a menu path, a framework's structure). The census never
flags either, because a stale claim still answers the question it was found by. Only a dated re-check does, and
`check_volatility.py` keeps the order.

**The queue.** The next-oldest dated claims: sixty-five from September, which `check_volatility.py` lists oldest first.

## 51. What shipped — the forty-fifth wave, the m365 claims from September

Recorded below as *Session — the forty-fifth wave, consoles and clocks*. §50's queue: the sixty-five claims from
September, of which the twenty-two in `m365` are this wave, all of them in nine topics.

| Topic | The claim | What Microsoft's page, or the address itself, said |
|---|---|---|
| *EOP &amp; Defender for Office* | Quarantine keeps mail 30 days by default, configurable downward | 15 days in the default and custom anti-spam policies, 30 in the Standard and Strict presets, settable from 1 to 30 |
| *M365 Tenant Anatomy* | The admin center is at admin.microsoft.com; Teams redirects to teams.cloud.microsoft | admin.microsoft.com redirects to admin.cloud.microsoft; Teams answers at both addresses |
| *Teams Governance &amp; Sprawl* | Owner warnings are the whole mechanism of expiry | Any use renews a group about 35 days before expiry with no warning sent, so the policy removes what nobody uses |
| *Microsoft 365 Groups* | Deleted groups are recoverable for 30 days by default | 30 days, and Microsoft says the window can't be changed |
| The other eighteen | Console names and addresses, SharePoint's limits, Graph's batch size, where call analytics and guest access live | Right, and re-dated with what each was checked against |

**Requesting the address is a source.** Six of the claims were web addresses, and the Microsoft page that once listed
which consoles had moved to `cloud.microsoft` no longer does. So each address was requested from this container, and
the answer recorded: a redirect to `admin.cloud.microsoft`, a sign-in page, a 403. The two that refused, Entra's
and Intune's, are confirmed instead by Microsoft's own pages: the group-restore page links `entra.microsoft.com`, and
the Intune admin center's link resolves to `intune.microsoft.com`. The SharePoint admin center's own link enters
through `admin.microsoft.com/sharepoint`, which the table now says.

**The queue.** The rest of September's claims: forty-three, in `cs`, `endpoint`, `infra`, `cloud` and six others.

## 52. What shipped — the forty-sixth wave, endpoint, infra and cloud from September

Recorded below as *Session — the forty-sixth wave, a default that upgrades keep*. §51's queue: the rest of
September's claims, of which the seventeen in `endpoint`, `infra` and `cloud` are this wave.

| Topic | The claim | What the owner's page said |
|---|---|---|
| `infra` *AD Replication* | The tombstone lifetime is 180 days on any modern domain | 180 is the default for a forest built on a supported Windows Server; upgrading never changes the existing value, so an old forest can still hold 60 |
| `endpoint` *The Intune Suite* | The Suite folds into E3 and E5 from mid-2026, split unevenly | Exactly which capabilities go to which tier, rolled out by 1 August 2026 and priced at the first renewal after 1 July; Microsoft's post and FAQ replace the write-ups the anchor cited |
| The other fifteen | Evaluation, replication interval, delete guard, storage minimums, metrics retention, rollback window, console names | Right, and re-dated; six anchors now cite the owner's page instead of a secondhand source |

**A default is a property of when the thing was made.** The tombstone claim was true of every forest built in the last
twenty years and false of the ones most likely to be in trouble: a forest old enough to have begun before Server 2003
SP1 keeps its 60 days through every upgrade since, and a DC left off for two months in that forest is the failure the
card is about. Microsoft's page says so in a note; the card now says it in its first sentence.

**The queue.** September's last twenty-six claims: seventeen in `cs`, most of them the csvistool deep links, and nine
across `philosophy`, `blueteam`, `data`, `grc`, `redteam` and `script`.

## 53. What shipped — the forty-seventh wave, September's last claims

Recorded below as *Session — the forty-seventh wave, a route read from the site that serves it*. §52's queue:
September's last twenty-six claims.

| Topic | The claim | What its source said |
|---|---|---|
| `cs` seven topics, `script` *Choosing the Right Data Structure* | Eighteen anchors for 39 csvistool routes | Every route is a key of the algorithm map in csvistool.com's published bundle; a made-up route is not |
| `redteam` *Cloud Credential Attacks* | An hour by default for an instance role | An hour is the default for an assumed session, up to twelve; instance role credentials rotate on their own and the role's maximum does not bind them |
| `philosophy` *Psychology* | The DSM-5-TR is the current edition | Still, and the APA said in January 2026 that its successor will be a living online document, undated and unnamed |
| `philosophy` *Qigong*, `blueteam` *Windows Forensic Artifacts*, `data` *MongoDB*, `grc` *PCI DSS* | Tai chi and falls, the prefetch caps, the 16 MB document, PCI DSS v4.x | Right, and re-dated with the page each was read on |

**When the source is out of reach, read what it produces.** The csvistool anchors named the tool's repository, which
this session's GitHub access does not cover. The routes were never facts about the repository anyway; they are facts
about the site a reader's click lands on, and that site ships one JavaScript bundle whose algorithm map is keyed by
route. All 39 keys are there. The check was tried on a route that does not exist first, and failed, which is what
made the other 39 passes worth having.

**The queue.** One dated claim from October, then none older than this month. The verification debt's next work is
not re-dating but widening: `check_volatility.py`'s three console candidates, read and recorded as false positives,
and the dated claims Phase 11 §3 says cannot be counted because nobody marked them.

## 54. What shipped — the forty-eighth wave, the last claim from October

Recorded below as *Session — the forty-eighth wave, a page that answers now*. §53's queue: one dated claim from
October, the UAH ASCII page the site owner asked to be linked, which the container of that day could not fetch.

| Topic | The claim | What the page said |
|---|---|---|
| `cs` *ASCII Character Set* | The link, recorded as linked and not read | The page answers now: it shows the 0-127 table and one extended table as images, and calls 128-255 the extended set, which the topic's own card explains is one code page among many |

**Every dated claim on the site has now been checked this month.** `check_volatility.py` prints one month, 2026-11,
for all 439 of them. That is the end of the re-dating queue and the start of a slower one: Phase 11 §3's finding is
that the claims nobody marked cannot be counted, so the next verification work is finding them, and the census of
console names, the three candidates recorded as false positives, is the only tool that looks.

**The queue.** None from the re-checks. The next dated claims to fall due are this month's own, in about three months.

**And the function is live.** The owner merged [garrettadams23/Studies#70](https://github.com/garrettadams23/Studies/pull/70) at 22:20 UTC on 25 November, after its CI passed. Netlify's production deploy of that merge lists one function, `health`, and the endpoint answered with status 200, `no-store` and the deploy's own id, which is the first invocation its metrics will show. The waves since, forty-four to forty-eight, are on the branch, which merged `main` back in rather than rewriting history, and wait for the next pull request.

## 55. What shipped — the forty-ninth wave, the tier-gating pass redone

Recorded below as *Session — the forty-ninth wave, a model answer that was wrong*. §54's queue was empty; the work came
from wave 44's finding that the one tier claim Phase 11 §7 had approved was false.

| Topic | The claim | What Microsoft's page said |
|---|---|---|
| `m365` *Licensing Without Tears* | A tier table with no Business Premium, and litigation hold first named at E3 | Business Premium covers up to 300 users with device management, threat protection and litigation hold; the summer 2026 packaging added Intune Plan 2, Remote Help and Defender for Office 365 Plan 1 to E3, and Security Copilot and the rest of the Intune Suite to E5 |
| `endpoint` *Endpoint Analytics &amp; Proactive Remediations* | An E3-or-above style license | Windows Enterprise E3 or E5, which Microsoft 365 F3, E3 and E5 include, Education A3 or A5, or Windows VDA; not Business Premium |
| `endpoint` *Conditional Access &amp; Device Compliance* | Sign-in risk needs P2 | Right: it comes from ID Protection, which needs Entra ID P2 |

**The model answer was the wrong one.** Phase 11 §7 named the hold claim as the site's tier-gating discipline done
right. It was the claim most worth checking, because the table above it was the same shape: a tier table for a
licensing family whose cheapest serious plan, the one most small businesses buy, was missing. §9 of Phase 11 now
records what that means for the phase's advice.

**The queue.** None from Phase 11's classes; each was read, and V1 was re-checked. The next dated claims fall due in
February.

## 56. What shipped — the fiftieth wave, the product-names class

Recorded below as *Session — the fiftieth wave, a guard that thought MECM was current*. §55's queue was empty. The
work came from the one class Phase 11 §4 listed and §6 never queued, because `check_renames.py` already guarded it.

| Topic | The name | What the owner's page said |
|---|---|---|
| `cloud` *Cloud Rosetta Stone* | GCP's infrastructure as code: Deployment Manager | Support ended on 31 March 2026, and Google points its users to Infrastructure Manager, which runs Terraform. The domain's own IaC topic had said so since the twenty-eighth wave |
| `cloud` *GCP Security*, *Azure Security* | Chronicle | Rebranded Google Security Operations on 25 April 2024; the API kept the old name |
| `cloud` *GCP Observability* | The operations suite, formerly Stackdriver | Google Cloud Observability; no dated notice of that rename was found |
| `cloud` *AWS Security Stack*, *CSPM*, *Azure Security* | Security Hub, aggregating findings and checking benchmarks | That service is Security Hub CSPM now. The name Security Hub belongs to a newer service, generally available since 2 December 2025, that correlates findings into exposures |
| `devops` *Terraform* | Terraform Cloud | HCP Terraform since 22 April 2024 |
| `endpoint` *Microsoft Configuration Manager (MECM)* | Titled Microsoft Endpoint Configuration Manager, with a release roughly three times a year | Microsoft Configuration Manager since October 2022, one of the Intune family; three versions a year until 2022 and two a year since, 2609 the latest |
| `endpoint`, `sec`, `redteam`: six mentions in six topics | WDAC | App Control for Business, previously called Windows Defender Application Control |
| `script` *Microsoft Graph From PowerShell* | MSOnline and AzureAD "retired or retiring" | Microsoft scheduled MSOnline to stop working between April and May 2025, and Q&amp;A answers since report it refusing even Global Admins; AzureAD was scheduled to stop from mid-October 2025. No notice confirms either, and the card now says what was scheduled |

**The registry.** Its 27 entries became 33. Seven were added, among them Chronicle, Terraform Cloud, WDAC and
Deployment Manager. One was removed: Docker Swarm mode, whose direction Docker's own page reverses. Three current names
were corrected, SCCM's, System Center Configuration Manager's and Facebook Workplace's, the last now marked closed. An
entry can record a closure as well as a rename: `closed` holds the month a product shut down, and after it neither of
its names is current. Phase 11 §10 is what this says about the guard.

**MECM stays the site's word.** The owner's own reference names MECM, and so do most of the admins the site is written
for. The topic took Microsoft's name in its title and says once which name is which; its 49 other mentions keep the
word, and the guard does not list MECM, by decision.

**The stamps.** `stamp_freshness.py --only` re-derived 381 untouched stamps in the six domains this wave edited, most
of them into September: blame's answer moved when the branch merged `main`, and the text did not. They were restored,
and a new mode, `--touched`, stamps only what differs from HEAD, which here was seventeen topics.

**The queue.** The registry's other twenty-three current names, each re-checked against its owner's page: this wave
checked four and all four were wrong, though each was checked because something had already flagged it. Then the
comparison tables as a class of their own, the Rosetta table and the analog columns in `cloud`'s security topics,
because a table naming other vendors' products in passing is where two of this wave's names hid after their own topics
had been corrected. Stackdriver joins the registry once a dated source for its renames is found. CrackMapExec's two
mentions in `pentest` were left: its successor is a fork, not a rename, and no page about it was read. The next dated
claims fall due in February.

## 57. What shipped — the fifty-first wave, the registry's other current names

Recorded below as *Session — the fifty-first wave, twenty-three names that held*. §56's queue, its first item: every
`data/renames.json` entry the fiftieth wave had not checked, read on its owner's page.

| Entries | The owner's page | Result |
|---|---|---|
| Thirteen Microsoft names: Entra ID twice, Entra Connect, Microsoft 365, Sentinel, Defender for Endpoint, Defender for Office 365, Purview Information Protection, Defender for Cloud Apps, Defender for Cloud, the Purview portal, Teams and modern authentication | Microsoft Learn's overview page for each | All current. Sentinel's overview now spends sixteen mentions on the Defender portal, a move of console, not of name |
| Five Google names: Workspace, Chat, Cloud Run functions, and allowlist and blocklist from the developer style guide | Google's product pages, the Cloud Run functions documentation and the style guide's word list | All current; the word list offers denylist and excludelist beside blocklist, and trustlist and safelist beside allowlist |
| AWS Quick | AWS's user guide, *What is AWS Quick?* | Current |
| main branch | GitHub's *About branches*: a new repository's default branch is named main | Current |
| Elastic Security, Nessus Essentials and X | Elastic's, Tenable's and X's own pages | Current |

**The yield was where the flags were.** Twenty-three held, and the four the fiftieth wave found wrong were the four a
reading had flagged. That is the opposite of §9's experience with dated claims, where a re-check of everything found
fourteen wrong of seventy-eight, and the likely reason is the kind of claim. A current name is a brand, and vendors
announce brands; most of the fourteen were defaults, limits and menu paths, which vendors change quietly.

**Each entry now says when it was checked.** Every entry carries `checked`, the month its current name was last read on
its owner's page, the way a fact anchor does, and `check_renames.py --list` prints them least recently checked first.
No gate reads the field: Phase 11 §3's finding stands, and the list is a queue, not a check.

**The queue.** The comparison tables, §56's second item. Then the dated claims due in February, and the registry's
names with them.

## 58. What shipped — the fifty-second wave, the comparison tables

Recorded below as *Session — the fifty-second wave, two cells and a word put back*. §57's queue: the tables that name
other vendors' products in passing, where two of the fiftieth wave's names had hidden.

Thirty tables have a header naming a vendor, an *analog* or an *equivalent*, twenty-three of them in `cloud`. Each was
read cell by cell, and the cells whose product showed any sign of moving were read on their owners' pages.

| Topic | The cell | What the owner's page said |
|---|---|---|
| `cloud` *Cloud Rosetta Stone* | Azure's CDN: Front Door / CDN | Azure CDN Standard from Microsoft (classic) takes no new profiles and retires on 30 September 2027; Front Door is Microsoft's CDN |
| `cloud` *Cloud Cost Control* | GCP's anomaly detection: budget anomaly alerts | Cloud Billing's cost anomaly detection, which compares usage costs with the account's own spending history |
| `cloud` *Cloud Rosetta Stone* | Azure's data warehouse: Synapse | Current: Microsoft's overview describes Azure Synapse with no retirement |

Both wrong cells sat in the column for the vendor the table was not about, the same place the fiftieth wave's
Deployment Manager and Chronicle had been.

**And a word put back.** The census found a query the fiftieth wave had broken after its own census closed. The
MSOnline card was reworded to say what Microsoft *scheduled* instead of asserting what it did, the rewording dropped
*retired*, the word the reader types, and `msonline retired` went from answered to nothing: the census row pushed with
that wave overstated by one. The card now says Microsoft *scheduled MSOnline to be retired*, which keeps both the
honesty and the word. The census is not part of `make check`, so an edit made after it closes can break a query with
every gate green, and `query_probe.mjs --check-plan` belongs last, after the final edit.

**The queue.** None from the comparison tables. The next dated claims fall due in February, and the registry's current
names with them.

## 59. What shipped — the fifty-fourth wave, two certifications the roadmap still sent people to

Recorded below as *Session — the fifty-fourth wave, an exam retiring in four days*. §58's queue was empty; the work
came from a census of the exam codes the site names outside its exam paths, which were all read this month. One of
them, AZ-500, had retired.

| Where | What it said | What Microsoft's pages said |
|---|---|---|
| `eng` *Cert Roadmaps*, the Azure row | AZ-900, then AZ-104, then AZ-500, with MS-102 for a mostly Microsoft 365 estate | AZ-500 retired on 31 August 2026, with SC-500, Cloud and AI Security Engineer Associate, recommended in its place; MS-102 retires on 30 November 2026, with AB-650, Microsoft 365 Certified: AI Services Administrator Associate |
| `eng` *Cert Roadmaps*, the renewal table | Microsoft: AZ-104, AZ-500, MS-102 renew yearly | The rule holds, and now names AZ-104, SC-500 and AB-650 |
| The MS-102 exam path | Read from the study guide in November 2026 | Now says when MS-102 retires, what Microsoft recommends instead, and that a certification already earned stays valid until it expires |

**The source was a roundup, not a page per exam.** Microsoft's *Credentials roundup: June 2026* lists seventeen
retiring certifications with a recommended replacement for each, and the certification pages confirm the two the site
named. The rename registry took AZ-500, AZ-800 and AZ-801, all three already retired. MS-102 waits for its own
retirement and for a path to replace it.

**The queue.** An AB-650 path, read from its study guide, with the m365 header tag and MS-102's registry entry moving
to it in the same wave. The guide gives 35 to 40% of the exam to managing and securing AI services, Microsoft 365
Copilot and agents, which the site has barely written about, so its gaps will be most of that section.

## 60. What shipped — the fifty-fifth wave, an AB-650 path and the gaps it shows

Recorded below as *Session — the fifty-fifth wave, the exam that replaces MS-102*. §59's queue.

AB-650, *Administering Microsoft 365 and AI Services*, is what Microsoft recommends in place of MS-102. Its study guide,
last updated 13 July 2026, has three skill areas, and the path takes them in order: 36 steps over topics that exist.

| Skill area | Weight | Steps | What the site has |
|---|---|---|---|
| Configure and manage Microsoft 365 tenants and workloads | 20 to 25% | 12 | The tenant, licensing, service health, mailboxes, Teams and SharePoint, from MS-102's path, with Teams call quality for network connectivity and the oversharing topic for preparing SharePoint for Copilot |
| Govern and secure Microsoft 365 tenants and workloads | 40 to 45% | 18 | All of it: Entra identities, roles, PIM and administrative units, authentication and Conditional Access, Defender for Office 365, and Purview's DLP, labels and retention |
| Manage and secure AI services in Microsoft 365 | 35 to 40% | 6 | Only the general topics: shadow AI, acceptable use, app consent, entitlement management, agent safety and usage reports |

**The header tags moved too.** `m365` now advertises AB-650 instead of MS-102, and `endpoint` Intune instead of MEM,
a name Microsoft stopped using in October 2022, by the Configuration Manager FAQ the fiftieth wave read. The README
follows. MS-102 joined the rename registry, and the guard now counts *retiring* as a status said aloud.

**The queue: AB-650's gaps, read from Microsoft's pages first.** Most of the third area, and four pieces of the first two.

| Gap | The guide's words | Likely home |
|---|---|---|
| Copilot's tenant settings | Web search for Copilot and Copilot Chat, Copilot Search, self-service purchases, Copilot in admin centers, release preferences, the AI disclaimer, video and image generation, user experiences, Copilot Cowork, third-party AI providers, Copilot connectors | A new `m365` topic |
| Agents and the agent registry | Entra Agent ID's lifecycle workflows, agent access through access packages and Conditional Access, agent owners, agent settings, discovering, reviewing, publishing, blocking and uploading agents, Agent 365's tools | A new `m365` topic |
| Agent 365 | Monitoring agent activity, protecting sensitive data, evaluating compliance gaps | The agents topic, or its own |
| Monitoring AI services | Costs, the admin center's Copilot usage reports, and the Copilot Control System for adoption and service health | A new `m365` topic |
| Copilot data readiness | SharePoint Advanced Management, Microsoft Search in SharePoint, site exclusions | Cards in *Data Governance for AI* |
| Purview for AI | DLP for Copilot, DLP alerts for AI services, Data Security Posture Management | A card in *Sensitivity Labels &amp; DLP*, or a topic |
| Microsoft 365 Backup | Setup, restore and monitoring | A card in *Backup for M365*, which never names the product |
| Copilot in Teams meetings, and network connectivity insights | Transcription and meeting settings; the admin center's connectivity insights | Cards in *Teams Policies* and *Teams Call Quality* |

Each is a product Microsoft built or renamed in 2025 or 2026, so each gets its owner's pages read before a word is
written, and census queries before the topic, the way MS-102's Defender gaps did in the fifteenth to seventeenth waves.

## 61. What shipped — the fifty-sixth wave, Copilot's settings

Recorded below as *Session — the fifty-sixth wave, a page of shortcuts*. §60's first gap: *Microsoft 365 Copilot
Settings — Where Each Control Lives, Web Search &amp; the AI Providers That See Your Data*, a new `m365` topic and the
first in the AB-650 path's third area.

| Card | Read on | What it says |
|---|---|---|
| Where the controls live | *Configure Microsoft Copilot settings in the Microsoft 365 admin center*, last updated 3 November 2026 | Four groups under Copilot ▸ Settings, about half of them shortcuts to the service that holds the real control; AI Administrator is the role Microsoft names |
| Web search | *Data, privacy, and security for web search*, 29 October 2026 | Bing gets a generated query of a few words and the client IP, never the prompt or a file; one Cloud Policy decides, and left unset it means on outside GCC and DoD |
| Third-party models | *Understanding AI functionality and models*, 10 September 2026 | Microsoft-hosted, subprocessor or independent processor, and the last processes data outside Microsoft's Data Protection Addendum |
| Copilot Cowork | *Manage Copilot Cowork for your organization*, 17 November 2026 | Access is a spending policy that selects Cowork; the agent entry left from preview controls nothing |
| Search and connectors | *Manage Microsoft Copilot Search*, and the Copilot connectors overview | Copilot Search needs no setup; synced connectors index into Microsoft Graph, federated ones fetch live through MCP |

**What the guide asks that the settings page does not hold.** Release preferences, the AI disclaimer and video
generation are in AB-650's list and were not on the settings page as read, so they are not in the topic. They join
the monitoring wave's reading rather than being guessed at.

**The queue.** Agents next: Entra Agent ID's lifecycle, the agent registry and Agent 365, the largest block left in the
guide's third area. Then monitoring AI services, costs, usage reports and the Copilot Control System, then the smaller
cards §60 lists.

## 62. What shipped — the fifty-seventh wave, agents and who answers for them

Recorded below as *Session — the fifty-seventh wave, an agent listed twice on purpose*. §61's queue: *Agents in
Microsoft 365 — The Agent Registry, Entra Agent ID &amp; Who Answers for an Agent*, a new `m365` topic.

| Card | Read on | What it says |
|---|---|---|
| The control plane | *Microsoft Agent 365 overview*, 11 November 2026 | One inventory of every agent in four parts, management, governance, security and business value; generally available per user for commercial tenants |
| The agent registry | *Agent Registry in Microsoft 365 admin center*, 6 November 2026 | Four kinds of agent; one Copilot Studio agent can appear twice by design; agents without owners and unmanaged agents are the counts to watch |
| Entra Agent ID | *Governing Agent identities and access*, 16 November 2026 | Four new objects, a human sponsor accountable for each agent, access packages whose expiry notices go to the sponsor; licensed through Microsoft 365 E7, or Agent 365 with Entra P1 or E3 |
| Conditional Access for agents | *Conditional Access for Agents in Microsoft Entra*, 31 July 2026 | Three ways an agent gets a token, each with a different subject, so a policy has to target the identity that actually asks |

**A licensing fact the site had no word for.** Two of the four pages license agent governance through Microsoft 365 E7,
which includes Agent 365 and the Entra Suite. The licensing topic's table stops at E5; it gains E7 when the monitoring
wave reads Microsoft's own plan page, rather than from a mention in a prerequisite line.

**The queue.** Monitoring AI services: Copilot Credits, spending policies and the cost dashboard, the admin center's
Copilot usage reports and the Copilot Control System, with the AI disclaimer and release preferences, which turned out
to live under Copilot ▸ Settings ▸ View all, a view the settings page as read did not list.

## 63. What shipped — the fifty-eighth wave, running Copilot, and a release ring going away

Recorded below as *Session — the fifty-eighth wave, four hours, two days and thirty*. §62's queue: *Running Copilot —
Copilot Credits, Spending Policies, the Usage Report &amp; When Features Arrive*, a new `m365` topic, and an E7 row in
*Licensing Without Tears*.

| Card | Read on | What it says |
|---|---|---|
| Paying for use | *Usage-Based Billing and Cost Management for Copilot Credits* and *Managing AI experiences enabled by usage-based billing*, both 30 October 2026 | Copilot Credits from P3, capacity packs or pay-as-you-go; spending policies by identity or by resource; *Auto-apply new services* is on by default |
| Watching spend and use | *Monitor Copilot Credit spending*, 17 November 2026, the usage report page and *Copilot controls measurement and reporting* | The cost dashboard is four hours behind and the usage report about two days; each answers a different question |
| Telling users, and pacing change | *Turn on AI Disclaimers* and *Configure new Standard and Deferred release options*, 16 November 2026 | The disclaimer reaches six apps and writes a Cloud Policy; Frontier, Standard and Deferred replace Targeted release, frozen this month and retired in January 2027 |
| *Licensing Without Tears*, E7 | *Compare Copilot in E3, E5, and E7*, 28 October 2026 | E7 is E5 plus Microsoft Copilot, the Entra Suite and Agent 365 |

**A retirement the site was spared.** Targeted release is the kind of name §56's census exists to find, and the site
never used it, so nothing was stale. The topic carries it so a reader who meets it in an old runbook learns it is going.

**The queue.** The data side of AB-650's gaps: SharePoint Advanced Management and Restricted Content Discovery for
Copilot's data readiness, where Microsoft has also begun retiring Restricted SharePoint Search, and Purview for AI, DLP
for Copilot and Data Security Posture Management. Then Microsoft 365 Backup, Copilot in Teams meetings and network
connectivity insights, as cards in the topics that own them.

## 64. What shipped — the fifty-ninth wave, hiding a site is not fixing it

Recorded below as *Session — the fifty-ninth wave, a stopgap and its replacement*. §63's queue, as two cards in topics
that already owned the subjects.

| Topic | Card | Read on |
|---|---|---|
| `ai` *Data Governance for AI* | SharePoint Advanced Management as the lasting fix, Restricted Content Discovery as the stopgap that changes no permission, and Restricted SharePoint Search being retired, with no new enablement since 31 July 2026 | Microsoft Learn's SAM overview, 28 October 2026, its Restricted Content Discovery page, 11 October, and its Restricted SharePoint Search page, 6 July |
| `m365` *Sensitivity Labels &amp; DLP* | DLP for Copilot and Cowork, its four controls, and Data Security Posture Management's weekly oversharing assessment | *Microsoft Purview DLP for Microsoft 365 Copilot and Cowork*, 9 November 2026, and DSPM for AI's page, which says a newer DSPM has replaced it |

**The console census earned its keep.** The first card named the SharePoint admin center with no date beside it, and
`check_volatility.py` counted a fourth candidate. It was a real console path, so it took a span, and the count is back
to three.

**The queue.** AB-650's last three gaps, each a card in the topic that owns it: Microsoft 365 Backup in *Backup for
M365*, Copilot in Teams meetings in *Teams Policies*, and network connectivity insights in *Teams Call Quality*.

## 65. What shipped — the sixtieth wave, AB-650's last gaps, and the path whole

Recorded below as *Session — the sixtieth wave, the whole site or the file*. §64's queue, as three cards in topics
that already owned the subjects.

| Topic | Card | Read on |
|---|---|---|
| `m365` *Backup for M365* | Microsoft 365 Backup: restore points every ten minutes, recovery windows to ten years, immutable backups, $0.15 per GB per month, and a site restore that rolls back the whole site | *Overview of Microsoft 365 Backup*, 20 November 2026 |
| `m365` *Teams Policies* | Copilot in meetings: during and after, only during, or off, and off also stops recording | *Manage Microsoft Copilot in Teams meetings and events*, 11 August 2026 |
| `m365` *Teams Call Quality* | The admin center's network connectivity page, per office, once the offices are known | *Network connectivity in the Microsoft 365 Admin Center*, 26 June 2026 |

**Every gap the study guide showed is answered.** AB-650's path has 39 steps, and the five waves since §60 wrote three
topics and five cards for the skills it lacked, each from Microsoft's own pages and each measured by census queries
added before it: 24 queries, opening at 0 and closing at 24. The path's description now says so.

**The console census twice.** Two cards in two waves named an admin center without a date, and `check_volatility.py`
counted a fourth candidate both times. A span closed each, which is the census working as written: a console named in
a new card gets dated in the wave that names it.

**The queue.** None from AB-650. The next dated claims fall due in February, and with them the rename registry's
current names and the exam codes, whose retirements Microsoft announces in a roundup rather than on each exam's page.

## 66. What shipped — the sixty-first wave, the exam that replaced AZ-800

Recorded below as *Session — the sixty-first wave, a tag back on the infra domain*. §65's queue was empty; Microsoft's
credentials roundup, read in the fifty-fourth wave, named AZ-802 as the replacement for AZ-800 and AZ-801, whose
retirement in the fourteenth wave had left `infra` with no exam to point at.

AZ-802, *Administering Windows Server*, has a study guide last updated 22 June 2026 and seven skill areas, and the path
takes them in order: 39 steps, every one a topic that exists, most of them in `infra`. The `infra` header tag moves from
*AD DS* back to an exam, *AZ-802*, and the README follows.

**The queue: AZ-802's gaps, read from Microsoft's pages first.**

| Gap | The guide's words |
|---|---|
| Read-only domain controllers | Deploy RODCs and manage account security on them; deploy domain controllers in Azure |
| Azure Files and Azure File Sync | Shares, permissions, File Sync and monitoring it, and migrating DFS and file shares to it |
| Hyper-V's own features | Enhanced Session Mode, PowerShell Direct, nested virtualization, GPU partitioning, Hyper-V Replica, NIC teaming |
| Windows Server storage | Storage Spaces Direct, Storage Replica, SMB over QUIC, SMB Direct, Storage QoS |
| Securing the server | Exploit protection, Credential Guard, SmartScreen, the OSConfig security baseline, Defender for Servers, Protected Users |
| Monitoring tools | Performance Monitor and data collector sets, System Insights, VM Insights, Azure Monitor data collection rules |
| Azure VM access | Just-in-time VM access and Azure Bastion |

## 67. What shipped — the sixty-second wave, the branch office and the cloud as sites

Recorded below as *Session — the sixty-second wave, a comment that moved*. §66's first gap: *Read-Only Domain
Controllers &amp; Domain Controllers in Azure — The Branch Office and the Cloud as Sites*, a new `infra` topic on the
AZ-802 path after FSMO roles.

| Card | Read on | What it says |
|---|---|---|
| Read-only domain controllers | Microsoft Learn's *Active Directory security groups*, 2 July 2025, and its RODC installation page, 12 May 2025 | Everything but passwords; the Allowed group starts empty and the Denied group wins; staging and administrator role separation let a branch technician finish the install |
| Domain controllers in Azure | Azure Architecture Center, *Deploy AD DS in an Azure Virtual Network*, 16 June 2026 | Two zones, static private addresses, Bastion, the database on its own disk, encryption at host, the DCs as the network's DNS, and a site of their own |

**The stamping tool, taught where a topic ends.** The first `--touched` run stamped this month on the topic before the new
one, which nobody had edited. A topic's span runs to the next topic, so it carries whatever sits between them, here
the comment that ends the domain; appending a topic moved that comment out of the old last topic's span, and the
comparison saw a change. `--touched` now compares each topic only up to its own closing tag, and the wrong stamp was
restored before the commit.

**The queue.** AZ-802's next gaps: Azure Files and Azure File Sync, whose pages this wave read ahead, then Hyper-V's own
features, Windows Server storage, securing the server, and its monitoring tools.

## 68. What shipped — the sixty-third wave, the file server that keeps only what is used

Recorded below as *Session — the sixty-third wave, placeholders*. §67's queue, its first item, as a card in `infra`'s
*File Services*, the topic that already taught shares, NTFS permissions and DFS.

| Card | Read on | What it says |
|---|---|---|
| Azure File Sync | *What is Azure Files?* and *What is Azure File Sync?*, both 17 August 2026, and the cloud tiering overview, 9 April 2026 | Shares in Azure over SMB and NFS; File Sync's sync groups, one cloud endpoint and its server endpoints; tiering by free space or by date; recovery by a new server downloading the namespace |

**The card leads with a trap, not a feature.** Cloud tiering leaves placeholders, so anything that opens every file, a
full scan or a file-level backup, recalls the whole share from Azure. The pages say backup moves to Azure Backup's
snapshots; the card says why.

**The queue.** AZ-802's remaining gaps: Hyper-V's own features, Windows Server storage, securing the server, and its
monitoring tools, each read on Microsoft's pages first.

## 69. What shipped — the sixty-fourth wave, Hyper-V's shortcuts

Recorded below as *Session — the sixty-fourth wave, a snapshot of a DC*. §68's queue, its first item, as a card in
`infra`'s *Hyper-V, vSphere &amp; the Open-Source Stack*.

| Card | Read on | What it says |
|---|---|---|
| Hyper-V's own features | Microsoft Learn's pages on PowerShell Direct, nested virtualization (10 June 2025), checkpoints (31 July 2024) and Hyper-V Replica (10 November 2025) | PowerShell into a VM from its host whatever its network; nested virtualization's processor and version floors; production checkpoints by default, and a standard checkpoint's risk to replicated systems such as AD; Replica as manual, asynchronous failover to another site |

**What the guide asked that the card leaves.** Enhanced Session Mode, GPU partitioning, device assignment and NIC
teaming are in AZ-802's list and were not on the four pages read, so they stay queued rather than written from memory.

**The queue.** Windows Server storage, securing the server, and its monitoring tools, then the Hyper-V items above.

## 70. What shipped — the sixty-fifth wave, storage without a SAN and shares without a VPN

Recorded below as *Session — the sixty-fifth wave, distance decides*. §69's queue, its first item, as cards in two
`infra` topics.

| Topic | Card | Read on |
|---|---|---|
| *SAN &amp; Fabric* | Storage Spaces Direct pooling two to sixteen servers' drives, and Storage Replica's synchronous and asynchronous modes | Microsoft Learn's Storage Spaces Direct overview, 11 February 2025, and Storage Replica overview, 22 August 2025 |
| *SMB &amp; NFS at Scale* | SMB over QUIC: TLS 1.3 on UDP 443, opt-in on the server, tried by clients after TCP | Microsoft Learn's *SMB over QUIC*, 24 July 2025 |

**The queue.** AZ-802's last gaps: securing the server, exploit protection, Credential Guard, SmartScreen, the OSConfig
baseline, Defender for Servers and Protected Users; its monitoring tools; and the Hyper-V items §69 left.

## 71. What shipped — the sixty-sixth wave, the server's own defenses

Recorded below as *Session — the sixty-sixth wave, the acronym the reader typed*. §70's queue, its first item, as a new
`infra` topic: *Hardening Windows Server — Credential Guard, Protected Users, the OSConfig Baseline &amp; Defender for
Servers*.

| Card | What it says | Read on |
|---|---|---|
| Credential Guard and Protected Users | Credential Guard isolates the LSA's NTLM hashes, Kerberos TGTs and stored domain credentials with virtualization-based security; a Protected Users member cannot use NTLM, DES or RC4 in pre-authentication, or delegation, and keeps a TGT four hours | Microsoft Learn's *Credential Guard*, 27 April 2026, and *Protected Users Security Group in Windows Server*, 27 June 2025 |
| The Windows Server 2025 security baseline | Three roles through OSConfig, on Windows Server 2025 only, with drift control that fights Group Policy over a setting both manage | Microsoft Learn's *Configure Security Baselines for Windows Server 2025*, 15 June 2026 |
| Defender for Servers and exploit protection | Defender for Cloud's plan for machines in Azure, other clouds and on premises, with Plan 2's agentless scanning; exploit protection from Windows Server 1803, spread as XML through Group Policy, with an audit mode | Microsoft Learn's Defender for Servers overview, 13 November 2026, and its exploit protection page, 25 March 2025 |

The topic opens AZ-802's security area in the path, before BitLocker, which takes the path from 40 steps to 41. It links
both ways to `infra`'s *Server Hardening Baseline*, the short list it deepens rather than repeats, and to Kerberos in
operations, privileged access management, `endpoint`'s security baselines and Azure Arc.

**A number that had stopped.** The *Related links* row's mainland read 1,553 from the twenty-eighth wave on, while the
linked topics it belongs to went from 1,569 to 1,573. Measured again it is 1,558: every linked topic except `math`'s
sixteen, which is what the row says it is.

**The queue.** SmartScreen was in §70's list and no page about it was read, so it stays queued. Then AZ-802's monitoring
tools: Performance Monitor's data collector sets, System Insights, VM Insights and Azure Monitor's data collection rules;
access to Azure VMs through just-in-time access and Bastion; and the Hyper-V items §69 left.

## 72. What shipped — the sixty-seventh wave, counters, forecasts and rules

Recorded below as *Session — the sixty-seventh wave, a policy, not a pipe*. §71's queue, its first two items: SmartScreen,
as a card in the hardening topic, and AZ-802's monitoring tools, as a new `infra` topic, *Monitoring Windows Server —
Performance Monitor, Data Collector Sets, System Insights &amp; Azure Monitor*.

| Card | What it says | Read on |
|---|---|---|
| SmartScreen, in *Hardening Windows Server* | Reputation checks on sites, downloads and apps; a warning users can bypass by default, so *Warn and prevent bypass*; no cover for files on internal shares | Microsoft Learn's SmartScreen overview, 3 November 2026, and its settings page, 27 May 2026 |
| Performance Monitor and data collector sets | Record the counters for a problem that comes and goes; `logman` builds, starts, imports and exports the sets, and `logman create counter`'s options set what and how long | Microsoft Learn's pages on `logman` and `logman create counter`, which apply to Windows Server 2025, and on Windows Admin Center's server tools |
| System Insights | Forecasting on the server itself, Windows Server 2019 and later, four capabilities every day at 3 a.m., each result an event: 151, 148, 150, 149 or 132 | Microsoft Learn's System Insights overview, 2 June 2025, and its management page, 4 June 2025 |
| Azure Monitor for servers | Host metrics free, guest data through enhanced monitoring and the Azure Monitor agent; a data collection rule as a policy, joined to each server by an association | Microsoft Learn's data collection rules overview, 20 October 2026, and *Monitor virtual machines in Azure*, 26 May 2026 |

**The name the exam uses.** AZ-802 asks for VM Insights. The address of Microsoft's VM insights overview now redirects
to *Monitor virtual machines in Azure*, which calls turning it on *enhanced monitoring* and keeps VM insights as the
name of a Performance view. The card gives both names and says which is which.

**A sentence a row was owed.** The *Dated claims* row records each wave's anchors in a sentence, and the sixty-sixth
wave changed the row's numbers without writing one. It is written now.

**Not a gap.** Entra Password Protection for AD DS is in AZ-802's security list, and `m365` has taught it since an
earlier wave, from the same Microsoft page this wave fetched again.

**The queue.** Just-in-time VM access and Azure Bastion, which AZ-802 lists under managing Windows Server VMs in Azure
and the site names only in passing; then the Hyper-V items §69 left, Enhanced Session Mode, GPU partitioning, device
assignment and NIC teaming; SMB Direct and Storage QoS from the storage area; and Windows Firewall's connection security
rules, which nothing on the site mentions.

## 73. What shipped — the sixty-eighth wave, no port facing the internet

Recorded below as *Session — the sixty-eighth wave, billed from the hour it is deployed*. §72's queue, its first item,
as a card in `cloud`'s *Azure Networking* topic, which the AZ-802 path already takes.

| Card | What it says | Read on |
|---|---|---|
| Reaching the VMs | JIT VM access, in Defender for Servers Plan 2, keeps the management ports denied and opens them to an approved requester's address for a set time; Azure Bastion reaches a network's VMs by private address over TLS on 443, in four SKUs, from a subnet of its own named AzureBastionSubnet, at least a /26 | Microsoft Learn's just-in-time overview, 3 July 2026, *What is Azure Bastion?*, 4 February 2026, and Bastion's configuration settings, 3 November 2026 |

**An anchor the console census read.** The Bastion anchor first said *Azure portal*, as the page does, and the census
counts a console name in an anchor as it does in prose: the topic became a fourth candidate. The anchor says *the
portal's web client* now, which is still the page's meaning.

**The queue.** The Hyper-V items §69 left, whose pages this wave read ahead: Enhanced Session Mode, Discrete Device
Assignment, GPU partitioning and Switch Embedded Teaming. Then SMB Direct and Storage QoS, and Windows Firewall's
connection security rules.

## 74. What shipped — the sixty-ninth wave, a device passed through pins the VM

Recorded below as *Session — the sixty-ninth wave, PCIe is not PCI*. §73's queue, its first item, as a card in
`infra`'s Hyper-V topic.

| Card | What it says | Read on |
|---|---|---|
| The host's hardware, in a VM | Enhanced session mode through VMConnect for local drives, clipboard and USB devices; Discrete Device Assignment for a whole GPU or NVMe device, losing live migration, save and restore, dynamic memory and the cluster; GPU partitioning on Windows Server 2025, which keeps live migration; Switch Embedded Teaming, up to eight identical adapters | Microsoft Learn's pages on VMConnect's local resources, 18 February 2025, Discrete Device Assignment, 19 February 2025, and GPU partitioning, 18 July 2025, and the Azure Local host network page, 15 January 2026, which its Windows Server switch page links for SET |

**Where Microsoft keeps SET now.** The Windows Server link for Switch Embedded Teaming redirects to Azure Local's host
network requirements, and the NIC Teaming overview's old address returns 404. The card cites the page Microsoft links,
and says that LBFO is unsupported *on Azure Local*, which is what that page says, rather than widening it to every
Windows Server.

**What the guide asked that the card leaves.** AZ-802 asks for NIC teaming inside the VM as well as on the host, and no
page read covers teaming in the guest, so it stays queued rather than written from memory.

**The queue.** SMB Direct and Storage QoS, whose pages this wave read ahead, and Windows Firewall's connection security
rules, from the firewall command-line page's IPsec and domain isolation sections. Then NIC teaming in the guest.

## 75. What shipped — the seventieth wave, three cards for three topics

Recorded below as *Session — the seventieth wave, counted in normalized IOPS*. §74's queue, its three items, each a card
in the existing topic it belongs to.

| Topic | Card | Read on |
|---|---|---|
| *SMB &amp; NFS at Scale* | SMB Direct: on by default since Windows Server 2012, switched on by SMB Multichannel, unusable by a VM's own virtual adapters, and compatible with encryption from Windows Server 2022 | Microsoft Learn's *SMB Direct*, 16 January 2025 |
| *Storage Performance* | Storage QoS: reservations and limits in normalized IOPS, a 256 KB request counting as 32, and aggregated or dedicated policies | Microsoft Learn's *Storage Quality of Service*, 10 October 2016, which applies to Windows Server 2025 |
| `endpoint`'s *Firewall &amp; Removable Media Policy* | Connection security rules, IPsec beside allow and block, and domain isolation requiring the computer's Kerberos identity inbound | Microsoft Learn's *Manage Windows Firewall With the Command Line*, 14 May 2026 |

*Storage Performance* joins the AZ-802 path after the SMB topic, so the storage area takes Storage QoS where the exam
lists it: 42 steps to 43.

**What the rest of the guide asks.** Reading AZ-802's 115 skills against the site found five more with no card:
PowerShell remoting's second hop, SSH Direct for Linux guests, the Hyper-V VM's own configuration (its virtual switch
types, virtual hard disks, integration services and memory), AD delegation, and DNS policies. Their pages come first,
as every gap's have.

**The queue.** The second hop, from the PowerShell team's page this wave read ahead, in the JEA topic. Then the Hyper-V
VM's configuration, from the integration services page also read ahead and the virtual switch page the sixty-ninth wave
read; then AD delegation, DNS policies and SSH Direct, once their pages are found; then NIC teaming in the guest.

## 76. What shipped — the seventy-first wave, the credentials that stop at ServerB

Recorded below as *Session — the seventy-first wave, a phrase that moved a query*. §75's queue, its first item, as a card
in `script`'s JEA topic, which the AZ-802 path already takes.

| Card | What it says | Read on |
|---|---|---|
| The second hop | Why a remoting session to ServerB is denied on ServerC, and the fixes in Microsoft's order: CredSSP, which caches credentials on ServerB; resource-based constrained delegation, set on ServerC; classic constrained delegation; JEA and RunAs; and the KDC's 15-minute negative cache | The PowerShell team's *Making the second hop in PowerShell Remoting*, 9 December 2025 |

**A phrase that moved a query.** The card's verdict said *the Protected Users group*, and `protected users group`, a
query the sixty-sixth wave closed, began finding the card instead of the hardening topic, which had said *Protected
Users … as a group*. The census caught it because `--check-plan` runs over every batch, not only the wave's own. The
topic that owns the subject now says the exact phrase, and both are answered.

**The queue.** The Hyper-V VM's own configuration, from the pages this wave read ahead: the virtual switch's types, the
virtual hard disk's formats and types from `New-VHD`, integration services, and dynamic memory from `Set-VMMemory`.
Then AD delegation, DNS policies and SSH Direct, and NIC teaming in the guest.

## 77. What shipped — the seventy-second wave, the settings every VM has

Recorded below as *Session — the seventy-second wave, managed from the host*. §76's queue, its first item, as a card in
`infra`'s Hyper-V topic, its third since the sixty-fourth wave.

| Card | What it says | Read on |
|---|---|---|
| The VM's own settings | External, internal and private virtual switches; VHD or VHDX by extension, and dynamic, fixed or differencing disks; integration services, on at both ends and managed from the host; dynamic memory's startup, minimum, maximum, buffer and priority | Microsoft Learn's pages on creating a virtual switch, 29 January 2025, Hyper-V's overview, 28 July 2025, `New-VHD` and `Set-VMMemory`, both 20 December 2016, and integration services, 18 February 2025 |

**What the pages did not say.** None of the five defines an internal or a private switch in a sentence, so the card says
what they do say: an external switch reaches the physical network and can be shared with the host, NAT runs on an
internal switch, and private switches are one of Hyper-V's tools for isolation. A definition from memory would have been
easy and is not what a dated claim is for.

**The queue.** AD delegation, from Microsoft's page on delegating through OUs, and DNS policies, from its overview, both
read ahead; then the spelling gate's `-isational` gap and its corrections; then SSH Direct, for which no Microsoft page
has been found, and NIC teaming in the guest.

## 78. What shipped — the seventy-third wave, the narrowest grant that does the job

Recorded below as *Session — the seventy-third wave, first match wins*. §77's queue, its first two items, as cards in
two `infra` topics already on the AZ-802 path.

| Topic | Card | Read on |
|---|---|---|
| *AD DS Boundaries* | Delegation through OUs: a group, an OU, a task; grants as narrow as a password reset; the defaults left to service administrators; and the create right, which carries every attribute of what is created | Microsoft Learn's *Delegating Administration by Using OU Objects*, 12 May 2025 |
| *Windows DNS Administration* | DNS policies: client subnets, zone scopes and recursion scopes; query resolution and zone transfer policies at server or zone level; first match wins; the server level can only deny or ignore | Microsoft Learn's *DNS Policies Overview*, 23 June 2022, which applies to Windows Server 2025 |

**Where AZ-802 stands.** Of the five gaps the seventieth wave found in the guide's 115 skills, four now have cards: the
second hop, the VM's own configuration, AD delegation and DNS policies. SSH Direct is the fifth, and no Microsoft page
for it has turned up on Learn's search or in its Hyper-V pages; with NIC teaming in the guest it is the path's last open
item, and both wait for a page rather than memory.

**The queue.** The spelling gate's `-isational` and `-isable` gap: *organisational* and *recognisable* pass because the
`-ise` rule's suffixes stop at `-isation`, and a scan found about forty such words in prose. The gate learns the
suffixes first, with fixtures, and the corrections follow in the same wave.

## 79. What shipped — the seventy-fourth wave, a suffix list that stopped short

Recorded below as *Session — the seventy-fourth wave, organizational*. §78's queue, a gate's gap, found while reading a
topic for a card.

**The gap.** `check_spelling.py`'s `-ise` rule took a word whose British `-ise` was followed by `e`, `es`, `ed`, `ing`,
`er`, `ers`, `ation` or `ations`, and nothing else. *Organisational* is `organis` + `ation` + `al`, so the rule's
closing boundary failed and the word passed, twenty-eight times, with *recognisable* twelve times beside it. The gate
said *0 British spellings* throughout, which was true of what it was asked.

| Change | Where |
|---|---|
| The suffix list gains `ational`, `ationally`, `able`, `ably`, `ability` and `abilities` | `ISE_RE` |
| Eight fixtures: four the rule must convert, and four it must not, `advisable`, `improvisational`, `revisable` and `disable` | The self-test, 163 fixtures to 171 |
| *Practisable* joins the dictionary as *practicable*, since the rule would have made it *practizable*; the one sentence that used it now says *something you can practice* | `IRREGULAR`, and `productivity` |
| 39 corrections by `--fix`, in 16 files, and four by hand inside `grc`'s and `threat`'s ASCII diagrams, which the gate does not read | 37 topics stamped |

**A title moved a slug.** One correction was in a topic's name, *Resilience Engineering &amp; Organizational Memory*,
and a name is a slug: the topic fell off its path and out of its related links until the old slug was recorded as an
alias and the two data files followed, as the retitles before it did. The measured rows caught it within one build:
*Learning paths* counted one topic off a path, and *Orphans* one more.

**SSH Direct, closed without a card.** Learn's search finds *SSH Direct* only in the AZ-802 and AZ-800 study guides,
on no documentation page, so there is nothing to cite and it is recorded as a skill the guide names and Microsoft does not
document. NIC teaming inside the guest stays open on the same terms.

**The queue.** MD-102's guide, updated 16 August 2026, read again the way AZ-802's was. Its candidates, each to be
confirmed against the site before it counts as a gap: Quiet Time policies, enrollment time grouping, Samsung Knox Mobile
Enrollment, specialty devices (Teams Rooms, HoloLens 2, Zebra) with Android firmware-over-the-air updates, custom
compliance with PowerShell, BitLocker recovery key rotation, and Intune's troubleshooting pane.

## 80. What shipped — the seventy-fifth wave, MD-102 read a second time

Recorded below as *Session — the seventy-fifth wave, one user on one screen*. §79's queue: MD-102's study guide, updated
16 August 2026, read against the site the way the seventieth wave read AZ-802's.

**What the second reading found.** Seventy-six skills, checked by their own words and by the words the site would use.
Seven have nothing behind them, and one more, the device query, has a single table cell:

| Gap | The guide's words | Home |
|---|---|---|
| Custom compliance | Extend device compliance by using PowerShell | *Compliance Policies Deep*, this wave |
| BitLocker key rotation | Rotate BitLocker recovery keys | *BitLocker at Scale*, this wave |
| The troubleshooting pane | Collect device diagnostics … including using the Troubleshooting blade | *Microsoft Intune*, this wave |
| Enrollment time grouping | Target a profile by using assignment filters and enrollment time grouping | Queued |
| Samsung Knox Mobile Enrollment | Configure enrollment for Android devices by integrating Intune with Samsung Knox Mobile Enrollment | Queued |
| Quiet Time | Configure Quiet Time policies for Android and iOS apps | Queued |
| Specialty devices and Zebra's FOTA | Teams Rooms, HoloLens 2 and Zebra profiles; Android firmware-over-the-air | Queued |

| Card | What it says | Read on |
|---|---|---|
| Custom compliance | A discovery script and a JSON file inside the policy, one script per policy, results that count for Conditional Access, and the four error codes 65007 to 65010 | Microsoft Learn's *Use custom compliance settings in Microsoft Intune*, 2 November 2026 |
| Key rotation | The BitLocker key rotation device action on Windows 10 1909 or later, the three policy settings it needs, and what deleting a device's Intune object does to BitLocker | Microsoft Learn's *Encrypt Windows devices with BitLocker using Intune*, 26 November 2025 |
| The help desk's view | The Troubleshooting + support pane for the Help desk operator role, its tabs, and what it does not capture | Microsoft Learn's *Use the Troubleshooting Dashboard*, 14 June 2024 |

**The queue.** Enrollment time grouping, Samsung Knox Mobile Enrollment and Quiet Time, from Microsoft's pages; then
the specialty devices with Zebra's firmware updates; then the device query's single cell, if Microsoft's page for it
can be found, since its old address now returns 404.

## 81. What shipped — the seventy-sixth wave, the group before the device

Recorded below as *Session — the seventy-sixth wave, the JSON the portal calls optional*. §80's queue, its first two
items, as cards in two `endpoint` topics.

| Topic | Card | Read on |
|---|---|---|
| *Microsoft Intune* | Enrollment time grouping: a static security group, owned by the Intune Provisioning Client, that the device joins during enrollment, so required apps and policies arrive at once rather than up to eight hours later | Microsoft Learn's *Set up enrollment time grouping*, 24 June 2026 |
| *iOS &amp; Android Enterprise* | Samsung Knox Mobile Enrollment: a Knox account approved in one to two business days, a profile naming Intune, the custom JSON with the enrollment token, and devices from a reseller or the Knox Deployment App | Microsoft Learn's *Enroll devices in Microsoft Intune with Samsung Knox Mobile Enrollment*, 1 December 2023 |

**Where Microsoft's Intune pages are moving.** Learn's search now returns Intune pages under new addresses, such as
`/intune/device-enrollment/` and `/intune/app-management/`, while the `/intune/intune-service/` addresses this wave and
the last read still answer. The anchors cite titles and dates, not addresses, so nothing on the site depends on which
of the two survives.

**The queue.** MD-102's specialty devices, Teams Rooms, HoloLens 2 and Zebra, with Zebra's firmware-over-the-air
updates; then Quiet Time, once a page is found. plan.md is 89 lines short of the 8,000 that reopen the fifth risk,
about two waves; when it crosses, the oldest session records move to the archive.

## 82. What shipped — the seventy-seventh wave, devices with no person behind them

Recorded below as *Session — the seventy-seventh wave, a room cannot do MFA*. §81's queue, its first item, as a card in
`endpoint`'s *Shared, Kiosk &amp; Frontline Devices*.

| Card | What it says | Read on |
|---|---|---|
| Specialty devices | Teams Rooms under compliance and Conditional Access, but not MFA on Windows or sign-in frequency anywhere; HoloLens as a Windows Holographic for Business device; Zebra's settings through OEMConfig; Zebra LifeGuard OTA firmware through Intune | Microsoft Learn's pages on Teams Rooms' supported policies, 6 July 2026, Windows Holographic, 17 March 2025, Zebra's Mobility Extensions, 27 June 2024, and Zebra LifeGuard Over-the-Air, 23 July 2026 |

**What the page did not say about HoloLens 2.** The first draft said HoloLens 2 runs plain Windows Holographic until an
Edition Upgrade profile raises it. Microsoft's page says the upgrade applies to devices on Windows Holographic and names
HoloLens, not HoloLens 2, so the card says that instead.

**Another gap in the spelling gate.** The shared-devices topic's own card says *enrol*. The dictionary lists *enrolment*
but not *enrol* or *enrols*, and a scan for its other single-`l` and doubled-`l` relatives found *tunnelling* and
*tunnelled* eleven times between them, with *funnelled*, *equalling*, *counselling*, *aluminium* and *wilful* once each. *Spectre* and *Lustre* are the
names of a CPU flaw and a file system, and *analogue* and *towards* are standard American English too, so those stay.

**The queue.** The dictionary entries and their corrections; then MD-102's last open items, Quiet Time and the device
query, once Microsoft pages for them are found; and the archive step, which this wave's record brings within one wave.

## 83. What shipped — the seventy-eighth wave, a dictionary that says it is one

Recorded below as *Session — the seventy-eighth wave, enroll*. §82's queue, its first item.

| Change | Where |
|---|---|
| Twenty entries: *enrol*, *enrols*, *wilful*, *wilfully*, *skilfully*, *aluminium*, and the doubled-`l` inflections of *tunnel*, *funnel*, *channel*, *counsel*, *equal*, *dial* and *marshal* | `IRREGULAR`, 84 entries to 104 |
| Eight fixtures: four that convert, and four American forms that must survive | The self-test |
| 27 corrections by `--fix` in 11 files, `acronyms.json` among them | 16 topics stamped |
| The acronym page's mock dialog, fixed where it is written | `gen_acronym_domain.py` |
| The calculus cheat sheet, regenerated from `math` | `CALCULUS-CHEAT-SHEET.md` |

**A commit made before its gates were read.** The wave's first commit went in with the gate run's exit status printed
beside it and unread: `gen_cheatsheet.py --check` had failed, because the cheat sheet is generated from `math`, where
two of the corrected words live. The commit was not pushed. It was amended with the regenerated file once all 45 gates
passed, and the commit step now tests the exit status instead of printing it.

**The queue.** An SC-500 path. The site has named SC-500 as AZ-500's successor since the fifty-fourth wave, in the
certification roadmap, and has no path for it, where AB-650 and AZ-802 each got one from their study guides. Then
MD-102's Quiet Time and device query, once Microsoft pages for them are found.

## 84. What shipped — the seventy-ninth wave, an SC-500 path and the gaps it shows

Recorded below as *Session — the seventy-ninth wave, AZ-500's successor gets its path*. §83's queue, its first item.

SC-500, *Implementing End-to-End Security Controls for Cloud and AI Workloads*, is what Microsoft recommends in place of
AZ-500, which retired on 31 August 2026. Its study guide, last updated 13 May 2026, has four skill areas, and the path
takes them in order: 39 steps over topics that exist.

| Skill area | Weight | Steps | What the site has |
|---|---|---|---|
| Manage identity, access, and governance | 20 to 25% | 12 | PIM, Conditional Access, authentication, app consent, managed identities, Key Vault, Azure Policy and RBAC, backup and infrastructure as code |
| Secure storage, databases, and networking | 25 to 30% | 6 | Azure's storage, SQL and networking topics, hybrid VPN, ZTNA, and Network Watcher in the troubleshooting playbook |
| Secure compute | 20 to 25% | 13 | AI oversharing, DSPM for AI, agents and Entra Agent ID, agent safety, Arc, Defender for Servers, App Service and Functions, Kubernetes and containers, WAF and API security |
| Manage and monitor security posture | 20 to 25% | 8 | CSPM, vulnerability management, attack surface, Log Analytics, SIEM, data collection rules, Defender XDR and Security Copilot |

**The queue: SC-500's gaps, read from Microsoft's pages first.** Each is a product the site never names, which a
search of every data file confirmed:

| Gap | The guide's words | Likely home |
|---|---|---|
| Defender for Cloud's own plans | Defender CSPM, regulatory compliance, the workload protection plans for storage, databases, containers, Key Vault and AI services, the Data and AI security dashboard, and AWS and GCP connectors | A new `cloud` topic |
| Microsoft Sentinel's machinery | Workspaces and roles, the content hub, data connectors, syslog and CEF, Windows Security events through data collection rules and WEF, custom tables, automation rules and playbooks, retention | A new topic |
| AI workloads in Azure | The AI gateway in API Management for Microsoft Foundry, Foundry's agent guardrails, real-time protection for Copilot Studio agents | A new topic |
| Network services | Azure Virtual Network Manager's network access policies, Virtual WAN security, Microsoft Entra Private Access | Cards in *Azure Networking* and *ZTNA* |
| VM security | Secure boot, vTPM, integrity monitoring and the security type; Azure Machine Configuration | A card in *Azure Compute &amp; Storage* or *Azure Arc* |
| Data controls | Azure SQL auditing; storage access policies | Cards in the Azure storage and database topics |

## 85. What shipped — the eightieth wave, coverage is a table, not a switch

Recorded below as *Session — the eightieth wave, a portal the anchor named first*. §84's queue, its first item, as a new
`cloud` topic: *Microsoft Defender for Cloud — Foundational vs Defender CSPM, the Workload Plans &amp; Regulatory
Compliance*, after *Azure Security*, which had made the general point that the workload plans are separate toggles.

| Card | What it says | Read on |
|---|---|---|
| The two CSPM plans | Foundational CSPM, free, with the benchmark and the secure score; Defender CSPM, paid, with attack paths, the security graph and agentless scanning; AWS, GCP, Arc and three DevOps platforms; serverless billing from April and July 2026 | Microsoft Learn's Defender for Cloud overview, 10 August 2026, and its CSPM page, 11 September 2026 |
| The workload plans | One plan per resource type; Storage's malware scanning and SAS misuse, Key Vault's anomaly alerts, AI Services' Prompt Shields alerts, text tokens only, and a trial capped at 75 billion tokens | Microsoft Learn's pages on Defender for Storage, 28 June 2026, Key Vault, 20 August 2025, and AI threat protection, 19 May 2026 |
| Regulatory compliance | Standards made of controls, controls made of recommendations, and the grayed controls no tool can test | Microsoft Learn's *Regulatory compliance standards in Microsoft Defender for Cloud*, 9 September 2024 |

**A portal the anchor named first.** The overview opens with Defender for Cloud's move into the Defender portal. The first
draft put that only in a fact anchor, and the console census, which reads anchors, counted the topic as a fourth
candidate. The move is worth a reader's knowing, so the prose says it now, inside a dated span.

**And a stale claim found next door.** Reading Microsoft Sentinel's pages for the next wave showed that *Azure Security*'s
card on Sentinel costs still describes the analytics, Basic and Archive tiers. Microsoft's table-tier page, updated 2 July
2026, describes two: the analytics tier, thirty days by default and up to two years, and the Data Lake tier, up to twelve
years in all, read through KQL and Spark jobs. It does not mention archive.

**The queue.** Microsoft Sentinel's machinery as SC-500 lists it, from the pages this wave read ahead: roles, the content
hub, connectors, syslog and CEF through the Azure Monitor agent, automation rules, and the two tiers, with *Azure
Security*'s stale card corrected in the same wave.

## 86. What shipped — the eighty-first wave, two tiers where there had been three

Recorded below as *Session — the eighty-first wave, an archive that is now a lake*. §85's queue, as a new `cloud`
topic, *Microsoft Sentinel — Roles, the Content Hub, Connectors, Automation Rules &amp; Two Data Tiers*, and one
correction in the topic beside it.

| Card | What it says | Read on |
|---|---|---|
| Roles, and where Sentinel lives | Reader, Responder, Contributor, Playbook Operator and Automation Contributor, assigned on the workspace's resource group; Sentinel only in the Defender portal after 31 March 2027 | Microsoft Learn's Sentinel roles page, 7 January 2026, and the notice on its content and automation pages |
| Content and connectors | The content hub's solutions and standalone items; syslog and CEF through the Azure Monitor agent, a Linux log forwarder and a data collection rule, and the roles each step needs | Microsoft Learn's *Microsoft Sentinel Content and Solutions Overview*, 27 May 2025, and its syslog and CEF via AMA page, 2 July 2026 |
| Automation rules | Triggers on incidents and alerts, conditions, and actions from tasks to closing, with a playbook only when the response leaves Sentinel | Microsoft Learn's automation rules page, 16 October 2024 |
| Data tiers and retention | The analytics tier, thirty days to two years; the Data Lake tier, up to twelve years, read through KQL and Spark jobs | Microsoft Learn's *Manage tables, tiers, and retention in Sentinel*, 2 July 2026 |

**The correction.** *Azure Security*'s card on Sentinel's costs said a Basic table could not feed scheduled analytics
rules the same way and an archived table had to be restored before it could be searched. Microsoft's table page now
describes two tiers and no archive, so the card says the analytics tier feeds rules and hunting and the Data Lake tier is
read by jobs, with an anchor saying which page it was checked against.

**The queue.** SC-500's AI workloads in Azure: the AI gateway in API Management for Microsoft Foundry, Foundry's agent
guardrails, and real-time protection for Copilot Studio agents. Then Virtual Network Manager, Virtual WAN and Entra
Private Access; trusted launch and Machine Configuration; and Azure SQL auditing with storage access policies.

## 87. What shipped — the eighty-second wave, a gateway governs only what passes through it

Recorded below as *Session — the eighty-second wave, the path the traffic takes*. §86's queue, its first item, as a new
`cloud` topic after Microsoft Sentinel: *Securing AI Workloads in Azure — the AI Gateway, Foundry Guardrails &amp;
Copilot Studio's Real-Time Protection*.

| Card | What it says | Read on |
|---|---|---|
| The AI gateway | API Management's AI gateway, a set of capabilities rather than a product: managed identities instead of keys, OAuth through the credential manager, content safety on prompts, token limits per caller, load balancing with a circuit breaker, and logging | Microsoft Learn's *AI gateway capabilities in Azure API Management*, 29 May 2026 |
| Foundry and the gateway | Approved models reach Foundry projects as connected models behind stable aliases; Azure AI Gateway and API Management are two kinds of hub; Foundry no longer links API Management itself; a direct backend call bypasses every policy | Microsoft Learn's *Configure Azure AI Gateway in your Foundry resources*, 9 November 2026 |
| Foundry guardrails | Controls made of a risk, intervention points and an action; four intervention points, two of them for agents only; blocking levels; an agent's guardrail fully overrides its model's; groundedness detection retiring on 30 April 2027 | Microsoft Learn's *Guardrails and controls overview in Microsoft Foundry*, 2 November 2026 |
| Copilot Studio agents | Built-in prompt injection protection, and real-time protection: an outside endpoint asked to allow or block each tool call, for generative orchestration only, failing open after one second unless set to block | Microsoft Learn's page on external threat detection for Copilot Studio custom agents, 1 June 2026 |
| Watching AI posture | Defender for Cloud's Data and AI security dashboard, and the five protections it needs before it shows everything | Microsoft Learn's *Data and AI Security Dashboard*, 1 May 2025 |

**A page newer than the guide.** SC-500's study guide, from May, asks for the AI gateway in API Management for Foundry.
Foundry's own page, updated in November, describes Azure AI Gateway as a resource type of its own and says Foundry no
longer creates links to API Management from its pages, while API Management is not deprecated. The card says both,
inside a dated span, rather than the guide's wording alone.

**The path's description.** The SC-500 path's blurb still listed Defender for Cloud's plans, Sentinel's content hub and
Foundry's guardrails as gaps, two waves after the first was filled. It now names the four that are left.

**The queue.** Azure Virtual Network Manager, Virtual WAN and Microsoft Entra Private Access, as cards in *Azure
Networking* and *ZTNA*; then trusted launch and Machine Configuration; then Azure SQL auditing and storage access
policies.

## 88. What shipped — the eighty-third wave, rules above the rules

Recorded below as *Session — the eighty-third wave, a query that answered before its card*. §87's queue, its first item,
as two cards in existing topics.

| Card | What it says | Read on |
|---|---|---|
| Governing many networks, in *Azure Networking* | Virtual Network Manager's network groups and configurations, its security admin rules evaluated before any NSG, Allow, Deny and Always Allow, and one configuration per region; Virtual WAN's secured hub, and routing intent for internet and private traffic | Microsoft Learn's Virtual Network Manager overview, 29 July 2026, its security admin rules page, 9 January 2026, *What is a secured virtual hub?*, 28 January 2026, and the routing intent page, 27 August 2026 |
| Microsoft's version, in *ZTNA* | Entra Private Access: private FQDNs and addresses reached through the Global Secure Access client and a private network connector; Quick Access as a transition state, and per-app apps for segmentation | Microsoft Learn's *Learn about Microsoft Entra Private Access*, 12 March 2026, and *How to configure Quick Access for Global Secure Access*, 25 March 2026 |

**A query that answered before its card.** The first draft's *virtual network manager security admin rules* already
matched, through words *Azure Networking*'s other cards happened to hold, so it measured nothing. It was replaced with
*security admin configuration*, which missed, before either card was written.

**A port the page misnames.** Microsoft's list of high-risk ports describes port 23 as TFTP, which runs on 69 and is
listed there too; 23 is Telnet's. The card names only ports whose descriptions are not in doubt.

**The path's description** now names trusted launch and Machine Configuration as SC-500's only gaps left.

**The queue.** Trusted launch, with secure boot, vTPM, integrity monitoring and the security type, and Azure Machine
Configuration; then Azure SQL auditing and storage access policies.

## 89. What shipped — the eighty-fourth wave, the boot and the inside of the box

Recorded below as *Session — the eighty-fourth wave, the templates are where it hides*. §88's queue, its first item, as
two cards in existing `cloud` topics.

| Card | What it says | Read on |
|---|---|---|
| Trusted launch, in *Azure Compute &amp; Storage* | Secure Boot, the vTPM and boot integrity monitoring through the Guest Attestation extension, with Defender for Cloud's recommendations and alert; the default for new Gen2 VMs, and the template setting that decides it | Microsoft Learn's *Trusted Launch for Azure virtual machines*, 25 September 2026 |
| Machine Configuration, in *Azure Arc* | Azure Policy reaching inside the OS on Azure VMs and Arc servers alike: guest assignments, up to 50 a machine, and the three enforcement modes; the Linux upgrade from November 2026 in a dated span | Microsoft Learn's *What is Azure Machine Configuration?*, 7 November 2025 |

**Two queries that measured nothing.** As in the last wave, the first draft's *azure machine configuration* already
matched, through common words in other cards, and was replaced with *guest configuration*, which missed, before either
card was written. Broad two- and three-word queries are matching more often as the site grows; the census keeps the
narrower one when the broad one cannot fail.

**One link.** *Azure Compute &amp; Storage* and *Hardware Root of Trust* now point at each other: the census's *boot
integrity monitoring* found the root-of-trust topic first, and the two explain one boot chain from two ends.

**The path's description** now names Azure SQL auditing and storage access policies as SC-500's last gaps.

**The queue.** Azure SQL auditing, for SQL Database and SQL Managed Instance, and storage access policies, as cards in
the Azure database and storage topics. That closes §84's list.

## 90. What shipped — the eighty-fifth wave, SC-500's list closed, and a headline wrong for three waves

Recorded below as *Session — the eighty-fifth wave, 0 unexplained, which was 1*. §89's queue, the last of §84's list,
as two cards in existing `cloud` topics, and a census defect found on the way.

| Card | What it says | Read on |
|---|---|---|
| Auditing, in *Azure Databases* | A server audit covers every database, and a database audit beside it audits twice; server-level alone unless a database needs its own destination, retention or events; the July 2025 rebuild into one server session and one `master` folder, and database-level auditing for many busy databases; three limits; Managed Instance's SQL Server Audit to a URL | Microsoft Learn's *Auditing for Azure SQL Database* and *Auditing policy at the server and database level*, both 5 October 2026, and *Get started with Azure SQL Managed Instance auditing*, 15 April 2026 |
| Access policies, in *Azure Compute &amp; Storage* | A stored access policy binds a service SAS, so it can be changed or revoked without regenerating the account key; five a resource, up to 30 seconds to apply, never an account or user delegation SAS; disallowing Shared Key | Microsoft Learn's *Define a stored access policy*, 31 January 2023, and *Grant limited access to data with shared access signatures (SAS)*, 27 February 2026 |

**SC-500's list is closed.** Every row of §84's gap table now has its topic or cards, and the path's description says
the gaps the guide showed have been filled, naming each.

**A headline that was wrong for three waves.** The census query *the database is slow* returned exactly 60 topics at
the eighty-first wave's commit, measured again here from a worktree, and 61 after the eighty-second wave's AI workloads
topic, which lists databases in one card and says *slow or down* in another. Sixty-one is wide, a wide query with no
recorded verdict is unexplained, and the *Reader questions answered* row said **0 unexplained** through three records
while the census printed one. `--check-plan` passed each time, because it checks the row's numbers by containment and a
1 is always somewhere in a cell that long. This wave found it only because its own auditing card briefly turned the
query into a miss, which printed its name.

Two changes. The query now carries a *wide by one, and inherent* note, the verdict an earlier wave gave *is the attacker
still in*: only *database* and *slow* survive the stop list, both ordinary words here, and the wanted topic is in the set.
And `--check-plan` now reads the headline's two claims where they stand, the first bold *answered of queries* and the
first bold *N unexplained*, so a headline cannot be satisfied by a digit elsewhere in the cell; four fixtures cover it,
27 in all. The row's prose had said ten wide results since the eighty-second wave, and says eleven.

**The queue.** MD-102's Quiet Time and device query, the two items §83 left waiting for Microsoft pages: look for the
pages again, and write the cards if they exist.

## 91. What shipped — the eighty-sixth wave, a page that moved rather than one that was missing

Recorded below as *Session — the eighty-sixth wave, the device query page was at a new address*. §90's queue, half of
it, as one card.

| Card | What it says | Read on |
|---|---|---|
| Device query, in *Microsoft Intune — Cloud MDM &amp; MAM* | A KQL query run live on one corporate-owned, Entra-joined Windows device over WNS; the tables and the subset of KQL it accepts; 128 KB of result and 15 queries a minute; remote actions from the results; the checks Microsoft says it should replace a remote control session for | Microsoft Learn's *Device query*, 1 September 2026 |

**Why it was missing.** The seventy-fifth wave recorded device query's page as a 404. Microsoft has moved Intune's
documentation to a new tree under `learn.microsoft.com/intune/`, and the page is now under its advanced analytics
section; Learn's own search found it, where the old addresses still return 404. Quiet Time is still not found, by the old
addresses or by search, and stays parked.

**The queue.** An AZ-104 path, from Microsoft's study guide, skills measured as of 17 April 2026: the site has a
*Running Azure* path but no exam path for Azure's administrator, the most common Azure exam. Then SC-200 and SC-300,
whose guides were updated in October 2026.

## 92. What shipped — the eighty-seventh wave, an AZ-104 path and the gaps it shows

Recorded below as *Session — the eighty-seventh wave, Azure's administrator gets a path*. §91's queue, its first item.

AZ-104, *Microsoft Azure Administrator*, had no path, though the site's Azure topics were written for exactly that
reader. Its study guide, skills measured as of 17 April 2026, has five skill areas, and the path takes them in order: 21
steps over topics that exist.

| Skill area | Weight | Steps | What the site has |
|---|---|---|---|
| Manage Azure identities and governance | 20 to 25% | 7 | Entra basics, self-service password reset, guests and B2B, RBAC scopes and Azure Policy, admin roles, tagging and cost control |
| Implement and manage storage | 15 to 20% | 3 | Azure Core, storage accounts with redundancy, lifecycle rules, SAS and stored access policies, and Azure Files in *File Services* |
| Deploy and manage Azure compute resources | 20 to 25% | 3 | Bicep and ARM, choosing compute, and App Service, Functions and Container Apps |
| Implement and manage virtual networking | 15 to 20% | 3 | *Azure Networking*, hybrid connectivity and peering, and the troubleshooting playbook's Network Watcher |
| Monitor and maintain Azure resources | 10 to 15% | 5 | Azure Monitor and KQL, monitoring VMs, backup strategy, restore testing and DR, and Update Manager |

**The queue: AZ-104's gaps**, each a product or feature the site never names, which a search of every data file
confirmed:

| Gap | The guide's words | Likely home |
|---|---|---|
| Azure Backup and Site Recovery | A Recovery Services vault and a Backup vault, backup policies, backup and restore, Site Recovery and failover to a secondary region, backup reports and alerts | A new `cloud` topic |
| Blob and file data protection | Blob versioning, soft delete for blobs, containers and file shares, Azure Files snapshots, object replication | Cards in *Azure Compute &amp; Storage* |
| Storage tools and access | AzCopy and Storage Explorer; storage firewalls and virtual networks; identity-based access for Azure Files | Cards in *Azure Compute &amp; Storage* and *File Services* |
| Azure Monitor's alerting | Action groups and alert processing rules; Connection monitor in Network Watcher | Cards in *Azure Monitor, Log Analytics &amp; KQL* |
| Azure DNS, and Azure Advisor | Azure DNS zones; Advisor's cost recommendations beside budgets and alerts | Cards in *Azure Networking* and *Cloud Cost Control* |

## 93. What shipped — the eighty-eighth wave, backup and recovery as two services

Recorded below as *Session — the eighty-eighth wave, a lock that cannot be corrected*. §92's queue, its first item, as a
new `cloud` topic after *Azure Automation &amp; Update Manager*: *Azure Backup &amp; Site Recovery — Two Vaults, Deletion
That Waits, and a Failover You Have Rehearsed*.

| Card | What it says | Read on |
|---|---|---|
| The two vaults | A Recovery Services vault for VMs, SQL Server in VMs and on-premises servers, with Cross Region Restore; a Backup vault for blobs, disks and PostgreSQL, through its managed identity; vaulted data out of production's reach; Backup is data protection and Site Recovery is failover | Microsoft Learn's Azure Backup overview, 16 September 2026, and its two vault overviews, both 9 October 2026 |
| Protecting the copy | Soft delete for 14 days, enhanced soft delete always on, immutability and its irreversible lock, multi-user authorization through Resource Guard, the three Backup roles, encryption and threat detection | Microsoft Learn's *Overview of security and cyber recovery in Azure Backup*, 16 November 2026 |
| Site Recovery | Replication between regions and from on premises, its frequencies, application-consistent recovery points, planned and unplanned failover, recovery plans, and drills that leave replication running | Microsoft Learn's *About Site Recovery*, 23 September 2026 |

**The queue.** AZ-104's next gaps from §92: blob and file data protection, versioning, soft delete, snapshots and object
replication, as cards in *Azure Compute &amp; Storage*; then the storage tools and access, AzCopy, Storage Explorer,
storage firewalls and identity-based access for Azure Files.

## 94. What shipped — the eighty-ninth wave, which deletion each protection undoes

Recorded below as *Session — the eighty-ninth wave, three switches for three deletions*. §93's queue, its first item, as
two cards in existing topics.

| Card | What it says | Read on |
|---|---|---|
| Protecting blob data, in *Azure Compute &amp; Storage* | Microsoft's three basic protections, an account lock, container soft delete and blob soft delete, and what each does not cover; versioning, snapshots, immutability policies and object replication, and Azure Backup for losing the account | Microsoft Learn's *Data protection overview*, 2 October 2026, and *Object replication for block blobs*, 10 September 2026 |
| Protecting Azure Files, in *File Services* | Share snapshots for single files, 200 a share for up to ten years; share-level soft delete, on by default, 7 days by default and up to 365; what neither covers | Microsoft Learn's *Use Azure Files Share Snapshots*, 26 October 2026, and *Azure File Share Soft Delete*, 20 July 2026 |

**The path's description** no longer lists blob versioning and object replication among AZ-104's gaps.

**The queue.** AZ-104's storage tools and access: AzCopy and Storage Explorer, storage firewalls and virtual network
rules, and identity-based access for Azure Files. Then Azure Monitor's action groups, alert processing rules and
Connection monitor; then Azure DNS and Azure Advisor.

## 95. What shipped — the ninetieth wave, who may reach the account, and how the data moves

Recorded below as *Session — the ninetieth wave, a page dated 2019 describing 2026*. §94's queue, its first item, as
three cards in existing topics.

| Card | What it says | Read on |
|---|---|---|
| Network rules, in *Azure Compute &amp; Storage* | The storage firewall's four kinds of allowance, virtual network rules with their service endpoint, IP rules, resource instance rules and trusted service exceptions; the service endpoint that moves a subnet off its IP rule; a rule that admits a client still needs authorization | Microsoft Learn's *Firewall rules and network access control for Azure Blob, Data Lake, Queue, and Table Storage*, 23 October 2026 |
| Moving data, in *Azure Compute &amp; Storage* | AzCopy v10 for scripted copies and sync, with Entra ID or SAS credentials; Storage Explorer for people; Azure Storage Mover for migrations past a terabyte | Microsoft Learn's *Get started with AzCopy*, 5 November 2026, and *Get started with Storage Explorer* |
| Identity-based access, in *File Services* | Kerberos from one of three identity sources per storage account, AD DS, Entra Domain Services or Entra Kerberos; share-level and file-level permissions; SMB only | Microsoft Learn's *Overview of Azure Files identity-based authentication for SMB access*, 18 September 2026 |

**A page with an old date.** Storage Explorer's page carries an `ms.date` of 8 November 2019 while describing releases
that need a .NET 10 runtime. The site's convention cites `ms.date`, so the anchor does, and says in the same breath what
the page describes; the card claims only what has not changed, that Storage Explorer is a desktop app for Windows, macOS
and Linux.

**The queue.** Azure Monitor's action groups, alert processing rules and Connection monitor, as a card in *Azure
Monitor, Log Analytics &amp; KQL*; then Azure DNS and Azure Advisor, which close AZ-104's list.

## 96. What shipped — the ninety-first wave, the three parts of an alert

Recorded below as *Session — the ninety-first wave, silence that ends by itself*. §95's queue, its first item, as a card
in *Azure Monitor, Log Analytics &amp; KQL*, which had one card before it.

| Card | What it says | Read on |
|---|---|---|
| Alerting | Alert rules fire, action groups notify and automate, up to five a rule and shared between rules, and alert processing rules add or suppress action groups as alerts fire, for maintenance windows and for alerts no rule created; Connection monitor's reachability tests along a path | Microsoft Learn's *Overview of Azure Monitor alerts*, 8 July 2026, *Create and manage action groups in Azure Monitor*, 21 July 2026, *Alert processing rules for Azure Monitor alerts*, 24 April 2026, and *Connection Monitor Overview*, 6 November 2026 |

**Two words.** The card says text message, not SMS, because the dictionary reads SMS as Systems Management Server,
and it names the alert types as Microsoft does. The AZ-104 path's description is down to two gaps.

**The queue.** Azure DNS, as a card in *Azure Networking*, and Azure Advisor beside budgets, as a card in *Cloud Cost
Control*, which close AZ-104's list. Then SC-200 and SC-300, whose study guides were updated in October 2026.

## 97. What shipped — the ninety-second wave, AZ-104's list closed

Recorded below as *Session — the ninety-second wave, a budget that only warns*. §96's queue, the last of §92's list, as
two cards in existing `cloud` topics.

| Card | What it says | Read on |
|---|---|---|
| Azure DNS, in *Azure Networking* | Public DNS for internet domains; Private DNS zones that answer only for linked virtual networks, with autoregistration and links across regions; split-horizon names; the DNS Private Resolver for on premises; and no `.local` | Microsoft Learn's *Azure DNS Overview*, 28 July 2026, and *Azure Private DNS*, 16 December 2025 |
| Azure's own tools, in *Cloud Cost Control* | A budget alerts on actual or forecast cost and can call an action group, but never stops consumption; Advisor recommends in five categories and can take a day to notice a fix | Microsoft Learn's *Tutorial: Create and manage budgets*, 26 June 2025, and *Introduction to Azure Advisor*, 2 December 2024 |

**AZ-104's list is closed.** Every row of §92's gap table now has its topic or cards, and the path's description says
so, naming each.

**The queue.** An SC-300 path, from Microsoft's study guide with skills measured as of 28 October 2026: identity, the
site's deepest ground outside endpoint management, with gaps already visible in a first search, among them custom
security attributes, cross-tenant synchronization, certificate-based authentication, protected actions, Application
Proxy and terms of use. Then SC-200.

## 98. What shipped — the ninety-third wave, an SC-300 path and the gaps it shows

Recorded below as *Session — the ninety-third wave, identity gets its own exam path*. §97's queue, its first item.

SC-300, *Microsoft Identity and Access Administrator*, had no path, though identity is the site's deepest ground
outside endpoint management. Its study guide, skills measured as of 28 October 2026, has four skill areas, and the path
takes them in order: 20 steps over topics that exist. The guide disagrees with itself once: its summary weights
authentication and access at 25 to 30%, and the section itself says 20 to 25%. The path's description gives both.

| Skill area | Weight | Steps | What the site has |
|---|---|---|---|
| Implement and manage user identities | 20 to 25% | 5 | Entra basics, admin roles, device identity, guests and B2B, Entra Connect and hybrid identity |
| Implement authentication and access management | 25 to 30%, or 20 to 25% | 7 | MFA, passkeys, self-service password reset, Conditional Access and its troubleshooting, ID Protection, and Global Secure Access in *ZTNA* |
| Plan and implement workload identities | 20 to 25% | 5 | Managed identities, app registrations and consent, OAuth and SAML, consent phishing, Defender for Cloud Apps |
| Plan and automate identity governance | 20 to 25% | 3 | Entitlement management and access reviews, privileged access, and Log Analytics for the identity logs |

**The queue: SC-300's gaps**, each a feature the site never names, which a search of every data file confirmed:

| Gap | The guide's words | Likely home |
|---|---|---|
| Protected actions, PIM for Groups, administrative units | Protected actions; PIM for Groups; administrative units | Cards in *Admin Roles &amp; Least Privilege*, which has two |
| Cross-tenant access and synchronization | Cross-tenant access settings; cross-tenant synchronization | A card in *External Collaboration* |
| Certificate-based authentication and registration campaigns | CBA; MFA registration campaigns | A card in *Multi-Factor Authentication* |
| Custom security attributes | Custom security attributes | A card in *Azure Hierarchy, RBAC Scopes &amp; Policy*, beside ABAC |
| Application Proxy | Integration for on-premises apps by using Application Proxy | A card in *ZTNA* |
| Terms of use and connected organizations | Terms of use; connected organizations | A card in *Entra ID Governance* |
| Identity Secure Score and the provisioning logs | Identity Secure Score; sign-in, audit and provisioning logs | A card in *Entra ID — Sign-In &amp; Conditional Access Troubleshooting* |

## 99. What shipped — the ninety-fourth wave, a role made smaller than its name

Recorded below as *Session — the ninety-fourth wave, approval on the group that leads to a role*. §98's queue, its first
two rows, as two cards in existing `m365` topics, and a correction to §98.

| Card | What it says | Read on |
|---|---|---|
| Narrowing a role, in *Admin Roles &amp; Least Privilege* | PIM for Groups makes a group's membership or ownership just-in-time, with the approval, MFA and time limits PIM gives roles, and protected actions put a Conditional Access policy on a permission, asked for at the moment it is used; a table sets both beside administrative units, which narrow where a role applies | Microsoft Learn's *Privileged Identity Management (PIM) for Groups*, 23 April 2026, and *What are protected actions in Microsoft Entra ID?*, 3 November 2025 |
| Across your own tenants, in *External Collaboration* | Cross-tenant synchronization keeps an organization's users in sync between its own tenants: a push from the source, as B2B users, into a target that has to allow it, removed when the person leaves | Microsoft Learn's *What is cross-tenant synchronization in Microsoft Entra ID?*, 2 November 2026 |

**A correction to §98.** Its queue called each row a feature the site never names, and two of them were named.
Administrative units have a whole `m365` topic, *Administrative Units — Delegating Part of the Tenant, and Fencing Off
the Accounts That Matter*, written in the sixteenth wave for MS-102 and already a step on three paths, and this wave's
first-draft query, `administrative units`, repeated one the sixteenth wave had added, which that topic answers. The
query was replaced with `just-in-time group membership`, the card names the topic instead of
repeating it, and the SC-300 path now carries the topic as its third step, after *Admin Roles*: 21 steps. And *External
Collaboration* already had the cross-tenant access policy, a row in its table on per-partner trust; synchronization was
the half that was missing. Every term the rest of the queue names was searched for again across all the data files, and
none of them is on the site.

**The queue.** SC-300's remaining gaps from §98: certificate-based authentication and registration campaigns, in
*Multi-Factor Authentication*; Application Proxy, in *ZTNA*; then custom security attributes, terms of use and connected
organizations, and Identity Secure Score with the provisioning logs. The last may belong beside `m365`'s *Secure Score
&amp; the Tenant Baseline* rather than in the troubleshooting topic §98 named, since Microsoft Secure Score is already
taught there; the wave that writes it decides.

## 100. What shipped — the ninety-fifth wave, a nudge and a published app

Recorded below as *Session — the ninety-fifth wave, the campaign that only helps if the old method goes*. §99's queue, its
first two items, as two cards in existing `sec` topics.

| Card | What it says | Read on |
|---|---|---|
| Entra's own methods, in *Multi-Factor Authentication* | Certificate-based authentication signs people in with certificates from the organization's own PKI directly against Entra ID, with no AD FS, and a registration campaign prompts them after an MFA sign-in to set up a passkey or Authenticator, one of the two at a time for the whole tenant | Microsoft Learn's *Microsoft Entra CBA Overview*, 4 March 2025, and *Run a Registration Campaign to Set Up a Passkey or Microsoft Authenticator*, 15 September 2026 |
| For one web app, in *ZTNA* | Application proxy publishes an on-premises web app at an external URL through the connector Private Access uses, outbound only on ports 80 and 443, for remote users and not the ones already inside | Microsoft Learn's *Publish on-premises apps with Microsoft Entra application proxy*, 10 March 2026 |

**Four sentences changed between the draft and the card**, each because the page said something else or nothing. The
draft called a registration campaign one method per campaign; the page says one method at a time for the whole tenant.
It said a campaign could run as a staged rollout, which the page never says. It called certificate-based authentication
free without the page's own qualification, that enforcing MFA through Conditional Access needs a licensed edition. And
the Application Proxy draft listed header-based apps among those it publishes directly, where the page says they go
through PingAccess, a partner service.

**A correction to the ninety-fourth wave.** Its sentence in the census row said the cross-tenant query found its card
among 13, *not first*. The census lists hits in domain order, so first was never a rank; the sentence now says only
*among 13*.

**The queue.** SC-300's remaining gaps: custom security attributes, in `cloud`'s *Azure Hierarchy, RBAC Scopes &amp;
Policy*, beside ABAC; terms of use and connected organizations, in `m365`'s *Entra ID Governance*; and Identity Secure
Score with the provisioning logs, beside *Secure Score &amp; the Tenant Baseline* or in *Entra ID — Sign-In &amp;
Conditional Access Troubleshooting*.

## 101. What shipped — the ninety-sixth wave, attributes nobody can read and terms everyone must accept

Recorded below as *Session — the ninety-sixth wave, a Global Administrator who cannot read a field*. §100's queue, its
first two items, as a card in `cloud` and one in `m365`.

| Card | What it says | Read on |
|---|---|---|
| Attributes for decisions, in *Azure Hierarchy, RBAC Scopes &amp; Policy* | Custom security attributes are tenant-wide key-value pairs on users and enterprise applications that only their own roles can read, not even a Global Administrator by default, which is what sets them apart from directory extensions, and the attributes Azure ABAC decides on | Microsoft Learn's *What are custom security attributes in Microsoft Entra ID?*, 28 October 2024 |
| At the edges, in *Entra ID Governance* | Terms of use are a Conditional Access grant control, with Entra ID P1, at most 40 per tenant and acceptance that can expire; connected organizations say who outside may request an access package, and the configured ones are the only ones a policy for all configured organizations admits | Microsoft Learn's *Set Up Microsoft Entra Terms of Use with Conditional Access*, 24 March 2026, and *Manage connected organizations in entitlement management*, 15 July 2024 |

The SC-300 path gains *Azure Hierarchy, RBAC Scopes &amp; Policy* as its fourth step, where the guide lists custom
security attributes, under managing Microsoft Entra identities: 22 steps. Its description now names one gap.

**Two things the tools caught.** The acronym annotator expanded JSON inside *JSON Web Token*, which then read as
*JSON (JavaScript Object Notation) Web Token*; the card says JWT instead, and the annotator expanded that. And the console
count went from three to four because a table cell said the admin center creates connected organizations as configured;
the cell now says an administrator does, by hand or through the API, which was the point.

**The queue.** SC-300's last gap: Identity Secure Score, with the provisioning logs the guide names beside the sign-in
and audit logs. After it, SC-200, *Microsoft Security Operations Analyst*, the next Microsoft exam the site has no path
for.

## 102. What shipped — the ninety-seventh wave, SC-300's list closed

Recorded below as *Session — the ninety-seventh wave, a status that earns the points without the work*. §101's queue,
its last SC-300 item, as a card in `m365` and one in `cloud`.

| Card | What it says | Read on |
|---|---|---|
| Identity's own score, in *Secure Score &amp; the Tenant Baseline* | The Identity Secure Score is Entra's percentage against Microsoft's identity recommendations, recalculated daily, with partial credit, and statuses that can hide an action or award its points on someone's word | Microsoft Learn's *What is the Identity Secure Score?*, 9 February 2026 |
| The third log, in *Entra ID — Sign-In &amp; Conditional Access Troubleshooting* | Beside the sign-in and audit logs, the provisioning log shows what Entra created, changed or removed in other systems, step by step, with Skipped among its statuses | Microsoft Learn's *User provisioning logs in Microsoft Entra ID*, 17 March 2025 |

The SC-300 path gains *Secure Score &amp; the Tenant Baseline* as its last step, where the guide ends, on monitoring and
improving the security posture with the Identity Secure Score: 23 steps. Every gap §98 listed that was a gap is now a
card, and the path's description says so, as SC-500's and AZ-104's do.

**The queue.** An SC-200 path, *Microsoft Security Operations Analyst*, from Microsoft's study guide, which the
eighty-seventh wave found current and which is to be fetched again before the path is written; then its gaps.

## 103. What shipped — the ninety-eighth wave, an SC-200 path and the gaps it shows

Recorded below as *Session — the ninety-eighth wave, the analyst's exam gets a path*. §102's queue.

SC-200, *Microsoft Security Operations Analyst*, had no path, though the site's Defender and Sentinel ground was built
for MS-102 and SC-500 and is most of what the exam asks. Its study guide, skills measured as of 21 October 2026 and
fetched again this wave, has three skill areas, and the path takes them in order: 23 steps over topics that exist.

| Skill area | Weight | Steps | What the site has |
|---|---|---|---|
| Manage a security operations environment | 40 to 45% | 11 | Defender XDR's incidents and automated investigation, its alert policies, Defender for Endpoint's onboarding and ASR rules, Microsoft Sentinel's roles, connectors, automation rules and tiers, SOAR, what logs cost, the Windows event IDs worth collecting, Log Analytics and KQL, and detections from requirement through tuning to ATT&amp;CK coverage |
| Respond to security incidents | 35 to 40% | 9 | Triage, Defender for Office 365 in depth, Purview's DLP alerts, Defender for Cloud, Defender for Cloud Apps, Entra ID Protection, identity threat detection, enrichment, and the audit log with Content search |
| Perform threat hunting | 20 to 25% | 3 | Threat hunting, Defender's threat analytics, and the Model Context Protocol that the Sentinel MCP server speaks |

**The queue: SC-200's gaps**, each a feature the site never names, checked this time by counting every term in all the
data files before the list was written, after §98 called two things gaps that were not:

| Gap | The guide's words | Likely home |
|---|---|---|
| Automatic attack disruption and case management | Configure automatic attack disruption; manage security incidents by using case management | Cards in *Defender XDR Incidents &amp; Advanced Hunting* |
| Security Copilot in Defender | Investigate incidents by using agentic AI, including embedded Microsoft Security Copilot | A card in *Defender XDR Incidents &amp; Advanced Hunting* |
| Defender for Endpoint's own controls | Advanced features, custom data collection, device groups and automation levels; device timelines, live response and investigation packages | A card in *Defender for Endpoint &amp; Intune* |
| Windows Event Forwarding | Plan and configure collection of Windows Security events by using WEF | A card in *Windows Event Logs* |
| Sentinel's rule types, anomalies, threat indicators, custom tables and SOC optimization | Scheduled, NRT, threat intelligence and machine learning rules; anomalies; ingest threat indicators; custom log tables; SOC optimization recommendations | Cards in *Microsoft Sentinel* |
| Hunting graphs, the Sentinel graph, notebooks and the Sentinel MCP server | Hunting graphs, including blast radius; Sentinel Graph; notebooks, including the Sentinel MCP Server | Cards in *Microsoft Sentinel* or *Threat Hunting — Assume Breach, Go Looking* |
| Microsoft Graph activity logs | Investigate threats by using Microsoft Graph activity logs | A card in *eDiscovery, Content Search &amp; the Audit Log* |

## 104. What shipped — the ninety-ninth wave, containment nobody approved

Recorded below as *Session — the ninety-ninth wave, the exclusions to set before the first disruption*. §103's queue,
its first two rows, as three cards in `m365`'s *Defender XDR Incidents &amp; Advanced Hunting*.

| Card | What it says | Read on |
|---|---|---|
| Attack disruption | Defender contains the users, devices and apps an attacker controls when it is highly confident an attack is in progress, without waiting for approval; every action can be undone, critical assets can be excluded, and a table lists five of the actions and what takes each | Microsoft Learn's *Automatic attack disruption in Microsoft Defender*, 11 June 2026 |
| Cases | Case management tracks SOC work as incident cases and generic cases, with owners, tasks, an SLA and an audit trail in Log Analytics, only in the Defender portal | Microsoft Learn's *Case management in the Microsoft Defender portal*, 19 August 2026 |
| Copilot in Defender | Security Copilot embedded in the portal summarizes incidents, scripts, files, devices, identities and email, drafts the incident report, and turns natural language into KQL | Microsoft Learn's *Microsoft Security Copilot and Chat in Microsoft Defender*, 17 July 2026 |

The disruption card sits after the topic's automated investigation card, because the contrast is the point: automated
remediation waits on the automation level, and attack disruption does not.

**A change the site had missed.** That automated investigation card, written in the fifteenth wave from the Defender
XDR overview, described automated investigations as something an alert starts and an analyst can watch. Reading ahead
for the next wave, two Defender for Endpoint pages said otherwise: from 1 September 2026 automated investigation and
response no longer runs as a separate investigation experience and cannot be started by hand, its detection and
response run inside Defender's antivirus protection, and a full antivirus scan is the on-demand route. The Defender XDR
overview, dated 28 April 2025, still does not say so, and SC-200's guide, measured on 21 October 2026, still lists
managing it. The card now says both, with an anchor naming the two pages, and the disruption card's opening leans only
on the automation levels, which remain.
Whether the change reaches Defender for Office 365's automated investigations, which *Alert Policies in Defender for
Office 365* names twice as an alert setting, no page read says, so those two mentions stay as they are until one does.
And Microsoft's pages disagree with each other: a third Defender for Endpoint page, on response actions on a device,
dated 23 July 2026, still lists *Initiate automated investigation* among them. The dated notice is the more specific
statement, so the card follows it, and the next wave's card, which reads the response actions page, says which page
still lists the button.

**The queue.** SC-200's next gaps from §103: Defender for Endpoint's own controls, from advanced features and automation
levels to live response and investigation packages; then Windows Event Forwarding; Sentinel's rule types, anomalies,
threat indicators, custom tables and SOC optimization; hunting graphs, notebooks and the Sentinel MCP server; and
Microsoft Graph activity logs.

## 105. What shipped — the hundredth wave, what an analyst can do to one device

Recorded below as *Session — the hundredth wave, check the proxy before isolating*. §104's queue, its first item, as
two cards in `endpoint`'s *Defender for Endpoint &amp; Intune*.

| Card | What it says | Read on |
|---|---|---|
| Response actions | A device's page isolates it, contains an unmanaged one, restricts it to Microsoft-signed code, collects an investigation package or opens a live response session, most of it on Plan 2 only, all of it in the Action center | Microsoft Learn's *Take response actions on a device in Microsoft Defender for Endpoint*, 23 July 2026, and its live response page, 28 July 2026 |
| Device groups | A device group scopes who sees which devices and sets the remediation level, from full remediation to none, with the highest-ranked group winning for a device that matches several | Microsoft Learn's pages on device groups, 2 July 2026, and automation levels, 4 April 2025 |

The response actions page still lists *Initiate automated investigation*, which the automated investigations page says
ended on 1 September 2026, as §104 expected; the card's anchor says so, and the card leaves the button out.

**The queue.** SC-200's remaining gaps: Windows Event Forwarding, in *Windows Event Logs*; Sentinel's rule types,
anomalies, threat indicators, custom tables and SOC optimization; hunting graphs, notebooks and the Sentinel MCP server;
and Microsoft Graph activity logs.

## 106. What shipped — the hundred-and-first wave, forwarding the logs the topic said to forward

Recorded below as *Session — the hundred-and-first wave, the events written before the device joined*. §105's queue,
its first item, as a card in `blueteam`'s *Windows Event Logs — The IDs That Matter*.

| Card | What it says | Read on |
|---|---|---|
| Getting them off the host | Windows Event Forwarding sends the events a subscription selects to a Windows Event Collector, pushed by Group Policy or pulled, from a baseline subscription for every device and a suspect one for a few; it cannot enable a channel or an audit policy, and Sentinel reads Windows events through two connectors, into SecurityEvent and WindowsEvent | Microsoft Learn's *Use Windows Event Forwarding to help with intrusion detection*, 18 August 2025, and Sentinel's data connector reference, 5 February 2026 |

The card sits under the topic's *Blind spot* card, whose verdict already ended on forwarding to a collector, which is why
two first-draft census queries found the topic before the card existed.

**The queue.** SC-200's remaining gaps: Sentinel's rule types, anomalies, threat indicators, custom tables and SOC
optimization; hunting graphs, notebooks and the Sentinel MCP server; and Microsoft Graph activity logs.

## 107. What shipped — the hundred-and-second wave, Sentinel's detections and what feeds them

Recorded below as *Session — the hundred-and-second wave, an anomaly is context, not a finding*. §106's queue, its
first item, as two cards in `cloud`'s *Microsoft Sentinel*.

| Card | What it says | Read on |
|---|---|---|
| Analytics rules | Scheduled rules, the one-minute near-real-time subset, anomaly rules that write to the Anomalies table and never alert, and the single-rule templates for threat intelligence, Fusion and behavior analytics; Microsoft security rules and Fusion switch off once Sentinel is in the Defender portal, and custom detections are now Microsoft's way to write new rules | Microsoft Learn's *Threat detection in Microsoft Sentinel*, 16 October 2024 |
| Feeding and tuning it | Threat intelligence as STIX, through four routes into Sentinel, custom tables ending in _CL that a data collection rule fills, and SOC optimization's recommendations and coverage grades | Microsoft Learn's pages on threat intelligence in Sentinel, 18 August 2025, custom tables in Azure Monitor Logs, 27 August 2026, and SOC optimization, 12 November 2026 |

The detection page carries a date older than what it says: it describes Sentinel leaving the Azure portal after
31 March 2027 and custom detections as the way forward, both later than its 16 October 2024 *ms.date*, so the card cites
that date and the topic's own portal card, written in the eighty-first wave, already agrees.

**The queue.** SC-200's last gaps: hunting graphs and the Sentinel graph, notebooks and the Sentinel MCP server, and
Microsoft Graph activity logs.

## 108. What shipped — the hundred-and-third wave, SC-200's list closed

Recorded below as *Session — the hundred-and-third wave, a hunt with its steps hidden*. §107's queue, SC-200's last
three gaps, as a card in `blueteam` and one in `m365`.

| Card | What it says | Read on |
|---|---|---|
| On Microsoft's stack, in *Threat Hunting — Assume Breach, Go Looking* | Advanced hunting's hunting graph and the Sentinel graph beneath it, with its blast radius view; Jupyter notebooks with Kqlmagic for what the portal cannot do; and Sentinel's hosted MCP server for questions in natural language | Microsoft Learn's pages on the hunting graph, 4 May 2026, the Sentinel graph, 7 August 2026, Jupyter notebooks, 7 March 2024, and Sentinel's support for MCP, 7 May 2026 |
| Graph activity logs, in *eDiscovery, Content Search &amp; the Audit Log* | Microsoft Graph activity logs record every request Graph receives for the tenant, including apps, SDKs and AI clients, through diagnostic settings, with Entra ID P1 and Security Administrator as the least role to set them up | Microsoft Learn's *Access Microsoft Graph activity logs for tenant monitoring*, 25 November 2025 |

Every gap §103 listed is now a card, five waves after the path was written, and the SC-200 path's description says so,
as SC-300's, SC-500's and AZ-104's do. One finding came out of the reading that the queue
never asked for: automated investigation and response's change on 1 September 2026, recorded in §104.

**The queue.** The Microsoft paths the eighty-seventh wave chose are done. Three more study guides were fetched while
this wave's gates ran, and all three are current: SC-401, *Administering Information Security in Microsoft 365*,
measured 28 October 2026; AZ-700, Azure networking, 27 July 2026; and AZ-305, Azure solutions architecture, 17 April
2026. SC-401 comes first, because `m365`'s Purview topics already hold most of what it asks; then its gaps.

## 109. What shipped — the hundred-and-fourth wave, an SC-401 path and the gaps it shows

Recorded below as *Session — the hundred-and-fourth wave, Purview gets its own exam path*. §108's queue, its first item.

SC-401, *Administering Information Security in Microsoft 365*, had no path, though `m365` has carried Purview topics
since the sixteenth wave. Its study guide, skills measured as of 28 October 2026, has three skill areas of equal weight,
and the path takes them in order: 16 steps over topics that exist.

| Skill area | Weight | Steps | What the site has |
|---|---|---|---|
| Implement information protection | 30 to 35% | 6 | Purview's map, data classification, sensitive information types, sensitivity labels, Defender for Cloud Apps, and Exchange's mail flow rules |
| Implement data loss prevention and retention | 30 to 35% | 5 | DLP's design, retention labels against retention policies, holds and archiving, data governance, and why retention is not a backup |
| Manage risks, alerts, and activities | 30 to 35% | 5 | The insider threat program, the audit log and eDiscovery, Defender XDR's queue, data governance for AI, and Copilot's settings with DSPM for AI |

**The queue: SC-401's gaps**, each a term counted across every data file before it was listed, with no hits:

| Gap | The guide's words | Likely home |
|---|---|---|
| Trainable classifiers, Data explorer and Content explorer | Create and manage trainable classifiers; monitor classification and label usage | A card in *Sensitive Information Types &amp; Endpoint DLP* |
| Label publishing policies | Configure and manage publishing policies for sensitivity labels | A card in *Sensitivity Labels &amp; DLP* |
| The Information Protection client and scanner | Plan and implement the client; bulk classification of on-premises data with the scanner | A card in *Sensitivity Labels &amp; DLP* |
| Purview Message Encryption and Advanced Message Encryption | Design and implement both | A card in *Mail Flow — Connectors, Transport Rules &amp; the Path a Message Takes* |
| Adaptive Protection, DLP policy precedence and just-in-time protection | Configure DLP for Adaptive Protection; interpret precedence; configure just-in-time protection | Cards in the two DLP topics |
| Adaptive scopes | Create, configure and manage adaptive policy scopes | A card in *Retention Policies vs Retention Labels* |
| Insider Risk Management's own settings | Connectors, indicators, policy templates, forensic evidence, notice templates | A card in *The Insider Threat Program*, or a new `m365` topic |
| Audit (Premium) and audit retention policies | Assign Audit (Premium) licenses; configure audit retention policies | A card in *eDiscovery, Content Search &amp; the Audit Log* |

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

## Session — the thirty-fourth wave, colors nobody had checked

§39's queue, NIST CSF 2.0 in `grc`. *Content ideas* §40 is the table.

### Read first

NIST's Cybersecurity Framework page, and two documents as the PDFs NIST publishes: CSWP 29, the CSF 2.0 of
26 February 2024, and the CSF 1.1 of 16 April 2018, both extracted with `pdftotext`. The page carrying CSF
2.0's figure of the six functions was rendered with `pdftoppm` and viewed, because a color is not text. Three
queries went into *somebody answerable to an auditor* before the fixes.

### What the documents said that the cards had to carry

CSF 2.0's six functions are Govern, Identify, Protect, Detect, Respond and Recover, and Govern informs how the
other five are prioritized. They hold 22 categories: six under Govern, three under Identify, five under
Protect, two under Detect, four under Respond and two under Recover. Version 1.1 had 23 categories in five
functions, among them Business Environment, Detection Processes and an Improvements category under both
Respond and Recover, none of which is a CSF 2.0 category. NIST's figure colors Govern yellow, Identify blue,
Protect purple, Detect orange, Respond red and Recover green.

### Two kinds of wrong

Of the four wrong names in the categories topic, two were 1.1's, Business Environment and Improvements, and two
are in neither version, *IOC Detection & Alerting* and *Restoration & Validation*. The colors matched no figure
of NIST's that this wave found. The CSF 2.0 topic's own colored rows match none either, but they are styling and
state nothing, so they stay.

### The census

The batch opened at 2 of 3 and closed at 3 of 3. The census as a whole is 738 of 761 with nothing unexplained.

```
2 commits · 4 topics corrected in grc · 3 census queries, 2 of 3 -> 3 of 3
topics 1,629 · dated claims 388 -> 392
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%
```

## Session — the thirty-fifth wave, the exam's words for what was already there

§40's queue, SecAI+'s summary terms. *Content ideas* §41 is the table.

### Read first

CompTIA's SecAI+ page, read in the thirtieth wave and read again for the two domain lines quoted here, and
CompTIA's PenTest+ page, fetched and read. Six queries went into *somebody revising for a CompTIA exam*, with
their wants named after the opening run showed what each reached.

### What the pages said

SecAI+'s AI-assisted security domain lists event triage, alert correlation and response orchestration as
workflows to automate, and threat modeling, behavior analysis and continuous monitoring as places to apply AI in
operations. PenTest+ PT0-003 launched on 17 December 2024 and PT0-002 retired on 17 June 2025.

### Wants named after the run, and said so

The six queries went in without wants, because the question was whether each term reached anything fitting, and
the wants were set from the topics that cover the subjects once the opening showed where the queries landed.
That is weaker than naming the want first, and it is recorded rather than smoothed over: four of the six landed
somewhere reasonable on their own, and the two that did not are the two this wave changed.

### The census

The batch opened at 4 of 6 and closed at 6 of 6, the two it changed finding their topics alone. The census as a
whole is 744 of 767 with nothing unexplained.

```
2 commits · 2 sentences in 2 topics, 1 badge · 6 census queries, 4 of 6 -> 6 of 6
topics 1,629 · dated claims 392 -> 394
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%
```

## Session — the thirty-sixth wave, a tactic split in two

§41's queue, MITRE ATT&amp;CK. *Content ideas* §42 is the table.

### Read first

ATT&amp;CK's Enterprise tactics page, the pages for TA0005 and TA0112, the April 2026 (v19) release notes and the
versions page, all fetched and read, and the pages of the eleven techniques the site cites by ID. Three queries
went into *a SOC analyst or defender* before the cards.

### What the pages said that the cards had to carry

Version 19's release notes call the split of Defense Evasion into Stealth and Defense Impairment its biggest
change, and count fifteen Enterprise tactics. TA0005 keeps its ID under the name Stealth, with 31 techniques
that reduce the chance of detection without touching the controls; TA0112, created on 14 April 2026, holds 18
that degrade or disable them. Version 20.1, of 13 October 2026, is current.

### The census

The batch opened at 1 of 3, the old name already finding the topic, and closed at 3 of 3, each among two. The
census as a whole is 747 of 770 with nothing unexplained.

```
2 commits · 2 cards corrected in 1 topic, 11 technique IDs checked · 3 census queries, 1 of 3 -> 3 of 3
topics 1,629 · dated claims 394 -> 396 · inline style attributes held at the ceiling of 401
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%
```

## Session — the thirty-seventh wave, a report a month old

§42's queue, post-quantum cryptography. *Content ideas* §43 is the table.

### Read first

NIST IR 8547's CSRC pages for the draft and the final, and the final as the PDF NIST publishes, extracted with
`pdftotext`; and NIST's release of 11 March 2025 choosing HQC, all fetched and read. CSRC's address for a FIPS 206
draft returned 404, and nothing here depends on it. Four queries went into *somebody revising for a CompTIA exam*
before the cards.

### What the report said that the cards had to carry

Quantum-vulnerable public-key algorithms are deprecated after 2030 and disallowed after 2035 under NIST's
standards, and the window between is for lower-risk systems with legacy constraints. Federal high value assets
and high impact systems move earlier, to post-quantum key establishment by 31 December 2030 and signatures by
31 December 2031, and federal agencies support TLS 1.3 by 2 January 2030. Symmetric primitives of at least
128-bit strength meet NIST's lowest post-quantum category; the few 112-bit symmetric standards are disallowed in
2030. HQC backs up ML-KEM on different math, with its final standard expected in 2027.

### The census

The batch opened at 1 of 4 and closed at 4 of 4, three alone. The census as a whole is 751 of 774 with nothing
unexplained.

```
2 commits · 1 new card, 1 sentence, 1 table row corrected in 1 topic · 4 census queries, 1 of 4 -> 4 of 4
topics 1,629 · dated claims 396 -> 398
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%
```

## Session — the thirty-eighth wave, a limit that changed in March

§43's queue, public TLS certificate lifetimes. *Content ideas* §44 is the table.

### Read first

The CA/Browser Forum's page for Ballot SC081v3 and its Baseline Requirements for TLS certificates, version
2.3.1, read as the PDF the Forum publishes and extracted with `pdftotext`, and Let's Encrypt's two posts on
ending OCSP, all fetched and read. The ballot page describes the change and its vote; the schedule's exact
dates are in the requirements' sections 6.3.2 and 4.2.1, which is why the PDF was read. Four queries went into
*a Linux or platform engineer* before the card.

### What the documents said that the card had to carry

A certificate issued before 15 March 2026 could be valid for 398 days; from then 200, from 15 March 2027 100,
and from 15 March 2029 47, and the requirements ask CAs not to issue for the maximum by default. Domain
validation can be reused for 200, 100 and finally 10 days on the same dates. All four browser makers voted for
the ballot and no certificate issuer voted against it. Let's Encrypt dropped OCSP URLs from its certificates on
7 May 2025 and turned its responders off on 6 August 2025, citing the privacy cost of a responder that learns
which site each visitor opens.

### The census

The batch opened at 0 of 4 and closed at 4 of 4, two alone. The census as a whole is 755 of 778 with nothing
unexplained.

```
2 commits · 1 new card, 1 sentence corrected in 1 topic · 4 census queries, 0 of 4 -> 4 of 4
topics 1,629 · dated claims 398 -> 400
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%
```

## Session — the thirty-ninth wave, a regulation the site had never named

§44's queue, the EU Cyber Resilience Act. *Content ideas* §45 is the table.

### Read first

The European Commission's Cyber Resilience Act page, last updated on 23 November 2026, and its page on the act's
reporting obligations, both fetched and read. Three queries went into *somebody answerable to an auditor* before
the card.

### What the pages said that the card had to carry

The act, Regulation (EU) 2024/2847, entered into force on 10 December 2024, and its main obligations apply from 11
December 2027. Reporting began on 11 September 2026: a manufacturer that becomes aware of an actively exploited
vulnerability or a severe incident sends an early warning within 24 hours and a notification within 72, and a final
report within 14 days after a fix is available, or a month after the notification for an incident, all through
ENISA's Single Reporting Platform, which reaches the national CSIRT and ENISA together. Open-source stewards report
from December 2027.

### A coincidence the census reported as an answer

`cyber resilience act` opened answered, because the regulatory topic held *cyber*, *resilience* and *act* in
three sentences about other things. The census counted it, which is what the census does; the record says what
it was, because a count cannot.

### The census

The batch opened at 1 of 3 and closed at 3 of 3, the regulation's name alone. The census as a whole is 758 of 781
with nothing unexplained.

```
2 commits · 1 new card and 1 table row in 1 topic · 3 census queries, 1 of 3 -> 3 of 3
topics 1,629 · dated claims 400 -> 401
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%
```

## Session — the fortieth wave, defaults that moved under the cards

§45's queue, numbered frameworks. *Content ideas* §46 is the table.

### Read first

CIS's Controls page and its page for version 8.1, Microsoft Learn's *Detect and remediate RC4 usage in Kerberos*,
and Microsoft Support's KB5073381 for CVE-2026-20833, all fetched and read. Four queries went in before the fixes,
two into *somebody answerable to an auditor* and two into *a SOC analyst or defender*.

### What the pages said that the cards had to carry

CIS describes its Controls, at version 8.1, as a prioritized set of Safeguards; the 18 are the Controls. Microsoft's
updates for CVE-2026-20833 audited RC4 service tickets from January 2026, made domain controllers assume AES when
nothing is configured from April 2026, and removed audit mode in July 2026; an explicit
DefaultDomainSupportedEncTypes value is left as it is, and one that allows RC4 logs KDCSVC event 205.

### The census

The batches opened at 0 of 4 and closed at 4 of 4, all four alone. The census as a whole is 762 of 785 with
nothing unexplained.

```
2 commits · 2 table rows and 1 dictionary note corrected · 4 census queries, 0 of 4 -> 4 of 4
topics 1,629 · dated claims 401 -> 403
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%
```

## Session — the forty-first wave, a thin topic and a first function

§46's queue, the thin topics, and the owner's request to turn on Netlify Functions. *Content ideas* §47 is the
table.

### Read first

Debian's apt-key(8) for bookworm and sources.list(5) for trixie, and DNF's configuration reference, all fetched and
read, for the package card; three queries went into *a Linux or platform engineer* before it. For the function:
the owner's saved copy of the project's Functions page, Netlify's own guidance for writing functions, read through
the connected Netlify tools, and the project's current production deploy, which builds `main` and reports *No
functions deployed*.

### What the function does, and how it was checked

`netlify/functions/health.mts` returns JSON naming the site, the serving deploy's id and context, the region, the
request id and the time, with `no-store` set in code because `netlify.toml`'s header rules do not reach function
responses. It was called with a mock context under Node's type stripping, bundled with esbuild and called again.
The service worker change was checked in a browser over HTTP, because the smoke suite runs over `file://`, where
service workers never start: with the old worker, the second call to a local stand-in for the function returned
the first call's cached answer; with the new one, each call reached the server and nothing was cached.

### The census

The batch opened at 0 of 3 and closed at 3 of 3, all alone. The census as a whole is 765 of 788 with nothing
unexplained.

```
3 commits · 1 new card in 1 topic · 1 function, 1 service-worker rule · 3 census queries, 0 of 3 -> 3 of 3
topics 1,629 · thin 7 -> 6 · dated claims 403 -> 406
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
service worker over HTTP: old worker cached the function's answer, new worker does not
visual 0/2 in this container, unchanged at 10.335% and 10.106%
```

## Session — the forty-second wave, the officers with no number

§47's queue: the visual baseline, then the thin topics, two military lookup cards first. *Content ideas* §48 is the
table.

### Read first

FM 6-0, *Commander and Staff Organization and Operations* (May 2022), from the Army Publishing Directorate, read as
its PDF; the Joint Staff's J-7 page, which refused the fetch and is cited from search results; NVD's record for
CVE-2025-30066, read through NVD's API; and GitHub's *Secure use reference*, *Workflow dependency lockfiles* and
*Enforcing lockfiles* pages. Six queries went into *a learner meeting a subject* and four into *a Linux or platform
engineer* before the cards. For the baseline, CI's own job logs for its last three runs.

### What the sources said that the cards had wrong

The *Staff Functions* verdict made two claims nobody had checked. Its account of which numbers exist where was
right in outline and wrong in detail: no S-5 at most battalions and brigades, and no 7 at all. Its reason for the
missing S8, that a battalion holds no budget of its own, is not in the manual; the card now gives the one that is, the
G-8 setting the funding allocated below it. *Common Codes* called the XO the deputy commander, which FM 6-0 says is
true only usually and only below division. And the first draft of the `devops` card said the attack touched no
victim's repository, which is true of how it reached them and not of what the stolen secrets could do next; it now says
the attacker needed no access to any victim's repository.

### The census

The batches opened at 0 of 10, six zeros and four that found other cards, and closed at 10 of 10, five alone. The
census as a whole is 775 of 798 with nothing unexplained.

```
3 commits · 3 new cards in 3 topics · 1 verdict, 2 table rows and 1 example corrected · 1 test tool change
10 census queries, 0 of 10 -> 10 of 10 · topics 1,629 · thin 6 -> 3 · dated claims 406 -> 411
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%: Playwright 1.63.0 here, 1.56.0 in CI
```

## Session — the forty-third wave, the cards the tables implied

§48's queue: the three thin topics left. *Content ideas* §49 is the table.

### Read first

PostgreSQL's documentation on sorting rows, and the queries themselves, run on PostgreSQL 16.15 and SQLite 3.53.1 in
this container against a tie, a single distinct salary and a NULL; RFC 9110 and RFC 6585 from rfc-editor.org; and the
renewal pages of CompTIA (the renewal policy, the CEU table, the fee table and the higher-level renewal table), ISC2's
member policies, GIAC's renewal page, AWS's recertification page, Google Cloud's Associate Cloud Engineer page and
Microsoft Learn's renewal page, all fetched and read. Nine queries went into three readers before the cards.

### What doing it found

The first two answers to the salary puzzle are the ones most people write, and on Postgres both return 300 for the
input with a NULL in it, because Postgres sorts NULL above every value and `DESC` puts it first. That is a property
of one database, not of SQL, and the card's table says which. The full-stack topic's references were labels from an
organization of the site that no longer exists; nothing checks a parenthesized label, only a cross-reference, so
they are cross-references now. And the measured-state gate passed a stale headline for the length of a build, which
is the one failure a gate that checks numbers should not have.

### The census

The batches opened at 1 of 9, four zeros and four that found other cards, and closed at 9 of 9 after three wording
fixes, two alone. The census as a whole is 784 of 807 with nothing unexplained.

```
3 commits · 3 new cards in 3 topics · 4 dead labels replaced with 8 links · 1 gate fixed
9 census queries, 1 of 9 -> 9 of 9 · topics 1,629 · thin 3 -> 0 · dated claims 411 -> 415
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%: Playwright 1.63.0 here, 1.56.0 in CI
```

## Session — the forty-fourth wave, twelve claims from August

§49's queue was empty, and `check_volatility.py`'s list of the oldest dated claims was the census that reported
something. *Content ideas* §50 is the table.

### Read first

For each claim, its owner's current page: Microsoft Learn's pages on gMSAs, shared mailboxes, message trace and the
What If tool, with the Exchange Online, Exchange Online Archiving and Purview service descriptions; NIST SP 800-57
Part 1 Rev. 5 as its PDF and CSRC's page for it; Regulation S-K Item 106 from the eCFR; Fortinet's November 2026
product matrix; LangChain's 1.0 announcement and LlamaIndex's framework documentation; and Raspberry Pi's price posts
of 2 February and 1 October 2026. Raspberry Pi's product page and news index refused the fetch; the two posts did not.
Five queries went into two readers before the corrections.

### What the re-check found

Seven of twelve had moved or were wrong, four were right and are exact now, and one, a used-hardware price, was
removed because nothing authoritative publishes it. The m365 hold claim was wrong in two topics at once, written the
same way in both. And the census could not have found any of it: `gmsa password length` and `shared mailbox size
limit` reached their topics before the wave, around a wrong unit and a vague limit.

### The census

The batches opened at 2 of 5 and closed at 5 of 5 after one wording fix, one alone. The census as a whole is 789 of
812 with nothing unexplained.

```
2 commits · 12 dated claims re-checked: 7 corrected, 4 confirmed and made exact, 1 removed · 9 anchors added
5 census queries, 2 of 5 -> 5 of 5 · topics 1,629 · dated claims 415 -> 423
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
CI on garrettadams23/Studies#70: every step passed, visual 2/2 under Playwright 1.56.0
visual 0/2 in this container, unchanged at 10.335% and 10.106%: Playwright 1.63.0 here
```

## Session — the forty-fifth wave, consoles and clocks

§50's queue, its `m365` part. *Content ideas* §51 is the table.

### Read first

Microsoft Learn's pages on the `cloud.microsoft` domain, quarantine retention, SharePoint's limits, group expiration
and restore, JSON batching in Graph, Teams guest access and call analytics, Microsoft Support's page on the SharePoint
recycle bin, and Learn's article on the list view threshold. The console addresses were requested one by one, and the
two that refused were confirmed by following Microsoft's own links one hop. Three queries went into *a service desk
engineer* before the corrections.

### What the re-check found

Four of twenty-two had moved, every one of them a number or a mechanism rather than a name: a default retention, an
address, how expiry decides, and whether a window can be changed. The expiry one was the largest, because it was the
card's verdict: Microsoft renews groups in use automatically, which the card never mentioned, and which turns
*nobody reads the warning* from a risk to every team into a risk to the quiet ones.

### The census

The batch opened at 1 of 3 and closed at 3 of 3 after three wording fixes, two alone. One of them was about the
matcher: a four-letter query word must match a whole word, so *automatically* does not answer *auto*, and the card
says *auto-renews*. The census as a whole is 792 of 815 with nothing unexplained.

```
2 commits · 22 dated claims re-checked: 4 corrected, 18 confirmed · 9 anchors added
3 census queries, 1 of 3 -> 3 of 3 · topics 1,629 · dated claims 423 -> 432
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%: Playwright 1.63.0 here, 1.56.0 in CI
```

## Session — the forty-sixth wave, a default that upgrades keep

§51's queue, its `endpoint`, `infra` and `cloud` part. *Content ideas* §52 is the table.

### Read first

Microsoft Learn's pages on Windows Admin Center, the site link replication interval, lingering objects and the
tombstone lifetime, Entra Connect's accidental-delete prevention, Azure Monitor metrics and the DISM uninstall window;
the Evaluation Center's Windows Server 2025 page; Google's storage classes page; and Microsoft's own announcement and
FAQ for the 2026 Microsoft 365 packaging change. One Microsoft troubleshooting page had moved and returned 404; its
replacement was found by search. Two queries went into *a service desk engineer*, measured against the page as built
before the corrections.

### What the re-check found

Two of seventeen needed more than a date. The tombstone default is a property of the forest's age, which the card had
stated as a property of the domain. The Intune Suite change was right in outline and sourced secondhand; Microsoft's
own pages give the exact split and dates, and the anchor cites them now. Six other anchors had named a concept rather
than a page, *Active Directory site link replInterval default and minimum*, and each now names the page it was read on.

### The census

The batch opened at 0 of 2 and closed at 2 of 2 after one wording fix, one alone. The census as a whole is 794 of
817 with nothing unexplained.

```
2 commits · 17 dated claims re-checked: 2 corrected, 15 confirmed, 6 anchors re-sourced · 4 anchors added
2 census queries, 0 of 2 -> 2 of 2 · topics 1,629 · dated claims 432 -> 436
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%: Playwright 1.63.0 here, 1.56.0 in CI
```

## Session — the forty-seventh wave, a route read from the site that serves it

§52's queue, September's last twenty-six claims. *Content ideas* §53 is the table.

### Read first

csvistool.com's page and its published bundle; AWS's IAM page on assuming roles and EC2's page on instance metadata
credentials; NPR's report of the APA's January 2026 papers, psychiatry.org having refused the fetch; NCCIH's tai chi
page; the SANS Internet Storm Center diary on prefetch; MongoDB's limits page; and the PCI SSC document library. Two
queries went in, measured against the page as built before the corrections.

### What the re-check found

One correction and one addition among twenty-six. The cloud-credential card gave an instance role a one-hour default
that AWS documents nowhere; it says what AWS does document now. The DSM card gained the APA's plan for its successor.
The other twenty-four were right, and eighteen of them had cited a repository the session could not read, so they
were checked against the site the links actually open.

### The census

The batches opened at 0 of 2 and closed at 2 of 2, both alone, with no wording fix. The census as a whole is 796 of
819 with nothing unexplained.

```
2 commits · 26 dated claims re-checked: 1 corrected, 1 extended, 24 confirmed · 3 anchors added
2 census queries, 0 of 2 -> 2 of 2 · topics 1,629 · dated claims 436 -> 439 · none older than 2026-10
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%: Playwright 1.63.0 here, 1.56.0 in CI
```

## Session — the forty-eighth wave, a page that answers now

§53's queue, one claim. *Content ideas* §54 is the table.

### Read first

The UAH page itself, fetched from www.cs.uah.edu, which an earlier container's network policy had blocked.

### What the re-check found

The link works and the page is what the owner described. It frames 128-255 as part of ASCII, which the site's own
card on extended ASCII does not, and the anchor records the difference rather than the site echoing it. No census
query: nothing a reader would type changed.

```
1 commit · 1 dated claim re-checked and its page read for the first time · 0 anchors added
topics 1,629 · dated claims 439, every one checked in 2026-11
45 gates green · the browser suites not rerun: the commit changes one HTML comment and a stamp
```

## Session — the forty-ninth wave, a model answer that was wrong

Phase 11's V1 pass, redone. *Content ideas* §55 is the table.

### Read first

Microsoft Learn's Business Premium overview, Remediations page, Conditional Access conditions and ID Protection
overview, the Exchange Online service description read in wave 44, and Microsoft's page for the 2026 Microsoft 365
packaging and pricing update. Two queries went into *a service desk engineer*, measured against the page before the
rewrite.

### What the pass found

Of the twenty-six sentences that tie a feature to a tier, twenty-three were written from Microsoft's pages in waves
15 to 19 and carry anchors. The three that predate those waves were checked, and two needed rewriting. The
licensing table now has the plan most small businesses buy, and the Remediations card names the licenses instead of
a shape of license. Phase 11 gained §9, on why reading a class found none of this and re-checking did.

### The census

The batch opened at 0 of 2 and closed at 2 of 2 after two wording fixes. The census as a whole is 798 of 821 with
nothing unexplained.

```
2 commits · 3 tier claims re-checked: 2 corrected, 1 confirmed · 3 anchors added · Phase 11 §9 written
2 census queries, 0 of 2 -> 2 of 2 · topics 1,629 · dated claims 439 -> 442
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%: Playwright 1.63.0 here, 1.56.0 in CI
```

## Session — the fiftieth wave, a guard that thought MECM was current

§55's queue was empty, so the wave took the class Phase 11 §6 never queued. *Content ideas* §56 is the table.

### Read first

Google's pages for Deployment Manager's deprecation, Google Security Operations and Google Cloud Observability, and
Google staff's notice of the SecOps rebrand on the Google Cloud Community; AWS's Security Hub CSPM guide and its News Blog
post of 2 December 2025; HashiCorp's *What is HCP Terraform?*, after its blog refused the fetch with 429; Microsoft
Learn's App Control for Business page and the Windows 11 IoT Enterprise 24H2 notes, the Configuration Manager FAQ and
the version table in *Updates and servicing*, and the Entra blog's two posts and archive on the PowerShell modules;
Docker's swarm mode page; and Meta's Workplace page. Seven census queries went in before any edit.

### What the census of names found

330 candidate names and version strings returned eight stale names in seventeen topics, and the over-match §8 predicted:
Bard was a druid grade, Pinpoint a verb, Container Registry a phrase describing Harbor. WSUS, OpenVAS and Windows 10
were current names in true sentences, and the other 49 mentions of MECM are the site's word by decision. Re-checking
the Configuration Manager card against Microsoft's version table found a claim the census was not looking for: a
release *roughly three times a year*, true until 2022. And one sentence the wave itself wrote went past its sources:
the PowerShell card said Microsoft *retired* MSOnline, where the pages read give Microsoft's schedule. It says
*scheduled* now, which is §9's rule applied to the wave's own words.

### The census

The batch opened at 3 of 7 and closed at 7 of 7 with no wording fix. The census as a whole is 805 of 828 with nothing
unexplained.

```
2 commits · 8 product names corrected in 17 topics · 1 release cadence corrected · 8 anchors added
registry 27 -> 33: 7 added, 1 removed, 3 current names corrected · check_renames self-test 14 -> 18 fixtures
stamp_freshness.py --touched: 17 topics stamped, where --only had moved 381
7 census queries, 3 of 7 -> 7 of 7 · topics 1,629 · dated claims 442 -> 450
45 gates green · smoke 167 · search 59 · axe 33/33 · resilience 64/64 · mobile 16/16 · backup 3/3
visual 0/2 in this container, unchanged at 10.335% and 10.106%: Playwright 1.63.0 here, 1.56.0 in CI
```

## Session — the fifty-first wave, twenty-three names that held

§56's queue, its first item. *Content ideas* §57 is the table.

### Read first

Twenty-two pages from the names' owners: Microsoft Learn's overviews for Entra, Entra Connect, Microsoft 365, Sentinel,
Defender for Endpoint, Defender for Office 365, Purview Information Protection, Defender for Cloud Apps, Defender for
Cloud, the Purview portal, Teams and hybrid modern authentication; Google's Workspace and Chat pages, the Cloud Run
functions documentation and the developer style guide's word list; AWS's *What is AWS Quick?*; GitHub's *Changing the
default branch* and *About branches*, the second because the first never names the default; and Elastic's, Tenable's
and X's own pages. No census queries: nothing a reader types changed.

### What the re-check found

Nothing wrong. Every current name in the registry is the name its owner uses today, so the fiftieth wave's four were the
whole of the registry's error, and every entry now records the month it was checked.

```
2 commits · 23 registry current names re-checked: 23 confirmed · `checked` on all 33 entries
45 gates green · the browser suites not rerun: the commit changes the registry and a tool's listing, not the page
```

## Session — the fifty-second wave, two cells and a word put back

§57's queue. *Content ideas* §58 is the table.

### Read first

Microsoft Learn's retirement FAQ for Azure CDN Standard from Microsoft (classic), its Azure Front Door overview and its
Azure Synapse Analytics overview, and Google's Cloud Billing page on cost anomalies. Two census queries went in before the
edits.

### What the reading found

Thirty tables and two wrong cells, both in the column for the vendor the table was not about. The census found a third
thing: a query the fiftieth wave's last rewording had broken, after the census that would have noticed had closed.

```
2 commits · 2 comparison-table cells corrected · 1 census query restored · 2 anchors added
2 census queries, 2 of 2 -> 2 of 2 · census 807 of 830 · topics 1,629 · dated claims 450 -> 452
45 gates green · smoke 167 · search 59 · the other suites not rerun: three cells of text, no markup
```

## Session — the fifty-third wave, a census that came back right

§58's queue was empty, so the wave tried the one ageing-claim shape a pattern can require. Phase 11 §11 is the result.

### What was built and read

`check_volatility.py --expiry`: sentences in the future tense about a reached year, deadlines in reached years, and
preview or *latest* states, reported and never failed, with six fixtures in the self-test. Its fourteen sentences were
read one by one, and each of the ten real claims was matched to its fact anchor.

```
2 commits · check_volatility.py --expiry, self-test 11 -> 17 fixtures · 14 sentences read: 10 dated and right, 4 noise
45 gates green · the browser suites not rerun: a tool's report mode and the plan, not the page
```

## Session — the fifty-fourth wave, an exam retiring in four days

§58's queue was empty, so the wave counted the exam codes the site names in prose. *Content ideas* §59 is the table.

### Read first

Microsoft Learn's certification pages for AZ-500, AZ-104, AZ-900, MS-102, MD-102 and Microsoft 365 Fundamentals, the
study guides for AZ-500, SC-500, AB-650 and AZ-802, Microsoft's renewal page, and the *Credentials roundup: June
2026* on the Microsoft Community Hub that both retirement notices link to. Three census queries went in before the edit.

### What the census of codes found

Eight codes outside the exam paths: AZ-104, AZ-500, AZ-900, MD-102, MS-102, PT0-003, SAA-C03 and 220-1101, the last
a citation of the cheat sheet a table came from. Every path itself had been read from its outline this month. AZ-500 had
retired three months before, and MS-102 retires four days after the wave.

```
2 commits · 2 roadmap rows and 1 exam path corrected · 3 retired exams registered · 1 anchor added
3 census queries, 1 of 3 -> 3 of 3 · census 810 of 833 · dated claims 452 -> 453
45 gates green · smoke 167 · search 59 · the other suites not rerun: two table rows and a path's blurb
```

## Session — the fifty-fifth wave, the exam that replaces MS-102

§59's queue. *Content ideas* §60 is the table and the gap list.

### Read first

Microsoft's AB-650 study guide, last updated 13 July 2026, every skill line of it; the MS-102 path for what carries
over; and every `m365` and `ai` topic, read for what each says about Microsoft 365 Copilot. One topic mentions Copilot,
once. No census queries: a path is built from topics that exist, and the gaps get their queries when they are written.

### What building the path found

The first two areas, two thirds of the exam, are the MS-102 path in a new order. The third is almost entirely
unwritten, and it is the part of the exam Microsoft added the new name for. The `endpoint` header had also been
advertising Microsoft Endpoint Manager four years after Microsoft retired the name.

```
2 commits · 1 exam path, 36 steps · 2 header tags and the README corrected · 1 registry entry, guard fixtures 18 -> 19
paths 119 -> 120, steps 2,334 -> 2,370 · 8 gaps queued
45 gates green · smoke 167 · search 59 · axe 33/33 · the other suites not rerun: a path and two tags
```

## Session — the fifty-sixth wave, a page of shortcuts

§60's queue, its first gap. *Content ideas* §61 is the table.

### Read first

Microsoft Learn's Copilot settings page and its pages on web search, AI models and their providers, Copilot Cowork's
administration, Copilot Search and Copilot connectors, plus the self-service purchase FAQ, the pay-as-you-go overview
and the Teams page on Copilot in meetings, the last two kept for later waves. Five census queries went in before the
topic.

### What the reading found

The settings page is mostly a map of other places: web search is a Cloud Policy, meeting behavior a Teams policy, the
protections Purview's. Two of its facts run against intuition, and they are what the topic leads with: an unconfigured
web search policy means on, and Cowork's access is decided by a billing object.

```
2 commits · 1 topic, 5 cards · 6 anchors and 2 spans · AB-650 path 36 -> 37 steps · related links 5,494 -> 5,504
5 census queries, 0 of 5 -> 5 of 5 · census 815 of 838 · topics 1,629 -> 1,630 · dated claims 453 -> 461
45 gates green · smoke 167 · search 59 · axe 33/33 · mobile 16/16
```

## Session — the fifty-seventh wave, an agent listed twice on purpose

§61's queue. *Content ideas* §62 is the table.

### Read first

Microsoft Learn's Agent 365 overview, the agent registry page, Entra ID Governance's page on agent identities,
Conditional Access for agents, and the admin center's page on managing agents. Five census queries went in before the
topic.

### What the reading found

The registry lists one agent twice when its creator shares it and an admin publishes it, and says so; the rows are
separate records, so deleting one leaves the other. And the census found the reader's word again: Microsoft's page says
*ownerless*, the first draft said *loses its owner*, and `ownerless agents` was a zero until the card used the word.

```
2 commits · 1 topic, 4 cards · 4 anchors and 1 span · AB-650 path 37 -> 38 steps · related links 5,504 -> 5,516
5 census queries, 0 of 5 -> 5 of 5 after one wording fix · census 820 of 843 · topics 1,630 -> 1,631 · dated claims 461 -> 466
45 gates green · smoke 167 · search 59 · axe 33/33 · mobile 16/16
```

## Session — the fifty-eighth wave, four hours, two days and thirty

§62's queue. *Content ideas* §63 is the table.

### Read first

Microsoft Learn's pages on usage-based billing, managing and monitoring Copilot Credit spending, the Copilot usage
report, Copilot controls' measurement pillar, AI disclaimers, the new release options, and the E3, E5 and E7
comparison. Six census queries went in before the topic.

### What the reading found

Three clocks a reader needs: the cost dashboard refreshes every four hours, the usage report trails by about two days,
and Deferred release holds major updates about thirty days. And a default worth turning off: every spending policy
starts by including services Microsoft has not shipped yet.

```
2 commits · 1 topic, 3 cards, and an E7 row · 8 anchors and 1 span · AB-650 path 38 -> 39 steps · related links 5,516 -> 5,526
6 census queries, 0 of 6 -> 6 of 6 after one wording fix · census 826 of 849 · topics 1,631 -> 1,632 · dated claims 466 -> 475
45 gates green · smoke 167 · search 59 · axe 33/33 · mobile 16/16
```

## Session — the fifty-ninth wave, a stopgap and its replacement

§63's queue. *Content ideas* §64 is the table.

### Read first

Microsoft Learn's pages on SharePoint Advanced Management, Restricted Content Discovery, Restricted SharePoint Search,
DLP for Microsoft 365 Copilot and Cowork, and DSPM for AI. Five census queries went in before the cards.

### What the reading found

Microsoft's own advice for Copilot readiness has already turned over once: the allow list it offered first, Restricted
SharePoint Search, is being retired for a control that hides sites instead of listing the allowed ones. And the page for
DSPM for AI is itself labeled as the classic version of something newer.

```
2 commits · 2 cards in existing topics · 5 anchors and 1 span · console candidates 4 -> 3
5 census queries, 0 of 5 -> 5 of 5 · census 831 of 854 · dated claims 475 -> 481
45 gates green · smoke 167 · search 59 · axe 33/33 · the other suites not rerun: two cards in existing topics
```

## Session — the sixtieth wave, the whole site or the file

§64's queue. *Content ideas* §65 is the table.

### Read first

Microsoft Learn's overview of Microsoft 365 Backup, its page on Copilot in Teams meetings and events, and its page on
network connectivity in the admin center. Three census queries went in before the cards.

### What the reading found

The detail that changes what an admin does is in Backup's table: restoring a SharePoint site rolls the whole site back
and overwrites everything since, while restoring a mailbox brings back only what changed. So the card's advice is to
restore a site beside itself, at a new URL, when only part of it was damaged.

```
3 commits · 3 cards in existing topics · 3 anchors and 2 spans · AB-650 path described as whole
3 census queries, 0 of 3 -> 3 of 3 · census 834 of 857 · dated claims 481 -> 486
45 gates green · smoke 167 · search 59 · axe 33/33 · the other suites not rerun: three cards in existing topics
```

## Session — the sixty-first wave, a tag back on the infra domain

§65's queue was empty, so the wave took the live exam the roadmap's sources had named. *Content ideas* §66 is the table.

### Read first

Microsoft's AZ-802 study guide, every skill line, and the titles of every topic in `infra`, `endpoint`, `net`, `cloud`,
`sec` and `script` that could answer one. No census queries: a path is built from topics that exist.

### What building the path found

`infra` already teaches most of a Windows Server administrator's exam, from FSMO roles to DHCP failover. The gaps are
the features Microsoft added to Windows Server in the last few releases and its Azure reach, which is the same shape
MD-102's and MS-102's gaps had.

```
2 commits · 1 exam path, 39 steps · the infra header tag and the README moved to AZ-802 · 7 gaps queued
paths 120 -> 121, steps 2,373 -> 2,412
45 gates green · smoke 167 · search 59 · the other suites not rerun: a path and a tag
```

## Session — the sixty-second wave, a comment that moved

§66's queue, its first gap. *Content ideas* §67 is the table.

### Read first

Microsoft Learn's security groups reference and RODC installation page, the Denied group's health-check page, and the
Azure Architecture Center's page on AD DS in an Azure virtual network. Four census queries went in before the topic.

### What the reading found

An RODC is a design for theft: what matters is what it caches, and Microsoft ships it caching nothing. And a DC in
Azure is a branch office with better locks, which needs a site and a site link like any other.

```
2 commits · 1 topic, 2 cards · 3 anchors · AZ-802 path 39 -> 40 steps · related links 5,526 -> 5,534
4 census queries, 0 of 4 -> 4 of 4 after one wording fix · census 838 of 861 · topics 1,632 -> 1,633 · dated claims 486 -> 489
stamp_freshness.py --touched fixed for appended topics · 45 gates green · smoke 167 · search 59 · axe 33/33
```

## Session — the sixty-third wave, placeholders

§67's queue, its first item. *Content ideas* §68 is the table.

### Read first

Microsoft Learn's pages on Azure Files, Azure File Sync and cloud tiering, fetched while the sixty-second wave's suites
ran. Three census queries went in before the card.

```
1 commit for the card, 1 for the plan · 1 card in an existing topic · 3 anchors
3 census queries, 0 of 3 -> 3 of 3 · census 841 of 864 · dated claims 489 -> 492
45 gates green · smoke 167 · search 59 · the other suites not rerun: one card in an existing topic
```

## Session — the sixty-fourth wave, a snapshot of a DC

§68's queue, its first item. *Content ideas* §69 is the table.

### Read first

Microsoft Learn's pages on PowerShell Direct, nested virtualization, checkpoints and Hyper-V Replica. Four census
queries went in before the card.

### What the reading found

Microsoft's checkpoint page names Active Directory as the system a standard checkpoint can damage, which ties this card
to the site's restore topic: the one VM state a hypervisor's undo button should not be trusted with is a domain
controller's.

```
2 commits · 1 card in an existing topic · 4 anchors
4 census queries, 0 of 4 -> 4 of 4 · census 845 of 868 · dated claims 492 -> 496
45 gates green · smoke 167 · search 59 · the other suites not rerun: one card in an existing topic
```

## Session — the sixty-fifth wave, distance decides

§69's queue, its first item. *Content ideas* §70 is the table.

### Read first

Microsoft Learn's pages on Storage Spaces Direct, Storage Replica and SMB over QUIC. Three census queries went in before
the cards.

```
2 commits · 2 cards in existing topics · 3 anchors
3 census queries, 0 of 3 -> 3 of 3 · census 848 of 871 · dated claims 496 -> 499
45 gates green · smoke 167 · search 59 · the other suites not rerun: two cards in existing topics
```

## Session — the sixty-sixth wave, the acronym the reader typed

§70's queue, its first item. *Content ideas* §71 is the table.

### Read first

Microsoft Learn's pages on Credential Guard, the Protected Users group, the Windows Server 2025 security baseline,
Defender for Servers and exploit protection. Four census queries went in before the topic.

### What the census found

The topic as first written answered three of the four. The fourth, `credential guard lsa isolation`, found nothing: the
prose said *Local Security Authority* and *isolated*, and the reader typed the acronym and the noun. Search matches a
word of five letters or more as a substring, so *isolated* never contains *isolation*, and the fact anchor that did say
LSA is not searched. The sentence says LSA now, and the build expands it on first use.

```
2 commits · 1 topic, 3 cards · 5 anchors · AZ-802 path 40 -> 41 steps · related links 5,534 -> 5,544
4 census queries, 0 of 4 -> 3 of 4 -> 4 of 4 after one wording fix · census 852 of 875 · topics 1,633 -> 1,634
dated claims 499 -> 504 · the Related links row's mainland, stale since the twenty-eighth wave, measured again: 1,558
45 gates green · smoke 167 · search 59 · axe 33/33 · the other suites not rerun: one topic in an existing domain
```

## Session — the sixty-seventh wave, a policy, not a pipe

§71's queue, its first two items. *Content ideas* §72 is the table.

### Read first

Microsoft Learn's pages on SmartScreen and its settings; on `logman` and `logman create counter`; on Windows Admin
Center's server tools; on System Insights and managing its capabilities; on data collection rules; and on monitoring
Azure VMs, which the old VM insights address now redirects to. Its page on Entra Password Protection for AD DS was read
too, and showed that item was not a gap. Six census queries went in before the topic and the card.

### What the census found

All six answered as first written. The *Dated claims* row needed a fix instead:
the sixty-sixth wave had changed its numbers without the sentence each wave writes there, and it has one now.

```
2 commits · 1 topic with 3 cards, and 1 card in an existing topic · 9 anchors, 1 span · AZ-802 path 41 -> 42 steps
6 census queries, 0 of 6 -> 6 of 6 · census 858 of 881 · topics 1,634 -> 1,635 · related links 5,544 -> 5,554
dated claims 504 -> 514 · console candidates still 3, with Windows Admin Center's first mention dated
45 gates green · smoke 167 · search 59 · axe 33/33 · the other suites not rerun: one topic and a card in one domain
```

## Session — the sixty-eighth wave, billed from the hour it is deployed

§72's queue, its first item. *Content ideas* §73 is the table.

### Read first

Microsoft Learn's pages on just-in-time VM access, Azure Bastion and Bastion's configuration settings, and, read ahead
for the next wave, its pages on enhanced session mode, Discrete Device Assignment, GPU partitioning and the host network
page its Windows Server docs link for Switch Embedded Teaming. Three census queries went in before the card.

### What the census found

All three answered as first written. The console census found the card's one slip: a fact anchor naming the Azure
portal, which made the topic a fourth candidate until the anchor said the portal's web client.

```
2 commits · 1 card in an existing topic · 3 anchors
3 census queries, 0 of 3 -> 3 of 3 · census 861 of 884 · dated claims 514 -> 517 · console candidates 4 -> 3
45 gates green · smoke 167 · search 59 · the other suites not rerun: one card in an existing topic
```

## Session — the sixty-ninth wave, PCIe is not PCI

§73's queue, its first item. *Content ideas* §74 is the table.

### Read first

Microsoft Learn's pages on VMConnect's local resources, Discrete Device Assignment and GPU partitioning; its Windows
Server page on creating a virtual switch, and the Azure Local host network page that page links for Switch Embedded
Teaming, after the old SET address redirected there and the NIC Teaming overview returned 404. Read ahead for the next
wave: SMB Direct, Storage QoS, and the firewall command-line page. Four census queries went in before the card.

### What the gates found

All four census queries answered as first written. The content lint did not pass: its pattern for a rendered acronym
allows a plural *e* or *s* after it, so *PCIe* read as *PCI*, whose default expansion is Payment Card Industry, rendered
in a domain that had never decided what PCI means. `hw` and `linux` had met the same thing and chose not to annotate PCI;
`infra` now does the same.

```
2 commits · 1 card in an existing topic · 4 anchors · 1 acronym decision
4 census queries, 0 of 4 -> 4 of 4 · census 865 of 888 · dated claims 517 -> 521
45 gates green after the PCI decision · smoke 167 · search 59 · the other suites not rerun: one card in an existing topic
```

## Session — the seventieth wave, counted in normalized IOPS

§74's queue, its three items. *Content ideas* §75 is the table.

### Read first

Microsoft Learn's pages on SMB Direct, Storage Quality of Service and managing Windows Firewall from the command line,
read in the sixty-ninth wave, and then AZ-802's study guide again, all 115 skills, against the site, which found the
five gaps §75 queues. Read ahead for the next waves: the PowerShell team's page on the second hop, and Microsoft's pages
on integration services and on Hyper-V. Four census queries went in before the cards.

### What the census found

One of the four was answered before the cards existed: `smb direct rdma` found the SMB topic, whose version table
already named RDMA among SMB 3's features. It stays in the census, since a reader typing it is now answered by a card
rather than a table cell. The other three opened at nothing or the wrong card and closed answered.

```
2 commits · 3 cards in three existing topics · 3 anchors · AZ-802 path 42 -> 43 steps
4 census queries, 1 of 4 -> 4 of 4 · census 869 of 892 · dated claims 521 -> 524
45 gates green · smoke 167 · search 59 · the other suites not rerun: cards in existing topics
```

## Session — the seventy-first wave, a phrase that moved a query

§75's queue, its first item. *Content ideas* §76 is the table.

### Read first

The PowerShell team's page on the second hop, read in the seventieth wave, and, for the next wave, Microsoft's
`New-VHD` and `Set-VMMemory` references, its virtual switch overview and its page on generation 1 and 2 VMs. Three
census queries went in before the card.

### What the census found

The card's three queries answered as first written, and `--check-plan`, which measures every batch, found the one it
broke: `protected users group`, which the sixty-sixth wave's hardening topic had answered, now found the second-hop card,
whose verdict said *the Protected Users group* where the hardening topic said *Protected Users … as a group*. The fix
went to the topic that owns the subject, which now says the exact phrase.

```
2 commits · 1 card in an existing topic · 1 anchor · 1 phrase restored in another topic
3 census queries, 0 of 3 -> 3 of 3 · 1 earlier query lost and restored · census 872 of 895 · dated claims 524 -> 525
45 gates green · smoke 167 · search 59 · the other suites not rerun: one card in an existing topic
```

## Session — the seventy-second wave, managed from the host

§76's queue, its first item. *Content ideas* §77 is the table.

### Read first

Microsoft Learn's pages on creating a virtual switch and on Hyper-V's overview, read in earlier waves, and its `New-VHD`,
`Set-VMMemory` and integration services pages; for the next wave, its pages on delegating administration through OUs
and on DNS policies. Four census queries went in before the card.

### What the census found

All four answered as first written. Reading the AD DS boundaries topic for the next wave's delegation card turned up
something the gates had missed: *organisational*, in that card and about two dozen other places. The spelling gate's
`-ise` rule stops at `-isation` and `-isations`, so `-isational` and `-isationally` pass it. That is queued as a gate fix
with its corrections, not folded into a content card.

```
2 commits · 1 card in an existing topic · 5 anchors
4 census queries, 0 of 4 -> 4 of 4 · census 876 of 899 · dated claims 525 -> 530
45 gates green · smoke 167 · search 59 · the other suites not rerun: one card in an existing topic
```

## Session — the seventy-third wave, first match wins

§77's queue, its first two items. *Content ideas* §78 is the table.

### Read first

Microsoft Learn's pages on delegating administration through OUs and on DNS policies, read in the seventy-second wave,
and Learn's search for a page on SSH Direct, which found none. Four census queries went in before the cards.

### What the census found

One of the four was answered before the cards: `ad delegation service administrators` found the AD DS boundaries topic,
whose design card already said delegation is one of the two reasons an OU exists. The other three opened at nothing or
another card and closed answered.

```
2 commits · 2 cards in two existing topics · 2 anchors
4 census queries, 1 of 4 -> 4 of 4 · census 880 of 903 · dated claims 530 -> 532
45 gates green · smoke 167 · search 59 · the other suites not rerun: cards in existing topics
```

## Session — the seventy-fourth wave, organizational

§78's queue. *Content ideas* §79 is the table.

### Read first

`check_spelling.py` itself: its rules, its keep-list and its dictionary, against a scan of every data file for words the
rules' suffix lists could not reach. Then Learn's search, three ways, for a page on SSH Direct, and MD-102's study guide,
updated 16 August 2026, for the next wave.

### What the gates found

The scan found the `-ise` gap and no other: `-yse` and `-our` forms beyond their suffix lists occur nowhere in the
corpus. The fix touched a topic's title, and the measured rows saw the moved slug on the next build, before any test
did.

```
1 commit · ISE_RE +6 suffixes · self-test 163 -> 171 fixtures · dictionary 83 -> 84 entries
44 spellings corrected: 39 by --fix in 16 files, 1 sentence rewritten, 4 in diagrams by hand · 37 topics stamped
1 slug moved and aliased · aliases 164 -> 165
45 gates green · smoke 167 · search 59 · axe 33/33
```

## Session — the seventy-fifth wave, one user on one screen

§79's queue. *Content ideas* §80 is the table.

### Read first

MD-102's study guide as Microsoft published it on 16 August 2026, all seventy-six skills against the site, then
Microsoft Learn's pages on custom compliance, BitLocker with Intune, and the troubleshooting dashboard. For the next
wave: enrollment time grouping and Samsung Knox Mobile Enrollment. A page on Quiet Time policies was not found by Learn's
search or at four likely addresses, and the device query's old address returns 404. Three census queries went in before
the cards.

### What the census found

All three answered as first written. Two of the cards name console paths, and both went into dated spans as they were
written, so the console census stayed at three without a second pass.

```
2 commits · 3 cards in three existing topics · 3 anchors, 2 spans
3 census queries, 0 of 3 -> 3 of 3 · census 883 of 906 · dated claims 532 -> 537
45 gates green · smoke 167 · search 59 · the other suites not rerun: cards in existing topics
```

## Session — the seventy-sixth wave, the JSON the portal calls optional

§80's queue, its first two items. *Content ideas* §81 is the table.

### Read first

Microsoft Learn's pages on enrollment time grouping and on Samsung Knox Mobile Enrollment, read in the seventy-fifth
wave, and Learn's search for Quiet Time, which returned Intune pages under new addresses and none about Quiet Time.
Three census queries went in before the cards.

### What the census found

All three opened at nothing and closed answered, as first written.

```
2 commits · 2 cards in two existing topics · 2 anchors
3 census queries, 0 of 3 -> 3 of 3 · census 886 of 909 · dated claims 537 -> 539
45 gates green · smoke 167 · search 59 · the other suites not rerun: cards in existing topics
```

## Session — the seventy-seventh wave, a room cannot do MFA

§81's queue, its first item. *Content ideas* §82 is the table.

### Read first

Microsoft Learn's pages on Teams Rooms' supported Conditional Access and compliance policies, on Windows Holographic
devices in Intune, on Zebra's Mobility Extensions and on Zebra LifeGuard Over-the-Air. Three census queries went in
before the card.

### What the census found

Two answered as first written. The third, `zebra lifeguard ota firmware`, found nothing: the prose said *LifeGuard
Over-the-Air*, the fact anchor said OTA, and anchors are not searched. The card says *LifeGuard OTA for short* now. A
reread before the build caught a claim the page did not make, about which HoloLens runs which edition, and the card
now says only what the page says.

```
2 commits · 1 card in an existing topic · 4 anchors, 1 span
3 census queries, 0 of 3 -> 2 of 3 -> 3 of 3 after one wording fix · census 889 of 912 · dated claims 539 -> 544
45 gates green · smoke 167 · search 59 · the other suites not rerun: one card in an existing topic
```

## Session — the seventy-eighth wave, enroll

§82's queue, its first item. *Content ideas* §83 is the table.

### Read first

`check_spelling.py`'s dictionary, against a scan of the corpus's prose for single-`l` and doubled-`l` British forms it
did not list, with each hit read in context: a proper noun, a word American English shares, or a real British form.

### What the gates found

`gen_cheatsheet.py --check`, the gate that keeps a generated file in step with its source, failed on the first run,
and the commit had already been made. Nothing was pushed until the regenerated file was in it and all 45 gates passed.

```
1 commit, amended once before it was pushed · IRREGULAR 84 -> 104 entries · self-test fixtures +8
27 spellings corrected in 11 files · 1 in a generator · 1 generated file regenerated · 16 topics stamped
45 gates green on the second run · smoke 167 · search 59 · axe 33/33
```

## Session — the seventy-ninth wave, AZ-500's successor gets its path

§83's queue, its first item. *Content ideas* §84 is the table.

### Read first

Microsoft's SC-500 study guide, last updated 13 May 2026: four skill areas and their twelve subheadings, every skill
checked against the site by its product's name. Thirty-nine skills map to topics that exist; the products the site never
names make §84's queue.

### The file

This record takes plan.md past 8,000 lines, which is the fifth risk's reopen condition, and option 1 ran for the fourth
time: the oldest 45 session records, from *a measurement of verdict quality that did not work* to the thirty-third
wave, moved to the end of `plan-archive.md` in their order, taking plan.md from 8,044 lines to 5,486. Every line of the
records moved; the two files' total differs by one blank line between records. The counts in the *Session records* row
and the README moved with them.

```
2 commits · 1 path, 39 steps · paths 121 -> 122, steps 2,416 -> 2,455 · 0 topics, 0 cards
45 gates green · smoke 167 · search 59 · the other suites not rerun: a path, not a topic
the fifth risk fired a fourth time, and the archive took the oldest session records
```

## Session — the eightieth wave, a portal the anchor named first

§84's queue, its first item. *Content ideas* §85 is the table.

### Read first

Microsoft Learn's pages on Defender for Cloud, its CSPM plans, regulatory compliance, and Defender for Storage, Key
Vault and AI threat protection; and, for the next wave, Microsoft Sentinel's pages on roles, the content hub, data
connectors, syslog and CEF through the Azure Monitor agent, automation rules, and tables, tiers and retention. Five
census queries went in before the topic.

### What the gates found

All five census queries answered as first written. The console census found a fourth candidate, the new topic, from a
fact anchor naming the Defender portal; the prose now states the move in a dated span. Reading ahead found the next
wave's correction: *Azure Security*'s Sentinel card describes tiers Microsoft's current page does not.

```
2 commits · 1 topic, 3 cards · 6 anchors, 1 span · SC-500 path 39 -> 40 steps · related links 5,554 -> 5,564
5 census queries, 0 of 5 -> 5 of 5 · census 894 of 917 · topics 1,635 -> 1,636 · dated claims 544 -> 551
45 gates green · smoke 167 · search 59 · axe 33/33
```

## Session — the eighty-first wave, an archive that is now a lake

§85's queue, Microsoft Sentinel's machinery. *Content ideas* §86 is the table.

### Read first

The Sentinel pages the last wave read ahead: roles, the content hub, data connectors, syslog and CEF through the Azure
Monitor agent, automation rules, and tables, tiers and retention, with each page's date taken from its own metadata.
Five census queries went in before the topic.

### What the gates found

All five census queries answered as first written, and the topic took no acronym or console decision: the move into the
Defender portal sits in a dated span from the first draft, which is the lesson the last wave left. The correction in
*Azure Security* went in with an anchor of its own, so the next re-check reads the tier page rather than the card's
memory of it.

```
2 commits · 1 topic, 4 cards · 7 anchors, 1 span · 1 card corrected · SC-500 path 40 -> 41 steps · related links 5,564 -> 5,574
5 census queries, 0 of 5 -> 5 of 5 · census 899 of 922 · topics 1,636 -> 1,637 · dated claims 551 -> 559
45 gates green · smoke 167 · search 59 · axe 33/33
```

## Session — the eighty-second wave, the path the traffic takes

§86's queue, SC-500's AI workloads in Azure. *Content ideas* §87 is the table.

### Read first

Microsoft Learn's pages on the AI gateway in API Management, configuring a gateway for Foundry, Foundry's guardrails,
Copilot Studio's external threat detection, and Defender for Cloud's Data and AI security dashboard, each page's date
from its own metadata. Five census queries went in before the topic.

### What the gates found

All five census queries answered as first written. The acronym dictionary reads TPM as the Trusted Platform Module, so
the prose says tokens per minute in words rather than borrowing the page's abbreviation. The dated spans went in with the
first draft, so the console census stayed at three. Reading the SC-500 path for the new step found its description two
waves out of date.

```
2 commits · 1 topic, 5 cards · 5 anchors, 3 spans · SC-500 path 41 -> 42 steps · related links 5,574 -> 5,586
5 census queries, 0 of 5 -> 5 of 5 · census 904 of 927 · topics 1,637 -> 1,638 · dated claims 559 -> 567
45 gates green · smoke 167 · search 59 · axe 33/33
```

## Session — the eighty-third wave, a query that answered before its card

§87's queue, SC-500's network services. *Content ideas* §88 is the table.

### Read first

Microsoft Learn's pages on Virtual Network Manager and its security admin rules, the secured virtual hub, Virtual WAN's
routing intent, Entra Private Access and Quick Access, read while the last wave's gates ran. Five census queries went in
before the cards, one of them replaced after the first measurement because it already matched.

### What the gates found

All five census queries answered once the cards were in. The cards needed no dated span: neither names a console, and the
console census stayed at three. Both topics' review stamps moved to November, *ZTNA*'s from August.

```
2 commits · 2 cards in 2 existing topics · 6 anchors · 0 topics · related links unchanged
5 census queries, 0 of 5 -> 5 of 5 · census 909 of 932 · dated claims 567 -> 573
45 gates green · smoke 167 · search 59 · the axe suite not rerun: cards, not a topic
```

## Session — the eighty-fourth wave, the templates are where it hides

§88's queue, SC-500's VM security. *Content ideas* §89 is the table.

### Read first

Microsoft Learn's pages on trusted launch and Azure Machine Configuration, read while the last wave's gates ran. Five
census queries went in before the cards, one replaced after the first measurement because it already matched.

### What the gates found

All five census queries answered once the cards were in. *boot integrity monitoring* lists *Hardware Root of Trust*
first, which is a fair answer too, and the two topics now link. The console census stayed at three.

```
2 commits · 2 cards in 2 existing topics · 2 anchors, 1 span · related links 5,586 -> 5,588
5 census queries, 0 of 5 -> 5 of 5 · census 914 of 937 · dated claims 573 -> 576
45 gates green · smoke 167 · search 59 · the axe suite not rerun: cards, not a topic
```

## Session — the eighty-fifth wave, 0 unexplained, which was 1

§89's queue, SC-500's data controls. *Content ideas* §90 is the table.

### Read first

Microsoft Learn's pages on SQL Database auditing, server- and database-level policies, Managed Instance auditing,
stored access policies and shared access signatures, read while the last wave's gates ran; the SAS overview was read to
source the card's claim about revocation before the claim was kept. Five census queries went in before the cards.

### What the gates found

All five census queries answered. The run after the cards printed one unexplained query, *the database is slow*, and
following it found the defect §90 records: the query had been wide, and unexplained, since the eighty-second wave, and
three records had said otherwise. A worktree at the eighty-first wave's commit measured 60, the line it crossed. The
auditing card's own word *slow* briefly made the query a miss as well; that cell now says *expensive*, which is also
what Microsoft's page says.

```
2 commits · 2 cards in 2 existing topics · 5 anchors · 1 census note · --check-plan reads the headline, 27 fixtures
5 census queries, 0 of 5 -> 5 of 5 · census 920 of 942, 0 unexplained, after 1 for three waves · dated claims 576 -> 581
45 gates green · smoke 167 · search 59 · the axe suite not rerun: cards, not a topic
```

## Session — the eighty-sixth wave, the device query page was at a new address

§90's queue, MD-102's device query. *Content ideas* §91 is the table.

### Read first

Learn's search API, for the two pages the seventy-fifth wave could not find: device query turned up under Intune's new
documentation tree, and Quiet Time did not. Then the device query page itself. Three census queries went in before the
card.

### What the gates found

Two census queries answered with the first draft. The third, *check a registry value without remote control*, found
nothing, because the verdict paraphrased Microsoft's list of checks in words a reader would not type; rewritten in the
page's own terms, a remote control session and the checks a query can answer without one, it answered. The census
headline check added last wave passed on its first real run. The first gate run stopped at the lint, on a `>`
in the anchor's menu path, *Devices > Windows*, which is the shape that check exists for: the tools that strip markup
with `<[^>]+>` would read the rest of the comment as card text. The anchor says *Devices, Windows* now.

```
2 commits · 1 card in 1 existing topic · 1 anchor, 1 span
3 census queries, 0 of 3 -> 3 of 3 · census 923 of 945, 0 unexplained · dated claims 581 -> 583
45 gates green, the second run · smoke 167 · search 59 · the axe suite not rerun: a card, not a topic
```

## Session — the eighty-seventh wave, Azure's administrator gets a path

§91's queue, its first item. *Content ideas* §92 is the table.

### Read first

Microsoft's study guides for AZ-104, SC-200 and SC-300, to check each is current before choosing: all three are, with
skills measured as of April and October 2026. AZ-104 came first because the site's Azure topics were already written for
its reader. Its skills were then checked against every data file by name, forty terms in all; the ones the site never
names are §92's queue, and blob lifecycle rules, which looked like a gap, turned out to be in *Azure Compute &amp;
Storage* already.

### What the gates found

`check_paths.py` found every step's topic and no topic off a path. The path added no topic, so the census and the share
image did not move.

```
2 commits · 1 path, 21 steps · paths 122 -> 123, steps 2,458 -> 2,479 · 0 topics, 0 cards
45 gates green · smoke 167 · search 59 · the axe suite not rerun: a path, not a topic
```

## Session — the eighty-eighth wave, a lock that cannot be corrected

§92's queue, AZ-104's backup and recovery. *Content ideas* §93 is the table.

### Read first

Microsoft Learn's Azure Backup overview, both vault overviews, its security and cyber recovery overview, and *About Site
Recovery*, read while the AZ-104 path's gates ran. Five census queries went in before the topic.

### What the gates found

All five census queries answered as first written. The topic names no console, so it needed no dated span, and
the console census stayed at three. Its five anchors went in with the first draft; one sentence was corrected on
reread, where the draft said customer-managed keys were for Recovery Services workloads only, and Microsoft's
Backup vault page offers them too.

```
2 commits · 1 topic, 3 cards · 5 anchors · AZ-104 path 21 -> 22 steps · related links 5,588 -> 5,596
5 census queries, 0 of 5 -> 5 of 5 · census 928 of 950, 0 unexplained · topics 1,638 -> 1,639 · dated claims 583 -> 588
45 gates green · smoke 167 · search 59 · axe 33/33
```

## Session — the eighty-ninth wave, three switches for three deletions

§93's queue, AZ-104's blob and file data protection. *Content ideas* §94 is the table.

### Read first

Microsoft Learn's data protection overview, its pages on blob versioning, blob and container soft delete and object
replication, and Azure Files' pages on share snapshots and share soft delete, read while two earlier waves' gates ran.
Five census queries went in before the cards.

### What the gates found

One first-draft query, *azure file share snapshot*, already matched *File Services* through its Azure File Sync card,
and was replaced before the cards with *azure files previous version of a file*, which found nothing; the card now
says what Microsoft's snapshot page says, that a share snapshot is how a previous version of a file comes back. All
five answered once the cards were in, and the AZ-104 path's description lost two of its gaps.

```
2 commits · 2 cards in 2 existing topics · 4 anchors
5 census queries, 0 of 5 -> 5 of 5 · census 933 of 955, 0 unexplained · dated claims 588 -> 592
45 gates green · smoke 167 · search 59 · the axe suite not rerun: cards, not a topic
```

## Session — the ninetieth wave, a page dated 2019 describing 2026

§94's queue, AZ-104's storage access and tools. *Content ideas* §95 is the table.

### Read first

Microsoft Learn's pages on the storage firewall's network rules, AzCopy, Storage Explorer and Azure Files' identity-based
access, read while the eighty-eighth wave's gates ran. Five census queries went in before the cards.

### What the gates found

All five census queries answered as first written. On reread, the first draft of the AzCopy card said both tools could
work from an account key; AzCopy's page lists Microsoft Entra ID and SAS tokens and no key, so the card says that. The
path's description lost two more of AZ-104's gaps.

```
2 commits · 3 cards in 2 existing topics · 4 anchors
5 census queries, 0 of 5 -> 5 of 5 · census 938 of 960, 0 unexplained · dated claims 592 -> 596
45 gates green · smoke 167 · search 59 · the axe suite not rerun: cards, not a topic
```

## Session — the ninety-first wave, silence that ends by itself

§95's queue, AZ-104's Azure Monitor alerting. *Content ideas* §96 is the table.

### Read first

Microsoft Learn's alerts overview and its pages on action groups, alert processing rules and Connection monitor, read
while earlier waves' gates ran; the overview was fetched to source the card's list of alert rule types before it was
kept. Five census queries went in before the card.

### What the gates found

Two census queries needed the card to use Microsoft's own words. *suppress alerts during maintenance* found nothing
until the card said what Microsoft's heading says, suppressing notifications during planned maintenance, and *log
search alert* found other cards until the card named the alert types as Microsoft does, metric, log search and
activity log alerts, where the draft had said a log query. The draft also wrote SMS for text messages, which the
acronym dictionary expands as Systems Management Server, ConfigMgr's old name; it says text message now. The SMS
expansions already on the site were checked, and all three mean what they say.

```
2 commits · 1 card in 1 existing topic · 4 anchors
5 census queries, 0 of 5 -> 5 of 5 · census 943 of 965, 0 unexplained · dated claims 596 -> 600
45 gates green · smoke 167 · search 59 · the axe suite not rerun: a card, not a topic
```

## Session — the ninety-second wave, a budget that only warns

§96's queue, AZ-104's last two gaps. *Content ideas* §97 is the table.

### Read first

Microsoft Learn's Azure DNS overview, its Private DNS page, the budgets tutorial and the Advisor introduction, read while
earlier waves' gates ran. Five census queries went in before the cards.

### What the gates found

One first-draft query, *azure private dns zone*, already matched *Azure Networking* through its private endpoint
content, and was replaced before the cards with *dns private resolver*, which found other cards. All five answered
once the cards were in. Two sentences went before the first build because the pages read did not say them: that a
registrar must delegate a public domain to Azure's name servers, and that Advisor is free. Both may be true; neither
was on the page.

```
2 commits · 2 cards in 2 existing topics · 4 anchors
5 census queries, 0 of 5 -> 5 of 5 · census 948 of 970, 0 unexplained · dated claims 600 -> 604
45 gates green · smoke 167 · search 59 · the axe suite not rerun: cards, not a topic
```

## Session — the ninety-third wave, identity gets its own exam path

§97's queue, its first item. *Content ideas* §98 is the table.

### Read first

Microsoft's SC-300 study guide, already fetched to check it was current, and every skill in it checked against the site's
data files by name; the terms the site never names are §98's queue. Pass-through authentication, which looked like a gap,
is in *Entra Connect &amp; Hybrid Identity* as *pass-through auth*.

### What the gates found

`check_paths.py` found every step's topic. The path added no topic, so the census and the share image did not move.

```
2 commits · 1 path, 20 steps · paths 123 -> 124, steps 2,480 -> 2,500 · 0 topics, 0 cards
45 gates green · smoke 167 · search 59 · the axe suite not rerun: a path, not a topic
```

## Session — the ninety-fourth wave, approval on the group that leads to a role

§98's queue, its first two rows. *Content ideas* §99 is the table.

### Read first

Microsoft Learn's pages on administrative units, PIM for Groups, protected actions and cross-tenant synchronization,
read while the SC-300 path's gates ran. Five census queries, measured against the site as it stood before the cards.

### What the gates found

The first draft of the roles card taught administrative units, and the census had a query for them already, from the
sixteenth wave, answered by a topic of their own; §98 had listed them as a gap. The card was cut back to PIM for Groups
and protected actions with a pointer to that topic, the query replaced, and the topic added to the SC-300 path. All five
queries answered once the cards were in, the last only after the cross-tenant card said in plain words that it keeps
users in sync between tenants, and that one finds its card among 13. One sentence of that card's verdict, that
Microsoft allows it between organizations with compliance responsibilities attached, was on the page and not in the
anchor, and went into the anchor before the commit.

```
2 commits · 2 cards in 2 existing topics · 3 anchors · SC-300 path 20 -> 21 steps
5 census queries, 0 of 5 -> 5 of 5 · census 953 of 975, 0 unexplained · dated claims 604 -> 607
45 gates green · smoke 167 · search 59 · the axe suite not rerun: cards, not a topic
```

## Session — the ninety-fifth wave, the campaign that only helps if the old method goes

§99's queue, its first two items. *Content ideas* §100 is the table.

### Read first

Microsoft Learn's overview of certificate-based authentication, its page on registration campaigns and its page on
publishing apps with Application Proxy, all fetched in the ninety-fourth wave and read again against the drafts. Five
census queries went in before the cards.

### What the gates found

The census opened at 0 of 5 and closed at 5 of 5 with no query replaced and no word changed for it. The reading did the
correcting this time: four draft sentences changed, listed in §100. The annotator added four expansions to the new
cards, AD FS in a card title, PKI, URL, and MFA in *ZTNA*, which had not named it before.

```
2 commits · 2 cards in 2 existing topics · 3 anchors
5 census queries, 0 of 5 -> 5 of 5 · census 958 of 980, 0 unexplained · dated claims 607 -> 610
45 gates green · smoke 167 · search 59 · the axe suite not rerun: cards, not a topic
```

## Session — the ninety-sixth wave, a Global Administrator who cannot read a field

§100's queue, its first two items. *Content ideas* §101 is the table.

### Read first

Microsoft Learn's page on custom security attributes, fetched in the ninety-fourth wave, and its pages on terms of use
and connected organizations, fetched for this one; and SC-300's study guide again, for where custom security attributes
sit. Five census queries went in before the cards.

### What the gates found

The census opened at 0 of 5, every query finding another card, and closed at 5 of 5 with none replaced. The custom
security attributes draft gained a table from the page's own comparison with directory extensions. The annotator's
JSON expansion and the console count's fourth candidate are in §101.

```
2 commits · 2 cards in 2 existing topics · 3 anchors · SC-300 path 21 -> 22 steps
5 census queries, 0 of 5 -> 5 of 5 · census 963 of 985, 0 unexplained · dated claims 610 -> 613
45 gates green · smoke 167 · search 59 · the axe suite not rerun: cards, not a topic
```

## Session — the ninety-seventh wave, a status that earns the points without the work

§101's queue, SC-300's last gap. *Content ideas* §102 is the table.

### Read first

Microsoft Learn's pages on the Identity Secure Score and the provisioning logs, and SC-300's study guide again, for
where it puts the Identity Secure Score. Five census queries went in before the cards.

### What the gates found

The census opened at 0 of 5, two zeros and three that found other cards. Four answered once the cards were in; the
fifth, *user was not provisioned*, needed the card to use the reader's word, and it now says a user was not
provisioned where they should exist instead of that an account does not.

```
2 commits · 2 cards in 2 existing topics · 2 anchors · SC-300 path 22 -> 23 steps, no gap left
5 census queries, 0 of 5 -> 5 of 5 · census 968 of 990, 0 unexplained · dated claims 613 -> 615
45 gates green · smoke 167 · search 59 · the axe suite not rerun: cards, not a topic
```

## Session — the ninety-eighth wave, the analyst's exam gets a path

§102's queue. *Content ideas* §103 is the table and the gap list.

### Read first

Microsoft's SC-200 study guide, fetched again, skills measured as of 21 October 2026, and its terms counted across the
data files before any gap was listed. Fourteen are named nowhere on the site, from attack disruption and live response
to the Sentinel graph and Graph activity logs; a few more are named only away from where SC-200 asks about them, such
as Security Copilot, which the site describes only in Intune, and notebooks and anomalies, which no Sentinel card
mentions. The rest were found in the topics that became the path's steps.

### What the gates found

`check_paths.py` found every step's topic. The path added no topic, so the census and the share image did not move.

```
2 commits · 1 path, 23 steps · paths 124 -> 125, steps 2,503 -> 2,526 · 0 topics, 0 cards
45 gates green · smoke 167 · search 59 · the axe suite not rerun: a path, not a topic
```

## Session — the ninety-ninth wave, the exclusions to set before the first disruption

§103's queue, its first two rows. *Content ideas* §104 is the table.

### Read first

Microsoft Learn's pages on automatic attack disruption, case management and Security Copilot in Defender, fetched while
the SC-200 path's gates ran. Six census queries went in before the cards.

### What the gates found

The census opened at 0 of 6, three zeros and three that found other cards. Four answered once the cards were in; the
other two needed the words the reader and Microsoft share. The cases card said *cases* and never *case management*,
the feature's own name, and the Copilot card said *plain language* where Microsoft's page says *natural language*.

The reading for the next wave found the change §104 records, and it went into this wave's commit: a fourth anchor and
a dated paragraph in the automated investigation card. The first gate run was stopped once the change was made, and a
second, started by mistake as a background job in the shell, was killed before it finished; the gates that count ran
from a clean build.

```
2 commits · 3 cards in 1 existing topic, 1 card corrected · 4 anchors
6 census queries, 0 of 6 -> 6 of 6 · census 974 of 996, 0 unexplained · dated claims 615 -> 619
45 gates green · smoke 167 · search 59 · the axe suite not rerun: cards, not a topic
```

## Session — the hundredth wave, check the proxy before isolating

§104's queue, its first item. *Content ideas* §105 is the table.

### Read first

Microsoft Learn's pages on response actions on a device, live response, device groups and automation levels, fetched
while the ninety-ninth wave's gates ran; the automation levels page is where the change §104 records was found. Five
census queries went in before the cards.

### What the gates found

One first-draft query, *live response*, was replaced before the cards: its two words already met in 60 topics, the
census's line for wide, and the card would have made it 61. *Live response session*, the button's own name, met in 19.
The census opened at 0 of 5, one zero and four that found other cards, and closed at 5 of 5. The census passed a
thousand queries with this batch.

```
2 commits · 2 cards in 1 existing topic · 4 anchors
5 census queries, 0 of 5 -> 5 of 5 · census 979 of 1,001, 0 unexplained · dated claims 619 -> 623
45 gates green · smoke 167 · search 59 · the axe suite not rerun: cards, not a topic
```

## Session — the hundred-and-first wave, the events written before the device joined

§105's queue, its first item. *Content ideas* §106 is the table.

### Read first

Microsoft Learn's page on Windows Event Forwarding for intrusion detection, and Sentinel's data connector reference for
the two Windows connectors and the tables they fill, fetched while the hundredth wave's gates ran. Four census queries
went in before the card.

### What the gates found

Two first-draft queries, *windows event forwarding* and *windows event collector*, already reached the topic, whose
existing card ends by telling the reader to forward to a collector; both were replaced with *wef subscription* and
*read existing events*, which found nothing and other cards. The census opened at 0 of 4 and closed at 4 of 4. The
card spells out AMA as the Azure Monitor Agent, because the acronym dictionary does not know it.

```
2 commits · 1 card in 1 existing topic · 2 anchors
4 census queries, 0 of 4 -> 4 of 4 · census 983 of 1,005, 0 unexplained · dated claims 623 -> 625
45 gates green · smoke 167 · search 59 · the axe suite not rerun: a card, not a topic
```

## Session — the hundred-and-second wave, an anomaly is context, not a finding

§106's queue, its first item. *Content ideas* §107 is the table.

### Read first

Microsoft Learn's pages on threat detection in Sentinel, its anomalies, threat intelligence, SOC optimization, and
custom tables in Azure Monitor Logs, fetched while the hundred-and-first wave's gates ran. Six census queries went in
before the cards.

### What the gates found

The census opened at 0 of 6, two zeros and four that found other cards, and closed at 6 of 6 with nothing replaced and no
word changed. The annotator added five expansions, among them STIX and TAXII, which the dictionary already knew. The
anomalies page was fetched and not cited: the detection page already says everything the card says about anomalies.

```
2 commits · 2 cards in 1 existing topic · 4 anchors
6 census queries, 0 of 6 -> 6 of 6 · census 989 of 1,011, 0 unexplained · dated claims 625 -> 629
45 gates green · smoke 167 · search 59 · the axe suite not rerun: cards, not a topic
```

## Session — the hundred-and-third wave, a hunt with its steps hidden

§107's queue, SC-200's last three gaps. *Content ideas* §108 is the table.

### Read first

Microsoft Learn's pages on the hunting graph, the Sentinel graph, Jupyter notebooks, Sentinel's support for MCP and
Microsoft Graph activity logs, fetched while the hundred-and-second wave's gates ran. Six census queries went in before
the cards.

### What the gates found

The census opened at 0 of 6, two zeros and four that found other cards. Five answered once the cards were in; the sixth,
*which app called the graph api*, needed the Graph card to say so in those words. The annotator expanded MCP in the
hunting card's title, which made the body's own spelled-out name a repeat, so the body now says only that the server is
hosted by Microsoft behind Entra sign-in.

```
2 commits · 2 cards in 2 existing topics · 5 anchors · SC-200's gap list closed
6 census queries, 0 of 6 -> 6 of 6 · census 995 of 1,017, 0 unexplained · dated claims 629 -> 634
45 gates green · smoke 167 · search 59 · the axe suite not rerun: cards, not a topic
```

## Session — the hundred-and-fourth wave, Purview gets its own exam path

§108's queue, its first item. *Content ideas* §109 is the table and the gap list.

### Read first

Microsoft's SC-401 study guide, skills measured as of 28 October 2026, fetched while the hundred-and-third wave's gates
ran, and its terms counted across the data files before any gap was listed. Fifteen terms have no hits, from trainable
classifiers to Audit (Premium); the rest were found in the topics that became the path's steps.

### What the gates found

`check_paths.py` found every step's topic. The path added no topic, so the census and the share image did not move.

```
2 commits · 1 path, 16 steps · paths 125 -> 126, steps 2,526 -> 2,542 · 0 topics, 0 cards
45 gates green · smoke 167 · search 59 · the axe suite not rerun: a path, not a topic
```
