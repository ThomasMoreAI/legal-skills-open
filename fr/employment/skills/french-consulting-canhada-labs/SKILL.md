---
name: french-consulting-canhada-labs
title: French Market Consultant
description: 'France-specific business consulting covering Convention Collective

  navigation, RGPD compliance specifics distinct from generic GDPR

  guidance, Bpifrance funding programmes, Crédit Impôt Recherche

  eligibility, French professional formality and relationship register,

  syndicat and CSE labour relations, and droit du travail obligations.

  Multi-jurisdiction-aware companion for operating in France. Use when:

  structuring employment in France; selecting or negotiating a Convention

  Collective; filing a CIR claim or Bpifrance application; advising on

  CSE consultation obligations; or adapting communication register for

  French professional contexts.'
author: Canhada-Labs
author_url: https://github.com/Canhada-Labs/ceo-orchestration/tree/main/.claude/skills/domains/i18n-business/skills/french-consulting
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: employment
language: en
---

# French Market Consultant

## Cardinal Rule

Every recommendation touching French employment, tax, or RGPD must
reference the applicable legal instrument — Convention Collective
identifier (IDCC), article of the Code du travail, CNIL délibération,
or Bpifrance programme reference — before any operational guidance is
issued. Guidance without a traceable legal basis is rejected at the
two-pass review gate (ADR-058). When the applicable instrument is
genuinely uncertain, state the ambiguity explicitly and identify the
verification step required.

## Fail-Fast Rule

Stop and escalate to a qualified French legal or fiscal counsel when
any of the following is detected:

- A proposed employment contract applies a Convention Collective
  whose IDCC has not been verified against the company's NAF/APE code
  — do not proceed until the classification is confirmed.
- A RGPD data-processing activity involves cross-border transfer to a
  non-adequate country without a valid transfer mechanism under RGPD
  Art. 46 — halt the transfer design and require a transfer-impact
  assessment.
- A CIR claim includes expenditure categories that have not been
  reviewed against CGI Art. 244 quater B current guidance — do not
  submit until eligible categories are verified with a commissaire
  aux comptes or agréé.
- A termination procedure has reached the convocation à entretien
  préalable stage without checking the applicable Convention Collective
  for obligations exceeding the Code du travail minimum — stop and
  verify before proceeding.
- A CSE consultation obligation arises from a project affecting
  conditions of work, headcount, or organisation — halt the project
  launch until the mandatory information and consultation procedure
  is completed.

## When to Apply

Apply this skill when:

- Selecting or switching a Convention Collective for a new or
  restructured French entity.
- Drafting or reviewing French employment contracts, trial-period
  clauses, or non-compete (clause de non-concurrence) provisions.
- Assessing CSE information and consultation obligations before
  launching a project, restructuring, or headcount change.
- Preparing or reviewing a Crédit Impôt Recherche declaration or
  evaluating R&D-project eligibility.
- Structuring a Bpifrance application — prêt d'honneur, French Tech
  grant, or guarantee scheme.
- Advising on RGPD obligations specific to French law, including
  CNIL guidance, sectoral référentiels, and French data-localisation
  requirements for certain public-sector contracts.
- Calibrating communication register and relationship-building
  protocols for French professional contexts.

Do not apply for generic EU GDPR advice without France-specific
dimension — use `core/compliance-lgpd` cross-referenced with
RGPD specifics instead. Do not apply for multi-country EU employment
strategy without first resolving the French-law obligations here.

## Convention Collective Navigation

**Selection logic:** A company's applicable Convention Collective is
determined primarily by its NAF/APE activity code, not by employee
choice. Verify the code at INSEE registration; confirm at URSSAF
registration. When multiple conventions are plausible (e.g.,
Syntec — IDCC 1486 vs. Métallurgie — IDCC 3248 for hardware-adjacent
tech companies), document the classification rationale and obtain
a formal written position from the DREETS if the ambiguity is material.

**Minimum mandatory provisions:** The Convention Collective sets
floors for salary grids (salaires minima conventionnels), notice
periods, trial-period durations, classification grades, and specific
benefits. Contractual terms may exceed but never undercut Convention
Collective minimums; a contract clause below the floor is void and
replaced by the floor automatically.

**Syntec specifics (IDCC 1486):** The most common convention for
tech and consulting companies. Key obligations: salary grid
coefficients 100–900 with mandatory minimums updated annually;
ETAM vs. ingénieurs-et-cadres status determines AGIRC-ARRCO tier;
forfait-jours (218 days standard) requires individual written
agreement and CC clause authorising it; télétravail avenant imposes
a written charter — unilateral arrangements without documentation
expose the employer to reclassification risk.

**Amendment tracking:** Avenants negotiated between social partners
may override prior terms; subscribe to Légifrance alerts or a
HR-legal monitoring service to detect avenants before their
entry-into-force date.

## RGPD Compliance Specifics

**CNIL authority:** The French data-protection authority (CNIL)
issues délibérations, recommandations, and référentiels that
operationalise RGPD obligations for specific sectors and
processing activities. These are not legally binding in the same
sense as the regulation, but non-compliance is treated as evidence
of inadequate organisational measures in enforcement proceedings.

**Mandatory DPO designation triggers:** Under RGPD Art. 37, a DPO
is mandatory for public authorities, large-scale systematic
monitoring, and large-scale special-category processing. The CNIL
expects DPO registration on its portal within two months of
designation.

**Records of processing (RoPA):** RGPD Art. 30 RoPA is mandatory
at 250+ employees; recommended below that threshold for any
non-occasional or special-category processing. Structure entries
to include legal basis, retention period, and transfer mechanism
per processing activity.

**Cookie consent — CNIL guidelines:** French cookie rules go beyond
the RGPD baseline. The CNIL recommends a consent mechanism where
refusal is as easy as acceptance; a single-click refusal option must
be visible on the same layer as the accept button. Pre-ticked boxes
and consent-walls (access conditioned on accepting analytics) are
non-compliant per CNIL délibération SAN-2021-023 and successors.

**RGPD + sectoral law intersection:** French health data is subject
to RGPD plus the loi Informatique et Libertés as amended plus
specific HDS (Hébergeur de Données de Santé) certification
requirements for hosting. Public-sector contracts may require
data hosted on SecNumCloud-qualified infrastructure. Verify sectoral
overlay before scoping any France-bound data architecture.

## Bpifrance + R&D Tax Credit

**Bpifrance programme taxonomy:**

```
Bpifrance instruments (non-exhaustive):
├── Prêt d'Honneur (zero-interest, personal loan to founder)
│   └── Eligibility: early-stage, no revenue required
├── Prêt Bpifrance (Prêt à la Création d'Entreprise — PCE, etc.)
│   └── Eligibility: SME, 3 years post-creation, no collateral
├── Garantie (counter-guarantee on bank loan, 40-70%)
│   └── Purpose: unlock bank lending with reduced collateral demand
├── Subventions i-Lab / i-Nov / French Tech Souveraineté
│   └── Eligibility: innovation projects; specific calls; dossier
├── French Tech (Visa, Mission, Next40/120 programme)
│   └── Not a fund; a label and network providing facilitated access
└── Aide à l'Innovation (AI) / Avances Remboursables
    └── Non-dilutive; repayable only on commercial success
```

**CIR — Crédit Impôt Recherche (CGI Art. 244 quater B):**
- Rate: 30% of eligible R&D expenditure up to €100 M; 5% above.
- Eligible expenditure: personnel costs for researchers and research
  technicians (with specific calculation rules for researcher time),
  depreciation of R&D-dedicated assets, subcontracting to agréé
  organisations or public research bodies, patent fees, technology
  watch costs (capped).
- Documentation requirement: the company must be able to demonstrate,
  at a subsequent tax audit (vérification de comptabilité or rescrit),
  that claimed activities meet the OCDE Frascati definition of R&D
  (systematic, creative, uncertainty-reducing, novel, transferable).
  Maintain project notebooks, git commit histories, technical reports,
  and researcher time-tracking records contemporaneously — reconstructed
  records carry significantly lower audit credibility.
- Rescrit fiscal: companies may request a binding advance ruling from
  the DGFIP on CIR eligibility before filing. A positive rescrit
  provides strong protection against subsequent reclassification;
  seek it for novel activity categories or large claimed amounts.
- JEI status (Jeune Entreprise Innovante): companies qualifying as JEI
  benefit from social-charge exemptions on researcher salaries in
  addition to CIR; the two regimes are cumulative subject to caps.

## Cultural + Communication Register

**Formality by default:** French professional communication defaults to
formal register (vouvoiement) unless the interlocutor explicitly
proposes tutoiement. Using tutoiement prematurely is perceived as
presumptuous, not friendly. Maintain vouvoiement in written
correspondence until a clear signal is given.

**Meeting and decision-making patterns:** French professional culture
values thorough verbal argumentation before convergence. Pushing for
a decision before the analytical debate is complete generates
resistance. Build structured-discussion time into project timelines.

**Written precision:** French professional writing emphasises
syntactic precision. Avoid anglicisms in formal documents. For
regulatory submissions (Bpifrance, CNIL, URSSAF), use the
terminology of the applicable regulation verbatim — paraphrase
creates ambiguity that administrative assessors resolve against
the applicant.

**Relationship investment:** French B2B relationship-building
requires face-to-face or substantive telephone contact before
written proposals. Cold-contact proposals without prior conversation
are less effective than in Anglo-American markets; referrals carry
disproportionate weight.

## Labour Relations Frame

**CSE — Comité Social et Économique:** Mandatory at 11+ employees
(délégués du personnel powers); full CSE with expanded prerogatives
at 50+ employees. Thresholds are calculated over 12 consecutive months.
Elections must be organised within 90 days of reaching the threshold;
failure to organise is a délit d'entrave.

**Consultation obligations:** The CSE must be consulted before:
any plan affecting conditions of work (PSE — Plan de Sauvegarde de
l'Emploi for 10+ dismissals in 30 days at 50+ employee companies);
introduction of new technologies that materially modify work
organisation; changes to work schedules; and any other matter
specified in the Convention Collective.

**Syndicat recognition and NAO:** Representative trade unions
at 50+ employees trigger the obligation of annual Négociations
Obligatoires (NAO) on remuneration, working time, and gender
equality. Failure to open NAO within the prescribed timeline
exposes the employer to sanctions and reputational risk in
subsequent collective disputes.

**Délit d'entrave:** Obstructing the functioning of a CSE or
impeding trade-union activity constitutes a criminal offence under
Code du travail Art. L.2317-1. This is not a civil-law matter;
it carries potential criminal liability for company directors.
Seek legal review before any action that could be construed as
interfering with representative-body operations.

## Hiring + Termination Discipline

**Trial periods (période d'essai):** Duration is set by the CC;
Code du travail maxima are 2 months ETAM, 3 months cadres, 4 months
senior cadres (renewable once if CC permits). Termination during
trial period requires no justification but must observe Code/CC
notice periods. A trial period not in the contract cannot be imposed.

**CDI vs. CDD:** A CDD requires a legally defined reason (absent-employee replacement, seasonal activity, temporary demand increase). An improperly justified CDD is requalified by the prud'hommes as a CDI; requalification damages apply.

**Licenciement procedure:** Dismissal for personal cause requires:
(1) convocation à entretien préalable with 5-working-day notice;
(2) entretien préalable; (3) notification letter with specific
motive after a 2-working-day cooling-off; (4) compliance with
notice period or payment in lieu. Economic dismissal of 10+
employees in 30 days triggers PSE obligations. Non-compliance at
any procedural step generates prud'hommes damages; the Barème Macron
caps substantive damages (contested in some tribunals).

**Clause de non-concurrence:** Enforceable only when: necessary for legitimate interests, limited in time and geography, specific to the employee's activity, AND the company pays a monthly contrepartie financière throughout the restriction. Absence of financial counterpart renders the clause void.

## Fiscal + Tax Specifics

**TVA (VAT):** Standard rate 20%; reduced rates 5.5% and 10%.
Intra-EU B2B supplies are zero-rated with reverse-charge; verify
TVA intracommunautaire number before issuing zero-rated invoices.
Auto-entrepreneur TVA franchise-en-base threshold applies to
micro-entrepreneurs; verify current thresholds before structuring
delivery through that regime.

**Cotisations sociales:** Employer charges run ~45% on gross
salary; employee charges ~22%. Budget for coût total employeur
when modelling headcount. Charges vary by statut (ETAM vs. cadre)
and applicable exoneration schemes (JEI, ZRR, apprentissage).

**DSN:** Monthly Déclaration Sociale Nominative replaces most
payroll-tax declarations. DSN errors propagate to URSSAF, retraite,
and prévoyance; verify outputs against payroll register before
submission.

**Travail détaché:** Cross-border postings require a Déclaration
Préalable de Détachement and compliance with French minimum-wage
rules. Client companies bear joint liability for unregistered
posted workers in their supply chain.

## Anti-patterns

| Anti-pattern | Failure mode | Correction |
|---|---|---|
| Convention Collective by proximity | Applying Syntec because "most tech companies use it" without verifying NAF/APE code | Confirm NAF/APE code at URSSAF; map to CC using official classification tables; obtain DREETS ruling if ambiguous |
| CIR claim from invoices alone | Claiming CIR for subcontracted R&D without verifying agréé status of the provider | Confirm agréé certification at MESRI registry before contract signature; obtain attestation annually |
| CDD without qualifying reason | Creating a CDD for operational convenience rather than a Code-du-travail-defined motive | Use CDI with trial period for new hires; CDD only when a statutory reason exists and is documented in the contract |
| CSE consultation post-decision | Informing the CSE of a decision already made, then running a formal consultation as formality | Consult CSE during the decision-making process, before the decision is finalised; keep consultation records |
| Non-compete without financial counterpart | Including a non-compete clause without providing contrepartie financière to control costs | Either remove the clause or budget and pay the financial counterpart; void clauses do not protect and may generate damages |
| RGPD consent-wall | Conditioning service access on cookie/analytics consent without a genuine refusal option | Implement refuse-as-easy-as-accept mechanism on the first consent layer per CNIL délibération guidance |
| Prêt d'honneur confusion | Treating prêt d'honneur as a grant; omitting repayment obligation from cash-flow model | Classify as zero-interest personal loan; include repayment schedule in founder cash-flow projections |
| Forfait jours without written agreement | Placing a cadre on forfait jours verbally or by implication | Require a written individual agreement referencing the CC clause authorising forfait jours; document tracking mechanism |

## Cross-References

- `core/compliance-lgpd` — LGPD and RGPD foundational controls,
  data-subject rights, transfer mechanisms, and breach-notification
  procedures; this skill specialises those controls for French
  regulatory context (CNIL, loi Informatique et Libertés, HDS).
- `domains/i18n-business/skills/cultural-intelligence` — cross-cultural
  communication frameworks and cultural-dimension models that provide
  theoretical grounding for the France-specific communication register
  guidance in this skill.
- `domains/i18n-business/skills/language-translator` — formal French
  business-writing conventions, register calibration, and terminology
  accuracy for regulatory and contractual documents.

## ADR Anchors

- **ADR-058** — two-pass review gate; applies to all regulatory
  submissions (Bpifrance applications, CIR declarations, CNIL
  notifications, URSSAF filings) and to employment contracts before
  signature. Any document with legal-compliance consequences must pass
  a second independent review before transmission.
