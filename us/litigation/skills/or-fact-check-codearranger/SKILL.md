---
name: or-fact-check-codearranger
title: Fact-Check Oregon Court Filings
description: 'Use this skill to fact-check Oregon court filings before filing. Triggers include "fact check", "verify citations", "check my citations", "consistency check", "audit this filing", "cite- check", "check for hallucinations". Runs four passes: (1) **citation verification** — every Or / Or App / P2d / P3d / US / S Ct / F / F3d / ORS / ORCP / OEC cite resolves to a real source; (2) **internal consistency** — dates, party names, cause number, amounts agree within document; (3) **packet consistency** — caption, parties agree across motion, declaration, order, notice; (4) **sworn-vs.-argued consistency** — no motion fact contradicts declaration. Uses canonical URLs in online-sources catalog. Composes with or-quality-check, or-law-references, and draft-* skills. **Verification only** — flags issues; does not rewrite.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-fact-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fact-Check Oregon Court Filings

Use this skill to verify Oregon court filings (or packets of
filings) before filing. The agent runs four passes and outputs
a report. The user reviews the report and accepts or rejects
each suggested correction.

> **NOT LEGAL ADVICE.** Fact-checking verifies the surface — it
> doesn't tell you whether the legal position is winning. Pair
> with substantive review by counsel where stakes warrant.

## When to invoke

Before filing any of:

- Motion (any type)
- Memorandum in support
- Declaration with exhibits
- Proposed Order
- Notice of Hearing
- Answer with affirmative defenses and counterclaims
- Brief on appeal

For a multi-document packet (motion + memo + decl + order +
notice), invoke once and check the whole packet for cross-
document consistency.

## The four passes

### Pass 1: Citation verification

Every cite in the filing resolves to a real source. The cite
patterns:

- **Oregon cases**: `[Party] v. [Party], [vol] Or [page], [vol]
  P2d/P3d [page] ([year])` — verify against CourtListener
- **Court of Appeals**: same pattern, `Or App` reporter
- **9th Circuit / federal**: `F`, `F2d`, `F3d`, `F Supp`, etc.
  — verify against CourtListener
- **Supreme Court**: `US`, `S Ct` — verify against
  CourtListener
- **ORS**: `ORS [Ch].[section]([subsection])` — verify against
  oregonlegislature.gov
- **ORCP**: `ORCP [N] [Letter]([number])` — verify against
  counciloncourtprocedures.org
- **OEC**: `OEC [N]([number])` — verify against
  oregonlegislature.gov (ORS Ch. 40)
- **UTCR**: `UTCR [N].[NNN]([N])` — verify against
  courts.oregon.gov/rules/UTCR
- **Local SLR**: `[County] SLR [N].[NNN]` — verify against the
  county's rules page
- **USC**: `[title] USC § [section]([sub])` — verify against
  uscode.house.gov
- **CFR**: `[title] CFR § [N].[NN]` — verify against ecfr.gov

For each cite:

1. **Resolve**: does the cite exist?
2. **Quote**: if the filing quotes the source, does the quote
   match?
3. **Holding**: if the filing relies on a case for a
   proposition, does the case actually stand for that
   proposition?
4. **Currency**: has the case been overruled or
   distinguished? Has the statute been amended? Is the rule
   number still in use?

Use WebFetch against the canonical URLs in
`or-law-references/references/online-sources.md`. Do not use
other fetch mechanisms.

#### Common Oregon citation errors to flag

| Pattern | Error |
|---------|-------|
| `Or.` (with period) | Oregon Style Manual uses `Or` without period |
| `P.3d` (with periods) | Oregon style is `P3d` |
| `U.S.C.` (with periods) | Oregon style is `USC` |
| `vs.` | Oregon uses `v.` |
| `Rule 12(b)(6)` or `CR 12(b)(6)` | Oregon uses `ORCP 21 A(8)` |
| `Wn.2d` or `Wn. App.` | Washington reporter — wrong jurisdiction |
| `CR 56` | Washington rule — Oregon is `ORCP 47` |
| `KCDC` or `KCSC` | Washington courts — wrong jurisdiction |
| `RCW [N.NN]` | Washington statutes — Oregon is `ORS [N.NNN]` |
| Lettered exhibits (A, B, C) | Oregon convention is numbered |
| `Exhibit A at page 5` | Should be `Exhibit 1 at p. 5` |
| Static "Page 5 of 12" | Must use PAGE and NUMPAGES Word fields |
| Bluebook periods in federal cites | Oregon style omits |

### Pass 2: Internal consistency

Within a single document, do the following agree:

- **Caption case number** = body case-number references
- **Caption party names** = body party-name references
- **Document title** in caption = document title at top of
  body = document title in footer
- **Hearing date** in motion = hearing date in Notice of
  Hearing
- **Exhibit numbers** referenced in body = exhibit numbers in
  Exhibit List
- **Dollar amounts** consistent throughout (e.g., the
  judgment amount in caption matches the amount in the
  body and in the proposed order)
- **Date references** consistent (e.g., "served on April 1,
  2025" appears the same in every paragraph that references
  the service date)
- **Paragraph cross-references** point to actual paragraphs
  (e.g., "see ¶ 4 above" verifies that ¶ 4 says what is
  implied)
- **Pin cites** to exhibits and pages are accurate

### Pass 3: Packet consistency

Across multiple documents in a single filing packet:

- **All captions are identical** (same court header, same
  parties in same order, same case number)
- **All document titles** match what the body actually
  contains (the Memorandum's title shouldn't say "Motion to
  Compel" if it accompanies a "Motion to Vacate")
- **Hearing date / location / mode** identical across Motion,
  Memorandum, Notice of Hearing, Proposed Order
- **Exhibit numbers** cross-referenced across documents
  (Motion ¶ 4 says "Decl. Ex. 2"; Declaration's Exhibit List
  must include Exhibit 2)
- **Signature blocks** identical (name, role, address, phone,
  email all match across documents in the packet)
- **Service lists** include the same parties in the same
  order

### Pass 4: Sworn-vs.-argued consistency

The single most damaging fact-check failure: a motion **argues**
a fact that contradicts what a **declaration** (sworn under
penalty of perjury) says.

Example:

- Declaration ¶ 4: "I received the validation notice on April
  3, 2025."
- Motion at p. 4: "Defendant received the validation notice
  on March 28, 2025."

These cannot both be true. Either the declaration is wrong (and
the declarant has committed perjury) or the motion mis-states
the record. Either way, opposing counsel will catch it and
exploit it.

The fact-check pass identifies every assertion in the motion
that purports to recite a fact, and locates the supporting
paragraph in the declaration. Each pair is then compared.

Discrepancies are flagged with:

- The motion language
- The declaration language
- A proposed correction (typically updating the motion to
  conform to the declaration, since the declaration is sworn)

## Output format

The agent produces a report:

```
=== Fact-Check Report ===
Packet: [Motion to Compel + Memorandum + Declaration + Order +
         Notice of Hearing]
Date: [today]

Pass 1: Citation Verification
  [PASS] Buchler v. Oregon Corrections Div., 316 Or 499 (1993)
  [PASS] ORCP 46 A(4)(a)
  [WARN] State v. Smith, 250 Or App 1, 280 P3d 1 (2012)
         — Year verified; check that opinion is for the
         proposition cited (current cite supports holding on
         relevance; brief cites it for proportionality —
         consider Phillips v. Beaverton instead)
  [FAIL] Mattiza v. Foster, 311 Or 1, 803 P3d 723 (1990)
         — Parallel cite is P2d, not P3d (1990 case predates
         P3d series). Correct to "803 P2d 723"

Pass 2: Internal Consistency
  [PASS] Caption case number matches body
  [PASS] Document titles match
  [WARN] Motion ¶ 5 references Exhibit 3; Exhibit List
         only includes Exhibits 1 and 2. Either add Exhibit 3
         to the list, or correct the reference to Exhibit 2.

Pass 3: Packet Consistency
  [PASS] All captions identical
  [FAIL] Motion identifies hearing as "June 15 at 9:30 AM
         WebEx"; Notice of Hearing says "June 17 at 9:00 AM
         in person". Reconcile.

Pass 4: Sworn-vs.-Argued Consistency
  [FAIL] Motion p. 4 states "Defendant received the
         validation notice on March 28, 2025."
         Declaration ¶ 4 states "I received the validation
         notice on April 3, 2025." Reconcile (typically
         conform the motion to the declaration).

Summary: 2 PASS, 2 WARN, 3 FAIL — review and correct before
filing.
```

## What this skill does NOT do

- It does NOT silently rewrite the filing. All flags require
  user review.
- It does NOT verify the legal soundness of the argument —
  whether the citations *support* the proposition is for the
  user (and ideally an attorney).
- It does NOT check the substantive law applies — e.g., if
  the filing relies on ORCP 36 B(1) for a discovery dispute
  in arbitration, this skill won't tell you that ORCP 36 may
  not apply in the arbitration proceeding.
- It does NOT check timing — that's `or-deadlines`.
- It does NOT check format — that's `or-quality-check`.

## How to invoke

```
User: Fact-check the motion-to-compel packet I just drafted.
Agent: [Runs the four passes, produces the report]
User: For the FAIL on the parallel cite, fix it. For the
       hearing-date discrepancy, the correct date is June 15
       — update the Notice of Hearing.
Agent: [Applies the two fixes; re-runs Pass 2/3 to verify;
       reports]
```

The user remains in control of every change.

## Citation verification — WebFetch templates

### Oregon case

```
WebFetch:
  url: https://www.courtlistener.com/?q=%22[case name]%22+%22[volume]+Or+[page]%22&type=o&court=or
  prompt: Verify this Oregon Supreme Court citation: [Party]
          v. [Party], [vol] Or [page], [parallel] P2d/P3d
          [page] ([year]). Confirm (1) the case exists at the
          cited reporter and page, (2) the parallel cite, (3)
          the year, and (4) the case is still good law.
          If the case has been overruled, distinguished, or
          superseded by a later Oregon decision, identify
          the later case.
```

### Oregon Court of Appeals

Same pattern, `court=orctapp`.

### 9th Circuit

```
WebFetch:
  url: https://www.courtlistener.com/?q=%22[case name]%22&type=o&court=ca9
  prompt: Verify this 9th Circuit citation: [Party] v.
          [Party], [vol] F3d/F2d [page] (9th Cir [year]).
          Confirm the citation and that the case is still
          good law.
```

### ORS section

```
WebFetch:
  url: https://www.oregonlegislature.gov/bills_laws/ors/ors[CHAPTER].html
  prompt: Locate ORS [chapter].[section]([subsection]).
          Quote the verbatim text. Identify the most recent
          legislative amendment.
```

### ORCP rule

```
WebFetch:
  url: https://counciloncourtprocedures.org/
  prompt: Locate the current ORCP PDF. Quote the verbatim
          text of ORCP [N] [Letter]([number]). Identify the
          effective date of the current version.
```

### UTCR rule

```
WebFetch:
  url: https://www.courts.oregon.gov/rules/UTCR/Pages/default.aspx
  prompt: Locate the current UTCR PDF. Quote the verbatim
          text of UTCR [N].[NNN]([N]). Identify the effective
          date.
```

### Federal statute

```
WebFetch:
  url: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title[N]-section[NNNN]&num=0&edition=prelim
  prompt: Locate [title] USC § [section]([subsection]).
          Quote the verbatim text. Identify the release
          point of the current version.
```

### Federal regulation

```
WebFetch:
  url: https://www.ecfr.gov/current/title-[N]/chapter-[N]/subchapter-[N]/part-[NNNN]/section-[NNNN].[NN]
  prompt: Locate [title] CFR § [N].[NN]. Quote the verbatim
          text as currently in effect. If a relevant date
          was specified, also identify the version in effect
          on that date.
```

## Pre-fact-check checklist (for the user)

Before invoking the skill, ensure:

- [ ] Draft is reasonably complete (don't fact-check a
      half-written motion)
- [ ] All exhibits referenced are listed
- [ ] All key dates are filled in (no "[date]" placeholders)
- [ ] Citations are inserted (no "TBD" or "[case here]"
      placeholders)
- [ ] Spell-check and grammar-check have been run

## Cross-references

- `or-law-references/references/online-sources.md` —
  canonical fetch URLs
- `or-law-references/references/citation-format.md` — Oregon
  Style Manual conventions
- `or-quality-check` — format-pass (paper, margins, fonts,
  footer)
- `or-file-packet` — final-packet preflight
- All draft-* skills — the documents that get fact-checked
