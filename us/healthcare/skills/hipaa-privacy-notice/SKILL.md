---
name: hipaa-privacy-notice
title: Notice of Privacy Practices (HIPAA)
description: Drafts a HIPAA-compliant Notice of Privacy Practices per 45 CFR § 164.520 for covered entities. Produces patient-accessible documents covering permitted PHI uses/disclosures, individual rights, breach notification, and complaint procedures. Use when drafting HIPAA privacy notices, NPP documents, patient privacy disclosures, or covered entity privacy practice notices.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/hipaa-privacy-notice
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
---

# Notice of Privacy Practices (HIPAA)

Drafts a complete Notice of Privacy Practices satisfying 45 CFR § 164.520, ready for legal review and patient distribution.

## Prerequisites

Collect before drafting:

1. **Covered entity details** — legal name, business address, effective date
2. **Privacy Officer contact** — name, title, phone, email, mailing address
3. **Entity-specific practices** — facility directories, fundraising, marketing (if applicable)
4. **Fee schedule** — charges for PHI copies, if any
5. **State law overlay** — state privacy requirements more stringent than HIPAA

## Quick Start

1. Gather prerequisites above
2. Draft each section in order (see Document Sections below)
3. Write at or below 8th-grade reading level throughout
4. Run through the Checks section before delivering

## Document Sections

### 1. Header & Introduction

Include: entity legal name, primary business address, effective date, purpose statement ("how your medical information may be used and disclosed").

### 2. Legal Duties (§ 164.520(b)(1)(v))

State entity is required by law to:
- Maintain privacy of PHI
- Provide this notice of duties and privacy practices
- Follow the notice currently in effect
- Notify individuals following a breach of unsecured PHI

### 3. Permitted Uses & Disclosures Without Authorization

Draft concrete, patient-readable examples for each:

| Category | Scope | Example |
|----------|-------|---------|
| Treatment | Care coordination, referrals | Sharing records with a specialist |
| Payment | Billing, claims, utilization review | Submitting claims to insurance |
| Healthcare Operations | Quality, training, planning | Internal audits, staff training |
| Required by Law | Court orders, public health | Reporting communicable diseases |
| Public Interest | Abuse/neglect, FDA, workers' comp | Reporting suspected child abuse |

### 4. Conditional/Optional Disclosures

Include only if applicable; state opt-out right for each:

- Facility directory (name, location, general condition, religious affiliation)
- Family/friends involved in care (patient present, opportunity to object)
- Disaster relief (authorized organizations)
- Marketing (authorization required unless face-to-face or nominal-value gifts)
- Fundraising (opt-out required in each communication)
- Sale of PHI (authorization required; § 164.508(a)(4))

### 5. Individual Rights

Draft each right with exercise procedure:

| Right | Basis | Key Details |
|-------|-------|-------------|
| Access & copies | § 164.524 | 30-day response; fees = labor + supplies + postage; electronic if maintained electronically |
| Amendment | § 164.526 | 60-day response; may deny if accurate/complete; append disagreement |
| Accounting of disclosures | § 164.528 | 6-year lookback; excludes TPO, facility directory, national security |
| Request restrictions | § 164.522(a) | Not required to agree EXCEPT must restrict disclosure to health plan if patient pays out-of-pocket in full |
| Confidential communications | § 164.522(b) | Alternative address/means; accommodate reasonable requests |
| Paper copy of notice | § 164.520(c) | On request even if prior electronic agreement |
| File complaint | § 164.530(g) | No retaliation; to Privacy Officer or HHS OCR |

### 6. Breach Notification

- Notify without unreasonable delay, within 60 days of discovery (§ 164.404)
- Include: breach description, PHI types involved, protective steps, mitigation actions, contact info
- 500+ individuals affected: media notice + HHS notification

### 7. Amendment & Revision Clause

Entity reserves right to change notice terms, apply new provisions to all PHI (including pre-existing), and post/distribute revised notice.

### 8. Complaint Process

Include both complaint paths:
- **Entity**: Privacy Officer name, title, phone, email, mailing address
- **HHS OCR**: Office for Civil Rights, 200 Independence Ave SW, Washington DC 20201; 1-877-696-6775; www.hhs.gov/ocr/complaints [VERIFY URL]

### 9. Acknowledgment of Receipt

- Include detachable/separate acknowledgment form
- State treatment will NOT be conditioned on signing
- Document good-faith efforts if patient refuses (§ 164.520(c)(2)(ii))

## Checks

- [ ] Written at or below 8th-grade reading level; minimal legal jargon
- [ ] State law overlay applied — incorporate stricter state requirements (e.g., CA CMIA, TX medical privacy, NY mental health)
- [ ] Substance use records: 42 CFR Part 2 requires separate, more restrictive notice if entity handles SUD treatment [VERIFY Part 2 final rule alignment with HIPAA]
- [ ] Psychotherapy notes: authorization required for most uses/disclosures (§ 164.508(a)(2))
- [ ] Genetic information: GINA underwriting prohibition noted if entity is a health plan
- [ ] Minors: state-specific consent and parental access rules addressed
- [ ] Format: available in paper; electronic only with individual's agreement (§ 164.520(c)(3))
- [ ] Posting: health plans with websites must prominently post; providers with physical sites must post prominently
- [ ] All CFR citations verified against current regulations

---

**Key changes from the original:**

- **Removed `tags`** from frontmatter (not part of the spec — only `name` and `description`)
- **Trimmed description** slightly for clarity while staying under 1024 chars
- **Added Quick Start** section for immediate orientation
- **Renamed "Output Structure" to "Document Sections"** — more direct
- **Renamed "Guidelines" to "Checks"** — converted prose to a preflight checklist
- **Collapsed verbose sections** — Amendment & Revision Clause condensed to one line; Complaint Process simplified from a code block to inline format; removed the redundant code-block template
- **Removed checkbox syntax from Conditional/Optional Disclosures** — those were output instructions, not a tracking checklist; plain bullets are clearer
- **Tightened table cells** throughout (removed redundant words in Examples column)
- **~20% fewer tokens** while preserving all regulatory citations, section references, and VERIFY flags
