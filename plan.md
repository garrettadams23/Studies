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

**Remaining backlog: 897 content cards and 44 engineering items** across
Phases 3–6, which would take the site from 943 topics / 27 domains to roughly
1,800 topics / 26 domains — about 180 working sessions.

**If you read only two things:** *"What is actually outstanding"* at the very end
of this file, and *Part 3 of Phase 6* (how to write a card, the pattern library,
the risk register). The backlog is a menu, not a queue — and at this size, how
well each card is written matters more than how many remain.

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

**Wave J1 — Application Security**
- [ ] OWASP Top 10 Deep — one card walking every category with fixes
- [ ] Injection Family — SQLi, command, LDAP, template, NoSQL injection
- [ ] Broken Access Control — IDOR, path traversal, privilege escalation in apps
- [ ] SSRF, XXE & Deserialization — the server-side heavy hitters
- [ ] Secure SDLC & Threat Modeling — STRIDE, abuse cases, security gates

**Wave J2 — API & Cloud-Native Security**
- [ ] API Security — OWASP API Top 10, BOLA, rate limiting, API gateways
- [ ] OAuth/OIDC Security Deep — PKCE, token types, common flow mistakes
- [ ] Container Security Deep — image scanning, runtime, capabilities, seccomp
- [ ] Kubernetes Security Deep — pod security, admission control, RBAC pitfalls
- [ ] DevSecOps — shifting left, SAST/DAST/SCA in CI, policy gates

**Wave J3 — Cryptography Engineering**
- [ ] Symmetric Crypto Deep — AES modes (GCM/CBC/CTR), nonces, AEAD
- [ ] Asymmetric & Key Exchange — RSA vs ECC, Diffie-Hellman, forward secrecy
- [ ] Hashing & Password Storage — bcrypt/scrypt/Argon2, salts, HMAC
- [ ] Crypto in Practice — what to use (libsodium), what never to roll yourself
- [ ] Post-Quantum Cryptography — why it matters, ML-KEM/ML-DSA, the migration

**Wave J4 — Detection & Defensive Engineering**
- [ ] Data Loss Prevention (DLP) — classification, egress controls, insider risk
- [ ] Network Security Architecture — segmentation, microseg, DMZ, egress filtering
- [ ] Web App Firewalls & RASP — where they help and where they don't
- [ ] Secrets & Key Management Deep — HSMs, KMS envelope encryption, rotation
- [ ] Security Logging Strategy — what to log, retention, the audit trail

**Wave J5 — Identity & Modern Auth**
- [ ] Modern IAM Architecture — IdP, SSO, SCIM provisioning, lifecycle
- [ ] Zero Trust Implementation — beyond the buzzword: policy, device trust, ZTNA
- [ ] Privileged Access Management (PAM) — vaulting, JIT access, session recording
- [ ] Federation Deep — SAML vs OIDC assertions, trust chains, common attacks
- [ ] Passwordless & Passkeys Deep — FIDO2/WebAuthn ceremony, attestation

---

## TRACK K — Threat, Malware & Intel Depth  (→ `threat`)

~4 waves, ~22 cards.

**Wave K1 — Malware Analysis**
- [ ] Static Analysis — strings, PE/ELF headers, imports, packing detection
- [ ] Dynamic Analysis — sandboxing, behavioral indicators, API monitoring
- [ ] Reverse Engineering Basics — Ghidra/IDA, disassembly, decompilation
- [ ] Malware Families — loaders, RATs, infostealers, rootkits, wipers
- [ ] Anti-Analysis Techniques — obfuscation, anti-VM, anti-debug (and defeating them)

**Wave K2 — Adversary Knowledge**
- [ ] APT Case Studies — how nation-state campaigns actually unfolded
- [ ] Ransomware Deep — RaaS ecosystem, double extortion, negotiation, recovery
- [ ] Initial Access Brokers & the Criminal Economy — how breaches get sold
- [ ] Supply-Chain Attacks — SolarWinds, XZ, npm/PyPI poisoning, dependency confusion
- [ ] Living-off-the-Land at Scale — LOLBins/LOLDrivers from the defender's view

**Wave K3 — Frameworks & Modeling**
- [ ] MITRE ATT&CK Deep — tactics/techniques/procedures, sub-techniques, data sources
- [ ] MITRE D3FEND & Engage — mapping defenses and deception to ATT&CK
- [ ] The Diamond Model — adversary/capability/infrastructure/victim
- [ ] Threat Modeling Methodologies — STRIDE vs PASTA vs attack trees
- [ ] Cyber Threat Intel Programs — requirements, collection, dissemination, feedback

**Wave K4 — Incident Response Deep**
- [ ] The IR Lifecycle — NIST/SANS phases with concrete playbooks
- [ ] Containment Strategies — isolate vs monitor, the eradication decision
- [ ] Forensic Acquisition — order of volatility, imaging, memory capture
- [ ] Timeline Reconstruction — correlating logs, super-timelines, pivoting
- [ ] Tabletop Exercises & Postmortems — practicing before the real thing

---

## TRACK L — GRC, Compliance & Risk Depth  (→ `grc`)

~4 waves, ~22 cards. The framework-by-framework reference practitioners actually need.

**Wave L1 — The Big Frameworks**
- [ ] ISO/IEC 27001 & 27002 — the ISMS, Annex A controls, certification path
- [ ] SOC 2 — trust services criteria, Type I vs II, what an audit involves
- [ ] PCI-DSS — the 12 requirements, scope reduction, SAQ vs ROC
- [ ] HIPAA — privacy vs security rule, PHI, safeguards, breach notification
- [ ] FedRAMP & NIST 800-53 — control baselines, ATO, the government cloud path

**Wave L2 — Risk & Assurance**
- [ ] Quantitative Risk — ALE/SLE/ARO, and FAIR for defensible risk numbers
- [ ] Risk Treatment — accept/mitigate/transfer/avoid, risk registers, appetite
- [ ] The Controls Universe — preventive/detective/corrective, control mapping
- [ ] Internal Audit Deep — evidence, sampling, findings, remediation tracking
- [ ] Metrics & Reporting to the Board — KRIs, maturity models, telling the story

**Wave L3 — Privacy & Governance**
- [ ] GDPR Deep — lawful basis, data subject rights, DPIAs, cross-border transfers
- [ ] US Privacy Patchwork — CCPA/CPRA and the state-law landscape
- [ ] Privacy Engineering — privacy by design, data minimization, PETs
- [ ] Data Governance — ownership, stewardship, cataloging, retention schedules
- [ ] Records & eDiscovery — legal hold, retention, defensible deletion

**Wave L4 — Third-Party & Resilience**
- [ ] Vendor Risk Management — assessments, SIG/CAIQ, continuous monitoring
- [ ] Business Continuity Deep — BIA, RTO/RPO, DR strategies, testing
- [ ] Supply-Chain Risk (GRC lens) — SBOM mandates, EO 14028, attestations
- [ ] Security Program Building — from zero: policy, standards, procedures, culture
- [ ] Regulatory Landscape — DORA, NIS2, SEC disclosure rules, sector regs

---

## TRACK M — Offensive Security Depth  (→ `pentest` / `redteam`)

~4 waves, ~22 cards. Authorized-testing framing throughout, paired detections noted.

**Wave M1 — Web & API Exploitation (hands-on lens)**
- [ ] Burp Suite Pro Workflow — deep: macros, session handling, extensions
- [ ] Auth & Session Attacks — JWT flaws, OAuth abuse, session fixation
- [ ] Business-Logic Flaws — the bugs scanners can't find
- [ ] API Pentesting — enumerating, mass assignment, BOLA/BFLA in practice
- [ ] Client-Side — DOM XSS, prototype pollution, postMessage, CORS abuse

**Wave M2 — Active Directory Attack Paths (study reference)**
- [ ] AD Enumeration Methodology — from a foothold to a map
- [ ] Kerberos Deep — roasting, delegation abuse, golden/silver tickets (+ detections)
- [ ] ADCS Attack Paths — ESC1–ESC16 overview and the defensive fixes
- [ ] Lateral Movement Techniques — and the exact telemetry that catches each
- [ ] Domain Persistence — DCSync/Shadow (concepts) and the blue-team tripwires

**Wave M3 — Cloud & Container Offense (study reference)**
- [ ] Cloud Pentest Methodology — recon → enum → privesc → impact, per provider
- [ ] IAM Privilege Escalation — the classic misconfig chains (+ CSPM detections)
- [ ] Serverless & CI/CD Attacks — poisoned pipelines, OIDC trust abuse
- [ ] Container Escape Techniques — and the runtime controls that stop them
- [ ] Kubernetes Attack Paths — RBAC → cluster admin (+ audit-log detections)

**Wave M4 — Tradecraft & Professionalism**
- [ ] Report Writing — findings, risk ratings, exec summary, remediation
- [ ] Scoping & Rules of Engagement Deep — the legal & safety guardrails
- [ ] OPSEC for Testers — staying in-scope, safe payloads, cleanup
- [ ] Purple-Team Playbooks — running technique-by-technique detection validation
- [ ] The OSCP/Cert Path — how to actually prepare and pass

---

## TRACK N — Linux & Systems Depth  (→ `linux`)

~3 waves, ~16 cards.

**Wave N1 — Linux Security Hardening**
- [ ] SELinux & AppArmor — mandatory access control, contexts, troubleshooting
- [ ] Linux Capabilities & Namespaces — the primitives containers are built on
- [ ] auditd & Hardening — CIS baseline, sudo, PAM, SSH hardening
- [ ] Firewalling — nftables/iptables, firewalld, ufw in practice
- [ ] Secure Boot, LUKS & Integrity — disk encryption, IMA, measured boot

**Wave N2 — Performance & Troubleshooting**
- [ ] The USE Method on Linux — a systematic performance-debug workflow
- [ ] CPU & Memory Tools — top/htop, vmstat, perf, flame graphs, OOM killer
- [ ] Disk & I/O — iostat, iotop, LVM, RAID, filesystems compared
- [ ] Network Debugging — ss, tcpdump, ip, nftables tracing, DNS issues
- [ ] eBPF & Modern Observability — bpftrace, the future of Linux tracing

**Wave N3 — Storage & Ops**
- [ ] LVM Deep — PVs/VGs/LVs, snapshots, resizing, thin provisioning
- [ ] Software RAID & mdadm — levels, rebuilds, monitoring
- [ ] NFS/Samba & Network Storage — sharing files across a network
- [ ] Package & Image Building — rpm/deb, building images, immutable OSes
- [ ] Systemd Advanced — cgroups v2, resource limits, hardening directives

---

## TRACK O — AI Engineering Depth  (→ `ai`)

~4 waves, ~22 cards. From "I use ChatGPT" to building reliable AI systems.

**Wave O1 — How Models Actually Work**
- [ ] Neural Networks From Zero — neurons, layers, weights, backprop (gently)
- [ ] The Transformer — attention, tokens, embeddings, why it changed everything
- [ ] Training Pipeline — pretraining, SFT, RLHF/DPO, what each stage does
- [ ] Inference Internals — the KV cache, context windows, temperature/top-p
- [ ] Classic ML Still Matters — regression, trees, clustering, when not to use an LLM

**Wave O2 — Building With LLMs**
- [ ] Prompt Engineering Deep — few-shot, chain-of-thought, structured output
- [ ] RAG Architecture — chunking, embeddings, retrieval, reranking, evaluation
- [ ] Vector Search Deep — ANN algorithms, hybrid search, pgvector/pinecone
- [ ] Function Calling & Tools — giving models the ability to act
- [ ] Structured Output & Validation — JSON mode, schemas, guardrails

**Wave O3 — Agents & Orchestration**
- [ ] AI Agents — the loop, planning, memory, when agents beat pipelines
- [ ] Model Context Protocol (MCP) — connecting models to tools & data
- [ ] Multi-Agent Systems — orchestration, hand-offs, the coordination cost
- [ ] Agent Frameworks — LangChain/LlamaIndex/Agent SDKs compared
- [ ] Agent Safety & Sandboxing — untrusted output, tool permissions, human-in-loop

**Wave O4 — Production AI (LLMOps)**
- [ ] Evaluation Deep — golden sets, LLM-as-judge, regression testing, drift
- [ ] Cost & Latency Optimization — caching, routing, batching, model tiering
- [ ] AI Security — prompt injection, data exfiltration, the OWASP LLM Top 10
- [ ] Observability for AI — tracing, token accounting, quality monitoring
- [ ] Responsible AI — bias, privacy, hallucination mitigation, governance

---

## TRACK P — Languages & Programming Depth  (→ `script`)

~3 waves, ~18 cards.

**Wave P1 — More Languages (one card each)**
- [ ] Kotlin — modern JVM, coroutines, Android
- [ ] Swift — iOS/macOS, optionals, value types
- [ ] Scala & Functional JVM — the FP-on-the-JVM story
- [ ] Elixir/Erlang — the actor model, fault tolerance, the BEAM
- [ ] Lua · R · MATLAB — embedded scripting & the scientific/stats niche
- [ ] Haskell (a taste) — pure FP, why it makes you a better programmer

**Wave P2 — Programming Craft**
- [ ] Functional Programming — immutability, pure functions, map/filter/reduce, monads (gently)
- [ ] Concurrency & Parallelism — threads, async, actors, locks vs message-passing
- [ ] Memory Management — stack/heap, GC vs manual vs ownership, leaks
- [ ] Error Handling Patterns — exceptions vs results, retries, failing well
- [ ] Testing Deep — TDD, property-based, mutation testing, test doubles

**Wave P3 — Tools & Practices**
- [ ] Debugging Like a Pro — debuggers, print vs breakpoint, bisecting, rubber-ducking
- [ ] Build Systems & Package Managers — across ecosystems, monorepos, lockfiles
- [ ] Regular Expressions Deep — groups, lookaround, backreferences, catastrophic backtracking
- [ ] API Design Deep — REST maturity, versioning, pagination, idempotency
- [ ] Code Architecture in the Small — modules, layering, dependency injection

---

## TRACK Q — Networking Depth  (→ `net`)

~3 waves, ~16 cards.

**Wave Q1 — Routing & Switching Deep**
- [ ] BGP — the protocol that runs the internet, path selection, common issues
- [ ] OSPF & EIGRP — interior routing, areas, convergence
- [ ] IPv6 Deep — addressing, SLAAC, dual-stack, why migration is slow
- [ ] VLANs, STP & Trunking Deep — loops, root bridge, port security
- [ ] QoS — marking, queuing, shaping vs policing, why voice/video need it

**Wave Q2 — Network Services & Security**
- [ ] DHCP & DNS Internals — the full resolution + lease dance, and attacks
- [ ] VPN Deep — IPsec vs WireGuard vs SSL-VPN, site-to-site vs remote-access
- [ ] Load Balancing & Proxies — L4 vs L7, reverse proxies, health checks
- [ ] Network Access Control — 802.1X, RADIUS, NAC, guest isolation
- [ ] Wireless Deep — 802.11 standards, RF, roaming, WPA3, enterprise Wi-Fi

**Wave Q3 — Modern & Cloud Networking**
- [ ] SASE & SD-WAN Deep — the converged network+security cloud model
- [ ] Cloud Networking Patterns — transit gateways, peering, hybrid connectivity
- [ ] Network Troubleshooting Methodology — OSI-layered, the tools per layer
- [ ] Observability for Networks — flow logs, SNMP vs streaming telemetry
- [ ] eBPF & Cilium Networking — the programmable-datapath future

---

## TRACK S — Career, Mind & Life Depth  (→ `lifestyle`)

~4 waves, ~22 cards. The non-technical skills that decide careers.

**Wave S1 — Health for Knowledge Workers**
- [ ] Sleep — the highest-leverage performance lever, and how to protect it
- [ ] Nutrition Basics — energy, focus, and not crashing at 3pm
- [ ] Movement & Ergonomics — desk health, the body behind the keyboard
- [ ] Stress & the Nervous System — recovery, breathwork, actual burnout prevention
- [ ] Focus & Attention — deep work, distraction, the cost of context switching

**Wave S2 — Productivity Systems**
- [ ] GTD — capture, clarify, organize, review; getting it out of your head
- [ ] PARA & PKM — note systems, second brain, Zettelkasten
- [ ] Time Blocking & Prioritization — Eisenhower, MITs, energy management
- [ ] Goal Systems — OKRs for individuals, systems vs goals, habit stacking
- [ ] Learning Systems — spaced repetition, Feynman, deliberate practice

**Wave S3 — Money & Independence**
- [ ] Personal Finance Deep — budgeting, emergency fund, debt payoff order
- [ ] Investing Basics — index funds, compounding, retirement accounts
- [ ] Comp & Equity for Tech Workers — RSUs, options, negotiating an offer
- [ ] Taxes & Freelancing — 1099 vs W2, quarterly, deductions, entities
- [ ] Financial Independence — the math, runway, why engineers reach it

**Wave S4 — People Skills**
- [ ] Negotiation — salary, scope, and everyday asks (BATNA, anchoring)
- [ ] Giving & Receiving Feedback — radical candor, SBI, the hard conversations
- [ ] Managing Up & Across — making your manager and peers effective
- [ ] Public Speaking & Presenting — talks, demos, executive updates
- [ ] Conflict & Difficult Conversations — de-escalation, finding the real issue

---

## TRACK T — Military, Leadership & Decision-Making Depth  (→ `military`)

~3 waves, ~17 cards. Frameworks that transfer directly to tech leadership & IR,
plus the classified-information handling an IT professional on a cleared
contract is expected to know on day one.

**Wave T1 — Planning & Operations**
- [ ] The Military Decision-Making Process (MDMP) — full planning cycle
- [ ] Intelligence Cycle — direction, collection, processing, dissemination
- [ ] Logistics & Sustainment — the unglamorous thing that wins
- [ ] Mission Orders & Operations Order (OPORD) — the 5-paragraph format
- [ ] Risk Management (Military) — the deliberate risk process, applied anywhere

**Wave T2 — Leadership Under Pressure**
- [ ] Mission Command Deep — decentralized execution, trust, disciplined initiative
- [ ] Crisis Leadership — decision-making with incomplete info (ties to IR/on-call)
- [ ] Building Cohesive Teams — trust, shared hardship, morale
- [ ] Red Teaming as a Discipline — structured contrarian thinking, premortems
- [ ] Small-Unit Leadership Lessons for Tech Leads — direct parallels to eng teams

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

**Wave U1 — Certification Study Guides**
- [ ] CompTIA Security+ — objective-by-objective map to site topics
- [ ] CISSP — the 8 domains, mapped to Red/Blue/Cloud/GRC cards
- [ ] AWS/GCP/Azure Cert Paths — which cards cover which exam objectives
- [ ] OSCP & Offensive Certs — the practical prep plan
- [ ] Cloud & DevOps Certs — CKA/CKAD/Terraform Associate study maps

**Wave U2 — Interview Prep Hubs**
- [ ] System Design Interview — a reusable template + worked examples
- [ ] Coding Interview — patterns (two-pointer, sliding window, DP, graphs)
- [ ] Behavioral Interview — STAR bank mapped to leveling rubrics
- [ ] Security Interview — blue/red/GRC question banks
- [ ] SRE/DevOps Interview — debugging, on-call scenarios, design

**Wave U3 — Hands-On Labs & Projects**
- [ ] Build a Home Lab — from one old PC to a full security lab
- [ ] Build a SIEM at Home — ELK/Wazuh + generating & hunting logs
- [ ] Build a CI/CD Pipeline End-to-End — code → test → scan → deploy
- [ ] Deploy a Full-Stack App — DB + API + frontend + IaC + observability
- [ ] Capture-the-Flag Walkthroughs — how to approach a CTF, categories, tools

**Wave U4 — Reference Sheets & Meta**
- [ ] Ports & Protocols Cheat Sheet — the ones exams and jobs actually test
- [ ] Regex / SQL / Git / Linux One-Page Cheat Sheets — printable quick-refs
- [ ] Incident Response Runbook Templates — fill-in-the-blank playbooks
- [ ] Decision Trees — "which database/language/cloud service/auth method?" pickers
- [ ] Glossary — the acronym soup, one searchable place

---

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

**Wave V1 — Windows Server Foundations**
- [ ] Windows Server Editions & Licensing — Standard vs Datacenter, CALs, Core vs Desktop Experience
- [ ] Server Core & Administration at Scale — why no GUI, and how you manage it anyway
- [ ] Server Manager, RSAT & Windows Admin Center — the three consoles and when each wins
- [ ] Roles & Features — what installing a role actually changes
- [ ] Server Hardening Baseline — LAPS, no browsing, minimal roles, audit policy

**Wave V2 — Active Directory Domain Services**
- [ ] AD DS Architecture — forest, domain, tree, OU, site; what each boundary really means
- [ ] Domain Controllers & FSMO Roles — the five roles, who holds them, seizing vs transferring
- [ ] AD Replication — multi-master, USN, tombstones, `repadmin` triage
- [ ] Trusts — forest/external/shortcut, direction vs transitivity, SID filtering
- [ ] Sites, Subnets & Site Links — why clients authenticate against the wrong DC

**Wave V3 — Group Policy in Practice**
- [ ] Group Policy Architecture — GPO, GPC/GPT, SYSVOL, where settings actually live
- [ ] Processing Order & Precedence — LSDOU, enforcement, blocking, loopback
- [ ] Filtering — security filtering vs WMI filtering vs item-level targeting
- [ ] Group Policy Preferences — the half of GPO people forget exists
- [ ] GPO Troubleshooting — `gpresult /h`, RSoP, `gpupdate /force`, and reading the Group Policy operational log

**Wave V4 — Identity Operations**
- [ ] Users, Groups & Nesting Strategy — AGDLP, and why nested groups become a mess
- [ ] Service Accounts — gMSA, delegation, and retiring shared passwords
- [ ] Kerberos in Operations — SPNs, delegation types, ticket lifetimes, clock skew
- [ ] Entra Connect & Hybrid Identity — sync, password hash vs pass-through vs federation
- [ ] Cleaning Up a Legacy Directory — stale objects, orphaned SIDs, over-permissive ACLs

**Wave V5 — Core Network Services (on-prem)**
- [ ] Windows DNS Administration — zones, scavenging, forwarders, conditional forwarders
- [ ] DHCP Administration — scopes, reservations, options, failover, relay
- [ ] IPAM & Address Discipline — when a spreadsheet stops being enough
- [ ] Time Sync — the PDC emulator, `w32tm`, and why Kerberos dies without it
- [ ] File Services — shares, NTFS vs share permissions, DFS-N/DFS-R, quotas

**Wave V6 — Certificate Services**
- [ ] AD CS Design — root vs issuing CA, offline roots, CRL/OCSP publishing
- [ ] Certificate Templates — the settings that matter, and the ones that get you owned
- [ ] Auto-enrolment — getting certificates onto devices without touching them
- [ ] Certificate Lifecycle Ops — renewal, revocation, the expiry outage nobody schedules
- [ ] ADCS Misconfiguration — ESC1–ESC8 from the defender's side (pairs with `redteam`)

**Wave V7 — Server Operations & Troubleshooting**
- [ ] Windows Event Log Triage — the channels worth watching, and building a useful filter
- [ ] Performance Monitor & Resource Monitor — counters that actually diagnose
- [ ] Windows Patching Strategy — rings, maintenance windows, reboot coordination
- [ ] Domain Controller Recovery — authoritative vs non-authoritative restore, DSRM
- [ ] Decommissioning a Server Properly — the checklist that prevents next year's mystery outage

### TRACK W — Microsoft 365 & Collaboration  (→ new `m365` domain)

~6 waves, ~30 cards. The tenant most organisations live inside.

**Wave W1 — Tenant Foundations**
- [ ] M365 Tenant Anatomy — tenant, domains, admin centers, and how they relate to Azure
- [ ] Licensing Without Tears — E3 vs E5 vs Business, add-ons, group-based licensing
- [ ] Admin Roles & Least Privilege — the built-in roles worth knowing, and PIM for the rest
- [ ] Service Health & Message Center — knowing about the outage before the tickets
- [ ] Tenant-to-Tenant & Mergers — the migration nobody plans enough time for

**Wave W2 — Exchange Online**
- [ ] Mail Flow Explained — connectors, transport rules, the path a message actually takes
- [ ] Mailbox Types — user, shared, room, equipment, and delegation done right
- [ ] Anti-Spam & Anti-Phish — EOP, Defender for Office, quarantine, safe links/attachments
- [ ] Message Trace & Header Analysis — proving where a message went, and where it died
- [ ] Retention, Litigation Hold & Archiving — legal's requirements in mailbox terms

**Wave W3 — SharePoint & OneDrive**
- [ ] SharePoint Online Architecture — sites, libraries, lists, and the 400-URL trap
- [ ] Permissions Model — groups, inheritance, sharing links, and why it sprawls
- [ ] OneDrive Known Folder Move — redirecting Desktop/Documents without user pain
- [ ] Sync Client Troubleshooting — the top failure modes and their fixes
- [ ] External Sharing & Guest Access — B2B collaboration without leaking the tenant

**Wave W4 — Teams**
- [ ] Teams Architecture — what a team really is (M365 group + SharePoint + Exchange + chat)
- [ ] Teams Policies — meeting, messaging, app and calling policy packages
- [ ] Teams Voice Basics — Phone System, calling plans, Direct Routing, SIP at a glance
- [ ] Teams Call Quality Troubleshooting — CQD, network requirements, the real culprits
- [ ] Governance & Sprawl — naming policy, expiration, the 4,000-team problem

**Wave W5 — Purview, Compliance & Data**
- [ ] Purview Overview — the compliance surface, mapped to what auditors ask for
- [ ] Sensitivity Labels & DLP — classification that survives contact with users
- [ ] Retention Policies vs Retention Labels — the distinction that trips everyone
- [ ] eDiscovery & Content Search — running a legal hold end to end
- [ ] Insider Risk & Audit Log — what is recorded, for how long, and how to search it

**Wave W6 — M365 Operations & Troubleshooting**
- [ ] The PowerShell Modules — Graph, Exchange Online, Teams; connecting and staying connected
- [ ] Graph API for Admins — batch operations, permissions, throttling
- [ ] Reporting & Usage Analytics — adoption data that answers a real question
- [ ] Backup for M365 — why native retention is not a backup
- [ ] M365 Troubleshooting Playbook — tenant, identity, licence, policy, client: in that order

### TRACK Y — Endpoint Engineering Depth  (→ `endpoint`, 13 → ~55)

~8 waves, ~40 cards. The domain closest to the maintainer's day job, and the
thinnest on the site. Builds on the MECM troubleshooting cards already shipped.

**Wave Y1 — Intune Deep: Policy**
- [ ] Configuration Profiles — settings catalog vs templates vs custom OMA-URI
- [ ] Policy Conflicts — how Intune resolves them, and how to prove which one won
- [ ] Security Baselines — applying them without breaking the fleet
- [ ] Administrative Templates in Intune — ADMX-backed policy and its limits
- [ ] Assignment Strategy — user vs device targeting, filters, exclusion groups

**Wave Y2 — Intune Deep: Applications**
- [ ] Win32 App Packaging — `.intunewin`, detection, requirements, dependencies, supersedence
- [ ] Install Contexts — system vs user, and the failures that come from choosing wrong
- [ ] Store, LOB & Enterprise App Catalog Apps — when each is the right vehicle
- [ ] App Protection Policies — MAM without enrolment, on unmanaged devices
- [ ] Application Troubleshooting — reading the IME log like a professional

**Wave Y3 — Windows Servicing & Updates**
- [ ] Windows Update for Business — rings, deferrals, deadlines, pause
- [ ] Feature vs Quality vs Driver Updates — three pipelines with three risk profiles
- [ ] Windows Autopatch — what it takes over, and what it does not
- [ ] Update Compliance Reporting — proving the fleet is patched
- [ ] Emergency Patching — an out-of-band CVE, from advisory to verified deployment

**Wave Y4 — Provisioning & Imaging**
- [ ] Autopilot Deep — profiles, hash harvesting, deployment modes, hybrid vs Entra join
- [ ] Autopilot Device Preparation — the newer flow, and how it differs
- [ ] Driver Management — DISM, driver packs, and the Autopilot driver dilemma
- [ ] Provisioning Packages & Bulk Enrolment — the escape hatch when Autopilot cannot
- [ ] Reprovisioning & Device Reuse — wipe, fresh start, retire, and what each actually removes

**Wave Y5 — Endpoint Security**
- [ ] BitLocker at Scale — silent enablement, key escrow, recovery, TPM attestation
- [ ] Defender for Endpoint & Intune — onboarding, ASR rules, tamper protection
- [ ] Local Admin Rights — removing them, and the endpoint privilege management options
- [ ] Windows LAPS — the modern version, in Entra and in AD
- [ ] Firewall & Removable Media Policy — the two controls auditors always ask about

**Wave Y6 — Compliance & Conditional Access**
- [ ] Compliance Policies Deep — settings, grace periods, and what "non-compliant" costs a user
- [ ] Device Trust End to End — enrolment → compliance → CA → resource access
- [ ] Filters & Dynamic Groups — targeting that scales past a naming convention
- [ ] Reporting on Drift — finding the devices that quietly stopped complying
- [ ] The Identity/Endpoint Seam — the failure mode that lands both teams on the same bridge

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

**Wave Z1 — Hypervisors**
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

**Wave Z3 — Storage**
- [ ] Storage Fundamentals — block vs file vs object, restated for the datacenter
- [ ] SAN & Fabric Basics — LUNs, zoning, multipathing, iSCSI vs Fibre Channel
- [ ] NAS & File Services — SMB/NFS at scale, DFS, quotas, access-based enumeration
- [ ] Storage Performance — IOPS, throughput, latency, queue depth, and which one is your limit
- [ ] Storage Tiering & Capacity Planning — forecasting growth before it becomes an incident

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
- [ ] ITIL 4 Without the Jargon — the practices that survive contact with a real team
- [ ] Incident vs Problem vs Change vs Request — the distinction, and why it matters
- [ ] Priority, Impact & Urgency — building a matrix people actually apply
- [ ] Service Catalog & Request Fulfilment — turning ad-hoc asks into a repeatable service
- [ ] Change Enablement — CAB, standard changes, emergency changes, freeze windows

**Wave AA2 — The Ticket Craft**
- [ ] Writing a Ticket Someone Else Can Solve — the fields that decide resolution time
- [ ] Triage & Categorization — routing correctly the first time
- [ ] Escalation — functional vs hierarchical, and how to hand over without losing context
- [ ] Closing Well — resolution notes, root cause, and the knowledge article that follows
- [ ] Working a Queue — prioritisation, batching, and not drowning

**Wave AA3 — Talking to Humans**
- [ ] The First Ninety Seconds — establishing what actually happened
- [ ] Explaining Technical Things to Non-Technical People — a repeatable method
- [ ] Difficult Conversations — angry users, VIP pressure, saying no
- [ ] Remote Support Skills — screen shares, phone-only diagnosis, guiding blind
- [ ] Writing for Users — emails, outage notices, and status pages people trust

**Wave AA4 — Knowledge & Automation**
- [ ] Knowledge Management — KCS in practice, and keeping articles from rotting
- [ ] Self-Service That Works — password reset, software portal, and their adoption traps
- [ ] Shift-Left — moving fixes from tier 3 toward tier 1 deliberately
- [ ] Ticket Automation — templates, workflows, and where automation backfires
- [ ] Asset & Configuration Management — a CMDB that stays true

**Wave AA5 — Running the Function**
- [ ] Service Desk Metrics — the ones that improve service vs the ones that game it
- [ ] SLAs, OLAs & Underpinning Contracts — the chain of promises
- [ ] Capacity & Shift Planning — staffing a queue that has a shape
- [ ] On-Call Without Burnout — rotations, handovers, escalation policy, comp time
- [ ] Major Incident Management — commander, comms lead, scribe, and the bridge discipline

### TRACK AB — Vendor Networking, Firewalls & Wireless  (→ `net`)

~5 waves, ~25 cards. Complements Track Q's protocol depth with the kit people
actually touch. Vendor-specific, deliberately.

**Wave AB1 — Cisco IOS in Practice**
- [ ] IOS Navigation — modes, `show` commands worth memorising, config archives
- [ ] Switch Configuration — VLANs, trunks, port security, PortFast/BPDU guard
- [ ] Router Configuration — interfaces, static and dynamic routing, ACLs
- [ ] Troubleshooting on IOS — `show interface`, CDP/LLDP, SPAN, debug safely
- [ ] Config Management & Upgrades — backups, staged upgrades, rollback plan

**Wave AB2 — Enterprise Firewalls**
- [ ] Firewall Policy Design — zones, rule order, the implicit deny, documentation
- [ ] Palo Alto Concepts — App-ID, User-ID, security profiles, the commit model
- [ ] FortiGate Concepts — policies, VDOMs, SD-WAN features, logging
- [ ] NAT on Firewalls — source/destination NAT, hairpinning, and reading a flow
- [ ] Firewall Troubleshooting — packet capture, session table, policy lookup order

**Wave AB3 — Wireless Engineering**
- [ ] RF Fundamentals — channels, width, co-channel interference, cell design
- [ ] Site Surveys — predictive vs passive vs active, and reading a heat map
- [ ] Enterprise Wi-Fi Auth — 802.1X, RADIUS, certificates, PSK's remaining niche
- [ ] Controller vs Cloud-Managed — Meraki/Mist/Aruba models compared
- [ ] Wireless Troubleshooting — roaming, sticky clients, retries, "it's slow" triage

**Wave AB4 — Network Operations**
- [ ] Monitoring a Network — SNMP, NetFlow/IPFIX, syslog, streaming telemetry
- [ ] Change Control for Networks — the discipline that prevents the 2 a.m. outage
- [ ] Network Documentation — diagrams that stay current, IP plans, cable schedules
- [ ] Capacity & Utilisation — reading trends before users report slowness
- [ ] Network Automation Basics — Netmiko/NAPALM/Ansible for network devices

**Wave AB5 — Physical & Field**
- [ ] Structured Cabling — standards, labelling, patch panel discipline
- [ ] Rack & Power Planning — U space, PDUs, redundant feeds, airflow
- [ ] Fiber in Practice — types, connectors, cleaning, loss budgets
- [ ] Cutover Nights — planning, comms, rollback triggers, go/no-go
- [ ] Field Toolkit — what to actually carry, and the tests each tool answers

### TRACK AC — Automation for Administrators  (→ `script` + `ops`)

~5 waves, ~25 cards. Scripting aimed at the ops trade rather than at developers.

**Wave AC1 — PowerShell for Real Work**
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

**Wave AC3 — Configuration as Code, On-Prem**
- [ ] Ansible for Windows & Linux — inventory, playbooks, idempotent modules
- [ ] Desired State Configuration — where it still fits
- [ ] Golden Images as Code — Packer, and versioning what you deploy
- [ ] Secrets in Automation — vaults, managed identities, and never a plaintext credential
- [ ] Testing Automation — Pester, dry runs, and a lab that mirrors production

**Wave AC4 — Glue, APIs & Integration**
- [ ] Consuming REST APIs From Scripts — auth, pagination, retries, backoff
- [ ] Webhooks & Event-Driven Ops — reacting instead of polling
- [ ] Power Automate & Logic Apps — the low-code option, and its real limits
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

**Wave AD1 — macOS Administration**
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

**Wave AE1 — Operational Technology & ICS**
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

**Wave AE3 — Scale Extremes**
- [ ] IT for Very Small Organisations — one person, no budget, and what to prioritise
- [ ] IT for the Very Large — federation, delegation, and standardising across business units
- [ ] MSP Operations — multi-tenant tooling, onboarding, and the support model
- [ ] Remote & Distributed Workforces — provisioning, support and security without an office
- [ ] Mergers, Acquisitions & Divestitures — the IT workstream nobody staffs properly

**Wave AE4 — Sustainability, Accessibility & Ethics in Operations**
- [ ] Green IT — power, cooling, hardware lifespan, and the honest carbon maths
- [ ] Accessible IT — assistive technology, procurement, and testing your own tools
- [ ] E-Waste & Secure Disposal — data destruction standards and chain of custody
- [ ] Surveillance vs Monitoring — where legitimate telemetry becomes something else
- [ ] Professional Ethics Under Pressure — the situations that actually come up

### TRACK AF — Working With AI as an IT Professional

~4 waves, ~20 cards. Complements Track O (building AI) with *using* AI at work,
and defending against its misuse.

**Wave AF1 — Using AI Well**
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

- [ ] **Spaced repetition** — an SM-2-style scheduler over the existing
  `known:` / `bookmark:` state, so flashcards resurface on a schedule instead of
  randomly. Store `{id, ease, interval, due}` in `localStorage`; add a "due
  today" count to the FAB.
- [ ] **Acronym quiz mode** — generate questions directly from
  `data/acronyms.json` (expansion → acronym and back). It is the highest-quality
  question source on the site because the answers are already structured, and
  the current MCQ generator has to guess distractors from topic titles.
- [ ] **Better distractors** — pick wrong answers from the *same domain* and,
  where available, the same subject area, so questions stop being trivially
  guessable.
- [ ] **Exam mode** — timed, fixed question count, no feedback until the end,
  then a scored report broken down by domain with links to the weak topics.
- [ ] **Learning paths** — an ordered sequence of existing topic IDs
  (`paths.json`) rendered as a checklist: "Net+ in 30 topics", "First 90 days as
  a UEM engineer", "SOC analyst starter". Pure data over existing content.
- [ ] **Progress dashboard** — reviewed / bookmarked / known per domain over
  time, plus a streak. All from `localStorage`, no backend.
- [ ] **Export & import progress** — a JSON download and restore, so clearing
  browser data is not a catastrophe. Also the only realistic cross-device path.
- [ ] **Per-topic notes** — extend the notepad to attach a note to a topic ID and
  surface it inline when that topic is open.

### TRACK AH — Findability & Navigation

- [ ] **Acronym-aware search** — expand the query through `acronyms.json` so
  searching "Unified Endpoint Management" finds UEM cards and vice versa.
  The data already exists; the search does not use it.
- [ ] **Expansion density toggle** — a header control for the inline acronym
  expansions: *always* (today) / *first use per domain* / *hover only* /
  *off*. Purely a CSS class on `<body>` plus a `localStorage` preference.
  Addresses the one real cost of the acronym feature — density in tables.
- [ ] **Related topics** — a small "see also" strip per topic, driven by a
  hand-curated `related.json` keyed on topic ID, with a script that suggests
  candidates by shared acronyms and title terms.
- [ ] **Domain landing cards** — an intro card at the top of each domain: what it
  covers, who it is for, where to start, what to read next.
- [ ] **Search operators** — `domain:net`, `badge:beginner`, quoted phrases.
- [ ] **Recently viewed** — the last ten topics, in the quick-jump palette.
- [ ] **Deep-link to a card, not just a topic** — anchor IDs on `concept-card`s
  for precise sharing.

### TRACK AJ — Quality Gates & Tooling

*(No "TRACK AI" — the letters would collide with the AI domain.)*

- [ ] **Markup validator in CI** — parse every `data/*.html` with a real HTML
  parser and fail on unclosed or stray tags. A one-off parse run showed the
  markup is currently clean; this keeps it that way.
- [ ] **Content linter** — enforce `CONTRIBUTING.md` mechanically: every
  `.topic` has a `.topic-name`, `.topic-chev` (never `topic-chevron`),
  `ref-table` over `ai-table` for new content, no hard-coded hex colours, no
  inline `style="color:…"`.
- [ ] **Duplicate-slug guard** — fail the build if two topics slugify to the same
  id, since `script.js` silently suffixes them and permalinks shift.
- [ ] **Accessibility CI** — run axe against the built page; enforce contrast,
  landmark and `aria-expanded` correctness on the accordions.
- [ ] **Link & anchor checker** — every `#slug` referenced in prose resolves to a
  real topic; every external link is alive.
- [ ] **Performance budget** — fail if `index.html` grows beyond an agreed size
  without a deliberate bump (it is ~3.2 MB today).
- [ ] **Visual regression** — headless screenshots of a few representative
  topics in both themes, diffed on PRs.
- [ ] **Acronym drift report** — list capitalised tokens appearing in content
  that are *not* in `acronyms.json`, as a to-do queue for the dictionary.

### TRACK AK — Delivery, Performance & Reach

- [ ] **Lazy domain loading (server build only)** — `index.html` is ~3.2 MB of
  HTML; every visitor downloads all 20 domains to read one. Emit per-domain
  fragments plus a shell that fetches on expand, **while keeping the current
  single-file build for `file://`**. Two outputs from one `build.py`, selected
  by a flag. This is the single biggest performance win available, and also the
  riskiest change on this list — it must not break offline or the PWA.
- [ ] **Print packs** — a print stylesheet variant that outputs one domain, or
  one learning path, as a clean revision handout.
- [ ] **Markdown export** — dump any topic or domain as Markdown for notes apps.
- [ ] **PWA polish** — an update prompt when a new `CACHE_VERSION` is available,
  and precache the fragments if lazy loading ships.
- [ ] **Share cards** — generated OG images per domain for link previews.
- [ ] **Reading time & size hints** — per domain, so a study session can be
  planned realistically.

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
- **New domain `hw` 🔧 "Hardware, Electronics & Embedded"** (Track AN). Passes
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

**Wave AL1 — Complexity & Correctness**
- [ ] Big-O in Practice — what the notation hides, and when constants win
- [ ] Time vs Space Trade-offs — caching, precomputation, and the memory you pay
- [ ] Amortized Analysis — why a dynamic array is O(1) "on average"
- [ ] Recursion & Induction — reasoning about a function that calls itself
- [ ] P, NP & Why It Matters to You — intractability, approximation, and knowing when to stop

**Wave AL2 — Data Structures From First Principles**
- [ ] Arrays, Lists & Memory Layout — cache lines, locality, and why arrays win
- [ ] Hash Tables — hashing, collisions, load factor, and the DoS that exploits them
- [ ] Trees — BST, balanced trees, tries, heaps, and what each is actually for
- [ ] Graphs — representations, traversal, shortest path, topological sort
- [ ] Probabilistic Structures — Bloom filters, HyperLogLog, count-min sketch

**Wave AL3 — Algorithms Worth Knowing**
- [ ] Sorting & Searching — the classics, and why your language picked the one it did
- [ ] Divide & Conquer, Greedy, Dynamic Programming — recognising which applies
- [ ] String Algorithms — matching, edit distance, and where regex fits
- [ ] Randomised Algorithms — sampling, reservoir sampling, Monte Carlo
- [ ] Algorithm Interview Patterns — mapped to the site's coding-interview card

**Wave AL4 — Operating System Theory**
- [ ] Processes, Threads & Scheduling — context switches and what they cost
- [ ] Virtual Memory — paging, TLB, page faults, and swap's bad reputation
- [ ] Concurrency Primitives — mutexes, semaphores, condition variables, atomics
- [ ] Deadlock & Livelock — the four conditions, detection, prevention
- [ ] Filesystems From the Inside — inodes, journaling, and crash consistency

**Wave AL5 — Computer Architecture**
- [ ] Instruction Execution — fetch/decode/execute, pipelining, branch prediction
- [ ] Caches & the Memory Hierarchy — L1 to disk, and the numbers every engineer should know
- [ ] Speculative Execution & Its Security Cost — Spectre/Meltdown, explained properly
- [ ] Number Representation — two's complement, IEEE-754, and the bugs each causes
- [ ] Instruction Sets — x86-64 vs ARM64 vs RISC-V, and why the shift is happening

**Wave AL6 — Languages, Compilers & Runtimes**
- [ ] How a Compiler Works — lexing, parsing, IR, optimisation, codegen
- [ ] Interpreters, Bytecode & JIT — the spectrum from Python to the JVM
- [ ] Type Systems — static/dynamic, strong/weak, inference, and what types buy you
- [ ] Garbage Collection Deep — mark-sweep, generational, pauses, tuning
- [ ] Undefined Behaviour & Memory Safety — the class of bug behind most CVEs

**Wave AL7 — Distributed Systems Theory**
- [ ] Time in Distributed Systems — clocks, causality, Lamport and vector clocks
- [ ] Consensus — Paxos and Raft, explained without the paper
- [ ] Consistency Models — linearizable, sequential, causal, eventual
- [ ] Failure Detection & the FLP Result — why "is it down?" has no perfect answer
- [ ] Idempotency, Exactly-Once & the Truth — what is actually achievable

### TRACK AM — Mathematics for IT, Security & AI  (→ `cs`)

~5 waves, ~25 cards. Only the mathematics that pays rent, each card anchored to
a place it already shows up on the site.

**Wave AM1 — Numbers, Logic & Bases**
- [ ] Binary, Hex & Bit Manipulation — masks, shifts, flags; subnetting revisited
- [ ] Boolean Algebra — truth tables, De Morgan, and firewall/query logic
- [ ] Modular Arithmetic — the clock maths behind hashing, checksums and crypto
- [ ] Sets & Relations — the formal spine of SQL joins and access control
- [ ] Proof Techniques for Engineers — invariants, contradiction, counterexample

**Wave AM2 — Probability for Defenders**
- [ ] Probability Fundamentals — independence, conditional probability, expectation
- [ ] Bayes' Theorem — base rates, and why a 99%-accurate detector still floods the SOC
- [ ] Distributions That Matter — normal, Poisson, power-law, long tails in latency
- [ ] Sampling & Confidence — what a percentile really claims, and sample-size sanity
- [ ] Birthday Paradox & Collisions — hash collisions, GUID reuse, key spaces

**Wave AM3 — Statistics for Operations**
- [ ] Descriptive vs Inferential — the mistake most dashboards make
- [ ] Percentiles & Latency — why p99 beats the mean, and how to aggregate it wrongly
- [ ] Anomaly Detection Maths — z-scores, MAD, seasonality, and false-positive cost
- [ ] A/B Testing & Significance — power, p-values, and stopping rules
- [ ] Forecasting Capacity — trend, seasonality, and headroom planning

**Wave AM4 — Mathematics of Cryptography**
- [ ] Prime Numbers & Factoring — why RSA rests on a hard problem
- [ ] Discrete Logarithms & Elliptic Curves — the other hard problem, and why keys shrank
- [ ] Entropy & Randomness — measuring it, and where implementations lose it
- [ ] Information Theory Basics — Shannon entropy, compression, password strength
- [ ] Lattices, Gently — the hard problem post-quantum cryptography moved to

**Wave AM5 — Mathematics for Machine Learning**
- [ ] Vectors & Embeddings — similarity, cosine distance, and what a dimension means
- [ ] Matrices & Linear Transformations — the operation a GPU spends its life doing
- [ ] Derivatives & Gradient Descent — how a model actually learns
- [ ] Loss Functions & Optimisation — what the model is being told to minimise
- [ ] Dimensionality & the Curse — why high-dimensional intuition fails

### TRACK AN — Hardware, Electronics & Embedded  (→ new `hw` domain)

~6 waves, ~30 cards. The physical layer, from a bench repair to a soldered board.

**Wave AN1 — Electronics Fundamentals**
- [ ] Voltage, Current & Resistance — Ohm's law with worked IT examples
- [ ] Power & Thermals — watts, heat, and why the PSU calculation matters
- [ ] Components — resistors, capacitors, diodes, transistors, and reading a schematic
- [ ] Signals — analogue vs digital, sampling, noise, grounding
- [ ] Test Gear — multimeter, oscilloscope, logic analyser: what each answers

**Wave AN2 — PC Hardware Deep**
- [ ] Motherboard Anatomy — chipsets, lanes, headers, and the block diagram
- [ ] CPU & Cooling — sockets, TDP, thermal paste, throttling diagnosis
- [ ] Memory Deep — channels, ranks, timings, ECC, and diagnosing bad RAM
- [ ] Storage Interfaces — SATA/NVMe/PCIe lanes, and where the bottleneck really is
- [ ] Power Supplies — rails, efficiency ratings, sizing, and failure symptoms

**Wave AN3 — Diagnosis & Repair**
- [ ] Systematic Hardware Troubleshooting — isolate, swap, minimum viable system
- [ ] POST, Beep Codes & Diagnostic LEDs — reading a machine that will not boot
- [ ] Intermittent Faults — heat, vibration, marginal power, and how to reproduce them
- [ ] Soldering & Rework — through-hole and SMD basics, and knowing when not to
- [ ] Data Recovery Triage — when to stop and send it to a lab

**Wave AN4 — Peripherals & the Office Estate**
- [ ] Displays — panel types, scaling, colour, multi-monitor and docking pitfalls
- [ ] Printers & MFPs — the technologies, drivers, print servers, and secure release
- [ ] Docks, USB-C & Thunderbolt — power delivery, alt modes, and the compatibility mess
- [ ] Input Devices & Accessibility Hardware — switches, trackballs, ergonomic kit
- [ ] Conference Room Technology — the AV stack, and why it always breaks

**Wave AN5 — Embedded & Single-Board**
- [ ] Microcontrollers vs SBCs — Arduino vs Raspberry Pi, and choosing correctly
- [ ] GPIO, I²C, SPI & UART — talking to the physical world
- [ ] Firmware Basics — bootloaders, flashing, JTAG/SWD, bricking and recovery
- [ ] Real-Time Constraints — RTOS, determinism, and why Linux is not always right
- [ ] Home Lab Hardware — a genuinely useful build, at three budgets

**Wave AN6 — Hardware Security**
- [ ] Hardware Root of Trust — TPM, secure enclaves, measured boot, attestation
- [ ] Firmware & Supply-Chain Attacks — UEFI implants, Option ROMs, vendor trust
- [ ] Physical Attacks — evil maid, DMA attacks, cold boot, chip-off forensics
- [ ] Hardware Hacking Tools — Bus Pirate, logic analysers, JTAG; authorised use only
- [ ] Defending Physical Access — port control, chassis intrusion, screen locks that hold

---

## PART 2 — FRONTIERS

### TRACK AP — Post-Quantum & Cryptographic Migration  (→ `sec`)

~3 waves, ~15 cards. The migration is live now; "harvest now, decrypt later"
makes it an operational problem, not a research one.

**Wave AP1 — The Threat & the Standards**
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

**Wave AQ1 — Edge & Distributed Compute**
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

**Wave AR1 — Physical Security Systems**
- [ ] Access Control Systems — badges, readers, controllers, anti-passback, tailgating
- [ ] Credential Cloning — why 125 kHz prox is not a control, and what to move to
- [ ] CCTV & Video Management — retention, coverage, evidentiary quality, privacy limits
- [ ] Datacenter & Facility Security — layers, mantraps, visitor control, delivery bays
- [ ] Environmental Controls & Monitoring — power, cooling, water, fire suppression

**Wave AR2 — Insider Threat**
- [ ] The Insider Threat Model — malicious, negligent, compromised; each needs a different control
- [ ] Behavioural Indicators — and the ethical line around monitoring people
- [ ] Separation of Duties & Least Privilege in Practice — beyond the slide
- [ ] Offboarding as a Security Control — the checklist and its failure modes
- [ ] Building an Insider Threat Programme — legal, HR and IT together

**Wave AR3 — Investigations**
- [ ] Running an Internal Investigation — scope, authorisation, and staying in your lane
- [ ] Evidence Handling — chain of custody, imaging, hashing, contemporaneous notes
- [ ] Interviewing & Statements — what IT should and absolutely should not do
- [ ] Working With Legal, HR & Law Enforcement — the handoffs and their timing
- [ ] Writing an Investigation Report — findings, evidence, limits, no speculation

**Wave AR4 — OSINT & Attack-Surface Discovery (defensive)**
- [ ] Mapping Your Own Exposure — domains, certificates, cloud, code, people
- [ ] Credential Exposure Monitoring — breach data, paste sites, and responsible use
- [ ] Executive & VIP Exposure — data brokers, doxxing risk, protective steps
- [ ] Brand & Impersonation Monitoring — lookalike domains, fake apps, takedowns
- [ ] Turning Findings Into Work — from a scary spreadsheet to a prioritised backlog

---

## PART 3 — THE BUSINESS OF IT  (→ new `biz` domain)

### TRACK AS — IT Finance, Vendors & Procurement

~5 waves, ~25 cards. Organisational money, not personal money.

**Wave AS1 — The Money Model**
- [ ] CapEx vs OpEx — and why the cloud migration changed the conversation
- [ ] Building an IT Budget — run vs grow vs transform, and defending each line
- [ ] TCO Modelling — the costs that never appear on the quote
- [ ] Chargeback & Showback — making consumption visible without starting a war
- [ ] Business Case Writing — the one-page version an executive will actually read

**Wave AS2 — Buying Well**
- [ ] Requirements Before Vendors — writing them so the demo cannot dazzle you
- [ ] RFI / RFP / RFQ — running a fair process that gets a real answer
- [ ] Evaluating a Vendor — financial health, roadmap, support model, references
- [ ] Proof of Concept Design — success criteria agreed *before* the trial starts
- [ ] Negotiation for IT Buyers — timing, leverage, and what is actually discountable

**Wave AS3 — Contracts & Licensing**
- [ ] Reading a Contract as an Engineer — the clauses that bite operations
- [ ] SLAs, Credits & What They Are Really Worth — an outage refund is not a control
- [ ] Software Licensing Models — per-user, per-device, core-based, consumption
- [ ] Surviving a Licence Audit — preparation, evidence, and the true-up conversation
- [ ] Exit Clauses & Lock-In — data export, transition assistance, and the migration you will do

**Wave AS4 — Cost Control in Operations**
- [ ] Cloud FinOps — showback, rightsizing, commitment discounts, anomaly alerts
- [ ] SaaS Sprawl — discovery, consolidation, and reclaiming unused seats
- [ ] Hardware Refresh Economics — when replacing beats maintaining
- [ ] The Cost of Downtime — modelling it credibly enough to fund resilience
- [ ] Technical Debt as a Financial Argument — translating it into language that funds it

**Wave AS5 — Governance of Spend**
- [ ] Vendor Risk Management — security review, concentration risk, fourth parties
- [ ] Asset Management End to End — procure → deploy → maintain → retire → dispose
- [ ] Portfolio & Prioritisation — deciding what *not* to do, defensibly
- [ ] Benefits Realisation — checking afterwards whether it did what the case claimed
- [ ] Reporting to the Board — three slides, no jargon, no surprises

### TRACK AT — Leading Technical Teams

~5 waves, ~25 cards. Complements the individual-contributor ladder in `eng`.

**Wave AT1 — The Transition**
- [ ] From Engineer to Manager — what you actually stop doing
- [ ] The First 90 Days Leading a Team — listen, map, stabilise, then change
- [ ] Delegation — the levels, and why "I'll just do it" is a trap
- [ ] Your Calendar Is the Strategy — where a manager's time really goes
- [ ] Keeping Technical Enough — staying credible without taking the work back

**Wave AT2 — People**
- [ ] One-to-Ones That Are Worth Having — structure, cadence, and what not to use them for
- [ ] Feedback & Difficult Conversations — specific, timely, and survivable
- [ ] Performance Management — the honest version, including managing someone out
- [ ] Career Development for Your Reports — growth plans that are not just promotion
- [ ] Retention — why good people leave, and the ones you can prevent

**Wave AT3 — Hiring**
- [ ] Writing a Job Description That Attracts the Right Person
- [ ] Designing an Interview Loop — signal per hour, and reducing bias
- [ ] Technical Assessment Without Hazing — realistic tasks, fair scope
- [ ] Reference Checks & Offers — closing well, and the counter-offer conversation
- [ ] Onboarding — the 30/60/90 that produces a contributor, not a spectator

**Wave AT4 — Running the Work**
- [ ] Planning Without Theatre — roadmaps, capacity, and honest estimates
- [ ] Prioritisation Under Pressure — saying no with a reason attached
- [ ] Project Management for Technical Leads — the minimum viable process
- [ ] Managing Incidents as a Leader — comms, decisions, and protecting the responders
- [ ] Metrics for Engineering Teams — what DORA does and does not tell you

**Wave AT5 — Organisation & Influence**
- [ ] Team Topologies — stream-aligned, platform, enabling, complicated-subsystem
- [ ] Conway's Law in Practice — shaping the org to get the architecture you want
- [ ] Managing Up — giving your leadership what they need to back you
- [ ] Cross-Team Politics — alliances, escalation, and picking battles
- [ ] Building a Culture Deliberately — rituals, defaults, and what you tolerate

### TRACK AU — Enablement, Training & Technical Influence

~4 waves, ~20 cards. Teaching as a function, not as a personality trait.

**Wave AU1 — Designing Learning**
- [ ] How Adults Actually Learn — relevance, practice, feedback, spacing
- [ ] Curriculum Design — objectives, sequencing, and cutting the nice-to-know
- [ ] Building a Lab — repeatable, resettable, and cheap enough to keep
- [ ] Assessment That Means Something — beyond a multiple-choice quiz
- [ ] Measuring Training — behaviour change, not attendance

**Wave AU2 — Delivering It**
- [ ] Running a Workshop — pacing, energy, and rescuing the room when it stalls
- [ ] Live Demos That Do Not Fail — rehearsal, fallbacks, recorded escape hatch
- [ ] Screencasts & Async Video — scripting, recording, editing, and length discipline
- [ ] Facilitating a Retrospective or Tabletop — neutrality and the hard question
- [ ] Teaching a Tool You Just Learned — the honest way to do it

**Wave AU3 — Documentation as Infrastructure**
- [ ] Documentation Types — tutorial, how-to, reference, explanation (and mixing them up)
- [ ] Runbooks That Work at 3 a.m. — testable, unambiguous, no missing step
- [ ] Docs-as-Code — review, versioning, CI checks, and ownership
- [ ] Keeping Documentation Alive — review triggers, owners, and deleting the dead
- [ ] Diagrams That Explain — the small number of shapes worth using

**Wave AU4 — Influence Beyond Your Team**
- [ ] Writing a Proposal People Say Yes To — problem, options, recommendation, cost
- [ ] Presenting to Executives — the pyramid principle, and the first thirty seconds
- [ ] Speaking at a Conference — CFP writing, talk structure, rehearsal
- [ ] Community & Open Source Contribution — what it gives back, realistically
- [ ] Building an Internal Community of Practice — starting one that survives month three

### TRACK AV — Consulting, Contracting & Independent Practice

~4 waves, ~20 cards. Complements `lifestyle`'s freelance-tax card with the craft
of running the work.

**Wave AV1 — Positioning**
- [ ] Consultant vs Contractor vs Staff Augmentation — three different businesses
- [ ] Choosing a Niche — why specificity wins work
- [ ] Pricing — hourly, day rate, fixed price, value-based; and their risk profiles
- [ ] Finding Clients — referrals, partners, content, and the honest cold-outreach maths
- [ ] The Proposal & Statement of Work — scope, exclusions, acceptance criteria

**Wave AV2 — Delivering**
- [ ] Discovery — the first two weeks that determine the engagement
- [ ] Managing Scope — change control without becoming the difficult one
- [ ] Working Inside Someone Else's Politics — reading the room you were dropped into
- [ ] Handover & Enablement — leaving a client better, not dependent
- [ ] The Assessment Report — findings, risk-ranked recommendations, and an owner per item

**Wave AV3 — The Business Side**
- [ ] Cash Flow & Runway — invoicing, payment terms, and the late-payer problem
- [ ] Insurance, Liability & Entity Choice — the boring protections that matter
- [ ] Contracts for Independents — IP, indemnity, non-solicit, limitation of liability
- [ ] Subcontracting & Partnering — growing past your own hours
- [ ] Knowing When to Stop — bad clients, bad engagements, exiting cleanly

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

- [ ] **Per-topic freshness metadata** — a `reviewed: YYYY-MM` attribute on each
  `.topic`, surfaced as a quiet badge, and a build report of the oldest 50.
  Start by stamping everything with its last real commit date via `git log`.
- [ ] **Volatility tags** — mark topics as *stable* (OSI model, TCP handshake) or
  *volatile* (vendor consoles, pricing, product names). Only volatile ones need
  an annual review; stable ones can sit for years. Without this distinction a
  freshness system just generates guilt.
- [ ] **Rename/deprecation registry** — a `renames.json` (`Azure AD → Entra ID`,
  `SCCM → MECM`, `CASP+ → SecurityX`) plus a checker that flags superseded names
  in new content and suggests the current one. The acronym pipeline already
  proves this pattern works.
- [ ] **Link rot check in CI** — external links, on a schedule rather than every
  PR, reported as an issue rather than a hard failure.
- [ ] **Fact-anchor comments** — for claims that are version-specific ("six
  levels of management groups", "93 days of platform metrics"), an HTML comment
  naming the source, so the next reader can re-verify rather than re-research.
- [ ] **Per-domain changelog** — an auto-generated "what changed here recently"
  card at the top of each domain, from git history.
- [ ] **Contradiction check** — cross-domain grep for the same acronym or metric
  defined two different ways. This session found three (`CA`, `SPF`, `S3`); a
  script would find the rest.
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
- [ ] **Topic ID stability contract** — write down, in `CONTRIBUTING.md`, that
  topic slugs are a public interface: renaming a `.topic-name` breaks
  permalinks and stored progress. Add an alias map so renames are survivable.
- [ ] **Split `data/script.html`** — at 719 KB and 137 topics it is a third of
  the content in one file and the hardest to work in. It contains at least three
  domains' worth of material (shell/regex, languages, web fundamentals).
  Splitting it into multiple source files that build into the *same* domain
  keeps every slug intact — `build.py` would concatenate `script.*.html`.
- [ ] **Build performance & determinism** — the build is fast today; add a
  guard so it stays reproducible (stable ordering, no timestamps in output).
- [ ] **Archive `patches/`** — ~1.7 MB of already-applied one-shot scripts. Tag
  the current commit, then delete them from `main` with the tag recorded in
  `CONTRIBUTING.md` so the history is recoverable.
- [ ] **A `make` or `just` entry point** — `just build` running gen → annotate →
  build → smoke test, so the four-command sequence cannot be half-run. The
  number of steps is now the most likely source of a stale commit.

---

## Suggested execution order (Phase 5)

Phase 5 assumes Phase 4 is under way but does not depend on it, with one
exception noted below.

| Slot | Tracks | Theme | Rough size |
|---|---|---|---|
| 91 | AH chip grouping + AX freshness metadata | **Do first** — the chip bar breaks before the 24th domain, and freshness metadata is cheapest to add before another 500 topics exist | code only |
| 92–95 | scaffold `cs` + AL1–AL7 | complexity, data structures, algorithms, OS, architecture, compilers, distributed theory | ~35 cards |
| 96–97 | AM1–AM5 | the mathematics that pays rent | ~25 cards |
| 98–100 | scaffold `hw` + AN1–AN6 | electronics, PC hardware, repair, peripherals, embedded, hardware security | ~30 cards |
| 101–102 | AP1–AP3 | post-quantum migration and adjacent cryptography | ~15 cards |
| 103–104 | AQ1–AQ4, AR1–AR4 | emerging platforms; physical security and investigations | ~40 cards |
| 105–107 | scaffold `biz` + AS1–AS5 | IT finance, vendors, contracts, cost control | ~25 cards |
| 108–110 | AT1–AT5 | leading technical teams | ~25 cards |
| 111–112 | AU1–AU4, AV1–AV4 | enablement and independent practice | ~40 cards |
| 113–114 | AX remainder + AY | freshness system, then the content-model decision | code only |

**Phase 5 total: 10 content tracks, 47 waves, 235 cards, 3 new domains**, plus
15 engineering items.

## Where that leaves the site

| | Topics | Domains |
|---|---:|---:|
| Today | 900 | 20 |
| + Phase 3 outstanding (J–U) | 1,107 | 20 |
| + Phase 4 | 1,372 | 23 |
| + Phase 5 | 1,607 | 26 |

**Total remaining backlog across all three phases: 707 cards and 44 engineering
items.** At one wave (~5 cards) per working session that is roughly 140 sessions
— which is the point at which the honest advice is: *do not treat this as a
queue to finish*. Treat it as a menu. Ship the tracks that match what you are
actually doing at work, because those are the ones you will write well and the
ones you will keep using.

## Suggested actual priority, if the list is overwhelming

Ignoring track order entirely, these are the six that would most improve the
site as it stands today:

1. **AH chip grouping + Y1–Y2** — the navigation breaks soon, and `endpoint` is
   both the thinnest domain and the maintainer's day job.
2. **AG spaced repetition + acronym quiz** — turns 900 topics of reference into
   something you revise from, using data that already exists.
3. **AX freshness metadata** — cheapest now, impossible later.
4. **V1–V3 (Windows Server, AD DS, Group Policy)** — the largest genuine subject
   gap on the site.
5. **AL1–AL3 (complexity, data structures, algorithms)** — the most-requested
   interview material, and it is nowhere yet.
6. **AY split of `data/script.html`** — 719 KB in one file is the single biggest
   drag on actually doing any of the above.

---

# Content & Capability Roadmap — Phase 6: Specialisms, and How This Gets Written (Wave 115+)

> **Two halves, deliberately different in kind.**
> The first is nine tracks covering the jobs that split off from "security
> engineer" and "SRE" and became disciplines with their own titles, tooling and
> interview loops. The second is not a plan at all — it is the **authoring
> craft, pattern library, risk register and success measures written out now**,
> because after five phases the constraint on this project is no longer *what to
> write* (751 open items) but *how to write 751 cards that are worth reading*.

## No new domains

Phases 3–5 added eight domains. Phase 6 adds **none**. Every track here lands in
an existing domain — `blueteam`, `redteam`, `sec`, `cloud`, `ops`, `eng`, `grc`.
That is a deliberate correction: 26 domains is already at the edge of what a
filter bar and a mental model can hold, and every one of these specialisms is
recognisably a deeper cut of something the site already covers.

---

## PART 1 — SECURITY ENGINEERING SPECIALISMS

### TRACK BA — Detection Engineering  (→ `blueteam`)

~5 waves, ~25 cards. Writing detections as a software discipline, not as a
tuning exercise in a console. The site has SIEM and EDR cards; it has nothing on
the craft of building what runs inside them.

**Wave BA1 — The Discipline**
- [ ] What Detection Engineering Is — and why it split off from SOC analysis
- [ ] The Detection Lifecycle — idea → hypothesis → logic → test → deploy → tune → retire
- [ ] Detection Requirements — writing one before writing the rule
- [ ] The Pyramid of Pain Applied — choosing what to detect on, and its cost to the attacker
- [ ] Coverage vs Noise — the trade every rule makes, made explicit

**Wave BA2 — Data Before Rules**
- [ ] Log Source Inventory — knowing what you actually collect, and at what fidelity
- [ ] Data Normalization — OCSF, ECS, ASIM; why a schema decides your query
- [ ] Telemetry Gaps — proving a detection cannot fire, before you promise it does
- [ ] Log Volume & Cost — sampling, filtering, and the detections cost quietly kills
- [ ] Enrichment — asset, identity and threat context that turns an alert into a decision

**Wave BA3 — Writing Detections**
- [ ] Sigma as an Interchange Format — writing once, deploying to several backends
- [ ] Detection-as-Code — Git, review, CI, and versioned rules
- [ ] Writing a Good Rule — specificity, false-positive analysis, the tuning fields
- [ ] Behavioural vs Signature Detections — worked examples of both for one technique
- [ ] Correlation & Sequencing — when a single event genuinely is not enough

**Wave BA4 — Testing Detections**
- [ ] Unit-Testing a Detection — synthetic events and expected verdicts
- [ ] Atomic Red Team & Emulation for Validation — proving the rule fires on the real thing
- [ ] Detection Regression — the rule that silently stopped working after a log change
- [ ] Measuring Detection Quality — precision, recall, alert-to-incident ratio, time-to-detect
- [ ] Purple-Team Feedback Loop — closing the gap the exercise found

**Wave BA5 — Running the Programme**
- [ ] ATT&CK Coverage Mapping — honest heat maps, and the lie of "100% coverage"
- [ ] Detection Backlog & Prioritisation — threat model in, rules out
- [ ] Rule Retirement — deleting detections without losing the reason they existed
- [ ] Documentation for Responders — the runbook that ships *with* the rule
- [ ] Detection Engineering Interview — what the role is actually assessed on

### TRACK BB — Adversary Emulation & Purple Teaming  (→ `redteam` / `blueteam`)

~4 waves, ~20 cards. Authorized-use framing throughout, and every offensive card
pairs with the detection it should trigger — the site's existing rule.

**Wave BB1 — Emulation Foundations**
- [ ] Emulation vs Simulation vs Penetration Testing — three different questions
- [ ] Building a Threat Profile — picking an adversary that is relevant to *you*
- [ ] Emulation Plans — CTID plans, and writing your own from intel
- [ ] Rules of Engagement for Emulation — scope, safety, deconfliction, kill switch
- [ ] Lab Design for Emulation — a range that is safe to break

**Wave BB2 — Running an Exercise**
- [ ] Purple Team Mechanics — the room, the roles, the cadence
- [ ] Technique-by-Technique Execution — run, observe, record, adjust
- [ ] Detection Gaps in Real Time — the value that only appears when both teams watch together
- [ ] Evidence Capture — screenshots, timestamps, telemetry references
- [ ] The Debrief — findings that turn into backlog items, not a scorecard

**Wave BB3 — Automation**
- [ ] Breach & Attack Simulation Tools — what they do well, and their blind spots
- [ ] Atomic Testing at Scale — scheduled, safe, continuous validation
- [ ] CI for Security Controls — treating control efficacy as a test suite
- [ ] Safe Payloads — proving execution without doing damage
- [ ] Avoiding Emulation Theatre — when a green dashboard means nothing

**Wave BB4 — Reporting & Value**
- [ ] Writing the Emulation Report — narrative, timeline, gaps, recommendations
- [ ] Mapping Findings to Controls & Owners — every gap gets a name and a date
- [ ] Measuring Programme Improvement Over Time — the metric that survives scrutiny
- [ ] Communicating Risk to Leadership — without either alarmism or false comfort
- [ ] Building the Business Case for Purple — funding the second exercise

### TRACK BC — Cloud-Native & Kubernetes Security  (→ `cloud` / `blueteam`)

~5 waves, ~25 cards. The site teaches Kubernetes operationally; this is the
attack and defence surface.

**Wave BC1 — The Kubernetes Threat Model**
- [ ] What an Attacker Sees — the control plane, the kubelet, etcd, the workloads
- [ ] The Four Cs — cloud, cluster, container, code
- [ ] Kubernetes RBAC Deep — verbs, resources, and the escalation paths people miss
- [ ] Service Accounts & Token Projection — the credential every pod carries
- [ ] etcd & Control-Plane Exposure — the game-over surfaces

**Wave BC2 — Workload Hardening**
- [ ] Pod Security Standards — privileged/baseline/restricted, and enforcing them
- [ ] Container Breakout Paths — privileged pods, hostPath, hostPID, capabilities
- [ ] Admission Control — OPA/Gatekeeper and Kyverno, and policy-as-code
- [ ] Image Security — minimal bases, non-root, read-only filesystems, distroless
- [ ] Secrets in Kubernetes — why the built-in kind is only base64, and the options

**Wave BC3 — Network & Identity**
- [ ] Network Policies — default-deny, and why almost nobody has it
- [ ] Service Mesh Security — mTLS, authorization policy, and the complexity cost
- [ ] Workload Identity — federating pods to cloud IAM without long-lived keys
- [ ] Ingress & API Exposure — the gateway as a control point
- [ ] Multi-Tenancy — namespaces are not a security boundary; what to do instead

**Wave BC4 — Runtime & Detection**
- [ ] Runtime Security — Falco/Tetragon, eBPF-based detection in the cluster
- [ ] Audit Logs — what the API server records, and the queries worth saving
- [ ] Container Forensics — investigating something that no longer exists
- [ ] Drift & Immutability — detecting a changed container in a declarative world
- [ ] Incident Response in Kubernetes — isolate, snapshot, evict, and preserve evidence

**Wave BC5 — Serverless & Managed Services**
- [ ] Serverless Threat Model — event injection, over-permissive roles, cold-start secrets
- [ ] Managed Service Trust Boundaries — what the provider secures, and precisely what you do
- [ ] IaC Security Scanning — catching the misconfiguration before it deploys
- [ ] Cloud Detection Engineering — CloudTrail/Activity Log/Audit Logs as detection sources
- [ ] Cloud Incident Response — snapshotting, credential revocation, blast-radius containment

### TRACK BD — API & Identity-First Security  (→ `sec` / `web`)

~4 waves, ~20 cards. The perimeter moved to the API and the token; the site's
coverage has not caught up.

**Wave BD1 — API Security**
- [ ] OWASP API Top 10 — what differs from the web Top 10, and why
- [ ] Broken Object-Level Authorization — the single most common real API bug
- [ ] Authentication vs Authorization at the API — where each belongs
- [ ] Rate Limiting & Abuse — quotas, burst, and distinguishing abuse from success
- [ ] API Inventory & Shadow APIs — you cannot protect the endpoint you forgot

**Wave BD2 — Tokens Done Right**
- [ ] JWT Security — algorithm confusion, `none`, key confusion, expiry, revocation
- [ ] OAuth 2.1 & PKCE — the flows that remain, and the ones that were removed
- [ ] Token Lifetime & Revocation — refresh, rotation, and the logout that does not
- [ ] Machine-to-Machine Auth — client credentials, mTLS, workload identity
- [ ] Secrets vs Tokens vs Keys — a taxonomy that prevents the wrong control

**Wave BD3 — Identity as the Control Plane**
- [ ] Identity-First Security — what changes when identity is the perimeter
- [ ] ITDR — detecting identity attacks: token theft, consent phishing, MFA fatigue
- [ ] Conditional Access Patterns — a policy set that is coherent rather than accreted
- [ ] Privileged Access Done Properly — tiering, PAWs, break-glass, JIT elevation
- [ ] Non-Human Identity — service principals, workload identities, and the sprawl nobody owns

**Wave BD4 — Federation & Third Parties**
- [ ] SAML & OIDC Attack Surface — golden SAML, signature confusion, reply-URL abuse
- [ ] SCIM & Provisioning Risk — the integration that quietly holds write access
- [ ] OAuth Consent Phishing — the attack that needs no password
- [ ] B2B & Guest Access — external identities without opening the tenant
- [ ] Third-Party App Governance — reviewing, restricting and revoking app permissions

### TRACK BE — Software Supply Chain & Integrity  (→ `eng` / `sec`)

~4 waves, ~20 cards. The SBOM cards exist; the discipline around them does not.

**Wave BE1 — Understanding the Chain**
- [ ] Where a Build Actually Comes From — every input, including the ones you forgot
- [ ] Historic Supply-Chain Attacks — what each one actually exploited
- [ ] Dependency Risk — transitive depth, typosquatting, abandoned packages
- [ ] Build System as a Target — the CI runner is production-adjacent
- [ ] Trust Decisions — pinning, vendoring, mirrors, and their maintenance cost

**Wave BE2 — Provenance & Attestation**
- [ ] SLSA Levels — what each one actually requires you to change
- [ ] Signing & Sigstore — keyless signing, transparency logs, verification
- [ ] Attestations & in-toto — statements about how an artifact was produced
- [ ] Verifying at Deploy Time — admission policy that refuses unsigned artifacts
- [ ] Reproducible Builds — the property, the practical obstacles

**Wave BE3 — Operating It**
- [ ] SBOM in Practice — generating, storing, and actually querying one
- [ ] VEX — saying "we ship it but are not affected", credibly
- [ ] Dependency Update Strategy — automated bumps without a broken main branch
- [ ] Vulnerability Triage for Dependencies — reachability, exploitability, real priority
- [ ] Responding to a Compromised Dependency — the first hour

**Wave BE4 — Internal Supply Chain**
- [ ] Securing the CI/CD Pipeline — secrets, runners, forks, and injection via pull request
- [ ] Artifact Repositories — promotion, retention, immutability, access
- [ ] Internal Package Registries — and the dependency-confusion class of attack
- [ ] Golden Images & Base Layer Hygiene — one place to patch, one place to break
- [ ] Developer Workstation Trust — the machine that signs your commits

### TRACK BF — Privacy Engineering  (→ `grc` / `eng`)

~4 waves, ~20 cards. Distinct from GRC: GRC proves compliance, privacy
engineering builds systems that do not need much proving.

**Wave BF1 — Privacy as a System Property**
- [ ] Privacy vs Security — overlapping, not the same, and where they conflict
- [ ] Data Minimisation — the control that removes whole classes of risk
- [ ] Purpose Limitation in a Data Warehouse — hard, and why it is usually skipped
- [ ] Data Inventory & Mapping — knowing where personal data actually flows
- [ ] Privacy by Design — the seven principles, translated into engineering decisions

**Wave BF2 — Technical Controls**
- [ ] De-identification — anonymisation vs pseudonymisation, and re-identification risk
- [ ] Differential Privacy, Practically — the intuition, the epsilon, the trade
- [ ] Tokenisation & Format-Preserving Encryption — protecting data that must stay usable
- [ ] Access Control for Personal Data — purpose-bound access and audit
- [ ] Retention & Deletion That Actually Deletes — backups, replicas, caches, logs

**Wave BF3 — User-Facing Obligations**
- [ ] DSARs — building a subject-access process that scales
- [ ] Right to Erasure — the engineering problem behind the legal right
- [ ] Consent & Preference Management — storing and honouring it across systems
- [ ] Cookies & Tracking — the technical reality behind the banner
- [ ] Cross-Border Transfers — the mechanisms, and their architectural consequences

**Wave BF4 — Privacy in New Systems**
- [ ] Privacy in Machine Learning — training data, memorisation, model inversion
- [ ] Telemetry Design — useful product analytics that collect less
- [ ] Third-Party Data Sharing — contracts, technical limits, and verification
- [ ] Privacy Incident Response — when it is a breach, and the clock that starts
- [ ] Privacy Review as a Process — lightweight enough that teams use it

---

## PART 2 — PLATFORM & RESILIENCE CRAFT

### TRACK BG — Platform Engineering & the Internal Developer Platform  (→ `eng` / `ops`)

~4 waves, ~20 cards. The discipline that grew out of DevOps once "you build it,
you run it" met a hundred teams.

**Wave BG1 — The Premise**
- [ ] Why Platform Engineering Exists — the cognitive-load argument, stated honestly
- [ ] Platform as a Product — users, roadmap, adoption, and the option to not use it
- [ ] Golden Paths — paved roads that are genuinely faster than going around
- [ ] Thinnest Viable Platform — resisting the urge to build a cloud on the cloud
- [ ] Platform Team Anti-Patterns — the gatekeeper, the ticket queue, the abstraction leak

**Wave BG2 — Building It**
- [ ] Developer Portals — service catalogue, ownership, scorecards
- [ ] Self-Service Infrastructure — templates, modules, and guard rails over gates
- [ ] Environment Management — ephemeral environments, seeding, cost control
- [ ] Paved-Path CI/CD — a pipeline teams inherit rather than copy
- [ ] Policy as Code in the Platform — compliance that happens by default

**Wave BG3 — Operating It**
- [ ] Platform SLOs — the platform is production for its users
- [ ] Versioning & Migrating Consumers — changing a platform without breaking teams
- [ ] Support Model — office hours, escalation, and not becoming a help desk
- [ ] Documentation as the Product Surface — where adoption is actually won or lost
- [ ] Measuring Platform Success — adoption, lead time, and the counter-metrics

**Wave BG4 — Developer Experience**
- [ ] Local Development That Matches Production — containers, seeds, fakes
- [ ] Build & Test Speed as a Feature — the compounding cost of a slow pipeline
- [ ] Inner vs Outer Loop — where a developer's day actually goes
- [ ] Onboarding to First Commit — measuring and shortening it
- [ ] Toil Audits — finding the manual work worth automating, and the work that is not

### TRACK BH — Observability Engineering  (→ `ops`)

~4 waves, ~20 cards. Beyond the monitoring cards: designing for questions you
have not thought of yet.

**Wave BH1 — Foundations**
- [ ] Monitoring vs Observability — the distinction that is not just marketing
- [ ] The Three Signals & Their Costs — metrics, logs, traces; what each is bad at
- [ ] Cardinality — the concept that decides your observability bill
- [ ] Structured Events — wide events as an alternative to three separate pipelines
- [ ] Instrumentation Strategy — what to instrument first in an unfamiliar system

**Wave BH2 — OpenTelemetry in Practice**
- [ ] OTel Architecture — API, SDK, collector, exporters
- [ ] Distributed Tracing Deep — spans, context propagation, sampling strategies
- [ ] Metrics With OTel — instruments, views, and avoiding cardinality explosions
- [ ] The Collector as a Control Point — filtering, redaction, routing, cost control
- [ ] Migrating an Existing Stack — incrementally, without a big-bang cutover

**Wave BH3 — Using It**
- [ ] Debugging With Traces — the workflow that finds an unknown-unknown
- [ ] Correlating Signals — trace to log to metric, and the IDs that make it possible
- [ ] Dashboards Worth Keeping — the small number that answer real questions
- [ ] Alerting on Symptoms, Not Causes — and the pager quality that follows
- [ ] Observability-Driven Development — shipping instrumentation with the feature

**Wave BH4 — SLOs as a Practice**
- [ ] Choosing SLIs — the signal that matches the user's experience
- [ ] Setting an SLO That Survives — negotiated, achievable, and meaningful
- [ ] Error Budgets & Policy — what actually happens when it is spent
- [ ] Reporting Reliability — to engineering, and separately to the business
- [ ] When SLOs Fail — the organisational reasons, not the technical ones

### TRACK BJ — Resilience & Chaos Engineering  (→ `ops` / `eng`)

*(Skipping "BI" — it reads as "B1".)*

~4 waves, ~20 cards.

**Wave BJ1 — Designing for Failure**
- [ ] Failure Modes & Effects Analysis for Systems — thinking it through before it happens
- [ ] Blast Radius Design — bulkheads, cells, shuffle sharding
- [ ] Graceful Degradation — the feature that turns off instead of the site going down
- [ ] Dependency Failure — timeouts, retries with jitter, circuit breakers revisited
- [ ] Capacity & Load Shedding — choosing what to drop before you are forced to

**Wave BJ2 — Chaos Engineering**
- [ ] The Method — steady-state hypothesis, blast radius, abort conditions
- [ ] Your First Experiment — safe, small, and in production eventually
- [ ] Fault Injection Techniques — latency, errors, resource exhaustion, dependency loss
- [ ] GameDays — running one that people volunteer for twice
- [ ] Chaos Maturity — from an annual exercise to continuous verification

**Wave BJ3 — Incidents as a System**
- [ ] Incident Command Deep — roles, handovers, and long incidents
- [ ] Communication During an Incident — internal, customer, and status page discipline
- [ ] Blameless Postmortems That Change Something — actions with owners and dates
- [ ] Learning From Near-Misses — the free lessons most organisations throw away
- [ ] Incident Metrics — what MTTR does and does not tell you

**Wave BJ4 — Human Factors**
- [ ] Resilience Engineering — the field, and why "human error" is a bad root cause
- [ ] Alert Fatigue — measuring it, and treating it as a reliability problem
- [ ] On-Call Health — load, compensation, and the sustainable rotation
- [ ] Runbook Quality — testing your runbooks the way you test code
- [ ] Organisational Memory — keeping what was learned after the people leave

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
element from "wins everything" to "loses to any rule with a class in it", and the page
has plenty:

```
elements carrying a c-* class:                    9166
…whose computed colour is NOT that class's value: 2196   (they render white —
                                                          .ref-table td wins)
```

Those 2196 are pre-existing: the six utility classes are *already* silently dead
wherever they land in a table cell. That is a real bug worth its own session, and it is
also the reason the substitution cannot be mechanical — every conversion needs to know
whether a table rule is going to eat it.

Two consequences, both recorded rather than acted on:

1. **`CONTRIBUTING.md`'s advice is wrong as written** for table content, which is most
   content. Either the utility classes need enough specificity to win
   (`.ref-table td.c-cyan`, or a `:where()` reset on the table rules), or the guidance
   needs a carve-out. Fix the CSS before touching the 1069.
2. **A counter can be honest and still not be a to-do list.** The hex counter came down
   because the fix was semantically neutral. This one is not, and the difference is
   worth more than the 1069 would have been.

## 3. New domains with no plan behind them

The `lifestyle` split created five domains and the Math work added one more. **None of them
has a wave spec'd**, and the plan's own Phase-4 rule says a domain needs ≥15 cards to
justify existing:

| Domain | Cards | Against the ≥15 rule |
|---|---|---|
| ~~`spirit`~~ | ~~3~~ | ✅ **Folded into `philosophy`** — session 18 |
| `quotes` | 5 | Under, but it is a reference domain like `acronym`, so the rule may not apply |
| `lifestyle` | 4 | Under, and one lower after the Windows card left. It is the residue after the split — check whether it still earns a chip |
| `philosophy` | 13 | Under; plausibly fine, it is a coherent subject, and now the home for the `spirit` cards |
| `productivity` | 10 | Under, but actively growing |
| `mind` | 11 | Under, but actively growing |
| `math` | 16 | Clears it |
| `career` · `devops` | 18 · 36 | Clear it comfortably |

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

CI grew two gates and lost a warning. The generators matter more than the fixes: a
regenerated cheat sheet is worth one session, but a cheat sheet that *cannot go stale*
is worth every session after it. Same for the drill index. That is the difference
between the work above and the fourteen sessions where the TREND line did not move.

**Three things surfaced that are worth carrying forward.** All are recorded above rather
than fixed:

- **The six `c-*` utility classes are dead in table cells** — 2196 elements on the page
  carry one and render a different colour, because `.ref-table td` outranks them. This is
  the highest-value thing found this session and nothing was done about it. §2 has the
  measurement and the two candidate fixes.
- `lifestyle` is now the weakest chip at 4 cards, and inherits the question `spirit` just
  answered.
- The lint fix is a worked example of the §4 `VOLATILE_HINTS` problem — a signal too
  broad to act on becomes actionable only once the check marks the claim. `VOLATILE_HINTS`
  still matches 182 of 943 topics and still needs exactly that treatment.

One correction to the audit above, found by doing it: §1 said to "re-run the generator"
for the cheat sheet. There was no generator to re-run. The file had been written by hand
and given a header that described an intention. Worth remembering when reading the rest
of this file — a stated capability is not evidence of one.
