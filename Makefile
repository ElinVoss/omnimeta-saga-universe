# Makefile for OmniMeta Saga Consistency Checks

.PHONY: verify

verify:
	@bash .github/scripts/verify_consistency.sh
