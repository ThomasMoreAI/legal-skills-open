# Warranty, guarantee, and the absence of a withdrawal right

Two topics that imported templates get wrong in opposite directions: they invent a statutory return right that does not exist, and they assume a warranty regime that cannot be contracted out of, when in Switzerland it largely can. Wording from OR Stand am 1. Januar 2026. Status as at 2026-08-05.

## There is no general right of withdrawal for online purchases

Art. 40a–40f OR is the only statutory withdrawal regime in Swiss general contract law, and it is a doorstep-selling rule.

**Scope, Art. 40a OR.** The provisions apply to contracts over movable goods and services intended for the customer's personal or family use, where the supplier acted in the course of a professional or commercial activity **and the customer's performance exceeds CHF 100** (Abs. 1 lit. b). Abs. 2 excludes transactions concluded within existing financial-services contracts by financial institutions and banks; Abs. 2bis refers insurance contracts to the VVG.

**Situations covered, Art. 40b OR.** The customer may revoke their offer or acceptance where the offer was made:

> a. an seinem Arbeitsplatz, in Wohnräumen oder in deren unmittelbaren Umgebung;
> b. in öffentlichen Verkehrsmitteln oder auf öffentlichen Strassen und Plätzen;
> c. an einer Werbeveranstaltung, die mit einer Ausflugsfahrt oder einem ähnlichen Anlass verbunden war;
> d. am Telefon oder über vergleichbare Mittel der gleichzeitigen mündlichen Telekommunikation.

The list is exhaustive. Online shopping, ordering by email, ordering through an app and ordering from a catalogue are **not** in it. Lit. d covers telephone selling and comparable simultaneous *oral* telecommunication — a video call, not a webshop.

**Exceptions, Art. 40c OR.** No withdrawal right where the customer expressly requested the contract negotiations, or gave their declaration at a market or trade-fair stand.

**Information duty, Art. 40d OR.** Where the right exists, the supplier must inform the customer in writing or in another form permitting proof by text about the withdrawal right, its form and its period, and give their address. The information must be dated, allow the contract to be identified, and reach the customer such that they know it when they offer or accept.

**Period and effects, Art. 40e, 40f OR.** No form is required for the revocation; the customer bears the burden of proving it was timely. The period is **14 days** and starts once the customer has offered or accepted **and** has become aware of the Art. 40d information. Sending on the last day suffices. On revocation both sides return what they received; the customer owes an appropriate rent for use of an item, and reimbursement of expenses for services performed under Art. 402 OR, but no further compensation.

**Drafting consequence.** A Swiss webshop that grants returns does so voluntarily. Call it "Rückgaberecht" or "freiwilliges Rückgaberecht" and state its own terms. Never call it Widerrufsrecht, never cite Art. 40a ff. OR for it, and never copy a German Widerrufsbelehrung or an Austrian Rücktrittsbelehrung. If the shop also sells by telephone, the Art. 40a ff. OR regime applies to those contracts and needs its own, separate notice.

## Warranty for defects — Art. 197 ff. OR

**Art. 197 OR.** The seller is liable to the buyer both for warranted characteristics and for the absence of physical or legal defects that remove or materially diminish the item's value or its fitness for the intended use. Abs. 2: liability applies even where the seller did not know of the defects.

**Art. 200 OR.** No liability for defects the buyer knew at the time of purchase; for defects the buyer should have noticed with ordinary attention, only where the seller warranted their absence.

**Art. 201 OR — Mängelrüge.** The buyer must inspect the item as soon as customary in the ordinary course of business and notify the seller **immediately** of any defect. Failure to do so means the item counts as approved, except for defects not detectable on customary inspection. This duty has no counterpart in EU consumer sales law and is a genuine advantage for Swiss sellers — and a genuine trap for buyers.

**Remedies, Art. 205–208 OR.** The buyer chooses between rescission (Wandelung) and price reduction (Minderung); the court may award only the reduction where rescission is not justified by the circumstances (Art. 205 Abs. 2). For fungible goods the buyer may instead demand sound goods of the same kind, and the seller may discharge itself by immediate replacement plus damages (Art. 206). Art. 208 governs restitution on rescission.

There is **no statutory hierarchy of repair before replacement before reduction**. The EU sequence in the Sale of Goods Directive does not apply.

**Limitation, Art. 210 OR.** Claims prescribe two years after delivery, even if the buyer discovers the defect later, unless the seller assumed liability for a longer period (Abs. 1). Five years for defects in items incorporated as intended into an immovable work (Abs. 2).

Art. 210 Abs. 4 OR is the consumer floor:

> 4 Eine Vereinbarung über die Verkürzung der Verjährungsfrist ist ungültig, wenn:
> a. sie die Verjährungsfrist auf weniger als zwei Jahre, bei gebrauchten Sachen auf weniger als ein Jahr verkürzt;
> b. die Sache für den persönlichen oder familiären Gebrauch des Käufers bestimmt ist; und
> c. der Verkäufer im Rahmen seiner beruflichen oder gewerblichen Tätigkeit handelt.

All three conditions are cumulative. In B2B sales the two-year period can be shortened freely.

**Exclusion, Art. 199 OR.** An agreement abolishing or restricting the duty to warrant is invalid only where the seller fraudulently concealed the defects. The OR contains **no consumer-specific prohibition on excluding warranty**. That is the real Swiss position and it is what makes imported templates wrong. Two qualifications must always be stated with it: a blanket exclusion in consumer standard terms is exposed to Art. 8 UWG (significant and unjustified imbalance to the detriment of consumers, contrary to good faith), and Art. 210 Abs. 4 OR independently invalidates a shortening of the limitation period in consumer sales.

State both halves. A text that says only "warranty can be excluded" is as wrong as one that says only "two years, mandatory".

## Guarantee (Garantie)

A Garantie is a voluntary contractual undertaking, typically by the manufacturer or the seller, and is governed by its own terms. It is additional to the statutory warranty and cannot replace it silently. Where a guarantee is advertised, its content, duration, territorial scope and the person bearing it must be stated accurately — inaccurate statements are exposed to Art. 3 Abs. 1 lit. b UWG (misleading statements about goods or their business circumstances).

## Template fragment

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h2>Gewährleistung</h2>
<p>Es gelten die gesetzlichen Bestimmungen über die Gewährleistung nach Art. 197 ff.
des Obligationenrechts. Mängel sind unverzüglich nach Entdeckung anzuzeigen
(Art. 201 OR). Die Verjährungsfrist beträgt zwei Jahre ab Ablieferung
(Art. 210 Abs. 1 OR); bei gebrauchten Sachen beträgt sie [[ein Jahr / zwei Jahre]].</p>
<p>[[Falls eine Einschränkung nach Art. 199 OR vorgesehen ist: konkrete Beschreibung
der Einschränkung – und Hinweis darauf, dass die Verkürzung der Verjährungsfrist bei
Konsumentenkäufen nach Art. 210 Abs. 4 OR ungültig ist.]]</p>

<h2>Garantie</h2>
<p>[[Garantiegeberin, Inhalt, Dauer, räumlicher Geltungsbereich, Vorgehen im
Garantiefall – oder: Wir gewähren keine über die gesetzliche Gewährleistung
hinausgehende Garantie.]]</p>

<h2>Freiwilliges Rückgaberecht</h2>
<p>Ein gesetzliches Widerrufs- oder Rückgaberecht besteht bei Bestellungen über
diesen Online-Shop nicht. Wir gewähren freiwillig ein Rückgaberecht von
[[Anzahl]] Tagen ab Erhalt der Ware unter folgenden Bedingungen:
[[Zustand der Ware, Verpackung, Rücksendekosten, Erstattungsweg]].</p>
<p>[[Nur falls auch telefonisch verkauft wird: Bei Verträgen, die am Telefon
abgeschlossen werden, besteht ein Widerrufsrecht von 14 Tagen nach
Art. 40a ff. OR. Belehrung nach Art. 40d OR separat beilegen.]]</p>
```

## Checkpoints

- [ ] No statutory withdrawal right asserted for online orders
- [ ] Any return policy is labelled voluntary, with its own conditions
- [ ] Telephone sales, if any, have a separate Art. 40d OR notice and the CHF 100 threshold is checked
- [ ] Warranty section states the Art. 201 OR notification duty
- [ ] Limitation period stated correctly, with the used-goods distinction
- [ ] Any exclusion under Art. 199 OR is explicit, and checked against Art. 8 UWG
- [ ] No shortening of the limitation period below two years for new consumer goods (Art. 210 Abs. 4 OR)
- [ ] Guarantee and warranty are kept linguistically separate
- [ ] No repair-before-replacement hierarchy imported from EU law
- [ ] For EU-facing sales, the parallel CRD and Sale of Goods Directive position is addressed separately
