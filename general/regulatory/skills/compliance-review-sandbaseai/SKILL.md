---
name: compliance-review-sandbaseai
title: Compliance Review
description: Use when reviewing a change for auditability, personal-data purpose and retention, consent, financial controls, or regulatory traceability gaps.
author: sandbaseai
author_url: https://github.com/sandbaseai/workbuddy-skill/tree/main/skills/compliance-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Compliance Review

Review a change for missing or weakened controls that affect auditability, privacy, retention, consent, financial integrity, or regulatory traceability. Work from the diff and exact repository evidence. This workflow does not provide legal advice or declare compliance; route jurisdiction-specific questions to the accountable privacy, legal, finance, or compliance owner.

## Set scope and obligations

Identify the changed files, feature or process, users and jurisdictions, data classes, records of processing, retention policy, financial impact, applicable standards, control owner, and release gate. State what is out of scope and which evidence sources were unavailable. Treat secrets, personal data, financial records, and incident details as sensitive; use redacted fixtures and least-privileged access.

Start with changed code and configuration, then inspect only the surrounding implementation needed to understand behavior. Use repository-native tests, policy files, schemas, migrations, audit configuration, and logs. Record the revision, commands, tool versions, evidence period, and limitations. Do not infer a control from a variable name, documentation claim, or a passing linter alone.

## Review control areas

Check the following where applicable:

- **Purpose and minimization:** every collected or derived personal-data field has a documented purpose, lawful/business basis owned by the right specialist, minimization rationale, access boundary, and safe failure behavior;
- **Consent and user choice:** consent is specific, informed, revocable, versioned, separated from unrelated terms, and not silently treated as permission after withdrawal; record evidence of state transitions and suppressed processing;
- **Retention and deletion:** storage, backups, caches, exports, logs, and derived records follow an approved retention schedule; deletion, legal hold, subject request, and restoration behavior are explicit and testable;
- **Auditability:** privileged, consent, data-access, financial, configuration, and lifecycle events record actor or service identity, target, action, decision, timestamp, correlation ID, outcome, and policy version without logging secrets or unnecessary PII;
- **Access and segregation:** authorization, tenant boundaries, approval steps, least privilege, dual control, and separation of duties protect sensitive data and financial operations; denied and emergency paths are observable;
- **Financial controls:** amounts, currency, rounding, idempotency, reconciliation, approvals, refunds, limits, and immutable history are validated at the service boundary; distinguish test/sandbox paths from production settlement;
- **Regulatory traceability:** map material obligations to a concrete control, evidence source, owner, review cadence, and exception process; label time-sensitive or jurisdiction-dependent claims for specialist verification.

## Classify findings

Separate confirmed control failure, control weakness, policy mismatch, documentation gap, observation, and unknown. Prioritize unauthorized access or disclosure, untracked financial changes, irreversible retention/deletion failures, missing consent enforcement, and audit gaps that prevent investigation. For each finding record a stable ID, affected path and location, obligation or control, exact evidence, preconditions, impact, severity rationale, owner, remediation, acceptance criteria, deadline, and retest method.

Do not include credentials, raw personal data, or unnecessary exploit instructions. Do not call a missing artifact “low risk” merely because no incident is known. If policy, jurisdiction, ownership, or evidence is ambiguous, state the uncertainty and route it rather than guessing.

## Remediate and hand off

Prefer deterministic enforcement at the service boundary, explicit defaults, redaction, reversible migrations, immutable audit events, and tests for denied, withdrawn, expired, deleted, reconciled, and failure states as relevant. Re-run the focused checks and inspect the resulting diff. Do not close a finding because a ticket exists; retest the control with comparable evidence and record residual risk and approver.

The final report includes scope, changed surfaces, obligations and assumptions, methods and evidence period, findings by class and severity, affected data or financial flows, specialist escalations, remediation owners and dates, exceptions, retest status, limitations, and the next authorized review gate.
