---
name: draft-property-sale-agreement-sboghossian
title: Property Sale Agreement
description: Use when drafting a real estate sale and purchase agreement for residential or commercial property. Covers required inputs (parties, property description, price, title, deposits), standard structure (conditions precedent, title warranties, inspection, closing, risk of loss, tax allocation, default), and MENA-specific registration requirements (Dubai DLD RERA Form F, Abu Dhabi DMT, KSA Saudi Land Authority, Lebanese Cadastre). Also covers off-plan/under-construction handover obligations and title issues (liens, easements, zoning). Triggers on "property sale", "real estate purchase", "sale and purchase agreement", "SPA", "conveyance", or "deed" requests involving real estate.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-property-sale-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: real-estate
language: en
---

# Property Sale Agreement

## When to use this

Use this skill when drafting a sale and purchase agreement (SPA / بيع عقار) for real estate — the binding contract under which a seller transfers ownership of real property to a buyer in exchange for payment.

Real property sale agreements are among the most heavily regulated commercial instruments: they are subject to local land law (lex situs), specific registration requirements, and in MENA, restrictions on foreign ownership. Getting these wrong can result in void transactions, unregistered title, or significant financial penalties.

This skill is distinct from:
- **[[draft-residential-lease]]**: for tenancy (rental) rather than sale
- **[[draft-mortgage]]**: for the security instrument over real property

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Seller + Buyer (full identification) | Including whether Buyer is foreign (triggers foreign-ownership rules in KSA, LB) |
| Property description | Legal description, plot/parcel number, title deed number, address, area in sqm |
| Purchase price + currency | Core economic term; include payment mechanics (cash, mortgage-funded, installment) |
| Closing date and place | Triggers registration timeline and risk allocation |
| Title status | Clean title? Mortgaged? Occupied? Disputes? |
| Deposit | Amount; refundable / non-refundable conditions |
| Inspection / due diligence period | Buyer's right to investigate condition, title, permits |

## Standard document structure

### 1. Parties and recitals
Full identification of Seller and Buyer. Recitals: Seller owns the Property and wishes to sell; Buyer wishes to purchase on the terms set out herein.

### 2. Property description
Precise legal description is critical — the registration authority checks this against their records:
- Title deed / certificate of title number
- Plot / parcel number and zone / block
- Building name and unit number (for strata/apartment)
- Area in square meters (as per the title deed)
- Address
- Annex the title deed as Exhibit A; annex a floor plan or survey as Exhibit B

### 3. Purchase price and payment mechanics

**Total purchase price**: [Amount] [Currency]

**Payment schedule**:
- On signing: [amount] — earnest money / initial deposit (held by escrow agent or with Seller)
- On satisfaction of conditions precedent: [amount]
- At closing/completion: balance of purchase price

**Mortgage-funded purchases**: if Buyer is financing, include a financing condition (see Conditions Precedent). Specify whether the mortgage will be used to pay off existing encumbrances on Seller's title.

**Escrow**: in many jurisdictions, it is standard practice to hold deposits in a neutral escrow until closing. State the escrow agent and the conditions for release.

### 4. Conditions precedent

These are conditions that must be satisfied before either party is obligated to complete the transaction:

**Buyer's conditions (for Buyer's benefit)**:
- Satisfactory title search confirming clean title (no undisclosed liens, encumbrances, or disputes)
- Satisfactory inspection (physical condition of the property meets an agreed standard)
- Mortgage approval / financing condition (Buyer has received formal mortgage commitment)
- Zoning and permits verification (property may be used for Buyer's intended purpose)
- No material change in the property's condition between signing and closing

**Seller's conditions (for Seller's benefit)**:
- Receipt of the initial deposit
- Confirmation that no foreign-ownership restriction applies (if Buyer is foreign)

**Condition-failure procedure**: if a condition is not satisfied by the long-stop date, the party whose benefit it was for may terminate; deposit refunded or forfeited per the terms.

### 5. Title warranties (Seller's representations)
Seller represents and warrants to Buyer:
- Seller is the sole legal owner of the Property; title is not subject to any undisclosed mortgage, charge, lien, encumbrance, or adverse claim
- No pending litigation, dispute, or claim affecting title to the Property
- No unregistered interests (tenancies, options, rights of pre-emption) that would affect Buyer's title
- All applicable taxes and utility charges are paid up to date; no outstanding assessments
- The Property does not violate any applicable building code, zoning law, or planning permission
- Seller has the full right and authority to sell the Property

### 6. Inspection rights and repair allocation

**Due diligence period** (typically 15-30 days from signing):
- Buyer may inspect the property and engage surveyors, engineers, or environmental consultants
- Buyer must notify Seller in writing of any material defects discovered
- Seller may elect to: (a) cure the defect before closing; (b) reduce the purchase price by the cost of cure; or (c) decline, in which case Buyer may terminate and recover the deposit

**"As is" clause**: if Seller refuses to warrant condition, state clearly that the property is sold in its current condition; Buyer accepts responsibility for physical condition after the inspection period; no reduction in price after the inspection period for latent defects discovered later.

### 7. Closing actions
At closing (completion), simultaneously:
- Seller executes and delivers the deed of transfer / conveyance document / title deed transfer
- Buyer pays the balance of the purchase price
- Seller delivers vacant possession (if vacant) or the keys / access credentials
- All closing documents are filed with the land registry simultaneously (or within the registration window)

### 8. Risk of loss between signing and closing
Specify who bears the risk if the property is destroyed or materially damaged between signing and closing:
- **Standard (common-law)**: risk passes to Buyer upon signing of the SPA (Buyer should insure immediately)
- **Civil-law default**: risk typically passes on transfer of possession or registration
- **Recommended**: risk remains with Seller until closing; Seller must maintain insurance through closing; if the property is destroyed, Buyer may terminate without penalty or accept the insurance proceeds in lieu of repairs

### 9. Tax allocation
Real estate transactions attract multiple taxes; allocation must be specified:

| Tax | Typical allocation |
|---|---|
| Transfer tax / registration fee | Split 50/50 (standard in many jurisdictions) or Buyer bears |
| VAT (where applicable) | Usually Buyer's cost for commercial property |
| Capital gains tax | Seller's cost (tax on profit from sale) |
| Stamp duty (UK) | Buyer's cost (SDLT in UK; Land Transaction Tax in Wales) |
| Broker's commission / brokerage fee | Specify which party pays; often each pays their own agent |

### 10. Brokerage
State whether a real estate agent was involved; which party engaged the agent; who is responsible for the commission. This is heavily regulated in Dubai (RERA-licensed agents required) and in most MENA markets.

### 11. Default and remedies

**Seller's default** (failing to close):
- Buyer may rescind and recover the deposit plus additional damages
- OR Buyer may seek specific performance (court order compelling Seller to transfer title)
- Specific performance is available in most civil-law and common-law jurisdictions for unique real estate (each property is unique)

**Buyer's default** (failing to close):
- Seller may rescind; the deposit is forfeited as liquidated damages
- OR Seller may seek specific performance requiring Buyer to complete the purchase
- If the deposit is insufficient to cover Seller's loss, Seller may claim additional damages beyond the forfeited deposit (verify whether the SPA limits damages to the deposit)

### 12. Force majeure
Limited application in real estate sales — courts are reluctant to excuse performance due to market conditions. Include: government seizure, expropriation order, natural disaster making the property uninhabitable before closing.

### 13. Governing law and dispute resolution

## Jurisdictional issues

### UAE — Dubai
- **RERA Form F** (MOU): Memorandum of Understanding — standard mandatory form for off-plan and secondary market sales; issued by Dubai Real Estate Regulatory Agency (RERA); must be signed before filing for transfer
- **Dubai Land Department (DLD) registration**: mandatory; transfer fees typically 4% of purchase price (split equally by convention, or as agreed); both parties or their authorized attorneys-in-fact must appear at DLD or a RERA-registered trustee office
- **Off-plan (under construction)**: DLD escrow requirements — developer must maintain an RERA-registered escrow account; buyer's payments go into escrow; buyer has right to cancel and recover funds in specified circumstances under RERA Regulation 9/2009
- **Foreign ownership**: Dubai allows foreign freehold ownership in designated freehold areas; non-designated areas are restricted to GCC nationals and UAE nationals

### UAE — Abu Dhabi
- **ADDED (Department of Municipal Affairs and Transport) registration**
- **ADM (Abu Dhabi Municipality)**: registration with the Integrated Land Management Platform (Manasik)
- Investment zones allow foreign freehold ownership; outside investment zones, foreigners may hold only usufruct or musataha rights (not full ownership)

### KSA
- **Foreign ownership**: Non-Saudi nationals are generally restricted from owning real estate in KSA; exceptions exist for certain investment zones (NEOM, Red Sea Project) under specific Investment Ministry licenses
- **Saudi Land Authority (Kadastral)**: all transfers registered with the local real estate registry at the Notary Public
- **Islamic mortgage (رهن) structure**: financing secured by property must use a Sharia-compliant structure (ijara, murabaha); conventional mortgage interest is not appropriate

### Lebanon
- **Lebanese Cadastre**: all property transfers registered at the Directorate General of Land Registry (cadastre); notarial deed required
- **Foreign ownership restrictions**: Decree 11614/1969 limits total foreign ownership to 3,000 m² in residential property and requires Council of Ministers approval beyond statutory limits; significant practical restrictions
- **Compulsory valuation**: the tax authorities set a minimum assessed value for transfer tax purposes that may differ from the stated purchase price

### France
- **Notarial system**: all real estate sales must be executed before a notaire; the "compromis de vente" (preliminary contract) is binding; the "acte authentique" before the notaire is the final conveyance
- **Pre-emption rights**: municipalities, co-owners, and some tenants have statutory pre-emption rights that must be respected
- **Diagnostics techniques**: mandatory disclosure reports (lead, asbestos, energy performance, etc.) must accompany the sale; failure to deliver them allows the Buyer to rescind

### UK
- **HM Land Registry**: all transfers registered; Land Registry Form TR1 (or TR2 for transfer of part)
- **Stamp Duty Land Tax (SDLT)**: graduated rates; significant for high-value residential and commercial properties
- **Caveat emptor**: in UK conveyancing, "buyer beware" applies — Seller is not obligated to volunteer defects (beyond statutory duties under the Consumer Rights Act for new-build); Buyer's surveyor is critical

## Title issues — flag and investigate

- **Mortgages and charges**: any registered mortgages must be discharged at or before closing; Seller must provide discharge or undertaking
- **Restrictive covenants**: limitations on use running with the land (e.g., residential use only)
- **Easements**: third-party rights over the property (access, utilities, drainage) — must be disclosed
- **Adverse possession claims**: particularly in LB and Egypt where cadastral registration is incomplete in some areas
- **Off-plan / under-construction risks**: developer insolvency; failure to deliver on time; changes to specifications; verify developer's RERA registration and escrow compliance (Dubai)
- **Boundary disputes**: verify the plot plan against the registered title; survey may be needed

## Critical pre-signing steps

- [ ] Title search by registered agent in jurisdiction (confirms registered owner, encumbrances, litigation)
- [ ] Physical inspection or survey (confirms boundaries, condition, compliance)
- [ ] Permits and zoning verification (property can be used as intended)
- [ ] Tax clearance from Seller (no outstanding property taxes, municipality fees, service charges)
- [ ] Foreign-ownership clearance (if applicable)
- [ ] Mortgage pre-approval from Buyer's lender (if mortgage-funded)

## Common mistakes

- Describing property vaguely ("the apartment in Building X") rather than by plot number and title deed — registration rejected
- Failing to specify deposit forfeiture terms clearly — disputes on whether deposit is refundable
- Omitting the condition for Buyer to verify that the mortgage can be discharged at closing — Buyer may become owner of encumbered property
- Not accounting for RERA Form F requirements in Dubai — transaction cannot proceed without it
- Specifying a foreign Buyer without checking foreign ownership clearance in KSA or LB

## Related skills

- [[draft-mortgage]]
- [[draft-residential-lease]]
- [[draft-property-due-diligence]]
- [[review-property-title]]
