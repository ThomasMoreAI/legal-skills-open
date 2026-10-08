---
name: co-discovery-codearranger
title: Colorado Discovery
description: This skill should be used when drafting, responding to, or compelling discovery in a Colorado civil case. Triggers include "Colorado discovery", "C.R.C.P. 26", "interrogatories under Rule 33", "Request for Production under Rule 34", "Request for Admission under Rule 36", "Rule 26(a)(1) disclosures", "motion to compel", "Rule 37 sanctions", "deposition under Rule 30", "discovery dispute", "duty to confer in Colorado". Covers the C.R.C.P. 26-37 framework, the presumptive numeric limits in district court (25 interrogatories, 50 RFAs, 1 deposition per side per witness without leave), C.R.C.P. 16(b) case-management interaction with discovery, meet-and-confer obligations under C.R.C.P. 121 § 1-12 and § 1-15(8), and the county-court simplified discovery framework under C.R.C.P. 311.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-discovery
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Colorado Discovery

> **NOT LEGAL ADVICE.** This skill helps draft and respond to
> discovery. Verify against current C.R.C.P. and the assigned
> judge's practice standards before serving or filing.

Use this skill in addition to `co-statewide-format`,
`co-law-references`, and (where applicable) `co-first-30-days`. The
Colorado discovery framework derives from **C.R.C.P. 26-37** in
district court, with simplified parallel provisions in **county
court** under **C.R.C.P. 311**.

## Snapshot — Colorado discovery clock

| Trigger | Deadline / event | Rule |
|---|---|---|
| Case at issue (last responsive pleading filed) | C.R.C.P. 16 / 26 clock starts | C.R.C.P. 16(b) |
| Rule 26(f) conference | ≥ 14 days before CMC | C.R.C.P. 26(f) |
| Joint Proposed CMO | 7 days before CMC | C.R.C.P. 16(b)(2) |
| Initial Case Management Conference | ~ 49 days after at-issue | C.R.C.P. 16(b) |
| Rule 26(a)(1) initial disclosures | 28 days after at-issue | C.R.C.P. 26(a)(1) |
| Written discovery responses | 30 days after service | C.R.C.P. 33(a), 34(b), 36(a) |
| Expert disclosures — affirmative | 91 days before trial | C.R.C.P. 26(a)(2)(C)(I) |
| Expert disclosures — rebuttal | 56 days before trial | C.R.C.P. 26(a)(2)(C)(II) |
| Trial witness list / final disclosures | 28 days before trial | C.R.C.P. 26(a)(3) |
| Discovery cutoff | 49 days before trial (default) | C.R.C.P. 16(b)(8) — modifiable in CMO |

## Initial disclosures — C.R.C.P. 26(a)(1)

Within **28 days after the case is at issue**, each party must
disclose **without awaiting a discovery request**:

1. **Witnesses** with discoverable information — name, address, phone,
   email, and subjects
2. **Documents** that the disclosing party may use to support its
   claims or defenses
3. **Damages computation** with documents supporting it
4. **Insurance agreements** that may indemnify

C.R.C.P. 26(a)(1) initial disclosures are **automatic** in district
court. They are **NOT** required in county court (C.R.C.P. 311 has
no parallel provision) — county court discovery is limited and
court-directed.

## Interrogatories — C.R.C.P. 33

Colorado **DOES** allow written interrogatories (unlike Oregon, which
does not). The presumptive limit is **25 written interrogatories**
per side, counting discrete subparts (C.R.C.P. 33(a)(2)).

- Service: any time after the case is at issue
- Response due: **30 days** after service (C.R.C.P. 33(a)(3))
- Form: each interrogatory answered separately, under oath, with any
  objection stated specifically
- Excess interrogatories: require **leave of court**

```
INTERROGATORIES

Pursuant to C.R.C.P. 33, [Defendant] requests that [Plaintiff]
answer the following Interrogatories in writing under oath and serve
them upon the undersigned within 30 days of service.

INTERROGATORY NO. 1: State the name, address, and current employer
of each person who has knowledge of the facts pleaded in your
Complaint.

ANSWER:
[Response]

INTERROGATORY NO. 2: [...]
```

## Requests for Production — C.R.C.P. 34

- Service: any time after the case is at issue
- Response due: **30 days** after service (C.R.C.P. 34(b)(2)(A))
- Production format: native if requested; otherwise reasonably
  usable
- ESI handling: parallel to Federal Rule 34 — preserve metadata
  unless waived

## Requests for Admission — C.R.C.P. 36

- Service: any time after the case is at issue
- Response due: **30 days** after service (35 days with the
  C.R.C.P. 6(e) mail-extension)
- **Critical**: silence = admission. A party that fails to timely
  deny or object to an RFA admits it for purposes of the litigation
  (C.R.C.P. 36(a))
- Cannot be more than 50 in number absent leave (C.R.C.P. 36(a))

## Depositions — C.R.C.P. 30

- Limit: **one deposition per witness per side** without leave
  (C.R.C.P. 30(a)(2)(A)(ii))
- Length: **6 hours** absent agreement or court order (C.R.C.P.
  30(d)(1) — Colorado parallel to FRCP 30(d)(1))
- Notice: must serve **reasonable** advance notice; 10-14 days is
  customary
- Remote: depositions by **video conference** permitted by stipulation
  or court order under C.R.C.P. 30(b)(4)

## Subpoenas — C.R.C.P. 45

- Subpoena issuance: by party's attorney or pro se signatory
- Non-party document subpoena: serve **notice on opposing parties**
  10 days before service on the third party (C.R.C.P. 45(b)(1))
- Court reporter required for testimony subpoenas; party requesting
  bears witness/mileage fees

## Meet-and-confer — C.R.C.P. 121 § 1-12 and § 1-15(8)

Colorado **requires conferral** before filing most discovery motions:

- **C.R.C.P. 121 § 1-15(8)**: non-dispositive motions require a
  conferral statement
- **C.R.C.P. 121 § 1-12**: discovery disputes specifically
  contemplate informal resolution before motion practice

A typical meet-and-confer email:

```
Subject: Conferral re: Discovery Responses — [Case Short Title],
         Case No. [Number]

[Counsel Name],

This email constitutes the conferral required by C.R.C.P. 121
§ 1-15(8) before I file a Motion to Compel.

Your client's responses to my client's First Set of Interrogatories
and Requests for Production, served on [DATE], are deficient in the
following respects:

  1. Interrogatory No. 3 — Boilerplate objection ("vague, overly
     broad, unduly burdensome") without specifying which terms are
     vague or quantifying the burden. C.R.C.P. 26(b)(5) requires
     particularity.

  2. RFP No. 7 — No documents produced; response states "no
     non-privileged responsive documents exist." But Plaintiff's
     Complaint refers to documents that fall squarely within this
     request.

  [...]

I propose the following resolution: [specific proposal]. Please
respond by [date 7-10 days out] confirming whether your client will
provide supplemental responses. If I do not hear back, I will
proceed with a Motion to Compel under C.R.C.P. 37(a).

Best regards,
[Name]
```

Save copies of all conferral attempts. The court will not entertain a
motion to compel that lacks a credible conferral effort.

## Motion to compel — C.R.C.P. 37(a)

If conferral fails, file a motion to compel. The motion must:

1. **State the specific deficiencies** (which interrogatory / RFP /
   RFA and why the response is inadequate)
2. **Attach the discovery requests and responses** as exhibits
3. **Document the conferral attempt** in a separate Certificate of
   Conferral under C.R.C.P. 121 § 1-15(8)
4. **Quote and dispute each objection** under C.R.C.P. 26(b)(5)'s
   particularity requirement
5. **Request specific relief**: an order compelling responses by a
   date certain, an order awarding costs and fees under C.R.C.P.
   37(a)(5), or an order striking objections

The opposing party has 21 days to respond (C.R.C.P. 121 § 1-15);
movant may reply within 7 days.

### Sanctions under C.R.C.P. 37(a)(5) and 37(b)

- **37(a)(5)**: court "**must**" award expenses and fees to the
  prevailing party on a successful motion to compel unless the
  non-movant's position was substantially justified or other
  circumstances make an award unjust
- **37(b)**: stronger sanctions for disobedience to a discovery order
  — including striking pleadings, default judgment, contempt

## Discovery in county court — C.R.C.P. 311

County-court civil cases (under $25,000) follow a **simplified**
discovery framework under C.R.C.P. 311:

- **No presumptive C.R.C.P. 26(a)(1) initial disclosures**
- **Limited interrogatories** — by court order only
- **Subpoena power** under C.R.C.P. 345 (county court version)
- **Trial typically within 90-120 days** of at-issue; little time
  for protracted discovery

This is the discovery framework in **consumer debt-buyer cases**
filed in county court — see `co-consumer-debt` for the
discovery-strategy guidance specific to debt-buyer defense.

## Privilege log — C.R.C.P. 26(b)(5)

When withholding any document on the basis of privilege, the
producing party must serve a **privilege log** describing the nature
of the withheld document(s) so the requesting party can assess the
claim. The log must include:

- Date
- Author / recipient
- Subject matter (general)
- Privilege asserted

Insufficient privilege logs are sanctionable — see *Trotter v. 7R
Holdings*, 873 F.3d 1010 (10th Cir. 2017) (analogous Colorado
practice).

## Composition

- For drafting the motion to compel: `co-draft-motion`
- For the supporting declaration: `co-draft-declaration`
- For statewide format: `co-statewide-format`
- For consumer-debt RFP/RFA banks: `co-consumer-debt`
- For deadlines arithmetic: `co-deadlines`

## References

- `references/rfp-templates.md` — Request for Production templates
- `references/interrogatory-templates.md` — Interrogatory templates
- `references/rfa-templates.md` — Request for Admission templates
- `references/motion-to-compel.md` — full motion-to-compel scaffold
- `references/conferral-templates.md` — meet-and-confer email
  templates
- `references/privilege-log.md` — privilege-log format and content
