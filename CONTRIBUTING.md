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

**outside a table** — these utility classes track the theme and keep the markup clean.

`style="color: var(--sky)"` **inside a table cell**, and for any accent without a class.
This looks like it contradicts the line above, and it is worth knowing why it does not:
`.ref-table td` sets a colour, and a class loses to it while an inline style wins. 2196
elements on the page already carry a `c-*` class that is doing nothing for this reason.
Until that is fixed (see `plan.md`, session 18), a class in a table cell is a silent no-op.

The full accent palette lives in `:root` in `style.css`: `--cyan` `--green` `--amber`
`--red` `--purple` `--muted` `--text` `--sky` `--orange` `--pink` `--yellow` `--emerald`
`--indigo` `--violet` `--rose` `--fuchsia` `--lime`, plus dimmed `--amber-2/-3`,
`--green-2/-3` and `--cyan-2` for three-tone ladders. Add a variable there rather than a
literal here.

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
