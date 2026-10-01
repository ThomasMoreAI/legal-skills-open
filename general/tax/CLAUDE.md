# Practice profile: Tax — jurisdiction-neutral

Orchestrator cold-start for plugin `general-tax`. Loaded after `general/CLAUDE.md`, before invoking a specific skill.

## Scope

Tax skills not tied to one country's law. Practice-area definition (`practices.json`, jurisdiction-agnostic): tax law: income/corporate/property tax, returns and forms (1099/SS-4/Schedules), tax audits and disputes with revenue authorities, tax planning, transfer pricing, R&D credits.

## Jurisdiction guardrail

Skills here are jurisdiction-neutral methods and tools. Obtain the governing law from the user; do **not** default to any country's law. Where a step turns on jurisdiction-specific rules, defer to the user or to a jurisdiction-specific plugin.

## Citation discipline

Cite only sources the user supplies or that the skill explicitly references. **Never invent** citations or assert country-specific rules.

## When this plugin does NOT apply

- Another area of law → the plugin for that practice area under `general/`.
- Another country's law → that jurisdiction's plugin.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
