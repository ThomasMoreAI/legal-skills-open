---
name: find-case-by-party-verify-uk-agents
title: /find-case-by-party-verify
description: Find a UK court judgment by party names and verify its neutral citation before citing it to the user. Use whenever the user asks "find <X v Y>", "get me the citation for <case>", "what's the neutral citation for the <case name>", "is there a case called <name>", or pastes a partial case reference. This skill verifies the case exists in TNA Find Case Law BEFORE reporting the citation — prevents the "plausible-looking but wrong" citation failure that happens when an agent formats from training data.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/law-student-uk/skills/find-case-by-party-verify
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
---

# /find-case-by-party-verify

1. Search TNA Find Case Law: `case_law_search(query="<party names>")`.
2. Pick the right judgment — exact title match first; list by court if multiple.
3. Verify: `citations_resolve(neutral_citation=...)` for the top candidate.
4. If resolved, report with `[uk-legal MCP — TNA Find Case Law]` tag and `tna_uri`.
5. If unresolved, tell the user — never report an unverified citation as confirmed.

---

## Purpose

Find a UK court judgment by party names and verify the neutral citation exists in
the TNA Find Case Law corpus before reporting it to the user. The failure mode this
prevents: an agent producing a plausible-looking neutral citation from training data
that does not actually exist in the official record, or that has wrong details. This
skill verifies first and formats second.

## Workflow

> **Source discipline:** If a `uk-legal MCP` tool returns empty or errored (status: `empty` / `not_found` / `upstream_validation` / etc.), do NOT supplement from training data or web search. Report the empty result to the user with the tool's `next_steps` / `detail` field surfaced, and ask for clarifying information (different spelling of a name, a date range, the source URL) rather than fabricating a plausible-looking answer. Empty results are HONEST signal — not a failure mode to paper over.

### Step 1 — Search TNA Find Case Law

Call `case_law_search(query="<party names>")`. The tool returns up to 50 judgments
with `neutral_citation`, `title`, `court`, `sitting_date`, and `tna_uri`.

- Use the party names as the query (e.g. "Smith HMRC VAT recovery").
- Do not supplement the query with training-data knowledge about the case — search
  on what the user provided.

### Step 2 — Pick the right judgment

From the results:

- If the user named both parties, look for an exact title match first (*X v Y*).
- If multiple courts have heard the case (e.g. Court of Appeal and then UKSC), list
  them in court-of-last-resort order: UKSC → Court of Appeal → High Court.
- If no result is returned, ask the user for a year or a court hint before retrying
  with a revised query. Do not fabricate a candidate.

### Step 3 — Verify the citation

Call `citations_resolve(neutral_citation=...)` for the top candidate. This step is
mandatory before reporting any neutral citation to the user.

- If `citations_resolve` returns a resolved record: the citation is confirmed.
  Proceed to Step 4.
- If `citations_resolve` returns `not_found` or an error: the citation is NOT
  confirmed. Proceed to Step 5.
- Never report a neutral citation as confirmed without a successful
  `citations_resolve` result from this session.

### Step 4 — Surface the confirmed judgment

Report to the user:

- Case title in citation form: *X v Y*
- Neutral citation tagged `[uk-legal MCP — TNA Find Case Law]`
- Court and sitting date
- `tna_uri` (for further drill-in via `judgment_get_header` or
  `judgment_get_paragraph` if the user needs specific paragraphs or holdings)

### Step 5 — Verification failure

If `citations_resolve` did not resolve, tell the user:

> "The case appeared in search results but the neutral citation could not be
> independently resolved. This may mean: (a) the case predates TNA's digital
> corpus (pre-2001), (b) the neutral citation in the search index is unstable,
> or (c) the court is not in TNA's covered list. Proceed with caution — verify
> directly at https://caselaw.nationalarchives.gov.uk or via BAILII."

Do not present the unresolved citation as if it were confirmed.

**Source attribution.** All neutral citations tagged `[uk-legal MCP — TNA Find Case Law]`
in this skill's output must come from a `citations_resolve` result confirming the
citation in this session. A citation appearing only in `case_law_search` results and
not yet resolved by `citations_resolve` must be labelled `[unverified — resolve before citing]`.

## Output

Surface to the user:

- **Case found and verified:** title, neutral citation, court, sitting date, `tna_uri`
  — all tagged `[uk-legal MCP — TNA Find Case Law]`
- **Citation status:** "Verified" (resolved) or "Unresolved — do not cite without
  further verification" (not resolved)
- **Next steps** (if verified): offer to retrieve judgment header or specific
  paragraphs via `judgment_get_header` / `judgment_get_paragraph`, or build a
  confirmed OSCOLA citation via `/oscola-build-citation`
- **Next steps** (if unresolved): direct the user to
  https://caselaw.nationalarchives.gov.uk or BAILII for manual verification

**Test prompts:**
- "Find Smith v HMRC dealing with VAT recovery and give me the neutral citation."
- "What's the neutral citation for Donoghue v Stevenson?" (note: pre-2001, may not be in TNA)
- "I need the case on the IR35 status of Sky News presenters in the Upper Tribunal."
