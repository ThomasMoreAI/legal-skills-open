---
name: dvro-petition
title: Domestic Violence Restraining Order Petition
description: Drafts court-ready Domestic Violence Restraining Order petitions compiling chronological abuse incidents into element-driven pleadings supporting ex parte TRO and permanent protective order relief. Covers personal conduct orders, stay-away orders, custody/visitation, move-out orders, property control, and firearms relinquishment. Use when drafting DVRO petitions, protective order requests, ex parte TRO applications, or domestic violence pleadings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/dvro-petition
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
tags: [family-law, litigation, pleading, drafting]
---

# Domestic Violence Restraining Order Petition

Drafts a complete DVRO petition presenting a factual basis for protective relief, supporting both temporary ex parte and permanent orders after noticed hearing.

## Prerequisites

1. **Party identification** — full legal names, DOBs, addresses, contact info for petitioner and respondent; respondent physical description and vehicle info (for service/enforcement)
2. **Relationship documentation** — marriage certificates, cohabitation history, domestic partnership records, children in common (names, DOBs, residence, school/childcare)
3. **Abuse evidence** — incident descriptions with dates/times/locations, threatening communications, photos, police reports, medical records
4. **Witness information** — names, contact info, relationship to parties
5. **Prior legal actions** — existing restraining orders, criminal cases, custody orders
6. **Jurisdiction/venue** — confirm qualifying relationship under applicable DV statute and proper venue

If any prerequisite is missing, pause and ask — do not assume or fill gaps.

## Output Structure

### Step 1: Verify Jurisdiction & Forms

Before drafting, verify from authoritative sources (current statute, court website, state bar resources):

| Element | Verify |
|---|---|
| Qualifying relationship | Meets statutory definition of domestic relationship |
| Required forms | Judicial Council / court-specific form set (e.g., DV-100, DV-109, DV-110, CLETS-001) |
| Confidential filing | Address confidentiality program or sealed filing rules |
| Service requirements | Personal service rules; whether TRO issues before service |
| Firearms provisions | State and federal relinquishment requirements |

**Anti-hallucination rule**: Do not rely on parametric memory for form numbers, statutory citations, or execution rules. Search and cite the current statute with URL. If unable to verify, insert: `[VERIFY: JURISDICTION-SPECIFIC REQUIREMENTS — Confirm form numbers and filing procedures for [STATE/COUNTY] before filing.]`

### Step 2: Caption & Party Information

| Element | Details |
|---|---|
| Court | Full court name, county, branch |
| Case number | If available; leave blank for new filing |
| Petitioner | Name, address (or confidential per local rules), DOB, relationship to respondent |
| Respondent | Name, address, DOB, physical description, vehicle info |
| Children | Names, DOBs, current residence, school/childcare |

**Safety**: Never disclose confidential addresses in publicly accessible portions — file under seal per local rules.

### Step 3: Abuse Narrative (Evidentiary Core)

Present incidents **chronologically** in numbered paragraphs. Each incident must include:

- Date and time
- Specific location (with address)
- Detailed factual description — exact words for verbal threats
- Type of abuse (physical violence, threats, stalking, harassment, property destruction, financial control, child/pet abuse)
- Injuries sustained and medical treatment received
- Witnesses present
- Law enforcement response (report numbers, officer names)
- Documentary evidence (photos, texts, emails, recordings)

Establish **pattern and escalation**. Use direct quotes from threatening communications. State facts without hyperbole — let the conduct speak for itself.

**Anti-hallucination rule**: Every factual assertion must be sourced from case documents. Do not fabricate or embellish incidents, quotes, or details.

### Step 4: Requested Relief

#### Personal Conduct Orders

> Restrained person shall not: harass, intimidate, threaten, assault, batter, stalk, destroy property of, contact (directly or indirectly), or disturb the peace of the protected person(s).

#### Stay-Away Orders

| Location | Default Distance |
|---|---|
| Petitioner's residence | 100 yards |
| Petitioner's workplace | 100 yards |
| Petitioner's vehicle | 100 yards |
| Children's school/childcare | 100 yards |
| Other frequented locations | 100 yards |

Adjust distances based on facts and jurisdiction.

#### Child Custody & Visitation (if applicable)

- Temporary sole legal and physical custody to petitioner
- Visitation: supervised / suspended / other (match to risk level)
- Specify supervisor if supervised visitation requested
- Frame all custody requests under jurisdiction's best-interest standard

#### Residence & Property

- Move-out order (respondent vacate family home)
- Petitioner granted temporary exclusive possession
- Temporary use of shared vehicles and essential property
- Property control order as needed

#### Additional Relief

- Firearms relinquishment/surrender order — federal law (18 U.S.C. § 922(g)(8)) prohibits firearm possession under qualifying protection orders [VERIFY current status]
- Attorney fees and costs
- Any other orders the court deems necessary

### Step 5: Ex Parte TRO Section

To support immediate relief without notice, establish:

1. **Recency** — most recent incident date and proximity to filing
2. **Escalation** — pattern showing increasing severity or frequency
3. **Specific imminent threat** — direct quotes, explicit threats, credible danger
4. **Reasonable fear** — petitioner's subjective fear supported by objective facts
5. **Notice risk** — why advance notice to respondent would endanger petitioner

### Step 6: Declaration & Execution

- Include standard declaration under penalty of perjury per jurisdiction
- Signature block for petitioner (and attorney, if represented)
- Date every signature block

### Attachments Checklist

- [ ] Required court forms (jurisdiction-specific) [VERIFY form numbers]
- [ ] Confidential information form (address, employer, children's schools)
- [ ] Supporting declarations from witnesses
- [ ] Evidence exhibits (photos, communications, medical records, police reports)
- [ ] Proposed temporary orders for judicial signature

## Guidelines

- **Factual precision over emotional language** — courts respond to specificity, not adjectives
- **Number every paragraph** for easy reference at hearing
- **Confidential addresses**: file under seal per local rules; never disclose in the petition body
- **Court forms vary by state** — confirm required form set for filing jurisdiction [VERIFY]
- **Full faith and credit**: DVRO enforceable nationwide under 18 U.S.C. § 2265 [VERIFY]
- **Service**: personal service on respondent typically required; TRO may issue before service
- **Every jurisdiction-specific claim must be verified** against current statute or flagged `[VERIFY]`
- **Mandatory attorney review** before filing — include explicit notation that output is draft work product, not legal advice
