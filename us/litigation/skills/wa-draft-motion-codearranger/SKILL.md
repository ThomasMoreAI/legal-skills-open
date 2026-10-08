---
name: wa-draft-motion-codearranger
title: Draft a Washington Motion + Supporting Memorandum
description: Use this skill when the user asks to draft a motion for a Washington State court — superior court or district court (KCDC). Triggers include "draft a motion", "write a motion to compel", "I need to file a motion to dismiss", "motion for summary judgment", "motion to vacate", "motion for reconsideration", "motion for default", "motion to strike", "new motion". Scaffolds a motion with supporting memorandum that complies with GR 14, statewide motion practice, and the pro-se drafting framework for concise, fact-forward drafting. Composes with `wa-statewide-format` (always), `wa-kcdc` (if KCDC), `wa-pro-se` (if pro se), and `wa-discovery` / `wa-post-judgment` depending on the motion type.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-draft-motion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Washington Motion + Supporting Memorandum

Scaffold a motion and companion memorandum that complies with GR 14,
statewide motion practice, and the pro-se drafting framework for concise,
fact-forward drafting.

> **NOT LEGAL ADVICE.** This skill scaffolds a court document as
> a drafting aid. The user — not the skill — chooses the motion
> type, theory of relief, and strategy. Verify every rule,
> deadline, and citation against current law before filing. Pair
> with substantive review by counsel where stakes warrant.

## Inputs to gather

Before drafting, confirm with the user (use AskUserQuestion for any
that are unclear):

1. **Motion type** — What is being asked of the court? (e.g., compel,
   dismiss, strike, default, summary judgment, vacate, reconsider)
2. **Court** — Which court? Load `wa-kcdc` if KCDC.
3. **Case caption** — Party names and case number
4. **Movant** — Who is filing? Pro se? Represented?
5. **Rule basis** — Which CR or CRLJ rule authorizes the motion?
6. **Key facts** — What are the 1–3 single best facts supporting relief?
7. **Relief sought** — Specific, enforceable relief
8. **Single or separate** — Combined motion+argument (simpler) or
   separate motion + memorandum (complex)?
9. **Supporting declaration** — Is there a declaration already filed,
   or does one need to be drafted alongside?

## Steps

1. **Load the companion skills.** Read:
   - `skills/wa-statewide-format/SKILL.md`
   - `skills/wa-statewide-format/references/templates/motion-with-memo.md`
   - `skills/wa-pro-se/SKILL.md` and
     `skills/wa-pro-se/references/pro-se-drafting-framework.md` if pro se
   - `skills/wa-kcdc/SKILL.md` and
     `skills/wa-kcdc/references/civil-motion-docket.md` if KCDC

2. **Choose option A or B:**
   - **Option A (self-contained)**: for simple motions — single
     document with Relief / Facts / Argument / Conclusion
   - **Option B (motion + memo)**: for complex motions — short motion
     with grounds, plus a separate 3–5 page memorandum

3. **Apply the pro-se drafting framework:**
   - Lead with the single best fact
   - Argument headings state the conclusion, not the topic
     (e.g., "A. The chain of title is missing" not "A. Chain of title")
   - Every factual assertion cited to exhibit or declaration paragraph
   - Every legal assertion cited to rule, statute, or case
   - Keep the motion ≤ 2 pages and memo ≤ 5 pages (combined ≤ 6)

4. **Draft in markdown first** using the scaffolded structure from
   `motion-with-memo.md`. Include:
   - Court caption with "NOTE ON MOTION CALENDAR" block
   - Roman-numeral section headings (I. RELIEF REQUESTED, II. FACTS,
     etc.)
   - Bold lead-in argument headings
   - Signature block

5. **Review with the user.** Show the draft. Iterate on the
   arguments, facts, and relief before generating the .docx.

6. **Generate the .docx** using the docx-js patterns in
   `skills/wa-statewide-format/references/docx-generation.md`.

7. **Offer companion documents.** Remind the user they likely also
   need a Declaration in support, a Proposed Order, a Note for Motion
   Docket, and a Certificate of Service. If any are missing, the
   agent can scaffold them using the `wa-draft-declaration`,
   `wa-draft-order`, and `wa-draft-note` skills — and assemble the
   full filing via the `wa-file-packet` skill when everything is
   ready.

8. **Deliver** via `computer://` link. Offer to run a GR 14 / content
   check using the `wa-quality-check` skill.

## Notes

- Under-ask rather than over-ask. A tight motion that asks for one
  precise thing is more persuasive than a kitchen-sink motion
- If combined, label the document "[MOTION TITLE] AND MEMORANDUM IN
  SUPPORT"
- Reserve CRLJ 11 sanctions for a separate motion — never combine
- For KCDC: remember the three-step motion-docket protocol — a
  hearing date is **not** self-selected. The `wa-schedule-hearing`
  skill handles step 1 (the CivilMGT email). Don't draft the Note
  until the clerks issue a date.
