# Practice profile: Administrative & Public Services — Ukraine

> **DRAFT** — auto-generated on import; review and refine before merge.

Orchestrator cold-start for plugin `ua-administrative`. Loaded after `ua/CLAUDE.md`, before invoking a specific skill.

## Scope

Citizen-facing administrative procedures and public services: passports / ID-cards and residence registration at ЦНАП, consular procedures abroad, driver- and vehicle-related services at СЦ МВС, and selecting the correct legal regime for letters, requests, and complaints to authorities.

## Forums & authorities

Administrative-service providers (ЦНАП, ДП «Документ», СЦ МВС, ДМС, consular institutions of the МЗС). Refusals and unlawful inaction are challenged before the administrative courts (КАС) — see the `litigation` plugin for the court route.

## Key sources of law

Within Ukraine: the statutes and Cabinet of Ministers resolutions governing each service, plus the general regimes for citizen appeals, access to public information, administrative procedure, administrative services, and personal-data access. For the sources-of-law hierarchy and working language, see `ua/CLAUDE.md`.

## Citation discipline

Follow the rules in `ua/CLAUDE.md`. **Never invent** statute numbers, resolution numbers, fees, or deadlines — each skill verifies current values via official sources before relying on a reference.

## When this plugin does NOT apply

- Court challenge of a refusal (адмінпозов) → `litigation`
- Drafting the substantive document itself → the relevant practice plugin

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
