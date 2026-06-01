---
name: soc2-programme-manager
title: soc2-programme-manager
description: This skill manages the SOC 2 certification programme including control design, evidence collection, and auditor coordination. Use when asked to prepare for SOC 2, design SOC 2 controls, or manage the audit process. Also consider when enterprise customers require SOC 2 compliance as a procurement condition. Suggest when the user pursues enterprise sales without SOC 2 readiness.
author: mittuled
author_url: https://github.com/mittuled/skill-os/tree/main/agents/legal/security-compliance-programme-manager/soc2-programme-manager
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# soc2-programme-manager

## Agent: Security & Compliance Programme Manager

L2 security and compliance programme manager (1x) responsible for SOC 2, security awareness training, disaster recovery, GDPR/CCPA compliance, and penetration test programme management.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Manages the end-to-end SOC 2 certification programme including Trust Services Criteria scoping, control design, evidence collection, gap remediation, auditor selection and coordination, and ongoing compliance monitoring.

## When to Use

- When the company decides to pursue SOC 2 Type I or Type II certification to satisfy enterprise customer requirements, investor expectations, or internal security maturity goals.
- When the SOC 2 audit observation period is approaching and controls, evidence collection, and auditor coordination must be managed through the engagement.
- When a SOC 2 report has been issued with exceptions or qualified opinions that require remediation and re-audit.

## Workflow

1. **Scope and Criteria Selection**: Determine the SOC 2 report type (Type I for point-in-time, Type II for observation period) and select applicable Trust Services Criteria: Security (required), Availability, Processing Integrity, Confidentiality, and Privacy. Define the system boundaries, infrastructure components, and third-party services in scope. Deliverable: SOC 2 scope document with system description and criteria selection rationale.
2. **Control Design and Mapping**: Design controls that satisfy each in-scope Trust Services Criterion. Map controls to the COSO framework and existing security policies. Common control areas include access management, change management, incident response, risk assessment, vendor management, encryption, logging and monitoring, and business continuity. Deliverable: control matrix mapping each control to its criterion, control owner, frequency, and evidence type.
3. **Gap Assessment and Remediation**: Assess current practices against each designed control. Identify gaps where controls are missing, undocumented, or not operating effectively. Prioritize remediation by audit timeline and effort. Deliverable: gap assessment report with remediation plan, owners, and deadlines.
4. **Evidence Collection System**: Establish continuous evidence collection for each control. Automate where possible (access review screenshots, change management ticket exports, security scan results, training completion reports). Define manual evidence collection procedures with responsible parties and collection cadence. Deliverable: evidence collection playbook with automation configurations and manual procedures.
5. **Auditor Selection and Engagement**: Select a qualified CPA firm with SOC 2 experience. Negotiate the engagement letter covering scope, timeline, fees, and deliverables. Conduct the readiness assessment with the auditor to identify any remaining gaps before the formal audit begins. Deliverable: executed audit engagement letter and readiness assessment findings.
6. **Audit Execution**: Manage the audit process including evidence submission, auditor inquiry responses, walkthroughs, and exception management. Coordinate with control owners to respond to auditor requests within agreed timelines. Track and resolve any exceptions or deviations identified during testing. Deliverable: audit coordination tracker with request status, exception log, and management responses.
7. **Report Review and Ongoing Monitoring**: Review the draft SOC 2 report for accuracy. Address any qualified opinions or exceptions through management responses and remediation commitments. Establish continuous monitoring to maintain control effectiveness throughout the year, not just during audit periods. Deliverable: final SOC 2 report, management response to exceptions, and continuous monitoring programme.

## Anti-Patterns

- **Audit-season compliance**: Implementing controls and collecting evidence only during the audit observation period rather than maintaining continuous compliance. *Why*: SOC 2 Type II evaluates operating effectiveness over a period; controls that are only active during audit season will be identified as exceptions by competent auditors.
- **Over-scoping Trust Services Criteria**: Including all five criteria when only Security is required by customers, creating unnecessary control burden. *Why*: each additional criterion requires additional controls, evidence, and auditor testing time; scope should be driven by customer requirements and business needs, not aspirational compliance.
- **Treating SOC 2 as a security programme**: Using SOC 2 controls as the entire security programme rather than mapping SOC 2 to a broader security framework. *Why*: SOC 2 is an attestation framework, not a security programme; controls designed solely to pass the audit may miss material security risks not covered by Trust Services Criteria.
- **Manual evidence collection at scale**: Relying on manual screenshots and spreadsheets for evidence collection as the control count grows. *Why*: manual collection is error-prone, time-consuming, and does not scale; automation platforms reduce the evidence collection burden and improve consistency.

## Output

**On success**: Produces the complete SOC 2 programme package containing the scope document, control matrix, gap assessment, evidence collection playbook, auditor engagement materials, audit coordination tracker, final SOC 2 report, and continuous monitoring programme. Delivered to security leadership, executive team, sales (for customer distribution), and compliance records.

**On failure**: Report which programme components are incomplete (e.g., unresolved control gaps, pending auditor selection, evidence collection not automated), what the current audit readiness level is, and what must be completed before the audit can proceed with projected timeline.

## Related Skills

- [`gdpr-ccpa-compliance-manager`](../gdpr-ccpa-compliance-manager/SKILL.md) -- SOC 2 Privacy criteria overlap with GDPR/CCPA requirements; coordinating both programmes reduces duplicate controls and evidence collection.
- [`penetration-test-programme-manager`](../penetration-test-programme-manager/SKILL.md) -- Penetration test results are key SOC 2 audit evidence for security control effectiveness.
