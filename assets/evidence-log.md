# Evidence Log

> Central search and evidence log for novelty claims. Every novelty claim must bind to query/source, date, key results, conclusion, and confidence.

## Rules

1. One row per search, literature-library scan, survey check, or knowledge-base query.
2. Every novelty claim in an evaluation white paper must reference one or more evidence rows.
3. Use narrow wording. Prefer "no exact match found in searched sources" over "no one has done this."
4. Confidence below 0.7 is preliminary and should not support a strong novelty claim.

## Search / Evidence Log

| ID | Date | Idea | Claim | Query / Source | Channel | Key Results | Conclusion | Confidence | Notes |
|----|------|------|-------|----------------|---------|-------------|------------|:----------:|-------|
| E1 | YYYY-MM-DD | [Idea name] | [Exact novelty claim] | ["keyword1" "keyword2"] | Web | [Specific papers / no exact match / adjacent work] | [Exact match / partial overlap / adjacent only / no close match] | 0.70 | [Caveats, missing databases, next searches] |

## Confidence Guide

| Confidence | Meaning |
|:----------:|---------|
| 0.9-1.0 | Multiple authoritative sources checked; exact and adjacent terms covered |
| 0.7-0.8 | Good coverage, but some databases, languages, or terms may be missing |
| 0.5-0.6 | Preliminary search only; useful for brainstorming, not final claims |
| <0.5 | Too weak to support a novelty claim |

## Claim Register

| Claim ID | Idea | Novelty Claim | Evidence Rows | Current Wording | Confidence | Status |
|----------|------|---------------|---------------|-----------------|:----------:|--------|
| C1 | [Idea name] | [Exact claim] | E1, E2 | [Allowed wording] | 0.70 | Draft / Supported / Needs more search / Collision found |
