#!/usr/bin/env python3
"""
Patch P3: Expand every disorder card with collapsible detail panels.
Injects:
  - CSS  : detail panel tabs + accordion within cards
  - JS   : DISORDER_DATA object + initDisorderDetails() auto-wiring
Requires P1 (and optionally P2) already applied.
Run: python3 patch_mental_disorders_p3.py [--dry-run]
"""
import sys, shutil, re
from pathlib import Path

FILES  = {'html': 'index.html', 'css': 'style.css', 'js': 'script.js'}
GUARD  = 'mental-disorders-p3'
CSS_SENTINEL = '/* end custom */'   # append before this or at EOF
JS_SENTINEL  = '// end domains'    # append before this or at EOF

# ─── CSS ─────────────────────────────────────────────────────────────────────
CSS = '''
/* ── Disorder Detail Panels (P3) ─────────────────────────── */
.disorder-expand-btn {
  display: inline-flex; align-items: center; gap: 4px;
  margin-top: 8px; padding: 3px 9px; border-radius: 4px;
  font-size: 0.72rem; font-weight: 600; letter-spacing: .04em;
  background: transparent; border: 1px solid var(--cyan);
  color: var(--cyan); cursor: pointer; transition: background .15s, color .15s;
}
.disorder-expand-btn:hover { background: var(--cyan); color: #000; }
.disorder-expand-btn.open  { background: var(--cyan); color: #000; }
.disorder-detail-panel {
  display: none; margin-top: 10px;
  border-top: 1px solid rgba(255,255,255,.08);
  padding-top: 8px;
}
.disorder-detail-panel.open { display: block; }
.detail-tabs {
  display: flex; gap: 4px; flex-wrap: wrap; margin-bottom: 8px;
}
.detail-tab {
  padding: 3px 10px; border-radius: 4px; font-size: 0.7rem; font-weight: 600;
  border: 1px solid rgba(255,255,255,.18); background: transparent;
  color: var(--text-muted); cursor: pointer; transition: all .15s;
}
.detail-tab:hover  { border-color: var(--cyan); color: var(--cyan); }
.detail-tab.active { background: var(--cyan); border-color: var(--cyan); color: #000; }
.detail-content {
  font-size: 0.78rem; line-height: 1.55; color: var(--text-muted);
  display: none;
}
.detail-content.active { display: block; }
/* light mode */
body.light .disorder-expand-btn        { border-color: var(--cyan); color: #0077aa; }
body.light .disorder-expand-btn:hover,
body.light .disorder-expand-btn.open   { background: var(--cyan); color: #fff; }
body.light .detail-tab                 { color: #555; border-color: #bbb; }
body.light .detail-tab:hover           { color: #0077aa; border-color: #0077aa; }
body.light .detail-tab.active          { background: var(--cyan); border-color: var(--cyan); color: #fff; }
body.light .detail-content             { color: #333; }
body.light .disorder-detail-panel      { border-top-color: rgba(0,0,0,.12); }
'''

# ─── JS ──────────────────────────────────────────────────────────────────────
# The DISORDER_DATA will be read from file to keep this script manageable
DISORDER_DATA_PATH = 'disorder_data.js'

JS_INIT = '''
// ── Disorder Detail Panels (P3) ──────────────────────────────
(function initDisorderDetails() {
  const TAB_LABELS = { c: 'Criteria', p: 'Prevalence', r: 'Risk Factors', d: 'Differential' };

  function buildPanel(label) {
    const entry = DISORDER_DATA[label];
    if (!entry) return null;

    const tabs  = Object.keys(entry).filter(k => TAB_LABELS[k]);
    if (!tabs.length) return null;

    // expand button
    const btn = document.createElement('button');
    btn.className = 'disorder-expand-btn';
    btn.textContent = '▸ Details';

    // panel
    const panel = document.createElement('div');
    panel.className = 'disorder-detail-panel';

    // tab bar
    const tabBar = document.createElement('div');
    tabBar.className = 'detail-tabs';

    // content area
    const contentWrap = document.createElement('div');

    tabs.forEach((k, i) => {
      const tab = document.createElement('button');
      tab.className = 'detail-tab' + (i === 0 ? ' active' : '');
      tab.textContent = TAB_LABELS[k];
      tab.dataset.key = k;

      const content = document.createElement('div');
      content.className = 'detail-content' + (i === 0 ? ' active' : '');
      content.textContent = entry[k];
      content.dataset.key = k;

      tab.addEventListener('click', () => {
        tabBar.querySelectorAll('.detail-tab').forEach(t => t.classList.remove('active'));
        contentWrap.querySelectorAll('.detail-content').forEach(c => c.classList.remove('active'));
        tab.classList.add('active');
        content.classList.add('active');
      });

      tabBar.appendChild(tab);
      contentWrap.appendChild(content);
    });

    panel.appendChild(tabBar);
    panel.appendChild(contentWrap);

    btn.addEventListener('click', () => {
      const open = panel.classList.toggle('open');
      btn.classList.toggle('open', open);
      btn.textContent = open ? '▾ Details' : '▸ Details';
    });

    return { btn, panel };
  }

  document.querySelectorAll('[data-domain="mental-disorders"] .concept-card').forEach(card => {
    const labelEl = card.querySelector('.concept-label');
    if (!labelEl) return;
    const label = labelEl.textContent.trim();
    const built = buildPanel(label);
    if (!built) return;
    card.appendChild(built.btn);
    card.appendChild(built.panel);
  });
})();
'''

def read(p):    return Path(p).read_text(encoding='utf-8')
def write(p,t): Path(p).write_text(t, encoding='utf-8')

def patch_html(src): return src, True, 'no HTML changes needed'

def patch_css(src):
    if GUARD in src: return src, False, 'already patched'
    block = f'\n/* {GUARD} */\n' + CSS
    if CSS_SENTINEL in src:
        src = src.replace(CSS_SENTINEL, block + '\n' + CSS_SENTINEL, 1)
    else:
        src += block
    return src, True, 'ok'

def patch_js(src):
    if GUARD in src: return src, False, 'already patched'
    try:
        disorder_js = Path(DISORDER_DATA_PATH).read_text()
    except FileNotFoundError:
        return src, False, f'{DISORDER_DATA_PATH} not found — run extractor first'
    block = f'\n// {GUARD}\n' + disorder_js + '\n' + JS_INIT
    if JS_SENTINEL in src:
        src = src.replace(JS_SENTINEL, block + '\n' + JS_SENTINEL, 1)
    else:
        src += block
    return src, True, f'injected {len(disorder_js):,} chars of disorder data + init'

patches = [
    (FILES['html'], patch_html),
    (FILES['css'],  patch_css),
    (FILES['js'],   patch_js),
]

dry = '--dry-run' in sys.argv
errors = []

for fname, fn in patches:
    try:
        orig = read(fname)
        patched, changed, msg = fn(orig)
        print(f'[{"CHANGED" if changed else "SKIP"}] {fname}: {msg}')
        if changed and not dry:
            shutil.copy(fname, fname + '.bak3')
            write(fname, patched)
            print(f'       wrote {fname} (backup: {fname}.bak3)')
    except FileNotFoundError:
        errors.append(fname)
        print(f'[ERROR] {fname}: file not found')
    except Exception as e:
        errors.append(str(e))
        print(f'[ERROR] {fname}: {e}')

if dry:  print('\n-- dry run, no files written --')
if errors: sys.exit(1)
