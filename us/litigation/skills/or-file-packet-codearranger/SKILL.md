---
name: or-file-packet-codearranger
title: Assemble an Oregon Court Filing Packet
description: Use this skill when the user is ready to assemble and file a complete Oregon court motion packet. Triggers include "assemble the packet", "I'm ready to file", "put together the filing", "finalize the motion for filing", "prepare the packet", "what goes in the packet", "organize the filing". Verifies that every required component is present (motion, declaration, exhibits, proposed order, Notice of Hearing, Certificate of Service), checks caption consistency across documents, confirms service lists match the parties, and produces filing instructions for OJD File and Serve. For Multnomah and Washington County, enforces working-copy preflight per the local SLR. Composes with `or-quality-check`, `or-fact-check`, `or-schedule-hearing`, and the draft-* skills.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-file-packet
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Assemble an Oregon Court Filing Packet

Gather and organize all documents required for a complete
Oregon civil filing: motion, supporting declaration, exhibits,
proposed order, Notice of Hearing, and Certificate of Service.

> **NOT LEGAL ADVICE.** This skill is a procedural and drafting
> aid, not legal advice. Verify current rules, deadlines, and
> venue-specific practices before filing. Pair with substantive
> review by counsel where stakes warrant.

## Standard packet for a noted civil motion

| # | Document | Skill |
|---|----------|-------|
| 1 | Motion + Memorandum | `or-draft-motion` |
| 2 | Supporting Declaration(s) with exhibits | `or-draft-declaration` |
| 3 | Proposed Order ("[PROPOSED]" in title) | `or-draft-order` |
| 4 | Notice of Hearing | `or-draft-note` |
| 5 | Certificate of Service | UTCR 1.090 |

Optionally:
- **Working copies** (Multnomah SLR 5.100, Washington Co SLR
  5.100 — over threshold pages) — paper packet delivered to
  chambers
- **Application for Fee Waiver** (ORS 21.682) if filing fees
  cannot be paid

## Step-by-step

### Step 1: Reserve the hearing date

Per the court's procedure (see `or-schedule-hearing`).

### Step 2: Draft each document

For each document, use the relevant draft-* skill:

- Motion + Memorandum → `or-draft-motion`
- Declaration → `or-draft-declaration`
- Proposed Order → `or-draft-order`
- Notice of Hearing → `or-draft-note`

### Step 3: Run Quality Check

Run `or-quality-check` against each document:

- UTCR 2.010 format compliance
- pro-se drafting framework content checks
- Citation format

Fix any FAILs before proceeding.

### Step 4: Run Fact Check

Run `or-fact-check` against the entire packet:

- Citation verification
- Internal consistency (within each document)
- Packet consistency (across documents)
- Sworn-vs.-argued consistency

Fix any FAILs before proceeding.

### Step 5: Preflight checklist

Before filing, verify:

#### Captions

- [ ] All five documents use **identical** court header
- [ ] All five documents have the **same case number**
- [ ] All five documents have the **same party names in the
      same order**
- [ ] Document titles match what's actually in the body

#### Hearing details (across motion, Notice of Hearing,
proposed order)

- [ ] **Date** matches
- [ ] **Time** matches
- [ ] **Mode** (in-person / WebEx) matches
- [ ] **Courtroom or connection info** matches
- [ ] **Assigned judge** matches

#### Service

- [ ] Certificate of Service in each document (or as a
      separate document)
- [ ] All parties identified by full name and address (or
      email)
- [ ] Method of service identified

#### Exhibits

- [ ] All exhibits referenced in the motion or declaration
      are present
- [ ] Exhibit numbering is sequential and consistent
- [ ] Cover pages and Exhibit List present in the
      declaration

#### File and Serve readiness

- [ ] Each document is in PDF format
- [ ] Each document is under 25 MB (or split if larger)
- [ ] Document codes selected matching UTCR 2.110 titles
- [ ] Filing fees identified (or fee-waiver application
      attached)

#### Signature

- [ ] Signature block on each document
- [ ] Date is filled in (or fill-in blanks for handwritten
      date)
- [ ] OSB# if counsel; omitted if pro se

#### Confidential information (UTCR 2.120)

- [ ] SSN redacted (last 4 only)
- [ ] Account numbers redacted (last 4 only)
- [ ] Minor children referenced by initials
- [ ] DOB redacted (year only for adults)

### Step 6: File via File and Serve

#### Sequence

In Multnomah, file each document separately with its own
document code. The order:

1. Motion + Memorandum — "Motion (Other)" or specific code
2. Supporting Declaration — "Declaration of [Name]"
3. Proposed Order — "Order — Proposed"
4. Notice of Hearing — "Notice of Hearing"
5. Certificate of Service — "Certificate of Service" (or
   included as page of each filed document)

#### Document codes

Pick from the File and Serve dropdown matching the UTCR 2.110
title. If no exact match, use the closest available; some
codes are:

- Motion (Other)
- Motion to Compel
- Motion to Dismiss
- Motion for Summary Judgment
- Motion to Vacate
- Memorandum in Support of Motion
- Declaration of [Name]
- Order — Proposed
- Notice of Hearing
- Certificate of Service

#### Fees

Pay or apply for waiver at submission. Filing fees:

| Filing | Fee (approximate) |
|--------|-------------------|
| Motion (most types) | ~$11 |
| Order — Proposed | $0 (no fee for proposed order) |
| Notice of Hearing | $0 |
| Declaration | $0 |

Verify against https://www.courts.oregon.gov/services/fees/.

### Step 7: Working copies (if required)

For Multnomah (over 25 pages total) or Washington Co (over 15
pages total):

- Print one complete packet (motion + memo + decl + exhibits +
  proposed order)
- Tab each document on its own tab
- Bind (binder clip, staple, or perfect bind)
- Add a cover with case caption, hearing date, judge name,
  and a short index of what's enclosed

Deliver:

- **Multnomah**: Mail room (loading dock) at 1200 SW 1st Ave,
  Portland; addressed to "Hon. [Judge Name], c/o [JA Name]"
- **Washington Co**: Civil Division counter, 2nd floor, 145
  NE 2nd Ave, Hillsboro
- Verify per-judge variations from the standing order

### Step 8: Serve under ORCP 9 / UTCR 21.100

- **eService through File and Serve**: for registered parties,
  service is automatic upon filing
- **Email**: for parties consenting in writing
- **Mail**: USPS first-class for non-registered parties
- **Hand delivery**: optional

Certificate of Service (UTCR 1.090) documents the service.

### Step 9: Calendar deadlines and hearing date

- Hearing date — calendar with reminders at 7, 3, and 1 day
  out (see `or-hearings/references/hearing-day-checklist.md`)
- Response deadline (if waiting for opposing party's
  response)
- Reply deadline (if you'll reply to opposing's response)

## Common packet errors

| Error | Consequence |
|-------|-------------|
| Caption discrepancy between motion and proposed order | Court rejects; refile |
| Hearing date mismatch between Notice and motion | Hearing falls off calendar |
| Missing Certificate of Service | UTCR 1.090 violation; clerk rejects |
| Exhibit numbering mismatch | Confused record; sanctions risk |
| Notice of Hearing filed before JA confirms date | Hearing date may be rejected |
| Filing fee not paid (and no fee-waiver applied) | Filing not accepted |
| Document over 25 MB | Upload fails |
| Wrong document code in File and Serve | Filing mis-indexed; may delay |
| Working copies not delivered when required | Judge sees incomplete record |
| Caption uses "vs." instead of "v." | Cosmetic but unprofessional |

## After filing

- **Confirm acceptance** within 1–2 business days (File and
  Serve sends email)
- **If rejected**, fix and re-file before any deadline
- **Update the calendar** with the hearing date and any
  intermediate deadlines
- **Track opposing's response** — if no response by the
  deadline, the motion is unopposed (judges may rule on the
  papers)
- **Prepare for the hearing** (see `or-hearings`)

## Pro se packet considerations

A pro se filer's packet is judged by the same standard as
counsel's. Common pro se shortcuts to avoid:

- Combining motion + declaration into one document (file
  separately)
- Skipping the Notice of Hearing (most courts require it)
- Lettered exhibits (use numbers in Oregon)
- Static page numbers in the footer (use PAGE / NUMPAGES
  Word fields)
- Forgetting the proposed order (judges expect one)
- No working copies for Multnomah over-25-page motions

## Companion skills

Run before assembling packet:
- `or-statewide-format` — formatting baseline
- `or-pro-se` — pro-se drafting framework
- The relevant draft-* skills

Run during packet assembly:
- `or-quality-check` — format pass
- `or-fact-check` — substantive pass

Run after filing:
- `or-hearings` — prep for the hearing

## Cross-references

- All draft-* skills — the individual documents
- `or-quality-check` — format pass
- `or-fact-check` — substantive pass
- `or-schedule-hearing` — reserving the date (prerequisite)
- `or-hearings` — preparing for the hearing (next step)
- `or-statewide-format/references/templates/` — the four
  primary templates
