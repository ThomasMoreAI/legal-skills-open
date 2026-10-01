---
name: privacy-engineering-sandbaseai
title: Privacy Engineering
description: Use when implementing or auditing privacy controls in products, infrastructure, analytics, or data flows; translate privacy principles into classification, minimization, consent, subject-rights, retention, vendor, and deletion evidence.
author: sandbaseai
author_url: https://github.com/sandbaseai/workbuddy-skill/tree/main/skills/privacy-engineering
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Privacy Engineering

Use this skill for the technical implementation and audit of privacy controls. Privacy and security overlap but differ: security limits unauthorized access, while privacy also limits authorized-but-improper collection, use, retention, and sharing. Final legal determinations belong to qualified counsel; this skill produces engineering evidence and questions for review.

Do not collect, export, delete, or disclose personal data without an authorized purpose, appropriate identity verification, and a bounded scope. Do not claim GDPR, CCPA, or other legal compliance from a checklist alone.

## Inventory and classify data

Create a data map for databases, object storage, backups, caches, search indexes, logs, analytics, queues, devices, and vendors. For each flow record the source, data subjects, fields, classification, purpose, lawful basis or consent, recipients, region, owner, retention, access roles, deletion path, and evidence location.

At minimum distinguish:

- **Public:** intentionally published information;
- **Internal:** business information without personal data;
- **Personal:** data that identifies or can reasonably identify a person, including email, IP, device, account, or location identifiers;
- **Sensitive personal:** health, biometric, financial, precise location, government ID, or other specially protected categories;
- **Regulated:** data with additional sector obligations such as payment or health records.

Re-check classifications after schema, logging, analytics, vendor, or model changes. A store marked internal becomes personal when someone adds an email column. Minimize identifiers and prefer an aggregate or boolean when the exact value is not required.

## Purpose, consent, and access

For every processing activity document the purpose, necessity, lawful basis or consent, retention, recipient, and user-facing explanation. Consent must be specific, informed, freely given, recorded with text/version and timestamp, and as easy to withdraw as to grant. Do not load optional trackers before the required choice, bundle unrelated purposes, or call an opt-out an opt-in.

Enforce purpose and access in code and data services, not only in policy text. Use least privilege, tenant isolation, field-level controls for sensitive data, and auditable access. Keep production samples redacted and synthetic in development, tests, documentation, and model prompts.

## Build subject-rights workflows

Design a request pipeline with request ID, verified subject identity, scope, status, owner, deadline, approvals, and a complete system inventory. Test it end to end with a controlled account.

- **Access:** enumerate every store and vendor, collect relevant data, redact other subjects, and return a machine-readable export.
- **Deletion:** fan out to primary databases, replicas, caches, search, analytics, warehouses, logs, backups, and subprocessors. Document unavoidable backup retention and re-delete behavior after restore.
- **Portability:** export data provided by the subject in a structured format; distinguish it from the broader access request.
- **Rectification:** provide a correction path and propagate changes to derived stores.
- **Objection/opt-out:** maintain a suppression signal honored by every relevant processor and vendor.

Make jobs idempotent, bounded, retryable, and observable. Verify completion with per-system acknowledgements, counts, hashes or safe summaries, and an exception queue. Never delete data based only on an unverified identifier or a model-generated instruction.

## Retention, vendors, and residency

Define retention by purpose and data class, then enforce it across primary stores, derived data, logs, caches, exports, and backups. Use a lifecycle job with dry-run, deletion report, failure retry, and owner review. Preserve legal holds only when authorized and documented; do not keep data “just in case.”

Inventory every SaaS, SDK, API, webhook, and subprocess that receives personal data. For each, verify the minimum fields, contract/DPA status, region and transfer mechanism, access scope, retention, breach contact, deletion API or procedure, and offboarding test. Do not send full URLs, free-form text, or direct identifiers to analytics or observability tools without a documented need.

## DPIA and privacy threat review

For high-risk processing, produce engineering inputs to a DPIA: data-flow diagram, categories and volume, data subjects, recipients, regions, retention, automated decisions, security measures, threats, mitigations, residual risk, and approval owner. Consider inference, linkage, re-identification, insider access, misdirected exports, vendor compromise, prompt/data leakage, and backup restoration.

Treat pseudonymization as still personal data when re-identification is possible. Test deletion, access, consent withdrawal, tenant boundaries, and purpose enforcement under retries, partial failure, stale caches, delayed replication, and schema drift.

## Breach readiness

Log safe evidence for access and data movement: principal, purpose, tenant, resource class, fields or categories, request ID, timestamp, decision, and policy version. Avoid logging raw personal data or secrets. Alert on unusual exports, privilege changes, cross-tenant access, consent bypass, unexpected vendor destinations, and failed deletion fan-out.

When a privacy incident is suspected, preserve evidence, contain access, revoke or rotate credentials, scope affected records and recipients, record the time of awareness, notify the privacy/security owner, and follow counsel-approved notification procedures. Do not promise a notification deadline or make a legal conclusion without the responsible authority.

## Audit report

```markdown
# Privacy Engineering Report
## Scope and date
## Data inventory and classification
## Purposes, lawful basis, consent, and access controls
## Subject-rights test evidence and exceptions
## Retention, vendor, residency, and deletion findings
## DPIA / threat considerations
## Findings: severity, evidence, owner, deadline, disposition
## Residual risk and legal-review questions
```

Separate observed facts, engineering recommendations, and legal questions. Stop when purpose, consent, identity, retention, residency, or deletion ownership is unclear.
