---
name: marketing-compliance-canhada-labs
title: Healthcare Marketing Compliance
description: 'Healthcare marketing compliance discipline covering the full pre-publication

  review lifecycle: claim substantiation against clinical-evidence hierarchy,

  FDA / FTC / Anvisa RDC 96 / EMA / EFPIA promotional rules, off-label use

  prohibition, fair-balance obligations (efficacy and safety in proportion),

  testimonial and HCP-engagement restrictions under Sunshine Act / Open

  Payments / EFPIA Disclosure Code, and PII / PHI handling in campaign

  analytics (HIPAA marketing authorisation, tracking-pixel case-law, LGPD

  Art. 11). Use when reviewing a promotional asset before publication; when

  authoring claim-substantiation packages; when assessing multi-jurisdiction

  promotional compliance for a new market entry; when evaluating testimonial

  or influencer contracts for regulatory exposure; or when preparing for an

  OCR / Anvisa / regulatory audit of promotional materials.'
author: Canhada-Labs
author_url: https://github.com/Canhada-Labs/ceo-orchestration/tree/main/.claude/skills/domains/healthcare/skills/marketing-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: healthcare
language: en
---

# Healthcare Marketing Compliance

## Cardinal Rule

Marketing review without licensed-clinician + regulatory + legal sign-off
is publication, not approval; publication of unapproved claims is
regulator-attention waiting to happen. No promotional asset — digital,
print, broadcast, social, or verbal — leaves internal review and reaches
any external audience without a documented, three-party MLR (Medical /
Legal / Regulatory) sign-off on record. Review is not a ceremony; it is
the chain of custody that determines whether a regulator inquiry becomes
a warning letter or a consent decree.

## Fail-Fast Rule

Stop and return a structured rejection when any of the following is true:

- The asset contains an off-label indication, dosing route, or patient
  population not reflected in the current product labelling or package
  insert.
- A comparative efficacy claim (superiority, non-inferiority, or parity)
  lacks a head-to-head, adequately-powered, peer-reviewed trial as the
  primary supporting reference.
- The asset uses patient testimonial, case study, or before-and-after
  imagery without a verified HIPAA authorisation, minor consent, or model
  release on file.
- A superlative claim ("most effective," "leading," "first-line") cannot
  be supported by independently auditable, current evidence.
- Fair-balance risk information is absent, buried below the primary
  benefit message, or rendered in font size, contrast, or duration that
  fails readability standards for the medium.
- The asset names an investigational product in a promotional context
  before regulatory approval in the target jurisdiction.

## When to Apply

Apply this skill when:

- Authoring or reviewing any promotional material referencing a drug,
  biologic, medical device, or diagnostic for any jurisdiction (US, BR,
  EU, or multi-jurisdiction bundle).
- Assessing a content marketing plan (social calendar, influencer brief,
  patient-community programme) for regulatory exposure before activation.
- Evaluating a testimonial contract, speaker-bureau agreement, or HCP
  advisory-board engagement for Sunshine Act / EFPIA Disclosure Code /
  Anvisa CMED transparency compliance.
- Designing campaign analytics architecture where patient or HCP data
  is collected, segmented, or used for targeting.
- Preparing corrective-action responses to regulator letters (FDA
  Untitled Letter, FDA Warning Letter, Anvisa notificação, OCR resolution
  agreement).

Do not apply this skill to clinical-trial protocol design, regulatory
submission strategy, or pharmacovigilance signal management; route those
to the relevant clinical-regulatory skill.

## PII / PHI in Campaigns

Patient and HCP data in marketing contexts carries an elevated regulatory
burden that standard PII rules do not fully cover.

**Patient testimonials:**
- Every testimonial from a patient requires a signed, condition-specific
  HIPAA authorisation that explicitly authorises promotional use. A
  generic research-consent or treatment-consent form is insufficient.
- Testimonials involving a minor require additional parental or guardian
  consent and, depending on jurisdiction, court approval.
- Where the patient's image, voice, or identifiable story is used, a
  model release covering commercial promotional use must accompany the
  HIPAA authorisation.
- LGPD Art. 11 classifies health data as sensitive personal data;
  processing for marketing purposes requires explicit, specific consent
  beyond the standard Art. 7 bases. The consent instrument must identify
  the promotional purpose by name and medium.

**Campaign analytics and tracking:**
- Campaign analytics systems must be configured to exclude PHI. Patient
  identifiers — name, MRN, date of birth, diagnosis codes, prescription
  history — must not enter CRM, DSP, or ad-platform audiences directly
  or via hashed match-keys applied to health-context data.
- The Office for Civil Rights (OCR) has issued enforcement guidance
  confirming that tracking pixel technologies (Meta Pixel, Google Tag)
  on authenticated patient-portal pages, symptom checkers, or
  prescription-refill flows constitute HIPAA-covered disclosures to
  third parties absent a Business Associate Agreement (BAA) covering
  the pixel vendor and a valid authorisation from the individual.
- Conduct a pixel audit before any campaign launch. Authenticated pages
  and health-context landing pages require pixel removal or BAA coverage;
  non-authenticated general-awareness pages require documented risk
  assessment.
- Aggregate or cohort-level analytics derived from PHI require a formal
  de-identification analysis (Safe Harbor or Expert Determination method
  per 45 CFR § 164.514) before the derived dataset enters campaign
  measurement.

## Claim Substantiation

Every promotional claim requires a pre-submission substantiation package
that travels with the asset through the MLR review cycle.

**Clinical-evidence hierarchy for claims:**

| Tier | Evidence Type | Acceptable Use |
|------|--------------|----------------|
| 1 | Randomised controlled trial (RCT), adequately powered, peer-reviewed | Primary efficacy and safety claims |
| 2 | Systematic review or meta-analysis of Tier 1 studies | Summary claims and class comparisons |
| 3 | Observational study (real-world evidence) | Contextual or supportive claims; not standalone for efficacy |
| 4 | Case series, case report, expert opinion | Background context only; never standalone for efficacy |

Rules:
- Claims derived from Tier 3 or Tier 4 evidence alone must be labelled
  as such and may not be stated as established fact.
- Selective citation — citing a study's favourable endpoint while omitting
  a co-primary or key secondary endpoint with a negative result — is a
  per se violation in all covered jurisdictions.
- On-label vs. off-label is determined by the current, jurisdiction-
  specific approved labelling or package insert, not by clinical practice
  norms or emerging data.
- Comparative claims require head-to-head evidence. Indirect comparison
  across separate trials (network meta-analysis) must be explicitly
  labelled as an indirect comparison and cannot support superiority claims
  without direct confirmatory evidence.
- Superlative claims ("only," "fastest," "most studied") require
  documented evidence that no competing product meets or exceeds the
  dimension claimed, as of the publication date of the asset.

## Fair Balance

Regulatory bodies across all covered jurisdictions require that risk
information appear in fair proportion to benefit claims, not as a
subordinate afterthought.

**Core principle:** The totality of information about a product's efficacy
and its risk profile must be presented in a manner that enables the
audience to form an accurate impression of the benefit-risk relationship.

**Medium-specific requirements:**

- *Broadcast (TV/radio):* Risk information must be presented in audio with
  adequate volume, pace, and duration relative to the benefit presentation.
  The major statement of risks must be prominent, not masked by competing
  audio or visual distraction.
- *Print (journal, direct-mail, patient-facing):* A brief summary of risk
  information (or, for DTC print, an adequate provision disclosing all
  important risk information) must accompany the promotional piece. Font
  size, contrast, and legibility must be equivalent to benefit claims.
- *Digital (website, banner, video):* Static pages must include the brief
  summary or a prominent link to prescribing information on every page
  where a claim appears. Video must carry audible and legible risk
  information; hyperlinked risk content does not substitute for on-page
  presence when a benefit claim is present.
- *Social media:* Single-product social posts that make a product claim
  must include risk information within the character or display limit of
  the post. The practice of placing risk information only in a bio-link
  or comment, separated from the benefit claim, does not satisfy fair
  balance requirements.

**Readability:** Risk information must be accessible to the intended
audience. Patient-directed materials must target a Grade 6-8 reading
level; HCP-directed materials follow professional-copy conventions but
must not obscure clinical significance through typographic subordination.

## Pre-Launch Review

The MLR triad is the minimum mandatory gate for every promotional asset.

**MLR participants and accountabilities:**

| Role | Review Scope |
|------|-------------|
| Medical (licensed clinician or medical director) | Clinical accuracy, evidence support, on-label scope, fair-balance adequacy |
| Legal (regulatory legal counsel) | Intellectual property, false-advertising exposure, Sunshine Act / disclosure obligations, litigation hold implications |
| Regulatory (regulatory affairs) | Jurisdictional compliance, labelling alignment, agency guideline conformance |

**Process rules:**
- All three parties must provide a documented approval — electronic
  signature with timestamp — before an asset is released to any channel.
- A two-of-three approval is not a valid release gate; unanimous MLR
  sign-off is required.
- Revision after any MLR sign-off restarts the review cycle for the
  revised sections; a minor-change waiver may be granted by regulatory
  only for corrections that do not alter a claim, risk statement, or
  visual presentation of data.
- All review versions, comments, and approvals must be retained in the
  promotional review system of record for a minimum of three years (US
  FDA 21 CFR § 314.81(b)(3)(i)) or the jurisdiction-specific retention
  minimum, whichever is longer.
- Turnaround SLA for standard review: five business days. For expedited
  launch materials: forty-eight hours with explicit regulatory-director
  sponsorship. For corrective actions: twenty-four hours maximum.

## Off-Label / Investigational

The prohibition on promotional pre-approval use is near-absolute in all
covered jurisdictions.

- Promotional communications — including disease-awareness campaigns
  structured to favour a product not yet approved for a condition — are
  prohibited before regulatory approval in each target jurisdiction.
- The medical-information response exception permits unsolicited requests
  from HCPs for off-label information to be answered by a medical-
  information function operating independently from marketing; the
  response must be non-promotional, balanced, and documented.
- The scientific-exchange exception (presentations at scientific
  conferences, peer-reviewed publication activity) is narrow: it covers
  bona fide scientific discourse by medical affairs, not commercially
  motivated communications routed through medical affairs to avoid
  promotional review.
- Investigational products in clinical trials must not be characterised
  in promotional materials with efficacy language, outcome predictions,
  or patient-segment targeting that pre-supposes approval.

## Testimonial / HCP Engagement

Aggregate spend transparency and anti-kickback compliance apply across
all HCP engagement types.

**Disclosure frameworks by jurisdiction:**

| Framework | Jurisdiction | Scope |
|-----------|-------------|-------|
| Sunshine Act / Open Payments (CMS) | US | All transfers of value to physicians and teaching hospitals; annual public reporting |
| EFPIA Disclosure Code | EU / EEA | Payments and transfers of value to HCPs and healthcare organisations; annual country-level reporting |
| Anvisa CMED transparency / CFM Código de Ética | Brazil | Commercial relationships between manufacturers and HCPs; Anvisa RDC 96 anti-inducement provisions |

**Operational rules:**
- Speaker fees, honoraria, advisory-board fees, and consulting fees must
  reflect fair market value (FMV) established by an independent,
  documented FMV analysis. Rates that exceed the FMV ceiling are
  presumptive anti-kickback exposures.
- Any transfer of value to an HCP — meals, travel, gifts, educational
  materials — must be tracked, documented, and reportable on demand.
  De minimis thresholds (US: $10 per item, $25 aggregate per year for
  non-educational items) apply but do not eliminate the record-keeping
  requirement.
- HCPs must not be engaged in speaker or advisory roles where their
  audience or influence is primarily attributable to patient-prescribing
  behaviour for the sponsoring company's products; such arrangements
  attract enhanced Anti-Kickback Statute scrutiny.
- Testimonial and endorsement arrangements with HCPs are subject to FTC
  Endorsement Guides disclosure requirements in US consumer-directed
  materials; the material connection must be clearly and conspicuously
  disclosed.

## Multi-Jurisdiction Compliance

Simultaneous or sequential market entry requires a jurisdiction matrix
before assets are finalised.

| Jurisdiction | Primary Regulatory Body | Key Promotional Rule | Notable Restriction |
|-------------|------------------------|---------------------|---------------------|
| United States | FDA (OPDP / CDER / CDRH) + FTC | 21 CFR § 202; FTC Act § 5 | DTC broadcast fair balance; off-label prohibition; comparative claim standards |
| Brazil | Anvisa + CFM + COREN | RDC 96/2008 (drugs); RDC 185/2001 (devices); CFM Resolução on HCP promotion | Prohibition on testimonials from patients or HCPs in mass media; Anvisa prior-approval for broadcast drug ads |
| European Union | EMA + national competent authorities + EFPIA | Directive 2001/83/EC Title VIII; national transpositions | Prescription-drug DTC advertising prohibited EU-wide; EFPIA self-regulatory overlay |
| United Kingdom | MHRA + PMCPA | ABPI Code of Practice | Post-Brexit MHRA autonomy; ABPI Code mandatory for PMCPA members |

Multi-jurisdiction assets must satisfy the most restrictive applicable
requirement on each dimension unless a jurisdiction-specific version is
produced and geo-fenced to its target market.

## Audit Readiness

Regulatory inspection readiness is a continuous state, not a pre-
inspection sprint.

**Document retention minimum:**
- Promotional review files (all versions, all MLR sign-offs, all
  supporting substantiation): three years post-last-distribution or
  jurisdiction minimum, whichever is longer.
- HCP transfer-of-value records: five years for US Anti-Kickback Statute
  purposes; seven years for Anvisa; follow the longest applicable period
  for global programmes.
- HIPAA marketing authorisations and consent instruments: six years from
  date of creation or last effective date per 45 CFR § 164.530(j).

**Corrective-action protocol:**
- Regulator letter received: acknowledge within forty-eight hours;
  convene MLR + legal crisis team within twenty-four hours of receipt.
- Asset takedown: immediate upon confirmed material violation; no asset
  remains live pending legal assessment when a material violation is
  identified.
- Corrective communication (where required by regulator): draft within
  ten business days; submit for MLR review under expedited SLA before
  regulator deadline.
- Root-cause analysis: complete within thirty days of corrective-action
  submission; update review checklist and training programme to address
  systemic gap.

## Anti-Patterns

| Anti-Pattern | Mechanism of Harm | Compliant Alternative |
|-------------|------------------|----------------------|
| Off-label suggestion via leading question ("Have you considered patients who struggle with X complication?") | Implies promotional intent for unapproved indication without explicit claim; attracts OPDP scrutiny as disguised off-label promotion | Frame HCP communications around approved indication; route off-label data to medical information under scientific-exchange exception |
| Testimonial without valid HIPAA authorisation or model release | PHI disclosure without authorisation; FTC disclosure gap; LGPD Art. 11 violation | Obtain condition-specific, promotion-purpose HIPAA authorisation before use; obtain model release separately |
| Fair-balance buried in fine print or audio speed-up | Effective suppression of risk information relative to benefit claim; per se FDA violation for broadcast | Present risk information at equivalent prominence, pace, and duration to benefit claim across medium |
| Comparative claim without head-to-head data | Misleading; actionable under FTC Act § 5 and FDA § 202 as implied superiority without adequate substantiation | Limit comparison to product-labelling data; label indirect comparisons explicitly as such |
| Pixel on authenticated patient-portal pages without BAA | OCR-enforced HIPAA violation; disclosure of PHI to third-party technology vendor | Remove pixel or obtain BAA with vendor; document decision in compliance record |
| Superlative claim ("the most prescribed") with stale supporting data | Claim may be false or misleading if market conditions have changed since the cited data period | Anchor superlatives to a specific, dated data source; refresh evidence at each review cycle |
| Sunshine Act threshold management (structuring payments below reporting threshold) | Anti-Kickback Statute exposure; potential False Claims Act liability | Record and report all transfers of value regardless of amount; FMV documentation is the control |

## Cross-References

- `core/compliance-lgpd` — LGPD legal bases (Art. 7, Art. 11), data
  subject rights, breach notification, and ANPD obligations that apply
  to PHI in Brazilian healthcare marketing contexts.
- `domains/healthcare/skills/healthcare-customer-service` — patient
  communication protocols, consent documentation, and service-interaction
  compliance requirements that intersect with promotional activities.
- `domains/marketing-global/skills/content-creator` — general content
  creation standards, editorial workflow, and brand-voice guidelines;
  healthcare marketing compliance rules layer on top of and supersede any
  general marketing guidance where a conflict exists.

## ADR Anchors

- ADR-058: Two-pass review gate — all outputs produced under this skill
  are subject to the two-pass review protocol: a first pass for regulatory
  accuracy and a second pass for completeness and internal consistency
  before delivery.
