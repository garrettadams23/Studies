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
| Colored text       | `class="c-cyan"` etc.   | ~~`style="color:var(--cyan)"`~~          |

### Text-color utility classes

Prefer these over inline `style="color:…"`:

`c-cyan` · `c-green` · `c-amber` · `c-red` · `c-purple` · `c-muted`

They already track the light/dark theme via CSS variables.

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

## Adding a domain

Add an entry to `data/domains.json` (`id`, `colorClass`, `icon`, `title`,
`certTags`, `sub`) and create a matching `data/{id}.html` with the topics.
