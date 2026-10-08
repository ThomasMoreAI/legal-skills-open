---
name: consular-visa-refusal-codearranger
title: Consular Visa Refusal — Department of State
description: 'Use this skill when a visa application was REFUSED at a U.S. consulate (a Department of State forum — NOT USCIS or immigration court). Identifies refusal type from refusal sheet — INA § 221(g) administrative-processing hold (curable by submitting missing document) versus INA § 212(a) ineligibility ground. Maps waivers: Form I-601, I-601A (unlawful-presence provisional), § 212(d)(3) nonimmigrant. Triggers: "visa refused", "221g", "administrative processing", "consulate denied my visa", "212a ineligibility", "I-601 waiver", "I-601A", "unlawful presence bar", "misrepresentation visa", "supervisory review", "what to do after visa denial", "DS-260 refused". Produces § 221(g) document-submission letter, waiver-assembly checklist, reconsideration letter to post. Warns: there is generally no court appeal of consular refusal.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-immigration-laws/skills/consular-visa-refusal
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Consular Visa Refusal — Department of State

> **NOT LEGAL ADVICE.** This skill produces drafting aids, checklists, and document
> scaffolds — **not legal advice**, and no attorney-client relationship is created. A
> consular refusal can carry a multi-year or permanent bar to reentry; a misstep on a
> waiver or an admission of a misrepresentation can foreclose options. Verify every
> ground, form edition, and deadline against current law, and **strongly consider a
> licensed immigration attorney** before submitting anything. Start with
> `immigration-pro-se` if you have not confirmed the forum.

## The consular forum

A visa applied for **abroad** (DS-160 for a nonimmigrant visa, DS-260 for an immigrant
visa) is adjudicated by a **consular officer** of the Department of State, governed by the
**INA**, the State Department regulations at **22 CFR Parts 40–42**, and the agency's
internal guidance in the **9 FAM**. This is a different forum from USCIS (benefits) and
EOIR (removal). Under **INA § 221(g)** every refused applicant is handed (or emailed) a
**refusal sheet** citing the section(s) of law the officer applied — read it first; it
tells you which path below applies.

> **FAM is agency guidance, not binding law.** The 9 FAM tells consular officers how the
> Department reads the statute, but it does not bind a court and is not itself the ground
> of refusal. **Always pair a FAM cite with the controlling INA § 212 / 22 CFR provision**
> that actually states the ground or the waiver. Cite, e.g., "INA § 212(a)(6)(C)(i)
> (8 U.S.C. § 1182(a)(6)(C)(i)); see 9 FAM 302.9" — never the FAM alone.

## § 221(g) vs. § 212(a) — read the refusal sheet

| | **INA § 221(g)** "refusal" | **INA § 212(a)** ineligibility |
|---|---|---|
| What it means | Application is **incomplete** or needs more review ("administrative processing") | A **substantive inadmissibility** ground applies to the applicant |
| Typical cause | Missing document, missing form, pending security/name check, requested evidence | Unlawful presence, misrepresentation, criminal record, public charge, prior removal |
| Curable how | **Submit the missing item / information** to the post — usually resolves it | Generally needs a **waiver** (if one exists) or the passage of time |
| Authority | INA § 221(g) (8 U.S.C. § 1201(g)); 22 CFR 41.121 / 42.81; 9 FAM 302.1 (212(a)(7)/221(g) doc grounds) | INA § 212(a) (8 U.S.C. § 1182(a)); 22 CFR 40.x; 9 FAM 302.2–302.14 |
| Status | A **"quasi-refusal"** that stays open pending the missing piece | A refusal on the merits; the case is decided unless a waiver clears it |

A § 221(g) hold is the common one and is **usually fixable by supplying what was asked
for** — gather the requested document, transcribe the case/refusal number exactly, and
submit it through the post's stated channel. The § 221(g) cover letter this skill drafts
itemizes each requested item against an enclosure index.

## The § 212(a) ineligibility framework and waivers

The substantive grounds live in **INA § 212(a) (8 U.S.C. § 1182(a))** and are applied by
consular officers per **9 FAM 302.2–302.14**, paired with the **22 CFR Part 40** subparts:

| Common ground | INA cite | FAM | Waiver path |
|---|---|---|---|
| Unlawful presence (3-yr / 10-yr / permanent bar) | § 212(a)(9)(B)–(C) | 9 FAM 302.11 | I-601 (or **I-601A** provisional, before departure); none for permanent bar w/o 10-yr wait |
| Misrepresentation / fraud | § 212(a)(6)(C)(i) | 9 FAM 302.9 | I-601 under § 212(i); § 212(d)(3) for NIV |
| Criminal grounds (CIMT, controlled substance) | § 212(a)(2) | 9 FAM 302.3–302.4 | I-601 under § 212(h); § 212(d)(3) for NIV |
| Public charge | § 212(a)(4) | 9 FAM 302.8 | no formal waiver; cured by sufficient I-864 / circumstances |
| Prior removal | § 212(a)(9)(A) | 9 FAM 302.11 | Form I-212 (consent to reapply) |

**Waiver instruments:**

- **Form I-601, Application for Waiver of Grounds of Inadmissibility** — the general
  inadmissibility waiver (e.g., § 212(h) criminal, § 212(i) fraud, certain § 212(a)(9)(B)
  unlawful-presence cases), usually requiring **extreme hardship** to a qualifying U.S.
  citizen / LPR relative. Filed with **USCIS**, not the consulate.
- **Form I-601A, Provisional Unlawful Presence Waiver** — waives **only** the
  § 212(a)(9)(B) unlawful-presence bar, **before** the applicant departs for the interview,
  so the bar does not strand them abroad. Filed with USCIS while still in the U.S.; the
  consular interview follows approval.
- **INA § 212(d)(3)(A) nonimmigrant waiver (8 U.S.C. § 1182(d)(3))** — a discretionary
  waiver for most grounds for a **nonimmigrant** visa applicant; the consular officer
  recommends it and CBP's Admissibility Review Office adjudicates. See 8 CFR Part 212 for
  the documentary-requirements / waiver framework and 9 FAM 302 for the field standard.

Which waiver (if any) exists depends on the exact ground and the visa type; confirm the
controlling INA § 212 subsection against the corpus before assuming a waiver is available.

## Consular nonreviewability — and what you actually can do

**There is generally NO appeal of a consular refusal to a court.** The doctrine of
**consular nonreviewability** means a federal court will not second-guess a consular
officer's visa decision. Do not draft a "court appeal" of a consular refusal. The real
avenues are administrative:

1. **Submit the § 221(g) item.** If the refusal sheet asks for a document or information,
   the fastest cure is to provide it through the post's stated channel. (This skill's
   § 221(g) cover letter.)
2. **Request reconsideration / supervisory review at the post.** Under **22 CFR 41.121(c)
   (NIV)** and **22 CFR 42.81(c) (IV)**, a refusal is reviewed — and may be referred to a
   supervisory officer. A concise, respectful letter to the post identifying a factual
   error or new evidence is the vehicle. (This skill's reconsideration letter.)
3. **LegalNet / Visa Office advisory opinion.** For a **legal-interpretation** question
   (how the law applies to the facts — not the discretionary merits), the Department's
   **Visa Office (LegalNet)** advisory-opinion channel can be raised, typically through the
   post or counsel. It addresses interpretation of law, not the officer's discretion.

Reconsideration is **not** an appeal and the post is not obligated to change its decision;
frame it as new facts / legal error, never as a demand.

## Artifacts this skill drafts

- A **§ 221(g) document-submission cover letter** — caption with the post, case/refusal
  number, applicant name and DOB; an enclosure index mapping each requested item; a
  one-line statement that the submission responds to the § 221(g) request.
- A **waiver-assembly checklist** — selects **I-601 / I-601A / § 212(d)(3)** by ground and
  visa type; lists the qualifying relative, the extreme-hardship evidence categories, and
  the filing destination (USCIS vs. ARO via the post).
- A **request-for-reconsideration / supervisory-review letter** to the post — states the
  specific factual error or new evidence, cites the controlling INA § 212 / 22 CFR
  provision (with the FAM as supporting guidance), and requests supervisory review under
  22 CFR 41.121(c) / 42.81(c).

## Related authority

- INA § 212 inadmissibility + waivers (8 U.S.C. § 1182) and INA § 221(g) (8 U.S.C.
  § 1201(g)): [`../../references/immigration-statutes/INA-II-immigration.md`](../../references/immigration-statutes/INA-II-immigration.md)
  (use the INA ↔ 8 U.S.C. crosswalk in
  [`../../references/immigration-statutes/README.md`](../../references/immigration-statutes/README.md)).
- State Dept. regulations: [`../../references/immigration-regulations/22CFR-040-visas-general.md`](../../references/immigration-regulations/22CFR-040-visas-general.md),
  [`../../references/immigration-regulations/22CFR-041-nonimmigrant-visas.md`](../../references/immigration-regulations/22CFR-041-nonimmigrant-visas.md),
  [`../../references/immigration-regulations/22CFR-042-immigrant-visas.md`](../../references/immigration-regulations/22CFR-042-immigrant-visas.md).
- Waiver / documentary framework: [`../../references/immigration-regulations/8CFR-212-inadmissibility.md`](../../references/immigration-regulations/8CFR-212-inadmissibility.md).
- FAM guidance (pair with the statute/CFR above): ineligibilities + waivers
  [`../../references/foreign-affairs-manual/09FAM-302-ineligibilities.md`](../../references/foreign-affairs-manual/09FAM-302-ineligibilities.md)
  (302.1 doc/221(g); 302.3–302.4 criminal; 302.9 misrepresentation; 302.11 unlawful
  presence / prior removal); NIV classifications
  [`../../references/foreign-affairs-manual/09FAM-402-niv-classifications.md`](../../references/foreign-affairs-manual/09FAM-402-niv-classifications.md);
  IV categories + processing
  [`../../references/foreign-affairs-manual/09FAM-502-504-iv-processing.md`](../../references/foreign-affairs-manual/09FAM-502-504-iv-processing.md);
  visas overview
  [`../../references/foreign-affairs-manual/09FAM-visas-overview.md`](../../references/foreign-affairs-manual/09FAM-visas-overview.md).

## Composition

Routed to from `immigration-pro-se` (which confirms this is the Department of State forum,
not USCIS or EOIR). Use `uscis-benefit-requests` to assemble and file the **I-601 / I-601A**
waiver packets, which are USCIS filings even though the refusal is consular. Run
`immigration-fact-check` to verify every INA § 212 / 22 CFR cite and to confirm each FAM
cite is paired with controlling law. Run `immigration-deadlines` for the one-year § 221(g)
follow-up clock (22 CFR 41.121(a) / 42.81(e) — failure to pursue within one year may
require a new application) and any waiver / reapplication timing.
