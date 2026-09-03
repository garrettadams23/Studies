# One entry point for the whole pipeline, so nobody has to remember the order.
#
# The order is not arbitrary: the acronym domain is generated from the
# dictionary, the annotator rewrites content using it, the stamper reads the
# content, and build.py assembles what all three produced. Running them out of
# order produces a page that is correct-looking and stale.
#
# `make` on its own is `make build`. Everything is plain Python and Node — no
# package manager, no virtualenv, no lockfile.

PY ?= python3
NODE ?= node

.DEFAULT_GOAL := build
.PHONY: build check test a11y og og-check visual all fmt acronyms stamp census clean help search browser resilience mobile backup measure

## build: regenerate index.html from data/ (the usual command)
build:
	$(PY) tools/gen_acronym_domain.py
	$(PY) tools/annotate_acronyms.py
	$(PY) build.py

## acronyms: rebuild the acronym domain and re-run the annotator only
acronyms:
	$(PY) tools/gen_acronym_domain.py
	$(PY) tools/annotate_acronyms.py

## stamp: re-derive freshness dates for one domain — make stamp ONLY=m365
stamp:
	@test -n "$(ONLY)" || { echo "usage: make stamp ONLY=<domain|file>"; exit 2; }
	$(PY) tools/stamp_freshness.py --only $(ONLY)

## check: every static gate CI runs, in the order that fails fastest
#
# "every static gate CI runs" was aspirational, not true: the generated
# artefacts — the acronym domain, the cheat sheet, the social card, the TI-84
# drill bank — were checked only on the server, and three of the four went stale
# without anyone noticing, because a red job step is only red where somebody
# looks. They are cheap and they are first now. None of them needs a browser.
check:
	$(PY) tools/check_gates.py
	$(PY) tools/gen_acronym_domain.py --check
	$(PY) tools/gen_cheatsheet.py --check
	$(NODE) tools/gen_og_image.mjs --check
	$(PY) tools/ti84_trainer.py --verify
	$(PY) tools/ti84_trainer.py --check-card
	$(PY) tools/check_markup.py --self-test
	$(PY) tools/check_markup.py
	$(PY) tools/lint_content.py
	$(PY) tools/fix_topic_names.py --check
	$(PY) tools/annotate_acronyms.py --check
	$(PY) tools/check_renames.py
	$(PY) tools/check_contradictions.py --self-test
	$(PY) tools/check_contradictions.py --strict
	$(PY) tools/check_contradictions.py --pairs --strict
	$(PY) tools/check_volatility.py --self-test
	$(PY) tools/check_volatility.py
	$(PY) tools/suggest_related.py --check
	$(PY) tools/check_paths.py
	$(PY) tools/stamp_freshness.py --verify
	$(PY) tools/check_determinism.py
	$(PY) tools/page_budget.py

## census: the four reports that measure content rather than gate it
census:
	@echo "── depth ──"       && $(PY) tools/depth_report.py
	@echo "── the floor ──"   && $(PY) tools/depth_report.py --bottom 12
	@echo "── duplicates ──"  && $(PY) tools/near_duplicates.py
	@echo "── orphans ──"     && $(PY) tools/orphan_report.py
	@echo "── questions ──"   && $(NODE) tools/query_probe.mjs --zero

## measure: time the load, and what N times the content would do to it
#
# Not in `make all` and it never fails: page_budget.py enforces a size, this is
# the measurement that size stands for. Its own output says which of its columns
# mean anything — read that before quoting one.
measure:
	$(NODE) tools/measure_load.mjs

## test: drive the built page in a real browser (needs playwright + chromium)
test:
	$(NODE) tools/smoke_test.mjs

## search: does searching for a thing find it (plan.md Phase 10 T5)
search:
	$(NODE) tools/search_test.mjs

## a11y: axe-core over the shell, a domain and a dialog, in both themes
a11y:
	$(NODE) tools/a11y_test.mjs

## og: regenerate the social card from the current content
og:
	$(NODE) tools/gen_og_image.mjs

## visual: pixel-diff the filter bar against tools/baseline (--update to accept)
visual:
	$(NODE) tools/visual_test.mjs

## resilience: the page must still work when the browser denies storage
resilience:
	$(NODE) tools/storage_denied_test.mjs

## mobile: the page must not scroll sideways at a phone's width (375px)
mobile:
	$(NODE) tools/mobile_test.mjs

## backup: an export must restore exactly what it saved (no data loss)
backup:
	$(NODE) tools/backup_test.mjs

## browser: every gate that needs playwright and chromium
browser: test search a11y visual resilience mobile backup

## all: build, then every check, then every browser gate
#
# `make all` is the contract: if this passes, CI passes. It did not used to be —
# `search` ran in CI and not here, `resilience`, `mobile` and `backup` ran here
# and not in CI, and neither list was a superset of the other. tools/check_gates.py
# is what keeps the two honest; it runs inside `make check`.
all: build check browser

## help: list these targets
help:
	@grep -E '^## ' $(MAKEFILE_LIST) | sed 's/^## /  /'
