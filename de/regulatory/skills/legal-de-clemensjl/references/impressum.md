# Impressum

Three layers apply in parallel: § 5 DDG for every commercial digital service, § 18 MStV for telemedia and journalistic-editorial content, and the company-law disclosure rules of § 35a GmbHG, § 80 AktG and § 37a HGB. One page can satisfy all three; none may be missing.

Accessibility: permanently available, easily recognisable and directly reachable. In practice a footer link labelled "Impressum" on every page, at most two clicks away, without login and not behind a consent layer.

## § 5 DDG — Allgemeine Informationspflichten

Status as at 05.08.2026. The DDG (Digitale-Dienste-Gesetz) of 06.05.2024, BGBl. 2024 I Nr. 149, entered into force on 14.05.2024 and replaced the TMG.

§ 5 Abs 1 DDG: providers of commercial digital services normally offered against payment must keep the following information permanently available, easily recognisable and directly reachable:

1. Name and address of the place of establishment; for legal persons additionally the legal form, the Vertretungsberechtigte, and — where capital figures are stated — the share capital and any outstanding contributions
2. Details allowing fast electronic contact and direct communication, including the e-mail address
3. Where the activity requires official authorisation: the competent supervisory authority
4. The Handelsregister, Vereinsregister, Partnerschaftsregister or Genossenschaftsregister with the registration number
5. For regulated professions: the Kammer, the Berufsbezeichnung and the state that conferred it, and the applicable Berufsrecht with a route to access it
6. The USt-IdNr. under § 27a UStG or the Wirtschafts-Identifikationsnummer, where held
7. For certain company forms: a statement that the company is in Abwicklung or Liquidation
8. For providers of audiovisual media services: the member state of establishment and the competent authorities

§ 5 Abs 2 DDG: further information duties under other provisions remain unaffected.

Number 2 means an e-mail address plus at least one second channel that yields a fast answer. A contact form alone is not enough.

## § 18 MStV — Informationspflichten

Status as at 05.08.2026. The MStV (Medienstaatsvertrag) has applied since 07.11.2020 and replaced the RStV.

- **Abs 1:** providers of telemedia that do not serve purely personal or family purposes must keep name and address readily recognisable, and for legal persons also the name and address of the Vertretungsberechtigter.
- **Abs 2:** providers of commercially operated telemedia with **journalistic-editorial** content must additionally name a **Verantwortlicher** with name and address. That person must be a natural person, permanently resident in Germany, not disqualified from public office by court judgment, of full legal capacity and able to be prosecuted.
- **Abs 3:** on social-media telemedia, content generated and posted automatically by a program controlling the user account must carry a legible notice saying so.

Journalistic-editorial means periodically produced, editorially selected and structured content aimed at the general public — blog, magazine, news section, curated advice content. A pure company presentation, portfolio or product page is not. Where the classification is arguable, name a Verantwortlicher: the cost is one line, the gap is actionable.

## Company-law disclosures

- **§ 35a Abs 1 GmbHG:** on all Geschäftsbriefe in whatever form addressed to a specific recipient — a website Impressum is treated as such in practice — legal form and seat, the Registergericht and Handelsregister number, and all Geschäftsführer with surname and at least one written-out first name. Where capital figures are given, the Stammkapital and any outstanding contributions.
- **§ 80 Abs 1 AktG:** the equivalent for the AG, including all Vorstandsmitglieder with the chair marked as such, and the chair of the Aufsichtsrat.
- **§ 37a HGB:** the equivalent for the eingetragener Kaufmann and the Personenhandelsgesellschaften.

Handelsregister numbers are HRA for Einzelkaufleute and Personengesellschaften, HRB for Kapitalgesellschaften. The register is kept by the Amtsgericht, never a Firmenbuch and never a Bezirksgericht.

## DSA contact point

Providers of intermediary services under Regulation (EU) 2022/2065 must designate a single point of contact for authorities (Art 11 DSA) and one for recipients of the service (Art 12 DSA) and publish the contact details. Easily accessible means, in practice, the Impressum. Details in `streitbeilegung-dsa.md`. The NetzDG was repealed on 14.05.2024; no NetzDG reporting duties remain.

## Template

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h1>Impressum</h1>
<p>Angaben gemäß § 5 DDG.</p>

<h2>Diensteanbieter</h2>
<p>
  [[Firma exactly as registered]]<br>
  [[Street and number]]<br>
  [[Postcode and town]], Deutschland
</p>

<h2>Kontakt</h2>
<p>
  E-Mail: <a href="mailto:[[address]]">[[address]]</a><br>
  Telefon: [[number]]
</p>

<h2>Unternehmensangaben</h2>
<p>
  Rechtsform: [[legal form]]<br>
  Vertretungsberechtigte Geschäftsführer: [[full names]]<br>
  Registergericht: Amtsgericht [[town]]<br>
  Registernummer: [[HRB … / HRA …]]<br>
  Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: [[DE………]]
</p>

<h2>Berufsrechtliche Angaben</h2>
<p>
  Berufsbezeichnung: [[title]] (verliehen in: Deutschland)<br>
  Zuständige Kammer: [[chamber, address, website]]<br>
  Berufsrechtliche Regelungen: [[named rules]], abrufbar unter [[URL]]<br>
  Zuständige Aufsichtsbehörde: [[authority and address — or: entfällt]]
</p>

<h2>Verantwortlicher für journalistisch-redaktionelle Inhalte gemäß § 18 Abs. 2 MStV</h2>
<p>
  [[Name of the natural person]]<br>
  [[Street and number]]<br>
  [[Postcode and town]]
</p>

<h2>Kontaktstelle gemäß Digital Services Act</h2>
<p>
  Kontaktstelle für Behörden (Art. 11 DSA) und für Nutzer (Art. 12 DSA): [[e-mail]]<br>
  Kommunikationssprachen: Deutsch, Englisch
</p>

<h2>Verbraucherstreitbeilegung</h2>
<p>[[see streitbeilegung-dsa.md — no ODR link]]</p>

<h2>Urheberrecht und Bildnachweis</h2>
<p>
  Die Inhalte dieser Website sind urheberrechtlich geschützt.<br>
  Bildquellen: [[photographer / stock provider / licence]]
</p>
```

## Checkpoints

- [ ] Reachable from every subpage in at most two clicks, no login, not behind the consent banner
- [ ] Link labelled "Impressum" — not "Über uns", "Kontakt" or "Legal"
- [ ] Address is a geographic address, not a PO box
- [ ] At least two contact channels, one of them e-mail (§ 5 Abs 1 Nr 2 DDG)
- [ ] Register court and number present where registered (§ 5 Abs 1 Nr 4 DDG, § 35a GmbHG)
- [ ] All Geschäftsführer or Vorstandsmitglieder named in full
- [ ] USt-IdNr. present where held; omitted, not invented, where not
- [ ] Supervisory authority named where the activity requires authorisation (§ 5 Abs 1 Nr 3 DDG)
- [ ] Kammer, Berufsbezeichnung, conferring state and access to the Berufsrecht for regulated professions (§ 5 Abs 1 Nr 5 DDG)
- [ ] § 18 Abs 2 MStV Verantwortlicher named where content is journalistic-editorial
- [ ] DSA contact points published where the service is an intermediary service
- [ ] No ODR link anywhere
- [ ] No § 5 TMG, no § 55 RStV, no NetzDG reference
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
