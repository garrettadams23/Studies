# CompTIA & Tech Reference — 2026 Edition

A comprehensive, interactive web-based reference for IT professionals, students,
and enthusiasts. Organized by concept domain with a dark/light theme engine,
collapsible accordions, syntax-highlighted code blocks, and reference tables.

## Live Demo

Open `index.html` in any modern web browser — no server or build step required.

## Features

- **One Domain at a Time** — Every domain is listed; the one you open is the
  only one the browser builds. Opening another releases the last, so the page
  costs 404 elements at rest instead of 92,330 and loads in a third of the time.
  Nothing is fetched — the content is all in the page, held as inert text until
  it is asked for, so this works offline and over `file://` exactly as before.
- **Interactive Filtering** — Sticky chip nav bar filters by domain instantly,
  and opens the domain it narrows to.
- **Full-text Search** — Debounced search reads every domain, not just the open
  one: it highlights hits in the domain on screen and shows the other domains'
  match counts on their headers, one click away and already filtered.
- **Theme Engine** — Dark / Light mode with `localStorage` persistence.
- **Collapsible Accordions** — Domain and topic-level expand / collapse, fully
  keyboard-operable (`Tab` to a header, `Enter` / `Space` to toggle).
- **Expand All / Collapse All** — Header button for bulk toggle.
- **Per-topic Permalinks** — Copy a `#slug` link to any topic; opening such a
  URL expands and scrolls straight to it.
- **Study Progress** — Mark topics as reviewed (saved in `localStorage`); each
  domain header shows a live `n/m` counter.
- **Notepad** — Slide-out scratchpad backed by `localStorage`, synced live
  across your open tabs. No dependencies.
- **Acronym Expansions Everywhere** — The first use of an acronym in any topic
  carries what it stands for right beside it, e.g. `ACL (Access Control List)`.
- **Acronym Dictionary** — A dedicated domain with 980+ IT acronyms, browsable
  A–Z or by subject area, searchable by acronym *or* by what it expands to.
- **Rotating Snap Quotes** — Philosophical quotes on a fade cycle.
- **URL Encode / Decode Widget** — Interactive tool in the Scripting domain.
- **Cloud Responsibility Matrix** — Visual IaaS / PaaS / SaaS / On-Prem breakdown.
- **Offline-first** — Self-hosted fonts and zero third-party requests; works
  fully over `file://`. Respects `prefers-reduced-motion` and prints cleanly.

## Domains

| Domain | Certs | Key Topics |
|---|---|---|
| 🌐 Networking | A+, Net+ | OSI, TCP/IP, Subnetting, Routing, VLANs, Wireless, DNS, Cabling, NMAP, TCPDump |
| 🔐 Security Core | Sec+, SecX | CIA Triad, AAA, PKI, Crypto, Cloud, Zero Trust, Kerberos, Password Attacks |
| ⚔️ Threat & Attack | Sec+, CySA+, PT+ | Kill Chain, MITRE ATT&CK, Diamond Model, Social Engineering, Malware, DoS |
| ⚖️ Governance & Risk | Sec+, SecX | NIST CSF 2.0, Risk Matrix, Defense-in-Depth, Legal Frameworks, CISSP 8 Domains |
| 🔬 Sec Operations | CySA+, SecX | IR PICERL, Vuln Mgmt, Troubleshooting, BCP/DR, Digital Forensics, Splunk SPL |
| 🎯 PenTest | PT+ | 5-Phase Methodology, OWASP Top 10, SQLmap |
| 🐧 Linux & Systems | Linux+, A+ | FHS, Permissions, Boot Process, SSH, Tmux, Unix Commands, RAID, A+ Hardware |
| 🤖 AI & ML | AI+ | ML Pipeline, Learning Paradigms, Agentic AI (MCP, Skills, Sub-agents), Ethics |
| 💻 Scripting & Web | Linux+, SecX | Regex, PowerShell, Bash, ZSH, Go, HTML, CSS, JS ES2022–ES2025, JSON, SQL, URL Encoding |
| ⌨️ Shortcuts | General | Windows, Linux Terminal, Excel, Word, Spotify, Google Chrome, DoD |
| 🧘 Lifestyle & Philosophy | Life | Stoicism, Buddhism, Taoism, Existentialism, Minimalism, Wicca, Paganism, Druidism |
| 🎖️ Military Codes | MIL | NATO Phonetic, Military Time, US Army Ranks, CMMC, DISA STIGs, Staff Codes J/G/S/N/A/C |
| 🔴 Red Team | PT+, OSCP | Recon, Exploitation, AD Attacks, C2, Password & Wireless |
| 🔵 Blue Team | CySA+, GCIH | NSM, SIEM, EDR, Detection, DFIR, Threat Intel |
| ☁️ Cloud | AWS, GCP | AWS, GCP, **Azure** (hierarchy, networking, compute/storage, Monitor & KQL, **troubleshooting playbook**, Entra ID sign-in), IAM, IaC, Cost |
| 🏛️ Engineering | ARCH, SWE | System Design, Architecture, Craft, Reliability, Career, IT Job Titles |
| 📊 Data | SQL, DATA | SQL, DB Internals, NoSQL, Warehousing, DBA |
| 🌐 Web | WEB, JS | Browser, CSS, JS, Frameworks, Performance, A11y |
| 📧 Microsoft 365 | M365, MS-102 | Tenant anatomy, licensing, admin roles, **Exchange Online** (mail flow, connectors, EOP/Defender, message trace), **SharePoint & OneDrive** (architecture, sharing sprawl, KFM), **Teams** (what a team is, governance), **Purview** (retention, labels, DLP, eDiscovery), backup, troubleshooting playbook |
| 🖥️ Endpoint | MD-102, MEM | **MECM** (client health, deployment & content, OSD/task sequences, site & server logs, CMPivot), Intune, Autopilot, ESP, Co-management |
| 🔤 Acronym Dictionary | REF | 980+ IT acronyms A–Z, plus per-subject indexes (Networking, Security, Cloud, Crypto, Data, AI, …) |

## Project Structure

```
index.html            Built output — open this in a browser (generated; do not hand-edit)
index-shell.html      Page skeleton (head, header, filter/search bar, notepad) — edit this
build.py              Assembles index-shell.html + data/* → index.html. Stamps each
                      topic's permalink id, parks each domain's content in an inert
                      <script type="text/html"> block, and minifies the output
reconcile_build.py    Recovery tool: syncs a hand-patched index.html back into data/*
script.js             All interactive logic (deferred domain content, accordion, filter,
                      search, theme, URL codec, notepad, permalinks, progress,
                      back-to-top)
style.css             Layout, themes, and component styles
data/
  domains.json        Domain metadata (id, icon, title, cert tags, subtitle)
  acronyms.json       Every acronym and what it stands for — the single source
                      of truth for both the dictionary and the inline expansions
  acronym.html        Generated from acronyms.json; do not hand-edit
  net.html … military.html   One file per domain — the .domain-body inner content
Img/
  diagrams/           Standalone copies of the two SVG diagrams (role scope,
                      acronym anatomy) — self-contained, light/dark aware
  favicon/            favicon.ico, site.webmanifest, PNG variants
  fonts/              Self-hosted Share Tech Mono + Outfit woff2
  fonts.css           @font-face rules pointing at Img/fonts/
  Studying-Tips.png   Header infographic (optimized)
tools/
  gen_acronym_domain.py   data/acronyms.json → data/acronym.html
  annotate_acronyms.py    Adds/refreshes the inline `(expansion)` spans in data/*.html
patches/              Historical one-time content-injection scripts (already applied)
CONTRIBUTING.md       Canonical topic markup conventions for new content
plan.md               Improvement plan / review log
.github/workflows/    CI: rebuilds index.html and fails if it is stale
```

## Editing Content

All topic content lives in `data/*.html` — one file per domain. To add or update a topic:

1. Edit the relevant `data/{domain}.html` file (see **CONTRIBUTING.md** for the
   canonical topic skeleton and class conventions).
2. Run `python3 build.py` from the project root.
3. Open `index.html` in a browser to verify.

One rule follows from the single-domain rendering, and it is a code rule rather
than a content one: nothing may answer a page-wide question by walking the DOM,
because only one domain is in it. Use `topicIndex()` for which topics exist and
`domainTopics(id)` for what they say — see **CONTRIBUTING.md**.

To add a new domain, add an entry to `data/domains.json` and create the matching
`data/{id}.html`. **Never hand-edit `index.html`** — it is generated; if it ever
drifts from `data/*`, `reconcile_build.py` can rebuild the sources from it.

### Acronyms

Acronym expansions live in one place: **`data/acronyms.json`**. After editing it,
or after adding content that uses acronyms, run:

```sh
python3 tools/gen_acronym_domain.py   # rebuilds the Acronym Dictionary domain
python3 tools/annotate_acronyms.py    # refreshes the inline (expansion) spans
python3 build.py
```

Both tools are idempotent — `annotate_acronyms.py` strips the spans it added
before re-adding them, so it is safe to re-run at any time, and
`--check` makes it report drift without writing. CI runs all three.

Each JSON entry looks like:

```json
{"a": "ACL", "m": [{"e": "Access Control List", "c": "Security"}]}
```

`a` is the acronym, `m` its meanings (`e` = expansion, `c` = subject area,
`n` = optional note). For terms that mean different things in different places,
`annotate` picks the default inline expansion, `byDomain` overrides it per domain
file (`null` = leave that domain alone), and `noAnnotate` keeps a term in the
dictionary while never expanding it inline — used for acronyms that collide with
ordinary words, like `IT` or `MAN`.

## Built With

- **HTML5** — Semantic structure, no external frameworks.
- **Vanilla CSS** — CSS custom properties, Flexbox, Grid.
- **Vanilla JavaScript** — Event delegation, accordion, filtering, search, theme,
  URL codec, notepad. No runtime dependencies.
- **Self-hosted fonts** — Share Tech Mono & Outfit (no third-party requests).

## License

MIT License — see [LICENSE](LICENSE) for details.
