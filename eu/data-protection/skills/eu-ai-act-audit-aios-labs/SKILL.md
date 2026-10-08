---
name: eu-ai-act-audit-aios-labs
title: EU AI Act Compliance Audit
description: Perform a full codebase audit for EU AI Act (Regulation 2024/1689) compliance. This skill scans the project for AI systems, classifies risk levels, checks transparency and GDPR obligations article-by-article, and produces a prioritized remediation report with file:line references. Use this skill when the user wants a comprehensive compliance review of their project against European AI regulation — e.g., "revisa si este proyecto cumple el AI Act", "audit this repo for EU AI Act compliance", "cumple mi proyecto la ley de IA europea", "what do we need for AI Act before August 2026". This skill is for full project audits that require scanning code, reading legal pages, and producing structured reports. Do NOT use for quick factual questions about specific AI Act articles, risk categories, or obligations — Claude can answer those directly without this skill.
author: aios-labs
author_url: https://github.com/aios-labs/eu-ai-act-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
sources:
- title: High Risk Obligations
  path: references/high-risk-obligations.md
- title: Risk Classification
  path: references/risk-classification.md
---

# EU AI Act Compliance Audit

Perform a structured compliance audit of a software project against the EU AI Act (Regulation (EU) 2024/1689). The audit produces a prioritized report with risk classification, article-by-article compliance status, and actionable remediation steps.

## Why this matters

The EU AI Act is the world's first comprehensive AI regulation. Non-compliance carries fines up to 35M EUR or 7% of global annual turnover. Obligations are phased in — some are already in force, others take effect in August 2026.

## Audit workflow

Follow these steps in order. Be thorough but efficient — skip steps that clearly don't apply.

### Step 1: Research latest regulatory context

Before diving into the codebase, fetch the latest guidance and updates. The AI Act is actively being implemented, with new guidance, codes of practice, and delegated acts being published regularly.

**Search for the latest updates using WebSearch:**

1. Search `EU AI Act 2026 latest guidance implementation` to find recent updates from the EU AI Office
2. Search `EU AI Act Code of Practice transparency AI-generated content` for the latest draft of the transparency code
3. If the project involves a specific domain (healthcare, education, employment, etc.), search for sector-specific guidance

**Key authoritative sources to check with WebFetch when relevant:**

| Source | URL | What it provides |
|---|---|---|
| EU AI Act full text | `https://artificialintelligenceact.eu/` | Article-by-article text with annotations |
| Article 50 (transparency) | `https://artificialintelligenceact.eu/article/50/` | Detailed transparency obligations |
| Implementation timeline | `https://artificialintelligenceact.eu/implementation-timeline/` | Current enforcement dates |
| EU Commission AI page | `https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai` | Official policy updates |
| Compliance checker | `https://artificialintelligenceact.eu/assessment/eu-ai-act-compliance-checker/` | Interactive assessment tool |
| Navigating the AI Act FAQ | `https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act` | Official FAQ from the Commission |
| GPAI guidelines | `https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers` | Obligations for GPAI model providers |
| Code of Practice on transparency | `https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content` | Draft code for AI content marking |

Fetch 2-3 of the most relevant sources based on what the project does. Don't fetch all of them — focus on what matters for the specific project being audited.

### Step 2: Discover AI systems in the project

Search the codebase broadly for any AI/ML usage.

**Direct indicators** (packages, imports, API calls):
- LLM providers: `openai`, `anthropic`, `@ai-sdk`, `langchain`, `llamaindex`, `openrouter`, `huggingface`, `cohere`, `mistral`, `groq`, `together`, `replicate`, `bedrock`, `claude`, `gpt`
- ML frameworks: `tensorflow`, `pytorch`, `torch`, `scikit-learn`, `sklearn`, `transformers`, `onnx`, `mlflow`
- AI SDKs: `ai`, `vercel/ai`, `assistant-ui`, `copilotkit`
- Vector/embeddings: `pinecone`, `weaviate`, `chromadb`, `pgvector`, `embedding`

**Indirect indicators** (features that may use AI):
- Chat/assistant interfaces, chatbots, conversational UI
- Recommendation engines, content personalization
- Automated moderation, content filtering, spam detection
- Predictive analytics, scoring, classification, ranking
- Image/video/audio generation or analysis
- Search with semantic/AI-powered ranking

**Where to look**: `package.json`, `requirements.txt`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `.env*`, API routes, middleware, config files, system prompts, model configs.

For each AI system found, document:
- What model/service it uses and how (API, self-hosted, fine-tuned)
- What it does (purpose, functionality)
- Who interacts with it (internal users, general public, specific groups)
- What data flows through it (user inputs, outputs, any data stored)
- Whether it makes or influences decisions about people

If no AI systems are found, report that the project has no AI Act obligations and stop.

### Step 3: Determine the organization's role

For each AI system, classify the organization's role:

| Role | Definition | Typical case |
|---|---|---|
| **Provider** | Develops the AI system and places it on the market under their name | You train/fine-tune a model and deploy it as a product |
| **Deployer** | Uses an AI system under their authority (not personal use) | You integrate GPT/Claude/etc. into your app |
| **Importer** | Places a non-EU AI system on the EU market | You distribute a US-built AI tool in EU |
| **Distributor** | Makes an AI system available without modifying it | You resell an AI product as-is |

Most projects using third-party LLM APIs are **deployers**. If the project significantly modifies model behavior (fine-tuning, custom training), it may qualify as a provider.

### Step 4: Classify risk level

Read `references/risk-classification.md` for the full Annex III categories. Classify each AI system into one of four risk levels:

| Level | Key triggers | Main obligations |
|---|---|---|
| **Prohibited** (Art. 5) | Social scoring, subliminal manipulation, exploitation of vulnerabilities, real-time biometric ID in public spaces, emotion recognition at work/school (with exceptions) | Cannot be deployed — must be removed |
| **High-risk** (Annex III) | Biometrics, critical infrastructure, education access, employment decisions, essential public/private services, law enforcement, migration, justice administration | Full compliance framework (Arts. 9-15, 17, 26, 27) |
| **Limited risk** (Art. 50) | Chatbots interacting with people, AI-generated content, emotion recognition, deepfakes | Transparency and disclosure obligations |
| **Minimal risk** | Everything else | No specific AI Act obligations (Art. 4 AI literacy still applies) |

An informational chatbot that doesn't make decisions about people's rights or access to services is typically **limited risk**. However, if it operates in an Annex III domain or influences individual decisions, escalate the classification.

### Step 5: Check applicable obligations

Based on risk level and role, audit each requirement. Use these tables for structured reporting.

#### For ALL AI systems (any risk level):

| Requirement | Article | In force | What to check |
|---|---|---|---|
| AI literacy | Art. 4 | Feb 2, 2025 | Staff operating/overseeing AI have adequate training. Look for training docs, policies, or internal guidelines |

#### For limited-risk systems (chatbots, generative AI):

| Requirement | Article | In force | What to check |
|---|---|---|---|
| AI interaction disclosure | Art. 50(1) | Aug 2, 2026 | Users must be clearly informed they're interacting with AI — prominently, before or at start of interaction. Not buried in footer or fine print |
| AI-generated content marking | Art. 50(2) | Aug 2, 2026 | Content must be marked as AI-generated in machine-readable format (metadata, watermarking) where technically feasible |
| Deepfake labeling | Art. 50(4) | Aug 2, 2026 | Synthetic media resembling real people/events must be disclosed |

When checking transparency, search the latest Code of Practice using WebSearch: `EU AI Act Code of Practice transparency marking labeling` — as the final code may have been published with specific technical requirements.

#### For high-risk systems:

Read `references/high-risk-obligations.md` for the detailed checklist. Key areas: risk management (Art. 9), data governance (Art. 10), technical documentation (Art. 11), logging (Art. 12), transparency to deployers (Art. 13), human oversight (Art. 14), accuracy/robustness/security (Art. 15), quality management (Art. 17), FRIA for public bodies (Art. 27).

#### GPAI model obligations (Chapter V):

These obligations fall primarily on the **model provider** (OpenAI, Anthropic, Google, etc.), not on deployers. As a deployer, verify:
- Your provider publishes model documentation per Art. 53
- Your provider has a copyright compliance policy
- For systemic risk models: provider conducts adversarial testing (Art. 55)

Use WebSearch to check: `[provider name] EU AI Act GPAI compliance` — major providers are publishing compliance pages.

### Step 6: Check GDPR intersections

The AI Act works alongside GDPR. For AI systems processing personal data:

| Check | Detail |
|---|---|
| Privacy policy covers AI | Does it mention the AI system, data processed, purpose, and legal basis? |
| Legal basis stated | Consent, legitimate interest, or contractual necessity for AI data processing? |
| International transfers | If data goes to non-EU servers (common with US LLM APIs), are there SCCs or adequacy decisions? |
| Data subject rights | Can users access, correct, or delete their AI-processed data? |
| DPIA conducted | For high-risk processing, is there a Data Protection Impact Assessment? |

### Step 7: Review technical safeguards

| Safeguard | What to look for in code |
|---|---|
| Input validation | Inputs sanitized before reaching AI (injection prevention, rate limiting) |
| Output constraints | Token limits, content filters, read-only DB access, response boundaries |
| Human oversight | Kill switch, human-in-the-loop for critical decisions, override capability |
| Logging | AI interactions logged for audit trail (not just console.log — persistent storage) |
| Error handling | Graceful degradation when AI service fails |
| Guardrails | System prompts preventing harmful outputs, content policies |

### Step 8: Accessibility check (complementary)

Not part of the AI Act itself, but public-sector digital services in the EU must comply with the Web Accessibility Directive (2016/2102). Flag if:
- The AI interface lacks WCAG 2.1 AA compliance
- No accessibility statement exists
- Screen reader support is insufficient
- The accessibility link was removed or is missing

## Report format

Write the report in the same language the user used to request the audit. Use this structure:

```
# EU AI Act Compliance Audit — [Project Name]

## 1. AI Systems Identified
For each system: name, model/service, purpose, users, org role (provider/deployer)

## 2. Risk Classification
For each system: risk level, reasoning, which Annex III category (if high-risk)

## 3. Compliance Status
| Requirement | Article | Status | Detail |
Status: COMPLIANT / PARTIAL / NON-COMPLIANT / NOT APPLICABLE / NOT VERIFIABLE

## 4. Findings (by priority)

### High Priority (blocking — must fix before applicable deadline)
Numbered, with file:line references where possible

### Medium Priority (should address before deadline)
...

### Low Priority (recommendations / best practices)
...

## 5. Summary
| Area | Rating |
2-3 sentence conclusion with key deadlines and next steps

## Sources
Links to the regulatory sources consulted during the audit
```

## Important guidelines

- **Be precise about legal requirements vs. recommendations.** The AI Act has specific obligations with specific deadlines. Clearly distinguish "the law requires X" from "it would be good practice to do Y."
- **Check the current date against the timeline.** If it's before August 2, 2026, some transparency obligations aren't yet enforceable — but flag them as upcoming.
- **Don't burden deployers with provider obligations.** Most GPAI model compliance (Art. 53-55) is the provider's responsibility.
- **Flag public bodies.** Government-linked projects face additional scrutiny (FRIA under Art. 27) and accessibility requirements.
- **Reference specific articles and paragraphs.** Don't just say "transparency requirements" — cite Art. 50(1) for chatbot disclosure, Art. 50(2) for content marking, etc.
- **Give actionable code-level fixes.** When finding non-compliance in the codebase, reference specific files and lines, and suggest concrete changes.
