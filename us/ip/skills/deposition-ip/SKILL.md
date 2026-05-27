---
name: deposition-ip
title: IP Litigation Deposition Supplement
description: Supplements general deposition preparation with IP-specific examination frameworks for patent, trademark, copyright, and trade secret cases. Covers witness strategies for inventors, accused infringers, licensing witnesses, and experts. Use alongside @deposition-preparation and @deposition-expert-witness when planning IP depositions, drafting outlines, or analyzing witness strategy.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-ip
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# IP Litigation Deposition Supplement

Adds IP-specific examination frameworks to @deposition-preparation. Covers four case types — patent, trademark, copyright, trade secret — with witness-specific question lines and damages theory.

## Prerequisites

- Relevant patents, registrations, or trade secret identification statements
- Prosecution history and claim construction positions (patent)
- Prior art references at issue
- Accused product/process technical documentation
- Licensing history and comparable licenses
- Expert reports (if designated)
- Confidentiality agreements (trade secret)

## Case Type Reference

| Case Type | Key Issues | Primary Witnesses |
|-----------|-----------|-------------------|
| **Patent** | Claim construction, infringement (literal/DOE), validity, reasonable royalty, lost profits, willfulness | Inventor, R&D/engineering, licensing/business, technical expert, damages expert |
| **Trademark** | Distinctiveness, priority of use, likelihood of confusion, willfulness, damages | Mark owner, marketing, consumer survey expert, damages expert |
| **Copyright** | Ownership, originality, access/copying, substantial similarity, fair use | Author/creator, access witnesses, similarity expert, damages expert |
| **Trade Secret** | Existence, reasonable secrecy measures, misappropriation, damages | Developer, accused misappropriator, security witnesses, damages expert |

## Patent Examination Frameworks

### Inventor

- **Conception/reduction to practice**: When conceived, what problem solved, corroborating records, who was told, prototyping/testing timeline
- **Prior art knowledge**: Awareness at time of invention, searches conducted, how invention differs from specific references — failure to disclose bears on inequitable conduct
- **Claims/prosecution**: Understanding of claim 1, meaning of disputed terms, involvement in prosecution, reasons for amendments

### Accused Infringer Technical Witness

- **Product/process**: How accused product works step-by-step, development timeline and team
- **Design choices**: Alternatives considered, reasons for chosen approach, awareness of patent, design-around efforts
- **Claim element mapping**: Whether product has each claim element, how it performs each function
- **Non-infringement**: Which limitation is missing, how product differs from claims

### Licensing / Damages Witness

- **Licensing history**: Prior licenses (parties, terms, royalty rates), negotiation process, comparable licenses
- **Georgia-Pacific hypothetical negotiation**: Most significant factors, proposed royalty rate and base, non-infringing alternatives and market availability
- **Lost profits (Panduit)**: Manufacturing capacity, market share but-for infringement, patented feature as demand driver, apportionment methodology

### Patent Expert Depositions

Apply @deposition-expert-witness framework, then add:

**Technical expert**: Claim term construction with prosecution history support; element-by-element infringement walkthrough; physical examination and source code review; prior art disclosure analysis; PHOSITA motivation to combine references

**Damages expert**: Royalty rate and methodology; which Georgia-Pacific factors applied and how; comparable license analysis; royalty base; "but for" world for lost profits; apportionment to patented feature

## Trademark Examination Frameworks

### Mark Owner

- Creation timeline, selection rationale, first use in commerce with documentation
- Inherent distinctiveness vs. acquired secondary meaning; supporting advertising
- Awareness of defendant's mark, confusion incidents, harm (lost sales, goodwill, costs)

### Accused Infringer

- Adoption timeline, decision-maker, whether trademark search was conducted
- Awareness of plaintiff's mark, legal advice received
- Intent to trade on goodwill or cause confusion
- Knowledge of actual confusion incidents (misdirected orders, customer inquiries)

## Trade Secret Examination Frameworks

### Owner / Developer

- Specific description of trade secret and what makes it secret
- Security measures: physical (locks, access control), electronic (passwords, encryption), contractual (NDAs, employment agreements, need-to-know)
- Value: development investment, independent replication cost
- Misappropriation theory: how defendant acquired/used it, timeline

### Accused Misappropriator

- Relationship with plaintiff, confidentiality agreements signed
- Access to claimed information, how obtained
- Independent development evidence
- Knowledge that information was confidential
- Disclosure to others, relationship between own product and alleged secret

## Key Documents

| Document | Focus Areas |
|----------|------------|
| Prosecution file | Amendments, arguments, prior art, rejections |
| Invention records / lab notebooks | Conception date, reduction to practice |
| Prior art references | Witness knowledge, differences from claims |
| Licensing agreements | Terms, rates, comparability |
| Design documents | Alternatives considered, patent awareness |
| Technical specs | Element-by-element product function |
| Confidentiality / NDA agreements | Obligation scope, acknowledgment |
| Financial records | Sales, profits, damages support |

## Checklist

- [ ] Review all patents, registrations, or trade secret identification statements
- [ ] Review prosecution history and claim construction positions (patent)
- [ ] Build claim element mapping chart (patent)
- [ ] Analyze all prior art at issue (patent/copyright)
- [ ] Understand accused product/process technical operation
- [ ] Review licensing agreements and identify comparables
- [ ] Prepare likelihood of confusion factor analysis (trademark)
- [ ] Review confidentiality agreements and security measures (trade secret)
- [ ] Review expert reports if available
- [ ] Prepare damages theory framework for case type

## Pitfalls

- **Claim construction first** (patent): Establish witness's understanding of disputed terms before infringement/validity questions — inconsistencies become impeachment material
- **Pin inventors on prior art**: Document what the inventor knew and when; undisclosed known prior art bears on inequitable conduct
- **Prosecution history estoppel**: Explore amendments limiting claim scope under DOE
- **Trade secret specificity**: Use deposition to test whether plaintiff identified trade secrets with reasonable particularity
- **Willfulness**: Establish knowledge of IP rights and steps taken (or not) after learning of them
- **Apportionment**: Required when patented feature is not entire basis for demand — press experts on methodology

## Cross-References

- @deposition-preparation — Primary deposition framework
- @deposition-expert-witness — Expert deposition framework for IP technical and damages experts
- @deposition-30b6-corporate-rep — Corporate representative depositions in IP cases
- @deposition-questioning-techniques — Examination techniques

## Key Authorities

- 35 U.S.C. §§ 101–287 (Patent Act)
- 15 U.S.C. §§ 1051–1141 (Lanham Act)
- 17 U.S.C. §§ 101–810 (Copyright Act)
- 18 U.S.C. §§ 1836–1839 (DTSA)
- *Georgia-Pacific v. U.S. Plywood*, 318 F. Supp. 1116 (S.D.N.Y. 1970) — royalty factors
- *Markman v. Westview Instruments*, 517 U.S. 370 (1996) — claim construction
- State UTSA adoptions vary — confirm applicable state law
