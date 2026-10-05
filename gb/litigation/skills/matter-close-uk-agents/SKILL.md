---
name: matter-close-uk-agents
title: /matter-close
description: Close a matter — capture outcome, final exposure, and lessons, then archive it out of the active portfolio without deleting the record. Use when the user wants to close a matter, says "[matter] is done", or needs to record a settlement, judgment, withdrawal, dismissal, or consolidation outcome.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/litigation-legal-uk/skills/matter-close
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
---

# /matter-close

1. Follow the workflow and reference below.
2. Confirm slug and current status.
3. Capture outcome: resolution type (settled, judgment for/against, dismissed/discontinued, withdrawn, consolidated), date, final exposure/cost, lessons.
4. Update `_log.yaml`: `status: closed`, add `closed: YYYY-MM-DD` and `outcome:` fields.
5. Append final entry to `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/[slug]/history.md`.
6. Matter stays in `_log.yaml` and `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/[slug]/` — not deleted. `/portfolio-status` filters it from active rollups.

---

# Matter Close

## Purpose

Matters end. The outcome is the single most valuable data point the portfolio generates — it calibrates the risk framework for future matters. Closing a matter captures the outcome structurally so the record is useful, not just archived.

## Load context

- `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/_log.yaml` — find the row
- `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/[slug]/matter.md` — reference (intake context)
- `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/[slug]/history.md` — append target

**Conflicts gate — unbypassable.** Before closing, check `_log.yaml` for the matter slug. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Nothing to close — either the slug is wrong or the matter was never intaken through `/litigation-legal-uk:matter-intake`. Check the slug first; if it genuinely was never intaken, there's no row to update and no file structure to close."

## Input

Slug (required).

## The close

### 1. Resolution type

- `settled` — with counterparty, sterling amount, structural terms (Tomlin order / consent order / bare settlement)
- `judgment-for-us` — at what stage, appeal exposure (Court of Appeal / UKSC window)
- `judgment-against-us` — at what stage, appeal status, exposure crystallised
- `discontinued` — claimant discontinued under CPR 38; any costs order
- `dismissed` — dismissed by the court, by what mechanism (strike-out, summary judgment, etc.)
- `withdrawn` — by agreement, circumstances
- `consolidated` — merged into another matter (provide slug of parent matter)
- `other` — with explanation

### 2. Resolution date

The date the matter actually ended (consent order sealed, judgment handed down, notice of discontinuance filed, Tomlin order sealing settlement).

### 3. Final exposure

- Actual cost to company (settlement amount + fees + injunctive/structural cost)
- vs. initial exposure range at intake (did we call it?)
- Reserve accuracy (if reserved): booked vs. actual
- Costs order (if any): indemnity basis / standard basis; amount

### 4. Lessons

Two or three sentences. What did we get right? What did we misjudge? Anything the intake should have flagged earlier?

This is the part future counsel will reread. Be honest. "Misjudged likelihood — claimant's solicitors were more aggressive than expected" is worth more than "resolved favourably."

### 5. Seed doc prompt

Settlement agreement, final order, notice of discontinuance — path if available. Not required.

## Writing

**Before closing the matter (the consequential act — the matter is archived and active tracking ends):** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`. If the Role is Non-lawyer:

> Closing a matter has legal consequences — it ends active tracking, may affect any associated legal hold (run `/legal-hold --release` separately if appropriate), and establishes the final record the company relies on. Have you reviewed this with a solicitor or barrister? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: the matter, resolution type and terms, final exposure vs. initial, reserve accuracy, related matters or appeals still live, what could go wrong with premature closure, what to ask the solicitor/barrister.]
>
> If you need to find a licensed solicitor, barrister, or other authorised legal professional: the SRA (solicitors.lawsociety.org.uk) or Bar Standards Board (barstandardsboard.org.uk/find-a-barrister) for England & Wales; the Law Society of Scotland (lawscot.org.uk) for Scotland; the Law Society of Northern Ireland (lawsoc-ni.org) for Northern Ireland.

Do not write the close fields or append the close entry without an explicit yes.

### Update `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/_log.yaml`

```yaml
status: closed
closed: [YYYY-MM-DD]
outcome: [resolution-type]
final_cost: [sterling amount]
last_updated: [today]   # close is the last touch; record it
```

Retain all existing fields. Do not delete the row.

### Append final entry to `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/[slug]/history.md`

```markdown
## [YYYY-MM-DD] — Matter closed: [resolution-type]

**Resolution:** [narrative — what happened, on what terms]
**Final cost:** [amount + structural terms if any]
**vs. initial exposure:** [compare to matter.md intake range]
**Reserve accuracy:** [if applicable]
**Costs order:** [if any — party, basis, amount]

**Lessons:**
[2-3 sentences — honest retrospective]

**Related doc:** [settlement agreement / final order / etc., if provided]
```

### Touch `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/[slug]/matter.md`

Add a closing block at the end (don't modify earlier sections — they're the historical intake):

```markdown
---

## Closed [YYYY-MM-DD]

[Resolution summary in one paragraph. Pointer to the final history entry for detail.]
```

## Confirm

Show the user the full close entry and the yaml changes before writing.

## What this skill does not do

- Delete matters. Closed matters stay in `_log.yaml` and on disk — they're the training set for the portfolio's judgment.
- Re-open. If a closed matter comes back (appeal, related litigation), open a new matter that references the closed one in `matter.md`.
- Summarise lessons the user didn't say. If the user skips the lessons section, leave it empty rather than invent.
- Release the legal hold. Preservation notice release is a separate action via `/legal-hold --release` — closing the matter record does not automatically release custodians from their preservation obligations.
