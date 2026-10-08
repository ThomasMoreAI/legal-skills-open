---
name: cnil-scanner-thewatcher01
title: cnil-scanner
description: Check if a company has declared a DPO (Data Protection Officer) to the CNIL. Use when the user asks about RGPD compliance status of a company, or to identify prospects without a DPO. Companies without a DPO are hot RGPD consulting prospects.
author: TheWatcher01
author_url: https://github.com/TheWatcher01/skills/tree/main/.claude/skills/cnil-scanner
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: data-protection
language: en
---

# cnil-scanner

Check DPO (Data Protection Officer) declarations in the CNIL open data registry.

## Triggers

- `/cnil 424761419`
- `/cnil OVH`
- "cette entreprise a-t-elle un DPO?"
- "qui n'a pas de DPO dans le 31?"
- "verifier la conformite RGPD de X"

## How it works

Queries the CNIL DPO declaration dataset published on data.gouv.fr via the tabular API. No authentication required.

API endpoint: `https://tabular-api.data.gouv.fr/api/resources/0651b990-9d0f-404e-8aee-9f3a7755eedb/data/`

## Critical use case

**Companies WITHOUT a declared DPO are hot RGPD consulting prospects.** Any company processing personal data at scale is legally required to have a DPO (RGPD Art. 37). This skill identifies non-compliant companies for targeted prospecting.

## Usage

```bash
python3 {baseDir}/scripts/cnil.py --query "424761419" --format json
python3 {baseDir}/scripts/cnil.py --query "OVH" --format text
python3 {baseDir}/scripts/cnil.py --query "424761419" --format json
```

## Arguments

| Argument       | Required | Default | Description                                  |
|----------------|----------|---------|----------------------------------------------|
| `--query`      | yes      |         | SIREN number (9 digits) or company name       |
| `--department`  | no       |         | Filter by department code (postal code prefix) |
| `--format`     | no       | json    | Output format: `json` or `text`               |

## Output fields

- `has_dpo` — boolean, whether a DPO declaration was found
- `organism_name` — name of the declaring organization
- `siren` — SIREN number
- `dpo_name` — DPO name (if publicly available)
- `declaration_date` — date of DPO declaration
- `postal_code` — postal code of the organization
- `prospect_signal` — "HOT" if no DPO found, "COLD" if DPO declared

## RGPD compliance note

This skill only uses publicly available open data from the CNIL registry. No personal data is collected or stored. DPO declarations are public by design (RGPD Art. 37(7)).
