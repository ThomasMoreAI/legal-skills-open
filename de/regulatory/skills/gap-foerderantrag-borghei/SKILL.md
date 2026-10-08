---
name: gap-foerderantrag-borghei
title: /agrarrecht:gap-foerderantrag
description: 'Begleitung und Verteidigung des Sammelantrags GAP 2023–2027 – Direktzahlungen (Einkommensgrundstützung, Umverteilung, Junglandwirteprämie, gekoppelte Stützung), Öko-Regelungen, Konditionalität (GLÖZ 1–9, GAB), Sanktionsbemessung, Widerspruch und Klage. Statutory anchors: VO (EU) 2021/2115, 2021/2116; GAP-DZG; GAPInVeKoSG; GAP-KondV; GAP-IntegrV. Use when ein Betriebsinhaber den Sammelantrag vorbereitet, eine Bewilligung erhält, eine Kürzung/Sanktion verteidigt oder Widerspruch/Klage erwägt.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/agrarrecht/skills/gap-foerderantrag
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: regulatory
language: de
---

# /agrarrecht:gap-foerderantrag

## Zweck

Der Skill begleitet den **GAP-Sammelantrag** (Gemeinsame Agrarpolitik 2023–2027) und seine Verteidigung in Widerspruch und verwaltungsgerichtlicher Klage. Er deckt die Direktzahlungen der 1. Säule (Einkommensgrundstützung, ergänzende Umverteilungseinkommensstützung, Junglandwirteprämie, gekoppelte Einkommensstützung), die **Öko-Regelungen** (Eco-Schemes nach Art. 31 VO (EU) 2021/2115) und die **Konditionalität** (GLÖZ-Standards und GAB nach Anhang III VO (EU) 2021/2115) ab. Er adressiert Sanktionsbemessung und das Widerspruchs- und Klageverfahren gegen Bewilligungs- und Rücknahmebescheide.

## Eingaben

- Betriebsdaten (Betriebsnummer InVeKoS — als `[Betr.-Nr.]` redigieren; Bundesland; Hektar landwirtschaftliche Nutzfläche; Flurstückzuordnung als anonymisierte Liste)
- Antragsjahr und konkreter Verfahrensstand (in Vorbereitung / bewilligt / Kürzung angedroht / Rücknahme nach § 48 VwVfG / Widerspruch / Klage)
- Beantragte Förderkomponenten (Basisprämie, Umverteilung, Junglandwirte, gekoppelte Stützung, Öko-Regelungen 1–7)
- Behauptete Konditionalitätsverstöße (welcher GLÖZ / GAB; Tatsachenbasis Vor-Ort-Kontrolle / Fernerkundung / Monitoring)
- Frühere Bescheide und Kürzungshistorie

## Sub-Agent-Architektur

Researcher liefert die einschlägigen EU-VO-Vorschriften (insb. VO (EU) 2021/2115 und 2021/2116) mit CELEX-Links, das deutsche Durchführungsrecht (GAP-DZG, GAPInVeKoSG, GAP-KondV, GAP-IntegrV), BVerwG-/OVG-Linien zur Rücknahme und zur Sanktionsbemessung sowie die jährlichen Beträge mit `[unverifiziert – aktueller Stand prüfen]`. Drafter erstellt im Gutachtenstil eine Antragsbegleitung oder Widerspruchsbegründung, die Konditionalität, Verhältnismäßigkeit der Sanktion und Beweislast adressiert. Reviewer prüft Stichtag, Sanktionsbemessung, Anwendungsvorrang der EU-VO und das Risiko von Folgejahresausschlüssen.

## Ablauf

### 1. Anwendungsbereich und Antragsberechtigung

Prüfung, ob der Mandant **Betriebsinhaber** iSv Art. 3 Nr. 1 VO (EU) 2021/2115 ist (landwirtschaftliche Tätigkeit nach Art. 4 Abs. 2 VO (EU) 2021/2115, Mindestschwelle für Direktzahlungen nach Art. 18). Sachlich: **förderfähige Hektarfläche** nach Art. 4 Abs. 4 VO (EU) 2021/2115 iVm § 4 GAP-DZG. Zeitlich: Antragsjahr und Stichtag des Sammelantrags (landesrechtlich bestimmt, jährlich kommuniziert) `[unverifiziert – aktueller Stand prüfen]`.

### 2. Förderkomponenten der 1. Säule

| Komponente | Rechtsgrundlage | Hinweis |
|---|---|---|
| Einkommensgrundstützung (Basisprämie) | Art. 21–28 VO (EU) 2021/2115; §§ 4 ff. GAP-DZG | EUR/ha jährlich rechtsfortbildend `[unverifiziert]` |
| Ergänzende Umverteilungseinkommensstützung | Art. 29 VO (EU) 2021/2115; § 9 GAP-DZG | Erste Hektare höher vergütet; Schwellen jährlich `[unverifiziert]` |
| Junglandwirteprämie | Art. 30 VO (EU) 2021/2115; § 10 GAP-DZG | Altersgrenze, Erstniederlassung, max. Jahre `[unverifiziert]` |
| Gekoppelte Einkommensstützung | Art. 32 ff. VO (EU) 2021/2115; § 11 GAP-DZG | DE: Mutterschafe/-ziegen, Mutterkühe `[unverifiziert]` |

### 3. Öko-Regelungen (Art. 31 VO (EU) 2021/2115; § 20 GAP-DZG)

Sieben Öko-Regelungen in Deutschland (Stand 2023–2024 `[unverifiziert – aktueller Stand prüfen]`):
1. Bereitstellung von Flächen zur Verbesserung der Biodiversität (Brachen über die Konditionalität hinaus)
2. Anbau vielfältiger Kulturen
3. Beibehaltung agroforstwirtschaftlicher Bewirtschaftung auf Ackerland
4. Extensivierung von Dauergrünland
5. Ergebnisorientierte extensive Bewirtschaftung von Dauergrünland (Kennarten)
6. Bewirtschaftung von Acker- und Dauerkulturflächen ohne Pflanzenschutzmittel
7. Anwendung von Pflanzenschutzmitteln in Schutzgebieten

Förderhöhe je Öko-Regelung jährlich bekanntgegeben. Mehrfachförderung mit ELER-Maßnahmen ist nach dem Doppelförderungsverbot (Art. 36 VO (EU) 2021/2116) auszuschließen.

### 4. Konditionalität (Art. 12, 13 VO (EU) 2021/2115; GAP-KondV)

**GLÖZ-Standards** (Anhang III VO (EU) 2021/2115; präzisiert in der GAP-KondV):

| GLÖZ | Inhalt (gerafft) |
|---|---|
| 1 | Erhaltung Dauergrünland (Anteilsschwelle, Genehmigungspflicht Umbruch) |
| 2 | Schutz Feuchtgebiete und Moore |
| 3 | Verbot Stoppelabbrennen |
| 4 | Pufferstreifen entlang Wasserläufen |
| 5 | Bodenbearbeitung zur Erosionsminderung |
| 6 | Mindestbodenbedeckung über den Winter |
| 7 | Fruchtwechsel |
| 8 | Mindestanteil nichtproduktiver Flächen / Landschaftselemente |
| 9 | Verbot Umbruch ökologisch sensibler Dauergrünlandflächen |

**Grundanforderungen Betriebsführung (GAB)** — Anhang III VO (EU) 2021/2115 verweist auf nationale Umsetzung u. a. der DüV, der Pflanzenschutz-VO, der Habitat- und Vogelschutzrichtlinie sowie der Wasserrahmenrichtlinie.

### 5. Sanktionsbemessung bei Konditionalitätsverstößen

Rechtsgrundlage: Art. 84, 85 VO (EU) 2021/2116; konkretisiert in der DV (EU) 2022/1172 `[unverifiziert]`. Bemessungsstufen idR:

- **Fahrlässig**: Kürzung Direktzahlungen idR 3 %, je nach Schwere/Ausmaß/Dauer 1 %–5 %
- **Vorsätzlich**: 15 %–100 %; Ausschluss möglich
- **Wiederholung**: Faktor 3 auf den Prozentsatz bis 15 %; danach Vorsatzpfad

Verhältnismäßigkeit (Art. 59 VO (EU) 2021/2116) und Verschuldensmaßstab sind in jeder Begründung zu adressieren — pauschale Kürzungen ohne Einzelfallabwägung sind angreifbar.

### 6. Verfahren und Rechtsschutz

- **Sammelantrag** über das InVeKoS-Portal des jeweiligen Bundeslandes; Stichtag jährlich kommuniziert. **Nachfristen** und Anteilskürzungen nach Art. 8 DV (EU) 2022/1173 `[unverifiziert]`.
- **Bewilligungsbescheid** der Landesbehörde. **Rücknahme** und **Widerruf** für die Vergangenheit nach §§ 48, 49 VwVfG iVm Vertrauensschutz (insb. § 48 Abs. 2 VwVfG).
- **Widerspruch** § 70 VwGO innerhalb 1 Monats ab Bekanntgabe; aufschiebende Wirkung § 80 VwGO grundsätzlich gegeben, kann durch Anordnung der sofortigen Vollziehung entfallen.
- **Klageweg**: idR Verwaltungsgericht (§ 40 VwGO); in einzelnen Bundesländern für bestimmte Förderarten besondere Zuständigkeiten möglich `[unverifiziert – landesrechtlich prüfen]`.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### EU-Recht

- [VO (EU) 2021/2115](https://eur-lex.europa.eu/eli/reg/2021/2115/oj) (GAP-Strategieplan-VO)
- [VO (EU) 2021/2116](https://eur-lex.europa.eu/eli/reg/2021/2116/oj) (Horizontale VO – Finanzierung, Verwaltung, Konditionalität, InVeKoS)
- [VO (EU) 2021/2117](https://eur-lex.europa.eu/eli/reg/2021/2117/oj) (Änderungs-VO Landwirtschaft)
- DurchführungsVO (EU) 2022/1172, 2022/1173 (InVeKoS, Sanktionen, Antragsverfahren) `[unverifiziert]`
- GAP-Strategieplan Deutschland 2023–2027

### Deutsches Recht

- [GAP-DZG](https://www.gesetze-im-internet.de/gapdzg/) (Direktzahlungen-Durchführungsgesetz)
- [GAPInVeKoSG](https://www.gesetze-im-internet.de/gapinvekosg/) (Integriertes Verwaltungs- und Kontrollsystem)
- [GAP-KondV](https://www.gesetze-im-internet.de/gap-kondv/) (Konditionalitätsverordnung)
- [GAP-IntegrV](https://www.gesetze-im-internet.de/gap-integrv/) (Integrierter Antrag)
- [§§ 48, 49 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__48.html) (Rücknahme/Widerruf)
- [§ 70 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html) (Widerspruchsfrist)

### Kommentare

- Düsing, in: Düsing/Martinez, Agrarrecht, Stand 2024, GAP-DZG / GAP-KondV `[unverifiziert]`
- Martinez, in: Düsing/Martinez, Agrarrecht, Stand 2024, VO (EU) 2021/2115 `[unverifiziert]`
- Norer, Handbuch des Agrarrechts, 3. Aufl. `[unverifiziert]`

### Rechtsprechung (`[unverifiziert – prüfen in juris/curia.europa.eu]`)

1. EuGH-Rechtsprechung zur Vorgänger-VO (EU) Nr. 1307/2013 zur Verhältnismäßigkeit der Konditionalitätssanktionen — für VO (EU) 2021/2115 nur eingeschränkt übertragbar.
2. BVerwG zu Rücknahme von Agrarsubventionen nach § 48 VwVfG und unionsrechtlich determiniertem Vertrauensschutz.
3. OVG-Linien (insb. OVG Lüneburg, OVG Greifswald, OVG Magdeburg) zur Fernerkundungs-Beweislast.

## Ausgabeformat

```
GUTACHTEN — GAP-Sammelantrag / Konditionalität
Betrieb: [Betr.-Nr.], Bundesland, Antragsjahr JJJJ

I. Sachverhalt (knapp)
II. Frage(n)
III. Kurzantwort
     – Antragsberechtigung: [ja / nein / unklar]
     – Empfehlung: [Antrag stellen / Korrektur / Widerspruch / Klage]

IV. Rechtliche Bewertung
    1. Anwendungsbereich und Antragsberechtigung
       (Betriebsinhaber Art. 3 VO (EU) 2021/2115; förderfähige Hektar)
    2. Förderkomponenten der 1. Säule
       (Basisprämie, Umverteilung, Junglandwirte, gekoppelte Stützung)
    3. Öko-Regelungen
       (welche Maßnahmen, Doppelförderungsverbot)
    4. Konditionalität
       a) GLÖZ-Standards (welcher Verstoß)
       b) GAB (welche Norm)
       c) Beweislage (Vor-Ort, Fernerkundung, Monitoring)
    5. Sanktionsbemessung
       (Fahrlässigkeit / Vorsatz / Wiederholung; Verhältnismäßigkeit
        Art. 59 VO (EU) 2021/2116)
    6. Rechtsschutz
       (Widerspruch § 70 VwGO; Klage; aufschiebende Wirkung)

V. Antrag / Empfehlung
   – z. B. "Widerspruch wird eingelegt; aufschiebende Wirkung
     gewährt § 80 Abs. 1 VwGO; hilfsweise Antrag nach § 80 V VwGO."

VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VII. Frist-Tabelle
     <übernommen vom Researcher>

VIII. Quellenverzeichnis
```

## Beispiel (Auszug, Gutachtenstil)

> **III. Konditionalität, GLÖZ 8.** Die Landesbehörde stützt die Kürzung von 5 % auf einen Verstoß gegen GLÖZ 8 (Mindestanteil nichtproduktive Flächen, Art. 13 i.V.m. Anhang III VO (EU) 2021/2115). Maßgeblich ist § 11 GAP-KondV. Der Mandant hat ausweislich der eingereichten Flurstücksliste 4,2 % nichtproduktive Flächen ausgewiesen; die geforderte Mindestschwelle beträgt nach § 11 Abs. 1 GAP-KondV 4 % der Ackerfläche `[unverifiziert – aktueller Stand prüfen]`. Damit ist der GLÖZ-Standard formal eingehalten; die Kürzung trägt nicht. Ferner ist nach Art. 59 VO (EU) 2021/2116 die Verhältnismäßigkeit zu wahren — selbst bei Verstoß wäre eine Kürzung von 5 % bei erstmaliger und geringfügiger Abweichung als unverhältnismäßig anzusehen, da die GAP-KondV in § 19 Abs. 1 eine Bandbreite von 1 % bis 5 % je nach Schwere vorsieht `[unverifiziert]`.

## Risiken / typische Fehler

- **Verspäteter Sammelantrag**. Kürzung 1 % je Werktag nach Stichtag; nach 25 Werktagen Komplettausschluss `[unverifiziert – aktueller Stand prüfen]`.
- **Doppelförderung Öko-Regelung + ELER-Maßnahme** (Verstoß Art. 36 VO (EU) 2021/2116).
- **Pauschale Übernahme der Behördensanktion** ohne Prüfung von Verschuldensgrad und Verhältnismäßigkeit (Art. 59 VO (EU) 2021/2116).
- **Übersehen der unionsrechtlich determinierten Vertrauensschutzgrenzen** bei Rücknahme nach § 48 VwVfG (EuGH-Linie strenger als § 48 Abs. 2 VwVfG).
- **Nicht ausgenutzte aufschiebende Wirkung** des Widerspruchs (§ 80 Abs. 1 VwGO).
- **Konkreten EUR/ha-Betrag** ohne `[unverifiziert – aktueller Stand prüfen]` ausweisen — die Beträge ändern sich jährlich.
- **Verkennen, dass das BVerwG / OVG**, nicht das Landwirtschaftsgericht, zuständig ist (anders als beim Grundstücksverkehr).
