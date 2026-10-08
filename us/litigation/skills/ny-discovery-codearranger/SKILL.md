---
name: ny-discovery-codearranger
title: New York Discovery
description: Use when drafting, responding to, or compelling discovery in a New York civil case. Triggers include 'CPLR 3120 RFPs', 'NY notice for discovery and inspection', 'document production in NY case', 'CPLR 3130 interrogatories', '25- interrogatory limit', 'CPLR 3132 service of interrogatories', 'CPLR 3123 notice to admit', 'request to admit in NY', 'CPLR 3107 deposition notice', 'New York meet and confer', 'CPLR 3124 motion to compel', '22 NYCRR § 202.20-f conferral', 'Preliminary Conference order', 'CPLR 3101 scope of disclosure'. Covers CPLR Article 31 (Disclosure), the 25-interrogatory cap under CPLR 3130 + 3133, the 22 NYCRR § 202.20-f meet-and-confer rule (2021), motion to compel under CPLR 3124, the Preliminary Conference and Compliance Conference framework, and the CPLR 3101 "material and necessary" disclosure scope.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-discovery
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# New York Discovery

> **NOT LEGAL ADVICE.** Discovery practice in New York is
> driven by CPLR Article 31 plus the assigned Justice's Part
> Rules. Verify the Part Rules and any Preliminary Conference
> order before drafting or responding.

## Scope of disclosure — CPLR 3101

CPLR 3101(a) sets the broadest scope of any U.S.
jurisdiction: *"full disclosure of all matter material and
necessary in the prosecution or defense of an action."* The
*Allen v. Crowell-Collier Publ'g Co.*, 21 NY2d 403 (1968)
gloss reads "material and necessary" liberally — anything
that may *reasonably* lead to admissible evidence.

Exceptions (CPLR 3101(b)–(d)):

- **(b)** — privileged matter (attorney-client, doctor-
  patient under CPLR 4504, etc.)
- **(c)** — attorney's work product (absolute)
- **(d)(1)** — expert disclosures (statutory expert
  exchange)
- **(d)(2)** — materials prepared in anticipation of
  litigation ("trial-preparation materials") — qualified
  immunity, available on substantial-need showing

## Discovery devices

### 1. Notice for Discovery and Inspection (CPLR 3120) — "RFPs"

The NY analog to FRCP 34 / state-rule document requests.
Serve a written notice describing the documents/items with
"reasonable particularity"; the receiving party has **20
days** to serve a response under CPLR 3120(2) (default
under CPLR 2103, plus mail-rule add-ons; the Preliminary
Conference order often fixes a different response date).

### 2. Interrogatories (CPLR 3130–3134)

- **CPLR 3130**: written interrogatories available, but
  *not* alongside an EBT (deposition) in personal-injury,
  property-damage, or wrongful-death cases (CPLR 3130(1))
- **CPLR 3133(b)**: **25-interrogatory limit** — counted
  per discrete subject; subparts can count separately
- **CPLR 3133(a)**: response due **20 days** after service
- **CPLR 3133(b)**: response in writing, signed and verified
  by the responding party (corporate parties: an officer)

The 25-cap is the same as the federal limit under FRCP 33.

### 3. Notice to Admit (CPLR 3123)

The NY analog to FRCP 36 / RFAs. Serve a notice with
discrete requests; **20-day** response window; non-response
is **deemed an admission**. Limitations: cannot demand
admission of ultimate issues (*Tomasino*, 22 AD3d 540) and
not appropriate for genuinely disputed material facts.

### 4. Depositions (CPLR 3106–3119) — "EBT" (Examinations Before Trial)

- **CPLR 3106**: priority of EBT — plaintiff usually goes
  first
- **CPLR 3107**: notice on **20 days'** notice; non-party
  by subpoena under CPLR 3119
- **22 NYCRR § 202.7(a)**: meet-and-confer attempt required
  before motion practice related to depositions
- **Sanctions for EBT non-attendance**: CPLR 3126

### 5. Other devices

- **Bill of Particulars** (CPLR 3041–3044) — clarifies
  pleading; not technically "discovery" but functionally
  used to flesh out allegations
- **Notice for Production of Statements** (CPLR 3101(e))
- **Independent Medical Examination** (CPLR 3121)

## Meet-and-confer — 22 NYCRR § 202.20-f (Feb 2021)

In **Supreme/County Court civil actions**, before moving to
compel or for a protective order, the movant must:

1. **Confer in good faith** with the opposing party in
   person or by phone (a single email exchange typically
   doesn't satisfy)
2. **File an affirmation of good-faith conferral** —
   identifying the dates and substance of conferral attempts

Some Justices' Part Rules impose **additional pre-motion-
letter requirements** before filing a motion to compel — a
short letter to chambers laying out the dispute, with the
opposing party's letter in response, before any formal
motion is permitted.

## Motion to compel — CPLR 3124

If the opposing party fails to respond or provides
inadequate responses, move to compel under **CPLR 3124**.

Process:

1. **Meet and confer** per 22 NYCRR § 202.20-f
2. **Notice of Motion** returnable before the assigned IAS
   Part (CPLR 2214)
3. **Affirmation** detailing the discovery served, the
   responses received (or non-response), and the
   inadequacy; attach the discovery requests and any
   response as exhibits
4. **Memorandum of Law** (optional but often expected by
   Commercial Division Justices)
5. **Proposed Order** — see `ny-draft-order`

Available relief under CPLR 3124 + 3126:

- Order compelling disclosure
- Conditional order of dismissal/preclusion (CPLR 3126)
- Striking the pleading (drastic; CPLR 3126(3))
- Default judgment (CPLR 3126(3))
- Costs and counsel fees (22 NYCRR § 130-1.1)

## Preliminary Conference (22 NYCRR § 202.12)

Within 45 days of RJI, the IAS Part holds a Preliminary
Conference. The PC order sets a discovery schedule:

1. Bill of Particulars demanded/served
2. Document discovery (CPLR 3120) demanded/served
3. Interrogatories (CPLR 3130) demanded/served
4. Depositions noticed/taken
5. Note of Issue filing date

The PC order *supersedes* the CPLR 3120(2) 20-day default
response window; rely on the PC order's dates.

## Compliance Conference + Note of Issue

- **Compliance Conference** — mid-discovery; verify
  schedule adherence
- **Note of Issue** (22 NYCRR § 202.21) — certifies
  discovery complete; triggers the dispositive-motion
  window (typically 60–120 days, set per Part Rules)
- **Certificate of Readiness** — filed with the Note of
  Issue; affirms discovery complete

## Composition with other ny- skills

- `ny-statewide-format` — format for discovery papers
- `ny-draft-motion` + `ny-draft-declaration` — scaffolders
  for motion to compel + supporting affirmation
- `ny-deadlines` — CPLR 3133/3107/3123 timing computation
- `ny-consumer-debt` — debt-buyer-specific RFPs and notices
  to admit
- `ny-nyco` / `ny-kings` / etc. — county-specific Part Rule
  variations
