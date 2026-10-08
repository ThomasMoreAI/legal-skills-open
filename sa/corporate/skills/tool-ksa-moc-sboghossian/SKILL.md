---
name: tool-ksa-moc-sboghossian
title: KSA Ministry of Commerce — Commercial Registry Tool
description: Use when performing KYC, due diligence, or counterparty verification for a Saudi Arabian entity. Queries the KSA Ministry of Commerce (MOC) commercial registration (Sijil Tijari) database to retrieve entity name, activities, authorized signatories, corporate form, and share encumbrances. Essential before signing any commercial contract with a Saudi party or conducting KYC under Saudi AML frameworks.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-ksa-moc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: sa
practice: corporate
language: en
---

# KSA Ministry of Commerce — Commercial Registry Tool

## What it does

This tool queries the Saudi Ministry of Commerce (MOC) Sijil Tijari (Commercial Registration) database to retrieve authoritative entity information for Saudi Arabian companies and sole establishments. It is the primary source of truth for corporate identity, authorized activities, and signatory authority in KSA commercial transactions.

Source: https://mc.gov.sa/

## Setup / auth

| Parameter | Description | Required |
|-----------|-------------|----------|
| `crNumber` | 10-digit Commercial Registration number | Conditional |
| `entityName` | Arabic or transliterated entity name for search | Conditional |
| `ownerNationalId` | Saudi national ID or Iqama for owner-based search | Conditional |
| `apiKey` | MOC API credentials (if using e-services gateway) | Recommended |

At minimum, provide either `crNumber` or `entityName`. Direct CR number lookup is faster and more precise.

## Capabilities

### CR number lookup
```
Input:  { crNumber: "1010XXXXXXX" }
Output: {
  crNumber, entityNameAr, entityNameEn,
  legalForm, capital, paidUpCapital,
  activities: [{ code, descriptionAr, descriptionEn }],
  partners: [{ nameAr, nameEn, nationalId, sharePercentage }],
  authorizedSignatories: [{ name, idNumber, signingAuthority }],
  crExpiryDate, registrationDate,
  status: "Active" | "Suspended" | "Cancelled",
  encumbrances: { mortgages: [...], attachments: [...] }
}
```

### Owner / individual search
```
Input:  { ownerNationalId: "1XXXXXXXXX" }
Output: [ { crNumber, entityName, form, status, expiryDate } ]
```
Lists all commercial registrations held by a given individual — useful for UBO mapping.

### CR expiry monitoring
Flag entities whose CR expires within 30, 60, or 90 days — a CR expiry renders the entity legally incapacitated to contract until renewal.

## Key fields for legal due diligence

### Legal form
| Form (Arabic) | Form (English) | Notes |
|---------------|----------------|-------|
| شركة ذات مسؤولية محدودة | LLC (Sharikat Mas'ouliyya Mahdouda) | Most common; partners liable up to capital |
| شركة مساهمة | JSC (Sharikat Musahama) | Public or closed; shares transferable |
| مؤسسة فردية | Sole Establishment | Owner has unlimited personal liability |
| شركة مساهمة مبسطة | Simplified JSC | 2024+ reform; one-person possible |
| شركة قابضة | Holding Company | Requires MISA license if foreign-owned |

### Object clause (نشاط — Nashat)
The activities listed in the CR define the legal scope of the entity's operations. A company cannot legally bind itself to a contract that falls outside its listed activities. Always verify that the counterparty's نشاط covers the subject matter of the agreement.

### Authorized signatories
The CR lists who may sign on behalf of the entity and in what capacity. Verify that the person signing a contract:
1. Appears in the CR as an authorized signatory, **and**
2. Has the specified scope of authority (unlimited, limited to certain transaction sizes, etc.)

Boards of directors of JSCs may grant additional powers of attorney (توكيل رسمي); request a notarized PoA if the signatory is not listed in the CR.

### Capital and encumbrances
- Paid-up capital is relevant for assessing the entity's financial capacity to perform.
- Share mortgages (رهن حصص) are partially visible in the CR — note that MOC visibility is limited and does not reflect all bank pledge arrangements. Supplement with notary (كاتب العدل) searches for pledge filings.

## Cross-reference requirements

For a complete KYC / due diligence package on a Saudi entity, always pair this tool with:

| Tool | Purpose |
|------|---------|
| [[tool-un-sanctions]] | UN Security Council sanctions screening |
| [[tool-ofac-sanctions]] | US SDN screening — critical if any USD payments or US nexus |
| MISA (Ministry of Investment) | For foreign-invested entities: MISA license number confirms permitted foreign shareholding |
| ZATCA (Zakat, Tax & Customs Authority) | VAT registration verification for supply contracts |
| SAMA (Saudi Central Bank) | For financial institutions: licensing and prudential status |

## AML / KYC regulatory context

KSA AML/CTF obligations are governed by the Anti-Money Laundering Law (Royal Decree M/31) and SAMA's Customer Due Diligence Rules. For a Saudi-domiciled legal person, mandatory KYC documentation includes:

1. Certified CR extract (not older than 3 months for high-risk transactions)
2. Articles of association (نظام الشركة)
3. Board resolution authorizing the signatory (for JSCs)
4. National IDs of UBOs above 25% threshold
5. Proof of registered address

SAMA and SAMA-supervised entities must also verify the entity against the Financial Intelligence Unit (SAFIU) watch lists.

## Common pitfalls

- **CR not renewed**: many KSA entities defer CR renewal; a lapsed CR is a significant red flag. Always check the expiry date.
- **Multiple CRs**: a group may operate through a head-office CR plus regional branch registrations. Confirm which CR is the contracting entity.
- **eFawateer billing mismatch**: for procurement contracts, the billing entity's CR must match the party shown on ZATCA invoices (Fatoorah e-invoicing system).
- **Activity scope creep**: especially in tech/fintech deals, the counterparty's CR activities may predate the digital economy — check for "e-commerce" or "information technology" in the listed activities.
- **Non-Saudi-citizen partners**: foreign partners in LLCs may appear in the CR but require a valid residency permit (Iqama) and MISA clearance. Verify independently.

## Output schema

```json
{
  "crNumber": "1010XXXXXXX",
  "entityNameAr": "شركة ...",
  "entityNameEn": "... Company",
  "legalForm": "LLC",
  "status": "Active",
  "crExpiryDate": "2026-03-15",
  "capital": 500000,
  "paidUpCapital": 500000,
  "currency": "SAR",
  "activities": [...],
  "partners": [...],
  "authorizedSignatories": [...],
  "encumbrances": { "mortgages": [], "attachments": [] },
  "source": "MOC Sijil Tijari",
  "fetchedAt": "2026-05-14T10:00:00Z"
}
```

## Related skills

- [[tool-un-sanctions]] — UN consolidated list screening
- [[tool-ofac-sanctions]] — US OFAC SDN list screening
- [[tool-uae-ded]] — UAE Department of Economic Development registry (parallel tool for UAE entities)
- [[tool-lb-commercial-register]] — Lebanon commercial register (parallel tool for Lebanese entities)
- [[research-beneficial-ownership-lookup]] — UBO tracing beyond the share register layer
