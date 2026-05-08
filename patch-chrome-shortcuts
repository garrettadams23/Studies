#!/usr/bin/env python3
"""
patch_chrome_shortcuts.py
Injects Chrome keyboard shortcuts topic into the Shortcuts domain.
Also updates style.css and script.js with minimal additions.
Run from project root: python3 patch_chrome_shortcuts.py
"""

import sys

# ── CHROME SHORTCUTS HTML FRAGMENT ──────────────────────────────────────────
CHROME_TOPIC = '''
          <!-- ── TOPIC: CHROME SHORTCUTS ──────────────────────────────── -->
          <!-- /chrome-topic-start -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">🌐</span>
              <span class="topic-name">Google Chrome — Keyboard Shortcuts</span>
              <span class="topic-badge">WIN · MAC · LINUX</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Reference — Google Chrome</div>
                <div class="concept-title">Tabs · Windows · Address Bar · Webpage · Mouse · DevTools</div>
                <div class="concept-desc">
                  Shortcuts use <strong style="color:var(--cyan)">Ctrl</strong> on Windows/Linux and
                  <strong style="color:var(--amber)">⌘</strong> on Mac.
                  Mac equivalents shown in brackets where they differ.
                </div>
                <div class="dw">

                  <div class="dt">▸ TABS &amp; WINDOWS</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Action</th><th>Windows / Linux</th><th>Mac</th></tr>
                    <tr><td>New window</td><td>Ctrl + N</td><td>⌘ + N</td></tr>
                    <tr><td>New Incognito window</td><td>Ctrl + Shift + N</td><td>⌘ + Shift + N</td></tr>
                    <tr><td>New tab</td><td>Ctrl + T</td><td>⌘ + T</td></tr>
                    <tr><td>Reopen last closed tab</td><td>Ctrl + Shift + T</td><td>⌘ + Shift + T</td></tr>
                    <tr><td>Next tab</td><td>Ctrl + Tab / Ctrl + PgDn</td><td>⌘ + Option + →</td></tr>
                    <tr><td>Previous tab</td><td>Ctrl + Shift + Tab / Ctrl + PgUp</td><td>⌘ + Option + ←</td></tr>
                    <tr><td>Jump to tab 1–8</td><td>Ctrl + 1–8</td><td>⌘ + 1–8</td></tr>
                    <tr><td>Jump to last tab</td><td>Ctrl + 9</td><td>⌘ + 9</td></tr>
                    <tr><td>Close current tab</td><td>Ctrl + W / Ctrl + F4</td><td>⌘ + W</td></tr>
                    <tr><td>Close current window</td><td>Ctrl + Shift + W / Alt + F4</td><td>⌘ + Shift + W</td></tr>
                    <tr><td>Quit Chrome</td><td>Alt + F then X</td><td>⌘ + Q</td></tr>
                    <tr><td>Full-screen toggle</td><td>F11</td><td>Fn + F</td></tr>
                    <tr><td>Move tab right / left</td><td>Ctrl + Shift + PgDn / PgUp</td><td>Ctrl + Shift + PgDn / PgUp</td></tr>
                    <tr><td>Home page (current tab)</td><td>Alt + Home</td><td>—</td></tr>
                    <tr><td>Back / Forward (history)</td><td>Alt + ← / Alt + →</td><td>⌘ + [ / ⌘ + ]</td></tr>
                  </table>

                  <div class="dt">▸ CHROME FEATURES</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Action</th><th>Windows / Linux</th><th>Mac</th></tr>
                    <tr><td>Open Chrome menu</td><td>Alt + F or Alt + E</td><td>—</td></tr>
                    <tr><td>Bookmarks bar toggle</td><td>Ctrl + Shift + B</td><td>⌘ + Shift + B</td></tr>
                    <tr><td>Bookmark Manager</td><td>Ctrl + Shift + O</td><td>⌘ + Option + B</td></tr>
                    <tr><td>History page</td><td>Ctrl + H</td><td>⌘ + Y</td></tr>
                    <tr><td>Downloads page</td><td>Ctrl + J</td><td>⌘ + Shift + J</td></tr>
                    <tr><td>Chrome Task Manager</td><td>Shift + Esc</td><td>—</td></tr>
                    <tr><td>Find on page</td><td>Ctrl + F / F3</td><td>⌘ + F</td></tr>
                    <tr><td>Next find result</td><td>Ctrl + G</td><td>⌘ + G</td></tr>
                    <tr><td>Previous find result</td><td>Ctrl + Shift + G</td><td>⌘ + Shift + G</td></tr>
                    <tr><td>Developer Tools</td><td>Ctrl + Shift + J / F12</td><td>⌘ + Option + I</td></tr>
                    <tr><td>Clear browsing data</td><td>Ctrl + Shift + Delete</td><td>⌘ + Shift + Delete</td></tr>
                    <tr><td>Settings</td><td>—</td><td>⌘ + ,</td></tr>
                    <tr><td>Split view (active tab)</td><td>Shift + Alt + N</td><td>⌘ + Option + N</td></tr>
                    <tr><td>Caret browsing</td><td>F7</td><td>F7</td></tr>
                    <tr><td>Skip to web content</td><td>Ctrl + F6</td><td>—</td></tr>
                  </table>

                  <div class="dt">▸ ADDRESS BAR</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Action</th><th>Windows / Linux</th><th>Mac</th></tr>
                    <tr><td>Focus address bar</td><td>Ctrl + L / Alt + D / F6</td><td>⌘ + L</td></tr>
                    <tr><td>Search from anywhere</td><td>Ctrl + K / Ctrl + E</td><td>⌘ + Option + F</td></tr>
                    <tr><td>Open search in new tab</td><td>Type term + Alt + Enter</td><td>Type term + ⌘ + Return</td></tr>
                    <tr><td>Add www. and .com, open</td><td>Type name + Ctrl + Enter</td><td>Type name + Ctrl + Return</td></tr>
                    <tr><td>Open in new window</td><td>Type name + Ctrl + Shift + Enter</td><td>Type name + Ctrl + Shift + Return</td></tr>
                    <tr><td>Remove address prediction</td><td>↓ highlight + Shift + Delete</td><td>↓ highlight + Shift + Fn + Delete</td></tr>
                  </table>

                  <div class="dt">▸ WEBPAGE NAVIGATION</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Action</th><th>Windows / Linux</th><th>Mac</th></tr>
                    <tr><td>Print page</td><td>Ctrl + P</td><td>⌘ + P</td></tr>
                    <tr><td>Save page</td><td>Ctrl + S</td><td>⌘ + S</td></tr>
                    <tr><td>Reload page</td><td>F5 / Ctrl + R</td><td>⌘ + R</td></tr>
                    <tr><td>Hard reload (ignore cache)</td><td>Shift + F5 / Ctrl + Shift + R</td><td>⌘ + Shift + R</td></tr>
                    <tr><td>Stop loading</td><td>Esc</td><td>Esc</td></tr>
                    <tr><td>Bookmark current page</td><td>Ctrl + D</td><td>⌘ + D</td></tr>
                    <tr><td>Bookmark all open tabs</td><td>Ctrl + Shift + D</td><td>⌘ + Shift + D</td></tr>
                    <tr><td>Zoom in / out</td><td>Ctrl + + / Ctrl + -</td><td>⌘ + + / ⌘ + -</td></tr>
                    <tr><td>Reset zoom</td><td>Ctrl + 0</td><td>⌘ + 0</td></tr>
                    <tr><td>Scroll down one screen</td><td>Space / PgDn</td><td>Space</td></tr>
                    <tr><td>Scroll up one screen</td><td>Shift + Space / PgUp</td><td>Shift + Space</td></tr>
                    <tr><td>Go to top / bottom</td><td>Home / End</td><td>⌘ + ↑ / ⌘ + ↓</td></tr>
                    <tr><td>View page source</td><td>Ctrl + U</td><td>⌘ + Option + U</td></tr>
                    <tr><td>JavaScript console</td><td>Ctrl + Shift + J</td><td>⌘ + Option + J</td></tr>
                    <tr><td>Delete previous word (field)</td><td>Ctrl + Backspace</td><td>Option + Delete</td></tr>
                  </table>

                  <div class="dt">▸ MOUSE SHORTCUTS</div>
                  <table class="ref-table">
                    <tr><th>Action</th><th>Shortcut</th></tr>
                    <tr><td style="color:var(--cyan)">Open link in background tab</td><td>Ctrl + Click (⌘ + Click on Mac)</td></tr>
                    <tr><td style="color:var(--cyan)">Open link &amp; jump to it</td><td>Ctrl + Shift + Click</td></tr>
                    <tr><td style="color:var(--cyan)">Open link in new window</td><td>Shift + Click</td></tr>
                    <tr><td style="color:var(--cyan)">Download link target</td><td>Alt + Click (Option + Click on Mac)</td></tr>
                    <tr><td style="color:var(--cyan)">Drag link to open in tab</td><td>Drag to blank area of tab strip</td></tr>
                    <tr><td style="color:var(--cyan)">Pop tab into new window</td><td>Drag tab out of tab strip</td></tr>
                    <tr><td style="color:var(--cyan)">Zoom in / out</td><td>Ctrl + Scroll wheel up / down</td></tr>
                    <tr><td style="color:var(--cyan)">Scroll horizontally</td><td>Shift + Scroll wheel</td></tr>
                    <tr><td style="color:var(--cyan)">View browsing history</td><td>Right-click / hold Back or Forward</td></tr>
                  </table>

                </div>
              </div>
            </div>
          </div>
          <!-- /chrome-topic-end -->
'''

# ── CSS ADDITIONS ────────────────────────────────────────────────────────────
CSS_ADDITION = '''
/* ── Chrome shortcut chip accent ── */
.chip.c-shortcut { color: #facc15; border-color: rgba(250,204,21,.3); }
.chip.c-shortcut.active, .chip.c-shortcut:hover { background: rgba(250,204,21,.10); }

/* ── snap-quote fade animation (if not already present) ── */
.snap-quote { opacity: 0; transition: opacity .6s ease; min-height: 28px; margin-top: 10px; font-style: italic; font-size: 12px; color: var(--muted); }
.snap-quote.visible { opacity: 1; }
.sq-mark { color: var(--cyan); font-size: 18px; vertical-align: middle; }
.sq-text { margin: 0 4px; }
'''

# ── SCRIPT.JS ADDITIONS (snap-quote styles already in script; no change needed)
# No JS changes required for this patch.

# ── README UPDATE ─────────────────────────────────────────────────────────────
README_CONTENT = '''# 🧠 CompTIA & Tech Reference — 2026 Edition

A comprehensive, interactive web-based reference for IT professionals, students,
and enthusiasts. Organized by concept domain with a dark/light theme engine,
collapsible accordions, syntax-highlighted code blocks, and reference tables.

## 🚀 Live Demo
Open `index.html` in any modern web browser — no build step required.

## 🌟 Key Features
- **Interactive Filtering** — Toggle between domains via chip nav bar.
- **Theme Engine** — Dark/Light mode with LocalStorage persistence.
- **Collapsible Accordions** — Domain and topic-level expand/collapse.
- **Expand All / Collapse All** — Header button for bulk toggle.
- **Rotating Snap Quotes** — 18 philosophical quotes, 8 s fade cycle.
- **URL Encode/Decode Widget** — Interactive tool in the Scripting domain.
- **CVSS v3.1 Calculator** — Interactive scoring in Threat Frameworks.

## 📚 Domains Covered

| Domain | Certs / Tags | Topics |
|---|---|---|
| 🌐 Networking | A+, Net+ | OSI, TCP/IP, Subnetting, Routing, VLANs, Wireless, DNS, Cabling, NMAP, TCPDump |
| 🔐 Security Core | Sec+, SecX | CIA Triad, AAA, PKI, Crypto, Cloud, Zero Trust, Kerberos, Password Attacks |
| ⚔️ Threat & Attack | Sec+, CySA+, PT+ | Kill Chain, MITRE ATT&CK, Diamond Model, Social Engineering, Malware, DoS, Google Hacking |
| ⚖️ Governance & Risk | Sec+, SecX | NIST CSF 2.0, Risk Matrix, Defense-in-Depth, Legal Frameworks, CISSP 8 Domains |
| 🔬 Sec Operations | CySA+, SecX | IR PICERL, Vulnerability Mgmt, Troubleshooting, BCP/DR, Digital Forensics, Splunk SPL |
| 🎯 PenTest | PT+ | 5-Phase Methodology, OWASP Top 10, SQLmap |
| 🐧 Linux & Systems | Linux+, A+ | FHS, File Permissions, Boot Process, SSH, Tmux, Unix Commands, RAID, A+ Hardware |
| 🤖 AI & ML | AI+ | ML Pipeline, Learning Paradigms, Agentic AI, Ethics (NIST AI RMF) |
| 💻 Scripting & Web | Linux+, SecX | Regex, PowerShell, Bash, ZSH, Go, Python, HTML, CSS, JavaScript ES2022–ES2025, JSON/jq, SQL, URL Encoding |
| ⌨️ Shortcuts | General | Windows, Linux Terminal, Excel, Word, Spotify, **Google Chrome**, DoD/Military |
| 🧘 Lifestyle & Philosophy | Life | Stoicism, Machiavellianism, Psychology, Buddhism, Taoism, Existentialism, Minimalism, Wicca, Paganism, Druidism |
| 🎖️ Military Codes | MIL | NATO Phonetic, Military Time, US Army Ranks, CMMC, DISA STIGs, Clearances, Staff Codes J/G/S/N/A/C |

## ⌨️ Chrome Keyboard Shortcuts (new in this release)
Full reference for **Windows/Linux** and **Mac** covering:
- Tabs & Windows management
- Chrome feature shortcuts (DevTools, Bookmarks, History, Downloads)
- Address bar power shortcuts
- Webpage navigation & zoom
- Mouse shortcuts

Source: [Google Chrome Help](https://support.google.com/chrome/answer/157179)

## 🛠️ Built With
- **HTML5** — Semantic structure, no frameworks.
- **Vanilla CSS** — CSS custom properties, Flexbox, Grid.
- **Vanilla JavaScript** — Accordion logic, filtering, theme management.
- **Google Fonts** — Share Tech Mono & Outfit.

## 📂 Project Structure
```
index.html          Main application entry point
style.css           All layout and theme styling
script.js           Interactive logic and UI state
Img/                Diagrams, study tips infographic, favicons
plan.md             Development roadmap
patch_*.py          Idempotent injection scripts (run from project root)
```

## 🔧 Patch Scripts
Each `patch_*.py` script is **idempotent** — safe to run multiple times.
Sentinel comments prevent double-injection. Run from project root:
```bash
python3 patch_chrome_shortcuts.py
```

## 📄 License
MIT License — see [LICENSE](LICENSE) for details.
'''

# ── PATCH LOGIC ──────────────────────────────────────────────────────────────
ANCHOR_HTML  = "<!-- /domain-body shortcut -->"
SENTINEL     = "<!-- /chrome-topic-end -->"

def patch_html(path="index.html"):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    if SENTINEL in src:
        print(f"[SKIP] {path} — Chrome topic already injected.")
        return
    if ANCHOR_HTML not in src:
        print(f"[FAIL] {path} — anchor '{ANCHOR_HTML}' not found.", file=sys.stderr)
        sys.exit(1)
    patched = src.replace(ANCHOR_HTML, CHROME_TOPIC + "\n        " + ANCHOR_HTML)
    with open(path, "w", encoding="utf-8") as f:
        f.write(patched)
    print(f"[OK]   {path} — Chrome shortcuts topic injected.")

CSS_SENTINEL = "/* ── Chrome shortcut chip accent ── */"

def patch_css(path="style.css"):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    if CSS_SENTINEL in src:
        print(f"[SKIP] {path} — CSS already patched.")
        return
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n" + CSS_ADDITION)
    print(f"[OK]   {path} — CSS additions appended.")

def update_readme(path="README.md"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(README_CONTENT)
    print(f"[OK]   {path} — README updated.")

if __name__ == "__main__":
    patch_html()
    patch_css()
    update_readme()
    print("\nDone. Refresh index.html in your browser.")
