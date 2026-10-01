# Practice profile: Environmental Law — comparative

Orchestrator cold-start for plugin `cross-jurisdiction-environmental`. Loaded after `cross-jurisdiction/CLAUDE.md`, before invoking a specific skill.

## Scope

Environmental Law skills comparing several legal systems. Practice-area definition (`practices.json`, jurisdiction-agnostic): environmental law: EIA, EPA/NEPA, environmental permits, air/water/soil pollution, contaminated land, waste, biodiversity/endangered species, emissions trading/ETS and climate regulation when tied to environmental obligations.

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
