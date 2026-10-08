---
name: pa-workflow-litigation-brief-cite-checker-sboghossian
title: Brief Cite Checker
description: Use when a litigator needs to verify every citation in a court brief before filing. Checks that cases exist, pin-cites are accurate, holdings are correctly stated, and subsequent treatment (overruling, distinguishing, limitation) has not undermined the cited proposition. Applies Bluebook and OSCOLA citation formats. Covers common-law courts (DIFC, ADGM, UK, US) and mixed civil-law jurisdictions (UAE, KSA, LB, EG) where citation practice differs materially.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-litigation-brief-cite-checker
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Brief Cite Checker

## Purpose

A single bad citation in a filed brief damages credibility and, in some jurisdictions, can result in sanctions. This workflow runs a systematic five-pass check on every citation in a brief — existence, accuracy, holding, subsequent treatment, and formatting — producing a citation report before the document is filed.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Brief text (full) | Yes | Word / PDF / plain text — all citations will be extracted |
| Target court and jurisdiction | Yes | Determines citation format rules and available databases |
| Citation style | Optional | Default: Bluebook (US/DIFC common-law); OSCOLA (UK/ADGM); civil-law narrative for LB/EG/KSA |
| Deadline | Optional | Flags if time-critical |

## Review Methodology

### Pass 1 — Citation extraction

Parse the brief for all citations:
- Case citations (short form and long form)
- Statutory references
- Regulatory citations
- Secondary sources (treatises, law review articles, restatements)
- Record citations (deposition transcripts, exhibits)

Output an ordered list with page/paragraph location in the brief.

### Pass 2 — Existence check

Verify each case citation resolves to a real decision in the applicable database:
- US: Westlaw, LexisNexis, Google Scholar, CourtListener
- UK: BAILII, ICLR
- DIFC: DIFC Courts portal (published judgments)
- ADGM: ADGM Courts published judgments
- UAE (onshore): UAE Federal Court database; Dubai courts; Abu Dhabi courts
- KSA: Board of Grievances + Royal Decree database
- LB: Lebanese Court of Cassation + Council of State published decisions
- EG: Egyptian Court of Cassation database

Flag any citation that cannot be verified. Do not guess — mark "NOT FOUND" and require attorney confirmation before filing.

### Pass 3 — Pin-cite accuracy

For every citation with a page or paragraph reference:
- Confirm the cited text appears at the stated page/paragraph
- Flag if the proposition attributed to the case actually appears elsewhere in the decision (wrong pin-cite)
- Note if the cited passage is dicta rather than holding

### Pass 4 — Holding correctly stated

This is the highest-value pass:
- Does the brief's characterization of the holding accurately reflect what the court decided?
- Is the case being cited for a proposition it did not actually establish?
- Is a dissent or concurrence being cited as if it were majority reasoning?
- Is the case from a non-binding jurisdiction being cited without a signal (see Bluebook Rule 10.6)?

Flag as:
- **ACCURATE** — holding correctly stated
- **OVERSTATED** — brief claims broader proposition than the case supports
- **MISCHARACTERIZED** — brief attributes the wrong holding
- **DICTA** — cited passage is not the holding

### Pass 5 — Subsequent treatment

Check each case for subsequent history:
- **Overruled**: the proposition no longer represents good law
- **Reversed on appeal**: the decision cited was later reversed by a higher court
- **Distinguished on key fact**: courts have limited the case to its specific facts
- **Superseded by statute**: the legal rule was changed by legislation after the decision
- **Questioned**: courts have expressed doubt without formally overruling

Sources: KeyCite (Westlaw), Shepard's (Lexis), BCite (Lexis UK), Hein Online for older materials. For DIFC/ADGM: manual check of subsequent decisions mentioning the cited case (no automated citator available as of 2025).

### Pass 6 — Citation format

| Format | Jurisdiction | Notes |
|---|---|---|
| Bluebook 21st ed. | US courts; many international arbitrations | Cases: party name, reporter, page (year) |
| OSCOLA 4th ed. | UK courts; DIFC; ADGM | Cases: party name [year] law report court |
| Neutral citation | DIFC / ADGM / UK post-2002 | [Year] DIFC nnn; [Year] ADGM nnn |
| Civil-law narrative | LB, EG, KSA onshore | Court, chamber, date, docket number |

Check: italicization, comma placement, reporter abbreviations, parallel citations where required.

## Output Format

```markdown
## Citation Report — [Brief Title] — [Date]

### Summary
- Total citations reviewed: 47
- Issues found: 6 (2 HIGH, 3 MEDIUM, 1 LOW)

### HIGH — Must fix before filing
| # | Citation | Issue | Recommendation |
|---|---|---|---|
| 1 | Smith v. Jones, 123 F.3d 456, 460 (9th Cir. 1998) | OVERRULED — overruled by X v. Y, 200 F.3d 100 (9th Cir. 2002) | Remove or replace with current authority |

### MEDIUM — Review required
...

### LOW — Formatting
...

### Verified Clean (41 citations)
List of citations confirmed accurate.
```

## Jurisdictional Notes

- **DIFC / ADGM**: These courts follow English common-law tradition and publish judgments online. Citation practice follows OSCOLA. No citator equivalent to KeyCite — subsequent treatment must be checked manually. Counsel should verify no later DIFC/ADGM judgment has distinguished or limited the cited authority.
- **UAE onshore**: Arabic is the official language of the courts; citations to Arabic-language judgments should include the court name, chamber, date, and docket number. English-language summaries from official sources may be cited with caution.
- **KSA**: Sharia court and Board of Grievances decisions are binding within their domains. Saudi legal research databases (e.g., Saudi Legalist, Adaala platform) should be used for Saudi-court citations. Regulatory decisions from specialized tribunals (SAMA, CMA, ZATCA) should be verified on the regulator's official portal.
- **Lebanon**: Published decisions of the Lebanese Court of Cassation and the Council of State are the primary sources. Access is through the Justice Palace library or the Lebanese Lawyers' Association database. Many decisions are not publicly digitized — alert counsel to verify through chambers.
- **Egypt**: Court of Cassation decisions are published in the official gazette (Al-Jarida Al-Rasmiya) and on LACP (Legal Affairs and Contracts Portal). Civil law jurisdiction — doctrine of stare decisis does not formally apply but Court of Cassation decisions are highly persuasive.

## Limits and Escalation

- This workflow cannot independently access Westlaw, LexisNexis, or other subscription databases without authenticated tool integration. When database access is unavailable, flag citations for manual attorney verification.
- The workflow does not assess whether a case is correctly applied to the facts of the current matter — that is a substantive legal judgment requiring attorney review.
- For international arbitration briefs (DIAC, ICC, LCIA, ADCCAC), citation practice varies by tribunal rules; verify applicable procedural rules before formatting.

## Related Skills

- [[pa-workflow-litigation-motion-template-library]]
- [[pa-workflow-litigation-real-time-trial-assist-api]]
- [[pa-workflow-litigation-transcript-search-q-and-a-indexing]]
- [[review-litigation-brief]]
- [[pa-workflow-litigation-case-theory-simulator]]
