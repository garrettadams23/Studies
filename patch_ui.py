#!/usr/bin/env python3
"""
patch_ui.py — Three UI changes to the Tech Reference site:
  1. Move theme toggle (☀/☾) and expand-all (↕) into the header next to the badge
  2. Remove those two buttons from the filter bar
  3. Add a rotating snap-quote below the description paragraph in the header

Usage:  python3 patch_ui.py
Idempotent: skips already-patched files.
"""
import sys

SENTINEL = 'id="header-controls"'

# ─── 1. HEADER BADGE AREA — inject controls row ──────────────────────────────
# Insert after the header-badge div and before the h1.

BADGE_ANCHOR = '''          <div class="header-badge">
            CompTIA &amp; Tech Reference · 2026 Edition
          </div>
          <h1>'''

BADGE_REPLACEMENT = '''          <div class="header-top-row">
            <div class="header-badge">
              CompTIA &amp; Tech Reference · 2026 Edition
            </div>
            <div class="header-controls" id="header-controls">
              <button class="hdr-btn" id="hdr-theme-btn" onclick="toggleTheme(this)" title="Toggle theme">
                ☀
              </button>
              <button class="hdr-btn" id="hdr-expand-btn" onclick="toggleAll(this)" title="Expand / collapse all">
                ↕
              </button>
            </div>
          </div>
          <h1>'''

# ─── 2. QUOTE — insert after the <p> description ─────────────────────────────
P_ANCHOR = '''          </p>
        </div>
        <div class="header-image">'''

P_REPLACEMENT = '''          </p>
          <div class="snap-quote" id="snap-quote">
            <span class="sq-mark">"</span>
            <span class="sq-text" id="sq-text"></span>
            <span class="sq-mark">"</span>
          </div>
        </div>
        <div class="header-image">'''

# ─── 3. FILTER BAR — remove old theme + expand buttons ───────────────────────
# Strip the two utility chips that previously lived at the end of filter-inner.

THEME_BTN_ANCHOR = '''        <!-- Theme toggle — uses localStorage for persistence -->
        <div
          class="chip c-all"
          style="
            margin-left: auto;
            border-color: var(--amber);
            color: var(--amber);
          "
          onclick="toggleTheme(this)"
          id="theme-toggle-btn"
        >
          ☀ LIGHT MODE
        </div>
        <!-- Expand/collapse all accordion sections at once -->
        <div
          class="chip c-all"
          style="border-color: var(--cyan); color: var(--cyan)"
          onclick="toggleAll(this)"
        >
          ↕ EXPAND ALL
        </div>'''

THEME_BTN_REPLACEMENT = '''        <!-- theme + expand moved to header -->'''

# ─── CSS ADDITIONS ────────────────────────────────────────────────────────────
CSS_ADDITIONS = """
/* ── HEADER CONTROLS (theme + expand) ── */
.header-top-row {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 14px;
}
.header-controls { display: flex; gap: 8px; }
.hdr-btn {
  font-size: 16px;
  background: rgba(255,255,255,.06);
  border: 1px solid var(--border);
  color: var(--text);
  border-radius: 6px;
  width: 36px;
  height: 36px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background .2s, border-color .2s, transform .15s;
  padding: 0;
  line-height: 1;
}
.hdr-btn:hover {
  background: rgba(255,255,255,.12);
  border-color: var(--cyan);
  transform: translateY(-1px);
}
[data-theme="light"] .hdr-btn {
  background: rgba(0,0,0,.04);
  border-color: #c5d0de;
  color: #0f172a;
}
[data-theme="light"] .hdr-btn:hover {
  background: rgba(0,0,0,.09);
  border-color: #0284c7;
}

/* ── SNAP QUOTE ── */
.snap-quote {
  margin-top: 14px;
  padding: 10px 14px;
  border-left: 2px solid var(--cyan);
  background: rgba(0,212,255,.04);
  border-radius: 0 4px 4px 0;
  font-size: 12.5px;
  color: var(--muted);
  font-style: italic;
  line-height: 1.7;
  min-height: 42px;
  opacity: 0;
  transition: opacity .6s ease;
}
.snap-quote.visible { opacity: 1; }
.sq-mark { color: var(--cyan); font-size: 18px; line-height: 0; vertical-align: -4px; font-style: normal; }
.sq-text { margin: 0 4px; }
[data-theme="light"] .snap-quote {
  border-left-color: #0284c7;
  background: rgba(2,132,199,.04);
  color: #475569;
}
[data-theme="light"] .sq-mark { color: #0284c7; }
"""

# ─── JS ADDITIONS ─────────────────────────────────────────────────────────────
# Appended to script.js — handles:
#   • snap-quote rotation
#   • syncing the new header buttons with the old toggleTheme / toggleAll logic
JS_ADDITIONS = """
// ─────────────────────────────────────────────────────────────────────────────
// SNAP QUOTE — rotates through quotes in the header every 8 seconds
// ─────────────────────────────────────────────────────────────────────────────
(function initSnapQuote() {
  var quotes = [
    "The obstacle is the way. — Marcus Aurelius",
    "An unexamined life is not worth living. — Socrates",
    "Simplicity is the ultimate sophistication. — Leonardo da Vinci",
    "He who has a why can bear almost any how. — Nietzsche",
    "The Tao that can be told is not the eternal Tao. — Lao Tzu",
    "One must imagine Sisyphus happy. — Albert Camus",
    "We suffer more in imagination than in reality. — Seneca",
    "Before enlightenment, chop wood, carry water. — Zen proverb",
    "You have power over your mind, not outside events. — Marcus Aurelius",
    "The quieter you become, the more you can hear. — Ram Dass",
    "Amor fati — love your fate. — Nietzsche",
    "Water is the softest thing, yet it overcomes the hardest. — Lao Tzu",
    "To know yourself is the beginning of all wisdom. — Aristotle",
    "Security comes not from having things, but from releasing the need to control. — Epictetus",
    "In the middle of difficulty lies opportunity. — Albert Einstein",
    "Do not seek for things to happen the way you want them to. — Epictetus",
    "Peace comes from within. Do not seek it without. — Buddha",
    "The present moment always will have been. — Marcus Aurelius"
  ];

  window.addEventListener("DOMContentLoaded", function () {
    var el = document.getElementById("sq-text");
    var box = document.getElementById("snap-quote");
    if (!el || !box) return;

    var idx = Math.floor(Math.random() * quotes.length);

    function showQuote(i) {
      box.classList.remove("visible");
      setTimeout(function () {
        el.textContent = quotes[i % quotes.length];
        box.classList.add("visible");
      }, 600);
    }

    showQuote(idx);
    setInterval(function () {
      idx = (idx + 1) % quotes.length;
      showQuote(idx);
    }, 8000);
  });
})();

// ─────────────────────────────────────────────────────────────────────────────
// SYNC header buttons with existing toggleTheme / toggleAll state on load
// ─────────────────────────────────────────────────────────────────────────────
(function syncHeaderButtons() {
  window.addEventListener("DOMContentLoaded", function () {
    // Theme button — mirror saved theme into the new header button
    var hdrTheme = document.getElementById("hdr-theme-btn");
    if (hdrTheme) {
      var t = localStorage.getItem("theme") || "dark";
      hdrTheme.textContent = t === "light" ? "☾" : "☀";
    }
  });
})();

// Patch toggleTheme to also update the new header button
var _origToggleTheme = toggleTheme;
toggleTheme = function (btn) {
  _origToggleTheme(btn);
  // keep header icon in sync regardless of which button triggered the call
  var hdrBtn = document.getElementById("hdr-theme-btn");
  if (hdrBtn) {
    var theme = document.documentElement.getAttribute("data-theme");
    hdrBtn.textContent = theme === "light" ? "☾" : "☀";
  }
};

// Patch toggleAll to also update the new header button label
var _origToggleAll = toggleAll;
toggleAll = function (btn) {
  _origToggleAll(btn);
  var hdrBtn = document.getElementById("hdr-expand-btn");
  if (hdrBtn) {
    hdrBtn.title = allExpanded ? "Collapse all" : "Expand all";
  }
};
"""


# ─── HELPERS ──────────────────────────────────────────────────────────────────

def patch_replace(path, anchor, replacement, label):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    if anchor not in src:
        print(f"  ERROR {path} — anchor not found for: {label}")
        print(f"        Expected: {anchor[:80]!r}")
        sys.exit(1)
    patched = src.replace(anchor, replacement, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(patched)
    print(f"  OK    {path} — {label}")


def append_to(path, content, sentinel, label):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    if sentinel in src:
        print(f"  SKIP  {path} — {label} already applied")
        return
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)
    print(f"  OK    {path} — {label}")


def is_patched(path, sentinel):
    with open(path, "r", encoding="utf-8") as f:
        return sentinel in f.read()


# ─── MAIN ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Applying UI patches...")

    if is_patched("index.html", SENTINEL):
        print("  SKIP  index.html — already patched")
    else:
        patch_replace("index.html", BADGE_ANCHOR, BADGE_REPLACEMENT, "header badge → top-row with buttons")
        patch_replace("index.html", P_ANCHOR, P_REPLACEMENT, "snap-quote below description")
        patch_replace("index.html", THEME_BTN_ANCHOR, THEME_BTN_REPLACEMENT, "removed filter-bar theme+expand chips")

    append_to("style.css", CSS_ADDITIONS, "hdr-btn", "header controls + snap-quote CSS")
    append_to("script.js", JS_ADDITIONS, "initSnapQuote", "snap-quote + button sync JS")

    print("Done.")
