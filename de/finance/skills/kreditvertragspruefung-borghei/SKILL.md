---
name: kreditvertragspruefung-borghei
title: /bankrecht:kreditvertragspruefung
description: Prüfung von Verbraucherdarlehensverträgen nach §§ 491 ff. BGB. Informationspflichten und Pflichtangaben Art. 247 EGBGB, Widerrufsrecht §§ 495, 355 ff. BGB, vorzeitige Rückzahlung § 502 BGB mit Vorfälligkeitsentschädigung, Kopplungsverbote, AGB-Kontrolle. Use when ein Verbraucherdarlehensvertrag bewertet oder eine Forderung der Bank aus solchem Vertrag geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/bankrecht/skills/kreditvertragspruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: finance
language: de
---

# /bankrecht:kreditvertragspruefung

## Zweck

Verbraucherdarlehen sind hochgradig regulierungsdicht. Formfehler bei Pflichtangaben können das Widerrufsrecht „ewig" laufen lassen (vor BGH/EuGH-Konkretisierungen) und damit den Darlehensvertrag rückabwickeln. Dieser Skill prüft die Wirksamkeit und identifiziert Streichungs-/Verteidigungsoptionen.

## Eingaben

- Vertragstyp (Verbraucherdarlehen, Unternehmerkredit, Hypothekendarlehen, Anschlussfinanzierung)
- Vertragsschluss-Datum (für Anwendbarkeit der jeweiligen Fassung von §§ 491 ff. BGB)
- Darlehensbetrag, Laufzeit, Sollzinssatz, effektiver Jahreszins
- Verbundene Verträge (z. B. mit gekauftem Gut, Restschuldversicherung)
- Widerrufsbelehrung im Vertrag

## Ablauf

### 1. Anwendungsbereich

[§ 491 BGB](https://www.gesetze-im-internet.de/bgb/__491.html): Verbraucherdarlehen, wenn:

- Darlehensgeber als **Unternehmer** (§ 14 BGB) handelt
- Darlehensnehmer **Verbraucher** (§ 13 BGB) ist
- Darlehensbetrag > 200 EUR (§ 491 Abs. 2 Nr. 1 BGB)

**Sonderkategorien:**

- **Hypothekendarlehen** § 491 Abs. 3 BGB: erhöhte Pflichtangaben
- **Immobiliar-Verbraucherdarlehen** §§ 491b ff. BGB: Wohnimmobilienkredit-Richtlinie-Umsetzung

### 2. Pflichtangaben Art. 247 EGBGB

Vorvertragliche Standardinformationen + vertragliche Pflichtangaben. Auswahl:

- Name und Anschrift der Vertragsparteien
- Vertragstyp
- Nettodarlehensbetrag
- Laufzeit
- Sollzinssatz und Bedingungen
- Effektiver Jahreszins
- Auszahlungs- und Tilgungsplan
- **Widerrufsbelehrung** (siehe Ziff. 3)
- Verzugszinsen
- Vorzeitige Rückzahlung mit Entschädigung
- Außerordentliche Kündigungsrechte
- Vermittler / Verbundene Verträge

Fehlerhafte / fehlende Pflichtangaben → Widerrufsfrist beginnt nicht zu laufen (§ 356b BGB für klassische Verbraucherdarlehen; bei Immobiliardarlehen Begrenzung durch § 356b Abs. 2 S. 4 BGB auf 1 Jahr und 14 Tage seit Vertragsschluss).

### 3. Widerrufsrecht (§§ 495, 355 ff. BGB)

- **Frist:** 14 Tage
- **Beginn:** mit Erhalt der ordnungsgemäßen Widerrufsbelehrung und Vertragsurkunde (§ 356b BGB)
- **Rechtsfolge:** Rückabwicklung als gesetzliches Rückgewährschuldverhältnis
- **Schweigeklauseln:** bei Immobiliardarlehen Höchstgrenze 1 Jahr und 14 Tage

### 4. Vorzeitige Rückzahlung ([§ 502 BGB](https://www.gesetze-im-internet.de/bgb/__502.html))

- Recht zur vorzeitigen Rückzahlung
- Anbieter kann **angemessene** Vorfälligkeitsentschädigung verlangen
- Berechnung: Differenz zwischen ursprünglichem Zinsanspruch und Wiederanlagezins (vermindert um Verwaltungskosten und Risikokosten)
- **Höchstgrenze** § 502 Abs. 3 BGB
- Bei fehlender Angabe der Berechnung im Vertrag (§ 502 Abs. 2 BGB): kein Vorfälligkeitsentschädigungsanspruch

### 5. Restschuldversicherung / Kopplung

- Kopplungsverbote § 492a BGB
- Bei Verbundene Verträge § 358 BGB: Widerruf des einen erstreckt sich auf den anderen

### 6. AGB-Inhaltskontrolle

§§ 305 ff. BGB greifen ergänzend. Häufig problematisch:

- Bearbeitungsgebühren in Allgemeinkredit-AGB → unwirksam (BGH, Urt. v. 13.05.2014 – XI ZR 405/12, NJW 2014, 2420 `[unverifiziert – prüfen]`)
- „Anpassungsklauseln" der Bank ohne Widerrufsrecht
- Verzugszins-Pauschalierung über § 288 BGB hinaus

## Quellen

### Statute

- [§§ 491–505d BGB](https://www.gesetze-im-internet.de/bgb/__491.html)
- [§ 355 BGB](https://www.gesetze-im-internet.de/bgb/__355.html), [§ 356b BGB](https://www.gesetze-im-internet.de/bgb/__356b.html), [§ 502 BGB](https://www.gesetze-im-internet.de/bgb/__502.html)
- [Art. 247 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_247.html)
- [Richtlinie 2008/48/EG (Verbraucherkredit)](https://eur-lex.europa.eu/eli/dir/2008/48/oj)
- [Richtlinie 2014/17/EU (Wohnimmobilienkredit)](https://eur-lex.europa.eu/eli/dir/2014/17/oj)

### Kommentare

- Müller-Christmann, in: BeckOGK BGB, § 491 Rn. 1 ff.
- Pamp, in: MüKoBGB, 9. Aufl. 2023, § 491 Rn. 1 ff.

### Rechtsprechung

- EuGH, Urt. v. 26.03.2020 – C-66/19, NJW 2020, 1657 (Kausalkette der Widerrufsbelehrung) `[unverifiziert – prüfen]`
- BGH, Urt. v. 27.02.2018 – XI ZR 224/17, NJW 2018, 1747 `[unverifiziert – prüfen]`
- BGH, Urt. v. 13.05.2014 – XI ZR 405/12, NJW 2014, 2420 (Bearbeitungsgebühr) `[unverifiziert – prüfen]`

## Ausgabeformat

```
VERBRAUCHERDARLEHENSVERTRAG-PRÜFUNG — <Mandat> — <Datum>

I.    Anwendungsbereich              [Verbraucherdarlehen / Immobiliardarlehen / Unternehmerkredit]
II.   Pflichtangaben (Art. 247 EGBGB)
      Vollständigkeit:                [✓ / ⚠️ Liste fehlender Angaben]
III.  Widerrufsrecht (§§ 495, 356b)
      Belehrung korrekt:              [✓ / 🔴 fehlerhaft]
      Frist:                          [abgelaufen / läuft noch / „ewig" bei Fehler]
IV.   Vorzeitige Rückzahlung § 502
      Berechnung im Vertrag dargestellt:  [✓ / 🔴]
      Vorfälligkeitsentschädigung:    [angemessen / überhöht]
V.    AGB-Kontrolle (§§ 305 ff.)
      Bearbeitungsgebühren:           [keine / 🔴 unwirksam, Rückforderung]
      Anpassungsklauseln:             [zulässig / 🔴]
VI.   Verbundene Verträge / RSV       [N/A / vorhanden]

Empfehlung: <…>
Verteidigungslinie / Strategie:       <…>
```

## Risiken / typische Fehler

- **Widerrufsbelehrung als Standard ohne Prüfung übernommen** — Fehler in Pflichtangaben lässt Frist nicht beginnen.
- **Bearbeitungsgebühren akzeptiert** — sind nach BGH-Rspr. unwirksam und rückforderbar.
- **§ 502 BGB-Berechnung übersehen** — fehlt sie im Vertrag, entfällt der Vorfälligkeitsanspruch.
- **Kopplungsverbote ignoriert** — Restschuldversicherung als Pflicht ist § 492a BGB-widrig.
- **Verjährungsbeginn falsch berechnet** — bei Widerruf Rückgewährschuldverhältnis hat eigene Verjährung.
- **EU-Recht außer Acht** — die EuGH-Rechtsprechung schärft die Auslegung kontinuierlich.
