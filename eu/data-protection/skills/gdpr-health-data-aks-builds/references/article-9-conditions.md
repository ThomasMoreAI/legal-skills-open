# GDPR Article 9 — Conditions for Processing Health Data

A working reference for the lawful conditions that permit processing of special category data (which includes data concerning health, genetic data, and biometric data for the purpose of uniquely identifying a natural person) under GDPR Article 9. Verify the current text of GDPR (Regulation 2016/679), national Member State derogations adopted under Art. 9(4), and current EDPB / supervisory authority guidance. Consult your DPO and counsel for binding determinations — Article 9 analysis is fact-specific and Member-State-dependent.

## How Article 9 Works

Article 9(1) prohibits processing of special category data by default. Article 9(2) lists the conditions under which processing is permitted — at least one Art. 9(2) condition must apply. In addition, a separate Art. 6(1) lawful basis is required (consent / contract / legal obligation / vital interests / public task / legitimate interests, with health-specific caveats). The two are stacked, not alternatives. Verify with EDPB guidance — there has been guidance and case law on whether the Art. 6 basis is truly required separately, or whether the Art. 9(2) condition is sufficient on its own; conservative practice stacks both.

## The Article 9(2) Conditions

### (a) Explicit Consent
The data subject has given **explicit consent** to processing for one or more specified purposes, except where Union or Member State law provides that the prohibition cannot be lifted by consent.

**Healthcare examples**: Research consent in academic studies, opt-in consent to commercial wellness apps, consent to share health data with a third-party (e.g., genetic testing service sharing results with a partner).

**Caveats**: Consent must be freely given, specific, informed, unambiguous (Art. 4(11)), and explicit (a higher bar than ordinary consent — typically a clear affirmative statement). Can be withdrawn at any time (Art. 7(3)). Power imbalance (e.g., employer-employee, clinician-patient) can invalidate consent.

### (b) Employment, Social Security, Social Protection
Processing necessary for carrying out the obligations and exercising specific rights of the controller or data subject in the field of **employment, social security, and social protection law**, in so far as authorised by Union or Member State law.

**Healthcare examples**: Occupational health screening required by national law, sick-leave administration, social-insurance health benefit processing.

**Caveats**: Specific Member State law must underpin the processing.

### (c) Vital Interests
Processing necessary to protect the **vital interests** of the data subject or of another natural person where the data subject is physically or legally incapable of giving consent.

**Healthcare examples**: Emergency treatment of an unconscious patient, public-health emergencies, search and rescue.

**Caveats**: Narrow. The data subject must be incapable of giving consent — not just unavailable. Other lawful conditions are preferred where they apply.

### (d) Legitimate Activities of Foundations / Associations
Processing carried out in the course of legitimate activities with appropriate safeguards by a **foundation, association or any other not-for-profit body with a political, philosophical, religious or trade union aim**, and on condition that the processing relates solely to the members or to former members, or to persons who have regular contact with it in connection with its purposes, and that the personal data are not disclosed outside that body without the consent of the data subjects.

**Healthcare examples**: Patient advocacy organizations processing member health data.

### (e) Data Manifestly Made Public by the Data Subject
Processing relates to personal data which are **manifestly made public** by the data subject.

**Healthcare examples**: Patient-authored public blogs about their condition, public social media posts about treatment. **Caveats**: "Manifestly" is a high bar; data must be put in the public domain by the data subject themselves, not by others.

### (f) Establishment, Exercise, or Defence of Legal Claims
Processing necessary for the **establishment, exercise or defence of legal claims** or whenever courts are acting in their judicial capacity.

**Healthcare examples**: Litigation discovery, medical malpractice defense, regulatory investigation response.

### (g) Substantial Public Interest
Processing necessary for reasons of **substantial public interest**, on the basis of Union or Member State law which shall be proportionate to the aim pursued, respect the essence of the right to data protection, and provide for suitable and specific measures to safeguard the fundamental rights and the interests of the data subject.

**Healthcare examples**: Various national-law-based health processing (varies widely by Member State); national health registries, anti-fraud in health insurance.

**Caveats**: Always requires specific Member State law as the substrate.

### (h) Preventive or Occupational Medicine, Medical Diagnosis, Provision of Health or Social Care
Processing necessary for the purposes of **preventive or occupational medicine**, for the **assessment of the working capacity** of the employee, **medical diagnosis**, the **provision of health or social care or treatment** or the **management of health or social care systems and services** on the basis of Union or Member State law or pursuant to contract with a health professional and subject to the conditions and safeguards referred to in paragraph 3.

**Healthcare examples**: This is the **workhorse condition** for routine clinical care. EHR processing, hospital information systems, primary care, diagnostic imaging, prescribing.

**Conditions of paragraph 3**: Processing must be by or under the responsibility of a professional subject to the obligation of professional secrecy under Union or Member State law or rules established by national competent bodies, or by another person also subject to an obligation of secrecy.

### (i) Public Interest in the Area of Public Health
Processing necessary for reasons of **public interest in the area of public health**, such as protecting against serious cross-border threats to health or ensuring high standards of quality and safety of health care and of medicinal products or medical devices, on the basis of Union or Member State law providing for suitable and specific measures to safeguard the rights and freedoms of the data subject.

**Healthcare examples**: Disease surveillance, pharmacovigilance, medical device vigilance, pandemic response, vaccine effectiveness studies.

### (j) Archiving, Scientific or Historical Research, Statistical Purposes
Processing necessary for **archiving purposes in the public interest, scientific or historical research purposes or statistical purposes** in accordance with Article 89(1), based on Union or Member State law which shall be proportionate to the aim pursued, respect the essence of the right to data protection, and provide for suitable and specific measures to safeguard the fundamental rights and the interests of the data subject.

**Healthcare examples**: Clinical research, registry studies, retrospective observational research, biobank operation.

**Conditions of Art. 89(1)**: Appropriate technical and organisational measures (pseudonymization, etc.), data minimisation, derogations from data subject rights where they would render the research purpose impossible — verify Member State implementation.

## Article 6(1) Lawful Basis (Stacked)

Conservative practice requires identifying both an Art. 9(2) condition AND an Art. 6(1) basis. Common combinations:

| Art. 9(2) | Common Art. 6(1) basis |
|---|---|
| (a) Explicit consent | (a) Consent |
| (h) Medical diagnosis / treatment | (b) Contract (with patient), (c) legal obligation (with national health law), (e) public task (for public health systems) |
| (i) Public health | (c) Legal obligation, (e) public task |
| (j) Scientific research | (e) Public task, (f) legitimate interests (with documented LIA), (a) consent |

Verify with EDPB / SA guidance for the current view on stacking.

## Article 9(4) — Member State Derogations

Art. 9(4) permits Member States to **maintain or introduce further conditions, including limitations, with regard to the processing of genetic data, biometric data or data concerning health**. This is why Member State law matters enormously for health data:

- **Germany (BDSG)**: Specific provisions for health data, employer health processing, social security
- **France (Code de la santé publique + CNIL deliberations)**: Detailed health-data-processing framework, methodology references (MR-001, MR-003, MR-004, MR-005, etc.) for research, national health data platform (Health Data Hub)
- **Italy (Codice Privacy + Garante guidance)**: Specific health-data rules
- **Spain (LOPDGDD)**: National implementing law with health-data provisions
- **Netherlands (UAVG)**: Implementing law with sector-specific provisions
- **Ireland (Data Protection Act 2018)**: Health Research Regulations require explicit consent (with limited exceptions) — stricter than the GDPR baseline
- **UK (UK GDPR + DPA 2018)**: Post-Brexit, applies in parallel with EU GDPR for UK residents; verify current adequacy decision status

This list is illustrative — verify each Member State's current law and supervisory authority guidance with local counsel.

## Practical Decision Pattern

1. **Identify the processing purpose** in concrete terms (clinical care, research, public health, commercial wellness, etc.)
2. **Map to one (or more) Art. 9(2) conditions** — usually (h) for clinical care, (j) for research, (i) for public health, (a) for direct-to-consumer
3. **Identify the Art. 6(1) lawful basis** that pairs with it
4. **Identify the Member State derogations under Art. 9(4)** that apply
5. **Confirm the safeguards** required by Art. 9(3) (professional secrecy) and/or Art. 89 (research safeguards) are in place
6. **Document the decision** in the records of processing (Art. 30) and, where required, in a DPIA
7. **Route the binding determination to DPO and counsel**

## Final Disclaimers

- Verify the current text of Articles 6, 9, 27, 30, 35, 36, 89, and the relevant recitals
- Verify each Member State's national implementing law and supervisory authority guidance
- Consult your DPO and local counsel — Article 9 analysis is jurisdiction-specific and fact-specific
- This reference is a working aid, not legal advice
