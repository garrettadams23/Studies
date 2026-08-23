#!/usr/bin/env node
/**
 * smoke_test.mjs — Drives the built index.html in a real browser.
 *
 * plan.md has claimed "verified headless (Chromium)" since the first review, and
 * every session that changed structure re-derived a throwaway script to justify
 * it. That is the same shape as the cheat sheet's "Generated from the Math
 * domain" header: a capability asserted in prose with nothing checking it. This
 * is the check.
 *
 * It is deliberately about *behaviour a structural change can break* — decks
 * built per domain, permalinks derived from titles, progress keyed by slug —
 * rather than pixels. Folding a domain or moving a card between domains touches
 * every one of those.
 *
 * Since only one domain's content is in the document at a time, most of these
 * checks have to say which domain they mean and open it first. That is not
 * ceremony: a check that reads `document.querySelectorAll(".topic")` now
 * answers for a twenty-ninth of the site and passes, which is precisely the
 * silent-partial-result failure the design has to be held away from. Anything
 * page-wide is asserted against the inlined topic index instead.
 *
 * Usage:
 *   node tools/smoke_test.mjs                 # build first; this only reads
 *   node tools/smoke_test.mjs --url <file://> # non-default page
 */

import { existsSync } from "fs";
import { resolve } from "path";
import { createRequire } from "module";

// Resolve playwright from wherever it is: a local node_modules (CI does
// `npm install playwright`), or a global install (developer machines, and this
// project has no package.json to hang a dependency off).
const chromium = await (async () => {
  try {
    return (await import("playwright")).chromium;
  } catch {
    const require = createRequire(import.meta.url);
    for (const base of ["/opt/node22/lib/node_modules", "/usr/lib/node_modules",
                        "/usr/local/lib/node_modules"]) {
      try {
        return (await import(`${base}/playwright/index.mjs`)).chromium;
      } catch { /* try the next one */ }
    }
    console.error("error: playwright not found. Install it with 'npm install playwright'.");
    process.exit(1);
  }
})();

const ROOT = resolve(new URL("..", import.meta.url).pathname);
const argUrl = process.argv.indexOf("--url");
const PAGE = argUrl > -1 ? process.argv[argUrl + 1] : `file://${ROOT}/index.html`;

if (PAGE.startsWith("file://") && !existsSync(PAGE.slice(7))) {
  console.error(`error: ${PAGE.slice(7)} does not exist — run 'python build.py' first.`);
  process.exit(1);
}

const results = [];
const check = (name, pass, detail = "") => {
  results.push({ name, pass, detail });
  console.log(`${pass ? "ok  " : "FAIL"} : ${name}${detail ? `  — ${detail}` : ""}`);
};

/** Run a step that drives the page; a broken page must fail a check, not crash.
 *  Without this a missing #study-fab throws a 30s TimeoutError and the run ends
 *  with a stack trace and no summary — unreadable exactly when it matters. */
const step = async (name, fn, fallback = null) => {
  try {
    return await fn();
  } catch (e) {
    check(name, false, String(e.message || e).split("\n")[0].slice(0, 90));
    return fallback;
  }
};

const browser = await chromium.launch();
const context = await browser.newContext();
const page = await context.newPage();
const consoleErrors = [];
const offsite = [];
page.on("console", m => { if (m.type() === "error") consoleErrors.push(m.text()); });
page.on("pageerror", e => consoleErrors.push(`pageerror: ${e.message}`));
page.on("request", r => { if (!r.url().startsWith("file://")) offsite.push(r.url()); });

await page.goto(PAGE, { waitUntil: "load" });

/** Open one domain by clicking its header, and wait for the content to arrive.
 *  "attached", not "visible": during a search the domain's non-matching topics
 *  are hidden, and the first one usually is. */
const openDomain = async (id) => {
  // The header toggles, so clicking an already-open domain would close it —
  // and a deep link or a search may have opened it before this call.
  const already = await page.evaluate(d =>
    document.querySelector(`.domain-section[data-domain="${d}"]`)?.dataset.hydrated === "1", id);
  if (!already) await page.locator(`.domain-section[data-domain="${id}"] .domain-header`).click();
  await page.waitForSelector(`.domain-section[data-domain="${id}"] .topic`,
    { state: "attached", timeout: 5000 });
};

// ── structure ───────────────────────────────────────────────────────────────
const structure = await page.evaluate(() => {
  const chips = [...document.querySelectorAll(".chip[data-domain]")].map(c => c.dataset.domain);
  const sections = [...document.querySelectorAll(".domain-section[data-domain]")]
    .map(e => e.dataset.domain);
  const index = JSON.parse(document.getElementById("topic-index").textContent);
  return {
    chips, sections, index,
    indexed: Object.values(index).reduce((n, v) => n + v.length, 0),
    inDom: document.querySelectorAll(".topic").length,
    deferred: document.querySelectorAll("script.domain-src").length,
  };
});
// Every chip must have a section and vice versa: a domain removed from one and
// left in the other is exactly the breakage a fold causes, and it is silent.
const chipSet = new Set(structure.chips.filter(d => d !== "all"));
const secSet = new Set(structure.sections);
const orphanChips = [...chipSet].filter(d => !secSet.has(d));
const orphanSections = [...secSet].filter(d => !chipSet.has(d));
check("every filter chip has a domain section", orphanChips.length === 0, orphanChips.join(", "));
check("every domain section has a filter chip", orphanSections.length === 0, orphanSections.join(", "));
check("topics present", structure.indexed > 0,
  `${structure.indexed} topics, ${secSet.size} domains`);

// ── the deferral itself ─────────────────────────────────────────────────────
// The point of the build: every domain ships its content, none of it is markup
// until asked for. A regression here is silent — the page looks identical and
// simply costs what it used to.
check("no domain content in the document at load", structure.inDom === 0,
  `${structure.inDom} topic elements before any domain is opened`);
check("every domain has a deferred content block",
  structure.deferred === structure.sections.length,
  `${structure.deferred} blocks for ${structure.sections.length} domains`);

const [firstDomain, secondDomain] = structure.sections;
await step("opening a domain renders exactly that domain", async () => {
  await openDomain(firstDomain);
  const one = await page.evaluate(() => ({
    hydrated: [...document.querySelectorAll('.domain-section[data-hydrated="1"]')].map(s => s.dataset.domain),
    topics: document.querySelectorAll(".topic").length,
  }));
  check("opening a domain renders exactly that domain",
    one.hydrated.length === 1 && one.hydrated[0] === firstDomain && one.topics > 0,
    `${one.hydrated.join(", ") || "none"} · ${one.topics} topics`);

  // The eviction is the feature. Without it the page grows back to its old size
  // over a browsing session, one domain at a time, and nothing would say so.
  await openDomain(secondDomain);
  const two = await page.evaluate(() => ({
    hydrated: [...document.querySelectorAll('.domain-section[data-hydrated="1"]')].map(s => s.dataset.domain),
    stale: document.querySelectorAll(".domain-section:not([data-hydrated]) .topic").length,
  }));
  check("opening a second domain drops the first",
    two.hydrated.length === 1 && two.hydrated[0] === secondDomain && two.stale === 0,
    `${two.hydrated.join(", ")} live · ${two.stale} orphaned topics`);
});

// The ids the page routes on are stamped at build time; the ones the browser
// sees have to be the same ones, or every permalink resolves to a domain and
// then finds nothing in it.
const domIds = await page.evaluate(d =>
  [...document.querySelectorAll(`.domain-section[data-domain="${d}"] .topic`)].map(t => t.id),
  secondDomain);
const indexIds = structure.index[secondDomain] || [];
check("rendered topic ids match the inlined index",
  domIds.length === indexIds.length && domIds.every((id, i) => id === indexIds[i]),
  `${secondDomain}: ${domIds.length} rendered vs ${indexIds.length} indexed`);
await page.goto(PAGE, { waitUntil: "load" });

// ── every topic has a unique, non-empty id (permalinks depend on it) ────────
// From the index, which is the page-wide answer; the previous check confirmed
// the index and the rendered markup agree.
const ids = Object.values(structure.index).flat();
const dupes = ids.filter((id, i) => id && ids.indexOf(id) !== i);
check("every topic has an id", ids.every(Boolean), `${ids.filter(x => !x).length} missing`);
check("topic ids are unique", dupes.length === 0, [...new Set(dupes)].slice(0, 3).join(", "));

// ── permalinks: cold-load a hash and confirm it expands the right card ──────
const sample = ids.filter(Boolean).filter((_, i) => i % Math.ceil(ids.length / 5) === 0).slice(0, 5);
let permalinkFails = [];
for (const id of sample) {
  await page.goto(`${PAGE}#${id}`, { waitUntil: "load" });
  await page.waitForTimeout(450);
  const ok = await page.evaluate(i => {
    const t = document.getElementById(i);
    const body = t?.querySelector(".topic-body");
    return !!t && !!body && body.classList.contains("open") && body.offsetParent !== null;
  }, id);
  if (!ok) permalinkFails.push(id);
}
check("permalinks expand their topic", permalinkFails.length === 0, permalinkFails.join(", "));

// ── card-level permalinks: #topic/2 lands on that card, not just the topic ───
// Both halves matter. Landing on the wrong card is a silent wrong answer, and
// an index past the end has to fall back to the topic rather than doing
// nothing — links outlive the cards they were written against.
// Pick a topic that actually has several concept cards. The id map only knows
// ids, and card counts live in the deferred text, so a domain is opened and
// asked. Choosing the first id blindly picked a single-card topic and let the
// check pass without exercising anything.
await page.goto(PAGE, { waitUntil: "load" });
const cardProbeDomain = await page.evaluate(() =>
  document.querySelector(".domain-section")?.dataset.domain || null);
await openDomain(cardProbeDomain);
await page.waitForTimeout(250);
const cardTarget = await page.evaluate(() => {
  const t = [...document.querySelectorAll(".topic")]
    .find(x => x.id && x.querySelectorAll(".topic-body > .concept-card").length >= 3);
  return t ? t.id : null;
});
check("found a multi-card topic to test card links against", !!cardTarget, cardTarget || "none");
if (cardTarget) {
  await page.goto(`${PAGE}#${cardTarget}/2`, { waitUntil: "load" });
  await page.waitForTimeout(600);
  const hit = await page.evaluate(id => {
    const t = document.getElementById(id);
    const cards = t ? [...t.querySelectorAll(".topic-body > .concept-card")] : [];
    return { cards: cards.length, marked: cards.findIndex(c => c.classList.contains("card-linked")) };
  }, cardTarget);
  check("a card-level link marks that card",
    hit.cards >= 3 && hit.marked === 1,
    `${cardTarget}: ${hit.cards} cards, marked index ${hit.marked}`);

  await page.waitForTimeout(2400);   // let the mark expire before the next case
  await page.goto(`${PAGE}#${cardTarget}/99`, { waitUntil: "load" });
  await page.waitForTimeout(600);
  const over = await page.evaluate(id => ({
    open: !!document.getElementById(id)?.querySelector(".topic-body.open"),
    marked: !!document.querySelector(".concept-card.card-linked"),
  }), cardTarget);
  check("an out-of-range card index falls back to the topic",
    over.open && !over.marked, `open=${over.open} marked=${over.marked}`);
}

// ── per-domain size hints ───────────────────────────────────────────────────
// build.py computes these from the real word count; a missing or zero-topic
// meta means the stats function stopped seeing the body it measures.
const meta = await page.evaluate(() =>
  [...document.querySelectorAll(".domain-section")].map(s => ({
    domain: s.dataset.domain,
    text: s.querySelector(".domain-meta")?.textContent.trim() || null,
  })));
const missing = meta.filter(m => !m.text).map(m => m.domain);
const zero = meta.filter(m => m.text && /^0 topics/.test(m.text)).map(m => m.domain);
check("every domain has a size hint", missing.length === 0, missing.join(", "));
check("no domain reports 0 topics", zero.length === 0, zero.join(", "));

// ── search ──────────────────────────────────────────────────────────────────
// Search reads the deferred text, so it still covers all 29 domains while only
// one of them is rendered. Both halves are checked: the open domain shows its
// hits, and the domains that are not open still report theirs. A search that
// silently shrank to the open domain would pass the first half alone.
await page.goto(PAGE, { waitUntil: "load" });
await page.fill("#search-input", "kerberos");
await page.waitForTimeout(400);
const search = await page.evaluate(() => ({
  visible: [...document.querySelectorAll(".topic")].filter(t => t.offsetParent !== null).length,
  live: document.querySelectorAll('.domain-section[data-hydrated="1"]').length,
  badged: [...document.querySelectorAll(".domain-section:not(.search-hidden) .domain-matches")].length,
  count: document.getElementById("search-count")?.textContent || "",
}));
check("search narrows the page", search.visible > 0 && search.visible < 200,
  `${search.visible} visible`);
check("search still reaches unopened domains", search.badged > 1 && search.live === 1,
  `${search.badged} domains matched, ${search.live} rendered · ${search.count}`);

// Opening one of those collapsed domains has to land on the same result the
// count promised, not on the whole domain.
const otherDomain = await page.evaluate(() => {
  const live = document.querySelector('.domain-section[data-hydrated="1"]')?.dataset.domain;
  return [...document.querySelectorAll(".domain-section:not(.search-hidden)")]
    .map(s => s.dataset.domain).find(d => d !== live) || null;
});
if (otherDomain) {
  await openDomain(otherDomain);
  await page.waitForTimeout(250);
  const crossed = await page.evaluate(d => {
    const sec = document.querySelector(`.domain-section[data-domain="${d}"]`);
    const shown = [...sec.querySelectorAll(".topic")].filter(t => !t.classList.contains("search-hidden"));
    const promised = parseInt(sec.querySelector(".domain-matches")?.textContent || "0", 10);
    return { shown: shown.length, promised, marks: sec.querySelectorAll("mark.sh").length };
  }, otherDomain);
  check("a domain opened during a search shows its matches",
    crossed.shown === crossed.promised && crossed.promised > 0 && crossed.marks > 0,
    `${otherDomain}: ${crossed.shown} shown of ${crossed.promised} promised, ${crossed.marks} highlights`);
}
// ── search operators ────────────────────────────────────────────────────────
// `domain:` and quoted phrases narrow a 1,300-topic site to something a reader
// can use. The cases worth protecting are the ones that fail quietly: an
// operator that is ignored answers a different question than the one asked, and
// looks like a result rather than a mistake.
const ops = await page.evaluate(async () => {
  const el = document.getElementById("search-input");
  const probe = async q => {
    el.value = q;
    el.dispatchEvent(new Event("input", { bubbles: true }));
    await new Promise(r => setTimeout(r, 350));
    const n = document.getElementById("search-count")?.textContent || "";
    const m = n.match(/^(\d+) match/);
    return { text: n, hits: m ? Number(m[1]) : 0,
             domains: [...document.querySelectorAll(".domain-section:not(.search-hidden)")].length };
  };
  const out = {};
  out.bare      = await probe("firewall");
  out.scoped    = await probe("domain:net firewall");
  out.unknownDm = await probe("domain:nosuchdomain firewall");
  out.phrase    = await probe('"shuffle sharding"');
  out.nonsense  = await probe('"shuffle sharding" biscuits');
  out.shortText = await probe("domain:hw x");
  return out;
});
check("domain: narrows the search", ops.scoped.hits > 0 && ops.scoped.hits < ops.bare.hits
  && ops.scoped.domains === 1,
  `${ops.bare.hits} unscoped -> ${ops.scoped.hits} in ${ops.scoped.domains} domain`);
check("an unknown domain: yields nothing, not everything", ops.unknownDm.hits === 0,
  ops.unknownDm.text);
check("a quoted phrase matches", ops.phrase.hits > 0, ops.phrase.text);
check("phrase and free text are combined, not merged", ops.nonsense.hits === 0,
  ops.nonsense.text);
check("free text too short to use rejects the query rather than dropping it",
  ops.shortText.hits === 0, ops.shortText.text || "(cleared)");

await page.fill("#search-input", "");
await page.waitForTimeout(250);

// ── study decks: one option per studyable domain, plus the three special ────
const deck = await step("study tools open", async () => {
  await page.click("#study-fab", { timeout: 5000 });
  await page.click('.study-mi[data-act="cards"]', { timeout: 5000 });
  await page.waitForTimeout(350);
  return page.evaluate(() => {
    const sel = document.querySelector("#st-modal select");
    return sel ? {
      n: sel.options.length,
      values: [...sel.options].map(o => o.value),
      labels: [...sel.options].map(o => o.textContent.trim()),
    } : null;
  });
});
check("flashcard deck picker exists", !!deck);
if (deck) {
  const domainOpts = deck.values.filter(v => !v.startsWith("__"));
  const missing = [...secSet].filter(d => d !== "acronym" && !domainOpts.includes(d));
  const extra = domainOpts.filter(d => !secSet.has(d));
  check("a deck for every studyable domain", missing.length === 0, missing.join(", "));
  check("no deck for a domain that is gone", extra.length === 0, extra.join(", "));
  // A deck labelled (0) means the domain's cards did not reach the deck builder.
  const empty = deck.labels.filter(l => /\(0\)$/.test(l));
  check("no empty decks", empty.length === 0, empty.join(", "));
}
await page.keyboard.press("Escape");
await page.waitForTimeout(200);

// ── progress round-trip, on a real card ─────────────────────────────────────
const target = ids.find(Boolean);
const persisted = await step("reviewed state persists across reload", async () => {
  await page.goto(`${PAGE}#${target}`, { waitUntil: "load" });
  await page.waitForTimeout(500);
  // Attribute selector, not `#id`: slugs are ASCII but may start with a digit,
  // which is a valid id and an invalid bare CSS id selector.
  await page.locator(`[id="${target}"] .topic-review`).first().click({ timeout: 5000 });
  await page.waitForTimeout(200);
  await page.reload({ waitUntil: "load" });
  await page.waitForTimeout(500);
  return page.evaluate(
    id => localStorage.getItem(`reviewed:${id}`) === "1" &&
          document.getElementById(id)?.classList.contains("reviewed"), target);
}, "threw");
if (persisted !== "threw") check("reviewed state persists across reload", persisted, target);

// ── acronym expansion density ───────────────────────────────────────────────
// Three modes on a class on <body>, with a stored preference. Worth a check
// because the failure is silent in both directions: a mode that stops applying
// leaves expansions on for a reader who turned them off, and a preference that
// stops persisting resets on every visit without erroring.
const acro = await step("acronym density toggle cycles and persists", async () => {
  await page.goto(PAGE, { waitUntil: "load" });
  await page.waitForTimeout(400);
  const seen = [];
  for (let i = 0; i < 4; i++) {
    seen.push(await page.evaluate(() =>
      document.body.className.match(/acro-(hover|off)/)?.[1] || "always"));
    await page.click("#hdr-acro-btn");
    await page.waitForTimeout(120);
  }
  const cycled = seen.join(">") === "always>hover>off>always";
  // The stored preference has to survive a reload, which is the whole point of
  // storing it rather than keeping it in a variable.
  await page.evaluate(() => localStorage.setItem("acro-density", "off"));
  await page.reload({ waitUntil: "load" });
  await page.waitForTimeout(400);
  const kept = await page.evaluate(() => document.body.classList.contains("acro-off"));
  return { cycled, kept, seen: seen.join(" > ") };
});
if (acro !== "threw") {
  check("acronym density cycles always > hover > off", acro.cycled, acro.seen);
  check("acronym density preference survives a reload", acro.kept, acro.kept ? "acro-off" : "lost");
}
await page.evaluate(() => localStorage.removeItem("acro-density")).catch(() => {});

// ── recently viewed in the quick-jump palette ───────────────────────────────
// The palette opens on an empty query, and what it shows first is the only
// thing most readers ever see of it. Checked because both halves fail quietly:
// visits that stop being recorded leave an arbitrary list, and recent rows that
// leak into a filtered query put the wrong topics above the matches.
const recent = await step("quick jump leads with recently viewed", async () => {
  await page.goto(PAGE, { waitUntil: "load" });
  await page.evaluate(() => localStorage.removeItem("recent-topics"));
  await page.waitForTimeout(300);
  const visited = await page.evaluate(() => {
    const idx = typeof topicIndex === "function" ? topicIndex() : {};
    return Object.values(idx).flat().slice(0, 3);
  });
  for (const id of visited) {
    await page.evaluate(i => { location.hash = i; }, id);
    await page.waitForTimeout(400);
  }
  const stored = await page.evaluate(() => JSON.parse(localStorage.getItem("recent-topics") || "[]"));
  await page.evaluate(() => stOpenJump());
  await page.waitForTimeout(300);
  const led = await page.evaluate(n => {
    const rows = [...document.querySelectorAll(".st-jump-item")].slice(0, n);
    return rows.length === n && rows.every(r => !!r.querySelector(".st-jump-recent"));
  }, visited.length);
  await page.fill("#st-jump-input", "kerberos");
  await page.waitForTimeout(250);
  const leaked = await page.evaluate(() => !!document.querySelector(".st-jump-recent"));
  return { newestFirst: stored[0] === visited[visited.length - 1], count: stored.length, led, leaked };
});
if (recent !== "threw") {
  check("visits are recorded newest-first", recent.newestFirst && recent.count === 3,
    `${recent.count} recorded`);
  check("the palette's empty query leads with them", recent.led, recent.led ? "all badged" : "not led");
  check("recent rows do not leak into a filtered query", !recent.leaked,
    recent.leaked ? "badge present under query" : "none");
}
await page.evaluate(() => localStorage.removeItem("recent-topics")).catch(() => {});

// ── theming: every marked volatile claim, and the topology diagrams ─────────
// Both live inside domain content, so the domain that owns them has to be open
// to have anything to measure. Which domain that is comes from the deferred
// text rather than a hard-coded name — these move between waves, and a check
// that silently measures nothing is worse than one that fails.
const domainWith = async (needle) => page.evaluate(sel =>
  [...document.querySelectorAll("script.domain-src")]
    .find(s => s.textContent.includes(sel))?.dataset.domain || null, needle);
const topoDomain = await domainWith('class="topo-svg"');
const volDomain = await domainWith('class="volatile"');

const themed = async () => {
  const out = { body: null, line: null, circle: null, volatile: null };
  out.body = await page.evaluate(() => getComputedStyle(document.body).backgroundColor);
  if (topoDomain) {
    await openDomain(topoDomain);
    Object.assign(out, await page.evaluate(() => {
      const g = el => el ? getComputedStyle(el) : null;
      return {
        line: g(document.querySelector(".topo-svg line"))?.stroke,
        circle: g(document.querySelector(".topo-svg circle"))?.fill,
      };
    }));
  }
  if (volDomain) {
    await openDomain(volDomain);
    out.volatile = await page.evaluate(() => {
      const el = document.querySelector(".volatile");
      return el ? getComputedStyle(el).borderBottomColor : undefined;
    });
  }
  return out;
};
check("the themed elements are in some domain", !!topoDomain && !!volDomain,
  `topo-svg in ${topoDomain}, volatile in ${volDomain}`);
const darkT = await themed();
await page.evaluate(() => document.documentElement.setAttribute("data-theme", "light"));
await page.waitForTimeout(250);
const lightT = await themed();
// Assert presence separately from behaviour. Skipping a check when its element
// is missing is how a harness reports success on a page that lost the feature:
// renaming .topo-svg once took this file from 21 checks to 19, all passing.
for (const k of ["body", "line", "circle", "volatile"]) {
  if (darkT[k] == null) {
    check(`'${k}' element is present to theme`, false, "selector matched nothing");
    continue;
  }
  check(`'${k}' follows the theme`, darkT[k] !== lightT[k], `${darkT[k]} -> ${lightT[k]}`);
}

// ── nothing hard-coded survived into a style attribute ──────────────────────
const rawHex = await page.evaluate(() =>
  [...document.querySelectorAll("[style*='#']")]
    .filter(e => /#[0-9a-fA-F]{3,8}\b/.test(e.getAttribute("style"))).length);
check("no raw hex colour in a style attribute", rawHex === 0, `${rawHex} found`);

// ── keyboard: Enter opens a domain, then a topic ────────────────────────────
await page.goto(PAGE, { waitUntil: "load" });
await page.locator(".domain-header").first().focus();
await page.keyboard.press("Enter");
await page.waitForTimeout(300);
const kbDomain = await page.evaluate(() =>
  document.querySelector(".domain-body")?.classList.contains("open"));
check("Enter opens a domain", !!kbDomain);
await page.locator(".domain-body.open .topic-header").first().focus();
await page.keyboard.press("Enter");
await page.waitForTimeout(300);
const kbTopic = await page.evaluate(() =>
  document.querySelector(".domain-body.open .topic-header")?.getAttribute("aria-expanded"));
check("Enter opens a topic and sets aria-expanded", kbTopic === "true", `aria-expanded=${kbTopic}`);

// ── domain landing cards ────────────────────────────────────────────────────
// The card is data, not content: it must render above the topics, link only to
// topics that exist, and stay out of everything that counts .topic elements.
await page.goto(PAGE, { waitUntil: "load" });
const introPayload = await page.evaluate(() => {
  const el = document.getElementById("domain-intros");
  try { return el ? JSON.parse(el.textContent) : null; } catch { return null; }
});
const domainIds = await page.evaluate(() =>
  [...document.querySelectorAll(".domain-section")].map(s => s.dataset.domain));
check("every domain has a landing card in the payload",
  !!introPayload && domainIds.every(d => introPayload[d]),
  `${introPayload ? Object.keys(introPayload).length : 0} intros for ${domainIds.length} domains`);

const introDomain = domainIds[0];
await page.evaluate(d => openDomain(domainSection(d)), introDomain);
await page.waitForTimeout(300);
const intro = await page.evaluate(d => {
  const body = domainSection(d).querySelector(".domain-body");
  const card = body.querySelector(":scope > .domain-intro");
  if (!card) return null;
  return {
    first: body.firstElementChild === card,
    rows: [...card.querySelectorAll(".di-label")].map(l => l.textContent),
    links: [...card.querySelectorAll(".di-link")].map(b => b.textContent),
    topics: body.querySelectorAll(".topic").length,
    indexed: (topicIndex()[d] || []).length,
    introIsTopic: card.classList.contains("topic"),
  };
}, introDomain);
check("the landing card renders above the topics",
  !!intro && intro.first, intro ? `first=${intro.first}` : "no .domain-intro");
check("the landing card carries its rows",
  !!intro && intro.rows.length >= 3, intro ? intro.rows.join(",") : "");
// Names are resolved at render time, so a link that survived is a link that
// points at a topic actually in this domain. A count short of the payload's
// means a topic was renamed and the card silently lost a signpost.
const wantStarts = introPayload?.[introDomain]?.start?.length ?? 0;
check("every 'start here' name resolved to a real topic",
  !!intro && intro.links.length === wantStarts,
  `${intro ? intro.links.length : 0}/${wantStarts} resolved`);
check("the landing card is not counted as a topic",
  !!intro && !intro.introIsTopic && intro.topics === intro.indexed,
  intro ? `${intro.topics} in DOM vs ${intro.indexed} indexed` : "");

// Clicking a start link must land on that topic, open.
const startJump = await page.evaluate(async () => {
  const card = document.querySelector(".domain-body.open > .domain-intro");
  const btn = card?.querySelector(".di-link");
  if (!btn) return null;
  const want = btn.textContent;
  btn.click();
  await new Promise(r => setTimeout(r, 350));
  const t = document.getElementById(location.hash.slice(1));
  // The heading carries its inline acronym expansions; the card stores the
  // title as written. Compare like for like by dropping the expansion spans,
  // which is exactly what plainLabel() does when the card's names are matched.
  const name = t?.querySelector(".topic-name")?.cloneNode(true);
  name?.querySelectorAll(".acro-exp").forEach(e => e.remove());
  const got = (name?.textContent || "").replace(/\s+/g, " ").trim();
  return { want, got,
           open: !!t?.querySelector(".topic-body")?.classList.contains("open") };
});
check("a 'start here' link opens its topic",
  !!startJump && startJump.open && startJump.got === startJump.want,
  startJump ? `${startJump.want} -> ${startJump.got} (open=${startJump.open})` : "no link");

// The check above only exercises one domain. A rename in any of the other
// twenty-nine costs that card a signpost just as quietly, so resolve the whole
// payload the same way the renderer does.
const unresolved = await page.evaluate(() => {
  const intros = domainIntros();
  const bad = [];
  Object.keys(intros).forEach(d => {
    const names = new Set(domainTopics(d).map(t => t.name));
    (intros[d].start || []).forEach(n => { if (!names.has(n)) bad.push(`${d}: ${n}`); });
  });
  return bad;
});
check("every landing card's 'start here' names resolve, in all domains",
  unresolved.length === 0, unresolved.slice(0, 3).join(" | "));

// A search asked for topics; the front matter should get out of the way, and
// come back when the query is cleared.
await page.evaluate(() => runSearch("subnet"));
await page.waitForTimeout(300);
const introDuringSearch = await page.evaluate(() =>
  [...document.querySelectorAll(".domain-body.open > .domain-intro")]
    .every(c => getComputedStyle(c).display === "none"));
await page.evaluate(() => runSearch(""));
await page.waitForTimeout(300);
const introAfterSearch = await page.evaluate(() => {
  const c = document.querySelector(".domain-body.open > .domain-intro");
  return c ? getComputedStyle(c).display !== "none" : null;
});
check("the landing card hides while a search is filtering", introDuringSearch === true);
check("the landing card comes back when the search is cleared", introAfterSearch === true);

// ── see also ────────────────────────────────────────────────────────────────
// The strip renders on open, links only to topics that resolve, and following
// one lands on that topic — including when it lives in another domain, which is
// half of them and the case a within-domain test would never exercise.
await page.goto(PAGE, { waitUntil: "load" });
const saProbe = await page.evaluate(async () => {
  const rel = relatedTopics();
  // Pick a topic whose strip crosses a domain boundary.
  const src = Object.keys(rel).find(id =>
    topicDomain(id) && rel[id].some(t => topicDomain(t) && topicDomain(t) !== topicDomain(id)));
  if (!src) return null;
  location.hash = src;
  openHashTarget();
  await new Promise(r => setTimeout(r, 400));
  const topic = document.getElementById(src);
  const strip = topic?.querySelector(":scope > .topic-body > .see-also");
  return {
    src,
    wanted: rel[src].length,
    rendered: strip ? strip.querySelectorAll(".sa-link").length : 0,
    label: strip?.querySelector(".sa-label")?.textContent || "",
    tagged: strip ? strip.querySelectorAll(".sa-domain").length : 0,
    lastChild: strip ? topic.querySelector(":scope > .topic-body").lastElementChild === strip : false,
  };
});
check("a related topic renders its see-also strip",
  !!saProbe && saProbe.rendered === saProbe.wanted && saProbe.label === "See also",
  saProbe ? `${saProbe.rendered}/${saProbe.wanted} links on ${saProbe.src}` : "no cross-domain pair");
check("the strip sits below the last concept card",
  !!saProbe && saProbe.lastChild);
check("a link out of the domain says so",
  !!saProbe && saProbe.tagged > 0, saProbe ? `${saProbe.tagged} tagged` : "");

const saJump = await page.evaluate(async () => {
  const btn = document.querySelector(".topic-body.open .see-also .sa-link");
  if (!btn) return null;
  const want = btn.childNodes[0].textContent.trim();
  btn.click();
  await new Promise(r => setTimeout(r, 400));
  const t = document.getElementById(location.hash.slice(1));
  const name = t?.querySelector(".topic-name")?.cloneNode(true);
  name?.querySelectorAll(".acro-exp").forEach(e => e.remove());
  return { want, got: (name?.textContent || "").replace(/\s+/g, " ").trim(),
           open: !!t?.querySelector(".topic-body")?.classList.contains("open") };
});
check("following a see-also link opens that topic",
  !!saJump && saJump.open && saJump.got === saJump.want,
  saJump ? `${saJump.want} -> ${saJump.got}` : "no link");

// The strip is rendered once per topic however the topic was opened, and every
// id in the payload has to resolve — a dead id would render a link to nothing.
const saOnce = await page.evaluate(async () => {
  const id = location.hash.slice(1);
  const topic = document.getElementById(id);
  const header = topic?.querySelector(".topic-header");
  header?.click(); await new Promise(r => setTimeout(r, 150));
  header?.click(); await new Promise(r => setTimeout(r, 150));
  return topic?.querySelectorAll(".see-also").length ?? -1;
});
check("the strip is rendered once, not once per open", saOnce <= 1, `${saOnce} strips`);

const relDead = await page.evaluate(() => {
  const rel = relatedTopics();
  const bad = [];
  Object.keys(rel).forEach(src => {
    if (!topicDomain(src)) bad.push(src);
    rel[src].forEach(t => { if (!topicDomain(t)) bad.push(`${src} -> ${t}`); });
  });
  return bad;
});
check("every related id resolves to a real topic",
  relDead.length === 0, relDead.slice(0, 3).join(" | "));

// ── clickable cross-references ──────────────────────────────────────────────
// build.py resolves every <span class="xref"> title to a topic id. The span has
// to reach that topic on a click and on Enter, and every stamped id has to
// resolve — an id that does not is a link to nothing.
await page.goto(PAGE, { waitUntil: "load" });
const xrefIds = await page.evaluate(() =>
  [...document.querySelectorAll("script.domain-src")]
    .flatMap(s => [...s.textContent.matchAll(/data-xref="([^"]+)"/g)].map(m => m[1])));
check("cross-references are stamped with a topic id", xrefIds.length > 100,
  `${xrefIds.length} stamped`);
const xrefDead = await page.evaluate(ids => ids.filter(id => !topicDomain(id)), xrefIds);
check("every stamped cross-reference resolves", xrefDead.length === 0,
  xrefDead.slice(0, 3).join(" | "));

const xrefJump = await page.evaluate(async () => {
  // Open the domain that owns the first stamped cross-reference, then find it
  // in the live DOM — the spans live inside topic bodies, so the topic has to
  // be open before one is clickable.
  const src = [...document.querySelectorAll("script.domain-src")]
    .find(s => s.textContent.includes("data-xref="));
  const d = src.closest(".domain-section").dataset.domain;
  openDomain(domainSection(d));
  await new Promise(r => setTimeout(r, 200));
  document.querySelectorAll(".domain-body.open .topic-header")
    .forEach(h => { h.classList.add("open"); h.nextElementSibling.classList.add("open"); });
  const span = document.querySelector(".domain-body.open .xref[data-xref]");
  if (!span) return null;
  const want = span.dataset.xref;
  const focusable = span.getAttribute("tabindex") === "0" && span.getAttribute("role") === "link";
  span.click();
  await new Promise(r => setTimeout(r, 400));
  return { want, got: location.hash.slice(1), focusable,
           open: !!document.getElementById(want)?.querySelector(".topic-body")?.classList.contains("open") };
});
check("clicking a cross-reference opens the topic it names",
  !!xrefJump && xrefJump.got === xrefJump.want && xrefJump.open,
  xrefJump ? `${xrefJump.want} -> ${xrefJump.got} (open=${xrefJump.open})` : "none found");
check("a cross-reference is reachable by keyboard",
  !!xrefJump && xrefJump.focusable);

const xrefKey = await page.evaluate(async () => {
  const span = document.querySelector(".domain-body.open .topic-body.open .xref[data-xref]");
  if (!span) return null;
  const want = span.dataset.xref;
  // The click check above left the hash pointing at a topic. Clearing it first
  // is what makes this an assertion rather than a formality: with the hash
  // still set, a keydown handler that did nothing at all would pass.
  history.replaceState(null, "", location.pathname);
  span.focus();
  span.dispatchEvent(new KeyboardEvent("keydown",
    { key: "Enter", bubbles: true, cancelable: true }));
  await new Promise(r => setTimeout(r, 400));
  return { want, got: location.hash.slice(1) };
});
check("Enter on a focused cross-reference follows it",
  !!xrefKey && !!xrefKey.want && xrefKey.got === xrefKey.want,
  xrefKey ? `${xrefKey.want} -> ${xrefKey.got}` : "none found");

// ── study tooling: scheduler, acronym quiz, distractors, backup ─────────────
// Four features that shipped without any coverage. Each has a failure that is
// silent: a scheduler that stops writing records looks like "nothing is due",
// a quiz whose distractors come from the wrong pool looks like an easy quiz,
// and an export that drops a key looks like a smaller export.
await page.goto(PAGE, { waitUntil: "load" });

const srs = await page.evaluate(() => {
  localStorage.clear();
  const id = stIndex()[0].id;
  const first = srsGrade(id, "good");
  const second = srsGrade(id, "good");
  const third = srsGrade(id, "good");
  const badge = document.querySelector("#study-fab .study-badge")?.textContent ?? null;
  // A card graded three times is scheduled well past today, so it must not be
  // in the due count — that is the whole point of the interval.
  const dueAfter = srsDueCount();
  const failed = srsGrade(id, "again");
  return {
    id, first, second, third, badge, dueAfter,
    known: localStorage.getItem("known:" + id),
    failedInterval: failed.i, failedEase: failed.e, thirdEase: third.e,
    failedDue: failed.d, tomorrow: srsToday(1),
    dueNow: srsDueCount(),
  };
});
check("grading a card writes a scheduler record",
  !!srs && srs.first.i === 1 && typeof srs.first.d === "string" && srs.first.n === 1,
  JSON.stringify(srs?.first));
check("the interval grows across gradings",
  srs.second.i === 6 && srs.third.i > srs.second.i,
  `${srs.first.i} -> ${srs.second.i} -> ${srs.third.i} days`);
check("a graded card counts as known", srs.known === "1");
check("a scheduled card is not due today", srs.dueAfter === 0, `${srs.dueAfter} due`);
// The scheduler works in whole days, so "again" means tomorrow rather than
// later in this session — asserted as written, not as an SRS purist would want
// it. If that is ever changed, this is the check that should change with it.
check("'again' resets the interval and lowers the ease",
  srs.failedInterval === 1 && srs.failedEase < srs.thirdEase
  && srs.failedDue === srs.tomorrow && srs.dueNow === 0,
  `i=${srs.failedInterval}, ease ${srs.thirdEase} -> ${srs.failedEase}, due ${srs.failedDue}`);

const acroQ = await page.evaluate(() => {
  const qs = acroQuestions("__all", 8);
  const areas = acroAreas();
  const bad = qs.filter(q =>
    q.options.length !== 4 ||
    new Set(q.options.map(o => o.toLowerCase())).size !== 4 ||
    !q.options.includes(q.answer));
  // Same-area distractors are the claim the code makes; check it on an area
  // big enough that the fallback to the whole dictionary never kicks in.
  const big = areas.map(a => ({ a, n: acroQuestions(a, 3).length }))
    .filter(r => r.n === 3).slice(0, 3);
  return { count: qs.length, areas: areas.length, bad: bad.length, big: big.map(r => r.a) };
});
check("the acronym quiz builds questions from the dictionary",
  acroQ.count === 8 && acroQ.areas > 10, `${acroQ.count} questions, ${acroQ.areas} areas`);
check("every acronym question has four distinct options, one of them right",
  acroQ.bad === 0, `${acroQ.bad} malformed`);
check("a single subject area can fill a quiz on its own",
  acroQ.big.length === 3, acroQ.big.join(", "));

const distract = await page.evaluate(() => {
  const domain = [...document.querySelectorAll(".domain-section")]
    .map(s => s.dataset.domain).find(d => stTopicsForScope(d).length >= 8);
  if (!domain) return null;
  const stage = document.createElement("div");
  stStartQuiz(domain, stage);
  const ids = [...stage.querySelectorAll(".st-q-opt")].map(b => b.dataset.id);
  const owner = new Set(stTopicsForScope(domain).map(t => t.id));
  return { domain, options: ids.length, foreign: ids.filter(id => !owner.has(id)).length };
});
check("quiz distractors come from the scope that was chosen",
  !!distract && distract.options === 4 && distract.foreign === 0,
  distract ? `${distract.options} options, ${distract.foreign} from outside ${distract.domain}` : "no domain");

const backup = await page.evaluate(() => {
  localStorage.clear();
  const ids = stIndex().slice(0, 3).map(t => t.id);
  localStorage.setItem("reviewed:" + ids[0], "1");
  localStorage.setItem("bookmark:" + ids[1], "1");
  srsGrade(ids[2], "good");
  localStorage.setItem("unrelated-key", "should not travel");
  const payload = bkExport();
  const text = JSON.stringify(payload);
  localStorage.clear();
  const vetted = bkValidate(text);
  const { kept, skipped } = bkSanitise(vetted.data);
  bkApply(kept, "replace");
  return {
    counts: payload.counts,
    carriedUnrelated: Object.keys(payload.data).includes("unrelated-key"),
    skipped,
    restored: {
      reviewed: localStorage.getItem("reviewed:" + ids[0]),
      bookmark: localStorage.getItem("bookmark:" + ids[1]),
      srs: !!localStorage.getItem("srs:" + ids[2]),
    },
  };
});
check("an export carries the progress keys and nothing else",
  backup.counts.reviewed === 1 && backup.counts.bookmark === 1 && backup.counts.srs === 1
  && !backup.carriedUnrelated,
  JSON.stringify(backup.counts));
check("an import restores what was exported",
  backup.restored.reviewed === "1" && backup.restored.bookmark === "1" && backup.restored.srs,
  JSON.stringify(backup.restored));

const rejects = await page.evaluate(() => {
  const out = {};
  const tryIt = (name, text) => {
    try { bkValidate(text); out[name] = "accepted"; }
    catch (e) { out[name] = "rejected"; }
  };
  tryIt("garbage", "not json at all");
  tryIt("wrongFormat", JSON.stringify({ format: "something-else", version: 1, data: {} }));
  tryIt("wrongVersion", JSON.stringify({ format: "techref-progress", version: 99, data: {} }));
  // A well-formed file carrying a key we do not own, and a malformed record.
  const { kept, skipped } = bkSanitise({ "evil-key": "x", "srs:abc": { d: "not-a-date" } });
  out.sanitised = `${Object.keys(kept).length} kept, ${skipped} refused`;
  return out;
});
check("a file that is not a progress export is refused",
  rejects.garbage === "rejected" && rejects.wrongFormat === "rejected"
  && rejects.wrongVersion === "rejected", JSON.stringify(rejects));
check("an import refuses keys and shapes it does not own",
  rejects.sanitised === "0 kept, 2 refused", rejects.sanitised);

await page.evaluate(() => localStorage.clear());

// ── learning paths ──────────────────────────────────────────────────────────
// A path drops steps it cannot resolve, so a broken path renders as a *shorter*
// path. That is the failure to guard: the rendered step count has to match the
// payload, and the progress has to track the same reviewed state the ✓ sets.
await page.goto(PAGE, { waitUntil: "load" });
const pathPayload = await page.evaluate(() => {
  const el = document.getElementById("learning-paths");
  try { return el ? JSON.parse(el.textContent) : null; } catch { return null; }
});
check("learning paths are inlined", Array.isArray(pathPayload) && pathPayload.length > 0,
  `${pathPayload ? pathPayload.length : 0} paths`);

const pathResolve = await page.evaluate(() => {
  const byId = new Set(stIndex().map(t => t.id));
  const bad = [];
  learningPaths().forEach(p =>
    (p.steps || []).forEach(s => { if (!byId.has(s)) bad.push(`${p.id}: ${s}`); }));
  return { bad, total: learningPaths().reduce((n, p) => n + p.steps.length, 0) };
});
check("every step in every path resolves to a topic",
  pathResolve.bad.length === 0, pathResolve.bad.slice(0, 3).join(" | "));

const pathUI = await page.evaluate(async () => {
  localStorage.clear();
  const p = learningPaths()[0];
  // Mark the first two steps reviewed, so progress has something to report.
  localStorage.setItem("reviewed:" + p.steps[0], "1");
  localStorage.setItem("reviewed:" + p.steps[1], "1");
  stOpenPaths();
  await new Promise(r => setTimeout(r, 200));
  const card = document.querySelector(`.st-path[data-id="${p.id}"]`);
  const listCount = card?.querySelector(".st-path-count")?.textContent || "";
  card?.querySelector(".st-path-open").click();
  await new Promise(r => setTimeout(r, 200));
  const steps = [...document.querySelectorAll(".st-path-step")];
  return {
    id: p.id,
    listCount,
    rendered: steps.length,
    declared: p.steps.length,
    done: steps.filter(li => li.classList.contains("done")).length,
    hereIndex: steps.findIndex(li => li.classList.contains("here")),
    hasContinue: !!document.getElementById("st-path-next"),
  };
});
check("a path renders every step it declares",
  pathUI.rendered === pathUI.declared, `${pathUI.rendered}/${pathUI.declared}`);
check("reviewed steps count as done",
  pathUI.done === 2 && pathUI.listCount.startsWith("2/"),
  `${pathUI.done} done, list said ${pathUI.listCount}`);
check("the first unreviewed step is marked as where you are",
  pathUI.hereIndex === 2 && pathUI.hasContinue, `here at index ${pathUI.hereIndex}`);

const pathJump = await page.evaluate(async () => {
  const btn = document.getElementById("st-path-next");
  const want = learningPaths()[0].steps[2];
  btn.click();
  await new Promise(r => setTimeout(r, 400));
  return { want, got: location.hash.slice(1),
           open: !!document.getElementById(want)?.querySelector(".topic-body")?.classList.contains("open") };
});
check("Continue opens the step you are on",
  pathJump.got === pathJump.want && pathJump.open,
  `${pathJump.want} -> ${pathJump.got}`);
await page.evaluate(() => localStorage.clear());

// ── per-topic notes ─────────────────────────────────────────────────────────
// A note that saves but never reappears, or reappears but never exports, are
// both silent — the reader only finds out when the note is gone.
await page.goto(PAGE, { waitUntil: "load" });
const note = await page.evaluate(async () => {
  localStorage.clear();
  const first = [...document.querySelectorAll(".domain-section")][0].dataset.domain;
  openDomain(domainSection(first));
  await new Promise(r => setTimeout(r, 250));
  const topic = document.querySelector(".domain-body.open .topic");
  topic.querySelector(".topic-note-btn").click();
  await new Promise(r => setTimeout(r, 150));
  const input = topic.querySelector(".topic-note .tn-input");
  const opened = !!input && !input.hidden;
  input.value = "check this against the lab build";
  input.dispatchEvent(new Event("blur"));
  await new Promise(r => setTimeout(r, 100));
  return {
    id: topic.id, opened,
    stored: localStorage.getItem("note:" + topic.id),
    shown: topic.querySelector(".topic-note .tn-text")?.textContent,
    inputHidden: topic.querySelector(".topic-note .tn-input")?.hidden,
    flagged: topic.classList.contains("noted"),
    // The note must be the first thing in the body, above the concept cards.
    first: topic.querySelector(":scope > .topic-body").firstElementChild
             ?.classList.contains("topic-note"),
  };
});
check("the note button opens an editor on the topic", note.opened);
check("a note is saved, shown and flagged on the topic",
  note.stored === "check this against the lab build"
  && note.shown === note.stored && note.inputHidden && note.flagged,
  `stored=${JSON.stringify(note.stored)} flagged=${note.flagged}`);
check("the note sits above the concept cards", note.first === true);

const noteBack = await page.evaluate(async () => {
  const id = [...document.querySelectorAll(".topic")].find(t => t.classList.contains("noted"))?.id;
  // Close and reopen the domain: the note lives in storage, not in the DOM that
  // just got thrown away.
  const section = domainSection(topicDomain(id));
  closeDomain(section);
  openDomain(section);
  await new Promise(r => setTimeout(r, 250));
  document.getElementById(id).querySelector(".topic-header").click();
  await new Promise(r => setTimeout(r, 200));
  return document.getElementById(id)?.querySelector(".topic-note .tn-text")?.textContent || "";
});
check("a note survives the domain being evicted and reopened",
  noteBack === "check this against the lab build", noteBack);

const noteBackup = await page.evaluate(() => {
  const payload = bkExport();
  const noteKeys = Object.keys(payload.data).filter(k => k.startsWith("note:"));
  localStorage.clear();
  const { kept } = bkSanitise(bkValidate(JSON.stringify(payload)).data);
  bkApply(kept, "replace");
  const restored = noteKeys.map(k => localStorage.getItem(k));
  // And a note shape the page does not accept must be refused, like any other.
  const bad = bkSanitise({ "note:x": 42, "note:y": "   " });
  return { counted: payload.counts.topicNote, noteKeys: noteKeys.length,
           restored, refused: bad.skipped };
});
check("notes travel in the progress export",
  noteBackup.counted === 1 && noteBackup.noteKeys === 1,
  `counted ${noteBackup.counted}, ${noteBackup.noteKeys} keys`);
check("notes come back on import",
  noteBackup.restored[0] === "check this against the lab build", noteBackup.restored[0]);
check("a note that is not a usable string is refused on import",
  noteBackup.refused === 2, `${noteBackup.refused} refused`);

const noteGone = await page.evaluate(async () => {
  const id = [...document.querySelectorAll(".topic")].find(t => t.classList.contains("noted"))?.id;
  const topic = document.getElementById(id);
  topic.querySelector(".topic-note .tn-edit").click();
  topic.querySelector(".topic-note .tn-clear").click();
  await new Promise(r => setTimeout(r, 120));
  return { stored: localStorage.getItem("note:" + id),
           block: !!topic.querySelector(".topic-note"),
           flagged: topic.classList.contains("noted") };
});
check("deleting a note removes the block and the flag",
  noteGone.stored === null && !noteGone.block && !noteGone.flagged,
  JSON.stringify(noteGone));
await page.evaluate(() => localStorage.clear());

// ── hygiene ─────────────────────────────────────────────────────────────────
check("no console errors", consoleErrors.length === 0, consoleErrors.slice(0, 2).join(" | "));
check("no off-site requests", offsite.length === 0, offsite.slice(0, 2).join(" | "));

await browser.close();

const failed = results.filter(r => !r.pass);
console.log(`\n${results.length - failed.length}/${results.length} checks passed.`);
process.exit(failed.length ? 1 : 0);
