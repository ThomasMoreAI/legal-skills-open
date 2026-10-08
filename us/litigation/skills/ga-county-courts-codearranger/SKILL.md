---
name: ga-county-courts-codearranger
title: Georgia County Courts — Rest-of-State Roll-Up
description: 'Use when handling a Georgia case in any county NOT covered by the dedicated venue skills (`ga-fulton`, `ga-cobb`, `ga-gwinnett`). A rest-of-state roll-up that drives the per-county research workflow: identify the county''s judicial circuit, whether it has a State Court, its Magistrate Court, which e-filing platform it uses (PeachCourt vs. Odyssey eFileGA), the local rules, and the clerk''s filing and fee practices. Triggers: "file in [other Georgia county]", "my Georgia county court", "which e-filing system Georgia", "PeachCourt or eFileGA", "what circuit is [county] in", "does [county] have a State Court", "Superior Court of [county]", "Georgia county clerk filing", "Georgia local court rules". Statewide rules (CPA, the Uniform State / Superior / Magistrate Court Rules, O.C.G.A. § 9-11-10 format) apply everywhere; local practice and standing orders vary by circuit. Layers on top of `ga-statewide-format`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-county-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Georgia County Courts — Rest-of-State Roll-Up

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. Verify
> every step against the current local rules of the filing court, the
> assigned judge's standing orders, and the clerk's practices before
> filing. County and circuit practices change; confirm with the clerk
> before relying on anything here.

Use this skill in addition to `ga-statewide-format` when the case is
in a Georgia county **other than** Fulton, Cobb, or Gwinnett (which
have their own venue skills: `ga-fulton`, `ga-cobb`, `ga-gwinnett`).
Georgia has **159 counties** — far too many for one skill each — so
the long tail is handled by a **per-county research workflow** plus
this roll-up. The statewide rules are uniform; what varies county to
county is the **court structure**, the **e-filing platform**, the
**local rules**, and the **clerk's practices**.

## What is uniform statewide (applies in every county)

- The **Georgia Civil Practice Act** (O.C.G.A. Title 9, Chapter 11) —
  same answer, default, discovery, and summary-judgment rules
  everywhere.
- The **Uniform Superior Court Rules**, the parallel **Uniform State
  Court Rules**, and the **Uniform Magistrate Court Rules**.
- The **pleading-format baseline** (O.C.G.A. § 9-11-10 caption,
  numbered paragraphs, separate counts) plus the marketplace format
  baseline — see `ga-statewide-format`.

## What varies by county (the per-county research workflow)

Before drafting or filing in a non-flagship county, work through these
steps:

### 1. Identify the county's judicial circuit (O.C.G.A. § 15-6-1)

Every county sits in a **judicial circuit**; the Superior Court judges
are assigned by circuit. There are roughly **50 circuits** (the AOC's
2024 workload assessment counts **51**), and **the count is in flux —
the General Assembly amends § 15-6-1 frequently**, splitting and
adding circuits. **Verify the current circuit for the filing county**
(and the current circuit count) against § 15-6-1 and the
georgiacourts.gov directory rather than relying on a memorized list. A
single-county circuit (e.g., the metro counties) and a multi-county
circuit are administered differently.

### 2. Determine whether the county has a State Court

State Courts exist **only where created by local act**, in **fewer
than half** of the 159 counties. If the county **has** a State Court,
civil actions of any amount (except equity / divorce / title-to-land /
felony) typically file there — see `ga-state-court`. If it **does
not**, those civil actions file in the county's **Superior Court**
instead. **Confirm the county's State Court status** before choosing
the forum.

### 3. Locate the Magistrate Court

Every county has a **Magistrate Court** for small-claims (within the
current O.C.G.A. § 15-10-2(5) cap), dispossessory, and garnishment —
see `ga-magistrate`. Confirm the local Magistrate Court's filing
practices and whether it supplies statement-of-claim forms.

### 4. Identify the e-filing platform (PeachCourt vs. Odyssey eFileGA)

Georgia counties use **two different e-filing systems**, and **which
one a county uses is county-dependent**:

- **PeachCourt** (the eFileGA front end on a Tyler Odyssey backbone) —
  used by many counties.
- **Odyssey eFileGA** (Tyler) — used by other counties.

**Always check the current platform for the filing county** at the AOC
e-filing directory — **https://georgiacourts.gov/efile-court-records**
— before assembling a packet. Civil e-filing is broadly mandatory in
the higher courts statewide (the SB407 mandate, effective around
1/1/2019), but Magistrate e-filing is often **optional**; confirm
both the platform and whether e-filing is mandatory or permissive for
the specific court.

### 5. Pull the local rules and standing orders

In addition to the uniform rules, each circuit (and often each
assigned judge) issues **local rules** and **standing / case-
management orders**. These commonly set chambers-copy thresholds,
proposed-order delivery, ADR-by-default, and scheduling defaults.
**Read the assigned judge's standing order** — per-judge civil
case-management orders are common in the metro circuits and elsewhere.

### 6. Confirm the clerk's filing and fee practices

Filing fees, accepted payment, in-person vs. e-file acceptance for pro
se filers, and proposed-order delivery vary by clerk's office. Confirm
with the **Clerk of Superior Court / State Court / Magistrate Court**
for the county before filing.

## Forum-selection summary (which Georgia court)

| If the claim is… | File in… |
|---|---|
| A civil money/tort claim, any amount, **and the county has a State Court** | **State Court** (`ga-state-court`) |
| A civil money/tort claim where the county has **no** State Court | **Superior Court** (per the county's circuit) |
| Equity, divorce, title to land, or a felony | **Superior Court** (exclusive) |
| A small civil claim within the § 15-10-2(5) cap, dispossessory, or garnishment | **Magistrate Court** (`ga-magistrate`) |

Confirm the subject-matter routing — the State/Superior split is by
**subject, not dollar amount** (see `ga-state-court`).

## Caption — generic county variant

```
        [SUPERIOR | STATE | MAGISTRATE] COURT OF [COUNTY] COUNTY
                          STATE OF GEORGIA

[PLAINTIFF],                        )
                                    )
        Plaintiff,                  )   Civil Action File No. _________
                                    )
v.                                  )
                                    )
[DEFENDANT],                        )
                                    )
        Defendant.                  )

                  [DOCUMENT TITLE IN ALL CAPS]
```

Pick the court line for the chosen forum and the county name for the
filing county; use **"Civil Action File No. ____"**. See
`ga-statewide-format` for the full pleading paper, the numbered-
paragraph body (O.C.G.A. § 9-11-10), the certificate of service, and
the pro se signature block.

**Agent behavior:** before drafting or filing in any non-flagship
county, run the per-county workflow above — (1) the **current circuit
(§ 15-6-1)**, (2) whether the county has a **State Court**, (3) the
**Magistrate Court** practices, (4) the **e-filing platform**
(PeachCourt vs. Odyssey eFileGA, via georgiacourts.gov/efile-court-records),
(5) the **local rules and the assigned judge's standing order**, and
(6) the **clerk's fee/filing practices**. Do not assume a flagship
county's practice carries to another county.

## Composition

- For statewide format and the Georgia caption: `ga-statewide-format`
- For the dedicated flagship venues: `ga-fulton`, `ga-cobb`,
  `ga-gwinnett`
- For the civil-any-amount forum and the Superior/State split:
  `ga-state-court`
- For the small-claims / dispossessory / garnishment forum:
  `ga-magistrate`
- For the answer, defenses, and default avoidance: `ga-first-30-days`
- For discovery practice: `ga-discovery`
- For consumer-debt defenses: `ga-consumer-debt`
- For deadline computation and Georgia legal holidays: `ga-deadlines`
- For assembling and e-filing a packet: `ga-file-packet`
- For citation verification: `ga-fact-check`

## References

- `references/circuit-directory.md` — O.C.G.A. § 15-6-1 judicial
  circuits, the ~50-51 (in-flux) circuit count, and the county-to-
  circuit lookup workflow
- `references/efiling-platforms.md` — PeachCourt vs. Odyssey eFileGA,
  the georgiacourts.gov/efile-court-records directory, and the SB407
  mandatory-e-filing posture
- `references/county-forum-checklist.md` — the per-county research
  workflow (circuit, State Court status, Magistrate Court, local
  rules, clerk practices)
