# Email, telephone and advertising rules

Swiss direct marketing law sits in the UWG, not in a telecommunications or data protection act. Enforcement is criminal on complaint and civil, with standing for competitors, customers, consumer organisations and the Confederation. Wording from UWG Stand am 1. Januar 2025 and FMG Stand am 1. Juni 2026. Status as at 2026-08-05.

## Mass electronic advertising — Art. 3 Abs. 1 lit. o UWG

> o. Massenwerbung ohne direkten Zusammenhang mit einem angeforderten Inhalt fernmeldetechnisch sendet oder solche Sendungen veranlasst und es dabei unterlässt, vorher die Einwilligung der Kunden einzuholen, den korrekten Absender anzugeben oder auf eine problemlose und kostenlose Ablehnungsmöglichkeit hinzuweisen; wer beim Verkauf von Waren, Werken oder Leistungen Kontaktinformationen von Kunden erhält und dabei auf die Ablehnungsmöglichkeit hinweist, handelt nicht unlauter, wenn er diesen Kunden ohne deren Einwilligung Massenwerbung für eigene ähnliche Waren, Werke oder Leistungen sendet;

Three cumulative requirements for mass advertising sent by telecommunications means without a direct connection to requested content:

1. **prior consent** of the customer,
2. the **correct sender** indicated,
3. a reference to an **easy and free refusal option**.

Missing any one of the three makes the sending unfair.

**Existing-customer exception.** Whoever obtains customer contact information **in the course of selling** goods, works or services and points out the refusal option **at that moment** may send mass advertising for **their own similar** goods, works or services without consent. Four elements, all required: the data came from a sale (not from a download, a competition or a newsletter form alone), the refusal option was flagged at collection, the recipient is that customer, and the advertising concerns the sender's own similar offering. Cross-selling an unrelated product line falls outside it.

"Massenwerbung" means advertising sent to an indeterminate number of recipients. A genuinely individual message is outside lit. o — but a mail-merge to a list is not individual.

**Double opt-in is not a statutory requirement in Switzerland.** It is the practical way to discharge the burden of proving consent, which lies with the sender. Log timestamp, IP, the wording consented to and the confirmation event; keep the confirmation email free of advertising content.

Every mailing needs sender identification and a working one-click unsubscribe. Include the Impressum details in the mailing: a commercial email that offers goods or services is itself electronic commerce under Art. 3 Abs. 1 lit. s UWG, although Art. 3 Abs. 2 UWG excludes contracts concluded exclusively by individual email exchange.

## Telephone marketing — Art. 3 Abs. 1 lit. u, v, w UWG

> u. den Vermerk im Telefonverzeichnis nicht beachtet, dass ein Kunde keine Werbemitteilungen von Personen erhalten möchte, mit denen er in keiner Geschäftsbeziehung steht, und dass seine Daten zu Zwecken der Direktwerbung nicht weitergegeben werden dürfen; Kunden ohne Verzeichniseintrag sind den Kunden mit Verzeichniseintrag und Vermerk gleichgestellt;
> v. Werbeanrufe tätigt, ohne dass eine Rufnummer angezeigt wird, die im Telefonverzeichnis eingetragen ist und zu deren Nutzung er berechtigt ist;
> w. sich auf Informationen stützt, von denen sie oder er aufgrund eines Verstosses gegen die Buchstaben u oder v Kenntnis erhalten hat;

The Sterneintrag is the asterisk marker in the telephone directory. Since the amendment in force from 1 January 2021, **persons with no directory entry at all are treated the same as those with an entry and a marker**. In practice that means: no cold calling of mobile numbers that are not listed, and no cold calling of anyone whose number is not in the directory. Lit. w extends liability to anyone who builds on data obtained through a lit. u or v breach.

Lit. v requires a displayed caller number that is entered in the directory and that the caller is entitled to use. Number suppression and spoofed CLI for advertising calls are unfair per se.

Art. 45a FMG obliges telecommunications providers to combat unfair advertising under Art. 3 Abs. 1 lit. o, u and v UWG, and empowers the Federal Council to define the measures. That is a duty on carriers, not a defence for advertisers.

## Environmental and climate claims — Art. 3 Abs. 1 lit. x UWG

> x. Angaben über sich, seine Waren, Werke oder Leistungen in Bezug auf die verursachte Klimabelastung macht, die nicht durch objektive und überprüfbare Grundlagen belegt werden können.

Inserted by the act of 15 March 2024, **in force since 1 January 2025** (AS 2024 376). "Klimaneutral", "CO2-kompensiert", "net zero by 2030" and similar claims now require objective, verifiable substantiation held by the advertiser. Keep the substantiation on file before publishing the claim, not after a complaint.

## Other UWG hooks that catch marketing copy

- Art. 3 Abs. 1 lit. b UWG: incorrect or misleading statements about oneself, one's goods, works, services, prices, stock, or business circumstances.
- Art. 3 Abs. 1 lit. e UWG: comparative advertising that is incorrect, misleading, unnecessarily disparaging or parasitic.
- Art. 3 Abs. 1 lit. h UWG: particularly aggressive sales methods impairing freedom of decision.
- Art. 3 Abs. 1 lit. t UWG: promising a prize in a competition or draw whose redemption is tied to a premium-rate number, an expense contribution, a purchase, or attendance at a sales event, promotional trip or further draw.

## Sanctions and standing

Art. 23 Abs. 1 UWG: intentional unfair competition under Art. 3 is punishable **on complaint** with a custodial sentence of up to three years or a monetary penalty. Art. 10 UWG gives standing to customers, to professional and business associations, to consumer protection organisations of national or regional importance, and to the Confederation where the public interest requires it — including where the interests of several persons or collective interests are threatened (Abs. 3 lit. b). Art. 10 Abs. 4 UWG allows the Federal Council to inform the public about unfair conduct, naming the firms concerned.

Advertising self-regulation runs through the Schweizerische Lauterkeitskommission (faire-werbung.ch), whose decisions are not binding but are widely followed and frequently reported.

## Template fragments

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h2>Newsletter-Anmeldung</h2>
<label>
  <input type="checkbox" name="newsletter_consent" required>
  Ich möchte den Newsletter von [[Firma]] mit Informationen zu
  [[konkrete Inhalte]] per E-Mail erhalten. Ich kann diese Einwilligung
  jederzeit widerrufen, indem ich auf den Abmeldelink in jeder E-Mail klicke
  oder eine Nachricht an [[E-Mail]] sende.
</label>
```

```text
Footer jeder Aussendung:

[[Firma]], [[Adresse]], Schweiz – [[E-Mail]]
Sie erhalten diese E-Mail, weil Sie sich am [[Datum]] für unseren Newsletter
angemeldet haben. Abmelden: [[Ein-Klick-Link]]
```

For the existing-customer route, the refusal notice must appear at the point of sale, for example directly under the email field in the checkout, not only in the AGB.

## Checkpoints

- [ ] Consent is separate, not pre-ticked, and names the sender and the content
- [ ] Consent evidence stored with timestamp, IP, wording version and confirmation event
- [ ] Every mailing names the correct sender and carries a free one-click unsubscribe
- [ ] Existing-customer route, if relied on, satisfies all four elements of Art. 3 Abs. 1 lit. o UWG, with the point-of-sale notice documented
- [ ] No purchased or scraped address lists
- [ ] Telephone campaigns screened against directory markers, and unlisted numbers excluded (Art. 3 Abs. 1 lit. u UWG)
- [ ] Advertising calls display a directory-registered number the caller may use (lit. v)
- [ ] Climate and environmental claims have objective, verifiable substantiation on file (lit. x)
- [ ] Comparative claims and price claims checked against Art. 3 Abs. 1 lit. b and e UWG
- [ ] Competition and prize mechanics checked against Art. 3 Abs. 1 lit. t UWG
- [ ] For EU recipients, the parallel ePrivacy and GDPR consent standard is met as well
