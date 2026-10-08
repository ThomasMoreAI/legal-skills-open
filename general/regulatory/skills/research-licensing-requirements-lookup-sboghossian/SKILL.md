---
name: research-licensing-requirements-lookup-sboghossian
title: Licensing Requirements Lookup
description: 'Use when a business or its advisors need to identify every license required to operate a specific business activity in a specific jurisdiction — covering commercial licenses, sector-specific regulatory licenses (financial, healthcare, food, education, legal, accounting), professional licenses, and ancillary compliance requirements (labor, data protection, environmental). MENA-first: covers UAE (onshore + DIFC + ADGM + free zones), KSA, Lebanon, and Egypt with sector-level regulator details.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/research/research-licensing-requirements-lookup
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Licensing Requirements Lookup

Given a business activity and target jurisdiction, identify all licenses, permits, and approvals required to operate lawfully. Covers the full licensing stack: commercial registration, sector-specific regulatory licenses, professional licenses, and ancillary compliance obligations.

## When to use this

- Setting up a new business in a MENA jurisdiction
- Expanding an existing business into a new sector or jurisdiction
- Advising a client on the regulatory gap between their current licenses and the activities they want to undertake
- Pre-acquisition due diligence: does the target hold all required licenses?
- Responding to a regulator inquiry or enforcement action about unlicensed activity

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Business activity (specific) | Licensing requirements are activity-specific, not company-type-specific — "offering investment advice" triggers different licenses than "managing a fund" | Required — be specific |
| Target jurisdiction | UAE onshore vs DIFC vs ADGM vs KSA vs LB have entirely different regimes | Required |
| Entity type | LLC, branch, free-zone company, representative office — affects available license categories | Provide if known |
| Nationality of owners | Many MENA jurisdictions have foreign-ownership restrictions or special regimes | Relevant for UAE, KSA, LB |
| Intended client base | B2B vs B2C; retail vs professional clients — affects regulatory classification | Provide if relevant |
| Timeline | Some licenses have long lead times; urgency affects sequencing advice | Provide if known |

## License categories and issuing bodies

### 1. Commercial license (foundation layer)

Every business operating in a jurisdiction needs a base commercial license from the relevant commercial authority. Without this, sector licenses typically cannot be obtained.

| Jurisdiction | Authority | License type | Ownership rules |
|---|---|---|---|
| Dubai onshore | Dubai Economy and Tourism (DET, formerly DED) | Commercial / professional / industrial | UAE nationals or GCC nationals must hold ≥ 51% for most onshore LLCs (some activities exempt under FDI Law Federal Decree-Law No. 26 of 2020) |
| Abu Dhabi onshore | Department of Economic Development Abu Dhabi (ADDED) | Commercial / professional / industrial | Same 51% rule applies; foreign branch structures available |
| UAE Federal | Ministry of Economy (MOE) for national companies | Federal commercial registration | Varies |
| UAE Free zones (JAFZA, DMCC, DIFC, ADGM, TECOM, etc.) | Each free zone authority (e.g., JAFZA for Jebel Ali; DMCCA for DMCC; DIFC Authority) | Free zone company license | 100% foreign ownership; activities restricted to those permitted in the free zone's approved activity list |
| KSA | Ministry of Commerce (MOC) via Qiyas portal | Commercial registration (Sijil Tijari) + entity registration | Foreign investors: minimum capital requirements apply; 100% foreign ownership now permitted in most sectors under Vision 2030 reforms |
| Lebanon | Commercial Register (Registre du Commerce) at relevant court | Commercial entity registration (SAL, SARL, etc.) | No restrictions on foreign ownership for most sectors; special rules for banking, media, real estate |
| Egypt | General Authority for Investment (GAFI) | Investment registration + commercial registration | Foreign ownership rules vary by sector; GAFI provides unified window |

### 2. Sector-specific regulatory licenses

#### Financial services

| Jurisdiction | Regulator | License types |
|---|---|---|
| UAE onshore | Securities and Commodities Authority (SCA) | Investment advisor, fund manager, broker-dealer, exchange license |
| DIFC | Dubai Financial Services Authority (DFSA) | Category 1–4 licenses (banking, asset management, advice, arrangement); insurance |
| ADGM | Financial Services Regulatory Authority (FSRA) | Banking, investment management, insurance, payment services |
| KSA | Capital Market Authority (CMA) + Saudi Arabian Monetary Authority (SAMA) | Securities activities: CMA; banking: SAMA; insurance: SAMA (IA/CCHI); fintech: SAMA/CMA sandbox |
| Lebanon | Banque du Liban (BDL) | Banking license; exchange license; insurance oversight (MOE) |
| Egypt | Financial Regulatory Authority (FRA) + Central Bank of Egypt (CBE) | Securities: FRA; banking: CBE |

**Key fintech note**: UAE, KSA, and Bahrain have active regulatory sandbox programs. A sandbox authorization is NOT a full license and restricts client numbers and activity scope.

#### Healthcare

| Jurisdiction | Regulator | License types |
|---|---|---|
| Abu Dhabi | Department of Health Abu Dhabi (DOH) | Healthcare facility license; practitioner registration (HAAD/DOH) |
| Dubai | Dubai Health Authority (DHA) | Healthcare facility license; practitioner license (DHA) |
| KSA | Saudi Commission for Health Specialties (SCFHS) + Ministry of Health (MOH) | Practitioner license (SCFHS); facility license (MOH) |
| UAE (Medical Device / Pharma) | Ministry of Health and Prevention (MOHAP) | Product registration; import permit |

#### Food and agriculture

| Jurisdiction | Regulator |
|---|---|
| UAE Federal | Ministry of Climate Change and Environment (MOCCAE) |
| Abu Dhabi | Abu Dhabi Agriculture and Food Safety Authority (ADAFSA) |
| KSA | Saudi Food and Drug Authority (SFDA) |

#### Education

| Jurisdiction | Regulator |
|---|---|
| UAE | Ministry of Education (MOE) for K-12; Commission for Academic Accreditation (CAA) for higher education; Knowledge and Human Development Authority (KHDA) for private schools in Dubai |
| KSA | Saudi Commission for Academic Accreditation (SCAI) + Ministry of Education |

### 3. Professional licenses

Individual practitioners in regulated professions need personal professional licenses separate from the entity's commercial license:

| Profession | UAE | KSA | Lebanon |
|---|---|---|---|
| Lawyers | UAE Ministry of Justice; per-emirate bar (Dubai: DBA, Abu Dhabi: ABA); DIFC: DIFC Authority | Saudi Bar Association (SBA); only Saudi nationals may practice as advocates in Saudi courts | Beirut Bar Association / Tripoli Bar (membership mandatory) |
| Accountants / Auditors | UAE Ministry of Economy (CPA registration for audit); DIFC: DFSA registered auditor | Saudi Organization for Chartered and Professional Accountants (SOCPA) | Lebanese Association of Certified Public Accountants (LACPA) |
| Doctors | DHA (Dubai); DOH (Abu Dhabi); MOH (other emirates) | Saudi Commission for Health Specialties (SCFHS) | Lebanese Order of Physicians |
| Engineers | UAE Society of Engineers; per-emirate licensing authorities | Saudi Council of Engineers | Lebanese Order of Engineers and Architects |
| Real estate brokers | Real Estate Regulatory Agency (RERA/DLD) in Dubai | Ministry of Housing / Real Estate General Authority (REGA) | No formal national licensing body |

### 4. Ancillary compliance requirements

Beyond the core commercial and sector licenses, businesses must obtain:

| Requirement | UAE | KSA |
|---|---|---|
| Labor / immigration | Ministry of Human Resources and Emiratisation (MOHRE) — work permit and Emiratisation quota; GDRFA — residence visas | Ministry of Human Resources and Social Development — Iqama (work permit); Saudization (Nitaqat) quota compliance |
| Data protection | UAE Federal Decree-Law No. 45 of 2021 on Personal Data Protection — register if controller of large-scale processing; DIFC/ADGM: separate DP frameworks | Saudi Personal Data Protection Law (PDPL, Royal Decree M/19 of 2021) — data controller registration with NDMO |
| Anti-money laundering | CBUAE AML registration for DNFBPs (Designated Non-Financial Businesses and Professions); DIFC: DFSA AML framework | SAMA AML guidelines; FATF compliance requirements |
| Environmental | Per-emirate environment authority permits for industrial/manufacturing activities | Saudi Green Initiative-related disclosures; Ministry of Environment permits |
| Municipal / building | Dubai Municipality / DEWA / ADWEA approvals for premises | Municipal permits for physical locations |

## Output schema

```json
{
  "activity": "string",
  "jurisdiction": "string",
  "licenses": [
    {
      "license": "name of license",
      "issuer": "name of regulatory authority",
      "validity": "1 year | 3 years | etc.",
      "cost": "amount or range (verify with authority for current fees)",
      "leadTime": "estimated processing time in business days/weeks",
      "prereqs": ["list of prerequisites: e.g., 'commercial license must be obtained first'"],
      "renewalPath": "auto-renewal / annual filing / exam re-certification",
      "foreignOwnershipRule": "if applicable",
      "notes": "jurisdiction-specific traps or nuances"
    }
  ],
  "sequencing": "Recommended order of obtaining licenses (some cannot be obtained before others)",
  "totalEstimatedTimeline": "string",
  "professionalLicensesRequired": ["list if practitioners need individual licenses"],
  "ancillaryCompliance": ["AML registration", "data protection registration", "labor quota compliance", etc.]
}
```

## Common traps

1. **UAE free-zone company ≠ license to operate onshore**: a DMCC or JAFZA entity cannot have a physical office or conduct business onshore without a separate establishment or a service agent. Confirm the geographic scope of the proposed activity.
2. **DIFC/ADGM activity scope limitations**: DFSA and FSRA licenses specify exactly which activities are permitted; operating outside the licensed scope is a regulatory breach.
3. **KSA foreign company licensing**: a foreign company conducting business in KSA must be registered even if it has no physical presence; the definition of "conducting business" has been interpreted broadly by the Ministry of Commerce.
4. **Lebanon financial sector fragmentation**: separate licenses required from BDL for banking/exchange, MOE for insurance; the sector has been under significant stress since 2019 and new license applications face delays.
5. **Relying on an old license for new activities**: in UAE especially, adding a new business activity requires a license amendment — the existing license does not automatically cover it.

## Cross-reference

Always pair with:
- [[research-regulation-lookup]] for the full statutory text of the relevant licensing law
- [[research-regulator-guidance-lookup]] for the regulator's current interpretation of licensing conditions
- [[research-recent-amendments-tracker]] to check whether licensing requirements have recently changed

## Related skills

- [[research-regulation-lookup]]
- [[research-regulator-guidance-lookup]]
- [[research-recent-amendments-tracker]]
- [[research-jurisdiction-comparison]]
- [[review-compliance-gap-analysis]]
