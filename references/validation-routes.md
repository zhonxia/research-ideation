# Validation Routes For Combination Innovation

Choose the primary validation route before designing a probe. Falsifiability does not imply that every idea must first prove a new target-field problem exists.

## Contents

1. Route selection
2. Problem-existence route
3. Effect-efficacy route
4. Shared scientific requirements
5. Route-specific probe templates

## Route Selection

Use the route that matches the central claim:

| Central claim | Primary route | Main question |
|---|---|---|
| The target method fails, becomes invalid, or suffers a measurable limitation under condition Z | Problem-existence | Does the claimed problem materially affect the target? |
| An adapted mature method improves a target task over the current practice | Effect-efficacy | Does the adaptation produce a meaningful benefit at acceptable cost? |

Do not rewrite an effect claim as a problem-existence claim merely to make the adaptation look necessary. A legitimate target task with an improvable baseline is sufficient motivation for the effect-efficacy route.

When generating a batch of combination ideas, consider both routes. Unless the evidence or user request clearly favors one route, do not make every candidate use the same route.

## Problem-Existence Route

Use this route when the research contribution depends on showing that a target-field assumption, guarantee, metric, or workflow actually fails.

Required fields:

- Claimed problem and affected population or regime
- Observable consequence and severity measure
- Native workaround and why it may be insufficient
- Existence/severity test
- Positive and negative controls
- Stop or reframe condition if the effect is absent or negligible

Primary validation:

> Show that problem P materially affects target T under condition Z.

Do not start solution development before a cheap existence or severity probe when the entire contribution disappears if P is absent.

## Effect-Efficacy Route

Use this route when the target task is already legitimate and the main contribution is an adapted method that may improve it. Do not require a new failure phenomenon before testing the method.

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

Use this minimum comparison set when feasible:

| Arm | Purpose |
|---|---|
| Native target-field baseline N | Tests whether the proposal improves current practice |
| Direct transfer M | Tests whether adaptation is actually necessary |
| Adapted method C | Measures the proposed contribution |
| Strong non-target-field baseline | Prevents target-field insularity when an external baseline is relevant |

An average improvement alone is insufficient when it comes from more parameters, more data, more tuning, or more compute. Normalize resources or report the tradeoff explicitly.

## Shared Scientific Requirements

Both routes must still establish:

1. Structural fit rather than label similarity.
2. A contribution beyond interface glue.
3. Comparison with credible native alternatives.
4. A route-aligned falsification criterion.
5. Generalizable knowledge: mechanism, design rule, boundary, or reproducible effect rather than a one-dataset win.

The adaptation need not repair a newly discovered defect. It may encode target constraints, exploit target structure, reduce cost, or improve an established outcome.

## Route-Specific Probe Templates

### Problem-Existence Probe

```text
Claimed problem:
Affected condition:
Existence/severity metric:
Positive control:
Negative control:
Continue threshold:
Stop or reframe threshold:
```

### Effect-Efficacy Probe

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
