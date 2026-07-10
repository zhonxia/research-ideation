#!/usr/bin/env python3
"""Validate a research-ideation IDEA workspace.

The v4 contract uses stable IDs while this validator remains read-compatible
with legacy title-based registries and lifecycle labels.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote


IDEA_ID_RE = re.compile(r"^IDEA-\d{4}-\d{4}$", re.IGNORECASE)
EVIDENCE_ID_RE = re.compile(r"^EV-\d{4}-\d{4}$", re.IGNORECASE)
CLAIM_ID_RE = re.compile(r"^CLM-IDEA-\d{4}-\d{4}-\d{2}$", re.IGNORECASE)
IDEA_ID_SEARCH_RE = re.compile(r"IDEA-\d{4}-\d{4}", re.IGNORECASE)
EVIDENCE_ID_SEARCH_RE = re.compile(r"EV-\d{4}-\d{4}", re.IGNORECASE)
PLACEHOLDER_MARKERS = ("YYYY", "[", "示例", "example")

CANONICAL_STATUSES = {
    "初筛",
    "评估中",
    "进行中",
    "搁置",
    "拒绝",
    "重复",
    "已取代",
    "已完成",
    "已放弃",
}
LEGACY_STATUSES = {"收集", "待评估", "研究中", "已归档"}
STATUS_ALIASES = {
    "pending": "待评估",
    "todo": "待评估",
    "screening": "初筛",
    "under evaluation": "评估中",
    "evaluating": "评估中",
    "researching": "研究中",
    "active": "进行中",
    "in progress": "进行中",
    "parked": "搁置",
    "rejected": "拒绝",
    "duplicate": "重复",
    "superseded": "已取代",
    "completed": "已完成",
    "done": "已完成",
    "abandoned": "已放弃",
    "archived": "已归档",
}

STATUS_DIRECTORY = {
    "评估中": "02-评估中",
    "研究中": "02-评估中",
    "进行中": "03-进行中",
    "已完成": "04-已归档",
    "已归档": "04-已归档",
}
DIRECTORY_STATUS = {
    "02-评估中": {"评估中", "研究中"},
    "03-进行中": {"进行中"},
    "04-已归档": {"搁置", "拒绝", "重复", "已取代", "已完成", "已放弃", "已归档"},
}


@dataclass
class Finding:
    level: str
    code: str
    message: str
    path: str | None = None


@dataclass
class IdeaRecord:
    idea_id: str | None
    raw_id: str
    title: str
    status: str
    next_review: str
    relation: str
    score: str
    artifact_hint: str
    source: str

    @property
    def key(self) -> str:
        return (self.idea_id or canonical_title(self.title)).casefold()


def strip_markdown(value: str) -> str:
    value = value.strip()
    value = re.sub(r"~~(.*?)~~", r"\1", value)
    value = re.sub(r"`([^`]*)`", r"\1", value)
    value = re.sub(r"\*\*([^*]*)\*\*", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")
    return re.sub(r"\s+", " ", value).strip()


def canonical_title(value: str) -> str:
    value = strip_markdown(value)
    value = re.sub(r"^IDEA-\d{4}-\d{4}\s*", "", value, flags=re.IGNORECASE)
    value = re.sub(r"^(?:#?\d+(?:[.)、]|\s)\s*|[-*]\s+)", "", value)
    value = re.sub(r"[\s_+＋:：()（）\[\]【】\-]+", "", value)
    return value.casefold()


def canonical_status(value: str) -> str:
    value = strip_markdown(value)
    for status in sorted(CANONICAL_STATUSES | LEGACY_STATUSES, key=len, reverse=True):
        if status in value:
            return status
    return STATUS_ALIASES.get(value.casefold(), value)


def extract_artifact_hint(value: str) -> str:
    match = re.search(r"\[[^\]]+\]\(([^)]+)\)", value)
    if not match:
        return ""
    parts = [unquote(part) for part in match.group(1).split("/") if part not in {"", ".", ".."}]
    for dirname in DIRECTORY_STATUS:
        if dirname in parts:
            index = parts.index(dirname)
            if index + 1 < len(parts):
                return parts[index + 1]
    return ""


def split_markdown_row(line: str) -> list[str]:
    line = line.strip()
    if not line.startswith("|") or not line.endswith("|"):
        return []
    return [cell.strip() for cell in line.strip("|").split("|")]


def is_separator_row(cells: Iterable[str]) -> bool:
    values = list(cells)
    return bool(values) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in values)


def iter_markdown_tables(text: str) -> Iterable[tuple[list[str], list[list[str]]]]:
    lines = text.splitlines()
    index = 0
    while index < len(lines) - 1:
        header = split_markdown_row(lines[index])
        separator = split_markdown_row(lines[index + 1])
        if header and len(header) == len(separator) and is_separator_row(separator):
            rows: list[list[str]] = []
            index += 2
            while index < len(lines):
                row = split_markdown_row(lines[index])
                if not row:
                    break
                row.extend([""] * (len(header) - len(row)))
                rows.append(row[: len(header)])
                index += 1
            yield header, rows
        else:
            index += 1


def find_column(headers: list[str], candidates: list[str]) -> int | None:
    normalized = [strip_markdown(header).casefold() for header in headers]
    for candidate in candidates:
        for index, header in enumerate(normalized):
            if candidate.casefold() == header:
                return index
    return None


def read_text(path: Path, findings: list[Finding], *, required: bool = True) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        if required:
            findings.append(Finding("ERROR", "missing_file", "Required file is missing", str(path)))
    except UnicodeDecodeError:
        findings.append(Finding("ERROR", "decode_error", "File is not valid UTF-8", str(path)))
    return ""


def is_placeholder(value: str) -> bool:
    lowered = value.casefold()
    return not value or any(marker.casefold() in lowered for marker in PLACEHOLDER_MARKERS)


def parse_registry(path: Path, findings: list[Finding], require_ids: bool) -> list[IdeaRecord]:
    text = read_text(path, findings)
    records: list[IdeaRecord] = []
    table_found = False

    for headers, rows in iter_markdown_tables(text):
        title_column = find_column(headers, ["标题", "点子", "title", "idea"])
        status_column = find_column(headers, ["状态", "status"])
        if title_column is None or status_column is None:
            continue
        table_found = True
        id_column = find_column(headers, ["id", "idea id", "idea_id", "#"])
        review_column = find_column(headers, ["下次复查", "next review"])
        relation_column = find_column(headers, ["关联/原因", "关联", "原因", "relation", "reason"])
        score_column = find_column(headers, ["评分", "score"])

        for row in rows:
            raw_title = row[title_column]
            title = strip_markdown(raw_title)
            if is_placeholder(title):
                continue
            raw_id = strip_markdown(row[id_column]) if id_column is not None else ""
            idea_id = raw_id.upper() if IDEA_ID_RE.fullmatch(raw_id) else None
            status = canonical_status(row[status_column])
            record = IdeaRecord(
                idea_id=idea_id,
                raw_id=raw_id,
                title=title,
                status=status,
                next_review=strip_markdown(row[review_column]) if review_column is not None else "",
                relation=strip_markdown(row[relation_column]) if relation_column is not None else "",
                score=strip_markdown(row[score_column]) if score_column is not None else "",
                artifact_hint=extract_artifact_hint(raw_title),
                source=str(path),
            )
            records.append(record)

            if not idea_id:
                level = "ERROR" if require_ids else "WARN"
                code = "invalid_idea_id" if raw_id else "missing_idea_id"
                findings.append(Finding(level, code, f"Idea '{title}' lacks a valid IDEA-YYYY-NNNN ID", str(path)))
            if status in LEGACY_STATUSES:
                findings.append(Finding("WARN", "legacy_status", f"Idea '{title}' uses legacy status: {status}", str(path)))
            elif status not in CANONICAL_STATUSES:
                findings.append(Finding("ERROR", "unknown_status", f"Idea '{title}' has unknown status: {status}", str(path)))
            if status == "搁置" and not record.next_review:
                findings.append(Finding("ERROR", "missing_next_review", f"Parked idea '{title}' needs a next review date", str(path)))
            if status in {"重复", "已取代"} and not IDEA_ID_SEARCH_RE.search(record.relation):
                findings.append(Finding("ERROR", "missing_related_id", f"Idea '{title}' with status {status} needs a related idea ID", str(path)))
            validate_score(record, findings)

    if not table_found:
        findings.append(Finding("ERROR", "registry_table_not_found", "No registry table with title and status columns was found", str(path)))

    detect_registry_duplicates(records, findings, path)
    return records


def validate_score(record: IdeaRecord, findings: list[Finding]) -> None:
    if not record.score:
        return
    v2 = re.search(r"v2\s*:\s*(\d+(?:\.\d+)?)\s*/\s*100", record.score, re.IGNORECASE)
    legacy = re.search(r"(\d+(?:\.\d+)?)\s*/\s*30", record.score)
    if v2 and not 0 <= float(v2.group(1)) <= 100:
        findings.append(Finding("ERROR", "score_out_of_range", f"Idea '{record.title}' has an invalid v2 score", record.source))
    elif legacy and not 0 <= float(legacy.group(1)) <= 30:
        findings.append(Finding("ERROR", "score_out_of_range", f"Idea '{record.title}' has an invalid legacy score", record.source))
    elif not v2 and not legacy:
        findings.append(Finding("WARN", "unversioned_score", f"Idea '{record.title}' has an unrecognized or unversioned score: {record.score}", record.source))


def detect_registry_duplicates(records: list[IdeaRecord], findings: list[Finding], path: Path) -> None:
    ids: dict[str, str] = {}
    raw_ids: dict[str, str] = {}
    titles: dict[str, str] = {}
    for record in records:
        if record.idea_id:
            if record.idea_id in ids:
                findings.append(Finding("ERROR", "duplicate_idea_id", f"Duplicate idea ID {record.idea_id}: '{ids[record.idea_id]}' and '{record.title}'", str(path)))
            ids[record.idea_id] = record.title
        elif record.raw_id:
            raw_key = record.raw_id.casefold()
            if raw_key in raw_ids:
                findings.append(Finding("WARN", "duplicate_legacy_id", f"Duplicate legacy ID {record.raw_id}: '{raw_ids[raw_key]}' and '{record.title}'", str(path)))
            raw_ids[raw_key] = record.title

        title_key = canonical_title(record.title)
        if title_key in titles:
            findings.append(Finding("ERROR", "duplicate_title", f"Duplicate canonical title: '{titles[title_key]}' and '{record.title}'", str(path)))
        titles[title_key] = record.title


def registry_maps(
    records: list[IdeaRecord],
) -> tuple[dict[str, IdeaRecord], dict[str, list[IdeaRecord]], dict[str, list[IdeaRecord]]]:
    by_id = {record.idea_id: record for record in records if record.idea_id}
    by_title: dict[str, list[IdeaRecord]] = {}
    by_hint: dict[str, list[IdeaRecord]] = {}
    for record in records:
        by_title.setdefault(canonical_title(record.title), []).append(record)
        if record.artifact_hint:
            by_hint.setdefault(canonical_title(record.artifact_hint), []).append(record)
    return by_id, by_title, by_hint


def parse_folder_identity(name: str) -> tuple[str | None, str]:
    match = re.search(r"IDEA-\d{4}-\d{4}", name, re.IGNORECASE)
    idea_id = match.group(0).upper() if match else None
    return idea_id, canonical_title(name)


def match_folder(
    name: str,
    by_id: dict[str, IdeaRecord],
    by_title: dict[str, list[IdeaRecord]],
    by_hint: dict[str, list[IdeaRecord]],
) -> tuple[IdeaRecord | None, bool]:
    folder_id, folder_title = parse_folder_identity(name)
    if folder_id:
        return by_id.get(folder_id), False
    hinted = by_hint.get(folder_title, [])
    if len(hinted) == 1:
        return hinted[0], False
    exact = by_title.get(folder_title, [])
    if len(exact) == 1:
        return exact[0], False
    fuzzy = [record for key, values in by_title.items() if key and (key in folder_title or folder_title in key) for record in values]
    unique = {record.key: record for record in fuzzy}
    if len(unique) == 1:
        return next(iter(unique.values())), True
    return None, bool(unique)


def validate_folders(root: Path, records: list[IdeaRecord], findings: list[Finding]) -> dict[str, int]:
    by_id, by_title, by_hint = registry_maps(records)
    counts: dict[str, int] = {}
    matched_keys: set[str] = set()
    matched_raw_ids: set[str] = set()
    all_folder_titles: set[str] = set()

    for dirname, allowed_statuses in DIRECTORY_STATUS.items():
        directory = root / dirname
        if not directory.is_dir():
            findings.append(Finding("ERROR", "missing_dir", "Required status directory is missing", str(directory)))
            counts[dirname] = 0
            continue
        folders = [child for child in directory.iterdir() if child.is_dir() and not child.name.startswith(".")]
        counts[dirname] = len(folders)
        for folder in folders:
            all_folder_titles.add(canonical_title(folder.name))
            record, fuzzy = match_folder(folder.name, by_id, by_title, by_hint)
            if record is None:
                code = "ambiguous_folder_match" if fuzzy else "folder_not_registered"
                findings.append(Finding("ERROR", code, f"Folder '{folder.name}' cannot be matched to one registry record", str(folder)))
                continue
            matched_keys.add(record.key)
            if record.raw_id:
                matched_raw_ids.add(record.raw_id.casefold())
            if fuzzy:
                findings.append(Finding("WARN", "legacy_title_match", f"Folder '{folder.name}' matched '{record.title}' by a legacy fuzzy title", str(folder)))
            if record.status not in allowed_statuses:
                findings.append(Finding("ERROR", "folder_status_mismatch", f"Folder '{folder.name}' is in {dirname}, but registry status is {record.status}", str(folder)))
            validate_artifact_folder(folder, record, by_id, findings)

    for record in records:
        required_directory = STATUS_DIRECTORY.get(record.status)
        legacy_id_matched = bool(record.raw_id and record.raw_id.casefold() in matched_raw_ids)
        hint_matched = bool(record.artifact_hint and canonical_title(record.artifact_hint) in all_folder_titles)
        if required_directory and record.key not in matched_keys and not legacy_id_matched and not hint_matched:
            findings.append(Finding("ERROR", "required_folder_missing", f"Idea '{record.title}' with status {record.status} has no folder in {required_directory}", str(root / required_directory)))
    return counts


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"\'')
    return values


def validate_artifact_folder(folder: Path, record: IdeaRecord, by_id: dict[str, IdeaRecord], findings: list[Finding]) -> None:
    markdown_files = [path for path in folder.rglob("*.md") if path.is_file()]
    if not markdown_files:
        findings.append(Finding("WARN", "artifact_folder_empty", "Artifact folder contains no Markdown document", str(folder)))
        return
    frontmatter_seen = False
    for path in markdown_files:
        text = read_text(path, findings, required=False)
        metadata = parse_frontmatter(text)
        if not metadata:
            continue
        frontmatter_seen = True
        document_id = metadata.get("idea_id", "").upper()
        if document_id and not IDEA_ID_RE.fullmatch(document_id):
            findings.append(Finding("ERROR", "invalid_document_idea_id", f"Invalid idea_id in {path.name}: {document_id}", str(path)))
        elif document_id and document_id not in by_id:
            findings.append(Finding("ERROR", "document_idea_not_registered", f"Document references unregistered idea ID: {document_id}", str(path)))
        elif document_id and record.idea_id and document_id != record.idea_id:
            findings.append(Finding("ERROR", "document_folder_id_mismatch", f"Document idea_id {document_id} does not match folder record {record.idea_id}", str(path)))
        validate_score_table(text, path, findings)
    if record.idea_id and not frontmatter_seen:
        findings.append(Finding("WARN", "missing_artifact_frontmatter", f"No Markdown artifact declares idea_id for {record.idea_id}", str(folder)))


def validate_score_table(text: str, path: Path, findings: list[Finding]) -> None:
    for headers, rows in iter_markdown_tables(text):
        dimension_column = find_column(headers, ["dimension", "维度"])
        score_column = find_column(headers, ["score (1-5)", "score", "评分"])
        if dimension_column is None or score_column is None:
            continue
        for row in rows:
            dimension = strip_markdown(row[dimension_column])
            score = strip_markdown(row[score_column])
            if is_placeholder(score):
                continue
            try:
                number = float(score)
            except ValueError:
                findings.append(Finding("WARN", "non_numeric_dimension_score", f"Non-numeric score for '{dimension}': {score}", str(path)))
                continue
            if number < 1 or number > 5 or number * 2 != round(number * 2):
                findings.append(Finding("ERROR", "dimension_score_out_of_range", f"Score for '{dimension}' must be 1-5 in 0.5 increments", str(path)))


def validate_inbox(path: Path, registered_ids: set[str], findings: list[Finding]) -> int:
    text = read_text(path, findings)
    count = 0
    for headers, rows in iter_markdown_tables(text):
        idea_column = find_column(headers, ["原始点子", "点子", "idea", "title"])
        if idea_column is None:
            continue
        disposition_column = find_column(headers, ["处置 / idea id", "处置", "disposition", "idea id"])
        for row in rows:
            idea = strip_markdown(row[idea_column])
            if is_placeholder(idea):
                continue
            count += 1
            if disposition_column is None:
                continue
            disposition = strip_markdown(row[disposition_column])
            match = IDEA_ID_RE.search(disposition)
            if match and match.group(0).upper() not in registered_ids:
                findings.append(Finding("ERROR", "inbox_unknown_idea_id", f"Inbox row '{idea}' references an unregistered idea ID", str(path)))
    return count


def split_ids(value: str, pattern: re.Pattern[str]) -> list[str]:
    return [match.group(0).upper() for match in pattern.finditer(value)]


def validate_evidence(
    path: Path,
    records: list[IdeaRecord],
    findings: list[Finding],
    *,
    require_ids: bool,
) -> tuple[int, int]:
    text = read_text(path, findings)
    evidence: dict[str, str] = {}
    claims: dict[str, tuple[str, list[str]]] = {}
    by_id, by_title, _ = registry_maps(records)

    def resolve_idea(value: str) -> str | None:
        normalized = strip_markdown(value)
        if normalized.upper() in by_id:
            return normalized.upper()
        title_matches = by_title.get(canonical_title(normalized), [])
        if len(title_matches) == 1:
            return title_matches[0].key
        return None

    for headers, rows in iter_markdown_tables(text):
        evidence_column = find_column(headers, ["evidence id", "证据 id"])
        claim_column = find_column(headers, ["claim id", "声明 id"])
        idea_column = find_column(headers, ["idea id", "点子 id"])
        evidence_refs_column = find_column(headers, ["evidence ids", "证据 ids"])

        if evidence_column is not None and idea_column is not None:
            for row in rows:
                evidence_id = strip_markdown(row[evidence_column]).upper()
                idea_id = strip_markdown(row[idea_column]).upper()
                if is_placeholder(evidence_id):
                    continue
                if not EVIDENCE_ID_RE.fullmatch(evidence_id):
                    level = "ERROR" if require_ids else "WARN"
                    findings.append(Finding(level, "legacy_evidence_id", f"Evidence ID is not EV-YYYY-NNNN: {evidence_id}", str(path)))
                if evidence_id in evidence:
                    findings.append(Finding("ERROR", "duplicate_evidence_id", f"Duplicate evidence ID: {evidence_id}", str(path)))
                resolved_idea = resolve_idea(idea_id)
                evidence[evidence_id] = resolved_idea or idea_id
                if resolved_idea is None:
                    findings.append(Finding("ERROR", "evidence_unknown_idea_id", f"Evidence {evidence_id} references unregistered idea {idea_id}", str(path)))

        if claim_column is not None and idea_column is not None and evidence_refs_column is not None:
            for row in rows:
                claim_id = strip_markdown(row[claim_column]).upper()
                idea_id = strip_markdown(row[idea_column]).upper()
                if is_placeholder(claim_id):
                    continue
                if not CLAIM_ID_RE.fullmatch(claim_id):
                    level = "ERROR" if require_ids else "WARN"
                    findings.append(Finding(level, "legacy_claim_id", f"Claim ID is not CLM-IDEA-YYYY-NNNN-NN: {claim_id}", str(path)))
                if claim_id in claims:
                    findings.append(Finding("ERROR", "duplicate_claim_id", f"Duplicate claim ID: {claim_id}", str(path)))
                resolved_idea = resolve_idea(idea_id)
                reference_value = row[evidence_refs_column]
                evidence_ids = split_ids(reference_value, EVIDENCE_ID_SEARCH_RE)
                if not evidence_ids and not require_ids:
                    evidence_ids = [item.strip().upper() for item in re.split(r"[,，\s]+", strip_markdown(reference_value)) if item.strip()]
                claims[claim_id] = (resolved_idea or idea_id, evidence_ids)
                if resolved_idea is None:
                    findings.append(Finding("ERROR", "claim_unknown_idea_id", f"Claim {claim_id} references unregistered idea {idea_id}", str(path)))

    for claim_id, (idea_id, evidence_ids) in claims.items():
        if not evidence_ids:
            findings.append(Finding("ERROR", "claim_without_evidence", f"Claim {claim_id} has no evidence IDs", str(path)))
        for evidence_id in evidence_ids:
            if evidence_id not in evidence:
                findings.append(Finding("ERROR", "unresolved_evidence_reference", f"Claim {claim_id} references missing evidence {evidence_id}", str(path)))
            elif evidence[evidence_id] != idea_id:
                findings.append(Finding("ERROR", "cross_idea_evidence_reference", f"Claim {claim_id} references evidence owned by {evidence[evidence_id]}", str(path)))
    return len(evidence), len(claims)


def validate(root: Path, *, require_ids: bool = False) -> tuple[list[Finding], dict[str, object]]:
    findings: list[Finding] = []
    root = root.expanduser().resolve()
    if not root.exists():
        return [Finding("ERROR", "missing_root", "IDEA root does not exist", str(root))], {}
    if not root.is_dir():
        return [Finding("ERROR", "root_not_directory", "IDEA root is not a directory", str(root))], {}

    required_directories = ["01-灵感收集", "02-评估中", "03-进行中", "04-已归档", "05-文献库"]
    for dirname in required_directories:
        if not (root / dirname).is_dir():
            findings.append(Finding("ERROR", "missing_dir", "Required directory is missing", str(root / dirname)))

    collection = root / "01-灵感收集"
    registry_path = collection / "索引.md"
    records = parse_registry(registry_path, findings, require_ids)
    registered_ids = {record.idea_id for record in records if record.idea_id}
    inbox_count = validate_inbox(collection / "待评估点子.md", registered_ids, findings)
    evidence_count, claim_count = validate_evidence(
        collection / "evidence-log.md", records, findings, require_ids=require_ids
    )
    folder_counts = validate_folders(root, records, findings)

    summary = {
        "idea_root": str(root),
        "registry_records": len(records),
        "records_with_stable_ids": len(registered_ids),
        "inbox_rows": inbox_count,
        "evidence_records": evidence_count,
        "claims": claim_count,
        "status_folders": folder_counts,
        "errors": sum(finding.level == "ERROR" for finding in findings),
        "warnings": sum(finding.level == "WARN" for finding in findings),
    }
    return findings, summary


def find_default_root(path: Path) -> Path:
    path = path.expanduser().resolve()
    if (path / "01-灵感收集").exists():
        return path
    if (path / "IDEA" / "01-灵感收集").exists():
        return path / "IDEA"
    return path


def print_report(findings: list[Finding], summary: dict[str, object], *, verbose: bool = False) -> None:
    print("IDEA Workspace Validation v4")
    print(f"Root: {summary.get('idea_root', 'unknown')}")
    print(
        "Registry: {registry_records} ({records_with_stable_ids} stable IDs) | Inbox: {inbox_rows} | "
        "Evidence: {evidence_records} | Claims: {claims} | Errors: {errors} | Warnings: {warnings}".format(
            **{key: summary.get(key, 0) for key in (
                "registry_records", "records_with_stable_ids", "inbox_rows", "evidence_records", "claims", "errors", "warnings"
            )}
        )
    )
    if not findings:
        print("OK: workspace conforms to the v4 contract.")
        return
    migration_codes = {"missing_idea_id", "invalid_idea_id", "legacy_status"}
    visible = findings if verbose else [
        finding for finding in findings if finding.level == "ERROR" or finding.code not in migration_codes
    ]
    for finding in visible:
        location = f" ({finding.path})" if finding.path else ""
        print(f"[{finding.level}] {finding.code}: {finding.message}{location}")
    if not verbose:
        for code in sorted(migration_codes):
            count = sum(finding.code == code for finding in findings)
            if count:
                print(f"[WARN] {code}: {count} migration finding(s); use --verbose or --json for details")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a research-ideation IDEA workspace.")
    parser.add_argument("idea_root", nargs="?", default=".", help="IDEA root or parent containing IDEA/")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    parser.add_argument("--require-ids", action="store_true", help="Treat missing or legacy idea IDs as errors")
    parser.add_argument("--verbose", action="store_true", help="Print every migration warning")
    args = parser.parse_args()

    findings, summary = validate(find_default_root(Path(args.idea_root)), require_ids=args.require_ids)
    if args.json:
        print(json.dumps({"summary": summary, "findings": [asdict(item) for item in findings]}, ensure_ascii=False, indent=2))
    else:
        print_report(findings, summary, verbose=args.verbose)
    errors = sum(item.level == "ERROR" for item in findings)
    warnings = sum(item.level == "WARN" for item in findings)
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
