---
name: conflicts-check
title: Conflicts Check
description: Run a NY/NJ RPC conflicts check for a solo or small-firm practice against the firm's conflicts-check workbook whenever a new prospective client, vendor engagement, direct client, fixed-fee package sale, subcontract end-client matter, or new adverse party on an existing matter appears. Trigger on any phrasing like "run a conflicts check on X", "can I take on X", "new client X — check conflicts", "X wants to engage me", "does X conflict", or whenever the user describes a new engagement opportunity and the conflicts workbook is available — even if they don't say the word "conflict". Produces a RED/YELLOW/GREEN read, the rule analysis (1.7 / 1.9 / 1.18 / personal interests), and a ready-to-log Conflict Checks Log row.
author: bstevescherer
author_url: https://github.com/bstevescherer/heycounsel-community/tree/main/skills/conflicts-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
sources:
- title: Analysis patterns
  path: references/analysis_patterns.md
---

# Conflicts Check

Runs a two-tier conflicts check against the firm's conflicts-check workbook. The workbook is the NY RPC 1.10(e) written system of record; this skill is the check protocol run against it. **The script finds names; the lawyer-grade analysis is yours to write.** A clean sweep is never phrased as legal clearance — it is "no hits in the written system."

## Expected workbook structure

The skill assumes a workbook with tabs along these lines. Adapt the tab names to whatever the firm actually uses:

| Tab | Contents |
|---|---|
| Client-Matter Register | Every engagement: client, matter, dates, status |
| Parties Index | Clients, corporate families, principals, and end clients — with alias rows |
| Counterparty Log(s) | Parties negotiated *against* on client matters (one tab per major client, or one combined) |
| Prospects Log | Prospective clients where confidential info may have been received (1.18) |
| Personal Interests | Prior employers, equity holdings, close professional networks |
| Conflict Checks Log | Running record of every check run |
| Waivers Log | Executed conflict waivers with document references |

## Step 0 — Get the workbook (required input, ask if missing)

The expected flow is that the user attaches the current conflicts-check workbook with the request (e.g., "run conflicts on Acme Robotics" + attached file). Check `/mnt/user-data/uploads/` and files shared in this conversation for it.

**If no workbook is attached: STOP before doing anything else — no name assembly, no web search, no analysis — and ask for it in one short message**, e.g.: "Attach the current conflicts-check workbook and I'll run the check on Acme Robotics." Then wait. When the file arrives in the next message, run the full check without re-asking for the prospect details already given.

Never run a check against a stale copy, an older version from a prior session, or a reconstructed-from-memory version — the whole point of the written system under NY RPC 1.10(e) is that memory doesn't count. If multiple versions are present in the conversation, use the most recently uploaded one and say which one you used.

## Step 1 — Assemble the name set (before searching)

A check is only as good as the names swept. From the user's description, build the list:

1. **The prospect entity** — exact legal name if given, plus any trade names / dbas mentioned.
2. **Principals** — founders, named individuals.
3. **Corporate family** — parent, known affiliates. If the prospect is a company of any size and the family isn't stated, do ONE quick web search ("<company> parent company subsidiaries") to identify parents/affiliates before sweeping. Log what you searched.
4. **Adverse parties on the prospective matter** — who is on the other side of the paper for the work being proposed (counterparties, opposing parties, target vendors). If the user hasn't said what the matter is, ask — the matter description drives the "substantially related" analysis and the adverse-party list.
5. **Subcontract structures** (any engagement where a law firm is the client of record): the conflict surface is the END CLIENT and the end client's counterparties, not just the firm. Get those names.

## Step 2 — Run the deterministic sweep

```bash
python scripts/name_sweep.py <workbook.xlsx> "Name One" "Name Two" ...
```

The script sweeps every cell of every tab (including Notes columns, where end-client counterparties live), normalizes case/punctuation/entity suffixes, and reports EXACT / SUBSTRING / PARTIAL hits with full row context as JSON.

Data quirks to respect:
- **Aliases are real rows** in the Parties Index (an abbreviation, a ticker, a US-subsidiary shorthand, a d/b/a). A hit on any alias is a hit on the client. Aliases only work if someone maintained them — if a client is known internally by an acronym and no alias row exists, flag that gap.
- **Category placeholder rows** ("HVAC vendors — log each", "misc. SaaS vendors") don't search. If the sweep relies on a category row rather than a named party, flag the gap to the user.
- **PARTIAL hits need human eyes** — report them as "possible, verify" rather than silently promoting or dropping them.

## Step 3 — Two-tier analysis of every hit

**Tier 1 — client-level hits** (Client-Matter Register, Parties Index client/family/principal rows, Prospects Log, Personal Interests):
- Prospect IS a current client / affiliate → new-matter check, usually clean, note it.
- Prospect or its family is ADVERSE to a current client → RPC 1.7(a)(1) direct adversity or 1.7(a)(2) material limitation. Waivable only with informed consent confirmed in writing from each affected client + reasonable belief of competent/diligent representation for all. Same-litigation opposing parties: never waivable.
- Hit on a FORMER client (including end clients that arrived through a firm subcontract and are tagged as such in the Parties Index) → RPC 1.9: is the new matter the SAME or SUBSTANTIALLY RELATED, and would it be adverse? Substantially related = same transaction, or old confidences would materially advance the new client's position.
- Hit in Prospects Log → RPC 1.18: was confidential info received, and could it be significantly harmful in this matter?
- Hit in Personal Interests (prior employers, professional networks, equity) → 1.7(a)(2) personal-interest analysis; equity-for-fees triggers 1.8(a).

**Tier 2 — counterparty-level hits** (Counterparty Logs, counterparty names inside Notes):
A tier-2 hit is NEVER automatic disqualification — these parties were negotiated against; they are not clients. It triggers analysis:
- Would representing the prospect mean working on/against paper the user negotiated for a current client (confidential playbook positions)?
- Would it foreclose future client work on that vendor (pre-committed carve-out)?
- Is a live negotiation, renewal, or dispute with that counterparty foreseeable?

Scope splits the answer: internal-only governance work for a former counterparty is much cleaner than anything touching the commercial paper the user marked up. See the counterparty-becomes-prospect pattern in `references/analysis_patterns.md` — read it whenever a tier-2 hit involves a major client's counterparty.

## Step 4 — Deliver the read

Output in this order (RED/YELLOW/GREEN, conclusions front-loaded, concise):

1. **Verdict line**: GREEN (no hits / clean analysis — proceed), YELLOW (hits requiring analysis or waiver — here's the path), RED (decline or carve out scope).
2. **Hits table**: name → tab/row → rule implicated → one-line analysis.
3. **The judgment calls**: material-limitation and substantially-related determinations are fact-specific. For genuinely close calls, recommend the NYSBA or NJ ethics hotline before papering anything.
4. **Ready-to-log row** for the Conflict Checks Log, matching its columns exactly:
   `Check Date | Prospective Client/Matter | Names Searched | Hits Found | Rule(s) Implicated | Analysis | Outcome | Waiver Ref | Checked By`
   Date format YYYY.MM.DD. Outcome values: `Clear — proceed` / `Waivable — consent obtained` / `Waivable — consent pending` / `Declined`. Offer to append it to the workbook directly (openpyxl, preserve formatting and font) and return the updated file.
5. **If a waiver is the path**: draft the informed-consent talking points and remind that consent must be CONFIRMED IN WRITING and logged in the Waivers Log with a document reference.

## Boundaries

- Never phrase a clean sweep as "no conflict exists" — phrase as "no hits in the written system; based on the recorded engagements, I see no conflict under 1.7/1.9/1.18."
- Never transcribe client confidences into the check output — category level only, matching the workbook's own discipline.
- Rule citations here are NY and NJ. If the practice is admitted elsewhere, re-check the local numbering and any imputation/screening differences before relying on this.
- This data is confidential attorney work product. No retention, no training.
- The check must be logged BEFORE the engagement letter goes out — if the user is about to send an EL without logging, say so.
