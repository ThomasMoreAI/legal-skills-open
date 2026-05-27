---
name: lien-foreclosure
title: Mechanic's Lien Foreclosure Complaint
description: Drafts a mechanic's lien foreclosure complaint to enforce unpaid construction liens through court-ordered property sale. Covers jurisdictional allegations, lien validity, breach of contract, and unjust enrichment counts. Use when drafting lien foreclosure complaints, mechanic's lien enforcement actions, or construction payment disputes requiring judicial sale.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/lien-foreclosure
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: construction
language: en
tags: [drafting, litigation, pleading]
---

# Mechanic's Lien Foreclosure Complaint

Drafts a complaint to foreclose a mechanic's lien, seeking judicial sale of real property to satisfy unpaid construction debts.

## Prerequisites

Before drafting, confirm availability of:

1. **Parties** — full legal names, entity types, addresses for plaintiff, property owner, junior lienholders
2. **Contract** — original agreement or PO with payment terms
3. **Payment records** — invoiced amounts, partial payments, outstanding balance
4. **Recorded lien** — recording date, instrument number, county, legal description
5. **Timeline** — commencement, completion/cessation, demand dates
6. **Statutory compliance** — preliminary notices (if required), recording within deadline, service on owner
7. **Applicable state lien statute** identified

## Quick Start

1. Extract party, contract, lien, and timeline data from case documents
2. Draft complaint with caption, jurisdictional allegations, factual chronology, and counts
3. Attach recorded lien, contract, and statutory notices as exhibits
4. Verify all statutory deadlines were met before filing

## Information Extraction

Search case documents for:

| Data Point | Source |
|---|---|
| Plaintiff entity name + type | Contract, business filings |
| Property owner / defendants | Title report, contract |
| Junior lienholders | Title report |
| Contract price / payment terms | Contract or PO |
| Work performed / materials supplied | Invoices, delivery receipts |
| Commencement and completion dates | Project records, daily logs |
| Lien recording date + instrument no. | Recorded lien document |
| Legal description of property | Recorded lien or title docs |
| Preliminary notice service dates | Proof of service |
| Demand dates and responses | Correspondence |
| Amount owed (principal + interest) | Payment ledger, contract |

## Complaint Structure

### Caption

- Court: superior/circuit court for the county where property is located
- Plaintiff with full entity type
- Defendants: property owner + all parties with recorded interests affected by foreclosure
- This is an in rem proceeding tied to the property's situs

### Jurisdictional Allegations

- Subject matter jurisdiction under state mechanic's lien statute [VERIFY citation]
- Amount in controversy meets threshold
- Venue proper: property located in this county

### Factual Allegations (Chronological)

1. **Contractual relationship** — parties, project, scope, price, payment terms
2. **Performance** — specific dates of labor/delivery, reasonable value
3. **Breach** — failure to pay despite demand; exact amount owed, partial payments
4. **Statutory compliance**:
   - Preliminary notice served (if required) — date, method
   - Lien recorded within statutory period — date, instrument no., county
   - Lien served on owner — date, method

### Count I — Foreclosure of Mechanic's Lien

- Incorporate preceding allegations
- Allege valid, perfected lien in stated amount
- Request: determination of amount due, adjudication of lien validity and priority, order of foreclosure, judicial sale with proceeds applied to judgment

### Count II — Breach of Contract

- Contract formation and terms
- Plaintiff's full performance
- Defendant's material breach (nonpayment)
- Damages = unpaid balance + consequential damages if permitted

### Count III — Unjust Enrichment (Alternative)

- Defendant received benefit of plaintiff's labor/materials
- Knowledge of benefit; retention without payment is inequitable
- Include only where jurisdiction permits alternative pleading alongside express contract claims

### Prayer for Relief

- Judgment foreclosing mechanic's lien
- Full amount due with pre-judgment interest (statutory or contractual rate)
- Judicial sale; proceeds applied: (1) costs of sale, (2) plaintiff's lien/judgment
- Deficiency judgment if state law permits
- Breach of contract damages
- Attorney's fees and costs if authorized by contract or statute
- Such other relief as the court deems just

### Exhibits

1. Recorded mechanic's lien (certified copy)
2. Contract or purchase order
3. Statutory notices with proof of service
4. Verification/affidavit if required by state law

## Critical Checks

- **Foreclosure deadline**: Most states impose 6-12 months after lien recording to file suit — verify the lien has not expired
- **Strict compliance**: Lien statutes are strictly construed; any procedural defect (late recording, deficient notice) can invalidate the lien entirely
- **Legal descriptions**: Copy exactly from the recorded lien — never paraphrase
- **Monetary precision**: Use exact figures; no rounding or estimates
- **One allegation per paragraph**: Number consecutively
- **Local rules**: Caption format, margins, spacing, page numbering must comply with filing court requirements
- **Uncertain citations**: Mark any unverified statutory citation with [VERIFY]
