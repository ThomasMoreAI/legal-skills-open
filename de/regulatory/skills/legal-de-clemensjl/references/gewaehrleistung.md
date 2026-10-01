# Gewährleistung, digital products and Garantie

Status as at 05.08.2026. Three regimes: goods under **§§ 434 ff, 474 ff BGB**, digital products under **§§ 327 ff BGB**, and voluntary guarantees under **§ 443 and § 479 BGB**.

Keep the vocabulary straight. **Gewährleistung** (statutory, mandatory, owed by the seller) is not **Garantie** (voluntary, additional, given by seller or manufacturer). A page that calls the statutory rights a "Garantie" misleads and is abmahnfähig.

## Goods — § 434 BGB

> **(1)** Die Sache ist frei von Sachmängeln, wenn sie bei Gefahrübergang den subjektiven Anforderungen, den objektiven Anforderungen und den Montageanforderungen dieser Vorschrift entspricht.

- **Abs 2 subjektive Anforderungen:** the agreed quality, fitness for the contractually presupposed use, and the agreed accessories and instructions.
- **Abs 3 objektive Anforderungen:** unless otherwise validly agreed, fitness for ordinary use and the quality customary in goods of that kind which the buyer can expect, including durability, quantity, functionality, compatibility, and the quality of a sample.
- **Abs 4 Montageanforderungen:** proper assembly, or improper assembly not attributable to the seller.
- **Abs 5:** delivery of a different thing counts as a defect.

Deviating from the objective requirements against a consumer requires, under **§ 476 Abs 1 Satz 2 BGB**, that the consumer was specifically informed of the deviation before the declaration of contract and that the deviation was expressly and separately agreed. A clause tucked into the AGB does not do it.

## Limitation and reversal of proof

- **§ 438 Abs 1 Nr 3 BGB:** the ordinary limitation period for claims under § 437 BGB is **two years** from delivery.
- **§ 477 BGB:** in a Verbrauchsgüterkauf, a defect appearing within **one year** of delivery is presumed to have existed at delivery.
- **§ 476 Abs 2 BGB:** limitation may not be made easier by agreement before notification of a defect where the result is a period shorter than **two years** from the statutory start, or shorter than **one year for used goods**. Any such agreement additionally requires the specific information and separate agreement under § 476 Abs 1 Satz 2 BGB.

"Gewährleistung 12 Monate" against a consumer buying new goods is void. So is any general exclusion of the statutory rights.

## Digital products — §§ 327 ff BGB

Applies to consumer contracts for the supply of digital content or digital services (§ 327 BGB), including where the consumer pays with data rather than money, and to goods with digital elements via § 327a BGB.

- **§ 327e BGB:** a Produktmangel exists where the product does not meet the subjective, objective and integration requirements.
- **§ 327f BGB — Aktualisierungen.** The trader must ensure that updates necessary to maintain conformity, **including security updates**, are supplied and that the consumer is informed about them, for the relevant period. For a continuous supply that is the whole supply period; otherwise it is the period the consumer can reasonably expect given the type and purpose of the product and the circumstances. Where the consumer fails to install a supplied update within a reasonable period, the trader is not liable for a defect caused solely by that failure, provided the trader informed the consumer about the update and the consequences of not installing it, and the failure was not caused by defective installation instructions.
- **§ 327j BGB:** limitation rules for digital products.
- **§ 327k BGB:** reversal of the burden of proof; for continuous supply it runs over the whole supply period.
- **§ 327r BGB:** changes to the digital product beyond what is necessary to maintain conformity require a contractual reservation, a valid reason, no additional cost, and notice; where the change impairs access or use more than insignificantly, the consumer may terminate.
- **§ 327q BGB:** the effect of withdrawal of data protection consent on the contract.

The update period must be a concrete statement on the product page. "Wir liefern Updates" is not an answer to § 327f BGB.

## Garantie — § 443 and § 479 BGB

**§ 479 Abs 1 BGB:** a Garantieerklärung must be drafted simply and comprehensibly and must contain

1. a reference to the consumer's statutory rights in case of defects, that exercising them is free of charge, and that they are not restricted by the guarantee
2. the name and address of the guarantor
3. the procedure the consumer must follow to invoke the guarantee
4. the goods to which the guarantee relates
5. the terms of the guarantee, in particular its duration and territorial scope

**§ 479 Abs 2 BGB:** the guarantee statement must be made available to the consumer on a durable medium at the latest at the time of delivery.

**§ 479 Abs 3 BGB:** where the manufacturer has given a Haltbarkeitsgarantie, the consumer has at least a claim to Nacherfüllung against the manufacturer during the guarantee period.

**§ 479 Abs 4 BGB:** failure to meet these requirements does not affect the validity of the guarantee obligation. The guarantee still binds the guarantor; the breach is an unfair-practice problem, not an escape route.

## Template

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h2>Gewährleistung</h2>
<p>Es gilt das gesetzliche Mängelhaftungsrecht. Ansprüche wegen eines Mangels verjähren
   bei neuen Waren in zwei Jahren ab Ablieferung (§ 438 Abs. 1 Nr. 3 BGB).
   [[for used goods: statement of the agreed one-year period, plus proof that the
   consumer was specifically informed and that the agreement was made expressly and
   separately as required by § 476 Abs. 1 Satz 2 BGB]]</p>

<h2>Aktualisierungen bei digitalen Produkten</h2>
<p>Wir stellen für [[product]] Aktualisierungen einschließlich Sicherheitsaktualisierungen
   bereit, die zum Erhalt der Vertragsmäßigkeit erforderlich sind, und informieren Sie
   darüber. Zeitraum: [[concrete period or: für die gesamte Dauer der Bereitstellung]]
   (§ 327f BGB).</p>

<h2>Garantie</h2>
<p>[[only where a guarantee is actually given — otherwise delete this section entirely]]<br>
   Garantiegeber: [[name and address]]<br>
   Garantierte Ware: [[goods]]<br>
   Dauer: [[duration]] · Räumlicher Geltungsbereich: [[scope]]<br>
   Verfahren zur Geltendmachung: [[procedure]]<br>
   Ihre gesetzlichen Mängelrechte bestehen unentgeltlich neben dieser Garantie und werden
   durch sie nicht eingeschränkt.</p>
```

## Checkpoints

- [ ] "Gewährleistung" and "Garantie" kept strictly apart in the wording
- [ ] No shortening below two years for new goods against a consumer (§ 476 Abs 2 BGB)
- [ ] Used-goods one-year period, where used, backed by the specific information and separate agreement under § 476 Abs 1 Satz 2 BGB
- [ ] No general exclusion of the statutory rights
- [ ] Update obligation under § 327f BGB addressed with a concrete period on the product page
- [ ] Goods with digital elements routed through § 327a BGB, not treated as plain goods
- [ ] Guarantee statement, where given, contains all five items of § 479 Abs 1 BGB
- [ ] Guarantee statement supplied on a durable medium by delivery at the latest (§ 479 Abs 2 BGB)
- [ ] Manufacturer Haltbarkeitsgarantie, where advertised, reflected accurately (§ 479 Abs 3 BGB)
- [ ] No Austrian VGG or "Gewährleistungsfrist nach ABGB" wording
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
