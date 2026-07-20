# Research Ideation v4

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![v4](https://img.shields.io/badge/version-v4-brightgreen)]()

🇨🇳 [中文](README.zh.md)

An evidence-backed workflow for generating, screening, evaluating, and managing academic research ideas.

---

### What changed in v4

v4 replaces the single-step brainstorm-and-score workflow with a staged funnel:

```text
Inbox -> deduplicate -> screen -> evaluate -> feasibility probe -> active
                         |             |
                         +-> reject    +-> park / duplicate / supersede / archive
```

Key changes:

- Stable idea IDs: `IDEA-YYYY-NNNN`
- Clear separation between local coverage gaps and validated research gaps
- Hard gates before scoring: significance, answerability, resources, ethics
- Weighted 100-point scoring with confidence and sensitivity analysis
- Urgency as scheduling metadata, not a quality score
- Profiles for theoretical, computational, qualitative, clinical/field, and design research
- Eleven complementary generation methods, including contradiction mapping, counterexample-first, measurement-first, and regime mapping
- A two-route combination workflow: problem-led discovery or method-led effect improvement, both backed by a verified cross-domain method atlas
- A lightweight research idea card before full evaluation
- Four-part novelty-claim decomposition, abstract triage, focused full-text review, and a concrete Delta Statement
- A canonical registry plus a temporary inbox, eliminating duplicate lifecycle truth
- Claim and evidence IDs instead of copied search-log rows
- Deterministic initialization and a legacy-compatible validator

### Install

Use the repository as a skill folder, or build a lean runtime archive:

```bash
python scripts/package_skill.py dist/research-ideation.zip
```

The archive includes only runtime skill files. Repository documentation, tests, Git metadata, and release artifacts are excluded.

### Initialize an IDEA workspace

```bash
python scripts/init_idea.py /path/to/IDEA
```

The initializer creates:

```text
IDEA/
├── 01-灵感收集/
│   ├── 索引.md
│   ├── 想点子指南.md
│   ├── 待评估点子.md
│   ├── _研究点子卡模板.md
│   ├── evidence-log.md
│   └── 问题结构图谱.md
├── 02-评估中/
├── 03-进行中/
├── 04-已归档/
├── 05-文献库/
│   └── _文献模板.md
├── 06-跨领域方法库/
│   ├── 索引.md
│   ├── 扫描记录.md
│   └── 领域/
│       └── _方法卡模板.md
└── README.md
```

Existing files are preserved. Use `--force` only when replacement is intentional.

### Validate

```bash
python scripts/validate_idea_index.py /path/to/IDEA
python scripts/validate_idea_index.py /path/to/IDEA --json
python scripts/validate_idea_index.py /path/to/IDEA --strict --require-ids
python scripts/validate_idea_index.py /path/to/IDEA --verbose
```

The validator checks:

- Stable and duplicate idea IDs
- Canonical and legacy statuses
- Required decision fields and score ranges
- Folder-to-registry consistency
- White-paper `idea_id` frontmatter
- Evidence/claim IDs and unresolved references
- Inbox dispositions that reference unknown ideas

Legacy title-based registries remain readable. Missing stable IDs and old lifecycle labels become warnings unless `--require-ids` or `--strict` raises the migration bar.

### Eleven generation methods

1. Combination innovation
2. Weakness triangulation
3. Method transplantation
4. Theory deep dive
5. Boundary and assumption challenge
6. Citation-chain gap mining
7. Goal-driven reverse engineering
8. Contradiction mapping
9. Counterexample-first research
10. Measurement-first research
11. Regime and phase mapping

Combination innovation supports two primary validation routes:

- **Problem-existence**: show that a target limitation materially affects the system before investing in a remedy.
- **Effect-efficacy**: adapt a mature method to an established target task and test whether it beats a strong native baseline and direct transfer by a meaningful margin at acceptable cost.

The effect-efficacy route requires baselines, ablations, uncertainty analysis, and resource accounting. It does not require inventing or proving a new target-field defect first.

### Run tests

```bash
python -m unittest discover -s tests -v
```

### Core principles

1. A local coverage gap only proves local coverage is incomplete.
2. An idea receives its stable ID when it leaves the inbox; IDs are never reused.
3. Score only after all hard gates are passed.
4. Every score must be accompanied by evidence rationale and confidence level.
5. Compare only ideas scored under the same version and compatible research profiles.
6. Validate immediately after any lifecycle, evidence, or folder change.
7. **Default to the effect-efficacy route.** Most published SCI papers follow the "borrow a mature method, adapt it to the target, compare against baselines" pattern. Only switch to the problem-existence route when the central claim depends on proving that a target limitation actually exists.

### Repository layout

```text
SKILL.md                    Core workflow and routing
agents/openai.yaml          Codex UI metadata
assets/                     Workspace templates
references/                 Detailed methods and contracts
references/cross-domain-method-atlas.md  Combination-search protocol
references/evaluation-guide.md  Route selection, profiles, template, scoring, and framing
scripts/init_idea.py        Deterministic initializer
scripts/validate_idea_index.py  Workspace validator
scripts/package_skill.py    Lean release builder
tests/                      Standard-library test suite
```

MIT License.
