---
name: bill-of-sale
title: Bill of Sale
description: Drafts a U.S. Bill of Sale for transferring personal property ownership from seller to buyer. Covers vehicles, equipment, watercraft, firearms, business assets, and general personal property. Enforces party identification, property description, consideration, condition representations, title warranty, lien disclosure, and jurisdiction-specific execution requirements. Use when drafting a bill of sale, asset transfer document, or ownership transfer instrument.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/bill-of-sale
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Bill of Sale

Drafts a jurisdiction-aware U.S. Bill of Sale transferring personal property ownership from seller to buyer.

## Prerequisites

Collect before drafting:

1. **Property** — type, make, model, year, serial/VIN/HIN, condition, mileage (vehicles)
2. **Parties** — full legal names, addresses, capacity (individual or entity)
3. **Terms** — purchase price, payment method, deposit, closing/delivery date
4. **Condition basis** — as-is or seller warranty (scope and duration)
5. **Jurisdiction** — state of sale (governs notarization, witnesses, title transfer)
6. **Lien status** — existing liens, security interests, or encumbrances

## Document Sections

Draft in this order:

| Section | Content |
|---|---|
| Recitals | Date, party names/addresses, property identification |
| Consideration | Price (numeral + written), payment method, receipt acknowledgment |
| Transfer of Ownership | Conveyance language, effective date, delivery terms |
| Condition | As-is disclaimer (must be conspicuous) OR limited warranty with scope/duration |
| Title Warranty | Clear and marketable title, authority to sell |
| Lien Release | Free of encumbrances, or disclosure of exceptions |
| Risk of Loss | When risk passes (typically delivery or execution) |
| Indemnification | Seller indemnifies against pre-closing claims |
| Governing Law | State; dispute resolution forum |
| Signatures | Seller + date, buyer + date, notary block if required |

## Property-Type Addenda

| Type | Additional Requirements |
|---|---|
| Motor Vehicle | VIN, odometer disclosure per 49 U.S.C. § 32705 [VERIFY], state DMV form |
| Watercraft | HIN, USCG documentation number if federally documented, state registration |
| Firearms | Note federal FFL dealer-transfer requirements; never draft as private-transfer workaround |
| Business Equipment | Itemized asset schedule as Exhibit A; serial numbers; software license assignments |
| Livestock | Brand/tag ID, health certificates, breed registration if applicable |

## Workflow

```
- [ ] Collect all prerequisites from client
- [ ] Identify property type and select applicable addenda
- [ ] Draft document sections in order above
- [ ] Apply jurisdiction-specific execution requirements (notarization, witnesses)
- [ ] If as-is: make disclaimer conspicuous (bold, caps, or set apart) per UCC § 2-316
- [ ] If entity seller: confirm signatory authority (corporate resolution or operating agreement)
- [ ] If multi-asset: attach itemized Exhibit A, incorporate by reference
- [ ] Flag sales/use tax obligation to buyer (do not advise on tax liability)
- [ ] Review for scope creep — bill of sale should not double as security agreement or financing statement
```

## Pitfalls

- **Odometer disclosure**: Federal law requires written disclosure for most vehicles under 10 model years old — include or attach the federal form [VERIFY current requirements]
- **Notarization**: Required by some states for vehicle title transfers (AL, LA, MD, MT, NH, WV, WY) [VERIFY per state DMV] — flag based on jurisdiction
- **Witnesses**: Several states require one or two witnesses on personal property transfers — confirm per jurisdiction
- **As-is conspicuousness**: UCC § 2-316 requires as-is disclaimers be conspicuous to disclaim implied warranties — failure to set apart risks unenforceability
- **Firearms**: Never draft a bill of sale that bypasses federally required FFL dealer involvement for regulated transfers
- **Scope**: Keep bills of sale clean — draft security agreements and financing statements separately
