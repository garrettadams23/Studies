/**
 * script.js  —  CompTIA & Tech Reference  |  2026 Edition
 * =========================================================
 * hydrateDomain / openDomain / toggleDomain / toggleTopic / filter / toggleAll
 * toggleTheme / updateThemeUI
 * initSnapQuote / initCloudStack / initTouchFeedback
 * URL codec helpers
 *
 * One domain's content is in the document at a time. Read the DEFERRED DOMAIN
 * CONTENT section before changing anything that walks .topic — the rule is that
 * *which* topics exist comes from topicIndex(), and *what they say* comes from
 * domainTopics(); neither may come from querySelectorAll across the page.
 */

// ── STATE ──────────────────────────────────────────────────────────────────
let allExpanded = false;

// Storage is not always available: blocked cookies, a hardened browser, or
// Safari private mode make `localStorage` throw on access. Most call sites below
// already guard it inline; these helpers cover the rest so a storage failure
// degrades one feature instead of throwing — which, at the load-time theme IIFE,
// would halt the whole script and leave the page inert.
const safeLS = {
  get(k)    { try { return localStorage.getItem(k); } catch { return null; } },
  set(k, v) { try { localStorage.setItem(k, v); } catch { /* blocked or full */ } },
  remove(k) { try { localStorage.removeItem(k); } catch { /* blocked */ } },
  // The key enumeration is its own hazard: `localStorage.length` and `.key(i)`
  // throw when storage is blocked, so a `for (…length…)` loop throws at the bound
  // before any per-item guard can run. This returns [] instead.
  keys()    {
    try {
      const out = [];
      for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (k) out.push(k); }
      return out;
    } catch { return []; }
  },
};
// sessionStorage throws in exactly the same cases; the notepad is its only user.
const safeSS = {
  get(k)    { try { return sessionStorage.getItem(k); } catch { return null; } },
  set(k, v) { try { sessionStorage.setItem(k, v); } catch { /* blocked or full */ } },
};

const QUOTES = [
  "What stands in the way becomes the way. — Marcus Aurelius, Meditations 5.20",
  "The unexamined life is not worth living. — Socrates, in Plato's Apology",
  "Simplicity is the ultimate sophistication. — widely quoted, source unknown",
  "He who has a why can bear almost any how. — Nietzsche",
  "The Tao that can be told is not the eternal Tao. — Lao Tzu",
  "One must imagine Sisyphus happy. — Camus, The Myth of Sisyphus",
  "We suffer more often in imagination than in reality. — Seneca, Letters 13",
  "Before enlightenment, chop wood, carry water. — Zen proverb",
  "You have power over your mind, not outside events. — Marcus Aurelius",
  "The quieter you become, the more you can hear. — Ram Dass",
  "Amor fati — love your fate. — Nietzsche",
  "Water is the softest thing, yet it overcomes the hardest. — Lao Tzu",
  "Know thyself. — inscribed at Delphi",
  "Security comes not from having things, but from releasing the need to control. — Epictetus",
  "In the middle of difficulty lies opportunity. — widely quoted, source unknown",
  "Do not seek to have events happen as you want them to, but want them to happen as they do. — Epictetus, Enchiridion 8",
  "Peace comes from within. Do not seek it without. — modern aphorism",
  "The present moment always will have been. — Marcus Aurelius"
];

// ── DEFERRED DOMAIN CONTENT ────────────────────────────────────────────────
// Every domain's header is in the document. No domain's content is: build.py
// parks each body in an inert `<script type="text/html">` beside its section,
// which the parser keeps as a single text node — no elements, no style
// resolution, no layout. Opening a domain moves that text into `.domain-body`;
// opening another empties the first. The document therefore holds the shell
// plus at most one domain, which is what took the page from 92,330 elements at
// load to 484.
//
// Two rules keep the rest of the file honest about content it cannot see:
//
//   1. Which topics exist  → topicIndex(), the id map build.py inlines. The
//      progress badges, the random pick and `#slug` routing all need to answer
//      for 29 domains, 28 of which have nothing in the DOM.
//   2. What a topic says   → domainTopics(), which parses one domain's deferred
//      text once and caches it. Search and the study decks read that, never the
//      live DOM, so they cover the whole page exactly as before.
//
// Anything that reaches for `document.querySelectorAll(".topic")` instead is
// asking about the one open domain, and will quietly answer for a 29th of the
// page. That is the failure mode to watch for here.

/** domain id -> its topic ids, in page order (inlined by build.py). */
let _topicIndex = null;
function topicIndex() {
  if (_topicIndex) return _topicIndex;
  const el = document.getElementById("topic-index");
  try {
    const o = el ? JSON.parse(el.textContent) : {};
    _topicIndex = (o && typeof o === "object" && !Array.isArray(o)) ? o : {};
  } catch { _topicIndex = {}; }
  return _topicIndex;
}

/** topic id -> the domain that owns it, so a permalink can find its section. */
let _topicOwner = null;
function topicDomain(id) {
  if (!_topicOwner) {
    _topicOwner = new Map();
    Object.keys(topicIndex()).forEach(d => topicIndex()[d].forEach(t => _topicOwner.set(t, d)));
  }
  return _topicOwner.get(id) || null;
}

function allTopicIds() {
  return Object.keys(topicIndex()).reduce((all, d) => all.concat(topicIndex()[d]), []);
}

/** Cached domain sections — the headers are static, so this never goes stale. */
let _domainSections = null;
function domainSections() {
  if (!_domainSections) _domainSections = [...document.querySelectorAll(".domain-section")];
  return _domainSections;
}

function domainSection(id) {
  return domainSections().find(s => s.dataset.domain === id) || null;
}

/** The one domain whose content is currently in the document, or null. */
let _liveDomain = null;

function isHydrated(section) { return !!section && section.dataset.hydrated === "1"; }

/**
 * Move a domain's deferred content into its body, evicting whichever domain
 * was there. Everything the outgoing domain owned goes with it — topic
 * elements, the injected tool buttons, any search highlights — because every
 * piece of state worth keeping lives in localStorage or in topicIndex(), not in
 * those nodes.
 */
function hydrateDomain(section) {
  if (!section || isHydrated(section)) return false;
  const src = section.querySelector("script.domain-src");
  const body = section.querySelector(".domain-body");
  if (!src || !body) return false;
  if (_liveDomain && _liveDomain !== section) dehydrateDomain(_liveDomain);
  body.innerHTML = src.textContent;
  section.dataset.hydrated = "1";
  _liveDomain = section;
  enhanceDomain(section);
  renderDomainIntro(section);
  return true;
}

/** domain id -> its landing card (inlined by build.py from data/domain-intros.json). */
let _domainIntros = null;
function domainIntros() {
  if (_domainIntros) return _domainIntros;
  const el = document.getElementById("domain-intros");
  try {
    const o = el ? JSON.parse(el.textContent) : {};
    _domainIntros = (o && typeof o === "object" && !Array.isArray(o)) ? o : {};
  } catch { _domainIntros = {}; }
  return _domainIntros;
}

/** domain id -> {month, topics}: what was reviewed here most recently. */
let _changelog = null;
function changelog() {
  if (_changelog) return _changelog;
  const el = document.getElementById("changelog");
  try {
    const o = el ? JSON.parse(el.textContent) : {};
    _changelog = (o && typeof o === "object" && !Array.isArray(o)) ? o : {};
  } catch { _changelog = {}; }
  return _changelog;
}

/** "August 2026" from "2026-08". Falls back to the raw value rather than NaN. */
const MONTHS = ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"];
function monthLabel(ym) {
  const m = /^(\d{4})-(\d{2})$/.exec(ym || "");
  if (!m) return ym || "";
  const n = Number(m[2]);
  return (n >= 1 && n <= 12) ? `${MONTHS[n - 1]} ${m[1]}` : ym;
}

/**
 * Put a domain's landing card above its topics: what it covers, who it is for,
 * three topics to start with, and where to go next.
 *
 * The card is data rather than a `.topic` in the content file, and that is the
 * whole point — a signpost should not be counted by the topic index, dated by
 * stamp_freshness.py, offered by the random pick or dealt into a study deck.
 *
 * The "start here" entries are stored as topic *names* and resolved here
 * against the domain's own parsed topics. A name that no longer resolves is
 * dropped rather than rendered dead, so renaming a topic costs the card one
 * link instead of leaving a button that goes nowhere.
 */
function renderDomainIntro(section) {
  const body = section?.querySelector(".domain-body");
  const intro = domainIntros()[section?.dataset.domain];
  if (!body || !intro || body.querySelector(":scope > .domain-intro")) return;

  const byName = new Map();
  domainTopics(section.dataset.domain).forEach(t => {
    if (t.name && t.id && !byName.has(t.name)) byName.set(t.name, t.id);
  });

  const card = document.createElement("div");
  card.className = "domain-intro";

  const add = (cls, label, text) => {
    if (!text) return;
    const row = document.createElement("div");
    row.className = "di-row " + cls;
    const l = document.createElement("span");
    l.className = "di-label";
    l.textContent = label;
    const v = document.createElement("span");
    v.className = "di-text";
    v.textContent = text;
    row.append(l, v);
    card.append(row);
  };

  add("di-covers", "Covers", intro.covers);
  add("di-who", "For", intro.who);

  const starts = (intro.start || []).filter(n => byName.has(n));
  if (starts.length) {
    const row = document.createElement("div");
    row.className = "di-row di-start";
    const l = document.createElement("span");
    l.className = "di-label";
    l.textContent = "Start here";
    const list = document.createElement("span");
    list.className = "di-text di-links";
    starts.forEach(name => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "di-link";
      b.textContent = name;
      b.addEventListener("click", () => stGoToTopic(byName.get(name)));
      list.append(b);
    });
    row.append(l, list);
    card.append(row);
  }

  add("di-next", "Then", intro.next);

  // "Is anyone still maintaining this?" — answered from the freshness stamps
  // rather than left to be guessed at from the writing style.
  const log = changelog()[section.dataset.domain];
  const rows = domainTopics(section.dataset.domain);
  const recent = (log?.topics || [])
    .map(id => rows.find(t => t.id === id))
    .filter(Boolean);
  if (log?.month) {
    const row = document.createElement("div");
    row.className = "di-row di-updated";
    const l = document.createElement("span");
    l.className = "di-label";
    l.textContent = "Updated";
    const v = document.createElement("span");
    v.className = "di-text di-links";
    const when = document.createElement("span");
    when.className = "di-when";
    when.textContent = monthLabel(log.month);
    v.append(when);
    recent.forEach(t => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "di-link";
      b.textContent = t.name;
      b.addEventListener("click", () => stGoToTopic(t.id));
      v.append(b);
    });
    row.append(l, v);
    card.append(row);
  }

  body.prepend(card);
}

// ── PER-TOPIC NOTES ─────────────────────────────────────────────────────────
// One note per topic, stored under `note:<id>`, shown at the top of the topic's
// body whenever that topic is open. Separate from the notepad, which is a
// single shared scratchpad: a note about Kerberos delegation belongs on the
// Kerberos card, not in a pile with everything else.
//
// It is deliberately the same shape as the other per-topic state — a prefixed
// key holding a plain string — so the export, the import's validation and the
// "what do we own" list all pick it up by the rule they already have.

function topicNote(id) {
  try { return localStorage.getItem(NOTE_PREFIX + id) || ""; } catch { return ""; }
}

function saveTopicNote(id, text) {
  const value = (text || "").slice(0, NOTE_MAX).trim();
  try {
    if (value) { localStorage.setItem(NOTE_PREFIX + id, value); streakTouch(); }
    else localStorage.removeItem(NOTE_PREFIX + id);
  } catch { /* quota — the note stays on screen, just unsaved */ }
  document.getElementById(id)?.classList.toggle("noted", !!value);
  return value;
}

/**
 * Render the note block into a topic body, or update it in place.
 *
 * `open` forces the editor open — what the 📝 button does. Without it the block
 * only appears when there is a note to show, so a topic nobody has annotated
 * looks exactly as it did before this feature existed.
 */
function renderTopicNote(topic, { open = false } = {}) {
  if (!topic) return null;
  const body = topic.querySelector(":scope > .topic-body");
  if (!body) return null;
  const existing = body.querySelector(":scope > .topic-note");
  const text = topicNote(topic.id);
  if (!text && !open) { existing?.remove(); return null; }

  let block = existing;
  if (!block) {
    block = document.createElement("div");
    block.className = "topic-note";
    block.innerHTML =
      '<div class="tn-head"><span class="tn-label">My note</span>' +
      '<button type="button" class="tn-edit">Edit</button>' +
      '<button type="button" class="tn-clear" hidden>Delete</button></div>' +
      '<div class="tn-text"></div>' +
      '<textarea class="tn-input" rows="3" maxlength="' + NOTE_MAX +
      '" placeholder="A note only you see. Stored in this browser, and included in your progress export."></textarea>';
    body.prepend(block);

    const input = block.querySelector(".tn-input");
    const commit = () => {
      const saved = saveTopicNote(topic.id, input.value);
      block.querySelector(".tn-text").textContent = saved;
      setEditing(false);
      if (!saved) block.remove();
    };
    block.querySelector(".tn-edit").addEventListener("click", () => setEditing(true));
    block.querySelector(".tn-clear").addEventListener("click", () => {
      input.value = ""; commit();
    });
    input.addEventListener("blur", commit);
    input.addEventListener("keydown", e => {
      // Escape abandons the edit; the note on screen is the saved one.
      if (e.key === "Escape") { input.value = topicNote(topic.id); commit(); }
    });

    function setEditing(on) {
      block.classList.toggle("editing", on);
      block.querySelector(".tn-text").hidden = on;
      block.querySelector(".tn-clear").hidden = !on;
      input.hidden = !on;
      if (on) { input.focus(); input.setSelectionRange(input.value.length, input.value.length); }
    }
    block._setEditing = setEditing;
    setEditing(false);
  }

  block.querySelector(".tn-text").textContent = text;
  block.querySelector(".tn-input").value = text;
  if (open) block._setEditing(true);
  return block;
}

/** The 📝 button: open the topic if it is closed, then focus the editor. */
function toggleTopicNote(topic) {
  const header = topic.querySelector(":scope > .topic-header");
  const body = topic.querySelector(":scope > .topic-body");
  if (body && !body.classList.contains("open")) {
    setTopicOpen(header, true);
    renderSeeAlso(topic);
  }
  renderTopicNote(topic, { open: true });
}

/** topic id -> ids worth reading next (inlined by build.py from data/related.json).
 *
 * The payload is index-encoded — {ids: [slug, …], adj: [[i, …], …]} — because
 * slugs average 48 characters and each one would otherwise be repeated on
 * every edge pointing at it. Decoding once here keeps every caller working
 * with plain slugs. An older page cached by the service worker may still hold
 * the flat {slug: [slug, …]} form, so both are accepted. */
let _related = null;
function relatedTopics() {
  if (_related) return _related;
  const el = document.getElementById("related-topics");
  try {
    const o = el ? JSON.parse(el.textContent) : {};
    if (o && Array.isArray(o.ids) && Array.isArray(o.adj)) {
      const out = {};
      o.ids.forEach((slug, i) => {
        const links = (o.adj[i] || []).map(j => o.ids[j]).filter(Boolean);
        if (links.length) out[slug] = links;
      });
      _related = out;
    } else {
      _related = (o && typeof o === "object" && !Array.isArray(o)) ? o : {};
    }
  } catch { _related = {}; }
  return _related;
}

/** A topic id -> its title as written, without parsing every domain. */
function topicName(id) {
  const d = topicDomain(id);
  if (!d) return null;
  return domainTopics(d).find(t => t.id === id)?.name || null;
}

/**
 * Append the "See also" strip to a topic, once, the first time it is opened.
 *
 * Rendered on open rather than at hydration because a domain is dozens of
 * topics and a reader opens two or three: doing it here spends the work on the
 * cards actually read, and it is where the target titles are resolved, which
 * costs a parse of whichever *other* domain a link points into.
 *
 * An id that no longer resolves is dropped and a strip with nothing left in it
 * is not rendered at all — deleting a topic must not leave dead links on
 * everything that referenced it.
 */
function renderSeeAlso(topic) {
  if (!topic || topic.dataset.seeAlso === "1") return;
  topic.dataset.seeAlso = "1";
  const body = topic.querySelector(":scope > .topic-body");
  const ids = relatedTopics()[topic.id];
  if (!body || !Array.isArray(ids) || !ids.length) return;

  const rows = ids
    .map(id => ({ id, name: topicName(id), domain: topicDomain(id) }))
    .filter(r => r.name);
  if (!rows.length) return;

  const strip = document.createElement("div");
  strip.className = "see-also";
  const label = document.createElement("span");
  label.className = "sa-label";
  label.textContent = "See also";
  strip.append(label);
  rows.forEach(r => {
    const b = document.createElement("button");
    b.type = "button";
    b.className = "sa-link";
    b.textContent = r.name;
    // The domain is worth showing: half these links leave the domain the
    // reader is in, and following one without knowing that is disorienting.
    if (r.domain && r.domain !== topic.closest(".domain-section")?.dataset.domain) {
      const tag = document.createElement("span");
      tag.className = "sa-domain";
      tag.textContent = r.domain;
      b.append(" ", tag);
    }
    b.addEventListener("click", () => stGoToTopic(r.id));
    strip.append(b);
  });
  body.append(strip);
}

/** Empty a domain's body and collapse it. Its content stays in the page as text. */
function dehydrateDomain(section) {
  if (!isHydrated(section)) return;
  const body = section.querySelector(".domain-body");
  const header = section.querySelector(".domain-header");
  body.classList.remove("open");
  body.textContent = "";
  delete section.dataset.hydrated;
  header?.classList.remove("open");
  header?.setAttribute("aria-expanded", "false");
  if (_liveDomain === section) _liveDomain = null;
  // The <mark> wrappers went with the nodes; the set that tracked them must not
  // outlive them or clearHighlights() would walk detached elements.
  _highlighted.clear();
}

/** Open a domain — hydrating it, and closing whichever one was open. */
function openDomain(section, opts = {}) {
  if (!section) return;
  const header = section.querySelector(".domain-header");
  const body = section.querySelector(".domain-body");
  hydrateDomain(section);
  body.classList.add("open");
  header.classList.add("open");
  header.setAttribute("aria-expanded", "true");
  // A domain opened while a search is running shows that search's result, not
  // its whole self — otherwise the chips and the search disagree about what the
  // page is showing.
  if (_searchTerm) applySearchToDomain(section);
  if (opts.scroll) header.scrollIntoView({ behavior: "smooth", block: "start" });
}

function closeDomain(section) { dehydrateDomain(section); }

/**
 * Per-topic setup for a domain that has just arrived in the DOM: the a11y
 * attributes, stored progress, and the ★ ✓ 🔗 tool cluster. This used to run
 * once at load over all 1,080 topics; it now runs over the few dozen in one
 * domain, on open.
 */
function enhanceDomain(section) {
  const ids = topicIndex()[section.dataset.domain] || [];
  section.querySelectorAll(".topic").forEach((topic, i) => {
    // build.py stamps the ids. The fallback is for a hand-built fragment (a
    // patch script, a test page) that never went through it.
    if (!topic.id) topic.id = ids[i] || slugify(labelText(topic.querySelector(".topic-name")));
    const header = topic.querySelector(":scope > .topic-header");
    if (!header) return;
    // The header used to be role="button" and also contained the ★ ✓ 📝 🔗
    // buttons — a control nested inside a control, which is invalid ARIA and
    // leaves those four unreachable or ambiguous to a screen reader. The
    // clickable part is now a real <button> wrapping the icon, name, badge and
    // chevron; the tools are its siblings. The header keeps the layout and no
    // longer claims to be interactive itself.
    let toggle = header.querySelector(":scope > .topic-toggle");
    if (!toggle) {
      toggle = document.createElement("button");
      toggle.type = "button";
      toggle.className = "topic-toggle";
      // Everything except the chevron. The chevron stays a sibling so the row
      // keeps its original order — name, tools, chevron — and because a
      // decorative arrow does not belong inside the button's accessible name.
      const chev = header.querySelector(":scope > .topic-chev");
      chev?.setAttribute("aria-hidden", "true");
      [...header.childNodes].forEach(n => { if (n !== chev) toggle.appendChild(n); });
      chev ? header.insertBefore(toggle, chev) : header.appendChild(toggle);
    }
    header.removeAttribute("tabindex");
    header.removeAttribute("role");
    header.removeAttribute("aria-expanded");
    toggle.setAttribute("aria-expanded", header.classList.contains("open") ? "true" : "false");

    if (safeLS.get(REVIEWED_PREFIX + topic.id) === "1") topic.classList.add("reviewed");
    if (safeLS.get(BOOKMARK_PREFIX + topic.id) === "1") topic.classList.add("bookmarked");
    if (safeLS.get(NOTE_PREFIX + topic.id)) topic.classList.add("noted");

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

      const note = document.createElement("button");
      note.type = "button";
      note.className = "topic-note-btn";
      note.title = "Note on this topic";
      note.setAttribute("aria-label", "Write a note on this topic");
      note.textContent = "📝";

      tools.append(bookmark, review, note, link);
      const chev = header.querySelector(":scope > .topic-chev");
      chev ? header.insertBefore(tools, chev) : header.appendChild(tools);
    }
  });

  // Widgets that live inside a topic and used to be wired at load. The codec's
  // buttons are handled by delegation on the container; only the matrix builds
  // DOM of its own, and only when its host arrives.
  initCloudStack();
  updateDomainProgress(section);
}

// ── DEFERRED CONTENT INDEX ─────────────────────────────────────────────────
// What search and the study decks read instead of the DOM. Parsing markup with
// regexes is a poor general idea and a good specific one here: the shapes are
// generated by build.py from data/*.html, tools/lint_content.py already holds
// the same patterns in Python, and the alternative — DOMParser — rebuilds the
// 90,000 elements this whole change exists to avoid.

const TOPIC_OPEN = '<div class="topic"';
const RE_TOPIC_ID = /\bid="([^"]+)"/;
/**
 * The opening tag of an element carrying one class, whatever else it carries.
 *
 * Both halves of that matter and both were got wrong first time. Any element:
 * a concept title is a <div> 2,263 times and an <h4> 342 times, and pinning the
 * tag indexed the <h4> ones as empty. Whatever else: `class="concept-desc
 * verdict"` is still a description, and requiring an exact attribute skipped
 * the modifier'd ones — quietly, and only on some cards.
 */
const classRe = cls =>
  new RegExp(`<[a-zA-Z][\\w-]*\\b[^>]*class="(?:[^"]*\\s)?${cls}(?:\\s[^"]*)?"[^>]*>`);

const RE_TOPIC_NAME = classRe("topic-name");
const RE_TOPIC_BADGE = classRe("topic-badge");
const RE_CONCEPT_TITLE = classRe("concept-title");
const RE_CONCEPT_DESC = classRe("concept-desc");
const RE_ACRO_SPAN = /<span class="acro-exp">\([^<]*?\)<\/span\s*>/g;

/**
 * The contents of the first element matching `open`, counting nesting.
 *
 * The lazy `(.*?)</span>` version of this is wrong on exactly the markup that
 * matters: a topic name carrying an inline acronym expansion ends at the
 * *expansion's* closing tag, so "OSI Model — 7 Layers" indexes as
 * "OSI (Open Systems Interconnection)" and every deck and jump list shows that.
 */
function firstInner(html, open) {
  const m = open.exec(html);
  if (!m) return "";
  const tag = /^<([a-zA-Z][\w-]*)/.exec(m[0])[1];
  const openTag = `<${tag}`, closeTag = `</${tag}`;
  const start = m.index + m[0].length;
  let depth = 1, i = start;
  while (depth > 0) {
    const c = html.indexOf(closeTag, i);
    if (c === -1) return html.slice(start);
    const o = html.indexOf(openTag, i);
    if (o !== -1 && o < c) { depth++; i = o + openTag.length; continue; }
    depth--;
    if (!depth) return html.slice(start, c);
    i = c + closeTag.length;
  }
  return "";
}

// Entity decoding, by table rather than by parser. The obvious version assigns
// to a detached <textarea>'s innerHTML and reads .value back, which is correct
// for every entity that exists — and cost 1,167 ms of the 1,652 ms it took to
// index the page, because each call is a parser round trip. The table covers
// every named entity data/*.html actually contains (`grep -o '&[a-z]*;'` finds
// nine) plus a few likely neighbours; numeric refs are handled generically, and
// anything else is left as written — it would read as `&hellip;` in a deck,
// which is wrong but visible, rather than breaking the parse.
const ENTITIES = {
  "&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"', "&#39;": "'",
  "&nbsp;": " ", "&bull;": "\u2022", "&middot;": "\u00b7",
  "&times;": "\u00d7", "&ge;": "\u2265", "&le;": "\u2264", "&mdash;": "\u2014",
};
const RE_ENTITY = /&(?:#(\d+)|#[xX]([0-9a-fA-F]+)|[a-zA-Z][a-zA-Z0-9]*);/g;

function decodeEntities(s) {
  if (!s || s.indexOf("&") === -1) return s;
  return s.replace(RE_ENTITY, (whole, dec, hex) => {
    if (dec) return String.fromCodePoint(+dec);
    if (hex) return String.fromCodePoint(parseInt(hex, 16));
    return ENTITIES[whole] !== undefined ? ENTITIES[whole] : whole;
  });
}

// A tag, by the parser's rule: `<` then a letter (or `</`). `<[^>]+>` looks
// equivalent and is not — `WHERE created_at < now()` inside a code block has a
// `>` somewhere after it, so the loose pattern swallows the comparison operator
// and everything up to it. The browser does not, because `< ` cannot open a tag.
const RE_TAG = /<\/?[a-zA-Z][^>]*>|<!--[\s\S]*?-->/g;
const RE_WS = /\s+/g;

/** Markup -> the text a reader sees, whitespace collapsed.
 *
 * Tags become nothing, not a space. That looks like the more dangerous choice
 * and is the correct one: it is what textContent does, and the source already
 * carries a newline between anything that needs separating. Replacing them with
 * a space instead put one inside every inline acronym expansion —
 * `CIDR ( Classless Inter-Domain Routing )` — which is not what the card says
 * and so is not what a search for it should have to match.
 */
function plainText(html) {
  return decodeEntities(html.replace(RE_TAG, "").replace(RE_WS, " ")).trim();
}

/** Same, with the inline acronym expansions dropped — the title as written. */
function plainLabel(html) {
  return plainText(html.replace(RE_ACRO_SPAN, ""));
}

const RE_TOPIC_READ = /<span class="topic-read"[^>]*>.*?<\/span>/gi;
const RE_TOPIC_LEVEL = /data-level="([a-z]+)"/;
const RE_TOPIC_REVIEWED = /data-reviewed="(\d{4}-\d{2})"/;

const _domainTopics = new Map();

/**
 * One domain's topics, parsed from its deferred block: id, the fields the decks
 * show, and the lowercased full text search matches on. Cached — the content
 * never changes — and warmed in idle time after load, so the first search does
 * not pay for the parse.
 */
function domainTopics(domainId) {
  const cached = _domainTopics.get(domainId);
  if (cached) return cached;

  const rows = [];
  const src = domainSection(domainId)?.querySelector("script.domain-src");
  const html = src ? src.textContent : "";
  let start = html.indexOf(TOPIC_OPEN);
  while (start !== -1) {
    const next = html.indexOf(TOPIC_OPEN, start + TOPIC_OPEN.length);
    const chunk = html.slice(start, next === -1 ? html.length : next);
    const openTag = chunk.slice(0, chunk.indexOf(">") + 1);
    rows.push({
      id: (RE_TOPIC_ID.exec(openTag) || ["", ""])[1],
      level: (RE_TOPIC_LEVEL.exec(openTag) || ["", "core"])[1],
      reviewed: (RE_TOPIC_REVIEWED.exec(openTag) || ["", ""])[1],
      name: plainLabel(firstInner(chunk, RE_TOPIC_NAME)),
      title: plainText(firstInner(chunk, RE_CONCEPT_TITLE)),
      desc: plainText(firstInner(chunk, RE_CONCEPT_DESC)),
      badge: plainText(firstInner(chunk, RE_TOPIC_BADGE)),
      // The build stamps a reading-time span into every header (plan.md T6).
      // It is chrome, not content: leaving it in made "min" match 1,337 of
      // 1,367 topics, which is the same failure the acronym-alternate bug
      // produced and would have been just as invisible.
      text: plainText(chunk.replace(RE_TOPIC_READ, "")).toLowerCase(),
    });
    start = next;
  }
  _domainTopics.set(domainId, rows);
  return rows;
}

/**
 * Parse the deferred blocks during idle time, one domain per callback.
 *
 * Without this the first search would parse all 29 at once — the one moment the
 * user is waiting on a keystroke. With it the work is done before they type,
 * and it never competes with the first paint.
 */
function warmContentIndex() {
  const queue = Object.keys(topicIndex()).filter(d => !_domainTopics.has(d));
  if (!queue.length) return;
  const idle = window.requestIdleCallback
    ? window.requestIdleCallback.bind(window)
    : (fn => setTimeout(() => fn({ timeRemaining: () => 0 }), 80));
  const step = deadline => {
    do { domainTopics(queue.shift()); } while (queue.length && deadline.timeRemaining() > 8);
    if (queue.length) idle(step, { timeout: 3000 });
  };
  idle(step, { timeout: 3000 });
}

// ── ACCORDION ──────────────────────────────────────────────────────────────
function toggleDomain(h) {
  const section = h.closest(".domain-section");
  if (!section) return;
  section.querySelector(".domain-body").classList.contains("open")
    ? closeDomain(section)
    : openDomain(section);
}

/** The element carrying a topic's expanded state — its toggle button. */
function topicToggle(header) {
  return header?.querySelector(":scope > .topic-toggle") || header;
}

/** Set a topic's open state in one place: the header class, the body, the aria. */
function setTopicOpen(header, open) {
  if (!header) return;
  header.classList.toggle("open", open);
  header.parentElement?.querySelector(":scope > .topic-body")?.classList.toggle("open", open);
  topicToggle(header).setAttribute("aria-expanded", open ? "true" : "false");
}

function toggleTopic(h) {
  const header = h.classList?.contains("topic-toggle") ? h.parentElement : h;
  const open = !header.classList.contains("open");
  setTopicOpen(header, open);
  if (open) {
    renderSeeAlso(header.parentElement);
    renderTopicNote(header.parentElement);
    updateTopicHash(header.parentElement);
  }
}

// ── FILTER ─────────────────────────────────────────────────────────────────
function filter(domain, chip) {
  document.querySelectorAll(".chip").forEach(c => c.classList.remove("active"));
  chip.classList.add("active");
  domainSections().forEach(s => {
    s.classList.toggle("hidden", domain !== "all" && s.dataset.domain !== domain);
  });
  // Narrowing to a single domain is a request to read it, and it is the only
  // one on screen — so open it. ALL leaves whatever is open open; closing it
  // would throw away the reader's place for no reason.
  if (domain !== "all") openDomain(domainSection(domain));
}

// ── EXPAND / COLLAPSE ALL ──────────────────────────────────────────────────
// Scoped to the open domain, because that is the only content there is. The
// old whole-page version would have to build all 29 domains to expand them —
// the exact thing a reader pressing "expand" is not asking for.
function toggleAll() {
  allExpanded = !allExpanded;
  let section = _liveDomain;
  if (allExpanded && !section) {
    section = domainSections().find(s =>
      !s.classList.contains("hidden") && !s.classList.contains("search-hidden"));
    if (section) openDomain(section);
  }
  if (section) {
    section.querySelectorAll(".topic-header").forEach(h => setTopicOpen(h, allExpanded));
    if (!allExpanded) closeDomain(section);
  } else {
    allExpanded = false;
  }
  const hdrBtn = document.getElementById("hdr-expand-btn");
  if (hdrBtn) {
    hdrBtn.title = allExpanded ? "Collapse the open domain" : "Expand the open domain";
    hdrBtn.setAttribute("aria-checked", allExpanded ? "true" : "false");
  }
}

// ── THEME ──────────────────────────────────────────────────────────────────
function toggleTheme() {
  const doc  = document.documentElement;
  const next = doc.getAttribute("data-theme") === "light" ? "dark" : "light";
  doc.setAttribute("data-theme", next);
  safeLS.set("theme", next);
  updateThemeUI(next);
}

function updateThemeUI(theme) {
  const btn = document.getElementById("hdr-theme-btn");
  if (btn) btn.setAttribute("aria-checked", theme === "light" ? "true" : "false");
}

// ── INIT THEME (prevent flash) ─────────────────────────────────────────────
(function () {
  const saved = safeLS.get("theme") || "dark";
  document.documentElement.setAttribute("data-theme", saved);
})();

// ── DOM READY ──────────────────────────────────────────────────────────────

// ── WHAT'S NEW SINCE YOUR LAST VISIT ────────────────────────────────────────
// plan.md Phase 10 T8. The changelog answers "what changed"; this answers "what
// changed *for me*", which is the question people actually have. No new data:
// every topic already carries `data-reviewed`, and the reader's side is one
// month string in localStorage.
const SEEN_KEY = "seen-through";

/** The newest freshness stamp anywhere on the site, or "" if there are none. */
function newestReviewedMonth() {
  let newest = "";
  Object.keys(topicIndex()).forEach(d => {
    domainTopics(d).forEach(t => { if (t.reviewed > newest) newest = t.reviewed; });
  });
  return newest;
}

function countUpdatedSince(month) {
  let n = 0;
  Object.keys(topicIndex()).forEach(d => {
    domainTopics(d).forEach(t => { if (t.reviewed && t.reviewed > month) n++; });
  });
  return n;
}

/**
 * Show the banner, or silently record where a first-time reader is starting.
 *
 * A reader with nothing stored is **not** told that 1,426 topics are new —
 * they are all new, the statement is useless, and it would train people to
 * dismiss the banner before it ever says anything. Their first visit just
 * records the newest month and shows nothing.
 */
function initWhatsNew() {
  const bar = document.getElementById("whatsnew");
  if (!bar) return;
  const newest = newestReviewedMonth();
  if (!newest) return;

  let seen = null;
  try { seen = localStorage.getItem(SEEN_KEY); } catch { return; }
  const markSeen = () => {
    try { localStorage.setItem(SEEN_KEY, newest); } catch { /* full or blocked */ }
  };
  if (!seen || !/^\d{4}-\d{2}$/.test(seen)) { markSeen(); return; }

  const n = countUpdatedSince(seen);
  if (!n) return;

  document.getElementById("whatsnew-text").textContent =
    `${n} topic${n === 1 ? "" : "s"} updated since ${monthLabel(seen)}`;
  bar.hidden = false;

  document.getElementById("whatsnew-show")?.addEventListener("click", () => {
    const input = document.getElementById("search-input");
    if (!input) return;
    // Route it through the search box rather than a private code path: the
    // reader can then see the query, edit it, add `domain:` to it, or clear it
    // with Esc like any other search.
    input.value = `since:${seen}`;
    runSearch(input.value);
    input.focus();
  });
  document.getElementById("whatsnew-seen")?.addEventListener("click", () => {
    markSeen();
    bar.hidden = true;
  });
}

document.addEventListener("DOMContentLoaded", () => {
  updateThemeUI(document.documentElement.getAttribute("data-theme"));
  initSnapQuote();
  initCloudStack();
  initTouchFeedback();
  // After the content index is warm enough to answer; it parses on demand, so
  // this is correct at load and costs one pass over the already-parsed rows.
  initWhatsNew();

  // Filter chips — event delegation on the filter bar
  document.querySelector(".filter-bar")?.addEventListener("click", e => {
    const chip = e.target.closest(".chip");
    if (chip) filter(chip.dataset.domain || "all", chip);
  });

  // Accordion — event delegation on the container
  const container = document.getElementById("domain-container");
  container?.addEventListener("click", e => {
    // Per-topic tool buttons take precedence over the toggle
    const tool = e.target.closest(".topic-review, .topic-permalink, .topic-bookmark, .topic-note-btn");
    if (tool) { e.stopPropagation(); handleTopicTool(tool); return; }
    // The URL codec lives inside a topic, so its buttons arrive and leave with
    // their domain — delegation instead of the load-time wiring they had.
    const codec = e.target.closest(".url-codec-btn");
    if (codec) {
      e.stopPropagation();
      if (codec.classList.contains("btn-encode")) urlToolEncode();
      else if (codec.classList.contains("btn-decode")) urlToolDecode();
      else if (codec.classList.contains("btn-copy")) urlToolCopy();
      else if (codec.classList.contains("btn-clear")) urlToolClear();
      return;
    }
    // A concept card's label copies a link to that card. Inside a topic body,
    // so it must be handled before the topic-header toggle below — and it never
    // reaches it anyway, but the ordering states the intent.
    const cardLabel = e.target.closest(".concept-label");
    if (cardLabel) { e.stopPropagation(); copyCardLink(cardLabel); return; }
    // A cross-reference build.py resolved to an id. Inert spans — a title that
    // no longer matches a topic — fall through and stay plain text.
    const xref = e.target.closest(".xref[data-xref]");
    if (xref) { e.stopPropagation(); stGoToTopic(xref.dataset.xref); return; }
    const dh = e.target.closest(".domain-header");
    if (dh) { toggleDomain(dh); return; }
    // The button is the control; the header around it is layout. Clicking the
    // padding either side of the button still toggles, which is what a large
    // touch target is for.
    const tt = e.target.closest(".topic-toggle");
    if (tt) { toggleTopic(tt.parentElement); return; }
    const th = e.target.closest(".topic-header");
    if (th) toggleTopic(th);
  });

  // Accordion — keyboard support (Enter / Space on focused headers)
  container?.addEventListener("keydown", e => {
    if (e.key !== "Enter" && e.key !== " ") return;
    const xref = e.target.closest(".xref[data-xref]");
    if (xref) { e.preventDefault(); stGoToTopic(xref.dataset.xref); return; }
    // A real <button> already fires a click on Enter and Space; handling it
    // here as well toggled the topic twice, which looked like nothing happening.
    if (e.target.closest(".topic-toggle")) return;
    const header = e.target.closest(".domain-header, .topic-header");
    if (!header || e.target.closest(".topic-review, .topic-permalink, .topic-note-btn")) return;
    e.preventDefault();
    header.classList.contains("domain-header") ? toggleDomain(header) : toggleTopic(header);
  });

  // Header control buttons
  document.getElementById("hdr-theme-btn")?.addEventListener("click", toggleTheme);
  document.getElementById("hdr-expand-btn")?.addEventListener("click", toggleAll);
  document.getElementById("hdr-random-btn")?.addEventListener("click", jumpToRandomTopic);
  document.getElementById("hdr-acro-btn")?.addEventListener("click", cycleAcroMode);
  applyAcroMode(acroMode());

  // Search + notepad + URL codec — wired here (not inline) so the CSP can stay
  // script-src 'self' with no 'unsafe-inline'.
  document.getElementById("search-input")?.addEventListener("input", e => onSearchInput(e.target.value));
  document.getElementById("search-clear")?.addEventListener("click", clearSearch);
  document.getElementById("notepad-tab")?.addEventListener("click", toggleNotepad);

  // Global keyboard shortcuts (ignored while typing in a field)
  document.addEventListener("keydown", handleGlobalKeys);

  initAccessibilityAndTools();
  initBackToTop();
  initStudyTools();

  // Parse the deferred domain text in idle time, so the first search and the
  // first deck are instant instead of paying for all 29 domains at once.
  warmContentIndex();
});

// ── ACRONYM EXPANSION DENSITY ────────────────────────────────────────────────
// The inline expansions are the point of the acronym feature, and their one
// real cost is density inside tables. Three modes, a class on <body>, and a
// stored preference — no rebuild, and the annotator is untouched.
const ACRO_MODES = ["always", "hover", "off"];
const ACRO_KEY = "acro-density";

function acroMode() {
  const m = safeLS.get(ACRO_KEY);
  return ACRO_MODES.includes(m) ? m : "always";
}

function applyAcroMode(mode) {
  document.body.classList.remove("acro-hover", "acro-off");
  if (mode !== "always") document.body.classList.add("acro-" + mode);
  const btn = document.getElementById("hdr-acro-btn");
  const label = document.getElementById("hdr-acro-label");
  if (label) label.textContent = mode.toUpperCase();
  if (btn) {
    btn.setAttribute("aria-label",
      mode === "always" ? "Acronym expansions: always shown"
      : mode === "hover" ? "Acronym expansions: shown on hover"
      : "Acronym expansions: hidden");
  }
}

function cycleAcroMode() {
  const next = ACRO_MODES[(ACRO_MODES.indexOf(acroMode()) + 1) % ACRO_MODES.length];
  safeLS.set(ACRO_KEY, next);
  applyAcroMode(next);
}

// ── RANDOM TOPIC ─────────────────────────────────────────────────────────────
// Open a random topic (and its domain), update the hash, and scroll to it.
function jumpToRandomTopic() {
  // From the id map, not the DOM: a random pick over the open domain would be
  // a random pick over a 29th of the site.
  const ids = allTopicIds();
  if (!ids.length) return;
  const id = ids[Math.floor(Math.random() * ids.length)];
  // Clear any active filter/search so the pick is guaranteed visible
  if (typeof clearSearch === "function") {
    const si = document.getElementById("search-input");
    if (si && si.value) clearSearch();
  }
  location.hash = id;   // openHashTarget (hashchange) opens the domain + scrolls
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
    case "a": case "A": e.preventDefault(); cycleAcroMode(); break;
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
  // Also skip when it is already built: its domain can be opened, closed and
  // opened again, and this used to run exactly once per page load.
  if (!container || container.firstChild) return;

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
// Delegated, not per-element: topic headers arrive and leave with their domain,
// and three listeners on each of 1,080 of them was the second-largest thing the
// old load pass did.
function initTouchFeedback() {
  const SEL = ".chip, .domain-header, .topic-header";
  const clear = () => document.querySelectorAll(".is-tapping")
    .forEach(el => el.classList.remove("is-tapping"));
  document.addEventListener("touchstart", e => {
    const el = e.target.closest?.(SEL);
    if (el) el.classList.add("is-tapping");
  }, { passive: true });
  document.addEventListener("touchend", clear, { passive: true });
  document.addEventListener("touchcancel", clear, { passive: true });
}

// ── ACCESSIBILITY, PERMALINKS & PROGRESS ───────────────────────────────────
const REVIEWED_PREFIX = "reviewed:";
const NOTE_PREFIX = "note:";
const STREAK_KEY = "study-streak";
const NOTE_MAX = 1000;

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
 * Load-time setup for the parts of the page that are always present.
 *
 * The per-topic half of this — ids, stored progress, the tool cluster — moved
 * to enhanceDomain(), which runs on a domain when it opens. What is left is the
 * domain headers, the progress badges (read from the id map, so they are right
 * for domains with nothing in the DOM), and the deep-link handler.
 */
function initAccessibilityAndTools() {
  // Before any stored state is read, so a renamed topic shows the progress the
  // user earned under its old id.
  migrateAliasedProgress();

  document.querySelectorAll(".domain-header").forEach(h => {
    h.setAttribute("tabindex", "0");
    h.setAttribute("role", "button");
    h.setAttribute("aria-expanded", "false");
  });

  domainSections().forEach(updateDomainProgress);

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
    on ? safeLS.set(key, "1") : safeLS.remove(key);
    if (on) streakTouch();
    if (typeof stRefreshStudyList === "function") stRefreshStudyList();
  } else if (btn.classList.contains("topic-review")) {
    const on = topic.classList.toggle("reviewed");
    const key = REVIEWED_PREFIX + topic.id;
    on ? safeLS.set(key, "1") : safeLS.remove(key);
    if (on) streakTouch();
    updateDomainProgress(topic.closest(".domain-section"));
  } else if (btn.classList.contains("topic-note-btn")) {
    toggleTopicNote(topic);
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

/** Update the "n/m reviewed" badge on a domain header.
 *
 * Counted from the id map and localStorage, not from `.topic.reviewed` nodes:
 * every domain header shows a badge and at most one of them has any topics in
 * the document to count.
 */
function updateDomainProgress(domain) {
  if (!domain) return;
  const header = domain.querySelector(".domain-header");
  if (!header) return;
  const ids = topicIndex()[domain.dataset.domain] || [];
  const done = ids.reduce(
    (n, id) => n + (safeLS.get(REVIEWED_PREFIX + id) === "1" ? 1 : 0), 0);
  let badge = header.querySelector(".domain-progress");
  if (!badge) {
    badge = document.createElement("span");
    badge.className = "domain-progress";
    const chev = header.querySelector(".chevron");
    chev ? header.insertBefore(badge, chev) : header.appendChild(badge);
  }
  badge.textContent = `${done}/${ids.length}`;
  badge.classList.toggle("complete", done === ids.length && ids.length > 0);
}

/** Reflect the currently-open topic in the URL without a scroll jump. */
function updateTopicHash(topic) {
  if (topic?.id) history.replaceState(null, "", `#${topic.id}`);
  recordVisit(topic?.id);
}

// ── RECENTLY VIEWED ─────────────────────────────────────────────────────────
// The quick-jump palette opens on an empty query, and with 1,300+ topics its
// first sixty rows were whatever the index happened to hold — arbitrary, and
// never what the reader wanted. The list they actually want on an empty query
// is the handful of topics they were just in.
//
// Stored as ids rather than as anything resolved: a card that is later renamed
// or removed simply drops out when the index cannot resolve it, which is the
// right failure. Ten is enough to cover a session's back-and-forth without the
// palette becoming a second history page.
const RECENT_KEY = "recent-topics";
const RECENT_MAX = 10;

function recentIds() {
  try {
    const raw = JSON.parse(localStorage.getItem(RECENT_KEY) || "[]");
    return Array.isArray(raw) ? raw.filter(x => typeof x === "string") : [];
  } catch {
    return [];   // corrupt or unavailable storage is not worth an error here
  }
}

function recordVisit(id) {
  if (!id) return;
  const next = [id, ...recentIds().filter(x => x !== id)].slice(0, RECENT_MAX);
  try { localStorage.setItem(RECENT_KEY, JSON.stringify(next)); } catch { /* full or blocked */ }
}

/** Recently-viewed rows, resolved against the study index and in visit order. */
function recentTopics() {
  const idx = stIndex();
  const byId = new Map(idx.map(t => [t.id, t]));
  return recentIds().map(id => byId.get(id)).filter(Boolean);
}

/** Expand and scroll to the topic named in location.hash, if any. */
// ── SLUG ALIASES ────────────────────────────────────────────────────────────
// Topic ids are derived from the title, so renaming a card silently breaks
// every permalink anyone shared and orphans the progress stored under the old
// id. tools/fix_topic_names.py records each move; build.py inlines the map.

// The flag is keyed on the *contents* of the alias map, not on a version
// number. A boolean ran the migration once per device and then never again, so
// an alias added later — every topic merge does that — moved nobody's progress
// on a device that had already visited. Hashing the map means the key changes
// exactly when the map does, the migration runs once more, and a device that
// has seen this map does nothing.
const ALIAS_MIGRATED_PREFIX = "migrated:slug-aliases:";
let _slugAliases = null;

function slugAliases() {
  if (_slugAliases) return _slugAliases;
  const el = document.getElementById("slug-aliases");
  try {
    const o = el ? JSON.parse(el.textContent) : {};
    _slugAliases = (o && typeof o === "object" && !Array.isArray(o)) ? o : {};
  } catch { _slugAliases = {}; }
  return _slugAliases;
}

/**
 * Move progress from renamed topics onto their current ids, once.
 *
 * Only where the new id has no data of its own — a device that has already
 * studied the renamed card keeps what it did there. The flag makes a second
 * run a no-op, so this cannot keep resurrecting keys the user has since
 * cleared.
 */
function aliasMapKey(aliases) {
  // FNV-1a over the sorted pairs. Not a security hash — it only has to change
  // when the map does, and be the same length every time.
  const src = Object.keys(aliases).sort().map(k => k + ">" + aliases[k]).join("|");
  let h = 0x811c9dc5;
  for (let i = 0; i < src.length; i++) {
    h ^= src.charCodeAt(i);
    h = Math.imul(h, 0x01000193) >>> 0;
  }
  return ALIAS_MIGRATED_PREFIX + h.toString(36);
}

function migrateAliasedProgress() {
  const aliases = slugAliases();
  const flag = aliasMapKey(aliases);
  try { if (localStorage.getItem(flag)) return 0; } catch { return 0; }
  let moved = 0;
  Object.keys(aliases).forEach(old => {
    const now = aliases[old];
    // NOTE_PREFIX is here deliberately. It was missing, so a merged or renamed
    // topic silently discarded the one piece of progress the reader actually
    // wrote themselves — which is the opposite of what the alias map is for.
    [REVIEWED_PREFIX, BOOKMARK_PREFIX, KNOWN_PREFIX, SRS_PREFIX, NOTE_PREFIX].forEach(p => {
      const from = localStorage.getItem(p + old);
      if (from === null) return;
      if (localStorage.getItem(p + now) === null) {
        try { localStorage.setItem(p + now, from); moved++; } catch { return; }
      }
      localStorage.removeItem(p + old);
    });
  });
  try {
    // Drop the previous generation's flag (and the original v1 boolean) so the
    // keys do not accumulate one per alias-map revision, forever.
    Object.keys(localStorage)
      .filter(k => (k.startsWith(ALIAS_MIGRATED_PREFIX) || k === "migrated:slug-aliases-v1")
                   && k !== flag)
      .forEach(k => localStorage.removeItem(k));
    localStorage.setItem(flag, "1");
  } catch { /* quota, or storage blocked entirely */ }
  return moved;
}

/**
 * Split `#topic-id/3` into the topic and the 1-based concept-card index.
 *
 * Cards are addressed by position rather than by a slug of their title. A slug
 * would be prettier and would need every `.concept-title` stamped at build
 * time and kept stable — and concept titles are edited far more freely than
 * topic names, which have an alias map precisely because they are not. An
 * index survives rewording and breaks on reordering; between the two,
 * rewording is what actually happens.
 */
function splitCardHash(hash) {
  const m = hash.match(/^(.*?)\/(\d+)$/);
  return m ? { id: m[1], card: Number(m[2]) } : { id: hash, card: 0 };
}

function openHashTarget() {
  const parsed = splitCardHash(decodeURIComponent(location.hash.slice(1)));
  let id = parsed.id;
  if (!id) return;
  // A stale link resolves through the alias map, then rewrites itself so the
  // address bar — and anything copied out of it — carries the current id.
  // Resolved against the id map rather than the document: the topic a cold link
  // names is almost never in the DOM yet, which is the whole point.
  if (!topicDomain(id) && slugAliases()[id]) {
    id = slugAliases()[id];
    const rewritten = parsed.card ? `#${id}/${parsed.card}` : `#${id}`;
    if (history.replaceState) history.replaceState(null, "", rewritten);
    else location.hash = rewritten.slice(1);
  }
  const domainId = topicDomain(id);
  if (!domainId) return;
  const section = domainSection(domainId);
  // A link into a domain the chip bar has filtered out drops the filter. The
  // alternative is rendering a card inside a `display: none` section and
  // scrolling to nothing.
  if (section?.classList.contains("hidden")) {
    document.querySelector('.chip[data-domain="all"]')?.click();
  }
  openDomain(section);
  const topic = document.getElementById(id);
  if (!topic || !topic.classList.contains("topic")) return;
  // A topic reached by link is shown even when a search is filtering its
  // domain — the reader asked for this card by name.
  topic.classList.remove("search-hidden");
  setTopicOpen(topic.querySelector(":scope > .topic-header"), true);
  renderSeeAlso(topic);
  renderTopicNote(topic);

  // A card-level link scrolls to the card and marks it briefly. Falling back to
  // the topic when the index is out of range is deliberate: a link shared
  // before a card was removed should still land somewhere useful rather than
  // doing nothing.
  const card = parsed.card
    ? topic.querySelectorAll(".topic-body > .concept-card")[parsed.card - 1]
    : null;
  recordVisit(topic.id);
  if (card) {
    card.scrollIntoView({ behavior: "smooth", block: "center" });
    card.classList.add("card-linked");
    setTimeout(() => card.classList.remove("card-linked"), 2200);
  } else {
    topic.scrollIntoView({ behavior: "smooth", block: "start" });
  }
}

/**
 * Copy a link to one concept card. Delegated from the domain body rather than
 * given a button per card: a domain can hold several hundred concept cards, and
 * an affordance that costs one element each is a real slice of the DOM budget
 * for something used rarely. The label carries the hint in its `title`.
 */
function copyCardLink(label) {
  const card = label.closest(".concept-card");
  const topic = label.closest(".topic");
  if (!card || !topic?.id) return;
  const cards = [...topic.querySelectorAll(".topic-body > .concept-card")];
  const n = cards.indexOf(card) + 1;
  if (n < 1) return;
  const url = `${location.origin}${location.pathname}#${topic.id}/${n}`;
  const done = () => {
    label.classList.add("copied");
    setTimeout(() => label.classList.remove("copied"), 1200);
  };
  if (navigator.clipboard?.writeText) {
    navigator.clipboard.writeText(url)
      .then(done)
      // No clipboard permission — over `file://`, or a browser that withholds
      // it. Putting the link in the address bar is the fallback, and it still
      // confirms: a silent no-op reads as a broken control.
      .catch(() => { location.hash = `${topic.id}/${n}`; done(); });
  } else {
    location.hash = `${topic.id}/${n}`;
    done();
  }
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
  // The Clipboard API is absent in an insecure context — file://, plain http,
  // a permissionless iframe — where `navigator.clipboard` is undefined and an
  // unguarded call throws. The other three copy buttons already guard and fall
  // back; this one did not. Fall back to selecting the field for a manual copy.
  const fallback = () => { el.select(); _msg("⌘/Ctrl-C to copy.", "var(--amber)"); };
  if (navigator.clipboard?.writeText) {
    navigator.clipboard.writeText(el.value)
      .then(() => _msg("✓ Copied.", "var(--green)"))
      .catch(fallback);
  } else {
    fallback();
  }
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
// Acronym <-> expansion lookup, built once from the block build.py inlines.
// Searching "Unified Endpoint Management" should find the UEM cards even
// where the page only says UEM, and vice versa.
let _acroSearchMap = null;
function acroSearchMap() {
  if (_acroSearchMap) return _acroSearchMap;
  const m = new Map();
  const add = (key, val) => {
    const k = key.toLowerCase();
    if (!m.has(k)) m.set(k, new Set());
    m.get(k).add(val);
  };
  (typeof acroData === "function" ? acroData() : []).forEach(([a, exps]) => {
    exps.forEach(e => { add(a, e); add(e, a); });
  });
  _acroSearchMap = m;
  return m;
}

/**
 * The query plus anything the dictionary says is the same thing.
 * Exact lookup only — a substring match would make "IP" pull in every
 * expansion containing the word "internet".
 */
function searchTerms(term) {
  const terms = [term];
  (acroSearchMap().get(term.toLowerCase()) || []).forEach(alt => {
    if (alt.toLowerCase() !== term.toLowerCase()) terms.push(alt);
  });
  return terms;
}

/**
 * A test for one search term against a topic's text.
 *
 * Long terms match as substrings, which is what a reader expects: typing
 * "kerber" should find Kerberos. **Short ones must not**, and the reason is
 * the acronym map rather than the reader. Searching "incident response" adds
 * the dictionary's alternate "IR", and `text.includes("ir")` is true of
 * "requires", "first", "third" and "directory" — so the query returned 1,220
 * of 1,367 topics, which is not a search result, it is the site.
 *
 * The guard in searchTerms() covers the *lookup* ("IP" must not pull in every
 * expansion containing "internet"); this covers the *match*, which is the
 * other half and was missing. Word-boundary rather than \b, so a term with
 * punctuation in it still behaves.
 */
const SHORT_TERM = 4;
function matcher(lowered) {
  if (lowered.length > SHORT_TERM) return text => text.includes(lowered);
  const esc = lowered.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const re = new RegExp(`(?<![a-z0-9])${esc}(?![a-z0-9])`);
  return text => re.test(text);
}

/**
 * Split a raw query into its operators, its quoted phrases and the free text.
 *
 * At 1,300+ topics a bare substring search returns more than a reader can use,
 * and the two things they actually want are "only in this domain" and "these
 * words, in this order". Both are one regex each; neither needs an index.
 *
 *   domain:net tcp        → free text "tcp", restricted to the net domain
 *   "default deny"        → that phrase, literally, not two words
 *   domain:ops "burn rate" alerting
 *
 * `domain:` is matched against domain ids, which are what the chips and the
 * permalinks already use, so the vocabulary is one the reader has seen. An id
 * that does not exist yields no matches rather than being ignored — silently
 * dropping an operator would answer a different question than the one asked.
 */
const RE_DOMAIN_OP = /(?:^|\s)domain:([a-z0-9_-]+)/gi;
// plan.md Phase 10 T7. `data-level` is stamped at build time from the badge —
// beginner, advanced, or core meaning "not marked as either". An operator
// rather than a chip: it composes with `domain:`, needs no room in a filter bar
// that is already full, and lands in the same place readers already look for
// `domain:`. A level that does not exist yields no matches rather than being
// ignored, for the reason the domain operator does.
const RE_LEVEL_OP = /(?:^|\s)level:([a-z]+)/gi;
// plan.md Phase 10 T8. `since:2026-06` is *strictly after* that month, which is
// what "since" means in English and what the what's-new banner needs: it passes
// the last month this reader acknowledged, and wants what landed afterwards.
// Month strings compare correctly as strings because they are zero-padded.
const RE_SINCE_OP = /(?:^|\s)since:(\d{4}-\d{2})/gi;
const RE_PHRASE = /"([^"]+)"/g;

function parseQuery(raw) {
  const domains = [];
  const phrases = [];
  let rest = raw.replace(RE_PHRASE, (_, p) => {
    const t = p.trim();
    if (t) phrases.push(t);
    return " ";
  });
  rest = rest.replace(RE_DOMAIN_OP, (_, d) => {
    domains.push(d.toLowerCase());
    return " ";
  });
  const levels = [];
  rest = rest.replace(RE_LEVEL_OP, (_, l) => {
    levels.push(l.toLowerCase());
    return " ";
  });
  let since = "";
  rest = rest.replace(RE_SINCE_OP, (_, m) => { since = m; return " "; });
  return { domains, levels, since, phrases, text: rest.replace(/\s+/g, " ").trim() };
}

// ── SEARCH STATE ────────────────────────────────────────────────────────────
// A search now spans more of the page than the page is showing, so the result
// has to be held rather than only painted: which topics matched, per domain, so
// that a domain opened later can be filtered to the same result.
let _searchTerm = "";        // the applied query ("" when not searching)
let _searchTermList = [];    // it, plus whatever the dictionary says is the same
const _searchHits = new Map();  // domain id -> Set of matching topic ids

/** The "n matches" pill on a collapsed domain's header. */
function setMatchBadge(section, n) {
  const header = section.querySelector(".domain-header");
  let badge = header.querySelector(".domain-matches");
  if (!badge) {
    badge = document.createElement("span");
    badge.className = "domain-matches";
    header.insertBefore(badge, header.querySelector(".domain-progress") || header.querySelector(".chevron"));
  }
  badge.textContent = `${n} match${n === 1 ? "" : "es"}`;
}

/**
 * Filter and highlight the open domain against the current search.
 *
 * Split out from runSearch because it runs twice over: once when the search
 * picks a domain to show, and again whenever the reader opens a different one
 * while the query is still in the box.
 */
function applySearchToDomain(section) {
  const hits = _searchHits.get(section.dataset.domain);
  section.querySelectorAll(".topic").forEach(topic => {
    if (hits && hits.has(topic.id)) {
      topic.classList.remove("search-hidden");
      setTopicOpen(topic.querySelector(":scope > .topic-header"), true);
      renderSeeAlso(topic);
      renderTopicNote(topic);
      topic.querySelectorAll(
        ".topic-name, .concept-title, .concept-label, .concept-desc, .dw, .dt, .code-block"
      ).forEach(n => _searchTermList.forEach(t => highlightIn(n, t)));
    } else {
      topic.classList.add("search-hidden");
    }
  });
  // A search asked for topics, not for the domain's front matter.
  section.querySelector(":scope > .domain-body > .domain-intro")
    ?.classList.add("search-hidden");
}

/**
 * Immediate search runner. Prefer the debounced onSearchInput() for keystrokes.
 *
 * Every domain is searched — the deferred blocks are parsed text, not markup
 * the browser has to build — but only one domain's matches are rendered. The
 * rest report their count on their header and open on a click, already
 * filtered. That is the same reach as the old whole-DOM search with a
 * twenty-ninth of the layout.
 *
 * @param {string} raw - Current value of the search input.
 */
function runSearch(raw) {
  const term = raw.trim();
  const clearBtn = document.getElementById("search-clear");
  const countEl  = document.getElementById("search-count");

  if (clearBtn) clearBtn.classList.toggle("visible", term.length > 0);

  // Reset previous highlights and visibility
  clearHighlights();
  _searchHits.clear();
  domainSections().forEach(s => {
    s.classList.remove("search-hidden");
    s.querySelector(".domain-matches")?.remove();
  });
  _liveDomain?.querySelectorAll(".topic.search-hidden, .domain-intro.search-hidden")
    .forEach(el => el.classList.remove("search-hidden"));

  const q = parseQuery(term);
  // A query is runnable once it carries something to match on: free text of at
  // least two characters, or a phrase, or a bare `domain:` used to browse one
  // domain. Measuring the raw string instead would reject `domain:hw` — which
  // is two characters of operator and eight of intent.
  //
  // Free text below the threshold makes the whole query unusable rather than
  // being dropped. Dropping it is worse than doing nothing: `domain:hw x`
  // would quietly answer "everything in hw", which is not what was asked and
  // reads as a result rather than as a rejected query.
  const tooShort = q.text.length > 0 && q.text.length < 2;
  const usable = !tooShort
    && (q.text.length >= 2 || q.phrases.length > 0 || q.domains.length > 0
        || q.levels.length > 0 || q.since);
  _searchTerm = usable ? term : "";
  if (!_searchTerm) {
    _searchTermList = [];
    if (countEl) countEl.textContent = "";
    return;
  }

  // Highlight everything the reader asked for: the phrases verbatim, and the
  // free text along with whatever the acronym dictionary says is the same
  // thing. The operators themselves are never highlighted — they are not
  // content the reader was looking for.
  const textTerms = q.text ? searchTerms(q.text) : [];
  _searchTermList = [...q.phrases, ...textTerms];
  const loweredText = textTerms.map(t => t.toLowerCase()).map(matcher);
  const loweredPhrases = q.phrases.map(p => p.toLowerCase());
  let matchCount = 0, domainCount = 0, firstHit = null;

  domainSections().forEach(section => {
    const hits = new Set();
    // `domain:` narrows which domains are searched at all. Several are additive
    // — `domain:net domain:hw` searches both.
    if (q.domains.length && !q.domains.includes(section.dataset.domain)) {
      section.classList.add("search-hidden");
      return;
    }
    domainTopics(section.dataset.domain).forEach(t => {
      // Phrases are required, all of them; the free text is satisfied by the
      // query or any of its acronym equivalents. A query that is only
      // operators and phrases matches on the phrases alone.
      if (q.levels.length && !q.levels.includes(t.level)) return;
      if (q.since && !(t.reviewed && t.reviewed > q.since)) return;
      if (!loweredPhrases.every(p => t.text.includes(p))) return;
      if (loweredText.length && !loweredText.some(m => m(t.text))) return;
      hits.add(t.id);
    });
    if (!hits.size) {
      section.classList.add("search-hidden");
      return;
    }
    _searchHits.set(section.dataset.domain, hits);
    matchCount += hits.size;
    domainCount++;
    // A chip filter still wins over the search's choice of what to show: a
    // domain the reader has filtered away must not be the one that renders.
    if (!firstHit && !section.classList.contains("hidden")) firstHit = section;
    setMatchBadge(section, hits.size);
  });

  // Show the domain the reader is already in if it has anything; otherwise the
  // first that does. The others stay one click away with their counts visible.
  const target = _liveDomain && _searchHits.has(_liveDomain.dataset.domain)
    && !_liveDomain.classList.contains("hidden") ? _liveDomain : firstHit;
  if (target) openDomain(target);

  if (countEl) {
    // Only the acronym alternates belong in "also matching" — phrases are what
    // the reader typed, not something the dictionary added on their behalf.
    const via = textTerms.length > 1
      ? ` · also matching ${textTerms.slice(1).map(t => `“${t}”`).join(", ")}` : "";
    // Say when an operator narrowed the search, so "no matches" is never
    // ambiguous between "nothing on the site" and "nothing in that domain".
    const parts = [];
    if (q.domains.length) parts.push(`in ${q.domains.join(", ")}`);
    if (q.levels.length) parts.push(`at ${q.levels.join(", ")} level`);
    if (q.since) parts.push(`updated after ${monthLabel(q.since)}`);
    const scope = parts.length ? ` · ${parts.join(" · ")}` : "";
    countEl.textContent = matchCount
      ? `${matchCount} match${matchCount !== 1 ? "es" : ""} in ${domainCount} domain${domainCount !== 1 ? "s" : ""}${via}`
      : `no matches${scope}`;
  }
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
  let id = safeSS.get(NP_SESSION_KEY);
  if (!id) {
    id = Math.random().toString(36).slice(2, 10);
    safeSS.set(NP_SESSION_KEY, id);
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

  nameEl.value = safeLS.get(NP_AUTHOR_KEY) || "";

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
    if (nameEl.value.trim()) safeLS.set(NP_AUTHOR_KEY, nameEl.value.trim());

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

/** How many topics are waiting today — drives the badge on the study button.
 *
 * Runs at load, and the loop bound `localStorage.length` throws — not returns —
 * when storage is blocked, which `srsGet`'s own guard below cannot catch because
 * it never gets called. Wrapped so a blocked-storage visitor sees a zero badge
 * instead of an uncaught error at load. */
function srsDueCount() {
  let due = 0;
  try {
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      if (!k || !k.startsWith(SRS_PREFIX)) continue;
      const r = srsGet(k.slice(SRS_PREFIX.length));
      if (r && r.d <= srsToday()) due++;
    }
  } catch { /* storage blocked — nothing is due */ }
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
  if (grade !== "again") safeLS.set(KNOWN_PREFIX + id, "1");
  streakTouch();
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

/** Build a flat index of every topic on the page (once).
 *
 * From the deferred blocks, not the document: a deck built from what is
 * rendered would be one domain deep and look perfectly healthy, which is the
 * failure this whole file has to keep avoiding.
 */
function stIndex() {
  if (_stIndex) return _stIndex;
  _stIndex = [];
  domainSections().forEach(domain => {
    const domainId = domain.dataset.domain || "";
    const domainTitle = (domain.querySelector(".domain-title")?.textContent || "").trim();
    const domainIcon = (domain.querySelector(".domain-icon")?.textContent || "").trim();
    domainTopics(domainId).forEach(t => {
      if (t.id && t.name) {
        _stIndex.push({ id: t.id, name: t.name, title: t.title, desc: t.desc,
                        badge: t.badge, domainId, domainTitle, domainIcon });
      }
    });
  });
  return _stIndex;
}

function stIsBookmarked(id) { return safeLS.get(BOOKMARK_PREFIX + id) === "1"; }

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
  // The exam's clock is an interval, and an interval outlives the modal that
  // owns it — left running it would keep ticking against a stage that is no
  // longer on screen, and eventually "submit" a paper nobody is sitting.
  stExamStop();
  _examState = null;
}

function esc(s) { return (s || "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])); }

// ── Scope selector (All / a domain / Bookmarks) ─────────────────────────────
// The acronym dictionary's "topics" are A–Z index sections, not concepts. As a
// flashcard the front reads "A — 75 acronyms"; as a quiz the distractors are
// "Acronyms — B" and "Acronyms — C". It has its own quiz (🔤 Acronym quiz),
// which asks the question this material can actually answer.
const ST_NOT_STUDYABLE = new Set(["acronym"]);
function stIsStudyable(t) { return !ST_NOT_STUDYABLE.has(t.domainId); }

function stScopeOptions() {
  const doms = [];
  const seen = new Map();
  stIndex().filter(stIsStudyable).forEach(t => {
    if (!seen.has(t.domainId)) {
      const d = { id: t.domainId, title: t.domainTitle, icon: t.domainIcon, n: 0 };
      seen.set(t.domainId, d);
      doms.push(d);
    }
    seen.get(t.domainId).n++;
  });
  return doms;
}
function stTopicsForScope(scope) {
  const all = stIndex();
  if (scope === "__all") return all.filter(stIsStudyable);
  // Starring and grading are deliberate acts, so those two decks honour the
  // user's choice even for a section the domain list would not offer.
  if (scope === "__bookmarks") return all.filter(t => stIsBookmarked(t.id));
  if (scope === "__due") return all.filter(t => srsGet(t.id) && srsIsDue(t.id));
  return all.filter(t => t.domainId === scope);
}
function stScopeSelectHTML(id) {
  const dueN = srsDueCount();
  const opts = ['<option value="__all">◈ All domains</option>',
    '<option value="__bookmarks">★ My study list</option>',
    `<option value="__due">⏰ Due today${dueN ? ` (${dueN})` : ""}</option>`]
    // d.title, not d.domainTitle — the latter is the key on an stIndex row, not
    // on what stScopeOptions returns, and reading it left every deck in the list
    // showing an icon and no name. Two domains share the 🌐 icon, so two of the
    // options were literally identical.
    .concat(stScopeOptions().map(d =>
      // Parentheses, not a dash: some domain titles already contain an em dash
      // ("Endpoint Management — Intune · MECM") and a second one read as a typo.
      `<option value="${esc(d.id)}">${esc(d.icon)} ${esc(d.title)} (${d.n})</option>`));
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

    // On an empty query the palette leads with what the reader was just
    // looking at, then falls back to the index. Recent rows are marked so the
    // ordering is explained rather than mysterious.
    let recentCount = 0;
    function render(q) {
      const query = q.trim().toLowerCase();
      const idx = stIndex();
      if (query) {
        recentCount = 0;
        items = idx
          .filter(t => (t.name + " " + t.domainTitle + " " + t.title).toLowerCase().includes(query))
          .slice(0, 60);
      } else {
        const recent = recentTopics();
        recentCount = recent.length;
        const seen = new Set(recent.map(t => t.id));
        items = [...recent, ...idx.filter(t => !seen.has(t.id))].slice(0, 60);
      }
      active = 0;
      list.innerHTML = items.map((t, i) =>
        `<li class="st-jump-item${i === 0 ? " active" : ""}" data-i="${i}">` +
        `<span class="st-jump-name">${esc(t.name)}</span>` +
        (i < recentCount ? '<span class="st-jump-recent">recent</span>' : "") +
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
// ── EXAM MODE ───────────────────────────────────────────────────────────────
// The quiz with three things taken away and one added: a fixed length, a clock,
// and no feedback until the end — then a report broken down by domain, with the
// topics that were missed linked so the next step is one click rather than a
// memory exercise.
//
// The no-feedback rule is the point of the mode. A quiz that marks each answer
// is a study tool; an exam that does not is a measurement, and the difference
// is whether the score means anything.

const EXAM_SECONDS_PER_Q = 45;
let _examState = null;

/**
 * Distractors from the question's own domain wherever that domain is big
 * enough, falling back to the scope.
 *
 * Drawing them from the whole site — which is what "all domains" would do
 * naively — makes almost every question answerable by noticing that three
 * options are about Kubernetes and one is about soldering.
 */
function examDistractors(q, pool, byDomain) {
  const home = (byDomain.get(q.domainId) || []).filter(t => t.id !== q.id);
  const from = home.length >= 3 ? home : pool.filter(t => t.id !== q.id);
  return shuffle(from.slice()).slice(0, 3);
}

function examBuild(scope, count) {
  const pool = stTopicsForScope(scope).filter(t => t.title || t.desc);
  if (pool.length < 4) return null;
  const byDomain = new Map();
  pool.forEach(t => {
    if (!byDomain.has(t.domainId)) byDomain.set(t.domainId, []);
    byDomain.get(t.domainId).push(t);
  });
  return shuffle(pool.slice()).slice(0, Math.min(count, pool.length)).map(q => {
    const wrong = examDistractors(q, pool, byDomain);
    return {
      id: q.id, name: q.name, domainId: q.domainId, domainTitle: q.domainTitle,
      domainIcon: q.domainIcon,
      prompt: q.title || (q.desc || "").slice(0, 160),
      options: shuffle([q, ...wrong]).map(o => ({ id: o.id, name: o.name })),
      answer: q.id,
    };
  }).filter(q => q.options.length === 4);
}

function examTimeLeft() {
  const s = _examState;
  if (!s || !s.limit) return null;
  return Math.max(0, s.limit - Math.round((Date.now() - s.started) / 1000));
}

function examClock(seconds) {
  const m = Math.floor(seconds / 60), sec = seconds % 60;
  return `${m}:${String(sec).padStart(2, "0")}`;
}

function stOpenExam() {
  stOpen(body => {
    body.innerHTML =
      '<h2 class="st-h">📋 Exam</h2>' +
      '<p class="st-bk-lead">A fixed number of questions, a clock, and no feedback until the end — ' +
      'then a breakdown by domain with every missed topic linked.</p>' +
      '<div class="st-toolbar"><label class="st-lbl">From</label>' + stScopeSelectHTML("st-ex-scope") +
      '</div>' +
      '<div class="st-toolbar"><label class="st-lbl">Length</label>' +
      '<select id="st-ex-count" class="st-select">' +
        '<option value="10">10 questions</option>' +
        '<option value="20" selected>20 questions</option>' +
        '<option value="40">40 questions</option></select>' +
      '<label class="st-lbl">Clock</label>' +
      '<select id="st-ex-timed" class="st-select">' +
        '<option value="1" selected>Timed</option>' +
        '<option value="0">Untimed</option></select>' +
      '<button id="st-ex-start" class="st-btn st-btn-primary">Begin</button></div>' +
      '<div id="st-ex-stage"></div>';
    const stage = body.querySelector("#st-ex-stage");
    body.querySelector("#st-ex-start").addEventListener("click", () => stStartExam(
      body.querySelector("#st-ex-scope").value,
      Number(body.querySelector("#st-ex-count").value),
      body.querySelector("#st-ex-timed").value === "1",
      stage));
  });
}

function stStartExam(scope, count, timed, stage) {
  const questions = examBuild(scope, count);
  if (!questions || questions.length < 4) {
    stage.innerHTML = '<p class="st-empty">Not enough topics with descriptions in that scope to sit an exam. Pick a broader one.</p>';
    return;
  }
  stExamStop();
  _examState = {
    scope, questions, i: 0, answers: new Array(questions.length).fill(null),
    started: Date.now(), limit: timed ? questions.length * EXAM_SECONDS_PER_Q : 0,
    timer: null, stage,
  };
  if (_examState.limit) {
    _examState.timer = setInterval(() => {
      const left = examTimeLeft();
      const el = document.getElementById("st-ex-clock");
      if (el) {
        el.textContent = examClock(left);
        el.classList.toggle("low", left <= 60);
      }
      // Running out is a submission, not an error: the paper is taken away and
      // whatever is on it is marked.
      if (left <= 0) stExamFinish();
    }, 1000);
  }
  stExamRender();
}

/** Clear the interval whenever the exam ends, is restarted, or the modal closes. */
function stExamStop() {
  if (_examState?.timer) clearInterval(_examState.timer);
  if (_examState) _examState.timer = null;
}

function stExamRender() {
  const s = _examState; if (!s) return;
  const q = s.questions[s.i];
  const left = examTimeLeft();
  const answered = s.answers.filter(a => a !== null).length;
  s.stage.innerHTML =
    '<div class="st-ex-bar">' +
      `<span class="st-progress">Question ${s.i + 1} / ${s.questions.length}</span>` +
      `<span class="st-ex-answered">${answered} answered</span>` +
      (s.limit ? `<span id="st-ex-clock" class="st-ex-clock${left <= 60 ? " low" : ""}">${examClock(left)}</span>` : "") +
    '</div>' +
    `<div class="st-q-prompt"><span class="st-q-label">Which topic does this describe?</span>${esc(q.prompt)}</div>` +
    '<ul class="st-q-options">' + q.options.map(o =>
      `<li><button class="st-q-opt${s.answers[s.i] === o.id ? " chosen" : ""}" data-id="${esc(o.id)}">${esc(o.name)}</button></li>`).join("") +
    '</ul>' +
    '<div class="st-ex-nav">' +
      `<button id="st-ex-prev" class="st-btn"${s.i === 0 ? " disabled" : ""}>← Back</button>` +
      (s.i === s.questions.length - 1
        ? '<button id="st-ex-finish" class="st-btn st-btn-primary">Finish</button>'
        : '<button id="st-ex-next" class="st-btn st-btn-primary">Next →</button>') +
    '</div>';
  // Choosing an answer says nothing about whether it was right — that is the
  // whole mode. It moves on, because hesitating over a mark you will not get is
  // the habit an exam is meant to break.
  s.stage.querySelectorAll(".st-q-opt").forEach(btn => btn.addEventListener("click", () => {
    s.answers[s.i] = btn.dataset.id;
    if (s.i < s.questions.length - 1) { s.i++; stExamRender(); }
    else stExamRender();
  }));
  s.stage.querySelector("#st-ex-prev")?.addEventListener("click", () => { if (s.i > 0) { s.i--; stExamRender(); } });
  s.stage.querySelector("#st-ex-next")?.addEventListener("click", () => { s.i++; stExamRender(); });
  s.stage.querySelector("#st-ex-finish")?.addEventListener("click", stExamFinish);
}

function examResult() {
  const s = _examState;
  const byDomain = new Map();
  const missed = [];
  s.questions.forEach((q, i) => {
    const right = s.answers[i] === q.answer;
    if (!byDomain.has(q.domainId)) {
      byDomain.set(q.domainId, { id: q.domainId, title: q.domainTitle, icon: q.domainIcon, n: 0, right: 0 });
    }
    const d = byDomain.get(q.domainId);
    d.n++;
    if (right) d.right++;
    else missed.push({ id: q.id, name: q.name, domainId: q.domainId, skipped: s.answers[i] === null });
  });
  const score = s.questions.length - missed.length;
  return {
    score, total: s.questions.length, missed,
    elapsed: Math.round((Date.now() - s.started) / 1000),
    // Weakest first: a report is a list of what to do next, and the domain you
    // scored 40% in belongs above the one you scored 90% in.
    domains: [...byDomain.values()].sort((a, b) => (a.right / a.n) - (b.right / b.n)),
  };
}

function stExamFinish() {
  const s = _examState; if (!s) return;
  stExamStop();
  const r = examResult();
  const pct = Math.round((r.score / r.total) * 100);
  s.stage.innerHTML =
    '<div class="st-result"><div class="st-result-big">' +
      (pct >= 80 ? "🏆" : pct >= 50 ? "👍" : "📚") + '</div>' +
    `<p>Score: <strong>${r.score} / ${r.total}</strong> (${pct}%) · ${examClock(r.elapsed)} taken</p></div>` +
    '<table class="st-ex-table"><thead><tr><th>Domain</th><th>Score</th><th></th></tr></thead><tbody>' +
    r.domains.map(d => {
      const p = Math.round((d.right / d.n) * 100);
      return `<tr><td>${esc(d.icon)} ${esc(d.title)}</td><td class="st-pg-num">${d.right}/${d.n}</td>` +
        `<td class="st-pg-barcell"><div class="st-pg-bar"><div class="st-pg-fill" style="width:${p}%"></div></div></td></tr>`;
    }).join("") + '</tbody></table>' +
    (r.missed.length
      ? '<h3 class="st-path-title">What to review</h3>' +
        '<div class="st-toolbar"><span class="st-count">' +
        `${r.missed.length} missed</span>` +
        '<button id="st-ex-star" class="st-btn">★ Star all of these</button>' +
        '<button id="st-ex-again" class="st-btn st-btn-primary">Sit another</button></div>' +
        '<ul class="st-list">' + r.missed.map(m =>
          `<li class="st-list-item"><button class="st-list-link" data-id="${esc(m.id)}">${esc(m.name)}</button>` +
          `<span class="st-step-dom">${esc(m.domainId)}${m.skipped ? " · unanswered" : ""}</span></li>`).join("") +
        '</ul>'
      : '<p class="st-hint">Nothing missed. Pick a broader scope or a longer paper.</p>' +
        '<div class="st-toolbar"><button id="st-ex-again" class="st-btn st-btn-primary">Sit another</button></div>');
  s.stage.querySelectorAll(".st-list-link").forEach(b =>
    b.addEventListener("click", () => { stClose(); stGoToTopic(b.dataset.id); }));
  s.stage.querySelector("#st-ex-star")?.addEventListener("click", e => {
    r.missed.forEach(m => safeLS.set(BOOKMARK_PREFIX + m.id, "1"));
    document.querySelectorAll(".topic").forEach(t => {
      if (safeLS.get(BOOKMARK_PREFIX + t.id) === "1") t.classList.add("bookmarked");
    });
    e.target.textContent = `★ ${r.missed.length} starred`;
    e.target.disabled = true;
    if (typeof stRefreshStudyList === "function") stRefreshStudyList();
  });
  s.stage.querySelector("#st-ex-again")?.addEventListener("click", () => stOpenExam());
  streakTouch();
  return r;
}

// ── MARKDOWN EXPORT ─────────────────────────────────────────────────────────
// Take a topic, a domain or the whole site out of this page and into a notes
// app. The conversion runs over the deferred block's markup rather than the
// live DOM, so a domain that has never been opened exports exactly like one
// that has — the same reason every other feature here reads the blocks.

// Elements that end a line. Without this, a card built from nested <div>s — the
// layer stacks, the comparison grids — flattens into one unreadable run: the
// markup carried the structure and the text never did.
const MD_BLOCK = new Set(["DIV", "P", "SECTION", "UL", "OL", "TR", "H1", "H2", "H3", "H4", "H5", "H6"]);

/** Inline elements that become Markdown wrappers rather than structure. */
const MD_WRAP = { strong: "**", b: "**", em: "_", i: "_", code: "`" };

/** Collapse runs of whitespace without eating the space between two elements. */
function mdText(s) { return (s || "").replace(/\s+/g, " "); }

function mdEscape(s) {
  // Only the characters that would change the meaning of a *table* cell or
  // start a list. Escaping every Markdown metacharacter makes prose unreadable
  // for the sake of edge cases that do not occur in this content.
  return s.replace(/\|/g, "\\|");
}

/** One table -> a Markdown table. Ragged rows are padded, never dropped. */
function mdTable(table) {
  const trs = [...table.querySelectorAll("tr")];
  const rows = trs.map(tr =>
    [...tr.querySelectorAll("th, td")].map(c => mdEscape(mdText(c.textContent).trim())));
  if (!rows.length) return "";
  const width = Math.max(...rows.map(r => r.length));
  const pad = r => r.concat(Array(width - r.length).fill(""));
  // Most tables here have no <thead> at all — the header is a bare <tr> of
  // <th>. Keying off <thead> put five empty cells in the header and pushed the
  // real one into the body, on every table on the site.
  const headIndex = trs.findIndex(tr => tr.querySelector("th"));
  const hasHead = headIndex !== -1 && rows[headIndex].some(Boolean);
  const head = hasHead ? pad(rows[headIndex]) : Array(width).fill("");
  const body = rows.filter((_, i) => !hasHead || i !== headIndex);
  return [
    `| ${head.join(" | ")} |`,
    `| ${Array(width).fill("---").join(" | ")} |`,
    ...body.map(r => `| ${pad(r).join(" | ")} |`),
  ].join("\n") + "\n";
}

/**
 * Walk a topic's markup and emit Markdown.
 *
 * Deliberately structural rather than generic: this converts *this site's*
 * conventions — concept cards, reference tables, code blocks, cross-references
 * — and it is much better at that than a general HTML-to-Markdown pass would
 * be, because it knows a `.concept-label` is a kicker and not a paragraph.
 */
function mdFromNode(node, out) {
  if (node.nodeType === 3) { out.push(mdText(node.nodeValue)); return; }
  if (node.nodeType !== 1) return;
  const el = node;
  const cls = el.classList;

  if (cls.contains("topic-icon") || cls.contains("topic-chev")) return;
  if (cls.contains("acro-exp")) { out.push(" " + mdText(el.textContent).trim()); return; }

  if (el.tagName === "PRE") {
    out.push("\n```\n" + el.textContent.replace(/\s+$/, "") + "\n```\n\n");
    return;
  }
  if (el.tagName === "TABLE") { out.push("\n" + mdTable(el) + "\n"); return; }
  if (el.tagName === "BR") { out.push("\n"); return; }
  if (el.tagName === "LI") {
    out.push("- ");
    [...el.childNodes].forEach(c => mdFromNode(c, out));
    out.push("\n");
    return;
  }

  const wrap = MD_WRAP[el.tagName.toLowerCase()];
  const text = mdText(el.textContent).trim();
  if (wrap && text) { out.push(wrap + text + wrap); return; }

  if (cls.contains("topic-name")) { out.push(`\n## ${text}\n\n`); return; }
  if (cls.contains("topic-badge")) { out.push(`_${text}_\n\n`); return; }
  if (cls.contains("concept-label")) { out.push(`**${text.toUpperCase()}**\n\n`); return; }
  if (cls.contains("concept-title")) { out.push(`### ${text}\n\n`); return; }
  if (cls.contains("xref")) { out.push(`_${text}_`); return; }
  // A row of a div-built table. There are 78 of these on the site against 1,883
  // real <table> elements, and until they are converted the export has to know
  // their class names: their children are cells, and cells belong on one line.
  if (cls.contains("layer") || cls.contains("dt-row") || cls.contains("kc-row")
      || cls.contains("nist-row") || cls.contains("perm-row")
      || cls.contains("url-codec-row")) {
    const cells = [...el.children].map(c => mdText(c.textContent).trim()).filter(Boolean);
    out.push((cells.length ? cells.join(" — ") : text) + "\n");
    return;
  }

  [...el.childNodes].forEach(c => mdFromNode(c, out));
  if (cls.contains("concept-desc") || cls.contains("dt")) out.push("\n\n");
  else if (MD_BLOCK.has(el.tagName)) out.push("\n");
  if (cls.contains("concept-card")) out.push("\n");
}

function mdForTopicHtml(html) {
  const host = document.createElement("div");
  host.innerHTML = html;
  const out = [];
  [...host.childNodes].forEach(c => mdFromNode(c, out));
  // Tidy the prose, and only the prose: a fenced block's leading whitespace is
  // the code's own indentation, and collapsing it would corrupt every example
  // on the site.
  return out.join("")
    .split(/(```[\s\S]*?```)/g)
    .map((chunk, i) => i % 2 ? chunk : chunk
      .replace(/[ \t]{2,}/g, " ")
      .replace(/^[ \t]+/gm, "")
      .replace(/[ \t]+$/gm, ""))
    .join("")
    .replace(/\n{3,}/g, "\n\n")
    .trim() + "\n";
}

/** The raw markup of one topic, from its domain's deferred block. */
function topicHtml(id) {
  const d = topicDomain(id);
  const src = d && domainSection(d)?.querySelector("script.domain-src");
  if (!src) return "";
  const html = src.textContent;
  const marker = `id="${id}"`;
  const at = html.indexOf(marker);
  if (at === -1) return "";
  const start = html.lastIndexOf(TOPIC_OPEN, at);
  const next = html.indexOf(TOPIC_OPEN, at);
  return html.slice(start, next === -1 ? html.length : next);
}

/** Markdown for a set of topics, grouped under their domain headings. */
function mdForTopics(rows, title) {
  const byDomain = new Map();
  rows.forEach(t => {
    if (!byDomain.has(t.domainId)) byDomain.set(t.domainId, []);
    byDomain.get(t.domainId).push(t);
  });
  const parts = [`# ${title}`, "", `_${rows.length} topic${rows.length === 1 ? "" : "s"}, exported ${srsToday()}._`, ""];
  byDomain.forEach((topics, domainId) => {
    const label = topics[0].domainTitle || domainId;
    if (byDomain.size > 1) parts.push(`\n# ${topics[0].domainIcon} ${label}`.trim(), "");
    topics.forEach(t => {
      const md = mdForTopicHtml(topicHtml(t.id));
      if (md.trim()) parts.push(md, "");
    });
  });
  return parts.join("\n").replace(/\n{3,}/g, "\n\n");
}

function stOpenExport(initialScope) {
  stOpen(body => {
    body.innerHTML =
      '<h2 class="st-h">⬇ Export as Markdown</h2>' +
      '<p class="st-bk-lead">Take a topic, a domain or the whole library into a notes app. ' +
      'Tables, code blocks and cross-references come across; the styling does not.</p>' +
      '<div class="st-toolbar"><label class="st-lbl">Export</label>' + stScopeSelectHTML("st-md-scope") +
      '<button id="st-md-go" class="st-btn st-btn-primary">Generate</button></div>' +
      '<div class="st-toolbar"><span class="st-count" id="st-md-size"></span>' +
      '<button id="st-md-copy" class="st-btn" disabled>Copy</button>' +
      '<button id="st-md-dl" class="st-btn" disabled>Download</button></div>' +
      '<textarea id="st-md-out" class="tn-input" rows="12" readonly ' +
      'placeholder="Pick a scope and press Generate."></textarea>';
    const scope = body.querySelector("#st-md-scope");
    if (initialScope) scope.value = initialScope;
    const out = body.querySelector("#st-md-out");
    const size = body.querySelector("#st-md-size");
    const copy = body.querySelector("#st-md-copy");
    const dl = body.querySelector("#st-md-dl");

    const generate = () => {
      const rows = stTopicsForScope(scope.value);
      if (!rows.length) {
        out.value = ""; size.textContent = "Nothing in that scope.";
        copy.disabled = dl.disabled = true;
        return;
      }
      const label = scope.options[scope.selectedIndex].textContent.replace(/\s*\(\d+\)\s*$/, "").trim();
      out.value = mdForTopics(rows, label);
      size.textContent = `${rows.length} topics · ${Math.round(out.value.length / 1024)} KB`;
      copy.disabled = dl.disabled = false;
    };
    body.querySelector("#st-md-go").addEventListener("click", generate);
    copy.addEventListener("click", () => {
      const done = () => { copy.textContent = "Copied"; setTimeout(() => (copy.textContent = "Copy"), 1200); };
      // Selecting the textarea is the fallback that works everywhere, including
      // the contexts where the clipboard API is refused without a prompt.
      if (navigator.clipboard?.writeText) navigator.clipboard.writeText(out.value).then(done).catch(() => { out.select(); done(); });
      else { out.select(); done(); }
    });
    dl.addEventListener("click", () => {
      const blob = new Blob([out.value], { type: "text/markdown" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `techref-${slugify(scope.value === "__all" ? "all-domains" : scope.value)}-${srsToday()}.md`;
      document.body.appendChild(a);
      a.click();
      a.remove();
      setTimeout(() => URL.revokeObjectURL(url), 2000);
    });
    generate();
  });
}

// ── PRINT PACKS ─────────────────────────────────────────────────────────────
// A revision handout: one domain, one learning path or the study list, printed
// with every card open and none of the page's furniture.
//
// Built into a container of its own rather than by styling what happens to be
// on screen. Only one domain is ever hydrated, so "print what is rendered"
// could never span a learning path — and a path is exactly the thing worth
// printing.

function printPackHtml(rows, title) {
  const parts = [`<h1 class="pp-title">${esc(title)}</h1>`,
                 `<p class="pp-meta">${rows.length} topic${rows.length === 1 ? "" : "s"} · ${srsToday()}</p>`];
  let lastDomain = null;
  rows.forEach((t, i) => {
    if (t.domainId !== lastDomain) {
      parts.push(`<h2 class="pp-domain">${esc(t.domainIcon)} ${esc(t.domainTitle || t.domainId)}</h2>`);
      lastDomain = t.domainId;
    }
    const html = topicHtml(t.id);
    if (!html) return;
    // Numbered, because a printed pack has no scrollbar to orient by and a
    // path's order is the whole point of it.
    parts.push(`<section class="pp-topic"><span class="pp-n">${i + 1}</span>${html}</section>`);
  });
  return parts.join("\n");
}

function buildPrintPack(rows, title) {
  document.getElementById("print-pack")?.remove();
  const host = document.createElement("div");
  host.id = "print-pack";
  host.innerHTML = printPackHtml(rows, title);
  // Every card open: a handout with collapsed sections is a list of titles.
  host.querySelectorAll(".topic-header").forEach(h => h.classList.add("open"));
  host.querySelectorAll(".topic-body").forEach(b => b.classList.add("open"));
  // The pack never runs through enhanceDomain, so it has no toggle buttons —
  // classes alone are what the print stylesheet reads.
  document.body.appendChild(host);
  document.body.classList.add("printing");
  return host;
}

function clearPrintPack() {
  document.getElementById("print-pack")?.remove();
  document.body.classList.remove("printing");
}

function stOpenPrint() {
  stOpen(body => {
    const paths = learningPaths();
    body.innerHTML =
      '<h2 class="st-h">🖨 Print pack</h2>' +
      '<p class="st-bk-lead">A revision handout with every card open and none of the page ' +
      'furniture. Print it, or save it as a PDF from the print dialog.</p>' +
      '<div class="st-toolbar"><label class="st-lbl">Pack</label>' +
      '<select id="st-pp-scope" class="st-select">' +
        '<optgroup label="Domains">' + stScopeOptions().map(d =>
          `<option value="d:${esc(d.id)}">${esc(d.icon)} ${esc(d.title)} (${d.n})</option>`).join("") +
        '</optgroup>' +
        (paths.length ? '<optgroup label="Learning paths">' + paths.map(p =>
          `<option value="p:${esc(p.id)}">${esc(p.icon || "🧭")} ${esc(p.name)}</option>`).join("") +
          '</optgroup>' : "") +
        '<optgroup label="Yours">' +
          '<option value="s:__bookmarks">★ My study list</option>' +
          '<option value="s:__due">⏰ Due today</option>' +
        '</optgroup>' +
      '</select>' +
      '<button id="st-pp-go" class="st-btn st-btn-primary">Print</button></div>' +
      '<p class="st-hint" id="st-pp-note"></p>';
    const sel = body.querySelector("#st-pp-scope");
    const note = body.querySelector("#st-pp-note");

    const chosen = () => {
      const [kind, key] = [sel.value.slice(0, 1), sel.value.slice(2)];
      if (kind === "p") {
        const path = learningPaths().find(p => p.id === key);
        return { rows: path ? pathSteps(path) : [], title: path ? path.name : key };
      }
      const rows = stTopicsForScope(key);
      const label = sel.options[sel.selectedIndex].textContent.replace(/\s*\(\d+\)\s*$/, "").trim();
      return { rows, title: label };
    };
    const describe = () => {
      const { rows } = chosen();
      note.textContent = rows.length
        ? `${rows.length} topic${rows.length === 1 ? "" : "s"} in this pack.`
        : "Nothing in that pack yet.";
    };
    sel.addEventListener("change", describe);
    describe();
    body.querySelector("#st-pp-go").addEventListener("click", () => {
      const { rows, title } = chosen();
      if (!rows.length) return;
      buildPrintPack(rows, title);
      stClose();
      // The print dialog is modal, so the cleanup has to be bound to the event
      // rather than run after the call — some browsers return immediately.
      const done = () => { clearPrintPack(); window.removeEventListener("afterprint", done); };
      window.addEventListener("afterprint", done);
      window.print();
      // Belt and braces for browsers that never fire afterprint.
      setTimeout(done, 60000);
    });
  });
}

// ── STREAK ──────────────────────────────────────────────────────────────────
// One record: the last day anything was studied, the run length, and the best
// run. Days rather than sessions, and no list of dates — a streak that needs a
// growing array to answer "how many days in a row" is storing the wrong thing.

function streakGet() {
  try {
    const r = JSON.parse(localStorage.getItem(STREAK_KEY) || "null");
    if (r && typeof r === "object" && typeof r.last === "string") return r;
  } catch { /* corrupt — start again */ }
  return { last: "", n: 0, best: 0 };
}

/**
 * Mark today as studied. Called from every action that means work happened:
 * marking a topic reviewed, starring one, writing a note, grading a card.
 *
 * Yesterday continues the run; anything older starts a new one; today is a
 * no-op, so a busy day counts once.
 */
function streakTouch() {
  const r = streakGet();
  const today = srsToday();
  if (r.last === today) return r;
  r.n = r.last === srsToday(-1) ? r.n + 1 : 1;
  r.last = today;
  r.best = Math.max(r.best || 0, r.n);
  try { localStorage.setItem(STREAK_KEY, JSON.stringify(r)); } catch { /* quota */ }
  return r;
}

/** A run only counts while it is current: yesterday's streak, unfed, is over. */
function streakCurrent() {
  const r = streakGet();
  if (r.last === srsToday() || r.last === srsToday(-1)) return r.n;
  return 0;
}

// ── PROGRESS DASHBOARD ──────────────────────────────────────────────────────
// Every number here already exists in localStorage and in the inlined topic
// index. Nothing is computed from the document, which is the only way this can
// report on all thirty domains when at most one of them is in the DOM.

function progressStats() {
  const idx = topicIndex();
  const rows = [];
  let all = { total: 0, reviewed: 0, bookmarked: 0, known: 0, noted: 0, due: 0 };
  domainSections().forEach(section => {
    const id = section.dataset.domain;
    const ids = idx[id] || [];
    const row = {
      id,
      title: (section.querySelector(".domain-title")?.textContent || id).trim(),
      icon: (section.querySelector(".domain-icon")?.textContent || "").trim(),
      total: ids.length, reviewed: 0, bookmarked: 0, known: 0, noted: 0, due: 0,
    };
    ids.forEach(t => {
      if (safeLS.get(REVIEWED_PREFIX + t) === "1") row.reviewed++;
      if (safeLS.get(BOOKMARK_PREFIX + t) === "1") row.bookmarked++;
      if (safeLS.get(KNOWN_PREFIX + t) === "1") row.known++;
      if (safeLS.get(NOTE_PREFIX + t)) row.noted++;
      if (srsGet(t) && srsIsDue(t)) row.due++;
    });
    rows.push(row);
    Object.keys(all).forEach(k => { all[k] += row[k]; });
  });
  return { rows, all };
}

function stOpenProgress() {
  stOpen(body => {
    const { rows, all } = progressStats();
    const streak = streakCurrent();
    const best = streakGet().best || 0;
    const pct = all.total ? Math.round((all.reviewed / all.total) * 100) : 0;
    // Domains nobody has touched go last: the list is a record of what has been
    // read, and burying that under twenty untouched rows is not a report.
    const sorted = rows.slice().sort((a, b) =>
      (b.reviewed - a.reviewed) || (b.known - a.known) || a.title.localeCompare(b.title));
    body.innerHTML =
      '<h2 class="st-h">📊 Progress</h2>' +
      '<div class="st-pg-top">' +
        `<div class="st-pg-stat"><span class="st-pg-n">${all.reviewed}</span>` +
          `<span class="st-pg-l">of ${all.total} reviewed</span></div>` +
        `<div class="st-pg-stat"><span class="st-pg-n">${pct}%</span>` +
          '<span class="st-pg-l">of the site</span></div>' +
        `<div class="st-pg-stat"><span class="st-pg-n">${streak}</span>` +
          `<span class="st-pg-l">day streak${best > streak ? ` · best ${best}` : ""}</span></div>` +
        `<div class="st-pg-stat"><span class="st-pg-n">${all.due}</span>` +
          '<span class="st-pg-l">due today</span></div>' +
      '</div>' +
      `<p class="st-hint">${all.bookmarked} starred · ${all.known} known · ${all.noted} with a note. ` +
      'Everything here lives in this browser — back it up from the study menu.</p>' +
      '<table class="st-pg-table"><thead><tr><th>Domain</th><th>Reviewed</th><th></th>' +
      '<th>★</th><th>✓</th><th>📝</th></tr></thead><tbody>' +
      sorted.map(r => {
        const p = r.total ? Math.round((r.reviewed / r.total) * 100) : 0;
        return `<tr${r.reviewed ? "" : ' class="untouched"'}>` +
          `<td><button class="st-pg-dom" data-id="${esc(r.id)}">${esc(r.icon)} ${esc(r.title)}</button></td>` +
          `<td class="st-pg-num">${r.reviewed}/${r.total}</td>` +
          `<td class="st-pg-barcell"><div class="st-pg-bar"><div class="st-pg-fill" style="width:${p}%"></div></div></td>` +
          `<td class="st-pg-num">${r.bookmarked || ""}</td>` +
          `<td class="st-pg-num">${r.known || ""}</td>` +
          `<td class="st-pg-num">${r.noted || ""}</td></tr>`;
      }).join("") + '</tbody></table>';
    body.querySelectorAll(".st-pg-dom").forEach(b => b.addEventListener("click", () => {
      stClose();
      const section = domainSection(b.dataset.id);
      section?.scrollIntoView({ behavior: "smooth", block: "start" });
      openDomain(section);
    }));
  });
}

// ── LEARNING PATHS ──────────────────────────────────────────────────────────
// An ordered route through topics that already exist, rendered as a checklist
// against the progress in localStorage. No content of its own — the value is
// entirely in the order, which is why a path costs a few hundred bytes.

let _paths = null;
function learningPaths() {
  if (_paths) return _paths;
  const el = document.getElementById("learning-paths");
  try {
    const p = el ? JSON.parse(el.textContent) : [];
    _paths = Array.isArray(p) ? p : [];
  } catch { _paths = []; }
  return _paths;
}

/** One path's steps, resolved to topics and dropping any that no longer exist. */
function pathSteps(path) {
  const byId = new Map(stIndex().map(t => [t.id, t]));
  return (path.steps || []).map(id => byId.get(id)).filter(Boolean);
}

/** Done means reviewed — the same ✓ the topic header sets, not a second state. */
function pathProgress(path) {
  const steps = pathSteps(path);
  const done = steps.filter(t => safeLS.get(REVIEWED_PREFIX + t.id) === "1").length;
  return { done, total: steps.length };
}

function stOpenPaths() {
  stOpen(body => {
    body.innerHTML = '<h2 class="st-h">🧭 Learning paths</h2><div id="st-paths-body"></div>';
    stRenderPathList(body.querySelector("#st-paths-body"));
  });
}

function stRenderPathList(host) {
  const paths = learningPaths();
  if (!paths.length) {
    host.innerHTML = '<p class="st-empty">No paths are defined.</p>';
    return;
  }
  host.innerHTML =
    '<p class="st-hint">A route through topics that already exist, in an order that builds. ' +
    'A step counts as done when the topic is marked ✓ reviewed.</p>' +
    '<ul class="st-paths">' + paths.map(p => {
      const { done, total } = pathProgress(p);
      const pct = total ? Math.round((done / total) * 100) : 0;
      return `<li class="st-path" data-id="${esc(p.id)}">` +
        `<button class="st-path-open">` +
          `<span class="st-path-icon">${esc(p.icon || "🧭")}</span>` +
          `<span class="st-path-main"><span class="st-path-name">${esc(p.name)}</span>` +
          `<span class="st-path-blurb">${esc(p.blurb || "")}</span>` +
          `<span class="st-path-for">${esc(p["for"] || "")}</span></span>` +
          `<span class="st-path-count">${done}/${total}</span>` +
        `</button>` +
        `<div class="st-path-bar"><div class="st-path-fill" style="width:${pct}%"></div></div>` +
      `</li>`;
    }).join("") + '</ul>';
  host.querySelectorAll(".st-path").forEach(li =>
    li.querySelector(".st-path-open").addEventListener("click", () => {
      const path = learningPaths().find(p => p.id === li.dataset.id);
      if (path) stRenderPath(host, path);
    }));
}

function stRenderPath(host, path) {
  const steps = pathSteps(path);
  const { done, total } = pathProgress(path);
  // The first unreviewed step is where the reader is, and saying so is most of
  // what a path is for — an ordered list without a "you are here" is a list.
  const nextStep = steps.find(t => safeLS.get(REVIEWED_PREFIX + t.id) !== "1");
  host.innerHTML =
    '<button id="st-path-back" class="st-btn">← All paths</button>' +
    `<h3 class="st-path-title">${esc(path.icon || "🧭")} ${esc(path.name)}</h3>` +
    `<p class="st-hint">${esc(path.blurb || "")}</p>` +
    `<p class="st-hint st-path-for">${esc(path["for"] || "")}</p>` +
    `<div class="st-toolbar"><span class="st-count">${done} of ${total} reviewed</span>` +
    (nextStep ? '<button id="st-path-next" class="st-btn st-btn-primary">Continue</button>' : "") +
    '</div>' +
    '<ol class="st-path-steps">' + steps.map((t, i) => {
      const isDone = safeLS.get(REVIEWED_PREFIX + t.id) === "1";
      const here = !isDone && t === nextStep;
      return `<li class="st-path-step${isDone ? " done" : ""}${here ? " here" : ""}">` +
        `<span class="st-step-n">${isDone ? "✓" : i + 1}</span>` +
        `<button class="st-step-link" data-id="${esc(t.id)}">${esc(t.name)}</button>` +
        `<span class="st-step-dom">${esc(t.domainIcon)} ${esc(t.domainId)}</span></li>`;
    }).join("") + '</ol>';
  host.querySelector("#st-path-back").addEventListener("click", () => stRenderPathList(host));
  host.querySelector("#st-path-next")?.addEventListener("click", () => {
    stClose(); stGoToTopic(nextStep.id);
  });
  host.querySelectorAll(".st-step-link").forEach(b =>
    b.addEventListener("click", () => { stClose(); stGoToTopic(b.dataset.id); }));
}

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
    safeLS.remove(BOOKMARK_PREFIX + id);
    document.getElementById(id)?.classList.remove("bookmarked");
    stRenderStudyList(host);
  }));
}
/** Called when a bookmark toggles elsewhere so an open list stays fresh. */
function stRefreshStudyList() {
  const host = document.getElementById("st-list-body");
  if (host && _stOverlay && !_stOverlay.hidden) stRenderStudyList(host);
}

// ── BACKUP (export / import progress) ───────────────────────────────────────
// There is no backend, so the only honest cross-device path is a file the user
// carries themselves. Everything below is local: a Blob download and a
// FileReader, both of which work over file:// as well as https.

const BK_FORMAT = "techref-progress";
const BK_VERSION = 1;

/** Which bucket a localStorage key belongs to, or null if we do not own it. */
function bkCategory(key) {
  if (key.startsWith(REVIEWED_PREFIX)) return "reviewed";
  if (key.startsWith(BOOKMARK_PREFIX)) return "bookmark";
  if (key.startsWith(KNOWN_PREFIX)) return "known";
  if (key.startsWith(SRS_PREFIX)) return "srs";
  if (key.startsWith(NOTE_PREFIX)) return "topicNote";
  if (key === STREAK_KEY) return "streak";
  if (key === NP_STORE_KEY || key === NP_AUTHOR_KEY) return "notes";
  return null;
}

/** Keys whose stored value is itself JSON — exported parsed, so the file reads. */
function bkIsJson(key) {
  return key.startsWith(SRS_PREFIX) || key === NP_STORE_KEY || key === STREAK_KEY;
}

function bkParse(raw) { try { return JSON.parse(raw); } catch { return null; } }

// bkCollect exports JSON-valued keys (srs, notes, streak) *parsed*, so the file
// reads as nested JSON rather than escaped strings — see bkIsJson. localStorage
// only holds strings, so those values must be re-serialised on the way back in.
// Without this, setItem(k, anObject) writes the literal "[object Object]" and a
// restored backup silently loses every SRS schedule, the notepad and the streak.
// bkStored gives the string localStorage stores; bkObj gives the parsed object a
// merge comparison needs — each tolerating a value that is already in the other
// form (a hand-edited file, or a non-JSON key).
function bkStored(v) { return typeof v === "string" ? v : JSON.stringify(v); }
function bkObj(v) { return typeof v === "string" ? bkParse(v) : v; }

/** Every key we own, with JSON values expanded. */
function bkCollect() {
  const data = {};
  for (const k of safeLS.keys()) {
    if (!bkCategory(k)) continue;
    const raw = safeLS.get(k);
    if (raw === null) continue;
    const parsed = bkIsJson(k) ? bkParse(raw) : null;
    data[k] = parsed === null ? raw : parsed;
  }
  return data;
}

function bkCounts(data) {
  const c = { reviewed: 0, bookmark: 0, known: 0, srs: 0, topicNote: 0, notes: 0, streak: 0 };
  Object.keys(data).forEach(k => {
    const cat = bkCategory(k);
    if (!cat) return;
    if (cat === "notes") {
      if (k === NP_STORE_KEY) c.notes += Array.isArray(data[k]) ? data[k].length : 0;
    } else c[cat]++;
  });
  return c;
}

function bkExport() {
  const data = bkCollect();
  const payload = {
    format: BK_FORMAT,
    version: BK_VERSION,
    exported: new Date().toISOString(),
    counts: bkCounts(data),
    data
  };
  const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `techref-progress-${srsToday()}.json`;
  document.body.appendChild(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 2000);
  return payload;
}

/**
 * Parse and vet a file before anything touches storage. Throws with a message
 * meant to be read by a person, not a console.
 */
function bkValidate(text) {
  let obj;
  try { obj = JSON.parse(text); }
  catch { throw new Error("That file is not valid JSON — it may have been edited or truncated."); }
  if (!obj || typeof obj !== "object" || Array.isArray(obj))
    throw new Error("That file does not contain a progress object.");
  if (obj.format !== BK_FORMAT)
    throw new Error(`Not a study-progress file. Expected "format": "${BK_FORMAT}".`);
  if (obj.version !== BK_VERSION)
    throw new Error(`This file says version ${JSON.stringify(obj.version)}; this page understands version ${BK_VERSION} only.`);
  if (!obj.data || typeof obj.data !== "object" || Array.isArray(obj.data))
    throw new Error('That file has no "data" section.');
  return obj;
}

/**
 * Turn one imported entry into the exact string localStorage should hold, or
 * null to drop it. This is the gate that stops a hand-edited file from writing
 * arbitrary keys or arbitrary shapes.
 */
function bkSerialise(key, v) {
  if (key.startsWith(SRS_PREFIX)) {
    const r = typeof v === "string" ? bkParse(v) : v;
    if (!r || typeof r !== "object" || Array.isArray(r)) return null;
    if (typeof r.d !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(r.d)) return null;
    const e = Number(r.e), i = Number(r.i), n = Number(r.n);
    return JSON.stringify({
      e: Number.isFinite(e) ? Math.min(4, Math.max(1.3, e)) : 2.5,
      i: Number.isFinite(i) && i > 0 ? Math.round(i) : 1,
      d: r.d,
      n: Number.isFinite(n) && n >= 0 ? Math.round(n) : 0
    });
  }
  if (key === NP_STORE_KEY) {
    const a = typeof v === "string" ? bkParse(v) : v;
    return Array.isArray(a) ? JSON.stringify(a) : null;
  }
  if (key === NP_AUTHOR_KEY) return typeof v === "string" ? v.slice(0, 80) : null;
  if (key === STREAK_KEY) {
    const r = typeof v === "string" ? bkParse(v) : v;
    if (!r || typeof r !== "object" || Array.isArray(r)) return null;
    if (typeof r.last !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(r.last)) return null;
    const n = Number(r.n), best = Number(r.best);
    return JSON.stringify({
      last: r.last,
      n: Number.isFinite(n) && n >= 0 ? Math.round(n) : 0,
      best: Number.isFinite(best) && best >= 0 ? Math.round(best) : 0,
    });
  }
  // A per-topic note is free text, so it is the one key here with no shape to
  // check beyond "a non-empty string, truncated to what the editor allows".
  if (key.startsWith(NOTE_PREFIX)) {
    if (typeof v !== "string") return null;
    const t = v.slice(0, NOTE_MAX).trim();
    return t || null;
  }
  // reviewed / bookmark / known are plain flags
  return (v === "1" || v === 1 || v === true) ? "1" : null;
}

/** Split an imported data block into what we will write and what we refused. */
function bkSanitise(data) {
  const kept = {};
  let skipped = 0;
  Object.keys(data).forEach(k => {
    if (!bkCategory(k)) { skipped++; return; }
    const s = bkSerialise(k, data[k]);
    if (s === null) { skipped++; return; }
    kept[k] = s;
  });
  return { kept, skipped };
}

/** Keys we own that are in storage right now — the blast radius of "replace". */
function bkOwnedKeys() {
  return safeLS.keys().filter(bkCategory);
}

/**
 * What an import would change, without changing it. `merge` reports the
 * scheduling entries it would leave alone, which is the number people actually
 * want to see before they commit.
 */
function bkDiff(kept, mode) {
  const d = { add: 0, overwrite: 0, keepLocal: 0, remove: 0 };
  if (mode === "replace") d.remove = bkOwnedKeys().filter(k => !(k in kept)).length;
  Object.keys(kept).forEach(k => {
    const mine = safeLS.get(k);
    if (mine === null) { d.add++; return; }
    if (mode === "merge" && k.startsWith(SRS_PREFIX)) {
      const a = bkParse(mine), b = bkObj(kept[k]);
      if (a && b && typeof a.d === "string" && a.d > b.d) { d.keepLocal++; return; }
    }
    if (mine === bkStored(kept[k])) d.keepLocal++; else d.overwrite++;
  });
  return d;
}

/**
 * Write the vetted keys.
 *   merge   — union; for a topic scheduled on both sides the later due date
 *             wins, so importing can never pull a card forward unexpectedly.
 *   replace — drop everything we own first, then write the file verbatim.
 */
function bkApply(kept, mode) {
  if (mode === "replace") bkOwnedKeys().forEach(k => safeLS.remove(k));
  Object.keys(kept).forEach(k => {
    if (mode === "merge" && k.startsWith(SRS_PREFIX)) {
      const mine = safeLS.get(k);
      if (mine) {
        const a = bkParse(mine), b = bkObj(kept[k]);
        if (a && b && typeof a.d === "string" && a.d > b.d) return;   // local is later
      }
    }
    try { localStorage.setItem(k, bkStored(kept[k])); } catch { /* quota — skip the rest of this key */ }
  });
}

/** Re-read storage into the page so an import is visible without a reload. */
function bkRefreshUI() {
  // Only the open domain has topics to repaint; every other domain reads the
  // imported storage when it is next opened, and its badge is recomputed below.
  document.querySelectorAll(".topic[id]").forEach(t => {
    t.classList.toggle("reviewed", safeLS.get(REVIEWED_PREFIX + t.id) === "1");
    t.classList.toggle("bookmarked", safeLS.get(BOOKMARK_PREFIX + t.id) === "1");
  });
  domainSections().forEach(d => updateDomainProgress(d));
  srsUpdateBadge();
  if (typeof stRefreshStudyList === "function") stRefreshStudyList();
}

function bkCountLine(c) {
  // Two kinds of note, and conflating them would misreport a restore: `notes`
  // is the shared notepad's entries, `topicNote` is one note pinned to a topic.
  const pin = c.topicNote || 0;
  return `${c.reviewed} reviewed · ${c.bookmark} starred · ${c.known} known · ` +
         `${c.srs} scheduled · ${pin} topic note${pin === 1 ? "" : "s"} · ` +
         `${c.notes} notepad note${c.notes === 1 ? "" : "s"}`;
}

function stOpenBackup() {
  stOpen(body => {
    const here = bkCounts(bkCollect());
    body.innerHTML =
      '<h2 class="st-h">💾 Back up &amp; restore</h2>' +
      '<p class="st-bk-lead">Progress lives in this browser only. Export a file to move it to another ' +
      'device — or to keep it before clearing site data.</p>' +
      `<div class="st-bk-block"><div class="st-bk-head">On this device</div>` +
      `<p class="st-bk-now">${esc(bkCountLine(here))}</p>` +
      '<button id="st-bk-export" class="st-btn st-btn-primary">Export to file</button></div>' +
      '<div class="st-bk-block"><div class="st-bk-head">Restore from a file</div>' +
      '<div class="st-toolbar"><label class="st-lbl" for="st-bk-mode">Mode</label>' +
      '<select id="st-bk-mode" class="st-select">' +
        '<option value="merge">Merge — keep both, later review date wins</option>' +
        '<option value="replace">Replace — wipe local progress first</option>' +
        '<option value="preview">Preview — show what would change, write nothing</option>' +
      '</select></div>' +
      '<input id="st-bk-file" class="st-bk-file" type="file" accept="application/json,.json" />' +
      '<div id="st-bk-out" class="st-bk-out" role="status" aria-live="polite"></div></div>';

    const out = body.querySelector("#st-bk-out");
    const mode = body.querySelector("#st-bk-mode");
    const file = body.querySelector("#st-bk-file");

    body.querySelector("#st-bk-export").addEventListener("click", () => {
      const p = bkExport();
      out.className = "st-bk-out st-bk-ok";
      out.textContent = `Exported ${bkCountLine(p.counts)} — check your downloads.`;
    });

    let pending = null;   // { kept, skipped, payload } waiting on a confirm click

    const readFile = f => {
      const reader = new FileReader();
      reader.onerror = () => {
        out.className = "st-bk-out st-bk-err";
        out.textContent = "Could not read that file.";
      };
      reader.onload = () => {
        let payload;
        try { payload = bkValidate(String(reader.result)); }
        catch (err) {
          pending = null;
          out.className = "st-bk-out st-bk-err";
          out.textContent = err.message;
          return;
        }
        const { kept, skipped } = bkSanitise(payload.data);
        const m = mode.value;
        const diff = bkDiff(kept, m);
        pending = { kept, mode: m };

        const rows = [
          ["In the file", bkCountLine(bkCounts(payload.data))],
          ["New entries", String(diff.add)],
          [m === "merge" ? "Overwritten" : "Changed", String(diff.overwrite)],
          ["Left as-is", String(diff.keepLocal)]
        ];
        if (m === "replace") rows.push(["Deleted from this device", String(diff.remove)]);
        if (skipped) rows.push(["Ignored (unknown key or bad shape)", String(skipped)]);

        out.className = "st-bk-out";
        out.innerHTML =
          '<dl class="st-bk-diff">' + rows.map(([k, v]) =>
            `<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join("") + "</dl>" +
          (m === "preview"
            ? '<p class="st-hint">Preview only — nothing has been written.</p>'
            : `<button id="st-bk-go" class="st-btn ${m === "replace" ? "st-btn-again" : "st-btn-primary"}">` +
              `${m === "replace" ? "Replace my progress" : "Merge into this device"}</button>`);

        out.querySelector("#st-bk-go")?.addEventListener("click", () => {
          if (!pending) return;
          // The notepad renders from a closure, so only it needs a reload.
          const touchedNotes = NP_STORE_KEY in pending.kept;
          bkApply(pending.kept, pending.mode);
          bkRefreshUI();
          pending = null;
          out.className = "st-bk-out st-bk-ok";
          out.innerHTML = `Restored. This device now holds ${esc(bkCountLine(bkCounts(bkCollect())))}.` +
            (touchedNotes ? ' <button id="st-bk-reload" class="st-link">Reload to refresh notes</button>' : "");
          out.querySelector("#st-bk-reload")?.addEventListener("click", () => location.reload());
        });
      };
      reader.readAsText(f);
    };

    file.addEventListener("change", () => { if (file.files && file.files[0]) readFile(file.files[0]); });
    // Changing the mode after picking a file should re-cost the same file.
    mode.addEventListener("change", () => { if (file.files && file.files[0]) readFile(file.files[0]); });
  });
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
      '<button class="study-mi" data-act="paths"><span>🧭</span> Learning paths</button>' +
      '<button class="study-mi" data-act="exam"><span>📋</span> Exam mode</button>' +
      '<button class="study-mi" data-act="progress"><span>📊</span> Progress</button>' +
      '<button class="study-mi" data-act="md"><span>⬇</span> Export as Markdown</button>' +
      '<button class="study-mi" data-act="print"><span>🖨</span> Print pack</button>' +
      '<button class="study-mi" data-act="backup"><span>💾</span> Back up &amp; restore</button>' +
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
       acro: stOpenAcroQuiz, list: stOpenStudyList, paths: stOpenPaths,
       progress: stOpenProgress, exam: stOpenExam, md: stOpenExport,
       print: stOpenPrint,
       backup: stOpenBackup }[mi.dataset.act])();
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
/**
 * Offer a reload when a new version is waiting.
 *
 * The worker no longer calls skipWaiting() on install, so a new version sits in
 * `waiting` until someone accepts it. That is the point: swapping the assets
 * under an open page is how a reader ends up with a new script.js and an old
 * index.html, and on a page that keeps their progress in localStorage that is
 * not a cosmetic problem.
 *
 * Rendered rather than alert()ed, and dismissible: an update is worth
 * mentioning once, not insisting on.
 */
function showUpdateToast(worker) {
  if (document.getElementById("update-toast")) return null;
  const bar = document.createElement("div");
  bar.id = "update-toast";
  bar.setAttribute("role", "status");
  bar.innerHTML =
    '<span class="ut-text">A newer version of this page is ready.</span>' +
    '<button type="button" class="ut-go">Reload</button>' +
    '<button type="button" class="ut-dismiss" aria-label="Dismiss">✕</button>';
  bar.querySelector(".ut-go").addEventListener("click", () => {
    bar.querySelector(".ut-go").textContent = "Reloading…";
    // The worker takes over, fires controllerchange, and the page reloads once.
    // Without the guard a page can reload in a loop when several tabs accept.
    worker?.postMessage({ type: "skip-waiting" });
    if (!worker) location.reload();
  });
  bar.querySelector(".ut-dismiss").addEventListener("click", () => bar.remove());
  document.body.appendChild(bar);
  return bar;
}

if ("serviceWorker" in navigator && location.protocol.startsWith("http")) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("/sw.js").then(reg => {
      if (reg.waiting) showUpdateToast(reg.waiting);
      reg.addEventListener("updatefound", () => {
        const installing = reg.installing;
        installing?.addEventListener("statechange", () => {
          // "installed" with a controller already present means an update, not
          // a first install — the first install has nothing to replace.
          if (installing.state === "installed" && navigator.serviceWorker.controller) {
            showUpdateToast(installing);
          }
        });
      });
    }).catch(() => {});
    let reloading = false;
    navigator.serviceWorker.addEventListener("controllerchange", () => {
      if (reloading) return;
      reloading = true;
      location.reload();
    });
  });
}
