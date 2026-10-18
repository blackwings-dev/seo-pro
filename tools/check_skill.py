#!/usr/bin/env python3
"""
check_skill.py — integrity checks for the seo-pro repository. Standard library only.

  python3 tools/check_skill.py            # from the repository root; exit 1 if anything is wrong

Checks:
  1. Every practice ID cited anywhere (references, SKILL.md, scripts) has a heading that defines it.
  2. Every backticked path to a skill file (references/…, scripts/…, ../verticals/…) exists.
  3. Every relative Markdown link points to a file that exists.
  4. Every Markdown table row has the same number of columns as its header.
  5. SKILL.md frontmatter has a name and a description of at most 1,024 characters.
  6. plugin.json, marketplace.json and evals.json are valid; the plugin version matches the top CHANGELOG entry.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "plugins" / "seo-pro" / "skills" / "seo-pro"
PREFIXES = "BAVWLEPSYMXRDGO"   # engine, vertical, playbook and operating-plan layers
ID_RX = re.compile(rf"(?<![\w/.#-])([{PREFIXES}])(\d{{1,2}})(?![\w])")
HEADING_RX = re.compile(r"^#{2,3} ([A-Z]?\d+)\.", re.M)
PATH_RX = re.compile(r"`((?:\.\./)*(?:references|scripts|verticals|playbooks|engines)/[^`\s]+?\.(?:md|py))(?:#[^`]*)?`")
LINK_RX = re.compile(r"\[[^\]]*\]\(((?!https?:|mailto:|#)[^)\s]+)\)")
PRACTICES_IN_CODE = re.compile(r'self\.add\(\s*"(?:critical|warning|info)",\s*"([^"]+)"')
NON_ID_CONTEXT = re.compile(r"(Q[0-4]|T[0-4]|H[1-6]|P75|p75|A4 paper)")

errors: list[str] = []


def err(msg: str):
    errors.append(msg)


def md_files() -> list[Path]:
    files = sorted(SKILL.rglob("*.md")) + [ROOT / "README.md", ROOT / "CHANGELOG.md"]
    return [f for f in files if f.exists()]


def defined_ids() -> set[str]:
    ids = set()
    for f in sorted(SKILL.rglob("*.md")):
        ids.update(HEADING_RX.findall(f.read_text(encoding="utf-8")))
    return ids


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def check_ids(ids: set[str]):
    for f in sorted(SKILL.rglob("*.md")):
        text = strip_code_blocks(f.read_text(encoding="utf-8"))
        for m in ID_RX.finditer(text):
            ident = m.group(1) + m.group(2)
            if ident not in ids:
                line = text[: m.start()].count("\n") + 1
                err(f"{f.relative_to(ROOT)}:{line}: practice {ident} is cited but never defined")
    for py in sorted((SKILL / "scripts").glob("*.py")):
        src = py.read_text(encoding="utf-8")
        for m in PRACTICES_IN_CODE.finditer(src):
            for token in re.split(r"[,\s]+", m.group(1)):
                if not token or token in ("myths",):
                    continue
                if re.fullmatch(r"\d+", token):
                    if not 1 <= int(token) <= 160:
                        err(f"{py.name}: practice {token} is outside 1–160")
                elif token not in ids:
                    err(f"{py.name}: finding cites {token}, which no reference defines")


def check_paths():
    for f in md_files():
        text = f.read_text(encoding="utf-8")
        for m in PATH_RX.finditer(text):
            rel = m.group(1)
            candidates = [f.parent / rel, SKILL / rel, SKILL / "references" / rel]
            if not any(c.resolve().exists() for c in candidates):
                line = text[: m.start()].count("\n") + 1
                err(f"{f.relative_to(ROOT)}:{line}: path `{rel}` does not exist")
        for m in LINK_RX.finditer(strip_code_blocks(text)):
            target = m.group(1).split("#", 1)[0]
            if target and not (f.parent / target).resolve().exists():
                line = text[: m.start()].count("\n") + 1
                err(f"{f.relative_to(ROOT)}:{line}: link target {target} does not exist")


def check_tables():
    for f in md_files():
        in_code = False
        header_cols = None
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_code = not in_code
                header_cols = None
                continue
            if in_code:
                continue
            s = line.strip()
            if not (s.startswith("|") and s.endswith("|")):
                header_cols = None
                continue
            cols = len(re.split(r"(?<!\\)\|", s)) - 2
            if header_cols is None:
                header_cols = cols
            elif cols != header_cols:
                err(f"{f.relative_to(ROOT)}:{i}: table row has {cols} columns, header has {header_cols}")


def check_manifests():
    skill_md = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    fm = re.match(r"^---\n(.*?)\n---\n", skill_md, re.S)
    if not fm:
        err("SKILL.md: missing frontmatter")
    else:
        name = re.search(r"^name:\s*(.+)$", fm.group(1), re.M)
        desc = re.search(r"^description:\s*(.+)$", fm.group(1), re.M)
        if not name:
            err("SKILL.md: frontmatter has no name")
        if not desc:
            err("SKILL.md: frontmatter has no description")
        elif len(desc.group(1)) > 1024:
            err(f"SKILL.md: description is {len(desc.group(1))} characters (limit 1,024)")
    version = None
    for path in (ROOT / ".claude-plugin" / "marketplace.json", ROOT / "plugins" / "seo-pro" / ".claude-plugin" / "plugin.json",
                 ROOT / "evals" / "evals.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            err(f"{path.relative_to(ROOT)}: {e}")
            continue
        if path.name == "plugin.json":
            version = data.get("version")
    top = re.search(r"^## (\d+\.\d+\.\d+)", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), re.M)
    if version and top and top.group(1) != version:
        err(f"plugin.json version {version} does not match the top CHANGELOG entry {top.group(1)}")
    for py in sorted((SKILL / "scripts").glob("*.py")):
        if "__version__" not in py.read_text(encoding="utf-8"):
            err(f"{py.name}: no __version__")


def main() -> int:
    ids = defined_ids()
    check_ids(ids)
    check_paths()
    check_tables()
    check_manifests()
    if errors:
        print(f"{len(errors)} problem(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK — {len(ids)} practice IDs defined, {len(md_files())} Markdown files checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
