---
name: in-draft-motion-codearranger
title: Draft an Indiana Motion (with Memorandum of Law)
description: 'This skill should be used when the user asks to "draft an Indiana motion", "Indiana motion to dismiss", "Indiana motion to compel", "Indiana summary judgment", "T.R. 56 motion", "Indiana motion to vacate", "T.R. 60(B) motion", "Indiana motion to correct error", "T.R. 59 motion", "Indiana memo of law", "Indiana memorandum in support", or any other Indiana motion-drafting request. Scaffolds the motion + memorandum + supporting declaration + proposed order packet under Indiana Trial Rule 7 with the caption from T.R. 10(A), signature block from T.R. 11(A), and verification under T.R. 11(B) where required. Trigger phrases: "Indiana motion", "T.R. 7 motion", "T.R. 12(B)(6) motion", "T.R. 56 summary judgment", "T.R. 59 motion to correct error", "T.R. 60(B) motion", "Indiana memorandum in support".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-draft-motion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Indiana Motion (with Memorandum of Law)

This is the scaffolder for any motion filed in an Indiana civil
court. It produces a four-document packet:

1. **Motion** — the operative request for relief
2. **Memorandum in Support** — the legal argument
3. **Declaration (or Affidavit)** — any sworn factual predicate
4. **Proposed Order** — the order the judge will sign if granted

Marion CPC § II.A and most Indiana county local rules require a
proposed order to accompany any motion. The court typically will
not rule without one.

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify each cited rule, statute, and case against current
> sources before filing.

## Motion structure — Trial Rule 7(B)

T.R. 7(B) requires every motion to:

- State the relief sought "with particularity"
- State the grounds for the relief

Indiana practice splits the motion into two documents: the
**Motion** itself (1-3 pages, stating the request and grounds)
and a **Memorandum in Support** (longer, with the legal argument
and case law). This is the convention even though T.R. 7 does not
strictly require separation.

## Scaffolded motion document

```
                     STATE OF INDIANA
                  IN THE [COURT NAME] COURT
              [COUNTY NAME] COUNTY, INDIANA

[PLAINTIFF NAME],                   )
                                    )
            Plaintiff,              )    Cause No. [###]
                                    )
        v.                          )
                                    )
[DEFENDANT NAME],                   )
                                    )
            Defendant.              )

      DEFENDANT'S MOTION TO [RELIEF] UNDER TRIAL RULE [#]

   Defendant [NAME], by counsel / pro se, respectfully moves
this Court for an order [RELIEF] pursuant to Indiana Trial Rule
[#]. In support, Defendant states:

   1. [Procedural posture — e.g., "On [date], Plaintiff filed
      its Complaint, and Defendant was served on [date]."]

   2. [Why the relief is warranted — concise factual basis
      tied to legal grounds]

   3. [Legal authority — cite the controlling rule, statute,
      or case]

   4. A memorandum in support is filed contemporaneously.

   5. A proposed order is submitted herewith.

   WHEREFORE, Defendant respectfully requests the Court [GRANT
RELIEF], and for any further relief the Court deems just.

                              Respectfully submitted,


                              _______________________________
                              [SIGNER NAME], [Pro Se / Atty. No.]
                              [Street Address]
                              [City, IN ZIP]
                              Telephone: (___) ___-____
                              Email: ________________________


                       CERTIFICATE OF SERVICE

I certify that on [DATE] a copy of the foregoing was served via
the Indiana E-Filing System on all counsel of record.

                              _______________________________
                              [SIGNER NAME]
```

## Memorandum in Support — scaffold

```
                     STATE OF INDIANA
                  IN THE [COURT NAME] COURT
              [COUNTY NAME] COUNTY, INDIANA

[PLAINTIFF NAME],                   )
                                    )
            Plaintiff,              )    Cause No. [###]
                                    )
        v.                          )
                                    )
[DEFENDANT NAME],                   )
                                    )
            Defendant.              )

   MEMORANDUM IN SUPPORT OF DEFENDANT'S MOTION TO [RELIEF]

                       I. INTRODUCTION

   [1-2 paragraphs framing the motion. State what relief is
sought, the rule supporting it, and the headline reason.]

                    II. STATEMENT OF FACTS

   1. [Numbered paragraph stating the first material fact, with
      a citation to the supporting declaration or exhibit:
      "(Decl. ¶ 3; Ex. A)."]

   2. [Second fact.]

   3. [Third fact, etc.]

                       III. ARGUMENT

A.  [Heading 1 — the first legal proposition.]

   [Paragraph stating the proposition + binding authority.
   "Under Trial Rule X, [proposition]. The Indiana Supreme Court
   confirmed this in *Smith v. Jones*, 123 N.E.3d 456, 462 (Ind.
   2023). Here, [application]."]

B.  [Heading 2 — the second legal proposition.]

   ...

                       IV. CONCLUSION

   For the foregoing reasons, Defendant respectfully requests
the Court [GRANT RELIEF].

                              Respectfully submitted,


                              _______________________________
                              [SIGNER NAME], [Pro Se / Atty. No.]
```

## Page limits

Indiana does NOT set statewide page limits on memoranda. Local
practice:

- **Marion Civil Division (LR49-TR5-203)**: chambers-copy
  threshold at 15 pages, but no hard cap. Most motions stay
  under 15 pages by convention.
- **Lake County (LR45-TR5)**: chambers-copy threshold at 20
  pages.
- **Hamilton County (LR29-TR5)**: chambers-copy threshold at 15
  pages.
- Other counties: typically 15-25 pages by local convention.

For motions exceeding the chambers-copy threshold, follow the
chambers-copy delivery protocol in the venue skill (e.g.,
`in-marion` § "Chambers copies — when and how").

## Motion types — pattern variations

### T.R. 12(B)(6) — Motion to Dismiss for Failure to State a Claim

- Title: "DEFENDANT'S MOTION TO DISMISS UNDER TRIAL RULE
  12(B)(6)"
- Standard: accept all well-pleaded allegations as true; ask
  whether under any conceivable set of facts the plaintiff would
  be entitled to relief (*Trail v. Boys & Girls Clubs of
  Northwest Ind.*, 845 N.E.2d 130 (Ind. 2006))
- No need for declaration — confined to the four corners of the
  Complaint
- Outside-the-pleadings exhibits will convert the motion to T.R.
  56 (summary judgment)

### T.R. 56 — Motion for Summary Judgment

- Title: "DEFENDANT'S MOTION FOR SUMMARY JUDGMENT"
- **Critical Indiana-specific point**: Indiana applies the
  *Jarboe* burden — the movant must AFFIRMATIVELY NEGATE an
  element with admissible evidence, not just point to absence of
  evidence in the record. *Jarboe v. Landmark Cmty. Newspapers*,
  644 N.E.2d 118 (Ind. 1994); reaffirmed *Hughley v. State*, 15
  N.E.3d 1000 (Ind. 2014).
- Indiana **rejected** the federal *Celotex* "show the absence
  of evidence" approach.
- Must include a "Statement of Material Facts Not in Genuine
  Dispute" with paragraph-numbered facts, each citing a sworn
  declaration or exhibit (T.R. 56(C)).
- Response deadline: 30 days from service of motion (T.R.
  56(C)).
- Hearing: usually within 60 days; the court must hold a hearing
  if requested (T.R. 56(C)).

### T.R. 37(A) — Motion to Compel

- Title: "DEFENDANT'S MOTION TO COMPEL RESPONSES TO REQUESTS FOR
  PRODUCTION"
- Must include T.R. 37(E) meet-and-confer certificate
- Recite each unanswered discovery request with the alleged
  defect

### T.R. 60(B) — Motion for Relief from Judgment

- Title: "DEFENDANT'S MOTION FOR RELIEF FROM JUDGMENT UNDER
  TRIAL RULE 60(B)(1)"
- Required showing: (1) excusable neglect or other T.R. 60(B)
  ground + (2) meritorious defense
- Filed in the trial court (not the Court of Appeals)
- Outer deadline: 1 year for grounds (1), (2), (3); "reasonable
  time" for (4)-(8)

### T.R. 59 — Motion to Correct Error

- Title: "DEFENDANT'S MOTION TO CORRECT ERROR (TRIAL RULE 59)"
- **30-day jurisdictional deadline from final judgment**
- Must state with specificity the alleged errors
- Court has 45 days to rule (T.R. 59(B)) or motion is deemed
  denied

## Verification — when required

Most motions do NOT require a verified motion. Exceptions:

- T.R. 65 preliminary injunction (verified petition)
- IC 34-26-5 protective order petition
- T.R. 69 proceedings supplemental motion
- T.R. 12(B)(2) lack of personal jurisdiction (when challenging
  the affidavit of service)

For verified motions, the signer affirms under penalties for
perjury per IC 35-44.1-2-1: "I affirm, under the penalties for
perjury, that the foregoing representations are true."

## Composition

- `in-statewide-format` for T.R. 5(E) format + T.R. 10 caption
- `in-marion` / `in-lake` / `in-county-courts` for venue + local
  rules
- `in-pro-se` for self-represented signature block
- `in-draft-declaration` for the supporting declaration
- `in-draft-order` for the proposed order
- `in-fact-check` for the pre-filing citation audit
- `in-quality-check` for the final QC

## References

- `references/motion-template.md` — full motion + memo + decl +
  order packet for a T.R. 12(B)(6) motion
- `references/sj-template.md` — T.R. 56 summary judgment packet
  with Jarboe burden language
- `references/motion-to-compel-template.md` — T.R. 37(A) packet
  with meet-and-confer certificate
- `references/tr60-motion-template.md` — T.R. 60(B)(1) motion
  to vacate default
- `references/tr59-motion-template.md` — T.R. 59 motion to
  correct error

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
