# Practice profile: Consumer Protection — jurisdiction-neutral

Orchestrator cold-start for plugin `general-consumer`. Loaded after `general/CLAUDE.md`.

## Scope

Consumer complaints and formal claim letters: structuring the facts, escalation levels, and
the demand itself. These are process tools, not tied to one country's law.

## Jurisdiction guardrail

The skill text is in French and may cite French consumer law as an example. Obtain the
governing law and the consumer's country from the user; do **not** default to French law.
For a French consumer, prefer `fr/consumer`.

## Citation discipline

Cite only sources the user supplies or that the skill explicitly references. **Never
invent** citations or assert country-specific legal rules.

## When this plugin does NOT apply

- French small claims and consumer mediation → `fr/consumer`.
- Business-to-business disputes → `general/commercial`.
- Litigation after the complaint fails → `general/litigation` or a jurisdiction plugin.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
