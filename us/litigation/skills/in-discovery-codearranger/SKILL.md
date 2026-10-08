---
name: in-discovery-codearranger
title: Indiana Civil Discovery
description: 'This skill should be used when the user asks to "draft an interrogatory", "send a request for production", "respond to discovery", "Indiana RFP", "Indiana RFA", "motion to compel Indiana", "Trial Rule 33", "Trial Rule 34", "Trial Rule 36", "Trial Rule 37", "Indiana deposition notice", "Indiana subpoena", "Trial Rule 45", "meet and confer Indiana", "Indiana discovery scope", "Indiana e-discovery", "Indiana protective order discovery", or any related civil discovery topic. Covers Indiana''s discovery regime under Trial Rules 26-37 — note the 25-interrogatory cap under T.R. 33(A), the broad "reasonably calculated to lead to discoverable evidence" scope of T.R. 26(B), meet-and-confer requirements under T.R. 37(E), and the motion-to-compel framework under T.R. 37(A). Trigger phrases: "T.R. 33", "T.R. 34", "T.R. 36", "T.R. 37(E)", "Indiana 25- interrogatory cap", "Indiana RFP response", "Indiana request for admission", "T.R. 45 subpoena", "Indiana deposition T.R. 30".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-discovery
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Indiana Civil Discovery

This skill governs all discovery activity in an Indiana civil
case — pre-trial fact development through interrogatories,
requests for production, requests for admission, depositions, and
subpoenas. The authority is Indiana Trial Rules 26-37, which
closely parallel the federal rules but include Indiana-specific
caps and procedure (most notably the 25-interrogatory limit under
T.R. 33(A) and the meet-and-confer rule under T.R. 37(E)).

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify against the current Indiana Trial Rules and the local
> rules of the venue county before serving or filing discovery.

## Discovery scope — Trial Rule 26(B)

T.R. 26(B)(1) defines the scope:

> "Parties may obtain discovery regarding any matter, not
> privileged, which is relevant to the subject matter involved
> in the pending action, whether it relates to the claim or
> defense of the party seeking discovery or to the claim or
> defense of any other party. ... It is not ground for objection
> that the information sought will be inadmissible at the trial
> if the information sought appears reasonably calculated to
> lead to the discovery of admissible evidence."

This is the **same wording** as the pre-2015 federal Rule 26(b);
Indiana did NOT adopt the 2015 federal "proportionality"
amendment to FRCP 26(b)(1). Indiana discovery is therefore
**broader** than federal discovery on the proportionality
dimension. The familiar federal "proportional to the needs of the
case" factors do not appear in Indiana's rule.

Limits:

- **Privilege** — attorney-client, work product (T.R. 26(B)(3)),
  spousal privilege, etc. Apply normal privilege doctrine.
- **Work product** — qualified immunity under T.R. 26(B)(3); the
  party seeking work product must show substantial need and
  inability to obtain equivalent without undue hardship.
- **Protective order** — T.R. 26(C) authorizes protective orders
  on a showing of good cause; standard model order is the Indiana
  State Bar Association's "Stipulated Protective Order
  Regarding Confidential Information" template.

## The four discovery devices

### 1. Interrogatories — Trial Rule 33

**The 25-interrogatory cap.** T.R. 33(A) limits interrogatories to
"25 in number including all discrete subparts." Counting subparts:
the Indiana Supreme Court has held that discrete subparts each
count, paralleling FRCP 33(a). To exceed the cap, the propounding
party must obtain leave of court or written stipulation.

Marion Civil Division's CPC § IV.B encourages parties to
stipulate to a higher cap rather than litigate the issue. The
typical stipulation is 50 interrogatories.

**Response deadline.** T.R. 33(C): 30 days after service. Unlike
federal practice (Rule 33(b)(4)), Indiana does NOT add 3 days for
service by mail — the 30-day clock runs from the date of service,
period. Service-by-mail extension applies only to the 20-day
answer rule under T.R. 6(C).

**Form of response.** Each interrogatory restated, then "Answer:"
followed by the response. If objection, state the objection with
particularity (T.R. 33(C)(2)). Verification by oath is required
(T.R. 33(C)).

**Common objections to interrogatories**:

| Objection | When to assert |
|-----------|----------------|
| Overbreadth | Interrogatory not limited in time or scope |
| Vagueness | Defined terms unclear |
| Privileged | Attorney-client, work product |
| Burdensome | Compilation requires extensive effort |
| Compound | Single interrogatory disguised as multiple |
| Exceeds 25-cap | Counting the subparts pushes past the cap |

### 2. Requests for Production — Trial Rule 34

**No numerical cap** on Requests for Production (RFPs) in Indiana.
Unlike interrogatories, parties may serve as many RFPs as needed,
though courts will quash unreasonably burdensome requests.

**Response deadline.** T.R. 34(B): 30 days after service. Each
request must be answered (production or objection) within 30 days.

**Form of response.** Each request restated, followed by
"Response: Documents responsive to this request are attached as
[Exhibit A / Bates 0001-0100]" or an objection.

**Electronically stored information (ESI).** T.R. 34(A)(2)
permits requests for ESI. Indiana adopted electronic-discovery
rules in 2008, paralleling FRCP 34. Specify the form of
production (PDF, native file with metadata, etc.) in the request.

### 3. Requests for Admission — Trial Rule 36

**Critical rule.** T.R. 36(A): if a request for admission is not
answered or objected to within 30 days of service, the matter is
**deemed admitted**. A pro se litigant who misses the 30-day
window has waived the disputed facts.

**Use cases:**
- Authenticate documents ("Admit that Exhibit A is a true and
  accurate copy of the [contract / agreement / statement]")
- Establish factual predicates ("Admit that on March 1, 2024, the
  defendant signed the document attached as Exhibit B")
- Narrow trial issues

**Response options.** Within 30 days, the responding party must
either:

- Admit the request
- Deny the request (specifically and with particularity)
- State that the responding party lacks sufficient information
  after reasonable inquiry (the "reasonable inquiry" answer)
- Object to the request

A general denial or a non-responsive "deny" will be treated as an
admission (T.R. 36(A)(2)). The 30-day deadline is jurisdictional
— motion to extend must be filed before the 30 days expire.

### 4. Depositions — Trial Rule 30

T.R. 30 governs oral depositions. Indiana practice closely
mirrors federal:

- **Notice**: at least 10 days notice (T.R. 30(B)(1))
- **Duration**: 7 hours of testimony unless extended (T.R.
  30(D)(2))
- **Location**: at the deponent's residence county unless agreed
  otherwise; for parties, the action's venue county is also
  acceptable
- **Subpoena**: required for non-parties (T.R. 45)
- **Objection**: stated for the record; the deposition continues;
  rulings made by the trial court later

**Number of depositions**: no fixed cap in T.R. 30. Marion CPC
recommends parties limit to 10 depositions per side absent
stipulation.

## Subpoenas — Trial Rule 45

T.R. 45 governs subpoenas. Two forms:

- **Subpoena Duces Tecum** — commands the recipient to produce
  documents
- **Subpoena Ad Testificandum** — commands the recipient to
  appear at a deposition or trial

Service of a subpoena: by Sheriff or any non-party adult, with a
witness-fee tender ($10 plus mileage). Marion LR49-TR45 requires
the subpoena to include a copy of T.R. 45(C) (rights of the
recipient).

For documents-only subpoenas to non-parties, T.R. 45(B)(1)
requires notice to all parties at least 5 days before service so
they can object.

## Meet-and-confer — Trial Rule 37(E)

T.R. 37(E) was added in 2008 (renumbered in 2014). Before filing
a motion to compel, the moving party MUST:

> "[I]n good faith confer or attempt to confer with the person or
> party failing to make the discovery in an effort to resolve the
> matter without court action."

Practical points:

- A single email or letter typically satisfies "attempt to
  confer." Best practice: send a detailed letter setting out the
  defects, give the recipient at least 7-10 days to respond, then
  follow up.
- The meet-and-confer certificate is attached to the motion to
  compel (T.R. 37(E)). Without it, the court may decline to rule.
- Marion LR49-TR37 requires the certificate to recite the dates
  of the conferral and the specific issues discussed.

## Motion to Compel — Trial Rule 37(A)

When meet-and-confer fails, file a Motion to Compel under T.R.
37(A). Required components:

1. **Caption + title**: "DEFENDANT'S MOTION TO COMPEL RESPONSES
   TO REQUESTS FOR PRODUCTION"
2. **Recital of facts**: date the discovery was served, date the
   response was due, status of meet-and-confer
3. **Specific deficiencies**: each unanswered request listed
   verbatim with a brief explanation of why the response is
   inadequate
4. **Authority**: T.R. 26(B), T.R. 34, T.R. 37(A), and any case
   law on the specific issue
5. **Relief sought**: order compelling response within X days,
   sanctions under T.R. 37(B), reasonable attorney fees / costs
   under T.R. 37(A)(4)
6. **Meet-and-confer certificate**: required exhibit
7. **Proposed order**: required by Marion CPC § II.A

**Sanctions under T.R. 37(B)** — if the court grants the motion
and the noncompliant party still refuses to respond, the court
may:

- Strike pleadings
- Hold the party in contempt
- Award reasonable attorney fees and costs
- Enter judgment as a discovery sanction (the so-called "death
  penalty" sanction; reserved for egregious noncompliance)

Indiana's leading case on discovery sanctions: *Wright v.
Miller*, 989 N.E.2d 324 (Ind. 2013) (affirming discretion of
trial court in sanctioning a party for repeated discovery
violations).

## Discovery in small-claims and limited-jurisdiction cases

Indiana Small Claims Rules (S.C.R.) 6 limits discovery in small-
claims cases:

> "No interrogatories, requests for production of documents,
> requests for admission, or depositions shall be allowed except
> upon order of the court."

Marion County Small Claims practice rarely orders discovery; the
court expects the parties to be ready at trial without formal
pretrial discovery. Lake County's County Division small-claims
dockets follow the same restriction.

For Civil Plenary (PL), Civil Collection (CC), and Civil Tort
(CT) cases in Marion / Lake Superior Courts and county Circuit /
Superior Courts, full T.R. 26-37 discovery applies.

## Discovery timeline — typical Marion civil case

```
Day 0     Issue joined (Answer filed)
Day 60    Joint CMS filed
Day 90    First status conference; discovery officially open
Day 120   First wave of discovery served
Day 150   Discovery responses due (30 days from service)
Day 180   Meet-and-confer over deficiencies
Day 210   Motion to compel filed if needed
Day 240   Second wave of discovery served (after document review)
Day 270   Depositions begin
Day 330   Expert disclosures (typically by court order)
Day 360   Discovery cut-off (typically 60-90 days before trial)
```

## Composition

- `in-statewide-format` for T.R. 5(E) / T.R. 10 baseline
- `in-marion` / `in-lake` / `in-county-courts` for venue-specific
  meet-and-confer protocols
- `in-pro-se` for self-represented discovery scope and pitfalls
- `in-deadlines` for the 30-day response calculation
- `in-fact-check` to verify case citations
- `in-draft-motion` for the motion-to-compel scaffolder

## References

- `references/discovery-rules-summary.md` — T.R. 26-37 quick-look
- `references/interrogatory-templates.md` — pattern interrogatory
  banks for civil collection, contract, tort
- `references/rfp-templates.md` — pattern RFP banks
- `references/rfa-templates.md` — pattern RFA banks
- `references/motion-to-compel-template.md` — fully drafted
  scaffold with meet-and-confer certificate

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
