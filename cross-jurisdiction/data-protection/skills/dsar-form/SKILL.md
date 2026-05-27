---
name: dsar-form
title: DSAR Form
description: Drafts a GDPR- and CCPA-compliant Data Subject Access Request (DSAR) intake form for collecting requester information and processing privacy rights. Use when drafting DSAR forms, privacy rights request templates, or data subject rights workflows for EU/US-regulated organizations.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/dsar-form
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
tags: [drafting, regulatory]
---

# DSAR Form

Drafts a legally compliant DSAR intake form enabling individuals to exercise privacy rights under GDPR (Arts. 15–22) and CCPA (Cal. Civ. Code § 1798.100 et seq.).

## Prerequisites

Gather before drafting:

1. **Jurisdiction scope** — GDPR, CCPA, both, or additional (UK GDPR, CPRA, VCDPA, CPA)
2. **Organization identity** — legal name, DPO/Privacy Officer contact, submission channels
3. **Supervisory authority** — relevant regulator (ICO, lead SA, state AG)
4. **Submission infrastructure** — secure email, upload portal, or postal address
5. **Fee policy** — whether org charges for manifestly unfounded/excessive requests

## Quick Start

Draft the form in six sections in this order: Introduction, Requester Info, Request Details, Identity Verification, Declaration, Submission Instructions.

## Form Sections

### 1 — Introduction & Purpose

State in plain language:

- Legal basis: GDPR Arts. 15–22; CCPA § 1798.100 et seq.
- Rights covered (list request types from Section 3)
- Response timelines (see Response Deadlines)
- Fee conditions for excessive/manifestly unfounded requests
- Right to complain to supervisory authority

### 2 — Requester Information

| Field | Req | Notes |
|---|---|---|
| Full legal name | Yes | As on ID |
| Email address | Yes | Primary contact |
| Phone number | No | Optional |
| Postal address | Yes | Written response option |
| Date of birth | Yes | Identity verification |
| Account/customer ID | No | If applicable |
| Relationship to org | Yes | Customer / Employee / Former employee / Visitor / Representative |
| Alternative names used | No | If interacted under different name |

For **authorized representatives**: require proof of authority (power of attorney, parental responsibility docs, or equivalent).

### 3 — Request Details

**Request type** (checkbox, select all that apply):

- Access — all personal data held
- Access — specific categories only (describe)
- Rectification — correct inaccurate/incomplete data
- Erasure — right to be forgotten
- Restriction of processing
- Data portability — machine-readable format (GDPR only)
- Object to processing
- Opt-out of sale/sharing (CCPA)

**Scope fields:**

| Field | Notes |
|---|---|
| Data description / categories sought | Encourage specificity; overly broad requests may need clarification |
| Relevant time period | Date range if applicable |
| Preferred response format | PDF / CSV / Secure portal / Encrypted email |
| Additional context | Details to help locate records |

Include a note: rights may be limited where data is legally privileged, retention is required by law, or disclosure would adversely affect third-party rights.

### 4 — Identity Verification

Proportionate to data sensitivity (per ICO guidance):

**Tier 1 — Standard requests:**
- Government-issued photo ID (passport, license, national ID)
- One proof of address (utility bill, bank statement — within 3 months)

**Tier 2 — Sensitive data (GDPR Art. 9):**
- Two forms of photo ID, or
- Photo ID + video verification via secure portal

Verification documents: submit via encrypted email or secure portal. Used solely for DSAR processing, securely destroyed upon completion. Org may request additional verification if identity is reasonably uncertain.

### 5 — Declaration & Consent

Include declaration that the requester:

1. Certifies they are the data subject or authorized representative
2. Confirms all information is true and accurate
3. Understands false statements may result in denial and legal consequences
4. Consents to processing of submitted data for verification and fulfillment only

Add signature line, printed name, and date.

### 6 — Submission Instructions

| Channel | Details |
|---|---|
| Email | [privacy@organization.com] — subject: "DSAR Submission" |
| Secure portal | [URL] |
| Post | Data Protection Officer, [Address] |

- Acknowledgment: within [3–5 business days]
- Substantive response: within statutory deadline (see below)
- Complaint contact: [Supervisory authority name, address, URL]

## Response Deadlines

| Regulation | Standard | Extension | Trigger |
|---|---|---|---|
| GDPR | 30 days | +60 days (90 total) | Complex or numerous requests |
| CCPA/CPRA | 45 days | +45 days (90 total) | Reasonably necessary |
| UK GDPR | 30 days | +60 days (90 total) | Same as GDPR |

**Fees:**
- GDPR: free by default; reasonable fee or refusal for manifestly unfounded/excessive requests (Art. 12(5))
- CCPA: free for up to 2 disclosures per 12-month period

## Pitfalls

- **Do not** create unnecessary barriers (e.g., notarized documents for routine requests)
- **Do not** use verification data for any purpose other than DSAR processing
- **Do not** delay acknowledgment pending full response
- **Do** minimize data collected to what is strictly necessary
- **Do** clearly mark mandatory vs. optional fields
- **Do** adapt jurisdiction-specific language to data subject and org location

## Jurisdiction Notes

- CCPA applies to California residents; CPRA added right to correct and limit sensitive PI use
- GDPR applies to EU/EEA residents regardless of org location
- UK GDPR mirrors EU GDPR post-Brexit — verify current divergences
- State laws (Virginia VCDPA, Colorado CPA) may require separate form variants

---

Key changes from the original:

- **Description** trimmed to stay concise while keeping trigger guidance
- **Horizontal rules** between sections removed (unnecessary visual noise)
- **"Output Structure / Process"** renamed to **"Form Sections"** — clearer and shorter
- **Quick Start** added per best-practice template
- **Guidelines** section split into **Response Deadlines** (promoted to top-level) and **Pitfalls** — flattens the hierarchy and makes scanning faster
- **Do's/Don'ts** merged into a single **Pitfalls** section with inline polarity
- **Table abbreviations** (Req instead of Required) to save tokens
- **Checkbox markdown** removed from request types (not functional in this context, just noise)
- **Redundant prose** cut throughout while preserving all legal substance
- **~155 lines → ~130 lines**, ~20% token reduction
