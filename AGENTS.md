# AGENTS.md — research-ideation

## Repo purpose

Skill definition for an AI assistant (OpenCode/WorkBuddy). Generates, evaluates, and manages academic research ideas. Primary entrypoint is `SKILL.md`.

## File layout

- `SKILL.md` — skill behavior definition (read this first before acting)
- `README.md` — bilingual (EN/CN) system overview for end users
- `assets/` — template files copied into the user's `IDEA/` folder on init
- `references/` — supporting docs (scoring guidelines, brainstorming methods)

## Init workflow

When user says "initialize the IDEA folder":

1. `mkdir -p IDEA/{01-灵感收集,02-评估中,03-进行中,04-已归档,05-文献库}`
2. Copy `assets/` templates → corresponding `IDEA/` locations
3. Read every `.md` file in `05-文献库/` if populated
4. Extract direction + core idea from each paper, classify into categories
5. Populate `索引.md` novelty map: existing directions, gaps, opportunity spaces

The literature baseline (`05-文献库/`) is mandatory before idea generation. Always scan it on init/re-sync.

## Workflow phases

```
Literature baseline (05-文献库/) → scan → 索引.md (gaps identified)
                                          ↓
想点子指南.md (6 methods) → generate → 待评估点子.md (raw pool)
                                          ↓
register as pending ─────────────────→ 索引.md (status: 待评估)
                                          ↓
research + evaluate → 02-评估中/[idea-name]/ (white paper)
                                          ↓
update status ────────────────────────→ 索引.md (待评估 → 评估中)
```

## Non-obvious conventions

- `索引.md` is triple-purpose: idea registry + lifecycle tracker + novelty verification map. Don't split.
- Ideas are registered in `索引.md` at generation time (status: 待评估), not just after evaluation.
- Idea lifecycle: 待评估 → 评估中 → 进行中 → 已归档. Update `索引.md` on every transition.
- One paper = one `.md` file in `05-文献库/`. One evaluated idea = one folder in `02-评估中/`.
- Novelty claims require ≥3 keyword combinations searched (English + Chinese). Never claim without proof.
- Scoring: 6 dimensions × 1-5 (0.5 increments), max 30. Score 3.0 = adequate, not good.
- `想点子指南.md` is extensible — user adds new methods over time.
- Evaluation white papers follow `references/evaluation-template.md` exactly.

## No build/test system

Pure markdown. No linting, typechecking, or tests. No package.json or dependencies.
