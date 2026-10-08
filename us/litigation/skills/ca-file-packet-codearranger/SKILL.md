---
name: ca-file-packet-codearranger
title: Assemble a California Court Filing Packet
description: Use when assembling and filing a complete California superior court motion packet. Triggers include "assemble my packet", "what do I need to file in LASC", "what goes in my motion packet", "California e-filing", "Odyssey eFileCA", "File and ServeXpress", "memorandum page limit California", "CRC 3.1113", "separate statement", "filing fee California", "fee waiver FW-001", "FW-003 Order on Court Fee Waiver". Verifies every required component, enforces cross-document consistency, applies CRC 2.100-2.119 format gates, checks the CCP § 1005(b) court-day service deadlines, and produces a filing instruction sheet for the specific court (LASC, SFSC, or county per `ca-county-courts`). Layers on top of `ca-statewide-format`, `ca-draft-motion`, `ca-draft-note`, `ca-draft-declaration`, `ca-draft-order`, `ca-quality-check`, and the venue-specific skill.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-file-packet
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Assemble a California Court Filing Packet

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify against current rules and case law before filing.

## When to use

When a user has all (or nearly all) of the drafting components
ready and needs to (a) confirm the packet is complete, (b)
enforce cross-document consistency, (c) compute the filing-
service deadlines under CCP § 1005(b), and (d) follow the
court-specific e-filing procedure.

If the user is still drafting components, use `ca-draft-motion`,
`ca-draft-declaration`, `ca-draft-note`, or `ca-draft-order`
first.

## Packet components (motion practice)

For a typical noticed civil motion in California (not ex parte,
not a summary-judgment motion — those have additional
requirements), the packet contains:

| Component | Authority | Notes |
|---|---|---|
| **Notice of Motion** | Code Civ. Proc., § 1010 | **Separate document** from the memorandum (CA convention). Identifies date, time, department, courthouse, nature of motion, grounds, and supporting papers. |
| **Memorandum of Points and Authorities** | Cal. Rules of Court, rule 3.1113 | Max **15 pages** under rule 3.1113(d); 20 with leave. Table of contents + table of authorities required if over 10 pages (rule 3.1113(f)). |
| **Separate Statement** | Cal. Rules of Court, rule 3.1345 | **REQUIRED** for motions to compel further responses (interrogatories, RFPs, RFAs), motions for summary judgment / adjudication, and certain other motions. Lists each disputed item, the response, and the reason for compelling. |
| **Declaration(s)** | Code Civ. Proc., § 2015.5 | Penalty-of-perjury attestation under California law; must include **date AND place of execution**. Authenticates exhibits. Meet-and-confer declaration if required. |
| **Request for Judicial Notice** | Cal. Evid. Code, §§ 452-453 | If asking the court to take judicial notice of court records, statutes, public records, etc. |
| **Proposed Order** | Cal. Rules of Court, rule 3.1312 | **Separate document**. Title typically begins "[PROPOSED] ORDER…". |
| **Proof of Service** | Cal. Rules of Court, rule 1.21; CCP § 1013(a)-(c), § 1010.6 | Judicial Council form POS-040 (general) or POS-030 (by mail); or CCP § 1013a declaration. |

## Page limits — CRC 3.1113

- Default memorandum max: **15 pages** (rule 3.1113(d)).
- Summary judgment / adjudication memorandum max: **20 pages**
  (rule 3.1113(d)).
- Application for permission to file longer brief: required;
  filed and served at least 24 hours before due date.
- Table of contents + table of authorities required if memo
  exceeds 10 pages (rule 3.1113(f)).
- Page-limit calculation does NOT include caption page, tables,
  signature blocks, exhibits, declarations, separate statement,
  or proposed order.

## Format gate (CRC 2.100-2.119)

Before assembly, run the `ca-statewide-format` checks on each
component:

- Letter paper, 8.5" × 11" (CRC 2.104)
- White, opaque, unglazed paper (CRC 2.103) — recyclable
- One side only (CRC 2.103)
- 1" margins on all sides (CRC 2.107)
- 12-point font, essentially equivalent to Courier, Times New
  Roman, or Arial (CRC 2.104, 2.105)
- 1.5- or double-spaced (CRC 2.108(a))
- Line numbering in the left margin (CRC 2.108(b))
- Black ink only (CRC 2.103) — stricter than OR / WA
- Two-hole punch at top (CRC 2.119)
- Footer with title of paper + page number (CRC 2.110)

For e-filed documents, the paper-physical requirements (hole
punch, paper color) are advisory only; the court applies them
to printed working copies and chambers copies.

## Service timing — CCP § 1005(b)

California uses **court days** (not calendar days) for motion
notice. Backwards-from-hearing arithmetic:

| Period | Days | Counting basis |
|---|---|---|
| Notice of motion served by | -16 court days | from hearing |
| Add for in-state mail | +5 calendar days | CCP § 1013(a) |
| Add for e-service | +2 court days | CCP § 1010.6(a)(3)(B) |
| Add for fax or express mail | +2 court days | CCP § 1013(c), (d) |
| Add for out-of-state mail | +10 calendar days | CCP § 1013(a) |
| Opposition due | -9 court days | from hearing |
| Reply due | -5 court days | from hearing |

A court day = Monday-Friday excluding judicial holidays (CCP
§ 12c, § 135). Use `scripts/case-calendar.py --rule
motion-notice-min` (and related rules) to compute concrete
dates.

**Always reserve the hearing date BEFORE serving the notice** in
LASC, SFSC, and most other counties. See `ca-schedule-hearing`.

## E-filing (mandatory in most CA courts)

Cal. Rules of Court 2.250-2.261 govern. Mandatory for
represented parties in most superior courts; varies for pro per.

### Court-by-court e-filing systems

| Court | System | Portal |
|---|---|---|
| LASC | Odyssey eFileCA (Tyler) | efilingsupport.lacourt.org |
| SFSC | File and ServeXpress | sfsuperiorcourt.org/efiling |
| Orange County | Civil eFile (One Legal / various vendors) | occourts.org |
| San Diego County | Odyssey eFileCA (Tyler) | sdcourt.ca.gov |
| Santa Clara County | Odyssey eFileCA (Tyler) | scscourt.org |
| Alameda County | Odyssey eFileCA (Tyler) | alameda.courts.ca.gov |
| Sacramento County | One Legal / multiple | saccourt.ca.gov |
| Other counties | Varies | Check the court's website |

### PDF requirements (CRC 2.256, 2.257)

- Text-searchable (OCR if scanned).
- Bookmarked for any document with 25+ pages of exhibits (CRC
  3.1110(f)(4)) — each exhibit gets its own bookmark.
- File names per court convention; some courts require a
  document-code in the name.
- Stamped pages where required.

## Filing fees (Gov. Code, §§ 70611, 70617)

| Filing | Fee (approximate) | Authority |
|---|---|---|
| Unlimited civil first appearance | $435 | Gov. Code, § 70611 |
| Limited civil first appearance (≤ $25K) | $370 | Gov. Code, § 70613 |
| Motion (non-paper subsequent appearance) | $60 | Gov. Code, § 70617 |
| Demurrer / motion to strike (post-answer) | $60 | Gov. Code, § 70617 |
| Stipulated abstract | $25 | Various |

**Verify current fee against the court's published schedule** —
filing fees are adjusted periodically.

### Fee waiver

- Judicial Council Form **FW-001** (Request to Waive Court Fees)
  — for the litigant.
- Judicial Council Form **FW-003** (Order on Court Fee Waiver) —
  for the court.
- Statutory authority: Gov. Code, §§ 68630-68641.
- Eligibility: (a) receipt of public benefits; (b) household
  income at or below 125% of federal poverty guidelines; (c)
  cannot afford fees + basic necessities.

## Cross-document consistency checks

Before submission, verify:

- [ ] Caption (court, county, case number, parties) matches
      across every document
- [ ] Document title in caption matches document title in
      footer (CRC 2.110)
- [ ] Hearing date / time / department consistent across
      Notice of Motion, memorandum, and proposed order
- [ ] All exhibits referenced in declarations are attached
- [ ] All declarations referenced in memorandum are filed with
      the packet
- [ ] Proof of Service lists every document served
- [ ] Separate Statement (if required) addresses every disputed
      item from the motion
- [ ] Page count of memorandum within CRC 3.1113 limit
- [ ] Memorandum has table of contents + table of authorities
      if over 10 pages
- [ ] Penalty-of-perjury attestation in every declaration
      includes **date AND place of execution** (CCP § 2015.5)
- [ ] Notice of Motion includes the full CCP § 1010 elements

## Output

When asked to assemble a packet, produce:

1. **Packet manifest** — numbered list of documents with file
   names suitable for e-filing.
2. **Filing instructions** — court-specific portal, login,
   docket category, and filing fee.
3. **Service instructions** — list of parties + service method
   + computed deadlines (with `case-calendar.py` output where
   relevant).
4. **Pre-filing checklist** — the cross-document consistency
   checks above, marked off.
5. **Working-copy / chambers-copy requirements** — many CA
   judges require a paper working copy hand-delivered to
   chambers; verify per the department.

## Common pitfalls

- Combining the Notice of Motion and Memorandum into a single
  document — CA convention separates them.
- Exceeding the 15-page memorandum limit without leave (rule
  3.1113(d)).
- Omitting the table of contents + table of authorities on a
  memo over 10 pages (rule 3.1113(f)).
- Forgetting the Separate Statement on a motion to compel
  further or summary judgment motion (rule 3.1345).
- Filing a declaration that omits the place of execution
  (CCP § 2015.5).
- Computing service deadlines in calendar days when CCP
  § 1005(b) requires court days.
- Serving the notice before reserving the hearing date —
  many CA departments require reservation first.
- Importing Oregon's "File and Serve" (OJD) procedure or
  Washington's KCDC/KCSC portals — California uses different
  systems per county.

## Cross-references

- `ca-statewide-format` — format compliance baseline
- `ca-draft-motion` / `-declaration` / `-note` / `-order` —
  individual component scaffolders
- `ca-quality-check` — pre-filing QC pass
- `ca-schedule-hearing` — reservation protocol
- `ca-lasc` / `ca-sfsc` / `ca-county-courts` — venue-specific
  filing systems and local rules
- `ca-deadlines` — CCP § 1005(b) service-deadline computation
- `ca-discovery` — separate-statement requirements for
  discovery motions
- `scripts/case-calendar.py` — concrete deadline arithmetic
- `scripts/format-check.py` — CRC 2.100-2.119 docx checker
