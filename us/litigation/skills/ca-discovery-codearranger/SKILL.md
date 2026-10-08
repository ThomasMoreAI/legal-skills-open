---
name: ca-discovery-codearranger
title: California Discovery — Procedural Reference
description: 'Use when drafting, responding to, or compelling discovery in California civil cases. Triggers include "requests for production", "RFP", "RFA", "interrogatories", "specially prepared interrogatories", "form interrogatories", "DISC-001", "deposition", "meet and confer", "motion to compel", "discovery cutoff", "rule of 35", "separate statement", "CRC 3.1345", "discovery objections", "privilege log", "45-day deadline", "discovery sanctions". Covers California Civil Discovery Act (CCP §§ 2016.010 et seq.): scope, six methods, interrogatory limits, Rule of 35, meet-and-confer requirements, 45-day jurisdictional deadline for motions to compel further, mandatory separate statements, and sanctions under CCP § 2023.030.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-discovery
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Meet And Confer
  path: references/meet-and-confer.md
- title: Objection Responses
  path: references/objection-responses.md
---

# California Discovery — Procedural Reference

This skill covers the **matter-neutral procedural framework** for
discovery under the California Civil Discovery Act (Code Civ. Proc.,
§§ 2016.010 et seq.). For subject-matter-specific request banks
(e.g., debt-buyer chain-of-title RFPs), compose with the relevant
subject-matter skill.

> **NOT LEGAL ADVICE.** Verify each statute and the applicable local
> rules before drafting.

## Discovery scope — CCP § 2017.010

The scope of civil discovery in California:

> "Unless otherwise limited by order of the court... any party may
> obtain discovery regarding any matter, not privileged, that is
> relevant to the subject matter involved in the pending action...
> if the matter either is itself admissible in evidence or appears
> reasonably calculated to lead to the discovery of admissible
> evidence."
> (Code Civ. Proc., § 2017.010.)

Scope is broad — **relevance to the subject matter** is the test,
not relevance to an admissible claim or defense. This is broader
than the post-2015 federal standard (FRCP 26(b)(1), which requires
relevance to a *claim or defense*).

Limits on scope:

- **Privilege**: attorney-client (Evid. Code, §§ 950-962),
  work product (Code Civ. Proc., § 2018.020), and other statutory
  privileges shield protected materials
- **Proportionality**: courts will limit unduly burdensome discovery
  under Code Civ. Proc., § 2019.030
- **Discovery cutoff**: 30 days before trial (see below)

## The six discovery methods

California's Civil Discovery Act provides six tools:

1. **Oral depositions** (Code Civ. Proc., §§ 2025.010 et seq.)
2. **Written depositions** (Code Civ. Proc., §§ 2028.010 et seq.)
3. **Interrogatories** (Code Civ. Proc., §§ 2030.010 et seq.)
4. **Requests for production / inspection** (Code Civ. Proc.,
   §§ 2031.010 et seq.)
5. **Physical / mental examinations** (Code Civ. Proc.,
   §§ 2032.010 et seq.)
6. **Requests for admission** (Code Civ. Proc., §§ 2033.010 et seq.)

Subpoenas for non-party discovery live at Code Civ. Proc.,
§§ 1985–1987.8.

**Important California distinction:** Unlike Oregon (which has no
interrogatories under the ORCP as a matter of right), **California
allows interrogatories** subject to numerical caps. Unlike federal
practice (where interrogatories are limited to 25 without leave),
California uses the **"Rule of 35"** described below.

---

## Interrogatories — the Rule of 35 (CCP § 2030.030)

### Specially prepared interrogatories

A party may propound specially prepared interrogatories (drafted
specifically for the case). Under Code of Civil Procedure section
2030.030, subdivision (a)(1):

- **Up to 35** specially prepared interrogatories may be served
  on any other party **without a supporting declaration**.
- **Over 35** requires a **Declaration of Necessity** under Code
  of Civil Procedure sections 2030.040 and 2030.050.

The Declaration of Necessity must state facts showing:

- The complexity or the quantity of issues in the case; OR
- The financial burden on parties of going to trial; OR
- The expedience of using interrogatories for issues that might
  otherwise require depositions (Code Civ. Proc., § 2030.050).

**Do not exceed 35 without a declaration.** Interrogatories over
the limit are objectionable on their face; the responding party
can refuse to answer anything beyond No. 35 without a valid
declaration.

### Form interrogatories — no numerical limit

**Judicial Council Form Interrogatories** have no numerical cap
(Code Civ. Proc., § 2030.030(b)):

- **DISC-001** — Form Interrogatories — General (covers
  background facts, damages, witnesses, documents, insurance)
- **DISC-002** — Form Interrogatories — Economic Litigation
  (for economic damages: business records, lost profits, etc.)
- **DISC-020** — Form Interrogatories — Employment Law
- **DISC-004** — Form Interrogatories — Unlawful Detainer

Parties may select specific questions from the form by checking
the applicable boxes. Unanswered checked questions are treated
as unanswered interrogatories.

**Strategy note:** Form interrogatories are often more effective
than specially prepared interrogatories for standard factual
background because (a) they have no numerical limit, (b) they
have been interpreted by appellate courts, and (c) form-approved
language is harder to object to on vagueness grounds.

### Response deadline — interrogatories

The responding party must serve verified responses within:

- **30 calendar days** from the date of service (Code Civ. Proc.,
  § 2030.260(a))
- **35 calendar days** if interrogatories were served with the
  summons (Code Civ. Proc., § 2030.260(b))

**Responses must be verified** — signed under penalty of perjury
under Code of Civil Procedure section 2015.5 (Code Civ. Proc.,
§ 2030.250(a)). Unverified interrogatory responses are a nullity
and the propounding party may move to compel verified responses.

---

## Requests for Production (RFPs) — CCP §§ 2031.010 et seq.

### No numerical cap

Unlike interrogatories, requests for production have **no
numerical limit** in California (Code Civ. Proc., § 2031.010).
A party may propound as many RFPs as needed.

### Response deadline

The responding party must serve a **written response** and
produce (or make available for inspection) all responsive
documents within:

- **30 calendar days** from the date of service (Code Civ. Proc.,
  § 2031.260(a))
- **35 calendar days** if served with the summons

Responses must be verified (Code Civ. Proc., § 2031.250).

### Form of response

Each response must state one of:

1. **Agreement to comply**: "Responding party will comply with
   this demand and produce all responsive documents in its
   possession, custody, or control."
2. **Inability to comply**: verified statement that responding
   party conducted a diligent search and that no responsive
   documents exist or are not in its possession, custody, or
   control. (Code Civ. Proc., § 2031.230.)
3. **Objection**: state specific grounds (Code Civ. Proc.,
   § 2031.240). Boilerplate objections without explanation are
   insufficient — they can be stricken.

### What "possession, custody, or control" means

A party must produce documents it **controls**, not just documents
physically in its office. Control includes documents a party has
the **legal right to obtain** from a third party on demand. A debt
buyer claiming it does not "possess" documents from the original
creditor when it has contractual rights to request them is likely
making an insufficient possession objection.

### Drafting good RFPs

A well-drafted RFP is:

- **Specific**: targets a defined category ("all documents
  constituting the original cardholder agreement"), not "all
  documents related to the account"
- **Defined terms**: definitions section at the top of the RFP
  set should define "DOCUMENT", "RELATE TO / CONCERNING",
  "YOU / YOUR", etc.
- **Time-bounded**: "documents dated or created between January
  1, 2018 and December 31, 2023"
- **Party-bounded**: "documents in the possession, custody, or
  control of Plaintiff or its agents"

Example (well-drafted):

> **Request for Production No. 3:** All documents constituting,
> evidencing, or summarizing the original credit card agreement
> between Defendant and Bank of America for account number ending
> in XXXX, including any signature pages, terms and conditions,
> and electronic acceptance records, from the date the account
> was opened through the date Plaintiff claims it was assigned
> to Plaintiff.

---

## Requests for Admission (RFAs) — CCP §§ 2033.010 et seq.

### Numerical cap — Rule of 35 for RFAs

Similar to interrogatories, California limits specially prepared
RFAs to **35** without a declaration of necessity under Code of
Civil Procedure section 2033.030:

- **Up to 35 RFAs** without supporting declaration
- **Over 35** requires a declaration under Code Civ. Proc.,
  § 2033.050

RFAs seeking admission of the genuineness of documents are
**excluded** from the 35-question limit (Code Civ. Proc.,
§ 2033.030(b)) — you may propound an unlimited number of
document-genuineness RFAs in addition to the 35 factual RFAs.

### Response deadline

- **30 calendar days** from service (Code Civ. Proc.,
  § 2033.250(a))
- **35 calendar days** if served with the summons

### Default admission

Failure to respond within the deadline results in all matters
**deemed admitted** by operation of law (Code Civ. Proc.,
§ 2033.280(b)). The admitting party must file a motion for relief
from waiver — this is an uphill battle. Do not miss RFA deadlines.

### Drafting effective RFAs

Each RFA should be a **single, simple, provable fact**:

Good:
> **Request for Admission No. 5:** Admit that Plaintiff is a
> Delaware limited liability company.

Bad:
> **Request for Admission No. 5:** Admit that Plaintiff is a
> Delaware LLC organized in 2017 that purchased Defendant's
> account from Bank of America pursuant to a bulk sale
> agreement executed on April 1, 2022.

The compound form invites a partial denial that is useless for
narrowing issues. Break it into three separate RFAs.

---

## Depositions — CCP §§ 2025.010 et seq.

### Scheduling

Any party may take the deposition of any person after:

- Service of the complaint; AND
- 20 days after service of the summons (unless a declaration
  of earlier necessity is filed) (Code Civ. Proc., § 2025.210(b))

Deposition notice must be served at least **10 calendar days**
before the deposition (Code Civ. Proc., § 2025.270(a)). If the
deponent is a party, notice is sufficient; non-parties require
a deposition **subpoena** (Code Civ. Proc., § 2020.010).

### Deposition limits

Under Code Civ. Proc., § 2025.610:

- A witness may be deposed only **once per action** unless:
  - Leave of court is granted; or
  - The parties stipulate; or
  - The deposition was improperly short or incomplete for good
    cause

No fixed numerical limit on the number of different deponents
per party per case (unlike FRCP 30(a)(2)(A)'s 10-deposition cap),
but courts will limit unreasonable deposition programs under
Code Civ. Proc., § 2019.030.

### Deposition by written questions

Allowed under Code Civ. Proc., §§ 2028.010 et seq. Practical
for simple factual matters where an oral deposition is not
cost-effective; the process is slower and procedurally cumbersome.

---

## Discovery cutoff — CCP § 2024.020

**The discovery cutoff is 30 days before trial** (Code Civ. Proc.,
§ 2024.020(a)). All discovery must be **completed** (not just
served) before this date.

"Completed" means:
- For depositions: the deposition has concluded
- For written discovery: the response deadline has passed

Practical implications:

- If trial is in 60 days, serve all written discovery immediately
  (responses are due in 30 days; the cutoff is 30 days before
  trial — you need the full 30 days of response time before the
  cutoff)
- If trial is in 45 days, you are too late to serve written
  discovery and have the responses before the cutoff — unless
  the opposing party agrees to shorter response times

**Motions to compel discovery must be heard no later than
15 days before trial** (Code Civ. Proc., § 2024.020(a)).
This means filing the motion at least 16+ days before trial,
accounting for the notice period.

---

## Meet-and-confer — mandatory prerequisite

Before filing a motion to compel further discovery responses,
the moving party **must** meet and confer in writing (Code Civ.
Proc., §§ 2030.300(b)(1), 2031.310(b)(2), 2033.290(b)(1)).

The declaration in support of the motion must state:

- That a meet-and-confer was conducted
- The specific topics addressed
- The outcome (or non-response)

A motion without an adequate meet-and-confer declaration will be
denied. Many courts also expect a telephonic conference, not just
a letter, if the letter goes unanswered.

See `references/meet-and-confer.md` for sample letters and timing.

---

## Motion to compel further responses — CCP §§ 2030.300, 2031.310, 2033.290

### Grounds

A party may move to compel further responses if:

- The response is evasive or incomplete
- An objection is without merit or too general
- The response was unverified

### The 45-day JURISDICTIONAL deadline

**This is the most critical and most frequently missed deadline
in California discovery motion practice.**

The motion to compel **further** responses must be filed and
served within **45 days** of service of the verified response
(or any supplemental response):

- Interrogatories: Code Civ. Proc., § 2030.300(c)
- RFPs: Code Civ. Proc., § 2031.310(c)
- RFAs: Code Civ. Proc., § 2033.290(c)

**The 45-day deadline is JURISDICTIONAL.** The court loses
jurisdiction to compel if the motion is filed even one day late,
absent a court order or stipulation extending the deadline.
(*Sexton v. Superior Court* (1997) 58 Cal.App.4th 1403, 1409–10.)

Consequences:

- If the responding party served unverified responses, the
  45-day clock does **not** start running — unverified responses
  are a nullity; move to compel the verified response instead
  (Code Civ. Proc., § 2030.250(a))
- If the responding party serves supplemental responses, a new
  45-day period begins for the new responses
- Stipulations to extend the deadline must be in writing and
  filed with the court; oral agreements do not preserve
  jurisdiction

**Calendar the 45-day deadline immediately upon receiving any
discovery response.** This is a bright-line cut-off.

### Required separate statement — CRC 3.1345

Every motion to compel further discovery responses must include
a **Separate Statement** (California Rules of Court, rule 3.1345).

The Separate Statement must contain, for each discovery request
at issue:

1. The full text of the request
2. The full text of the response (including all objections)
3. The factual and legal reasons why the response is deficient
   and further response should be compelled

Omitting the Separate Statement is grounds for denial without
prejudice. It cannot be waived.

### Monetary sanctions — CCP § 2023.030

Upon granting a motion to compel further responses, the court
**shall** impose a monetary sanction against the losing party
"unless it finds that the one subject to the sanction acted with
substantial justification or that other circumstances make the
imposition of the sanction unjust" (Code Civ. Proc., § 2023.030(a)).

"Shall impose" means sanctions are **mandatory** on a successful
motion, not discretionary. Track attorney time (or pro se time
value) from the first meet-and-confer letter through the hearing
for the fee petition.

In addition to monetary sanctions, the court may impose:

- **Issue sanctions**: designated facts treated as established
  (Code Civ. Proc., § 2023.030(b))
- **Evidence sanctions**: prohibition on introducing evidence
  (Code Civ. Proc., § 2023.030(c))
- **Terminating sanctions**: dismissal or default (Code Civ.
  Proc., § 2023.030(d))
- **Contempt**: Code Civ. Proc., § 2023.030(e)

---

## Protective orders — CCP § 2019.060

A party from whom discovery is sought may move for a protective
order to:

- Limit the time, place, or manner of discovery
- Require certain procedures for protecting confidential
  information
- Forbid inquiry into certain matters
- Seal discovery materials (e.g., financial records, medical
  records, trade secrets)

Standard: **good cause** (Code Civ. Proc., § 2019.060). The court
balances the burden of disclosure against the need.

---

## Privilege log

When a party withholds documents on grounds of privilege or
work-product protection, California practice requires a **privilege
log** identifying each withheld document with enough information
for the propounding party to assess the claim.

Required log entries (per practice under Code Civ. Proc.,
§ 2031.240(c)(1)):

- Description of the document (without disclosing the privileged
  content)
- Date
- Author
- Recipient(s)
- Privilege asserted

A bare objection without a log is insufficient for privilege
claims and may result in an order compelling production or a
finding that the privilege was waived.

---

## Subpoenas for non-party discovery — CCP §§ 1985–1987.8

To obtain documents from a non-party, serve a **deposition
subpoena for business records** (not a party RFP). Key rules:

- Use Judicial Council form SUBP-010 (deposition subpoena for
  personal appearance and production of documents) or SUBP-002
  (business records subpoena without deposition)
- Serve the non-party at least **20 days** before the production
  date
- Serve a copy on all parties to the action at least **5 days**
  before serving the non-party (Code Civ. Proc., § 2020.220)
- Non-party has **15 days** to object (Code Civ. Proc., § 1985.3)

Consumer records and employment records require an additional
**notice to the consumer or employee** and a 15-day waiting period
after service of that notice before records are produced.
(Code Civ. Proc., § 1985.6.)

---

## Subject-matter request banks

This skill is matter-neutral. For pre-built request banks:

- **Debt-buyer chain of title**: see `ca-consumer-debt/references/`
  (RFPs targeting original creditor agreement, assignment schedule,
  pool-sale agreement, payment history)
- **Landlord-tenant** (future): would live in `ca-landlord-tenant/
  references/`
- **Personal injury** (future): would live in `ca-personal-injury/
  references/`

## References

- `references/meet-and-confer.md` — mandatory meet-and-confer
  protocol for California, sample letters, and timing chart
- `references/objection-responses.md` — common objections
  (overbroad, vague, burdensome, privilege, work product, trade
  secret) and California-specific guidance on each

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
