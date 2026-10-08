---
name: prompt-pack-ai-governance-policy-sboghossian
title: AI Governance Policy
description: Use when drafting an AI governance policy for an organization addressing responsible AI use, risk assessment, bias detection, transparency, human oversight, data handling for AI training, vendor evaluation, and incident response. Covers privacy and data protection practice area across MENA (UAE, KSA, EG) and global jurisdictions, with attention to emerging AI-specific regulatory frameworks.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-ai-governance-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# AI Governance Policy

## When to use this

Use this skill when an organization needs a formal AI governance policy to:
- Establish principles and rules for responsible AI use by employees and systems
- Comply with emerging AI regulations and data protection laws that apply to automated processing
- Satisfy investor, customer, or regulatory due diligence requirements
- Manage risk from AI-related harms (bias, discrimination, privacy violations, safety incidents)

Triggers: regulator inquiry, data protection audit, board request, procurement requirement, investor due diligence, or proactive compliance posture.

---

## Prompt template

> Draft an AI governance policy for [organization] that addresses responsible AI use, risk assessment framework, bias detection and mitigation, transparency requirements, human oversight mechanisms, data handling for AI training, vendor evaluation criteria, and incident response procedures.

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Organization name and type | Regulatory requirements differ (financial institution vs. hospital vs. tech company) |
| Jurisdictions of operation | Determines which AI regulations and data protection laws apply |
| AI use cases in scope | Policy must be calibrated to actual risk — a chatbot has different risk than a credit-scoring model |
| Regulatory context | Is this for DIFC PDPL compliance? UAE AI Strategy? EU AI Act (for EU operations)? |

---

## Document structure

### 1. Purpose and scope
- Organization's commitment to responsible AI
- Definition of AI systems in scope (narrow: ML models producing decisions or outputs affecting individuals; broader: any automated processing tool)
- Who the policy applies to (employees, contractors, vendors)
- Relationship to other policies (data protection policy, acceptable use policy, vendor management policy)

### 2. AI risk classification framework
A tiered framework adapted to the organization's context:

| Risk tier | Criteria | Governance requirements |
|-----------|---------|------------------------|
| High risk | Decisions affecting individual rights, safety, access to services, employment, credit, healthcare | Mandatory human review; DPIA/AI impact assessment; formal approval before deployment |
| Medium risk | Significant business decisions; processing of personal data at scale | Impact assessment; documented testing; periodic review |
| Low risk | Content generation, internal productivity tools, no individual-facing decisions | Acceptable use guidelines; standard data handling |

For organizations with EU operations, map to EU AI Act risk categories (unacceptable / high / limited / minimal).

### 3. Responsible AI principles
State the organization's principles. Standard set:
- **Fairness**: AI systems must not produce discriminatory outputs based on protected characteristics
- **Transparency**: decisions made with AI assistance must be explainable to affected individuals on request
- **Privacy**: AI systems must comply with applicable data protection law; data minimization applies
- **Accountability**: every AI system must have a named owner responsible for governance
- **Safety**: AI systems must be tested before deployment; ongoing monitoring required
- **Human oversight**: high-risk AI decisions require human review before acting

### 4. Bias detection and mitigation
- Define "bias" in the organization's context (statistical bias, disparate impact, representational bias)
- Testing requirements before deployment: what tests are required, who conducts them, what threshold triggers remediation
- Ongoing monitoring: frequency; metrics to track; who reviews
- Remediation process: what happens when bias is detected post-deployment
- Training data governance: documentation of data sources, known limitations, exclusions

### 5. Transparency and explainability
- Individual rights: if an AI system makes or substantially informs a consequential decision about an individual, that individual has the right to explanation and to human review (required under GDPR Art. 22, UAE PDPL, DIFC Data Protection Law)
- Internal transparency: document what AI systems exist, what they do, and what data they use
- External transparency: disclosure obligations in terms of service or privacy notice

### 6. Human oversight mechanisms
- Define which decisions require human sign-off before acting on AI output
- Escalation path for borderline cases
- "Human in the loop" vs. "Human on the loop" distinction and when each applies
- Override rights: any individual affected by an AI decision has the right to request human review (mandatory in most data protection regimes)

### 7. Data handling for AI training
- Principles: purpose limitation (data collected for X may not be used to train AI without separate legal basis); data minimization; consent or legitimate interest assessment
- Training data sourcing: approved sources; prohibited categories (personal data of children; sensitive categories without explicit consent)
- Data retention for training sets: how long; deletion on model retirement
- Documentation: maintain a training data register

### 8. AI vendor evaluation criteria
Before procuring an AI system from a vendor:
- Does the vendor disclose training data sources and known limitations?
- What bias testing has the vendor conducted?
- What data does the vendor process and where is it stored? (Data residency requirements in UAE, KSA, EG)
- What is the vendor's incident response obligation?
- Does the vendor's AI use comply with applicable regulation?
- Contractual requirements: AI use restrictions, data processing agreement (DPA), audit rights, incident notification timelines

### 9. Incident response
- Definition of an AI incident: unauthorized output, harmful decision, bias event, data breach involving AI system, system failure
- Notification: who must be notified internally; regulatory notification requirements (UAE PDPL: 72-hour notification for data breaches; DIFC Data Protection Law: similar; GDPR: 72 hours)
- Containment: immediate steps to limit harm
- Investigation: root cause; was the incident foreseeable and preventable?
- Remediation: fix; affected individual notification; record
- Learning: post-incident review; policy update if required

### 10. Governance and accountability
- AI Governance Committee (or equivalent): composition; meeting frequency; mandate
- AI system owner responsibilities
- Annual policy review obligation
- Employee training requirements
- Non-compliance consequences

---

## Jurisdictional notes

### UAE
UAE Federal Decree-Law 45/2021 on Personal Data Protection applies to automated processing. No dedicated AI Act as of mid-2026, but the UAE AI Strategy 2031 sets national direction. Financial services AI governed by CBUAE and FSRA guidance. Healthcare AI: MOH guidance applies.

### KSA
Saudi PDPL (Personal Data Protection Law, Royal Decree M/19/2021) applies to automated decisions. SDAIA (Saudi Data and Artificial Intelligence Authority) is developing AI governance frameworks. Financial services: SAMA fintech frameworks apply to AI.

### DIFC
DIFC Data Protection Law (DIFC Law No. 5 of 2020) includes automated processing provisions aligned with GDPR. DFSA has issued guidance on algorithmic systems in financial services.

### EU (if operations or EU data subjects)
EU AI Act (Regulation 2024/1689) applies: mandatory risk classification, conformity assessments for high-risk AI, prohibited AI practices. Coordinate with EU AI Act timeline (phased implementation 2024–2027).

---

## Common mistakes

- Scope too broad: a policy covering "all software" is unmanageable; define AI systems precisely
- No accountability chain: policy states principles without naming who is responsible
- Missing vendor provisions: many AI risks enter through third-party tools
- Training data treated as anonymous: aggregated personal data is often still personal data; document the legal basis
- No update mechanism: AI regulation is evolving rapidly; include an annual review obligation

---

## Related skills

- [[prompt-pack-ai-system-data-governance-framework]] — the broader data governance framework for AI/ML systems
- [[kb-data-protection-mena]] — data protection law reference for MENA jurisdictions
- [[draft-privacy-policy]] — privacy policy that must be aligned with AI governance policy
- [[heuristic-always-state-jurisdiction-first]] — jurisdiction-first drafting rule
