# Evaluation Guide

Used during the `评估中` phase. Combine with `idea-generation-methods.md` (for the generation-side structure) and `novelty-protocol.md` (for differentiation claims).

## Contents

1. Validation route selection
2. Research profile selection
3. Evaluation white paper template
4. Scoring reference
5. Story framing

---

## 1. Validation Route Selection

Choose the primary validation route before designing a probe. Falsifiability does not imply that every idea must first prove a new target-field problem exists.

### Route Selection

| Central claim | Primary route | Main question |
|---|---|---|
| The target method fails, becomes invalid, or suffers a measurable limitation under condition Z | Problem-existence | Does the claimed problem materially affect the target? |
| An adapted mature method improves a target task over the current practice | Effect-efficacy | Does the adaptation produce a meaningful benefit at acceptable cost? |

Do not rewrite an effect claim as a problem-existence claim merely to make the adaptation look necessary. A legitimate target task with an improvable baseline is sufficient motivation for the effect-efficacy route.

Default to the **effect-efficacy** route. Only switch to problem-existence when the central contribution depends on proving that a target limitation actually exists.

### Lifecycle Calibration

Route selection happens during generation, but contribution detail grows by stage:

| Stage | Required contribution detail |
|---|---|
| Brainstorming / `初筛` | A plausible innovation hook: what capability is borrowed, why direct transfer may be insufficient, and one or two candidate mechanism directions |
| `评估中` | A concrete method or knowledge delta against the closest work and direct transfer, plus the comparison and falsification design |
| `进行中` | A complete algorithmic, theoretical, measurement, or constructive contribution aligned with the paper's claims |

At `初筛`, the target-specific adaptation may remain a mechanism family rather than a finalized formulation. Do not demand implementation-level detail that suppresses exploration. Direct application without an innovation hook still fails the screen.

### Problem-Existence Route

Use when the research contribution depends on showing that a target-field assumption, guarantee, metric, or workflow actually fails.

Required fields:

- Claimed problem and affected population or regime
- Observable consequence and severity measure
- Native workaround and why it may be insufficient
- Existence/severity test with positive and negative controls
- Stop or reframe condition if the effect is absent or negligible

Primary validation:

> Show that problem P materially affects target T under condition Z.

Do not start solution development before a cheap existence or severity probe when the entire contribution disappears if P is absent.

### Effect-Efficacy Route

Use when the target task is already legitimate and the main contribution is an adapted method that may improve it. Do not require a new failure phenomenon before testing the method.

Required fields:

- Established target task and current practice
- Mature source method and its demonstrated capability
- Structural reason it may transfer
- Target-specific adaptation
- Primary outcome and minimum meaningful improvement
- Accuracy/quality, computation, data, interpretability, and maintenance costs
- Strong native baseline, direct unadapted transfer, adapted method, and relevant non-target-field baseline
- Ablations that isolate the adaptation
- Uncertainty analysis across datasets, regimes, and random seeds where applicable
- Stop or reframe condition if gains are negligible, unstable, or explained only by extra resources

Primary validation:

> Show that adapted method C improves outcome R over strong native baseline N under condition Z, while cost K remains acceptable.

Minimum comparison set:

| Arm | Purpose |
|---|---|
| Native target-field baseline N | Tests whether the proposal improves current practice |
| Direct transfer M | Tests whether adaptation is actually necessary |
| Adapted method C | Measures the proposed contribution |
| Strong non-target-field baseline | Prevents target-field insularity when an external baseline is relevant |

An average improvement alone is insufficient when it comes from more parameters, more data, more tuning, or more compute. Normalize resources or report the tradeoff explicitly.

### Shared Scientific Requirements

Both routes must still establish the following at the depth appropriate to the lifecycle stage:

1. Structural fit rather than label similarity.
2. A contribution beyond interface glue.
3. Comparison with credible native alternatives.
4. A route-aligned falsification criterion.
5. Generalizable knowledge: mechanism, design rule, boundary, or reproducible effect rather than a one-dataset win.

The adaptation need not repair a newly discovered defect. It may encode target constraints, exploit target structure, reduce cost, or improve an established outcome. During `初筛`, treat this as a contribution hypothesis; verify that it is scientifically substantive during `评估中`.

### Route-Specific Probe Templates

**Problem-existence probe:**

```text
Claimed problem:
Affected condition:
Existence/severity metric:
Positive control:
Negative control:
Continue threshold:
Stop or reframe threshold:
```

**Effect-efficacy probe:**

```text
Target task:
Native baseline:
Source method:
Target-specific adaptation:
Primary outcome:
Minimum meaningful improvement:
Direct-transfer control:
Ablations:
Resource/cost controls:
Uncertainty protocol:
Continue threshold:
Stop or reframe threshold:
```

---

## 2. Research Profile Selection

Select one primary profile before applying gates, planning validation, or interpreting scores. Use a secondary profile only when the contribution is genuinely mixed.

### Theoretical

- Define objects, assumptions, claim, and scope precisely.
- Validate through proof, counterexample search, boundary cases, and relation to known results.
- Treat theorem significance, assumption realism, and proof tractability as key feasibility evidence.
- The minimum probe may be a restricted-case proof or counterexample.

### Computational / Experimental

- Define datasets, baselines, metrics, ablations, uncertainty, and compute budget.
- Separate algorithmic novelty from implementation changes.
- Plan statistical power, leakage controls, robustness, and reproducibility.
- For effect-efficacy claims, predefine a minimum meaningful improvement and compare a strong native baseline, direct transfer, adapted method, and relevant external baseline while controlling resources.
- The minimum probe may be a small controlled benchmark, synthetic identifiability test, or strong-baseline reproduction.

### Qualitative

- Define the phenomenon, sampling logic, positionality, data collection, and analytic approach.
- Evaluate credibility, transferability, reflexivity, and saturation rather than benchmark accuracy.
- Treat access, consent, transcription, and coding capacity as resources.
- The minimum probe may be access confirmation or a small set of pilot interviews.

### Clinical / Field

- Define population, intervention/exposure, comparator, outcomes, setting, and safety constraints.
- Evaluate clinical relevance, recruitment, power, protocol registration, ethics, and implementation fidelity.
- Separate surrogate outcomes from outcomes that matter to patients or stakeholders.
- The minimum probe may be a retrospective feasibility audit, recruitment estimate, or protocol review.

### Design / Constructive

- Define stakeholder need, artifact, design principles, context, and evaluation criteria.
- Distinguish a research contribution from routine engineering.
- Evaluate utility, usability, field performance, generalizable design knowledge, and maintenance burden.
- The minimum probe may be a low-fidelity prototype or stakeholder walkthrough.

### Cross-Profile Rule

Do not penalize a theoretical idea for lacking a standard dataset, or reward a qualitative study for benchmark availability. Translate `feasibility` and `validation clarity` through the selected profile while retaining the same weighted dimensions.

---

## 3. Evaluation White Paper Template

Use this template only after an idea passes initial screening. Keep evidence in the central evidence log and reference its IDs here.

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
|---|---|---|---|---|---|:---:|
| [Citation] | DOI/URL | Abstract / Full text | [match/partial/different/unclear by part] | [narrow difference] | High/Med/Low |

**Delta Statement**:

> Unlike [closest verified work], which [does X under condition or assumption Y], this idea [changes X, relaxes Y, or extends to Z], and tests the difference through [observable result R].

## 5. Differentiation Claims

| Claim ID | Narrow claim | Evidence IDs | Gap level | Confidence | Allowed wording |
|---|---|---|---|---|---|:---:|
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
|---|---|:---:|:---:|---|---|
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

---

## 4. Scoring Reference

Apply the hard gates (section 3 of the white paper) before calculating a weighted score. Scores support portfolio decisions; they do not measure scientific truth.

### Weighted Dimensions

Score in 0.5 increments from 1 to 5.

| Dimension | Weight | 1 | 3 | 5 |
|---|:---:|---|---|---|
| Problem significance | 20 | Marginal or unclear consequence | Useful answer for a defined audience | Changes important knowledge, capability, or decisions |
| Differentiation | 20 | Closely duplicates existing work | Defensible extension with meaningful distinction | Clear, important gap supported by strong bounded evidence |
| Technical/method feasibility | 15 | No credible route | Major uncertainties but testable route | Clear route with accessible prerequisites |
| Validation clarity | 15 | Success cannot be judged | Plausible evaluation with unresolved threats | Decisive tests, comparators, and uncertainty analysis |
| Publication/communication readiness | 10 | Audience and contribution unclear | Plausible venue and narrative | Clear audience, contribution, and coherent evidence story |
| Strategic fit | 20 | High opportunity cost, little leverage | Some relevant capability | Strong leverage across expertise, assets, and portfolio |

Calculate:

```text
weighted contribution = score / 5 * weight
total = sum(weighted contributions), max 100
```

### Confidence

Record Low, Medium, or High confidence for every dimension:

- **Low**: assumption or preliminary evidence dominates.
- **Medium**: useful evidence exists but an important uncertainty remains.
- **High**: multiple independent evidence sources or a completed probe support the score.

Run a sensitivity check using plausible low/high scores for the least certain dimensions. If the decision changes, choose `Probe first` rather than pretending the point estimate is decisive.

### Urgency Metadata

Urgency does not contribute to the weighted score. Record:

- Competitive pressure: Low / Medium / High
- External deadline or opportunity window
- Cost of waiting
- Next review date

Use urgency to schedule work after quality and expected value are assessed.

### Legacy Scores

Keep legacy `/30` totals labeled as `v1`. Do not multiply them into a v2 score. Re-score an idea under v2 before comparing it with new records.

---

## 5. Story Framing

Framing clarifies a contribution; it cannot substitute for significance, differentiation, or evidence.

### Narrative Options

| Pattern | Structure | Useful for |
|---|---|---|
| Problem -> solution -> consequence | Important problem, proposed contribution, resulting capability | Applied and method papers |
| Current practice -> limitation -> bridge | Existing approach, bounded limitation, contribution that closes it | Extensions and measurement work |
| Observation -> explanation -> implication | Surprising result, mechanism, broader consequence | Empirical and theoretical work |
| Claim -> assumptions -> evidence | Precise claim, conditions, proof or tests | Theory and high-risk claims |

### One-Sentence Test

Write one sentence containing:

1. The important problem or observation
2. The exact gap
3. The contribution
4. The consequence if correct

If the sentence requires inflated novelty language, return to the claim and evidence. Score publication/communication readiness on audience fit, contribution clarity, and narrative coherence, not assumed reviewer psychology.
