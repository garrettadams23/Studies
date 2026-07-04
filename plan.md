# Improvement Plan — Tech & Life Reference (July 2026 Review)

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
- [ ] Applied

### 2. Delete duplicate/dead data files
- **Evidence:** `data/disorder_data.js` and `Patches files/disorder_data.js` are
  byte-identical (135,544 bytes each) and **neither is loaded by anything**
  (no `<script src>` references in `index-shell.html`/`index.html`).
- **Fix:** Delete both (git history preserves them).
- [ ] Applied

### 3. Delete `studies.html` (560 KB)
- **Evidence:** Old pre-split monolith ("CompTIA & Tech Reference" title, old
  formatting). Nothing references it — not `index.html`, `script.js`, or `README.md`.
- **Fix:** Delete. It's a stale snapshot that will only drift further from reality.
- [ ] Applied

### 4. Fix the `.topic-chevron` styling bug (287 topics affected)
- **Evidence:** Newer content waves emit `<span class="topic-chevron">›</span>`
  (287 occurrences in `data/*.html`) but `style.css` only defines `.topic-chev`
  (112 occurrences use that). The 287 newer topics have an unstyled chevron that
  doesn't rotate on expand.
- **Fix (pick one):**
  - a) One-time `sed` across `data/*.html`: `topic-chevron` → `topic-chev`, rebuild; or
  - b) Add `.topic-chevron` as an alias selector next to every `.topic-chev` rule.
  Option (a) is cleaner long-term.
- [ ] Applied

### 5. Crush the image weight (~14 MB → well under 1 MB)
- **Evidence:**
  - `Img/Studying-Tips.png` = **7.5 MB** — loaded in the page header.
  - `Img/favicon/favicon.svg` = **6.7 MB** — an SVG favicon should be ~1–5 KB;
    this almost certainly has a giant embedded raster.
  - `Img/favicon/web-app-manifest-512x512.png` = 388 KB.
- **Fix:** Re-export Studying-Tips as WebP/optimized PNG at display resolution
  (~100–300 KB); regenerate favicon.svg as a true vector (or drop it — the
  96×96 PNG + .ico already cover browsers); `oxipng`/`squoosh` the manifest PNGs.
- [ ] Applied

---

## P2 — Performance

### 6. Minify output in `build.py` (~450 KB / 19% off index.html)
- **Evidence:** `index.html` is 2,375,874 chars; stripping leading indentation
  alone saves 19% (~452 KB). The data files are heavily indented.
- **Fix:** In `build.py`, strip leading whitespace and collapse blank lines when
  assembling (safe for this markup — but skip lines inside `<pre`…`</pre>` so
  `.code-block` formatting is preserved). Keep `data/*.html` pretty for editing;
  only the built output gets minified.
- [ ] Applied

### 7. Debounce + index the search (currently full-DOM scan per keystroke)
- **Evidence:** `index-shell.html:92` wires `oninput="searchContent(this.value)"`;
  `searchContent()` (script.js ~708) walks every `.domain-section`/`.topic` and
  lowercases each topic's full `textContent` on **every keystroke** against a
  2.4 MB DOM. No debounce.
- **Fix:** (a) debounce 150–250 ms; (b) build a one-time cache
  `Map<topicEl, lowercasedText>` on first search and reuse it; (c) only run
  highlighting on the visible/matched topics (already mostly true).
- [ ] Applied

### 8. Fix search-highlight markup corruption
- **Evidence:** `highlightIn()` (script.js ~695) does
  `el.innerHTML = el.innerHTML.replace(re, '<mark>…')` — despite the comment
  claiming "text nodes only", it regex-replaces the raw HTML string. Searching
  terms that appear inside tags/attributes (e.g. `table`, `span`, `color`,
  `href`) injects `<mark>` inside tags and corrupts the DOM until cleared.
- **Fix:** Walk actual text nodes (`TreeWalker` with `NodeFilter.SHOW_TEXT`) and
  wrap matches in `<mark>` — never string-replace `innerHTML`.
- [ ] Applied

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
- [ ] Applied

### 10. Self-host or gracefully degrade Google Fonts
- **Evidence:** Both `index-shell.html` and `notepad.jsx` pull Share Tech Mono +
  Outfit from `fonts.googleapis.com`. Offline / file:// use falls back silently;
  it's also the only remaining third-party call once #9 lands.
- **Fix:** Either self-host the two WOFF2 files under `Img/fonts/` (works
  offline, no tracking), or keep the CDN but add
  `<link rel="preconnect" href="https://fonts.gstatic.com">` and rely on
  `display=swap` (already present).
- [ ] Applied

---

## P3 — Security

### 11. Unpinned third-party scripts (supply-chain risk)
- **Evidence:** `https://unpkg.com/@babel/standalone/babel.min.js` has **no
  version pin** — unpkg serves the latest tag, so a compromised or broken
  release ships straight to the page. React/ReactDOM are major-pinned only
  (`react@18`). None have Subresource Integrity (SRI) hashes.
- **Fix:** Item #9 removes all three. If any CDN script is ever kept: pin the
  exact version and add `integrity="sha384-…" crossorigin="anonymous"`.
- [ ] Applied (superseded by #9)

### 12. `target="_blank"` without `rel="noopener noreferrer"`
- **Evidence:** 1 occurrence in `data/script.html`. Opened pages get a
  `window.opener` handle (tab-nabbing) — low risk here but free to fix.
- **Fix:** Add `rel="noopener noreferrer"`; make it a convention for future content.
- [ ] Applied

### 13. "Shared" notepad isn't shared — clarify or wire a backend
- **Evidence:** `notepad.jsx` stores notes in `localStorage`
  (`shared-notepad-notes`) and polls every 8 s "for new notes from others" —
  but localStorage never leaves the browser. The UI wording ("shared notepad")
  overpromises; the polling only syncs tabs on the same machine.
- **Fix:** When rewriting (#9), rename to "Notepad", keep localStorage, and use
  the `storage` event instead of polling. (A real shared backend would need a
  service + auth — out of scope for a static site.)
- [ ] Applied

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
- [ ] Applied

### 16. Per-topic permalinks + deep linking
- **Evidence:** No way to link someone to a specific topic; the page always
  opens fully collapsed at the top.
- **Fix:** At load, assign stable slug `id`s to each `.topic` (from topic name);
  on header click update `location.hash`; on load, expand + scroll to the
  hash target. Pairs well with a "copy link" icon on each topic header.
- [ ] Applied

### 17. Study-progress tracking ("mark as reviewed")
- **Idea:** This is a study site with hundreds of topics and no sense of
  progress. A small checkmark toggle per topic persisted to localStorage
  (`reviewed:{slug}`), plus a per-domain "12/31 reviewed" counter in the domain
  header, would make revision passes far more effective. Cheap to build on top
  of #16's slugs.
- [ ] Applied

### 18. Back-to-top button + print stylesheet
- **Evidence:** The built page is very long; there's no quick way back to the
  filter bar. Printing currently emits dark backgrounds and collapsed bodies.
- **Fix:** Floating ↑ button (appears after ~2 screens). `@media print`: force
  light theme, expand all bodies, hide header controls/notepad/search.
- [ ] Applied

### 19. `prefers-reduced-motion` support
- **Evidence:** Accordion/theme transitions animate unconditionally.
- **Fix:** `@media (prefers-reduced-motion: reduce)` block that zeroes
  transition durations and disables animations.
- [ ] Applied

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
- [ ] Applied

---

## P5 — Repo hygiene, docs & tooling

### 21. Rename `Patches files/` → `patches/`
- **Evidence:** The space in the directory name forces quoting in every shell
  command and breaks naive tooling. It holds ~1.9 MB of one-time,
  already-applied injection scripts.
- **Fix:** `git mv "Patches files" patches`. Optionally add `patches/README.md`
  noting these are historical (idempotent, already applied — safe to re-run but
  never needed).
- [ ] Applied

### 22. Update `README.md` to match reality
- **Evidence:** README's project-structure block omits `studies.html`,
  `notepad.jsx`, `reconcile_build.py`, `Patches files/`, and `plan.md`; it
  documents `domains.js` (actual file is `domains.json`), and the notepad/CDN
  dependency isn't mentioned anywhere.
- **Fix:** Refresh the structure block after P1 deletions land; document
  `reconcile_build.py` (recovery tool: syncs a hand-patched `index.html` back
  into `data/*`) and the build workflow (`edit data/ → python3 build.py`).
- [ ] Applied

### 23. CI guard: fail if `index.html` is stale
- **Evidence:** `index.html` is a tracked build artifact; nothing verifies it
  matches `data/*`. A hand-edit to `index.html` silently diverges (the failure
  mode `reconcile_build.py` exists to repair).
- **Fix:** GitHub Action on push/PR: `python3 build.py && git diff --exit-code
  index.html`. ~15 lines of YAML; catches drift forever.
- [ ] Applied

### 24. Repo growth awareness
- **Evidence:** Every content wave re-commits the full 2.4 MB `index.html`;
  ~50 waves in, history carries dozens of full copies (git delta-compresses,
  but HTML deltas across injections are large).
- **Fix:** Keep tracking `index.html` (file:// usage depends on it), but the
  minification in #6 shrinks each future delta, and the P1 deletions
  (`studies.html`, dead data, 14 MB of images) stop the worst bloat. No history
  rewrite needed.
- [ ] Applied (via #5, #6)

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
