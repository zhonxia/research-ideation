#!/usr/bin/env python3
"""Validate consistency of a Research Ideation IDEA folder.

Checks:
- required IDEA files/directories exist
- ideas in 索引.md have lifecycle-consistent locations
- 待评估点子.md and 索引.md agree on pending ideas
- folders in 02-评估中 / 03-进行中 / 04-已归档 are registered in 索引.md

The parser intentionally accepts simple Markdown tables instead of requiring a
strict database format. This keeps the IDEA system lightweight while catching
the lifecycle drift that tends to accumulate over time.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


STATUS_DIRS = {
    "评估中": "02-评估中",
    "进行中": "03-进行中",
    "已归档": "04-已归档",
}
PENDING_STATUS = "待评估"


@dataclass
class Finding:
    level: str
    code: str
    message: str
    path: str | None = None


@dataclass
class IdeaRecord:
    title: str
    status: str
    source: str


def strip_markdown(value: str) -> str:
    value = value.strip()
    value = re.sub(r"`([^`]*)`", r"\1", value)
    value = re.sub(r"\*\*([^*]*)\*\*", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")
    return re.sub(r"\s+", " ", value).strip()


def canonical_title(value: str) -> str:
    value = strip_markdown(value)
    value = re.sub(r"^[#\-\*\d\.\s]+", "", value)
    value = re.sub(r"\s+", "", value)
    return value.casefold()


def canonical_status(value: str) -> str:
    value = strip_markdown(value)
    for status in [PENDING_STATUS, *STATUS_DIRS.keys()]:
        if status in value:
            return status
    lower = value.casefold()
    aliases = {
        "pending": PENDING_STATUS,
        "todo": PENDING_STATUS,
        "under evaluation": "评估中",
        "evaluating": "评估中",
        "active": "进行中",
        "in progress": "进行中",
        "archived": "已归档",
        "done": "已归档",
        "abandoned": "已归档",
    }
    return aliases.get(lower, value)


def split_markdown_row(line: str) -> list[str]:
    line = line.strip()
    if not line.startswith("|") or not line.endswith("|"):
        return []
    return [cell.strip() for cell in line.strip("|").split("|")]


def is_separator_row(cells: Iterable[str]) -> bool:
    cells = list(cells)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def iter_markdown_tables(text: str) -> Iterable[tuple[list[str], list[list[str]]]]:
    lines = text.splitlines()
    i = 0
    while i < len(lines) - 1:
        header = split_markdown_row(lines[i])
        separator = split_markdown_row(lines[i + 1])
        if header and is_separator_row(separator) and len(header) == len(separator):
            rows: list[list[str]] = []
            i += 2
            while i < len(lines):
                row = split_markdown_row(lines[i])
                if not row:
                    break
                if len(row) < len(header):
                    row.extend([""] * (len(header) - len(row)))
                rows.append(row[: len(header)])
                i += 1
            yield header, rows
        else:
            i += 1


def find_column(headers: list[str], candidates: list[str]) -> int | None:
    normalized = [strip_markdown(h).casefold() for h in headers]
    for candidate in candidates:
        candidate = candidate.casefold()
        for idx, header in enumerate(normalized):
            if candidate == header or candidate in header:
                return idx
    return None


def read_text(path: Path, findings: list[Finding]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        findings.append(Finding("ERROR", "missing_file", "Required file is missing", str(path)))
    except UnicodeDecodeError:
        findings.append(Finding("ERROR", "decode_error", "File is not valid UTF-8", str(path)))
    return ""


def parse_index(index_path: Path, findings: list[Finding]) -> dict[str, IdeaRecord]:
    text = read_text(index_path, findings)
    records: dict[str, IdeaRecord] = {}
    if not text:
        return records

    found_table = False
    for headers, rows in iter_markdown_tables(text):
        title_col = find_column(headers, ["标题", "点子", "idea", "title"])
        status_col = find_column(headers, ["状态", "status"])
        if title_col is None or status_col is None:
            continue
        found_table = True
        for row in rows:
            title = strip_markdown(row[title_col])
            status = canonical_status(row[status_col])
            if not title:
                continue
            key = canonical_title(title)
            if key in records:
                findings.append(
                    Finding(
                        "ERROR",
                        "duplicate_index_entry",
                        f"Duplicate index entry for idea: {title}",
                        str(index_path),
                    )
                )
            records[key] = IdeaRecord(title=title, status=status, source=str(index_path))

    if not found_table:
        findings.append(
            Finding(
                "ERROR",
                "index_table_not_found",
                "Could not find an index table with title/idea and status columns",
                str(index_path),
            )
        )
    return records


def parse_pending_pool(pending_path: Path, findings: list[Finding]) -> dict[str, str]:
    text = read_text(pending_path, findings)
    pending: dict[str, str] = {}
    if not text:
        return pending

    found_table = False
    for headers, rows in iter_markdown_tables(text):
        idea_col = find_column(headers, ["点子", "idea", "title", "标题"])
        if idea_col is None:
            continue
        found_table = True
        for row in rows:
            title = strip_markdown(row[idea_col])
            if title:
                pending[canonical_title(title)] = title

    if not found_table:
        findings.append(
            Finding(
                "WARN",
                "pending_table_not_found",
                "Could not find a pending idea table; skipping pending-pool cross-check",
                str(pending_path),
            )
        )
    return pending


def list_status_folders(idea_root: Path, findings: list[Finding]) -> dict[str, dict[str, str]]:
    folders_by_status: dict[str, dict[str, str]] = {}
    for status, dirname in STATUS_DIRS.items():
        folder = idea_root / dirname
        if not folder.exists():
            findings.append(Finding("ERROR", "missing_dir", "Required status directory is missing", str(folder)))
            folders_by_status[status] = {}
            continue
        if not folder.is_dir():
            findings.append(Finding("ERROR", "not_directory", "Required status path is not a directory", str(folder)))
            folders_by_status[status] = {}
            continue
        entries = {}
        for child in folder.iterdir():
            if child.name.startswith("."):
                continue
            if child.is_dir():
                entries[canonical_title(child.name)] = child.name
        folders_by_status[status] = entries
    return folders_by_status


def validate(idea_root: Path) -> tuple[list[Finding], dict[str, object]]:
    findings: list[Finding] = []
    idea_root = idea_root.resolve()

    if not idea_root.exists():
        return [Finding("ERROR", "missing_root", "IDEA root does not exist", str(idea_root))], {}
    if not idea_root.is_dir():
        return [Finding("ERROR", "root_not_directory", "IDEA root is not a directory", str(idea_root))], {}

    collection_dir = idea_root / "01-灵感收集"
    index_path = collection_dir / "索引.md"
    pending_path = collection_dir / "待评估点子.md"
    for required in [collection_dir, idea_root / "05-文献库"]:
        if not required.exists():
            findings.append(Finding("ERROR", "missing_dir", "Required directory is missing", str(required)))

    index = parse_index(index_path, findings)
    pending = parse_pending_pool(pending_path, findings)
    folders_by_status = list_status_folders(idea_root, findings)

    valid_statuses = {PENDING_STATUS, *STATUS_DIRS.keys()}
    for key, record in index.items():
        if record.status not in valid_statuses:
            findings.append(
                Finding(
                    "WARN",
                    "unknown_status",
                    f"Index entry '{record.title}' has unknown status: {record.status}",
                    record.source,
                )
            )
            continue

        if record.status == PENDING_STATUS:
            if key not in pending:
                findings.append(
                    Finding(
                        "WARN",
                        "pending_missing_from_pool",
                        f"Index marks '{record.title}' as 待评估 but it is not in 待评估点子.md",
                        str(pending_path),
                    )
                )
            continue

        expected_folder = folders_by_status.get(record.status, {})
        if key not in expected_folder:
            findings.append(
                Finding(
                    "ERROR",
                    "indexed_idea_missing_folder",
                    f"Index marks '{record.title}' as {record.status} but no matching folder exists in {STATUS_DIRS[record.status]}",
                    str(idea_root / STATUS_DIRS[record.status]),
                )
            )

    for key, title in pending.items():
        record = index.get(key)
        if record is None:
            findings.append(
                Finding(
                    "ERROR",
                    "pending_not_indexed",
                    f"Pending idea '{title}' is in 待评估点子.md but not registered in 索引.md",
                    str(pending_path),
                )
            )
        elif record.status != PENDING_STATUS:
            findings.append(
                Finding(
                    "WARN",
                    "pending_status_mismatch",
                    f"Pending pool contains '{title}' but index status is {record.status}",
                    str(pending_path),
                )
            )

    for status, folders in folders_by_status.items():
        for key, folder_name in folders.items():
            record = index.get(key)
            if record is None:
                findings.append(
                    Finding(
                        "ERROR",
                        "folder_not_indexed",
                        f"Folder '{folder_name}' exists in {STATUS_DIRS[status]} but is not registered in 索引.md",
                        str(idea_root / STATUS_DIRS[status] / folder_name),
                    )
                )
            elif record.status != status:
                findings.append(
                    Finding(
                        "ERROR",
                        "folder_status_mismatch",
                        f"Folder '{folder_name}' is in {STATUS_DIRS[status]} but index status is {record.status}",
                        str(idea_root / STATUS_DIRS[status] / folder_name),
                    )
                )

    summary = {
        "idea_root": str(idea_root),
        "indexed_ideas": len(index),
        "pending_pool_ideas": len(pending),
        "status_folders": {status: len(folders) for status, folders in folders_by_status.items()},
        "errors": sum(1 for finding in findings if finding.level == "ERROR"),
        "warnings": sum(1 for finding in findings if finding.level == "WARN"),
    }
    return findings, summary


def find_default_root(path: Path) -> Path:
    path = path.resolve()
    if (path / "01-灵感收集").exists():
        return path
    if (path / "IDEA" / "01-灵感收集").exists():
        return path / "IDEA"
    return path


def print_text_report(findings: list[Finding], summary: dict[str, object]) -> None:
    print("IDEA Index Validation")
    print(f"Root: {summary.get('idea_root', 'unknown')}")
    print(
        f"Indexed: {summary.get('indexed_ideas', 0)} | Pending pool: {summary.get('pending_pool_ideas', 0)} | "
        f"Errors: {summary.get('errors', 0)} | Warnings: {summary.get('warnings', 0)}"
    )
    status_folders = summary.get("status_folders", {})
    if isinstance(status_folders, dict):
        print("Folders: " + ", ".join(f"{status}={count}" for status, count in status_folders.items()))
    print()

    if not findings:
        print("OK: index, pending pool, and status folders are consistent.")
        return

    for finding in findings:
        location = f" ({finding.path})" if finding.path else ""
        print(f"[{finding.level}] {finding.code}: {finding.message}{location}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an IDEA folder's index and lifecycle consistency.")
    parser.add_argument("idea_root", nargs="?", default=".", help="Path to IDEA root, or a parent containing IDEA/")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a text report")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    idea_root = find_default_root(Path(args.idea_root))
    findings, summary = validate(idea_root)

    if args.json:
        print(json.dumps({"summary": summary, "findings": [asdict(f) for f in findings]}, ensure_ascii=False, indent=2))
    else:
        print_text_report(findings, summary)

    errors = sum(1 for finding in findings if finding.level == "ERROR")
    warnings = sum(1 for finding in findings if finding.level == "WARN")
    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
