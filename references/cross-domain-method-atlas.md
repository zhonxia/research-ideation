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
Target problem-structure map
        x
Cross-domain mature-method atlas
        ↓ structural matching
Match and negative-match register
        ↓ selected pair
Method-transplantation validation
        ↓
Provisional research candidate
```

Do not match domain labels directly. Match a target problem's abstract structure to the structure a method is designed to solve.

## Stable Identifiers

| Entity | Format | Example |
|---|---|---|
| Target problem | `PROB-TARGET-NNN` | `PROB-BRB-001` |
| Mature method | `METHOD-DOMAIN-NNN` | `METHOD-CTRL-001` |
| Domain scan | `SCAN-YYYY-NNNN` | `SCAN-2026-0001` |
| Match attempt | `MATCH-YYYY-NNNN` | `MATCH-2026-0001` |

Never recycle identifiers. A rejected match remains useful evidence.

## Build The Problem-Structure Map

Start from the target field, not from fashionable source methods.

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

Require this bridge statement:

> In the target field, problem P has structure S. Method M addresses S under assumptions A. The target setting violates or extends B, so contribution C is required. Result R would distinguish C from native baseline N.

If the statement cannot be completed with evidence, record a negative or deferred match instead of generating an idea.

## Hand Off To Method Transplantation

Combination innovation ends after it discovers and records a promising pair. Method transplantation then performs the deep transfer analysis:

- Construct-to-construct mapping
- Preserved, violated, and unknown assumptions
- Native target-field alternatives
- Negative-transfer and failure tests
- Required theoretical or algorithmic adaptation
- Minimum discriminating probe

Only after this handoff should a pair enter the idea inbox.

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
- Ignoring native target-field baselines
- Hiding failed mappings instead of recording negative matches
- Reusing a method's name while violating its defining assumptions
- Claiming novelty before running the novelty protocol
