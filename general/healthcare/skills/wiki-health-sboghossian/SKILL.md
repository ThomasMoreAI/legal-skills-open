---
name: wiki-health-sboghossian
title: Healthcare Law in MENA
description: Use when advising on healthcare law, medical licensing, telemedicine regulation, AI-in-healthcare compliance, or medical malpractice in MENA jurisdictions. Covers the licensing and regulatory frameworks of MoH (UAE/KSA/Lebanon/Egypt), DHA, HAAD/DoH, SCFHS, telemedicine rules, data privacy for health records, and the regulatory treatment of AI diagnostic tools. Reach for this skill when the user asks about healthcare licensing, telemedicine law, medical malpractice, or health-sector AI regulation in MENA.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/wiki/wiki-health
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: healthcare
language: en
---

# Healthcare Law in MENA

## Scope

This pack covers the healthcare regulatory frameworks relevant to legal practice in MENA: professional licensing bodies, facility licensing, telemedicine regulation, AI in healthcare, data privacy for health records, and medical malpractice. It is oriented toward legal practitioners advising healthcare clients and legal-AI products that may be used in healthcare compliance contexts.

---

## Regulatory bodies by jurisdiction

### UAE

UAE healthcare regulation operates at three levels: federal, Dubai, and Abu Dhabi.

| Body | Jurisdiction | Key functions |
|---|---|---|
| **Ministry of Health and Prevention (MoHAP)** | UAE federal | Federal health policy, facility licensing in non-emirate-specific zones, drug registration |
| **Dubai Health Authority (DHA)** | Emirate of Dubai | Professional licensing, facility inspection, Dubai Health Insurance Law enforcement |
| **Department of Health – Abu Dhabi (DoH)** | Emirate of Abu Dhabi | Professional licensing in Abu Dhabi, Thiqa insurance scheme |
| **DIFC (healthcare activities)** | DIFC free zone | Healthcare facilities in DIFC are subject to DoH licensing |
| **DHCC (Dubai Healthcare City Authority)** | Dubai Healthcare City free zone | Specialized free zone for healthcare providers; own licensing and standards body |

**Professional licensing in UAE**: Healthcare professionals (physicians, nurses, pharmacists, dentists) must hold a license from the relevant emirate authority. Licensing requires qualification verification, language proficiency testing, and in some cases a prometric exam. There is no single federal practitioner license that works across all emirates; a Dubai-licensed physician must also obtain a DoH license to practice in Abu Dhabi.

### KSA

| Body | Key functions |
|---|---|
| **Ministry of Health (MoH KSA)** | National health policy, public hospital network, facility licensing |
| **Saudi Commission for Health Specialties (SCFHS)** | Professional credentialing and licensing for all health specialties; mandatory for all practitioners |
| **Saudi Food and Drug Authority (SFDA)** | Drug registration, medical device approval, healthcare product safety |
| **National Health Information Center (NHIC)** | Health data standards, electronic health records |

SCFHS licensing is mandatory for any healthcare professional working in KSA regardless of nationality. The Commission maintains a Prometric-based examination system and a DataFlow credential verification requirement for foreign-trained professionals.

### Lebanon

| Body | Key functions |
|---|---|
| **Ministry of Public Health (MoPH Lebanon)** | Facility licensing, drug registration |
| **Lebanese Medical Council (Ordre des Médecins)** | Physician licensing; membership mandatory to practice |
| **Order of Nurses of Lebanon** | Nursing licensing |

Lebanon's healthcare regulatory system has been significantly strained by the economic crisis since 2019. Brain drain of healthcare professionals is a significant regulatory enforcement challenge; many licensed physicians practice abroad while maintaining Lebanese registration.

### Egypt

| Body | Key functions |
|---|---|
| **Ministry of Health and Population (MoHP Egypt)** | National policy, public facilities, drug registration |
| **Egyptian Medical Syndicate** | Physician licensing and professional conduct |
| **Health Insurance Authority (HIA)** | Administers universal health insurance (rolled out under the 2018 Health Insurance Law) |

---

## Telemedicine regulation

Telemedicine has expanded rapidly across MENA post-COVID. Regulatory status:

| Jurisdiction | Status | Key requirements |
|---|---|---|
| UAE (federal/DHA) | Permitted; licensed platforms only | Platform must hold DHA telehealth facility license; prescribing physician must be DHA/DoH licensed; patient consent required |
| KSA | Permitted via licensed platforms | SFDA/MoH approved platforms; prescribing controlled substances via telemedicine restricted |
| Lebanon | Limited regulation; practice evolving | No comprehensive telemedicine law; practitioners use general licensing rules |
| Egypt | Law 180/2023 provides framework | Electronic health records required; physician must be licensed in Egypt |
| DIFC/ADGM | Allowed but practitioners must hold UAE licensing authority license | Free zone status does not exempt from DHA/DoH licensing requirements for clinical practice |

**Cross-border telemedicine**: A physician in Lebanon treating a UAE patient via video call falls into a regulatory grey zone — Lebanese licensing applies to the physician, but UAE patient-protection rules may also apply. Most MENA jurisdictions take the position that telemedicine to patients in their jurisdiction requires local licensure; cross-border practice without local license is an enforcement risk.

---

## AI in healthcare: regulatory treatment

The use of AI tools for diagnosis, clinical decision support, and treatment recommendation is an emerging regulatory area across MENA.

### UAE

The DHA has issued guidance on AI-enabled medical devices. AI-powered diagnostic tools are classified as medical devices if they make or influence clinical decisions, and are subject to SFDA medical device registration. Software-as-a-Medical-Device (SaMD) follows international frameworks (IMDRF).

### KSA

The SFDA regulates medical devices including AI-enabled software. The Saudi Data and AI Authority (SDAIA) has issued an AI ethics framework that applies to AI in healthcare. AI systems used in clinical settings must comply with both SFDA device regulation and SDAIA ethical requirements.

### Data privacy for health records

Health data is classified as sensitive data across all MENA jurisdictions:

| Jurisdiction | Framework | Key obligation |
|---|---|---|
| UAE | UAE PDPL (Federal Decree-Law No. 45/2021) | Explicit consent required for health data processing; enhanced security obligations |
| KSA | KSA PDPL (Royal Decree M/19) | Sensitive data provisions; health data requires explicit consent; data localisation |
| DIFC | DIFC Data Protection Law 2020 | Special category data; explicit consent + DPO designation |
| ADGM | ADGM DPR 2021 | Same as DIFC; FSRA oversight |
| Lebanon | No comprehensive PDPL | Medical confidentiality under Medical Ethics Code applies |
| Egypt | Egypt PDPL (Law 151/2020) | Sensitive data; explicit consent; cross-border restrictions |

---

## Medical malpractice

### UAE framework

Medical malpractice in UAE is governed by Federal Law No. 4/2016 on Medical Liability. Key provisions:
- Establishes mandatory Medical Liability Insurance for all practitioners and facilities
- Medical Liability Committee (operated by each health authority) adjudicates claims before court proceedings
- Compensation is payable in three categories: death (Diya / blood money under UAE Civil Code), permanent disability, and temporary disability
- Criminal liability is possible for gross negligence; practitioners can face prosecution under the Penal Code in addition to civil liability

### KSA framework

KSA medical malpractice operates under both Sharia principles and the Health Practitioner Law. Diya (blood money) applies where death results from medical error; compensation rates are set by the Saudi government periodically. The Ministry of Health has a medical error committee system for investigation prior to court proceedings.

### Lebanon framework

Lebanon applies the general civil law of obligations (tort) to medical malpractice. Physicians are held to a duty of means (obligation de moyens), not a duty of result — they must apply reasonable professional care, not guarantee outcomes. The Lebanese Court of Cassation has developed significant case law on the standard of care.

---

## Caveats & currency

Healthcare regulations in MENA change frequently, particularly post-COVID as telemedicine frameworks were established and AI-in-healthcare guidance is being actively developed. The regulatory status of telemedicine and AI tools in each jurisdiction should be verified against current regulatory guidance from the relevant authority before advising clients. Licensing requirements change; verify with DHA, DoH, SCFHS, and MoPH websites for current qualification and documentation requirements.

---

## Related skills

- [[wiki-legal]]
- [[wiki-geopolitics]]
- [[wiki-haqq-product]]
- [[wiki-real-estate]]
