# Concept Cards

Concept cards are the controlled professional-term layer. Use them for material legal terms before mapping facts into request bases or rule-obligation groups.

## When To Use

Use a card when a term affects:

- claim target or request basis;
- element facts;
- defenses or counter-defenses;
- evidence targets;
- filing/retrieval labels;
- current-law or case-law verification tasks.

Examples include agency, unauthorized disposition, prescription, non-typical security, factoring, finance lease, ownership retention, company guarantee, personal information, medical damage, inheritance restoration, and marital debt.

## Card Function

A concept card is not verified law. It fixes the project working meaning of a term and records source status.

Minimum fields:

```text
term
aliases
category
working_definition
positive_triggers
negative_triggers
adjacent_concepts
request_basis_impact
defense_impact
evidence_targets
verification_tasks
source_status
verification_status
```

## Runtime Protocol

1. Extract material terms from facts, claims, contracts, pleadings, and evidence.
2. Check the concept-card seed first.
3. If no card exists, check the concept-candidate index and local retrieval snippets.
4. If still absent, create a temporary concept card labeled `model_inference/unverified`.
5. Use the card to explain trigger facts, exclusions, adjacent concepts, and proof targets.
6. Then map to request bases, rule-obligation groups, and verification tasks.

## Temporary Card

Use this shape in outputs when the catalog has not caught up:

```markdown
| term | trigger facts | adjacent concepts | request-basis impact | verification task | status |
| --- | --- | --- | --- | --- | --- |
```

Temporary cards may become repository entries only after they are abstract, reusable, sourced, and tied to a concrete repair location.

## Source Discipline

- Lecture and table materials are `scholarly_reference` or `case_training_sample`.
- OCR text carries `ocr_risk` until checked.
- Current law and judicial interpretations require authority verification.
- Case-law paths require research scope, comparability, and contrary-case tracking.
