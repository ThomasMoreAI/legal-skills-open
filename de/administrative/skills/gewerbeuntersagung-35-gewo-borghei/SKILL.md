---
name: gewerbeuntersagung-35-gewo-borghei
title: /gewerberecht:gewerbeuntersagung-35-gewo
description: Gewerbeuntersagung wegen Unzuverlässigkeit nach § 35 GewO – gebundene Entscheidung bei Unzuverlässigkeit und Erforderlichkeit Abs. 1 S. 1, erweiterte Untersagung auf andere Gewerbe und Leitungstätigkeiten Abs. 1 S. 2, Fortsetzung des Verfahrens trotz Betriebsaufgabe Abs. 1 S. 3, Gestattung durch Stellvertreter Abs. 2, Bindung an strafgerichtliche Feststellungen Abs. 3, Anhörung von IHK und Handwerkskammer Abs. 4, Wiedergestattung Abs. 6 mit Jahressperre, Zuständigkeit Abs. 7, Untersagung gegen Vertretungsberechtigte Abs. 7a, Sperrwirkung spezialgesetzlicher Untersagungsvorschriften Abs. 8 sowie Anhörung § 28 VwVfG, Sofortvollzug § 80 Abs. 2 S. 1 Nr. 4 VwGO und Rechtsschutz nach der VwGO. Use when eine Gewerbeuntersagung droht, angehört wird oder bereits ergangen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/gewerberecht/skills/gewerbeuntersagung-35-gewo
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /gewerberecht:gewerbeuntersagung-35-gewo

## Zweck

Der Skill führt ein Untersagungsverfahren nach § 35 GewO von der Anhörung bis zum Eilrechtsschutz. Er prüft die Unzuverlässigkeit anhand der in der Praxis maßgeblichen Fallgruppen, kontrolliert die Erforderlichkeit und die Reichweite der Untersagung und benennt den einzigen wirksamen Verteidigungsansatz in der Sache: die Beseitigung der Unzuverlässigkeitsgründe vor dem maßgeblichen Beurteilungszeitpunkt.

## Eingaben

- Untersagungsverfügung oder Anhörungsschreiben mit Datum
- Gewerbe und Rechtsform; bei juristischen Personen die Organe
- Anknüpfungstatsachen: Steuerrückstände, Sozialversicherungsrückstände, Insolvenz, Vollstreckungsmaßnahmen, Eintragungen im Schuldnerverzeichnis, Straftaten, Ordnungswidrigkeiten
- Erklärungs- und Zahlungsverhalten gegenüber Finanzamt und Einzugsstelle
- Etwaige Ratenvereinbarung, Stundung, Sanierungskonzept, Restschuldbefreiung
- Ob eine spezialgesetzliche Untersagungs- oder Widerrufsvorschrift besteht
- Ob Sofortvollzug angeordnet wurde und wie er begründet ist

## Sub-Agent-Architektur

Der Researcher beschafft § 35 GewO, die Verwaltungsvorschriften, die einschlägige Rechtsprechung des BVerwG und der Oberverwaltungsgerichte sowie die Kommentarliteratur. Der Drafter subsumiert die Anknüpfungstatsachen, prüft Erforderlichkeit und Reichweite und entwirft Stellungnahme, Widerspruch oder Eilantrag. Der Reviewer kontrolliert den Beurteilungszeitpunkt, die Sperrwirkung des Abs. 8, die Anhörung der Kammern nach Abs. 4 und die Fristen.

## Ablauf

### 1. Sperrwirkung spezialgesetzlicher Vorschriften prüfen ([§ 35 Abs. 8 GewO](https://www.gesetze-im-internet.de/gewo/__35.html))

**Dieser Schritt steht vor allem anderen.** Nach § 35 Abs. 8 S. 1 GewO sind die Absätze 1 bis 7a **nicht anzuwenden**, soweit für einzelne Gewerbe besondere Untersagungs- oder Betriebsschließungsvorschriften bestehen, die auf die Unzuverlässigkeit abstellen, **oder** soweit eine erteilte Zulassung wegen Unzuverlässigkeit zurückgenommen oder widerrufen werden kann.

Praktische Folge: Bei **erlaubnispflichtigen** Gewerben — etwa nach §§ 34a, 34c, 34d, 34f, 34i GewO — ist regelmäßig **nicht** § 35 GewO, sondern die Rücknahme oder der Widerruf der Erlaubnis nach §§ 48, 49 VwVfG bzw. der spezialgesetzlichen Regelung einschlägig (`/gewerberecht:gewerbeerlaubnis-34-gewo`). Eine auf § 35 GewO gestützte Verfügung ist dann bereits deshalb rechtswidrig.

Ausgenommen von der Sperrwirkung bleiben nach § 35 Abs. 8 S. 2 GewO die Tätigkeit als vertretungsberechtigte Person oder Betriebsleiter sowie Vorschriften über strafgerichtliche Untersagungen.

### 2. Unzuverlässigkeit prüfen ([§ 35 Abs. 1 S. 1 GewO](https://www.gesetze-im-internet.de/gewo/__35.html))

Unzuverlässig ist, wer nach dem Gesamtbild seines Verhaltens keine Gewähr dafür bietet, das Gewerbe künftig ordnungsgemäß auszuüben. Es handelt sich um eine **Prognoseentscheidung** auf der Grundlage feststehender Tatsachen; ein Verschulden ist **nicht** erforderlich.

Praktisch bedeutsame Fallgruppen:

| Fallgruppe | Prüfpunkte |
|---|---|
| **Steuerrückstände** | Höhe absolut und im Verhältnis zum Umsatz, Dauer, Entwicklung, Verhalten gegenüber dem Finanzamt, Verletzung der Erklärungspflichten. Nicht die Höhe allein trägt, sondern das Gesamtbild aus Rückstand und Verhalten |
| **Sozialversicherungsbeiträge** | Rückstände bei der Einzugsstelle; zugleich strafrechtliche Relevanz nach § 266a StGB |
| **Wirtschaftliche Leistungsunfähigkeit** | Zahlungsunfähigkeit oder Überschuldung, fruchtlose Vollstreckung, Eintragung im Schuldnerverzeichnis, Abgabe der Vermögensauskunft |
| **Straftaten und Ordnungswidrigkeiten** | Gewerbebezug erforderlich; Verwertungsverbote des BZRG beachten |
| **Verstöße gegen gewerberechtliche Pflichten** | Anzeigepflicht § 14 GewO, Buchführung, Aufzeichnungs- und Auskunftspflichten |

**Insolvenzbezug:** Die Eröffnung eines Insolvenzverfahrens begründet für sich genommen noch nicht zwingend die Unzuverlässigkeit; entscheidend ist, ob ein tragfähiges Sanierungskonzept besteht und die laufenden Pflichten erfüllt werden. Die Wechselwirkung zwischen Restschuldbefreiung, Insolvenzplan und gewerberechtlicher Prognose ist im Einzelfall zu belegen `[unverifiziert – prüfen]`.

**Maßgeblicher Beurteilungszeitpunkt** ist bei der Anfechtung der Untersagungsverfügung nach ständiger verwaltungsgerichtlicher Praxis der Zeitpunkt der **letzten Behördenentscheidung** — also des Widerspruchsbescheids, sonst der Ausgangsverfügung. **Nachträgliche Tilgung wirkt im Anfechtungsprozess nicht mehr**, sondern nur noch über den Wiedergestattungsantrag nach Abs. 6. Diese Weichenstellung ist die praktisch wichtigste des Gebiets und im Mandat sofort zu kommunizieren; die einschlägige Rechtsprechung ist zu belegen `[unverifiziert – prüfen]`.

### 3. Erforderlichkeit prüfen

Die Untersagung setzt zusätzlich voraus, dass sie **zum Schutz der Allgemeinheit oder der im Betrieb Beschäftigten erforderlich** ist. Zu prüfen sind mildere Mittel: Auflagen, Ratenvereinbarungen mit dem Finanzamt, Bestellung eines Stellvertreters nach § 35 Abs. 2 iVm § 45 GewO, teilweise statt vollständige Untersagung.

Liegen Unzuverlässigkeit und Erforderlichkeit vor, ist die Untersagung **gebunden** — „ist zu untersagen". Ein Ermessensfehler kann dann nur noch die **Reichweite** betreffen, nicht das Ob.

### 4. Reichweite bestimmen ([§ 35 Abs. 1 S. 2, Abs. 7a GewO](https://www.gesetze-im-internet.de/gewo/__35.html))

- **Erweiterte Untersagung (Abs. 1 S. 2)**: Die Untersagung kann auf die Tätigkeit als **Vertretungsberechtigter** oder **Betriebsleiter** sowie auf **einzelne andere oder alle Gewerbe** erstreckt werden, soweit die festgestellten Tatsachen die Annahme rechtfertigen, dass der Gewerbetreibende auch insoweit unzuverlässig ist. Die Erstreckung ist **Ermessensentscheidung** und muss eigenständig begründet werden; eine formelhafte Begründung ist angreifbar (§ 39 VwVfG, § 114 VwGO).
- **Abs. 1 S. 3**: Das Verfahren kann **fortgesetzt** werden, auch wenn der Betrieb während des Verfahrens aufgegeben wird. Die Betriebsaufgabe erledigt die Verfügung also nicht.
- **Abs. 7a**: Die Untersagung kann auch **gegen Vertretungsberechtigte und Betriebsleiter** ausgesprochen werden; dieses Verfahren läuft unabhängig vom Verfahren gegen den Gewerbetreibenden. Abs. 8 S. 2 nimmt diese Konstellation von der Sperrwirkung aus.
- **Abs. 9**: Entsprechende Anwendung auf Genossenschaften sowie auf den Handel mit Arzneimitteln, Lotterielosen und Bezugs- oder Anteilscheinen.

Bei **juristischen Personen** trifft die Untersagung die Gesellschaft; parallel kommt die Untersagung gegen das Organ nach Abs. 7a in Betracht. Beide Verfahren sind auseinanderzuhalten.

### 5. Verfahrensrecht prüfen

- **Anhörung** nach [§ 28 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__28.html) bzw. der Landesparallelvorschrift. Die Anhörung ist der wichtigste Zeitpunkt zur Beibringung von Tilgungsnachweisen und Ratenvereinbarungen.
- **Kammeranhörung** nach § 35 Abs. 4 GewO: Vor der Untersagung **sollen** die zuständige Industrie- und Handelskammer oder Handwerkskammer, besondere staatliche Aufsichtsbehörden und bei Genossenschaften der Prüfungsverband gehört werden; ihnen sind die Vorwürfe mitzuteilen und die erforderlichen Unterlagen zu übersenden. Die Anhörung kann bei Gefahr im Verzug unterbleiben, die Stellen sind dann zu unterrichten. Das Unterbleiben ohne Gefahr im Verzug ist ein Verfahrensfehler und ausdrücklich zu rügen.
- **Zuständigkeit** nach Abs. 7: Behörde am Bezirk der gewerblichen Niederlassung; fehlt sie, am Ort der Gewerbeausübung. Für die Vollstreckung sind auch die Behörden am Ausübungsort zuständig.
- **Begründung** nach § 39 VwVfG, insbesondere für die Ermessensausübung bei der erweiterten Untersagung.
- **Bindung an strafgerichtliche Feststellungen** nach Abs. 3: Will die Behörde einen Sachverhalt berücksichtigen, der Gegenstand der Urteilsfindung in einem Strafverfahren war, darf sie zum Nachteil des Gewerbetreibenden nicht von den dortigen Feststellungen zum Sachverhalt, zur Schuldfrage und zur Gefahrenprognose nach § 70 StGB abweichen. Strafbefehl, Ablehnung der Eröffnung des Hauptverfahrens und vorläufiges Berufsverbot stehen einem Urteil gleich; Bußgeldentscheidungen binden hinsichtlich Sachverhalt und Schuldfrage. Abs. 1 S. 2 bleibt unberührt.

### 6. Rechtsschutz und Sofortvollzug

- **Widerspruch** nach §§ 68 ff. VwGO, soweit das Landesrecht das Vorverfahren nicht abgeschafft hat — die Abschaffung ist landesrechtlich zu prüfen `[unverifiziert – prüfen]` je Land. Frist: ein Monat ([§ 70 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html)).
- **Anfechtungsklage** nach [§ 42 Abs. 1 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html), Frist ein Monat ([§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html)).
- **Sofortvollzug**: Die Anordnung nach [§ 80 Abs. 2 S. 1 Nr. 4 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html) bedarf der schriftlichen Begründung des besonderen Vollzugsinteresses nach § 80 Abs. 3 VwGO. Eine Begründung, die lediglich die Untersagungsgründe wiederholt, genügt nicht — das ist der häufigste Angriffspunkt im Eilverfahren. Rechtsbehelf: Antrag nach [§ 80 Abs. 5 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html) (`/verwaltungsrecht:vorlaeufiger-rechtsschutz-80`).
- **Zwangsmittel**: Zwangsgeld und unmittelbarer Zwang nach dem jeweiligen Verwaltungsvollstreckungsrecht; die Fortsetzung des Betriebs trotz vollziehbarer Untersagung ist zudem nach § 148 Nr. 1 GewO strafbewehrt.

### 7. Wiedergestattung ([§ 35 Abs. 6 GewO](https://www.gesetze-im-internet.de/gewo/__35.html))

Auf schriftlichen oder elektronischen Antrag ist die persönliche Ausübung des Gewerbes **wieder zu gestatten**, wenn Tatsachen die Annahme rechtfertigen, dass eine Unzuverlässigkeit im Sinne des Abs. 1 **nicht mehr vorliegt**. Vor Ablauf **eines Jahres** nach Durchführung der Untersagungsverfügung ist die Wiedergestattung nur bei **besonderen Gründen** möglich.

Der Wiedergestattungsantrag ist der eigentliche Weg zurück in die gewerbliche Tätigkeit, wenn die Rückstände nach dem maßgeblichen Beurteilungszeitpunkt getilgt wurden. Er ist von Anfang an mitzuplanen: Tilgungsnachweise, Ratenvereinbarungen, Erklärungsverhalten und ein tragfähiges Konzept sind zu dokumentieren.

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik; die Anknüpfung bleibt juristische Eingabe:

```bash
# Widerspruchsfrist § 70 VwGO: 1 Monat ab Bekanntgabe am 12.03.2026 in Bayern
python -m scripts.legal_calc.cli frist --ereignis 12.03.2026 --menge 1 --einheit monate --land BY

# Klagefrist § 74 VwGO: 1 Monat ab Zustellung des Widerspruchsbescheids
python -m scripts.legal_calc.cli frist --ereignis 20.06.2026 --menge 1 --einheit monate --land BY

# Jahressperre der Wiedergestattung § 35 Abs. 6 S. 2 GewO ab Durchführung der Untersagung
python -m scripts.legal_calc.cli frist --ereignis 01.07.2026 --menge 1 --einheit jahre --land BY
```

`--json` liefert die Rechenschritte samt berücksichtigter Feiertage.

## Quellen

### Statute

- [§ 35 GewO](https://www.gesetze-im-internet.de/gewo/__35.html), [§ 14 GewO](https://www.gesetze-im-internet.de/gewo/__14.html), [§ 15 GewO](https://www.gesetze-im-internet.de/gewo/__15.html), [§ 45 GewO](https://www.gesetze-im-internet.de/gewo/__45.html), [§ 148 GewO](https://www.gesetze-im-internet.de/gewo/__148.html)
- [§ 28 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__28.html), [§ 39 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__39.html), [§ 48 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__48.html), [§ 49 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__49.html)
- [§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html), [§ 70 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html), [§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html), [§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html), [§ 114 VwGO](https://www.gesetze-im-internet.de/vwgo/__114.html)
- [§ 70 StGB](https://www.gesetze-im-internet.de/stgb/__70.html), [§ 266a StGB](https://www.gesetze-im-internet.de/stgb/__266a.html); [BZRG](https://www.gesetze-im-internet.de/bzrg/)
- Landesverwaltungsvollstreckungsrecht sowie landesrechtliche Regelungen zum Vorverfahren `[unverifiziert – prüfen]`

### Kommentare

- Landmann/Rohmer, GewO, § 35 Rn. 1 ff. (Standardkommentar).
- Pielow, GewO, § 35.
- Ennuschat/Wank/Winkler, GewO, § 35.
- Kopp/Schenke, VwGO, § 80 Abs. 5, § 114.
- Kopp/Ramsauer, VwVfG, §§ 28, 39, 48, 49.

### Rechtsprechung

Zur gewerberechtlichen Unzuverlässigkeit, zum maßgeblichen Beurteilungszeitpunkt und zur erweiterten Untersagung besteht gefestigte Rechtsprechung des BVerwG und der Oberverwaltungsgerichte. Jede konkrete Entscheidung ist vor Verwendung in juris, Beck-Online oder auf bverwg.de zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
GEWERBEUNTERSAGUNG § 35 GewO — <Mandat> — <Datum>

I.   Vorprüfung
     Gewerbe:                 <…>   Erlaubnispflichtig: [ja / nein]
     Sperrwirkung Abs. 8:     [einschlägig — § 35 GewO unanwendbar / nicht einschlägig]
     Adressat:                <natürliche Person / Gesellschaft / Organ nach Abs. 7a>

II.  Anknüpfungstatsachen
     Steuerrückstände:        <Betrag, Dauer, Erklärungsverhalten>
     Sozialversicherung:      <Betrag, Dauer>
     Vollstreckung / Schuldnerverzeichnis: <…>
     Straftaten / OWi:        <Gewerbebezug, BZRG-Verwertbarkeit>
     Insolvenz:               <Stand, Sanierungskonzept>

III. Unzuverlässigkeit und Erforderlichkeit
     Prognose:                <Gesamtbild>
     Maßgeblicher Zeitpunkt:  <letzte Behördenentscheidung — Datum>
     Mildere Mittel:          <Auflage / Ratenvereinbarung / Stellvertreter § 35 Abs. 2>
     Ergebnis:                [gebundene Untersagung / nicht erforderlich]

IV.  Reichweite
     Untersagtes Gewerbe:     <…>
     Erweiterung Abs. 1 S. 2: [ausgesprochen — eigenständig begründet? / nein]
     Abs. 7a gegen Organ:     [Verfahren läuft / nein]
     Betriebsaufgabe:         [Verfahren fortgesetzt nach Abs. 1 S. 3]

V.   Verfahren
     Anhörung § 28 VwVfG:     [erfolgt am <Datum> / unterblieben]
     Kammeranhörung Abs. 4:   [erfolgt / unterblieben — Gefahr im Verzug? Rüge]
     Zuständigkeit Abs. 7:    <Behörde>
     Begründung § 39 VwVfG:   [tragfähig / formelhaft]
     Bindung Abs. 3:          [strafgerichtliche Feststellungen — Umfang]

VI.  Rechtsschutz
     Widerspruch:             Frist bis <Datum> [Vorverfahren im Land <X> vorgesehen?]
     Klage § 74 VwGO:         Frist bis <Datum>, VG <Ort>
     Sofortvollzug:           [angeordnet — Begründung § 80 Abs. 3 VwGO tragfähig? / nein]
     Antrag § 80 Abs. 5 VwGO: [empfohlen / nicht erforderlich]

VII. Wiedergestattung Abs. 6
     Jahressperre endet:      <Datum>   Besondere Gründe: <…>
     Aufbaumaßnahmen:         <Tilgungsplan, Ratenvereinbarung, Nachweise>

VIII.Risiko: 🟢 / 🟡 / 🔴 <Begründung>
IX.  Quellenverzeichnis
```

### Formulierungshilfe — Stellungnahme im Anhörungsverfahren (Gerüst)

```
An die <Behörde>
Anhörung zur beabsichtigten Gewerbeuntersagung, Az. <…>

Namens und in Vollmacht nehmen wir zu der beabsichtigten Untersagung wie
folgt Stellung:

I.   Verfahrensrügen
     1. Eine Anhörung der zuständigen Industrie- und Handelskammer nach
        § 35 Abs. 4 GewO ist bislang nicht erfolgt; Gefahr im Verzug ist
        nicht ersichtlich.
II.  Anwendbarkeit
     Für das ausgeübte Gewerbe besteht mit § <…> eine besondere
     Untersagungsvorschrift; § 35 GewO ist nach Abs. 8 nicht anwendbar.
III. Zur Unzuverlässigkeit
     1. Die Rückstände beruhen auf <…> und sind seit <Datum> rückläufig.
     2. Mit dem Finanzamt besteht seit <Datum> eine Ratenvereinbarung
        (Anlage <…>); die laufenden Erklärungen werden fristgerecht
        abgegeben (Anlage <…>).
IV.  Zur Erforderlichkeit
     Als milderes Mittel kommt <Auflage / Stellvertreterbestellung nach
     § 35 Abs. 2 iVm § 45 GewO> in Betracht.
V.   Anträge
     1. Von der Untersagung abzusehen.
     2. Hilfsweise: von der erweiterten Untersagung nach § 35 Abs. 1 S. 2
        GewO abzusehen und von der Anordnung der sofortigen Vollziehung
        abzusehen.
```

## Risiken / typische Fehler

- **§ 35 GewO trotz Sperrwirkung des Abs. 8 angewandt.** Bei erlaubnispflichtigen Gewerben ist regelmäßig Rücknahme oder Widerruf der Erlaubnis der richtige Weg.
- **Maßgeblichen Beurteilungszeitpunkt verkannt.** Nachträgliche Tilgung hilft im Anfechtungsprozess nicht mehr; sie gehört in die Anhörung oder in den Wiedergestattungsantrag nach Abs. 6.
- **Auf ein Ermessen beim Ob gehofft.** Liegen Unzuverlässigkeit und Erforderlichkeit vor, ist die Untersagung gebunden; Ermessen besteht nur bei der Erweiterung nach Abs. 1 S. 2.
- **Erweiterte Untersagung ohne eigenständige Begründung hingenommen.** Sie ist Ermessensentscheidung und nach § 39 VwVfG zu begründen; formelhafte Begründungen sind angreifbar.
- **Kammeranhörung nach Abs. 4 nicht gerügt**, obwohl sie ohne Gefahr im Verzug unterblieben ist.
- **Betriebsaufgabe für erledigend gehalten.** Abs. 1 S. 3 lässt die Fortsetzung des Verfahrens ausdrücklich zu.
- **Verfahren gegen Gesellschaft und Organ vermengt.** Die Untersagung nach Abs. 7a läuft unabhängig.
- **Bindungswirkung des Abs. 3 überdehnt oder übersehen.** Sie erfasst Sachverhalt, Schuldfrage und Prognose nach § 70 StGB, nicht jede strafrechtliche Wertung.
- **Sofortvollzugsbegründung nicht angegriffen.** Eine bloße Wiederholung der Untersagungsgründe genügt § 80 Abs. 3 VwGO nicht.
- **Wiedergestattung erst nach Jahren geplant.** Die Jahressperre des Abs. 6 S. 2 läuft ab Durchführung der Untersagung; der Antrag ist von Anfang an vorzubereiten.
- **Rechtsprechung erfunden.** Jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
