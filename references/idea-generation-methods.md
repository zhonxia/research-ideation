# Idea Generation Methods

Use these eleven methods to create candidates. Generation produces hypotheses and contribution sketches, not novelty claims.

## Contents

1. Combination innovation
2. Weakness triangulation
3. Method transplantation
4. Theory deep dive
5. Boundary and assumption challenge
6. Citation-chain gap mining
7. Goal-driven reverse engineering
8. Contradiction mapping
9. Counterexample-first research
10. Measurement-first research
11. Regime and phase mapping
12. Method selection
13. Screening and deduplication

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

## 8. Contradiction Mapping

Start when credible studies, definitions, theories, or experiments appear to support incompatible conclusions.

1. Express each result as `claim | conditions | construct definition | data | method | metric`.
2. Normalize terminology and determine whether both studies measured the same construct.
3. Separate genuine contradiction from differences in population, assumptions, preprocessing, optimization, or evaluation.
4. Propose the smallest moderator or boundary condition that could explain both results.
5. Design a discriminating study in which the competing explanations make different predictions.

If normalization removes the contradiction, downgrade the candidate from a new mechanism to a synthesis, benchmark, or reporting-standard contribution.

Output: contradiction matrix, candidate moderator, unifying hypothesis, and discriminating test.

BRB/ER example: two weighting or reliability methods reverse their ranking under different conflict levels. Map the hidden conditions and test whether evidence dependence explains the reversal.

## 9. Counterexample-First Research

Start from a property that is assumed, informally claimed, or proved only under narrow conditions.

1. State the property as a falsifiable proposition.
2. Define the smallest valid instance: fewest rules, attributes, states, or evidence sources.
3. Search systematically using enumeration, symbolic solving, adversarial optimization, or property-based testing.
4. Minimize any counterexample so the failure mechanism is interpretable.
5. Infer the missing condition, revise the conjecture, or design a repair.
6. Re-run the search against the revised claim.

This differs from boundary and assumption challenge: it begins with an executable falsification artifact rather than an assumption list.

Output: minimal counterexample or bounded negative search, failure mechanism, revised proposition, and repair test.

BRB/ER example: find the smallest rule base in which locally monotone rules produce a non-monotone aggregate, then derive sufficient conditions for global monotonicity.

## 10. Measurement-First Research

Start when progress is limited by an ambiguous construct, weak proxy, unstable metric, or benchmark that rewards the wrong behavior.

1. Define the target construct and the decision it is meant to support.
2. Audit existing proxies for content, construct, criterion, and ecological validity.
3. Identify known-groups, adversarial, invariance, and test-retest checks the measure should pass.
4. Design the smallest new metric, instrument, benchmark, or annotation protocol that closes the validity gap.
5. Test whether conclusions or model rankings change under the improved measure.

Do not create a new metric merely because it correlates with a preferred method. Require a validation argument independent of the proposed model.

Output: construct definition, validity threats, measurement design, validation protocol, and consequence for prior conclusions.

BRB/ER example: replace parameter-count or rule-readable proxies for interpretability with a human comprehension and decision-calibration instrument.

## 11. Regime And Phase Mapping

Start when a method may behave qualitatively differently across scale, noise, dependence, sparsity, conflict, or resource conditions.

1. Select two to four theoretically meaningful axes and define their ranges.
2. Build a factorial, logarithmic, or adaptive grid over the regimes.
3. Measure not only average performance but stability, calibration, computation, failure probability, and structural behavior.
4. Locate crossovers, discontinuities, collapse regions, or changes in the best method.
5. Form a mechanism-level hypothesis for each boundary and test it on held-out regimes.
6. Derive a scaling law, boundary theorem, or method-selection rule when evidence supports it.

Use `phase transition` only when discontinuous or critical behavior is demonstrated. Otherwise call the result a regime map or crossover analysis.

Output: regime map, critical boundaries, explanatory hypothesis, and method-selection rule.

BRB/ER example: map rule count, evidence dependence, and weight perturbation to identify where ER calibration collapses and which robust variant dominates.

## Method Selection

| Available signal | Prefer |
|---|---|
| New technology, theory, data regime, or domain | Combination innovation |
| Repeated practical or empirical weakness | Weakness triangulation |
| Mature construct in another field | Method transplantation |
| Missing mathematical foundation | Theory deep dive |
| Unrealistic default assumption | Boundary and assumption challenge |
| Explicit unresolved statement with a citation history | Citation-chain gap mining |
| Concrete outcome blocked by missing knowledge | Goal-driven reverse engineering |
| Credible results that cannot all be true under one model | Contradiction mapping |
| Accepted property that may fail on a small instance | Counterexample-first research |
| Weak construct, proxy, metric, or benchmark | Measurement-first research |
| Behavior changes across scale or operating conditions | Regime and phase mapping |

Use more than one method only when each contributes a different artifact. Do not relabel one candidate eleven times.

## Screening And Deduplication

Before promotion from the inbox:

- Compare titles, aliases, questions, mechanisms, and intended contributions.
- Merge candidates that differ only in wording or application domain.
- Link variants under a parent idea when they test the same core claim.
- Reject label combinations with no real problem or scientific uncertainty.
- Assign a stable idea ID only after deduplication.
- Apply hard gates before detailed literature work.

Do not label an idea novel during generation. Record promising search targets as local coverage gaps until the novelty protocol is completed.
