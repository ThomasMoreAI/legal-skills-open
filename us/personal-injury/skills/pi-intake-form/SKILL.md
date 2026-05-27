---
name: pi-intake-form
title: Personal Injury Client Intake Form
description: 'Drafts a structured personal injury client intake form for initial consultations covering client identification, incident details, injury/treatment history, insurance, prior legal history, and authorizations. Supports conflict checking, case evaluation, and engagement setup. Use when onboarding a new PI client, creating intake questionnaires, or building pre-filing client records. Trigger keywords: personal injury intake, client onboarding, PI questionnaire, accident intake, injury claim intake.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/pi-intake-form
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
tags: [checklist, drafting, litigation]
---

# Personal Injury Client Intake Form

Drafts a fillable intake form for prospective personal injury clients that supports conflict checking, statute-of-limitations tracking, case evaluation, and engagement setup.

## Prerequisites

1. **Jurisdiction** — state of incident and client residence (determines SOL, comparative fault rules, damage caps, no-fault requirements).
2. **Firm details** — firm name, address, contact info, fee structure (contingency percentage, cost advancement policy).
3. **Documents already provided** — accident reports, medical records, photos, correspondence — to pre-populate fields and generate follow-up questions.

## Output Structure

Generate a fillable intake form with the following sections in order. Calculate and flag the statute-of-limitations deadline prominently at the top based on jurisdiction and incident type.

### 1) Client Identification

| Field | Notes |
|---|---|
| Full legal name | As on government ID |
| Former names / aliases | For conflict checking |
| Date of birth | |
| SSN (last 4 only) | Include privacy notice |
| Residential address | |
| Mailing address (if different) | |
| Marital status / spouse name | Loss-of-consortium relevance |
| Dependents (names, ages) | Wrongful death relevance |

### 2) Contact & Communication

| Field | Notes |
|---|---|
| Primary phone | Mobile / landline |
| Secondary phone | |
| Email (personal / work) | |
| Preferred contact method | Phone / email / text / portal |
| Do NOT contact at | Confidentiality concerns |
| Text/email consent | Security limitation warning |
| Authorized recipients | Others permitted case info |
| Interpreter / accommodation | Language or accessibility needs |

### 3) Incident Details

- **Date of incident** — flag SOL deadline (verify jurisdiction-specific period)
- **Location** — street address, city, county, state
- **Type** — motor vehicle, slip/fall, premises liability, product liability, medical malpractice, dog bite, workplace, other
- **Narrative** — client's own words, chronological
- **Conditions** — weather, road, environmental (if applicable)
- **Police / incident report** — report number, agency
- **Witnesses** — name, phone, relationship, observations
- **Photos / video** — scene, injuries, property damage

### 4) Parties Involved

For each opposing party and additional involved parties:

| Field | Details |
|---|---|
| Full name | |
| Role | At-fault driver, property owner, employer, manufacturer, etc. |
| Contact info / address | |
| Insurance carrier & policy # | If known |
| Attorney (if represented) | Name, firm, contact |
| Employer | If commercial vehicle / on-the-job |
| Relationship to client | Stranger, employer, landlord, etc. |

Ensure every named person/entity is captured for conflict-system intake.

### 5) Injuries & Medical Treatment

- **Injuries sustained** — body parts, diagnosis if known
- **Ambulance transport** — destination facility
- **ER / urgent care** — date, facility
- **Treating physicians** — name, specialty, facility, treatment dates
- **Ongoing treatment** — PT, scheduled surgery, pain management
- **Pre-existing conditions** — same body parts or related (critical for causation)
- **Lost work days** — dates, employer, wage rate
- **Current symptom status** — improving / stable / worsening
- **Medical records authorization** — HIPAA-compliant release attached

### 6) Insurance Information

| Type | Carrier | Policy # | Limits (if known) |
|---|---|---|---|
| Client auto | | | |
| Client health | | | |
| UM/UIM coverage | | | |
| MedPay / PIP | | | |
| At-fault liability | | | |
| Homeowner's / renter's | | | |
| Umbrella | | | |

- **Recorded statement given?** — to whom, when (flag as red flag)
- **Signed anything from opposing insurer?** — flag immediately

Note: no-fault states require adjusted insurance sections [VERIFY jurisdiction].

### 7) Property Damage

- Vehicle year/make/model, current location
- Repair estimate or total loss determination
- Rental car status
- Personal property damaged

### 8) Prior Legal History

- **Prior attorneys on this matter** — name, firm, dates, reason ended
- **Pending / prior litigation** (past 10 years) — case, court, status
- **Prior PI claims** — critical for credibility and IME preparation
- **Criminal history** — may be discoverable
- **Bankruptcy filings** — affects claim ownership
- **Family members with matters at firm** — conflict check

### 9) Financial / Fee Discussion

- Employment status and occupation
- Income range (bracketed: <$25K / $25-50K / $50-100K / $100K+)
- Contingency fee explanation — plain-language description
- Cost advancement acknowledgment
- Lien awareness — Medicare, Medicaid, ERISA, workers' comp, child support

State that a separate written contingency fee agreement will follow if the firm accepts the matter. Do not include a fee agreement in the intake form.

### 10) Authorizations & Disclosures

Include with signature lines:

- [ ] No attorney-client relationship disclaimer — intake does not create representation
- [ ] Medical records authorization (HIPAA-compliant, separate signature)
- [ ] Employment records authorization
- [ ] Insurance records authorization
- [ ] Third-party communication consent
- [ ] Data privacy notice
- [ ] Text/email communication consent (with security warnings)
- [ ] Accuracy acknowledgment

Signature blocks: prospective client, intake attorney, date.

## Guidelines

- Flag SOL deadline at top of completed form; verify jurisdiction-specific periods.
- Use plain language throughout — clients are often injured and stressed.
- Pre-populate from uploaded documents; generate specific follow-up questions for gaps.
- Capture all named persons/entities in conflict-check-compatible format.
- Note state-specific variations: no-fault insurance, pure vs. modified comparative fault, damage caps [VERIFY].
- Flag red flags early: prior recorded statements, signed releases, pre-existing conditions in same body part, approaching SOL.
- Formatting: minimum 11pt body, adequate white space, section headers, fillable fields.
- Use [VERIFY] for all jurisdiction-specific rules before finalizing.

## Cross-references

- @demand-letter-personal-injury
- @medical-records-summary
- @contingency-fee-agreement
- @hipaa-authorization
