---
name: auth-packet-summary
title: Authorization Packet Summary
description: Validates and summarizes the four required authorization forms in a personal injury matter (retainer, HIPAA release, insurance authorization, employment record release). Confirms signatures, dates, scope, and completeness to determine readiness for the investigation phase. Use when reviewing client onboarding packets, verifying authorization forms before discovery, or checking HIPAA and record-release compliance.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/auth-packet-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
---

# Authorization Packet Summary

Validates the four essential client authorization forms and produces a checklist plus formal memorandum confirming the firm's authority to request third-party records.

## Prerequisites

- All client-signed authorization forms uploaded to the matter
- Client full legal name and case/matter number
- Firm style guide (letterhead, fonts, margins) for PDF output

## Required Forms

| Form | Purpose |
|------|---------|
| Retainer Fee Agreement | Establishes attorney-client relationship and fee structure |
| HIPAA Medical Record Release | Authorizes healthcare providers to disclose PHI |
| Insurance Communication Authorization | Permits carrier contact and claims file access |
| Wage & Employment Record Release | Allows access to employment history, wages, personnel files |

## Workflow

### 1. Extract

For each form, extract:

- Client full legal name (as printed)
- Case/matter number
- Execution date
- Authorized record categories and temporal scope
- Named entities/providers
- Witness signatures and notarization (if jurisdiction requires)

### 2. Validate

Assign one status per form:

| Status | Criteria |
|--------|----------|
| **Complete and Valid** | All required elements present — signatures, dates, scope, mandatory fields |
| **Received but Deficient** | Form present; specify missing elements exactly |
| **Not Received** | Form absent from case file |

Per-form checklist:

- [ ] Client signature present and legible
- [ ] Date fully completed
- [ ] Mandatory fields filled (name, DOB, case/matter, scope)
- [ ] Witness/notarization present if required by state law
- [ ] No expiration issues under applicable privacy regulations

### 3. Cross-Reference

Compare across all four forms for consistency in client name spelling, case/matter number, and date ranges. Flag all discrepancies.

### 4. Compile Checklist

Produce a table with columns: Authorization Type, Status, Execution Date, Authorized Entities, Scope Limitations, Notes/Deficiencies.

For deficient or missing forms, specify exact corrective action (e.g., "Missing client signature on page 2").

### 5. Draft Memorandum

Write a formal memo containing:

1. **Status statement** — As of [date], whether all authorizations are complete or what remains outstanding
2. **Per-form scope summary** — Each authorization's scope, noting temporal or entity-specific limitations
3. **Issues** — Name discrepancies, missing signatures, approaching expirations
4. **Conclusion** — Either:
   - "Investigation phase may commence; firm authorized to request records from all identified entities within scope of client consent," OR
   - "Corrective actions required before record requests may proceed" with specifics

Tone: formal, definitive, suitable as permanent case file record.

## Output

1. **Authorization Checklist** — structured table for case management reference
2. **PDF Memorandum** — firm letterhead, serif 11–12pt, 1-inch margins, header with case ID/client/date/subject, footer with page numbers and `ATTORNEY-CLIENT PRIVILEGED AND CONFIDENTIAL` / `ATTORNEY WORK PRODUCT`, signature lines per firm policy

## Pitfalls

- Never mark "Complete and Valid" unless every required element is confirmed present
- If any form is deficient or missing, do **not** authorize commencement of record requests
- Note scope limitations prominently — staff requesting records must know consent boundaries
- Resolve name-spelling discrepancies by reference to the original document; flag for correction
- Jurisdiction-specific witnessing/notarization requirements vary by state; flag any uncertainty
- All output is privileged and confidential; transmit only via secure channels

---

**Key changes made:**

- **Frontmatter**: Removed `tags` (not part of the spec), tightened the `description` to be third-person with clear trigger guidance
- **Structure**: Reorganized into Overview → Prerequisites → Required Forms → Workflow → Output → Pitfalls pattern
- **Conciseness**: Collapsed the verbose Step 2 status table and validation checklist, merged Output Documents into a compact section, trimmed the Guidelines section into a focused Pitfalls list
- **Removed redundancy**: Eliminated the empty checklist table template (Step 4) — the column spec is sufficient; removed the repeated "tone" guidance that was implicit
- **Line count**: Reduced from 115 lines to ~85 lines while preserving all domain-critical content
