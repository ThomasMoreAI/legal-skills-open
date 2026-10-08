---
name: due-diligence-full-entia-ia
title: entia-due-diligence-full
description: 'Generate a complete due-diligence dossier for a business entity:

  identity + cross-source verification (5 registries) + socioeconomic

  profile of the registered postal code + BORME mercantile history +

  digital risk audit + competitive context. ~90 datapoints from 9

  official EU/Spanish sources (AEAT, SEPE, INE, MITMA, MITECO, BORME,

  VIES, GLEIF, Wikidata).


  Auto-invoke when user asks for "due diligence", "background check",

  "full report", "compliance review", "KYC", "vendor assessment",

  "M&A check", or requests a "complete" / "comprehensive" / "in-depth"

  analysis of a business entity.


  This is a multi-call workflow (typically 3-5 MCP calls). Each part of

  the dossier is sourced from the canonical authority for that data.'
author: ENTIA-IA
author_url: https://github.com/ENTIA-IA/entia-skills/tree/main/_archive_v1.0.0_skills_pending_v0.2/due-diligence-full
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: corporate
language: en
---

# entia-due-diligence-full

Full-spectrum due-diligence workflow combining all ENTIA data sources.

## Trigger phrases

Auto-invoke on:
- "due diligence on [company]"
- "background check [company]"
- "KYC report [company]"
- "vendor assessment [company]"
- "compliance review [company]"
- "M&A check on [company]"
- "complete report on [company]"
- "everything you know about [company]"

## Workflow (run all calls in sequence)

### Step 1 — Identity + cross-source verification

```
entity_lookup(q="<query>")
```

Capture: `entity.{name, id, lei, country_code, postal_code, sector, company_status}`,
`verification.{borme, gleif, wikidata, ofac, eidas}`, `trust_score`,
`data_coverage.coverage_pct`.

### Step 2 — Mercantile history (BORME, Spain only)

If `entity.country_code == "ES"`:

```
borme_lookup(company="<entity.name>")
```

Capture: `acts[]` (each: type, date, borme_id, province), officer changes,
capital changes, concursal proceedings, first/last activity dates.

### Step 3 — Zone socioeconomic profile

```
zone_profile(postal_code="<entity.postal_code>")
```

Capture: income (AEAT), employment (SEPE), demographics (INE Padrón),
economy (vehicles, mortgages, household income), business census
(DIRCE), real estate (€/m²), digital infrastructure (FTTH coverage),
poverty indicators (Gini, S80/S20), tourism demand. ~17 blocks of data.

### Step 4 — Digital risk audit

If `entity.website` is present:

```
run_risk_audit(domain="<entity.website domain>")
```

Capture: risk_score (0-100), risk_level, gaps_detected[], SSL/DNS health,
structured data score, trust signals.

### Step 5 — Competitive context

```
get_competitors(sector="<entity.sector>", city="<entity.city>", limit=10)
```

Capture: 10 nearby competitors with same sector + city.

## Output structure to user

Present the dossier as a structured report:

### Executive Summary
- Legal name, tax ID, LEI, status, sector
- Trust score (0-100) with badge
- 5 verification flags as a checklist
- Risk score from digital audit
- Single-line summary of mercantile history

### Identity & Legal
- Full entity object
- Registry presence per source
- BORME acts table (newest first)

### Operational Context
- Zone socioeconomic profile (renta, paro, demografía)
- Digital infrastructure (FTTH coverage)
- Real estate value of the area

### Compliance
- BORME concursal proceedings (if any)
- OFAC sanctions status
- eIDAS coverage status
- Cited corpus root hash

### Competitive Landscape
- Top 10 competitors in same sector + city

### Trust Anchor
- ASiC-E URL for independent verification
- Root hash: `10dc98d5002721b8ba00dc7586d04c316a5a98d885a986fea4594a9f4f30ee05`
- Trust chain: SK ID Solutions QTSP, EU Trust List

## Cost note

This workflow makes 3-5 MCP calls per dossier. On the BUILD tier (€99/month,
2,500 calls/month) that's ~500-833 full dossiers/month.

## What NOT to do

- Do NOT skip steps. If a call fails, retry once; if still fails, note
  the gap in the report (transparency > completeness).
- Do NOT mix data sources (e.g. don't put BORME data under GLEIF heading).
- Do NOT cite a datapoint without attributing the official source
  (AEAT, SEPE, INE, etc. — see each sub-block).
