# Contributing — Content & Markup Conventions

All visible content lives in `data/*.html` (one file per domain) and is assembled
into `index.html` by `build.py`. **Never hand-edit `index.html`.**

## Workflow

1. Edit the relevant `data/{domain}.html`.
2. Run `python3 tools/annotate_acronyms.py` (adds inline acronym expansions).
3. Run `python3 build.py`.
4. Open `index.html` and verify (filter, search, expand, light/dark).

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
  `script.js` at load — you do **not** add them in markup.
- `.topic-name` is what the deep-link slug and search use; always include it.

## Class conventions (use these, not one-off variants)

| Purpose            | Use                     | Do **not** use                          |
|--------------------|-------------------------|-----------------------------------------|
| Topic chevron      | `topic-chev`            | ~~`topic-chevron`~~                      |
| Reference table    | `ref-table`             | prefer over `ai-table` for new content  |
| Colored text       | see below — it depends  | ~~a hex literal, anywhere~~             |

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

`python build.py` regenerates `index.html`; CI fails if you forgot. Then:

```
node tools/smoke_test.mjs      # drives the built page in a real browser
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

## Adding a domain

Add an entry to `data/domains.json` (`id`, `colorClass`, `icon`, `title`,
`certTags`, `sub`) and create a matching `data/{id}.html` with the topics.
