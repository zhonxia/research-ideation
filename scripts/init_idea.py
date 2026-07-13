#!/usr/bin/env python3
"""Initialize an IDEA workspace from the bundled v4 templates."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


DIRECTORIES = (
    "01-灵感收集",
    "02-评估中",
    "03-进行中",
    "04-已归档",
    "05-文献库",
    "06-跨领域方法库/领域",
)

ASSET_MAP = {
    "README.md": "README.md",
    "索引.md": "01-灵感收集/索引.md",
    "想点子指南.md": "01-灵感收集/想点子指南.md",
    "待评估点子.md": "01-灵感收集/待评估点子.md",
    "研究点子卡.md": "01-灵感收集/_研究点子卡模板.md",
    "evidence-log.md": "01-灵感收集/evidence-log.md",
    "文献.md": "05-文献库/_文献模板.md",
    "问题结构图谱.md": "01-灵感收集/问题结构图谱.md",
    "方法库索引.md": "06-跨领域方法库/索引.md",
    "方法卡模板.md": "06-跨领域方法库/领域/_方法卡模板.md",
    "组合创新扫描记录.md": "06-跨领域方法库/扫描记录.md",
}


def initialize(root: Path, *, force: bool = False, dry_run: bool = False) -> tuple[list[str], list[str]]:
    root = root.expanduser().resolve()
    assets = Path(__file__).resolve().parent.parent / "assets"
    created: list[str] = []
    skipped: list[str] = []

    for relative in DIRECTORIES:
        target = root / relative
        if not target.exists():
            if not dry_run:
                target.mkdir(parents=True, exist_ok=True)
            created.append(f"directory {target}")

    for source_name, target_name in ASSET_MAP.items():
        source = assets / source_name
        target = root / target_name
        if not source.is_file():
            raise FileNotFoundError(f"Bundled asset is missing: {source}")
        if target.exists() and not force:
            skipped.append(str(target))
            continue
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        created.append(f"file {target}")

    return created, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize an IDEA research-ideation workspace.")
    parser.add_argument("idea_root", help="Destination IDEA directory")
    parser.add_argument("--force", action="store_true", help="Overwrite existing template files")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without writing files")
    args = parser.parse_args()

    try:
        created, skipped = initialize(Path(args.idea_root), force=args.force, dry_run=args.dry_run)
    except (OSError, FileNotFoundError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    action = "Would create" if args.dry_run else "Created"
    print(f"{action}: {len(created)}")
    for item in created:
        print(f"  {item}")
    print(f"Skipped existing: {len(skipped)}")
    for item in skipped:
        print(f"  {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
