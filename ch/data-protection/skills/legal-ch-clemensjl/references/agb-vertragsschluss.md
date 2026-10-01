# Contract formation and AGB

Swiss contract law is in the OR (SR 220). There is no consumer contract code, no information-duty catalogue comparable to the EU Consumer Rights Directive, and no statutory list of unfair terms. What exists instead is a short set of e-commerce process duties in the unfair competition act, a general unfairness clause, and judge-made rules on incorporating standard terms. Wording from OR Stand am 1. Januar 2026 and UWG Stand am 1. Januar 2025. Status as at 2026-08-05.

## Formation — Art. 1–10 OR

- Art. 1 OR: a contract requires the mutual, concurring expression of intent.
- Art. 3–5 OR: an offer with a time limit binds until it expires; an offer to an absent party binds until a timely reply could be expected.
- Art. 6a OR: sending an unsolicited item is not an offer; the recipient need neither return nor keep it, but must notify the sender if the item was obviously sent by mistake.
- Art. 7 Abs. 1 OR: the offeror is not bound if the offer carries a disclaimer or if such a reservation follows from the nature of the transaction or the circumstances.
- Art. 7 Abs. 2 OR: sending tariffs, price lists and the like is not in itself an offer.
- Art. 7 Abs. 3 OR: **displaying goods with a stated price is as a rule an offer.**

Art. 7 Abs. 3 OR is the provision that matters for a shop. Left alone, a product page with a price can be construed as a binding offer, so that the customer's order concludes the contract and a pricing error is the seller's problem. The standard fix is an express reservation in the AGB and at the checkout: the presentation is a non-binding invitation, the customer's order is the offer, and the contract comes into existence only with the seller's acceptance. Distinguish that acceptance from the technical order acknowledgement required by Art. 3 Abs. 1 lit. s Ziff. 4 UWG — one email can do both jobs only if it says clearly which it is.

## E-commerce process duties — Art. 3 Abs. 1 lit. s Ziff. 2–4 UWG

Whoever offers goods, works or services in electronic commerce acts unfairly if they fail to:

> 2. auf die einzelnen technischen Schritte, die zu einem Vertragsabschluss führen, hinzuweisen,
> 3. angemessene technische Mittel zur Verfügung zu stellen, mit denen Eingabefehler vor Abgabe der Bestellung erkannt und korrigiert werden können,
> 4. die Bestellung des Kunden unverzüglich auf elektronischem Wege zu bestätigen;

Art. 3 Abs. 2 UWG excludes voice telephony and contracts concluded exclusively by exchange of email or comparable individual communication.

Intentional breach is punishable on complaint under Art. 23 Abs. 1 UWG with a custodial sentence of up to three years or a monetary penalty.

There is **no statutory button-labelling rule** in Switzerland. The German "zahlungspflichtig bestellen" requirement of § 312j BGB and the Austrian § 8 FAGG have no Swiss counterpart. A clearly labelled order button is still good practice and reduces exposure under Art. 3 Abs. 1 lit. b UWG, but do not cite a Swiss provision that does not exist.

## AGB: incorporation and content control

There is no Swiss statute on standard terms comparable to the EU Unfair Terms Directive. Two controls operate.

**Incorporation, by case law.** Under the Ungewöhnlichkeitsregel developed by the Bundesgericht, a clause in globally accepted standard terms is not incorporated if it is unusual for the party in question and the party did not have to expect it, judged from the perspective of the weaker or less experienced party at the time of signing, and the more so the more the clause alters the character of the contract or departs materially from the statutory position. The practical consequence: unusual clauses must be highlighted specifically, not buried. This is judge-made law, not a statutory article — do not cite an article number for it.

**Content control, by statute.** Art. 8 UWG, in the version in force since 1 July 2012:

> Unlauter handelt insbesondere, wer allgemeine Geschäftsbedingungen verwendet, die in Treu und Glauben verletzender Weise zum Nachteil der Konsumentinnen und Konsumenten ein erhebliches und ungerechtfertigtes Missverhältnis zwischen den vertraglichen Rechten und den vertraglichen Pflichten vorsehen.

Art. 8 UWG applies only to consumer contracts, contains no blacklist and no greylist, and requires both a significant and an unjustified imbalance contrary to good faith. Standing to sue follows Art. 9 and 10 UWG, which includes consumer organisations of national or regional importance and the Confederation.

Art. 8a UWG additionally prohibits parity clauses imposed by accommodation-booking platforms on accommodation businesses.

## Geoblocking — Art. 3a UWG

In force since 1 January 2022. Unfair conduct includes discriminating against a customer **in Switzerland** in distance trade, without objective justification, on grounds of nationality, domicile, place of establishment, the seat of their payment service provider or the place of issue of their payment instrument, by: discriminating on price or payment conditions (lit. a); blocking or restricting access to an online portal (lit. b); or redirecting them without their consent to a version of the portal other than the one they sought (lit. c). Abs. 2 exempts a list of sectors including financial services, electronic communications services, public transport, healthcare, gambling, private security, social services and audiovisual services.

Note the direction: Art. 3a UWG protects customers **in Switzerland**. It does not oblige a Swiss shop to serve EU customers.

## Template fragment

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h2>Vertragsschluss</h2>
<p>Die Darstellung der Produkte im Online-Shop ist kein bindendes Angebot, sondern
eine unverbindliche Aufforderung zur Bestellung. Mit dem Absenden der Bestellung
geben Sie ein verbindliches Angebot ab. Der Vertrag kommt zustande, sobald wir Ihre
Bestellung ausdrücklich annehmen oder die Ware versenden.</p>
<p>Der Eingang Ihrer Bestellung wird unverzüglich elektronisch bestätigt. Diese
Eingangsbestätigung ist noch keine Annahme.</p>

<h2>Ablauf der Bestellung</h2>
<ol>
  <li>Produkt auswählen und in den Warenkorb legen</li>
  <li>Warenkorb prüfen, Adress- und Zahlungsdaten eingeben</li>
  <li>Übersichtsseite mit allen Angaben; Eingaben können über die Schaltfläche
      «Zurück» oder durch direkte Bearbeitung der Felder korrigiert werden</li>
  <li>Bestellung absenden</li>
  <li>Elektronische Eingangsbestätigung</li>
</ol>

<h2>Vertragssprache und anwendbares Recht</h2>
<p>Vertragssprache ist [[Sprache]]. Es gilt Schweizer Recht unter Ausschluss des
Übereinkommens der Vereinten Nationen über Verträge über den internationalen
Warenkauf (CISG). [[Gerichtsstand]]</p>
```

Where consumers domiciled in the EU are targeted, a choice of Swiss law does not deprive them of the mandatory consumer protection of their habitual residence; see `eu-crossborder.md`.

## Checkpoints

- [ ] The product page either carries a binding-offer reservation or the shop accepts that Art. 7 Abs. 3 OR makes it an offer
- [ ] The technical steps leading to contract conclusion are described (Art. 3 Abs. 1 lit. s Ziff. 2 UWG)
- [ ] An input-error correction mechanism exists before the order is placed (Ziff. 3)
- [ ] An immediate electronic order acknowledgement is sent (Ziff. 4), and it says whether it is an acceptance
- [ ] AGB are presented before the order is placed and can be saved
- [ ] Unusual clauses are highlighted separately, not buried in the body
- [ ] Consumer-facing AGB reviewed against Art. 8 UWG for significant and unjustified imbalance
- [ ] No pre-ticked add-ons or optional services
- [ ] Geoblocking behaviour checked against Art. 3a UWG for customers in Switzerland
- [ ] No citation of § 312j BGB, § 8 FAGG or a Swiss "Bestellbutton" duty that does not exist
- [ ] Choice of law and jurisdiction clauses checked against Art. 32 ZPO and, for EU customers, Rome I and the Lugano Convention
