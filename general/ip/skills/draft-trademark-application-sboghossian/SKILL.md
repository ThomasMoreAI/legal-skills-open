---
name: draft-trademark-application-sboghossian
title: Trademark Application Drafting
description: Use when drafting a trademark application — preparing the applicant details, mark representation, Nice Classification specification, and priority claim for filing with a national registry or via the WIPO Madrid System. Covers specification-drafting discipline (precise vs too vague vs too broad), the GCC unified application, WIPO Madrid, EUIPO, UAE MOEC, KSA SAIP, and Lebanon IP office procedures. Flags the critical rule that overly vague or broad specifications slow examination and weaken enforceability.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-trademark-application
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Trademark Application Drafting

A trademark application claims proprietary rights in a sign (word, logo, combined mark, sound, three-dimensional shape, color) in respect of specified goods and services. The quality of the specification — neither too vague nor too broad — is the single most important factor in examination speed and post-registration enforceability.

## When to use this

- New brand launch requiring trademark protection in one or more jurisdictions
- Expansion of existing trademark registration to new jurisdictions or new classes
- Portfolio filing in connection with a financing round (investors often require TM evidence of ownership before funding)
- Filing a priority claim within 6 months of a first-filed application to extend protection to additional jurisdictions
- Responding to a trademark examination report (not covered here — this skill is for the initial filing only)

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Applicant (legal name, entity type, registered address) | Legal owner of the mark; must be the entity with commercial use rights | Must provide |
| Mark (word / device / combined / sound / 3D / color) | What is being protected | Must provide; logo must be in clean file format |
| Classes under Nice Classification (1–45) | The commercial scope of the application | Must identify all relevant classes |
| Goods/services specification per class | What, precisely, is covered within each class | Must draft carefully |
| Jurisdiction(s) of filing | Determines applicable procedure, fees, and timeline | Must provide |
| Priority claim | Is this based on an earlier filing within 6 months? | Provide prior application number, date, country if claiming |

## Optional inputs

- Representative / attorney details (required for foreign applicants in most jurisdictions)
- Use in commerce evidence (required for US applications; optional elsewhere)
- Transliteration of the mark (for Arabic marks filed in WIPO or Latin-script registries)
- Color claim (if the mark is filed in color and specific colors are claimed as distinctive)
- Power of Attorney / Letter of Authorization (required in MENA, EU, and most other jurisdictions when an attorney files on behalf of the applicant)

## Nice Classification Basics

The Nice Classification (International Classification of Goods and Services, 12th edition current) has 45 classes:
- **Classes 1–34**: goods
- **Classes 35–45**: services

Each class is a separate filing unit (separate fee). Filing in all 45 classes is not appropriate — only classes relevant to the applicant's actual or intended commercial activities.

### Commonly relevant classes for tech and legal-sector companies

| Class | Coverage |
|---|---|
| 9 | Computer software; mobile applications; downloadable content; electronic databases |
| 35 | Business services; online marketplace services; advertising; administrative services |
| 36 | Financial services; insurance; real estate |
| 38 | Telecommunications; communication services; online connectivity |
| 42 | Technology services; SaaS; platform services; legal technology services; research and development |
| 45 | Legal services; personal and social services; security services |

## Specification Drafting

### The governing principle
A specification must be precise enough to be accepted by the examiner, broad enough to cover the applicant's actual and anticipated commercial activities, and honest (applicant must have a bona fide intent to use the mark in relation to the specified goods/services).

### Examples

| Specification | Assessment | Why |
|---|---|---|
| "Computer software for legal document analysis and contract review" | Good | Specific, unambiguous, ties to a real product |
| "Computer software" | Too vague | Examiner will require limitation in most jurisdictions |
| "All goods and services in this class" | Not permitted | Rejected in almost all jurisdictions; not an honest claim |
| "AI-powered legal research and document management software delivered as a service via the internet" | Good | Precise; covers the actual product; acceptable in Class 42 |
| "Legal services" (Class 45) | Acceptable if the applicant is a law firm or LegalTech company providing legal services | But a software company that does not provide legal services directly cannot claim this |

### Use pre-approved terms where possible
Most IP offices provide a database of pre-approved terms (USPTO ID Manual; EUIPO Goods and Services Builder; WIPO Madrid Goods and Services Manager). Using pre-approved terms accelerates examination.

## Per-Jurisdiction Filing Procedures

### WIPO Madrid System
Single filing covers protection in up to 125+ member countries (full list at WIPO.int). Requirements:
- Must have a "basic mark" — an existing trademark registration or pending application in the applicant's home country
- File via the national IP office of the home country (called the "Office of Origin")
- WIPO examines for formalities; each designated jurisdiction then examines on the merits
- 18-month period for designated offices to refuse; if no refusal within 18 months, the mark is registered in that jurisdiction
- Cost: WIPO basic fee + designation fees per country

### GCC Trademark Office
A single application filed with the GCC Patent Office in Riyadh covers trademark protection in all six GCC member states (Saudi Arabia, UAE, Bahrain, Oman, Kuwait, Qatar).
- Examination conducted centrally by the GCC Patent Office
- Once registered, the mark is valid in all six GCC states
- Useful for companies with GCC-wide commercial activity; cheaper than six separate national filings

### UAE — MOEC TM Registry
- Filing: through the UAE Ministry of Economy (MOEC) IP portal
- Examination: distinctiveness, no conflict with prior marks
- Publication: in the Official Gazette for opposition (30 days)
- Registration: certificate issued
- Renewal: every 10 years
- Arabic mark requirement: marks in Arabic or including Arabic text must use the standard Arabic equivalent

### KSA — Saudi Authority for Intellectual Property (SAIP)
- Filing: through SAIP's online portal
- Classification: Nice Classification applies
- Opposition: 60 days post-publication
- Registration validity: 10 years, renewable
- Local agent: foreign applicants must be represented by a KSA-licensed trademark agent
- Arabic text: marks must include an Arabic transliteration/translation if they contain foreign words

### Lebanon — Ministry of Economy and Trade IP Office
- Filing: at the IP Department of the Ministry of Economy and Trade in Beirut
- Examination: strict requirements on distinctiveness and form
- Local presence: foreign applicants require a Lebanese representative
- Official language: Arabic (French accepted in practice for many filings)
- Opposition: 30 days after publication in the Official Gazette
- Registration: 15 years, renewable

### EUIPO — EU Trademark (EUTM)
- Single filing covers all 27 EU member states
- Online filing through EUIPO portal
- Examination: absolute and relative grounds
- Opposition: 3-month opposition period after publication
- Registration: 10 years, renewable
- Unitary character: a EUTM is either registered for all EU members or refused for all (one country's refusal kills the entire application; consider national filings for complex cases)

### UK — Intellectual Property Office (IPO)
- Post-Brexit, EUTM no longer covers UK; separate UK application required
- UK Comparable Marks: existing EUTMs were automatically cloned as equivalent UK marks at Brexit; new EUTMs registered after January 1, 2021 do not cover UK
- Filing through UK IPO portal; 4-month opposition period

### US — USPTO
- Filing through TEAS (Trademark Electronic Application System)
- Two bases: (1) Use in Commerce (already using the mark in US commerce) or (2) Intent to Use (bona fide intention to use, with evidence of use required within 36 months of Notice of Allowance)
- Examination by USPTO examining attorney; Office Actions if issues
- Publication for opposition: 30 days
- Registration: 10 years; Section 8 and 15 declarations required between years 5–6 to maintain registration

## Application Document Components

1. **Applicant details**: full legal name; type of entity (individual, corporation, partnership); registered address; nationality/country of incorporation
2. **Representative** (if filing through an agent): name, firm, address; attach Power of Attorney or Letter of Authorization as required
3. **Mark representation**:
   - Word mark: type the word(s) exactly as they should be registered (capitalization matters)
   - Figurative / device mark: provide a clear, high-resolution image (typically JPEG or PNG, minimum 300 dpi); black and white image for a mark without specific color claim; color image + color claim if specific colors are part of the mark
   - Sound mark: audio file plus a graphic representation (spectrograph or musical notation)
4. **Classification**: list each Nice class number with the proposed goods/services specification for that class
5. **Priority claim**: if claiming Paris Convention priority, state: country of first filing, application number, filing date; the priority claim must be made within 6 months of the priority date
6. **Declaration of use / intent to use**: depends on jurisdiction (mandatory in US; voluntary elsewhere)
7. **Power of Attorney**: if an agent is acting on behalf of the applicant; in many MENA jurisdictions, the POA must be notarized and apostilled/legalized (see below)

## Notarization and Legalization in MENA Jurisdictions

For foreign applicants filing in UAE, KSA, or Lebanon through a local attorney:
- The Power of Attorney must typically be notarized before a notary public in the applicant's home country
- Then legalized (apostilled if the home country is a Hague Convention member; legalized through the UAE/KSA/LB embassy/consulate chain if not)
- UAE, KSA, and Lebanon are parties to the Apostille Convention as of recent years (UAE acceded in 2021; KSA acceded in 2023); confirm current status and applicable procedures

## Anti-Patterns

| Anti-pattern | Risk |
|---|---|
| Filing a vague mark image (low resolution logo) | Rejected; or registration weakened because scope of protection is unclear |
| Overly broad specification in an attempt to block competitors | Examiner will require limitation; in US/EU, registered in broad terms but enforceability limited to actual use |
| Not claiming all relevant classes | Competitors can file in the unclaimed classes; gaps in coverage discovered only when infringement occurs |
| Filing in one jurisdiction and assuming global protection | Trademark rights are territorial; protection only in jurisdictions where registered or where common-law use rights apply |
| Missing the priority window | 6 months from first filing; one day late = no priority claim |

## Related skills

- [[draft-takedown-dmca]]
- [[draft-cease-and-desist]]
- [[review-ip-infringement]]
- [[kb-ip-law-mena]]
