# 🧠 CompTIA & Tech Reference — 2026 Edition

A comprehensive, interactive web-based reference for IT professionals, students,
and enthusiasts. Organized by concept domain with a dark/light theme engine,
collapsible accordions, syntax-highlighted code blocks, and reference tables.

## 🚀 Live Demo
Open `index.html` in any modern web browser — no build step required.

## 🌟 Key Features
- **Interactive Filtering** — Toggle between domains via sticky chip nav bar.
- **Theme Engine** — Dark / Light mode with `localStorage` persistence.
- **Collapsible Accordions** — Domain and topic-level expand / collapse.
- **Expand All / Collapse All** — Header `↕` button for bulk toggle.
- **Rotating Snap Quotes** — 18 philosophical quotes, 8 s fade cycle.
- **URL Encode / Decode Widget** — Interactive tool in the Scripting domain.
- **CVSS v3.1 Calculator** — Interactive scoring in Threat Frameworks.

## 📚 Domains Covered

| Domain | Certs / Tags | Key Topics |
|---|---|---|
| 🌐 Networking | A+, Net+ | OSI, TCP/IP, Subnetting, Routing, VLANs, Wireless, DNS, Cabling, NMAP, TCPDump |
| 🔐 Security Core | Sec+, SecX | CIA Triad, AAA, PKI, Crypto, Cloud, Zero Trust, Kerberos, Password Attacks |
| ⚔️ Threat & Attack | Sec+, CySA+, PT+ | Kill Chain, MITRE ATT&CK, Diamond Model, Social Engineering, Malware, DoS |
| ⚖️ Governance & Risk | Sec+, SecX | NIST CSF 2.0, Risk Matrix, Defense-in-Depth, Legal Frameworks, CISSP 8 Domains |
| 🔬 Sec Operations | CySA+, SecX | IR PICERL, Vuln Mgmt, Troubleshooting, BCP/DR, Digital Forensics, Splunk SPL |
| 🎯 PenTest | PT+ | 5-Phase Methodology, OWASP Top 10, SQLmap |
| 🐧 Linux & Systems | Linux+, A+ | FHS, Permissions, Boot Process, SSH, Tmux, Unix Commands, RAID, A+ Hardware |
| 🤖 AI & ML | AI+ | ML Pipeline, Learning Paradigms, Agentic AI (MCP, Skills, Sub-agents), Ethics |
| 💻 Scripting & Web | Linux+, SecX | Regex, PowerShell, Bash, ZSH, Go, Python, HTML, CSS, JS ES2022–ES2025, JSON/jq, SQL, URL Encoding |
| ⌨️ Shortcuts | General | Windows, Linux Terminal, Excel, Word, Spotify, **Google Chrome**, DoD / Military |
| 🧘 Lifestyle & Philosophy | Life | Stoicism, Machiavellianism, Psychology, Buddhism, Taoism, Existentialism, Minimalism, Wicca, Paganism, Druidism |
| 🎖️ Military Codes | MIL | NATO Phonetic, Military Time, US Army Ranks, CMMC, DISA STIGs, Staff Codes J/G/S/N/A/C |

## ⌨️ Google Chrome Shortcuts (added this release)

Full reference sourced from [Google Chrome Help](https://support.google.com/chrome/answer/157179)
covering **Windows / Linux** and **Mac**:

| Category | Examples |
|---|---|
| Tabs & Windows | New tab `Ctrl+T`, Reopen closed `Ctrl+Shift+T`, Close `Ctrl+W` |
| Chrome Features | DevTools `F12`, Bookmarks `Ctrl+Shift+B`, History `Ctrl+H` |
| Address Bar | Focus `Ctrl+L`, Open in new tab `Alt+Enter`, .com shortcut `Ctrl+Enter` |
| Webpage Nav | Hard reload `Ctrl+Shift+R`, Zoom `Ctrl+±`, View source `Ctrl+U` |
| Mouse Shortcuts | Background tab `Ctrl+Click`, Download link `Alt+Click`, Scroll zoom `Ctrl+Wheel` |

## 🛠️ Built With
- **HTML5** — Semantic structure, no external frameworks.
- **Vanilla CSS** — CSS custom properties, Flexbox, Grid.
- **Vanilla JavaScript** — Accordion logic, filtering, theme, URL codec.
- **Google Fonts** — Share Tech Mono & Outfit.

## 📂 Project Structure

```
index.html               Main application entry point
style.css                All layout and theme styling
script.js                Interactive logic and UI state management
Img/                     Diagrams, study tips infographic, favicons
  favicon/               favicon.ico, favicon.svg, site.webmanifest
plan.md                  Development roadmap and task tracking
README.md                This file
patch_chrome_shortcuts.py  Idempotent injection script — adds Chrome shortcuts topic
```

## 🔧 Patch Scripts

Each `patch_*.py` is **idempotent** — safe to run multiple times.
Sentinel HTML comments prevent double-injection.

```bash
# From project root
python3 patch_chrome_shortcuts.py
```

The script:
1. Injects the Chrome shortcuts topic into `<!-- /domain-body shortcut -->` in `index.html`
2. Appends CSS additions to `style.css` (snap-quote animation, chip colours)
3. Rewrites `README.md` with updated content

## 📄 License
MIT License — see [LICENSE](LICENSE) for details.
