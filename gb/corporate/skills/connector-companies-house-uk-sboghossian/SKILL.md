---
name: connector-companies-house-uk-sboghossian
title: Connector — Companies House UK
description: Use when a lawyer or due-diligence analyst needs to retrieve corporate information about a UK-registered company — including registered address, directors, filing history, charges, annual accounts, and confirmation statements — from Companies House, the UK's official corporate registry. Free and comprehensive public API; no auth required. Triggers on due diligence, counterparty checks, corporate structure analysis, or any request for a UK company's statutory information.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/connector/connector-companies-house-uk
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: corporate
language: en
---

# Connector — Companies House UK

## What it does

Companies House is the UK's official registrar of companies, maintained by the UK government. Every company incorporated in England & Wales, Scotland, or Northern Ireland must file statutory information here. The connector provides read access to the Companies House public API, enabling automated corporate due diligence, counterparty verification, and corporate structure analysis within legal-AI workflows.

Key data available:
- Company name, number, and registered office address.
- Incorporation date and company type (Ltd, PLC, LLP, etc.).
- Current and resigned directors and persons with significant control (PSC).
- Filed accounts (annual reports, abbreviated accounts).
- Confirmation statements (annual return equivalents).
- Mortgage and charge register (secured lending registered against the company).
- Insolvency and dissolution status.
- Overseas companies registered in the UK.

## Setup / auth

The Companies House API is **publicly accessible** — no OAuth or API key is required for basic company search and profile retrieval.

However, for production use at scale (>600 requests/minute), register for a free Companies House API key:
- Register at: `developer.company-information.service.gov.uk`
- Key is free; rate limits are generous for legal research volumes.
- Key stored in the platform secrets manager; included in the `Authorization` header as a Basic Auth username (password left blank).

## Capabilities

| Capability | API endpoint | Notes |
|---|---|---|
| Search companies by name | `/search/companies` | Returns up to 20 results; paginated |
| Company profile | `/company/{company_number}` | Full statutory profile |
| Officers (directors) | `/company/{company_number}/officers` | Current + resigned, with appointment dates |
| Persons with significant control | `/company/{company_number}/persons-with-significant-control` | 25%+ shareholders / beneficial owners |
| Filing history | `/company/{company_number}/filing-history` | All filed documents with download links |
| Charges (mortgages) | `/company/{company_number}/charges` | Outstanding and satisfied charges |
| Insolvency | `/company/{company_number}/insolvency` | Liquidation, administration, CVA status |
| Registered address history | Via filing history | Requires parsing previous confirmation statements |

## Usage patterns

### Pattern 1 — Quick counterparty check before contract

```
User: "Check Acme Global Ltd before we sign the SPA"
→ Search Companies House for "Acme Global Ltd"
→ Return: company number, incorporation date, registered address, 
  current directors, PSC, any charges or insolvency flags
→ Flag: any unusual findings (recently incorporated, dormant accounts, outstanding charges)
```

### Pattern 2 — Director disqualification check

Before appointing an individual as a director of a UK subsidiary, verify they are not subject to a director disqualification order. The Companies House API does not directly expose disqualification data, but the Insolvency Service maintains a separate disqualified directors register accessible via the Companies House search. Surface this as a separate check step.

### Pattern 3 — Corporate structure mapping for M&A due diligence

For a target company, use the PSC register to map the beneficial ownership chain up to the ultimate beneficial owner (UBO). Cross-reference UBOs against [[connector-ofac-sanctions]] for sanctions screening.

Note: UK PSC rules require companies to disclose individuals with >25% shareholding or significant influence. Shell structures using nominee shareholders can obscure UBOs — flag if the PSC register shows only corporate PSCs with no individual UBO disclosed.

### Pattern 4 — Charge register review for lending

Before a secured lending transaction, retrieve all registered charges:
- Outstanding charges: active security interests the borrower has granted.
- Satisfied charges: historical security fully discharged.
- Fixed vs floating charge classification.
- Charge holder identity (useful for identifying existing lender relationships).

## MENA relevance

UK Companies House lookups are relevant in MENA legal practice in several scenarios:
- **DIFC / ADGM entities** with UK-registered holding companies (common for MENA PE structures).
- **Lebanese diaspora businesses** with UK-incorporated entities as the operating vehicle.
- **MENA companies listed on the London Stock Exchange (LSE or AIM)** — counterparty diligence before signing English-law governed contracts.
- **KSA family groups** with UK holding structures — PSC register is the starting point for corporate structure mapping.

## Permissions & safety

- **Public data only.** Companies House data is fully public; no PII restrictions apply to the data itself.
- **Accuracy caveat.** Companies House data is only as accurate as the last filed document. Addresses and directors may be stale by up to 12 months (the filing cycle). Always note the "last filed" date.
- **No write access.** The connector cannot file documents with Companies House. Any statutory filing (confirmation statement, change of directors, charge registration) must be done through a licensed company secretary or solicitor.
- **Rate limits.** Respect the 600 requests/minute limit. Implement exponential backoff on `429 Too Many Requests`.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| Company not found | Dissolved, non-UK, or name misspelling | Try by company number; suggest checking HMRC or the Insolvency Register |
| Stale filing data | Company behind on filings (compliance failure) | Flag the filing gap as a diligence concern |
| PSC "exempt" | Company is listed or qualifies for PSC exemption | Note; source UBO from prospectus or regulatory disclosure |
| Overseas company | Non-UK company registered for UK filing purposes | Profile will be limited; use home-jurisdiction registry for primary data |
| API `503` | Companies House maintenance window (common on weekends) | Retry; note that Companies House undergoes periodic planned maintenance |

## Related skills

- [[connector-eur-lex]]
- [[connector-sec-edgar]]
- [[connector-wipo-trademark]]
- [[connector-legal-data-hunter]]
- [[connector-ofac-sanctions]]
