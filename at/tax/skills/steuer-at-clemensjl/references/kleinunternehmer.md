# Kleinunternehmerregelung — § 6 Abs 1 Z 27 UStG and Art 6a UStG

Basis: § 6 Abs 1 Z 27 and Abs 3 UStG 1994, Art 6a UStG (Binnenmarktregelung), consolidated version as at 2026-08-05 (RIS). The regime was rewritten with effect from 2025-01-01 in implementation of Directive (EU) 2020/285. Anything written before 2025 about this regime is wrong on the threshold, on the arithmetic, and on cross-border availability.

## The domestic threshold

> "Kleinunternehmer ist ein Unternehmer, der sein Unternehmen im Inland oder in einem anderen Mitgliedstaat betreibt und dessen Umsätze nach § 1 Abs. 1 Z 1 und 2 die Umsatzgrenze von **55 000 Euro** (Kleinunternehmergrenze) im vorangegangenen Kalenderjahr nicht, und im laufenden Jahr noch nicht übersteigen." — § 6 Abs 1 Z 27 UStG

Three consequences that implementations get wrong:

1. **The figure is an actual turnover figure.** The last sentence of the provision: "Hinsichtlich der Berechnung der Kleinunternehmergrenze und des Schwellenwertes ist nicht auf die Bemessungsgrundlage bei unterstellter Steuerpflicht abzustellen." The pre-2025 exercise of grossing the net threshold up by the notional VAT rate is gone. Sum the actual consideration.
2. **Establishment in any member state qualifies**, not only Austria — subject to the extra conditions below.
3. Excluded from the count: Umsätze aus Hilfsgeschäften including Geschäftsveräußerungen, and turnover exempt under § 6 Abs 1 Z 8 lit d und j, Z 9 lit b und d, Z 10 bis 15, Z 17 bis 26 und Z 28.

## The tolerance rule

> "Wird die Kleinunternehmergrenze … überschritten, ist die Steuerbefreiung ab diesem Zeitpunkt nicht mehr anwendbar. Bei Überschreiten der Kleinunternehmergrenze um **nicht mehr als 10 %** kann die Steuerbefreiung jedoch noch bis zum Ende des Kalenderjahres in Anspruch genommen werden." — § 6 Abs 1 Z 27 UStG

| Turnover in the year | Effect |
|---|---|
| up to 55 000 € | exempt |
| over 55 000 € but not over 60 500 € (55 000 + 10 %) | exempt to the end of the calendar year; taxable from 1 January following |
| over 60 500 € | exemption falls away **from that moment**; the transaction that breaches the 10 % band and everything after it is taxable |

This is a hard billing-engine requirement: the running turnover total must be evaluated **per transaction**, not per month, because the switchover happens mid-invoice-run.

## The EU scheme — Art 6a UStG

An Austrian-established Unternehmer can claim the small-business exemption in other member states if:

- the **unionsweiter Jahresumsatz does not exceed 100 000 €** in the previous calendar year and not yet in the current one (Art 6a Abs 1), and
- a **Vorabmitteilung** has been filed through the BMF portal, and
- at least one member state confirms application of an exemption under Art 284 Abs 2 of Directive 2006/112/EG.

Procedure and deadlines from Art 6a:

| Step | Content | Deadline |
|---|---|---|
| Vorabmitteilung (Abs 2) | name, activity, legal form, e-mail, address; existing VAT-IDs and scheme identifiers; the target member states; turnover per member state for the current year, the previous year, and the year before that where that state requires it | before use |
| Issue of the Kleinunternehmer-Identifikationsnummer (Abs 3) | within **35 working days** of receipt of the Vorabmitteilung, unless a longer period is needed against evasion | — |
| Change notification (Abs 4) | any change to the Abs 2 data, including adding or dropping a target member state | without delay |
| Quarterly report (Abs 5) | turnover made in each member state, per calendar quarter | within **one month** of the end of the quarter |
| Threshold breach report (Abs 5) | the fact of exceeding 100 000 € plus the amount of supplies made from the start of the current quarter to the moment of the breach | within **15 working days** |

The identifier issued for this scheme carries the suffix **`-EX`** appended to the Austrian identifier. [[UNVERIFIED: the exact character layout of the Austrian `-EX` identifier — the suffix is confirmed by practitioner sources (KPMG Austria, ICON Tax News, February 2025) and by Art 284 Abs 3 of Directive 2006/112/EG, but Art 6a UStG itself does not spell out the format; confirm against the BMF portal registration screen before hard-coding a validation regex]]

For an Unternehmer established in **another** member state claiming the Austrian exemption, § 6 Abs 1 Z 27 adds: the 100 000 € union-wide test must be met, the Art 6a-equivalent procedure must have been applied for in the home state, and the exemption applies from the day the Kleinunternehmer-Identifikationsnummer is communicated — or, where one already exists, from the day the other member state confirms it for Austria.

Exceeding the 100 000 € union-wide threshold ends the exemption at that moment, with **no tolerance band** — the 10 % rule is written only for the Kleinunternehmergrenze.

## Invoicing as a Kleinunternehmer

- **No VAT is shown.** Not 0 %, not "USt 0,00 €". A tax amount shown without being owed is owed under § 11 Abs 14 UStG.
- The invoice must carry a **reference to the exemption**: § 11 Abs 1 Z 3 lit e requires "im Falle einer Steuerbefreiung einen Hinweis, dass für diese Lieferung oder sonstige Leistung eine Steuerbefreiung gilt". The statute prescribes the substance, not the exact sentence.
- The **simplified content of § 11 Abs 6** may be used regardless of amount, because that provision expressly covers invoices "die von einem Unternehmer ausgestellt werden, der die Steuerbefreiung in § 6 Abs. 1 Z 27 in Anspruch nimmt".
- No UID is printed unless one has actually been issued. § 11 Abs 1 Z 3 lit i requires the own UID only where the Unternehmer makes domestic supplies carrying a right to input VAT deduction — which the exemption removes.
- No input VAT deduction on purchases: the exemption in § 6 Abs 1 Z 27 is an exemption that excludes deduction.

### Wording used in practice (German, as issued)

```text
<!-- ENTWURF – steuerlich nicht freigegeben -->
Umsatzsteuerbefreit aufgrund der Kleinunternehmerregelung gemäß § 6 Abs 1 Z 27 UStG.
```

For an invoice issued under the EU scheme into another member state, add the identifier actually issued:

```text
Kleinunternehmer-Identifikationsnummer: [[AT________EX]]
Steuerbefreiung für Kleinunternehmen gemäß Art 284 der Richtlinie 2006/112/EG.
```

## Regelbesteuerungsantrag — § 6 Abs 3 UStG

> "Der Unternehmer, dessen Umsätze nach Abs. 1 Z 27 befreit sind, kann bis zur Rechtskraft des Bescheides gegenüber dem Finanzamt schriftlich — bzw. wenn der Unternehmer sein Unternehmen in einem anderen Mitgliedstaat betreibt, über das Portal des anderen Mitgliedstaates — erklären, dass er auf die Anwendung des Abs. 1 Z 27 verzichtet. Der Verzicht kann nur mit Wirkung vom Beginn eines Kalenderjahres ausgeübt werden und **bindet den Unternehmer mindestens für fünf Kalenderjahre** (Bindefrist zur Steuerpflicht)."

Implications for a product: the VAT status of a tenant is a **year-boundary** setting with a five-year lock-in, not a toggle. Model it as a dated status with an effective-from date and a minimum end date, and refuse mid-year flips.

## Checkpoints

- [ ] Threshold constant is 55 000 €, evaluated on actual turnover, not on a grossed-up net figure
- [ ] Running turnover is evaluated per transaction, not per period
- [ ] The 10 % band (to 60 500 €) keeps the exemption only to the end of the calendar year
- [ ] Beyond the band, the exemption drops at the breaching transaction and later invoices in the same run carry VAT
- [ ] Turnover from Hilfsgeschäfte and Geschäftsveräußerungen is excluded from the count
- [ ] Kleinunternehmer invoices show no VAT and no 0 % line
- [ ] Exemption reference printed on every such invoice
- [ ] Own UID suppressed unless one has actually been issued
- [ ] EU scheme: 100 000 € union-wide threshold tracked separately, with no tolerance band
- [ ] EU scheme: quarterly report due within one month, breach report within 15 working days
- [ ] VAT status stored as a dated status with a five-year Bindefrist where a Verzicht was declared
- [ ] `-EX` identifier format confirmed against the BMF portal before any validation regex ships
