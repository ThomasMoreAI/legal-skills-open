---
name: wa-post-judgment-codearranger
title: Washington Post-Judgment Procedure
description: Navigate post-judgment procedures in Washington State — motions to vacate under CR 60, garnishment under RCW 6.27, supplemental proceedings, exemption claims, and satisfaction of judgment. Use when the user asks about vacating a default judgment, responding to a wage garnishment or bank levy, exempting property from collection, answering supplemental interrogatories, or filing a satisfaction of judgment.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-post-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Exemptions
  path: references/exemptions.md
- title: Garnishment Response
  path: references/garnishment-response.md
- title: Motion To Vacate
  path: references/motion-to-vacate.md
- title: Satisfaction Of Judgment
  path: references/satisfaction-of-judgment.md
- title: Supplemental Proceedings
  path: references/supplemental-proceedings.md
---

# Washington Post-Judgment Procedure

When a judgment has been entered — against the defendant or for the
defendant — a separate body of rules governs what happens next. Pro
se defendants most often face post-judgment procedure in two
situations:

1. **A default judgment was entered against them** and they want to
   vacate it under CR 60
2. **A judgment creditor is collecting** — garnishment, bank levy,
   supplemental proceedings — and the debtor needs to know their
   rights and exemptions

This skill covers both angles.

> **NOT LEGAL ADVICE.** This skill is a procedural and drafting
> aid, not legal advice. Post-judgment outcomes turn on facts and
> deadlines specific to the user's case; verify every rule,
> deadline, and exemption against current law before filing. Pair
> with substantive review by counsel where stakes warrant.

## Core principles

1. **Vacation is about cause plus diligence** — CR 60 requires a
   specific ground (mistake, surprise, excusable neglect, void
   judgment, fraud) and reasonable promptness
2. **Exemptions protect the debtor** — federal and state law
   reserve essential income and property from collection; the
   debtor must **claim** the exemption or it is waived
3. **Garnishment is a formal process** — the creditor must serve
   the writ, the employer or bank must answer, and the debtor must
   receive notice of exemptions with an **Exemption Claim Form**
4. **Time limits are strict** — 1 year for CR 60(b)(1)-(3), 28
   days to respond to most supplemental proceedings, 21 days to
   return the Exemption Claim Form

## When to use this skill

Triggers include:

- "A default judgment was entered against me — how do I vacate it"
- "I just got served with a writ of garnishment"
- "My bank account was frozen"
- "My wages are being garnished"
- "What can the creditor take? What is exempt?"
- "I got a subpoena for a debtor's examination"
- "I paid the judgment — how do I file satisfaction"
- "The creditor is still trying to collect after I paid"
- "I want to appeal — or move to reconsider — the judgment"
- "Can they take my social security / unemployment / VA benefits?"

## The landscape

### If you are the judgment debtor

Primary statutes and rules:

- **CR 60 / CRLJ 60** — motion to vacate
- **RCW 6.27** — wage garnishment
- **RCW 6.13** — homestead exemption (cap framework keyed to
  county median sale price post-2021 reform — see chapter file
  for current formula)
- **RCW 6.15** — personal property exemptions
- **15 U.S.C. § 1673** — federal CCPA wage-garnishment cap (see
  federal-debt-laws corpus for current text)
- **RCW 6.32** — supplemental proceedings (debtor's exam)
- **CR 69 / RCW 6.17** — execution on judgments

### If you are the judgment creditor

(Less common for pro se, but sometimes relevant when a consumer
wins a counterclaim.)

- **RCW 6.17** — execution
- **RCW 6.27** — writ of garnishment (continuing lien on wages,
  one-shot lien on bank accounts)
- **RCW 4.56** — judgment procedures

## Motion to vacate — CR 60 / CRLJ 60

The most common pro se post-judgment motion: vacating a default
that was entered while the defendant was served but did not
respond.

See `references/motion-to-vacate.md` for the full template and
grounds analysis.

### Grounds (CR 60(b))

| Subsection | Ground | Time limit |
|------------|--------|-----------|
| (1) | Mistake, inadvertence, surprise, excusable neglect | 1 year |
| (2) | Newly discovered evidence | 1 year |
| (3) | Fraud, misrepresentation, misconduct | 1 year |
| (4) | Erroneous proceedings (new trial) | Reasonable time |
| (5) | Judgment is void | No fixed limit (but diligence required) |
| (6) | Satisfied, released, or discharged | Reasonable time |
| (7) | Judgment based on vacated prior judgment | Reasonable time |
| (8) | Unavoidable casualty / misfortune preventing defense | Reasonable time |
| (9) | Equitable relief — fraud on the court | No limit |
| (10) | Misidentification / no service (via CR 60(b)(5) void) | Reasonable time |
| (11) | Any other reason justifying relief | Reasonable time |

### Most common pro se grounds

- **Void for defective service** (CR 60(b)(5)) — sewer service,
  substitute service on non-resident
- **Excusable neglect** (CR 60(b)(1)) — missed deadline due to a
  valid reason
- **Fraud** (CR 60(b)(3)) — debt buyer misrepresented the debt
  or the chain of title

### Strategy

- **File quickly** — even if you have 1 year, courts weigh
  diligence. File within 30 days of learning of the judgment if
  possible
- **Lead with void service** if available — it sidesteps the
  discretionary "excusable neglect" analysis
- **Attach a meritorious defense** — Washington requires the
  moving party to show a prima facie defense (except on pure
  "void" grounds). Common defenses for pro se:
  - Lack of standing (debt-buyer case)
  - Statute of limitations
  - Lack of contract / lack of documentation
  - FDCPA / CPA counterclaim

## Responding to garnishment — RCW 6.27

If a writ of garnishment has been served on your employer (wage
garnishment) or bank (non-wage garnishment), you will receive
copies **by mail** along with notice of exemptions.

See `references/garnishment-response.md` for the detailed
process.

### Key deadlines

| Event | Deadline |
|-------|----------|
| Return Exemption Claim Form | Per RCW 6.27 — see `wa-deadlines` for current day count |
| Garnishee (employer / bank) files answer | Per RCW 6.27.190 — see `wa-deadlines` |
| Contest the garnishment | By motion; no fixed period but sooner is better |

### Exemptions — wages (continuing lien)

Washington's wage-garnishment exemption is more protective than
the federal CCPA cap (15 U.S.C. § 1673). RCW 6.27 sets the WA
percentage / multiplier framework. **Current cap percentages,
the multiplier (× state minimum wage), and the special consumer-
debt protection rate are amended periodically** — read
`wa-law-references/references/wa-rcw-debt/RCW-6_27.md` for the
current values rather than relying on memory. Low-income workers
whose disposable earnings fall below the statutory floor face
$0 garnishment.

### Exemptions — bank accounts / personal property

WA exempts categories of personal property from execution under
RCW 6.15. Categories include:

- Clothing and basic household goods (reasonable-value standard)
- Motor vehicles (capped at a dollar amount, plural permitted)
- Tools of trade (capped at a dollar amount)
- Bank account (capped at a dollar amount for individual debtors)
- Wedding ring and heirlooms (reasonable-value standard)
- Personal property of any kind (general wildcard, capped)

**The specific dollar caps for each category are amended
periodically by the Legislature.** See `RCW-6_15.md` for the
current cap on each category.

### Exemptions — homestead (RCW 6.13)

RCW 6.13 sets the WA homestead exemption. As of 2021, the cap is
keyed to county median sale price (not a fixed dollar amount,
which is unusual nationally — most states have a fixed homestead
cap). Automatic; no filing required. Applies to equity, not
market value. For the current per-county formula and any
adjustments, see `RCW-6_13.md`.

### Exemptions — Social Security, unemployment, VA, SSI

- **100% exempt** from garnishment under federal and state law
- Direct deposits are automatically protected by bank under
  31 C.F.R. § 212 (the federal bank-protection rule has its own
  lookback period; see the regulation for the current period)
- If wrongly frozen, notify the bank in writing of the exemption
  and file an Exemption Claim Form

### Filing the Exemption Claim Form

1. Complete the form sent with the writ
2. List all exempt funds or property
3. Sign under oath
4. **Send** to:
   - Court clerk (file the original or file electronically)
   - Creditor's attorney (by mail or email)
   - Garnishee (bank / employer) — so they know what to hold
5. Keep a copy

Court will schedule a hearing. If the creditor does not object
within the time allowed, the exemption is granted.

## Supplemental proceedings (debtor's exam) — RCW 6.32

A creditor may apply for an order requiring the debtor to appear
for examination under oath about income, assets, and bank
accounts.

### Rules

- Usually served by personal service
- Appearance is mandatory — failure is contempt (RCW 6.32.180)
- Questioning is broad — creditor may ask about all assets,
  income, bank accounts, employment, debts owed to you,
  transfers in the last 1-2 years
- Debtor may claim the 5th Amendment on specific criminal
  questions (rare but possible)

### Preparation

- Bring records of income and assets
- Know your exemptions cold — the creditor is hunting for
  non-exempt assets
- Be truthful — lying is contempt and possible perjury
- You may have counsel present — some courts allow pro bono
  clinics (Northwest Justice Project, King County Bar Housing
  Justice Project) to assist with supp proc

See `references/supplemental-proceedings.md` for prep guide.

## Satisfaction of judgment — RCW 4.56.100

When the judgment is paid, the judgment creditor **must file a
satisfaction** within 60 days of payment. If they do not:

- The debtor may file a motion to compel satisfaction
- Damages of up to $500 and attorney fees are available (RCW
  4.56.110)

### Partial satisfaction

If payment is partial, the creditor files a partial satisfaction
showing the amount credited and the remaining balance.

### Voluntary satisfaction by debtor

If the creditor refuses to file, the debtor can:

1. Send a demand letter
2. If still not filed, move the court for an order of
   satisfaction
3. Attach proof of payment (cleared check, bank record, money
   order stub)

See `references/satisfaction-of-judgment.md` for the motion and
demand-letter templates.

## Reconsideration and appeal

### CR 59 motion for reconsideration

- **10 days** from entry of judgment (CR 59(b))
- Narrow grounds — newly discovered evidence, manifest error of
  fact or law, irregularity in the proceedings, etc.
- Does not extend appeal deadline unless ruled on

### Appeal

- **30 days** from entry of a final order to file a Notice of
  Appeal (RAP 5.2)
- Goes to the **Washington Court of Appeals** from superior
  court
- District court (KCDC) appeals go to **superior court** as the
  appellate forum, per RALJ rules
- Transcript must be ordered within 30 days; designation of
  clerk's papers within 14 days

## Key-skill workflow — "I just got a default judgment — help me
vacate it"

1. **Verify the judgment** — pull the court docket, check
   service records, check whether you were actually served
2. **Identify the ground** — void service, excusable neglect,
   fraud
3. **Draft a meritorious defense** — the defense that would have
   been raised if the case had been contested
4. **Draft the motion and declaration** — under CR 60, with
   attached defense and evidence
5. **Note for Motion Docket** — schedule the hearing
6. **Serve opposing counsel**
7. **File** — superior court or district court per the
   originating court
8. **Prepare for argument** — use the wa-hearings skill
9. **If granted** — answer the complaint immediately; defend the
   case on the merits

## Key-skill workflow — "I got a writ of garnishment"

1. **Read the exemption notice** — sent with the writ
2. **Identify exempt funds** — wages below cap, Social
   Security, unemployment, VA, etc.
3. **Complete the Exemption Claim Form** within 21 days
4. **Serve** on court, creditor, and garnishee
5. **Attend the exemption hearing** if scheduled
6. **Negotiate payment** — if the debt is valid and funds are
   non-exempt, consider a payment plan to release the writ
7. **If wrongful** — if you believe the underlying judgment is
   void (default without service), file CR 60 in parallel to
   vacate the judgment itself

## References

- `references/motion-to-vacate.md` — CR 60 motion template, all
  grounds with specific pleadings
- `references/garnishment-response.md` — Exemption Claim Form,
  process, timing
- `references/exemptions.md` — Detailed exemption charts and
  authority
- `references/supplemental-proceedings.md` — Debtor's exam prep
- `references/satisfaction-of-judgment.md` — Satisfaction motion
  and demand letter

## Notes

- **Do not ignore a garnishment** — the money is gone within
  days if you miss the exemption claim deadline
- **Do not wait on a default judgment** — diligence matters
  under CR 60
- **Do not pay a time-barred debt** without legal review — a
  payment may **restart the statute of limitations** under RCW
  4.16.270
- **Do not sign a confession of judgment** without legal advice
  — it waives rights
- **Pro bono resources**: Northwest Justice Project (CLEAR
  hotline: 1-888-201-1014), King County Bar Consumer
  Representation Project, Washington Law Help
  (washingtonlawhelp.org)
