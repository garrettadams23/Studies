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
- [ ] Add three filter chips to `index-shell.html` (`data-domain`, `.c-redteam`
  / `.c-blueteam` / `.c-cloud` classes).
- [ ] Add `.domain-redteam` / `.domain-blueteam` / `.domain-cloud` accent colors
  and `.chip.c-*` rules to `style.css` (mirror an existing domain's block).
- [ ] Create empty `data/redteam.html` / `data/blueteam.html` / `data/cloud.html`
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
- [ ] Burp Suite — Proxy, Repeater, Intruder, Scanner workflow
- [ ] OWASP ZAP — the open-source web proxy/scanner
- [ ] sqlmap — automated SQL injection (levels, risk, tamper scripts)
- [ ] ffuf & Gobuster — content/parameter/vhost fuzzing
- [ ] Nuclei — templated vulnerability scanning (dual-use with Blue)
- [ ] Nikto & wpscan — web server & WordPress scanning

**Wave R3 — Exploitation frameworks**
- [ ] Metasploit Framework — modules, sessions, msfconsole workflow
- [ ] msfvenom — payload generation & encoders (concepts + formats)
- [ ] Searchsploit / Exploit-DB — finding & vetting public exploits
- [ ] Impacket — the Python toolkit (psexec, secretsdump, wmiexec, ntlmrelayx)
- [ ] Nuclei/CrackMapExec as exploitation orchestrators

**Wave R4 — Active Directory attack tooling**
- [ ] BloodHound / SharpHound — AD attack-path graphing
- [ ] Mimikatz — credential extraction (what it does; Blue detections)
- [ ] Rubeus & Kerbrute — Kerberos abuse (roasting, AS-REP, TGT)
- [ ] Responder & ntlmrelayx — LLMNR/NBT-NS poisoning & relay
- [ ] NetExec (CrackMapExec) — the AD swiss-army knife
- [ ] PowerView / PowerSploit — AD enumeration from PowerShell
- [ ] Certify / Certipy — AD CS (ADCS) abuse (ESC1–ESC8 overview)

**Wave R5 — Command & Control (C2)**
- [ ] C2 Concepts — beacons, listeners, redirectors, malleable profiles
- [ ] Cobalt Strike — the commercial standard (what defenders look for)
- [ ] Sliver — the open-source modern C2
- [ ] Mythic & Havoc — agent/collaboration frameworks
- [ ] Empire / Starkiller — PowerShell/Python post-ex C2

**Wave R6 — Password & hash attacks**
- [ ] Hashcat — modes, masks, rules, GPU cracking workflow
- [ ] John the Ripper — formats, wordlist/incremental, jumbo
- [ ] Hydra & Medusa — online/network login brute-forcing
- [ ] Wordlists & CeWL/Crunch — rockyou, custom lists, mangling
- [ ] Hash identification & extraction (hashid, /etc/shadow, NTDS)

**Wave R7 — Wireless & hardware**
- [ ] Aircrack-ng suite — capture, deauth, WPA handshake cracking
- [ ] Wifite & hcxdumptool — automated Wi-Fi + PMKID attacks
- [ ] Bettercap — MITM framework (Wi-Fi, BLE, HID, ARP)
- [ ] Kismet — wireless detection & sniffing
- [ ] Flipper Zero — Sub-GHz/RFID/NFC/IR/BadUSB multi-tool
- [ ] Rubber Ducky / O.MG cable — HID injection (BadUSB)
- [ ] Proxmark3 & HackRF — RFID cloning & software-defined radio

**Wave R8 — Post-exploitation, evasion & LOLBins**
- [ ] Living off the Land — LOLBAS / GTFOBins (built-ins as weapons)
- [ ] Privilege escalation scanners — linPEAS / winPEAS / PowerUp
- [ ] AMSI & AV/EDR evasion — concepts, obfuscation, why it works (defensive lens)
- [ ] Pivoting & tunneling — Chisel, ligolo-ng, SSH/socks, proxychains
- [ ] Data exfil channels — DNS/ICMP/HTTPS tunneling (detection notes)

**Wave R9 — Cloud & container offense**
- [ ] Pacu — the AWS exploitation framework
- [ ] CloudFox & enumerate-iam — cloud attack-surface enumeration
- [ ] Kubernetes attacks — kube-hunter, RBAC abuse, container escape
- [ ] Cloud credential attacks — SSRF→IMDS, key theft, role chaining
- [ ] Purple-team bridge — mapping the above to ATT&CK & detections

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
- [ ] Splunk — SPL query language, indexes, dashboards, alerts
- [ ] Elastic / ELK Stack — Elasticsearch, Logstash, Kibana, Beats
- [ ] Wazuh — open-source XDR/SIEM (agents, rules, decoders)
- [ ] Graylog & Loki — log aggregation alternatives
- [ ] Sigma — vendor-neutral detection rules (write once, convert anywhere)

**Wave B3 — Endpoint visibility & EDR**
- [ ] Sysmon — the Windows telemetry powerhouse (config, event IDs)
- [ ] OSQuery — your endpoints as a SQL-queryable fleet
- [ ] Velociraptor — endpoint DFIR & hunting at scale
- [ ] Windows Event Logs — the IDs that matter (4624/4625/4688/4768…)
- [ ] auditd & Linux endpoint logging

**Wave B4 — Detection engineering**
- [ ] YARA — pattern-matching rules for malware/files
- [ ] Sigma-to-SIEM — detection-as-code workflow
- [ ] MITRE ATT&CK mapping & Navigator — coverage-driven detection
- [ ] Atomic Red Team & Caldera — adversary emulation to test detections
- [ ] Detection tuning — reducing false positives, alert fatigue

**Wave B5 — Digital forensics & IR (DFIR)**
- [ ] Volatility — memory forensics (processes, injection, artifacts)
- [ ] Autopsy / The Sleuth Kit — disk forensics
- [ ] KAPE & plaso/log2timeline — triage collection & super-timelines
- [ ] Chain of custody & evidence handling (procedure card)
- [ ] Windows forensic artifacts — Prefetch, ShimCache, AmCache, MFT, registry

**Wave B6 — Threat intelligence & sharing**
- [ ] MISP — threat-intel sharing platform (IOCs, feeds, taxonomies)
- [ ] OpenCTI — structured CTI knowledge base
- [ ] STIX / TAXII — the standards for exchanging threat intel
- [ ] VirusTotal / Hybrid Analysis / Any.Run — sample analysis & sandboxing
- [ ] Pyramid of Pain & IOC vs TTP-based detection

**Wave B7 — Vuln management, hardening & benchmarks**
- [ ] Nessus & OpenVAS/Greenbone — vulnerability scanners
- [ ] CIS Benchmarks & CIS-CAT — hardening baselines
- [ ] Lynis — Linux/Unix audit & hardening
- [ ] OpenSCAP & DISA STIGs — compliance-driven hardening
- [ ] Patch & config management (WSUS/Ansible) as a control

**Wave B8 — Deception & email/identity defense**
- [ ] Honeypots & Canarytokens — deception tech (T-Pot, canaries)
- [ ] Email security stack — SPF/DKIM/DMARC enforcement, sandboxing, banners
- [ ] Identity threat detection — impossible travel, ITDR, conditional access
- [ ] Purple teaming — running the exercise & closing detection gaps

---

## TRACK C — Cloud Platforms: AWS & GCP How-To  (→ `cloud`)

~9 waves, ~50 cards. Parallel AWS/GCP structure so learners can cross-map, with
an explicit "Rosetta stone" card. Azure kept as a lighter bonus set.

**Wave C1 — Cloud foundations & getting started**
- [ ] Cloud Fundamentals — IaaS/PaaS/SaaS, regions/AZs, shared-responsibility
- [ ] AWS — Getting Started (account, root vs IAM, console vs CLI, free tier)
- [ ] AWS CLI & CloudShell — install, configure, profiles, `--query` JMESPath
- [ ] GCP — Getting Started (org/folder/project hierarchy, billing)
- [ ] gcloud CLI & Cloud Shell — init, config, `gcloud`/`gsutil`/`bq`
- [ ] Cloud Service Rosetta Stone — AWS ↔ GCP ↔ Azure equivalents table

**Wave C2 — Identity & access (the #1 cloud risk)**
- [ ] AWS IAM — users, groups, roles, policies (identity vs resource vs SCP)
- [ ] AWS IAM Deep — assume-role, STS, permission boundaries, least privilege
- [ ] GCP IAM — members, roles (basic/predefined/custom), resource hierarchy
- [ ] GCP Service Accounts & Workload Identity — machine auth done right
- [ ] Cloud IAM pitfalls — wildcard policies, privilege escalation paths

**Wave C3 — Networking**
- [ ] AWS VPC — subnets, route tables, IGW/NAT, security groups vs NACLs
- [ ] AWS Load Balancing & DNS — ALB/NLB, Route 53, CloudFront
- [ ] GCP VPC — global VPC, subnets, firewall rules, Cloud NAT
- [ ] GCP Load Balancing & DNS — global LB, Cloud DNS, Cloud CDN
- [ ] Hybrid connectivity — VPN, Direct Connect / Cloud Interconnect, peering

**Wave C4 — Compute**
- [ ] AWS Compute — EC2, AMIs, instance types, Auto Scaling, spot
- [ ] AWS Serverless & Containers — Lambda, ECS, EKS, Fargate
- [ ] GCP Compute — Compute Engine, machine families, MIGs, preemptible
- [ ] GCP Serverless & Containers — Cloud Run, Cloud Functions, GKE
- [ ] Choosing compute — VM vs container vs serverless decision guide

**Wave C5 — Storage & databases**
- [ ] AWS Storage — S3 (deep), EBS, EFS, storage classes & lifecycle
- [ ] AWS Databases — RDS, Aurora, DynamoDB, ElastiCache
- [ ] GCP Storage — Cloud Storage, Persistent Disk, Filestore
- [ ] GCP Databases — Cloud SQL, Spanner, Firestore, Bigtable
- [ ] BigQuery — serverless analytics warehouse (SQL, slots, cost)

**Wave C6 — Cloud security services**
- [ ] AWS Security Stack — CloudTrail, Config, GuardDuty, Security Hub, Inspector
- [ ] AWS Data Protection — KMS, Secrets Manager, encryption at rest/in transit
- [ ] GCP Security Stack — Cloud Logging/Audit, Security Command Center
- [ ] GCP Data Protection — Cloud KMS, Secret Manager, VPC Service Controls
- [ ] CSPM & cloud posture — ScoutSuite, Prowler, Steampipe (Blue-team bridge)

**Wave C7 — Infrastructure as Code & DevOps on cloud**
- [ ] Terraform on AWS/GCP — providers, remote state, modules (ties to ops topic)
- [ ] AWS-native IaC — CloudFormation & CDK
- [ ] GCP-native IaC — Deployment Manager & Config Controller
- [ ] Cloud CI/CD — CodePipeline / Cloud Build, artifact registries
- [ ] Cloud cost control — budgets, tagging, Cost Explorer / billing export (→ FinOps)

**Wave C8 — Observability & operations on cloud**
- [ ] AWS Observability — CloudWatch (metrics/logs/alarms), X-Ray
- [ ] GCP Observability — Cloud Monitoring, Cloud Logging, Cloud Trace
- [ ] Well-Architected / Architecture Framework — the 5–6 pillars
- [ ] Landing zones & multi-account/project — Organizations, Control Tower

**Wave C9 — Azure bonus (lighter set)**
- [ ] Azure — Getting Started, Entra ID (formerly Azure AD)
- [ ] Azure Core — Resource Groups, VNet, VMs, Storage Accounts
- [ ] Azure Security — Defender for Cloud, Key Vault, Sentinel (SIEM)

---

## TRACK X — Round out existing domains ("the more the better")

Lower priority than R/B/C but each fills a real gap; interleave as desired.

**Languages (`script`)**
- [ ] Rust · Java · C# / .NET · Ruby · PHP · C — one card each (mirror the Go/Python style)
- [ ] Assembly & how programs run — registers, stack, calling conventions (pairs w/ RE)
- [ ] Semantic Versioning & dependency management (npm/pip/cargo lockfiles)

**Networking (`net`)**
- [ ] Network Automation — Ansible, Netmiko, NAPALM, gNMI
- [ ] SD-WAN & MPLS · Multicast · PoE · 802.1Q trunking deep-dive
- [ ] DNSSEC, DoH/DoT — securing name resolution

**Linux (`linux`)**
- [ ] Podman & rootless containers · systemd deep-dive · sysctl/kernel tuning
- [ ] ZFS & Btrfs — snapshots, subvolumes, integrity
- [ ] Advanced Bash — traps, parameter expansion, coprocesses

**AI & ML (`ai`)**
- [ ] Fine-tuning vs RAG vs prompting — when to use which
- [ ] LoRA / PEFT · Quantization (GGUF, bitsandbytes) · Tokenization internals
- [ ] Running local LLMs — Ollama, llama.cpp, LM Studio
- [ ] LLM evaluation & guardrails · Diffusion models (how image gen works)

**Data (`script`/`ai`)**
- [ ] Apache Kafka (deep) · Spark · Airflow/Dagster · dbt
- [ ] Dimensional modeling — star/snowflake schemas, slowly-changing dimensions

**Productivity (`shortcut`)**
- [ ] VS Code · Vim (deep) · modern CLI tools (ripgrep, fzf, bat, jq, eza)
- [ ] Git power-user — rebase, reflog, bisect, worktrees, aliases

**Study meta (any domain / a new `certs` section)**
- [ ] Cert Roadmaps — CompTIA (A+→Net+→Sec+→CySA+→PenTest+→CASP), OSCP path,
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
- [ ] Scalability 101 — vertical vs horizontal, stateless design, shared-nothing
- [ ] Load Balancing & Sharding — strategies, consistent hashing, hot keys
- [ ] Back-of-the-Envelope — latency numbers every engineer should know, capacity math
- [ ] Designing for Failure — redundancy, graceful degradation, bulkheads, blast radius
- [ ] The System Design Interview — a framework (requirements → estimate → API → data → scale → trade-offs)

**Wave E2 — Architecture Styles**
- [ ] Monolith vs Microservices vs Modular Monolith — honest trade-offs
- [ ] Event-Driven Architecture — deep (choreography vs orchestration; ties to Message Queues)
- [ ] Clean / Hexagonal / Ports & Adapters — keeping business logic independent
- [ ] CQRS & Event Sourcing — read/write split, the append-only log
- [ ] The Twelve-Factor App — the checklist for cloud-native services
- [ ] Cloud-Native & Serverless architecture patterns

**Wave E3 — Domain Modeling & Design**
- [ ] Domain-Driven Design (DDD) — bounded contexts, ubiquitous language, aggregates
- [ ] SOLID Principles — deep card with examples of each
- [ ] Coupling & Cohesion — Law of Demeter, dependency direction
- [ ] API-First & Contract-Driven design — OpenAPI, consumer-driven contracts
- [ ] Schema & data modeling patterns — normalization trade-offs, polyglot persistence

**Wave E4 — Engineering Craft & Quality**
- [ ] Clean Code & Naming — deep (functions, comments, structure)
- [ ] Code Review — doing it well (giving + receiving; what to look for)
- [ ] Testing Strategy — the test pyramid, unit/integration/e2e, TDD & BDD
- [ ] Technical Debt — recognizing, quantifying, and paying it down deliberately
- [ ] ADRs & Design Docs — Architecture Decision Records, RFCs, the C4 model

**Wave E5 — Reliability & Distributed Patterns**
- [ ] Resilience Patterns — circuit breaker, retry + backoff + jitter, timeout, bulkhead
- [ ] Idempotency & Exactly-Once — deep (ties to API Design + Message Queues)
- [ ] Distributed Transactions — Saga, Outbox, 2PC and why 2PC is avoided
- [ ] Backpressure & Flow Control — protecting systems under load
- [ ] Consistency in practice — read-repair, quorums, tunable consistency (ties to CAP)

**Wave E6 — Engineering Career & Roles**
- [ ] The Engineering Ladder — junior → mid → senior → staff → principal
- [ ] Staff+ Archetypes — tech lead, architect, solver, right-hand
- [ ] Tech Lead vs Engineering Manager — the fork in the road
- [ ] Estimation & Planning — story points, velocity, why estimates are hard
- [ ] Influence Without Authority — RFCs, stakeholder comms, driving alignment
- [ ] Career Ladders & Interviews — leveling, system-design & coding interview prep

---

## TRACK F — DevOps & Platform Engineering  (→ deepen `ops`)

5 waves, ~25 cards. Deepens the tools already present as concept-topics.

**Wave F1 — DevOps Foundations & Culture**
- [ ] What DevOps Actually Is — CALMS, breaking the dev/ops wall, you-build-it-you-run-it
- [ ] The Three Ways — Flow, Feedback, Continual Learning (The Phoenix/DevOps Handbook)
- [ ] DORA Metrics — deploy frequency, lead time, MTTR, change-failure rate
- [ ] Value Stream Mapping — finding the bottleneck in delivery
- [ ] Platform Engineering & the IDP — golden paths, self-service, the internal developer platform

**Wave F2 — CI/CD Pipelines Deep**
- [ ] Pipeline Design — stages, quality gates, artifacts, promotion between envs
- [ ] GitHub Actions — workflows, jobs, matrix builds, secrets, reusable/composite actions
- [ ] Jenkins · GitLab CI · CircleCI — comparison & when to pick which
- [ ] Branching Strategies — trunk-based vs GitHub Flow vs GitFlow (and why trunk wins at scale)
- [ ] Progressive Delivery — feature flags + canary + blue-green wired into the pipeline

**Wave F3 — Containers & Kubernetes Deep**
- [ ] Docker Deep — multi-stage builds, layer caching, image slimming, distroless
- [ ] Kubernetes Objects — pods, deployments, services, ingress, configmaps/secrets
- [ ] Helm & Kustomize — packaging and templating manifests
- [ ] K8s Networking & Storage — CNI, CSI, ingress controllers, persistent volumes
- [ ] K8s Security — RBAC, network policies, pod security standards, admission control

**Wave F4 — Config, Secrets & Supply Chain**
- [ ] Configuration Management — Ansible deep (playbooks, roles, inventory), Chef/Puppet/Salt
- [ ] Secrets Management — HashiCorp Vault, external-secrets, sealed secrets, dynamic creds
- [ ] Software Supply Chain Security — SBOM, SLSA, Sigstore/cosign, provenance & signing
- [ ] Policy as Code — OPA/Rego, Kyverno, Conftest guardrails in CI
- [ ] Artifact & Registry Management — container/package registries, retention, promotion

**Wave F5 — Observability & Operations Deep**
- [ ] Prometheus & Grafana — metrics model, PromQL, dashboards, Alertmanager
- [ ] Golden Signals + RED / USE — what to actually measure
- [ ] SLIs, SLOs & Error Budgets — deep (turning SRE theory into alert thresholds)
- [ ] Structured Logging & Log Pipelines — correlation IDs, aggregation (ties to SIEM)
- [ ] On-Call Done Humanely — rotations, escalation, runbooks, blameless postmortems

---

## TRACK G — Developer Environment & VS Code  (→ deepen `shortcut`)

3 waves, ~16 cards. Replaces the single shallow `VS Code` card.

**Wave G1 — VS Code Mastery**
- [ ] VS Code Setup & Settings — settings.json, Settings Sync, Profiles per stack
- [ ] Command Palette & Keybindings — the shortcuts that actually save time
- [ ] Editing Superpowers — multi-cursor, column select, refactor, snippets, regex find/replace
- [ ] Debugging — launch.json, breakpoints (conditional/logpoints), watch, call stack
- [ ] Integrated Terminal, Tasks & the Source Control panel
- [ ] Essential Extensions — per-language + productivity (and how to stay lean)

**Wave G2 — Remote & Containerized Dev**
- [ ] Remote Development — Remote-SSH, WSL, and how the client/server split works
- [ ] Dev Containers — devcontainer.json, reproducible per-project toolchains
- [ ] GitHub Codespaces & cloud dev environments
- [ ] Live Share — real-time collaborative editing & debugging

**Wave G3 — The Modern Dev Environment**
- [ ] Dotfiles & Config Management — chezmoi/stow, version-controlled setup
- [ ] Shell & Terminal Setup — zsh/fish, starship prompt, tmux (ties to existing tmux card)
- [ ] Runtime & Version Managers — asdf/mise, nvm, pyenv, direnv per-project
- [ ] AI Pair Programming — Copilot, Cursor, Claude Code — using them well without over-trusting

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
