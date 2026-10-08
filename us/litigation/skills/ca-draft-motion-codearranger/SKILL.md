---
name: ca-draft-motion-codearranger
title: Draft a California Motion Packet
description: Use this skill when the user asks to draft a motion for a California superior court. Triggers include "draft a California motion", "write a motion to compel", "I need to file a demurrer", "motion for summary judgment California", "anti-SLAPP motion", "motion to strike California", "motion to quash service", "16 court days notice", "memorandum of points and authorities", "CCP 1005 notice period", "motion to compel arbitration CCP 1281.2", "new California motion". Scaffolds a complete motion packet that complies with CRC 3.1113, CCP § 1005, and the pro-se drafting framework adapted for California superior court practice. Composes with `ca-statewide-format` (always), `ca-lasc` / `ca-sfsc` / `ca-county-courts` (court-specific), `ca-pro-se` (if pro se), and `ca-discovery` / `ca-post-judgment` depending on the motion type.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-draft-motion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a California Motion Packet

Scaffold a complete California motion packet that complies with
CRC 3.1113, CCP § 1005, and the pro-se drafting framework adapted for
California superior court practice.

## What this skill produces

A California motion packet with the following components, each
on its own page or properly separated:

1. **Notice of Motion** (CCP § 1010) — standalone document;
   states the date, time, department, grounds, and supporting
   papers
2. **Memorandum of Points and Authorities** (CRC 3.1113) —
   supporting brief; max 15 pages without leave (CRC
   3.1113(d)); table of contents and table of authorities
   required if over 10 pages (CRC 3.1113(f))
3. **Declaration(s)** — separately titled documents; sworn
   facts under CCP § 2015.5
4. **Request for Judicial Notice** (Cal. Evid. Code §§ 452–453)
   — if requesting the court to notice legislative history,
   court records, official acts, etc.
5. **Proposed Order** (CRC 3.1312) — title "[PROPOSED] ORDER
   GRANTING [Motion Title]"
6. **Proof of Service** — signed by server; affirmatively
   states method and date

## Inputs to ask the user

- **Court / venue**: Los Angeles Superior? San Francisco
  Superior? Other?
- **Case number**: e.g., `25STCV12345`
- **Caption**: Plaintiff / Defendant party names
- **Motion type**: demurrer, motion to strike, compel, SJ,
  anti-SLAPP, MTC arbitration, motion in limine, etc.
- **Procedural authority**: which CCP / CRC / local rule is
  being invoked
- **Relief requested**: specifically what should the court order?
- **Hearing date**: already reserved with the clerk?
- **Department and judge**: e.g., Dept. 32, Hon. [Name]
- **Pro se or counsel**: affects signature block and
  formatting of attorney info block
- **Meet-and-confer compliance**: completed? (required for
  demurrer, motion to strike, motion to compel)

## Motion packet components in detail

### 1. Notice of Motion (CCP § 1010)

The Notice of Motion is a **separate document** — not combined
with the Memorandum. It functions as the cover page of the
packet and establishes the hearing date on the face of the
filing.

Required content under CCP § 1010:

- Caption per CRC 2.111 (see below)
- Title: "NOTICE OF MOTION AND MOTION FOR [RELIEF]"
- Date, time, and place of hearing (department number,
  courthouse address)
- Nature of the relief sought
- Grounds (legal basis, with citations)
- Statement of supporting papers: "This motion is based on
  this notice; the accompanying Memorandum of Points and
  Authorities; the Declaration of [Name] filed herewith; the
  [pleadings and papers on file in this action]; and such oral
  and documentary evidence as may be presented at the hearing."

```
                    NOTICE OF MOTION AND MOTION
                TO COMPEL FURTHER RESPONSES TO REQUESTS
                 FOR PRODUCTION UNDER CCP § 2031.310

TO PLAINTIFF [NAME] AND ITS COUNSEL OF RECORD:

PLEASE TAKE NOTICE that on [DATE], at [TIME], in Department
[##] of the above-entitled court, located at [COURTHOUSE
ADDRESS], Defendant [Name] will, and hereby does, move for
an order compelling Plaintiff to serve further responses to
Defendant's Requests for Production, Set One, Nos. [X–Y],
without objection, and to produce all responsive documents
within [10] days of the order.

This Motion is made pursuant to CCP § 2031.310 on the grounds
that Plaintiff's objections are without merit and that
Plaintiff has failed to comply with its obligations under
CCP §§ 2031.230 and 2031.240.

This Motion is based on this Notice; the accompanying
Memorandum of Points and Authorities; the Declaration of
[Declarant Name] filed herewith; and the pleadings and papers
on file in this action.

DATED: _______________

                                    ___________________________
                                    [NAME]
                                    [Attorney for] Defendant
```

### 2. Memorandum of Points and Authorities (CRC 3.1113)

The Memorandum is the substantive brief. Key requirements:

- **Page limit**: 15 pages without leave of court (CRC
  3.1113(d)); 20 pages with leave
- **Table of contents + table of authorities**: required if
  memorandum exceeds 10 pages (CRC 3.1113(f))
- **Font and margins**: CRC 2.104 (12 pt), CRC 2.108 (1 inch
  margins); double-spaced body (CRC 2.108(b))
- **Separate from Notice**: Memorandum begins on its own page

Structure (pro-se drafting framework for California):

```
MEMORANDUM OF POINTS AND AUTHORITIES

I.   INTRODUCTION
II.  STATEMENT OF FACTS
III. ARGUMENT
     A. [Point heading — first issue]
     B. [Point heading — second issue]
     C. [Fee award] (if applicable)
IV.  CONCLUSION
```

### 3. Declarations

See `ca-draft-declaration` for full scaffold. Key integration:

- Declarations are filed as separately titled documents
- Each declaration supports specific factual paragraphs cited
  in the Memorandum
- Exhibits attach to the declaration, not the motion

### 4. Request for Judicial Notice (if needed)

Under Cal. Evid. Code § 452, the court **may** judicially
notice legislative history, official acts, court records,
and certain public documents. Under § 453, a party requesting
judicial notice must give advance notice of the request.

Format:

```
REQUEST FOR JUDICIAL NOTICE IN SUPPORT OF [MOTION TITLE]

Pursuant to California Evidence Code §§ 452–453, Defendant
respectfully requests that the Court take judicial notice
of the following:

1.  A true and correct copy of [Document], attached hereto
    as Exhibit A. This document is [the basis for notice —
    e.g., "a record of the Los Angeles Superior Court" per
    Evid. Code § 452(d)].

2.  [Additional items ...]
```

### 5. Proposed Order

See `ca-draft-order` for full scaffold. Key integration:

- Title: "[PROPOSED] ORDER GRANTING [MOTION TITLE]"
- Filed with the motion packet at the time of filing
- Per CRC 3.1312, prevailing party circulates for
  approval/objection post-ruling

### 6. Proof of Service

Filed with every document served on opposing parties. Must
affirmatively state:

- Name and address of the server
- Date, method, and address of service
- If mail: must state the server is over 18, not a party,
  and mailing from a CA county on the stated date (CCP
  § 1013a)
- If electronic: must state the transmission was complete
  (CCP § 1010.6)
- Signed under penalty of perjury

## Service and notice timing

### CCP § 1005(b) — minimum notice

| Service method | Notice period before hearing |
|---|---|
| Personal service | 16 court days |
| First-class mail (CA) | 16 court days + 5 calendar days |
| First-class mail (out-of-state) | 16 court days + 10 calendar days |
| Electronic service (CCP § 1010.6) | 16 court days + 2 court days |
| Overnight delivery | 16 court days + 2 calendar days |

Opposition is due **9 court days** before the hearing.
Reply is due **5 court days** before the hearing (§ 1005(b)).

### Calculation tip

Count **court days** (excluding weekends and California
holidays per Cal. Gov. Code § 6700 et seq.), not calendar
days. Use `ca-deadlines` to compute the exact calendar date.

### Hearing reservation

Most California superior courts — including LASC — require
you to reserve a hearing date **before** serving the Notice
of Motion. Check the court's local rules and the department's
standing orders. LASC requires reservation through the Court
Reservation System (CRS). SFSC Civil Division has its own
scheduling portal.

## Caption format (CRC 2.111)

The caption appears at the top of every document:

```
[Name]                                    [CASE NUMBER FORMAT:
[Address]                                  25STCV12345 (LASC)
[City, State, ZIP]                         CGC-25-123456 (SFSC)]
[Phone]
[Email]
[CA Bar No. XXXXXX — attorneys only]      [HEARING DATE]
                                           [DATE]:
[Party: Plaintiff / Defendant, in pro per] [TIME]:
                                           [DEPT]:
                                           [JUDGE]:

              SUPERIOR COURT OF THE STATE OF CALIFORNIA
                       COUNTY OF [COUNTY]

[PLAINTIFF NAME],                    )
                                     )   Case No. [Case Number]
          Plaintiff,                 )
                                     )   [PROPOSED] ORDER
     v.                              )   [or document title]
                                     )
[DEFENDANT NAME],                    )   Hearing:
                                     )   Date:  [Date]
          Defendant.                 )   Time:  [Time]
                                     )   Dept.: [Dept. No.]
                                     )   Judge: Hon. [Name]
```

- Attorney info (or pro se info) goes in the **upper-left
  block** within the first 2.5 inches from the top
- Case information goes in the **upper-right block**
- Line numbers (1–28) appear on the left margin per CRC 2.108

## The pro-se drafting framework — California adaptation

California judges are busy. Apply the pro-se drafting framework:

**Lead with the strongest legal point**. The Introduction
should not recite procedural history — it should state the
result the court should reach and the primary reason in two
sentences maximum.

### I. Introduction (one to two paragraphs)

```
I.  INTRODUCTION

    Plaintiff has stonewalled discovery for three months.
    The documents at issue — Plaintiff's chain-of-title
    records — go to whether Plaintiff owns the account it
    sued on. The Court should compel production and shift
    fees under CCP § 2023.030.
```

Avoid: "This case arises from..." or "On [date], Plaintiff
filed..." Save procedural background for the facts section.

### II. Statement of Facts

Each fact is one short sentence, cited to the supporting
declaration paragraph and exhibit:

```
II. STATEMENT OF FACTS

    On April 1, 2025, Defendant served Requests for
    Production, Set One, Nos. 1–8. (Decl. Smith ¶ 3,
    Ex. 1.) On May 1, 2025, Plaintiff served Responses,
    interposing boilerplate objections and producing no
    documents. (Decl. Smith ¶ 4, Ex. 2.) On May 10, 2025,
    Defendant sent a meet-and-confer letter identifying
    the deficiencies. (Decl. Smith ¶ 5, Ex. 3.) The
    parties conferred by telephone on May 15, 2025. (Id.
    ¶ 6.) Plaintiff did not supplement its responses. (Id.
    ¶ 7.)
```

### III. Argument

Sub-headings in bold, all caps:

```
III. ARGUMENT

     A.  THE DOCUMENTS ARE RELEVANT AND DISCOVERABLE
         UNDER CCP § 2017.010.

         [2–3 paragraphs with rule → facts → conclusion]

     B.  PLAINTIFF'S OBJECTIONS ARE MERITLESS.

         [2–3 paragraphs]

     C.  THE COURT SHOULD AWARD MONETARY SANCTIONS
         UNDER CCP § 2023.030(a).

         [1–2 paragraphs]
```

### IV. Conclusion

One sentence. Restate the specific relief:

```
IV. CONCLUSION

    For the foregoing reasons, Defendant respectfully
    requests that the Court grant this Motion, compel
    Plaintiff to serve verified further responses and
    produce all responsive documents within 10 days, and
    award monetary sanctions of $[amount].
```

## Motion-type quick reference

### General Demurrer (CCP § 430.10(e)/(f))

- **Grounds**: failure to state facts sufficient to
  constitute a cause of action (§ 430.10(e)); uncertainty
  (§ 430.10(f))
- **Meet-and-confer**: CCP § 430.41 — counsel must meet and
  confer at least 5 days before filing (or file promptly
  after); declaration of compliance required
- **Timing**: 30 days after service of complaint if served
  in CA (CCP § 430.40); check local rules
- **Companion document**: a demurrer may stand alone or
  accompany a motion to strike; no supporting declaration
  usually required unless facts are at issue

### Motion to Strike (CCP §§ 435–437)

- **Targets**: irrelevant, false, or improper matter in
  any pleading; punitive damage claims lacking proper
  allegations
- **Meet-and-confer**: CCP § 435.5 — same framework as
  demurrer meet-and-confer
- **Common use**: striking punitive damages allegations in
  concert with a demurrer

### Motion to Quash Service of Summons (CCP § 418.10)

- **Grounds**: no personal jurisdiction; improper service
- **Timing**: must be filed before or in lieu of answering
- **Effect**: does not waive jurisdictional defenses if
  properly raised

### Anti-SLAPP Motion (CCP § 425.16)

- **Two-step test**: (1) defendant shows the claim arises
  from protected activity (petition or free speech); (2)
  plaintiff shows probability of prevailing
- **Timing**: 60 days of service of complaint (§ 425.16(f));
  may be later with court permission
- **Discovery stay**: automatic on filing (§ 425.16(g))
- **Fee award**: mandatory to prevailing defendant
  (§ 425.16(c)(1))
- **Special statement**: no mandatory separate statement;
  anti-SLAPP briefing is self-contained

### Motion for Summary Judgment / Adjudication (CCP § 437c)

- **Notice**: 75 days before hearing (§ 437c(a)) — this is
  the most important California distinction from federal
  practice
- **Mandatory separate statement**: § 437c(b)(1) — a separate
  document listing each material fact and the evidence
  supporting it; the court need not consider evidence not
  cited in the separate statement
- **Opposition**: 14 days before hearing (§ 437c(b)(2))
- **Reply**: 5 days before hearing (§ 437c(b)(4))
- **Standard**: no triable issue of material fact + moving
  party entitled to judgment as a matter of law
- **Adjudication**: limits to specific causes of action or
  affirmative defenses (§ 437c(f))

### Motion to Compel (CCP §§ 2030.300, 2031.310, 2033.290)

- **Interrogatories**: CCP § 2030.300 (compel further
  responses); deadline: 45 days after service of responses
  (§ 2030.300(c))
- **Requests for production**: CCP § 2031.310 (compel
  further); same 45-day deadline
- **Requests for admissions**: CCP § 2033.290 (compel
  further)
- **Separate statement**: required by CRC 3.1345 — each
  request, the response, and the moving party's argument
  must appear side-by-side
- **Fee motion**: CCP § 2023.030(a) — monetary sanctions
  for misuse of discovery

### Motion to Compel Arbitration (CCP § 1281.2)

- **Standard**: show written agreement to arbitrate +
  dispute falls within scope
- **Defense to watch**: CCP § 1281.2(c) — court may decline
  to compel if there is a risk of conflicting rulings with
  a pending related court action
- **Stay**: court stays the action while arbitration
  proceeds

### Motion in Limine

- **Timing**: typically filed 10–30 days before trial per
  local rules; check department-specific rules
- **No mandatory separate statement** for motions in limine
- **Limited memorandum length**: many courts impose a
  tighter page limit than CRC 3.1113(d) for motions in
  limine

## Meet-and-confer requirements

| Motion type | Rule | Deadline |
|---|---|---|
| Demurrer | CCP § 430.41 | At least 5 days before filing |
| Motion to strike | CCP § 435.5 | At least 5 days before filing |
| Motion to compel (discovery) | CCP §§ 2030.300(b), 2031.310(b) | Before filing; declaration required |
| Summary judgment | CCP § 437c | No statutory M&C requirement; some courts require it |

The meet-and-confer declaration must be filed with the motion
(§ 430.41(a)(3) for demurrers; §§ 2030.300(b)(2),
2031.310(b)(2) for discovery motions). Describe: when, how,
what was discussed, what remains unresolved.

## Worked example — Motion to Compel Further Responses to Discovery

### Packet components

1. **Notice of Motion and Motion to Compel Further Responses
   to Requests for Production, Set One, Under CCP § 2031.310**
2. **Memorandum of Points and Authorities** (with separate
   statement incorporated by reference or attached)
3. **Separate Statement of Disputed Items** (CRC 3.1345)
4. **Declaration of Defendant Jane Doe** — facts re service,
   responses, meet-and-confer
5. **[PROPOSED] Order Granting Motion to Compel**
6. **Proof of Service**

### Separate Statement format (CRC 3.1345)

```
SEPARATE STATEMENT OF ITEMS IN DISPUTE
IN SUPPORT OF MOTION TO COMPEL FURTHER RESPONSES
TO REQUESTS FOR PRODUCTION, SET ONE

REQUEST FOR PRODUCTION NO. 3:

All DOCUMENTS evidencing any assignment of the alleged
account from [Original Creditor] to Plaintiff.

RESPONSE TO REQUEST FOR PRODUCTION NO. 3:

[Plaintiff's verbatim response, including all objections]

REASON WHY FURTHER RESPONSE SHOULD BE COMPELLED:

The documents showing chain of title are directly relevant
to Plaintiff's standing to sue under CCP § 2017.010. ...
```

### Skeleton memorandum for a motion to compel

```
MEMORANDUM OF POINTS AND AUTHORITIES IN SUPPORT OF
DEFENDANT'S MOTION TO COMPEL FURTHER RESPONSES TO
REQUESTS FOR PRODUCTION, SET ONE, UNDER CCP § 2031.310

I.  INTRODUCTION

    Plaintiff cannot prove it owns the account it sued on
    because it refuses to produce its chain-of-title
    documents. The Court should compel production and
    award sanctions.

II. STATEMENT OF FACTS

    [Numbered factual paragraphs with declaration cites]

III. ARGUMENT

    A.  THE DOCUMENTS ARE DISCOVERABLE.

        Under CCP § 2017.010, any matter relevant to any
        party's claim or defense and proportional to the
        needs of the case is discoverable. ...

    B.  PLAINTIFF'S OBJECTIONS ARE BOILERPLATE AND
        IMPROPER.

        Boilerplate objections are an abuse of the
        discovery process. (See Weil & Brown, Cal. Prac.
        Guide: Civil Procedure Before Trial (Rutter) ¶
        8:1484.) The objection "not in my possession" does
        not excuse a party from searching for documents
        in its custody or control. (CCP § 2031.230.) ...

    C.  MONETARY SANCTIONS ARE WARRANTED.

        CCP § 2023.030(a) authorizes the court to impose
        monetary sanctions for misuse of discovery. ...

IV. CONCLUSION

    [Specific relief requested]
```

## Layered composition

This skill ALWAYS composes with:

- **`ca-statewide-format`** — caption, fonts, margins,
  line numbers, footer, exhibit conventions
- **The relevant court skill** — `ca-lasc`, `ca-sfsc`, or
  `ca-county-courts` — for local rules, department-specific
  procedures, and hearing reservation

It typically composes with:

- **`ca-pro-se`** — pro-se drafting framework details, pro se
  signature block, service protocol
- **`ca-draft-declaration`** — to draft the supporting
  declaration
- **`ca-draft-order`** — to draft the proposed order
- **`ca-draft-note`** — to draft the Notice of Motion

For motion-type-specific guidance:

- **`ca-discovery`** — for motions to compel; separate
  statement practice
- **`ca-post-judgment`** — for motions re: judgment
  enforcement
- **`ca-first-30-days`** — for demurrers, motions to
  strike, motions to quash in the initial response phase

## Output

The skill produces a Markdown scaffold of the motion packet.
The user fills in:

- Specific facts (with declaration citations)
- Specific argument
- Specific relief
- All citations verified against current codes

## Quality checks

After scaffolding, run:

- **`ca-quality-check`** — CRC 2.100–2.119 format pass
- **`ca-fact-check`** — citation and consistency pass

Before filing.

## Cross-references

- `ca-statewide-format` — caption + CRC 2.100–2.119 format
- `ca-pro-se` — pro-se drafting framework and pro se conventions
- `ca-lasc` / `ca-sfsc` / `ca-county-courts` — local rules
  and department procedures
- `ca-discovery` — discovery motion practice including
  separate statement

**NOT LEGAL ADVICE.** Generated content is a drafting aid;
verify against current rules and case law before filing.
