# Idea Generation Methods

Use these seven methods to create candidates. Generation produces hypotheses and contribution sketches, not novelty claims.

## Contents

1. Combination innovation
2. Weakness triangulation
3. Method transplantation
4. Theory deep dive
5. Boundary and assumption challenge
6. Citation-chain gap mining
7. Goal-driven reverse engineering
8. Screening and deduplication

## 1. Combination Innovation

Combine a core method or phenomenon with a technology, theory, data regime, or domain.

Ask:

- Does the combination solve a real incompatibility or merely join fashionable labels?
- What scientific question becomes answerable only after the combination?
- Which component is the contribution rather than implementation glue?

Output: one precise research question, the necessary interaction, and a non-combination baseline.

## 2. Weakness Triangulation

Look for the same limitation in multiple independent evidence types:

- Reviews and meta-analyses
- Empirical failure reports
- Practitioner or stakeholder needs
- Replication failures
- Dataset or measurement limitations

Require at least two evidence types before treating a weakness as a strong candidate. Repeated author boilerplate alone is weak evidence.

Output: affected population/system, observed consequence, and why current workarounds fail.

## 3. Method Transplantation

Map a mature construct from another field onto an isomorphic problem.

Check:

1. Which assumptions make the source method valid?
2. Do those assumptions hold in the target field?
3. What adaptation is scientifically non-trivial?
4. Which target-field baseline is stronger than a naive transplant?

Output: source construct, target construct, preserved assumptions, broken assumptions, and required adaptation.

## 4. Theory Deep Dive

Search for missing foundations:

- Existence, uniqueness, identifiability, consistency, or convergence
- Finite-sample or approximation guarantees
- Boundary behavior and relaxed assumptions
- Robustness, stability, calibration, or uncertainty
- Connections to established mathematical frameworks

Output: theorem-level statement or formal question, required assumptions, and a counterexample or falsification route.

## 5. Boundary And Assumption Challenge

List default assumptions, then stress each one:

| Default | Boundary or violation | Candidate question |
|---|---|---|
| Independent observations | Dependence or feedback | What remains identifiable or stable? |
| Clean complete data | Missing, noisy, adversarial data | What guarantee survives corruption? |
| Fixed structure | Adaptive or continuous structure | Can structure be learned without losing validity? |
| Average-case behavior | Worst-case or tail behavior | What can be guaranteed in critical regimes? |

Output: challenged assumption, realistic violating regime, and measurable consequence.

## 6. Citation-Chain Gap Mining

Start from recent high-relevance papers, reviews, standards, or replications. Extract a specific unresolved claim, then trace forward citations to determine whether it remains unresolved.

This differs from weakness triangulation: it verifies the history and current status of one explicit gap through a citation chain rather than aggregating recurring problems.

Output: originating citation, exact gap statement, forward-citation coverage, and current status.

## 7. Goal-Driven Reverse Engineering

Start from a concrete, verifiable outcome and decompose backward:

1. Define the outcome and success criterion.
2. List every theoretical, methodological, data, and system dependency.
3. Mark where existing knowledge becomes insufficient.
4. Test necessity: can the outcome be reached without filling the gap?
5. Test scientific value: would filling the gap yield generalizable knowledge rather than one-off engineering?
6. Test feasibility: why might the missing result be absent?

Output: goal, broken dependency, necessity argument, generalizable contribution, and cheapest invalidating probe.

## Screening And Deduplication

Before promotion from the inbox:

- Compare titles, aliases, questions, mechanisms, and intended contributions.
- Merge candidates that differ only in wording or application domain.
- Link variants under a parent idea when they test the same core claim.
- Reject label combinations with no real problem or scientific uncertainty.
- Assign a stable idea ID only after deduplication.
- Apply hard gates before detailed literature work.

Do not label an idea novel during generation. Record promising search targets as local coverage gaps until the novelty protocol is completed.
