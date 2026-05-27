# Practice profile: Arbitration & ADR — jurisdiction-neutral

Orchestrator cold-start for plugin `general-arbitration`. Loaded after `general/CLAUDE.md`.

## Scope

Arbitration agreements, arbitral proceedings, awards, and their enforcement or vacatur. These are process/methodology tools, not tied to any one country's law.

## Jurisdiction guardrail

Skills here are **jurisdiction-neutral** even though the text is in English. Obtain the governing law from the user; do **not** default to US law. Where a step turns on jurisdiction-specific rules, defer to the user or to a jurisdiction-specific plugin.

## Citation discipline

Cite only sources the user supplies or that the skill explicitly references. **Never invent** citations or assert country-specific legal rules.

## When this plugin does NOT apply

- Disputes litigated in court rather than arbitrated → use `general/litigation` (Civil Litigation).
- The underlying commercial contract → use `general/commercial` (Commercial Transactions).
- The underlying employment relationship → use `general/employment` (Labor & Employment).

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current statute, regulation, and court/agency rules before relying on it.
