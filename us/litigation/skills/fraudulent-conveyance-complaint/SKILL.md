---
name: fraudulent-conveyance-complaint
title: Fraudulent Conveyance Complaint
description: 'Drafts a U.S. fraudulent conveyance complaint to avoid and recover debtor asset transfers under UFTA, UVTA, or state equivalents. Covers actual fraud (UVTA § 4(a)(1)), constructive fraud theories, badges of fraud, provisional remedies, and full prayer for relief. Use when a creditor needs to challenge a transfer made to hinder, delay, or defraud creditors, including bankruptcy adversary proceedings. Triggers: fraudulent conveyance, fraudulent transfer, voidable transaction, badges of fraud, asset concealment, debtor insolvency, UFTA, UVTA, avoidance action.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/fraudulent-conveyance-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fraudulent Conveyance Complaint

Drafts a litigation-ready complaint to avoid a debtor's fraudulent asset transfer and recover value for creditors under UFTA, UVTA, or state equivalents.

## Quick Start

Gather from the user:

1. **Creditor's claim** — nature of debt, date incurred, amount, judgment status
2. **Transfer details** — asset description (legal description if real property), date, transferee, stated vs. actual consideration
3. **Debtor financial condition** — insolvency evidence (balance sheet, cash-flow, or unreasonably small capital)
4. **Badges of fraud** — insider relationship, retention of control, concealment, timing, consideration adequacy
5. **Jurisdiction** — governing statute (UFTA, UVTA, or state-specific); federal vs. state court; bankruptcy adversary proceeding

Then produce the complaint following the workflow below.

## Core Workflow

### 1. Caption

```
[COURT NAME]
[DISTRICT/COUNTY]

[PLAINTIFF],
    Plaintiff,
v.
[DEBTOR-TRANSFEROR] and [TRANSFEREE],
    Defendants.

Case No. [________]
COMPLAINT FOR FRAUDULENT CONVEYANCE
```

Apply FRCP 10 (federal) or local rules (state).

### 2. Parties

| Party | Required Allegations |
|---|---|
| Plaintiff-creditor | Legal name, entity type, standing basis, nature and amount of debt |
| Debtor-transferor | Identity, entity type, insider status if applicable |
| Transferee | Identity, consideration paid, knowledge of debtor's intent |
| Subsequent transferees | Downstream recipients; good-faith purchaser status if asserted |

### 3. Jurisdiction & Venue

| Basis | Requirements |
|---|---|
| Federal diversity | 28 U.S.C. § 1332 — citizenship of each party, amount > $75,000 |
| Federal bankruptcy | 28 U.S.C. §§ 157, 1334 — adversary proceeding under FRBP 7001 |
| State court | Jurisdictional statute + amount-in-controversy threshold |
| Personal jurisdiction | Residence, principal place of business, property situs, or where transfer executed |
| Venue | Defendant's residence, where cause arose, or where property located |

### 4. Factual Allegations

Plead in numbered paragraphs, chronologically:

1. Origin, nature, and amount of claim; date debt incurred; judgment status
2. Whether claim is pre-transfer or post-transfer (determines available theories)
3. Debtor's financial condition at time of transfer — plead all that apply:
   - Liabilities exceeded assets at fair valuation (balance sheet insolvency)
   - Unable to pay debts as due (cash-flow insolvency)
   - Transfer left debtor with unreasonably small capital
4. Transfer description: asset, date, transferee, stated consideration, fair market value
5. Badges of fraud:

| Badge | Allegation |
|---|---|
| Insider transfer | Relationship: family member, officer, affiliate, controlled entity |
| Retention of control | Debtor continued to use, possess, or control asset post-transfer |
| Concealment | Transfer not recorded, disclosed, or reported to creditors |
| Substantially all assets | Scope of asset depletion relative to debtor's total estate |
| Inadequate consideration | FMV vs. consideration actually received |
| Timing | Transfer occurred [X days] before/after debt incurred or suit filed |
| Prior pattern | History of transfers or asset-shifting |

6. Transferee's actual or constructive knowledge of debtor's fraudulent intent (if applicable)

### 5. Causes of Action

**Count I — Actual Fraudulent Transfer**
- UVTA § 4(a)(1) [VERIFY state codification]
- Elements: (1) transfer by debtor; (2) actual intent to hinder, delay, or defraud any creditor
- Incorporate badges of fraud and direct evidence of intent
- Available to present and future creditors

**Count II — Constructive Fraud (Insolvency)**
- UVTA § 4(a)(2) [VERIFY state codification]
- Elements: (1) transfer without reasonably equivalent value; (2) debtor insolvent at time or became insolvent as result
- Plead in the alternative to Count I

**Count III — Constructive Fraud (Insider Antecedent Debt)** *(if applicable)*
- UVTA § 5(b) [VERIFY state codification]
- Elements: (1) transfer to insider; (2) for antecedent debt; (3) debtor insolvent; (4) insider had reasonable cause to believe debtor insolvent

**Additional claims** *(as applicable)*: conspiracy to defraud creditors, aiding and abetting, successor liability, lis pendens (real property — file with complaint)

### 6. Prayer for Relief

```
- [ ] Avoidance of the transfer to extent necessary to satisfy plaintiff's claim
- [ ] Recovery of transferred property or its value from transferee
- [ ] Money judgment against debtor for underlying debt (if not already obtained)
- [ ] Money judgment against transferee to extent of asset value received
- [ ] Attachment, garnishment, or receiver to preserve assets pending judgment
- [ ] Preliminary injunction against further dissipation (if imminent risk)
- [ ] Pre- and post-judgment interest at statutory rate
- [ ] Costs of suit
- [ ] Attorney's fees (if permitted by statute — verify jurisdiction)
- [ ] Such other relief as the court deems just and proper
```

### 7. Signature Block & Verification

- Attorney: name, bar number, firm, address, phone, email; FRCP 11 or state-equivalent certification
- **Verification**: many jurisdictions require verification for fraudulent conveyance complaints, especially when seeking provisional remedies — confirm local rules; some require notarization, others accept unsworn declaration under penalty of perjury

## Pitfalls

- **UFTA vs. UVTA** — Most states adopted UVTA (2014) but effective dates vary. [VERIFY] current state codification before citing section numbers.
- **Statute of limitations** — UVTA § 9: 4 years from transfer (actual fraud); 4 years or 1 year after discovery, whichever is later (constructive fraud). [VERIFY state equivalent.]
- **Bankruptcy intersection** — 11 U.S.C. § 548 reaches transfers within 2 years of petition; trustee may also invoke state UFTA/UVTA via § 544(b) for longer state limitations periods.
- **Good-faith defense** — Transferee who took for value and in good faith may retain the transfer. Plead facts negating good faith where known; affects remedy (avoidance vs. money judgment).
- **Reasonably equivalent value** — Distinct from fair market value; courts apply totality-of-circumstances. Inadequate price alone is not constructive fraud without insolvency.
- **Provisional remedies** — If dissipation risk is imminent, prepare TRO/preliminary injunction for concurrent filing; allege irreparable harm and likelihood of success.
- **Insider definition** — UVTA § 1(8) defines insiders broadly: relatives, general partners, directors, officers, affiliates. [VERIFY state definition.]
