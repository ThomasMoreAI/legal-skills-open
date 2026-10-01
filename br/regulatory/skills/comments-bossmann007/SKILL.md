---
name: comments-bossmann007
title: /comments
description: Review open consulta pública / tomada de subsídios periods from Brazilian regulatory agencies, log decisions, track deadlines. Use when an agency (ANPD, ANATEL, ANVISA, BCB, etc.) has a participation window open and you need to surface deadlines, decide whether to file a contribuição, or record a filing / not-filing / waived decision (--decide CMT-ID).
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/regulatory-legal/skills/comments
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: en
---

# /comments

## Purpose

Consultas públicas e tomadas de subsídios have deadlines (prazo de
participação). The decision to file a contribuição or not is an attorney
call — but the deadline disappearing without a logged decision is the risk.
This skill surfaces open participation periods and records decisions.

Under Brazil's Lei Geral das Agências Reguladoras (Lei 13.848/2019), the
agências reguladoras must open the regulatory process to social
participation: **consulta pública** (written contributions on a proposed act,
art. 9 `[settled — last confirmed 2026-07-03]`) and **audiência pública** (an
oral public hearing the agency may convene on a relevant matter, art. 10
`[settled — last confirmed 2026-07-03]`). Beyond these statutory instruments,
agencies may create others by regimento interno (art. 11) — the **tomada de
subsídios** (early-stage input-gathering before a proposal is drafted) is one
such regimental instrument that the **ANPD** in particular uses, alongside its
consultas públicas, on data-protection regulamentações under the LGPD `[model
knowledge — verify — tomada de subsídios is agency-regimental, not in Lei
13.848]`. Participation is
generally written, submitted via the agency's electronic portal (Participa +
Brasil / the agency's own consulta system) within the published prazo.

## Load context

`~/.claude/plugins/config/claude-for-legal/regulatory-legal/comment-tracker.yaml` → all tracked consultas/tomadas de subsídios and their status.
`~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` → default comment decision owner.

## Default view — open participation periods

```markdown
## Consulta / Tomada de Subsídios Tracker — [date]

### ⏰ Deadline in <14 days

| ID | Regulation | Deadline | Days left | Decision | Owner |
|---|---|---|---|---|---|
| CMT-001 | [name] | [date] | [N] | Undecided | [owner] |

### 🟡 Open (>14 days)

[same table]

### Recently decided

| ID | Regulation | Decision | Rationale |
|---|---|---|---|
| CMT-002 | [name] | Not filing | [reason] |

---

**Total open:** [N]  **Undecided with deadline <30 days:** [N]
```

## Log a decision

```
/regulatory-legal:comments --decide CMT-001
Decision: [filing / not-filing / waived]
Rationale: "[brief — e.g., 'Rule doesn't apply to our model' or 'Filing comment on Section 3']"
```

Updates tracker. If decision is "filing": prompt for filing deadline reminder
(comment deadline minus 5 business days for internal review).

## Notifications

On first detection of a consulta pública / tomada de subsídios (populated by
reg-feed-watcher): Slack DM to comment decision owner if Slack MCP is
configured and `owner_slack` is set.

Reminder at 14 days before deadline if decision is still "undecided."
Reminder at 3 days before deadline if still undecided — elevated urgency.

## Consequential-action gate (submit a regulatory comment / respond to a regulator)

**Before logging a decision as "filing" — and always before producing a comment letter or regulator-response draft for submission:** Read `## Who's using this` in ~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md. If the Role is **Non-lawyer**:

> Submitting a contribuição or response to an agência reguladora has legal consequences. It's a public statement of the company's position, it goes on the record in the processo regulatório or enforcement matter, and positions taken here bind the company and can be used against it in subsequent proceedings. Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> - The processo regulatório or inquiry (agência reguladora, nº do processo/consulta, prazo)
> - What the proposed contribuição/response says and on what sections
> - Open questions and what's unresolved
> - What could go wrong (adverse admissions, inconsistent prior positions, coordination-of-comment concerns with associações setoriais)
> - What to ask the attorney (should we file at all; should we file jointly through an associação/entidade de classe; are there positions we should not take)
>
> If you need to find a lawyer: the OAB (Ordem dos Advogados do Brasil) seccional of your estado is the starting point — its Comissão de sociedade/serviço de referência or the local subsecção can point you to counsel. (For a foreign regulator: that jurisdiction's professional body — state bar in the US; SRA/Bar Standards Board in England & Wales; or the local equivalent.)

Do not log a "filing" decision or produce a submission-ready draft past this gate without an explicit yes. Tracking views, deadline reminders, and "not-filing / waived" decisions do not require the gate.

---

## What this skill does not do

- Draft the contribuição. That is a separate attorney task.
- Make the filing decision. It tracks the decision; the attorney makes it.
- Monitor post-comment activity. Once a decision is filed, this tracker's job
  is done — follow the processo regulatório through `/regulatory-legal:reg-feed-watcher`.

## US-agency fallback (gated)

Use this ONLY when the tracked item is a US federal rulemaking (an agency
Notice of Proposed Rulemaking / NPRM) rather than a Brazilian consulta pública
or tomada de subsídios — e.g., the practice profile's jurisdiction footprint
includes the US and a US regulator (SEC, FTC, CFPB, etc.) has opened a comment
period. Do not apply this to Brazilian agency processes.

When it applies, the mechanics differ:
- The instrument is an **NPRM** published in the **Federal Register**;
  comments are filed on **Regulations.gov** against the rule's **docket**
  within the published comment period. `[model knowledge — verify]`
- Everything else in this skill (the tracker, the deadline reminders, the
  consequential-action gate, the not-filing/waived logging) works the same —
  only the underlying regime label and filing portal change. Tag any US cite
  `[model knowledge — verify]` and confirm against Regulations.gov before
  relying.

> The `comment-decision` `gap_type` semantics, the per-send Slack confirmation rule, and the comment-tracker.yaml schema live in the **gap-surfacer** reference skill — load it before doing substantive work.
