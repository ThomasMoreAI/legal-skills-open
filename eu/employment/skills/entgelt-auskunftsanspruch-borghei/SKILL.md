---
name: entgelt-auskunftsanspruch-borghei
title: /entgelttransparenz-eu:entgelt-auskunftsanspruch
description: Auskunfts- und Transparenzrechte im Entgeltgefüge – Entgelttransparenz vor der Beschäftigung nach Art. 5 RL (EU) 2023/970 mit Anspruch auf Einstiegsentgelt oder Entgeltspanne, Verbot der Frage nach der bisherigen Entgeltentwicklung und geschlechtsneutralen Stellenausschreibungen, Auskunftsrecht der Beschäftigten nach Art. 7 auf individuelle und durchschnittliche Entgelthöhen aufgeschlüsselt nach Geschlecht und Vergleichsgruppe, Antwortfrist von zwei Monaten Art. 7 Abs. 4, jährliche Hinweispflicht Art. 7 Abs. 3, Unwirksamkeit von Entgeltverschwiegenheitsklauseln Art. 7 Abs. 5, Zugänglichkeit der Kriterien Art. 6 und Art. 8, Datenschutz Art. 12 sowie das geltende Auskunftsverfahren der §§ 10 bis 16 EntgTranspG mit der 200-Beschäftigten-Schwelle und der Sechs-Personen-Vergleichsgruppe. Use when ein Auskunftsverlangen zu beantworten, eine Stellenausschreibung zu prüfen oder eine Verschwiegenheitsklausel zu bewerten ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/entgelttransparenz-eu/skills/entgelt-auskunftsanspruch
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: employment
language: de
---

# /entgelttransparenz-eu:entgelt-auskunftsanspruch

## Zweck

Der Skill bearbeitet die Transparenzrechte im laufenden und im anzubahnenden Arbeitsverhältnis. Er trennt dabei durchgehend, was das **geltende EntgTranspG** heute schon gewährt, und was die **Richtlinie** verlangt — und legt bei der Beantwortung eines Auskunftsverlangens die für den Mandanten belastbare Linie fest.

## Eingaben

- Auskunftsverlangen im Wortlaut mit Eingangsdatum; Absender und dessen Funktion
- Arbeitgeber: Beschäftigtenzahl, Trägerschaft, Tarifbindung
- Entgeltsystem: Entgeltgruppen, Kriterien, variable Bestandteile, Zulagen
- Vergleichsgruppe: Tätigkeit, Zusammensetzung, Anzahl der Personen je Geschlecht
- Bestehende Verschwiegenheitsklauseln in Arbeitsverträgen oder Betriebsvereinbarungen
- Stellenausschreibungen und der Ablauf des Einstellungsverfahrens
- Ob ein Betriebsrat besteht und ob er eingebunden wurde

## Sub-Agent-Architektur

Der Researcher beschafft die RL (EU) 2023/970, das EntgTranspG, das BetrVG und den Umsetzungsstand. Der Drafter formuliert die Antwort auf das Auskunftsverlangen oder das Verlangen selbst und prüft Ausschreibung und Klauseln. Der Reviewer kontrolliert die Zweimonatsfrist, die Vollständigkeit der Auskunft und ob geltendes Recht und Richtlinienziel sauber getrennt sind.

## Ablauf

### 1. Rechtsgrundlage bestimmen

| Anliegen | Heute geltend | Richtlinie |
|---|---|---|
| Auskunft über Vergleichsentgelt | [§§ 10 ff. EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__10.html) — Betriebe mit **in der Regel mehr als 200 Beschäftigten** | **Art. 7** — ohne Schwellenwert |
| Entgeltangabe in der Stellenausschreibung | keine allgemeine Pflicht | **Art. 5 Abs. 1** |
| Frage nach bisherigem Gehalt | zulässigkeitsstreitig | **Art. 5 Abs. 2** — ausdrückliches Verbot |
| Verschwiegenheit über das eigene Entgelt | AGB- und AGG-Kontrolle | **Art. 7 Abs. 5** |

Bei **staatlichen** Arbeitgebern kann sich die Beschäftigte nach Ablauf der Umsetzungsfrist auf hinreichend genaue und unbedingte Richtlinienbestimmungen unmittelbar berufen (`/entgelttransparenz-eu:entgelttransparenz-umsetzungsstand`).

### 2. Vorvertragliche Transparenz (Art. 5 RL (EU) 2023/970)

- **Abs. 1** — Stellenbewerber haben Anspruch auf Information über **a)** das auf objektiven, geschlechtsneutralen Kriterien beruhende **Einstiegsentgelt oder dessen Spanne** und **b)** gegebenenfalls die einschlägigen Bestimmungen des angewandten **Tarifvertrags**. Die Information ist so bereitzustellen, dass **fundierte und transparente Entgeltverhandlungen** gewährleistet sind — etwa in der veröffentlichten Stellenausschreibung, vor dem Vorstellungsgespräch oder auf andere Weise.
- **Abs. 2** — Der Arbeitgeber **darf Bewerber nicht nach ihrer Entgeltentwicklung in laufenden oder früheren Beschäftigungsverhältnissen befragen.** Das ist ein klares, unbedingtes Verbot — der stärkste Kandidat für unmittelbare Wirkung gegenüber staatlichen Arbeitgebern.
- **Abs. 3** — **Stellenausschreibungen und Berufsbezeichnungen müssen geschlechtsneutral** sein; Einstellungsverfahren sind nichtdiskriminierend zu führen.

Praktisch heißt das für die Umstellung: Entgeltspannen definieren und begründen, Fragebögen und Bewerbungsformulare um die Gehaltshistorie bereinigen, Ausschreibungstexte und Berufsbezeichnungen prüfen, Interviewleitfäden anpassen.

### 3. Auskunftsrecht der Beschäftigten (Art. 7 RL (EU) 2023/970)

- **Abs. 1** — Anspruch auf Auskunft über die **individuelle Entgelthöhe** und die **durchschnittlichen Entgelthöhen**, **aufgeschlüsselt nach Geschlecht** und für die **Gruppen von Arbeitnehmern, die gleiche oder gleichwertige Arbeit verrichten**, **in schriftlicher Form**.
- **Abs. 2** — Das Verlangen kann über **Arbeitnehmervertreter** oder über eine **Gleichbehandlungsstelle** gestellt werden. Sind die Informationen unzutreffend oder unvollständig, besteht Anspruch auf **zusätzliche und angemessene Klarstellungen** und eine **begründete Antwort**.
- **Abs. 3** — Der Arbeitgeber **informiert alle Arbeitnehmer jährlich** über dieses Recht und über die Schritte zu seiner Wahrnehmung. Das ist eine **Bringschuld**, keine Antwortpflicht auf Nachfrage.
- **Abs. 4** — Die Auskunft ist **innerhalb einer angemessenen Frist, jedenfalls innerhalb von zwei Monaten** ab Antragstellung zu erteilen.
- **Abs. 5** — Arbeitnehmer **dürfen nicht daran gehindert werden, ihr Entgelt offenzulegen**, um den Grundsatz des gleichen Entgelts durchzusetzen. Entgeltverschwiegenheitsklauseln sind insoweit unwirksam.

Flankierend: **Art. 6** — Transparenz bei der Festlegung des Entgelts und der Politik der Entgeltentwicklung; die Kriterien müssen **objektiv und geschlechtsneutral** und den Beschäftigten **leicht zugänglich** sein. **Art. 8** — Zugänglichkeit der Informationen, auch für Menschen mit Behinderungen. **Art. 12** — Datenschutz: personenbezogene Daten dürfen nur zum Zweck des gleichen Entgelts verwendet werden.

### 4. Das geltende deutsche Verfahren (§§ 10 ff. EntgTranspG)

Solange kein Umsetzungsgesetz gilt, ist das Auskunftsverlangen nach dem **EntgTranspG** zu bearbeiten:

| Element | Regelung |
|---|---|
| Anwendungsbereich | Betriebe mit **in der Regel mehr als 200 Beschäftigten** bei demselben Arbeitgeber ([§ 12 Abs. 1 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__12.html)) |
| Gegenstand | Kriterien und Verfahren der Entgeltfindung sowie das **Vergleichsentgelt** einer gleichen oder gleichwertigen Tätigkeit |
| Vergleichsgruppe | Auskunft nur, wenn die Vergleichstätigkeit von **mindestens sechs Beschäftigten des jeweils anderen Geschlechts** ausgeübt wird |
| Angabe | statistischer **Median** des durchschnittlichen monatlichen Bruttoentgelts, hochgerechnet auf Vollzeitäquivalente |
| Weg | in tarifgebundenen Betrieben grundsätzlich über den **Betriebsrat** ([§ 14](https://www.gesetze-im-internet.de/entgtranspg/__14.html)), sonst über den Arbeitgeber ([§ 15 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__15.html)) |
| Frist | Antwort binnen **drei Monaten** ([§ 15 Abs. 3 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__15.html)) |
| Turnus | Wiederholung grundsätzlich alle **zwei Jahre** ([§ 10 Abs. 2 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__10.html)) |

Die konkreten Schwellen, Fristen und die Rolle des Betriebsrats sind am geltenden Wortlaut zu prüfen und mit Fassungsstand zu zitieren `[unverifiziert – prüfen]`.

**Die Richtlinie verschärft an drei Stellen:** kein Schwellenwert, **zwei** statt drei Monate, und eine **jährliche Hinweispflicht** — bei staatlichen Arbeitgebern schon heute relevant.

### 5. Antwort auf ein Auskunftsverlangen entwerfen

Eine belastbare Antwort enthält:

1. **Empfangsbestätigung** mit Fristnotiz;
2. **Prüfung der Vergleichsgruppe** — Tätigkeit, Gleichwertigkeit nach objektiven Kriterien, Zahl der Vergleichspersonen;
3. **Angabe** des Vergleichsentgelts in der geschuldeten Form (Median bzw. Durchschnitt nach Geschlecht);
4. **Kriterien und Verfahren** der Entgeltfindung;
5. **Datenschutzhinweis** — keine Offenlegung individueller Entgelte identifizierbarer Personen;
6. **Hinweis** auf das Recht, Klarstellungen zu verlangen.

Bei zu kleiner Vergleichsgruppe ist **transparent zu begründen**, warum keine Angabe erfolgt — und zu prüfen, ob nach der Richtlinie eine andere Gruppenbildung geboten wäre.

### 6. Betriebsverfassungsrechtliche Flankierung

Der Betriebsrat hat nach [§ 80 Abs. 1 Nr. 2a, Abs. 2 BetrVG](https://www.gesetze-im-internet.de/betrvg/__80.html) Überwachungs- und Informationsrechte zur Entgeltgleichheit; [§ 13 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__13.html) weist ihm im Auskunftsverfahren eine eigene Rolle zu. Das Einsichtsrecht in Bruttoentgeltlisten nach [§ 80 Abs. 2 S. 2 BetrVG](https://www.gesetze-im-internet.de/betrvg/__80.html) ist gesondert zu prüfen. Art. 13 der Richtlinie stärkt den sozialen Dialog zusätzlich.

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# Art. 7 Abs. 4 RL (EU) 2023/970: 2 Monate ab Antrag vom 15.07.2026
python -m scripts.legal_calc.cli frist --ereignis 15.07.2026 --menge 2 --einheit monate --land BY

# § 15 Abs. 3 EntgTranspG: 3 Monate ab Zugang des Verlangens
python -m scripts.legal_calc.cli frist --ereignis 15.07.2026 --menge 3 --einheit monate --land BY

# § 10 Abs. 2 EntgTranspG: Wiederholung des Verlangens nach zwei Jahren
python -m scripts.legal_calc.cli frist --ereignis 15.07.2026 --menge 2 --einheit jahre --land BY
```

Ob Tätigkeiten „gleichwertig" sind, ist eine Wertung nach objektiven, geschlechtsneutralen Kriterien und gesondert zu begründen.

## Quellen

### Rechtsakte

- Richtlinie (EU) 2023/970, Art. 4, 5, 6, 7, 8, 12, 13 — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2023/970/oj)
- [EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/) – [§ 3](https://www.gesetze-im-internet.de/entgtranspg/__3.html), [§ 4](https://www.gesetze-im-internet.de/entgtranspg/__4.html), [§ 10 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__10.html), [§ 11](https://www.gesetze-im-internet.de/entgtranspg/__11.html), [§ 12 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__12.html), [§ 13](https://www.gesetze-im-internet.de/entgtranspg/__13.html), [§ 14](https://www.gesetze-im-internet.de/entgtranspg/__14.html), [§ 15](https://www.gesetze-im-internet.de/entgtranspg/__15.html), [§ 16 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__16.html)
- Art. 157 AEUV — [EUR-Lex](https://eur-lex.europa.eu/eli/treaty/tfeu_2012/oj)
- [§ 80 BetrVG](https://www.gesetze-im-internet.de/betrvg/__80.html); [AGG](https://www.gesetze-im-internet.de/agg/)
- Verordnung (EU) 2016/679 (DSGVO), Art. 5, 6 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

### Kommentare und Literatur

- ErfK und HWK zum EntgTranspG und zu Art. 157 AEUV.
- Fitting und GK-BetrVG zu § 80 BetrVG (Einsicht in Bruttoentgeltlisten).
- Beiträge zum Auskunftsanspruch nach der RL (EU) 2023/970 in NZA und RdA 2024–2026 (Fundstelle prüfen) `[unverifiziert – prüfen]`

### Rechtsprechung

Zum Auskunftsanspruch nach dem EntgTranspG und zur Darlegungslast bei Entgeltgleichheit besteht Rechtsprechung des **BAG**; zur RL (EU) 2023/970 liegt noch keine Judikatur vor. Jede konkrete Entscheidung ist vor Verwendung in juris, Beck-Online oder auf bundesarbeitsgericht.de zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
ENTGELT-AUSKUNFT — <Mandat> — <Datum>

I.   Rechtsgrundlage
     Umsetzungsgesetz verkündet:  [nein — EntgTranspG + Richtlinienwirkung / ja am <Datum>]
     Arbeitgeber:                 [privat / staatlich]
     Anwendbar:                   [§§ 10 ff. EntgTranspG / Art. 7 unmittelbar / beides]

II.  Verlangen
     Eingang:                 <Datum>   Antragsteller: <…>
     Weg:                     [Betriebsrat § 14 / Arbeitgeber § 15 / Arbeitnehmervertreter Art. 7 Abs. 2]
     Frist:                   [2 Monate Art. 7 Abs. 4 bis <Datum> / 3 Monate § 15 Abs. 3 bis <Datum>]

III. Vergleichsgruppe
     Tätigkeit:               <…>
     Gleichwertigkeit (objektive, geschlechtsneutrale Kriterien): <Begründung>
     Personenzahl je Geschlecht: <…>   Schwelle sechs (EntgTranspG): [erreicht / nicht erreicht]
     Folge bei Unterschreitung: <transparente Begründung; Prüfung anderer Gruppenbildung>

IV.  Auskunftsinhalt
     Individuelle Entgelthöhe:    <…>
     Durchschnitt nach Geschlecht / Median: <…>
     Kriterien und Verfahren:     <…>
     Datenschutz Art. 12 / DSGVO: <keine identifizierbaren Einzelentgelte>

V.   Vorvertragliche Transparenz Art. 5
     Entgeltangabe in Ausschreibung: [vorhanden / fehlt]
     Frage nach Gehaltshistorie:     [gestellt — unzulässig nach Abs. 2 / unterlassen]
     Geschlechtsneutralität Abs. 3:  [geprüft]

VI.  Verschwiegenheitsklausel
     Wortlaut:                <…>
     Bewertung Art. 7 Abs. 5: [unwirksam, soweit sie die Durchsetzung hindert]
     Handlungsbedarf:         <Vertragsanpassung>

VII. Jährliche Hinweispflicht Art. 7 Abs. 3
     Umgesetzt:               [ja / nein — Bringschuld]

VIII.Betriebsrat
     § 13 EntgTranspG / § 80 BetrVG: <Einbindung>

IX.  Risiko: 🟢 / 🟡 / 🔴 <Begründung>
X.   Quellenverzeichnis
```

## Risiken / typische Fehler

- **Zwei- und Dreimonatsfrist verwechselt.** Art. 7 Abs. 4 RL gibt **zwei** Monate, § 15 Abs. 3 EntgTranspG **drei**; welche gilt, hängt von der Rechtsgrundlage ab.
- **Schwellenwert der Richtlinie unterstellt.** Art. 7 kennt **keine** 200-Beschäftigten-Schwelle — diese steht im EntgTranspG.
- **Individuelle Entgelte offengelegt.** Geschuldet sind Durchschnitts- bzw. Medianwerte; identifizierbare Einzelentgelte verletzen Art. 12 RL und die DSGVO.
- **Frage nach der Gehaltshistorie beibehalten.** Art. 5 Abs. 2 RL verbietet sie ausdrücklich.
- **Verschwiegenheitsklausel unverändert gelassen.** Art. 7 Abs. 5 RL nimmt ihr die Wirkung, soweit sie die Durchsetzung des gleichen Entgelts hindert.
- **Jährliche Hinweispflicht als Antwortpflicht missverstanden.** Art. 7 Abs. 3 RL begründet eine **Bringschuld**.
- **Vergleichsgruppe nach Stellenbezeichnung statt nach Gleichwertigkeit gebildet.** Maßstab sind Kompetenzen, Belastungen, Verantwortung und Arbeitsbedingungen (Art. 4 RL).
- **Betriebsrat übergangen**, obwohl § 14 EntgTranspG bzw. § 80 BetrVG ihn einbindet.
- **Auskunft ohne Begründung verweigert**, wenn die Vergleichsgruppe zu klein ist.
- **Rechtsprechung erfunden.** Jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
