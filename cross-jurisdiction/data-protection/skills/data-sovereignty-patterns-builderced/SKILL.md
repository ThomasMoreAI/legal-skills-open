---
name: data-sovereignty-patterns-builderced
title: Data Sovereignty Patterns
description: Navigate cross-border data transfer rules — Schrems II, EU SCCs, adequacy decisions, data localization requirements for EU, US, Brazil, and other jurisdictions.
author: BuilderCed
author_url: https://github.com/BuilderCed/agent-skills/tree/main/skills/sovereignty/data-sovereignty-patterns
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
---

# Data Sovereignty Patterns

> **DISCLAIMER**: Guidance only. Cross-border data transfers require legal assessment specific to your situation.

## When to Use

- Choosing cloud providers (data residency requirements)
- Using AI APIs that process data outside the EU
- Designing data architecture for multi-region deployments
- Assessing compliance for international data flows
- Responding to data localization requirements

## EU → Non-EU Transfer Mechanisms

After Schrems II (CJEU C-311/18), transferring personal data outside the EEA requires:

### 1. Adequacy Decisions (Easiest)
Countries deemed adequate by the European Commission:

| Country | Decision Date | Notes |
|---------|--------------|-------|
| UK | 2021 (renewed) | Post-Brexit, includes sunset clause |
| Japan | 2019 | Mutual adequacy |
| South Korea | 2022 | Comprehensive |
| USA | 2023 (EU-US DPF) | Data Privacy Framework, requires self-certification |
| Canada | 2001 | Commercial only (PIPEDA) |
| Switzerland | 2000 | Comprehensive |
| Israel | 2011 | Comprehensive |
| New Zealand | 2012 | Comprehensive |
| Argentina | 2003 | Comprehensive |
| Uruguay | 2012 | Comprehensive |

For adequate countries: transfer freely, no additional mechanism needed.

### 2. Standard Contractual Clauses (SCCs)
For non-adequate countries, use EU-approved SCC templates:

| Module | Scenario |
|--------|----------|
| Module 1 | Controller → Controller |
| Module 2 | Controller → Processor (most common: you → cloud provider) |
| Module 3 | Processor → Sub-processor |
| Module 4 | Processor → Controller |

**Required**: Transfer Impact Assessment (TIA) evaluating recipient country laws.

### 3. Binding Corporate Rules (BCRs)
For intra-group transfers within multinational companies. Complex, expensive, long approval (~18 months).

## Data Localization by Region

| Region | Requirement | Affected Data |
|--------|-------------|---------------|
| EU/EEA | Transfer mechanism required for export | Personal data (GDPR) |
| Russia | Localization of Russian citizens' data | Personal data |
| China | Security assessment for cross-border transfers | Personal data + "important data" |
| India | Proposed localization (DPDP Act 2023) | Sensitive personal data |
| Brazil | Similar to GDPR (LGPD) | Personal data, adequacy or SCCs |
| Saudi Arabia | Localization for certain sectors | Government, health, finance |
| Turkey | Explicit consent or BCR for transfers | Personal data |

## Architecture Patterns

### Pattern 1: EU-Only Deployment
Deploy all infrastructure in EU. Simplest compliance.
- Cloud: eu-west-1, eu-central-1, eu-north-1
- AI APIs: Use EU-hosted endpoints (Anthropic EU, Azure EU OpenAI)
- Database: Supabase EU, Neon EU, PlanetScale EU

### Pattern 2: Data Residency with Global Compute
- Store personal data in EU
- Process with EU-hosted compute
- Non-personal data can be global
- Use anonymization/pseudonymization before cross-border transfer

### Pattern 3: Multi-Region with SCCs
- SCCs in place with all non-EU processors
- TIA completed per destination country
- Regular review of adequacy decisions
- Data mapping documenting all flows

## AI-Specific Considerations

| AI Service | Data Flow | Mechanism Needed |
|-----------|-----------|-----------------|
| Claude API (Anthropic) | EU → US | EU-US DPF (if Anthropic self-certified) or SCCs |
| OpenAI API | EU → US | EU-US DPF or SCCs |
| Ollama (local) | No transfer | None (local processing) |
| Azure OpenAI (EU) | EU → EU | None (intra-EEA) |
| Google Vertex (EU) | EU → EU | None (if EU region selected) |

## What This Skill Does NOT Do

- Does not draft SCCs or BCRs (use lawyer)
- Does not perform Transfer Impact Assessments
- Does not track adequacy decision changes in real-time
- Does not cover sector-specific rules (health, finance, defense)
