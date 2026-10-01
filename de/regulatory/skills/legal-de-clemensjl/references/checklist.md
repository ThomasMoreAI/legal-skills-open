# Pre-launch checklist

Run before go-live. Every finding is reported with the norm and the location, not as a general remark. Anything technically verifiable is verified technically, not judged from intent.

## Technical pass first

These four steps produce half the findings in a few minutes:

1. Load the site in a fresh browser profile with the network tab open. Note every third-party domain contacted **before** a consent decision.
2. Application tab: record every cookie, LocalStorage and IndexedDB entry present before the decision.
3. Full-text search the whole project — including shop system texts, e-mail templates, invoice templates and marketplace shop descriptions — for: `TMG`, `TTDSG`, `RStV`, `NetzDG`, `odr`, `Online-Streitbeilegung`, `OS-Plattform`, `ec.europa.eu/consumers`, `ECG`, `MedienG`, `FAGG`, `Rücktrittsrecht`, `Firmenbuch`, `Bezirksgericht`, `ATU`, `GISA`.
4. Walk the order flow and the cancellation flow once with the keyboard only, no mouse.

## Impressum

- [ ] Reachable from every page in at most two clicks, link labelled "Impressum"
- [ ] Reachable without consent and without login
- [ ] Name, geographic address, legal form, Vertretungsberechtigte (§ 5 Abs 1 Nr 1 DDG)
- [ ] E-mail plus a second fast contact channel (§ 5 Abs 1 Nr 2 DDG)
- [ ] Supervisory authority where the activity requires authorisation (Nr 3)
- [ ] Register and registration number (Nr 4, § 35a GmbHG, § 80 AktG, § 37a HGB)
- [ ] Kammer, Berufsbezeichnung, conferring state, applicable Berufsrecht with access (Nr 5)
- [ ] USt-IdNr. under § 27a UStG where held (Nr 6)
- [ ] Liquidation notice where applicable (Nr 7)
- [ ] § 18 Abs 2 MStV Verantwortlicher named for journalistic-editorial content
- [ ] DSA contact points where the service is an intermediary service
- [ ] Cites § 5 DDG — not § 5 TMG, not § 55 RStV, not § 5 ECG

## Data protection

- [ ] Datenschutzerklärung present, reachable without consent and without login
- [ ] Every processing operation with purpose, legal basis, recipients, retention
- [ ] Legitimate interests named concretely
- [ ] Every service that actually fires is listed — reconciled against the network capture
- [ ] Third-country transfers listed individually with the transfer instrument
- [ ] Data subject rights complete, withdrawal right stated
- [ ] Correct **Landes**datenschutzbehörde named with address and website
- [ ] Age threshold stated as 16 (Art 8 Abs 1 DSGVO, no German derogation)
- [ ] § 38 BDSG headcount check done against the threshold of 20, result documented
- [ ] Verarbeitungsverzeichnis, AVV, TOM and breach process exist internally

## Cookies and tracking

- [ ] No third-party request before the consent decision
- [ ] No non-essential cookie, LocalStorage or IndexedDB entry before the decision
- [ ] Reject on the first layer, same visual weight as accept
- [ ] No pre-ticked categories, no consent by scrolling
- [ ] Granular choice per purpose
- [ ] Withdrawal as easy as consent, permanent footer link
- [ ] Consent log with timestamp and text version
- [ ] Web fonts served locally
- [ ] Maps, video, captcha and social embeds behind consent or click-to-load
- [ ] Cites § 25 TDDDG — not § 25 TTDSG, not § 15 TMG

## Shop and distance selling

- [ ] Order button labelled "zahlungspflichtig bestellen" or an unambiguous equivalent (§ 312j Abs 3 BGB)
- [ ] Order summary immediately above the button (§ 312j Abs 2 BGB)
- [ ] Total price including VAT, shipping stated separately and identifiably (§ 3 PAngV)
- [ ] Grundpreis where § 4 PAngV applies
- [ ] Every price-reduction claim backed by the 30-day lowest price (§ 11 PAngV)
- [ ] Delivery date and delivery restrictions stated
- [ ] Input-error correction available (§ 312i Abs 1 Satz 1 Nr 1 BGB)
- [ ] Order confirmation sent electronically without undue delay
- [ ] AGB retrievable and storable, screened against §§ 307 to 309 BGB
- [ ] All Art 246a § 1 Abs 1 EGBGB items present
- [ ] No pre-ticked add-ons (§ 312a Abs 3 BGB)
- [ ] Marketplace operators: Art 246d EGBGB information present

## Withdrawal

- [ ] Term used is "Widerruf", never "Rücktritt"
- [ ] Belehrung taken from Anlage 1 zu Art 246a § 1 Abs 2 Satz 2 EGBGB, not paraphrased
- [ ] Muster-Widerrufsformular from Anlage 2 provided and storable
- [ ] Period and start correct for the contract type (§ 356 Abs 2 BGB)
- [ ] Return-cost allocation stated where the consumer bears them
- [ ] Digital content with immediate access: two separate unticked confirmations (§ 356 Abs 6 BGB), stored with timestamp
- [ ] Services started early: § 356 Abs 5 BGB consent obtained the same way
- [ ] No invented restrictions on the right
- [ ] **§ 356a BGB Widerrufsfunktion built** — "Vertrag widerrufen" plus "Widerruf bestätigen", permanently available, no login, acknowledgement with date and time. Mandatory since 19.06.2026.

## Cancellation button

- [ ] Continuing obligation concluded online: § 312k BGB applies — including where payment is one-off (BGH I ZR 161/24)
- [ ] Button labelled "Verträge hier kündigen", confirmation button "jetzt kündigen"
- [ ] Permanently available, no login, not behind the consent banner
- [ ] Confirmation page carries all five required fields and **nothing else** (BGH I ZR 200/25)
- [ ] Acknowledgement on a durable medium with date and time

## Warranty

- [ ] "Gewährleistung" and "Garantie" kept apart
- [ ] No shortening below two years for new goods against a consumer (§ 476 Abs 2 BGB)
- [ ] § 327f BGB update obligation addressed with a concrete period
- [ ] Guarantee statement, where given, complete under § 479 Abs 1 BGB and supplied on a durable medium

## Marketing

- [ ] Newsletter consent separate, unticked, purpose concrete
- [ ] Double opt-in active, confirmation e-mail advertising-free
- [ ] Consent log with timestamp, IP and text version
- [ ] Unsubscribe link in every mailing, one click
- [ ] Impressum data in every mailing
- [ ] Soft opt-in only where all four conditions of § 7 Abs 3 UWG are documented
- [ ] Sponsored content labelled "Werbung" or "Anzeige" in German, visible without expanding
- [ ] Review verification practice disclosed (§ 5b Abs 3 UWG)

## Accessibility

- [ ] BFSG scope decided, Kleinstunternehmen status documented if claimed
- [ ] § 14 Abs 1 Nr 2 BFSG information published with all four Anlage 3 Nr 1 items
- [ ] Keyboard pass through the main flows succeeded, focus visible
- [ ] Contrasts measured
- [ ] Form labels associated, errors reported as text
- [ ] Screen reader pass through the order or sign-up flow

## Products

- [ ] LUCID registration before the first shipment; packaging duties re-checked against the VerpackDG from 12.08.2026
- [ ] stiftung ear registration where electricals are sold; § 17 and § 18 ElektroG duties addressed
- [ ] BattDG registration and take-back where batteries are shipped, including batteries inside devices
- [ ] Textile fibre composition in the product description and on the label

## Dispute resolution and platform

- [ ] No ODR link and no mention of the EU platform, project-wide
- [ ] § 36 VSBG statement present in the correct variant
- [ ] § 37 VSBG Textform notice built into the complaints process
- [ ] DSA classification documented; Art 11, 12, 16, 17 duties implemented where hosting third-party content
- [ ] No NetzDG reference

## Cross-cutting

- [ ] No German-obsolete norms: TMG, TTDSG, RStV, NetzDG, BDSG-alt
- [ ] No Austrian norms: ECG, MedienG, FAGG, KSchG, UGB, Firmenbuch, GISA, UID ATU
- [ ] No US assumptions: opt-out cookies, arbitration clause, class-action waiver, "Terms of Service" as a legal category
- [ ] Image rights and licences documented (UrhG)
- [ ] Third-party marks and logos used only with authorisation
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
- [ ] Draft marker still present wherever legal sign-off has not been given

## Output format

Report findings as a table, most severe first:

| Severity | Location | Norm | Finding | Fix |
|---|---|---|---|---|
| kritisch / hoch / mittel | file:line or URL | § | what is missing or wrong | concrete step |

**Kritisch** means: Abmahnrisiko, Bußgeld, or unenforceability of the contract. That includes a missing Impressum, tracking before consent, a wrongly labelled order button, a missing Widerrufsbelehrung, a missing § 312k BGB cancellation button, and a missing § 356a BGB withdrawal function.
