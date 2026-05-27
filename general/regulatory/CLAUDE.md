# Practice profile: Regulatory & Administrative — jurisdiction-neutral

Orchestrator cold-start for plugin `general-regulatory`. Loaded after `general/CLAUDE.md`.

## Scope

Cross-sector administrative law and regulatory compliance: rulemaking, licensing, and agency enforcement. These are process/methodology tools, not tied to any one country's law.

## Jurisdiction guardrail

Skills here are **jurisdiction-neutral** even though the text is in English. Obtain the governing law from the user; do **not** default to US law. Where a step turns on jurisdiction-specific rules, defer to the user or to a jurisdiction-specific plugin.

## Citation discipline

Cite only sources the user supplies or that the skill explicitly references. **Never invent** citations or assert country-specific legal rules.

## When this plugin does NOT apply

- Health-sector regulation → see the Healthcare & Life Sciences practice (e.g. `us/healthcare`).
- Environmental regulation → use `general/environmental` (Environmental Law).
- Securities regulation → see the Securities & Capital Markets practice (e.g. `us/securities`).
- Privacy regulation → use `general/data-protection` (Data Protection & Privacy).

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current statute, regulation, and court/agency rules before relying on it.
