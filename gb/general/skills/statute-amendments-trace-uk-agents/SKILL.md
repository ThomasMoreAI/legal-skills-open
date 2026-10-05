---
name: statute-amendments-trace-uk-agents
title: /statute-amendments-trace
description: Trace the current state of a UK Act including in-force amendments AND any pending bills that would amend it. Use whenever the user asks "is <Act> current", "what's the latest version of <Act>", "have any bills amended this", "what's pending for <Act>", or "what changes are proposed to <Act>". Statutes are living documents — a citation without amendment-status risks citing repealed or superseded text.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/commercial-legal-uk/skills/statute-amendments-trace
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# /statute-amendments-trace

1. Locate the statute: `legislation_search(query="<title>")`.
2. Get TOC and jurisdictional extent: `legislation_get_toc(type=..., year=..., number=...)`.
3. Check in-force amendments via `legislation_get_section` for sections of interest.
4. Search for pending bills: `bills_search_bills(query="<short title>")`.
5. Report current status, jurisdictional extent, and pending bills with stage and sponsor.

---

## Purpose

Trace the current amendment status of a UK Act and surface any pending parliamentary
bills that would further amend it. Statutes are living documents — citing an Act
without checking its amendment status risks relying on repealed, suspended, or
superseded text. This skill checks both the current enacted state (via
legislation.gov.uk) and the parliamentary pipeline (via the Bills API).

## Workflow

> **Source discipline:** If a `uk-legal MCP` tool returns empty or errored (status: `empty` / `not_found` / `upstream_validation` / etc.), do NOT supplement from training data or web search. Report the empty result to the user with the tool's `next_steps` / `detail` field surfaced, and ask for clarifying information (different spelling of a name, a date range, the source URL) rather than fabricating a plausible-looking answer. Empty results are HONEST signal — not a failure mode to paper over.

### Step 1 — Locate the statute

Call `legislation_search(query="<title>")`. If the user gave only a partial title,
include the year if known to narrow results. If multiple statutes match, list them
and ask the user to confirm which one before proceeding.

### Step 2 — Get the TOC and extent

Call `legislation_get_toc(type=..., year=..., number=...)` using the identifiers
returned in Step 1. This returns:

- The structural table of contents for the Act
- The `extent` field: which jurisdictions the Act applies to (England, Wales,
  Scotland, Northern Ireland — note that extent can vary section by section)
- Any amended version flag indicating that in-force amendments have been applied
  to the legislation.gov.uk text

### Step 3 — Check in-force amendments

If Step 2 returns an amended version flag, or if the user is specifically asking
about the current text of one or more sections, call `legislation_get_section`
for those sections to confirm the current enacted text.

Note in the output which sections were confirmed via `legislation_get_section`
in this session and which were not. Do not assert that a section is current
without having retrieved it in this session, or without reporting the limitation.

### Step 4 — Check for pending amendments

Call `bills_search_bills(query="<short title>")` using the short title of the Act.
The tool returns current Bills referencing the Act, with `current_stage`, `house`,
and `sponsor` for each.

- If the Bills search returns results, report each matching bill with its
  `current_stage`, originating house, and sponsor.
- If the Bills search returns empty, state explicitly: "No current bills referencing
  this Act found in the Bills API at time of check."
- Do not supplement from training data about pending legislation — the Bills API
  result is the authoritative signal for the pipeline check.

### Step 5 — Surface to the user

Report:

- Current statute status tagged `[uk-legal MCP — legislation.gov.uk]`
- Jurisdictional extent from the `extent` field, noting any section-by-section
  variation
- Pending bills (if any) tagged `[uk-legal MCP — bills]` — for each: bill title,
  `current_stage`, originating house, sponsor
- If no pending bills: "No current bills referencing this Act found in the Bills API
  at time of check."
- Offer next steps (see ## Output below)

**Source attribution.** All statute status information carries `[uk-legal MCP —
legislation.gov.uk]`. All bill pipeline information carries `[uk-legal MCP — bills]`.
No pending bill may be reported without a `bills_search_bills` result from this
session.

## Output

Surface to the user:

- **Act identified:** short title, year, legislation.gov.uk reference
  `[uk-legal MCP — legislation.gov.uk]`
- **Jurisdictional extent:** from the `extent` field, noting any section-by-section
  variation
- **In-force amendment status:** whether amendments have been applied to the
  legislation.gov.uk text; which sections were confirmed via `legislation_get_section`
  (if any) and their current text
- **Pending bills** (if any): per bill — title, `current_stage`, originating house,
  sponsor `[uk-legal MCP — bills]`
- **Suggested next steps:**
  - To see what peers and MPs said about a pending bill: `/find-member-contribution`
  - To trace a pending bill's full parliamentary journey: `/bill-debate-trace`

**Test prompts:**
- "Is section 21 of the Housing Act 1988 still in force? What bills would amend it?"
- "What's the current state of the Online Safety Act 2023?"
- "Are there any pending amendments to the Equality Act 2010?"
