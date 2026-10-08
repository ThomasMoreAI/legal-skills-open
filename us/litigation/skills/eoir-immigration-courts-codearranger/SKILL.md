---
name: eoir-immigration-courts-codearranger
title: EOIR — The Immigration Courts and Their Rules
description: 'Use this skill to understand the EOIR immigration-court system and filing rules — the structural/formatting anchor for every EOIR filing. Covers the Executive Office for Immigration Review (EOIR): ~70 courts, immigration judges, Board of Immigration Appeals, jurisdiction, venue, change of venue, master-calendar vs. individual-calendar hearings, and the procedural authority (8 CFR Parts 1003/1240/1208 binding regulations + ICPM/BIA Practice Manual guidance). Triggers: "immigration court rules", "ICPM", "how do I file in immigration court", "EOIR filing format", "ECAS", "eFiling", "master calendar hearing", "change of venue", "page limits immigration court", "proof of service EOIR", "cover page", "which immigration court". Produces filing checklists, caption/cover-page/service scaffold, venue worksheets. Composes with eoir-removal-defense, bia-appeals, and immigration-fact-check.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-immigration-laws/skills/eoir-immigration-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# EOIR — The Immigration Courts and Their Rules

> **NOT LEGAL ADVICE.** Drafting aids and checklists only — not legal advice, no
> attorney-client relationship. The practice-manual conventions below change; confirm the
> current Immigration Court Practice Manual and the controlling 8 CFR provision, and check
> your specific court's standing orders, before filing.

## The court system in one page

The **Executive Office for Immigration Review (EOIR)** is part of the **Department of
Justice** — *not* DHS. DHS (through ICE counsel) is the **opposing party** in removal
proceedings; EOIR is the neutral adjudicator. Structure:

- **Immigration courts (~70 nationwide)**, supervised by the **Office of the Chief
  Immigration Judge (OCIJ)**. Each court has one or more **Immigration Judges (IJs)**;
  larger courts have an **Assistant Chief Immigration Judge (ACIJ)**.
- The **Board of Immigration Appeals (BIA)** — the single, nationwide appellate body that
  reviews IJ decisions (see `bia-appeals`).
- Appeals from the BIA go to the **U.S. Court of Appeals** for the circuit where the
  immigration court sat (see `circuit-petition-for-review`).

A removal case is filed when DHS files a **Notice to Appear (NTA, Form I-862)** with an
immigration court. Venue is the court where the NTA is filed; it can be moved (below).

## Two layers of procedural authority — cite the right one

| Layer | What it is | Where |
|---|---|---|
| **Binding regulations (LAW)** | 8 CFR **Part 1003** (EOIR, the Board, IJ proceedings, motions), **Part 1240** (removal proceedings), **Part 1208** (asylum before EOIR) | Verbatim in [`../../references/immigration-regulations/`](../../references/immigration-regulations/) |
| **Practice manuals (guidance)** | **Immigration Court Practice Manual (ICPM)** and **BIA Practice Manual (BIAPM)** — filing format, page limits, deadlines, e-filing | [`../../references/court-rules/`](../../references/court-rules/) (pointer stubs + canonical URLs) |

**Rule of thumb:** cite the **8 CFR regulation** for anything jurisdictional or substantive
(e.g., the IJ's authority, motion standards, the appeal right); use the **practice manual**
only for mechanics (format, tabs, page limits, service). Never rely on the manual where a
regulation governs.

## Hearings — master calendar vs. individual

- **Master calendar hearing (MCH).** Short, often high-volume scheduling/pleading hearing.
  The respondent **pleads to the NTA** (admits/denies the factual allegations, concedes or
  contests the charge(s) of removability) and **designates relief** sought. See
  `eoir-removal-defense` for the pleading mechanics.
- **Individual / merits hearing.** The evidentiary hearing on the application(s) for relief
  — testimony, exhibits, witnesses. Filing deadlines (the "call-up" / submission deadline
  set by the IJ or the ICPM default) are firm; late exhibits can be refused.

## Filing format — the conventions EOIR expects

The ICPM sets the format. Confirm current specifics in
[`../../references/court-rules/Immigration-Court-Practice-Manual.md`](../../references/court-rules/Immigration-Court-Practice-Manual.md);
the durable conventions a filing should follow:

- **Cover page / caption** identifying the respondent by full name and **A-number**, the
  immigration court (city), the IJ if assigned, the proceeding type, and the next hearing
  date.
- **A signed proof / certificate of service** on the opposing party — **DHS/ICE Office of
  the Principal Legal Advisor (OPLA)** counsel for that court — for every filing.
- **Exhibits tabbed and labeled** (alphabetical for the respondent; numeric for DHS), with
  a table of contents and consecutive pagination; a proposed-order / cover where required.
- **Page limits and the "call-up" filing deadline** per the ICPM / the IJ's standing order.
- **A certificate of translation** for any non-English document.
- **E-filing through ECAS** (EOIR Courts & Appeals System) where the court is on ECAS;
  paper filing otherwise. A self-represented respondent registers for an ECAS pro-se
  account or files paper.

Use the `eoir-immigration-courts` cover-page + proof-of-service scaffold below; the
substantive motion bodies come from `eoir-removal-defense` / `eoir-motions-to-reopen-reconsider`.

## Venue and change of venue

Venue is the court where DHS filed the NTA. A **motion to change venue** (decided under the
8 CFR Part 1003 framework and the ICPM) is filed when the respondent has moved or for
convenience-of-the-parties reasons; it typically requires pleading to the NTA and stating
a fixed address in the new location. Route the motion through `eoir-removal-defense`.

## Artifacts this skill drafts

- A **filing-format checklist** (cover page, caption, service on OPLA, tabbed exhibits,
  page limits, translation certificate, ECAS vs. paper).
- A **cover-page + caption + certificate-of-service scaffold** for an immigration-court filing.
- A **venue / change-of-venue worksheet**.

## Related authority

- **8 CFR Part 1003** (EOIR / BIA / IJ proceedings) —
  [`../../references/immigration-regulations/8CFR-1003-eoir-bia.md`](../../references/immigration-regulations/8CFR-1003-eoir-bia.md);
  **Part 1240** (removal) — [`8CFR-1240-removal-eoir.md`](../../references/immigration-regulations/8CFR-1240-removal-eoir.md);
  **Part 1208** (asylum) — [`8CFR-1208-asylum-eoir.md`](../../references/immigration-regulations/8CFR-1208-asylum-eoir.md).
- **ICPM + BIA Practice Manual** — [`../../references/court-rules/`](../../references/court-rules/).
- Removal-proceeding statute: **INA § 240 / 8 U.S.C. § 1229a** (see the statutes corpus crosswalk).

## Composition

The structural/format anchor for EOIR work. `eoir-removal-defense`,
`eoir-motions-to-reopen-reconsider`, and `bia-appeals` supply the substantive filings;
`immigration-deadlines` supplies the clocks; `immigration-fact-check` verifies citations.
