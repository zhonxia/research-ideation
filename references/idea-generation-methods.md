# Idea Generation Methods

Detailed reference for each of the 6 brainstorming methods. Load this file when generating ideas.

---

## Method 1: Combination Innovation (组合创新)

Combine your core research topic with:
- **New technologies**: LLM, GNN, RL, federated learning, contrastive learning, meta-learning, diffusion models, transformers, variational inference, optimal transport...
- **New domains**: Healthcare, finance, autonomous driving, industrial IoT, cybersecurity...

### How to apply
1. List all technologies adjacent to your field
2. List all application domains where your method could apply
3. For each pair, ask: "What if I combined [your method] with [new tech] in [new domain]?"
4. Check if the combination has been done before

### Example
- "What if I combined [my method] with reinforcement learning?" → Novel hybrid approach
- "What if I used contrastive learning to learn better feature representations for [my method]?" → Representation-enhanced approach

---

## Method 2: Fix Weaknesses (补短板)

### How to apply
1. Read 3-5 recent survey papers in your field
2. Extract all "limitations" and "future work" sections
3. Identify recurring weaknesses across multiple papers
4. Each weakness = one potential idea

### Common weakness patterns
- Computational complexity too high → efficiency improvement
- Only tested on small datasets → scalability
- Static model, can't adapt → online/incremental learning
- Requires too much labeled data → few-shot/active learning
- Poor interpretability → explainability methods
- Single-source data → multi-source/multi-modal fusion

---

## Method 3: Transplant Methods (搬方法)

Two directions:

### Direction A: Other fields → Your field
1. Identify a bottleneck in your research area
2. Search mature fields (physics, mathematics, economics, biology) for theories that describe similar phenomena
3. Adapt the theory to your problem

### Direction B: Your unique advantage → Other fields
1. What is your method uniquely good at?
2. Which other fields face problems your method can solve?
3. Adapt your method to their problem

### Examples of transplanted theories
- Information Bottleneck → Model compression
- Optimal Transport → Cross-domain adaptation
- Variational Inference → Posterior uncertainty estimation
- Information Geometry → Geometric interpretation of learning algorithms
- Fisher Information → Measuring parameter importance

---

## Method 4: Theory Deep Dive (理论深挖)

### Questions to ask
- What mathematical properties of my method remain unproven?
- Can the boundary conditions of existing theorems be relaxed?
- Is there a simpler proof for known results?
- What happens at the asymptotic limits (n→0, n→∞)?
- Are there connections to other mathematical frameworks I haven't explored?
- What are the identifiability conditions for my model?
- Is there a non-convex generalization of my method?
- Does my method satisfy fundamental statistical laws (e.g., law of large numbers, central limit theorem)?

---

## Method 5: Boundary Limit Method (边界极限法)

Challenge the default assumptions in existing research.

### How to apply
1. List all "obvious" assumptions in your field
2. For each assumption, ask: "What if this isn't true?"
3. If breaking the assumption leads to a meaningful research problem, it's an idea

### Assumption-breaking template

| Default Assumption | Reality | New Idea |
|-------------------|---------|----------|
| Components are independent | Components interact | Component-level interaction modeling |
| Combination is convex | Non-convex fusion possible | Non-convex fusion methods |
| Model is discriminative | Could be generative | Generative approach to the problem |
| Model structure is fixed | Structure could be continuous | Differentiable structure learning |
| Data is perfect | Noisy, missing, uncertain | Robust method under data corruption |

---

## Method 6: Literature Deconstruction (文献解构法)

Mine "Future Work" sections from top papers for research directions.

### How to apply
1. Find the 3-5 most cited recent papers in your field
2. Read their Discussion and Future Work sections carefully
3. Extract specific open problems (not vague "more research is needed")
4. Cross-reference: has anyone actually addressed this gap since the paper was published?

### Where to look
- "Although our method works for X, it fails when Y because of Z" → Solve Z
- "Future work should consider..." → Do that future work
- "We assumed that..." → Break that assumption (overlaps with Method 5)
- Survey paper's "Research gaps" table → Fill those gaps

---

## Method 7: Reverse-Engineering Research (反向推导研究法)

> **Core insight (preserved verbatim)**
>
> Originality does not come from "having a goal first." It comes from:
> **In pursuing your goal, you are forced to enter territory others have not yet explored — or not explored sufficiently.**
> That is the most valuable thing about reverse-engineering research.

### The Method

Start not from a research gap, but from a **concrete goal you need to achieve** — a system you want to build, a problem you want to solve, a performance bar you want to hit.

Then ask: "What theoretical foundations, algorithmic primitives, or data structures do I NEED to exist in order to reach this goal?"

If those foundations don't exist (or don't exist in sufficient form), **that's your research contribution** — not invented to be novel, but necessary to fulfill a real purpose.

### Four Steps

1. **Define a concrete goal** — not a research direction, but a real, verifiable outcome
2. **Decompose backwards** — list every existing result your goal depends on; where does the chain break?
3. **Validate necessity** — can you reach the goal without filling this gap? Yes → engineering; No → contribution
4. **Write the motivation** — "To achieve X, this gap *must* be filled; existing methods cannot do it"

### Examples

| Concrete Goal | Gap (chain breaks here) | Contribution |
|---------------|------------------------|--------------|
| Prove BRB convergence under ρ-mixing samples | No sample-complexity bound for belief updates under mixing coefficients | ρ-mixing convergence theorem for BRB |
| Train BRB in federated private-data settings | No distributed update rule compatible with BRB's non-linear activation | Federated BRB optimization theory |
| Keep ER fusion calibrated under adversarial weight perturbation | No perturbation bound on belief combination under adversarial weight shifts | Robustness theory for ER evidence weights |

### Why this generates original ideas

- **Necessity-driven novelty**: You enter unexplored territory because your path *runs through* it — reviewers feel the inevitability
- **Motivation is self-justifying**: The contribution is forced by the goal, not assembled to look novel
- **Paper cohesion**: Every component traces back to one goal; no "we also tried X" digressions
- **Immune to "why not use Y"**: If Y cannot achieve your stated goal, the objection collapses

### Common mistakes

- **Goal too vague** ("make BRB better") → decomposition won't terminate at a specific gap
- **Goal achievable with existing tools** → no genuine gap emerges; only engineering work remains
- **Goal fabricated retroactively** → method fails; reviewers can tell

---

## Novelty Verification Checklist

After generating ideas with any method, verify novelty:

- [ ] **Check `05-文献库/` first** — does any literature note already cover this direction?
- [ ] Web search with 3+ keyword combinations (English + Chinese)
- [ ] Check recent survey papers (last 2-3 years) for mentions
- [ ] Check user's knowledge base (if applicable)
- [ ] Search for adjacent work that partially overlaps
- [ ] Distinguish "exact match" from "related but different"
- [ ] Record every check in `01-灵感收集/evidence-log.md` with date, query/source, key results, conclusion, and confidence
- [ ] Copy relevant evidence rows into the evaluation white paper's embedded Search Log
- [ ] Link each novelty claim to one or more evidence rows
- [ ] If novel, add to `索引.md` gap list for future reference

## Evidence Log Standard

Every novelty claim must be backed by a row in the evidence log. Use this row format:

| Date | Idea | Claim | Query / Source | Channel | Key Results | Conclusion | Confidence | Notes |
|------|------|-------|----------------|---------|-------------|------------|:----------:|-------|
| YYYY-MM-DD | [Idea] | [Narrow claim] | [Query/source] | Web / `05-文献库` / survey / knowledge base | [Specific findings] | Exact match / partial overlap / adjacent only / no close match | 0.0-1.0 | [Caveats] |

Do not write "confirmed novel" unless the evidence is broad and strong. Prefer: "No exact match found in the searched sources as of YYYY-MM-DD."
