#!/usr/bin/env python3
"""
Build machine-friendly generation payloads from Bible prompts.

Inputs: N??_Bible_*.(md|txt|yaml|yml) under 04_Writer_Deliverables/02_Bibles
- Prefers YAML front-matter (strict keys)
- Falls back to legacy headings (best-effort extraction)

Outputs:
- Single node: JSON to stdout or --out path
- All nodes: --all -> writes NDJSON (one JSON per line) to --out

Usage:
  python3 tools/build_generation_payload.py --node N23 --out payload.json
  python3 tools/build_generation_payload.py --all --out payloads.ndjson
"""
import re, json, argparse
from pathlib import Path

PROMPT_DIR = Path("04_Writer_Deliverables/02_Bibles")
ALLOWED = (".md", ".txt", ".yaml", ".yml")
TITLE_BY_NODE = {28: "Echoes End", 29: "Apex of Stasis"}

def read_text(p): return p.read_text(encoding="utf-8", errors="ignore")

def node_from_name(name):
    m = re.search(r"N(\d{2})_Bible_", name) # Corrected regex to match current file names
    return int(m.group(1)) if m else None

def parse_frontmatter(text):
    # same simple parser as in linter; returns dict or {}
    lines = text.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i >= len(lines) or lines[i].strip() != "---":
        return {}, text
    i += 1
    data, cur = {}, None
    while i < len(lines):
        ln = lines[i]
        if ln.strip() == "---":
            i += 1
            break
        m = re.match(r"^\s*([A-Za-z0-9_]+)\s*:\s*(.*)$", ln)
        if m:
            k, v = m.group(1), m.group(2).strip()
            if v == "":
                data[k] = []
                cur = k
            else:
                data[k] = v
                cur = k if isinstance(data.get(k), list) else None
        else:
            m2 = re.match(r"^\s*-\s+(.*)$", ln)
            if m2 and cur:
                data.setdefault(cur, []).append(m2.group(1).strip())
        i += 1
    body = "\n".join(lines[i:])
    return data, body

def parse_legacy(text):
    def section(h):
        pat = rf"^\s*#\s*{h}\b(.*?)(?=^\s*#\s|\Z)"
        m = re.search(pat, text, flags=re.I|re.M|re.S)
        return m.group(1).strip() if m else ""
    gen_line = re.search(r'^\s*#\s*GENERATE.*?—\s*"([^"]+)"', text, flags=re.M)
    title = gen_line.group(1).strip() if gen_line else ""
    your_task = section("YOUR\\s+TASK")
    beats = [re.sub(r'^\s*[-*]\s+', '', ln).strip()
             for ln in section("NOVELLA\\s+SCOPE").splitlines() if re.match(r'^\s*[-*]\s+', ln)]
    must_include = [re.sub(r'^\s*[-*]\s+', '', ln).strip()
                    for ln in section("WHAT\\s+YOU\\s+MUST\\s+PRESENT").splitlines() if re.match(r'^\s*[-*]\s+', ln)]
    banned = [re.sub(r'^\s*[-*]\s+', '', ln).strip()
              for ln in section("WHAT\\s+YOU\\s+MUST\\s+NOT\\s+PRESENT").splitlines() if re.match(r'^\s*[-*]\s+', ln)]
    acceptance = [
        "Includes one irreversible decision",
        "Names a concrete cost for success",
        "Establishes a timer/pressure element",
        "Contains at least one specific, visual image"
    ]
    return {
        "title": title or "TODO",
        "logline": (your_task.splitlines() or ["TODO: fill logline from YOUR TASK"])[0].strip(),
        "beats": beats[:7] or ["TODO: add 3–7 beats"],
        "must_include": must_include,
        "banned": banned,
        "continuity_in": [],
        "continuity_out": [],
        "acceptance": acceptance
    }

def normalize(node_num, data):
    # enforce canon for N28/N29
    if node_num in TITLE_BY_NODE:
        data["title"] = TITLE_BY_NODE[node_num]
    # minimal sanity
    data["node"] = node_num
    data.setdefault("beats", [])
    data["beats"] = data["beats"][:7]
    return data

def load_prompt(node: int):
    # find the file with this node
    candidates = sorted([p for p in PROMPT_DIR.glob(f"N{node:02d}_Bible_*.*") if p.suffix.lower() in ALLOWED])
    if not candidates:
        raise SystemExit(f"No prompt file found for N{node:02d}")
    p = candidates[0]
    text = read_text(p)
    fm, _ = parse_frontmatter(text)
    if fm:
        data = {
            "title": fm.get("title",""),
            "logline": fm.get("logline",""),
            "beats": fm.get("beats", []),
            "must_include": fm.get("must_include", []),
            "banned": fm.get("banned", []),
            "continuity_in": fm.get("continuity_in", []),
            "continuity_out": fm.get("continuity_out", []),
            "acceptance": fm.get("acceptance", []),
        }
    else:
        data = parse_legacy(text)
    return normalize(node, data)

def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--node", type=str, help="Node like N23 or 23")
    g.add_argument("--all", action="store_true")
    ap.add_argument("--out", type=str, help="Output file (.json for single, .ndjson for --all)")
    args = ap.parse_args()

    if args.node:
        num = int(args.node.replace("N",""))
        payload = load_prompt(num)
        s = json.dumps(payload, indent=2)
        if args.out:
            Path(args.out).write_text(s, encoding="utf-8")
        else:
            print(s)
        return

    # all nodes -> NDJSON
    out_lines = []
    for i in range(1, 31):
        try:
            payload = load_prompt(i)
            out_lines.append(json.dumps(payload))
        except SystemExit:
            # skip missing in legacy; strictness is enforced by your linter elsewhere
            continue

    data = "\n".join(out_lines) + ("\n" if out_lines else "")
    if args.out:
        Path(args.out).write_text(data, encoding="utf-8")
    else:
        print(data)

if __name__ == "__main__":
    main()
