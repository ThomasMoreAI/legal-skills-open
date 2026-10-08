---
name: sgb-vi-rentenanspruch-borghei
title: /sozialrecht:sgb-vi-rentenanspruch
description: Prüfung des Rentenanspruchs nach SGB VI – Altersrenten §§ 35–38 (Regelaltersrente, langjährig / besonders langjährig Versicherte, Schwerbehinderte), Erwerbsminderungsrente §§ 43, 50, 51 (volle vs. teilweise EM, Wartezeit, besondere versicherungsrechtliche Voraussetzungen), Hinzuverdienst § 96a. Use when Mandantin Renteneintritt plant, Erwerbsminderung geltend macht oder einen Rentenbescheid prüft.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/sozialrecht/skills/sgb-vi-rentenanspruch
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: social-security
language: de
---

# /sozialrecht:sgb-vi-rentenanspruch

## Zweck

Renten nach SGB VI sind beitragsbasiert; jeder Anspruch hängt von versicherungsrechtlichen Voraussetzungen (Wartezeit § 50, Pflichtbeiträge § 51) und persönlichen Voraussetzungen (Alter, gesundheitlicher Leistungsfall) ab. Dieser Skill prüft systematisch beide Achsen und bestimmt, **welche** Rentenart in Betracht kommt und ob ein Antrag erfolgversprechend ist.

## Eingaben

- Geburtsdatum, Geschlecht, Versicherungsnummer (anonymisiert)
- Versicherungsverlauf: Pflichtbeitragszeiten, freiwillige Beiträge, Anrechnungszeiten, Berücksichtigungszeiten (z. B. Kindererziehung § 56 SGB VI, Pflegezeiten § 3 S. 1 Nr. 1a SGB VI)
- Letzte ausgeübte Beschäftigung / Selbständigkeit (Datum, Dauer)
- Gesundheitlicher Befund (bei EM-Antrag): Diagnose, sozialmedizinisches Leistungsvermögen (Stunden pro Tag auf dem allgemeinen Arbeitsmarkt), Reha-Maßnahmen
- Schwerbehinderung (Grad, Feststellungsbescheid Versorgungsamt)
- Bisherige Rentenbescheide / Renteninformation / Rentenauskunft
- Aktueller Hinzuverdienst (Brutto pro Jahr)

## Sub-Agent-Architektur

Researcher liefert SGB-VI-Normen, Kassler Kommentar / jurisPK-SGB VI sowie BSG-Rechtsprechung zu Wartezeit, Leistungsfall und Berufsschutz. Drafter erstellt die Anspruchsprüfung nach Rentenarten gestaffelt. Reviewer prüft Antragsfrist § 99 SGB VI, Mitwirkung § 60 SGB I, Hinzuverdienst und das Zusammenspiel mit ALG II / SGB XII.

## Ablauf

### 1. Versicherungsrechtliche Voraussetzungen

| Voraussetzung | Norm | Inhalt |
|---|---|---|
| Wartezeit | [§ 50 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__50.html) | Mindestversicherungszeit: 5 J. (allgemein), 35 J. (langjährig Versicherte), 45 J. (besonders langjährig) |
| Anrechenbare Zeiten | [§§ 51, 54–58 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__51.html) | Pflichtbeiträge, freiwillige Beiträge, Anrechnungs-, Berücksichtigungs-, Ersatzzeiten |
| Bes. vers.-rechtl. Voraussetzung bei EM | [§ 43 Abs. 1 Nr. 2 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__43.html) | 3 Jahre Pflichtbeiträge in den letzten 5 Jahren vor Leistungsfall |

### 2. Altersrenten — Rentenarten

| Rentenart | Norm | Wartezeit | Altersgrenze |
|---|---|---|---|
| Regelaltersrente | [§ 35 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__35.html) | 5 J. | Regelaltersgrenze § 235 SGB VI (gestaffelt auf 67) |
| Langjährig Versicherte | [§ 36 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__36.html) | 35 J. | 63, mit Abschlägen 0,3 %/Monat |
| Besonders langjährig Versicherte | [§ 38 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__38.html) | 45 J. | 65 (geb. 1953 ff. ggf. später) — **abschlagsfrei** |
| Schwerbehinderte Menschen | [§ 37 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__37.html) | 35 J. | 65 mit Abschlägen ab 62 (GdB ≥ 50 erforderlich) |

Hinweise:

- **Vorgezogene Inanspruchnahme** § 77 SGB VI: Abschlag 0,3 % je Monat (3,6 %/Jahr) der vorzeitigen Inanspruchnahme; Zuschlag bei späterem Beginn.
- **Sonderfälle bei langjährig Versicherten:** anrechnungsfähig sind insb. Pflichtbeitragszeiten, Berücksichtigungszeiten für Kindererziehung, Anrechnungszeiten wegen Krankheit / Schwangerschaft (§ 51 SGB VI).

### 3. Erwerbsminderungsrente ([§ 43 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__43.html))

**Volle EM (§ 43 Abs. 2):** Leistungsvermögen < 3 Stunden täglich auf dem allgemeinen Arbeitsmarkt.

**Teilweise EM (§ 43 Abs. 1):** Leistungsvermögen ≥ 3, aber < 6 Stunden täglich.

Voraussetzungen kumulativ:

1. **Medizinische Voraussetzungen** (sozialmedizinisches Gutachten der DRV / MDK)
2. **Allgemeine Wartezeit** 5 Jahre (§ 50 Abs. 1 S. 1 Nr. 2 SGB VI)
3. **Besondere versicherungsrechtliche Voraussetzungen** (§ 43 Abs. 1 S. 1 Nr. 2 SGB VI): mind. 3 Jahre Pflichtbeiträge in den letzten 5 Jahren vor Leistungsfall
4. **Verschlossener Teilzeitarbeitsmarkt:** Bei teilweiser EM gilt § 43 Abs. 3 SGB VI; faktisch wird volle EM gewährt, wenn der Teilzeitarbeitsmarkt verschlossen ist (BSG, st. Rspr. — sog. "konkrete Betrachtungsweise" `[unverifiziert – prüfen]`)

**Berufsschutz:** Nur für Versicherte, die vor dem 02.01.1961 geboren sind ([§ 240 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__240.html) — Renten wegen teilweiser Erwerbsminderung bei Berufsunfähigkeit).

### 4. Hinzuverdienst ([§ 96a SGB VI](https://www.gesetze-im-internet.de/sgb_6/__96a.html))

Seit 01.01.2023 ist der Hinzuverdienst bei Altersrenten **unbeschränkt**.

Bei Erwerbsminderungsrenten gelten Hinzuverdienstgrenzen:

- **Volle EM:** dynamische Grenze (ca. 18.500 EUR jährlich, Stand prüfen)
- **Teilweise EM:** höhere Grenze, einkommensabhängig

Übersteigt der Hinzuverdienst die Grenze, wird die Rente anteilig gekürzt (§ 96a Abs. 1a SGB VI).

### 5. Antragstellung ([§ 99 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__99.html), [§§ 115 ff.](https://www.gesetze-im-internet.de/sgb_6/__115.html))

- **Antragserfordernis:** Rente wird nur auf Antrag gewährt.
- **Rückwirkung:** Antrag, der innerhalb von 3 Kalendermonaten nach Ablauf des Monats gestellt wird, in dem die Anspruchsvoraussetzungen erfüllt waren, gilt als zum Anfang dieses Monats gestellt.
- **Reha vor Rente** (§ 9 SGB VI): EM-Anträge werden regelmäßig als Reha-Anträge geprüft.

### 6. Verfahren

- Antrag bei der DRV (regional oder Bund), § 19 SGB I.
- Bescheid = Verwaltungsakt § 31 SGB X; Begründungspflicht § 35 SGB X.
- Widerspruch § 84 SGG (1 Monat), Klage SG § 87 SGG.
- Bei Rentenüberzahlung: Erstattung § 50 SGB X i.V.m. Rücknahme § 45 SGB X.

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 35](https://www.gesetze-im-internet.de/sgb_6/__35.html), [§ 36](https://www.gesetze-im-internet.de/sgb_6/__36.html), [§ 37](https://www.gesetze-im-internet.de/sgb_6/__37.html), [§ 38](https://www.gesetze-im-internet.de/sgb_6/__38.html), [§ 43](https://www.gesetze-im-internet.de/sgb_6/__43.html), [§ 50](https://www.gesetze-im-internet.de/sgb_6/__50.html), [§ 51](https://www.gesetze-im-internet.de/sgb_6/__51.html), [§ 77](https://www.gesetze-im-internet.de/sgb_6/__77.html), [§ 96a](https://www.gesetze-im-internet.de/sgb_6/__96a.html), [§ 99](https://www.gesetze-im-internet.de/sgb_6/__99.html), [§ 235](https://www.gesetze-im-internet.de/sgb_6/__235.html), [§ 240](https://www.gesetze-im-internet.de/sgb_6/__240.html) SGB VI
- [§ 9 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__9.html) (Reha vor Rente)
- [§ 60 SGB I](https://www.gesetze-im-internet.de/sgb_1/__60.html)

### Kommentare

- Kreikebohm, in: KassKomm, Stand 2024, § 43 SGB VI Rn. … (Erwerbsminderungsrente)
- Fichte, in: Hauck/Noftz SGB VI, § 50 Rn. … (Wartezeitanrechnung)
- Klattenhoff, in: jurisPK-SGB VI, 3. Aufl. 2024, § 35 Rn. … (Regelaltersrente, Übergangsregelungen)
- Wengler, in: BeckOK SozR, § 96a SGB VI Rn. … (Hinzuverdienst nach Reform 2023)

### Rechtsprechung (`[unverifiziert – prüfen in juris / SozR]`)

1. BSG, Urt. v. 17.02.2010 – B 5 R 130/08 R (volle EM bei verschlossenem Teilzeitarbeitsmarkt — "konkrete Betrachtungsweise")
2. BSG, Urt. v. 23.03.2006 – B 11a AL 29/05 R (versicherungsrechtliche Voraussetzungen, Streckungstatbestände § 43 Abs. 4)
3. BSG, Urt. v. 28.06.2018 – B 5 R 25/17 R (Wartezeitanrechnung Berücksichtigungszeiten Kindererziehung)
4. BVerfG, Beschl. v. 11.01.2011 – 1 BvR 3588/08 (Stichtagsregelung Berufsunfähigkeit § 240 SGB VI)

## Ausgabeformat

```
RENTENANSPRUCHSPRÜFUNG — <Mandant/in, anonymisiert>
Stand: <Datum> — Risikoeinstufung: 🟢/🟡/🔴

A. Sachverhalt
   - Geburtsdatum / Alter / Geschlecht
   - Versicherungsverlauf (Jahre PflBeitr., AnrZ., BerZ.)
   - Gesundheitlicher Status (bei EM)
   - Beschäftigungsstatus aktuell
   - Schwerbehinderung (GdB)

B. In Betracht kommende Rentenart(en)
   - Regelaltersrente § 35 — Voraussetzungen erfüllt? <…>
   - Altersrente langjährig Versicherte § 36 — <…>
   - Altersrente besonders langjährig Versicherte § 38 — <…>
   - Altersrente Schwerbehinderte § 37 — <…>
   - Erwerbsminderungsrente § 43 (voll / teilweise) — <…>

C. Versicherungsrechtliche Voraussetzungen
   - Wartezeit § 50: erfüllt mit <X> Jahren / Beitragsmonaten
   - Besondere vers.-rechtl. Voraussetzung § 43 Abs. 1 Nr. 2: <…>

D. Persönliche Voraussetzungen
   - Altersgrenze: <…>
   - Leistungsfall EM: <Datum / streitig>
   - Sozialmedizinisches Leistungsvermögen: <Stunden/Tag>

E. Abschläge / Zuschläge § 77 SGB VI
   - Vorzeitige Inanspruchnahme: −0,3 %/Monat = <…> %
   - Aufschub: +0,5 %/Monat

F. Hinzuverdienst § 96a
   - <Brutto/Jahr> vs. Grenze <…> EUR

G. Antrag / Verfahren
   - Antrag bei DRV-Träger <…>
   - Antragsfrist § 99 SGB VI (3 Monate Rückwirkung)
   - Mitwirkung § 60 SGB I (Unterlagen, ärztl. Befunde)
   - Ggf. Reha vor Rente § 9 SGB VI

H. Risiken / offene Punkte
   - <…>

I. Quellenverzeichnis
```

## Beispiele

### Beispiel (gekürzter Auszug, Gutachtenstil)

> M. (52 J., männlich) ist seit dem 14.08.2025 arbeitsunfähig wegen chronischer Wirbelsäulenerkrankung. Eine medizinische Reha im Frühjahr 2026 brachte keine wesentliche Besserung; das sozialmedizinische Gutachten der DRV vom 03.04.2026 attestiert ein Leistungsvermögen von täglich unter 3 Stunden auf dem allgemeinen Arbeitsmarkt.
>
> **I. Versicherungsrechtliche Voraussetzungen.** Die allgemeine Wartezeit von fünf Jahren (§ 50 Abs. 1 S. 1 Nr. 2 SGB VI) ist mit 12 Jahren Pflichtbeiträgen erfüllt. Die **besonderen versicherungsrechtlichen Voraussetzungen** (§ 43 Abs. 1 S. 1 Nr. 2 SGB VI) verlangen 3 Jahre Pflichtbeiträge in den letzten 5 Jahren vor Eintritt der Erwerbsminderung; ausweislich des Versicherungsverlaufs liegen 5 durchgehende Pflichtbeitragsjahre vor — die Voraussetzung ist damit erfüllt.
>
> **II. Persönliche Voraussetzungen.** Der Leistungsfall ist nach der Befundlage spätestens am 03.04.2026 eingetreten; das attestierte Leistungsvermögen von unter 3 Stunden täglich begründet **volle Erwerbsminderung** (§ 43 Abs. 2 S. 2 SGB VI).
>
> **III. Antragsmodalitäten.** Der Antrag ist bei der DRV zu stellen (§ 99 SGB VI). Wird er innerhalb von drei Kalendermonaten nach Eintritt des Leistungsfalls eingereicht, wirkt er auf den Monatsanfang nach Leistungsfall zurück.
>
> **Ergebnis (🟡 mittleres Risiko wegen sozialmedizinischer Beurteilung):** Anspruch auf Rente wegen voller Erwerbsminderung dem Grunde nach gegeben …

## Risiken / typische Fehler

- **Wartezeit-Mythos:** "Ich habe doch 5 Jahre eingezahlt" — § 43 SGB VI verlangt **zusätzlich** die besonderen versicherungsrechtlichen Voraussetzungen (3 in 5).
- **Streckungstatbestände § 43 Abs. 4 SGB VI** übersehen: Anrechnungszeiten wegen Krankheit, Schwangerschaft, Kindererziehung können den 5-Jahres-Zeitraum verlängern.
- **Reha vor Rente:** Ein EM-Antrag wird gemäß § 116 Abs. 2 SGB VI in Reha-Antrag umgedeutet. Ablehnung der Reha = Verlust der EM-Chance.
- **Hinzuverdienstgrenze EM:** Anders als bei Altersrenten gilt weiterhin eine Grenze; Überschreitung kürzt die EM-Rente.
- **§ 240 SGB VI Berufsschutz:** Gilt nur für vor dem 02.01.1961 Geborene. Jüngere Versicherte haben keinen Berufsschutz mehr.
- **Antragsfrist § 99 SGB VI:** Nur 3 Monate Rückwirkung. Späterer Antrag = späterer Rentenbeginn.
- **Schwerbehinderung muss bei Rentenantragstellung festgestellt sein** (Bescheid Versorgungsamt) — bloßer Antrag genügt nicht für § 37 SGB VI.
