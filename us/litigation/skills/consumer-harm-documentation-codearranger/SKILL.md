---
name: consumer-harm-documentation-codearranger
title: Consumer Harm Documentation & Evidence
description: Use this skill to build documentation and evidence for FCRA or consumer claims. Triggers include "document my damages", "prove harm", "record the call", "they hung up on me", "track postage and time", "communication log", "harm log", "damages worksheet", "emotional distress", "wearable data", "written breakdown from creditor", "settlement value". Covers logging communications, call-recording consent rules (verify by state), capturing hang-ups as bad-faith evidence, filming online interactions, harm taxonomy (higher interest, denials, insurance hikes, "firm books" log), requesting cost breakdowns, and documenting emotional distress. Produces communication logs, harm ledgers, and harm-declaration scaffolds. Composes with consumer-report-ordering, consumer- credit-disputes, consumer-report-accuracy, consumer-credit- monitoring, state *-consumer-debt bundles, and state *-pro-se.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-federal-laws/skills/consumer-harm-documentation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Consumer Harm Documentation & Evidence

> **NOT LEGAL ADVICE.** This skill produces drafting aids and checklists. It is not legal advice
> and does not create an attorney-client relationship. Verify every deadline, dollar threshold,
> and statutory citation against current law before relying on or filing anything.

## Purpose

Claims succeed and settlements rise on **documentation**. The same facts are worth far more with a
clean evidence trail than without one. This skill captures two things: **violations** (what the
creditor, collector, or CRA did wrong) and **harm** (what it cost the consumer — in money, time,
and well-being).

Statutory text: [`../../references/federal-debt-laws/FCRA.md`](../../references/federal-debt-laws/FCRA.md)
(and `FDCPA.md` for collection-conduct violations).

## Recording communications

Record and preserve **every** communication with creditors, collectors, and credit reporting
agencies — calls, letters, portal messages, chats.

> **Call-recording consent varies by state.** Some states allow **one-party** consent (the consumer
> alone may record); others require **all-party** consent (every participant must consent). **Verify
> the rule for the relevant state before recording a call** — route this to the applicable state
> plugin / `*-pro-se` skill. When in doubt, **announce the recording** ("this call is being
> recorded") to satisfy all-party regimes.

- **Capture the bad acts that prove themselves:** a collector who **refuses to be recorded**, talks
  over the notice, or **hangs up** has handed the consumer evidence of bad faith or deceptive
  practice — note the date, time, name, and what was said.
- **Film online interactions.** Screen-record or screenshot dispute portals and chat sessions so
  the record isn't just the company's version.

## The harm taxonomy

Document each category that applies, with proof:

| Harm | Proof to gather |
|---|---|
| Higher interest rate | Loan/card statements showing the rate; a **written breakdown requested from the creditor** |
| Credit / service **denial** | Adverse-action / denial letters (from `consumer-report-ordering`) |
| **Insurance** premium increase | Renewal notices, premium comparisons (tie to the C.L.U.E. report) |
| **Job** denial | Employer adverse-action notice citing a background/credit report |
| **Eviction / tenant-screening** error | The screening report + denial; corrected report |
| **Time & postage** spent disputing | A dedicated **"firm books"** mailing log — every certified-mail receipt, postage cost, and hours spent |

- **Save statements and request written cost breakdowns** from creditors to quantify the extra cost
  caused by the misreporting — concrete dollar figures move settlements.

## Emotional & physiological harm

Emotional distress is compensable and affects settlement value. Document it concretely:

- **Providers:** treatment notes, a letter from a doctor or therapist tying stress/anxiety to the
  events.
- **Wearables / health devices:** data from an Apple Watch or similar device (elevated heart rate,
  disrupted sleep) around the dates of the denials/collection contacts can corroborate distress.
  Present it neutrally as **evidence a drafter cites**, not as a medical diagnosis.
- **Claude as a drafting aid:** wearable health-data exports can be summarized and folded into a
  **harm-declaration scaffold** here — the consumer reviews, verifies, and signs it. The skill
  drafts; it does not diagnose.

## Artifacts this skill drafts

- **Communication log** — chronological record of every contact (date, time, party, channel, who
  said what, whether recorded, refusals/hang-ups).
- **Harm/damages ledger** — one row per harm with category, dollar amount, supporting document, and
  a postage-and-time ("firm books") section.
- **Harm-declaration scaffold** — a sworn-declaration skeleton (financial, time, and emotional/
  physiological harm) for the consumer to verify and sign; routes formatting/verification language
  to the state `*-draft-declaration` / `*-pro-se` skill.

Each artifact ends with the `NOT LEGAL ADVICE` disclaimer.

## Related federal authority

- **ECOA § 1691(d) + Reg B § 1002.9** —
  [`../../references/federal-debt-laws/ECOA.md`](../../references/federal-debt-laws/ECOA.md) /
  [`../../references/federal-debt-laws/Reg-B.md`](../../references/federal-debt-laws/Reg-B.md).
  The **denial letter** that proves harm is an adverse-action notice governed by ECOA / Reg B (not
  only FCRA § 1681m) — preserve it and document the missing/late notice as its own violation.
- **Reg V §§ 1022.70–1022.75 (12 CFR Part 1022)** —
  [`../../references/federal-debt-laws/Reg-V.md`](../../references/federal-debt-laws/Reg-V.md).
  The **risk-based-pricing notice** rules are the mechanism behind the "higher interest rate" harm
  — cite them when documenting increased borrowing cost.
- **FDCPA** —
  [`../../references/federal-debt-laws/FDCPA.md`](../../references/federal-debt-laws/FDCPA.md) — for
  the collection-conduct violations (false statements, threats, § 1692e(8) disputed-debt reporting)
  captured in the communication log.

## Composition

- Denial letters and non-delivery come from **`consumer-report-ordering`**.
- Dispute/complaint proof is preserved alongside the **`consumer-credit-disputes`** trail.
- Collection-conduct violations → the state **`*-consumer-debt`** bundle (FDCPA/Reg F).
- Declaration formatting + verification language → the state **`*-draft-declaration`** and
  **`*-pro-se`** skills.
- Clear harm is the lever for the data-breach / private-suit posture in **`consumer-credit-monitoring`**.
