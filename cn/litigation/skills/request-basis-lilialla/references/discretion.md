# Model Discretion

This skill should be structured, not mechanical.

Use three layers:

1. Hard guardrails: never break source, fact, verification, or request-basis classification rules.
2. Scaffolding: use request goals, candidate bases, rule-obligation groups, elements, defenses, evidence targets, and candidate causes of action.
3. Exploration: propose alternative paths, unusual issues, conflicts, or better research questions when facts justify it.

## Hard Guardrails

- Do not equate cause of action, claim text, article number, legal relationship, or evidence with request basis.
- Do not treat party statements as found facts.
- Do not state current law or court practice as verified without authority search.
- Do not package OCR, books, lectures, or user checklists as verified law.
- Do not collapse different claim targets into one vague label.

## Flexible Scaffolding

The output does not have to follow one fixed template. It may start with:

- claim targets;
- legal relationship map;
- issue list;
- evidence gaps;
- candidate causes of action;
- rule-obligation group mapping.

But it must eventually make request goals, candidate request bases, elements, defenses, evidence targets, and verification needs visible.

## Discretion Budget

Pick the lightest depth that fits the task:

- `open_scan`: sparse facts or brainstorming. List candidate paths, missing facts, and research questions. Do not force a full three-layer analysis.
- `structured_analysis`: clear study facts or claim goal. Make request basis, elements, defenses, and source status visible.
- `evidence_matrix`: litigation materials. Strictly separate statements, evidence, disputed facts, proof targets, and gaps.
- `research_expanded`: law, judicial interpretation, or case-law questions. Expand linked modules only with source and verification status.

Do not start with maximal tables when the user is still shaping the problem.

## Exploration Rules

Creative or non-obvious paths are welcome if labeled:

- candidate path;
- model inference;
- needs evidence;
- needs MCP verification;
- needs human review.

Do not suppress a plausible path merely because it is absent from the seed catalog. Add it as a candidate and explain the trigger facts.

Do not over-expand every related doctrine. Link broad modules through `related_group_ids` or verification tasks.
