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

| Dimension | Score | One-sentence reason |
|-----------|:-----:|---------------------|
| Novelty | X.X | [Why this score? Mention the strongest evidence or uncertainty.] |
| Technical Feasibility | X.X | [Why this score? Name the key implementation blocker or enabler.] |
| Experimental Verifiability | X.X | [Why this score? Mention benchmarks, data, metrics, or missing validation path.] |
| Publication Feasibility | X.X | [Why this score? Mention venue fit, story strength, or reviewer risk.] |
| Fit with Current Research | X.X | [Why this score? Mention overlap with current work, data, or methods.] |
| Urgency | X.X | [Why this score? Mention competitive pressure or lack of rush.] |

Example:

| Dimension | Score | One-sentence reason |
|-----------|:-----:|---------------------|
| Novelty | 4.0 | Searched Semantic Scholar and Google Scholar; no direct combination found, but adjacent work exists. |
| Technical Feasibility | 3.0 | The method is plausible, but access to the required molecular dataset is uncertain. |

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

### Novelty Claims

Each claim below must be supported by one or more rows in the Search Log. Use narrow wording and avoid absolute claims unless the evidence is unusually strong.

| Claim ID | Novelty Claim | Evidence Rows | Confidence | Allowed Wording |
|----------|---------------|---------------|:----------:|-----------------|
| C1 | [Exact claim being made] | E1, E2, E3 | 0.75 | [No exact match found in searched sources as of YYYY-MM-DD] |

### Search Log

Every row must also be appended to `01-灵感收集/evidence-log.md` so the central evidence history stays complete.

| Row ID | Date | Query / Source | Channel | Key Results | Conclusion | Confidence | Supports Claim | Notes |
|--------|------|----------------|---------|-------------|------------|:----------:|----------------|-------|
| E1 | YYYY-MM-DD | `"keyword1" "keyword2"` | Web | [Top papers / no exact match / related work] | [Exact match / partial overlap / adjacent only / no close match] | 0.70 | C1 | [Caveats, missing databases] |
| E2 | YYYY-MM-DD | `05-文献库/` scan | Literature library | [Relevant notes found / none found] | [Conclusion] | 0.80 | C1 | [Scope of local library] |
| E3 | YYYY-MM-DD | [Survey paper title, year] | Survey | [What the survey covers or misses] | [Conclusion] | 0.75 | C1 | [Limitations] |

### Verdict

- [ ] Exact combination has been done before
- [ ] Partial overlap with existing work (specify)
- [ ] No exact match found in searched sources as of YYYY-MM-DD

**Careful novelty statement**: [State exactly what can be claimed based on the evidence above. Prefer "no exact match found in searched sources" over "no one has done this."]

**Residual uncertainty**: [What sources, databases, venues, languages, or keywords still need checking?]

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

Novelty score must have a one-sentence reason that points to the strongest Search Log evidence or the main uncertainty.

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

---

> 💡 **Storytelling matters**: How you frame an idea can be as important as the idea itself. See [`references/story-framing.md`](story-framing.md) for reviewer psychology, four narrative frameworks, and the one-sentence test — use these to strengthen the `Publication Feasibility` score and the overall white paper narrative.
