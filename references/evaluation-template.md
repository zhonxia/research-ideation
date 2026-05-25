# Evaluation White Paper Template

Use this template when writing an evaluation white paper for a research idea.

---

```markdown
# [Idea Name] Technical Evaluation White Paper v1.0

**Created**: YYYY-MM-DD  
**Type**: Initial Screening  
**Status**: Under Evaluation  

---

## 1. Executive Summary

**Core Question**: [One sentence describing the research question]

**Findings**:
- [Key finding 1]
- [Key finding 2]
- [Key finding 3]

**Score**: **XX.X / 30**

| Dimension | Score | Notes |
|-----------|:-----:|-------|
| Novelty | X.X | |
| Technical Feasibility | X.X | |
| Experimental Verifiability | X.X | |
| Publication Feasibility | X.X | |
| Fit with Current Research | X.X | |
| Urgency | X.X | |

---

## 2. Idea Definition

**[Idea Name]**: [Precise definition in one paragraph]

| Approach | Core Idea | Analogy |
|----------|-----------|---------|
| A. [Name] | [Description] | [Comparison] |
| B. [Name] | [Description] | [Comparison] |

**Recommended Priority**: [A > B > C]

---

## 3. Research Status

### 3.1 Existing Work on Your Method's Side

[What has the field already done? What methods exist?]

| Method | Type | Sequential? |
|--------|------|:-----------:|
| GA | Evolutionary | ✗ |
| PSO | Swarm | ✗ |

### 3.2 Adjacent Work That Almost Reaches This Idea

| Work | Distance | Analysis |
|------|:--------:|----------|
| Paper 1 | Close | [Why it's close but different] |
| Paper 2 | Medium | [Why it's close but different] |

### 3.3 Knowledge Base / Literature Library Verification

- [ ] Checked `05-文献库/` — found / not found
- [ ] Checked external knowledge base (if applicable)
- [ ] Document what was found (even if nothing)

---

## 4. Novelty Verification

### Search Log

| Query | Results | Verdict |
|-------|---------|---------|
| "keyword1" "keyword2" | X results | [Novel/Collision] |
| "keyword3" "keyword4" | X results | [Novel/Collision] |

### Verdict

- [ ] Exact combination has been done before
- [ ] Partial overlap with existing work (specify)
- [x] Confirmed novel (no direct or close competitors)

---

## 5. Technical Feasibility

### Approach A: [Name]

**Problem Formulation**:
- State: [s_t = ...]
- Action: [a_t = ...]
- Reward: [r_t = ...]

**Technical Route**:
```
[Input] → [Step 1] → [Step 2] → [Output]
```

**Advantages**:
- [Advantage 1]
- [Advantage 2]

**Challenges**:
- [Challenge 1]
- [Challenge 2]

### Approach B: [Name]
[Same structure]

---

## 6. Application Scenarios

| Scenario | Recommended Approach | Reason |
|----------|:-------------------:|--------|
| [Scenario 1] | A | [Why] |
| [Scenario 2] | B | [Why] |

---

## 7. Risk Assessment

| Risk | Severity | Probability | Mitigation |
|------|:--------:|:-----------:|------------|
| [Risk 1] | High | Medium | [How to handle] |
| [Risk 2] | Medium | High | [How to handle] |

---

## 8. Literature Support

| # | Reference | Purpose |
|---|-----------|---------|
| 1 | [Author, Year, Journal] | [What it supports] |
| 2 | [Author, Year, Journal] | [What it supports] |

---

## 9. Horizontal Comparison

| Idea | Novelty | Total | Status |
|------|:------:|:-----:|--------|
| [This idea] | X.X | XX.X | Under evaluation |
| [Previous idea 1] | X.X | XX.X | [Status] |
| [Previous idea 2] | X.X | XX.X | [Status] |

---

## 10. Conclusion & Recommendation

**Conclusion**: [One paragraph summary]

**Recommendation**:
- [ ] Proceed to next phase
- [ ] Needs more research
- [ ] Not recommended

**Next Steps**:
- [ ] [Action 1]
- [ ] [Action 2]
- [ ] [Action 3]
```

---

## Scoring Guidelines

### Novelty (新颖性)
- 5.0: Completely unexplored, zero competitors
- 4.0: Very few related works, clear gap
- 3.0: Some adjacent work exists, differentiation needed
- 2.0: Significant competition, must find unique angle
- 1.0: Already well-studied

### Technical Feasibility (技术可行性)
- 5.0: Clear technical path, known building blocks
- 4.0: Mostly clear, minor unknowns
- 3.0: Significant technical challenges but theoretically solvable
- 2.0: Major open problems, high risk
- 1.0: Theoretically questionable

### Experimental Verifiability (实验可验证性)
- 5.0: Standard benchmarks exist, clear metrics
- 4.0: Can create meaningful experiments
- 3.0: Experiments possible but require effort
- 2.0: Hard to demonstrate convincingly
- 1.0: Nearly impossible to verify

### Publication Feasibility (发表可行性)
- 5.0: Perfect fit for top venues, addresses hot topic
- 4.0: Good fit for relevant journals/conferences
- 3.0: Publishable with right framing
- 2.0: Niche audience, may need to find right venue
- 1.0: Hard to find appropriate venue

### Fit with Current Research (契合度)
- 5.0: Direct extension of current work
- 4.0: Strong connection, shares data/methods
- 3.0: Related field, some overlap
- 2.0: Different direction but same domain
- 1.0: Completely different research area

### Urgency (紧迫性)
- 5.0: Multiple groups about to publish, must act now
- 4.0: Growing interest, likely competition in 6-12 months
- 3.0: Moderate interest, some risk of being scooped
- 2.0: Low competition, can take time
- 1.0: No rush, niche topic

### Storytelling in Research — Why Framing Matters (讲故事的重要性)

#### Reviewer Psychology (审稿人心理)

A reviewer reads 5–10 papers per submission cycle. Their first impression forms in ~2 minutes after reading the title and abstract. Technical novelty alone won't save a poorly framed paper — but a well-framed story can elevate solid-but-not-groundbreaking work.

Key insight: **"Novelty" is partly about framing.** The same result can sound like an incremental improvement or a significant advance, depending on how you define the contribution. The `Publication Feasibility` score should reflect not just whether the topic is hot, but whether the idea *can be told as a compelling story*.

#### Four Narrative Frameworks (四种叙事框架)

| Framework | Structure | Best For |
|-----------|-----------|----------|
| **Problem → Solution → Impact** | State the problem → propose your solution → show the impact | Most papers (safe, clear, universal) |
| **Before → Gap → Bridge** | How things are done now → what's missing → how we bridge it | Method improvement, incremental but solid work |
| **Surprise → Investigation → Discovery** | Start with a counterintuitive observation → dig deeper → reveal the mechanism | Analytical/theoretical papers |
| **Claim → Defense → Evidence** | Make a bold claim → explain why it's plausible → prove it with experiments | High-risk, high-reward ideas |

#### The One-Sentence Test (一句话测试)

After writing the paper, try to summarize it in one sentence. If that sentence doesn't make your advisor lean in, the reviewer won't either.

> **Pro tip**: Before you even start the evaluation, ask yourself: "If I had only 30 seconds to pitch this idea at a conference dinner, what would I say?" The answer is your story core. Everything in the white paper should serve that core.
