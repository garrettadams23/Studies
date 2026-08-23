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

**In progress — Y1–Y3 were already built (endpoint reached 29 cards since this track
was speced), Y5 shipped this session.** endpoint is now 34. Remaining: Y4 provisioning
depth, Y6 compliance/CA depth, Y7 MECM site design, Y8 analytics/fleet. `[x]` marks
the card that fills each item below.

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
- [ ] Autopilot Deep — profiles, hash harvesting, deployment modes, hybrid vs Entra join
- [ ] Autopilot Device Preparation — the newer flow, and how it differs
- [ ] Driver Management — DISM, driver packs, and the Autopilot driver dilemma
- [ ] Provisioning Packages & Bulk Enrolment — the escape hatch when Autopilot cannot
- [ ] Reprovisioning & Device Reuse — wipe, fresh start, retire, and what each actually removes

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
- [ ] MECM Site Design — CAS, primary, secondary, and when each is justified
- [ ] Boundary Groups Done Right — fallback, relationships, and the classic misconfiguration
- [ ] Collections & Queries — WQL that does not melt the site server
- [ ] Co-management Workloads — moving each slider, safely, in order
- [ ] Retiring MECM — the honest migration path to cloud-only, and what genuinely blocks it

**Wave Y8 — Endpoint Analytics & the Fleet**
- [ ] Endpoint Analytics — startup score, app reliability, work-from-anywhere metrics
- [ ] Proactive Remediations — detect-and-fix scripts as a first-class tool
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
- [ ] Remaining: sizing/overcommit deep, VM lifecycle/templates, live migration ops, P2V/V2V, storage fundamentals/SAN/NAS/performance/tiering, backup targets & products, failover/failback drill, tabletop, post-incident review (narrower depth — follow on demand)

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
- [ ] The Object Pipeline — the thing that makes PowerShell different from Bash
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
- [ ] **Visual regression** — headless screenshots of a few representative
  topics in both themes, diffed on PRs.
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
- [ ] Signals — analogue vs digital, sampling, noise, grounding — still open; the noise and
  grounding half is the part with real IT application
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
- [ ] **Depth, re-audited later:** all three cards are short — 4.6 KB, 4.4 KB and 3.7 KB, two
  concept cards each — so the track is covered at concept level and thin underneath. The two items
  with the most genuine room left are *Certificate &amp; PKI Migration* (chains, hardware security
  modules, and the long tail of embedded devices that will never receive a new algorithm) and
  *Reading a Cryptographic Claim Critically*. Neither is a rewrite; both are depth on an existing
  card or one new card each.

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
- [ ] Teaching a Tool You Just Learned — the honest way to do it — still open; a small, genuine
  card about the credibility of teaching from one step ahead

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
- [ ] Subcontracting & Partnering — growing past your own hours — still open
- [x] Knowing When to Stop — bad clients, bad engagements, exiting cleanly — the closing section of
  the business-side card

**Wave AV4 — Specialist Practices**
- [ ] Running a Security Assessment Engagement — rules of engagement to final debrief
- [ ] Fractional & Advisory Roles — vCISO, fractional IT director; scope and boundaries
- [ ] Expert Witness & Forensic Work — standards, impartiality, and report discipline
- [ ] Training & Workshop Delivery as a Product — packaging what you know
- [ ] Productising a Service — from bespoke hours to a repeatable offer

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
- [ ] **Fact-anchor comments** — for claims that are version-specific ("six
  levels of management groups", "93 days of platform metrics"), an HTML comment
  naming the source, so the next reader can re-verify rather than re-research.
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
- [ ] **Screenshot-dated warnings** — any card describing a vendor UI gets a
  "console as of <date>" note, because those age fastest of all.

### TRACK AY — Content Model & Build Evolution

Recorded with trade-offs rather than as a recommendation, because it is the kind
of change that is easy to start and expensive to abandon.

- [ ] **Evaluate a structured content model** — topics as data (JSON/YAML with
  typed blocks: prose, table, code, diagram) rendered by `build.py`, instead of
  hand-written HTML. **For:** mechanical validation, trivial exports (Markdown,
  print, quiz questions), no more inline-style drift, and every card becomes
  queryable. **Against:** 900 existing topics to migrate, HTML is currently
  expressive and easy to hand-edit, and the build becomes a real program.
  **Decision rule:** only worth it if Tracks AG/AK actually need topic-level
  structured data — do not do it for tidiness alone.
- [ ] **Incremental path if that is a yes** — new domains author in the new model
  and old ones stay HTML; `build.py` handles both. Never a big-bang migration.
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
- [ ] Secrets in Kubernetes — why the built-in kind is only base64, and the options — still open;
  partly reached by the etcd row and the token card, but the options comparison is unwritten

**Wave BC3 — Network & Identity** — shipped into `cloud`, except where noted.
- [x] Network Policies — default-deny, and why almost nobody has it
- [x] Service Mesh Security — mTLS, authorization policy, and the complexity cost — same card, so
  the "network policy first, mesh only for the second column" judgement is stated once
- [x] Workload Identity — federating pods to cloud IAM without long-lived keys — inside the
  service-account token card, where the audience field explains the mechanism
- [ ] Ingress & API Exposure — the gateway as a control point — still open
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
- [ ] Third-Party Data Sharing — contracts, technical limits, and verification — still open; the
  vendor-contract half is in `grc`'s third-party cards, the technical-verification half is not
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
| **Content goes stale** — vendor renames, dead consoles, changed limits | High | High | Phase-5 Track AX: freshness metadata, volatility tags, rename registry | Planned |
| **Scope paralysis** — 751 open items is demotivating rather than motivating | High | Medium | Treat the plan as a menu; the "actual priority" list at the end of Phase 5 | Partly |
| **Progress data loss** — everything is `localStorage`; clearing the browser wipes it | Medium | Medium | Phase-4 Track AG: export/import | **Mitigated** — session 10 shipped export/import with merge, replace and preview |
| **Page weight** — `index.html` is 3.4 MB and grows with every wave | Medium | Medium | Measured in session 14 — it is not slow. `tools/page_budget.py` enforces size and element budgets in CI; lazy loading stays unbuilt until a budget is hit | **Mitigated** |
| **Generated-file drift** — `acronym.html` / `index.html` committed stale | Medium | Low | CI already rebuilds and fails on drift; `--check` mode on the annotator | **Mitigated** |
| **Slug churn** — renaming a topic silently breaks permalinks and progress | Medium | Medium | Phase-5 Track AY: ID stability contract and alias map | Planned |
| **Accuracy drift** — a confident wrong card is worse than no card | Medium | High | Authoring rule 6; Phase-5 fact-anchor comments | Partly |
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
| Mainframe & legacy systems (z/OS, COBOL, AS/400) | `infra` | Genuinely uncovered and genuinely still running banks — worth **one card** on why it persists and how it integrates, not a track |
| Reverse engineering & binary analysis | `redteam` / Track M | Partly implied by malware analysis in Track K; add explicitly to M if it is ever a working need |
| Accessibility engineering (beyond WCAG basics in `web`) | `web` | Two cards at most: testing with assistive tech, and remediation workflow |
| Internationalization engineering | `web` | One card; the site itself has rejected translation, so this is for the reader's products |
| Payments & fintech infrastructure | `data` / `grc` | PCI DSS is already covered; the rest is a niche |
| Blockchain & distributed ledger | — | **Rejected.** Low operational relevance to this site's readership, and the security angle is already covered by key management |
| HPC & scientific computing | — | **Rejected.** Different career entirely |
| Video, streaming & media engineering | — | **Rejected.** Same reason |
| Technical SEO & web operations | `web` | One card, and only because the site itself has SEO tags |

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

## 2. The lint TREND, which has not moved

`lint_content.py` has tracked these as warnings for fourteen sessions and none has gone
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
| `philosophy` | 14 | Under; plausibly fine, it is a coherent subject, and now the home for the `spirit` cards and minimalism |
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
