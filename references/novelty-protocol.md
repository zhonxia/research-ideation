# Differentiation And Novelty Protocol

Novelty is a bounded evidence claim, not a search-count claim.

## Gap Levels

| Level | Evidence | Permitted use |
|---|---|---|
| Local coverage gap | Absent from the user's library | Prioritize searching only |
| Search-supported gap | Documented multi-channel search found no exact match | Preliminary evaluation wording |
| Validated research gap | Reviews, terminology variants, databases, and citation chains converge | Strong but still bounded claim |

## Search Protocol

### 1. Decompose The Claim

State the narrow novelty claim, then separate it into four comparable parts:

| Part | Question |
|---|---|
| Problem framing | What task, inputs, outputs, population, and evaluation setting are claimed? |
| Core mechanism | What algorithm, theory, proof move, experimental design, or data construction is proposed? |
| Key insight | Why should it work, and what is claimed to be missing from prior work? |
| Application domain | Where is it expected to apply, and how broad is that scope? |

Record assumptions and operating conditions separately. They can determine whether two apparently similar methods are actually equivalent, but they are not a fifth score to count mechanically.

### 2. Search Broadly

1. Define concept families: phenomenon, mechanism, method, outcome, population/domain, and legacy terminology.
2. Use complementary queries for the original problem, broader domain, exact method, mechanism signature, assumptions, and counter-hypotheses.
3. Search relevant scholarly databases and field-specific indexes, not only general web search.
4. Check recent reviews or evidence syntheses and the local library.
5. Record inclusion/exclusion rationale, languages, date range, channels, and search end date.

### 3. Triage Titles And Abstracts

1. Merge and deduplicate results by stable identifier and normalized title.
2. Compare each result against the four claim parts.
3. Mark each part as `match`, `partial`, `different`, or `unclear`; do not convert the count into a novelty score.
4. Retain papers for full-text review when the core mechanism may match, at least two parts match or partially match, the work is a recent close neighbor, or the abstract leaves a decisive point unclear.
5. Rank retained papers by threat to the claim. Normally deep-read the top 3–7; adjust the number when the field or search budget justifies it.

### 4. Deep-Read The Closest Works

For each retained paper, verify from the full text:

- Exact problem setup, data or premises, outcomes, and evaluation regime
- Actual mechanism or proof, not only the paper's headline description
- Authors' explanation of why it works
- Assumptions, limitations, and tested scope
- A precise section, passage, equation, table, or experiment supporting the comparison

Use the abstract only when full text is unavailable, and label that limitation. Search backward references and forward citations for the closest works. Add newly discovered terminology and competitors to the search set.

### 5. State The Difference

Write one Delta Statement:

> Unlike [closest verified work], which [does X under condition or assumption Y], the proposed work [changes X, relaxes Y, or extends to Z], and tests the difference through [observable result R].

The sentence must name the closest work, the concrete difference, and how that difference can be observed. If no defensible sentence can be written, report that the idea overlaps or remains too vague and revise it before scoring.

### 6. Close The Search

1. Record exact matches, partial overlaps, contrary evidence, and null searches.
2. Stop at declared saturation or a declared time budget; record which occurred.
3. Store evidence rows and claim links in `evidence-log.md`.

## Saturation Rule

Treat a search as saturated only when two consecutive query/citation iterations add no new close competitor, terminology family, or material qualification. Saturation does not prove universal absence.

## Evidence Quality

| Grade | Typical support |
|---|---|
| A | Multiple authoritative databases, current review coverage, citation chains, terminology variants, and independently verified identifiers |
| B | Strong multi-channel coverage with minor unresolved scope |
| C | Preliminary database/web coverage; useful for screening only |
| D | Local-library check or a few queries; cannot support novelty wording |

Confidence must reflect coverage, source quality, and unresolved scope. Do not derive confidence from the number of queries alone.

Do not treat model-recalled citations as evidence until their identifiers and contents are verified from a live source.

## Evidence Row Requirements

Record:

- Stable evidence ID and idea/claim IDs
- Search/check date and retrieval date
- Query or source
- Database/channel and coverage axis
- Date/language filters
- Stable paper identifiers or URLs
- Key results and contrary evidence
- Conclusion: exact match / partial overlap / adjacent / no close match
- Quality grade and confidence
- Caveats and next searches

## Claim Language

Prefer:

> Within the documented databases, terminology, date range, languages, and citation chains searched through YYYY-MM-DD, no exact match was found for [narrow claim]. Related work addresses [adjacent scope] but not [bounded difference].

Avoid:

- "This is completely novel."
- "No one has studied this."
- "The literature has no solution" when only the local library was checked.
