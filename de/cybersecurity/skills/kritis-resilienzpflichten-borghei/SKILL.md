---
name: kritis-resilienzpflichten-borghei
title: /kritis-resilienz:kritis-resilienzpflichten
description: Resilienzpflichten und Resilienzplan nach dem KRITIS-Dachgesetz – Risikoanalyse und Risikobewertung des Betreibers § 12 auf Grundlage der nationalen Risikoanalysen § 11, Resilienzpflichten § 13 mit den vier Zielen Verhinderung von Vorfällen, angemessener physischer Schutz von Liegenschaften und Anlagen, Reaktion und Begrenzung negativer Auswirkungen sowie zügige Wiederherstellung, Verhältnismäßigkeitsmaßstab und Stand der Technik § 13 Abs. 2, sektorenübergreifende und sektorspezifische Mindestanforderungen § 14, Vorrang von Durchführungsrechtsakten der Kommission § 15, Nachweise und behördliche Anordnungen einschließlich Audits § 16, Gleichwertigkeit von Nachweisen § 17, Unterstützung durch die Behörden § 19 und Ausnahmebescheid § 22. Use when ein Resilienzplan zu erstellen, ein Nachweis zu erbringen oder eine behördliche Anordnung abzuwehren ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/kritis-resilienz/skills/kritis-resilienzpflichten
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: cybersecurity
language: de
---

# /kritis-resilienz:kritis-resilienzpflichten

## Zweck

Der Skill erstellt und prüft die materielle Compliance unter dem KRITIS-Dachgesetz: Risikoanalyse, Resilienzplan, Maßnahmenauswahl und Nachweisführung. Sein Schwerpunkt liegt auf dem **All-Gefahren-Ansatz** — anders als NIS2 erfasst das Dachgesetz Sabotage, Naturgefahren, technisches Versagen, Zutritt und Personal — und auf dem **Verhältnismäßigkeitsmaßstab**, der die einzige echte Begrenzung der Pflichten darstellt.

## Eingaben

- Registrierte kritische Anlage(n) und die erbrachte kritische Dienstleistung
- Vorliegende nationale Risikoanalysen und Risikobewertungen nach § 11
- Eigene Risikoanalyse nach § 12: Stand, Methodik, Datum
- Bestehende Schutzkonzepte: Zutrittskontrolle, Perimeterschutz, Notstrom, Redundanzen, Notfall- und Wiederanlaufplanung, Personalsicherheit
- Bereits vorhandene Zertifizierungen und Audits (ISO 27001, ISO 22301, branchenspezifische Nachweise, B3S)
- Behördliche Anordnungen, Auditverlangen oder Fristsetzungen nach § 16
- Ob eine Bereichsausnahme nach § 4 Abs. 2 greift

## Sub-Agent-Architektur

Der Researcher beschafft KRITIS-DachG, die Verordnungen nach §§ 11, 14, die RL (EU) 2022/2557, etwaige Durchführungsrechtsakte der Kommission und die Verlautbarungen des BBK. Der Drafter strukturiert Risikoanalyse und Resilienzplan entlang der vier Ziele des § 13 Abs. 1 und formuliert die Verhältnismäßigkeitsbegründung. Der Reviewer prüft, ob jede Maßnahme einem Ziel zugeordnet ist, ob die Zweck-Mittel-Relation belegt ist und ob Nachweise nach § 17 gleichwertig angerechnet werden können.

## Ablauf

### 1. Anwendbarkeit der Pflichten klären

Die §§ 12 bis 16 gehören zu den Vorschriften, die nach [§ 4 Abs. 2 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__4.html) für bestimmte Betreiber **nicht** gelten — insbesondere für DORA-Finanzunternehmen und für den Sektor Informationstechnik und Telekommunikation; im Sektor Siedlungsabfallentsorgung bleibt **§ 12 anwendbar**. Die Prüfung erfolgt vor jeder inhaltlichen Arbeit (`/kritis-resilienz:kritis-anwendungsbereich-registrierung`).

### 2. Risikoanalyse des Betreibers ([§ 12 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__12.html))

Der Betreiber führt eine eigene **Risikoanalyse und Risikobewertung** durch. Sie baut auf den **nationalen Risikoanalysen und Risikobewertungen** nach [§ 11 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__11.html) auf, die das Bundesministerium des Innern mit dem BBK erstellt.

Inhaltlich zu erfassen sind alle Gefahrenarten des All-Gefahren-Ansatzes:

| Gefahrenkategorie | Beispiele |
|---|---|
| **Vorsätzliche Handlungen** | Sabotage, Anschlag, Einbruch, Insider-Täter, Drohnenüberflug |
| **Naturgefahren** | Hochwasser, Sturm, Hitze, Starkregen, Erdbeben |
| **Technisches und menschliches Versagen** | Ausfall von Anlagenteilen, Bedienfehler, Wartungsversäumnis |
| **Abhängigkeiten** | Strom, Wasser, Telekommunikation, Lieferanten, Personal |
| **Kaskadeneffekte** | Ausfallfolgen für andere kritische Dienstleistungen |

Die Analyse ist zu dokumentieren und fortzuschreiben; sie ist zugleich die Begründungsgrundlage für die Verhältnismäßigkeit der gewählten Maßnahmen.

### 3. Resilienzpflichten und Resilienzplan ([§ 13 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__13.html))

Nach § 13 Abs. 1 hat der Betreiber Maßnahmen zu treffen, um

1. **das Auftreten von Vorfällen zu verhindern**,
2. einen **angemessenen physischen Schutz** von Liegenschaften und kritischen Anlagen zu gewährleisten,
3. **auf Vorfälle zu reagieren, sie abzuwehren und die negativen Auswirkungen zu begrenzen**, und
4. nach Vorfällen die **zügige Wiederherstellung** der kritischen Dienstleistung zu gewährleisten.

**Jede Maßnahme des Resilienzplans wird genau einem dieser vier Ziele zugeordnet.** Ein Plan, der Maßnahmen nur aufzählt, ist gegenüber der Behörde nicht verteidigungsfähig.

**Maßstab (§ 13 Abs. 2):** Auf Grundlage der nationalen Analysen **und** der eigenen Analyse nach § 12 sind **verhältnismäßige technische, sicherheitsbezogene und organisatorische Maßnahmen** zu treffen. Der **Stand der Technik soll eingehalten werden**. Es ist ein **Verhältnismäßigkeitsmaßstab** anzulegen und eine **Zweck-Mittel-Relation** zu bilden, bei der insbesondere der Aufwand zur Verhinderung oder Begrenzung ins Verhältnis zu setzen ist.

Praktisch heißt das: Der Plan dokumentiert je Maßnahme **Risiko → Ziel nach Abs. 1 → Maßnahme → Aufwand → Restrisiko**. Wo eine an sich mögliche Maßnahme unterbleibt, wird die Zweck-Mittel-Relation ausdrücklich begründet — das ist die einzige belastbare Verteidigung gegen eine spätere Anordnung.

### 4. Mindestanforderungen und Unionsrecht ([§ 14 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__14.html), [§ 15 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__15.html))

- **§ 14** — sektorenübergreifende und sektorspezifische **Mindestanforderungen**, näher bestimmt durch Rechtsverordnung; sie sind der Boden, nicht die Decke der Pflichten `[unverifiziert – prüfen]` hinsichtlich der geltenden Fassung.
- **§ 15** — **Vorrang von Durchführungsrechtsakten der Europäischen Kommission**. Erlässt die Kommission zu einem Bereich einen Durchführungsrechtsakt, geht dieser vor. Vor jeder Maßnahmenplanung ist zu prüfen, ob ein solcher Rechtsakt existiert.

### 5. Nachweise, Audits und Anordnungen ([§ 16 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__16.html), [§ 17 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__17.html))

**§ 16** regelt die Nachweisführung und die behördlichen Anordnungen. Praxisrelevant sind:

- die Pflicht, die Erfüllung der Resilienzpflichten auf Verlangen **nachzuweisen**;
- **Anordnungen** der zuständigen Behörde nach Abs. 2 und Abs. 3 sowie Abs. 5 — sie sind vollziehbar und nach § 24 Abs. 1 Nr. 2 bußgeldbewehrt;
- **Audits**: Das **Ergebnis eines Audits** ist nach Abs. 3 S. 3 zu übermitteln; die unterlassene, unrichtige, unvollständige oder verspätete Übermittlung ist nach § 24 Abs. 1 Nr. 3 mit bis zu **500.000 EUR** bewehrt;
- **Betretens- und Auskunftsrechte** nach Abs. 4 S. 3, deren Verweigerung nach § 24 Abs. 1 Nr. 4 bewehrt ist.

**§ 17 — Gleichwertigkeit von Nachweisen.** Bereits vorhandene Nachweise und sonstige öffentlich-rechtliche Anforderungen können als gleichwertig anerkannt werden. Das ist der Hebel, um bestehende Zertifizierungen und branchenspezifische Sicherheitsstandards nicht doppelt zu erarbeiten — die Gleichwertigkeit ist jedoch **darzulegen**, nicht zu behaupten, und deckt regelmäßig nur einen Teil der vier Ziele des § 13 Abs. 1 ab. Insbesondere decken cybersicherheitsbezogene Zertifizierungen den **physischen** Schutz nach Abs. 1 Nr. 2 typischerweise **nicht** ab.

Flankierend: **[§ 6](https://www.gesetze-im-internet.de/kritisdachg/__6.html)** (sonstige Resilienzregelungen und Resilienzmaßnahmen) und **[§ 19](https://www.gesetze-im-internet.de/kritisdachg/__19.html)** (Unterstützung der Betreiber, freiwillige Angebote).

### 6. Rechtsschutz

Anordnungen nach § 16 sind Verwaltungsakte. Es gelten Anhörung nach [§ 28 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__28.html), Begründung nach [§ 39 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__39.html), Widerspruch und Anfechtungsklage nach [§§ 68 ff.](https://www.gesetze-im-internet.de/vwgo/__68.html), [§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html) — soweit das Vorverfahren landesrechtlich noch vorgesehen ist `[unverifiziert – prüfen]` — sowie bei Sofortvollzug der Antrag nach [§ 80 Abs. 5 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html). Der **Ausnahmebescheid** nach [§ 22](https://www.gesetze-im-internet.de/kritisdachg/__22.html) ist der förmliche Weg, einzelne Pflichten abzubedingen.

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik; Risikobewertung und Zweck-Mittel-Relation bleiben juristische und fachliche Eingaben:

```bash
# Behördliche Fristsetzung zur Nachweisvorlage nach § 16
python -m scripts.legal_calc.cli frist --ereignis 02.06.2026 --menge 6 --einheit wochen --land BY

# Widerspruchsfrist § 70 VwGO gegen eine Anordnung nach § 16
python -m scripts.legal_calc.cli frist --ereignis 02.06.2026 --menge 1 --einheit monate --land BY

# Turnus der Fortschreibung von Risikoanalyse und Resilienzplan
python -m scripts.legal_calc.cli frist --ereignis 01.09.2026 --menge 2 --einheit jahre --land BY
```

## Quellen

### Statute

- [§ 4 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__4.html), [§ 6](https://www.gesetze-im-internet.de/kritisdachg/__6.html), [§ 11](https://www.gesetze-im-internet.de/kritisdachg/__11.html), [§ 12](https://www.gesetze-im-internet.de/kritisdachg/__12.html), [§ 13](https://www.gesetze-im-internet.de/kritisdachg/__13.html), [§ 14](https://www.gesetze-im-internet.de/kritisdachg/__14.html), [§ 15](https://www.gesetze-im-internet.de/kritisdachg/__15.html), [§ 16](https://www.gesetze-im-internet.de/kritisdachg/__16.html), [§ 17](https://www.gesetze-im-internet.de/kritisdachg/__17.html), [§ 19](https://www.gesetze-im-internet.de/kritisdachg/__19.html), [§ 22](https://www.gesetze-im-internet.de/kritisdachg/__22.html), [§ 24 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__24.html)
- Richtlinie (EU) 2022/2557, insbesondere Art. 12 bis 14 — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2022/2557/oj)
- [§ 28 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__28.html), [§ 39 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__39.html), [§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html), [§ 68 VwGO](https://www.gesetze-im-internet.de/vwgo/__68.html), [§ 70 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html), [§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html)
- Rechtsverordnungen nach §§ 11, 14 KRITISDachG `[unverifiziert – prüfen]`

### Kommentare und Literatur

- Kommentierungen zum KRITIS-Dachgesetz (Erscheinungsstand prüfen) `[unverifiziert – prüfen]`
- Gitter/Kipker, IT-Sicherheitsrecht (Abgrenzung physische Resilienz / Cybersicherheit).
- BBK, Handreichungen und FAQ zur Umsetzung des KRITIS-Dachgesetzes.
- Branchenspezifische Sicherheitsstandards (B3S) als möglicher Gleichwertigkeitsnachweis nach § 17.

### Rechtsprechung

Zum KRITIS-Dachgesetz liegt **keine** Rechtsprechung vor. Für Anordnungen, Verhältnismäßigkeit und Sofortvollzug ist auf die allgemeine verwaltungsgerichtliche Judikatur zurückzugreifen; jede Entscheidung ist vor Verwendung in juris oder Beck-Online zu verifizieren `[unverifiziert – prüfen]`.

## Ausgabeformat

```
KRITIS-RESILIENZ — <Betreiber / Anlage> — <Datum>

I.   Anwendbarkeit
     Bereichsausnahme § 4 Abs. 2: [greift für §§ … / greift nicht]
     Durchführungsrechtsakt § 15: [vorhanden — geht vor / keiner]

II.  Risikoanalyse § 12
     Nationale Analysen § 11 herangezogen: [ja / nein]
     Gefahrenkategorien:      vorsätzlich | Naturgefahren | Versagen | Abhängigkeiten | Kaskaden
     Stand / Datum:           <…>   Fortschreibung: <Turnus>

III. Resilienzplan § 13
     Ziel Abs. 1 Nr. 1 Verhinderung:      <Maßnahmen>
     Ziel Abs. 1 Nr. 2 physischer Schutz: <Maßnahmen>
     Ziel Abs. 1 Nr. 3 Reaktion/Begrenzung: <Maßnahmen>
     Ziel Abs. 1 Nr. 4 Wiederherstellung: <Maßnahmen>
     Je Maßnahme: Risiko → Ziel → Maßnahme → Aufwand → Restrisiko
     Stand der Technik Abs. 2:            [eingehalten / begründet abgewichen]
     Zweck-Mittel-Relation:               <Begründung, auch für unterlassene Maßnahmen>

IV.  Mindestanforderungen § 14
     Sektorenübergreifend:    <erfüllt / Lücke>
     Sektorspezifisch:        <erfüllt / Lücke>

V.   Nachweise §§ 16, 17
     Nachweisverlangen:       <Datum, Frist bis <Datum>>
     Audit-Ergebnis übermittelt (§ 16 Abs. 3 S. 3): [ja / offen — 500.000 EUR Risiko]
     Gleichwertigkeit § 17:   <ISO 27001 / ISO 22301 / B3S — welche Ziele gedeckt?>
     Nicht gedeckt:           <regelmäßig der physische Schutz nach Abs. 1 Nr. 2>

VI.  Behördliche Anordnungen und Rechtsschutz
     Anordnung nach § 16 Abs. <…> vom <Datum>
     Anhörung § 28 VwVfG:     [erfolgt / unterblieben]
     Rechtsbehelf:            Frist bis <Datum>; Sofortvollzug: [angeordnet / nein]
     Ausnahmebescheid § 22:   [beantragt / nicht einschlägig]

VII. Bußgeldrisiko § 24
     Nr. 2 lit. a Anordnung:  bis 1.000.000 EUR
     Nr. 3 Audit-Ergebnis:    bis 500.000 EUR
     Nr. 2 lit. b:            bis 200.000 EUR
     übrige:                  bis 100.000 EUR

VIII.Risiko: 🟢 / 🟡 / 🔴 <Begründung>
IX.  Quellenverzeichnis
```

## Risiken / typische Fehler

- **Cyber-Zertifizierung als Resilienznachweis vorgelegt.** ISO 27001 und vergleichbare Nachweise decken den **physischen** Schutz nach § 13 Abs. 1 Nr. 2 regelmäßig nicht ab; § 17 verlangt die Darlegung der Gleichwertigkeit.
- **Maßnahmen ohne Zuordnung zu den vier Zielen des § 13 Abs. 1 aufgelistet.**
- **Verhältnismäßigkeit behauptet statt gerechnet.** § 13 Abs. 2 verlangt eine ausdrückliche Zweck-Mittel-Relation, insbesondere für **unterlassene** Maßnahmen.
- **Nationale Risikoanalysen nach § 11 nicht herangezogen** — sie sind Grundlage der eigenen Analyse nach § 12.
- **Durchführungsrechtsakte der Kommission übersehen.** § 15 ordnet ihren Vorrang an.
- **Audit-Ergebnis nicht übermittelt.** § 16 Abs. 3 S. 3 verlangt es; § 24 Abs. 1 Nr. 3 bewehrt den Verstoß mit bis zu 500.000 EUR.
- **Bereichsausnahme des § 4 Abs. 2 nicht geprüft**, bevor ein vollständiger Resilienzplan erarbeitet wird.
- **All-Gefahren-Ansatz auf Sabotage verengt.** Naturgefahren, technisches Versagen, Abhängigkeiten und Kaskadeneffekte gehören dazu.
- **Rechtsprechung erfunden.** Zum KRITIS-DachG gibt es keine; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
