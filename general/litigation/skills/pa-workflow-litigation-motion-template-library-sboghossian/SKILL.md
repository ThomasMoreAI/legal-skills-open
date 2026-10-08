---
name: pa-workflow-litigation-motion-template-library-sboghossian
title: Motion Template Library
description: Use when a litigator needs a structured starting template for a court motion, adapted to the specific court, jurisdiction, and procedural rules. Covers motions to dismiss, summary judgment, compel, in limine, and sanctions, each adapted per jurisdiction (US, UK, DIFC, ADGM, UAE, KSA, LB, EG). Produces jurisdiction-appropriate structure, required legal standards, and a checklist of required components before filing.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-litigation-motion-template-library
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Motion Template Library

## Purpose

This skill surfaces a jurisdiction-appropriate motion template when a litigator needs to draft a formal court motion. Each template includes: the required legal standard for the motion type, the mandatory structural components for the applicable court, placeholder guidance (not `[INSERT X]`-style — rather, annotated instructions at each point), common grounds, and a pre-filing checklist.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Motion type | Yes | See categories below |
| Court / forum | Yes | Determines structural requirements and citation format |
| Jurisdiction | Yes | Determines applicable legal standard |
| Case summary (facts + claims) | Recommended | Allows pre-population of fact section |
| Governing procedural rules | Optional | Auto-supplied per forum; override if local rules apply |

## Motion Types and Standards

### 1. Motion to Dismiss / Strike Out

| Forum | Procedural basis | Standard |
|---|---|---|
| US Federal | FRCP 12(b)(6) | Plausibility — Twombly/Iqbal: facts, if true, must plausibly state a claim for relief |
| UK courts | CPR 3.4 / Part 24 | No real prospect of success; claim is an abuse of process |
| DIFC | DIFC Court Rules Part 12 | Follows English CPR approach |
| ADGM | ADGM Court Procedure Rules | Follows English CPR approach |
| UAE onshore | CPC Art. 115+ | Procedural defect, lack of jurisdiction, or substantive illegality |
| KSA Commercial Courts | Commercial Court Law | Lack of jurisdiction; procedural defect; invalid service |
| Lebanon | LCPC Art. 35+ | Inadmissibility (fin de non-recevoir) or lack of jurisdiction |
| Egypt | Egyptian CPC | Inadmissibility; prescription; lack of capacity |

**Template structure:**
1. Caption (court, parties, case number)
2. Introduction — nature of motion and relief sought
3. Procedural history (brief)
4. Legal standard (state precisely)
5. Argument — matched to each pleaded claim
6. Conclusion and relief requested
7. Certificate of service

### 2. Motion for Summary Judgment / Summary Disposal

| Forum | Standard |
|---|---|
| US Federal (FRCP 56) | No genuine dispute as to any material fact; movant entitled to judgment as a matter of law |
| UK (CPR Part 24) | No real prospect of success on the claim or defence |
| DIFC / ADGM | Follows CPR Part 24 |
| UAE onshore | No direct equivalent; partial parallel in urgent/provisional relief applications |

**Template structure:**
1. Introduction and summary of relief sought
2. Statement of undisputed material facts (numbered; each supported by record citation)
3. Legal standard
4. Argument — applied to each claim/defense
5. Conclusion
6. Supporting declaration(s) (US: FRCP 56(c); UK: statement of truth)
7. Index of exhibits

**Practice note for MENA**: UAE onshore and KSA courts do not have a direct summary judgment mechanism comparable to FRCP 56. The closest equivalent is requesting a case to be decided on the pleadings or through expedited proceedings (talab mustajil). Tailor strategy accordingly.

### 3. Motion to Compel Discovery / Disclosure

| Forum | Basis |
|---|---|
| US Federal | FRCP 37(a) — failure to respond or respond adequately to discovery requests |
| UK (CPR 31.12) | Application for specific disclosure |
| DIFC / ADGM | DIFC Rules Part 29 / ADGM Rules — follows English approach |
| International Arbitration | IBA Rules Art. 3(4) — tribunal ordered production not complied with |

**Template structure:**
1. Introduction — what was requested; what is missing
2. Description of outstanding discovery (itemized)
3. Procedural history of attempts to resolve (required in most jurisdictions before filing)
4. Legal basis for compelled production
5. Specific relief requested (production, sanctions, adverse inference)
6. Proposed order

**Meet-and-confer requirement**: US courts require a good-faith conference before filing (FRCP 37(a)(1)); DIFC rules require a similar correspondence exchange. Document attempts to resolve in a letter exhibit.

### 4. Motion in Limine

Purpose: to exclude or limit specific evidence before trial/hearing.

**Template structure:**
1. Identification of evidence sought to be excluded
2. Procedural basis for exclusion
3. Argument — ground by ground (relevance, prejudice, privilege, hearsay, authentication, expert qualification)
4. Relief sought (exclusion, limitation, redaction)

Common grounds in MENA arbitration:
- Privilege (legal advice, settlement without prejudice communications)
- Proportionality (IBA Rules Art. 9.2)
- Confidentiality (trade secret; regulatory confidentiality)

### 5. Motion for Sanctions / Costs

| Forum | Basis |
|---|---|
| US Federal | FRCP 11 (frivolous filings); 28 U.S.C. § 1927 (vexatious conduct); inherent power |
| UK courts | CPR 44 — unreasonable conduct; wasted costs orders |
| DIFC / ADGM | DIFC / ADGM Rules — indemnity costs for bad-faith conduct |
| International Arbitration | IBA Rules; ICC Rules Art. 38(5) — tribunal may apportion costs for bad-faith conduct |

**Template structure:**
1. Nature of sanctionable conduct
2. Applicable rule or inherent authority
3. Factual record of conduct (exhibit-supported)
4. Relief sought (monetary sanctions, fees, adverse inference)
5. Certification (FRCP 11 safe harbor: must serve motion and allow 21-day cure before filing)

## Filing Checklist (Universal)

Before filing any motion:

- [ ] Correct caption (parties, court, docket number)
- [ ] Statement of the applicable legal standard
- [ ] Each argument tied to a specific rule or precedent
- [ ] All citations verified ([[pa-workflow-litigation-brief-cite-checker]])
- [ ] Word / page limit compliance (check local rules)
- [ ] Certificate of service included
- [ ] Proposed order attached (required in many jurisdictions)
- [ ] Meet-and-confer requirement satisfied (where applicable)
- [ ] Arabic translation required (UAE / KSA onshore submissions)
- [ ] Notarization / authentication of foreign documents (where required)

## Jurisdictional Filing Notes

- **UAE onshore**: Submissions are in Arabic. Foreign-language documents must be accompanied by a certified Arabic translation. The court may require originals or notarized copies.
- **KSA**: Commercial court filings require Arabic. Saudi lawyers must file on behalf of parties; foreign counsel appear as legal consultants. Courts use the Unified Portal (Najiz) for electronic filings.
- **Lebanon**: Filings are in Arabic or French. Case files are maintained manually; electronic filing is limited. Check specific court practice for form and timing requirements.
- **DIFC**: English-language proceedings. Electronic filing via the DIFC Court e-filing portal. OSCOLA citation format standard.
- **ADGM**: English-language proceedings. Court uses a similar electronic filing system.

## Related Skills

- [[pa-workflow-litigation-brief-cite-checker]]
- [[pa-workflow-litigation-case-theory-simulator]]
- [[pa-workflow-litigation-privilege-log-drafting]]
- [[pa-workflow-litigation-discovery-first-pass-tagging]]
