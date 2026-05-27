---
name: commercial-lease-summary
title: Commercial Lease Summary
description: 'Produces structured U.S. commercial lease abstracts covering business terms, financial obligations, operating covenants, risk allocation, and deadlines. Use when summarizing a commercial lease, preparing a lease abstract, reviewing premises/term/rent/CAM, or identifying SNDA, assignment, default, and renewal issues. Triggers: commercial lease summary, lease abstract, CAM reconciliation, base rent escalation, SNDA, assignment/sublease, tenant default, guaranty.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/commercial-lease-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Commercial Lease Summary

Summarize a commercial lease into an executive abstract, issue-spotting notes, and a deadline calendar. Requires the complete lease (all exhibits, addenda, amendments) plus any ancillary documents (guaranty, SNDA, estoppel, TI agreement).

## Quick Start

1. Collect the full lease and all referenced documents.
2. Confirm jurisdiction (state) and property location.
3. Produce output in the section order below, citing exact sections (e.g., "§4.2") for every material term.

## Output Sections

### 1. Executive Overview

6–10 bullets: parties, premises, term, base rent, major escalations, key options, unusual risk allocations, critical deadlines.

### 2. Deal Snapshot

Table with fields: Landlord/Tenant, Premises (address + RSF/USF), Term start/end, Rent commencement, Possession/delivery condition, Renewal options, Use clause, Exclusive/non-compete/radius, Security deposit/guaranty.

### 3. Premises & Term

- Premises description, exclusions, common areas, parking.
- Commencement trigger (delivery, substantial completion, other).
- Holdover terms/rate; early access or build-out access.

### 4. Financial Obligations

Table with columns: Item | Amount/Formula | Frequency | Escalation | Notes.

Rows: Base rent, Additional rent (CAM), Taxes, Insurance, Utilities, Percentage rent, Other charges.

### 5. Use, Operations & Compliance

Permitted use/restrictions, signage, hours, co-tenancy, continuous operation, go-dark rights.

### 6. Maintenance, Repairs & Alterations

- Landlord vs. tenant responsibilities: structural, roof, HVAC, systems, interior, exterior, parking, common areas.
- TI approvals and restoration obligations.

### 7. Insurance, Indemnity & Risk

Required coverages/limits, additional insureds, waiver of subrogation, indemnity scope, casualty and condemnation allocation.

### 8. Assignment / Subletting / Change of Control

Consent standard, prohibited transfers, recapture rights, profit-sharing, deemed-assignment triggers.

### 9. Default / Remedies / Termination

Default types, notice/cure periods, remedies, self-help, acceleration, liquidated damages, termination triggers.

### 10. Security Deposit / Guaranty

Amount, form, return conditions, draws/replenishment, guarantor identity and scope.

### 11. SNDA / Financing

Subordination, non-disturbance, attornment requirements, estoppel certificate timing.

### 12. Special Provisions

Options to purchase, ROFR/ROFO, kick-out, co-tenancy, exclusive, radius, sustainability, landlord relocation rights.

### 13. Issue Flags

Check each and mark findings:

- [ ] Unclear commencement or rent-start trigger
- [ ] CAM/tax pass-through calculation missing or ambiguous
- [ ] Maintenance scope conflicts between sections
- [ ] Insurance limits inconsistent
- [ ] Remedies one-sided or commercially atypical
- [ ] Missing SNDA or lender protections
- [ ] Conflicting option deadlines or notice methods
- [ ] Missing exhibits or schedules referenced
- [ ] Standard clauses absent for this deal type/jurisdiction

### 14. Key Dates & Deadlines

Table with columns: Event | Date/Deadline | Notice Requirements | Source Section.

Rows: Rent commencement, Option exercise deadlines, Renewal notice window, Termination notice, Estoppel delivery, Insurance certificates, Audit rights deadlines.

## Pitfalls

- **No legal advice.** Summarize as written; do not infer market terms.
- **Cite everything.** Every material term needs a section reference.
- **Flag gaps.** Mark ambiguities, conflicts, or missing exhibits as `[UNRESOLVED]`. Mark uncertain citations as `[VERIFY]`.
- **Jurisdiction.** Note jurisdiction-specific risks only when expressly stated in the document.
- **Amendments.** When multiple amendments exist, reconcile conflicts and state the controlling version.

---

Key changes from the original:

- **Removed `tags`** — not part of the spec frontmatter
- **Tightened description** — kept third-person with clear triggers, removed "Trigger keywords:" label
- **Added Quick Start** — 3-step entry point per best practices
- **Compressed output sections** — eliminated empty table scaffolding (token-expensive, no informational value) and replaced with concise column/row descriptions
- **Merged "Missing Standard Provisions"** into Issue Flags as a single checklist item
- **Renamed "Guidelines" to "Pitfalls"** — matches best-practice section naming, reformatted as bold-key/explanation pairs for scannability
- **Removed "Prerequisites" as standalone section** — folded into the overview sentence
- **~90 lines down from ~129** — tighter token footprint while preserving all domain content

Want me to retry writing the file?
