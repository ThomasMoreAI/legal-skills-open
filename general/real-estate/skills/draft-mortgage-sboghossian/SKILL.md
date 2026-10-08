---
name: draft-mortgage-sboghossian
title: Mortgage / Hypothec / Charge on Real Property
description: Use when drafting a mortgage, hypothec, or charge over real property as security for a loan or obligation. Covers all core elements — parties, property description, secured amount, payment schedule, default events, power of sale, insurance, and land-registry registration — with jurisdiction-specific guidance for UAE (Dubai/Abu Dhabi), KSA, Lebanon, DIFC/ADGM, France, and UK. Triggers on "mortgage", "hypothec", "charge over property", "real estate security", "رهن عقاري", or "nantissement immobilier" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-mortgage
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: real-estate
language: en
---

# Mortgage / Hypothec / Charge on Real Property

## When to use this

Use this skill when a borrower or property owner is granting security over real property to a lender or creditor as collateral for a loan, facility, or other obligation.

Terminology varies by jurisdiction:
- **Mortgage** — common-law term (UK, DIFC, ADGM, US)
- **Hypothec / hypothèque** — civil-law term (LB, FR, EG)
- **رهن عقاري** (Rahn 'Aqari) — Arabic / Gulf usage
- **Charge** — English law equivalent (legal mortgage or charge by way of legal mortgage)

Always pair this skill with [[draft-loan-agreement]] for the underlying credit obligation.

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Mortgagor (borrower / property owner) | Full identification; owner of the property |
| Mortgagee (lender / creditor) | Full identification; beneficiary of the security |
| Property description | Legal description, title deed / registration number, address, plot/parcel number |
| Secured amount | Principal amount + interest + fees + costs covered by the security |
| Interest rate / payment schedule | Cross-reference to the loan agreement |
| Default events | When can the lender enforce? |
| Governing law | Jurisdiction; real property security is typically governed by the lex situs (law of the place where the property is located) |

## Document structure

### 1. Parties and recitals
- Full identification of Mortgagor and Mortgagee
- Recital: the Mortgagor has borrowed / is borrowing X from the Mortgagee; to secure repayment, the Mortgagor grants this mortgage
- Cross-reference: the underlying Loan Agreement / Credit Agreement

### 2. Property description
Precise legal description is critical — the registration authority will not accept ambiguity:
- Title deed number
- Plot / parcel number and zone
- Building name, unit number, floor (for apartments / strata)
- Area in square meters
- Address
- Annex the title deed / land registry extract as an exhibit

### 3. Secured obligations
State precisely what the mortgage secures:
- Principal of the loan: AED/USD/SAR X
- Interest at the agreed rate
- Fees, costs, and expenses (including enforcement costs)
- All other obligations under the Loan Agreement
- Consider whether the mortgage secures future advances (securing a revolving facility requires specific language and may not be registrable in all jurisdictions without an amendment)

### 4. Grant of mortgage / hypothec
The granting clause — must be in the exact form required by local law:
- **UAE / Dubai**: "The Mortgagor hereby grants and creates a first-ranking mortgage (رهن) over the Property in favor of the Mortgagee..."
- **LB**: "Le constituant constitue par la présente une hypothèque en premier rang sur l'immeuble..."
- **UK**: "The Chargor charges [the Property] by way of legal mortgage in favor of [the Chargee]..."

### 5. Payment schedule and interest
Cross-reference the Loan Agreement for the repayment schedule. State:
- Monthly / quarterly / bullet payment dates
- Interest: rate, reset mechanism (if variable), payment date
- Late payment interest on overdue amounts

### 6. Representations and warranties
Mortgagor warrants:
- Good and marketable title to the Property; no prior encumbrances beyond disclosed ones
- No pending litigation, disputes, or claims affecting the Property
- All taxes and charges on the Property are paid up to date
- The Property is not subject to any tenancy that would impair enforcement
- The Mortgagor has authority to create the mortgage

### 7. Covenants (Mortgagor's obligations)
Standard ongoing obligations:
- **Maintain the Property**: keep in good repair; not permit deterioration
- **Insurance**: maintain adequate property insurance with the Mortgagee noted as loss payee; minimum coverage = replacement value or secured amount (whichever higher)
- **Pay taxes and charges**: all municipal rates, property taxes, service charges
- **Not alienate**: not sell, transfer, further encumber, or create any additional mortgage without Mortgagee's prior written consent
- **Notify Mortgagee**: of any compulsory purchase / expropriation proceedings; any material damage; any litigation affecting title

### 8. Events of default
Mortgage enforcement is triggered by:
- Non-payment under the Loan Agreement (after any applicable grace period)
- Breach of Loan Agreement covenants
- Breach of mortgage covenants (e.g., failure to insure, unauthorized transfer)
- Borrower insolvency
- Material damage to the Property beyond the insured value
- Compulsory purchase / expropriation without adequate compensation
- Any Event of Default under the Loan Agreement

### 9. Enforcement and remedies

**Power of sale**: on default, the Mortgagee may sell the Property and apply proceeds to the secured obligations. Note: in many MENA jurisdictions, power of sale requires court order or is subject to specific statutory procedures.

**Possession**: right to take possession of the Property on default (common-law jurisdictions: UK, DIFC; more restricted in civil-law jurisdictions).

**Appointment of receiver**: a court-appointed receiver may manage the Property and collect rents pending enforcement.

**Application of proceeds**: sale proceeds applied in order: (1) enforcement costs; (2) accrued interest; (3) principal; (4) other amounts due; (5) surplus to Mortgagor.

### 10. Registration
Registration with the relevant land authority is not just a formality — in most jurisdictions, the mortgage is not effective against third parties until registered. Failure to register can result in loss of priority.

See Jurisdictional notes below for registration mechanics.

### 11. Further assurances
Mortgagor agrees to execute any additional documents and take any steps required to perfect or maintain the mortgage security.

### 12. Governing law
Real property security is always governed by the lex situs (law of the place where the Property is situated). Even if the Loan Agreement is governed by a different law (e.g., English law for DIFC deals), the mortgage must comply with local land law.

## Jurisdictional notes

| Jurisdiction | Registration authority | Key rules |
|---|---|---|
| **UAE — Dubai** | Dubai Land Department (DLD) | Registration mandatory; DLD notarization and registration fee (typically 0.25% of secured amount); Islamic mortgage (رهن) for Sharia-compliant financing; first-ranking mortgage priority determined by registration date |
| **UAE — Abu Dhabi** | Abu Dhabi Department of Municipal Affairs (ADDED) | Tawtheeq registration; similar mechanics to Dubai |
| **KSA** | Real Estate Registry / Ministry of Justice | رهن عقاري; registration with the Notary Public (كاتب العدل); Islamic rahn structure preferred; interest-based mortgages restructured as ijara (lease-finance) or murabaha secured by property |
| **Lebanon** | Cadastre (Directorate General of Land Registry) | Hypothèque; registered by a notary at the Cadastre; priority determined by registration date; pre-registration (promesse d'hypothèque) also possible |
| **Egypt** | Real Estate Registry | Law 114/1946 on registration; hypothèque must be notarized and registered; Islamic mortgages also available |
| **France** | Service de la publicité foncière | Hypothèque conventionnelle; Code Civil Art. 2385+; notarized deed mandatory; registered at the Land Publicity Office |
| **UK** | HM Land Registry | Legal mortgage by charge (Law of Property Act 1925, s.85); registered at HMLR; non-registration is void against liquidator and purchasers |
| **DIFC** | DIFC Land Register (for DIFC properties) | DIFC Real Property Law No. 10 of 2018; registered charge at DIFC Land Register |

### MENA enforcement considerations
In UAE and KSA, enforcement of mortgage security by private sale without court involvement is generally not available — the Mortgagee must pursue enforcement through the courts (execution proceedings or specialized enforcement courts). This can be a slow process. Lenders often take additional security instruments (personal guarantees, pledges of operating accounts) to provide faster enforcement routes.

In Lebanon, a lender with a notarized and registered hypothec may apply for an ordre (court-supervised auction) through an expedited process, but the overall enforcement timeline can still be lengthy.

## Insurance requirements

The mortgage instrument should specify:
- Policy type: all-risks property insurance (at minimum)
- Minimum sum insured: replacement value of the building
- The Mortgagee is noted as loss payee (insurance proceeds paid to Mortgagee, applied to secured obligations)
- Mortgagor to renew annually and provide evidence to Mortgagee
- If Mortgagor fails to insure, Mortgagee may insure at Mortgagor's cost

## Common mistakes

- Incomplete or inaccurate property description — causes registration rejection
- Failure to register — mortgage ineffective against third parties and in enforcement
- Not cross-referencing all secured obligations — partial security coverage
- Not specifying who is the loss payee on the insurance — proceeds may go to the Mortgagor, not the lender
- Islamic finance transactions: characterizing ijara / murabaha as a conventional mortgage in the instrument — raises Sharia compliance concerns

## Related skills

- [[draft-loan-agreement]]
- [[draft-security-agreement]]
- [[draft-property-sale-agreement]]
- [[draft-guarantee]]
