# Practice profile: Employment & Labor — comparative

Orchestrator cold-start for plugin `cross-jurisdiction-employment`. Loaded after `cross-jurisdiction/CLAUDE.md`, before invoking a specific skill.

## Scope

Employment & Labor skills comparing several legal systems. Practice-area definition (`practices.json`, jurisdiction-agnostic): employment and labor law: employment contracts, termination/severance, worker classification, discrimination and harassment (Title VII/EEOC), wage/hour (FLSA), collective/union relations and labor arbitration, HR policies and internal HR investigations.

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
