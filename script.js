/**
 * script.js
 * =========
 * CompTIA & Tech Reference — Interactive UI Logic
 * 2026 Edition
 */

// ─────────────────────────────────────────────────────────────────────────────
// STATE & CONSTANTS
// ─────────────────────────────────────────────────────────────────────────────

/** @type {boolean} Tracks whether all sections are currently expanded. */
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

// ─────────────────────────────────────────────────────────────────────────────
// 1. CORE UI COMPONENTS (Accordions & Filtering)
// ─────────────────────────────────────────────────────────────────────────────

/**
 * Toggle a domain section open or closed.
 * @param {HTMLElement} h - The .domain-header element that was clicked.
 */
function toggleDomain(h) {
  const b = h.nextElementSibling;
  const isOpen = b.classList.toggle("open");
  h.classList.toggle("open", isOpen);
}

/**
 * Toggle a topic row open or closed.
 * @param {HTMLElement} h - The .topic-header element that was clicked.
 */
function toggleTopic(h) {
  h.classList.toggle("open");
  h.nextElementSibling.classList.toggle("open");
}

/**
 * Filter visible domain sections by category.
 * @param {string} domain - Domain key (e.g. "net") or "all".
 * @param {HTMLElement} chip - The clicked .chip element.
 */
function filter(domain, chip) {
  document.querySelectorAll(".chip").forEach(c => c.classList.remove("active"));
  chip.classList.add("active");

  document.querySelectorAll(".domain-section").forEach(s => {
    s.classList.toggle("hidden", domain !== "all" && s.dataset.domain !== domain);
  });
}

/**
 * Expand or collapse every domain and topic accordion at once.
 * @param {HTMLElement} btn - The trigger button.
 */
function toggleAll(btn) {
  allExpanded = !allExpanded;

  const headers = document.querySelectorAll(".domain-header, .topic-header");
  const bodies = document.querySelectorAll(".domain-body, .topic-body");

  headers.forEach(h => h.classList.toggle("open", allExpanded));
  bodies.forEach(b => b.classList.toggle("open", allExpanded));

  // Sync button labels
  const mainBtn = document.getElementById("expand-all-btn"); // if exists
  if (mainBtn) mainBtn.textContent = allExpanded ? "↕ COLLAPSE ALL" : "↕ EXPAND ALL";

  const hdrBtn = document.getElementById("hdr-expand-btn");
  if (hdrBtn) hdrBtn.title = allExpanded ? "Collapse all" : "Expand all";
}

// ─────────────────────────────────────────────────────────────────────────────
// 2. THEME MANAGEMENT
// ─────────────────────────────────────────────────────────────────────────────

/**
 * Toggle between dark and light theme.
 * @param {HTMLElement} btn - The trigger button.
 */
function toggleTheme(btn) {
  const doc = document.documentElement;
  const currentTheme = doc.getAttribute("data-theme");
  const newTheme = currentTheme === "light" ? "dark" : "light";

  doc.setAttribute("data-theme", newTheme);
  localStorage.setItem("theme", newTheme);

  updateThemeUI(newTheme);
}

/**
 * Update all theme-related UI elements (buttons, icons).
 * @param {string} theme - "light" or "dark".
 */
function updateThemeUI(theme) {
  // Update main toggle button if it exists
  const mainBtn = document.getElementById("theme-toggle-btn");
  if (mainBtn) {
    mainBtn.textContent = theme === "light" ? "☾ DARK MODE" : "☀ LIGHT MODE";
    mainBtn.style.color = theme === "light" ? "var(--purple)" : "var(--amber)";
    mainBtn.style.borderColor = theme === "light" ? "var(--purple)" : "var(--amber)";
  }

  // Update header mini-toggle
  const hdrBtn = document.getElementById("hdr-theme-btn");
  if (hdrBtn) hdrBtn.textContent = theme === "light" ? "☾" : "☀";
}

// ─────────────────────────────────────────────────────────────────────────────
// 3. INITIALIZATION & DYNAMIC BUILDERS
// ─────────────────────────────────────────────────────────────────────────────

/**
 * Initialize theme immediately to prevent flash.
 */
(function() {
  const savedTheme = localStorage.getItem("theme") || "dark";
  document.documentElement.setAttribute("data-theme", savedTheme);
})();

document.addEventListener("DOMContentLoaded", () => {
  const currentTheme = document.documentElement.getAttribute("data-theme");
  updateThemeUI(currentTheme);

  initSnapQuote();
  initCloudStack();
  initTouchFeedback();
});

/**
 * Rotate random quotes in the header.
 */
function initSnapQuote() {
  const el = document.getElementById("sq-text");
  const box = document.getElementById("snap-quote");
  if (!el || !box) return;

  let idx = Math.floor(Math.random() * QUOTES.length);

  const showQuote = (i) => {
    box.classList.remove("visible");
    setTimeout(() => {
      el.textContent = QUOTES[i % QUOTES.length];
      box.classList.add("visible");
    }, 600);
  };

  showQuote(idx);
  setInterval(() => showQuote(++idx), 8000);
}

/**
 * Build the Cloud Responsibility Matrix (IaaS/PaaS/SaaS).
 */
function initCloudStack() {
  const container = document.getElementById("cloud-stack");
  if (!container) return;

  const layers = ["Applications", "Data", "Runtime", "Middleware", "OS", "Virtualization", "Servers", "Storage", "Networking"];
  const resp = [
    [1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0],
    [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]
  ];
  const colors = [
    ["rgba(255,77,109,.12)", "#ff4d6d"], // On-Prem
    ["rgba(255,176,32,.09)", "#ffb020"], // IaaS
    ["rgba(0,212,255,.08)", "#00d4ff"], // PaaS
    ["rgba(0,255,153,.08)", "#00ff99"]  // SaaS
  ];

  layers.forEach((name, rIdx) => {
    const row = document.createElement("div");
    row.style.cssText = "display:flex;gap:0;margin-bottom:3px;align-items:stretch";

    const lbl = document.createElement("div");
    lbl.style.cssText = "width:120px;font-size:11.5px;color:#cdd9f0;padding:5px 4px 5px 0;flex-shrink:0;font-weight:500";
    lbl.textContent = name;
    row.appendChild(lbl);

    resp[rIdx].forEach((isCust, cIdx) => {
      const cell = document.createElement("div");
      cell.style.cssText = `flex:1;text-align:center;padding:5px 3px;font-size:11px;font-weight:600;border-radius:3px;margin:0 2px;
        ${isCust ? `background:${colors[cIdx][0]};color:${colors[cIdx][1]};border:1px solid ${colors[cIdx][0]}` :
        `background:rgba(255,255,255,.02);color:#3a4a60;border:1px solid rgba(255,255,255,.05)`}`;
      cell.textContent = isCust ? "Customer" : "Provider";
      row.appendChild(cell);
    });
    container.appendChild(row);
  });
}

/**
 * Visual feedback for touch devices.
 */
function initTouchFeedback() {
  const interactive = document.querySelectorAll(".chip, .domain-header, .topic-header");
  const addTap = function() { this.classList.add("is-tapping"); };
  const remTap = function() { this.classList.remove("is-tapping"); };

  interactive.forEach(el => {
    el.addEventListener("touchstart", addTap, { passive: true });
    el.addEventListener("touchend", remTap, { passive: true });
    el.addEventListener("touchcancel", remTap, { passive: true });
  });
}

// ─────────────────────────────────────────────────────────────────────────────
// 4. UTILITY TOOLS (URL Codec)
// ─────────────────────────────────────────────────────────────────────────────

const _urlIn = () => document.getElementById("url-codec-input")?.value || "";
const _urlOut = (v) => { const el = document.getElementById("url-codec-output"); if(el) el.value = v; };

function _urlMsg(txt, color = "var(--muted)") {
  const el = document.getElementById("url-codec-msg");
  if (!el) return;
  el.textContent = txt;
  el.style.color = color;
  clearTimeout(el._t);
  el._t = setTimeout(() => el.textContent = "", 2500);
}

function urlToolEncode() {
  const raw = _urlIn();
  if (!raw) return _urlMsg("⚠ Nothing to encode.", "var(--amber)");
  try {
    _urlOut(encodeURIComponent(raw));
    _urlMsg("✓ Encoded.", "var(--green)");
  } catch(e) { _urlMsg("✗ Encode error: " + e.message, "var(--red)"); }
}

function urlToolDecode() {
  const raw = _urlIn();
  if (!raw) return _urlMsg("⚠ Nothing to decode.", "var(--amber)");
  try {
    _urlOut(decodeURIComponent(raw.replace(/\+/g, " ")));
    _urlMsg("✓ Decoded.", "var(--cyan)");
  } catch(e) { _urlMsg("✗ Malformed encoding.", "var(--red)"); }
}

function urlToolCopy() {
  const el = document.getElementById("url-codec-output");
  if (!el?.value) return _urlMsg("⚠ Nothing to copy.", "var(--amber)");
  navigator.clipboard.writeText(el.value).then(() => _urlMsg("✓ Copied.", "var(--green)"));
}

function urlToolClear() {
  const i = document.getElementById("url-codec-input");
  const o = document.getElementById("url-codec-output");
  if(i) i.value = "";
  if(o) o.value = "";
  _urlMsg("");
}
