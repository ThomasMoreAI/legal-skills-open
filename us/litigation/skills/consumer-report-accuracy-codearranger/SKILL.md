---
name: consumer-report-accuracy-codearranger
title: Consumer Report Accuracy & Key Data Points
description: 'Use this skill to audit and correct consumer-report data: PII and tradeline points affecting reporting duration, scoring, and SOL. Triggers include "wrong info on my credit report", "update my address", "Date of First Delinquency", "DOFD", "re-aged debt", "disputed by consumer", "mark it disputed", "why didn''t my score go up", "dispute flag missing", "monitor my report weekly". Covers PII hygiene (remove stale addresses/phones causing mistaken matches and fraud), Date of First Delinquency clock (§ 1681c) and SOL anchor, watching for re-aging, ensuring "disputed by consumer" flag for score lift, and weekly monitoring. Produces PII correction requests, re-aging challenge letters, and dispute-mark checklists. Composes with consumer-report-ordering, consumer- credit-disputes, consumer-harm-documentation, consumer-credit- monitoring, state *-consumer-debt bundles, and state *-pro-se.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-federal-laws/skills/consumer-report-accuracy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Consumer Report Accuracy & Key Data Points

> **NOT LEGAL ADVICE.** This skill produces drafting aids and checklists. It is not legal advice
> and does not create an attorney-client relationship. Verify every deadline, dollar threshold,
> and statutory citation against current law before relying on or filing anything.

## Purpose

Once the reports are in hand (`consumer-report-ordering`), read them like an adjuster. Two layers
matter: the **PII block** (who the report thinks you are) and the **tradeline data points** (what it
says you did and for how long). Errors in either cause mistaken matches, fraud exposure, depressed
scores, and extended liability on old debt.

Statutory text: [`../../references/federal-debt-laws/FCRA.md`](../../references/federal-debt-laws/FCRA.md).

## PII hygiene

Review and, where possible, correct **all** identifying fields: legal name and variants, current
and former **addresses**, **phone numbers**, and **employer** information.

- **Remove stale or wrong addresses and phone numbers.** Old data invites **mistaken merging** of
  another person's records into the file and makes **identity fraud** easier to pull off. Fewer,
  accurate data points = fewer wrong matches.
- **When a furnisher's active reporting blocks removal:** some PII can't be deleted while a
  furnisher is actively reporting an account tied to it. In that case, **request the furnisher's
  contact information** from the CRA and pursue the correction at the source (furnisher dispute
  under § 1681s-2(b)) rather than only at the bureau.

## The Date of First Delinquency (DOFD) — the master clock

The **Date of First Delinquency** is the single most important date on a tradeline. It sets:

- **Reporting duration** — most negative items must come off ~**7 years** from the DOFD
  (15 U.S.C. § 1681c). The DOFD does **not** reset when a debt is sold or paid.
- **Statute-of-limitations analysis** — the DOFD anchors how old the debt is for SOL purposes under
  the applicable **state** law (route the SOL determination to the relevant `*-consumer-debt`
  bundle).

**Watch for re-aging.** Debt buyers and some furnishers **alter the DOFD** to a later date to keep
a stale account reporting (and to make a time-barred debt look collectible). Re-aging is a
reportable, disputable violation. If the DOFD looks inconsistent across the Big-3 or has moved,
flag it and challenge it.

## The "disputed by consumer" flag

When an item is under dispute, it should be marked **"disputed by the consumer"** on the report.

- A properly marked item is **excluded from credit-score calculation** — which typically produces
  an **immediate score increase** while the item remains on the file pending resolution.
- After filing a dispute, **verify the mark actually appears.** A **missing or incorrect** dispute
  comment signals the dispute was not properly processed — loop back to `consumer-credit-disputes`
  and correct it.

## Monitoring cadence & evidence organization

- Pull reports regularly via **annualcreditreport.com**, and where available use **weekly pulls**
  to watch dispute status and catch changes quickly.
- **Annotate as you go:** mark questionable items with **sticky notes** (or the digital equivalent)
  so the evidence is organized for disputes and any later claim — which line, which bureau, what's
  wrong, and what proof exists.

## Artifacts this skill drafts

- **PII correction request** — itemizes wrong/stale name, address, phone, employer fields to
  correct or delete, per CRA.
- **Re-aging challenge letter** — identifies the altered DOFD, states the correct date with proof,
  and demands correction (paired with the § 1681i dispute from `consumer-credit-disputes`).
- **Dispute-mark verification checklist** — confirms each disputed tradeline carries the
  "disputed by consumer" comment on each bureau, flagging any that don't.

Each artifact ends with the `NOT LEGAL ADVICE` disclaimer.

## Related federal authority

- **Reg V § 1022.42 (12 CFR Part 1022)** —
  [`../../references/federal-debt-laws/Reg-V.md`](../../references/federal-debt-laws/Reg-V.md).
  Imposes the furnisher's **accuracy and integrity** duties that a re-aged Date of First
  Delinquency, a stale tradeline, or a mismatched-PII account violates.
- **FDCPA § 1692e(8)** —
  [`../../references/federal-debt-laws/FDCPA.md`](../../references/federal-debt-laws/FDCPA.md).
  When a collector reports a debt without noting the consumer's dispute, the **missing "disputed by
  consumer" notation is itself an FDCPA violation** — tie the report defect to the statute.

## Composition

- Get the reports → **`consumer-report-ordering`**.
- File the lawful dispute that effects the correction → **`consumer-credit-disputes`**.
- DOFD-driven SOL / time-barred-debt analysis → the state **`*-consumer-debt`** bundle.
- Preserve proof of errors and harm → **`consumer-harm-documentation`**.
- Keep watching and propagate corrections → **`consumer-credit-monitoring`**.
- Pro-se mechanics → the state **`*-pro-se`** skill.
