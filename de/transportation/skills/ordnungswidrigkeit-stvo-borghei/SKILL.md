---
name: ordnungswidrigkeit-stvo-borghei
title: /verkehrsrecht:ordnungswidrigkeit-stvo
description: Prüfung eines Bußgeldbescheids wegen Verstoßes gegen die StVO – formelle Anforderungen § 66 OWiG, Einspruchsfrist 2 Wochen § 67 OWiG, standardisierte Messverfahren mit Akteneinsicht in Rohmessdaten, Fahrverbot § 25 StVG, Absehen wegen besonderer Härte § 4 IV BKatV, Verfolgungsverjährung § 26 III StVG / § 31 OWiG. Use when ein Mandant einen Bußgeldbescheid (Geschwindigkeit, Abstand, Rotlicht, Handy) erhalten hat und Einspruch geprüft werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verkehrsrecht/skills/ordnungswidrigkeit-stvo
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: transportation
language: de
---

# /verkehrsrecht:ordnungswidrigkeit-stvo

## Zweck

Der Skill prüft Bußgeldbescheide wegen Ordnungswidrigkeiten nach StVO/StVG, entwickelt Verteidigungsansätze (Bestreiten der Fahrereigenschaft, Messfehler, Verfahrensfehler, Verfolgungsverjährung, Absehen vom Fahrverbot) und entwirft die Einspruchsbegründung samt Beweis- und Akteneinsichtsanträgen. Er klärt die Schnittstelle zum Verkehrsstrafrecht (§§ 142, 315c, 316 StGB) und das Doppelverfolgungsverbot § 21 OWiG.

## Eingaben

- Bußgeldbescheid (Tatzeit, Tatort, Tatvorwurf, BKatV-Anlagen-Position, Bußgeld, FAER-Punkte, ggf. Fahrverbot)
- Messverfahren / Beweismittel (Lasermessgerät, PoliScan, ES 3.0, Lichtschrankenmessung, Polizeibeobachtung)
- Bisheriger Verfahrensgang (Anhörungsbogen, Zeugenfragebogen, Zustellungsdatum)
- Position des Mandanten (Fahrer- oder Halterhaftung; berufliche Angewiesenheit auf Fahrerlaubnis)
- Vor-OWi-Eintragungen (FAER-Auszug)

## Sub-Agent-Architektur

Researcher liefert StVO, BKatV, OWiG, OLG-Bußgeldsenat-Rspr. und BVerfG-Rspr. zu standardisierten Messverfahren sowie Burhoff- und Krenberger/Krumm-Belegstellen. Drafter entwirft die Einspruchsbegründung in Urteilsstil mit Beweis- und Akteneinsichtsanträgen. Reviewer prüft Einspruchsfrist § 67 OWiG, Verfolgungsverjährung § 26 III StVG, Doppelverfolgungsverbot § 21 OWiG.

## Ablauf

### 1. Formelle Prüfung des Bußgeldbescheids

Anforderungen § 66 OWiG (Pflichtangaben):

- Personalien des Betroffenen
- **Tatzeit und -ort** (Datum, Uhrzeit, Streckenkilometer/Adresse)
- **Tatvorwurf** mit Beweismitteln (Messgerät, Eichdatum, Toleranzabzug)
- **anzuwendende Vorschriften** (StVO-Norm + BKatV-Anlagen-Position)
- **Geldbuße**, Nebenfolgen (Fahrverbot § 25 StVG)
- Belehrung über Einspruch und Frist

Fehlerhafte Bescheide können konkretisierungsbedürftig oder — bei groben Mängeln — unwirksam sein (vgl. § 66 OWiG; OLG-Rspr., `[unverifiziert – prüfen]`).

### 2. Einspruchsfrist § 67 OWiG

**2 Wochen ab Zustellung** des Bußgeldbescheids (§ 67 Abs. 1 OWiG). Einspruch ist schriftlich oder zu Protokoll bei der Bußgeldbehörde einzulegen. Wiedereinsetzung in den vorigen Stand § 52 OWiG iVm §§ 44, 45 StPO.

### 3. Verfolgungsverjährung § 26 Abs. 3 StVG / § 31 OWiG

- **3 Monate** ab Tatzeit bis zum Erlass des Bußgeldbescheids (§ 26 Abs. 3 StVG).
- Nach Erlass des Bescheids: **6 Monate** Verjährung.
- **Unterbrechungstatbestände** § 33 OWiG (insb. Anhörung des Betroffenen, Erlass des Bescheids) zu prüfen.

### 4. Standardisierte Messverfahren

Anerkannte standardisierte Messverfahren (z. B. ES 3.0, PoliScan Speed, ESO, Riegl FG21-P) genießen Beweiserleichterung (BGH, Beschl. v. 19.08.1993 – 4 StR 627/92, BGHSt 39, 291 `[unverifiziert – prüfen]`). Voraussetzungen:

- gültige Eichung (Eichschein)
- Bedienung nach Bedienungsanleitung
- Toleranzabzug (idR 3 km/h bis 100 km/h, sonst 3%; je Gerät unterschiedlich)

**Akteneinsicht in Rohmessdaten** und Bedienungsanleitung ist Verteidigungsstandard — Rechtsprechung uneinheitlich: BVerfG, Beschl. v. 12.11.2020 – 2 BvR 1616/18 (rechtliches Gehör verlangt Zugang zu nicht aktenkundigen Informationen, `[unverifiziert – Az. prüfen]`); vgl. ferner BVerfG 2 BvR 1167/20 `[unverifiziert]`. Die OLG-Linie ist gespalten (insb. OLG Bamberg/Karlsruhe großzügiger, OLG Düsseldorf zurückhaltender).

### 5. Fahrverbot § 25 StVG

- Regelfahrverbot 1 Monat bei qualifizierten Verstößen (vgl. Anlage zur BKatV).
- **Absehen vom Fahrverbot § 4 Abs. 4 BKatV** bei besonderer Härte (idR berufliche Existenzgefährdung) gegen Erhöhung der Geldbuße. Maßstab streng: bloße Unbequemlichkeit genügt nicht (OLG Hamm, OLG Bamberg, `[unverifiziert – prüfen]`).
- **4-Monats-Antritts-Frist** § 25 Abs. 2a StVG (bei Ersttätern: Antritt binnen 4 Monaten ab Rechtskraft selbst wählbar).

### 6. Verteidigungsstrategien

- **Bestreiten der Fahrereigenschaft** (Halterhaftung nur bei Parkverstößen § 25a StVG; sonst Fahrer-Identifizierung erforderlich).
- **Messfehler** (Aufstellort, fehlende Eichung, abweichende Bedienungsanleitung, Reflexionen, Front-/Heckmessung).
- **Verfahrensfehler** (Zustellung, Verfolgungsverjährung, Doppelverfolgung § 21 OWiG bei parallelem Strafverfahren).
- **Absehen vom Fahrverbot** § 4 IV BKatV (berufliche Härte, ärztliche Notwendigkeit etc.).
- **Punkte und FAER**: Konkrete Punktzahl nur unter Bezug auf die geltende **Anlage zur BKatV** angeben (Stand prüfen).

### 7. Hauptverhandlung erzwingen

Nach Einspruch und Anberaumung der Hauptverhandlung (§ 71 OWiG) kann der Betroffene weitere Beweisanträge stellen. Verzicht auf Erscheinen nach § 73 II OWiG möglich. Die Rechtsbeschwerde § 79 OWiG ist nur eingeschränkt zulässig (Zulassungsbeschwerde § 80 OWiG).

### 8. Schnittstelle Strafrecht

- Bei §§ 142, 315c, 316 StGB ist die Tat zugleich Straftat. § 21 OWiG sperrt die OWi-Verfolgung, wenn dieselbe Handlung zugleich Straftat ist und die Straftat verfolgt wird.
- Bei BAK über 1,1 ‰: absolute Fahruntüchtigkeit, § 316 StGB (kein OWi-Verfahren mehr).
- Bei BAK 0,5–1,1 ‰: § 24a StVG OWi (oder § 316 StGB bei relativer Fahruntüchtigkeit mit Ausfallerscheinungen).

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 24 StVG](https://www.gesetze-im-internet.de/stvg/__24.html) (OWi-Generalklausel)
- [§ 24a StVG](https://www.gesetze-im-internet.de/stvg/__24a.html) (0,5-Promille-Grenze)
- [§ 25 StVG](https://www.gesetze-im-internet.de/stvg/__25.html) (Fahrverbot)
- [§ 25a StVG](https://www.gesetze-im-internet.de/stvg/__25a.html) (Halterhaftung Park-OWi)
- [§ 26 StVG](https://www.gesetze-im-internet.de/stvg/__26.html) (Verfolgungsverjährung)
- [§ 29 StVG](https://www.gesetze-im-internet.de/stvg/__29.html) (FAER)
- [StVO](https://www.gesetze-im-internet.de/stvo_2013/) – §§ 1, 3, 4, 7–9, 23, 24, 49
- [BKatV](https://www.gesetze-im-internet.de/bkatv_2013/) (mit Anlage Bußgeldkatalog) – § 4 IV (Absehen vom Fahrverbot)
- [§ 17 OWiG](https://www.gesetze-im-internet.de/owig_1968/__17.html); [§ 21 OWiG](https://www.gesetze-im-internet.de/owig_1968/__21.html); [§ 26 OWiG](https://www.gesetze-im-internet.de/owig_1968/__26.html); [§ 31 OWiG](https://www.gesetze-im-internet.de/owig_1968/__31.html); [§ 33 OWiG](https://www.gesetze-im-internet.de/owig_1968/__33.html); [§ 46 OWiG](https://www.gesetze-im-internet.de/owig_1968/__46.html); [§ 66 OWiG](https://www.gesetze-im-internet.de/owig_1968/__66.html); [§ 67 OWiG](https://www.gesetze-im-internet.de/owig_1968/__67.html); [§ 71 OWiG](https://www.gesetze-im-internet.de/owig_1968/__71.html); [§ 79 OWiG](https://www.gesetze-im-internet.de/owig_1968/__79.html); [§ 80 OWiG](https://www.gesetze-im-internet.de/owig_1968/__80.html)
- [§ 147 StPO](https://www.gesetze-im-internet.de/stpo/__147.html) iVm § 46 OWiG (Akteneinsicht)
- [§ 142 StGB](https://www.gesetze-im-internet.de/stgb/__142.html); [§ 315c StGB](https://www.gesetze-im-internet.de/stgb/__315c.html); [§ 316 StGB](https://www.gesetze-im-internet.de/stgb/__316.html)

### Kommentare

- Burhoff, Handbuch für das straßenverkehrsrechtliche OWi-Verfahren, 6. Aufl. 2021
- Krenberger/Krumm, OWiG, 7. Aufl. 2024, § 66 OWiG Rn. 1 ff., § 67 OWiG Rn. 1 ff.
- Göhler, OWiG, 19. Aufl. 2024, § 66 Rn. 1 ff.
- Krumm, in: Hentschel/König/Dauer, Straßenverkehrsrecht, 47. Aufl. 2023, § 25 StVG Rn. 1 ff., BKatV Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris/Beck-Online]`)

1. BGH, Beschl. v. 19.08.1993 – 4 StR 627/92, BGHSt 39, 291 (standardisiertes Messverfahren)
2. BVerfG, Beschl. v. 12.11.2020 – 2 BvR 1616/18 (rechtliches Gehör / Akteneinsicht Rohmessdaten)
3. BVerfG, Beschl. v. 20.06.2023 – 2 BvR 1167/20 (Akteneinsicht standardisierte Messverfahren — Aktenzeichen prüfen)
4. OLG Bamberg, Beschl. v. 13.06.2018 – 3 Ss OWi 626/18 (Bedienungsanleitung als Verteidigungsmaterial)
5. OLG Hamm, Beschl. v. 09.07.2019 – 4 RBs 211/19 (Absehen vom Fahrverbot bei beruflicher Härte)

## Ausgabeformat

```
EINSPRUCHSBEGRÜNDUNG / GUTACHTEN — OWi nach StVO
Bescheid: <Bußgeldbehörde, Az., Zustellungsdatum>
Einspruchsfrist § 67 OWiG: <Datum>

I.   Sachverhalt
II.  Frage(n)
III. Kurzantwort
     – Einspruch erfolgversprechend: [ja / nein / teilweise]
     – Ziel: [Einstellung / Reduzierung Bußgeld / Absehen Fahrverbot]

IV.  Rechtliche Bewertung
     1. Formelle Prüfung Bußgeldbescheid (§ 66 OWiG)
     2. Verfolgungsverjährung (§ 26 III StVG, § 31 OWiG)
     3. Materielle Tatbestandsverwirklichung
        a) StVO-Norm
        b) BKatV-Anlage (Stand prüfen!)
        c) Messverfahren / Beweiswürdigung
     4. Rechtsfolgen
        a) Geldbuße § 17 OWiG
        b) FAER-Punkte (Stand BKatV-Anlage)
        c) Fahrverbot § 25 StVG
        d) Absehen § 4 IV BKatV (besondere Härte)
     5. Schnittstelle StGB §§ 142, 315c, 316; § 21 OWiG

V.   Beweisanträge / Akteneinsichtsanträge
     – Akteneinsicht § 147 StPO iVm § 46 OWiG
     – Rohmessdaten, Eichschein, Bedienungsanleitung
     – ggf. Sachverständiger zum Messverfahren

VI.  Risiken / offene Punkte
     🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VII. Fristenkalender
     – Einspruchsfrist § 67 OWiG: <Datum>
     – Verfolgungsverjährung: <Datum>

VIII. Quellenverzeichnis
```

## Beispiel (Auszug, Urteilsstil)

> **III. Kurzantwort.** Der Einspruch ist innerhalb der Frist des § 67 Abs. 1 OWiG einzulegen. Eine Reduzierung der Sanktion ist über zwei Linien zu verfolgen: erstens Akteneinsicht in Rohmessdaten und Bedienungsanleitung des verwendeten Lasermessgeräts (BVerfG, Beschl. v. 12.11.2020 – 2 BvR 1616/18 `[unverifiziert – prüfen]`), zweitens Antrag auf Absehen vom Fahrverbot nach § 4 Abs. 4 BKatV unter Darlegung der beruflichen Existenzgefährdung.
>
> **IV.4.d) Absehen § 4 IV BKatV.** Die Mandantin ist als Außendienstmitarbeiterin auf den Führerschein zwingend angewiesen; ein einmonatiges Fahrverbot würde mit überwiegender Wahrscheinlichkeit zur Kündigung des Arbeitsverhältnisses führen. Das ist nach der OLG-Linie (OLG Hamm, Beschl. v. 09.07.2019 – 4 RBs 211/19 `[unverifiziert]`) ein Härtefall, der das Absehen gegen Erhöhung der Geldbuße trägt.

## Risiken / typische Fehler

- **Einspruchsfrist § 67 OWiG** (2 Wochen) versäumt — Wiedereinsetzung § 52 OWiG nur eng möglich.
- **Verfolgungsverjährung § 26 III StVG** nicht geprüft — typische Lücke bei langsamen Bußgeldstellen.
- **Punkte- oder Bußgeldhöhe** ohne Bezug auf die geltende **Anlage zur BKatV** behauptet — Stand-Hinweis fehlt.
- **Pauschale Absehen-Argumentation** ohne konkrete Darlegung der beruflichen Härte.
- **§ 21 OWiG übersehen**, wenn dieselbe Tat zugleich Straftat ist (insb. §§ 142, 315c, 316 StGB).
- **Akteneinsicht nicht beantragt** — Rohmessdaten und Bedienungsanleitung sind Pflichtmaterial der Verteidigung.
- **Halterhaftung § 25a StVG** mit Fahrerhaftung verwechseln (Halterhaftung nur bei Parkverstößen).
