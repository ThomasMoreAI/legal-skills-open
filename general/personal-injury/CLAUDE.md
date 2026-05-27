# Practice profile: Personal Injury & Torts — jurisdiction-neutral

Orchestrator cold-start for plugin `general-personal-injury`. Loaded after `general/CLAUDE.md`.

## Scope

Tort claims for personal injury: negligence, liability, causation, and damages. These are process/methodology tools, not tied to any one country's law.

## Jurisdiction guardrail

Skills here are **jurisdiction-neutral** even though the text is in English. Obtain the governing law from the user; do **not** default to US law. Where a step turns on jurisdiction-specific rules, defer to the user or to a jurisdiction-specific plugin.

## Citation discipline

Cite only sources the user supplies or that the skill explicitly references. **Never invent** citations or assert country-specific legal rules.

## When this plugin does NOT apply

- General civil procedure → use `general/litigation` (Civil Litigation).
- Coverage of the claim → see the Insurance Law practice (e.g. `us/insurance`).
- Medical-malpractice regulatory overlap → see the Healthcare & Life Sciences practice (e.g. `us/healthcare`).

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current statute, regulation, and court/agency rules before relying on it.
