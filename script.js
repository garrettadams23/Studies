// ── Domain toggle
function toggleDomain(h) {
  var b = h.nextElementSibling;
  var o = b.classList.toggle("open");
  h.classList.toggle("open", o);
}
// ── Topic toggle
function toggleTopic(h) {
  h.classList.toggle("open");
  h.nextElementSibling.classList.toggle("open");
}
// ── Filter chips
function filter(domain, chip) {
  document.querySelectorAll(".chip").forEach((c) => c.classList.remove("active"));
  chip.classList.add("active");
  document.querySelectorAll(".domain-section").forEach((s) => {
    s.classList.toggle("hidden", domain !== "all" && s.dataset.domain !== domain);
  });
}

// ── Theme toggle
function toggleTheme(btn) {
  const doc = document.documentElement;
  const currentTheme = doc.getAttribute("data-theme");
  const newTheme = currentTheme === "light" ? "dark" : "light";
  doc.setAttribute("data-theme", newTheme);
  localStorage.setItem("theme", newTheme);
  updateThemeButton(btn, newTheme);
}

function updateThemeButton(btn, theme) {
  if (!btn) return;
  btn.textContent = theme === "light" ? "☾ DARK MODE" : "☀ LIGHT MODE";
  btn.style.color = theme === "light" ? "var(--purple)" : "var(--amber)";
  btn.style.borderColor = theme === "light" ? "var(--purple)" : "var(--amber)";
}

// ── Initialize theme
(function () {
  const savedTheme = localStorage.getItem("theme") || "dark";
  document.documentElement.setAttribute("data-theme", savedTheme);
  window.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("theme-toggle-btn");
    updateThemeButton(btn, savedTheme);
  });
})();

// ── Build cloud responsibility stack
(function () {
  var container = document.getElementById("cloud-stack");
  if (!container) return;
  var layers = ["Applications","Data","Runtime","Middleware","OS","Virtualization","Servers","Storage","Networking"];
  var resp = [[1,1,1,1],[1,1,1,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]];
  var colors = [
    ["rgba(255,77,109,.12)","#ff4d6d"],
    ["rgba(255,176,32,.09)","#ffb020"],
    ["rgba(0,212,255,.08)","#00d4ff"],
    ["rgba(0,255,153,.08)","#00ff99"],
  ];
  layers.forEach(function (l, i) {
    var row = document.createElement("div");
    row.style.cssText = "display:flex;gap:0;margin-bottom:3px;align-items:stretch";
    var lbl = document.createElement("div");
    lbl.style.cssText = "width:120px;font-size:11.5px;color:#cdd9f0;padding:5px 4px 5px 0;flex-shrink:0;font-weight:500";
    lbl.textContent = l;
    row.appendChild(lbl);
    resp[i].forEach(function (v, ci) {
      var cell = document.createElement("div");
      cell.style.cssText =
        "flex:1;text-align:center;padding:5px 3px;font-size:11px;font-weight:600;border-radius:3px;margin:0 2px;" +
        (v
          ? "background:" + colors[ci][0] + ";color:" + colors[ci][1] + ";border:1px solid " + colors[ci][0]
          : "background:rgba(255,255,255,.02);color:#3a4a60;border:1px solid rgba(255,255,255,.05)");
      cell.textContent = v ? "Customer" : "Provider";
      row.appendChild(cell);
    });
    container.appendChild(row);
  });
})();

// ── Toggle All
var allExpanded = false;
function toggleAll(btn) {
  allExpanded = !allExpanded;
  var headers = document.querySelectorAll(".domain-header, .topic-header");
  var bodies = document.querySelectorAll(".domain-body, .topic-body");
  headers.forEach((h) => h.classList.toggle("open", allExpanded));
  bodies.forEach((b) => b.classList.toggle("open", allExpanded));
  btn.textContent = allExpanded ? "↕ COLLAPSE ALL" : "↕ EXPAND ALL";
}

// ══════════════════════════════════════════
// CVSS v3.1 BASE SCORE CALCULATOR
// ══════════════════════════════════════════
(function () {
  // Metric definitions
  const exploitMetrics = [
    {
      id: "AV", label: "AV", name: "Attack Vector",
      desc: "How is the vulnerability exploited?",
      opts: [
        { v: "N", label: "Network",   score: 0.85, color: "#ef4444" },
        { v: "A", label: "Adjacent",  score: 0.62, color: "#f97316" },
        { v: "L", label: "Local",     score: 0.55, color: "#eab308" },
        { v: "P", label: "Physical",  score: 0.20, color: "#22c55e" },
      ]
    },
    {
      id: "AC", label: "AC", name: "Attack Complexity",
      desc: "Conditions beyond attacker's control?",
      opts: [
        { v: "L", label: "Low",  score: 0.77, color: "#ef4444" },
        { v: "H", label: "High", score: 0.44, color: "#22c55e" },
      ]
    },
    {
      id: "PR", label: "PR", name: "Privileges Required",
      desc: "Privileges needed before exploit?",
      opts: [
        { v: "N", label: "None", score: 0.85, color: "#ef4444" },
        { v: "L", label: "Low",  score: 0.62, color: "#eab308" },
        { v: "H", label: "High", score: 0.27, color: "#22c55e" },
      ]
    },
    {
      id: "UI", label: "UI", name: "User Interaction",
      desc: "Is user participation required?",
      opts: [
        { v: "N", label: "None",     score: 0.85, color: "#ef4444" },
        { v: "R", label: "Required", score: 0.62, color: "#22c55e" },
      ]
    },
    {
      id: "S", label: "S", name: "Scope",
      desc: "Can impact cross security boundaries?",
      opts: [
        { v: "U", label: "Unchanged", score: 0, color: "#22c55e" },
        { v: "C", label: "Changed",   score: 1, color: "#ef4444" },
      ]
    },
  ];

  const impactMetrics = [
    {
      id: "C", label: "C", name: "Confidentiality Impact",
      desc: "Impact to data confidentiality",
      opts: [
        { v: "N", label: "None", score: 0,    color: "#22c55e" },
        { v: "L", label: "Low",  score: 0.22, color: "#eab308" },
        { v: "H", label: "High", score: 0.56, color: "#ef4444" },
      ]
    },
    {
      id: "I", label: "I", name: "Integrity Impact",
      desc: "Impact to data integrity",
      opts: [
        { v: "N", label: "None", score: 0,    color: "#22c55e" },
        { v: "L", label: "Low",  score: 0.22, color: "#eab308" },
        { v: "H", label: "High", score: 0.56, color: "#ef4444" },
      ]
    },
    {
      id: "A", label: "A", name: "Availability Impact",
      desc: "Impact to system availability",
      opts: [
        { v: "N", label: "None", score: 0,    color: "#22c55e" },
        { v: "L", label: "Low",  score: 0.22, color: "#eab308" },
        { v: "H", label: "High", score: 0.56, color: "#ef4444" },
      ]
    },
  ];

  // State
  const selected = { AV: null, AC: null, PR: null, UI: null, S: null, C: null, I: null, A: null };
  // PR adjusted scores when Scope Changed
  const PR_SCOPE_CHANGED = { N: 0.85, L: 0.50, H: 0.50 };

  function renderGrid(metrics, containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = "";
    metrics.forEach(m => {
      const card = document.createElement("div");
      card.className = "cvss-metric-card";
      card.innerHTML = `
        <div class="cvss-metric-title">${m.label}</div>
        <div class="cvss-metric-name">${m.name}</div>
        <div style="font-size:10.5px;color:var(--muted);margin-bottom:8px">${m.desc}</div>
        <div class="cvss-opts">
          ${m.opts.map(o => `
            <button class="cvss-opt-btn" data-metric="${m.id}" data-val="${o.v}" data-color="${o.color}"
              style="${selected[m.id] === o.v ? `background:${o.color}22;color:${o.color};border-color:${o.color};font-weight:700` : ""}"
              onclick="cvssSelect('${m.id}','${o.v}','${o.color}',this)">
              ${o.label}&nbsp;<span style="opacity:.6;font-size:9px">(${o.v})</span>
            </button>`).join("")}
        </div>`;
      container.appendChild(card);
    });
  }

  window.cvssSelect = function(metric, val, color, btn) {
    selected[metric] = val;
    // Deselect siblings
    btn.closest(".cvss-opts").querySelectorAll(".cvss-opt-btn").forEach(b => {
      b.style.background = "";
      b.style.color = "";
      b.style.borderColor = "";
      b.style.fontWeight = "";
    });
    btn.style.background = color + "22";
    btn.style.color = color;
    btn.style.borderColor = color;
    btn.style.fontWeight = "700";
    calculateScore();
  };

  function calculateScore() {
    const { AV, AC, PR, UI, S, C, I, A } = selected;
    if (!AV || !AC || !PR || !UI || !S || !C || !I || !A) {
      document.getElementById("cvss-score-num").textContent = "—";
      document.getElementById("cvss-score-num").style.color = "#94a3b8";
      document.getElementById("cvss-score-label").textContent = "Select all metrics";
      return;
    }

    // Get raw values
    const avVal = exploitMetrics[0].opts.find(o => o.v === AV).score;
    const acVal = exploitMetrics[1].opts.find(o => o.v === AC).score;
    const scopeChanged = S === "C";
    const prRaw = exploitMetrics[2].opts.find(o => o.v === PR).score;
    const prVal = scopeChanged ? PR_SCOPE_CHANGED[PR] : prRaw;
    const uiVal = exploitMetrics[3].opts.find(o => o.v === UI).score;
    const cVal = impactMetrics[0].opts.find(o => o.v === C).score;
    const iVal = impactMetrics[1].opts.find(o => o.v === I).score;
    const aVal = impactMetrics[2].opts.find(o => o.v === A).score;

    // ISS
    const ISS = 1 - (1 - cVal) * (1 - iVal) * (1 - aVal);
    // Impact sub score
    let Impact;
    if (scopeChanged) {
      Impact = 7.52 * (ISS - 0.029) - 3.25 * Math.pow(ISS - 0.02, 15);
    } else {
      Impact = 6.42 * ISS;
    }
    // Exploitability sub score
    const Exploitability = 8.22 * avVal * acVal * prVal * uiVal;
    // Base score
    let base = 0;
    if (Impact <= 0) {
      base = 0;
    } else if (scopeChanged) {
      base = Math.min(1.08 * (Impact + Exploitability), 10);
    } else {
      base = Math.min(Impact + Exploitability, 10);
    }
    // Ceiling to 1 decimal
    base = Math.ceil(base * 10) / 10;

    // Severity
    let severity = "None", sColor = "#94a3b8";
    if (base >= 9.0)      { severity = "Critical"; sColor = "#ef4444"; }
    else if (base >= 7.0) { severity = "High";     sColor = "#f97316"; }
    else if (base >= 4.0) { severity = "Medium";   sColor = "#eab308"; }
    else if (base >= 0.1) { severity = "Low";      sColor = "#22c55e"; }
    else                  { severity = "None";     sColor = "#94a3b8"; }

    document.getElementById("cvss-score-num").textContent = base.toFixed(1);
    document.getElementById("cvss-score-num").style.color = sColor;
    document.getElementById("cvss-score-label").textContent = severity + " Severity";
    document.getElementById("cvss-score-bar").style.borderColor = sColor + "55";

    // Vector string
    document.getElementById("cvss-vector").textContent =
      `CVSS:3.1/AV:${AV}/AC:${AC}/PR:${PR}/UI:${UI}/S:${S}/C:${C}/I:${I}/A:${A}`;
  }

  function init() {
    const eGrid = document.getElementById("cvss-exploit-grid");
    const iGrid = document.getElementById("cvss-impact-grid");
    if (!eGrid || !iGrid) return;
    renderGrid(exploitMetrics, "cvss-exploit-grid");
    renderGrid(impactMetrics, "cvss-impact-grid");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
