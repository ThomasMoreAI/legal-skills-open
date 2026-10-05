---
name: eu-ai-act-quick-check-knowledgepa3
title: EU AI Act Quick Check — Free Tier
description: Quick EU AI Act risk classification for any AI system. Screens prohibited practices (Article 5), classifies high-risk systems (Annex III), and estimates penalty exposure. Powered by GIA.
author: knowledgepa3
author_url: https://github.com/knowledgepa3/gia-eu-ai-act/tree/main/skills/eu-ai-act-quick-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# EU AI Act Quick Check — Free Tier
**Powered by GIA — Governance Intelligence Automation**
**Author:** Advanced Consulting Experts, LLC

---

## What This Does

This free tool classifies any AI system under the EU AI Act (Regulation 2024/1689). It answers the three most critical questions:

1. Is this system **prohibited** under Article 5?
2. Is this system **high-risk** under Annex III?
3. What are the **potential fines** if non-compliant?

## How to Use

Ask the user to describe their AI system. Then run through the assessment below.

---

## Phase 1: Prohibited Practice Screen (Article 5)

Check the system against ALL 8 prohibited categories. A match means the system CANNOT be deployed in the EU.

Ask these questions:

1. Does it use subliminal techniques to materially distort behavior or decision-making?
2. Does it exploit vulnerabilities of specific groups (age, disability, socio-economic status)?
3. Does it perform social scoring that leads to detrimental treatment?
4. Does it categorize individuals by biometric data based on sensitive/protected characteristics?
5. Does it perform emotion recognition in workplace or education settings?
6. Does it perform real-time remote biometric identification in public spaces?
7. Does it scrape facial images from the internet or CCTV for database building?
8. Does it assess or predict likelihood of criminal offenses based solely on profiling?

**If ANY answer is YES:** Stop. The system is PROHIBITED. Fines up to 7% of global annual turnover or EUR 35M (whichever is higher).

**If ALL answers are NO:** Proceed to Phase 2.

---

## Phase 2: High-Risk Classification (Annex III)

Check the system against all 8 Annex III categories:

| Category | Area | Examples |
|----------|------|----------|
| Point 1 | Biometrics | Remote biometric ID, categorization, emotion recognition |
| Point 2 | Critical Infrastructure | Digital infrastructure, road traffic, water/gas/electricity |
| Point 3 | Education | Admissions, outcomes evaluation, exam monitoring |
| Point 4 | Employment | Recruitment, CV screening, performance evaluation |
| Point 5 | Essential Services | Social benefits, healthcare triage, credit scoring, insurance |
| Point 6 | Law Enforcement | Risk assessment, evidence evaluation, profiling |
| Point 7 | Migration/Border | Asylum assessment, border risk, document verification |
| Point 8 | Justice/Democracy | Judicial support, evidence evaluation, voting systems |

Also check the Safety Component Rule (Art. 6(1)):
- Is the system a safety component of a product covered by EU harmonization legislation?

**CRITICAL:** If the system profiles individuals in any way, it is HIGH-RISK regardless of exemptions.

---

## Phase 3: Penalty Exposure

Calculate fines based on the classification:

| Violation Type | Fine |
|---------------|------|
| Prohibited Practices (Art. 5) | 7% of global annual turnover or EUR 35M |
| High-Risk Non-Compliance (Art. 9-15) | 3% of global annual turnover or EUR 15M |
| False Information to Authorities | 1% of global annual turnover or EUR 7.5M |

Ask the user for their approximate global annual revenue. Calculate exposure for each applicable tier.

**SME Rule:** Fines capped at lower percentage for small/micro enterprises.

---

## Output Format

Present results as:

EU AI ACT QUICK CHECK RESULTS
==============================

System: [name]
Classification: [PROHIBITED / HIGH-RISK / LIMITED-RISK / MINIMAL-RISK]
Annex III Category: [if applicable]
Penalty Exposure: [calculated amount]

Key Finding: [one-sentence summary]

Days Until Enforcement: [calculate days to August 2, 2026]

---

## Key Dates

| Date | Milestone |
|------|-----------|
| Already Active | Prohibited practices (Art. 5) enforceable NOW |
| **August 2, 2026** | **ALL high-risk requirements enforceable** |
| August 2, 2027 | High-risk AI in regulated products |

---

## What's Included (Free Tier)

- Article 5 prohibited practice screening (all 8 categories)
- Annex III high-risk classification (all 8 categories)
- Penalty exposure calculation (all 3 tiers)
- Basic classification report

## Upgrade to GIA Pro for Full Compliance

The free Quick Check tells you WHERE you stand. GIA Pro tells you HOW to get compliant.

**GIA Pro includes:**
- Full Articles 9-15 gap analysis with checklists
- Conformity assessment path selection (self-assessment vs third-party)
- EU Declaration of Conformity template generation
- Post-market monitoring plan (Article 72)
- GIA governance scoring with forensic audit trail
- Sealed memory packs with SHA-256 verification
- NIST AI RMF + ISO 42001 cross-mapping (16/16 controls)
- Remediation roadmap with prioritized actions

Learn more: https://aceexperts.org/gia/eu-ai-act-pro

---

*Powered by GIA — Governance Intelligence Automation. All assessments logged.*
