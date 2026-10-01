---
name: bodacc-watch-thewatcher01
title: bodacc-watch
description: 'Monitor BODACC (Bulletin Officiel des Annonces Civiles et Commerciales) for business signals: company creations, modifications, insolvency proceedings, sales. Use when the user asks about recent commercial announcements for a company or a territory.'
author: TheWatcher01
author_url: https://github.com/TheWatcher01/skills/tree/main/.claude/skills/bodacc-watch
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: bankruptcy
language: fr
---

# bodacc-watch

Monitor the BODACC for business signals: creations, modifications, insolvency proceedings, asset sales.

## Triggers

- `/bodacc OVH`
- `/bodacc 31 creation`
- "quelles entreprises creees cette semaine en 31?"
- "procedures collectives recentes a Toulouse"
- "signaux business pour OVH"

## How it works

Queries the BODACC OpenDataSoft API (DILA) which publishes all official commercial announcements. No authentication required.

API endpoint: `https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records`

## Signal types

| Signal                  | BODACC code | Meaning                                    |
|-------------------------|-------------|---------------------------------------------|
| `creation`              | creation    | New company registered                      |
| `modification`          | modification| Change in status, capital, management        |
| `procedure_collective`  | PCL         | Insolvency: safeguard, receivership, liquidation |
| `vente_cession`         | vente       | Business or asset sale                       |

## Usage

```bash
python3 {baseDir}/scripts/bodacc.py --query "OVH" --format json
python3 {baseDir}/scripts/bodacc.py --department 31 --signal creation --format json
python3 {baseDir}/scripts/bodacc.py --query "cybersecurite" --days 30 --format text
```

## Arguments

| Argument       | Required | Default | Description                                 |
|----------------|----------|---------|---------------------------------------------|
| `--query`      | no       |         | Company name or keywords to search           |
| `--department`  | no       |         | Department code (e.g. 31, 75)                |
| `--signal`     | no       |         | Filter by signal type (creation, modification, procedure_collective, vente_cession) |
| `--days`       | no       | 7       | Look back N days from today                  |
| `--per-page`   | no       | 20      | Number of results (1-100)                    |
| `--format`     | no       | json    | Output format: `json` or `text`              |

## Output fields

- `date` — publication date
- `type` — signal type
- `entity_name` — company/entity name
- `siren` — SIREN if available
- `department` — department code
- `description` — announcement summary
- `source_url` — link to original BODACC notice
