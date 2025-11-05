#!/usr/bin/env python3
"""
Migrate legacy Bible prompt files to YAML front-matter.

- Parses headings from legacy prompts (md/txt) and builds front-matter:
  node, title, logline, beats, must_include, banned, continuity_in, continuity_out, acceptance
- Leaves the original content intact below the front-matter fence.
- Idempotent: run again and it won’t double-add front-matter.
- Best-effort extraction; leaves TODOs if a section is missing.

Usage:
  python3 .github/scripts/migrate_prompts_to_yaml.py [--write] [--nodes N01,N02,...]

Without --write it shows a preview diff in the console (non-destructive).
"""
import re, sys, argparse, difflib
from pathlib import Path

PROMPT_DIR = Path("04_Writer_Deliverables/02_Bibles")
GLOBS = ("N??_Bible_*.*",) # Corrected glob to match current file names
EXTS = {".md", ".txt"}
TITLE_BY_NODE = {28: "Echoes End", 29: "Apex of Stasis"}

def read_text(p):
    return p.read_text(encoding="utf-8", errors="ignore")

def write_text(p, s):
    p.write_text(s, encoding="utf-8")

def node_from_name(name):
    m = re.search(r"N(\d{2})_Bible_", name) # Corrected regex to match current file names
    return int(m.group(1)) if m else None

def parse_legacy(text):
    # crude slicer for sections
    def section(head):
        pat = rf"^\s*#\s*{head}\b(.*?)(?=^\s*#\s|\Z)"
        m = re.search(pat, text, flags=re.I|re.M|re.S)
        return m.group(1).strip() if m else ""

    gen_line = re.search(r'^\s*#\s*GENERATE.*?—\s*"([^"]+)"', text, flags=re.M)
    title = gen_line.group(1).strip() if gen_line else ""

    your_task = section("YOUR\\s+TASK")
    constraints = section("CRITICAL\\s+CONSTRAINTS")
    must_present = section("WHAT\\s+YOU\\s+MUST\\s+PRESENT")
    must_not = section("WHAT\\s+YOU\\s+MUST\\s+NOT\\s+PRESENT")
    foundation = section("FOUNDATION\\s+FILES.*")
    novella = section("NOVELLA\\s+SCOPE")
    immutable = section("MAJOR\\s+EVENTS\\s*\\(IMMUTABLE\\)")

    # extract bullets into lists
    def bullets(block):
        return [re.sub(r'^\s*[-*]\s+', '', ln).strip()
                for ln in block.splitlines() if re.match(r'^\s*[-*]\s+', ln)]

    beats = bullets(novella) or bullets(your_task)
    must_include = bullets(must_present)
    banned = bullets(must_not)

    # continuity guessing: pull file references from foundation block
    continuity_in = re.findall(r'(N\d{2}_[A-Za-z0-9_]+\\.\w+)', foundation)
    # continuity out: try to infer from last lines of novella/must_present
    continuity_out = []

    acceptance = []
    # seed default acceptance if empty
    if not acceptance:
        acceptance = [
            "Includes one irreversible decision",
            "Names a concrete cost for success",
            "Establishes a timer/pressure element",
            "Contains at least one specific, visual image"
        ]

    return {
        "title": title,
        "logline": (your_task.splitlines() or ["TODO: fill logline from YOUR TASK"])[0].strip(),
        "beats": beats[:7],
        "must_include": must_include,
        "banned": banned,
        "continuity_in": continuity_in[:10],
        "continuity_out": continuity_out,
        "acceptance": acceptance
    }

def has_frontmatter(text):
    return text.lstrip().startswith("---\n")

def build_frontmatter(node_num, data):
    # enforce canon titles on N28/N29
    if node_num in TITLE_BY_NODE and data["title"]:
        data["title"] = TITLE_BY_NODE[node_num]

    def list_block(key):
        items = data.get(key, [])
        if not items: return f"{key}: []"
        return f"{key}:\n" + "".join([f"  - {i}\n" for i in items])

    fm = [
        "---",
        f"node: {node_num}",
        f"title: {data.get('title','').strip() or 'TODO'}",
        f"logline: {data.get('logline','').strip() or 'TODO'}",
        list_block("beats"),
        list_block("must_include"),
        list_block("banned"),
        list_block("continuity_in"),
        list_block("continuity_out"),
        list_block("acceptance"),
        "---",
        ""
    ]
    return "\n".join(fm)

def migrate_file(p: Path, write=False):
    if p.suffix.lower() not in EXTS:
        return None
    text = read_text(p)
    if has_frontmatter(text):
        return None  # already migrated

    node_num = node_from_name(p.name)
    legacy = parse_legacy(text)
    fm = build_frontmatter(node_num, legacy)
    new_text = fm + text
    if not write:
        diff = difflib.unified_diff(text.splitlines(), new_text.splitlines(),
                                    fromfile=p.name, tofile=p.name+" (migrated)", lineterm="")
        print("\n".join(diff))
    else:
        write_text(p, new_text)
    return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="Apply changes in-place")
    ap.add_argument("--nodes", type=str, help="Comma list like N01,N02,...")
    args = ap.parse_args()

    allow = None
    if args.nodes:
        allow = {int(n[1:]) for n in args.nodes.split(",")}

    targets = []
    for pat in GLOBS:
        for p in sorted((PROMPT_DIR).glob(pat)):
            if p.suffix.lower() in EXTS:
                if allow is None or node_from_name(p.name) in allow:
                    targets.append(p)

    changed = 0
    for p in targets:
        res = migrate_file(p, write=args.write)
        if res: changed += 1

    print(f"Processed {len(targets)} file(s); migrated: {changed}")

if __name__ == "__main__":
    main()
