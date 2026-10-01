# Newsletter, advertising and sponsored content

Status as at 05.08.2026. Governing norms: **§ 7 UWG** for unsolicited advertising, **§ 5a Abs 4 UWG** for undisclosed commercial purpose, **§ 6 DDG** for commercial communications, and the DSGVO for the underlying processing.

## § 7 UWG — Unzumutbare Belästigungen

**Abs 1:** a commercial practice that unreasonably harasses a market participant is unlawful.

**Abs 2** treats the following as always unreasonable, among others:

- persistent solicitation against a recognisably unwanted contact
- **telephone advertising to a consumer without their prior express consent**, and to another market participant without at least presumed consent
- advertising by **automatic calling machine, fax or electronic mail without the addressee's prior express consent**
- advertising by electronic mail that conceals or disguises the sender's identity, that breaches § 6 Abs 1 DDG, or that gives no valid address to which the recipient can send an objection at basic transmission rates

**Abs 3 — the soft opt-in.** Advertising by electronic mail without express consent is permitted only where **all four** conditions hold:

1. the trader obtained the address **from the customer in connection with the sale of goods or services**
2. the address is used for **direct advertising for the trader's own similar goods or services**
3. the customer has not objected to the use
4. the customer is clearly and unmistakably informed, **on collection of the address and on every use**, that they may object at any time without incurring costs other than transmission costs at basic rates

"Similar" is read narrowly: the same need or a substitute product, not the whole catalogue. All four conditions must be documented, or the exemption cannot be relied on.

## Double opt-in

Not a statute, an evidence mechanism. Art 7 Abs 1 DSGVO places the burden of proving consent on the controller, and § 7 Abs 2 UWG requires prior express consent. Single opt-in cannot be proved against a denial and cannot exclude third-party sign-ups.

Requirements for the process:

- separate, unticked checkbox with a concrete purpose statement, not bundled into the AGB or the order
- confirmation e-mail that is **advertising-free**: only the confirmation link, the purpose and the identity. A confirmation e-mail carrying a voucher or product recommendation is itself unsolicited advertising.
- log per subscription: timestamp of sign-up, IP, timestamp of confirmation, the exact consent wording and its version
- one-click unsubscribe link in every mailing
- Impressum data in every mailing (§ 5 DDG applies to the mailing as a digital service)

## § 6 DDG — commercial communications

Status as at 05.08.2026. Commercial communications in digital services must be clearly identifiable as such; the natural or legal person on whose behalf they are made must be clearly identifiable; promotional offers such as discounts, premiums and gifts must be clearly identifiable as such and their conditions easily accessible and presented clearly and unambiguously; the same applies to promotional competitions and games. The successor to § 6 TMG — a text citing § 6 TMG is stale.

## § 5a Abs 4 UWG — Influencer and sponsored content

> Unlauter handelt auch, wer den kommerziellen Zweck einer geschäftlichen Handlung nicht kenntlich macht, sofern sich dieser nicht unmittelbar aus den Umständen ergibt, und das Nichtkenntlichmachen geeignet ist, den Verbraucher oder sonstigen Marktteilnehmer zu einer geschäftlichen Entscheidung zu veranlassen, die er andernfalls nicht getroffen hätte.

The 2022 UWG amendment added the qualification that, for the promotion of a **third party's** business, a commercial purpose exists only where consideration is received; consideration is rebuttably presumed unless the actor shows otherwise. Promotion of the actor's **own** business always has a commercial purpose.

Practical consequences:

- paid or otherwise compensated posts: label as **"Werbung"** or **"Anzeige"**, in German, at the start, visible without expanding the caption, not hidden among hashtags
- free products, press samples, trips and affiliate commissions count as consideration
- affiliate links are always commercial, including in one's own blog
- a foreign-language label ("ad", "sponsored", "PR sample") is not sufficient for a German-speaking audience
- Nr 11 of the Anhang zu § 3 Abs 3 UWG separately prohibits editorial content paid for without a clear indication

## Reviews and rankings

- **§ 5b Abs 3 UWG:** a trader who makes consumer reviews accessible must state whether and how they ensure the reviews originate from consumers who actually used the product.
- Nr 23b and Nr 23c of the Anhang zu § 3 Abs 3 UWG prohibit claiming that reviews are verified without taking reasonable steps, and submitting or commissioning false reviews.
- **§ 5b Abs 2 UWG:** where products are ranked in response to a search query, the main parameters determining the ranking and their relative weight must be disclosed.

## Template

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<label>
  <input type="checkbox" name="newsletter" value="1">
  Ich möchte den Newsletter von [[Firma]] mit Informationen zu [[concrete topics]]
  per E-Mail erhalten. Ich kann die Einwilligung jederzeit mit Wirkung für die Zukunft
  widerrufen, zum Beispiel über den Abmeldelink in jeder E-Mail.
  Hinweise zur Verarbeitung: <a href="/datenschutz">Datenschutzerklärung</a>.
</label>
```

Confirmation e-mail, advertising-free:

```text
Betreff: Bitte bestätigen Sie Ihre Newsletter-Anmeldung

Sie haben sich am [[date, time]] für den Newsletter von [[Firma]] angemeldet.
Bitte bestätigen Sie die Anmeldung: [[link]]

Wenn Sie sich nicht angemeldet haben, ignorieren Sie diese E-Mail.

[[Impressum block: Firma, Anschrift, Vertretungsberechtigte, Registergericht,
Registernummer, USt-IdNr., E-Mail]]
```

## Checkpoints

- [ ] Newsletter consent is a separate, unticked checkbox with a concrete purpose
- [ ] Double opt-in active, confirmation e-mail free of advertising
- [ ] Consent log with timestamp, IP and text version
- [ ] One-click unsubscribe link in every mailing
- [ ] Impressum data in every mailing
- [ ] Soft opt-in under § 7 Abs 3 UWG only where all four conditions are documented
- [ ] Objection notice given on collection **and** on every use
- [ ] No telephone advertising to consumers without prior express consent (§ 7 Abs 2 UWG)
- [ ] Commercial communications identifiable, promotional conditions accessible (§ 6 DDG)
- [ ] Sponsored content labelled "Werbung" or "Anzeige" in German, at the start, visible without expanding
- [ ] Affiliate links marked
- [ ] Review verification practice disclosed (§ 5b Abs 3 UWG)
- [ ] Ranking parameters disclosed where products are ranked (§ 5b Abs 2 UWG)
- [ ] No Austrian § 174 TKG or ECG-Liste reference
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
