---
name: legal-at-clemensjl
title: Rechtstexte Österreich
description: Use when writing, reviewing, or fixing legally required texts for an Austrian website, webshop, app, or newsletter — Impressum, Offenlegung, Datenschutzerklärung, Cookie-Banner, AGB, Rücktrittsbelehrung, Gewährleistung, Barrierefreiheitserklärung — or when asked whether an Austrian online presence is rechtskonform. Also use when a German or US legal template is about to be reused for Austria, when personal data processing starts, or before a site goes live.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/legal-at
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: data-protection
language: de
sources:
- title: Agb Fernabsatz
  path: references/agb-fernabsatz.md
- title: Barrierefreiheit
  path: references/barrierefreiheit.md
- title: Checkliste
  path: references/checkliste.md
- title: Cookies
  path: references/cookies.md
- title: Datenschutz
  path: references/datenschutz.md
- title: Dsgvo Intern
  path: references/dsgvo-intern.md
- title: Gewaehrleistung
  path: references/gewaehrleistung.md
- title: Impressum
  path: references/impressum.md
- title: Marketing
  path: references/marketing.md
- title: Plattform Dsa
  path: references/plattform-dsa.md
- title: Ruecktritt
  path: references/ruecktritt.md
- title: Sachverhalt
  path: references/sachverhalt.md
- title: Streitbeilegung
  path: references/streitbeilegung.md
---

# Rechtstexte Österreich

Pflichttexte für österreichische Websites, Webshops, Apps und Newsletter. Grundlage sind DSGVO, DSG, ECG, MedienG, UGB, GewO, FAGG, KSchG, VGG, TKG 2021, UWG, PrAG, BaFG und DSA.

**Kernprinzip:** Österreich ist nicht Deutschland. Die Impressumspflicht folgt aus **drei** Gesetzen parallel (ECG, MedienG, UGB/GewO), nicht aus einem § 5 TMG. Wer ein deutsches Muster kopiert, produziert ein formell unvollständiges Impressum und verliert dazu die österreichischen Besonderheiten — Offenlegung nach § 25 MedienG, Gewerbewortlaut, Aufsichtsbehörde, Einwilligungsalter 14 statt 16.

## Kein Rechtsrat

Dieser Skill erzeugt Entwürfe und Prüfergebnisse, keine Rechtsberatung. Vor dem Livegang gilt:

- Bei Webshop, Abo, Zahlungsabwicklung, Kinderdaten, Gesundheitsdaten oder Plattformbetrieb: **anwaltliche Freigabe einholen.**
- Kostenlose Erstberatung: WKO-Rechtsservice (für Mitglieder), Internet Ombudsstelle (ombudsstelle.at), Datenschutzbehörde (dsb.gv.at) für Auslegungsfragen.
- Jeder erzeugte Text bekommt einen sichtbaren Marker `<!-- ENTWURF – juristisch nicht freigegeben -->` als HTML-Kommentar, bis Clemens die Freigabe bestätigt. Marker nie stillschweigend entfernen.

Diesen Abschnitt im Output nie weglassen und nie relativieren.

## Ablauf

1. **Sachverhalt erheben, bevor irgendein Text entsteht.** Ohne die Antworten sind alle Texte Raten. Fragen in `references/sachverhalt.md`.
2. **Pflicht-Matrix bestimmen** (unten): welche Texte braucht genau dieses Projekt.
3. **Pro Pflichttext die zugehörige Referenzdatei lesen**, dann Entwurf schreiben. Nie aus dem Gedächtnis — die Paragrafen sind zu spezifisch.
4. **Checkliste** `references/checkliste.md` durchgehen, Befunde mit Paragraf benennen.
5. Freigabe-Hinweis ausgeben, Entwurfs-Marker stehen lassen.

**Form des Outputs.** Der Output besteht aus genau vier Teilen, in dieser Reihenfolge:

1. der Rechtstext oder Befund selbst, mit Entwurfs-Marker
2. die Liste der `[[FEHLT: …]]`-Punkte, die Clemens beisteuern muss
3. angrenzende Pflichten, die im selben Projekt offen sind, in einem Satz je Pflicht
4. der Freigabe-Hinweis

Die Norm steht jeweils direkt bei der Aussage, zu der sie gehört. Dateinamen und Pfade der Referenzdateien gehören in keinen dieser vier Teile — sie sind Arbeitsmaterial, nicht Teil der Lieferung.

## Pflicht-Matrix

| Situation | Pflichttexte | Referenz |
|---|---|---|
| Jede Website mit wirtschaftlichem Zweck | Impressum (ECG § 5), Offenlegung (MedienG §§ 24, 25) | `impressum.md` |
| Website verarbeitet personenbezogene Daten (auch nur Server-Logs, Kontaktformular) | Datenschutzerklärung (DSGVO Art 13/14) | `datenschutz.md` |
| Nicht technisch notwendige Cookies, Analytics, Pixel, Embeds, Fonts vom Fremdserver | Consent-Banner + Cookie-Abschnitt (TKG 2021 § 165 Abs 3) | `cookies.md` |
| Verkauf an Verbraucher online | AGB, vorvertragliche Infos (FAGG § 4), korrekter Bestellbutton | `agb-fernabsatz.md` |
| Verkauf an Verbraucher online | Rücktrittsbelehrung + Muster-Rücktrittsformular (FAGG §§ 11–18) | `ruecktritt.md` |
| Verkauf von Waren oder digitalen Leistungen | Gewährleistungshinweis, ggf. Garantieerklärung (VGG, ABGB) | `gewaehrleistung.md` |
| Newsletter, E-Mail-Werbung, SMS-Werbung | Double-Opt-In, Einwilligungstext, Abmeldung, ECG-Liste | `marketing.md` |
| B2C-Onlineangebot, kein Kleinstunternehmen | Barrierefreiheitserklärung (BaFG, WCAG 2.1 AA) | `barrierefreiheit.md` |
| Hosting, Forum, Kommentare, Marktplatz, UGC | DSA-Kontaktstelle, Melde-/Abhilfeverfahren, AGB-Transparenz | `plattform-dsa.md` |
| Verbrauchergeschäft | Hinweis auf Streitschlichtungsstelle | `streitbeilegung.md` |
| Personenbezogene Daten in irgendeiner Form | Verarbeitungsverzeichnis, AVV, TOM, Breach-Prozess (intern, nicht auf der Seite) | `dsgvo-intern.md` |
| Kinder unter 14 als Zielgruppe | Elterneinwilligung nach § 4 Abs 4 DSG | `datenschutz.md` |

## Harte Regeln

- **ODR-Plattform ist tot.** Die EU-Streitbeilegungsplattform wurde durch VO (EU) 2024/3228 abgeschaltet, Betrieb endete 20.07.2025. Ein Link darauf ist heute ein toter Link und potenziell irreführende Geschäftspraxis. Findet sich in einem Bestandstext ein ODR-Hinweis, wird er ersatzlos entfernt und stattdessen auf die nationale Schlichtungsstelle verwiesen. Nie neu einbauen, egal was ein Muster sagt.
- **Einwilligungsalter ist 14, nicht 16.** § 4 Abs 4 DSG senkt die Altersgrenze aus Art 8 DSGVO für Dienste der Informationsgesellschaft auf das vollendete 14. Lebensjahr. Darunter braucht es die Einwilligung des gesetzlichen Vertreters.
- **Kein Tracking vor Einwilligung.** Kein Analytics-, Pixel-, Map-, Video- oder Font-Request darf feuern, bevor der Nutzer aktiv zugestimmt hat. "Ablehnen" muss auf der ersten Banner-Ebene stehen, gleich prominent wie "Akzeptieren". Vorangekreuzte Boxen und reine "OK"-Banner sind unwirksam.
- **Zwei verschiedene Buttons, zwei verschiedene Paragrafen.** Der **Bestellbutton** richtet sich nach **§ 8 FAGG**, die **Vertragsbestätigung** nach **§ 7 Abs 3 FAGG**, der **Widerrufsbutton** nach **§ 13a FAGG**. Diese drei werden regelmäßig verwechselt; jede Aussage dazu bekommt den richtigen Paragrafen oder gar keinen.
- **Bestellbutton wörtlich beschriften.** § 8 FAGG verlangt eine Beschriftung, die die Zahlungspflicht ausdrückt — "zahlungspflichtig bestellen" oder gleichwertig eindeutig. "Absenden", "Weiter", "Jetzt starten" bindet den Verbraucher nicht.
- **Keine deutschen Paragrafen.** Taucht in einem Text § 5 TMG, § 55 RStV, BDSG, DSGVO-Umsetzung "BDSG-neu", "Widerrufsrecht" statt "Rücktrittsrecht" oder "Amtsgericht" auf, ist der Text aus einer deutschen Vorlage entstanden und muss vollständig neu geschrieben werden, nicht gepatcht.
- **Keine erfundenen Angaben.** Firmenbuchnummer, UID, Gewerbewortlaut, Kammerzugehörigkeit, Aufsichtsbehörde und Anschrift nie plausibel ausfüllen. Fehlt ein Wert, kommt `[[FEHLT: Firmenbuchnummer]]` in den Text und in die Rückmeldung an Clemens.
- **Vollständige Anschrift, keine Postfächer.** § 5 ECG verlangt die geografische Anschrift der Niederlassung. Bei Einzelunternehmen ohne Geschäftslokal ist das die Wohnadresse — wenn Clemens das nicht will, ist das ein Geschäftsentscheid (Coworking-Adresse, Firmensitz), keine Formulierungsfrage. Sofort ansprechen statt umschiffen.

## Deutsche Rechtsirrtümer (False Friends)

Deutsche Pflichten wirken plausibel und werden unter Zeitdruck erfunden. Keine davon existiert in Österreich in dieser Form. Wird eine behauptet, ist sie zu streichen und durch die österreichische Entsprechung zu ersetzen — falls es eine gibt.

| Behauptung aus dem deutschen Recht | Lage in Österreich |
|---|---|
| Kündigungsbutton nach § 312k BGB für Abos | Existiert nicht. Es gibt seit 2026 den **Widerrufsbutton nach § 13a FAGG**, der etwas anderes regelt: die Ausübung des Rücktrittsrechts, nicht die Kündigung eines Dauerschuldverhältnisses. Nicht verwechseln. |
| § 5 TMG Impressum | § 5 ECG, dazu §§ 24, 25 MedienG und § 14 UGB parallel |
| § 55 RStV Verantwortlicher für den Inhalt | Kein Pendant; stattdessen Offenlegung nach § 25 MedienG |
| Haftungsprivileg § 7 Abs 1 TMG | §§ 13 bis 19 ECG; für eigene Inhalte gibt es kein Privileg |
| Widerrufsrecht, Widerrufsbelehrung im Fließtext | Rücktrittsrecht, Rücktrittsbelehrung. Nur das Muster-Widerrufsformular heißt so, weil der Anhang aus der Richtlinie stammt. |
| BDSG, § 38 BDSG Datenschutzbeauftragter ab 20 Personen | DSG; keine Schwelle nach Beschäftigtenzahl |
| Einwilligungsalter 16 | 14 nach § 4 Abs 4 DSG |
| Amtsgericht, Landgericht, Handelsregister, HRB | Bezirksgericht, Landesgericht, Firmenbuch, FN |
| USt-IdNr. nach § 27a UStG | UID-Nummer, Format ATU |
| Link auf die EU-ODR-Plattform | Abgeschaltet, siehe unten |

Kommt eine Pflicht in den Sinn, die sich nicht auf eine konkrete österreichische Norm zurückführen lässt, wird sie nicht behauptet, sondern als offene Frage gemeldet.

## Häufige Fehler

| Fehler | Warum falsch |
|---|---|
| Impressum nur nach ECG | MedienG §§ 24, 25 gelten parallel; Offenlegung fehlt |
| "Diese Seite verwendet Cookies. OK" | Keine Einwilligung im Sinn des § 165 Abs 3 TKG 2021 |
| Google Fonts / Maps / YouTube ohne Consent | Drittlandübermittlung + Endgerätezugriff vor Einwilligung |
| Datenschutzerklärung ohne Rechtsgrundlage je Zweck | Art 13 Abs 1 lit c DSGVO verlangt die Grundlage pro Verarbeitung |
| "14 Tage Widerrufsrecht" | Falscher Begriff; in Österreich Rücktrittsrecht nach FAGG |
| Rücktrittsbelehrung ohne Muster-Formular | Anhang I Teil B FAGG ist Pflichtbestandteil |
| Gewährleistung auf 1 Jahr verkürzt (B2C) | VGG lässt das bei Neuware nicht zu |
| Newsletter-Anmeldung ohne Double-Opt-In | Beweislast für Einwilligung liegt beim Absender |
| Barrierefreiheit ignoriert | BaFG gilt seit 28.06.2025 für B2C-Onlineangebote |
| Bilder ohne Lizenznachweis | UrhG; Nachweis gehört ins Projekt, nicht in den Rechtstext |

## Referenzdateien

Jede enthält Paragrafenstand, Pflichtinhalte, Textvorlage und Prüfpunkte.

- `references/sachverhalt.md` — Fragenkatalog vor dem ersten Text
- `references/impressum.md` — ECG § 5, MedienG §§ 24/25, UGB § 14, GewO § 63, DSA-Kontaktstelle
- `references/datenschutz.md` — Art 13/14 DSGVO, DSG-Abweichungen, Kinderdaten, Auftragsverarbeiter, Drittland
- `references/dsgvo-intern.md` — Verarbeitungsverzeichnis, AVV, TOM, Breach-Meldung, DSFA, Datenschutzbeauftragter
- `references/cookies.md` — TKG 2021 § 165 Abs 3, Banner-Anforderungen, Kategorisierung, Nachweis
- `references/agb-fernabsatz.md` — FAGG-Informationspflichten, Bestellprozess, Preisauszeichnung
- `references/ruecktritt.md` — Fristen, Ausnahmen, Rechtsfolgen, Muster-Rücktrittsformular
- `references/gewaehrleistung.md` — VGG, Aktualisierungspflicht, Garantie, Abgrenzung
- `references/marketing.md` — TKG 2021 § 174, UWG, Influencer-Kennzeichnung, Bewertungen, Gewinnspiele
- `references/barrierefreiheit.md` — BaFG, Anwendungsbereich, Kleinstunternehmen, Erklärung
- `references/plattform-dsa.md` — DSA-Pflichten für UGC, Foren, Marktplätze, Hosting
- `references/streitbeilegung.md` — AStG, zuständige Stellen, ODR-Abschaltung
- `references/checkliste.md` — Pre-Launch-Prüfliste mit Paragrafenzuordnung
