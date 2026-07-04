/**
 * script.js  —  CompTIA & Tech Reference  |  2026 Edition
 * =========================================================
 * toggleDomain / toggleTopic / filter / toggleAll
 * toggleTheme / updateThemeUI
 * initSnapQuote / initCloudStack / initTouchFeedback
 * URL codec helpers
 */

// ── STATE ──────────────────────────────────────────────────────────────────
let allExpanded = false;

const QUOTES = [
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

// ── ACCORDION ──────────────────────────────────────────────────────────────
function toggleDomain(h) {
  const b = h.nextElementSibling;
  const open = b.classList.toggle("open");
  h.classList.toggle("open", open);
}

function toggleTopic(h) {
  h.classList.toggle("open");
  h.nextElementSibling.classList.toggle("open");
}

// ── FILTER ─────────────────────────────────────────────────────────────────
function filter(domain, chip) {
  document.querySelectorAll(".chip").forEach(c => c.classList.remove("active"));
  chip.classList.add("active");
  document.querySelectorAll(".domain-section").forEach(s => {
    s.classList.toggle("hidden", domain !== "all" && s.dataset.domain !== domain);
  });
}

// ── EXPAND / COLLAPSE ALL ──────────────────────────────────────────────────
function toggleAll() {
  allExpanded = !allExpanded;
  document.querySelectorAll(".domain-header, .topic-header").forEach(h => h.classList.toggle("open", allExpanded));
  document.querySelectorAll(".domain-body, .topic-body").forEach(b => b.classList.toggle("open", allExpanded));
  const hdrBtn = document.getElementById("hdr-expand-btn");
  if (hdrBtn) {
    hdrBtn.title = allExpanded ? "Collapse all" : "Expand all";
    hdrBtn.setAttribute("aria-checked", allExpanded ? "true" : "false");
  }
}

// ── THEME ──────────────────────────────────────────────────────────────────
function toggleTheme() {
  const doc  = document.documentElement;
  const next = doc.getAttribute("data-theme") === "light" ? "dark" : "light";
  doc.setAttribute("data-theme", next);
  localStorage.setItem("theme", next);
  updateThemeUI(next);
}

function updateThemeUI(theme) {
  const btn = document.getElementById("hdr-theme-btn");
  if (btn) btn.setAttribute("aria-checked", theme === "light" ? "true" : "false");
}

// ── INIT THEME (prevent flash) ─────────────────────────────────────────────
(function () {
  const saved = localStorage.getItem("theme") || "dark";
  document.documentElement.setAttribute("data-theme", saved);
})();

// ── DOM READY ──────────────────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  updateThemeUI(document.documentElement.getAttribute("data-theme"));
  initSnapQuote();
  initCloudStack();
  initTouchFeedback();

  // Filter chips — event delegation on the filter bar
  document.querySelector(".filter-bar")?.addEventListener("click", e => {
    const chip = e.target.closest(".chip");
    if (chip) filter(chip.dataset.domain || "all", chip);
  });

  // Accordion — event delegation on the container
  document.getElementById("domain-container")?.addEventListener("click", e => {
    const dh = e.target.closest(".domain-header");
    if (dh) { toggleDomain(dh); return; }
    const th = e.target.closest(".topic-header");
    if (th) toggleTopic(th);
  });

  // Header control buttons
  document.getElementById("hdr-theme-btn")?.addEventListener("click", toggleTheme);
  document.getElementById("hdr-expand-btn")?.addEventListener("click", toggleAll);
});

// ── SNAP QUOTE ─────────────────────────────────────────────────────────────
function initSnapQuote() {
  const el  = document.getElementById("sq-text");
  const box = document.getElementById("snap-quote");
  if (!el || !box) return;

  let idx = Math.floor(Math.random() * QUOTES.length);

  const show = (i) => {
    box.classList.remove("visible");
    setTimeout(() => {
      el.textContent = QUOTES[i % QUOTES.length];
      box.classList.add("visible");
    }, 600);
  };

  show(idx);
  setInterval(() => show(++idx), 8000);
}

// ── CLOUD RESPONSIBILITY MATRIX ────────────────────────────────────────────
function initCloudStack() {
  const container = document.getElementById("cloud-stack");
  if (!container) return;

  const layers = ["Applications","Data","Runtime","Middleware","OS","Virtualization","Servers","Storage","Networking"];
  const resp   = [[1,1,1,0],[1,1,1,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]];

  layers.forEach((name, r) => {
    const row = document.createElement("div");
    row.className = "cloud-row";

    const lbl = document.createElement("div");
    lbl.className = "cloud-label";
    lbl.textContent = name;
    row.appendChild(lbl);

    resp[r].forEach((isCust, c) => {
      const cell = document.createElement("div");
      cell.className = `cloud-cell ${isCust ? `cloud-cell-c${c}` : "cloud-cell-provider"}`;
      cell.textContent = isCust ? "Customer" : "Provider";
      row.appendChild(cell);
    });
    container.appendChild(row);
  });
}

// ── TOUCH FEEDBACK ─────────────────────────────────────────────────────────
function initTouchFeedback() {
  document.querySelectorAll(".chip, .domain-header, .topic-header").forEach(el => {
    el.addEventListener("touchstart",  function() { this.classList.add("is-tapping");    }, { passive: true });
    el.addEventListener("touchend",    function() { this.classList.remove("is-tapping"); }, { passive: true });
    el.addEventListener("touchcancel", function() { this.classList.remove("is-tapping"); }, { passive: true });
  });
}

// ── URL CODEC WIDGET ───────────────────────────────────────────────────────
const _in  = () => document.getElementById("url-codec-input")?.value || "";
const _out = (v) => { const el = document.getElementById("url-codec-output"); if (el) el.value = v; };
const _msg = (txt, color = "var(--muted)") => {
  const el = document.getElementById("url-codec-msg");
  if (!el) return;
  el.textContent = txt;
  el.style.color = color;
  clearTimeout(el._t);
  el._t = setTimeout(() => el.textContent = "", 2500);
};

function urlToolEncode() {
  const raw = _in();
  if (!raw) return _msg("⚠ Nothing to encode.", "var(--amber)");
  try { _out(encodeURIComponent(raw)); _msg("✓ Encoded.", "var(--green)"); }
  catch (e) { _msg("✗ " + e.message, "var(--red)"); }
}

function urlToolDecode() {
  const raw = _in();
  if (!raw) return _msg("⚠ Nothing to decode.", "var(--amber)");
  try { _out(decodeURIComponent(raw.replace(/\+/g, " "))); _msg("✓ Decoded.", "var(--cyan)"); }
  catch (e) { _msg("✗ Malformed encoding.", "var(--red)"); }
}

function urlToolCopy() {
  const el = document.getElementById("url-codec-output");
  if (!el?.value) return _msg("⚠ Nothing to copy.", "var(--amber)");
  navigator.clipboard.writeText(el.value).then(() => _msg("✓ Copied.", "var(--green)"));
}

function urlToolClear() {
  const i = document.getElementById("url-codec-input");
  const o = document.getElementById("url-codec-output");
  if (i) i.value = "";
  if (o) o.value = "";
  _msg("");
}

// ─────────────────────────────────────────────────────────────────────────────
// SEARCH
// ─────────────────────────────────────────────────────────────────────────────

/** Nodes we injected <mark> highlights into during the current search. */
const _highlighted = new Set();

/** Lowercased textContent per topic, computed once (content never changes). */
const _topicTextCache = new WeakMap();
function topicSearchText(topic) {
  let t = _topicTextCache.get(topic);
  if (t === undefined) {
    t = topic.textContent.toLowerCase();
    _topicTextCache.set(topic, t);
  }
  return t;
}

/** Cached domain sections (built once on first search). */
let _domainSections = null;
function domainSections() {
  if (!_domainSections) _domainSections = [...document.querySelectorAll(".domain-section")];
  return _domainSections;
}

/** Remove all <mark class="sh"> wrappers, restoring the original text nodes. */
function clearHighlights() {
  _highlighted.forEach(el => {
    el.querySelectorAll("mark.sh").forEach(m => {
      m.replaceWith(document.createTextNode(m.textContent));
    });
    el.normalize(); // merge adjacent text nodes back together
  });
  _highlighted.clear();
}

/**
 * Wrap every occurrence of `term` inside `el` in <mark class="sh">.
 * Walks real text nodes only — never touches tags or attributes, so it
 * cannot corrupt the markup the way an innerHTML string-replace would.
 */
function highlightIn(el, term) {
  const termLower = term.toLowerCase();
  const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      return node.nodeValue.toLowerCase().includes(termLower)
        ? NodeFilter.FILTER_ACCEPT
        : NodeFilter.FILTER_REJECT;
    },
  });
  const targets = [];
  while (walker.nextNode()) targets.push(walker.currentNode);
  if (!targets.length) return;

  const escaped = term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const re = new RegExp(escaped, "gi");
  targets.forEach(node => {
    const text = node.nodeValue;
    const frag = document.createDocumentFragment();
    let last = 0, m;
    re.lastIndex = 0;
    while ((m = re.exec(text)) !== null) {
      if (m.index > last) frag.appendChild(document.createTextNode(text.slice(last, m.index)));
      const mark = document.createElement("mark");
      mark.className = "sh";
      mark.textContent = m[0];
      frag.appendChild(mark);
      last = m.index + m[0].length;
      if (m[0].length === 0) re.lastIndex++; // guard against zero-width matches
    }
    if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
    node.parentNode.replaceChild(frag, node);
  });
  _highlighted.add(el);
}

/**
 * Immediate search runner. Prefer the debounced onSearchInput() for keystrokes.
 * @param {string} raw - Current value of the search input.
 */
function runSearch(raw) {
  const term = raw.trim();
  const clearBtn = document.getElementById("search-clear");
  const countEl  = document.getElementById("search-count");

  if (clearBtn) clearBtn.classList.toggle("visible", term.length > 0);

  // Reset previous highlights and visibility
  clearHighlights();
  document.querySelectorAll(".topic.search-hidden, .domain-section.search-hidden")
    .forEach(el => el.classList.remove("search-hidden"));

  if (term.length < 2) {
    if (countEl) countEl.textContent = "";
    return;
  }

  const termLower = term.toLowerCase();
  let matchCount = 0;

  domainSections().forEach(domain => {
    let domainHasMatch = false;

    domain.querySelectorAll(".topic").forEach(topic => {
      if (topicSearchText(topic).includes(termLower)) {
        domainHasMatch = true;
        matchCount++;

        // Auto-expand the topic and its parent domain
        topic.querySelector(".topic-header")?.classList.add("open");
        topic.querySelector(".topic-body")?.classList.add("open");
        domain.querySelector(".domain-header")?.classList.add("open");
        domain.querySelector(".domain-body")?.classList.add("open");

        // Highlight only the text-bearing nodes of matched topics
        topic.querySelectorAll(
          ".topic-name, .concept-title, .concept-label, .concept-desc, .dw, .dt, .code-block"
        ).forEach(n => highlightIn(n, term));
      } else {
        topic.classList.add("search-hidden");
      }
    });

    if (!domainHasMatch) domain.classList.add("search-hidden");
  });

  if (countEl) countEl.textContent = matchCount ? `${matchCount} match${matchCount !== 1 ? "es" : ""}` : "no matches";
}

/** Debounced entry point wired to the search box's oninput. */
let _searchTimer = null;
function onSearchInput(raw) {
  // Toggle the clear button immediately for responsiveness
  const clearBtn = document.getElementById("search-clear");
  if (clearBtn) clearBtn.classList.toggle("visible", raw.trim().length > 0);
  clearTimeout(_searchTimer);
  _searchTimer = setTimeout(() => runSearch(raw), 180);
}

/** Backwards-compatible alias (older markup may call searchContent). */
function searchContent(raw) { onSearchInput(raw); }

/** Clear search input and reset view immediately. */
function clearSearch() {
  clearTimeout(_searchTimer);
  const input = document.getElementById("search-input");
  if (input) { input.value = ""; input.focus(); }
  runSearch("");
}

// ── NOTEPAD SLIDE TAB ────────────────────────────────────────────────────────
// Vanilla, dependency-free notepad backed by localStorage. Notes persist in the
// visitor's own browser and sync live across their open tabs via the `storage`
// event — no React, no Babel, no CDN, and it works over file://.

const NP_MAX_CHARS  = 500;
const NP_STORE_KEY  = "shared-notepad-notes";
const NP_SESSION_KEY = "notepad-session-id";
const NP_AUTHOR_KEY = "notepad-author";

let _notepadMounted = false;

function npSessionId() {
  let id = sessionStorage.getItem(NP_SESSION_KEY);
  if (!id) {
    id = Math.random().toString(36).slice(2, 10);
    sessionStorage.setItem(NP_SESSION_KEY, id);
  }
  return id;
}

function npLoad() {
  try {
    const raw = localStorage.getItem(NP_STORE_KEY);
    const arr = raw ? JSON.parse(raw) : [];
    return Array.isArray(arr) ? arr : [];
  } catch { return []; }
}

function npSave(notes) {
  try { localStorage.setItem(NP_STORE_KEY, JSON.stringify(notes)); }
  catch (e) { console.error("Notepad storage write failed", e); }
}

function npRelativeTime(ts) {
  const diff = Math.floor((Date.now() - ts) / 1000);
  if (diff < 5) return "just now";
  if (diff < 60) return `${diff}s ago`;
  if (diff < 3600) return `${Math.floor(diff / 60)}m ago`;
  if (diff < 86400) return `${Math.floor(diff / 3600)}h ago`;
  return new Date(ts).toLocaleDateString();
}

function toggleNotepad() {
  const panel = document.getElementById("notepad-panel");
  const tab   = document.getElementById("notepad-tab");
  const open  = panel.classList.toggle("open");
  tab.classList.toggle("open", open);
  if (open && !_notepadMounted) {
    _notepadMounted = true;
    mountNotepad(document.getElementById("notepad-root"));
  }
}

function mountNotepad(root) {
  const sessionId = npSessionId();
  let notes = npLoad();
  let sort = "newest";
  let filter = "";

  // Build the static skeleton with textContent-safe DOM (no innerHTML of data).
  root.textContent = "";
  root.insertAdjacentHTML("beforeend", `
    <div class="np-wrap">
      <div class="np-hdr">
        <span class="np-hdr-icon">📋</span>
        <div>
          <div class="np-hdr-title">Notepad</div>
          <div class="np-hdr-sub">Saved in this browser · synced across your tabs</div>
        </div>
      </div>
      <div class="np-compose">
        <div class="np-compose-top">
          <input class="np-name" type="text" placeholder="Your name (optional)" maxlength="30" />
          <span class="np-char">0/${NP_MAX_CHARS}</span>
        </div>
        <textarea class="np-input" rows="3" placeholder="Leave a note for yourself…"></textarea>
        <div class="np-compose-footer">
          <span class="np-hint"><kbd>Ctrl</kbd>+<kbd>Enter</kbd> to post</span>
          <button class="np-post" type="button" disabled>POST NOTE ▶</button>
        </div>
      </div>
      <div class="np-toolbar">
        <span class="np-count"></span>
        <input class="np-filter" type="text" placeholder="⌕ filter notes…" />
        <button class="np-sort active" type="button" data-sort="newest">NEWEST</button>
        <button class="np-sort" type="button" data-sort="oldest">OLDEST</button>
      </div>
      <div class="np-list"></div>
      <div class="np-toast"></div>
    </div>
  `);

  const nameEl   = root.querySelector(".np-name");
  const charEl   = root.querySelector(".np-char");
  const inputEl  = root.querySelector(".np-input");
  const postBtn  = root.querySelector(".np-post");
  const countEl  = root.querySelector(".np-count");
  const filterEl = root.querySelector(".np-filter");
  const listEl   = root.querySelector(".np-list");
  const toastEl  = root.querySelector(".np-toast");
  const sortBtns = [...root.querySelectorAll(".np-sort")];

  nameEl.value = localStorage.getItem(NP_AUTHOR_KEY) || "";

  let toastTimer = null;
  function showToast(msg) {
    toastEl.textContent = msg;
    toastEl.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toastEl.classList.remove("show"), 2200);
  }

  function updateCharCount() {
    const n = inputEl.value.length;
    charEl.textContent = `${n}/${NP_MAX_CHARS}`;
    charEl.classList.toggle("over", n > NP_MAX_CHARS);
    charEl.classList.toggle("warn", n > NP_MAX_CHARS * 0.85 && n <= NP_MAX_CHARS);
    postBtn.disabled = inputEl.value.trim().length === 0 || n > NP_MAX_CHARS;
  }

  function renderList() {
    const q = filter.toLowerCase();
    const shown = notes
      .filter(n => !q || n.body.toLowerCase().includes(q) || (n.author || "").toLowerCase().includes(q))
      .sort((a, b) => sort === "newest" ? b.ts - a.ts : a.ts - b.ts);

    countEl.textContent = `${notes.length} note${notes.length !== 1 ? "s" : ""}`;
    listEl.textContent = "";

    if (!shown.length) {
      const empty = document.createElement("div");
      empty.className = "np-empty";
      empty.textContent = filter
        ? "No notes match that filter."
        : "No notes yet — jot something down.";
      listEl.appendChild(empty);
      return;
    }

    shown.forEach(n => {
      const own = n.sessionId === sessionId;
      const card = document.createElement("div");
      card.className = "np-card" + (own ? " own" : "");

      const meta = document.createElement("div");
      meta.className = "np-meta";
      const author = document.createElement("span");
      author.className = "np-author";
      author.textContent = n.author || "Anonymous";
      const time = document.createElement("span");
      time.className = "np-time";
      time.textContent = npRelativeTime(n.ts);
      meta.append(author, time);
      if (own) {
        const badge = document.createElement("span");
        badge.className = "np-badge";
        badge.textContent = "YOU";
        const del = document.createElement("button");
        del.className = "np-del";
        del.type = "button";
        del.title = "Delete";
        del.textContent = "✕";
        del.addEventListener("click", () => deleteNote(n.id));
        meta.append(badge, del);
      }

      const bodyEl = document.createElement("div");
      bodyEl.className = "np-body";
      bodyEl.textContent = n.body; // textContent — never interprets note as HTML

      card.append(meta, bodyEl);
      listEl.appendChild(card);
    });
  }

  function postNote() {
    const body = inputEl.value.trim();
    const author = nameEl.value.trim() || "Anonymous";
    if (!body || body.length > NP_MAX_CHARS) return;
    if (nameEl.value.trim()) localStorage.setItem(NP_AUTHOR_KEY, nameEl.value.trim());

    notes = npLoad(); // re-read so we don't clobber a note from another tab
    notes.unshift({
      id: Math.random().toString(36).slice(2),
      author, body, ts: Date.now(), sessionId,
    });
    npSave(notes);
    inputEl.value = "";
    updateCharCount();
    renderList();
    showToast("✓ note posted");
  }

  function deleteNote(id) {
    notes = npLoad().filter(n => n.id !== id);
    npSave(notes);
    renderList();
    showToast("note removed");
  }

  // Wire events
  inputEl.addEventListener("input", updateCharCount);
  inputEl.addEventListener("keydown", e => {
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") { e.preventDefault(); postNote(); }
  });
  postBtn.addEventListener("click", postNote);
  filterEl.addEventListener("input", () => { filter = filterEl.value.trim(); renderList(); });
  sortBtns.forEach(btn => btn.addEventListener("click", () => {
    sort = btn.dataset.sort;
    sortBtns.forEach(b => b.classList.toggle("active", b === btn));
    renderList();
  }));

  // Live sync across the visitor's own tabs
  window.addEventListener("storage", e => {
    if (e.key === NP_STORE_KEY) { notes = npLoad(); renderList(); }
  });

  updateCharCount();
  renderList();
}
