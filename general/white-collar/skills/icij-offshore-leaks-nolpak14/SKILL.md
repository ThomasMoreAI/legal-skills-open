---
name: icij-offshore-leaks-nolpak14
title: Icij offshore leaks
description: 'Search a person or company against the ICIJ Offshore Leaks Database for free - the Panama Papers, Paradise Papers, Pandora Papers, Bahamas Leaks and Offshore Leaks records of offshore entities, officers and intermediaries, for enhanced due diligence. Use for offshore-structure red-flags and the offshore leg of an enhanced-DD / EDD / KYC / AML workflow. Trigger on: ''offshore leaks'', ''Panama Papers'', ''Pandora Papers'', ''Paradise Papers'', ''offshore entities'', ''is this person in the offshore leaks'', ''offshore structure'', ''ICIJ'', ''shell company search'', ''enhanced due diligence''. This is a leak-data red-flag lane, NOT a company registry and NOT proof of wrongdoing - a match is a prompt to dig deeper, never a conclusion; no API key required.'
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/icij-offshore-leaks
license: MIT
version: 0.1.2
execution_mode: open
jurisdiction: general
practice: white-collar
language: en
---

# icij-offshore-leaks

Search a name against the **ICIJ Offshore Leaks Database** - the offshore leg of an enhanced due-diligence (EDD) check. Take the entity and the beneficial owners / directors you extracted from a registry, and ask a single question: does any of them appear in the offshore leaks? This runs on ICIJ's public database aggregating the Panama Papers, Paradise Papers, Pandora Papers, Bahamas Leaks and the original Offshore Leaks - **free and keyless**. But read the disclaimer below before you read a single result: this is leak data, and appearing in it is a *red flag to investigate*, never a finding of wrongdoing.

> **ICIJ disclaimer (carry this on every output):** "ICIJ does not intend to suggest or imply that any individuals, companies or other entities included in the Offshore Leaks Database have broken the law or otherwise acted improperly. There are legitimate uses for offshore companies and trusts."

## Persona

You are an enhanced due-diligence analyst running the offshore-structure lane of a screen. You search customers, counterparties, and their beneficial owners for exposure to leaked offshore data, you understand that a name match is a *candidate to verify* - not a hit, and never proof of wrongdoing (ICIJ itself disclaims that reading; there are legitimate reasons to hold an offshore company or trust) - and you keep offshore exposure separate from sanctions, litigation and debarment: distinct data problems that together make one screen.

## What this gives you (for free)

- **Entities** - the offshore companies, trusts and foundations named in the leaks: name, jurisdiction of incorporation, linked country, incorporation/struck-off dates, and the source leak.
- **Officers** - the people and companies connected to those entities (shareholders, directors, beneficiaries).
- **Intermediaries** - the go-betweens (law firms, agents, banks) that set up or managed the structures.
- **Addresses** - the registered addresses tying the records together - the key corroborator for confirming a common-name match.

Each record carries which leak it came from (`sourceID`), so you can tell a Panama Papers entity from a Pandora Papers one. This is leak data curated by an investigative-journalism non-profit, **not an official register**.

## Licence (free, but attribution + share-alike apply)

The database is released under the **Open Database License (ODbL) v1.0**, and its contents under **CC-BY-SA**. **Commercial use is allowed** (this is *not* a non-commercial licence) - but two obligations attach to any redistribution or derivative:

- **Attribution** - you must cite ICIJ as the source.
- **Share-alike** - a derivative database carries the same ODbL/CC-BY-SA licence.

Using it internally as one EDD signal is fine; publishing a derived dataset triggers the share-alike terms.

## Data sources (no key)

Base URL: `https://offshoreleaks.icij.org`

| # | Purpose | Method + path |
|---|---|---|
| 1 | Reconcile / search by name | `POST /api/v1/reconcile` |
| 2 | Node detail (entity/officer/etc.) | `GET /nodes/{id}.json` |
| 3 | Bulk download (CSV + Neo4j dumps) | `https://offshoreleaks.icij.org/pages/database` |

The search endpoint is a **W3C Reconciliation Service (v0.2)**. Post `queries` as a map; each query returns ranked candidate matches:

```bash
# 1. Search for a name (keyless)
curl -s "https://offshoreleaks.icij.org/api/v1/reconcile" \
  --data-urlencode 'queries={"q0":{"query":"ACME HOLDINGS LIMITED"}}'

# 2. Pull the full record for a matched node id
curl -s "https://offshoreleaks.icij.org/nodes/12345678.json"
```

Each reconcile match returns: `id`, `name`, `description` (which leak the record is from), `score`, `match` (a boolean the service sets on a confident single match), and `types[]` - the record type (entity / officer / intermediary / address). You can filter by type in the query. Resolve any `id` to its full record via endpoint 2.

## Response fields

- **Identity** - `name` (the entity / officer / intermediary), and the record `type`.
- **Jurisdiction** - the jurisdiction of incorporation plus the linked `countries` / `country_codes`.
- **Source leak** - `sourceID`: one of *Offshore Leaks (2013)*, *Panama Papers (2016)*, *Bahamas Leaks (2016)*, *Paradise Papers (2017)*, *Pandora Papers (2021)*.
- **Status** - `valid_until` (the leak snapshot the record belongs to) and any `categories`.
- **Relationships** - the linked nodes: *officer-of*, *registered-address*, *intermediary-of* - how the person, the company, the address and the agent connect.

## Workflow: search an entity and its owners

```
1. Build the subject list
   -> the entity name + every beneficial owner / director you extracted
      (e.g. from CRBR, KRS, Handelsregister, Companies House PSC)

2. Reconcile each name  (POST /api/v1/reconcile)
   -> read the ranked candidates and their score / sourceID / type

3. Confirm identity before you call it a match
   -> pull the node (GET /nodes/{id}.json) and corroborate with a second
      identifier: address, jurisdiction, DOB, or a related party from the
      registry data. Name alone is never enough.

4. Interpret each confirmed match as a PROMPT, not a verdict
   -> confirmed subject in a leak -> RED FLAG: escalate to enhanced DD; ask
      why the structure exists. Not a finding of wrongdoing.
   -> name-only match, no corroboration -> likely a name collision: document why
   -> no match -> no offshore-leaks exposure found (this database, this snapshot)

5. Record the search: which name, the query date, node ids, and the outcome
   per subject - each carrying the ICIJ disclaimer
```

## Output interpretation

- **Appearing in the database is a red flag to investigate, never a conclusion.** Carry the ICIJ disclaimer on every result: *"ICIJ does not intend to suggest or imply that any individuals, companies or other entities included in the Offshore Leaks Database have broken the law or otherwise acted improperly. There are legitimate uses for offshore companies and trusts."* A match tells you to dig deeper - not that anyone did anything wrong.
- **A name match is a candidate, not a verdict.** Name collisions are common; the database does no entity resolution. Confirm the hit is *your* subject with a second identifier - address, DOB, jurisdiction, or a related party from the registry data - before acting on it. This is the same adjudication discipline as `sanctions-pep-screening` and `us-court-records`.
- **This is leak data, not an official register.** It returns records from a fixed leak snapshot, not live entity records - there is no current registry status, no filing history, no proof the structure still exists. Resolve the entity itself with a registry skill; use this only as a red-flag overlay.
- **The data is static and dated.** Each leak is a periodic release (the Panama Papers data, for example, runs current through roughly 2015). "No match" means nothing was found *in these snapshots* - it is not proof of no offshore exposure. Say so when you report a clear result.
- **Offshore exposure is not sanctions, litigation or debarment.** An offshore-leaks hit tells you a party appears in leaked offshore data - not that it is sanctioned, sued, or barred. Run those lanes separately.

## Cross-sell - the offshore-structure lane of a fuller screen

This skill is one lane of an enhanced due-diligence screen. Pair it with the sanctions, litigation and adverse-media lanes, and wire all of them onto the registry actors: extract the beneficial owners and directors, then run each one across sanctions, US court history, adverse media, and the offshore leaks.

| Lane | Source |
|---|---|
| Sanctions + PEP (OFAC / EU / UK / UN, free) | `sanctions-pep-screening` |
| US litigation / adverse history (free) | `us-court-records` |
| US federal debarment / exclusions (free) | `sam-gov-exclusions` |
| Adverse media over the same subject | `regdata/adverse-media-scraper` |
| Extract beneficial owners (PL) | `regdata/crbr-beneficial-owners-scraper` |
| Extract board members (PL) | `regdata/krs-fullnames-scraper` |
| Extract PSC / officers (UK, free) | `companies-house-uk` |

For the full workflow - risk scoring, adverse-media overlay, cross-source validation - route to **`regdata-kyc-aml`**. The registry actors use a free Apify token: https://apify.com?fpr=getregdata.

## Related skills

- **`sanctions-pep-screening`** - the sanctions and PEP lanes; run alongside this for a fuller adverse screen (sanctions + PEP + litigation + offshore).
- **`us-court-records`** - the US litigation / adverse-history lane; the natural companion to offshore-structure red-flags.
- **`sam-gov-exclusions`** - the US federal debarment lane.
- **`regdata-kyc-aml`** - the full KYC/AML/KYB framework; offshore exposure is one of its enhanced-DD risk dimensions.
- **`gleif-lei-lookup`** - resolve an entity's global LEI and its parent/child structure, then search each leg here.

## More on getregdata.com

- All skills and paid registry coverage: https://getregdata.com/skills/ and https://getregdata.com/registries/
