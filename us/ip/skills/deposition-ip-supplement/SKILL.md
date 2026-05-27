---
name: deposition-ip-supplement
title: IP Litigation Deposition Supplement
description: Provides IP-specific deposition examination frameworks for patent, trademark, copyright, and trade secret cases. Covers inventor, infringer, licensing, and expert witnesses with question maps for claim construction, prior art, willfulness, Georgia-Pacific factors, likelihood of confusion, and trade secret identification. Use when preparing IP litigation depositions alongside @deposition-preparation and @deposition-expert-witness.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-ip-supplement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# IP Litigation Deposition Supplement

IP-specific examination strategies for patent, trademark, copyright, and trade secret depositions. Supplements `@deposition-preparation` as the primary framework.

## Quick Start

1. Activate `@deposition-preparation` as primary framework
2. Gather: IP registrations, prosecution history, claim construction order, licensing history, expert reports
3. Identify case type below and select relevant witness frameworks
4. For expert depositions, also apply `@deposition-expert-witness`

## Case Types

| Type | Key Issues | Key Witnesses |
|------|-----------|---------------|
| **Patent** | Claim construction, infringement (literal/DOE), validity, willfulness, damages | Inventors, R&D/engineering, licensing, technical/damages experts |
| **Trademark** | Distinctiveness, priority, likelihood of confusion, willfulness, damages | Mark owner, marketing, survey experts, damages expert |
| **Copyright** | Ownership, originality, access, substantial similarity, fair use, damages | Authors, access witnesses, similarity/damages experts |
| **Trade Secret** | Existence, reasonable secrecy measures, misappropriation, damages | Secret owners, accused misappropriators, security, damages expert |

## Examination Frameworks

### Patent — Inventor

| Topic | Key Questions |
|-------|--------------|
| Conception | First conception date; problem solved; contemporaneous records; who was told |
| Reduction to practice | Date; testing/prototyping; corroborating documentation |
| Prior art knowledge | Known prior art; searches conducted; how invention differs from [specific ref] |
| Claims | Understanding of claim scope; meaning of [disputed term]; relationship to accused product |
| Prosecution | Involvement; review of office actions; reasons for amendments |

### Patent — Accused Infringer Technical Witness

| Topic | Key Questions |
|-------|--------------|
| Product/process | How [accused product] works; key components; development timeline |
| Design process | Alternatives considered; why this approach; patent awareness; design-around efforts |
| Claim mapping | Presence of [claim element]; how product performs [claim function] |
| Non-infringement | Which limitation not met; how product differs from claims |
| Prior art | Prior products/publications before patent priority date |

### Patent — Licensing/Damages Witness

| Topic | Key Questions |
|-------|--------------|
| Licensing history | Existing licenses; royalty rates; negotiation process; comparables |
| Commercial success | Sales figures; success attributable to patented feature |
| Market | Competitors; non-infringing alternatives; market share impact |
| Hypothetical negotiation | Pre-infringement terms; Georgia-Pacific factors; royalty rate and base |

### Patent — Technical Expert

Apply `@deposition-expert-witness` plus:

- **Claim construction**: Basis for construing [disputed term]; prosecution history; specification support
- **Infringement**: Element-by-element walkthrough; physical exam of accused product; source code review (software)
- **Validity**: Prior art considered; whether [reference] discloses [element]; PHOSITA motivation to combine

### Patent — Damages Expert

| Topic | Key Questions |
|-------|--------------|
| Reasonable royalty | Methodology; Georgia-Pacific factors applied; comparable licenses; royalty base |
| Lost profits | "But for" world; manufacturing capacity; non-infringing alternatives; market share methodology |
| Apportionment | Method for isolating patented feature value; consumer demand driver analysis |

### Trademark — Mark Owner

| Topic | Key Questions |
|-------|--------------|
| Creation/adoption | When/who created; why chosen; first use in commerce |
| Distinctiveness | Inherent or acquired secondary meaning; consumer recognition; advertising investment |
| Confusion | Awareness of defendant's mark; actual confusion incidents; similarity; relatedness of goods |
| Damages | Lost sales; goodwill damage; costs addressing confusion |

### Trademark — Accused Infringer

| Topic | Key Questions |
|-------|--------------|
| Adoption | When/who decided to use mark; prior search; awareness of plaintiff's mark |
| Intent | Intent to trade on goodwill; legal advice; good/bad faith indicators |
| Confusion | Known confusion incidents; misdirected customers/orders |
| Market | How customers find and distinguish products |

### Trade Secret — Owner

| Topic | Key Questions |
|-------|--------------|
| Identification | Specific description; what makes it secret; development date and team |
| Secrecy measures | Physical/electronic security; NDAs; need-to-know restrictions; training |
| Value | Development investment; competitive advantage; cost of independent development |
| Misappropriation | How defendant acquired secret; evidence; timing |

### Trade Secret — Accused Misappropriator

| Topic | Key Questions |
|-------|--------------|
| Relationship | Nature of relationship; access; agreements signed; understood obligations |
| Accused information | Awareness of trade secret; how obtained; independent development evidence |
| Use/disclosure | Use of information; third-party disclosure; relation to accused product |
| Notice | Knowledge of confidentiality; steps taken regarding obligations |

## Document Focus Areas

| Document | Topics |
|----------|--------|
| Prosecution file | Amendments, arguments, prior art, rejections |
| Invention records | Lab notebooks, conception/RTP dates, corroboration |
| Licensing agreements | Terms, comparability, negotiation history |
| Design/technical docs | Development process, alternatives, product operation |
| Marketing materials | Features emphasized, performance claims |
| Confidentiality agreements | Scope, obligations, signatories |
| Source code | Software patents, trade secret cases |
| Financial records | Damages calculation support |

## Preparation Checklist

- [ ] Review patents/registrations/trade secret identification
- [ ] Review prosecution history and file wrapper (patent)
- [ ] Map disputed claim terms and proposed constructions (patent)
- [ ] Prepare claim element mapping chart (patent)
- [ ] Identify prior art references and gaps (patent/copyright)
- [ ] Understand accused product/process technical operation
- [ ] Review licensing agreements and comparables
- [ ] Prepare likelihood of confusion analysis (trademark — DuPont)
- [ ] Review confidentiality agreements and secrecy measures (trade secret)
- [ ] Understand damages theory and expert methodology
- [ ] Review expert reports — apply `@deposition-expert-witness`

## Pitfalls

- Pin claim constructions before deposing technical witnesses — questions must track operative constructions
- Lock inventors to specific conception/RTP dates with corroborating documents
- Force precise trade secret identification before substantive questions — vague descriptions create indefiniteness defenses
- Prosecution history estoppel: lock infringers into positions foreclosing DOE arguments
- Cover all 15 Georgia-Pacific factors with damages witnesses; gaps invite Daubert challenge
- Willfulness (§ 284): pre-suit patent knowledge required — establish/negate knowledge timeline
- DTSA vs. state UTSA: confirm governing law; definitions and preemption scope vary
- Copyright fair use: explore each of four factors independently with relevant witnesses

## References

- 35 U.S.C. §§ 101–287 (Patent Act)
- 15 U.S.C. §§ 1051–1141 (Lanham Act)
- 17 U.S.C. §§ 101–810 (Copyright Act)
- 18 U.S.C. §§ 1836–1839 (DTSA)
- *Georgia-Pacific v. U.S. Plywood*, 318 F. Supp. 1116 (S.D.N.Y. 1970)
- *Markman v. Westview Instruments*, 517 U.S. 370 (1996)
- *Halo Electronics v. Pulse Electronics*, 579 U.S. 93 (2016)
