---
name: prompt-pack-due-diligence-request-list-sboghossian
title: Due Diligence Request List
description: Use when preparing a comprehensive due diligence request list (DDRL) for an M&A acquisition — covering corporate documents, financials, material contracts, IP, real property, employment, litigation, regulatory compliance, and IT/data. Tailored to the target company's industry and jurisdiction. Relevant for transactions in MENA (UAE, KSA, DIFC, ADGM, LB, EG) and internationally. Trigger when buy-side counsel needs to send an initial or supplemental document request to the seller or its counsel.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-due-diligence-request-list
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Due Diligence Request List

## When to use this

Use this skill when buy-side counsel in an M&A transaction needs to prepare the initial (or supplemental) due diligence request list — the structured document request sent to the seller or its counsel to populate the virtual data room (VDR). The DDRL shapes the entire due diligence process; a well-structured list ensures comprehensive coverage and reduces follow-up rounds.

Typical triggers:
- LOI or term sheet signed; due diligence formally opened
- VDR has been established but is incomplete; supplemental requests needed
- First-round DDRL has been responded to; second-round targeted requests needed
- Sector-specific compliance diligence requires bespoke document categories

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Target company name | Identity and entity type affects what documents to request | Ask |
| Industry / sector | Drives sector-specific categories (financial, healthcare, technology, real estate, etc.) | Ask |
| Target's jurisdiction(s) of operation | Determines applicable regulatory and corporate law documents | Ask |
| Transaction structure (share purchase / asset purchase) | Asset purchase — focus on specific assets; share purchase — full company diligence | Ask |
| Deal timeline | Affects prioritization of initial vs. supplemental requests | Ask |

## Optional inputs

- Known risks already identified (to prioritize certain categories)
- Whether a W&I insurer's requirements need to be met
- Whether competition/antitrust filing will be required (additional regulatory documents needed)
- Target's group structure (if subsidiaries are material, requests need to cover them)

## Document structure

A standard DDRL is organized into numbered sections. Each item is a specific category of documents.

---

### Section 1 — Corporate and Constitutional Documents

1.1 Certificate of incorporation, commercial registration, and all amendments  
1.2 Articles of association / memorandum of association (current and all prior versions)  
1.3 Shareholder register (current and historical); all share certificates issued  
1.4 All shareholder agreements, voting agreements, or similar arrangements  
1.5 List of all directors, officers, and authorized signatories with terms of appointment  
1.6 All board minutes, committee minutes, and shareholder resolutions for the past [3–5] years  
1.7 Corporate structure chart showing all subsidiaries and affiliates  
1.8 Foreign entity registrations (if operating in multiple countries)  
1.9 Powers of attorney outstanding  

---

### Section 2 — Financial Documents

2.1 Audited financial statements for the past [3–5] years  
2.2 Most recent management accounts  
2.3 Details of all bank accounts and facilities; overdraft and loan agreements  
2.4 Details of all indebtedness (financial indebtedness, guarantees, security interests)  
2.5 Accounts payable and receivable aging schedules  
2.6 Capital expenditure history and forecast  
2.7 Off-balance sheet arrangements and contingent liabilities  

---

### Section 3 — Material Contracts

3.1 All contracts with a value exceeding [threshold] or term exceeding [X] years  
3.2 Top 10 customer contracts (by revenue); top 10 supplier contracts (by spend)  
3.3 All contracts containing change-of-control or assignment-restriction clauses  
3.4 All joint venture, partnership, and shareholder agreements  
3.5 All agency, distribution, and franchise agreements  
3.6 All outsourcing agreements for material services  
3.7 Any contracts with government or state-owned entities  
3.8 Any exclusivity arrangements or non-competition obligations  

---

### Section 4 — Intellectual Property

4.1 List of all registered IP (trademarks, patents, designs, domain names) with registration numbers and renewal dates  
4.2 IP assignment agreements from founders, employees, and consultants  
4.3 All IP licensing agreements (in-bound and out-bound)  
4.4 Open-source software inventory and compliance records  
4.5 Details of any IP infringement claims or disputes (threatened or pending)  

---

### Section 5 — Real Property

5.1 Title deeds or equivalent documents for all owned real property  
5.2 All lease agreements (as landlord and as tenant); confirmation of no amendments  
5.3 Planning and building permits; occupancy certificates  
5.4 Any property encumbrances, charges, or easements  
5.5 Any outstanding property disputes or regulatory notices  

---

### Section 6 — Employment and HR

6.1 List of all employees with position, tenure, and compensation (aggregated if confidential at this stage)  
6.2 Template and non-standard employment contracts; consultant / contractor agreements  
6.3 Details of all pending or threatened employment claims or disputes  
6.4 Details of collective bargaining agreements or union recognition  
6.5 NSSF / pension / retirement fund contribution records and compliance  
6.6 End-of-service gratuity calculation and funding status  
6.7 Equity incentive plans; list of option / RSU holders and vesting schedules  
6.8 Details of any key-person departures in the past 12 months  

---

### Section 7 — Litigation and Disputes

7.1 List of all current and pending litigation, arbitration, and administrative proceedings (as claimant and defendant)  
7.2 All claim letters, demand letters, and notices of dispute received in the past [3] years  
7.3 Details of any criminal investigations or regulatory enforcement actions  
7.4 Details of any judgments or arbitral awards outstanding against the target  

---

### Section 8 — Regulatory and Licensing

8.1 All material licenses, permits, and regulatory approvals held  
8.2 Correspondence with regulators in the past [3] years  
8.3 Any regulatory warnings, deficiency notices, or enforcement actions  
8.4 Anti-money laundering (AML) / KYC policies and compliance records  
8.5 Any sanctions screening records or notifications  

---

### Section 9 — Tax

9.1 Tax returns (corporate income tax, VAT, withholding tax) for the past [3–5] years  
9.2 Open tax assessments or disputes with tax authorities  
9.3 Transfer pricing documentation  
9.4 Details of any tax rulings, advance pricing agreements, or concessions  
9.5 Zakat calculations and payment receipts (KSA entities)  

---

### Section 10 — IT and Data Protection

10.1 IT systems inventory; key software licenses  
10.2 Data protection / privacy policy; records of processing activities  
10.3 Details of any data breaches (reported and unreported in the past [3] years)  
10.4 Cybersecurity audit reports  
10.5 Details of all SaaS agreements and cloud service contracts  
10.6 Disaster recovery and business continuity plans  

---

## Jurisdictional notes

### MENA-specific items to add

| Jurisdiction | Additional document categories |
|---|---|
| **UAE** | Emirates ID and residency visa status of all sponsored employees; Tasheel records; UAE Ultimate Beneficial Owner (UBO) register extract; Economic Substance Regulation (ESR) compliance records |
| **KSA** | Saudi Commercial Register; GOSI (social insurance) contribution records; Saudization (Nitaqat) compliance certificate; Hawkamah or CMA filings if listed or licensed |
| **Lebanon** | CNSS (NSSF) compliance records; Central Bank of Lebanon approvals if financial institution; corporate registry extract (extrait du registre de commerce) |
| **Egypt** | GAFI registration documents; Egyptian Tax Authority compliance certificate; EFSA filings if financial institution; Zakat returns (not applicable but confirm) |
| **DIFC / ADGM** | DIFC/ADGM Registrar of Companies extract; DFSA/FSRA licenses; DEWS (workplace savings) compliance records |

## Drafting standards

- Number all items hierarchically (1.1, 1.2, etc.) to allow seller to respond item by item.
- Include a document submission instructions cover page: VDR access instructions, response deadline, preferred format (native files vs. PDF), and redaction protocol.
- For sensitive items (personal data, key contracts), offer to accept redacted versions initially and request full versions after exclusivity is granted.
- Prioritize items in a "Priority 1" section for the first VDR upload; this accelerates the deal.

## Common mistakes

- **Too broad**: Asking for "all documents" generates an unmanageable VDR and unhelpful responses; be specific.
- **No deadline**: The DDRL must include a deadline for initial population of the VDR; open-ended requests stall deals.
- **Missing change-of-control sweep**: Failing to specifically request contracts with change-of-control triggers is one of the most costly oversights in M&A diligence.
- **Ignoring UBO requirements**: In UAE and GCC, UBO registers are mandatory; failure to confirm beneficial ownership chain is a compliance gap.

## Related skills

- [[prompt-pack-due-diligence-report]]
- [[prompt-pack-disclosure-letter]]
- [[prompt-pack-escrow-agreement]]
- [[prompt-pack-document-production-request]]
