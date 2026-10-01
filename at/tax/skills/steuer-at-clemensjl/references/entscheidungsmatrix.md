# Decision matrix — business facts in, obligation set out

Run after `intake.md`, before writing anything. Every threshold below is verified against RIS, consolidated versions as at 2026-08-05.

## Step 1 — VAT status

| Prior-year turnover (§ 1 Abs 1 Z 1 und 2 UStG) | Current-year turnover | Status |
|---|---|---|
| ≤ 55 000 € | ≤ 55 000 € | Kleinunternehmer, exempt under § 6 Abs 1 Z 27 UStG |
| ≤ 55 000 € | > 55 000 € but ≤ 60 500 € | still exempt **to the end of the calendar year**; taxable from 1 January |
| ≤ 55 000 € | > 60 500 € | exempt until the breaching transaction, taxable from it |
| > 55 000 € | any | regular taxation from 1 January |
| any | any, but Verzicht under § 6 Abs 3 filed | regular taxation, bound for at least five calendar years |

Then: **exempt** → invoices without VAT, with the exemption reference, § 11 Abs 6 simplification available at any amount, no input VAT deduction, no own UID on invoices. **Taxable** → full § 11 Abs 1 Z 3 element set.

## Step 2 — Invoice obligation and shape

| Customer and amount | Duty | Shape |
|---|---|---|
| Business customer or juristische Person, any amount | mandatory, § 11 Abs 1 Z 1, within 6 months | full element set |
| Business customer, invoice total > 10 000 € | as above | **plus recipient UID**, § 11 Abs 1 Z 3 lit b |
| Any customer, invoice total ≤ 400 € | optional for consumers | Kleinbetragsrechnung, § 11 Abs 6 |
| Kleinunternehmer, any amount | as per customer type | § 11 Abs 6 content plus exemption reference |
| Consumer, above 400 € | optional (right, not duty) | full set if issued |
| Werklieferung/Werkleistung on a property, to a consumer | mandatory, § 11 Abs 1 Z 1 | full set |
| Intra-EU B2B service, recipient owes tax | mandatory, § 11 Abs 1 Z 2 | recipient UID, liability reference, **no VAT amount**, by the 15th of the following month, **no § 11 Abs 6 simplification** |

## Step 3 — Cash and point of sale

Evaluate **per Betrieb**:

| Annual turnover | Barumsätze (incl. card, vouchers) | Result |
|---|---|---|
| ≤ 15 000 € | any | no Registrierkassenpflicht. **§ 132a Beleg duty still applies** |
| > 15 000 € | ≤ 7 500 € | no Registrierkassenpflicht. **§ 132a Beleg duty still applies** |
| > 15 000 € | > 7 500 € | **Registrierkassenpflicht** from the beginning of the fourth month after the Voranmeldungszeitraum of first breach, § 131b Abs 1 Z 2 and Abs 3 BAO, plus full RKSV |
| any | zero cash of any kind | no § 131b duty; no § 132a duty in practice, since it attaches to cash payments received |

Then check whether an exemption removes both duties (§ 1 Abs 4 BarUV):

| Situation | Limit | Effect |
|---|---|---|
| Outdoor / door-to-door, not in enclosed premises | 45 000 € per calendar year and taxpayer | both duties off, § 131 Abs 4 Z 1 lit a BAO, § 2 BarUV |
| Hütten | same 45 000 € | both off, lit b |
| Buschenschank, ≤ 14 days per year | same 45 000 € | both off, lit c |
| Non-profit association canteen, ≤ 52 days per year | same 45 000 € | both off, lit d |
| Wirtschaftlicher Geschäftsbetrieb of a tax-privileged body, § 45 Abs 1, 1a, 2 BAO | — | both off, § 3 BarUV |
| Vending / service machine in operation after 2015-12-31 | ≤ 20 € per transaction | both off, § 4 BarUV |
| Ticket machine in operation after 2015-12-31, complete capture assured | — | § 131b off, § 5 BarUV |
| Online shop, no cash direct to the supplier, agreement via an online platform | — | **§ 131b off only**; § 132a unaffected, § 6 BarUV and § 131 Abs 4 Z 4 BAO |
| Supply away from the business premises | — | entry may be deferred to return, **Beleg must still be handed over at payment**, § 7 BarUV. Not for taxi/Mietwagen |

Machines in operation before 2016-01-01: §§ 4 and 5 BarUV take effect for them on **2027-01-01** (§ 9 Abs 2 BarUV).

## Step 4 — Cross-border

| Situation | Obligation |
|---|---|
| Domestic supplies only | nothing further |
| B2B goods to another member state | ZM, Art 21 Abs 3 UStG; exemption conditional on the ZM being filed, Art 7 Abs 1 Z 5 |
| B2B services to another member state, recipient owes tax under Art 196 | ZM; invoice with recipient UID and liability reference by the 15th of the following month |
| B2C goods distance sales + B2C digital services combined ≤ 10 000 € (previous and current year) | Austrian VAT, Art 3 Abs 5 and Art 3a Abs 5 UStG |
| Combined > 10 000 €, or waiver declared | destination-country VAT from the breaching transaction; register EU-OSS; waiver binds two calendar years |
| Imported goods sold to EU consumers, ≤ 150 € intrinsic value per consignment | IOSS available, § 25b UStG |
| Marketplace facilitating third-party supplies | check deemed-supplier status, § 3 Abs 3a UStG |
| Sales to Switzerland or other third countries | Ausfuhrlieferung § 7 UStG with export evidence; no ZM, no OSS; foreign registration may apply |
| Services received from foreign suppliers | reverse charge on the input side, § 19 Abs 1 second sentence |

## Step 5 — Filing rhythm

| Prior-year turnover | Voranmeldungszeitraum | UVA due | ZM due |
|---|---|---|---|
| ≤ 100 000 € | calendar quarter (monthly optional) | 15th of the second month after the quarter | end of the month after the quarter |
| > 100 000 € | calendar month | 15th of the second following month | end of the following month |

§ 21 Abs 1 and 2 UStG, Art 21 Abs 3 UStG. The ZM is always the earlier deadline.

## Step 6 — Records

Always: seven years from the end of the calendar year, § 132 Abs 1 BAO. Electronic invoices additionally need authenticity, integrity and legibility over the full period, § 11 Abs 2 UStG. With a Registrierkasse, add the DEP quarterly backups, the Startbeleg with its check result, the Jahresbeleg and any Schlussbeleg. See `aufbewahrung.md`.

## Worked examples

**Freelance developer, 48 000 € turnover, B2B clients in Austria and Germany, invoices by bank transfer only, no cash.**
Kleinunternehmer under § 6 Abs 1 Z 27 — but note that German B2B clients cannot use the exemption unless the Art 6a scheme is joined, so the supply into Germany is examined separately. No Registrierkassenpflicht and no Beleg duty in practice, because no cash is received. Invoices carry the § 11 Abs 6 content plus the exemption reference. ZM for the German B2B services if the Art 196 shift applies. Retention seven years.

**Café, 180 000 € turnover, 140 000 € of it cash and card.**
Regular taxation. Registrierkassenpflicht: both thresholds exceeded. Full RKSV — signature unit, FinanzOnline registration, Startbeleg, Monatsbeleg, Jahresbeleg, DEP with quarterly external backups. § 132a Beleg on every payment with the § 11 RKSV additions. Rate mix now spans 20 %, 10 % and, since 2026-07-01, 4,9 % on any qualifying Anlage 3 retail items — five amount buckets in the payload. Monthly UVA.

**Webshop, 900 000 € turnover, physical goods, EU-wide consumers, no shop counter.**
Regular taxation. No Registrierkassenpflicht: § 6 BarUV exempts online-shop turnover where no cash goes directly to the supplier — but the § 132a Beleg duty is expressly unaffected, so any cash-on-delivery or counter pickup needs a Beleg. 10 000 € pan-EU threshold long exceeded: destination rates and EU-OSS. ZM for any B2B supplies. Accounting duty under § 189 Abs 1 Z 3 UGB if the entity is not in Abs 4. Monthly UVA.

**Market stall, 38 000 € turnover, entirely cash, sells outdoors.**
Turnover and cash turnover both over the § 131b thresholds, **but** the supplies are made on public places outside enclosed premises and stay under the 45 000 € limit of § 131 Abs 4 Z 1 lit a BAO — so § 2 BarUV switches **both** the Registrierkassenpflicht and the Belegerteilungspflicht off, provided no individual records enabling turnover determination are kept (§ 1 Abs 1 BarUV). Simplified turnover determination by counting the till back, documented per till, at the latest at the start of the next working day (§ 1 Abs 2 and 3 BarUV). Kleinunternehmer status available.

## Checkpoints

- [ ] VAT status determined from actual prior-year and current-year turnover figures
- [ ] Cash-turnover figure separated from total turnover and evaluated per Betrieb
- [ ] Registrierkasse decision recorded with both thresholds and the start date computed
- [ ] Every claimed BarUV exemption recorded with its provision and the underlying figures
- [ ] Online-shop exemption not mistaken for a Beleg exemption
- [ ] Cross-border threshold evaluated on the combined goods-plus-digital-services total
- [ ] Filing rhythm derived from the 100 000 € test, with the ZM deadline set earlier than the UVA
- [ ] Result written down as an obligation list with the section number next to each item
