---
name: eu-ai-act-rashadansari
title: EU AI Act
description: 'Reference knowledge on the EU AI Act (Regulation (EU) 2024/1689): risk tiers, obligations, compliance deadlines including the 2026 AI Omnibus changes, penalties, and scope. Activate when the user asks about the EU AI Act, AI regulation in Europe, high-risk AI compliance, AI transparency or watermarking obligations, GPAI model rules, or whether a product or feature falls under EU AI rules.'
author: RashadAnsari
author_url: https://github.com/RashadAnsari/myagents/tree/master/plugins/albino/skills/eu-ai-act
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# EU AI Act

Working knowledge of Regulation (EU) 2024/1689 (the EU AI Act). Use it to answer
questions and assess whether a system, feature, or product is in scope and what
obligations apply.

## Freshness rule (read first)

The implementation timeline was amended by the "Digital Omnibus on AI"
package: adopted by Parliament on 16 June 2026, approved by Council on
29 June 2026, and signed on 8 July 2026. Official Journal publication was
expected before 2 August 2026, with entry into force on the third day after
publication. If advice depends on the amendments being in force, verify
publication via web search (query: "Digital Omnibus AI Official Journal").
Prefer primary sources: digital-strategy.ec.europa.eu and
ai-act-service-desk.ec.europa.eu. Warn users that most guidance published
before mid-2026 describes deadlines that no longer apply.

## What the Act is

- The EU's comprehensive AI regulation, the first of its kind. Entered into
  force 1 August 2024, applying in stages.
- Extraterritorial: applies to providers and deployers outside the EU if the
  AI system's output is used in the EU (sales, access, downstream
  integrations).
- Not retroactive: systems already on the market before a given obligation
  applies may be grandfathered for certain obligations, unless significantly
  redesigned afterwards.

## Risk tiers

1. **Prohibited practices** (banned since 2 February 2025): social scoring by
   public authorities, manipulative or exploitative AI, untargeted scraping of
   facial images, emotion recognition in workplaces and schools (with narrow
   exceptions), most real-time remote biometric identification in public
   spaces. The Omnibus adds a prohibition on AI systems that generate
   non-consensual intimate imagery or child sexual abuse material, including
   general-purpose image and video tools where such output is a reasonably
   foreseeable and reproducible outcome; providers must implement refusal
   training, output controls, and content filtering. Compliance deadline:
   2 December 2026.
2. **High-risk systems**: two families.
   - Annex III stand-alone systems: biometrics, critical infrastructure,
     education, employment and worker management, access to essential services
     and credit, law enforcement, migration/asylum/border control,
     administration of justice.
   - Annex I embedded systems: AI as a safety component of products already
     covered by EU product law (medical devices, vehicles, toys, etc.), via
     Article 6(1). The Omnibus narrows this family: AI used solely for user
     assistance, performance optimization, service efficiency, automation or
     convenience, or quality control is not automatically a safety component
     unless its failure poses health or safety risks, and AI embedded in
     Machinery Regulation products is largely excluded from the high-risk
     regime (the Commission can reintroduce AI-specific requirements via
     delegated acts). Medical devices and toys remain fully in scope.
   - Obligations: risk management system, data governance, technical
     documentation, logging, human oversight, accuracy/robustness/
     cybersecurity requirements, conformity assessment, CE marking,
     registration in the EU database.
3. **Limited risk**: transparency obligations only (Article 50, below).
4. **Minimal or no risk**: no new obligations. Most AI systems in use (spam
   filters, game AI, routine ML features) fall here.

## Timeline (as amended by the Digital Omnibus, signed 8 July 2026)

| Date | What applies |
|---|---|
| 2 Feb 2025 | Prohibitions; AI literacy obligations; general provisions |
| 2 Aug 2025 | GPAI model obligations; EU and national governance in place; national penalty rules |
| 2 Aug 2026 | Article 50 transparency rules; innovation support measures; enforcement begins at national and EU level |
| 2 Dec 2026 | Compliance deadline for the new NCII/CSAM prohibition; end of the watermarking grace period for systems placed on the market before 2 Aug 2026 |
| 2 Aug 2027 | GPAI models placed on the market before 2 Aug 2025 must be compliant; at least one regulatory sandbox per Member State (delayed from 2 Aug 2026) |
| 2 Dec 2027 | High-risk rules for Annex III stand-alone systems (delayed from 2 Aug 2026) |
| 2 Aug 2028 | High-risk rules for Annex I AI embedded in regulated products, Article 6(1) (delayed from 2 Aug 2027) |

The Omnibus rationale: harmonised standards and conformity-assessment tooling
were not ready, so high-risk application was tied to the availability of those
support tools. The transparency regime was NOT delayed.

## Article 50 transparency obligations (apply from 2 August 2026)

- Systems interacting directly with people must disclose that the user is
  dealing with a machine, unless obvious from context.
- AI-generated or manipulated audio, image, video ("deepfakes") must be
  disclosed as artificially generated.
- Article 50(2): providers of systems generating synthetic audio, image,
  video, or text must mark outputs in a machine-readable format
  (watermarking) so they are detectable as artificially generated. Systems
  placed on the market before 2 August 2026 have an Omnibus grace period
  until 2 December 2026; systems placed after that date must comply from
  2 August 2026.
- Emotion recognition and biometric categorisation systems must inform the
  people exposed to them.

## General-purpose AI (GPAI) model rules (since 2 August 2025)

- Providers of GPAI models (foundation/frontier model vendors) owe technical
  documentation, copyright policy, training-data summaries; models with
  systemic risk owe additional evaluation, incident reporting, and
  cybersecurity duties.
- Downstream API users of these models do not inherit the provider
  obligations, but remain responsible for their own deployment (including
  Article 50 transparency and any high-risk classification of the resulting
  system).

## Other Digital Omnibus amendments

- AI Office powers expanded: exclusive supervision of AI systems built on a
  GPAI model developed within the same undertaking, and of AI integrated
  into very large online platforms and search engines (VLOPs/VLOSEs), with
  investigation, on-site inspection, binding commitment, and fining powers.
- AI literacy (Article 4) softened: providers and deployers must support
  staff AI literacy rather than guarantee specific literacy levels.
- Bias detection: the legal basis for processing special-category personal
  data to detect and correct bias is extended from high-risk providers to
  providers and deployers of all AI systems and GPAI models, subject to a
  strict necessity standard.
- Registration simplified: non-high-risk Annex III systems self-assessed by
  providers still register in the EU database, but with a lighter
  administrative footprint.

## Penalties

- Up to EUR 35M or 7% of global annual turnover: prohibited practices.
- Up to EUR 15M or 3%: most other violations (including high-risk and
  transparency obligations).
- Up to EUR 7.5M or 1%: supplying incorrect or misleading information to
  authorities.
- Overlapping GDPR exposure (up to EUR 20M or 4%) where AI mishandles
  personal data, e.g. biometric or emotion recognition applications.

## How to assess a system (workflow)

1. Confirm EU nexus: is the system or its output placed on the EU market or
   used in the EU? If no, the Act does not apply.
2. Check the prohibited list. If matched, the practice must stop; no
   compliance path exists.
3. Classify against Annex III and Article 6(1)/Annex I. If high-risk, map the
   full obligation set and plan conformity assessment lead time against the
   applicable deadline (verify current dates per the freshness rule).
4. If not high-risk, check Article 50: does the system chat with users,
   generate synthetic media or text, or perform emotion
   recognition/biometric categorisation? If yes, transparency and marking
   duties apply.
5. Otherwise, the system is minimal-risk: no new obligations, but note AI
   literacy duties on the organisation and any sector rules.
6. For anything using third-party foundation models, separate the model
   provider's GPAI duties from the deployer's own duties; advise only on the
   latter unless asked.

## Answer style

- Lead with the classification and the applicable deadline; cite the article
  or annex (e.g. "Article 50(2)", "Annex III") so the user can verify.
- Flag legal-advice limits: this is regulatory orientation, not legal advice;
  recommend counsel for high-risk classification decisions and conformity
  assessments.
