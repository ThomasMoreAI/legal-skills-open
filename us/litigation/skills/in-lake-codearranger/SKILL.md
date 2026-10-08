---
name: in-lake-codearranger
title: Lake Superior Court — Crown Point / Hammond / East Chicago
description: 'This skill should be used when the user asks to "file in Lake Superior Court", "Lake County Indiana", "Crown Point courthouse", "Hammond civil court", "East Chicago city court", "LR45", "Lake County local rule", "Lake civil division", "Northwest Indiana filing", "Calumet division", or any similar Lake County, Indiana filing question. Covers Lake Superior Court''s three-courthouse configuration (Crown Point Government Center, Hammond Civil Court, East Chicago City Court), the Civil Division case assignment, Lake County Local Rules of Court (the LR45 series), and Calumet Township small-claims practice. Trigger phrases: "Lake Superior", "Crown Point civil", "Hammond Superior", "LR45-TR", "Lake County e-filing", "Calumet Division", "Lake Circuit Court".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-lake
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Lake Superior Court — Crown Point / Hammond / East Chicago

Lake Superior Court is Indiana's **second-largest trial court** by
civil docket — sited in the northwest corner of the state along
the Calumet region and serving the Gary / Hammond / Merrillville
population center. The court is constituted under IC 33-33-45 and
operates from three primary courthouse complexes:

- **Lake County Government Center**, 2293 N. Main Street, Crown
  Point, IN 46307 — primary civil and criminal courthouse for
  Civil Divisions 1, 2, 3, and 4
- **Hammond Superior Court (East Chicago Division)**, 232 Russell
  Street, Hammond, IN 46320 — Civil Division 5 and limited
  criminal docket
- **East Chicago Superior Court**, 3711 Main Street, East
  Chicago, IN 46312 — minor civil and ordinance violations

The **Lake Circuit Court** is constituted separately under IC
33-33-45-1 and sits in Crown Point at the County Government
Center; the Circuit Court has overlapping civil jurisdiction with
the Superior Court (most Indiana counties have this dual structure
— see `in-county-courts`).

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify against current Lake County Local Rules and the assigned
> division's chambers practice before filing.

## Case assignment — by division and case type

Lake Superior Court assigns civil cases by **case-type code** and
random rotation across the Civil Division courts. The cause
number structure:

`45D01-2504-PL-000567`

Parsing:
- `45` — Lake County
- `D01` — Superior Court, Division 1 (Crown Point Civil 1)
- `2504` — April 2025 filing
- `PL` — Plaintiff (civil plenary)
- `000567` — sequence number

Division taxonomy:

| Cause prefix | Court | Location |
|--------------|-------|----------|
| `45C01` | Lake Circuit Court | Crown Point |
| `45D01` | Lake Superior Court, Civil Division 1 | Crown Point |
| `45D02` | Lake Superior Court, Civil Division 2 | Crown Point |
| `45D03` | Lake Superior Court, Civil Division 3 | Crown Point |
| `45D04` | Lake Superior Court, Civil Division 4 | Crown Point |
| `45D05` | Lake Superior Court, Civil Division 5 | Hammond |
| `45D11` | Lake Superior Court, County Division 1 (small claims) | Crown Point |
| `45D12` | Lake Superior Court, County Division 2 (Hammond) | Hammond |
| `45D13` | Lake Superior Court, County Division 3 (Gary) | Gary |
| `45D14` | Lake Superior Court, County Division 4 (East Chicago) | East Chicago |

The County Divisions (45D11-D14) carry the small-claims and
ordinance-violation dockets under IC 33-29-2; civil claims up to
$10,000 file there, while claims above $10,000 go to a Civil
Division.

## Lake County Local Rules (LR45)

Lake adopts local rules with the prefix `LR45`. Highlights:

| Rule | Subject |
|------|---------|
| LR45-TR3.1 | Appearance form |
| LR45-TR5 | Format of documents; chambers copies for filings over 20 pages |
| LR45-TR16 | Pretrial procedure; CMS template |
| LR45-TR40 | Trial setting and continuances |
| LR45-TR53.5 | Continuances — requires written motion, no oral motions |
| LR45-TR65 | Preliminary injunction — verified petition required |
| LR45-TR79 | Special judges; selection from Lake County panel |
| LR45-FL00 | Domestic Relations standing orders |
| LR45-AR1 | Court hours and holidays |

Compared to Marion: Lake's chambers-copy threshold is **20 pages**
(higher than Marion's 15) and the chambers copies must be
delivered to the assigned division's courtroom secretary, not the
judge directly.

## E-filing — Odyssey

Lake County adopted mandatory Odyssey e-filing for civil cases on
**July 1, 2017** (about six months after Marion). Same portal:
https://efile.courts.in.gov. Service Contacts and document codes
are identical to Marion.

Practical tips:

- Self-represented filers may e-file or paper-file. Paper filings
  are accepted at the Crown Point County Government Center
  Clerk's office Mon-Fri 8:30 AM - 4:30 PM.
- Filing fees: Lake's civil filing fee for a PL case is the
  statewide schedule under IC 33-37-4-4; verify the current Lake
  Clerk fee table.
- Document codes: identical to Marion's Odyssey schema.
- Hardcopy filings: paper filings still accepted from pro se
  filers under Indiana Administrative Rule 16 (the statewide
  e-filing rule's pro se carve-out).

## Civil case management — Lake Civil Divisions

Lake Civil Divisions do not have a unified CPC manual like Marion;
each division publishes its own case-management standing order on
the Lake Superior Court website (`lakecountyin.gov/superior-court`).
Common features across divisions:

- **Initial CMS**: due at the first status conference (typically
  60-90 days post-issue-joined)
- **Discovery cap**: T.R. 33(A)'s 25-interrogatory limit;
  Division 1 and Division 5 are stricter and require leave of
  court for any expansion
- **Motion practice**: motions submitted in writing under T.R. 7;
  oral argument requires a written request
- **Settlement conferences**: Lake divisions routinely set a
  mandatory settlement conference 60-90 days before trial

Lake Division 5 (Hammond) is the busiest division by case count
and runs the fastest docket; it has the shortest motion-decision
turnaround in the county.

## Township small-claims courts in Lake County

Lake County's small-claims docket runs through the **County
Divisions 11-14** (cause prefixes 45D11-D14) and is NOT a township
court. This differs from Marion County, where small-claims are
separate township courts. Lake's County Division clerks accept
small-claims complaints on a one-page Notice of Claim form
available on the Lake Superior Court website.

Jurisdictional caps and key features:

- Civil claims **up to $10,000** (IC 33-29-2-4)
- Trial de novo to Lake Superior Court Civil Division within 60
  days of judgment (IC 33-29-2-13)
- Bench trials only; no jury option
- Discovery limited; written discovery requires leave

## Composition — which skills layer here

- `in-statewide-format` for T.R. 5(E) / T.R. 10 baseline
- `in-pro-se` for self-represented filing in Lake
- `in-discovery` for T.R. 26-37 + Lake CMS interactions
- `in-deadlines` for T.R. 6 deadline math with Indiana legal
  holidays
- `in-schedule-hearing` for Lake-specific hearing setting
- `in-consumer-debt` if the case is a debt-collection action

## References

- `references/lr45-summary.md` — concise summary of every LR45
  rule
- `references/lake-divisions.md` — the 10 civil + county
  divisions with addresses and chambers contacts
- `references/lake-cause-numbers.md` — the cause-number parsing
  table

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current local rules and case law before filing.
