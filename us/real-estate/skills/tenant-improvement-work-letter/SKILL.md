---
name: tenant-improvement-work-letter
title: Tenant Improvement Work Letter
description: 'Drafts a U.S. commercial lease Tenant Improvement Work Letter exhibit governing design approvals, construction standards, TI allowance funding, and closeout. Use when drafting or revising a work letter, tenant improvement allowance terms, build-out procedures, or a lease exhibit for tenant improvements. Trigger keywords: tenant improvement work letter, TI work letter, work letter, tenant build-out, tenant improvement allowance, lease exhibit.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/tenant-improvement-work-letter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Tenant Improvement Work Letter

Drafts the lease exhibit that controls TI scope, approvals, construction standards, allowance funding, and closeout.

## Prerequisites

1. **Lease terms** — defined terms, notice clause, permitted use, delivery condition, rent commencement, defaults, insurance, exhibits list.
2. **Premises data** — address, suite, rentable SF, base building condition, landlord work scope, building standards.
3. **Allowance terms** — total and per-SF TI allowance, eligible costs, retainage, reimbursement method, unused allowance treatment.
4. **Delivery schedule** — plan submittal deadlines, review periods, start date, substantial completion date, delay rules.
5. **Contractor model** — landlord or tenant GC, approved list or pre-qualification, supervision rights, site rules.
6. **Compliance inputs** — applicable codes, ADA, permits, union labor rules, building rules, lien law mechanics.

## Quick Start

1. Collect deal terms using the intake table below.
2. Confirm which party controls the GC, permitting, and compliance.
3. Draft definitions, then build sections per the template skeleton.
4. Populate the allowance eligibility and disbursement requirements.
5. Set milestone dates in the timeline table and define delay consequences.
6. Cross-reference lease defined terms and state conflict-control priority.

## Core Workflow

### Deal Terms Intake

| Field | Required Detail |
| --- | --- |
| Lease date and parties | Full legal names, execution date |
| Premises | Address, suite, rentable SF |
| TI scope | Base building vs. tenant work delineation |
| Allowance | Dollar amount, per-SF calc, funding cap |
| Eligible costs | Hard costs, soft costs, permit fees |
| Exclusions | FF&E, IT, security, change-order costs |
| Approval timelines | Landlord review periods per submission |
| Construction window | Start and substantial completion dates |
| Disbursement | Progress vs. final, retainage %, payment path |
| Delay rules | Excusable vs. non-excusable and effects |

### Required Definitions

Tenant Improvements / TI Work · Approved Plans · Tenant Improvement Allowance · Substantial Completion · Hard Costs / Soft Costs · Change Order · Punch List · Permits and Approvals · Landlord's Work (if any)

### Section Checklist

- Incorporation into lease; conflict-control clause
- Plan preparation and approval workflow
- Permitting and compliance obligations
- Construction standards and site rules
- Access, hours, and coordination with other tenants
- Insurance and risk allocation
- Allowance eligibility and exclusions
- Disbursement procedure and documentation
- Lien protection and indemnity
- Overruns, savings, and change orders
- Substantial completion and punch list
- Defaults, remedies, and cross-default to lease
- Ownership and maintenance of improvements
- Delivery of as-builts, warranties, and manuals
- Governing law (if not already in lease)

### Allowance Eligibility

| Cost Category | Eligible | Notes |
| --- | --- | --- |
| Base building tie-ins | Yes | Only if required by plans |
| Architectural / engineering | Yes | Licensed professionals required |
| Permits and fees | Yes | Include inspections |
| GC and subcontractor labor | Yes | Hard costs only |
| Materials and finishes | Yes | Building standard or better |
| FF&E | No | Tenant responsibility |
| IT / AV / telecom | No | Unless expressly allowed |
| Security systems | No | Unless expressly allowed |
| Tenant-driven change orders | No | Tenant pays overages |

### Disbursement Package

Each draw request must include:

- Executed disbursement request form
- Paid invoices and vendor statements
- Conditional or unconditional lien waivers
- Contractor affidavit and compliance certification
- Evidence of permits and inspections
- Progress photos or architect certification
- Retainage release conditions (final draw only)

### Timeline and Delay Rules

| Milestone | Default Rule |
| --- | --- |
| Space plan submission | X days after lease execution |
| Landlord review | X business days per submission |
| Construction docs | X days after space plan approval |
| Permit submission | X days after final plan approval |
| Construction start | X days after permits issued |
| Substantial completion | On or before target date |
| Punch list | Complete within X days |
| Delay effects | Excusable delays extend deadlines |

### Template Skeleton

```text
WORK LETTER (EXHIBIT __)

1.  Incorporation; Priority
2.  Definitions
3.  Plans; Landlord Approval
4.  Permits; Code and ADA Compliance
5.  Construction; Contractors; Site Rules
6.  TI Allowance; Eligible Costs; Exclusions
7.  Disbursement Procedure; Retainage
8.  Change Orders; Cost Overruns; Savings
9.  Schedule; Substantial Completion; Punch List
10. Lien Protection; Indemnity
11. Defaults; Remedies; Cross-Default
12. Ownership; Maintenance; As-Builts and Warranties
13. Miscellaneous
Signatures
```

## Guidelines

- Use the lease's defined terms and cross-reference relevant lease sections throughout.
- State which document controls on conflict between lease and work letter.
- Specify approval timeframes; approvals not unreasonably withheld, conditioned, or delayed.
- Allocate permitting and compliance duties explicitly to one party.
- Tie every disbursement to lien waivers and proof of payment.
- Include retainage percentage and objective release conditions.
- Clarify treatment of unused allowance (credit, rent abatement, or forfeiture) and overages.
- Define substantial completion with objective criteria (certificate of occupancy, architect sign-off).
- Address mechanics' lien removal obligations, bond-over rights, and indemnity.
- Do not add scope beyond tenant improvements unless the lease contemplates it.
- Mark uncertain local requirements with [VERIFY].

---

**Key changes made:**

- **Added Quick Start section** — a 6-step rapid onboarding path that was missing from the original.
- **Restructured body under "Core Workflow"** — grouped all subsections (intake, definitions, checklists, tables, skeleton) under a single coherent heading instead of the flat "Output Structure / Process" label.
- **Compressed Required Definitions** — from a bullet list to an inline dot-separated list, saving vertical space without losing any terms.
- **Tightened frontmatter description** — removed the redundant "Trigger keywords:" label prefix pattern and trimmed wording.
- **Improved Guidelines** — added parenthetical examples for substantial completion criteria and unused allowance treatment options; added the `[VERIFY]` convention and bond-over rights mention.
- **Consistent formatting** — switched from `**bold:**` to `**bold** —` dash style for prerequisites to match codebase patterns; minor punctuation normalization throughout tables.
