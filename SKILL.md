---
name: research-ideation
description: "Systematic research idea generation, evaluation, and management for academic researchers. Provides 7 brainstorming methods (including reverse-engineering research), novelty verification against literature, and a standardized 30-point scoring framework. Trigger on: generating research ideas, evaluating research directions, checking novelty, managing an idea pipeline, comparing research proposals, or brainstorming. Use when the user asks about thinking of new research directions, whether an idea is worth pursuing, or needs to systematically generate and assess research ideas."
---

# Research Ideation — Systematic Idea Management & Evaluation

A domain-agnostic system for generating, evaluating, and managing research ideas. Designed for academic researchers in any field who need to systematically explore research directions rather than relying on ad-hoc inspiration.

## Core Philosophy

Ideas are not random sparks — they can be systematically generated, rigorously evaluated, and objectively compared. This skill provides the framework.

**The key insight**: Before generating new ideas, you need a baseline. The `文献库/` (literature library) serves as that baseline — it tells you what already exists so you know what's genuinely new.

## Folder Structure

Initialize the IDEA folder with this structure:

```
IDEA/
├── 01-灵感收集/          # Idea collection & brainstorming
│   ├── 索引.md            # Index of all ideas + literature novelty map
│   ├── 想点子指南.md       # Idea generation methodology (6 methods)
│   ├── 待评估点子.md       # Idea pool (unstructured brainstorming)
│   └── evidence-log.md    # Search/evidence log for novelty claims
├── 02-评估中/            # Under evaluation
│   └── [点子名]/          # Each idea gets its own folder
│       └── [评估白皮书.md] # Evaluation white paper
├── 03-进行中/            # Actively working on
├── 04-已归档/            # Completed or abandoned
├── 05-文献库/            # Literature library — research directions extracted from papers
│   └── [论文名].md        # One file per paper (title, core idea, direction category)
└── README.md             # System overview & file responsibilities
```

To initialize, run:

```bash
mkdir -p IDEA/{01-灵感收集,02-评估中,03-进行中,04-已归档,05-文献库}
```

Then create the template files from `assets/` — copy each `.md` file to its corresponding location.

## Workflow

### Phase 0: Initialize & Build Literature Baseline

This is the **most critical step**. Before generating any ideas, you must understand what already exists.

When the user says "initialize the IDEA folder" or "set up the IDEA system":

1. Create the folder structure (see above)
2. Create template files from `assets/`
3. **Scan the literature library**: Read every `.md` file in `05-文献库/`
4. For each literature note, extract: title, authors, research direction, core idea
5. **Classify** each paper's research direction into categories (e.g., interpretability, robustness, fault diagnosis, etc.)
6. **Populate `索引.md`**: Write all extracted research directions into the novelty verification section
7. **Identify gaps**: List directions that are NOT covered by any paper — these are your potential opportunity spaces

**Literature note format** (each file in `05-文献库/`):

```markdown
# [Paper Title]

- **Authors**: [Names]
- **Journal/Year**: [Venue, YYYY]
- **Direction**: [Research direction category]
- **Core Idea**: [One-paragraph summary of the method]
- **Relation to My Work**: [Why this paper matters to your research]
```

Even if the user hasn't populated `05-文献库/` yet, create the placeholder so they know to fill it. The literature baseline can be built incrementally — add papers as you read them.

**When to update the literature library**: Every time the user reads a new paper, add a note file. The index should be re-synced.

### Phase 1: Generate Ideas

When the user asks to "think of new ideas" or "brainstorm research directions":

1. Read `01-灵感收集/想点子指南.md` — understand the generation methods
2. Read `01-灵感收集/索引.md` — understand what already exists (novelty baseline)
3. **Check the literature gaps** — the gaps identified in the index are priority targets
4. Apply each method systematically (see `references/idea-generation-methods.md` for detailed guidance)
   - Methods 1–6: diverge outward from existing literature
   - **Method 7 (Reverse-Engineering)**: start from a concrete goal, decompose backwards until you hit a gap the literature cannot fill — that gap is your contribution
5. Perform novelty verification via web search and record every search in `01-灵感收集/evidence-log.md`
6. Write results to `01-灵感收集/待评估点子.md`
7. **Register each new idea in `01-灵感收集/索引.md`** with status "待评估" — this prevents duplicate ideas during brainstorming and makes the index the single source of truth for all ideas

### Phase 2: Evaluate an Idea

When the user asks to "evaluate" or "assess" an idea:

1. Read `01-灵感收集/想点子指南.md` for methodology context
2. Conduct comprehensive literature research:
   - Web search with multiple keyword combinations
   - Search the `05-文献库/` literature library
   - Check user's knowledge base (if configured)
   - Search for direct competitors, adjacent work, and related methods
3. Record all novelty evidence in both places:
   - Append each query/source/check to `01-灵感收集/evidence-log.md`
   - Copy the relevant rows into the white paper's embedded Search Log
4. Write evaluation white paper using template in `references/evaluation-template.md`
5. Create idea folder in `02-评估中/[idea-name]/`
6. Update `01-灵感收集/索引.md` — change status from "待评估" to "评估中", fill in evaluation details (score, one-sentence reasons, verdict)
7. Update `01-灵感收集/待评估点子.md` to mark the idea as evaluated

### Phase 3: Novelty Verification

Before claiming an idea is novel, verify through multiple channels and bind the claim to evidence:

1. **`05-文献库/`** — Check if any literature note already covers this direction
2. **Web search** — Use at least 3-5 different keyword combinations (English + Chinese)
3. **Survey papers** — Check if comprehensive surveys mention the direction
4. **Knowledge base** — If user has an external knowledge base (e.g., IMA, Zotero), search it
5. **Claim carefully** — Distinguish "no work exists" from "no exact match but related work exists"

#### Evidence Log Standard

Every novelty claim must be traceable to search evidence. A claim is not allowed unless it has at least one supporting row in `01-灵感收集/evidence-log.md` or the white paper's embedded Search Log.

Each evidence row must include:

| Field | Required content |
|-------|------------------|
| Date | Search/check date in `YYYY-MM-DD` |
| Idea | Idea or claim being checked |
| Claim | The exact novelty claim, stated narrowly |
| Query / Source | Search query, literature-library check, survey paper, or knowledge-base query |
| Channel | Web, `05-文献库`, survey, IMA/Zotero, manual paper |
| Key Results | Specific papers, authors, years, links, or "no exact match found" |
| Conclusion | Exact match / partial overlap / adjacent only / no close match |
| Confidence | 0.0-1.0 confidence in the conclusion |
| Notes | Caveats, missing databases, next searches |

Confidence should be conservative:
- `0.9-1.0`: Multiple authoritative sources checked; exact wording and adjacent terms covered
- `0.7-0.8`: Good search coverage, but some databases or languages may be missing
- `0.5-0.6`: Preliminary search only; use for brainstorming, not final novelty claims
- `<0.5`: Too weak to support a novelty claim

Use careful wording:
- Allowed with evidence: "No exact match found in the searched sources as of YYYY-MM-DD."
- Avoid: "No one has done this" unless the evidence coverage is unusually comprehensive.

### Phase 4: Sync Literature → Index

When the user adds new papers to `05-文献库/`:

1. Read each new literature note
2. Extract research direction and core idea
3. Update the novelty verification section in `索引.md`
4. Re-check: do any new papers overlap with existing ideas in `索引.md` (check against all statuses)?
5. If overlap found, update the affected idea's entry in `索引.md` with a note about the collision

### Phase 5: Transition Idea Status

When the user says "move [idea] to [new status]" or "I'm starting/abandoning this idea":

1. Identify current idea entry in `索引.md`
2. Update the status:
   - `进行中` → moving from `02-评估中/` (evaluation folder) to `03-进行中/` (active)
   - `已归档` → moving from `03-进行中/` or `02-评估中/` to `04-已归档/`
3. Move the idea folder to the corresponding directory
4. Add a brief summary note (e.g., "reason for archiving" if applicable)
5. Update `索引.md` with the new status
6. Run `scripts/validate_idea_index.py IDEA/` and fix any lifecycle inconsistency it reports

### Phase 6: Refine & Update

When the user says "fix" or "update" an evaluation:

1. Identify specific problems (literature gaps, wrong novelty claim, missing references)
2. Conduct targeted additional research
3. Revise the white paper, noting what changed
4. Update version number

### Phase 7: Validate Idea Index

When the user asks to "validate", "check consistency", "audit IDEA", or after any lifecycle transition:

1. Run the bundled script:

```bash
python scripts/validate_idea_index.py /path/to/IDEA
```

2. Review findings:
   - `ERROR`: must fix; the index, pending pool, or status folders disagree
   - `WARN`: should review; the script skipped a weakly structured section or found an unknown status
3. Fix the relevant file or folder:
   - Add missing pending ideas to `索引.md`
   - Move folders to match their status
   - Update status in `索引.md`
   - Register unindexed folders
4. Re-run the script until it reports zero errors.

Use `--json` when another tool should consume the report, and `--strict` when warnings should fail validation too.

## File Responsibilities

| File | Role | One-line rule |
|------|------|---------------|
| `索引.md` | Index + novelty map + lifecycle tracker | Central registry — all ideas (待评估/评估中/进行中/已归档) + literature landscape |
| `想点子指南.md` | Methodology | How to think of ideas — updated when user teaches new methods |
| `待评估点子.md` | Idea pool | Raw brainstorming — one line per idea, no structure required |
| `evidence-log.md` | Evidence log | Every novelty claim must link to query/source/date/conclusion/confidence |
| `05-文献库/*.md` | Literature library | One file per paper — building the novelty baseline |
| `README.md` | System docs | File responsibilities and workflow overview |
| `scripts/validate_idea_index.py` | Consistency validator | Checks `索引.md`, `待评估点子.md`, and status folders agree |

### Data Flow

```
文献库/ (literature library)
        ↓ scan & classify on init / sync
索引.md (novelty baseline + gaps + idea register)
        ↓ informs
想点子指南.md (methodology)
        ↓ apply methods
待评估点子.md (raw pool) ──→ 索引.md (register as pending)
        ↓ research & evaluate
02-评估中/[idea-name]/ (white paper)
        ↓ update status
索引.md (待评估 → 评估中, fill score)
```

## Important Rules

1. **Literature first, ideas second** — Always build the novelty baseline before generating ideas
2. **One evaluated idea = one folder** — Each evaluated idea gets its own folder and white paper in `02-评估中/`
3. **One paper = one file** — Each paper in `05-文献库/` gets its own note
4. **Novelty requires proof** — Never claim "this is novel" without searching at least 3 keyword combinations
5. **Evidence rows are mandatory** — Every novelty claim must include query/source, date, key results, conclusion, and confidence
6. **Every score needs one sentence** — After each dimension score, write one short reason explaining why that number was chosen
7. **Score honestly** — A score of 3.0 means "adequate", not "good". Don't inflate
8. **Index is the single source of truth** — Every idea (pending or evaluated) and every literature note must be registered in `索引.md`. Ideas enter the index at generation time (status: 待评估), not just after evaluation
9. **Idea lifecycle** — Ideas flow through statuses: 待评估 → 评估中 → 进行中 → 已归档. Update `索引.md` at every transition
10. **Track competitors** — If related work exists, document it explicitly. Don't pretend it doesn't
11. **Keep literature notes concise** — One file per paper, focus on direction + core idea (not full summary)
12. **Validate after transitions** — Run `scripts/validate_idea_index.py IDEA/` after moving ideas or editing lifecycle status

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

Each dimension must include a one-sentence reason after the score. Keep it lightweight: the goal is to remember why the score was assigned three months later, not to create another audit system.

Example:

```markdown
Novelty: 4/5 — Searched Semantic Scholar and Google Scholar; no direct combination found, but adjacent work exists.
Technical Feasibility: 3/5 — The method is plausible, but access to the required molecular dataset is uncertain.
```
