#!/usr/bin/env python3
"""
patch_search.py
Adds a search bar to the IT reference tool.
Run from project root: python3 patch_search.py
"""

import sys

# ── Injection targets ────────────────────────────────────────────────────────
FILES = {
    "index.html": [
        {
            # Insert search bar row between filter-bar and container
            "anchor": "<!-- /container -->",
            "mode":   "before",
            "guard":  "search-bar",
            "html": """\
    <!-- SEARCH BAR ──────────────────────────────────────────────────────── -->
    <div class="search-bar" id="search-bar">
      <div class="search-inner">
        <span class="search-icon">⌕</span>
        <input
          id="search-input"
          class="search-input"
          type="search"
          placeholder="Search topics, concepts, code…"
          oninput="searchContent(this.value)"
          autocomplete="off"
          spellcheck="false"
        />
        <button class="search-clear" id="search-clear" onclick="clearSearch()" title="Clear search">✕</button>
        <span class="search-count" id="search-count"></span>
      </div>
    </div>
    <!-- /search-bar -->
""",
        }
    ],
    "style.css": [
        {
            # Append CSS at end of file
            "anchor": None,
            "mode":   "append",
            "guard":  ".search-bar",
            "css": """
/* ── SEARCH BAR ─────────────────────────────────────────────────────────── */
.search-bar {
  position: sticky; top: 45px; z-index: 99;
  background: rgba(7, 9, 15, 0.97); backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border); padding: 10px 24px;
}
[data-theme="light"] .search-bar { background: rgba(240, 244, 248, 0.97); }

.search-inner {
  display: flex; align-items: center; gap: 10px;
  max-width: 680px; margin: 0 auto;
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: 4px; padding: 0 12px; transition: border-color 0.2s;
}
.search-inner:focus-within { border-color: var(--cyan); }

.search-icon { color: var(--muted); font-size: 18px; flex-shrink: 0; line-height: 1; }

.search-input {
  flex: 1; background: transparent; border: none; outline: none;
  font-family: var(--mono); font-size: 13px; color: var(--text);
  padding: 9px 0; caret-color: var(--cyan);
}
.search-input::placeholder { color: var(--muted); }

.search-clear {
  background: transparent; border: none; color: var(--muted);
  font-size: 12px; cursor: pointer; padding: 4px 2px;
  opacity: 0; transition: opacity 0.15s; flex-shrink: 0;
}
.search-clear.visible { opacity: 1; }
.search-clear:hover { color: var(--red); }

.search-count {
  font-family: var(--mono); font-size: 10px; color: var(--cyan);
  white-space: nowrap; flex-shrink: 0; min-width: 60px; text-align: right;
}

/* Highlight matched text */
mark.sh {
  background: rgba(0, 212, 255, 0.25); color: inherit;
  border-radius: 2px; padding: 0 1px;
}
[data-theme="light"] mark.sh { background: rgba(0, 150, 200, 0.2); }

/* Dim non-matching topics during search */
.topic.search-hidden { display: none; }
.domain-section.search-hidden { display: none; }

@media (max-width: 600px) {
  .search-bar { top: 40px; padding: 8px 12px; }
}
""",
        }
    ],
    "script.js": [
        {
            # Append JS at end of file
            "anchor": None,
            "mode":   "append",
            "guard":  "searchContent",
            "js": """
// ─────────────────────────────────────────────────────────────────────────────
// SEARCH
// ─────────────────────────────────────────────────────────────────────────────

/** Stored original innerHTML for each searchable node (keyed by element). */
const _originals = new WeakMap();

/** Save original HTML before first search so we can restore highlights. */
function saveOriginal(el) {
  if (!_originals.has(el)) _originals.set(el, el.innerHTML);
}

/** Restore all saved originals (removes highlights). */
function restoreOriginals() {
  document.querySelectorAll("[data-search-marked]").forEach(el => {
    if (_originals.has(el)) el.innerHTML = _originals.get(el);
    el.removeAttribute("data-search-marked");
  });
}

/**
 * Highlight all occurrences of `term` in el.innerHTML.
 * Works on text nodes only — avoids mangling tag attributes.
 */
function highlightIn(el, term) {
  saveOriginal(el);
  const escaped = term.replace(/[.*+?^${}()|[\]\\\\]/g, "\\\\$&");
  const re = new RegExp(`(${escaped})`, "gi");
  el.innerHTML = el.innerHTML.replace(re, '<mark class="sh">$1</mark>');
  el.setAttribute("data-search-marked", "1");
}

/**
 * Main search handler — called on every keystroke.
 * @param {string} raw - Current value of the search input.
 */
function searchContent(raw) {
  const term = raw.trim();
  const clearBtn = document.getElementById("search-clear");
  const countEl  = document.getElementById("search-count");

  // Show/hide clear button
  if (clearBtn) clearBtn.classList.toggle("visible", term.length > 0);

  // Reset all previous highlights and visibility
  restoreOriginals();
  document.querySelectorAll(".topic.search-hidden, .domain-section.search-hidden")
    .forEach(el => el.classList.remove("search-hidden"));

  if (term.length < 2) {
    if (countEl) countEl.textContent = "";
    return;
  }

  const termLower = term.toLowerCase();
  let matchCount = 0;

  document.querySelectorAll(".domain-section").forEach(domain => {
    let domainHasMatch = false;

    domain.querySelectorAll(".topic").forEach(topic => {
      // Searchable nodes inside each topic
      const nodes = [
        ...topic.querySelectorAll(".topic-name, .concept-title, .concept-label, .concept-desc, .dw, .dt, .code-block"),
      ];

      const topicText = topic.textContent.toLowerCase();
      const matches   = topicText.includes(termLower);

      if (matches) {
        domainHasMatch = true;
        matchCount++;

        // Auto-expand the topic and its parent domain
        topic.querySelector(".topic-header")?.classList.add("open");
        topic.querySelector(".topic-body")?.classList.add("open");
        domain.querySelector(".domain-header")?.classList.add("open");
        domain.querySelector(".domain-body")?.classList.add("open");

        // Highlight in text-bearing nodes
        nodes.forEach(n => highlightIn(n, term));
      } else {
        topic.classList.add("search-hidden");
      }
    });

    if (!domainHasMatch) domain.classList.add("search-hidden");
  });

  if (countEl) countEl.textContent = matchCount ? `${matchCount} match${matchCount !== 1 ? "es" : ""}` : "no matches";
}

/** Clear search input and reset view. */
function clearSearch() {
  const input = document.getElementById("search-input");
  if (input) { input.value = ""; input.focus(); }
  searchContent("");
}
""",
        }
    ],
}

# ── Patch engine ─────────────────────────────────────────────────────────────

def patch(path, injections):
    try:
        with open(path, "r", encoding="utf-8") as f:
            src = f.read()
    except FileNotFoundError:
        print(f"  ✗ NOT FOUND: {path}")
        return False

    changed = False
    for inj in injections:
        guard = inj["guard"]
        if guard in src:
            print(f"  ✓ SKIP (already applied): {guard} in {path}")
            continue

        mode = inj["mode"]
        content = inj.get("html") or inj.get("css") or inj.get("js", "")

        if mode == "before":
            anchor = inj["anchor"]
            if anchor not in src:
                print(f"  ✗ ANCHOR NOT FOUND: '{anchor}' in {path}")
                continue
            src = src.replace(anchor, content + anchor, 1)
            print(f"  ✓ INJECTED before '{anchor}' in {path}")
            changed = True

        elif mode == "append":
            src = src + content
            print(f"  ✓ APPENDED to {path}")
            changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(src)
    return changed


# ── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== patch_search.py — Search Bar Injection ===\n")
    ok = True
    for filepath, injections in FILES.items():
        print(f"[{filepath}]")
        result = patch(filepath, injections)
        if result is False:
            ok = False
        print()

    if ok:
        print("Done. Run: open index.html")
    else:
        print("One or more files were missing — check paths.", file=sys.stderr)
        sys.exit(1)
