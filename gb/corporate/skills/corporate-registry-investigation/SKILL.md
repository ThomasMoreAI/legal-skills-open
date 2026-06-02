---
name: corporate-registry-investigation
title: corporate-registry-investigation
description: Use when users say "Companies House search", "investigate this UK company", "check officers/PSCs/charges", "registry snapshot", "group structure", "filing history", or need UK company profile, filings, risk leads, and registry evidence reviewed without unsupported allegations.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/corporate-registry-investigation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: corporate
language: en
tags: [companies-house, investigation, registry, due-diligence, uk]
---

# corporate-registry-investigation

## When to Use

- A user needs a quick company profile from Companies House records.
- A litigation, diligence, onboarding, or enforcement workflow needs officers, PSCs, charges, filings, or group indicators.
- The user wants risk signals from public registry material.

This skill reads registry evidence. It does not prove beneficial ownership beyond what the registry and supplied documents show.

## Audience and Work Shape

Audience: disputes, diligence, KYC, onboarding, conflicts, and in-house legal users doing first-pass UK registry review for lawyer or compliance review.

Work shape: pattern-matched review of registry evidence. The skill extracts and labels public registry facts and risk leads; it does not conclude wrongdoing, beneficial ownership, or suitability.

## Legal Failure Modes

- Legal support, not legal advice: registry outputs are investigative leads, not legal findings or allegations.
- Privilege/confidentiality: in litigation, enforcement, or internal-investigation contexts, outputs may form privileged or work-product material. Do not circulate outside the privilege group without lawyer approval.
- Accountability: the skill tabulates evidence and inferences; the lawyer or responsible reviewer decides what the evidence means and whether follow-up is required.

## Access Modes

This skill works in three modes:

1. **Live registry mode** - use browser, web search, MCP, API, or other configured access to retrieve Companies House pages, filings, officers, PSCs, charges, and filing history.
2. **User-supplied registry mode** - use company profile pages, filing PDFs, screenshots, API exports, CSVs, HTML, or pasted registry material supplied by the user.
3. **No-source mode** - prepare a company-number/name search plan and checklist, but do not state registry facts or risk signals.

If live Companies House access is unavailable and the user has not supplied registry material, ask for a company number, company-profile export, filing PDFs, screenshots, or source access. Do not fill registry facts from model memory.

## How It Works

### 1. Identify the company

Confirm:

- Company name.
- Company number, if known.
- Jurisdiction, usually England and Wales, Scotland, or Northern Ireland.
- Whether similarly named entities should be checked.

Prefer company number over name matching.

### 2. Pull registry snapshot

If live Companies House access is unavailable, ask the user for filings, screenshots, an API export, or company-profile text. State clearly whether findings are based on live registry access or user-supplied registry material.

Collect:

- Registered name and number.
- Status.
- Incorporation date.
- Registered office.
- SIC codes.
- Accounts status.
- Confirmation statement status.
- Filing history.
- Insolvency markers, if any.

Record retrieval date. Registry data changes. For each material fact, cite the filing name, filing date, transaction id, document id, or registry page from which it came.

### 3. Review people and control

Extract:

- Current and former officers.
- Persons with significant control.
- Appointment and resignation dates.
- Nationality, country of residence, and occupation where provided.
- Corporate officers or corporate PSCs.

Do not conflate individuals across companies by name alone. Use available identifiers such as month/year of birth, correspondence address, appointment dates, officer id, and source filing; if identity is uncertain, mark `possible_match_needs_verification`.

Flag evidence-based registry patterns requiring verification, such as rapid officer churn, repeated service-address or corporate-officer patterns, circular control, or missing PSC statements. Do not infer wrongdoing, nominee status, or control from nationality, residence, or name patterns alone.

### 4. Review charges and filings

Check:

- Outstanding and satisfied charges.
- Charge holders.
- Debenture or fixed/floating charge indicators.
- Recent accounts.
- Confirmation statements.
- Name changes.
- Registered office changes.
- Strike-off, restoration, insolvency, or liquidation filings.

When available, read filing text rather than relying only on filing titles.

### 5. Build relationship and risk summary

Produce:

- One-paragraph company summary.
- Timeline of material registry events.
- Officers and PSC table.
- Charges table.
- Filing red flags.
- Group-role indicators, such as parent, subsidiary, SPV, trading company, dormant company, or holding company.
- Follow-up searches needed.

Label red flags as investigative leads, not legal findings or allegations.

## Confidence Bands

- High: direct registry evidence from a live or user-supplied Companies House source.
- Medium: inference from a registry pattern, such as officer churn or unresolved charges.
- Low: possible identity match, group-role indicator, OCR-derived filing text, or unresolved ownership chain.

## Not in Scope

- Non-UK registry investigation.
- Sanctions, PEP, or adverse-media screening.
- KYC sign-off.
- Beneficial-ownership confirmation beyond registry evidence.
- Litigation or insolvency court-record searches unless separately sourced.
- Substantive accounts analysis without filing text and qualified review.

## Escalation

Stop and ask the responsible lawyer or reviewer when identity match is uncertain, filings are unreadable or scanned without OCR, ownership cannot be resolved from registry material, or a pattern would need to be characterised as wrongdoing to be useful.

### 6. Keep evidence and uncertainty separate

Use:

- `registry_evidence` for facts from Companies House.
- `inference` for conclusions drawn from patterns.
- `needs_verification` for anything requiring filings, contracts, accounts notes, court records, or non-registry sources.

Do not overstate public registry data.

## Example

```text
Investigate this UK company. Pull Companies House details, officers, PSCs, charges, filing history, accounts signals, and any red flags. Separate registry facts from inferences.
```

For a compact output pattern, see `examples/output.md`.
For the registry snapshot, filing extraction, risk-lead, and identity-caution model, see `references/companies-house-investigation-model.md`.

## Limitations

- Companies House data can be incomplete, stale, or self-reported.
- PSC data may not reveal ultimate beneficial ownership in complex structures.
- Accounts analysis requires reading filings, not just metadata.
- Registry red flags are leads, not findings.
