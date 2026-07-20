# Cross-Domain Method Atlas

Use the atlas to turn combination innovation from random association into a reproducible search process.

## Contents

1. Three-layer model
2. Stable identifiers
3. Build the problem-structure map
4. Scan source domains
5. Admit mature methods
6. Match problems to methods
7. Hand off to method transplantation
8. Coverage and stopping rules
9. Anti-patterns

## Three-Layer Model

```text
Target problem or established target task
        x
Cross-domain mature-method atlas
        ↓ structural matching
Match and negative-match register
        ↓ selected pair
Method-transplantation validation
        ↓
Provisional research candidate
```

Do not match domain labels directly. Match the target problem or task structure to the structure a method is designed to solve.

Combination innovation supports two entry routes. Read [evaluation-guide.md](evaluation-guide.md) before matching:

- **Problem-led**: start from a verified target limitation and test whether it materially exists.
- **Method-led effect scan**: start from a verified mature capability, then search established target tasks where a target-specific adaptation could deliver measurable benefit over a strong native baseline.

Method-led does not mean trend-led. Reject a method selected only because it is fashionable, recent, or easy to attach.

## Stable Identifiers

| Entity | Format | Example |
|---|---|---|
| Target problem | `PROB-TARGET-NNN` | `PROB-BRB-001` |
| Mature method | `METHOD-DOMAIN-NNN` | `METHOD-CTRL-001` |
| Domain scan | `SCAN-YYYY-NNNN` | `SCAN-2026-0001` |
| Match attempt | `MATCH-YYYY-NNNN` | `MATCH-2026-0001` |

Never recycle identifiers. A rejected match remains useful evidence.

## Build The Problem-Structure Map

For the problem-led route, start from the target field, not from fashionable source methods. For the method-led effect route, begin with a verified method card but require an established target task, outcome, and native baseline before creating a match.

For each target problem, record:

- Observable symptom and affected artifact
- Scientific or decision consequence
- Abstract structure, such as dependence, delayed feedback, strategic reporting, combinatorial growth, distribution shift, or constrained verification
- Current workaround and why it is insufficient
- Constraints that a valid solution must preserve
- Evidence supporting the problem's reality
- Status and priority

Do not create a target problem merely to justify a source method.

## Scan Source Domains

Use domains as a coverage schedule. Start with a bounded set and expand only when target structures justify it.

Recommended initial families:

| Code | Source domain | Typical structures |
|---|---|---|
| `STAT` | Statistical learning and robust statistics | estimation, calibration, contamination, finite-sample uncertainty |
| `CTRL` | Control and dynamical systems | feedback, stability, observability, online adaptation |
| `INFO` | Information theory | compression, information preservation, rates, coding limits |
| `OR` | Optimization and operations research | constrained allocation, scheduling, combinatorial search |
| `CAUS` | Causal inference | intervention, confounding, transportability, counterfactuals |
| `FORM` | Formal methods | invariants, reachability, abstraction, certification |
| `GAME` | Game theory and mechanism design | strategic behavior, incentives, distributed decisions |
| `MEAS` | Measurement science and psychometrics | latent constructs, reliability, validity, measurement invariance |

For each scan:

1. State the target structures motivating the scan.
2. Search authoritative handbooks, tutorials, reviews, standards, and canonical papers.
3. Record databases, queries, languages, date range, and inclusion criteria.
4. Extract only methods that meet the maturity gate.
5. Record excluded methods and the reason when they are likely to be proposed again.
6. Stop at saturation or the declared budget and record which occurred.

## Admit Mature Methods

A method enters the atlas only when all required fields are supported:

| Gate | Required evidence |
|---|---|
| Stable identity | Unambiguous name, aliases, and source domain |
| Structural purpose | Clear statement of the problem structure it solves |
| Formal contract | Inputs, outputs, assumptions, and guarantees or intended behavior |
| Maturity | Canonical source plus independent use, review, standard, or established implementation |
| Failure knowledge | Known limitations, invalid regimes, or common misuse |
| Traceability | Stable identifiers or URLs and a verification date |

Do not admit a method based only on an AI-generated description or one unverified paper.

## Match Problems To Methods

Evaluate each pair through four gates:

1. **Structural fit**: Does the method solve the same abstract structure rather than merely sharing terminology?
2. **Assumption compatibility**: Which source assumptions hold, fail, or remain unknown in the target system?
3. **Necessity and alternatives**: Does a native target-field method already solve the problem adequately?
4. **Non-trivial adaptation**: Is a scientifically meaningful adaptation required, or only implementation glue?

Choose the primary validation route before writing the bridge statement.

Problem-existence route:

> In the target field, problem P has structure S. Method M addresses S under assumptions A. The target setting violates or extends B, so contribution C is required. Result R would distinguish C from native baseline N.

Effect-efficacy route:

> In target task T, baseline N is evaluated by outcome R. Method M improves structurally similar tasks under assumptions A. Target constraint B requires adaptation C. C must beat N and direct transfer M by a meaningful margin while keeping cost K acceptable.

If the statement cannot be completed with evidence, record a negative or deferred match instead of generating an idea.

## Hand Off To Method Transplantation

Combination innovation ends after it discovers and records a promising pair. Method transplantation then performs a stage-calibrated transfer analysis. During brainstorming and `初筛`, record only the borrowed capability, a plausible target-specific innovation hook, why direct transfer may be insufficient, and the minimum discriminating probe. During `评估中`, complete the deeper analysis:

- Construct-to-construct mapping
- Preserved, violated, and unknown assumptions
- Native target-field alternatives
- Selected validation route
- Existence/severity test or controlled effect comparison
- Required theoretical or algorithmic adaptation
- Minimum discriminating probe

Only after the lightweight handoff should a pair enter the idea inbox or receive `初筛` status. Do not require the full algorithm or theory before provisional promotion; do require it before the idea advances beyond evaluation.

## Coverage And Stopping Rules

Track coverage at three levels:

- Domain coverage: unscanned / partial / saturated / stale
- Method-card coverage: candidate / verified / deprecated
- Match coverage: untested / promising / negative / deferred / promoted

A domain scan is saturated when two consecutive search iterations add no new method family, important assumption, or failure mode relevant to the declared target structures. Mark scans stale after material reviews, standards, or methods appear.

Prefer a small verified atlas over an exhaustive unverified catalog. Start with 8 domains and 3-5 verified methods per domain.

## Anti-Patterns

- Domain-name Cartesian products such as "physics + BRB" without a shared structure
- Trend lists without source verification
- Treating a mature source method as evidence that the target field needs it
- Requiring a new target-field defect when the central claim is an effect improvement on an established task
- Claiming improvement without a strong native baseline, direct-transfer control, ablation, uncertainty, or resource accounting
- Ignoring native target-field baselines
- Hiding failed mappings instead of recording negative matches
- Reusing a method's name while violating its defining assumptions
- Claiming novelty before running the novelty protocol
