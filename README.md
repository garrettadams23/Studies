# CompTIA & Tech Reference — 2026 Edition

A comprehensive, interactive web-based reference for IT professionals, students,
and enthusiasts. Organized by concept domain with a dark/light theme engine,
collapsible accordions, syntax-highlighted code blocks, and reference tables.

## Live Demo

Open `index.html` in any modern web browser — no server or build step required.

## Features

- **Interactive Filtering** — Sticky chip nav bar filters by domain instantly.
- **Theme Engine** — Dark / Light mode with `localStorage` persistence.
- **Collapsible Accordions** — Domain and topic-level expand / collapse.
- **Expand All / Collapse All** — Header `↕` button for bulk toggle.
- **Rotating Snap Quotes** — 18 philosophical quotes, 8 s fade cycle.
- **URL Encode / Decode Widget** — Interactive tool in the Scripting domain.
- **Cloud Responsibility Matrix** — Visual IaaS / PaaS / SaaS / On-Prem breakdown.

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

## Project Structure

```
index.html            Built output — open this in a browser
index-shell.html      Page skeleton (header, filter bar, container) — edit this
build.py              Assembles index-shell.html + data/* → index.html
script.js             All interactive logic (accordion, filter, theme, URL codec)
style.css             Layout, themes, and component styles
data/
  domains.json        Domain metadata (id, icon, title, cert tags, subtitle)
  net.html            Networking topic content
  sec.html            Security Core topic content
  threat.html         Threat & Attack topic content
  grc.html            Governance & Risk topic content
  ops.html            Security Operations topic content
  pentest.html        Penetration Testing topic content
  linux.html          Linux & Systems topic content
  ai.html             AI & ML topic content
  script.html         Scripting & Web topic content
  shortcut.html       Shortcuts & Productivity topic content
  lifestyle.html      Lifestyle & Philosophy topic content
  military.html       Military Staff Codes topic content
Img/
  favicon/            favicon.ico, favicon.svg, site.webmanifest, PNG variants
  Studying-Tips.png   Header infographic
tools/
  patch_chrome_shortcuts.py   One-time injection script (already applied)
plan.md               Structural fix plan and task tracking
```

## Editing Content

All topic content lives in `data/*.html` — one file per domain. To add or update a topic:

1. Edit the relevant `data/{domain}.html` file.
2. Run `python3 build.py` from the project root.
3. Open `index.html` in a browser to verify.

To add a new domain, add an entry to `data/domains.json` and create the matching `data/{id}.html`.

## Built With

- **HTML5** — Semantic structure, no external frameworks.
- **Vanilla CSS** — CSS custom properties, Flexbox, Grid.
- **Vanilla JavaScript** — Event delegation, accordion, filtering, theme, URL codec.
- **Google Fonts** — Share Tech Mono & Outfit.

## License

MIT License — see [LICENSE](LICENSE) for details.
