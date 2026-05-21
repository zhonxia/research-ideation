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
- "What if I combined BRB with reinforcement learning?" → BRB+RL (novel)
- "What if I used contrastive learning to learn better BRB rule activations?" → BRB+Contrastive Learning (novel)

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
- Information Bottleneck → Rule compression
- Optimal Transport → Cross-domain rule transfer
- Variational Inference → Posterior uncertainty estimation
- Information Geometry → Geometric interpretation of ER rules
- Fisher Information → Measuring rule contribution

---

## Method 4: Theory Deep Dive (理论深挖)

### Questions to ask
- What mathematical properties of my method remain unproven?
- Can the boundary conditions of existing theorems be relaxed?
- Is there a simpler proof for known results?
- What happens at the asymptotic limits (n→0, n→∞)?
- Are there connections to other mathematical frameworks I haven't explored?

### For ER/BRB specifically
- Does ER combination satisfy the law of large numbers?
- What are the identifiability conditions for BRB parameters?
- Is there a non-convex generalization of ER combination?
- What is the information-geometric interpretation of ER rules?

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
| Rules are independent | Rules interact | Rule-level attention mechanism |
| ER combination is convex | Non-convex fusion possible | Non-convex evidence fusion |
| Model is discriminative | Could be generative | Generative BRB |
| Rules are fixed IF-THEN | Rules could be continuous | Differentiable rule structure |
| Data is perfect | Noisy, missing, uncertain | Robust BRB under data corruption |

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

## Novelty Verification Checklist

After generating ideas with any method, verify novelty:

- [ ] Web search with 3+ keyword combinations (English + Chinese)
- [ ] Check recent survey papers (last 2-3 years) for mentions
- [ ] Check user's knowledge base (if applicable)
- [ ] Search for adjacent work that partially overlaps
- [ ] Distinguish "exact match" from "related but different"
- [ ] Document what you found (even if nothing) in the evaluation
