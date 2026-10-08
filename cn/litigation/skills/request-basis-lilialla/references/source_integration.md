# Source Integration

Use this reference when adding or updating books, papers, statutes, judicial interpretations, court guidance such as minutes, cases, lecture tables, templates, or user checklists.

## Principle

Preserve original sources, but do not make the skill quote or follow them verbatim. Convert sources into traceable atomic propositions, then merge those propositions into rule-obligation groups.

```text
source file
  -> source registry / locator index
  -> atomic source assertions
  -> rule nodes / elements / defenses / evidence targets
  -> rule-obligation groups
  -> verification tasks
  -> runtime skill behavior
```

## Integration Steps

1. Register the source in the source registry with title, source id, optional portable locator, source status, and primary use.
2. Build or refresh retrieval chunks when the source is large.
3. Extract atomic source assertions. One assertion should express one legal proposition, doctrine, case-law path, evidence rule, or checklist item.
4. Classify each assertion:
   - `verified_law` only after authority verification;
   - `judicial_interpretation` or `court_guidance` as authority candidates needing version/effect checks;
   - `case_law_reference` for cases and裁判路径;
   - `scholarly_reference` for books, papers, lectures, and academic systems;
   - `user_curated_checklist` for user-made lists.
5. Map assertions to existing rule nodes where possible.
6. If no existing node fits, add a new node with `necessity`, `trigger_condition`, and `depth`.
7. Merge same-substance assertions under one rule node, preserving all sources in `source_assertions`.
8. Record conflicts instead of averaging them.
9. Add MCP/authority verification tasks for current law, judicial interpretation, court guidance, special law, minutes, and case-law paths.
10. Update evals only after the merged rule affects runtime behavior.

## Locator Discipline

- Runtime seed data should cite sources by `source_id`, `resource_id`, title, page, line, and semantic locator.
- Do not put local or package-specific paths into request-basis seeds, concept cards, rule-obligation groups, verification tasks, or evals.
- Path-like locators belong only in optional source registries, locator indexes, conversion inventories, and maintenance reports.
- If a distributed package does not include the referenced source registry or material package, keep the source assertion but mark retrieval as unavailable.

## Merge Rules

Merge when propositions share:

- same claim goal or issue;
- same legal effect;
- same trigger facts;
- same rule function;
- no unresolved conflict on authority, time effect, or scope.

Do not merge when differences involve:

- request basis vs defense vs evidence rule;
- current law vs scholarly view;
- national rule vs local rule;
- judicial interpretation vs meeting minutes/court guidance;
- majority path vs minority or contrary case-law path;
- exam expression vs litigation proof requirement.

## Update Priority

When new materials are added, prioritize:

1. authority materials: statutes, judicial interpretations, court guidance, minutes;
2. request-basis and element structure;
3. defenses, counter-defenses, and proof burdens;
4. case-law concretization and comparability;
5. academic papers and books;
6. user checklists and practice reminders;
7. eval tasks that catch the newly introduced risk.

## Runtime Impact

A new source changes the skill only after it changes one of:

- a rule-obligation group;
- a request-basis seed entry;
- a source/verification task;
- a mode guardrail;
- an eval task or rubric.

If it is only background reading, keep it indexed and retrievable without changing runtime rules.

## Integration Audit

When asked whether all materials are integrated, separate these levels:

- `registered_only`: known source, no extracted runtime effect;
- `indexed_only`: retrievable chunks only;
- `candidate_only`: candidates or review batches only;
- `digested_summary`: source digest exists with reusable claim goals, concepts, defenses, evidence issues, eval targets, and extraction tasks;
- `rule_or_seed`: concept cards, request-basis seeds, rule groups, or verification queue;
- `synthesized`: included in a claim-family or institution synthesis.

Do not describe `registered`, `indexed`, or `candidate_only` material as digested. Do not describe `digested_summary` as verified law or mature catalog coverage. Conversion artifacts may be useful for OCR tracing, but they are not independent legal authorities.
