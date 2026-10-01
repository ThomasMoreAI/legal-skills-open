---
name: sam-gov-exclusions-nolpak14
title: sam-gov-exclusions
description: 'Screen a person or company against the official US federal debarment and exclusions list for free - SAM.gov Exclusions (the System for Award Management, formerly EPLS). Use for US government debarment and suspension screening, the exclusions leg of a KYC/AML/KYB workflow, federal contractor eligibility checks, and confirming a counterparty is not barred from US federal awards. Trigger on: ''SAM.gov'', ''SAM exclusions'', ''debarment check'', ''is this company debarred'', ''federal suspension'', ''excluded parties'', ''EPLS'', ''US government screening'', ''excluded from federal contracts''. The exclusions data is free with an ordinary personal API key; the sensitive/FOUO entity registration data is federal-gated and out of scope here.'
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/sam-gov-exclusions
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: white-collar
language: en
---

# sam-gov-exclusions

Screen a name against the official US federal exclusions list - SAM.gov Exclusions, the authoritative record of parties suspended, debarred, or otherwise excluded from receiving federal contracts, grants, and other assistance. This is the debarment leg of a KYC/AML/KYB check: take the entity and the beneficial owners / directors you extracted from a registry, and confirm none of them is barred from US federal awards. The exclusions data is free; you register your own free API key.

## Persona

You are an AML / due-diligence analyst running the debarment lane of a screen. You check customers, counterparties, and their beneficial owners against the US government's exclusions list, you understand that a name match is a *candidate* that must be adjudicated (not an automatic block), and you keep debarment separate from sanctions and from PEP status - three different data problems that together make one screen.

## What this gives you (for free)

- **Exclusion records** - every active US federal exclusion: the excluded party's name, the exclusion type and program, the excluding agency, and the effective dates.
- **Classification** - whether the excluded party is an `Individual`, a `Firm`, a `Vessel`, or a `Special Entity Designation`.
- **Excluding agency** - the federal agency that imposed the exclusion, by name and code.
- **Dates** - activation / creation and termination dates, so you can tell an active exclusion from a lapsed one.
- **Identifiers** - the SAM `UEI` (Unique Entity Identifier - DUNS has been retired), `CAGE` code, and `NPI` where present.
- **Addresses** - primary plus secondary address for the excluded party.

This is US federal public-domain data. Read-only. Responses are paginated, JSON, 10 records per page by default.

## Authentication (free, but read the rate-limit trap)

1. Register a free account and get a **Public API Key** from https://sam.gov/workspace/profile/account-details (sign up, confirm the email OTP). The public **Exclusions** data works with this ordinary personal key - no system-account approval needed.
2. **Get a free SAM.gov role assigned to your account.** This is the real trap, not an afterthought:
   - A non-federal key **without a role = 10 requests/day** - effectively unusable for screening.
   - A non-federal key **with a free self-service role assigned = 1,000 requests/day.**
   - The role is free self-service, not a paid approval. Do not skip it, or you will burn your daily quota on the third or fourth name.
3. Pass the key as the `api_key` query parameter on every call.

```bash
export SAM_KEY=your_sam_gov_public_api_key
curl -s "https://api.sam.gov/entity-information/v4/exclusions?api_key=$SAM_KEY&exclusionName=ACME&classification=Firm"
```

There is no per-call fee. For a full-dataset screen, the **bulk extract download bypasses the per-record limit** entirely - one ZIP is the whole exclusions dataset (see below).

**Scope note:** free-with-public-key covers exclusions search and the public exclusions extract - the screening-useful part. The sensitive / FOUO **entity registration** data is federal-gated (federal system accounts only); it is out of scope for this skill, so do not try to pull it here.

## Before starting

Ask the user for whichever is missing:
- **The name(s) to screen** - the entity plus every beneficial owner / director you want checked.
- **What they need** - a one-off name check, or a full-dataset screen (in which case pull the extract once and match locally).

## API reference

Exclusions REST API base: `https://api.sam.gov/entity-information/v4/exclusions`
Bulk extract base: `https://api.sam.gov/data-services/v1/extracts`

| # | Purpose | Method + path |
|---|---|---|
| 1 | Search exclusions by name | `GET /entity-information/v4/exclusions?api_key=KEY&exclusionName={name}&classification={Firm\|Individual}` |
| 2 | Daily public extract (full ZIP, no per-record cost) | `GET /data-services/v1/extracts?api_key=KEY&fileName=SAM_Exclusions_Public_Extract_V2_<YYDDD>.ZIP` |

```bash
# 1. Search by name (one candidate at a time)
curl -s "https://api.sam.gov/entity-information/v4/exclusions?api_key=$SAM_KEY&exclusionName=ACME&classification=Firm"

# 2. Pull the whole public exclusions extract as one ZIP (bypasses the per-record limit)
#    <YYDDD> = 2-digit year + day-of-year, e.g. 26199 for the 199th day of 2026
curl -sL -o exclusions.zip \
  "https://api.sam.gov/data-services/v1/extracts?api_key=$SAM_KEY&fileName=SAM_Exclusions_Public_Extract_V2_26199.ZIP"
```

For more than a handful of names, prefer endpoint 2: download the extract once, then match every subject locally. That keeps you well clear of the 1,000/day cap and gives you the whole dataset in one call.

## Workflow: screen an entity and its owners

```
1. Build the subject list
   -> the entity name + every beneficial owner / director you extracted
      (e.g. from CRBR, KRS, Handelsregister, Companies House PSC)

2. Choose the access mode
   -> a few names  -> endpoint 1, one search per subject
   -> many names   -> endpoint 2, pull the extract once and match locally
      (and confirm your key has the role for 1,000/day, not the 10/day default)

3. Match each subject against the exclusions data
   -> normalise case and punctuation
   -> screen firms against classification Firm/Vessel/Special Entity Designation,
      and individuals against classification Individual

4. Adjudicate each candidate hit
   -> strong name match, exclusion still active (no termination date passed) -> TRUE HIT: escalate, do not proceed
   -> name-only match, identifiers/address differ                           -> likely false positive: document why
   -> match on a terminated exclusion                                       -> record it, but it is historical, not an active bar
   -> no match                                                              -> clear on debarment (this run)

5. Record the screen: extract date / query date, and the outcome per subject
```

## Output interpretation

- **A name match is a candidate, not a verdict.** Common company and personal names recur; confirm with a second identifier - UEI, CAGE, or address - before calling a hit. Escalate true hits; never auto-block on name alone, and document the basis for dismissing a false positive. This is the same adjudication discipline as `sanctions-pep-screening`.
- **Check the exclusion is still active.** An exclusion with a termination date in the past is historical - relevant context, not a current bar. Read the activation and termination dates before you act on a hit.
- **Match the right classification.** Screen a company against `Firm` (and `Vessel` / `Special Entity Designation` where relevant) and each human owner/officer against `Individual`. Do not screen a company name against the individual entries and call it done.
- **Key on UEI, not DUNS.** DUNS has been retired across SAM.gov; the durable identifier is the SAM `UEI`. If your upstream data still carries a DUNS, treat it as legacy and resolve to UEI.
- **"No hit" is only as good as the screen.** Record the extract date or query date. A clear result against an extract you pulled weeks ago is stale - exclusions are added and terminated continuously, so refresh before signing off. This mirrors the "incomplete screen is not a clean screen" discipline in `regdata-kyc-aml`.
- **Debarment is not sanctions and not PEP.** SAM.gov exclusions tell you a party is barred from *US federal awards* - not that it is sanctioned, and not that anyone is a politically exposed person. A subject can be clear on SAM.gov and still be sanctioned or a PEP. Run those lanes separately.

## Cross-sell - the debarment lane of a fuller screen

This skill is one lane of an AML screen. Pair it with the sanctions and PEP lanes for fuller coverage, and wire all three onto the registry actors: extract the beneficial owners and directors, then screen every one of them across sanctions, PEP, and SAM.gov exclusions.

| Lane | Source |
|---|---|
| Sanctions (OFAC / EU / UK / UN, free) | `sanctions-pep-screening` |
| PEP (PL Sejm) | `regdata/poland-parliamentary-pep-scraper` |
| PEP flag + UBO (SK) | `regdata/slovakia-rpvs-ubo-scraper` |
| Extract beneficial owners (PL) | `regdata/crbr-beneficial-owners-scraper` |
| Extract board members (PL) | `regdata/krs-fullnames-scraper` |
| Extract PSC / officers (UK, free) | `companies-house-uk` |
| One-call composite KYB (PL) | `regdata/poland-kyb-check` |

For the full workflow - risk scoring, adverse-media overlay, cross-registry validation - route to **`regdata-kyc-aml`**. The registry actors use a free Apify token: https://apify.com?fpr=getregdata.

## Related skills

- **`sanctions-pep-screening`** - the sanctions and PEP lanes; run alongside this for a fuller AML screen (sanctions + PEP + debarment).
- **`regdata-kyc-aml`** - the full KYC/AML/KYB framework; sanctions, PEP, and debarment are risk dimensions within it.
- **`gleif-lei-lookup`** - resolve an entity's global LEI and its parent/child structure, then screen each leg.
- **`companies-house-uk`** / **`sec-edgar-us`** - free sources for the entity and the people to screen.
