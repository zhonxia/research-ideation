# Evaluation White Paper Template v2

Use this template only after an idea passes initial screening. Keep evidence in the central evidence log and reference its IDs here.

## Contents

1. Decision summary
2. Idea definition
3. Hard gates
4. Research landscape
5. Differentiation claims
6. Research plan and feasibility probe
7. Evaluation profile and score
8. Risks and governance
9. Decision

```markdown
---
idea_id: IDEA-YYYY-NNNN
title: Short stable title
status: 评估中
research_profile: theoretical | computational-experimental | qualitative | clinical-field | design-constructive
primary_validation: problem-existence | effect-efficacy | other
score_version: v2
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# [IDEA-ID] [Title] Evaluation White Paper

## 1. Decision Summary

**Research question**: [One precise, answerable question]

**Proposed contribution**: [What new knowledge, method, artifact, or evidence would result?]

**Current decision**: Proceed / Probe first / Park / Reject / Duplicate / Superseded

**Weighted score**: XX.X / 100  
**Overall confidence**: Low / Medium / High  
**Urgency**: Low / Medium / High; [reason and decision window]  
**Next review**: YYYY-MM-DD / N/A

## 2. Idea Definition

### 2.1 Scope

- **Population/system/domain**: [scope]
- **Intervention/method/exposure**: [scope]
- **Comparator/baseline**: [scope]
- **Outcome/claim**: [scope]
- **Explicit exclusions**: [what this idea does not claim]

### 2.2 Contribution Type

- [ ] Theory or proof
- [ ] Method or algorithm
- [ ] Empirical finding
- [ ] Dataset, benchmark, or measurement instrument
- [ ] System or design artifact
- [ ] Synthesis or conceptual framework

### 2.3 One-Sentence Pitch

[Problem -> gap -> contribution -> consequence]

### 2.4 Innovation Claim Breakdown

| Part | Proposed claim |
|---|---|
| Problem framing | [task, inputs, outputs, population, evaluation setting] |
| Core mechanism | [algorithm, theory, proof move, experiment, or data construction] |
| Key insight | [why it may work and what prior work lacks] |
| Application domain | [field, setting, and intended scope] |

**Assumptions and operating conditions**: [conditions required for the claim]

## 3. Hard Gates

| Gate | Pass? | Evidence and reason |
|---|:---:|---|
| Problem significance | Yes / No / Unknown | [Who needs the answer and what changes?] |
| Falsifiability / answerability | Yes / No / Unknown | [What result would disconfirm or bound the claim?] |
| Resource access | Yes / No / Unknown | [Data, equipment, expertise, time, permissions] |
| Ethics and governance | Yes / No / N/A / Unknown | [Privacy, consent, safety, dual use, licensing] |

**Gate decision**: Continue / Run a gate-closing probe / Stop

Do not calculate a weighted score while a critical gate is `No`. Treat `Unknown` as an explicit next action.

## 4. Research Landscape

### 4.1 Local Coverage

[Summarize relevant `05-文献库/` notes. Label absences only as local coverage gaps.]

### 4.2 Search Scope

- **Databases/channels**: [list]
- **Date range**: [range]
- **Languages**: [list]
- **Terminology families**: [list]
- **Reviews checked**: [citations]
- **Backward/forward citation chains**: [scope]
- **Search end date**: YYYY-MM-DD
- **Stopping rule reached**: saturation / time budget / unresolved

### 4.3 Closest Work

| Work | Identifier | Evidence read | Four-part comparison | Remaining difference | Threat level |
|---|---|---|---|---|:---:|
| [Citation] | DOI/URL | Abstract / Full text | [match/partial/different/unclear by part] | [narrow difference] | High/Med/Low |

**Delta Statement**:

> Unlike [closest verified work], which [does X under condition or assumption Y], this idea [changes X, relaxes Y, or extends to Z], and tests the difference through [observable result R].

## 5. Differentiation Claims

| Claim ID | Narrow claim | Evidence IDs | Gap level | Confidence | Allowed wording |
|---|---|---|---|:---:|---|
| CLM-[IDEA-ID]-01 | [claim] | EV-YYYY-NNNN, ... | Local / Search-supported / Validated | 0.00-1.00 | [bounded statement] |

**Contrary evidence**: [Evidence that weakens or narrows the contribution]

**Residual uncertainty**: [Missing venues, terms, languages, data, or citation branches]

## 6. Research Plan And Feasibility Probe

### 6.1 Primary Validation Route

**Route**: Problem-existence / Effect-efficacy / Other

**Central empirical or theoretical claim**: [What result carries the paper?]

Do not require a problem-existence proof for an effect-efficacy claim. Match the probe to the central claim.

### 6.2 Claim-Aligned Minimum Probe

- **Question**: [cheapest high-information uncertainty]
- **Procedure**: [small proof, pilot, expert interview, data audit, prototype, etc.]
- **Pass criterion**: [observable threshold]
- **Stop criterion**: [result that rejects or reframes the idea]
- **Budget**: [time/resources]

For a problem-existence route, specify the existence/severity metric and positive/negative controls.

For an effect-efficacy route, complete this comparison design:

| Element | Specification |
|---|---|
| Established target task | [task and why it matters] |
| Strong native baseline N | [current credible method] |
| Direct transfer M | [source method without target-specific adaptation] |
| Adapted method C | [proposed method] |
| Relevant external baseline | [if applicable] |
| Primary outcome R | [metric] |
| Minimum meaningful improvement | [predefined threshold] |
| Ablations | [components that isolate the adaptation] |
| Resource and cost controls K | [data, parameters, tuning, compute, maintenance] |
| Uncertainty protocol | [datasets, regimes, seeds, intervals/tests] |

### 6.3 Full Research Plan

[Use the selected research profile. Define data or premises, method, comparators, outcomes, uncertainty analysis, and reproducibility plan.]

### 6.4 Expected Failure Modes

| Failure mode | Likelihood | Consequence | Early signal | Mitigation |
|---|:---:|:---:|---|---|
| [risk] | H/M/L | H/M/L | [signal] | [action] |

## 7. Evaluation Profile And Score

**Profile**: [profile]  
**Score version**: v2

| Dimension | Weight | Score (1-5) | Confidence | One-sentence evidence-based reason |
|---|:---:|:---:|:---:|---|
| Problem significance | 20 | X.X | L/M/H | [reason] |
| Differentiation | 20 | X.X | L/M/H | [reason and claim IDs] |
| Technical/method feasibility | 15 | X.X | L/M/H | [reason] |
| Validation clarity | 15 | X.X | L/M/H | [reason] |
| Publication/communication readiness | 10 | X.X | L/M/H | [audience, venue, and framing] |
| Strategic fit | 20 | X.X | L/M/H | [skills, portfolio, resources] |

**Weighted score**: sum(score / 5 * weight) = XX.X / 100

**Sensitivity**: [Which uncertain dimension could change the decision? Re-score the plausible low/high case.]

For publication/communication readiness, use [story-framing.md](story-framing.md) to clarify the narrative. Do not use framing to compensate for weak significance, differentiation, or evidence.

Do not compare this score with legacy 30-point scores without explicitly converting or re-evaluating them.

## 8. Risks And Governance

| Area | Finding | Required action |
|---|---|---|
| Ethics/privacy | [finding] | [action] |
| Permissions/licensing | [finding] | [action] |
| Dual use/safety | [finding] | [action] |
| Reproducibility | [finding] | [action] |
| Researcher degrees of freedom | [finding] | [action] |

## 9. Decision

**Decision**: Proceed / Probe first / Park / Reject / Duplicate / Superseded

**Decision reason**: [Tie the decision to gates, evidence, score sensitivity, and opportunity cost.]

**Related idea ID**: [required for Duplicate or Superseded]

**Next actions**:

- [ ] [owner/action/date]
- [ ] [owner/action/date]

**Next review date**: YYYY-MM-DD / N/A
```
