---
name: conversation-intake-trademark-filing-sboghossian
title: Intake — Trademark Filing
description: Use when a user wants to file a trademark application and Claude must gather the mark description, owner, Nice classification, filing jurisdictions, and clearance status before generating a filing strategy and cost estimate. Triggers on requests to register a brand, logo, name, or trademark nationally or internationally. Covers MENA national filing (UAE, KSA, LB, EG) and Madrid Protocol international designations, with specific handling for Arabic-script marks and GCC-block filings.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-intake-trademark-filing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Intake — Trademark Filing

## When this applies

Activate when a user wants to register a trademark, service mark, brand name, logo, or other distinctive sign in one or more jurisdictions. This skill gathers the ten inputs needed to produce a filing strategy, jurisdiction-coverage plan, and cost estimate before routing to the drafting and filing workflow. A clearance search recommendation is always part of the output — filing without clearing is a waste of filing fees.

## Behavior

Multi-turn intake (two turns for multi-jurisdiction strategies; one turn for single-country word-mark filings). Extract any information already given. Always recommend a clearance search if one has not been done — do not route to filing without flagging clearance risk.

## Required fields

### 1. Mark description

What is being registered?

| Mark type | Description needed | Notes |
|---|---|---|
| Word mark | The word(s) in plain text | Broadest protection; covers all fonts and colors |
| Figurative (logo) | Visual description + high-quality reproduction (JPEG/PNG, 900×900px minimum) | Protect the visual design as filed |
| Combined (word + logo) | Both elements | Narrower than separate registrations; sometimes better to file both |
| Sound mark | Audio file + graphic notation (sonogram) | Accepted in UAE, EU, US; less commonly in KSA/LB |
| 3D / shape mark | 3D rendering + description | Higher distinctiveness threshold; must be non-functional |
| Color mark | Pantone reference + specimen of use | Requires extensive evidence of distinctiveness through use |
| Arabic-script mark | Arabic text + transliteration + English translation | Critical for MENA filings — see jurisdictional notes |

### 2. Owner

- Full legal name of the trademark owner (not the representative or applicant's lawyer — the registration must be in the name of the legal owner of the brand).
- Entity type: individual, company, trust, government entity.
- Nationality and jurisdiction of incorporation / residence.
- Note: some MENA jurisdictions (KSA) require foreign applicants to designate a local agent; GCC nationals may have reciprocal simplified treatment.

### 3. Goods and services — Nice Classification

The International Classification of Goods and Services (Nice Classification, currently 12th edition) organizes all goods and services into 45 classes (1–34: goods; 35–45: services). The filing fee is per class in almost every jurisdiction.

Confirm:
- What goods / services does the brand cover?
- In which Nice class(es)?

Guidance (common classes for startups / MENA-focused businesses):
- Class 9: software, mobile apps, AI products, electronic goods
- Class 35: business services, marketing, retail store services
- Class 36: financial services, insurance, real estate, fintech
- Class 38: telecommunications, internet platforms, messaging
- Class 41: education, training, entertainment, publishing
- Class 42: SaaS, software development, tech consulting, legal tech
- Class 45: legal services, personal/social services, security

If the user is unsure of the classes, provide a class recommendation based on the business description. Filing in too narrow a class set leaves the brand exposed; filing in unnecessary classes wastes fees.

### 4. Countries and filing route

Confirm the target jurisdiction list:

**National filings** (each country filed separately):
- UAE: Ministry of Economy Trademark Office (online via moe.gov.ae); trademark register maintained by MoE; renewal every 10 years.
- KSA: Saudi Authority for Intellectual Property (SAIP); online portal; 10-year registration; Arabic and/or English.
- Lebanon: Ministry of Economy and Trade — Trademark and Industrial Designs Directorate; French / Arabic; 15-year registration renewable.
- Egypt: Egyptian Intellectual Property Office (EIPO) under ITIDA; Arabic primary; 10-year registration; renewal for similar periods.
- EUIPO (EU): single application covers all 27 EU member states; 10-year registration; powerful opposition system.
- UKIPO: post-Brexit UK-only registration; 10-year; examined on absolute and relative grounds.
- USPTO: US federal registration; Statement of Use or intent-to-use basis; 10-year renewal (with 5/6-year Section 8 declaration).

**Madrid Protocol (WIPO — international route)**:
- Single international application via WIPO's Madrid System designates multiple member countries.
- Based on a home-country basic application or registration.
- Cost-effective for 5+ country portfolios; standard 18-month examination period per designated country.
- Key MENA member countries: UAE (member), KSA (member), EG (member), LB (not a member as at 2025 — verify; direct national filing required).
- Weakness: a successful central attack on the basic application in the first 5 years cancels all international designations ("central attack risk").

**GCC Gulf Cooperation Council trademark**:
- GCC Trademark Law (Unified Trademark Law) provides for a single GCC-wide registration covering all 6 GCC member states (UAE, KSA, Bahrain, Kuwait, Oman, Qatar).
- Filed through any GCC member state's trademark office; administered by GCC General Secretariat.
- Highly cost-effective for brands operating across the GCC.
- Note: examine current status of GCC trademark system operability — implementation has been uneven; verify whether the GCC joint registration system is fully operational for the target offices.

### 5. Prior use

- Date of first use in commerce (or first use in commerce in each target country, if used in multiple markets).
- Evidence of use: sales receipts, website screenshots, social media with timestamps, packaging, advertising materials.
- Prior use affects:
  - **US**: use-in-commerce basis (Section 1(a)) vs intent-to-use basis (Section 1(b)); use-based filings are stronger.
  - **UK / EU**: use-based rights (passing-off / prior use defense) can be raised against a later registered mark.
  - **LB, KSA, UAE**: first-to-file systems — use alone does not create trademark rights; registration is essential. Prior use may help in opposition proceedings but does not substitute for registration.

### 6. Existing registrations

List any trademark registrations already held:
- Country, registration number, class(es), registration date, expiry date.
- Are any registrations at risk of cancellation for non-use? (Most jurisdictions require 3–5 years of use to avoid cancellation; UAE: non-use for 5 consecutive years grounds for cancellation.)
- Any pending applications or oppositions?

### 7. Clearance search

Has a clearance / availability search been done?

- If **yes**: what was found? Were any confusingly similar marks identified? Was an FTO (freedom to operate) opinion obtained?
- If **no**: strongly recommend conducting one before filing. Filing without clearing risks:
  - Opposition by an earlier right-holder.
  - Infringement claims after commercial launch (potentially more expensive than the search would have cost).
- Claude can route to [[tool-wipo-trademark-search]] and [[tool-local-trademark-registers]] for preliminary screening, but recommend engaging a local trademark attorney for a formal clearance opinion in each target jurisdiction.

### 8. Arabic-script handling for MENA filings

For any mark to be used in MENA markets:
- If the brand is an English or foreign-language word mark, confirm whether an Arabic transliteration or translation will be filed alongside it.
- Arabic and English versions of a mark should ideally be registered separately AND as a combined mark.
- KSA: Arabic-language description of the mark is required in the application form; Arabic word marks must be phonetically clear.
- UAE: bilingual filings (Arabic + English) are common and advisable for broader protection.
- LB: French and Arabic both accepted; French widely used in commercial filings.
- Note: phonetic similarity in Arabic can be different from visual similarity — a mark that is visually distinct in Latin script may be phonetically confusingly similar to an existing Arabic mark.

### 9. Color claim

- Is the mark being filed in color or in black and white?
- **Black-and-white (grayscale) filing**: provides broader protection — the registration covers the mark in any color combination.
- **Color filing**: protects only the specific color(s) filed; allows competitors to use the same design in different colors.
- Best practice for logos: file in black and white for broadest protection; consider filing a color version as a secondary registration if brand identity is strongly color-dependent.
- Pantone / RAL codes should be specified if a color claim is made.

### 10. Description of mark

A brief, precise description of the mark as it will appear in the application:
- For word marks: "The word ACME in standard characters."
- For figurative / logo marks: "A stylized eagle in profile, with wings spread, colored blue and white, with the word ACME beneath in sans-serif font."
- Clear descriptions avoid office actions and accelerate examination.

## Output

At the end of intake, produce:

1. A structured intake summary confirming all ten fields.
2. A filing strategy recommendation: national vs Madrid Protocol vs GCC trademark — with one-paragraph rationale comparing cost, timeline, and coverage.
3. A clearance search recommendation: confirm whether a search has been done; if not, recommend scope of search (identical and phonetically similar marks; same and adjacent classes).
4. A cost estimate framework (per-class, per-jurisdiction official fees; note that professional fees vary by agent).
5. A routing instruction to [[research-precedent-finder]] for clearance context and to the filing workflow.

## Jurisdictional notes

| Jurisdiction | Filing timeline | Examination basis | Opposition period |
|---|---|---|---|
| UAE (MoE) | 18–24 months to registration | Absolute + relative grounds | 30 days from gazette publication |
| KSA (SAIP) | 12–18 months | Absolute + relative grounds | 60 days from publication |
| Lebanon (MoET) | 2–4 years (historically slow) | Absolute grounds primarily | 60 days from gazette publication |
| Egypt (EIPO) | 18–36 months | Absolute + relative grounds | 60 days from acceptance |
| EUIPO (EU) | 5–7 months if no opposition | Absolute grounds (examiner); relative grounds (opposition) | 3 months from gazette publication |
| WIPO Madrid | 18 months per designated country | National examination by designated office | Per national rules |
| USPTO | 12–18 months | Absolute + relative grounds | 30 days from approval for publication |

## Do not

- Route to filing before recommending a clearance search — the cost of a search is trivial compared to the cost of an infringement dispute.
- File only in English-script for brands that will primarily trade in Arabic-speaking MENA markets — brand protection requires Arabic-language coverage.
- Assume Madrid Protocol coverage is available for Lebanon until current membership status is confirmed.
- Recommend a single class filing without reviewing the full scope of the user's commercial activities — under-filing in classes is a common and consequential mistake.

## Related skills

- [[research-precedent-finder]]
- [[tool-wipo-trademark-search]]
- [[tool-local-trademark-registers]]
- [[kb-intellectual-property-mena]]
- [[conversation-intake-nda]]
- [[conversation-uncertainty-language]]
