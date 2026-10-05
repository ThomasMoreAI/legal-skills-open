# EU AI Act for Israeli Companies

When and how Regulation (EU) 2024/1689 ("EU AI Act") reaches Israeli AI providers and deployers. Not legal advice.

## Baseline Facts

- Legal instrument: Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence
- Entry into force: August 1, 2024
- Risk-based structure: Prohibited, High-risk (Annex III), Limited-risk, Minimal-risk, plus General-Purpose AI (GPAI) obligations
- Enforcement: Member-state authorities plus the European AI Office for GPAI

## When Israeli Companies Are in Scope

Article 2 defines scope. You are caught if any of these apply:

1. You place an AI system on the EU market as a provider (sell, license, or make available in the EU under your name or brand)
2. You put an AI system into service in the EU under your name or brand
3. The output of your AI system is used in the EU, even if you operate the system from Israel

A pure Israeli-only deployment with only Israeli users does not trigger the Act, even if the underlying model was trained on European data.

## Risk Tiers in Practice

### Prohibited (Article 5)
Examples: social scoring by public authorities, real-time remote biometric identification in publicly accessible spaces for law enforcement (with narrow exceptions), exploiting vulnerabilities of specific groups, emotion recognition in workplace or education contexts. Cannot be placed on the EU market.

### High-Risk (Annex III)
Eight categories:
1. Biometrics
2. Critical infrastructure
3. Education and vocational training
4. Employment, worker management, access to self-employment
5. Access to essential private and public services
6. Law enforcement
7. Migration, asylum, border control
8. Administration of justice and democratic processes

Provider obligations include:
- Risk management system across the lifecycle
- Data governance for training, validation, test data
- Technical documentation
- Logging
- Transparency and information to deployers
- Human oversight
- Accuracy, robustness, cybersecurity
- Quality management system
- Conformity assessment (Annex VI self-assessment or Annex VII notified body, depending on system)
- Registration in the EU database
- CE marking
- Post-market monitoring
- Incident reporting to the relevant authority

Non-EU providers of high-risk systems must appoint an authorized representative established in the EU (Article 22).

### Limited-Risk
Chatbots and synthetic content require transparency disclosures. Users must know they are interacting with AI. Synthetic content must be machine-readable as such.

### Minimal-Risk
Most AI. Voluntary codes of conduct. No mandatory obligations.

### GPAI (General-Purpose AI models)
Obligations on model providers:
- Technical documentation for downstream developers
- Information summary of copyrighted training data
- Copyright policy for text and data mining opt-outs
- Compliance with Union copyright law

GPAI models with systemic risk (above a compute threshold, currently 10^25 FLOPs for training) face additional obligations including model evaluations, adversarial testing, cybersecurity, and serious incident reporting.

## Staggered Timeline

| Date | Status | What applies |
|------|--------|-------------|
| August 1, 2024 | In force | Act enters into force |
| February 2, 2025 | In force | Prohibitions (Article 5) and AI literacy obligations (Article 4) apply |
| August 2, 2025 | In force | GPAI obligations, governance structures, penalties apply. New GPAI models placed on the EU market after this date must comply immediately; providers of pre-existing GPAI models have until August 2, 2027 to comply |
| July 27, 2026 | In force | Articles 102 to 110 apply, per the new Article 113(3)(d) |
| August 2, 2026 | In force | **The general date of application, which did NOT move.** Article 50 transparency obligations apply to systems placed on the market from this date |
| December 2, 2026 | Upcoming | Two NEW prohibitions inserted by the Omnibus apply: Article 5(1) first subparagraph points (ba) and (bb), and Article 5(1a) and (1b) |
| December 2, 2026 | Upcoming | Providers of AI systems generating synthetic audio, image, video or text **that were placed on the market before August 2, 2026** must comply with Article 50(2) by this date (new Article 111(4)). This is a legacy grace period, not the start date for new systems |
| December 2, 2027 | Upcoming (moved from August 2, 2026) | Chapter III Sections 1 to 3 apply to high-risk AI systems under Article 6(2) and Annex III |
| August 2, 2028 | Upcoming (moved from August 2, 2027) | Chapter III Sections 1 to 3 apply to high-risk AI systems under Article 6(1) and Annex I |
| August 2, 2030 | Upcoming | Providers and deployers of high-risk systems intended for use by public authorities (amended Article 111(2)) |

**Timeline change (Digital Omnibus on AI): adopted, not pending.** Regulation (EU) 2026/1744 of 8 July 2026 was published in OJ L 2026/1744 on 24 July 2026 and entered into force on 27 July 2026. It amends Regulation (EU) 2024/1689 directly, so quote the amended Article 113 rather than the original, and cite EUR-Lex rather than a tracker site (`artificialintelligenceact.eu/implementation-timeline` still shows the pre-Omnibus schedule).

Only the HIGH-RISK dates moved. GPAI obligations were not postponed, and the general date of application stayed at 2 August 2026. Any customer document reading "the AI Act was postponed to 2027" as covering everything is wrong.

The Commission's stated reason for the postponement is the delayed availability of standards, common specifications and alternative guidance, and the delayed establishment of national competent authorities.

## General-Purpose AI Code of Practice

On July 10, 2025 the European AI Office published the final version of the voluntary Code of Practice for GPAI providers. The Commission and the AI Board have confirmed that the Code is an adequate voluntary tool. It has three chapters: Transparency, Copyright, and Safety and Security. Signing is voluntary but is the Commission's preferred route for demonstrating compliance with GPAI obligations. For Israeli GPAI providers selling into the EU, signing the Code is usually less work than building a bespoke compliance dossier.

## Decision Framework for Israeli Companies

Run through these questions in order:

1. **Am I in scope at all?** Is the system placed on the EU market, put into service in the EU, or is its output used in the EU? If no to all three, Regulation (EU) 2024/1689 does not apply. Ask this FIRST: the prohibitions are obligations under the Regulation, so they cannot bite a system the Regulation does not reach. An Israel-only deployment is outside scope even if it does something the Act would prohibit, and it is still governed by Israeli law.
2. **What is my ROLE?** Provider, deployer, importer or distributor carry different obligations, and a deployer that puts its own name or trademark on a high-risk system, or substantially modifies one, can be treated as its provider. For the common Israeli profile, a wrapper or fine-tune over a third-party foundation model sold to EU enterprise customers, this question decides everything. Read Articles 3, 25 and 26 rather than assuming; note also that Article 4 AI literacy has bound deployers as well as providers since 2 February 2025.
3. **Is my system prohibited?** If yes, stop. Do not place on the EU market. Check the amended Article 5, which Regulation (EU) 2026/1744 extended with further prohibitions applying from 2 December 2026.
4. **Is my system in Annex III (high-risk)?** If yes, plan for full high-risk obligations and an EU authorised representative. Article 6(3) provides a derogation for an Annex III system that performs a narrow procedural task, improves a prior human activity, detects decision patterns without replacing human assessment, or performs preparatory work, and does not profile. Read Article 6 before claiming it, and note that claiming it carries its own registration duty.
5. **Is my system limited-risk (chatbot, deepfake, emotion recognition outside work/school)?** If yes, transparency obligations apply, and they are live now: the general date of application, 2 August 2026, did not move.
6. **Is my model a GPAI?** If it is a foundation model offered for downstream use, GPAI obligations apply. Check the compute threshold for the systemic-risk tier.
7. **If minimal-risk:** consider voluntary codes of conduct for signalling trust to EU customers.

## Practical Notes for Israeli Teams

- Budget for EU authorized representative early if you expect to ship high-risk systems. This is typically a legal services contract, not an engineering task.
- Conformity assessment for high-risk is the largest cost. Allocate time.
- GPAI training data summaries will be a significant documentation effort. Start tracking training data provenance now.
- Copyright opt-outs: honor machine-readable opt-outs in training data scraping from EU sources.
- The EU AI Act does not preempt Israeli law. You may need to satisfy both regimes simultaneously.

## Gaps and Open Questions

- Harmonized standards for high-risk systems are still being drafted by CEN/CENELEC. Until finalized, use the Act's core requirements as a floor.
- Interaction with GDPR is active and evolving. DPIA under GDPR and risk management under AI Act are related but distinct.
- The European AI Office's guidance on GPAI is still maturing. Track it as it is published.
