#!/usr/bin/env python3
"""
build.py — Assembles index.html from source files.

Source files:
  index-shell.html      Page skeleton (header, filter bar, container placeholder)
  data/domains.json     Domain metadata array
  data/{id}.html        Inner content of each domain's .domain-body

Output:
  index.html            Self-contained page (works with file://, no server needed)

Every domain header is in the markup; no domain's *content* is. Each body ships
inside an inert `<script type="text/html">` block, which the HTML parser keeps as
one text node and never builds elements, styles or layout for. script.js moves
one domain's block into its `.domain-body` when it opens and empties it again
when another opens, so the live document holds the shell plus at most one
domain — 92,330 elements at load became 484.

Two things make that safe rather than merely smaller. Topic ids are stamped here
instead of derived in the browser, so a permalink resolves to a domain before
that domain exists in the DOM; and the id map is inlined next to the acronym
payload, so progress badges, the random-topic pick and hash routing all work
without parsing a single deferred block.

Usage:
  python3 build.py
"""

import hashlib
import json
import html as html_lib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data"

# The slug rule lives in tools/lint_content.py, itself a port of script.js.
# Reusing it here is what lets build.py stamp the ids the page used to derive at
# runtime — see assign_topic_ids.
sys.path.insert(0, str(ROOT / "tools"))
from lint_content import (ACRO_SPAN_RE, XREF_RE, domain_files, domain_of,  # noqa: E402
                          slugify, topic_label)

# Set to False (or pass --no-minify) to keep the built HTML pretty-printed.
MINIFY = "--no-minify" not in sys.argv

_PRE_RE = re.compile(r"<pre\b.*?</pre>", re.DOTALL | re.IGNORECASE)


def minify_html(source):
    """Strip leading indentation and blank lines from the built HTML.

    Whitespace between a newline and a tag collapses to nothing meaningful in
    HTML rendering, so removing it is safe and shaves ~19% off the output.
    <pre> blocks are protected verbatim because their whitespace is literal.
    """
    pres = []

    def _stash(m):
        pres.append(m.group(0))
        return f"\x00PRE{len(pres) - 1}\x00"

    protected = _PRE_RE.sub(_stash, source)
    lines = (ln.rstrip() for ln in protected.split("\n"))
    minified = "\n".join(ln.lstrip() for ln in lines if ln.strip())

    for i, block in enumerate(pres):
        minified = minified.replace(f"\x00PRE{i}\x00", block)
    return minified


# Words a person reads per minute of technical prose. Deliberately conservative:
# these cards are dense, and an overstated "5 min" that takes fifteen is worse
# than no estimate. Round to a multiple of 5 above 20 minutes, because the
# precision is not real and printing "47 min" implies it is.
WPM = 180

_TAG_RE = re.compile(r"<[^>]+>")
_ACRO_RE = re.compile(r'<span class="acro-exp">\([^<]*?\)</span\s*>')
_PRE_BLOCK_RE = re.compile(r"<pre\b.*?</pre\s*>", re.S)
_TABLE_RE = re.compile(r"<table\b.*?</table\s*>", re.S)


def domain_stats(body_content):
    """(topic count, reading-time label) for one domain's body.

    Three kinds of text, three speeds, because this site is unusually
    table-dense and counting everything at prose speed gets it wrong in the
    direction that matters. A reference table is read slower per word than
    prose — you scan rows and compare cells — so it is weighted up. A shell
    transcript is skimmed, so it is weighted down.

    Measured spread across the 29 domains after weighting: 6 minutes for
    `lifestyle` to 4h 45m for `script`, which matches how long those actually
    take to work through.
    """
    topics = body_content.count('<div class="topic"')

    code_words = sum(len(_TAG_RE.sub(" ", m).split())
                     for m in _PRE_BLOCK_RE.findall(body_content))
    rest = _PRE_BLOCK_RE.sub(" ", body_content)

    table_words = sum(len(_TAG_RE.sub(" ", m).split())
                      for m in _TABLE_RE.findall(rest))
    prose = _TAG_RE.sub(" ", _ACRO_RE.sub("", _TABLE_RE.sub(" ", rest)))

    words = len(prose.split()) + int(table_words * 1.4) + code_words // 3

    mins = max(1, round(words / WPM))
    if mins > 20:
        mins = 5 * round(mins / 5)
    label = f"{mins} min" if mins < 60 else f"{mins // 60}h {mins % 60:02d}m"
    return topics, label


# ── TOPIC IDS ───────────────────────────────────────────────────────────────
# script.js used to walk every .topic at load and derive its id from the title.
# That pass cannot run against content the page has not built yet, and a
# permalink has to resolve *before* its domain is in the DOM, so the ids are
# stamped here instead. The rule and the ordering are lint_content's, which is
# the same rule fix_topic_names.py numbers the slug alias map with — verified
# identical to the browser's output across all 1,080 topics.
TOPIC_OPEN = '<div class="topic"'
_TOPIC_OPEN_RE = re.compile(re.escape(TOPIC_OPEN))


def assign_topic_ids(body, used):
    """Stamp `id="slug"` on every topic in one domain body.

    `used` carries across domains because the de-duplication does: the browser
    numbered a repeated title `-2` in document order over the whole page, and a
    map keyed to per-file numbering would rename cards that never moved.
    """
    starts = [m.start() for m in _TOPIC_OPEN_RE.finditer(body)]
    out, ids, prev = [], [], 0
    for n, start in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(body)
        label, _ = topic_label(body[start:end])
        if not label:
            raise SystemExit(
                f"error: a topic has no title text to slug from, near char {start}. "
                "Every .topic needs a <span class=\"topic-name\"> — run "
                "python tools/lint_content.py.")
        base = slugify(label)
        slug, i = base, 2
        while slug in used:
            slug = f"{base}-{i}"
            i += 1
        used.add(slug)
        ids.append(slug)
        cut = start + len(TOPIC_OPEN)
        out.append(body[prev:cut])
        out.append(f' id="{slug}"')
        prev = cut
    out.append(body[prev:])
    return "".join(out), ids


CHARS_PER_MINUTE = 1000        # ~200 words a minute at ~5 characters a word
_CHEV_RE = re.compile(r'(\s*)<span class="topic-chev">')


def stamp_reading_time(body):
    """Stamp `data-read` on every topic and render it beside the badge.

    plan.md Phase 10 T6. Cards on this site run from 900 to 15,000 characters
    with no outward sign of which is which, so a reader deciding whether to
    open one is guessing. Derived at build time from the plain-text length,
    because the length is already known here and nothing about it needs to be
    computed in the browser.

    **The caveat the plan asked for, kept next to the code:** this is a proxy
    for *length*, not for *difficulty*. A dense 2,000-character card marked
    "2 min" is a small lie, and the honest defence is that the alternative —
    no signal at all — is a larger one. T7's `data-level` is the axis that
    would carry difficulty; this is not it.
    """
    starts = [m.start() for m in _TOPIC_OPEN_RE.finditer(body)]
    out, prev, stamped = [], 0, 0
    for n, start in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(body)
        block = body[start:end]
        minutes = max(1, round(len(_TAG_RE.sub("", block)) / CHARS_PER_MINUTE))
        # At the *end* of the open tag, not straight after `class="topic"`.
        # The first version inserted here and pushed `id` rightwards, which
        # silently broke orphan_report.py's `<div class="topic" id="..."`
        # regex — it reported "0 of 0 topics" and read like a clean result.
        cut = start + block.index(">") + 1
        chev = _CHEV_RE.search(block)
        out.append(body[prev:cut - 1])
        out.append(f' data-read="{minutes}"')
        out.append(">")
        if chev:
            # Before the chevron, after the badge: the chevron is the affordance
            # and stays rightmost.
            at = start + chev.start()
            out.append(body[cut:at])
            out.append(f'{chev.group(1)}<span class="topic-read" '
                       f'title="Rough reading time, estimated from length">'
                       f'{minutes} min</span>')
            prev = start + chev.start()
            stamped += 1
        else:
            prev = cut
    out.append(body[prev:])
    return "".join(out), stamped


_BADGE_RE = re.compile(r'<span class="topic-badge">(.*?)</span>', re.S)
_BEGINNER_RE = re.compile(r"\bbeginner\b", re.I)
_ADVANCED_RE = re.compile(r"\b(advanced|expert|deep)\b", re.I)


def stamp_level(body):
    """Stamp `data-level` on every topic, read from its badge.

    plan.md Phase 10 T7. The site teaches at two levels and the only outward
    sign is a badge that sometimes reads *Beginner*, so the beginner layer is
    discoverable by accident rather than filterable.

    **The rule is deliberately mechanical and it does not guess.** A badge that
    says Beginner means beginner; one that says Advanced, Expert or Deep means
    advanced; everything else is `core`, which is a statement that the card is
    *not marked* as either — not a claim that it sits in the middle. T7 as
    written suggested stamping the rest "by hand", and hand-labelling 1,300
    cards' difficulty in one pass would produce a confident number nobody had
    actually assessed. Three honest values beat three invented ones.
    """
    starts = [m.start() for m in _TOPIC_OPEN_RE.finditer(body)]
    out, prev = [], 0
    counts = {"beginner": 0, "advanced": 0, "core": 0}
    for n, start in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(body)
        badge = _BADGE_RE.search(body[start:end])
        text = _TAG_RE.sub("", badge.group(1)) if badge else ""
        if _BEGINNER_RE.search(text):
            level = "beginner"
        elif _ADVANCED_RE.search(text):
            level = "advanced"
        else:
            level = "core"
        counts[level] += 1
        cut = start + body[start:end].index(">") + 1     # end of the open tag
        out.append(body[prev:cut - 1])
        out.append(f' data-level="{level}">')
        prev = cut
    out.append(body[prev:])
    return "".join(out), counts


def topic_titles(body, ids):
    """The title of each topic in one body, paired with the id just stamped."""
    starts = [m.start() for m in _TOPIC_OPEN_RE.finditer(body)]
    out = {}
    for n, start in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(body)
        label, _ = topic_label(body[start:end])
        # First writer wins, matching how the linter resolves a duplicated
        # title: the id map is only ambiguous for titles that are ambiguous.
        out.setdefault(label, ids[n])
    return out


def link_xrefs(body, by_title):
    """Stamp `data-xref="id"` on every cross-reference whose title resolves.

    `<span class="xref">Exact Topic Title</span>` was inert markup: the linter
    proved the title existed, but a reader still had to go and find the card by
    hand. Resolving the id here rather than in the browser is the same reasoning
    as topic ids themselves — the target is almost never in the DOM, because
    only one domain's content ever is.

    The span's inner HTML is left exactly as written. The annotator injects
    acronym expansions inside it, so the title is matched the way the linter
    matches it — expansions stripped — while what renders keeps them.
    """
    linked = [0]

    def _stamp(m):
        title = html_lib.unescape(re.sub(r"<[^>]+>", "", ACRO_SPAN_RE.sub("", m.group(1))))
        title = re.sub(r"\s+", " ", title).strip()
        slug = by_title.get(title)
        if not slug:
            return m.group(0)
        linked[0] += 1
        # Focusable and announced as a link: it behaves like one, and a
        # cross-reference a keyboard reader cannot reach is not a link.
        return (f'<span class="xref" data-xref="{slug}" role="link" tabindex="0">'
                f'{m.group(1)}</span>')

    return XREF_RE.sub(_stamp, body), linked[0]


_REVIEWED_RE = re.compile(r'data-reviewed="(\d{4}-\d{2})"')


def recent_topics(body, ids, limit=3):
    """The most recently reviewed topics in one domain, newest first.

    Read from the `data-reviewed` stamps rather than from git, so the build
    stays offline and deterministic and the answer matches what
    stamp_freshness.py put in the file. Ties keep document order, which is a
    stable and meaningful fallback: the stamps are month-granular, so ties are
    the normal case rather than the exception.
    """
    starts = [m.start() for m in _TOPIC_OPEN_RE.finditer(body)]
    rows = []
    for n, start in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(body)
        m = _REVIEWED_RE.search(body[start:end])
        if m and n < len(ids):
            rows.append((m.group(1), n, ids[n]))
    if not rows:
        return None
    rows.sort(key=lambda r: (r[0], -r[1]), reverse=True)
    return {"month": rows[0][0], "topics": [r[2] for r in rows[:limit]]}


def build_cert_tags(cert_tags):
    parts = []
    for tag in cert_tags:
        parts.append(f'<span class="ctag {tag["cls"]}">{tag["text"]}</span>')
    return "\n            ".join(parts)


def build_domain_section(domain, body_content):
    """One domain: its header, an empty body, and its content held in reserve.

    The body starts empty and script.js fills it from the sibling
    `<script type="text/html">` on open. That block is why the page can carry 29
    domains and render one: the parser reads it as a single text node, so none of
    it becomes elements, styles or layout until it is asked for.

    Nothing in the content needs escaping for that to hold. The only sequence
    that can end a script block is a literal `</script`, and topic markup writes
    every code sample's tags as entities (`&lt;script&gt;`) — checked below, so a
    future card that pastes one raw fails the build instead of truncating the
    page at that point.
    """
    if "</script" in body_content.lower():
        raise SystemExit(
            f"error: data/{domain['id']}.html contains a literal '</script' — it would "
            "end the deferred content block early and truncate the page. Write it as "
            "&lt;/script&gt;.")
    cert_tags_html = build_cert_tags(domain["certTags"])
    sub = domain["sub"]
    topics, read_time = domain_stats(body_content)
    return f"""\
      <div class="domain-section {domain['colorClass']}" data-domain="{domain['id']}">
        <div class="domain-header">
          <span class="domain-icon">{domain['icon']}</span>
          <span class="domain-title">{domain['title']}</span>
          <div class="cert-tags">
            {cert_tags_html}
          </div>
          <span class="domain-sub">{sub}</span>
          <span class="domain-meta" aria-label="{topics} topics, about {read_time} to read"
            >{topics} topics · ~{read_time}</span>
          <span class="chevron">▾</span>
        </div>
        <div class="domain-body"></div>
        <script type="text/html" class="domain-src" data-domain="{domain['id']}">
{body_content}
        </script>
      </div>"""


def build_acronym_payload():
    """The dictionary, compacted for the quiz and the acronym-aware search.

    Only what those two need — acronym, its expansions, and its subject area.
    Notes and per-domain overrides are dropped, which halves the payload
    against shipping acronyms.json verbatim.
    """
    path = DATA / "acronyms.json"
    if not path.exists():
        return "[]"
    entries = json.loads(path.read_text(encoding="utf-8"))["entries"]
    compact = [[e["a"], [m["e"] for m in e["m"]], e["m"][0]["c"]] for e in entries]
    payload = json.dumps(compact, separators=(",", ":"), ensure_ascii=False)
    # A JSON block ends at the first "</script>" the parser sees, wherever it is.
    print(f"  + acronym payload ({len(payload):,} chars, {len(entries)} entries)")
    return payload.replace("</", "<\\/")


def build_slug_aliases():
    """Old topic slug -> current one, so a shared permalink never rots.

    Written by tools/fix_topic_names.py whenever a rename moves a slug. The page
    uses it to redirect a stale hash and to migrate the progress stored under
    the old id.
    """
    path = DATA / "slug-aliases.json"
    if not path.exists():
        return "{}"
    aliases = json.loads(path.read_text(encoding="utf-8"))
    payload = json.dumps(aliases, separators=(",", ":"), ensure_ascii=False)
    print(f"  + slug aliases ({len(payload):,} chars, {len(aliases)} entries)")
    return payload.replace("</", "<\\/")


def build_topic_index(index):
    """domain id -> its topic ids, in page order.

    Small enough to inline (45 KB against a 4 MB page) and it is what
    replaces the load-time DOM walk: the progress badge on every collapsed
    domain, the random-topic pick and `#slug` routing all read this instead of
    content they would otherwise have to build first.
    """
    payload = json.dumps(index, separators=(",", ":"), ensure_ascii=False)
    total = sum(len(v) for v in index.values())
    print(f"  + topic index ({len(payload):,} chars, {total} topics)")
    return payload.replace("</", "<\\/")


def build_changelog(changelog):
    """domain id -> {month, topics}: what was reviewed here most recently.

    Rendered on the domain's landing card. It answers the question a reference
    site cannot otherwise answer — "is anyone still maintaining this?" — from
    data the freshness stamps already carry.
    """
    payload = json.dumps(changelog, separators=(",", ":"), ensure_ascii=False)
    print(f"  + changelog ({len(payload):,} chars, {len(changelog)} domains)")
    return payload.replace("</", "<\\/")


def build_domain_intros():
    """domain id -> its landing card, inlined from data/domain-intros.json.

    Rendered by script.js when a domain hydrates, above its topics. It is
    deliberately not a `.topic` in the content files: the intro would then be
    counted by the topic index, dated by stamp_freshness.py, checked by
    lint_content.py and offered by the decks and the random pick, none of which
    should be true of a signpost. Keeping it as data leaves the whole content
    pipeline untouched.

    `start` holds topic *names*; script.js resolves them against the topic index
    and drops any that no longer exist, so a rename degrades to a shorter list
    rather than a dead link.
    """
    path = DATA / "domain-intros.json"
    if not path.exists():
        return "{}"
    intros = json.loads(path.read_text(encoding="utf-8"))
    payload = json.dumps(intros, separators=(",", ":"), ensure_ascii=False)
    print(f"  + domain intros ({len(payload):,} chars, {len(intros)} domains)")
    return payload.replace("</", "<\\/")


def build_related():
    """topic id -> the ids worth reading next, inlined from data/related.json.

    Keyed on ids rather than titles because ids are stamped here and covered by
    the slug alias file, so a rename carries the relation with it. The page
    drops any id it cannot resolve, which is what keeps a deleted topic from
    leaving dead strips behind on everything that pointed at it.
    """
    path = DATA / "related.json"
    if not path.exists():
        return "{}"
    related = json.loads(path.read_text(encoding="utf-8"))
    payload = json.dumps(related, separators=(",", ":"), ensure_ascii=False)
    total = sum(len(v) for v in related.values())
    print(f"  + related topics ({len(payload):,} chars, {total} links on {len(related)} topics)")
    return payload.replace("</", "<\\/")


def build_paths():
    """Ordered reading routes over existing topics, from data/paths.json.

    Pure data: a path is a list of topic ids the page renders as a checklist
    against the progress already in localStorage. Nothing here is content, which
    is why a path costs a few hundred bytes and no maintenance beyond the ids
    staying valid — checked by tools/check_paths.py.
    """
    path = DATA / "paths.json"
    if not path.exists():
        return "[]"
    paths = json.loads(path.read_text(encoding="utf-8"))
    payload = json.dumps(paths, separators=(",", ":"), ensure_ascii=False)
    steps = sum(len(p.get("steps") or []) for p in paths)
    print(f"  + learning paths ({len(payload):,} chars, {len(paths)} paths, {steps} steps)")
    return payload.replace("</", "<\\/")


_SW_VERSION_RE = re.compile(r'(const CACHE_VERSION = ")[^"]*(";)')


def stamp_sw_version(page_bytes):
    """Derive the service worker's cache version from what it precaches.

    A hand-bumped version number has two failure modes and both have bitten
    real sites: forgetting to bump it, so returning visitors keep a stale page
    forever; and bumping it on every deploy, so an unchanged build throws away
    a perfectly good cache. Hashing the assets removes both — the version
    changes exactly when the bytes do.

    Only the three files that actually change are hashed. The fonts and icons
    are in PRECACHE too and have not changed in the life of this project;
    including them would mean reading them on every build for no signal.
    """
    sw = ROOT / "sw.js"
    if not sw.exists():
        return None
    digest = hashlib.sha256(page_bytes)
    for name in ("style.css", "script.js"):
        path = ROOT / name
        if path.exists():
            digest.update(path.read_bytes())
    version = f"techref-{digest.hexdigest()[:12]}"
    text = sw.read_text(encoding="utf-8")
    updated, n = _SW_VERSION_RE.subn(lambda m: f"{m.group(1)}{version}{m.group(2)}", text)
    if not n:
        raise SystemExit("error: sw.js has no CACHE_VERSION line to stamp.")
    if updated != text:
        sw.write_text(updated, encoding="utf-8")
        print(f"  + sw.js cache version -> {version}")
    return version


def main():
    shell_path = ROOT / "index-shell.html"
    domains_path = DATA / "domains.json"

    if not shell_path.exists():
        print("ERROR: index-shell.html not found.", file=sys.stderr)
        sys.exit(1)
    if not domains_path.exists():
        print("ERROR: data/domains.json not found.", file=sys.stderr)
        sys.exit(1)

    shell = shell_path.read_text(encoding="utf-8")
    domains = json.loads(domains_path.read_text(encoding="utf-8"))

    # Two passes. Ids are stamped for every domain first, because a
    # cross-reference resolves against the whole site: the card it names is
    # usually in another domain, whose ids do not exist yet during the first
    # domain's turn.
    bodies = []
    used_slugs = set()
    topic_index = {}
    by_title = {}
    level_counts = {}
    changelog = {}
    for domain in domains:
        # One file, or an ordered set of parts concatenated in filename order.
        # Parts build into the same domain, so the topic order — and therefore
        # every slug — is exactly what a single file would have produced.
        paths = domain_files(domain["id"])
        if not paths:
            print(f"WARNING: no source for {domain['id']} — skipping.")
            continue
        chunks = []
        for part in paths:
            text = part.read_text(encoding="utf-8")
            # Joined with nothing, so a part is an exact slice of what a single
            # file held. A part that does not end in a newline would glue its
            # last line to the next part's first, which is the one way this can
            # silently corrupt a card.
            if not text.endswith("\n") and part is not paths[-1]:
                raise SystemExit(f"error: {part.name} does not end with a newline.")
            chunks.append(text)
        body = "".join(chunks)
        body, ids = assign_topic_ids(body, used_slugs)
        body, _read = stamp_reading_time(body)
        body, lv = stamp_level(body)
        for k, v in lv.items():
            level_counts[k] = level_counts.get(k, 0) + v
        topic_index[domain["id"]] = ids
        by_title.update(topic_titles(body, ids))
        recent = recent_topics(body, ids)
        if recent:
            changelog[domain["id"]] = recent
        bodies.append((domain, body, ids))
        if len(paths) > 1:
            print(f"    ({len(paths)} parts: {', '.join(p.name for p in paths)})")

    sections = []
    xref_total = 0
    for domain, body, ids in bodies:
        body, linked = link_xrefs(body, by_title)
        xref_total += linked
        sections.append(build_domain_section(domain, body))
        print(f"  + {domain['id']} ({len(body):,} chars, {len(ids)} topics)")
    print(f"  + {xref_total} cross-references linked")
    print("  + levels: " + ", ".join(f"{k} {v}" for k, v in
                                     sorted(level_counts.items(), key=lambda r: -r[1])))

    domains_html = "\n\n".join(sections)
    output = shell.replace("<!-- DOMAINS_CONTENT -->", domains_html)
    output = output.replace("<!-- ACRONYM_DATA -->", build_acronym_payload())
    output = output.replace("<!-- SLUG_ALIASES -->", build_slug_aliases())
    output = output.replace("<!-- TOPIC_INDEX -->", build_topic_index(topic_index))
    output = output.replace("<!-- DOMAIN_INTROS -->", build_domain_intros())
    output = output.replace("<!-- RELATED_TOPICS -->", build_related())
    output = output.replace("<!-- LEARNING_PATHS -->", build_paths())
    output = output.replace("<!-- CHANGELOG -->", build_changelog(changelog))

    # The link-preview text quotes the site's size. Substituting it here is the
    # difference between a number that is right and a number that was right
    # once: every content wave used to need someone to remember to edit it, and
    # the check that caught the drift only caught it after the fact.
    total_topics = sum(len(v) for v in topic_index.values())
    output = output.replace("<!-- TOPIC_COUNT -->", f"{total_topics:,}")
    output = output.replace("<!-- DOMAIN_COUNT -->", str(len(topic_index)))

    if MINIFY:
        raw_len = len(output)
        output = minify_html(output)
        saved = raw_len - len(output)
        print(f"\n  minified: {raw_len:,} -> {len(output):,} chars (-{saved / raw_len * 100:.0f}%)")

    out_path = ROOT / "index.html"
    out_path.write_text(output, encoding="utf-8")
    stamp_sw_version(output.encode("utf-8"))
    print(f"Built {out_path} ({len(output):,} chars, {len(output.encode()):,} bytes)")


if __name__ == "__main__":
    main()
