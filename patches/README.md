# patches/ — Historical content-injection scripts

These are one-time Python scripts used to inject content into the site during
earlier development waves (`patch_beginner_concepts_v*`, `patch_ai`,
`patch_domains`, etc.). **Their output is already baked into `data/*.html`.**

They are kept only as a historical record of how each content wave was authored.
They are idempotent (each checks for a sentinel before injecting), so re-running
one is harmless — but there is no reason to. New content should be added by
editing `data/*.html` directly per **../CONTRIBUTING.md**, not by writing new
patch scripts.
