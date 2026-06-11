---
name: carta-form-adv
title: Form ADV Part 1A — Filing Data
description: Fetches Form ADV Part 1A filing data and generates an interactive HTML filing guide + Excel filing reference. Covers Items 5.D/F/H, Schedule D §7.B.(1) per-fund detail, beneficial owner breakdown, asset class composition, and capital activity. Use when asked about Form ADV, regulatory AUM, Schedule D, Form PF Section 1, SEC filing data, or private fund disclosures. Do NOT use for general fund metrics, NAV lookups, or LP contribution history — use carta-explore-data instead.
author: carta
author_url: https://github.com/carta/plugins/tree/main/plugins/carta-investors/skills/carta-form-adv
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: investment-funds
language: en
---

<!-- Part of the official Carta AI Agent Plugin -->

[PATTERN carta-writing-style v0.0.2]
[PATTERN etiquette v0.0.6]
[PATTERN text v0.0.8]
[PATTERN tables v0.0.12]
[PATTERN carta-watermark v0.0.10]
[PATTERN base v0.1.0]

# Form ADV Part 1A — Filing Data

Pulls Form ADV Part 1A data from Carta and generates **two artifacts**:

- **Interactive HTML filing guide** (Items 5.D/F/H, Schedule D §7.B.(1) per fund, IARD checklist)
- **Excel filing reference** (same data, with a Manual Fields sheet for IARD entry)

The artifacts ARE the deliverable. **Do not render Form ADV data as markdown tables in the chat window.** Chat output is limited to a brief status acknowledgment, applicable caveats, the compliance reminder, and a follow-up question.

---

## When to Use

- "Pull our Form ADV data"
- "What's our regulatory AUM for our annual filing?"
- "Show me Schedule D §7.B.(1) data"
- "What do I need for Form PF Section 1?"
- "Give me the asset class composition of our portfolio"
- "What's our annual subscription and distribution activity?"

---

## Entry

Propose the **most recent completed calendar year-end** as the default reporting date — `(current year − 1)-12-31` based on today's date. State the proposed date and let the user override.

> "I'll pull your Form ADV Part 1A data from Carta and build an interactive filing guide and Excel reference. I'll use **{YYYY}-12-31** as the reporting date — confirm or give me a different date. Items requiring manual IARD entry (auditor info, employee counts, fund IDs) will be flagged in both artifacts."

---

## Workflow — Execute ALL Four Steps

You MUST complete every step on every invocation. Step 3 is not optional — the artifacts are the deliverable, not a supplementary export.

### Step 1 — Resolve context

- **Default `reporting_date` to the most recent completed calendar year-end** — `(current year − 1)-12-31` based on today's date. Surface the proposed date in the Entry message and proceed unless the user gives a different one.
- Accept any natural-language override ("December 2023", "end of 2022", "Dec 31, 2024") and resolve to YYYY-12-31. Do not silently use a hardcoded year.
- If this is the first query, call `list_contexts` then `set_context` to establish the firm context.
- See **Fund Scope Disambiguation** below if the user names a specific fund or fund count.

### Step 2 — Run the queries (silently)

Read `${CLAUDE_PLUGIN_ROOT}/skills/carta-form-adv/references/form-adv-queries.md` for the SQL. Execute all three queries in order via `fetch("dwh:execute:query", {"sql": "..."})`:

1. **Query 1** — per-fund AUM, fund detail, capital activity, point-in-time portfolio composition.
2. **Query 2** — per-fund investor demographics (point-in-time membership and NAV from `PARTNER_MONTHLY_NAV_CALCULATIONS`, mutually-exclusive entity-type buckets).
3. **Query 3** — firm-level **distinct** LP aggregates (Items 5.D, 5.H). This block is **required**: the artifact generators read distinct LP counts from `firm_aggregates` instead of summing per-fund counts (which double-counts any LP in multiple funds).

**Do not echo raw rows or render markdown tables** of the results.

### Step 3 — Generate the artifacts (MANDATORY)

Read `${CLAUDE_PLUGIN_ROOT}/skills/carta-form-adv/references/filing-guide.md` and execute its four sub-steps in order, every time:

1. Build `form_adv_data.json` with the actual query result values (no placeholders).
2. Run `generate_form_adv_artifact.py` → HTML artifact.
3. Run `form_adv_excel_generator.py` → Excel filing reference.
4. Open the HTML in Claude Desktop's preview panel via `preview_start` / `preview_list` / `preview_eval`. If preview is unavailable, surface the file path as a fallback.

If any sub-step fails, see **Error Handling** — do not silently skip.

### Step 4 — Acknowledge in chat (no data tables)

Send a brief plain-text message. Substitute the resolved values:

> Pulled your Form ADV Part 1A data for **{reporting_date}** across **{N} funds**. Two artifacts generated:
>
> - **Interactive filing guide** — open in the preview panel _(or:_ saved to `<resolved-tmpdir>/FormADV_<FirmName>_<Year>.html`)
> - **Excel filing reference** — `<resolved-tmpdir>/FormADV_<FirmName>_<Year>.xlsx`
>
> Blue = Carta-filled. Orange = manual IARD entry. The Manual Fields sheet (Excel) and IARD Checklist tab (HTML) list every field needing manual entry.

After the status, surface only caveats that **apply to this specific filing** (e.g., "NAV for [fund] is not calculated for [date] — those fields show `—`"). Do not enumerate every possible caveat — full caveat list is in the artifact's Legend sheet.

Then close with the Escalation Contract reminder and Response Closing.

---

## Fund Scope Disambiguation

1. **User names a specific fund, no match found** → use `AskUserQuestion` to present up to 4 candidate fund names. Do not expand scope until the user picks one.
2. **User states a fund count that doesn't match query results** → surface the discrepancy and wait for confirmation: *"I found [N] funds, not [user's count]. Confirm which are in scope before I run the filing."*
3. **No fund named** → include all funds in the firm context.

---

## Error Handling

| Symptom | Likely cause | Tell the user |
|---|---|---|
| Query returns no rows | `reporting_date` precedes any fund data, or firm context not set | "No data found for that date. Confirm the reporting date and firm context, then try again." |
| `set_context` fails | MCP not connected or user lacks access | "I wasn't able to find your firm. Make sure the Carta MCP server is connected." |
| Permission denied (403) | User lacks data warehouse access | "Your account doesn't have data warehouse access for this query. Contact your Carta admin." |
| All NAV fields null for a fund | Monthly NAV calculation hasn't run for that period | "NAV not calculated for [fund] as of [date] — performance and Net AUM will be blank. Ask your fund admin to run the NAV before filing." |
| Fund count mismatch | Excluded entity type (e.g., GP entity) | "I found [N] Fund/SPV entities. If you expected [M], some funds may be a different entity type — check with your Carta admin." |
| HTML artifact script fails | Missing `uv`, malformed JSON, or unwritable output path | "I couldn't generate the interactive filing guide. Try again, or open an issue if it persists. The Excel file may still be available — check the path below." |
| Excel generator fails | Missing `uv`/`openpyxl`, malformed JSON, or unwritable path | "I couldn't generate the Excel filing reference. The HTML guide may still be available. Try again or contact support." |
| Preview panel won't open | `preview_start` unavailable, port conflict, or `launch.json` write failed | "The preview panel didn't open. The HTML file is at the path above — open it in your browser. Use File → Print → Save as PDF for export." |

---

## Escalation Contract

This skill produces figures used directly in SEC filings. Always surface this reminder when the user indicates they are preparing to file:

> **Filing deadline check:** If any values differ from your fund administrator's records, or you're within 5 business days of your filing deadline, verify with your compliance team before submitting to the SEC. Carta data reflects fund administration records as of the reporting date — discrepancies should be resolved against the fund's audited financial statements.

---

## Voice Guidelines

- Refer to "your Form ADV data" or "your filing guide" — never "query results" or "database output".
- Data gaps: "I wasn't able to retrieve that for [fund name]" — not technical details.
- Proactively explain FMV ≠ NAV and Regulatory AUM ≠ NAV if the user asks about discrepancies.
- Always remind that manual IARD fields must be entered by the user before submitting.
- Apply the Carta watermark per [PATTERN carta-watermark v0.0.10] on all natural-language replies.

---

## Response Closing

End every response with the data-provenance footer, immediately followed by the follow-up question:

*Data as of {reporting_date} · Balance sheet uses effective_date (accounting date) · Verify legal names, fiscal year ends, and IARD fund IDs before filing*

> "Would you like to compare to your prior year's filing, pull additional Form PF fields, or walk through the IARD manual entry checklist?"
