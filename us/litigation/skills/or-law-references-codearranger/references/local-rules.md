# Local Rules — Oregon Supplemental Local Rules (SLR)

Each Oregon circuit court adopts **Supplemental Local Rules
(SLR)** layered on top of the statewide UTCR. When the SLR
conflicts with the UTCR, the UTCR controls (UTCR 1.040). When
the UTCR is silent, the SLR governs.

This reference summarizes the most-used SLR sections for the
high-volume circuits. Pull the current PDF from each county's
website before citing.

## Authoritative source

For each county:
```
https://www.courts.oregon.gov/courts/[county-slug]/rules
```

Examples:
- https://www.courts.oregon.gov/courts/multnomah/rules
- https://www.courts.oregon.gov/courts/washington/rules
- https://www.courts.oregon.gov/courts/clackamas/rules
- https://www.courts.oregon.gov/courts/lane/rules
- https://www.courts.oregon.gov/courts/marion/rules

## Multnomah County SLR (4th Judicial District)

The most-developed Oregon SLR. Updates typically effective
February 1 or August 1.

### Chapter 5 — Motions

- **SLR 5.015** — Notice of Hearing on Motion: filed within 3
  business days of JA confirming the date
- **SLR 5.025** — Setting motions: through the assigned judge's
  JA (not a centralized motions clerk)
- **SLR 5.045** — Meet-and-confer certification required on
  every ORCP 36, 43, 44, 45, 46 motion
- **SLR 5.060** — Ex parte motions: notice required unless
  excused; civil ex parte hours M–F 8:30 AM – 12:00 PM in the
  Ex Parte Department
- **SLR 5.100** — Working copies: required for motions over 25
  pages total, SJ motions (always), or where judge requests
- **SLR 5.101** — Submission of orders: routed to chambers, not
  the clerk's office

### Chapter 7 — Conferences and remote hearings

- **SLR 7.010** — WebEx is default for routine civil motions;
  in-person reserved for evidentiary hearings and SJ

### Chapter 8 — Mandatory arbitration (ORS 36.400)

- **SLR 8.010** — Cases $10,000–$50,000 go to arbitration;
  arbitrators from the OJD panel

### Chapter 12 — Pretrial

- **SLR 12.010** — Pretrial conference mandatory in non-
  arbitration cases set for trial, 30–60 days before trial

## Washington County (Oregon) SLR (20th Judicial District)

### Chapter 5

- **SLR 5.025** — Setting motions: through the Civil Division
  (not assigned judge's JA)
- **SLR 5.045** — Notice of Hearing filed **simultaneously**
  with the motion (stricter than Multnomah)
- **SLR 5.046** — Meet-and-confer certification on discovery
  motions
- **SLR 5.060** — Ex parte: notice required; Civil Division
  counter
- **SLR 5.100** — Working copies: motions over **15 pages**
  total (lower threshold than Multnomah's 25)
- **SLR 5.101** — Submission of orders to chambers

### Chapter 7

- **SLR 7.010** — Remote hearings per assigned judge's
  standing order

### Chapter 8

- **SLR 8.010** — Mandatory arbitration

## Clackamas County SLR (5th Judicial District)

### Chapter 5

- Motion scheduling: lightly centralized; the Civil counter at
  807 Main Street, Oregon City, sets dates for most judges
- Working copies encouraged for any motion; required for SJ
- Standing orders on individual judges' pages

## Lane County SLR (2nd Judicial District)

### Chapter 5

- Strong individual-JA practice
- Court Administrator at 125 E 8th Ave handles scheduling that
  does not route through a JA
- Working copies per assigned judge's standing order
- SLR 5 is well-developed; pull current PDF from
  courts.oregon.gov/courts/lane/rules

## Marion County SLR (3rd Judicial District)

### Chapter 5

- Civil Department on Floor 2, 100 High Street NE, Salem
- Strong active SLR; Marion sees significant administrative-
  law and state-government civil filings
- Working copies required for SJ; judge-discretion otherwise

## Other counties — at a glance

| County | District | Salient SLR feature |
|--------|----------|---------------------|
| Jackson | 1st | Lightly centralized; significant rural-civil docket |
| Deschutes | 11th | Civil scheduling through court coordinator |
| Linn | 23rd | Centralized motion docket common |
| Benton | 21st | Combined with Lincoln; centralized motion docket |
| Yamhill | 25th | Centralized motion docket |
| Polk | 12th | Centralized motion docket |
| Douglas | 16th | Centralized motion docket |
| Rural counties (Wallowa, Wheeler, etc.) | 7th, 10th, 24th | Centralized motion docket; minimal SLR |

For any non-listed county, pull the SLR PDF from
courts.oregon.gov/courts/[county-slug]/rules.

## How SLRs interact with UTCR

- **UTCR controls** when the SLR conflicts (UTCR 1.040)
- **UTCR 2.010** format requirements (paper, margins, fonts)
  apply statewide; SLRs cannot relax them
- **UTCR 5.050** oral argument convention applies statewide;
  SLRs add detail on scheduling
- **UTCR 7.010** remote hearings is enabled by SLR
  implementation (each county decides default mode)
- **UTCR 21** eFiling rules apply statewide; SLRs supplement
  for document codes and local procedures

## Common Multnomah vs. Washington Co differences

| Aspect | Multnomah | Washington Co (OR) |
|--------|-----------|---------------------|
| Scheduling | Through JA | Through Civil Division |
| Notice of Hearing timing | Within 3 business days of JA confirm | Simultaneous with motion |
| Working-copy threshold | 25 pages | 15 pages |
| Meet-and-confer SLR | SLR 5.045 | SLR 5.046 |
| Order submission | Chambers email | Chambers / Civil Division |
| Default hearing mode | WebEx for routine | Judge-dependent |

When porting practice between Multnomah and Washington County,
these are the first details to update — the SLR numbering and
thresholds differ.

## Inquiring about an SLR

When the user asks "what does Multnomah SLR 5.100 require?",
the workflow is:

1. Fetch the current Multnomah SLR PDF:
   ```
   WebFetch:
     url: https://www.courts.oregon.gov/courts/multnomah/rules
     prompt: Locate the link to the current Multnomah SLR PDF,
             then locate Section 5.100. Quote the verbatim
             text and identify the effective date.
   ```
2. Quote the verbatim text in the answer
3. Note the effective date and any recent amendments
4. Flag if the section has been renumbered since prior versions

Never paraphrase from memory in a filing or court-facing
communication. Pull the current text.
