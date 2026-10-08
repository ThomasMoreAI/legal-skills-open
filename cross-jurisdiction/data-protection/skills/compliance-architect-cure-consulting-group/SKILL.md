---
name: compliance-architect-cure-consulting-group
title: Compliance Architect
description: 'Designs HIPAA, COPPA, GDPR, CCPA, and PCI compliance: consent, audit trails, data classification. Use when an app handles health, kids'', EU, California, or card data, or needs a BAA/DPA check.'
author: Cure-Consulting-Group
author_url: https://github.com/Cure-Consulting-Group/ProductEngineeringSkills/tree/main/skills/security/compliance-architect
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
---

# Compliance Architect

**Outcome:** a compliance architecture for the named app on Cure's Firebase-first stack (Android, iOS,
web): which regulations apply and why, field-level data classification, consent and age-gate design,
audit-trail design, vendor BAA/DPA status, and the tests that prove the controls work. **Done when** every
regulated field has a classification, every third party that receives regulated data has a BAA/DPA status,
and each control has a test. A question ("does COPPA apply?") gets an answer, not the full package.
Match length to the need; no filler sections or restated summaries.

This is architecture guidance, not legal advice; regulated launches need counsel sign-off because penalty
exposure is per violation and per user.

Principles Cure applies on every engagement: collect only what a named feature needs; consent is granular,
revocable, and recorded server-side; PHI, card data, and children's data are encrypted in transit and at
rest with separated keys; every control has an automated test.

## Pre-Processing (Auto-Context)

Context — run these read-only commands first; skip any that fail or aren't permitted (they only tailor the output):

- Stack manifest: `head -40 package.json 2>/dev/null || head -40 build.gradle.kts 2>/dev/null || head -20 Podfile 2>/dev/null || echo "(none detected)"`
- Rules and config: `ls firestore.rules storage.rules database.rules.json firebase.json 2>/dev/null || echo "(no Firebase rules files)"`

## Automated Compliance Scan

Search the codebase and report posture before designing:

1. **PII fields**: `email|phone|ssn|social_security|date_?of_?birth|dob|address|diagnos|medication` in models and schemas.
2. **Third-party SDKs receiving data**: `firebase/analytics|crashlytics|mixpanel|segment|amplitude|sentry|openai|anthropic|@google/genai` — each is a potential BAA/DPA or COPPA disclosure.
3. **Consent**: `consent|opt_?in|opt_?out|gpc|Sec-GPC` — absence in user-facing code is a finding.
4. **Retention/deletion**: `delete|purge|retain|expire|ttl` in the data layer; Firestore TTL policies in `firestore.indexes.json` or console notes.
5. **Audit logging**: `audit|access_log` in server code; client-side writes to an audit collection are a finding.

## Step 1: Classify the Regulation

| Regulation | Applies when | Architecture consequences |
|---|---|---|
| HIPAA | Covered entity or business associate handling PHI | BAA chain, access controls, audit logs, encryption, breach notice ≤60 days |
| COPPA | Service directed to under-13s, or actual knowledge of under-13 users (US) | See the COPPA rule below |
| GDPR | EU/EEA data subjects | Lawful basis per purpose, DPIA for high-risk processing, 72-hour breach notice to the authority, erasure and portability |
| CCPA/CPRA | California consumers, business over thresholds | Know/delete/correct, opt-out of sale/share, honor GPC, 45-day response; 2026 regulations below |
| PCI DSS v4.0.1 | Card data stored, processed, or transmitted | Keep out of scope with hosted fields/tokenization (Stripe Elements/Checkout → SAQ A) |
| SOC 2 | B2B/enterprise buyers ask for it | Trust Services Criteria evidence; no statutory penalty |

Several can apply at once; the union of requirements applies and the stricter rule wins on each control.
Health data from under-13 users triggers both HIPAA and COPPA; design consent to COPPA.

**COPPA, stated once for the library** (legal-doc-scaffold defers here): COPPA does not ban collecting data
from children under 13; it requires verifiable parental consent before collection (plus, under the 2025
amendments, separate consent before disclosing to third parties), a written data-retention policy, and a
written security program. compliance-architect owns the consent-flow design. The amended rule was
published 2025-04-22, effective 2025-06-23, with compliance required by 2026-04-22. There is no annual
re-consent requirement.

**California 2026 regulations** (CPPA, approved 2025-09-23; in effect from 2026-01-01): risk assessments
for significant-risk processing (existing processing assessed by 2027-12-31; submissions due 2028-04-01);
ADMT notice/opt-out/access for significant decisions from 2027-01-01; annual cybersecurity audits phased
in from 2028-04-01 by revenue. If a Cure product uses a model to make significant decisions about
Californians (lending, housing, employment, education, health care), flag ADMT scope.

### Penalty reference (verified 2026-09-23; re-check before quoting to a client)

| Regime | Current figure | Source |
|---|---|---|
| HIPAA CMP | \$145–\$73,011 per violation (Tier 4 min \$73,011); calendar-year cap \$2,190,294 per identical provision; OCR's 2019 enforcement discretion applies lower caps to Tiers 1–3 | HHS 2026 adjustment, 91 FR (2026-01-28) |
| COPPA (FTC Act §5(m)) | \$53,088 per violation; FTC made no 2026 adjustment (OMB M-26-11 cancelled 2026 inflation adjustments) | FTC 2025 adjustment; Federal Register 2026-07-07 notice |
| CCPA/CPRA | \$2,663 per violation; \$7,988 intentional or involving minors under 16; next CPI adjustment January 2027 | CPPA announcement 2024-12-17 |
| GDPR | Up to €20M or 4% of worldwide annual turnover, whichever is higher | Art. 83(5) |
| PCI DSS | Contractual fines set by card brands/acquirers — not public; confirm with the acquirer | — |

PCI DSS v4.0 was retired 2024-12-31; v4.0.1's future-dated requirements became mandatory 2025-03-31
(e.g. 6.4.3 payment-page script inventory and 11.6.1 change detection — relevant even for SAQ A pages
that embed hosted fields).

## Step 2: Gather Context

Confirm: data types (PII, PHI, card, behavioral, location, children's); user ages and geographies (US
states, EU, California); data flow (collection point → storage → processors, including LLM APIs); third
parties and what each receives; existing auth, encryption, and logging; greenfield vs retrofit.

## Step 3: Data Classification

| Level | Examples | Controls |
|---|---|---|
| Public | app name, published content | none |
| Internal | internal IDs, non-PII events, flag states | role-based access |
| Confidential | email, phone, address, DOB, IP, device IDs, usage history | encrypted at rest (Firestore default), access-logged, masked in logs, erasable, transfer-restricted |
| Restricted | PHI, card data (never store CVV), SSN, children's PII, biometrics, secrets | above + application-level encryption with a separate key (Cloud KMS), MFA + approval for human access, alert on access, regulatory breach notice |

Deliver a field-level table per collection:

| Collection.field | Level | Regulation | Retention |
|---|---|---|---|
| users.email | Confidential | GDPR/CCPA | account lifetime + 30 days |
| users.dateOfBirth | Confidential | COPPA/GDPR | account lifetime + 30 days |
| health_records.* | Restricted | HIPAA | state law* |
| users.paymentMethodToken | Restricted | PCI (token only) | active subscription |
| consent_records.* | Restricted | COPPA/GDPR | per the written retention policy; long enough to prove consent |

\* HIPAA does not set a medical-record retention period (its 6-year rule in 45 CFR 164.316(b)(2) covers
compliance documentation); state law does — commonly 6–10 years for adults, longer for minors. Confirm
per state before use.

## Step 4: Consent and Age Gate

**Consent record** (`consent_records`, written only by a Cloud Function with a server timestamp; clients
never write it directly): `userId`, `consentType` (marketing, analytics, data_processing, parental,
third_party_disclosure), `granted`, `policyVersion`, `method`, `timestamp`, `parentContact` (COPPA),
`ipHash`, `userAgent`. Append-only: withdrawal is a new record with `granted: false`.

Regime-specific rules the flow must meet:

- **GDPR**: separate consent per purpose; no pre-ticked boxes; withdrawal as easy as giving; consent is
  only one lawful basis — use contract or legitimate interest where they fit instead of forcing consent.
- **COPPA**: verifiable parental consent before any collection beyond the narrow exceptions (e.g. the
  parent's contact to request consent); FTC-recognized methods include signed form, payment-card
  transaction, video call, government ID check, knowledge-based questions, and face match to ID; separate
  consent for third-party disclosure unless integral to the service; parent can review, delete, and refuse
  further collection; no behavioral advertising or analytics identifiers for child accounts without
  consent.
- **CCPA/CPRA**: "Do Not Sell or Share" (or an alternative opt-out link), honor the GPC signal as an
  opt-out, opt-in required before selling/sharing data of consumers under 16.
- **HIPAA**: authorization for uses beyond treatment, payment, and operations, naming the PHI, recipient,
  purpose, and expiry; revocable.

**Age gate:** neutral date-of-birth prompt (no default age, no hint that 13 is the cut-off). Under 13:
collect only the parent's contact, send the consent request, and delete the contact if consent does not
arrive within the stated window; on consent, create a child account with analytics and ad identifiers off
(`setAnalyticsCollectionEnabled(false)`, Crashlytics collection off unless covered by consent). 13–15:
no sale/share without opt-in (CCPA). Store the age-gate result server-side; on device use Keystore- or
Keychain-backed storage (not the deprecated EncryptedSharedPreferences).

## Step 5: Audit Trail

**Event schema:** `eventId`, server `timestamp`, `actorId`, `actorRole`, `action` (read, create, update,
delete, export, consent_granted, consent_withdrawn), `resource`, `classification`, `fieldsAccessed`,
`fieldsModified` (hashes, not values), `result` (success/denied/error), `reason` (required for
Restricted access), `ipHash`.

**What to log:** every read and write of Restricted data (including the user viewing their own PHI),
admin access to Confidential data with a reason, system processes touching PHI, exports, and denied
attempts.

**Where to store it** — the system of record must be outside the reach of the people and code that
administer the protected data: write events server-side to Cloud Logging (a dedicated log bucket with
locked retention) routed to BigQuery for queries, or to a Cloud Storage bucket with Bucket Lock, ideally in
a separate project. A Firestore `audit_logs` collection is acceptable only as a convenience copy, with
`allow create, update, delete: if false` so clients cannot forge or erase entries (Admin SDK writes bypass
rules).

**Retention:** HIPAA documentation and the audit-review records it calls for — 6 years (45 CFR
164.316(b)(2)); PCI DSS 4.0.1 Req. 10.5.1 — 12 months, last 3 immediately available; GDPR — as long as
needed to demonstrate compliance, stated in the record of processing; SOC 2 — per the auditor's period
(typically 12 months).

**Lineage for Restricted data:** record origin (source, consentId), copies (BigQuery, backups), shares
(recipient, purpose, BAA/DPA id), and scheduled deletion.

## Step 6: Platform Patterns

Read [reference/details.md](reference/details.md) when writing client-side storage code (Android Keystore
+ Tink, iOS Keychain), Firestore rules for PHI/consent/audit collections, or the role-claim Cloud Function.

## Step 7: BAA, DPA, and Vendors

HIPAA BAA chain (vendor terms change — re-verify at engagement start; Google list checked 2026-09-23 at
cloud.google.com/security/compliance/hipaa):

| Vendor / product | BAA | Notes |
|---|---|---|
| Google Cloud: Firestore, Cloud Storage, Cloud Functions, Cloud Run, Identity Platform, Cloud KMS, BigQuery, Cloud Logging | Available under the Google Cloud BAA | Only products on Google's HIPAA covered-products list |
| Firebase Authentication, Hosting, App Hosting, Realtime Database, Cloud Messaging, Crashlytics, Analytics | Not covered | Keep PHI out; use Identity Platform instead of Firebase Auth for PHI apps. Vertex AI / Gemini coverage — confirm before use |
| Google Analytics / GA4 | Not offered | Never send PHI (including PHI-revealing page paths or event names) |
| Stripe | Not offered | Relies on HIPAA's payment-processing exemption; keep PHI out of descriptors, metadata, invoices |
| Twilio | Available on eligible editions | Confirm before use |
| SendGrid | Not HIPAA-eligible | Use a BAA-covered email provider for PHI |
| Vercel | Available (Pro add-on / Enterprise) | Confirm before use |
| OpenAI, Anthropic, Sentry, Mixpanel | Plan-dependent | Confirm before use; strip PHI before any LLM call without a BAA |

GDPR DPA (Art. 28) must cover: subject matter, duration, purpose, data categories, data subjects,
sub-processor approval and list, transfer mechanism (SCCs, adequacy, or EU-US Data Privacy Framework
certification), assistance with data-subject rights and breaches, deletion/return at termination, audit
rights.

Vendor scorecard (score each 0–10; ≥90 approve, 70–89 approve with conditions, <70 reject): current SOC 2
Type II; encryption at rest; TLS config; RBAC + MFA + audit logging; BAA/DPA signed; breach-notice SLA;
data residency; published IR process; sub-processor list and change notice; deletion API.

## Step 8: Tests and Erasure

Controls ship with tests in CI:

- Rules (Firebase emulator, `@firebase/rules-unit-testing`): a non-owner cannot read `health_records`;
  nobody can update or delete `consent_records` or `audit_logs` from a client.
- Data flow: no Restricted fields in analytics events or logs (pattern scan of emitted events); no PII
  in child-account analytics; LLM calls strip Restricted fields when the provider has no BAA.
- Consent: processing is gated on a consent record; withdrawal stops processing (target ≤24 h); the age
  gate blocks under-13 collection without consent.
- Retention: scheduled deletions run; backups age out per policy.

**Erasure (GDPR Art. 17 / CCPA delete):** verify identity (re-auth), then complete deletion without undue
delay and within one month under GDPR (extendable by two months for complex requests, with notice) and 45
days under CCPA. Do not add a grace period that consumes the deadline; an optional short undo window
must end well inside it. Delete Firestore/Cloud SQL records, Storage files, the Firebase Auth/Identity
Platform account, analytics user data (GA4 user deletion API), and third-party copies (Stripe customer,
email lists); keep a PII-free deletion record; confirm to the user.

## Code/Artifact Generation

Applies only when Step 1 classifies the request as designing or retrofitting a system. Produce the
classification table, consent and audit schemas, Firestore rules, vendor table, and test list for the
regulations in scope. For a question or a review, answer or report findings; don't generate the package.

## Compliance Report

```
COMPLIANCE ARCHITECTURE — [app] — [date]
Regulations in scope: [regime — why it applies]
Classification: Public [n] · Internal [n] · Confidential [n] · Restricted [n]
Gaps: | # | Regime | Control | Finding | Severity | Fix |
Vendors: | Vendor | Data received | BAA/DPA | Action |
Open questions for counsel: [..]
```

Related: the `security-review` skill (OWASP code review), `legal-doc-scaffold` (privacy policy text),
`firebase-architect` (schema and rules), `test-accounts` (compliance-safe test data).
