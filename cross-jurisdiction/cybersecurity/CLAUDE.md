# Practice profile: Cybersecurity & Information Security — comparative

Orchestrator cold-start for plugin `cross-jurisdiction-cybersecurity`. Loaded after `cross-jurisdiction/CLAUDE.md`, before invoking a specific skill.

## Scope

Cybersecurity & Information Security skills comparing several legal systems. Practice-area definition (`practices.json`, jurisdiction-agnostic): information security as a practice: NIS2/DORA/CRA, NYDFS 23 NYCRR 500, CMMC, SOC 2 / ISO 27001/27701, ANSSI/EBIOS/PSSI, incident response/operational resilience.

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
