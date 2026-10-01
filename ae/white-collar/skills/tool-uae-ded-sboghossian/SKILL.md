---
name: tool-uae-ded-sboghossian
title: UAE Department of Economic Development — Trade License Lookup
description: Use when performing KYC, counterparty verification, or due diligence on a UAE mainland company. Queries the Department of Economic Development (DED) trade license database of the relevant emirate to verify entity name, license type, expiry, permitted activities, shareholders, and authorized signatories. Critical before signing any commercial contract with a UAE onshore entity. Note that DIFC, ADGM, and free zone companies have separate registers — this tool covers mainland only.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-uae-ded
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ae
practice: white-collar
language: en
---

# UAE Department of Economic Development — Trade License Lookup

## What it does

This tool queries the Department of Economic Development (DED) trade license databases of UAE mainland emirates to retrieve authoritative entity information for UAE onshore companies. Each emirate maintains its own DED, and trade licenses are issued and managed at the emirate level.

This is the primary source of truth for corporate identity, licensed activities, and signatory authority for UAE mainland companies. For free zone entities, see [[tool-uae-freezone-registries]].

## Emirates and their DED equivalents

| Emirate | Authority | Portal |
|---------|-----------|--------|
| Dubai | Dubai Economy & Tourism (DET) — formerly Dubai DED | dubaided.gov.ae |
| Abu Dhabi | Abu Dhabi Department of Economic Development (ADDED) | aded.ae |
| Sharjah | Sharjah Economic Development Department (SEDD) | sedd.ae |
| Ras Al Khaimah | RAK Department of Economic Development | ded.rak.ae |
| Ajman | Ajman Department of Economic Development | ded.ajman.ae |
| Fujairah | Fujairah Economic Development Department | fujairahded.ae |
| Umm Al Quwain | UAQ DED | uaqded.ae |

Dubai and Abu Dhabi account for the vast majority of commercial entities. Most international counterparties are Dubai or Abu Dhabi licensed.

## Free zones — important distinction

The UAE has approximately 45 free zones. Free zone companies are **not** licensed by the DED — they are licensed by the free zone authority. This tool does not cover free zones. Key free zones and their registers:

| Free Zone | Authority | Notes |
|-----------|-----------|-------|
| DIFC (Dubai) | DIFC Registrar of Companies | English common law; own courts |
| ADGM (Abu Dhabi) | ADGM Registration Authority | English common law; own courts |
| DMCC (Dubai) | DMCC Authority | Gold and commodities |
| JAFZA (Dubai) | Jebel Ali Free Zone Authority | Industrial / logistics |
| Dubai Internet City / Media City | TECOM Group | Tech / media |
| DAFZA (Dubai) | Dubai Airport Free Zone | Aviation |
| Abu Dhabi Global Market (ADGM) | ADGM Registration Authority | Finance / professional services |
| Khalifa Industrial Zone (KIZAD) | AD Ports Group | Industrial |

For DIFC and ADGM entities, use the respective online company search portals directly. Their governance frameworks (DIFC Companies Law, ADGM Companies Regulations) differ materially from UAE mainland law.

## Setup / auth

| Parameter | Description | Required |
|-----------|-------------|----------|
| `licenseNumber` | Trade license number (format varies by emirate) | Conditional |
| `tradeName` | Company trade name (Arabic or English) | Conditional |
| `emirate` | `dubai` / `abudhabi` / `sharjah` / `rak` / `ajman` / `fujairah` / `uaq` | Recommended |
| `apiKey` | DED API credentials (where available) | Optional |

Dubai DET and Abu Dhabi ADDED provide partial APIs; other emirates are primarily scraping targets with web portals. Confirm API availability per emirate.

## Capabilities

### Trade license lookup
```
Input:  { licenseNumber: "1234567", emirate: "dubai" }
Output: {
  licenseNumber, tradeName, legalForm,
  licenseType: "commercial" | "industrial" | "professional" | "tourism",
  issuedBy, issuanceDate, expiryDate,
  status: "Active" | "Expired" | "Cancelled" | "Suspended",
  registeredAddress,
  activities: [{ code, description }],
  shareholders: [{ name, nationality, sharePercentage }],
  managers: [{ name, nationality, role }],
  authorizedSignatories: [{ name, designation }],
  capitalAmount, currency
}
```

### Trade name search
```
Input:  { tradeName: "Acme Trading", emirate: "abudhabi" }
Output: [ { licenseNumber, tradeName, legalForm, status, licenseExpiry } ]
```

### Activity code lookup
UAE activities are coded using a standard code list (different from Nice classes). For example:
- 7020: Management consultancy
- 6201: Computer programming activities
- 4619: Other goods wholesale
- 6619: Other financial service activities (not insurance or pension funding)

Confirming that the activity code in the license covers the subject matter of the contract is a critical KYC step.

## Key fields for legal due diligence

### Legal form
| UAE Form | Description | Key feature |
|---|---|---|
| LLC (Limited Liability Company) | Most common; 1 to unlimited shareholders | Foreign ownership now 100% permitted in most activities (post-2021 reform) |
| Branch of Foreign Company | Extension of parent; no separate legal personality | Parent is liable |
| Civil Company | Professional service firms (law, medicine, accounting) | Emirate-level registration |
| Free Zone Company | Established in and licensed by free zone | Free zone law governs; not DED |
| Joint Stock Company (PJSC/PSC) | Public or private; SCA-regulated for PJSCs | Complex governance requirements |

### License expiry
A UAE trade license is renewed annually. An expired license is a critical due diligence flag:
- An entity with an expired license cannot legally engage in business activities
- Banks typically suspend accounts for expired-license holders
- Signatories may lack authority to bind the entity once the license lapses

Always check `expiryDate` and note if it expires within 30 days — flag for the user.

### Authorized signatories and authority
The trade license lists managers and authorized signatories. However, the scope of authority (unlimited signing authority vs. limited to specific amounts or categories) is typically found in:
- The MOA (Memorandum of Association — عقد التأسيس)
- A specific power of attorney

Request the MOA if the signatory's authority is not clear from the license.

### Post-2021 company law reforms
UAE Federal Decree-Law No. 32 of 2021 (Commercial Companies Law) introduced significant changes:
- 100% foreign ownership now permitted for LLCs in most sectors (previously required 51% UAE national shareholder)
- New corporate governance requirements for larger companies
- Simplified single-person company (SPC) form
- Enhanced shareholder rights

When reviewing older contracts or corporate structures pre-dating 2021, note that the sponsorship / UAE national shareholder structure may have been restructured.

## Cross-reference requirements

For complete KYC on a UAE mainland entity:

| Tool | Purpose |
|------|---------|
| [[tool-un-sanctions]] | UN Security Council consolidated list — baseline for all UAE transactions |
| [[tool-ofac-sanctions]] | US SDN list — critical given UAE's USD-denominated economy |
| UAE Central Bank (CBUAE) | For financial institutions: licensing and AML status |
| SCA (Securities and Commodities Authority) | For listed companies and investment firms |
| MOJ (Ministry of Justice) | Notarized documents and court records |

## Common pitfalls

- **Free zone company presented as DED-licensed**: a common error in commercial practice. Check whether the license issuer is a DED or a free zone authority.
- **License scope mismatch**: counterparty's license lists "general trading" but the contract involves a specifically regulated activity (financial services, healthcare, food). Verify sub-licensing requirements.
- **Individual vs company**: some UAE businesses operate under a sole proprietorship license (license holder = individual) rather than a company license. The individual is personally liable.
- **Manager vs authorized signatory**: the "manager" shown on the license may not be the person authorized to sign external contracts. Check the MOA for scope of signing authority.
- **Multiple entities in a group**: UAE groups often have the same trade name for multiple entities in different emirates or free zones. Confirm the exact legal entity and license number.

## Output schema

```json
{
  "licenseNumber": "1234567",
  "tradeName": "Acme Trading LLC",
  "legalForm": "LLC",
  "issuedBy": "Dubai Economy & Tourism",
  "emirate": "Dubai",
  "status": "Active",
  "issuanceDate": "2018-03-15",
  "expiryDate": "2026-03-14",
  "expiryWarning": false,
  "activities": [
    { "code": "7020", "description": "Management Consultancy" }
  ],
  "shareholders": [
    { "name": "John Smith", "nationality": "GB", "sharePercentage": 100 }
  ],
  "authorizedSignatories": [
    { "name": "Jane Doe", "designation": "General Manager" }
  ],
  "registeredAddress": "...",
  "capitalAmount": 300000,
  "currency": "AED",
  "source": "Dubai Economy & Tourism",
  "fetchedAt": "2026-05-14T10:00:00Z"
}
```

## Related skills

- [[tool-ksa-moc]] — KSA Ministry of Commerce registry (parallel tool for Saudi entities)
- [[tool-lb-commercial-register]] — Lebanon commercial register (parallel tool for Lebanese entities)
- [[tool-un-sanctions]] — UN consolidated list screening
- [[tool-ofac-sanctions]] — US OFAC SDN screening
- [[research-beneficial-ownership-lookup]] — UBO tracing beyond DED share-register layer
