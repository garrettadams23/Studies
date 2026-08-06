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
  h.setAttribute("aria-expanded", open ? "true" : "false");
}

function toggleTopic(h) {
  const open = h.classList.toggle("open");
  h.nextElementSibling.classList.toggle("open", open);
  h.setAttribute("aria-expanded", open ? "true" : "false");
  if (open) updateTopicHash(h.parentElement);
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
  document.querySelectorAll(".domain-header, .topic-header").forEach(h => {
    h.classList.toggle("open", allExpanded);
    if (h.hasAttribute("aria-expanded")) h.setAttribute("aria-expanded", allExpanded ? "true" : "false");
  });
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
  const container = document.getElementById("domain-container");
  container?.addEventListener("click", e => {
    // Per-topic tool buttons take precedence over the toggle
    const tool = e.target.closest(".topic-review, .topic-permalink, .topic-bookmark");
    if (tool) { e.stopPropagation(); handleTopicTool(tool); return; }
    const dh = e.target.closest(".domain-header");
    if (dh) { toggleDomain(dh); return; }
    const th = e.target.closest(".topic-header");
    if (th) toggleTopic(th);
  });

  // Accordion — keyboard support (Enter / Space on focused headers)
  container?.addEventListener("keydown", e => {
    if (e.key !== "Enter" && e.key !== " ") return;
    const header = e.target.closest(".domain-header, .topic-header");
    if (!header || e.target.closest(".topic-review, .topic-permalink")) return;
    e.preventDefault();
    header.classList.contains("domain-header") ? toggleDomain(header) : toggleTopic(header);
  });

  // Header control buttons
  document.getElementById("hdr-theme-btn")?.addEventListener("click", toggleTheme);
  document.getElementById("hdr-expand-btn")?.addEventListener("click", toggleAll);
  document.getElementById("hdr-random-btn")?.addEventListener("click", jumpToRandomTopic);

  // Search + notepad + URL codec — wired here (not inline) so the CSP can stay
  // script-src 'self' with no 'unsafe-inline'.
  document.getElementById("search-input")?.addEventListener("input", e => onSearchInput(e.target.value));
  document.getElementById("search-clear")?.addEventListener("click", clearSearch);
  document.getElementById("notepad-tab")?.addEventListener("click", toggleNotepad);
  document.querySelector(".url-codec-btn.btn-encode")?.addEventListener("click", urlToolEncode);
  document.querySelector(".url-codec-btn.btn-decode")?.addEventListener("click", urlToolDecode);
  document.querySelector(".url-codec-btn.btn-copy")?.addEventListener("click", urlToolCopy);
  document.querySelector(".url-codec-btn.btn-clear")?.addEventListener("click", urlToolClear);

  // Global keyboard shortcuts (ignored while typing in a field)
  document.addEventListener("keydown", handleGlobalKeys);

  initAccessibilityAndTools();
  initBackToTop();
  initStudyTools();
});

// ── RANDOM TOPIC ─────────────────────────────────────────────────────────────
// Open a random topic (and its domain), update the hash, and scroll to it.
function jumpToRandomTopic() {
  const topics = document.querySelectorAll(".topic[id]");
  if (!topics.length) return;
  const topic = topics[Math.floor(Math.random() * topics.length)];
  // Clear any active filter/search so the pick is guaranteed visible
  if (typeof clearSearch === "function") {
    const si = document.getElementById("search-input");
    if (si && si.value) clearSearch();
  }
  location.hash = topic.id;   // openHashTarget (hashchange) expands + scrolls
  openHashTarget();
}

// ── GLOBAL KEYBOARD SHORTCUTS ────────────────────────────────────────────────
// "/" focus search · "e" expand/collapse all · "t" toggle theme · "r" random ·
// Esc clears the search. Ignored while typing in a field (Esc still clears search).
function handleGlobalKeys(e) {
  if (e.ctrlKey || e.metaKey || e.altKey) return;
  // While a study-tools modal is open, let it own the keyboard.
  if (typeof _stOverlay !== "undefined" && _stOverlay && !_stOverlay.hidden) return;
  const t = e.target;
  const typing = t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA" ||
    t.tagName === "SELECT" || t.isContentEditable);

  if (e.key === "Escape") {
    const si = document.getElementById("search-input");
    if (si && si.value) { clearSearch(); si.blur(); e.preventDefault(); }
    else if (typing && t.blur) t.blur();
    return;
  }
  if (typing) return;

  switch (e.key) {
    case "/":
      { const si = document.getElementById("search-input");
        if (si) { e.preventDefault(); si.focus(); si.select?.(); } }
      break;
    case "e": case "E": e.preventDefault(); toggleAll(); break;
    case "t": case "T": e.preventDefault(); toggleTheme(); break;
    case "r": case "R": e.preventDefault(); jumpToRandomTopic(); break;
    default: break;
  }
}

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

// ── ACCESSIBILITY, PERMALINKS & PROGRESS ───────────────────────────────────
const REVIEWED_PREFIX = "reviewed:";

/**
 * Text of an element with the inline acronym expansions removed.
 *
 * tools/annotate_acronyms.py injects `<span class="acro-exp">(…)</span>` beside
 * the first use of an acronym, including inside `.topic-name`. Deep-link slugs
 * and the study-list index are derived from that text, so they have to see the
 * title as it was written — otherwise every annotated topic's permalink would
 * change and stored bookmarks would break.
 */
function labelText(el) {
  if (!el) return "";
  let node = el;
  if (el.querySelector(".acro-exp")) {
    node = el.cloneNode(true);
    node.querySelectorAll(".acro-exp").forEach(n => n.remove());
  }
  return node.textContent.replace(/\s+/g, " ");
}

function slugify(s) {
  return s.toLowerCase()
    .replace(/[^\w\s-]/g, "")
    .trim()
    .replace(/[\s_]+/g, "-")
    .replace(/-+/g, "-")
    .slice(0, 60) || "topic";
}

/**
 * One pass over the DOM to make the accordion accessible and add per-topic
 * permalink + "mark reviewed" tools. Runs once at load.
 */
function initAccessibilityAndTools() {
  // Make every accordion header focusable and announce its state
  document.querySelectorAll(".domain-header, .topic-header").forEach(h => {
    h.setAttribute("tabindex", "0");
    h.setAttribute("role", "button");
    h.setAttribute("aria-expanded", h.classList.contains("open") ? "true" : "false");
  });

  const usedIds = new Set();
  document.querySelectorAll(".domain-section").forEach(domain => {
    domain.querySelectorAll(".topic").forEach(topic => {
      const header = topic.querySelector(":scope > .topic-header");
      if (!header) return;
      const nameEl = header.querySelector(".topic-name");
      // Older "Beginner" topics carry the title as a bare text node in the
      // header (no .topic-name); fall back to the header's own text.
      const label = labelText(nameEl || header).trim();

      // Stable, unique slug id for deep-linking
      if (!topic.id) {
        let base = slugify(label), id = base, i = 2;
        while (usedIds.has(id)) id = `${base}-${i++}`;
        usedIds.add(id);
        topic.id = id;
      }

      // Reflect stored "reviewed" state
      if (localStorage.getItem(REVIEWED_PREFIX + topic.id) === "1") {
        topic.classList.add("reviewed");
      }
      // Reflect stored "bookmarked" state
      if (localStorage.getItem(BOOKMARK_PREFIX + topic.id) === "1") {
        topic.classList.add("bookmarked");
      }

      // Inject the tool cluster (bookmark + reviewed toggle + permalink) once
      if (!header.querySelector(".topic-tools")) {
        const tools = document.createElement("span");
        tools.className = "topic-tools";

        const bookmark = document.createElement("button");
        bookmark.type = "button";
        bookmark.className = "topic-bookmark";
        bookmark.title = "Save to study list";
        bookmark.setAttribute("aria-label", "Save topic to study list");
        bookmark.textContent = "★";

        const review = document.createElement("button");
        review.type = "button";
        review.className = "topic-review";
        review.title = "Mark topic as reviewed";
        review.setAttribute("aria-label", "Mark topic as reviewed");
        review.textContent = "✓";

        const link = document.createElement("button");
        link.type = "button";
        link.className = "topic-permalink";
        link.title = "Copy link to this topic";
        link.setAttribute("aria-label", "Copy link to this topic");
        link.textContent = "🔗";

        tools.append(bookmark, review, link);
        // Insert before the chevron so it stays right-aligned
        const chev = header.querySelector(".topic-chev");
        chev ? header.insertBefore(tools, chev) : header.appendChild(tools);
      }
    });
    updateDomainProgress(domain);
  });

  // Deep-link: open + scroll to a topic referenced in the URL hash
  openHashTarget();
  window.addEventListener("hashchange", openHashTarget);
}

function handleTopicTool(btn) {
  const topic = btn.closest(".topic");
  if (!topic) return;
  if (btn.classList.contains("topic-bookmark")) {
    const on = topic.classList.toggle("bookmarked");
    const key = BOOKMARK_PREFIX + topic.id;
    on ? localStorage.setItem(key, "1") : localStorage.removeItem(key);
    if (typeof stRefreshStudyList === "function") stRefreshStudyList();
  } else if (btn.classList.contains("topic-review")) {
    const on = topic.classList.toggle("reviewed");
    const key = REVIEWED_PREFIX + topic.id;
    on ? localStorage.setItem(key, "1") : localStorage.removeItem(key);
    updateDomainProgress(topic.closest(".domain-section"));
  } else if (btn.classList.contains("topic-permalink")) {
    const url = `${location.origin}${location.pathname}#${topic.id}`;
    const done = () => { btn.classList.add("copied"); setTimeout(() => btn.classList.remove("copied"), 1200); };
    if (navigator.clipboard?.writeText) {
      navigator.clipboard.writeText(url).then(done).catch(() => { location.hash = topic.id; });
    } else {
      location.hash = topic.id; done();
    }
  }
}

/** Update the "n/m reviewed" badge on a domain header. */
function updateDomainProgress(domain) {
  if (!domain) return;
  const header = domain.querySelector(".domain-header");
  if (!header) return;
  const topics = domain.querySelectorAll(".topic");
  const done = domain.querySelectorAll(".topic.reviewed").length;
  let badge = header.querySelector(".domain-progress");
  if (!badge) {
    badge = document.createElement("span");
    badge.className = "domain-progress";
    const chev = header.querySelector(".chevron");
    chev ? header.insertBefore(badge, chev) : header.appendChild(badge);
  }
  badge.textContent = `${done}/${topics.length}`;
  badge.classList.toggle("complete", done === topics.length && topics.length > 0);
}

/** Reflect the currently-open topic in the URL without a scroll jump. */
function updateTopicHash(topic) {
  if (topic?.id) history.replaceState(null, "", `#${topic.id}`);
}

/** Expand and scroll to the topic named in location.hash, if any. */
function openHashTarget() {
  const id = decodeURIComponent(location.hash.slice(1));
  if (!id) return;
  const topic = document.getElementById(id);
  if (!topic || !topic.classList.contains("topic")) return;
  const domain = topic.closest(".domain-section");
  domain?.querySelector(".domain-header")?.classList.add("open");
  domain?.querySelector(".domain-body")?.classList.add("open");
  domain?.querySelector(".domain-header")?.setAttribute("aria-expanded", "true");
  const th = topic.querySelector(".topic-header");
  th?.classList.add("open");
  th?.setAttribute("aria-expanded", "true");
  topic.querySelector(".topic-body")?.classList.add("open");
  topic.scrollIntoView({ behavior: "smooth", block: "start" });
}

// ── BACK TO TOP ─────────────────────────────────────────────────────────────
function initBackToTop() {
  const btn = document.createElement("button");
  btn.id = "back-to-top";
  btn.type = "button";
  btn.title = "Back to top";
  btn.setAttribute("aria-label", "Back to top");
  btn.textContent = "↑";
  btn.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
  document.body.appendChild(btn);

  let ticking = false;
  window.addEventListener("scroll", () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      btn.classList.toggle("visible", window.scrollY > window.innerHeight * 1.5);
      ticking = false;
    });
  }, { passive: true });
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


// ═══════════════════════════════════════════════════════════════════════════
// STUDY TOOLS — bookmarks / study list, quick-jump palette, flashcards, quiz.
// All vanilla JS, state in localStorage. UI is injected at runtime (no build
// dependency beyond the CSS in style.css).
// ═══════════════════════════════════════════════════════════════════════════

const BOOKMARK_PREFIX = "bookmark:";
const KNOWN_PREFIX = "known:";
const SRS_PREFIX = "srs:";

// ── SPACED REPETITION ───────────────────────────────────────────────────────
// A reduced SM-2 over the topics the flashcards already know about. One record
// per topic: e = ease, i = interval in days, d = due date, n = repetition
// count. A topic with no record is simply new — nothing to migrate.

/** Local YYYY-MM-DD. Not toISOString(), which would shift the day by timezone. */
function srsToday(offsetDays = 0) {
  const d = new Date();
  d.setDate(d.getDate() + offsetDays);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
}

function srsGet(id) {
  try {
    const raw = localStorage.getItem(SRS_PREFIX + id);
    if (!raw) return null;
    const r = JSON.parse(raw);
    return (typeof r === "object" && r) ? r : null;
  } catch { return null; }        // a corrupt record is treated as "new"
}

function srsIsDue(id) {
  const r = srsGet(id);
  return !r || r.d <= srsToday();
}

/** How many topics are waiting today — drives the badge on the study button. */
function srsDueCount() {
  let due = 0;
  for (let i = 0; i < localStorage.length; i++) {
    const k = localStorage.key(i);
    if (!k || !k.startsWith(SRS_PREFIX)) continue;
    const r = srsGet(k.slice(SRS_PREFIX.length));
    if (r && r.d <= srsToday()) due++;
  }
  return due;
}

/**
 * Grade a card and schedule the next sight of it.
 *   again → back to day 1, ease down       hard → small step, ease down
 *   good  → 1, 6, then interval x ease     easy → a longer step, ease up
 * Ease is floored at 1.3, as in SM-2, or a card you keep failing collapses to
 * being shown every session forever.
 */
function srsGrade(id, grade) {
  const r = srsGet(id) || { e: 2.5, i: 1, n: 0 };
  let { e, i, n } = r;
  if (grade === "again")      { n = 0; i = 1;                          e = Math.max(1.3, e - 0.20); }
  else if (grade === "hard")  { n += 1; i = Math.max(1, Math.round(i * 1.2)); e = Math.max(1.3, e - 0.15); }
  else if (grade === "good")  { n += 1; i = n === 1 ? 1 : n === 2 ? 6 : Math.round(i * e); }
  else                        { n += 1; i = Math.max(4, Math.round(i * e * 1.3)); e = e + 0.15; }
  const rec = { e: Math.round(e * 100) / 100, i, d: srsToday(i), n };
  try { localStorage.setItem(SRS_PREFIX + id, JSON.stringify(rec)); } catch { /* quota */ }
  if (grade !== "again") localStorage.setItem(KNOWN_PREFIX + id, "1");
  srsUpdateBadge();
  return rec;
}

/** Reflect the due count on the study launcher, or clear it when zero. */
function srsUpdateBadge() {
  const btn = document.getElementById("study-fab");
  if (!btn) return;
  const n = srsDueCount();
  let b = btn.querySelector(".study-badge");
  if (!n) { b?.remove(); btn.removeAttribute("data-due"); return; }
  if (!b) {
    b = document.createElement("span");
    b.className = "study-badge";
    btn.appendChild(b);
  }
  b.textContent = n > 99 ? "99+" : String(n);
  btn.setAttribute("data-due", String(n));
  btn.setAttribute("aria-label", `Study tools — ${n} card${n === 1 ? "" : "s"} due`);
}
let _stIndex = null;

/** Build a flat index of every topic on the page (once). */
function stIndex() {
  if (_stIndex) return _stIndex;
  _stIndex = [];
  document.querySelectorAll(".domain-section").forEach(domain => {
    const domainId = domain.dataset.domain || "";
    const domainTitle = (domain.querySelector(".domain-title")?.textContent || "").trim();
    const domainIcon = (domain.querySelector(".domain-icon")?.textContent || "").trim();
    domain.querySelectorAll(".topic").forEach(t => {
      const name = labelText(t.querySelector(".topic-name")
        || t.querySelector(".topic-header")).trim();
      const title = (t.querySelector(".concept-title")?.textContent || "").trim();
      const desc = (t.querySelector(".concept-desc")?.textContent || "").trim();
      const badge = (t.querySelector(".topic-badge")?.textContent || "").trim();
      if (t.id && name) _stIndex.push({ id: t.id, name, title, desc, badge, domainId, domainTitle, domainIcon, el: t });
    });
  });
  return _stIndex;
}

function stIsBookmarked(id) { return localStorage.getItem(BOOKMARK_PREFIX + id) === "1"; }

/** Reveal + scroll to a topic by id (reuses the deep-link opener). */
function stGoToTopic(id) {
  location.hash = id;      // triggers openHashTarget via hashchange
  openHashTarget();
}

// ── Shared modal shell ──────────────────────────────────────────────────────
let _stOverlay = null;
function stModal() {
  if (_stOverlay) return _stOverlay;
  const ov = document.createElement("div");
  ov.id = "st-overlay";
  ov.hidden = true;
  ov.innerHTML =
    '<div id="st-modal" role="dialog" aria-modal="true" aria-label="Study tools">' +
    '<button id="st-close" title="Close (Esc)" aria-label="Close">✕</button>' +
    '<div id="st-body"></div></div>';
  ov.addEventListener("click", e => { if (e.target === ov) stClose(); });
  ov.querySelector("#st-close").addEventListener("click", stClose);
  document.body.appendChild(ov);
  _stOverlay = ov;
  return ov;
}
function stOpen(renderFn) {
  const ov = stModal();
  ov.hidden = false;
  document.body.classList.add("st-lock");
  renderFn(ov.querySelector("#st-body"));
}
function stClose() {
  if (_stOverlay) _stOverlay.hidden = true;
  document.body.classList.remove("st-lock");
  _stQuizState = null;
  _stCardState = null;
}

function esc(s) { return (s || "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])); }

// ── Scope selector (All / a domain / Bookmarks) ─────────────────────────────
function stScopeOptions() {
  const doms = [];
  const seen = new Set();
  stIndex().forEach(t => {
    if (!seen.has(t.domainId)) { seen.add(t.domainId); doms.push({ id: t.domainId, title: t.domainTitle, icon: t.domainIcon }); }
  });
  return doms;
}
function stTopicsForScope(scope) {
  const all = stIndex();
  if (scope === "__all") return all.slice();
  if (scope === "__bookmarks") return all.filter(t => stIsBookmarked(t.id));
  if (scope === "__due") return all.filter(t => srsGet(t.id) && srsIsDue(t.id));
  return all.filter(t => t.domainId === scope);
}
function stScopeSelectHTML(id) {
  const dueN = srsDueCount();
  const opts = ['<option value="__all">◈ All domains</option>',
    '<option value="__bookmarks">★ My study list</option>',
    `<option value="__due">⏰ Due today${dueN ? ` (${dueN})` : ""}</option>`]
    .concat(stScopeOptions().map(d => `<option value="${esc(d.id)}">${esc(d.icon)} ${esc(d.domainTitle)}</option>`));
  return `<select id="${id}" class="st-select">${opts.join("")}</select>`;
}

function shuffle(a) {
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}

// ── QUICK-JUMP PALETTE ──────────────────────────────────────────────────────
function stOpenJump() {
  stOpen(body => {
    body.innerHTML =
      '<h2 class="st-h">Quick jump</h2>' +
      '<input id="st-jump-input" class="st-input" type="search" placeholder="Type a topic or domain…" autocomplete="off" />' +
      '<ul id="st-jump-list" class="st-jump-list"></ul>' +
      '<p class="st-hint">↑ ↓ to move · Enter to jump · Esc to close</p>';
    const input = body.querySelector("#st-jump-input");
    const list = body.querySelector("#st-jump-list");
    let items = [], active = 0;

    function render(q) {
      const query = q.trim().toLowerCase();
      const idx = stIndex();
      items = (query
        ? idx.filter(t => (t.name + " " + t.domainTitle + " " + t.title).toLowerCase().includes(query))
        : idx).slice(0, 60);
      active = 0;
      list.innerHTML = items.map((t, i) =>
        `<li class="st-jump-item${i === 0 ? " active" : ""}" data-i="${i}">` +
        `<span class="st-jump-name">${esc(t.name)}</span>` +
        `<span class="st-jump-dom">${esc(t.domainIcon)} ${esc(t.domainTitle)}</span></li>`).join("")
        || '<li class="st-jump-empty">No matches</li>';
    }
    function move(d) {
      if (!items.length) return;
      active = (active + d + items.length) % items.length;
      list.querySelectorAll(".st-jump-item").forEach((el, i) => el.classList.toggle("active", i === active));
      list.querySelector(".st-jump-item.active")?.scrollIntoView({ block: "nearest" });
    }
    function choose() { const t = items[active]; if (t) { stClose(); stGoToTopic(t.id); } }

    input.addEventListener("input", () => render(input.value));
    input.addEventListener("keydown", e => {
      if (e.key === "ArrowDown") { e.preventDefault(); move(1); }
      else if (e.key === "ArrowUp") { e.preventDefault(); move(-1); }
      else if (e.key === "Enter") { e.preventDefault(); choose(); }
    });
    list.addEventListener("click", e => {
      const li = e.target.closest(".st-jump-item"); if (!li) return;
      active = +li.dataset.i; choose();
    });
    render("");
    setTimeout(() => input.focus(), 30);
  });
}

// ── FLASHCARDS ──────────────────────────────────────────────────────────────
let _stCardState = null;
function stOpenFlashcards(initialScope) {
  stOpen(body => {
    const due = srsDueCount();
    body.innerHTML =
      '<h2 class="st-h">Flashcards</h2>' +
      '<div class="st-toolbar"><label class="st-lbl">Deck</label>' + stScopeSelectHTML("st-fc-scope") +
      '<button id="st-fc-start" class="st-btn st-btn-primary">Start</button></div>' +
      (due ? `<p class="st-hint">⏰ ${due} card${due === 1 ? "" : "s"} due for review today.</p>` : "") +
      '<div id="st-fc-stage"></div>';
    const scope = body.querySelector("#st-fc-scope");
    if (initialScope) scope.value = initialScope;
    body.querySelector("#st-fc-start").addEventListener("click", () => stStartFlashcards(scope.value, body.querySelector("#st-fc-stage")));
    stStartFlashcards(scope.value, body.querySelector("#st-fc-stage"));
  });
}

/** Flashcards, opened straight onto the cards the scheduler says are due. */
function stOpenDue() { stOpenFlashcards("__due"); }
function stStartFlashcards(scope, stage) {
  let deck = shuffle(stTopicsForScope(scope));
  if (!deck.length) {
    stage.innerHTML = scope === "__due"
      ? '<p class="st-empty">Nothing due. Grade some cards from another deck and they will come back here on a schedule.</p>'
      : '<p class="st-empty">No cards in this deck. Star some topics with ★, or pick another deck.</p>';
    return;
  }
  _stCardState = { deck, i: 0, flipped: false, total: deck.length, done: 0 };
  stRenderCard(stage);
}
/** One grade button, captioned with the interval that choice would schedule. */
function stGradeBtn(grade, label, id) {
  const r = srsGet(id) || { e: 2.5, i: 1, n: 0 };
  let days;
  if (grade === "again") days = 1;
  else if (grade === "hard") days = Math.max(1, Math.round(r.i * 1.2));
  else if (grade === "good") days = r.n === 0 ? 1 : r.n === 1 ? 6 : Math.round(r.i * r.e);
  else days = Math.max(4, Math.round(r.i * r.e * 1.3));
  const when = days === 1 ? "1d" : days < 30 ? days + "d" : Math.round(days / 30) + "mo";
  return `<button class="st-btn st-grade st-grade-${grade}" data-grade="${grade}">` +
         `${label}<span class="st-grade-when">${when}</span></button>`;
}

function stRenderCard(stage) {
  const s = _stCardState; if (!s) return;
  if (s.i >= s.deck.length) {
    stage.innerHTML = `<div class="st-result"><div class="st-result-big">✅</div><p>Deck complete — ${s.total} card${s.total === 1 ? "" : "s"} reviewed.</p>` +
      '<button id="st-fc-again" class="st-btn st-btn-primary">Shuffle &amp; repeat</button></div>';
    stage.querySelector("#st-fc-again").addEventListener("click", () => { s.deck = shuffle(s.deck); s.i = 0; s.done = 0; stRenderCard(stage); });
    return;
  }
  const t = s.deck[s.i];
  stage.innerHTML =
    `<div class="st-progress">Card ${s.i + 1} / ${s.deck.length}</div>` +
    `<div class="st-card${s.flipped ? " flipped" : ""}" id="st-card" tabindex="0" role="button" aria-label="Flip card">` +
      `<div class="st-card-face st-card-front"><span class="st-card-dom">${esc(t.domainIcon)} ${esc(t.domainTitle)}</span>` +
        `<span class="st-card-q">${esc(t.name)}</span><span class="st-card-tap">Tap or press Space to flip</span></div>` +
      `<div class="st-card-face st-card-back"><span class="st-card-title">${esc(t.title || t.name)}</span>` +
        `<span class="st-card-desc">${esc(t.desc || "(open the topic for details)")}</span></div>` +
    `</div>` +
    (s.flipped
      ? '<div class="st-card-actions st-grades">' +
        stGradeBtn("again", "↻ Again", t.id) + stGradeBtn("hard", "Hard", t.id) +
        stGradeBtn("good", "Good", t.id) + stGradeBtn("easy", "Easy", t.id) +
        '<button id="st-open" class="st-btn">Open topic ↗</button></div>'
      : '<div class="st-card-actions"><button id="st-flip" class="st-btn st-btn-primary">Flip</button></div>');

  const card = stage.querySelector("#st-card");
  const flip = () => { s.flipped = !s.flipped; stRenderCard(stage); };
  card.addEventListener("click", flip);
  card.addEventListener("keydown", e => { if (e.key === " " || e.key === "Enter") { e.preventDefault(); flip(); } });
  stage.querySelector("#st-flip")?.addEventListener("click", flip);
  stage.querySelectorAll(".st-grade").forEach(b => b.addEventListener("click", () => {
    srsGrade(t.id, b.dataset.grade);
    // "Again" also puts the card back in this session's deck — a card you just
    // failed should come round again now, not only tomorrow.
    if (b.dataset.grade === "again") s.deck.push(t); else s.done++;
    s.flipped = false; s.i++; stRenderCard(stage);
  }));
  stage.querySelector("#st-open")?.addEventListener("click", () => { stClose(); stGoToTopic(t.id); });
  setTimeout(() => card.focus(), 20);
}

// ── QUIZ (multiple choice, auto-generated) ──────────────────────────────────
let _stQuizState = null;
function stOpenQuiz() {
  stOpen(body => {
    body.innerHTML =
      '<h2 class="st-h">Quiz</h2>' +
      '<div class="st-toolbar"><label class="st-lbl">From</label>' + stScopeSelectHTML("st-qz-scope") +
      '<button id="st-qz-start" class="st-btn st-btn-primary">Start</button></div>' +
      '<div id="st-qz-stage"></div>';
    const scope = body.querySelector("#st-qz-scope");
    body.querySelector("#st-qz-start").addEventListener("click", () => stStartQuiz(scope.value, body.querySelector("#st-qz-stage")));
    stStartQuiz(scope.value, body.querySelector("#st-qz-stage"));
  });
}
function stStartQuiz(scope, stage) {
  const pool = stTopicsForScope(scope).filter(t => t.title || t.desc);
  if (pool.length < 4) { stage.innerHTML = '<p class="st-empty">Need at least 4 topics with descriptions to build a quiz. Pick a broader scope.</p>'; return; }
  const questions = shuffle(pool.slice()).slice(0, Math.min(10, pool.length));
  _stQuizState = { pool, questions, i: 0, score: 0, answered: false };
  stRenderQuestion(stage);
}
function stRenderQuestion(stage) {
  const s = _stQuizState; if (!s) return;
  if (s.i >= s.questions.length) {
    const pct = Math.round((s.score / s.questions.length) * 100);
    stage.innerHTML = `<div class="st-result"><div class="st-result-big">${pct >= 80 ? "🏆" : pct >= 50 ? "👍" : "📚"}</div>` +
      `<p>Score: <strong>${s.score} / ${s.questions.length}</strong> (${pct}%)</p>` +
      '<button id="st-qz-retry" class="st-btn st-btn-primary">New quiz</button></div>';
    stage.querySelector("#st-qz-retry").addEventListener("click", () => stRestartQuizSame(stage));
    return;
  }
  const q = s.questions[s.i];
  const prompt = q.title || q.desc.slice(0, 160);
  const distractors = shuffle(s.pool.filter(t => t.id !== q.id)).slice(0, 3);
  const options = shuffle([q, ...distractors]);
  stage.innerHTML =
    `<div class="st-progress">Question ${s.i + 1} / ${s.questions.length} · Score ${s.score}</div>` +
    `<div class="st-q-prompt"><span class="st-q-label">Which topic does this describe?</span>${esc(prompt)}</div>` +
    '<ul class="st-q-options">' + options.map(o =>
      `<li><button class="st-q-opt" data-id="${esc(o.id)}">${esc(o.name)}</button></li>`).join("") + '</ul>' +
    '<div id="st-q-feedback" class="st-q-feedback"></div>';
  s.answered = false;
  stage.querySelectorAll(".st-q-opt").forEach(btn => btn.addEventListener("click", () => {
    if (s.answered) return; s.answered = true;
    const correct = btn.dataset.id === q.id;
    if (correct) s.score++;
    stage.querySelectorAll(".st-q-opt").forEach(b => {
      if (b.dataset.id === q.id) b.classList.add("correct");
      else if (b === btn) b.classList.add("wrong");
      b.disabled = true;
    });
    const fb = stage.querySelector("#st-q-feedback");
    fb.innerHTML = (correct ? '<span class="st-ok">Correct!</span> ' : '<span class="st-no">Not quite.</span> ') +
      `Answer: <strong>${esc(q.name)}</strong>` +
      ` · <button class="st-link" id="st-q-open">open ↗</button>` +
      ` <button class="st-btn st-btn-primary st-next" id="st-q-next">Next →</button>`;
    fb.querySelector("#st-q-open").addEventListener("click", () => { stClose(); stGoToTopic(q.id); });
    fb.querySelector("#st-q-next").addEventListener("click", () => { s.i++; stRenderQuestion(stage); });
  }));
}
function stRestartQuizSame(stage) {
  const s = _stQuizState; if (!s) return;
  s.questions = shuffle(s.pool.slice()).slice(0, Math.min(10, s.pool.length));
  s.i = 0; s.score = 0; stRenderQuestion(stage);
}

// ── ACRONYM QUIZ ────────────────────────────────────────────────────────────
// Questions built from the dictionary rather than from topic titles. The
// answers are already structured, so distractors can be chosen honestly
// instead of guessed — which is the weakness of the topic quiz.

let _acroData = null;

/** The compact dictionary inlined by build.py: [acronym, [expansions], area]. */
function acroData() {
  if (_acroData) return _acroData;
  const el = document.getElementById("acronym-data");
  try {
    _acroData = el ? JSON.parse(el.textContent) : [];
  } catch { _acroData = []; }
  return _acroData;
}

/** Group by subject area, so a distractor is never a giveaway from elsewhere. */
function acroByArea() {
  const byArea = new Map();
  acroData().forEach(e => {
    if (!byArea.has(e[2])) byArea.set(e[2], []);
    byArea.get(e[2]).push(e);
  });
  return byArea;
}

function acroAreas() {
  return [...acroByArea().keys()].sort();
}

/** Three wrong answers from the same area, falling back to the whole set. */
function acroDistractors(entry, pick, n) {
  const byArea = acroByArea();
  const sameArea = (byArea.get(entry[2]) || []).filter(e => e[0] !== entry[0]);
  const pool = sameArea.length >= n ? sameArea : acroData().filter(e => e[0] !== entry[0]);
  const out = [];
  const seen = new Set([pick(entry).toLowerCase()]);
  for (const cand of shuffle(pool.slice())) {
    // Two acronyms that differ only in case (IoC / IOC) make a typography
    // question, not a knowledge one.
    if (cand[0].toLowerCase() === entry[0].toLowerCase()) continue;
    const v = pick(cand);
    if (!v || seen.has(v.toLowerCase())) continue;
    seen.add(v.toLowerCase());
    out.push(v);
    if (out.length === n) break;
  }
  return out;
}

function acroQuestions(area, count) {
  const all = acroData().filter(e => area === "__all" || e[2] === area);
  const single = all.filter(e => e[1].length === 1);
  const multi = all.filter(e => e[1].length > 1);
  const qs = [];

  shuffle(single.slice()).forEach(e => {
    if (qs.length >= count) return;
    if (Math.random() < 0.5) {
      // Expand: acronym -> what it stands for
      const wrong = acroDistractors(e, x => x[1][0], 3);
      if (wrong.length < 3) return;
      qs.push({ q: `<strong>${esc(e[0])}</strong> stands for…`, area: e[2],
                answer: e[1][0], options: shuffle([e[1][0], ...wrong]) });
    } else {
      // Contract: expansion -> which acronym
      const wrong = acroDistractors(e, x => x[0], 3);
      if (wrong.length < 3) return;
      qs.push({ q: `Which acronym means <em>${esc(e[1][0])}</em>?`, area: e[2],
                answer: e[0], options: shuffle([e[0], ...wrong]) });
    }
  });

  // Disambiguation is the only place a multi-meaning entry is fair: the other
  // meanings of the same acronym are the distractors, which is the actual skill.
  shuffle(multi.slice()).slice(0, Math.max(1, Math.round(count * 0.2))).forEach(e => {
    const answer = e[1][0];
    const others = e[1].slice(1);
    const wrong = others.concat(acroDistractors(e, x => x[1][0], 3 - others.length));
    if (wrong.length < 3) return;
    qs.push({ q: `<strong>${esc(e[0])}</strong> has more than one meaning. In a ` +
                 `<strong>${esc(e[2])}</strong> context, which one applies?`, area: e[2],
              answer, options: shuffle([answer, ...wrong.slice(0, 3)]) });
  });

  return shuffle(qs).slice(0, count);
}

let _acroQuizState = null;

function stOpenAcroQuiz() {
  stOpen(body => {
    if (!acroData().length) {
      body.innerHTML = '<h2 class="st-h">Acronym quiz</h2>' +
        '<p class="st-empty">The acronym dictionary was not found on this page. ' +
        'Rebuild with <code>python3 build.py</code>.</p>';
      return;
    }
    const areas = acroAreas().map(a => `<option value="${esc(a)}">${esc(a)}</option>`).join("");
    body.innerHTML =
      '<h2 class="st-h">Acronym quiz</h2>' +
      '<div class="st-toolbar"><label class="st-lbl">Area</label>' +
      `<select id="st-aq-area" class="st-select"><option value="__all">◈ All areas</option>${areas}</select>` +
      '<button id="st-aq-start" class="st-btn st-btn-primary">Start</button></div>' +
      `<p class="st-hint">${acroData().length} acronyms in the dictionary.</p>` +
      '<div id="st-aq-stage"></div>';
    const sel = body.querySelector("#st-aq-area");
    const stage = body.querySelector("#st-aq-stage");
    body.querySelector("#st-aq-start").addEventListener("click", () => stStartAcroQuiz(sel.value, stage));
    stStartAcroQuiz(sel.value, stage);
  });
}

function stStartAcroQuiz(area, stage) {
  const questions = acroQuestions(area, 10);
  if (questions.length < 4) {
    stage.innerHTML = '<p class="st-empty">Not enough acronyms in that area to build a quiz. Pick a broader one.</p>';
    return;
  }
  _acroQuizState = { area, questions, i: 0, score: 0, answered: false };
  stRenderAcroQuestion(stage);
}

function stRenderAcroQuestion(stage) {
  const s = _acroQuizState; if (!s) return;
  if (s.i >= s.questions.length) {
    const pct = Math.round((s.score / s.questions.length) * 100);
    stage.innerHTML = `<div class="st-result"><div class="st-result-big">${pct >= 80 ? "🏆" : pct >= 50 ? "👍" : "📚"}</div>` +
      `<p>Score: <strong>${s.score} / ${s.questions.length}</strong> (${pct}%)</p>` +
      '<button id="st-aq-retry" class="st-btn st-btn-primary">New quiz</button></div>';
    stage.querySelector("#st-aq-retry").addEventListener("click", () => stStartAcroQuiz(s.area, stage));
    return;
  }
  const q = s.questions[s.i];
  // Reuses the topic quiz's markup and styling — same component, new source.
  stage.innerHTML =
    `<div class="st-progress">Question ${s.i + 1} / ${s.questions.length} · Score ${s.score}</div>` +
    `<div class="st-q-prompt"><span class="st-q-label">${esc(q.area)}</span>${q.q}</div>` +
    '<ul class="st-q-options">' +
    q.options.map((o, n) => `<li><button class="st-q-opt" data-n="${n}">${esc(o)}</button></li>`).join("") +
    '</ul><div id="st-q-feedback" class="st-q-feedback"></div>';

  s.answered = false;
  stage.querySelectorAll(".st-q-opt").forEach(btn => btn.addEventListener("click", () => {
    if (s.answered) return;
    s.answered = true;
    const right = q.options[Number(btn.dataset.n)] === q.answer;
    if (right) s.score++;
    stage.querySelectorAll(".st-q-opt").forEach(b => {
      if (q.options[Number(b.dataset.n)] === q.answer) b.classList.add("correct");
      else if (b === btn) b.classList.add("wrong");
      b.disabled = true;
    });
    const fb = stage.querySelector("#st-q-feedback");
    fb.innerHTML = (right ? '<span class="st-ok">Correct!</span> ' : '<span class="st-no">Not quite.</span> ') +
      `Answer: <strong>${esc(q.answer)}</strong>` +
      ' <button class="st-btn st-next" id="st-aq-next">Next →</button>';
    fb.querySelector("#st-aq-next").addEventListener("click", () => {
      s.i++; s.answered = false; stRenderAcroQuestion(stage);
    });
    fb.querySelector("#st-aq-next").focus();
  }));
}

// ── STUDY LIST (bookmarks) ──────────────────────────────────────────────────
function stOpenStudyList() {
  stOpen(body => {
    body.innerHTML = '<h2 class="st-h">★ My study list</h2><div id="st-list-body"></div>';
    stRenderStudyList(body.querySelector("#st-list-body"));
  });
}
function stRenderStudyList(host) {
  const marked = stIndex().filter(t => stIsBookmarked(t.id));
  if (!marked.length) {
    host.innerHTML = '<p class="st-empty">No saved topics yet. Click the ★ on any topic to add it here, then quiz or flashcard just your list.</p>';
    return;
  }
  const byDom = {};
  marked.forEach(t => { (byDom[t.domainTitle] = byDom[t.domainTitle] || []).push(t); });
  host.innerHTML =
    `<div class="st-toolbar"><span class="st-count">${marked.length} saved</span>` +
    '<button id="st-list-fc" class="st-btn">Flashcard these</button>' +
    '<button id="st-list-qz" class="st-btn">Quiz these</button></div>' +
    '<ul class="st-list">' + Object.keys(byDom).map(dom =>
      `<li class="st-list-dom">${esc(byDom[dom][0].domainIcon)} ${esc(dom)}</li>` +
      byDom[dom].map(t =>
        `<li class="st-list-item"><button class="st-list-link" data-id="${esc(t.id)}">${esc(t.name)}</button>` +
        `<button class="st-list-remove" data-id="${esc(t.id)}" title="Remove">✕</button></li>`).join("")
    ).join("") + '</ul>';
  host.querySelector("#st-list-fc").addEventListener("click", () => stOpenFlashcards());
  host.querySelector("#st-list-qz").addEventListener("click", () => stOpenQuiz());
  host.querySelectorAll(".st-list-link").forEach(b => b.addEventListener("click", () => { stClose(); stGoToTopic(b.dataset.id); }));
  host.querySelectorAll(".st-list-remove").forEach(b => b.addEventListener("click", () => {
    const id = b.dataset.id;
    localStorage.removeItem(BOOKMARK_PREFIX + id);
    document.getElementById(id)?.classList.remove("bookmarked");
    stRenderStudyList(host);
  }));
}
/** Called when a bookmark toggles elsewhere so an open list stays fresh. */
function stRefreshStudyList() {
  const host = document.getElementById("st-list-body");
  if (host && _stOverlay && !_stOverlay.hidden) stRenderStudyList(host);
}

// ── LAUNCHER (FAB + menu) + keyboard shortcut ───────────────────────────────
function initStudyTools() {
  const fab = document.createElement("div");
  fab.id = "study-fab-wrap";
  fab.innerHTML =
    '<div id="study-menu" hidden>' +
      '<button class="study-mi" data-act="jump"><span>⌘K</span> Quick jump</button>' +
      '<button class="study-mi" data-act="cards"><span>🃏</span> Flashcards</button>' +
      '<button class="study-mi" data-act="due"><span>⏰</span> Review due</button>' +
      '<button class="study-mi" data-act="quiz"><span>❓</span> Quiz</button>' +
      '<button class="study-mi" data-act="acro"><span>🔤</span> Acronym quiz</button>' +
      '<button class="study-mi" data-act="list"><span>★</span> Study list</button>' +
    '</div>' +
    '<button id="study-fab" title="Study tools" aria-label="Study tools" aria-haspopup="true" aria-expanded="false">' +
      '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">' +
        '<path fill="currentColor" d="M12 3 1 8l11 5 9-4.09V15h2V8L12 3z"/>' +
        '<path fill="currentColor" d="M5 11.18v3.02C5 15.75 8.13 17 12 17s7-1.25 7-2.8v-3.02l-7 3.18-7-3.18z"/>' +
      '</svg></button>';
  document.body.appendChild(fab);

  const menu = fab.querySelector("#study-menu");
  const btn = fab.querySelector("#study-fab");
  const closeMenu = () => { menu.hidden = true; btn.setAttribute("aria-expanded", "false"); };
  btn.addEventListener("click", e => {
    // Stop this click from also reaching the document "click-outside" handler,
    // which could otherwise re-close the menu we just opened (touch devices).
    e.stopPropagation();
    const willOpen = menu.hidden;      // currently hidden -> we're opening
    menu.hidden = !willOpen;           // toggle
    btn.setAttribute("aria-expanded", willOpen ? "true" : "false");
  });
  menu.addEventListener("click", e => {
    const mi = e.target.closest(".study-mi"); if (!mi) return;
    closeMenu();
    ({ jump: stOpenJump, cards: stOpenFlashcards, due: stOpenDue, quiz: stOpenQuiz,
       acro: stOpenAcroQuiz, list: stOpenStudyList }[mi.dataset.act])();
  });
  document.addEventListener("click", e => { if (!fab.contains(e.target) && !menu.hidden) closeMenu(); });

  srsUpdateBadge();
  // Another tab grading a card should update this one's badge too.
  window.addEventListener("storage", e => { if (e.key && e.key.startsWith(SRS_PREFIX)) srsUpdateBadge(); });

  // Global keyboard shortcuts
  document.addEventListener("keydown", e => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") { e.preventDefault(); stOpenJump(); return; }
    if (e.key === "Escape" && _stOverlay && !_stOverlay.hidden) { stClose(); }
  });
}

// ── SERVICE WORKER (offline PWA; https only — never over file://) ────────────
if ("serviceWorker" in navigator && location.protocol.startsWith("http")) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("/sw.js").catch(() => {});
  });
}
