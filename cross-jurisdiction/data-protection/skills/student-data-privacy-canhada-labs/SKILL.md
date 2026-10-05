---
name: student-data-privacy-canhada-labs
title: Student Data Privacy
description: Privacy engineering for K-12 and higher-ed student data under FERPA (US), LGPD-educational (BR), and COPPA (US under-13). Covers parental consent state machine, age-gate enforcement, minimum-necessary collection, purpose limitation, directory-information opt-out lifecycle, SIS roster integrity, and PII handling in grade exports. Use when designing signup, SSO, roster sync, export/portability, or any endpoint that serves student records. Combines with consent-lifecycle (lgpd reference) and pii-data-flow (lgpd reference) for cross-regime consent and data mapping.
author: Canhada-Labs
author_url: https://github.com/Canhada-Labs/ceo-orchestration/tree/main/.claude/skills/domains/edtech/skills/student-data-privacy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
---

# Student Data Privacy

## Cardinal Rule

**A student's consent is their parent's consent until the law says
otherwise.** Age-gate decides the regime, parental-consent surface
decides the flow, data-sharing-agreement (DSA) decides the vendor
relationship. All three MUST be resolved before a student record is
written.

## The three regimes you will encounter

| Regime | Scope | Key obligation |
|---|---|---|
| **COPPA** (US, under-13) | All online services that knowingly collect PII from children under 13 | Verifiable Parental Consent (VPC) BEFORE collection; parental access/deletion rights |
| **FERPA** (US, all K-12 + higher-ed student records) | Educational records held by schools + their "school officials" (vendors under DSA) | Directory-info opt-out; parental/eligible-student access; no disclosure without consent (with narrow exceptions) |
| **LGPD-educational** (BR) | Student data in Brazilian educational context | Art. 14 (children/adolescents), legal basis (usually legítimo interesse + parental consent for under-12), RIPD when high-risk |

A US K-12 edtech platform operating in Brazil must honor **all three**.

## Age-gate state machine

```
                      ┌──────────────────────────┐
                      │   User hits signup       │
                      └──────────┬───────────────┘
                                 ▼
                      ┌──────────────────────────┐
          ┌───────────│  Collect birthdate       │
          │           │  (server-validated)      │
          │           └──────────┬───────────────┘
          │                      │
          │                      ▼
          │       ┌────────────────────────────────┐
          │       │  Age = floor((now - dob)/year) │
          │       │  Store dob, NOT just age bool  │
          │       └──────────┬─────────────────────┘
          │                  │
          ▼                  ▼
    ┌──────────┐       ┌──────────────┐      ┌──────────────┐
    │ age < 13 │──────▶│ 13 ≤ age<18 │─────▶│  age ≥ 18    │
    │  COPPA   │       │   FERPA      │      │  Self-consent│
    │   path   │       │ +parental    │      │  path (still │
    └────┬─────┘       │  per-district│      │  FERPA while │
         │             │   policy     │      │   enrolled)  │
         ▼             └──────┬───────┘      └──────────────┘
  ┌─────────────┐             │
  │ VPC required│             ▼
  │ (FTC method)│      ┌──────────────┐
  └─────┬───────┘      │ Parental     │
        │              │ consent if   │
        │              │ district     │
        ▼              │ requires     │
  ┌─────────────┐      └──────────────┘
  │ Account in  │
  │ "pending VPC"│
  │  → block    │
  │  all writes │
  └─────────────┘
```

Critical invariants:

1. **Store the birthdate**, not just `is_under_13`. When regulations
   shift (e.g. GDPR-K age raises), you re-evaluate from dob.
2. **Server-side enforcement.** Client-side age gates are bypassable.
3. **Audit the age-gate decision** in an append-only log with raw
   dob + decision + timestamp + actor_id.

## VPC (Verifiable Parental Consent) methods (FTC-approved)

| Method | Friction | Confidence |
|---|---|---|
| Signed paper form (mail/fax) | High | High |
| Signed form via e-signature service | Medium | High |
| Credit card $0.50 charge + refund | Medium | Medium |
| Video call to verify ID | High | High |
| Knowledge-based auth (tax records, etc.) | Medium | Medium |
| Government ID upload + match | High | High |
| Email + confirming callback | Low | Low (only for non-disclosure consent) |

**Rejected as VPC:** Email link clicked from the child's inbox.
Single checkbox. Age gate self-attestation.

## FERPA directory-information (DI) machinery

Directory information is a FERPA-specific concept: name, address,
phone, email, photo, enrollment dates, degrees. Schools can disclose
DI without consent UNLESS the parent/eligible student has opted out.

### Invariants

- **DI opt-out is per-student per-district per-year.** Reset may apply
  at district's discretion.
- **Scope matters.** Some districts define DI narrowly (name + grade
  level only); others broadly. The vendor honors the district's policy.
- **Opt-out check before every public display.** Never cache
  "this-student-is-publishable" past the current request; policies
  change mid-year.

### Code-level pattern

```python
def can_display_directory(student_id: str, field: str, audience: str) -> bool:
    student = get_student(student_id)
    district_policy = get_district_di_policy(student.district_id)
    if field not in district_policy.included_fields:
        return False  # district doesn't consider this DI
    if not student.directory_opt_in_current_year(field):
        return False  # per-student opt-out in effect
    if audience in ("public_web", "yearbook", "press"):
        return district_policy.public_disclosure_enabled
    return True
```

## Minimum-necessary collection

Before adding a field to any student-facing form or roster sync:

- [ ] What's the declared purpose? (no purpose = no field)
- [ ] What's the retention class? (education lifecycle, indefinite,
      transient, session-only?)
- [ ] Who reads it? (student, guardian, teacher, district admin,
      vendor, analytics?)
- [ ] Who writes it? (student self-report, roster sync, admin edit?)
- [ ] Can we derive it instead? (age from dob; cohort from enrollment)

If any answer is "we're not sure," the field doesn't ship.

## PII in grade exports — the cross-family leakage trap

A student's grade export MUST NOT contain other students' identities.
Scenarios:

- **Class rank:** disclosing "Alice is rank 7 of 30" implicitly
  reveals 29 other positions. Either disclose rank WITHOUT the
  cohort size, or express as quartile.
- **Group-project grades:** "Alice's grade on the group project was
  B, her groupmates were Bob (A) and Carol (C)" is a FERPA disclosure
  of Bob and Carol's grades. Export Alice's grade; reference
  groupmates by pseudonym.
- **Teacher comments:** "Alice improved faster than most in her class"
  is fine; "Alice improved faster than Bob and Carol" is not.

## Privacy checklist for every edtech change

- [ ] **Age-gate server-side?** (EDTECH-004)
- [ ] **Parental consent verifiable?** (EDTECH-003)
- [ ] **Birthdate stored, not just `under_13` bool?**
- [ ] **Directory-info opt-out honored on every display?** (EDTECH-005)
- [ ] **PII never in URLs, referers, or analytics payloads?** (EDTECH-001, EDTECH-006)
- [ ] **Grade exports redact other students' identities?**
- [ ] **Consent revocation propagates to ML training data?** (EDTECH-007)
- [ ] **Roster sync scoped per district?**
- [ ] **DSA on file before onboarding the district?**
- [ ] **New field has declared purpose + retention class?**

## References

- 34 CFR Part 99 (FERPA)
- 16 CFR Part 312 (COPPA Rule)
- LGPD Art. 14 (tratamento de dados de crianças e adolescentes)
- FTC COPPA FAQ (annually updated)
- `.claude/skills/domains/edtech/skills/assessment-integrity/SKILL.md`
- `.claude/skills/core/consent-lifecycle/SKILL.md` (consent state machine reference)
- `.claude/skills/core/pii-data-flow/SKILL.md` (PII inventory format)
