# Distance selling, AGB, order process and prices

Status as at 05.08.2026. The pre-contractual information duty sits in **§ 312d Abs 1 BGB** and refers to **Art 246a EGBGB**; the ordering process is governed by **§§ 312i, 312j BGB**; prices by the **PAngV** (Preisangabenverordnung 2022); AGB by **§§ 305 to 310 BGB**.

## § 312d Abs 1 BGB

> Bei außerhalb von Geschäftsräumen geschlossenen Verträgen und bei Fernabsatzverträgen ist der Unternehmer verpflichtet, den Verbraucher nach Maßgabe des Artikels 246a des Einführungsgesetzes zum Bürgerlichen Gesetzbuche zu informieren.

The information provided becomes part of the contract unless the parties expressly agree otherwise. For distance contracts about financial services, § 312d Abs 2 BGB refers to Art 246b EGBGB instead, and adds design requirements for the online interface under Art 246b § 4 EGBGB.

## Art 246a § 1 Abs 1 EGBGB — information before the contract

The catalogue covers, among others:

- the essential characteristics of the goods or services
- identity of the trader, geographic address, telephone number and e-mail address, and where different the address for complaints
- the total price including all taxes and charges, or the manner of calculation, plus all shipping, delivery and postal charges and any other costs
- for continuing obligations: the total costs per billing period, minimum term and conditions of termination
- payment, delivery and performance arrangements and the delivery date
- the existence of the statutory Mängelhaftung and, where offered, after-sales service and commercial guarantees
- duration of the contract and conditions of termination
- functionality, compatibility and interoperability of goods with digital elements and of digital content and services
- the possibility of access to out-of-court complaint and redress mechanisms

**Art 246a § 1 Abs 2 EGBGB** adds, where a withdrawal right exists, the conditions, time limits and procedure for exercising it, plus the **Muster-Widerrufsformular** — see `widerruf.md`.

**Anlage 1 zu Art 246a § 1 Abs 2 Satz 2 EGBGB** contains the Muster-Widerrufsbelehrung. **Anlage 2** contains the Muster-Widerrufsformular. Using the model correctly filled in produces the statutory conformity presumption; deviating from it puts the burden on the trader.

The information must be given on a durable medium or, where the contract is concluded electronically, in a way that lets the consumer store and reproduce it.

## § 312j Abs 2 and 3 BGB — the order process

**Abs 2:** immediately before the consumer places the order, the trader must make available clearly and legibly the essential characteristics, the total price, shipping costs, the duration of the contract and any minimum term.

**Abs 3:** the order situation must be designed so that the consumer, when ordering, expressly acknowledges that they undertake a payment obligation. Where the order is placed via a button, that button must be labelled legibly

> **mit nichts anderem als den Wörtern „zahlungspflichtig bestellen" oder mit einer entsprechenden eindeutigen Formulierung**

**Abs 4:** a contract concluded in breach of Abs 2 or Abs 3 does not bind the consumer. This is not a fine, it is unenforceability of the whole contract.

Acceptable equivalents in practice: "kostenpflichtig bestellen", "zahlungspflichtigen Vertrag schließen", "kaufen". Not acceptable: "Bestellung absenden", "Weiter", "Jetzt anmelden", "Bestellung abschicken", "Jetzt gratis testen" for a paid subscription.

## § 312i BGB — general electronic commerce duties

Technical means to detect and correct input errors before submission, confirmation of receipt of the order without undue delay by electronic means, and the ability to retrieve and store the contract terms including the AGB.

## § 312l BGB — online marketplaces

An operator of an online marketplace must inform the consumer in accordance with **Art 246d EGBGB**. § 312l Abs 2 BGB defines an online marketplace as a service allowing consumers to conclude distance contracts with other traders or consumers through software operated by or on behalf of the trader, including a website, part of a website, or an application. Core content of Art 246d EGBGB: the main parameters determining ranking and their relative importance, whether the third party offering the goods is a trader, and — where they are not — the notice that consumer protection law does not apply to that contract.

## Preisangabenverordnung

- **§ 3 PAngV:** the Gesamtpreis, that is the price including VAT and all other price components, must be stated. Additional shipping costs must be stated separately and be clearly identifiable.
- **§ 4 PAngV — Grundpreis:** whoever offers goods to consumers by weight, volume, length or area must state, alongside the total price, the **Grundpreis** unmistakably, clearly and legibly. § 4 Abs 3 PAngV lists the exemptions.
- **§ 11 Abs 1 PAngV — Preisermäßigungen:** whoever announces a price reduction for goods must state the **lowest total price applied to consumers in the 30 days before the reduction**. § 11 Abs 2 covers stepwise uninterrupted reductions; § 11 Abs 4 exempts individual price reductions and reductions for perishable goods where the reason is identified. A struck-through "UVP" or "statt"-price without the 30-day reference is a PAngV breach and abmahnfähig.

## AGB

Measured against §§ 305 to 310 BGB. Recurring problems in generated terms:

- clauses limiting the statutory Mängelhaftung against consumers — void under § 476 Abs 1 BGB
- shortening the limitation period for new goods against a consumer below the statutory period — see `gewaehrleistung.md`
- blanket disclaimers of liability for intent or gross negligence, or for injury to life, body or health — void under § 309 Nr 7 BGB
- reservation of the right to change terms unilaterally without a substantive trigger — § 308 Nr 4 BGB
- a Gerichtsstand clause against a consumer — ineffective, § 38 ZPO
- an arbitration or class-action-waiver clause imported from a US template — ineffective under §§ 307 ff BGB
- Widerrufsbelehrung buried inside the AGB instead of being given as its own information

The AGB must be retrievable and storable before the order is placed (§ 312i Abs 1 Satz 1 Nr 4 BGB) and incorporated under § 305 Abs 2 BGB.

## Template — checkout summary and order button

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<section aria-labelledby="bestelluebersicht">
  <h2 id="bestelluebersicht">Ihre Bestellung</h2>
  <!-- § 312j Abs. 2 BGB: directly above the button, clearly and legibly -->
  <ul>
    <li>[[product]] — [[essential characteristics]]</li>
    <li>Menge: [[quantity]]</li>
    <li>Preis: [[gross price]] EUR inkl. [[rate]] % USt.</li>
    <li>Versandkosten: [[shipping]] EUR</li>
    <li><strong>Gesamtpreis: [[total]] EUR</strong></li>
    <li>Lieferung: [[delivery window]] nach [[country]]</li>
    <li>[[for continuing obligations: Laufzeit [[term]], Kündigungsfrist [[period]],
        Gesamtkosten je Abrechnungszeitraum [[amount]] EUR]]</li>
  </ul>

  <label>
    <input type="checkbox" name="agb" required>
    Ich habe die <a href="/agb">AGB</a> und die
    <a href="/widerrufsbelehrung">Widerrufsbelehrung</a> zur Kenntnis genommen.
  </label>

  <!-- § 312j Abs. 3 BGB: nothing other than this wording on the button -->
  <button type="submit">zahlungspflichtig bestellen</button>
</section>
```

## Template — price display

```html
<p>
  <span class="price">[[gross price]] EUR</span>
  <span class="vat">inkl. [[rate]] % USt.</span>
  <span class="shipping">zzgl. <a href="/versand">Versandkosten</a></span>
  <!-- § 4 PAngV, where the goods are sold by weight, volume, length or area -->
  <span class="unit-price">([[base price]] EUR / [[unit]])</span>
</p>

<!-- § 11 Abs. 1 PAngV, only where a price reduction is announced -->
<p class="reduction">
  Aktionspreis [[new price]] EUR ·
  Niedrigster Gesamtpreis der letzten 30 Tage: [[lowest 30-day price]] EUR
</p>
```

## Checkpoints

- [ ] All Art 246a § 1 Abs 1 EGBGB items present before the order
- [ ] Order button labelled "zahlungspflichtig bestellen" or an unambiguous equivalent, and nothing else (§ 312j Abs 3 BGB)
- [ ] Order summary immediately above the button with characteristics, total price, shipping, term (§ 312j Abs 2 BGB)
- [ ] Input-error correction available before submission (§ 312i Abs 1 Satz 1 Nr 1 BGB)
- [ ] Order receipt confirmed electronically without undue delay
- [ ] Contract terms including AGB retrievable and storable
- [ ] Total price including VAT stated; shipping costs stated separately and identifiably (§ 3 PAngV)
- [ ] Grundpreis stated where § 4 PAngV applies
- [ ] Every price-reduction claim backed by the 30-day lowest price (§ 11 PAngV)
- [ ] Delivery date and any delivery restrictions stated
- [ ] No pre-ticked add-ons (§ 312a Abs 3 BGB)
- [ ] AGB screened against §§ 307 to 309 BGB, no US or Austrian clauses
- [ ] Marketplace operators: Art 246d EGBGB ranking and trader-status information present
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
