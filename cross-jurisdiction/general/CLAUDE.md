# Practice profile: General Methodology — Cross-jurisdiction

Orchestrator cold-start for plugin `cross-jurisdiction-general`. Loaded after
`cross-jurisdiction/CLAUDE.md`, before invoking a specific skill.

## Scope

Cross-jurisdiction methodology that is not tied to a specific practice area: comparative
research approaches, multi-country project structuring, legal-research workflows that span
several jurisdictions.

## Jurisdiction guardrail

Inherited from `cross-jurisdiction/CLAUDE.md`: every claim must name the country it
applies to and cite **that** country's own sources. **Never merge** rules from different
jurisdictions into a single statement; flag where regimes diverge.

## Key sources of law

Skills in this plugin are typically methodological rather than substantive. When they
touch the substantive law of a specific country, that country's own sources govern the
citation form (see the country-level `CLAUDE.md`).

## Citation discipline

Attribute each rule to its jurisdiction and source. Follow each jurisdiction's own
citation form. **Never invent** statutes, cases, or section numbers.

## When this plugin does NOT apply

- Comparative analyses on a specific practice area → use the corresponding
  `cross-jurisdiction/<practice>` plugin (e.g., `cross-jurisdiction/data-protection`).
- Single-jurisdiction work → use the appropriate country plugin.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Comparative summaries
> simplify; verify each jurisdiction's current law with local counsel before relying on it.
