# Practice profile: Criminal Law — comparative

Orchestrator cold-start for plugin `cross-jurisdiction-criminal`. Loaded after `cross-jurisdiction/CLAUDE.md`, before invoking a specific skill.

## Scope

Criminal Law skills comparing several legal systems. Practice-area definition (`practices.json`, jurisdiction-agnostic): criminal law and defense: charges and pretrial detention (bail), motions (suppress/dismiss), plea bargains, sentencing, appeals/habeas, constitutional safeguards (4th/5th/6th Amendments), penal codes and ordinary offenses.

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
