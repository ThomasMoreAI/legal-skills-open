---
name: tool-companies-house-uk-sboghossian
title: Tool — UK Companies House Registry
description: Use when performing KYC/UBO research, pre-transaction due diligence, or credit checks on UK-registered companies and their officers. UK Companies House is the world's most comprehensive free corporate registry — covering full filing history, director and PSC registers, charges, and insolvency filings. Particularly useful in MENA deals where UK holding structures, UK subsidiaries, or UK-based officers are common.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-companies-house-uk
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: corporate
language: en
---

# Tool — UK Companies House Registry

## What it does

Queries the UK Companies House (CH) public registry to retrieve corporate information, officer data, PSC (People with Significant Control) records, filing history, charges, and insolvency filings for any company registered in England & Wales, Scotland, or Northern Ireland.

Companies House is widely considered the world's most open and comprehensive free corporate registry. It is frequently the most accessible first entry point for due diligence on MENA deals because many BVI, Cayman, and GCC holding structures maintain a UK subsidiary or have UK-based directors.

## Setup / auth

- **Free public API:** Companies House provides a public API (https://developer.company-information.service.gov.uk/) requiring an API key (free, self-registered).
- **Rate limits:** 600 requests per 5-minute window per API key; implement caching for repeated lookups on the same company.
- **Data freshness:** Filed documents typically appear within 24–72 hours of submission at CH. For real-time solvency risk, supplement with credit-bureau data.

## Capabilities

### Search modes

| Mode | Input | Returns |
|---|---|---|
| Company number lookup | `company_number` (8-digit, e.g., `12345678`) | Full company profile, status, registered address, SIC code |
| Company name search | `company_name` (partial match supported) | List of matching companies with numbers and status |
| Officer search | `officer_name` | All directorships (current + historic) for the individual |
| PSC search | `psc_name` | All PSC registrations linked to the individual/entity |
| Insolvency search | `company_number` | Insolvency practitioners, proceedings, and status |

### Data retrievable

| Data category | Description | KYC relevance |
|---|---|---|
| **Company profile** | Registered address, SIC, incorporation date, company type, status (active/dissolved/in-liquidation) | Basic entity verification |
| **Officer register** | Directors, secretaries, LLP members — name, DOB, nationality, appointment/resignation dates | Who controls the company |
| **PSC register** | Persons or legal entities with >25% ownership or control | UBO (Ultimate Beneficial Owner) identification |
| **Filing history** | Annual returns, confirmation statements, accounts, mortgage charges | Financial health, compliance track record |
| **Charges register** | Fixed and floating charges, debentures — creditor, creation date, status | Security encumbrances on assets |
| **Accounts** | Filed annual accounts (micro, small, full) | Financial snapshot; note that small companies file abridged accounts |
| **Insolvency filings** | CVA, administration, liquidation, winding-up petitions | Solvency red flags |

## Output schema

```json
{
  "companyNumber": "12345678",
  "companyName": "Gulf Holdings UK Limited",
  "status": "active",
  "incorporationDate": "2019-03-15",
  "registeredAddress": "1 King Street, London, EC2V 8AU",
  "sicCode": "64999",
  "officers": [
    {
      "name": "Al Rashidi, Mohammed Fahad",
      "role": "Director",
      "nationality": "Saudi",
      "appointedOn": "2019-03-15",
      "resignedOn": null,
      "dob": { "month": 6, "year": 1978 }
    }
  ],
  "pscs": [
    {
      "name": "Gulf Capital SAOC",
      "kind": "corporate-entity",
      "naturesOfControl": ["ownership-of-shares-75-to-100-percent"],
      "notifiedOn": "2019-03-15"
    }
  ],
  "charges": [],
  "insolvency": null,
  "filingHistoryUrl": "https://find-and-update.company-information.service.gov.uk/company/12345678/filing-history"
}
```

## Usage patterns

### Pattern 1 — Pre-acquisition KYC

Client is acquiring a UK target. Run Companies House search to:
1. Confirm company status and registered address
2. Extract full officer list and cross-check with sanctions databases
3. Map PSC chain to identify UBOs
4. Review charges register for undisclosed security interests

### Pattern 2 — MENA deal — UK holding company

A UAE family office holds UK real estate through a UK SPV. Run CH to:
1. Identify the SPV and confirm it is active (not dormant or dissolved)
2. Confirm directors match the counterparty's representations
3. Extract PSC register to verify ownership chain consistency with deal documents

### Pattern 3 — Officer background check

Run officer name search to surface all historical directorships — including resigned positions and involvement in dissolved or liquidated companies — as part of a background check.

### Pattern 4 — Insolvency screening

Before extending credit or entering a significant contract, run insolvency check to confirm no winding-up petition, administration, or CVA in progress.

## Permissions & safety

- Return only publicly available Companies House data; do not attempt to access non-public records.
- PSC DOB and officer full DOB are available to the full digit for anti-fraud purposes under the Economic Crime (Transparency and Enforcement) Act 2022; handle personal data in accordance with UK GDPR.
- Do not represent a clean Companies House result as a clean AML check — Companies House is one layer; also check OFAC, HMT, and EU sanctions for all principals.

## Failure modes

| Failure | Response |
|---|---|
| Company not found | Return 0 results; suggest searching by registered number (more reliable than name) |
| Company dissolved/struck off | Return status prominently; warn that the entity may not be valid for contracting |
| PSC register shows "exemption applied" | Flag that UBO transparency is claimed to be exempt (e.g., listed company); note the listed exchange |
| Charges register shows unreleased charge | Flag prominently; advise review of the charge document and confirmation of release before title transfer |

## Related skills

- [[tool-adgm-courts-search]]
- [[tool-difc-courts-search]]
- [[research-kyc-ubo]]
- [[review-due-diligence]]
