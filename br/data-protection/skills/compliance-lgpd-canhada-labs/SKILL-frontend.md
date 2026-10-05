---
name: compliance-lgpd
description: LGPD (Lei 13.709/2018) compliance for a Brazilian SaaS platform.
  Covers data subject rights, legal bases for processing, PII classification, data
  retention, cookie consent, Terms of Service, Privacy Policy, cross-border data
  transfer to AI providers, audit trails, breach notification, and DPO designation.
  Use when discussing privacy, compliance, LGPD, terms of service, privacy policy,
  data protection, PII, ANPD, data breach, cookie consent, cross-border transfer,
  or any legal/regulatory requirement for {{PROJECT_NAME}}. Also use when reviewing
  telemetry, logging, or AI integrations for PII exposure. If your product operates
  in a regulated industry (finance, health, etc.), add domain-specific regulators
  on top of the LGPD baseline described here. Owner: Compliance Specialist (archetype).
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
