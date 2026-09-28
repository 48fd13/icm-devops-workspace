#!/usr/bin/env python3
"""Initialize a DevOps workspace by copying this kit's template into a folder.

    python3 scripts/init-workspace.py /path/to/workspace
    python3 scripts/init-workspace.py /path/to/workspace --overwrite

Existing files are never replaced unless --overwrite is given, and then only
files that come from the template. Nothing is registered, no Git repository is
created, and no other file in the target is touched.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = KIT_ROOT / "template"
README = Path("_workspace/README.md")


def template_files() -> list[Path]:
    return sorted(p.relative_to(TEMPLATE) for p in TEMPLATE.rglob("*") if p.is_file())


def stamp_initialized(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^initialized:.*$", f"initialized: {date.today().isoformat()}", text, count=1, flags=re.M)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("target", help="Folder to initialize. It must already exist.")
    parser.add_argument("--overwrite", action="store_true", help="Replace existing files that come from the template.")
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    if not target.is_dir():
        print(f"Target folder does not exist: {target}", file=sys.stderr)
        return 1
    if target == KIT_ROOT or KIT_ROOT in target.parents:
        print("Refusing to initialize inside the kit itself.", file=sys.stderr)
        return 1

    copied: list[Path] = []
    skipped: list[Path] = []
    replaced: list[Path] = []
    for rel in template_files():
        dst = target / rel
        if dst.exists():
            if not args.overwrite:
                skipped.append(rel)
                continue
            replaced.append(rel)
        else:
            copied.append(rel)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(TEMPLATE / rel, dst)
        if rel == README:
            stamp_initialized(dst)

    for label, paths in (("Copied", copied), ("Replaced", replaced), ("Skipped (already exists)", skipped)):
        if paths:
            print(f"\n{label}: {len(paths)}")
            for rel in paths:
                print(f"  {rel}")

    print(f"\nWorkspace ready at {target}")
    if skipped:
        print("Some files already existed and were left unchanged. Review them, or re-run with --overwrite.")
    print("\nNext steps:")
    print("  1. Read AGENTS.md and adjust the safety gates to your environment.")
    print("  2. Describe your repositories in _workspace/map/workspace-map.md.")
    print("  3. Ask your agent for work; it routes through _workspace/map/routing-table.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
