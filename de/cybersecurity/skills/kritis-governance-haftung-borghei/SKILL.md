---
name: kritis-governance-haftung-borghei
title: /kritis-resilienz:kritis-governance-haftung
description: Geschäftsleiterpflichten und Haftung nach dem KRITIS-Dachgesetz – Umsetzungs- und Überwachungspflicht der Geschäftsleitung § 20 Abs. 1 für die Resilienzmaßnahmen nach § 13 Abs. 1 einschließlich Sicherstellung durch geeignete Organisationsmaßnahmen, Innenhaftung gegenüber der eigenen Einrichtung § 20 Abs. 2 nach den gesellschaftsrechtlichen Regeln der jeweiligen Rechtsform mit subsidiärer Haftung nach dem Dachgesetz, Berichtspflichten § 21, Bußgeldkatalog § 24 mit Rahmen von 100.000 bis 1.000.000 EUR und der Zuständigkeitsverteilung zwischen BBK und Sektorbehörde, Ausnahmebescheid § 22 sowie das Zusammenspiel mit §§ 43 GmbHG, 93 AktG, § 130 OWiG und der Verbandsgeldbuße § 30 OWiG. Use when die Geschäftsleitung ihre KRITIS-Pflichten organisieren, dokumentieren oder ein Haftungs- und Bußgeldrisiko bewerten muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/kritis-resilienz/skills/kritis-governance-haftung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: cybersecurity
language: de
---

# /kritis-resilienz:kritis-governance-haftung

## Zweck

Der Skill übersetzt die KRITIS-Pflichten in Governance: Wer in der Geschäftsleitung schuldet was, wie wird es dokumentiert, und welches Haftungs- und Bußgeldrisiko entsteht bei Versäumnissen. Er hält dabei die drei Ebenen auseinander, die in der Praxis vermengt werden: **Innenhaftung** der Geschäftsleitung, **Bußgeld** gegen Person und Verband, und **Delegation**, die Überwachungspflichten nicht beseitigt.

## Eingaben

- Rechtsform der Einrichtung und Zusammensetzung der Geschäftsleitung; Ressortverteilung
- Vorhandene Geschäftsordnung, Ressortzuweisung, Delegationsdokumente
- Stand von Registrierung (§ 8), Risikoanalyse (§ 12) und Resilienzplan (§ 13)
- Berichtswege: wer berichtet der Geschäftsleitung wann, mit welcher Tiefe
- Behördliche Anordnungen, Auditverlangen, laufende Bußgeldverfahren
- D&O-Deckung und deren Ausschlüsse
- Ob eine Bereichsausnahme nach § 4 Abs. 2 greift — § 20 gehört zu den ausgenommenen Vorschriften

## Sub-Agent-Architektur

Der Researcher beschafft §§ 20, 21, 24 KRITISDachG, die gesellschaftsrechtlichen Haftungsnormen, §§ 30, 130 OWiG und die Verlautbarungen des BBK. Der Drafter entwirft Beschlussvorlage, Ressort- und Delegationsdokumentation sowie den Berichtsturnus. Der Reviewer prüft, ob die Überwachungspflicht trotz Delegation abgebildet ist, ob die Bereichsausnahme geprüft wurde und ob Bußgeldrahmen tatbestandsgenau zugeordnet sind.

## Ablauf

### 1. Anwendbarkeit prüfen

**§ 20 gehört zu den Vorschriften, die nach [§ 4 Abs. 2 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__4.html) für bestimmte Betreiber nicht gelten** — insbesondere für DORA-Finanzunternehmen und den Sektor Informationstechnik und Telekommunikation. Für diese Einrichtungen folgt die Geschäftsleiterverantwortung aus DORA bzw. dem BSIG und dem allgemeinen Gesellschaftsrecht. Die Prüfung steht am Anfang (`/kritis-resilienz:kritis-anwendungsbereich-registrierung`).

### 2. Umsetzungs- und Überwachungspflicht ([§ 20 Abs. 1 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__20.html))

Geschäftsleitungen von Betreibern kritischer Anlagen sind verpflichtet,

- die nach **§ 13 Abs. 1** zu ergreifenden **Resilienzmaßnahmen umzusetzen** **und**
- **ihre Umsetzung durch geeignete Organisationsmaßnahmen sicherzustellen**.

Die Norm enthält damit **zwei** Pflichten: eine Handlungs- und eine Überwachungspflicht. Delegation an eine Fachabteilung, einen Resilienzbeauftragten oder einen Dienstleister erfüllt die erste, **nicht** die zweite. Die Überwachungspflicht bleibt bei der Geschäftsleitung und verlangt:

| Element | Ausgestaltung |
|---|---|
| **Zuständigkeit** | ausdrückliche Ressortzuweisung in Geschäftsordnung oder Geschäftsverteilungsplan |
| **Ressourcen** | Budget und Personal, dokumentiert im Beschluss |
| **Berichtswesen** | fester Turnus, definierte Inhalte, Eskalationsschwellen |
| **Kontrolle** | Nachhalten von Maßnahmen, Audits, Fristen aus § 16 |
| **Dokumentation** | Beschlüsse, Vorlagen, Protokolle — die Beweislast im Haftungs- und Bußgeldverfahren liegt praktisch bei der Geschäftsleitung |

Bei mehrgliedriger Geschäftsleitung gilt der gesellschaftsrechtliche Grundsatz der **Gesamtverantwortung**: Ressortverteilung reduziert die Pflicht des nicht zuständigen Mitglieds auf Überwachung, beseitigt sie aber nicht.

### 3. Haftung ([§ 20 Abs. 2 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__20.html))

Geschäftsleitungen, die ihre Pflicht nach Abs. 1 verletzen, **haften ihrer Einrichtung** für einen **schuldhaft verursachten Schaden** nach den **auf die Rechtsform anwendbaren Regeln des Gesellschaftsrechts**. Nach dem Dachgesetz selbst haften sie **nur**, wenn die gesellschaftsrechtlichen Bestimmungen der Einrichtung **keine** Haftungsregelung enthalten.

Die Systematik ist damit:

1. **vorrangig** die gesellschaftsrechtliche Innenhaftung — [§ 43 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__43.html), [§ 93 AktG](https://www.gesetze-im-internet.de/aktg/__93.html), [§ 34 GenG](https://www.gesetze-im-internet.de/geng/__34.html), für kommunale Eigenbetriebe und Anstalten das jeweilige Landesrecht `[unverifiziert – prüfen]`;
2. **subsidiär** § 20 Abs. 2 KRITISDachG, wenn eine solche Regelung fehlt.

Es handelt sich um **Innenhaftung** gegenüber der eigenen Einrichtung — das Dachgesetz begründet **keinen** Außenhaftungsanspruch betroffener Dritter oder Kunden. Ansprüche Dritter richten sich nach allgemeinem Recht (Vertrag, § 823 BGB), und § 20 ist insoweit kein Schutzgesetz kraft ausdrücklicher Anordnung; die Einordnung ist im Einzelfall zu begründen und nicht zu unterstellen `[unverifiziert – prüfen]`.

**Verzicht und Vergleich** über Ersatzansprüche unterliegen den gesellschaftsrechtlichen Schranken (etwa § 93 Abs. 4 AktG). **D&O-Deckung** ist auf Ausschlüsse für Bußgelder und wissentliche Pflichtverletzung zu prüfen.

### 4. Berichtspflichten ([§ 21 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__21.html))

§ 21 begründet Berichtspflichten gegenüber den zuständigen Stellen; Abs. 6 gehört zu den nach § 4 Abs. 2 ausgenommenen Vorschriften. Inhalt und Turnus sind am geltenden Wortlaut und an der einschlägigen Rechtsverordnung abzulesen `[unverifiziert – prüfen]`. Für die Governance ist entscheidend, dass der Bericht **aus dem internen Berichtswesen gespeist** wird — ein Bericht, den die Geschäftsleitung nicht vorher gesehen hat, ist ein Governance-Mangel.

### 5. Bußgeld ([§ 24 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__24.html))

**Tatbestände (Abs. 1):**

| Nr. | Verstoß |
|---|---|
| 1 | Registrierungsangaben nach § 8 Abs. 1 nicht, nicht richtig, nicht vollständig, nicht in der vorgeschriebenen Weise oder nicht rechtzeitig übermittelt |
| 2 | Zuwiderhandlung gegen eine **vollziehbare Anordnung** — lit. a nach § 8 Abs. 2 S. 1, lit. b nach § 16 Abs. 2 S. 1 oder 2 oder Abs. 3 S. 3, auch iVm Abs. 5 S. 3, oder nach § 16 Abs. 5 S. 1 oder 2 |
| 3 | **Audit-Ergebnis** entgegen § 16 Abs. 3 S. 3 nicht, nicht richtig, nicht vollständig oder nicht rechtzeitig übermittelt |
| 4 | Betreten nicht gestattet, Unterlagen nicht vorgelegt oder Auskunft nicht erteilt (§ 16 Abs. 4 S. 3) |

**Rahmen (Abs. 2):**

| Fall | Höchstbetrag |
|---|---|
| Abs. 1 Nr. 2 lit. a | **1.000.000 EUR** |
| Abs. 1 Nr. 3 | **500.000 EUR** |
| Abs. 1 Nr. 2 lit. b | **200.000 EUR** |
| übrige Fälle | **100.000 EUR** |

**Zuständigkeit (Abs. 3):** In den Fällen des Abs. 1 Nr. 1 und Nr. 2 lit. a ist Verwaltungsbehörde iSd [§ 36 Abs. 1 Nr. 1 OWiG](https://www.gesetze-im-internet.de/owig_1968/__36.html) das **BBK**, im Übrigen die nach § 3 Abs. 2 S. 1 zuständige Behörde.

**Flankierend** treten hinzu: die **Aufsichtspflichtverletzung** nach [§ 130 OWiG](https://www.gesetze-im-internet.de/owig_1968/__130.html) und die **Verbandsgeldbuße** nach [§ 30 OWiG](https://www.gesetze-im-internet.de/owig_1968/__30.html) (`/wirtschafts-steuerstrafrecht:verbandsgeldbusse-30-130-owig` bzw. die einschlägige Skill dieses Plugins). Ein Organisationsversäumnis kann damit **zugleich** persönliche Innenhaftung, persönliches Bußgeld und Verbandsgeldbuße auslösen.

### 6. Entlastung organisieren

Was die Geschäftsleitung im Streitfall entlastet, ist die **dokumentierte** Befassung:

1. Beschluss über Zuständigkeit, Budget und Berichtsturnus;
2. Vorlage der Risikoanalyse nach § 12 und des Resilienzplans nach § 13 an die Geschäftsleitung;
3. protokollierte Entscheidung über **unterlassene** Maßnahmen mit Zweck-Mittel-Relation nach § 13 Abs. 2;
4. Nachhalten von Anordnungen und Fristen aus § 16;
5. Befassung mit jedem Vorfall nach § 18 und mit dem Monatsbericht;
6. jährliche Wirksamkeitskontrolle.

Der **Ausnahmebescheid** nach [§ 22 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__22.html) ist der einzige förmliche Weg, einzelne Pflichten abzubedingen; er ist zu beantragen, nicht anzunehmen.

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# Verjährung der Innenhaftung: § 43 Abs. 4 GmbHG / § 93 Abs. 6 AktG - Frist gesondert prüfen
python -m scripts.legal_calc.cli frist --ereignis 01.07.2026 --menge 5 --einheit jahre --land BY

# Verfolgungsverjährung der Ordnungswidrigkeit, § 31 OWiG - Rahmen tatbestandsbezogen prüfen
python -m scripts.legal_calc.cli frist --ereignis 01.07.2026 --menge 3 --einheit jahre --land BY

# Berichtsturnus der Geschäftsleitung
python -m scripts.legal_calc.cli frist --ereignis 01.07.2026 --menge 6 --einheit monate --land BY
```

Welche Verjährungsfrist gilt, hängt von Rechtsform und Tatbestand ab und ist gesondert zu belegen.

## Quellen

### Statute

- [§ 4 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__4.html), [§ 8](https://www.gesetze-im-internet.de/kritisdachg/__8.html), [§ 12](https://www.gesetze-im-internet.de/kritisdachg/__12.html), [§ 13 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__13.html), [§ 16 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__16.html), [§ 18](https://www.gesetze-im-internet.de/kritisdachg/__18.html), [§ 20](https://www.gesetze-im-internet.de/kritisdachg/__20.html), [§ 21](https://www.gesetze-im-internet.de/kritisdachg/__21.html), [§ 22](https://www.gesetze-im-internet.de/kritisdachg/__22.html), [§ 24 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__24.html)
- [§ 43 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__43.html), [§ 93 AktG](https://www.gesetze-im-internet.de/aktg/__93.html), [§ 34 GenG](https://www.gesetze-im-internet.de/geng/__34.html)
- [§ 30 OWiG](https://www.gesetze-im-internet.de/owig_1968/__30.html), [§ 31 OWiG](https://www.gesetze-im-internet.de/owig_1968/__31.html), [§ 36 OWiG](https://www.gesetze-im-internet.de/owig_1968/__36.html), [§ 130 OWiG](https://www.gesetze-im-internet.de/owig_1968/__130.html)
- [§ 823 BGB](https://www.gesetze-im-internet.de/bgb/__823.html)
- Richtlinie (EU) 2022/2557 — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2022/2557/oj); Verordnung (EU) 2022/2554 (DORA) — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
- Landesrecht für kommunale Eigenbetriebe und Anstalten `[unverifiziert – prüfen]`

### Kommentare und Literatur

- Kommentierungen zum KRITIS-Dachgesetz (Erscheinungsstand prüfen) `[unverifiziert – prüfen]`
- Baumbach/Hueck und Scholz, GmbHG, § 43; Hüffer/Koch, AktG, § 93.
- Krenzler/Herresthal u. a. zu §§ 30, 130 OWiG in der Compliance-Praxis.
- BBK, Handreichungen zur Geschäftsleiterverantwortung.

### Rechtsprechung

Zu § 20 KRITISDachG existiert **keine** Rechtsprechung. Für die Innenhaftung ist auf die gefestigte Judikatur zu § 43 GmbHG und § 93 AktG — einschließlich der Business Judgment Rule — zurückzugreifen, für Aufsichtspflichtverletzungen auf die Rechtsprechung zu § 130 OWiG. Jede konkrete Entscheidung ist vor Verwendung in juris oder Beck-Online zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
KRITIS-GOVERNANCE — <Einrichtung> — <Datum>

I.   Anwendbarkeit
     Bereichsausnahme § 4 Abs. 2 (§ 20 ausgenommen?): [ja — DORA/BSIG maßgeblich / nein]
     Rechtsform:              <GmbH / AG / eG / AöR / Eigenbetrieb>
     Maßgebliche Haftungsnorm: <§ 43 GmbHG / § 93 AktG / § 34 GenG / Landesrecht>

II.  Pflichtenlage § 20 Abs. 1
     Umsetzungspflicht:       <Stand der Maßnahmen nach § 13 Abs. 1>
     Überwachungspflicht:     <Organisationsmaßnahmen>
     Ressortzuweisung:        [dokumentiert / fehlt]
     Gesamtverantwortung:     <Pflicht der nicht zuständigen Mitglieder>
     Delegation:              [zulässig für Umsetzung — Überwachung bleibt]

III. Dokumentationslage
     Beschluss Zuständigkeit/Budget:   [vorhanden / fehlt]
     Vorlage § 12 / § 13:              [erfolgt am <Datum> / fehlt]
     Entscheidung über unterlassene Maßnahmen (§ 13 Abs. 2): [protokolliert / fehlt]
     Nachhalten § 16 / § 18:           [dokumentiert / fehlt]

IV.  Haftung § 20 Abs. 2
     Vorrangige Innenhaftung:  <Norm>
     Subsidiarität § 20 Abs. 2:[greift / greift nicht]
     Außenhaftung Dritter:     kein Anspruch aus § 20; allgemeines Recht
     D&O:                      <Deckung / Ausschlüsse>

V.   Bußgeldrisiko § 24
     Tatbestand:               <Abs. 1 Nr. …>
     Rahmen:                   <1.000.000 / 500.000 / 200.000 / 100.000 EUR>
     Behörde Abs. 3:           [BBK / Sektorbehörde § 3 Abs. 2 S. 1]
     § 130 OWiG / § 30 OWiG:   <Aufsichtspflicht / Verbandsgeldbuße>

VI.  Maßnahmenplan
     Sofort | 30 Tage | 90 Tage mit Verantwortlichkeit und Nachweis

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

## Risiken / typische Fehler

- **Delegation als Pflichterfüllung behandelt.** § 20 Abs. 1 KRITISDachG verlangt Umsetzung **und** Sicherstellung durch Organisationsmaßnahmen; die Überwachungspflicht bleibt bei der Geschäftsleitung.
- **Haftungsgrundlage falsch gewählt.** § 20 Abs. 2 greift **subsidiär**; vorrangig ist die gesellschaftsrechtliche Innenhaftung der jeweiligen Rechtsform.
- **Außenhaftung gegenüber Kunden aus § 20 abgeleitet.** Die Norm regelt Innenhaftung; Ansprüche Dritter folgen dem allgemeinen Recht.
- **Bereichsausnahme des § 4 Abs. 2 übersehen** — für DORA-Finanzunternehmen und IT/TK gilt § 20 nicht.
- **Ressortverteilung als Enthaftung verstanden.** Sie reduziert die Pflicht auf Überwachung, beseitigt sie nicht.
- **Unterlassene Maßnahmen nicht protokolliert.** Ohne dokumentierte Zweck-Mittel-Relation nach § 13 Abs. 2 fehlt die Entlastung.
- **Bußgeldrahmen pauschal mit 1 Mio. EUR angegeben.** § 24 Abs. 2 KRITISDachG staffelt tatbestandsbezogen: 1.000.000 / 500.000 / 200.000 / 100.000 EUR.
- **Zuständige Bußgeldbehörde nicht bestimmt** (§ 24 Abs. 3: BBK oder Sektorbehörde).
- **§§ 30, 130 OWiG ausgeblendet** — Verbandsgeldbuße und Aufsichtspflichtverletzung treten hinzu.
- **Rechtsprechung erfunden.** Zu § 20 KRITISDachG gibt es keine; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
