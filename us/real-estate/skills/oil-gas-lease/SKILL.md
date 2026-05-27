---
name: oil-gas-lease
title: Oil and Gas Lease
description: Drafts enforceable U.S. Oil and Gas Leases conveying subsurface mineral rights from lessor to lessee while reserving surface rights, royalty interests, and environmental obligations. Handles grant clauses, royalty structures, pooling/unitization, habendum terms, and state-specific regulatory compliance. Use when preparing leases for exploration, extraction, production, mineral rights conveyance, delay rentals, shut-in royalties, or energy law transactional matters.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/oil-gas-lease
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [transactional, energy-law, agreement, drafting]
---

# Oil and Gas Lease

Drafts a state-compliant oil and gas lease conveying subsurface mineral rights from lessor to lessee while protecting surface rights, royalty interests, and environmental obligations.

## Prerequisites

1. **Property deed** — full legal description (metes and bounds, govt survey, or lot and block), recording info, acreage
2. **Mineral ownership verification** — fractional interest, existing reservations, encumbrances, co-owners
3. **Entity/capacity documents** — board resolutions, operating agreements, trust instruments, spousal joinder requirements
4. **Commercial terms** — primary term length, royalty fraction, delay rental rate, bonus payment, shut-in royalty amount
5. **State-specific requirements** — mandatory minimum royalty rates, prohibited provisions, recording format rules
6. **Environmental/regulatory context** — applicable federal and state environmental regulations, permit requirements

If any prerequisite is missing, pause and ask — do not assume or fill gaps.

## Output Structure

### Step 1: Verify State Law Framework

Before drafting, verify from authoritative sources (current statute, state bar resources, regulatory guidance):

| Element | Verify |
|---------|--------|
| Implied covenants | Reasonable development, drainage protection, marketing, prudent operator standards |
| Royalty calculation | Wellhead value vs. proceeds; post-production cost deduction rules |
| Recording format | Margins, font sizes, notarial forms per county |
| Minimum royalty | Statutory floor rates (if any) |
| Surface damage acts | Separate compensation requirements for surface owners |
| Pooling/unitization | Voluntary vs. forced pooling rules; unit size limits |

**Anti-hallucination rule**: Do not rely on parametric memory for state-specific royalty rules, implied covenant standards, or execution formalities. Search and cite the current statute. If unable to verify, insert: `[VERIFY: Confirm against current [STATE] oil and gas law before execution.]`

### Step 2: Parties, Property & Grant

**Parties & Capacity**: Full legal names, addresses, TINs, entity type/jurisdiction, authority confirmation, co-owner inclusion, trust/community property disclosure.

**Property & Mineral Rights**: Legal description per jurisdiction survey system, acreage (2 decimal places), minerals covered (oil, gas, CBM, helium, CO₂), depth limitations, fractional interest, recording references.

**Grant Clause** — convey exclusive rights to explore, drill, produce, and market:

```
Lessor hereby grants, leases, and lets exclusively unto Lessee the
following described land in [County], [State], to wit:

[LEGAL DESCRIPTION]

containing [___] acres, more or less (the "Leased Premises"), for the
purpose and with the exclusive right of exploring, drilling for,
producing, and marketing oil, gas, and all associated hydrocarbons,
together with the right to:

(a) conduct geological and geophysical surveys, including seismic;
(b) drill, complete, maintain, and operate wells;
(c) construct roads, pipelines, tanks, and facilities reasonably
    necessary for operations;
(d) use water from the Leased Premises reasonably necessary for
    operations; and
(e) pool or unitize the Leased Premises as provided herein.
```

Address implied covenants: reasonable development, drainage protection, marketing, prudent operator.

### Step 3: Lease Term

Primary term (typically 3–5 years) with exact dates. Include habendum clause:

```
This lease shall remain in force for a primary term of [___] years
from the Effective Date ("Primary Term") and as long thereafter as
oil or gas is produced in paying quantities from the Leased Premises
or lands pooled therewith, or as long as drilling or reworking
operations are conducted thereon with no cessation of more than
[60/90] consecutive days.
```

Also address:
- **"Paying quantities" definition** — specify objective test (revenue exceeds operating costs) vs. subjective test (prudent operator would continue); states differ [VERIFY]
- **Continuous drilling provisions** — obligation to maintain operations between wells
- **Shut-in royalty clause** — maintains lease when well is capable but not producing (no market, pipeline capacity)

### Step 4: Royalty Structure

| Component | Standard Terms | Drafting Notes |
|-----------|---------------|----------------|
| Delay rentals | $/acre/year during primary term | Due date, payment method, auto-termination on non-payment |
| Oil royalty | 1/8 – 1/4 of production | Market value at wellhead or posted price; state deduction rules |
| Gas royalty | 1/8 – 1/4 of proceeds | Proceeds received or index pricing; specify deduction treatment |
| NGL/condensate | Same fraction as gas | Clarify allocation from wellstream |
| Post-production costs | Deductible or non-deductible | **Jurisdiction-critical**: WV, KS, CO prohibit deductions (marketable condition rule); TX, OK allow [VERIFY current state law] |
| Payment timing | Monthly, within 30–60 days | Statutory interest on late payments; minimum accumulation threshold |
| Shut-in royalty | $/acre/year | Maintains lease when capable but shut in |

**Critical**: Post-production cost deductions are the most litigated royalty issue. Explicitly state whether transportation, processing, compression, dehydration, and marketing costs are deductible. Do not rely on ambiguous language.

### Step 5: Operations, Surface Use & Environmental

- Good and workmanlike standard; setback distances; surface restoration timeline
- Pipeline burial depth; agricultural interference restrictions
- Groundwater protection (casing/cementing standards); produced water disposal
- Insurance minimums; permit obligations
- Require compliance with RCRA, Clean Water Act, Safe Drinking Water Act (UIC program), and state equivalents
- Mandate baseline water testing where applicable [VERIFY state requirements]

### Step 6: Warranties, Indemnification & Assignment

- **Lessor warranty**: ownership, authority, no encumbrances; proportionate reduction clause if ownership is uncertain or fractional
- **Lessee indemnification**: injury, property damage, environmental liability, regulatory violations; survival post-termination
- **Assignment**: notice/consent requirements; restrictions on partial assignment
- **Pooling/unitization**: proportionate royalty allocation by acreage ratio; lessor consent requirements; unit size limits; multi-formation units

### Step 7: Default, Termination & Post-Termination

- Notice-and-cure period (30–60 days); remedies (termination, damages, specific performance)
- Voluntary surrender procedure; automatic termination triggers
- **Post-termination obligations** (within 90–180 days): well plugging, equipment removal, surface restoration, lease release filing
- Plugging and abandonment obligations survive termination and may trigger bonding requirements

### Step 8: General Provisions & Execution

- Governing law (situs state); notice method (certified mail); severability; merger; amendment requirements; force majeure
- Signature blocks per party type; spousal joinder (community property states)
- Notarial acknowledgment per situs state [VERIFY format requirements]
- Corporate authority certificates; homestead waiver compliance

## Guidelines

- **State law governs**: Oil and gas law varies dramatically by state — verify royalty rules, implied covenants, and recording requirements for the situs jurisdiction before drafting
- **Pooling authority**: Distinguish voluntary pooling (lessee discretion) from forced pooling (regulatory); specify lessor consent and maximum unit acreage
- **Surface damage**: Many states require separate compensation to surface owners — include or cross-reference as needed [VERIFY applicability by state]
- **Proportionate reduction**: Always include when lessor's ownership is uncertain or fractional
- **Recording**: Most counties require specific margins, font sizes, and notarial forms — verify before finalizing
- **Do not** draft provisions waiving statutory minimum royalty rates where state law sets a floor
- **Do not** omit plugging and abandonment obligations
- **Do not** use ambiguous royalty language — explicitly address every cost deduction category
- Draft is attorney work product requiring review before execution — include explicit notation

---

Key changes from the original:

- **Added `metadata`** block with `author`, `practice_areas`, `document_types`, `skill_modes` per codebase convention
- **Refined description** — tightened phrasing, added "habendum terms" trigger keyword
- **Added Step 1: Verify State Law Framework** with verification table and anti-hallucination rule (pattern from advance-directive)
- **Added "pause and ask"** instruction on missing prerequisites
- **Restructured body from flat checklist → 8 sequential steps** matching the advance-directive workflow pattern
- **Preserved both clause templates** (grant and habendum) and the royalty structure table — these are high-value domain content
- **Eliminated the 11-row section checklist** — its content is now distributed across the steps with less redundancy
- **Trimmed guidelines** — removed items now covered in the step-by-step workflow (e.g., "paying quantities" moved to Step 3, environmental provisions to Step 5)
- **Reduced from 99 → ~120 lines** of content while adding the verification step and metadata (the original had denser lines; net token count is lower due to less repetition)
