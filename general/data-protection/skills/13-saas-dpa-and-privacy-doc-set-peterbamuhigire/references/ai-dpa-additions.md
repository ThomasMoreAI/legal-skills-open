# AI-Specific DPA and Privacy Doc Additions

When the SaaS ships AI features, the DPA and privacy doc set MUST add the AI clauses below.

## 1. DPA Schedule -- AI Processing

Add a Schedule (e.g. Schedule 5: AI Processing) covering:

### 1.1 Categories of AI processing

- LLM-based generation, retrieval-augmented generation, classification, embedding-based search, agent workflows.

### 1.2 AI sub-processors

- Cross-reference the AI sub-processor list (see Trust Center pack).
- 30 days advance notice on additions; right of objection.

### 1.3 Training-data exclusion

```
Processor shall ensure that Customer Personal Data, Customer Content, and any prompts or responses derived therefrom shall NOT be used by any AI sub-processor to train, fine-tune, or otherwise improve any AI model that is not exclusively dedicated to Customer's account. Processor shall maintain contractual and technical controls (including provider no-training endpoints where available) to enforce this exclusion and shall provide evidence of such controls upon Customer's reasonable request.
```

### 1.4 Conversation log retention

- Per-tenant partition.
- Retention: 90 d hot, 13 mo cold; configurable shorter on request.
- Deletion on offboarding within 30 days.

### 1.5 Automated decision-making (GDPR Art. 22 / POPIA s.71)

```
Where the Service is used by Customer to make automated decisions producing legal or similarly significant effects on data subjects, Customer shall be solely responsible for the lawful basis under Art. 22 GDPR and for providing meaningful information about the logic involved and the significance and envisaged consequences of such processing. Processor shall provide reasonable assistance with such information requests where the underlying logic of Processor-provided AI features is within Processor's knowledge.
```

### 1.6 Right to explanation

Processor shall provide, on Customer or data-subject request, the operational pins (model + version, prompt registry tag, retrieval index version) for any AI output that is the subject of a request, subject to confidentiality protections.

### 1.7 AI incident notification

AI-quality incidents that affect data-subject rights (cross-tenant leakage, mass-scale hallucination affecting persons, biased decision incident) are notifiable within 72 hours per GDPR Art. 33 and parallel local laws (Kenya DPA, Nigeria DP Act 2023, POPIA).

### 1.8 Audit and evidence

Processor maintains and provides on request:

- AI Architecture Spec summary.
- AI Data Spec summary.
- Per-feature Model Card.
- Eval and red-team latest reports (summary form).
- Provider training-exclusion audit evidence (most recent).
- Hallucination SLO most recent compliance summary.

### 1.9 Customer obligations

Customer warrants:

- Lawful basis under Art. 6 (and Art. 9 where special category) for content processed through AI features.
- Notice to data subjects where required.
- No use of AI features for prohibited purposes under EU AI Act Art. 5 or any local equivalent.
- Where the use of AI features is high-risk under EU AI Act Annex III, Customer signs the Annex III addendum and bears the deployer obligations under Art. 26.

## 2. Privacy Policy AI Addendum

Add a section in the public privacy policy:

- What AI features we offer.
- Which data goes to providers.
- Training-data exclusion commitment.
- Retention.
- How to contact us about an AI output.

Copy library lives at `09-governance-compliance/15-ai-act-and-regulatory-compliance-doc/references/ai-disclosure-copy-library.md`.

## 3. DPIA reference

Cross-link the AI DPIA artefact at `09-governance-compliance/16-ai-data-flow-and-dpia/` for any customer Art. 35 / Art. 36 process.

## Cross-links

- Trust Center AI additions: `09-governance-compliance/12-saas-trust-center-document-pack/references/ai-trust-center-additions.md`
- Responsible AI Declaration: `09-governance-compliance/14-ai-responsible-ai-declaration/`
- AI Regulatory Compliance Doc: `09-governance-compliance/15-ai-act-and-regulatory-compliance-doc/`
- AI Data Flow & DPIA: `09-governance-compliance/16-ai-data-flow-and-dpia/`
