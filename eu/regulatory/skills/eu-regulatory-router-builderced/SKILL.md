---
name: eu-regulatory-router-builderced
title: EU Regulatory Router
description: Identify which EU regulations (AI Act, NIS2, DORA, GDPR) apply to your system based on sector, data types, and entity size, then route to the right compliance skill.
author: BuilderCed
author_url: https://github.com/BuilderCed/agent-skills/tree/main/skills/compliance/eu-regulatory-router
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# EU Regulatory Router

> **DISCLAIMER**: This skill provides guidance only. It does not constitute legal advice. Regulatory applicability depends on specific circumstances that require qualified legal assessment.

## When to Use

- Starting a new project and unsure which EU regulations apply
- Assessing regulatory exposure for an existing system
- Preparing for compliance audits
- When multiple regulations might overlap

## Decision Tree

### Question 1: Does your system process personal data?
- **YES** → GDPR applies. Use `gdpr-data-protection`.
- **NO** → Skip GDPR. Continue.

### Question 2: Does your system use AI/ML models?
- **YES** → AI Act likely applies. Use `eu-ai-act-compliance` to classify risk.
- **NO** → Skip AI Act. Continue.

### Question 3: Is your organization in a NIS2 sector?
Essential: Energy, transport, banking, health, water, digital infrastructure, ICT management, public admin, space.
Important: Postal, waste, chemicals, food, manufacturing, digital providers, research.
- **YES** + medium/large entity → NIS2 applies. Use `eu-nis2-compliance`.
- **NO** → Skip NIS2. Continue.

### Question 4: Is your organization a financial entity?
Banking, investment, insurance, pension, crypto, infrastructure.
- **YES** → DORA applies. Use `eu-dora-compliance`.
- **NO** → Skip DORA.

## Overlap Scenarios

| Scenario | Regulations | Priority |
|----------|-------------|----------|
| Fintech with AI chatbot | GDPR + AI Act + DORA | All three. DORA for resilience, AI Act for chatbot, GDPR for data. |
| Hospital with AI diagnostics | GDPR + AI Act + NIS2 | AI Act HIGH-RISK (health). NIS2 for cybersecurity. GDPR for patient data. |
| SaaS for SMEs (non-financial) | GDPR | Usually GDPR only. NIS2 if digital infrastructure. |
| Cloud provider | GDPR + NIS2 | NIS2 as digital infrastructure. GDPR as processor. |
| E-commerce with recommendations | GDPR + AI Act (limited risk) | GDPR for customer data. AI Act transparency for recommendations. |

## Regulatory Collision Warning

When an AI security incident occurs at a financial institution, it can trigger ALL FOUR regulations simultaneously:
- **DORA**: ICT incident reporting (4h + 72h + 1 month)
- **NIS2**: Significant incident reporting (24h + 72h + 1 month)
- **AI Act**: If AI system involved, conformity breach
- **GDPR**: If personal data affected, data breach notification (72h)

**Coordinate reporting timelines** — the strictest deadline governs.

## What This Skill Does NOT Do

- Does not provide legal certainty on regulatory applicability
- Does not handle national transposition differences
- Does not cover sector-specific regulations (e.g., MiCA for crypto beyond DORA)
- Does not replace legal counsel assessment
