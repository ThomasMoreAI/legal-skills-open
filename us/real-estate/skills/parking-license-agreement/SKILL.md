---
name: parking-license-agreement
title: Parking License Agreement
description: Drafts a revocable Parking License Agreement for commercial office tenancies that avoids creating a lease, easement, or bailment. Trigger when user needs parking licenses, parking privileges, parking access agreements, or ancillary parking documents tied to commercial leases.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/parking-license-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Parking License Agreement

Draft a revocable parking license for commercial office tenancies that protects the licensor while expressly negating any lease, easement, or bailment.

## Prerequisites

Gather before drafting:

1. **Underlying office lease** — executed or final form; term dates, notice clauses, renewal provisions
2. **Facility details** — address, type (garage/surface), space count and type (reserved vs. unreserved), existing rules
3. **Party information** — full legal names, entity types, states of formation, addresses for licensor and licensee
4. **Commercial terms** — monthly fee per space, payment method, escalation mechanism, insurance minimums

## Document Sections

Draft these sections in order:

### 1. Header & Parties

- Title: "PARKING LICENSE AGREEMENT" — centered, caps
- Effective date tied to lease commencement or specified date
- Licensor and licensee: full legal name, entity type, state, address
- Recitals: licensor operates facility; licensee holds office lease; desires parking privileges

### 2. Grant of License & Legal Characterization

- Number of spaces, reserved vs. unreserved, specific facility location
- **Three required disclaimers:**
  1. Not a lease, easement, or property interest — revocable license only
  2. Not a bailment — no custody/control of vehicles or contents
  3. No liability for theft, damage, vandalism, or loss except licensor's gross negligence or willful misconduct

### 3. Term & Lease Linkage

- Co-terminous with underlying lease — starts and ends together
- Auto-terminates on early lease termination (default, casualty, condemnation, mutual agreement) — no separate notice
- Cannot extend beyond lease term; renewal requires mutual agreement
- Vehicles must be removed immediately upon termination

### 4. Fees & Payment

| Term | Detail |
|------|--------|
| Rate | $ per space/month; total monthly obligation |
| Due date | 1st of each month (typical) |
| Method | Check / wire / ACH |
| Late fee | Flat amount or % of monthly fee |
| Interest | Specified rate (within usury limits) |
| Escalation | CPI, fixed %, or licensor-set with 30–60 day notice |
| Taxes | Sales/use tax responsibility |

### 5. Permitted Use & Restrictions

- **Allowed**: Standard passenger vehicles, light trucks, SUVs of licensee's employees, officers, directors, authorized visitors
- **Prohibited**: Commercial/oversized vehicles, RVs, boats, trailers, inoperable vehicles; vehicle repair/washing/commercial activity; overnight parking or use outside facility hours; sublicense or transfer of rights
- All vehicles must be registered, insured, operable; licensee responsible for user compliance

### 6. Rules & Regulations

- Comply with facility rules as amended by licensor in sole discretion
- Licensor may: temporarily close facility (reasonable efforts to minimize disruption), reconfigure spaces, modify access, implement new management systems
- Licensee responsible for access cards/permits; liable for replacement cost

### 7. Liability, Indemnification & Insurance

- **Indemnification**: Licensee indemnifies, defends, holds harmless licensor and affiliates from all claims arising from licensee's use, user acts/omissions, or breach
- **Insurance minimums** (bracket amounts for client confirmation):
  - CGL per occurrence and aggregate
  - Auto liability covering all vehicles using spaces
- Licensor named additional insured; licensee's insurance primary and non-contributory
- Certificates due before first use and annually

### 8. Termination & Default

| Trigger | Notice/Cure |
|---------|-------------|
| Non-payment | [X] days written notice |
| Other breach | [X] days written notice |
| Lease terminated | Immediate, no notice |
| Without cause | [X] days prior written notice |

- Post-termination: cease use, remove vehicles, return access devices
- Indemnification survives termination
- **Holdover**: double monthly fee (daily pro-rata); licensor may tow at licensee's expense

### 9. Assignment & Transfer

- Personal to licensee — no assignment, sublicense, or transfer without licensor's prior written consent (sole discretion)
- Unauthorized transfer is void and material breach
- Consented assignment does not release licensee unless licensor expressly agrees in writing

### 10. General Provisions

Entire agreement, amendment by signed writing, severability, governing law (facility state, no conflicts-of-law), binding on successors, notices (delivery/mail/courier/email), no waiver, no partnership/agency, prevailing party attorneys' fees.

### 11. Signature Block

Separate blocks for licensor and licensee (entity name, by/name/title/date lines). Signature page must share at least one substantive provision — never standalone. Add witness/notary only if required by local law.

## Pitfalls & Checks

- **License, not lease** — reinforce throughout; never use "tenant," "landlord," or "demised premises"; use "licensor" and "licensee" consistently
- **Licensor liability cap** at gross negligence / willful misconduct — do not expand without explicit instruction
- **Escalation clauses** must comply with any parking fee provisions in the underlying lease
- **Insurance minimums** should match or exceed office lease requirements
- **Reserved spaces** — describe by number, level, or map reference; attach exhibit if needed
- **Bracketed placeholders** — all dollar amounts and cure periods require client confirmation before finalizing
- **Jurisdiction** — confirm local notarization or witness requirements before including

---

**Key changes made:**
- Tightened the `description` to third-person with clear trigger guidance
- Renamed "Output Structure" to "Document Sections" for clarity
- Collapsed the Header & Parties table into a compact bullet list
- Consolidated Permitted Use prohibitions into a single dense bullet instead of a sub-list
- Condensed Rules & Regulations and General Provisions into compact prose
- Removed the code-fenced signature block template (replaced with a concise description)
- Removed the "Licensee liable for acts/omissions of any permitted assignee" line (already covered by indemnification)
- Renamed "Guidelines" to "Pitfalls & Checks" for actionable framing
- Trimmed redundant phrasing throughout (~30% token reduction)
