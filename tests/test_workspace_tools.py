from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.init_idea import initialize
from scripts.package_skill import build_archive
from scripts.validate_idea_index import canonical_title, validate


REGISTRY_HEADER = """# 灵感索引

## 点子登记册

| ID | 标题 | 创建时间 | 研究类型 | 标签 | 状态 | 评分 | 置信度 | 下次复查 | 关联/原因 |
|---|---|---|---|---|---|---|:---:|---|---|
"""


EMPTY_EVIDENCE = """# Evidence Log

| Evidence ID | 检索日期 | Idea ID | Claim ID | Query / Source | Channel | Coverage | Filters | Stable IDs / URLs | Key Results | Conclusion | Grade | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|:---:|:---:|---|

| Claim ID | Idea ID | Narrow Claim | Evidence IDs | Gap Level | Allowed Wording | Confidence | Status |
|---|---|---|---|---|---|:---:|---|
"""


class WorkspaceToolsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "IDEA"
        initialize(self.root)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_registry(self, rows: str) -> None:
        (self.root / "01-灵感收集" / "索引.md").write_text(REGISTRY_HEADER + rows, encoding="utf-8")

    def write_evidence(self, text: str = EMPTY_EVIDENCE) -> None:
        (self.root / "01-灵感收集" / "evidence-log.md").write_text(text, encoding="utf-8")

    def codes(self, **kwargs: bool) -> list[str]:
        findings, _ = validate(self.root, **kwargs)
        return [finding.code for finding in findings]

    def test_initializer_maps_assets_and_preserves_existing_files(self) -> None:
        self.assertTrue((self.root / "README.md").is_file())
        self.assertTrue((self.root / "01-灵感收集" / "索引.md").is_file())
        self.assertTrue((self.root / "01-灵感收集" / "_研究点子卡模板.md").is_file())
        self.assertTrue((self.root / "05-文献库" / "_文献模板.md").is_file())
        self.assertTrue((self.root / "01-灵感收集" / "问题结构图谱.md").is_file())
        self.assertTrue((self.root / "06-跨领域方法库" / "索引.md").is_file())
        self.assertTrue((self.root / "06-跨领域方法库" / "扫描记录.md").is_file())
        self.assertTrue((self.root / "06-跨领域方法库" / "领域" / "_方法卡模板.md").is_file())
        self.assertFalse((self.root / "01-灵感收集" / "文献.md").exists())

        registry = self.root / "01-灵感收集" / "索引.md"
        registry.write_text("custom", encoding="utf-8")
        _, skipped = initialize(self.root)
        self.assertIn(registry.resolve(), {Path(path).resolve() for path in skipped})
        self.assertEqual("custom", registry.read_text(encoding="utf-8"))

    def test_empty_initialized_workspace_is_valid(self) -> None:
        findings, summary = validate(self.root, require_ids=True)
        self.assertEqual([], findings)
        self.assertEqual(0, summary["registry_records"])
        self.assertEqual({"problems": 0, "methods": 0, "scans": 0, "matches": 0}, summary["method_atlas"])

    def test_title_normalization_preserves_numeric_terms(self) -> None:
        self.assertEqual(canonical_title("#13 Legacy title"), canonical_title("Legacy title"))
        self.assertEqual("3dbrb", canonical_title("3D-BRB"))

    def test_valid_evaluating_idea_and_evidence(self) -> None:
        self.write_registry(
            "| IDEA-2026-0001 | Verified BRB | 2026-07-10 | theoretical | BRB | 评估中 | v2:80/100 | High | | Gate passed |\n"
        )
        self.write_evidence(
            """# Evidence Log

| Evidence ID | 检索日期 | Idea ID | Claim ID | Query / Source | Channel | Coverage | Filters | Stable IDs / URLs | Key Results | Conclusion | Grade | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|:---:|:---:|---|
| EV-2026-0001 | 2026-07-10 | IDEA-2026-0001 | CLM-IDEA-2026-0001-01 | query | Scholar | exact | English | DOI | adjacent | adjacent | B | 0.80 | none |

| Claim ID | Idea ID | Narrow Claim | Evidence IDs | Gap Level | Allowed Wording | Confidence | Status |
|---|---|---|---|---|---|:---:|---|
| CLM-IDEA-2026-0001-01 | IDEA-2026-0001 | bounded claim | EV-2026-0001 | Search-supported | no exact match in scope | 0.80 | Supported |
"""
        )
        folder = self.root / "02-评估中" / "IDEA-2026-0001 Verified BRB"
        folder.mkdir()
        (folder / "evaluation.md").write_text(
            """---
idea_id: IDEA-2026-0001
status: 评估中
score_version: v2
---

| Dimension | Score (1-5) |
|---|:---:|
| Problem significance | 4.0 |
""",
            encoding="utf-8",
        )

        findings, summary = validate(self.root, require_ids=True)
        self.assertEqual([], findings)
        self.assertEqual(1, summary["evidence_records"])
        self.assertEqual(1, summary["claims"])

    def test_duplicate_id_and_unresolved_evidence_are_errors(self) -> None:
        self.write_registry(
            """| IDEA-2026-0001 | First | 2026-07-10 | theoretical | | 初筛 | | | | |
| IDEA-2026-0001 | Second | 2026-07-10 | theoretical | | 初筛 | | | | |
"""
        )
        self.write_evidence(
            """# Evidence Log

| Evidence ID | 检索日期 | Idea ID | Claim ID | Query / Source | Channel | Coverage | Filters | Stable IDs / URLs | Key Results | Conclusion | Grade | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|:---:|:---:|---|

| Claim ID | Idea ID | Narrow Claim | Evidence IDs | Gap Level | Allowed Wording | Confidence | Status |
|---|---|---|---|---|---|:---:|---|
| CLM-IDEA-2026-0001-01 | IDEA-2026-0001 | claim | EV-2026-9999 | Search-supported | bounded | 0.5 | Draft |
"""
        )
        codes = self.codes(require_ids=True)
        self.assertIn("duplicate_idea_id", codes)
        self.assertIn("unresolved_evidence_reference", codes)

    def test_legacy_registry_is_accepted_with_warnings(self) -> None:
        index = self.root / "01-灵感收集" / "索引.md"
        index.write_text(
            """# Legacy

| # | 标题 | 状态 |
|---|---|---|
| 42 | Legacy Theory | 研究中 |
""",
            encoding="utf-8",
        )
        self.write_evidence()
        folder = self.root / "02-评估中" / "Legacy Theory"
        folder.mkdir()
        (folder / "note.md").write_text("# Legacy", encoding="utf-8")

        findings, _ = validate(self.root)
        self.assertFalse(any(finding.level == "ERROR" for finding in findings))
        self.assertIn("invalid_idea_id", [finding.code for finding in findings])
        self.assertIn("legacy_status", [finding.code for finding in findings])

    def test_conditional_fields_and_score_range(self) -> None:
        self.write_registry(
            """| IDEA-2026-0001 | Parked | 2026-07-10 | theoretical | | 搁置 | v2:120/100 | Low | | reason |
| IDEA-2026-0002 | Duplicate | 2026-07-10 | theoretical | | 重复 | | Low | | no target |
"""
        )
        self.write_evidence()
        codes = self.codes(require_ids=True)
        self.assertIn("missing_next_review", codes)
        self.assertIn("missing_related_id", codes)
        self.assertIn("score_out_of_range", codes)

    def test_runtime_archive_is_lean_and_deterministic(self) -> None:
        first = Path(self.temporary.name) / "first.zip"
        second = Path(self.temporary.name) / "second.zip"
        build_archive(first)
        build_archive(second)
        self.assertEqual(first.read_bytes(), second.read_bytes())
        with zipfile.ZipFile(first) as archive:
            members = set(archive.namelist())
        self.assertIn("research-ideation/SKILL.md", members)
        self.assertIn("research-ideation/agents/openai.yaml", members)
        self.assertIn("research-ideation/scripts/init_idea.py", members)
        self.assertNotIn("research-ideation/README.md", members)
        self.assertFalse(any(name.startswith("research-ideation/tests/") for name in members))

    def test_generation_method_catalog_is_consistent(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        methods = (skill_root / "references" / "idea-generation-methods.md").read_text(encoding="utf-8")
        guide = (skill_root / "assets" / "想点子指南.md").read_text(encoding="utf-8")
        inbox = (skill_root / "assets" / "待评估点子.md").read_text(encoding="utf-8")
        readme = (skill_root / "README.md").read_text(encoding="utf-8")

        self.assertIn("eleven methods", methods)
        for number in range(1, 12):
            self.assertIn(f"## {number}.", methods)
        self.assertIn("十一种生成方法", guide)
        self.assertIn("1-11 / 用户输入", inbox)
        self.assertIn("### Eleven generation methods", readme)
        self.assertIn("cross-domain-method-atlas.md", methods)

    def test_valid_cross_domain_match(self) -> None:
        problem_path = self.root / "01-灵感收集" / "问题结构图谱.md"
        problem_path.write_text(
            """# Problems

| Problem ID | 问题标题 | 状态 |
|---|---|---|
| PROB-BRB-001 | Dependent evidence | Verified |
""",
            encoding="utf-8",
        )
        atlas = self.root / "06-跨领域方法库"
        (atlas / "索引.md").write_text(
            """# Methods

| Method ID | 方法名 | 核心假设 | 成熟度证据 | 失败边界 | 状态 |
|---|---|---|---|---|---|
| METHOD-STAT-001 | Robust estimator | bounded contamination | review and independent use | high contamination | Verified |
""",
            encoding="utf-8",
        )
        (atlas / "扫描记录.md").write_text(
            """# Scans

| Scan ID | 目标 Problem IDs | 新增 Method IDs |
|---|---|---|
| SCAN-2026-0001 | PROB-BRB-001 | METHOD-STAT-001 |

| Match ID | Problem ID | Method ID | Bridge Statement | 结果 | Idea ID | 原因/下一步 |
|---|---|---|---|---|---|---|
| MATCH-2026-0001 | PROB-BRB-001 | METHOD-STAT-001 | P has S; M solves S under A; adapt C and compare N | Promising | | run transfer validation |
""",
            encoding="utf-8",
        )

        findings, summary = validate(self.root, require_ids=True)
        self.assertEqual([], findings)
        self.assertEqual({"problems": 1, "methods": 1, "scans": 1, "matches": 1}, summary["method_atlas"])

    def test_invalid_cross_domain_match_is_reported(self) -> None:
        problem_path = self.root / "01-灵感收集" / "问题结构图谱.md"
        problem_path.write_text(
            """# Problems

| Problem ID | 问题标题 |
|---|---|
| PROB-BRB-001 | Known problem |
""",
            encoding="utf-8",
        )
        atlas = self.root / "06-跨领域方法库"
        (atlas / "索引.md").write_text(
            """# Methods

| Method ID | 方法名 | 状态 |
|---|---|---|
| METHOD-STAT-001 | Known method | Candidate |
""",
            encoding="utf-8",
        )
        (atlas / "扫描记录.md").write_text(
            """# Matches

| Match ID | Problem ID | Method ID | Bridge Statement | 结果 | Idea ID | 原因/下一步 |
|---|---|---|---|---|---|---|
| MATCH-2026-0001 | PROB-BRB-999 | METHOD-STAT-999 | | Negative | | |
""",
            encoding="utf-8",
        )

        codes = self.codes(require_ids=True)
        self.assertIn("match_unknown_problem", codes)
        self.assertIn("match_unknown_method", codes)
        self.assertIn("negative_match_without_reason", codes)


if __name__ == "__main__":
    unittest.main()
