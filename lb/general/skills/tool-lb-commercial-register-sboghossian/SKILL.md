---
name: tool-lb-commercial-register-sboghossian
title: Lebanon Commercial Register (Sijil al-Tijari)
description: Use when performing KYC, counterparty verification, or corporate due diligence on a Lebanese entity. Queries the Lebanon Commercial Register (Sijil al-Tijari) held at the Mohafaza commercial courts to retrieve company form, capital, partners, board composition, statutory auditor, and encumbrances. Essential before signing commercial contracts with Lebanese parties; important caveat on data freshness given court-system delays.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-lb-commercial-register
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: lb
practice: general
language: en
---

# Lebanon Commercial Register (Sijil al-Tijari)

## What it does

This tool queries the Lebanese commercial registry system to retrieve authoritative corporate identity information for Lebanese entities. The register is maintained by the commercial courts (Tribunaux de Commerce) attached to each of the six governorates (Mohafazat): Beirut, Mount Lebanon, North Lebanon, South Lebanon, Bekaa, and Nabatieh.

Lebanon's commercial law is codified in the Code de Commerce du Liban (Legislative Decree 304/1942 as amended), which requires all commercial entities to register and keep their register entries current.

## Registry structure by governorate

| Governorate | Court | Coverage |
|-------------|-------|---------|
| Beirut | Tribunal de Commerce de Beyrouth | Largest; covers greater Beirut and most holding companies |
| Mount Lebanon | Tribunal de Commerce du Mont-Liban (Baabda) | Suburbs + Metn, Kesrouan, Chouf, Aley |
| North Lebanon | Tribunal de Commerce du Nord (Tripoli) | North + Akkar |
| South Lebanon | Tribunal de Commerce du Sud (Saida) | South + Jezzine |
| Bekaa | Tribunal de Commerce de la Bekaa (Zahle) | Bekaa valley |
| Nabatieh | Tribunal de Commerce de Nabatieh | South governorate |

For the vast majority of commercial and holding structures, the Beirut register is the relevant register. Off-shore holding companies (société offshore) are registered exclusively with the Beirut register.

## Setup / auth

| Parameter | Description | Required |
|-----------|-------------|----------|
| `registrationNumber` | Registry number in format `[number]/[year]` (e.g., `12345/2019`) | Conditional |
| `companyName` | Arabic or French name for search | Conditional |
| `governorate` | Filter search to a specific court registry | No — defaults to all |

## Capabilities

### Registration number lookup
```
Input:  { registrationNumber: "12345/2019" }
Output: {
  registrationNumber, companyNameAr, companyNameFr,
  legalForm, registrationDate, governorate,
  capital: { declared, paidUp, currency },
  objectClause, address,
  partners: [{ name, nationality, shares, shareClass }],
  boardMembers: [{ name, role, nationality }],
  statutoryAuditor: { firm, appointedDate },
  mortgages: [...],
  bankruptcyStatus, liquidationStatus,
  lastModified
}
```

### Company name search
```
Input:  { companyName: "Société XYZ SARL", governorate: "Beirut" }
Output: [ { registrationNumber, companyName, form, status, lastModified } ]
```

## Key fields and their legal significance

### Legal forms (formes sociales)

| Abbreviation | French | English equivalent | Liability |
|---|---|---|---|
| SAL | Société Anonyme Libanaise | Joint stock company (JSC) | Limited to capital |
| SARL | Société à Responsabilité Limitée | LLC | Limited to capital |
| SNC | Société en Nom Collectif | General partnership | Unlimited / joint & several |
| SCS | Société en Commandite Simple | Limited partnership | Mixed |
| Société Offshore | Offshore holding company | Offshore holding | Limited |
| SFC | Société Financière de Crédit | Financial credit company | Specific license |

**SAL vs SARL distinction**: In a SAL, shareholders are not publicly listed in the register (the register shows the board only); verify shareholding via a notarized shareholder register extract. In a SARL, partners and their percentage shares are registered and publicly visible.

### Capital
Both declared capital and paid-up capital are shown where available. Under Lebanese law, the full SAL capital must be subscribed at formation; SARL capital must be fully paid in. Note that in the context of Lebanon's currency crisis post-2019, capital figures denominated in Lebanese Pounds (LBP) carry significant nominal inflation distortion — USD-denominated capital clauses are more meaningful.

### Object clause
Verify the object clause covers the subject matter of the proposed transaction. A company acting outside its object clause may create ultra vires arguments, though Lebanese courts have generally taken a permissive approach.

### Partners / shareholders
- For SARLs: partners and their exact share percentages are registered. Cross-reference with AML UBO rules (BDL Circular 126 and subsequent circulars require CDD on beneficial owners above 25%).
- For SALs: the register shows board members and company officers, not necessarily shareholders. Request a notarized extract from the internal shareholder register or minutes of the most recent general assembly.

### Mortgages and encumbrances
The register records pledges over shares (gage sur parts sociales) and certain commercial mortgages (nantissement de fonds de commerce). However, bank pledge arrangements registered with BDL or individual banks are not necessarily reflected here. For high-value transactions, supplement with searches at the relevant notary (كاتب العدل / notaire) and BDL.

### Bankruptcy / liquidation
The register reflects judicial liquidation orders (faillite, liquidation judiciaire) and voluntary dissolution resolutions. However, there is often a lag of weeks to months between a court order and the register entry. For time-sensitive transactions, obtain a recent certificate from the court clerk (greffier) stating no pending proceedings.

## Data freshness warning

Lebanon's commercial register suffers from well-documented administrative delays. The Beirut court registry is the slowest of the six governorates, sometimes running 6–18 months behind. For any high-stakes transaction:

1. **Request a fresh notarized excerpt** (extrait du registre de commerce) from the relevant court — this is the authoritative primary source.
2. **Do not rely on database records alone** for mergers, acquisitions, or secured lending.
3. **For SALs**, additionally request a recent procès-verbal of the general assembly and board meeting minutes.

## Offshore companies (Sociétés Offshore)

Lebanese offshore companies (Law 19/1999) are registered with the Beirut commercial register but have restricted access to the Lebanese market. They are commonly used as regional holding structures. Key characteristics:
- Cannot conduct business in Lebanon with Lebanese residents (with limited exceptions)
- Exempt from most Lebanese taxes on foreign-source income
- Annual fee of USD 600 or equivalent
- Increasing scrutiny under FATF and BDL Circular 126 for UBO disclosure

For offshore company counterparties, UBO verification beyond the register layer is mandatory — see [[research-beneficial-ownership-lookup]].

## AML / KYC regulatory context

Banque du Liban (BDL) Circular 126 (and its successors) imposes enhanced due diligence requirements on Lebanese financial institutions for legal persons. Key requirements:
- Identify and verify UBOs above 25% threshold
- Obtain resolution authorizing the signatory
- Annual update for ongoing business relationships

Post-2019, Lebanon is subject to enhanced international scrutiny. FATF has flagged Lebanon's AML framework as requiring improvement. For cross-border transactions, counterparties may demand enhanced documentation packages regardless of the register data.

## Output schema

```json
{
  "registrationNumber": "12345/2019",
  "court": "Tribunal de Commerce de Beyrouth",
  "companyNameFr": "Société XYZ SARL",
  "companyNameAr": "شركة ...",
  "legalForm": "SARL",
  "status": "Active",
  "registrationDate": "2019-06-10",
  "capital": { "declared": 30000000, "paidUp": 30000000, "currency": "LBP" },
  "objectClause": "...",
  "partners": [...],
  "boardMembers": [...],
  "statutoryAuditor": { "firm": "...", "appointedDate": "..." },
  "mortgages": [],
  "bankruptcyStatus": "None",
  "lastModified": "2023-11-01",
  "source": "Sijil al-Tijari — Lebanon Commercial Register",
  "freshnessWarning": true,
  "fetchedAt": "2026-05-14T10:00:00Z"
}
```

## Related skills

- [[research-beneficial-ownership-lookup]] — UBO tracing beyond the share register layer
- [[tool-un-sanctions]] — UN consolidated list screening (critical for Lebanon given regional conflict exposure)
- [[tool-ofac-sanctions]] — US OFAC SDN screening (Lebanon has active US sanctions programs)
- [[tool-ksa-moc]] — KSA commercial registry (parallel tool for Saudi entities)
- [[tool-uae-ded]] — UAE DED registry (parallel tool for UAE entities)
