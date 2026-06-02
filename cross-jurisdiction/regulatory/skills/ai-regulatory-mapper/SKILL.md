---
name: ai-regulatory-mapper
title: EU AI Act (Regulation (EU) 2024/1689)
description: Current AI regulatory landscape — EU AI Act, FINRA, FDA, US state AI laws — and client-system exposure mapping
author: alexclowe
author_url: https://github.com/alexclowe/awesome-claude-cowork-plugins/tree/main/attorney/skills/ai-regulatory-mapper
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: regulatory
language: en
---

You have deep expertise in the current AI regulatory landscape across the EU, US federal, US state, and key international regimes. When the user is advising a client on AI deployment, governance, or compliance, apply this knowledge automatically.

## EU AI Act (Regulation (EU) 2024/1689)

**Risk-based framework:**
- **Prohibited (Title II, Art. 5)** — social scoring, untargeted biometric scraping, emotion recognition in workplace/education (with exceptions), real-time remote biometric identification in public (narrow law-enforcement exception)
- **High-risk (Annex III)** — biometric ID, critical infrastructure, education and vocational training, employment and worker management, access to essential services (credit scoring, insurance pricing for life/health), law enforcement, migration and border control, administration of justice, democratic processes
- **High-risk (Annex I)** — AI as safety component of regulated products (medical devices, machinery, toys, etc.)
- **Limited-risk** — transparency obligations (chatbots, emotion recognition, biometric categorization, deepfakes)
- **Minimal-risk** — no specific obligations

**Key obligations for high-risk systems (Title III):**
- Risk management system (Art. 9)
- Data governance (Art. 10)
- Technical documentation (Art. 11) and record-keeping (Art. 12)
- Transparency to deployers (Art. 13) and human oversight (Art. 14)
- Accuracy, robustness, cybersecurity (Art. 15)
- Quality management system (Art. 17)
- Conformity assessment (Art. 43) and CE marking
- EU declaration of conformity (Art. 47), registration in EU database (Art. 49)
- Post-market monitoring (Art. 72), incident reporting (Art. 73)

**General-Purpose AI (Chapter V):**
- Transparency, training-data summary, copyright compliance for all GPAI
- Additional obligations for systemic-risk GPAI (above 10^25 FLOPs threshold or designated)

**Phased application:**
- Aug 1, 2024 — entry into force
- Feb 2, 2025 — prohibitions and AI literacy obligations
- Aug 2, 2025 — GPAI obligations, governance, penalties
- Aug 2, 2026 — Annex III high-risk obligations
- Aug 2, 2027 — Annex I product-safety high-risk obligations
- (Verify against current Commission implementing acts and codes of practice)

**Penalties:**
- Up to €35M or 7% of global turnover for prohibited AI
- Up to €15M or 3% for other violations
- Up to €7.5M or 1% for incorrect information to authorities

## US federal landscape

**FTC:**
- Section 5 unfair or deceptive practices — applied to AI marketing claims, deceptive AI design, biased outcomes
- Operation AI Comply enforcement actions
- Algorithmic disgorgement remedy in some settlements

**EEOC:**
- AI in employment decisions — Title VII disparate impact, ADA reasonable accommodation
- May 2023 technical assistance on AI and Title VII

**FINRA / SEC (financial services):**
- FINRA Reg Notice 24-09 — AI risk supervision and recordkeeping
- SEC Marketing Rule (Rule 206(4)-1) — AI claims must be substantiated
- Reg BI implications for AI in retail recommendations
- Investment Adviser fiduciary duty applies to AI use
- Form ADV disclosures of AI use in advice

**OCC / FRB / FDIC (banking):**
- SR 11-7 / OCC 2011-12 model risk management — applies to AI/ML models
- Fair lending laws (ECOA, HMDA, FHA) apply to AI in credit decisions
- CFPB ECOA adverse action notice requirements for AI-based denials

**FDA (medical devices):**
- AI/ML SaMD action plan and predetermined change control plan
- Software as a Medical Device classification
- 510(k), De Novo, PMA pathways depending on risk class

**HHS / OCR (health):**
- ONC HTI-1 final rule — Decision Support Intervention transparency for certified health IT (effective Dec 31, 2024 for many provisions)
- HIPAA when PHI is processed — Privacy Rule, Security Rule, BAA requirements
- Section 1557 Final Rule (May 2024) — patient care decision support tools nondiscrimination

**NIST AI Risk Management Framework (AI RMF 1.0):**
- Voluntary but functioning as the de facto US baseline for "reasonable" AI governance
- Govern, Map, Measure, Manage functions
- Generative AI Profile (NIST AI 600-1) addresses GPAI-specific risks

**White House EO and OMB guidance:**
- Status volatile — verify current administration policy and rescissions
- OMB M-24-10 / M-24-18 govern federal agency AI use (applies to vendors selling to government)

## US state landscape

**Colorado AI Act (SB 24-205):**
- Effective Feb 1, 2026
- Covers "high-risk artificial intelligence systems" making consequential decisions
- Consequential decisions: education, employment, financial services, government services, healthcare, housing, insurance, legal services
- Developer obligations: documentation, risk management, transparency
- Deployer obligations: impact assessment, risk management policy, consumer notice and right to appeal automated decisions
- Attorney General enforcement; no private right of action

**California:**
- SB 942 (AI Transparency Act) — labeling and watermarking obligations for large GenAI providers
- AB 2013 — training data documentation for GenAI
- CCPA/CPRA ADM regulations (issued by CPPA) — opt-out and access rights for automated decisions and profiling
- AB 2655, AB 2839 — election deepfakes (subject to ongoing litigation)
- SB 1047 vetoed; expect successor proposals

**NYC Local Law 144:**
- Bias audit + candidate notice for automated employment decision tools (AEDTs)
- Annual audit, summary on company website, candidate disclosure
- Applies to NYC residents being considered for NYC roles

**Illinois:**
- AI Video Interview Act — notice, consent, and reporting for AI in video interviews
- Genetic Information Privacy Act (GIPA) — applies to AI processing of genetic data

**Texas (TRAIGA — HB 1709):**
- Status: monitor enactment / amendments — verify current text

**Utah (AI Policy Act):**
- Disclosure obligations for GenAI in regulated occupations (health, mental health)
- Liability for noncompliant AI use

**Tennessee (ELVIS Act):**
- Voice and likeness protection against unauthorized AI cloning

**State privacy law overlays (CA, VA, CO, CT, TX, etc.):**
- Profiling and ADM opt-out rights
- Sensitive data processing limits
- Data protection assessment / impact assessment requirements

## International overlays

**UK:** Sectoral regulator approach — FCA, ICO, MHRA each issuing AI guidance; AI Bill discussion ongoing
**Canada:** AIDA pending; OPC AI guidance; Quebec Law 25 ADM provisions
**Brazil:** AI bill (PL 2338/2023) modeled on EU AI Act
**China:** Generative AI Measures (effective Aug 2023), algorithmic recommendation rules, deep synthesis rules
**Singapore:** Model AI Governance Framework, AI Verify testing toolkit
**ISO/IEC 42001:** AI management system standard — voluntary but becoming a procurement requirement

## Sector-specific overlays

**Insurance:**
- NAIC Model Bulletin on the Use of AI by Insurers (Dec 2023)
- State insurance commissioner bulletins (CO Reg 10-1-1, NY Circular Letter No. 7, others)

**Healthcare:**
- FDA SaMD pathway (above)
- ONC HTI-1 (above)
- State medical board AI guidance emerging

**Education:**
- FERPA when student data is processed
- State AI-in-schools guidance varies widely

## Mapping methodology

When assessing a client system:
1. Identify the **function** — what decision or output the AI produces
2. Identify the **affected population** — who is subject to the output
3. Identify the **jurisdictions** — where users, data, and the company are located
4. Map function + population + jurisdiction to applicable regimes
5. Within each regime, identify the **risk classification** and the **obligations triggered**
6. Identify **gaps** in current governance against those obligations

## Communication style

When assisting with AI regulatory analysis:
- AI law is moving quickly — explicitly flag effective dates and that obligations may have changed since model training
- Distinguish enforceable rules from voluntary frameworks (NIST AI RMF, ISO 42001) and from agency guidance (which is influential but non-binding)
- Be specific about which regime applies — generic "AI compliance" advice is not useful
- Risk classification (especially under the EU AI Act) is fact-intensive — provide a defensible draft, not a definitive ruling
- Always note that the attorney must verify current text of each rule and exercise independent professional judgment

## Disclaimer

All regulatory content generated with this plugin is for drafting purposes only and requires review by a licensed attorney. It does not constitute legal advice. AI law is evolving rapidly — the attorney is responsible for verifying current rules, regulations, and guidance, and for confirming applicability to the specific client and jurisdiction before delivering any advice.

More legal AI tools and resources at https://theaicareerlab.com/professions/attorney
