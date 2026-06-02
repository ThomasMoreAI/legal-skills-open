---
name: compliance-checklist-generation
title: Compliance Checklist Generation
description: Generate compliance checklists for SOC2, HIPAA, PCI-DSS, and GDPR with gap analysis and remediation priorities.
author: seb1n
author_url: https://github.com/seb1n/awesome-ai-agent-skills/tree/main/legal-and-compliance/compliance-checklist-generation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Compliance Checklist Generation

Create structured, actionable compliance checklists for major regulatory frameworks including SOC2, HIPAA, PCI-DSS, and GDPR. This skill maps controls to requirements, assesses readiness against each control, identifies gaps, and produces prioritized remediation plans. Output includes status tracking, evidence requirements, and effort estimates for each control item.

## Workflow

1. **Identify Applicable Frameworks** — Determine which compliance frameworks apply based on the business type, data handled, customer requirements, and geographic reach. A healthcare SaaS needs HIPAA. A company processing credit cards needs PCI-DSS. Enterprise B2B SaaS customers almost universally request SOC2. Serving EU users triggers GDPR. Multiple frameworks often overlap — identify shared controls to reduce duplicate effort.

2. **Map Controls to Requirements** — Break each framework into its constituent control categories and individual requirements. For SOC2, map across the five Trust Services Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy). For HIPAA, cover Administrative, Physical, and Technical Safeguards. For PCI-DSS, address all 12 requirement families. For GDPR, map to Articles 5-49 covering principles, rights, and obligations.

3. **Assess Current State** — For each control, evaluate the current implementation status: Implemented (evidence exists), Partially Implemented (control exists but has gaps), Not Implemented (no control in place), or Not Applicable (with documented justification). Where possible, reference existing documentation, tool configurations, or process artifacts as evidence.

4. **Generate Checklist with Status and Gaps** — Produce a structured checklist organized by control category, with each item showing: the requirement description, current status, evidence needed, gap description (if any), and remediation effort estimate (hours/days). Include a summary dashboard showing overall readiness percentage per category.

5. **Prioritize Remediation** — Rank gaps by a combination of risk severity, audit impact, implementation effort, and shared coverage across frameworks. Quick wins (high impact, low effort) should be prioritized first. Group related remediation items that can be addressed together, such as implementing a single logging solution that satisfies SOC2, HIPAA, and PCI-DSS log requirements simultaneously.

## Usage

Specify which framework(s) you need, your business type, current security posture, and any upcoming audit deadlines. The more context about existing controls, the more accurate the gap analysis.

**Example prompt:**
```
Generate a SOC2 Type II readiness checklist for our Series A startup. We're a B2B SaaS running on AWS. We use GitHub for code, Datadog for monitoring, and have about 20 employees. We need to be audit-ready in 6 months.
```

## Examples

### Example 1: SOC2 Type II Readiness for a Startup

**Input:** 20-person B2B SaaS startup on AWS. Uses GitHub, Datadog, Google Workspace, Slack. No formal security program yet. SOC2 audit in 6 months.

**Output:**

**Readiness Summary:** 34% ready (estimated)

| Category | Controls | Implemented | Partial | Missing | Readiness |
|----------|----------|-------------|---------|---------|-----------|
| Access Control | 12 | 3 | 4 | 5 | 28% |
| Change Management | 8 | 5 | 2 | 1 | 63% |
| Incident Response | 6 | 0 | 1 | 5 | 8% |
| Risk Assessment | 5 | 0 | 0 | 5 | 0% |
| Monitoring & Logging | 7 | 4 | 2 | 1 | 57% |
| Vendor Management | 4 | 0 | 1 | 3 | 13% |
| HR & Security Awareness | 6 | 1 | 2 | 3 | 17% |

**Sample Controls (Access Control category):**

| # | Requirement | Status | Evidence Needed | Gap / Action | Effort |
|---|------------|--------|-----------------|--------------|--------|
| AC-1 | MFA enforced for all production systems | Partial | AWS IAM policy screenshots, IdP config | MFA enabled for AWS console but not for SSH access to EC2 instances. Enable MFA for all access paths. | 2 days |
| AC-2 | Role-based access control with least privilege | Missing | IAM role definitions, access matrix | No formal RBAC model. Define roles, map to AWS IAM policies, GitHub teams, and Google Workspace groups. | 5 days |
| AC-3 | Quarterly access reviews | Missing | Access review records, approval logs | No process exists. Implement quarterly reviews of all system access with manager sign-off. Tool recommendation: Vanta or Drata for automated tracking. | 3 days |
| AC-4 | Offboarding removes access within 24 hours | Partial | Offboarding checklist, deprovisioning logs | Ad hoc process exists but not documented. Formalize checklist covering all systems, automate via identity provider where possible. | 2 days |

**Priority Remediation (Month 1):** Risk assessment (required foundation for all other controls), MFA enforcement across all systems, formal access control policy document, incident response plan draft.

### Example 2: GDPR Compliance for E-Commerce

**Input:** EU-based e-commerce site selling consumer electronics. Collects name, address, email, payment data, browsing behavior. Uses Google Analytics, Meta Pixel, Mailchimp for email marketing. Ships to all EU countries.

**Output:**

**Readiness Summary:** 42% ready (estimated)

| GDPR Area | Requirements | Met | Gaps | Readiness |
|-----------|-------------|-----|------|-----------|
| Lawful Basis & Consent | 8 | 3 | 5 | 38% |
| Data Subject Rights | 7 | 2 | 5 | 29% |
| Data Processing Records | 4 | 1 | 3 | 25% |
| International Transfers | 3 | 1 | 2 | 33% |
| Security Measures | 6 | 4 | 2 | 67% |
| Breach Notification | 3 | 1 | 2 | 33% |
| DPO & Governance | 4 | 2 | 2 | 50% |

**Sample Controls (Data Subject Rights):**

| # | Requirement | Status | Gap / Action | Effort |
|---|------------|--------|--------------|--------|
| DSR-1 | Right of access (Art. 15) — respond within 30 days | Missing | No automated process to compile all data held about a user. Implement data export from database, Google Analytics, Mailchimp. Build internal tool or use privacy management platform. | 5 days |
| DSR-2 | Right to erasure (Art. 17) — delete on request | Partial | Can delete from main database but not from analytics, backups, or Mailchimp. Map all data stores and implement deletion cascade across all systems. | 4 days |
| DSR-3 | Right to portability (Art. 20) — machine-readable export | Missing | No export functionality. Build JSON/CSV export endpoint for user data. | 3 days |
| DSR-4 | Cookie consent with granular opt-in | Partial | Cookie banner exists but uses pre-ticked boxes (non-compliant). Replace with compliant CMP (e.g., Cookiebot, OneTrust) with granular categories and reject-all option. | 2 days |

## Best Practices

- Start with a single framework and expand — SOC2 Security criteria overlap significantly with HIPAA Technical Safeguards and PCI-DSS, so the first framework provides a foundation.
- Map controls across frameworks to identify shared requirements and avoid duplicating effort on controls that satisfy multiple standards simultaneously.
- Use compliance automation platforms (Vanta, Drata, Secureframe) to continuously collect evidence rather than scrambling before audits.
- Document "Not Applicable" justifications formally — auditors will question every N/A item and require documented rationale.
- Set calendar reminders for recurring controls (quarterly access reviews, annual risk assessments, penetration tests) to avoid lapses between audit periods.
- Treat the checklist as a living document — update status weekly during active remediation and review quarterly once compliant.

## Edge Cases

- **Startups with no existing security program** — Begin with a risk assessment to establish baseline. Many controls can be implemented quickly using cloud-native features (AWS CloudTrail, GitHub branch protection, Google Workspace security settings). Prioritize foundational policies first: information security, acceptable use, incident response.
- **Multi-framework audits** — When pursuing SOC2 + HIPAA + PCI-DSS simultaneously, build a unified control framework that maps each internal control to every applicable requirement across standards. Auditors may accept shared evidence for overlapping controls.
- **Companies using serverless or PaaS architectures** — Many infrastructure controls shift to the cloud provider under the shared responsibility model. Document which controls are inherited (physical security, hypervisor patching) versus which remain the customer's responsibility (application security, access management).
- **Rapid growth or frequent organizational changes** — Controls that depend on employee count or role structure (access reviews, security training completion) need processes that scale. Automate onboarding/offboarding checklists and tie security training to HR onboarding flows.
- **Inherited compliance from acquisitions** — When acquiring a company, their compliance status doesn't transfer automatically. Conduct a compliance gap assessment of the acquired entity and build an integration timeline for bringing them under your compliance umbrella.
