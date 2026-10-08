# Recent Decisions — Oregon and 9th Circuit Consumer-Debt

A tracking reference for recent appellate decisions affecting
Oregon consumer-debt defense. **This file should be refreshed
periodically** (the quarterly remote-agent routine, or by ad
hoc research at the start of any new case).

> **NOT LEGAL ADVICE.** Verify each citation; case law
> evolves.

## How to use this reference

For any Oregon debt-buyer or consumer-debt case starting:

1. **Check this reference** for recent decisions impacting
   your fact pattern
2. **Run a fresh search** on CourtListener for Oregon (Or,
   Or App) + 9th Circuit (Ca9) opinions in the last 2 years
   using key terms (FDCPA, UTPA, ORS 697, chain of title,
   business records)
3. **Note any case currently in active litigation** that may
   change the law before your case concludes
4. **Update this file** after research (pull-request the
   updates if a corpus refresh is appropriate)

## Recent Oregon decisions to research

### Oregon Court of Appeals

Recent areas of focus (search by keyword on CourtListener):

- **OEC 803(6) foundation** in debt-buyer cases —
  authentication of original-creditor records by remote
  custodian
- **ORS 697 registration** — DCBS registration requirements
  and lack-of-capacity defense
- **UTPA scope** in debt-collection contexts — "ascertainable
  loss" standard, punitive damages
- **ORCP 71 vacation** — recent applications of the *Wagar*
  three-factor analysis
- **ORS 12.080 SOL** — open-account vs. written-contract
  characterization

### Oregon Supreme Court

Less frequent debt-specific decisions, but watch for:

- UTPA scope decisions
- ORCP 47 SJ standard refinements
- Fee-shifting case law (ORS 20.075, 20.105 applications)

## Recent 9th Circuit decisions

The 9th Circuit binds federal practice in Oregon and is
persuasive in Oregon state court. Recent areas:

- **FDCPA SOL** application (post-*Rotkiske*)
- **Reg F implementation** decisions (post-November 2021
  effective date)
- **Class certification** in FDCPA / FCRA cases
- **Article III standing** developments (*TransUnion LLC v.
  Ramirez*, 594 US ___ (2021), and progeny)
- **Bankruptcy proof-of-claim** practice on time-barred debt
  (post-*Midland v. Johnson*)

## Supreme Court of the United States

Watch for:

- FDCPA scope and remedies decisions
- Article III standing in consumer-protection cases
- Federal arbitration preemption (impacts Oregon UTPA
  carve-outs)

## Recent CFPB enforcement actions

The CFPB regularly issues enforcement actions and amicus
briefs that interpret FDCPA / Reg F. These are not binding
authority but inform plaintiff behavior:

- CFPB consent orders against debt buyers
- CFPB amicus briefs in private FDCPA litigation
- CFPB enforcement priorities

Pull from: https://www.consumerfinance.gov/enforcement/

## How to refresh this list

### CourtListener search query (Oregon)

```
WebFetch:
  url: https://www.courtlistener.com/?q=%22FDCPA%22+OR+%22ORS+646%22+OR+%22ORS+697%22&type=o&court=or,orctapp&order_by=dateFiled+desc
  prompt: List the 10 most recent Oregon Supreme Court and
          Court of Appeals decisions touching on FDCPA,
          Oregon UTPA, or ORS 697. For each, provide:
            - Citation
            - Date
            - Brief 1-sentence holding
            - Whether the decision is published or unpublished
```

### CourtListener search query (9th Circuit)

```
WebFetch:
  url: https://www.courtlistener.com/?q=%22FDCPA%22+OR+%22Regulation+F%22&type=o&court=ca9&order_by=dateFiled+desc
  prompt: List the 10 most recent 9th Circuit decisions
          on FDCPA or Regulation F. For each, provide:
            - Citation
            - Date
            - Brief 1-sentence holding
```

### Caselaw Access Project (older Oregon decisions)

For older Oregon decisions not in CourtListener:

```
WebFetch:
  url: https://api.case.law/v1/cases/?jurisdiction=or&search=[query]
  prompt: Search the Oregon Reports for [topic]. Identify
          decisions on point.
```

## Quarterly refresh routine

The plugin's quarterly agent routine (mirroring the WA
plugin's `trig_018yahbiUwS1uTUJSuDNrCqG`) should:

1. Pull the latest Oregon Court of Appeals decisions on:
   - FDCPA / Reg F
   - ORS 646.605 (UTPA)
   - ORS 697 (Collection Agency)
   - ORS 12.080 (SOL)
   - OEC 803(6) / 902(11) (business records)
2. Pull the latest 9th Circuit decisions in similar areas
3. Pull recent CFPB enforcement actions
4. Update this file if any decision materially affects the
   substantive law summarized in other references

## What to do when this reference is stale

If you can't run the refresh routine in real-time:

1. Treat the references in this directory as **last verified
   on the date of the plugin version**
2. **Re-verify** key cases against CourtListener before
   citing in a filing
3. **Note in the filing** if a key holding is from a recent
   decision that might be subject to en banc review or
   Supreme Court review

## Reading recent decisions

When a recent Oregon Court of Appeals decision is found:

- **Read the full opinion**, not just the headnote
- **Check for concurrences / dissents** — they may signal
  doctrinal instability
- **Check the disposition** — published vs. unpublished
- **Check for petition for review** filed in the Oregon
  Supreme Court — if granted, the case is in flux

## Cross-references

- `or-consumer-debt` SKILL — main bundle
- `references/key-cases.md` — foundational cases
- `references/fdcpa.md` — FDCPA detail
- `references/utpa.md` — UTPA detail
- `references/ors-697.md` — ORS 697 detail
- `references/evidence-debt-buyer.md` — OEC 803(6) /
  902(11) doctrine
- `or-law-references/references/online-sources.md` —
  canonical URLs
- `or-law-references/references/legal-data-apis.md` —
  programmatic access
