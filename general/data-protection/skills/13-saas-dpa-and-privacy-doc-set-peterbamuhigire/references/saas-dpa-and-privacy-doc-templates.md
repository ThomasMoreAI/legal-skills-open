# SaaS DPA & Privacy — Document Templates

## A. DPA skeleton

```
DATA PROCESSING ADDENDUM

1. Parties
2. Background and scope
3. Definitions (incorporates GDPR Art.4 definitions)
4. Subject matter, duration, nature, purpose of processing
5. Types of personal data and categories of data subjects
6. Processor obligations:
   6.1 Process only on documented instructions of Controller
   6.2 Confidentiality of personnel
   6.3 Security measures (Annex I — Technical & Organisational Measures)
   6.4 Sub-processors (Annex III — current list; 30-day notice for new; right of objection)
   6.5 Assistance with data-subject rights requests
   6.6 Assistance with DPIA and prior consultation
   6.7 Deletion or return of personal data at end of processing
   6.8 Audit and information rights (with reasonable notice)
7. Controller obligations
8. International transfers — Standard Contractual Clauses incorporated (Annex II)
9. Liability and indemnity
10. Term and termination
11. Governing law

Annex I — Technical & Organisational Measures
Annex II — Standard Contractual Clauses (Module 2 controller-to-processor, EU 2021/914)
Annex III — Sub-processor list (current as of [date])
Annex IV — Country-specific addenda (UK IDTA, Swiss FDPIC, etc.)
```

## B. ROPA template (Art.30 record)

| # | Activity | Purpose | Lawful basis | Data subjects | Personal data | Recipients | Transfers | Retention | Security |
|---|----------|---------|--------------|---------------|---------------|------------|-----------|-----------|----------|
| 1 | User authentication | Identity verification | Performance of contract | End users | email, hashed password, IP | Identity service, audit log | none / SCC where transferred | life of account | TLS, hashed pwd, MFA |
| 2 | Billing | Invoicing | Performance of contract | Tenant admin | name, billing address, payment token | Stripe | SCC | 7 y (tax) | TLS, no PAN stored |
| 3 | Product telemetry | Improvement | Legitimate interest | End users | usage events with tenant_id | metering service | none | 13 mo | TLS, AES-256 at rest |
| ... | | | | | | | | | |

## C. Retention & destruction schedule

| Data class | Retention | Trigger | Destruction method | Verification | Owner |
|------------|-----------|---------|--------------------|--------------|-------|
| Account / billing PII | contract + 7 y | offboarding + retention end | hard delete (verified) | post-delete query = 0 rows | privacy officer |
| Operational data | per contract | offboarding + 30 d grace | hard delete | verified | privacy officer |
| Telemetry raw | 13 mo | TTL | rotate-out from bus | retention policy enforced | platform |
| Aggregates | 7 y | finance retention | rotate-out | finance audit | finance |
| Logs | 13 mo | TTL | rotate-out | retention policy enforced | platform |
| Backups | 35 d (example) | retention end | encrypted rotate-out + key destruction | backup audit | platform |

## D. Breach notification procedure

```
1. Detection: monitoring alarm | audit log | customer report | third-party advisory.
2. Incident commander declared; severity classified using IR matrix; tenant scope estimated.
3. Confirmation within 24 hours of detection.
4. Risk assessment:
   - Categories and number of data subjects.
   - Categories and volume of personal data.
   - Likely consequences.
   - Measures taken / proposed to address.
5. Notify supervisory authority within 72 hours of confirmation (GDPR Art.33):
   - Nature, categories, approximate numbers.
   - Contact details of DPO.
   - Likely consequences.
   - Measures taken or proposed.
6. Notify customers (controllers) within 24 hours of confirmation per DPA.
7. Notify affected data subjects if high risk (GDPR Art.34).
8. Record-keeping: every breach logged in the breach register regardless of notifiability.
9. Postmortem and remediation tracked to closure.
```

## E. DSAR procedure

```
Receipt channels: in-product profile page | privacy@ | postal.
Identity verification: account-based authentication + secondary factor for sensitive requests.
Acknowledgement: within 5 business days.
Statutory windows:
  - GDPR: 30 days, extendable by +60 days with notice.
  - POPIA: reasonable time.
  - CCPA: 45 days, extendable by +45.
Right of access: machine-readable export.
Right to erasure: trigger Tenant Lifecycle Runbook hard-delete; honour exceptions (legal hold, ongoing contract).
Right to portability: standard JSON/CSV export.
Right to rectification: in-product UI + audit-logged change.
Right to object / restrict: feature flag.
Refusals: documented with grounds.
Record-keeping: every request and outcome logged for 3 years.
```
