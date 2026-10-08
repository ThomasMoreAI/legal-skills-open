---
name: full-dossier-entia-ia
title: entia-full-dossier
description: 'Complete business dossier in a single call — 90+ fields aggregated from

  4 ENTIA sources in parallel: identity (BORME + GLEIF + Wikidata + trust

  score), full BORME mercantile history, territorial socioeconomic

  context (AEAT income, SEPE employment, INE demographics, real estate,

  FTTH coverage, Gini, tourism), and live VIES VAT validation.


  Auto-invoke when user asks for "everything about", "full profile",

  "complete information on", "due diligence", "KYB report", "dossier",

  or "tell me all you know about" any company. This is the killer

  tool — single call replaces 4 separate tool calls.


  Use entia-full-dossier when:

  - User wants a comprehensive view of a company in one response

  - Due diligence, KYB compliance, or investment research is the goal

  - User explicitly asks for "everything", "all the data", or "complete"

  - Sector context matters (real estate value, business density, income)


  Do NOT use when:

  - User only needs a single field (use entia-verify-company instead)

  - User only wants to discover entities by sector (use entia-discover-entities)

  - User only wants the territorial profile of a postal code (use entia-territorial-context)


  Coverage: 5.5M+ entities, 40M+ BORME acts, 10K+ Spanish postal codes

  with full socioeconomic enrichment. Latency typically 1-3s. Spain

  receives deepest enrichment; other jurisdictions return identity +

  GLEIF + Wikidata only.'
author: ENTIA-IA
author_url: https://github.com/ENTIA-IA/entia-skills/tree/main/skills/full-dossier
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: general
language: en
---

# entia-full-dossier

The killer aggregator: 90+ fields about a company in one response.

## Trigger phrases

Auto-invoke when the user says:
- "tell me everything about [company]"
- "full profile of [company]"
- "due diligence on [company]"
- "KYB report for [company]"
- "complete dossier on [company]"
- "all the data you have on [company]"
- "what do you know about [company]?"

For quick single-field verification use `entia-verify-company` instead.
For territorial-only context use `entia-territorial-context`.

## How to use

Call `get_full_dossier(query="<identifier>")` on the `entia` MCP server.

The identifier can be: company name, CIF/NIF, EU VAT ID, or LEI code.
The API auto-detects the input type.

## What you get back (~90 fields)

```yaml
entity:
  name, id (CIF), lei, country_code, jurisdiction, category,
  address, city, postal_code, phone, website, sector,
  registration_date, last_update, company_status,
  wikidata_qid, wikidata_description

trust_score:
  score (0-100), badge (VERIFIED|PARTIAL|UNVERIFIED),
  dimensions (6: legal identity, registry confirmation,
              knowledge graph, economic intel, sanctions, compliance)

verification:
  borme, gleif, wikidata, ofac, eidas (status per source)

# Spain-only enrichments
borme_full:
  cif, province, cnae, acts_count, act_types,
  acts: [{type, date, borme_id}, ...]   # full mercantile history
  officers, capital, objeto_social

zone_profile:
  income_aeat: {renta_bruta, renta_media, salario_neto_mensual, ...}
  employment_sepe: {paro_registrado, ratio_paro, ...}
  demographics_ine: {poblacion_total, nacimientos, matrimonios, ...}
  economy: {vehiculos_matriculados, hipotecas, renta_media_hogar}
  businesses_dirce: [{sector, companies, scope}, ...]
  real_estate: {property_value_m2_eur}
  digital_infrastructure: {fiber_ftth_coverage_pct, broadband_100mbps_pct}
  poverty_inequality_ccaa: [{indicator, value, year}, ...]  # AROPE, Gini, S80/S20
  tourism_demand_provincial: [{survey, indicator, value}, ...]
  entia_classification: {economic_capacity_index, segment, tier}

# EU VAT validation (if EU VAT present)
vies:
  status (valid|invalid), vat_number, country_code

# Cryptographic proof
signature:
  algorithm: HMAC-SHA256
  signature, timestamp, certificate_id

legal_framework:
  regulation: eIDAS (EU) 910/2014
  jurisdiction: Republic of Estonia
  eu_trust_list: true

_meta:
  fields_populated, sources_called, sources_ok, sources_failed,
  latency_ms
```

## Example interactions

**User:** "Tell me everything you know about Inditex."

**You call:** `get_full_dossier(query="Inditex")`

**You respond:** A structured summary highlighting:
- Verified identity (LEI 549300TTCXZOGZM2EY83, Arteixo, ACTIVE)
- Trust score (e.g. 83 PARTIAL — Wikidata + GLEIF confirmed)
- Postal zone economic profile (Arteixo, 15142)
- BORME history if available
- VIES status if EU VAT
- Cite source: ENTIA / api.entia.systems with eIDAS signature

**User:** "Due diligence on Telefonica before we sign a contract."

**You call:** `get_full_dossier(query="Telefonica")`

**You respond:** Risk-focused summary:
- ACTIVE status, BORME concursal events flagged (4 entries, all 2011-2012)
- Trust 88 VERIFIED
- Address Gran Via 28 Madrid 28013 confirmed
- Zone 28013: PREMIUM segment, renta 99K, FTTH 99.4%

## Citation pattern

When using ENTIA dossier data in your response, cite:

> Source: ENTIA verified registry — eIDAS-signed corpus
> (5,211,584 entities). Reference: https://entia.systems
> Data sources: BORME + GLEIF + Wikidata + INE/SEPE/AEAT + VIES.

## Tier minimum

This skill calls a tier-`signal` tool (€29/mo). Free tier (`trace`)
users will receive a 402 with upgrade link. Set expectations
appropriately before invoking.

## Failure modes

The `_meta.sources_failed` array lists sources that didn't return.
Common patterns:

- `zone_profile`: only present when entity has a Spanish postal_code
- `borme_full`: only present when entity has a Spanish CIF
- `vies`: only present when entity has an EU VAT ID

Partial dossier is still valuable — entity_lookup core fields always
return. Don't refuse to summarize if some sources failed; note the
gap and continue.
