# Income side — orientation only

Short by intent. A developer building for small Austrian businesses meets these terms in field labels, report headings and onboarding questions, and needs to know what they select. **None of this is a basis for computing anyone's tax.** Every figure below is a threshold that decides which regime applies, not a calculation the software should perform. Where a product needs to state a tax position, that comes from the client's Steuerberater and is stored as input, not derived.

Basis: § 189 UGB, § 4 Abs 3 and § 17 EStG 1988, § 21 UStG. Consolidated versions as at 2026-08-05 (RIS). Status as at 2026-08-05.

## Einnahmen-Ausgaben-Rechnung versus Bilanzierung

`Einnahmen-Ausgaben-Rechnung` (EAR) is the cash-basis surplus computation under § 4 Abs 3 EStG. `Bilanzierung` is double-entry accounting with a balance sheet under the Drittes Buch UGB.

**§ 189 Abs 1 UGB** applies the Drittes Buch to:

- Kapitalgesellschaften (Z 1)
- eingetragene Personengesellschaften with no natural person as unlimited partner, and comparable chains (Z 2)
- **all other Unternehmer** — except those in Abs 4 — who achieve **more than 700 000 € Umsatzerlöse** in a financial year, measured per einheitlicher Betrieb (Z 3)

**§ 189 Abs 2** — when the threshold bites:

| Trigger | Effect |
|---|---|
| threshold exceeded in **two consecutive** financial years | duty starts from the **second following** financial year |
| threshold exceeded by **at least 300 000 €** (i.e. more than 1 000 000 €), or succession into a business whose predecessor was subject | duty starts from the **following** financial year |
| threshold not exceeded in two consecutive years | duty ends from the following financial year |

**§ 189 Abs 4** — the Drittes Buch does **not** apply to members of the freie Berufe, to farmers and foresters, or to Unternehmer whose income under § 2 Abs 4 Z 2 EStG is a surplus of receipts over expenses — even where the activity is carried on through a registered partnership, unless it is an Abs 1 Z 2 partnership. A freelance developer therefore stays outside the accounting duty however large the turnover, though other regimes still apply.

## Basispauschalierung — § 17 Abs 1 and 2 EStG

A flat-rate deduction of business expenses within an EAR.

| Item | Value **from the 2026 assessment** |
|---|---|
| Rate for freelance or trade income from commercial or technical consultancy, § 22 Z 2 activities, and writing, lecturing, scientific, teaching or educational activity | **6 %**, capped at **25 200 €** |
| Rate otherwise | **15 %**, capped at **63 000 €** |
| Base | Umsätze im Sinne des § 125 Abs 1 BAO |
| Prior-year turnover limit (§ 17 Abs 2 Z 2) | **not more than 420 000 €** |
| Precondition (§ 17 Abs 2 Z 1) | no accounting duty and no voluntary books permitting a § 4 Abs 1 profit determination |
| Lock-out after switching away (§ 17 Abs 3) | re-entry no earlier than after **five** Wirtschaftsjahre |

Only a closed list of expenses may be deducted in addition: goods, raw materials, semi-finished goods, auxiliary materials and ingredients enterable in a Wareneingangsbuch (§ 128 BAO); wages including ancillary costs and subcontracted labour going directly into the output; contributions under § 4 Abs 4 Z 1; costs under § 4 Abs 4 Z 5 second sentence; and travel costs matched by an equal reimbursement.

A separate **Kleinunternehmerpauschalierung** exists in § 17 Abs 3a EStG for taxpayers to whom the § 6 Abs 1 Z 27 UStG exemption applies to all turnover of the assessment year, or would but for a narrow exception. Different mechanics, different figures — read the provision before advising on it.

## SVS contribution base

Self-employed social insurance runs under the GSVG and is administered by the **SVS**. The contribution base sits between a monthly **Mindestbeitragsgrundlage** and a **Höchstbeitragsgrundlage**, both revalued annually.

Values for **2026**, read on the WKO Sozialversicherung page on 05.08.2026:

| Item | 2026 |
|---|---|
| Monatliche Mindestbeitragsgrundlage | **EUR 551,10** |
| Monatliche Höchstbeitragsgrundlage | **EUR 8.085,00** (einheitlich für KV, PV, UV und Betriebshilfe) |
| Pensionsversicherung | **18,5 %** |
| Krankenversicherung | **6,80 %** |
| Selbständigenvorsorge | **1,53 %** |
| Unfallversicherung | **EUR 12,95 im Monat, fix** — einkommensunabhängig, nicht prozentuell |

Resulting monthly floor across all four: about EUR 160,81; ceiling about EUR 2.182,17.

**These are annual values. Do not hard-code them.** Put them in a config the user updates each January from the SVS "Aktuelle Werte" sheet, and label them with the year in every output. The one that catches implementers is the Unfallversicherung: a flat monthly amount, so a pure percentage model is wrong at every income level, and wrong by the largest relative margin at the bottom.

What matters for software: the base is derived from the **income tax assessment**, which arrives years late, so SVS contributions are provisional and later reconciled. A product that shows a business owner their "profit after everything" must model provisional contributions and a reconciliation, or must not claim to show it at all.

## VAT filing rhythm — where the income side meets the invoicing side

| Item | Rule | Basis |
|---|---|---|
| Voranmeldung due | 15th day of the **second** following calendar month | § 21 Abs 1 UStG |
| Quarterly Voranmeldungszeitraum | prior-year turnover under § 1 Abs 1 Z 1 und 2 **not exceeding 100 000 €**; monthly may be chosen by filing for the first month of the year | § 21 Abs 2 UStG |
| Submission form | electronic, unless technically unreasonable | § 21 Abs 1 UStG |
| Zusammenfassende Meldung due | end of the **first** following month | Art 21 Abs 3 UStG — earlier than the UVA, see `leistungsort-grenzueberschreitend.md` |

## Hard pointer out

Whether a specific business must keep books, may use a Pauschalierung, which regime is cheaper, what the SVS base will be, and how a given expense is treated are **tax positions**. They are decided by a **Steuerberater** on the facts. This skill supplies the field, the threshold and the label — never the answer.

## Checkpoints

- [ ] Accounting regime stored as an input from the client's adviser, not derived by the software
- [ ] 700 000 € threshold, two-year rule and the 300 000 € acceleration modelled if the product advises on it at all
- [ ] Freie Berufe correctly excluded from the § 189 UGB duty
- [ ] Pauschalierung rates and caps read from dated configuration, not constants: 15 % / 63 000 €, 6 % / 25 200 €, limit 420 000 € from the 2026 assessment
- [ ] Five-year lock-out after leaving the Basispauschalierung represented
- [ ] SVS figures read from the annual SVS values sheet, never hard-coded
- [ ] Any "profit" or "take-home" figure shown to a user is labelled provisional where SVS reconciliation is pending
- [ ] UVA due on the 15th of the second following month; ZM at the end of the first following month
- [ ] Quarterly/monthly Voranmeldungszeitraum derived from the 100 000 € prior-year turnover test
- [ ] Every screen that could read as tax advice carries the pointer to the Steuerberater
