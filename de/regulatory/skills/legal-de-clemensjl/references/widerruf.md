# Widerrufsrecht

Status as at 05.08.2026. The right follows from **§ 312g Abs 1 BGB** in conjunction with **§ 355 BGB**; the periods and their expiry from **§ 356 BGB**; the information duty from **Art 246a § 1 Abs 2 EGBGB** with **Anlage 1** (Muster-Widerrufsbelehrung) and **Anlage 2** (Muster-Widerrufsformular); and since 19.06.2026 the electronic withdrawal function from **§ 356a BGB**.

The German term is **Widerruf**, never "Rücktritt". Rücktritt is a different institute (§§ 323, 346 BGB). An Austrian template speaking of "Rücktrittsrecht" and "Rücktrittsbelehrung" is rewritten, not renamed.

## Period and declaration

**§ 355 Abs 2 Satz 1 BGB:** the period is **14 days**. It begins with the conclusion of the contract unless otherwise provided.

**§ 355 Abs 1 BGB:** withdrawal is effected by a declaration to the trader. It must unambiguously express the decision to withdraw, needs no reasons, and dispatch in good time suffices. Requiring a specific form — registered letter, a form, a phone call — is ineffective.

**§ 356 Abs 2 BGB:** for a sale of goods the period does not begin before the consumer or a third party designated by them, other than the carrier, has received the goods; for an order of several goods delivered separately, on receipt of the last one; for delivery in several partial consignments, on receipt of the last one; for regular delivery over a defined period, on receipt of the first one.

**§ 356 Abs 3 BGB:** the period does not begin before the trader has informed the consumer in accordance with the requirements of Art 246a § 1 Abs 2 Satz 1 Nr 1 EGBGB.

**§ 356 Abs 4 BGB:** the right expires at the latest **twelve months and 14 days** after the point in time named in Abs 2 or § 355 Abs 2 Satz 2 BGB. A missing or defective Belehrung therefore costs a year of open withdrawal exposure, not a fine.

Note the numbering: the expiry rules for services are now in **§ 356 Abs 5 BGB** and for digital content in **§ 356 Abs 6 BGB**. Older templates and older commentary place them in Abs 4 and Abs 5. Check the Absatz before citing.

## Expiry in the two cases that matter online

**§ 356 Abs 5 BGB — services.** The right expires on full performance where the consumer has expressly consented to the trader beginning performance before the end of the withdrawal period, and has acknowledged that the right is lost on full performance.

**§ 356 Abs 6 BGB — digital content not on a tangible medium.** The right expires where the trader has begun performance and the consumer has expressly consented to the start before the end of the period and confirmed knowledge that consent causes the right to lapse.

Implementation: two separate, unticked checkboxes at the point of order, with the consent stored with a timestamp and the exact wording shown. A single combined checkbox does not satisfy either provision. The trader must also confirm the consent on a durable medium under § 312f BGB.

## Exceptions — § 312g Abs 2 BGB

Withdrawal is excluded, among others, for:

- goods not prefabricated where an individual choice or specification by the consumer is decisive, or which are clearly tailored to personal needs (Nr 1)
- goods liable to deteriorate rapidly or whose expiry date would be exceeded quickly (Nr 2)
- sealed goods unsuitable for return for health protection or hygiene reasons where the seal was removed after delivery (Nr 3)
- goods inseparably mixed with other goods after delivery (Nr 4)
- alcoholic beverages whose price was agreed at conclusion, delivery after 30 days, and whose value depends on market fluctuations (Nr 5)
- sealed audio or video recordings or computer software where the seal was removed after delivery (Nr 6)
- newspapers, periodicals and magazines, except subscription contracts (Nr 7)
- goods or services whose price depends on financial market fluctuations outside the trader's control (Nr 8)
- accommodation other than for residential purposes, carriage of goods, motor vehicle rental, catering, and services connected with leisure activities, where a specific date or period is provided (Nr 9)
- public auctions (Nr 10)
- urgent repairs or maintenance expressly requested by the consumer (Nr 11)
- betting and lottery services, subject to the stated qualifications (Nr 12)
- contracts notarially recorded (Nr 13)

Do not invent restrictions. "Only unopened", "only in original packaging", "only unworn" are not exceptions and turn into an unfair term.

## § 356a BGB — electronic Widerrufsfunktion, mandatory from 19.06.2026

Introduced by the Gesetz zur Änderung des Verbrauchervertrags- und des Versicherungsvertragsrechts sowie zur Änderung des Behandlungsvertragsrechts of 03.02.2026, BGBl. 2026 I Nr. 28, applicable from **19.06.2026**.

Where a distance contract is concluded via an **online user interface**, the trader must ensure the consumer can submit the withdrawal declaration through a **withdrawal function on that interface**.

- The function must be legible and labelled **"Vertrag widerrufen"** or an equivalent unambiguous formulation.
- It leads to a confirmation step with a separate confirmation function labelled **"Widerruf bestätigen"** or an equivalent unambiguous formulation.
- The function must be permanently available, prominently placed and easily accessible throughout the withdrawal period.
- It must allow the consumer to transmit their name, information identifying the contract, and electronic contact details for the acknowledgement.
- On activation, the trader must confirm receipt on a durable medium without undue delay, stating the content of the declaration and the **date and time** of receipt.

Consequence of omission: the same exposure as a defective Belehrung — the withdrawal period does not run properly and can extend to twelve months and 14 days (§ 356 Abs 4 BGB), plus abmahnfähig conduct under the UWG.

This is a **third** button, distinct from the § 312j Abs 3 BGB order button and the § 312k BGB cancellation button. Do not merge them and do not reuse the wording.

## Muster-Widerrufsbelehrung

Do not paraphrase. Take **Anlage 1 zu Art 246a § 1 Abs 2 Satz 2 EGBGB** verbatim, fill in the bracketed instructions, and keep the structure. Using the model correctly produces the statutory conformity presumption. The Muster-Widerrufsformular from **Anlage 2** must be provided in a form the consumer can store — a downloadable PDF or a copyable text block, not an image.

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h1>Widerrufsbelehrung</h1>
<p>[[Insert the current wording of Anlage 1 zu Art. 246a § 1 Abs. 2 Satz 2 EGBGB verbatim,
   with the trader's name, address, telephone number and e-mail address filled in, the
   correct variant for goods / services / digital content selected, and the return-cost
   clause chosen.]]</p>

<h2>Muster-Widerrufsformular</h2>
<p>[[Insert Anlage 2 zu Art. 246a § 1 Abs. 2 Satz 1 Nr. 1 EGBGB verbatim,
   downloadable and storable.]]</p>

<h2>Widerruf online erklären</h2>
<p>Sie können den Widerruf auch über unsere Widerrufsfunktion erklären:
   <a href="[[URL]]">Vertrag widerrufen</a></p>
```

## Checkpoints

- [ ] Term used is "Widerruf", never "Rücktritt"
- [ ] Period stated as 14 days, start correct for the contract type (§ 356 Abs 2 BGB)
- [ ] Belehrung wording taken from Anlage 1 zu Art 246a EGBGB, not paraphrased
- [ ] Trader's name, geographic address, telephone number and e-mail address inside the Belehrung
- [ ] Muster-Widerrufsformular from Anlage 2 provided and storable
- [ ] Return-cost allocation stated where the consumer is to bear them
- [ ] No invented restrictions on the right
- [ ] § 312g Abs 2 BGB exceptions applied only where they actually fit
- [ ] Digital content with immediate access: two separate unticked confirmations under § 356 Abs 6 BGB, stored with timestamp, confirmed under § 312f BGB
- [ ] Services started early: § 356 Abs 5 BGB consent obtained the same way
- [ ] § 356a BGB withdrawal function built: "Vertrag widerrufen" plus "Widerruf bestätigen", reachable without login, acknowledgement with date and time
- [ ] Absatz numbers checked against the current § 356 BGB, not against an older template
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
