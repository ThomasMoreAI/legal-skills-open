# Practice profile: Tax — comparative

Orchestrator cold-start for plugin `cross-jurisdiction-tax`. Loaded after `cross-jurisdiction/CLAUDE.md`, before invoking a specific skill.

## Scope

Tax skills comparing several legal systems. Practice-area definition (`practices.json`, jurisdiction-agnostic): tax law: income/corporate/property tax, returns and forms (1099/SS-4/Schedules), tax audits and disputes with revenue authorities, tax planning, transfer pricing, R&D credits.

## Comparative guardrail

State for every point which legal system it comes from; do not merge rules of different systems into one answer.

## Citation discipline

Cite each system's sources in its own citation format. **Never invent** article numbers, case names, or references.

## When this plugin does NOT apply

- Another area of law → the plugin for that practice area under `cross-jurisdiction/`.
- Another country's law → that jurisdiction's plugin.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
