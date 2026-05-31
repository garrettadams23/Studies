#!/usr/bin/env python3
"""
patch_notepad.py
Adds a slide-out shared notepad tab to index.html.
Requires: notepad.jsx in the same directory.
Run from project root: python3 patch_notepad.py
"""
import sys, os

# ── Fragments ────────────────────────────────────────────────────────────────

# 1. CDN scripts for React + Babel — injected before </head>
HEAD_SCRIPTS = """\
  <!-- NOTEPAD: React + Babel CDN -->
  <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
  <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
"""

# 2. Slide tab button + panel shell — injected before </body>
BODY_HTML = """\
  <!-- NOTEPAD: slide tab -->
  <button id="notepad-tab" class="notepad-tab" onclick="toggleNotepad()" title="Open shared notepad">
    <span class="notepad-tab-icon">📋</span>
    <span class="notepad-tab-label">NOTEPAD</span>
  </button>

  <div id="notepad-panel" class="notepad-panel">
    <div id="notepad-root">
      <div class="notepad-loading">Loading notepad…</div>
    </div>
  </div>
"""

# 3. CSS — appended to style.css
NOTEPAD_CSS = """
/* ── NOTEPAD SLIDE TAB ──────────────────────────────────────────────────── */
.notepad-tab {
  position: fixed; right: 0; top: 50%;
  transform: translateY(-50%) rotate(0deg);
  z-index: 1100;
  display: flex; flex-direction: column; align-items: center; gap: 6px;
  background: var(--bg2); border: 1px solid var(--border);
  border-right: none; border-radius: 6px 0 0 6px;
  padding: 14px 8px; cursor: pointer;
  transition: background 0.2s, border-color 0.2s, transform 0.2s;
}
.notepad-tab:hover { background: var(--bg3); border-color: var(--cyan); }
.notepad-tab.open  { border-color: var(--cyan); background: var(--bg3); }

.notepad-tab-icon  { font-size: 18px; line-height: 1; }
.notepad-tab-label {
  font-family: var(--mono); font-size: 9px; color: var(--cyan);
  letter-spacing: 2px; text-transform: uppercase;
  writing-mode: vertical-rl; transform: rotate(180deg);
}

.notepad-panel {
  position: fixed; top: 0; right: -440px; width: 420px; height: 100vh;
  background: var(--bg); border-left: 1px solid var(--border);
  z-index: 1099; overflow-y: auto;
  transition: right 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: -8px 0 32px rgba(0,0,0,0.5);
}
.notepad-panel.open { right: 0; }

.notepad-loading {
  display: flex; align-items: center; justify-content: center;
  height: 100vh; font-family: var(--mono); font-size: 12px;
  color: var(--muted); letter-spacing: 1px;
}

/* Shift tab left when panel is open */
.notepad-tab.open { right: 420px; }

@media (max-width: 600px) {
  .notepad-panel { width: 100vw; right: -100vw; }
  .notepad-tab.open { right: 100vw; }
}
"""

# 4. JS toggle function — appended to script.js
NOTEPAD_JS = """
// ── NOTEPAD SLIDE TAB ────────────────────────────────────────────────────────
let _notepadMounted = false;

function toggleNotepad() {
  const panel = document.getElementById('notepad-panel');
  const tab   = document.getElementById('notepad-tab');
  const open  = panel.classList.toggle('open');
  tab.classList.toggle('open', open);

  if (open && !_notepadMounted) {
    _notepadMounted = true;
    // Load the JSX component via Babel standalone
    const script = document.createElement('script');
    script.type = 'text/babel';
    script.src  = 'notepad.jsx';
    script.setAttribute('data-presets', 'react');
    script.onload = () => {
      // notepad.jsx must call mountNotepad() or we mount via global
      if (window.__mountNotepad) window.__mountNotepad();
    };
    document.head.appendChild(script);
  }
}
"""

# ── Patch engine ─────────────────────────────────────────────────────────────
def patch_file(path, injections):
    if not os.path.exists(path):
        print(f"  ✗ NOT FOUND: {path}"); return False
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()
    changed = False
    for inj in injections:
        guard = inj['guard']
        if guard in src:
            print(f"  ✓ SKIP (already applied): {guard}"); continue
        anchor, content, mode = inj['anchor'], inj['content'], inj.get('mode','before')
        if anchor and anchor not in src:
            print(f"  ✗ ANCHOR MISSING: '{anchor}' in {path}"); continue
        if mode == 'before':
            src = src.replace(anchor, content + anchor, 1)
        elif mode == 'append':
            src = src + content
        print(f"  ✓ INJECTED: {guard}")
        changed = True
    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(src)
    return True

# ── notepad.jsx mount shim — append export→global bridge ─────────────────────
JSX_SHIM = """
// Mount bridge for Babel standalone loader
window.__mountNotepad = function() {
  const root = ReactDOM.createRoot(document.getElementById('notepad-root'));
  root.render(React.createElement(SharedNotepad));
};
// Auto-mount if panel already open
window.__mountNotepad();
"""

def patch_jsx(path):
    if not os.path.exists(path):
        print(f"  ✗ NOT FOUND: {path}"); return False
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()
    guard = '__mountNotepad'
    if guard in src:
        print(f"  ✓ SKIP (already applied): {guard} in {path}"); return True
    # Remove ES module export default → plain function for Babel UMD
    src = src.replace('export default function SharedNotepad', 'function SharedNotepad')
    # Remove ES import lines (React/useState etc. provided by CDN globals)
    lines = [l for l in src.splitlines() if not l.strip().startswith('import ')]
    src = '\n'.join(lines) + JSX_SHIM
    with open(path, 'w', encoding='utf-8') as f:
        f.write(src)
    print(f"  ✓ PATCHED: {path} (removed imports, added mount bridge)")
    return True

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("=== patch_notepad.py — Slide Tab Notepad ===\n")

    print("[index.html]")
    patch_file('index.html', [
        {'guard': 'NOTEPAD: React + Babel CDN', 'anchor': '</head>',     'content': HEAD_SCRIPTS, 'mode': 'before'},
        {'guard': 'NOTEPAD: slide tab',          'anchor': '</body>',     'content': BODY_HTML,    'mode': 'before'},
    ])

    print("\n[style.css]")
    patch_file('style.css', [
        {'guard': 'NOTEPAD SLIDE TAB', 'anchor': None, 'content': NOTEPAD_CSS, 'mode': 'append'},
    ])

    print("\n[script.js]")
    patch_file('script.js', [
        {'guard': 'NOTEPAD SLIDE TAB', 'anchor': None, 'content': NOTEPAD_JS, 'mode': 'append'},
    ])

    print("\n[notepad.jsx]")
    patch_jsx('notepad.jsx')

    print("\nDone. Deploy all 4 files to Netlify.")
