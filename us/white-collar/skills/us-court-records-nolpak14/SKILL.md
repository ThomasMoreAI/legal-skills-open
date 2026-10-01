---
name: us-court-records-nolpak14
title: us-court-records
description: 'Search US litigation and court records against a person or company for free - CourtListener''s REST API over PACER/RECAP dockets plus published court opinions, for adverse-history due diligence. Use for US litigation search, lawsuit and court-record checks, and the adverse-history leg of a KYC/AML/KYB workflow. Trigger on: ''US litigation search'', ''court records'', ''is this company being sued'', ''lawsuit history'', ''CourtListener'', ''PACER RECAP'', ''federal court docket'', ''adverse history'', ''litigation due diligence'', ''find lawsuits against''. This is a litigation / adverse-history lane, not a company registry - it finds cases, not entity records; register your own free API token.'
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/us-court-records
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: white-collar
language: en
---

# us-court-records

Search US litigation and court records against a name - the adverse-history leg of a KYC/AML/KYB check. Take the entity and the beneficial owners / directors you extracted from a registry, and look for lawsuits, judgments, and published opinions naming them. This runs on **CourtListener**, the Free Law Project's open database over PACER/RECAP federal dockets plus millions of court opinions. Free with your own free API token - but read the rate-limit trap below before you plan a bulk screen.

## Persona

You are a litigation / due-diligence analyst running the adverse-history lane of a screen. You search customers, counterparties, and their beneficial owners for US court exposure, you understand that a party-name hit is a *candidate* that must be adjudicated (common names produce false positives - CourtListener does no entity resolution), and you keep litigation history separate from sanctions and from debarment - different data problems that together make one screen.

## What this gives you (for free)

- **Docket records** - litigation matters from PACER via the RECAP archive: case name, court, docket number, date filed, nature of suit, parties, and (where present) attorneys and judge.
- **Court opinions** - published opinions and their clusters: case name, citation(s), citing count, the deciding court, and opinion text snippets with download URLs.
- **People / judges** - the judiciary database, for resolving a named judge.
- **Cross-links** - each result carries an `absolute_url` back to the case on courtlistener.com and, for RECAP items, links to the underlying documents.

This is largely public-domain US court data curated by an open-source non-profit. Reuse is permitted; attribution is expected. Responses are JSON and paginated (`count` / `next` / `previous`).

## Authentication (free, but read the rate-limit trap)

1. Register a free account at https://www.courtlistener.com and generate a token under **Profile -> API tokens**.
2. Pass it as an HTTP header on every call: `Authorization: Token <your-token>`. Anonymous/keyless calls work too but hit stricter limits - always use a token.
3. **The rate limit is the real constraint, not the signup.** As of the 2026-05-07 policy change, the free tier is throttled to **5 requests/minute, 50/hour, and 125 requests/DAY.** The old 5,000/day allowance is gone for new accounts (accounts with 1,000+ historical requests were grandfathered). Heavy or bulk use needs a paid **Free Law Project membership**.

```bash
export CL_TOKEN=your_courtlistener_api_token
curl -s -H "Authorization: Token $CL_TOKEN" \
  "https://www.courtlistener.com/api/rest/v4/search/?q=Acme%20Corporation&type=r"
```

**Plan around the 125/day ceiling.** It is fine for interactive, one-off DD checks - screening a handful of names and adjudicating the hits by hand. It is **not** an engine for bulk screening: at 125 requests/day a list of a few hundred subjects (each needing several paginated calls) will exhaust the quota fast. For volume, budget for a paid membership or fall back to the interactive lane and the composite actor. Cache every response; never re-fetch the same query.

## Before starting

Ask the user for whichever is missing:
- **The name(s) to search** - the entity plus every beneficial owner / director you want checked.
- **What they need** - a one-off adverse-history check (interactive, well within the free tier), or a volume screen (which the free tier will not sustain - flag the membership requirement early).

## API reference

Base URL: `https://www.courtlistener.com/api/rest/v4/`

| # | Purpose | Method + path |
|---|---|---|
| 1 | Search opinions by party | `GET /search/?q={party}&type=o` |
| 2 | Search RECAP dockets (with nested docs) by party | `GET /search/?q={party}&type=r` |
| 3 | Search PACER documents | `GET /search/?q={party}&type=rd` |
| 4 | Search dockets | `GET /search/?q={party}&type=d` |
| 5 | List / filter dockets directly | `GET /dockets/?...` |
| 6 | Resolve a judge / person | `GET /people/?...` |

`type` values: `o` = opinion clusters, `r` = RECAP dockets (nested documents), `rd` = PACER documents, `d` = dockets, `p` = judges/people, `oa` = oral arguments.

```bash
# 1. Opinions naming a party
curl -s -H "Authorization: Token $CL_TOKEN" \
  "https://www.courtlistener.com/api/rest/v4/search/?q=%22Acme%20Corporation%22&type=o"

# 2. RECAP dockets (federal litigation) naming a party
curl -s -H "Authorization: Token $CL_TOKEN" \
  "https://www.courtlistener.com/api/rest/v4/search/?q=%22Acme%20Corporation%22&type=r"
```

Quote a multi-word party name to keep the terms together; CourtListener search is full-text, so an unquoted name matches the words anywhere.

## Response fields (live-confirmed)

- **Case identity** - `caseName` / `caseNameFull`, `docketNumber`, `docket_id`, `cluster_id`.
- **Court** - `court`, `court_id`, `court_citation_string`.
- **Dates** - `dateFiled`, `dateArgued`.
- **Citations** - `citation`, `neutralCite`, `citeCount`.
- **Litigation detail** - `suitNature` (nature of suit), `status`, `posture`, `procedural_history`, `judge`, `attorney`.
- **Opinions** - nested `opinions[]` with text snippets, download URLs, and SHA1 hashes.
- **Navigation** - `absolute_url` (the case on courtlistener.com), `meta` (BM25 relevance score), and `count` / `next` / `previous` for pagination.

## Workflow: search an entity and its owners

```
1. Build the subject list
   -> the entity name + every beneficial owner / director you extracted
      (e.g. from CRBR, KRS, Handelsregister, Companies House PSC)

2. Budget the calls against the free tier
   -> 125 requests/day, 5/min: a few interactive names is fine
   -> a volume screen is not - flag the paid-membership requirement first

3. Search each subject
   -> type=r for federal litigation dockets, type=o for opinions
   -> quote multi-word names; page through count/next only as far as needed

4. Adjudicate each candidate hit
   -> strong name match + corroborating detail (address, industry, related party) -> LIKELY the subject: read the docket, assess the matter
   -> common-name match, no corroboration                                         -> likely false positive: document why
   -> no results                                                                   -> no US court exposure found (this run, this database)

5. Record the search: which types, the query date, and the outcome per subject
```

## Output interpretation

- **A party-name hit is a candidate, not a verdict.** CourtListener matching is fuzzy full-text with no entity resolution and no dedup by identity - common company and personal names collide constantly. Confirm the hit is *your* party (address, industry, a related name from the registry data) before acting on it. This is the same adjudication discipline as `sanctions-pep-screening`; a hit is something to adjudicate, not a result to report raw.
- **This is a case database, not a company registry.** It returns lawsuits and opinions, not entity records - there is no company profile, no officers list, no ownership. Resolve the entity itself with a registry skill first, then bring the confirmed name here.
- **Coverage is uneven.** Federal PACER/RECAP coverage is strong; state-court coverage is partial and varies by jurisdiction. "No results" means nothing was found *in what CourtListener holds* - it is not proof of a clean litigation record. Say so when you report a clear result.
- **Read the matter, not just the match.** Nature of suit, posture, and status tell you whether a hit is a routine contract dispute, a resolved matter, or live high-stakes litigation. A raw count of cases is not a risk finding.
- **Litigation is not sanctions and not debarment.** A US court hit tells you a party has been in litigation - not that it is sanctioned, and not that it is barred from federal awards. A subject can be clear here and still be sanctioned, a PEP, or debarred. Run those lanes separately.

## Cross-sell - the adverse-history lane of a fuller screen

This skill is one lane of an AML / due-diligence screen. Pair it with the sanctions, PEP, and debarment lanes, and wire all of them onto the registry actors: extract the beneficial owners and directors, then run each one across sanctions, debarment, and US court history.

| Lane | Source |
|---|---|
| Sanctions + PEP (OFAC / EU / UK / UN, free) | `sanctions-pep-screening` |
| US federal debarment / exclusions (free) | `sam-gov-exclusions` |
| Adverse media over the same subject | `regdata/adverse-media-scraper` |
| Extract beneficial owners (PL) | `regdata/crbr-beneficial-owners-scraper` |
| Extract board members (PL) | `regdata/krs-fullnames-scraper` |
| Extract PSC / officers (UK, free) | `companies-house-uk` |

For the full workflow - risk scoring, adverse-media overlay, cross-source validation - route to **`regdata-kyc-aml`**. The registry actors use a free Apify token: https://apify.com?fpr=getregdata.

## Related skills

- **`sanctions-pep-screening`** - the sanctions and PEP lanes; run alongside this for a fuller adverse screen (sanctions + PEP + debarment + litigation).
- **`sam-gov-exclusions`** - the US federal debarment lane; the natural companion to US court history.
- **`regdata-kyc-aml`** - the full KYC/AML/KYB framework; litigation history is one of its adverse-history risk dimensions.
- **`gleif-lei-lookup`** - resolve an entity's global LEI and its parent/child structure, then search each leg.
- **`companies-house-uk`** - free source for the entity and the people to search.
