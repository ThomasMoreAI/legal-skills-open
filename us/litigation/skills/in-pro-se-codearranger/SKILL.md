---
name: in-pro-se-codearranger
title: Pro Se Drafting and Procedure for Indiana Courts
description: 'Use for self-represented (pro se) litigants in Indiana courts. Covers **pro se framework**, **service under Trial Rule 4**, **Parker procedural protocol**, **T.R. 11(A) pro se signature**, ***Goossens v. Goossens* equal-standards doctrine** (pro se held to same rules as counsel), fee waivers under **IC 33-37-3-2**, Odyssey e-filing, and county Self-Help Centers. Triggers: "pro se Indiana", "Indiana self-represented", "Indiana pro se appearance", "Trial Rule 4 service", "Indiana fee waiver", "indiana self-help center".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-pro-se
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Pro Se Drafting and Procedure for Indiana Courts

This skill carries the conventions, forms, and procedural pitfalls
specific to self-represented (pro se) civil litigants in Indiana
trial courts. Apply it whenever the filer is not represented by
counsel — whether plaintiff or defendant — and the document is
being prepared for filing in a Circuit Court, Superior Court,
County Court, or township small-claims court.

> **NOT LEGAL ADVICE.** Generated content is a drafting aid; pro
> se litigants are held to the same procedural standards as
> attorneys (*Goossens v. Goossens*, 829 N.E.2d 36, 43 (Ind. Ct.
> App. 2005)). Always verify rule numbers, deadlines, and case-
> specific requirements against the current Indiana Trial Rules
> and the venue court's local rules before filing. For complex
> matters, or matters with substantial sums at stake, consider
> consulting a licensed Indiana attorney.

## The two pro se ground rules

### Rule 1: You are held to the same procedural standards as a lawyer.

*Goossens v. Goossens*, 829 N.E.2d 36, 43 (Ind. Ct. App. 2005),
holds that "pro se litigants are held to the same standards as
licensed attorneys" — and Indiana courts have consistently applied
this doctrine. The court does not waive deadline rules, format
rules, service rules, or evidentiary requirements because the
filer is pro se. Missing the 20-day answer window under T.R. 6(C)
results in default judgment under T.R. 55, regardless of whether
the defendant had a lawyer.

Plan accordingly:

- Always know your next deadline before leaving court
- E-file or hand-deliver everything — never rely on mail without a
  fallback plan
- Use the format-check.py script in this plugin to validate every
  filing against T.R. 5(E) before upload

### Rule 2: The court will not give you legal advice.

Clerks, judicial assistants, and judges cannot tell you:

- Whether to file a motion
- What defenses to assert
- How to phrase an argument
- Whether your case is winnable

They CAN tell you:

- The next available hearing date
- Whether a particular form exists
- The filing fee
- Where to find the Self-Help Center
- The case number

This is the **Indiana Code of Judicial Conduct Canon 2 / Rule 2.4
boundary** — judges and court staff must remain neutral. Plan to
gather substantive guidance from:

- The Indiana Pro Bono Commission (`probono.indianabar.org`)
- The Indiana State Bar Association's Modest Means Program
- The Marion County Self-Service Center at the City-County
  Building
- Indiana Legal Services (`indianalegalservices.org`) — free
  representation for income-qualified parties
- Public Law Library (most county courthouses have one)

## The Parker framework — adapted for Indiana

The "Parker framework" is a step-by-step civil-procedure protocol
that pro se litigants can apply to any motion or filing. Adapted
to Indiana:

1. **Identify the procedural posture.** What stage of the case is
   this? Pre-answer? Discovery? Post-judgment? The applicable rule
   depends on this.
2. **Find the controlling rule.** Indiana Trial Rules first, then
   the venue county's local rules. For example, a motion to
   compel discovery: T.R. 37 (statewide) + LR49-TR37 (Marion
   local) or LR45-TR37 (Lake local).
3. **Find the controlling statute** (if any). Some procedures are
   driven by statute, not rule — garnishment (IC 24-4.5), small
   claims (IC 33-29-2 or IC 33-34), filing fees (IC 33-37-4-4).
4. **Find the controlling case law.** The Indiana Supreme Court
   and Court of Appeals issue interpretive decisions. Use
   `in-fact-check` to verify any case citation.
5. **Compute the deadline.** Use `in-deadlines` and the bundled
   `case-calendar.py` script for T.R. 6 deadline math.
6. **Draft the document.** Use one of the four scaffolders
   (`in-draft-motion`, `in-draft-declaration`, `in-draft-note`,
   `in-draft-order`).
7. **Quality-check** with `in-quality-check`.
8. **Assemble the packet** with `in-file-packet`.
9. **Submit** through Odyssey or the appropriate paper-filing
   protocol.
10. **Calendar** the next deadline and the response window.

## Signature block — Indiana pro se convention

T.R. 11(A) requires every paper to be signed at the end. The pro
se signature block:

```
                              Respectfully submitted,


                              _______________________________
                              [PARTY NAME], Pro Se
                              [Street Address]
                              [City, IN ZIP]
                              Telephone: (___) ___-____
                              Email: ________________________
```

Key points:

- Write "Pro Se" (not "in pro per" — that's California) after
  the name, on the same line
- Phone number is required; email is required if you are
  registered for Odyssey e-filing
- Indiana does NOT require an Attorney Number for pro se filers
  (the "Atty. No." line is for licensed attorneys only)
- Email address must be the same as the address on file with
  Odyssey

## Appearance form (T.R. 3.1)

Indiana Trial Rule 3.1 requires every party to file a formal
"Appearance" at or before the time of the party's first
substantive filing. The Appearance form provides the court with:

- The party's name and contact information
- The party's pro se or attorney status
- The party's preferred service method (email + mailing address)
- Any related-case information

Marion uses the Marion-specific Appearance form (LR49-TR3.1);
Lake uses LR45-TR3.1; other counties have their own. The
**statewide form** is also available at courts.in.gov/forms — file
the statewide form unless the county has rejected it (none have,
to date).

For pro se defendants, the Appearance is filed simultaneously
with the Answer (typically as a single Odyssey transmission).

## Service of process — Trial Rule 4

T.R. 4 governs how a complaint must be served on the defendant.
The most common methods:

- **Personal service** (T.R. 4.1) — by Sheriff or a private
  process server appointed under T.R. 4.12. Costs $30-50.
- **Service by certified mail with return receipt requested** —
  the cheapest method ($8-10). The signed green card returns to
  the Clerk's office and triggers the 20-day answer window.
- **Service by publication** (T.R. 4.13) — used only when the
  defendant cannot be located. Requires an affidavit of diligence
  before the court will authorize.

Notes:

- The 20-day answer window starts on the date the green card is
  signed, NOT the date you mailed the certified packet.
- Service must include the Summons AND the Complaint together.
- A pro se plaintiff who serves by certified mail must file a
  Return of Service through Odyssey after the green card returns,
  using document code 25001 (Return of Service).

## Fee waivers — proceeding in forma pauperis

IC 33-37-3-2 (the **Affidavit of Indigency**) allows a pro se
filer to proceed without paying filing fees if income is at or
below 125% of the federal poverty line. The form is **CCS Form
1042** (Indiana Office of Judicial Administration Approved Form);
it must be filed with the initial complaint or answer.

Required showings:

- Household size and gross monthly income
- Liquid assets (cash, bank accounts)
- A statement of why the fee would impose hardship

The judge rules on the petition within a few days. If granted,
the filing fee, e-filing fee, and Sheriff service fee are all
waived. If denied, the petitioner may pay the fee and proceed.

## Odyssey e-filing for pro se filers

Indiana Administrative Rule 16 permits but does not require pro
se e-filing. Steps:

1. Register a free Odyssey account at `efile.courts.in.gov`
2. Verify email
3. Add the case to your account (using the cause number)
4. Upload the PDF of your document
5. Select the correct document code from the dropdown
6. Pay the e-filing fee ($10-15 transaction fee) or claim
   indigency
7. The system serves all registered Service Contacts
   automatically

For pro se filers who prefer paper filing: every Indiana county
clerk's office accepts paper filings during business hours. The
clerk will stamp the original, return a file-stamped copy to the
filer, and route the original to the assigned courtroom.

## Self-Help Centers — county directory

Many counties operate a **Self-Help Center** or **Pro Se
Resource Center** to help self-represented litigants navigate the
court system. Notable:

- **Marion County Self-Service Center** — City-County Building,
  Suite W-122; (317) 327-3506. Hours: M-F 8 AM - 4 PM. Provides
  form completion assistance for divorce, custody, small claims,
  and protective orders.
- **Allen County Self-Help Center** — Allen County Courthouse,
  Room 411. Limited form-completion assistance.
- **Indianapolis Bar Foundation Modest Means** — referral service
  for limited-scope representation.
- **Indiana Legal Services** — statewide; income-qualified
  free legal aid.

The Indiana Office of Judicial Administration maintains an
**eFiling Help Desk** at (317) 232-1313 for technical Odyssey
issues.

## Common pro se pitfalls — and how to avoid them

| Pitfall | Avoid by ... |
|---------|--------------|
| Missing the 20-day answer window | Calendar `T.R. 6(C)` deadline immediately on receipt of the Summons |
| Failing to file an Appearance | File the LR49-TR3.1 / LR45-TR3.1 / statewide Appearance with your first filing |
| Submitting an unsigned filing | Every PDF must show your wet or `/s/` signature on the last page (T.R. 11(A)) |
| Forgetting the proposed order | Marion CPC § II.A requires every motion to include a proposed order; without one the court may decline to rule |
| Wrong document code in Odyssey | Cross-reference with the Marion or Lake document-code reference |
| Email address out of date | Update Service Contacts whenever you change email — missed orders are not excused |
| Missing the chambers copy threshold | Marion: >15 pages; Lake: >20 pages — deliver paper chambers copy within 24 hours |
| Filing without a Certificate of Service | T.R. 5(B) requires service on every other party; include the Certificate of Service in the body |
| Citing rules without verification | Use `in-fact-check` and cross-check the current Indiana Trial Rules — they're amended frequently |

## Composition — which skills layer here

- `in-statewide-format` for T.R. 5(E) / T.R. 10 baseline
- `in-marion` / `in-lake` / `in-county-courts` for venue-specific
  Self-Help Centers and local rules
- `in-discovery` for pro se discovery scope and limits
- `in-deadlines` for T.R. 6 calculation
- `in-draft-motion` / `in-draft-declaration` / `in-draft-note` /
  `in-draft-order` for the scaffolders
- `in-file-packet` for packet assembly
- `in-consumer-debt` if you are a consumer-debt defendant —
  Indiana's consumer-protection statutes (DCSA) are favorable

## References

- `references/appearance-form.md` — T.R. 3.1 Appearance with
  the statewide form
- `references/affidavit-indigency.md` — CCS Form 1042 walkthrough
- `references/service-of-process.md` — T.R. 4 service options
- `references/self-help-centers.md` — directory of county
  Self-Help Centers
- `references/parker-framework.md` — Indiana-specific Parker
  protocol

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
