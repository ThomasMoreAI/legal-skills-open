# Practice profile: Trusts & Estates — comparative

Orchestrator cold-start for plugin `cross-jurisdiction-trusts-and-estates`. Loaded after `cross-jurisdiction/CLAUDE.md`, before invoking a specific skill.

## Scope

Trusts & Estates skills comparing several legal systems. Practice-area definition (`practices.json`, jurisdiction-agnostic): estate planning and instruments for death/incapacity: wills (will/pour-over), trusts (revocable/ILIT/CRT/SNT), probate and estate administration, fiduciary duties, powers of attorney (durable/healthcare POA), advance directives, guardian nomination for minors within a will/estate plan, elder law (Medicaid planning), forced heirship (Pflichtteil).

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
