---
name: bfsg-dienstleistung-ecommerce-borghei
title: /barrierefreiheit-bfsg:bfsg-dienstleistung-ecommerce
description: Barrierefreiheit von Dienstleistungen im elektronischen Geschäftsverkehr – Pflichten des Dienstleistungserbringers § 14 BFSG, Barrierefreiheitsinformationen nach Anlage 3 Nr. 1 mit Beschreibung, Erläuterung, Konformitätsdarlegung und Angabe der Marktüberwachungsbehörde, materielle Anforderungen der §§ 12, 13 und 19 BFSGV, Stand der Technik § 3 BFSGV und Konformitätsvermutung §§ 4, 5 BFSG über harmonisierte Normen, Ausnahmen §§ 16, 17 BFSG mit Kriterienkatalog der Anlage 4 und fünfjährigem Wiederholungsrhythmus § 17 Abs. 3, Marktüberwachung von Dienstleistungen §§ 28–31, Verbraucher- und Verbandsrechte §§ 32, 33, Schlichtung § 34 sowie Bußgeld § 37 Abs. 1 Nr. 8. Use when ein Online-Shop, eine App, ein Bankangebot oder ein Personenbeförderungsdienst auf BFSG-Konformität zu bringen oder eine Beanstandung abzuwehren ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/barrierefreiheit-bfsg/skills/bfsg-dienstleistung-ecommerce
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /barrierefreiheit-bfsg:bfsg-dienstleistung-ecommerce

## Zweck

Der Skill bringt eine erfasste Dienstleistung — typischerweise einen Online-Shop, eine App oder ein Bankangebot für Verbraucher — auf BFSG-Konformität. Er trennt die drei Ebenen, die in der Praxis regelmäßig vermengt werden: die **materiellen** Anforderungen der BFSGV, die **Informationspflicht** nach § 14 Abs. 1 Nr. 2 iVm Anlage 3 und die **Dokumentationspflicht** bei Berufung auf eine Ausnahme. Er entwirft die Barrierefreiheitsinformationen und die Reaktion auf Verbraucher-, Verbands- und Behördenanträge.

## Eingaben

- Art der Dienstleistung und Zuordnung zu § 1 Abs. 3 BFSG
- Verbraucherbezug; bei gemischten Angeboten die Abgrenzung der B2C-Strecke
- Technischer Stand: Prüfbericht, WCAG- bzw. EN-301-549-Konformitätsstand, offene Barrieren
- Vorhandene Barrierefreiheitsinformationen und ihr Fundort (AGB, Fußzeile, eigene Seite)
- Eingesetzte Produkte iSd § 1 Abs. 2 BFSG (Terminals, Endgeräte) und deren Einsatzbeginn
- Etwaige Beurteilungen nach §§ 16, 17 BFSG samt Datum
- Vorliegender Verbraucher- oder Verbandsantrag, Behördenschreiben, Schlichtungsantrag

## Sub-Agent-Architektur

Der Researcher beschafft BFSG, BFSGV, Anlagen 3 und 4, die Richtlinie (EU) 2019/882 und die von der Bundesfachstelle für Barrierefreiheit veröffentlichten Standards und Konformitätstabellen. Der Drafter erstellt die Konformitätsmatrix, entwirft die Barrierefreiheitsinformationen und die Stellungnahme. Der Reviewer prüft, ob die Informationspflicht tatsächlich alle vier Elemente der Anlage 3 Nr. 1 enthält, ob eine Ausnahmeberufung dokumentiert und gemeldet ist und ob der Rechtsweg zutreffend dargestellt wird.

## Ablauf

### 1. Pflichtentrias des § 14 BFSG bestimmen

Nach [§ 14 Abs. 1 BFSG](https://www.gesetze-im-internet.de/bfsg/__14.html) darf der Dienstleistungserbringer seine Dienstleistung nur anbieten oder erbringen, wenn

1. die Dienstleistung die Barrierefreiheitsanforderungen der BFSGV **erfüllt** und
2. er die **Informationen nach Anlage 3 Nr. 1 erstellt** und **für die Allgemeinheit in barrierefreier Form zugänglich gemacht** hat.

Flankierend:

- **§ 14 Abs. 2** — Aufbewahrung der Informationen, solange die Dienstleistung angeboten oder erbracht wird.
- **§ 14 Abs. 3** — fortlaufende Gewährleistung der Konformität; Änderungen der Erbringung, der Anforderungen und der herangezogenen Normen sind zu berücksichtigen.
- **§ 14 Abs. 4** — bei Nichtkonformität: unverzüglich Korrekturmaßnahmen; genügt die Dienstleistung den Anforderungen nicht, ist die Marktüberwachungsbehörde — und sind die Behörden aller Mitgliedstaaten, in denen angeboten wird — **unverzüglich** und mit ausführlichen Angaben zu Art der Nichtkonformität und Korrekturmaßnahmen zu informieren.
- **§ 14 Abs. 5** — Auskunft und Kooperation gegenüber der Marktüberwachungsbehörde auf begründetes Verlangen.

Das Anbieten einer nicht konformen Dienstleistung ist nach [§ 37 Abs. 1 Nr. 8 BFSG](https://www.gesetze-im-internet.de/bfsg/__37.html) mit einer Geldbuße bis **100.000 EUR** bewehrt.

### 2. Materielle Anforderungen der BFSGV zuordnen

| Norm | Inhalt |
|---|---|
| [§ 12 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__12.html) | **Allgemeine Anforderungen an Dienstleistungen**: eingesetzte Produkte müssen ihrerseits den §§ 4 bis 11 BFSGV genügen; Informationen über Funktionsweise und Verbindung zu Produkten sind über mehr als einen sensorischen Kanal, auffindbar, verständlich, wahrnehmbar, in generierbaren Textformaten, in angemessener Schriftgröße mit ausreichendem Kontrast und mit Alternativdarstellung für nicht-textliche Inhalte bereitzustellen |
| [§ 13 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__13.html) | zusätzliche Anforderungen an bestimmte Dienstleistungen |
| [§ 14 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__14.html) | Telekommunikationsdienstleister |
| [§ 15 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__15.html), [§ 16 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__16.html) | Personenbeförderungsdienste; Stadt-, Vorort- und Regionalverkehr |
| [§ 17 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__17.html) | Bankdienstleistungen für Verbraucher |
| [§ 18 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__18.html) | E-Books |
| [§ 19 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__19.html) | **Dienstleistungen im elektronischen Geschäftsverkehr**: Informationen zur Barrierefreiheit der angebotenen Produkte und Dienstleistungen, soweit vom verantwortlichen Wirtschaftsakteur bereitgestellt; Identifizierungs-, Authentifizierungs-, Sicherheits- und Zahlungsfunktionen sowie elektronische Signaturen und Zahlungsdienste müssen **wahrnehmbar, bedienbar, verständlich und robust** gestaltet sein |
| [§ 20 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__20.html), [§ 21 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__21.html) | funktionale Leistungskriterien |

Die vier Prinzipien des § 19 BFSGV — wahrnehmbar, bedienbar, verständlich, robust — sind die POUR-Prinzipien der WCAG. Über [§ 4 BFSG](https://www.gesetze-im-internet.de/bfsg/__4.html) vermittelt die Übereinstimmung mit einer im Amtsblatt gelisteten **harmonisierten Norm** die Konformitätsvermutung; für digitale Angebote ist dies **EN 301 549**, die ihrerseits auf die WCAG verweist `[unverifiziert – prüfen]` hinsichtlich des jeweils gelisteten Fassungsstands. [§ 3 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__3.html) verlangt daneben die Beachtung des **Standes der Technik**; die Bundesfachstelle für Barrierefreiheit veröffentlicht dazu Standardauflistungen und Konformitätstabellen.

**Die Vermutungswirkung ist anforderungsbezogen**: Ein Konformitätsgrad „WCAG AA weitgehend erfüllt" trägt nicht; erforderlich ist die Zuordnung je Anforderung.

### 3. Barrierefreiheitsinformationen nach Anlage 3 Nr. 1 erstellen

Der Dienstleistungserbringer gibt **in den AGB oder auf andere deutlich wahrnehmbare Weise** an, wie die Dienstleistung die Anforderungen erfüllt. Die Information umfasst eine Beschreibung der geltenden Anforderungen und deckt, soweit für die Bewertung von Belang, Gestaltung und Durchführung ab. Neben den Verbraucherinformationspflichten des Art. 246 EGBGB enthält sie **jedenfalls**:

- a) eine **allgemeine Beschreibung der Dienstleistung in einem barrierefreien Format**;
- b) **Beschreibungen und Erläuterungen**, die zum Verständnis der Durchführung erforderlich sind;
- c) eine **Beschreibung, wie die Dienstleistung die einschlägigen Anforderungen der BFSGV erfüllt**;
- d) die **Angabe der zuständigen Marktüberwachungsbehörde**.

Nach Anlage 3 Nr. 2 kann der Erbringer hierfür harmonisierte Normen und technische Spezifikationen ganz oder teilweise anwenden.

**Element d) fehlt in der Praxis fast immer.** Die Angabe der zuständigen Marktüberwachungsbehörde ist Pflichtbestandteil, nicht Zierrat. Die Information ist ihrerseits **barrierefrei** zugänglich zu machen und für die **Allgemeinheit** — also ohne Login und ohne Bestellvorgang.

### 4. Ausnahmen prüfen und dokumentieren (§§ 16, 17 BFSG, Anlage 4)

- **[§ 16 BFSG](https://www.gesetze-im-internet.de/bfsg/__16.html) — grundlegende Veränderung**: Die Anforderungen gelten nur, soweit ihre Einhaltung keine wesentliche Änderung erfordert, die zu einer grundlegenden Veränderung der Wesensmerkmale führt. Beurteilung durch den Erbringer, Dokumentation fünf Jahre, Vorlage auf Verlangen, unverzügliche Mitteilung an die Behörden aller betroffenen Mitgliedstaaten.
- **[§ 17 BFSG](https://www.gesetze-im-internet.de/bfsg/__17.html) — unverhältnismäßige Belastung**: Beurteilung nach den Kriterien der **Anlage 4** — insbesondere das Verhältnis der Nettokosten der Einhaltung zu den Gesamtkosten der Dienstleistungserbringung, einmalige Organisationskosten (Personal, Schulung, Prozessentwicklung, Leitfäden, Rechtskenntnis), laufende Kosten (Planung, Produktionsprozesse, Prüfung, Dokumentation) sowie das Verhältnis von Kosten und Nutzen für Menschen mit Behinderungen. Dokumentation fünf Jahre; **Wiederholung mindestens alle fünf Jahre** und stets bei Änderung der Dienstleistung oder auf behördliche Aufforderung (§ 17 Abs. 3). **§ 17 Abs. 4 sperrt die Berufung**, wenn nichteigene öffentliche oder private Mittel zur Verbesserung der Barrierefreiheit bezogen wurden.

Eine Ausnahme, die weder beurteilt noch dokumentiert noch gemeldet ist, existiert rechtlich nicht.

### 5. Marktüberwachung, Verbraucher- und Verbandsrechte

- **[§ 28 BFSG](https://www.gesetze-im-internet.de/bfsg/__28.html)** — Marktüberwachung von Dienstleistungen durch die zuständigen Behörden; **[§ 29](https://www.gesetze-im-internet.de/bfsg/__29.html)** — Maßnahmen bei nicht konformen Dienstleistungen; **[§ 30](https://www.gesetze-im-internet.de/bfsg/__30.html)** — formale Nichtkonformität; **[§ 31](https://www.gesetze-im-internet.de/bfsg/__31.html)** — Veröffentlichung von Informationen.
- **[§ 32 BFSG](https://www.gesetze-im-internet.de/bfsg/__32.html)** — Auf **Antrag eines Verbrauchers** hat die Behörde ein Verfahren einzuleiten, wenn geltend gemacht wird, dass ein Verstoß die Nutzung unmöglich macht oder einschränkt. Der Verbraucher kann einen nach § 15 Abs. 3 BGG anerkannten Verband oder eine qualifizierte Einrichtung nach § 3 Abs. 1 S. 1 Nr. 1 UKlaG beauftragen. Nach **§ 32 Abs. 2** können solche Verbände und Einrichtungen den Antrag **ohne eigene Rechtsverletzung** stellen, wenn der Verstoß ihren satzungsgemäßen Aufgabenbereich berührt. Die Behörde entscheidet durch **Bescheid** (Abs. 3).
- **[§ 33 BFSG](https://www.gesetze-im-internet.de/bfsg/__33.html)** — Rechtsbehelfe nach der VwGO gegen den Bescheid oder dessen Unterlassen, auch durch Verbände und qualifizierte Einrichtungen; vor dem BVerwG nur durch Personen mit Befähigung zum Richteramt.
- **[§ 34 BFSG](https://www.gesetze-im-internet.de/bfsg/__34.html)** — **Schlichtung** vor der Schlichtungsstelle nach § 16 Abs. 1 BGG; ein Verfahren nach § 32 ist bis zur Beendigung der Schlichtung **auszusetzen** (§ 34 Abs. 4).

**Das BFSG kennt keinen eigenen zivilrechtlichen Erfüllungs- oder Schadensersatzanspruch des Verbrauchers.** Die Durchsetzung läuft über das Verwaltungsverfahren, die Schlichtung und – als eigenständige, streitige Frage – über das Lauterkeitsrecht. Ob ein BFSG-Verstoß eine Marktverhaltensregel iSd § 3a UWG darstellt und damit abmahnfähig ist, ist **ungeklärt**; die Frage ist im Mandat offen zu benennen und nicht als entschieden darzustellen `[unverifiziert – prüfen]`.

### 6. Altbestand und Übergang (§ 38 BFSG)

Dienstleistungen dürfen unter Einsatz von Produkten, die vor dem 28.06.2025 rechtmäßig eingesetzt wurden, **bis zum 27.06.2030** weiter erbracht werden; vor diesem Stichtag geschlossene Dienstleistungsverträge dürfen bis zum Ablauf ihrer Laufzeit, längstens bis zum 27.06.2030, unverändert fortbestehen. Selbstbedienungsterminals genießen die Fünfzehnjahresfrist des § 38 Abs. 2. Details: `/barrierefreiheit-bfsg:bfsg-anwendungsbereich`.

## Deterministische Berechnung

Zu rechnen sind der Fünfjahresrhythmus der Beurteilung nach § 17 Abs. 3 BFSG, die Aufbewahrungsfristen und die Verfahrensfristen. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# Wiederholung der Beurteilung § 17 Abs. 3 BFSG: 5 Jahre ab 30.06.2025
python -m scripts.legal_calc.cli frist --ereignis 30.06.2025 --menge 5 --einheit jahre --land BY

# Widerspruchsfrist § 70 VwGO gegen den Bescheid nach § 32 Abs. 3 BFSG
python -m scripts.legal_calc.cli frist --ereignis 05.05.2026 --menge 1 --einheit monate --land BY
```

Ob eine Belastung „unverhältnismäßig" ist, bleibt eine Wertung nach Anlage 4 und ist gesondert zu begründen.

## Quellen

### Statute

- [§ 1](https://www.gesetze-im-internet.de/bfsg/__1.html), [§ 3](https://www.gesetze-im-internet.de/bfsg/__3.html), [§ 4](https://www.gesetze-im-internet.de/bfsg/__4.html), [§ 5](https://www.gesetze-im-internet.de/bfsg/__5.html), [§ 14](https://www.gesetze-im-internet.de/bfsg/__14.html), [§ 16](https://www.gesetze-im-internet.de/bfsg/__16.html), [§ 17](https://www.gesetze-im-internet.de/bfsg/__17.html), [§ 28](https://www.gesetze-im-internet.de/bfsg/__28.html), [§ 29](https://www.gesetze-im-internet.de/bfsg/__29.html), [§ 32](https://www.gesetze-im-internet.de/bfsg/__32.html), [§ 33](https://www.gesetze-im-internet.de/bfsg/__33.html), [§ 34](https://www.gesetze-im-internet.de/bfsg/__34.html), [§ 37 BFSG](https://www.gesetze-im-internet.de/bfsg/__37.html), [§ 38 BFSG](https://www.gesetze-im-internet.de/bfsg/__38.html); Anlagen 3 und 4
- [§ 3](https://www.gesetze-im-internet.de/bfsgv/__3.html), [§ 12](https://www.gesetze-im-internet.de/bfsgv/__12.html), [§ 13](https://www.gesetze-im-internet.de/bfsgv/__13.html), [§ 17](https://www.gesetze-im-internet.de/bfsgv/__17.html), [§ 19](https://www.gesetze-im-internet.de/bfsgv/__19.html), [§ 21 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__21.html)
- Richtlinie (EU) 2019/882, Anhang I Abschnitt III und IV — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2019/882/oj)
- [§ 16 BGG](https://www.gesetze-im-internet.de/bgg/__16.html) (Schlichtungsstelle), § 15 Abs. 3 BGG (anerkannte Verbände)
- Art. 246 EGBGB; [§ 3a UWG](https://www.gesetze-im-internet.de/uwg_2004/__3a.html); [§ 70 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html)

### Kommentare und Literatur

- Ritgen/Sellmann, BFSG, Kommentar, § 14, § 17, §§ 32 ff.
- Dörr/Natlacen, Barrierefreiheitsstärkungsgesetz, Praxishandbuch, Kap. Dienstleistungen und E-Commerce.
- Köhler/Bornkamm/Feddersen, UWG, § 3a (zur Marktverhaltensregel — Einordnung des BFSG offen).
- Bundesfachstelle für Barrierefreiheit, Standardauflistung und Konformitätstabellen nach § 3 Abs. 2 BFSGV.

### Rechtsprechung

Zum BFSG liegt bislang **keine gefestigte Rechtsprechung** vor; insbesondere ist ungeklärt, ob § 14 BFSG eine Marktverhaltensregel iSd § 3a UWG ist. Jede Entscheidung, die ein Modell hierzu nennt, ist als `[unverifiziert – prüfen]` zu behandeln, bis sie in juris oder Beck-Online belegt ist.

## Ausgabeformat

```
BFSG-DIENSTLEISTUNGSPRÜFUNG — <Angebot> — <Datum>

I.   Einordnung
     Dienstleistung § 1 Abs. 3 Nr.:   <…>
     Verbraucherbezug:                [ja / gemischt — B2C-Strecke: …]
     Erbringung seit:                 <Datum>   Übergang § 38: [einschlägig / nein]

II.  Materielle Konformität
     Einschlägige BFSGV-Normen:       <§§ 12, 13, 19, 21 …>
     Herangezogene harmonisierte Norm: <…>   Vermutungswirkung § 4 BFSG: [je Anforderung]
     Befundmatrix:
       Anforderung | Status | Nachweis | offene Barriere
       <…>

III. Informationspflicht § 14 Abs. 1 Nr. 2 iVm Anlage 3 Nr. 1
     a) allgemeine Beschreibung in barrierefreiem Format:  [vorhanden / fehlt]
     b) Beschreibungen und Erläuterungen:                  [vorhanden / fehlt]
     c) Darlegung der Anforderungserfüllung:               [vorhanden / fehlt]
     d) Angabe der Marktüberwachungsbehörde:               [vorhanden / fehlt]
     Fundort:                          <AGB / eigene Seite / Fußzeile>
     Barrierefrei und ohne Login zugänglich: [ja / nein]

IV.  Ausnahmen
     § 16 grundlegende Veränderung:    [beurteilt am <Datum> / nicht beurteilt]
     § 17 unverhältnismäßige Belastung nach Anlage 4: [beurteilt am <Datum> / nicht beurteilt]
     Nächste Wiederholung § 17 Abs. 3: <Datum>
     Fördermittel (§ 17 Abs. 4):       [ja — Berufung gesperrt / nein]
     Mitteilung an die Behörde:        [erfolgt / offen]

V.   Verfahren und Rechtsschutz
     Antrag nach § 32 Abs. 1 / Abs. 2: <Verbraucher / Verband / qualifizierte Einrichtung>
     Bescheid § 32 Abs. 3:             <Stand>
     Schlichtung § 34:                 [beantragt — Verfahren ausgesetzt / nein]
     Rechtsbehelf § 33 iVm VwGO:       <Frist bis <Datum>>
     UWG-Risiko:                       offen — § 3a UWG ungeklärt

VI.  Maßnahmenplan
     Sofort | 30 Tage | 90 Tage | mit Priorität und Verantwortlichkeit

VII. Bußgeldrisiko § 37 Abs. 1 Nr. 8: bis 100.000 EUR
VIII.Risiko: 🟢 / 🟡 / 🔴 <Begründung>
IX.  Quellenverzeichnis
```

### Formulierungshilfe — Barrierefreiheitsinformationen nach Anlage 3 Nr. 1 (Gerüst)

```
Erklärung zur Barrierefreiheit unserer Dienstleistung

1. Allgemeine Beschreibung
   <Beschreibung der Dienstleistung in einfacher, barrierefrei
   zugänglicher Form>

2. Durchführung der Dienstleistung
   <Erläuterung des Ablaufs: Suche, Auswahl, Registrierung,
   Authentifizierung, Zahlung, Support>

3. Erfüllung der Barrierefreiheitsanforderungen
   Die Dienstleistung erfüllt die Anforderungen der §§ 12 und 19 BFSGV.
   Zugrunde gelegt wurde <harmonisierte Norm / technische Spezifikation>
   in der Fassung <…>. Abweichungen bestehen bei <…>; hierzu wurde eine
   Beurteilung nach § <16 / 17> BFSG am <Datum> vorgenommen.

4. Zuständige Marktüberwachungsbehörde
   <Bezeichnung, Anschrift, Kontakt>

5. Rückmeldung und Kontakt
   <barrierefreier Kontaktweg>; Schlichtung nach § 34 BFSG iVm
   § 16 BGG möglich.
```

## Risiken / typische Fehler

- **Angabe der Marktüberwachungsbehörde fehlt.** Anlage 3 Nr. 1 Buchst. d ist Pflichtbestandteil der Barrierefreiheitsinformationen.
- **Barrierefreiheitsinformationen hinter Login oder im Bestellprozess versteckt.** § 14 Abs. 1 Nr. 2 BFSG verlangt Zugänglichkeit **für die Allgemeinheit** und **in barrierefreier Form**.
- **BFSG-Erklärung mit der Erklärung zur Barrierefreiheit nach BITV 2.0 verwechselt.** Beide Regime haben unterschiedliche Pflichtinhalte und Adressaten.
- **Pauschale WCAG-Aussage statt anforderungsbezogener Zuordnung.** Die Vermutungswirkung des § 4 BFSG wirkt nur, soweit die gelistete Norm die konkrete Anforderung abdeckt.
- **Ausnahme behauptet ohne Beurteilung, Dokumentation und Mitteilung.** §§ 16, 17 BFSG setzen alle drei Schritte voraus; § 17 Abs. 4 sperrt zudem bei Fördermittelbezug.
- **Fünfjahresrhythmus des § 17 Abs. 3 nicht terminiert.**
- **Verbandsantrag als unzulässig behandelt.** § 32 Abs. 2 BFSG lässt ihn ohne eigene Rechtsverletzung zu.
- **Schlichtungsantrag ignoriert.** Nach § 34 Abs. 4 BFSG ist das Verfahren nach § 32 bis zur Beendigung der Schlichtung auszusetzen.
- **UWG-Abmahnfähigkeit als geklärt dargestellt.** Ob § 14 BFSG Marktverhaltensregel iSd § 3a UWG ist, ist offen und als offen zu benennen.
- **Rechtsprechung erfunden.** Zum BFSG existiert kaum Judikatur; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
