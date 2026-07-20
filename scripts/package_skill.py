#!/usr/bin/env python3
"""Build a deterministic, runtime-only research-ideation skill archive."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path


RUNTIME_ROOT_FILES = ("SKILL.md",)
RUNTIME_DIRECTORIES = ("agents", "assets", "references")
RUNTIME_SCRIPTS = ("init_idea.py", "validate_idea_index.py")
ZIP_TIMESTAMP = (2020, 1, 1, 0, 0, 0)


def runtime_files(skill_root: Path) -> list[Path]:
    files = [skill_root / name for name in RUNTIME_ROOT_FILES]
    for dirname in RUNTIME_DIRECTORIES:
        directory = skill_root / dirname
        if directory.is_dir():
            files.extend(path for path in directory.rglob("*") if path.is_file())
    files.extend(skill_root / "scripts" / name for name in RUNTIME_SCRIPTS)
    return sorted(files, key=lambda path: path.relative_to(skill_root).as_posix())


def build_archive(output: Path) -> list[str]:
    skill_root = Path(__file__).resolve().parent.parent
    output = output.expanduser().resolve()
    files = runtime_files(skill_root)
    missing = [path for path in files if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing runtime file: {missing[0]}")

    output.parent.mkdir(parents=True, exist_ok=True)
    members: list[str] = []
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = path.relative_to(skill_root).as_posix()
            member = relative
            # Write parent directory entries first (required by some zip importers)
            parent = Path(relative).parent
            if str(parent) != ".":
                parent_path = str(parent) + "/"
                if parent_path not in members:
                    dir_info = zipfile.ZipInfo(parent_path, date_time=ZIP_TIMESTAMP)
                    dir_info.external_attr = 0o40755 << 16
                    archive.writestr(dir_info, "")
                    members.append(parent_path)
            info = zipfile.ZipInfo(member, date_time=ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
            members.append(member)
    return members


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a lean research-ideation skill archive.")
    parser.add_argument("output", nargs="?", default="dist/research-ideation.zip", help="Output zip path")
    args = parser.parse_args()
    try:
        members = build_archive(Path(args.output))
    except OSError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Created {Path(args.output).expanduser().resolve()} with {len(members)} runtime files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
