---
name: research-ideation
description: "Systematic research idea generation, evaluation, and management for academic researchers. Provides 6 brainstorming methods, novelty verification against literature, and a standardized 30-point scoring framework. Trigger on: generating research ideas, evaluating research directions, checking novelty, managing an idea pipeline, comparing research proposals, or brainstorming. Use when the user asks about thinking of new research directions, whether an idea is worth pursuing, or needs to systematically generate and assess research ideas."
agent_created: false
---

# Research Ideation — Systematic Idea Management & Evaluation

A domain-agnostic system for generating, evaluating, and managing research ideas. Designed for academic researchers in any field who need to systematically explore research directions rather than relying on ad-hoc inspiration.

## Core Philosophy

Ideas are not random sparks — they can be systematically generated, rigorously evaluated, and objectively compared. This skill provides the framework.

## Folder Structure

Initialize the IDEA folder with this structure:

```
IDEA/
├── 01-灵感收集/          # Idea collection & brainstorming
│   ├── 索引.md            # Index of all ideas + literature novelty map
│   ├── 想点子指南.md       # Idea generation methodology (6 methods)
│   └── 待评估点子.md       # Idea pool (unstructured brainstorming)
├── 02-评估中/            # Under evaluation
│   └── [点子名]/          # Each idea gets its own folder
│       └── [评估白皮书.md] # Evaluation white paper
├── 03-进行中/            # Actively working on
├── 04-已归档/            # Completed or abandoned
└── README.md             # System overview & file responsibilities
```

To initialize, run:

```bash
mkdir -p IDEA/{01-灵感收集,02-评估中,03-进行中,04-已归档}
```

Then create the template files in `assets/` — copy each `.md` file to its corresponding location.

## Workflow

### Phase 1: Generate Ideas

When the user asks to "think of new ideas" or "brainstorm research directions":

1. Read `01-灵感收集/想点子指南.md` to understand the generation methods
2. Read `01-灵感收集/索引.md` to understand existing ideas and literature landscape
3. Apply each method systematically (see `references/idea-generation-methods.md` for detailed guidance)
4. Perform novelty verification via web search
5. Write results to `01-灵感收集/待评估点子.md`

### Phase 2: Evaluate an Idea

When the user asks to "evaluate" or "assess" an idea:

1. Read `01-灵感收集/想点子指南.md` for methodology context
2. Conduct comprehensive literature research:
   - Web search with multiple keyword combinations
   - Check user's IMA knowledge base (if available and user specifies the name)
   - Search for direct competitors, adjacent work, and related methods
3. Write evaluation white paper using template in `references/evaluation-template.md`
4. Create idea folder in `02-评估中/[idea-name]/`
5. Update `01-灵感收集/索引.md` with the new entry
6. Update `01-灵感收集/待评估点子.md` to mark the idea as evaluated

### Phase 3: Novelty Verification

Before claiming an idea is novel, verify through multiple channels:

1. **Web search** — Use at least 3-5 different keyword combinations
2. **Survey papers in your field** — Check if comprehensive surveys mention the direction
3. **Knowledge base / literature collection** — If user has a personal literature collection or knowledge base, search it
4. **Claim carefully** — If the exact combination hasn't been found, check adjacent work that partially overlaps. Distinguish "no work exists" from "no exact match but related work exists"

### Phase 4: Refine & Update

When the user says "fix" or "update" an evaluation:

1. Identify specific problems (literature gaps, wrong novelty claim, missing references)
2. Conduct targeted additional research
3. Revise the white paper, noting what changed
4. Update version number

## File Responsibilities

| File | Role | One-line rule |
|------|------|---------------|
| `想点子指南.md` | Methodology | How to think of ideas — updated when user teaches new methods |
| `待评估点子.md` | Idea pool | Raw brainstorming — one line per idea, no structure required |
| `索引.md` | Index + novelty map | All evaluated ideas + literature landscape for novelty checks |
| `README.md` | System docs | File responsibilities and workflow overview |

### Flow

```
想点子指南.md (methodology)
        ↓ apply methods
碎片想法 → 待评估点子.md (pool)
                ↓ research & evaluate
独立评估文件 (one folder per idea) → 索引.md (register)
```

## Evaluation White Paper Structure

Each evaluation white paper should contain (see `references/evaluation-template.md` for full template):

1. **Executive Summary** — Score, verdict, key finding
2. **Idea Definition** — What exactly is the idea
3. **Research Status** — Existing work, competitors, adjacent work
4. **Novelty Verification** — What's been checked, what's truly new
5. **Technical Feasibility** — Concrete technical paths
6. **Application Scenarios** — Where would this be useful
7. **Risk Assessment** — What could go wrong
8. **Literature Support** — Key references
9. **Horizontal Comparison** — How it compares to other evaluated ideas
10. **Conclusion & Recommendation** — Proceed or not

## Scoring System

Rate each idea on 6 dimensions (1-5 scale, 0.5 increments):

| Dimension | What it measures |
|-----------|-----------------|
| Novelty (新颖性) | Has this been done before? |
| Technical Feasibility (技术可行性) | Can it actually be implemented? |
| Experimental Verifiability (实验可验证性) | Can results be demonstrated? |
| Publication Feasibility (发表可行性) | Will reviewers accept it? |
| Fit with Current Research (契合度) | Does it align with your existing work? |
| Urgency (紧迫性) | Is there competitive pressure? |

Total = sum of all 6 dimensions (max 30).

## Important Rules

1. **One idea = one file** — Each evaluated idea gets its own folder and white paper
2. **Novelty requires proof** — Never claim "this is novel" without searching at least 3 keyword combinations
3. **Score honestly** — A score of 3.0 means "adequate", not "good". Don't inflate
4. **Update the index** — Every new idea must be registered in `索引.md`
5. **Track competitors** — If related work exists, document it explicitly. Don't pretend it doesn't
