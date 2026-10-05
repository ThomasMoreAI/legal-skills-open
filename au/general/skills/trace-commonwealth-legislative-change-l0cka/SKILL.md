---
name: trace-commonwealth-legislative-change-l0cka
title: Trace Commonwealth Legislative Change
description: Trace textual changes to provisions of Australian Commonwealth Acts and registered instruments between two dates or compilations using Federal Register versions, compilation endnotes, amendment histories, amending legislation and commencement material. Use when asked what changed in a provision, which amendment made a change, when it commenced, whether it was incorporated, or whether endpoint text stayed the same despite intervening amendments. Do not use for Bills, State or Territory law, case treatment, court deadlines, legal interpretation, transitional operation or application to facts.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-legal-research/skills/trace-commonwealth-legislative-change
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: general
language: en
sources:
- title: Change Tracing Method
  path: references/change-tracing-method.md
---

# Trace Commonwealth Legislative Change

Use the Federal Register of Legislation to produce an evidence-linked change
trace. Keep textual change, commencement, incorporation and legal operation as
separate questions.

Read [references/change-tracing-method.md](references/change-tracing-method.md)
before performing a trace. It defines the source hierarchy, comparison
semantics, attribution test and special cases.

## Workflow

1. Fix the scope.
   - Accept Commonwealth Acts and registered legislative or notifiable
     instruments.
   - Record an earlier and later date or two uniquely identified compilations.
     The later date may default to today's `Australia/Sydney` date when stated;
     never invent the earlier date.
   - Require an exact provision for a provision-level textual conclusion and
     limit one trace to 10 expressly identified provisions. Without one,
     provide only a compilation-event inventory.
   - Return `OUTSIDE SCOPE` for Bills, State or Territory law, case treatment,
     deadlines, interpretation, transitional operation, application to facts
     or substantive legal advice.
2. Resolve the title and complete interval.
   - Establish the exact title and Title ID. Treat multiple plausible titles
     as ambiguous.
   - Identify both endpoint compilations and every intervening compilation.
     Do not compare only the endpoints: text can change and later revert.
   - Describe a compilation by its compilation date or effective period. Never
     say that a compilation commenced; reserve commencement for legislation,
     provisions and amendment items.
   - When command execution is available, use the bundled helper:

     ```bash
     python3 <skill-root>/scripts/frl_change_trace.py trace C2004A03712 \
       --from 2024-01-01 --to 2024-06-01
     ```

     Resolve `<skill-root>` as the directory containing this `SKILL.md`. The
     helper supplies metadata and navigation links only. It does not establish
     a textual change, commencement, legal effect or provision-level causation.
     It is optional and read-only, and it makes network requests only to
     `legislation.gov.au`. Without command execution, follow the same steps on
     the official website directly.
3. Compare the official text.
   - Inspect the exact provision in both endpoint compilations and in each
     potentially relevant intervening compilation.
   - Quote only the minimum text needed to show the change. Preserve subsection,
     paragraph, note and definition boundaries.
   - Call a version authorised only after confirming the official PDF bears the
     required authorisation wording. Do not transfer that label to HTML, EPUB
     or a modified copy.
   - Distinguish `NO NET TEXT CHANGE` from `INTERVENING CHANGES WITH NO NET
     CHANGE`. A shared endpoint compilation proves no compilation transition,
     not that legal operation was unchanged.
   - If the provision is absent at one endpoint, verify whether it was inserted,
     repealed, renumbered or otherwise relocated before labelling the event.
4. Establish provenance and timing.
   - Treat API compilation reasons as navigation evidence. Confirm relevance
     to the requested provision from the compilation endnotes and amendment
     history.
   - Inspect the amending Act or instrument and exact schedule item. Then check
     its commencement provision and any commencement instrument.
   - Keep commencement separate from incorporation into a compilation. Flag
     commenced but unincorporated amendments, retrospective dates, application,
     savings and transitional provisions.
   - Do not infer legal operation or application from a textual comparison.
5. Report using the required result contract.

## Result contract

Lead with one status:

- `VERIFIED` — the endpoint text, intervening events, amendment source and
  relevant timing were established from official material.
- `VERIFIED WITH QUALIFICATIONS` — the trace is supported, but an identified
  commencement, incorporation, retrospective or mapping issue limits it.
- `NOT VERIFIED` — the official evidence is missing, ambiguous, inconsistent or
  insufficient.
- `OUTSIDE SCOPE` — the request falls outside this textual change workflow.

Then provide:

```text
Requested trace: <title, provision and question>
Jurisdiction: Commonwealth of Australia
Comparison interval: <earlier to later date or compilation>
Official title and Title ID: <title and ID>
Earlier compilation: <number, Register ID and effective period>
Later compilation: <number, Register ID and effective period>
Provision: <exact identifier or not supplied>
Endpoint finding: <TEXT CHANGED / NO NET TEXT CHANGE / INTERVENING CHANGES WITH
  NO NET CHANGE / PROVISION ADDED, REMOVED OR RENUMBERED / NOT ESTABLISHED>
Before and after text: <minimum exact text or not established>
Intervening compilation events: <every event in the interval>
Amending legislation and item: <official title, Title ID and provision>
Commencement evidence: <source and date for the amendment or not established>
Incorporation status: <incorporated, unincorporated or not established>
Currency and retrospective flags: <none or itemised flags>
Official sources: <exact pages and documents inspected, with format>
Checked: <date and Australian timezone>
Limitations and human review: <what remains unverified and the review point>
```

For more than one provision, use an evidence table with one row per provision.
Never describe `NO NET TEXT CHANGE` as proof that the law or its operation did
not change.

## Fail closed

Return `NOT VERIFIED` rather than guessing when an endpoint cannot be matched
uniquely, a provision cannot be mapped reliably, relevant amendment or
commencement material is unavailable, a commenced but unincorporated amendment
affects the interval, or retrospective, application, savings or transitional
issues prevent the requested textual conclusion.
