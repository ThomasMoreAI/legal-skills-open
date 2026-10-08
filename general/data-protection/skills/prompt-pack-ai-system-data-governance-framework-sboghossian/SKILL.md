---
name: prompt-pack-ai-system-data-governance-framework-sboghossian
title: AI System Data Governance Framework
description: Use when drafting a data governance framework specifically for an organization's AI and machine learning systems, addressing training data requirements, bias mitigation, data minimization, purpose limitation, transparency obligations, individual rights in automated decision-making, and compliance with emerging AI regulations. Covers privacy and data protection across MENA and global jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-ai-system-data-governance-framework
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# AI System Data Governance Framework

## When to use this

Use this skill when an organization needs a **data governance framework** specifically scoped to its AI/ML systems. This is a more technical and data-architecture-focused document than an AI Governance Policy — it addresses the data lifecycle for AI: how training data is sourced, curated, stored, used, and retired.

The distinction:
- **AI Governance Policy** ([[prompt-pack-ai-governance-policy]]): principles, oversight, accountability, incident response — the "what we believe and who is responsible"
- **AI System Data Governance Framework** (this skill): data sourcing, bias testing, data minimization, rights management, regulatory compliance — the "how we handle data throughout the AI lifecycle"

Triggers: data protection audit, AI deployment review, regulatory examination, investor due diligence on AI/ML pipeline.

---

## Prompt template

> Draft a data governance framework for [Company's] AI/ML systems addressing training data requirements, bias mitigation, data minimization, purpose limitation, transparency obligations, individual rights in automated decision-making, and compliance with emerging AI regulations.

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Company name and type | Sector-specific requirements (financial services, healthcare, HR tech have heightened obligations) |
| AI/ML use cases | The framework must be calibrated to the actual data flows and decision types |
| Jurisdictions of operation | Determines applicable data protection and AI regulations |
| Existing data governance infrastructure | Framework should build on, not duplicate, existing policies |

---

## Document structure

### 1. Framework scope and objectives
- Define which AI/ML systems are in scope (production models; experimental models; third-party AI tools used in production; models under development)
- Define "personal data processed by AI systems" — includes training data, inference inputs, outputs that are used to make decisions about individuals
- State compliance objectives: data protection law compliance; bias risk management; explainability; audit readiness

### 2. Training data governance

#### 2.1 Sourcing requirements
- Approved data sources: first-party data (collected with appropriate consent or legitimate interest); licensed third-party datasets; synthetic data; open datasets with reviewed licensing
- Prohibited sources: unlicensed web scraping of personal data; data obtained without legal basis; data subject to country-specific transfer restrictions (UAE: data localization requirements in certain sectors; KSA: PDPL cross-border transfer rules; EG: PDL transfer restrictions)
- Source documentation: every training dataset must have a "data card" recording source, collection date, legal basis, known biases, and limitations

#### 2.2 Data minimization
- Training data must be limited to what is necessary for the stated model purpose (purpose limitation under GDPR Art. 5, UAE PDPL, DIFC Data Protection Law)
- Sensitive categories require explicit consent or alternative statutory grounds: health data, biometric data, financial data, religious/political belief data (if relevant to model)
- Pseudonymization and anonymization: where possible, training data should be pseudonymized; truly anonymized data falls outside data protection law scope (note: re-identification risk must be assessed)

#### 2.3 Data quality requirements
- Completeness: is the dataset representative of the population the model will serve? Under-representation creates bias
- Accuracy: what is the error rate in labels? What is the process for error correction?
- Timeliness: how old is the data? Is it still representative?
- Documentation: data quality assessments must be documented and retained

### 3. Bias mitigation

#### 3.1 Pre-training assessment
Before training any model that makes or informs consequential decisions about individuals:
- Identify sensitive attributes relevant to the use case (gender, nationality, age, disability status, religion — these are protected characteristics under most jurisdictions' anti-discrimination law)
- Assess whether training data contains proxy variables for sensitive attributes (postcode as a proxy for ethnicity, for example)
- Define fairness metrics appropriate to the use case (demographic parity, equalized odds, etc.)

#### 3.2 Testing protocol
- Disaggregated performance testing: model performance must be measured separately for each demographic group, not only in aggregate
- Bias test threshold: define the maximum acceptable performance gap between groups before deployment is blocked
- Red-teaming: adversarial testing for harmful outputs, particularly for generative AI systems

#### 3.3 Post-deployment monitoring
- Ongoing output monitoring for drift and emerging bias
- Frequency: at minimum quarterly for high-risk models; annually for low-risk
- Escalation: what triggers an immediate review (e.g., a user complaint, a regulatory inquiry, a media report)

### 4. Purpose limitation and data minimization at inference

- Data collected during model inference (inputs) must be used only for the stated purpose
- Retention of inference inputs and outputs: define retention period per use case; default to minimum necessary
- Secondary use of inference data (e.g., using user queries to a chatbot to further train the model): requires legal basis analysis; user notification; in many cases, opt-in consent
- Profiling: automated profiling of individuals based on AI outputs requires DPIA and, in many jurisdictions, a specific legal basis

### 5. Transparency obligations

#### 5.1 Internal transparency — model documentation
Every production model must have a "model card" recording:
- Purpose and intended use
- Training data sources and known limitations
- Performance metrics including disaggregated results
- Known failure modes and edge cases
- Human oversight requirements
- Responsible owner

#### 5.2 External transparency — individual notification
Individuals whose data is used in AI training or who are subject to AI-assisted decisions must be informed:
- In the privacy notice: what AI systems exist; what decisions they inform; whether human review is available
- At point of automated decision: notification that an automated process was used and how to request human review

### 6. Individual rights in automated decision-making

Per applicable data protection law:
- **Right to explanation**: individuals have the right to an explanation of any automated decision that significantly affects them (GDPR Art. 22; UAE PDPL Art. 30; DIFC Data Protection Law s. 22)
- **Right to human review**: individuals may request human review of automated decisions
- **Right to object**: individuals may object to processing their data for automated profiling

Framework obligations:
- Implement a process to receive and respond to these rights requests within statutory timeframes (UAE PDPL: 5 business days; GDPR: one month)
- Maintain records of automated decisions sufficient to support explanation requests
- Train customer-facing staff on how to handle these requests

### 7. Regulatory compliance mapping

| Regulation | Key requirements for AI data governance |
|-----------|----------------------------------------|
| UAE Federal Decree-Law 45/2021 (PDPL) | Automated decision-making disclosure; cross-border transfer rules; data residency in some sectors |
| Saudi PDPL (2021) | Consent for automated processing affecting individuals; data localization |
| DIFC Data Protection Law (2020) | GDPR-aligned; automated decision-making rights; DPO appointment requirements |
| ADGM Data Protection Regulations (2021) | Similar to DIFC |
| EU AI Act (2024) | Risk classification; conformity assessment for high-risk AI; prohibited AI practices |
| GDPR | Art. 22 automated decision-making; Art. 25 privacy by design; DPIA for high-risk processing |

### 8. Model retirement and data deletion
- When a model is retired, document the retirement decision and date
- Training data used exclusively for that model: delete per retention schedule
- Model weights: archive for the statutory limitation period to support any future claims or investigations, then delete
- Inference logs: delete per retention schedule documented in the model card

---

## Jurisdictional notes on cross-border data transfers for AI training

Several MENA jurisdictions impose data localization or transfer restrictions that directly affect AI training data pipelines:

- **UAE**: certain sectors (financial services, healthcare, government) have data residency requirements; general PDPL requires "adequate protection" in destination country for transfers
- **KSA**: PDPL requires data about Saudi residents to be processed within the Kingdom for sensitive categories; transfer outside requires consent or adequate-protection finding
- **Egypt**: PDL (Law 151/2020) restricts cross-border transfer of personal data; licensing required for cross-border processing in some cases

Cloud-based AI training that transfers data to servers in non-MENA jurisdictions must be assessed against these rules.

---

## Common mistakes

- No distinction between training data governance and inference data governance — they have different risk profiles and different regulatory treatment
- Assuming anonymized training data has zero regulatory risk — re-identification risk means this assumption must be tested
- No model card or data card documentation — creates audit and explainability gaps
- Rights request process not operationalized — having a right in a policy that no one knows how to execute is non-compliance
- Framework not updated when new AI use cases are deployed — annual review and change-triggered reviews are essential

---

## Related skills

- [[prompt-pack-ai-governance-policy]] — the companion governance policy (principles, oversight, accountability)
- [[kb-data-protection-mena]] — MENA data protection law reference
- [[draft-privacy-policy]] — privacy notice obligations that must reference AI processing
- [[heuristic-always-state-jurisdiction-first]] — jurisdiction-first drafting
