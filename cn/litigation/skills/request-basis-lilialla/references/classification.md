# Case Entry And Cause Of Action Strategy

Do not let one cause of action replace request-basis analysis.

Use dual entry:

Substantive entry:

1. Claim goal: who wants what from whom.
2. Party roles and factual relationship.
3. Candidate request bases and rule-obligation groups.
4. Element facts, defenses, counter-defenses, proof targets.

Procedural/retrieval entry:

1. User-provided or document-provided cause of action.
2. Candidate causes of action inferred from claim goals and disputed legal relationships.
3. Filing, pleading drafting, case-law retrieval, and calibration labels.

Cause of action is not the source of the right. It is a court classification, retrieval handle, and later calibration field. It is many-to-many with request bases.

Rules:

- If the user gives no cause of action, do not force a single one.
- If the user gives a cause of action, still analyze claim goals and candidate request bases independently.
- Do not use a cause of action to exclude other possible request bases.
- In filing, pleading, or case-law retrieval tasks, output candidate causes of action early, but keep them separate from request bases.
- Treat `catalog_review_batches.cause_context` as extraction context, not runtime classification.

Practical entry question:

```text
Who seeks what relief from whom, and what candidate legal or transactional bases could support that relief?
```

Only after that, ask:

```text
Which candidate causes of action help retrieve materials, draft pleadings, or compare cases?
```
