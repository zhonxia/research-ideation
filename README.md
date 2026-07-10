# Research Ideation v4

An evidence-backed workflow for generating, screening, evaluating, and managing academic research ideas.

[English](#english) | [中文](#中文)

## English

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
│   └── evidence-log.md
├── 02-评估中/
├── 03-进行中/
├── 04-已归档/
├── 05-文献库/
│   └── _文献模板.md
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

### Run tests

```bash
python -m unittest discover -s tests -v
```

## 中文

### v4 的核心变化

v4 不再让每个灵感直接进入完整白皮书，而是采用逐级增加成本的漏斗：

```text
Inbox → 去重 → 初筛 → 评估 → 最小可否证探针 → 进行中
                    ↘ 拒绝       ↘ 搁置 / 重复 / 已取代 / 归档
```

主要改进：

- 使用稳定点子 ID：`IDEA-YYYY-NNNN`
- 严格区分“本地文献未覆盖”和“经检索支持的研究缺口”
- 评分前先检查问题重要性、可回答性、资源和伦理四项硬门槛
- 使用带置信度与敏感性分析的百分制评分
- 紧迫性只影响排程，不再抬高质量总分
- 支持理论、计算实验、定性、临床/现场、设计/构造研究
- `索引.md` 是唯一生命周期真相源，`待评估点子.md` 只做临时 inbox
- 白皮书引用 claim/evidence ID，不复制证据表
- 初始化器确定性映射文件，校验器兼容旧格式

### 初始化

```bash
python scripts/init_idea.py /path/to/IDEA
```

默认不会覆盖已有文件。需要明确替换模板时才使用 `--force`。

### 校验

```bash
python scripts/validate_idea_index.py /path/to/IDEA
python scripts/validate_idea_index.py /path/to/IDEA --strict --require-ids
```

旧索引仍可读取；旧状态、缺失稳定 ID、标题模糊匹配会给出迁移警告。新建工作区应直接满足 v4 契约。

### 核心原则

1. 本地库缺失只能说明本地覆盖缺口。
2. 点子离开 inbox 时分配稳定 ID，ID 永不复用。
3. 硬门槛通过后再评分。
4. 分数必须包含证据理由和置信度。
5. 只比较相同评分版本和兼容研究类型。
6. 生命周期、证据或文件夹变化后立即校验。

## Repository layout

```text
SKILL.md                    Core workflow and routing
agents/openai.yaml          Codex UI metadata
assets/                     Workspace templates
references/                 Detailed methods and contracts
scripts/init_idea.py        Deterministic initializer
scripts/validate_idea_index.py  Workspace validator
scripts/package_skill.py    Lean release builder
tests/                      Standard-library test suite
```

MIT License.
