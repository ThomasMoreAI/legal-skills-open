# Cross-cutting context: jurisdiction-agnostic skills

Orchestrator cold-start for `general/` plugins. Loaded before the plugin-specific `CLAUDE.md`.

## What these skills are

Process, formatting, and methodology tools — summarization, extraction, drafting workflow, document
handling — that do **not** depend on any single country's law.

## Jurisdiction guardrail (mandatory)

The skill text is in English, but the skills are **not** US-specific. Do **not** assume or default to
US law. Obtain the governing jurisdiction from the user. Where a task turns on country-specific rules,
defer to the user or route to a jurisdiction-specific plugin (e.g. `us/<practice>`, `ru/<practice>`).

## Citation discipline (mandatory)

Cite only the materials the user supplies or that the skill explicitly references. **Never invent**
citations, statutes, or case numbers, and **never** assert a country-specific legal rule as if it were
universal.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Apply the law of the relevant jurisdiction
> and verify against current sources before relying on it.
