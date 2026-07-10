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

Use combination innovation as a systematic discovery process across the target problem-structure map and a verified cross-domain method atlas. Read [cross-domain-method-atlas.md](cross-domain-method-atlas.md) before running a broad combination scan.

### Procedure

1. Select one or more verified target problems and abstract away field-specific terminology.
2. Select a bounded source-domain scan from the coverage plan.
3. Search authoritative sources and extract only methods that pass the maturity gate.
4. Match problem structures to method purposes.
5. Reject pairs that share only labels, violate defining assumptions, duplicate native solutions, or require only implementation glue.
6. Record promising, negative, and deferred matches.
7. Send promising pairs to Method 3 for deep transfer validation.

Require this bridge sentence:

> Target problem P has structure S; method M addresses S under assumptions A; the target setting violates or extends B, so adaptation C is required; outcome R distinguishes C from native baseline N.

Output: coverage-aware scan record, verified method cards, match/negative-match records, and a shortlist for Method 3. Do not output a novelty claim.

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

Deeply validate one promising problem-method pair discovered by Method 1 or another evidence-backed route. Method 3 does not perform broad random scanning.

### Procedure

1. Map source constructs, operations, inputs, outputs, and guarantees to target constructs.
2. Classify every important source assumption as preserved, violated, or unknown.
3. Compare against native target-field methods and the no-transplant baseline.
4. Design a negative-transfer test that would show the source method is inappropriate.
5. Specify the theoretical, algorithmic, or measurement adaptation required by violated assumptions.
6. Define the minimum discriminating probe and stop criterion.

Output: construct mapping, assumption ledger, native alternatives, negative-transfer test, required adaptation, and minimum probe. Promote the pair only when the adaptation yields generalizable knowledge.

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
| Verified target problem plus a mature method with the same abstract structure | Combination innovation |
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
