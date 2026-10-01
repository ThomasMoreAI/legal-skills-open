---
name: medical-standards-sencersoylu
title: Medical Research Standards
description: Medical research standards including IRB/Helsinki ethics, HIPAA, MeSH terminology, and ICMJE authorship criteria
author: sencersoylu
author_url: https://github.com/sencersoylu/scholar-flow/tree/main/skills/discipline/medical-standards
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: life-sciences
language: en
---

# Medical Research Standards

Comprehensive standards and regulatory requirements for medical and health sciences research. This skill provides protocols for ethics, privacy, terminology, authorship, trial registration, reporting, and conflict of interest disclosure.

## When to Use

- When designing any medical, clinical, or health sciences research study
- When preparing an IRB/ethics committee submission
- When handling patient or health data
- When determining authorship for a medical publication
- When registering a clinical trial
- When selecting a reporting guideline
- When drafting conflict of interest disclosures

---

## Protocol

### 1. Research Ethics

#### 1.1 Declaration of Helsinki

The World Medical Association Declaration of Helsinki (last amended 2013) establishes ethical principles for medical research involving human subjects. Key principles:

1. **Primacy of participant welfare** -- the well-being of the individual research subject takes precedence over all other interests
2. **Scientific validity** -- research must be based on thorough knowledge of the scientific literature and adequate laboratory/animal experimentation
3. **Protocol review** -- every research study must be submitted to an independent ethics committee for review before commencement
4. **Informed consent** -- participation must be voluntary, with adequate information provided in understandable language
5. **Privacy and confidentiality** -- every precaution must be taken to protect the privacy of participants and the confidentiality of their data
6. **Vulnerable populations** -- additional protections are required for groups that are vulnerable to coercion or undue influence (children, prisoners, cognitively impaired individuals, economically disadvantaged persons)
7. **Risk-benefit assessment** -- research is justified only if the potential benefits outweigh the risks
8. **Post-study access** -- provisions should be made for post-study access to interventions identified as beneficial

#### 1.2 Institutional Review Board (IRB) / Ethics Committee

Application requirements:

1. Study protocol with scientific justification
2. Principal investigator qualifications and training (e.g., CITI certification)
3. Informed consent form(s) -- must include: purpose, procedures, risks, benefits, alternatives, confidentiality measures, voluntary participation statement, contact information
4. Recruitment materials and procedures
5. Data collection instruments
6. Data management and security plan
7. Risk assessment and mitigation strategies
8. Funding sources and potential conflicts of interest
9. HIPAA authorization form (if applicable in the US)

Review categories:
- **Exempt** -- minimal risk, existing data, educational tests, surveys of non-sensitive topics
- **Expedited** -- no more than minimal risk, minor changes to approved research
- **Full board** -- greater than minimal risk, vulnerable populations, investigational drugs/devices

#### 1.3 Informed Consent Requirements

Mandatory elements (per 45 CFR 46.116):
- Statement that the study involves research
- Explanation of purposes and expected duration
- Description of procedures
- Description of reasonably foreseeable risks
- Description of expected benefits
- Disclosure of alternative treatments
- Confidentiality assurances
- Compensation and treatment for injury (if applicable)
- Contact information for questions
- Statement that participation is voluntary

### 2. Privacy and Data Protection

#### 2.1 HIPAA (United States)

The Health Insurance Portability and Accountability Act Privacy Rule governs Protected Health Information (PHI). The 18 HIPAA identifiers that must be removed for de-identification (Safe Harbor method):

1. Names
2. Geographic data smaller than state
3. Dates (except year) related to an individual
4. Telephone numbers
5. Fax numbers
6. Email addresses
7. Social Security numbers
8. Medical record numbers
9. Health plan beneficiary numbers
10. Account numbers
11. Certificate/license numbers
12. Vehicle identifiers and serial numbers
13. Device identifiers and serial numbers
14. Web URLs
15. IP addresses
16. Biometric identifiers
17. Full-face photographs
18. Any other unique identifying number or code

Research use of PHI requires one of:
- Individual authorization
- IRB or Privacy Board waiver
- De-identified data (Safe Harbor or Expert Determination method)
- Limited data set with Data Use Agreement

#### 2.2 GDPR (European Union)

The General Data Protection Regulation applies to health data as a "special category" of personal data. Requirements:

- **Lawful basis** -- explicit consent or public interest in health (Article 9(2))
- **Data Protection Impact Assessment (DPIA)** -- required for large-scale processing of health data
- **Data minimization** -- collect only what is necessary for the research purpose
- **Right to erasure** -- participants can request data deletion (subject to research exemptions under Article 89)
- **Data Protection Officer (DPO)** -- required for organizations processing health data at scale
- **Cross-border transfers** -- Standard Contractual Clauses or adequacy decisions required for transfers outside the EU/EEA
- **Breach notification** -- supervisory authority must be notified within 72 hours of a personal data breach

### 3. Terminology and Classification

#### 3.1 MeSH (Medical Subject Headings)

MeSH is the NLM controlled vocabulary thesaurus used for indexing PubMed articles.

Usage protocol:
1. Search the MeSH database (https://meshb.nlm.nih.gov/) to find official terms
2. Use MeSH terms in search strategies for systematic reviews
3. Combine MeSH terms with free-text keywords using Boolean operators
4. Use MeSH subheadings (qualifiers) to narrow searches (e.g., "Diabetes Mellitus/therapy")
5. Exploit the MeSH tree hierarchy -- search broader terms to capture all narrower concepts
6. Use [MeSH Major Topic] to find articles where the term is a primary focus

#### 3.2 ICD Coding

- **ICD-10** -- International Classification of Diseases, 10th Revision, for diagnoses and conditions
- **ICD-10-PCS** -- Procedure Coding System for inpatient procedures
- Use standardized ICD codes in study definitions for reproducibility
- Report ICD version and specific codes used in the Methods section

### 4. Authorship

#### 4.1 ICMJE Authorship Criteria

The International Committee of Medical Journal Editors defines authorship by four criteria. All four must be met:

1. **Substantial contributions** to the conception or design of the work; or the acquisition, analysis, or interpretation of data for the work; AND
2. **Drafting the work** or revising it critically for important intellectual content; AND
3. **Final approval** of the version to be published; AND
4. **Agreement to be accountable** for all aspects of the work in ensuring that questions related to the accuracy or integrity of any part of the work are appropriately investigated and resolved

Important notes:
- Acquisition of funding, collection of data, or general supervision alone does not justify authorship
- All persons designated as authors should meet all four criteria
- Contributors who do not meet all four criteria should be listed in Acknowledgments
- The corresponding author must ensure all listed authors meet criteria and that no deserving authors are omitted

#### 4.2 CRediT (Contributor Roles Taxonomy)

The 14 CRediT roles for transparent attribution:

| Role | Definition |
|------|-----------|
| Conceptualization | Ideas; formulation of research goals and aims |
| Data curation | Annotation, scrubbing, and maintenance of research data |
| Formal analysis | Application of statistical, mathematical, or computational techniques |
| Funding acquisition | Acquisition of financial support |
| Investigation | Conducting research and investigation process |
| Methodology | Development or design of methodology |
| Project administration | Management and coordination |
| Resources | Provision of study materials, reagents, patients, laboratory samples, computing resources |
| Software | Programming, software development, computer code design |
| Supervision | Oversight and leadership responsibility |
| Validation | Replication/reproducibility of results |
| Visualization | Data presentation, figures, tables |
| Writing -- original draft | Preparation of the initial manuscript |
| Writing -- review and editing | Critical review and revision |

### 5. Trial Registration

#### 5.1 ClinicalTrials.gov

ICMJE requires prospective registration of all clinical trials before enrollment of the first participant.

Required registration data elements:
1. Study title and acronym
2. Study type (interventional or observational)
3. Study phase (I, II, III, IV)
4. Study design (allocation, intervention model, masking, primary purpose)
5. Conditions or diseases studied
6. Interventions (drug, device, procedure, behavioral, other)
7. Primary and secondary outcome measures with time frames
8. Eligibility criteria (inclusion and exclusion)
9. Target enrollment
10. Study start and estimated completion dates
11. Sponsor and collaborators
12. Principal investigator
13. Study locations

Registration number (NCT number) must be included in the manuscript abstract and methods section.

#### 5.2 WHO International Clinical Trials Registry Platform (ICTRP)

WHO ICTRP maintains a network of registries meeting international standards. Acceptable primary registries include:
- ClinicalTrials.gov (US)
- EU Clinical Trials Register (EUCTR)
- ISRCTN Registry
- ANZCTR (Australia/New Zealand)
- CTRI (India)
- ChiCTR (China)

### 6. Reporting Guidelines (EQUATOR Network)

Select the appropriate reporting guideline based on study design:

| Study Design | Guideline | Key Items |
|-------------|-----------|-----------|
| Randomized controlled trial | CONSORT 2010 | 25 items |
| Observational study (cohort, case-control, cross-sectional) | STROBE | 22 items |
| Systematic review / meta-analysis | PRISMA 2020 | 27 items |
| Diagnostic accuracy study | STARD 2015 | 30 items |
| Case report | CARE | 13 items |
| Quality improvement study | SQUIRE 2.0 | 18 items |
| Animal research | ARRIVE 2.0 | 21 items |
| Economic evaluation | CHEERS 2022 | 28 items |
| Qualitative research | COREQ | 32 items |

Access all checklists at https://www.equator-network.org/

### 7. Conflict of Interest Disclosure

#### 7.1 ICMJE COI Form

All authors must complete the ICMJE Disclosure of Interest form covering:

1. **Financial activities** -- grants, consulting fees, honoraria, royalties, stock/stock options, patents, expert testimony received in the past 36 months related to the submitted work
2. **Financial activities outside the submitted work** -- same categories for activities not directly related
3. **Intellectual property** -- patents planned, pending, or issued
4. **Other relationships** -- membership on advisory boards, committees, or other relationships that could be perceived as influencing the work
5. **Institutional COI** -- financial relationships held by the authors' institutions

Disclosure principles:
- When in doubt, disclose
- Disclose relationships from the past 36 months
- Include relationships regardless of whether the author believes they constitute a conflict
- The corresponding author is responsible for collecting and submitting all authors' forms

---

## Checklist

### Ethics and Compliance
- [ ] Study protocol reviewed and approved by IRB/ethics committee
- [ ] Approval number documented in manuscript
- [ ] Informed consent obtained from all participants (or waiver documented)
- [ ] Helsinki Declaration compliance stated in Methods
- [ ] CITI or equivalent ethics training completed by all investigators

### Privacy
- [ ] PHI/personal data handling complies with HIPAA and/or GDPR
- [ ] De-identification performed using validated method
- [ ] Data security measures documented
- [ ] Data sharing agreements in place (if multi-site)

### Terminology
- [ ] MeSH terms used in search strategies
- [ ] ICD codes reported for diagnoses (where applicable)
- [ ] Standardized nomenclature used consistently

### Authorship
- [ ] All authors meet all four ICMJE criteria
- [ ] CRediT roles assigned and documented
- [ ] Non-qualifying contributors listed in Acknowledgments
- [ ] Author order agreed upon by all authors

### Registration
- [ ] Clinical trial registered before first participant enrolled
- [ ] Registration number included in abstract and methods
- [ ] Registered outcomes match reported outcomes (or discrepancies explained)

### Reporting
- [ ] Appropriate EQUATOR guideline identified
- [ ] Reporting checklist completed with page/paragraph references
- [ ] Checklist submitted with manuscript

### Conflicts of Interest
- [ ] All authors completed ICMJE COI forms
- [ ] COI statement included in manuscript
- [ ] Funding sources fully disclosed

---

## References

- World Medical Association. Declaration of Helsinki -- Ethical Principles for Medical Research Involving Human Subjects. JAMA. 2013;310(20):2191-2194. doi:10.1001/jama.2013.281053
- International Committee of Medical Journal Editors. Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals. Updated 2023. http://www.icmje.org/recommendations/
- US Department of Health and Human Services. 45 CFR Part 46 -- Protection of Human Subjects. https://www.hhs.gov/ohrp/regulations-and-policy/regulations/45-cfr-46/
- US Department of Health and Human Services. HIPAA Privacy Rule. https://www.hhs.gov/hipaa/for-professionals/privacy/
- European Parliament. General Data Protection Regulation (EU) 2016/679. https://gdpr.eu/
- National Library of Medicine. Medical Subject Headings (MeSH). https://meshb.nlm.nih.gov/
- Brand A, Allen L, Altman M, Hlava M, Scott J. Beyond authorship: attribution, contribution, collaboration, and credit. Learned Publishing. 2015;28(2):151-155. doi:10.1087/20150211
- EQUATOR Network. Enhancing the QUAlity and Transparency Of health Research. https://www.equator-network.org/
- ClinicalTrials.gov. Protocol Registration Data Element Definitions. https://prsinfo.clinicaltrials.gov/definitions.html
