---
name: nda-drug-application
title: New Drug Application (NDA)
description: Drafts an eCTD-compliant New Drug Application (NDA) for FDA submission under 21 CFR Part 314. Compiles clinical trial data, CMC documentation, nonclinical studies, pharmacokinetics, integrated safety analyses, and proposed labeling into five-module eCTD structure. Use when preparing an NDA, FDA drug approval submission, pharmaceutical regulatory filing, or eCTD assembly for a new molecular entity.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/nda-drug-application
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: life-sciences
language: en
tags: [analysis, drafting]
---

# New Drug Application (NDA)

Drafts an eCTD-compliant NDA demonstrating safety and efficacy for FDA submission under 21 CFR Part 314.

## Prerequisites

1. **Clinical trial data** — Phase 1–3 protocols, CSRs, statistical analyses, patient demographics
2. **CMC documentation** — drug substance characterization, manufacturing process, batch records, stability data
3. **Nonclinical study reports** — pharmacology, toxicology (general, genetic, reproductive, carcinogenicity), safety pharmacology
4. **PK/bioavailability data** — human PK, special populations, DDI studies, exposure-response analyses
5. **Regulatory correspondence** — pre-IND/pre-NDA meeting minutes, special protocol assessments, FDA feedback
6. **Proposed labeling drafts** — if available
7. **Patent and exclusivity information** — patent numbers, expiration dates, exclusivity claims

## Output Structure

### Module 1: Administrative Information

| Element | Requirements |
|---|---|
| Cover letter | Sponsor details, application type, regulatory pathway, special designations (breakthrough, fast track, priority review, orphan) |
| FDA Form 356h | User fee info, debarment certification, field copy designations |
| Proposed names | Proprietary and established names |
| Indication statement | Precise medical terminology, dosage form, route, strength(s) |
| Regulatory strategy | Reference pre-submission meetings, SPAs, unmet medical need narrative |

### Module 2: Summaries

#### 2.5 Integrated Summary & Benefit-Risk

- Pharmacological class, MOA, therapeutic rationale
- Development program overview (nonclinical → Phase 1 → 2 → 3 logic)
- Pivotal trial summaries: design, population, endpoints, results (point estimates, CIs, p-values)
- Integrated safety: AE profile across program, SAEs, deaths, safety signals
- Risk mitigation: labeling, REMS if applicable
- Benefit-risk weighing per 21 CFR 314.50(c): efficacy magnitude vs. AE frequency/severity, disease seriousness, existing therapies

#### 2.3 Quality Overall Summary (CMC)

| Area | Key Elements |
|---|---|
| Drug substance | Chemical name, structure (stereochemistry), MW, solubility, polymorphism, particle size |
| Synthetic pathway | Starting materials, reagents, CPPs, in-process controls, impurity profile with qualification |
| Drug product | Quantitative formulation, excipient justification, compatibility evidence |
| Manufacturing | Flow diagrams, equipment specs, CPP ranges, process validation (≥3 batches) |
| Analytical methods | Validated for identity, assay, impurities, dissolution, CU |
| Stability | ICH Q1A (long-term, intermediate, accelerated), stability-indicating methods, trending |
| Container closure | System compatibility; device components if applicable (specs, human factors) |
| Compliance | 21 CFR Parts 210/211 (cGMP) |

#### 2.4 Nonclinical Overview

| Study Type | Key Elements |
|---|---|
| Primary pharmacodynamics | In vitro binding/functional assays, in vivo disease models |
| Secondary pharmacodynamics | Off-target activity screen |
| Safety pharmacology | hERG, in vivo QT, respiratory, CNS |
| PK (animal) | ADME across tox species, metabolite ID, cross-species comparison |
| Acute toxicity | Dose-response, target organ ID |
| Repeat-dose toxicity | Duration matching intended clinical use, recovery data |
| Genetic toxicology | Ames, in vitro chromosomal aberration, in vivo micronucleus |
| Carcinogenicity | Two species (if chronic use), adequate duration/power |
| Reproductive toxicity | Fertility, embryo-fetal (two species), pre/postnatal development |

All studies GLP-compliant per ICH M3(R2). Bridge nonclinical findings to clinical: starting dose selection, monitoring parameters, contraindications.

#### 2.7 Clinical Summary

**Pharmacokinetics:** ADME profile — absorption (food effect, bioavailability), distribution (Vd, protein binding), metabolism (CYP isoforms, DDI potential), elimination (clearance, t½). Special populations: renal (mild→ESRD), hepatic (Child-Pugh A/B/C), elderly, pediatric, pharmacogenomics. Bioequivalence bridging if formulation changed. Exposure-response analysis → dosing justification.

**Clinical Efficacy:** Phase 1 (safety, PK, dose range) → Phase 2 (dose-ranging, dose selection rationale) → Phase 3 pivotal trials. For each pivotal trial: design/randomization/blinding, population (I/E criteria), primary + secondary endpoints, statistical plan (sample size, missing data, multiplicity), results with CIs and p-values, clinical meaningfulness. Include cross-trial consistency, subgroup analyses (age, sex, race, severity), and failed/negative trial explanations. Follow ICH E3 for CSR format.

**Integrated Safety:** Database size (total exposed, patient-years) vs. FDA adequacy guidance. Common AEs by SOC/PT (MedDRA) with dose-response. SAE narratives with causality. Death narratives (investigator + sponsor causality). Discontinuation rates. Lab shifts, vitals, ECG/QTc. Class-specific topics: hepatotoxicity (Hy's Law), immunogenicity (ADA), hypersensitivity, CV events, malignancies. Signal detection via disproportionality analysis.

### Proposed Labeling (Module 1)

Draft per Physician Labeling Rule (21 CFR 201.56–57):

| Section | Key Requirements |
|---|---|
| Highlights | ≤½ page; recent changes, indication, dosing, contraindications, warnings, AEs |
| Indications & Usage | Precise population, condition, limitations |
| Dosage & Administration | Dose selection, preparation, technique, adjustments |
| Contraindications | Evidence-based; clear statements |
| Warnings & Precautions | By clinical importance; boxed warning if warranted |
| Adverse Reactions | Table format (incidence), SAE detail, discontinuation AEs |
| Drug Interactions | Clinically significant; management recommendations |
| Specific Populations | Pregnancy (registry if applicable), lactation, pediatric, geriatric |
| Clinical Pharmacology | MOA, PK summary |
| Clinical Studies | Designs + results supporting indication |

Include Medication Guide if serious public health concern; Instructions for Use if device component or complex administration.

### Risk Management, Patent & Exclusivity, Environmental

- **REMS** (if applicable): goals, ETASU, implementation system, assessment timetable
- **Patent**: numbers, expiration dates, certifications; exclusivity claims (NCE 5 yr, orphan 7 yr, pediatric 6 mo)
- **Environmental**: claim categorical exclusion under 21 CFR 25.31; calculate EIC (max daily dose × annual patient population → aquatic concentration < 1 ppb); full EA if threshold exceeded

## eCTD Assembly Checklist

- [ ] Module 1: Administrative, labeling, patent info
- [ ] Module 2: Summaries (quality, nonclinical, clinical)
- [ ] Module 3: Quality (CMC) full data
- [ ] Module 4: Nonclinical study reports
- [ ] Module 5: Clinical study reports
- [ ] Cross-references and hyperlinks between modules
- [ ] Consistent terminology throughout
- [ ] Proper eCTD file naming and metadata
- [ ] Gap analysis: flag missing data and strategic decision points

## Guidelines

1. **Trace conclusions to source data** — never assert efficacy or safety without citing specific trial results or study findings
2. **Anticipate FDA questions** — proactively address data limitations, alternative interpretations, ambiguous precedents
3. **Statistical rigor** — include point estimates, CIs, p-values; distinguish statistical from clinical significance
4. **Mark gaps explicitly** — flag missing data with `[DATA NEEDED: description]`
5. **Regulatory citations** [VERIFY current versions]: 21 CFR Part 314, 21 CFR Parts 210/211, 21 CFR 201.56–57, 21 CFR 25.31/25.40, ICH Q1A, ICH E3, ICH M3(R2)
6. **U.S. FDA jurisdiction only** — do not extrapolate to EMA, PMDA, or other authorities unless instructed
7. **Draft for sponsor review** — mark areas requiring sponsor input, additional data, or strategic decisions before submission
