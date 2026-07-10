# Scoring v2

Apply gates before scoring. Scores support portfolio decisions; they do not measure scientific truth.

## Hard Gates

| Gate | Pass condition |
|---|---|
| Problem significance | A credible stakeholder, scientific theory, or decision would benefit from the answer |
| Falsifiability / answerability | A result could reject, bound, or materially revise the claim |
| Resource access | A plausible path exists to required data, premises, tools, expertise, time, and permissions |
| Ethics and governance | Risks are acceptable or have a credible approval and mitigation path |

Do not calculate a weighted score when a critical gate is `No`. Convert `Unknown` into a time-bounded probe.

## Weighted Dimensions

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

## Confidence

Record Low, Medium, or High confidence for every dimension:

- **Low**: assumption or preliminary evidence dominates.
- **Medium**: useful evidence exists but an important uncertainty remains.
- **High**: multiple independent evidence sources or a completed probe support the score.

Run a sensitivity check using plausible low/high scores for the least certain dimensions. If the decision changes, choose `Probe first` rather than pretending the point estimate is decisive.

## Urgency Metadata

Urgency does not contribute to the weighted score. Record:

- Competitive pressure: Low / Medium / High
- External deadline or opportunity window
- Cost of waiting
- Next review date

Use urgency to schedule work after quality and expected value are assessed.

## Legacy Scores

Keep legacy `/30` totals labeled as `v1`. Do not multiply them into a v2 score. Re-score an idea under v2 before comparing it with new records.
