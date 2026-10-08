---
name: musterfeststellungsklage-vdug-borghei
title: /verbandsklage-vdug:musterfeststellungsklage-vdug
description: Musterfeststellungsklage nach § 41 VDuG – Feststellung des Vorliegens oder Nichtvorliegens tatsächlicher und rechtlicher Voraussetzungen für das Bestehen oder Nichtbestehen von Ansprüchen oder Rechtsverhältnissen (Feststellungsziele), Wahlfreiheit gegenüber der Abhilfeklage § 41 Abs. 2, Verbraucherquorum § 4 Abs. 1 Nr. 2, Bindungswirkung rechtskräftiger Urteile für den Folgeprozess des angemeldeten Verbrauchers § 11 Abs. 3 mit der Ausnahme für Abhilfeendurteile, Aussetzung anhängiger Individualklagen § 11 Abs. 1, Klageverbot für angemeldete Verbraucher § 11 Abs. 2, Sperrwirkung § 8, Revision § 42 sowie die Abgrenzung zum KapMuG-Musterverfahren § 1 Abs. 3. Use when Feststellungsziele zu formulieren, eine Musterfeststellungsklage abzuwehren oder die Wirkung eines Musterurteils auf Individualprozesse zu bestimmen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verbandsklage-vdug/skills/musterfeststellungsklage-vdug
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /verbandsklage-vdug:musterfeststellungsklage-vdug

## Zweck

Der Skill formuliert und prüft Feststellungsziele und bestimmt, was ein rechtskräftiges Musterurteil im nachfolgenden Individualprozess tatsächlich bindet. Er trennt dabei die drei Wirkungsebenen des § 11 VDuG, die in der Praxis regelmäßig vermengt werden: Aussetzung, Klageverbot und Bindungswirkung.

## Eingaben

- Lebenssachverhalt und die streitige Vorfrage (Klauselwirksamkeit, Aufklärungspflicht, Mangelhaftigkeit, Verstoßqualität)
- Entwurf der Feststellungsziele
- Ob die klageberechtigte Stelle auch Abhilfeklage erheben könnte
- Anhängige Individualklagen betroffener Verbraucher und deren Verfahrensstand
- Ob und wann die Verbandsklage im Verbandsklageregister bekannt gemacht wurde
- Ob Verbraucher bereits angemeldet sind

## Sub-Agent-Architektur

Der Researcher beschafft VDuG, ZPO, KapMuG und die Registerpraxis des Bundesamts für Justiz. Der Drafter formuliert die Feststellungsziele so, dass sie im Folgeprozess tragen, oder greift sie auf Beklagtenseite als zu unbestimmt an. Der Reviewer prüft die Reichweite der Bindungswirkung und insbesondere, ob die Ausnahme des § 11 Abs. 3 S. 2 beachtet ist.

## Ablauf

### 1. Klageziel bestimmen ([§ 41 VDuG](https://www.gesetze-im-internet.de/vdug/__41.html))

Mit der Musterfeststellungsklage begehrt die klageberechtigte Stelle die **Feststellung des Vorliegens oder Nichtvorliegens von tatsächlichen und rechtlichen Voraussetzungen für das Bestehen oder Nichtbestehen von Ansprüchen oder Rechtsverhältnissen** zwischen Verbrauchern und einem Unternehmer — den **Feststellungszielen**.

**§ 41 Abs. 2**: Der Zulässigkeit steht **nicht** entgegen, dass die klageberechtigte Stelle auch **Abhilfeklage erheben könnte**. Es gibt keinen Vorrang der Leistungsklage; die Wahl liegt bei der klagenden Stelle.

Wann die Musterfeststellungsklage der Abhilfeklage vorzuziehen ist:

| Konstellation | Geeignete Klageart |
|---|---|
| Anspruchshöhe individuell sehr unterschiedlich, Vorfrage aber einheitlich | **Musterfeststellungsklage** |
| Ansprüche im Wesentlichen gleichartig und bezifferbar | **Abhilfeklage** (`/verbandsklage-vdug:abhilfeklage-vdug`) |
| Streit allein über Wirksamkeit einer Klausel oder Bestehen einer Pflicht | **Musterfeststellungsklage** |
| Ziel ist unmittelbare Auszahlung ohne Folgeprozesse | **Abhilfeklage** mit kollektivem Gesamtbetrag |

### 2. Feststellungsziele formulieren

Ein Feststellungsziel muss **so bestimmt** sein, dass das Folgegericht es ohne erneute Sachprüfung anwenden kann. Brauchbare Ziele betreffen typischerweise:

- die **Unwirksamkeit einer konkret bezeichneten Klausel** in einer konkret bezeichneten Fassung;
- das **Bestehen einer Aufklärungs-, Informations- oder Hinweispflicht** in einer bestimmten Vertriebssituation;
- die **Zurechnung eines Verhaltens** zum Unternehmer;
- das Vorliegen eines **Verstoßes** gegen eine benannte Norm.

Untaugliche Ziele sind solche, die die Anspruchsberechtigung des einzelnen Verbrauchers voraussetzen (Kausalität, Kenntnis, Schadenshöhe) — sie sind dem Individualprozess vorbehalten und machen das Ziel im Folgeprozess wertlos. Auf Beklagtenseite ist genau hier anzusetzen: **Unbestimmtheit und Individualitätsbezug** der Feststellungsziele.

Zulässigkeitsvoraussetzung bleibt das **Quorum**: Nach [§ 4 Abs. 1 Nr. 2 VDuG](https://www.gesetze-im-internet.de/vdug/__4.html) müssen von den Feststellungszielen die Ansprüche oder Rechtsverhältnisse von **mindestens 50 Verbrauchern** abhängen können (`/verbandsklage-vdug:verbandsklage-zulaessigkeit`).

### 3. Die drei Wirkungen des [§ 11 VDuG](https://www.gesetze-im-internet.de/vdug/__11.html) auseinanderhalten

| Absatz | Wirkung | Voraussetzung | Folge |
|---|---|---|---|
| **Abs. 1** | **Aussetzung** | Verbraucher hat **vor** der Bekanntgabe der Verbandsklage im Register Individualklage erhoben **und** meldet seinen Anspruch zum Register an | Das Gericht **setzt aus** bis zur rechtskräftigen Entscheidung, sonstigen Erledigung oder wirksamen Rücknahme der Anmeldung |
| **Abs. 2** | **Klageverbot** | Verbraucher ist **angemeldet**, Verbandsklage ist **rechtshängig** | Er **kann keine** Klage über denselben Lebenssachverhalt und dieselben Ansprüche oder Feststellungsziele erheben |
| **Abs. 3** | **Bindungswirkung** | **rechtskräftiges Urteil** über die Verbandsklage | Es **bindet** das Gericht im Rechtsstreit zwischen **angemeldetem** Verbraucher und verklagtem Unternehmer, soweit die Entscheidung den Lebenssachverhalt und ein geltend gemachtes Feststellungsziel bzw. einen mit der Abhilfeklage geltend gemachten Anspruch betrifft |

**Die Ausnahme, die in der Praxis übersehen wird: § 11 Abs. 3 S. 2 — Satz 1 gilt _nicht_ für Abhilfeendurteile nach § 18.** Die Bindungswirkung des Musterurteils ist damit ein Spezifikum der Feststellungs- und Grundurteilsebene; das Abhilfeendurteil wirkt über das Umsetzungsverfahren, nicht über eine Bindung im Folgeprozess.

Ebenso wichtig: Die Wirkungen des § 11 setzen die **Anmeldung** voraus. Wer sich nicht anmeldet, ist weder gebunden noch begünstigt und behält seine Individualklage — trägt aber auch das volle Prozessrisiko (`/verbandsklage-vdug:anmeldung-umsetzungsverfahren`).

### 4. Verhältnis zu anderen Verfahren

- **Weitere Verbandsklagen**: [§ 8 VDuG](https://www.gesetze-im-internet.de/vdug/__8.html) sperrt ab **Anhängigkeit** eine zweite Verbandsklage zum selben Lebenssachverhalt mit denselben Feststellungszielen; die Sperre entfällt bei Beendigung ohne Sachentscheidung.
- **KapMuG**: Nach [§ 1 Abs. 3 VDuG](https://www.gesetze-im-internet.de/vdug/__1.html) hindert ein eröffnetes Musterverfahren nach dem [KapMuG](https://www.gesetze-im-internet.de/kapmug_2012/) die Verbandsklage **nicht**. Bei Kapitalanlegerstreitigkeiten können beide Wege nebeneinander bestehen; die Abgrenzung ist im Mandat ausdrücklich zu treffen.
- **Unterlassungsklagen** nach dem [UKlaG](https://www.gesetze-im-internet.de/uklag/) bleiben daneben möglich — sie zielen auf Unterlassung der Klauselverwendung, nicht auf Feststellung für Verbraucheransprüche.
- **Verjährung**: Die Anmeldung zum Verbandsklageregister wirkt sich auf die Verjährung der angemeldeten Ansprüche aus; die einschlägige Hemmungsnorm ist im konkreten Fall zu benennen und zu belegen `[unverifiziert – prüfen]`.

### 5. Rechtsmittel ([§ 42 VDuG](https://www.gesetze-im-internet.de/vdug/__42.html))

Gegen Urteile über die Musterfeststellungsklage findet die **Revision** statt. Da erstinstanzlich das Oberlandesgericht entscheidet (§ 3 Abs. 1 VDuG), führt der Rechtsmittelzug unmittelbar zum BGH; eine Berufungsinstanz gibt es nicht.

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# Anmeldefrist § 46 Abs. 1 VDuG: 3 Wochen nach Schluss der mündlichen Verhandlung,
# § 193 BGB ausdrücklich nicht anwendbar
python -m scripts.legal_calc.cli frist --ereignis 14.03.2026 --menge 3 --einheit wochen --land BY --kein-rollover

# Revisionsfrist § 548 ZPO: 1 Monat ab Zustellung
python -m scripts.legal_calc.cli frist --ereignis 20.05.2026 --menge 1 --einheit monate --land BY

# Regelverjährung des Individualanspruchs, falls die Anmeldung unterbleibt
python -m scripts.legal_calc.cli verjaehrung --entstehung 05.02.2023 --kenntnis 05.02.2023
```

## Quellen

### Statute

- [§ 1 VDuG](https://www.gesetze-im-internet.de/vdug/__1.html), [§ 3](https://www.gesetze-im-internet.de/vdug/__3.html), [§ 4 VDuG](https://www.gesetze-im-internet.de/vdug/__4.html), [§ 8](https://www.gesetze-im-internet.de/vdug/__8.html), [§ 11](https://www.gesetze-im-internet.de/vdug/__11.html), [§ 18 VDuG](https://www.gesetze-im-internet.de/vdug/__18.html), [§ 41](https://www.gesetze-im-internet.de/vdug/__41.html), [§ 42](https://www.gesetze-im-internet.de/vdug/__42.html), [§ 46 VDuG](https://www.gesetze-im-internet.de/vdug/__46.html)
- [§ 548 ZPO](https://www.gesetze-im-internet.de/zpo/__548.html), [§ 204 BGB](https://www.gesetze-im-internet.de/bgb/__204.html)
- [KapMuG](https://www.gesetze-im-internet.de/kapmug_2012/), [UKlaG](https://www.gesetze-im-internet.de/uklag/)
- Richtlinie (EU) 2020/1828 — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2020/1828/oj)

### Kommentare und Literatur

- Röthemeyer, VDuG, Kommentar, § 11, § 41.
- Nordholtz/Mekat, Musterfeststellungsklage und Verbandsklage, Kap. Feststellungsziele.
- Stadler, Kollektiver Rechtsschutz, Beiträge 2024–2026 (Fundstelle vor Verwendung prüfen) `[unverifiziert – prüfen]`

### Rechtsprechung

Zur alten Musterfeststellungsklage nach §§ 606 ff. ZPO a. F. besteht Rechtsprechung, die auf das VDuG nur eingeschränkt übertragbar ist — die Bindungswirkung ist neu geordnet. Zum VDuG selbst ergehen seit 2025/2026 erste obergerichtliche Entscheidungen. Jede Entscheidung ist vor Verwendung in juris oder Beck-Online zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
MUSTERFESTSTELLUNGSKLAGE — <Mandat> — <Datum>

I.   Klagewahl
     Ziel:                    <Vorfrage>
     Abhilfeklage möglich:    [ja — § 41 Abs. 2 steht nicht entgegen / nein]
     Begründung der Wahl:     <…>

II.  Feststellungsziele
     Ziel 1:                  <Wortlautvorschlag>
     Ziel n:                  <…>
     Bestimmtheit:            [tragfähig / zu unbestimmt]
     Individualitätsbezug:    [frei / enthält Kausalität, Kenntnis oder Höhe — angreifbar]
     Quorum § 4 Abs. 1 Nr. 2: [mindestens 50 abhängige Verbraucher dargelegt / nein]

III. Wirkungen § 11
     Abs. 1 Aussetzung:       <anhängige Individualklagen, Registerbekanntgabe am <Datum>>
     Abs. 2 Klageverbot:      <angemeldete Verbraucher>
     Abs. 3 Bindungswirkung:  <Reichweite>
       Ausnahme S. 2:         Abhilfeendurteile nach § 18 binden nicht

IV.  Verhältnis zu anderen Verfahren
     § 8 Sperrwirkung:        [greift / greift nicht]
     KapMuG § 1 Abs. 3:       [parallel zulässig]
     UKlaG-Unterlassung:      [daneben möglich]
     Verjährung / Anmeldung:  <Bewertung>

V.   Rechtsmittel
     Erstinstanz OLG § 3 Abs. 1 → Revision § 42 zum BGH, Frist bis <Datum>

VI.  Empfehlung
VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

## Risiken / typische Fehler

- **Bindungswirkung auf Abhilfeendurteile erstreckt.** § 11 Abs. 3 S. 2 VDuG nimmt sie ausdrücklich aus.
- **Wirkungen des § 11 ohne Anmeldung angenommen.** Aussetzung, Klageverbot und Bindung setzen die Anmeldung zum Verbandsklageregister voraus.
- **Feststellungsziele mit Individualmerkmalen befrachtet.** Kausalität, Kenntnis und Schadenshöhe gehören in den Folgeprozess; im Ziel machen sie es wertlos.
- **Vorrang der Abhilfeklage unterstellt.** § 41 Abs. 2 VDuG stellt klar, dass es ihn nicht gibt.
- **Berufung eingelegt.** Erstinstanzlich entscheidet das OLG; statthaft ist die Revision nach § 42 VDuG.
- **Quorum der Musterfeststellungsklage mit dem der Abhilfeklage verwechselt** — § 4 Abs. 1 Nr. 2 VDuG knüpft an die Abhängigkeit von den Feststellungszielen an.
- **KapMuG als Sperre behandelt** — § 1 Abs. 3 VDuG sagt das Gegenteil.
- **Verjährungsfolgen der Anmeldung nicht geprüft** und dem Mandanten nicht erläutert.
- **Rechtsprechung zur alten Musterfeststellungsklage unbesehen übertragen.** Die Bindungswirkung ist im VDuG neu geordnet.
- **Rechtsprechung erfunden.** Jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
