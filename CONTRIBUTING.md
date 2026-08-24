# Contributing — Content & Markup Conventions

All visible content lives in `data/*.html` and is assembled into `index.html` by
`build.py`. **Never hand-edit `index.html`.**

A domain is normally one file, `data/{id}.html`. A domain that has outgrown one
file is split into ordered **parts** — `data/script.01-references.html`,
`data/script.02-beginner.html`, … — which `build.py` concatenates in filename
order into the same domain. Parts exist so a large domain is workable; they are
not separate domains, and splitting one changes nothing about the built page.
A domain may have a single file *or* parts, never both; the tools error if it
has both.

## Workflow

```
make            # gen acronym domain -> annotate -> build
make check      # every static gate CI runs
make test       # drive the built page in a browser
```

Then open `index.html` and verify by hand (filter, search, expand, light/dark).

The order in `make build` is not arbitrary: the acronym domain is generated from
the dictionary, the annotator rewrites content using it, and `build.py`
assembles what both produced. Running them out of order gives you a page that
looks correct and is stale. `make help` lists everything.

## Canonical topic skeleton

Every topic is a `.topic` containing a `.topic-header` (the clickable bar) and a
`.topic-body` (revealed on expand). Use exactly this structure so styling,
filtering, search, permalinks, and progress tracking all work:

```html
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔐</span>
    <span class="topic-name">Human-Readable Topic Title</span>
    <span class="topic-badge">OPTIONAL TAG</span>
    <span class="topic-chev">▶</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">Reference</div>
      <div class="concept-title">Card Title</div>
      <div class="concept-desc">Prose explanation.</div>
      <!-- tables, code blocks, etc. -->
    </div>
  </div>
</div>
```

Notes:
- The permalink/reviewed tools and `aria`/keyboard support are added by
  `script.js` **when the topic's domain is opened** — you do not add them in
  markup.
- `.topic-name` is what the deep-link slug and search use; always include it.
- Do **not** write an `id` on a `.topic`. `build.py` stamps one, derived from
  `.topic-name`, and `data/slug-aliases.json` tracks it when a title changes.
- Never write a literal `</script` in content — not even inside `<pre>`. Domain
  content ships inside a `<script type="text/html">` block (see below), and that
  sequence would end it early. Write `&lt;/script&gt;`; the build fails on a raw
  one rather than shipping a truncated page.

## One domain at a time

`build.py` puts each domain's content in an inert `<script type="text/html">`
block next to its header instead of in the page body. `script.js` moves one
domain's block into the DOM when it is opened and empties it again when another
opens, so the browser only ever builds the domain being read — 404 elements at
load rather than 92,330.

This costs nothing in content conventions, and one thing in code conventions:

> **Never answer a page-wide question with `document.querySelectorAll(".topic")`.**
> It sees one domain and returns a confident, wrong answer.

Two accessors exist instead, both in `script.js`:

| You need | Use | Where it comes from |
|---|---|---|
| Which topics exist, and where | `topicIndex()` / `topicDomain(id)` | the id map `build.py` inlines |
| What a topic says (name, card text, full text) | `domainTopics(domainId)` | the deferred block, parsed once and cached |

Search, the flashcard and quiz decks, quick jump, the study list, the progress
badges and the random pick all go through those, which is why they still cover
all 29 domains while one is rendered. `tools/smoke_test.mjs` checks exactly that:
if it starts failing "search still reaches unopened domains", something started
reading the DOM again.

## Class conventions (use these, not one-off variants)

| Purpose            | Use                     | Do **not** use                          |
|--------------------|-------------------------|-----------------------------------------|
| Topic chevron      | `topic-chev`            | ~~`topic-chevron`~~                      |
| Reference table    | `ref-table`             | prefer over `ai-table` for new content  |
| Verdict after a table | `concept-desc verdict` | ~~`style="margin-top:10px"`~~          |
| Colored text       | see below — it depends  | ~~a hex literal, anywhere~~             |

### The verdict sentence

Almost every table here is followed by one paragraph saying what the table means — the
house rule that *every table gets a verdict*. It is spaced away from the table by 10px,
and that spacing has a class:

```html
<table class="ref-table"> … </table>
<div class="concept-desc verdict">The sentence that says what the table means.</div>
```

Do not write the margin inline. 1,142 cards did, long after the class existed, and
`lint_content.py` now fails the build on it with the line number. There is no matching
class for the *first* description inside a `.dw` — it needs no margin, and the 67 cards
that set `margin-top:0` there were overriding nothing.

`.ai-table` is not deprecated, whatever "prefer" suggests above. It is a genuinely
different design — larger text, an amber first column — used in 360 tables across 18
domains, and the linter reports it as a census line rather than a warning. Use
`ref-table` for new content because it is the house style; do not convert existing
tables, because that is a redesign.

### Colours

**Never write a hex literal in content.** `lint_content.py` fails the build on one in a
`style` attribute or an SVG paint attribute. Hard-coded colours keep their dark-mode
value in light mode, which is how a `#fff` label ended up invisible on a white card.

Reach for a colour one of two ways:

`c-cyan` · `c-green` · `c-amber` · `c-red` · `c-purple` · `c-muted`

These track the theme and work everywhere **except the first cell of a `.ref-table`
row**, where `.ref-table td:first-child` sets the colour at a higher specificity and
wins. That column is already styled bold-and-prominent by design, so it does not need a
class — and the linter now fails the build on one, because 1614 of them had accumulated
without ever rendering.

`style="color: var(--…)"` for any accent that has no utility class. The full palette is
in `:root` in `style.css`: `--cyan` `--green` `--amber` `--red` `--purple` `--muted`
`--text` `--sky` `--orange` `--pink` `--yellow` `--emerald` `--indigo` `--violet`
`--rose` `--fuchsia` `--lime`, plus dimmed `--amber-2/-3`, `--green-2/-3` and `--cyan-2`
for three-tone ladders. Add a variable there rather than a literal here.

## Before you push

`make build` regenerates `index.html`; CI fails if you forgot. Then:

```
make check                     # every static gate, fastest-failing first
make test                      # drives the built page in a real browser
```

It checks the things a structural change quietly breaks — a chip without its
domain section, a permalink that no longer expands its card, a study deck that
lost its domain, progress that stops persisting, a diagram that stopped
following the theme. Needs `npm install playwright` once. CI runs it too, as a
separate job so a markup typo still fails in seconds.

If you add a feature worth protecting, add a check. One rule, learned the hard
way: **assert the element is there before asserting how it behaves.** A check
that quietly disappears along with its selector turns a broken page into a
passing run.

## Pointing at another card

Quote the target's **exact title** in an `xref` span:

```html
<span class="xref">Kerberos Authentication Flow</span> in the Security domain
explains the ticket exchange.
```

`lint_content.py` fails the build if the title matches no card, and suggests the
nearest one when it can. Four references were already dangling when the check was
added — two naming cards that had been retitled, one naming a card that never
existed, and one that a passing acronym annotation had quietly rewritten.

Do not write the reference as plain prose or as `<em>`; nothing can check those. The
annotator skips `.xref`, so the quoted title stays byte-identical to the card it names.

## Claims that go out of date

Most of this site is conceptual and does not rot — how BGP works, what Zero Trust means,
a keyboard shortcut. A few things do: a console path, a street price, a service limit, a
version number. Mark those **at the claim**, not on the card:

```html
Used enterprise mini PC (<span class="volatile" data-checked="2026-08">~$80-150</span>)
```

`data-checked` is the month the claim was last *verified*, which is deliberately not the
card's `data-reviewed` — rewording a paragraph is not the same act as confirming a price
is still right. The reader gets a dotted underline and the date on hover; in print it
appears inline.

`python tools/stamp_freshness.py --report` then lists claims oldest-first, by claim
rather than by topic. `--candidates` runs a keyword guess to help you find things worth
marking — treat it as a prompt to read the card, never as a finding: it flags one topic
in five, including keyboard-shortcut cards, because a word like "console" in prose tells
you nothing.

Do not mark something that is not going to move. `$0` stays free.

### Fact anchors — where a number came from

A volatile span says *when* a claim was checked. A **fact anchor** says *where it came
from*, so the next person can re-verify it in a minute instead of re-researching it in an
hour. It is an HTML comment immediately before the element making the claim, so it costs
the reader nothing:

```html
<!-- fact: tombstone lifetime 180 days | source: Active Directory forest functional
     level defaults since Server 2003 SP1 | checked: 2026-08 -->
Deletions replicate as tombstones — markers that persist for 180 days …
```

Three fields, pipe-separated: the claim in a few words, the source, and the month you
checked it. Worth adding for a **version-specific number a reader could act on** — a
retention window, a service limit, an evaluation period, a default that a vendor could
change. Not worth adding for arithmetic, for something the card derives itself, or for a
figure whose source is the card's own worked example.

`python tools/check_volatility.py` validates both conventions — a malformed or future
`data-checked`, an anchor missing a field — and lists them oldest first so a freshness
pass has somewhere to start. It also reports topics that name a vendor console and carry
no dated span; that half is a queue to read, never a gate, because plenty of cards
mention a console without making a claim about one.

For repeated SVG diagram colours, style the shapes from a class on the `<svg>` instead —
`.topo-svg line { stroke: var(--sky); }` and `math.html`'s `msv-*` set are the pattern.

## Code blocks

Wrap literal code in `<pre class="code-block">…</pre>`. The build's minifier
preserves whitespace **only** inside `<pre>`, so never rely on indentation being
significant anywhere else.

## Acronyms

Never write an `<span class="acro-exp">…</span>` by hand — that class is owned by
`tools/annotate_acronyms.py`, which strips and re-adds every one of them on each
run. Just write the acronym normally; the tool annotates its first use in each
topic from `data/acronyms.json`.

If an acronym is missing an expansion, add it to `data/acronyms.json` and
re-run both tools:

```sh
python3 tools/gen_acronym_domain.py && python3 tools/annotate_acronyms.py && python3 build.py
```

Two things the tool will not touch, by design: anything inside `<pre>`, `<code>`
or `<kbd>`, and badges/chips/icons. So an acronym that only appears in a command
example never gets expanded inline — mention it in prose if it needs explaining.

## Freshness stamps

Every `.topic` carries `data-reviewed="YYYY-MM"`, written by
`tools/stamp_freshness.py` from git history. Never edit it by hand — run the
script, or let CI tell you it is stale.

**The convention it depends on: run mechanical passes as their own commit.**
The stamper works out which commits were purely mechanical by normalising the
annotator's `.acro-exp` spans and its own `data-reviewed` attributes away and
comparing against the parent. A commit that does that *and* adds real content
cannot be classified, so the annotated lines will read as freshly reviewed when
they were not. Keeping `python3 tools/annotate_acronyms.py` in a separate commit
from the content it annotates keeps the dates honest.

A topic that tracks something changeable — a vendor console, a price, a product
name — should also carry `data-volatile="true"`. Only volatile topics appear in
`--report`; stable ones (the OSI model, the TCP handshake) are excluded on
purpose, so the report stays a to-do list rather than a source of guilt.

## Topic IDs are a contract

A topic's id is `slugify(its title)`, stamped by `build.py` in document order,
with duplicates suffixed `-2`, `-3` in the order they are encountered **across
the whole site**. That id is not an implementation detail. It is:

* the permalink someone shared — `index.html#osi-model-7-layers`
* the key their progress is stored under — `reviewed:`, `bookmark:`, `known:`,
  `srs:`, `note:`
* the key `related.json` and `paths.json` point at

So a change that moves ids is a change that silently breaks other people's
saved state. What moves them:

| Change | Moves ids? |
|---|---|
| Editing a card's body | No |
| Renaming a topic | **Yes** — that topic's id, and `fix_topic_names.py` records an alias |
| Reordering topics within a domain | Only if two titles collide and swap suffixes |
| Moving cards between **parts of the same domain**, in order | No |
| Moving cards to a **different domain** | Possibly — dedup order changes site-wide |
| Adding a topic whose title duplicates an existing one | **Yes** — it takes `-2`, and anything already suffixed shifts |

Two rules follow. **Prefer parts over new domains** when a file gets too big —
that is why `script` is six parts rather than three domains. And when you do
rename, let `tools/fix_topic_names.py` write the alias so the old permalink
still lands; never hand-edit `data/slug-aliases.json`.

If you are refactoring and believe the page should be unchanged, prove it:
build before and after and compare `index.html` byte for byte. That is how the
`script` split was verified.

## Adding a domain

Add an entry to `data/domains.json` (`id`, `colorClass`, `icon`, `title`,
`certTags`, `sub`) and create a matching `data/{id}.html` with the topics.
