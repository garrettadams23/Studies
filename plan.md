# Structural Fix Plan — Tech Reference 2026

## Problems Identified

| # | File | Issue |
|---|------|-------|
| 1 | `script_additions.js` | Duplicate of the URL codec functions already in `script.js`. Never loaded by `index.html`. Dead code. |
| 2 | `index.html.bak` | Stale backup file tracked in git. Should be removed. |
| 3 | `patch-chrome-shortcuts` | Loose patch file in the root with no clear home. |
| 4 | `index.html` (19,784 lines / 917 KB) | All content is inlined — topics, tables, code blocks, diagrams. One file does everything. Hard to edit, search, or extend without scrolling thousands of lines. |
| 5 | `script.js` — `initCloudStack()` | Builds DOM rows using hardcoded `element.style.cssText` strings. Styles belong in `style.css`. |
| 6 | Global `onclick=""` handlers | Every interactive element uses inline HTML event attributes (`onclick="filter('net', this)"`). Couples JS to markup and pollutes the global scope. |
| 7 | Duplicate `lifestyle` domain | Second `data-domain="lifestyle"` section (Wicca/Paganism) at line 19232 was a separate, unfilterable section. |
| 8 | Chrome topic never applied | `patch_chrome_shortcuts.py` was committed but the shortcut content was never injected into the HTML. |

---

## Step 1 — Delete dead / stale files ✅

- [x] Delete `script_additions.js` (functions are duplicated from `script.js`; file is never loaded)
- [x] Delete `index.html.bak` (stale backup; git history preserves the old version)
- [x] Move `patch-chrome-shortcuts` → `tools/patch_chrome_shortcuts.py`

---

## Step 2 — Replace inline styles in `initCloudStack()` ✅

- [x] Added CSS classes to `style.css` (section 10):
  - `.cloud-row` — flex container
  - `.cloud-label` — label column
  - `.cloud-cell` — base cell
  - `.cloud-cell-c0` / `c1` / `c2` / `c3` — per-column customer colors
  - `.cloud-cell-provider` — muted provider style
- [x] Rewrote `initCloudStack()` in `script.js` to use `classList.add()` instead of `style.cssText`

---

## Step 3 — Remove inline `onclick` attributes ✅

- [x] Added `data-domain="..."` attributes to all chips in `index-shell.html`
- [x] Replaced `onclick` handlers with event delegation in `script.js` DOMContentLoaded:
  - `.filter-bar` → click on `.chip` reads `chip.dataset.domain`
  - `#domain-container` → click on `.domain-header` or `.topic-header`
  - `#hdr-theme-btn` / `#hdr-expand-btn` → direct listeners
- [x] Removed all structural `onclick="..."` from the HTML shell and domain content
- Note: 4 `onclick` attributes remain on URL codec action buttons (`urlToolEncode`, etc.) — these are form widget buttons, not structural navigation

---

## Step 4 — Break up the monolithic `index.html` (Option A) ✅

### New file structure

```
Studies/
  data/
    domains.json        ← domain metadata (id, icon, title, certTags, sub)
    net.html            ← inner topic content for Networking (16 topics)
    sec.html            ← Security Core (11 topics)
    threat.html         ← Threat & Attack (7 topics)
    grc.html            ← Governance & Risk (5 topics)
    ops.html            ← Sec Operations (6 topics)
    pentest.html        ← Penetration Testing (3 topics)
    linux.html          ← Linux & Systems (11 topics)
    ai.html             ← AI & ML (4 topics)
    script.html         ← Scripting & Web (25 topics)
    shortcut.html       ← Shortcuts (5 topics, incl. Chrome — now applied)
    lifestyle.html      ← Lifestyle & Philosophy (11 topics, incl. Wicca — merged)
    military.html       ← Military Staff Codes (6 topics)
  index-shell.html      ← Page skeleton (78 lines) — edit this
  build.py              ← Assembles shell + data/* → index.html
  index.html            ← Built output (self-contained, works with file://)
  script.js
  style.css
  tools/
    patch_chrome_shortcuts.py
  Img/
```

### Additional fixes made during extraction
- [x] Merged duplicate `lifestyle` section (Wicca/Paganism/Druidism) into `lifestyle.html`
- [x] Applied Chrome shortcuts topic to `shortcut.html` (patch was written but never run)
- [x] Corrected `data/domains.json` with accurate cert tags and subtitles

### To add content in the future
Edit `data/{domain}.html`, then run `python3 build.py`.

---

## Step 5 — Verify nothing broke ✅

- [x] 0 structural onclick attributes remain (only 4 URL codec widget buttons)
- [x] All 12 domain sections rendered with correct cert tags
- [x] 13 filter chips each have `data-domain` attribute
- [x] Script domain: 25 topics (was cut to 10 in first extraction due to extra topics outside the original domain-body)
- [x] Lifestyle: 11 topics (8 philosophy + 3 Wicca/Paganism merged)
- [x] Shortcut: 5 topics (General, Excel/Word, Spotify, DoD, Chrome)
- [x] Cloud stack renders via CSS classes
- [x] Theme toggle / expand-all use event listeners

### Remaining items to test in browser
- [ ] All filter chips show/hide correct domains
- [ ] Expand/collapse all works
- [ ] Theme toggle persists via `localStorage`
- [ ] URL codec encode, decode, copy, clear work
- [ ] Cloud stack matrix renders correctly
- [ ] Snap quote cycles on load
- [ ] Mobile touch feedback works (`.is-tapping`)
- [ ] Light mode and dark mode both look correct
