---
name: consumer-report-ordering-codearranger
title: Consumer Report Ordering
description: 'Use this skill to order all consumer reports: Big-3 bureaus and specialty CRAs (C.L.U.E., The Work Number, tenant-screening, MIB, ChexSystems, NCTUE). Triggers include "order my credit report", "annualcreditreport.com", "free credit report", "specialty report", "CLUE report", "ChexSystems", "free report after adverse action", "I was denied credit", "data breach free report", "identity theft free report". Covers free-report entitlements (annual, post-adverse-action § 1681j(b), data-breach / identity- theft / unemployment), specialty-CRA directory, and non-delivery private right of action (§§ 1681n / 1681o). Produces report- request checklists, specialty-CRA request letters, and post- adverse-action demands. Composes with consumer-credit-disputes, consumer-report-accuracy, consumer-harm-documentation, consumer- credit-monitoring, state *-consumer-debt bundles, and state *-pro-se skills.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-federal-laws/skills/consumer-report-ordering
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Consumer Report Ordering

> **NOT LEGAL ADVICE.** This skill produces drafting aids and checklists. It is not legal advice
> and does not create an attorney-client relationship. Verify every deadline, dollar threshold,
> and statutory citation against current law before relying on or filing anything.

## Purpose

You cannot exercise a right you cannot see. The first move in any credit-report matter is to get
**every** report the consumer is entitled to — not just the Big-3, but the specialty agencies that
quietly drive insurance premiums, apartment denials, bank-account openings, and job offers.
Ordering reports is also what **surfaces the errors** that cause higher interest rates, denials,
and other financial harm — the harm that later supports a claim.

The canonical statutory text is in
[`../../references/federal-debt-laws/FCRA.md`](../../references/federal-debt-laws/FCRA.md)
(15 U.S.C. §§ 1681–1681x). Cite to it; do not paraphrase the statute from memory.

## What to order

### The Big-3 national credit bureaus
Equifax, Experian, TransUnion — order all three; their files differ, and an error often appears on
one but not the others.

### Nationwide specialty consumer-reporting agencies (CRAs)
Order these too — most consumers never see them, and they are exactly where stale or wrong data
causes overpayment and denials:

| Domain | Common agency | Drives |
|---|---|---|
| Auto/home insurance | LexisNexis **C.L.U.E.** | Premiums, policy denials |
| Employment history | The Work Number (Equifax) | Hiring, income verification |
| Tenant screening | Various (RealPage, TransUnion SmartMove, etc.) | Rental denials |
| Medical | **MIB** | Life/health/disability underwriting |
| Prescription | Milliman IntelliScript | Insurance underwriting |
| Checking / deposit | **ChexSystems**, Early Warning | New-account denials |
| Utility / telecom | **NCTUE** | Deposits, service denials |

A fuller list is maintained by the CFPB ("list of consumer reporting companies"). The skill should
direct the consumer there for current addresses and order links rather than hard-coding them.

## Free-report entitlements

Order through the right door so the report is **free** and the entitlement is documented:

1. **Annual free report** — via `annualcreditreport.com` (the only federally authorized site).
   Specialty CRAs must also provide a free annual file disclosure on request.
2. **After an adverse action** — when a consumer is denied (or charged more for) credit,
   insurance, employment, or a rental based on a report, they may request a **free** report from
   the CRA that supplied it. The statutory request window is **60 days** from the adverse-action
   notice (15 U.S.C. § 1681j(b); the notice itself is required by § 1681m). The source guidance is
   to act fast — within roughly **15 business days** — so the report is pulled while the denial is
   fresh and the harm is documentable. Treat 15 business days as a promptness target, not the
   statutory deadline.
3. **Other free triggers** — identity-theft / fraud-alert victims, victims of a **data breach**,
   consumers on **public assistance**, and the **unemployed** (intending to apply for work within
   60 days) are entitled to additional free reports. See § 1681j(c)–(d).

## When a bureau misses the deadline

If a CRA fails to deliver a report the consumer is entitled to within the required time, that
failure can itself be a violation supporting a **private right of action** (15 U.S.C. § 1681n for
willful noncompliance, § 1681o for negligent). Document the request date, the method, and the
non-delivery. See `consumer-harm-documentation` for preservation of the record, and
`consumer-credit-disputes` for the lawful dispute framework if the consumer chooses to pursue
one. The decision whether to dispute or to sue is the consumer's.

## Workflow

1. **Inventory** which reports the consumer needs (always Big-3; add specialty CRAs matching the
   harm — insurance premium hike → C.L.U.E.; bank-account denial → ChexSystems; apartment denial →
   tenant screening; etc.).
2. **Pick the cheapest lawful door** (annual vs. adverse-action vs. other free trigger) and record
   which entitlement is being invoked.
3. **Generate the request artifacts** (below), each dated, with proof-of-mailing guidance routed to
   `consumer-harm-documentation`.
4. **Diary the deadlines** for delivery; if missed, flag for the private-right-of-action analysis.

## Artifacts this skill drafts

- **Master report-request checklist** — every Big-3 + specialty CRA the consumer should order, the
  entitlement invoked for each, and a delivery-due date column.
- **Specialty-CRA request letter** — a per-agency letter requesting the free annual file disclosure
  (and the report-of-record), with identity-verification enclosures listed.
- **Post-adverse-action free-report demand** — references the adverse-action notice, invokes
  § 1681j(b), and requests the report relied upon within the statutory window.

Each artifact ends with the `NOT LEGAL ADVICE` disclaimer.

## Related federal authority

Beyond the FCRA sections above, route to these already-shared corpora:

- **Reg V (12 CFR Part 1022)** — the FCRA's implementing regulation:
  [`../../references/federal-debt-laws/Reg-V.md`](../../references/federal-debt-laws/Reg-V.md).
  §§ 1022.130–1022.142 govern the **free annual report** and the centralized source
  (annualcreditreport.com); § 1022.123 covers the **identity-theft summary of rights** a victim is
  entitled to receive.
- **ECOA § 1691(d) + Reg B § 1002.9** —
  [`../../references/federal-debt-laws/ECOA.md`](../../references/federal-debt-laws/ECOA.md) /
  [`../../references/federal-debt-laws/Reg-B.md`](../../references/federal-debt-laws/Reg-B.md).
  A credit **denial notice** is an adverse-action notice under ECOA / Reg B as well as FCRA
  § 1681m — cite both when a denial letter is the free-report trigger or the documented harm.

## Composition

- Errors found here → **`consumer-report-accuracy`** (PII, Date of First Delinquency, dispute
  marking) and **`consumer-credit-disputes`** (lawful dispute).
- Denial letters / non-delivery → **`consumer-harm-documentation`** (build the damages record).
- Ongoing ordering cadence → **`consumer-credit-monitoring`**.
- Underlying debt defense → the state **`*-consumer-debt`** bundle; pro-se mechanics → the state
  **`*-pro-se`** skill.
