---
name: oh-municipal-courts-codearranger
title: Ohio Municipal Courts (R.C. Chapter 1901)
description: Use when filing in an Ohio Municipal Court (R.C. Chapter 1901) — $15,000 civil cap, $6,000 small claims (R.C. 1925), traffic, misdemeanor. Triggers include 'Ohio Municipal Court', 'Cleveland Municipal Court', 'Columbus Municipal Court', 'Cincinnati Municipal Court', 'Akron Municipal Court', 'Ohio small claims', 'R.C. 1901', 'R.C. 1925 small claims', '$15,000 civil Ohio'. Covers the Municipal Court Act + Small Claims Division + the consumer-debt collection dominance of Municipal Court in Ohio.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-municipal-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Ohio Municipal Courts (R.C. Chapter 1901)

> **NOT LEGAL ADVICE.** Municipal Court procedure varies
> across Ohio's ~130 Municipal Courts. Verify the specific
> court's local rules before filing.

## At a glance

- **Court system**: Municipal Courts established under
  **R.C. Chapter 1901** — a court of limited civil and
  criminal jurisdiction within a designated municipality
- **Civil jurisdiction**: up to **$15,000** (R.C. 1901.17;
  $6,000 cap before 2009)
- **Small Claims Division**: up to **$6,000** under R.C.
  Chapter 1925 (R.C. 1925.02)
- **Misdemeanor + traffic**: under R.C. 2935 + Traffic
  Rules
- **Forcible Entry and Detainer**: R.C. Chapter 1923 (the
  Municipal Court is the principal Ohio eviction forum)

## ~130 Municipal Courts statewide

Ohio's Municipal Courts cover most cities + many smaller
towns. The largest by civil-filing volume:

| Municipal Court | Region | E-filing? |
|---|---|---|
| **Cleveland** | Cuyahoga | Yes |
| **Columbus** | Franklin | Yes |
| **Cincinnati** | Hamilton | Yes |
| **Akron** | Summit | Yes |
| **Toledo** | Lucas | Yes |
| **Dayton** | Montgomery | Yes |
| **Canton** | Stark | Yes |
| **Hamilton** | Butler | Yes |
| **Youngstown** | Mahoning | Yes |

Most other Municipal Courts are smaller and may still rely
on paper filings.

## Civil Division procedure

### Jurisdictional cap

- Single claim **≤ $15,000** — Municipal Court has
  jurisdiction
- Single claim **> $15,000** — Common Pleas exclusive
- Counterclaims may exceed $15,000 only on transfer to
  Common Pleas (R.C. 1901.22)

### Procedural framework

- Ohio Civ. R. applies generally
- Loc. R. of the specific Municipal Court overlays
- 28-day answer clock under Civ. R. 12(A)(1) applies
- Magistrate practice (Civ. R. 53) used in most courts

## Small Claims Division (R.C. Chapter 1925)

The Small Claims Division is the **principal pro-se forum
in Ohio**:

- **$6,000 maximum claim** (R.C. 1925.02)
- **No formal pleadings** — written statement of claim on
  court-provided form
- **No counsel required** for natural persons; **counsel
  required** for limited-liability entities (R.C. 1925.17)
- **No discovery** under Civ. R. 26-37 (R.C. 1925.03);
  parties exchange information at the hearing
- **Magistrate hearing** typically within 30-45 days of
  filing
- **Right to trial de novo** in the Civil Division if
  dissatisfied with the small-claims result (R.C. 1925.10)
- **Default judgment** entered if defendant fails to
  appear

## Consumer-debt collection in Municipal Court

Ohio Municipal Courts handle the **vast majority of
consumer-debt collection cases** in the state given the
$15k cap fits most credit-card and consumer-finance
balances:

- Debt-buyer plaintiffs file in Municipal Court whenever
  possible (avoids Common Pleas jury demands)
- Default judgments common against pro-se defendants who
  don't answer within 28 days
- The Ohio CSPA (R.C. Chapter 1345) applies in full —
  debt-collection conduct that's "deceptive" or
  "unconscionable" is actionable under R.C. 1345.02 / .03
  with R.C. 1345.09 treble damages on willful violations

See `oh-consumer-debt` for the substantive bundle.

## Eviction practice — R.C. Chapter 1923

Forcible Entry and Detainer (F.E.D., commonly called
"eviction") is filed in Municipal Court (or County Court
in counties without Municipal Court). Procedure:

- **3-day notice to leave** (R.C. 1923.04) served on
  tenant
- **Complaint** filed in Municipal Court after 3-day
  period
- **First appearance** scheduled within 30 days
- **Restitution of premises** writ issues if tenant
  defaults or loses
- **Damages judgment** in a separate proceeding (Second
  Cause of Action)

See `oh-family-law` for related domestic-violence-
related housing protections that intersect with eviction
practice.

## Filing flow

1. **Complaint** + **$45-$80 filing fee** (varies by
   court)
2. **Service** by certified mail through the clerk or by
   personal service
3. **Answer** within 28 days under Civ. R. 12(A)(1)
   (default judgment if missed under Civ. R. 55)
4. **First appearance / pretrial** typically 30-60 days
   from filing
5. **Magistrate hearing** if contested; bench trial if
   appealed

## Composition with other oh- skills

- `oh-statewide-format` — Civ. R. 10 caption format
- `oh-first-30-days` — 28-day answer clock
- `oh-discovery` — limited Civ. R. discovery in Civil
  Division; NONE in Small Claims
- `oh-pro-se` — pro-se framework (Small Claims is
  dominated by pro-se litigants)
- `oh-consumer-debt` — CSPA + FDCPA + chain-of-title
  defense
