---
name: art-law-summaries
title: Art Law Summaries
description: Generates structured U.S. art law summaries with Bluebook citations, doctrinal analysis, and stakeholder guidance. Use when researching art law precedents, advising on art transactions, preparing for art market litigation, or surveying a doctrine or statute across ownership, provenance, copyright, VARA, NAGPRA, authentication, NFTs, or AI-generated art.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/art-law-summaries
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# Art Law Summaries

Produces structured art law research with case citations, holdings, reasoning, and stakeholder-specific guidance across major art market legal categories.

## Quick Start

Gather before generating:

1. **Topic** — specific area (e.g., VARA, Holocaust restitution, NAGPRA) or "comprehensive overview"
2. **Jurisdiction** — U.S. federal (default), specific circuit/state, or international
3. **Audience** — artist, gallery/dealer, collector, or legal professional
4. **Specific case or question** — optional; narrows to targeted analysis

## Coverage Areas

| Area | Key Authorities | Common Disputes |
|------|----------------|-----------------|
| Ownership & Title | UCC Art. 2; state property law | Stolen art recovery, estate disputes, consignment |
| Provenance & Holocaust Claims | HEAR Act (2016); FSIA | Chain-of-title gaps, good-faith purchaser, SOL revival |
| Copyright & Moral Rights | 17 U.S.C. §§ 101–1332; VARA § 106A | Reproduction, site-specific destruction, waiver scope |
| Cultural Heritage | NAGPRA (25 U.S.C. §§ 3001–3013); UNESCO 1970; UNIDROIT 1995 | Patrimony claims, museum deaccessions, export restrictions |
| Authentication | Common law fraud; UCC § 2-312 | Expert liability, catalogue raisonné disputes, forgery |
| Digital Art & NFTs | No settled federal framework `[VERIFY]` | Ownership vs. license, smart contract enforceability |
| AI-Generated Art | Copyright Office guidance (2023–present) `[VERIFY]` | Authorship threshold, training data infringement |
| AML Compliance | AML Act of 2020 (31 U.S.C. § 5312) | Dealer reporting, beneficial ownership |

## Case Summary Format

Use this template for each landmark case:

```
**[Case Name]**, [Bluebook Citation]
Court: [Jurisdiction / Level] | Year: [YYYY]
Facts: [2–3 sentences]
Issue: [Legal question presented]
Holding: [Court's ruling]
Reasoning: [Key doctrine or test applied]
Takeaway: [Practical implication for stakeholder]
Status: [Good law | Distinguished by X | Overruled by Y]
```

## Stakeholder Guidance

**Artists** — Copyright registration timing; VARA scope (visual art, editions ≤200, written waiver required); destruction claims per *Carter v. Helmsley-Spear* `[VERIFY]`; gallery contract terms (exclusivity, consignment, resale royalties).

**Galleries & Dealers** — Provenance due diligence (Art Loss Register, INTERPOL, Getty Provenance Index); consignment essentials (title retention, insurance, authority-to-sell); buyer disclosure and UCC § 2-312 warranty `[VERIFY]`; AML reporting thresholds.

**Collectors** — Acquisition docs (bill of sale, provenance, export/import certificates); forgery recourse (contractual vs. statutory); estate planning (IRC § 170 appraisal, charitable contributions, fractional interests).

## Emerging Issues

| Issue | Status | Key Authority |
|-------|--------|---------------|
| NFT ownership vs. license | Unsettled | No controlling precedent `[VERIFY]` |
| AI-art copyright | Evolving | Copyright Office guidance; *Thaler* `[VERIFY]` |
| Art market AML reporting | Active | AML Act of 2020; FinCEN rulemaking |
| Climate & cultural heritage | Framework stage | UNESCO 1972 World Heritage Convention |

## Pitfalls & Checks

- **All citations**: Bluebook format; mark unverified ones `[VERIFY]`
- **Circuit splits**: Flag explicitly (e.g., VARA "recognized stature" standard varies) `[VERIFY]`
- **HEAR Act**: Note SOL revival for Holocaust-era claims filed after 2016
- **NAGPRA**: Applies to federally funded institutions only — note private museum carve-outs
- **VARA vs. state**: Distinguish federal VARA from broader state statutes (CA Art Preservation Act, NY Artists' Authorship Rights Act)
- **Repatriation**: UNESCO 1970 = public law framework; UNIDROIT 1995 = private law claims
- **NFT/AI authority**: Rapidly evolving — always flag publication date of cited sources
