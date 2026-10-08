---
name: uscis-benefit-requests-codearranger
title: USCIS Benefit Requests — Cover Letters, Evidence Indexes, RFE/NOID Responses
description: 'Use this skill to assemble paperwork for a USCIS benefit request (DHS/USCIS forum adjudicating petitions and applications on papers, NOT immigration court). Drafts cover letter, tabbed evidence index, RFE/NOID responses, expedite letter. Explains initial evidence under 8 CFR § 103.2(b). Triggers: "USCIS cover letter", "I-130", "adjustment of status package", "received an RFE", "respond to RFE", "NOID", "notice of intent to deny", "evidence index", "exhibit list", "I-485 package", "N-400 package", "receipt number". Cardinal rules: **respond by deadline PRINTED ON NOTICE** (never assume days); address every item; **submit ALL evidence at once** — partial response adjudicated as filed (8 CFR § 103.2(b)(11)). Produces documents, not strategy. Composes with immigration-pro-se, immigration-deadlines, and immigration-fact-check.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-immigration-laws/skills/uscis-benefit-requests
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# USCIS Benefit Requests — Cover Letters, Evidence Indexes, RFE/NOID Responses

> **NOT LEGAL ADVICE.** This skill produces drafting aids, checklists, and document
> scaffolds — **not legal advice**, and no attorney-client relationship is created. USCIS
> deadlines (especially RFE / NOID response dates) are unforgiving and a defective filing
> can sink an otherwise approvable case. Verify every form edition, fee, deadline, and
> citation against current USCIS instructions and **strongly consider consulting a licensed
> immigration attorney or an EOIR-accredited representative** before filing.

## USCIS is its own forum — not immigration court

USCIS (within DHS) adjudicates **benefit requests** — petitions and applications — almost
entirely **on the papers**, under **8 CFR § 103.2**. This is a different forum from EOIR
immigration court (removal), the Board of Immigration Appeals, the consulates, and the
circuit courts; see `immigration-pro-se` for the four-forum map. Because USCIS rarely holds
a hearing, **the written package is the case**: what you enclose, how it is organized, and
how completely you answer a request is usually all the adjudicator sees.

A request is "received" on the date USCIS actually receives it at the designated filing
location, paper or electronic (8 CFR § 103.2(b)(7)), and USCIS issues a **receipt notice**
(Form I-797) with a **receipt number** (3 letters + 10 digits). Track it on the USCIS
case-status tool and online account, and **keep a complete copy of everything filed** — you
will need it to respond to any later RFE or NOID.

Common benefit contexts (route substantive eligibility elsewhere — this skill only builds
the paperwork):

| Form | Benefit | Statute |
|---|---|---|
| I-130 | Family petition (relative) | INA § 204 / 8 U.S.C. § 1154 |
| I-140 | Employment-based immigrant petition | INA § 204 / 8 U.S.C. § 1154 |
| I-485 | Adjustment of status to LPR | INA § 245 / 8 U.S.C. § 1255 |
| N-400 | Naturalization | INA §§ 316 / 319 / 8 U.S.C. §§ 1427 / 1430 |

## The cover letter and the evidence index

**Cover letter.** Every package opens with a one- to two-page cover letter that lets the
adjudicator orient instantly. It should state:

- **Petitioner / applicant and beneficiary** by full legal name, with the **A-number**
  (`A2NN-NNN-NNN`) and any prior **receipt number**.
- **The form and the benefit sought** (e.g., "Form I-130, Petition for Alien Relative, on
  behalf of [spouse]") and the classification claimed.
- The **filing fee** enclosed (or fee-waiver request) and the form edition date.
- An **itemized list of enclosures**, keyed to the tabs of the evidence index.
- A signature block (petitioner pro se, or G-28 representative of record).

**Evidence index / exhibit list.** Behind the cover letter, list every supporting document
as a numbered or lettered exhibit (**Tab A, Tab B, …** or **Exhibit 1, 2, …**), with a one-
line description and the physical tab/label that matches the document in the packet. Put
**translations** with a certificate of translation next to each foreign-language original.
A clean, tabbed index is what makes a package easy to approve — and is exactly what you re-
use when responding to an RFE.

**Initial evidence.** USCIS expects the **required initial evidence** for the benefit with
the filing; if it is missing or doesn't demonstrate eligibility, USCIS may deny outright or
issue an RFE (8 CFR § 103.2(b)(1)–(2), (b)(8)(ii)). Build the index against the form
instructions' evidence list so nothing required is omitted.

## Responding to an RFE or a NOID — the cardinal rules

An **RFE** (Request for Evidence) asks for more evidence; a **NOID** (Notice of Intent to
Deny) signals USCIS is inclined to deny and gives a last chance to rebut. Both are governed
by **8 CFR § 103.2(b)(8)**. The rules that decide cases:

1. **Respond by the deadline PRINTED ON THE NOTICE.** Never assume a fixed number of days —
   **read the notice and diary that exact date.** The regulation caps the maximum response
   window (RFE no more than twelve weeks; NOID no more than thirty days) and provides that
   **additional time may not be granted** (§ 103.2(b)(8)(iv)). The notice's own date
   controls; run it through `immigration-deadlines`.
2. **Address every item.** Answer each numbered request point-by-point; an unanswered item
   is treated as not established.
3. **Submit ALL evidence at once.** All requested materials must be filed **together in a
   single response**, along with the **original RFE/NOID notice** on top (§ 103.2(b)(11)).
   A **partial response is adjudicated on the record as filed** — submitting only some of
   the requested evidence "will be considered a request for a decision on the record." There
   is no second bite.
4. **Failing to respond = abandonment.** No timely response means the request "may be
   summarily denied as abandoned, denied based on the record, or both" (§ 103.2(b)(13)).

Structure an RFE/NOID response as: a cover letter re-identifying the case and receipt
number; a copy of the original notice on top; then a **point-by-point response** mirroring
the notice's numbering, each item cross-referenced to a tab in a fresh evidence index.

## Expedite requests

USCIS may, in its discretion, expedite a pending case that meets one of the published
**expedite criteria** (e.g., severe financial loss to a person or company; an emergency or
urgent humanitarian situation; a nonprofit's cultural/social-interest request; a clear
USCIS error; certain government interests). An expedite request is made through the USCIS
contact channels for the pending receipt number and should: identify the case and receipt
number, name the specific criterion invoked, and **attach documentary proof** of the urgency
(it is discretionary — assertion without evidence rarely succeeds). Frame it tightly to the
criterion; do not pad it.

## Artifacts this skill drafts

- **USCIS cover letter** — petitioner/beneficiary, A-number, receipt number, form + benefit
  sought, fee, and an itemized enclosure list.
- **Evidence index / exhibit list** — tabbed (Tab A… or Exhibit 1…), one line per item, with
  translation-certificate placement.
- **RFE response scaffold** — original notice on top + point-by-point answers keyed to a new
  evidence index, built to the deadline on the notice.
- **NOID response scaffold** — rebuttal addressing each stated basis for the proposed denial,
  with all evidence submitted at once.
- **Expedite-request letter** — receipt number, the specific expedite criterion, and the
  proof of urgency attached.

Each artifact ends with the `NOT LEGAL ADVICE` disclaimer.

## Related authority

- **Filing, RFE/NOID, initial evidence, receipt** — **8 CFR § 103.2** (esp. (b)(7) receipt
  date; (b)(8) RFE/NOID + initial evidence; (b)(11) all-evidence-at-once / partial = decision
  on record; (b)(13) failure to respond):
  [`../../references/immigration-regulations/8CFR-103-powers-fees.md`](../../references/immigration-regulations/8CFR-103-powers-fees.md).
- **Immigrant petitions (I-130 / I-140)** — **8 CFR Part 204**:
  [`../../references/immigration-regulations/8CFR-204-immigrant-petitions.md`](../../references/immigration-regulations/8CFR-204-immigrant-petitions.md).
- **Adjustment of status (I-485)** — **8 CFR Part 245**:
  [`../../references/immigration-regulations/8CFR-245-adjustment.md`](../../references/immigration-regulations/8CFR-245-adjustment.md).
- **INA substance** — Subchapter II (petitions § 204, adjustment § 245):
  [`../../references/immigration-statutes/INA-II-immigration.md`](../../references/immigration-statutes/INA-II-immigration.md),
  with the INA ↔ 8 U.S.C. crosswalk in
  [`../../references/immigration-statutes/README.md`](../../references/immigration-statutes/README.md)
  (cite by the crosswalk, not from memory).

## Composition

- Start with `immigration-pro-se` to confirm USCIS is the right forum and to capture the
  A-number / receipt number.
- Run every RFE / NOID deadline through `immigration-deadlines` — the date on the notice
  controls and cannot be extended.
- Pull the underlying file (A-file / receipt-history) via `immigration-foia` before
  responding to an RFE or NOID.
- Verify every citation and form edition a draft makes with `immigration-fact-check`.
