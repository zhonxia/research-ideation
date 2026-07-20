---
name: research-ideation
description: "Generate, screen, evaluate, and manage academic research ideas. Use when brainstorming research directions, evaluating proposals, or auditing an IDEA workspace."
---

# Research Ideation

Manage research ideas as an evidence-backed portfolio. Keep brainstorming cheap, make evaluation progressively stricter, and never equate absence from a local library with a research gap.

## Task Router

| When you want to... | Read this |
|---|---|
| Brainstorm new ideas | `SKILL.md` (this file) |
| Get unstuck or try a new angle | `references/idea-generation-methods.md` |
| Formally evaluate an idea | `references/evaluation-guide.md` |
| Check novelty / differentiation | `references/novelty-protocol.md` |
| Run combination innovation | `references/cross-domain-method-atlas.md` |
| Modify IDs, statuses, or folder layout | `references/data-contract.md` |

## Operating Model

```
Inbox -> deduplicate -> screen -> evaluate -> feasibility probe -> active
                         |             |
                         +-> reject    +-> park / duplicate / supersede / archive
```

- **Canonical registry**: `01-灵感收集/索引.md`
- **Temporary inbox**: `待评估点子.md` — one-line ideas, no formalism
- **Stable ID** (assigned when an idea leaves inbox): `IDEA-YYYY-NNNN`

Canonical statuses:

| Status | Meaning | Artifact location |
|---|---|---|
| `初筛` | Deduplicated, awaiting quick screen | Registry only |
| `评估中` | Evaluation underway | `02-评估中/` |
| `进行中` | Active research | `03-进行中/` |
| `搁置` / `拒绝` / `重复` / `已取代` / `已完成` / `已放弃` | Terminal or parked | `04-已归档/` |

## Package

When distributing as a zip archive, ensure SKILL.md is at the zip root (not nested under a subdirectory). The import tool reads SKILL.md directly from the archive root.

```bash
python scripts/package_skill.py dist/research-ideation.zip
```

## Initialize

```bash
python scripts/init_idea.py /path/to/IDEA
```

It maps each asset to the correct destination and does not overwrite existing files unless `--force` is supplied.

## Generate And Screen Ideas

1. **Default to effect-efficacy** (borrow a mature method, adapt it, compare against baselines). Only switch to problem-existence when the central claim depends on proving that a target limitation actually exists.
2. Write candidates to `待评估点子.md`. No formal requirements — one line is enough.

When presenting generated ideas to the user, **each idea must use this exact format**:

> **1. 解决什么问题：** 一句话点明核心痛点或 Gap。
> **2. 创新切入点：** 一句话说明最独特的抓手是什么。
> **3. 应用价值：** 一句话概括理论或实际意义。

每点控制在 1-2 句话内，不要展开成段落。

3. Deduplicate against the registry (titles, aliases, related IDs).
4. Promote worthwhile candidates to the registry with a stable ID and status `初筛`.
5. Apply the four hard gates (significance, falsifiability, resources, ethics). Reject or park failed candidates with a reason.

If stuck, read `references/idea-generation-methods.md` for alternative approaches.

### Contribution Detail By Stage

| Stage | What to have |
|---|---|
| **Brainstorming / `初筛`** | A sketch covering: (1) **what problem it solves** — the exact limitation or bottleneck in current practice, why it matters, what changes if solved; (2) borrowed capability and why direct transfer may be insufficient; (3) one or two innovation hooks; (4) a minimum probe and stop condition. **No finalized algorithm or proof required.** |
| **`评估中`** | Resolve the sketch into a concrete delta against the closest work and direct transfer, with a defensible mechanism and evaluation design. |
| **`进行中`** | Complete method, theory, measurement design, or artifact needed to support the paper's claims. |

Direct application without an innovation hook fails the screen. Conversely, do not reject a promising early idea because its exact mechanism has not yet been selected.

## Evaluate An Idea

1. Set status to `评估中`. Create `02-评估中/[IDEA-ID] [short-title]/`.
2. Read `references/evaluation-guide.md` — it covers validation route selection, research profiles, the white-paper template, scoring, and story framing.
3. Apply the four hard gates. If a critical gate is `No`, stop; if `Unknown`, define a time-bounded probe.
4. Execute the novelty protocol from `references/novelty-protocol.md` if differentiation matters.
5. Write the white paper using the template in `references/evaluation-guide.md`.
6. Score, update registry, validate workspace.

## Transition Status

1. Update the registry record.
2. Move artifacts to the status directory.
3. Record a decision reason. For `搁置`, add a next review date. For `重复` / `已取代`, add the related idea ID.
4. Run the validator and resolve new errors.

## Validate

```bash
python scripts/validate_idea_index.py /path/to/IDEA
python scripts/validate_idea_index.py /path/to/IDEA --strict --require-ids
```

## Communication Style

When using this skill to interact with the user:

1. **No double quotes.** Do not put words in quotes for emphasis or hedging. Quotes are only for direct citations from papers or sources.
2. **Plain language.** Say things directly. Avoid academic jargon (infrastructure, paradigm, granularity, leverage,赋能), abstract metaphors, and filler phrases ("from a certain perspective", "to some extent", "at the macro level").
3. **Direct conclusions first.** Say what the answer is, then explain why. Do not start with "this needs to be analyzed from multiple angles."
4. **Use Chinese only.** No mixing English terms unless the English word has no common Chinese equivalent (software names, code identifiers).

These rules apply regardless of the topic. Every response should sound like a person explaining something clearly, not a document summarizing itself.

## Non-Negotiable Rules

1. Do not infer global novelty from a local collection.
2. One canonical registry record per idea; one stable ID per promoted idea.
3. Keep inbox entries cheap; do not write a full white paper before screening.
4. Bind every novelty claim to evidence IDs and a documented search scope.
5. Include contrary and overlapping work; negative evidence is still evidence.
6. Apply hard gates before scoring.
7. Keep urgency outside the weighted score; record it as scheduling metadata.
8. Check ethics, privacy, permissions, and dual-use risk where applicable.
9. Compare only compatible score versions and research profiles.
10. Validate after lifecycle, registry, or evidence changes.
11. Match cross-domain methods by problem structure; preserve negative-match history.
12. Keep problem-existence and effect-efficacy validation distinct; default to effect-efficacy.
