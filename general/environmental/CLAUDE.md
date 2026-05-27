# Practice profile: Environmental Law — jurisdiction-neutral

Orchestrator cold-start for plugin `general-environmental`. Loaded after `general/CLAUDE.md`.

## Scope

Environmental regulation, contamination liability, permitting, and impact review. These are process/methodology tools, not tied to any one country's law.

## Jurisdiction guardrail

Skills here are **jurisdiction-neutral** even though the text is in English. Obtain the governing law from the user; do **not** default to US law. Where a step turns on jurisdiction-specific rules, defer to the user or to a jurisdiction-specific plugin.

## Citation discipline

Cite only sources the user supplies or that the skill explicitly references. **Never invent** citations or assert country-specific legal rules.

## When this plugin does NOT apply

- Non-environmental compliance → use `general/regulatory` (Regulatory & Administrative).
- Land use and zoning → use `general/real-estate` (Real Estate).
- General procedure → use `general/litigation` (Civil Litigation).

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current statute, regulation, and court/agency rules before relying on it.
