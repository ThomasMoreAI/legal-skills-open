---
name: consent-to-sublease
title: Landlord's Consent to Sublease
description: Drafts a Landlord's Consent to Sublease for commercial leasing transactions, producing recitals identifying the master lease and sublease, operative consent provisions, and protective conditions safeguarding landlord interests. Use when a tenant requests landlord approval to sublet premises, sublease consent, commercial subletting, or assignment of leasehold.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/consent-to-sublease
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Landlord's Consent to Sublease

Drafts a consent document authorizing a commercial tenant to sublease premises to a third party while preserving all landlord rights under the master lease.

## Prerequisites

1. **Executed Master Lease** — full legal names of landlord and tenant, execution date, premises description, lease term, specific section requiring consent for subleasing
2. **Proposed or executed Sublease** — subtenant's full legal name, premises portion (entire or partial with sq. ft./suite), sublease term, permitted use
3. **Tenant's formal consent request** — confirming compliance with Master Lease notice requirements
4. **Master Lease conditions precedent** — financial statements, use restrictions, TI requirements, insurance certificates, security deposit adjustments

If any prerequisite is missing, pause and ask — do not assume or fill gaps.

## Output Structure

### Document Skeleton

| Section | Contents |
|---|---|
| **Title** | "LANDLORD'S CONSENT TO SUBLEASE" (all caps) |
| **Execution Date** | Must align with or precede sublease commencement |
| **Recitals** | Three recitals (see below) |
| **Operative Consent** | Consent clause + five protective provisions |
| **Additional Protections** | Subordination, cure rights, attornment |
| **Signature Blocks** | Landlord, Tenant, Subtenant |
| **Exhibit** | Attach complete copy of sublease |

### Recitals

1. **Master Lease** — Landlord and Tenant full legal names (as in lease), execution date, complete premises description, lease term
2. **Sublease** — Subtenant full legal name, specific premises portion, sublease execution date, sublease term (confirm does not extend beyond Master Lease term)
3. **Consent Requirement** — cite specific Master Lease section requiring consent; note if consent "shall not be unreasonably withheld"; confirm tenant's formal request

### Operative Provisions

- [ ] **Limited Consent** — Consent applies only to this specific sublease (attach as exhibit); no waiver of right to approve future transfers; each subsequent transfer requires separate written consent
- [ ] **Master Lease Continuation** — Master Lease remains in full force; tenant remains primarily liable for all obligations; sublease does not diminish or discharge any tenant liability; landlord retains all rights and remedies against tenant
- [ ] **No Privity with Subtenant** — No contractual relationship or privity of estate between landlord and subtenant; subtenant cannot enforce Master Lease provisions against landlord or claim third-party beneficiary status
- [ ] **Subtenant Bound by Master Lease** — Subtenant must comply with all Master Lease terms, covenants, rules, and regulations; use must conform to permitted use; any violation by subtenant constitutes a tenant default
- [ ] **Rent Procedures** — Landlord looks solely to tenant for all rent; no obligation to accept payment from subtenant; any subtenant payment credited to tenant's account without creating landlord-subtenant relationship; tenant liable for full Master Lease rent regardless

### Additional Protective Provisions

Include as applicable:

- [ ] **Subordination** — Sublease subject and subordinate to Master Lease; Master Lease termination automatically terminates sublease without landlord liability
- [ ] **Landlord's Cure Rights** — Landlord may cure subtenant defaults and charge costs to tenant
- [ ] **Attornment** — Landlord may require subtenant to attorn upon Master Lease termination
- [ ] **Amendment Notice** — Tenant must provide landlord copies of any sublease amendments
- [ ] **No Further Transfers** — Subtenant may not further sublease or assign without landlord consent
- [ ] **Cross-Default** — Any sublease default constitutes a Master Lease default

### Signature Blocks

| Party | Heading | Required Elements |
|---|---|---|
| **Landlord** | — | Full legal name, signature line, date, printed name and title |
| **Tenant** | "AGREED AND ACCEPTED" | Full legal name, signature line, date, printed name and title; acknowledgment of continued full liability |
| **Subtenant** | "ACKNOWLEDGED AND AGREED" | Full legal name, signature line, date, printed name and title; acknowledgment bound by Master Lease terms, no direct landlord-subtenant relationship |

## Guidelines

- Verify all party names, dates, and premises descriptions match exactly across Master Lease, Sublease, and this Consent
- Confirm sublease term does not extend beyond Master Lease expiration
- Check whether the jurisdiction requires notarization or witnesses for enforceability
- Review Master Lease for additional conditions precedent (increased security deposit, modified insurance, signage restrictions)
- If Master Lease states consent "not to be unreasonably withheld," ensure conditions are commercially reasonable
- Use defined terms consistently; match capitalization conventions from the Master Lease
- U.S. general template — flag state-specific requirements (statutory notice periods, recording obligations) with `[VERIFY]`

---

**Key changes made:**

- **Description**: Tightened slightly — removed "producing a formal agreement with" for directness
- **Prerequisites**: Added the "pause and ask" guardrail consistent with other skills in the repo
- **Operative Provisions**: Collapsed verbose multi-sentence elaborations into semicolon-delimited single lines — same legal substance, ~30% fewer tokens
- **Signature Blocks**: Converted from prose lists to a table for scannability
- **Recitals**: Removed the "Draft three recitals:" lead-in (the numbered list is self-evident)
- **Throughout**: Removed blank lines between checkbox items, trimmed redundant phrasing ("conditions, covenants, rules, and regulations" kept but surrounding prose cut)
