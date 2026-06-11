---
name: ecp-manual
title: Export Compliance Program (ECP) Manual
description: Drafts an audit-ready Export Compliance Program manual covering EAR, ITAR, and OFAC requirements. Use when creating or updating an export compliance policy, international trade compliance program, or preparing enforcement defense documentation for regulatory review.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ecp-manual
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: sanctions
language: en
---

# Export Compliance Program (ECP) Manual

Drafts a tailored ECP Manual establishing policies, procedures, and controls for compliance with U.S. export control laws (EAR, ITAR, OFAC) and applicable foreign regimes.

## Prerequisites

Gather before drafting:

1. **Company profile** — legal name, structure, export-active business units
2. **Product/technology inventory** — catalog and technical specs for classification
3. **Export footprint** — destination countries, customer list, restricted-market exposure
4. **Compliance posture** — prior licenses, CJ rulings, VSD history, audit findings
5. **Org structure** — compliance personnel, reporting lines, ECP ownership (CCO, GC, EMPD)

Search uploaded documents for org charts, product catalogs, customer lists, prior licenses, agency correspondence, and audit findings. Tailor the manual to extracted details rather than producing a generic template.

## Quick Start

1. Collect prerequisites above
2. Draft each section in order (management commitment → risk → classification → licensing → screening → records → training → audit → VSD)
3. Use "must/shall" for required actions, "should" for best practices
4. Mark all regulatory citations with `[VERIFY]` for attorney review
5. Deliver as a living document with version control

## Manual Sections

### 1. Management Commitment Statement

- CEO/executive authorship with zero-tolerance policy language
- Authority grant: compliance personnel can halt non-compliant transactions
- Consequence statement: civil/criminal penalties, denial of export privileges, debarment, personal liability
- Resource commitment: personnel, systems, training, external counsel

### 2. Risk Assessment Framework

| Dimension | Key Factors |
|---|---|
| Item sensitivity | Dual-use (EAR/ECCN), defense article (ITAR/USML), deemed export exposure |
| Destination risk | Country tier, embargo status, proliferation concerns, sanctions programs |
| End-user/end-use | Ownership structure, diversion indicators, end-use information willingness |

**Cadence:** Enterprise-level annually (+ triggered by new products, markets, acquisitions, regulatory changes). Transaction-level per-deal with escalation criteria.

**Red flags triggering enhanced due diligence:**
- Customer reluctant to state end-use
- Product inconsistent with customer's business
- Unusual routing, shipping, or payment instructions
- Freight forwarders in high-risk jurisdictions
- Proximity to sensitive facilities or free trade zones

### 3. Classification Procedures

**EAR path:**
1. Determine jurisdiction (EAR vs. ITAR vs. other)
2. Review CCL → assign ECCN (product group, technical parameters, reasons for control)
3. Evaluate "specially designed" provisions; apply de minimis rules for foreign-made items with U.S. content
4. No CCL match → designate EAR99; document determination

**ITAR path:**
1. Review USML categories for defense article/service status
2. Ambiguity → file Commodity Jurisdiction request to DDTC
3. Document all CJ rulings; re-evaluate when products evolve

Retain classification worksheets, technical analyses, and CJ determinations. Review periodically as products or regulations change.

### 4. Licensing Determinations

| Scenario | Action |
|---|---|
| EAR-controlled | Check Commerce Country Chart (ECCN × destination) |
| License exception available | Verify all conditions; document exception basis |
| EAR99 / unrestricted | No license required; document determination |
| ITAR-controlled | Determine DSP-5, DSP-73, TAA, or MLA; submit via DECCS |
| OFAC nexus | Confirm general license or obtain specific OFAC license |

Also address: temporary exports, re-exports, deemed exports to foreign nationals, encryption items, multi-country transactions. Track all license conditions, validity periods, and reporting obligations.

### 5. Restricted Party Screening

**Required lists (minimum):** OFAC SDN List, BIS Entity List, BIS Denied Persons List, BIS Unverified List, BIS MEU List, State Dept AECA Debarred List, Consolidated Screening List (CSL).

**Protocol:**
- Screen at: onboarding, order entry, pre-shipment, periodic refresh
- Screen all parties: customer, consignee, end-user, freight forwarder, financial institutions
- Use fuzzy-logic matching for name variants and aliases
- Document: date/time, lists searched, results, false-positive rationale
- Confirmed match → prohibit transaction; escalate to counsel immediately

**OFAC 50% rule:** Entities 50%+ owned by an SDN are blocked even if not separately listed.

### 6. Recordkeeping

| Record Category | Retention |
|---|---|
| Export licenses & authorizations | Permanent (or license life + 5 yr) |
| Classification determinations | Product life + 5 yr |
| Screening results | 5 yr from transaction |
| Shipping docs (invoice, B/L, EEI/AES) | 5 yr from export |
| License exception docs | 5 yr from export |
| Technology transfer agreements | 5 yr from expiration |
| Training records | Employment + 5 yr |
| VSD correspondence | Permanent |

Regulatory minimums: EAR 5 yr [15 C.F.R. § 762.6 [VERIFY]]; ITAR 5 yr [22 C.F.R. § 122.5 [VERIFY]]; OFAC 5 yr [31 C.F.R. § 501.601 [VERIFY]].

Ensure efficient retrieval, access controls, backup, and disaster recovery. Involve legal counsel before producing records to government.

### 7. Training Program

| Tier | Audience | Topics |
|---|---|---|
| Awareness | All employees | Overview, violation consequences, reporting, no-retaliation |
| Intermediate | Sales, shipping, customer service | Red flags, screening, escalation, documentation |
| Advanced | Compliance specialists | Classification, licensing, deemed exports, sanctions analysis |
| Technical | Engineers, scientists, IT | Deemed export rules, technology/technical data definitions, authorization requirements |

Deliver via instructor-led, web-based, and scenario exercises. Track: attendee, date, topics, assessment scores. Retain as audit evidence.

### 8. Internal Audit Program

**Scope:** Classification accuracy, license compliance, screening completeness, recordkeeping adequacy, procedural adherence.

**Cadence:** Comprehensive annually; focused audits triggered by new markets/products/regulatory changes; risk-weighted transaction sampling.

**Output:** Severity-rated findings → root cause analysis → corrective action plan (named owners, firm deadlines) → follow-up verification.

**Reporting:** Findings to CCO/GC and business unit leaders; material findings escalated to CEO and board/audit committee.

### 9. Violation Response & Voluntary Self-Disclosure

**Upon discovery:**
1. Preserve evidence; implement litigation hold
2. Interview witnesses; reconstruct transaction history
3. Root cause analysis (procedure gap, system failure, training gap, intentional misconduct)
4. Hold similar transactions pending review
5. Engage export control counsel immediately

**VSD submission routes:**

| Regime | Agency | Mechanism |
|---|---|---|
| EAR | BIS Office of Export Enforcement | Written narrative + documentation |
| ITAR | DDTC | Per 22 C.F.R. Part 127 [VERIFY] |
| OFAC | OFAC | Per OFAC Enforcement Guidelines |

**VSD decision factors:** Severity, willfulness, national security harm, likelihood of independent discovery, mitigating factors, prior history.

**Discipline:** Minor/inadvertent → training. Moderate → written warning/PIP. Serious/intentional → suspension, termination, prosecution referral. Apply consistently across all levels.

## Checks and Pitfalls

- **Living document** — review annually and on regulatory/organizational change; version-control; retire obsolete editions
- **Counsel required** — VSD decisions, license applications, CJ requests, and investigations need export control attorney oversight
- **Deemed exports** — screen foreign national hires for controlled technology access before granting it
- **Encryption** — apply EAR §§ 740.17 and 742.15 [VERIFY]; conduct annual reviews and file required reports
- **EAR99 ≠ unrestricted** — EAR99 items still require licenses for embargoed destinations or prohibited end-uses under Part 744
- **Foreign regimes** — note applicable obligations (EU Dual-Use Regulation, UK Export Control Order) where the organization operates abroad
- **[VERIFY] tags** — all regulatory citations must be confirmed by qualified counsel before finalizing
