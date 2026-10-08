---
name: in-marion-codearranger
title: Marion Superior Court — Indianapolis (Indiana's Highest-Volume Civil Trial Court)
description: 'Use for Marion Superior Court (Indianapolis) — Indiana''s largest civil court. Covers the **36-courtroom configuration** (Civil, Criminal, Probate, Juvenile, Domestic Relations divisions), **random case assignment** to Civil courtrooms, **Marion County Local Rules (LR49)**, **Civil Pretrial Practice & Procedure (CPC)** case management, **township small-claims courts (IC 33-34)**, and **Odyssey e-filing** at the City-County Building. Triggers: "Marion Superior", "Marion Civil Division", "LR49-TR", "Civil Pretrial Practice", "Marion small claims".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-marion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Marion Superior Court — Indianapolis (Indiana's Highest-Volume Civil Trial Court)

Marion Superior Court is Indiana's busiest trial court — the
combined Marion Superior Court (a court of general and unified
jurisdiction under IC 33-33-49) sits in Indianapolis and handles
the largest civil docket in the state. The court's 36 numbered
courtrooms are divided across five divisions:

- **Civil Division** (Courtrooms 1-14): general civil, contract,
  tort, replevin, declaratory, debt-collection actions
- **Criminal Division** (Courtrooms 15-23): felony and high-level
  misdemeanor cases
- **Probate Division** (Courtrooms 24-29): estates, trusts,
  guardianships, adoptions
- **Juvenile Division** (Courtrooms 30-33): delinquency and CHINS
  cases
- **Domestic Relations Division** (Courtrooms D01-D08): divorce,
  custody, paternity, support (separate sub-numbering)

The Civil Division operates from the **City-County Building** at
200 East Washington Street, Indianapolis, IN 46204. The Marion
Circuit Court (separately constituted under IC 33-33-49-9) also
sits in the City-County Building.

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify against current Marion County Local Rules and the
> assigned courtroom's chambers practice before filing.

## Case assignment — random rotation

When a civil complaint is filed through Odyssey, the system
randomly assigns the case to one of the 14 Civil Division
courtrooms by the next available rotation slot. The cause number
encodes the assigned courtroom:

`49D01-2503-PL-001234`

Parsing:
- `49` — Marion County
- `D01` — Superior Court, Division 1 (Civil Courtroom 1)
- `2503` — March 2025 filing
- `PL` — Plaintiff (case type: civil plenary)
- `001234` — sequence number

Common Marion case-type codes:

| Code | Case type | Use |
|------|-----------|-----|
| `PL` | Plenary (civil) | General civil action over $10,000 |
| `CC` | Civil Collection | Debt-collection action |
| `CT` | Civil Tort | Personal injury, property damage |
| `MF` | Mortgage Foreclosure | Real-estate foreclosure |
| `DN` | Domestic Without Children | Dissolution without minor children |
| `DR` | Domestic Relations | Dissolution with children, custody |
| `MI` | Miscellaneous | Special-statute proceedings (e.g., name change) |
| `SC` | Small Claims | Filed in a township small-claims court |
| `EU` | Estate Unsupervised | Unsupervised probate estate |

The case-type code drives the Odyssey filing form, the document
codes available, and the assigned division.

## Marion County Local Rules (LR49)

Marion adopts local rules with the prefix `LR49` (49 is the Marion
County code in the Indiana judicial numbering scheme). The local
rules supplement, but do not supplant, the Indiana Trial Rules.

| Rule | Subject |
|------|---------|
| LR49-TR3.1 | Appearance form (Indiana Trial Rule 3.1 appearance) |
| LR49-TR5-203 | Format of documents — paper copy / chambers copy |
| LR49-TR5(F) | Confidentiality designations under Indiana Administrative Rule 9 |
| LR49-TR16 | Pretrial conferences (Civil Division case management) |
| LR49-TR45 | Subpoenas — chambers copy requirements |
| LR49-TR53.5 | Continuances |
| LR49-TR79 | Special judges |
| LR49-AR15 | Drug Court (criminal only) |
| LR49-FL00 | Domestic Relations Division standing orders |

The full LR49 set is available at the Marion Superior Court
website (`indy.gov/agency/marion-superior-court`) and via the
Indiana Supreme Court's local-rules portal.

## Civil Pretrial Practice and Procedure (CPC)

Marion Superior Civil Division publishes a court-wide **Civil
Pretrial Practice and Procedure** (CPC) manual that sets out
case-management standards across all 14 Civil Division courtrooms.
Key points:

- **Initial CMS (Case Management Statement)**: due within 60 days
  of issue being joined; uses the Marion CMS form (a 2-page form
  available on the court website and through Odyssey templates).
- **Discovery limits**: T.R. 33(A) caps interrogatories at 25
  (counting subparts as separate interrogatories); Marion CPC
  Section IV.B encourages parties to agree to a higher cap via
  written stipulation rather than seeking leave.
- **Motion practice**: every motion must be accompanied by a
  proposed order. The court will not rule without a proposed
  order in the filing.
- **Status conferences**: every Civil Division courtroom holds
  routine status conferences at 90-day intervals; attendance is
  by telephone unless the courtroom has set the conference in
  person.
- **Trial-setting**: trials are set by court order following the
  CMS conference; parties may not unilaterally set a trial date.

Always check the assigned courtroom's chambers practice page
(typically posted on `indy.gov` under "Marion Superior Court →
Courtrooms → [Number]") before filing — courtroom-specific
preferences vary (e.g., page limits on memoranda, chambers copy
requirements, courtesy copy delivery method).

## Chambers copies — when and how

Marion Civil Division requires a paper chambers copy for any
filing exceeding **15 pages** (LR49-TR5-203(d)). The chambers
copy must be:

- Stapled in the upper-left corner (no binding clips, no spiral
  binding)
- Three-hole punched on the left margin
- Delivered to the assigned courtroom's chambers within 24 hours
  of e-filing
- Marked "CHAMBERS COPY" on the first page in red ink or red
  highlighter

Some Civil Division courtrooms (notably Courtrooms 5 and 11 as of
recent practice) accept a courtesy PDF emailed directly to the
court reporter or judicial assistant in lieu of the paper
chambers copy. Confirm the courtroom-specific preference before
relying on the email option.

## E-filing — Odyssey

Marion mandated Odyssey e-filing for civil cases in December
2016 — the first county statewide. All civil filings (except
sealed and confidential petitions falling under Indiana
Administrative Rule 9) must be submitted via the Indiana E-Filing
System at https://efile.courts.in.gov.

Practical tips:

- Self-represented filers may register a free Odyssey account and
  e-file; see `in-pro-se` for the step-by-step.
- Filing fees: Marion's civil filing fee for a PL case is the
  statewide schedule under IC 33-37-4-4 plus the Marion county
  cost ($177 base + county costs as of 2024; verify on the
  Marion Clerk's fee schedule).
- Document codes: match the document title closely. "Motion to
  Dismiss" maps to document code 11020; "Memorandum in Support"
  maps to 11250; "Proposed Order" maps to 12000. The Odyssey UI
  is the canonical source; codes are updated quarterly.
- Filing deadline: Odyssey accepts filings until 11:59 PM local
  time on the deadline day; the file-stamp is automatic.

## Marion County Small Claims Courts (IC 33-34)

The **Marion County Small Claims Courts** are constitutionally
distinct from Marion Superior Court. They are nine **township**
small-claims courts (one per township in Marion County), each
with a single elected judge:

- Center Township Small Claims Court
- Decatur Township Small Claims Court
- Franklin Township Small Claims Court
- Lawrence Township Small Claims Court
- Perry Township Small Claims Court
- Pike Township Small Claims Court
- Warren Township Small Claims Court
- Washington Township Small Claims Court
- Wayne Township Small Claims Court

Jurisdiction is governed by IC 33-34-3 — civil claims **up to
$8,000** (compared to the $10,000 cap in Superior Court small-
claims dockets in other counties under IC 33-29-2-4). Venue rests
in the township where the claim arose, where the defendant
resides, or where the act giving rise to the claim occurred.

The Marion township small-claims courts adopted **Marion Small
Claims Manual** rules in addition to the Indiana Small Claims
Rules. Procedure highlights:

- No pleadings filing requirement beyond the Notice of Claim
  (small-claims complaint)
- Trial is bench-only; jury is not available
- Discovery is limited; parties must seek leave for written
  discovery
- A losing party may move for trial de novo in Marion Superior
  Court Civil Division within 60 days of judgment under IC
  33-34-9-1

For claims over $8,000, file in Marion Superior Court Civil
Division using a PL or CC case-type code rather than SC.

## Pretrial timeline — Marion Civil Division (typical case)

```
Day 0      Complaint filed; cause number assigned; courtroom rotated
Day 20     Answer due (T.R. 6(C)); appearance filed (LR49-TR3.1)
Day 30     Defendant's affirmative defenses fully pleaded
Day 60     Joint CMS or unilateral CMS filed
Day 90     First status / CMS conference
Day 180    Initial discovery completed (typical)
Day 300    Dispositive motions filed
Day 360    Pretrial conference
Day 420    Trial setting
```

The timeline varies courtroom-to-courtroom; the table reflects
the Marion CPC default for an ordinary civil case.

## Composition — which skills layer here

- `in-statewide-format` for T.R. 5(E) / T.R. 10 baseline
- `in-pro-se` for self-represented filing in Marion (a
  significant share of Marion small-claims filers are pro se)
- `in-discovery` for T.R. 26-37 + Marion CMS interactions
- `in-deadlines` for T.R. 6 deadline math with Marion / Indiana
  legal holidays
- `in-schedule-hearing` for Marion-specific hearing setting
- `in-consumer-debt` if the case is a debt-collection action

## References

- `references/lr49-summary.md` — concise summary of every LR49
  rule
- `references/civil-pretrial-practice.md` — Marion CPC manual
  summary
- `references/township-small-claims.md` — the nine township
  courts with addresses and chambers contacts
- `references/marion-cause-numbers.md` — the cause-number
  parsing table

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current local rules and case law before filing.
