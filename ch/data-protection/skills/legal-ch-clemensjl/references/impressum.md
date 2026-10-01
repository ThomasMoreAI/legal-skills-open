# Impressum

Switzerland has no media-law disclosure duty and no telemedia act. The Impressum duty for online offerings sits in the unfair competition act.

## Art. 3 Abs. 1 lit. s UWG — the operative provision

Wording, Stand am 1. Januar 2025. Status as at 2026-08-05. Unlauter handelt insbesondere, wer:

> s. Waren, Werke oder Leistungen im elektronischen Geschäftsverkehr anbietet und es dabei unterlässt:
> 1. klare und vollständige Angaben über seine Identität und seine Kontaktadresse einschliesslich derjenigen der elektronischen Post zu machen,
> 2. auf die einzelnen technischen Schritte, die zu einem Vertragsabschluss führen, hinzuweisen,
> 3. angemessene technische Mittel zur Verfügung zu stellen, mit denen Eingabefehler vor Abgabe der Bestellung erkannt und korrigiert werden können,
> 4. die Bestellung des Kunden unverzüglich auf elektronischem Wege zu bestätigen;

Art. 3 Abs. 2 UWG: Absatz 1 Buchstabe s findet keine Anwendung auf die Sprachtelefonie und auf Verträge, die ausschliesslich durch den Austausch von elektronischer Post oder durch vergleichbare individuelle Kommunikation geschlossen werden.

Ziffer 1 is the Impressum. Ziffern 2–4 are process duties covered in `agb-vertragsschluss.md`.

**Scope.** The duty attaches to anyone who *offers* goods, works or services in electronic commerce. A purely informational site with no offer is outside lit. s; a site that solicits enquiries for paid services is inside it. When in doubt, publish the Impressum — the cost is a footer link, the exposure is criminal.

**Sanction.** Art. 23 Abs. 1 UWG: intentional unfair competition under Art. 3, 4, 5 or 6 is punishable **auf Antrag** with a custodial sentence of up to three years or a monetary penalty. Standing to file the complaint follows Art. 9 and 10 UWG, which includes competitors, customers, trade and consumer organisations, and the Confederation (Art. 10 Abs. 3 UWG).

## What "Identität und Kontaktadresse" means in practice

- Natural person: first name and surname. Legal entity: the Firma exactly as entered in the Handelsregister.
- A geographic address — street, number, postal code, place. Not a PO box alone.
- An email address is named in the statute and cannot be replaced by a contact form.
- A telephone number is not named in Art. 3 Abs. 1 lit. s UWG. Publish one anyway where the business promises support; omitting it is a business decision, not a legal one.

## Art. 954a OR — mandatory use of the registered name

Wording, Stand am 1. Januar 2026. Status as at 2026-08-05:

> 1 In der Korrespondenz, auf Bestellscheinen und Rechnungen sowie in Bekanntmachungen muss die im Handelsregister eingetragene Firma oder der im Handelsregister eingetragene Name vollständig und unverändert angegeben werden.
> 2 Zusätzlich können Kurzbezeichnungen, Logos, Geschäftsbezeichnungen, Enseignes und ähnliche Angaben verwendet werden.

For registered entities this means the Impressum shows the full registered Firma, not the brand name alone. Legal form, Sitz and UID belong there for the same reason: they are what identifies the entity in the register.

## Registration and identifiers

- Art. 931 Abs. 1 OR: a natural person running a business with turnover of at least CHF 100,000 in the last financial year must register the sole proprietorship at the place of establishment. Liberal professions and farmers are exempt unless the business is run commercially. Unregistered sole proprietorships and branches may register voluntarily (Abs. 3).
- Art. 930 OR: registered legal entities receive a UID under the UIDG (SR 431.03). Format CHE-###.###.###.
- Art. 26 Abs. 2 lit. a MWSTG: an invoice must state the supplier's name and place as used in business, the fact of registration in the register of taxable persons, and the registration number. That is the MWST number, conventionally written CHE-###.###.### MWST.

## Regulated professions and supervision

No general Swiss provision requires naming the supervisory authority in an Impressum. Sector acts do — FINMA-supervised financial services, Swissmedic-regulated products, cantonal health and legal professions each carry their own disclosure rules. Determine the sector rule; do not invent an "Aufsichtsbehörde" line by analogy to Austrian or German templates.

## Accessibility of the Impressum

Reachable from every page, without login and without passing a consent dialog. Label the link "Impressum" — in French "Mentions légales", in Italian "Impressum" or "Note legali". "About us" or "Legal" alone is not the same signal.

## Template

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h1>Impressum</h1>

<h2>Verantwortlich für diese Website</h2>
<p>
  [[Firma laut Handelsregister]]<br>
  [[Strasse Nr.]]<br>
  [[PLZ Ort]], Schweiz
</p>

<h2>Kontakt</h2>
<p>
  E-Mail: <a href="mailto:[[adresse]]">[[adresse]]</a><br>
  Telefon: [[Nummer oder: entfällt]]
</p>

<h2>Unternehmensangaben</h2>
<p>
  Rechtsform: [[Rechtsform]]<br>
  Sitz: [[Ort]]<br>
  Handelsregisteramt: [[Kanton]]<br>
  UID: [[CHE-###.###.###]]<br>
  MWST-Nummer: [[CHE-###.###.### MWST oder: nicht mehrwertsteuerpflichtig]]<br>
  Zeichnungsberechtigte Personen: [[Namen]]
</p>

<h2>Berufsrechtliche Angaben</h2>
<p>[[Berufsbezeichnung, Register, zuständige Behörde – oder: entfällt]]</p>

<h2>Urheberrecht und Bildnachweis</h2>
<p>
  Die Inhalte dieser Website sind urheberrechtlich geschützt.<br>
  Bildquellen: [[Fotografin / Stock-Anbieter / Lizenz]]
</p>
```

Publish an equivalent version in every language in which customers are addressed.

## Checkpoints

- [ ] Reachable from every subpage, no login, no consent dialog in front of it
- [ ] Link labelled "Impressum" / "Mentions légales" / "Note legali"
- [ ] Identity: full registered Firma or full personal name (Art. 3 Abs. 1 lit. s Ziff. 1 UWG, Art. 954a OR)
- [ ] Geographic address, not a PO box
- [ ] Email address present as a mailto link, not only a form
- [ ] Legal form, Sitz, Handelsregisteramt and UID present for registered entities
- [ ] MWST number present or expressly marked as not applicable
- [ ] Sector-specific supervisory disclosure checked against the actual sector act, not assumed
- [ ] A version exists in every language of address
- [ ] No § 5 TMG, § 5 DDG, § 5 ECG, MedienG, Blattlinie or Medieninhaber wording
- [ ] No ODR link
- [ ] All `[[…]]` placeholders resolved or reported as open
