---
name: spain-tax-reporting-guilyx
title: Spanish tax reporting and filing — tax year 2025
description: Handle Spanish tax filing — the Renta campaign and its 30 June deadline, Modelo 100, Modelo 720 foreign asset reporting, quarterly Modelo 130 and 303 for the self-employed, and AEAT penalties. Use this whenever someone asks when the Spanish tax declaration is due, whether they must file, how to declare foreign assets or accounts, what Modelo 720 is, how to use the borrador or Cl@ve PIN, or what happens if they file late.
author: guilyx
author_url: https://github.com/guilyx/claude-tax-skills/tree/master/skills/spain-tax-reporting
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: tax
language: en
---

# Spanish tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Spain.

## Get the calendar

```bash
python -m taxcalc deadlines ES
```

## The Renta campaign

| Date | What |
| --- | --- |
| Early April 2026 | Campaign opens; borrador (draft) available online |
| 25 June 2026 | Deadline if paying by direct debit |
| 30 June 2026 | Deadline to file Modelo 100 for 2025 |
| 31 March 2026 | Modelo 720 foreign asset declaration |

The direct debit deadline being five days earlier catches people every year.

## Download the datos fiscales before doing anything else

AEAT publishes the data it already holds on you — employment income, withholding,
bank interest, property references. Start from that rather than from the
borrador, because the borrador makes assumptions (typically about family
circumstances and regional deductions) that are often wrong and are silently
accepted if you just confirm it.

## Modelo 720

Foreign assets must be reported by category — accounts, securities, and real
estate — where any category exceeds 50,000. Once filed, it only needs refiling
when a category grows by more than 20,000 or an asset is disposed of.

The historic penalty regime was struck down by the EU Court of Justice in 2022
as disproportionate, and the confiscatory penalties are gone. **The obligation
itself remains**, with ordinary penalties. Be accurate about this: older
guidance online is alarmist in a way that is no longer correct, and newer
guidance sometimes wrongly suggests the requirement was abolished.

## Who must file

Residents with employment income above 22,000 from a single payer, or above
15,876 where a second payer paid more than 1,500. Anyone with business income,
rental income or capital gains files regardless of amount. Note that having two
employers in a year — common after changing jobs — frequently pushes someone
over the lower threshold unexpectedly.

## Autónomos

Quarterly Modelo 130 instalments (20 April, 20 July, 20 October, 30 January) and
quarterly Modelo 303 for VAT, plus the annual Modelo 390 summary. These are
separate from the Renta and separately penalised.

## Penalties

A fixed 100–200 where no tax was due. Where tax is due, a surcharge of 1% plus
1% per month of delay, rising to 15% plus interest after twelve months — but
only if you file voluntarily. Once AEAT contacts you, penalties of 50% to 150%
of the unpaid amount apply instead. Filing late voluntarily is therefore far
better than waiting, and worth saying explicitly.
