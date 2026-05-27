# Cross-cutting context: cross-jurisdiction (comparative) skills

Orchestrator cold-start for `cross-jurisdiction/` plugins. Loaded before the plugin-specific `CLAUDE.md`.

## What these skills are

Comparative tools that analyze the law of **several countries at once** (e.g. EU vs. US data protection,
multi-country IP portfolios, cross-border regulatory mapping).

## Jurisdiction guardrail (mandatory)

Every statement must name the jurisdiction it applies to and cite **that** jurisdiction's own sources.
**Never** merge rules from different countries into a single claim; where regimes diverge, say so
explicitly. When one jurisdiction's rule is unknown, flag the gap rather than borrowing another's.

## Citation discipline (mandatory)

Attribute each rule to its jurisdiction and source. Follow each jurisdiction's own citation form.
**Never invent** statutes, cases, or section numbers.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Comparative summaries simplify; verify each
> jurisdiction's current law with local counsel before relying on it.
