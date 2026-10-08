# Kevin — Legal Workflow Engine

> **v1.0** | March 2026 | Companion to `SKILL.md`
>
> *Ten structured workflows. Each one takes messy startup reality as input and produces legally sound, audit-ready output.*

---

## How to Use This Document

Each workflow follows an identical structure so Kevin (and the humans using Kevin) can execute them repeatably:

| Section | Purpose |
|---|---|
| **Trigger** | When to initiate this workflow |
| **Input** | Exactly what information Kevin needs to begin |
| **Legal Framework** | The laws, regulations, and principles governing this workflow |
| **Process** | Step-by-step execution with decision gates |
| **Output** | The specific deliverable(s) produced |
| **Validation Criteria** | How to verify the output is legally sound |
| **Escalation Triggers** | When to stop and involve human legal counsel |

**Severity tags** used throughout: `LOW` `MEDIUM` `HIGH` `CRITICAL`

---

## Table of Contents

1. [AI Vendor Contract Review & Redlining](#workflow-1-ai-vendor-contract-review--redlining)
2. [AI Risk Classification & EU AI Act Compliance Assessment](#workflow-2-ai-risk-classification--eu-ai-act-compliance-assessment)
3. [Data Processing Addendum (DPA) Drafting for AI Systems](#workflow-3-data-processing-addendum-dpa-drafting-for-ai-systems)
4. [Internal AI Acceptable Use Policy Creation](#workflow-4-internal-ai-acceptable-use-policy-creation)
5. [AI Product Privacy Notice Generation](#workflow-5-ai-product-privacy-notice-generation)
6. [AI Threat Model Assessment](#workflow-6-ai-threat-model-assessment)
7. [Enterprise Customer AI Due Diligence Response](#workflow-7-enterprise-customer-ai-due-diligence-response)
8. [AI Intellectual Property Audit](#workflow-8-ai-intellectual-property-audit)
9. [AI Incident Response & Breach Notification](#workflow-9-ai-incident-response--breach-notification)
10. [AI Regulatory Change Impact Analysis](#workflow-10-ai-regulatory-change-impact-analysis)

---

## Workflow 1: AI Vendor Contract Review & Redlining

### Trigger

The startup is about to sign a contract with a vendor that provides, uses, or integrates AI in any part of their service delivery. This includes SaaS tools with AI features, LLM API providers, AI-powered analytics platforms, and outsourced services where the vendor may use AI.

### Input

| Required Input | Format | Source |
|---|---|---|
| Vendor contract / MSA / Order Form | PDF, DOCX, or plain text | Vendor |
| Any existing AI addendum or DPA from vendor | PDF, DOCX | Vendor |
| Description of vendor's AI usage (if known) | Free text | Sales/procurement team |
| Company's standard AI addendum template | DOCX | Legal / SKILL.md Section 4 |
| Categories of company data the vendor will access | List | Engineering / product team |
| Jurisdictions where services will be delivered | List | Operations |

### Legal Framework

| Law / Principle | Application |
|---|---|
| **EU AI Act (Reg. 2024/1689)** | Art. 5 (prohibited systems), Art. 6 (high-risk classification), Art. 25-27 (obligations on deployers), Art. 50 (transparency obligations) |
| **GDPR** | Art. 28 (processor obligations), Art. 32 (security), Art. 35 (DPIA), Art. 44-49 (international transfers) |
| **CCPA/CPRA** | §1798.100-199 (service provider obligations, data processing restrictions) |
| **CAIA (Colorado)** | §6-1-1701 et seq. (developer/deployer obligations, algorithmic discrimination) |
| **ACC Eight Principles** | Contract due diligence framework (see SKILL.md Section 4.1) |
| **NIST AI RMF 1.0** | GOVERN, MAP, MEASURE, MANAGE functions for vendor risk assessment |

### Process

**STEP 1 — Document Intake & Classification** `[5 min]`

1.1. Ingest all provided documents.

1.2. Classify the contract type:
- (A) Vendor provides an AI system for the startup's direct use (SaaS/license)
- (B) Vendor uses AI internally to deliver services to the startup
- (C) Both A and B
- (D) No AI involvement detected → flag for confirmation with procurement

1.3. Classify data sensitivity:
- Tier 1: No personal data, no confidential data → `LOW`
- Tier 2: Business-confidential data, no personal data → `MEDIUM`
- Tier 3: Personal data (non-sensitive) → `HIGH`
- Tier 4: Sensitive personal data, financial data, health data → `CRITICAL`

**STEP 2 — AI Term Gap Analysis** `[15 min]`

Scan the contract against the following mandatory elements. For each, score as PRESENT (adequate), WEAK (exists but insufficient), or MISSING:

| # | Element | Legal Basis | Minimum Standard |
|---|---|---|---|
| 2.1 | AI definition clause | EU AI Act Art. 3(1) | Definition of "AI System" covering autonomous operation, system-generated outputs, inference from data |
| 2.2 | Prior written approval requirement | ACC Principle 1 | General prohibition on AI use without explicit written approval per use case |
| 2.3 | AI use case description | ACC Principle 2 | Vendor must describe specific AI uses, models used, data flows |
| 2.4 | Vendor documentation obligation | ACC Principle 3; EU AI Act Art. 13 | Documentation of data processing, decision paths, human oversight, override conditions |
| 2.5 | Compliance representations | ACC Principle 4; EU AI Act Art. 16-22 | Vendor warrants compliance with all applicable AI Laws; confirms not prohibited/high-risk (or full disclosure if so) |
| 2.6 | Sub-processor / sub-contractor flow-down | ACC Principle 5; GDPR Art. 28(4) | Sub-processors bound by substantially similar AI terms; prior approval required |
| 2.7 | Data use limitations | GDPR Art. 5(1)(b); CCPA §1798.140(ag) | No use of company data for model training, improvement, or third-party benefit |
| 2.8 | Input/Output IP ownership | ACC Principle 7 | All IP in Inputs, Outputs, and derivative models accrues to the startup |
| 2.9 | Data segregation & encryption | NIST AI RMF; GDPR Art. 32 | Logical segmentation, unique encryption keys, no commingling |
| 2.10 | AI-specific indemnification | ACC Principle 7 | Indemnity for IP infringement of outputs, breach of AI terms, law violations, incorrect outputs |
| 2.11 | Model Drift monitoring | Industry standard | Continuous monitoring; 72-hour notification of drift; right to object |
| 2.12 | Security breach notification | GDPR Art. 33; NIST | 24-hour notification for AI security events (adversarial attacks, data poisoning, prompt injection, leakage) |
| 2.13 | Audit rights | ACC Principle 7; GDPR Art. 28(3)(h) | Right to audit AI system, model, governance framework |
| 2.14 | Bias & discrimination protections | EU AI Act Art. 10; CAIA §6-1-1702 | Free from bias; human oversight for consequential decisions |
| 2.15 | Data subject rights compliance | GDPR Art. 12-22; CCPA §1798.100-125 | Access, correction, deletion, opt-out support for AI-processed data |
| 2.16 | Prohibited/High-Risk system disclosure | EU AI Act Art. 5-6 | Representation that AI is not prohibited; 72-hour notification + termination right if discovered |
| 2.17 | Termination rights | ACC Principle 7 | Termination without penalty for material AI compliance failures |
| 2.18 | Conformity Assessment evidence | EU AI Act Art. 43 | For high-risk systems: CE marking, EU database registration, conformity documentation |

**STEP 3 — Risk Scoring** `[5 min]`

3.1. Count MISSING and WEAK elements from Step 2.

3.2. Apply risk multiplier based on data sensitivity tier from Step 1.3:

| Gap Count | Tier 1 (LOW) | Tier 2 (MED) | Tier 3 (HIGH) | Tier 4 (CRIT) |
|---|---|---|---|---|
| 0-2 gaps | LOW | MEDIUM | MEDIUM | HIGH |
| 3-5 gaps | MEDIUM | HIGH | HIGH | CRITICAL |
| 6-9 gaps | HIGH | HIGH | CRITICAL | CRITICAL |
| 10+ gaps | CRITICAL | CRITICAL | CRITICAL | CRITICAL |

3.3. Assign overall contract risk score.

**STEP 4 — Redline Generation** `[20 min]`

4.1. For each MISSING element: draft the complete clause using model language from SKILL.md Section 4. Mark as `[INSERTION — Kevin]`.

4.2. For each WEAK element: draft replacement language strengthening the provision. Mark as `[REVISION — Kevin]` with tracked changes showing original vs. proposed.

4.3. For each PRESENT element: confirm adequacy. If any language conflicts with applicable law, flag as `[CONFLICT — Kevin]`.

4.4. Apply jurisdiction-specific requirements:
- If EU market: ensure full EU AI Act alignment
- If Colorado: ensure CAIA compliance
- If California: ensure CCPA/CPRA service provider provisions
- If international transfers: ensure SCC or equivalent mechanisms

**STEP 5 — Negotiation Strategy Memo** `[10 min]`

5.1. Rank all redlines by priority: MUST-HAVE, SHOULD-HAVE, NICE-TO-HAVE.

5.2. For each MUST-HAVE, provide:
- The business and legal rationale
- The consequence of not obtaining this term
- A fallback position if the vendor pushes back

5.3. Identify any deal-breakers (elements that, if rejected, should halt the deal).

### Output

| Deliverable | Format | Description |
|---|---|---|
| **Redlined Contract** | DOCX with tracked changes | The vendor contract with all insertions, revisions, and conflict flags marked |
| **Gap Analysis Summary** | Table | The 18-element scorecard from Step 2 with PRESENT / WEAK / MISSING ratings |
| **Risk Score** | Single rating + rationale | Overall risk rating with explanation |
| **Negotiation Strategy Memo** | Structured memo | Prioritized redlines with rationale, consequences, and fallback positions |
| **AI Addendum** (if needed) | DOCX | Complete standalone AI addendum if the base contract has no AI terms |

### Validation Criteria

- [ ] Every MISSING element from the 18-point checklist has a drafted clause
- [ ] All drafted clauses cite to specific legal authority (statute article, regulation section)
- [ ] IP ownership unambiguously vests in the startup
- [ ] Data training prohibition is explicit, not implied
- [ ] Indemnification covers all four AI-specific scenarios (IP infringement, breach, law violation, incorrect output)
- [ ] Breach notification timeline does not exceed 24 hours for AI security events
- [ ] Termination rights exist for material AI compliance failures
- [ ] Sub-processor flow-down covers LLM providers specifically
- [ ] Jurisdictional requirements are addressed for all identified markets

### Escalation Triggers

Escalate to human legal counsel immediately if:

- `CRITICAL` The vendor refuses ALL AI-specific terms
- `CRITICAL` The AI system is classified as high-risk and the vendor has no conformity assessment
- `CRITICAL` The contract involves processing sensitive personal data (Tier 4) with no DPA
- `HIGH` The vendor claims IP ownership of outputs generated from your data
- `HIGH` The vendor's AI system may be a prohibited system under EU AI Act Art. 5
- `HIGH` The vendor insists on using your data for model training with no carve-out
- `MEDIUM` The vendor has no SOC 2 and processes personal data

---

## Workflow 2: AI Risk Classification & EU AI Act Compliance Assessment

### Trigger

The startup is developing, deploying, or procuring an AI system and needs to determine its risk classification under the EU AI Act and other applicable AI laws, and assess compliance obligations.

### Input

| Required Input | Format | Source |
|---|---|---|
| AI system description (purpose, functionality, use cases) | Free text / product spec | Product / engineering team |
| Data types processed (categories of personal data, if any) | List | Data / engineering team |
| Target markets and jurisdictions | List | Business / legal team |
| User categories (who interacts with or is affected by the AI) | List | Product team |
| Decision types made by the AI (advisory, automated, hybrid) | Description | Product team |
| AI model details (provider, type, training data sources) | Technical spec | Engineering team |
| Current compliance documentation (if any) | Various | Legal / compliance |

### Legal Framework

| Law / Principle | Application |
|---|---|
| **EU AI Act** | Art. 5 (prohibited practices), Art. 6 + Annex III (high-risk classification), Art. 50 (transparency for limited risk), Art. 51-52 (GPAI obligations) |
| **EU AI Act Annex I** | High-risk AI systems within EU harmonization legislation |
| **EU AI Act Annex III** | High-risk AI in: biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, justice |
| **CAIA** | §6-1-1701 (consequential decisions in education, employment, financial, housing, healthcare, legal) |
| **NIST AI RMF 1.0** | MAP function: contextualizing risks; GOVERN function: organizational governance |
| **ISO/IEC 42001:2023** | AI management system standard |

### Process

**STEP 1 — Prohibited Practice Screen** `[10 min]`

Screen the AI system against all prohibited practices under EU AI Act Art. 5. If ANY of the following are TRUE, the system is **BANNED** and cannot proceed:

| # | Prohibited Practice | Test Question | Result |
|---|---|---|---|
| 1.1 | Subliminal manipulation | Does the system deploy techniques beyond a person's consciousness to materially distort behavior in a way that causes or is likely to cause harm? | YES → `BANNED` / NO → Continue |
| 1.2 | Exploitation of vulnerabilities | Does the system exploit vulnerabilities of specific groups (age, disability, social/economic situation) to distort behavior causing harm? | YES → `BANNED` / NO → Continue |
| 1.3 | Social scoring by public authorities | Does the system evaluate or classify persons based on social behavior or personal characteristics leading to detrimental treatment? | YES → `BANNED` / NO → Continue |
| 1.4 | Predictive policing (solely profiling) | Does the system assess risk of criminal offending based solely on profiling or personality traits? | YES → `BANNED` / NO → Continue |
| 1.5 | Untargeted facial recognition scraping | Does the system create or expand facial recognition databases through untargeted scraping? | YES → `BANNED` / NO → Continue |
| 1.6 | Emotion recognition in workplace/school | Does the system infer emotions in workplace or educational settings (except for medical/safety reasons)? | YES → `BANNED` / NO → Continue |
| 1.7 | Biometric categorization (sensitive attributes) | Does the system categorize individuals based on biometric data to deduce race, political opinions, trade union membership, religious beliefs, sex life, or sexual orientation? | YES → `BANNED` / NO → Continue |
| 1.8 | Real-time remote biometric ID in public spaces | Does the system perform real-time remote biometric identification in publicly accessible spaces for law enforcement? | YES → `BANNED` (narrow exceptions) / NO → Continue |

If all answers are NO, proceed to Step 2.

**STEP 2 — High-Risk Classification (EU AI Act)** `[15 min]`

2.1. **Annex I check:** Is the AI system a safety component of, or itself, a product covered by EU harmonization legislation listed in Annex I (e.g., machinery, medical devices, vehicles, toys, lifts, radio equipment, civil aviation, rail systems)?
- YES → **HIGH-RISK** under Art. 6(1) → Proceed to Step 3
- NO → Continue to 2.2

2.2. **Annex III check:** Does the AI system fall into any of these categories?

| Category | Examples | Result |
|---|---|---|
| Biometrics (not prohibited above) | Remote biometric identification, emotion recognition (non-workplace), biometric categorization | HIGH-RISK |
| Critical infrastructure | AI managing energy, water, gas, heating, digital infrastructure, road traffic, supply of water | HIGH-RISK |
| Education & vocational training | AI determining access to education, evaluating learning outcomes, monitoring cheating | HIGH-RISK |
| Employment & workers management | AI for recruitment, screening, evaluating candidates, making promotion/termination/task allocation decisions | HIGH-RISK |
| Access to essential services | AI for credit scoring, risk assessment in insurance, evaluating eligibility for public benefits, emergency dispatching | HIGH-RISK |
| Law enforcement | AI for individual risk assessment, polygraphs, evidence evaluation, profiling in criminal investigations | HIGH-RISK |
| Migration, asylum, border control | AI for risk assessment, document authentication, asylum application processing | HIGH-RISK |
| Administration of justice | AI assisting judicial authorities in researching/interpreting facts and law, applying law to facts | HIGH-RISK |

2.3. **Exception check:** Even if matched above, the system is NOT high-risk if it performs a narrow procedural task, improves the result of a previously completed human activity, detects decision-making patterns without replacing human assessment, or is a preparatory task for an assessment in Annex III. Apply Art. 6(3) exceptions.

2.4. Record classification result: `PROHIBITED` / `HIGH-RISK` / `LIMITED RISK` / `MINIMAL RISK`

**STEP 3 — CAIA Classification** `[10 min]`

3.1. Does the AI system make or substantially support a **consequential decision** — a decision that has a material legal or similarly significant effect on a consumer's access to or terms of:

| Domain | Consequential? |
|---|---|
| Education enrollment or opportunity | YES |
| Employment or employment opportunity | YES |
| Financial or lending service | YES |
| Government service | YES |
| Healthcare service | YES |
| Housing | YES |
| Insurance | YES |
| Legal service | YES |

3.2. If YES to any: classify as **CAIA-regulated.** Determine whether the startup is a "developer" (builds/trains the AI) or "deployer" (uses the AI) or both.

**STEP 4 — GPAI Model Assessment** `[5 min]`

4.1. Is the AI system built on or does it integrate a general-purpose AI model (e.g., GPT-4, Claude, Gemini, Llama, Mistral)?

4.2. If the startup is the **provider** of a GPAI model:
- Technical documentation obligations (Art. 53)
- Copyright compliance (Art. 53(1)(c))
- Training data summary publication (Art. 53(1)(d))
- Systemic risk assessment if model exceeds 10^25 FLOPs (Art. 51)

4.3. If the startup is a **downstream deployer** of a GPAI model:
- Ensure the GPAI provider is compliant
- Maintain your own transparency and documentation obligations
- Ensure the provider supplies adequate Instructions for Use

**STEP 5 — Compliance Obligation Mapping** `[15 min]`

Based on the classification from Steps 1-4, map all applicable obligations:

For **HIGH-RISK** systems (EU AI Act):

| Obligation | Article | Deadline | Status |
|---|---|---|---|
| Risk management system | Art. 9 | Before market placement | ☐ |
| Data governance | Art. 10 | Before market placement | ☐ |
| Technical documentation | Art. 11 + Annex IV | Before market placement | ☐ |
| Record-keeping / logging | Art. 12 | Before market placement | ☐ |
| Transparency / Instructions for Use | Art. 13 | Before market placement | ☐ |
| Human oversight design | Art. 14 | Before market placement | ☐ |
| Accuracy, robustness, cybersecurity | Art. 15 | Before market placement | ☐ |
| Quality management system | Art. 17 | Before market placement | ☐ |
| Conformity assessment | Art. 43 | Before market placement | ☐ |
| CE marking | Art. 48 | Before market placement | ☐ |
| EU database registration | Art. 49 | Before market placement | ☐ |
| Post-market monitoring | Art. 72 | Ongoing | ☐ |
| Serious incident reporting | Art. 73 | Within 15 days of awareness | ☐ |

For **LIMITED RISK** systems:

| Obligation | Article | Deadline | Status |
|---|---|---|---|
| Disclose AI interaction to users | Art. 50(1) | At time of interaction | ☐ |
| Label AI-generated content (deepfakes) | Art. 50(2) | At time of publication | ☐ |
| Label AI-generated text on public interest topics | Art. 50(4) | At time of publication | ☐ |

For **CAIA-regulated** systems:

| Obligation | Provision | Deadline | Status |
|---|---|---|---|
| Risk management policy (aligned w/ NIST AI RMF) | §6-1-1702 | Before deployment | ☐ |
| Algorithmic discrimination protections | §6-1-1702 | Before deployment | ☐ |
| Impact assessment | §6-1-1703 | Before deployment + annually | ☐ |
| Consumer disclosure | §6-1-1704 | At time of decision | ☐ |
| Consumer appeal mechanism | §6-1-1704 | At time of decision | ☐ |
| AG notification of discrimination discovery | §6-1-1706 | Within 90 days | ☐ |

**STEP 6 — Timeline & Remediation Plan** `[10 min]`

6.1. Map each unfulfilled obligation to a responsible team member and deadline.

6.2. Prioritize by: (a) legal deadline proximity, (b) severity of non-compliance penalty, (c) implementation complexity.

6.3. Flag any obligations that cannot be met by the applicable deadline.

### Output

| Deliverable | Format | Description |
|---|---|---|
| **Risk Classification Report** | Structured document | Classification result with full analysis for EU AI Act, CAIA, and other applicable laws |
| **Prohibited Practice Screen** | Pass/Fail table | Step 1 results documenting why the system is not prohibited |
| **Compliance Obligation Map** | Checklist table | All applicable obligations with status, responsible party, and deadline |
| **Remediation Plan** | Action plan | Prioritized list of compliance gaps with timelines and ownership |
| **GPAI Assessment** (if applicable) | Memo | GPAI model obligations and compliance status |

### Validation Criteria

- [ ] All eight prohibited practice screens are documented with clear YES/NO reasoning
- [ ] High-risk classification analysis references specific Annex III categories or provides clear exclusion rationale
- [ ] Art. 6(3) exceptions are considered and documented where applicable
- [ ] CAIA classification addresses every covered domain
- [ ] Every identified obligation has an assigned owner and deadline
- [ ] The remediation plan is feasible within applicable legal deadlines
- [ ] GPAI obligations are assessed if any general-purpose model is integrated

### Escalation Triggers

- `CRITICAL` System matches a prohibited practice under Art. 5
- `CRITICAL` System is high-risk with no conformity assessment and market placement is imminent
- `HIGH` System makes consequential decisions under CAIA with no impact assessment
- `HIGH` GPAI model with systemic risk classification (>10^25 FLOPs) without documentation
- `MEDIUM` Classification is ambiguous; reasonable arguments exist for both high-risk and non-high-risk

---

## Workflow 3: Data Processing Addendum (DPA) Drafting for AI Systems

### Trigger

The startup is entering into a relationship where personal data will be processed by or through an AI system, either as a data controller engaging a processor, or as a processor receiving data from a controller.

### Input

| Required Input | Format | Source |
|---|---|---|
| Parties involved (controller/processor roles) | Description | Legal / business |
| Categories of data subjects | List | Product / legal |
| Categories of personal data processed | List | Engineering / data team |
| Purposes of processing | Description | Product / legal |
| AI system description and data flows | Technical spec | Engineering |
| Sub-processors (including LLM providers) | List with locations | Engineering / vendor |
| International transfer jurisdictions | List | Operations / engineering |
| Existing MSA or vendor agreement | Document | Legal |
| Data retention requirements | Description | Legal / compliance |

### Legal Framework

| Law / Principle | Application |
|---|---|
| **GDPR Art. 28** | Mandatory processor agreement requirements |
| **GDPR Art. 32** | Security of processing |
| **GDPR Art. 33-34** | Breach notification (72 hours to supervisory authority) |
| **GDPR Art. 35** | Data Protection Impact Assessment |
| **GDPR Art. 44-49** | International data transfers (SCCs, adequacy, BCRs) |
| **CCPA §1798.140(ag)** | Service provider / contractor obligations |
| **CCPA §1798.100(d)** | Restrictions on service provider use of personal information |
| **EU AI Act Art. 10** | Data governance for high-risk systems |
| **DIFC Data Protection Law** | Processing requirements for Dubai/DIFC operations |
| **Standard Contractual Clauses** | Commission Implementing Decision 2021/914 (controller-to-processor module) |

### Process

**STEP 1 — Role Determination** `[5 min]`

1.1. Determine data protection roles:

| Question | If YES → |
|---|---|
| Does the startup determine the purposes and means of processing? | Startup = Controller |
| Does the vendor process data on behalf of / under instructions from the startup? | Vendor = Processor |
| Do both parties jointly determine purposes and means? | Joint Controllers (Art. 26) |
| Is the vendor independently deciding how to use the data? | Vendor = Independent Controller (different DPA structure) |

1.2. Map the AI-specific data flow:
```
User Data → Startup (Controller) → Vendor API (Processor) → LLM Provider (Sub-Processor) → [Tools/APIs] (Further Sub-Processors)
```

**STEP 2 — DPA Core Provisions Drafting** `[20 min]`

Draft each provision in sequence:

**2.1 Subject Matter and Duration**
- Define the processing activities, duration, nature, and purpose
- Specify that processing relates to AI system operation
- Reference the underlying MSA

**2.2 Types of Personal Data and Data Subject Categories**
- Enumerate all categories with specificity
- Flag any special category data (Art. 9 GDPR) — triggers enhanced protections
- Flag any children's data — triggers COPPA / enhanced GDPR protections

**2.3 Obligations of the Processor**

Draft obligations covering:

| Obligation | Legal Basis | AI-Specific Requirement |
|---|---|---|
| Process only on documented instructions | GDPR Art. 28(3)(a) | AI system must not process data beyond instructed scope; no autonomous data collection |
| Confidentiality of personnel | GDPR Art. 28(3)(b) | Personnel accessing AI system data bound by confidentiality |
| Security measures | GDPR Art. 28(3)(c), 32 | AI-specific: input/output logging, prompt injection defense, model access controls, output filtering, tenant isolation |
| Sub-processor management | GDPR Art. 28(3)(d), 28(4) | Prior written approval for all sub-processors INCLUDING LLM providers; substantially similar terms |
| Assist with data subject rights | GDPR Art. 28(3)(e) | Must be able to identify, access, correct, and delete personal data processed by AI; address right to human review of automated decisions |
| Assist with security, breach notification, DPIA | GDPR Art. 28(3)(f) | AI-specific incident types included (adversarial attacks, data poisoning, model compromise) |
| Delete or return data on termination | GDPR Art. 28(3)(g) | Include deletion from model training data if applicable; confirmation of deletion |
| Audit and inspection rights | GDPR Art. 28(3)(h) | Right to audit AI system, not just data processing infrastructure |

**2.4 AI-Specific Addendum Provisions**

These provisions go BEYOND standard DPA requirements:

| Provision | Requirement | Rationale |
|---|---|---|
| **No model training** | Processor shall not use personal data to train, fine-tune, or improve any AI model | Prevents data leakage through model memorization |
| **Zero retention by LLM provider** | AI Features Provider (LLM) must maintain zero data retention beyond immediate processing | Minimizes exposure surface |
| **Data segregation** | Personal data processed by AI must be logically segmented per customer, encrypted with unique keys, not commingled | Multi-tenancy protection |
| **Input/Output confidentiality** | All Inputs and Outputs of the AI system are Confidential Information | Prevents vendor monetization of data/insights |
| **Model Drift monitoring** | Processor must monitor for Model Drift; notify within 72 hours of detection | Prevents degraded/unsafe performance |
| **Bias testing** | Processor must conduct and document bias testing for AI decisions affecting individuals | Discrimination prevention |
| **Human oversight** | AI decisions with legal or significant effects must allow for human review | GDPR Art. 22; CAIA requirements |
| **Automated decision-making disclosure** | Processor must support controller's obligation to inform data subjects of automated decision-making | GDPR Art. 13(2)(f), 14(2)(g), 22(3) |

**STEP 3 — International Transfer Mechanisms** `[10 min]`

3.1. Map all locations where personal data will be processed, including:
- Vendor's primary processing location
- LLM provider's processing location (often US-based)
- Any additional tool/API call destinations

3.2. For each transfer outside the adequate jurisdiction:
- Implement Standard Contractual Clauses (Module 2: Controller-to-Processor or Module 3: Processor-to-Processor)
- Conduct Transfer Impact Assessment
- Identify supplementary measures if needed

3.3. For DIFC-specific operations: ensure compliance with DIFC Data Protection Law transfer provisions.

**STEP 4 — Breach Notification Procedures** `[10 min]`

Draft breach notification provisions with AI-specific event types:

| Event Type | Notification Deadline | To Whom |
|---|---|---|
| Standard personal data breach | Without undue delay, max 72 hours (to controller) | Controller → Supervisory Authority within 72 hours; data subjects if high risk |
| AI-specific: adversarial attack compromising data | 24 hours to controller | Controller assesses regulatory notification obligations |
| AI-specific: data poisoning affecting outputs | 24 hours to controller | Controller assesses impact on data subjects |
| AI-specific: prompt injection leading to data exfiltration | 24 hours to controller | Controller → immediate assessment and notification |
| AI-specific: model memorization / data leakage in outputs | 24 hours to controller | Controller → assess scope and notify |
| AI-specific: cross-tenant data exposure | 24 hours to controller | Controller → assess and notify all affected subjects |

**STEP 5 — DPIA Trigger Assessment** `[5 min]`

5.1. Assess whether a DPIA is required under GDPR Art. 35. A DPIA is **mandatory** if the AI processing involves:
- Systematic and extensive evaluation of personal aspects (profiling) with legal/significant effects
- Large-scale processing of special categories of data
- Systematic monitoring of publicly accessible areas
- Any two or more from: evaluation/scoring, automated decision-making with legal effect, systematic monitoring, sensitive data, large scale, data matching/combining, vulnerable data subjects, innovative use of technology, transfer outside EU

5.2. If DPIA is required, include DPIA cooperation obligations in the DPA.

### Output

| Deliverable | Format | Description |
|---|---|---|
| **Data Processing Addendum** | DOCX | Complete DPA with all GDPR-mandated provisions plus AI-specific addendum |
| **Sub-Processor List** | Table | All sub-processors including LLM providers with locations and purposes |
| **Transfer Impact Assessment** | Memo | Assessment of international transfer risks and mechanisms |
| **DPIA Trigger Assessment** | Checklist | Determination of whether DPIA is required with reasoning |
| **Data Flow Diagram** | Diagram description | Visual representation of personal data flow through the AI system |

### Validation Criteria

- [ ] Every GDPR Art. 28(3) mandatory provision is addressed
- [ ] AI-specific provisions cover model training prohibition, zero retention, data segregation, bias testing, and human oversight
- [ ] All sub-processors (including LLM providers) are listed with locations
- [ ] International transfer mechanisms are identified and documented for every cross-border flow
- [ ] Breach notification timelines are specific and include AI-specific event types
- [ ] DPIA trigger assessment is documented
- [ ] CCPA service provider requirements are addressed if California data subjects are in scope
- [ ] Automated decision-making disclosure obligations are supported

### Escalation Triggers

- `CRITICAL` Special category data (health, biometric, genetic) is processed by AI with no enhanced safeguards
- `CRITICAL` LLM provider has no DPA or data processing terms
- `HIGH` International transfers occur with no legal mechanism in place
- `HIGH` AI system makes automated decisions with legal effects and no human review mechanism
- `MEDIUM` DPIA is required but has not been conducted

---

## Workflow 4: Internal AI Acceptable Use Policy Creation

### Trigger

The startup needs to establish or update its internal policy governing how employees, contractors, and agents use AI tools in connection with company business.

### Input

| Required Input | Format | Source |
|---|---|---|
| List of AI tools currently used or planned | List with descriptions | IT / Engineering |
| Types of data employees handle | Classification scheme | Security / compliance |
| Industry-specific regulatory requirements | List | Legal |
| Existing information security policy | Document | Security |
| Existing data classification policy | Document | Security |
| Employee count and structure (FTE, contractors, interns) | Number + categories | HR |
| Any prior AI-related incidents | Description | Security / legal |

### Legal Framework

| Law / Principle | Application |
|---|---|
| **EU AI Act Art. 4** | AI literacy obligation: ensure personnel have sufficient understanding of AI |
| **GDPR Art. 5** | Data minimization, purpose limitation, storage limitation, integrity, confidentiality |
| **GDPR Art. 32** | Appropriate technical and organizational measures |
| **CCPA §1798.100(d)** | Restrictions on use and disclosure of personal information |
| **CAIA §6-1-1702** | Risk management program aligned with NIST AI RMF |
| **NIST AI RMF** | GOVERN function: organizational AI governance policies |
| **Trade Secrets Law (DTSA, state UTSA)** | Protection of confidential business information |
| **Attorney-Client Privilege** | Protection of privileged communications from disclosure to AI tools |

### Process

**STEP 1 — Scoping** `[10 min]`

1.1. Define personnel scope: all individuals who use AI tools in connection with company business, including employees, independent contractors, temporary staff, interns, and consultants.

1.2. Define tool scope: direct use of generative AI tools (ChatGPT, Claude, Gemini, Copilot, Midjourney, etc.), AI features embedded in approved software, and company-built AI tools.

1.3. Define exclusion scope: personal use of AI tools unrelated to company business is outside policy scope (but note that using company devices/networks for personal AI use may still create risk).

**STEP 2 — Data Classification Matrix** `[10 min]`

Create a four-tier data classification for AI use:

| Tier | Classification | Examples | AI Tool Use |
|---|---|---|---|
| 1 | **Public** | Published marketing content, public filings, general knowledge | Permitted in any approved AI tool |
| 2 | **Internal** | Internal memos, meeting notes, project plans, non-sensitive code | Permitted in enterprise-grade approved AI tools only |
| 3 | **Confidential** | Customer data, financial projections, strategic plans, proprietary algorithms | Permitted ONLY in approved enterprise AI tools with data segregation guarantees; requires manager approval |
| 4 | **Restricted** | PII, PHI, financial account data, trade secrets, attorney-client privileged, source code with proprietary logic | **NEVER** input into any external AI tool; internal approved tools only with explicit CISO approval |

**STEP 3 — Policy Drafting** `[30 min]`

Draft the following sections:

**3.1 Purpose Statement**
Frame positively: AI tools increase productivity and innovation. This policy enables responsible use while managing risks to the company, customers, and employees.

**3.2 Approved Tools List**
- Maintain a living list of approved AI tools, categorized by data tier authorization
- New tools require evaluation through the procurement policy before use
- Include version/tier requirements (enterprise vs. consumer)

**3.3 Mandatory Rules** (non-negotiable):

| Rule | Legal Basis | Rationale |
|---|---|---|
| Only use approved AI tools for company business | NIST GOVERN; trade secrets | Prevents shadow AI and data leakage |
| Never input Restricted (Tier 4) data into external AI tools | GDPR Art. 5; CCPA; trade secrets; privilege | Prevents irreversible disclosure of sensitive data |
| Opt out of vendor data training wherever possible | GDPR Art. 5(1)(b); CCPA | Prevents company data from being used to train vendor models |
| Use enterprise/business accounts, not personal | GDPR Art. 32; information security | Ensures contractual protections apply |
| Enable multi-factor authentication | GDPR Art. 32; NIST | Basic access security |
| Review all AI-generated output before use | EU AI Act Art. 14 (human oversight); professional responsibility | AI outputs may be inaccurate, biased, or infringing |
| Do not represent AI-generated work as solely human-created where law requires disclosure | EU AI Act Art. 50; CAIA | Transparency obligations |
| Report AI security incidents immediately | GDPR Art. 33; company IR plan | Enables timely response |
| Do not use AI to make or support consequential decisions about individuals without human review | GDPR Art. 22; CAIA | Automated decision-making protections |
| Maintain confidentiality of AI-generated business insights | Trade secrets; NDA obligations | AI output can contain derived confidential information |

**3.4 Guidance by Use Case**

| Use Case | Permitted? | Conditions |
|---|---|---|
| Drafting emails, communications | Yes | Review before sending; no Tier 3-4 data |
| Code generation / debugging | Yes | Use approved code assistants only; review for security vulnerabilities; no proprietary algorithms |
| Research and summarization | Yes | Verify facts independently; cite primary sources |
| Creating presentations / documents | Yes | Review for accuracy; no confidential data in external tools |
| Customer-facing content generation | Yes | Human review and approval before publication |
| Data analysis | Conditional | Only with approved tools authorized for the data tier |
| Legal document drafting | Conditional | Attorney review required; never input privileged information into external tools |
| HR / employment decisions | Restricted | CAIA and local law compliance required; human decision-maker required; impact assessment |
| Financial forecasting / credit decisions | Restricted | Regulatory compliance required; human oversight; documentation |

**3.5 AI Literacy Training Requirements**
Per EU AI Act Art. 4, all personnel must receive training on:
- The capabilities and limitations of AI systems they use
- This policy and its requirements
- Data classification and handling
- Recognizing AI-generated errors, biases, and hallucinations
- Incident reporting procedures

Training frequency: onboarding + annual refresher + ad hoc for new tool deployments.

**3.6 Enforcement**
- Policy violations are subject to disciplinary action up to and including termination
- Violations involving data breaches will be handled under the incident response plan
- Anonymous reporting mechanism for suspected violations

### Output

| Deliverable | Format | Description |
|---|---|---|
| **AI Acceptable Use Policy** | Markdown or DOCX | Complete policy document ready for executive approval |
| **Approved AI Tools Register** | Table | Living list of approved tools with data tier authorizations |
| **Data Classification Guide for AI** | One-page reference | Quick-reference for employees on what data can go where |
| **Training Curriculum Outline** | Document | Topics, frequency, and assessment requirements for AI literacy |
| **Acknowledgment Form** | Form | Employee acknowledgment and agreement to comply |

### Validation Criteria

- [ ] Policy covers all personnel categories (employees, contractors, interns, consultants)
- [ ] Data classification matrix has four tiers with clear AI-use permissions per tier
- [ ] Restricted data (PII, PHI, trade secrets, privileged information) is explicitly prohibited from external AI tools
- [ ] Enterprise-only tool requirement is clear
- [ ] Human review requirement for all AI output is explicit
- [ ] EU AI Act Art. 4 literacy requirement is addressed
- [ ] CAIA consequential decision restrictions are addressed
- [ ] Incident reporting obligation is clear and immediate
- [ ] Enforcement mechanism is specified
- [ ] Policy can be updated as new tools are approved (living document)

### Escalation Triggers

- `CRITICAL` Discovery that employees have been inputting Tier 4 data (PII, trade secrets, privileged info) into unapproved AI tools
- `HIGH` No enterprise agreement exists for an AI tool widely used by employees
- `HIGH` AI tools are being used for consequential decisions (hiring, credit, etc.) without compliance review
- `MEDIUM` Employees using personal accounts for business AI use

---

## Workflow 5: AI Product Privacy Notice Generation

### Trigger

The startup is launching or updating an AI-powered product or service that processes personal data and needs a privacy notice that meets all applicable legal requirements including AI-specific disclosures.

### Input

| Required Input | Format | Source |
|---|---|---|
| Product/service description | Free text | Product team |
| Categories of personal data collected | Detailed list | Engineering / data team |
| Purposes of processing (including AI-specific purposes) | List | Product / legal |
| Third parties data is shared with (including LLM providers) | List with locations | Engineering |
| Data retention periods | Schedule | Legal / compliance |
| Automated decision-making / profiling activities | Description | Product team |
| Target jurisdictions and user demographics | List | Business team |
| Cookie / tracking technologies used | List | Engineering |
| Legal bases for processing | Assessment | Legal |
| Data subject rights procedures | Description | Legal / customer support |

### Legal Framework

| Law / Principle | Application |
|---|---|
| **GDPR Art. 13-14** | Information to be provided to data subjects at collection |
| **GDPR Art. 22** | Automated individual decision-making, including profiling |
| **CCPA §1798.100(a)** | Notice at or before collection |
| **CCPA §1798.110** | Categories of personal information collected, purposes, third parties |
| **EU AI Act Art. 50** | Transparency obligations for AI systems interacting with persons |
| **EU AI Act Art. 86** | Right to explanation for high-risk AI decisions |
| **CAIA §6-1-1704** | Consumer disclosure obligations for consequential AI decisions |
| **COPPA** | Parental consent and notice for children under 13 |
| **CalOPPA** | Privacy policy posting requirements for California users |
| **DIFC Data Protection Law** | Processing disclosures and individual rights |

### Process

**STEP 1 — Jurisdiction & Obligation Mapping** `[10 min]`

1.1. Based on target jurisdictions, identify all applicable privacy laws.

1.2. Apply the "highest common denominator" approach: the privacy notice should meet the most stringent requirements across all applicable jurisdictions, with jurisdiction-specific addenda where needed.

1.3. Flag special populations: children (COPPA), EU residents (GDPR), California residents (CCPA/CPRA), DIFC (DIFC Data Protection Law).

**STEP 2 — Content Assembly** `[25 min]`

Draft each section:

| Section | Required Content | Legal Basis |
|---|---|---|
| **Identity & Contact** | Company name, address, DPO contact (if applicable), privacy team email | GDPR Art. 13(1)(a-b) |
| **Data Collected** | Exhaustive list of personal data categories with specificity (not just "personal information") | GDPR Art. 13(1)(d); CCPA §1798.100(b) |
| **Purposes of Processing** | Each purpose separately stated; AI-specific purposes explicitly identified (e.g., "to generate personalized recommendations using machine learning") | GDPR Art. 13(1)(c); CCPA §1798.100(a) |
| **Legal Bases** | For each purpose, the specific legal basis: consent, contract performance, legitimate interest, legal obligation | GDPR Art. 13(1)(c) |
| **AI/Automated Decision-Making Disclosure** | Existence of automated decision-making including profiling; meaningful information about the logic involved; significance and envisaged consequences | GDPR Art. 13(2)(f); Art. 22(3); EU AI Act Art. 50; CAIA §6-1-1704 |
| **Third Party Sharing** | All categories of recipients including LLM providers, cloud infrastructure, analytics; for CCPA: categories of PI shared/sold | GDPR Art. 13(1)(e-f); CCPA §1798.110(c) |
| **International Transfers** | Countries where data is transferred; safeguards (SCCs, adequacy decisions) | GDPR Art. 13(1)(f) |
| **Retention Periods** | Specific periods or criteria for each category of data | GDPR Art. 13(2)(a) |
| **Individual Rights** | All applicable rights: access, correction, deletion, portability, objection, restriction, withdrawal of consent, right to human review of automated decisions, right not to be subject to solely automated decisions | GDPR Art. 13(2)(b-d); CCPA §1798.100-125; CAIA §6-1-1704 |
| **Right to Opt Out** | Opt-out of sale/sharing (CCPA); opt-out of automated decision-making (CCPA/CPRA); opt-out of profiling (GDPR) | CCPA §1798.120; GDPR Art. 21 |
| **Children's Privacy** | If service may be used by children: COPPA notice, age verification, parental consent mechanisms | COPPA; GDPR Art. 8 |
| **Cookies & Tracking** | Technologies used; purposes; consent mechanisms | ePrivacy Directive; CCPA |
| **Security Measures** | General description of security measures (without compromising security) | GDPR Art. 32 |
| **Updates** | How users will be notified of changes; effective date | Best practice |
| **Complaints** | Right to complain to supervisory authority with contact information | GDPR Art. 13(2)(d) |

**STEP 3 — AI-Specific Disclosure Drafting** `[15 min]`

This is the section most AI startups get wrong. Kevin drafts specific, meaningful disclosures:

3.1. **AI Interaction Disclosure** (EU AI Act Art. 50):
- Clearly inform users when they are interacting with an AI system (not a human)
- Disclose when content has been AI-generated (text, images, audio, video)
- Disclose when AI-generated content relates to matters of public interest (deepfake labeling)

3.2. **Automated Decision-Making Disclosure** (GDPR Art. 22; CAIA):
- Identify each automated decision that has legal or similarly significant effects
- Explain the logic involved in meaningful terms (not technical jargon)
- Describe the significance and envisaged consequences for the individual
- Explain the right to human intervention, to express a point of view, and to contest the decision
- Describe how to exercise the right to opt out or obtain human review

3.3. **AI Data Usage Disclosure**:
- Whether personal data is used to train or improve AI models
- Whether inputs to the AI system are stored and for how long
- Whether AI outputs are retained and associated with the individual
- Whether profiling occurs and the categories of data used

**STEP 4 — Readability & Accessibility Review** `[5 min]`

4.1. Ensure the notice is written in clear, plain language (GDPR Art. 12: "concise, transparent, intelligible and easily accessible form, using clear and plain language")

4.2. Target reading level: 8th grade or below

4.3. Use layered disclosure where appropriate: summary layer + detailed layer

4.4. Ensure accessibility: available in required languages, accessible format (WCAG 2.1 AA)

### Output

| Deliverable | Format | Description |
|---|---|---|
| **Privacy Notice** | Markdown (for web) + DOCX (for records) | Complete privacy notice meeting all applicable legal requirements |
| **AI Disclosure Section** | Standalone section | The AI-specific disclosure, also usable as an in-product notice |
| **Cookie Notice** | Markdown | Cookie/tracking technology notice if applicable |
| **Jurisdiction-Specific Addenda** | Supplements | California, DIFC, or other jurisdiction-specific provisions |
| **Consent Collection Matrix** | Table | What consent is needed, for what, and when |

### Validation Criteria

- [ ] Every GDPR Art. 13 required element is present
- [ ] Every CCPA §1798.100/110 required element is present
- [ ] AI interaction disclosure meets EU AI Act Art. 50
- [ ] Automated decision-making disclosure meets GDPR Art. 22(3) and CAIA §6-1-1704
- [ ] All third parties (including LLM providers) are disclosed
- [ ] International transfers are identified with safeguard mechanisms
- [ ] Individual rights section includes the right to human review of AI decisions
- [ ] Notice is written in plain language at 8th-grade reading level or below
- [ ] Data retention periods are specific, not vague

### Escalation Triggers

- `CRITICAL` Product makes automated decisions with legal effects and no disclosure mechanism exists
- `HIGH` Children may use the product and no COPPA compliance is in place
- `HIGH` Special category data (health, biometric) is processed by AI without explicit consent mechanism
- `MEDIUM` LLM provider is not disclosed as a third-party recipient

---

## Workflow 6: AI Threat Model Assessment

### Trigger

The startup is building, deploying, or significantly modifying an AI system and needs to identify, assess, and mitigate security and safety risks specific to generative AI architectures.

### Input

| Required Input | Format | Source |
|---|---|---|
| System architecture diagram | Diagram / description | Engineering |
| AI model details (provider, type, version) | Spec | Engineering |
| Tools/functions the AI agent can call | List with access levels | Engineering |
| Data types processed (by sensitivity) | Classified list | Security / data team |
| Authentication and authorization model | Description | Security |
| Multi-tenancy architecture | Description | Engineering |
| Existing security controls | List | Security |
| User access model (who can interact with the AI) | Description | Product |
| Deployment environment | Description | DevOps |

### Legal Framework

| Law / Principle | Application |
|---|---|
| **EU AI Act Art. 9** | Risk management system (mandatory for high-risk) |
| **EU AI Act Art. 15** | Accuracy, robustness, cybersecurity requirements |
| **GDPR Art. 25** | Data protection by design and by default |
| **GDPR Art. 32** | Security of processing appropriate to risk |
| **NIST AI RMF** | MAP and MEASURE functions: risk identification and assessment |
| **OWASP Top 10 for LLM Applications** | Industry-standard LLM threat taxonomy |
| **ISO/IEC 27001** | Information security management |
| **CAIA §6-1-1702** | Risk management policy aligned with NIST AI RMF |

### Process

**STEP 1 — Architecture Decomposition** `[10 min]`

Map the AI system into its component parts and identify the trust boundaries:

```
[User] ←→ [API Gateway] ←→ [AI Agent Orchestrator] ←→ [LLM Provider]
                                     ↕                        ↕
                              [Internal Tools]          [Cloud Storage]
                              [Databases]
                              [External APIs]
```

For each component, identify:
- Who controls it (your team, vendor, LLM provider)
- What data it can access
- What actions it can perform
- What authentication/authorization it uses

**STEP 2 — Threat Identification** `[20 min]`

Assess every threat path from the master threat model (SKILL.md Section 6). For each, determine applicability and current mitigation status:

| # | Threat Category | Threat Path | Applicable? | Current Mitigation | Gap? |
|---|---|---|---|---|---|
| T1 | Data exposure — public | LLM provider uses data for training | Y/N | [Describe] | Y/N |
| T2 | Data exposure — public | Source documents contain sensitive info | Y/N | [Describe] | Y/N |
| T3 | Data exposure — unauthorized 3P | LLM shares context with third parties | Y/N | [Describe] | Y/N |
| T4 | Data exposure — unauthorized 3P | Tool calls leak data to external services | Y/N | [Describe] | Y/N |
| T5 | Cross-user exposure | LLM session mixing between tenants | Y/N | [Describe] | Y/N |
| T6 | Cross-user exposure | Tool calls with wider-access tokens | Y/N | [Describe] | Y/N |
| T7 | Agent hijacking | Prompt injection → unauthorized actions | Y/N | [Describe] | Y/N |
| T8 | Agent hijacking | Function call definition override | Y/N | [Describe] | Y/N |
| T9 | Agent hijacking | Malicious code via eval() | Y/N | [Describe] | Y/N |
| T10 | Brand damage | Rude/adversarial/hallucinatory output | Y/N | [Describe] | Y/N |
| T11 | Legal/compliance | AI agrees to binding terms | Y/N | [Describe] | Y/N |
| T12 | Legal/compliance | AI breaks compliance rules | Y/N | [Describe] | Y/N |
| T13 | Legal/compliance | Copyright infringement of outputs | Y/N | [Describe] | Y/N |
| T14 | Financial | API cost abuse via recursion | Y/N | [Describe] | Y/N |
| T15 | Financial | DDoS on AI endpoints | Y/N | [Describe] | Y/N |
| T16 | Data integrity | Tampering without audit trail | Y/N | [Describe] | Y/N |
| T17 | Model integrity | Model poisoning (LLM breach) | Y/N | [Describe] | Y/N |
| T18 | Model integrity | Malicious code in model weights | Y/N | [Describe] | Y/N |

**STEP 3 — Risk Scoring** `[10 min]`

For each applicable threat with a gap, score:

| Factor | Scale |
|---|---|
| **Impact** (if exploited) | 1 (negligible) — 2 (minor) — 3 (moderate) — 4 (major) — 5 (catastrophic) |
| **Probability** (of exploitation) | 1 (rare) — 2 (unlikely) — 3 (possible) — 4 (likely) — 5 (almost certain) |
| **Ease of Exploitation** | 1 (expert only) — 2 (skilled) — 3 (moderate skill) — 4 (low skill) — 5 (trivial) |

**Risk Score** = (Impact × Probability × Ease) / 3

| Score Range | Risk Level | Action Required |
|---|---|---|
| 1-5 | `LOW` | Accept or monitor |
| 6-15 | `MEDIUM` | Mitigate within 90 days |
| 16-30 | `HIGH` | Mitigate within 30 days |
| 31+ | `CRITICAL` | Mitigate before deployment / immediately |

**STEP 4 — Mitigation Plan** `[15 min]`

For each HIGH and CRITICAL risk, draft a specific mitigation:

| Risk ID | Threat | Risk Score | Mitigation | Owner | Deadline | Verification Method |
|---|---|---|---|---|---|---|
| [T#] | [Description] | [Score] | [Specific technical/contractual/process control] | [Person/team] | [Date] | [How to verify mitigation works] |

Standard mitigations to apply:

| Control Category | Specific Controls |
|---|---|
| **Input controls** | Prompt injection detection, input sanitization, length limits, content filtering |
| **Output controls** | Response firewalls, content safety filters, PII detection in outputs, hallucination detection |
| **Access controls** | User-scoped tokens for all tool calls, principle of least privilege, MFA |
| **Data controls** | Encryption at rest/transit, tenant isolation, data segregation, zero retention at LLM layer |
| **Monitoring** | Audit logging, anomaly detection, cost alerts, Model Drift monitoring |
| **Operational** | Rate limiting, hard limits on token usage, circuit breakers for recursive agents |
| **Contractual** | Vendor AI addendum, LLM provider DPA, indemnification, audit rights |
| **Human oversight** | Approval queues for high-stakes actions, human review for consequential decisions |

**STEP 5 — Residual Risk Acceptance** `[5 min]`

5.1. After mitigations, re-score each risk.

5.2. Document residual risks that cannot be fully mitigated.

5.3. For each residual risk above LOW, require explicit acceptance by the responsible executive (CTO, CISO, or CEO depending on severity).

### Output

| Deliverable | Format | Description |
|---|---|---|
| **Threat Model Report** | Structured document | Complete threat identification, scoring, and analysis |
| **Risk Register** | Table | All identified risks with scores, mitigations, owners, and deadlines |
| **Mitigation Plan** | Action plan | Specific controls to implement with timelines |
| **Architecture Security Diagram** | Annotated diagram | System architecture with trust boundaries and control points marked |
| **Residual Risk Acceptance Log** | Sign-off document | Executive sign-off on accepted residual risks |

### Validation Criteria

- [ ] All 18 threat categories from the master model are assessed
- [ ] Every applicable threat has a risk score with documented reasoning
- [ ] Every HIGH and CRITICAL risk has a specific mitigation plan
- [ ] Mitigations address all four control layers: technical, contractual, process, and human
- [ ] Tool/function call access is scoped to minimum necessary permissions
- [ ] LLM output is never trusted as a direct parameter for sensitive operations
- [ ] Audit logging covers all AI interactions
- [ ] Residual risks are documented with executive sign-off

### Escalation Triggers

- `CRITICAL` Unmitigated path to sensitive data exposure via AI system
- `CRITICAL` AI agent has access to production databases with write permissions and no audit trail
- `HIGH` No prompt injection defenses in place for a user-facing AI system
- `HIGH` Tool calls use service account tokens rather than user-scoped tokens
- `MEDIUM` No output filtering or content safety mechanism

---

## Workflow 7: Enterprise Customer AI Due Diligence Response

### Trigger

An enterprise prospect or customer sends an AI-related due diligence questionnaire, security assessment, or compliance questionnaire as part of the sales process or annual vendor review.

### Input

| Required Input | Format | Source |
|---|---|---|
| Customer's questionnaire / assessment | Document (various formats) | Sales / customer success |
| Customer's specific requirements or concerns | Notes | Sales team |
| Company's current compliance documentation | Various | Legal / compliance / security |
| AI system technical documentation | Spec | Engineering |
| SOC 2 report (if available) | PDF | Security |
| Sub-processor list | Table | Legal / engineering |
| Insurance certificates | PDF | Finance / legal |
| SKILL.md Section 10.3 enterprise readiness checklist | Reference | This knowledge base |

### Legal Framework

| Law / Principle | Application |
|---|---|
| **EU AI Act** | All applicable provider/deployer obligations |
| **GDPR** | Processor compliance demonstration (Art. 28) |
| **CCPA** | Service provider obligations |
| **NIST AI RMF** | Framework alignment evidence |
| **ISO/IEC 42001** | AI management system (if certified) |
| **SOC 2** | Trust service criteria (if certified) |
| **Contractual obligations** | Whatever the customer's MSA/DPA requires |

### Process

**STEP 1 — Questionnaire Triage** `[10 min]`

1.1. Categorize each question into domains:

| Domain | Examples |
|---|---|
| AI Governance | AI policy, governance committee, responsible AI principles |
| Model Details | Model provider, type, training data, versioning |
| Data Handling | Processing, storage, retention, deletion, segregation |
| Security | Access controls, encryption, monitoring, incident response |
| Compliance | Regulatory status, certifications, conformity assessments |
| Privacy | DPA, DPIA, data subject rights, international transfers |
| IP & Ownership | Output ownership, training data rights, indemnification |
| Sub-processors | LLM providers, cloud infrastructure, third-party tools |
| Insurance | Coverage types, limits, AI-specific riders |
| HR & Training | Employee AI training, background checks, NDA obligations |

1.2. Flag any questions that require information the company does not yet have → these become compliance gaps to address.

**STEP 2 — Response Drafting** `[30 min]`

For each question, draft a response that is:
- **Accurate:** Never overstate compliance posture
- **Specific:** Provide concrete details, not boilerplate
- **Forward-looking:** If a capability is in progress, state the timeline
- **Documented:** Reference specific policies, certifications, or documents

**Standard response patterns:**

| Question Type | Response Framework |
|---|---|
| "Do you have an AI governance policy?" | "[Yes/In progress]. [Company] maintains an AI Acceptable Use Policy governing all personnel use of AI tools, effective [date]. The policy covers [scope]. [Reference to SKILL.md Workflow 4 output]." |
| "What AI models do you use?" | "[Company] uses [Model Name] from [Provider] via [enterprise API / self-hosted]. Model version: [X]. The model is accessed through [enterprise agreement / API] with [data processing terms]." |
| "How is our data protected in your AI system?" | "[Company] implements the following controls: [list from threat model]. Customer data is logically segregated [method], encrypted at rest [standard] and in transit [standard]. The LLM provider maintains [zero retention / X-day retention]. Customer data is never used for model training." |
| "Do you comply with the EU AI Act?" | "[Company]'s AI system is classified as [risk level] under the EU AI Act. [For high-risk: We have completed / are completing conformity assessment by [date]]. [For limited risk: We comply with transparency obligations under Art. 50]. [For minimal risk: Our system falls below the high-risk threshold because [reasons]]." |
| "What are your indemnification terms for AI?" | "[Company]'s standard AI addendum includes indemnification for [IP infringement, breach, law violation, incorrect output]. [Reference to standard terms]." |

**STEP 3 — Gap Identification** `[10 min]`

3.1. For each question where the company cannot provide a satisfactory response, document:
- The question
- What the customer expects
- What the company currently has
- What needs to be built/obtained
- Estimated timeline

3.2. Prioritize gaps by: (a) deal-blocking risk, (b) regulatory requirement, (c) implementation effort.

**STEP 4 — Supporting Documentation Assembly** `[10 min]`

Compile and prepare for sharing:

| Document | Status | Notes |
|---|---|---|
| AI Acceptable Use Policy | ☐ Ready / ☐ In Progress | Share redacted version |
| AI Governance Framework | ☐ Ready / ☐ In Progress | |
| SOC 2 Type II Report | ☐ Ready / ☐ In Progress / ☐ Not Started | Under NDA |
| Data Processing Addendum | ☐ Ready / ☐ In Progress | |
| AI Addendum | ☐ Ready / ☐ In Progress | |
| Sub-Processor List | ☐ Ready / ☐ In Progress | |
| Bias Testing Results | ☐ Ready / ☐ In Progress | Summary only |
| Incident Response Plan | ☐ Ready / ☐ In Progress | Redacted |
| Insurance Certificates | ☐ Ready / ☐ In Progress | |
| Data Flow Diagrams | ☐ Ready / ☐ In Progress | |

### Output

| Deliverable | Format | Description |
|---|---|---|
| **Completed Questionnaire** | Customer's format | All questions answered accurately and specifically |
| **Supporting Documentation Package** | Document bundle | All referenced policies and certifications |
| **Gap Report** | Internal memo | Identified gaps with remediation timeline |
| **Deal Risk Assessment** | Summary | Assessment of whether gaps are deal-blocking |

### Validation Criteria

- [ ] Every question has a response (no blanks)
- [ ] No response overstates current compliance posture
- [ ] Responses are specific, not boilerplate
- [ ] Supporting documentation is current and consistent with responses
- [ ] Gap report identifies realistic remediation timelines
- [ ] Confidential information is appropriately redacted in shared documents
- [ ] Responses are consistent with the company's existing contractual obligations

### Escalation Triggers

- `CRITICAL` Customer requires certifications the company does not have and cannot obtain before deal deadline
- `HIGH` Customer identifies a compliance gap that represents actual regulatory non-compliance
- `HIGH` Customer requires terms the company's standard agreements do not support
- `MEDIUM` Significant gap between customer expectations and company's current posture

---

## Workflow 8: AI Intellectual Property Audit

### Trigger

The startup needs to assess its IP position related to AI — either for fundraising due diligence, M&A, enterprise customer requirements, or proactive IP strategy.

### Input

| Required Input | Format | Source |
|---|---|---|
| AI models used (third-party and proprietary) | List with details | Engineering |
| Training data sources and licenses | Inventory | Engineering / data team |
| AI-generated output types and uses | Description | Product |
| Employee/contractor IP assignment agreements | Agreements | HR / legal |
| Vendor/LLM provider agreements | Contracts | Legal |
| Patent applications (if any) | Filings | Legal |
| Open-source components used | Dependency list with licenses | Engineering |
| Customer contracts regarding AI IP | Agreements | Legal / sales |

### Legal Framework

| Law / Principle | Application |
|---|---|
| **Copyright Act (US 17 USC)** | Copyright ownership; work-for-hire; fair use |
| **Patent Act (US 35 USC)** | Inventorship requirements (human inventor) |
| **DTSA (18 USC §1836)** | Trade secret protection |
| **EU Copyright Directive** | Text and data mining exceptions (Art. 3-4) |
| **EU AI Act Art. 53(1)(c)** | GPAI provider copyright compliance |
| **Berne Convention** | International copyright protection |
| **Open source licenses** | GPL, MIT, Apache, etc. — compliance requirements |

### Process

**STEP 1 — IP Asset Inventory** `[15 min]`

Catalog all AI-related IP assets:

| Asset Category | Items to Inventory | Ownership Status |
|---|---|---|
| **Proprietary models** | Custom-trained models, fine-tuned models, adapter layers | Document: who built it, with what data, under what agreement |
| **Training datasets** | Curated datasets, labeled data, synthetic data | Document: source, license, any restrictions |
| **Algorithms & architectures** | Novel architectures, prompt engineering techniques, agent workflows | Document: human inventors, development records |
| **Software & code** | Application code, infrastructure code, tooling | Document: authorship, open-source dependencies |
| **AI-generated outputs** | Content, code, designs, analyses produced by AI | Document: what AI was used, what human contribution was made |
| **Trade secrets** | Proprietary methods, datasets, business logic | Document: protective measures in place |
| **Vendor-provided models** | Third-party models used under license | Document: license terms, usage restrictions, IP provisions |

**STEP 2 — Rights Chain Analysis** `[20 min]`

For each IP asset, trace the chain of rights:

2.1. **Who created it?**
- Employee → work-for-hire (check employment agreement includes IP assignment)
- Contractor → NOT work-for-hire by default (check contractor agreement for IP assignment)
- AI tool → copyright ownership uncertain; document human contribution
- Third-party vendor → check license/contract terms

2.2. **What rights do you have?**
- Full ownership (assignment)
- License (exclusive or non-exclusive; scope and restrictions)
- Fair use claim (document analysis)
- No rights (gap to address)

2.3. **What restrictions apply?**
- Open-source license obligations (copyleft: GPL → derivative works must be open; permissive: MIT/Apache → attribution required)
- Vendor license restrictions (model use limitations, output ownership provisions, training data restrictions)
- Customer contract obligations (who owns outputs generated for customers)

**STEP 3 — Training Data Audit** `[15 min]`

This is the highest-liability area. For each training data source:

| Data Source | License Type | Permits ML Training? | Permits Commercial Use? | Opt-Out Mechanism? | Risk Level |
|---|---|---|---|---|---|
| [Source] | [License] | Y/N/Unclear | Y/N | Y/N | LOW/MED/HIGH |

**Red flags:**
- Data scraped from websites without TOS review → `HIGH`
- Copyrighted works without license for ML training → `HIGH`
- Personal data used for training without consent/legal basis → `CRITICAL`
- No documentation of data provenance → `HIGH`
- Data sourced from jurisdictions with strict text-and-data-mining rules (EU without Art. 4 exception) → `MEDIUM`

**STEP 4 — Output IP Assessment** `[10 min]`

4.1. Assess copyrightability of AI-generated outputs under current law:
- US: Copyright requires human authorship; purely AI-generated works may not be copyrightable (Thaler v. Perlmutter; Copyright Office guidance)
- EU: Similar human authorship requirement under most member state laws
- Strategy: Document and maximize human creative contribution to strengthen copyright claims

4.2. Assess contractual IP position:
- Do vendor agreements confirm customer ownership of outputs? (Should be YES)
- Do customer agreements address IP ownership of outputs generated for them? (Must be clear)
- Does the LLM provider claim any rights to outputs? (Should be NO)

**STEP 5 — Gap Remediation Plan** `[10 min]`

For each identified gap:

| Gap | Risk | Remediation | Priority | Owner |
|---|---|---|---|---|
| Missing contractor IP assignment | HIGH | Execute IP assignment agreements | Immediate | Legal/HR |
| Unlicensed training data | HIGH | License or remove; document fair use analysis | Immediate | Legal/Eng |
| Vendor contract silent on output IP | MEDIUM | Negotiate AI addendum | Next renewal | Legal |
| No trade secret protection program | MEDIUM | Implement NDA, access controls, documentation | 30 days | Legal/Security |
| Open-source compliance gaps | MEDIUM | Audit and remediate license compliance | 60 days | Engineering |

### Output

| Deliverable | Format | Description |
|---|---|---|
| **IP Audit Report** | Structured document | Complete inventory of AI IP assets with ownership analysis |
| **Rights Chain Analysis** | Table per asset | Who owns what, under what authority |
| **Training Data Audit** | Spreadsheet | Every data source with license status and risk rating |
| **Gap Remediation Plan** | Action plan | Prioritized list of IP gaps with fixes |
| **IP Strategy Recommendations** | Memo | Strategic recommendations for strengthening IP position |

### Validation Criteria

- [ ] Every AI-related IP asset is inventoried
- [ ] Rights chain is traced for each asset (creator → assignment/license → current owner)
- [ ] Training data sources are documented with licensing status
- [ ] Open-source components are audited for license compliance
- [ ] Employee and contractor IP assignment agreements are confirmed
- [ ] Vendor contracts address output IP ownership
- [ ] Human contribution to AI-assisted works is documented
- [ ] Trade secret protections are assessed
- [ ] Gap remediation has assigned owners and deadlines

### Escalation Triggers

- `CRITICAL` Training data includes copyrighted works without license and product is in market
- `CRITICAL` Key contractor work has no IP assignment agreement
- `HIGH` Vendor claims ownership of outputs generated from your data
- `HIGH` Open-source copyleft license (GPL) may contaminate proprietary code
- `MEDIUM` AI-generated outputs are being claimed as copyrightable without documented human contribution

---

## Workflow 9: AI Incident Response & Breach Notification

### Trigger

An AI-specific security incident, data breach, model failure, or compliance violation has been detected or reported.

### Input

| Required Input | Format | Source |
|---|---|---|
| Incident description and timeline | Report | Security / engineering / any reporter |
| Affected systems and data | Assessment | Engineering / security |
| Affected individuals (data subjects, users, customers) | Count + categories | Engineering / customer success |
| Current containment status | Description | Security / engineering |
| Applicable contracts and notification obligations | List | Legal |
| Regulatory notification requirements | Assessment | Legal / compliance |
| Insurance policy details | Policy | Finance / legal |

### Legal Framework

| Law / Principle | Application |
|---|---|
| **GDPR Art. 33** | Notification to supervisory authority within 72 hours |
| **GDPR Art. 34** | Notification to data subjects when high risk to rights/freedoms |
| **CCPA §1798.150** | Private right of action for data breaches involving unencrypted/unredeemed PII |
| **State breach notification laws** | 50 US states have breach notification requirements with varying timelines |
| **EU AI Act Art. 73** | Serious incident reporting for high-risk AI systems (15 days) |
| **Contractual obligations** | Customer DPA/AI addendum notification timelines (typically 24-72 hours) |
| **SEC Cybersecurity Rules** | Material cybersecurity incident disclosure (if public company or affects public company customer) |
| **CAIA** | Notification to AG of discovered algorithmic discrimination within 90 days |

### Process

**STEP 1 — Incident Classification** `[IMMEDIATE — within 1 hour]`

Classify the incident type and severity:

| Incident Type | Examples | Base Severity |
|---|---|---|
| **AI Data Breach** | Personal data exposed through AI system; cross-tenant data leakage; training data leak | CRITICAL |
| **Adversarial Attack** | Prompt injection leading to data exfiltration; model manipulation; jailbreak with harmful output | HIGH-CRITICAL |
| **Model Failure** | Significant Model Drift; hallucination causing user harm; systematic bias discovered | HIGH |
| **Data Poisoning** | Compromised training data; poisoned model weights; corrupted RAG data | HIGH |
| **AI Compliance Violation** | AI making prohibited decisions; unauthorized data processing; failure of human oversight | HIGH |
| **Algorithmic Discrimination** | Discovery that AI system produces discriminatory outcomes | HIGH |
| **IP Infringement** | Discovery that AI outputs infringe third-party rights at scale | MEDIUM-HIGH |
| **Cost/Availability** | API cost explosion; recursive agent loop; DDoS on AI endpoints | MEDIUM |
| **Brand/Reputation** | AI produces offensive, false, or harmful public-facing content | MEDIUM-HIGH |

**STEP 2 — Notification Obligation Assessment** `[Within 4 hours]`

Determine all notification obligations:

| Obligation | Trigger | Timeline | Responsible |
|---|---|---|---|
| **Internal escalation** | All incidents | Immediate | Incident commander |
| **Customer notification** (contractual) | Per DPA/AI addendum terms | Typically 24-72 hours | Legal + customer success |
| **GDPR supervisory authority** | Personal data breach likely to result in risk to rights/freedoms | 72 hours from awareness | DPO / Legal |
| **GDPR data subjects** | Breach likely to result in HIGH risk to rights/freedoms | Without undue delay | DPO / Legal |
| **State breach notification** | Unauthorized access to unencrypted PII | Varies: 30-90 days depending on state | Legal |
| **EU AI Act serious incident** | High-risk AI system: death, serious damage to health/property/environment, fundamental rights | 15 days; 2 days if imminent danger | Legal / compliance |
| **CAIA AG notification** | Discovery that AI system causes algorithmic discrimination | 90 days | Legal |
| **Insurance carrier** | Per policy terms | Per policy (typically "prompt" or "as soon as practicable") | Legal / finance |
| **Law enforcement** | If criminal activity suspected | Per counsel advice | Legal |

**STEP 3 — Containment & Remediation** `[Parallel with Steps 1-2]`

3.1. **Immediate containment:**
- Isolate affected AI system if ongoing exposure risk
- Revoke compromised credentials/tokens
- Block malicious inputs if adversarial attack
- Disable affected AI features if compliance violation
- Preserve evidence (logs, model state, input/output records)

3.2. **Investigation:**
- Determine root cause
- Assess full scope of impact (data subjects affected, data exposed, decisions tainted)
- Determine whether the incident is contained or ongoing
- Document timeline with precision

3.3. **Remediation:**
- Implement technical fix
- Update security controls
- Re-test and validate
- Update threat model

**STEP 4 — Notification Drafting** `[Per timeline requirements]`

For each required notification, draft content covering:

| Element | Content |
|---|---|
| Nature of the incident | What happened, when, how |
| Categories of data/individuals affected | Types of data; approximate number of subjects |
| Contact information | DPO or privacy team contact |
| Consequences | Likely consequences of the breach |
| Measures taken | Containment and remediation steps |
| Measures recommended | What affected individuals should do |

**For GDPR Art. 33 notification to supervisory authority:**
- Must be submitted within 72 hours of becoming "aware"
- If full information is not available, may submit in phases
- Document reasons for any delay beyond 72 hours

**For customer contractual notification:**
- Follow exact format and timeline specified in DPA/AI addendum
- Typically: nature of breach, data affected, measures taken, cooperation commitment

**STEP 5 — Post-Incident Review** `[Within 14 days]`

5.1. Conduct root cause analysis
5.2. Update threat model with lessons learned
5.3. Update incident response procedures
5.4. Implement preventive measures
5.5. Brief leadership and board (if material)
5.6. Document everything for regulatory and litigation defense

### Output

| Deliverable | Format | Description |
|---|---|---|
| **Incident Classification Report** | Structured document | Type, severity, scope, and timeline |
| **Notification Obligation Matrix** | Table | All notification requirements with timelines and status |
| **Notification Letters/Filings** | Per requirements | Supervisory authority, data subjects, customers, regulators |
| **Containment & Remediation Report** | Technical document | What was done, when, by whom |
| **Post-Incident Review** | Memo | Root cause, lessons learned, preventive measures |
| **Updated Threat Model** | Revised document | Threat model updated with incident findings |

### Validation Criteria

- [ ] Incident is classified within 1 hour of detection
- [ ] All notification obligations are identified within 4 hours
- [ ] GDPR supervisory authority is notified within 72 hours (if applicable)
- [ ] Customer notifications meet contractual timelines
- [ ] All notifications contain required legal elements
- [ ] Evidence is preserved for regulatory and litigation defense
- [ ] Post-incident review is completed within 14 days
- [ ] Threat model and IR plan are updated

### Escalation Triggers

- `CRITICAL` Personal data breach affecting >1,000 individuals with high risk to rights/freedoms
- `CRITICAL` AI system caused physical harm or death (EU AI Act Art. 73 serious incident)
- `CRITICAL` Cross-tenant data exposure in multi-customer system
- `HIGH` Regulatory notification deadline is approaching without ready filing
- `HIGH` Algorithmic discrimination discovered in production system
- `MEDIUM` Insurance carrier notification timeline approaching

---

## Workflow 10: AI Regulatory Change Impact Analysis

### Trigger

A new AI law, regulation, amendment, guidance document, enforcement action, or court decision is identified that may affect the startup's AI products, services, or operations.

### Input

| Required Input | Format | Source |
|---|---|---|
| The regulatory change (full text or summary) | Document / link | Legal / compliance / Kevin monitoring |
| Current compliance posture | SKILL.md outputs | Legal |
| Affected products and services | List | Product / engineering |
| Affected jurisdictions | List | Business / legal |
| Current contracts and obligations | Relevant agreements | Legal |
| Implementation timeline of the change | Dates | Legal analysis |

### Legal Framework

The framework for this workflow IS the regulatory change being analyzed, assessed against the startup's existing obligations under all laws tracked in SKILL.md Section 3.

### Process

**STEP 1 — Change Identification & Summary** `[10 min]`

1.1. Identify the source and authority:

| Source Type | Weight | Examples |
|---|---|---|
| **Enacted legislation** | Binding | EU AI Act amendments, CAIA, new state laws |
| **Final regulation / rule** | Binding | Implementing regulations, FTC rules |
| **Proposed legislation / rule** | Monitor | Bills in progress, proposed regulations |
| **Regulatory guidance** | Influential | EDPB guidelines, ICO guidance, FTC blog posts |
| **Enforcement action** | Precedential | FTC consent orders, GDPR fines, state AG actions |
| **Court decision** | Precedential | Federal/state court rulings on AI liability, IP, privacy |
| **Industry standard update** | Best practice | NIST AI RMF updates, ISO/IEC 42001 revisions |

1.2. Summarize the change in plain language: what changed, who it affects, when it takes effect, and what the penalties are for non-compliance.

**STEP 2 — Applicability Assessment** `[10 min]`

For each of the startup's AI products/services, determine:

| Question | Analysis |
|---|---|
| Does this change apply to our jurisdiction(s)? | [Assessment based on where the startup operates and where its users are] |
| Does this change apply to our AI system type? | [Assessment based on risk classification, use case, model type] |
| Does this change apply to our role? | [Assessment based on whether startup is provider, deployer, distributor, importer] |
| Are there exemptions that apply to us? | [Assessment: startup size, sandbox participation, transitional provisions] |
| What is the effective date? | [Date with compliance runway calculation] |

**STEP 3 — Gap Analysis Against Current Posture** `[15 min]`

Compare new requirements against current compliance status:

| New Requirement | Current Status | Gap? | Severity |
|---|---|---|---|
| [Requirement 1] | [What we currently do] | Y/N | LOW/MED/HIGH/CRIT |
| [Requirement 2] | [What we currently do] | Y/N | LOW/MED/HIGH/CRIT |
| ... | ... | ... | ... |

**STEP 4 — Impact Assessment** `[15 min]`

For each identified gap, assess:

| Impact Dimension | Assessment |
|---|---|
| **Product** | Does this require product changes (features, disclosures, controls)? |
| **Engineering** | Does this require technical implementation (new controls, monitoring, documentation)? |
| **Legal/Contracts** | Do contracts need to be updated (AI addendum, DPA, ToS, privacy notice)? |
| **Operations** | Do internal processes need to change (policies, training, governance)? |
| **Financial** | What is the cost of compliance? What is the cost of non-compliance (fines, lost deals)? |
| **Timeline** | Can we comply by the effective date? If not, what interim measures are available? |

**STEP 5 — Remediation Roadmap** `[10 min]`

5.1. Prioritize changes by: (a) legal deadline, (b) severity of non-compliance, (c) customer impact, (d) implementation effort.

5.2. Create phased implementation plan:

| Phase | Timeline | Actions |
|---|---|---|
| **Immediate** (0-30 days) | Before effective date or ASAP | Critical compliance gaps; contract updates for new deals |
| **Short-term** (30-90 days) | Within first quarter | Product changes; policy updates; training |
| **Medium-term** (90-180 days) | Within two quarters | Full technical implementation; retroactive contract updates |
| **Long-term** (180+ days) | Ongoing | Monitoring; optimization; audit preparation |

5.3. Assign ownership for each action item.

**STEP 6 — Stakeholder Communication** `[5 min]`

6.1. Draft internal briefing for leadership: what changed, what it means for us, what we need to do, what it costs, what the risk of non-action is.

6.2. If the change affects customers: draft customer communication explaining any changes to services, terms, or practices.

6.3. Update Kevin's regulatory tracking in SKILL.md Appendix A.

### Output

| Deliverable | Format | Description |
|---|---|---|
| **Regulatory Change Brief** | 1-2 page memo | Plain-language summary of the change and its applicability |
| **Gap Analysis** | Table | New requirements vs. current posture with gap identification |
| **Impact Assessment** | Structured analysis | Product, engineering, legal, operational, financial, and timeline impacts |
| **Remediation Roadmap** | Phased action plan | Prioritized actions with owners and deadlines |
| **Stakeholder Briefing** | Memo / presentation | Communication for leadership and affected teams |
| **Updated Compliance Calendar** | Calendar | Revised regulatory deadlines |

### Validation Criteria

- [ ] The regulatory change is correctly characterized (binding vs. guidance vs. proposed)
- [ ] Applicability assessment considers all relevant factors (jurisdiction, AI type, role, exemptions)
- [ ] Gap analysis covers every new requirement
- [ ] Impact assessment addresses all dimensions (product, engineering, legal, operations, financial, timeline)
- [ ] Remediation roadmap is realistic given available resources
- [ ] Every action item has an owner and deadline
- [ ] Compliance calendar is updated

### Escalation Triggers

- `CRITICAL` New law makes the startup's core AI functionality illegal or prohibited
- `CRITICAL` Compliance deadline is within 30 days and major gaps exist
- `HIGH` New enforcement action targets a competitor with similar AI practices
- `HIGH` New law creates personal liability for officers/directors related to AI governance
- `MEDIUM` Proposed legislation could significantly affect business model if enacted

---

## Appendix: Workflow Dependencies

Some workflows feed into others. Here is the dependency map:

```
Workflow 2 (Risk Classification)
  └──→ Workflow 3 (DPA Drafting) — classification determines DPA scope
  └──→ Workflow 5 (Privacy Notice) — classification drives disclosure requirements
  └──→ Workflow 6 (Threat Model) — classification sets security requirements

Workflow 4 (Internal Policy)
  └──→ Workflow 7 (Enterprise Due Diligence) — policy is a required deliverable

Workflow 6 (Threat Model)
  └──→ Workflow 9 (Incident Response) — threat model defines incident types
  └──→ Workflow 1 (Contract Review) — threat model informs contractual security requirements

Workflow 8 (IP Audit)
  └──→ Workflow 1 (Contract Review) — IP position informs negotiation strategy
  └──→ Workflow 7 (Enterprise Due Diligence) — IP audit supports customer questionnaires

Workflow 10 (Regulatory Change)
  └──→ ALL WORKFLOWS — regulatory changes may trigger updates to any workflow output
```

---

*Kevin Workflows v1.0 — March 2026*

*Each workflow produces audit-ready output. But Kevin reminds you: have a licensed attorney review anything before it goes out the door.*
