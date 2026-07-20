---
name: research-ideation
description: "Generate, screen, evaluate, compare, and manage academic research ideas with a staged funnel, stable idea IDs, literature-backed novelty claims, research-type profiles, and lifecycle validation. Use when brainstorming research directions, checking whether an idea is differentiated, prioritizing proposals, writing an idea evaluation, synchronizing a literature map, or auditing an IDEA workspace."
---

# Research Ideation

Manage research ideas as an evidence-backed portfolio. Keep brainstorming cheap, make evaluation progressively stricter, and never equate absence from a local library with a research gap.

## Operating Model

Use this funnel:

```text
Inbox -> deduplicate -> screen -> evaluate -> feasibility probe -> active
                         |             |
                         +-> reject    +-> park / duplicate / supersede / archive
```

Treat `01-灵感收集/索引.md` as the canonical registry. Treat `待评估点子.md` only as a temporary inbox. Assign a stable ID when an idea leaves the inbox:

```text
IDEA-YYYY-NNNN
```

Use these canonical statuses:

| Status | Meaning | Artifact location |
|---|---|---|
| `初筛` | Deduplicated and awaiting a quick screen | Registry only |
| `评估中` | Literature or feasibility evaluation is underway | `02-评估中/` |
| `进行中` | Selected as active research | `03-进行中/` |
| `搁置` | Plausible, but deferred with a review date | `04-已归档/` if artifacts exist |
| `拒绝` | Failed a gate or has poor expected value | `04-已归档/` if artifacts exist |
| `重复` | Duplicates another idea; record the target ID | `04-已归档/` if artifacts exist |
| `已取代` | Replaced by a stronger idea; record the target ID | `04-已归档/` |
| `已完成` | Research was completed | `04-已归档/` |
| `已放弃` | Work started but was stopped | `04-已归档/` |

Accept legacy `收集`, `待评估`, `研究中`, and `已归档` records when auditing existing workspaces. Do not create new records with those statuses.

Read [references/data-contract.md](references/data-contract.md) before changing IDs, tables, statuses, or folder locations.

## Initialize

Run the deterministic initializer instead of copying templates manually:

```bash
python scripts/init_idea.py /path/to/IDEA
```

It maps each asset to the correct destination and does not overwrite existing files unless `--force` is supplied.

After initialization:

1. Add concise notes to `05-文献库/`, one paper per file.
2. Classify the literature already collected.
3. Record uncovered local areas as **local coverage gaps**, not research gaps.
4. Record target-field bottlenecks in `01-灵感收集/问题结构图谱.md` before scanning source methods.
5. Use `06-跨领域方法库/` to track domain coverage, verified method cards, scans, and negative matches.
6. Run `python scripts/validate_idea_index.py /path/to/IDEA`.

## Generate And Screen Ideas

When brainstorming:

1. Read the user's research context, the registry, and relevant literature notes.
2. Read [references/idea-generation-methods.md](references/idea-generation-methods.md).
3. Choose methods from the signal actually available: use contradiction mapping for conflicting findings, counterexample-first for accepted properties, measurement-first for weak constructs or metrics, and regime mapping for behavior that changes across conditions.
4. Generate diverse candidates without making novelty claims.
5. Put raw candidates in `待评估点子.md`.
6. Deduplicate candidates against registry titles, aliases, and related IDs.
7. Promote worthwhile candidates into the registry with a stable ID and status `初筛`.
8. For a candidate being considered for formal evaluation, create a concise research idea card from `assets/研究点子卡.md`.
9. Apply the four hard gates in [references/scoring-v2.md](references/scoring-v2.md). Reject or park failed candidates with a reason.

Do not require a complete literature baseline before provisional brainstorming. Require sufficient evidence before evaluation, prioritization, or novelty claims.

## Run Systematic Combination Innovation

When the user asks to combine mature methods from other fields, read [references/cross-domain-method-atlas.md](references/cross-domain-method-atlas.md) and [references/validation-routes.md](references/validation-routes.md). Use this sequence:

1. Select the primary validation route for each candidate: **problem-existence** or **effect-efficacy**.
2. For problem-existence, start from a verified target problem in `问题结构图谱.md`. For effect-efficacy, start from an established target task and strong native baseline, then select a verified mature method with a relevant demonstrated capability.
3. Choose one bounded source-domain scan from `06-跨领域方法库/索引.md`.
4. Search authoritative reviews, handbooks, standards, canonical papers, and independent applications.
5. Admit a method card only after its structural purpose, inputs, outputs, assumptions, maturity evidence, and failure boundaries are traceable.
6. Match target structures to method purposes, not by domain labels or trend status.
7. Check native alternatives, assumption compatibility, and whether the adaptation adds scientific knowledge beyond interface glue.
8. Write a route-specific bridge statement and record the result in `扫描记录.md` as promising, negative, deferred, or promoted.
9. Hand promising pairs to Method 3 for deep transfer validation before adding them to the idea inbox.

Record negative matches. Do not let later brainstorming repeat a rejected pair without new evidence.

Do not equate falsifiability with problem-existence testing. For an effect-efficacy idea, make the primary probe a controlled comparison of the adapted method against strong baselines, with a minimum meaningful improvement, ablations, uncertainty, and resource costs. When generating a diverse batch, consider both validation routes unless the user or available evidence clearly favors one.

## Verify Differentiation

Use three evidence levels and preserve the distinction:

1. **Local coverage gap**: absent from `05-文献库/`; supports only a search priority.
2. **Search-supported gap**: no exact match found under a documented search protocol.
3. **Validated research gap**: converging evidence from databases, reviews, terminology variants, and citation chains supports a narrow claim.

Read [references/novelty-protocol.md](references/novelty-protocol.md) before checking novelty. Record evidence once in `evidence-log.md` using stable evidence and claim IDs. White papers must reference those IDs rather than copying evidence rows.

Before searching, split the novelty claim into problem framing, core mechanism, key insight, and application domain. Search broadly, triage by title and abstract, then read the full text of only the closest or ambiguous works. End with a concrete Delta Statement against the closest verified work. Treat assumptions and operating conditions as a separate mandatory check; do not reduce novelty to a simple count of matching axes.

Allowed wording:

> No exact match was found in the documented sources and search scope as of YYYY-MM-DD.

Avoid absolute wording such as "no one has done this."

## Evaluate An Idea

Choose a research profile before scoring. Read [references/research-profiles.md](references/research-profiles.md) and select the closest profile: theoretical, computational/experimental, qualitative, clinical/field, or design/constructive.

Then:

1. Confirm the idea ID and set status to `评估中`.
2. Create `02-评估中/[IDEA-ID] [short-title]/` for new work. Preserve legacy folder names when updating existing work.
3. Apply the significance, falsifiability, resource, and ethics gates.
4. Execute the novelty protocol: decompose the claim, search broadly, triage abstracts, deep-read the closest works, and write a Delta Statement.
5. Define a claim-aligned minimum feasibility probe. Use an existence/severity test for a problem-existence claim, and a controlled effect comparison for an effect-efficacy claim.
6. Write the white paper from [references/evaluation-template.md](references/evaluation-template.md).
7. Score with [references/scoring-v2.md](references/scoring-v2.md). Record a score, confidence, and one-sentence reason for every dimension.
8. Update the registry with the weighted score, confidence, decision, and next review date.
9. Remove or mark the corresponding inbox row as promoted.
10. Validate the workspace.

Treat the score as decision support, not objective truth. Compare ideas only when they use the same scoring version and compatible research profiles.

When the contribution is scientifically supported but hard to communicate, read [references/story-framing.md](references/story-framing.md). Use framing to clarify the contribution, never to inflate novelty.

## Transition Status

For every transition:

1. Update the canonical registry record.
2. Move existing artifacts to the status directory when required.
3. Record a decision reason.
4. For `搁置`, add a next review date.
5. For `重复` or `已取代`, add the related idea ID.
6. Run the validator and resolve new errors.

Never infer `已完成` from a folder move alone. Distinguish completion, rejection, duplication, supersession, and abandonment.

## Sync Literature

When adding papers:

1. Extract paper ID/DOI, title, venue/year, direction, core result, limitations, and relation to current ideas.
2. Update the local coverage map.
3. Re-check overlapping ideas across every status.
4. Add collision evidence to `evidence-log.md` and update affected decisions.
5. Label only the local map from local notes; run the novelty protocol before upgrading a gap level.

## Validate

Run:

```bash
python scripts/validate_idea_index.py /path/to/IDEA
```

Useful options:

```bash
python scripts/validate_idea_index.py /path/to/IDEA --json
python scripts/validate_idea_index.py /path/to/IDEA --strict
python scripts/validate_idea_index.py /path/to/IDEA --require-ids
```

Fix `ERROR` findings. Review `WARN` findings, especially legacy records, missing IDs, ambiguous folder matches, unresolved evidence references, and stale inbox entries.

## Non-Negotiable Rules

1. Do not infer global novelty from a local collection.
2. Keep one canonical registry record per idea and one stable ID per promoted idea.
3. Keep raw inbox entries cheap; do not write a full white paper before screening.
4. Bind every novelty claim to evidence IDs and a documented search scope.
5. Include contrary and overlapping work; negative evidence is still evidence.
6. Apply hard gates before scoring.
7. Keep urgency outside the weighted score; record it as scheduling metadata.
8. Check ethics, privacy, permissions, and dual-use risk where applicable.
9. Compare only compatible score versions and research profiles.
10. Validate after lifecycle, registry, or evidence changes.
11. Match cross-domain methods by problem structure and preserve negative-match history.
12. Keep problem-existence and effect-efficacy validation distinct; do not force every combination idea through a problem-existence proof.
