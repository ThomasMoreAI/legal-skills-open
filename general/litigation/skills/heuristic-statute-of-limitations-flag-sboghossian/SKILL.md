---
name: heuristic-statute-of-limitations-flag-sboghossian
title: Statute of Limitations Flag
description: Use whenever a user is analyzing a potential claim, drafting litigation strategy, or negotiating a settlement where time sensitivity matters. Automatically check and flag limitation/prescription periods for the relevant jurisdiction and claim type, calculate remaining time from the accrual date, and escalate urgently if the period is less than 6 months or 30 days. Covers LB, UAE federal, KSA, DIFC/ADGM, and notes EU/civil-law variability. Statute clock misses are unrecoverable errors.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/heuristic/heuristic-statute-of-limitations-flag
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Statute of Limitations Flag

## When this applies

This heuristic fires in any context where a legal claim may exist or be contemplated:

- Pre-litigation analysis ("Can I still bring this claim?")
- Claim drafting and pleading preparation.
- Settlement negotiation (remaining limitation period is a material factor in settlement value).
- Advising a client on a dispute that has been ongoing without formal action.
- Reviewing a contract claim where a breach occurred some time ago.
- Any matter note that references a past event that could give rise to a claim.

**Statute clock misses are unrecoverable.** A claim that is time-barred cannot be revived. This heuristic is P0 because missing a limitation period is a professional liability event.

## The check protocol

Before drafting or advising on any claim, run this five-step protocol:

1. **Identify the claim type**: contract? tort? employment? commercial? insurance? Limitation periods differ by claim type within the same jurisdiction.
2. **Identify the accrual date**: when did the cause of action arise? Typically: for contract claims, the date of breach; for tort, the date the damage occurred (or was discoverable).
3. **Identify the applicable limitation period** for the claim type and jurisdiction (see table below).
4. **Calculate the remaining period**: Accrual date + limitation period = expiry date. Flag if < 6 months remaining.
5. **Check tolling events**: has the clock been suspended (tolled)? Events that may toll the clock include: minority of the claimant, acknowledged debt/obligation by the debtor, ongoing negotiations, force majeure.

## Limitation periods by jurisdiction

All periods below are indicative. **Verify against current law before advising** — legislation changes and shorter periods frequently apply to specific claim subtypes.

### Lebanon (Code of Obligations and Contracts)

| Claim type | Period | Notes |
|---|---|---|
| Tort (general) | 3 years | Art. 257 COC; from date of damage or discovery |
| Contract (general commercial) | 10 years | Art. 349 CCO |
| Insurance claims | 2 years | Shorter specific period |
| Maritime claims | 1 year | Shorter specific period |
| Wage claims | 1 year | From termination or last payment |
| Real estate actions | Varies | Check specific provisions; some are very short |

*Note*: Lebanon's judicial system has been under significant operational stress since 2019. Court backlogs and practical enforcement of limitation rules should be verified with local counsel.

### UAE Federal

| Claim type | Period | Notes |
|---|---|---|
| Tort (civil) | 3 years | Civil Transactions Law |
| Contract (general) | 15 years | Civil Transactions Law — general contract |
| Commercial contracts | 10 years | Commercial Transactions Law |
| Employment claims | 1 year | From termination; MOHRE/court |
| Insurance claims | 3 years | Insurance Law specific period |
| Cheque dishonor | 1 year | Commercial Transactions Law |

*Note*: Emirate-level regulations (Dubai, Abu Dhabi) may impose shorter periods for specific regulated activities.

### KSA

KSA limitation periods are less codified than civil-law systems. They are derived from Sharia principles and applied by judicial discretion, supplemented by specific statutes for commercial, labor, and regulatory matters.

| Claim type | Indicative period | Notes |
|---|---|---|
| Commercial contracts | 10 years | Indicative; verify with local counsel |
| Labor claims | 1 year | From termination; Labor Law |
| Insurance claims | 5 years | SAMA regulatory guidance |
| Real estate | Varies | Verify per transaction type |

*Critical*: KSA limitation periods are fact-specific and judicial-discretion-based. Always obtain local counsel confirmation.

### DIFC and ADGM

DIFC and ADGM follow English-model limitation periods:

| Claim type | Period | Notes |
|---|---|---|
| Contract | 6 years | DIFC Limitation Law; ADGM Limitation Regulations |
| Tort | 3 years | With discoverability extension where applicable |
| Personal injury | 3 years | With specific rules on discoverability |
| Latent damage (property/professional negligence) | 3 years from discovery (max 15 years from act) | |

### EU / Civil-law (general)

EU member states and civil-law jurisdictions have their own limitation regimes, typically 2–10 years for contract and tort, subject to statutory variation per claim type and country. Always identify the specific member state law before advising.

## Escalation thresholds

| Remaining period | Action |
|---|---|
| > 12 months | Note the limitation period in the advice; no urgency flag |
| 6–12 months | Flag as "limitation approaching — calendar for action" |
| < 6 months | **Priority flag**: "Statute of limitations concern — fewer than 6 months remaining. Immediate review required." |
| < 30 days | **Urgent escalation**: "Statute expires in [N] days. Immediate filing or tolling action required." Surface to the supervising lawyer / partner immediately |

## Tolling events

The limitation clock may be suspended or reset by:

- **Minority of the claimant**: in many civil-law systems, the clock does not run against minors (verify per jurisdiction).
- **Acknowledgment of debt**: if the debtor acknowledges the obligation in writing, many civil-law systems reset the clock. Advise clients to obtain written acknowledgment of debt from counterparties where the clock is running.
- **Ongoing negotiations**: some civil-law systems toll the period during active negotiations. This is jurisdiction-specific and should not be relied upon without verification.
- **Legal incapacity**: insolvency proceedings, force majeure events, or legal incapacity of the claimant may toll the period.
- **Agreement to toll**: parties may agree in writing to extend the limitation period in some jurisdictions (not all jurisdictions permit this).

## Common mistakes

| Mistake | Risk |
|---|---|
| Using the general period without checking for shorter specific periods | Claim may be barred by a shorter subject-matter-specific period |
| Miscalculating the accrual date | Entire limitation analysis is based on wrong start date |
| Assuming the general contract period applies to employment claims | Employment limitation periods are typically much shorter (1 year in UAE and KSA) |
| Relying on a statute period without verifying against current law | Periods may have changed by amendment |
| Treating KSA periods as definitive | KSA periods require local counsel verification; judicial discretion is real |

## Related skills

- [[heuristic-numbers-and-dates-double-check]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-refuse-if-no-jurisdiction-given]]
- [[kb-litigation-mena]]
