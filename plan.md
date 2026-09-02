# Improvement Plan — Tech & Life Reference (July 2026 Review)

> **Status: ✅ All items applied** across six commits (Phases 1–6). Verified
> headless (Chromium): keyboard nav, search, permalinks, progress, notepad,
> offline fonts — zero network/console errors.

Full repository review covering performance, security, interface/UX, and repo hygiene.
Each item lists evidence, why it matters, and the fix. Checkboxes track what's been applied.

> The previous `plan.md` (2026 structural fix plan — split of the monolith into
> `index-shell.html` + `data/*` + `build.py`) was fully completed and is preserved
> in git history.

---

## Where things are — an index, because this file is 11,600 lines

Added when the revisited risk register named the file's own length as an open risk. The
live queue is Phases 7–11 at the bottom; everything above line 10,000 is closed and is kept
for the reasoning rather than the tasks.

| Section | Line | What it is | State |
|---|---|---|---|
| Improvement Plan (July 2026 review) | 1 | Performance, security, UX, repo hygiene | ✅ closed |
| Content Roadmap — Waves 15+ | ~337 | The first content expansion | ✅ closed |
| Architecture, Engineering & DevOps — Wave 27+ | ~647 | `eng` and `devops` foundations | ✅ closed |
| Phase 3 — Depth, Breadth & New Domains | ~803 | Tracks J–U. **Headline lesson: the backlog count was badly inflated** — grepping for a topic's *name* systematically overstated what was missing | ✅ closed |
| Phase 4 — The Enterprise Estate & the Study Platform | ~1482 | `m365`, `endpoint`, `infra`, plus SRS, quiz, export/import | ✅ closed |
| Phase 5 — Foundations, Frontiers & the Business of IT | ~2377 | `cs`, `ai`, consulting, privacy engineering, freshness tooling | ✅ closed |
| **Project risk register** | ~3472 | Event risks, imagined. Four now mitigated, four re-scored this session | 📘 living |
| Execution Handbook, Parts 1 & 2 | ~3542 | Ordering constraints, per-domain queue, ten session specs. **The specced ones are the ones that got built** | 📘 reference |
| Calculus track | ~4500 | `math` domain and the TI-84 tooling | ✅ closed |
| **What is actually outstanding** | ~4640 | The audit sections: defects, the lint trend, undersized domains, content age. All four now resolved and re-measured | ✅ closed |
| Session records | ~5100–10,360 | Roughly forty of them. The reasoning behind every decision above | 📘 archive |
| **Phase 7 — the next hundred cards** | ~10,365 | 93 cards shipped across 15 tracks; 3 rejected as duplicates. The probe over-counted again | ✅ **closed** |
| **Phase 8 — the depth problem** | ~10,754 | 330 thin → **147**, eighteen waves, 144 cards. §8's target met | ✅ **closed** |
| Worked specifications | ~10,897 | Four sessions written out to transcription depth | 📘 reference |
| **The card rubric** | ~10,988 | What the good cards have, measured from forty written in one session | 📘 reference |
| **Phase 9 — the duplication problem** | ~11,072 | Queue C1–C6 complete: **12 merges, 1 move, 1 link**, a dozen documented refusals | ✅ **closed** |
| **Phase 10 — the tooling** | ~11,175 | All nine shipped. **Five of them found a defect in something other than themselves** | ✅ **closed** |
| Domain shape | ~11,322 | The connectivity graph: hubs, broadcasters, islands | 📘 reference |
| **Phase 11 — the verification debt** | ~11,411 | 51 dated claims, and why the denominator is not countable | ⬜ **live** |
| **The session operating manual** | ~11,522 | The loop, the ordering constraints, and ten failures with their guards | 📘 **start here** |
| The risk register, revisited | ~11,624 | Four accumulation risks that only a measurement could find | 📘 living |

**If you read three things:** the session operating manual, the card rubric, and whichever
live phase you are about to work on. Line numbers drift as records are appended — the headings
are stable, the numbers are a hint.

---

## What's in this file

`plan.md` has grown into the project's full roadmap history. Read it in order or
jump to what you need:

| Section | What it is | Status |
|---|---|---|
| **Improvement Plan** (P1–P5) | The original repo review — performance, security, UX, hygiene | ✅ applied |
| **Content Roadmap — Next Waves** (Tracks R/B/C/X) | Red team, blue team, cloud, rounding out existing domains | ✅ shipped |
| **Architecture, Engineering & DevOps** (Tracks E/F/G) | Software architecture, DevOps, developer environment | ✅ shipped |
| **Phase 3 — Depth, Breadth & New Domains** (Tracks H–U) | `data` and `web` domains shipped; depth tracks **J–U outstanding (207 cards)** | 🔶 half done |
| **Phase 4 — The Enterprise Estate & the Study Platform** (Tracks V–AK) | Windows Server, M365, endpoint depth, virtualization, ITSM, vendor networking, automation, Apple/mobile, OT/regulated, AI at work + study tooling | ⬜ planned |
| **Phase 5 — Foundations, Frontiers & the Business of IT** (Tracks AL–AY) | CS & mathematics, hardware/embedded, post-quantum, emerging platforms, physical security, IT finance, leadership, enablement, consulting + content-trust tooling | ⬜ planned |
| **Phase 6 — Specialisms, and How This Gets Written** (Tracks BA–BJ) | Detection engineering, purple teaming, Kubernetes security, API/identity security, supply chain, privacy engineering, platform engineering, observability, resilience — **plus the card pattern library, authoring rules, risk register and success measures, written out rather than planned** | ⬜ planned |
| **Execution Handbook** | Ordering constraints, per-domain queue, a concrete first-ten-sessions schedule, three waves specified to the point of transcription, and reusable checklists | 📘 reference |
| **What is actually outstanding** | An audit of the repo as it really is — defects, the lint trend, undersized domains, content age. **Start here.** | ✅ short list cleared, session 18 |

**Remaining backlog: ~828 content cards and 44 engineering items** across
Phases 3–6, which would take the site from **1,008 topics / 29 domains** to roughly
1,800 topics — about 165 working sessions.

> **Phase 3 is complete as of the current session — 1,044 topics / 28 domains.**
> Tracks J, K, L, M, N, O, P, Q, S, T, U all resolved. The headline lesson, repeated
> across every one of them: the backlog count above is badly inflated. Track after
> track was already 60–100% built in a neighbouring domain, and grepping for a topic's
> *name* systematically overstated what was missing — a framework's name in a
> comparison table is not the same as a card covering it. The real remaining Phase-3
> work was a fraction of the spec: a few dozen genuine gap cards, not ~176. The
> honest per-track accounting is in each track's block below.

**If you read only two things:** *"What is actually outstanding"* at the very end
of this file, and *Part 3 of Phase 6* (how to write a card, the pattern library,
the risk register). The backlog is a menu, not a queue — and at this size, how
well each card is written matters more than how many remain.

### How to read a track's checklist

A mechanical count of `- [ ]` lines across this file badly overstates the real backlog,
for a structural reason worth knowing before you plan a session.

Most tracks now carry a **shipped-note** — a short bold paragraph at the top of the track
recording what was actually built, which items were consolidated into which card, and what
was deliberately left. Those notes are accurate. The `- [ ]` wave lists *underneath* them
are the **original specification**, written before anything shipped, and in most tracks they
were never ticked afterwards. Both are useful — the note says what exists, the spec says
what was once imagined — but only the note is current.

So: **where a track has a shipped-note, read the note first and treat the wave lists below it
as background.** Tracks carrying such a note are marked `⟵ see the shipped-note above` on
their first wave heading. Tracks without a note have checklists that mean what they say.

Three item states are used, and the distinction matters:

| Mark | Means |
|---|---|
| `- [x]` | Shipped. Where a card covers several specced items, the annotation says which card |
| `- [~]` | Genuinely covered, elsewhere — the annotation names the existing card and domain |
| `- [ ]` | Actually open |

`[~]` is doing a lot of work in the later tracks and should keep doing it. The repeated
finding of this project is that a track reads as unbuilt while being 60–100% covered by a
neighbouring domain under different card titles, and marking those `[~]` with a location is
what stops the next session rewriting them.

**What that convention is worth, measured.** At the time this note was written the file
contained **245** unticked `- [ ]` lines. **159 of them sit inside the nine tracks that carry
a shipped-note** — Y, Z, AC, AD, AE, AF, AP, AQ, AR — and are largely superseded by it. Only
**86** are in tracks whose checklists still mean what they say. A session that plans from the
raw count will pick a track that is mostly already built; a session that reads the notes first
will not.

---

## P1 — High-impact quick wins

### 1. Remove ~135 KB of dead code from `script.js`
- **Evidence:** `script.js` is 152 KB but only ~17 KB is live logic. Lines ~209–670
  embed a `DISORDER_DATA` blob (DSM mental-disorders text) plus a panel-builder IIFE
  that targets `[data-domain="mental-disorders"]` — but `index.html` contains **zero**
  `mental-disorders` elements (domain was never added to `data/domains.json`).
  Every visitor downloads and parses 135 KB that can never execute.
- **Fix:** Delete the `DISORDER_DATA` blob and its panel-builder IIFE from `script.js`.
  If the mental-disorders domain is wanted later, add it properly as a
  `data/` domain and load the blob lazily from its own file.
- [x] Applied

### 2. Delete duplicate/dead data files
- **Evidence:** `data/disorder_data.js` and `Patches files/disorder_data.js` are
  byte-identical (135,544 bytes each) and **neither is loaded by anything**
  (no `<script src>` references in `index-shell.html`/`index.html`).
- **Fix:** Delete both (git history preserves them).
- [x] Applied

### 3. Delete `studies.html` (560 KB)
- **Evidence:** Old pre-split monolith ("CompTIA & Tech Reference" title, old
  formatting). Nothing references it — not `index.html`, `script.js`, or `README.md`.
- **Fix:** Delete. It's a stale snapshot that will only drift further from reality.
- [x] Applied

### 4. Fix the `.topic-chevron` styling bug (287 topics affected)
- **Evidence:** Newer content waves emit `<span class="topic-chevron">›</span>`
  (287 occurrences in `data/*.html`) but `style.css` only defines `.topic-chev`
  (112 occurrences use that). The 287 newer topics have an unstyled chevron that
  doesn't rotate on expand.
- **Fix (pick one):**
  - a) One-time `sed` across `data/*.html`: `topic-chevron` → `topic-chev`, rebuild; or
  - b) Add `.topic-chevron` as an alias selector next to every `.topic-chev` rule.
  Option (a) is cleaner long-term.
- [x] Applied

### 5. Crush the image weight (~14 MB → well under 1 MB)
- **Evidence:**
  - `Img/Studying-Tips.png` = **7.5 MB** — loaded in the page header.
  - `Img/favicon/favicon.svg` = **6.7 MB** — an SVG favicon should be ~1–5 KB;
    this almost certainly has a giant embedded raster.
  - `Img/favicon/web-app-manifest-512x512.png` = 388 KB.
- **Fix:** Re-export Studying-Tips as WebP/optimized PNG at display resolution
  (~100–300 KB); regenerate favicon.svg as a true vector (or drop it — the
  96×96 PNG + .ico already cover browsers); `oxipng`/`squoosh` the manifest PNGs.
- [x] Applied

---

## P2 — Performance

### 6. Minify output in `build.py` (~450 KB / 19% off index.html)
- **Evidence:** `index.html` is 2,375,874 chars; stripping leading indentation
  alone saves 19% (~452 KB). The data files are heavily indented.
- **Fix:** In `build.py`, strip leading whitespace and collapse blank lines when
  assembling (safe for this markup — but skip lines inside `<pre`…`</pre>` so
  `.code-block` formatting is preserved). Keep `data/*.html` pretty for editing;
  only the built output gets minified.
- [x] Applied

### 7. Debounce + index the search (currently full-DOM scan per keystroke)
- **Evidence:** `index-shell.html:92` wires `oninput="searchContent(this.value)"`;
  `searchContent()` (script.js ~708) walks every `.domain-section`/`.topic` and
  lowercases each topic's full `textContent` on **every keystroke** against a
  2.4 MB DOM. No debounce.
- **Fix:** (a) debounce 150–250 ms; (b) build a one-time cache
  `Map<topicEl, lowercasedText>` on first search and reuse it; (c) only run
  highlighting on the visible/matched topics (already mostly true).
- [x] Applied

### 8. Fix search-highlight markup corruption
- **Evidence:** `highlightIn()` (script.js ~695) does
  `el.innerHTML = el.innerHTML.replace(re, '<mark>…')` — despite the comment
  claiming "text nodes only", it regex-replaces the raw HTML string. Searching
  terms that appear inside tags/attributes (e.g. `table`, `span`, `color`,
  `href`) injects `<mark>` inside tags and corrupts the DOM until cleared.
- **Fix:** Walk actual text nodes (`TreeWalker` with `NodeFilter.SHOW_TEXT`) and
  wrap matches in `<mark>` — never string-replace `innerHTML`.
- [x] Applied

### 9. Replace the runtime React+Babel notepad stack
- **Evidence:** `index-shell.html:20-22` loads React 18 + ReactDOM + **Babel
  standalone** (~3 MB combined) from unpkg, then `toggleNotepad()` fetches
  `notepad.jsx` as `text/babel` and compiles JSX **in the browser**. Two extra
  problems: (a) opened via `file://` (the documented usage), the `notepad.jsx`
  fetch is blocked by CORS — the notepad never loads; (b) the notepad is a
  simple CRUD list over localStorage that doesn't need React at all.
- **Fix:** Rewrite the notepad as ~100 lines of vanilla JS inside `script.js`,
  delete `notepad.jsx`, and remove all three CDN `<script>` tags. This also
  fixes the file:// breakage and removes the biggest third-party dependency.
- [x] Applied

### 10. Self-host or gracefully degrade Google Fonts
- **Evidence:** Both `index-shell.html` and `notepad.jsx` pull Share Tech Mono +
  Outfit from `fonts.googleapis.com`. Offline / file:// use falls back silently;
  it's also the only remaining third-party call once #9 lands.
- **Fix:** Either self-host the two WOFF2 files under `Img/fonts/` (works
  offline, no tracking), or keep the CDN but add
  `<link rel="preconnect" href="https://fonts.gstatic.com">` and rely on
  `display=swap` (already present).
- [x] Applied

---

## P3 — Security

### 11. Unpinned third-party scripts (supply-chain risk)
- **Evidence:** `https://unpkg.com/@babel/standalone/babel.min.js` has **no
  version pin** — unpkg serves the latest tag, so a compromised or broken
  release ships straight to the page. React/ReactDOM are major-pinned only
  (`react@18`). None have Subresource Integrity (SRI) hashes.
- **Fix:** Item #9 removes all three. If any CDN script is ever kept: pin the
  exact version and add `integrity="sha384-…" crossorigin="anonymous"`.
- [x] Applied (superseded by #9)

### 12. `target="_blank"` without `rel="noopener noreferrer"`
- **Evidence:** 1 occurrence in `data/script.html`. Opened pages get a
  `window.opener` handle (tab-nabbing) — low risk here but free to fix.
- **Fix:** Add `rel="noopener noreferrer"`; make it a convention for future content.
- [x] Applied

### 13. "Shared" notepad isn't shared — clarify or wire a backend
- **Evidence:** `notepad.jsx` stores notes in `localStorage`
  (`shared-notepad-notes`) and polls every 8 s "for new notes from others" —
  but localStorage never leaves the browser. The UI wording ("shared notepad")
  overpromises; the polling only syncs tabs on the same machine.
- **Fix:** When rewriting (#9), rename to "Notepad", keep localStorage, and use
  the `storage` event instead of polling. (A real shared backend would need a
  service + auth — out of scope for a static site.)
- [x] Applied

### 14. Secrets check — clean ✅
- Grep across the repo (including `Patches files/`) found no API keys, tokens,
  or credentials. `.gitignore` covers `.env*`, `*.bak`, `__pycache__/`, and
  nothing tracked violates it. Keep it that way: any future Gemini/API work
  must use env vars or GitHub Actions secrets, never committed files.

---

## P4 — Interface, UX & accessibility

### 15. Keyboard accessibility for accordions
- **Evidence:** `.domain-header` / `.topic-header` are `<div>`s toggled by click
  delegation — not focusable, no `role`, no `aria-expanded`, unusable without a
  mouse.
- **Fix:** At load, JS can decorate every header with `tabindex="0"`,
  `role="button"`, and synced `aria-expanded` (no need to touch 400+ topics in
  `data/`), and handle `Enter`/`Space` in a `keydown` delegate.
- [x] Applied

### 16. Per-topic permalinks + deep linking
- **Evidence:** No way to link someone to a specific topic; the page always
  opens fully collapsed at the top.
- **Fix:** At load, assign stable slug `id`s to each `.topic` (from topic name);
  on header click update `location.hash`; on load, expand + scroll to the
  hash target. Pairs well with a "copy link" icon on each topic header.
- [x] Applied

### 17. Study-progress tracking ("mark as reviewed")
- **Idea:** This is a study site with hundreds of topics and no sense of
  progress. A small checkmark toggle per topic persisted to localStorage
  (`reviewed:{slug}`), plus a per-domain "12/31 reviewed" counter in the domain
  header, would make revision passes far more effective. Cheap to build on top
  of #16's slugs.
- [x] Applied

### 18. Back-to-top button + print stylesheet
- **Evidence:** The built page is very long; there's no quick way back to the
  filter bar. Printing currently emits dark backgrounds and collapsed bodies.
- **Fix:** Floating ↑ button (appears after ~2 screens). `@media print`: force
  light theme, expand all bodies, hide header controls/notepad/search.
- [x] Applied

### 19. `prefers-reduced-motion` support
- **Evidence:** Accordion/theme transitions animate unconditionally.
- **Fix:** `@media (prefers-reduced-motion: reduce)` block that zeroes
  transition durations and disables animations.
- [x] Applied

### 20. Normalize content-markup conventions for future waves
- **Evidence:** Generations of patch scripts diverged: `topic-chevron` vs
  `topic-chev` (287 vs 112 — see #4), `ai-table` (361) vs `ref-table` (136,
  both styled but visually different), **1,527** inline `style="…"` attributes
  in `data/*.html` (mostly `color:var(--cyan)` variants).
- **Fix:** Don't churn existing content. Instead: (a) add utility classes
  (`.c-cyan`, `.c-amber`, `.c-green`, `.c-red`) to `style.css`; (b) write a short
  `CONTRIBUTING.md` (or README section) defining the canonical topic skeleton —
  one chevron class, one table class, utility classes over inline styles — so
  future content (human- or AI-authored) stays consistent.
- [x] Applied

---

## P5 — Repo hygiene, docs & tooling

### 21. Rename `Patches files/` → `patches/`
- **Evidence:** The space in the directory name forces quoting in every shell
  command and breaks naive tooling. It holds ~1.9 MB of one-time,
  already-applied injection scripts.
- **Fix:** `git mv "Patches files" patches`. Optionally add `patches/README.md`
  noting these are historical (idempotent, already applied — safe to re-run but
  never needed).
- [x] Applied

### 22. Update `README.md` to match reality
- **Evidence:** README's project-structure block omits `studies.html`,
  `notepad.jsx`, `reconcile_build.py`, `Patches files/`, and `plan.md`; it
  documents `domains.js` (actual file is `domains.json`), and the notepad/CDN
  dependency isn't mentioned anywhere.
- **Fix:** Refresh the structure block after P1 deletions land; document
  `reconcile_build.py` (recovery tool: syncs a hand-patched `index.html` back
  into `data/*`) and the build workflow (`edit data/ → python3 build.py`).
- [x] Applied

### 23. CI guard: fail if `index.html` is stale
- **Evidence:** `index.html` is a tracked build artifact; nothing verifies it
  matches `data/*`. A hand-edit to `index.html` silently diverges (the failure
  mode `reconcile_build.py` exists to repair).
- **Fix:** GitHub Action on push/PR: `python3 build.py && git diff --exit-code
  index.html`. ~15 lines of YAML; catches drift forever.
- [x] Applied

### 24. Repo growth awareness
- **Evidence:** Every content wave re-commits the full 2.4 MB `index.html`;
  ~50 waves in, history carries dozens of full copies (git delta-compresses,
  but HTML deltas across injections are large).
- **Fix:** Keep tracking `index.html` (file:// usage depends on it), but the
  minification in #6 shrinks each future delta, and the P1 deletions
  (`studies.html`, dead data, 14 MB of images) stop the worst bloat. No history
  rewrite needed.
- [x] Applied (via #5, #6)

---

## Suggested execution order

| Phase | Items | Effort | Payoff |
|-------|-------|--------|--------|
| 1 | #1 #2 #3 #5 (deletions + images) | ~1 hour | −15 MB shipped weight, −135 KB JS |
| 2 | #4 #12 (chevron fix, noopener) | minutes | visible styling fix on 287 topics |
| 3 | #6 #7 #8 (build minify, search) | ~2 hours | faster load + correct search |
| 4 | #9 #10 #11 #13 (notepad rewrite) | ~2 hours | notepad works on file://, no CDN risk |
| 5 | #15 #16 #17 #18 #19 (UX/a11y) | ~3 hours | keyboard nav, permalinks, progress |
| 6 | #20 #21 #22 #23 (conventions, docs, CI) | ~2 hours | future waves stay consistent |

---

# Content Roadmap — Next Waves (Wave 15+)

> **Context.** Waves 1–14 added 42 topics across the 12 existing domains (Python,
> TypeScript, OAuth, MCP, Terraform, BGP, MLOps, GitOps, WAF, SOAR, …); the site
> now holds ~530 topics and every build stays CI-green. This roadmap plans the
> **next** waves, driven by three explicit asks — **Red team tools**, **Blue team
> tools**, and **AWS + Google Cloud how-to** — plus cross-cutting gaps to round
> out the existing domains. "The more the better": this is deliberately large;
> pull waves off the top as capacity allows.

## Scope guardrail (Red/Blue content)

All offensive content is authored as **reference cards for authorized testing,
CTF, and cert prep** (PenTest+, OSCP, CySA+, GCIH) — matching the existing
`pentest` domain and its "Ethical Hacking 101" / "Scoping & Rules of Engagement"
topics. Each tool card states **what it is, legitimate use, key flags/workflow,
and a defensive detection note** — never novel weaponization, working malware, or
target-specific exploit chains. Every red-team card carries a one-line
"authorized use only" reminder, and pairs with a Blue-team detection angle so the
two tracks reinforce each other.

## Structural decision — three new domains (recommended)

Red tooling, Blue tooling, and Cloud are each large enough (15–35 topics) that
folding them into `pentest`/`ops`/`net` would bloat those and mix concept-topics
with tool-reference cards. Recommend **three new domains**, which `build.py`
already supports (it renders any entry in `data/domains.json` that has a matching
`data/{id}.html`).

**Wave 15 — domain scaffolding (prep, ~30 min):**
- [x] Add three entries to `data/domains.json`:
  - `redteam` 🔴 "Red Team & Offensive Tooling" — cert tags PT+ / OSCP
  - `blueteam` 🔵 "Blue Team & Defensive Tooling" — cert tags CySA+ / GCIH
  - `cloud`   ☁️ "Cloud Platforms — AWS · GCP · Azure" — cert tags AWS / GCP
- [x] Add three filter chips to `index-shell.html` (`data-domain`, `.c-redteam`
  / `.c-blueteam` / `.c-cloud` classes).
- [x] Add `.domain-redteam` / `.domain-blueteam` / `.domain-cloud` accent colors
  and `.chip.c-*` rules to `style.css` (mirror an existing domain's block).
- [x] Create empty `data/redteam.html` / `data/blueteam.html` / `data/cloud.html`
  with the trailing sentinel comment, then `python3 build.py` to verify 15 domains
  render and filter.
- *(Alternative if you'd rather not add domains: red cards → `pentest`, blue cards
  → `ops`/`threat`, cloud → a mix of `net`/`ops`. Doable, but noisier. Decide at
  Wave 15.)*

---

## TRACK R — Red Team & Offensive Tooling  (→ `redteam`)

Tool reference cards, grouped by kill-chain stage. ~9 waves, ~50 cards.

**Wave R1 — Recon & OSINT tooling**
- [x] Nmap — Deep Dive (scan types, NSE scripts, timing, output formats)
- [x] Masscan & RustScan — Internet-scale port discovery
- [x] theHarvester & Recon-ng — email/subdomain/host OSINT frameworks
- [x] Amass & Subfinder — subdomain enumeration at scale
- [x] Shodan & Censys — the search engines for exposed devices (dorks & filters)
- [x] Maltego & SpiderFoot — link-analysis / automated OSINT
- [x] Google Dorking & GHDB — advanced operators for exposed data

**Wave R2 — Web app attack tooling**
- [x] Burp Suite — Proxy, Repeater, Intruder, Scanner workflow
- [x] OWASP ZAP — the open-source web proxy/scanner
- [x] sqlmap — automated SQL injection (levels, risk, tamper scripts)
- [x] ffuf & Gobuster — content/parameter/vhost fuzzing
- [x] Nuclei — templated vulnerability scanning (dual-use with Blue)
- [x] Nikto & wpscan — web server & WordPress scanning

**Wave R3 — Exploitation frameworks**
- [x] Metasploit Framework — modules, sessions, msfconsole workflow
- [x] msfvenom — payload generation & encoders (concepts + formats)
- [x] Searchsploit / Exploit-DB — finding & vetting public exploits
- [x] Impacket — the Python toolkit (psexec, secretsdump, wmiexec, ntlmrelayx)
- [x] Nuclei/CrackMapExec as exploitation orchestrators

**Wave R4 — Active Directory attack tooling**
- [x] BloodHound / SharpHound — AD attack-path graphing
- [x] Mimikatz — credential extraction (what it does; Blue detections)
- [x] Rubeus & Kerbrute — Kerberos abuse (roasting, AS-REP, TGT)
- [x] Responder & ntlmrelayx — LLMNR/NBT-NS poisoning & relay
- [x] NetExec (CrackMapExec) — the AD swiss-army knife
- [x] PowerView / PowerSploit — AD enumeration from PowerShell
- [x] Certify / Certipy — AD CS (ADCS) abuse (ESC1–ESC8 overview)

**Wave R5 — Command & Control (C2)**
- [x] C2 Concepts — beacons, listeners, redirectors, malleable profiles
- [x] Cobalt Strike — the commercial standard (what defenders look for)
- [x] Sliver — the open-source modern C2
- [x] Mythic & Havoc — agent/collaboration frameworks
- [x] Empire / Starkiller — PowerShell/Python post-ex C2

**Wave R6 — Password & hash attacks**
- [x] Hashcat — modes, masks, rules, GPU cracking workflow
- [x] John the Ripper — formats, wordlist/incremental, jumbo
- [x] Hydra & Medusa — online/network login brute-forcing
- [x] Wordlists & CeWL/Crunch — rockyou, custom lists, mangling
- [x] Hash identification & extraction (hashid, /etc/shadow, NTDS)

**Wave R7 — Wireless & hardware**
- [x] Aircrack-ng suite — capture, deauth, WPA handshake cracking
- [x] Wifite & hcxdumptool — automated Wi-Fi + PMKID attacks
- [x] Bettercap — MITM framework (Wi-Fi, BLE, HID, ARP)
- [x] Kismet — wireless detection & sniffing
- [x] Flipper Zero — Sub-GHz/RFID/NFC/IR/BadUSB multi-tool
- [x] Rubber Ducky / O.MG cable — HID injection (BadUSB)
- [x] Proxmark3 & HackRF — RFID cloning & software-defined radio

**Wave R8 — Post-exploitation, evasion & LOLBins**
- [x] Living off the Land — LOLBAS / GTFOBins (built-ins as weapons)
- [x] Privilege escalation scanners — linPEAS / winPEAS / PowerUp
- [x] AMSI & AV/EDR evasion — concepts, obfuscation, why it works (defensive lens)
- [x] Pivoting & tunneling — Chisel, ligolo-ng, SSH/socks, proxychains
- [x] Data exfil channels — DNS/ICMP/HTTPS tunneling (detection notes)

**Wave R9 — Cloud & container offense**
- [x] Pacu — the AWS exploitation framework
- [x] CloudFox & enumerate-iam — cloud attack-surface enumeration
- [x] Kubernetes attacks — kube-hunter, RBAC abuse, container escape
- [x] Cloud credential attacks — SSRF→IMDS, key theft, role chaining
- [x] Purple-team bridge — mapping the above to ATT&CK & detections

---

## TRACK B — Blue Team & Defensive Tooling  (→ `blueteam`)

~8 waves, ~45 cards. Each pairs where possible with a Red card above.

**Wave B1 — Network security monitoring**
- [x] Wireshark — capture, display filters, Follow Stream, analysis
- [x] tcpdump — CLI capture & BPF filters (field card, deeper than the net topic)
- [x] Zeek (Bro) — network metadata logging & scripting
- [x] Suricata & Snort — signature IDS/IPS, rule syntax
- [x] Arkime / ntopng — full-packet capture & traffic analytics

**Wave B2 — SIEM & log analytics**
- [x] Splunk — SPL query language, indexes, dashboards, alerts
- [x] Elastic / ELK Stack — Elasticsearch, Logstash, Kibana, Beats
- [x] Wazuh — open-source XDR/SIEM (agents, rules, decoders)
- [x] Graylog & Loki — log aggregation alternatives
- [x] Sigma — vendor-neutral detection rules (write once, convert anywhere)

**Wave B3 — Endpoint visibility & EDR**
- [x] Sysmon — the Windows telemetry powerhouse (config, event IDs)
- [x] OSQuery — your endpoints as a SQL-queryable fleet
- [x] Velociraptor — endpoint DFIR & hunting at scale
- [x] Windows Event Logs — the IDs that matter (4624/4625/4688/4768…)
- [x] auditd & Linux endpoint logging

**Wave B4 — Detection engineering**
- [x] YARA — pattern-matching rules for malware/files
- [x] Sigma-to-SIEM — detection-as-code workflow
- [x] MITRE ATT&CK mapping & Navigator — coverage-driven detection
- [x] Atomic Red Team & Caldera — adversary emulation to test detections
- [x] Detection tuning — reducing false positives, alert fatigue

**Wave B5 — Digital forensics & IR (DFIR)**
- [x] Volatility — memory forensics (processes, injection, artifacts)
- [x] Autopsy / The Sleuth Kit — disk forensics
- [x] KAPE & plaso/log2timeline — triage collection & super-timelines
- [x] Chain of custody & evidence handling (procedure card)
- [x] Windows forensic artifacts — Prefetch, ShimCache, AmCache, MFT, registry

**Wave B6 — Threat intelligence & sharing**
- [x] MISP — threat-intel sharing platform (IOCs, feeds, taxonomies)
- [x] OpenCTI — structured CTI knowledge base
- [x] STIX / TAXII — the standards for exchanging threat intel
- [x] VirusTotal / Hybrid Analysis / Any.Run — sample analysis & sandboxing
- [x] Pyramid of Pain & IOC vs TTP-based detection

**Wave B7 — Vuln management, hardening & benchmarks**
- [x] Nessus & OpenVAS/Greenbone — vulnerability scanners
- [x] CIS Benchmarks & CIS-CAT — hardening baselines
- [x] Lynis — Linux/Unix audit & hardening
- [x] OpenSCAP & DISA STIGs — compliance-driven hardening
- [x] Patch & config management (WSUS/Ansible) as a control

**Wave B8 — Deception & email/identity defense**
- [x] Honeypots & Canarytokens — deception tech (T-Pot, canaries)
- [x] Email security stack — SPF/DKIM/DMARC enforcement, sandboxing, banners
- [x] Identity threat detection — impossible travel, ITDR, conditional access
- [x] Purple teaming — running the exercise & closing detection gaps

---

## TRACK C — Cloud Platforms: AWS & GCP How-To  (→ `cloud`)

~9 waves, ~50 cards. Parallel AWS/GCP structure so learners can cross-map, with
an explicit "Rosetta stone" card. Azure kept as a lighter bonus set.

**Wave C1 — Cloud foundations & getting started**
- [x] Cloud Fundamentals — IaaS/PaaS/SaaS, regions/AZs, shared-responsibility
- [x] AWS — Getting Started (account, root vs IAM, console vs CLI, free tier)
- [x] AWS CLI & CloudShell — install, configure, profiles, `--query` JMESPath
- [x] GCP — Getting Started (org/folder/project hierarchy, billing)
- [x] gcloud CLI & Cloud Shell — init, config, `gcloud`/`gsutil`/`bq`
- [x] Cloud Service Rosetta Stone — AWS ↔ GCP ↔ Azure equivalents table

**Wave C2 — Identity & access (the #1 cloud risk)**
- [x] AWS IAM — users, groups, roles, policies (identity vs resource vs SCP)
- [x] AWS IAM Deep — assume-role, STS, permission boundaries, least privilege
- [x] GCP IAM — members, roles (basic/predefined/custom), resource hierarchy
- [x] GCP Service Accounts & Workload Identity — machine auth done right
- [x] Cloud IAM pitfalls — wildcard policies, privilege escalation paths

**Wave C3 — Networking**
- [x] AWS VPC — subnets, route tables, IGW/NAT, security groups vs NACLs
- [x] AWS Load Balancing & DNS — ALB/NLB, Route 53, CloudFront
- [x] GCP VPC — global VPC, subnets, firewall rules, Cloud NAT
- [x] GCP Load Balancing & DNS — global LB, Cloud DNS, Cloud CDN
- [x] Hybrid connectivity — VPN, Direct Connect / Cloud Interconnect, peering

**Wave C4 — Compute**
- [x] AWS Compute — EC2, AMIs, instance types, Auto Scaling, spot
- [x] AWS Serverless & Containers — Lambda, ECS, EKS, Fargate
- [x] GCP Compute — Compute Engine, machine families, MIGs, preemptible
- [x] GCP Serverless & Containers — Cloud Run, Cloud Functions, GKE
- [x] Choosing compute — VM vs container vs serverless decision guide

**Wave C5 — Storage & databases**
- [x] AWS Storage — S3 (deep), EBS, EFS, storage classes & lifecycle
- [x] AWS Databases — RDS, Aurora, DynamoDB, ElastiCache
- [x] GCP Storage — Cloud Storage, Persistent Disk, Filestore
- [x] GCP Databases — Cloud SQL, Spanner, Firestore, Bigtable
- [x] BigQuery — serverless analytics warehouse (SQL, slots, cost)

**Wave C6 — Cloud security services**
- [x] AWS Security Stack — CloudTrail, Config, GuardDuty, Security Hub, Inspector
- [x] AWS Data Protection — KMS, Secrets Manager, encryption at rest/in transit
- [x] GCP Security Stack — Cloud Logging/Audit, Security Command Center
- [x] GCP Data Protection — Cloud KMS, Secret Manager, VPC Service Controls
- [x] CSPM & cloud posture — ScoutSuite, Prowler, Steampipe (Blue-team bridge)

**Wave C7 — Infrastructure as Code & DevOps on cloud**
- [x] Terraform on AWS/GCP — providers, remote state, modules (ties to ops topic)
- [x] AWS-native IaC — CloudFormation & CDK
- [x] GCP-native IaC — Deployment Manager & Config Controller
- [x] Cloud CI/CD — CodePipeline / Cloud Build, artifact registries
- [x] Cloud cost control — budgets, tagging, Cost Explorer / billing export (→ FinOps)

**Wave C8 — Observability & operations on cloud**
- [x] AWS Observability — CloudWatch (metrics/logs/alarms), X-Ray
- [x] GCP Observability — Cloud Monitoring, Cloud Logging, Cloud Trace
- [x] Well-Architected / Architecture Framework — the 5–6 pillars
- [x] Landing zones & multi-account/project — Organizations, Control Tower

**Wave C9 — Azure bonus (lighter set)**
- [x] Azure — Getting Started, Entra ID (formerly Azure AD)
- [x] Azure Core — Resource Groups, VNet, VMs, Storage Accounts
- [x] Azure Security — Defender for Cloud, Key Vault, Sentinel (SIEM)

---

## TRACK X — Round out existing domains ("the more the better")

Lower priority than R/B/C but each fills a real gap; interleave as desired.

**Languages (`script`)**
- [x] Rust · Java · C# / .NET · Ruby · PHP · C — one card each (mirror the Go/Python style)
- [x] Assembly & how programs run — registers, stack, calling conventions (pairs w/ RE)
- [x] Semantic Versioning & dependency management (npm/pip/cargo lockfiles)

**Networking (`net`)**
- [x] Network Automation — Ansible, Netmiko, NAPALM, gNMI
- [x] SD-WAN & MPLS · Multicast · PoE · 802.1Q trunking deep-dive
- [x] DNSSEC, DoH/DoT — securing name resolution

**Linux (`linux`)**
- [x] Podman & rootless containers · systemd deep-dive · sysctl/kernel tuning
- [x] ZFS & Btrfs — snapshots, subvolumes, integrity
- [x] Advanced Bash — traps, parameter expansion, coprocesses

**AI & ML (`ai`)**
- [x] Fine-tuning vs RAG vs prompting — when to use which
- [x] LoRA / PEFT · Quantization (GGUF, bitsandbytes) · Tokenization internals
- [x] Running local LLMs — Ollama, llama.cpp, LM Studio
- [x] LLM evaluation & guardrails · Diffusion models (how image gen works)

**Data (`script`/`ai`)**
- [x] Apache Kafka (deep) · Spark · Airflow/Dagster · dbt
- [x] Dimensional modeling — star/snowflake schemas, slowly-changing dimensions

**Productivity (`shortcut`)**
- [x] VS Code · Vim (deep) · modern CLI tools (ripgrep, fzf, bat, jq, eza)
- [x] Git power-user — rebase, reflog, bisect, worktrees, aliases

**Study meta (any domain / a new `certs` section)**
- [x] Cert Roadmaps — CompTIA (A+→Net+→Sec+→CySA+→PenTest+→CASP), OSCP path,
      CISSP, and cloud tracks (AWS SAA/Security, GCP ACE/PCA) with study order.

---

## Suggested execution order (next waves)

| Phase | Waves | Theme | Rough size |
|-------|-------|-------|-----------|
| 15 | scaffolding | 3 new domains wired + verified | ~30 min |
| 16–18 | R1–R3, B1–B2, C1–C2 | Highest-demand: recon+web offense, NSM+SIEM, cloud foundations+IAM | ~30 cards |
| 19–22 | R4–R6, B3–B5, C3–C5 | AD attacks, C2, passwords; endpoint+detection+DFIR; cloud net/compute/storage | ~45 cards |
| 23–25 | R7–R9, B6–B8, C6–C8 | Wireless/hardware/cloud-offense; TI+hardening+deception; cloud security+IaC+observability | ~40 cards |
| 26+ | Track X + C9 | Languages, automation, AI/data depth, Azure bonus, cert roadmaps | open-ended |

**Conventions unchanged:** every new topic follows `CONTRIBUTING.md` (styled
`topic-chev`, `ref-table`, `.c-*` utility colors, `<pre class="code-block">` for
commands), inherits search/permalinks/progress/keyboard-a11y automatically, and
each wave ends with `python3 build.py` + a headless smoke check + a CI-green
commit. Red-team cards additionally carry an authorized-use reminder and a paired
Blue-team detection note.

---

# Content Roadmap — Architecture, Engineering & DevOps (Wave 27+)

> **Added on request:** deeper coverage for **software architecture &
> engineering roles**, **DevOps/platform engineering**, and a **VS Code**
> mastery set. Complements — doesn't duplicate — the existing conceptual
> topics (`Design Patterns`, `Refactoring & Clean Code`, `API Design`, `CI/CD`,
> `SRE`, `Service Mesh`, `Message Queues`, and the shallow `VS Code` card).
> ~65 planned topics across 3 tracks / 16 waves.

## Structural decision

- **TRACK E** → new domain **`eng` 🏛️ "Software Engineering & Architecture"**.
  Distinct from `script` (language-focused) and `ops` (run/operate). Home for
  system design, architecture styles, engineering craft, and the career/role
  ladder. Wire it like the domains in Wave 15 (domains.json + chip + `.c-eng` /
  `.domain-eng` colors + `data/eng.html`).
- **TRACK F** → **deepen the existing `ops` domain** (it already carries CI/CD,
  K8s, IaC, GitOps, SRE, Terraform, Chaos, Deployment Strategies — effectively
  the DevOps/SRE domain). No new domain needed.
- **TRACK G** → **deepen `shortcut`** (Shortcuts & Productivity; already holds a
  `VS Code` card). Replace/expand that card with a proper multi-topic set.

---

## TRACK E — Software Architecture & Engineering Craft  (→ `eng`)

6 waves, ~32 cards. Aimed at the architect / senior+ / staff-engineer path.

**Wave E1 — System Design Fundamentals**
- [x] Scalability 101 — vertical vs horizontal, stateless design, shared-nothing
- [x] Load Balancing & Sharding — strategies, consistent hashing, hot keys
- [x] Back-of-the-Envelope — latency numbers every engineer should know, capacity math
- [x] Designing for Failure — redundancy, graceful degradation, bulkheads, blast radius
- [x] The System Design Interview — a framework (requirements → estimate → API → data → scale → trade-offs)

**Wave E2 — Architecture Styles**
- [x] Monolith vs Microservices vs Modular Monolith — honest trade-offs
- [x] Event-Driven Architecture — deep (choreography vs orchestration; ties to Message Queues)
- [x] Clean / Hexagonal / Ports & Adapters — keeping business logic independent
- [x] CQRS & Event Sourcing — read/write split, the append-only log
- [x] The Twelve-Factor App — the checklist for cloud-native services
- [x] Cloud-Native & Serverless architecture patterns

**Wave E3 — Domain Modeling & Design**
- [x] Domain-Driven Design (DDD) — bounded contexts, ubiquitous language, aggregates
- [x] SOLID Principles — deep card with examples of each
- [x] Coupling & Cohesion — Law of Demeter, dependency direction
- [x] API-First & Contract-Driven design — OpenAPI, consumer-driven contracts
- [x] Schema & data modeling patterns — normalization trade-offs, polyglot persistence

**Wave E4 — Engineering Craft & Quality**
- [x] Clean Code & Naming — deep (functions, comments, structure)
- [x] Code Review — doing it well (giving + receiving; what to look for)
- [x] Testing Strategy — the test pyramid, unit/integration/e2e, TDD & BDD
- [x] Technical Debt — recognizing, quantifying, and paying it down deliberately
- [x] ADRs & Design Docs — Architecture Decision Records, RFCs, the C4 model

**Wave E5 — Reliability & Distributed Patterns**
- [x] Resilience Patterns — circuit breaker, retry + backoff + jitter, timeout, bulkhead
- [x] Idempotency & Exactly-Once — deep (ties to API Design + Message Queues)
- [x] Distributed Transactions — Saga, Outbox, 2PC and why 2PC is avoided
- [x] Backpressure & Flow Control — protecting systems under load
- [x] Consistency in practice — read-repair, quorums, tunable consistency (ties to CAP)

**Wave E6 — Engineering Career & Roles**
- [x] The Engineering Ladder — junior → mid → senior → staff → principal
- [x] Staff+ Archetypes — tech lead, architect, solver, right-hand
- [x] Tech Lead vs Engineering Manager — the fork in the road
- [x] Estimation & Planning — story points, velocity, why estimates are hard
- [x] Influence Without Authority — RFCs, stakeholder comms, driving alignment
- [x] Career Ladders & Interviews — leveling, system-design & coding interview prep

---

## TRACK F — DevOps & Platform Engineering  (→ deepen `ops`)

5 waves, ~25 cards. Deepens the tools already present as concept-topics.

**Wave F1 — DevOps Foundations & Culture**
- [x] What DevOps Actually Is — CALMS, breaking the dev/ops wall, you-build-it-you-run-it
- [x] The Three Ways — Flow, Feedback, Continual Learning (The Phoenix/DevOps Handbook)
- [x] DORA Metrics — deploy frequency, lead time, MTTR, change-failure rate
- [x] Value Stream Mapping — finding the bottleneck in delivery
- [x] Platform Engineering & the IDP — golden paths, self-service, the internal developer platform

**Wave F2 — CI/CD Pipelines Deep**
- [x] Pipeline Design — stages, quality gates, artifacts, promotion between envs
- [x] GitHub Actions — workflows, jobs, matrix builds, secrets, reusable/composite actions
- [x] Jenkins · GitLab CI · CircleCI — comparison & when to pick which
- [x] Branching Strategies — trunk-based vs GitHub Flow vs GitFlow (and why trunk wins at scale)
- [x] Progressive Delivery — feature flags + canary + blue-green wired into the pipeline

**Wave F3 — Containers & Kubernetes Deep**
- [x] Docker Deep — multi-stage builds, layer caching, image slimming, distroless
- [x] Kubernetes Objects — pods, deployments, services, ingress, configmaps/secrets
- [x] Helm & Kustomize — packaging and templating manifests
- [x] K8s Networking & Storage — CNI, CSI, ingress controllers, persistent volumes
- [x] K8s Security — RBAC, network policies, pod security standards, admission control

**Wave F4 — Config, Secrets & Supply Chain**
- [x] Configuration Management — Ansible deep (playbooks, roles, inventory), Chef/Puppet/Salt
- [x] Secrets Management — HashiCorp Vault, external-secrets, sealed secrets, dynamic creds
- [x] Software Supply Chain Security — SBOM, SLSA, Sigstore/cosign, provenance & signing
- [x] Policy as Code — OPA/Rego, Kyverno, Conftest guardrails in CI
- [x] Artifact & Registry Management — container/package registries, retention, promotion

**Wave F5 — Observability & Operations Deep**
- [x] Prometheus & Grafana — metrics model, PromQL, dashboards, Alertmanager
- [x] Golden Signals + RED / USE — what to actually measure
- [x] SLIs, SLOs & Error Budgets — deep (turning SRE theory into alert thresholds)
- [x] Structured Logging & Log Pipelines — correlation IDs, aggregation (ties to SIEM)
- [x] On-Call Done Humanely — rotations, escalation, runbooks, blameless postmortems

---

## TRACK G — Developer Environment & VS Code  (→ deepen `shortcut`)

3 waves, ~16 cards. Replaces the single shallow `VS Code` card.

**Wave G1 — VS Code Mastery**
- [x] VS Code Setup & Settings — settings.json, Settings Sync, Profiles per stack
- [x] Command Palette & Keybindings — the shortcuts that actually save time
- [x] Editing Superpowers — multi-cursor, column select, refactor, snippets, regex find/replace
- [x] Debugging — launch.json, breakpoints (conditional/logpoints), watch, call stack
- [x] Integrated Terminal, Tasks & the Source Control panel
- [x] Essential Extensions — per-language + productivity (and how to stay lean)

**Wave G2 — Remote & Containerized Dev**
- [x] Remote Development — Remote-SSH, WSL, and how the client/server split works
- [x] Dev Containers — devcontainer.json, reproducible per-project toolchains
- [x] GitHub Codespaces & cloud dev environments
- [x] Live Share — real-time collaborative editing & debugging

**Wave G3 — The Modern Dev Environment**
- [x] Dotfiles & Config Management — chezmoi/stow, version-controlled setup
- [x] Shell & Terminal Setup — zsh/fish, starship prompt, tmux (ties to existing tmux card)
- [x] Runtime & Version Managers — asdf/mise, nvm, pyenv, direnv per-project
- [x] AI Pair Programming — Copilot, Cursor, Claude Code — using them well without over-trusting

---

## Suggested execution order (Wave 27+)

| Phase | Waves | Theme | Rough size |
|-------|-------|-------|-----------|
| 27 | scaffold `eng` + G1 | new Engineering domain wired; VS Code mastery set | ~7 cards |
| 28–30 | E1–E3, F1–F2 | system design + architecture styles + domain modeling; DevOps culture + CI/CD | ~28 cards |
| 31–33 | E4–E6, F3–F4, G2 | craft/quality + reliability + career; containers/K8s + supply chain; remote dev | ~30 cards |
| 34 | F5, G3 | observability/on-call deep; modern dev environment | ~9 cards |

Conventions unchanged: `CONTRIBUTING.md` skeleton, `python3 build.py` + headless
smoke check + CI-green commit per wave; each topic inherits search / permalinks /
progress / keyboard-a11y automatically.

---

# Content Roadmap — Phase 3: Depth, Breadth & New Domains (Wave 35+)

> **Added on request — "a big plan."** The Phase-2 roadmap (Tracks R/B/C/E/F/G/X)
> is fully shipped: **660 topics across 16 domains**, zero console errors. This
> phase is the ambitious follow-on — it **adds new domains** where the site is
> thin, and **deepens every existing domain** with the next layer of material.
> Ordered roughly by value; interleave freely. Each wave stays ~4–6 cards, follows
> `CONTRIBUTING.md`, and ships as one CI-green commit (`build.py` + headless smoke
> check). Offensive cards keep the authorized-use + paired-detection framing.

## Structural decisions

- **New domain `data` 📊 "Data & Databases"** — SQL/DB material is currently
  scattered across `script`/`ai`/`ops`. Give it a home: query mastery, database
  internals, NoSQL, warehousing, and the DBA/analytics-engineer path. Wire like
  Wave 15 (domains.json + chip + `.c-data`/`.domain-data` colors + `data/data.html`).
- **New domain `web` 🌐 "Web & Frontend Engineering"** — the site has only
  beginner HTML/CSS/JS. Modern frontend is a huge career surface: frameworks,
  the browser platform, performance, accessibility, and full-stack patterns.
- **Optional new domain `product` 🧭 "Product, Agile & Ways of Working"** — only
  if it grows past ~8 cards; otherwise fold into `eng`/`lifestyle`. Kept as a
  stretch goal at the end.
- **Everything else = new waves inside existing domains.** No new scaffolding.

---

## TRACK H — Data & Databases  (→ new `data` domain)

~8 waves, ~45 cards. The DBA / data-analyst / analytics-engineer companion.

**Wave H1 — Relational Foundations**
- [x] How a Database Works — pages, buffer pool, WAL, the storage engine
- [x] The Relational Model — relations, keys, referential integrity, NULL semantics
- [x] Normalization Deep — 1NF→BCNF with worked examples; when to denormalize
- [x] ACID & Transactions — atomicity, isolation levels, the anomalies each prevents
- [x] ER Modeling — entities, relationships, cardinality, crow's-foot diagrams

**Wave H2 — SQL Mastery**
- [x] SQL Joins Deep — inner/outer/self/cross, and how NULLs break naive joins
- [x] Window Functions — ranking, running totals, LAG/LEAD, partitions
- [x] CTEs & Recursion — readable queries, hierarchical/graph traversal
- [x] Aggregation & GROUP BY — HAVING, GROUPING SETS, ROLLUP/CUBE
- [x] Subqueries, EXISTS & Set Ops — correlated subqueries, UNION/INTERSECT/EXCEPT

**Wave H3 — Performance & Internals**
- [x] Indexes Explained — B-tree vs hash vs GIN/GiST, covering & composite indexes
- [x] Reading EXPLAIN / Query Plans — seq scan vs index scan, join strategies
- [x] Query Optimization — sargability, cardinality, the N+1 problem, statistics
- [x] Locking & MVCC — how Postgres/InnoDB avoid readers blocking writers
- [x] Partitioning & Sharding — scaling a single table/database horizontally

**Wave H4 — Postgres in Practice**
- [x] PostgreSQL Deep — psql, roles, schemas, extensions (the "default" DB)
- [x] Postgres Power Features — JSONB, arrays, full-text search, LISTEN/NOTIFY
- [x] MySQL / MariaDB — engine differences, gotchas, when it's chosen
- [x] SQLite — the embedded database that's everywhere (and its sweet spot)
- [x] Connection Pooling & PgBouncer — surviving many clients

**Wave H5 — NoSQL & Beyond**
- [x] NoSQL Landscape — document / key-value / wide-column / graph, CAP trade-offs
- [x] MongoDB — documents, aggregation pipeline, indexing, schema design
- [x] Redis — data structures, caching patterns, pub/sub, persistence, Lua
- [x] Cassandra / DynamoDB — wide-column, partition keys, single-table design
- [x] Graph Databases — Neo4j, Cypher, when relationships are the data

**Wave H6 — Analytics & Warehousing**
- [x] OLTP vs OLAP — row vs columnar storage, why analytics needs a warehouse
- [x] Columnar Engines — Parquet, DuckDB, ClickHouse; vectorized execution
- [x] Data Warehouse vs Lake vs Lakehouse — Snowflake/BigQuery/Databricks
- [x] The Semantic Layer & Metrics — one definition of "revenue" everywhere
- [x] Data Quality & Observability — tests, freshness, lineage, contracts

**Wave H7 — Operating Databases**
- [x] Backups & PITR — dumps vs physical, point-in-time recovery, testing restores
- [x] Replication & HA — primary/replica, failover, read scaling, split-brain
- [x] Migrations & Schema Change — zero-downtime, expand/contract, Flyway/Liquibase
- [x] Database Security — least privilege, row-level security, encryption, auditing
- [x] Monitoring a DB — slow-query logs, bloat, connection saturation, key metrics

**Wave H8 — Data Career & Modeling Craft**
- [x] Data Roles — analyst vs analytics engineer vs data engineer vs DBA vs scientist
- [x] Designing a Schema From Requirements — a walkthrough, OLTP → OLAP
- [x] Time-Series & Event Data — retention, downsampling, TimescaleDB/InfluxDB
- [x] Vector Databases — embeddings, ANN search, pgvector (bridge to AI domain)
- [x] The Data Interview — SQL problems, modeling questions, case studies

---

## TRACK I — Web & Frontend Engineering  (→ new `web` domain)

~7 waves, ~38 cards. From "I know some HTML" to shipping modern web apps.

**Wave I1 — The Browser Platform**
- [x] How the Browser Renders — parse → DOM/CSSOM → layout → paint → composite
- [x] The Critical Rendering Path & Reflow/Repaint — what makes pages jank
- [x] The DOM & Events — bubbling/capture, delegation, the event loop revisited
- [x] Web Storage & State — cookies vs localStorage vs IndexedDB vs cache
- [x] DevTools Mastery — elements, network, performance, memory, Lighthouse

**Wave I2 — Modern CSS**
- [x] Flexbox — the one-dimensional layout system, deep
- [x] CSS Grid — two-dimensional layout, template areas, auto-fit/minmax
- [x] Responsive Design — media/container queries, fluid type, mobile-first
- [x] Modern CSS — custom properties, nesting, :has(), cascade layers, clamp()
- [x] Design Systems & Tokens — Tailwind, CSS-in-JS, BEM, component styling

**Wave I3 — JavaScript Deep (beyond the basics)**
- [x] Closures, Scope & the `this` Keyword — the interview favorites, clearly
- [x] Async Deep — promises, async/await, microtasks vs macrotasks, the event loop
- [x] Prototypes & Modern Classes — inheritance, the prototype chain
- [x] Modules & Bundlers — ESM, tree-shaking, Vite/esbuild/webpack
- [x] TypeScript — types, generics, narrowing, why teams adopt it

**Wave I4 — Frameworks**
- [x] React — components, hooks, state, reconciliation, the mental model
- [x] React Patterns — context, memoization, data fetching, common pitfalls
- [x] Vue & Svelte — reactivity models compared to React
- [x] Meta-Frameworks — Next.js/Nuxt/SvelteKit, SSR vs SSG vs ISR vs CSR
- [x] State Management — when you need Redux/Zustand/signals (and when you don't)

**Wave I5 — Talking to Backends**
- [x] Fetch, REST & the Network — status codes, CORS, caching headers in practice
- [x] GraphQL — schema, queries/mutations, over/under-fetching, when to use it
- [x] WebSockets & Realtime — SSE, polling, when each fits
- [x] Auth on the Frontend — tokens vs cookies, OAuth flows, secure storage
- [x] API Client Patterns — React Query/SWR, caching, optimistic updates

**Wave I6 — Quality, Performance & A11y**
- [x] Web Performance — Core Web Vitals (LCP/INP/CLS), code-splitting, lazy loading
- [x] Web Accessibility (a11y) — WCAG, ARIA, keyboard nav, screen readers
- [x] Frontend Testing — unit (Vitest), component (Testing Library), e2e (Playwright)
- [x] Web Security for Frontend — XSS, CSRF, CSP, clickjacking (bridge to `sec`)
- [x] SEO & Metadata — semantic HTML, Open Graph, structured data

**Wave I7 — Shipping & The Edge**
- [x] Progressive Web Apps — service workers, offline, installability
- [x] Rendering at the Edge — CDNs, edge functions, image optimization
- [x] Web Assembly — what it is, when to reach for it
- [x] Frontend Build & Deploy — CI, preview deploys, Netlify/Vercel/Pages
- [x] The Full-Stack Picture — how frontend, API, and DB fit together end-to-end

---

## TRACK J — Applied Security Depth  (→ `sec`)

~5 waves, ~28 cards. Beyond fundamentals — the working security engineer's kit.

> **Session 19: site check run before writing. Wave J1 shipped 3 of 5.** `sec` already
> holds two OWASP Top 10 cards and a Threat Modeling card, so those two were cut `- [~]`.
>
> **On the "sec duplicates itself worse than script" claim — I overstated it, and the
> correction is the same one the previous session needed.** Counting titles gave three
> Zero Trust cards and two OWASP cards. Applying this file's own tiering rule:
>
> - The **Beginner**-badged Zero Trust and OWASP cards are a deliberate tier, exactly like
>   `script`'s *Lists & Key/Value*. Not duplicates. Kept.
> - Of the two architecture-tier Zero Trust cards, one was a **pillars reference**
>   (Identity · Device · Network · Data · Workload · Visibility) and one was prose. They
>   overlapped only on the tenets.
>
> **So: one merge, not five cards of cleanup.** The pillars block was lifted into the
> prose card and the thin topic removed, with a slug alias. `sec` 3 → 2 Zero Trust cards.
>
> Twice now a "this domain duplicates itself" claim has shrunk on inspection — five cards
> to one in `script`, five to one here. **Counting titles overcounts duplication, because
> a tier and a redundancy look identical from the index.** Read the badges before
> believing the count.
>
> **Waves J2–J5 then checked properly, all 20 cards at once: 16 already covered, 4 gaps.**
> An 80% duplicate rate — far above the ~15% seen in Tracks V and AL, and the clearest
> demonstration yet of the stale-track problem. `sec` is the site's oldest large domain,
> so a track written against the *subject* of applied security was always going to
> collide with it.
>
> Written: **Post-Quantum Cryptography**, **Data Loss Prevention**, **Network Security
> Architecture**, **Privileged Access Management**. Everything else in J2–J5 is marked
> `- [~]`.
>
> **Track J total: 7 written of 25 specced.** One caveat recorded honestly — several
> "COVERED" matches are fundamentals cards where the track specced a *Deep* version
> (*Encryption Fundamentals* against *Symmetric Crypto Deep — AES modes, nonces, AEAD*).
> Those may justify a depth card later, the way `cs` earned its place above `script`. That
> needs the existing cards read rather than their titles matched, and is not a
> title-check decision.

**Wave J1 — Application Security**
- [~] OWASP Top 10 Deep — one card walking every category with fixes
- [x] Injection Family — SQLi, command, LDAP, template, NoSQL injection
- [x] Broken Access Control — IDOR, path traversal, privilege escalation in apps
- [x] SSRF, XXE & Deserialization — the server-side heavy hitters
- [~] Secure SDLC & Threat Modeling — STRIDE, abuse cases, security gates

**Wave J2 — API & Cloud-Native Security**
- [~] API Security — OWASP API Top 10, BOLA, rate limiting, API gateways
- [~] OAuth/OIDC Security Deep — PKCE, token types, common flow mistakes
- [~] Container Security Deep — image scanning, runtime, capabilities, seccomp
- [~] Kubernetes Security Deep — pod security, admission control, RBAC pitfalls
- [~] DevSecOps — shifting left, SAST/DAST/SCA in CI, policy gates

**Wave J3 — Cryptography Engineering**
- [~] Symmetric Crypto Deep — AES modes (GCM/CBC/CTR), nonces, AEAD
- [~] Asymmetric & Key Exchange — RSA vs ECC, Diffie-Hellman, forward secrecy
- [~] Hashing & Password Storage — bcrypt/scrypt/Argon2, salts, HMAC
- [~] Crypto in Practice — what to use (libsodium), what never to roll yourself
- [x] Post-Quantum Cryptography — why it matters, ML-KEM/ML-DSA, the migration

**Wave J4 — Detection & Defensive Engineering**
- [x] Data Loss Prevention (DLP) — classification, egress controls, insider risk
- [x] Network Security Architecture — segmentation, microseg, DMZ, egress filtering
- [~] Web App Firewalls & RASP — where they help and where they don't
- [~] Secrets & Key Management Deep — HSMs, KMS envelope encryption, rotation
- [~] Security Logging Strategy — what to log, retention, the audit trail

**Wave J5 — Identity & Modern Auth**
- [~] Modern IAM Architecture — IdP, SSO, SCIM provisioning, lifecycle
- [~] Zero Trust Implementation — beyond the buzzword: policy, device trust, ZTNA
- [x] Privileged Access Management (PAM) — vaulting, JIT access, session recording
- [~] Federation Deep — SAML vs OIDC assertions, trust chains, common attacks
- [~] Passwordless & Passkeys Deep — FIDO2/WebAuthn ceremony, attestation

---

## TRACK K — Threat, Malware & Intel Depth  (→ `threat`)

~4 waves, ~22 cards.

**COMPLETE — 22 of 22, six cards written and sixteen already built.** `threat` had
23 cards and the neighbours had more: forensics lives in `blueteam` (Volatility,
Autopsy, Windows artifacts) and `ops`, the defender's supply-chain view in `devops`
and `sec`, STRIDE in `sec`. The site check found the same thing Track V and Track AL
found — the list was written against the subject, not the site. `threat` is now 29.

**Wave K1 — Malware Analysis**
- [x] Static Analysis → *Malware Analysis — Understanding What the Bad Code Does* + `sec`'s *Malware Analysis – Static & Dynamic Analysis Fundamentals*
- [x] Dynamic Analysis → same two cards
- [x] Reverse Engineering Basics → *Reverse Engineering & Binary Analysis — Reading Code You Don't Have Source For*
- [x] Malware Families → *Malware Types Reference*
- [x] Anti-Analysis Techniques → *Anti-Analysis Techniques — How Malware Hides, and How Analysts Win Anyway*

**Wave K2 — Adversary Knowledge**
- [x] APT Case Studies → *Threat Actors — Know Your Adversary* (named-campaign detail deliberately not duplicated; it is the fastest-rotting content on the site)
- [x] Ransomware Deep → *Ransomware — The Defining Threat of the Era* + the Beginner-tier *Ransomware – How It Spreads*
- [x] Initial Access Brokers & the Criminal Economy → *The Criminal Economy — Access Brokers, Affiliates & How Breaches Get Sold*
- [x] Supply-Chain Attacks → *Supply-Chain Attacks — Compromise One, Reach Thousands* (attacker lens; the defender lens is `devops`/`sec`)
- [x] Living-off-the-Land at Scale → covered in `threat` and `redteam`

**Wave K3 — Frameworks & Modeling**
- [x] MITRE ATT&CK Deep → *MITRE ATT&CK Framework* + `blueteam`'s *MITRE ATT&CK & Navigator*
- [x] MITRE D3FEND & Engage → *MITRE D3FEND & Engage — Mapping Defenses and Deception to ATT&CK*
- [x] The Diamond Model → *Diamond Model of Intrusion Analysis*
- [x] Threat Modeling Methodologies → *Threat Modeling Methodologies — STRIDE vs PASTA vs Attack Trees*
- [x] Cyber Threat Intel Programs → *Threat Intelligence Lifecycle* + *Threat Intelligence — Turning Data Into Decisions*

**Wave K4 — Incident Response Deep**
- [x] The IR Lifecycle → `ops` and `blueteam` incident-response cards
- [x] Containment Strategies → same
- [x] Forensic Acquisition → *Digital Forensics* + `ops`'s *Digital Forensics Process* + `blueteam`'s Volatility card
- [x] Timeline Reconstruction → `blueteam` super-timeline material
- [x] Tabletop Exercises & Postmortems → `grc`, `ops` and `military` all carry it

---

## TRACK L — GRC, Compliance & Risk Depth  (→ `grc`)

~4 waves, ~22 cards. The framework-by-framework reference practitioners actually need.

**COMPLETE — 22 of 22, seven cards written and fifteen already built.** `grc` had 27
cards, but the big frameworks were one table row each inside *Compliance Frameworks —
Playing by the Rules*. That is the pattern worth naming for the remaining tracks: a
framework's **name** appearing on the site is not the same as the site **covering** it,
and a grep for the name says the wrong thing. `grc` is now 34.

**Wave L1 — The Big Frameworks**
- [x] ISO/IEC 27001 & 27002 → *ISO/IEC 27001 & 27002 — The ISMS, Annex A and Certification*
- [x] SOC 2 → *SOC 2 – Trust Service Criteria* + *Reading a SOC 2 Report Without Falling Asleep*
- [x] PCI-DSS → *PCI DSS — The 12 Requirements, Scope Reduction & SAQ vs ROC*
- [x] HIPAA → *HIPAA — Privacy Rule, Security Rule & Breach Notification*
- [x] FedRAMP & NIST 800-53 → *FedRAMP & NIST 800-53 — Control Baselines and the ATO*

**Wave L2 — Risk & Assurance**
- [x] Quantitative Risk → *Risk Management 101* already carries SLE/ARO/ALE and inherent vs residual (FAIR is named but thin — a known soft spot, not worth a card alone)
- [x] Risk Treatment → *Risk Management Lifecycle* + *Risk Management 101*
- [x] The Controls Universe → *The Controls Universe — Types, Functions & Mapping Once to Many*
- [x] Internal Audit Deep → *The Audit Process* + *Audit Prep* + *The Three Lines of Defense*
- [x] Metrics & Reporting to the Board → covered across the audit and maturity material

**Wave L3 — Privacy & Governance**
- [x] GDPR Deep → *Privacy Regulations — GDPR* + *Privacy Law – GDPR*
- [x] US Privacy Patchwork → CCPA/CPRA covered in the privacy cards
- [x] Privacy Engineering → *Data Privacy Techniques — Anonymization & Differential Privacy*
- [x] Data Governance → *Data Governance, Retention & eDiscovery — Owning Data on Purpose*
- [x] Records & eDiscovery → same card

**Wave L4 — Third-Party & Resilience**
- [x] Vendor Risk Management → *Vendor Risk Management – Securing the Supply Chain* + *Vendor Risk Assessments*
- [x] Business Continuity Deep → *Business Continuity & Disaster Recovery* + *BCP*
- [x] Supply-Chain Risk (GRC lens) → `devops`'s *Software Supply Chain Security* + the vendor-risk cards
- [x] Security Program Building → *Frameworks Without the Jargon* + *Security Awareness* + *Change Management*
- [x] Regulatory Landscape → *The Regulatory Landscape — DORA, NIS2 & Cyber Disclosure Rules*

---

## TRACK M — Offensive Security Depth  (→ `pentest` / `redteam`)

~4 waves, ~22 cards. Authorized-testing framing throughout, paired detections noted.

**COMPLETE by existing coverage — no cards written.** This is the track the site was
already deepest on: `redteam` (43 cards) and `pentest` (29) are the two most-built
security domains, and between them they cover the whole spec, usually
tool-by-tool with the exact named tools the spec asks for. Writing anything here would
be the "second introduction" the method warns against. One genuine thin spot recorded
below rather than papered over.

**Wave M1 — Web & API Exploitation**
- [x] Burp Suite Pro Workflow → `redteam` *Burp Suite — The Web Pentest Workbench*
- [x] Auth & Session Attacks → JWT/OAuth in `sec`, `web`, `script`; attack lens in `pentest`
- [x] Business-Logic Flaws → `pentest` and `sec` web-app cards
- [x] API Pentesting → mass assignment / IDOR in `pentest` (*Finding Your First IDOR*) and `sec`
- [~] Client-Side — DOM XSS, prototype pollution, postMessage, CORS. **Genuine gap:**
  prototype pollution and postMessage are nowhere; DOM XSS/CORS are in `web`'s
  frontend-security card. This is `web`/Track I depth, not offensive tooling — left for
  a Track I follow-up rather than forced into `redteam`.

**Wave M2 — Active Directory Attack Paths**
- [x] AD Enumeration → `redteam` *BloodHound & SharpHound*, *Impacket*
- [x] Kerberos Deep → `redteam` *Kerberos Attacks — Rubeus & Kerbrute*
- [x] ADCS Attack Paths → `redteam` *ADCS Abuse — Certipy & the ESC Techniques*
- [x] Lateral Movement → `redteam` *Responder & NTLM Relay*, *Living off the Land*
- [x] Domain Persistence → *Mimikatz*, DCSync in `redteam`/`blueteam`/`sec`

**Wave M3 — Cloud & Container Offense**
- [x] Cloud Pentest Methodology → `redteam` *Pacu*, *CloudFox & enumerate-iam*
- [x] IAM Privilege Escalation → *CloudFox*, *Cloud Credential Attacks & the Purple-Team Bridge*
- [x] Serverless & CI/CD Attacks → cloud-credential and purple-team cards (poisoned-pipeline depth is thin — `devops` territory)
- [x] Container Escape → `redteam` *Kubernetes Attacks — RBAC Abuse & Container Escape*
- [x] Kubernetes Attack Paths → same card

**Wave M4 — Tradecraft & Professionalism**
- [x] Report Writing → `pentest` *Pentest Reporting — The Skill That Makes or Breaks Your Career*
- [x] Scoping & Rules of Engagement → `pentest` *Scoping & Rules of Engagement* + `redteam` *Rules of Engagement — Read This First*
- [x] OPSEC for Testers → covered across the RoE and C2 cards
- [x] Purple-Team Playbooks → `redteam` *Cloud Credential Attacks & the Purple-Team Bridge*
- [x] The OSCP/Cert Path → OSCP prep in `career`, `pentest`, `redteam`, `eng`

---

## TRACK N — Linux & Systems Depth  (→ `linux`)

~3 waves, ~16 cards.

**COMPLETE — 2 cards written, 14 already built.** `linux` was already the largest
domain on the site at 56 cards, and it covered all of N1–N3 except two genuine gaps in
the integrity/imaging area. `linux` is now 58.

**Wave N1 — Linux Security Hardening**
- [x] SELinux & AppArmor → *SELinux & AppArmor — Mandatory Access Control*
- [x] Capabilities & Namespaces → *Under the Hood — Namespaces & cgroups* + *Container Internals*
- [x] auditd & Hardening → *Shell, Cron & Hardening* + auditd in `sec`/`blueteam`
- [x] Firewalling → *Linux Firewalls — iptables, nftables & ufw*
- [x] Secure Boot, LUKS & Integrity → *Secure Boot, LUKS & Integrity — Measured Boot, dm-verity & IMA* (written — LUKS/Secure Boot were only in `sec`/`eng`/`military`, none of it on `linux` and none of it covering measured boot or runtime integrity)

**Wave N2 — Performance & Troubleshooting**
- [x] The USE Method → *Performance Debugging — When You Need to Go Deeper* + `ops`
- [x] CPU & Memory Tools → same, plus *"The Disk Is Full"* and process cards
- [x] Disk & I/O → *Storage Management — Disks, Partitions, LVM & RAID*
- [x] Network Debugging → *The ip Command — Modern Linux Networking* + performance card
- [x] eBPF & Modern Observability → *eBPF — Programmable Kernel Observability & Security*

**Wave N3 — Storage & Ops**
- [x] LVM Deep → *LVM & Storage – Flexible Disk Management* + *Storage Management*
- [x] Software RAID & mdadm → *RAID Levels Reference* + *Storage Management*
- [x] NFS/Samba → *NFS & Samba – Sharing Files Across the Network*
- [x] Package & Image Building → *Package & Image Building — From rpm/deb to Immutable Linux* (written — package install existed, but building packages and image-based/immutable OSes were nowhere)
- [x] Systemd Advanced → *systemd Deep — Units, Timers & Journald*

---

## TRACK O — AI Engineering Depth  (→ `ai`)

~4 waves, ~22 cards. From "I use ChatGPT" to building reliable AI systems.

**COMPLETE — 22 of 22, ten cards written and fourteen already built.**

**Checked against the site before writing, and most of this track was already
built.** `ai` had 34 cards when the wave started; fourteen of the twenty-two specced
items already had one. Every item below is marked with the card that fills it, so the
next session does not re-derive the list. `ai` is now 44 cards.

The framework card is the one to re-read first when this ages: the category table
(who owns the loop, who owns the hosting) is durable, the product names under it are
marked volatile on purpose.

**Wave O1 — How Models Actually Work**
- [x] Neural Networks From Zero → *Neural Networks & Deep Learning*
- [x] The Transformer → *The Transformer — Attention and Why It Changed Everything*
- [x] Training Pipeline → *Training Pipeline — Pretraining, SFT, RLHF & DPO*
- [x] Inference Internals → *Inference Internals — KV Cache, Context Windows & Sampling*
- [x] Classic ML Still Matters → *ML Foundations* + *Machine Learning Fundamentals*

**Wave O2 — Building With LLMs**
- [x] Prompt Engineering Deep → *Prompt Engineering — Getting Better Answers from AI*
- [x] RAG Architecture → *Embeddings & RAG*
- [x] Vector Search Deep → *Vector Databases — Similarity Search at Scale*
- [x] Function Calling & Tools → *Function Calling & Tools — Letting a Model Act*
- [x] Structured Output & Validation → *Structured Output & Validation — Getting JSON You Can Trust*

**Wave O3 — Agents & Orchestration**
- [x] AI Agents → *Agentic AI & Orchestration*
- [x] Model Context Protocol (MCP) → *Model Context Protocol (MCP) — USB-C for AI*
- [x] Multi-Agent Systems → *Multi-Agent Systems — Orchestration, Hand-offs & the Coordination Cost*
- [x] Agent Frameworks → *Agent Frameworks — What They Give You and What They Cost*
- [x] Agent Safety & Sandboxing → *Agent Safety & Sandboxing — Permissions, Blast Radius & Human-in-the-Loop*

**Wave O4 — Production AI (LLMOps)**
- [x] Evaluation Deep → *LLM Evaluation, Guardrails & Diffusion Models*
- [x] Cost & Latency Optimization → *Cost & Latency Optimization — Caching, Batching & Model Tiering*
- [x] AI Security → *AI Security — Attacking and Defending AI Systems*
- [x] Observability for AI → *Observability for AI — Tracing, Token Accounting & Quality Monitoring*
- [x] Responsible AI → *AI Ethics* + *AI Governance & Frameworks*

**`ai` also self-duplicates and this track did not cause it.** Four pairs, all
predating the wave: *Fine-Tuning vs RAG vs Prompting* / *Fine-Tuning vs. Prompting vs.
RAG*; *ML Pipeline – From Raw Data* / *Machine Learning Pipeline*; *ML Foundations* /
*Machine Learning Fundamentals*; and two AI Ethics cards. Some of these are the
deliberate Beginner tier — apply the tiering rule from Track J before merging any of
them, which is what turned a claimed five `sec` duplicates into one real merge.

---

## TRACK P — Languages & Programming Depth  (→ `script`)

~3 waves, ~18 cards.

**COMPLETE — 2 cards written, the rest already built.** `script` is the biggest domain
on the site at 136 cards, and it already carried Rust, Java, C#/.NET, Ruby, PHP, C,
Assembly, Go, TypeScript and Python plus the entire craft and tooling spec. The only
real gap was the languages in P1 that had no card at all. Two consolidated cards fill
it; a single card per obscure language would have been thin. `script` is now 138.

**Wave P1 — More Languages**
- [x] Kotlin / Swift / Scala → *Kotlin, Swift & Scala — Modern Typed Application Languages*
- [x] Elixir/Erlang / Haskell / Lua·R·MATLAB → *Elixir, Haskell & the Functional / Niche Languages*
  (six specced language cards consolidated into two — the shared ideas are the point, and one card each would repeat null-safety and immutability five times)

**Wave P2 — Programming Craft**
- [x] Functional Programming → *Programming Paradigms (Gently)* + the new functional-languages card
- [x] Concurrency & Parallelism → *Concurrency — Doing More Than One Thing at Once* + *Python Async/Await*
- [x] Memory Management → `cs`'s *Garbage Collection — Generational Collectors, Pauses & Tuning* + Rust ownership in *Rust — Safe Systems Programming*
- [x] Error Handling Patterns → *Exception Handling* + *Handling Errors Gracefully*
- [x] Testing Deep → *Testing With pytest*, *Testing Strategy*, *Mocking*

**Wave P3 — Tools & Practices**
- [x] Debugging Like a Pro → *Debugging — Finding Out Why Your Code Lies to You*
- [x] Build Systems & Package Managers → *Semantic Versioning & Dependency Management* + *Reproducible Python Environments*
- [x] Regular Expressions Deep → multiple regex cards including *A Survival Guide for IT Tasks*
- [x] API Design Deep → *API Design — Versioning, Pagination, Rate Limits & Idempotency*
- [x] Code Architecture → *SOLID Principles* + *Design Patterns* + *Refactoring & Clean Code*

---

## TRACK Q — Networking Depth  (→ `net`)

~3 waves, ~16 cards.

**COMPLETE by existing coverage — no cards written.** `net` (55 cards) already carries
the whole spec at study-reference depth, dedicated card by dedicated card. The one
item that looked like a gap — OSPF & EIGRP — is covered inside *Routing Protocols — How
Routers Find the Best Path*, which lays out RIP/OSPF/EIGRP with the distance-vector vs
link-state distinction and Dijkstra cost. Verified card-by-card, not by grep.

**Wave Q1 — Routing & Switching Deep**
- [x] BGP → *BGP — How the Internet Routes Between Networks*
- [x] OSPF & EIGRP → *Routing Protocols — How Routers Find the Best Path* (link-state/distance-vector, Dijkstra) + *Routing Protocols & WAN Technologies*
- [x] IPv6 Deep → *IPv6 — The Internet's Upgrade*
- [x] VLANs, STP & Trunking → *Switching & VLANs* + *WAN & Switching Deep — SD-WAN, MPLS, VLANs & PoE* (STP/root bridge in both)
- [x] QoS → *QoS — Quality of Service & Traffic Shaping*

**Wave Q2 — Network Services & Security**
- [x] DHCP & DNS Internals → *DNS Deep Dive — Records, Resolution & Security* + *DHCP* + *DNSSEC & Encrypted DNS*
- [x] VPN Deep → *VPNs & Tunneling* + *VPNs Explained*
- [x] Load Balancing & Proxies → *Load Balancers & High Availability* + *Reverse Proxies — nginx, HAProxy*
- [x] Network Access Control → *802.1X & NAC — Who Gets On the Network?*
- [x] Wireless Deep → *Wireless Networking — 802.11 Standards & Security* + *Wireless Security*

**Wave Q3 — Modern & Cloud Networking**
- [x] SASE & SD-WAN Deep → *WAN & Switching Deep — SD-WAN, MPLS, VLANs & PoE*
- [x] Cloud Networking Patterns → *Cloud Networking — VPC, Subnets & CDNs* + *Cloud Networking – VPC, Subnets & Security Groups*
- [x] Network Troubleshooting → *Network Troubleshooting — A Systematic Approach* + *Packet Analysis*
- [x] Observability for Networks → *Network Monitoring — Seeing What Flows Through*
- [x] eBPF & Cilium Networking → covered in `devops` and `linux` (*eBPF — Programmable Kernel Observability*); it is a datapath/platform topic, defensibly not in `net`

---

## TRACK S — Career, Mind & Life Depth  (→ `lifestyle`)

~4 waves, ~22 cards. The non-technical skills that decide careers.

**COMPLETE — 1 card written; the rest already live in the `career` / `productivity` /
`mind` trio.** This track was speced against a `lifestyle` domain that was never
created, and deliberately not: the site's Growth group (`career`, `productivity`,
`mind`) already *is* the lifestyle domain, split three ways, and the chip bar is a
crowded single row of 28 — a fourth Growth domain would be redundant and cost budget.
So Track S is satisfied where its content already lives, with one genuine gap filled.

**Wave S1 — Health for Knowledge Workers**
- [x] Sleep → `productivity` *Sleep — Where the Studying Actually Sticks*
- [x] Nutrition Basics → *Fuel & Focus — Nutrition for a Desk-Bound Brain* (written — nutrition was the one item with zero coverage anywhere on the site)
- [x] Movement & Ergonomics → `mind` *Desk Body — Eyes, Wrists, Back & the Dose Problem*
- [x] Stress & the Nervous System → `mind` *Burnout — Recognizing It Before It Breaks You* + *Resilience & Perspective*
- [x] Focus & Attention → `productivity` *Attention — Task Switching, Residue & the Cost of Interruption*

**Wave S2 — Productivity Systems**
- [x] GTD → `productivity` *Time Management* + *Habits & Time*
- [x] PARA & PKM → `productivity` *Note-Taking for Learning* + *The Memory Palace*
- [x] Time Blocking & Prioritization → `productivity` *Time Management — Making Your Hours Count*
- [x] Goal Systems → `productivity` *Habits & Time* + *The Japanese Mastery Loop* (Kaizen)
- [x] Learning Systems → `productivity` *Learning How to Learn* + *Study Systems That Survive a Brain That Won't Cooperate*

**Wave S3 — Money & Independence**
- [x] Personal Finance / Investing / FI → `career` *Financial Basics for IT Workers* + *Money & Adulting Basics* (FI math is a thin spot — a candidate for a future `career` card, not a new domain)
- [x] Comp & Equity → `career` *Negotiating Your First IT Offer*
- [x] Taxes & Freelancing → covered in the financial-basics cards (freelance-entity depth is thin)

**Wave S4 — People Skills**
- [x] Negotiation → `career` *Negotiating Your First IT Offer* + `military` red-teaming/BATNA-adjacent
- [x] Feedback / Managing Up / Conflict → `career` *Soft Skills* + *Clear Technical Communication* + `mind` *Communication & Relationships*
- [x] Public Speaking & Presenting → `career` *Clear Technical Communication* + *Technical Writing*

---

## TRACK T — Military, Leadership & Decision-Making Depth  (→ `military`)

~3 waves, ~17 cards. Frameworks that transfer directly to tech leadership & IR,
plus the classified-information handling an IT professional on a cleared
contract is expected to know on day one.

**Wave T1 — Planning & Operations** — 2 written, 3 already built
- [x] MDMP → *MDMP & the OPORD — The Planning Cycle and the Five-Paragraph Order*
- [x] Intelligence Cycle → *The Intelligence Cycle — Direction, Collection, Processing, Dissemination*
- [x] Mission Orders & OPORD → folded into the MDMP card (the OPORD is MDMP's output; a separate card would repeat it)
- [x] Logistics & Sustainment → covered as OPORD paragraph 4 + `ops`/`grc` continuity material (a standalone card would be thin)
- [x] Risk Management (Military) → *PACE Planning* + `grc`'s risk cards cover the deliberate-risk process

**Wave T2 — Leadership Under Pressure** — complete by existing coverage
- [x] Mission Command Deep → *Leadership — Styles, Mission Command & Cohesion* + *Commander's Intent*
- [x] Crisis Leadership → *OODA Loop* + `mind`'s *Surviving On-Call* (decision-making with incomplete info)
- [x] Building Cohesive Teams → *Leadership — Styles, Mission Command & Cohesion*
- [x] Red Teaming as a Discipline → *Red Teaming as a Discipline — Premortems & Structured Contrarian Thinking*
- [x] Small-Unit Leadership for Tech Leads → *Leadership – Military Principles Applied to IT Teams*

**Track T complete: 3 cards written (MDMP/OPORD, Intelligence Cycle, Red Teaming),
T3 was already shipped, and the rest were built. `military` is now 32 cards.**

**Wave T3 — Classified Information Handling &amp; the SF Series** ✅ **SHIPPED**

The Standard Form series is the physical protocol around classified material,
and it is colour-coded on purpose: the colour is the control. Anyone working
on a cleared contract meets these forms before they meet a system. Written as
reference, US-specific, and explicitly *about* the forms — no classified
content, only the public handling procedure.

- [x] Classification Levels &amp; Markings — Top Secret / Secret / Confidential, the damage standard behind each, plus CUI; banner lines, portion marking, classification authority blocks, declassification instructions
- [x] Cover Sheets — SF 703 / 704 / 705 — the colour code (**SF 703 Top Secret = orange**, **SF 704 Secret = red**, **SF 705 Confidential = blue**), what a cover sheet is for, when it attaches and when it comes off, and why the top sheet always matches the highest classification in the stack
- [x] Media &amp; Equipment Labels — SF 706–712 — SF 706 Top Secret (orange), SF 707 Secret (red), SF 708 Confidential (blue), SF 709 Classified (purple, pending determination), SF 710 Unclassified (green, for mixed environments), SF 711 Data Descriptor, SF 712 Classified SCI (yellow); labelling drives, removable media and systems
- [x] Container &amp; End-of-Day Forms — SF 700 (security container information), SF 701 (activity security checklist), SF 702 (security container check sheet); who signs what, when, and what a missed check actually triggers
- [x] Clearance Paperwork — SF 312 nondisclosure agreement, SF 86 questionnaire, SF 714 financial disclosure; the adjudicative guidelines, reinvestigation, continuous evaluation — and what a clearance is *not* (it is not need-to-know)
- [x] Spills, Sanitisation &amp; Reporting — classified message incidents, what to do in the first ten minutes, why you do not delete it yourself, media sanitisation standards, and the reporting chain

**Why this belongs on this site:** the `endpoint`, `blueteam` and `grc`
domains already cover DISA STIGs, CMMC and media destruction. This is the
human-procedure half of the same job, and it is the part that gets people
walked out of the building. Cross-link the SF 706–712 card to the media
sanitisation material in `ops`, and the SF 312 card to the insider-threat
material planned in Track AR.

---

## TRACK U — Cross-Cutting Capstones & Study Aids  (spans domains)

~4 waves, ~20 cards. Tie the whole site together for exam & interview prep.

**SUBSTANTIALLY COVERED — no new cards this session, gaps recorded honestly.** Track U
is a *meta* track: it points at content that already exists and proposes to reorganize
it into hubs. Most of what it names is on the site — the reorganization, not new
content, is what remains, and that is a Phase-4 navigation job (Track AH / the glossary
hub) rather than a content wave. Marked per item so a future session knows what is real
content vs. what is a cross-linking exercise.

**Wave U1 — Certification Study Guides**
- [x] OSCP & Offensive Certs → OSCP prep in `career`, `pentest`, `redteam`, `eng`
- [x] Cloud / DevOps / Security+ / CISSP paths → `career` *Certifications — The Roadmap* + *Certification Roadmap*; the per-objective maps are a **cross-linking exercise**, not missing content (Phase-4 hub work)

**Wave U2 — Interview Prep Hubs**
- [x] System Design Interview → `eng`, `data`, `sec` system-design cards
- [x] Coding Interview → `cs` algorithms/structures + `script` fundamentals
- [x] Behavioral Interview → `career` *Interview Preparation* (STAR)
- [x] Security / SRE / DevOps Interview → covered across `sec`, `blueteam`, `ops`, `devops`, `mind` (on-call)

**Wave U3 — Hands-On Labs & Projects**
- [x] Build a Home Lab → `career` *Building a Home Lab* + `linux`/`net`/`pentest` lab cards
- [x] SIEM at Home → `blueteam` SIEM/Wazuh material
- [x] CI/CD Pipeline / Full-Stack Deploy → `devops` pipeline + `web`/`data` stack cards
- [x] CTF Walkthroughs → `pentest`/`redteam` methodology cards

**Wave U4 — Reference Sheets & Meta**
- [x] Ports & Protocols / Regex / SQL / Git / Linux cheat sheets → `net` *Common Ports*, `script` regex/SQL/Git, `linux` command refs; plus the generated `CALCULUS-CHEAT-SHEET.md`
- [x] IR Runbook Templates → `ops`/`blueteam` incident-response cards
- [x] Glossary → the `acronym` domain (1,069 acronyms, generated + searchable)
- [~] Decision Trees ("which database / language / cloud service?") → **genuine gap.**
  Scattered comparison tables exist, but no single decision-picker card. Left as the one
  real content item in Track U, a candidate for a future cross-cutting capstone.

---

## How much of Phase 3 is actually left — measured three times, and honestly unknown

Three tracks have now had a proper per-card site check before writing:

| Track | Specced | Already on the site | Written |
|---|---:|---:|---:|
| V — Windows Server | 35 | 7 (20%) | 28 |
| AL — CS fundamentals | 35 | 5 (14%) | 30 |
| J — Applied security | 25 | 18 (72%) | 7 |

**Track J's rate is the outlier and the reason is structural:** `sec` is the site's oldest
large domain, so a track written against the *subject* of applied security collides with
it almost everywhere. `infra` and `cs` were new domains, so nothing collided.

**A bulk check over the remaining tracks K–U was attempted and is not trustworthy.** A
three-keyword title match reported 24% covered across 176 cards, but inspection shows it
matching *"Security Program Building"* against *"Cryptography Fundamentals — The Building
Blocks of Security"* on the word "building". It will over-report coverage on coincidental
words and under-report it wherever a card is titled differently from its subject. Both
directions, so the 24% is not a number to plan with.

**What can be said honestly:**

- Tracks pointing at **established domains** — K (`threat`), L (`grc`), M (`redteam`/
  `pentest`), N (`linux`), P (`script`), Q (`net`) — should be expected to behave like J,
  not like V. Those six are ~85 of the remaining cards and may yield a third of that.
- Tracks pointing at **thinner or newer ground** — O (`ai`), S (`career`/`mind`),
  U (cross-cutting study aids) — should behave more like V.
- **The only reliable method is the per-card check, run at the start of the wave.** It
  cost about ten minutes per track and has now saved 24 cards of duplicate writing across
  three tracks.

So the backlog's true size is unknown, and the estimate in this file's header — ~825
cards — is an upper bound that is probably substantially wrong. That is a better position
than the confident number it replaced, and the way to improve it is one track at a time,
not another heuristic.

## Suggested execution order (Phase 3)

| Phase | Tracks | Theme | Rough size |
|-------|--------|-------|-----------|
| 35 | scaffold `data` + H1–H2 | new Data domain; relational + SQL mastery | ~15 cards |
| 36–38 | H3–H8 | DB internals, Postgres, NoSQL, warehousing, ops, career | ~30 cards |
| 39 | scaffold `web` + I1–I2 | new Web domain; browser + modern CSS | ~10 cards |
| 40–42 | I3–I7 | JS deep, frameworks, backends, quality/a11y, shipping | ~25 cards |
| 43–45 | J1–J5 | application/API/crypto/detection/identity security depth | ~28 cards |
| 46–48 | K, L | threat/malware/IR depth; GRC framework-by-framework | ~44 cards |
| 49–51 | M, N, Q | offensive depth; Linux & networking depth | ~54 cards |
| 52–54 | O, P | AI engineering depth; languages & craft | ~40 cards |
| 55–57 | S, T, U | life/mind/career; military leadership; capstones & study aids | ~53 cards |

**Grand total: ~11 new tracks, ~55 waves, ~320 planned cards**, taking the site
from 660 → ~980 topics across 18 domains. Same conventions throughout: one wave
= one CI-green commit; offensive content stays authorized-use + detection-paired;
every card inherits search / permalinks / progress / keyboard-a11y automatically.

**Stretch goals (only if they earn their keep):**
- New `product` 🧭 domain — agile/scrum/kanban, product thinking, UX for engineers,
  roadmapping, stakeholder management, metrics/experimentation.
- New `mobile` 📱 domain — iOS/Android/React Native/Flutter, app store, mobile security.
- Interactive extras — a quiz/flashcard mode over existing cards; a "learning path"
  overlay that sequences cards into guided tracks.

---

# Content & Capability Roadmap — Phase 4: The Enterprise Estate & the Study Platform (Wave 58+)

> **Added on request — "make more plan."** Written August 2026 against a measured
> snapshot of the repo, not from memory. Phase 3's *new-domain* half shipped
> (Tracks H and I are complete — `data` and `web` exist); its *depth* half
> (Tracks J–U, 207 cards) is still open and **remains the priority queue**.
> Phase 4 is deliberately about ground Phase 3 never covers: the **enterprise
> estate an IT professional actually operates**, the **operational trades**, and
> turning the site from a reference into a **study platform**.

## Where the site actually stands

Measured from `data/*.html` at the time of writing:

| Domain | Topics | | Domain | Topics |
|---|---:|---|---|---:|
| `script` Scripting & Web | 137 | | `redteam` Red Team | 43 |
| `ops` Security Operations | 68 | | `data` Data & Databases | 40 |
| `lifestyle` Lifestyle | 59 | | `blueteam` Blue Team | 37 |
| `linux` Linux & Systems | 56 | | `shortcut` Shortcuts | 37 |
| `net` Networking | 55 | | `eng` Engineering | 36 |
| `acronym` Acronym Dictionary | 53 | | `web` Web & Frontend | 35 |
| `cloud` Cloud (AWS·GCP·Azure) | 49 | | `ai` AI & ML | 34 |
| `sec` Security Core | 43 | | `pentest` PenTest | 29 |
| `grc` Governance & Risk | 28 | | `threat` Threat & Attack | 25 |
| `military` Military Codes | 23 | | `endpoint` Endpoint Mgmt | **13** |

**900 topics across 20 domains.** Two numbers drive this phase:

- **`endpoint` has 13 topics** — the thinnest domain on the site, and the one
  closest to the day job of the person maintaining it. Phase 4 takes it to ~55.
- **There is no home at all** for Windows Server, Active Directory
  administration, Exchange/SharePoint/Teams, virtualization, backup, or the
  service desk. That is most of enterprise IT, and it is entirely absent.

## What Phase 4 is, and is not

**It is:** the operator's half of IT. Phase 1–3 built an excellent *security and
software engineering* reference. A person running a real estate spends their week
in Active Directory, Intune, Exchange, a hypervisor, a backup console and a
ticket queue — and almost none of that is on the site yet.

**It is not:** a replacement for Tracks J–U. Ship those first or in parallel;
they deepen domains that already exist and already have an audience.

## Structural decisions

- **New domain `infra` 🏗️ "Infrastructure & Datacenter"** — Windows Server, AD
  DS administration, DNS/DHCP/PKI operations, virtualization, storage and
  backup. This is the biggest single hole in the site. Wire it the usual way:
  `scaffold_domain.py infra 🏗️ …` then `data/infra.html`.
- **New domain `m365` 📨 "Microsoft 365 & Collaboration"** — Exchange Online,
  SharePoint/OneDrive, Teams, Purview, licensing and tenant administration.
  Justified on its own because it is a distinct admin surface from Azure and
  from endpoint, with its own portals, PowerShell modules and failure modes.
- **New domain `itsm` 🎫 "Service Management & Support"** — ITIL practices,
  ticket craft, escalation, on-call, knowledge management, metrics. Small but
  high value: it is the layer every other domain gets consumed through, and it
  is what most people are actually hired into first.
- **Grow `endpoint` rather than splitting it** — Intune, MECM, Autopilot,
  packaging, servicing, macOS and mobile all belong to one role. 13 → ~55.
- **Rule for new domains, applied consistently:** a domain earns its own chip
  when it has (a) ≥ 15 cards of real material, (b) its own tooling and console,
  and (c) a job title attached to it. `infra`, `m365` and `itsm` all pass;
  "printing", "telephony" and "licensing" do not, and get folded in.
- **Part 4 is engineering, not content.** Those tracks change `script.js`,
  `style.css`, `build.py` and CI — they ship as normal commits, not waves.

---

## PART 1 — THE ENTERPRISE MICROSOFT ESTATE

### TRACK V — Windows Server & Directory Services  (→ new `infra` domain)

~7 waves, ~35 cards. The on-prem backbone almost every organisation still runs.
Pairs directly with the `redteam` AD-attack cards — same objects, defender's view.

> **✅ V1–V3 shipped (session 18) — `infra` exists and holds 15 cards.** That is the
> ≥15 bar exactly, which is why the priority shortlist grouped these three rather than
> starting with one. V4–V7 (identity operations, on-prem network services, certificate
> services, server operations) remain: 20 cards, and the domain now clears the bar
> without them, so they are optional rather than owed.
>
> The pairing above turned out to need care rather than assumption. `sec` already holds
> *Active Directory — Structure, Objects & Attacks*, which covers forest/domain/OU and
> Kerberos; writing an "AD DS Architecture" card would have been the duplicate rule 10
> exists to prevent. V2 opens by pointing at that card and answers the administrator's
> question instead — which boundary to reach for, and what each costs. **Check the
> neighbouring domain before writing the overview card; the gap is usually narrower than
> the track list implies.**

**Wave V1 — Windows Server Foundations**
- [x] Windows Server Editions & Licensing — Standard vs Datacenter, CALs, Core vs Desktop Experience
- [x] Server Core & Administration at Scale — why no GUI, and how you manage it anyway
- [x] Server Manager, RSAT & Windows Admin Center — the three consoles and when each wins
- [x] Roles & Features — what installing a role actually changes
- [x] Server Hardening Baseline — LAPS, no browsing, minimal roles, audit policy

**Wave V2 — Active Directory Domain Services**
- [x] AD DS Architecture — forest, domain, tree, OU, site; what each boundary really means
- [x] Domain Controllers & FSMO Roles — the five roles, who holds them, seizing vs transferring
- [x] AD Replication — multi-master, USN, tombstones, `repadmin` triage
- [x] Trusts — forest/external/shortcut, direction vs transitivity, SID filtering
- [x] Sites, Subnets & Site Links — why clients authenticate against the wrong DC

**Wave V3 — Group Policy in Practice**
- [x] Group Policy Architecture — GPO, GPC/GPT, SYSVOL, where settings actually live
- [x] Processing Order & Precedence — LSDOU, enforcement, blocking, loopback
- [x] Filtering — security filtering vs WMI filtering vs item-level targeting
- [x] Group Policy Preferences — the half of GPO people forget exists
- [x] GPO Troubleshooting — `gpresult /h`, RSoP, `gpupdate /force`, and reading the Group Policy operational log

**Wave V4 — Identity Operations**
- [x] Users, Groups & Nesting Strategy — AGDLP, and why nested groups become a mess
- [x] Service Accounts — gMSA, delegation, and retiring shared passwords
- [x] Kerberos in Operations — SPNs, delegation types, ticket lifetimes, clock skew
- [x] Entra Connect & Hybrid Identity — sync, password hash vs pass-through vs federation
- [x] Cleaning Up a Legacy Directory — stale objects, orphaned SIDs, over-permissive ACLs

**Wave V5 — Core Network Services (on-prem)**
- [x] Windows DNS Administration — zones, scavenging, forwarders, conditional forwarders
- [x] DHCP Administration — scopes, reservations, options, failover, relay
- [~] IPAM & Address Discipline — when a spreadsheet stops being enough
- [~] Time Sync — the PDC emulator, `w32tm`, and why Kerberos dies without it
- [x] File Services — shares, NTFS vs share permissions, DFS-N/DFS-R, quotas

**Wave V6 — Certificate Services**
- [x] AD CS Design — root vs issuing CA, offline roots, CRL/OCSP publishing
- [x] Certificate Templates — the settings that matter, and the ones that get you owned
- [x] Auto-enrolment — getting certificates onto devices without touching them
- [x] Certificate Lifecycle Ops — renewal, revocation, the expiry outage nobody schedules
- [x] ADCS Misconfiguration — ESC1–ESC8 from the defender's side (pairs with `redteam`)

**Wave V7 — Server Operations & Troubleshooting**
- [~] Windows Event Log Triage — the channels worth watching, and building a useful filter
- [~] Performance Monitor & Resource Monitor — counters that actually diagnose
- [~] Windows Patching Strategy — rings, maintenance windows, reboot coordination
- [x] Domain Controller Recovery — authoritative vs non-authoritative restore, DSRM
- [x] Decommissioning a Server Properly — the checklist that prevents next year's mystery outage

### TRACK W — Microsoft 365 & Collaboration  (→ new `m365` domain)

~6 waves, ~30 cards. The tenant most organisations live inside.

**Wave W1 — Tenant Foundations**
- [x] M365 Tenant Anatomy — tenant, domains, admin centers, and how they relate to Azure
- [x] Licensing Without Tears — E3 vs E5 vs Business, add-ons, group-based licensing
- [x] Admin Roles & Least Privilege — the built-in roles worth knowing, and PIM for the rest
- [x] Service Health & Message Center — knowing about the outage before the tickets
- [x] Tenant-to-Tenant & Mergers — the migration nobody plans enough time for

**Wave W2 — Exchange Online**
- [x] Mail Flow Explained — connectors, transport rules, the path a message actually takes
- [x] Mailbox Types — user, shared, room, equipment, and delegation done right
- [x] Anti-Spam & Anti-Phish — EOP, Defender for Office, quarantine, safe links/attachments
- [x] Message Trace & Header Analysis — proving where a message went, and where it died
- [x] Retention, Litigation Hold & Archiving — legal's requirements in mailbox terms

**Wave W3 — SharePoint & OneDrive**
- [x] SharePoint Online Architecture — sites, libraries, lists, and the 400-URL trap
- [x] Permissions Model — groups, inheritance, sharing links, and why it sprawls
- [x] OneDrive Known Folder Move — redirecting Desktop/Documents without user pain
- [x] Sync Client Troubleshooting — the top failure modes and their fixes
- [x] External Sharing & Guest Access — B2B collaboration without leaking the tenant

**Wave W4 — Teams**
- [x] Teams Architecture — what a team really is (M365 group + SharePoint + Exchange + chat)
- [x] Teams Policies — meeting, messaging, app and calling policy packages
- [x] Teams Voice Basics — Phone System, calling plans, Direct Routing, SIP at a glance
- [x] Teams Call Quality Troubleshooting — CQD, network requirements, the real culprits
- [x] Governance & Sprawl — naming policy, expiration, the 4,000-team problem

**Wave W5 — Purview, Compliance & Data**
- [x] Purview Overview — the compliance surface, mapped to what auditors ask for
- [x] Sensitivity Labels & DLP — classification that survives contact with users
- [x] Retention Policies vs Retention Labels — the distinction that trips everyone
- [x] eDiscovery & Content Search — running a legal hold end to end
- [x] Insider Risk & Audit Log — audit log in wave 1; Insider Risk in the Purview overview, wave 2

**Wave W6 — M365 Operations & Troubleshooting**
- [x] The PowerShell Modules — Graph, Exchange Online, Teams; connecting and staying connected
- [x] Graph API for Admins — batch operations, permissions, throttling
- [x] Reporting & Usage Analytics — adoption data that answers a real question
- [x] Backup for M365 — why native retention is not a backup
- [x] M365 Troubleshooting Playbook — tenant, identity, licence, policy, client: in that order

### TRACK Y — Endpoint Engineering Depth  (→ `endpoint`, 13 → ~55)

~8 waves, ~40 cards. The domain closest to the maintainer's day job.

**Largely built.** Y1–Y3 were already there, Y5 and Y6 shipped, and the enterprise-MS
waves this September closed most of what remained: Y8's analytics pair (Endpoint Analytics
& Proactive Remediations), Y7's architecture void (MECM at Scale — Site Design, Boundary
Groups & Collections), and Y4's one genuine gap (Autopilot Device Preparation — the classic
Autopilot card already covered hash harvesting, modes and hybrid-vs-Entra join). endpoint is
now 52. What is left is genuinely narrower: Y4 driver management and provisioning packages,
Y8 hardware lifecycle / fleet reporting / the runbook document. `[x]` marks the card that
fills each item, `[~]` names where an item is already covered under a different title.

**Wave Y1 — Intune Deep: Policy** ⟵ see the shipped-note above
- [x] Configuration Profiles → *Configuration Profiles — Settings Catalog, Templates & Custom*
- [x] Policy Conflicts → *Policy Conflicts — Proving Which One Won*
- [x] Security Baselines → *Security Baselines Without Breaking the Fleet*
- [x] Administrative Templates → *Administrative Templates & ADMX-Backed Policy*
- [x] Assignment Strategy → *Assignment Strategy — Users, Devices, Filters & Exclusions*

**Wave Y2 — Intune Deep: Applications**
- [x] Win32 App Packaging → *Win32 App Packaging — .intunewin End to End*
- [x] Install Contexts → *Install Contexts — System vs User*
- [x] Store/LOB/Catalog → *Store, LOB & Enterprise App Catalog Apps*
- [x] App Protection Policies → *App Protection Policies — MAM Without Enrolment*
- [x] Application Troubleshooting → *Application Troubleshooting — Reading the IME Log*

**Wave Y3 — Windows Servicing & Updates**
- [x] Windows Update for Business → *Windows Update for Business — Rings, Deferrals & Deadlines*
- [x] Feature/Quality/Driver → *Feature vs Quality vs Driver Updates*
- [x] Windows Autopatch → *Windows Autopatch — What It Takes Over*
- [x] Update Compliance Reporting → *Update Compliance Reporting — Where the Truth Lives*
- [x] Emergency Patching → *Emergency Patching — Advisory to Verified*

**Wave Y4 — Provisioning & Imaging**
- [~] Autopilot Deep — profiles, hash harvesting, deployment modes, hybrid vs Entra join → covered by *Windows Autopilot — Zero-Touch Provisioning* (modes, hardware hash/group tags, deployment profile, Entra vs hybrid join, troubleshooting)
- [x] Autopilot Device Preparation — the newer flow, and how it differs → *Autopilot Device Preparation — The Newer Flow That Deletes the Hardware Hash*
- [x] Driver Management — DISM, driver packs, and the Autopilot driver dilemma
- [ ] Provisioning Packages & Bulk Enrolment — the escape hatch when Autopilot cannot
- [~] Reprovisioning & Device Reuse — wipe, fresh start, retire, and what each actually removes → Autopilot Reset / Fresh Start covered in the Autopilot card and *The Device That Comes Back Six Months Later, Still Enrolled*

**Wave Y5 — Endpoint Security**
- [x] BitLocker at Scale → *BitLocker at Scale — Silent Enablement, Key Escrow & Recovery* (written)
- [x] Defender for Endpoint → *Defender for Endpoint & Intune — Onboarding, ASR Rules & Tamper Protection* (written)
- [x] Local Admin Rights → *Local Admin Rights — Removing Them, and Endpoint Privilege Management* (written)
- [x] Windows LAPS → *Windows LAPS — Local Admin Password Rotation in Entra and AD* (written)
- [x] Firewall & Removable Media → *Firewall & Removable Media Policy — The Two Controls Auditors Ask About* (written)

**Wave Y6 — Compliance & Conditional Access**
- [x] Compliance Policies Deep → *Compliance Policies Deep — Settings, Grace Periods & What Non-Compliant Costs*
- [x] Device Trust End to End → *Device Trust End to End — Enrolment → Compliance → CA → Access*
- [x] Filters & Dynamic Groups → *Assignment Strategy — Users, Devices, Filters & Exclusions* (already built)
- [x] Reporting on Drift → *Reporting on Drift — Finding Devices That Quietly Stopped Complying*
- [x] The Identity/Endpoint Seam → *The Identity/Endpoint Seam — The Failure That Lands Both Teams on the Bridge*

**Wave Y7 — MECM Beyond Troubleshooting**
- [x] MECM Site Design — CAS, primary, secondary, and when each is justified → *MECM at Scale — Site Design, Boundary Groups & Collections That Don't Melt the Server* (the Inversion card)
- [x] Boundary Groups Done Right — fallback, relationships, and the classic misconfiguration → same card (the Fingerprint card)
- [x] Collections & Queries — WQL that does not melt the site server → same card (the Decision card)
- [~] Co-management Workloads — moving each slider, safely, in order → covered by *Co-management & Cloud Attach* (workload sliders, pilot vs all, the recommended journey)
- [~] Retiring MECM — the honest migration path to cloud-only, and what genuinely blocks it → the retire-to-cloud journey in *Co-management & Cloud Attach*, and the exit framing in the MECM at Scale Decision card

**Wave Y8 — Endpoint Analytics & the Fleet**
- [x] Endpoint Analytics — startup score, app reliability, work-from-anywhere metrics → *Endpoint Analytics & Proactive Remediations* (shipped this September)
- [x] Proactive Remediations — detect-and-fix scripts as a first-class tool → same card
- [ ] Hardware Lifecycle — refresh planning, warranty, disposal, data destruction
- [ ] Fleet Reporting — the five numbers leadership actually asks for
- [ ] Building an Endpoint Runbook — the document that lets someone else take the pager

### TRACK Z — Virtualization, Storage & Backup  (→ `infra`)

~5 waves, ~25 cards. The layer under everything, and the one nobody tests until
they need it.

**Wave shipped this session — 6 cards covering the core void** (`infra` had no
virtualization or backup at all). Written as the essential spine rather than all 25
specced: fundamentals + the two-hypervisor comparison, snapshots-are-not-backups,
3-2-1-1-0 strategy, ransomware-resilient backup, and restore testing / DR posture. The
remaining Z items (SAN/fabric depth, storage performance, P2V/V2V, product-specific
Veeam mechanics) are genuine but narrower and can follow if the estate needs them.
`infra` is now 34.

- [x] Virtualization Fundamentals → *Virtualization Fundamentals — Hypervisors, Overcommit & the Noisy Neighbour*
- [x] vSphere / Hyper-V / Proxmox·KVM → *Hyper-V, vSphere & the Open-Source Stack — The Vocabulary That Transfers* (three specced cards consolidated into one comparison — the six shared ideas are the lesson)
- [x] Snapshots Are Not Backups → *Snapshots Are Not Backups — What They Cost and How They Bite*
- [x] Backup Strategy → *Backup Strategy — 3-2-1-1-0 and the Schemes That Make Restores Possible*
- [x] Ransomware-Resilient Backup → *Ransomware-Resilient Backup — Immutability, Isolation & Assuming the Domain Is Lost*
- [x] Restore Testing + DR Design + DR for Cloud/SaaS → *Restore Testing & DR Design — Turning Backups Into a Recovery Capability*
- [x] VM lifecycle/templates, live migration ops, P2V/V2V and virtualisation troubleshooting →
  four cards into `infra`, see the session record. Still open and genuinely narrower:
  sizing/overcommit deep, storage performance/tiering, backup targets & products, failover/failback
  drill, tabletop, post-incident review.

**Wave Z1 — Hypervisors** ⟵ see the shipped-note above
- [ ] Virtualization Fundamentals — type 1 vs type 2, paravirtualization, hardware assist
- [ ] VMware vSphere — ESXi, vCenter, clusters, DRS/HA, the vocabulary
- [ ] Hyper-V — generations, integration services, checkpoints, Windows-shop realities
- [ ] Proxmox & KVM — the open-source stack, and where it fits
- [ ] Sizing & Overcommit — CPU ready, memory ballooning, the noisy-neighbour problem

**Wave Z2 — Virtual Machine Operations**
- [ ] VM Lifecycle — templates, cloning, sysprep, golden images
- [ ] Snapshots Are Not Backups — what they cost, and how they bite
- [ ] Live Migration & Maintenance Mode — patching hosts without an outage
- [ ] P2V and V2V — the migrations that still happen
- [ ] Virtualization Troubleshooting — the storage/network/host triage order

**Wave Z3 — Storage** — shipped into `infra`. See the session record.
- [x] Storage Fundamentals — block vs file vs object, restated for the datacenter
- [x] SAN & Fabric Basics — LUNs, zoning, multipathing, iSCSI vs Fibre Channel
- [x] NAS & File Services — SMB/NFS at scale, DFS, quotas, access-based enumeration — split: the
  permissions, DFS and quota half was already carded as *File Services — Share vs NTFS Permissions,
  DFS &amp; Quotas*, so the new card is the protocol half (dialects, round-trip behaviour, why file
  workloads feel slow) and the two cross-reference each other
- [x] Storage Performance — IOPS, throughput, latency, queue depth, and which one is your limit
- [x] Storage Tiering & Capacity Planning — forecasting growth before it becomes an incident — two
  cards, because they are different jobs: the efficiency-features card covers tiering with thin
  provisioning and dedup, and capacity planning stands alone
- [x] **Added beyond the plan:** RAID &amp; Erasure Coding — the redundancy layer the track assumed
  and never specced; `RAID` appeared in `cs`, `linux` and `script` but nowhere in `infra`, and
  `erasure coding` was a site-wide zero
- [x] **Added beyond the plan:** Thin Provisioning, Deduplication &amp; Tiering — `thin provision`
  and `erasure coding` were zeros and the thin-provisioning cliff is a real operational hazard

**Wave Z4 — Backup & Recovery**
- [ ] Backup Strategy — 3-2-1-1-0, full/incremental/differential, retention schemes
- [ ] Backup Targets — disk, tape, cloud, immutable and air-gapped copies
- [ ] Backup Products in Practice — Veeam and friends: jobs, repositories, proxies
- [ ] Restore Testing — the drill that turns a backup into a recovery capability
- [ ] Ransomware-Resilient Backup — immutability, isolation, and assuming the domain is lost

**Wave Z5 — Business Continuity in the Real World**
- [ ] DR Design — hot/warm/cold, replication, and matching spend to RTO/RPO
- [ ] Failover & Failback — the half of the runbook everyone forgets to write
- [ ] Tabletop Exercises — running one that finds real gaps
- [ ] The Post-Incident Review — blameless, specific, and actually followed up
- [ ] DR for Cloud & SaaS — what the provider covers, and precisely what it does not

---

## PART 2 — THE OPERATIONAL TRADES

### TRACK AA — Service Desk & IT Service Management  (→ new `itsm` domain)

~5 waves, ~25 cards. The trade most people enter IT through, treated seriously.

**Wave AA1 — The Practices**
- [~] ITIL 4 Without the Jargon — the practices that survive contact with a real team — **already carded as 'ITIL & Service Management — How IT Runs as a Business' in ops**
- [x] Incident vs Problem vs Change vs Request — the distinction, and why it matters
- [x] Priority, Impact & Urgency — building a matrix people actually apply
- [x] Service Catalog & Request Fulfilment — turning ad-hoc asks into a repeatable service
- [~] Change Enablement — CAB, standard changes, emergency changes, freeze windows — **already carded as 'Change Management – The Process That Prevents Self-Inflicted Outages' in grc**

**Wave AA2 — The Ticket Craft**
- [x] Writing a Ticket Someone Else Can Solve — the fields that decide resolution time
- [x] Triage & Categorization — routing correctly the first time
- [x] Escalation — functional vs hierarchical, and how to hand over without losing context
- [x] Closing Well — resolution notes, root cause, and the knowledge article that follows
- [x] Working a Queue — prioritisation, batching, and not drowning

**Wave AA3 — Talking to Humans**
- [x] The First Ninety Seconds — establishing what actually happened
- [x] Explaining Technical Things to Non-Technical People — a repeatable method
- [x] Difficult Conversations — angry users, VIP pressure, saying no
- [x] Remote Support Skills — screen shares, phone-only diagnosis, guiding blind
- [x] Writing for Users — emails, outage notices, and status pages people trust

**Wave AA4 — Knowledge & Automation**
- [x] Knowledge Management — KCS in practice, and keeping articles from rotting
- [x] Self-Service That Works — password reset, software portal, and their adoption traps
- [x] Shift-Left — moving fixes from tier 3 toward tier 1 deliberately
- [x] Ticket Automation — templates, workflows, and where automation backfires
- [x] Asset & Configuration Management — a CMDB that stays true

**Wave AA5 — Running the Function**
- [x] Service Desk Metrics — the ones that improve service vs the ones that game it
- [x] SLAs, OLAs & Underpinning Contracts — the chain of promises
- [x] Capacity & Shift Planning — staffing a queue that has a shape
- [~] On-Call Without Burnout — rotations, handovers, escalation policy, comp time — **already carded as 'On-Call Done Humanely' in ops, plus two cards in mind**
- [~] Major Incident Management — commander, comms lead, scribe, and the bridge discipline — **already carded as 'Incident Command — Running a Major Incident Without Chaos' in ops**

### TRACK AB — Vendor Networking, Firewalls & Wireless  (→ `net`)

~5 waves, ~25 cards. Complements Track Q's protocol depth with the kit people
actually touch. Vendor-specific, deliberately.

**Wave AB1 — Cisco IOS in Practice**
- [x] IOS Navigation — modes, `show` commands worth memorising, config archives
- [x] Switch Configuration — VLANs, trunks, port security, PortFast/BPDU guard
- [~] Router Configuration — interfaces, static and dynamic routing, ACLs — **core routing, ACLs and interfaces are carded in 'Routing Protocols & WAN Technologies' and 'Routing, VLANs & Network Devices' in net**
- [~] Troubleshooting on IOS — `show interface`, CDP/LLDP, SPAN, debug safely — **already carded as 'Network Device CLI — Show Commands' in net**
- [x] Config Management & Upgrades — backups, staged upgrades, rollback plan

**Wave AB2 — Enterprise Firewalls**
- [x] Firewall Policy Design — zones, rule order, the implicit deny, documentation
- [x] Palo Alto Concepts — App-ID, User-ID, security profiles, the commit model
- [x] FortiGate Concepts — policies, VDOMs, SD-WAN features, logging
- [x] NAT on Firewalls — source/destination NAT, hairpinning, and reading a flow
- [x] Firewall Troubleshooting — packet capture, session table, policy lookup order

**Wave AB3 — Wireless Engineering**
- [x] RF Fundamentals — channels, width, co-channel interference, cell design
- [x] Site Surveys — predictive vs passive vs active, and reading a heat map
- [~] Enterprise Wi-Fi Auth — 802.1X, RADIUS, certificates, PSK's remaining niche — **already carded as '802.1X & NAC — Who Gets On the Network?' in net**
- [x] Controller vs Cloud-Managed — Meraki/Mist/Aruba models compared
- [x] Wireless Troubleshooting — roaming, sticky clients, retries, "it's slow" triage

**Wave AB4 — Network Operations**
- [~] Monitoring a Network — SNMP, NetFlow/IPFIX, syslog, streaming telemetry — **already carded as 'Network Monitoring — Seeing What Flows Through' in net**
- [~] Change Control for Networks — the discipline that prevents the 2 a.m. outage — **already carded as 'Change Management – The Process That Prevents Self-Inflicted Outages' in grc, and the cutover card above**
- [x] Network Documentation — diagrams that stay current, IP plans, cable schedules
- [~] Capacity & Utilisation — reading trends before users report slowness — **already carded as 'Capacity Planning – Answering "Will We Run Out of Room?" Before You Do' in ops**
- [~] Network Automation Basics — Netmiko/NAPALM/Ansible for network devices — **already carded as 'Network Automation — Ansible, Netmiko & NAPALM' in net**

**Wave AB5 — Physical & Field**
- [x] Structured Cabling — standards, labelling, patch panel discipline
- [x] Rack & Power Planning — U space, PDUs, redundant feeds, airflow
- [x] Fiber in Practice — types, connectors, cleaning, loss budgets
- [x] Cutover Nights — planning, comms, rollback triggers, go/no-go
- [x] Field Toolkit — what to actually carry, and the tests each tool answers

### TRACK AC — Automation for Administrators  (→ `script` + `ops`)

~5 waves, ~25 cards. Scripting aimed at the ops trade rather than at developers.

**Mostly built; 3 genuine-gap cards written.** `script` (138 cards) already carries the
general automation craft — PowerShell references, IT/cloud/network automation, webhooks,
idempotent scheduling, robust API consumption — so most of AC's craft waves (AC1 pipeline
basics, AC4 API/glue, AC5 version control/documentation) are covered there. Three items
had zero coverage and were written: Microsoft Graph from PowerShell (the modern admin
API; MSOnline/AzureAD are retiring), JEA (constrained, audited delegation — least
privilege for ops), and automation risk/discipline (blast radius, sanity caps, the kill
switch). `script` 138→140, `ops` gains the risk card.

- [x] Working With Graph From PowerShell → *Microsoft Graph From PowerShell — The Modern Admin API*
- [x] Remoting / JEA → *JEA — Just Enough Administration & Constrained Remoting* (plus remoting basics already in the PowerShell cards)
- [x] Automation Risk + Idempotency + logging/auditability + script-to-service → *Automation Risk & Discipline — Blast Radius, Approval Gates & the Kill Switch* (`ops`)
- [x] AC1 pipeline/functions/modules, AC4 REST/webhooks/data-wrangling, AC5 Git/docs → already in `script` (*PowerShell*, *IT Automation*, *Consuming APIs Robustly*, *Webhooks & ChatOps*, *Scheduling Scripts the Right Way*, *Git*)
- [x] **Remaining items shipped** — Ansible/DSC config-as-code, Packer golden images, Pester
  testing and Power Automate/Logic Apps, plus *Secrets in Automation*, which the track specced
  (AC3.4) and which was a genuine zero: `credential in script` and `PowerShell DSC` returned no
  matches anywhere on the site. 5 cards into `script`; see the session record.

**Wave AC1 — PowerShell for Real Work** ⟵ see the shipped-note above
- [x] The Object Pipeline — the thing that makes PowerShell different from Bash
- [ ] Remoting — WinRM, sessions, `Invoke-Command` fan-out, JEA
- [ ] Error Handling That Survives Production — try/catch, `-ErrorAction`, transcripts
- [ ] Writing a Reusable Function — parameters, validation, `-WhatIf`, comment-based help
- [ ] Modules & Distribution — packaging, signing, and an internal repository

**Wave AC2 — Automating the Estate**
- [ ] Bulk User & Group Operations — CSV-driven changes with a dry run
- [ ] Reporting Scripts — from ad-hoc query to scheduled, versioned report
- [ ] Working With Graph From PowerShell — auth, paging, throttling, permissions
- [ ] Scheduled Tasks vs Azure Automation vs Functions — where to run the thing
- [ ] Idempotency for Admins — scripts that are safe to run twice

**Wave AC3 — Configuration as Code, On-Prem** — shipped into `script`.
- [x] Ansible for Windows & Linux — inventory, playbooks, idempotent modules
- [x] Desired State Configuration — where it still fits — same card as Ansible, written as the
  push/pull comparison, since "where it still fits" is only answerable against the alternative
- [x] Golden Images as Code — Packer, and versioning what you deploy
- [x] Secrets in Automation — vaults, managed identities, and never a plaintext credential
- [x] Testing Automation — Pester, dry runs, and a lab that mirrors production

**Wave AC4 — Glue, APIs & Integration**
- [ ] Consuming REST APIs From Scripts — auth, pagination, retries, backoff
- [ ] Webhooks & Event-Driven Ops — reacting instead of polling
- [x] Power Automate & Logic Apps — the low-code option, and its real limits — into `script`, beside the code-based options, because the card's whole point is the comparison
- [ ] CSV, JSON & Excel Wrangling — the daily data shuffling, done cleanly
- [ ] Building an Internal Tool — when a script deserves a front end

**Wave AC5 — Operational Discipline**
- [ ] Version Control for Admins — Git for people who do not ship software
- [ ] Documenting a Script So It Outlives You — the header that saves the next person
- [ ] Logging & Auditability — what an automation must record to be trusted
- [ ] Automation Risk — blast radius, approval gates, and the kill switch
- [ ] From Script to Service — handover, ownership, and retirement

### TRACK AD — Apple, Android & Cross-Platform Endpoint  (→ `endpoint`)

~4 waves, ~20 cards. Fleets are not all Windows; the site currently assumes they are.

**Genuine void — 3 consolidated cards written.** endpoint's 38 cards were entirely
Windows/Intune/MECM; macOS, iOS and Android had only passing mentions and Apple fleet
management (ABM/ADE, supervision) was absent. Three cards cover the cross-platform spine;
the narrower AD4 (ChromeOS, kiosks, UEM selection) can follow. endpoint 38→41.

- [x] macOS for Windows Admins + Security Model → *macOS for Windows Admins — The Translation Table & Security Model* (Gatekeeper/TCC/SIP/XProtect + the PPPC profile)
- [x] Apple Fleet Management (ABM/ADE/VPP, Jamf vs Intune, FileVault escrow) → *Apple Fleet Management — Business Manager, ADE, Jamf vs Intune & FileVault Escrow*
- [x] iOS/Android Enterprise + MAM → *iOS & Android Enterprise — Supervision, Work Profiles & MAM*
- [x] Config profiles / .mobileconfig → in the macOS card; MAM without enrolment cross-linked to the existing App Protection Policies card
- [ ] Remaining (narrower): Jamf smart-group depth, macOS update timing specifics, multi-platform policy design, Linux desktop, ChromeOS, kiosk/frontline, UEM selection — follow on demand

**Wave AD1 — macOS Administration** ⟵ see the shipped-note above
- [ ] macOS for Windows Admins — the translation table for every concept
- [ ] macOS Security Model — Gatekeeper, notarization, TCC, SIP, XProtect
- [ ] Configuration Profiles — the `.mobileconfig` model and its payloads
- [ ] macOS Update Management — deferrals, enforcement, and Apple's timing
- [ ] macOS Troubleshooting — logs, `profiles`, `mdmclient`, and the console

**Wave AD2 — Apple Fleet Management**
- [ ] Apple Business Manager — ADE, VPP, Managed Apple IDs
- [ ] Jamf Pro Concepts — smart groups, policies, patch management
- [ ] Intune for macOS — what it covers, and where it still falls short
- [ ] Apple Device Enrolment Flows — ADE vs user enrolment vs BYOD
- [ ] FileVault & Escrow — encryption and recovery keys on Apple hardware

**Wave AD3 — Mobile**
- [ ] iOS Management — supervised vs unsupervised, the supervision-only capabilities
- [ ] Android Enterprise — work profile, fully managed, dedicated devices
- [ ] Mobile App Management Without Enrolment — protecting data on personal phones
- [ ] Certificates & Wi-Fi/VPN on Mobile — SCEP/PKCS profiles that actually deploy
- [ ] Mobile Troubleshooting — enrolment failures, push, and the vendor-specific traps

**Wave AD4 — Cross-Platform Reality**
- [ ] Multi-Platform Policy Design — one intent, four implementations
- [ ] Linux Desktop Management — the enterprise-Linux endpoint story
- [ ] ChromeOS in the Enterprise — where it wins, and its management model
- [ ] Kiosks, Shared & Frontline Devices — shared sign-in, autologin, lockdown
- [ ] Choosing a UEM — evaluation criteria that are not a vendor feature matrix

---

## PART 3 — SPECIALIST & EMERGING

### TRACK AE — Regulated, OT & Specialist Environments

~4 waves, ~20 cards. Where the generic answer is the wrong answer.

**AE1 (OT/ICS) written — 3 cards into `sec`, the most distinctive void on the site.**
Purdue model, Modbus/DNP3/OPC UA and IEC 62443 were entirely absent. AE2 (regulated
industries) largely overlaps existing `grc` work (HIPAA, PCI, CMMC/STIGs); AE3/AE4 (scale
extremes, sustainability/accessibility) are narrower and can follow. `sec` 46→49.

- [x] OT vs IT + The Purdue Model → *OT vs IT & the Purdue Model — When the Generic Answer Is the Wrong Answer*
- [x] ICS Protocols → *ICS Protocols — Modbus, DNP3, OPC UA and Their Security Assumptions*
- [x] Securing OT Without Breaking It + OT Incident Response → *Securing OT Without Breaking It — Segmentation, Access & Safety-First IR*
- [x] AE2 regulated industries → HIPAA/PCI/CMMC/STIGs already in `grc`; legal hold in `grc`'s data-governance card
- [x] **Scale extremes, green IT, accessible IT and surveillance-vs-monitoring shipped** — AE3 and
  AE4 in full, 8 cards into `ops`; e-waste and professional ethics were already carded elsewhere.
  See the session record.
- [ ] Remaining (narrower): healthcare/finance/gov/edu operational specifics — the AE2 items whose
  regulatory half is already in `grc` but whose day-to-day operational texture is not written

**Wave AE1 — Operational Technology & ICS** ⟵ see the shipped-note above
- [ ] OT vs IT — different priorities, different consequences, different clocks
- [ ] The Purdue Model — levels, and where the boundaries really sit today
- [ ] ICS Protocols — Modbus, DNP3, OPC UA and their security assumptions
- [ ] Securing OT Without Breaking It — passive monitoring, segmentation, patch reality
- [ ] OT Incident Response — safety first, and why you may not pull the plug

**Wave AE2 — Regulated Industries**
- [ ] Healthcare IT — HIPAA in operations, clinical systems, medical device gotchas
- [ ] Financial Services IT — SOX, PCI DSS in practice, change control expectations
- [ ] Government & Defense IT — CMMC, STIGs, ATO packages, air-gapped realities
- [ ] Education IT — FERPA, 1:1 device programs, seasonal load, tiny budgets
- [ ] Legal Hold & Discovery for IT — what "preserve everything" means operationally

**Wave AE3 — Scale Extremes** — shipped into `ops`. See the session record.
- [x] IT for Very Small Organisations — one person, no budget, and what to prioritise
- [x] IT for the Very Large — federation, delegation, and standardising across business units
- [x] MSP Operations — multi-tenant tooling, onboarding, and the support model
- [x] Remote & Distributed Workforces — provisioning, support and security without an office
- [x] Mergers, Acquisitions & Divestitures — the IT workstream nobody staffs properly

**Wave AE4 — Sustainability, Accessibility & Ethics in Operations** — shipped into `ops`, except
where noted.
- [x] Green IT — power, cooling, hardware lifespan, and the honest carbon maths
- [x] Accessible IT — assistive technology, procurement, and testing your own tools
- [~] E-Waste & Secure Disposal — data destruction standards and chain of custody — carded earlier
  this session as *Media Sanitisation &amp; Disposal — What "Wiped" Actually Means* in `sec`; the
  Green IT card cross-references it, because sanitisation is what makes reuse and resale available
- [x] Surveillance vs Monitoring — where legitimate telemetry becomes something else
- [~] Professional Ethics Under Pressure — carded in `career` as *Professional Ethics — The
  Responsibility That Comes With Access*; the surveillance card cross-references it and supplies the
  specific requests that test the line

### TRACK AF — Working With AI as an IT Professional

~4 waves, ~20 cards. Complements Track O (building AI) with *using* AI at work,
and defending against its misuse. Content lands in `ai`.

**Enterprise-governance + impersonation wave shipped this session — 5 cards.** AF1
(using AI well, prompting, verification) was already covered by `ai`'s *Using AI Well*,
*AI Tools for IT Work* and *Prompt Engineering* cards; AF3's phishing/deepfake basics
touch several domains. The genuine void was the **operator/governance** angle, now
filled:

- [x] Copilot & Assistant Deployment → *Deploying AI Assistants — Copilot, Licensing & Data Boundaries*
- [x] Shadow AI → *Shadow AI — Finding It, and Offering a Sanctioned Path Instead*
- [x] AI Acceptable Use Policy → *AI Acceptable Use — A Policy People Will Actually Follow*
- [x] Data Governance for AI → *Data Governance for AI — Oversharing at the Speed of Search*
- [x] Voice & Video Impersonation → *Deepfakes & Voice/Video Impersonation — Verification That Resists AI*
- [x] AF1 "Using AI Well" cluster → already in `ai` (*Using AI Well*, *AI Tools for IT Work*, *Prompt Engineering*)
- [ ] Remaining (narrower / measurement-y): AI for log analysis, measuring whether it helped, detecting automated attacks, the AI-incident tabletop, and the AF4 career-effects wave — follow on demand

**Wave AF1 — Using AI Well** ⟵ see the shipped-note above
- [ ] What LLMs Are Good and Bad At — a calibrated mental model for daily work
- [ ] Prompting for Technical Work — context, constraints, and verification loops
- [ ] AI-Assisted Scripting — generating, reviewing and testing code you did not write
- [ ] AI for Log & Error Analysis — where it accelerates triage, where it invents
- [ ] Verification Discipline — never shipping an unverified AI answer

**Wave AF2 — AI in the Enterprise**
- [ ] Copilot & Assistant Deployment — licensing, data boundaries, admin controls
- [ ] Data Governance for AI — what the assistant can see, and oversharing at scale
- [ ] Shadow AI — discovering it, and giving people a sanctioned path instead
- [ ] AI Acceptable Use Policy — a policy people will actually follow
- [ ] Measuring Whether It Helped — beyond vendor-supplied productivity claims

**Wave AF3 — AI-Enabled Attacks & Defence**
- [ ] AI-Assisted Phishing & Deepfakes — what changed, and what did not
- [ ] Voice & Video Impersonation — verification procedures that resist it
- [ ] Prompt Injection Against Your Own Tools — the agent that reads attacker text
- [ ] Detecting Automated Attacks — behavioural signals that scale
- [ ] Tabletop: An AI-Assisted Incident — running the exercise

**Wave AF4 — Career Effects**
- [ ] What AI Changes About IT Roles — honestly, by role, with the parts it cannot do
- [ ] Skills That Appreciate — judgement, systems thinking, verification, communication
- [ ] Building AI Into a Workflow — one real workflow, before and after
- [ ] Interviewing in an AI World — what employers now test for
- [ ] Staying Current Without Drowning — a sustainable information diet

---

## PART 4 — THE SITE AS A STUDY PLATFORM (engineering, not content)

These change code, not `data/*.html`. Each is a normal commit with a headless
smoke check; none of them should regress `file://` support.

### TRACK AG — Study Tooling

The study FAB already has **flashcards, an auto-generated quiz, a study list and
a quick-jump palette**. This track makes them into a system rather than four
separate toys.

*Shipped-note: four of the eight below are done and were shipped without any test coverage —
spaced repetition, the acronym quiz, the distractor fix and export/import. All four were verified
headlessly and given the checks they never had (14 of them) rather than rewritten. Read the ticks.*

- [x] **Spaced repetition** — **already built.** `srsGrade()` / `srsIsDue()` / `srsDueCount()` in
  `script.js`, storing `{e, i, d, n}` under `srs:<id>`, with the due count badged on the study FAB
  and a "⏰ Due today" deck. Verified: intervals step 1 → 6 → 15 days across three "good" gradings,
  a graded card is marked known, a scheduled card leaves the due count, and "again" resets the
  interval and drops the ease. Five checks added.
- [x] **Acronym quiz mode** — **already built.** `acroQuestions()` builds expand, contract and
  disambiguate questions straight from the dictionary. Verified: 8 questions across 28 subject
  areas, every one with four distinct options including the answer, and a single area can fill a
  quiz on its own. Three checks added.
- [x] **Better distractors** — **already built, both quizzes.** The topic quiz draws wrong answers
  from the chosen scope's pool; `acroDistractors()` draws from the same subject area and falls back
  to the whole dictionary only when the area is too small. The multi-meaning questions use the
  *other meanings of the same acronym* as distractors, which is the sharper version of the item.
  Verified: a domain-scoped quiz produced four options, none from outside that domain.
- [x] **Exam mode** — 📋 Exam in the study menu. Fixed length (10 / 20 / 40), a clock at 45 seconds
  a question or untimed, answers recorded with **no marking until the end**, back-navigation to
  change one, and running out of time submits rather than errors. The report scores the paper,
  breaks it down by domain **weakest first**, lists every missed topic as a link — marking the ones
  left blank as such — and offers "★ star all of these", which puts the whole list into the study
  deck in one click.
- [x] **Learning paths** — `data/paths.json`, six routes over 75 existing topics, inlined by
  `build.py` and opened from the study menu as 🧭 Learning paths. A step counts as done when the
  topic carries the same ✓ the topic header sets — not a second, parallel progress state — and the
  first unreviewed step is marked "you are here" with a **Continue** button that goes straight to
  it. `tools/check_paths.py` gates the ids in CI. Routes: Network Foundations (22), SOC Analyst
  Starter (15), Breaking Into IT (11), Comfortable in the Terminal (11), First 90 Days on an
  Endpoint Team (8), Cloud From Zero (8).
- [x] **Progress dashboard** — 📊 Progress in the study menu: reviewed of total for the whole site
  and per domain with a bar, plus starred, known, noted and due counts, and a day streak with its
  best run. Every number comes from `localStorage` and the inlined topic index, never from the
  document — the dashboard has to report on all thirty domains while at most one is in the DOM.
  Domains with nothing read are listed last and muted rather than hidden. The streak is one record
  (`{last, n, best}`), fed by every action that means work happened, and it travels in the export.
- [x] **Export & import progress** — **already built** (session 10): `bkExport()`, `bkValidate()`,
  `bkSanitise()` and `bkApply()` with merge / replace / preview. Verified end to end: the export
  carries reviewed, bookmark, known and srs keys and refuses to carry an unrelated one; a round trip
  restores all three; a file that is not a progress export is rejected on all three grounds; and a
  well-formed file carrying a key the page does not own, or a malformed scheduler record, is
  refused rather than written. Six checks added.
- [x] **Per-topic notes** — a 📝 in the topic tool cluster beside ★ ✓ 🔗. One note per topic under
  `note:<id>`, rendered at the top of the topic body whenever that topic is open, with the header
  button lit on any topic that carries one. Built as a *sibling* of the notepad rather than an
  extension of it: the notepad is one shared scratchpad, and a note about Kerberos delegation
  belongs on the Kerberos card. Because it uses the same prefixed-key shape as the other per-topic
  state, the export, the import's validation and the "what do we own" list picked it up by the rules
  they already had — one branch in `bkSerialise` for free text, and the count line now distinguishes
  topic notes from notepad notes so a restore cannot misreport.

### TRACK AH — Findability & Navigation

- [x] **Acronym-aware search** — expand the query through `acronyms.json` so
  searching "Unified Endpoint Management" finds UEM cards and vice versa.
  **Already built** — `acroSearchMap()` and `searchTerms()` in `script.js` do exactly this, and
  the count line reports the alternate it matched through. Verified headlessly in both directions:
  `UEM` and `Unified Endpoint Management` each return 7 matches in 4 domains, `MFA` and
  `Multi-Factor Authentication` each return 54 in 14. Ticked after checking rather than assuming.
- [x] **Expansion density toggle** — **already built.** `cycleAcroMode()` in `script.js` plus the
  `.acro-hover` / `.acro-off` rules in `style.css`, behind the header's acronym button. Three modes
  rather than the four specced: *first use per domain* would need the annotator to mark first uses
  at build time, and the hover mode already solves the density-in-tables cost the item was written
  for. Verified headlessly — cycles always → hover → off → always, the label and stored preference
  track it, and the preference survives a reload. Two smoke checks added, since it had none.
- [x] **Related topics** — `data/related.json` keyed on topic id, inlined by `build.py` and
  rendered as a "See also" strip the first time a topic is opened. Seeded from the 201
  `<span class="xref">` cross-references already in the cards — a writer saying two topics belong
  together, and already title-checked by the linter — then curated up to 554 links on 412 topics.
  `tools/suggest_related.py` provides the shortlists (`--xrefs`, `--domain`, `--topic`) and a
  `--check` that catches a dead id before it renders as a dead link.
- [x] **Clickable cross-references** — `build.py` now stamps `data-xref="topic-id"`, `role="link"`
  and `tabindex="0"` on all 201 of them, in a second pass after every domain's ids exist, since a
  cross-reference almost always names a card in another domain. Click and Enter both follow.
  A span whose title stops resolving keeps neither the id nor the styling, so it degrades to the
  plain italic text it was rather than to a dead link.
- [x] **Domain landing cards** — 30 intros shipped as `data/domain-intros.json`, inlined by
  `build.py` and rendered by `script.js` above a domain's topics on hydration. Deliberately *not*
  a `.topic` in the content files: a signpost should not be counted by the topic index, dated by
  `stamp_freshness.py`, checked by `lint_content.py`, offered by the random pick or dealt into a
  deck. `start` holds topic names, resolved against the parsed block at render time, so a rename
  costs the card one link instead of leaving a dead button.
- [x] **Search operators** — `domain:net` and quoted phrases shipped; `badge:` deliberately not.
  Badges are inconsistent across domains — "SEC • Essential", "Beginner", "OPS • Modern" and
  "LIFESTYLE • Career" all coexist — so a `badge:` operator would need a vocabulary the reader
  cannot guess. `domain:` uses domain ids, which the chips and permalinks already expose. Multiple
  `domain:` terms are additive. Documented in the search box's tooltip; five smoke checks protect
  the behaviour.
- [x] **Recently viewed** — the last ten topics lead the quick-jump palette on an empty query,
  badged so the ordering reads as deliberate. Stored as ids, so a card later renamed or removed
  simply drops out when the index cannot resolve it. Visits are recorded from both paths that open
  a topic — clicking a header and following a link. Three smoke checks.
- [x] **Deep-link to a card, not just a topic** — `#topic-id/3` scrolls to the third concept card
  and marks it briefly; clicking a card's `.concept-label` copies that link. Cards are addressed by
  position rather than by a slug of their title: a slug needs every `.concept-title` stamped and
  kept stable, and concept titles are edited far more freely than topic names — which have an alias
  map precisely because they are not. An index survives rewording and breaks on reordering; between
  the two, rewording is what actually happens. Out-of-range indices fall back to the topic, so a
  link shared before a card was removed still lands somewhere useful.

### TRACK AJ — Quality Gates & Tooling

*(No "TRACK AI" — the letters would collide with the AI domain.)*

*Shipped-note: five of the eight below are done. `lint_content.py`, `page_budget.py` and the
duplicate-slug guard have been in CI for many sessions; `check_markup.py` and `acronym_drift.py`
shipped in the Track AJ wave. Read the ticks, not the original list.*

- [x] **Markup validator in CI** — `tools/check_markup.py`, a stack-based `html.parser` pass over
  every `data/*.html` fragment and over `index.html`. Unclosed tags, stray closers and closed void
  elements all fail the build. `--self-test` runs it over six deliberately broken fixtures and fails
  if any of them passes, so "0 errors" cannot mean "stopped looking". Both steps are in CI.
- [x] **Content linter** — `tools/lint_content.py`, in CI since session 10; tracks a warning trend
  and errors on convention breaks and dangling cross-references.
- [x] **Duplicate-slug guard** — `lint_content.py` errors on a collision by name, with the file and
  line of the topic that claimed the slug first. `build.py` still suffixes, so the guard is what
  makes the suffix visible rather than silent.
- [x] **Accessibility CI** — `tools/a11y_test.mjs`, axe-core over three states (shell, an open
  domain with an expanded topic, a study dialog) in **both themes**, in CI and behind `make a11y`.
  Its first run found **16 serious violations**; all are fixed and all six scans are clean.
- [~] **Link & anchor checker** — measured rather than built: the content contains **one**
  `href="#"` and **one** external link in 1,355 topics. Cross-references are the real mechanism, and
  all 201 are checked by `lint_content.py` and now resolved to ids by `build.py`. There is nothing
  left for this item to check; it was written before the `xref` convention existed.
- [x] **Performance budget** — `tools/page_budget.py`, in CI, four metrics with headroom.
- [x] **Visual regression** — `tools/visual_test.mjs`, in CI and behind `make visual`. Deliberately
  **not** "a few representative topics": it shoots the **filter bar** in both themes and nothing
  else. Content screenshots fail on every content wave, and a check that fails constantly is one
  people learn to ignore. Threshold calibrated rather than guessed — repeated runs differ by exactly
  zero pixels, and reverting one chip's colour moves 0.111%, so the limit is 0.05%.
- [x] **Acronym drift report** — `tools/acronym_drift.py`. Capitalised tokens the dictionary lacks,
  ranked by frequency, per domain with `--domain`; `--unused` lists entries no card uses. A report,
  not a gate — see the tool's docstring for why neither number is safe to fail a build on.

### TRACK AK — Delivery, Performance & Reach

- [x] **Lazy domain loading** — ✅ **shipped, as deferred content rather than fetched
  fragments; see §4b-iii.** Not the shape this item specified. There are no per-domain
  files and no fetch: `build.py` parks each domain's body in an inert
  `<script type="text/html">` block in the same single file, and `script.js` moves one
  domain into the DOM at a time. That keeps `file://`, the PWA and the offline story
  exactly as they were — the flag and the second build output this item asked for were
  never needed. It also does not save a byte, which §4b-ii had already established was
  the weak half of the argument; it costs 37 KB gzipped. What it buys is the DOM-size
  win §4b-ii identified as the real one: **92,330 elements → 404 at load, 2,739 ms →
  771 ms on a 4× throttled phone.** All five whole-DOM features were rewired rather
  than left to silently under-report. Original note follows. `index.html` is ~3.2 MB of
  HTML; every visitor downloads all 20 domains to read one. Emit per-domain
  fragments plus a shell that fetches on expand, **while keeping the current
  single-file build for `file://`**. Two outputs from one `build.py`, selected
  by a flag. This is the single biggest performance win available, and also the
  riskiest change on this list — it must not break offline or the PWA.
- [x] **Print packs** — 🖨 Print pack in the study menu: a domain, a **learning path**, the study
  list or today's due cards, every card open, none of the page furniture, page-broken between
  domains and never through a concept card. Built into its own container rather than by styling what
  is on screen — only one domain is ever hydrated, so "print what is rendered" could never produce a
  path that spans five domains, which is the pack most worth printing.
- [x] **Markdown export** — ⬇ Export as Markdown in the study menu, with the same scope picker the
  decks use (all / one domain / study list / due today). Converts from the *deferred blocks*, so a
  domain that has never been opened exports identically to one that has. Copy or download; the
  filename carries the scope and the date.
- [x] **PWA polish** — the worker no longer calls `skipWaiting()` on install, so a new version
  *waits*; the page offers a dismissible "A newer version of this page is ready — Reload", and only
  then does the swap happen. `CACHE_VERSION` is now **derived by `build.py`** from a hash of
  `index.html`, `style.css` and `script.js`, so it changes exactly when the bytes do — no forgotten
  bump, no pointless invalidation — and CI fails if it is stale. The fragments clause is moot:
  lazy loading shipped as inline deferred blocks, so there is nothing separate to precache.
- [x] **Share cards** — one card for the site, not thirty. `tools/gen_og_image.mjs` renders
  `Img/og-card.png` at 1200×630 from an HTML template through Playwright, with the topic and domain
  counts read from the sources so they cannot go stale; `--check` fails CI if it is out of date. The
  page also gained the `description`, Open Graph and Twitter tags it had never had at all.
  **Per-domain cards were deliberately not built**: domains are hash fragments, and no crawler
  distinguishes `/#net` from `/` or runs the script that would render it — they would be thirty
  images nothing ever requests.
- [x] **Reading time & size hints** — per domain, so a study session can be
  planned realistically. ✅ Session 19. Computed in `build.py` from the real word
  count, weighted by kind: tables ×1.4 because they are scanned rather than read,
  code blocks ÷3 because they are skimmed. Counting everything at prose speed
  under-estimated the table-dense domains, which is the wrong direction — an
  estimate that reads short is worse than none. Spread runs 7 min (`lifestyle`) to
  4h 15m (`script`), and the smoke test fails if any domain loses its hint or
  reports zero topics.

---

## Content debt register

Measured, not guessed. None of it is urgent; all of it is cheap to fix while
touching a file for other reasons.

| Item | Count | Notes |
|---|---:|---|
| Topics with no `.topic-name` | 90 | `script.js` falls back to the header's full text, so their slugs include the badge and icon text. Concentrated in the older "Beginner" waves. |
| Inline `style="…"` attributes | 1,918 | `CONTRIBUTING.md` says use the `c-*` utility classes; the light theme is where this shows. |
| Hard-coded hex colours in content | 148 | Same problem, worse: these do not track the theme at all. |
| `ai-table` vs `ref-table` | 361 vs 615 | `CONTRIBUTING.md` prefers `ref-table` for new content; the split is historical. |
| Old `topo-svg` diagrams | 5 | In `net.html`, hard-coded dark-theme strokes — invisible-ish in light mode. The two new SVGs use theme variables and should be the pattern. |
| `patches/` | ~1.7 MB | 50+ already-applied one-shot scripts. Archive to a tag or a branch and delete from `main`. |
| `index.html` | ~3.2 MB | See Track AK. |

**Markup health:** a full parse of every `data/*.html` found **no unclosed or
stray tags**. Raw `<span` vs `</span>` counts differ only because the formatter
splits closing tags across lines (`</span\n>`), which is valid — worth knowing
before someone "fixes" a bug that does not exist.

---

## Suggested execution order (Phase 4)

Interleave with the outstanding Phase-3 tracks; do not block on them.

| Slot | Tracks | Theme | Rough size |
|---|---|---|---|
| 58 | AG (spaced repetition, acronym quiz) + AH (acronym-aware search, density toggle) | Make what exists better before adding more | code only |
| 59–62 | scaffold `infra` + V1–V4 | Windows Server, AD DS, Group Policy, identity ops | ~20 cards |
| 63–64 | V5–V7 | DNS/DHCP/files, AD CS, server troubleshooting | ~15 cards |
| 65–68 | Y1–Y4 | Intune policy & apps, servicing, provisioning | ~20 cards |
| 69–71 | Y5–Y8 | endpoint security, compliance, MECM depth, analytics | ~20 cards |
| 72–74 | scaffold `m365` + W1–W6 | tenant, Exchange, SharePoint, Teams, Purview, ops | ~30 cards |
| 75–77 | Z1–Z5 | hypervisors, storage, backup, DR | ~25 cards |
| 78–79 | scaffold `itsm` + AA1–AA5 | the support trade, done seriously | ~25 cards |
| 80–82 | AB1–AB5 | Cisco, firewalls, wireless, netops, physical | ~25 cards |
| 83–84 | AC1–AC5 | PowerShell and automation for admins | ~25 cards |
| 85–86 | AD1–AD4 | macOS, Apple fleet, mobile, cross-platform | ~20 cards |
| 87–88 | AE1–AE4, AF1–AF4 | OT/regulated/scale; AI at work | ~40 cards |
| 89–90 | AJ + AK | quality gates, then lazy loading and print packs | code only |

**Phase 4 total: 10 content tracks, 53 waves, 265 cards, 3 new domains**,
taking the site from 900 → ~1,165 topics across 23 domains — plus ~29
engineering items that make those topics easier to find, study and trust.

Combined with the outstanding Phase-3 depth tracks (J–U, 207 cards), the full
remaining backlog is **466 cards**.

## Definition of done for a wave

Unchanged from earlier phases, restated so it is in one place:

1. Content lives in `data/{domain}.html` and follows `CONTRIBUTING.md`.
2. `python3 tools/annotate_acronyms.py` — add any new acronyms to
   `data/acronyms.json` first, with a `byDomain` override if the term is
   ambiguous in that domain.
3. `python3 tools/gen_acronym_domain.py` if the dictionary changed.
4. `python3 build.py`, then a headless load of `index.html`: zero console
   errors, the new topic reachable by permalink, search finds it.
5. One commit per wave, CI green.
6. Offensive content keeps the authorized-use framing and pairs with detection.

## Ideas considered and deliberately rejected

Recorded so they do not get re-proposed every planning round.

- **A `product` domain** (agile, roadmapping, stakeholder management) — real
  subject, wrong site. It has no operational surface and would sit unread next
  to twenty technical domains. The parts that matter to engineers already live
  in `eng` and `lifestyle`.
- **A `mobile` app-development domain** — distinct from mobile *device
  management*, which Track AD covers. App development is a whole career the site
  does not otherwise touch; adding it would stretch the premise past breaking.
- **User accounts and a backend** — the site's defining property is that it is
  static, works from `file://`, and stores nothing about anyone. Cross-device
  sync is worth wanting, but export/import (Track AG) buys most of the value at
  none of the cost.
- **A comments or contributions layer** — moderation burden, no audience for it.
- **Splitting the acronym dictionary into its own site** — the inline expansions
  are the feature; separating the data from the content it annotates would
  remove the reason it works.
- **Translating the site** — the vocabulary is English-native (every acronym,
  every certification, every vendor console). Translation would be a permanent
  maintenance tax on a solo project. Track AK's exports are the pragmatic
  substitute.

---

# Content & Capability Roadmap — Phase 5: Foundations, Frontiers & the Business of IT (Wave 91+)

> **The layers Phases 1–4 sit on top of, and the ones they stop short of.**
> Phase 4 covered the estate an operator runs. Phase 5 goes one level *down* —
> the computer science and mathematics under every domain, and the physical
> hardware under that — and one level *out* — the frontier technologies arriving
> now, and the business, leadership and practice layer that decides whether any
> of it gets funded.

## What is deliberately not here

Checked against existing content before writing, because three of these nearly
became duplicate tracks:

- **Personal health, productivity systems and personal finance** — already
  Phase-3 Track S (Waves S1–S3), and `lifestyle` already ships *Burnout*,
  *Time Management*, *Financial Basics for IT Workers* and *Learning How to
  Learn*. Phase 5 touches money only at the **organisational** level: budgets,
  vendors, contracts, TCO.
- **Technical writing, mentorship and professional ethics as personal skills** —
  already in `lifestyle`. Track AU is about **enablement as a function**:
  curricula, labs, workshops, internal training programmes.
- **Freelance tax mechanics** — Track S3 has it. Track AV is about building and
  running a *practice*: positioning, scoping, pricing, delivery, client risk.

## Structural decisions

- **New domain `cs` 🧮 "Computer Science & Mathematics"** (Tracks AL, AM). This
  bends the Phase-4 rule that a domain needs its own tooling and console —
  theory has neither. It earns the exception because it is the substrate under
  *every* other domain and belongs to none of them: complexity theory is as
  relevant to a query plan as to a rate limiter as to a password-cracking
  estimate. Filing it inside `eng` would bury it from the security and data
  readers who need it most.
- **New domain `hw` 🔧 "Hardware, Electronics & Embedded"** (Track AN) — **scaffolded and shipped**;
  8 cards, accent `#a3e635`, chip in the Core IT group. Passes
  the rule cleanly: its own tools (multimeter, logic analyser, soldering iron,
  POST card), its own job titles (bench tech, field engineer, embedded
  developer), and easily 30 cards of material.
  **Migration note:** `linux` already holds A+ hardware cards. Do **not** move
  them — that would break permalinks and stored progress. Add new material to
  `hw` and cross-link both ways; revisit consolidation only if `hw` passes ~25
  cards and the duplication becomes visible.
- **New domain `biz` 💼 "IT Business, Leadership & Practice"** (Tracks AS–AV).
  Distinct from `lifestyle` (which is the *individual*) and from `grc` (which is
  *controls and audit*). This is the money, the people and the practice.
- **A consequence to plan for:** this takes the site to **26 domains**, and the
  filter chip bar is already a single scrolling row of 21. Phase 4's Track AH
  gains one item: **group the chips into categories** — Core IT · Security ·
  Engineering · Cloud & Infrastructure · Foundations · Human — as a two-tier
  bar or a grouped dropdown. Ship that *before* the 24th domain, not after.

---

## PART 1 — FOUNDATIONS

### TRACK AL — Computer Science Fundamentals  (→ new `cs` domain)

~7 waves, ~35 cards. The theory that keeps turning up in interviews, incident
reviews and design arguments — taught for practitioners, not for a degree.

> **✅ AL1–AL3 shipped (session 18) — `cs` exists and holds 15 cards.**
>
> **The shortlist's claim that this material "is nowhere yet" was false.** `script`
> already carried six cards on it — *Big O Notation*, *Big O & Algorithms*, three on
> data structures, and *Thinking in Algorithms* — at beginner-to-intermediate depth,
> and duplicating each other. Writing AL1's "Big-O in Practice" and AL2's "Arrays,
> Lists & Memory Layout" as specified would have produced a third Big-O card and a
> fourth data-structures card.
>
> `cs` therefore holds the depth that genuinely was missing and cross-references
> `script` for the basics — the boundary V2 drew against `sec`, drawn twice more here.
> Cards skipped as duplicates: the Big-O introduction, the arrays/lists introduction,
> and the container-choosing card. Cards written instead: what Big-O hides, amortized
> analysis, hash flooding, trees beyond BST, graphs, probabilistic structures,
> catastrophic backtracking, reservoir sampling.
>
> **`script` still duplicates itself** — two Big-O cards and three data-structure
> cards, at overlapping depth. Not touched here, because merging content is a
> different act from adding it and deserves its own session. It is the strongest
> remaining candidate in that domain, ahead of anything on the AL4–AL7 list.
>
> **✅ AL4 also shipped — `cs` is at 20 cards.** AL5 and AL6 (architecture, compilers)
> remain and are genuinely absent. **AL7 is mostly not** — `devops` has *CAP Theorem &
> Consistency Models*, and `eng` has *Idempotency & Exactly-Once*, *Distributed
> Transactions* and *Consistency in Practice*. Only three AL7 cards are real gaps:
> clocks and causality, consensus (Paxos/Raft), and failure detection with FLP.

*(`- [~]` marks a card deliberately cut rather than deferred — see the wave note.)*

**Wave AL1 — Complexity & Correctness**
- [x] Big-O in Practice — what the notation hides, and when constants win
- [x] Time vs Space Trade-offs — caching, precomputation, and the memory you pay
- [x] Amortized Analysis — why a dynamic array is O(1) "on average"
- [x] Recursion & Induction — reasoning about a function that calls itself
- [x] P, NP & Why It Matters to You — intractability, approximation, and knowing when to stop

**Wave AL2 — Data Structures From First Principles**
- [x] Arrays, Lists & Memory Layout — cache lines, locality, and why arrays win
- [x] Hash Tables — hashing, collisions, load factor, and the DoS that exploits them
- [x] Trees — BST, balanced trees, tries, heaps, and what each is actually for
- [x] Graphs — representations, traversal, shortest path, topological sort
- [x] Probabilistic Structures — Bloom filters, HyperLogLog, count-min sketch

**Wave AL3 — Algorithms Worth Knowing**
- [x] Sorting & Searching — the classics, and why your language picked the one it did
- [x] Divide & Conquer, Greedy, Dynamic Programming — recognising which applies
- [x] String Algorithms — matching, edit distance, and where regex fits
- [x] Randomised Algorithms — sampling, reservoir sampling, Monte Carlo
- [x] Algorithm Interview Patterns — mapped to the site's coding-interview card

**Wave AL4 — Operating System Theory**
- [x] Processes, Threads & Scheduling — context switches and what they cost
- [x] Virtual Memory — paging, TLB, page faults, and swap's bad reputation
- [x] Concurrency Primitives — mutexes, semaphores, condition variables, atomics
- [x] Deadlock & Livelock — the four conditions, detection, prevention
- [x] Filesystems From the Inside — inodes, journaling, and crash consistency

**Wave AL5 — Computer Architecture**
- [x] Instruction Execution — fetch/decode/execute, pipelining, branch prediction
- [x] Caches & the Memory Hierarchy — L1 to disk, and the numbers every engineer should know
- [x] Speculative Execution & Its Security Cost — Spectre/Meltdown, explained properly
- [x] Number Representation — two's complement, IEEE-754, and the bugs each causes
- [x] Instruction Sets — x86-64 vs ARM64 vs RISC-V, and why the shift is happening

**Wave AL6 — Languages, Compilers & Runtimes**
- [x] How a Compiler Works — lexing, parsing, IR, optimisation, codegen
- [x] Interpreters, Bytecode & JIT — the spectrum from Python to the JVM
- [x] Type Systems — static/dynamic, strong/weak, inference, and what types buy you
- [x] Garbage Collection Deep — mark-sweep, generational, pauses, tuning
- [x] Undefined Behaviour & Memory Safety — the class of bug behind most CVEs

**Wave AL7 — Distributed Systems Theory**
- [x] Time in Distributed Systems — clocks, causality, Lamport and vector clocks
- [x] Consensus — Paxos and Raft, explained without the paper
- [~] Consistency Models — linearizable, sequential, causal, eventual
- [x] Failure Detection & the FLP Result — why "is it down?" has no perfect answer
- [~] Idempotency, Exactly-Once & the Truth — what is actually achievable

### TRACK AM — Mathematics for IT, Security & AI  (→ `cs`)

~5 waves, ~25 cards. Only the mathematics that pays rent, each card anchored to
a place it already shows up on the site.

**Wave AM1 — Numbers, Logic & Bases**
- [~] Binary, Hex & Bit Manipulation — masks, shifts, flags; subnetting revisited — **covered by 'Number Representation — Two's Complement, IEEE-754 & the Bugs Each Causes' in cs and the subnetting cards in net**
- [x] Boolean Algebra — truth tables, De Morgan, and firewall/query logic
- [x] Modular Arithmetic — the clock maths behind hashing, checksums and crypto
- [x] Sets & Relations — the formal spine of SQL joins and access control
- [x] Proof Techniques for Engineers — invariants, contradiction, counterexample

**Wave AM2 — Probability for Defenders**
- [x] Probability Fundamentals — independence, conditional probability, expectation
- [x] Bayes' Theorem — base rates, and why a 99%-accurate detector still floods the SOC
- [x] Distributions That Matter — normal, Poisson, power-law, long tails in latency
- [x] Sampling & Confidence — what a percentile really claims, and sample-size sanity
- [x] Birthday Paradox & Collisions — hash collisions, GUID reuse, key spaces

**Wave AM3 — Statistics for Operations**
- [x] Descriptive vs Inferential — the mistake most dashboards make
- [x] Percentiles & Latency — why p99 beats the mean, and how to aggregate it wrongly
- [x] Anomaly Detection Maths — z-scores, MAD, seasonality, and false-positive cost
- [x] A/B Testing & Significance — power, p-values, and stopping rules
- [x] Forecasting Capacity — trend, seasonality, and headroom planning

**Wave AM4 — Mathematics of Cryptography**
- [x] Prime Numbers & Factoring — why RSA rests on a hard problem
- [x] Discrete Logarithms & Elliptic Curves — the other hard problem, and why keys shrank
- [x] Entropy & Randomness — measuring it, and where implementations lose it
- [~] Information Theory Basics — Shannon entropy, compression, password strength — **shipped as part of 'Entropy & Randomness — Measuring It, and Where Implementations Lose It'**
- [x] Lattices, Gently — the hard problem post-quantum cryptography moved to

**Wave AM5 — Mathematics for Machine Learning**
- [x] Vectors & Embeddings — similarity, cosine distance, and what a dimension means
- [x] Matrices & Linear Transformations — the operation a GPU spends its life doing
- [x] Derivatives & Gradient Descent — how a model actually learns
- [x] Loss Functions & Optimisation — what the model is being told to minimise
- [x] Dimensionality & the Curse — why high-dimensional intuition fails

### TRACK AN — Hardware, Electronics & Embedded  (→ new `hw` domain)

~6 waves, ~30 cards. The physical layer, from a bench repair to a soldered board.

**Wave AN1 — Electronics Fundamentals** — shipped; `hw` domain scaffolded. See the session record.
- [x] Voltage, Current & Resistance — Ohm's law with worked IT examples
- [x] Power & Thermals — watts, heat, and why the PSU calculation matters
- [x] Components — resistors, capacitors, diodes, transistors, and reading a schematic
- [x] Signals → *Signals — Analogue, Digital, Noise & the Grounding Problem*. The noise and
  grounding half is the bulk of it, as the note asked, and aliasing is carried across into
  monitoring — a metric sampled every five minutes cannot represent a thirty-second event, and will
  draw a smooth line through spikes it never saw.
- [x] Test Gear — multimeter, oscilloscope, logic analyser: what each answers

**Wave AN2 — PC Hardware Deep** — shipped into `hw`.
- [x] Motherboard Anatomy — chipsets, lanes, headers, and the block diagram
- [x] CPU & Cooling — sockets, TDP, thermal paste, throttling diagnosis
- [x] Memory Deep — channels, ranks, timings, ECC, and diagnosing bad RAM
- [x] Storage Interfaces — SATA/NVMe/PCIe lanes, and where the bottleneck really is
- [x] Power Supplies — rails, efficiency ratings, sizing, and failure symptoms — inside
  *Power &amp; Thermals*, where the sizing calculation and the failure-symptom table both live

**Wave AN3 — Diagnosis & Repair** — shipped into `hw`.
- [x] Systematic Hardware Troubleshooting — isolate, swap, minimum viable system
- [x] POST, Beep Codes & Diagnostic LEDs — reading a machine that will not boot
- [x] Intermittent Faults — heat, vibration, marginal power, and how to reproduce them
- [x] Soldering & Rework — through-hole and SMD basics, and knowing when not to
- [x] Data Recovery Triage — when to stop and send it to a lab

**Wave AN4 — Peripherals & the Office Estate** — shipped into `hw`.
- [x] Displays — panel types, scaling, colour, multi-monitor and docking pitfalls
- [x] Printers & MFPs — the technologies, drivers, print servers, and secure release
- [x] Docks, USB-C & Thunderbolt — power delivery, alt modes, and the compatibility mess
- [x] Input Devices & Accessibility Hardware — switches, trackballs, ergonomic kit
- [x] Conference Room Technology — the AV stack, and why it always breaks

**Wave AN5 — Embedded & Single-Board** — shipped into `hw`. Track AN is now complete except for
one AN1 item.
- [x] Microcontrollers vs SBCs — Arduino vs Raspberry Pi, and choosing correctly
- [x] GPIO, I²C, SPI & UART — talking to the physical world
- [x] Firmware Basics — bootloaders, flashing, JTAG/SWD, bricking and recovery
- [x] Real-Time Constraints — RTOS, determinism, and why Linux is not always right
- [x] Home Lab Hardware — a genuinely useful build, at three budgets

**Wave AN6 — Hardware Security** — shipped into `sec`, not `hw`. See the session record
*Track AN6: hardware and firmware device security* at the end of this file. The `hw` domain
does not exist yet and these five items are security material that a security domain reader
needs whether or not an electronics domain is ever built; parking them behind a domain that
may never be scaffolded was the worse choice.
- [x] Hardware Root of Trust — TPM, secure enclaves, measured boot, attestation
- [x] Firmware & Supply-Chain Attacks — UEFI implants, Option ROMs, vendor trust — split across
  *Firmware Update Mechanisms* (the attack path) and *Counterfeit &amp; Tampered Hardware* (vendor trust)
- [x] Physical Attacks — evil maid, DMA attacks, cold boot, chip-off forensics — *The Hardware Attack Surface*
- [x] Hardware Hacking Tools — Bus Pirate, logic analysers, JTAG; authorised use only — *Firmware
  Extraction &amp; Analysis*, framed as authorised assessment work throughout
- [~] Defending Physical Access — port control, chassis intrusion, screen locks that hold — the
  defensive half is inside *The Hardware Attack Surface*; the estate-management depth (DMA port
  policy, chassis intrusion switches at fleet scale) is still open and belongs with `endpoint`
- [x] **Added beyond the plan:** Media Sanitisation &amp; Disposal — the decommissioning end of the
  same hardware lifecycle, and a genuine zero-mention void

---

## PART 2 — FRONTIERS

### TRACK AP — Post-Quantum & Cryptographic Migration  (→ `sec`)

~3 waves, ~15 cards. The migration is live now; "harvest now, decrypt later"
makes it an operational problem, not a research one.

**AP1 was already built (Track J's *Post-Quantum Cryptography* card); AP2 & AP3 core
written — 2 cards into `sec`.** `sec` 52→54.

- [x] AP1 threat & standards → *Post-Quantum Cryptography — Harvest Now, Decrypt Later* (Track J: Shor/Grover, ML-KEM/ML-DSA, hybrid, what doesn't break)
- [x] AP2 the migration (inventory, crypto-agility, CBOM, PKI, roadmap) → *Doing the PQC Migration — Inventory, Crypto-Agility & the Roadmap*
- [x] AP3 adjacent crypto (ZKP, homomorphic, MPC, threshold, confidential computing) → *Adjacent Cryptography — ZKPs, Homomorphic Encryption, MPC & Confidential Computing*
- [x] **Depth, re-audited:** both named items shipped as new cards rather than as depth on the
  existing three, which stay as the concept-level entry points. *Certificate &amp; PKI Migration —
  Chains, HSMs &amp; the Devices That Will Never Update* and *Reading a Cryptographic Claim
  Critically — Vendor Slides &amp; "Military-Grade"*. `sec` 84 → 86.

**Wave AP1 — The Threat & the Standards** ⟵ see the shipped-note above
- [ ] Quantum Computing for Security People — qubits, Shor, Grover, and what actually breaks
- [ ] Harvest Now, Decrypt Later — which of today's data has a long enough shelf life to care
- [ ] The NIST PQC Standards — ML-KEM, ML-DSA, SLH-DSA, and what each replaces
- [ ] Hybrid Key Exchange — running classical and post-quantum side by side
- [ ] What Does *Not* Break — symmetric crypto, hashes, and the Grover correction

**Wave AP2 — Doing the Migration**
- [ ] Cryptographic Inventory — finding every place you use crypto, including the forgotten ones
- [ ] Crypto-Agility — designing so the next algorithm swap is a config change
- [ ] CBOM — a cryptographic bill of materials, and how it differs from an SBOM
- [ ] Certificate & PKI Migration — chains, hardware, and the long tail of embedded devices
- [ ] A Migration Roadmap — sequencing by data lifetime and by system replaceability

**Wave AP3 — Adjacent Cryptography**
- [ ] Zero-Knowledge Proofs — the concept, and the small number of real IT uses
- [ ] Homomorphic Encryption — computing on ciphertext, and the current cost
- [ ] Secure Multi-Party Computation & Threshold Signatures — splitting trust
- [ ] Confidential Computing — TEEs, enclaves, attestation, and the trust you still extend
- [ ] Reading a Cryptographic Claim Critically — the marketing tells to distrust

### TRACK AQ — Emerging Platforms & Connectivity  (→ `net` / `ops`)

~4 waves, ~20 cards. Kept deliberately practical: what an operator would have to
support if the business bought it tomorrow.

**AQ1 & AQ2 cores written — 2 cards into `net`.** Edge and modern connectivity were
absent (5G/satellite/IoT-radios only in passing). AQ3 (AR/VR/spatial) is the most
speculative and fastest-ageing; left for on-demand. `net` 55→57.

- [x] Modern Connectivity (5G, private cellular/CBRS, satellite/LEO, LPWAN/Zigbee/Thread/Matter) → *Modern Connectivity — 5G, Private Cellular, Satellite & IoT Radios*
- [x] Edge Computing + CDN function-at-edge + fleet mgmt + offline-first + edge security → *Edge Computing — What It Is Once the Marketing Is Removed*
- [ ] Remaining (narrower/speculative): AR/VR/XR, headset management, digital twins, spatial-data privacy, frontier-pilot evaluation — follow on demand

**Wave AQ1 — Edge & Distributed Compute** ⟵ see the shipped-note above
- [ ] Edge Computing — what it is once the marketing is removed, and when latency justifies it
- [ ] CDN Compute & Function-at-Edge — running logic in the POP
- [ ] Managing Fleets of Edge Devices — updates, drift and observability without a datacenter
- [ ] Offline-First Design — the constraint edge and field work share
- [ ] Edge Security — physical exposure, key management, and lateral movement risk

**Wave AQ2 — Modern Connectivity**
- [ ] 5G for Enterprises — what changed, network slicing, and the realistic use cases
- [ ] Private Cellular & CBRS — when Wi-Fi is genuinely the wrong tool
- [ ] Satellite Internet — LEO constellations, latency, and where it fits in a WAN
- [ ] LPWAN & IoT Radios — LoRaWAN, Zigbee, Thread, Matter; range vs power vs bandwidth
- [ ] Choosing a Connectivity Mix — a decision table for a distributed site

**Wave AQ3 — Immersive & Spatial**
- [ ] AR/VR/XR in the Enterprise — training, field service, and the honest adoption record
- [ ] Managing Headsets — enrolment, updates, hygiene, and the support model
- [ ] Digital Twins — the useful definition, and the data pipeline behind one
- [ ] Spatial Data & Privacy — what a room-scanning device actually records
- [ ] Evaluating a Frontier Pilot — the criteria that stop a demo becoming a commitment

**Wave AQ4 — Automation at the Physical Layer**
- [ ] Robotics & Warehouse Automation for IT — the systems, the networks, the failure modes
- [ ] Building Management Systems — HVAC, access, lighting on the corporate network
- [ ] Smart Buildings & the IoT Attack Surface — segmentation as the primary control
- [ ] Drones & Field Sensors — data volume, chain of custody, airspace rules
- [ ] Supporting Non-Standard Devices — the runbook for kit that has no MDM

### TRACK AR — Physical Security, Investigations & Insider Threat  (→ `sec` / `ops`)

~4 waves, ~20 cards. The half of security that is not on the network.

**AR1–AR3 core written — 3 consolidated cards into `sec`.** Physical security, insider
threat and investigations had only passing mentions; no dedicated cards. `sec` 49→52.

- [x] Physical Security Systems (access control, cloning, CCTV, mantraps, environmental) → *Physical Security Systems — Access Control, CCTV & the Facility Layers*
- [x] The Insider Threat Model + behavioural indicators + SoD + offboarding + programme → *The Insider Threat Programme — Malicious, Negligent & Compromised*
- [x] Investigations + evidence handling + interviewing + working with legal + report → *Internal Investigations & Evidence Handling — Staying in Your Lane*
- [x] AR4 OSINT/attack-surface (defensive) → largely covered by `threat`/`redteam` OSINT cards
- [ ] Remaining (narrower): datacenter facility specifics, credential-cloning deep, CCTV evidentiary detail, insider-programme build-out, interview technique — follow on demand

Cross-linked to the SF-312 clearance card and the digital-forensics card.

**Wave AR1 — Physical Security Systems** ⟵ see the shipped-note above
- [ ] Access Control Systems — badges, readers, controllers, anti-passback, tailgating
- [x] Credential Cloning — why 125 kHz prox is not a control, and what to move to
- [ ] CCTV & Video Management — retention, coverage, evidentiary quality, privacy limits
- [ ] Datacenter & Facility Security — layers, mantraps, visitor control, delivery bays
- [ ] Environmental Controls & Monitoring — power, cooling, water, fire suppression

**Wave AR2 — Insider Threat**
- [ ] The Insider Threat Model — malicious, negligent, compromised; each needs a different control
- [ ] Behavioural Indicators — and the ethical line around monitoring people
- [ ] Separation of Duties & Least Privilege in Practice — beyond the slide
- [x] Offboarding as a Security Control — the checklist and its failure modes
- [ ] Building an Insider Threat Programme — legal, HR and IT together

**Wave AR3 — Investigations**
- [ ] Running an Internal Investigation — scope, authorisation, and staying in your lane
- [ ] Evidence Handling — chain of custody, imaging, hashing, contemporaneous notes
- [ ] Interviewing & Statements — what IT should and absolutely should not do
- [ ] Working With Legal, HR & Law Enforcement — the handoffs and their timing
- [ ] Writing an Investigation Report — findings, evidence, limits, no speculation

**Wave AR4 — OSINT & Attack-Surface Discovery (defensive)**
- [x] Mapping Your Own Exposure — domains, certificates, cloud, code, people
- [x] Credential Exposure Monitoring — breach data, paste sites, and responsible use
- [x] Executive & VIP Exposure — data brokers, doxxing risk, protective steps
- [x] Brand & Impersonation Monitoring — lookalike domains, fake apps, takedowns
- [x] Turning Findings Into Work — from a scary spreadsheet to a prioritised backlog

---

## PART 3 — THE BUSINESS OF IT  (→ new `biz` domain)

### TRACK AS — IT Finance, Vendors & Procurement

~5 waves, ~25 cards. Organisational money, not personal money.

**Wave AS1 — The Money Model**
- [x] CapEx vs OpEx — and why the cloud migration changed the conversation
- [x] Building an IT Budget — run vs grow vs transform, and defending each line
- [x] TCO Modelling — the costs that never appear on the quote
- [x] Chargeback & Showback — making consumption visible without starting a war
- [x] Business Case Writing — the one-page version an executive will actually read

**Wave AS2 — Buying Well**
- [x] Requirements Before Vendors — writing them so the demo cannot dazzle you
- [x] RFI / RFP / RFQ — running a fair process that gets a real answer
- [x] Evaluating a Vendor — financial health, roadmap, support model, references
- [x] Proof of Concept Design — success criteria agreed *before* the trial starts
- [x] Negotiation for IT Buyers — timing, leverage, and what is actually discountable

**Wave AS3 — Contracts & Licensing**
- [x] Reading a Contract as an Engineer — the clauses that bite operations
- [x] SLAs, Credits & What They Are Really Worth — an outage refund is not a control
- [x] Software Licensing Models — per-user, per-device, core-based, consumption
- [x] Surviving a Licence Audit — preparation, evidence, and the true-up conversation
- [x] Exit Clauses & Lock-In — data export, transition assistance, and the migration you will do

**Wave AS4 — Cost Control in Operations**
- [~] Cloud FinOps — showback, rightsizing, commitment discounts, anomaly alerts — **already carded as 'Cloud Cost Control — Budgets, Tags & Rightsizing' in cloud and 'FinOps — Cloud Cost Management' in devops**
- [x] SaaS Sprawl — discovery, consolidation, and reclaiming unused seats
- [x] Hardware Refresh Economics — when replacing beats maintaining
- [x] The Cost of Downtime — modelling it credibly enough to fund resilience
- [x] Technical Debt as a Financial Argument — translating it into language that funds it

**Wave AS5 — Governance of Spend**
- [~] Vendor Risk Management — security review, concentration risk, fourth parties — **already carded three times in grc, including 'Third-Party Risk — Your Security Is Only as Strong as Your Vendors'**
- [~] Asset Management End to End — procure → deploy → maintain → retire → dispose — **already carded as 'Asset & Configuration Management — A CMDB That Stays True' in ops**
- [x] Portfolio & Prioritisation — deciding what *not* to do, defensibly
- [~] Benefits Realisation — checking afterwards whether it did what the case claimed — **shipped as a section of 'The Business Case — One Page an Executive Will Actually Read'**
- [x] Reporting to the Board — three slides, no jargon, no surprises

### TRACK AT — Leading Technical Teams

~5 waves, ~25 cards. Complements the individual-contributor ladder in `eng`.

**Wave AT1 — The Transition**
- [x] From Engineer to Manager — what you actually stop doing
- [x] The First 90 Days Leading a Team — listen, map, stabilise, then change
- [x] Delegation — the levels, and why "I'll just do it" is a trap
- [x] Your Calendar Is the Strategy — where a manager's time really goes
- [x] Keeping Technical Enough — staying credible without taking the work back

**Wave AT2 — People**
- [x] One-to-Ones That Are Worth Having — structure, cadence, and what not to use them for
- [x] Feedback & Difficult Conversations — specific, timely, and survivable
- [x] Performance Management — the honest version, including managing someone out
- [x] Career Development for Your Reports — growth plans that are not just promotion
- [x] Retention — why good people leave, and the ones you can prevent

**Wave AT3 — Hiring**
- [x] Writing a Job Description That Attracts the Right Person
- [x] Designing an Interview Loop — signal per hour, and reducing bias
- [x] Technical Assessment Without Hazing — realistic tasks, fair scope
- [x] Reference Checks & Offers — closing well, and the counter-offer conversation
- [x] Onboarding — the 30/60/90 that produces a contributor, not a spectator

**Wave AT4 — Running the Work**
- [x] Planning Without Theatre — roadmaps, capacity, and honest estimates
- [~] Prioritisation Under Pressure — saying no with a reason attached — **already carded as 'Portfolio & Prioritisation — Deciding What Not to Do, Defensibly' in eng and 'Difficult Conversations — Angry Users, VIP Pressure & Saying No' in ops**
- [x] Project Management for Technical Leads — the minimum viable process
- [~] Managing Incidents as a Leader — comms, decisions, and protecting the responders — **already carded as 'Incident Command — Running a Major Incident Without Chaos' in ops**
- [~] Metrics for Engineering Teams — what DORA does and does not tell you — **already carded as 'DORA Metrics — Measuring Delivery Performance' in devops**

**Wave AT5 — Organisation & Influence**
- [x] Team Topologies — stream-aligned, platform, enabling, complicated-subsystem
- [x] Conway's Law in Practice — shaping the org to get the architecture you want
- [x] Managing Up — giving your leadership what they need to back you
- [x] Cross-Team Politics — alliances, escalation, and picking battles
- [x] Building a Culture Deliberately — rituals, defaults, and what you tolerate

### TRACK AU — Enablement, Training & Technical Influence

~4 waves, ~20 cards. Teaching as a function, not as a personality trait.

**Wave AU1 — Designing Learning** — shipped into `career`.
- [x] How Adults Actually Learn — relevance, practice, feedback, spacing
- [x] Curriculum Design — objectives, sequencing, and cutting the nice-to-know
- [~] Building a Lab — repeatable, resettable, and cheap enough to keep — `career` already carries
  three home-lab cards (*Building a Home Lab*, *Home Lab – Practicing IT Skills*, *Building a Home
  Lab Without Breaking the Bank*)
- [x] Assessment That Means Something — beyond a multiple-choice quiz — same card as curriculum
  design, because assessment is step 2 of backward design and cannot be taught after it
- [x] Measuring Training — behaviour change, not attendance — the four-level table closing the
  adult-learning card

**Wave AU2 — Delivering It** — shipped into `career`.
- [x] Running a Workshop — pacing, energy, and rescuing the room when it stalls
- [x] Live Demos That Do Not Fail — rehearsal, fallbacks, recorded escape hatch
- [x] Screencasts & Async Video — scripting, recording, editing, and length discipline — same card
  as demos; both are "showing rather than telling", and the fallback recording links them
- [x] Facilitating a Retrospective or Tabletop — neutrality and the hard question
- [x] Teaching a Tool You Just Learned → shipped into `career`. One step ahead is the *best*
  distance to teach from, because the expert has forgotten what was confusing; the credibility
  problem is solved by saying where you are rather than by waiting for mastery.

**Wave AU3 — Documentation as Infrastructure** — shipped into `career`, except where noted.
- [x] Documentation Types — tutorial, how-to, reference, explanation (and mixing them up)
- [~] Runbooks That Work at 3 a.m. — carded in `ops` as *Writing Runbooks That People Actually
  Follow*, with the testing half added in this session's resilience wave
- [x] Docs-as-Code — review, versioning, CI checks, and ownership — same card as documentation types
- [x] Keeping Documentation Alive — review triggers, owners, and deleting the dead — same card
- [x] Diagrams That Explain — the small number of shapes worth using

**Wave AU4 — Influence Beyond Your Team** — shipped into `career` as one card.
- [x] Writing a Proposal People Say Yes To — problem, options, recommendation, cost
- [x] Presenting to Executives — the pyramid principle, and the first thirty seconds
- [x] Speaking at a Conference — CFP writing, talk structure, rehearsal
- [~] Community & Open Source Contribution — carded in `career` as *Building in Public — Your
  Reputation Compounds*
- [x] Building an Internal Community of Practice — starting one that survives month three

### TRACK AV — Consulting, Contracting & Independent Practice

~4 waves, ~20 cards. Complements `lifestyle`'s freelance-tax card with the craft
of running the work.

**Wave AV1 — Positioning** — shipped into `career`.
- [x] Consultant vs Contractor vs Staff Augmentation — three different businesses
- [x] Choosing a Niche — why specificity wins work — same card, because the niche only makes sense
  once you know which of the three businesses you are in
- [x] Pricing — hourly, day rate, fixed price, value-based; and their risk profiles
- [x] Finding Clients — referrals, partners, content, and the honest cold-outreach maths
- [x] The Proposal & Statement of Work — scope, exclusions, acceptance criteria

**Wave AV2 — Delivering** — shipped into `career`.
- [x] Discovery — the first two weeks that determine the engagement
- [x] Managing Scope — change control without becoming the difficult one — same card as discovery;
  scope creep is what happens when discovery was skipped
- [x] Working Inside Someone Else's Politics — reading the room you were dropped into
- [x] Handover & Enablement — leaving a client better, not dependent — same card as politics, since
  both are about the internal team's relationship to your presence
- [x] The Assessment Report — findings, risk-ranked recommendations, and an owner per item

**Wave AV3 — The Business Side** — partly shipped into `career`.
- [x] Cash Flow & Runway — invoicing, payment terms, and the late-payer problem
- [x] Insurance, Liability & Entity Choice — the boring protections that matter — same card, framed
  as orientation with an explicit note that jurisdictions differ and this is not legal advice
- [x] Contracts for Independents — IP, indemnity, non-solicit, limitation of liability — same card
- [x] Subcontracting & Partnering → *Subcontracting & Partnering — Growing Past Your Own Hours*
- [x] Knowing When to Stop — bad clients, bad engagements, exiting cleanly — the closing section of
  the business-side card

**Wave AV4 — Specialist Practices**
- [x] Running a Security Assessment Engagement → *Running a Security Assessment — Rules of Engagement to Final Debrief*
- [x] Fractional & Advisory Roles → *Fractional & Advisory Roles — vCISO, Fractional IT Director & the Boundary Problem*
- [x] Expert Witness & Forensic Work → *Expert Witness & Forensic Work — Impartiality, Standards & Report Discipline*
- [x] Training & Workshop Delivery as a Product → *Training & Workshop Delivery as a Product — Packaging What You Know*
- [x] Productising a Service → *Productising a Service — From Bespoke Hours to a Repeatable Offer*

---

## PART 4 — SITE: TRUST & LONGEVITY (engineering, not content)

The site is now large enough that its main risk is no longer "too little
content" — it is **content that quietly goes stale and nobody notices**. Azure AD
became Entra ID; SCCM became MECM; CASP+ became SecurityX. Every one of those
renames is already somewhere in `data/`.

### TRACK AX — Content Freshness & Accuracy

*Shipped-note: three of the eight below are done — freshness metadata, volatility tags and the
rename registry. A fourth measured itself away. Read the ticks.*

- [x] **Per-topic freshness metadata** — `data-reviewed="YYYY-MM"` on every `.topic`, derived from
  `git blame` by `tools/stamp_freshness.py` with mechanical commits excluded, `--verify` in CI, and
  1,310 stamps current across 29 files. The badge and the oldest-50 report were dropped
  deliberately: the stamp drives the volatility warnings below, and a date on every card is noise
  rather than information.
- [x] **Volatility tags** — shipped as `<span class="volatile" data-checked="YYYY-MM">` around the
  specific claim rather than as a tag on the whole topic, which is the better shape: what goes stale
  is a console name or a limit, not a card. Applied at the claim level, styled with a dotted
  underline and a tooltip carrying the check date.
- [x] **Rename/deprecation registry** — `data/renames.json`, 25 renames, plus
  `tools/check_renames.py` in CI. It reads prose only, allows a mention that is explicitly
  historical ("formerly Azure AD") or sits beside the new name, and carries an `allow` list for
  strings that are still literally correct — "Azure AD Connect" outlived "Azure AD", and
  `twitter:card` is the meta tag's actual name. Found and fixed nine real uses across six files.
- [~] **Link rot check in CI** — nothing to check. The whole site contains **one** external link
  and **one** `href="#"` across 1,369 topics; it is a self-contained reference that deliberately
  makes no third-party requests. Measured rather than built, same as Track AJ's link checker.
- [x] **Fact-anchor comments** — the convention is
  `<!-- fact: <claim> | source: <where> | checked: YYYY-MM -->` immediately before the element
  making the claim, documented in `CONTRIBUTING.md` and validated by `tools/check_volatility.py`
  (a missing field or a non-`YYYY-MM` date fails CI). Five applied to real claims to start it off,
  including the plan's own example — the 93-day platform-metric retention.
- [x] **Per-domain changelog** — an **Updated** row on each domain's landing card: the month the
  domain was last reviewed and the topics reviewed then, as links. Generated by `build.py` from the
  `data-reviewed` stamps rather than from git history at build time, which keeps the build offline
  and deterministic and guarantees the answer matches what `stamp_freshness.py` actually wrote.
- [x] **Contradiction check** — `tools/check_contradictions.py`, in CI. It checks the two things
  that are genuinely mechanical: a hand-written acronym expansion that disagrees with
  `acronyms.json`, and the ports the site attaches to a service. It deliberately does **not** attempt
  "contradictions" in general — a limit or a retention period needs to know what the number is
  *about*, which no regex supplies, and the docstring says so rather than pretending. Found eight
  real disagreements on its first run.
- [x] **Screenshot-dated warnings** — implemented as the existing `.volatile` span applied to the
  console *name*, which is the thing that changes; ten added across `endpoint`, `infra` and `m365`,
  taking the site from 33 dated claims to 43. `check_volatility.py` also reports topics naming a
  vendor console with no dated span — a queue of 14, reported and deliberately not gated, because
  most of them mention a console without making a claim about it ("Microsoft Management Console"
  has not moved in twenty years).

### TRACK AY — Content Model & Build Evolution

Recorded with trade-offs rather than as a recommendation, because it is the kind
of change that is easy to start and expensive to abandon.

- [x] **Evaluate a structured content model** — **evaluated; the answer is no.** The decision rule
  was "only worth it if Tracks AG/AK actually need topic-level structured data". Both tracks are now
  complete and the evidence is in the session record below: every consumer built — study decks,
  quizzes, exam mode, learning paths, related topics, landing cards, print packs — needed *ids and
  small external JSON*, not structured topics. One consumer, the Markdown export, genuinely wanted
  structure, and it cost ~120 lines and three bugs rather than 1,375 migrations.
- [~] **Incremental path if that is a yes** — moot, since the answer is no. The evaluation named a
  much smaller change that gets the same benefit: convert the **78 div-built pseudo-tables** to real
  `<table>` markup. That is where the export's special cases live, and it is 78 elements against
  1,883 real tables. Until then the Markdown export knows their class names — `kc-row`, `nist-row`,
  `perm-row`, `url-codec-row`, `layer`, `dt-row` — so they export as rows rather than as one line
  per cell. Naming them in the converter is the cheap half; converting the markup is the half that
  also fixes screen-reader output.
- [x] **Topic ID stability contract** — written into `CONTRIBUTING.md` as *Topic IDs are a
  contract*, with the table of what does and does not move an id, why it matters (permalinks and
  five `localStorage` key prefixes), the rule to prefer parts over new domains, and the
  build-and-compare-bytes proof the `script` split used.
- [x] **Split `data/script.html`** — done exactly as specified: six ordered parts building into the
  *same* domain, concatenated by `build.py` in filename order.
  `script.01-references` (25) · `02-beginner` (36) · `03-python` (41) · `04-it-automation` (10) ·
  `05-platform` (26) · `06-admin-automation` (7). Every slug, permalink and stored progress key is
  untouched, and the built `index.html` is **byte-identical** to the pre-split build — which is the
  proof, not a hope. `domain_files()` in `lint_content.py` is now the one place that answers "where
  does a domain live", and six tools use it.
- [x] **Build determinism** — `tools/check_determinism.py` builds twice and compares the bytes of
  `index.html` and `sw.js`, in CI and in `make check`. Verified to fail on a planted `time_ns()`
  before being wired in. It is also what makes "the built page is byte-identical", the proof the
  `script` split relied on, mean anything.
- [x] **Archive `patches/`** — 54 one-shot injection scripts, 1.8 MB, untouched since 2026-07-04
  and superseded by editing `data/` directly. Tagged `archive/patches-2026-08` and deleted;
  recoverable with `git checkout archive/patches-2026-08 -- patches/`.
- [x] **A `make` entry point** — `make` builds, `make check` runs every static gate in
  fastest-failing order, `make test` drives the browser, `make all` does all three, `make stamp
  ONLY=<domain>` restamps one domain, `make help` lists them. `make` rather than `just`, because
  `make` is already on the machine. The ordering inside `build` is documented in the file: the
  acronym domain is generated from the dictionary, the annotator rewrites content using it, and
  `build.py` assembles what both produced.
- [x] What Detection Engineering Is — and why it split off from SOC analysis
- [x] The Detection Lifecycle — idea → hypothesis → logic → test → deploy → tune → retire
- [x] Detection Requirements — writing one before writing the rule
- [~] The Pyramid of Pain Applied — choosing what to detect on, and its cost to the attacker — **already carded as 'Detection Tuning & the Pyramid of Pain'**
- [x] Coverage vs Noise — the trade every rule makes, made explicit

**Wave BA2 — Data Before Rules**
- [x] Log Source Inventory — knowing what you actually collect, and at what fidelity
- [x] Data Normalization — OCSF, ECS, ASIM; why a schema decides your query
- [x] Telemetry Gaps — proving a detection cannot fire, before you promise it does
- [x] Log Volume & Cost — sampling, filtering, and the detections cost quietly kills
- [x] Enrichment — asset, identity and threat context that turns an alert into a decision

**Wave BA3 — Writing Detections**
- [~] Sigma as an Interchange Format — writing once, deploying to several backends — **already carded as 'Sigma — Write Detections Once, Run Anywhere'**
- [x] Detection-as-Code — Git, review, CI, and versioned rules
- [x] Writing a Good Rule — specificity, false-positive analysis, the tuning fields
- [x] Behavioural vs Signature Detections — worked examples of both for one technique
- [x] Correlation & Sequencing — when a single event genuinely is not enough

**Wave BA4 — Testing Detections**
- [x] Unit-Testing a Detection — synthetic events and expected verdicts
- [x] Atomic Red Team & Emulation for Validation — proving the rule fires on the real thing
- [x] Detection Regression — the rule that silently stopped working after a log change
- [x] Measuring Detection Quality — precision, recall, alert-to-incident ratio, time-to-detect
- [~] Purple-Team Feedback Loop — closing the gap the exercise found — **already carded as 'Purple Teaming — Closing the Detection Gap'**

**Wave BA5 — Running the Programme**
- [x] ATT&CK Coverage Mapping — honest heat maps, and the lie of "100% coverage"
- [x] Detection Backlog & Prioritisation — threat model in, rules out
- [x] Rule Retirement — deleting detections without losing the reason they existed
- [x] Documentation for Responders — the runbook that ships *with* the rule
- [x] Detection Engineering Interview — what the role is actually assessed on

### TRACK BB — Adversary Emulation & Purple Teaming  (→ `redteam` / `blueteam`)

~4 waves, ~20 cards. Authorized-use framing throughout, and every offensive card
pairs with the detection it should trigger — the site's existing rule.

**Wave BB1 — Emulation Foundations**
- [x] Emulation vs Simulation vs Penetration Testing — three different questions
- [x] Building a Threat Profile — picking an adversary that is relevant to *you*
- [x] Emulation Plans — CTID plans, and writing your own from intel
- [x] Rules of Engagement for Emulation — scope, safety, deconfliction, kill switch
- [x] Lab Design for Emulation — a range that is safe to break

**Wave BB2 — Running an Exercise**
- [x] Purple Team Mechanics — the room, the roles, the cadence
- [x] Technique-by-Technique Execution — run, observe, record, adjust
- [x] Detection Gaps in Real Time — the value that only appears when both teams watch together
- [x] Evidence Capture — screenshots, timestamps, telemetry references
- [x] The Debrief — findings that turn into backlog items, not a scorecard

**Wave BB3 — Automation**
- [x] Breach & Attack Simulation Tools — what they do well, and their blind spots
- [x] Atomic Testing at Scale — scheduled, safe, continuous validation
- [x] CI for Security Controls — treating control efficacy as a test suite
- [x] Safe Payloads — proving execution without doing damage
- [x] Avoiding Emulation Theatre — when a green dashboard means nothing

**Wave BB4 — Reporting & Value**
- [x] Writing the Emulation Report — narrative, timeline, gaps, recommendations
- [x] Mapping Findings to Controls & Owners — every gap gets a name and a date
- [x] Measuring Programme Improvement Over Time — the metric that survives scrutiny
- [x] Communicating Risk to Leadership — without either alarmism or false comfort
- [x] Building the Business Case for Purple — funding the second exercise

### TRACK BC — Cloud-Native & Kubernetes Security  (→ `cloud` / `blueteam`)

~5 waves, ~25 cards. The site teaches Kubernetes operationally; this is the
attack and defence surface.

**Wave BC1 — The Kubernetes Threat Model** — shipped into `cloud`.
- [x] What an Attacker Sees — the control plane, the kubelet, etcd, the workloads
- [x] The Four Cs — cloud, cluster, container, code — same card; the model is diagnostic and needs
  the surfaces beside it to be worth anything
- [x] Kubernetes RBAC Deep — verbs, resources, and the escalation paths people miss
- [x] Service Accounts & Token Projection — the credential every pod carries
- [x] etcd & Control-Plane Exposure — the game-over surfaces — the surfaces table in the threat-model
  card, ranked by consequence

**Wave BC2 — Workload Hardening** — shipped into `cloud`, except where noted.
- [x] Pod Security Standards — privileged/baseline/restricted, and enforcing them
- [x] Container Breakout Paths — privileged pods, hostPath, hostPID, capabilities — same card as
  PSA, because the profiles only make sense once you know what they are refusing
- [~] Admission Control — OPA/Gatekeeper and Kyverno, and policy-as-code — already carded as
  *Policy as Code — OPA/Rego &amp; Kyverno* in `devops`; the new card cross-references it and adds
  the PSA-validates-but-cannot-mutate ordering trap
- [~] Image Security — minimal bases, non-root, read-only filesystems, distroless — carded in
  `devops` (*Container Security*) and `linux`
- [x] Secrets in Kubernetes → *Secrets in Kubernetes — Base64 Is Not Encryption, and the Options
  That Are*. The options comparison the note asked for, plus the clause people miss: permission to
  create a pod in a namespace is permission to read every Secret in it.

**Wave BC3 — Network & Identity** — shipped into `cloud`, except where noted.
- [x] Network Policies — default-deny, and why almost nobody has it
- [x] Service Mesh Security — mTLS, authorization policy, and the complexity cost — same card, so
  the "network policy first, mesh only for the second column" judgement is stated once
- [x] Workload Identity — federating pods to cloud IAM without long-lived keys — inside the
  service-account token card, where the audience field explains the mechanism
- [x] Ingress & API Exposure → *Ingress & API Exposure — The Gateway as a Control Point*, including
  the Ingress / Gateway API / service mesh division of labour and the 502 debugging order
- [x] Multi-Tenancy — namespaces are not a security boundary; what to do instead

**Wave BC4 — Runtime & Detection** — shipped into `cloud`.
- [x] Runtime Security — Falco/Tetragon, eBPF-based detection in the cluster
- [x] Audit Logs — what the API server records, and the queries worth saving — same card as
  runtime, because the point is that the two answer different questions
- [x] Container Forensics — investigating something that no longer exists
- [x] Drift & Immutability — detecting a changed container in a declarative world — the GitOps-diff
  row in the incident-response card
- [x] Incident Response in Kubernetes — isolate, snapshot, evict, and preserve evidence

**Wave BC5 — Serverless & Managed Services** — shipped into `cloud`. Track BC is complete except
for the three items noted in BC2 and BC3 above.
- [x] Serverless Threat Model — event injection, over-permissive roles, cold-start secrets
- [x] Managed Service Trust Boundaries — what the provider secures, and precisely what you do
- [x] IaC Security Scanning — catching the misconfiguration before it deploys
- [x] Cloud Detection Engineering — CloudTrail/Activity Log/Audit Logs as detection sources
- [x] Cloud Incident Response — snapshotting, credential revocation, blast-radius containment

### TRACK BD — API & Identity-First Security  (→ `sec` / `web`)

~4 waves, ~20 cards. The perimeter moved to the API and the token; the site's
coverage has not caught up.

**Wave BD1 — API Security** — shipped into `sec`.
- [x] OWASP API Top 10 — what differs from the web Top 10, and why
- [x] Broken Object-Level Authorization — the single most common real API bug
- [~] Authentication vs Authorization at the API — where each belongs — already carded at concept
  level in *API Security – OAuth2, JWT &amp; Token-Based Authentication*; the API-specific half is
  inside the BOLA card, where it belongs
- [x] Rate Limiting & Abuse — quotas, burst, and distinguishing abuse from success
- [x] API Inventory & Shadow APIs — you cannot protect the endpoint you forgot

**Wave BD2 — Tokens Done Right** — closed. Three cards shipped into `sec`; see both BD session
records.
- [~] JWT Security — algorithm confusion, `none`, key confusion, expiry, revocation — `alg: none`
  and the revocation problem are already in the existing `sec` API card; algorithm and key
  confusion are in the federation card. A standalone JWT card would have been a third telling
- [x] OAuth 2.1 & PKCE — the flows that remain, and the ones that were removed
- [x] Token Lifetime & Revocation — refresh, rotation, and the logout that does not
- [~] Machine-to-Machine Auth — client credentials, mTLS, workload identity — carded as
  *Non-Human Identity* earlier this session, which is where the credential-choice table lives
- [x] Secrets vs Tokens vs Keys — a taxonomy that prevents the wrong control

**Wave BD3 — Identity as the Control Plane**
- [~] Identity-First Security — what changes when identity is the perimeter — carded twice as
  *Zero Trust — Never Trust, Always Verify* (`sec`) and *Zero Trust – "Never Trust, Always Verify"
  Explained Simply* (`net`); the identity-as-perimeter argument is what those cards are
- [~] ITDR — detecting identity attacks: token theft, consent phishing, MFA fatigue — carded as
  *Identity Threat Detection &amp; Response (ITDR)* in `blueteam`; this session's federation and
  consent-phishing cards cross-reference it
- [~] Conditional Access Patterns — a policy set that is coherent rather than accreted — carded as
  *Conditional Access &amp; Device Compliance* (`endpoint`) and *Entra ID — Sign-In &amp; Conditional
  Access Troubleshooting* (`cloud`)
- [~] Privileged Access Done Properly — tiering, PAWs, break-glass, JIT elevation — carded as
  *Privileged Access Management — Vaulting, Just-in-Time &amp; Session Recording*; tier-zero and
  privileged-access-workstation material is in `infra`
- [x] Non-Human Identity — service principals, workload identities, and the sprawl nobody owns

**Wave BD4 — Federation & Third Parties** — shipped into `sec`.
- [x] SAML & OIDC Attack Surface — golden SAML, signature confusion, reply-URL abuse
- [x] SCIM & Provisioning Risk — the integration that quietly holds write access — inside
  *Third-Party App Governance*, which is where the reader will look for it
- [x] OAuth Consent Phishing — the attack that needs no password
- [x] B2B & Guest Access — external identities without opening the tenant — same card; guests and
  integrations are the same governance gap seen from two directions
- [x] Third-Party App Governance — reviewing, restricting and revoking app permissions

### TRACK BE — Software Supply Chain & Integrity  (→ `eng` / `sec`)

~4 waves, ~20 cards. The SBOM cards exist; the discipline around them does not.

**Wave BE1 — Understanding the Chain** — shipped into `eng`, not `sec`. See the session record.
- [x] Where a Build Actually Comes From — every input, including the ones you forgot
- [x] Historic Supply-Chain Attacks — what each one actually exploited — written as a pattern table
  inside the same card rather than a card of case studies, because the shared structure is the
  lesson and the individual incidents date badly
- [x] Dependency Risk — transitive depth, typosquatting, abandoned packages
- [x] Build System as a Target — the CI runner is production-adjacent — *Securing the Pipeline*
- [x] Trust Decisions — pinning, vendoring, mirrors, and their maintenance cost — split where the
  reader meets each: pinning's cost with dependency risk, mirrors with internal registries

**Wave BE2 — Provenance & Attestation** — shipped into `eng`.
- [x] SLSA Levels — what each one actually requires you to change
- [x] Signing & Sigstore — keyless signing, transparency logs, verification
- [x] Attestations & in-toto — statements about how an artifact was produced — same card; the
  who/how distinction only lands when the two are taught together
- [x] Verifying at Deploy Time — admission policy that refuses unsigned artifacts
- [x] Reproducible Builds — the property, the practical obstacles

**Wave BE3 — Operating It** — shipped into `eng`.
- [x] SBOM in Practice — generating, storing, and actually querying one
- [x] VEX — saying "we ship it but are not affected", credibly
- [x] Dependency Update Strategy — automated bumps without a broken main branch
- [x] Vulnerability Triage for Dependencies — reachability, exploitability, real priority
- [x] Responding to a Compromised Dependency — the first hour

**Wave BE4 — Internal Supply Chain** — shipped into `eng`, except where noted.
- [x] Securing the CI/CD Pipeline — secrets, runners, forks, and injection via pull request
- [~] Artifact Repositories — promotion, retention, immutability, access — already carded as
  *Artifact &amp; Registry Management* in `devops`; the new card cross-references it
- [x] Internal Package Registries — and the dependency-confusion class of attack
- [x] Golden Images & Base Layer Hygiene — one place to patch, one place to break — inside
  *Securing the Pipeline*, where the rebuild-schedule point has something to attach to
- [~] Developer Workstation Trust — the machine that signs your commits — the endpoint half is
  carded in `endpoint`; the commit-signing half is a genuine small gap, left open

### TRACK BF — Privacy Engineering  (→ `grc` / `eng`)

~4 waves, ~20 cards. Distinct from GRC: GRC proves compliance, privacy
engineering builds systems that do not need much proving.

**Wave BF1 — Privacy as a System Property** — shipped into `grc`. See the session record.
- [x] Privacy vs Security — overlapping, not the same, and where they conflict — reframed as
  privacy *engineering* vs privacy *compliance*, which is the distinction the reader of this site
  actually needs, since the compliance half is already four cards in this domain
- [x] Data Minimisation — the control that removes whole classes of risk
- [x] Purpose Limitation in a Data Warehouse — hard, and why it is usually skipped
- [x] Data Inventory & Mapping — knowing where personal data actually flows
- [~] Privacy by Design — the seven principles, translated into engineering decisions — the
  principle is carded in *Privacy Regulations*; the translation is distributed through this whole
  cluster rather than restated as a list

**Wave BF2 — Technical Controls** — shipped into `grc`, except where noted.
- [~] De-identification — anonymisation vs pseudonymisation, and re-identification risk — the
  techniques are carded in *Data Privacy Techniques*; the legal consequence of the
  pseudonymisation/anonymisation distinction is in the tokenisation card, which is where it bites
- [~] Differential Privacy, Practically — already carded in *Data Privacy Techniques* and `ai`
- [x] Tokenisation & Format-Preserving Encryption — protecting data that must stay usable
- [x] Access Control for Personal Data — purpose-bound access and audit — inside the purpose
  limitation card, because purpose-bound access is what purpose limitation means operationally
- [x] Retention & Deletion That Actually Deletes — backups, replicas, caches, logs

**Wave BF3 — User-Facing Obligations** — shipped into `grc`.
- [x] DSARs — building a subject-access process that scales
- [x] Right to Erasure — the engineering problem behind the legal right — split across the deletion
  card (the mechanism) and the DSAR card (the process); the legal shape is already in *Privacy Law*
- [x] Consent & Preference Management — storing and honouring it across systems
- [x] Cookies & Tracking — the technical reality behind the banner — same card
- [x] Cross-Border Transfers — the mechanisms, and their architectural consequences — inside the
  flow-mapping card, framed as the architecture decision it actually is

**Wave BF4 — Privacy in New Systems** — partly shipped.
- [~] Privacy in Machine Learning — training data, memorisation, model inversion — carded in `ai`
  (*Adversarial AI &amp; AI Threats*) and named in *Data Privacy Techniques*
- [x] Telemetry Design — useful product analytics that collect less
- [x] Third-Party Data Sharing → *Third-Party Data Sharing — Contracts, Technical Limits &
  Verification*, written to supply exactly the missing half: what you send, how to reduce it, and
  how to verify rather than assume.
  written
- [x] Privacy Incident Response — when it is a breach, and the clock that starts
- [x] Privacy Review as a Process — lightweight enough that teams use it — the trigger table in the
  first card

---

## PART 2 — PLATFORM & RESILIENCE CRAFT

### TRACK BG — Platform Engineering & the Internal Developer Platform  (→ `eng` / `ops`)

~4 waves, ~20 cards. The discipline that grew out of DevOps once "you build it,
you run it" met a hundred teams.

**Wave BG1 — The Premise** — shipped into `devops`.
- [x] Why Platform Engineering Exists — the cognitive-load argument, stated honestly
- [x] Platform as a Product — users, roadmap, adoption, and the option to not use it
- [x] Golden Paths — paved roads that are genuinely faster than going around
- [x] Thinnest Viable Platform — resisting the urge to build a cloud on the cloud — same card as
  golden paths, because the two are the same discipline pointed at build and at scope
- [x] Platform Team Anti-Patterns — the gatekeeper, the ticket queue, the abstraction leak — inside
  *Platform as a Product*, where each anti-pattern reads as a product failure

**Wave BG2 — Building It** — shipped into `devops`, except where noted.
- [x] Developer Portals — service catalogue, ownership, scorecards
- [x] Self-Service Infrastructure — templates, modules, and guard rails over gates
- [x] Environment Management — ephemeral environments, seeding, cost control — same card; the
  guard-rail argument and the ephemeral-environment payoff belong together
- [~] Paved-Path CI/CD — a pipeline teams inherit rather than copy — the pipeline material is
  already carded in `devops` (*CI/CD*, *GitHub Actions*, the CI landscape card); the
  inherit-rather-than-copy point is the golden-path card's contents table
- [~] Policy as Code in the Platform — compliance that happens by default — carded as
  *Policy as Code — OPA/Rego &amp; Kyverno* in this domain

**Wave BG3 — Operating It** — shipped into `devops`.
- [x] Platform SLOs — the platform is production for its users
- [x] Versioning & Migrating Consumers — changing a platform without breaking teams
- [x] Support Model — office hours, escalation, and not becoming a help desk — same card as SLOs
  and migration, which are the three things a platform owes its users once it has any
- [x] Documentation as the Product Surface — where adoption is actually won or lost — the closing
  section of *Measuring Platform Success*, because it is the highest-leverage adoption lever
- [x] Measuring Platform Success — adoption, lead time, and the counter-metrics

**Wave BG4 — Developer Experience** — shipped into `devops`, as one card.
- [x] Local Development That Matches Production — containers, seeds, fakes
- [x] Build & Test Speed as a Feature — the compounding cost of a slow pipeline
- [x] Inner vs Outer Loop — where a developer's day actually goes
- [x] Onboarding to First Commit — measuring and shortening it
- [x] Toil Audits — finding the manual work worth automating, and the work that is not

### TRACK BH — Observability Engineering  (→ `ops`)

~4 waves, ~20 cards. Beyond the monitoring cards: designing for questions you
have not thought of yet.

**Wave BH1 — Foundations** — shipped into `ops`.
- [~] Monitoring vs Observability — the distinction that is not just marketing — already carded as
  *Known Unknowns vs Unknown Unknowns* in `ops`; the new wide-events card restates the distinction
  where it becomes actionable rather than definitional
- [x] The Three Signals & Their Costs — metrics, logs, traces; what each is bad at
- [x] Cardinality — the concept that decides your observability bill
- [x] Structured Events — wide events as an alternative to three separate pipelines — same card as
  the three signals, because wide events only make sense as an answer to their weaknesses
- [x] Instrumentation Strategy — what to instrument first in an unfamiliar system

**Wave BH2 — OpenTelemetry in Practice** — shipped into `ops`.
- [x] OTel Architecture — API, SDK, collector, exporters
- [x] Distributed Tracing Deep — spans, context propagation, sampling strategies — the sampling half
  is its own card; spans and context propagation are already carded in
  *Distributed Tracing &amp; OpenTelemetry*, and propagation reappears in the correlation card
- [~] Metrics With OTel — instruments, views, and avoiding cardinality explosions — the cardinality
  half is the cardinality card, which is the part that matters; instruments and views are reference
  material better read from the specification than from a card
- [x] The Collector as a Control Point — filtering, redaction, routing, cost control
- [x] Migrating an Existing Stack — incrementally, without a big-bang cutover — the six-step
  sequence in the collector card

**Wave BH3 — Using It** — shipped into `ops`.
- [x] Debugging With Traces — the workflow that finds an unknown-unknown
- [x] Correlating Signals — trace to log to metric, and the IDs that make it possible
- [x] Dashboards Worth Keeping — the small number that answer real questions
- [~] Alerting on Symptoms, Not Causes — carded twice already in `ops`; burn-rate alerting, which is
  the part that was missing, is in the error-budget card
- [x] Observability-Driven Development — shipping instrumentation with the feature — the closing
  section of the instrumentation card

**Wave BH4 — SLOs as a Practice** — shipped into `ops`.
- [x] Choosing SLIs — the signal that matches the user's experience
- [x] Setting an SLO That Survives — negotiated, achievable, and meaningful
- [x] Error Budgets & Policy — what actually happens when it is spent
- [ ] Reporting Reliability — to engineering, and separately to the business — still open; the
  upward-reporting craft is carded in `eng` (*Reporting Upward*) but not the reliability-specific
  version
- [x] When SLOs Fail — the organisational reasons, not the technical ones

### TRACK BJ — Resilience & Chaos Engineering  (→ `ops` / `eng`)

*(Skipping "BI" — it reads as "B1".)*

~4 waves, ~20 cards.

**Wave BJ1 — Designing for Failure** — shipped into `ops`, except where noted.
- [x] Failure Modes & Effects Analysis for Systems — thinking it through before it happens
- [x] Blast Radius Design — bulkheads, cells, shuffle sharding
- [x] Graceful Degradation — the feature that turns off instead of the site going down
- [~] Dependency Failure — timeouts, retries with jitter, circuit breakers revisited — carded in
  `eng` as *Resilience Patterns — Circuit Breaker, Retry &amp; Timeout*; the new degradation card
  cross-references it
- [x] Capacity & Load Shedding — choosing what to drop before you are forced to — same card as
  degradation, because shedding requests and shedding features are one decision

**Wave BJ2 — Chaos Engineering** — mostly pre-existing; the organisational half shipped.
- [~] The Method — steady-state hypothesis, blast radius, abort conditions — carded in `ops` as
  *Chaos Engineering — Breaking Things on Purpose*
- [~] Your First Experiment — safe, small, and in production eventually — same card ("Don't Start
  Here" is its closing section)
- [~] Fault Injection Techniques — latency, errors, resource exhaustion, dependency loss — same card
- [x] GameDays — running one that people volunteer for twice
- [x] Chaos Maturity — from an annual exercise to continuous verification — same card, as a
  six-stage path that says plainly where most teams should stop

**Wave BJ3 — Incidents as a System** — mostly pre-existing.
- [~] Incident Command Deep — roles, handovers, and long incidents — carded in `ops` as
  *Incident Command — Running a Major Incident Without Chaos*
- [~] Communication During an Incident — carded in `ops` as *Writing for Users — Outage Notices
  &amp; Status Pages People Trust*
- [~] Blameless Postmortems That Change Something — carded in `ops` as *Writing a Postmortem People
  Actually Learn From*; the analytical half it was missing is in the new resilience-engineering card
- [x] Learning From Near-Misses — the free lessons most organisations throw away
- [x] Incident Metrics — what MTTR does and does not tell you — same card

**Wave BJ4 — Human Factors** — shipped into `ops`, except where noted.
- [x] Resilience Engineering — the field, and why "human error" is a bad root cause
- [x] Alert Fatigue — measuring it, and treating it as a reliability problem
- [~] On-Call Health — load, compensation, and the sustainable rotation — carded in `ops` as
  *On-Call Done Humanely*
- [x] Runbook Quality — testing your runbooks the way you test code — same card as alert fatigue;
  both are about operational artifacts decaying silently
- [x] Organisational Memory — keeping what was learned after the people leave

---

## PART 3 — WRITTEN NOW, NOT PLANNED

Everything above is a list. This part is the material itself, because the
binding constraint on this project has changed: there are now 751 planned cards
and one person. Quality per card matters more than another list.

### The card pattern library

Measured across the 2,014 `.concept-card`s currently on the site (counting the
markup each card contains, up to the next card boundary):

| Shape | Share | Notes |
|---|---:|---|
| Prose only | ~50% | The default, and correctly so |
| With a table | ~38% | Reference and comparison material |
| With a code block | ~7% | Commands and syntax |
| Table + code | ~4% | The heaviest cards; use sparingly |
| Grid or SVG | ~1% | Diagrams, used rarely |

Nine patterns cover almost everything worth writing. Each has a job; using the
wrong one is why some cards read as padding.

**1 — Concept card (prose only).** One idea, three to six sentences, no table.
Use when the reader needs a mental model before any detail. *Failure mode:* a
concept card that lists things — that is a table wearing prose.

**2 — Reference table.** `Thing | What it is | Worth remembering`. The workhorse.
*Rule:* always follow it with one sentence of "so what" — the table states
facts, the sentence states the judgement.

**3 — Comparison table.** `— | Option A | Option B`, rows are dimensions.
Use when the reader's real question is "which one". *Rule:* include a row for
how each one *fails*, not only what each one does.

**4 — Decision table.** `Option | Reach for it when`. Shorter than a comparison,
and better when there are more than three options. See *Four Load Balancers, One
Right Answer* in `cloud`.

**5 — Error reference.** `Code | What it actually means | First move`. The
highest-value pattern on the site for operational domains, because it maps the
thing the reader is staring at to the thing they should do. See the Azure and
MECM troubleshooting cards.

**6 — Command toolkit.** A `<pre class="code-block">` where every command is
preceded by a comment saying what question it answers. *Rule:* commands must be
runnable as written; placeholders in `<angle-brackets>`.

**7 — Artifact map.** `Symptom | Where to look | Log`. The diagnostic companion
to the error reference — used by both the MECM and Intune troubleshooting cards.

**8 — Staged flow.** Numbered phases with what happens and what can break at
each. Use for lifecycles: enrolment, boot, a request path, an incident.

**9 — The trap.** A short bolded callout after a table naming the mistake
everyone makes. `<strong class="c-amber">The gotcha:</strong> …`. This is the
pattern readers remember, and the one most often missing.

### How to write a card that earns its place

1. **Lead with what it is for**, not what it is or where it came from. History
   is a sentence, not a paragraph.
2. **One card, one idea.** If the title needs an "and", it is two cards — unless
   the "and" is the point (*"Coder vs Programmer"*).
3. **Every table gets a verdict.** A table without a following judgement sentence
   makes the reader do work you should have done.
4. **Name the failure mode.** The card is more useful for saying what breaks than
   for listing what exists. Vendors write the feature list already.
5. **No marketing verbs.** *Leverages, empowers, seamlessly, robust* — if a
   sentence survives deleting them, delete them.
6. **Numbers need a source or a hedge.** Either cite where a figure comes from,
   or write "roughly". Precision you cannot defend is worse than an estimate.
7. **Write for the person mid-incident**, not the person studying on a Sunday.
   The Sunday reader can follow a card written for 3 a.m.; the reverse is false.
8. **Code must run.** If it was not executed, mark it as illustrative.
9. **Assume the acronym pipeline.** Write acronyms plainly; do not hand-write
   expansions — `tools/annotate_acronyms.py` owns that, and hand-written ones
   get stripped.
10. **Cut the card that only exists for completeness.** A domain with 20 good
    cards beats one with 35 where 15 are filler. This is the hardest rule and
    the one that most protects the site.

### Project risk register

The realistic threats to this project, in likelihood order. Three are already
mitigated by work in this repo; the rest are open.

| Risk | Likelihood | Impact | Mitigation | State |
|---|---|---|---|---|
| **Content goes stale** — vendor renames, dead consoles, changed limits | High | High | Track AX shipped: freshness stamps, volatile spans, fact anchors, rename registry, vendor-console queue | **Partly** — the tooling exists and covers **51 dated claims**. Phase 11 established the denominator is not mechanically countable, so coverage is unknown by construction |
| **Scope paralysis** — the open-item count keeps rising | High | Medium | The menu framing, and the ordered first-ten in each phase | **Open, and worse.** Phases 7–11 added roughly 96 cards, 244 deepenings, 23 merges, 9 tools and 5 verification waves. The mitigation is the ordering, not the count |
| **Progress data loss** — everything is `localStorage`; clearing the browser wipes it | Medium | Medium | Phase-4 Track AG: export/import | **Mitigated** — session 10 shipped export/import with merge, replace and preview |
| **Page weight** — `index.html` is 3.4 MB and grows with every wave | Medium | Medium | Measured in session 14 — it is not slow. `tools/page_budget.py` enforces size and element budgets in CI; lazy loading stays unbuilt until a budget is hit | **Mitigated** |
| **Generated-file drift** — `acronym.html` / `index.html` committed stale | Medium | Low | CI already rebuilds and fails on drift; `--check` mode on the annotator | **Mitigated** |
| **Slug churn** — renaming a topic silently breaks permalinks and progress | Medium | Medium | Track AY shipped: `slug-aliases.json`, `renames.json`, `check_renames.py` in CI, and the ID contract written into `CONTRIBUTING.md` | **Mitigated** |
| **Accuracy drift** — a confident wrong card is worse than no card | Medium | High | Fact anchors, contradiction checking, and the acronym ratchets | **Partly, and re-scored upward.** One session found **eight wrong acronym expansions** live on the site, three of them in topic titles. Every one was well-formed markup that passed every gate |
| **Bus factor of one** — one maintainer holds all the context | Medium | High | The plan itself, `CONTRIBUTING.md`, and tooling that encodes conventions | Partly |
| **Markup rot** — inconsistent classes and inline styles accumulate | Medium | Low | Phase-4 Track AJ content linter | **Mitigated** — `tools/lint_content.py` runs in CI and tracks a warning trend |
| **Burnout** — a 140-session backlog written by someone with a day job | Medium | High | Ship what matches current work; no deadline; the menu framing | Open |
| **Hosting/domain lapse** | Low | High | Static site, works from `file://`, in Git — recoverable by design | **Mitigated** |
| **Tooling single point of failure** — the acronym pipeline is now load-bearing | Low | Medium | Idempotent, `--check` mode, CI-verified, documented in README | **Mitigated** |

### How you would know the site is working

No analytics, by design — so the measures have to be ones you can observe
directly.

- **The lookup test.** When a real question comes up at work, is the site faster
  than a web search? If not for a given domain, that domain is decorative.
- **The onboarding test.** Could you hand a new colleague a domain and a learning
  path and have them be useful? Track AG's paths make this testable.
- **Time-to-card.** When something new lands (a rename, a new service, a CVE
  class), how long until a card exists? Weeks is fine; never is the failure.
- **Volatile-topic freshness.** Percentage of *volatile* topics reviewed in the
  last twelve months. Stable topics are excluded deliberately — see Track AX.
- **Your own usage.** The `reviewed:` and `bookmark:` keys already record it. A
  dashboard (Track AG) turns that into the most honest signal available: which
  domains you actually return to.
- **Build health.** CI green, zero console errors, build reproducible, generated
  files never stale. Already true; keep it true.

---

## Phase 6 in numbers

| | |
|---|---|
| Content tracks | 9 (BA–BJ) |
| Waves | 38 |
| Cards | 190 |
| New domains | **0** |
| Written now, not planned | Card pattern library · authoring rules · risk register · success measures |

## Cumulative position

| | Topics | Domains |
|---|---:|---:|
| Today | 900 | 20 |
| + Phase 3 outstanding | 1,107 | 20 |
| + Phase 4 | 1,372 | 23 |
| + Phase 5 | 1,607 | 26 |
| + Phase 6 | 1,797 | 26 |

**Total remaining backlog: 897 content cards and 44 engineering items.**

That number is now large enough to be its own risk, which is why it is in the
register above. The plan is finished; the correct next move is not to plan
further but to **ship one wave** — and the shortlist for which one is at the end
of Phase 5.

---

# Execution Handbook — turning 897 cards into shipped work

> **This is not Phase 7.** Phase 6 closed by saying the subject planning is
> finished and the next move is to ship a wave, and that still holds — another
> list of card titles would be padding. What the plan genuinely lacks is the
> layer between "897 items" and "a commit": the ordering constraints, a
> per-domain view, and at least one wave specified in enough detail that it can
> be executed without re-deciding anything. That is what this section is.

## 1. Ordering constraints

Most of the backlog can be done in any order. These are the exceptions — the
places where doing B before A costs real rework.

| Do this first | Before this | Why |
|---|---|---|
| **AH — chip grouping** | The 24th domain (`cs`) | The filter bar is one scrolling row of 21 chips today. Three more (`infra`, `m365`, `itsm`) is survivable; six is not. Retrofitting grouping after six new chips means re-testing every chip. |
| **AX — freshness metadata** | Any large content wave | Stamping ~900 topics from `git log` is one script today. After another 500 topics, the same script runs on 1,400 and the backfill is less accurate because more topics have been touched for unrelated reasons. |
| **AJ — duplicate-slug guard** | Any wave adding 20+ topics | `script.js` silently suffixes colliding slugs (`-2`), which shifts permalinks. Cheapest to catch at build time, and near-impossible to unpick later. |
| **AY — split `data/script.html`** | Tracks P and AC (28 cards queued into `script`) | 719 KB in one file is already the hardest place to work. Adding 28 cards first makes the split bigger and riskier. |
| **AG — export/import progress** | Telling anyone to rely on the study tools | Progress is `localStorage` only. Recommending flashcards before there is a backup path is setting up a data-loss complaint. |
| **Domain scaffold** | That domain's first wave | `scaffold_domain.py` must run before `data/{id}.html` has content, or `build.py` warns and skips it. |
| **`data/acronyms.json` entries** | The wave that uses them | The annotator only expands terms it knows. Add the acronym, then write the cards, then run the annotator — in that order. |
| **AK — performance budget** | AK — lazy loading | Set the budget while the number is still known and defensible (3.15 MB), so the lazy-loading work has a target to hit rather than a vibe. |

Everything else is genuinely parallel. In particular, no content track blocks
any other content track.

## 2. Per-domain queue

Derived from the plan's own track→domain annotations. "Queued" splits a track's
cards evenly across the domains it names.

| Domain | Topics now | Queued | After | Tracks targeting it |
|---|---:|---:|---:|---|
| `ops` | 68 | 72 | 140 | AC, AQ, AR, BG, BH, BJ |
| `sec` | 43 | 70 | 113 | J, AP, AR, BD, BE |
| `endpoint` | 13 | 60 | 73 | Y, AD |
| `net` | 55 | 50 | 105 | Q, AB, AQ |
| `blueteam` | 37 | 48 | 85 | BA, BB, BC |
| `eng` | 36 | 40 | 76 | BE, BF, BG, BJ |
| `grc` | 28 | 30 | 58 | L, BF |
| `script` | 137 | 28 | 165 | P, AC |
| `threat` | 25 | 20 | 45 | K |
| `ai` | 34 | 20 | 54 | O |
| `lifestyle` | 59 | 20 | 79 | S |
| `redteam` | 43 | 20 | 63 | M, BB |
| `linux` | 56 | 15 | 71 | N |
| `cloud` | 49 | 12 | 61 | BC |
| `pentest` | 29 | 10 | 39 | M |
| `military` | 23 | 16 | 39 | T |
| `web` | 35 | 10 | 45 | BD |
| `shortcut` | 37 | **0** | 37 | — |
| `data` | 40 | **0** | 40 | — |
| `acronym` | 53 | n/a | — | generated |

Plus five new domains carrying their own tracks: `infra` (V + Z, 60), `m365`
(W, 30), `itsm` (AA, 25), `cs` (AL + AM, 60), `hw` (AN, 30), and `biz`
(AS–AV, 90).

**Two findings worth acting on:**

- **`shortcut` and `data` have nothing queued.** Not an oversight to fix by
  inventing tracks — `data` is genuinely complete at 40 cards (Track H shipped
  in full), and `shortcut` is a productivity grab-bag that does not need depth.
  Record them as **done unless something changes**, and stop feeling the gap.
- **`ops` is the most over-subscribed domain** at 68 → 140. Six tracks point at
  it because "operations" absorbs anything that is neither pure security nor
  pure engineering. Before starting BG/BH/BJ, check whether the platform,
  observability and resilience material would be better as its own domain — the
  Phase-4 rule (≥15 cards, own tooling, a job title) says yes for all three
  combined. That decision should be made **before** 72 cards land, not after.

## 3. The first ten sessions

One session ≈ one wave ≈ one commit. This turns the shortlist at the end of
Phase 5 into something with an order.

| # | Do | Output |
|---|---|---|
| 1 | **AH chip grouping** — group the 21 chips into six categories | `index-shell.html` + `style.css`; no content change |
| 2 | **AX freshness stamp** — script that writes `data-reviewed="YYYY-MM"` on every topic from `git log`, plus an "oldest 50" build report | `tools/stamp_freshness.py`, one-time run committed |
| 3 | **AJ duplicate-slug guard + markup validator** in CI | `tools/lint_content.py`, wired into `build-check.yml` |
| 4 | **Wave Y1 — Intune policy** (spec'd in §4 below) | 5 cards in `endpoint` |
| 5 | **Wave Y2 — Intune applications** | 5 cards in `endpoint` |
| 6 | **AG-1 spaced repetition** (spec'd in §5) | `script.js` + FAB badge |
| 7 | **AG-2 acronym quiz mode** — questions generated from `acronyms.json` | `script.js` |
| 8 | **AH-2 acronym-aware search + density toggle** (spec'd in §6) | `script.js`, `style.css`, `index-shell.html` |
| 9 | **Wave Y3 — Windows servicing & updates** | 5 cards in `endpoint` |
| 10 | **AG-3 export/import progress** | `script.js`; closes the data-loss risk |

After ten sessions: `endpoint` has grown 13 → 28, the study tools are a system
rather than four toys, the navigation survives six more domains, and three of
the open risks in the register are closed. That is a better position than any
ten content waves would leave.

## 4. Worked specification — Wave Y1, "Intune Deep: Policy"

Specified to the point where writing it is transcription, not design. Use this
as the template for spec'ing any other wave.

**Target:** `data/endpoint.html`, appended before `<!-- /domain-body endpoint -->`.
**Badge:** `Intune • Policy`. **Icon per card:** `⚙️ 🥊 🛡️ 📋 🎯`.

| # | Topic name | Pattern (§ Phase 6) | Must contain | The trap to name |
|---|---|---|---|---|
| 1 | Configuration Profiles — Settings Catalog, Templates & Custom | Comparison table | Three-column comparison: settings catalog / template / custom OMA-URI, with rows for *coverage*, *discoverability*, *reporting*, *when it breaks* | Custom OMA-URI has no reporting to speak of — you find out it failed from the device, not the console |
| 2 | Policy Conflicts — Proving Which One Won | Staged flow + error reference | The resolution order, then a per-device diagnosis path: console conflict report → device `MDMDiagnostics` → registry under `Provisioning` | Two profiles setting the same CSP to different values leaves the setting *unset*, not "last writer wins" |
| 3 | Security Baselines Without Breaking the Fleet | Decision table | Baseline vs settings-catalog policy vs GPO parity; a staged rollout ring plan; what to exclude on day one | Applying a baseline at 100% is the single fastest way to lock a fleet out of something |
| 4 | Administrative Templates & ADMX-Backed Policy | Reference table | Which GPO settings exist in Intune, which do not, and the ADMX ingestion path for third-party templates | ADMX-backed policy is not the same surface as the settings catalog; a setting in one may be absent in the other |
| 5 | Assignment Strategy — Users, Devices, Filters & Exclusions | Decision table + trap | User vs device targeting per policy type; filters vs dynamic groups; exclusion precedence | Exclusion always wins over inclusion — the commonest cause of "the policy is assigned but not applying" |

**Acronyms.** Checked against `data/acronyms.json`: `ADMX`, `OMA-URI`, `CSP`,
`MDM`, `MAM`, `RBAC`, `ESP`, `GPO`, `IME`, `TPM`, `BYOD` are all present, and
`CSP`/`ESP` already carry the correct `byDomain` override for `endpoint`.
**Missing and needed before writing:** `ADML` (Administrative Language file),
`COPE` (Corporate-Owned, Personally Enabled), `COBO` (Corporate-Owned, Business
Only), `KFM` (Known Folder Move). Add those four first.

**Sequence:**

```sh
# 1. acronyms first, or the annotator will not expand them
$EDITOR data/acronyms.json          # add ADML, COPE, COBO, KFM
python3 tools/gen_acronym_domain.py

# 2. write the five cards into data/endpoint.html

# 3. annotate, build, verify
python3 tools/annotate_acronyms.py
python3 build.py
python3 -m http.server 8000         # then load and check the console
```

**Done when:** five topics reachable by permalink, zero console errors, search
finds each by title and by an expansion (e.g. searching "Configuration Service
Provider" finds card 2), `tools/annotate_acronyms.py --check` exits 0, and
`git diff --exit-code -- index.html` is clean after a rebuild.

**Commit message shape:** one line naming the wave, then what each card covers
and any acronym or tooling change — the pattern used by the Azure/MECM commits.

## 5. Worked specification — AG-1, spaced repetition

The study FAB already has flashcards, a quiz, a study list and a jump palette.
This adds scheduling, using state that already exists.

**Existing keys** (`script.js`): `reviewed:<id>`, `bookmark:<id>`, `known:<id>`.
**New key:** `srs:<id>` → `{"e":2.5,"i":1,"d":"2026-08-12","n":0}` — ease,
interval in days, due date, repetition count.

**Algorithm — SM-2, reduced.** On grading a card *again / hard / good / easy*:

```
again  → n=0, i=1,            e = max(1.3, e-0.20)
hard   → n+=1, i = max(1, i*1.2), e = max(1.3, e-0.15)
good   → n+=1, i = (n==1 ? 1 : n==2 ? 6 : round(i*e))
easy   → n+=1, i = round(i*e*1.3), e = e+0.15
due    = today + i days
```

**Surface area:**
- Flashcard view gains four grade buttons in place of the current advance.
- The FAB shows a "due today" count; zero means no badge.
- The scope selector gains **Due today** alongside All / domain / Bookmarks.
- A card with no `srs:` entry is treated as new and enters at `n=0`.

**Deliberately not doing:** cross-device sync (see AG export/import), per-card
statistics beyond the four fields, or replacing the existing random flashcard
mode — keep it as "browse" and add "review" beside it.

**Done when:** grading four cards and reloading preserves due dates; the badge
count matches the number of `srs:` entries with `d <= today`; and clearing
`localStorage` degrades to the current behaviour rather than erroring.

## 6. Worked specification — AH-2, acronym-aware search + density toggle

Two changes that share one data source and should ship together.

**A — acronym-aware search.** `runSearch()` currently matches raw text. Before
matching, expand the query through the dictionary:

1. At first search, build `Map<lowercased expansion → [acronyms]>` and
   `Map<acronym → [expansions]>` from the same JSON the annotator uses. The
   built page already contains every expansion inline, so the map can be built
   from the DOM (`.acro-exp` spans) with no new fetch — which keeps `file://`
   working.
2. If the query matches an acronym, also match its expansions, and vice versa.
3. Highlight both forms in results.

**Done when:** searching `Unified Endpoint Management` returns the UEM cards,
searching `UEM` returns them too, and the search still runs under the existing
debounce with no visible delay on a 3.15 MB page.

**B — expansion density toggle.** A header control writing
`localStorage["acro-density"]` and a class on `<body>`:

| Mode | Class | Behaviour |
|---|---|---|
| Always (default) | — | Current behaviour: bracketed expansion inline |
| Hover | `acro-hover` | `.acro-exp { display:none }`; shown on `:hover`/`:focus-within` of the parent, and always shown on touch-only via a media query |
| Off | `acro-off` | `.acro-exp { display:none }` unconditionally |

This is pure CSS plus one preference — no rebuild, no change to the annotator,
and it directly answers the one real cost of the acronym feature: density inside
tables.

**Done when:** the setting survives a reload, the dictionary domain is
unaffected (it has no `.acro-exp` spans), and printing respects the current mode.

## 7. Checklists

These use `☐` rather than task-list checkboxes on purpose: they are reusable,
and every backlog figure in this file is a tally of unchecked task-list boxes.
Ticking a checklist should never move the backlog number.

**Ship a content wave**

☐ Any new acronyms added to `data/acronyms.json` first, with `byDomain` set if the term is ambiguous in that domain
☐ `python3 tools/gen_acronym_domain.py` if the dictionary changed
☐ Cards follow `CONTRIBUTING.md` and use one of the nine patterns
☐ Every table followed by a verdict sentence; the trap named where there is one
☐ `python3 tools/annotate_acronyms.py` then read the diff — check no expansion is wrong for the context
☐ `python3 build.py`
☐ Load `index.html`: zero console errors, each new topic reachable by `#slug`, search finds it
☐ `git diff --exit-code -- index.html` clean after a second build
☐ One commit, CI green

**Scaffold a new domain**

☐ `python3 scaffold_domain.py <id> <icon> "<title>" "<CHIP>" <chipColor> <accent> "<sub>" ctag-general:TAG`
☐ Create `data/<id>.html` with at least one topic before building
☐ Add the chip to its category group (post-AH)
☐ Add a row to the README domain table
☐ Confirm the domain accent colour is legible in both themes

**Before calling it a release**

☐ `tools/annotate_acronyms.py --check` exits 0
☐ `tools/gen_acronym_domain.py` produces no diff
☐ `build.py` twice produces no diff
☐ Headless load in both themes, no console errors
☐ `sw.js` `CACHE_VERSION` bumped if assets changed

## 8. Appendix — subject gaps with no track

Recorded for completeness. None of these justifies a seventh phase; each is a
card or two folded into an existing track if it ever matters.

| Gap | Where it would go | Verdict |
|---|---|---|
| ~~Mainframe & legacy systems (z/OS, COBOL, AS/400)~~ | `infra` | ✅ **Shipped** — *Mainframe & Midrange — Why They Are Still There, and How You Integrate With One*. One card, as the verdict said |
| ~~Reverse engineering & binary analysis~~ | `threat` | ✅ **Already covered** — *Reverse Engineering & Binary Analysis — Reading Code You Don't Have Source For* landed in `threat`, not `redteam`. Audited, not rewritten |
| ~~Accessibility engineering (beyond WCAG basics in `web`)~~ | `web` · `ops` | ✅ **Both halves closed** — assistive-tech testing was already in `ops` (*Accessible IT*); the remediation workflow shipped as *Accessibility Remediation — Working Through an Audit Backlog* |
| ~~Internationalization engineering~~ | `web` | ✅ **Shipped** — *Internationalization (i18n) — Designing for Languages You Do Not Speak*. Still nothing about translating this site |
| Payments & fintech infrastructure | `data` / `grc` | PCI DSS is already covered; the rest is a niche |
| Blockchain & distributed ledger | — | **Rejected.** Low operational relevance to this site's readership, and the security angle is already covered by key management |
| HPC & scientific computing | — | **Rejected.** Different career entirely |
| Video, streaming & media engineering | — | **Rejected.** Same reason |
| ~~Technical SEO & web operations~~ | `web` | ✅ **Shipped** — *Technical SEO Operations — Crawling, Indexing & Migrations Without Losing Traffic*. The existing SEO card was on-page metadata; this is the operational half |

---

## Closing note

The plan is done. Three phases of subject roadmap, one handbook, and a register
of what could go wrong. The remaining risk is not that something was left
unplanned — it is that planning is more comfortable than writing, and this file
is now 897 unwritten cards long.

**Session one is a two-hour job: group the chips.** Start there.

---

# Execution Handbook, Part 2 — the remaining seven session specs

> §3 above lists ten sessions; §4–6 specified three of them. This specifies the
> other seven to the same standard, so that every one of the first ten sessions
> can be started without designing anything first. After this, the plan contains
> no undesigned work for the next ten commits.

## Session 1 — AH-1, group the filter chips

**Problem.** `.filter-inner` is a single `flex-wrap: nowrap` row inside an
`overflow-x: auto` bar, holding 21 chips. Three more domains is tolerable; six
is not.

**Constraint that makes this cheap.** Chips are handled by delegation on
`.filter-bar` (`e.target.closest(".chip")`), and `filter()` only reads
`chip.dataset.domain` and toggles `.hidden` on `.domain-section`. **Neither
function needs to change** — grouping is a markup and CSS job as long as every
chip keeps its class and `data-domain`.

**Design.** Wrap chips in labelled groups inside `.filter-inner`:

```html
<div class="chip-group" data-group="core">
  <span class="chip-group-label">Core IT</span>
  <div class="chip c-net" data-domain="net">🌐 NETWORKING</div>
  …
</div>
```

Six groups, mapping every current and planned domain:

| Group | Domains |
|---|---|
| Core IT | `net`, `linux`, `endpoint`, `cloud`, `shortcut`, *`infra`*, *`m365`*, *`itsm`*, *`hw`* |
| Security | `sec`, `threat`, `grc`, `ops`, `pentest`, `redteam`, `blueteam` |
| Engineering | `eng`, `script`, `web`, `data`, `ai` |
| Human | `lifestyle`, `military`, *`biz`* |
| Reference | `acronym`, *`cs`* |

(*italic* = planned, not yet scaffolded.)

> **Shipped as five groups, not six.** `cloud` went into Core IT rather than
> standing alone — a one-chip group looked like a mistake. And the mobile
> fallback is the original single scrolling row rather than a `<details>`
> collapse: wrapping into five labelled rows made the *sticky* bar 474 px tall
> on a 390 px-wide phone, which is worse than swiping. Desktop is three tidy
> rows at 127 px and no horizontal scroll.

**CSS.** `.filter-inner` becomes `flex-wrap: wrap` with `row-gap: 10px`;
`.chip-group` is a flex row with its own `gap: 6px` and a small uppercase
`--muted` label. Below 720 px, collapse to a `<details>` per group so the bar
stays one or two rows on a phone. `ALL DOMAINS` stays outside any group, first.

**Accessibility.** Give each group `role="group"` and
`aria-label="<group name> domains"`. The chips are already reachable; do not
change their tab order.

**Done when:** every chip still filters, the active state still moves, the bar
is at most two rows at 1280 px and collapsed on mobile, and adding a new chip
means editing one group rather than the whole row.

## Session 2 — AX-1, stamp topic freshness from git history

**Goal.** `data-reviewed="YYYY-MM"` on every `.topic`, plus a report of the
oldest volatile ones.

**The trap that makes a naive version wrong.** `git blame` returns the last
commit that touched each line — and mechanical passes touch nearly every line.
The acronym annotation in this repo modified 2,388 lines across 19 files in one
commit. Blaming naively would report the entire site as freshly reviewed, which
is worse than no metadata at all.

**Fix.** Use git's own mechanism:

```sh
# .git-blame-ignore-revs — mechanical commits only, one SHA per line with a comment
<sha>   # bulk acronym annotation
<sha>   # formatter pass
git blame --line-porcelain --ignore-revs-file=.git-blame-ignore-revs -- data/net.html
```

Also set `blame.ignoreRevsFile` in `.git/config` locally so interactive blame
agrees with the tool.

**Algorithm (`tools/stamp_freshness.py`).**

1. For each `data/*.html` except `acronym.html`, blame once and build
   `line → author-time`.
2. Split the file on `<div class="topic">` to get each topic's line range.
3. `reviewed = max(author-time in range)` → format `YYYY-MM`.
4. Rewrite the opening tag as `<div class="topic" data-reviewed="2026-08">`.
5. Idempotent: strip any existing `data-reviewed` first, exactly as the
   annotator strips its own spans.

**Volatility.** Add `data-volatile="true"` only where it is true. Seed the
candidate list by keyword — *Intune, MECM, Entra, portal, console, pricing,
licence, tier, SKU, version* — and print it for a human to confirm. Do **not**
auto-apply: a wrong volatility tag either creates noise or hides staleness.

**Report (`tools/freshness_report.py`).** Oldest 50 topics that are
`data-volatile="true"`, with domain, title and age in months. Stable topics are
excluded by design — see the Phase-5 rationale.

**Surfacing it.** A quiet `.topic-age` badge on topics older than 18 months,
volatile only, hidden in print. Optional; the report alone earns the session.

**Done when:** running the stamper twice produces no diff, no topic is marked
fresh purely because of a mechanical commit, and the report names topics you
recognise as genuinely stale.

## Session 3 — AJ-1, content linter and duplicate-slug guard

**One script, `tools/lint_content.py`, exit non-zero on error.**

| Check | Level | Rule |
|---|---|---|
| Markup well-formed | error | Parse each `data/*.html` with `html.parser`; no unclosed or stray tags |
| Duplicate slugs | error | Two topics slugifying to the same id |
| Missing `.topic-name` | warn | 90 today; do not fail the build, report the count so it trends down |
| `topic-chevron` | error | The banned variant from `CONTRIBUTING.md` |
| Hand-written `.acro-exp` | error | That class belongs to the annotator |
| Hard-coded hex colour | warn | 148 today; breaks the light theme |
| Inline `style="color:…"` | warn | Use the `c-*` utility classes |
| `ai-table` in a changed file | warn | Prefer `ref-table` for new content |

**Replicating the slug exactly.** `script.js` uses:

```js
s.toLowerCase().replace(/[^\w\s-]/g,"").trim()
 .replace(/[\s_]+/g,"-").replace(/-+/g,"-").slice(0,60) || "topic"
```

In JavaScript `\w` is ASCII-only. Python's `\w` is Unicode-aware by default, so
a naive port keeps accented characters the browser would strip and the two
disagree. **Pass `flags=re.ASCII`.** Titles are ASCII today, so the bug would
lie dormant until the first topic with an accent — exactly the kind of drift a
guard exists to prevent.

Uniqueness must be computed the same way too: `script.js` walks
`.domain-section` in document order and suffixes collisions `-2`, `-3`. The
linter should report the *pair*, not just the duplicate.

**Wire into CI** after the existing acronym checks in `build-check.yml`.

**Done when:** the linter passes on `main` as it stands, deliberately breaking
one rule in a scratch commit fails CI, and the warn counts are printed as a
single summary line so they can be tracked over time.

## Session 5 — Wave Y2, "Intune Deep: Applications"

**Target:** `data/endpoint.html`. **Badge:** `Intune • Apps`.

| # | Topic name | Pattern | Must contain | The trap to name |
|---|---|---|---|---|
| 1 | Win32 App Packaging — `.intunewin` End to End | Staged flow + command toolkit | Content prep tool → upload → install/uninstall commands → detection → requirements → dependencies → supersedence | Supersedence and dependencies are evaluated per-device at assignment time; a loop between two apps stalls both silently |
| 2 | Install Contexts — System vs User | Comparison table | Which context each install type runs in, where each writes, and how detection differs per context | A user-context app assigned to a device group installs for whoever happens to log in first — and reports success for the device |
| 3 | Store, LOB & Enterprise App Catalog Apps | Decision table | Five delivery vehicles with update ownership, offline capability and version pinning per row | Store apps update themselves; if you need a pinned version, Win32 is the only honest choice |
| 4 | App Protection Policies — MAM Without Enrolment | Reference table + trap | Protected app list, data-transfer rules, conditional launch, wipe scope | App protection only covers apps that are MAM-aware; a PDF opened in an unmanaged viewer leaves the boundary |
| 5 | Application Troubleshooting — Reading the IME Log | Artifact map + error reference | `IntuneManagementExtension.log` and `AgentExecutor.log`; the detection-vs-enforcement split; the error codes from the MECM card that also apply here | Exit code 0 with "not detected" is always the detection rule, never the installer — the same trap as MECM, worth repeating here |

**Acronyms:** `IME`, `LOB`, `MAM`, `MSI`, `PKG` present. **Check before
writing:** `MSIX` (present), and add `PSADT` (PowerShell App Deployment Toolkit)
if it is mentioned.

**Cross-link:** card 5 should reference the MECM deployment-troubleshooting
topic rather than restating it — same failure, two consoles.

## Session 7 — AG-2, acronym quiz mode

**Why this one is worth a session.** The existing quiz generates multiple-choice
questions from topic titles and has to invent distractors. `acronyms.json` is
1,021 entries of structured question/answer pairs that already exist.

**Question types.**

| Type | Prompt | Answer | Distractors |
|---|---|---|---|
| Expand | "UEM stands for…" | `annotate` or `m[0].e` | Three expansions from the **same subject area** |
| Contract | "Which acronym means *Unified Endpoint Management*?" | `a` | Three acronyms of similar length from the same area |
| Disambiguate | "In a networking context, MAC means…" | The `byDomain` value | The entry's other meanings |

**Rules that keep it fair.**
- Only the *disambiguate* type may use multi-meaning entries; the other two
  skip anything with `m.length > 1`, or accept any listed meaning.
- Distractors must come from the same `c` (subject area) — otherwise "which of
  these is a storage term" gives it away.
- Never use two acronyms in one question that differ only by case (`IoC` /
  `IOC`) — that is a typography test, not knowledge.
- Entries flagged `noAnnotate` are still fair game: they are ambiguous in prose,
  not unknowable.

**Data source.** Read `acronyms.json` at build time and emit it as a
`<script type="application/json" id="acronym-data">` block in `index.html`, so
the quiz works over `file://` with no fetch. That block is also what Session 8's
acronym-aware search should consume — build it here, use it twice.

**Done when:** 20 questions generate with no repeats, every distractor is
plausible, and the scope selector can limit to one subject area.

## Session 9 — Wave Y3, "Windows Servicing & Updates"

**Target:** `data/endpoint.html`. **Badge:** `Intune • Servicing`.

| # | Topic name | Pattern | Must contain | The trap to name |
|---|---|---|---|---|
| 1 | Windows Update for Business — Rings, Deferrals & Deadlines | Staged flow | A four-ring model with population, deferral, deadline and grace period per ring | A deadline with no grace period reboots people mid-meeting; the grace period is the control that decides whether users trust you |
| 2 | Feature vs Quality vs Driver Updates | Comparison table | Cadence, risk, rollback window and control surface for each of the three pipelines | They are three independent pipelines — pausing quality updates does not pause drivers |
| 3 | Windows Autopatch — What It Takes Over | Decision table | What Autopatch owns, what stays yours, prerequisites, and the exit path | It manages the rings for you, which means your carefully built rings stop being the source of truth |
| 4 | Update Compliance Reporting | Artifact map | Where the truth lives: Intune reports, Update Compliance, and the device's own history | "Not applicable" and "unknown" are not the same as compliant, and most dashboards blur them |
| 5 | Emergency Patching — Advisory to Verified | Staged flow + checklist | Triage the CVE, pick the vehicle, ring-skip criteria, verification query, and the comms | Skipping rings for a genuine emergency is correct; skipping *verification* never is |

**Acronyms:** `WUfB`, `CVE`, `KEV`, `SLA` all present. Add `LCU` (Latest
Cumulative Update) and `SSU` (Servicing Stack Update) before writing.

## Session 10 — AG-3, export and import progress

**Goal.** Close the "progress data loss" risk in the register, and give the only
realistic cross-device path without a backend.

**Shape.**

```json
{
  "format": "techref-progress",
  "version": 1,
  "exported": "2026-08-05T12:00:00Z",
  "counts": { "reviewed": 128, "bookmark": 34, "known": 71, "srs": 71 },
  "data": {
    "reviewed:aaa-framework": "1",
    "bookmark:azure-troubleshooting-playbook": "1",
    "srs:uem-engineer": { "e": 2.5, "i": 6, "d": "2026-08-19", "n": 3 }
  }
}
```

**Export.** Collect keys with the known prefixes plus the notepad key. Download
as `techref-progress-YYYY-MM-DD.json` via a Blob URL — no network, works over
`file://`.

**Import.** Three explicit modes, chosen in the dialog:

| Mode | Behaviour |
|---|---|
| Merge (default) | Union of keys; for `srs:` entries present in both, keep the **later** due date so nothing is re-surfaced unexpectedly |
| Replace | Clear the known prefixes first, then write the file |
| Preview | Show counts per category and what would change, write nothing |

**Guard rails.** Validate `format` and `version` before touching anything;
refuse unknown versions rather than guessing. Ignore any key that does not match
a known prefix — an imported file must not be able to write arbitrary
`localStorage`. Show the counts and require a confirm click.

**Done when:** export → clear site data → import restores every counter exactly;
merge on a device with existing progress loses nothing; and a hand-edited file
with a bad version is rejected with a readable message.

---

## After these ten

Every remaining item in this file is a card title or a one-line engineering
idea, and that is the correct level of detail for work that is months away.
Specifying further now would be planning for its own sake — the specs above
exist because they are *next*, not because specs are inherently valuable.

The rule to carry forward: **spec one session ahead, not ten.** When session 10
is done, spec session 11 from whichever track matches the work in front of you,
using §4 as the template.

---

## Sessions 1–10 — what actually shipped

Recorded so the next person does not re-plan work that exists. Each line is one
commit on `claude/acronym-definitions-it-dictionary-mcqw8h`.

| # | Shipped | Evidence |
|---|---|---|
| 1 | Chips regrouped into five `.chip-group` blocks; mobile kept as one scrolling row | Sticky bar was 474 px tall on a phone before the mobile revert; 50 px after |
| 2 | `tools/stamp_freshness.py` — `data-reviewed="YYYY-MM"` on 862 topics, `--check` in CI | Mechanical commits detected by normalisation and passed to `--ignore-rev`, or every topic would read as reviewed today |
| 3 | `tools/lint_content.py` — errors block, warnings tracked as a TREND line | Found a real duplicate slug: `script.html` and `web.html` both titled a card "GraphQL — Ask for Exactly What You Need" |
| 4 | Wave Y1 — Intune policy, 5 cards | `endpoint` 13 → 18 |
| 5 | Wave Y2 — Intune applications, 5 cards | `endpoint` 18 → 23 |
| 6 | AG-1 spaced repetition — reduced SM-2 in `srs:<id>`, due badge on the FAB | Scheduling maths exercised directly in headless Chromium |
| 7 | AG-2 acronym quiz, generated from `acronyms.json` at build time | Dictionary inlined as compact JSON: 52 KB, not the 112 KB source |
| 8 | AH-2 acronym-aware search + three-state expansion density toggle | Searching `RBAC` and `role-based access control` return the same topics |
| 9 | Wave Y3 — Windows servicing and updates, 5 cards | `endpoint` 23 → 28 |
| 10 | AG-3 export / import progress | Round-trip byte-exact; merge keeps the later due date; four malformed files rejected with readable messages and zero writes |

Two register risks moved to **Mitigated**: progress data loss (session 10) and
markup rot (session 3).

**One thing session 10 turned up that was not on any list.** The study modal was
unreadable in light theme — `#st-modal` painted `var(--card, #0f1830)` and
`--card` was never defined, so the panel stayed dark navy while the text
inherited the light theme's near-black `--text`. Seven `var(--fg, …)` fallbacks
had the same shape: a variable that does not exist, papered over by a dark
default. `--card` is now defined in both themes and the dead `--fg` fallbacks
point at `--text`. The lesson generalises: **a `var()` fallback that renders
correctly is indistinguishable from a variable that works**, and only the second
theme tells them apart. Grep for fallbacks on undefined names before trusting a
theme.

## Session 11 — AJ-2 / AY, legacy topic headers and the alias map

Specified because it is next, and because session 10 walked into the symptom:
a quiz option rendered as *"Beginner Password Attacks 101 – Cracking, Spraying,
and Why MFA Matters ★ ✓ 🔗"*.

**The defect.** 90 topics carry their title as a bare text node in
`.topic-header` instead of inside `.topic-name`. `stIndex()` falls back to the
header's own `textContent`, which swallows the `.topic-badge` word and the
injected tool buttons. Every flashcard, quiz option and study-list row for those
90 topics is wrong. Distribution:

| File | Count | | File | Count |
|---|---|---|---|---|
| `grc` | 11 | | `pentest` | 6 |
| `linux` | 10 | | `military` | 5 |
| `net` | 10 | | `threat` | 5 |
| `script` | 10 | | `shortcut` | 2 |
| `sec` | 10 | | `lifestyle` | 8 |
| `ops` | 7 | | `ai` | 6 |

**Why it is not a five-minute fix.** No topic in `data/*.html` carries an `id`
attribute — all 916 slugs are derived at runtime from the header text. Wrapping
those titles changes the derived slug for **all 90**, measured:

```
beginner-ml-pipeline-from-raw-data-to-a-serving-model
  -> ml-pipeline-from-raw-data-to-a-serving-model
beginner-prompt-injection-the-sql-injection-of-the-ai-world
  -> prompt-injection-the-sql-injection-of-the-ai-world
```

That breaks every shared permalink and every `reviewed:` / `bookmark:` /
`known:` / `srs:` key those topics own. This is the **slug churn** risk in the
register arriving in person, so close it properly rather than around it.

**Do it in this order.**

1. **Write `tools/fix_topic_names.py`** — wrap the bare title of a legacy header
   in `<span class="topic-name">`, leaving the badge outside it. Idempotent, and
   it emits the old → new slug pair for each topic it touches.
2. **Emit an alias map**, `data/slug-aliases.json`, `{old: new}`, committed. The
   script writes it; it is not hand-maintained.
3. **Inline it at build time** the way the acronym payload already is, as
   `<script type="application/json" id="slug-aliases">`.
4. **Teach `openHashTarget` the map**: an unknown hash that matches an alias
   resolves to the new id and replaces the hash via `history.replaceState`, so
   the address bar self-heals and the old link keeps working forever.
5. **Migrate storage once.** On load, for each alias with data under the old key
   and none under the new, move it. Guard with a `migrated:slug-aliases-v1` flag
   so it runs once and re-running is a no-op.
6. **Add a lint error, not a warning:** a `.topic-header` with a bare text-node
   title is now an error. The warning existed for two sessions and nobody acted
   on it — the count only became interesting when it produced a visible bug.

**Done when:** `topic without .topic-name` reads 0; a permalink captured before
the change still lands on the right card and rewrites itself; a topic marked
reviewed under an old slug is still reviewed after; and the quiz shows no
stray ★ ✓ 🔗.

**Watch for.** `stamp_freshness.py` will see 90 rewritten headers — run it with
the wrapping commit in `--ignore-rev` or every one of those topics will claim it
was reviewed this month. That is the same trap session 2 built the mechanism
for; use it.

### Session 11 — outcome

Shipped as two commits, in that order, because the sequencing turned out to
matter:

1. **`Rename a duplicate title: Container Security 101`.** The wrap surfaced a
   collision that had been hiding in plain sight: `sec.html` and `ops.html` both
   carried a card called "Container Security — Hardening Docker & Images". They
   never collided because the `sec.html` one is a legacy header, so its slug
   carried the badge word — `beginner-container-security-…`. Take the badge out
   of the label and the two become the same slug, with the second silently
   taking `-2`. The beginner card was retitled to what it actually covers.
2. **`Wrap 90 legacy topic titles in .topic-name`.** The wrap, the 91-entry
   alias map, the runtime that reads it, and the lint promotion.

**What the tooling learned.** Three decisions came out of things that went
wrong on the first attempt, and each is worth keeping:

- **Compare against `HEAD`, not the working tree.** The first run computed
  "before" from the files on disk, so a rename made in the same change as the
  wrap was already present in the baseline and its old permalink went
  unrecorded. Edit order should never decide whether a link survives.
  `committed_texts()` now reads `git show HEAD:…`.
- **`--check` must not re-derive the map.** The alias map is an append-only
  record of links we have published; nothing in the tree can regenerate it.
  CI checks the three things it *can* check: no legacy header remains, no alias
  points at a slug that no longer exists, and no slug moves without an alias.
- **Aliases compose, so runtime never needs two hops.** The rename moved a slug
  and the wrap moved it again. `compose_aliases()` re-points existing entries
  through the current run's moves, so the oldest published link still resolves
  in a single lookup. Verified: `#beginner-container-security-hardening-docker-images`
  lands on `#container-security-101-why-an-image-is-not-a-sandbox`.

**And one that would have quietly poisoned the freshness data.** The wrapping
commit is not a content edit, but `git blame` cannot tell. Rather than passing
the commit to `--ignore-rev` by hand — which works once and is forgotten
forever after — `stamp_freshness.normalise()` now strips the `.topic-name`
wrapper the same way it strips acronym spans, so the commit classifies itself
as mechanical. The regex substitutes `\1`, keeping the title: a *retitled* card
is a real edit and still dates as one. That is why `sec.html`'s renamed topic
moved to `2026-08` while the other 89 wrapped topics kept their dates.

**Measured.** 91 aliases, 0 dangling, 0 shadowed by a live id; 915 topics in the
study index with 0 labels carrying a badge word or a ★ ✓ 🔗 glyph; a stale
permalink lands, opens the card and rewrites its own hash; progress stored under
an old slug migrates once, never clobbers data already under the new id, and a
second load does not resurrect keys the user has since cleared.

## Session 12 — candidates

Nothing here is spec'd yet, deliberately: **spec one session ahead, not ten.**
Pick from the register, not from appetite.

| Candidate | Why it might be next | Why it might not |
|---|---|---|
| **AK page weight** — `index.html` is 3.4 MB and every wave adds to it | The only **Planned** risk with a number attached that keeps growing on its own | Nobody has complained; measure real load time on a phone before optimising |
| **AX volatility tags** — mark cards whose facts expire (portal names, SKUs, limits) | `stamp_freshness.py` already knows which topics *look* volatile (`VOLATILE_HINTS`); the report exists and nothing consumes it | Half-built already, so the remaining value is smaller than it looks |
| **The `ops` split** — 68 cards and six tracks pointed at it | The plan's own rule says decide **before** 72 cards land, and it is at 68 | It is a rename of many slugs; the alias machinery is now in place, which makes it cheaper than it was yesterday |
| **The `<h3>`-in-header inconsistency** | 46 wrapped headers carry an `<h3>` and render a size larger than their neighbours | Cosmetic, and the linter does not flag it — add the rule first, then decide |

The `ops` split is the one whose cost just dropped: session 11 built exactly the
machinery a large rename needs. If it is going to happen, it is cheaper now than
it will be at 90 cards.

### Session 12 — outcome: the `ops` split

Done. `ops` was at 68 cards with six tracks still pointing at it, and the plan
set the decision point at 72.

**The seam is a job description, not a topic list.**

| Domain | Keeps | Cards |
|---|---|---|
| `ops` — IT & Security Operations | Service desk troubleshooting, SOC, incident response and command, forensics, SIEM/SOAR, vulnerability management, BCP/DR, ITIL, runbooks, postmortems, on-call — and the observability and SRE material those roles work inside | 32 |
| `devops` — DevOps, Platform & Delivery | CI/CD, IaC, containers and Kubernetes, GitOps, secrets, supply chain, config management, deployment strategies, plus the architecture cards that only make sense beside them (queues, caching, serverless, object storage, CAP, FinOps) | 36 |

Both clear the Phase-4 bar: 15+ cards, own tooling, a job title you can hire for.
An SRE/observability third domain was considered and rejected — 12 cards, under
the bar. **The observability block is the seam most likely to want revisiting**;
if it grows past 15 it should probably leave `ops` for a domain of its own.

**Slugs did not move.** They derive from the title, not the domain, so the whole
split needed no aliases and no migration — `fix_topic_names.py --check`
confirmed zero unrecorded moves. That is worth remembering before the next
reorganisation: moving a card between domains is free, renaming one is not.

**Two things the move surfaced, both worth keeping.**

- **A `byDomain` acronym override is keyed to a domain, so moving a card can
  silently change what an acronym expands to.** `SCP` became "Secure Copy
  Protocol" in a card about AWS Organizations guardrails, because the override
  that made it "Service Control Policy" was keyed on `ops`. Audit every
  multi-meaning acronym in a file after moving cards into it — there were four
  in the new file, and one was wrong.
- **Dating content requires following it, not the file it lives in.** The split
  first marked all 36 moved cards as reviewed this month. Fixing it properly
  took three changes to `stamp_freshness.py`, and two of them were general
  bugs that the split merely exposed:

  1. `git blame -C -C`, so a line moved from a file modified in the same commit
     keeps its original date. This also corrected 42 topics in `linux`,
     `script` and `sec` that had been dated by an in-file move — all of them
     backwards, to when the content actually landed. Two `-C` and not three:
     the third searches every file in every commit and takes minutes.
  2. **The ignore list has to follow the content the way blame does.**
     Mechanical commits were found per path, so a file created by a split could
     not see the whole-tree markup passes that had swept the file its cards came
     from. They are now identified globally — a commit that changed nothing real
     in *any* domain file it touched. That alone took 36 wrong dates down to 3.
  3. `.git-blame-ignore-revs`, with its limitation written into the file:
     `--ignore-rev` reattributes a line to whatever touched it *before*, so a
     line the ignored commit created stays put.

  Three cards still date to the split. Copy detection catches the long runs of a
  relocated card and misses the short ones. Three cards reading one month newer
  in a month-granularity signal is a documented imprecision, not a reason to
  build a relocation detector.

**And one near-miss worth naming.** The "file git has never seen" fallback was
written as a blanket `return {}`. It then swallowed a malformed
`.git-blame-ignore-revs` and cheerfully reported *"0 topics stamped"* — a
freshness tool reporting success while measuring nothing. Narrowed to the two
error strings it was meant for. **A fallback that cannot fail is not robust, it
is silent.**

## Session 13 — candidates

| Candidate | Why it might be next | Why it might not |
|---|---|---|
| **AK page weight** — 3.4 MB and growing | Still the only Planned risk with a number that grows on its own; now 21 domains | Measure a real phone load first; the answer may be "fine" |
| **AX volatility consumers** — `stamp_freshness.py --report` finds volatile+stale cards and nothing reads it | The data already exists; surfacing it in the page is small | Needs a design decision: a badge on the card, or a review queue in the study tools? |
| **`devops` content waves** | A new domain at 36 cards with no wave written specifically for it | It was just reorganised; let it settle before adding |
| **The `<h3>`-in-header inconsistency** — 46 wrapped headers render a size larger | Now visible side by side with their neighbours after session 11 | Cosmetic; add the lint rule first, then decide |

The honest ordering: **AX volatility consumers**, because the measurement exists
and is unused, and unused measurement is the cheapest thing in the plan to
mistake for progress.

### Session 13 — outcome, including the recommendation that did not survive contact

**AX volatility was the recommendation above, and it was wrong.** Running
`stamp_freshness.py --report` before building anything: 182 of 915 topics match
`VOLATILE_HINTS`, and **the oldest is two months old**. Nothing is stale. A
"needs review" queue built on this today would render an empty list, and a badge
would either never appear or appear on a fifth of the site at once.

Two things follow, and the second matters more than the first:

- **`VOLATILE_HINTS` is too broad to act on.** It matches `portal`, `licence`,
  `version \d` and `tier`, which is a fifth of the corpus. Before anything
  consumes this signal it needs to be a property of the *claim* — a console path,
  a price, a limit — not of the prose containing a word. That is a content
  convention, not a script.
- **The signal needs age before a consumer is worth building.** The measurement
  is six weeks old on a corpus written this year. Come back when something is
  actually a year stale, and design the consumer against real rows.

Recording this rather than quietly dropping it: the plan told me to build a
consumer for measurement that exists, and checking the measurement first was
what stopped it. **Read the data before designing the thing that reads the
data.**

**What shipped instead: the `<h3>`-in-header cleanup.** Session 11 put every
title inside `.topic-name`, which made a second inconsistency visible — 45 of
those titles also sat inside an `<h3>` and rendered a size larger and heavier
than every neighbouring card. All 915 topic names now compute to 14px; before,
45 did not. A heading tag inside `.topic-header` is now a lint error, and
`normalise()` strips heading tags so the unwrap read as markup rather than as 45
cards reviewed this month.

Worth being explicit about what was *not* done: making all 915 titles real
headings is a defensible change with accessibility implications worth thinking
about properly. Making 45 of them headings and 870 spans was not a decision
anyone made, and that is the only part this fixes.

## Session 14 — candidates

| Candidate | Why it might be next | Why it might not |
|---|---|---|
| **AK page weight** — 3.4 MB, 21 domains | The last Planned risk with a number that grows on its own | Measure a real phone load first; the answer may be "fine", and that is a valid outcome |
| **A volatility convention** — mark the *claim*, not the prose | Session 13 showed the current heuristic cannot be acted on | Authoring conventions only stick if the linter can check them; design that first |
| **`devops` content waves** | 36 cards, no wave written for it as its own domain | Freshly reorganised; a wave written now would be written against a domain nobody has read yet |
| **Study-tools decks per domain** | 21 domains now; the deck picker was designed for 19 | Small, and nothing is visibly broken |

**AK page weight**, and specifically: measure before optimising. The plan has
carried "3.2 MB and growing" as a risk since Phase 4 without anyone timing a
load. Session 13's lesson applies directly — read the data before designing the
thing that acts on it.

### Session 14 — outcome: the numbers, and a budget instead of a rewrite

Measured before writing a line of optimisation:

| | desktop | phone (4× CPU throttle) |
|---|---|---|
| First contentful paint | 160 ms | 336 ms |
| Load event | 308 ms | 1,284 ms |
| Chip filter | 28 ms | 50 ms |

Transfer and size, which do not vary by device: **836 KB gzipped**, 24% of
3.3 MB raw; **78,819 elements** live, 75,063 of them static markup.

**The page is not slow.** Lazy per-domain loading — the planned mitigation since
Phase 4 — would have traded a working offline-first single document for
machinery aimed at a problem that has not arrived. Second time in two sessions
that reading the measurement first changed what got built.

What the page *is* is **unbounded**: every wave adds to it and nothing pushes
back. So the mitigation is a budget, not a rewrite. `tools/page_budget.py`
checks gzipped size, raw size and static element count against budgets ~25%
above today, and runs in CI after the build. A normal wave passes; a doubling
does not. When a budget is hit, *that* is the moment for the lazy-loading
conversation — with a number in hand, and with the budget moved deliberately in
its own commit if the growth is worth it.

The register's **Page weight** risk moves to **Mitigated**: not because the page
got smaller, but because it can no longer grow unnoticed.

One detail kept honest in the tool rather than glossed: the budgeted element
count is *static markup*. The live DOM runs ~4,400 higher, almost entirely the
four-element tool cluster `script.js` injects into each of 915 topics. CI cannot
run a browser, so it budgets what a content wave actually changes — and the file
states both numbers so neither is mistaken for the other.

### Session 15 — a bug the reorganisation walked into

Session 14's candidate list had "study-tools decks per domain" with *"small, and
nothing is visibly broken."* That was wrong, and only checking made it obvious:
the flashcard and quiz deck pickers listed all twenty-one domains as a **bare
emoji with no name**. `stScopeSelectHTML` read `d.domainTitle` off the objects
`stScopeOptions` returns, which carry `title` — `domainTitle` is the key on an
`stIndex` row, not on a scope option. Undefined for every entry, silently, since
the picker was written. Networking and Web share the 🌐 icon, so two options
were byte-identical.

Fixed, and each deck now carries its size — `🌐 Networking (55)` — because the
first question about a deck is how long it will take, and the picker already
walks the index to build the list.

**The pattern worth naming:** three sessions running, the plan's own judgement
about what was worth doing was corrected by spending two minutes looking. The
volatility consumer was not worth building (data too young), the lazy-loading
rewrite was not worth building (page not slow), and the deck picker was not
"nothing visibly broken" (broken since it was written). A plan is a hypothesis.
Check it against the artifact before you spend a session on it.

### Session 16 — Wave T3, the wave you actually asked for

Everything since session 10 has been tooling and structure. This one is content,
and it is the item you named directly: **SF 703 Top Secret (orange), SF 704
Secret (red), SF 705 Confidential (blue), and all other SF.** Six cards in
`military`, taking it 23 → 29.

Written as reference about the forms and the public handling procedure — no
classified content, only the protocol. Each card names the trap rather than only
the rule; the three worth remembering:

- **The SF numbers ascend as the classification descends.** 703 is Top Secret,
  705 is Confidential. Everyone guesses it the other way round the first time.
- **SF 710 green exists so that "no label" means something.** In a mixed
  environment where only classified media is labelled, an unlabelled drive is
  ambiguous. Label everything and an unlabelled drive becomes an anomaly.
- **Concealing a spill is a different act from causing one.** Accidental spills
  are common and survivable; the deletion is what ends careers.

The dictionary gained `SF`, `SCI`, `SAP`, `NISPOM` and `DCSA`. `SAP` is
disambiguated — Special Access Program in `military`, the ERP suite elsewhere —
and carries `noAnnotate`, so it expands only where a domain says which is meant.
That mechanism was built in session 1 for exactly this and has now paid for
itself several times.

**A note on ordering, honestly.** Six sessions of tooling ran before this card
got written, and it was requested before any of them. The tooling was not wasted
— this wave inherited permalinks, progress, freshness stamping, acronym
expansion, search, flashcards and a page budget without a line of work — but the
ordering was mine, not yours. Worth stating plainly rather than presenting the
sequence as if it had been optimal.

### Session 17 — the acronym dictionary was in the wrong decks

Following the same habit as the last four sessions: before adding anything,
look at what is there. The flashcard and quiz decks included the acronym
dictionary, whose 54 "topics" are A–Z index sections. As a flashcard the front
read *"A — 75 acronyms"*; as a quiz question the distractors were *"Acronyms —
B"* and *"Acronyms — C"*. Fifty-four of them, 6% of the All-domains deck.

The material is fine — it is a different question, and the dedicated 🔤 acronym
quiz already asks it, generated from `acronyms.json` rather than from the page.
Excluded from the domain list and from All-domains; **not** from bookmarks or
due-today, because starring a section and grading a card are deliberate acts and
a deck built from the user's own choices should honour them.

`ST_NOT_STUDYABLE` is a one-entry set rather than a special case, so the next
index-style domain — a glossary, a cheat-sheet hub, the Track U reference
sheets — has an obvious place to be listed.

### Where the register stands after sessions 10–14

| Risk | State |
|---|---|
| Progress data loss | **Mitigated** — session 10 |
| Markup rot | **Mitigated** — session 3, extended by 11 and 13 |
| Slug churn | **Mitigated** — session 11: alias map, self-healing links, storage migration |
| Generated-file drift | **Mitigated** — CI |
| Page weight | **Mitigated** — session 14: measured, budgeted |
| Content goes stale | **Partly** — stamps exist; session 13 showed the volatility heuristic is not yet actionable |
| Accuracy drift · Bus factor · Scope paralysis | **Partly** — as before |

Six of nine mitigated. The three that remain are the ones that cannot be closed
by tooling: whether the content is right, whether one person holds all the
context, and whether the list is too long to be motivating. Those are answered
by writing cards and by keeping this file honest, which is what the last five
sessions have been for.

---

# CALCULUS TRACK — Math 104 study plan, gaps and tooling

Added from the course's own requirements screen, the Study.com "Math 104: Calculus
Formulas & Properties" reference, and the review guide below. This section is a
live study plan rather than a roadmap item: it tracks what the course tests,
what the site already covers, and what is still missing.

## 1. The review guide

### 1.1 Limits and Continuity
- **Evaluating limits** — basic algebraic limits, and limits of trigonometric functions
- **One-sided limits** — from the left and right, using piecewise functions and graphs
- **Limits at infinity** — behaviour as x approaches ±∞
- **Limit laws** — the limit of a sum is the sum of the limits, and the rest of the algebra
- **Existence** — a limit does not exist when the left- and right-hand limits disagree

### 1.2 Derivatives and Rates of Change
- **Advanced implicit differentiation** — relationships mixing x with trig functions of y,
  such as `x·sin(y) = 5y + 2x`, needing the product rule *and* the chain rule, then
  grouping the `dy/dx` terms to solve
- **Derivatives of inverse trigonometric functions** — the standard formulas, memorised
- **Implicit differentiation** — where y is not solved for explicitly; apply `dy/dx`
  every time a y is differentiated
- **Choosing the first rule** — identify the *outermost* operation to know which rule
  applies first. This is the skill that makes the others usable
- **The chain rule** — differentiate the outer function keeping the inner intact, then
  multiply by the derivative of the inner
- **Antiderivatives** — working backwards by applying the power rule in reverse
- **Higher-order derivatives** — how rates of change themselves change
- **Graphing the difference quotient** — reading `f(a + Δx)` off a graph at a horizontal
  distance Δx from a base point a
- **Graphical rate of change** — the slope between two points, `m = (y₂ − y₁)/(x₂ − x₁)`,
  as the constant rate over that interval
- **The limit definition** — `f′(x) = lim(h→0) [f(x+h) − f(x)] / h`
- **Defining the derivative** — the instantaneous rate of change
- **Kinematics** — constant velocity means position changes at a constant rate;
  acceleration is the second derivative of position `s(t)`
- **Related rates** — the chain rule against time, given one rate to find another

### 1.3 Core Calculus Theorems
- **Rolle's Theorem** — continuous on `[a,b]`, differentiable on `(a,b)`, and
  `f(a) = f(b)` gives some `c` with `f′(c) = 0`. For an interval like `[0,3]` it is
  **mandatory** that `f(0) = f(3)` before the theorem may be used at all
- **Mean Value Theorem** — average rate over the interval equals instantaneous rate at
  some interior point. Applies to real scenarios: proving a driver exceeded a limit by
  comparing average speed over a known distance against the posted minimum

## 2. Gaps this turned up

The Study.com formula list names things the Math domain does not yet cover. Checked
against the site rather than assumed:

| Missing | Where it belongs | Note |
|---|---|---|
| **Trapezoidal Rule** | Unit 3 / cheat sheet | Numerical integration — the course lists it explicitly and the site has nothing. Highest-value gap |
| **Right-triangle trig** (SOH-CAH-TOA) | Trigonometry card | The site defines sin/cos/tan from the unit circle only. The course defines all six as side ratios. Students meet both and courses rarely reconcile them |
| **Volume of a hemisphere** | Shape formulas | One row |
| **Equation of an ellipse / "oval"** | Algebra & Geometry | Listed by the course; absent here |
| **Inverse trig derivatives** | Cheat sheet has three | arcsec, arccsc, arccot are not listed. Add for completeness |
| **Series depth** | Unit 3 | Still open from the earlier audit — integral, comparison, limit comparison and root tests; radius and interval of convergence |

## 3. Tooling idea — a Python TI-84 trainer

**The problem.** Ch 5 is a required chapter test on using a scientific calculator, and
the TI-84 Plus CE card on this site is a *reference*. Reading key sequences is not the
same as being able to produce them under time pressure, and the calculator itself is a
poor practice environment because it gives no feedback on whether you used it well.

**The idea.** A small Python program that drills the calculator rather than emulating it.
Not a TI-84 simulator — that is a large project with no learning payoff. A **key-sequence
trainer**:

```
$ python tools/ti84_trainer.py

  Find the derivative of x² at x = 3.
  What do you type?
  > MATH 8 nDeriv(X²,X,3)
  ✔  Correct. Answer: 6

  You need sin(π) to read 0, not 0.0548. What is wrong and how do you fix it?
  > mode is degrees, press MODE and select RADIAN
  ✔

  ERR: INVALID DIM appears when you press GRAPH. Most likely cause?
  > stat plot left on
  ✔  2nd Y= turns the plots off.
```

**Why Python and why here.** The site already generates content from data
(`acronyms.json` → the dictionary, the SVG generators). A trainer fits the same shape: a
JSON file of prompts and accepted answers, a small runner, and — because the answers are
deterministic — the same file can generate the flashcards for the calculator card, so the
drill and the reference cannot drift apart.

**Scope, deliberately small.**

| In | Out |
|---|---|
| Key-sequence prompts with fuzzy answer matching | Emulating the screen or the keypad |
| The numeric functions: `nDeriv`, `fnInt`, `Σ`, `logBASE` | Any attempt at symbolic algebra |
| The CALC menu items and what each asks for | Graphing |
| The error messages and their usual causes | Programs, matrices, statistics |
| Verifying the *answer* with Python's own maths, so the drill states the right number | Being a calculator you would actually use |

**Done when:** a run of twenty prompts covers mode setup, the four numeric functions, the
CALC menu, and the five common errors — and every stated answer is computed by Python
rather than typed in by hand, so the drill cannot be wrong about arithmetic.

**Worth building only if** Ch 5 turns out to be harder than it looks. The reference card
may be enough on its own; check the chapter test first. That is the same lesson as
sessions 13–15 — read the data before designing the thing that reads the data.

### Outcome — built

Shipped as `tools/ti84_trainer.py` + `data/ti84_drills.json`, 27 drills across the four
areas the spec named: mode setup, the numeric functions, the CALC menu, and the errors.

The design rule held: **every number the program states is computed at run time.** Ten
drills carry a `compute` expression evaluated in a namespace with no builtins, so the
drill cannot be wrong about arithmetic even if someone edits the bank carelessly.
`--verify` evaluates all of them plus checks structure, and is wired into
`build-check.yml`.

One decision worth recording. `nderiv()` in the trainer is a **symmetric difference
quotient**, not an exact derivative — deliberately, because that is what the TI-84 does,
and it is why `nDeriv(abs(X),X,0)` returns a confident `0` where no derivative exists.
Using an exact derivative would have made the trainer disagree with the machine it is
teaching, and the drill about that specific lie would have been unable to demonstrate it.

**Note on the gate above:** it said to check the Ch 5 test first. That check did not
happen — the build was requested directly. The gate was right in principle and the
trainer may turn out to be more than Ch 5 needs; it cost little and the CI check keeps it
honest, but this is recorded as a spec whose own precondition was skipped.

The remaining half of the idea — generating the calculator card's flashcards from the
same JSON so drill and reference cannot drift — was **built in session 18**; see below.

---

# WHAT IS ACTUALLY OUTSTANDING

An audit rather than a wish list. Everything below was checked against the repo on
2026-08-13, not recalled — the counts come from `lint_content.py`, `git grep` and the
domain files themselves. Ordered by how much it costs to leave undone.

> **Session 18 (2026-08-14) closed the honest short list — all three items.**
> Each entry below is annotated with what happened. The section is kept rather
> than deleted, because the reasoning is what makes the next audit cheap.

## 1. Things that are wrong right now

These are defects, not missing features. Each is small.

| Item | Evidence | Fix | State |
|---|---|---|---|
| **`CALCULUS-CHEAT-SHEET.md` is stale and overclaims** | 7 sections in the file, 16 cards in the Math domain. Its header says "Generated from the Math domain", which is no longer true — it was generated from one card | Re-run the generator over all cards, or narrow the header to what it actually covers | ✅ **Fixed.** There was no generator — the claim was aspirational. `tools/gen_cheatsheet.py` now walks all 16 cards (65 sections, 933 lines) and `--check` is a CI gate |
| **`Windows Administration Fundamentals` is in `lifestyle`** | `grep -l` finds it in `data/lifestyle.html`. It is technical Windows content sitting in Life Admin | Move to `endpoint`. Slugs derive from titles, so nothing breaks — proven twice | ✅ **Moved.** `endpoint` 28 → 29 cards, `lifestyle` 5 → 4. Both subtitles updated; permalink unchanged, as predicted |
| **The TI-84 drill and its card can drift** | The card cross-references `ti84_trainer.py` in prose only. The spec called for the card's flashcards to be generated from `ti84_drills.json` | Generate them, or accept the drift and say so in the card | ✅ **Generated.** The prose had already drifted — it named 2 of the 4 areas. The card's drill index is now emitted by `--sync-card` between markers and gated by `--check-card` |

## 2. ✅ The lint TREND — resolved, and it had gone *up*

`lint_content.py` tracked these as warnings for fourteen sessions and none had gone
down:

```
1946  inline style attribute
 361  ai-table (prefer ref-table)
 148  hard-coded hex colour
```

**This is the honest problem with tracked warnings: a number nobody is accountable for
is decoration.** Three options, and picking one matters more than which:

1. **Fix a slice per session** — say 200 inline styles — and let the TREND line show it falling.
2. **Promote one to an error** at its current count as a ratchet, so it can only improve.
3. **Delete the counters** and stop pretending they are being managed.

The hard-coded hex count is the one with real consequence: those colours do not follow the
light/dark theme, which is exactly the class of bug that made the study modal unreadable in
light mode.

### ✅ Resolved — and the hypothesis was confirmed the hard way

`hard-coded hex` went 148 → 0 and became an error in session 18. The other two were
measured again when the content backlog emptied, and the finding is worth stating
plainly: **`inline style attribute` had risen from 1,946 to 2,707 — up 39% while being
"tracked".** Sessions kept writing the thing the counter counts, including the four cards
written earlier that same day. A tracked warning does not merely fail to improve; it
provides cover for getting worse.

Each of the three options was applied to a different counter, chosen by what the numbers
turned out to be:

| Counter | Was | Now | Option taken |
|---|---|---|---|
| `hard-coded hex colour` | 148 | 0, an error | 2 — ratchet at zero (session 18) |
| `inline style attribute` | 2,707 | 1,565, ceilinged | 1 **and** 2 — fix the slice, then ratchet |
| `ai-table (prefer ref-table)` | 360 | a census line | 3 — delete the counter, with evidence |

**Inline styles.** The distribution was the whole story: 1,142 of 2,507 were one shape —
`<div class="concept-desc" style="margin-top:…">`, the verdict sentence after a table —
and `.concept-desc.verdict` had existed as a class for several sessions without content
using it. Converted, plus 67 `margin-top:0` on first children that a check of every
`.concept-desc` rule proved were overriding nothing. Then a **ceiling** rather than a
zero, because zero is unreachable: 806 of the remainder colour the first cell of a
`.ref-table`, where a utility class provably loses on specificity — the finding that cost
session 18 a 1,614-instance bug. A ceiling can fall and cannot rise, and the inline form
of the verdict margin is now its own error with a line number, so the shape cannot come
back.

**`ai-table`.** The label asserted a preference the stylesheet contradicts. `.ai-table` is
`.9rem` text with an amber, `nowrap` first column; `.ref-table` is 12px with a white one
and a tinted mono header. Converting 360 tables across 18 domains would be a visible
redesign, not a cleanup, and nobody had ever agreed to it. It is now reported as a census
line — the information without the false imperative — and `CONTRIBUTING.md` says so.

One free result: the dead-first-cell guard only ever matched `.ref-table`, though
`.ai-table td:first-child` sets colour at the same specificity. `.ai-table` has never
carried a dead class; the guard now covers it so it never starts.

### ✅ Session 18 — the hex counter, closed by doing 1 and 2 together

```
TREND ai-table=361 hard-coded=148 inline=1946     before
TREND ai-table=361 inline=1946                    after
```

Picking the counter turned out to be the easy half. The instructive part was that
**8 of the 148 were never colours at all.** The check was a bare
`#[0-9a-fA-F]{3,6}` sweep, so it counted `"deploy #4521"`, `"invoice #4471"`, and
five CSS samples in `script`/`web` that exist precisely to *teach* hex notation.
A counter with an unreachable floor cannot be driven to zero, which is a decent
explanation for why nobody tried for fourteen sessions.

So the check was narrowed to the claim — a literal inside a `style="…"` value or an
SVG paint attribute — which is the same lesson `VOLATILE_HINTS` is still waiting for
in §4: *design the check before you ask anyone to act on the number.*

The remaining 140 were real, and fell into two shapes:

- **89 in `net`'s five topology diagrams**, as `stroke="#38bdf8"` / `fill="#0d1120"` on
  every line and circle. `fill="#0d1120"` is `--bg2` — the *dark page background* — so in
  light mode every node was painted a near-black disc on a white card. Replaced with
  `.topo-svg line|circle|text` rules, the same class-based pattern `math.html` already
  uses for its `msv-*` diagrams and the reason that file has never had a literal in it.
- **51 as `style="color: #…"`** across nine domains. `military.html` was already mixing
  `var(--purple)` and `#38bdf8` in adjacent `<th>`s, so the convention existed; it just
  was not applied. The worst of these was `pentest`'s `style="color: #fff"` on three
  `<strong>`s — white text, on a white light-mode card, invisible.

Both needed somewhere to point at, so `:root` gained a themed accent palette — `--sky`,
`--orange`, `--pink`, `--yellow`, `--emerald`, `--indigo`, `--violet`, `--rose`,
`--fuchsia`, `--lime`, plus dimmed `--amber-2/-3`, `--green-2/-3`, `--cyan-2` for the
three-tone severity ladders in `ops` and `linux` — each with a light counterpart.
`.topo-name`'s `color: #fff` in `style.css` went the same way.

Verified in headless Chromium by toggling `data-theme` and reading computed styles:
every affected element now changes colour with the theme, `0` elements carry a raw hex
in a `style` attribute, no console errors, no off-site requests.

**The counter is now an error, not a warning** — a ratchet at zero, with a message that
names the palette. Regression tested by reintroducing one literal: CI fails.

`inline style attribute` (1946) and `ai-table` (361) are deliberately still warnings.
Two ratchets are enough to hold the line; a third would block content work, which is
the thing the site is actually for.

### The inline-style counter, and why the obvious fix is wrong

Worth writing down, because it looks like a free win and is not.

**1069 of the 1946** inline styles are colour-only — `style="color: var(--cyan)"` and
nothing else. `CONTRIBUTING.md` already forbids exactly this, in a table, in favour of
`class="c-cyan"`. So the counter looks halvable by one mechanical substitution.

It was tried in this session, on all 866 that a naive match caught, and **reverted**.
Inline `style` beats any class on specificity; `.c-cyan` does not. Converting moves the
element from "wins everything" to "loses to any rule that outranks a bare class", and
the page has one that matters: `.ref-table td:first-child`, at (0,2,1).

The counter is real, but the substitution is not safe to do blind. Every conversion has
to know whether a table rule will eat it — which is exactly what happened to the 866,
and why they went back.

### The dead utility classes — measured, then removed

Chasing the above turned up something better. **1614 elements carried a `c-*` class that
had never once rendered**, all of them the first cell of a `.ref-table` row:

```
elements carrying a c-* colour class:  8300
…rendering that colour:                6686
…overridden:                           1614   ← every one a .ref-table td:first-child
```

The first read of this was "1614 cells are the wrong colour" — a live rendering bug.
**That was wrong, and the correction is the interesting part.** `.ref-table
td:first-child { font-weight: 600; color: #fff }` is deliberate: the key column is
styled bold and prominent on purpose, and has looked that way since it was written. The
classes were boilerplate — in `net.html`, 12 ref-tables carry `c-cyan` on *every* first
cell and 9 carry none, never a mix. Nobody was choosing cyan per-cell; a habit was being
applied to a column the design already handled.

So the site was never rendering wrongly. The markup was just claiming something it could
not deliver. The fix is to delete the claim, not to honour it — making all 1614 live
would be a 1614-cell redesign nobody asked for, and would undo the point of the
key-column rule.

Removed, and verified as a no-op the only way worth trusting: computed `color`,
`font-weight` and `background-color` for **all 83,344 elements**, in both themes, before
and after. Zero differences. (15 elements differed in light mode until two runs of the
*same* build showed the same 15 — a theme transition still in flight, not the change.)

`lint_content.py` now errors on a colour class in that position, so the 1614 cannot
creep back. `CONTRIBUTING.md` says where the classes do and do not work.

**The lesson worth keeping is the misdiagnosis, not the cleanup.** "2196 elements render
the wrong colour" and "1614 elements carry a class that does nothing" describe the same
measurement and imply opposite actions — one a visual bug to fix, one dead markup to
delete. The number was right both times. Only reading the *design intent* behind the
overriding rule told them apart, and that is not something a linter can do.

## 3. New domains with no plan behind them

The `lifestyle` split created five domains and the Math work added one more. **None of them
has a wave spec'd**, and the plan's own Phase-4 rule says a domain needs ≥15 cards to
justify existing:

| Domain | Cards | Against the ≥15 rule |
|---|---|---|
| ~~`spirit`~~ | ~~3~~ | ✅ **Folded into `philosophy`** — session 18 |
| `quotes` | 5 | Under, but it is a reference domain like `acronym`, so the rule may not apply |
| ~~`lifestyle`~~ | ~~4~~ | ✅ **Folded, session 19.** Split three ways — see below |
| ~~`philosophy`~~ | ~~14~~ → **17** | ✅ **Clears it.** Ethics, arguments &amp; fallacies, and epistemology added — the machinery the domain had none of, next to the traditions it covered well |
| `productivity` | 10 | Under, but actively growing |
| `mind` | 11 | Under, but actively growing |
| `math` | 16 | Clears it |
| `career` · `devops` | 21 · 36 | Clear it comfortably |

### ✅ Session 19 — `lifestyle` folded, and why it took a decision rather than a fold

`spirit` had one obvious home. `lifestyle` had none, which is why it sat unresolved after
`spirit` was settled: its four cards do not belong together and never did.

| Card | To | Why |
|---|---|---|
| Money & Adulting Basics | `career` | Personal finance for a working person; `career` already holds offer negotiation and home-lab budgets |
| Financial Basics for IT Workers | `career` | Says so in the title |
| Remote Work — Working Well From Anywhere | `career` | Professional practice, beside the soft-skills cards |
| Minimalism & Intentional Living | `philosophy` | A values card. It belongs beside Stoicism and Taoism, not beside interview prep |

29 → **28 domains**, topic count unchanged. All four permalinks verified in a browser.

**The general point:** the ≥15 bar asks whether a domain earns a chip, but the useful
question when it does not is *where does each card actually belong*. Three of these four
had a clear home and one needed a judgement; none of them wanted the same one. A domain
that cannot be folded in one move is usually a bag rather than a subject, and that is the
signal to look at the cards individually.

**Decide `spirit` first.** Three cards is not a domain; it is a chip that dilutes the bar.

### ✅ Session 18 — decided: folded

Wicca, Paganism and Druidism moved into `philosophy`, which already carried Buddhism
under a `SPIRITUAL PHILOSOPHY` badge and Taoism under `CHINESE PHILOSOPHY` — so the
domain was already doing this job, and `spirit` was a second chip for the same shelf.
Re-badged to `EARTH-BASED PRACTICE` / `EARTH-BASED TRADITION` to match how the other
traditions there are labelled.

Removed with it: the chip in `index-shell.html`, the `.c-spirit` / `.domain-spirit`
rules in `style.css`, the entry in `domains.json`, and a dead `byDomain.spirit` key in
`acronyms.json` (an `AD` suppression — `philosophy` already carried the same rule).
28 domains → **27 domains, with the topic count still 943**: nothing was lost in the
move, which is the number worth checking after a fold. Permalinks survive because slugs derive from
titles, not domains — third time that has held.

The rule earned its keep here. `lifestyle` at 4 is now the weakest chip on the bar and
is the next one to answer for itself; the honest options are the same two.

## 4. Content age

274 topics still carry `data-reviewed="2026-06"`, the oldest stamp in the repo. Nothing is
stale by any reasonable standard yet — the site is months old, not years — but this is the
number to watch, and the freshness tooling exists precisely so it can be watched rather
than guessed at.

> ✅ **Re-measured.** No `2026-06` stamps remain: the distribution is now **446 at 2026-07
> and 900 at 2026-08**, across the 1,346 hand-written topics (the 59 generated `acronym`
> cards carry no stamp by design). The number moved because cards get edited, not because
> anyone ran a freshness pass — which is the useful thing to know about it.

Related and still unresolved from session 13: **`VOLATILE_HINTS` is too broad to act on.**
182 of 943 topics match it. Before anything consumes that signal it needs to mark the
*claim* — a console path, a price, a limit — not prose containing a word like "portal".
That is a content convention, and conventions only stick if the linter can check them, so
design the check first.

### ✅ Session 18 — the check, and a surprise about the content

Built as specified: the claim is marked where it sits.

```html
Used enterprise mini PC (<span class="volatile" data-checked="2026-08">~$80-150</span>)
```

`data-checked` is when the *claim* was verified, deliberately distinct from the card's
`data-reviewed` — rewording a paragraph is not the same act as confirming a price. The
reader gets a dotted underline and the date on hover, inline in print; that matters,
because a convention that only feeds a linter gets abandoned, and this one pays the
reader back.

`lint_content.py` errors on all four ways to get it wrong: a mark with no date, a
malformed month, a date in the future, and `data-checked` on something not marked
volatile. `stamp_freshness.py --report` now lists **claims**, oldest first, naming the
claim and its topic. The old keyword sweep moved to `--candidates` and prints a warning
about what it is.

**The surprise: there is almost nothing to mark.** Going looking for real volatile
claims across 888 topics turned up:

| Looked for | Found |
|---|---|
| `as of <year>` dated claims | **0** |
| Console breadcrumbs (`A > B > C`) | `project > folder > org` (a GCP concept), `TimeGenerated > ago` (a KQL operator), `db > myapp` (shell redirection) — **0 real ones** |
| Prices | 4 genuine ones, all home-lab hardware in `career` |
| Service limits | none stated as a number |

So the 184 flagged topics were essentially **all** false positives, and the freshness
anxiety behind §4 was misplaced. This site is conceptual — how BGP works, what Zero
Trust means, which key opens DevTools. That does not rot. Four claims are marked, which
is not a token sample; it is the population.

That reframes the content-age worry above. 274 topics carrying `2026-06` is not a debt,
because almost none of them assert anything that can become false. The number to watch
is `--report`, and it currently has four rows.

A third instance of the same lesson, after the hex counter and the dead classes: **the
heuristic was not just noisy, it was measuring a problem that did not exist.** Matching
claim *shape* instead of product names halved the flags, and was still wrong — it cannot
separate "Settings &gt; Devices &gt; Enrol" from "Python → Bash → PowerShell", because
the difference is meaning. Only a human marking the claim can carry that, which is why
the convention is the answer and no regex was ever going to be.

## 4b. The page budget stops the backlog at about 20% of it

Found by checking what this session's 61 cards actually cost, rather than by
reading the card counts.

```
                     session start      now       budget
elements                  78,780      82,646      93,000
headroom                     15%         11%
```

**63 elements per card**, measured over 61 cards. That leaves ~10,300 elements, so
**about 163 more cards fit before `page_budget.py` fails the build.** The backlog is
~828 cards.

This is the real constraint on `plan.md`, and it is not the one the file describes.
The header talks about ~165 working sessions; the honest statement is that the page
hits a hard ceiling roughly a fifth of the way through the backlog, and every wave
from here spends about 0.6% of what remains.

Three consequences:

1. **Track AK's lazy loading is no longer a "later" item.** It was deliberately gated
   on a measurement — `page_budget.py`'s own docstring says hitting a budget "is the
   moment to have the lazy-loading conversation, with a measurement in hand". That
   moment is now visible and close. AK should be re-read as a prerequisite for the
   second half of the content backlog, not as polish.
2. **The 15% duplicate rate found this session helps twice.** A card not written costs
   nothing in elements. If the rest of the backlog duplicates at a similar rate, the
   real runway is longer than 163 — which is an argument for running the site check
   before every wave, not just a tidiness one.
3. **Raising the budget is not the fix.** The numbers were set from a real
   measurement — 836 KB over the wire, 336 ms first paint on a throttled phone. Moving
   the ceiling without re-measuring would turn the one honest number in this file back
   into a feeling.

> **The ceiling in this section moved — see §4b-iv.** Everything measured here
> stood; what changed is which measurement the project is willing to be bound
> by. The byte ceiling was raised from 1,100 KB to 2,200 KB and `raw_mb` became
> the binding budget, on the owner's explicit call that a slow first visit does
> not matter for this site. The "~20% of the backlog" arithmetic below is
> therefore no longer the operative limit.

## 4b-ii. Lazy loading is not the win Track AK claims — measured

§4b said the page budget bounds the backlog and pointed at Track AK's lazy domain
loading as the fix. Before building it, two things were checked. Both change the
recommendation.

**First: five features read the whole DOM.** Track AK describes the work as "emit
per-domain fragments plus a shell that fetches on expand", which reads as a build
change. It is not — these all walk `.domain-section .topic` in the live document and
would silently return partial results against a lazily-loaded page:

| Feature | Function |
|---|---|
| Search | `runSearch` → `domainSections()` |
| Flashcards, quiz, quick-jump, study list, due-today | `stIndex()` |
| Domain progress badges (`n/m reviewed`) | `updateDomainProgress` |
| Expand all | `toggleAll` |
| Random topic | `jumpToRandomTopic` |

Nothing would error. The decks would just be short and search would miss, which is the
worst failure mode available — the page looks fine.

**Second, and decisive: the search index is most of the page.** `topicSearchText` indexes
`topic.textContent`, so keeping today's search behaviour means shipping essentially all
the text anyway. Measured across 1,007 topics:

```
built page, gzipped        967 KB
full-text search index     743 KB   (77% of the page)
titles only                 17 KB   ( 2% of the page)
```

So:

- **Lazy shell + today's search → saves ~224 KB, 23%.** A large, risky change for less
  than a quarter, and it adds a fetch to every first expand.
- **Lazy shell + titles-only search → saves ~950 KB, 98%** — but search stops finding
  anything by its content, which on a reference site is most of its value.

**The recommendation flips.** Track AK calls lazy loading "the single biggest performance
win available". It is not, at the current search behaviour — it is a 23% win. The real
choice is not *how* to lazy-load; it is **whether full-text client-side search is worth
77% of the page**, and that is a product decision, not an engineering one.

Cheaper things to do first, in order:

1. **Nothing.** 967 KB gzipped, 336 ms first paint on a throttled phone (measured, §AK).
   The page is not slow; it is unbounded. Those are different problems and only the
   second one is real.
2. **Trim the index, not the page — measured, and this is the option worth taking.**
   Indexing topic names, every concept title, the first sentence of each
   `.concept-desc`, and table header cells:

   ```
   full text (today)                                  743 KB   77% of page   lazy saving 23%
   names + concept titles + 1st sentences + <th>      164 KB   17% of page   lazy saving 83%
   titles only                                         17 KB    2% of page   lazy saving 98%
   ```

   **The middle tier gets 83% of the saving for a search that is still substantive** —
   on a reference site most searches are for a term that appears in a title, a concept
   heading or a table header, and all three stay indexed. What is lost is finding a word
   that appears only in the middle of a paragraph.

   That is a real behaviour change and should be a deliberate one, but it is a far better
   trade than either extreme, and it is the thing to prototype if the ceiling is ever
   actually reached.
3. **Lazy-load only the biggest domains.** `script` alone is 4h 15m of reading; a handful
   of fragments gets much of the 23% without a whole-site rewrite.

### The decision, taken in session 19: keep full-text search, do not lazy-load yet

Two more measurements settled it.

**Lazy loading's real benefit is DOM size, not bytes.** Simulated by emptying every
domain body except three, in the DOM, on a 4× throttled phone:

```
full page        87,489 elements   chip filter  60 ms
3 of 29 loaded   14,208 elements   chip filter  14 ms
                 84% fewer         4.3× faster
```

That is a better argument than the byte one — a search index shipped as JSON is not
DOM, so the interaction win survives even while keeping full-text search. Track AK
never made this argument; it argued from download size, where the case is weak.

**But the page is not slow.** Re-measured at 1,007 topics: 819 ms load on desktop,
1,615 ms on a 4× throttled phone, 60 ms to filter, search in the same range. Nothing
here is painful, and the ceiling is ~160 cards away.

**So: keep full-text search, do not lazy-load now.** The byte saving is 23%, the
interaction is already acceptable, and the change breaks five features and needs a
verification path that does not exist. Revisit when *either* the throttled load passes
roughly 3 s *or* `page_budget.py` actually fails — and when revisiting, build it for the
DOM-size argument with the 164 KB middle-tier index, not for the byte argument.

**One correction worth carrying.** The first attempt at these numbers timed the chip
filter through `page.click()` and reported 677 ms, which reads as a serious regression
and would have justified the rewrite on the spot. Timed with `performance.now()` inside
the page it is 60 ms — the rest was the test driver's round trip. **Measure interaction
inside the page.** That is now in `page_budget.py`'s docstring, next to the numbers it
would have corrupted.

Until this is revisited, **the honest position is that the budget ceiling limits the
backlog and no cheap fix exists.** That is worth knowing before another 160 cards are
written against an assumption that lazy loading will rescue it.

> **Superseded in part — see §4b-iii.** The deferral shipped, on the user's request
> rather than on this section's trigger. Everything above about *bytes* held exactly:
> it saved none, and cost 37 KB. Everything above about *DOM size* held too, and was
> understated — the measured drop was 92,330 elements to 404, not to 14,208. The one
> claim that did not survive contact is "needs a verification path that does not
> exist": the path was `tools/smoke_test.mjs`, which went from 23 checks to 31.
>
> **The recommendation this section ends on is now retired — see §4b-iv.** The
> 164 KB middle-tier search index existed to buy bytes at the cost of turning
> full-text search into partial search. Bytes stopped being the binding
> constraint, so the trade is no longer worth making: the site keeps full-text
> search and does not build the trimmed index.

## 4c. Session 19 — the `script` duplication, resolved and partly disproved

The previous session named `script` duplicating itself as the strongest remaining item.
Looked at properly, it was **one duplicate, not five**.

| Pair | Verdict |
|---|---|
| Two Big-O cards | **Genuine duplicate — merged.** |
| *How Data is Organised in Memory* vs *Choosing the Right Data Structure* | **Not a duplicate.** The first is the language-agnostic core eight; the second is Python-specific. Tiering. |
| *Data Structures — Lists & Key/Value* | **Not a duplicate.** Badged `Beginner • Core`; the site runs a deliberate beginner tier. |

**The merge preserved everything worth keeping.** The removed card's four concept-cards
were not deleted with it — three were rehoused where each belongs (the hidden-O(n²)
lesson to the surviving Big-O card, the cost table to *Choosing the Right Data
Structure*, which had semantics but no complexity column, and the recursion primer to
*Thinking in Algorithms*). Only the duplicated complexity table was dropped. The old
permalink resolves through `slug-aliases.json`, verified end to end.

**Lesson for the remaining "duplicate" candidates:** two cards on one subject are
usually a tier, not a redundancy. Check what each is *for* before merging — the
Big-O pair genuinely overlapped, and the other four did not.

## 4d. The acronym dictionary expands one way, everywhere

Found inside that work: a graph-traversal row read **"DFS (Dynamic Frequency
Selection)"**, and two Windows file-services cards had the same wrong expansion where
they meant Distributed File System. The entry's note already said *"Also Distributed
File System"* — the information was present and nothing consumed it.

**A wrong expansion is well-formed markup**, so every existing check passed it. This is
the same shape as the hex counter and the dangling cross-references: correct-looking
output, no claim being verified.

`lint_content.py` now reports these, and the first version of the check was **too broad
in exactly the way the hex counter had been**. It flagged every entry whose note
contained "also" — which caught `COPE` ("a device the user may *also* use personally")
and `FIFO` ("a Unix named pipe is *also* called a FIFO"), notes describing a synonym
rather than a second meaning, plus entries never annotated anywhere.

Narrowed to require the acronym to be **rendered in two or more domains**: ten becomes
four — `CD`, `SOC`, `VM`, `MTTR`.

**All 49 current annotations of the ten were then checked by hand, and every one is
correct.** `CD` is always inside "CI/CD"; `SOC` is Security Operations Center in all
eight domains including `grc`; `VM` is Virtual Machine in all eight including
`blueteam`'s sandbox cards. DFS was the only live defect.

So the counter measures **exposure, not debt** — four acronyms a future card could
plausibly get wrong — and the tool now says so in its output, to stop the number being
read as a backlog.

Getting a check too broad twice in one session, in the same direction, is the note worth
keeping: **the first version of a check usually matches something that co-occurs with the
claim rather than the claim itself.** Requiring evidence of real use is what fixed both.

## 5. Unknowns I cannot resolve alone

| Question | Why it is blocking | What would settle it |
|---|---|---|
| Does Calculus Ch 3 cover **parametric and polar**? | If it does, that is a real hole in the Math domain. "Vectors in Calculus" does not say | A screenshot of Ch 3's lesson list |
| Is Ch 5 (the calculator test) actually hard? | The TI-84 trainer was built with its own precondition unchecked. If Ch 5 is easy, that tool was over-build | Take the chapter test |
| More BetterU material? | `betteru.live` is blocked by this environment's egress policy. The `/sources/` pages are the mineable ones — they carry the claims and citations | Save them as `.mhtml` and attach, as with the Japanese mastery page |

## 6. Backlog reality check

`plan.md` currently holds **935 unchecked items against 331 checked**. That ratio has not
improved much, and it will not, because the file has been used as a place to record ideas
faster than they can be built.

That is not a failure — a backlog is a menu, and the "Scope paralysis" risk in the register
says exactly this. But it is worth being honest that **most of those 935 will never be
built**, and the useful part of this file is the last two hundred lines, not the first three
thousand. If it ever becomes discouraging, delete a track wholesale rather than carrying it
as debt.

## The honest short list

If only three things get done, do these:

1. ~~**Regenerate the cheat sheet**~~ — ✅ session 18. A generator now exists; the header
   is true and CI keeps it true.
2. ~~**Decide `spirit`**~~ — ✅ session 18. Folded into `philosophy`.
3. ~~**Pick one lint counter and actually move it**~~ — ✅ session 18. `hard-coded hex`:
   148 → 0, and promoted to an error so it stays there.

Everything else is optional, and saying so is the point of this section.

---

## Session 18 — what shipped, and what it cost

All three short-list items, plus the two remaining defects in §1, in one pass. The
theme through it: **every one of them was a claim nobody was checking.**

| Claim | Was | Now |
|---|---|---|
| "Generated from the Math domain" | Hand-written from 1 of 16 cards | `tools/gen_cheatsheet.py`, gated by `--check` |
| "There is a drill for this card" | Prose naming 2 of 4 areas | Generated block, gated by `--check-card` |
| `148 hard-coded hex colour` | 8 of them were not colours | Check narrowed to real paint contexts; error at 0 |
| `spirit` is a domain | 3 cards | Folded; the ≥15 rule applied for the first time |
| Windows Admin is Life Admin | Mis-filed since the split | In `endpoint` |
| `class="c-cyan"` colours a cell | Dead in 1614 first cells | Removed; lint errors on the position |
| "Verified headless (Chromium)" | Re-derived by hand each session | `tools/smoke_test.mjs`, 21 checks, in CI |

CI grew two gates and lost a warning. The generators matter more than the fixes: a
regenerated cheat sheet is worth one session, but a cheat sheet that *cannot go stale*
is worth every session after it. Same for the drill index. That is the difference
between the work above and the fourteen sessions where the TREND line did not move.

**Three things surfaced that are worth carrying forward.** All are recorded above rather
than fixed:

- **The 1069 colour-only inline styles still cannot be mechanically converted** to `c-*`
  classes, and `CONTRIBUTING.md` now says why. Worth doing eventually, one component at a
  time, with the before/after computed-style diff used above as the gate. Not worth doing
  blind.
- `lifestyle` is now the weakest chip at 4 cards, and inherits the question `spirit` just
  answered.
- ~~`VOLATILE_HINTS` still needs the same treatment~~ — ✅ done, see §4. The convention,
  the linter check and the report all exist. The finding underneath is the useful part:
  the site has four volatile claims in total, so content age was never the risk it looked
  like.

One correction to the audit above, found by doing it: §1 said to "re-run the generator"
for the cheat sheet. There was no generator to re-run. The file had been written by hand
and given a header that described an intention. Worth remembering when reading the rest
of this file — a stated capability is not evidence of one.

### The headline claim, made checkable

This file's own header has said **"Verified headless (Chromium)"** since the first
review. It was true each time somebody wrote it, and never afterwards: every session that
changed structure re-derived a throwaway script, and between sessions nothing checked it.
Same shape as the cheat sheet header.

`tools/smoke_test.mjs` is now that check — 21 assertions, run in CI as its own job. It
tests what a *structural* change breaks, not pixels:

- every filter chip has a domain section, and every section has a chip (a half-finished
  fold is silent otherwise)
- every topic has a unique id, and a cold-loaded permalink expands its card
- one study deck per studyable domain, none for a domain that is gone, and none empty
- reviewed state survives a reload
- body, diagrams and volatile marks all change colour with the theme
- no raw hex in a style attribute; Enter opens a domain and a topic; no console errors;
  no off-site requests

**The harness had the bug it exists to catch.** Renaming `.topo-svg` in a deliberately
broken copy should have failed it. Instead the theme loop skipped the now-missing
selectors and reported **19/19 passed** — a page with its diagrams destroyed, green.
Fixed by asserting presence separately from behaviour, and re-tested against four broken
copies: a deleted chip, a reintroduced literal, the renamed class, and the script tag
pointed at nothing. All four now fail, and the last one fails *readably* rather than
dying on a 30-second timeout.

That is the fourth instance this session of the same thing, and the sharpest, because it
happened to a tool built specifically to avoid it: **a check that can quietly stop
checking is worse than no check**, since it also reports success. Worth re-reading before
adding a counter, a lint rule, or an assertion to this repo.

### Content off the backlog — Tracks V1–V3 and AL1–AL3

Both remaining content items on the Phase-5 priority shortlist are done, plus two
further `infra` waves: **43 cards, eight commits**, two new domains each landing on
exactly the 15-card bar. Site 943 → **985 topics, 27 → 29 domains**.

| Wave | Domain | Cards written | Specced |
|---|---|---:|---:|
| V1–V3 Windows Server, AD DS, Group Policy | `infra` (new) | 15 | 15 |
| AL1–AL3 complexity, structures, algorithms | `cs` (new) | 15 | 15 |
| V4 identity operations | `infra` | 5 | 5 |
| V5 on-prem network services | `infra` | 3 | 5 |
| V6 certificate services | `infra` | 3 | 5 |
| V7 server operations | `infra` | 2 | 5 |
| AL4 operating system theory | `cs` | 5 | 5 |
| AL7 clocks, consensus, failure detection | `cs` | 3 | 5 |
| **Total** | | **51** | **60** |

**Track V is complete at 28 cards against a 35-card spec, and nine cards across the
session were cut rather than written.** Every cut is marked `- [~]` in the track lists
with the reason in its wave commit. `infra` 28, `cs` 23 — both well clear of the bar.

Every wave held the lint counters flat: `TREND ai-table=361 inline=1946` before the
first card and after the last, because the verdict paragraphs use a class.

**The finding that matters more than the cards: the track lists are stale, and in a
predictable direction.** Both tracks claimed a gap that was partly or wholly already
filled — Track V by `sec`'s Active Directory card, Track AL by six cards in `script`
including a claim that the material "is nowhere yet". Every track in this file was
written by looking at the *subject*, not at the *site*, and the site has moved since.

The habit that fixes it costs one command before each wave:

```
python3 -c "import re,json,pathlib; [print(d,n) for d in [x['id'] for x in
  json.load(open('data/domains.json'))] for n in re.findall(
  r'class=\"topic-name\"[^>]*>(.*?)</span', pathlib.Path(f'data/{d}.html').read_text(), re.S)]"
```

Grep it for the subject before writing. Where a card already exists, either write the
depth above it and link down — which is what both domains do — or cut the card. Do not
write the second introduction.

**Nine of sixty specced cards were cut.** That is 15%, and it is the number worth
carrying forward: a track list written against a subject rather than a site
over-specifies by roughly that much. Where the duplication concentrated:

| Cut | Already covered by |
|---|---|
| AD DS Architecture | `sec` Active Directory — Structure, Objects & Attacks |
| Big-O in Practice (as specced), Arrays & Lists, Choosing a Structure | `script`, six cards |
| Time Sync | folded into V4's Kerberos card, where the failure mode belongs |
| IPAM | nothing — cut as filler, one idea and no failure mode |
| Windows Event Log Triage | `blueteam` Windows Event Logs — The IDs That Matter |
| Windows Patching Strategy | `endpoint` Windows Autopatch, Emergency Patching |
| PerfMon & Resource Monitor | `ops` Performance & Capacity, Monitoring & Observability |
| Consistency Models, Idempotency & Exactly-Once | `devops` CAP Theorem; `eng` Idempotency, Sagas, Quorums |

**V7 was 60% already written.** A whole wave, three of five cards, sitting in three
other domains. Nothing in the track list could have told you that.

**Cutting is part of writing a wave, not a failure to finish one.** V5 shipped three of
its five specced cards: *Time Sync* because it is already the third section of V4's
Kerberos card, where a failure mode belongs; *IPAM* because it had one idea and no
failure mode, and a card whose content is "eventually use a tool" is exactly what rule
10 describes. A wave is done when the cards that earn their place are written, not when
the checkbox count matches. Cut cards are marked `- [~]` so the next reader knows the
difference between skipped and rejected.

### Detail — Track V1–V3

With the audit clear, the shortlist's remaining content item was V1–V3, "the largest
genuine subject gap on the site". Shipped: `infra`, 15 cards over three waves, one
commit each. Site is now **961 topics / 28 domains**.

Four things worth carrying into the next wave:

- **Check the neighbouring domain before writing the overview card.** `sec` already
  covered AD structure. The planned "AD DS Architecture" card would have been a
  duplicate, so V2 links to it and answers the operational question instead. The
  track list was written before that card existed and does not know about it — no
  track list does.
- **`scaffold_domain.py` had two bugs, now fixed.** It appended the chip to the *last*
  chip group regardless of fit and prefixed the icon to the chip label, so `infra`
  arrived as "🏢 🏢 WINDOWS SERVER" under *Reference*. Corrected by hand for this wave,
  then fixed in the script: `chip_label` is now the complete label, and `--group
  "Core IT domains"` picks the destination group. `m365`, `itsm`, `cs`, `hw` and `biz`
  would each have hit it. Section order still follows `domains.json`, which the script
  appends to — move the entry by hand if the domain belongs next to a relative.
- **`data/acronyms.json` is sorted by raw string**, so uppercase entries precede
  lowercase-initial ones (`mTLS`, `osquery`, `gMSA`). Sorting with a
  case-insensitive key rewrites 566 lines for no reason. Insert, then sort with
  `key=lambda e: e['a']`.
- **A wave can cost the lint counters nothing.** The 313 existing
  `style="margin-top:10px"` verdict paragraphs now have a name —
  `.concept-desc.verdict` — so 28 new ones added zero to the inline-style count.
  Converting the other 313 is still the unsafe-blind change described above; a new
  wave choosing the class is free.

### The cross-reference check — a fourth ratchet, and a fourth misdiagnosis

Writing 51 cards meant writing cross-references, and the habit of this session made the
obvious question available: *is anything checking those?* Nothing was, and four were
wrong — one naming a card that has never existed, two naming cards that had been
retitled, and one naming a card I referenced from AL1 and then never wrote.

`<span class="xref">Exact Topic Title</span>` is now the convention; `lint_content.py`
resolves every reference against real titles and suggests the nearest match on a miss.
Third ratchet at zero, after topic names and hard-coded colours.

Two things fell out of converting the sixteen references, both worth keeping:

- **The acronym annotator was rewriting the quoted titles.** It injected expansions
  inside the `xref` span, so a reference that was correct when written would fail the
  check the next time the annotator ran. `xref` is now in `SKIP_CLASSES`. Any future
  convention that quotes exact text needs the same treatment — the annotator touches
  everything it is not told to leave alone.
- **The linter was right and I was wrong, twice, about the same two strings.** I
  "corrected" two references to `DNS (Domain Name System)` and `PKI (Public Key
  Infrastructure)` using titles from a throwaway probe whose non-greedy regex had
  spliced an acronym expansion into the captured title. The real titles are *DNS Deep
  Dive — Records, Resolution & Security* and *PKI & Certificate Lifecycle*. Only
  calling `topic_label()` — the function the linter itself uses — got the right answer.

**Write the probe against the tool, not alongside it.** Four times this session a
throwaway script disagreed with a checked one, and the throwaway was wrong every time:
a `.topic.open` selector script.js never sets, a storage key that did not exist, a
notepad treated as a textarea, and now a title regex. The habit that costs least is to
import the module that already knows.

### On this session's method

Four verification failures in this session turned out to be broken *tests*, not broken
code: a `.topic.open` selector that script.js never sets, a progress probe searching the
wrong storage key, a notepad treated as a textarea when it is a compose-and-post list,
and three "broken" page copies that were merely missing their sibling `script.js`
(`index.html` is not self-contained — `build.py`'s docstring calls it that, and means
"needs no server"). Every one looked like a finding for a minute.

The habit that caught them all was cheap: **run the control.** Test the thing you did not
change, and if it fails too, the test is wrong. It cost four extra runs and prevented
four wrong entries in this file.

---

## Session record — Phase 3 finished (Tracks J–U)

This session took Phase 3 from "measured but unknown" to complete: eleven tracks
(J, K, L, M, N, O, P, Q, S, T, U — T3 and the earlier J/V/AL waves already shipped)
resolved, the site from **1,013 to 1,044 topics** across 28 domains. Roughly two dozen
genuine gap cards were written; the rest of the ~176-card Phase-3 spec turned out to be
already built in neighbouring domains.

**Cards written, by domain:**

| Domain | Cards | What |
|---|---:|---|
| `ai` (Track O) | 10 | function calling, structured output, cost/latency, observability, the transformer, training pipeline, inference internals, multi-agent, agent frameworks, agent safety |
| `threat` (Track K) | 6 | reverse engineering, anti-analysis, supply-chain attacks, the criminal economy, threat-modeling methodologies, D3FEND/Engage |
| `grc` (Track L) | 7 | ISO 27001/27002, PCI DSS, HIPAA, FedRAMP/800-53, the controls universe, data governance/eDiscovery, the regulatory landscape |
| `linux` (Track N) | 2 | Secure Boot/LUKS/integrity, package & image building |
| `script` (Track P) | 2 | Kotlin/Swift/Scala, Elixir/Haskell/niche languages |
| `military` (Track T) | 3 | MDMP & OPORD, the intelligence cycle, red teaming as a discipline |
| `mind` (Track S) | 1 | nutrition for a desk-bound brain |
| **Total** | **31** | |

Tracks M and Q were **complete by existing coverage** and got no new cards — `redteam`,
`pentest` and `net` already covered their specs tool-by-tool. Tracks S and U were
satisfied where their content already lives (`career`/`productivity`/`mind`, and the
meta/hub material), each with one honest gap recorded rather than papered over.

**The one lesson worth carrying to Phase 4.** The Track-V finding from last session —
"track lists are written against the subject, not the site" — held for every single
Phase-3 track, and this session sharpened it into a rule with two parts:

1. **Grep finds the name; the name is not the coverage.** ISO 27001, HIPAA and PCI each
   appeared as one row of a comparison table in `grc`. The word was on the site; the
   framework was not. You have to *read the card* the grep points at.
2. **"Complete by existing coverage" is a real, honest outcome** — distinct from cutting
   an item — but only when every claim is backed by a named card the next reader can
   check. Every `[x]` in the Phase-3 tracks now names the card that fills it.

Applied together, these turned a nominal ~176-card backlog into ~31 cards of genuine new
content plus a lot of careful accounting. The backlog headline at the top of this file
is inflated for the same reason, across all remaining phases — treat every future track
list as a hypothesis to check against the site, not a queue to burn down.

**Content authority.** The ten `ai` cards were written against the `claude-api` skill's
reference rather than from memory, because the API surface in exactly this area — tool
loops, `output_config.format` vs the deprecated `output_format`, prompt-caching
economics, the model IDs — moved in the last year, and a card written from recall would
teach the old shapes. Provider-specific specifics elsewhere (framework names, FedRAMP
governance, PCI/ISO version lines) are marked `volatile`; the structural facts around
them are not.

**Gate, every wave:** full lint gate green, smoke test 23/23, page budget ~8% headroom
remaining (the binding constraint now — the backlog is bounded by bytes, not ideas).
The `TREND` counters held flat across the session (ai-table=360, inline≈1965), because
every new card uses `ref-table` and classed colour, not `ai-table` or inline hex.

---

## Session record addendum — Phases 4 & 5 opened, and the budget wall reached honestly

After finishing Phase 3, the same session opened Phase 4 **and** three Phase-5 tracks —
**ten waves**, all chosen by the Phase-3 rule (audit the site first, fill genuine voids,
deepen existing domains rather than spin up new ones):

| Wave | Domain | Cards | What it filled |
|---|---|---:|---|
| Y5 — Endpoint Security | `endpoint` 29→34 | 5 | BitLocker at scale, Defender/ASR, local-admin removal + EPM, Windows LAPS, firewall/removable-media |
| Y6 — Compliance & Conditional Access | `endpoint` 34→38 | 4 | compliance policies deep, device-trust end-to-end, drift reporting, the identity/endpoint seam |
| AD — Cross-Platform Endpoint | `endpoint` 38→41 | 3 | macOS for Windows admins, Apple fleet mgmt (ABM/ADE/Jamf/FileVault), iOS/Android Enterprise |
| Z — Virtualization & Backup | `infra` 28→34 | 6 | the total void: hypervisors, overcommit, snapshots≠backups, 3-2-1-1-0, ransomware-resilient backup, restore testing/DR |
| AF — AI at Work (governance) | `ai` 44→49 | 5 | assistant deployment, shadow AI, AI acceptable use, data governance for AI, deepfake/impersonation defence |
| AC — Automation for Admins | `script` 138→140, `ops` 32→33 | 3 | Graph from PowerShell, JEA, automation risk/discipline |
| AE1 — OT/ICS Security | `sec` 46→49 | 3 | OT vs IT + Purdue model, ICS protocols, securing OT + safety-first IR |
| AR — Physical Security & Insider Threat | `sec` 49→52 | 3 | physical security systems, the insider-threat programme, internal investigations |
| AP — PQC Migration & Adjacent Crypto | `sec` 52→54 | 2 | doing the PQC migration (inventory/CBOM/agility), adjacent crypto (ZKP/HE/MPC/TEE) |
| AQ — Emerging Platforms | `net` 55→57 | 2 | modern connectivity (5G/satellite/IoT radios), edge computing |

**Total this session: 67 cards** (31 Phase 3 + 36 Phase 4/5), site **1,013 → 1,080 topics**.
Every wave found the same inflation Phase 3 did — Y1–Y3 already built, the AF1 "using AI
well" cluster already in `ai`, AC's craft waves already in `script`, AE2's regulated
industries already in `grc`, AP1's threat/standards already in Track J's PQC card. The
genuine new content was a fraction of the nominal spec, every time.

**What remains is now a decision, not more surgical waves.** The high-value
*existing-domain* voids across Phases 4 and 5 are filled. What remains is either **new
domains** (`m365` for Exchange/SharePoint/Teams, `itsm` for the service desk, `hw` for
hardware/embedded — a chip-bar and architecture decision; the bar is already a crowded
row of 28) or **narrower depth** items marked "follow on demand" in each track above
(vendor networking, AR/VR, healthcare/finance operational specifics, the business/
leadership tracks AS–AV, and the study-platform engineering tracks AG–AK).

**Where content stops, and why.** The page budget is at **~5% gzip headroom** (1,045 KB
of the 1,100 KB ceiling), down from 15% at the start of the session — 67 cards added. This is exactly the wall §4b and §4b-ii documented, and the
session-19 decision is explicit: **do not keep writing content against the ceiling on the
assumption lazy loading will rescue it.** The remaining Phase 4–6 backlog is hundreds of
cards plus three new domains (`m365`, `itsm`, and the Phase-5/6 domains), and it does not
fit under the byte ceiling as the site is built today.

**The unblock is known and deliberately not yet built.** §4b-ii's measured recommendation
is the 164 KB middle-tier search index (names + concept titles + first sentences + table
headers), which gets 83% of the lazy-loading saving while keeping substantive search —
but that is a search-*behaviour* change (product decision), and session 19 set the trigger
to build it as *"when either the throttled load passes ~3 s or `page_budget.py` actually
fails."* Neither is true yet (throttled load ~1.6 s, budget 7% clear). So the honest
position, unchanged: **the budget bounds the backlog, the unblock is specified, and it is
correctly gated on a trigger that has not fired.**

The next session that wants to add substantial content faces a genuine fork, and both
branches are decisions rather than more of the same:

1. **Build the 164 KB middle-tier search index first, then continue.** Unblocks the whole
   backlog, but changes search from full-text to substantive-but-partial — a product
   decision. Build it for the DOM-size argument (§4b-ii), not the byte one, and re-measure.
2. **Open a new domain** (`m365`, `itsm`) for the enterprise-collaboration and service-desk
   voids that have no home. Architecture decision — the chip bar is a crowded row of 28.
3. **Keep doing surgical genuine-gap waves** into existing domains, accepting each must now
   earn its bytes against a ~5.6% ceiling — perhaps 40–50 cards of runway before the budget
   actually fails and forces branch 1.

What it should **not** do is treat the inflated backlog count as a runway; it is not one.
The high-value existing-domain voids this session could reach are now filled.

> **This fork is resolved — see §4b-iii and §4b-iv.** Branch 1 is retired: bytes stopped
> being the binding constraint, so full-text search stays. Branch 3's "40–50 cards of
> runway" is superseded by a measured ~1,000. Branch 2 — whether to open `m365` / `itsm` —
> is untouched, because it was always an architecture question rather than a budget one,
> and it is now the only real fork left.

---

## 4b-iii. The deferral shipped — one domain in the DOM at a time

Asked for directly: *"I want all domains to show the other domains and only show the
content of one domain at a time to lower the processing needed."* That is §4b-ii's
DOM-size argument, and it is the half of the case that measured well.

### What was built

Not what Track AK specified. There are no per-domain fragment files and nothing is
fetched, because a fetch would have cost the `file://` story that every other decision
in this repo has protected. Instead `build.py` emits each domain's body inside an inert
block beside its header:

```html
<div class="domain-section" data-domain="net">
  <div class="domain-header">…</div>
  <div class="domain-body"></div>
  <script type="text/html" class="domain-src" data-domain="net">…the whole domain…</script>
</div>
```

The HTML parser reads that block as one text node: no elements, no style resolution, no
layout. `script.js` moves it into `.domain-body` when the domain opens and empties the
previous one. Everything still ships in one file, still works offline, still works over
`file://`, and the service worker precache list did not change.

### Measured, 4× CPU throttle, 1,080 topics

| | before | after |
|---|---:|---:|
| elements at load | 92,330 | **404** |
| elements with a domain open | 92,330 | 5,892 |
| load event | 2,739 ms | **771 ms** |
| open a domain | 125 ms | 63 ms |
| chip filter | 46 ms | 57 ms |
| first search (cold) | 1,211 ms | **243 ms** |
| search after idle warm-up | — | 13 ms |
| gzipped page | 1,044 KB | **1,081 KB** |

Two of those need their honest reading. The **chip filter got slower**, because a chip
now opens the domain it narrows to — it is doing more, not the same work worse. And the
**page got 37 KB bigger**: the topic ids `build.py` now stamps, plus the inlined id map.
§4b-ii predicted the byte case was weak; it turns out to be negative. The budget wall in
§4b is therefore **unchanged and slightly closer** — 2% gzip headroom, not 5%. Anyone
reading this section as "the content ceiling is lifted" has read it backwards.

### The five whole-DOM features, and what each reads now

§4b-ii's strongest argument against building this was that five features walk
`.domain-section .topic` and would silently return partial results. That was right, and
it was the bulk of the work. Two accessors replaced the DOM walk:

- `topicIndex()` — domain id → its topic ids, inlined by `build.py` (45 KB). Answers
  *which topics exist*.
- `domainTopics(id)` — one domain's deferred text, parsed once and cached, warmed in
  `requestIdleCallback` after load. Answers *what a topic says*.

| Feature | Was | Now |
|---|---|---|
| Search | `topic.textContent` per topic | `domainTopics()` for all 29; renders one, badges the rest with their counts |
| Flashcards, quiz, quick-jump, study list, due-today | `stIndex()` over the DOM | `stIndex()` over `domainTopics()` — 1,080 cards, 28 domains, unchanged |
| Progress badges (`n/m`) | counted `.topic.reviewed` | `topicIndex()` + `localStorage` |
| Expand all | every domain | the open domain, and it opens one if none is |
| Random topic | `document.querySelectorAll(".topic[id]")` | `topicIndex()` |

**Search changed behaviour, deliberately.** It still reads every domain — the reach is
identical — but only the open domain's hits are rendered; the rest report `n matches` on
their header and arrive already filtered when clicked. The count line says so:
`23 matches in 8 domains`.

### Verification

`tools/smoke_test.mjs` went from 23 checks to 31, including the three that would catch a
regression back to the old behaviour: no topic elements at load, opening a second domain
drops the first, and *search still reaches unopened domains*. Separately, a throwaway
parity harness hydrated all 29 domains and compared every field the study decks and the
search read — id, name, concept title, description, badge, full text — against what the
DOM produced before. **1,080 topics, one difference**, and it is the right one: the cloud
responsibility matrix, whose cells `script.js` generates at runtime and which is
therefore not in the authored text any more. Its card's prose still carries IaaS/PaaS/
SaaS; the generated words "Customer" and "Provider" are no longer searchable.

That harness earned its keep. It caught four real bugs that all failed the same way —
quietly, on a subset:

1. A topic name ending at the first `</span>` indexed *"OSI (Open Systems
   Interconnection)"* instead of *"OSI Model — 7 Layers"*, on every card carrying an
   inline acronym expansion. Fixed with a nesting-aware slice.
2. `class="concept-title"` matched exactly missed the 342 `<h4>` variants and every
   `class="concept-desc verdict"` — the field came back empty and the flashcard showed
   its fallback.
3. Replacing tags with a space rather than nothing put one inside every expansion:
   `CIDR ( Classless Inter-Domain Routing )`, which is not what the card says and so not
   what a search for it matched.
4. `<[^>]+>` as "a tag" ate `WHERE created_at < now()` in a SQL sample, because a `>`
   follows it eventually. The browser never does this: `< ` cannot open a tag.

Every one of those would have shipped looking fine.

### What it cost

- **37 KB gzipped**, above.
- **Print** covers the open domain plus every domain's header, rather than the whole
  site. That is closer to Track AK's "print packs" item than what it replaced, but it is
  a change.
- **Expand all** is domain-scoped. The old behaviour would now mean building all 29.
- One card's runtime-generated table text left the search index (above).
- `tools/page_budget.py` grew a metric: `dom_elements` (404, budget 1,500) and
  `content_elements` (86,767, budget 100,000) replace the single `elements` count, which
  no longer meant one thing.

### What this does and does not unblock

It does not unblock the content backlog — that is bounded by bytes, and bytes got
slightly worse. §4b-ii's middle-tier search index is still the fix for that, and it is
now **much cheaper to build**: search already reads a purpose-built index rather than the
DOM, so trimming what goes into that index is a change to one function, not to the page.
The fork in the session record below stands, with branch 1 unchanged and easier.

---

## 4b-iv. The byte ceiling moved, deliberately — 1,100 KB → 2,200 KB

§4b stopped the content backlog at roughly 20% of itself on a gzip ceiling. §4b-iii then
shipped the deferral and made that ceiling slightly *worse* — 1,081 KB of 1,100. The
obvious next move looked like §4b-ii's trimmed search index, bought with a downgrade from
full-text search.

It was the wrong question. The right one, asked by the owner: **why is the gzip number the
one being enforced at all?**

### The structural reason bytes are the wrong budget here

| | paid when | who pays |
|---|---|---|
| **download** (1,081 KB gzipped) | once — `sw.js` precaches the page | a first-time visitor only |
| **parse** (4.1 MB raw) | every load, cache or no cache | every visitor, every time |

This is a reference people re-open, not a landing page seen once. So the budget was
enforcing the cost that amortises to nothing and ignoring the cost paid on every visit.
That inversion is the whole finding; the rest is arithmetic.

### Measured — how the page scales with raw size

Simulated by duplicating each deferred block N times. The load path never parses those
blocks, so this is an honest model of "the same page with N times the cards". Chromium,
4× CPU throttle, medians of three, first context discarded as warm-up:

| raw size | ≈ topics | load event | search (warm) | JS heap |
|---:|---:|---:|---:|---:|
| **4.1 MB** | **1,080** | **768 ms** | **57 ms** | **14 MB** |
| 8.1 MB | ~2,150 | 1,164 ms | 97 ms | 26 MB |
| 12.2 MB | ~3,230 | 1,822 ms | 147 ms | 40 MB |
| 16.3 MB | ~4,300 | 2,298 ms | 179 ms | 69 MB |

Linear: **~125 ms of load per additional MB**. Session 19's own revisit trigger — throttled
load past 3 s — is not reached until roughly **22 MB / 5,800 topics**.

At 1,080 topics the unit costs are: **3.9 KB raw and 80 elements per topic**.

### The decision

**The owner's call, recorded as such: a slow first visit does not matter for this site.**
That is the only cost of ignoring bytes, and it falls on one population — a first-time
visitor on a slow connection. Nobody else is affected: Netlify's free allowance is ~23,000
visits a month even at four times this size, and every returning reader is served from the
service worker.

So the budget was re-derived from the measurements rather than from headroom over today:

| metric | was | now | why this number |
|---|---:|---:|---|
| `raw_mb` | 4.4 | **8.0** | ~1.2 s throttled load, ~1,000 more cards. **The binding budget.** |
| `gzip_kb` | 1,100 | **2,200** | what 8.0 MB compresses to at the measured 3.85× — a tripwire behind `raw_mb`, not a wall |
| `dom_elements` | 1,500 | 1,500 | unchanged; content growth does not move it, only new domains do (~70 domains of room) |
| `content_elements` | 100,000 | **175,000** | the library at the `raw_mb` ceiling, at 80 elements/topic |

All four now sit near 50% headroom, so whichever fails, it is the one a content wave
actually moves. `raw_mb` is set to 8.0 rather than the 22 MB the load-time data would
allow, because **a budget that will be reached is worth more than one that will not** —
at 8.0 MB, re-measure rather than assuming this table still holds.

### What this retires, and what it does not

- **Retired: §4b-ii's 164 KB middle-tier search index.** It bought bytes by making search
  partial. Bytes no longer bind, so the site keeps full-text search. This is the second
  time that recommendation has been overtaken by a measurement, which is the argument for
  taking measurements before building things, not after.
- **Retired: the "~40–50 cards of runway" in the session record.** The measured runway is
  ~1,000 cards to `raw_mb`, ~3,200 to the 3-second load line.
- **Not retired: the backlog is still inflated.** Phase 3 and the Phase 4/5 waves each
  found 60–100% of their nominal spec already written in a neighbouring domain. A bigger
  ceiling does not make the backlog count real; grep before writing, every time.
- **Not retired: the `m365` / `itsm` domain question.** That was always an architecture
  decision about a 28-chip bar, never a budget one. It is now the only open fork.

### The gap this leaves, named rather than papered over

Only one domain renders, so the worst *interaction* on the site is opening the largest
one — and no budget measures that. At 4× throttle today:

| domain | content elements | open |
|---|---:|---:|
| `acronym` | 16,511 | 127 ms |
| `script` | 13,729 | 196 ms |
| median domain | 2,220 | ~35 ms |

A domain three times the size of `script` would open visibly slowly and would pass every
budget in `page_budget.py`. The metric to add, if that becomes a real risk, is the largest
single domain's element count — not another page-wide total. It is deliberately not added
now: no domain is close, and an unfired budget is a guess.

---

## Session record — Track W opened: the `m365` domain

The first content wave since the byte ceiling moved (§4b-iv), and the first new domain since
`infra`. Written to the Phase-3 rule that has held every time since: **audit the site before
writing a line**, because the backlog count has been inflated in every wave so far.

### The audit, which decided what to build

Probed all 28 existing domains for the four candidate tracks. The result was unusually
clear-cut, and it is the reason this session opened a domain rather than deepening one:

| Probe | Mentions across the site | Verdict |
|---|---:|---|
| `mail flow`, `message trace`, `transport rule`, `shared mailbox` | **0** | genuine void |
| `purview`, `litigation hold`, `safe links`, `direct routing` | **0** | genuine void |
| `m365 group`, `files on-demand`, `group-based licensing` | **0** | genuine void |
| `sharepoint` | 1 (a passing mention in `grc`) | genuine void |
| `onedrive`, `known folder` | 2 (both in the acronym dictionary) | genuine void |
| `teams` | 76 — **every one meaning "groups of people"** | genuine void |
| virtualization, storage, backup/DR | already carded in `infra` | Track Z was right: already built |
| ITIL, change, on-call, runbooks | already carded in `ops`/`grc`/`mind` | ITSM needs no domain |
| Autopilot, boundary groups, co-management | already carded in `endpoint` | Track Y depth already there |

So the inflation rule held for three of the four candidate tracks and broke for the fourth.
Microsoft 365 — the workload most of this site's readers administer daily — had no home.

### What shipped

**`data/m365.html`, 18 cards, ~40 minutes of reading.** Site: 1,080 → **1,098 topics**, 28 → **29
domains**. The chip sits in Core IT between Windows Server and the reference domains.

| Group | Cards |
|---|---|
| Foundations | Tenant anatomy · Licensing &amp; group-based assignment · Admin roles &amp; PIM · Service Health &amp; Message Center |
| Exchange Online | Mail flow &amp; connectors · Mailbox types &amp; delegation · EOP &amp; Defender for Office · Message trace &amp; headers |
| SharePoint / OneDrive | Site architecture &amp; the limits that bite · Sharing &amp; permissions sprawl · KFM, Files On-Demand &amp; sync triage |
| Teams | What a team actually is · Governance, expiry &amp; guests |
| Purview | Retention policies vs labels · Sensitivity labels &amp; DLP · eDiscovery, content search &amp; audit log |
| Operations | Backup for M365 · The five-layer troubleshooting playbook |

**21 Track W items are now ticked against 18 cards**, because several specced items are one
card in practice — KFM and sync troubleshooting are one problem, external sharing and guest
access are covered where they actually bite. One item was deliberately *un*-ticked after
review: the unified audit log shipped, Insider Risk Management did not, and marking it done
would have been the exact failure mode this file keeps warning about.

### What the audit changed about the writing

Every card that could have restated an existing one instead points at it. Thirteen
cross-references, all resolving: SPF/DKIM/DMARC to `threat`, Conditional Access and Autopilot
to `endpoint`, Entra Connect and the backup cards to `infra`, governance-level retention to
`grc`, Copilot licensing and AI oversharing to `ai`, Graph PowerShell to `script`. The Graph
card in Track W was dropped outright on discovering
<span>Microsoft Graph From PowerShell — The Modern Admin API</span> already exists.

Eighteen `volatile` marks carry `data-checked="2026-08"` — every portal address, licence tier
claim, retention window and item limit. This is the most vendor-volatile domain on the site and
it should be re-checked more often than the others; the marks are what make that possible.

### Two things worth carrying forward

**The ceiling raise was load-bearing, immediately.** This wave took the page to **1,100.2 KB
gzipped** — which would have failed the old 1,100 KB budget by 0.2 KB. The wave that
demonstrated the ceiling was binding was the very next one written. Under the new budget it
sits at 50% headroom, and `raw_mb` is at 4.1 of 8.0.

**`stamp_freshness.py` in write mode rewrote 250 unrelated stamps.** Running it to stamp 18 new
cards re-derived every stamp on the site from `git blame` and moved ~250 topics from
`2026-06`/`2026-07` to later months, with no content change behind the move. That is the same
git-version sensitivity the CI comment already documents for `--check`. The churn was reverted
and the new cards were stamped directly.

> **Fixed in the following commit.** `--only <domain>` stamps just the files a wave touched;
> the docstring now names it as the usual case and says why. Running
> `--only m365` against the hand-written stamps produced no diff, which is the check that the
> hand-stamping and the git-derived answer agree.

### Track W after this session

Nine items remain, and they are genuinely thinner than the ones shipped: tenant-to-tenant
migration, litigation hold in mailbox terms, Teams policy packages, Teams voice and call
quality, a Purview overview, the PowerShell modules, Graph for admins (mostly covered in
`script`), usage reporting, and Insider Risk Management. A second wave of ~6 cards would close
the domain; none of them is a foundation the rest depends on.

> **Wave 2 shipped in the same session — Track W is closed.** Eight more cards, not six: Teams
> voice, Teams call quality, Teams policies and precedence, retention/hold/archiving, the
> Purview overview (carrying Insider Risk), the admin PowerShell modules, usage reporting, and
> tenant-to-tenant migration. `m365` is **26 cards**; the site is **1,106 topics / 29 domains**.
> All nine remaining items are ticked, and the wave-1 partial on Insider Risk is now complete.
> Re-audited before writing: all nine were genuine voids — `meeting policy`, `calling plan`,
> `direct routing`, `cqd`, `litigation hold`, `communication compliance`, `usage report` and
> `tenant-to-tenant` each returned **0** mentions across the other 28 domains. The only overlap
> found was network-side QoS and jitter in `net`, which the call-quality card cross-references
> rather than restates.

---

## Session record — Track BA: detection engineering as a discipline

Third content wave of the session, and the audit changed the shape of it more than any wave so
far.

### The audit: the tools were all there, the discipline was not

`blueteam` already carries 37 cards of detection *tooling* — Sigma, Sysmon, ATT&amp;CK Navigator,
Atomic Red Team, Splunk, Elastic, Wazuh, purple teaming, tuning and the Pyramid of Pain. So the
first instinct, "blueteam is well covered, pick another track", was wrong in an interesting way.
Probing for the engineering practice around those tools found this:

| Probe | Mentions site-wide |
|---|---:|
| `detection as code`, `alert tuning`, `false positive rate`, `att&ck coverage` | **0** |
| `detection engineering` | 3 |
| `sigma rule` | 2 |

The tools were documented and the practice that makes them add up to a programme was not. That
is a different kind of gap from the M365 one — not an absent subject, but an absent *altitude*.

### What shipped

**12 cards into `blueteam`**, 37 → 49. Site: 1,106 → **1,118 topics**.

| Group | Cards |
|---|---|
| The discipline | What detection engineering is · The detection lifecycle · Detection requirements |
| The data | Log source inventory &amp; telemetry gaps · Normalisation schemas (OCSF/ECS/ASIM) · Log volume &amp; cost |
| The practice | Detection-as-code · Testing &amp; regression · Measuring quality |
| The programme | ATT&amp;CK coverage mapping · The backlog &amp; retirement · Responder runbooks |

Six cross-references point back at the tool cards rather than restating them: Sigma, ATT&amp;CK
Navigator, Atomic Red Team, Sysmon, threat hunting, and the Operations runbook card.

### The spine the cards share

One argument runs through the wave, and it is worth stating in the plan because it is what makes
the cards a set rather than twelve essays: **a detection that has stopped working is
indistinguishable from a quiet environment.** The lifecycle exists to give each stage an exit
condition, the telemetry inventory exists to prove a rule *can* fire, regression tests exist to
prove it *still* fires, the coverage levels exist to stop a green square meaning "a rule exists",
and the metrics section exists because most detection dashboards measure things that go up when
the programme gets worse.

### Track BA after this wave

Eight items were left; three of them are already carded in `blueteam` and are now marked `[~]`
rather than ticked — the Pyramid of Pain, Sigma as an interchange format, and the purple-team
feedback loop all have existing homes, and writing second versions would be exactly the
duplication the audit rule exists to prevent. Five genuine items remain: enrichment, writing a
good rule, behavioural vs signature detections, correlation and sequencing, and what the role is
assessed on in interview.

> **Wave 2 shipped in the same session — Track BA is closed.** Those five, re-audited first and
> all genuine (`false-positive analysis`, `rule specificity`, `asset context`, `event sequencing`
> and `ioc-based` each returned **0** mentions site-wide). `blueteam` is **54 cards**; the site
> is **1,123 topics**. The five carry the craft-level material the first wave assumed: which
> attribute to match on and what it costs the attacker to change, false-positive analysis run on
> history before deployment rather than on analysts after it, a worked three-way detection of one
> technique, enrichment as the usual real fix for a "noisy" rule, the five correlation shapes and
> the four silent ways stateful rules break, and what the role is assessed on. Two tracks are now
> closed in one session — W and BA.

---

## Session record — Track AA: the service-desk half of `ops`

Fourth content wave. The audit result was the starkest of the session, and it also produced the
one deliberate deviation from a track's spec.

### The audit

| Probe | Mentions site-wide |
|---|---:|
| `problem management`, `known error`, `csat`, `escalation matrix`, `shift handover`, `swarming`, `ticket triage`, `service catalog` | **0** |
| everything else probed in the track | 5, total, across 29 domains |

Eight of nine probes returned nothing. `ops` already carried 33 cards, but reading its list
explains the gap precisely: incident response, incident command, postmortems, SRE, SLOs,
observability, on-call, chaos engineering — **the SRE and security half of operations, and none of
the service-desk half.** A site aimed at CompTIA-track IT professionals was missing the work most
of them actually do.

### The deviation: `ops`, not a new `itsm` domain

Track AA specifies a new domain. This wave put the cards in `ops` instead, for three reasons
worth recording so the next session does not "fix" it:

1. **The plan's own repeatedly-validated rule** is to deepen existing domains rather than spin up
   new ones. Service-desk work *is* operations; the split would have been organisational, not
   conceptual.
2. **`ops` was lopsided.** It described operations as practised by SREs and SOC analysts only.
   Adding the service-desk half makes one coherent domain rather than two partial ones.
3. **The chip bar is at 29.** The deferral shipped this session makes a 30th domain nearly free at
   load, so this is now an editorial judgement rather than a performance one — and editorially,
   one Operations domain reads better than an Operations domain and a Service Desk domain that
   cross-reference each other constantly.

`ops` is now 48 cards, which is large but within the range of `net` (57), `sec` (57) and
`linux` (58).

### What shipped

**15 cards into `ops`**, 33 → 48. Site: 1,123 → **1,138 topics**.

| Group | Cards |
|---|---|
| The model | Incident vs problem vs change vs request · Priority, impact &amp; urgency |
| The ticket | Writing a ticket someone else can solve · Triage &amp; categorisation · Escalation &amp; handover · Closing well |
| The queue | Working a queue · Service desk metrics |
| The people | Explaining technical things · Difficult conversations · Writing for users |
| The system | Knowledge management (KCS) · Self-service &amp; shift-left · SLAs, OLAs &amp; underpinning contracts · CMDB |

Four track items are marked `[~]` rather than ticked, because they already have homes: ITIL
itself, major incident management, on-call without burnout, and change enablement — that last one
is already covered in `grc` down to standard/normal/emergency changes and what a good change
request contains, so a second version would have been pure duplication.

### The thread running through the wave

Where the detection-engineering wave had "a rule that stopped working looks like a quiet
environment", this one has: **every service-desk metric has a cheat, and the cheat is usually
locally rational.** Tickets closed per agent rewards closing early. Handle time rewards rushing.
First-contact resolution rewards logging the hard part as a new ticket tomorrow. The cards say so
explicitly and pair each metric with the counter-metric that exposes its cheat, because a service
desk measured badly does not underperform quietly — it reorganises itself around the measurement.

### Track AA after this wave

Five items remain: the service catalogue and request fulfilment, the first ninety seconds of an
incident, remote support skills, ticket automation, and capacity and shift planning.

> **Wave 2 shipped in the same session — Track AA is closed.** All five, re-audited first and all
> genuine (`request fulfilment`, `first 90 seconds`, `screen share`, `ticket automation` and
> `shift planning` each returned **0** mentions site-wide). `ops` is **53 cards**; the site is
> **1,143 topics**. The wave's sharpest card is ticket automation: auto-closing "waiting on user"
> tickets improves three reported numbers — backlog length, average age, SLA attainment — while
> doing nothing for the person whose problem is unsolved, which is the metric-cheat pattern from
> wave 1 in its purest form. Also worth carrying: the queueing-theory point that utilisation above
> roughly 80% makes waiting times swing wildly, so planned slack is a feature rather than waste.
> **Three tracks closed this session — W, BA and AA.**

---

## Session record — Track AM wave 1: the applied maths behind the rest of the site

Fifth content wave, and the one that fills a gap of a different kind again. `cs` carries 33 cards
of algorithms, systems and architecture; `math` is a calculus course. Neither holds the applied
maths the *rest of the site* already depends on — the site teaches entropy, birthday attacks, p99
latency and base rates without ever giving the arithmetic behind them.

### The audit

`modular arithmetic`, `bayes`, `linear algebra`, `combinatorics`, `birthday paradox`,
`vector space` and `gradient descent`: **7 of 10 probes returned zero**, and the whole set
totalled 8 mentions across 29 domains.

### What shipped

**13 cards into `cs`**, 33 → 46. Site: 1,143 → **1,156 topics**.

| Cluster | Cards |
|---|---|
| Discrete | Modular arithmetic · Boolean algebra |
| Probability for ops &amp; security | Probability fundamentals · Bayes &amp; base rates · Distributions that matter · Percentiles &amp; latency · The birthday paradox |
| Information &amp; crypto | Entropy &amp; randomness · Primes &amp; factoring · Discrete logs &amp; elliptic curves |
| Machine learning | Vectors &amp; embeddings · Gradient descent · The curse of dimensionality |

Two further items are marked `[~]`: binary and bit manipulation is already covered by cs's number
representation card plus the subnetting cards in `net`, and information theory was folded into the
entropy card rather than split across two.

### Why this wave connects the site to itself

Each card was written to land under something the site already asserts:

| Existing content | The maths now behind it |
|---|---|
| Detection engineering's precision and noise cards | Bayes and base rates — the 99%-accurate detector producing 1% real alerts, derived |
| `Enrichment — The Context That Turns an Alert Into a Decision` | Which lever moves alert quality, and why threshold-tightening barely does |
| `SLIs, SLOs & Error Budgets`, and this session's capacity card | Percentiles, why p99 cannot be averaged, and sample-size honesty |
| Hashing, tokens and identifiers across `sec` and `web` | The birthday bound, and why 128 bits is the number |
| Password and key material across `sec` | Shannon entropy, and the five ways implementations lose randomness |
| The AI domain's embeddings and model cards | Cosine similarity, gradient descent, and the curse |

The Bayes card is the one worth flagging: the detection-engineering wave earlier in this session
argued operationally that enrichment beats threshold-tightening, and this card derives the same
conclusion arithmetically. Two waves, two altitudes, one answer — which is what a reference site
should do and mostly does not.

### Track AM after this wave

Ten items remain, all genuinely uncovered: sets and relations, proof techniques, sampling and
confidence, descriptive vs inferential, anomaly-detection maths, A/B testing, capacity
forecasting, lattices, matrices and linear transformations, and loss functions.

> **Wave 2 shipped in the same session — Track AM is closed.** All ten, re-audited and all genuine
> (`set theory`, `proof by contradiction`, `confidence interval`, `z-score`, `p-value`,
> `linear regression`, `learning with errors`, `linear transformation` and `cross-entropy` each
> returned **0**). `cs` is **56 cards**; the site is **1,166 topics**. **Four tracks closed this
> session — W, BA, AA and AM.**
>
> The second wave kept the same connective discipline as the first. The anomaly-detection card ends
> at the base-rate arithmetic from the Bayes card; the forecasting card hands off to `ops`'s
> capacity card at the point where maths becomes procurement; the matrix card lands on cache
> locality, already carded in `cs`, at the scale where it is impossible to miss; the lattice card
> stops where `sec`'s post-quantum migration card begins; and the loss-function card closes on the
> same observation as the service-desk metrics card written earlier in this session — **the moment
> a proxy becomes the target, it stops measuring what it was chosen to represent.** That sentence
> is now the site's most-repeated idea, arrived at independently in operations, detection
> engineering and machine learning, which is a reasonable sign it is true.

---

## Session record — Track AS: IT finance and procurement, into `eng`

Sixth content wave. The audit found a void of a kind the site had not filled before — not a
technology, but the commercial half of the job.

### The audit

`chargeback`, `showback`, `vendor management`, `contract negotiation`, `budget cycle` and
`true-up` returned **0**. `capex`, `opex`, `total cost of ownership` and `rfp` returned 2 each —
**every one of them from the acronym dictionary**, meaning the site could expand the abbreviation
and say nothing about the concept. Only cloud FinOps was genuinely covered, twice.

### What shipped

**14 cards into `eng`**, 36 → 50. Site: 1,166 → **1,180 topics**.

| Group | Cards |
|---|---|
| Money | CapEx vs OpEx · Building an IT budget · TCO modelling · Chargeback &amp; showback · SaaS sprawl |
| Making the case | The business case · The cost of downtime · Technical debt as a financial argument |
| Buying | Requirements before vendors · Evaluating a vendor &amp; the PoC · Negotiation for IT buyers |
| Living with it | Reading a contract as an engineer · Licensing models &amp; surviving an audit · Exit clauses &amp; lock-in |

Three items are `[~]`: cloud FinOps (carded in `cloud` and `devops`), vendor risk management
(carded three times in `grc`), and end-to-end asset management (the CMDB card written earlier this
session). Benefits realisation shipped as a section of the business-case card rather than as its
own.

### Why `eng` rather than `career`

`career` is about the individual's trajectory and personal finances; this material is about
running IT as a business function. `eng` already carries the engineering ladder, tech lead vs
engineering manager, estimation and planning, and the wider IT org — the professional-practice
cluster. These sit with those.

### The argument the wave keeps making

Engineers lose these conversations by under-claiming and by arguing in the wrong currency. Nearly
every card contains a two-column table turning an engineering statement into a business one — "the
framework is three versions behind" becomes "it leaves security support in June, which is an audit
finding and blocks the integration". The point is not persuasion technique; it is that a
consequence with a date attached is a decision someone else can own, and a technical complaint is
not.

Three specific things worth carrying: leverage is highest before you have chosen and near zero at
renewal, so almost every purchasing mistake is negotiating later on that curve than necessary; an
SLA credit is a pre-agreed refund schedule rather than an availability control, so if an outage
would genuinely hurt, the mitigation is your architecture; and process lock-in — the organisation
reshaping itself around a tool's assumptions — is the largest exit cost and the one that never
appears in the original TCO model.

### Track AS after this wave

Three items remain: hardware refresh economics, portfolio and prioritisation, and reporting to the
board.

> **Shipped immediately after — Track AS is closed.** `eng` is **53 cards**; the site is **1,183
> topics**. **Five tracks closed this session — W, BA, AA, AM and AS.** The three closers:
> hardware refresh, where the cost of keeping a machine lands in everyone else's budget and staff
> time on slow machines dwarfs the rest at fleet scale; portfolio prioritisation as deciding what
> will *not* happen, with work-in-progress limits as the free improvement organisations refuse
> because it means saying "not yet" out loud; and reporting upward, where every metric needs the
> sentence that says why anyone should care — rising cloud spend against falling unit cost being
> the success story that reads as a problem without it.

---

## Session record — Track AT wave 1: leading technical teams

Seventh content wave, and the emptiest audit of the session: seven probes for the management
craft — `one-on-one`, `interview loop`, `team topolog`, `managing up`, `giving feedback`,
`coaching` — returned **one mention in total across 29 domains**. `eng` had the *positions*
(the ladder, staff+ archetypes, tech lead vs engineering manager, influence without authority)
and nothing about the work.

### What shipped

**10 cards into `eng`**, 53 → 63. Site: 1,183 → **1,193 topics**.

| Group | Cards |
|---|---|
| The transition | Engineer to manager · The first 90 days leading a team |
| The core loop | Delegation · One-to-ones · Feedback &amp; difficult conversations |
| The people | Performance &amp; retention · Hiring · Onboarding |
| The system | Team shapes &amp; Conway's law · Managing up &amp; cross-team politics |

### The thread

Where the finance wave was about currency, this one is about a single repeated observation:
**the failure is almost always in the handover, not in the person.** Delegation that comes back
wrong had an unstated level. Feedback that lands badly was vague or late. A review that surprises
someone failed months earlier. An enabling team that became a dependency forgot that its defining
feature is leaving. Culture is not the stated values but the accumulated record of what got
addressed. Each card locates the failure in something the leader controls, which is both more
useful and more uncomfortable than the alternative.

Two things worth carrying: the delegation levels stated out loud ("decide and tell me afterwards"
takes three seconds and removes most of the ambiguity), and the arithmetic that makes "faster if I
do it" wrong at around the third occurrence — plus the part the arithmetic misses, which is that
the other person was bored and now is not.

### Track AT after this wave

Eight items remain: the manager's calendar, keeping technical enough, reference checks and offers,
planning without theatre, prioritisation under pressure, project management for technical leads,
managing incidents as a leader, and engineering team metrics.

> **Wave 2 shipped in the same session — Track AT is closed.** Five written, three marked `[~]` as
> already carded (prioritisation under pressure, incident leadership, DORA metrics). `eng` is
> **68 cards**; the site is **1,198 topics**. **Six tracks closed this session — W, BA, AA, AM, AS
> and AT.**
>
> The velocity card in this wave names the session's recurring pattern explicitly for the first
> time: velocity used to forecast is useful and velocity used as a target inflates, which is the
> same failure as the service-desk metrics, the auto-close automation and the machine-learning loss
> function. Three waves in three different domains arrived at it independently, and the card now
> says so — it is one pattern rather than three coincidences.

---

## Session record — Track BB: purple teaming as an exercise discipline, into `redteam`

Eighth content wave, and the natural completion of the detection-engineering work from earlier in
the session. That wave repeatedly pointed at purple exercises as the source of measured recall —
the only way to get a denominator for "how much did we miss" — while the site had two
single-section cards on the subject.

### The audit

`emulation plan`, `exercise scoping`, `purple exercise` and `control validation`: **0** each,
three mentions in total. `blueteam` carried *Adversary Emulation — Atomic Red Team &amp; Caldera*
and *Purple Teaming — Closing the Detection Gap*, both one concept card long. The tools were
named; the discipline of running an exercise was not.

### Placed in `redteam`, and why

The two existing cards are in `blueteam`, so keeping the cluster together had an argument. Three
things outweighed it: `blueteam` was already the largest security domain at 54 cards while
`redteam` sat at 44; the craft in these cards — threat profiling, emulation plans, rules of
engagement, lab design, safe payloads, execution — is red-side work; and the blue-side half is
already carded in detail from the detection wave, which these cross-reference six times. The
result is two domains that each hold their half of the exercise and point at each other, rather
than one domain holding both.

### What shipped

**9 cards into `redteam`**, 44 → 53. Site: 1,198 → **1,207 topics**.

| Group | Cards |
|---|---|
| Choosing the activity | Emulation vs simulation vs pentest · Building a threat profile |
| Setting it up | Emulation plans &amp; rules of engagement · Lab design |
| Running it | Purple team mechanics · Evidence capture &amp; the debrief |
| Keeping it true | Continuous validation · Avoiding emulation theatre · The report &amp; funding the next one |

### The two ideas worth carrying

**Four outcomes per technique, not two.** Prevented, detected, logged-only, and nothing. Recording
pass/fail loses the distinction that decides who does the follow-up work: "logged only" is a
detection task and the cheapest win available, while "nothing" is a logging project that no
detection can fix. Organisations routinely discover at their first exercise that they already
collect everything needed for a dozen detections nobody wrote.

**Emulation theatre is the same pattern again.** A detection written to match the emulation
framework's distinctive command line fires perfectly every exercise and never once on an
adversary. Re-running only the techniques known to pass, counting an alert nobody triages as
coverage, quietly dropping the techniques that keep failing — each is locally reasonable, and
together they produce a rising score and a static defence. This is the fourth independent
appearance of the proxy-becomes-target pattern this session, after the service-desk metrics, the
ML loss function and engineering velocity.

---

## Session record — Track AB: the operational layer under `net`'s concept cards

Ninth content wave, and the audit found a gap with a shape worth naming: `net` had 57 cards of
*concepts* — switching and VLANs, firewalls, NAT, 802.1X, wireless security, monitoring,
automation — and almost nothing at the level where someone configures or troubleshoots them.

| Probe | Mentions |
|---|---:|
| `bpdu guard`, `portfast`, `site survey`, `co-channel`, `rule order`, `session table`, `policy lookup`, `source nat`, `destination nat`, `structured cabling`, `go/no-go`, `rollback trigger` | **0** each |
| `switchport mode`, `access-list`, `show running-config`, `implicit deny`, `patch panel` | 1 each |

The site could explain what a VLAN is and not what a trunk misconfiguration looks like; what a
firewall does and not why the rule never matched.

### What shipped

**13 cards into `net`**, 57 → 70. Site: 1,207 → **1,220 topics**. `net` is now the largest domain,
which is defensible for a site whose readers are largely working toward Network+ and beyond.

| Group | Cards |
|---|---|
| Device operations | Config management, archives &amp; upgrades · Switch port configuration &amp; edge protection |
| Firewalls | Policy design &amp; rule order · NAT in practice · Firewall troubleshooting · Vendor firewall concepts |
| Wireless | RF fundamentals &amp; site surveys · Wireless troubleshooting · Controller vs cloud-managed |
| Physical &amp; field | Structured cabling, racks &amp; fibre · The field toolkit |
| Change | Cutover nights · Network documentation that stays current |

Seven track items are `[~]`: router configuration, IOS troubleshooting, enterprise Wi-Fi auth,
network monitoring, network automation, network change control and capacity — all already carded,
most of them in `net` itself.

### The through-line

Every card in this wave is written from the position of someone connected *through* the thing they
are changing. That is the difference between network operations and every other kind: the timed
reload before a risky change, out-of-band access verified before the cutover starts rather than
when it is needed, the rollback trigger agreed while everyone is rested, and never saving a
configuration until you have proved you can still reach the device. Three separate cards arrive at
the same discipline from different directions, which is why it is stated explicitly in the first
one rather than implied across all of them.

Two specifics worth carrying: PortFast without BPDU guard converts a slow-boot complaint into an
outage risk, so they are a pair and never one alone; and hairpin NAT is usually the wrong fix for
"works from home, not from the office" — split-horizon DNS is simpler, faster, and removes the
firewall from a path it does not need to be in.

---

## Session record — Track AR: external exposure, offboarding and credential cloning

Tenth content wave. `sec` already carried three AR cards from an earlier session — physical
security systems, the insider threat programme, internal investigations — so the audit was about
finding what those did *not* reach.

### The audit

The exposure sub-track was almost entirely absent: `credential exposure`, `paste site`,
`takedown` and `data broker` returned **0**, with seven mentions across the whole cluster.
`offboarding checklist` returned **0**. The physical and investigations material sat at 19
mentions, which is the three existing cards doing their job at concept level.

### What shipped

**7 cards into `sec`**, 57 → 64. Site: 1,220 → **1,227 topics**.

| Group | Cards |
|---|---|
| Seeing yourself | Mapping your own attack surface · Credential exposure monitoring |
| Being impersonated | Brand &amp; impersonation monitoring · Executive &amp; VIP exposure |
| Acting on it | Turning findings into work |
| The gaps in existing cards | Offboarding as a security control · Access credentials &amp; cloning |

### What these cards are actually about

The exposure cluster is **the same reconnaissance the Red Team domain teaches, pointed at
yourself** — and the cards say so, cross-referencing `Reconnaissance (OSINT)` directly. The
observation that makes it worth writing: an attacker's inventory of your internet-facing estate is
routinely more complete than your own asset register, because yours records what was provisioned
deliberately and theirs includes everything anyone ever stood up and forgot.

Three specifics worth carrying:

- **Dangling DNS is the finding that becomes a real compromise.** A CNAME to a deleted cloud
  resource hands your subdomain — and its trust — to whoever can claim the name next. It is created
  by ordinary decommissioning that skipped one step, which is why the fix is a checklist item
  rather than a scan.
- **Infostealer logs changed the credential-exposure problem.** They contain session cookies as
  well as passwords, so resetting the password while leaving sessions live achieves nothing, and
  the compromised thing is the device rather than the account.
- **Blocklist before takedown.** Submission to browser and mail blocklists protects users within
  minutes while removal runs for days, and the priority ordering is the part people get wrong.

### Track AR after this wave

Fourteen items remain, all in the physical-security and internal-investigations depth: access
control system internals, CCTV evidentiary quality, datacenter facility layers, environmental
monitoring, behavioural indicators, separation of duties, running an investigation, interviewing,
working with law enforcement, and investigation reports. Each is genuine and each is a *narrower*
specialism than this site's audience generally needs — the concept-level card exists for all of
them. Left open deliberately rather than marked covered: they are real gaps, just low-priority
ones, and saying so is more useful to the next session than a tick would be.

---

## Session record — Track AN6: hardware and firmware device security

Eleventh content wave, and the first to take material from Phase 5's `hw` domain plan and ship it
into an existing domain instead.

### The decision, first

Track AN scaffolds a new `hw` domain covering electronics, PC hardware, repair, peripherals,
embedded and hardware security — roughly 30 cards across six waves. AN6 is the last of those six.
Building the domain to reach its security wave is the wrong order of work: the five AN6 items are
security material, they belong to a reader who is already in `sec`, and the other five waves are a
different audience entirely. They shipped into `sec`. If `hw` is ever scaffolded, AN6 is done and
the domain starts at electronics — which is where an electronics domain should start anyway.

### The audit

Probed the whole tree for the vocabulary these cards would need:

| Probe | Mentions before this wave |
|---|---|
| `jtag` | 0 |
| `hardware root of trust` | 0 |
| `supply chain implant` | 0 |
| `chip-off` | 0 |
| `firmware update mechanism` | 0 |
| `degauss` / `shred` / `purge` (media sanitisation sense) | 0 |
| `secure boot` / `tpm` / `uefi` | present, but operational only |

The last row is the one that shaped the wave. `linux` and `endpoint` already teach Secure Boot and
BitLocker-with-TPM as *things you configure* — enrol the key, escrow the recovery key, do not break
the chain. Nothing anywhere explained what the chain proves, what it does not prove, or what an
attacker with the device in their hands actually does. That is the gap: not the settings, the
threat model underneath them.

### What shipped

**6 cards into `sec`**, 64 → 70. Site: 1,227 → **1,233 topics**.

| Card | What it is for |
|---|---|
| The Hardware Attack Surface — What Physical Access to a Device Buys | evil maid, DMA, cold boot, chip-off, and what each actually requires |
| Firmware Extraction &amp; Analysis — Getting the Code Off, and Reading It | UART/JTAG/SPI flash, the tools, and authorised-use framing |
| Hardware Root of Trust — What a Verified Boot Chain Actually Proves | secure boot vs measured boot, attestation, and the limits |
| Firmware Update Mechanisms — The Feature That Is Also the Attack Path | signing, rollback protection, A/B slots, and estates that never patch |
| Counterfeit &amp; Tampered Hardware — Provenance, Grey Market &amp; Implants | the boring risk that is common vs the exciting one that is rare |
| Media Sanitisation &amp; Disposal — What "Wiped" Actually Means | clear/purge/destroy, SSD reality, and the process failures |

### What these cards are actually about

Three specifics worth carrying:

- **Secure boot refuses; measured boot records.** They are constantly conflated and they solve
  different problems. Secure boot stops an unsigned component from running and tells you nothing
  afterwards. Measured boot lets anything run but hashes each stage into the TPM, so a remote
  verifier can see what booted. Attestation needs the second; only the second survives an attacker
  who can sign.
- **Overwriting an SSD does not do to it what it does to a disk.** Wear levelling means the
  logical block you overwrote and the flash page holding the old data are different places. The
  block-overwrite tooling everyone learned on spinning disks is theatre on flash; the answer is the
  drive's own sanitise command, or having encrypted from day one so disposal is a key deletion.
- **Targeted implants are overweighted and counterfeits are underweighted.** The interdiction story
  gets the attention; the thing that actually reaches estates is a counterfeit part with a
  relabelled controller, failing early and carrying firmware nobody can attest. Provenance is a
  purchasing control, and it is the cheapest one on this list.

### Verification

`lint_content.py` 1,233 topics / 144 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py --check` clean · `stamp_freshness.py --only sec` then `--verify` clean ·
`smoke_test.mjs` 31/31 · budget after build: raw 4.6 / 8.0 MB, gzip 1,245 / 2,200 KB,
DOM 416 / 1,500, content elements 97,401 / 175,000.

---

## Session record — Track BD: API and identity-first security

Twelfth content wave, and the largest single void found by audit so far.

### The audit

Track BD's premise is that the perimeter moved to the API and the token while the site's coverage
stayed with the network and the login page. The probe results said so bluntly:

| Probe | Mentions before this wave |
|---|---|
| `BOLA` | 0 (one unrelated hit in `math`) |
| `broken object`, `OWASP API`, `shadow API` | 0 |
| `golden SAML`, `signature confusion`, `reply URL` | 0 |
| `consent phishing`, `app consent`, `enterprise application` | 0 |
| `non-human identity`, `client credentials`, `device code` | 0 |
| `PKCE`, `JWT`, `SCIM`, `conditional access` | present — see below |

The last row is where the audit had to be careful rather than fast. Those terms appear, so a
keyword pass would call the track covered. Reading the actual cards showed what they are: a
beginner-level `sec` card explaining what a token is and how OAuth2 roles fit together, plus `web`
cards on sessions, cookies and federated identity. All correct, all pitched at first contact. None
of them is about attacking or defending any of it.

Two items were therefore deliberately *not* written. `alg: none` and the revocation problem are
already taught in the existing API card, and a standalone JWT-security card would have been a third
telling of the same material — algorithm and key confusion went into the federation card instead,
where the golden-SAML material gives them a reason to exist. Authentication-vs-authorization is
likewise already carded; its API-specific consequence lives inside the BOLA card, which is the only
place it changes what a reader does.

### What shipped

**8 cards into `sec`**, 70 → 78. Site: 1,233 → **1,241 topics**.

| Group | Cards |
|---|---|
| API security (BD1) | The OWASP API Security Top 10 · Broken Object-Level Authorization · API Abuse &amp; Rate Limiting · API Inventory &amp; Shadow APIs |
| Identity-first (BD3–BD4) | Federation Attack Surface · OAuth Consent Phishing · Third-Party App Governance · Non-Human Identity |

### What these cards are actually about

The connective idea across all eight: **every one of these attacks is legitimate use of a working
system.** No exploit, no malformed input, no bypass. That is why the existing control set misses
them, and it is what makes them worth eight cards.

Four specifics worth carrying:

- **BOLA is a missing line, which is why review never catches it.** The endpoint validates the
  token, loads the record by ID, returns it. Nothing in the diff looks wrong because the wrongness
  is an absence. Scoping the query by tenant beats a separate ownership check — a check can be
  forgotten on the next endpoint, a repository that will not return cross-tenant rows cannot be.
- **Unguessable identifiers are not an authorization control.** Worth doing, and it stops trivial
  enumeration, but identifiers leak through shared links, exports, webhooks and support tickets.
  The real test needs two accounts and a replay, and it belongs in the pipeline.
- **Consent phishing defeats every anti-phishing control by being genuine.** Real domain, real
  certificate, real login, real MFA. The password reset afterwards changes nothing, because the
  refresh token survives it. Prevention is a tenant setting; response is revoking the grant, not
  the credential.
- **Machine identities outnumber humans and no part of the identity lifecycle reaches them.** No
  joiner, no leaver, no MFA, and an access review that stalls because nobody can say what the
  account is for. The card ends on rotation rehearsal, because a team that does not know what
  breaks when a credential rotates will, under incident pressure, choose to leave the attacker's
  access in place.

### A stamp correction worth recording

`stamp_freshness.py --only sec` moved 25 topics from `2026-08` back to `2026-07`. That looked like
the blame-drift hazard the tool's own docstring warns about, and it is the opposite: those are
foundational cards — Active Directory, TLS, password hashing, threat modelling — that an earlier
whole-tree run had wrongly bumped forward. `git log -S` on their content confirms the real last
edit was July. The `--only` path corrected them. Recorded here so a future session reading the diff
does not "fix" it back.

### Track BD after this wave

BD2 (tokens) is the remaining substantive gap: OAuth 2.1 flow changes and PKCE, token lifetime and
rotation, machine-to-machine auth, and a secrets/tokens/keys taxonomy. Worth writing, and it should
be written as one card about token lifetime rather than four that re-explain what a token is. BD3
is otherwise complete — conditional access and privileged-access tiering are already carded in
`m365`, `endpoint` and `infra`.

### Verification

`lint_content.py` 1,241 topics / 150 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py` clean · `stamp_freshness.py --verify` clean · `smoke_test.mjs` 31/31 ·
budget after build: raw 4.7 / 8.0 MB, gzip 1,257 / 2,200 KB, DOM 416 / 1,500, content elements
98,092 / 175,000.

---

## Session record — Track BE: software supply chain and integrity

Thirteenth content wave. The whole track, in one pass, into `eng`.

### The audit

| Probe | Mentions before this wave |
|---|---|
| `in-toto`, `reproducible build`, `artifact repository`, `golden image` | 0 |
| `VEX` | acronym list and one unrelated `linux` hit only |
| `dependency confusion` | 1, in `threat` |
| `SLSA`, `sigstore` | present in `devops` and `threat` |
| `SBOM` | present in four domains |

The middle rows made this an audit that had to read rather than count. `devops` carries *Software
Supply Chain Security — SBOM…* and `sec` carries *Supply Chain Security — Trust What You Build
With*; both are real cards and both are roughly three concept cards long. Reading them showed the
shape: they name SBOM, SLSA and sigstore and say why each matters. Nothing anywhere says what a
SLSA level costs you, how keyless signing removes the key, what a VEX justification has to contain,
or what you do in the hour after a dependency you ship turns out to be malicious.

### The domain decision

The plan targets `eng` / `sec`. It went entirely to `eng`, for two reasons. The material is about
how software gets built — the reader who needs it is the one already thinking about builds,
pipelines and dependencies. And `sec` had just reached 78 topics in the previous wave while `eng`
sat at 68; concentrating a third supply-chain cluster in `sec` would have made the largest domain
larger while leaving the engineering domain without the material its own readers need. The new
cards cross-reference `devops` for policy-as-code and registry mechanics, and `ops` for incident
response, so the existing cards stay the entry points they already were.

### What shipped

**8 cards into `eng`**, 68 → 76. Site: 1,241 → **1,249 topics**.

| Group | Cards |
|---|---|
| Understanding the chain (BE1) | Where a Build Actually Comes From · Dependency Risk |
| Provenance (BE2) | SLSA Levels · Signing, Sigstore &amp; Attestation · Verifying at Deploy Time |
| Operating it (BE3) | SBOM in Practice &amp; VEX · Dependency Triage &amp; Update Strategy |
| Internal chain (BE4) | Securing the Pipeline |

### What these cards are actually about

The organising observation, stated in the first card and paid off in the last: in every one of these
attacks **nothing goes wrong on the victim's side.** The repository is untouched, the reviews
happened, the signature verifies. That is why signature-checking and publisher-verification controls
do not fire — the attacker satisfied both. It is also the argument for provenance: *which build,
from which source, on which system* names facts an attacker cannot fabricate by holding a key.

Four specifics worth carrying:

- **`cosign verify $IMAGE` on its own is close to meaningless.** Keyless signing is open by design,
  so a valid signature only proves somebody signed. The control is `--certificate-identity-regexp`
  anchored to the start of the string, plus the issuer, plus verifying by digest rather than by a
  mutable tag.
- **Pinning and a working update process are one control, not two.** Pinning defends against
  takeover, protestware and republished versions, and it also stops security fixes arriving. The
  combination that works is a cooling-off delay on new releases plus auto-merge once they have aged.
- **Generating provenance and verifying it are different projects, and the second is the control.**
  Generation breaks nothing so it ships; enforcement can stop a deploy so it is deferred. The
  rollout sequence in the deploy-time card exists because every failed attempt at this control
  fails the same way — global enforcement on a Tuesday, universal exemption by Thursday.
- **A compromised dependency is not a vulnerability to patch.** It is code that already executed on
  developer machines and CI runners. Removing the package restores a clean tree and does nothing
  about the credentials read an hour after install; the runners are compromised hosts and their
  secrets are burned.

### Track BE after this wave

Two items left open deliberately, both marked `[~]` above: artifact repositories, already carded in
`devops`; and developer-workstation trust, whose endpoint half is in `endpoint` and whose
commit-signing half is a genuine small gap.

### Verification

`lint_content.py` 1,249 topics / 153 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py` clean · `stamp_freshness.py --only eng` touched only the 8 new cards, no
churn · `--verify` clean · `smoke_test.mjs` 31/31 · budget after build: raw 4.7 / 8.0 MB, gzip
1,269 / 2,200 KB, DOM 416 / 1,500, content elements 98,725 / 175,000.

---

## Session record — Track BC: cloud-native and Kubernetes security

Fourteenth content wave. Waves BC1–BC4 into `cloud`; BC5 (serverless and managed services) left for
a later pass.

### The audit

| Probe | Mentions before this wave |
|---|---|
| `service account token`, `token projection` | 0 |
| `hostPID`, `container forensic` | 0 |
| `namespaces are not a security boundary` | 0 |
| `kubelet` | 1, in `redteam` |
| `pod security standard`, `default-deny`, `Falco`, `Tetragon` | present, scattered |

The scattered row needed reading rather than counting, and what it found was thin: the entire
site's Kubernetes security coverage was one `devops` card (*Kubernetes Security — RBAC…*, three
concept cards), one `devops` container-hardening card, and one `redteam` attack card
(*Kubernetes Attacks*, 4.4 KB, two concept cards). Those are correct and they are introductions.
Nothing said what `create pods` is actually equivalent to, why every pod carries an API credential,
what a NetworkPolicy does on a CNI that does not implement it, or why killing a compromised pod
destroys the evidence.

### The domain decision

The plan targets `cloud` / `blueteam`. All eight went to `cloud`: the reader who needs this is
already thinking about cloud-native infrastructure, and `cloud` was at 49 topics against
`blueteam`'s 54. The cards cross-reference `devops` for policy-as-code and service-mesh
architecture, `redteam` for the offensive walkthrough, `blueteam` for detection-as-code, and `ops`
for incident response — so every neighbouring domain keeps its existing entry point.

### What shipped

**8 cards into `cloud`**, 49 → 57. Site: 1,249 → **1,257 topics**.

| Group | Cards |
|---|---|
| Threat model (BC1) | The Kubernetes Threat Model · Kubernetes RBAC Deep · Service Account Tokens &amp; Workload Identity |
| Hardening (BC2) | Container Breakout Paths &amp; Pod Security Standards |
| Network &amp; tenancy (BC3) | Network Policies &amp; Service Mesh · Kubernetes Multi-Tenancy |
| Runtime &amp; response (BC4) | Runtime Security &amp; Audit Logs · Incident Response in Kubernetes |

### What these cards are actually about

The through-line: **Kubernetes hardening is almost entirely about changing defaults, not about
finding vulnerabilities.** Every path in these cards is open in a fresh cluster and closable from a
manifest. That is why the wave reads as configuration rather than exploitation, and why the
threat-model card is drawn from inside one pod rather than from the control plane down.

Four specifics worth carrying:

- **Several ordinary-looking RBAC verbs are cluster-admin.** `create pods` means running as any
  service account in the namespace; `pods/exec` means taking over an existing workload's identity;
  write access to a mutating webhook means rewriting every object entering the cluster. Nothing in
  a role definition says so, which is why RBAC reviews that read like least-privilege often are not.
- **Every pod is issued an API credential it did not ask for.** `automountServiceAccountToken:
  false` is a one-line fix for workloads that never call the API, which is most of them. And the
  legacy-versus-projected distinction decides whether a stolen token expires or works forever from
  anywhere.
- **A NetworkPolicy on a CNI that does not implement it applies cleanly and does nothing.** The
  object appears in `kubectl get` either way. Also: default-deny egress blocks cluster DNS, which is
  what breaks every first attempt and looks nothing like a network-policy problem.
- **Killing a compromised pod destroys the evidence and redeploys the vulnerability.** The
  containment move is removing the label the controller's selector matches — the workload heals, the
  original keeps running, and you get to investigate. Under pressure, availability wins unless the
  team already knows this trick.

### Track BC after this wave

Three items open, all recorded above: secrets in Kubernetes (the options comparison), ingress and
API exposure, and the whole of BC5 — serverless threat model, managed-service trust boundaries, IaC
scanning, cloud detection engineering and cloud incident response. BC5 is the natural next wave in
this area; note that `sec` and `redteam` already carry parts of the cloud-detection and
credential-attack material, so it needs the same read-not-count audit this one got.

### Verification

`lint_content.py` 1,257 topics / 159 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py` clean · `stamp_freshness.py --only cloud` touched only the 8 new cards ·
`--verify` clean · `smoke_test.mjs` 31/31 · budget after build: raw 4.8 / 8.0 MB, gzip 1,281 /
2,200 KB, DOM 416 / 1,500, content elements 99,393 / 175,000.

---

## Session record — Track BC5: serverless, managed services and cloud response

Fifteenth content wave, and it closes Track BC apart from three recorded items.

### The audit

| Probe | Mentions before this wave |
|---|---|
| serverless security / lambda permissions | 0 |
| `checkov`, `tfsec`, `terrascan`, "IaC scanning" | 0 |
| "cloud detection" | 0 |
| snapshot forensics, credential revocation, blast-radius containment | 0 |
| `CloudTrail`, `GuardDuty`, "shared responsibility" | present |

The present row is named in passing: `cloud` and `redteam` mention CloudTrail as a thing that
exists, and shared responsibility appears as the standard diagram. Nothing treated the control-plane
log as a detection source with rules attached, and nothing said where the responsibility line
actually sits for a given service class — which is the only form of that diagram anyone can act on.

### What shipped

**5 cards into `cloud`**, 57 → 62. Site: 1,257 → **1,262 topics**.

Serverless Threat Model · Managed Service Trust Boundaries · IaC Security Scanning ·
Cloud Detection Engineering · Cloud Incident Response.

### What these cards are actually about

The organising claim: **in the cloud the API call is the attack, and the identity is the asset.**
Every card lands somewhere on that. It is why cloud incident response starts by asking which
identity acted rather than which host is compromised, why the control-plane log is the primary
telemetry, and why serverless concentrates risk into an execution role.

Four specifics worth carrying:

- **A serverless execution environment is reused between invocations.** Warm starts are the same
  container, so a credential or a user's data cached in a global variable is readable by the next
  caller, and files written to the temp directory survive. The mental model says each invocation is
  fresh; it is not.
- **Deleting an access key does not stop the session.** Temporary credentials already issued stay
  valid for their full lifetime, so the immediate containment control is an explicit deny policy on
  the role — before any cleanup.
- **Preserve before you contain.** Terminating a compromised instance destroys memory, and
  auto-scaling may do it for you while you are deciding. Snapshot and isolate; never terminate as a
  first move.
- **Logs stored in the account being attacked are evidence the attacker can edit.** Organisation-wide
  logging to a separate locked account is the prerequisite that makes every detection in these
  cards trustworthy, and it is a configuration decision made months before it matters.

The IaC card carries a smaller point worth keeping: the same rule fires in a posture tool and in a
scanner, and finding it three days earlier changes nothing about the rule and everything about the
economics. Both are needed — the scanner sees what the code declares, posture management sees what
exists, and each is blind exactly where the other looks.

### Track BC after this wave

Complete except: secrets in Kubernetes (the options comparison), ingress and API exposure as a
control point, and image security, which is already carded in `devops` and `linux`. All three are
marked in the track above.

### Verification

`lint_content.py` 1,262 topics / 163 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py` clean · `stamp_freshness.py --only cloud` touched only the 5 new cards ·
`--verify` clean · `smoke_test.mjs` 31/31 · budget after build: raw 4.8 / 8.0 MB, gzip 1,288 /
2,200 KB, DOM 416 / 1,500, content elements 99,819 / 175,000.

---

## Session record — Track BF: privacy engineering

Sixteenth content wave.

### The audit

| Probe | Mentions before this wave |
|---|---|
| `pseudonymisation` / `pseudonymization` | 0 |
| `tokenisation` / `tokenization` | 0 |
| `DSAR` / "subject access" | 0 |
| "consent management" | 0 |
| "cross-border transfer" | 0 |
| "telemetry design" | 0 |
| differential privacy, re-identification, data minimisation, privacy by design, purpose limitation | present in `grc` |

The present row is four existing `grc` cards: *Data Privacy Techniques*, *Privacy Regulations*,
*Privacy Law*, and *Data Governance, Retention &amp; eDiscovery*. Reading them showed they are the
compliance half, and a good one — k-anonymity, differential privacy, GDPR vocabulary, data subject
rights, retention as governance. What none of them does is tell an engineer how to build the
system: how to make purpose limitation hold in a warehouse, what actually happens to a record when
you delete it, how to answer a subject access request without consuming a team, or how to honour a
withdrawn consent in the six systems that took a copy.

That gap is exactly Track BF's stated premise — *GRC proves compliance, privacy engineering builds
systems that do not need much proving* — so the first card was written to name the distinction
explicitly rather than assume the reader arrives with it.

### The domain decision

Track BF targets `grc` / `eng`. All eight went to `grc`, which is where a reader looking for privacy
will look, and where the four compliance cards already sit so the two halves cross-reference each
other. `grc` was also among the smaller domains at 36 topics; `eng` had just taken the supply-chain
wave and stood at 76. The new cards carry the badge **Privacy Engineering**, distinct from the
existing **Privacy** badge, so the two halves are visually separable within the domain.

### What shipped

**8 cards into `grc`**, 36 → 44. Site: 1,262 → **1,270 topics**.

Privacy Engineering vs Compliance · Data Inventory &amp; Flow Mapping · Purpose Limitation in a Data
Warehouse · Tokenisation &amp; Format-Preserving Encryption · Deletion That Actually Deletes ·
Subject Access Requests at Scale · Consent, Preferences &amp; Tracking · Telemetry Design &amp;
Privacy Incident Response.

### What these cards are actually about

The through-line: **almost every default in modern architecture works against privacy, and none of
them was chosen to.** Soft deletes, event sourcing, backups, replicas, caches, warehouses,
generous telemetry — each is good engineering, and collectively they are why an organisation with
excellent privacy documentation frequently cannot delete a person.

Four specifics worth carrying:

- **Pseudonymised data is still personal data.** Identifiers replaced but the mapping retained
  anywhere means every obligation continues to apply. Calling it anonymous is the single most
  consequential mistake in this area, and it is usually made in good faith.
- **Data minimisation is the only control that removes categories of risk rather than managing
  them.** Not collecting a field removes the breach, the access review, the retention schedule, the
  subject-access search and the deletion job at once, permanently. Every other control is ongoing
  work with an ongoing failure rate.
- **Backups are settled practice, not the hard part.** Regulators accept that backups cannot be
  surgically edited; what is expected is a defined expiry and a documented process so a restore does
  not resurrect erased records. The hard parts are search indexes, event streams and the analytics
  warehouse — the one-way pipelines nobody propagates deletions into.
- **The seventy-two hours include the weekend, and awareness starts with the support agent.** The
  common failure is a security team resolving an incident competently while nobody asks whether
  personal data was involved. The fix is a standing assessment step inside the existing incident
  process, not a parallel privacy process.

### A second stamp correction

`stamp_freshness.py --only grc` moved 16 topics from `2026-06` to `2026-07`. As with the `sec` case
in the API wave, this is a correction rather than drift: `git log -S` on those cards' titles shows
them created in commit d38592c, dated 2026-07, so 2026-06 was stale. Recorded for the same reason —
so a later session reading the diff does not reverse it.

### Track BF after this wave

One item genuinely open: third-party data sharing, whose contract half is in `grc`'s vendor cards
and whose technical-verification half is unwritten. Everything else is either shipped or already
carded elsewhere, marked `[~]` in the track above with the location.

### Verification

`lint_content.py` 1,270 topics / 167 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py` clean · `stamp_freshness.py --verify` clean · `smoke_test.mjs` 31/31 ·
budget after build: raw 4.8 / 8.0 MB, gzip 1,301 / 2,200 KB, DOM 416 / 1,500, content elements
100,530 / 175,000.

---

## Session record — Track BG: platform engineering and the internal developer platform

Seventeenth content wave. The whole track, in one pass, into `devops`.

### The audit

| Probe | Mentions before this wave |
|---|---|
| "paved road" / "paved path", "platform as a product" | 0 |
| "thinnest viable platform", "self-service infrastructure" | 0 |
| "ephemeral environment", "service catalog" / "scorecard" | 0 |
| "inner loop" / "outer loop", "onboarding to first commit" | 0 |
| "platform SLO" | 0 |
| `golden path`, `cognitive load`, `developer portal`, `Backstage` | present |

The present row is one `devops` card — *Platform Engineering &amp; the Internal Developer
Platform* — whose four concept cards are golden paths, the commit-to-production pipeline, CI in the
repository, and which CI tool to pick. Three of those four are really CI/CD material. The card names
the discipline and then teaches pipelines, which is a reasonable card and leaves the discipline
itself unwritten.

### What shipped

**8 cards into `devops`**, 36 → 44. Site: 1,270 → **1,278 topics**.

Why Platform Engineering Exists · Platform as a Product · Golden Paths &amp; the Thinnest Viable
Platform · Developer Portals, Service Catalogues &amp; Scorecards · Self-Service Infrastructure &amp;
Environment Management · Platform SLOs &amp; Migrating Consumers · Measuring Platform Success ·
Developer Experience.

They carry a **Platform** badge, so the cluster is separable from the domain's DevOps and Delivery
material.

### What these cards are actually about

The through-line is a constraint rather than a technique: **a platform only stays good while its
users could leave.** Voluntary adoption is what forces it to be genuinely faster than the
alternative; mandate it and the feedback that would have corrected the roadmap arrives as
complaints to management instead. Nearly every anti-pattern in the wave is downstream of losing
that constraint.

Four specifics worth carrying:

- **Not all cognitive load should be removed.** Extraneous load — pipelines, wiring, provisioning —
  is the entire mandate. Germane load, the effort that builds understanding of how your system
  fails, must be protected: hiding production behaviour from the team that owns the service
  relocates the understanding away from whoever is paged at three in the morning.
- **A gate and a guard rail address the same risk and charge differently.** A gate charges every
  request the latency of a human, forever, to catch the rare bad one. A guard rail charges
  engineering effort once. Almost every gate in a real organisation defends against the exceptional
  case while billing the common one.
- **The seed dataset decides whether ephemeral environments are useful.** Per-pull-request
  environments are the highest-value capability on the list, and an environment with no realistic
  data only proves the service starts. Building a good synthetic seed set is the unglamorous part
  and it is the actual work.
- **A platform team ships no product, which makes it permanently fundable and permanently
  cuttable.** Its output is other teams going faster, which is invisible unless measured and which
  those teams will attribute to their own competence. Measurement is the only evidence — and it
  equally catches the platform team that genuinely is not helping.

The developer-experience card carries the observation that most surprises people: platform attention
goes to the outer loop because that is where the infrastructure is, while the hours are in the inner
loop. A two-minute rebuild does not cost two minutes; it costs the context that fell out of the
engineer's head while they waited, and a cycle slow enough to break concentration pushes people
toward larger batches — the opposite of what the outer-loop investment was for.

### A third stamp correction

`stamp_freshness.py --only devops` moved three topics: two CI/CD cards from `2026-08` to `2026-07`
and one Kubernetes card from `2026-06` to `2026-07`. All three trace to commit a5f941f, the August
commit that split the old `ops` domain into `ops` and `devops`. That is a file move, not an edit —
exactly the mechanical-commit case the tool's `--ignore-rev` classification exists for — so looking
through it to the pre-split date is correct behaviour, not drift. Third such correction this
session; the pattern is consistent enough to state plainly: **when `--only` moves an old stamp,
check whether a mechanical commit inflated it before assuming the tool is wrong.**

### Track BG after this wave

Complete. Two items are marked `[~]` because they were already carded in this same domain — paved-
path CI/CD and policy as code — and the new cards point at them rather than restating them.

### Verification

`lint_content.py` 1,278 topics / 167 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py` clean · `stamp_freshness.py --verify` clean · `smoke_test.mjs` 31/31 ·
budget after build: raw 4.9 / 8.0 MB, gzip 1,312 / 2,200 KB, DOM 416 / 1,500, content elements
101,187 / 175,000.

---

## Session record — Track BH: observability engineering

Eighteenth content wave.

### The audit

| Probe | Mentions before this wave |
|---|---|
| "wide event" | 0 |
| `cardinality` | 1, in `data`, about database indexes |
| OpenTelemetry, distributed tracing, error budget, SLI, SLO, observability | present in `ops` and `cloud` |

The present row was the whole audit, and it needed reading rather than counting. `ops` carries
seven observability cards, and their sizes tell the story: *Monitoring &amp; Observability* is
2.2 KB, *Golden Signals* 1.2 KB, *SLIs* 1.0 KB, *Prometheus &amp; Grafana* 2.2 KB,
*Distributed Tracing &amp; OpenTelemetry* 4.7 KB. They teach what a metric is, what a span is, that
OTel exists, and that you should alert on symptoms — twice, in two different cards.

None of them touches the decisions that actually shape an observability practice: what a label
costs, what to do when the trace you need was sampled away, where to put a policy that applies to
every signal, or what happens when the error budget runs out and nobody has agreed what happens.

### What shipped

**8 cards into `ops`**, 53 → 61. Site: 1,278 → **1,286 topics**.

Cardinality · The Three Signals &amp; Wide Events · Instrumentation Strategy · OpenTelemetry
Architecture &amp; the Collector · Sampling · Debugging With Traces, Correlation &amp; Dashboards ·
Choosing SLIs &amp; Setting an SLO That Survives · Error Budgets, Policy &amp; Why SLOs Fail.

### What these cards are actually about

The through-line: **every observability decision is a decision about what you will not be able to
ask later.** A label you did not add, a trace that was sampled away, a field left out of an event —
each is a question that becomes unanswerable at the exact moment it matters. The cards are
organised around making those trade-offs explicit while they are still cheap.

Four specifics worth carrying:

- **Cardinality multiplies and the multiplication is invisible in the code.** One extra label
  argument turns a hundred series into a hundred thousand. The rule that prevents nearly all of it:
  a metric label must have a bounded set of values you could write down; anything else belongs in a
  trace or an event, where the cost model is per-event rather than per-combination.
- **Uniform sampling discards precisely what you needed.** An error affecting one request in ten
  thousand, sampled at one percent, is captured once per million requests — so during the incident,
  the trace does not exist. Bias the policy on purpose: keep everything unusual, keep a thin
  baseline. And once you do, trace counts are no longer traffic counts, which is its own class of
  confidently wrong dashboard.
- **The collector is the most useful component in the stack and is usually skipped.** It is the one
  place every signal passes through, so redaction, label allow-lists, cost control, tail sampling
  and backend migration all belong there — none of them requiring an application change.
- **SLO programmes fail organisationally, not technically.** The technical work is a week. The
  failure that does lasting damage is tying an SLO to someone's performance review: it stops being
  a measurement and becomes a target to manage, incidents get reclassified, and the organisation
  loses the ability to see its own reliability long after the programme ends.

The instrumentation card carries the observation most likely to change what a reader does tomorrow:
a service can return HTTP 200 to every request while placing no orders, and every technical
dashboard will show a healthy system. Every service needs at least one metric a non-engineer would
recognise as the thing it is for.

### Track BH after this wave

One item genuinely open: reporting reliability to the business as distinct from to engineering. Four
items are marked `[~]` with their existing location — the monitoring/observability distinction,
OTel instruments and views, and symptom-based alerting, which `ops` already carded twice.

### Verification

`lint_content.py` 1,286 topics / 169 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py` clean · `stamp_freshness.py --only ops` corrected three stamps to 2026-07
(`git log -S` confirms commit d38592c, dated July — the fourth such correction, per the rule
recorded in the platform-engineering session record) · `--verify` clean · `smoke_test.mjs` 31/31 ·
budget after build: raw 4.9 / 8.0 MB, gzip 1,324 / 2,200 KB, DOM 416 / 1,500, content elements
101,920 / 175,000.

---

## Session record — Track BJ: resilience, plus a real bug in stamp_freshness.py

Nineteenth content wave, and the most heavily pre-covered track audited so far.

### The audit

`ops` already carries five strong incident cards — *Chaos Engineering* (4.9 KB, with the method,
running an experiment, what to inject, and a "don't start here" caveat), *Incident Command*,
*Writing a Postmortem People Actually Learn From*, *Writing Runbooks That People Actually Follow*,
and *On-Call Done Humanely*. `eng` carries *Designing for Failure* and *Resilience Patterns —
Circuit Breaker, Retry &amp; Timeout*.

That is roughly half of Track BJ already written, and written well. So this audit was mostly about
finding what the twenty planned items contain that those seven cards do not:

| Probe | Mentions before this wave |
|---|---|
| "shuffle shard", `gameday`, `FMEA` | 0 |
| "near-miss" | 2, both in a threat-intel sense |
| `bulkhead`, "load shedding" | 1 each, in `eng`, in passing |

**7 cards into `ops`**, 61 → 68. Site: 1,286 → **1,293 topics**. Twelve of the twenty track items
are marked `[~]` with the card that already covers them — the largest proportion of any track this
session, and the honest result.

Blast Radius Design · FMEA for Systems · Load Shedding &amp; Graceful Degradation · GameDays &amp;
Chaos Maturity · Near-Misses &amp; Incident Metrics · Resilience Engineering &amp; Organisational
Memory · Alert Fatigue &amp; Runbook Quality.

### What these cards are actually about

Four specifics worth carrying:

- **Congestion collapse has a recognisable dashboard signature:** high CPU, high queue depth,
  near-zero successful throughput, every latency percentile pinned at the timeout. A system showing
  that shape is spending all its capacity on work that will be discarded, and refusing ten percent
  of requests immediately would serve the other ninety.
- **Shuffle sharding is combinatorics doing reliability work.** Two workers each from a pool of
  eight gives twenty-eight distinct pairs, so one abusive tenant affects the handful who share both
  of its workers rather than a whole shard. It contains nothing if the workers share a database.
- **"Human error" is where the investigation stopped.** The action made sense to the person given
  what they could see; understanding why it made sense is what produces a fix. And the gap between
  the documented procedure and what people actually do is usually *why the system works* — treat a
  deviation as a question before treating it as non-compliance.
- **A noisy pager is an outage you have not had yet.** It is a technical defect, not only a
  wellbeing one: an engineer who has learned the pager is usually wrong acknowledges the real page
  more slowly. Track the proportion of pages that led to action; below about half, the pager is
  training people to ignore it.

### The bug: stamps were oscillating

This wave's stamping run moved three `ops` topics from `2026-07` back to `2026-08` — the exact three
the previous wave had moved from `2026-08` to `2026-07`. Not drift: a genuine cycle, and worth
recording because four earlier "corrections" this session were the same mechanism seen from one side.

**Cause.** A topic's date was `max()` over the blame times of every line in its span, including the
opening `<div class="topic" data-reviewed="…">` line — the line the script itself rewrites. Writing
a corrected stamp inside a commit that also adds real content makes that commit non-mechanical, so
it cannot be ignored when blaming; blame then dates the opening line to that commit, `max` picks it
up, and the topic moves forward. The next run's stamping commit *is* mechanical, the ignore list
catches it, and the topic moves back. Two waves, two directions, same three cards.

**Fix.** A new `body_times()` helper takes the span minus its opening line. A card's opening tag
carries no content, so its blame date can never be honest evidence that anyone reviewed the card —
any real edit touches a body line too. Dropping it removes the cycle at no cost. The fallback
matters: some topics in `data/*.html` are written on a single line with header and body together, so
when the body yields nothing the helper falls back to the full span rather than silently leaving the
topic unstamped.

**Verified.** Restoring the three stamps to their committed values and re-running now leaves them
alone and moves only the seven new cards. `--only` on `sec`, `grc`, `devops`, `cloud` and `eng` —
the five domains corrected earlier this session — reports no change on any of them.

This also revises what the platform-engineering record said. That rule — *when `--only` moves an old
stamp, check whether a mechanical commit inflated it* — was right about the four cases it described,
and it was treating a symptom. The cause is fixed now; a stamp that moves after this commit deserves
the original suspicion again.

### Verification

`lint_content.py` 1,293 topics / 173 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py --check` clean · `stamp_freshness.py --verify` clean · `smoke_test.mjs` 31/31 ·
budget after build: raw 4.9 / 8.0 MB, gzip 1,335 / 2,200 KB, DOM 416 / 1,500, content elements
102,492 / 175,000.

---

## Session record — Track Z3: storage

Twentieth content wave, and the first to return to a Phase-4 track after finishing Phase 6.

### Choosing this one

With Phase 6 closed, a count of remaining open items put Track Z at the top with 26. Reading the
track showed most of that was already answered: an earlier session shipped the six-card spine —
virtualization fundamentals, the hypervisor comparison, snapshots-are-not-backups, 3-2-1-1-0,
ransomware-resilient backup and restore testing — and recorded exactly what it left. Wave Z3,
storage, was untouched in full.

**An audit note worth recording.** The first probe run reported `RPO`, `RTO`, `ML-KEM`,
`crypto-agility` and `live migration` as site-wide zeros. All five were false. The patterns were
written as `"RPO\|RTO"` and passed to `grep -E`, where `\|` is an escaped pipe — a literal `|`
character — so the search was for the string `RPO|RTO`, which appears nowhere. Under `-E` the
alternation is a bare `|`; the backslash form belongs to basic `grep`. Re-running correctly showed
`RTO` in nine domains and post-quantum already carded in `sec`. **A zero from a multi-term probe is
worth re-running as separate single-term greps before it becomes a wave.** Had that gone unchecked
this session would have written a post-quantum card that already exists.

### The audit, corrected

| Probe | Mentions before this wave |
|---|---|
| `erasure coding`, `thin provision`, `paravirtual` | 0 |
| `iSCSI` | acronym list only |
| `RAID` | `cs`, `linux`, `script` — nowhere in `infra` |
| `deduplicat` | `script` and `threat`, neither about storage |
| `hypervisor`, `live migration`, `vMotion`, `3-2-1` | present in `infra` — the spine already shipped |

### What shipped

**7 cards into `infra`**, 34 → 41. Site: 1,293 → **1,300 topics**.

Storage Fundamentals · RAID &amp; Erasure Coding · SAN &amp; Fabric · SMB &amp; NFS at Scale ·
Storage Performance · Thin Provisioning, Deduplication &amp; Tiering · Storage Capacity Planning.

### What these cards are actually about

The through-line: **storage failures are almost never surprises about the media.** They are
consequences of a design choice made months earlier — the wrong access model, an efficiency feature
outside its assumptions, a redundancy scheme whose rebuild window nobody costed, a growth rate
nobody was reporting.

Four specifics worth carrying:

- **Block, file and object differ by where the filesystem lives.** Everything else follows: only one
  server can own a block device because two filesystems writing the same blocks corrupt each other;
  file storage is shareable because the storage system arbitrates; object storage cannot modify part
  of a file because there is no block layer to modify.
- **The rebuild window is the real risk in RAID, not the parity mathematics.** A rebuild reads every
  remaining drive end to end, for hours or days, while degraded, on drives of the same age and
  batch. Single parity fell out of favour because disks got bigger and the window grew — not because
  anything about parity changed.
- **Thin provisioning has no gradual failure.** Behaviour is normal right up to a full pool, then
  writes fail across every volume in it at once. And the usual cause is not growth: it is deleted
  space never reclaimed, because a guest deleting a file tells the array nothing without UNMAP or
  TRIM. Pools fill while every volume inside reports free space.
- **Capacity is a time problem, not a percentage problem.** "82% full" prompts nothing; "eleven
  weeks left, and procurement takes eight" is a decision with a deadline. And in an all-flash estate
  the array often runs out of controller headroom long before terabytes, which no capacity report
  will mention.

The SMB/NFS card carries the one that resolves most user complaints: file protocols are chatty, so
opening a file is a sequence of round trips. "The share is slow from the branch office" is a latency
problem, adding bandwidth reliably fails to fix it, and a million small files behaves nothing like
one large file of the same size.

### Track Z after this wave

Waves Z1, Z2, Z4 and Z5 remain partly open, and the earlier session's note still describes them
accurately: sizing and overcommit depth, VM lifecycle and templates, live-migration operations,
P2V/V2V, backup products, failover and failback drills, tabletops. All genuine, all narrower than
what shipped, and reasonable to leave until an estate needs them.

### Verification

`lint_content.py` 1,300 topics / 178 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py` clean · `stamp_freshness.py --only infra` touched only the 7 new cards —
the oscillation fix from the previous wave holding across a second domain · `--verify` clean ·
`smoke_test.mjs` 31/31 · budget after build: raw 5.0 / 8.0 MB, gzip 1,346 / 2,200 KB, DOM 416 /
1,500, content elements 103,217 / 175,000.

---

## Session record — Track AC: the remaining automation items

Twenty-first content wave, and it closes Track AC.

### The audit

An earlier session shipped three genuine-gap cards here (Graph from PowerShell, JEA, automation
risk) and recorded four items as remaining. Probing those four plus the rest of the track:

| Probe | Mentions before this wave |
|---|---|
| `PowerShell DSC`, `Power Automate`, "logic app" | 0 |
| "credential in script", "runbook automation" | 0 |
| `Ansible` | 6 domains — but as a named tool, not as configuration-as-code practice |
| `idempoten`, "dry run", `WhatIf`, "error handling", `webhook`, `REST API` | present in `script` |

The last row confirms the earlier session's judgement: `script` genuinely carries the automation
craft, and the four recorded remainders were the real gaps. One addition — *Secrets in Automation*
(AC3.4) was on the track and not on the remaining list, and `credential in script` was a site-wide
zero, so it went in too.

### What shipped

**5 cards into `script`**, 140 → 145. Site: 1,300 → **1,305 topics**.

Configuration as Code On-Prem · Golden Images as Code · Secrets in Automation · Testing Automation ·
Power Automate &amp; Logic Apps.

### What these cards are actually about

The through-line: **operations code has more authority over an estate than most application code,
and is held to a far lower standard.** The script that disables accounts across a directory acts as
an administrator, on everything, unattended, with nobody watching the result — and gets none of the
review, testing or staging that a web application gets. That is historical rather than reasoned:
scripts started as one-off conveniences and quietly became infrastructure.

Four specifics worth carrying:

- **The best secret is the one that does not exist.** Before choosing where to store a credential,
  check whether the work can run somewhere with a platform identity — a managed identity, a
  federated pipeline, a group-managed service account. Most credential-handling problems dissolve
  rather than get solved.
- **A secret that ever reached a repository is compromised.** Removing it in a later commit changes
  nothing; the old revision still has it. Rotation is the only step that ends the exposure, and
  history rewriting on a shared branch is disruptive and usually incomplete.
- **Idempotency is a property you write, not one the tool gives you.** The moment a playbook shells
  out to a raw command the guarantee is gone and the tool cannot tell. The working standard: a
  second run reports zero changes, and an unexpected "changed" is a defect.
- **Low-code wins the build and code wins the maintenance.** The connector library is the real
  product, and the criteria that matter are about the second year — how long the thing will live and
  how bad its failure would be, not how quickly it can exist.

The testing card's practical core is a rewrite that costs ten minutes: separate the decision from
the action, so the rule that selects which accounts get disabled can be tested against every awkward
case without a directory and without disabling anybody. And the useful lab is not a copy of
production — it is ten deliberately strange objects (a nested group, a name with an apostrophe, a
machine offline for a year), because those shapes are what break bulk scripts.

### A large stamp correction, verified

`stamp_freshness.py --only script` moved 73 topics from `2026-06` to `2026-07` — much larger churn
than any previous wave, and worth checking rather than assuming. Every one of the 73 was validated
programmatically against `git log -S`: for each changed topic, the newest commit touching its
content was compared against the new stamp, and **none** claimed a date fresher than its history
supports. `script.html` had simply not been re-stamped since the July wave that edited those cards.
This is backlog, not drift — and the oscillation fix means it should not recur.

### Track AC after this wave

Complete. Waves AC1, AC2, AC4 and AC5 remain formally unticked in the list above, and the earlier
session's note explains why: their items are carded in `script` already, under different names.

### Verification

`lint_content.py` 1,305 topics / 182 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py` clean · `stamp_freshness.py --verify` clean · `smoke_test.mjs` 31/31 ·
budget after build: raw 5.0 / 8.0 MB, gzip 1,354 / 2,200 KB, DOM 416 / 1,500, content elements
103,660 / 175,000.

---

## Session record — Track AU: enablement, training and technical influence

Twenty-second content wave, and the first track in this session that had **zero** items ticked
before it started.

### The audit

| Probe | Mentions before this wave |
|---|---|
| "training session", `workshop`, "lunch and learn", "brown bag" | 0 |
| "conference talk", "knowledge transfer" | 0 |
| "documentation…audience" | 0 |
| "technical writing", `mentoring` | present in `career` |

`career` carries *Clear Technical Communication*, *Technical Writing*, *Mentorship* and *Building in
Public* — the individual-skill layer, and a good one. What none of them covers is teaching as a
**function**: designing a curriculum, running a room, facilitating a session where you have no
stake in the answer, or getting a proposal through people who do not report to you. That is the
track's own framing — *teaching as a function, not as a personality trait* — and it was accurate.

### What shipped

**8 cards into `career`**, 21 → 29. Site: 1,305 → **1,313 topics**.

How Adults Actually Learn · Curriculum Design &amp; Assessment · Running a Workshop · Live Demos
&amp; Screencasts · Facilitating Retrospectives &amp; Tabletops · Documentation Types &amp;
Docs-as-Code · Diagrams That Explain · Proposals, Executives &amp; Speaking.

### What these cards are actually about

The through-line: **the expert is systematically the worst judge of whether their explanation
worked.** Their knowledge is chunked, so they cannot feel the weight of what they are asking a
learner to hold; their diagram is comprehensive because they can already read it; their proposal
builds to a conclusion because that is the order in which they earned it. Every card here is, in
some form, a countermeasure to that blind spot.

Four specifics worth carrying:

- **Explaining is not teaching.** An hour of excellent explanation produces people who understood it
  in the room and cannot do it on Thursday. Understanding while somebody else drives is a different
  capability from doing it, and only the second is what anyone wanted.
- **Design backwards from the behaviour.** Name what people must do unaided, decide what would prove
  it, then choose content — and delete everything left over. The nice-to-know is what pushes a
  session long, rushes the practice, and turns the exercise into a demo.
- **A tutorial cannot have branches.** If it says "depending on your environment", it is a how-to
  guide and a beginner will fail at that sentence. Most frustrating documentation is two documents
  wearing one title.
- **Put the recommendation first, and include do-nothing honestly.** A proposal presenting one
  course of action reads as advocacy; one that says what happens if you decline reads as advice, and
  gets a decision rather than a request for more information.

Two smaller ones worth keeping: the silent written round at the start of a retrospective costs three
minutes and reliably surfaces what the most junior person was not going to say; and the diagram you
draw *while* explaining a system to someone is almost always at the right level of abstraction,
because it contains exactly what was needed and nothing else.

### Track AU after this wave

One item genuinely open — *Teaching a Tool You Just Learned* — and three marked `[~]` against
existing cards in `career` and `ops`.

### Verification

`lint_content.py` 1,313 topics / 183 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py` clean · `stamp_freshness.py --only career` moved one topic 2026-06 → 2026-07,
looking through an August mechanical commit as designed · `--verify` clean · `smoke_test.mjs` 31/31 ·
budget after build: raw 5.0 / 8.0 MB, gzip 1,367 / 2,200 KB, DOM 416 / 1,500, content elements
104,484 / 175,000.

---

## Session record — Track AV: consulting, contracting and independent practice

Twenty-third content wave, and the second zero-ticked track closed in a row.

### The audit

| Probe | Mentions before this wave |
|---|---|
| `consulting`, `freelance`, "rate card", "day rate" | 0 |
| "client discovery", `IR35` | 0 |
| "statement of work" | 2 — `acronym` and `pentest`, in a penetration-testing sense |
| `contracting` | `grc` and `military`, neither about independent practice |

`career` carries the employed-career layer well — negotiating an offer, financial basics, breaking
in, growing into senior. Nothing addressed the other path at all.

### What shipped

**8 cards into `career`**, 29 → 37. Site: 1,313 → **1,321 topics**.

Consultant, Contractor or Staff Augmentation · Pricing · Finding Clients · The Proposal &amp;
Statement of Work · Discovery &amp; Managing Scope · Someone Else's Politics &amp; Handover · The
Assessment Report · The Business Side.

### What these cards are actually about

The through-line: **almost every failure in independent practice is a pricing or scoping decision
made before the work started, discovered months later.** The engagement that will not end, the
fixed-price job that ate three unpaid weeks, the client whose late payment becomes your crisis, the
report nobody acted on — each traces back to something that was cheap to define up front and
expensive to renegotiate afterwards.

Four specifics worth carrying:

- **Work the rate backwards from billable days.** A realistic year is 130–150 billable days once
  holiday, sales, admin and gaps between engagements are counted — not 220. The day rate that
  matches a salary is therefore considerably higher than the naive division, and getting this wrong
  at the start is what makes the first year feel like a mistake.
- **Hourly pricing penalises expertise.** The person who solves it in two hours earns less than the
  one who takes eight, and the client experiences the fast answer as poor value. That misalignment
  is the argument for every other pricing model.
- **Deemed acceptance is the least glamorous clause and does the most work.** Without it an
  engagement can be held open indefinitely by a client who is merely busy — no dispute, no bad
  faith, just a review that never happens and an invoice that cannot be raised.
- **Dependency is commercially attractive and professionally corrosive.** The client who cannot
  operate what you built keeps paying, and every later engagement is a rescue rather than a choice.
  Referrals from work that visibly holds are worth more than a retainer built on helplessness.

Two smaller ones: referring out work you cannot take is the highest-return, least obvious business
development there is; and the honest unfinished-work list at handover — three things remaining, what
you would do, roughly what they cost — is in practice the most common origin of the next engagement.

### A note on scope

The contracts and protections card is deliberately written as orientation rather than as advice, and
says so in the card: entity structure, employment-status rules, insurance requirements and
enforceability of restrictive covenants all vary substantially by jurisdiction. The card names what
to look at and why it matters, and points at getting professional help for anything significant.
That framing is the right one for this site's audience and should be kept if the card is revised.

### Track AV after this wave

Two areas open: subcontracting and partnering (AV3.4), and the whole of AV4 — running a security
assessment engagement end to end, fractional and advisory roles, expert witness work, and
productising a service. AV4 is the most specialised material in the track and reasonable to leave
until asked for.

### Verification

`lint_content.py` 1,321 topics / 185 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py` clean · `stamp_freshness.py --only career` touched only the 8 new cards ·
`--verify` clean · `smoke_test.mjs` 31/31 · budget after build: raw 5.1 / 8.0 MB, gzip 1,381 /
2,200 KB, DOM 416 / 1,500, content elements 105,348 / 175,000.

---

## Session record — Track AE3/AE4: scale extremes, sustainability, accessibility and ethics

Twenty-fourth content wave.

### Choosing this one, and two tracks ruled out

Three tracks were audited before picking. **AQ (Emerging Platforms)** turned out largely covered:
`net` carries *Modern Connectivity — 5G, Private Cellular, Satellite &amp; IoT* and *Edge Computing*,
which between them answer most of the track. **AD (Apple/Android)** likewise: `endpoint` carries
*macOS for Windows Admins*, *Apple Fleet Management* and *iOS &amp; Android Enterprise*, and the
genuine zeros left — declarative device management, Kandji, Knox — are narrow vendor specifics.
Recording both here so a later session does not re-audit them.

Track AE's earlier session shipped AE1 (OT/ICS) and correctly judged AE2 as overlapping `grc`. AE3
and AE4 were untouched, and the probes agreed:

| Probe | Mentions before this wave |
|---|---|
| "multi-tenant tooling", `divestiture` | 0 |
| "green IT", `PUE`, "e-waste" | 0 |
| "small business IT", "seasonal load" | 0 |
| `MSP` | `acronym`, `endpoint`, `grc` — named, never as an operating model |
| `accessib`, `WCAG`, "screen reader" | present — all web-facing, in `web`, `script` and `grc` |

That last row is the interesting one. Accessibility is on the site as a *web standard*. Nothing
covered it as an *IT operations* concern — the internal tools IT procures, the assistive software
application control silently blocks, the MFA method that excludes someone.

### What shipped

**8 cards into `ops`**, 68 → 76. Site: 1,321 → **1,329 topics**.

IT for Very Small Organisations · IT for the Very Large · MSP Operations · Remote &amp; Distributed
Workforces · Mergers, Acquisitions &amp; Divestitures · Green IT · Accessible IT · Surveillance vs
Monitoring.

All eight went to `ops` under an **Operating Context** badge rather than splitting the ethics and
sustainability cards to `grc`. They are one idea — how the same IT job changes with the context it
is done in — and separating them would have made the reader hunt.

### What these cards are actually about

The through-line: **the generic answer is calibrated to a mid-sized, office-based, single-entity
organisation, and almost nobody works in one.** Every card is a case where the standard advice is
not merely insufficient but actively wrong.

Four specifics worth carrying:

- **Manufacturing usually outweighs running, for end-user devices.** Emissions from building a
  laptop exceed several years of using it, which inverts the intuitive advice: extending the refresh
  cycle by a year does more than any power setting. Endpoint power settings are worth doing and not
  worth leading with; reducing email storage measures nothing.
- **At large scale, every technical problem is an agreement problem.** The engineering to standardise
  endpoint management takes weeks; the agreement takes quarters. Skipping it produces a standard
  that exists on paper while everyone continues as before.
- **An MSP's remote-management platform is tier zero and is usually protected like an ordinary SaaS
  tool.** It exists to push software to every endpoint at every client, so an attacker who reaches
  it has that capability too — which is exactly how mass incidents have happened.
- **The monitoring/surveillance line is drawn by purpose, not by data or tooling.** It is crossed by
  drift: a capability exists, a senior person asks a reasonable-sounding question, somebody answers
  because they can, and a precedent is set nobody decided. The control that matters is protecting
  the junior person who has to say no — written authorisation rules, so refusal is procedure rather
  than personal courage.

The small-organisation card carries the one most likely to be acted on tomorrow: domains,
certificates and cloud tenancies registered to an individual's personal account are an ordinary
convenience at founding and an existential problem the day that person leaves badly or cannot be
reached.

### Track AE after this wave

One area open: the AE2 operational specifics for healthcare, finance, government and education —
the regulatory half is carded in `grc`, the day-to-day texture is not.

### Verification

`lint_content.py` 1,329 topics / 190 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py` clean · `stamp_freshness.py --only ops` touched only the 8 new cards ·
`--verify` clean · `smoke_test.mjs` 31/31 · budget after build: raw 5.1 / 8.0 MB, gzip 1,395 /
2,200 KB, DOM 416 / 1,500, content elements 106,125 / 175,000.

---

## Session record — Track BD2: tokens

Twenty-fifth content wave, and a short one: three cards closing the gap this session's earlier BD
wave explicitly left open.

### The audit

| Probe | Mentions before this wave |
|---|---|
| "OAuth 2.1", "token revocation", "token lifetime" | 0 |
| `logout` | `linux` and `shortcut`, both about shell and keyboard shortcuts |
| `PKCE`, "refresh token", "client credentials" | present — named in the beginner API card and in `web` |

The earlier BD record predicted this shape and it held: the vocabulary appears, the operational
consequences do not. Nothing said which OAuth flows were removed and why, what happens to a token
when you disable an account, or why "sign out everywhere" frequently does not.

### What shipped

**3 cards into `sec`**, 78 → 81. Site: 1,329 → **1,332 topics**.

OAuth 2.1 &amp; PKCE · Token Lifetime &amp; Revocation · Secrets, Tokens &amp; Keys.

### What these cards are actually about

The through-line, and the reason these three belong together: **a self-contained token cannot be
withdrawn, only outlived.** The property that lets an API validate a token locally without asking
the issuer anything is the same property that makes disabling an account a control over the *next*
session rather than the current one. Every design decision here follows from that constraint.

Three specifics worth carrying:

- **The device authorization grant is a phishing mechanism nobody has to fake.** The attacker
  initiates the request, sends the victim the genuine code and the genuine URL, and receives the
  token when the victim signs in correctly with MFA on the real page. Restrict the flow by policy to
  the few scenarios that need it and alert on it everywhere else.
- **On refresh-token replay, revoke the whole family.** A rotated token presented twice means two
  parties hold it and you cannot tell which is the attacker. Occasionally logging out a legitimate
  user is enormously better than silently letting the attacker continue.
- **Bearer is the property that matters and is the least visible.** Access tokens, API keys, session
  cookies and refresh tokens are all bearer credentials: whoever holds it is you, with no further
  check. Sender-constrained alternatives remove that, at a complexity cost most systems have not yet
  accepted.

The taxonomy card ends on the certificate-expiry outage — the most predictable failure in IT, caused
by manual renewal and an inventory gap, and removable with automation plus alerting that fires early
enough to act during working hours.

### Track BD after this wave

Closed. BD1, BD3 and BD4 shipped in the earlier wave; BD2 is done here. Two items across the track
are `[~]` against cards written elsewhere this session.

### Verification

`lint_content.py` 1,332 topics / 193 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py` clean · `stamp_freshness.py --only sec` touched only the 3 new cards ·
`--verify` clean · `smoke_test.mjs` 31/31 · budget after build: raw 5.2 / 8.0 MB, gzip 1,400 /
2,200 KB, DOM 416 / 1,500, content elements 106,430 / 175,000.

---

## Session record — Track AN1/AN2: the `hw` domain, scaffolded and opened

Twenty-sixth content wave, and the first new domain of this session — the site's **30th**.

### Why this one, and why now

After the plan.md accuracy pass, the honest backlog was 86 items in tracks whose checklists still
mean what they say — and Track AN held 25 of them, by far the largest single genuine void. The
probes were unambiguous:

| Probe | Mentions before this wave |
|---|---|
| `thermal paste`, "POST beep", `resistor`, `multimeter`, `oscilloscope` | 0 |
| `Arduino`, `I2C`, `RTOS`, "soldering" (electronics sense) | 0 |
| `motherboard`, "power supply" | acronym list only |
| `Ohm` | one hit in `script`, unrelated |

Nothing on the site covered PC hardware, electronics or embedded systems at all. `linux` was
expected to hold A+ hardware material and does not — its topic list is entirely software.

### The domain decision, revisited

The earlier AN6 record argued that hardware *security* belonged in `sec` rather than behind a domain
that might never be scaffolded, and shipped it there. That was right, and it left the question of
whether `hw` should exist at all. It should: electronics fundamentals, PC hardware, diagnosis and
repair, peripherals and embedded are a coherent body of work with a distinct audience, and they do
not fit in any existing domain. AN6 staying in `sec` is not a loss — the security reader finds it
where they are, and `hw` starts at electronics, which is where an electronics domain should start.

### Scaffolding

Four files, no tooling — there is no `scaffold_domain.py` in `tools/`, contrary to what a session
summary claimed, so this was done by hand and is recorded here for the next new domain:

| File | Change |
|---|---|
| `data/domains.json` | Entry inserted after `infra`; id `hw`, icon 🔧, A+ and Hands-On cert tags |
| `index-shell.html` | Chip added to the Core IT group, after `m365` |
| `style.css` | Accent `#a3e635` — checked against the 19 hex values already in use, all distinct |
| `data/hw.html` | The content itself |

One behaviour worth knowing: `stamp_freshness.py --only hw` reports "0 topics stamped" for a
brand-new file, because git has never seen it and blame returns nothing. That is the documented
path, not a failure — the hand-written stamps stand and `--verify` passes. The next run, once
committed, will confirm them.

### What shipped

**8 cards, a new `hw` domain.** Site: 1,332 → **1,340 topics**, 29 → **30 domains**.

| Wave | Cards |
|---|---|
| AN1 — Electronics | Voltage, Current &amp; Resistance · Power &amp; Thermals · Components &amp; Schematics · Test Gear |
| AN2 — PC Hardware | Motherboard Anatomy · CPU &amp; Cooling · Memory Deep · Storage Interfaces |

### What these cards are actually about

The through-line: **hardware knowledge earns its place in an IT career as diagnosis, not as
repair.** Component-level repair is rarely economic and usually voids a warranty. What this
material buys is the ability to tell an electrical problem from a logical one, to know when a
vendor's explanation is implausible, and to recognise the physical cause behind a ticket that has
been chased through software for a fortnight.

Four specifics worth carrying:

- **TDP is a cooling design target, not a consumption figure.** A 65 W processor can draw well over
  200 W in boost by design, so a cooler sized to the rated number produces a machine that is fast for
  thirty seconds. And throttling at 95 °C is a cooling problem while throttling at 70 °C is a
  power-limit setting — different diagnoses entirely.
- **UPS volt-amps are not watts.** VA equals watts only for a purely resistive load, and a computer
  power supply is not one. Multiply by the stated power factor before comparing to your load.
- **Which memory slots you use silently halves bandwidth.** The channel pairs are usually not
  adjacent, so filling the two slots nearest the processor is the common error — and the machine
  boots and works perfectly, which is why it presents as a performance mystery rather than a fault.
- **An M.2 slot is a form factor, not a protocol.** An M.2 SATA drive in an M.2 slot delivers SATA
  speeds and looks, to whoever bought "an M.2 SSD", like a defective product.

The cards are also where the site's cheapest sustainability advice now lives, and it is literal:
compressed air and ten minutes routinely restore a throttling laptop that was being considered for
replacement.

### Track AN after this wave

AN1 has one item open — analogue versus digital signals, sampling, noise and grounding, where the
noise and grounding half has the real IT application. AN3 (diagnosis and repair), AN4 (peripherals
and the office estate) and AN5 (embedded and single-board) are untouched and are the natural next
waves in this domain. AN6 shipped into `sec` earlier this session.

### Verification

`lint_content.py` 30 domain files, 1,340 topics / 194 cross-references clean ·
`fix_topic_names.py --check` clean · `annotate_acronyms.py` clean · `stamp_freshness.py --verify`
clean · `smoke_test.mjs` 31/31 · topic index confirms 8 `hw` topics and one deferred block ·
budget after build: raw 5.2 / 8.0 MB, gzip 1,414 / 2,200 KB, DOM 428 / 1,500 (the new chip),
content elements 107,250 / 175,000.

---

## Session record — Track AN3: diagnosis and repair

Twenty-seventh content wave, filling out the `hw` domain opened in the previous one.

### What shipped

**5 cards into `hw`**, 8 → 13. Site: 1,340 → **1,345 topics**.

Systematic Hardware Troubleshooting · POST, Beep Codes &amp; Diagnostic LEDs · Intermittent Faults ·
Soldering &amp; Rework · Data Recovery Triage.

### What these cards are actually about

The through-line: **hardware faults reward discipline over knowledge, because the search space is
small and finite.** A desktop has perhaps eight replaceable parts. What wastes the afternoon is
changing three of them at once and losing track of what was tried — which is why the method reads as
bureaucratic and beats intuition almost every time.

Four specifics worth carrying:

- **Swap with known-good, never with another suspect.** Moving a suspect part into a second suspect
  machine produces a result nobody can interpret. Known-good means a part you have just watched
  working, in a machine you have just watched working.
- **A machine with no display is still reporting.** POST runs before anything is visible, so failure
  before display initialisation leaves beeps, diagnostic LEDs and a POST code as the only channels.
  The BOOT LED is the dividing line: past it, hardware initialisation succeeded and the problem has
  become a storage or bootloader one.
- **"Intermittent" means conditional, and the condition is findable.** Fails after twenty minutes is
  thermal; fails when cold is a marginal joint, which is real and counter-intuitive; fails at the
  same time daily is environmental. When a machine has been fully rebuilt and still fails, move the
  whole machine to a different room — that single test separates the box from the environment.
- **The first data-recovery decision is whether to power it on again.** Clicking, grinding or
  repeated spin-up means stop: every further attempt converts a recoverable case into a more
  expensive or impossible one. Where the drive still reads, image it first and work only on copies.

Two safety points are stated in the soldering card without hedging, and should stay that way: power
supplies and CRT-era displays hold a dangerous charge after unplugging, and lithium cells are a fire
risk that must never be soldered directly.

### Track AN after this wave

AN1 has one item open (signals — analogue vs digital, sampling, noise, grounding). AN4 (peripherals
and the office estate) and AN5 (embedded and single-board) are untouched and are the natural next
waves. AN2 and AN3 are complete; AN6 shipped into `sec`.

### Verification

`lint_content.py` 30 domain files, 1,345 topics / 195 cross-references clean ·
`fix_topic_names.py --check` clean · `annotate_acronyms.py` clean · `stamp_freshness.py --only hw`
now works normally against the committed file and touched only the 5 new cards · `--verify` clean ·
`smoke_test.mjs` 31/31 · budget after build: raw 5.2 / 8.0 MB, gzip 1,423 / 2,200 KB, DOM 428 /
1,500, content elements 107,790 / 175,000.

---

## Session record — Track AN4: peripherals and the office estate

Twenty-eighth content wave. `hw` 13 → 18. Site: 1,345 → **1,350 topics**.

Displays · Printers &amp; MFPs · Docks, USB-C &amp; Thunderbolt · Input Devices &amp; Accessibility
Hardware · Conference Room Technology.

### What these cards are actually about

The through-line: **this is the hardware users actually touch, and it generates support load out of
all proportion to its complexity.** Nobody escalates about a CPU. They escalate about the second
monitor, the dock, the printer and the meeting room — and in each case the fault is usually a
configuration or a cable rather than a component.

Four specifics worth carrying:

- **USB-C is a connector shape, and that is the entire problem.** Two identical-looking cables can
  differ by a factor of eighty in bandwidth; a port may deliver 7.5 W or 240 W. Most "the dock is
  broken" tickets are a charge-only cable from a phone box. Buy certified, label them, standardise.
- **Read a dock's power *to the host*, not its own supply rating.** A 180 W dock may deliver 65 W
  upstream, and a workstation laptop under load will slowly flatten while plugged in.
- **"We cannot hear you" is a dropdown.** The conferencing application is on the laptop's own
  microphone and speakers rather than the room system. Teaching people where that setting lives
  resolves more room incidents than any equipment change.
- **Security baselines that disable accessibility features are a common own-goal.** The features
  have been abused for privilege escalation at a login screen — a real technique — and blunt
  mitigation removes the on-screen keyboard from someone who depends on it. Fix the specific abuse,
  not the feature.

Two estate-level points worth keeping: standardise on one monitor model and one scaling setting
where you can, because a fleet with three pixel densities produces a permanent trickle of tickets no
individual fix resolves; and in a meeting-room emergency, get the meeting running on any channel
first and fix the room afterwards — the meeting is what matters, the room is not.

### Track AN after this wave

AN5 (embedded and single-board) is the last unwritten wave, plus the one open AN1 item on signals.

### Verification

`lint_content.py` 1,350 topics / 198 cross-references clean · `fix_topic_names.py --check` clean ·
`annotate_acronyms.py` clean · `stamp_freshness.py --only hw` touched only the 5 new cards ·
`--verify` clean · `smoke_test.mjs` 31/31 · budget after build: raw 5.3 / 8.0 MB, gzip 1,431 /
2,200 KB, DOM 428 / 1,500, content elements 108,342 / 175,000.

---

## Session record — Track AN5: embedded and single-board, closing Track AN

Twenty-ninth content wave. `hw` 18 → 23. Site: 1,350 → **1,355 topics**.

Microcontrollers vs Single-Board Computers · GPIO, I²C, SPI &amp; UART · Firmware Basics ·
Real-Time Constraints · Home Lab Hardware.

### What these cards are actually about

The through-line: **the choice between a microcontroller and a small Linux computer is decided by
constraints that are invisible in a feature comparison** — power budget, timing guarantees, and what
happens when the power is pulled. Choosing wrongly is the standard first-project mistake, in both
directions, and it is settled by four questions rather than by capability.

Four specifics worth carrying:

- **Real-time means predictable, not fast.** A guaranteed two milliseconds every time is real-time;
  usually fifty microseconds with an occasional thirty milliseconds is not. General-purpose
  operating systems optimise the average, and real-time systems are specified by the worst case.
- **Voltage-level mismatch is how beginners destroy boards, and it is silent.** The jumper wires are
  identical; 5 V into a 3.3 V input damages it permanently. Checking two datasheets takes thirty
  seconds. Missing a common ground is the other one, and its symptom is nothing working at all.
- **A device with accessible debug pins is very hard to permanently brick.** SWD and JTAG talk to
  the silicon rather than to software, so they recover devices with no working firmware. Read-out
  protection fuses are frequently one-way and turn a development board into an ornament.
- **Second-hand small-form-factor office machines are the strongest value in home labs.** Quiet,
  cheap, low-power, generous with memory, and three cluster nicely — almost always a better choice
  than a decommissioned rack server, which is loud, hot and expensive to run.

The SBC card carries the point that matters to an IT estate rather than a hobbyist: single-board
computers are already in most organisations as signage, monitoring and "temporary" bridges, usually
unowned and unpatched on the corporate network. The productive response is a sanctioned path — a
segment, a base image, an asset-register entry with an owner — because prohibition drives it
underground.

### Track AN after this wave

Complete except one AN1 item: signals — analogue versus digital, sampling, noise and grounding.
`hw` is 23 topics across five waves, with AN6 in `sec`.

### Verification

`lint_content.py` 30 domain files, 1,355 topics / 201 cross-references clean ·
`fix_topic_names.py --check` clean · `annotate_acronyms.py` clean · `stamp_freshness.py --only hw`
touched only the 5 new cards · `--verify` clean · `smoke_test.mjs` 31/31 · budget after build:
raw 5.3 / 8.0 MB, gzip 1,439 / 2,200 KB, DOM 428 / 1,500, content elements 108,893 / 175,000.

---

## Session record — Track AH: search operators, and one item that was already built

Thirtieth wave, and the first engineering rather than content one this session. With the content
backlog in live tracks down to twelve items and the site at 1,355 topics across 30 domains,
findability is now worth more than another card.

### One item was already done

**Acronym-aware search** was specced as "the data already exists; the search does not use it". It
does — `acroSearchMap()` and `searchTerms()` have been expanding queries through the acronym
dictionary, and the count line reports which alternate matched. Verified headlessly in both
directions before ticking: `UEM` and `Unified Endpoint Management` each return 7 matches in 4
domains; `MFA` and `Multi-Factor Authentication` each return 54 in 14.

That is the third time this session a specced item turned out to be built. The checklist convention
note added earlier covers the shipped-note case; this is the other one — an item whose implementation
landed without anyone going back to the plan. **Check before writing, including for engineering
items.**

### What shipped

**Search operators.** Two, chosen because they are what a reader of a 1,300-topic site actually
needs:

- `domain:net firewall` — restricts the search to one domain. Multiple are additive. Uses domain
  ids, which the chips and permalinks already expose, so the vocabulary is one the reader has seen.
- `"exact phrase"` — matched literally. Several phrases are all required, and they combine with free
  text rather than merging into one substring, so `"default deny" DNS` asks for both.

`badge:beginner` from the spec was deliberately **not** built. Badges are inconsistent across
domains — "SEC • Essential", "Beginner", "OPS • Modern" and "LIFESTYLE • Career" all coexist — so
the operator would need a vocabulary a reader cannot guess and would mostly return nothing. Making
badges consistent is a content job; if it is ever done, the operator becomes worth having.

### A bug found in the first version

The initial implementation dropped free text shorter than two characters, so `domain:hw x` returned
all 23 topics in `hw` — answering "everything in that domain" to a reader who asked for "x", and
presenting it as a result rather than a rejected query. Fixed: free text below the threshold now
makes the whole query unusable, matching what a bare one-character query already did. It is the same
class of failure as a silently-ignored operator, which is why both now have a smoke check.

### Verification

Five new checks in `smoke_test.mjs`, 31 → **36**, covering exactly the failures that would be quiet:
`domain:` actually narrowing (93 unscoped → 17 in one domain), an unknown domain yielding nothing
rather than everything, a phrase matching, phrase-plus-text combining rather than merging, and short
free text rejecting the query. The operators are documented in the search box's tooltip, since an
undiscoverable feature is not one.

`lint_content.py` 1,355 topics clean · `stamp_freshness.py --verify` clean · `smoke_test.mjs` 36/36 ·
no console errors, no off-site requests · budget unchanged at raw 5.3 / 8.0 MB, gzip 1,440 / 2,200 KB.

### Track AH after this wave

Five items open: expansion-density toggle, related topics, domain landing cards, recently viewed,
and deep-linking to a concept card. The last is small and useful; related topics needs a curated
data file and is the largest.

---

## Session record — Track AH: card-level deep links

Thirty-first wave, and the last piece of work before this session's branch was left for review.

### What shipped

`#topic-id/3` now resolves to the third concept card in that topic: the domain hydrates, the topic
opens, the card is scrolled to centre and outlined for a couple of seconds. Clicking any concept
card's label copies that link.

Three decisions worth recording:

- **Cards are addressed by position, not by a title slug.** A slug would be prettier and would need
  every `.concept-title` stamped at build time and kept stable. Concept titles are edited far more
  freely than topic names — which have an alias map precisely because they are not. An index
  survives rewording and breaks on reordering; rewording is what actually happens.
- **The affordance costs no elements.** A domain can hold several hundred concept cards, so a link
  button per card is a real slice of the DOM budget for something used rarely. The label itself is
  the control, delegated from the domain container, with the hint in a hover state.
- **Out-of-range falls back to the topic.** Links outlive the cards they were written against, and
  landing on the topic is better than doing nothing.

The clipboard fallback also now confirms. Over `file://` there is no clipboard permission, so the
handler puts the link in the address bar instead — and previously said nothing, which reads as a
broken control. It now shows the same "copied" state either way.

### Verification

Two new smoke checks, 36 → **39** (one is a guard that the test found a topic with enough cards to
be worth testing — the first version silently passed against a single-card topic and exercised
nothing). Verified: a card link marks the right card (7-card topic, index 1 for `/2`), an
out-of-range index opens the topic and marks nothing, and a plain topic link is unaffected.

`lint_content.py` 1,355 topics clean · `stamp_freshness.py --verify` clean · `smoke_test.mjs` 39/39 ·
no console errors, no off-site requests · budget unchanged.

### Track AH after this wave

Four items open: expansion-density toggle, related topics, domain landing cards, recently viewed.

---

## Session record — Track AH: recently viewed, and a fourth already-built item

Thirty-second wave.

### The fourth already-built item

**Expansion density toggle** was specced and is implemented: `cycleAcroMode()` plus `.acro-hover`
and `.acro-off` rules, behind the header's acronym button. It ships three modes rather than the
four specced — *first use per domain* would need the annotator to mark first uses at build time,
and hover mode already solves the density-in-tables problem the item was written for. Verified
before ticking: cycles correctly, label and stored preference track, and the preference survives a
reload. It had **no smoke coverage**, so two checks were added — the failure is silent in both
directions, since a mode that stops applying leaves expansions on for someone who turned them off.

Four items this session turned out to be built already: acronym-aware search, the density toggle,
and two BD3 identity items carded under different names. That is a consistent enough rate to
restate the rule from the checklist convention note plainly: **verify before writing, including for
engineering items, and add the missing test rather than the feature.**

### What shipped

**Recently viewed.** The quick-jump palette opens on an empty query, and with 1,355 topics its
first sixty rows were whatever the index happened to hold — arbitrary, and never what the reader
wanted. It now leads with the last ten topics visited, badged `recent` so the ordering is explained
rather than mysterious, then falls back to the index. Typing a query drops them entirely.

Two design notes:

- **Stored as ids, resolved at render.** A topic later renamed or removed simply drops out when the
  study index cannot resolve it, which is the right failure — the alternative caches names that go
  stale silently.
- **Visits are recorded from both paths that open a topic**, clicking a header and following a link.
  Recording only one would have produced a list that was right about half the time, which is worse
  than one that is obviously empty.

### Verification

Five new checks, 39 → **44**. The recently-viewed ones cover exactly the quiet failures: visits that
stop being recorded leave an arbitrary list, and recent rows leaking into a filtered query would put
the wrong topics above the matches.

`lint_content.py` 1,355 topics clean · `stamp_freshness.py --verify` clean · `smoke_test.mjs` 44/44 ·
no console errors, no off-site requests · budget unchanged at raw 5.3 / 8.0 MB.

### Track AH after this wave

Two items open: **related topics** (needs a curated `related.json` and a suggestion script — the
largest remaining item in the track) and **domain landing cards** (30 short intros; content work
with a small rendering change).


## Session record — Track AH: domain landing cards

Thirty domains, 1,355 topics, and until now the only thing a reader saw on opening one was a wall of
collapsed headers. Every domain now opens on a short card: what it covers, who it is for, three
topics to start with as buttons, and which domains to read next.

### The one architectural decision

The intro is **data, rendered at hydration** — not a card written into `data/*.html`. Written into
the content files it would have been a `.topic`, and then it would have been counted by the topic
index, dated by `stamp_freshness.py`, linted by `lint_content.py`, offered by the random pick, and
dealt into study decks. Thirty signposts polluting five separate systems, each of which would have
needed an exception. As data it touches none of them: `build.py` gained one payload function of the
same shape as the three already there, `script.js` gained a renderer, and the entire content
pipeline is untouched. A smoke check asserts the separation directly — the DOM's `.topic` count for
an open domain must still equal its indexed count.

### The name-resolution trap, and what it cost to find

`start` stores topic **names**, resolved at render time against the domain's parsed block, so a
renamed topic drops its link rather than leaving a button that goes nowhere. Getting the names to
match took three passes, and each failure was worth recording:

1. **The extractor was wrong, not the data.** A first check reported 21 unresolved names. The regex
   `<span class="topic-name">(.*?)</span>` stops at the *first* `</span>` — which, in any title
   carrying an inline acronym expansion, is the expansion's closing tag. So "Cloud Rosetta Stone —
   AWS (Amazon Web Services) ↔ GCP ↔ Azure" was being read as "Cloud Rosetta Stone — AWS (Amazon Web
   Services)" and compared against itself, unequal. **Any regex that reads `.topic-name` has to
   balance nested spans**; the fix is a small scanner, kept in the scratchpad tooling.
2. **Then 23 genuine mismatches surfaced.** Titles written from memory: `Purple Teaming — Closing
   the Detection Gap` for a card actually called `Purple Team Mechanics — The Room, the Roles & the
   Cadence`, a `Stoicism` topic that does not exist in a seven-topic philosophy domain, three
   military titles invented wholesale. A close-match report against the real titles made each one a
   decision rather than a guess.
3. **The comparison had to be against `plainLabel`, not the raw title.** `domainTopics()` strips the
   acronym expansion spans, so the runtime sees "OSI Model — 7 Layers" while the JSON held "OSI
   (Open Systems Interconnection) Model — 7 Layers". All 90 names were rewritten to the stripped
   form by matching each against its own file, which is the only version of this that cannot drift.

The general lesson is the same one this project keeps relearning: **an audit that reports failures
is not evidence the data is wrong — check the instrument first.** A 21-item failure list that was
entirely the extractor's fault would have led to 21 unnecessary content edits.

### Verification

Nine new checks, 44 → **53**. They cover the card rendering above the topics, carrying its rows,
staying out of the topic count, its links opening the right topic, hiding during a search and
returning when cleared — and one that resolves the `start` names for **all thirty** domains rather
than the one the other checks exercise, because a rename in any of the other twenty-nine costs a
card a signpost just as quietly.

`smoke_test.mjs` 53/53 · no console errors, no off-site requests · budget raw 5.3 / 8.0 MB,
gzip 1,445 / 2,200 KB, DOM 428 / 1,500.

### Track AH after this wave

One item open: **related topics** — a "see also" strip per topic, needing a curated `related.json`
and a script that suggests candidates by shared acronyms and title terms. It is the largest
remaining item in the track, and the name-resolution work above applies to it directly: key it on
**topic ids**, not names, since ids are stamped by `build.py` and already have an alias file
covering renames.


## Session record — Track AH: related topics, closing the track

The last item in Track AH, and the one whose brief said "hand-curated" for a reason.

### The seed was already in the content

201 `<span class="xref">Exact Topic Title</span>` cross-references sit in the cards, and each one is
a writer saying *these two belong together*. `lint_content.py` already proves every one resolves to
a real title. Read both ways — the reader of the target wants the link as much as the reader of the
source — they gave **402 directed edges across 321 topics before a single judgement call**, and
they are curation rather than inference. Curation on top brought it to **554 links on 412 topics**:
all 23 hardware cards (the new domain had almost no xrefs), and `web` and `data`, which had 0/35
and 3/40 coverage and whose topics form obvious reading orders.

### The suggestion script is a shortlist, and its precision says why

`tools/suggest_related.py` ranks candidates by shared title terms weighted by rarity, plus shared
title acronyms, with a cross-domain bonus. Run over the hardware domain it proposed, in its top
five: Ohm's **Law** ↔ GDPR & CCPA (**law**), **Components** & Schematics ↔ React **Components**,
Memory Deep ↔ Organisational **Memory**, Storage Interfaces (PCIe **lanes**) ↔ IT Career Paths
(Finding Your **Lane**). Roughly a quarter of the top suggestions were worth keeping — and the
quarter that were, were excellent: Test Gear ↔ The Field Toolkit, Memory Deep ↔ Virtual Memory,
Power & Thermals ↔ Green IT.

That ratio is the argument for the whole design. A strip generated automatically would be right a
quarter of the time, which is exactly often enough to look deliberate and exactly wrong enough to
teach a reader to ignore it. **The script's job is to make curation cheap, not to do it**, and the
docstring says so, so the next session does not "improve" it into an auto-generator.

### Keyed on ids, not titles

The landing-card work in the previous wave resolved topics by **name** and paid for it three times
over. This file is keyed on **ids**: they are stamped by `build.py`, the alias file already covers
renames, and `suggest_related.py` imports build.py's own stamping so a suggestion can be pasted
straight in. The renderer still drops anything that fails to resolve — a deleted topic must not
leave dead strips on everything that pointed at it — and both `--check` and a smoke check assert
that nothing currently does.

### Rendering

The strip is built the first time a topic opens, not at hydration: a domain is dozens of topics and
a reader opens two or three, and resolving a target's title costs a parse of whichever *other*
domain it lives in. All three paths that open a topic — the header, a permalink, a search hit — go
through it. A link leaving the domain is tagged with the domain it goes to, because roughly half of
them do and following one blind is disorienting.

### Verification

Six new checks, 53 → **59**: the strip renders on open with every link resolved, sits below the last
concept card, tags a cross-domain link, follows to the right topic, renders once rather than once
per open, and — the one that matters over time — every id in the whole payload resolves.

`smoke_test.mjs` 59/59 · `suggest_related.py --check` clean, 0 one-way edges · budget raw 5.4 / 8.0
MB, gzip 1,456 / 2,200 KB, DOM 429 / 1,500.

### Track AH is now closed

Every item in the track is shipped. The obvious follow-on is new and recorded above rather than
folded in here: **the 201 xrefs are still inert**. They are lint-checked, styled, and now proven to
resolve to ids — clicking one should go there.

Coverage to build on, for whoever picks up related topics again: `script` 12/145, `linux` 5/58,
`acronym` 0/59, `shortcut` 0/37, `pentest` 3/29, `math` 0/16, `philosophy` 0/14.


## Session record — Track AH follow-on: the cross-references became links

201 `<span class="xref">Exact Topic Title</span>` spans had been sitting in the content since the
convention was introduced. The linter proved every title resolved; the reader still had to go and
find the card by hand. Seeding `related.json` from them in the previous wave proved they resolve to
**ids**, which is all a link needs.

**Two passes in `build.py`.** A cross-reference names a card in another domain far more often than
its own, so the ids for every domain are stamped before any body is rewritten. Resolving in the
browser was never an option for the same reason topic ids are not derived there: the target is
almost never in the DOM, because only one domain's content ever is.

**Matched the way the linter matches.** The acronym annotator injects expansions *inside* the xref
span, so the title is compared with expansions stripped while the span's inner HTML is left exactly
as written — the reader keeps the expansion, the matcher does not see it.

**Failure is a downgrade, not a dead link.** Only a span that resolved gets `data-xref`, and only
`.xref[data-xref]` is styled and handled as clickable. A title that stops matching goes back to
being plain italic text, which is what it was before this change.

### Verification

Five new checks, 59 → **64**: the spans are stamped, every stamped id resolves, a click lands on the
named topic with it open, the span is focusable and announced as a link, and Enter follows it.

The keyboard check needed hardening before it meant anything. Written the obvious way it reused the
span the click test had just followed, so the hash already held the expected id and a keydown
handler that did nothing at all would have passed. It now clears the hash first. That is the third
time in this project a check has passed for a reason unrelated to the feature — **write the
assertion, then ask what would still pass if the feature were deleted.**

`smoke_test.mjs` 64/64 · `lint_content.py` clean · budget raw 5.4 / 8.0 MB, gzip 1,460 / 2,200 KB,
DOM 429 / 1,500.


## Session record — Track AJ: two quality gates, and one item that measured itself away

Track AJ's checklist was written before most of it existed. Verified first, as the checklist
convention requires: **three of the eight items were already shipped and in CI** — the content
linter, the duplicate-slug guard and the performance budget. That is the fifth time this has
happened, and the count is now high enough to be the default expectation rather than a surprise.

### Markup validator

`lint_content.py` reads the content as text, which is right for "does this card use `ref-table`"
and useless for "is this markup well-formed". `tools/check_markup.py` runs a stack-based
`html.parser` over every fragment and over the built page: unclosed elements, closers with nothing
open, and closed void elements.

It matters more here than in an ordinary page. A domain's content is parsed once as *text*, shipped
inside an inert script block, and only becomes elements when `innerHTML` runs on it — so a stray tag
is invisible until a reader opens that one domain, and the browser's repair (hoisting the rest of
the card out of its parent) is silent. All 31 files are clean today; the point is keeping them that
way.

**The validator has a `--self-test`, and it is in CI next to the validator itself.** Six fixtures,
each broken one specific way, plus one well-formed fixture that must produce nothing. A checker that
reports "0 errors" is indistinguishable from a checker that has quietly stopped looking, and the
previous wave had already been bitten by a keyboard test that passed for an unrelated reason.

### Acronym drift report

`tools/acronym_drift.py` lists capitalised tokens the dictionary has never heard of. The first run
returned 3,050 tokens and was useless — the top of the list was `ID`, `TERMS`, `WHAT`, `IS`, `WHY`,
`LIFESTYLE`. Three exclusions fixed it, and the third is the interesting one:

- **Categorical labels are not prose.** `.topic-badge` and `.concept-label` are shouted by design.
- **A plural of a known entry is not drift.** APIs, VMs, URLs.
- **An ordinary word being shouted in a heading is not an acronym** — WHAT, WHY, FROM, KEY. There is
  no wordlist on the machine to consult, so **the content supplies one**: a token whose lowercase
  form appears twenty or more times in the site's own lowercase prose is a word. No data file, no
  maintenance, and it adapts as the writing does.

1,711 tokens remain, and narrowed to a single domain it is a direct work queue — `--domain hw`
returns SBC, UART, JTAG, SWD, TX, RX, XMP, VRM, every one a real gap left by the hardware wave.

**Neither number gates CI, deliberately.** The unknown-token list is full of product names;
`--unused` reports 173 dictionary entries no card uses, and the dictionary is *also* a standalone
reference domain and the quiz's question bank, so an entry existing for its own sake is the point.
A gate on either would fail every content wave for reasons nobody should act on. The docstring says
so, so the next session does not "fix" it into a gate.

### The item that measured itself away

**Link & anchor checker** — "every `#slug` referenced in prose resolves; every external link is
alive". Measured before building: the content holds **one** `href="#"` and **one** external link
across 1,355 topics. The item was written before the `<span class="xref">` convention existed, and
that convention is now checked by the linter and resolved to ids by the build. Marked `[~]` with the
measurement rather than built, and rather than left open to be rediscovered.

### Also in CI now

`suggest_related.py --check`, verified to fail on a planted bad id before being wired in — the same
rule as the self-test above.

`check_markup.py` 31 files clean · self-test 6 fixtures clean · `smoke_test.mjs` 64/64 ·
`lint_content.py` clean · budget raw 5.4 / 8.0 MB.

### Track AJ after this wave

Two items open: **accessibility CI** (axe against the built page; the smoke test already covers
`aria-expanded` on both accordion levels and theme contrast on four elements) and **visual
regression** (screenshot diffs, the least valuable item in the track on a page whose layout is this
stable).

The drift report also leaves a content queue behind it: the dictionary is missing the embedded and
hardware vocabulary the last content wave introduced.


## Session record — the drift report's first queue, worked

`acronym_drift.py` shipped in the previous wave with a work queue attached. This is that queue,
worked, which is also the tool's first real test.

**25 entries added**, 1,069 → 1,094: the embedded and hardware vocabulary the hardware wave
introduced and nothing was watching (UART, JTAG, SWD, SBC, GPIO, VRM, XMP, TX, RX), plus the gaps
the report surfaced elsewhere — IDOR, OPA, SLSA, IMA, OPSEC, JVM, ZAP, RC4, PHP, E2E, UTC, IEC, OMA,
OOBE, CySA, PUE. `hw`'s unknown-token count fell from 42 tokens / 83 occurrences to 32 / 43.

### The wave found a wrong expansion that had been shipping

`SPI` was in the dictionary with exactly one meaning — **Stateful Packet Inspection** — and the
annotator had been rendering that inside `GPIO, I²C, SPI & UART` and beside "SPI flash chip". Both
uses on the site are **Serial Peripheral Interface**; the firewall sense appears in no card at all.
The entry now carries both meanings with the bus as the annotated default, so the reference domain
keeps the firewall sense and the cards say what they mean.

This is worth stating plainly, because it is the argument for the tool existing: the error was in
content the linter passes, the smoke test passes, and a human had read. What surfaced it was
counting a domain's vocabulary against the dictionary — the one check nothing was doing. The
ambiguity warning `lint_content.py` already tracks (four, unchanged) could not see it either: a
single-meaning entry is not ambiguous, it is just wrong.

`SBC` was added the other way round — two meanings from the start, `Single-Board Computer` as the
default with `byDomain` overrides to `Session Border Controller` for `net` and `m365`. Verified in
the diff: `hw` got the board, `m365` got the controller.

### Verification

Every new expansion was read in the diff rather than trusted: 39 distinct injections across 16
files, all correct after the SPI fix. `annotate_acronyms.py --check` clean · `lint_content.py`
clean, ambiguity trend unchanged at 4 · `check_markup.py` 31 files clean ·
`stamp_freshness.py --verify` 1,296 stamps valid (the acronym domain's 59 topics are generated and
carry none by design) · `smoke_test.mjs` 64/64.


## Session record — Track AG: learning paths, and covering four features that had no tests

Two halves. The first was bookkeeping with teeth: **four of Track AG's eight items were already
built** — spaced repetition, the acronym quiz, the distractor fix and export/import — and **not one
of them had a single test**. Each fails silently, which is what makes the gap matter: a scheduler
that stops writing records looks like "nothing is due"; distractors drawn from the wrong pool look
like an easy quiz; an export that drops a key looks like a smaller export. Fourteen checks added,
64 → 77, and the features left alone.

One assertion had to be corrected rather than the code. The scheduler works in **whole days**, so
"again" schedules a lapsed card for tomorrow rather than later in the same session. An SRS purist
would re-queue it immediately; the check now asserts the behaviour as written, with a note to change
the check if the behaviour ever changes. Writing the test is how that got noticed at all.

### Learning paths

Six routes over 75 topics that already exist — Network Foundations, SOC Analyst Starter, Breaking
Into IT, Comfortable in the Terminal, First 90 Days on an Endpoint Team, Cloud From Zero. The whole
feature is 4.9 KB of ids: no new content, and the value is entirely in the order.

Three decisions worth keeping:

- **Done means reviewed.** A path reads the same `reviewed:` key the ✓ on a topic header sets rather
  than inventing a per-path state. Progress therefore already exists the moment a path is added, it
  survives export/import for free, and there is no second source of truth to reconcile.
- **"You are here" is the feature.** An ordered list without a current position is just a list. The
  first unreviewed step is marked and a **Continue** button opens it.
- **Authored by resolver, not by hand.** The paths were written as `(domain, title fragment)` pairs
  and resolved to ids by a script that refuses ambiguity — it caught six selectors matching two
  topics each (`SSH`, `Bash`, `Package Management`, `CIA`, `Infrastructure as Code`) and one naming
  a card that does not exist. Typing 75 slugs by hand would have produced silent misses instead;
  this is the same lesson as the landing cards, applied before it cost anything.

`tools/check_paths.py` gates every step id in CI, verified to fail on a planted bad step before
being wired in. It also reports reach: the six paths touch 75 distinct topics across 15 domains.

### Verification

`smoke_test.mjs` 83/83 — six new checks covering that a path renders every step it declares (a
broken path renders as a *shorter* path, which is the silent failure), that reviewed steps count as
done, that "you are here" lands on the first unreviewed step, and that Continue opens it.

### Track AG after this wave

Two items open: **exam mode** (timed, fixed count, no feedback until a scored per-domain report) and
**per-topic notes** (attach a note to a topic id and surface it inline). Both are self-contained;
exam mode is the larger one and would reuse the quiz generators as they stand.


## Session record — Track AG: per-topic notes

A 📝 alongside ★ ✓ 🔗. One note per topic, at the top of that topic's body, lit on the header when a
topic carries one.

**Built beside the notepad, not inside it.** The item said "extend the notepad to attach a note to a
topic ID". The notepad is a single shared scratchpad with authorship and sorting; threading a
topic id through it would have meant a mode inside a feature that does not want one. A separate
`note:<id>` key is smaller, and it lands in the right place — a note about Kerberos delegation
belongs on the Kerberos card, not in a pile with everything else.

**The shape was the design.** Using the same prefixed-key-holding-a-string form as `reviewed:` and
`bookmark:` meant the backup system adopted notes almost for free: `bkCategory` gained one line,
`bkOwnedKeys` and the export needed nothing. Writing the test is what caught the one place it was
*not* free — `bkSerialise`'s fallback treats every unrecognised key as a boolean flag, so notes
would have been silently refused on import. One branch fixed it. The count line now separates topic
notes from notepad notes as well, because conflating them would misreport what a restore actually
put back.

**Failure modes covered.** Eight checks, 83 → **91**: the editor opens, the note saves and shows and
flags its topic, it sits above the concept cards, it survives the domain being evicted and
reopened — the case that matters most here, since only one domain's content is ever in the DOM — it
travels in the export and comes back on import, a malformed note is refused, and deleting one
removes the block and the flag.

### Track AG after this wave

Two items open: **exam mode** and the **progress dashboard**. Exam mode would reuse the quiz
generators as they stand; the dashboard is the more useful of the two, since every number it needs
is already in `localStorage` and nothing currently shows a reader what they have covered.


## Session record — Track AG: the progress dashboard, and a streak that cannot lie

📊 Progress in the study menu. Reviewed of total for the site and per domain, plus starred, known,
noted, due today, and a day streak with its best run.

**Nothing is computed from the document.** This is the constraint the whole page is built around and
the one a dashboard is most likely to break: counting `.topic` elements would report on the single
domain that happens to be open and look entirely healthy doing it. Every count reads the inlined
topic index and `localStorage`, so all thirty domains are reported whether or not any of them has
ever been opened. The smoke check asserts exactly that — six reviewed topics across three domains,
counted correctly while **zero** topics are rendered.

**The streak is one record, not a list of days.** `{last, n, best}`. A streak that needs a growing
array of dates to answer "how many days in a row" is storing the wrong thing. Three behaviours
follow and each is checked: a busy day counts once, yesterday continues the run, and a lapsed run
reads as zero *without* being destroyed — `streakCurrent()` returns 0 while `best` survives, so a
missed day costs the run rather than the record.

**Untouched domains are muted, not hidden.** A report that shows only what has been read cannot show
what has not, and "what have I not touched" is the more useful question after the first week.

### Verification

Nine new checks, 91 → **100**: the dashboard's coverage and its independence from the DOM, the
streak's three transitions and its best-run memory, and both directions of its export — restored
intact, and a malformed record refused.


## Session record — Track AG closed: exam mode

The last item in the track.

**The mode is defined by what it withholds.** A quiz that marks each answer as you go is a study
tool; an exam that does not is a measurement. Everything else follows from that: answers are
recorded and the paper moves on, a chosen option is styled as *chosen* and never as right or wrong,
and nothing is scored until the paper is handed in. The checks assert the absence — after answering
deliberately wrongly, zero marking elements exist in the stage.

**Distractors come from the question's own domain.** The plain quiz draws from the selected scope,
which is right for a single domain and wrong for "all domains": three options about Kubernetes and
one about soldering is a question about noticing the odd one out. Exam mode uses the question's own
domain wherever that domain has four topics to offer, falling back to the scope otherwise. Checked
over a 20-question all-domains paper: zero questions drew an option from another domain.

**The report is a to-do list, not a scoreboard.** Domains are ordered weakest first, every missed
topic is a link back to it, unanswered questions are marked as unanswered rather than merged with
wrong ones, and "★ star all of these" turns the result into a study deck in one click.

**The bug the tests were written to catch.** The clock is an interval, and an interval outlives the
modal that owns it. Left running after the reader closes the exam, it would keep ticking against a
detached stage and eventually "submit" a paper nobody was sitting. `stClose()` now stops it, and a
check opens an exam, confirms the timer is running, closes the modal and confirms the state is gone.

### Verification

Ten new checks, 100 → **110**.

### Track AG is now closed

All eight items shipped. Four of them turned out to be built already and were given the tests they
never had; four were built this session — learning paths, per-topic notes, the progress dashboard
and exam mode. The study tools are now a system rather than four separate toys, which is what the
track's own preamble asked for: a path tells you what to read, the dashboard tells you what you have
covered, the scheduler brings it back, and the exam tells you whether any of it stuck.


## Session record — m365 content wave: nine cards

Six engineering waves in a row; this one is content. `m365` was audited rather than guessed at: 26
topics, well-built, with the voids clustered in exactly the places a domain grows *around* rather
than into — the object model beneath the workloads, the two migrations, and the identity surface.

### The audit

Twenty candidate subjects were probed against the whole site before anything was written. Zero
mentions: **Power Platform**, **M365 Groups** as an object, **SPMT**, **cutover/staged migration**,
**hybrid Exchange**. One or two mentions only: **Secure Score**, **multi-geo**, **data residency**,
**guest access**, **B2B**. Already carded and left alone: Copilot licensing and data boundaries
(a concept card inside an existing topic), Conditional Access (41 mentions across the site), DMARC
(33), access reviews (10).

**One audit false positive, again.** `grep -oi Viva` returned 22 — every one of them inside the word
*sur**viva**l*. The count and the file list disagreed, which is what caught it. Case-insensitive
substring counts need a word boundary, and the rule already recorded for multi-term greps applies
just as well to short single terms.

### What shipped

Nine cards, 26 → **35** topics:

- **Microsoft 365 Groups** — the object underneath Teams, SharePoint, Planner and the odd deletion
  behaviour. Written first deliberately: several existing cards make more sense once it exists.
- **Exchange Online Migration** and **SharePoint & OneDrive Migration** — the two projects that
  dominate a tenant's first two years and had no coverage at all.
- **Power Platform Governance** — a development platform ships in the licence whether or not anyone
  planned one.
- **External Collaboration** — guests are accounts in your directory that no HR process will ever
  retire.
- **App Registrations, Service Principals & Consent** — including the failure that arrives on a
  schedule: client secrets expire silently at 3am.
- **Secure Score & the Tenant Baseline** — sorted by what an intrusion actually runs into rather
  than by points, with break-glass accounts as step one.
- **Multi-Geo & Data Residency** — mostly an argument for establishing which question is being
  asked before building anything.
- **Joiner, Mover, Leaver in M365 Terms** — the process whose absence causes most of the cleanup the
  other cards describe.

### Verification

`check_markup.py` clean after every card, which caught nothing this time but would have caught the
one truncated heredoc that has bitten this project before. `lint_content.py` caught **three** bad
cross-references written from memory — `Automation Risk` was really `Automation Risk & Discipline`,
and two named cards that do not exist. All three repointed at real titles. The new xrefs were folded
into `related.json` (+26 links) and `stamp_freshness.py --only m365` stamped the new cards with **no
churn on the existing 26** — the `body_times()` fix from earlier still holds.

Site total 1,355 → **1,364** topics. Budget raw 5.4 / 8.0 MB, content elements 110,310 / 175,000.
`smoke_test.mjs` 110/110.


## Session record — pentest content wave: five cards, and one the audit killed

`pentest` had 29 topics with visible duplication (two privilege-escalation cards, two on password
attacks, "Methodology & Phases" beside "Penetration Testing Phases"). The gaps were not in the
tooling — `redteam` covers that in depth — but in the *kinds of engagement* the domain never
described.

### An API card was written, then deleted

The probe that justified it was `grep "API pentest"` → **0**, and that was the wrong probe. Listing
topic titles instead found five cards in `sec`, including **"The OWASP API Security Top 10 — Where
the Web List Stops Being Enough"**, whose subtitle was almost word-for-word the one already drafted,
plus dedicated cards on broken object-level authorisation, rate limiting and shadow API inventory.
The card was discarded before it shipped.

This is the third recorded instance of the same mistake and it now has a rule: **probe the topic
titles, not just the prose.** A phrase-shaped grep (`"API pentest"`, `"physical pentest"`) asks
whether anyone happened to use that exact wording. Listing `.topic-name` across the site asks
whether the subject is covered, which is the actual question.

### What shipped

Five cards, 29 → **34**:

- **Physical Assessments & Covert Entry** — the only engagement where being wrong means the police.
  Leads on paperwork rather than technique, including the shared-tenancy trap: a client can
  authorise entry to their suite and cannot authorise the lobby, the lifts or the loading bay.
- **Cloud Penetration Testing** — testing a configuration, not a network, and the rule that
  permission to edit permissions is equivalent to every permission.
- **Mobile Application Testing** — every mobile assessment is two assessments, and the severity is
  in the second one. States plainly that pinning and root detection are speed bumps, not controls.
- **Rating a Finding — CVSS, EPSS & the Number the Client Will Argue About** — CVSS was cited seven
  times in the domain and explained nowhere. Includes the disputes, and the position that a
  low-scoring finding you are worried about belongs in the narrative anyway.
- **Responsible Disclosure & Bug Bounties** — finding it was never the risky part. Covers the four
  positions a researcher can be in, and the minimum-proof line that separates a report from an
  unauthorised access to personal data.

### A stamp correction worth recording

Stamping pentest moved **six existing topics from 2026-06 to 2026-07**. Verified rather than
accepted: `git log -S` on a distinctive line from each shows them created in `d38592c`, dated
**2026-07-13**. The old 2026-06 stamps were wrong, and they were wrong because the domain had not
been re-stamped since the `body_times()` fix — the old code took the maximum blame date over the
whole topic span *including the opening tag the stamper itself rewrites*, which pinned the date to
the previous stamping run. Any domain not re-stamped since that fix may carry the same error.

Site total 1,364 → **1,369** topics. `check_markup.py` clean · `lint_content.py` clean ·
`smoke_test.mjs` 110/110 · related.json +14 links from the new cross-references.


## Session record — correcting the freshness stamps the fix had not reached

The pentest wave turned up six topics stamped 2026-06 that were really 2026-07, and named the
cause: a domain that has not been re-stamped since the `body_times()` fix carries dates derived the
old way. That is a claim about the whole site, so it was checked against the whole site.

`stamp_freshness.py --check` named **nine domains**: ai, career, linux, military, mind, net,
philosophy, shortcut, threat. Re-stamping moved **88 topics**, in both directions:

| Change | Topics |
|---|---|
| 2026-06 → 2026-07 | 73 |
| 2026-08 → 2026-07 | 13 |
| 2026-07 → 2026-08 | 2 |

**The thirteen downgrades are the important ones.** A stamp that understates freshness is a nuisance;
one that overstates it tells a reader a card was reviewed a month more recently than it was, which
is the failure a freshness stamp exists to prevent. Traced properly rather than accepted: the
Subnetting & CIDR card's topic body was last touched by `1bc9ce8` on **2026-08-02** — a site-wide
acronym pass across 31 files — which `global_markup_passes()` correctly ignores, leaving 2026-07 as
the real date. A naive `git blame` over the same span reports August and would have "confirmed" the
wrong answer. The tool is more careful than the check.

`--check` now reports nothing to update, so the site is consistent for the first time since the fix
landed. 1,310 stamps across 29 files; the acronym domain's 59 topics are generated and carry none by
design.


## Session record — Track AX: the rename registry, and two items that were already built

Track AX's checklist predates most of the freshness tooling. Verified first, as usual: **per-topic
freshness metadata** and **volatility tags** are both shipped, and the link-rot item has nothing to
check — one external link on the whole site.

The volatility tag is worth a note because it shipped in a *better* shape than specified. The item
asked for topics to be tagged stable or volatile. What exists instead is
`<span class="volatile" data-checked="YYYY-MM">` around the individual claim, because what goes
stale is a console name or a limit, not a card: "Security &amp; Compliance Center" ages while the
paragraph explaining retention around it does not. Tagging the topic would have marked the whole
card suspect to protect four words.

### The rename registry

`data/renames.json` holds 25 renames; `tools/check_renames.py` gates them in CI. Three design
decisions carry the whole thing:

- **A historical mention is not an error.** "Entra ID (formerly Azure AD)" is a card doing its job.
  The checker looks for that framing, or for the new name within ninety characters, and stays quiet.
- **`allow` for names that outlived the rename.** "Azure AD Connect" contains "Azure AD" and is
  correct; `twitter:card` is the meta tag's actual name; "Office 365" is still the literal label of
  a Conditional Access app group.
- **Prose only.** A renamed product inside a command, a URL or an attribute is usually still right —
  `mxtoolbox.com/blacklists.aspx` is a real address — and reporting it is pure noise.

It found **nine real uses across six files**, every one a case of an old name reading as current:
`WSUS / SCCM / Intune` in a patching table, "Salesforce, Office 365, Gmail" as SaaS examples,
"Okta, Azure AD, Ping" as identity providers, "Azure AD Conditional Access", a Kubernetes
`whitelist`, and three mail-reputation `blacklist`s. All nine fixed. Verified the checker fails on a
planted regression before wiring it into CI.

### Track AX after this wave

Four items open: **fact-anchor comments**, **per-domain changelog**, **contradiction check** and
**screenshot-dated warnings**. The contradiction check is the interesting one — cross-domain
disagreement about a number or a definition is the failure mode this site is most exposed to at
1,369 topics, and nothing currently looks for it.


## Session record — Track AX: the per-domain changelog

An **Updated** row on every domain's landing card — the month the domain was last reviewed, and the
three topics reviewed then, as links.

**Generated from the stamps, not from git.** The item said "from git history", and doing that at
build time would have made the build depend on a repository, on `git` being present, and on blame
heuristics that already differ between git versions — a problem this project has hit before, badly
enough that CI runs `--verify` instead of `--check` because of it. The `data-reviewed` attributes
are already in the files, already derived from git by `stamp_freshness.py`, and already validated.
Reading them keeps the build offline, deterministic, and consistent with what the stamps claim.

It answers a question a reference site cannot otherwise answer and should not make the reader guess
at from the writing style: *is anyone still maintaining this?*

### The check that caught its own regression

Adding the row broke an existing check — "every 'start here' name resolved" reported **6/3**,
because the new links reuse `.di-link`. That is the check doing exactly its job: a count-based
assertion noticing that the thing it counts changed shape. It is now scoped to `.di-start .di-link`
with a comment saying why, and two new checks cover the changelog itself, including that every entry
names topics that exist and a month that parses.

Three new checks, 110 → **113**. Budget raw 5.5 / 8.0 MB.

The one domain with no changelog entry is `acronym`, which is generated from the dictionary and
carries no stamps by design — the check allows exactly one such domain rather than skipping the
assertion.


## Session record — Track AX: the contradiction check

At 1,369 topics the failure this site is most exposed to is not a wrong fact. It is two cards that
are each defensible and disagree with each other — and nothing was looking for that. The linter
checks structure, the markup checker checks well-formedness, and both are perfectly content with two
cards saying different things.

### Scope, chosen honestly

Two kinds of disagreement are mechanically checkable, and the tool checks those two rather than
claiming to check contradictions in general:

1. **A hand-written acronym expansion that disagrees with the dictionary.** This one is invisible to
   every existing tool: `annotate_acronyms.py` only ever *adds* expansions and never reads the ones
   an author typed, so `RTO (Recovery Time Object)` sits next to a dictionary saying *Objective*
   forever.
2. **Ports attached to a service.** "SSH on 22" appears everywhere here; one card saying 23 is both
   wrong and unfindable by eye.

A limit, a retention period or a version number needs to know what the number is *about*, and no
amount of regex supplies that. The docstring says so, so nobody later "completes" the tool into
something that reports noise.

### The heuristic that made it usable

The first run produced **40 findings, of which about five were real**. The rest were parentheticals
that are not expansions at all: `SIEM (Wazuh, Security Onion)`, `AI (NIST AI RMF)`, `C2 (Beacon)`,
`IDOR (Lab Practice)`.

The fix is the definition of an acronym: **an expansion's initials spell it**. Taking the initials of
the parenthetical's significant words and comparing them to the acronym — with one letter of slack
for shorthands like *Next-Gen Firewall* for NGFW, and a floor of two initials so `AI (AlphaGo)` and
`AP (Authenticator)` cannot pass on a single letter — took 40 findings to **8**, all real.

### What the eight were

Two were genuine second meanings the dictionary lacked, now added: **CD** is *Continuous Delivery*
and *Continuous Deployment* (a real distinction the devops card was drawing correctly), and **AV** is
*Antivirus* everywhere except `grc`, where it is *Asset Value* in the quantitative risk formula — a
`byDomain` override, and the site's ambiguity warning count dropped from 4 to 3 as a result.

The other six were the site disagreeing with itself in miniature: `ARO` written as *Annual* in one
card and *Annualized* in another, and four places where the annotator's correct expansion sat
directly beside a hand-written one that said something slightly different —
`ALB (Application Load Balancer) (Application LB)`. Redundant *and* inconsistent, in one string.

Verified the checker fails on a planted contradiction before wiring it into CI.


## Session record — a formatting normalisation, and what `--ignore-rev` cannot do

849 opening tags and 729 closing tags across twelve content files were written in a formatter's
line-broken style:

```
<span class="topic-name"
  >Stoicism — The Art of Rational Endurance</span
>
```

Valid HTML, and every tool here already coped: `lint_content.py`'s regexes and `script.js`'s
`classRe` both allow attributes to run across lines. What it broke was the obvious thing — a plain
`<span class="topic-name">` search misses **41 topics**, 3% of the site invisible to any grep. That
cost time twice in one session, most visibly when an audit reported 7 topics in `philosophy` where
there are 14.

### Proving a formatting change is a formatting change

Whole-document comparison **does not work here** and it is worth knowing why before someone tries
it: the domain bodies ship inside `<script type="text/html">`, so `html.parser` hands back one
enormous text node per domain and reports a difference for any whitespace change at all.

The comparison that does work extracts each of the 30 deferred blocks and parses *those* as
fragments, comparing streams of `(tag, attrs, text)` events with whitespace collapsed. All 30
identical. `<pre>` blocks were excluded from the rewrite, since their whitespace is literal.

### The freshness cost, measured rather than assumed

A mechanical commit is supposed to be neutralised by `.git-blame-ignore-revs`. This one is listed
there and **it does not work**, which was worth establishing rather than assuming:

| Attempt | Result |
|---|---|
| `--ignore-revs-file` with the commit listed | still blames the reflow |
| `git blame -w` (ignore whitespace) | still blames the reflow |
| `-w -C -C` together | still blames the reflow |

The reason is that this commit **merged lines** rather than reindenting them. `--ignore-rev`
reattributes a line to whatever touched it before; a line assembled from two others has no single
predecessor, and `-w` cannot help for the same reason. Four cards in `script.html` are therefore
stamped 2026-08 for a reflow, and three more in `career.html` and `mind.html` still date to the
lifestyle split for the matching reason — the split *created* those lines in files that had no
earlier version of them.

Seven cards, one month late, permanently. The alternative is a hand-kept per-topic override list,
which would rot faster than the error costs. Recorded in `.git-blame-ignore-revs` beside both
commits so the next session does not spend an hour rediscovering it.

### Also this wave

Two smoke checks pin the runtime behaviour the whole investigation started from: **every indexed
topic reaches `stIndex()`**, and every row in it has a name. `stIndex()` silently drops a topic it
cannot parse a name for, and everything the study tools offer is built from it — decks, quizzes, the
palette, paths, related topics. A topic that falls out is not broken, it is *absent* from all of
them, and nothing would have said so. 1,369 / 1,369 today. 113 → **115**.


## Session record — productivity content wave: the study-skills half of a study site

`productivity` was the thinnest substantial domain on the site at ten topics, which is an odd gap
for a site whose entire purpose is helping someone learn this material. Audited by listing topic
titles across all 30 domains — the lesson from the pentest wave, applied first this time rather than
after writing a duplicate card.

**Confirmed void.** Nothing on retrieval practice, interleaving, deliberate practice,
procrastination, exam technique or energy management existed as a topic anywhere. The nearest
neighbour, `career`'s *How Adults Actually Learn*, is about **teaching other people** — cognitive
load in a session, measuring training by behaviour — so it was read first, kept distinct, and
cross-referenced rather than duplicated.

### Six cards, 10 → 16

- **Retrieval Practice** — the most replicated finding in the study of studying, and the one this
  site's own spaced-repetition scheduler implements. Includes the free version for technical work:
  say what the command will output before you run it.
- **Interleaving & Desirable Difficulties** — the idea that reorganises the rest: performance during
  practice and retention afterwards are different things, and several conditions that worsen the
  first improve the second. Includes when *not* to interleave, which most treatments omit.
- **Deliberate Practice** — why "10,000 hours" is the wrong number, and how to manufacture the
  missing condition in an IT career, which is almost always feedback.
- **Procrastination** — a mood problem wearing a time-management costume, with the finding that
  self-criticism reliably increases the next delay, and a table of the things that merely look like
  procrastination and need different help entirely.
- **Exam Technique** — the second skill, and the cheaper one. A table that separates losing marks to
  knowledge from losing them to process, since only one of those is fixed by more study.
- **Energy, Not Time** — an hour is not a unit of capacity, and a plan missed weekly for two months
  is a plan that does not fit the life it was written for.

The cards deliberately cross-link into each other and into `mind` and `career`: retrieval → spacing
→ the site's own scheduler, exam technique → sleep, procrastination → burnout, energy → desk body.
Eight new links folded into `related.json`.

Site total 1,369 → **1,375** topics. Budget raw 5.5 / 8.0 MB, content elements 111,516 / 175,000.
`smoke_test.mjs` 115/115, every checker clean, no stamp churn on the existing ten.


## Session record — splitting the biggest file without moving a single slug

`data/script.html` was 762 KB and 145 topics — a fifth of the site's topics in one file, and by a
wide margin the hardest to work in. Track AY specified the safe shape years of caution had already
arrived at, and it is worth restating because it is the whole reason this was low-risk: **split into
parts that build into the same domain**, not into new domains.

Topic ids come from `build.py` stamping slugs in document order with de-duplication carried across
the whole site. Split `script` into three *domains* and that order changes, every duplicate-title
suffix shifts, and permalinks and stored progress break silently. Split it into ordered *parts*
concatenated back into one domain and the byte sequence build.py sees is exactly what it saw before.

### The gate that made it safe

`index.html` was built before the split, and again after. **Byte-identical.** Not "tests pass" —
identical output from identical input, which is the only evidence that matters for a refactor whose
entire claim is that it changes nothing.

The parts are exact slices of the original file, joined with nothing, and `build.py` refuses to
concatenate a part that does not end in a newline — the one way this could silently glue a card's
last line to the next card's first.

### One helper, six tools

The real work was that six tools each had their own idea of where a domain's source lives.
`domain_files(domain_id)` in `lint_content.py` is now the single answer — one file, or its parts in
filename order, and it *errors* if both exist rather than quietly preferring one.

Two subtleties the tools surfaced, both of which would have been silent bugs:

- `annotate_acronyms.py` derived the domain from `path.stem`, so `script.03-python` looked like a
  domain called `script.03-python` and its `byDomain` acronym overrides stopped applying. It reads
  the filename prefix now. Caught because `--check` reported `script.05-platform.html` out of date.
- `fix_topic_names.py` already had a local function called `domain_files`, which the import
  shadowed into infinite recursion. Renamed to `source_files()`.

`stamp_freshness.py --only` now accepts either a domain (`--only script`, all six parts) or a single
part (`--only script.03-python.html`) — which is the day-to-day benefit of the split: after editing
one part, only that part is restamped.

### Everything else, unchanged

`smoke_test.mjs` 115/115 · `lint_content.py` clean · `check_markup.py` now parses 36 files instead
of 31 · renames, contradictions and paths all clean · `fix_topic_names.py --check` reports the same
103 aliases.

### The freshness cost, again measured

Restamping after the split moved **20 of the 145 cards** from 2026-07 to 2026-08. `-C -C` copy
detection recovers the other 125 by itself — the delete and the adds are one commit, which is
exactly the case it is for — and the 20 that fall through are short blocks under git's
copy-detection minimum. Listing the split in `.git-blame-ignore-revs` recovers **none** of them,
measured rather than assumed, for the reason the file's own header gives: the part files did not
exist before this commit, so there is no earlier version of those lines to fall back to.

Twenty cards, one month generous. Recorded beside the commit in the ignore file, with the
measurement, so the next session does not repeat the experiment. That is now the third instance of
the same limitation in this session, and the pattern is worth stating once: **a mechanical commit
that creates or merges lines cannot be neutralised by `--ignore-rev`.** Only one that *modifies*
existing lines can.


## Session record — repo hygiene: one entry point, one contract, one fewer megabyte

Three Track AY items, all small, all overdue.

### `make`, not `just`

`make` is already on the machine; `just` would be a dependency to install before you can build a
site whose entire selling point is having none. `make` builds, `make check` runs every static gate
in fastest-failing order, `make test` drives the browser, `make all` chains them, `make stamp
ONLY=<domain>` restamps one domain, and `make help` lists them.

The value is not saving keystrokes — it is that **the order is now recorded somewhere other than
a person's memory**. The acronym domain is generated from the dictionary, the annotator rewrites
content using it, and `build.py` assembles what both produced. Run out of order you get a page that
looks correct and is stale, which is the worst kind of wrong for a reference site.

### Topic IDs are a contract

Written into `CONTRIBUTING.md`, because the `script` split made it concrete and because this is the
one thing in the repo that silently breaks *other people's* saved state rather than the build.

A topic id is the permalink someone shared, the key their progress is stored under across five
`localStorage` prefixes, and the key `related.json` and `paths.json` point at. The section carries a
table of what does and does not move an id, and two rules that follow from it: **prefer parts over
new domains** when a file gets too big, and let `fix_topic_names.py` write the alias when you do
rename. Plus the proof technique the split used — build before and after, compare bytes.

### patches/ archived

54 one-shot content-injection scripts, 1.8 MB, untouched since 2026-07-04, whose output has been in
`data/*.html` since each wave shipped. Tagged `archive/patches-2026-08` and deleted. The tag is
local; it exists so the directory is recoverable by name rather than by SHA archaeology:

    git checkout archive/patches-2026-08 -- patches/


## Session record — Markdown export, and three bugs the tests found

⬇ Export as Markdown in the study menu: a topic, a domain, the study list, or the whole library,
copied or downloaded as a `.md` file. It converts from the **deferred blocks**, not the live DOM, so
a domain nobody has opened exports exactly like one that has — the constraint every feature here
lives under, asserted directly by a check that runs the export with zero topics rendered.

### Structural, not generic

The converter knows this site's conventions rather than HTML in general, and it is much better for
knowing them: a `.concept-label` becomes a bold kicker rather than a paragraph, a `.concept-title`
becomes `###`, a `.xref` becomes italics, an `.acro-exp` is kept inline because an exported file has
no hover to reveal it. Fenced code keeps its own indentation — the whitespace tidy-up deliberately
skips fenced regions, since collapsing it would corrupt every example on the site.

### What writing the tests found

Three real bugs, none of which would have been visible by skim-reading an export:

1. **Every table on the site exported with an empty header row.** `mdTable` keyed off `<thead>`, and
   almost no table here has one — the header is a bare `<tr>` of `<th>`. So the header line came out
   as `| | | | | |` and the real headings were pushed into the body. Now it finds the first row
   containing a `<th>`.
2. **Div-built tables flattened into one unreadable line.** The layer stacks and comparison grids
   carry their structure in nested `<div>`s, and nothing emitted a line break for them. Block-level
   elements now end a line, and a `.layer` row joins its cells with `—` on one.
3. **Leading whitespace broke every heading.** Text nodes between elements were emitted verbatim, so
   headings came out as `&nbsp;### Title` and no Markdown renderer would have treated them as
   headings.

And two bugs in the *checks themselves*, which is its own lesson: the topic chosen for the table
test was matched on the bare string `<table` and turned out to be a code sample, and the
run-splitting used `runs[runs.length - 1] ||= []` on an empty array — which assigns to index `-1`,
creating a property rather than an element, so the "square rows" assertion was silently examining
nothing at all and would have passed on any output. **A check that examines nothing passes.**

Seven new checks, 115 → **123**.


## Session record — PWA polish: consent, and a version nobody has to remember

Two changes, and the second is the substantive one.

**The worker stopped taking over without asking.** It called `skipWaiting()` on install, which swaps
the cached assets under a page that is already open — a new `script.js` talking to an old
`index.html`. On a page that keeps a reader's progress, bookmarks, notes and scheduler state in
`localStorage`, that is not a cosmetic risk. The new version now waits, the page offers a
dismissible reload, and `skipWaiting()` happens only when the reader accepts. A `controllerchange`
guard stops the reload looping when several tabs accept at once.

**`CACHE_VERSION` is derived, not typed.** A hand-bumped cache version has two failure modes and
both are common: forget to bump it and returning visitors keep a stale page indefinitely; bump it
every deploy and an unchanged build throws away a good cache. `build.py` now hashes the three files
that actually change and writes `techref-<hash>` into `sw.js`, so the version moves exactly when the
bytes do. CI fails if it is stale, the same way it already fails on a stale `index.html`.

### Testing what cannot be tested here

The worker only runs over http(s) and the smoke tests run over `file://`, so the registration path
is genuinely out of reach. Rather than skip the feature, the four checks cover the part that
actually breaks: the toast renders **once** rather than once per event, carries `role="status"`,
posts exactly `{type:"skip-waiting"}` to the waiting worker when accepted, and can be dismissed. The
comment says why the registration itself is not covered, so the gap is a recorded decision rather
than an oversight.

123 → **127** checks.


## Session record — print packs

🖨 Print pack: a domain, a learning path, the study list or today's due cards, as a handout.

**Generated, not styled.** The obvious implementation is a print stylesheet over whatever is on
screen, and it cannot work here: only one domain is ever hydrated, so the pack most worth printing —
a learning path, which spans five domains in the SOC starter's case — could never be produced that
way. The pack is built into a container of its own from the deferred blocks, with every card forced
open, and `body.printing` hides everything else.

That hiding is written as `body.printing > *:not(#print-pack)` rather than as a list of things to
hide, so a header or panel added next year does not quietly start appearing on printouts.

Page breaks are set where they help: a new page per domain, never a break through a concept card,
and breaks allowed inside a topic — a card that would rather start a new page than split is worth
the whitespace; a whole topic is not.

Five checks, 127 → **132**, and the first one had to be fixed before it meant anything: it tested
the first learning path, which is entirely inside `net`, so "spans a whole path" was passing without
ever crossing a domain boundary. It now picks a path that actually crosses one — 15 topics across 5
domains, built with zero topics rendered.


## Session record — Track AJ: accessibility CI, and the sixteen violations it found

`tools/a11y_test.mjs` runs axe-core over three states — the shell at load, an open domain with an
expanded topic, and a study dialog — in **both themes**. Six scans. It is deliberately separate from
`smoke_test.mjs`: the smoke test asserts specific behaviour and must pass on every commit, while
this runs a third-party rule set that can grow new rules between versions, and mixing them would
make a smoke failure ambiguous. It scans one domain rather than thirty, and says why: the content
markup is generated from the same conventions everywhere, so the thirtieth domain exercises the same
rules at thirty times the cost, and `lint_content.py` is what keeps the conventions uniform.

The first run: **0 of 6 scans clean, 16 serious violations.** Three distinct problems.

### The accessible name nobody gave the search box

`label-title-only`: the search input's only accessible name came from its `title`, which carries the
operator documentation. One `aria-label`.

### Colour, in both directions

Nearly 300 nodes failed contrast, and the causes were worth separating rather than "darkening things
until axe went quiet":

- **All 30 filter chips were unreadable in light mode.** Each carries its own hue, all picked
  against a near-black background, and every one of them failed on a light one — in the single place
  the whole page is navigated from. Each is now darkened to 4.6–4.7:1, computed rather than
  eyeballed so nothing is darkened more than it needs to be, and the identity survives.
- **`--cyan`, `--green` and `--red` failed in light mode** at 3.4–4.4:1, and they are used for small
  text throughout. Darkened at the token, which fixed many nodes at once.
- **The active ALL chip was `#fff` on a light background** — 1.1:1. It had simply disappeared.
- **`--muted` failed in dark mode** at 3.3–3.8:1, and the per-domain `--accent` values had the same
  light-mode problem as the chips: one override per domain fixed the see-also links, landing card
  buttons and every clickable cross-reference together.
- **Two decorative `opacity` values were doing the damage**, not the colours: the cert tags' `0.7`
  cost 1.3 contrast points in both themes, and the dashboard's `0.55` on untouched rows multiplied
  against already-muted text. Both replaced with colour choices, which is what a reader with low
  vision can actually work with.

### The one that was a real bug, not a shade

`nested-interactive`, on all 1,375 topics: `.topic-header` had `role="button"` **and contained the
★ ✓ 📝 🔗 buttons**. A control inside a control is invalid ARIA and leaves those four ambiguous or
unreachable to a screen reader.

The header is now layout with no role, and the clickable part is a real `<button class="topic-toggle">`
wrapping the icon, name and badge, with the tools and the chevron as siblings — so the row order is
unchanged and the chevron, being decorative, is `aria-hidden` and outside the button's accessible
name. All twelve places that set a topic's open state now go through one `setTopicOpen()`.

**It broke everything first, informatively.** The initial version wrapped the chevron too, so
`header.insertBefore(tools, chev)` threw against a node that was no longer its child —
`enhanceDomain` aborted, and nine smoke checks failed at once. That is the smoke suite doing exactly
its job: a structural change that looked fine in one place took the whole domain's setup with it,
and the failure list said so within seconds.

### Result

**6/6 scans clean.** `make a11y` runs it; CI runs it as part of the browser job. Two new smoke
checks pin the structure that replaced the violation, 132 → **133**.


## Session record — link previews, and a guard on the build itself

### The site had no link preview at all

Not "the per-domain cards were missing" — no `description`, no Open Graph, no Twitter card. A link
to it rendered as a bare URL everywhere it was shared, which for a free public reference is a
straightforward loss.

`tools/gen_og_image.mjs` renders `Img/og-card.png` at 1200×630 from an HTML template through
Playwright, which is already a dependency for the tests. The counts on the card — 1,375 topics, 30
domains, 0 third-party requests — are **read from the sources at render time**, so the card cannot
advertise a number the site no longer has, and `--check` fails CI if it is stale.

**Per-domain cards were not built, on purpose.** The original item asked for one per domain. Domains
here are hash fragments; no crawler distinguishes `/#net` from `/`, and none runs the JavaScript
that would render that domain. Thirty images that nothing would ever request. The reasoning is in
the item and in the tool's docstring so it is not re-proposed.

A smoke check asserts the preview text quotes the site's **real** size — the description is written
by hand and the card is generated, so they can drift, and a preview advertising last year's numbers
is exactly the kind of wrong nobody notices for a year.

### Build determinism

`tools/check_determinism.py` builds twice and compares bytes. Cheap, and it is the check that gives
meaning to the technique this session leaned on twice: *build before, build after, compare*. Without
it, "byte-identical" only ever meant "identical this once".

Verified against a planted `time_ns()` in `build.py` before being wired into CI — it reported both
outputs differing and exited non-zero.

135 checks; `make` now also has `a11y` and `og` targets.


## Session record — Track AX closed: dated claims and where numbers came from

The last two items in the track, and they are two halves of one idea: a reference site's real
failure is not being wrong when written, it is being right when written and quietly wrong two years
later.

### Two conventions, one checker

`tools/check_volatility.py` validates both and separates what it can gate from what it cannot:

- **Errors** — a `data-checked` that is malformed or in the future, an anchor missing its source.
  Unambiguous, so they fail the build. Verified against a planted future date and a fieldless anchor.
- **A queue** — every dated claim, oldest first, so a freshness pass has a starting point.
- **Candidates** — topics naming a vendor console with no dated span. **Reported, never failed.**
  Fourteen remain and most should stay that way: "Microsoft Management Console" has not moved in
  twenty years, and a gate here would only teach people to add a span they do not mean.

The candidate regex is deliberately narrow. Matching the bare word "console" finds 133 hits on this
site, nearly all of them terminals; a queue that noisy is wallpaper, not work.

### Screenshot-dated warnings, as spans rather than notes

The item asked for a "console as of <date>" note per card. What shipped instead marks the console
**name** — `<span class="volatile" data-checked="2026-08">Intune admin centre</span>` — because that
is the thing that changes, and a whole-card note would put a date on a paragraph that is still
correct. Ten added, 33 → 43 dated claims.

### Fact anchors

`<!-- fact: <claim> | source: <where> | checked: YYYY-MM -->`, immediately before the element making
the claim. Invisible to the reader, and it turns "re-research this" into "re-verify this". Five
applied, chosen as vendor-defined numbers a reader could act on — the 93-day platform-metric
retention (the plan's own example), the 180-day tombstone lifetime, Windows Server's 180-day
evaluation, the gMSA 240-character/30-day defaults, and the 30-day group soft delete.

`CONTRIBUTING.md` says what deserves one and what does not: not arithmetic, not something the card
derives itself, not a figure whose source is the card's own worked example.

### Track AX is now closed

All eight items. Three were already built and were ticked after verification, one measured itself
away (one external link on the whole site), and four shipped this session: the rename registry, the
per-domain changelog, the contradiction check, and these two.


## Session record — the structured content model, evaluated and declined

Track AY held this decision open for a reason, with an explicit rule attached: *only worth it if
Tracks AG/AK actually need topic-level structured data — do not do it for tidiness alone.* Both
tracks are now finished, so the rule can be applied against evidence rather than intuition.

### What the consumers actually needed

Everything Tracks AG and AK asked for got built this session. What each one turned out to need:

| Consumer | Needed |
|---|---|
| Flashcards, quiz, exam mode | `.topic-name`, one `.concept-title`, one `.concept-desc` — three regexes |
| Spaced repetition, progress, streak | topic **ids** and `localStorage`. No content at all |
| Learning paths | an ordered list of ids in `paths.json` |
| Related topics | a map of ids in `related.json`, seeded from the `xref` spans |
| Domain landing cards | `domain-intros.json`, keyed on domain |
| Per-domain changelog | the `data-reviewed` attribute |
| Print packs | the topic's markup, used verbatim |
| **Markdown export** | **structure — the one real case** |

Seven of eight needed ids and small external JSON files. That is not a content-model problem; it is
exactly the architecture already in place, and each payload took an afternoon.

### The one that wanted structure, priced honestly

The Markdown export is the case the item was written for, and it did cost something: a ~120-line
structural converter, plus three real bugs that only surfaced because the tests were written —
every table exporting with an empty header row, div-built tables flattening into one unreadable
line, and headings carrying leading whitespace.

Against that: **1,375 topics to migrate**, and a build that becomes a real program with a template
layer, a schema and its own bugs. A hundred and twenty lines is not a case for rewriting the corpus.

### What the evaluation *did* find

The export's ugliest special cases are not about HTML in general. They are about a specific habit:
**78 places where a table is built out of `<div>`s** — `kc-row`, `layer-stack`, `nist-row`,
`risk-matrix` — against **1,883 real `<table>` elements**. Those 78 are why the converter needs a
`.layer` rule, why the print pack needs its own break rules, and why a naive HTML-to-Markdown pass
would produce nonsense.

So the recommendation is not "restructure the content". It is: **convert 78 elements to real
tables**, which removes the special cases, improves screen-reader output for free, and can be done
one card at a time by anyone with an afternoon. Logged as the incremental item in place of the
migration path that is no longer needed.

### The rule earned its keep

This decision was deferred across many sessions with a test attached to it. The test turned out to
be answerable only *after* building the features — and when it was answered, it said no, clearly,
with numbers. Worth remembering the next time something is tempting and expensive: writing down what
would make it worthwhile is what stopped it happening on vibes.


## Session record — mind content wave: the non-technical half of the job

`mind` was the thinnest substantial domain at twelve topics, covering the part of an IT career that
is not technical. Audited by topic title across all thirty domains first — which found that two
candidates were already handled and should not be duplicated: **difficult conversations** exists
twice, in `ops` (angry users, VIP pressure, saying no) and `eng` (giving feedback), and **money**
has two cards in `career`.

### Five cards, 12 → 17

- **Layoffs & Job Loss** — nothing on the site mentioned this at all, in a field where it happens to
  most people at least once. Separates the business decision from the verdict, gives the
  time-sensitive first week in order, and is explicit about the one thing that turns a bad month
  into a legal problem: taking company material on the way out.
- **The Always-On Feeling** — deliberately *not* burnout. Burnout is exhaustion; this is
  hypervigilance, and it usually comes first. The most useful row in it is an engineering one:
  people check dashboards off-shift because they do not trust their alerts, so fixing the alerts
  fixes the checking.
- **Comparison** — you are measuring an ordinary Tuesday against the aggregate of everyone else's
  best days. Ends on the structural point rather than the personal one: comparison is unbearable
  where admitting ignorance is unsafe, and that is a property of the team.
- **A Manager You Cannot Fix** — separates mismatch, overload, out-of-depth, structurally trapped
  and bad actor, because those are five problems with five different answers and treating them
  alike is how people stay stuck for years.
- **Asking for Help** — the four-line question that gets answered fast, the timebox that settles
  when to send it, and the other half nobody writes down: how a senior person answers decides
  whether anyone asks them again.

### A count that no longer needs remembering

The link-preview check failed on this wave, correctly: the hand-written description said 1,375
topics and the site had 1,380. Rather than edit the number, `build.py` now substitutes it — the
description and the Open Graph text carry `<!-- TOPIC_COUNT -->` placeholders filled from the topic
index. The check that caught the drift stays, but there is nothing left for it to catch.

Site total 1,375 → **1,380**. Twelve new cross-references folded into `related.json`.


## Session record — the SASE gap, found by probing subjects rather than domains

At 1,380 topics, picking the thinnest domain stops being the right way to find gaps. This wave
probed the other way: a list of ~70 significant IT subjects checked against every **topic title** on
the site, looking for zero hits.

Most came back covered, several under names the probe did not guess — eBPF inside a Kubernetes
detection card, TPM inside *Hardware Root of Trust*, agents inside *Agentic AI*, salary inside two
negotiation cards. The genuine hole was a cluster: **SASE, SSE, ZTNA, CASB, SWG**. Zero Trust as a
*principle* has two cards in `sec`; the product architecture that implements it — the thing
organisations actually buy and deploy — had none.

### Three cards

- **SASE & SSE** — leads with the deflationary point: it is not a technology, it is five existing
  products bought as one subscription and delivered from someone else's edge. Which changes the
  evaluation question from "is SASE good" to "is *this vendor's* gateway, and their ZTNA, and their
  CASB each good enough". Includes the SSE-versus-SASE distinction that keeps half a sales
  conversation off the table, and the two failure modes: a single point of failure you do not own,
  and TLS inspection breaking pinned applications silently.
- **ZTNA** — access to an application rather than a position on a network, with the row people
  underrate: a VPN concentrator must be reachable from the internet and has been a reliable source
  of catastrophic vulnerabilities, while a ZTNA connector only dials out. Ends on what it does *not*
  fix — reaching an application is not permission to do everything in it.
- **CASB & Secure Web Gateway** — inline versus API mode, and why the mode decides which questions
  can be answered. The shadow-IT section argues against the obvious response: blocking everything
  unsanctioned produces a workforce on personal devices where you can see nothing, so read the
  report as a demand signal — sanction, consolidate, restrict, block, in that order.

Site total 1,380 → **1,383**. Twelve new cross-references. The link-preview counts updated
themselves, which is the build-time substitution from the previous wave earning its keep.


## Session record — the virtualisation operations set, on demand

Track Z's shipped-note left a list of "narrower depth — follow on demand" items. Four of them are
the day-to-day of running a hypervisor estate, and the probe confirmed the gap: `sysprep` appeared
twice on the whole site, `maintenance mode` once, `CPU ready` once, `P2V` not at all.

- **VM Lifecycle** — templates, cloning and the identity problem. Leads on the argument rather than
  the procedure: every hand-built server is a future outage with a person's name on it. The
  duplicated-identity table (SID, secure channel, MAC, SSH host keys, cloud-init state) is the part
  that gets misdiagnosed for days, and the rule that follows is that a template is generalised once
  and never booted again.
- **Live Migration & Maintenance Mode** — what the memory pre-copy actually does, and therefore why
  everything that breaks it is something stopping the final delta from getting small. The patching
  round is written as a sequence, with the capacity check first because it is the step that gets
  skipped and the one that turns a window into an incident.
- **P2V & V2V** — framed honestly as a *last* option, with "leave it physical and isolated" listed
  as a real answer rather than a joke. The licensing row is the one that ends projects, which is why
  "keep the original powered off" is on the checklist.
- **Virtualisation Troubleshooting** — the storage, host, network, guest order, and why starting
  where the ticket points is the slowest route. **CPU ready** gets the emphasis because it inverts
  the usual reading: a guest with low utilisation that feels slow is not using the processor because
  it cannot get it, and adding virtual processors makes it worse.

Site total 1,383 → **1,387**. All suites green, budget 31% headroom.


## Session record — open-source licences, the gap the probe found next

The subject probe returned zero topic-title matches for `open source licen`, `GPL`, `MIT licen` and
`copyleft`. The prose confirmed it: **GPL and copyleft appear nowhere on the site**, on a reference
that covers dependency risk, SBOM, supply-chain security and commercial licensing audits in depth.
The obligations that come with the code were the one part missing.

One card, written to lead with the question people skip:

**"Which licence?" is the second question. The first is "are you distributing?"** Most obligations
in most licences are triggered by distribution; running something internally triggers very little.
That single distinction scopes the entire subject, and it is why the AGPL exists — ordinary copyleft
was written when software was shipped, so hosting a modified version was an obligation-free
loophole.

Two things it says that similar material usually does not. **Source-available is not open source**,
and several well-known projects have relicensed to terms that forbid exactly the hosted use a reader
might have planned, while still being described as open source in blog posts — so check the licence
file in the version you are actually pulling. And **the obligation follows the code, not the route
it took**, which now includes code an assistant suggested.

Deliberately one card rather than two. A second on choosing and trusting dependencies was drafted in
outline and dropped: `eng` already has *Dependency Risk — Transitive Depth, Typosquatting & the
Abandoned Package* and *Dependency Triage*, and `devops` has *Software Supply Chain Security*. The
audit-first rule applies to my own good ideas.

Site total 1,387 → **1,388**.


## Session record — Track AP depth, as the re-audit specified

The item named two gaps and predicted their shape correctly: "neither is a rewrite; both are depth
on an existing card or one new card each". Both became new cards, because each is a different
*question* from the ones the concept cards answer rather than more detail on the same one.

**Certificate & PKI Migration.** The insight it is built around is that a certificate migration runs
in the opposite direction to the instinct: you do not start by issuing new leaf certificates, you
start by asking whether anything in the estate can validate the new chain at all. Two things fall
out of that. The **HSM certification lag** — a validated module cannot ship a new algorithm the week
the standard lands, so the implement-validate-buy-install pipeline, not the cryptography, sets the
earliest possible migration date. And the **long tail**: building controls, medical equipment,
field devices and appliances whose vendor is gone will never receive a new algorithm, and the honest
answer for all of them is the same — terminate the modern cryptography at a proxy you control and
let the legacy device speak whatever it can, on a segment where that is acceptable.

There is also a genuinely cheerful note in it, which is rare for this subject: as public certificate
lifetimes fall toward weeks, the automation that becomes mandatory is the same automation that makes
an algorithm change a configuration change. **Short lifetimes are crypto-agility arriving by another
route.**

**Reading a Cryptographic Claim Critically.** Built on the observation that every serious failure in
deployed cryptography has been in key management, mode selection or protocol design rather than in
the cipher — which is precisely why the cipher is the part printed on the slide. The most useful
thing in it is the ten-second test: *what happens when a user forgets their password?* If the vendor
can restore the data, they hold a key. That may be perfectly acceptable; it is simply not the
product the marketing described.

`sec` 84 → **86**. Site total 1,388 → **1,390**.


## Session record — Track AJ closed: visual regression, scoped to survive

The last open item in the track, and the one most likely to be built badly. The spec said "headless
screenshots of a few representative topics in both themes". Built that way it would fail on every
content wave, and **a check that fails constantly is one people learn to ignore** — which is worse
than not having it, because the ignoring spreads to the checks that matter.

So it shoots one thing: **the filter bar**, both themes, one viewport. Thirty coloured chips in a
row. It changes rarely, every visitor sees it, and it is the exact place the light-mode contrast bug
lived.

### Two things the first attempt got wrong, both visible only by looking

The first version screenshotted the whole `<header>`. Opening the baseline showed why that was a
mistake twice over: the header is dominated by **a large static illustration** that can never
regress and made the baseline 290 KB, and it contains the **rotating quote** — so the check would
have failed at random, on a schedule nobody could predict. Switching to the filter bar took the
baselines from 600 KB to 68 KB and made them deterministic.

### The threshold is calibrated, not guessed

Repeated runs in one environment differ by **exactly zero** pixels. Reverting a single chip's colour
to its pre-fix value moves **0.111%** — one chip's text is a small share of a bar of thirty. The
first threshold, 0.2%, would have watched that go straight past; it is now 0.05%, verified to fail
on the planted revert and pass on the restore.

The docstring names the escape hatch explicitly: if a runner's font rendering ever makes this noisy,
raise the number or drop the shot — do not silence the job.

### Track AJ is now closed

All eight items. Three were already shipped, one measured itself away, and four were built this
session: the markup validator with its self-test, the acronym drift report, the accessibility scan
that found sixteen violations, and this.


## Session record — closing Track BC's two open items

The two Kubernetes items the track left explicitly open, both written to fill the gap the note
described rather than to restate what the neighbouring cards already say.

**Secrets in Kubernetes.** The note asked for "the options comparison", and that is the middle
section — encryption at rest, Sealed Secrets, External Secrets, the CSI driver, workload identity
federation, and calling a cloud secret manager directly — each labelled with the problem it actually
solves, because they solve different ones. The framing around it matters more though: *every option
except the last two is a better way to store a long-lived credential, while those two remove the
long-lived credential*.

Two things in it that get missed. **Permission to create a pod in a namespace is permission to read
every Secret in it**, because a pod can simply mount them — so namespace RBAC is a boundary between
teams, not between a team and its own secrets. And most real exposure is not the storage at all: it
is environment variables in a pod description, a framework logging its configuration at start-up,
Helm release history, CI output, and debug containers.

**Ingress & API Exposure.** Built on the observation that the ingress is the narrowest point in the
system and the cheapest control point available — and the most commonly wasted, run as a router
while authentication, rate limiting and header hygiene get reimplemented per service. Names the
Ingress / Gateway API / service mesh division of labour, and says why the Gateway API split is worth
understanding even if you never adopt it: with plain Ingress, anyone who can create the object can
usually claim any hostname, so separating listener ownership from route ownership is a permissions
model rather than a feature.

Its debugging list ends where it should: **"Service has no endpoints" is the most common cause of a
502 from an ingress** — a selector typo or an unready probe — and the Ingress object reports itself
perfectly healthy throughout.

Site total 1,390 → **1,392**. Track BC is closed.


## Session record — four single-item closures: AN, AU, BF, and BC before them

The live content backlog was eleven items across five tracks. Four are now closed; the six remaining
are Track AV's specialist-practice set.

**Signals** (`hw`) — the note said "the noise and grounding half is the part with real IT
application", and that is where the weight went: ground loops in audio and video, the missing common
ground that makes a serial link work on the bench and fail on site, induced interference near
machinery, and the device that only works when you touch it because *you* are the ground path. Two
rules carry most of it — ground shields at one end only, and separately powered devices exchanging
data need a shared reference. It also carries aliasing across into ordinary monitoring: a metric
sampled every five minutes cannot represent a thirty-second event and will draw a confident smooth
line through spikes it never saw.

**Teaching a Tool You Just Learned** (`career`) — the argument is that one step ahead is the *best*
distance to teach from, not a compromise: the expert has forgotten what was confusing and you have
not, and that advantage expires within months. The highest-value artefact a recent learner can
produce is the one experts never write — a table of exact error text and what it actually meant.
The credibility problem is solved by stating the distance, not by waiting for mastery.

**Third-Party Data Sharing** (`grc`) — written to supply precisely the half the note said was
missing. A contract is a promise, enforceable afterwards at cost; a technical limit is a fact that
applies on the day. The verification section is the part that rarely exists: capture what the
integration actually sends once a year (**field creep** is the normal state of a long-lived feed),
ask for evidence of deletion rather than confirmation, and test the export before you need it,
because an exit clause with no working export is a clause and not an exit.

Site total 1,392 → **1,395**.


## Session record — Track AV closed: the specialist-practice set

Six cards into `career`, closing the last of the live content backlog. `career` 38 → **44**.

Each is built on the one thing that distinguishes it from ordinary consultancy advice:

- **Subcontracting & Partnering** — when you are prime, *the client's opinion of the work is their
  opinion of you*; delegating delivery does not delegate reputation, so review time is a real cost
  that has to sit inside the margin before the price is agreed. The honest summary is that
  subcontracting converts a delivery business into a management business, and people who love the
  work often discover they have hired themselves into a job they did not want.
- **Productising a Service** — same work, named scope, fixed price. Written down, the reason it
  sells better is a fact about buyers: an unfamiliar supplier asking for an open-ended commitment
  needs far more trust than one asking for a bounded, named amount. Price from your **worst** run,
  and write the exclusions before the inclusions.
- **Fractional & Advisory Roles** — the failure mode is a client who wanted *capacity* buying
  *judgement*, and the rule for doing the job in two days a month is that your success condition is
  the client needing you less. Firm on one thing: lending your title to a policy you cannot
  influence transfers all the risk and none of the authority.
- **Running a Security Assessment** — an engagement is a sequence, and the technical work is the
  smaller half. Sell the **retest** in the original engagement, because one that must be separately
  justified three months later usually is not. The debrief runs technical-team-first, since the
  people who will implement every fix are the people the findings expose.
- **Expert Witness & Forensic Work** — the duty is to the court, not to whoever is paying, and an
  expert who advocates is ineffective rather than merely unethical. The timezone row is not a small
  point: normalisation failures have undone more digital timelines than any technical error.
- **Training as a Product** — the lab is where the budget goes, and the discipline that saves you is
  that it must reset in minutes and run without your laptop. Happy-sheets measure enjoyment; a
  client who cannot see a change will not rebook.

### A mistake worth recording

The splice used `glob("scratchpad/av/*.html")` and the directory still held **two cards from a
session two days earlier** — so it appended eight files and shipped two topics a second time.
`lint_content.py` caught it immediately, by name, with both line numbers: *slug already used by
career.html:2561 — permalinks shift*. Reverted and redone with an explicit file list.

Two lessons. **Glob a scratchpad and you inherit its history** — name the files. And the
duplicate-slug guard, ticked earlier this session as "already shipped", earned its place within the
hour: without it two duplicated topics would have shipped and quietly shifted the ids of everything
suffixed after them.

Site total 1,395 → **1,401**. The live content backlog is now empty.


## Session record — the Appendix-8 gaps, closed

The live backlog emptied last session, so this one went to the oldest open list in the file:
**§8, "subject gaps with no track"**, written months ago and never revisited. Nine rows, three
already rejected on the merits. The remaining six were audited against the site as it is now
rather than as it was when the row was written, and the audit moved two of them before any
content was drafted.

| Row | Audit found | Outcome |
|---|---|---|
| Mainframe & legacy systems | Zero topic titles matching `mainframe`, `COBOL`, `AS/400`, `z/OS` | Written |
| Internationalization | Zero matching `i18n`, `internationali*`, `localiz*` | Written |
| Technical SEO & web ops | One card, and it is on-page metadata only | Written — the operational half |
| Accessibility beyond WCAG | Five accessibility topics across four domains | Half already covered; wrote the other half |
| Reverse engineering | A full card in `threat`, not `redteam` where the row expected it | **Already closed** — no work needed |
| Payments & fintech | PCI DSS covered in `grc`; the row's own verdict was "niche" | Left as rejected |

Two of the six needed no writing at all, and finding that out cost one grep each. **The row was
stale, not the site** — which is the argument for auditing a backlog item against current content
before treating it as work, and it is the same discipline that killed the API-pentest card
earlier: probe *topic titles*, not prose.

### The four cards

**Mainframe & Midrange** (`infra`) — the useful framing is that these systems survive for an
engineering reason, not a cowardice one: the specification is the code, and forty years of rules
about how interest accrues exist nowhere else in writing. The card is built around the fact that
you will never write COBOL and will absolutely have to parse a fixed-width EBCDIC file — so the
data traps get their own table, because every one of them parses without error and is wrong.
Packed decimal read as text corrupts money silently; a copybook is the only parser you will get;
trailing spaces are structural. Two inversions worth stating plainly: consumption is billed, so
optimisation *is* the cost control rather than something you do later; and the batch window is a
real deadline, so an integration that adds twenty minutes to a run ending at 05:50 is an outage.
The modernisation section says the comparison harness is the deliverable, and that automated
COBOL-to-Java translation produces COBOL written in Java — a maintainable legacy system converted
into an unmaintainable modern one, which reads as progress on a slide.

**Internationalization (i18n)** (`web`) — the thesis is in the title of the first concept card:
i18n is not translation, it is removing the assumptions that make translation impossible. The
whole subject compresses into the concatenation bug, so that gets the code block: `"You have " + n
+ " messages"` bakes in word order, a two-category plural rule, and the absence of gender, and no
translation budget can repair it. Arabic uses six plural categories; Japanese uses one. The rest
is the *never format these by hand* table (Swedish sorts **å** after **z**, German sorts it with
**a** — same characters, both correct), text expansion, RTL as logical properties rather than a
`direction` flip, and the form assumptions that lock people out rather than annoy them. It ends on
pseudo-localization, which is the only technique here that finds bugs **before** a translator is
hired: `[!!! Šàvé çhàngéš —— ]` exposes hardcoded strings, overflow and runtime-assembled
sentences in one build.

**Technical SEO Operations** (`web`) — the existing SEO card is on-page metadata, so this one is
the part a developer gets paged for. It is organised around *discovered → crawled → indexed →
ranking*, because naming the failing joint turns a vague complaint into a five-minute diagnosis,
and because it separates work you can do from work you cannot: an engineer who accepts a ranking
target has accepted a goal with no lever attached. The centrepiece is the mistake everyone makes
once — blocking a URL in `robots.txt` so the crawler can never read the `noindex` inside it, which
leaves the page indexed permanently and removes the only mechanism that could have cleared it. The
migration section says the redirect map is the deliverable and must be built from a crawl of the
old site *before* launch, because afterwards the list is unrecoverable. Also written down: field
data and lab data disagree, and the field number is the one that counts.

**Accessibility Remediation** (`web`) — what happens after someone hands you four hundred
findings. The argument is that the tool's severity column is the wrong sort: it describes how
badly a guideline is broken, not whether anybody is stopped, and an unlabelled submit button ends
a session while a low-contrast footer link does not. Then the fact that is invisible in the
report — **four hundred violations are usually twelve components**, because scanners count
instances and a date picker on thirty screens is thirty findings and one bug. Regrouping by
component before planning turns an unbounded slog into a bounded list, and it decides where the
fix belongs: if the accessible name has to be added at thirty call sites, the component is wrong.
The card is blunt about overlay widgets (a purchase that feels like a fix) and about optimistic
conformance statements (what converts a complaint into a documented misrepresentation), and it
ends on the observation that half an hour watching one person use a screen reader reorders the
backlog more accurately than any severity column.

### Wiring

Four new permalinks, nine cross-references resolved at build time, and **fourteen bidirectional
related-topic pairs** added to `related.json` — hand-picked, because the suggester's top hits for
these titles were `sin, cos, tan & sec` for the mainframe card and `Databases — ACID & Indexing`
for the SEO one. Token overlap has nothing to say about a subject the site has never covered,
which is exactly the case where a new card needs the links most.

One thing the tooling caught immediately: `related.json` slugs are truncated at 60 characters, so
the hand-written `…language-that-funds-it` did not exist — the real id ends `…funds-i`. The check
named the missing target and the resulting one-way edge in the same run.

Site total 1,401 → **1,405**. `infra` 45 → 46, `web` 35 → 38. Smoke **135/135** · axe **6/6** ·
visual **2/2** · budget 29% gzip headroom. The OG card was regenerated, since its topic count is
baked into the image.


## Session record — the lint counters, settled

With §8 closed, the next-oldest open decision in the file was §2: three tracked warnings,
fourteen sessions, no movement, and an explicit instruction that *picking one of the three
options matters more than which*. Measuring first changed what there was to pick.

### The number had gone up

`inline style attribute` was 1,946 when §2 was written and **2,707** when it was measured
again — up 39% while being "tracked". The four cards written earlier the same day
contributed to it, which is the cleanest possible demonstration of the section's own
hypothesis: a counter nobody is accountable for does not stall, it provides cover.

### The distribution decided the work

```
 978  style="margin-top:10px"        806  <td style="color: var(--…)">
 440  style="color: var(--cyan)"     111  <strong style="color: var(--…)">
 133  style="color: var(--amber)"     …
 104  style="margin-top:8px"
  67  style="margin-top:0"
```

Two clusters, and they wanted opposite answers.

**The spacing cluster was one shape with an existing class.** An HTML parse of all 35
domain files rather than a grep — because the question was about *parents*, not text —
returned an unusually clean result:

| | style | parent | first child |
|---|---|---|---|
| 970 | `margin-top:10px` | `.dw` | no |
| 103 | `margin-top:8px` | `.dw` | no |
| 67 | `margin-top:0` | `.dw` | **yes** |
| 2 | `margin-top:6px` | `.dw` | no |

Every single one was a `.concept-desc` inside a `.dw`; every positive margin was on a
non-first child and every zero was on a first child. And `.concept-desc.verdict` had
existed as a named class for several sessions, with a comment in `style.css` saying
content "wrote this as `style="margin-top:10px"` 313 times before it had a name; new cards
use the class". New cards did not use the class. The count had tripled.

The 67 zeros needed a check rather than an assumption: `.concept-desc` sets padding and no
margin, `.dw` adds none, and no other rule in the file touches it — so `margin-top:0` was
overriding nothing, 67 times.

**Verified rather than asserted.** 970 convert to exactly the same rendering; 105 gain
2–4px. Screenshotting three topic bodies before and after gave the honest version: two
cards **byte-identical PNGs**, and the one with five 8px gaps taller by exactly 10px — 5 ×
2px, the predicted number. That is the difference between "this should be a no-op" and
knowing which 105 places changed and by how much.

**The colour cluster wanted the opposite answer.** 806 of them colour the first cell of a
`.ref-table`, and `style.css` already carries the note explaining why: `.ref-table
td:first-child` beats a utility class on specificity, 1,614 first cells had accumulated a
class that never rendered, and the inline form is what actually works. Converting those
would reintroduce the exact bug session 18 removed. So the counter can never reach zero,
which makes a zero-ratchet the wrong instrument.

### What shipped

- `.concept-desc.verdict` applied 1,075 times; 67 no-op `margin-top:0` removed. **2,707 → 1,565.**
- A **ceiling** ratchet in `lint_content.py`: the count may fall and may not rise. Exceeding
  it is an error naming the number and the reason.
- The inline verdict margin is now its own error with a line number, so the shape that
  produced 1,142 of them cannot come back. Tested by injecting three regressions: three
  errors with line numbers, plus the ceiling breach, exit 1.
- `ai-table` retired as a warning. Its label — "prefer ref-table" — asserted a preference
  the stylesheet contradicts: `.9rem` text and an amber `nowrap` first column against 12px
  and a white one. 360 tables across 18 domains is a redesign, not a cleanup. Now a census
  line, with `CONTRIBUTING.md` saying explicitly that existing tables should not be converted.
- The dead-first-cell guard now covers `.ai-table` too — its first column is styled at the
  same specificity, and it has never carried a dead class. Guarded at zero so it never starts.
- `CONTRIBUTING.md` gained a *verdict sentence* section; the stale "313 times" note in
  `style.css` was replaced with what actually happened.

### The general lesson

Three counters, three different right answers, and none of them guessable from the label:
one was debt with a class already waiting, one was a design decision mislabelled as debt,
and one had been real debt and was fixed. **The label on a tracked warning is a hypothesis
about the number, and it goes stale faster than the number does.** Reading the distribution
took one command in each case; acting on the label without reading it would have got two of
the three wrong.

Site total unchanged at **1,405**. Smoke **135/135** · axe **6/6** · visual **2/2** · OG
card current.


## Session record — the vendor-console queue, made worth reading

`check_volatility.py` ends every run with an advisory list: *topics that name a vendor
console and carry no dated span*. It had printed **14** for several sessions and nobody had
worked it, which is the same failure mode §2 had just been fixed for — so it got the same
treatment: read the output before trusting the label.

**Of the 14, three carried a real claim.** 21% precision, on a list a person is asked to
read every session.

| Marked | Where | The claim |
|---|---|---|
| `Entra admin center ▸ Conditional Access ▸ What If` | `cloud` | A console path, inside a code comment |
| `intune.microsoft.com` | `endpoint` | A console host — and this one has already moved once, from `endpoint.microsoft.com` |
| `Teams admin` | `m365` | A table cell saying which console owns a setting |

The other eleven were four distinct heuristic bugs, each visible the moment the matching
text was printed beside the topic name rather than just the count:

- **`exchange admin` and `teams admin` matched inside longer words** — "Exchange
  Administrator" is a role, and "most Teams administration is really SharePoint" is a
  sentence. A trailing `\b` fixes both.
- **`management console` named the Microsoft Management Console** — `gpmc.msc`,
  `compmgmt.msc`, a snap-in host that has not been renamed since the 1990s. This check
  exists for vendor consoles that get renamed; MMC is the exact opposite of that. Four of
  the eleven.
- **`cloud console` is a noun phrase, not a product.** Both hits meant "whichever cloud you
  use" — one in an IaC comparison table, one in a Python automation card.
- **`\badmin\.[a-z]` matched `old-admin.example.com`** in a subdomain-enumeration card.
  Now requires a real boundary before it and skips the reserved example domains.

**14 → 2**, and the two survivors are honest ones: both say "admin centre" in passing
without making a claim about it, which is precisely the case the tool's own docstring
predicted and refused to fail the build over.

One thing was *added* while narrowing: the console **hosts**, enumerated —
`entra` · `intune` · `purview` · `compliance` · `security` `.microsoft.com`. That set is
small, and it is the highest-value thing on the whole list, because a card naming a host
that has moved is wrong rather than merely aged. Adding it produced no new candidates,
which is its own small confirmation: every card already naming one had already marked it.

### The self-test, and why this one needed it

A regex narrowed on evidence is one edit away from being widened back by someone who does
not have the evidence. So the evidence is now fixtures: ten strings taken verbatim from the
content as it was when the tuning happened, each with the reason it must or must not match,
run by `--self-test` in `make check` and in CI beside `check_markup.py`'s.

It caught a mistake immediately. The fixture asserting that `intune.microsoft.com` matches
**failed** — the card had actually been caught by "admin center" three words earlier, and
the bare host matched nothing at all. Without the fixture the enumerated-hosts rule would
never have been written, because the list would have looked like it already worked.

### The pattern, twice in one session

§2 and this were the same shape: a number printed every run that nobody had read the
composition of. In both cases the label was a hypothesis about the contents — "prefer
ref-table", "names a vendor console" — and in both cases one pass over the actual matches
contradicted it. **The count is cheap to print and worthless to act on; the distribution is
one command away and decides everything.**

Also re-measured while here: §4's content-age number. No `2026-06` stamps remain — 446 at
`2026-07`, 900 at `2026-08`.

Site total unchanged at **1,405**. 43 → **46 volatile spans**. Smoke **135/135** · axe
**6/6** · visual **2/2**.


## Session record — `ATT&CK` was two unknown acronyms

Third pass of the same method in one session, and this one was over in two commands.
`acronym_drift.py` reports capitalised tokens the dictionary has never seen. Its list runs
to 1,732 entries and is mostly product names by design — but positions **7 and 8** were
`ATT` (39) and `CK` (39).

An ampersand is not a word character, so `\b[A-Z]…\b` split `ATT&CK` in half. The
dictionary has carried `ATT&CK` since it was written; the tool had been reporting its two
fragments as unknown, at the top of the queue, ever since.

The tokenizer now joins an ampersand **only when nothing separates it from the words on
either side**, which is what keeps "Backup &amp; Recovery" as two words. 76 phantom
occurrences left the list, and four real acronyms that had been invisible as fragments
appeared: `POA&M`, `VR&E`, `W&B`, `S&P`.

Two of the four were worth acting on, and the first turned out to be a defect rather than
a gap:

- **`POA&M` was in the dictionary as `POAM`.** Content writes `POA&M` five times and
  `POAM` zero times — the only two `POAM` strings on the site were in `acronym.html`,
  which is *generated from the dictionary*. So the site was publishing a misspelling of a
  standard RMF/FedRAMP term, sourced entirely from the one file claiming to be the
  authority on it. Renamed; the reference domain now prints it correctly and the annotator
  matches the five real uses.
- **`VR&E`** added — a Veterans Affairs benefit named once in `military`, and genuinely an
  acronym rather than a product.

`W&B` (Weights & Biases) and `S&P` (Standard & Poor's) are company names and correctly
stay out.

**One judgement worth recording.** `VR&E` was first filed under a new `"c": "Military"`
category — and the acronym domain is generated *by category*, so one entry created a whole
`By Area — Military` topic and moved the site total to 1,406. `Government` already held
`DoD`, `DISA`, `NATO`, `NDAA`, `SCI` and `SF`: the same territory, fourteen entries deep.
Refiled, and the topic count went back to 1,405. **A category field in a generated
taxonomy is a structural decision, not a label** — worth a look at the neighbours before
inventing one.

Site total unchanged at **1,405**; dictionary 1,094 → **1,095** entries. Smoke **135/135** ·
axe **6/6** · visual **2/2**.


## Session record — six wrong acronym expansions, and the ratchet that closes the class

§4d ended by saying the ambiguous-acronym counter measures **exposure, not debt** — four
acronyms a future card could plausibly get wrong — and that all 49 annotations of them had
been checked by hand. That was true for the shape it checked: single-meaning entries whose
*note* mentions a second meaning. It said nothing about the other shape, which is the
common one: an entry with **several structured meanings**, an `annotate` default, and a
`byDomain` map covering some domains and not others.

Found while auditing `hw` for content gaps, in a **topic title**:

> Memory Deep — Channels, Ranks, Timings, **ECC (Elliptic Curve Cryptography)** & Diagnosing Bad RAM

The dictionary already knew Error-Correcting Code. `byDomain` had `linux` and not `hw`.

### Six, all live

| Acronym | Domain | Rendered as | Should be | The giveaway |
|---|---|---|---|---|
| `ECC` | `hw` | Elliptic Curve Cryptography | Error-Correcting Code | in the card title, beside "Diagnosing Bad RAM" |
| `DC` | `hw` | Domain Controller | Direct Current | "Watch out for **DC** voltage — is the rail present?" |
| `IPS` | `hw` | Intrusion Prevention System | In-Plane Switching | a table of *display panels*: "wide viewing angles, consistent colour" |
| `KVM` | `net` | Kernel-based Virtual Machine | Keyboard, Video, Mouse | "two PDUs… switches, appliances and the **KVM**" |
| `SSG` | `shortcut` | Static Site Generation | Staff Sergeant | "E-6 Staff Sergeant **SSG**" |
| `DORA` | `grc` | DevOps Research and Assessment | Digital Operational Resilience Act | "The Regulatory Landscape — **DORA**, NIS2 & Cyber Disclosure Rules" |

Two of the six needed a meaning the dictionary did not have at all (`Staff Sergeant`,
`Digital Operational Resilience Act`), so they could not have been fixed by an override
alone. A seventh was found in passing and is a different shape: **`PDU` rendered as
Protocol Data Unit in a rack-power sentence** — correct elsewhere in the same file, and
`byDomain` is per-domain, so no override can separate them. Fixed in the content by
spelling out "power distribution units", and the meaning added to the dictionary for the
reference domain.

`SSG` is worth one more line, because the fix is invisible: it is now **not annotated at
all**, and that is right. The annotator skips an expansion already spelled out within ~250
characters, and "Staff Sergeant" was three words to its left the whole time. The wrong
expansion was the only reason anything rendered.

### The ratchet

`byDomain` is now **exhaustive** rather than exceptional: **81 decisions**, one for every
domain where a multi-meaning acronym actually renders, including the 75 that only confirm
the default. `lint_content.py` errors on a rendering with no decision, naming the acronym,
the domain, what it would annotate as, and every meaning available — so a new card in a new
domain surfaces the choice once, before it ships. Verified by deleting `ECC`'s `hw` key:
one error, exit 1.

### The regex that audited itself

The first pass reported **28** uncovered pairs. The second reported **77** — and the
difference was not new content. The audit matched acronyms with a plain `\b`, so it was
finding `DP` inside `UDP`, `RA` inside `YARA` and `DORA`, `SCP` inside `OSCP`, `TS` inside
`HSTS`, and `MAC` inside `HMAC`. Roughly half of the first list was the regex looking at
itself.

That is the same failure as the `Viva`/"sur**viva**l" audit and the `POA&M` token split,
three sessions running: **a token boundary is not a word boundary when the tokens are
acronyms**, because acronyms are made of the same characters as the words they hide in. The
lookbehind `(?<![A-Za-z0-9])` is in the shipped check with the four false matches named
beside it.

Site total unchanged at **1,405**; dictionary 1,095 → **1,095** entries with three new
meanings. Smoke **135/135** · axe **6/6** · visual **2/2**.


## Session record — the `threat` wave: five attacks the site had never described

`threat` sat at 31 topics with a solid framework layer — kill chain, ATT&CK, Diamond,
threat intel, malware analysis, ransomware, supply chain, the criminal economy. The audit
probed **topic titles** for specific attack techniques rather than for frameworks, and the
zero-coverage list was startling for a security site:

```
business email      0     credential stuffing   0     watering hole   0
invoice fraud       0     password spray        0     drive-by        0
botnet              0     account takeover      0     malvertising    0
infostealer         0     MFA fatigue           0     SIM swap        0
```

Five cards, chosen so each one says something the site could not say before rather than
restating a taxonomy it already had.

**Business Email Compromise** — the framing is that every control in the stack looks for a
payload and there isn't one: no attachment, no link, no code, and the only indicator is a
sentence about urgency. So it consistently outranks ransomware in reported losses while
barely registering in security tooling, because it is a *payment process failure* that
arrives by email. Three delivery routes, and only the third matters — a genuinely
compromised mailbox replying inside a real thread, which authentication cannot touch, and
the card says plainly that a DMARC rollout is worth doing and is not a BEC control. The
inbox rule gets its own section because it is the whole trick and the best artefact in the
investigation: it hides the supplier's "we did not change our details" reply, and it
survives a password reset. The response section inverts the usual runbook — **call the bank
before touching the mailbox**, because the mailbox will still be compromised in an hour and
the money will not still be recoverable.

**MFA Bypass in Practice** — one sentence carries the card: *MFA authenticates a login, not
a session*. Everything current follows from that gap, so the techniques are ranked by how
much they care about your factors, with adversary-in-the-middle first. The relay diagram
makes the necessity visible: any factor whose proof is a value a human can read out and
type in can be relayed live by something in the middle, which is a property of the design
and not a bug to be patched. That puts phishing-resistant authentication in its own row —
not "stronger MFA" but the only category structurally immune, because the browser tells the
authenticator which origin is asking and it refuses to lie. The post-login sequence is
included because two of its six steps — registering a new factor, granting an application
consent — are what outlive the response, and are also the two most alertable events.

**Infostealers** — a business model disguised as a malware family. It runs once, takes
everything, deletes itself: no persistence, no beacon, no encryption event, and the only
surviving artefact is a file on someone else's server. The log contents table leads with
session cookies rather than passwords, because a cookie is a completed login with MFA
already satisfied, and includes the machine fingerprint row that explains why replayed
sessions do not trigger impossible-travel logic. The response section exists to correct one
ordering people get wrong under pressure: **revoke sessions before resetting the password**,
or the reset locks the door behind the intruder.

**Attack Infrastructure** — the layer under the techniques, and the reason infrastructure
indicators age better than file indicators: hosting and proxy pools are reused across
campaigns while payloads are not. Bulletproof hosting, residential proxies, fast flux,
domain generation, booter services — and the honest note that booters put denial-of-service
capability behind a card payment, which retires "who would bother attacking us" as a threat
model. The living-off-trusted-services section is the structural one: when command traffic
runs through a mainstream cloud service, blocklists, certificate scrutiny, reputation and
geography all fail simultaneously and correctly, which is the argument for detections built
on regularity and process lineage instead. Takedowns get a table that says plainly they are
a window, not a fix — and that the window is a good time to hunt.

**Watering Holes, Drive-Bys & Malvertising** — the delivery routes that need no message, and
the card opens by saying the thing an incident review needs to hear: *the absence of a
phishing email is not evidence of an insider or a lie*. The profiling-step diagram explains
why these are so hard to reproduce — the site looks clean when you check it because you are
not in the profile and have already been seen — which relocates the investigation to your
own proxy logs. It ends on the technique that has largely replaced browser exploitation:
the page puts a command on the clipboard and talks the user through pasting it, so nothing
is exploited, patching does not help, and the only tell is process lineage.

### Notes from the build

- The linter caught the one mistake, by name: a cross-reference to *Email Authentication —
  SPF, DKIM **&** DMARC* when the real title uses commas. It printed the correction.
- The `undecided_meanings` ratchet added an hour earlier stayed silent through five new
  security cards full of ambiguous acronyms — the first evidence that the 81 recorded
  decisions actually cover the domains content is written in.
- 17 bidirectional related-topic pairs, hand-picked again.

`threat` 31 → **36**. Site total 1,405 → **1,410**. Smoke **135/135** · axe **6/6** ·
visual **2/2** · gzip headroom 28%.


## Session record — `hw`: the two cards a hardware domain should not have been missing

A broad title probe across seven domains — testing for specific subjects rather than
frameworks — returned a mixed result worth recording, because **half the "gaps" were
phrasing misses**. `pentest` came back with zeros for "report writing" and "cloud pentest";
it has *Pentest Reporting – The Skill That Makes or Breaks Your Career* and *Cloud
Penetration Testing — What You May Test, and What You Are Actually Testing*. `math` came
back with zeros for statistics and linear algebra, which is correct and irrelevant: that
domain is a calculus course, not a mathematics library, and widening it would be a decision
about scope rather than a gap.

That leaves the probe useful only when the zero is checked against the domain's actual
title list. Doing that for `hw` left two that were genuinely absent, and both are core
material rather than exotica.

**Static, Handling & the Bench** — the card exists because the usual ESD briefing does not
survive contact with experience: everybody has handled memory carelessly and seen nothing
die, and that observation is true. The framing that works is the distinction between
destroying and **degrading**: a discharge you can feel is far more than a modern gate needs,
the ones below that threshold produce no symptom at all, and the resulting fault surfaces
weeks later as an intermittent that nobody attributes to the person who installed it. So "I
have never damaged anything" is evidence about attribution, not about practice.

The precautions are ranked rather than listed, because the ranking is the content: touching
the chassis and holding boards by the edges carry most of the value and cost nothing, a
wrist strap has to reach the same ground as the board, an antistatic bag shields on the
*outside* so a board resting on one is unprotected, and antistatic sprays and lead-less
bracelets are sold as protection and provide none. Then the honest note that the dangerous
moment is not the work — it is carrying the part across a carpeted office and setting it on
a plastic desk.

A second concept card says the thing the safety briefing never does: **more parts die on a
bench from force than from static**. Bent pins from a cold cooler twisted off an unlatched
socket, a cracked board from pressing a connector home unsupported, and the standoff in a
hole the board does not have — which shorts the underside and kills motherboards silently.

**Laptops — Batteries, Thermals & What Is Actually Replaceable** — organised around the
fact that every desktop-repair assumption is deliberately inverted, so *the diagnosis
matters more precisely because half the repairs are not economically available*. The
battery section corrects folklore that was true of nickel chemistry decades ago: deep
discharges accelerate lithium ageing rather than preventing memory effect, overcharging is
prevented in hardware so what ages a cell is sitting full and warm, and calibration re-syncs
the gauge without changing capacity. Swelling gets a red flag, because the visible symptom —
a trackpad that clicks oddly, a case that will not sit flat — arrives well before anything
dramatic.

The thermal section exists because "it got slow" is usually a cooling story, and it ends on
a measurement rather than a symptom: **log clock speed under sustained load**, since a
processor holding its clock at 95°C is fine and one dropping to a third of rated speed after
ninety seconds is not, and the difference is invisible from outside the chassis. The
repair-or-replace table closes on the row that changes the most outcomes — a machine that is
slow because of a mechanical drive and too little memory is under-specified rather than old,
and that is the repair most likely to be skipped because "slow" sounds like age.

### Two catches by the tooling, both by name

- A cross-reference to *Media Sanitisation & Disposal — What "Wiped" **Has to Mean**"* when
  the real title ends *"Actually Means"*. The linter printed the correction.
- `check_renames.py` rejected **"some vendors whitelist which cards will boot"** — house
  style is allowlist. Reworded to "will only boot cards from an approved list", which is
  better English anyway. That check has been in `make check` for many sessions and this is
  the first time it has caught something written in the same session.

`hw` 24 → **26**. Site total 1,410 → **1,412**. Smoke **135/135** · axe **6/6** · visual
**2/2**.


## Session record — `mind`: anxiety, motivation, and the card about getting help

`mind` had 17 topics covering the psychology of an IT career well — imposter syndrome,
burnout, on-call, layoffs, comparison, asking for help — and three gaps that a domain about
minds should not have. The audit also killed a fourth candidate before it was written:
ADHD-style working, because `productivity`'s *Study Systems That Survive a Brain That Won't
Cooperate* already carries "design for the bad day", the five structural moves, and body
doubling. Checking the concept-card titles inside the adjacent card, rather than only its
title, is what caught that.

**Anxiety — What Keeps It Going, and What Actually Shrinks It.** Opens by saying what it is
not: no diagnosis, no treatment plan, and the last section is the one that matters if things
are severe. Then two mechanisms.

The first is ordering: the threat response runs before the reasoning finishes, which is why
*knowing* a fear is disproportionate changes nothing in the moment. People conclude they are
irrational; they are experiencing a system working as designed on the wrong input. The
symptom table ends on the row worth sitting with — the dread arrives before a reason and the
mind supplies one afterwards, which is why arguing with the reason rarely helps and why the
same feeling attaches to a different worry next week.

The second is the one the card is built around: **avoidance is what keeps it alive**. Every
avoidance produces relief, and relief teaches two false things — that the situation was
dangerous, and that avoiding works. The diagram shows the circle getting smaller. Then the
term worth knowing, *safety behaviour*: the small thing that gets you through, which feels
like the reason you coped and is the reason the fear survived intact. The what-helps table
is ranked by evidence rather than appeal, and says plainly that graded approach and dropping
safety behaviours are the treatment while breathing, sleep and exercise are maintenance —
and that alcohol works for two hours and worsens tomorrow's baseline.

**Motivation — Why Waiting For It Fails.** The thesis is that motivation is largely a
consequence of engagement rather than a prerequisite, so treating it as a prerequisite
guarantees the wait. The card's real contribution is the diagnostic: **low motivation is a
symptom with four common causes** — depleted, unclear, powerless, misaligned — which want
completely different responses, and applying discipline to the first is how people arrive at
burnout. The question that separates them is what happens on a good day: if a rested
Saturday makes the task feel possible it is depletion or ambiguity; if it feels exactly as
unappealing, it is agency or alignment, and no technique addresses those. Then autonomy,
competence and relatedness as the conditions that actually produce sustained effort, with
willpower listed fourth and described as real, small, and the least reliable of the four.

**Getting Professional Help.** Written because the delay is real and the reasons are
practical rather than philosophical — not knowing what it involves, not knowing how to
start, and above all believing you are not struggling *enough*. The card argues with that
directly: there is no threshold, and "struggling enough" is a bar people set above wherever
they currently are, so it never gets cleared however bad things become. Then the routes in
(with the two facts people do not know: an employee assistance programme does not tell your
manager, and using a private session while on a public waiting list is normal), what modern
therapy actually involves — closer to structured problem-solving with homework than to the
version in films — and the objections answered plainly, including the career one, since
clinical records are separate from employment and clearance processes generally treat
seeking help as a positive.

It ends on the section for the reader who is not the one struggling: what to do when a
colleague tells you. Listen without solving, take it at face value, say what you can
actually do rather than "anything you need", and — if they mention harming themselves — ask
directly. **Asking does not plant the idea.** That myth is persistent and it stops people
asking the question that most often turns things.

### On writing this domain

These three are the most careful cards in the file, and the care shows in what they refuse
to do: no diagnosis, no promises, no technique offered where the honest answer is a
professional. The register the domain already had — practical, specific, unsentimental —
turned out to be exactly right for the subject, which is the argument for writing new
material *in* an established voice rather than adopting a new one for a sensitive topic.

9 bidirectional related pairs. `mind` 17 → **20**. Site total 1,412 → **1,415**.


## Session record — `philosophy` clears its own bar, with the three cards it was missing

§3's Phase-4 rule says a domain needs ≥15 cards to justify a chip. `philosophy` sat at 14 and
had been left there twice, on the reasonable grounds that it is a coherent subject rather
than a bag. This session added the three cards that make it clear the bar honestly — chosen
because they were genuinely absent, not to reach a number.

The domain's existing shape explains the gaps. It covers **traditions** thoroughly —
Stoicism, Buddhism, Taoism, Existentialism, Machiavelli, three earth-based practices — and
carries three short cards of folk wisdom and decision heuristics. What it had none of was
the machinery: how to reason about right action, how arguments work, and how you know
anything. For a reader who spends their working life debugging and evaluating claims, those
are the three most directly usable parts of the subject.

**Ethics — The Three Families.** Deliberately not framed as a contest with a winner, because
nobody reasons from a single theory and the framing is why most people find the subject
useless. Consequentialism, deontology and virtue ethics as **three questions to ask about
the same decision**, where disagreement between them is information: where all three agree
you did not need the framework, and where they conflict is where the hard cases are. Each
gets the case that makes it obviously right and the case that makes it obviously monstrous,
so the reader is not captured by whichever they read last. Contractualism is named as the
fourth because it is the one people already use without knowing it — *could I justify this
to everyone affected?*

The worked example is a disclosure decision with a ninety-day silence from a vendor whose
product is in hospitals, run through all four lenses. The point of the exercise is stated
plainly: the lenses do not deliver an answer, they generate the considerations you would
otherwise skip. Then three traps that look like ethical reasoning — "it's legal", "everyone
does it", "I only built the tool", "I have no choice" — and the habit worth more than
picking a theory: **noticing when you have switched lenses mid-argument**, arguing
consequences while they favour you and rights the moment they do not.

**Arguments & Fallacies.** Opens on validity versus soundness, and the case that matters is
the third one in the code block: every sentence true, and the conclusion still unearned.
"Which are you disputing — the structure or a premise?" ends a lot of circular
disagreements. Then deduction, induction and abduction with what each is entitled to, and
the honest note that **abduction is the one people mistake for proof** — "the deploy went out
at 14:00 and errors started at 14:02" is a good hypothesis and not a finding, which is how a
team spends a day rolling back an innocent release. The fallacy list skips the Latin in
favour of the nine that actually turn up in a design review, and ends by saying that
**naming a fallacy is not an argument either**. The last concept card is the one nobody
teaches: burden of proof, absence of evidence being weak evidence only *if you looked*, and
the single most useful question in a stuck technical argument — what would change your mind?

**How You Know.** Starts from an honest accounting: most of what anyone knows is testimony,
so the practical question is almost never "is this true" but "how much weight does this
source deserve on this subject". Confidence as a number rather than a mood, with the
discipline that makes it real — write it down *before* the outcome, because remembered
confidence is reliably revised. Then two failures that look like rigour and are worse than
credulity because they come with a sense of being the sceptic in the room: **isolated demand
for rigour** (the standard moved with the conclusion, so it is not a standard) and
**symmetric doubt** ("nobody really knows", which is a way of keeping your prior). It ends on
the four states of knowing, and on why imposter syndrome is so often a good sign: the
discomfort is what moving out of *not knowing that you do not know* feels like, and the
people who never feel it are frequently still there.

### Two self-caught mistakes

A cross-reference to a *Root Cause Analysis* card that does not exist — invented from
memory, checked against the title index before splicing, and replaced with the `script`
debugging card that actually carries the argument. And a stray
`<div class="topic-icon-none"></div>` written into the third card's header, which is the
second time in this file's history that an invented placeholder div has been typed out and
removed. Both were caught before the build; the first would have been caught by the linter,
the second by nothing.

`philosophy` 14 → **17**, above the ≥15 bar for the first time. 9 bidirectional related
pairs. Site total 1,415 → **1,418**.


## Session record — `data`: the three cards a database domain kept not being

`data` had 40 topics and read like an excellent database course: relational model, joins,
window functions, query plans, indexes, MVCC, six engines, backups, replication. What it
had almost nothing of was **data in motion** — the discipline that sits between the
production database and the warehouse, and where a data engineer actually spends the week.

The probe returned zero for `lineage`, `streaming`, `CDC` and `data contract`. Two nearby
cards were checked before writing rather than after: *Time-Series & Event Data* turned out
to be about **storing** time-indexed data (partitioning, downsampling), not moving it, and
*Data Quality & Observability* is the check list, not provenance. Both are ~1,300-character
single-concept cards from the domain's earlier style, so there was no overlap to manage.

**Streaming & Event Pipelines.** The model that makes these systems make sense is not a
queue — it is an **append-only log with a cursor per reader**, and stating that first
explains everything people find surprising: nothing is consumed, several teams read the same
events, a broken consumer rewinds, a slow reader falls behind instead of blocking. The
diagram carries the design decision that matters most, which is that ordering holds *within
a partition and nowhere else*, so the partition key is the ordering guarantee — pick a
random key for even distribution and "balance updated" can arrive before "account created".

Then delivery semantics, framed as where you put the work rather than as a dial: the
practical answer is **at-least-once plus an idempotent consumer**, because chasing
end-to-end exactly-once across a broker, a job and an external API means building
distributed transactions when an upsert would have done. Then the two clocks — event time
versus processing time — with the reason processing-time windows are trivial and wrong: *a
replay produces different numbers than the original run*, which makes the pipeline
unauditable. And a closing card on when not to stream, ending on the most common expensive
mistake in the area: building a streaming pipeline for a dashboard somebody reads once a
morning. The requirement was freshness, the answer was a schedule, and the project bought an
on-call rota.

**Change Data Capture.** Opens on the observation that makes it obvious in hindsight — the
database already keeps a durable ordered record of every committed change, because
replication depends on it, so read *that* rather than the tables. The comparison table's
load-bearing row is deletes: a timestamp-based load can never learn a row is gone, so
cancelled orders stay counted and the numbers drift upward forever in a way that looks like
growth.

The hard part gets its own card, because it is the part tutorials skip: **snapshot and stream
have to be joined at a known log position**, with no gap and a deliberate overlap, which is
why every CDC sink must be idempotent on purpose rather than defensively. Log retention is
called out as a real operational parameter — it sets how long a consumer may be broken before
recovery means re-snapshotting production on a Monday morning. And the card ends on the
coupling nobody warns about: CDC is operationally non-invasive and architecturally the
opposite, because it publishes the source system's internal schema to people the developer
has never met.

**Data Lineage & Contracts.** Framed by the two questions that consume a data team's week —
*where did this number come from* and *what breaks if I change this* — and the observation
that without lineage both are answered by whoever has been there longest, which is a
staffing dependency dressed as a knowledge one. Three grades of lineage with the honest
verdict that **automatically derived table-level beats hand-maintained column-level**,
because a lineage graph nobody trusts is worse than none: people check it, find it wrong
once, and stop.

Contracts are the half lineage cannot supply — lineage says what *is* connected, not what
anyone *promised* — with the clause the whole thing exists for (change policy) and the
enforcement point that decides whether it works at all: checked in the warehouse it is a
report that the damage happened; checked in the producer's build it stops the change. The
decay table then lands on a principle this file keeps arriving at from different directions:
**documentation not derived from the thing it documents will diverge from it**, invisibly,
until somebody relies on it. The success measure is deliberately unglamorous — how long it
takes to answer "where did this number come from" for a figure you did not build.

9 bidirectional related pairs. `data` 40 → **43**. Site total 1,418 → **1,421**. Smoke
**135/135** · axe **6/6** · visual **2/2**.


## Session record — `grc`: the register, the exception, and the board pack

`grc` had 45 topics and covered frameworks exhaustively — NIST CSF twice, ISO 27001, SOC 2,
PCI DSS, HIPAA, FedRAMP, GDPR, DORA — plus eight privacy-engineering cards. What it had none
of was **the three artefacts a GRC function actually produces**: the risk register, the
exception, and the report that goes upward. Frameworks describe what should exist; these are
what people spend their weeks writing.

**The Risk Register in Practice.** Existing cards cover the concepts — threat/vulnerability/
impact, the four treatments, three lines of defence. This one is about the document, and it
opens by naming the failure mode precisely: a register becomes a list of everything anyone
was ever uneasy about, scored once, owned by "IT", reviewed the week before an audit, and
correctly treated as a compliance artefact thereafter.

The centre of the card is that **the wording is the work**. "Cyber attack" is a category,
"No MFA" is a missing control that names the fix and hides the consequence, "Legacy systems"
is a condition. The sentence shape — *because of X there is a risk that Y resulting in Z* —
forces the missing information out, and the test is memorable: **can the entry be wrong?**
"Cyber attack" can never be closed and never be disproven, which is exactly why it survives
every review. Then the fields that earn their place (owner is a person, not a team; the
last-changed dates are the most diagnostic pair in the file), scoring honestly with the note
that **the point of scoring is ordering, not measurement**, and six checkable signs a
register has stopped working — ending on the unfashionable repair, which is to delete most
of it.

**Exceptions & Risk Acceptance.** Built on an inversion worth stating plainly: a policy with
no exception route is not stricter, it is *less enforced*, because the deviations happen
anyway and stop being recorded. Hence the line the card is proudest of — the exception
register is the most honest document in a security programme, because it describes the
organisation as it actually is, and is therefore the best thing to read in a new role.

The structural argument is about who approves. Security should **advise and never approve**,
because it does not carry the consequence and cannot trade it against the benefit that
motivated the request; when security approves, the business stops weighing the trade-off and
the security team ends up owning an outcome it never had authority to prevent. Then expiry
as the whole mechanism, with the mature and uncomfortable third option: if the blocker will
never clear, **change the policy** — eighty permanent exceptions are a standard describing an
aspiration. It closes by reading the register as a diagnostic, where "zero exceptions" means
the process is unusable rather than that the organisation is compliant.

**Reporting Security Upward.** The failure is specific: every number on the usual slide is
real and none of them supports a decision this audience can make. A board can approve money,
change policy, accept risk, or ask a question — it cannot tune a rule, and "alerts triaged"
is a staffing argument wearing a security costume. Four questions boards actually ask, with
what answers each, and the observation that **the fourth — what do you need from us — is the
one to build the pack around**: a report ending in three named decisions gets decisions, and
one ending in a summary gets thanked.

Then trend-and-target over single numbers, with the denominator warning (a metric improves
when the scope shrinks, which is the commonest way a security graph gets better), and
quantification without spurious precision — **ranges are more credible than point estimates,
not less**, and they protect the presenter, which is the asymmetry that makes people avoid
quantifying at all. It ends on reporting bad news as the real test of whether anything else
in the pack is believed, and on the through-line: a security report is not an account of your
activity, it is an input to somebody else's decision.

9 bidirectional related pairs. `grc` 45 → **48**. Site total 1,421 → **1,424**. Smoke
**135/135** · axe **6/6** · visual **2/2**.


## Session record — `ai`: hallucination and multimodal, the two gaps in a dense domain

`ai` was the hardest domain to find a gap in — 49 topics covering transformers, training
pipeline, inference internals, RAG, fine-tuning, agents, MLOps, governance, shadow AI and
acceptable use. Two things were genuinely missing, and the first is conspicuous.

**Hallucination had no card.** The word appears thirteen times across the domain's prose and
once as a table row inside a 1,491-character card that also covers guardrails *and* diffusion
models. For the single most-asked question about these systems, that is a gap.

The card refuses the framing that it is a defect. A model produces plausible continuations;
where the data supports a fact the plausible continuation is the true one, which is why any
of this works; where it does not, the model still produces a plausible continuation, because
that is the only thing it does. Two consequences explain why "just tell it not to make things
up" fails: there is no separate fact store to consult and no internal flag distinguishing
recall from construction, so it cannot report a difference that does not exist from the
inside — and **a fabricated citation is formatted exactly as carefully as a real one**,
because fluency was never conditional on truth.

Then six *shapes*, because lumping them together is why mitigations get chosen badly, and
the one flagged as most expensive for technical readers is the invented interface: a function
or flag that *should* exist given the naming conventions around it, so the reader's own
knowledge argues in its favour. The mitigation table is ranked with honest limits, and the
verdict is that the top two — retrieval, and mechanical verification — share a shape: **both
replace the model's memory with something checkable.** Everything below is a percentage
improvement on an unreliable process; those two change what the process is. The card ends on
a design frame (what does a wrong answer cost, and who finds out) and on measurement, where
the row that gets skipped is tracking refusal rate beside error rate — a change that halves
errors by refusing a third of questions has not improved the product, and only the pair shows
it.

**Multimodal Models.** Built on the implementation fact that predicts everything surprising:
the image becomes tokens in the same context as the text. So images consume context budget by
size, fine detail can be lost before reasoning starts, and **an instruction written inside an
image is just more tokens** — which is why it can be obeyed. The capability table draws the
useful boundary not between images and text but between interpretation and precision, with
counting called out for its own warning because the failure is so counter-intuitive: a model
that describes a complex scene in detail will still miscount the chairs in it.

The document section is the one with a real engineering consequence. Passing page images
often beats text extraction because layout survives — and introduces a failure the old
pipelines did not have: **no intermediate artefact to audit**. Traditional extraction failed
loudly and left evidence; a model reading a page fails quietly and leaves an answer. For
anything financial or contractual, keep something you can point at when asked where the
number came from, which is the same argument the `data` lineage card makes about pipelines
and is now cross-referenced to it.

### The linter, again, by name

Two invented cross-references, both plausible and both wrong: *Embeddings & RAG — Giving AI
**Long-Term Memory*** (actual: *Access to Your Own Data*) and *Prompt Injection – The "SQL
Injection" of the AI **Era*** (actual: *World*). Both were reconstructed from memory of the
domain rather than copied, and the linter named both with the correction. That is now five
xref corrections it has supplied in this session, all of the same kind: a title remembered
approximately.

7 bidirectional related pairs. `ai` 49 → **51**. Site total 1,424 → **1,426**. Smoke
**135/135** · axe **6/6** · visual **2/2**.


## Session record — `net`: three faults the domain could describe the tools for but not the fault

`net` is the largest domain after `script` and `sec` — 70 topics covering OSI, subnetting,
routing protocols, BGP, DNS four times over, wireless, firewalls, NAT, QoS, cabling, cutover
nights and the field toolkit. Three subjects returned zero, and all three are the *fault*
rather than the technology: the domain could describe the switch, the tunnel and the QoS
policy, and had no card on the loop, the black hole, or the one-way call.

**Spanning Tree.** Opens on the fact that makes a layer-2 loop different in kind rather than
degree: an IP packet has a time-to-live and a routing loop dies; **an Ethernet frame has no
such field**, so a broadcast in a loop is copied forever and the domain saturates in seconds.
The symptom table leads with the oldest diagnostic in the building — port lights solid rather
than blinking — and includes the one that matters operationally: you cannot reach the switch
to fix it, which is why out-of-band access exists.

The protocol section states what it actually does, which is *elect then block* rather than
detect and break, and names the trap: with every switch at default priority the tie breaks on
MAC address, so **the oldest switch in the building usually becomes root** — often a forgotten
access switch in a cupboard, with every path bending towards it. Then edge ports, and the
line the card is built to deliver: edge acceleration without BPDU guard is the single most
common spanning-tree misconfiguration, and the failure it produces is the first section of
the card. The diagnosis runs physical-first for longer than feels natural, because the
management path is part of the casualty, and ends on the step skipped once service returns —
finding out which protection was missing, since a loop is the network telling you exactly
that.

**MTU, Fragmentation & the Half-Loading Website.** Written around a symptom pattern
distinctive enough that recognising it once saves days: **small things work and large things
hang**. Ping succeeds, DNS resolves, the login page loads, the page with images stalls
halfway. Nothing times out cleanly and every connectivity test passes.

The mechanism is three outcomes when an oversized packet meets a narrower path, and the third
— the black hole — is the one caused deliberately: blocking ICMP wholesale as hardening
removes path MTU discovery, so the sender never learns and the connection hangs rather than
failing. The fault then appears months later on a different system and is never connected
back to that rule. The proof is a two-minute ping with the don't-fragment flag, with the
arithmetic spelled out because that is the part people get wrong, and the fixes are ranked
with the honest split: **clamping is the pragmatic answer and the ICMP rule is the real one**,
because a clamp only helps TCP. It closes with a line for a change checklist — after standing
up any tunnel, test with a large transfer rather than a ping, since ping proves reachability
and nothing about size.

**Voice & Real-Time Traffic.** The framing is that real-time traffic cares about different
numbers, and **a late packet is exactly as useless as a lost one**. That explains the
complaint the domain otherwise had no answer for: a link with plenty of spare bandwidth
carrying unusable calls, while the monitoring graph says nothing is wrong — because
five-minute averages are drawn to smooth out exactly the 200-millisecond windows where the
call breaks.

Then signalling versus media, which produces the fingerprint of the whole subject:
**one-way audio**, which is almost never the phones and almost always something in the path
treating the two directions of a media stream as unrelated. QoS gets the honest verdict that
marking is stripped or ignored across the internet, so for calls that leave your network
quality is bought rather than configured. And a closing argument for why voice is worth
caring about even without a phone system: it is the most sensitive instrument on the network,
detecting microbursts and marginal wireless long before anything else complains — when calls
degrade and nothing else has, the network changed and the calls noticed first.

9 bidirectional related pairs. `net` 70 → **73**. Site total 1,426 → **1,429**. Smoke
**135/135** · axe **6/6** · visual **2/2**.


## Session record — `web`: the craft cards, and an `ops` probe that found nothing

Two probes this round, and the negative one is worth recording first. **`ops` returned four
apparent gaps — change advisory, problem management, knowledge base, handover — and has all
four**, as *Incident vs Problem vs Change vs Request*, *Knowledge Management — KCS in
Practice*, and *Escalation — Functional vs Hierarchical, and Handing Over Without Losing
Context*. That domain is 76 topics and genuinely finished for now. Four zeros, four phrasing
misses, no work: the probe is a filter, never a finding.

`web` was the opposite. Its CSS coverage is layout and features — Grid, Flexbox, custom
properties, `:has()`, layers, design tokens — and it had nothing on the craft of making
something look deliberate, nothing on theming as a practice, and no card on forms at all,
which for the part of the web where users actually leave is a strange omission.

**Typography & Visual Hierarchy.** Built on a diagnosis rather than a style guide: amateur
design is usually not ugly, it is *undecided* — nine font sizes, margins picked by eye,
four greys that are almost the same. The eye detects near-misses and reads them as
carelessness. So the fix is constraint rather than taste, and the card is a set of
constraints: a ratio-based type scale to choose from and never between, a spacing scale used
everywhere, two or three text colours, one accent. The verdict singles out line length —
`max-width: 65ch` is one declaration and the most common damaging mistake in developer-built
pages. It ends on the squint test, which is the discipline in one action: squinting removes
detail and leaves hierarchy, and if the most prominent thing on the page is a border or a
stray bold label, the hierarchy is arguing with the content.

**Theming & Dark Mode.** The thesis is that dark mode is hard because of the *names*, not the
colours: `--grey-100` and `--light-border` are descriptions of appearance, so in a second
theme they are wrong or lying, and a codebase full of them cannot be themed without reading
every usage. Hence role names, and the retrofit test that is one grep — which is why "we will
add dark mode later" is a much larger promise than it sounds.

Then the mistake that produces most theming bugs: treating it as a boolean when there are
**three states**, and the `:not([data-theme="light"])` guard that is always missing from the
first attempt — without it a user who chose light gets dark after sunset when their OS
switches, which is a memorable afternoon. The flash gets its own card as a sequencing
problem with the inline pre-stylesheet script, including the `try/catch` (storage throws
outright in some privacy modes) and `color-scheme` (skip it and the scrollbars stay bright).
The what-breaks list is the same every time — shadows, pure black and white, saturated
accents, baked-in white in images, inline SVG, and contrast checked once in light mode and
never again.

**Forms.** Opens where the losses are: the form is where users leave, and the failures are
not aesthetic. The centre is validation *timing*, with a two-line policy that removes most
complaints — **blur to show, input to clear** — and the note that validating while typing
before the first blur is correct and feels like being interrupted mid-sentence. Then error
messages that say what would be valid rather than that this is not, the platform attributes
that are free quality (`autocomplete` named as the highest-value attribute on any form, and
a placeholder explicitly not a label), and the assumptions worth removing, each of which
rejects real people. It closes on long forms, where the highest-value single change is not
clearing the form on a failed submit — a user who loses twenty minutes of answers rarely
returns, and unlike everything else on the card it costs one decision rather than a redesign.

9 bidirectional related pairs. `web` 38 → **41**. Site total 1,429 → **1,432**. Smoke
**135/135** · axe **6/6** · visual **2/2**.


---

# Phase 7 — the next hundred cards

> **✅ CLOSED.** Every card in this phase is now built. The ordered first ten shipped, then
> the tracks were worked through to the end: **93 cards across all 15 tracks**, with **3
> candidates rejected** as duplicates of cards a neighbouring domain already held (the
> `script` dates card, the `career` contracting-admin card, and the `math` reading-the-question
> card — all recorded in *Rejected, with reasons* below, and in the closing session record).
> The site reached **1,512 topics**. The header said 96; the honest built count is 93, and the
> gap is the file correcting its own probe again — the recurring lesson of this whole phase.
>
> The original plan follows, unchanged for the record. Track tables now carry ✅ on every card
> that shipped; the three without a tick are the documented rejections.

> The live backlog emptied this session. §8's appendix is closed, §2's counters are settled,
> §4's content-age number is re-measured, and eleven domains took a wave. This phase
> replenishes the queue with **specified** work: every entry names the card, the domain, and
> **the argument it turns on**, so a future session can start writing without designing
> anything first. That is the standard §4–§7 set, and it is the only standard that has ever
> produced cards from this file.
>
> **96 cards across 15 tracks**, plus a rejected list so the same candidates are not
> re-argued. The heading is a round number and the count is the honest one — this file has
> corrected an overclaiming header once already, and is not going to introduce another.

## 0. How this list was made, and its measured error rate

Every entry below came from the same two-step method the last eleven waves used.

1. **Probe topic titles**, not prose, for a subject across all 30 domains.
2. **Check every zero against the domain's actual title list** before believing it.

Step 2 is not optional, and this round produced the number that proves it. Across eight
domains, 128 probe terms returned zero. Reading the title lists reduced those to the
genuinely uncovered:

| Domain | Probe zeros | Real gaps | Notes |
|---|---|---|---|
| `ops` | 11 | **0** | Change advisory, problem management, knowledge base and handover all exist under other titles. 76 topics, finished |
| `cs` | 17 | 5 | Graph traversal, memoisation and floating point are all covered inside broader cards |
| `linux` | 19 | 6 | Package management, permissions and boot each have two or three cards already |
| `career` | 13 | 3 | Negotiation, home labs, writing, speaking, consulting — all present |
| `eng` | 17 | 6 | One-to-ones, feedback, delegation, ladders and Conway's Law are all there |
| `threat` | 15 | **10** | The genuinely thin one, even after this session's five cards |
| `redteam` | 15 | 6 | Tooling is exhaustive; tradecraft between the tools is not |
| `hw` | 12 | 2 | Two of the zeros were cards written **this session** — "battery" missed "Batteries" |

**Roughly 60% of probe zeros are phrasing misses.** That last row is the one to remember:
the probe reported a gap for a card written an hour earlier, because the title used a plural.
A probe is a filter that produces candidates. The title list is what produces findings.

---

## Track CA — `threat`: the actors and the economy

`threat` is 36 topics and is still the thinnest of the security domains relative to its
subject. This session added the technique layer; what remains missing is **who** and **why**.

| Card | The argument it turns on |
|---|---|
| ✅ **State-Sponsored Operations — Different Objectives, Different Tradecraft** | Criminals optimise for money per hour and leave when it stops paying; state operations optimise for access and will spend a year being quiet. That single difference predicts everything else — dwell time, tooling investment, target selection, and why "we're not a target" is a claim about value to a *specific* sponsor rather than about size |
| ✅ **Attribution — How It Is Actually Done, and Why It Is Usually Wrong** | Attribution is an intelligence judgement with a confidence level, not a forensic result. Infrastructure, tooling, language and timezone are all cheap to fake and are faked deliberately. The useful question for a defender is never *who* — it is *what did they do*, which is actionable and does not require being right about a country |
| ✅ **The Extortion Economy — Double Extortion, Leak Sites &amp; the Payment Question** | Encryption stopped being the leverage; the leak site is. That is why good backups no longer end the incident, and why the decision to pay is a legal, insurance and reputational question with a technical input rather than a technical decision |
| ✅ **Ransomware Negotiation — What Actually Happens** | The negotiation is a business transaction run by people with a process, a price ladder and a reputation to protect. Knowing that changes the posture: it is not a hostage film, and the first hour's messages set the frame for everything after |
| ✅ **Dark-Web Markets &amp; Forums — What Is Sold, and What That Means for You** | Access, data and tooling are commodities with prices, and the prices tell you what you are worth to an attacker. This is also where your credentials appear before your incident does — the monitoring feed with the clearest action attached |
| ✅ **Zero-Days &amp; the Exploit Market — Who Buys, and What "Zero-Day" Costs** | A zero-day is an expensive, perishable asset, which is why almost nothing you defend against uses one. The operational conclusion is unfashionable and correct: patch the known, because the known is what is being used |
| ✅ **Disinformation &amp; Influence Operations — The Attack on the Decision, Not the System** | Nothing is compromised, and the outcome is still achieved. Worth a card because it is the threat class most technical readers have no model for, and because the defensive controls are editorial and procedural rather than technical |
| ✅ **Critical Infrastructure &amp; OT Threat — Why Consequence Changes Everything** | Availability outranks confidentiality, patching windows are measured in years, and an incident can hurt someone physically. Every instinct from IT security is either wrong or dangerously mistimed here |
| ✅ **Hacktivism &amp; Ideological Actors — Low Capability, High Publicity** | The technical bar is usually low and the reputational impact is not, which inverts the usual risk maths. Defacements and leaks are cheap; the response is a communications problem with a technical component |
| ✅ **Fraud &amp; Money Movement — Where the Money Actually Goes** | Every financially motivated intrusion ends in a payment rail, and the rails have controls, delays and reversal windows. Understanding the cash-out step explains why some attacks target odd systems, and where the intervention points are |

---

## Track CB — `redteam`: the tradecraft between the tools

52 topics, and it is a **tooling catalogue** — Nmap, Burp, Metasploit, Impacket, BloodHound,
Mimikatz, four C2 frameworks, Hashcat. What is missing is the craft that decides whether the
tools work, which is also the part that transfers when the tools change.

| Card | The argument it turns on |
|---|---|
| ✅ **Operator OPSEC — Not Being Caught Is Part of the Objective** | An engagement that is detected on day one still produces findings, and produces the *wrong* ones: you have tested the client's response to a noisy operator rather than to a realistic adversary. OPSEC is therefore a fidelity requirement, not vanity |
| ✅ **Payload Development &amp; Evasion — Why Signatures Stopped Mattering** | Modern detection is behavioural, so a novel binary is not the win it once was. What gets caught is the sequence of actions, which means evasion is about *what you do* rather than *what you send* — and that reframes the whole subject |
| ✅ **Phishing Infrastructure — Domains, Certificates, Categorisation &amp; Ageing** | The email is the easy part. The infrastructure — a domain with age and a category, a certificate, a redirector, a sending reputation — is the part with a lead time measured in weeks, and forgetting that is what makes an engagement slip |
| ✅ **Persistence — Choosing a Mechanism You Can Also Remove** | Every persistence choice is a promise to clean up. The mechanisms are ranked here by how reliably they can be removed and evidenced, because leaving a client with an artefact nobody documented is the failure mode that ends relationships |
| ✅ **Lateral Movement as a Decision, Not a Technique** | The tools are covered; the judgement is not. Each hop trades detection risk against objective progress, and the operators who get caught are usually the ones who moved because they could rather than because the objective required it |
| ✅ **The Engagement Debrief for a Hostile Room** | Some findings land in a room where somebody's decision is being criticised. Delivering those without losing the finding is a skill with a method — separate the system from the person, lead with what worked, and never present a finding the technical team has not already seen |

---

## Track CC — `blueteam`: the parts a detection programme runs on

54 topics, and the detection-engineering track is genuinely thorough. The gaps are the
*operational* surroundings: what happens to a detection after it fires, and the economics.

| Card | The argument it turns on |
|---|---|
| ✅ **Log Retention as a Design Decision** | Retention is chosen by cost and then discovered during an incident, always in that order. The right frame is: how far back must we be able to answer a question, and what is the cheapest tier that still answers it? |
| ✅ **Threat-Feed Reality — Why Most Indicators Are Worthless to You** | An indicator's value decays with time and rises with specificity to your environment. Most purchased feeds are neither timely nor specific, and the card's job is to give a reader the questions that separate a feed worth paying for from a list of hashes |
| ✅ **User &amp; Entity Behaviour Analytics — What Baselining Can and Cannot Learn** | A baseline built during an incident learns the incident as normal, and a baseline built on a small population learns nothing at all. UEBA works where behaviour is genuinely repetitive and fails politely everywhere else |
| ✅ **Analyst Burnout as a Detection Problem** | Alert volume is a design output, not a fact of nature, and turnover in a SOC is a measurable consequence of tuning decisions made months earlier. This is the card that connects §CC's engineering to the human cost of getting it wrong |
| ✅ **Shift Handover in a SOC** | The most information is lost at the moment it is most needed. A handover format that survives fatigue is a small artefact with an outsized effect, and it is the same problem `ops` solved for escalation |
| ✅ **SOC Metrics That Do Not Lie** | Mean time to detect is gameable by narrowing what counts as detected. The honest set measures coverage, dwell time and the alert-to-incident ratio — and each one is uncomfortable in a way the gameable ones are not |

---

## Track CD — `cloud`: the operating model, not the services

64 topics, and they are overwhelmingly **service documentation** — AWS this, GCP that, Azure
the other. The provider-neutral operating decisions are almost entirely absent, and they are
the part that transfers between providers and outlives any console.

| Card | The argument it turns on |
|---|---|
| ✅ **Multi-Cloud — The Four Reasons, and Which Ones Survive Contact** | Regulatory requirement, acquisition, deliberate best-of-breed, and fear of lock-in. Only the first two are usually real; the fourth buys an abstraction layer that costs more than the lock-in it avoids, and the card should say so plainly |
| ✅ **Exit Planning &amp; Lock-In — Pricing the Door Before You Need It** | Lock-in is not binary, it is a cost with a number. Compute is portable, managed data services are not, and the identity layer is the hardest of all. The exercise worth doing once is: what would it cost, in weeks, to leave? |
| ✅ **Tagging &amp; Cost Allocation — The Policy That Has to Be Enforced at Creation** | Retro-tagging never completes. A tag policy that is enforced at resource creation is the only kind that produces usable cost data, and this is one of the few governance controls where "block it" is genuinely the right answer |
| ✅ **Commitment Discounts — Reserved, Savings Plans &amp; the Forecast They Require** | A commitment is a bet on your own capacity forecast, and the discount is the premium for taking the risk off the provider. Buying them without a forecast is how organisations end up paying for capacity they stopped using |
| ✅ **Quotas &amp; Service Limits — The Outage That Is Not a Failure** | Nothing broke; you hit a number. Limits are per-account, per-region, silently different between them, and raising one takes a support ticket with a lead time. The card's job is to make this a pre-launch checklist item rather than a launch-night discovery |
| ✅ **Region Failover &amp; Cloud DR — What "Multi-Region" Actually Requires** | Data has gravity and consistency has a price. Most "multi-region" architectures are single-region with a cold copy, which is a legitimate choice and a different one — and the difference should be stated in the runbook rather than discovered during the event |
| ✅ **Data Residency &amp; Sovereignty — Where the Bytes Are, and Who Can Compel Them** | Two separate questions that get merged: *where is it stored* and *whose law reaches it*. The second is the one that surprises people, and it is not answered by choosing a region |

---

## Track CE — `devops`: the release factory

44 topics with strong pipeline and platform coverage. The gaps are the parts of the factory
that get blamed when delivery slows.

| Card | The argument it turns on |
|---|---|
| ✅ **Flaky Tests — A Reliability Problem in the Test Suite** | A suite that fails randomly teaches the team to re-run rather than to read, and once that habit forms the suite stops being a signal at all. Flakiness must be measured and quarantined with an owner and a date, or the test suite decays into ceremony |
| ✅ **Test Data — The Constraint That Shapes Every Environment** | Production data cannot be copied and synthetic data does not find real bugs. Every strategy is a trade between fidelity, privacy and refresh cost, and choosing one deliberately is what makes environments usable |
| ✅ **Ephemeral Environments — One Per Change, and What It Costs** | An environment per pull request removes the queue for the shared staging system, which is often the real bottleneck. It also requires that infrastructure and data can be created from code in minutes, which is why most teams cannot have it yet |
| ✅ **Monorepo vs Many Repos — The Trade Is About Coordination, Not Storage** | One repo makes cross-cutting changes atomic and makes tooling a full-time job. Many repos make each team independent and make a shared change a project. Pick the failure you can staff |
| ✅ **Build Caches &amp; Incremental Builds — Where the Minutes Actually Go** | Nobody optimises a build until it hurts, and by then the fix is architectural. The card gives the measurement first: which step, on which machine, on a cold cache and a warm one |
| ✅ **Release Notes &amp; Changelogs as an Interface** | A changelog is the API of your release process, read by support, security and customers. Generated from commits it is noise; written per user-visible change it is the cheapest support tool you own |

---

## Track CF — `eng`: the decisions, not the people

77 topics, and the people half is genuinely well covered — one-to-ones, feedback,
delegation, ladders, Conway's Law, managing up, calendars, planning. What is missing is the
**decision-making machinery** of a technical organisation.

| Card | The argument it turns on |
|---|---|
| ✅ **RFCs &amp; Design Docs — Writing to Decide, Not to Record** | A design doc written after the decision is documentation; one written before it is a decision-making tool, and the difference is whether anyone was ever able to change the outcome by reading it. Includes the failure mode: the doc that circulates for comment after the work has started |
| ✅ **Architecture Decision Records — The Format Whose Value Is the Rejected Options** | The decision matters less than the alternatives and the constraints that killed them, because in two years the constraints will have changed and only the ADR will say which ones they were |
| ✅ **Build vs Buy — The Question Behind the Question** | The comparison is never build cost against licence cost. It is *total* cost against *total* cost, including the maintenance you will owe forever and the exit you will eventually want — and the honest version usually turns on whether this is your differentiator |
| ✅ **The Staff Engineer Role — What It Is When It Is Not Management** | The individual-contributor track above senior is real and badly defined nearly everywhere. The card's job is to describe what the work actually is — scope, influence without authority, and the projects only this role can do — and what it is not |
| ✅ **Goals That Survive the Quarter — OKRs Without the Theatre** | Most goal frameworks fail the same way: outputs written as outcomes, targets set to be achievable, and a review that nobody attends. The fix is fewer goals, a measure that could go the wrong way, and a named person |
| ✅ **Measuring Developer Productivity Without Doing Harm** | Every individual metric in this space is gameable and most are actively harmful. What can be measured is the *system* — lead time, review latency, time to first commit for a new joiner — and the card should be blunt about why the individual version keeps being attempted |

---

## Track CG — `linux`: the cards for when it will not boot

58 topics and three cards each on permissions, packages and boot. What is missing is
**recovery** — the situations where the normal tools are not available.

| Card | The argument it turns on |
|---|---|
| ✅ **Rescuing a System That Will Not Boot — GRUB, initramfs &amp; the Chroot** | The recovery sequence is short and needs to be known cold, because it is used exactly when there is no time to look it up: boot media, mount, bind the pseudo-filesystems, chroot, fix, rebuild the initramfs, exit, unmount |
| ✅ **sudoers &amp; PAM — The Two Files That Decide Who You Are** | Authentication and authorisation are separate stacks that people conflate. A card that explains the PAM stack's order and the sudoers grammar prevents the two mistakes that lock everyone out of a box |
| ✅ **Journald, Logrotate &amp; the Disk That Filled With Logs** | Log retention on a single host is a configuration nobody sets until the disk is full at 3 a.m. Both mechanisms exist, they overlap confusingly, and the interaction is the part worth writing down |
| ✅ **Moving Data Safely — rsync, Its Flags, and the Trailing Slash** | One character changes whether you copy a directory or its contents, and the mistake is unrecoverable when combined with `--delete`. The card is a short one built entirely around the dry run |
| ✅ **strace &amp; ltrace — Watching a Program Ask the Kernel for Things** | When logs say nothing and the code is not yours, syscall tracing is the tool that answers "what file is it actually looking for". The subject is narrow, the payoff is a class of unsolvable problems becoming solvable |
| ✅ **Linux on the Desktop, and WSL — Two Different Answers to the Same Wish** | Worth one card because the audience keeps asking, and because the honest answer is about workflows rather than about Linux: the subsystem removes the dual-boot decision and imposes a filesystem boundary people trip over |

---

## Track CH — `cs`: the five primitives that are genuinely absent

56 topics and the strongest domain in the file. Almost every probe zero was covered inside a
broader card — graph traversal inside *Graphs*, memoisation inside *Divide & Conquer, Greedy,
Dynamic Programming*, floating point inside *Number Representation*. Five are real.

| Card | The argument it turns on |
|---|---|
| ✅ **Compression — Why It Works, and Why It Sometimes Cannot** | Compression exploits redundancy, so incompressible data is data with none — which is why encrypted and already-compressed files do not shrink, and why "compress then encrypt" is the only order that works. Includes the security note that compressing attacker-influenced data alongside secrets leaks length |
| ✅ **Consistent Hashing — Adding a Server Without Moving Everything** | Modulo-based sharding remaps nearly every key when the server count changes. The ring, and virtual nodes on top of it, is one of the small number of ideas that made horizontal scaling practical, and it recurs in caches, databases and load balancers |
| ✅ **Byte Order &amp; Binary Layout — Endianness, Alignment &amp; Struct Packing** | The bug class where the data parses and is wrong, which the `infra` mainframe card meets from the other end. This is the general version: the same bytes mean different numbers depending on who wrote them |
| ✅ **Catastrophic Backtracking — When a Regular Expression Is a Denial of Service** | A pattern with nested quantifiers can take exponential time on an input a user chooses. It is the rare bug that is simultaneously a performance problem, a security vulnerability, and invisible in code review unless you know the shape |
| ✅ **Little's Law &amp; Queueing — Why the Wait Explodes Before the Server Is Full** | Utilisation and latency are not linear, and the knee is much earlier than intuition says. One equation explains queue length, why running a system at 90% is a choice about latency, and why adding one more worker sometimes fixes everything |

---

## Track CI — `script`: the toolchain half

145 topics, the largest domain, and it teaches the *language* thoroughly. What it teaches
much less of is **the working environment around the code** — the part that decides whether
a script survives being handed to someone else.

| Card | The argument it turns on |
|---|---|
| ✅ **Type Hints &amp; a Type Checker — Documentation the Machine Verifies** | Hints that nothing checks are comments with better syntax. The value appears the moment a checker runs in CI, and the honest cost is the gradual-typing boundary where a large untyped codebase meets a typed edge |
| ✅ **pathlib &amp; the End of String Paths** | Path manipulation with string concatenation is a portability bug waiting for a Windows user. A short card, because the argument is short and the habit change is total |
| ✅ **subprocess Without Shell Injection** | The convenient form is the dangerous one. A list of arguments beats a shell string, and the card should show the exact case where interpolating a filename becomes remote code execution |
| ✅ **Threads, Processes &amp; async — Choosing by Where the Time Goes** | Three concurrency models and one question that picks between them: is the program waiting on I/O or burning processor? Everything else is detail, and getting this wrong is why "we added threads and it got slower" |
| ✅ **Packaging &amp; Dependency Pinning — Making It Installable by Someone Else** | The gap between "works on my machine" and "installs" is a project file and a lockfile. This is also the supply-chain surface, which connects to `eng`'s dependency-risk card |
| ✅ **Pre-Commit, Formatters &amp; Linters — Ending the Style Argument** | A formatter removes an entire category of review comment by making style non-negotiable and automatic. The card's argument is social rather than technical: the tool is valuable because it stops humans discussing whitespace |
| **Dates &amp; Times in Code — The Five Mistakes** | Naive datetimes, local-time arithmetic, storing offsets instead of zones, assuming days are 24 hours, and formatting for humans in a database. Pairs with the existing *Dates, Times & Time Zones* card, which covers the concepts rather than the code |

---

## Track CJ — `infra`: the physical estate

46 topics, and the Windows-server and storage coverage is deep. What is missing is
**everything that is not a server** — the room, the power, the labels, and the process for
keeping track of any of it.

| Card | The argument it turns on |
|---|---|
| ✅ **Failover Clustering — Quorum Is the Whole Subject** | Clusters do not fail because a node dies; they fail because the surviving nodes cannot agree that it did. Quorum, witnesses and split-brain are the content, and the card should say plainly that a two-node cluster without a witness is a coin toss |
| ✅ **The Rack, the Power &amp; the Cooling** | Dual feeds are pointless if a single-supply device is plugged into one of them, hot air recirculates without blanking panels, and floor loading is a real limit in older buildings. A card of physical constraints that software people meet exactly once |
| ✅ **Labelling &amp; Asset Tagging — The Boring Discipline That Pays Out at 3 a.m.** | Every recovery is faster in a room where the cables and devices are labelled, and nobody has ever regretted it. The argument is about when the cost is paid versus when the benefit lands |
| ✅ **Tape, Archive &amp; the Restore Nobody Has Tested** | Tape did not die, it became the offline copy in the ransomware playbook. Restore rate, media ageing and drive availability are the questions, and the last one strands more archives than the first two |
| ✅ **Decommissioning at Estate Scale** | The existing card covers one server. This is the programme version: finding what nobody owns, the notice period, the DNS entries and firewall rules that outlive the host, and the systems still pointing at it |
| ✅ **Patching a Server Estate — Windows, Rings &amp; the Ones That Cannot Reboot** | The endpoint domain has this for laptops. Servers are the harder case: dependency order, maintenance windows negotiated with a business, and the small population that will never be patched and needs a compensating control instead |

---

## Track CK — `endpoint`: the devices that are not laptops

41 topics, mostly Intune and MECM depth. The gaps are device *classes* the estate contains
and the documentation does not.

| Card | The argument it turns on |
|---|---|
| ✅ **Shared, Kiosk &amp; Frontline Devices** | Every assumption in endpoint management is about one device with one user. Shared devices break identity, compliance, licensing and the wipe path simultaneously, and each needs a separate answer |
| ✅ **BYOD in Practice — What You Can Actually Require** | The control surface on a device you do not own is small, legally constrained, and mostly about the *application* rather than the device. The card's job is to be honest about which controls survive the conversation with legal |
| ✅ **Virtual Desktops — When the Endpoint Is a Session** | Non-persistent desktops invert almost every management assumption: profiles, licensing, patching and troubleshooting all move, and the cost model is different enough that it should be chosen for a reason rather than as a default |
| ✅ **Browser Management — The Most-Used Application in the Estate** | Extensions, policy, profile sync and the sign-in boundary between work and personal identity. It is the single application every user runs all day and the one least often managed deliberately |
| ✅ **Application Compatibility &amp; the Legacy App** | Every estate has one application blocking an upgrade. The card is a decision tree — compatibility mode, virtualisation, isolation, containment, replacement — and the honest note that the last option is the only permanent one |
| ✅ **Lost, Stolen &amp; Returning Devices** | The wipe path, the data question, the licence release, and what happens when the device comes back six months later still enrolled. A short operational card that prevents a specific expensive mess |

---

## Track CL — `m365`: the workloads nobody documents

35 topics with excellent Exchange, SharePoint, Teams and Purview coverage. The gaps are the
second-tier workloads that arrive switched on, spread quietly, and are never governed.

| Card | The argument it turns on |
|---|---|
| ✅ **Power BI Governance — Workspaces, Datasets &amp; the Gateway Nobody Owns** | Reports proliferate faster than any other artefact in the suite, each embedding its own copy of a metric definition. The governance problem is the same one `data`'s semantic-layer card describes, arriving through a different door |
| ✅ **Viva &amp; the Employee-Experience Surface** | It is switched on by default, it surfaces analytics about people, and the privacy question is real. Worth a card mostly so somebody has made a deliberate decision about it, which `ops`'s surveillance-versus-monitoring card frames |
| ✅ **Forms, Bookings, Lists &amp; Whiteboard — The Small Apps and Their Data** | Each one creates records somewhere, each has a sharing default, and none appears in the retention conversation. A single card covering "where does this actually store things" for four apps people use without asking |
| ✅ **Defender for Office in Depth — Policy Order &amp; Why a Message Got Through** | The existing card introduces it. This is the operational half: which policy applied, in what order, and how to prove it from the message trace — the question every mail administrator is asked and few can answer quickly |
| ✅ **Exchange Hybrid — The Coexistence Nobody Meant to Keep** | Hybrid is a migration state that becomes permanent, and the last mailbox on-premises costs more than the previous thousand. The card should name the exit condition, because nobody plans one |

---

## Track CM — `productivity`: the systems half

16 topics, and they are all **learning science** — retrieval practice, interleaving, spacing,
deliberate practice, sleep, attention, procrastination. Excellent, and it means the domain
has almost nothing about *managing work*, which is the other half of what its title promises.

| Card | The argument it turns on |
|---|---|
| ✅ **The Inbox — Why It Is Not a To-Do List, and What Replaces It** | An inbox sorts by arrival, which is the one ordering guaranteed not to match importance. Every workable system separates capture from decision from action, and the mechanism matters less than that separation existing |
| ✅ **The Weekly Review — The Habit That Makes Every Other System Work** | Any capture system degrades into a graveyard without a scheduled moment to re-read it. The review is what converts a list into a plan, and it is the first thing dropped when busy — which is precisely when it pays most |
| ✅ **Time Blocking &amp; Its Failure Modes** | Deciding when something happens converts an open-ended list into a finite day, which is honest and uncomfortable. The failure is over-scheduling: a plan with no slack survives the first interruption and then gets abandoned |
| ✅ **Focus Blocks — Making Uninterrupted Time Possible in an Interrupt-Driven Job** | The existing *Attention* card covers what switching costs. This is the operational answer for someone on a rota: negotiating coverage, the shape of a realistic block, and why "I'll focus when it's quiet" never arrives |
| ✅ **Notes That Get Reopened — Structure, Linking &amp; the Search Test** | The existing note-taking card is about learning. This is about the reference pile: if you cannot find it in ten seconds it does not exist, which makes search behaviour the design constraint rather than folder structure |
| ✅ **Goals, and the Difference Between a Goal and a Wish** | A goal names an outcome, a date, and the first action. Anything missing one of the three is a wish, and the card's value is that this test is applied in ten seconds to anything already written down |

---

## Track CN — `sec`: the programme cards

86 topics, the second largest domain, and it is strongest on *technique*. The gaps are the
cards about running security as an ongoing function rather than as a set of controls.

| Card | The argument it turns on |
|---|---|
| ✅ **Asset Discovery — You Cannot Protect What Nobody Listed** | Every control's coverage is a fraction with an unknown denominator until the estate is enumerated, and the enumeration is always wrong in the same direction. This is the card that makes every other coverage metric meaningful |
| ✅ **Vulnerability Prioritisation — Severity Is Not Priority** | A high-severity finding on an isolated internal host loses to a medium on an internet-facing one, every time. Exploitability, exposure and asset value are the multipliers, and the card should name the specific published sources that carry them |
| ✅ **Shadow IT — Finding It Without Making It Worse** | Unsanctioned tools exist because a sanctioned one was missing or slow. Discovery is easy and the response is the whole subject: a blocked service returns as an unmanaged one, so the sanctioned path has to be genuinely better |
| ✅ **Break-Glass Accounts — The Ones That Must Work When Everything Else Does Not** | Excluded from conditional access, credentials split and sealed, monitored on use, and tested on a schedule. Every organisation has them, almost none tests them, and the day they are needed is the day the identity provider is down |
| ✅ **Code Signing &amp; the Key That Cannot Leak** | A signing key is a trust anchor with a blast radius the size of your install base. The card covers where the key lives, who can invoke it, and why build-time signing in a pipeline needs the same treatment as a production credential |
| ✅ **Security Champions — Making the Team Larger Than the Team** | A security function is always outnumbered by engineers, so influence scales and headcount does not. The programme works when champions get something real — early access, training, time — and fails when it is a title with meetings attached |

---

## Track CO — the singles

Domains needing one or two cards rather than a track. Each verified against the domain's
actual title list.

| Domain | Card | The argument |
|---|---|---|
| `hw` | ✅ **Warranty, RMA &amp; the Refurbished Question** | The commercial half of hardware: what a warranty actually covers, how an advance replacement changes downtime, and when refurbished is a good decision rather than a cheap one |
| `hw` | ✅ **Labels, Cables &amp; the Toolkit for the Bench** | Complements the new handling card with the consumables and the cable-management practice that decides whether the next person can work on it |
| `career` | ✅ **Asking for a Raise — The Case, Not the Conversation** | The existing card covers a first offer. A raise inside a company is a different exercise: it is a written case about market and contribution, delivered before the budget cycle rather than during a review |
| `career` | **Contracting Admin — Invoicing, Tax, Insurance &amp; the Boring Protections** | The consulting track covers pricing, proposals and scope. This is the machinery underneath, which is where independents actually get hurt |
| `ops` | ✅ **Compliance Evidence as an Operational Output** | Auditors want proof a control ran, not a description of it. Designing the evidence at the same time as the control converts an annual scramble into a byproduct — and this is `grc`'s audit card seen from the operations side |
| `military` | ✅ **Transitioning Out — The Timeline, and What to Start When** | The domain has GI Bill and résumé-translation cards. This is the calendar version, because the decisions with the longest lead times are the ones people make last |
| `math` | **Reading the Question — Where Marks Are Lost That Are Not About Maths** | The domain is a calculus course, so this stays in scope: the marks lost to misread instructions, unstated units and unshown working, which is a different failure from not knowing the material |
| `quotes` | ✅ **Sourcing a Quotation — Finding the Original, and the Ones That Are Not Real** | Five topics and the domain's own thesis is that an unsourced quote is a rumour with good grammar. The method card is missing: how to actually chase an attribution to a primary source, and the tells of a fabricated one |

---

## Ordering — the first ten, and why in this order

Not a priority list of importance. A sequence chosen so each session is startable in one
sitting and the early ones re-establish the method.

| # | Card | Why here |
|---|---|---|
| ✅ 1 | `cs` **Little's Law &amp; Queueing** | Self-contained, one equation, and it explains three existing cards from underneath |
| ✅ 2 | `threat` **State-Sponsored Operations** | The thinnest domain relative to its subject, and the card that anchors the rest of Track CA |
| ✅ 3 | `sec` **Asset Discovery** | Every coverage metric elsewhere depends on it; writing it first makes later cards able to reference it |
| ✅ 4 | `cloud` **Multi-Cloud — The Four Reasons** | The most-asked question in the domain and the one with the least written down |
| ✅ 5 | `linux` **Rescuing a System That Will Not Boot** | Short, high-value, and the kind of card people return to |
| ✅ 6 | `eng` **RFCs &amp; Design Docs** | Unlocks Track CF, since the ADR and build-vs-buy cards both reference it |
| ✅ 7 | `productivity` **The Weekly Review** | The smallest card that makes the rest of Track CM coherent |
| ✅ 8 | `redteam` **Operator OPSEC** | Reframes the whole tooling catalogue that already exists |
| ✅ 9 | `script` **subprocess Without Shell Injection** | One clear security lesson, short, and overdue in the largest domain |
| ✅ 10 | `blueteam` **SOC Metrics That Do Not Lie** | Pairs with `grc`'s new board-reporting card, and the two should cross-reference |

**✅ All ten shipped. Site 1,420 → 1,430.** See the session record at the end of this file.

**After ten, re-run the audit rather than continuing down the list.** Eleven waves shipped
this session and the site moved from 1,401 to 1,432 topics; a list written today describes a
site that will have changed by the time it is half-built. The list is a starting point with a
shelf life, and the method that produced it is the durable part.

---

## Rejected, with reasons

Recorded so they do not have to be re-argued.

| Candidate | Verdict |
|---|---|
| `math`: statistics, linear algebra, graph theory | **Rejected.** The domain is a specific calculus course, not a mathematics library. `cs` already carries probability, distributions, matrices and Bayes for the technical reader |
| `ai`: model-selection and benchmark cards | **Rejected as written.** Anything naming specific models or prices is stale within months, and the site has no mechanism to keep it true. The durable version is mechanism, which the new hallucination card covers |
| `web`: animation and motion | **Deferred, not rejected.** Real, but thinner than the three shipped this round. Fold the `prefers-reduced-motion` point into the accessibility remediation card if it does not get its own |
| `pentest`: API testing | **Rejected again.** Killed once already for duplicating five `sec` cards. The finding stands |
| `endpoint`: ChromeOS, thin clients | **Rejected.** Genuinely narrow, and the virtual-desktop card covers the operating model that matters |
| `sec`: TPM as its own card | **Rejected.** Covered by `linux`'s measured-boot card and `endpoint`'s BitLocker card from both ends |
| `blueteam`: malware detonation | **Rejected.** *Malware Sandboxes — VirusTotal, Any.Run & Hybrid Analysis* already exists |
| Anything about this site's own architecture | **Rejected permanently.** It is a study site, not a case study. The engineering record belongs in this file |
| `script`: *Dates & Times in Code — The Five Mistakes* | **Rejected (built-out duplicate).** *Dates & Times — Trickier Than You Think* already teaches UTC storage, timezone-aware datetimes, `strftime`/`strptime` and the naive-datetime trap. The five mistakes *are* that card. The spec paired it with the concept card and missed that the code card already existed |
| `career`: *Contracting Admin — Invoicing, Tax, Insurance & the Boring Protections* | **Rejected (built-out duplicate).** The consulting track already carries *The Business Side — Cash Flow, Contracts & the Boring Protections That Matter* — same machinery, same phrase |
| `math`: *Reading the Question — Where Marks Are Lost That Are Not About Maths* | **Rejected (built-out duplicate).** *Chapter Tests & the Final — Where the Marks Actually Go* already covers answering the wrong question, units, degree-mode and showing working — the whole of the proposed card |

---

## Session record — two more wrong expansions, found by the audit rather than by a check

Building Phase 7 meant reading every domain's title list, and two titles were wrong in a way
no check could see.

> `cs`: **How a Compiler Works — Lexing, Parsing, IR (Incident Response) & Codegen**

`IR` was a **single-meaning** dictionary entry — "Incident Response", category Security — so
`undecided_meanings`, added earlier this session, could not look at it: that check only asks
about entries with several meanings. And `ambiguous_acronyms` only asks about entries whose
note says "also". IR's entry had no note at all. Three renderings were wrong:

| Where | Rendered | Should be |
|---|---|---|
| `cs` — a compiler card's **title** | Incident Response | Intermediate Representation |
| `pentest` — "Sub-GHz, RFID, NFC, **IR**, BadUSB" | Incident Response | Infrared |
| `redteam` — a row literally headed *Infrared* | Incident Response | Infrared |

The `redteam` one is the tell: the correct expansion was three words to the left in the same
table row, and the annotator wrote the wrong one anyway. After the fix it renders nothing
there at all, which is right — the annotator skips an expansion already spelled out nearby,
so the wrong meaning was the only reason anything appeared.

A second, found the same way:

> `blueteam`: "A common home-lab / **SMB (Server Message Block)** choice"

That is Small and Medium Business. Same shape, same reason the checks were silent.

### The check that now exists, and what it can and cannot do

There is no rule that catches these, because **the dictionary does not know the second
meaning exists**. Nothing in the data distinguishes a term that genuinely means one thing
from one that has been borrowed somewhere and never recorded.

What correlates is **breadth**. An acronym a single subject owns tends to stay in that
subject; one rendered across many unrelated domains has usually been borrowed by one of
them. `IR` rendered in eight domains, `SMB` in seven. So `lint_content.py` now prints the
single-meaning acronyms rendered in six or more domains, widest first — 60 of them, led by
`API` at 21 domains and `IP` at 21 — as **a census to read, not a gate to pass**. Every entry
on it is probably fine; the two that were not would both have been on it.

That is a weaker instrument than the multi-meaning ratchet and it is the honest limit of
what is checkable here. Recorded plainly because the temptation with a census is to describe
it as a check.

`IR` and `SMB` are now multi-meaning entries with exhaustive `byDomain` maps, which brings
them under the ratchet: **83 recorded decisions**, up from 81. Site total unchanged at
**1,432**. Smoke **135/135** · axe **6/6** · visual **2/2**.


---

## Session record — Phase 7 closed, and three duplicates the probe did not catch

The remaining **46 cards** of Phase 7 shipped this session, across all fifteen tracks, taking
the site **1,466 → 1,512 topics**. The full-track writes: `threat` (9 — the actors and the
economy), `redteam` (5 — the tradecraft between the tools), `blueteam` (5), `cloud` (6 — the
provider-neutral operating model), `endpoint` (6 — the device classes that are not laptops),
`m365` (5 — the workloads nobody governs), and the singletons in `eng`, `script`, `infra`,
`productivity`, `hw` (×2), `career`, `ops`, `military` and `quotes`.

**Three candidates were rejected**, every one for the reason this phase keeps rediscovering:
the probe named a gap a neighbouring card already filled, and reading the target's actual
content — not its title — settled it. They are in *Rejected, with reasons* above:

- `script` **Dates & Times in Code** — *Dates & Times — Trickier Than You Think* is already the
  code card: UTC storage, timezone-aware datetimes, `strftime`, the naive-datetime trap.
- `career` **Contracting Admin** — *The Business Side — Cash Flow, Contracts & the Boring
  Protections That Matter* already carries the machinery underneath, phrase and all.
- `math` **Reading the Question** — *Chapter Tests & the Final — Where the Marks Actually Go*
  already covers answering the wrong question, units, degree-mode and showing working.

### A fourth correction, and the verification lesson behind it

`blueteam` **SOC Metrics That Do Not Lie** was on the Track-CC list as unbuilt. It was not — it
shipped in the ordered first ten. A duplicate got written and then **caught by the
slug-collision linter**, not by the plan. The cause is worth recording: the pre-flight check
that produced the CC list matched card titles with a regex that stopped at the first
annotated acronym, so `SOC <span…>(Security Operations Center)</span> Metrics That Do Not Lie`
read as `SOC`, and the card looked absent. **Verify a card's existence against its slug or its
de-annotated title, never against a naive `topic-name` match** — the same acronym-truncation
trap the title census was built to watch, arriving through the tooling this time. The linter
did exactly the job the *card rubric* claims for it: it caught the invented duplicate the
moment it was built.

The header specified 96; the honest built count is **93**. The gap is three documented
rejections, which is the file correcting its own probe once more — the single most repeated
lesson of Phase 7, now closing it as it opened it.

`make check` green across every static gate; determinism reproducible; page budget **15% raw /
16% gzip headroom**. Smoke **120/120** · axe **6/6** · visual **2/2**.


---

# Phase 8 — the depth problem, measured

Phase 7 asks what is missing. This asks a question the file has never asked: **how good is
what is already there?** The answer is uncomfortable and it is the most useful number in this
document.

## 1. The measurement

Every topic on the site, measured by plain-text length with markup stripped, and by how many
`.concept-card` blocks it contains.

```
concept-cards per topic, site-wide (1,432 topics)
  0 cards:     6      ← malformed or reference-only
  1 card:    470      ← the early style
  2 cards:   189
  3 cards:   409      ← the current style
  4 cards:   252
  5 cards:    75
  6+ cards:   31
```

**330 topics — 23% of the site — have a single concept card *and* fewer than 1,800 plain
characters.** Excluding the 22 in the generated `acronym` domain, **308 are hand-written**.
Sampling twenty of them at random returned twenty of the same shape: one concept card, one
reference table, one closing sentence. Not bad cards. *Early* cards, written before the
current form existed.

## 2. Where it is concentrated

| Domain | Thin | % of domain | Reading |
|---|---|---|---|
| `data` | 40 | **93%** thin by length | Written as a database course in one early pass, and almost untouched since |
| `web` | 35 | 85% | Same, plus six deep cards added this session that drag the mean up and leave the median at 1,415 |
| `redteam` | 40 | 77% | A tooling catalogue. Each tool got a paragraph and a table |
| `blueteam` | 36 | 67% | Same shape for the first 37; the detection-engineering track added later is deep |
| `cloud` | 40 | 62% | Service documentation, three providers, one card each |
| `shortcut` | 20 | 62% | Reference domain — **legitimately short**, see §4 |
| `devops` | 20 | 45% | The platform-engineering track is deep; the original tool cards are not |
| `eng` | 33 | 43% | The management track is deep; the early technical cards are not |
| `cs`, `infra`, `hw`, `m365`, `math` | 0 | 0% | Written entirely in the current style |

The pattern is chronological, not topical. **Domains written early are thin; domains and
tracks written after the form settled are not.** Nothing was done badly — the house style
changed and nobody went back.

## 3. Why this outranks Phase 7

A new card costs a permalink, a related-topics entry, an entry in every learning path that
should mention it, and a slot in a reader's attention. A deepened card costs none of those:
the id already exists, the links already point at it, search already finds it, and a reader
who bookmarked it gets more for free.

| | New card | Deepened card |
|---|---|---|
| Permalink | New id, new alias risk | Unchanged |
| Related map | Needs 2–3 new bidirectional pairs | Already wired |
| Learning paths | May need inserting | Already placed |
| Reader who already found it | Has to find it | Gets more, silently |
| Page budget | Adds a topic to the index and the search payload | Adds bytes only |
| Risk of duplication | Real, and the audit exists to manage it | **Zero** |

That last row is the argument. Every new card carries a duplication risk that costs an audit
to manage; deepening carries none, because the subject is already claimed.

## 4. What is legitimately short, and must be left alone

Not every short card is thin. Three populations are correct as they are, and a deepening
pass that does not exclude them will do damage.

| Population | Why it is fine |
|---|---|
| `shortcut` — keyboard and command references | The entire value is that it is scannable. Prose would ruin it |
| `acronym` — the generated domain | Emitted from `data/acronyms.json`. Editing the output is a bug, not an improvement |
| Genuine one-idea cards | Some subjects are one table. *Common Ports*, *RAID Levels*, *Beep Codes* — a verdict sentence is the most they need |

**The test for whether a short card is thin:** can you name, in one sentence, an argument the
card is making that the table does not already state? If no, it is a reference card and it is
finished. If yes, that sentence is the missing concept card.

## 5. The deepening pass, specified

Not a rewrite. A card is deepened by adding what the current form has and the early form
did not, in this order — and stopping at whichever step runs out of genuine material.

| Step | Add | Test that it earned its place |
|---|---|---|
| 1 | **A verdict** on the existing table | Says what the table *means*, not what it contains. If it restates a row, delete it |
| 2 | **The failure mode** | What goes wrong with this in practice, and what it looks like from outside |
| 3 | **The decision** | When you would choose this over the alternative, and what you give up |
| 4 | **The trap** | The thing that is true and surprising — the reason a reader would send this card to a colleague |
| 5 | Cross-references | Two or three, to cards that genuinely continue the argument |

A card that reaches step 3 is done. **Steps 4 and 5 are what make it worth reading twice**,
and a card with nothing to say at step 4 should stop at three rather than pad.

## 6. The queue, by leverage

Ordered by how much the domain's readers gain per hour of work — which is thin count
weighted by how central the domain is to why anyone visits.

| Wave | Domain | Cards | Why this position |
|---|---|---|---|
| ✅ **D1** | `data` | ~~40~~ → **32** | Worst ratio on the site, and the subject rewards depth. **Eight shipped** — the W4 spec's exact list. 93% thin → 74% |
| ✅ **D2** | `redteam` | ~~40~~ → **32** | The tooling catalogue is the domain's identity. **Eight shipped**, all with the same addition: *what it leaves behind* and *what the defender sees*. 77% thin → 62% |
| ✅ **D3** | `cloud` | ~~40~~ → **32** | Three providers, one card each. **Eight shipped**, all provider-neutral: the failure mode that is the same on all three. 63% thin → 50% |
| ✅ **D4** | `blueteam` | ~~36~~ → **28** | The first 37 cards predate the detection-engineering track that follows them. **Eight shipped**, all with the same addition: *what this tool cannot see, and what you pair it with*. 67% thin → 52% |
| ✅ **D5** | `web` | ~~35~~ → **27** | Median 1,415 against a mean of 2,622 — the clearest bimodal domain in the file, and it is bimodal because of *where it was written*. **Eight shipped**, each naming an instrument. 85% thin → 66% |
| ✅ **D6** | `eng` | ~~33~~ → **25** | The architecture cards sat beside a management track that had no choice but to be about trade-offs. **Eight shipped**, each naming a bill and a threshold. 43% thin → 32% |
| ✅ **D7** | `devops` | ~~20~~ → **12** | Platform track deep, tool cards thin. **Eight shipped**, each on day two rather than day one. 47% thin → 28% |
| — | `shortcut` | 20 | **Excluded.** Reference domain, see §4 |

**244 cards across seven waves**, before counting the tail in `script`, `linux` and `ops`.

**Status: all seven waves shipped — 56 cards, 288 thin → 231.** The queue as written is
finished; the remaining 231 are the tail this table deliberately did not name, and they need
a fresh census before anyone writes a wave D8. See the closing record for what that census
should ask.

### The D4 spec — written before the cards, like D1's, D2's and D3's

`blueteam`'s thin cards share one structural gap and it is the mirror image of `redteam`'s.
The offensive catalogue documented what a tool does and never what using it costs; the
defensive catalogue documents what a tool **sees** and never what it **misses**. That gap is
worse on this side, because a list of capabilities with no coverage gaps produces exactly the
failure the domain exists to prevent: believing you have visibility you do not have.

So the D4 addition is uniform, one card per topic:

> **What this tool cannot see, and what you pair it with to cover the gap.**

Three tests a D4 addition has to pass, all of which failed at least once while drafting:

| Test | Why |
|---|---|
| The blind spot must be **structural**, not a configuration mistake | "You forgot to enable it" is a checklist item. "It sits at the perimeter and lateral movement never crosses the perimeter" is a property of where the sensor is |
| It must name **what covers the gap** | A blind spot with no pairing is discouragement. The point is a defender who now knows which second source to go add |
| It must not be **the same blind spot eight times** | "Encrypted traffic" is true of three network tools and would be lazy on the other five. If two cards want the same sentence, one of them is the wrong card to deepen |

Eight chosen for the wave, each with a blind spot of a different *kind* — placement, retention,
acquisition, translation, attribution, coverage-by-selection:

| Card | The kind of blindness |
|---|---|
| Zeek | Placement — a sensor sees what crosses it, and less crosses it every year |
| Wireshark | Retroactivity — it cannot analyse a capture nobody took |
| Suricata & Snort | Prior knowledge — a signature is a description of something already named |
| Windows Event Logs | Retention and defaults — the event you need is off, or already rolled over |
| auditd | Attribution — syscalls are not intent, and containers muddy whose syscall it was |
| Volatility | Acquisition — memory is gone the moment the machine is |
| Sigma | Translation — portable rule, non-portable field names |
| Honeypots | Selection — deception is silent against an attacker who does not look |

### The D5 spec — the domain where the author's machine is the problem

`web` is bimodal because of *where it was written*. Every thin card in the domain describes a
feature correctly, from a fast laptop, on a fast network, in the current version of one
browser, with no assistive technology attached and the dev server running on `localhost`. The
deep cards in the same domain are the ones that eventually met a real user. That difference is
the entire gap, and it is measurable rather than stylistic.

So the D5 addition is:

> **The number your own machine cannot show you** — what this looks like on the device the
> user actually has, and the specific way to go measure it.

The measurement clause is not optional. A card that says "it's slower on phones" is the
padding this phase exists to avoid; a card that says *4× CPU throttle, Performance panel,
16.7 ms per frame* hands the reader something to do this afternoon. **Every D5 addition must
name an instrument, a setting, or a threshold.**

| Card | The environment gap |
|---|---|
| Reflow & Jank | CPU — the median phone is several times slower than the machine the code was written on |
| Web Storage | Policy — the browser can refuse or evict, and two of the three APIs have no quota you control |
| Core Web Vitals | Lab vs field — Lighthouse is a simulation of one load; the field number is a p75 across real ones |
| Fetch, REST & CORS | Origin — the dev proxy makes everything same-origin, so the preflight never happens until production |
| Modules & Bundlers | Parse cost — bytes are what you measure and CPU time is what the user feels |
| Responsive Design | Device vs viewport — DevTools device mode resizes a window; it does not give you a finger |
| Accessibility | Automated vs human — a clean automated scan is the floor, and this repo's own 6/6 is exactly that |
| Frontend Testing | Latency — `localhost` has none, and CI flake is usually the test discovering that |

### The D6 spec — every pattern sends a bill, and most cards only print the benefit

`eng`'s management track reads well because management writing has no choice but to be about
trade-offs: there is no way to describe *influence without authority* that does not admit what
it costs. The architecture track has a choice, and the thin cards took it. They name the
pattern, explain the mechanism, and stop — which reads as endorsement, and endorsement is how a
four-person team ends up running a saga orchestrator.

The D6 addition:

> **The bill this pattern sends, and the size below which it is a net loss.**

Two required parts, and a card missing either was rewritten:

| Part | Why it is required |
|---|---|
| A **concrete ongoing cost**, not a caveat | "It adds complexity" is true of everything and decides nothing. "Every feature now touches four files and a mapper" is a thing the reader can weigh |
| A **threshold** — a team size, a service count, a moment | The trade genuinely flips somewhere. A card that says "it depends" has moved the work back onto the reader, which is what they came here to avoid |

Eight chosen so the *kind* of bill differs each time — a wave of eight cards all saying
"complexity" would be one idea in eight places:

| Card | The kind of bill |
|---|---|
| Monolith vs Microservices | Organisational — the threshold is team count, not request rate |
| CQRS & Event Sourcing | Permanence — an append-only log is a promise you cannot take back |
| Domain-Driven Design | Access to people — without the domain expert it degrades to a folder layout |
| Clean / Hexagonal | Indirection — the adapter you never swap is pure overhead |
| Saga & Outbox | Business logic — compensation is not rollback, and somebody has to design every partial state |
| Resilience Patterns | Load amplification — retries cause the outage they were added to survive |
| Event-Driven | Observability — you trade the stack trace for a correlation ID |
| SOLID | Speculative generality — an interface with one implementation is a guess about the future |

### The D7 spec — day two, not day one

`devops`'s thin cards all describe adoption: what the tool is, how you set it up, the commands.
Not one of them describes what the thing **becomes**. That is the whole gap, because in this
domain nothing fails at adoption — every tool here installs fine and demos well. They fail two
years later, quietly, in a shape that was decided by one choice made in week one.

> **What this looks like two years in, and the one decision now that prevents it.**

This is deliberately *not* D6's bill-and-threshold, and the difference is worth stating because
the two are easy to blur. D6 asks **whether to adopt at all** — a trade you make once, with a
size below which it is a loss. D7 assumes adoption already happened and asks **what it decays
into** — a failure that has no threshold, arrives on schedule, and is cheap to prevent and
expensive to reverse.

The preventive decision must be **something you can do this week**, and it must be genuinely
cheaper now than later. If the fix is equally easy in year two, there is nothing to warn about
and the card is not a D7 card.

| Card | The decay |
|---|---|
| Helm & Kustomize | Charts become a templating language nobody can diff |
| GitHub Actions | Forty copy-pasted workflows and unpinned third-party actions |
| Secrets Management | Nothing can be rotated, because rotation was never once performed |
| Kubernetes Security | Everyone is cluster-admin and the network is flat |
| Policy as Code | Two hundred policies, all in audit mode |
| CI/CD Pipeline | A slow pipeline makes batches bigger, which makes failures harder — the flywheel in reverse |
| Docker | Images that cannot be rebuilt, running as root |
| Platform Engineering | The platform team becomes the ticket queue it was built to abolish |

### The D8 spec — the query that runs, returns a number, and is wrong

The census that Phase 8's closing record asked for has now been run, and it changed the queue:
184 of 227 remaining thin cards are inside the seven domains D1–D7 already worked, because each
wave took eight and no domain was finished. So D8 goes back to `data` — worst ratio on the site
at 74%, and the same domain D1 started with.

`data` is unlike every other domain here in one specific way, and it is the way that makes it
worth a second wave. **Everywhere else on this site, a mistake produces an error.** A misconfigured
sensor logs nothing, a bad Dockerfile fails to build, a wrong subnet mask drops the packet. In a
database, the overwhelmingly common failure is a query that runs to completion, returns a
plausible number, and is wrong — and nobody finds out until the number reaches a meeting.

> **The addition: name the silent wrong answer, and say how you would notice.**

Both halves are required. A card that names a trap without a detection is a warning nobody can
act on; the detection is what makes it a working card rather than a piece of folklore.

The eight are chosen so the *mechanism* of wrongness differs each time — a wave of eight cards
all about NULLs would be one idea in eight places, even though NULL is genuinely responsible for
three of them:

| Card | The silent wrong answer |
|---|---|
| SQL Joins | A `WHERE` on the right-hand table turns a LEFT JOIN back into an INNER JOIN |
| Aggregation | Joining before aggregating multiplies rows, and `SUM` cannot tell |
| Window Functions | The default frame is `RANGE`, and ties collapse into one bucket |
| Subqueries & EXISTS | `NOT IN` against a subquery containing one NULL returns **zero rows** |
| ACID & Transactions | Read-modify-write without a lock loses an update at any isolation level below `SERIALIZABLE` |
| Reading Query Plans | `EXPLAIN` without `ANALYZE` prints an estimate, and the estimate is the thing that was wrong |
| Indexes | A `UNIQUE` index does not prevent duplicate NULLs |
| Time-Series | Grouping by day in the wrong time zone moves rows between days, and late arrivals change yesterday |

**✅ D8 shipped** — 8 cards, `data` 31 → 23 thin (74% → 55%).

### The D9 spec — the bug that sent you here

`web`'s second wave takes the other half of the domain. D5 worked the tooling and performance
cards, where the gap was the developer's own machine. What is left in the thin list splits
cleanly into framework cards and **fundamentals** — Closures, Prototypes, the DOM and events,
Promises, Flexbox, Grid, custom properties, how a page renders — and those have a different
problem entirely.

Nobody reads a closures card out of curiosity. They read it because a loop printed the same
number five times, or a value went stale inside a callback, and something sent them looking.
The thin fundamentals cards explain the mechanism and never name the symptom, which means
**the reader who needs the card most cannot recognise that this is the card**.

> **The addition: the bug that sent you here.** Symptom first, in the words someone would use
> before they knew the cause; mechanism second.

One test, and it is strict: the symptom has to be **recognisable without knowing the
answer**. "You misunderstand the event loop" is not a symptom. "Your `forEach` finished
instantly and nothing was saved" is.

| Card | The symptom |
|---|---|
| Closures, Scope & `this` | The loop printed `5` five times; `this` became undefined when you passed the method somewhere |
| Prototypes & Modern Classes | It worked as `obj.method()` and broke as `setTimeout(obj.method)` |
| The DOM & Events | The click handler works, until the row was added after page load |
| Async Deep | `forEach` returned immediately and nothing was saved; a loop of `await` took thirty seconds |
| Flexbox | The flex item refuses to shrink and pushes the layout wider than the screen |
| CSS Grid | One long word or a wide table blows the column out past `1fr` |
| Modern CSS | A `var()` fallback did not apply, and the property came out `unset` rather than inherited |
| How the Browser Renders a Page | The text jumps when the font loads, and the page is blank until the stylesheet arrives |

**✅ D9 shipped** — 8 cards, `web` 25 → 17 thin (64% → 44%).

### The D11 spec — what you must already have before this runs

D2 gave `redteam`'s tool cards *what using this costs you*. Thirty-two remain, and they share a
second gap that is arguably worse for a reader learning the subject: **every card is written as
though you can simply run the tool.**

You cannot. Mimikatz needs local administrator and a debug privilege. Rubeus needs a domain
context. Impacket needs a credential or a hash you do not have yet. Hashcat needs the hash
*first*, which is the entire problem. A catalogue that omits the precondition reads as a list of
capabilities when the real subject is a **chain**, and the chain is the thing a learner cannot
infer from the tool's own documentation.

> **The addition: what you must already have before this runs, and the control that denies it.**

The second clause is not decoration. A prerequisite is a control point by definition — the place
a defender can stand — and naming it keeps these cards useful on both sides of the engagement,
which is how the rest of this site treats offence.

One test: the prerequisite must be **specific enough to be denied**. "Access to the network" is
not a prerequisite; "a credential or NTLM hash, plus reachability to 445" is, because a defender
can act on each half.

| Card | The precondition | Kind |
|---|---|---|
| Mimikatz | Local admin *and* `SeDebugPrivilege`, on a host where LSASS is readable | Privilege |
| BloodHound & SharpHound | **Any authenticated domain user** — that is the finding | None at all |
| Impacket | A credential or hash, plus reachability to SMB/RPC | Credential |
| Kerberos Attacks | A domain user, plus an account configured a particular way | Protocol configuration |
| Hashcat | The hash, already stolen. Everything upstream is the hard part | Prior theft |
| Pacu | Valid AWS credentials — usually long-lived keys that should not exist | Cloud key |
| ADCS Abuse | A domain user plus one misconfigured certificate template | Misconfiguration |
| Living off the Land | Code execution you already have, and nothing else | Existing foothold |

**✅ D11 shipped** — 8 cards, `redteam` 32 → 24 thin (62% → 46%).

### The D12 spec — the assumption you carry over from the other cloud

D3 worked `cloud`'s *concept* cards — cost control, landing zones, CSPM, Terraform — and its
rule was **provider-neutral**: write the failure mode that is the same on all three, because a
service description dated on the day it was written is the thing on this site most certain to
rot.

The thirty-two that remain are the opposite kind of card. They are **service** cards, they come
in matched pairs (AWS IAM and GCP IAM, AWS VPC and GCP VPC, and so on), and for them the
provider *is* the subject. Writing those provider-neutral would be writing nothing.

So D12 inverts D3's rule deliberately, and the inversion is the point:

> **The addition: the assumption you carry over from the other cloud, and exactly where it is
> wrong.**

Anyone who learned one cloud and moved to another arrives with a working mental model that is
about 80% right, and the 20% is not evenly distributed — it is concentrated in a handful of
places where the two designs disagree at the root. Those places are almost never in the
comparison table, because comparison tables map service *names*.

The test: the difference has to be **structural, not a naming difference**. "AWS calls it a
Security Group and GCP calls it a firewall rule" is a glossary entry. "GCP firewall rules are
VPC-wide and priority-ordered with denies; AWS security groups are instance-attached, stateful
and allow-only" is a different model of the same problem.

| Card | The assumption that breaks |
|---|---|
| GCP IAM | You cannot attach a policy to an identity — permissions are bindings *on resources* |
| AWS IAM Policies | A permission can be granted and still denied; five policy types are evaluated |
| GCP VPC | The VPC is **global**. Subnets are regional. Firewall rules span the whole network |
| AWS VPC | Everything is AZ-scoped, and a subnet is "public" only because of its route table |
| GCP Service Accounts | A service account is an identity **and** a resource you grant access *to* |
| AWS KMS | The key policy is the authority; the default one delegates to IAM, and a custom one may not |
| GCP Load Balancing | One global anycast IP, and health checks arrive from ranges you must allow |
| AWS Observability | Logs and Metrics are separate products with separate bills |

**✅ D12 shipped** — 8 cards, `cloud` 32 → 24 thin (50% → 38%).

### The D13 spec — what it means when it finds nothing

D4 gave `blueteam`'s tool cards *what this tool cannot see*. The twenty-eight that remain are
mostly the domain's **practices and outputs** — hunting, tuning, benchmarks, forensics,
adversary emulation, threat intel — and they share a gap that is peculiar to defensive work and
almost never written down.

**Blue-team tools return a negative result most of the time.** The hunt finds nothing. The
sandbox says clean. The benchmark passes. The coverage map is green. And nothing on this site,
or in most of the documentation these tools ship with, says how to read that — so a negative
result gets treated as reassurance when it is, at best, a statement about the question that was
asked.

> **The addition: what it means when this finds nothing, and what would have to be true for that
> to be good news.**

The second clause is the working half. "It might be a false negative" is a shrug; naming the
conditions under which absence is genuinely evidence is a checklist somebody can run.

The eight are chosen so the *mechanism* of the false negative differs each time:

| Card | Why "nothing found" may mean nothing |
|---|---|
| Threat Hunting | The hypothesis was never written down, so nobody can say what was ruled out |
| Windows Forensic Artifacts | Absence of an artefact is not absence of activity — rollover, defaults, anti-forensics |
| Vulnerability Scanners | An unauthenticated scan is a guess from outside the host |
| MITRE ATT&CK coverage | A green cell means a rule exists, not that it fires |
| YARA | A rule is a hypothesis about bytes; no match means your description is wrong, not that the file is clean |
| Malware Sandboxes | Evasion, time bombs, geofencing, and C2 that was already taken down |
| Detection Tuning | Zero alerts after tuning: did you remove the noise or the detection? |
| CIS Benchmarks & STIGs | A pass measures configuration against a checklist, and "not applicable" is doing a lot of work |

**✅ D13 shipped** — 8 cards, `blueteam` 28 → 20 thin (52% → 37%).

### The D14 spec — the number at which this stops being the right answer

`data`'s remaining thin cards are mostly **product** cards: PostgreSQL, SQLite, Redis, MongoDB,
Cassandra, DuckDB, graph databases. D1 gave each card a different missing thing and D8 gave the
SQL cards their silent wrong answers. The product cards need a third thing, and it is the one
that makes database advice either useful or worthless:

> **The addition: the number at which this stops being the right answer, and what you move to.**

Every one of these cards is currently written as though data volume and access pattern were
details. In databases they are the *only* thing. "PostgreSQL is the default choice" is true and
useless without the sentence that follows it — until *what*? "SQLite is everywhere" is true and
the limit is not the one people assume: it handles hundreds of gigabytes comfortably and falls
over on **concurrent writers**, which is a completely different axis.

Two requirements, and a card missing either was rewritten:

| Requirement | Why |
|---|---|
| A **named threshold** — rows, writes per second, working-set size, hop count, concurrent writers | "It depends on your workload" hands the work back. A number is arguable; a shrug is not |
| **What you move to**, and what that costs | A limit with no next step is discouragement. The migration is the actual decision |

The eight are chosen so the *dimension* differs each time — a wave where every threshold was
"rows in the table" would be one idea eight times:

| Card | The axis that actually binds |
|---|---|
| PostgreSQL | Connections and the single writer node, long before storage |
| SQLite | Concurrent writers — not size |
| Redis | Working set against RAM, and what eviction does at the boundary |
| MongoDB | The moment the access pattern needs a join |
| Cassandra & DynamoDB | Below a threshold as well as above one — knowing the queries first |
| Partitioning & Sharding | Maintenance cost, not query time. And sharding is a one-way door |
| Columnar Engines | Scan-heavy analytics, and DuckDB's single-node ceiling |
| Graph Databases | Traversal depth: two hops is a join, five is a graph |

**✅ D14 shipped** — 8 cards, `data` 23 → 15 thin (55% → 36%).

### The D15 spec — show the artefact

D6 took `eng`'s architecture patterns. What remains splits into more technical cards and a
**craft and career** cluster — code review, ADRs, estimation, technical debt, Staff+ archetypes,
influence without authority — and those are thin in a way that adding analysis will not fix.

They already contain analysis. What they contain none of is **the thing itself**. A card explains
that a good review comment is specific and kind, and never shows one. A card explains that an ADR
records the decision and its context, and never contains an ADR. A card explains that estimates
should carry assumptions, and gives no estimate.

> **The addition: the artefact, written out. The review comment as it would be typed. The ADR
> with its headings filled in. The estimate with its assumptions and its range.**

This is the first spec in the phase that adds *concrete* rather than *analytical* content, and it
is the right one here for a specific reason: craft is imitated before it is understood. A reader
who has never seen a good design doc cannot produce one from a description of its qualities, and
one worked example does more than a page of criteria.

The test: **it has to be copy-pasteable.** Not "a review comment should explain the why" but the
comment, in quotes, that somebody could adapt in thirty seconds.

| Card | The artefact |
|---|---|
| Code Review | Three versions of the same comment: unhelpful, good, and blocking |
| ADRs & Design Docs | A complete short ADR, all four headings filled in |
| Estimation & Planning | An estimate with its assumptions listed and a range rather than a number |
| Designing for Failure | A completed pre-mortem for one real dependency, rows and all |
| Staff+ Archetypes | What evidence looks like per archetype, as sentences a manager could paste |
| Influence Without Authority | The message that actually gets another team to act |
| Back-of-the-Envelope | A full worked calculation with the numbers |
| API-First | The contract, and the three questions to ask in review |

**✅ D15 shipped** — 8 cards, `eng` 24 → 16 thin (32% → 21%).

### The D16 spec — what this touches that your scope may not cover

`redteam` has had two waves. D2 gave each tool card *what using it costs you and what the
defender sees*; D11 gave *what you must already have before it runs*. The twenty-four remaining
share a third gap, and it is the one the domain's own first card —
**Rules of Engagement — Read This First** — exists to address and then never connects to any
specific tool.

Several of these tools reach past the target by their nature rather than by mistake. Radio does
not respect a property line. OSINT about a company is mostly data about its **people**. A MITM
on a network segment intercepts everyone on it. `sqlmap` writes. Proving exfiltration means
actually moving data somewhere real.

> **The addition: what this touches beyond the target, and the line the rules of engagement have
> to contain before you run it.**

The second clause keeps it practical rather than a caution: a boundary with no corresponding
clause is a worry, and a boundary with one is a pre-engagement checklist.

The test: the reach must be **inherent to the tool**, not a mistake an operator could avoid.
"Do not scan out of scope" is discipline; "802.11 capture cannot exclude the neighbours' frames"
is physics.

| Card | What it reaches |
|---|---|
| Shodan & Censys | Third-party data about hosts, some of which are not yours and some of which is old |
| Google Dorking, Maltego, SpiderFoot | Personal data about employees — the subject is people, not infrastructure |
| Wifite & hcxdumptool | Radio geography, which ignores the property line entirely |
| Bettercap | Every device on the segment, not just the one in scope |
| sqlmap | The target's data, in write mode, on a system that may be production |
| Flipper Zero & Sub-GHz/RFID | Physical premises, other tenants, and law that varies sharply by jurisdiction |
| Data Exfiltration Channels | Real data leaving to a real destination you now hold |
| msfvenom | An artefact that becomes public the moment somebody submits it to a scanner |

**✅ D16 shipped** — 8 cards, `redteam` 24 → 16 thin (46% → 31%).

### The D17 spec — what you are billed for, and which default is expensive

`cloud` has had two waves: D3's provider-neutral failure modes for the concept cards, D12's
cross-cloud assumptions for the service cards. The twenty-four remaining share a third gap, and
it is the one thing that makes this domain unlike every other on the site.

**Everywhere else, a mistake breaks something. Here, a mistake is billed** — quietly, monthly,
by a service that is working exactly as designed. Not one of these cards says what the meter
counts.

> **The addition: the unit you are billed for, which default is expensive, and where the surprise
> line item comes from.**

One hard rule, and it is what makes this durable rather than the fastest-rotting content on the
site: **name the unit, never the price.** Prices change quarterly and would put a stale number on
1,420 pages. Billing *shapes* — per GB scanned, per hour whether or not it is used, per GB
crossing a zone boundary, a 90-day minimum on an object stored for one — change on a scale of
years, and they are what actually determines the invoice.

| Card | The meter |
|---|---|
| GCP Storage | Storage class minimums — an Archive object deleted next week still bills for a year |
| AWS Compute | The instance is the part you switch off. EBS, snapshots and a public IPv4 are not |
| GCP Compute | Persistent disks bill provisioned, not used; discounts are a commitment decision |
| GCP Observability | Log **ingestion** volume, and a default bucket that keeps everything |
| BigQuery | Bytes **scanned**, not returned. `SELECT *` is the whole lesson |
| Cloud CI/CD | Build minutes, and what a cache miss costs on every push |
| Hybrid Connectivity | Data transfer — the line item that surprises people most, on every provider |
| GCP Databases | HA doubles it, storage auto-grows and **never shrinks** |

**✅ D17 shipped** — 8 cards, `cloud` 24 → 16 thin (38% → 25%). Site at **155 thin**.

**✅ D18 shipped** — 8 cards, `blueteam` 20 → 12 thin (37% → 22%). Site at **147 thin — §8's target is met.**

### The D18 spec — who owns it, how often, and what it becomes without that

The wave that crosses §8's target goes back to `blueteam` for a third time. D4 gave its tool
cards *what this tool cannot see*; D13 gave its practices *how to read a negative result*. The
twenty remaining share the failure mode that actually kills defensive tooling in real
organisations, and it is not technical.

**These tools are deployed and then not operated.** A threat-intel platform whose feeds nobody
curates fills with expired indicators. A SIEM's field extractions break silently the day an
application changes its log format. A hardening scanner produces a report nobody opens. An
adversary-emulation exercise run once proves something about a Tuesday in March.

> **The addition: what this needs from a person every week or month, and what it silently becomes
> without that.**

The second clause is what stops this being a maintenance checklist. Every one of these degrades
into a *specific* wrong thing — not "it gets worse" but "it becomes a list of indicators that
were true last year", which is a claim somebody can go and check.

The test: the cadence must be **nameable** — weekly, per release, per log-source change — and the
degraded state must be **recognisable**, so a reader can tell whether they are already in it.

| Card | Without an owner it becomes |
|---|---|
| MISP & OpenCTI | A database of indicators that were true last year |
| Splunk / SPL | Dashboards that quietly stopped matching when a log format changed |
| OSQuery | Packs that error on some platforms and return nothing, which looks like a clean fleet |
| Lynis | A score nobody reads, instead of a diff somebody acts on |
| Adversary Emulation | Evidence about one Tuesday, presented as coverage |
| Chain of Custody | A process that exists in a document and has never been performed |
| Purple Teaming | A workshop, rather than a loop that closes |
| Elastic / ELK | A cluster with a mapping explosion and no index lifecycle |

## 7. The trap in this plan

A deepening programme is exactly the kind of work that feels productive and can produce
nothing. Three specific ways it fails, and the guard for each.

| Failure | Guard |
|---|---|
| **Padding** — words added, nothing said | The step-4 test. If you cannot name the trap, stop at three cards. A padded card is worse than a short one, because it now costs the reader time to discover there is nothing there |
| **Rewriting instead of extending** | The existing table is usually correct and was checked. Add around it. Rewriting invites new errors into content that was already verified |
| **Losing the title** | Deepening must not retitle, because the id is a permalink and five `localStorage` prefixes key on it. If a better title genuinely emerges, it goes through `data/renames.json` and `slug-aliases.json` like any rename |

## 8. How to measure whether it worked

The measurement in §1 is a script, not a judgement, so it can be re-run. The honest success
criteria:

```
before:  330 topics single-concept and under 1,800 chars   (23% of site)
target:  under 150, with the remainder audited and confirmed as reference cards
ACTUAL:  147 (10% of site) after 18 waves — ✅ target met, and the remainder audited in D10
```

And the counter-metric, because §7's first failure mode is invisible in a length number:
**mean characters per concept card should not rise.** If cards get longer and the number of
concept cards per topic does not, the pass is padding rather than deepening — and that is
detectable in the same script that produced this section.


---

# Worked specifications — four sessions, startable without designing

> §4–§7 of the original handbook specified ten sessions to this standard, and those are the
> ten that got built. Everything specified only as a title has a much worse record. So four
> of Phase 7's first ten, and one Phase 8 wave, are written out here to the same depth: the
> concept cards, the tables, the verdict each table needs, and the cross-references.

## W1 — `cs`: *Little's Law &amp; Queueing — Why the Wait Explodes Before the Server Is Full*

**Badge** `CS • Systems` · **Icon** ⏳ · **Position** after *Percentiles &amp; Latency*, which
it explains from underneath.

| Concept card | Content |
|---|---|
| 1 — *One Equation, and What It Refuses to Let You Believe* | `L = λW`. Items in the system equals arrival rate times time in the system. It holds for any stable system regardless of distribution, which is unusual and is why it is worth memorising. The immediate use: two of the three are always measurable, so the third is never a guess |
| 2 — *Utilisation and Latency Are Not Linear* | The table of wait multiplier against utilisation — 50%, 70%, 80%, 90%, 95%, 99% — with the knee visible. **Verdict:** running a system at 90% is not efficiency, it is a decision about latency that somebody should have made on purpose |
| 3 — *Why Adding One Worker Sometimes Fixes Everything* | Because you moved back down the curve, not because you added 10% capacity. Explains the support queue that collapses when one person joins, and the API that recovers from a two-instance increase |
| 4 — *Variability Is the Hidden Term* | The equation says nothing about variance, and variance is what makes a queue at 60% utilisation still spike. Batch arrivals, slow outliers, and the single long job that blocks everything behind it |
| 5 — *Where This Shows Up* | Table across four domains: a support queue (`ops`), a thread pool (`cs`), a database connection pool (`data`), a checkout line. **Verdict:** it is the same equation each time, which is the argument for learning it once |

**Cross-references** *Percentiles &amp; Latency*, *Working a Queue — Prioritisation, Batching &amp;
Not Drowning*, *Connection Pooling — Surviving Many Clients*, *Capacity Planning*.

**The trap to land** the intuition that a system at 80% has 20% headroom. It has roughly a
quarter of the headroom it had at 50%, and the reader should leave unable to unsee that.

---

## W2 — `sec`: *Asset Discovery — You Cannot Protect What Nobody Listed*

**Badge** `SEC • Programme` · **Icon** 🗺️ · **Position** near *Mapping Your Own Attack
Surface*, which it generalises inward.

| Concept card | Content |
|---|---|
| 1 — *Every Coverage Metric Has an Unknown Denominator* | "98% of endpoints have the agent" is a claim about the machines you know. The interesting machines are in the other set by definition, and the sentence is unfalsifiable until the estate is enumerated |
| 2 — *Six Sources, and Why No Single One Is Enough* | Table: directory objects · DHCP leases · network scans · cloud APIs · agent inventories · finance's purchase records. Each has a characteristic blind spot — **the last one finds what IT never provisioned**, which is why it is on the list |
| 3 — *Reconciliation Is the Work* | Six sources produce six overlapping lists with different identifiers. The card's practical core: choose a primary key, decide what "the same machine" means, and record what each source uniquely contributed. **Verdict:** the reconciliation rules are the asset inventory; the list is its output |
| 4 — *The Categories That Are Always Missing* | Contractor devices · test systems that became production · lab equipment · cloud accounts opened on a card · things with an IP and no owner. Each with the source that would have found it |
| 5 — *Keeping It True* | An inventory decays from the day it is finished. The only durable version is derived — provisioning writes to it, decommissioning removes from it, and a weekly diff is reviewed by a person. **Verdict:** a hand-maintained inventory is a snapshot with a date on it, and should be labelled as one |

**Cross-references** *Asset &amp; Configuration Management — A CMDB That Stays True*,
*Mapping Your Own Attack Surface*, *Shadow IT* (Phase 7, CN), *Vulnerability Management
Lifecycle*.

**The trap to land** the finance record. Nearly every organisation can find unmanaged cloud
spend and unknown SaaS from an expenses export in an afternoon, and almost nobody has tried.

---

## W3 — `cloud`: *Multi-Cloud — The Four Reasons, and Which Ones Survive Contact*

**Badge** `Cloud • Strategy` · **Icon** 🧭 · **Position** beside *Landing Zones &amp;
Multi-Account Structure*.

| Concept card | Content |
|---|---|
| 1 — *Four Reasons, and Two of Them Are Real* | Regulatory requirement · acquisition · deliberate best-of-breed · fear of lock-in. The first two are facts you inherit; the third is defensible per workload; **the fourth buys an abstraction layer that usually costs more than the lock-in it avoids** |
| 2 — *What Multi-Cloud Actually Costs* | Table: two sets of IAM models, two networking models, two billing models, two on-call knowledge bases, and every engineer half as deep in each. **Verdict:** the cost is not the infrastructure, it is that expertise does not divide |
| 3 — *The Abstraction Trap* | A layer that hides both providers gives you the intersection of their features and the union of their failure modes, plus a component only you maintain. Where it is genuinely right: a small, stable surface — object storage, DNS, secrets — chosen deliberately |
| 4 — *The Version That Works* | Per-workload placement with a common identity and a common observability plane. Each workload lives entirely in one provider; the things that must be shared are the things that are boring in both |
| 5 — *Asking the Question Properly* | Not "should we be multi-cloud" but: which workload, moved to which provider, for which specific capability, at what cost in expertise? **Verdict:** a question nobody can answer in that form is a strategy nobody has |

**Cross-references** *Landing Zones &amp; Multi-Account Structure*, *Well-Architected*, *Exit
Planning &amp; Lock-In* (Phase 7, CD), *Cloud Rosetta Stone*.

---

## W4 — Phase 8 wave **D1**, `data`: the deepening pass, worked

Not one card — a session. `data` has 40 thin topics; a session takes eight of them and
applies §5's steps. The eight, and the one thing each is missing:

| Card | Add |
|---|---|
| *Locking &amp; MVCC* | The failure mode: what a lock wait looks like from the application (a timeout, not an error), and why the query that is *blocked* is rarely the query that is *wrong* |
| *Connection Pooling* | The decision: pool size against database max connections, and the arithmetic that makes a small pool faster than a large one. Cross-reference W1 |
| *ER Modeling* | The trap: modelling the current process rather than the invariant, which is why the schema needs changing every time the business does |
| *The Semantic Layer &amp; Metrics* | The decision: where the definition lives when the warehouse, the dashboard and the application each have one |
| *Normalization — 1NF Through BCNF* | The verdict the table lacks: when to stop, and the honest note that analytical schemas denormalise on purpose |
| *Backups &amp; Point-in-Time Recovery* | The failure mode: the restore that has never been run, and the recovery-time number nobody has measured |
| *Replication &amp; High Availability* | The decision: synchronous against asynchronous, expressed as what you lose in each failure |
| *Monitoring a Database* | The trap: averages hiding the p99, which is the same argument as W1 arriving from a different direction |

**Session shape** eight cards, roughly two hours, one commit. Re-run the §1 measurement
afterwards and record both numbers — thin count *and* mean characters per concept card, so
§7's padding failure is visible if it happened.


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

# Phase 9 — the duplication problem, measured

Phase 7 asks what is missing. Phase 8 asks how good what is there is. This asks the third
question: **how much of it is the same thing twice?**

## 1. The measurement

Every pair of topic titles, compared by token overlap with stop-words and acronym expansions
removed. `acronym` excluded, since it is generated.

**36 pairs share 50% or more of their meaningful tokens.** The top of the list is not
ambiguous:

| Overlap | Pair |
|---|---|
| 0.86 | `script` *Web Scraping — Extracting Data From Websites* · `script` *Web Scraping – Extracting Data from Websites with Python* |
| 0.83 | `net` *Wireless — 802.11 Standards &amp; Security* · `net` *Wireless Networking — 802.11 Standards &amp; Security* · `net` *Wireless Security – 802.11 Standards &amp; Wi-Fi Hardening* (three of them) |
| 0.80 | `script` *WebAssembly (WASM)* · `web` *WebAssembly — Native Speed in the Browser* |
| 0.71 | `sec` *Zero Trust — Never Trust, Always Verify* · `sec` *Zero Trust – "Never Trust, Always Verify" Explained* |
| 0.71 | `script` *Object-Oriented Programming — Classes, Objects &amp; Inheritance* · `script` *Object-Oriented Programming — Classes &amp; Objects* |
| 0.71 | `script` *Design Patterns — Reusable Solutions* · `script` *Design Patterns — Named Solutions* |
| 0.60 | Kubernetes, three times: `devops` ×2 and `linux` ×1 |
| 0.62 | `shortcut` *tmux — Never Lose a Session Again* · `shortcut` *Tmux Survival Kit – Never Lose a Terminal Session* |

Concentration by domain pair: `script`↔`script` 6, `net`↔`net` 5, `script`↔`shortcut` 5,
`eng`↔`script` 3.

**Two `script` cards on regular expressions. Two on Git. Two on files. Three on Kubernetes
across two domains. Three on wireless in one domain.**

## 2. Why this happened, precisely

Not carelessness — a missing check. The audit method that governs new content
(*probe titles, verify the zeros*) was invented partway through this file's history and has
only ever been applied to cards being written **now**. Nothing has ever looked backwards, so
every session that wrote a card on a subject an earlier session had already covered added a
second one, and the site kept both.

The dash tells the story: several pairs differ only in whether the title uses an em dash or
an en dash, which means they were written by different sessions using different conventions
and neither session saw the other's card.

## 3. Legitimate duplication, which must not be consolidated

Some of this is deliberate and correct. The site teaches at two levels, and the same subject
appears once for a beginner and once in depth **on purpose**.

| Pattern | Verdict |
|---|---|
| A *Beginner*-badged card and a deep card on the same subject | **Keep both.** This is the site's teaching model, and collapsing it makes the beginner layer disappear |
| A *Reference* card (a table) and a *Concept* card | **Keep both.** Different jobs; the reference card is looked up, the concept card is read |
| The same subject from two *perspectives* — an attacker's and a defender's | **Keep both.** `pentest`↔`redteam` and `threat`↔`blueteam` pairs are usually this |
| Two cards with the same badge, the same depth, and no stated difference | **Consolidate.** This is the real population |

**The test:** open both, and write one sentence saying who each is for. If the sentence is
the same, one of them should not exist.

## 4. What consolidation costs, and the rule that follows

Deleting a topic is not free, and this file has established exactly how not free.

| Cost | Detail |
|---|---|
| The permalink dies | The id is a URL somebody may have bookmarked. `data/slug-aliases.json` exists for this and must be updated |
| Five `localStorage` prefixes orphan | `reviewed:` `bookmark:` `known:` `srs:` `note:` — a reader's note on the deleted card becomes unreachable |
| Related-map edges break | `suggest_related.py --check` will catch it; the fix is to repoint, not to delete the pair |
| Learning-path steps break | `check_paths.py` catches it; same fix |

**And a third option, added in wave C4 and absent from the table above: move.** When §3 says
keep both and the two cards are in the wrong *places* rather than duplicated, changing a card's
domain costs nothing at all — ids are `slugify(title)`, so the permalink, the five
`localStorage` prefixes, the related edges and the path steps are all unchanged. Check whether
the duplication is apparent before assuming it is real.

**So the rule is: merge, never delete.** The surviving card absorbs whatever the other had
that it lacked, the retired id goes into `slug-aliases.json` pointing at the survivor, and
`renames.json` records why. A reader following an old link lands on the better card. Nobody
loses a note.

## 5. The queue

| Wave | Pairs | Notes |
|---|---|---|
| **C1** — `script` internal | 6 | Web Scraping, OOP, Design Patterns, Regular Expressions, Git, Files. The largest domain and the worst offender, which is not a coincidence — 145 topics written across many sessions |
| **C2** — `net` wireless and cloud | 5 | Three wireless cards is the clearest case on the site. Likely outcome: one beginner card, one deep card, one retired into them |
| ✅ **C3** — `script`↔`shortcut` | 5 | Checked before merging, and the check was right: **2 merged, 4 refused**. The pair that mattered most was not on the list — two `script` PowerShell cards scoring 0.25 on titles and nearly identical in content |
| ✅ **C4** — Kubernetes across `devops` and `linux` | 3 | The guess was right and the action was not a merge. `devops` owns Kubernetes; `linux` owns container internals. **Moved, not merged** — §3 says keep both, and the card was in the wrong domain, not duplicated |
| ✅ **C5** — `sec` Zero Trust, `web`↔`script` WebAssembly and TypeScript | 4 | Small and clean, and it turned out to overlap Phase 8: both `web` cards retired were on the **thin** list. **2 merged, 1 refused** |
| ✅ **C6** — the tail | ~13 | Audited. The expectation held — **2 merged, the rest kept** — and the audit found a wrong acronym expansion that no check could see. **Phase 9's queue is complete** |

**About 23 merges**, of which perhaps 15 are unambiguous.

## 6. The check that should have existed

A near-duplicate report is mechanical and cheap: tokenise titles, strip stop-words and
acronym expansions, compare pairwise, report above a threshold. 1,432 titles is a million
comparisons and runs in under a second.

It cannot be a gate — legitimate duplication exists and §3 says why — so it is a **census**,
like the acronym-breadth report added earlier this session. Its job is to make a session
writing a new card notice that a similar one already exists, which is exactly the failure
that produced this list.

**And it should run at write time, not at review time.** A new card that overlaps an existing
one by 50% should be caught before the session builds a related-topics entry for it.


---

# Phase 10 — the tooling that makes Phases 8 and 9 real

Every item here exists because something in this session could not be measured, or was
measured by a throwaway script that nobody will find again. The rule this file has arrived at
several times over: **a number stated in a plan and not produced by a committed script is a
claim with a shelf life.**

## ✅ T1 — `tools/depth_report.py` — shipped

Phase 8's entire argument rests on a measurement that currently lives in this document and
nowhere else. The script emits both numbers §8 asks for:

```
1,432 topics · 330 single-concept and under 1,800 chars (23%)
mean chars per concept card: 1,118        ← the padding counter-metric
by domain, worst first: data 93% · web 85% · redteam 77% · blueteam 67% · cloud 62%
```

**Why both numbers:** thin count alone rewards padding, which is Phase 8's first failure
mode. Chars-per-concept-card rising while topic count holds is the fingerprint of a
deepening pass that added words and no ideas.

Not a gate. A census, printed by `make check` beside the acronym-breadth one.

## ✅ T2 — `tools/near_duplicates.py` — shipped

Phase 9 §6. Tokenise titles, strip stop-words and acronym expansions, compare pairwise,
report above 0.5 overlap. Runs in under a second on 1,432 titles.

**The design decision that matters:** it must be runnable on a *candidate title* before the
card is written — `near_duplicates.py --title "Spanning Tree — …"` — because the failure it
prevents is a session writing a card that already exists, and by review time the cost is
already sunk. The full pairwise report is the secondary mode.

## ✅ T3 — The verdict check, which is the rubric made mechanical — shipped

Measured this session: **2,098 tables across the site, and 565 of them (27%) are followed by
nothing at all.** No verdict, no prose, straight into the next block.

`style.css` already asserts the house rule — *every table gets a verdict* — and nothing has
ever checked it. Worst offenders: `script` 69, `shortcut` 51, `net` 46, `sec` 39.

| Decision | Reasoning |
|---|---|
| Warning, with a ceiling — not an error | 565 is too many to fix in one pass, and some are legitimate: a reference table in `shortcut` genuinely needs no verdict |
| Ceiling at the current count | Same ratchet as `inline style attribute`. It can fall and cannot rise, so no new table ships without a sentence saying what it means |
| Exclude `shortcut` and `acronym` | Reference domains, per Phase 8 §4 |

This is the highest-leverage check in the phase, because it enforces the one property §1 of
the rubric identifies as the difference between a card and a search result.

## ✅ T4 — The related-map orphan report — shipped

**902 of 1,432 topics (63%) have no related-topic link at all.** That is not automatically
wrong — the map was built by hand and hand-built things are partial — but the interesting
subset is:

**159 topics with three or more concept cards and over 3,000 characters have no links in or
out.** These are *good* cards that are dead ends. The worst are startling:

```
7 cards, 7,137 chars   Note-Taking for Learning — Notes You Never Reopen Are Theatre
7 cards, 6,538 chars   The Japanese Mastery Loop — Kata, Poka-Yoke, Hansei, Kaizen
6 cards, 6,222 chars   The Memory Palace — Method of Loci for Ordered Lists
6 cards, 6,028 chars   Study Systems That Survive a Brain That Won't Cooperate
6 cards, 5,584 chars   Microsoft Endpoint Configuration Manager (MECM)
```

The `productivity` domain is almost entirely unlinked, which explains something the reader
would notice: its cards are among the best on the site and are reachable only by browsing to
them.

**The report ranks orphans by depth**, so the work queue is "good cards nobody can reach
from anywhere else" rather than "topics missing metadata". Roughly 159 topics × 2 pairs is a
few sessions of genuinely high-return work.

## ✅ T5 — A search-quality harness

The site has search, acronym-aware search and a quiz built on the same index, and **nothing
tests whether searching for a thing finds it**. Every other user-facing behaviour has a
smoke test.

The shape is a fixture file of realistic queries and their expected topic:

```
"one way audio"          → voice-real-time-traffic-…
"page loads halfway"     → mtu-fragmentation-…
"revoke before reset"    → infostealers-…
"why is my laptop slow"  → laptops-batteries-thermals-…
"POAM"                   → the-risk-register-… or the acronym card
```

Score is *expected topic in the top three*. It fails when a content change quietly breaks
retrieval — for example when two near-duplicate cards (Phase 9) both match a query and
neither ranks first, which is a duplication symptom the title report cannot see.

## ✅ T6 — Reading time on the topic header

Derived at build time from character count, stamped as an attribute, rendered small beside
the badge. Costs nothing and sets an expectation, which matters on a site where cards range
from 900 to 15,000 characters with no outward sign of which is which.

**The honest caveat:** reading time is a proxy for length, not difficulty, and labelling a
dense 2,000-character card "2 min" is a small lie. Worth it, but the plan should say so.

## ✅ T7 — A difficulty attribute, and a filter for it

The site teaches at two levels — Phase 9 §3 says so explicitly — and the only outward sign is
a badge that sometimes reads *Beginner*. A `data-level` attribute with three values, stamped
from the badge where one exists and by hand elsewhere, would make the beginner layer
**filterable** rather than discoverable by accident.

This also fixes something Phase 9 exposed: three wireless cards are confusing without levels
and are a sensible progression with them.

## ✅ T8 — "New since you last visited"

The changelog exists and is generated. A per-reader version is a timestamp in `localStorage`
and a diff against the changelog's own dates — no new data, no server, one small view.

**Why it is worth the code:** the site adds thirty topics in a session and a returning reader
has no way to find them. The changelog answers "what changed"; this answers "what changed
*for me*", which is the question people actually have.

## ✅ T9 — A contradiction check across near-duplicates

`check_contradictions.py` already compares claims across the site. Phase 9's pairs are the
highest-probability place for two cards to disagree, because they were written by different
sessions months apart. Running the existing checker **restricted to the 36 near-duplicate
pairs** is a cheap, targeted pass — and any disagreement it finds is a bug in one of them,
not a stylistic difference.

## Ordering

| # | Item | Why here |
|---|---|---|
| 1 | **T3** verdict check | Highest leverage, enforces the rubric, and the ratchet stops the number growing while the rest happens |
| 2 | **T1** depth report | Phase 8 cannot start honestly without it |
| 3 | **T2** near-duplicates | Phase 9 needs it, and the `--title` mode prevents the next instance |
| 4 | **T4** orphan report | Turns a vague "the related map is partial" into 159 named cards |
| 5 | ✅ **T9** contradiction pass | Ten minutes, reuses an existing tool, and finds real bugs if any exist. **It found two — in the tool** |
| 6 | ✅ **T5** search harness | The last untested user-facing behaviour. **21 fixtures, 6 known misses, and one query that returned 90% of the site** |
| 7 | ✅ **T6** reading time | Shipped, and it broke both contrast and the search index on the way in |
| 8 | ✅ **T7** difficulty attribute | Shipped as `data-level` plus a `level:` search operator. 121 beginner, 8 advanced, 1,297 core |
| 9 | ✅ **T8** new since last visit | Shipped as a banner plus a `since:` operator. **Phase 10 is complete — all nine items** |


---

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

# Closing note for Phase 7–10

Four phases, and they are not alternatives — they are the same site measured four ways.

| Phase | Question | Size | Cost per unit |
|---|---|---|---|
| **7** — the gaps | What is missing? | 96 cards | High. New id, new links, duplication risk |
| **8** — the depth | How good is what is there? | 330 thin, ~244 queued | Medium. No new ids, no duplication risk |
| **9** — the duplication | How much is here twice? | 36 pairs, ~23 merges | Low, and it *reduces* the site |
| **10** — the tooling | Can any of this be measured next time? | 9 tools | Lowest, and it is what makes the other three verifiable |

**The recommended order is 10, 9, 8, 7 — the reverse of how they were written.** The tooling
makes the numbers reproducible; consolidation shrinks the surface before anyone invests in
it; deepening improves what survives; and new cards go last, onto a site that has been
measured, cleaned and improved rather than onto one that has not.

That order is also the least appealing, because writing new cards is the enjoyable part and
running a duplicate report is not. This file has made that observation before, about a
different backlog, and it was right then: **the reason the queue never shrinks is that the
enjoyable work is always available.**

One honest caveat on all four phases. The site moved from 1,401 to 1,432 topics in a single
session, and eleven domains changed. Every number in Phases 7–10 was measured on **1,432
topics, 30 domains, at the end of that session**. They will be wrong soon, and the scripts in
Phase 10 exist precisely so that being wrong is a one-command problem rather than a rewrite.


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

# The risk register, revisited — four risks that only a measurement could find

The register in the Execution Handbook was written from imagination: *what could go wrong
with a project like this?* It was a good list and four of its entries are now mitigated. But
every risk on it is one somebody could think of without looking at the repository.

Phases 8–11 looked. These four were invisible until something was counted, and none of them
appears on the original list.

| Risk | Likelihood | Impact | Evidence | State |
|---|---|---|---|---|
| **Silent style drift** — the house form improves and earlier content is never revisited, so the site becomes two sites wearing one theme | **Certain — it already happened** | High | 330 topics (23%) are single-concept and under 1,800 characters, concentrated entirely in domains written early. `data` is 93% thin; `cs` and `infra` are 0% | **Open.** Phase 8 |
| **Blind duplication** — the audit method governs new cards and has never looked backwards, so two sessions months apart both cover a subject and both cards ship | **Certain — it already happened** | Medium | 36 title pairs at ≥50% token overlap. Two `script` cards on regular expressions, three Kubernetes cards across two domains, three wireless cards in one. Several pairs differ only in em dash versus en dash | **Open.** Phase 9 |
| **Unreachable quality** — good cards exist and nothing links to them, so the reader who would benefit never arrives | High | Medium | 902 topics have no related-topic link, and **159 of those have 3+ concept cards and 3,000+ characters**. The `productivity` domain is among the best written and almost entirely unlinked | **Open.** Phase 10 T4 |
| **Unfalsifiable freshness** — the site can state what it has dated and cannot state what it has not | Certain | Medium | 51 dated claims. Three attempts to count the denominator failed on IP addresses, Wi-Fi standards and shell variables. There is no textual property that distinguishes a claim that ages | **Accepted, not mitigable.** Phase 11 §3 |

## What these four have in common

All four are **accumulation** risks rather than event risks. Nothing goes wrong on a
particular day; a small cost is paid per session and never collected. The original register
is full of event risks — a domain lapsing, data being cleared, a build breaking — and those
are the ones a person imagines, because they have a moment attached.

That suggests a habit rather than a mitigation: **once a phase, measure something nobody has
measured.** All four of these came from a single afternoon of counting things the repository
already contained, and every one of them was cheaper to find than it would have been to
predict.

## The fifth, which is about this file

| Risk | State |
|---|---|
| **The plan outgrows its own readability** — 11,600 lines, and the useful part is the last few hundred | **Open, and now acute** |

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


## Session record — Phase 10, items T1–T4 shipped, and four numbers that moved

The plan's own recommended order is **10, 9, 8, 7**, so this session started with the
tooling. Four tools, three of them censuses, and every one of them disagreed with the number
`plan.md` quoted — which is the entire argument for committing the script rather than the
figure.

| Number | Plan said | Tool says | Why they differ |
|---|---|---|---|
| Thin topics | 330 (23%) | **288 (20%)** | The plan counted `shortcut` and `acronym`; the tool excludes them, per Phase 8 §4's own rule about reference domains. Same population, honest denominator |
| Tables with no verdict | 565 | **513** | Same exclusion, same reason |
| Near-duplicate pairs | 36 | **54** | The tool folds plurals. "Regular Expressions" and "Regular Expression" were being counted as different subjects by the throwaway script that produced 36 |
| Deep orphans | 159 | **158** | The tool counts a resolved `data-xref` as a link, because a reader can follow one. One card was reachable that way |

Three of the four corrections make the site look *better* and one makes it look worse. That
distribution is roughly what an honest instrument should produce, and it is the reason the
plan's numbers are now marked as superseded rather than quietly edited.

### T3 — the verdict check, and why it is a ceiling

`style.css` has asserted *every table gets a verdict* since the `.verdict` class was
introduced, and nothing had ever checked it. **513 tables are followed by no prose at all**,
across every domain except the two reference ones.

A ceiling rather than an error, for exactly the reason the inline-style counter is one: 513
cannot be cleared in a pass, and a handful are legitimate. What the ceiling buys is that
**no new table ships without a sentence saying what it means** — which is the single property
the card rubric identifies as the difference between a card and a search result.

### T2 — the mode that matters, and the version of it that was wrong

`--title` is the point of the tool: run it *before* writing, because by review time the cost
is sunk. The first version used Jaccard overlap and reported this:

```
$ near_duplicates.py --title "Spanning Tree Protocol — Loops and Convergence"
  0.25  [net] Spanning Tree — Why a Loop Is Catastrophic, and What STP Does…
  Nothing at or above 0.50; closest shown. Clear to write.
```

**"Clear to write", against a card the same session had written.** Jaccard is symmetric and
punishes a short candidate against a long existing title, however completely the subject is
covered. The measure for `--title` is *containment* — what share of the candidate's tokens
already exist — which scores the same pair at 0.60 and refuses. Plural folding was needed
too: `loops` against `loop`.

That is the fifth check in this file whose first version measured something adjacent to the
claim. The pattern is now reliable enough to plan around: **write the check, then run it
against a case you already know the answer to**, before trusting a single number it produces.

### T4 — what the orphan report actually found

902 topics have no related link and no cross-reference pointing at them. The useful slice is
the 158 that are deep, and the domain concentration is stark:

```
7 cards  7,137 chars  [productivity] Note-Taking for Learning
7 cards  6,538 chars  [productivity] The Japanese Mastery Loop
6 cards  6,222 chars  [productivity] The Memory Palace
6 cards  6,028 chars  [productivity] Study Systems That Survive a Brain That Won't Cooperate
6 cards  4,946 chars  [productivity] Attention — Task Switching, Residue
```

**Five of the top seven are `productivity`**, which the connectivity measurement already
flagged as an island. The domain is among the best-written on the site and is reachable only
by clicking its chip. That is now a named, ranked work queue rather than an impression.

### Wiring

`make census` runs all three; CI prints them in the log as a reports-only step, so the
numbers move visibly in a pull request without gating it. `make check` gained the verdict
ceiling. All three tools guard `SIGPIPE`, because a census is a thing people pipe into
`head` and a `BrokenPipeError` traceback looks like a crash.

**Remaining in Phase 10:** T5 search harness, T9 contradiction pass over the duplicate pairs,
and the three reader-facing items T6–T8.


## Session record — two bugs found by reading Phase 9's own preconditions

Phase 9 §4 lists what a topic merge costs, and the list is what makes "merge, never delete"
the rule: the permalink dies, and **five `localStorage` prefixes orphan** — `reviewed:`
`bookmark:` `known:` `srs:` `note:`. The alias map exists to prevent both.

Before doing a single merge, I read the code that does the preventing. It did not.

### Bug one — `note:` was never migrated

```js
[REVIEWED_PREFIX, BOOKMARK_PREFIX, KNOWN_PREFIX, SRS_PREFIX].forEach(p => {
```

Four of the five. The missing one is the only piece of progress a reader **writes by hand**
— everything else is a click. So every rename in the site's history has silently discarded
the reader's own words while carefully preserving their checkboxes, and Phase 9 was about to
do it twenty-three more times.

### Bug two — the migration ran once per device, ever

```js
const ALIAS_MIGRATED_KEY = "migrated:slug-aliases-v1";
if (localStorage.getItem(ALIAS_MIGRATED_KEY)) return 0;
```

A boolean. A device that had visited before the merge would never migrate an alias added
after it — which is every device, for every future merge. The alias map's *hash redirect*
would still work, so the link would resolve and the progress would not follow it.

The flag is now keyed on the **contents** of the alias map — an FNV-1a hash of the sorted
pairs — so it changes exactly when the map does, runs once more, and does nothing on a
device that has already seen that map. Previous-generation flags are removed when the new
one is written, so they do not accumulate one per revision.

### And a test, because neither half had one

Three checks, and the middle one is named for what it is: *a note survives the move, which is
the one it used to lose*. The third proves a second run with an unchanged map moves nothing
and leaves exactly one flag. **135 → 138 smoke checks.**

### The general point

Phase 9 is a queue of twenty-three merges. Reading the preconditions before starting cost
twenty minutes and found a data-loss bug that had been live for the whole history of the
alias map — **and it would have been invisible after the merges, because a lost note leaves
nothing behind to notice.** The plan section that made this findable is the one listing what
the work *costs*, which is the least interesting part of a plan to write and turned out to be
the load-bearing one.


## Session record — Phase 9, first wave: four merges and four refusals

Eight candidate pairs examined with Phase 9 §3's test — *open both, write one sentence saying
who each is for; if the sentence is the same, one should not exist.* **Four merged, four kept**,
and the refusals took longer than the merges.

### Merged

| Retired | Into | Absorbed |
|---|---|---|
| `script` *Design Patterns — Named Solutions* | *Design Patterns — Reusable Solutions* | The over-engineering warning. The survivor had **no verdict at all** — it ended mid-code-block, which is the 513-table problem in its natural habitat |
| `script` *Web Scraping — Extracting Data From Websites* | *…with Python* | One honest sentence the survivor lacked: personal or research use is a grey area, **commercial use of scraped data is frequently unlawful outright** — the distinction that decides whether a hobby project can become a product |
| `net` *Wireless — 802.11 Standards & Security* | *Wireless Networking — 802.11…* | **Wi-Fi 7 (802.11be)**, which only the retired card had, the generation-name mapping, the 802.1X row, and two verdicts where there had been none |
| `devops` *Kubernetes — Container Orchestration at Scale* | *…Fundamentals* | The complexity caveat, rebuilt as a full concept card: when Kubernetes earns its cost and when it does not, ending on *"Kubernetes because it is what serious teams use" is not a requirement* |

Every merge left the survivor **better than either card was**, which is the test of whether
consolidation is worth doing at all. Three of the four added a verdict that had never existed.

### Kept, and why

| Pair | Why it stays |
|---|---|
| `sec` Zero Trust ×2 | One `SEC • Architecture`, one `Beginner`. The site's two-level teaching model, working exactly as designed |
| `script` OOP ×2 | One is a **language-agnostic reference** with a cross-language comparison table; one teaches it in Python. Different jobs — §3's reference-plus-concept case |
| `net` DNS deep-dives ×2 | Titles overlap at 0.60; content does not. One is *what DNS is* — records, DNSSEC, zones. The other is *how to troubleshoot it* — the resolution chain, tracing, cache. Both Beginner-badged, neither redundant |
| `net` Cloud Networking ×2 | Beginner and `NET • Cloud`. Same as Zero Trust |

**Half the queue was not work.** That is the number worth carrying into the remaining waves:
Phase 9 estimated "23 merges, of which perhaps 15 are unambiguous", and the first eight pairs
returned a 50% rate. The estimate should probably be halved.

### What the census says now

```
before  54 pairs at or above 0.50, across 1,373 titles
after   48 pairs at or above 0.50, across 1,369 titles
```

Four merges removed six pairs, because the three-way wireless and Kubernetes clusters each
collapsed more than one edge.

### On the mechanics

`slug-aliases.json` 103 → **107 entries**. `make check` passed without a single repointing:
none of the four retired ids appeared in `related.json` or `paths.json`, which the checks
would have named. That is luck rather than design — the next wave should check before
deleting rather than after, and the merge helper should do it.

Site total **1,432 → 1,428**. Smoke **138/138** · axe **6/6** · visual **2/2**. This is the
only phase whose success makes the site smaller.


## Session record — Phase 9 wave two, and the guard earning its place on first use

Wave one ended on a note: *"`make check` passed with no repointing needed, which was luck
rather than design — the merge helper should check `related.json` and `paths.json` before
deleting, not after."*

So the throwaway script became `tools/retire_topic.py`, with the check in front of the
delete. **It refused the first merge it was asked to do.**

```
$ retire_topic.py ai --retire "Fine-Tuning vs RAG" --into "Fine-Tuning vs. Prompting"
REFUSED — 3 reference(s) would break:
  related.json has fine-tuning-vs-rag-vs-prompting-when-to-use-which as a source with 1 link(s)
  related.json: training-pipeline-pretraining-sft-rlhf-dpo -> fine-tuning-vs-rag-…
  ai.html cross-references it by title
```

Three real references, on the very next merge after the wave that got away with it. The
repointing took two minutes with the list in front of me; finding them after the block was
gone would have meant reading a failing lint run and reconstructing what had been deleted.

The tool also refuses an ambiguous fragment — `"Zero Trust — Never Trust"` matched three
topics, because one card's title contains another's — and it follows existing aliases
forward, so no alias is left pointing at a topic that no longer exists.

### Two more merges

| Retired | Into | Absorbed |
|---|---|---|
| `ai` *Fine-Tuning vs RAG vs Prompting* | *…Picking the Right Tool* | The cost-ordered table and the rule underneath it: prompt, then retrieve, then fine-tune — plus the classic mistake, which is **fine-tuning to add knowledge** |
| `linux` *Disk Management* | *Storage Management* | The two commands the survivor lacked, and a verdict it never had |

The `linux` absorption is the one worth recording, because it nearly went wrong. The
absorption edit missed its anchor — the file uses a literal `→`, not `&rarr;` — and printed
an error, **but the retire ran anyway**, because they were two separate commands in one
shell line. For a few minutes the `df`/`du` content existed only in Git.

Recovering it turned out to improve the result. Reading the survivor properly showed it
already had `df -h`, `df -i` and two forms of `du`; what it genuinely lacked was the
largest-files command, `lsof +L1 | grep deleted`, and a verdict. So the absorbed content is
three lines rather than a duplicated block:

> When `df` and `du` disagree, the difference is a deleted file some process still has open —
> a log rotated out from under a service that never reopened it. The space returns when that
> process restarts, not when the file is removed, because it already was.

**The lesson is about sequencing, not about the tool:** absorb first, verify the absorption
landed, and only then retire. `retire_topic.py` cannot check that, because whether the
survivor absorbed the right thing is a judgement.

### Where the numbers are

```
topics        1,432 → 1,428 → 1,426     six merges
duplicates       54 →    48 →    46
thin topics     288 →   287              one survivor crossed the line by absorbing
mean chars/card 1,196 → 1,198            the padding counter-metric, holding
```

`slug-aliases.json` 103 → **109**. Smoke **138/138** · axe **6/6** · visual **2/2**.

That thin-count line is the first evidence Phase 8's counter-metric works as designed:
absorbing content into a survivor moved a card off the thin list and moved the mean by two
characters. A padding pass would have moved the mean by a great deal more.


## Session record — Phase 8 wave D1: the deepening pass, and the counter-metric holding

The W4 worked specification named eight `data` cards and the one thing each was missing.
All eight shipped, exactly as specified — which is the first evidence in this file that a
*deepening* wave can be specified to transcription depth the same way a content wave can.

| Card | Added | The sentence it now carries |
|---|---|---|
| *Locking & MVCC* | The failure mode | A lock wait does not look like an error — it looks like **nothing, for a while, and then a timeout** from a component several layers away |
| *Connection Pooling* | The decision | Raising the pool size past a point buys wait time rather than throughput. Fifty small pools still sum to one large one |
| *ER Modeling* | The trap | Model the invariant, not this year's process — and price belongs on the order line, because a product's price changing must not rewrite last year's revenue |
| *Normalization* | The verdict | 3NF and stop for transactional; denormalise deliberately for analytical. **Duplication with an owner is different from duplication by accident** |
| *Backups & PITR* | The failure mode | Backup jobs are monitored and restores are not, so the number nobody has measured is how long recovery takes |
| *Replication & HA* | The decision | Synchronous makes the replica a dependency of every write — you traded data loss for availability, which is a different trade from the one most people think they are making |
| *Monitoring a Database* | The trap | 10,000 queries at 2 ms and 100 at 4 s has a mean of 41 ms and a p99 of four seconds |
| *The Semantic Layer* | The decision | A definition in a glossary is documentation; a definition queries cannot bypass is the thing itself |

### The measurement, which is the point of having built the tool

```
                          before   after
thin topics                  287     279      ← eight, exactly
data domain             40 (93%)  32 (74%)
mean chars/concept card    1,198   1,200      ← +2
```

**The counter-metric is the finding.** Phase 8 §7 names padding as the first failure mode —
words added, nothing said — and predicted it would show up as the thin count falling while
mean characters per concept card rises. Eight cards gained roughly 2,000 characters each and
the mean moved by **two characters**, because every addition came as a *new concept card*
rather than as more prose in the existing one.

That is the difference between deepening and padding stated numerically, and it is now
checkable on every future wave without anyone having to read the diff.

### On the method

Each addition took one of Phase 8 §5's steps — verdict, failure mode, decision, trap — and
stopped there. None of the eight reached step 4 *and* step 5; several had exactly one honest
thing to add and got exactly one. The step list is doing what a rubric should: giving
permission to stop.

The habit that made it fast was reading all eight cards first, in one pass, before writing
anything. The eight are related — pooling, locking and monitoring are the same queueing
problem from three angles — and writing them together let each one point at the others
instead of repeating them.

Site **1,426 topics** (unchanged — deepening adds no ids, which is the whole argument for
doing it before Phase 7). Smoke **138/138** · axe **6/6** · visual **2/2**.


## Session record — Phase 8 wave D2: `redteam`, and the addition that changed the domain

D2's spec was one sentence and it turned out to be the right one: *each card needs the same
addition — when would you not use this, and what does it look like to the defender.* Eight
tool cards, one uniform second concept card, and the domain now reads differently.

| Tool | The sentence it gained |
|---|---|
| Masscan | There is no quiet configuration — there is a rate you chose and a rate somebody else notices |
| Amass | Passive and active are two different engagements, and the forgotten host is usually already in certificate transparency, because the log is permanent |
| ffuf | **Getting blocked invalidates the test** — the client learns their rate limiting works rather than whether their application is sound |
| Nuclei | A template is a request and a match condition written by a stranger, and both halves can be wrong. Read the ones tagged intrusive before enabling them |
| Responder | The defensive answer removes the technique rather than detecting it, and all three settings are free — which is why it still works everywhere |
| Aircrack-ng | Every other tool is bounded by an address range; **radio is bounded by geography**, and geography does not respect the rules of engagement |
| Sliver | Widely adopted means widely detected. What gets caught is beacon regularity, not framework choice |
| Nikto | Run it once, early, and never as your evidence — every finding is a lead to confirm |

### Why the uniform addition works here and would not elsewhere

`data`'s eight cards each needed a *different* thing — a failure mode here, a decision there.
`redteam`'s eight needed the same thing eight times, because the domain has a single
structural gap: it documents what a tool does and never what using it costs. That is a
property of the domain, not of the cards, and the spec caught it in one line.

It also makes the domain more useful to the reader it did not previously serve. Half these
tables now answer a defender's question — *what would I see if someone did this to me* — from
cards filed under offence. **The `redteam` tooling catalogue has quietly become a detection
reference**, which is a better outcome than the cards being individually longer.

### The measurement

```
                          D1 end   D2 end
thin topics                  279      271     ← eight, exactly, again
redteam                 40 (77%)  32 (62%)
mean chars/concept card    1,200    1,201     ← +1
```

Two waves, sixteen cards, and the padding counter-metric has moved **three characters in
total**. Phase 8 §8's target was "under 150 thin, with the remainder audited"; the run so far
is 288 → 271, which is sixteen cards of real progress and a reminder that the target is
roughly fifteen more sessions of this.

Site **1,426 topics**. Smoke **138/138** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 8 wave D3: `cloud`, and the failure mode that is provider-neutral

D3's spec asked for something harder than D1's or D2's: not *a* second card, but a second
card that stays true across AWS, Azure and GCP. The domain's thin cards are thin for a
specific reason — they were written as "here is the service, here is roughly what it costs",
and a service description dated on the day it was written is the one thing on this site
guaranteed to rot. A failure mode does not rot. The eight additions are all failure modes.

| Card | The second card it gained |
|---|---|
| Choosing Compute | Operational cost, not compute cost, is what you are choosing — the instance price is the number you compare and the patching, scaling and on-call are the number you pay |
| Cloud Cost Control | **A budget alert is not a budget control.** The alert fires after the spend, and every provider's story here is the same: the thing that stops spend is a quota, not a notification |
| Landing Zones | Retrofitting one is a different project entirely. Most of the rows are inconvenient; **overlapping `10.0.0.0/16` ranges is the one that is unfixable** without renumbering a live network |
| CSPM | Four thousand findings is the same as zero findings. The tool's default posture is "report everything", and a backlog nobody triages is indistinguishable from no tool at all |
| Terraform on AWS & GCP | State is the thing that breaks, and drift is how you find out — the console change somebody made at 2am is not in state, and the next apply is where you learn that |
| AWS Load Balancing & DNS | Failover is as fast as the slowest cache between you and the user, which is never your TTL alone: resolvers round up, and some clients pin for the life of the process |
| AWS Databases | What "managed" covers, and the half it does not — backups and patching yes; your schema, your query plans and your connection count no |
| AWS Serverless & Containers | **Scale-to-zero is a property of the function, not of the system.** The function scales to zero; the database it opens a connection to does not |

### Why provider-neutrality was the right constraint

The obvious way to deepen a cloud card is to add the other two providers' equivalents, and
that produces a three-column table that needs re-checking every quarter — the site already
carries 1,367 freshness stamps and does not need more surface that ages. Writing to the
failure mode instead means the card is *more* durable after the deepening than before it:
connection exhaustion behind a scale-to-zero function has been true since the first
serverless runtime shipped and will outlast every service name in the domain.

Three waves in, the three specs have each asked for a different addition — a per-card gap in
`data`, one uniform sentence in `redteam`, a provider-neutral failure mode in `cloud` — and
each was written *before* the cards were touched. The specs are doing real work; they are not
decoration on the table.

### The measurement

```
                          D1 end   D2 end   D3 end
thin topics                  279      271      263     ← eight, exactly, three times
cloud                                     40 (63%)  →  32 (50%)
mean chars/concept card    1,200    1,201    1,202     ← +1 again
```

Twenty-four cards across three waves and the padding counter-metric has moved **two
characters**. That number is the whole argument that this pass is adding content rather than
inflating it, and it only holds because every addition arrives as a new concept card with a
claim of its own rather than as extra sentences bolted onto an existing one.

Site **1,426 topics**. Smoke **138/138** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 8 wave D4: `blueteam`, and the mirror of D2

D2 gave the offensive catalogue the sentence it was missing — *what using this costs you*.
D4 gives the defensive catalogue the mirror of it, and the mirror turns out to matter more.
A red-team card that omits its cost makes an operator careless. **A blue-team card that omits
its blind spot makes a defender confident**, and confidence about coverage you do not have is
the specific failure the whole domain exists to prevent.

| Tool | What it cannot see |
|---|---|
| Zeek | A sensor sees what crosses it, and less crosses it every year — split-tunnel laptops, east-west inside a subnet, cloud-to-cloud that has no on-premise path |
| Wireshark | **You cannot analyse a capture nobody took.** By the time an incident is declared the packets are gone; only what was already being written down survives |
| Suricata & Snort | A signature is a description of something already named — the rule has to exist before the traffic does |
| Windows Event Logs | The event you need is off (4688 command line, 4104) or already rolled over. **Local retention is not retention** |
| auditd | Syscalls are not intent, and on a container host they arrive attributed to the host namespace unless something maps them back |
| Volatility | Memory is gone the moment the machine is. Every plugin is downstream of one decision made by whoever touched the box first |
| Sigma | Portable rule, non-portable field names — **a rule that converts cleanly and matches nothing looks identical to one that works** |
| Honeypots | Deception is silent against an attacker who does not look. Silence from a canary is not evidence of absence |

### The test that did the most work

Of D4's three tests, *"not the same blind spot eight times"* rejected the most drafts.
"Encrypted traffic" is a true and interesting limitation of Zeek, Suricata, Wireshark and
Arkime, and writing it four times would have produced four cards that each said the same thing
and a wave that added one idea rather than eight. Forcing a different **kind** of blindness per
card — placement, retroactivity, prior knowledge, retention, attribution, acquisition,
translation, selection — is what made the set worth eight cards instead of one.

That taxonomy is now the reusable part. It is a checklist for any detection tool this site
adds later: *which of these eight kinds of blind does it have?* Most tools have two, and the
one they do not advertise is usually the one worth writing down.

### Two additions that are load-bearing beyond their own card

- **Zeek's coverage question.** "What percentage of your hosts' traffic physically traverses
  this sensor?" — if nobody knows, that is the finding. It converts a vague unease into a
  number somebody has to go get.
- **Sigma's deployment test.** Fire the behaviour, confirm the rule alerts. Untested imported
  rules are the most convincing coverage theatre in the domain, because the rule count rises
  and the detection does not.

### The measurement

```
                          D1     D2     D3     D4
thin topics              279    271    263    255     ← eight, exactly, four times
blueteam                                 36 →  28  (67% → 52%)
mean chars/concept card 1,200  1,201  1,202  1,203    ← +1, every wave
```

Thirty-two cards, four waves, and the padding counter-metric has moved **three characters**.
The regularity is not luck: the discipline is that a deepening arrives as a *new concept card
with its own claim*, never as extra sentences inside an existing one, and a new card that says
something carries roughly the domain mean by construction.

Site **1,426 topics**. Smoke **138/138** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 8 wave D5: `web`, and the machine the code was written on

`web`'s bimodality had a cause, and finding it was most of the wave. The deep cards and the
thin cards are not separated by effort or by subject — they are separated by whether the card
ever met a real user. Every thin card describes its feature correctly from a fast laptop, on a
fast network, in one current browser, with no assistive technology attached and the dev server
on `localhost`. **The deep ones are the ones that had been to production.**

That made the D5 addition write itself: *the number your own machine cannot show you*, with a
hard requirement that every card name an instrument, a setting or a threshold.

| Card | The gap, and the instrument |
|---|---|
| Reflow & Jank | Your laptop is not the device that will jank — **DevTools CPU 4–6× slowdown**, 16.7 ms per frame, long tasks over 50 ms |
| Web Storage | The browser can refuse, and can take it back later — quota throws in private mode, ITP clears script-written storage, `localStorage` is synchronous |
| Core Web Vitals | **Lighthouse is a lab, your users are the field** — field decides *whether*, lab finds *why*; LCP 2.5 s / INP 200 ms / CLS 0.1, all at p75 |
| Fetch, REST & CORS | The dev proxy makes everything same-origin, so the first real preflight is made by a user; `credentials` plus wildcard origin is rejected outright |
| Modules & Bundlers | Bytes are what you measure, CPU time is what the user feels — Coverage panel for unused bytes, throttled trace for parse cost |
| Responsive Design | **Device mode resizes a window; it does not give you a finger** — 44×44 tap targets, `100dvh`, `env(safe-area-inset-*)`, 200% zoom |
| Accessibility | A clean automated scan is the floor — the two free manual passes are unplugging the mouse and turning the display off |
| Frontend Testing | `localhost` has no latency, and CI flake is the test finding out — a fixed `waitForTimeout` encodes a guess about speed |

### The instrument requirement is what kept this wave honest

"It's slower on phones" is exactly the padding Phase 8 §7 warns about: it reads like content,
costs the reader time, and leaves them with nothing to do. Requiring a named instrument killed
four drafts outright and forced the rest to be specific enough to act on this afternoon. It
also produced the wave's most useful single sentence, which is a dropdown: **CPU throttling in
DevTools is the cheapest device lab in existence.**

### The uncomfortable one

The accessibility card says a clean automated scan is the floor rather than the result — and
this repository's own `make a11y` reports **6/6 scans clean** on every commit in this phase.
Both things are true at once, and writing the card meant writing down that our own green check
proves the machine-checkable subset and nothing about focus order, alt text that says
`image1.png`, or colour used as the only signal. A check you rely on is the hardest thing to
describe the limits of, which is a reason to do it rather than a reason not to.

### The measurement

```
                          D1     D2     D3     D4     D5
thin topics              279    271    263    255    247   ← eight, exactly, five times
web                                            35 →  27  (85% → 66%)
mean chars/concept card 1,200  1,201  1,202  1,203  1,204
```

Forty cards, five waves, **four characters** of movement in the padding counter-metric. Phase
8 §8's target of "under 150 thin" is now 97 cards away — twelve more waves of this, which is
worth saying plainly rather than implying the end is near.

Site **1,426 topics**. Smoke **138/138** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 8 wave D6: `eng`, and why the management track was already good

The D6 diagnosis is the most transferable thing in this wave, and it is not about
architecture. `eng`'s management cards read well because **management writing has no option
but to be about trade-offs** — there is no way to describe *influence without authority* that
does not admit what it costs you. Architecture writing has that option, and the thin cards took
it: name the pattern, explain the mechanism, stop. That reads as endorsement, and endorsement is
how a four-person team ends up running a saga orchestrator.

| Pattern | The bill, and the threshold |
|---|---|
| Monolith vs Microservices | **The threshold is team count, not request rate.** One team at any traffic level should stay a monolith; several teams on one release train is the real signal |
| CQRS & Event Sourcing | An append-only log is a promise you cannot take back — erasure requests, schema versions you must read forever, replay time that grows with history |
| Domain-Driven Design | Without the domain expert it degrades into a folder layout. The cheap half — name things the way the business does — is worth doing everywhere |
| Clean / Hexagonal | **The adapter you never swap is pure overhead.** Ports pay at payment providers and third-party APIs; the database is not going to change |
| Saga & Outbox | Compensation is not rollback — a refund is not an un-charge, and every partial state needs a screen and a support answer |
| Resilience Patterns | Retries cause the outage they were added to survive. Three layers retrying three times is twenty-seven requests for one action |
| Event-Driven | You trade the stack trace for a correlation ID, and most brokers are at-least-once whatever the marketing says |
| SOLID | An interface with one implementation is a guess about the future. **Name the second implementation** before adding the abstraction |

### The threshold requirement, and what it rejected

Requiring a *number or a moment* rather than a caveat is what stopped this wave becoming eight
paragraphs about complexity. "It depends" hands the work back to the reader, which is precisely
what they came here to avoid. Three drafts were rewritten for having a bill and no threshold —
and the microservices card was rewritten twice, because the first version's threshold was
request rate, which is the wrong axis and the single most common way this decision is got
wrong.

The SOLID card is the one that changed shape most: it became a three-column table — the letter,
the failure when it is read as a rule, the use when it is read as pressure — because SOLID's
actual problem is not that the principles are wrong but that they are applied as law.

### The measurement

```
                          D1     D2     D3     D4     D5     D6
thin topics              279    271    263    255    247    239   ← eight, exactly, six times
eng                                                   33 →  25  (43% → 32%)
mean chars/concept card 1,200  1,201  1,202  1,203  1,204  1,205
```

Forty-eight cards, six waves, **five characters** of movement. One card per wave, on average,
is now being rewritten for failing its own spec's test rather than for being wrong — which is
the sign the specs are doing more work than the drafting.

Site **1,426 topics**. Smoke **138/138** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 8 wave D7: `devops`, and the seven-wave queue closes

D7's spec is the only one in the phase that assumes the decision has already been made.
D1–D6 all ask some version of *should you, and at what size* — D7 asks what happens after you
did. That distinction is the wave's whole content, because nothing in `devops` fails at
adoption. Every tool in the domain installs cleanly and demos well. They fail two years later,
quietly, in a shape decided by one choice made in week one.

| Tool | Two years in | The week-one decision |
|---|---|---|
| Helm & Kustomize | A chart nobody can diff | Render and diff in CI on every PR |
| GitHub Actions | Forty copy-pasted workflows, unpinned third-party actions | **Pin by commit SHA** — a tag is mutable |
| Secrets Management | Nothing can be rotated | Rotate one real secret in the first week and watch what breaks |
| Kubernetes Security | cluster-admin everywhere, flat network | **Default-deny NetworkPolicy before there is anything to break** |
| Policy as Code | Two hundred policies, all in audit | Ship every policy with an enforcement date in the same PR |
| CI/CD Pipeline | 45 minutes, so batches get bigger | Build time is a bug with an owner and a budget |
| Docker | An image nobody can rebuild, running as root | Pin the base by digest; add the `USER` line now |
| Platform Engineering | The platform team is the new ticket queue | A paved road, not a walled garden — there must be a way off it |

### The one test that made this spec work

*The preventive decision must be cheaper now than later.* If a fix is equally easy in year two,
there is nothing to warn about and the card is not a D7 card — it is advice, and advice with no
expiry date does not need a table. Two candidates were cut on exactly that: both were sensible
practices that could be adopted at any point, which meant the card had no reason to be about
time.

The item that best survives the test is the default-deny NetworkPolicy. In an empty namespace it
is one manifest. In a namespace with thirty running services it means discovering every
undocumented dependency simultaneously, under load — which is precisely why that ticket is open
in so many estates and closed in so few.

### The counter-metric moved two, and that is worth saying

```
                          D1     D2     D3     D4     D5     D6     D7
thin topics              279    271    263    255    247    239    231
devops                                                       20 →  12  (47% → 28%)
mean chars/concept card 1,200  1,201  1,202  1,203  1,204  1,205  1,207
```

Every previous wave moved the mean by exactly one. D7 moved it by two, because these cards
carry five-row tables *and* a substantial verdict, which is a slightly heavier shape than D3's
or D4's. It is still well inside noise, and it is recorded rather than smoothed over: the point
of a counter-metric is that you report it when it moves the wrong way, otherwise it is
decoration.

### The queue is finished; the phase is not

**Seven waves, 56 cards, 288 thin → 231.** §6's table is complete and every row is ticked. The
target in §8 was *under 150*, so the honest position is that the plan's queue got 40% of the way
there and 81 cards still stand between here and it.

> **Correction, made when the D8 census was actually run.** The sentence that followed this one
> said those 81 cards "live in the tail the table never named — `script`, `linux`, `ops`,
> `sec`". That was a guess and it was wrong. The census puts **184 of the 227 remaining thin
> cards inside the seven domains the queue already worked** — `data` 31, `redteam` 32, `cloud`
> 32, `blueteam` 28, `web` 25, `eng` 24, `devops` 12 — because each wave took eight and the
> domains were never finished. The unnamed tail is 43 cards, not 81. The queue's shape was
> right and its depth per domain was not.

Anyone writing a wave D8 should not extend this table by guessing. The census to run first:

| Question | Why it changes the answer |
|---|---|
| Which domains are thin *and* frequently visited? | Six waves were chosen by thin count alone. Thin-and-unread is the cheapest thing on this list to leave alone |
| Which thin topics are also **orphans**? | `orphan_report.py` already exists. A thin topic with no inbound link may want retiring rather than deepening |
| Which are thin because they are **reference**, like `shortcut`? | §4 excluded two domains by hand. That judgement should be a rule by now, not a list |
| Has the median moved, or only the mean? | The counter-metric watches the mean. A wave that deepened only the easiest cards would not show up in it |

The last of those is the real risk in what has just been done: seven waves each picked eight
cards, and *nothing forced them to be the eight hardest*. That is the honest limitation of this
phase, written down at the point where it is still cheap to fix.

Site **1,426 topics**. Smoke **138/138** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 10 T9: the pass found nothing, and the checker was why

T9 was scoped as ten minutes of work: `check_contradictions.py` already compares claims across
the site, so restrict it to the near-duplicate pairs and read what falls out. The restriction
went in as a `--pairs` mode reusing `near_duplicates.py`'s own topic splitter and title regexes
— deliberately importing them rather than growing a second splitter, because two splitters drift
and the pair check would then quietly compare the wrong text.

It reported **zero disagreements across 46 pairs**, first run.

Zero is the right answer and is indistinguishable from a check that cannot find anything. So,
per the rule this repo has now paid for five times, the next step was not to believe it.

### What the two proofs found

A `--self-test` with seven fixtures passed cleanly. That was not enough: fixtures test the
comparison, not the plumbing that feeds it. The second proof was to **inject a known
contradiction into a real pair** — `SSH on port 22` into one Zero Trust card, `SSH on port 2200`
into the other — and re-run.

It still reported zero. Two separate bugs, both in the checker, both older than T9:

| Bug | What it meant |
|---|---|
| The port regex keyed on the **first** capitalised word before `port`, not the nearest | `In this estate SSH on port 22` was recorded as a claim about a service called `IN`. Quieter on real prose, but this is why the site's port table listed CAPTURE, DEFAULT, PRIVACY and SECURE as services |
| `PRE_RE` strips `<pre>` and `<code>` — and the house style also writes code as **`div.code-block`** | Every shell sample written as a div has been read as prose by this checker since it was written. `# Default port 22` in a comment was a claim |

Both are fixed: the gap between service and port must now contain no other capitalised word, and
a nesting-aware `strip_code_divs()` removes the div form before anything else runs. A short
`NOT_SERVICE` list handles the residue — `Ticket-Based Authentication (port 88)` and `Web pages
use port 80/443` are not claims about services named AUTHENTICATION and WEB.

### The measurement

```
                        before   after
services keyed              27      15   ← 12 of the 27 were not services
of which real protocols     15      14   + BB, from a MAC address "AA:BB on port 1"
conflicts surfaced           0       1   ← DNS on 53 and 853, which is DNS-over-TLS
```

The conflict count going **up** is the point. The old table's zero was not a clean site; it was
a table so noisy that a real pair of ports could not surface in it. DNS on 53 and 853 is exactly
the legitimate case the tool's own text says to read rather than automate, and it is now visible
enough to read.

### What T9 actually delivered

Not a content fix — after the repairs, the pair pass still reports zero, and that zero now means
something. What it delivered is **two long-standing defects in a check that gates every build**,
found by taking its clean result seriously enough to disbelieve it. Nine fixtures now stand
guard, two of them regression tests written directly from the bugs.

The reusable rule, which is now stated as a rule rather than re-derived each time: **a new check
that passes on first run has not been tested. Fixtures prove the comparison; only injecting a
known-bad case into real data proves the plumbing.**

`make check` and CI both run `--self-test`, `--strict` and `--pairs --strict`.

---

## Session record — Phase 10 T5: there is no top three

T5's spec scored fixtures as *expected topic in the top three*. Writing the harness found the
first problem immediately: **there is no top three.** The search is substring matching over a
per-domain index and hands back an unordered `Set`; nothing ranks. Scoring against a ranking
that does not exist would have been the sixth check in this repo to measure something adjacent
to its claim, so the spec's scoring was dropped rather than faked.

What is actually true of an unranked result set is two things, and the harness measures both:

| Measure | Why it is the honest one |
|---|---|
| **Found** — the expected topic is in the hits | This is the regression test T5 was for. A renamed card or a reworded phrase breaks it |
| **Scan cost** — how many results the reader must read | With no ranking, result-set size *is* the quality metric. A per-fixture ceiling stops a query quietly widening to half the site |

### The bug the harness found on its first run

`"incident response"` returned **1,220 of 1,367 topics.**

The cause is a guard that covers half of what it needs to. `searchTerms()` looks the query up in
the acronym dictionary and adds what it finds — for "incident response", the alternate `IR`. Its
docstring says, correctly, that the *lookup* must be exact, "a substring match would make IP pull
in every expansion containing the word internet". But the alternate is then matched against topic
text with `text.includes("ir")`, which is true of *requires*, *first*, *third* and *directory*.
The lookup was guarded; the match was not.

Fixed with a `matcher()` that keeps substring behaviour for terms over four characters — typing
`kerber` should still find Kerberos — and requires word boundaries below that.

```
                       before   after
"incident response"     1,220      49
"mtu"                       5       3   ← two were "nmtui"
"dns"                     120     109
"kerberos"                 25      25   ← unchanged, as it should be
```

### The known misses are the deliverable, not a shortfall

Six queries a reader plausibly types return nothing, and the harness prints them every run
rather than hiding them:

| Query | Why it misses |
|---|---|
| `tcp handshake` | Two words that never appear adjacent on the site |
| `three way handshake` | The site writes it *three-way* |
| `wifi 6` | The site writes it *Wi-Fi 6*; only the hyphenated form matches |
| `why is my laptop slow` | A whole sentence, matched as one substring |
| `page loads halfway` | The MTU card says *half-loading* |
| `POAM` | The dictionary entry is now `POA&M`, and the map keys on that |

They gate nothing. Four of the six are the same root cause — **whole-string substring matching
has no notion of words** — which is the single largest available improvement to this site's
search and is a bigger change than a harness. Writing it down here is what makes it a decision
somebody takes rather than a thing nobody noticed. The harness also reports a miss that starts
working, so the backlog cannot quietly grow.

### Proved, not assumed

Same rule as T9, applied without needing to relearn it. 21/21 passing is exactly the result a
harness that cannot fail would produce, so: `one-way audio` was renamed out of `data/net.html`,
the page rebuilt, and the fixture went `FAIL … 0 result(s) — NOT FOUND`. Restored, and the run
returned to 21/21. That is the failure T5 exists to catch, demonstrated rather than asserted.

`make search` and a CI step run it. `make test` is unchanged at **138/138**.

---

## Session record — Phase 10 T6: reading time, and the two things it broke

T6 is the smallest item in Phase 10 and the one that broke the most. The feature itself is
twelve lines: `stamp_reading_time()` in `build.py` walks each topic, divides the plain-text
length by 1,000 characters a minute, stamps `data-read` on the `.topic` and renders a
`<span class="topic-read">` before the chevron. It shipped with the caveat the plan asked for
written next to the code rather than only here — **this is a proxy for length, not difficulty**,
and a dense 2,000-character card marked "2 min" is a small lie that a total absence of signal
would have been a larger one.

Then two checks that already existed caught two failures neither of which was in the feature.

### axe: 62 elements failing contrast, in both themes

The first CSS was `color: var(--muted); opacity: 0.75` — quieter than the badge on purpose,
since a size estimate should not compete with a title. `--muted` is already the quietest colour
in the palette that passes contrast, so dimming it to three-quarters put 62 elements under the
threshold in dark *and* light.

The fix is a deletion, and the comment left in `style.css` says why so nobody re-adds it:
**quieter than passing is not a design choice that exists.** If a thing must be visually
subordinate beyond what colour allows, the lever is size or position, not opacity.

### Search: `"min"` matched 1,337 of 1,367 topics

The search index is built by `plainText()` over the raw topic block, so anything *rendered* into
a topic is searchable — and the reading time is rendered into every one of them. One
build-time addition turned a common English word into a query that returns the entire site.

This is the same failure as T5's acronym-alternate bug, one day later and from the opposite
direction: there, a short *term* matched everything; here, a short *string in the content*
matched everything. `domainTopics()` now strips `.topic-read` before indexing, on the principle
that **chrome is not content** — the index should carry what an author wrote, never what the
build added.

```
"min"     1,337 → 27
"3 min"     359 → 4
```

### The check that should have caught it, added

T5's harness passed 21/21 through both of these, because every fixture asks *does this query
find its card* and neither bug broke a fixture's card. So T5 gained a second section:
**index hygiene** — a handful of strings that must stay narrow or return nothing at all.

The first attempt got it wrong in the way this repo keeps getting it wrong. `"class"` looked
like a markup probe and is not one: it is an English word, above the four-character substring
threshold, and it legitimately matches 275 topics through *classes*, *classic* and
*classification*. A ceiling that fails on correct behaviour teaches people to raise ceilings, so
it was replaced with strings that appear **only** in markup — `concept-desc`, `topic-header`,
`data-read` — each with a ceiling of zero.

`make search` is now **25/25**: 21 retrieval fixtures, 4 hygiene ceilings, 6 known misses
reported and gating nothing.

### What this item is really evidence of

Three separate checks — axe, the search harness, and the fixtures added because the harness did
not catch it — each caught something a twelve-line feature broke somewhere else entirely. None
of them was written for this feature. That is the argument for the checks being where the
investment goes: the cost of adding a small visible thing to 1,426 cards is not in writing it.

Site **1,426 topics**. Check PASS · smoke **138/138** · search **25/25** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 10 T7: three honest levels beat three invented ones

T7 asked for `data-level` with three values, "stamped from the badge where one exists and by
hand elsewhere". The first half is mechanical. **The second half is where the item would have
gone wrong**, and it was not done as written.

Hand-labelling the difficulty of 1,300 cards in one pass does not produce an assessment; it
produces a confident-looking attribute that nobody actually evaluated, on a site whose whole
argument is that its claims are checkable. So the rule stamps only what the badge says and
labels the rest `core` — which is a statement that **the card is not marked as either**, not a
claim that it sits in the middle:

```
core      1,297
beginner    121   ← badge contains "Beginner"
advanced      8   ← badge contains "Advanced", "Expert" or "Deep"
```

Eight advanced cards is a thin layer and it is reported as eight rather than padded out.
`level:beginner` is the filter that carries this item; `level:advanced` is a byproduct that is
honest about how small it is.

### An operator, not a chip

The plan implied a filter control. It shipped as a search operator instead — `level:beginner`,
composing with `domain:` and with free text — for three reasons, in descending order of weight:

| Reason | |
|---|---|
| It composes | `level:beginner domain:net` is ten cards, and no chip design gives you that intersection without a second row of controls |
| The filter bar is full | Thirty domain chips in four labelled groups. A level control would either crowd it or hide below the fold, and `visual_test.mjs` pixel-diffs that bar for exactly this reason |
| It lands where readers already look | `domain:` is documented in the search box's own tooltip. `level:` is now on the line beneath it, in the same place, learned the same way |

An unknown level yields no matches rather than being silently ignored — the same rule
`domain:` follows, and for the same reason: quietly dropping an operator answers a different
question than the one asked. `level:nonsense` is a search-harness fixture with a ceiling of zero
so it stays that way.

### What T6 made possible here

T7 took about a third of the effort it would have a day earlier, because T6 had already
established the pattern: a build-time pass that walks topics, derives something from the block,
and stamps an attribute on the `.topic`. `stamp_level()` is `stamp_reading_time()` with a
different derivation, and `domainTopics()` already had the shape for indexing an attribute off
the open tag. Two reader-facing features, one mechanism.

`make search` is now **28/28** — 23 retrieval fixtures, 5 hygiene ceilings.

Site **1,426 topics**. Check PASS · smoke **138/138** · search **28/28** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 10 T8: what changed *for me*, and Phase 10 closes

T8 needed no new data, exactly as the plan predicted, but not from the source it named. The
changelog holds only each domain's most recent month and at most three topic ids — enough for
the "Updated" row on a domain intro card, far too little for a per-reader diff. The data that
was already sufficient is **`data-reviewed`, which every one of the 1,426 topics carries**.
`domainTopics()` now indexes it off the open tag, exactly as it indexes T7's `data-level`.

### The operator is the feature; the banner is the doorway

```
since:2026-06                 → everything reviewed after June 2026
since:2026-07 domain:net      → 31 topics
since:2099-01                 → nothing, and a harness fixture pins it there
```

`since:` is *strictly after*, because that is what the English word means and it is what the
banner needs — it passes the last month this reader acknowledged and wants what landed
afterwards. Month strings compare correctly as strings because they are zero-padded, so the
whole comparison is `t.reviewed > q.since`.

The banner does not have a private code path. "Show them" **puts the query in the search box
and runs it**, so the reader can see it, edit it, add `domain:` to it, or clear it with Esc like
any other search. A feature that produces a view you cannot reach any other way is a feature you
have to maintain twice.

### The behaviour most likely to have been got wrong

A reader with nothing stored must be told **nothing**. Every topic is new to them, the statement
is useless, and a banner that opens by saying "1,426 topics updated" teaches people to dismiss
it before it ever says anything worth reading. So a first visit records the newest month
silently and shows no banner.

That is the first of four new smoke checks, and it is the one worth having:

```
ok : a first-time reader is not told the whole site is new       — hidden true, stored 2026-08
ok : a returning reader is told how many topics changed          — 1367 topics updated since June 2026
ok : 'show them' puts an editable query in the search box        — since:2026-06
ok : 'mark as seen' advances the stored month and hides the banner — stored 2026-08
```

Every `localStorage` access is inside `try/catch` and the banner simply never appears when
storage throws — a private window must not be a broken page.

### Phase 10 is complete

Nine items, all shipped, and the pattern across them is worth stating once. **Five of the nine
found a defect in something other than themselves**: T2's own first version measured the wrong
thing; T9 found two long-standing bugs in the checker it was extending; T5 found a query
returning 90% of the site; T6 broke contrast and the search index and was caught by axe and by
T5's harness; T8 was clean only because T6 and T7 had already paid for the mechanism it used.

The tooling items were justified as making the content phases honest. What they actually did as
often was catch each other.

| Item | | Shipped as |
|---|---|---|
| T1 | depth report | `tools/depth_report.py` — thin count and the padding counter-metric |
| T2 | near-duplicates | `tools/near_duplicates.py` — census, and a `--title` pre-flight |
| T3 | verdict check | A ceiling in `lint_content.py`, ratcheted |
| T4 | orphan report | `tools/orphan_report.py` |
| T5 | search harness | `tools/search_test.mjs` — 25 checks, 6 known misses |
| T6 | reading time | `data-read` and a header span |
| T7 | difficulty | `data-level` and the `level:` operator |
| T8 | new since last visit | The banner and the `since:` operator |
| T9 | contradiction pass | `--pairs` and `--self-test` in `check_contradictions.py` |

Site **1,426 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 9 wave C3, and the pair the report could not see

C3 was flagged in the queue as the ambiguous wave — `shortcut` is a reference domain, so §3's
*reference-plus-concept* exemption was expected to cover most of it. That expectation held for
four of the five and was wrong about the rest in a way worth writing down.

### The two merges

| Retired | Into | Why the §3 test said consolidate |
|---|---|---|
| `script` **PowerShell — Windows Automation** | `script` **PowerShell — Scripting Reference** | Both single-card references, same domain, 13 of 17 cmdlets shared. "Who is this for?" produces the identical sentence twice |
| `shortcut` **Git Power User — Beyond add, commit, push** | `script` **Git Advanced Workflows – Beyond add, commit, push** | Same five subjects (stash, interactive rebase, reflog, bisect) and **the same subtitle**. Not a reference card: five prose concept cards, so the §3 exemption does not apply |

Both absorbed first and verified before anything was retired, per the rule this phase learned
the hard way. The PowerShell survivor gained discovery (`Get-Command`, `Get-Help`,
`Get-Member`), `try`/`catch`, execution policy and WinRM remoting — none of which it had. The
Git survivor gained 17 commands it lacked: `blame`, `log --grep/--author/-S`, `show`, `diff`,
and the whole undo group (`restore`, `commit --amend`, `reset --soft/--mixed/--hard`, `revert`,
`rebase --continue/--abort`).

### The finding: title overlap is a proxy, and here it failed

The two `script` PowerShell cards are the clearest duplicate in this wave. `near_duplicates.py`
scores them **0.25** — nowhere near the 0.50 floor — because their titles diverge:

```
"PowerShell — Scripting Reference"    → {powershell, scripting}
"PowerShell — Windows Automation"     → {powershell, window, automation}
                                        overlap 0.25
```

Both were reachable only because each scored ≥ 0.50 against a *third* card in `shortcut`, which
is how they came to be read side by side at all. **The pair that mattered most was found by
accident.**

That is a real limitation of the measurement, not a bug in it. §6 justified the tool as
"tokenise titles, compare pairwise, report above a threshold" and titles are what the tool has.
Content-similarity comparison over 1,365 topics is a different and much larger tool, and this
file's standing rule is not to ship a measurement whose cost it has not counted. So the
limitation is recorded here rather than papered over: **C3's real lesson is that the census
finds duplicated *titles*, and duplicated *cards* are a superset of that.**

### The tool gap that would have blocked wave C4 entirely

`retire_topic.py` located both topics in one domain. The Git merge is `shortcut` → `script`,
and it simply could not run — and **C4 is Kubernetes across `devops` and `linux`**, so the next
wave in the queue was blocked by the same limitation.

`--into-domain` fixes it in four lines. Ids are unique site-wide, so nothing else in the tool
cared which file the survivor came from; only `locate()` did.

### The four refusals, each with the sentence that saved it

| Pair | Verdict |
|---|---|
| `shortcut` *tmux — Never Lose a Session Again* · `shortcut` *Tmux Survival Kit* | **Keep both.** One is badged `SHORTCUTS • Productivity` and is a keybinding reference; the other is badged `Beginner` and teaches sessions/windows/panes. §3's first row, exactly |
| `script` *PowerShell — Scripting Reference* · `shortcut` *PowerShell — Windows (and Cross-Platform) Scripting* | **Keep both.** The shortcut card opens with *Why PowerShell Replaced Command Prompt* — it is for someone who has never used it. The reference is for someone who has |
| `shortcut` *VS Code* · `shortcut` *VS Code — Debugging* | **Keep both.** A keybinding table and a `launch.json` how-to. A title artefact: "VS Code" is the entire first title, so containment is trivially high |
| `shortcut` *Windows* · `endpoint` *Windows Administration Fundamentals* | **Keep both.** Same artefact, one shared token, two unrelated cards |

Three of the four refusals are one-token titles scoring high for structural reasons. That is
worth knowing about the census: **short titles inflate overlap**, and a `shortcut` domain full
of one-word titles will keep producing these.

```
topics       1,426 → 1,424
pairs ≥ 0.50    46 → 44
aliases        109 → 111
```

Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 9 wave C4: the answer was a move, and a merge would have been wrong

C4's single pair scores **1.00** — the highest on the site — and merging it would have been a
mistake. That is worth more than the pair itself, because 1.00 is exactly the score that
invites acting without reading.

```
1.00  [devops] Kubernetes – Container Orchestration Fundamentals   Beginner, 5 concept cards
      [linux]  Kubernetes — Container Orchestration Reference      DEVOPS · CLOUD, 1 reference card
```

Both of §3's exemptions apply at once: **a Beginner card beside a deep card**, and **a reference
card beside a concept card**. The titles are near-identical because both describe the same
subject correctly; the cards are not the same card. §3's test — one sentence saying who each is
for — gives two different sentences immediately.

### So what *was* wrong

The queue's own note guessed it: *"which domain owns the subject. Probably `devops`, with
`linux` keeping a container-internals card that is genuinely its own."* The domain census
confirms it exactly:

| Domain | What it owns |
|---|---|
| `linux` | Docker, Podman & rootless, **Under the Hood — Namespaces & cgroups**, **Container Internals** — the layer beneath the orchestrator |
| `devops` | Kubernetes Fundamentals, Objects, Networking & Storage, Helm & Kustomize, Secrets — five cards on the orchestrator |

A Kubernetes *reference* was the only Kubernetes card outside `devops`, in the domain that owns
everything **under** containers rather than above them. So it moved.

### A move is cheaper than a merge, and this file has not said so before

Topic ids are `slugify(title)`, so a card that changes domain **keeps its id**. That means:

| Cost of a merge | Cost of this move |
|---|---|
| The retired permalink dies; `slug-aliases.json` grows | Nothing — the id is unchanged |
| Five `localStorage` prefixes orphan | Nothing — same id, same keys |
| Related edges and path steps break | Nothing — both are keyed by id, and neither records a domain |
| Content has to be absorbed and verified first | Nothing — the card moves whole |

**Where §3 says keep both and the cards are in the wrong places, move them.** That option was
not in §4's cost table and belongs there: it is the correct answer whenever the duplication is
apparent rather than real, and it costs nothing at all. `check_paths.py`,
`suggest_related.py --check` and all 142 smoke checks pass unchanged, which is the evidence.

What `devops` gained is also a real content win rather than bookkeeping: the reference card
carries **13 `kubectl` verbs** — `get`, `describe`, `logs`, `exec`, `apply`, `delete`,
`rollout`, `scale`, `top`, `port-forward`, `config`, `cluster-info` — and the domain's five
existing Kubernetes cards had `kubectl apply` between them.

```
topics    1,424 (unchanged — a move creates and destroys nothing)
devops       43 → 44
linux        57 → 56
pairs        44 (the pair remains, and is now correctly a keep-both)
```

Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 9 wave C5, where deduplication and deepening turn out to be the same work

C5 was billed as "small and clean" and was, but it connects two phases that this file has kept
apart. **Both `web` cards retired here were on Phase 8's thin list**: *WebAssembly — Native
Speed in the Browser* (1,292 plain chars, one concept card) and *TypeScript — Types for
JavaScript* (1,345, one card). Each duplicated a `script` card four to five times its size.

| Retired | Into | Ratio |
|---|---|---|
| `web` **WebAssembly — Native Speed in the Browser** | `script` **WebAssembly (WASM) — Near-Native Speed in the Browser** | 1,990 → 4,815 chars |
| `web` **TypeScript — Types for JavaScript** | `script` **TypeScript — JavaScript That Scales** | 2,343 → 9,094 chars |

That is worth stating as a general observation rather than a coincidence, because it changes
how the two phases should be sequenced:

> **A thin card is a duplicate-shaped thing.** Both of these were written by a session that
> covered a subject an earlier session had already covered *properly*, and produced a summary
> of it. The thin card and the near-duplicate card are frequently the same card, and Phase 8's
> census is therefore a second lens on Phase 9's population.

The practical consequence: a wave D8 should cross-reference `depth_report.py --thin` against
`near_duplicates.py` **before** deepening anything. Deepening a card that ought to be retired is
the most expensive mistake available in either phase.

### What was absorbed, and what was already there

The discipline held and mostly found that the survivors were complete. TypeScript's survivor
already covered erasure at runtime, `any`, `strict` and narrowing — the `web` card's entire
content bar one idea. So the absorptions were small and precise rather than wholesale:

- **WASM** gained the boundary cost — *a hot loop calling back into JavaScript every iteration
  can be slower than the JavaScript it replaced* — and the server-side framing: WASI as a
  sandbox for running somebody else's code without giving it your process.
- **TypeScript** gained a verdict it did not have at all. Its last block was a bare table, which
  the linter's `table with no verdict` counter had been counting for months. The `web` card's
  framing supplied it: the payoff people feel is not caught bugs, it is **fearless refactoring**.

That second one is a merge improving the survivor's structure rather than only its content,
which is the best case for this phase and is not the usual one.

### The refusal

`sec` **Zero Trust — Never Trust, Always Verify** (badge `SEC • Architecture`, 5 cards) against
`sec` **Zero Trust – "Never Trust, Always Verify" Explained Simply** (badge **Beginner**, 4
cards), at 0.83 overlap. §3's first row, unambiguously: **keep both.** The near-identical titles
are two sessions naming the same idea correctly, and the badges say plainly who each is for.

### Two related edges repointed, which is the guard doing its job again

`retire_topic.py` refused both merges on first attempt — `how-the-browser-renders-a-page →
webassembly-native-speed-in-the-browser` and `prototypes-modern-classes →
typescript-types-for-javascript`. Repointed at the survivors, and `suggest_related.py --check`
reports **882 links, 0 one-way** afterwards. Third real use of that guard, third time it named
something that would have broken silently.

```
topics       1,424 → 1,422
thin           231 → 229    ← two of them left by retirement, not by deepening
pairs ≥ 0.50    44 → 42
aliases        111 → 113
```

Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 9 wave C6: the tail, and the ninth wrong acronym

C6 was scoped as *"audit, expect to keep most"* and that expectation was correct. The wave's
value is not in its two merges; it is in what auditing forty pairs turned up on the way.

### The two merges, both found by C5's rule

C5's finding was that **a thin card is a duplicate-shaped thing**, so this wave started by
cross-referencing `depth_report.py --thin` against `near_duplicates.py` rather than reading the
list top-down. Six of forty pairs had a thin side. Two were real:

| Retired | Into | What was absorbed |
|---|---|---|
| `eng` **Testing Strategy — The Test Pyramid** (1 card) | `script` **Testing Strategy — Why and How to Test** (4 cards) | BDD and *given/when/then* — the survivor already had the pyramid, TDD, the ice-cream cone, and "test behaviour not implementation" |
| `data` **Vector Databases — Embeddings & Similarity Search** (1 card) | `ai` **Vector Databases — Similarity Search at Scale** (4 cards) | **Nothing.** The survivor already covered pgvector, hybrid search, HNSW/IVF, cosine and the vendor list |

That second row is the cleanest possible case for this phase: a card whose entire content
already existed, better, one domain away — and whose own text said *"Direct bridge to the AI
domain's RAG cards"*, which is a card describing itself as a pointer.

### The ninth wrong acronym expansion, and why nothing could have caught it

Reading both Vector Databases cards side by side surfaced this, in both of them:

```
ANN (Artificial Neural Network) index    HNSW/IVF — approximate nearest-neighbor for speed
```

**The row states the correct expansion in its own second column** and the annotator stamped the
wrong one beside it. In a vector database, ANN is *Approximate Nearest Neighbour*. The
dictionary held one meaning, the neural-network one, so every use on the site was annotated
wrong — and there were exactly two uses, both in this sense.

No check on this site could have found it. `check_contradictions.py` compares hand-written
expansions against the dictionary; this expansion *came from* the dictionary. The
`--pairs` mode compares two cards' claims; both cards agreed, and both were wrong. **A
dictionary with one meaning cannot disagree with itself**, which is the shape of this whole
class of error and the reason all nine were found by reading rather than by tooling.

Fixed as a multi-meaning entry with `byDomain` for `ai` and `data`. The residual risk is
recorded rather than hidden: if a future `ai` card writes ANN meaning a neural network, it will
now be annotated wrong in the other direction. Every current use is the vector sense, and the
neural-network cards spell the words out.

### The refusal that became a link

`data` **ER Modeling — Designing the Schema** and `data` **Designing a Schema From
Requirements** score 0.50, and one is thin — which by this wave's own rule made it a merge
candidate. Reading them says otherwise: one is entities, relationships and cardinality; the
other is a six-step walkthrough from *"we sell stuff"* to tables, ending on the price-snapshot
insight. Theory and process, two different sentences, **keep both**.

So the constructive action was a related edge in both directions rather than a merge. That is
worth naming as a third outcome alongside *merge* and *move*: **when two cards are genuinely
adjacent rather than duplicated, link them.** A reader who lands on the theory should be one
click from the walkthrough, and the near-duplicate census is a good place to find pairs that
deserve an edge.

### Phase 9's queue is complete

| Wave | Merged | Refused |
|---|---|---|
| C1 `script` internal | 4 | 4 |
| C2 `net` wireless and cloud | 2 | — |
| C3 `script`↔`shortcut` | 2 | 4 |
| C4 Kubernetes cross-domain | 0 (**1 moved**) | 1 |
| C5 Zero Trust, WASM, TypeScript | 2 | 1 |
| C6 the tail | 2 | the rest, one of them **linked** |

**12 merges, one move, one new link, and roughly a dozen documented refusals.** §5 estimated
"about 23 merges, of which perhaps 15 are unambiguous". The real number is half that, and the
gap is the point: **the estimate was made from titles, and titles overstate duplication.**
Every refusal above was a pair whose titles matched and whose cards did not — a beginner card
beside a deep one, a reference beside a concept, a one-word `shortcut` title inflating overlap,
theory beside a walkthrough.

```
topics       1,426 → 1,420   (six retired across C3–C6, one moved)
thin           231 → 227     (four of them left by retirement)
pairs ≥ 0.50    46 → 40
aliases        109 → 115
```

Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2** · related **882 links, 0 one-way**.

---

## Session record — Phase 8 wave D8: the domain where mistakes do not raise errors

D8 is the first wave chosen by census rather than by the queue, and the census sent it back to
where D1 started. `data` was still the worst ratio on the site at 74%, because D1 took eight
cards out of forty and stopped — which is the finding that corrected Phase 8's closing record
higher up this file.

The spec is the sharpest one in the phase, and it is specific to this domain in a way the others
were not:

> **Everywhere else on this site, a mistake produces an error.** A misconfigured sensor logs
> nothing; a bad Dockerfile fails to build; a wrong subnet mask drops the packet. In a database,
> the common failure is a query that runs to completion, returns a plausible number, and is
> wrong.

| Card | The silent wrong answer |
|---|---|
| SQL Joins | A `WHERE` on the right-hand table turns a LEFT JOIN back into an INNER JOIN — **filters on the right belong in `ON`** |
| Aggregation | Join first, aggregate second, and `SUM` cannot tell. Two one-to-many joins multiply by the *product* |
| Window Functions | The default frame is `RANGE`, so tied rows all get the total *after* all of them. Write `ROWS` explicitly |
| Subqueries & EXISTS | **`NOT IN` against a subquery holding one NULL returns zero rows.** Use `NOT EXISTS` and never have to know |
| ACID & Transactions | Read-modify-write loses an update at `READ COMMITTED`, which is the default in three of the big four |
| Reading Query Plans | `EXPLAIN` prints the estimate that *was* the mistake. The finding is the largest estimated-to-actual ratio |
| Indexes | A `UNIQUE` index does not stop duplicate NULLs — every constraint in SQL has a NULL-shaped hole |
| Time-Series | Yesterday's number changes when late events arrive, and nobody reruns the report |

### The second half of the spec did the work

*Name the silent wrong answer, and say how you would notice.* The detection clause is what
separates these from folklore, and writing it forced each card to be concrete:

- Joins — run it without the `WHERE` and compare row counts; if the filter drops you to exactly
  the inner-join count, the `LEFT` is decorative.
- Aggregation — aggregate the fact table alone and compare totals.
- Window functions — look for identical consecutive running totals on rows with different
  amounts.
- Indexes — `SELECT COUNT(*) FROM t WHERE email IS NULL`, one query, on any nullable column you
  believed was unique.
- Time-series — recompute a week-old day and compare it to what was reported at the time.

**ACID is the honest exception and says so**: you usually do *not* notice, which is precisely
why it is the entry worth remembering. A card that claimed a detection there would have been
inventing one.

### The median's first reading

```
                        before   after
thin topics                227     219
data                 31 (74%)  23 (55%)
mean chars/card          1,207   1,209
median topic             2,948   2,965      ← +17
10th percentile          1,362   1,364      ← +2
```

The new metric behaves exactly as it should and the reading needs stating plainly: **eight cards
out of 1,420 cannot move a median far.** Seventeen characters is the arithmetic, not a
disappointment. What the number is for is the shape over many waves — a programme that only ever
deepened easy cards would hold the median flat while the thin count fell, and that divergence is
visible over ten waves and invisible over one.

The 10th percentile moving by two is the more interesting reading: cards leaving the bottom
decile are replaced by the next ones up, so **the floor barely rises until the tail is genuinely
worked**. That is the number to watch, and it is the number this phase has least right to feel
good about yet.

Site **1,420 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 8 wave D9: the card the reader cannot recognise

D5 worked `web`'s tooling and performance cards. What was left was the fundamentals —
closures, prototypes, events, promises, Flexbox, Grid, custom properties, the render pipeline —
and they were thin for a reason none of the earlier specs would have caught.

**Nobody reads a closures card out of curiosity.** They read it because a loop printed the same
number five times. The thin fundamentals cards explain the mechanism correctly and never name
the symptom, which means the reader who needs the card most has no way to tell that this is the
card. The page is searchable by cause and the reader only has the effect.

| Card | The symptom, in the words used before the cause is known |
|---|---|
| Closures, Scope & `this` | The loop printed `5` five times; `this` went undefined when the method was passed somewhere |
| Prototypes & Modern Classes | It worked as `obj.method()` and broke as `setTimeout(obj.method)` |
| The DOM & Events | The click handler works, until the row was added after page load |
| Async Deep | **`forEach` returned immediately and nothing was saved**; thirty `await`s took thirty seconds |
| Flexbox | The flex item refuses to shrink and pushes the page wider than the screen |
| CSS Grid | One long word blows a `1fr` column out past its share |
| Modern CSS | A `var()` fallback did not apply, and the property came out `unset` |
| How the Browser Renders a Page | The text jumps when the font loads; the page is blank until the CSS arrives |

### The test that kept this honest

*The symptom has to be recognisable without knowing the answer.* That rejected four first
drafts, all of which had written the symptom from the far side of the explanation — "you have
misunderstood the event loop" describes a reader who already knows what is wrong. It is
surprisingly hard to write, because by the time you can explain a bug you have forgotten what it
looked like before you could.

The best evidence the constraint worked: **two pairs of cards turned out to share a root
cause**, and neither would have surfaced without symptom-first writing. Flexbox's
`min-width: auto` and Grid's `minmax(auto, 1fr)` are the same rule in two syntaxes, and both
cards now say so explicitly:

> `minmax(0, 1fr)` in Grid is `min-width: 0` in Flexbox. Both exist because both layout models
> default to "never smaller than the content" — the right default for text, the wrong one for
> anything that can be arbitrarily wide.

And Closures and Prototypes both produce the same "`this` is undefined" error from two different
directions, which is exactly why it confuses people: the two cards now separate *a closure
captures the variable, not its value* from *`this` is supplied by the call, not the definition*.

### The measurement

```
                        D8 end   D9 end
thin topics                219      211
web                                25 →  17   (64% → 44%)
mean chars/concept card  1,209    1,210
median topic             2,965    2,996      ← +31, the largest move yet
10th percentile          1,364    1,365      ← +1
```

The median moved 31 this wave against 17 last, because `web`'s fundamentals cards were sitting
just below it rather than at the very bottom — deepening a card at the 55th percentile does more
to the median than deepening one at the 5th. **The 10th percentile moved by one**, which
continues to be the honest number: nine waves in, the actual floor of this site has not moved,
and it will not until a wave deliberately targets the shortest cards rather than the ones with
the most to say.

That is now a named commitment rather than an observation: **D10 goes to the bottom decile by
character count, across whatever domains it falls in.**

> **Retracted the same session, after actually looking.** `depth_report.py --bottom` was written
> to execute this commitment and immediately showed it was the wrong target. The bottom decile
> is not underdeveloped content: **64 of its 132 cards carry a badge that means deliberately
> short** — `Beginner • Core`, `Linux+ • CLI`, `PenTest+ • Recon`, `Military • Reference`. They
> are the beginner layer §3 of Phase 9 exists to protect, and the per-certification objective
> skims. Deepening them would make the beginner cards stop being beginner cards and the syllabus
> skims stop being skims. See the D10 record below.

Site **1,420 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 8 wave D10: the wave that did not happen, and the metric that hid why

D9 ended with a commitment: *the 10th percentile has moved three characters in nine waves, so
D10 goes to the bottom decile by character count.* Executing that commitment needed a tool that
did not exist — every existing mode of `depth_report.py` answers "which cards are **thin**",
and thin is `one concept card AND under 1,800 characters`. So `--bottom` was written, listing
the shortest topics regardless of card count.

It answered the question in one screen, and the answer was that the commitment was wrong.

```
   317 · 0 card(s)  military   Common Codes Decoded              [Military • Reference]
   443 · 1 card(s)  linux      Package Management                [Linux+ • Distros]
   458 · 2 card(s)  linux      File Ops & Text Processing        [Linux+ • CLI]
   475 · 1 card(s)  military   Staff Functions 1–9               [Military • Sections]
   636 · 2 card(s)  script     Scope — Where Variables Live      [Beginner • Core]
   710 · 2 card(s)  pentest    Web, Wireless & Reporting         [PenTest+ • Specialized]

64 of the 132 in the bottom decile carry a badge that means deliberately short.
```

**The bottom of this site is not underdeveloped. It is two things that are supposed to be
short**: the beginner layer that Phase 9 §3 exists to protect, and per-certification objective
skims — a Linux+ candidate wants six package managers in a table, not an essay on repository
signing. Deepening either would destroy the thing that makes it useful. The 10th percentile has
not moved in nine waves because **nothing should have moved it.**

### Two measurement failures, and only one of them was known

The first was already suspected: nine waves picked eight cards each and nothing forced them to
be the hardest. True, and it turns out not to be the interesting one.

The second was invisible until `--bottom` existed. **The thin metric's `cc <= 1` clause means a
458-character topic with two concept cards is not thin.** Of the 24 shortest topics on the site,
**21 were never counted by the measurement that has driven ten waves of work.** T1's census
answers "which cards are one card and short", and that has been silently standing in for "which
cards are short" since Phase 8 began.

That is not a reason to change the thin definition — a single-concept card genuinely is the
signal that a subject was covered once and left — but it is a reason for the report to carry
both numbers and say which is which. `--bottom` now does, and it marks the deliberate ones with
a `·` so nobody re-derives this finding in three months.

### What this says about the phase's target

Phase 8 §8 wants "under 150 thin". At 211 that is 61 cards, or roughly eight more waves. What
D10 establishes is that **the target should be read as a ceiling on genuinely thin cards, not as
a claim about the site's floor** — and that the floor, measured honestly, is where it should be.
A future session that sees "10th percentile: 1,365" and decides to attack it should read this
record first.

### D10 therefore ships tooling and a correction, and the wave moves on

No content was deepened under this heading, which is the right outcome and is recorded as such
rather than being quietly replaced with an easier wave under the same name. The next content
wave takes the worst remaining ratio in a domain with no deliberate-short population:
**`redteam`, 32 thin of 52.**

`--bottom` is in `make census`. Nothing else changed.

---

## Session record — Phase 8 wave D11: a catalogue of tools is not an attack path

D2 gave `redteam`'s tool cards *what using this costs you*. Thirty-two were left, and they shared
a second gap that matters more to someone learning the subject: **every card was written as
though you could simply run the tool.**

You cannot. Mimikatz is not the start of an attack, it is what you do after you have already won
on a host. Hashcat needs the hash, and stealing the hash was the hard part. Impacket assumes you
are already somebody. Without the precondition, a catalogue of capabilities stands in for what is
actually a chain — and the chain is the part the tool's own documentation never supplies.

| Tool | What you must already have | The control that denies it |
|---|---|---|
| Mimikatz | Local admin **and** `SeDebugPrivilege`, with LSASS readable | Credential Guard and RunAsPPL remove the technique, not just detect it |
| BloodHound | **Any authenticated domain user** | None — and that is the finding |
| Impacket | A credential or hash, plus reach to 445/135 | LAPS kills the reuse; a host firewall kills the reach |
| Kerberos Attacks | A domain user plus an account configured badly | gMSA and required pre-auth, both settings changes |
| Hashcat | The hash, already stolen — and its algorithm decides everything | Length beats complexity; the KDF beats both |
| Pacu | Valid AWS credentials, usually a long-lived key | Do not issue them; require IMDSv2 |
| ADCS Abuse | A domain user and one unreviewed template | An ACL and a checkbox, set once during a migration |
| Living off the Land | Code execution, and nothing else | The emptiest prerequisite, and therefore the hardest |

### The test the spec needed

*The prerequisite must be specific enough to be denied.* "Access to the network" is not a
prerequisite. "A credential or NTLM hash, plus reachability to 445" is, because a defender can
act on each half separately — and it turns out that the second half, **blocking
workstation-to-workstation SMB at the host firewall**, is the single cheapest row in the whole
wave. Nothing legitimate needs it.

### The two cards that came out differently from the other six

**BloodHound has no control.** Its precondition is a normal user account, Active Directory is
readable by design, and no setting takes that away. The card had to say so, and then say what
follows: this is the one entry in the domain where the defensive answer is to *run the tool
yourself, first, and keep running it* — because the attack paths were already there and the win
is deleting them, not detecting the enumeration.

**ADCS behaves unlike everything else after the incident.** A certificate outlives a password
reset. Rotating credentials does not revoke a certificate an attacker already holds, and the
validity can be years — so the response order inverts: find the templates, then check what has
already been issued, and be prepared to revoke rather than reset.

Both were discovered by applying the spec rather than by knowing them in advance, which is the
argument for writing the spec before the cards. Six of eight produced a tidy precondition-and-
control pair; the two that refused to are the two worth reading.

### The measurement

```
                        D9 end  D10   D11 end
thin topics                211  211       203
redteam                             32 →   24   (62% → 46%)
mean chars/concept card  1,210  —       1,212
median topic             2,996  —       3,014    ← crosses 3,000
10th percentile          1,365  —       1,365    ← unchanged, and now expected to be
```

Eighty-eight cards across eleven waves, and the padding counter-metric has moved **twelve
characters in total**. The 10th percentile did not move and D10 established that it should not:
the floor of this site is the beginner layer and the certification skims, and both are the right
length already.

Site **1,420 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 8 wave D12: the wave that inverts D3's own rule

D3's rule for `cloud` was **provider-neutral**, and it was right for the cards it covered: cost
control, landing zones, CSPM, Terraform. Those are concept cards, and a service description
dated on the day it was written is the thing on this site most certain to rot.

D12 covers the other thirty-two, and they are the opposite kind of card. They come in matched
pairs — AWS IAM and GCP IAM, AWS VPC and GCP VPC, AWS KMS and GCP KMS — and for them **the
provider is the subject**. Writing those provider-neutral would be writing nothing at all. So
this wave inverts the earlier rule on purpose, and the two rules are compatible because they
apply to different kinds of card. That distinction is now written into the spec rather than
being something a later session has to infer from a contradiction.

| Card | The assumption that breaks on arrival |
|---|---|
| GCP IAM | **You cannot attach a policy to an identity.** You bind a role to a principal *on a resource*, and inheritance is additive |
| AWS IAM Deep | A permission can be granted and still denied — five policy types evaluate, and one explicit `Deny` ends it |
| GCP VPC | The VPC is **global**; subnets are regional; firewall rules are network-wide, priority-ordered, and have denies |
| AWS VPC | Everything is AZ-scoped, and **a subnet is public only because its route table says so** |
| GCP Service Accounts | A service account is an identity *and* a resource — `serviceAccountTokenCreator` is impersonation |
| AWS KMS | The key policy is the authority; the default one delegates to IAM, and a custom one may not |
| GCP Load Balancing | One global anycast IP, and health checks arrive from `35.191.0.0/16` and `130.211.0.0/22` |
| AWS Observability | Logs and Metrics are separate products, and custom metrics bill per metric per month |

### The test, and what it threw out

*The difference has to be structural, not a naming difference.* "AWS calls it a Security Group
and GCP calls it a firewall rule" is a glossary entry and was cut twice. What survives is where
the two designs disagree at the root — global versus regional networks, additive-allow versus
explicit-deny evaluation, resource-policy versus identity-policy authority.

The clearest example of why this matters is the pair of network cards. Translating a design in
either direction is not rewording: a GCP design that assumed global reach and tag-targeted rules
becomes, in AWS, peering connections, per-subnet route tables and per-instance groups. **The
provider decides how many boundaries the design has**, which is a thing to know before choosing
one rather than after.

### Two rows that are worth more than the cards they sit in

- **AWS KMS**: a custom key policy that omits the root statement locks IAM out entirely, and a
  key policy that names nobody is unrecoverable without AWS support. That is the one mistake in
  this wave with no self-service repair.
- **GCP load balancing**: allowing the two health-check ranges is the single most common cause of
  "every backend is unhealthy and the config looks perfect". It is a firewall rule, and it should
  be created with the load balancer rather than discovered during the outage.

### The measurement

```
                        D11 end   D12 end
thin topics                 203       195
cloud                              32 →  24   (50% → 38%)
mean chars/concept card   1,212     1,214
median topic              3,014     3,027
10th percentile           1,365     1,367
```

**Ninety-six cards across twelve waves, and the padding counter-metric has moved fourteen
characters.** Phase 8 §8's target of "under 150 thin" is now 45 cards away — six more waves at
the current rate, and for the first time in this phase the end is close enough to name.

Site **1,420 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 8 wave D13: reading a negative result

D4 gave `blueteam`'s tool cards *what this tool cannot see*. The twenty-eight left are mostly
the domain's practices and outputs — hunting, tuning, benchmarks, forensics, coverage maps,
detonation — and they share a gap that belongs to defensive work specifically.

**Blue-team tools return a negative result most of the time.** The hunt finds nothing. The
sandbox says clean. The benchmark passes. The matrix is green. Nothing on this site said how to
read that, so the reassuring answer was being taken at face value in exactly the eight places
where it deserves the most suspicion.

| Card | What "nothing found" may actually mean |
|---|---|
| Threat Hunting | Nobody wrote the hypothesis down, so nothing was ruled out — **the output of a clean hunt should be a statement of coverage** |
| Windows Forensic Artifacts | Prefetch is off by default on Server; the USN journal wraps in hours. Scope the conclusion to the artefacts examined |
| Vulnerability Scanners | An unauthenticated scan infers versions from banners. **Report the denominator: what fraction was scanned, and credentialed** |
| MITRE ATT&CK | A green cell means a rule was tagged. Colour the matrix from test results, not rule inventory |
| YARA | A rule is a hypothesis about bytes; no match falsifies the rule, not the file |
| Malware Sandboxes | A suspiciously empty report is itself a finding — evasion looks exactly like harmlessness |
| Detection Tuning | **A well-tuned rule and a broken rule both produce silence.** Re-run the behaviour and confirm the alert still fires |
| CIS Benchmarks | A fully hardened host running vulnerable software scores very well |

### The clause that made the wave work

The spec required two things: what a null result may mean, *and* what would have to be true for
it to be good news. The first half alone is a shrug — "it might be a false negative" leaves the
reader exactly where they started. The second half turns each card into something runnable:

- A hunt is trustworthy if the hypothesis was falsifiable, the coverage was measured, and the
  query is recorded verbatim.
- A scan result is trustworthy in proportion to the fraction of assets reached **with
  credentials**.
- A tuning change is trustworthy once the behaviour has been re-run and the alert observed.

Those are three checklists that did not exist on this site an hour ago, and each is a few minutes
of work rather than a project.

### The card that argues with a number the site elsewhere reports approvingly

The MITRE ATT&CK card says an inventory-coloured coverage map typically overstates real coverage
by around three to one, and that the honest number is the one that predicts incident outcomes.
That sits alongside D6's accessibility finding — where this repository's own green `make a11y`
was described as the floor rather than the result — and the two are the same argument in
different domains: **a measurement that is easy to make green is the one to trust least**, and
the site should say so about its own numbers as readily as about anyone else's.

### The measurement

```
                        D12 end   D13 end
thin topics                 195       187
blueteam                           28 →  20   (52% → 37%)
mean chars/concept card   1,214     1,215
median topic              3,027     3,046
10th percentile           1,367     1,373
```

**104 cards across thirteen waves; fifteen characters of movement in the counter-metric.** The
"under 150 thin" target is 37 cards away — under five waves.

Site **1,420 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 8 wave D14: the number, or it is not advice

`data` has now had three waves and each one found a different missing thing, which is unusual —
most domains here have one structural gap repeated across their cards. D1 gave eight cards eight
different additions. D8 gave the SQL cards their silent wrong answers. D14 takes the **product**
cards, and their gap is the one that decides whether database writing is useful at all.

Every product card was written as though volume and access pattern were details. In databases
they are the only thing. *"PostgreSQL is the default choice"* is true and useless without the
sentence that follows it, and *"SQLite is everywhere"* is true with the limit on an axis nobody
expects.

| Card | The threshold, and what you move to |
|---|---|
| PostgreSQL | **Connections bind first** — a few hundred, long before storage. Pooler, then replicas, then partitioning, then distributed |
| SQLite | **One writer at a time, database-wide.** Size is not the limit; hundreds of GB is ordinary. Funnel writes through one process, or move to Postgres |
| Redis | Working set against RAM, and `noeviction` **fails writes** at the boundary. TTL on everything |
| MongoDB | The moment a second access pattern needs a join. Write down the three queries first |
| Cassandra & DynamoDB | **There is a floor as well as a ceiling** — three nodes of Cassandra do less than one good Postgres |
| Partitioning & Sharding | You partition for *maintenance* long before speed. Sharding is a one-way door |
| Columnar Engines | Scans win, point lookups lose. A laptop running DuckDB handles what gets proposed as a cluster |
| Graph Databases | Two hops is a join; five is a graph. Try a recursive CTE first |

### Why the second requirement mattered more than the first

The spec asked for a threshold **and** what you move to. Thresholds alone would have produced
eight cards of discouragement — "this will not scale" is not information. The migration path is
the actual decision, and writing it forced an ordering that most of these cards were quietly
skipping:

> Pooler, then indexes and query fixes, then read replicas, then partitioning, then anything
> distributed. **Most teams that believe they have outgrown Postgres have skipped step one.**

### The two cards that invert the expected direction

**SQLite's limit is not size.** It is dismissed on scale grounds and scale is where it does best.
Getting that right meant contradicting the received framing rather than repeating it, and it
changes what the card is for: the question is never "how big is the data" but "how many processes
need to write".

**Cassandra has a floor.** Every card of this kind describes the scale above which you need a
distributed database. The more useful number for almost every reader is the one below which
choosing one is a mistake — and that number is high.

### The measurement

```
                        D13 end   D14 end
thin topics                 187       179
data                               23 →  15   (55% → 36%)
mean chars/concept card   1,215     1,217
median topic              3,046     3,070
10th percentile           1,373     1,381    ← +8, the largest single move it has made
```

`data` has gone **40 → 15** across three waves, from the worst ratio on the site to below the
median domain. And the 10th percentile moved eight characters, which is the first time it has
moved meaningfully — not because this wave targeted the floor, but because `data`'s product cards
were genuinely near it.

**112 cards across fourteen waves; seventeen characters of counter-metric movement.** The "under
150 thin" target is 29 cards away.

Site **1,420 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 8 wave D15: the first wave that adds concrete rather than analysis

Fourteen waves added *analysis* — a failure mode, a blind spot, a threshold, a bill, a
prerequisite, a null result. D15 is the first that adds **the thing itself**, and `eng`'s craft
cluster is where that was the only move available.

Those cards do not lack analysis. They contain plenty. What they contain none of is an example. A
card explains that a review comment should be specific and kind and never shows one; a card
explains what an ADR records and contains no ADR; a card says estimates should carry assumptions
and gives no estimate. **Craft is imitated before it is understood**, and a reader who has never
seen a good design doc cannot produce one from a list of its qualities.

| Card | The artefact now on the page |
|---|---|
| Code Review | The same N+1 comment written three ways — unhelpful, good, and blocking |
| ADRs & Design Docs | A complete ADR-014, four headings, one screen |
| Estimation & Planning | "3–5 weeks, 80% confidence", with what is excluded and what would break it |
| Designing for Failure | A filled-in pre-mortem for a payment provider, four columns, five rows |
| Staff+ Archetypes | Promotion-packet sentences per archetype — scope, outcome, artefact |
| Influence Without Authority | The cross-team request that gets ignored, and the one that gets done |
| Back-of-the-Envelope | 5M users → 36 TB/year → "not one Postgres table", worked through |
| API-First | One endpoint's contract, then the three questions to ask of it |

### The test, and the row it produced

*It has to be copy-pasteable.* Not "a review comment should explain the why" but the comment, in
quotes, that somebody could adapt in thirty seconds. That constraint is what turned the influence
card from advice into a diagnosis: the message that works does so **because it removes the other
team's work, not because it is more polite** — it arrives with the PR written, the flag defaulting
to off, one specific ask, and an easy way to say no. Nothing in the abstract version of that card
said any of it.

The pre-mortem produced the wave's most useful single row, and it is the one nobody writes down:

> *The provider succeeded and our write failed.* Every team has considered "the dependency is
> down". Almost none have considered the case where money moved and the order did not — which is
> where the fix has to be designed in (record intent, reconcile after) rather than added later.

### One card was cut for duplicating a card that already existed

Technical Debt was in the original eight, with a debt item written to compete with features. The
domain already carries **Technical Debt as a Financial Argument — Language That Funds It**, which
is that artefact, better. Caught by `retire_topic.py`'s ambiguity refusal on the title fragment —
a guard written for Phase 9 turning up a Phase 8 duplication before it was written rather than
after. Replaced with **Designing for Failure**.

### The measurement

```
                        D14 end   D15 end
thin topics                 179       171
eng                                24 →  16   (32% → 21%)
mean chars/concept card   1,217     1,218
median topic              3,070     3,082
10th percentile           1,381     1,389
```

**120 cards across fifteen waves; eighteen characters of counter-metric movement.** The "under
150 thin" target is **21 cards away** — three waves.

Site **1,420 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 8 wave D16: connecting the rules of engagement to the tools

`redteam`'s first card is **Rules of Engagement — Read This First**, and until this wave it was
the only card in the domain that mentioned scope. Fifty-one others described tools as though
authorisation were a paperwork step that happens once, somewhere else. D16 connects the two.

The spec's test did the discriminating: the reach must be **inherent to the tool**, not a mistake
an operator could avoid. "Do not scan out of scope" is discipline and was cut twice. "802.11
capture cannot exclude the neighbours' frames" is physics.

| Card | What it reaches, and the clause that has to exist |
|---|---|
| Shodan & Censys | Third-party observations, some stale, some about recycled cloud IPs. **Ownership confirmed in writing before active testing** |
| Google Dorking, Maltego, SpiderFoot | The subject is *people*. Lawful basis, and a deletion date for the corpus |
| Wifite & hcxdumptool | **Radio does not respect the property line.** ESSIDs in scope, deauth authorised or not, out-of-scope captures discarded unanalysed |
| Bettercap | The whole broadcast domain — printers, handsets, a contractor's phone. Segments named; third-party traffic handled |
| sqlmap | It writes by default, and `--dump` extracts real personal data. **Prove with a version string, then stop** |
| Flipper Zero & Sub-GHz | Premises, other tenants, and law that changes at the border. Physical authorisation, a letter carried on the person, a jurisdiction check |
| Data Exfiltration | Real data to infrastructure you now own. **Plant a canary and exfiltrate that** |
| msfvenom | An artefact that becomes public the moment anyone submits it to a scanner |

### Three findings that were not obvious before writing them down

- **"Passive" describes the effect on the target's systems, not on people.** OSINT tooling
  returns personal data about named employees, and collecting it is regulated whether or not a
  packet ever reached the client. The word has been doing damage by implying the wrong thing.
- **The client cannot always authorise the test.** In a shared building they do not own the radio
  environment or the car-park barrier, and this is the one area in the domain where a signed
  scope document from the client is genuinely insufficient.
- **The proof can be the harm.** Exfiltration is the only technique here where demonstrating the
  finding *is* the finding's damage — which is why the canary-file habit matters more than any
  clause: it proves the channel without the payload ever being a real record.

### What the wave says about the domain

Three waves in, `redteam`'s cards now answer four questions each: what the tool does, what using
it costs and what the defender sees (D2), what you must already have (D11), and what it touches
beyond the target (D16). That is the shape of a professional tool reference rather than a
catalogue, and it arrived by applying a different lens each time rather than by making any single
card longer.

### The measurement

```
                        D15 end   D16 end
thin topics                 171       163
redteam                            24 →  16   (46% → 31%)
mean chars/concept card   1,218     1,220
median topic              3,082     3,105
10th percentile           1,389     1,393
```

**128 cards across sixteen waves; twenty characters of counter-metric movement.** The "under 150
thin" target is **13 cards away** — two waves.

Site **1,420 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 8 wave D17: the domain where a mistake is billed

Three waves on `cloud`, three lenses. D3: the failure mode that is the same on all three
providers. D12: the assumption you carry over from the other cloud. D17: the meter.

**Everywhere else on this site a mistake breaks something. Here it is billed** — quietly,
monthly, by a service working exactly as designed — and not one of these twenty-four cards said
what the meter counts.

| Card | The meter, and the expensive default |
|---|---|
| GCP Storage | Minimum storage duration per class — **an Archive object deleted next week still bills for a year** |
| AWS Compute | Stopping the instance stops the instance. EBS, snapshots and the public IPv4 keep billing |
| GCP Compute | Persistent disks bill **provisioned**, not used, and cannot be shrunk in place |
| GCP Observability | Log *ingestion* volume. Exclusions act before the meter; retention only acts after |
| BigQuery | Bytes **scanned**, not returned. `LIMIT` does not reduce it; `--dry_run` is free |
| Cloud CI/CD | Build minutes × machine size, and a cache that never hits re-downloads the world per push |
| Hybrid Connectivity | Data transfer, on every boundary — the largest line on data-heavy invoices |
| GCP Databases | HA is a second instance; storage auto-grows and **never shrinks** |

### The rule that makes this durable instead of the fastest-rotting content on the site

**Name the unit, never the price.** Prices change quarterly; a number here would be stale within
a quarter and wrong on 1,420 pages. Billing *shapes* — per GB scanned, per hour whether used or
not, per GB crossing a zone boundary, a 90-day minimum on an object stored for one — change on a
scale of years, and they are what actually determines the invoice. Every draft that reached for a
figure was rewritten to name the meter instead.

That constraint also produced the wave's most transferable observations, none of which is a
price:

- **Exclusions beat retention**, because one acts before ingestion is counted and the other after.
- **The cheapest byte is the one you are not storing** — a lifecycle rule that deletes outperforms
  every class optimisation.
- **Three architectural moves remove transfer charges rather than reducing them**: private
  endpoints, a CDN in front of anything public, and keeping a request's path inside one zone.
- **Everything expensive in CI is also everything slow**, which is the happy case — the same fixes
  shorten the feedback loop, and that is the argument that gets them scheduled.

### The measurement

```
                        D16 end   D17 end
thin topics                 163       155
cloud                              24 →  16   (38% → 25%)
mean chars/concept card   1,220     1,221
median topic              3,105     3,114
10th percentile           1,393     1,404
```

**136 cards across seventeen waves; twenty-one characters of counter-metric movement.** The
"under 150 thin" target is **five cards away** — it falls next wave.

Site **1,420 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 8 wave D18, and the target is met

`blueteam`'s third wave takes the failure mode that actually kills defensive tooling in real
organisations, and it is not technical. **These tools are deployed and then not operated.**

| Card | Without an owner it becomes |
|---|---|
| MISP & OpenCTI | A database of indicators that were true last year |
| Splunk / SPL | **Field extractions break silently the day a log format changes** — searches keep running and quietly go empty |
| OSQuery | A query that errors returns nothing, which looks exactly like a clean fleet |
| Lynis | A score nobody reads, instead of a diff somebody acts on |
| Adversary Emulation | Evidence about one Tuesday in March, presented as coverage |
| Chain of Custody | A process that exists in a document and has never been performed |
| Purple Teaming | A workshop, rather than a loop that closes |
| Elastic / ELK | A mapping explosion and no lifecycle policy |

Three of the eight converged on the same shape without being written to, which is the wave's most
useful result: **ask something you know must be true, and alert when it stops being true.** A
SIEM's most valuable alert is "this log source has sent nothing for an hour". osquery's is a
canary query for a file that exists on every host. Elasticsearch's is a snapshot restore that has
actually been performed. In each case the tool cannot distinguish *nothing found* from *nothing
asked*, and one deliberate known-true probe is what separates a healthy deployment from a silent
one.

The chain-of-custody card is the one to act on first, and it costs an hour a year: seize a spare
laptop properly, fill in the real form, hash the image, store the record. That rehearsal finds
the flat write-blocker battery and the person who did not know they were on the authorised list
— and of everything in this domain, it is where the gap between *written* and *practised* carries
the highest cost.

---

# Phase 8, closed: 144 cards, eighteen waves

```
before:  330 topics single-concept and under 1,800 plain chars   (23% of the site)
target:  under 150
ACTUAL:  147                                                     (10% of the site)
```

| | D1 | D5 | D9 | D13 | D18 |
|---|---|---|---|---|---|
| thin topics | 279 | 247 | 211 | 187 | **147** |
| mean chars/concept card | 1,200 | 1,204 | 1,210 | 1,215 | **1,223** |
| median topic | — | — | 2,996 | 3,046 | **3,133** |
| 10th percentile | — | — | 1,365 | 1,373 | **1,415** |

**The counter-metric moved twenty-three characters across 144 cards.** That is the number the
phase should be judged on, because §7 named padding as the way this work fails and the mean is
what detects it. It held because the discipline never changed: every addition arrived as a *new
concept card with a claim of its own*, never as extra sentences inside an existing one.

## What eighteen specs turned out to be worth

The thing that transfers is not any individual card. It is that **each wave was given a written
spec before any card was touched**, and that no spec was reused. Eighteen domains-and-clusters,
eighteen different structural gaps:

| | Domain | The gap |
|---|---|---|
| D1 | `data` | A different missing thing per card — the only wave without a uniform spec |
| D2 | `redteam` | What using this costs you, and what the defender sees |
| D3 | `cloud` | The failure mode that is the same on all three providers |
| D4 | `blueteam` | What this tool cannot see |
| D5 | `web` | The number your own machine cannot show you |
| D6 | `eng` | The bill this pattern sends, and the size below which it is a net loss |
| D7 | `devops` | What this looks like two years in |
| D8 | `data` | The query that runs, returns a number, and is wrong |
| D9 | `web` | The bug that sent you here |
| D10 | — | **No wave.** The bottom decile is deliberately short, and the commitment was retracted |
| D11 | `redteam` | What you must already have before this runs |
| D12 | `cloud` | The assumption you carry over from the other cloud |
| D13 | `blueteam` | What it means when it finds nothing |
| D14 | `data` | The number at which this stops being the right answer |
| D15 | `eng` | Show the artefact |
| D16 | `redteam` | What this touches that your scope may not cover |
| D17 | `cloud` | What you are billed for, and which default is expensive |
| D18 | `blueteam` | Who owns it, how often, and what it becomes without that |

Two of those rows matter more than the rest.

**D10 is the wave that did not happen.** D9 committed the next wave to the bottom decile by
character count; building the tool to execute that commitment showed the commitment was wrong,
because the bottom of this site is the beginner layer and the certification skims and both are
the right length already. It was retracted in the same session and recorded under its own
heading rather than being quietly replaced with an easier wave under the same name.

**D12 inverts D3's own rule**, deliberately, and the spec says why: provider-neutrality is right
for concept cards and writes nothing for service cards. A later session reading both without that
sentence would have found a contradiction instead of a distinction.

## What is left, and what it is not

147 thin topics remain, and the composition is now known rather than assumed:

- **64 of the bottom decile are badged deliberately short** — `Beginner • Core`, `Linux+ • CLI`,
  `PenTest+ • Recon`, `Military • Reference`. These are not debt. Phase 9 §3 exists to protect
  the first group and D10 established the second.
- The rest sit across `web` 17, `eng` 16, `redteam` 16, `cloud` 16, `data` 15, `script` 14,
  `devops` 12, `blueteam` 12 and a long tail of single figures.

Any future wave should start from `depth_report.py`, cross-reference `--thin` against
`near_duplicates.py` (Phase 9 C5's finding: **a thin card is often a duplicate-shaped thing**),
and check `--bottom` before assuming a short card is an underdeveloped one.

Site **1,420 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 7's first ten, and the checks that caught four mistakes

The ordered ten shipped as specified. Each was pre-flighted with
`near_duplicates.py --title` before a word was written &mdash; which is the mode T2 was built
for, and this is the first session to have used it as intended rather than as a census.

| # | Card | The argument it turns on |
|---|---|---|
| 1 | `cs` **Little's Law & Queueing** | `W = L / λ`, and the wall at 90% utilisation. Adding one worker is not a 15% improvement, it is a fourfold reduction in queueing delay |
| 2 | `threat` **State-Sponsored Operations** | Criminals optimise for money per hour; states optimise for access and will spend a year being quiet. **"We're not a target" is a claim about value to a specific sponsor** |
| 3 | `sec` **Asset Discovery** | Every coverage metric is a fraction with an unknown denominator — and inventories are always wrong in the same direction |
| 4 | `cloud` **Multi-Cloud** | Four reasons, two of them real. **The abstraction that avoids lock-in is a dependency with one maintainer** |
| 5 | `linux` **Rescuing a System That Will Not Boot** | Mount, bind, chroot, fix, rebuild, exit, unmount — and step three is the one people skip |
| 6 | `eng` **RFCs & Design Docs** | Written before the decision, or it is documentation. The test is whether anyone could change the outcome by reading it |
| 7 | `productivity` **The Weekly Review** | Capture without review is a graveyard, and reading back last week's *calendar* finds more than the inboxes do |
| 8 | `redteam` **Operator OPSEC** | Detection on day one measures the client's response to a noisy operator. **Be hard to detect and trivially easy to identify once detected** |
| 9 | `script` **subprocess Without Shell Injection** | The convenient form is the dangerous one, and a list of arguments removes the bug class rather than filtering it |
| 10 | `blueteam` **SOC Metrics That Do Not Lie** | MTTD is gameable by narrowing what counts as detected. Four metrics that resist gaming, each uncomfortable |

### Four mistakes, four different checks

Writing ten new cards rather than deepening existing ones exercises a different set of guards,
and every one of them fired:

| Caught by | What it was |
|---|---|
| **The verdict ratchet** in `lint_content.py` | `table with no verdict: 514 exceeds the ceiling of 513`. Eight new tables had been written without one. Fixed by writing eight verdicts — the ratchet turned a style rule into content |
| **The xref checker** | Three invented cross-reference titles: *Landing Zones — The Account Structure You Cannot Retrofit*, *Motivation — Why Waiting for It Fails and What Low-Motivation Systems Look Like*, and an ADR title with the acronym expansion inside it. All three were plausible and none existed |
| **The acronym `byDomain` check** | Writing "a CI/CD supplier" in `threat` introduced `CD` to a domain with no decision recorded for it, and the linter refused to guess between Continuous Delivery and Continuous Deployment |
| **`suggest_related.py --check`** | Ten new cards would have been ten orphans. Eleven bidirectional edges added, and the one-way count stayed at zero |

The xref row is the one worth noting, because it is the **sixth** time this session that a
cross-reference has been invented rather than looked up. The failure is consistent enough to
name as a rule: **a title you can remember is a title you are reconstructing.** Grep for it
first, every time — the linter will catch it, but at the cost of a build cycle each.

### What the new cards were built to do

Six of the ten exist to be referenced by other cards rather than read alone, which is why the
ordering put them early. *Asset Discovery* gives every coverage metric elsewhere a denominator.
*Little's Law* explains three existing cards from underneath — connection pools, CI queues and
retry storms are one phenomenon. *RFCs & Design Docs* completes a pair with the existing ADR
card: **the doc is the deliberation and the ADR is the residue**, and writing only one of the
two loses either the record or the chance to influence it.

```
topics     1,420 → 1,430
thin         147 → 147     (none of the ten is thin)
mean chars/concept card  1,223 → 1,227
related links  882 → 904, still 0 one-way
```

Site **1,430 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 7, tracks CE and CI: the release factory and the toolchain

Phase 7 says *&ldquo;after ten, re-run the audit rather than continuing down the list&rdquo;*, so
the audit was re-run before this batch and it chose the tracks. `devops` was 27% thin with the
best-specified remaining track; `script` was 143 topics teaching the language thoroughly and the
environment around it barely. **Track CE is now complete (6 of 6) and CI is complete (5 of 5).**

| Domain | Card | The argument |
|---|---|---|
| `devops` | Flaky Tests | A suite that fails randomly teaches the team to re-run rather than read — and **automatic retries are the fix that removes the evidence** |
| `devops` | Test Data | Fidelity, privacy, refresh cost: pick two. Teams that never chose have all three at their worst |
| `devops` | Ephemeral Environments | **The shared staging queue is often the real bottleneck**, and the prerequisites are the capabilities that make production recoverable |
| `devops` | Monorepo vs Many Repos | The trade is about coordination, not storage. Pick the failure you can staff |
| `devops` | Build Caches | Measure first — the minutes are in dependency install, not compile. **The cache key is the whole design** |
| `devops` | Release Notes | A changelog is the API of your release process, read by five audiences with five different questions |
| `script` | Type Hints & a Type Checker | Hints nothing checks are comments with better syntax. **A type annotation is not validation** |
| `script` | pathlib | Always pass `encoding="utf-8"`; `resolve()` before comparing; check the path stays inside the directory you meant |
| `script` | Threads, Processes & async | One diagnostic picks all three: is the program waiting, or computing? |
| `script` | Packaging & Dependency Pinning | Pin for applications, range for libraries — and **this is the supply-chain surface** |

### The verdict ratchet fired again, and harder

Thirteen new tables without verdicts this time (520 against a ceiling of 513), after eight last
batch. That is not carelessness twice; it is a **structural property of writing new cards**. A
deepening wave adds one card with one table and one verdict, because the spec asks for a claim.
A new card is three cards and three tables, and the middle one is always the reference table
that feels like it speaks for itself.

It does not. Writing the thirteen verdicts produced some of the better lines in the batch — the
antisocial-pinning point, the GIL-is-not-a-lock warning, the observation that an unpinned
`requirements.txt` failure gets debugged as though it were your code. **The ratchet is not a
style rule with a content side effect; it is a content rule enforced by counting.**

### And the seventh invented cross-reference

*Software Supply Chain Security — SBOM, SLSA & Signing.* The real title ends *& Sigstore*. The
linter's "Did you mean" caught it in one cycle, which is the third time this session that
feature has paid for itself — but the rule stated after the last batch stands unchanged and was
ignored one batch later: **grep for the title, do not remember it.**

```
topics     1,430 → 1,440
thin         147 → 147   (none of the twenty new cards is thin)
mean chars/concept card  1,227 → 1,231
related links  904 → 924, still 0 one-way
```

Site **1,440 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 7, tracks CG and CH complete: recovery, and five primitives

Two more tracks closed. `linux`'s was **recovery** — the situations where the normal tools are
not available — and `cs`'s was five primitives the domain genuinely lacked despite being the
strongest in the file.

| Domain | Card | The claim it turns on |
|---|---|---|
| `linux` | sudoers & PAM | Two separate stacks people conflate. **If nobody can authenticate, editing sudoers will not help** |
| `linux` | Journald & Logrotate | Two overlapping retention systems, and the disk fills because of the one you did not configure |
| `linux` | rsync & the trailing slash | One character decides directory-or-contents, and with `--delete` there is no undo. **A mirror is not a backup** |
| `linux` | strace & ltrace | What is this program actually asking the kernel for? Grep for `ENOENT` first |
| `linux` | Linux on the desktop, and WSL | The honest answer is about workflows. Hardware support is written for the OS the machine shipped with |
| `cs` | Compression | Incompressible data is data with no redundancy — **if encrypted output compresses, the cipher is broken** |
| `cs` | Consistent hashing | Modulo sharding gets *worse* as the cluster grows, and virtual nodes are a correctness requirement |
| `cs` | Byte order & binary layout | Padding bytes are uninitialised, so writing a struct to a socket leaks memory |
| `cs` | Catastrophic backtracking | Simultaneously a performance bug, a security vulnerability, and invisible in review |

### The ratchet, a third time — and the pattern is now measurable

Ten verdict-less tables this batch, after thirteen and eight before it. Three batches of new
cards, three ratchet failures, and **the rate is essentially constant at about one per card**.
That is no longer a lapse; it is the shape of the work. A new card is three concept cards and
three tables, and the middle one is always the reference table that appears to speak for itself.

The stated intention at the start of this batch was to write the verdicts as I went. It did not
happen, and recording that is more useful than claiming it did: **an intention is not a control,
and the ratchet is.** The right fix is the same one this file reaches for elsewhere — make the
tool do it. A future session should teach the card scaffold to refuse a table with no verdict at
the point of writing rather than at the point of linting.

### Two more `byDomain` decisions the acronym checker demanded

`CD` in `threat` last batch, `WAF` in `cs` this one — the ReDoS card mentions a web application
firewall, and `cs` had no recorded decision between that and *Well-Architected Framework*. Both
took ten seconds and both are the check working exactly as designed: **a new card in a new
domain is where an ambiguous acronym first becomes ambiguous.**

```
topics     1,440 → 1,449
thin         147 → 147   (none of the twenty-nine new cards is thin)
mean chars/concept card  1,231 → 1,235
related links  924 → 942, still 0 one-way
```

**Phase 7: 31 of 96 shipped.** Tracks CE, CG, CH and CI complete.

Site **1,449 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 7, tracks CJ and CM: and the scaffold that stopped the ratchet firing

Two more tracks closed. `infra` was missing **everything that is not a server** — the room, the
power, the labels, the process for keeping track of any of it. `productivity` was sixteen topics
of learning science with almost nothing about *managing work*, which is the other half of what
its title promises.

| Domain | Card | The claim it turns on |
|---|---|---|
| `infra` | Failover Clustering | Clusters fail because the survivors cannot agree a node died. **A two-node cluster with no witness is a coin toss** |
| `infra` | The Rack, the Power & the Cooling | Dual feeds are pointless if a single-supply device is plugged into one. Blanking panels are the cheapest cooling fix there is |
| `infra` | Labelling & Asset Tagging | The cost is paid now and the benefit lands at 3 a.m. **Label the physical fact, not the logical role** |
| `infra` | Tape & the Untested Restore | Tape became the offline copy. The question that strands archives is *will there be a drive that can read it* |
| `infra` | Decommissioning at Estate Scale | The hard part is finding what nobody owns — and **a dangling DNS record is a subdomain takeover** |
| `productivity` | The Inbox | An inbox is a list of other people's priorities, sorted by the one ordering guaranteed not to match importance |
| `productivity` | Time Blocking | The failure is over-scheduling. Block 50–60% of the day; **move a lost block rather than deleting it** |
| `productivity` | Focus Blocks | "I'll focus when it's quiet" never arrives. Uninterrupted time on a rota is a coverage negotiation |
| `productivity` | Notes That Get Reopened | If you cannot find it in ten seconds it does not exist. **Write the title as the search you will type** |

### The fix from the last record, applied and tested

The previous session record said an intention is not a control, and that the right answer was to
teach the card scaffold to refuse a table with no verdict at the point of writing. That was done
before this batch, and it fired **four times in nine cards** — each time as an immediate error
naming the card, rather than as a lint failure twenty minutes later after a build.

The measurable result: `table with no verdict` **held at 509**, where the previous three batches
took it to 521, 520 and 514. Three batches of the same mistake, one small change, and the
mistake stopped. That is the same shape as every other guard in this file: *the cheapest place
to catch something is where it is written, and the ratchet's job is to catch what escapes.*

### One acronym decision, again from a new domain

`PDU` in `infra` — the rack card uses power distribution units, and the dictionary held
*Protocol Data Unit* as well. Third batch in a row where a new card in a new domain is the thing
that first makes an acronym ambiguous, which is a pattern worth naming: **the acronym dictionary
is only as decided as the domains it has been used in.**

```
topics     1,449 → 1,458
thin         147 → 147   (none of the thirty-eight new cards is thin)
mean chars/concept card  1,235 → 1,238
related links  942 → 960, still 0 one-way
table with no verdict  509 → 509
```

**Phase 7: 40 of 96 shipped.** Tracks CE, CG, CH, CI, CJ and CM complete.

Site **1,458 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — Phase 7, tracks CF and CN: and the census's second blind spot

Tracks CF (`eng`, the decision-making machinery) and CN (`sec`, running security as a function)
are complete. Eight new cards and **one card that turned out not to need writing** — which is
the more interesting result.

| Domain | Card | The claim it turns on |
|---|---|---|
| `eng` | Build vs Buy | Never build cost against licence cost. **The question behind it is whether this is your differentiator** |
| `eng` | The Staff Engineer Role | Not a very good senior. A problem that crosses teams and belongs to none of them |
| `eng` | Goals That Survive the Quarter | A goal you are confident of hitting carries no information |
| `sec` | Vulnerability Prioritisation | Severity is a property of the flaw; priority is a property of your estate. **KEV first, then EPSS weighted by exposure** |
| `sec` | Shadow IT | Every instance is a requirements document somebody wrote by spending money |
| `sec` | Break-Glass Accounts | The day you need them is the day the identity provider is down — and **two accounts, not one** |
| `sec` | Code Signing | You are not protecting a file, you are controlling an operation |
| `sec` | Security Champions | Influence scales and headcount does not. Measured by consultations, not by headcount |

### The card that already existed, and the reason the check missed it

Track CF asks for *Architecture Decision Records — The Format Whose Value Is the Rejected
Options*. The `--title` pre-flight said **clear to write**. The site already has
**ADRs & Design Docs**.

```
tokens("ADRs & Design Docs")                          = {adr, design, doc}
tokens("Architecture Decision Records — …")           = {architecture, decision, record, …}
containment                                           = 0.00
```

**An abbreviation and its expansion share no characters**, so a token census cannot see they are
the same subject. This is the second structural limitation the title census has shown this
session — the first being the two `script` PowerShell cards at 0.25, where the titles diverged
while the content did not. Different mechanism, same class: *the tool measures titles and the
question is about subjects.*

### Fixed, and the fix had to be asymmetric

`tokens()` now takes `expand=`, pulling each acronym's dictionary meanings in. Turning that on
everywhere was the obvious move and the measurement rejected it:

```
census pairs ≥ 0.50, expansion off  = 40
census pairs ≥ 0.50, expansion on   = 80
```

Any two titles sharing an acronym now also share every word of its expansions, and the census
doubled with almost all of the new pairs false. So the two modes now differ deliberately:
**`--title` expands both sides, because a missed match costs a duplicate card; the census does
not, because a false pair costs a reader's time and there are a million comparisons.**
Asymmetric tools for asymmetric questions — and with the fix, the ADR candidate surfaces as the
top hit at 0.38.

The card itself became a **deepening** rather than a new topic: the existing ADR card had two
concept cards and covered neither rejected options nor the constraints that killed them, so it
gained a third. The right outcome, and one the plan's own queue would have got wrong.

### The scaffold held again

Four more refusals in this batch, and `table with no verdict` **stayed at 509** across seventeen
new cards. One further byDomain decision — `CISA` in `sec`, which the dictionary also knows as
*Certified Information Systems Auditor*.

```
topics     1,458 → 1,466
thin         147 → 147
mean chars/concept card  1,238 → 1,241
related links  960 → 976, still 0 one-way
```

**Phase 7: 49 of 96 shipped.** Tracks CE, CF, CG, CH, CI, CJ, CM and CN complete.

Site **1,466 topics**. Check PASS · smoke **142/142** · search **30/30** · axe **6/6** · visual **2/2**.

---

## Session record — September: enterprise Microsoft management, and the one data-architecture gap

A directed pass — "go deep in MECM, Intune, Azure, Exchange, and enterprise-level Microsoft
management" — followed by the general plan. The interesting result is *where* the genuine gaps
were, because the site was already saturated at the foundational and professional levels. They
clustered almost entirely at one seam: **the hybrid boundary where cloud management meets the
on-prem estate it is replacing.** Nine cards, each a real absence rather than a manufactured one.

| Domain | Card | The claim it turns on |
|---|---|---|
| `cloud` | Azure Arc | The management plane, not the VM, is the product — Arc projects on-prem/multicloud servers into ARM |
| `cloud` | Azure Automation & Update Manager | Agentless patching that already covers Arc-projected servers; runbooks with managed identity |
| `cloud` | Entra ID Protection | Conditional Access that reacts to **risk**, not just rules — sign-in and user risk drive the gate |
| `endpoint` | Endpoint Analytics & Proactive Remediations | Detect-and-fix scripts as a first-class tool; the startup/reliability score |
| `endpoint` | Windows 365 & AVD | Fixed per-user Cloud PC vs pooled multi-session — the licensing model is the design decision |
| `endpoint` | MECM at Scale | **The CAS is the mistake** — one primary goes to ~150k; boundary groups route content; collections are queries that tax the site server |
| `endpoint` | Autopilot Device Preparation | The hardware hash was the bottleneck; the 2024 flow deletes the pre-registration entirely |
| `m365` | Exchange Server On-Prem | You moved the mailboxes and still run a server — the "last Exchange" is a management shim for AD-sourced identity |
| `m365` | Entra ID Governance | Access-by-ticket is a permanent grant nobody revokes; the access review's **default action** is where governance quietly fails |

### The data-architecture gap, and the discipline that stopped it at one

Resuming the general plan, a broad professional-level probe found the storage-architecture
question covered (warehouse/lake/lakehouse) but the **ownership** question absent:

| Domain | Card | The claim it turns on |
|---|---|---|
| `data` | Data Mesh | The bottleneck is the central team that owns the warehouse, not the warehouse — and it is an org restructure sold as an architecture. Most teams need a lakehouse plus data-product discipline, not a mesh |

The card leads with the honest verdict — *most organisations have the scattered-data problem, not
the central-bottleneck problem, and the mesh makes the first one worse before better.* That the
next probe after it found nothing is the point: **a rising count is not progress**, and the deliberate
content pass returns to its floor once the genuine gaps are filled.

### What this pass confirms about where the site is

The nine were not evenly distributed — eight sit on the cloud/on-prem management seam and one on a
single data-architecture question. Everywhere else the probes returned covered-or-`[~]`. Track Y
(Endpoint) is now largely closed: Y4's real gap (device preparation) and Y7's architecture void
(MECM at Scale) shipped, Y8's analytics pair earlier, and the classic Autopilot card already owned
the rest of Y4. What remains there is genuinely narrower — driver management, provisioning packages,
the hardware-lifecycle and runbook documents — the kind of thing to write on demand, not to
manufacture.

```
topics       1,520 → 1,529
related links  ~1,290 → 1,322, still 0 one-way
table with no verdict  509 → 509   (nine cards, every table ends on a verdict)
inline style attribute 1,549 → 1,549
```

Site **1,529 topics**. Check PASS · smoke **142/142** · axe **6/6** · mobile **9/9** · visual **2/2** · determinism reproducible.

---

## Session record — September, part 2: a deepening wave, because the gaps had moved from breadth to depth

With new-content genuinely saturated (every breadth probe returning covered-or-`[~]`), the
honest next move was the one Phase 8 named and `tools/depth_report.py` measures: the **thin
tail** — single-concept cards under 1,800 plain characters. The report put it at **147 of
1,529 (10%)**, concentrated in the domains authored before the current three-card form settled.
This wave took it to **102 (7%)** — forty-five cards, each gaining one genuine second concept
card, with the padding counter-metric holding flat throughout.

The rule the wave held to: **a deepening is a second card that names something the first did
not — a failure mode, an inversion, a decision — never the first card restated longer.** The
proof it held is the counter-metric: mean chars per concept card moved **1,241 → 1,254** across
forty-five additions (i.e. barely), while the thin count fell 45 and the 10th percentile rose
**1,433 → ~1,484**. Padding would have moved the mean and left the percentile flat; this did the
opposite. One genuine content bug surfaced and was fixed along the way: the rendering-modes card
annotated **CSR** as *Certificate Signing Request* when it means *Client-Side Rendering* — CSR was
single-meaning in `acronyms.json`, so the fix added the meaning with a `byDomain` decision and the
idempotent annotator corrected the span on rebuild.

| Domain | Card | The second angle added |
|---|---|---|
| `data` | Warehouse vs Lake vs Lakehouse | The lakehouse is not the default; the table format is a lock-in |
| `data` | Schema Migrations | The migration that looks instant is the one that locks the table |
| `data` | The NoSQL Landscape | Choosing the store is a query decision, not a data-shape one |
| `eng` | Coupling & Cohesion | Couple along the axis of change; low coupling is not free |
| `eng` | Idempotency & Exactly-Once | The key is easy; the race and the dedup window are not |
| `eng` | Technical Debt | The word is abused two ways, and that is how debt never gets paid |
| `eng` | Backpressure | It relocates the pileup to whatever you forgot to bound |
| `eng` | Scalability 101 | Scale up first; horizontal is about failure, not throughput |
| `eng` | Load Balancing & Sharding | The shard key is a one-way door; the LB's job is health checks |
| `web` | State Management | Most state bugs are state that isn't state |
| `web` | Realtime | The cost is operational and arrives after launch |
| `web` | Frontend Security | XSS is an output-encoding bug; encode at the sink |
| `devops` | Branching Strategies | The model is downstream of your release cadence |
| `devops` | Progressive Delivery | A canary is only as good as its metric; flags are debt |
| `devops` | DORA Metrics | A diagnostic you can't game as a set; not a leaderboard |
| `cloud` | Well-Architected | The pillars trade off — it's chosen trade-offs, not a score |
| `cloud` | Cloud IAM Pitfalls | Escalation is a graph, not a policy; guard IAM-write |
| `ops` | Golden Signals | What to measure, not where — the gap is the last mile |
| `ops` | On-Call Done Humanely | Alert fatigue is a death spiral; delete alerts |
| `linux` | systemd Deep | Most systemd pain is fighting it — the Type= field and the cgroup |
| `linux` | Advanced Bash | set -e is necessary, not sufficient — it silently doesn't fire |
| `data` | Data Quality & Observability | Structural checks pass while the data is business-wrong |
| `data` | Designing a Schema | The noun list misses point-in-time facts and the join table |
| `ai` | LoRA/Quantization/Tokenization | LoRA adapts but can't teach; quant loss isn't uniform |
| `blueteam` | Patch & Config Management | Coverage % is a comfort metric; the risk is the exceptions |
| `pentest` | Recon Methodology | Won by turning findings into an attack surface, not more tools |
| `eng` | Consistency in Practice | W+R>N is a staleness bound, not linearizability |
| `web` | Frontend Auth | No XSS-proof token store; lifetime/rotation is the boundary |
| `eng` | Cloud-Native & Serverless | Moves the ops cost, doesn't remove it |
| `web` | GraphQL on the Backend | Relocates complexity server-side; the query is an attack surface |
| `eng` | The System Design Interview | The three failure modes the framework doesn't enumerate |
| `data` | How a Database Actually Works | The buffer pool is the whole story; the working set must fit in RAM |
| `data` | The Relational Model | Put the invariant in the DB — every writer passes through it |
| `data` | Query Optimization | The once-fast query that went slow: stale stats and the plan flip |
| `web` | React — Mental Model | Most bugs fight UI = f(state); useEffect is not a lifecycle hook |
| `web` | Meta-Frameworks | Rendering mode is per-route; the axis is the server/client boundary |
| `net` | DNSSEC & Encrypted DNS | DNSSEC stalled, DoH spread — and DoH blinds the defender |
| `data` | Database Security — RLS | The bypass footguns (owner bypass, forgotten context) leak tenants |
| `data` | Postgres JSONB | A one-way convenience; promote any field you query on |
| `eng` | The Twelve-Factor App | Statelessness is load-bearing; the bug appears at 2+ instances |
| `web` | Progressive Web Apps | A service worker makes the browser a distributed-systems node |
| `web` | Rendering at the Edge | Compute is near the user; the data is still far — that's the limit |
| `eng` | Clean Code & Naming | Over-applied, the rules invert into their opposite |
| `data` | CTEs & Recursion | The optimization fence — readable steps the planner won't cross |
| `data` | MySQL / MariaDB | "Looser SQL" was an integrity landmine; MariaDB is no longer a twin |

### What the wave deliberately did not touch

The thin count did not go to zero, and should not. The report's `--bottom` view and its
`DELIBERATE` badge list mark the cards that are short *on purpose* — the beginner layer and the
per-certification objective skims — and deepening those would make them worse. Beyond those, the
remaining tail is largely **tool- and provider-reference cards** (`John the Ripper`, `tcpdump`,
`gcloud CLI`, the language blurbs): a scannable one-table reference is the right shape for those,
and a forced second card would be the exact padding the counter-metric exists to catch. The wave
stopped at each domain the moment it reached that reference floor, which is why it deepened the
concept-rich domains (`data`, `eng`, `web`, `devops`, `cloud`, `ops`) and left the tool domains
(`redteam`, `blueteam`, `script`) near where they were.

```
thin single-concept (<1,800 chars)   147 → 102  (10% → 7%)
mean chars per concept card        1,241 → 1,254   (forty-five cards; counter-metric held)
10th-percentile topic length       1,433 → ~1,484
table with no verdict                509 → 509   (every new table ends on a verdict)
```

Site **1,529 topics** (depth, not count — no new topics this wave). Check PASS · smoke
**142/142** · axe **6/6** · mobile **9/9** · visual **2/2** · determinism reproducible.

---

## Session record — September, part 3: the paths programme, where the gap was navigation not content

With content saturated and the depth tail worked down, the next honest question was not *what
is missing* but *what is unreachable*. `check_paths` answered it: **12 paths, 175 steps, 175 of
1,529 topics** — 11% of the site sat on a curated route, and the domains left off that map were
not small ones.

| Domain | Topics | Path steps before |
|---|---|---|
| `script` | 148 | 1 |
| `sec` | 92 | 3 |
| `eng` | 81 | **0** |
| `ops` | 77 | 8 |
| `cloud` | 74 | 5 |
| `linux` | 62 | 9 |
| `blueteam` | 60 | 3 |
| `redteam` | 58 | **0** |
| `infra` | 52 | 2 |
| `threat` | 46 | 2 |
| `m365` | 42 | 1 |
| `pentest` | 34 | **0** |

Twenty-four new paths later: **36 paths, 579 steps, 555 distinct topics — 36% of the site.**

**None of this is new content.** A path is an ordered list of topic ids over cards that already
exist, so the whole wave added zero topics and zero words. That is exactly why it was worth
doing: the writing was already there and simply had no route through it. A reader wanting to
become a detection engineer had sixty blueteam cards and no order to meet them in.

| Path | Steps | The arc it sequences |
|---|---|---|
| Ship It and Run It | 17 | culture → branch → CI → package → IaC → deploy → observe → on-call → postmortem → DORA |
| Running Windows Server & AD | 22 | the box → the directory → replication → policy → identity hygiene → core services → DC recovery |
| The Layer Under Everything | 19 | virtualisation → VM ops → storage → clustering → backup → restore testing → decommissioning |
| From Engineer to Manager | 18 | the fork → the transition → the weekly loop → hiring → Conway → planning → managing up |
| The Software Supply Chain | 10 | where a build comes from → SBOM/VEX → SLSA → signing → verify at deploy → the pipeline |
| Administering Microsoft 365 | 23 | tenant → licensing → roles → Groups → Exchange → SharePoint → Teams → security → compliance |
| Running Azure | 13 | fundamentals → hierarchy/RBAC → network → compute → Defender → CA → KQL → Arc |
| Securing Cloud-Native | 17 | trust boundaries → cloud IAM → K8s threat model → isolation → serverless → detect → respond |
| Identity Is the Perimeter | 18 | IAM → factors → passkeys → federation → tokens → the attacks → PAM → offboarding |
| Application & API Security | 15 | threat model → web bug classes → headers → API top 10 → BOLA → SAST/DAST → supply chain |
| Detection Engineering | 23 | requirement before rule → telemetry → schema → detection-as-code → test → measure → retire |
| DFIR | 12 | chain of custody → telemetry → artifacts → timelines → disk → memory → at scale → hunting |
| Penetration Testing, End to End | 17 | authorisation → phases → recon → scan → exploit → post-ex → rate → report → disclose |
| Adversary Emulation & Purple | 13 | emulation ≠ pentest → threat profile → kill switch → lab → ATT&CK → measure → anti-theatre |
| Python That Ships | 22 | venvs → errors/logging → typing → CLIs → secrets → pytest → tooling → packaging |
| Automation for Administrators | 15 | PowerShell → Graph → idempotent scheduling → secrets → JEA → config as code → blast radius |
| Linux Administration, Properly | 22 | permissions → sudoers/PAM → boot → systemd → storage → firewalls → MAC → namespaces → rescue |
| Reading the Threat Landscape | 18 | actors → frameworks → intel lifecycle → the criminal economy → ransomware → attribution |
| Endpoint Engineering with Intune | 27 | provisioning → policy → apps → update rings → security → device trust → analytics |
| The Mixed Fleet — Beyond Windows | 11 | macOS → Apple fleet → iOS/Android → BYOD → kiosk → sessions → browser → legacy |
| Running MECM (ConfigMgr) | 7 | the product → site architecture → site/client health → deployment → OSD → co-management |
| Hardware & the Bench | 20 | static → electrical basics → test gear → the components → POST → isolate-and-swap → rework |
| Going Independent | 14 | which model → pricing → clients → SOW → scope → the report → cash flow → past your own hours |
| Teaching & Enablement | 11 | how adults learn → curriculum → the room → demos → docs, diagrams, proposals |

### Two things the wave was careful about

**Reuse across paths is not duplication.** 489 steps resolve to 470 distinct topics, so a
handful of cards appear in two paths — `admin-roles-least-privilege` sits in both the endpoint
and M365 routes, `measuring-detection-quality` in both detection engineering and purple teaming.
`check_paths` only flags a step repeated *within* one path, which is the copy-paste it is
actually looking for. A topic genuinely on two routes should be on both.

**The offensive paths lead with authorisation**, because the domains already do: *Ethical
Hacking 101* and *Scoping & Rules of Engagement* are steps one and two of the pentest path, and
the emulation path's third step is the one about scope, safety and the kill switch. That is the
site's own framing, kept rather than added.

### What is left, and why the number will not reach 100%

`mind` (2 steps) is the only domain left with real content and almost no route, and it is a
small, deliberately browsable one. But the ceiling here is not 1,529. Reference
domains (`acronym`, `shortcut`) are lookup surfaces, not routes, and much of the site is
deliberately *browsable* rather than sequential. A path earns its place when a real job or
subject has an order that genuinely matters; inventing one for a set of cards that do not build
on each other would be the same failure as padding a thin card.

```
paths            12 → 36
steps           175 → 579
topics reached  175 → 555   (11% → 36% of the site)
new topics            0     (curation over existing content)
```

Check PASS (`check_paths`: every step resolves, no duplicates within a path) · smoke **142/142**
· axe **6/6** · mobile **9/9** · visual **2/2** · determinism reproducible.

---

## Session record — September, part 4: the orphan programme finished, and two cards the census could not have found

`tools/orphan_report.py` was written to answer a question the depth report cannot:
not *which cards are thin* but *which good cards can nobody reach*. Its docstring
records 159 topics with three or more concept cards and over 3,000 plain characters
that had no related link and no cross-reference pointing at them. This session took
that number to **zero**.

### Why the tool's own suggester was not used

`tools/suggest_related.py` will happily rank candidates by term overlap, and its
docstring warns what that produces: strips filled with the same four cards, because
overlap measures vocabulary rather than adjacency. Two cards that both say "policy"
forty times are not related; a card about proposals and a card about scope control
are, and share almost no vocabulary. So none of the 334 pairs added here came from
the ranker.

They came from three sources, in order of confidence:

| Source | Pairs | What made it trustworthy |
|---|---|---|
| Learning-path adjacency | 47 | Two cards already sequenced next to each other in a curated path are, by construction, a reader's next step |
| Domain curation, ops/net/linux/infra/grc/sec | 112 | Read both cards, keep the pair only if the second answers a question the first raises |
| Domain curation, the remaining 65 deep orphans | 175 | Same rule, applied to every deep orphan until none was left |

Every target was resolved against the built slug set before writing, so no batch
could introduce a dangling id — the drop count was zero on all three.

### What the orphans turned out to be

Not junk. The seven platform-engineering cards were a complete, well-argued sequence
that linked to nothing, including to each other. The six beginner calculus cards had
no route back to the three unit cards that contain them. The consulting sequence —
discovery, proposal, pricing, finding clients, cash flow — was five islands. The
military OPSEC card and both OSINT cards were writing about the same idea from two
directions with no acknowledgement of each other. That is a navigation defect, not a
content one, and it was invisible to every gate the repo runs.

```
deep orphans   133 → 0
all orphans    799 → 551   (a census, not a gate)
related.json   723 keys / 1,308 links → 982 keys / 2,002 links, 0 one-way
new content    none — curation over cards that already existed
```

### Two cards, from reading the plan against the site rather than the site against itself

The unchecked boxes in this file are not a reliable backlog: most of the
Virtualization, Backup & DR, Apple and mobile-management items were checked off in
practice long ago, under consolidated titles in `infra` and `endpoint`. Probing each
one against the built page found the content already there. Two survived that probe.

**The Object Pipeline — Why PowerShell Is Not Bash With Different Verbs** (`script`).
`Select-Object` appears in code blocks across six domain files, and the site had no
card explaining the thing that makes those blocks work. The card is built around the
inversion — Unix throws structure away at the pipe and re-parses it downstream;
PowerShell never serialises until a human is the audience — and then names the four
places the model leaks, each with the error text it produces: format records in a
CSV export, `Deserialized.System.*` losing its methods across a remoting boundary,
`-eq` filtering an array instead of answering true or false, and a pipeline
materialised in memory by the parentheses someone added for readability.

**Driver Management — Driver Packs, DISM & the Autopilot Dilemma** (`endpoint`).
The servicing card covers driver *updates* as one of three pipelines. Nothing covered
getting drivers onto a machine in the first place, which is where the real
architectural choice sits: a task sequence owns versions and pays for a catalogue,
Autopilot delegates versions and pays in drift, and Intune driver update policies buy
back a rings-and-approval say over anything published to Windows Update. The verdict
is that the expensive position is the accidental third one — packs nobody refreshed
and policies nobody configured.

Both are in three learning paths (Automation for Administrators; Endpoint Engineering
with Intune; Running MECM) and both are linked in `related.json`, so neither shipped
as a new orphan.

### One acronym decision the checker demanded, and one entry it was missing

`DISM` was not in `data/acronyms.json` at all despite appearing in `infra` — added as
*Deployment Image Servicing and Management*. And the driver card's mention of an ARM
device made `ARM` render in `endpoint` for the first time, where it means the CPU
architecture rather than Azure Resource Manager; the lint refused the build until
that `byDomain` decision was written down. That is the fourth time this check has
caught a real ambiguity rather than a formatting slip.

```
topics         1,529 → 1,531
paths          37 paths, 599 steps, 572 distinct topics
```

Check PASS · smoke **142/142** · axe **6/6** · mobile **9/9** · visual **2/2** ·
determinism reproducible.

---

## Session record — the redteam tail, and reusing D11's spec instead of writing a new one

D2 gave `redteam`'s tool cards *what using this costs you*; D11 gave eight of them
*what you must already have*, under a spec worth restating: **the prerequisite must
be specific enough to be denied.** Sixteen thin cards were left — 28% of the domain,
the worst ratio on the site — and none of them had had either treatment.

The temptation with a tool card is to write more about the tool. That is padding, and
the counter-metric exists to catch it. D11's spec avoids it because it adds a
different *kind* of statement: not what the tool does, but the condition that has to
be true before it does anything, and the single setting that removes that condition.
Eight more cards, same spec, no new spec needed.

| Tool | What must already be true | The control that denies it |
|---|---|---|
| Cobalt Strike | Code execution **and** an egress path Beacon can use | Authenticated egress proxy kills the channel; WDAC kills the loader |
| Burp Suite | A credential at every privilege level you intend to test | Contractual, not technical — the scope and the accounts issued |
| Searchsploit | An exact version, on a target that really is that version | Backporting: the fix ships while the banner still reads vulnerable |
| Hydra / Medusa | **Valid usernames**, and no second factor | MFA changes what a hit means; lockout denies the brute force |
| Wordlists & hashes | The hash — and its algorithm decides everything | A real KDF work factor; salt denies precomputation; length denies rules |
| PEAS / PowerUp | Execution as anybody, plus the right to run something unsigned | Application control and constrained language mode |
| Pivoting | Outbound reach **and** routes into the target segment | Egress filtering denies one half, segmentation the other |
| Kubernetes attacks | A mounted service-account token, or an admitted privileged pod | `automountServiceAccountToken: false`; Pod Security Standards |

### Three findings that came out of applying the spec rather than knowing them first

**Version-hiding is the weaker control, and the site had been saying otherwise.** The
existing Searchsploit verdict named banner suppression. Backported distribution
patches are what actually deny the technique — `2.4.52-1ubuntu4.14` carries the fix
while reporting upstream `2.4.52` — and the consequence is the failure mode the card
now leads with: the version-matched finding that is not real, which is the fastest
way to lose a client's trust in every other finding in the report.

**Hydra's prerequisite is the username list, not the password list.** Spraying
guessed usernames is noise; the enumeration that produces real ones is a separate
finding that should be reported whether or not the spray succeeds. And with MFA
enforced, a correct password proves password hygiene rather than access — a different
finding at a different severity, which the operator can only know by asking about the
tenant before running anything.

**Hash identification fails silently.** `hashid` guesses from shape, raw MD5 and NTLM
are both 32 hex characters, and the wrong `-m` returns zero cracks against genuinely
weak passwords — which reads exactly like a strong password policy. A failed crack is
evidence only if you know you attacked the right algorithm.

### The measurement

```
                          before   after
thin topics                  102      94
redteam thin                  16       8   (28% → 14%)
mean chars/concept card    1,256   1,257   ← the counter-metric, +1 over eight cards
median topic               3,242   3,248
10th percentile            1,484   1,493
```

Site **1,531 topics**. One acronym entry the wave needed: `WDAC` was used in `sec`
and absent from `data/acronyms.json`, so it annotated nowhere.

Check PASS · smoke **142/142** · axe **6/6** · mobile **9/9** · visual **2/2** ·
determinism reproducible.

---

## Session record — the cloud tail: the default that is wrong, and the day you find out

`cloud` had 14 thin topics, all of them provider-tour cards — *AWS Getting Started*,
*GCP Security*, *Azure Security* — that list services and what each one does. Writing
more about the services would have been padding. The dimension they all lacked is the
one that costs money and incidents: **what the provider turns on for you, what it
leaves off, and which of those defaults is wrong for anyone past the free tier.**

Six cards, one spec: name the default, say what it silently costs, and end on the
setting that changes it — at the level where it survives the next project.

| Card | The default | What it costs before anyone notices |
|---|---|---|
| AWS IAM | `iam:PassRole` on `"Resource": "*"` reads as harmless | With any launch permission it is AdministratorAccess with extra steps |
| AWS Security Stack | CloudTrail records management events only | No record of object reads — the exfiltration question has no answer, ever |
| Google Cloud | Every VM gets the default compute service account | That account holds `Editor` on the project; one SSRF rewrites the project |
| GCP Security | Data Access logs off for every service but BigQuery | You know who changed the bucket, not who read it |
| Azure Getting Started | Any user may register apps and invite guests | Shadow app registrations, consent phishing, an unowned guest directory |
| Azure Security | Defender's paid plans are per-resource-type toggles | Three of six enabled, one dashboard, a confident green over blind resources |

### The two rows that are worth more than the cards they sit in

**`iam:PassRole` is the one a policy review does not catch.** Every AWS review greps
for `"Action": "*"`; the escalation that actually happens is two narrow permissions
that are individually defensible. That is an argument for Access Analyzer over manual
reading, because the tool reasons about what a combination reaches rather than what
each statement says.

**Azure's security-defaults window.** Tenants get hurt in the gap: defaults are
switched off *in order to* build Conditional Access, the CA policies sit in
report-only while somebody tests them, and the tenant spends weeks with neither. The
card says to build and verify first and switch in one change, with a break-glass
account excluded and its credentials reachable without the tenant.

### The check caught a fifth genuine ambiguity

`CA` renders in `cloud` for the first time, and in that domain all three occurrences
mean **Conditional Access**, not Certificate Authority — which is the expansion the
annotator had already stamped into the new card before the lint refused the build.
That is the fifth time this check has caught a wrong meaning rather than a formatting
slip, and the second in this session.

### The measurement

```
                          before   after
thin topics                   94      88
cloud thin                    14       8   (19% → 11%)
mean chars/concept card    1,257   1,259   ← +2 over six cards
median topic               3,248   3,259
10th percentile            1,493   1,505
```

Across this session's two deepening waves: **14 cards, thin 102 → 88, counter-metric
+3 characters.**

Check PASS · smoke **142/142** · axe **6/6** · mobile **9/9** · visual **2/2** ·
determinism reproducible.

---

## Session record — the blueteam tail: what the tool cannot see

`redteam`'s spec was *what you must already have*. The defensive equivalent is not the
same question — a defender owns the host, so preconditions are cheap — but there is a
symmetric one that matters more, and none of the eleven thin `blueteam` cards asked
it: **what does this tool not collect, and what does a false negative look like?**

Six cards, one spec: name the boundary, give the null result its fingerprint, and end
on how to report a finding of nothing honestly.

| Card | What it cannot see | The fingerprint of the false negative |
|---|---|---|
| tcpdump | Whatever the kernel dropped, snaplen truncated, or TLS encrypted | `N packets dropped by kernel` on exit — printed, and never read |
| Arkime & ntopng | Anything older than the ring buffer, which is days while dwell time is weeks | A confident "show me last Tuesday" that returns an empty result set |
| Graylog & Loki | Loki: any content you did not make a label | A slow query that hits a limit and returns partial results as if complete |
| Velociraptor | Every client that did not answer the hunt | "No findings" from 4,180 of 4,900 endpoints |
| Autopsy & TSK | On a TRIM SSD, deleted data the controller already erased | Carving unallocated space returns zeros |
| OpenSCAP & STIGs | Anything above the configuration layer — and its own non-answers | A percentage inflated by `notapplicable` and `notchecked` rolled into "pass" |

### Three of these invert advice the site was giving

**"Recover deleted files" is a spinning-disk assumption.** TRIM plus garbage
collection destroys freed blocks on the drive's own schedule, often within minutes and
before seizure. So carving returning nothing is not evidence that nothing was there —
and disk becomes the *second* question, after memory and after the artefacts that
record what ran, because a machine's own logs routinely outlive the file contents.

**Full capture is a retention number, not a capability.** The useful design is weeks
of packets and years of metadata, because Zeek connection records cost a fraction of a
percent of the packets they describe and answer most of the questions anyone asks.
A team that believes it has full capture and has four days of it will plan an
investigation it cannot finish.

**A hunt is a fraction, never a verdict.** Asleep laptops, unreachable networks,
never-enrolled hosts and a machine the attacker removed the agent from are
indistinguishable in the result set — all absent — and the host you most want to hear
from is the one most likely to be missing. Report the denominator.

### And one that is an outage waiting to happen

`oscap --remediate` applies fixes in rule order with no knowledge of the application.
The classic outcomes are a hardened SSH configuration that locks out the management
account and a mount option that stops a database starting. Generate the remediation as
a script, read it, and put it through change control — the value of machine-readable
policy is that the diff is reviewable, not that it can be applied unread.

### The measurement

```
                          before   after
thin topics                   88      82
blueteam thin                 11       5   (18% → 8%)
mean chars/concept card    1,259   1,260   ← +1 over six cards
median topic               3,259   3,263
10th percentile            1,505   1,516
```

Three deepening waves this session: **20 cards, thin 102 → 82, counter-metric +4
characters.** The 10th percentile has moved 32 characters and the median 21 — the tail
is rising because cards left the tail, not because anything got wordier.

Check PASS · smoke **142/142** · axe **6/6** · mobile **9/9** · visual **2/2** ·
determinism reproducible.

---

## Session record — the devops tail: the failure mode of the idea, not more about the idea

`devops`'s thin cards split cleanly in two, and the two halves needed different
questions. The culture cards — *What DevOps Actually Is*, *The Three Ways*, *Value
Stream Mapping* — are correct and unfalsifiable as written; what they lack is what
adopting them badly looks like from inside. The Kubernetes reference cards list
objects accurately and omit the fields that decide what happens under pressure.

| Card | The failure mode | Its fingerprint |
|---|---|---|
| What DevOps Actually Is | A "DevOps team" — the old wall rebuilt one department left | Deploys need a ticket; that team is on call for services it did not write |
| The Three Ways | Buying the First Way and skipping the Second | Deployment frequency and change-failure rate rising together |
| Value Stream Mapping | Improving a step that was never the constraint | Build time halved, lead time unchanged |
| Kubernetes Objects | No `requests`/`limits`, so the pod is `BestEffort` | Evicted first, and nobody chose it |
| CNI & CSI | A NetworkPolicy the CNI does not enforce; a ReadWriteOnce volume | `kubectl get netpol` shows the control; `Multi-Attach error` stalls the rollout |

### The two that are worth more than their cards

**The organisational response to missing feedback attacks flow instead.** When change
failure rate climbs, the instinct is an approval gate — which slows the First Way to
compensate for an absent Second, and detects nothing, because a human reading a diff
is not a test. That is why the DORA numbers are quoted in fours: the pairs are what
distinguish "faster" from "faster at shipping defects."

**A NetworkPolicy on a Flannel cluster is accepted, listed, and inert.** The API
server takes it, `kubectl get netpol` shows it, the repo contains it, and the
compliance evidence cites it — and no packet is affected, because enforcement belongs
to the CNI and Flannel does not implement it. The card's instruction is to prove
enforcement once by curling between two pods the policy should separate, rather than
by reading YAML.

### One correction to the site's own emphasis

The Kubernetes objects card ended on "everything is declarative YAML reconciled to
desired state," which is true and is not what breaks. Memory and CPU limits look like
a pair in the manifest and behave in opposite ways: memory is incompressible, so over
the limit means OOM-killed, while CPU is compressible, so over the limit means
throttled — latency with no error and no restart. The usual sound default is a memory
request equal to its limit and no CPU limit at all.

### The measurement

```
                          before   after
thin topics                   82      77
devops thin                    9       4   (18% → 8%)
mean chars/concept card    1,260   1,261   ← +1 over five cards
median topic               3,263   3,268
10th percentile            1,516   1,529
```

Four waves this session: **25 cards, thin 102 → 77, counter-metric +5 characters, and
the 10th percentile up 45.**

Check PASS · smoke **142/142** · axe **6/6** · mobile **9/9** · visual **2/2** ·
determinism reproducible.

---

## Session record — the web tail: what is true on your machine and false for users

Four thin `web` cards, one question: **what does this look like in development that it
does not look like in production?** Frontend is the domain where that gap is
systematic rather than occasional, and — this is the part worth stating — the gap
always runs in the flattering direction.

| Card | True locally | False for users |
|---|---|---|
| React Patterns | The deps array is "when to re-run" | It is a cache key over the closure; omit one and the effect reads a dead render |
| Data Fetching | The library handles caching | The query key is cache identity, and query placement decides the waterfall |
| DevTools | The profile you recorded | Warm cache, dev build, a fast laptop, and a Lighthouse score that moves ten points between runs |
| Build & Deploy | Secrets are in env vars, not the bundle | Prefixed vars are inlined at build time and cached on a CDN after you delete them |

### The two rows that turn into security tickets rather than performance ones

**A query key missing a variable serves one user's data under another's question.**
It reads as a caching glitch and is an authorisation bug, and the sibling of it is a
query cache that is never cleared on sign-out — the next person on a shared browser
gets cached responses belonging to the last.

**A preview deploy is a public URL.** Every pull request gets a live, generally
unauthenticated environment, and if it is wired to real services then anyone with the
link — including whatever crawled the PR comment — is talking to production data.
Preview environments want their own credentials, their own data, and password
protection: a five-minute setting and an expensive omission.

### One thing the site was implying and should not

"Never put secrets in frontend env vars" is correct and is not where teams get caught.
The mechanism is that bundlers inline `VITE_`/`NEXT_PUBLIC_`/`REACT_APP_` variables at
build time, so a misplaced key is a literal string in a JavaScript file on a CDN —
which survives deleting the variable, survives rotating the key, and is only removed
by a rebuild and a purge. The card now says to grep the built output in CI, because
checking the config cannot find this and checking the bundle always can.

### The measurement

```
                          before   after
thin topics                   77      73
web thin                       8       4   (21% → 10%)
mean chars/concept card    1,261   1,262   ← +1 over four cards
median topic               3,268   3,276
10th percentile            1,529   1,552
```

Five waves this session: **29 cards, thin 102 → 73, counter-metric +6 characters, and
the 10th percentile up 68.** Every wave used a different spec, because the question a
domain has not answered is different in each — *what you must already have* for
offensive tools, *what it cannot see* for defensive ones, *the default that is wrong*
for cloud, *the failure mode of the idea* for devops, and *what is true on your
machine and false for users* for the frontend. A single spec applied across all of
them would have produced five versions of the same card.

Check PASS · smoke **142/142** · axe **6/6** · mobile **9/9** · visual **2/2** ·
determinism reproducible.

---

## Session record — the script tail: what choosing this decides for you

`script`'s thin cards are tours — a language or a tool, its syntax, its ecosystem,
a verdict. Accurate, and they answer *what is this* without answering the question
someone reading them is actually about to face: **what does picking this decide on my
behalf, and what does that make expensive?** Every technology here has already made a
set of trade-offs; adopting it is inheriting them, and the inherited ones are what
show up eighteen months later.

| Card | What it makes cheap | What it makes expensive |
|---|---|---|
| Rust | A whole class of memory and concurrency bugs, gone at compile time | Prototypes whose shape is still moving; shared-mutable graphs; build times |
| Java | Long-lived services — mature GC, real production profiling | Cold starts, footprint, and autoscaling that adds cold instances during a spike |
| PHP | Shared-nothing request handling: leaks cannot accumulate, one crash costs one request | Anything that must live between requests — pools, caches, sockets |
| C | The ABI everything links against; freestanding targets | Everything else — and "we are careful" is not a strategy, tooling is |
| Kafka | Replayable, decoupled event flow | The partition key, which decides ordering, parallelism and skew at once |
| Spark | Data that genuinely exceeds one machine | Every shuffle — and the premise, now that DuckDB and Polars exist |

### Three things that were worth writing down

**Undefined behaviour is a licence, not a crash.** The C card described UB as going
off the rails. The modern reality is that an optimiser assumes UB never happens and
reasons *backwards*: a null check placed after a dereference gets deleted, because the
dereference proves the pointer was non-null. The defensive check disappears and the
bug it guarded becomes exploitable — at `-O2`, on one compiler, often after an
upgrade. That reframes the practices from hygiene to necessity.

**Java's JIT warm-up decides the deployment shape before a line is written.** A
runtime that gets faster the longer it runs is the best case in the industry for a
long-lived service and a poor fit for a 200ms function. Virtual threads are the
biggest change to that story in twenty years, because they remove the main reason
teams reached for a different runtime.

**Kafka's partition key is the architecture.** Ordering exists only within a
partition, so keying by customer gives you the ordering you meant and a hot partition
if one customer is enormous; the partition count caps the consumer group forever,
because partitions add easily and never come off. Most "Kafka incidents" are a hot
partition, a rebalance storm, or an at-least-once delivery into a non-idempotent sink.

### The measurement

```
                          before   after
thin topics                   73      67
script thin                   14       8   (9% → 5%)
mean chars/concept card    1,262   1,264   ← +2 over six cards
median topic               3,276   3,281
10th percentile            1,552   1,569
```

Six waves this session: **35 cards, thin 102 → 67 (a third of the tail gone),
counter-metric +8 characters, 10th percentile up 85.**

Check PASS · smoke **142/142** · axe **6/6** · mobile **9/9** · visual **2/2** ·
determinism reproducible.

---

## Session record — the long tail across four domains, and a note on what the counter-metric can and cannot see

Seven cards finishing the cloud provider-tour set and starting on `eng` and `linux`.
Same discipline as the six waves before it, applied to whatever question each card had
not answered.

| Card | The thing that was missing |
|---|---|
| AWS CLI & CloudShell | The credential chain decides which account you just changed — an exported key outranks the profile you named |
| gcloud CLI & Cloud Shell | Two independent contexts, and two logins: `auth login` and `auth application-default login` are different identities |
| AWS-Native IaC | "No state file to manage" means AWS manages it, including the automatic rollback that deletes the database it just created |
| Azure Core | A resource group is a lifecycle container, not a security, network or billing boundary — and its region is only where its metadata lives |
| Tech Lead vs EM | Both tracks fail in year one the same way: by not letting go of the work that earned the promotion |
| Linux permissions | `w` on a *directory* is enough to delete a read-only file you do not own — which is what the sticky bit is for |
| Podman rootless | Rootless is a UID mapping, and every confusing thing about it follows: bind-mount denials, ports under 1024, and containers that die at logout without `enable-linger` |

### A gate caught a rendering bug the eye would not

`lint_content` refused the build over a single cell: `c-cyan` on the *first* cell of a
`.ref-table` row never renders, because `td:first-child` outranks it. The class was
present, the markup was valid, the colour would simply not have appeared — and the row
in question was the one meant to stand out. Moved to the second cell. That check
exists because this exact class of "styled and invisible" mistake is unreviewable by
reading the diff.

### What the padding counter-metric actually measures

Mean characters per concept card has moved **1,254 → 1,266 across this session's
42 cards**, and it is worth being precise about why, because the rule in this file
says it must not rise.

The metric detects padding by rising when *existing cards get wordier*. Every card in
these seven waves was **appended**, not edited: `git show --numstat` over the seven
content commits reports 1,301 insertions and 9 deletions in `data/*.html`, and the
nine deletions are the acronym annotator reflowing lines plus two hand-fixed word
choices. No existing prose was lengthened by a single character.

So the twelve-character rise is arithmetic, not padding: the new cards are denser than
the site's mean — a table plus a verdict runs 1,500–2,500 characters against a mean of
1,266 — and adding above-average cards raises an average. The measure that would catch
real padding here is the one to watch instead: **the 10th percentile has moved
1,484 → 1,584 and the median 3,242 → 3,291**, which is what it looks like when cards
leave the tail rather than when everything gets longer.

```
                          session start   now
thin topics                        102     60
mean chars/concept card          1,254  1,266   (+12 over 42 appended cards)
median topic                     3,242  3,291
10th percentile                  1,484  1,584
```

Check PASS · smoke **142/142** · axe **6/6** · mobile **9/9** · visual **2/2** ·
determinism reproducible.

---

## Session record — finishing redteam: the tail of the offensive-tool set

Five more cards under D11's spec, taking `redteam` from the worst thin ratio on the
site (28% at the start of the session) to **5%**.

| Tool | What must already be true | The control that denies it |
|---|---|---|
| John the Ripper | Someone gave you the *file* — an archive, a private key, a KeePass database | The share ACL, the key storage, the vault: the extraction is the finding, the crack is the second one |
| CloudFox / enumerate-iam | A cloud credential that should not have reached you | Not "least privilege" — key issuance, secret scanning, IMDSv2, OIDC federation, one per route |
| theHarvester / Recon-ng | A scope that covers what the module you enabled actually touches | Nothing technical: enumerate your modules and record them |
| BadUSB / RF implants | Proximity **and** an unlocked session, an unencrypted badge, or a system with no rolling code | Lock timeouts and USB device control; a badge generation change; a system replacement |
| OWASP ZAP | A session it can hold and a route list it cannot discover | — the coverage claim is the finding here, not a control |

### Three things that changed how a card reads

**"Passive" is a property of the configuration, not of the tool.** `-b all` enables
sources indiscriminately, and among them are modules that resolve, screenshot or probe
discovered hosts — active reconnaissance against infrastructure that may not be in
scope, from your address. The card's instruction is to enumerate the modules you
enabled and put them in the report, which is the difference between a defensible
engagement and an argument.

**An unauthenticated DAST scan of a single-page application tests the login page.**
The spider finds one route, the interesting ones are behind the session, and the
baseline scan attacks nothing by design. So the pipeline should fail on *new* findings
against a reviewed baseline rather than on a total — an absolute-count gate acquires a
permanent exception within a fortnight.

**Software-defined radio has a legal prerequisite the engagement letter cannot
grant.** Transmitting on licensed spectrum is an offence in most jurisdictions
regardless of what the client authorised, so receive-only is the default and
transmitting is a separate, explicit decision.

### The measurement

```
                          before   after
thin topics                   60      55
redteam thin                   8       3   (14% → 5%; 28% at session start)
mean chars/concept card    1,266   1,267
median topic               3,291   3,304
10th percentile            1,584   1,638
```

Check PASS · smoke **142/142** · axe **6/6** · mobile **9/9** · visual **2/2** ·
determinism reproducible.
