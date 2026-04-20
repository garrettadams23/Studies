/**
 * script.js
 * =========
 * CompTIA & Tech Reference — Interactive UI Logic
 * 2026 Edition
 *
 * Responsibilities:
 *   1. Domain accordion toggle  (toggleDomain)
 *   2. Topic accordion toggle   (toggleTopic)
 *   3. Domain filter chips      (filter)
 *   4. Light / dark theme       (toggleTheme, updateThemeButton)
 *   5. Expand / collapse all    (toggleAll)
 *   6. Cloud responsibility stack builder (IIFE on DOMContentLoaded)
 *   7. Theme persistence via localStorage
 *
 * No external dependencies. Vanilla JS only.
 */

// ─────────────────────────────────────────────────────────────────────────────
// 1. DOMAIN ACCORDION
// Toggles the domain body open/closed. Also updates the chevron icon direction
// via CSS class .open (see style.css → .domain-header.open .chevron).
// ─────────────────────────────────────────────────────────────────────────────

/**
 * Toggle a domain section open or closed.
 * @param {HTMLElement} h - The .domain-header element that was clicked.
 */
function toggleDomain(h) {
  var b = h.nextElementSibling; // .domain-body immediately follows header
  var o = b.classList.toggle("open"); // toggle returns new state (true = open)
  h.classList.toggle("open", o); // sync header class for chevron rotation
}

// ─────────────────────────────────────────────────────────────────────────────
// 2. TOPIC ACCORDION
// Toggles an individual topic row open/closed within a domain body.
// The .open class on both header and body drives the CSS display transition.
// ─────────────────────────────────────────────────────────────────────────────

/**
 * Toggle a topic row open or closed.
 * @param {HTMLElement} h - The .topic-header element that was clicked.
 */
function toggleTopic(h) {
  h.classList.toggle("open"); // rotates the ▶ chevron via CSS
  h.nextElementSibling.classList.toggle("open"); // shows/hides .topic-body
}

// ─────────────────────────────────────────────────────────────────────────────
// 3. FILTER CHIPS
// Hides all domain sections that don't match the selected filter chip.
// "all" shows every section. Any other value matches data-domain attribute.
// ─────────────────────────────────────────────────────────────────────────────

/**
 * Filter visible domain sections by category.
 * @param {string}      domain - Domain key (e.g. "net") or "all".
 * @param {HTMLElement} chip   - The clicked .chip element (for active styling).
 */
function filter(domain, chip) {
  // Remove active state from all chips, then mark the clicked one
  document.querySelectorAll(".chip").forEach(function (c) {
    c.classList.remove("active");
  });
  chip.classList.add("active");

  // Show/hide domain sections based on their data-domain attribute
  document.querySelectorAll(".domain-section").forEach(function (s) {
    s.classList.toggle(
      "hidden",
      domain !== "all" && s.dataset.domain !== domain,
    );
  });
}

// ─────────────────────────────────────────────────────────────────────────────
// 4. THEME TOGGLE
// Switches between dark (default) and light mode.
// Persists selection to localStorage so preference survives page reloads.
// CSS variables in :root / [data-theme="light"] handle all visual changes.
// ─────────────────────────────────────────────────────────────────────────────

/**
 * Toggle between dark and light theme.
 * @param {HTMLElement} btn - The theme toggle button element.
 */
function toggleTheme(btn) {
  var doc = document.documentElement;
  var currentTheme = doc.getAttribute("data-theme");
  var newTheme = currentTheme === "light" ? "dark" : "light";

  doc.setAttribute("data-theme", newTheme);
  localStorage.setItem("theme", newTheme); // persist across page loads

  updateThemeButton(btn, newTheme);
}

/**
 * Update the theme button's label and color to reflect current theme.
 * @param {HTMLElement|null} btn   - The button element to update.
 * @param {string}           theme - Current theme: "light" or "dark".
 */
function updateThemeButton(btn, theme) {
  if (!btn) return;

  // Update label text
  btn.textContent = theme === "light" ? "☾ DARK MODE" : "☀ LIGHT MODE";

  // Update button accent color to match the active theme palette
  btn.style.color = theme === "light" ? "var(--purple)" : "var(--amber)";
  btn.style.borderColor = theme === "light" ? "var(--purple)" : "var(--amber)";
}

// ─────────────────────────────────────────────────────────────────────────────
// 4b. THEME INITIALIZATION
// Runs immediately (IIFE) to apply saved theme before the page renders,
// preventing a flash of the wrong theme.
// ─────────────────────────────────────────────────────────────────────────────
(function initTheme() {
  var savedTheme = localStorage.getItem("theme") || "dark"; // dark is default
  document.documentElement.setAttribute("data-theme", savedTheme);

  // Wait for DOM so the button element exists before we update it
  window.addEventListener("DOMContentLoaded", function () {
    var btn = document.getElementById("theme-toggle-btn");
    updateThemeButton(btn, savedTheme);
  });
})();

// ─────────────────────────────────────────────────────────────────────────────
// 5. CLOUD RESPONSIBILITY STACK BUILDER
// Dynamically generates the IaaS/PaaS/SaaS shared responsibility matrix.
// Runs after DOM is ready. The matrix shows which layers are "Customer" vs
// "Provider" responsibility for each cloud model.
// ─────────────────────────────────────────────────────────────────────────────
(function buildCloudStack() {
  window.addEventListener("DOMContentLoaded", function () {
    var container = document.getElementById("cloud-stack");
    if (!container) return;

    // Stack layers from top (application) to bottom (networking infrastructure)
    var layers = [
      "Applications",
      "Data",
      "Runtime",
      "Middleware",
      "OS",
      "Virtualization",
      "Servers",
      "Storage",
      "Networking",
    ];

    /**
     * Responsibility matrix: rows = layers, columns = [OnPrem, IaaS, PaaS, SaaS]
     * 1 = Customer responsibility, 0 = Provider responsibility
     */
    var resp = [
      [1, 1, 1, 0], // Applications
      [1, 1, 1, 0], // Data          ← SaaS: provider manages app, customer owns data policy
      [1, 1, 0, 0], // Runtime
      [1, 1, 0, 0], // Middleware
      [1, 1, 0, 0], // OS
      [1, 0, 0, 0], // Virtualization
      [1, 0, 0, 0], // Servers
      [1, 0, 0, 0], // Storage
      [1, 0, 0, 0], // Networking
    ];

    // Color pairs: [background, text] per column [OnPrem, IaaS, PaaS, SaaS]
    var colors = [
      ["rgba(255,77,109,.12)", "#ff4d6d"], // On-Prem  — red
      ["rgba(255,176,32,.09)", "#ffb020"], // IaaS     — amber
      ["rgba(0,212,255,.08)", "#00d4ff"], // PaaS     — cyan
      ["rgba(0,255,153,.08)", "#00ff99"], // SaaS     — green
    ];

    // Build one row per layer
    layers.forEach(function (layerName, rowIndex) {
      var row = document.createElement("div");
      row.style.cssText =
        "display:flex;gap:0;margin-bottom:3px;align-items:stretch";

      // Layer name label column
      var lbl = document.createElement("div");
      lbl.style.cssText =
        "width:120px;font-size:11.5px;color:#cdd9f0;padding:5px 4px 5px 0;" +
        "flex-shrink:0;font-weight:500";
      lbl.textContent = layerName;
      row.appendChild(lbl);

      // Four model cells (OnPrem → SaaS)
      resp[rowIndex].forEach(function (isCustomer, colIndex) {
        var cell = document.createElement("div");
        cell.style.cssText =
          "flex:1;text-align:center;padding:5px 3px;font-size:11px;" +
          "font-weight:600;border-radius:3px;margin:0 2px;" +
          (isCustomer
            ? "background:" +
              colors[colIndex][0] +
              ";color:" +
              colors[colIndex][1] +
              ";border:1px solid " +
              colors[colIndex][0]
            : "background:rgba(255,255,255,.02);color:#3a4a60;" +
              "border:1px solid rgba(255,255,255,.05)");
        cell.textContent = isCustomer ? "Customer" : "Provider";
        row.appendChild(cell);
      });

      container.appendChild(row);
    });
  });
})();

// ─────────────────────────────────────────────────────────────────────────────
// 6. EXPAND / COLLAPSE ALL
// Toggles every domain and topic accordion open or closed simultaneously.
// Tracks state with the module-level allExpanded variable.
// ─────────────────────────────────────────────────────────────────────────────

/** @type {boolean} Tracks whether all sections are currently expanded. */
var allExpanded = false;

/**
 * Expand or collapse every domain and topic accordion at once.
 * @param {HTMLElement} btn - The "Expand All / Collapse All" button.
 */
function toggleAll(btn) {
  allExpanded = !allExpanded;

  // Select all accordion headers and bodies
  var headers = document.querySelectorAll(".domain-header, .topic-header");
  var bodies = document.querySelectorAll(".domain-body, .topic-body");

  headers.forEach(function (h) {
    h.classList.toggle("open", allExpanded);
  });
  bodies.forEach(function (b) {
    b.classList.toggle("open", allExpanded);
  });

  // Update button label to reflect next action
  btn.textContent = allExpanded ? "↕ COLLAPSE ALL" : "↕ EXPAND ALL";
}

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
