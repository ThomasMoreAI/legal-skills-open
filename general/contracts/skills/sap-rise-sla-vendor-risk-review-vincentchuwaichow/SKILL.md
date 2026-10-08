---
name: sap-rise-sla-vendor-risk-review-vincentchuwaichow
title: RISE with SAP SLA and Vendor Risk Review
description: 'Advisory review of RISE with SAP and SAP cloud service contracts for SLA and vendor risk: responsibility split between SAP, customer, and partner; SLA tiers and credit mechanisms; availability and DR commitments; data residency; exit and portability obligations; shared security responsibilities; and audit rights. Does not touch or mutate any live system.'
author: VincentChuWaiChow
author_url: https://github.com/VincentChuWaiChow/vanguard-frontier-agentic/tree/master/skills/sap/sap-rise-sla-vendor-risk-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
sources:
- title: Official Sources
  path: references/official-sources.md
- title: Safety Checklist
  path: references/safety-checklist.md
- title: Workflow And Output
  path: references/workflow-and-output.md
---

# RISE with SAP SLA and Vendor Risk Review

## Purpose

Assess the vendor risk and SLA posture of a RISE with SAP engagement or SAP cloud service agreement. Evaluate the contractual responsibility split between SAP, the customer, and the system integrator or partner; SLA tier definitions and credit mechanisms; system availability and disaster recovery commitments; data residency and cross-border transfer obligations; exit and data portability clauses; the shared responsibility model for security; and audit and compliance rights. Surface contractual gaps, ambiguous responsibility boundaries, weak SLA credit structures, and missing exit provisions that represent vendor lock-in or compliance risk. Does not connect to or mutate any live system, contract management platform, or SAP environment.

## When to use

Use this skill when the user asks to:

- review a RISE with SAP contract or cloud service agreement for SLA gaps, vendor risk, or responsibility ambiguity,
- assess the contractual responsibility split between SAP, the customer, and the implementation partner across infrastructure, application, and data layers,
- evaluate SLA tier definitions, availability commitments, and credit mechanisms for adequacy against business continuity requirements,
- review disaster recovery and business continuity commitments in a RISE with SAP or SAP cloud service agreement,
- assess data residency clauses and cross-border data transfer obligations in an SAP cloud contract,
- review exit and data portability provisions in a RISE with SAP agreement to understand vendor lock-in risk,
- evaluate the shared security responsibility model between SAP and the customer for a RISE with SAP or SAP BTP engagement,
- assess audit rights and third-party certification commitments (ISO 27001, SOC 2, etc.) in an SAP cloud service agreement,
- prepare for contract renegotiation, renewal, or escalation with SAP,
- support a compliance or legal review of SAP cloud obligations.

## When not to use

- When the request requires live access to the SAP contract management portal or a specific signed contract document — this skill accepts only user-provided contract excerpts, term summaries, or written descriptions.
- When the request concerns SAP BTP account model governance — use `sap-btp-governance-review`.
- When the request concerns SAP licensing cost optimization or BTP consumption FinOps — use `sap-license-btp-consumption-finops-review`.
- When the request concerns the technical transformation program structure — use `sap-transformation-portfolio-triage-review`.
- When the request requires legal advice on contract terms — this skill provides advisory risk classification, not legal counsel.

## Does not touch live systems

This skill operates on user-provided contract excerpts, term summaries, SAP Trust Center publications, SAP cloud service descriptions, or written descriptions of contractual obligations. It does not connect to any SAP system, SAP contract management portal, SAP for Me, or any live environment. All live inspection is out of scope.

## Lean operating rules

- Classify responsibility before assessing risk. Every SLA or security finding must be classified by responsibility layer (SAP-managed / customer-managed / partner-managed / shared) before a risk level is assigned.
- Use SAP's published shared responsibility model as the baseline. SAP publishes responsibility matrices for RISE with SAP and SAP BTP that define what SAP manages and what the customer manages at infrastructure, platform, application, and data layers. Deviations from this baseline in the user's contract are risk findings.
- SLA credit mechanisms must be evaluated against recovery time objectives. An SLA credit that compensates financially but does not include service restoration guarantees does not address business continuity risk.
- Data residency obligations must map to actual processing locations. A contractual data residency clause is only as strong as the accompanying technical controls and audit evidence. Flag clauses where residency is stated but audit rights to verify it are absent.
- Exit and portability provisions must specify format, timeline, and cost. A portability clause that does not specify the data export format, the export timeline, and whether export is at SAP's cost or the customer's cost is not an effective exit provision.
- Audit rights must be specific. A generic audit rights clause without specifying the audit mechanism (customer right to audit, third-party certification, or SAP-provided audit report) does not provide meaningful assurance.
- Do not conflate RISE with SAP scope with SAP S/4HANA Public Cloud scope. RISE with SAP is a commercial bundling model; the underlying technical scope depends on whether the customer is on S/4HANA Private Cloud Edition or S/4HANA Cloud Public Edition. The responsibility split differs significantly between these two.
- Evidence from user-provided contract text or SAP Trust Center publications takes precedence over inference.
- Load only the reference needed for the contract domain under review.

## Evidence rules

Label all claims with one of:

- `documentation-based` — grounded in SAP Trust Center publications, SAP cloud service descriptions, SAP shared responsibility documentation, or official SAP contractual framework documentation
- `user-provided evidence` — contract excerpts, term summaries, SLA schedules, or written descriptions of contractual obligations provided by the user
- `inference` — derived reasoning not directly confirmed by official SAP publications or user-provided contract text

## Live-environment rules

**This skill does not touch live systems.** There is no API call, contract management portal access, SAP system connection, SAP for Me login, or any live environment access in this skill's execution path. Users must supply contract excerpts, SAP Trust Center documentation references, SLA schedules, or written descriptions of their RISE with SAP or SAP cloud service obligations for this skill to review.

## References

Load only when needed:

- [Workflow and output contract](references/workflow-and-output.md) — responsibility layer taxonomy, risk severity classification, SLA and vendor risk assessment criteria, output format.
- [Safety checklist](references/safety-checklist.md) — non-negotiables, common contract review mistakes, when to push back.
- [Official sources](references/official-sources.md) — SAP Trust Center, RISE with SAP shared responsibility documentation, SAP cloud service descriptions, data processing agreements.

## Response minimum

Return, at minimum:

- **Problem classification**: contract domain(s) affected (responsibility split / SLA and credits / availability and DR / data residency / exit and portability / security responsibilities / audit rights) and specific finding(s).
- **Evidence used**: documentation-based / user-provided evidence / inference.
- **Risk level**: critical (contractual gap creating unmanaged compliance, regulatory, or business continuity exposure) / high (ambiguous responsibility boundary or weak SLA credit mechanism with material business impact) / medium (missing provision that is negotiable but currently absent) / low (best practice deviation in contract structure or language).
- **Recommended action**: specific contractual or operational remediation per finding (renegotiate clause, request SLA schedule addendum, obtain SAP Trust Center certification evidence, implement compensating control, clarify responsibility matrix).
- **Refusal / escalation triggers**: if legal interpretation of contract terms is required, state that this skill provides risk classification only and that legal counsel must be engaged. If access to the signed contract is required, state that and request the user provide the relevant excerpts.
- **Business impact**: regulatory non-compliance risk, business continuity exposure, vendor lock-in risk, or audit finding risk.
- **Next verification step**: validate responsibility and SLA findings against the signed contract schedule and current SAP Trust Center publications before escalating.
