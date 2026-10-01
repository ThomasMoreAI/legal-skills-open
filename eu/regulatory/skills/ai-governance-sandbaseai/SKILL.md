---
name: ai-governance-sandbaseai
title: AI Governance
description: Use when classifying AI-system risk, establishing responsible-AI governance, preparing model or system documentation, assessing human oversight, or mapping controls to frameworks such as the EU AI Act and NIST AI RMF.
author: sandbaseai
author_url: https://github.com/sandbaseai/workbuddy-skill/tree/main/skills/ai-governance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# AI Governance

Use this skill to turn responsible-AI principles and applicable requirements into decisions, controls, and evidence across an AI system’s lifecycle. It produces an engineering governance assessment, not legal advice or a certification. Confirm the current authoritative regulation, jurisdiction, sector obligations, contract, and counsel before making a compliance claim.

Do not deploy a high-impact or externally consequential AI system based only on a model score, vendor statement, or checklist. Do not hide limitations, remove meaningful human review, use sensitive data without a documented purpose, or treat a model card as proof of safe operation.

## Establish the system record

For each use case record:

- provider, model/version, owner, deployer, users, affected people, geography, sector, and lifecycle stage;
- intended purpose, prohibited or foreseeable misuse, decision authority, autonomy, inputs/outputs, downstream actions, and third parties;
- data categories, provenance, consent/purpose, retention, residency, sensitive attributes, labels, and known gaps;
- performance, fairness, privacy, security, reliability, latency, cost, accessibility, and environmental objectives;
- applicable law/policy/framework, risk tier rationale, decision rights, escalation, approval, monitoring, rollback, and retirement criteria.

Maintain an inventory that is versioned and reviewable. Reassess after a model, prompt, retrieval corpus, tool, data, user population, jurisdiction, or decision-impact change.

## Classify risk by impact

Use a documented, evidence-backed classification rather than a product label. Consider whether the system:

- influences access to employment, education, credit, insurance, housing, healthcare, public services, justice, migration, safety, or democratic processes;
- performs biometric, emotion, profiling, surveillance, ranking, recommendation, generation, or autonomous action;
- affects vulnerable people, handles sensitive data, operates at scale, or can cause irreversible physical, financial, legal, or reputational harm;
- is transparent to the affected person and has a practical human appeal or correction path.

Map the result to the applicable framework’s categories (for example prohibited, high-impact, transparency-requiring, or low-risk) and preserve the rationale, evidence, uncertainty, owner, and approval. Do not infer a legal category from a generic risk table without checking the current official text.

## Use the NIST AI RMF lifecycle

```text
GOVERN -> MAP -> MEASURE -> MANAGE
```

- **Govern:** establish policies, accountability, authority, training, incentives, procurement controls, and an exception process.
- **Map:** understand stakeholders, context, intended use, harms, benefits, constraints, dependencies, and affected communities.
- **Measure:** test capability, validity, robustness, security, privacy, fairness, explainability, accessibility, drift, and human factors with representative and adversarial cases.
- **Manage:** prioritize risks, implement mitigations, monitor residual risk, handle incidents, communicate limitations, and decide whether to deploy, restrict, pause, or retire.

Each function needs an owner, evidence, review cadence, and stop condition. Keep observed facts separate from interpretations and governance decisions.

## Lifecycle gates

1. **Intake:** define purpose, affected people, alternatives, risk appetite, prohibited uses, and decision owner.
2. **Design:** complete data-flow, threat, privacy, accessibility, human-oversight, and misuse reviews.
3. **Build/source:** verify model/data/vendor provenance, licenses, dependencies, documentation, and change controls.
4. **Validate:** test representative and edge populations, foreseeable misuse, prompt injection/tool abuse where relevant, calibration, uncertainty, drift sensitivity, and failure recovery.
5. **Approve:** record residual risks, limitations, monitoring, user notice, appeal/correction, rollback, and accountable sign-off.
6. **Operate:** monitor outcomes and incidents, investigate disparities, preserve audit evidence, review changes, and reapprove material updates.
7. **Retire:** revoke access, handle data retention/deletion, communicate the end of service, preserve required records, and verify downstream cleanup.

Do not allow a model to approve its own deployment or risk exception. High-impact decisions require appropriately qualified human oversight with authority, time, information, training, and the ability to override or stop the system. A human rubber stamp is not meaningful oversight.

## Evidence and controls

Maintain, as applicable:

- system description, intended purpose, architecture, model/data lineage, versions, licenses, and change log;
- data governance, quality, representativeness, bias analysis, consent/purpose, retention, and access records;
- evaluation datasets, test protocol, metrics, confidence/uncertainty, subgroup analysis, red-team results, and known limitations;
- human-oversight instructions, user disclosures, explanations, appeal/correction route, and accessibility checks;
- operational logs with privacy minimization, incident records, monitoring thresholds, drift, abuse, cost, and performance;
- vendor due diligence, contracts, subprocessors, security/privacy controls, and an exit or fallback plan.

Avoid retaining prompts, outputs, or identifiers beyond the purpose. Redact secrets and personal data in evaluation artifacts. Make evidence reproducible without exposing protected data.

## Fairness, safety, and transparency review

Define who may be harmed and what “acceptable” means before choosing a metric. Check subgroup coverage, label quality, missingness, unequal error costs, intersectional effects, automation bias, accessibility, language, and distribution shift. No single fairness metric resolves a policy trade-off; document the choice and affected stakeholders.

Tell users when they interact with or are materially affected by AI where required or appropriate. State capabilities, limitations, uncertainty, data use, human review, appeal path, and how to report harm. Do not present generated content or automated decisions as authoritative without verification.

## Incident and exception handling

Define severity, notification path, containment authority, evidence preservation, affected-population analysis, remediation, and reapproval. Stop or restrict the system when there is unsafe drift, discriminatory impact, privacy/security breach, unexplained high-impact failure, missing oversight, or a violated use restriction.

Every exception has a scope, expiry, owner, compensating control, affected people, rationale, and review date. “Accepted risk” requires an accountable decision and does not erase disclosure or legal obligations.

## Handoff report

```markdown
# AI Governance Assessment
## System, purpose, version, jurisdiction, and affected people
## Risk classification and rationale
## Govern / Map / Measure / Manage evidence
## Data, model, vendor, privacy, security, fairness, and accessibility findings
## Human oversight, transparency, appeal, and monitoring
## Decision: approve / restrict / remediate / pause / retire
## Owners, deadlines, residual risk, exceptions, and next review
```

Stop when the purpose, affected population, authority, evidence, or applicable requirement is ambiguous; escalate to the accountable product, risk, privacy, security, and legal owners.
