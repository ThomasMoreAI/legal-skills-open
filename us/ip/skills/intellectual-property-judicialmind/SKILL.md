---
name: intellectual-property-judicialmind
title: Intellectual Property
description: Intellectual property law skill covering patents, trademarks, copyrights, and trade secrets. Use when the user needs assistance with IP protection, patent drafting, trademark registration, copyright matters, licensing, or IP disputes. Triggers on keywords like "patent", "trademark", "copyright", "trade secret", "IP", "intellectual property", "infringement", "prior art", "licensing", "USPTO".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/intellectual-property
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
sources:
- title: Licensing Templates
  path: references/licensing-templates.md
- title: Patent Prosecution
  path: references/patent-prosecution.md
- title: Trademark Clearance
  path: references/trademark-clearance.md
---

# Intellectual Property

This skill provides expert guidance for protecting and enforcing intellectual property rights.

## Core Capabilities

### 1. Patents
- Patentability analysis
- Patent drafting and prosecution
- Prior art searches
- Patent portfolio management

### 2. Trademarks
- Trademark searches and clearance
- Registration and prosecution
- Portfolio management
- Enforcement and opposition

### 3. Copyrights
- Copyright registration
- Infringement analysis
- Fair use assessment
- Licensing

### 4. Trade Secrets
- Protection programs
- NDA drafting
- Misappropriation claims
- Employee mobility issues

## Patent Practice

### Patentability Requirements (35 U.S.C.)
| Requirement | Standard | Key Cases |
|-------------|----------|-----------|
| Subject Matter (§101) | Process, machine, manufacture, composition | Alice, Mayo, Bilski |
| Novelty (§102) | Not anticipated by prior art | |
| Non-obviousness (§103) | Not obvious to PHOSITA | KSR, Graham v. John Deere |
| Written Description (§112) | Describe invention adequately | |
| Enablement (§112) | Enable one skilled to make/use | |

### Patent Types
| Type | Term | Coverage |
|------|------|----------|
| Utility | 20 years from filing | Function, use, structure |
| Design | 15 years from grant | Ornamental appearance |
| Plant | 20 years from filing | New plant varieties |

### Patent Application Components
```
1. Specification
   - Title
   - Cross-references
   - Background
   - Summary
   - Brief description of drawings
   - Detailed description

2. Claims
   - Independent claims (broad)
   - Dependent claims (narrow)

3. Abstract

4. Drawings (if needed)

5. Formal papers
   - Declaration/oath
   - Power of attorney
   - Assignment
```

### Prosecution Timeline
```
Filing → Publication (18 mo) → Office Action → Response →
Allowance/Final Rejection → Appeal/RCE → Grant
```

## Trademark Practice

### Registration Requirements
- Use in commerce (or bona fide intent)
- Distinctive mark
- Not confusingly similar to existing marks
- Not merely descriptive or generic

### Strength Spectrum
```
STRONGEST ←────────────────────────────────→ WEAKEST

Fanciful → Arbitrary → Suggestive → Descriptive → Generic
(Kodak)    (Apple)     (Coppertone)  (Sharp TV)    (Escalator)
```

### Likelihood of Confusion Factors (DuPont Factors)
1. Similarity of marks
2. Similarity of goods/services
3. Channels of trade
4. Conditions of sale
5. Fame of prior mark
6. Number of similar marks
7. Nature and extent of actual confusion
8. Length of concurrent use
9. Variety of goods
10. Market interface
11. Applicant's right to exclude
12. Extent of potential confusion
13. Other established facts

### Registration Process
```
1. Clearance Search
2. Application Filing (TEAS)
3. Examination (~3-4 months)
4. Publication (30 days)
5. Opposition Period
6. Registration (or Notice of Allowance for ITU)
7. Statement of Use (if ITU)
8. Maintenance (Sections 8, 9, 15)
```

### Maintenance Requirements
| Filing | Deadline | Purpose |
|--------|----------|---------|
| Section 8 | 5-6 years | Continued use declaration |
| Section 15 | 5-6 years | Incontestability |
| Section 8 & 9 | Every 10 years | Renewal |

## Copyright Practice

### Protectable Works (17 U.S.C. § 102)
- Literary works
- Musical works
- Dramatic works
- Choreographic works
- Pictorial, graphic, sculptural works
- Motion pictures and audiovisual works
- Sound recordings
- Architectural works

### Not Protectable
- Ideas, procedures, processes
- Facts
- Titles, names, short phrases
- Works in public domain
- Government works

### Copyright Duration
| Work Type | Duration |
|-----------|----------|
| Individual author | Life + 70 years |
| Joint work | Life of last surviving author + 70 years |
| Work for hire | 95 years from publication or 120 from creation |
| Anonymous/pseudonymous | Same as work for hire |

### Fair Use Analysis (§ 107)
1. **Purpose and character** of use (commercial vs. educational, transformative)
2. **Nature** of copyrighted work (creative vs. factual)
3. **Amount and substantiality** of portion used
4. **Effect on market** for original work

### Registration Benefits
- Prerequisite to suit (for US works)
- Statutory damages ($750-$30,000; up to $150,000 if willful)
- Attorney's fees
- Prima facie evidence of validity

## Trade Secret Practice

### Elements (DTSA / UTSA)
1. Information
2. Derives value from secrecy
3. Reasonable efforts to maintain secrecy

### Protection Measures
- [ ] Confidentiality agreements
- [ ] Employee training
- [ ] Physical security
- [ ] Digital security (access controls, encryption)
- [ ] Need-to-know access
- [ ] Exit interviews
- [ ] Marking confidential documents
- [ ] Visitor protocols

### Misappropriation Claims
**Acquisition**: Improper means (theft, bribery, breach of duty)
**Disclosure/Use**: Without consent, when should know improper

### Remedies
- Injunctive relief
- Damages (actual loss + unjust enrichment)
- Exemplary damages (2x for willful)
- Attorney's fees (bad faith or willful)

## IP Licensing

### Key License Terms
| Term | Description |
|------|-------------|
| Grant clause | Scope of rights licensed |
| Field of use | Permitted applications |
| Territory | Geographic scope |
| Exclusivity | Exclusive, sole, or non-exclusive |
| Sublicense rights | Ability to sublicense |
| Term | Duration of license |
| Royalties | Payment structure |
| Audit rights | Verify royalty payments |
| Improvements | Rights to enhancements |
| Representations | IP ownership, non-infringement |
| Indemnification | IP infringement claims |

### Royalty Structures
- Running royalty (% of sales)
- Flat fee (lump sum)
- Minimum guarantees
- Milestone payments
- Hybrid structures

## IP Disputes

### Patent Infringement Analysis
1. Claim construction
2. Literal infringement
3. Doctrine of equivalents
4. Defenses (invalidity, exhaustion, implied license)

### Trademark Infringement
- Likelihood of confusion
- Dilution (famous marks)
- Cybersquatting (ACPA, UDRP)

### Copyright Infringement
1. Ownership of valid copyright
2. Copying (access + substantial similarity)
3. Defenses (fair use, license, independent creation)

## Key Databases and Resources

| Resource | Purpose | URL |
|----------|---------|-----|
| USPTO | Patent/trademark search | uspto.gov |
| WIPO | International filings | wipo.int |
| Google Patents | Patent search | patents.google.com |
| EPO Espacenet | European patents | espacenet.com |
| TESS | Trademark search | tmsearch.uspto.gov |
| Copyright Office | Registration | copyright.gov |

## Integration with Other Skills

- **legal-research**: Case law and precedent
- **contract-lifecycle**: IP licensing agreements
- **corporate-ma**: IP due diligence
- **litigation**: IP enforcement
- **international-arbitration**: Cross-border IP disputes

## Reference Files

For detailed guidance:
- `references/patent-prosecution.md` - Patent application guide
- `references/trademark-clearance.md` - TM search methodology
- `references/licensing-templates.md` - License agreement forms
