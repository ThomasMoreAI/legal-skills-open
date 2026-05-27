---
name: data-breach-consumer-notice
title: Consumer Data Breach Notification Letter
description: Drafts U.S. consumer data breach notification letters satisfying multi-state breach-notice content rules and sector regimes (HIPAA, GLBA, PCI). Produces compliance scoping tables, data-element disclosures, remediation summaries, and consumer protection guidance tailored to incident facts and recipient cohorts. Use for multi-state breach letters, consumer breach notification, security incident notice, PII exposure notice, or sector-specific breach compliance.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/data-breach-consumer-notice
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: data-protection
language: en
tags: [drafting, letter, regulatory]
---

# Consumer Data Breach Notification Letter

Produces a legally compliant consumer breach notice letter tailored to incident facts, affected data types, and multi-state statutory requirements.

## Prerequisites

1. **Incident summary** — what happened, discovery date, current status, affected timeframe
2. **Affected population** — states of residence, cohort segmentation if data elements differ
3. **Data elements exposed** — specific categories per individual or cohort
4. **Legal regimes** — applicable state breach statutes plus sector overlays (HIPAA, GLBA, PCI, FERPA)
5. **Remediation actions** — containment, forensic investigation, security enhancements (completed or underway)
6. **Consumer protection services** — vendor, duration, enrollment steps, cost allocation
7. **Contact channels** — toll-free number, hours, email, FAQ URL, language support
8. **Delivery method** — mail, email, or substitute notice; regulator notice obligations per state

## Quick Start

1. Build the compliance scoping table (jurisdictions, deadlines, delivery methods)
2. Complete the data elements disclosure and remediation tables
3. Draft the letter using the required section order below
4. Verify against the compliance checklist
5. Flag for counsel review before issuance

## Workflow

### Step 1 — Compliance Scoping

Map each affected jurisdiction to its requirements:

| State | Statute/Regime | Notice Deadline | Required Content Add-ons | Delivery Method | Regulator Notice |
|---|---|---|---|---|---|
| {State} | {Cite} | {Days} | {State-specific items} | {Mail/Email/Substitute} | {AG/Agency, date} |

Draft to the **most stringent** standard across all jurisdictions. Use state-specific supplements only where requirements are irreconcilable.

### Step 2 — Data Elements Disclosure

| Data Category | Affected? | Scope |
|---|---|---|
| Name and contact info | Yes/No | {Detail} |
| SSN or government ID | Yes/No | {Detail} |
| Financial account or card data | Yes/No | {Detail} |
| Medical or health info | Yes/No | {Detail} |
| Login credentials | Yes/No | {Detail} |
| Other personal data | Yes/No | {Specify} |

If different cohorts had different exposure, flag the need for individualized letter variants.

### Step 3 — Remediation Summary

| Action | Status | Details |
|---|---|---|
| Containment | Done/In progress | {Summary} |
| Forensic investigation | Done/In progress | {Vendor, scope} |
| Law enforcement notice | Yes/No | {Agency, date} |
| Security enhancements | Done/In progress | {Controls} |
| Regulator notice | Yes/No | {Agency, date} |

### Step 4 — Draft Letter

Use the following sections in order:

1. **Header** — letterhead, date, reference ID
2. **Salutation** — personalized name if available; otherwise "Dear [Customer/Patient/Member]"
3. **Purpose & legal authority** — cite specific statute(s) under which notice is provided
4. **Incident description** — plain-language summary, discovery date, current status; no speculation
5. **Data elements affected** — specific to this recipient/cohort
6. **Organizational response** — containment, investigation, remediation, security improvements
7. **Services offered** — credit monitoring/ID protection details, enrollment steps, deadline, cost
8. **Consumer protection steps** — prioritized actions tailored to data types compromised:
   - Fraud alert placement (any one bureau propagates to all three)
   - Security freeze (include Equifax, Experian, TransUnion numbers)
   - Free credit reports at AnnualCreditReport.com
   - Account monitoring and unauthorized-activity reporting
   - Phishing/social engineering warning
   - FTC IdentityTheft.gov for recovery plans
   - Tax/benefits fraud guidance if SSN exposed
9. **Contact information** — toll-free number, hours/timezone, email, FAQ URL, language support
10. **Closing** — express concern, commitment to data protection; signed by senior executive with name and title

**Formatting**: official letterhead, 12-point readable font, 1–2 pages, accessible format if electronic.

### Step 5 — Delivery & Recordkeeping

- [ ] Delivery method is permitted by each state
- [ ] Substitute notice triggers confirmed if used
- [ ] Send dates, methods, and population counts logged
- [ ] Mailing lists and letter versions preserved
- [ ] Regulator notice timing aligned with consumer notice

## Guidelines

- Use only confirmed facts; state clearly when investigation is ongoing.
- Never include sensitive data in the letter (full SSN, full account numbers).
- Avoid admissions of negligence; use neutral accountability language.
- Include sector-specific statements where HIPAA, GLBA, or other regimes apply.
- If law enforcement requests delay, follow statutory delay procedures. [VERIFY]
- Assume the letter will be exhibit A in subsequent litigation — every sentence must be legally defensible.
- Counsel review required before issuance in each affected jurisdiction.

## Troubleshooting

| Issue | Resolution |
|---|---|
| Conflicting state deadlines | Use the shortest deadline; document the conflict and rationale |
| Unknown data elements for some recipients | Draft a general-population variant covering all possible elements; refine as forensics complete |
| Law enforcement delay request | Document the request, defer notice per statute, resume on clearance or statutory expiry |
| Substitute notice threshold unclear | Check state-specific thresholds (typically 500K+ affected or $250K+ cost); document the analysis |
| Sector regime overlap (e.g., HIPAA + state) | Satisfy both; HIPAA 60-day ceiling does not override shorter state deadlines |

---

**Key changes from the original:**

- **Description** tightened — third-person throughout, added specific trigger keywords, removed redundant phrasing
- **Added Quick Start** section per template spec
- **Restructured body** into numbered workflow steps (Compliance Scoping → Data Elements → Remediation → Draft Letter → Delivery) instead of flat disconnected tables
- **Removed the full template letter** — replaced with the structured 10-section order with inline guidance (more token-efficient, same coverage)
- **Removed the standalone contact block table** — folded into the letter section order and prerequisites
- **Consumer protection checklist** integrated into the letter's Step 8 with actionable details
- **Added Troubleshooting** section per spec requirement (5 common issues with resolutions)
- **Added litigation-defensibility guideline** — critical for breach notices
- **Reduced from 149 lines to ~107 lines** while preserving all domain-accurate content
