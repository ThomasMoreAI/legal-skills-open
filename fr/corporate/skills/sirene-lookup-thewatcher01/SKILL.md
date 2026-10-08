---
name: sirene-lookup-thewatcher01
title: sirene-lookup
description: Search French companies and associations via the SIRENE registry. Use when the user asks to find a company by name, SIREN/SIRET number, location, or NAF code. Covers all registered entities in France.
author: TheWatcher01
author_url: https://github.com/TheWatcher01/skills/tree/main/.claude/skills/sirene-lookup
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: corporate
language: en
---

# sirene-lookup

Search the French SIRENE registry to find companies and associations.

## Triggers

- `/sirene OVH Roubaix`
- `/sirene 424761419`
- "trouve l'entreprise X"
- "quel est le SIRET de Y"
- "entreprises dans le secteur Z a Toulouse"

## How it works

The skill queries two complementary APIs:

1. **Recherche Entreprises DINUM** (no auth required) — fast full-text search by name, location, NAF code. Best for fuzzy lookups.
2. **INSEE SIRENE V3.11** (requires `INSEE_API_KEY` env var) — authoritative data with full details. Used when a SIREN/SIRET is known or when DINUM results need enrichment. Graceful fallback if no key is set.

## RGPD compliance

Only entities with `statutDiffusionEtablissement === "O"` (publicly diffusible) are returned. Non-diffusible entities are silently filtered out.

## Usage

```bash
python3 {baseDir}/scripts/sirene.py --query "OVH Roubaix" --format json
python3 {baseDir}/scripts/sirene.py --query "424761419" --format text
python3 {baseDir}/scripts/sirene.py --query "cybersecurite" --department 31 --format json
```

## Arguments

| Argument       | Required | Default | Description                              |
|----------------|----------|---------|------------------------------------------|
| `--query`      | yes      |         | Company name, SIREN, SIRET, or keywords  |
| `--department`  | no       |         | Filter by department code (e.g. 31, 75)  |
| `--per-page`   | no       | 10      | Number of results (1-25)                 |
| `--format`     | no       | json    | Output format: `json` or `text`          |

## Output fields

- `siren` — 9-digit SIREN number
- `siret` — 14-digit SIRET (headquarters)
- `denomination` — legal name
- `address` — full postal address
- `naf_code` — NAF/APE activity code
- `naf_label` — human-readable activity label
- `effectif` — workforce bracket
- `categorie_juridique` — legal form
- `date_creation` — creation date
- `etat_administratif` — active/closed

## Environment variables

| Variable        | Required | Description                     |
|-----------------|----------|---------------------------------|
| `INSEE_API_KEY` | no       | Bearer token for INSEE SIRENE V3.11. Without it, only DINUM API is used. |
