#!/usr/bin/env python3
"""
OmniMeta Bible Prompt Linter

What it does (fast + ruthless):
- Finds all prompt files in 04_Writer_Deliverables/02_Bibles matching N??_Prompt_*.(md|txt|yaml|yml)
- Passes if a file matches EITHER:
    A) New schema: YAML front-matter at top with required keys (see REQUIRED_* below)
    B) Legacy schema: required markdown headings (GENERATE, YOUR TASK, CRITICAL CONSTRAINTS, etc.)
- For N28/N29, enforces corrected titles (Echoes End / Apex of Stasis)
- For new schema, enforces:
    - beats length 3..7
    - acceptance includes: irreversible / cost / timer / image (keyword match)
    - node number matches filename
- Optional modes:
    --require-all       -> fail if any N01..N30 prompt is missing
    --strict-schema     -> require NEW YAML schema (legacy no longer accepted)
    --json              -> print machine-readable summary to stdout

Exit codes:
  0 = OK, 1 = failures detected
"""
import sys, re, json, argparse
from pathlib import Path
from typing import Dict, Any, List, Tuple

PROMPT_DIR = Path("04_Writer_Deliverables/02_Bibles")
PROMPT_PATTERNS = ("N??_Bible_*.*",) # Corrected pattern to match current file names
ALLOWED_EXTS = {".md", ".txt", ".yaml", ".yml"}

REQ_SCALARS = ["node", "title", "logline"]
REQ_LISTS   = ["beats", "must_include", "banned", "continuity_in", "continuity_out", "acceptance"]
ACCEPTANCE_KEYWORDS = ["irreversible", "cost", "timer", "image"]

TITLE_BY_NODE = {28: "Echoes End", 29: "Apex of Stasis"}

# ---- utils -----------------------------------------------------------------
def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

def node_from_filename(name: str) -> int | None:
    m = re.search(r"N(\d{2})_Bible_", name) # Corrected regex to match current file names
    return int(m.group(1)) if m else None

def parse_frontmatter(text: str) -> Tuple[Dict[str, Any], str]:
    """
    Extremely simple front-matter parser supporting:
      key: value
      key:
        - item
        - item
    Returns (data_dict, body_without_frontmatter)
    """
    lines = text.splitlines()
    i = 0
    # skip leading blank
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i >= len(lines) or lines[i].strip() != "---":
        return {}, text  # no frontmatter
    i += 1
    data: Dict[str, Any] = {}
    current_list_key: str | None = None
    while i < len(lines):
        ln = lines[i]
        if ln.strip() == "---":
            i += 1
            break
        # key: value
        m = re.match(r"^\s*([A-Za-z0-9_]+)\s*:\s*(.*)$", ln)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val == "" and key in REQ_LISTS:
                data[key] = []
                current_list_key = key
            else:
                data[key] = val
                current_list_key = key if key in REQ_LISTS else None
        else:
            # list item?
            m2 = re.match(r"^\s*-\s+(.*)$", ln)
            if m2 and current_list_key:
                data.setdefault(current_list_key, [])
                data[current_list_key].append(m2.group(1).strip())
        i += 1
    body = "\n".join(lines[i:])
    return data, body

def has_legacy_sections(text: str) -> List[str]:
    """Return list of missing legacy headings (empty if OK). Case-insensitive, flexible spacing."""
    patterns = {
        "GENERATE": r"^\s*#\s*GENERATE\b",
        "YOUR TASK": r"^\s*#\s*YOUR\s+TASK\b",
        "CRITICAL CONSTRAINTS": r"^\s*#\s*CRITICAL\s+CONSTRAINTS\b",
        "MUST PRESENT": r"^\s*#\s*WHAT\s+YOU\s+MUST\s+PRESENT\b",
        "MUST NOT": r"^\s*#\s*WHAT\s+YOU\s+MUST\s+NOT\s+PRESENT\b",
        "FOUNDATION": r"^\s*#\s*FOUNDATION\s+FILES.*",
        "NOVELLA SCOPE": r"^\s*#\s*NOVELLA\s+SCOPE\b",
        "IMMUTABLE": r"^\s*#\s*MAJOR\s+EVENTS\s*\(IMMUTABLE\)\b",
    }
    missing = []
    for label, pat in patterns.items():
        if not re.search(pat, text, flags=re.I | re.M):
            missing.append(label)
    return missing

def find_immutable_bullets(text: str) -> int:
    # count bullets under the IMMUTABLE section (rudimentary)
    m = re.search(r"^\s*#\s*MAJOR\s+EVENTS\s*\(IMMUTABLE\)\b(.*?)(?:^\s*#\s|\Z)", text, flags=re.I | re.M | re.S)
    if not m:
        return 0
    block = m.group(1)
    return len(re.findall(r"^\s*[-*]\s+", block, flags=re.M))

# ---- validators -------------------------------------------------------------
def validate_yaml_schema(front: Dict[str, Any], filename_node: int) -> List[str]:
    errs = []
    # required scalars
    for k in REQ_SCALARS:
        if k not in front or str(front[k]).strip() == "":
            errs.append(f"Missing YAML key: {k}")
    # required lists
    for k in REQ_LISTS:
        if k not in front or not isinstance(front[k], list) or len(front[k]) == 0:
            errs.append(f"Missing/empty YAML list: {k}")
    # node match
    try:
        n_val = front.get("node")
        node_num = int(str(n_val).replace("N", "").strip())
        if filename_node and node_num != filename_node:
            errs.append(f"Node mismatch: frontmatter says N{node_num:02d}, filename is N{filename_node:02d}")
    except Exception:
        errs.append("YAML 'node' must be an int or 'N##'")
    # beats length
    if "beats" in front:
        blen = len(front["beats"])
        if blen < 3 or blen > 7:
            errs.append(f"beats must contain 3..7 items (found {blen})")
    # acceptance includes key concepts
    if "acceptance" in front:
        acc = " ".join(front["acceptance"]).lower()
        for kw in ACCEPTANCE_KEYWORDS:
            if kw not in acc:
                errs.append(f"acceptance missing keyword: {kw}")
    # N28/N29 titles
    if filename_node in TITLE_BY_NODE:
        want = TITLE_BY_NODE[filename_node]
        got = str(front.get("title", "")).strip()
        if got != want:
            errs.append(f"N{filename_node:02d} title must be '{want}' (got '{got}')")
    return errs

def validate_legacy(text: str, filename_node: int) -> List[str]:
    errs = []
    missing = has_legacy_sections(text)
    if missing:
        errs.append("Missing legacy sections: " + ", ".join(missing))
    # IMMUTABLE should have >=1 bullet
    if find_immutable_bullets(text) == 0:
        errs.append("IMMUTABLE section has no bullet points")
    # N28/N29 title check (best-effort)
    if filename_node in (28, 29):
        # try to read the heading line after GENERATE for the quoted title
        m = re.search(r"^\s*#\s*GENERATE.*?—\s*\"([^\"]+)\"", text, flags=re.M)
        if m:
            got = m.group(1).strip()
            want = TITLE_BY_NODE[filename_node]
            if got != want:
                errs.append(f"N{filename_node:02d} title must be '{want}' (got '{got}')")
    return errs

# ---- main ------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--require-all", action="store_true", help="Require prompts for N01..N30 to exist")
    ap.add_argument("--strict-schema", action="store_true", help="Require YAML schema; do not accept legacy headings")
    ap.add_argument("--json", action="store_true", help="Print JSON summary")
    args = ap.parse_args()

    root = Path(".").resolve()
    prompt_root = (root / PROMPT_DIR)
    results = []

    # discover files
    files: List[Path] = []
    if prompt_root.exists():
        for pat in PROMPT_PATTERNS:
            files.extend(sorted([p for p in prompt_root.glob(pat) if p.suffix.lower() in ALLOWED_EXTS]))
    files = sorted(files, key=lambda p: p.name)

    # optional completeness check
    missing_nodes = []
    if args.require_all:
        present_nodes = {node_from_filename(p.name) for p in files if node_from_filename(p.name)}
        for i in range(1, 31):
            if i not in present_nodes:
                missing_nodes.append(i)

    failures = 0
    for p in files:
        text = read_text(p)
        fname_node = node_from_filename(p.name)
        front, body = parse_frontmatter(text)
        used_schema = False
        errs = []
        if front:
            used_schema = True
            errs = validate_yaml_schema(front, fname_node or -1)
        if not front or (errs and not args.strict_schema):
            # Try legacy if either no frontmatter OR invalid schema but not strict
            legacy_errs = validate_legacy(text, fname_node or -1)
            if not front or (errs and not args.strict_schema and not legacy_errs):
                # legacy accepted
                errs = []
                used_schema = False
            else:
                # choose the smaller error list to show
                if not args.strict_schema and len(legacy_errs) < len(errs):
                    errs = legacy_errs
                    used_schema = False
        results.append({
            "file": str(p.relative_to(root)),
            "node": fname_node,
            "used_schema": used_schema,
            "errors": errs
        })
        if errs:
            failures += 1

    if args.require_all and missing_nodes:
        failures += 1

    if args.json:
        print(json.dumps({
            "missing_nodes": [f"N{n:02d}" for n in missing_nodes],
            "results": results
        }, indent=2))
    else:
        if args.require_all and missing_nodes:
            print("❌ Missing prompt files for:", ", ".join(f"N{n:02d}" for n in missing_nodes))
        for r in results:
            if r["errors"]:
                print(f"❌ {r['file']} [{f'N{r['node']:02d}' if r['node'] else '?'}]:")
                for e in r["errors"]:
                    print(f"   - {e}")
            else:
                print(f"✅ {r['file']} [{f'N{r['node']:02d}' if r['node'] else '?'}] ({'YAML' if r['used_schema'] else 'legacy'})")

    sys.exit(1 if failures or (args.require_all and missing_nodes) else 0)

if __name__ == "__main__":
    main()
