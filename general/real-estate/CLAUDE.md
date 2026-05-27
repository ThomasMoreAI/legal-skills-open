# Practice profile: Real Estate — jurisdiction-neutral

Orchestrator cold-start for plugin `general-real-estate`. Loaded after `general/CLAUDE.md`.

## Scope

Real property: conveyancing, leasing, title, financing, and land use. These are process/methodology tools, not tied to any one country's law.

## Jurisdiction guardrail

Skills here are **jurisdiction-neutral** even though the text is in English. Obtain the governing law from the user; do **not** default to US law. Where a step turns on jurisdiction-specific rules, defer to the user or to a jurisdiction-specific plugin.

## Citation discipline

Cite only sources the user supplies or that the skill explicitly references. **Never invent** citations or assert country-specific legal rules.

## When this plugin does NOT apply

- Construction of improvements → use `general/construction` (Construction Law).
- Contamination and remediation → use `general/environmental` (Environmental Law).
- Mortgage lending → use `general/finance` (Banking & Finance).
- Leases treated as commercial contracts → use `general/commercial` (Commercial Transactions).

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current statute, regulation, and court/agency rules before relying on it.
