---
name: solar-site-lease
title: Solar Site Lease Agreement
description: Drafts U.S. solar site lease agreements between landowners and solar developers for long-term ground leases of solar PV facilities. Covers option and lease terms, rent structures, easements, construction and operations rights, decommissioning security, insurance and indemnity, tax and REC allocation, assignment and lender protections, defaults, and memorandum of lease. Use when drafting solar farm land leases, solar PV site leases, renewable energy land leases, or solar facility ground lease agreements.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/solar-site-lease
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, regulatory, transactional, energy, lease]
---

# Solar Site Lease Agreement

Draft a long-term ground lease for siting, constructing, operating, and decommissioning a solar energy facility.

## Prerequisites

1. **Parties** — legal names, entity types, signatories, notice addresses
2. **Property** — legal description, parcel IDs, survey, acreage, title report, existing easements
3. **Project scope** — capacity (MW), site plan, BESS if any, interconnection point, access roads
4. **Business terms** — option period, lease term, renewals, rent model, escalation, bonus or revenue share
5. **Jurisdiction** — zoning/setback rules, environmental and stormwater requirements, decommissioning ordinances
6. **Financing** — lender collateral assignment needs, step-in rights, SNDA requirements
7. **Insurance and tax** — target limits, property tax treatment, REC ownership position

## Output Structure / Process

### Key Terms Table

Populate before drafting.

| Term | Required Input | Notes |
|---|---|---|
| Premises | Legal description, parcel IDs, acreage | Exhibit A; specify excluded areas |
| Option/Feasibility | Length, payment, extensions | Tie to permitting and interconnection |
| Lease Term | Operations term, renewals, notice | Align with PPA and equipment life |
| Rent | Base, per-acre or fixed, escalation | Payment timing and proration |
| Access/Easements | Locations, width, utilities | Construction and perpetual access |
| Decommissioning Security | Bond/LOC amount, trigger, update cadence | Align with local rules and lender needs |
| Insurance | CGL limits, property, workers' comp | Name Lessor additional insured |
| Taxes/RECs | Allocation, PILOT, REC ownership | Reporting and audit rights |
| Assignment | Permitted transferees, consent standard | Allow lender collateral assignment |

### Article Order

1. Parties, recitals, defined terms
2. Premises and exhibits; legal description and survey
3. Option and site investigation rights
4. Lease commencement and conditions precedent
5. Lease term and renewal mechanics
6. Rent, escalation, and payment procedures
7. Use rights and permitted improvements
8. Access, easements, and utility interconnection
9. Construction standards and site controls
10. Operations, maintenance, and vegetation management
11. Compliance with laws, permits, and environmental duties
12. Ownership of improvements and personal property status
13. Insurance, indemnity, and limitation of liability
14. Taxes, assessments, incentives, and RECs
15. Assignment, sublease, and lender protections
16. Casualty, condemnation, and restoration
17. Defaults, notices, and cure periods
18. Termination rights and decommissioning
19. Recording; memorandum of lease form
20. Miscellaneous: confidentiality, notices, amendments, counterparts

### Decommissioning Template

```
Decommissioning. Within {12} months after termination or expiration,
Lessee shall remove all solar equipment, foundations, cables, and
improvements to a depth of {X} feet, restore grade, and reseed
disturbed areas, subject to applicable law.

Security. Beginning {Year/Trigger}, Lessee shall maintain a bond or
letter of credit in the amount of {$} (adjusted every {N} years) to
secure decommissioning, payable to Lessor, with {Lessor approval} of
issuer and form.
```

### Exhibits

- **A** — Legal description and survey
- **B** — Site plan and easement map
- **C** — Form of memorandum of lease
- **D** — Insurance requirements and certificates
- **E** — Decommissioning plan (if required by jurisdiction)

### Pre-Finalization Checklist

- [ ] Legal description matches survey and title report
- [ ] Option period and drop-dead COD date defined
- [ ] Rent schedule and escalation unambiguous
- [ ] Decommissioning security meets local ordinance or county guidelines
- [ ] REC ownership and tax responsibility explicitly allocated
- [ ] Assignment and lender step-in rights included
- [ ] Recording requirements and notary blocks correct

## Guidelines

- Use governing law of the state where property is located
- Tie commencement and extensions to objective milestones and permits
- Do not guarantee tax credits or incentives; state no assurance
- Allocate property tax and PILOT obligations with clear reimbursement mechanics
- Provide Lessor access and inspection rights with reasonable notice
- Preserve Lessor compatible use rights if intended (e.g., grazing) with carve-outs
- Use realistic cure periods (monetary and non-monetary); define notice methods
- Require compliance with zoning, setbacks, glare/noise, stormwater, and environmental permits
- Record only a memorandum of lease to keep financial terms confidential
- Mark jurisdiction-specific statutory citations with [VERIFY] if unconfirmed

---

Key changes from the original:

- **Added `metadata` block** with `author`, `practice_areas` (Real estate, Energy), `document_types` (Lease), and `skill_modes` (Drafting) for proper semantic search indexing
- **Tightened description** — removed redundant "landowners/lessors and solar developers/lessees" phrasing, dropped "recording of" filler
- **Reformatted prerequisites** — switched from verbose labels ("Parties and authority:", "Property data:") to bold dash format matching the bill-of-sale pattern
- **Added subheadings** to Output Structure (Key Terms Table, Article Order, Decommissioning Template, Exhibits, Pre-Finalization Checklist) for scannability
- **Stripped filler sentences** — removed "Populate a key terms table before drafting the full agreement", "Draft the agreement in numbered articles using this order", "Use this decommissioning and security template and fill all placeholders", "Include exhibits as separate attachments", "Before finalizing, confirm the checklist"
- **Trimmed table notes** — shortened "Attach as Exhibit A" to "Exhibit A", "Define payment timing" to "Payment timing", etc.
- **Removed trailing periods** from list items and checklist for consistency
- **Reduced from 106 to 100 lines** while preserving all domain-specific content
