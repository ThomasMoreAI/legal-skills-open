---
name: aussenpruefung-betriebspruefung-borghei
title: /steuerrecht:aussenpruefung-betriebspruefung
description: Begleitung einer Außenprüfung (Betriebsprüfung) durch die Finanzbehörde nach §§ 193 ff. AO. Anordnung und Prüfungsumfang, Mitwirkungspflichten §§ 90, 200 AO, Schlussbesprechung § 201 AO, Schätzungen § 162 AO, Rechtsbehelfe gegen Prüfungshandlungen, GoBD-konforme Aufzeichnungen. Use when ein Mandant eine Prüfungsanordnung erhalten hat oder die Schlussbesprechung vorbereitet.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/steuerrecht/skills/aussenpruefung-betriebspruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: tax
language: de
---

# /steuerrecht:aussenpruefung-betriebspruefung

## Zweck

Die Außenprüfung entscheidet regelmäßig über sechs- bis siebenstellige Mehrergebnisse. Fehler in Mitwirkung und Verfahrensführung können zu Schätzungen führen, deren Bekämpfung im Einspruchsverfahren / Finanzgericht aufwendig ist. Dieser Skill begleitet von Prüfungsanordnung bis Schlussbesprechung.

## Eingaben

- Prüfungsanordnung (Datum, prüfender Beamter, Zeitraum, Steuerarten)
- Größenklasse (Großbetrieb / Mittelbetrieb / Kleinbetrieb / Anschluss prüfung)
- Bilanzunterlagen und Buchführung (DATEV, GoBD-Konformität)
- Vorgeschichte (frühere Prüfungen, offene Punkte)
- Branche und Risikoschwerpunkte

## Ablauf

### 1. Prüfungsanordnung ([§ 196 AO](https://www.gesetze-im-internet.de/ao_1977/__196.html))

- Schriftlicher Verwaltungsakt
- Inhalt: Prüfungszeitraum, Steuerarten, prüfender Beamter, voraussichtlicher Beginn
- **Rechtsbehelf**: Einspruch zulässig (§ 347 AO), Aussetzung der Vollziehung § 361 AO
- Inhaltliche Beschränkung des Prüfungsumfangs nur bei missbräuchlicher Erweiterung erfolgversprechend

### 2. Mitwirkungspflichten

#### § 90 AO (Allgemein)

- Aufklärung des Sachverhalts
- Bezeichnung der Beweismittel
- Erweiterte Mitwirkung bei Auslandssachverhalten (§ 90 Abs. 2, 3 AO)

#### § 200 AO (Außenprüfung)

- Vorlage von Aufzeichnungen, Büchern, Belegen
- Datenzugriff (Z1/Z2/Z3): unmittelbar / mittelbar / Datenträger
- GoBD-Konformität (Grundsätze zur ordnungsmäßigen Führung und Aufbewahrung von Büchern, Aufzeichnungen und Unterlagen)

### 3. Datenzugriff (GDPdU/GoBD)

**Z1** — Direkter Zugriff auf das DV-System des Steuerpflichtigen.
**Z2** — Mittelbarer Zugriff mit Datenauswertung durch den Steuerpflichtigen nach Vorgaben.
**Z3** — Übergabe maschinell auswertbarer Daten.

Z1 ist bei Außenprüfungen die häufigste Wahl. Auswahlrecht nicht direkt beim Prüfer.

### 4. Schätzungen ([§ 162 AO](https://www.gesetze-im-internet.de/ao_1977/__162.html))

Schätzung ist zulässig bei:

- Mitwirkungsverweigerung
- Nichtaufklärbarem Sachverhalt
- Mangelhafter Buchführung (§ 158 AO Umkehrschluss)
- Verprobung mit Branchen-Richtsätzen

Verteidigung: GoBD-Konformität, Plausibilität, Alternativrechnungen.

### 5. Schlussbesprechung ([§ 201 AO](https://www.gesetze-im-internet.de/ao_1977/__201.html))

- Pflicht der Finanzbehörde, vor Erlass des Bescheids
- Erörterung der strittigen Punkte
- Vorlage des Prüfungsberichts-Entwurfs
- Möglichkeit zur Stellungnahme

Strategisch entscheidend: in der Schlussbesprechung lassen sich Konzessionen aushandeln, die nach Erlass des Bescheids nur schwer zurückzuführen sind.

### 6. Prüfungsbericht (§ 202 AO)

- Schriftlicher Bericht über Feststellungen
- Bekanntgabe an Steuerpflichtigen
- Grundlage für die geänderten Steuerbescheide

### 7. Rechtsbehelf gegen Bescheide nach Prüfung

- **Einspruch** § 347 AO (1 Monat ab Bekanntgabe)
- **Aussetzung der Vollziehung** § 361 AO (Voraussetzung: ernstliche Zweifel oder unbillige Härte)
- **Klage** beim Finanzgericht nach Einspruchsentscheidung (§ 40 FGO)

### 8. Sonderprobleme

#### a) Tax Compliance / IKS

Implementierung interner Kontrollsysteme nach AEAO § 153 reduziert Hinterziehungsverdacht.

#### b) Strafrechtliches Risiko § 371 AO

Bei Hinweis auf Steuerhinterziehung — selbstanzeigerelevante Sachverhalte mit Strafverteidiger absprechen.

## Quellen

### Statute

- [§§ 193–203 AO](https://www.gesetze-im-internet.de/ao_1977/__193.html) (Außenprüfung)
- [§ 90 AO](https://www.gesetze-im-internet.de/ao_1977/__90.html), [§ 162 AO](https://www.gesetze-im-internet.de/ao_1977/__162.html), [§ 158 AO](https://www.gesetze-im-internet.de/ao_1977/__158.html)
- [§§ 347 ff. AO](https://www.gesetze-im-internet.de/ao_1977/__347.html), [§ 361 AO](https://www.gesetze-im-internet.de/ao_1977/__361.html)
- [§ 153 AO](https://www.gesetze-im-internet.de/ao_1977/__153.html), [§ 371 AO](https://www.gesetze-im-internet.de/ao_1977/__371.html)
- [FGO](https://www.gesetze-im-internet.de/fgo/)

### Verwaltungsanweisungen

- AEAO (Anwendungserlass zur Abgabenordnung)
- BMF, GoBD (Stand 28.11.2019)
- Allgemeine Verwaltungsvorschrift für die Betriebsprüfung (BpO)

### Kommentare

- Drüen, in: Tipke / Kruse, AO/FGO, 178. Lfg.
- Klein, AO, 16. Aufl. 2024
- Pahlke / Koenig, AO, 4. Aufl. 2023

### Rechtsprechung

- BFH, Urt. v. 27.09.2017 – XI R 18/16, BStBl. II 2018, 668 `[unverifiziert – prüfen]`
- BFH, Urt. v. 13.03.2018 – IX R 16/17, BStBl. II 2019, 169 `[unverifiziert – prüfen]`

## Ausgabeformat

```
AUSSENPRÜFUNG — Begleitung — <Mandant> — <Datum>

I.    Prüfungsanordnung
      Datum:                          <…>
      Zeitraum:                       <Veranlagungsjahre>
      Steuerarten:                    <ESt / KSt / GewSt / USt>
      Beamter:                        <…>
      Einspruch:                      [erwogen / nicht]

II.   Vorbereitung
      GoBD-Konformität:               [✓ / ⚠️]
      Datenzugriff (Z1/Z2/Z3):        [Z1 angekündigt — Vorbereitung]
      Risikoschwerpunkte:             <…>

III.  Mitwirkung
      Pflichten § 90, § 200:          [erfüllt / Lücken: …]
      Sprachregelung Prüfer:          <…>
      Dokumentation Anfragen:         <…>

IV.   Strittige Feststellungen
      <…>

V.    Schlussbesprechung-Strategie
      Verhandlungsspielraum:          <…>
      Kompromisspunkte:               <…>

VI.   Risikoeinschätzung Mehrergebnis: <EUR Bereich>
VII.  Strafrechtliches Risiko § 371:  [keiner / niedrig / mittel / hoch]

Folgemaßnahmen:                       <Einspruch / AdV / Klage>
```

## Risiken / typische Fehler

- **Datenzugriff Z1 vorbehaltlos eingeräumt** — bei sensiblen Daten Z3 anbieten.
- **Mitwirkungsverweigerung als Strategie** — provoziert Schätzungen, schwer zu beklagen.
- **Schlussbesprechung als Formalität** — wichtigster Verhandlungstermin.
- **GoBD-Mängel unterschätzt** — kann Buchführungs-Verwerfung nach § 158 AO auslösen.
- **§ 153 AO-Anzeige bei Erkenntnissen vergessen** — kann Steuerhinterziehung verhindern.
- **Selbstanzeige § 371 AO ohne Strafverteidiger-Abstimmung** — Tatbestandsverlust riskiert.
- **Fristen Einspruch und AdV verwechselt** — Einspruch hat keine aufschiebende Wirkung von selbst.
