# Idea Generation Methods

**Priority: default to the effect-efficacy route** (method transplantation, combination innovation). Most published SCI papers follow the "borrow a mature method, adapt it to the target, compare against baselines" pattern. Only switch to the problem-existence route when the central claim is that a target assumption, guarantee, or workflow actually fails.

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

Read [evaluation-guide.md](evaluation-guide.md) and choose one primary route for each candidate:

- **Problem-existence**: the contribution depends on showing that a target limitation materially exists.
- **Effect-efficacy**: the target task is already legitimate, and the contribution depends on an adapted mature method outperforming current practice.

### Procedure

1. Choose the validation route before defining the probe.
2. For problem-existence, select a verified target problem and abstract away field-specific terminology.
3. For effect-efficacy, select an established target task, outcome, and strong native baseline; a newly proven target defect is not required.
4. Select a bounded source-domain scan and extract only methods that pass the maturity gate.
5. Match target structures to method purposes.
6. Reject pairs that share only labels, violate defining assumptions, duplicate native solutions, or require only implementation glue.
7. Record promising, negative, and deferred matches, including the selected validation route.
8. Send promising pairs to Method 3 for deep transfer validation.

For problem-existence, require this bridge sentence:

> Target problem P has structure S; method M addresses S under assumptions A; the target setting violates or extends B, so adaptation C is required; outcome R distinguishes C from native baseline N.

For effect-efficacy, require this bridge sentence:

> Target task T currently uses baseline N and values outcome R; mature method M improves structurally similar tasks under assumptions A; target-specific constraint B requires adaptation C; C must outperform both N and direct transfer M by a meaningful margin while keeping cost K acceptable.

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

Validate one promising problem-method pair discovered by Method 1 or another evidence-backed route. Method 3 does not perform broad random scanning. Match the depth to the lifecycle stage: use a lightweight transfer sketch during brainstorming and `初筛`, then perform the full analysis during `评估中`.

### Procedure

1. Map source constructs, operations, inputs, outputs, and guarantees to target constructs.
2. Classify every important source assumption as preserved, violated, or unknown.
3. Compare against native target-field methods and the no-transplant baseline.
4. Preserve the selected validation route; do not automatically turn an effect-efficacy candidate into a problem-existence study. **The effect-efficacy route is the default** — only fall back to problem-existence when the central contribution depends on proving that a target limitation exists.
5. For problem-existence, design an existence/severity test before investing in the solution.
6. For effect-efficacy, compare the native baseline, direct transfer, adapted method, and relevant external baseline; define the minimum meaningful improvement, ablations, uncertainty, and resource controls.
7. Specify the theoretical, algorithmic, measurement, or design adaptation required by target constraints.
8. Define the route-aligned minimum discriminating probe and stop criterion.

For brainstorming and `初筛`, the minimum output is:

- borrowed capability and target task;
- a credible reason direct transfer may be insufficient;
- one or two candidate innovation hooks at the mechanism-family level;
- direct-transfer control, minimum probe, and stop condition.

Do not require an exact objective, solver, theorem, or proof at this stage. Do not treat direct application as the innovation itself.

For `评估中`, output the full validation route, construct mapping, assumption ledger, native alternatives, concrete adaptation, comparison design, and minimum probe. Advance to `进行中` only when the adaptation is supported as generalizable knowledge or a reproducible, meaningful effect beyond extra resources.

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

Each method has a **weight**. Higher weight = more likely to be chosen in a probabilistic draw. This ensures common routes are used often but novel routes are never starved.

| Method | Weight | Available signal | Validation route |
|---|---|---|---|
| Method transplantation | 30 | Mature method in another field + target task | **Effect-efficacy (default)** |
| Combination innovation | 25 | Cross-domain method match + target structure | **Effect-efficacy (default)** |
| Boundary and assumption challenge | 15 | Unrealistic default assumption | Problem-existence |
| Weakness triangulation | 8 | Repeated practical or empirical weakness | Problem-existence |
| Theory deep dive | 10 | Missing mathematical foundation | Problem-existence |
| Counterexample-first research | 5 | Accepted property that may fail on a small instance | Problem-existence |
| Contradiction mapping | 3 | Credible results cannot all be true under one model | Problem-existence |
| Citation-chain gap mining | 2 | Explicit unresolved statement with citation history | Problem-existence |
| Goal-driven reverse engineering | 1 | Concrete outcome blocked by missing knowledge | Mixed |
| Measurement-first research | 1 | Weak construct, proxy, metric, or benchmark | Problem-existence |
| Regime and phase mapping | <1 | Behavior changes across scale or conditions | Problem-existence |

**How to use:** Imagine a roulette wheel where each method occupies a slice proportional to its weight. Spin once to select the primary method, then spin again for a secondary method. This keeps common routes frequent while ensuring every method gets tried eventually.

**Default to the effect-efficacy route** (rows marked "Effect-efficacy (default)"). Only use problem-existence when the research contribution depends on proving that a target limitation exists.

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
