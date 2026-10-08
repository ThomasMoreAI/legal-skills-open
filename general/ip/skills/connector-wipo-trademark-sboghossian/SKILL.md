---
name: connector-wipo-trademark-sboghossian
title: Connector — WIPO Trademark (Global Brand Database)
description: Use when a lawyer or IP professional needs to search the WIPO Global Brand Database for existing trademark registrations — by mark name, owner, Nice class, or jurisdiction — as part of trademark clearance, freedom-to-operate analysis, brand due diligence, or Madrid Protocol application preparation. Free public API; rate-limited. Triggers on any trademark search, brand clearance, IP due diligence, or trademark conflict analysis across multiple jurisdictions including MENA, EU, UK, and international registrations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/connector/connector-wipo-trademark
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Connector — WIPO Trademark (Global Brand Database)

## What it does

The WIPO Global Brand Database aggregates trademark data from multiple national and international sources into a single searchable interface. The connector provides programmatic access to trademark searches as part of IP due diligence, clearance, and portfolio management workflows.

Coverage includes:
- International registrations under the **Madrid System** (WIPO-administered, ~130 member states including all major MENA jurisdictions).
- National trademark data from many participating IP offices (including USPTO, EUIPO, UK IPO, and selected MENA offices).
- Appellations of origin (geographical indications).

Key use cases:
- **Clearance search** before filing a new trademark application.
- **Due diligence** on a brand acquisition — identifying registered marks that could conflict.
- **Infringement triage** — checking whether a competitor's mark is registered and in what classes/jurisdictions.
- **Portfolio monitoring** — tracking the status of a client's existing international registrations.
- **Madrid Protocol filing prep** — confirming home-jurisdiction base registration before an international extension.

## Setup / auth

The WIPO Brand Database API (`branddb.wipo.int/branddb/api`) is a **public API with no authentication requirement** for basic searches.

However:
- Rate limits apply: implement a 1-second delay between requests to respect WIPO guidance.
- For high-volume searches (e.g., bulk portfolio monitoring), request a higher-quota access token from WIPO.
- Cache search results for 24 hours for non-urgent queries — trademark status changes infrequently.

## Understanding the search parameters

| Parameter | Description | Legal significance |
|---|---|---|
| Mark text | Word mark, transliteration, or phonetic equivalent | Search exact and similar marks |
| Owner/holder | Individual or entity name | Portfolio searches; ownership verification |
| Nice class | International Classification of Goods and Services (1–45) | Scope of protection |
| Vienna code | Figurative element classification | For device/logo marks |
| Jurisdiction | Country or WIPO member designation | Geographic scope |
| Filing date range | Date of first filing | Seniority / priority date |
| Status | Registered, expired, pending, opposed | Active vs lapsed rights |

## Nice classification — key classes for MENA legal-AI context

| Class | Goods/services | Relevance |
|---|---|---|
| 9 | Software, apps, electronic products | Legal-tech software trademark |
| 35 | Business services, data processing | Legal-ops SaaS services |
| 36 | Financial, insurance, legal services | Financial services — note: legal services are in Class 45 |
| 41 | Education, publishing | Legal training platforms |
| 42 | Scientific and technological services, IT | Technology services |
| 45 | Legal services, security services | All legal-service trademarks belong here |

For a legal-AI platform, the most relevant classes are **9, 35, 42, and 45**. A comprehensive trademark search for a legal-AI brand should check all four.

## Usage patterns

### Pattern 1 — Brand clearance before product launch

```
User: "Clear the brand 'LawPilot' for a UAE-based legal-AI SaaS"
→ Search WIPO Global Brand Database:
  - Mark: "LawPilot" (exact + phonetically similar)
  - Classes: 9, 35, 42, 45
  - Jurisdictions: UAE, GCC, international (Madrid Protocol designations including UAE)
→ Return:
  - Exact matches: list with owner, class, status, filing date
  - Phonetically similar: "LawPilot" vs "Law Pilot" vs "LoPilot"
  - Recommendation: proceed / caution / high-risk (based on hits)
```

### Pattern 2 — M&A brand due diligence

Before acquiring a company or brand:
- Retrieve all trademarks filed by or licensed to the target entity.
- Identify any registered marks in the relevant jurisdictions.
- Check for marks due for renewal (expiring in the next 12 months).
- Flag any opposition proceedings or cancellation actions noted in the status field.

### Pattern 3 — Madrid Protocol application — base registration check

For a Lebanese company wanting to extend its trademark internationally via Madrid Protocol:
- Confirm the base registration in Lebanon (via OEAP — Office de la Propriété Intellectuelle).
- Retrieve existing international designations (which countries the mark is already protected in).
- Identify target designation countries for the new application.

Note: WIPO Global Brand Database has varying coverage of Lebanese national trademark records. For authoritative Lebanese trademark search, [[connector-legal-data-hunter]] may provide better OEAP data.

### Pattern 4 — Competitor trademark monitoring

For a client concerned about brand infringement:
- Set up a periodic search (via [[connector-scheduled-tasks]]) for new trademark filings with:
  - Mark text similar to the client's brand.
  - Relevant Nice classes.
  - Target jurisdictions.
- Alert when a new application or registration is found that warrants review.

### Pattern 5 — Arabic brand transliteration check

For MENA brands, a trademark in Arabic script may also need protection for its transliterated Latin form (and vice versa). Search:
- Arabic script version.
- Most common Latin transliteration(s).
- Phonetic equivalents.

For example, the brand "حقوق" (Arabic for "rights") should also be checked as "Hquq," "Huquq," and "Huqqouq" across relevant jurisdictions.

## MENA trademark landscape

| Jurisdiction | Registry | Notes |
|---|---|---|
| UAE | UAE Ministry of Economy (MoE) trademark registry | UAE is a Madrid Protocol member; national and international registrations covered |
| KSA | SAIP (Saudi Authority for Intellectual Property) | Madrid Protocol member since 2020 |
| Lebanon | OEAP (Office de la Propriété Intellectuelle) | Limited digital infrastructure; WIPO coverage of Lebanese data is partial |
| Egypt | ITDA (Intellectual Property Rights Department) | WIPO coverage partial; in-country search recommended for clearance |
| DIFC | UK/EU registrations are recognized in practice; no separate DIFC trademark registry | DIFC-registered IP rights follow the underlying registration |
| ADGM | As DIFC | No separate ADGM registry |
| GCC | No unified GCC trademark system; each state registers separately | Filing in all 6 GCC states individually, or via Madrid System |

For MENA trademark matters, WIPO Global Brand Database is a starting point, not a complete clearance. National registry searches (particularly for UAE MoE and SAIP) should be conducted separately for comprehensive clearance opinions.

## Limits & professional responsibility

- **WIPO search ≠ clearance opinion.** A "no results" from the WIPO Brand Database does not mean a mark is free to use. It means no international registrations or covered national registrations were found. Unregistered but well-known marks (particularly relevant under UAE and Lebanon law) can also create rights. A qualified IP lawyer must sign off on any clearance opinion.
- **Coverage gaps.** Not all MENA national registries are fully indexed in the WIPO database. Advise the client that a local registry search is necessary for UAE, KSA, Egypt, and Lebanon.
- **Language and script.** Arabic-script searches require the Arabic text, not just a transliteration.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| No results for Arabic mark | Query sent in Latin only | Re-run with Arabic script; add transliterations |
| Stale status | Mark recently expired or renewed; database not yet updated | Note retrieval date; advise direct verification with the registry |
| Rate limited | Too many rapid queries | Implement per-query delay; queue bulk searches |
| Jurisdiction not covered | Some national registries not included | Note coverage gap; recommend local IP agent for the specific jurisdiction |

## Related skills

- [[connector-eur-lex]]
- [[connector-companies-house-uk]]
- [[connector-sec-edgar]]
- [[connector-legal-data-hunter]]
