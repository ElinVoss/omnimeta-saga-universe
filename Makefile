# Makefile for OmniMeta Saga Consistency Checks

.PHONY: verify

verify:
	@bash .github/scripts/verify_consistency.sh

.PHONY: lint-prompts lint-prompts-strict

lint-prompts:
	@python3 .github/scripts/lint_bible_prompts.py

lint-prompts-strict:
	@python3 .github/scripts/lint_bible_prompts.py --strict-schema --require-all
