# IDEA Data Contract v4

Use this contract for new records. The validator accepts legacy records but reports migration warnings.

## Stable Identifiers

| Entity | Format | Example |
|---|---|---|
| Idea | `IDEA-YYYY-NNNN` | `IDEA-2026-0106` |
| Evidence | `EV-YYYY-NNNN` | `EV-2026-0042` |
| Claim | `CLM-IDEA-YYYY-NNNN-NN` | `CLM-IDEA-2026-0106-01` |
| Paper note | DOI when available; otherwise `PAPER-YYYY-NNNN` | `10.1000/example` |
| Target problem | `PROB-TARGET-NNN` | `PROB-BRB-001` |
| Mature method | `METHOD-DOMAIN-NNN` | `METHOD-CTRL-001` |
| Domain scan | `SCAN-YYYY-NNNN` | `SCAN-2026-0001` |
| Method match | `MATCH-YYYY-NNNN` | `MATCH-2026-0001` |

Never recycle an ID. Titles and folder names may change; IDs must not.

## Canonical Registry

`01-灵感收集/索引.md` is the single source of truth for idea identity and lifecycle. Its canonical table must contain:

| Column | Required | Rule |
|---|:---:|---|
| ID | Yes | Unique stable idea ID |
| 标题 | Yes | Current human-readable title |
| 创建时间 | Yes | `YYYY-MM-DD` |
| 研究类型 | Yes | One research profile |
| 标签 | No | Comma-separated discovery labels |
| 状态 | Yes | One canonical status |
| 评分 | No | `v2:XX.X/100` or legacy notation |
| 置信度 | No | Low/Medium/High |
| 下次复查 | Conditional | Required for `搁置` |
| 关联/原因 | Conditional | Decision reason; target ID for `重复`/`已取代` |

The inbox is not a second registry. Remove a promoted row or set its disposition to the assigned idea ID.

## Research Idea Card

Use `01-灵感收集/_研究点子卡模板.md` for a promoted idea that is being considered for formal evaluation. The card is a lightweight decision artifact, not a second registry and not a replacement for the evaluation white paper.

- The registry remains the source of truth for ID and status.
- The card must split the innovation claim into problem framing, core mechanism, key insight, and application domain.
- The card must name the primary validation route. Combination ideas use `problem-existence` or `effect-efficacy`; other idea types may use `other` with an explicit claim-aligned probe.
- An effect-efficacy card must name a strong native baseline, direct-transfer control, adapted method, primary outcome, minimum meaningful improvement, ablations, uncertainty protocol, and resource costs.
- Record assumptions and operating conditions separately.
- Write a Delta Statement only after naming the closest verified work; use `待检索` before that evidence exists.
- Require the card before substantial evaluation work, not for every raw inbox entry.

## Cross-Domain Atlas Ownership

- `01-灵感收集/问题结构图谱.md` owns target problem identities and structural descriptions.
- `06-跨领域方法库/索引.md` owns domain coverage and method identities.
- `06-跨领域方法库/领域/*.md` owns full method cards.
- `06-跨领域方法库/扫描记录.md` owns scan sessions and all match outcomes, including negative matches.
- A promising match is not an idea until Method 3 validates the transfer and the pair is promoted through the inbox.

## Statuses And Locations

| Status | New records allowed? | Folder expectation |
|---|:---:|---|
| 初筛 | Yes | No folder required |
| 评估中 | Yes | Folder in `02-评估中/` |
| 进行中 | Yes | Folder in `03-进行中/` |
| 搁置 | Yes | `04-已归档/` if artifacts exist |
| 拒绝 | Yes | `04-已归档/` if artifacts exist |
| 重复 | Yes | Target idea ID required |
| 已取代 | Yes | Target idea ID required |
| 已完成 | Yes | Folder in `04-已归档/` |
| 已放弃 | Yes | Folder in `04-已归档/` if work began |
| 收集 | Legacy only | Keep raw candidates in the inbox; migrate promoted records to `初筛` |
| 待评估 | Legacy only | No folder required |
| 研究中 | Legacy only | Treat as `评估中` |
| 已归档 | Legacy only | Preserve until the terminal reason is known |

For new artifact folders, prefer `[IDEA-ID] [short-title]`. Preserve legacy folder names unless a migration is explicitly requested.

## Evidence Ownership

`evidence-log.md` owns evidence rows and claim-to-evidence links. White papers reference evidence IDs; they do not copy rows. A claim may cite many evidence rows, and an evidence row may support or contradict many claims.

## Comparison Rules

- Compare scores only under the same score version.
- Compare research profiles only when the dimensions have equivalent interpretations.
- Preserve legacy scores as labeled historical values; do not silently convert 30-point totals to v2.
