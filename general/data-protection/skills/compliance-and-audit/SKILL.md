---
name: compliance-and-audit
title: Compliance and Audit
description: Use when a project requires a compliance framework mapping, when risks need formal documentation, when audit evidence must be collected, or when producing a compliance attestation before release. Applies to SOC 2, ISO 27001, GDPR, PCI DSS, NIST CSF, and DORA.
author: Kaademos
author_url: https://github.com/Kaademos/secure-sdlc-agents/tree/main/skills/compliance-and-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Compliance and Audit

## Overview

This skill maintains the governance, risk, and compliance (GRC) layer of the Secure SDLC.
It translates security work into auditable, framework-aligned documentation that survives
a real audit — not a self-assessment checklist filled in the night before.

The discipline: compliance is a continuous process. Every security control implemented
during Build and Test must be captured as evidence at the time it is implemented,
not reconstructed six months later.

## When to Use

- A new project or feature processes regulated data (PII, payment data, health data)
- A compliance gap analysis is required
- Risks need to be formally accepted, transferred, or mitigated on record
- Audit evidence must be collected for a specific control
- Producing a compliance attestation before a release or audit
- Responding to a customer security questionnaire or due diligence request

## Process

### Step 1 — Determine applicable frameworks

Based on data classification and business context, identify which frameworks apply:

| Framework | Applies when… |
|---|---|
| **SOC 2 Type II** | You process customer data and need to demonstrate trust to enterprise buyers |
| **ISO/IEC 27001:2022** | Formal ISMS certification is required (often for EU/UK contracts) |
| **NIST CSF 2.0** | US federal contracts or voluntary alignment with US security standards |
| **PCI DSS v4.0** | Any feature handling payment card data |
| **GDPR / UK GDPR** | Any processing of personal data of EU or UK residents |
| **DORA** | Financial services entities operating in the EU |
| **HIPAA** | Protected health information (PHI) in the US |
| **OWASP ASVS** | Always — this is the technical requirements anchor for all other frameworks |

### Step 2 — Produce the risk register

Create or update `docs/risk-register.md` with every identified risk:

```markdown
| Risk ID | Description | Category | Likelihood | Impact | Inherent Risk | Control(s) | Residual Risk | Owner | Status | Due Date |
|---------|-------------|----------|------------|--------|--------------|------------|--------------|-------|--------|----------|
| R-001 | SQL injection in search endpoint | Application | High | Critical | Critical | Input validation, WAF, SAST | Medium | Dev Lead | Open | YYYY-MM-DD |
| R-002 | Insider access to production DB | Access Control | Medium | High | High | RBAC, PAM, audit logs | Low | Cloud/Platform | Mitigated | — |
```

Every vulnerability found by any agent must appear here with an owner, severity, and status.
Risks do not disappear — they are mitigated, accepted, or transferred, with documentation.

### Step 3 — Map controls to frameworks

Produce a control mapping table that connects ASVS requirements to applicable framework controls:

```markdown
| ASVS Ref | Requirement | SOC 2 | ISO 27001 | NIST CSF | PCI DSS |
|----------|-------------|-------|-----------|----------|---------| 
| V2.1.1 | Password complexity ≥ 12 chars | CC6.1 | A.8.5 | PR.AC-1 | Req 8.3 |
| V6.1.1 | Encryption at rest (AES-256) | CC6.7 | A.8.24 | PR.DS-1 | Req 3.5 |
| V9.1.1 | TLS 1.2+ for all external comms | CC6.7 | A.8.20 | PR.DS-2 | Req 4.2 |
```

### Step 4 — Collect audit evidence at time of implementation

For every control validated during Build or Test, create an evidence record immediately:

```markdown
## Evidence Record: [Control ID]

**Control:** [Framework] — [Reference] — [Control Name]
**Evidence Type:** Test result / Configuration screenshot / Policy document / Log extract
**Date Collected:** YYYY-MM-DD
**Collected By:** [Who or which agent]
**Description:** [What this demonstrates — be specific enough for an auditor who wasn't there]
**Artefact:** [File path or link]
**Review Status:** Pending / Approved
```

Evidence must be collected at implementation time. Evidence reconstructed after the fact
fails audit scrutiny.

### Step 5 — Risk acceptance process

When a risk cannot be fully mitigated before release:

1. Document the risk in full (likelihood, impact, inherent score, existing controls)
2. Describe the residual risk after controls
3. Obtain a written business justification
4. Record the name and role of the approver (must be appropriate seniority for the risk level)
5. Set a mandatory review date — accepted risks expire

```markdown
## Risk Acceptance: [Risk ID]

**Risk:** [Description]
**Inherent Risk:** [Score]
**Mitigating Controls:** [What's already in place]
**Residual Risk:** [Score after controls]
**Business Justification:** [Why this risk is being accepted rather than fixed]
**Accepted By:** [Name, Role]
**Acceptance Date:** YYYY-MM-DD
**Review Date:** YYYY-MM-DD
```

### Step 6 — Produce the release compliance attestation

Before every release, write `docs/audit-evidence/compliance-attestation-vX.Y.Z.md`:

```markdown
## Compliance Attestation — Release vX.Y.Z

**Date:** YYYY-MM-DD
**Frameworks in scope:** [List]

### Control Status Summary

| Framework | Total Controls | Compliant | Gap | Accepted Risk |
|-----------|---------------|-----------|-----|---------------|
| SOC 2 | 22 | 20 | 1 | 1 |

### Open Gaps
[List with owner and remediation timeline]

### Accepted Risks
[List with business justification and approver]

### Attestation
All in-scope controls reviewed. Gaps and accepted risks formally acknowledged.
Release is approved from a GRC perspective pending Release Manager sign-off.
```

## Common Rationalizations

| Excuse | Counter |
|---|---|
| "We'll document compliance after we launch" | Auditors require evidence contemporaneous with the control implementation. Retrospective documentation is a finding. |
| "We're too early-stage for formal compliance" | SOC 2 readiness takes 6–12 months. If you start when a customer requires it, you've already lost the deal. |
| "We've accepted this risk before" | Risk acceptance is time-bound and context-specific. Prior acceptance does not carry forward to a new feature or a changed threat landscape. |
| "The risk register is the security team's job, not mine" | Risk ownership belongs to the team generating the risk. Dev teams own application risks; Cloud teams own infrastructure risks. |
| "Our pentest report counts as audit evidence" | Pentest evidence is one artefact. Auditors require evidence for each control, not a single document. |

## Red Flags

- A risk register that hasn't been updated since the last audit
- Accepted risks with no expiry date — permanent acceptance is not a valid posture
- Compliance controls documented but no evidence they were actually implemented
- A feature handling PII with no GDPR Article 30 record of processing activity
- Audit evidence collected in a rush the week before an audit, not at time of implementation
- Framework mapping that lists "compliant" for controls that were never tested
- Risk acceptance signed off by an engineer rather than appropriate business authority

## Verification

Do not close this phase until:

- [ ] All applicable compliance frameworks identified and documented
- [ ] Risk register is current — all findings from appsec-engineer and cloud-platform-engineer have entries
- [ ] Control mapping table exists in `docs/` and reflects current ASVS requirements
- [ ] Audit evidence collected for every control claimed as implemented
- [ ] All accepted risks have a named approver, business justification, and review date
- [ ] Compliance attestation document written and reviewed before release
- [ ] `grc-analyst` has provided compliance context to `release-manager` for the go/no-go decision
