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
.PHONY: build check test all fmt acronyms stamp clean help

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
check:
	$(PY) tools/check_markup.py --self-test
	$(PY) tools/check_markup.py
	$(PY) tools/lint_content.py
	$(PY) tools/fix_topic_names.py --check
	$(PY) tools/annotate_acronyms.py --check
	$(PY) tools/check_renames.py
	$(PY) tools/check_contradictions.py --strict
	$(PY) tools/suggest_related.py --check
	$(PY) tools/check_paths.py
	$(PY) tools/stamp_freshness.py --verify
	$(PY) tools/page_budget.py

## test: drive the built page in a real browser (needs playwright + chromium)
test:
	$(NODE) tools/smoke_test.mjs

## all: build, then every check, then the browser tests
all: build check test

## help: list these targets
help:
	@grep -E '^## ' $(MAKEFILE_LIST) | sed 's/^## /  /'
