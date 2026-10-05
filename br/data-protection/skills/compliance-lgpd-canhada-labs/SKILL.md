---
name: compliance-lgpd-canhada-labs
title: LGPD Compliance for {{PROJECT_NAME}}
description: LGPD (Lei 13.709/2018) compliance for a Brazilian SaaS platform. Covers data subject rights, legal bases for processing, PII classification, data retention, cookie consent, Terms of Service, Privacy Policy, cross-border data transfer to AI providers, audit trails, breach notification, and DPO designation. Use when discussing privacy, compliance, LGPD, terms of service, privacy policy, data protection, PII, ANPD, data breach, cookie consent, cross-border transfer, or any legal/regulatory requirement for {{PROJECT_NAME}}. Also use when reviewing telemetry, logging, or AI integrations for PII exposure. If your product operates in a regulated industry (finance, health, etc.), add domain-specific regulators on top of the LGPD baseline described here.
author: Canhada-Labs
author_url: https://github.com/Canhada-Labs/ceo-orchestration/tree/main/.claude/skills/core/compliance-lgpd
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: en
---

# LGPD Compliance for {{PROJECT_NAME}}

## Fail-Fast Rule

If any data processing operation lacks a valid legal basis, **stop and reject
the operation**. Never collect, store, process, or transfer personal data without
an explicit legal basis documented in the data processing registry. Never assume
consent was given -- verify it.

## Cardinal Rule

**LGPD applies to ANY processing of personal data of individuals located in
Brazil, regardless of where the data processor is located.** {{PROJECT_NAME}}
operates as a Brazilian SaaS platform with users in Brazil. Every feature,
endpoint, log, telemetry event, and third-party integration must be evaluated
for LGPD compliance before shipping.

## Audit Baseline: Typical Initial Gaps

The following findings represent a typical starting compliance posture for a
new SaaS product. Treat them as a checklist to validate against your own
codebase:

| Finding | Severity | Status |
|---------|----------|--------|
| Terms of Service not yet published | CRITICAL | Not started |
| Privacy Policy not yet published | CRITICAL | Not started |
| PII in telemetry logs (e.g. `client_telemetry` table storing `client_ip`, `user_id`, `session_id`) | HIGH | Identified |
| User content sent to LLM providers without disclosure | HIGH | Identified |
| No cookie consent mechanism | MEDIUM | Not started |
| No data subject rights endpoints (access, deletion, portability) | HIGH | Not started |
| No DPO designated | MEDIUM | Not started |
| No data processing registry (ROPA) | HIGH | Not started |
| Encrypted secrets at rest (e.g. AES-256-GCM for sensitive fields) but no key rotation policy | MEDIUM | Partial |
| No data breach notification procedure | HIGH | Not started |

## LGPD Legal Bases (Art. 7)

For each category of data processing, {{PROJECT_NAME}} must identify one of
these legal bases:

| Legal Basis | LGPD Article | When to Use |
|-------------|-------------|-------------|
| Consent | Art. 7, I | Optional features: AI analysis, newsletter, behavioral analytics |
| Contractual necessity | Art. 7, V | Core SaaS: account, billing, feature delivery |
| Legitimate interest | Art. 7, IX | Security logs, fraud detection, product analytics (anonymized) |
| Legal/regulatory obligation | Art. 7, II | Tax records, sector-specific regulatory reporting |
| Credit protection | Art. 7, X | Billing dispute resolution |

### {{PROJECT_NAME}} Data Processing Registry

```
| Data Category              | Legal Basis         | Retention    | Shared With          |
|----------------------------|---------------------|--------------|----------------------|
| User profile (email, name) | Contractual         | Account life + 5yr | Supabase, Stripe |
| Sensitive credentials (enc)| Contractual         | Until revoked      | Never shared     |
| User-generated content     | Contractual         | Account life       | Supabase         |
| Usage data / activity      | Contractual         | Account life       | AI providers*    |
| IP addresses (telemetry)   | Legitimate interest | 7 days             | Supabase         |
| Session/browser data       | Legitimate interest | 7 days             | Supabase         |
| AI analysis requests       | Consent             | 30 days            | Anthropic, OpenAI, Google |
| Billing data               | Contractual         | 5 years (tax)      | Stripe           |
| Public/aggregated data     | N/A                 | 90 days raw        | Public API       |
| Derived analytics          | N/A (aggregated)    | 90 days            | None             |
```

*AI providers: Requires explicit consent + disclosure of which providers.

## PII Classification for {{PROJECT_NAME}}

### Directly Identifying PII

- `profiles.email` -- account email
- `profiles.full_name` -- display name
- `client_telemetry.client_ip` -- IP address (PII under LGPD)
- `client_telemetry.user_id` -- links to profile
- Encrypted third-party credentials (`api_key_enc`) -- linked to user
- Stripe `customer_id` -- links to payment identity

### Indirectly Identifying PII

- `client_telemetry.session_id` -- can correlate browsing patterns
- `client_telemetry.browser`, `viewport`, `locale` -- device fingerprinting
- `user_actions.*` -- behavior patterns that can be re-identified
- User content (notes, messages, uploaded files) sent to AI -- may reveal identity

### Non-Personal but Sensitive

- Public reference data and aggregates -- not PII
- System health metrics and logs (after PII scrubbing) -- not PII
- Integration health metadata -- not PII

## Data Subject Rights (LGPD Art. 18)

{{PROJECT_NAME}} must implement endpoints for each right:

### 1. Right of Access (Art. 18, II)

```typescript
// GET /api/privacy/my-data
// Returns all personal data associated with the authenticated user.
// Must include: profile, telemetry, activity history, user content,
// AI analysis history, billing records, API keys (masked).
// Response format: structured JSON + option for machine-readable export.
// Deadline: 15 days from request (Art. 19).
```

### 2. Right of Correction (Art. 18, III)

```typescript
// PATCH /api/privacy/my-data
// Allows correction of inaccurate personal data.
// Fields: email, full_name, locale preferences.
// Must propagate corrections to Stripe customer record.
```

### 3. Right of Deletion (Art. 18, VI)

```typescript
// DELETE /api/privacy/my-data
// Deletes all personal data except what is legally required to retain.
// Must delete: telemetry, session data, AI history, API keys.
// Must retain: any records mandated by sector/tax law (e.g. invoices 5yr).
// Must anonymize retained records (remove email, name linkage).
// Must revoke all active sessions and API keys.
// Must request deletion from Stripe (customer.delete).
// Must NOT request deletion from AI providers (they have their own retention).
// Document what was deleted vs retained and why.
```

### 4. Right of Portability (Art. 18, V)

```typescript
// GET /api/privacy/export
// Returns all user data in a structured, machine-readable format (JSON).
// Includes: profile, activity history, user content, API key metadata.
// Must be delivered within 15 days (can be immediate for digital).
// Format: JSON with clear schema documentation.
```

### 5. Right to Revoke Consent (Art. 18, IX)

```typescript
// POST /api/privacy/revoke-consent
// Body: { scope: "ai_analysis" | "newsletter" | "telemetry" | "all" }
// Immediately stops processing for the revoked scope.
// AI analysis: stop sending user content to LLM providers.
// Telemetry: stop collecting client_ip, browser, session data.
// Must not degrade core service (contractual basis still valid).
```

### 6. Right to Information (Art. 18, I)

```typescript
// GET /api/privacy/processing-info
// Public endpoint. Returns:
// - What data is collected and why
// - Legal basis for each category
// - Third parties data is shared with
// - Data retention periods
// - How to exercise rights
// - DPO contact information
```

## Cross-Border Data Transfer (LGPD Art. 33)

### Example: Data Sent to AI Providers

A typical SaaS may send user content and contextual data to one or more LLM
providers for AI-powered features:

| Provider | Location | Data Sent | Legal Mechanism |
|----------|----------|-----------|-----------------|
| Anthropic (Claude) | USA | User content + app context | Consent + Standard Contractual Clauses |
| OpenAI (GPT) | USA | User content + app context | Consent + Standard Contractual Clauses |
| Google (Gemini) | USA | User content + app context | Consent + Standard Contractual Clauses |

### Requirements for Lawful Transfer

1. **Explicit consent** (Art. 33, VIII): User must opt-in to AI analysis with
   clear disclosure that data leaves Brazil.

2. **Standard Contractual Clauses** (Art. 33, II-b): Verify each provider's
   DPA (Data Processing Agreement) covers LGPD requirements.

3. **Data minimization**: Send only the minimum data needed for analysis.
   Strip email, name, IP from AI requests. Use anonymized representations
   where possible.

4. **Provider DPA review checklist**:
   - Anthropic: Review usage policy for data retention (currently: no training on API data)
   - OpenAI: Review DPA for LGPD compliance, data retention settings
   - Google: Review Cloud DPA for Gemini API

```typescript
// CORRECT: Anonymized AI request
const aiRequest = {
  items: records.map(r => ({
    type: r.type,           // generic classifier -- not PII
    size_bucket: r.bucket,  // aggregate value -- not PII
    created_at: r.created_at,
  })),
  app_context: { /* aggregated non-personal context */ },
  // NO email, NO name, NO user_id, NO IP
};

// WRONG: Leaking PII to AI provider
const aiRequest = {
  user_email: user.email,  // NEVER
  user_name: user.name,    // NEVER
  ip: req.ip,              // NEVER
  raw_records: records,    // may contain PII
};
```

## Cookie Consent

### Requirements

{{PROJECT_NAME}} frontend (Vercel) must implement a cookie consent banner compliant
with LGPD Art. 7, I (consent) and Art. 8 (consent requirements):

1. **Before consent**: Only essential cookies (session, CSRF, auth).
2. **After consent**: Analytics, telemetry, preferences.
3. **Granular choices**: User must be able to accept/reject by category.
4. **Easy withdrawal**: Consent must be as easy to revoke as to give.
5. **Record of consent**: Store consent timestamp and scope in `profiles`.

### Cookie Categories for {{PROJECT_NAME}}

| Category | Examples | Legal Basis | Requires Consent |
|----------|---------|-------------|-----------------|
| Essential | Session JWT, CSRF token | Contractual | No |
| Analytics | Page views, feature usage | Legitimate interest | Yes (opt-out) |
| Telemetry | client_telemetry events | Legitimate interest | Yes (opt-out) |
| Preferences | Locale, theme, dashboard layout | Consent | Yes |
| Third-party | Stripe.js, AI provider calls | Consent | Yes |

## Terms of Service Requirements

### Mandatory Clauses for a Brazilian SaaS

1. **Service description**: Concise description of what the product does and
   for whom. Add any sector-specific capabilities your product offers.

2. **User eligibility**: Age requirements (usually 18+) and any
   jurisdiction-specific identifiers (e.g. CPF for Brazilian residents).

3. **Account responsibilities**: Credential security, acceptable use.

4. **Domain disclaimers**: Any disclaimers required by the sector your
   product operates in. Common examples:
   - Data is provided "as-is" with no guarantee of accuracy.
   - AI outputs are informational only, not professional advice.
   - Past performance does not guarantee future results.
   - (If regulated: add the sector-specific disclaimers your regulator requires.)

5. **Data processing**: Reference Privacy Policy. Explicit consent for AI features.

6. **Subscription and billing**: Tier descriptions, pricing in the user's
   currency, cancellation policy, refund policy (CDC Art. 49: 7-day regret
   period for online purchases).

7. **Intellectual property**: {{PROJECT_NAME}} owns the platform. Users own their data.

8. **Limitation of liability**: Maximum liability = fees paid in last 12 months.
   No liability for upstream service outages, data delays, or downstream losses.

9. **Termination**: Either party can terminate. Data retention post-termination
   per LGPD requirements.

10. **Governing law**: Brazilian law (Lei 10.406/2002 Civil Code, CDC 8.078/1990).
    Forum: Comarca of company registration.

## Privacy Policy Requirements

### Mandatory Sections (LGPD Art. 9)

1. **Identity of controller**: Company name, CNPJ, address, DPO contact.

2. **Data collected**: Full list by category (see PII Classification above).

3. **Purpose of processing**: Specific purpose for each data category.

4. **Legal basis**: Which Art. 7 basis applies to each processing activity.

5. **Data sharing**: All third parties, their purposes, and safeguards.
   Must list: Supabase (hosting), Stripe (billing), Anthropic/OpenAI/Google (AI),
   your PaaS (e.g. Fly.io, Railway, Render, Heroku, AWS) (infrastructure).

6. **International transfer**: Disclosure of data sent outside Brazil,
   safeguards applied, user's right to object.

7. **Retention periods**: Per-category retention (see registry above).

8. **Data subject rights**: How to exercise each right, response deadlines.

9. **Security measures**: Encryption at rest (Supabase), in transit (TLS),
   credential encryption (AES-256-GCM), access controls.

10. **Cookies**: Cookie policy (can be embedded or separate).

11. **Updates**: How users are notified of policy changes.

12. **DPO contact**: Name, email, phone.

## Sector-Specific Regulations (Domain Overlay)

LGPD is the baseline for any Brazilian product. Regulated industries add
extra rules on top. Build a table for your own sector. Example shape:

| Regulation | Scope | Impact on {{PROJECT_NAME}} |
|-----------|-------|-------------------|
| [Sector law] | [What it covers] | [What you must comply with] |
| [Agency rule] | [Reporting obligations] | [Thresholds and frequency] |
| [Tax authority guideline] | [Tax reporting] | [When you need to file and about whom] |
| [AML/KYC requirements] | [If you move money or high-risk data] | [Identity verification, suspicious activity reports] |

### {{PROJECT_NAME}} Classification

Classify your product honestly against the sector rules. A typical SaaS
might be a **data or workflow platform** with **limited direct regulatory
exposure**, in which case LGPD alone may cover you. But if you handle
money, health data, children's data, or other regulated categories, the
sector overlay can be substantial.

- **Pure SaaS (no regulated flows)**: LGPD only.
- **Handles money/payments**: add financial regulator + AML/KYC rules.
- **Handles health data**: add health regulator rules.
- **Targets minors**: add ECA/COPPA-equivalent rules.

Disclose to users which categories apply so they understand the full
compliance posture.

## Audit Trail Requirements

### What Must Be Logged (Tamper-Evident)

```typescript
// audit_log table -- append-only, no UPDATE/DELETE policies
interface AuditEntry {
  id: bigint;
  timestamp: string;         // ISO 8601
  actor_type: 'user' | 'system' | 'admin' | 'webhook';
  actor_id: string;          // user UUID or 'system'
  action: string;            // 'login' | 'record_created' | 'consent_granted' | etc.
  resource_type: string;     // 'profile' | 'record' | 'api_key' | 'consent'
  resource_id: string;
  details: Record<string, any>;  // action-specific context
  ip_address: string;        // for accountability (retained per legal basis)
  user_agent: string;
}
```

### Required Audit Events

- User login/logout (with IP)
- Consent granted/revoked (with scope and timestamp)
- Personal data access (who accessed, when, what)
- Personal data export requested
- Personal data deletion requested and executed
- Business-critical mutations (per your domain)
- API key created/revoked
- Admin actions (tier changes, manual overrides)
- Data breach detection

### Retention for Audit Logs

- Security events: 5 years (typical banking/regulated baseline)
- Consent records: Duration of processing + 5 years
- Business activity subject to tax/sector rules: per that rule (commonly 5 years)
- General audit: 2 years minimum

## Data Breach Notification (LGPD Art. 48)

### Procedure

1. **Detection**: Automated monitoring for unauthorized access, data exfiltration,
   credential compromise. Check: Supabase audit logs, your PaaS access logs (e.g. Fly.io, Railway, Render, Heroku, AWS),
   Stripe webhook anomalies.

2. **Assessment** (within 24h):
   - What data was compromised?
   - How many data subjects affected?
   - What is the risk level? (PII exposed? Financial data? Credentials?)

3. **Notification to ANPD** (within 72h of awareness -- ANPD Resolucao CD/ANPD 15):
   - Description of the incident
   - Categories of data subjects affected
   - Categories of personal data concerned
   - Number of affected data subjects
   - Measures taken to mitigate

4. **Notification to data subjects** (if high risk):
   - Clear, plain language description
   - What data was affected
   - What they should do (change passwords, revoke API keys)
   - Contact for DPO

5. **Remediation**:
   - Revoke compromised credentials
   - Rotate encryption keys if needed
   - Patch vulnerability
   - Update security measures
   - Document lessons learned

### Breach Notification Template

```
Subject: [{{PROJECT_NAME}}] Security Incident Notification

We identified unauthorized access to [DESCRIPTION] on [DATE].

Affected data: [LIST]
Number of users affected: [COUNT]
Actions taken: [MEASURES]

What you should do:
- Change your {{PROJECT_NAME}} password immediately
- Revoke and regenerate any third-party credentials stored in {{PROJECT_NAME}}
- Monitor connected accounts for unauthorized activity

Contact our Data Protection Officer: [DPO_EMAIL]
```

## DPO Designation

LGPD Art. 41 requires designation of a Data Protection Officer (Encarregado).

Requirements:
- Named individual or entity
- Contact information publicly available (Privacy Policy + website)
- Responsibilities: receive complaints, advise on data protection, interface
  with ANPD, maintain processing records
- Must be independent (no conflict of interest with business decisions)

For early-stage: Can be the founder/CTO initially, but must be formally
designated and published.

## Implementation Priority

| Priority | Item | Effort | Impact |
|----------|------|--------|--------|
| P0 | Privacy Policy (publish) | 2-3 days | Unblocks all compliance |
| P0 | Terms of Service (publish) | 2-3 days | Legal protection |
| P1 | Cookie consent banner | 1 day | Frontend + preferences table |
| P1 | AI consent gate (opt-in before sending data to LLMs) | 1 day | Cross-border compliance |
| P1 | client_telemetry IP anonymization (hash or truncate after 7d) | 0.5 day | PII reduction |
| P2 | Data subject rights endpoints (access, delete, export) | 3-5 days | Art. 18 compliance |
| P2 | Audit log table + event recording | 2-3 days | Accountability |
| P2 | DPO designation + public contact | 0.5 day | Art. 41 |
| P3 | Data processing registry (ROPA) document | 1-2 days | Art. 37 |
| P3 | Breach notification procedure (documented) | 1 day | Art. 48 |
| P3 | Provider DPA review (Anthropic, OpenAI, Google) | 2-3 days | Cross-border |

## Telemetry PII Remediation

### Current State: `client_telemetry` Table

The `client_telemetry` table (sql/core_tables.sql) stores:
- `client_ip` TEXT -- full IP address (PII under LGPD)
- `user_id` TEXT -- direct user identifier
- `session_id` TEXT -- correlatable to user
- `browser` TEXT -- device fingerprinting component
- `viewport` TEXT -- device fingerprinting component

### Remediation Steps

1. **IP anonymization**: Hash or truncate IP after 7 days.
   ```sql
   -- Daily cleanup: anonymize IPs older than 7 days
   UPDATE public.client_telemetry
   SET client_ip = 'anonymized'
   WHERE created_at < NOW() - INTERVAL '7 days'
   AND client_ip != 'anonymized';
   ```

2. **User ID pseudonymization**: For analytics, use hashed user_id.

3. **Retention**: Delete telemetry rows older than 30 days (already 7d cleanup
   exists in wiring.ts, but verify it runs).

4. **Consent gate**: Only collect telemetry if user has consented to
   "analytics" cookie category.

## Anti-Patterns to Reject

| Anti-Pattern | Why It's Wrong | Correct Approach |
|---|---|---|
| Collecting data "just in case" | Violates data minimization (Art. 6, III) | Collect only what's needed with documented purpose |
| Burying consent in ToS | Consent must be separate and specific (Art. 8) | Granular consent per processing purpose |
| Soft-delete for "deletion" requests | Data subject expects actual deletion | Hard delete + anonymize retained records |
| Sending full user profile to AI | Data minimization violation | Strip PII, send only minimal task-specific payload |
| IP logging without retention policy | Indefinite PII storage | Auto-anonymize after 7 days |
| No audit trail for data access | Cannot prove compliance to ANPD | Append-only audit log for all PII operations |
| Assuming consent once given is permanent | Consent can be revoked anytime (Art. 8, 5) | Check consent status before each processing |
| Same legal basis for everything | Each processing needs its own basis | Map each data flow to specific Art. 7 basis |
| Pre-checked consent boxes | Not freely given consent (Art. 8, 4) | Opt-in only, no defaults |
| Treating public/aggregated data as PII | Over-compliance wastes resources | Classify correctly -- aggregated/non-personal data is not PII |

## Compliance Frameworks Beyond LGPD

LGPD is one node in a wider regulatory graph. A {{PROJECT_NAME}} deployment
that crosses borders, accepts payment cards, handles patient data, or sells
to enterprise buyers will face overlapping rule sets — each with its own
articles, control catalog, evidence cadence, and auditor archetype. Treating
them as independent verticals duplicates work. Treating them as one frame
hides material differences. The table below is the discrimination matrix
the Compliance Specialist consults before scoping any new audit cycle.

| Framework | Scope trigger | Authority / certifier | Control catalog | Audit rhythm | Evidence shape |
|---|---|---|---|---|---|
| LGPD (this skill) | Personal data of subjects in Brazil | ANPD (regulator, not certifier) | LGPD Art. 6-9 + Resolucao CD/ANPD series | Continuous; spot inspections; mandatory breach notice 72h | DPIA, ROPA, consent ledger, breach log |
| GDPR | Personal data of subjects in EU/EEA | National DPAs (e.g. CNIL [FR], BfDI [DE], AEPD [ES]) | GDPR Articles 5-32 + EDPB guidelines | Continuous; DPO maintains register; 72h breach notice | DPIA (Art. 35), Records of Processing (Art. 30), DPA chain |
| UK GDPR | Personal data of subjects in the UK | ICO (Information Commissioner's Office) | UK GDPR + DPA 2018 | Continuous; complaint-driven enforcement; 72h breach notice | DPIA, ROPA, DPA chain; verify current ICO guidance on cross-border transfers (UK ↔ EEA), EU representative requirements, adequacy decisions, and Data (Use and Access) Act updates before treating UK and EU regimes as interchangeable |
| SOC 2 (Type II) | US enterprise sales gating; trust criteria opt-in | AICPA-licensed CPA firm (third-party auditor) | TSC: CC1-CC9 + optional A1/C1/PI1/P1-P8 | Annual report covering 6-12 month observation window | Control narratives, sampled evidence per CC, exception log |
| ISO/IEC 27001:2022 | International ISMS certification | Accredited certification body (e.g. BSI, DNV, Schellman) | Annex A: 93 controls across 4 themes (organizational, people, physical, tech) | Certification cycle: stage 1 + stage 2; surveillance year 1+2; recert year 3 | Statement of Applicability, risk register, internal audit reports, management review minutes |
| HIPAA | Protected Health Information of US patients | HHS Office for Civil Rights (OCR) | 45 CFR Part 164 — Administrative, Physical, Technical safeguards | No certification; complaint-driven enforcement; HHS audit program | Risk analysis, BAAs with subprocessors, training logs, breach notifications |
| PCI-DSS v4.0 | Storage/processing/transmission of cardholder data | QSA (third-party) for L1; SAQ for L2-L4 | 12 requirements grouped into 6 control objectives | Annual ROC or SAQ; quarterly ASV scans; ongoing | Network diagrams, scan reports, QSA workpapers, segmentation evidence |

### Discrimination rules

- **LGPD vs GDPR**: legal text is closely modeled but data-subject-rights
  windows differ (LGPD Art. 19: 15 days; GDPR Art. 12: one month extendable).
  Cross-border transfer mechanisms are NOT interchangeable — LGPD Art. 33
  references its own list, not Standard Contractual Clauses templated by
  the European Commission. NEVER assume a GDPR DPA satisfies LGPD by
  default; the controller-processor language must mention LGPD or be
  appended with an LGPD addendum citing Art. 33-39.
- **SOC 2 vs ISO 27001**: SOC 2 produces an attestation report (text
  consumed by buyers); ISO 27001 produces a certificate (binary pass/fail
  consumed by procurement filters). A SOC 2 report can be shared under
  NDA; a 27001 certificate is published. The two often share evidence
  but the auditor's question shape differs — SOC 2 asks "did the control
  operate over the period?", ISO asks "is the ISMS implemented and
  maintained per the SoA?". DO NOT pitch one as "equivalent" to the
  other to a buyer; they are not.
- **HIPAA vs everything else**: HIPAA has no certifier — there is no
  "HIPAA certified" badge. Vendors that claim it are either confused
  or selling a third-party-attested control set. The framework's
  position: when a counterparty asks "are you HIPAA compliant?", the
  honest answer is "we sign a BAA and our controls map to the Security
  Rule safeguards; here is the gap analysis", not "yes".
- **PCI-DSS scope discipline**: scope creep is the #1 cost driver. If
  cardholder data flows through {{PROJECT_NAME}} servers (even ephemerally),
  every connected system is in scope. Use a tokenization provider
  (Stripe.js, Adyen Drop-in, Braintree Hosted Fields) and verify the
  PAN never reaches your TLS termination point. Network segmentation
  evidence is what shrinks the audit surface — without it, the QSA
  treats the entire VPC as in-scope.

### Control overlap (one control, many frameworks)

A single mature control answers multiple framework questions. Map once,
satisfy many. Examples for a typical SaaS:

| Control | LGPD | GDPR | SOC 2 | ISO 27001 | HIPAA | PCI-DSS |
|---|---|---|---|---|---|---|
| MFA on admin/production access | Art. 46 (security) | Art. 32 | CC6.1 | A.5.16, A.8.5 | 164.312(d) | Req 8.4 |
| Encryption at rest for sensitive stores | Art. 46 | Art. 32 | CC6.1 / C1.1 | A.8.24 | 164.312(a)(2)(iv) | Req 3.5 |
| Encryption in transit (TLS 1.2+) | Art. 46 | Art. 32 | CC6.7 | A.8.24 / A.8.20 | 164.312(e)(1) | Req 4.2 |
| Quarterly access review | Art. 46 | Art. 32 | CC6.2 | A.5.18 | 164.308(a)(4) | Req 7.2 |
| Vendor / subprocessor risk register | Art. 39 | Art. 28 | CC9.2 | A.5.19 | BAA inventory | Req 12.8 |
| Centralized audit logging | Art. 37 | Art. 30 | CC7.2 | A.8.15, A.8.16 | 164.312(b) | Req 10 |
| Documented incident response | Art. 48 | Art. 33-34 | CC7.4 | A.5.24-A.5.27 | 164.308(a)(6) | Req 12.10 |
| Background checks on personnel with prod access | n/a (recommended) | Art. 32 | CC1.4 | A.6.1 | 164.308(a)(3) | Req 12.7 |

The Compliance Specialist's job is to design the control once, write the
evidence pipeline once, and produce the framework-specific narrative many
times. NEVER author seven separate control documents for the same
underlying mechanism.

## Cross-Framework Evidence Pipeline

Evidence collection breaks under manual labor at small scale and breaks
spectacularly at scale. The framework's stance: every recurring evidence
artifact gets a producer, a destination, a cadence, and a verification
step. Manual collection is the exception, documented as such.

### Evidence taxonomy (what every framework actually asks for)

Six artifact families cover most asks. The framework names below are the
canonical names — auditor terminology varies, but the underlying asks
collapse to these six.

| Family | Examples | Typical source | Cadence floor |
|---|---|---|---|
| Identity & access | IAM user list, group membership, MFA status, SSO config | IdP API (Okta, Entra ID, Google Workspace) + cloud IAM | Quarterly export with monthly delta |
| Access reviews | Reviewer attestation per principal per system | GRC tool or ticketing workflow | Quarterly for prod; semiannual for non-prod |
| Cryptographic posture | KMS key inventory, rotation state, TLS cert ages, cipher suites | KMS API + cert observability + nmap-tls | Continuous scan; monthly snapshot |
| Vendor / subprocessor risk | DPA inventory, SOC 2 reports collected, sub-tier flow-down | Procurement system + GRC | Annual review per vendor; new-vendor before signing |
| Incident & breach record | Postmortems, breach notifications, timeline | Ticketing + this skill's templates | Per event + monthly aggregate |
| Change management | PR merge logs with approver, prod deploy log, schema migration log | Git host API + deploy pipeline + DB migration log | Continuous with monthly sample |

### Pipeline architecture

```
producer (system of record)
  -> exporter (scheduled job / webhook handler)
  -> normalizer (convert to canonical schema)
  -> evidence store (append-only, content-addressed, time-stamped)
  -> indexer (control-id -> [artifact_uri, timestamp, hash] mapping)
  -> auditor view (read-only export per control, per period)
```

Three properties the store MUST have:

1. **Append-only with cryptographic timestamps.** A SOC 2 auditor's
   #1 trick is asking for an artifact "as of date X". If the store
   permits silent overwrites, the auditor cannot trust any artifact
   they did not personally pull at the time. Use object-lock /
   versioned-bucket / WORM storage; record the SHA256 + ingest
   timestamp in a separate ledger.
2. **Hash-chained ledger of ingestions.** Each evidence-store write
   produces a ledger entry `(prev_hash, artifact_sha256, ts,
   producer_id, control_id_set)`. The chain is independently
   verifiable; tampering with one entry breaks the downstream chain.
   This is the same pattern the framework's `audit_log` hook uses for
   its own audit trail (HMAC-chained per-instance via `_lib/audit_emit.py`).
3. **Read-only auditor view.** External auditors get a per-control,
   per-period export — never raw store access. The view is generated
   on demand and watermarked with the auditor's name and the request
   timestamp; copies that leak get traced back.

### CORRECT vs WRONG — evidence over time

```
# CORRECT — evidence captured continuously, sampled at audit time
Q1 access review: ticket-1234 (closed 2025-04-12) reviewed 312 principals,
  17 deprovisioned, evidence stored at evidence://access-reviews/2025-q1/...
Q2 access review: ticket-1567 (closed 2025-07-08) reviewed 318 principals,
  9 deprovisioned, evidence stored at evidence://access-reviews/2025-q2/...

# WRONG — evidence rebuilt the week before the audit
"We did access reviews quarterly. Here's a single spreadsheet covering
all of 2025 that someone built last week from current Okta state."
```

The wrong pattern fails sampling. The auditor will pick a random month
inside the period and ask "show me the deprovisioning of user X who
left on 2025-04-30" — if the evidence is a year-end snapshot, the
detail is gone and the control is rated `not effective` for the
period. The fix is not to argue with the auditor; the fix is to build
the pipeline in advance.

### Multi-framework collection cadence

A single artifact often satisfies multiple frameworks if collected at
the highest-frequency framework's cadence. Example: a quarterly access
review with documented reviewer attestation satisfies SOC 2 CC6.2 (any
period in the audit window can be sampled), ISO 27001 A.5.18 (operating
effectively), HIPAA 164.308(a)(4) (Information Access Management), and
LGPD Art. 46 (security measures). One review, four narratives. NEVER
run a separate "SOC 2 access review" and "ISO access review" — that is
duplicated cost producing identical evidence.

### Evidence-pipeline anti-patterns

| Anti-Pattern | Failure mode | Correct approach |
|---|---|---|
| Manual screenshot evidence | Not reproducible; auditor cannot verify timestamp; attacker-tamperable | Programmatic export with embedded timestamp + content hash |
| Single evidence run before audit | Sampling failure; period-of-effectiveness gap | Continuous capture; auditor samples the store, not a re-run |
| Evidence stored in mutable bucket | Auditor cannot trust historical artifacts | Object-lock or WORM bucket with versioning |
| One copy of each report | Loss of original auditor-watermarked copy | Per-auditor watermarked exports; originals retained in store |
| Re-using last year's narrative verbatim | Spec drift between control as designed and control as operated | Annual re-walk of each control with current evidence; narrative is regenerated, not pasted |
| Treating LGPD ROPA and GDPR Art. 30 register as separate documents | Duplicate maintenance; drift between them | Single processing registry with framework-mapping column |

## Audit-Readiness Posture

The Compliance Specialist runs an audit cycle in three phases. The phases
are sequential — you do not start phase B before phase A produces a
prioritized gap list, and phase C is driven by phase B's output, not by
the auditor's first email.

### Phase A — Readiness assessment

Goal: produce an honest scorecard of the current control posture against
the target framework's catalog. Deliverable is a per-control rating:
`absent` / `documented-only` / `implemented` / `tested` / `audit-ready`.

The auditor archetype rates conservatively. A control that exists in a
runbook but has never been exercised is `documented-only`, not
`implemented`. A control that runs but has no evidence trail is
`implemented`, not `tested`. A control that is `audit-ready` has all
of: written description, deployed mechanism, evidence in the pipeline,
operating effectively for the entire intended audit period, and a named
owner who can walk an external auditor through it.

```
# CORRECT — readiness scorecard with honest ratings
CC6.1 Logical access controls
  - Description: documented in policy v3.2 (2025-08-14)
  - Mechanism: SSO + MFA enforced via IdP policy
  - Evidence: weekly export of MFA-status from IdP API since 2025-09-01
  - Period of operation: 6 weeks of evidence, audit window requires 6 months
  - Rating: implemented (not yet audit-ready — need 5 more months of evidence)
  - Owner: head-of-platform

# WRONG — readiness scorecard built from optimism
CC6.1 — "audit-ready" (because we have SSO and feel good about it)
```

The wrong pattern produces a false-confidence scorecard that crashes
mid-audit. The right pattern produces an honest gap list that drives
phase B.

### Phase B — Gap remediation

Goal: close the controls rated below `audit-ready`, in priority order
weighted by `(audit-blocker severity) * (likelihood of being sampled) /
(remediation effort)`. The Compliance Specialist publishes the gap list
with owners and dates; the engineering org closes the gaps; the
specialist re-rates each control as remediation lands.

Two non-negotiables:

1. **Period of operation matters.** A control rolled out two weeks
   before the audit period closes generally cannot be claimed for the
   full period. The remediation plan MUST account for this — either
   move the audit window or scope the control to a future period.
   NEVER claim period coverage that the evidence does not support.
2. **Compensating controls are documented, not assumed.** When a
   control gap cannot be closed in time, the substitute mechanism is
   written down (what it is, why it covers the gap, who approved
   it) and presented to the auditor proactively. Surprise compensating
   controls discovered mid-audit produce findings.

### Phase C — Auditor engagement

Goal: produce a clean attestation/certificate. The cycle here is
walkthrough → request-list → evidence delivery → finding → response →
report. The framework's discipline applies at the conversation layer:

- **Answer the question asked, not the question imagined.** The
  auditor's request "show me how user provisioning works" is not an
  invitation to walk through the entire IAM architecture. Pull the
  control-specific evidence; offer the broader context only if asked.
  NEVER volunteer information about controls outside the audit scope —
  that material becomes a finding even if the in-scope control passes.
- **A finding is not a fight.** When the auditor flags a gap, the
  response sequence is: clarify the finding, agree on the underlying
  fact, propose a remediation with date, document the compensating
  control if any, accept or appeal in writing. Verbal pushback to a
  finding without a written counter-proposal produces a worse rating,
  not a better one.
- **Scope discipline at the walkthrough.** The auditor's first
  question — usually "tell me about your business" — is also a scoping
  question. Volunteering "we also process some healthcare data for one
  client" can pull HIPAA into a SOC 2 audit that did not require it.
  Pre-rehearsed walkthrough scripts (one per control owner) prevent
  this. The script answers the asked question and stops.
- **Exceptions are written, not narrated.** Any deviation from the
  control as designed (one server outside the standard, one user
  exempt, one period without evidence) is documented with: who
  approved, why, expiration date, compensating control. The auditor
  will find the exception; the only question is whether you found it
  first.

### Audit-readiness posture anti-patterns

| Anti-Pattern | Why it fails | Correct approach |
|---|---|---|
| "We're SOC 2 ready" with no scorecard | Self-rating without evidence collapses on contact with the auditor | Honest readiness scorecard per control before claiming readiness |
| Building evidence the week before kickoff | Period-of-operation gap; sampling fails | Build evidence pipeline 6+ months before target audit window |
| Letting engineering own the auditor relationship without a specialist | Engineers volunteer detail that auditors weaponize as scope | Compliance Specialist mediates; engineers answer specific questions through the specialist |
| Treating findings as personal attacks | Defensive responses produce worse ratings | Findings are facts about the system; respond with remediation plans |
| Skipping the walkthrough rehearsal | First-time-explained controls generate clarification rounds and findings | Rehearse each walkthrough; control owner can explain the control in two minutes |
| Promising audit timeline without phase-A scorecard | Slip becomes inevitable; auditor confidence drops | Scorecard first; timeline derived from scorecard, not from leadership wishful thinking |
| Bundling unrelated frameworks in one window | Cross-contamination of scope | Stagger frameworks; share evidence pipeline, not audit windows |

## References

- `core/security-and-auth` — auth + breach handling intersection (security
  VETO floor under ADR-052)
- `core/incident-management` — breach response procedure invoked from
  Art. 48 path
- `core/code-review-checklist` — the adversarial-framing methodology
  used by the Compliance Specialist on phase-A readiness scorecards
- `ADR-052` — multi-model dispatch by role (Compliance is a VETO-floor
  archetype)
- `domains/fintech/*` — sector overlay examples for regulated SaaS
