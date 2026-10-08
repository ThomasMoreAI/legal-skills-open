---
name: or-county-courts-codearranger
title: Oregon county circuit courts (non-Multnomah / non-Washington)
description: 'This skill should be used when drafting or filing civil documents in an Oregon circuit court other than Multnomah or Washington County — i.e., the circuit courts of the state''s other most populous counties: Clackamas (Oregon City), Lane (Eugene), Marion (Salem), Jackson (Medford), Deschutes (Bend), Linn (Albany), Benton (Corvallis), Yamhill (McMinnville), Polk (Dallas), and Douglas (Roseburg). Triggers include the county name plus "Circuit Court" / "where do I file" / "eFile" / "File and Serve" / "local rules" / "civil motion calendar", or a case venued in one of those counties. For Multnomah use `or-multcc`; for Washington County (Oregon) use `or-wccc`. Layer on top of `or-statewide-format`, and consult `or-law-references` for the per-court SLR text.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-county-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: County Courts Directory
  path: references/county-courts-directory.md
- title: Filing And Service
  path: references/filing-and-service.md
---

# Oregon county circuit courts (non-Multnomah / non-Washington)

Use this skill in addition to `or-statewide-format` when filing
in any Oregon circuit court other than Multnomah County or
Washington County.

> **NOT LEGAL ADVICE.** These notes describe each venue's
> procedural mechanics as a drafting aid, not legal advice. Local
> rules and judge-specific practices change; verify with the
> clerk and the current SLR before relying on anything here.

Oregon has 36 counties and 27 judicial districts (some districts
combine multiple counties — e.g., the 21st District is Benton
County only; the 22nd District is Crook and Jefferson). Every
county has at least one circuit court courthouse. The high-volume
counties below have their own SLR, judicial assistants, and
established motion practice.

## County / venue table — Oregon's most populous counties (after Multnomah & Washington)

| County | Seat | Courthouse / address | Judicial District | Civil contact |
|--------|------|----------------------|-------------------|---------------|
| Clackamas | Oregon City | 807 Main St, Oregon City OR 97045 | 5th | (503) 655-8447 |
| Lane | Eugene | 125 E 8th Ave, Eugene OR 97401 | 2nd | (541) 682-4020 |
| Marion | Salem | 100 High St NE, Salem OR 97301 | 3rd | (503) 588-5105 |
| Jackson | Medford | 100 S Oakdale Ave, Medford OR 97501 | 1st | (541) 776-7171 |
| Deschutes | Bend | 1100 NW Bond St, Bend OR 97703 | 11th | (541) 388-5300 |
| Linn | Albany | 300 SW 4th Ave, Albany OR 97321 | 23rd (with Benton) | (541) 967-3845 |
| Benton | Corvallis | 120 NW 4th St, Corvallis OR 97330 | 21st | (541) 766-6800 |
| Yamhill | McMinnville | 535 NE 5th St, McMinnville OR 97128 | 25th | (503) 434-7470 |
| Polk | Dallas | 850 Main St, Dallas OR 97338 | 12th | (503) 623-3154 |
| Douglas | Roseburg | 1036 SE Douglas Ave, Roseburg OR 97470 | 16th | (541) 957-2410 |

Pull current contacts from the OJD county-court page:
**https://www.courts.oregon.gov/courts/Pages/find-a-court.aspx**

Phone numbers and street addresses change. Verify the current
contact before drafting a date-request email or mailing
working copies.

## Caption — county variant

The court header line uses "FOR THE COUNTY OF [NAME]":

```
            IN THE CIRCUIT COURT OF THE STATE OF OREGON
                  FOR THE COUNTY OF CLACKAMAS
```

Case numbers follow the statewide format (`25CV12345`,
`25SC12345`, etc.) — same across all counties.

## Scheduling models across counties

Oregon counties use one of three motion-scheduling models:

| Model | Counties (typical) | How motions are set |
|-------|----------------------|---------------------|
| **Centralized motion docket** | Some smaller counties; varies by year | A single judge hears all civil motions on a rotating week; date reservation through court coordinator |
| **Court-administrator scheduling** | Lane, Marion, Jackson, Deschutes | Civil motions set by Court Administrator or Civil Department clerk |
| **Individual JA** | Multnomah; some larger civil departments in Lane, Marion | Date requested directly to assigned judge's JA |

To determine which model a county uses, look at its SLR Chapter
5 (Motions) and its court website. When in doubt, **call the
Civil Division** of the relevant courthouse.

## Per-county notes

### Clackamas County Circuit Court — Oregon City

- 5th Judicial District (Clackamas only)
- Multi-judge civil department; lightly centralized scheduling
- SLR available at courts.oregon.gov/courts/clackamas/rules
- Mandatory arbitration ($10K–$50K) follows ORS 36.400
- Civil counter: 807 Main Street, Oregon City OR 97045
- Active legal-aid presence: Legal Aid Services of Oregon —
  Clackamas branch

### Lane County Circuit Court — Eugene

- 2nd Judicial District (Lane only)
- Largest court in the Willamette Valley after Marion
- Strong individual-JA practice for most civil judges
- Lane SLR has detailed motion-practice rules (SLR Chapter 5)
- Multiple branch courthouses: Eugene (main, 125 E 8th Ave),
  Florence (small claims and limited civil; check current
  hours)
- Civil contact: (541) 682-4020

### Marion County Circuit Court — Salem

- 3rd Judicial District (Marion only); 5 civil judges
- Salem is the state capital; Marion sees significant
  administrative-law and state-government civil filings
- Marion SLR available at courts.oregon.gov/courts/marion/rules
- Civil Department on Floor 2, 100 High Street NE, Salem
- Mandatory arbitration program follows ORS 36.400
- Active pro bono panel through Marion County Bar

### Jackson County Circuit Court — Medford

- 1st Judicial District (Jackson and Josephine combined)
- Civil division at 100 S Oakdale Ave, Medford OR 97501
- Lightly centralized motion scheduling
- Significant rural-civil docket; FED (landlord-tenant) cases
  prominent

### Deschutes County Circuit Court — Bend

- 11th Judicial District (Deschutes only)
- Fast-growing; civil filings up significantly since 2018
- Civil scheduling through court coordinator
- Bend courthouse at 1100 NW Bond Street

### Linn County (Albany) — Benton County (Corvallis)

- 23rd Judicial District is Linn-only; 21st is Benton-only
- Distinct courthouses in Albany and Corvallis; share some
  administrative resources
- Smaller-population counties; centralized motion docket
  common

### Yamhill, Polk, Douglas

- Smaller counties with centralized motion dockets
- Many filings handled by the court coordinator rather than
  individual JAs

## Authoritative source — pull the current court page per county

For each county, the canonical source for judges, courtrooms,
JAs, hours, and SLR is:

**https://www.courts.oregon.gov/courts/[county-slug]/Pages/default.aspx**

Examples:
- /courts/clackamas/
- /courts/lane/
- /courts/marion/
- /courts/jackson/
- /courts/deschutes/

Each county page links to its current SLR PDF. Pull the current
PDF before relying on any SLR section.

## Filing fees

Statewide schedule under ORS 21.135-21.170; identical across all
36 counties. Verify against
https://www.courts.oregon.gov/services/fees/Pages/default.aspx

Fee waiver (ORS 21.682) and in forma pauperis (ORS 20.140) apply
identically across counties.

## eFiling

All Oregon circuit courts use **OJD File and Serve** (Tyler
Tech) statewide. Document codes are the same statewide; the
filing user picks the county at filing.

- Portal: https://oregon.tylertech.cloud/
- Self-help page: courts.oregon.gov/services/online/Pages/efile.aspx
- Help line: (855) 642-9748 (Tyler Tech support)
- File size: 25 MB per document; split larger filings

## Mandatory arbitration

ORS 36.400 et seq. applies statewide. Every county uses the OJD
arbitrator panel. The arbitration program differs slightly
across counties in how arbitrators are assigned (random vs.
party selection) — see the county's SLR Chapter 8.

## Document set (typical for any Oregon county)

1. Motion
2. Memorandum in Support (if argument over 1 page)
3. Supporting Declaration(s) with exhibits
4. Proposed Order ("[PROPOSED]" in title)
5. Notice of Hearing
6. Certificate of Service
7. Working copies (for motions over the local SLR threshold)

The set is the same statewide; the **timing** of when the
Notice of Hearing is filed and the **threshold** for working
copies vary by county SLR.

## Scheduling email — generic county template

```
To:      [Civil Division / court coordinator / JA email]
Subject: Hearing Date Request — [Case Short Title],
         Case No. [Cause Number]

Civil Division:

I am [Counsel of record / Defendant, pro se] in [case short
title], Case No. [cause number], assigned to [Judge Name (if
known)].

I am requesting a hearing date for [Motion Title], to be filed
[date]. Estimated argument time: [X minutes].

Proposed dates:
   [Date 1]
   [Date 2]
   [Date 3]

If the Court prefers WebEx or telephone, please advise so I can
include the connection details on the Notice of Hearing.

Thank you,
[Name][, pro se / OSB #]
[Contact info]
```

## References

- `references/county-courts-directory.md` — full directory of
  all 36 Oregon counties, their seats, judicial districts, and
  contact numbers
- `references/filing-and-service.md` — county-by-county quirks
  in filing and service practice
