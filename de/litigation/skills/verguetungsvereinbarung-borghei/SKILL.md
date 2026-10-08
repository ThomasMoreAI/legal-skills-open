---
name: verguetungsvereinbarung-borghei
title: /kostenrecht-rvg:verguetungsvereinbarung
description: Gestaltung und Prüfung anwaltlicher Vergütungsvereinbarungen – Form- und Belehrungserfordernisse § 3a RVG (Textform, Bezeichnung als Vergütungsvereinbarung, deutliche Absetzung, Verbot der Aufnahme in die Vollmacht, Hinweis auf die begrenzte Kostenerstattung), Erfolgshonorar § 4a RVG mit der Wertgrenze für Geldforderungen und der außergerichtlichen Inkassodienstleistung, Zeithonorar, Unterschreitung der gesetzlichen Gebühren § 4 RVG und § 49b Abs. 1 BRAO, Folgen des Formmangels § 4b RVG, Herabsetzung unangemessen hoher Vergütung § 3a Abs. 3 RVG sowie Abrechnung und Fälligkeit §§ 8, 10 RVG. Use when eine Honorarvereinbarung entworfen, eine bestehende auf Wirksamkeit geprüft oder ein Honoraranspruch gegen den Einwand des Formmangels verteidigt wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/kostenrecht-rvg/skills/verguetungsvereinbarung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /kostenrecht-rvg:verguetungsvereinbarung

## Zweck

Die Vergütungsvereinbarung ist ein Formalakt mit harter Sanktion: Verfehlt sie die Anforderungen des § 3a Abs. 1 RVG, kann der Anwalt nach § 4b RVG **keine höhere als die gesetzliche Vergütung** fordern — unabhängig davon, wie viel Arbeit tatsächlich angefallen ist und ob der Mandant die Vereinbarung verstanden hat. Dieser Skill entwirft die Vereinbarung, prüft eine bestehende auf jeden einzelnen Formpunkt und ordnet Zeithonorar, Pauschale und Erfolgshonorar den zulässigen Gestaltungen zu.

## Eingaben

- Mandatsgegenstand und voraussichtlicher Gegenstandswert (für den Vergleich mit der gesetzlichen Vergütung)
- Gewünschtes Modell: Zeithonorar, Pauschalhonorar, Gebührenmultiplikator, Erfolgshonorar, Mischform
- Gerichtliches oder außergerichtliches Mandat (entscheidend für § 4 RVG und § 49b Abs. 1 BRAO)
- Ist der Mandant Verbraucher? (AGB-Kontrolle §§ 305 ff. BGB, Widerrufsrecht bei Fernabsatz)
- Bei Erfolgshonorar: Höhe der Geldforderung, außergerichtliche Inkassodienstleistung, wirtschaftliche Situation des Auftraggebers
- Bereits erbrachte Leistungen und geleistete Zahlungen
- Bei Prüfung einer bestehenden Vereinbarung: Originaldokument, Vollmacht, Auftragserteilung als getrennte Urkunden?

## Sub-Agent-Architektur

Der **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) belegt die Formanforderungen aus §§ 3a, 4, 4a RVG und § 49b BRAO und ermittelt die gesetzliche Vergleichsvergütung. Der **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) entwirft die Vereinbarung mit allen Pflichthinweisen und stellt die Vergleichsrechnung auf. Der **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) arbeitet die Formcheckliste Punkt für Punkt ab und prüft berufsrechtliche Grenzen sowie die AGB-Kontrolle.

## Ablauf

### 1. Formanforderungen der Vergütungsvereinbarung ([§ 3a Abs. 1 RVG](https://www.gesetze-im-internet.de/rvg/__3a.html))

Vier kumulative Anforderungen, jede für sich Wirksamkeitsvoraussetzung:

1. **Textform** ([§ 126b BGB](https://www.gesetze-im-internet.de/bgb/__126b.html)) — Schriftform ist nicht erforderlich, E-Mail genügt; mündliche Absprachen genügen nie.
2. **Bezeichnung** als „Vergütungsvereinbarung" oder in vergleichbarer Weise. „Mandatsbedingungen" oder „Honorarhinweis" erfüllen das nicht zuverlässig.
3. **Deutliche Absetzung** von anderen Vereinbarungen mit Ausnahme der Auftragserteilung; die Vereinbarung darf **nicht in der Vollmacht enthalten** sein.
4. **Hinweis**, dass die gegnerische Partei, ein Verfahrensbeteiligter oder die Staatskasse im Falle der Kostenerstattung regelmäßig **nicht mehr als die gesetzliche Vergütung** erstatten muss.

Für die Gebührenvereinbarung bei Beratung nach [§ 34 RVG](https://www.gesetze-im-internet.de/rvg/__34.html) gelten die Sätze 1 und 2 nicht (§ 3a Abs. 1 S. 4 RVG) — die reine Beratungsvergütung ist formfrei vereinbar, was in der Praxis regelmäßig verkannt wird.

### 2. Folgen des Formmangels ([§ 4b RVG](https://www.gesetze-im-internet.de/rvg/__4b.html))

Aus einer Vereinbarung, die der Form des § 3a Abs. 1 S. 1 und 2 RVG oder den Anforderungen des § 4a Abs. 1 und 3 Nr. 1 bis 3 RVG nicht entspricht, kann der Rechtsanwalt **keine höhere als die gesetzliche Vergütung** fordern. Die Vereinbarung ist also nicht insgesamt nichtig — sie wird auf die gesetzliche Vergütung gekappt. Bereits geleistete Zahlungen sind nach Bereicherungsrecht rückabzuwickeln, soweit sie die gesetzliche Vergütung übersteigen.

Praktische Konsequenz: Der Formmangel ist der erste Einwand jedes Mandanten im Honorarprozess. Die Vereinbarung ist deshalb so zu gestalten, dass jeder der vier Punkte des § 3a Abs. 1 RVG **äußerlich erkennbar** erfüllt ist.

### 3. Herabsetzung unangemessen hoher Vergütung ([§ 3a Abs. 3 RVG](https://www.gesetze-im-internet.de/rvg/__3a.html))

Auch die formwirksame Vereinbarung ist nicht unangreifbar: Eine unangemessen hohe Vergütung kann im Rechtsstreit auf den angemessenen Betrag herabgesetzt werden; vor der Herabsetzung ist ein **Gutachten des Vorstands der Rechtsanwaltskammer** einzuholen. Berufsrechtlich flankiert dies [§ 49b Abs. 1 BRAO](https://www.gesetze-im-internet.de/brao/__49b.html). Zeithonorare mit sehr hohen Stundensätzen oder ohne jede Obergrenze sind hier der typische Angriffspunkt.

### 4. Zeithonorar und Pauschalhonorar

Das **Zeithonorar** ist die praktisch häufigste Gestaltung. Wirksamkeit und Durchsetzbarkeit hängen an der Dokumentation: Der Anwalt trägt die Darlegungs- und Beweislast für die aufgewandte Zeit; eine Abrechnung ohne nachvollziehbare Tätigkeitsbeschreibung je Zeiteinheit ist im Honorarprozess regelmäßig nicht schlüssig `[unverifiziert – prüfen]`. Zu regeln sind daher: Stundensatz je Bearbeiterebene, Abrechnungstakt, Reisezeiten, Auslagen, Zwischenabrechnung und Vorschüsse ([§ 9 RVG](https://www.gesetze-im-internet.de/rvg/__9.html)).

Das **Pauschalhonorar** setzt eine präzise Leistungsbeschreibung voraus; ohne sie ist bei Mandatserweiterung streitig, was abgegolten ist. Bei Verbrauchermandanten unterliegen vorformulierte Klauseln der AGB-Kontrolle nach §§ 305 ff. BGB.

### 5. Erfolgshonorar ([§ 4a RVG](https://www.gesetze-im-internet.de/rvg/__4a.html))

Seit der Neufassung 2021 ist das Erfolgshonorar zulässig, aber nur in engen Konstellationen. Nach § 4a Abs. 1 RVG darf es vereinbart werden, wenn

- sich der Auftrag auf eine **Geldforderung von höchstens 2.000 EUR** bezieht,
- eine **außergerichtliche Inkassodienstleistung** erbracht wird, oder
- der Auftraggeber ohne die Vereinbarung **bei verständiger Betrachtung von der Rechtsverfolgung abgehalten würde**.

Die Möglichkeit, Prozesskostenhilfe in Anspruch zu nehmen, bleibt bei dieser Beurteilung **außer Betracht**. Nach § 4a Abs. 2 RVG darf zudem vereinbart werden, dass im Misserfolgsfall keine oder eine geringere Vergütung anfällt, **wenn für den Erfolgsfall ein angemessener Zuschlag auf die gesetzliche Vergütung vereinbart wird**.

§ 4a Abs. 3 RVG verlangt zusätzliche Angaben in der Vereinbarung: die voraussichtliche gesetzliche Vergütung, gegebenenfalls die erfolgsunabhängige vertragliche Vergütung, den Einfluss der Vereinbarung auf Gerichtskosten und Kostenerstattung sowie die wesentlichen Gründe für die Bemessung des Erfolgsanteils. Fehlen diese Angaben, greift wiederum § 4b RVG.

### 6. Unterschreitung der gesetzlichen Gebühren ([§ 4 RVG](https://www.gesetze-im-internet.de/rvg/__4.html))

In **außergerichtlichen** Angelegenheiten kann eine niedrigere als die gesetzliche Vergütung vereinbart werden; sie muss in einem angemessenen Verhältnis zu Leistung, Verantwortung und Haftungsrisiko stehen. In **gerichtlichen** Verfahren ist die Unterschreitung unzulässig ([§ 49b Abs. 1 BRAO](https://www.gesetze-im-internet.de/brao/__49b.html)) — ein Verstoß ist berufsrechtlich sanktioniert und wettbewerbsrechtlich angreifbar.

### 7. Formulierungshilfe — Vergütungsvereinbarung (Zeithonorar)

```
VERGÜTUNGSVEREINBARUNG
(gesondertes Dokument — nicht Bestandteil der Vollmacht)

zwischen  <Mandant, Anschrift>            — Auftraggeber —
und       <Kanzlei, Anschrift>            — Rechtsanwalt —

§ 1  Gegenstand
     Der Rechtsanwalt wird beauftragt mit <präzise Beschreibung>.

§ 2  Vergütung
     (1) Die Vergütung bemisst sich nach dem Zeitaufwand.
         Der Stundensatz beträgt <…> EUR zzgl. Umsatzsteuer.
         Bearbeiterstufen: <Partner …, Associate …>.
     (2) Abgerechnet wird im Takt von <…> Minuten. Reisezeit wird
         mit <…> % des Stundensatzes berechnet.
     (3) Auslagen werden nach VV Teil 7 RVG gesondert berechnet.

§ 3  Vorschuss
     Der Rechtsanwalt kann nach § 9 RVG Vorschüsse anfordern.

§ 4  Abrechnung und Fälligkeit
     Abgerechnet wird monatlich unter Angabe der Tätigkeiten je
     Zeiteinheit. Die Vergütung wird nach § 8 RVG fällig.

§ 5  Hinweis nach § 3a Abs. 1 S. 3 RVG
     Der Auftraggeber wird darauf hingewiesen, dass die gegnerische
     Partei, ein anderer Verfahrensbeteiligter oder die Staatskasse
     im Falle der Kostenerstattung regelmäßig NICHT MEHR ALS DIE
     GESETZLICHE VERGÜTUNG erstatten muss. Die Differenz zwischen
     dieser Vereinbarung und der gesetzlichen Vergütung trägt der
     Auftraggeber auch dann, wenn er obsiegt.

§ 6  Vergleichsrechnung
     Die gesetzliche Vergütung beträgt bei einem Gegenstandswert von
     <…> EUR voraussichtlich <…> EUR brutto (siehe Anlage).

<Ort, Datum>     <Auftraggeber>          <Rechtsanwalt>
```

## Deterministische Berechnung

Die Vergleichsrechnung nach § 6 des Musters muss die **gesetzliche Vergütung** ausweisen, damit der Mandant die Differenz beurteilen kann. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) liefert diesen Vergleichswert deterministisch. **Der Gegenstandswert und — bei Rahmengebühren — die Bestimmung des Satzes nach § 14 RVG bleiben juristische Wertungen** und sind Eingabe; die vereinbarte Vergütung selbst rechnet der Rechner nicht.

```bash
# Vergleichsmaßstab: gesetzliche Geschäftsgebühr VV 2300 bei 12.000 EUR
python -m scripts.legal_calc.cli rvg --wert 12000 --posten geschaeft
```

```
RVG-Berechnung (Gegenstandswert 12,000.00 EUR, Tabelle Stand 2025-06-01)
  1,0-Gebühr: 707.00 EUR
  Geschäftsgebühr VV 2300 (1.3): 919.10 EUR
  Zwischensumme Gebühren: 919.10 EUR
  Auslagenpauschale VV 7002: 20.00 EUR
  Netto: 939.10 EUR
  USt VV 7008 (19%): 178.43 EUR
  Gesamt (brutto): 1,117.53 EUR
```

```bash
# Vergleichsmaßstab für den gerichtlichen Teil desselben Mandats
python -m scripts.legal_calc.cli rvg --wert 12000 --posten verfahren termin
```

```
RVG-Berechnung (Gegenstandswert 12,000.00 EUR, Tabelle Stand 2025-06-01)
  1,0-Gebühr: 707.00 EUR
  Verfahrensgebühr VV 3100 (1.3): 919.10 EUR
  Terminsgebühr VV 3104 (1.2): 848.40 EUR
  Zwischensumme Gebühren: 1,767.50 EUR
  Auslagenpauschale VV 7002: 20.00 EUR
  Netto: 1,787.50 EUR
  USt VV 7008 (19%): 339.62 EUR
  Gesamt (brutto): 2,127.12 EUR
```

Ergibt der Zeitaufwand ein Vielfaches dieses Betrages, ist das für sich genommen zulässig — die Grenze zieht erst § 3a Abs. 3 RVG (Herabsetzung einer unangemessen hohen Vergütung). Die Vergleichsrechnung ist mit Datum und Tabellenstand zur Handakte zu nehmen: Sie ist im Honorarprozess der Beleg dafür, dass der Mandant über die Größenordnung der Differenz informiert war. Die Zeile `Tabelle Stand 2025-06-01` nennt die Version der hinterlegten Gebührentabelle; sie ist vor jeder mandantengerichteten Verwendung gegen die aktuelle Anlage 2 zu § 13 RVG zu prüfen.

## Quellen

### Statute

- [§ 3a RVG](https://www.gesetze-im-internet.de/rvg/__3a.html), [§ 4 RVG](https://www.gesetze-im-internet.de/rvg/__4.html), [§ 4a RVG](https://www.gesetze-im-internet.de/rvg/__4a.html), [§ 4b RVG](https://www.gesetze-im-internet.de/rvg/__4b.html)
- [§ 8 RVG](https://www.gesetze-im-internet.de/rvg/__8.html), [§ 9 RVG](https://www.gesetze-im-internet.de/rvg/__9.html), [§ 10 RVG](https://www.gesetze-im-internet.de/rvg/__10.html), [§ 34 RVG](https://www.gesetze-im-internet.de/rvg/__34.html)
- [§ 49b BRAO](https://www.gesetze-im-internet.de/brao/__49b.html), [§ 126b BGB](https://www.gesetze-im-internet.de/bgb/__126b.html), [§ 305 BGB](https://www.gesetze-im-internet.de/bgb/__305.html), [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html)

### Kommentare

- Gerold / Schmidt, RVG, 26. Aufl. 2023, § 3a Rn. 1 ff. (Form, deutliche Absetzung)
- Mayer / Kroiß, RVG, 8. Aufl. 2021, § 4a Rn. 1 ff. (Erfolgshonorar nach der Neufassung 2021)
- Hartmann / Toussaint, Kostenrecht, 54. Aufl. 2024, § 4b RVG Rn. 1 ff.
- Kilian, in: Kilian / Offermann-Burckart / vom Stein, Praxishandbuch Anwaltsrecht, 3. Aufl. 2021, § 14 (Vergütungsvereinbarung)

### Rechtsprechung

- Rechtsprechung zu den Anforderungen an die Darlegung des Zeitaufwands bei Zeithonorarabrechnungen `[unverifiziert – prüfen]`
- Rechtsprechung zur „deutlichen Absetzung" im Sinne des § 3a Abs. 1 S. 2 RVG bei Kombination mit Mandatsbedingungen `[unverifiziert – prüfen]`

> Fundstellen sind vor Verwendung in juris, Beck-Online oder AGS/RVGreport zu ermitteln.

## Ausgabeformat

```
VERGÜTUNGSVEREINBARUNG — <Mandat-ID> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

I.    Modell                        [Zeithonorar / Pauschale /
                                     Multiplikator / Erfolgshonorar]
II.   Formcheck § 3a Abs. 1 RVG
      Textform § 126b BGB           [🟢 / 🔴]
      Als Vergütungsvereinbarung
      bezeichnet                    [🟢 / 🔴]
      Deutlich abgesetzt            [🟢 / 🔴]
      Nicht in der Vollmacht        [🟢 / 🔴]
      Erstattungshinweis S. 3       [🟢 / 🔴]
III.  Erfolgshonorar § 4a RVG       [N/A / zulässig nach Abs. 1 Nr. <…>]
      Pflichtangaben Abs. 3         [🟢 / 🔴 <fehlend>]
IV.   Unterschreitung § 4 RVG       [N/A / außergerichtlich zulässig /
                                     🔴 gerichtlich unzulässig § 49b BRAO]
V.    Vergleichsrechnung            gesetzlich <…> EUR brutto
      Vereinbart voraussichtlich    <…> EUR
      Angemessenheit § 3a Abs. 3    [🟢 / 🟡 Herabsetzungsrisiko]
VI.   AGB-Kontrolle §§ 305 ff. BGB  [N/A Individualvereinbarung / geprüft]
VII.  Abrechnung                    [§ 8 RVG Fälligkeit, § 10 RVG Form]

Folge bei Formmangel: § 4b RVG — nur die gesetzliche Vergütung.
Empfehlung: <…>
```

## Risiken / typische Fehler

- **Vergütungsvereinbarung in der Vollmacht** oder auf demselben Blatt wie die Mandatsbedingungen — Verstoß gegen § 3a Abs. 1 S. 2 RVG, Folge: § 4b RVG.
- **Erstattungshinweis nach § 3a Abs. 1 S. 3 RVG fehlt.** Der Hinweis auf die begrenzte Kostenerstattung ist Pflichtbestandteil, kein Serviceelement.
- **Nur mündliche Absprache über den Stundensatz** — Textform ist zwingend, § 126b BGB.
- **Erfolgshonorar ohne Prüfung des § 4a Abs. 1 RVG vereinbart.** Die Wertgrenze von 2.000 EUR, die außergerichtliche Inkassodienstleistung und das Abhalten von der Rechtsverfolgung sind abschließend; die Möglichkeit der Prozesskostenhilfe bleibt außer Betracht.
- **Pflichtangaben des § 4a Abs. 3 RVG weggelassen** — mit derselben Rechtsfolge wie ein Formmangel.
- **Gebührenunterschreitung im gerichtlichen Verfahren** entgegen § 4 RVG und § 49b Abs. 1 BRAO.
- **Zeithonorar ohne Tätigkeitsdokumentation je Zeiteinheit** — im Honorarprozess regelmäßig nicht schlüssig darlegbar.
- **Keine Vergleichsrechnung zur gesetzlichen Vergütung** zur Handakte genommen; im Streit über die Angemessenheit nach § 3a Abs. 3 RVG fehlt damit der Beleg der Aufklärung.
- **Abrechnung ohne die Angaben des § 10 RVG** oder vor Fälligkeit nach § 8 RVG eingefordert.
