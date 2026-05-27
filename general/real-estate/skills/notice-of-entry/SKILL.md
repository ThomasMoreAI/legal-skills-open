---
name: notice-of-entry
title: Notice of Property Entry
description: Drafts contract-compliant Notice of Property Entry letters that satisfy Access Agreement advance-notice, scope, and delivery requirements. Trigger when the user mentions notice of entry, right-of-entry notice, property entry notice, access agreement notice, property inspection notification, business-day calendar calculations for entry, COI delivery before property access, or documenting scope/personnel for a real property inspection, environmental assessment, or construction access.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/notice-of-entry
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: real-estate
language: en
tags: [drafting, letter, litigation, regulatory, transactional]
---

# Notice of Property Entry

Produces a notice that satisfies contractual advance-notice provisions, defines scope and personnel, confirms insurance compliance, and creates a defensible evidentiary record so the entry cannot be challenged as unauthorized.

**ATTORNEY REVIEW REQUIRED** — No notice produced by this skill may be sent without attorney review.

## Quick Start

1. Gather Agreement details and entry plan (Checkpoint A)
2. Parse notice clause into drafting constraints
3. Verify scope, build entry window, list entrants/equipment, confirm insurance
4. Assemble notice using template
5. Adversarial-proof and finalize
6. Run post-draft alignment (Checkpoint B) and quality audit

## Checkpoint A: Pre-Draft Intake

Gather before drafting (apply labeled defaults if user says "use defaults" or "just draft": standard format, 48-hour advance notice, business-day calculation, formal delivery with proof of service):

| # | Input | Details |
|---|---|---|
| 1 | **Parties** | Legal names as in Agreement; recipient addresses/emails per notice clause |
| 2 | **Property ID** | Street address, APN/parcel if in Agreement |
| 3 | **Entry window** | Date, time, duration, alternatives if permitted; time zone |
| 4 | **Purpose/scope** | Activities using the Agreement's own terms |
| 5 | **Access areas** | Specific zones tied to exhibits or site plans |
| 6 | **Entrants** | Names, roles, affiliations; badge/vehicle info if required |
| 7 | **Equipment** | All equipment/vehicles; flag disruptive activities |
| 8 | **Insurance** | Policy types, limits, dates, additional insured, endorsements |
| 9 | **Safety** | Escort, PPE, pre-entry meetings, sign-in procedures |
| 10 | **Delivery method** | Transmission method, timing, proof of service plan |

Do NOT guess contractual terms — pause and ask if anything is missing.

## Core Workflow

### Step 1: Parse Notice Clause

- Extract minimum lead time, business-day rules, permitted hours, content requirements, delivery methods, prerequisites (e.g., COI before entry)
- Determine if lead time is hours, business hours, or business days; whether weekends/holidays count
- Determine if notice is effective on sending or receipt — controls last permissible sending time
- **Calendar trap**: Friday notice for Monday entry likely violates a two-business-day requirement
- Address to exact recipient, address, and email in the Agreement

### Step 2: Verify Scope Against Agreement

- Confirm every activity falls within permitted purposes; **flag for attorney review** if arguably outside scope
- Use "specific to general" approach:
  - Specific: "drilling of three 2-inch diameter soil borings to a depth of 10 feet"
  - Catch-all: "and other activities reasonably related to the Phase II ESA as authorized under Section [__]"
- Use the Agreement's own nouns/verbs; reference exhibits and site plans
- Never use vague phrases like "general inspection" or "entire property"
- State boundaries of what entrant will and will not do

### Step 3: Build Entry Window

- Match Agreement's format (specific time vs. range); always specify time zone
- Primary + backup window only if Agreement permits
- Confirm site-specific restrictions (noise ordinances, HOA rules, permit windows)

### Step 4: Identify Entrants and Equipment

- Detail level per Agreement (named individuals vs. company + supervisor)
- Omit unnecessary personal data unless Agreement requires it
- Equipment descriptions must be honest and complete — under-disclosure appears deceptive
- Reference restoration/safety provisions for heavy equipment or invasive activities

### Step 5: Confirm Insurance

- COIs verified and in hand → state compliance and attach
- COIs pending → state intention and timing; do NOT represent coverage as confirmed
- Include policy types/limits only if verified from the certificate
- **Never state "fully insured"** without confirming terms against Agreement requirements

### Step 6: Assemble the Notice

Use this structure:

[Date]

[Recipient Name and Address per Notice Clause]

Re: Notice of Entry — [Agreement Title] dated [Date] — [Property Address]

Pursuant to Section [__] of the [Agreement Title] dated [Date] between
[Entering Party] and [Owner] (the "Agreement"), this letter constitutes
[lead time] advance written notice of Entering Party's intended entry
onto the property located at [Address] (the "Property").

DATE AND TIME OF ENTRY.
[Day, Date], arrival at approximately [time] [time zone], with
anticipated completion by [time].

PURPOSE AND SCOPE.
Entry will be for the limited purpose(s) authorized under Section [__]
of the Agreement, specifically: [describe activities]. No activities
outside the scope of the Agreement are intended.

AREAS TO BE ACCESSED.
Personnel will access only the following areas: [describe with exhibit
references].

PERSONNEL AND CONTRACTORS.
[List with roles and company affiliations]. The onsite supervisor will
be [Name], reachable at [phone].

EQUIPMENT AND VEHICLES.
[Describe]. [Vehicle information if required].

INSURANCE.
Entering Party confirms compliance with the insurance requirements of
Section [__] of the Agreement. [Certificate(s) attached as Exhibit [__]
/ previously provided on [date]].

Please advise promptly if the Property requires a specific check-in
procedure, escort, or safety orientation. Absent written objection on a
basis permitted by the Agreement, Entering Party intends to proceed as
noticed.

Sincerely,

[Name / Title / Contact Information]

cc: [All parties required by notice clause]
Enclosures: [COIs; Site Plan if applicable]

### Step 7: Adversarial-Proof and Finalize

- [ ] No unnecessary admissions (liability, causation, ownership of conditions)
- [ ] No promises beyond contractual obligations
- [ ] No privileged strategy, settlement positions, or sensitive information
- [ ] Language tethered to Agreement terms throughout
- [ ] Delivery via all methods required by Agreement; recommend redundant delivery for high-stakes entries

## Checkpoint B: Post-Draft Alignment

After delivering the draft, ask:

1. Does the entry window comply with the notice period counting business days?
2. Are all activities within the Agreement's permitted scope?
3. Are COIs current and matching Agreement insurance requirements?
4. Is there a lender, property manager, or tenant who must receive a copy?

If no response, recommend verifying the calendar calculation (most common failure) and proceed if authorized.

## Quality Audit

| Check | Verify |
|---|---|
| **Calendar** | Receipt-to-entry interval meets/exceeds contractual requirement (business days, weekends, holidays) |
| **Scope** | Every activity within Agreement's permitted activities |
| **Recipient** | Addressee and delivery method match notice clause; all cc parties included |
| **Insurance** | COI attached, limits match, correct additional insureds and endorsements |
| **Contact** | Onsite point of contact provided |
| **Facts** | Every assertion confirmed by user inputs or documentation |
| **Tone** | Firm notice asserting rights — not requesting permission, not argumentative |
| **Format** | Clear subject line, Agreement reference, consistent defined terms, clean signature block |

## Pitfalls and Checks

**Jurisdiction notes:**

| Jurisdiction | Consideration |
|---|---|
| California | Cal. Civ. Code § 1954: 24-hour statutory notice for residential landlord entry. Commercial access governed by contract. |
| New York | RPAPL § 881 `[VERIFY]`: summary proceeding for license to enter adjoining property. |
| Texas | Strict property rights; entries risking permanent land injury need clear remediation plans. |
| Federal environmental | CERCLA entries (42 U.S.C. § 9604(e)) must cite statutory authority or docket number. |

**Anti-hallucination rules:**
- Never fabricate lead times, policy limits, scope permissions, or legal citations
- Mark unverified statutes with `[VERIFY]`
- Never invent Agreement terms or section numbers

**Operational rules:**
- Flag statutory overlays (environmental regs, asbestos/lead paint, tenant notice statutes) for regulated activities
- If entry plan changes post-notice, determine whether Agreement requires revised/supplemental notice
- Preserve full record: notice, delivery confirmations, attachments, responses
