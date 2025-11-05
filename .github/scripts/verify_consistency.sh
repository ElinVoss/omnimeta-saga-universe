#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

BIBLES_DIR="04_Writer_Deliverables/02_Bibles"
TIMELINE="03_Structural_Timelines/01_Progression_Timeline_Master.md"
STORY_SPINE="03_Structural_Timelines/09_Story_Spine_Mapping_Innocent.md"

err(){ echo "❌ $*" >&2; exit 1; }

[[ -d "$BIBLES_DIR" ]] || err "Missing $BIBLES_DIR"

shopt -s nullglob
mapfile -t BIBLES < <(ls "$BIBLES_DIR"/N??_Bible_*.* 2>/dev/null | grep -E '\.(md|txt)$' || true)
((${#BIBLES[@]})) || err "No Bible files found"

declare -A seen
for path in "${BIBLES[@]}"; do
  f="$(basename "$path")"
  [[ "$f" =~ ^N[0-9]{2}_Bible_.*\.(md|txt)$ ]] || err "Bad filename: $f"
  n="${f:1:2}"                         # from N??_
  [[ -z "${seen[$n]:-}" ]] || err "Duplicate for N$n: ${seen[$n]} and $f"
  seen[$n]="$f"
done

# ensure exactly one file for each N01..N30 (either .md or .txt)
for n in $(seq -w 01 30); do
  [[ -n "${seen[$n]:-}" ]] || err "Missing Bible file for N$n"
done

# late-BREAK filenames must be the corrected canon
[[ "${seen[28],,}" =~ n28_bible_echoes_end\.(md|txt)$ ]] || err "N28 must be ECHOES_END (found: ${seen[28]:-missing})"
[[ "${seen[29],,}" =~ n29_bible_apex_of_stasis\.(md|txt)$ ]] || err "N29 must be APEX_OF_STASIS (found: ${seen[29]:-missing})"

# no old titles anywhere
if git grep -nE 'All Constructs Fall|Knotted Resolution' -- . >/dev/null; then
  git grep -nE 'All Constructs Fall|Knotted Resolution' -- .
  err "Old titles still present"
fi

# new titles must appear in timeline & spine
grep -q 'Echoes End' "$TIMELINE"       || err "Echoes End missing from timeline"
grep -q 'Apex of Stasis' "$TIMELINE"   || err "Apex of Stasis missing from timeline"
grep -q 'Echoes End' "$STORY_SPINE"    || err "Echoes End missing from story spine"
grep -q 'Apex of Stasis' "$STORY_SPINE"|| err "Apex of Stasis missing from story spine"

echo "✅ Consistency check passed."
