---
name: aufhebungsantrag-1059-borghei
title: /schiedsverfahren-adr:aufhebungsantrag-1059
description: Aufhebung eines Schiedsspruchs nach § 1059 ZPO – abschließender Katalog der Aufhebungsgründe Abs. 2 mit den vier Rügegründen Nr. 1 lit. a bis d (Unwirksamkeit der Schiedsvereinbarung, Gehörsverletzung, Überschreitung der Schiedsvereinbarung mit Teilaufhebung, fehlerhafte Bildung oder Verfahrensführung mit Kausalitätserfordernis) und den beiden von Amts wegen zu prüfenden Gründen Nr. 2 (fehlende Schiedsfähigkeit, ordre public), Dreimonatsfrist ab Empfang des Schiedsspruchs Abs. 3 mit Verlängerung um höchstens einen Monat nach einem Antrag nach § 1058, Sperre nach Vollstreckbarerklärung, Zurückverweisung Abs. 4 und Wiederaufleben der Schiedsvereinbarung Abs. 5, dazu OLG-Zuständigkeit § 1062, Verfahren § 1063 und Rechtsbeschwerde § 1065. Use when ein Schiedsspruch angegriffen oder ein Aufhebungsantrag abgewehrt werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/schiedsverfahren-adr/skills/aufhebungsantrag-1059
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: arbitration
language: de
---

# /schiedsverfahren-adr:aufhebungsantrag-1059

## Zweck

Der Skill prüft, ob ein Schiedsspruch angreifbar ist, und entwirft den Aufhebungsantrag oder dessen Abwehr. Er hält die entscheidende Grenze durch: Das Aufhebungsverfahren ist **keine zweite Tatsacheninstanz**. Eine inhaltlich falsche Rechtsanwendung ist kein Aufhebungsgrund; angreifbar sind nur die im Katalog des § 1059 Abs. 2 ZPO abschließend benannten Mängel.

## Eingaben

- Schiedsspruch im Wortlaut mit Datum des Erlasses und Datum des **Empfangs** durch den Mandanten
- Schiedsvereinbarung und Verfahrensordnung
- Verfahrensakte: Rügen, Protokolle, Beweisbeschlüsse, Schriftsatzfristen
- Ob ein Antrag nach § 1058 ZPO gestellt wurde und wann darüber entschieden wurde
- Ob bereits ein Antrag auf Vollstreckbarerklärung anhängig oder beschieden ist
- Schiedsort (bestimmt das zuständige OLG) und Sitz des Antragsgegners

## Sub-Agent-Architektur

Der Researcher beschafft die Normen, die Rechtsprechung des BGH und der Oberlandesgerichte zum ordre public und zur Gehörsrüge sowie die Kommentarliteratur. Der Drafter ordnet jeden Mangel einem Katalogtatbestand zu und formuliert den Antrag. Der Reviewer prüft zuerst die Dreimonatsfrist, dann die Präklusion nicht gerügter Verfahrensfehler, dann ob der Vortrag in Wahrheit auf eine révision au fond hinausläuft.

> **Hinweis zum Rechtsstand.** Das Zehnte Buch der ZPO ist Gegenstand des Gesetzes vom 20.05.2026 (BGBl. 2026 I Nr. 152); die Änderungen sind auf gesetze-im-internet.de textlich nachgewiesen, dokumentarisch aber noch nicht abschließend eingearbeitet. Der konsolidierte Stand ist gegen das Bundesgesetzblatt abzugleichen `[unverifiziert – prüfen]`.

## Ablauf

### 1. Frist zuerst rechnen ([§ 1059 Abs. 3 ZPO](https://www.gesetze-im-internet.de/zpo/__1059.html))

**Dieser Schritt steht vor allem anderen.**

- Der Aufhebungsantrag muss, sofern die Parteien nichts anderes vereinbaren, innerhalb von **drei Monaten** bei Gericht eingereicht werden.
- Die Frist beginnt mit dem Tag, an dem der Antragsteller den Schiedsspruch **empfangen** hat — nicht mit dem Erlassdatum nach § 1054 Abs. 3.
- Ist ein Antrag nach [§ 1058 ZPO](https://www.gesetze-im-internet.de/zpo/__1058.html) (Berichtigung, Auslegung, Ergänzung) gestellt worden, verlängert sich die Frist um **höchstens einen Monat** nach Empfang der Entscheidung über diesen Antrag.
- **Sperre**: Der Aufhebungsantrag kann **nicht mehr** gestellt werden, wenn der Schiedsspruch von einem deutschen Gericht **für vollstreckbar erklärt** worden ist.

Umgekehrt bestimmt [§ 1060 Abs. 2 S. 3 ZPO](https://www.gesetze-im-internet.de/zpo/__1060.html): Im Vollstreckbarerklärungsverfahren sind Aufhebungsgründe nach § 1059 Abs. 2 **Nr. 1** nicht mehr zu berücksichtigen, wenn die Fristen des Abs. 3 abgelaufen sind, ohne dass ein Aufhebungsantrag gestellt wurde. **Wer die drei Monate verstreichen lässt, verliert seine Rügegründe auch als Verteidigung** — die Gründe der Nr. 2 bleiben davon unberührt.

### 2. Aufhebungsgründe zuordnen ([§ 1059 Abs. 2 ZPO](https://www.gesetze-im-internet.de/zpo/__1059.html))

Der Katalog ist **abschließend**. Er zerfällt in zwei Gruppen:

**Nr. 1 — nur auf begründete Geltendmachung des Antragstellers:**

| lit. | Tatbestand | Praxispunkt |
|---|---|---|
| a | Partei war nach ihrem Personalstatut nicht fähig, die Schiedsvereinbarung zu schließen, **oder** die Schiedsvereinbarung ist nach dem gewählten Recht, hilfsweise nach deutschem Recht, **ungültig** | Anknüpfung an §§ 1029, 1031; typischer Fall: Formverstoß nach § 1031 Abs. 5 |
| b | Der Antragsteller wurde von der Bestellung eines Schiedsrichters oder vom Verfahren **nicht gehörig in Kenntnis gesetzt** oder konnte aus anderem Grund seine **Angriffs- oder Verteidigungsmittel nicht geltend machen** | Der Gehörsgrund; setzt regelmäßig die rechtzeitige Rüge im Schiedsverfahren voraus |
| c | Der Schiedsspruch betrifft eine **nicht von der Schiedsvereinbarung erfasste** Streitigkeit oder überschreitet deren Grenzen | **Teilaufhebung**, wenn der erfasste Teil abtrennbar ist |
| d | **Bildung des Schiedsgerichts oder Verfahren** entsprachen einer Bestimmung des Zehnten Buchs oder einer zulässigen Parteivereinbarung nicht **und es ist anzunehmen, dass sich dies auf den Schiedsspruch ausgewirkt hat** | **Kausalitätserfordernis** — der Vortrag muss die Auswirkung darlegen |

**Nr. 2 — von Amts wegen festzustellen:**

| lit. | Tatbestand |
|---|---|
| a | Der **Streitgegenstand ist nach deutschem Recht nicht schiedsfähig** (§ 1030) |
| b | Anerkennung oder Vollstreckung führt zu einem Ergebnis, das der **öffentlichen Ordnung (ordre public)** widerspricht |

Der **ordre public** ist eng auszulegen. Er erfasst Verstöße gegen elementare Grundsätze der Rechtsordnung — etwa gravierende Verfahrensverstöße, Verstöße gegen zwingendes Kartellrecht oder gegen Grundrechte —, **nicht** die schlichte Fehlanwendung materiellen Rechts. Die Abgrenzung ist im Antrag zu begründen und nicht zu behaupten; die einschlägige BGH-Rechtsprechung ist heranzuziehen und zu verifizieren `[unverifiziert – prüfen]`.

### 3. Präklusion prüfen

Zwei Präklusionsebenen greifen ineinander:

1. **Verfahrensinterne Präklusion.** Wer einen Verfahrensfehler oder die Unzuständigkeit im Schiedsverfahren nicht rechtzeitig rügt — Zuständigkeit spätestens mit der Klagebeantwortung nach [§ 1040 Abs. 2 ZPO](https://www.gesetze-im-internet.de/zpo/__1040.html), Gehörsverstöße unverzüglich —, kann sich darauf im Aufhebungsverfahren regelmäßig nicht mehr berufen.
2. **Fristpräklusion.** Der Ablauf der Dreimonatsfrist nach Abs. 3 sperrt die Gründe der Nr. 1 auch im Vollstreckbarerklärungsverfahren (§ 1060 Abs. 2 S. 3).

Ein Aufhebungsantrag, der ausschließlich mit im Schiedsverfahren nicht gerügten Verfahrensfehlern begründet wird, ist deshalb regelmäßig unbegründet.

### 4. Zuständigkeit und Verfahren ([§ 1062 ZPO](https://www.gesetze-im-internet.de/zpo/__1062.html), [§ 1063 ZPO](https://www.gesetze-im-internet.de/zpo/__1063.html))

- **Zuständig** ist das in der Schiedsvereinbarung bezeichnete **Oberlandesgericht**, sonst das OLG, in dessen Bezirk der Schiedsort liegt (§ 1062 Abs. 1 Nr. 4). Besteht kein deutscher Schiedsort, gilt § 1062 Abs. 2: OLG am Sitz oder gewöhnlichen Aufenthalt des Antragsgegners, hilfsweise am Vermögens- oder Gegenstandsort, äußerst hilfsweise das **Kammergericht**.
- **Verfahren** (§ 1063): Entscheidung durch **Beschluss**; der Gegner ist vorher zu hören. Das Gericht **hat mündliche Verhandlung anzuordnen**, wenn die Aufhebung beantragt wird oder wenn bei einem Antrag auf Anerkennung oder Vollstreckbarerklärung Aufhebungsgründe nach § 1059 Abs. 2 in Betracht kommen (Abs. 2). Der Vorsitzende kann ohne Anhörung des Gegners Sicherungsmaßnahmen zulassen (Abs. 3).
- **Rechtsmittel** (§ 1065): Gegen Entscheidungen nach § 1062 Abs. 1 Nr. 2 und Nr. 4 findet die **Rechtsbeschwerde** zum BGH statt; im Übrigen sind die Entscheidungen unanfechtbar. Die Rechtsbeschwerde kann auch auf die Verletzung eines Staatsvertrags gestützt werden.

### 5. Rechtsfolgen ([§ 1059 Abs. 4, 5 ZPO](https://www.gesetze-im-internet.de/zpo/__1059.html))

- **Abs. 4** — Das Gericht kann in geeigneten Fällen auf Antrag einer Partei unter Aufhebung des Schiedsspruchs die Sache an das **Schiedsgericht zurückverweisen**. Das ist der schonendere Weg gegenüber der ersatzlosen Aufhebung und sollte hilfsweise beantragt werden.
- **Abs. 5** — Die Aufhebung führt im Zweifel dazu, dass die **Schiedsvereinbarung wiederauflebt**. Wer den Streit nach der Aufhebung vor das staatliche Gericht bringen will, muss deshalb darlegen, warum die Schiedsvereinbarung ausnahmsweise nicht wiederauflebt — etwa weil sie gerade wegen Unwirksamkeit nach Abs. 2 Nr. 1 lit. a aufgehoben wurde.

### 6. Strategische Weichenstellung

| Ausgangslage | Empfehlung |
|---|---|
| Schiedsspruch belastet den Mandanten, Frist läuft | Aufhebungsantrag fristwahrend einreichen; Begründung nachreichen |
| Gegenseite hat Vollstreckbarerklärung beantragt | Aufhebungsgründe **im Vollstreckbarerklärungsverfahren** einwenden (§ 1060 Abs. 2) und zugleich Frist des § 1059 Abs. 3 wahren |
| Nur Rechenfehler oder Auslegungsbedarf | Antrag nach § 1058 ZPO — verlängert zugleich die Aufhebungsfrist |
| Fehler betrifft nur einen abtrennbaren Teil | **Teilaufhebung** nach Abs. 2 Nr. 1 lit. c beantragen |
| Verfahrensfehler heilbar | hilfsweise **Zurückverweisung** nach Abs. 4 beantragen |

## Deterministische Berechnung

Die Dreimonatsfrist ist die kritischste Frist des Gebiets. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik — der maßgebliche **Empfangstag** ist eine tatsächliche Feststellung und gesondert zu belegen:

```bash
# § 1059 Abs. 3 S. 1, 2 ZPO: 3 Monate ab Empfang des Schiedsspruchs am 20.11.2026
python -m scripts.legal_calc.cli frist --ereignis 20.11.2026 --menge 3 --einheit monate --land BY

# Verlängerung nach § 1059 Abs. 3 S. 3 ZPO: höchstens 1 Monat ab Empfang der § 1058-Entscheidung
python -m scripts.legal_calc.cli frist --ereignis 15.01.2027 --menge 1 --einheit monate --land BY

# § 1058 ZPO: 1 Monat für den Berichtigungs-, Auslegungs- oder Ergänzungsantrag
python -m scripts.legal_calc.cli frist --ereignis 20.11.2026 --menge 1 --einheit monate --land BY
```

`--json` liefert die Rechenschritte samt Normzitat.

## Quellen

### Statute

- [§ 1030](https://www.gesetze-im-internet.de/zpo/__1030.html), [§ 1040](https://www.gesetze-im-internet.de/zpo/__1040.html), [§ 1042](https://www.gesetze-im-internet.de/zpo/__1042.html), [§ 1054 ZPO](https://www.gesetze-im-internet.de/zpo/__1054.html), [§ 1058](https://www.gesetze-im-internet.de/zpo/__1058.html), [§ 1059](https://www.gesetze-im-internet.de/zpo/__1059.html), [§ 1060 ZPO](https://www.gesetze-im-internet.de/zpo/__1060.html), [§ 1062](https://www.gesetze-im-internet.de/zpo/__1062.html), [§ 1063](https://www.gesetze-im-internet.de/zpo/__1063.html), [§ 1065 ZPO](https://www.gesetze-im-internet.de/zpo/__1065.html)
- Art. 103 Abs. 1 GG (rechtliches Gehör als Maßstab des ordre public)

### Kommentare

- Zöller/Geimer, ZPO, § 1059.
- Musielak/Voit, ZPO, § 1059 Rn. 1 ff. (ordre public, Präklusion).
- Stein/Jonas/Schlosser, ZPO, § 1059.
- Schwab/Walter, Schiedsgerichtsbarkeit, Kap. Aufhebung.
- Prütting/Gehrlein, ZPO, § 1059, § 1063.

### Rechtsprechung

Zum ordre public, zur Gehörsrüge und zur Präklusion nicht gerügter Verfahrensfehler besteht gefestigte Rechtsprechung des BGH; sie ist im Einzelfall zu recherchieren. Jede konkrete Entscheidung ist vor Verwendung in juris, Beck-Online oder auf den Seiten des BGH zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
AUFHEBUNGSANTRAG § 1059 ZPO — <Mandat> — <Datum>

I.   Fristenlage
     Schiedsspruch erlassen am (§ 1054 Abs. 3):  <Datum>
     Empfangen am (§ 1059 Abs. 3 S. 2):          <Datum>
     Frist von 3 Monaten endet am:               <Datum>
     Antrag nach § 1058 gestellt:                [ja am <Datum> — Verlängerung bis <Datum> / nein]
     Vollstreckbarerklärung bereits erfolgt:     [ja — Antrag gesperrt / nein]

II.  Zuständigkeit und Verfahren
     Schiedsort:              <Ort>   → OLG <…> (§ 1062 Abs. 1 Nr. 4)
     Kein deutscher Schiedsort: <§ 1062 Abs. 2 — OLG <…> / KG>
     Mündliche Verhandlung § 1063 Abs. 2: zwingend
     Rechtsmittel § 1065:     Rechtsbeschwerde zum BGH

III. Aufhebungsgründe
     Nr. 1 lit. a Ungültigkeit:            [geltend gemacht — Begründung / nein]
     Nr. 1 lit. b Gehör:                   [ja — im Schiedsverfahren gerügt am <Datum> / nein]
     Nr. 1 lit. c Überschreitung:          [ja — Teilaufhebung möglich? / nein]
     Nr. 1 lit. d Bildung/Verfahren:       [ja — Kausalität dargelegt? / nein]
     Nr. 2 lit. a Schiedsfähigkeit:        [von Amts wegen — Feststellung]
     Nr. 2 lit. b ordre public:            [von Amts wegen — enge Auslegung, Begründung]

IV.  Präklusion
     Rügen im Schiedsverfahren:            <Übersicht mit Datum und Fundstelle>
     § 1040 Abs. 2 Zuständigkeitsrüge:     [rechtzeitig / verspätet]
     Folge:                                <…>

V.   Anträge
     1. Der Schiedsspruch vom <Datum> wird aufgehoben.
     2. Hilfsweise: Teilaufhebung hinsichtlich <…>.
     3. Hilfsweise: Aufhebung und Zurückverweisung an das Schiedsgericht (§ 1059 Abs. 4).
     4. Kosten.

VI.  Folgen der Aufhebung
     Wiederaufleben der Schiedsvereinbarung § 1059 Abs. 5: [ja / ausnahmsweise nein — Begründung]

VII. Abgrenzung
     Keine révision au fond — unrichtige Rechtsanwendung ist kein Aufhebungsgrund.

VIII.Risiko: 🟢 / 🟡 / 🔴 <Begründung>
IX.  Quellenverzeichnis
```

## Risiken / typische Fehler

- **Dreimonatsfrist ab Erlass statt ab Empfang gerechnet.** § 1059 Abs. 3 S. 2 ZPO knüpft an den Empfang durch den Antragsteller an.
- **Frist verstreichen lassen und auf die Verteidigung im Vollstreckbarerklärungsverfahren vertraut.** § 1060 Abs. 2 S. 3 ZPO sperrt dann die Gründe der Nr. 1.
- **Aufhebungsantrag nach erfolgter Vollstreckbarerklärung gestellt.** § 1059 Abs. 3 S. 4 ZPO schließt ihn aus.
- **Révision au fond betrieben.** Unrichtige Tatsachenfeststellung oder Rechtsanwendung ist kein Aufhebungsgrund; der Katalog des Abs. 2 ist abschließend.
- **Ordre public als Auffangargument.** Er greift nur bei Verstößen gegen elementare Grundsätze der Rechtsordnung und ist konkret zu begründen.
- **Kausalität bei Nr. 1 lit. d nicht dargelegt.** Der Verfahrensfehler muss sich auf den Schiedsspruch ausgewirkt haben können.
- **Verfahrensfehler im Schiedsverfahren nicht gerügt.** Die verfahrensinterne Präklusion schlägt auf das Aufhebungsverfahren durch.
- **Teilaufhebung nicht beantragt**, obwohl der von der Schiedsvereinbarung erfasste Teil abtrennbar ist (Abs. 2 Nr. 1 lit. c Halbs. 2).
- **Zurückverweisung nach Abs. 4 übersehen** — sie ist häufig das mildere und erfolgversprechendere Ziel.
- **Wiederaufleben der Schiedsvereinbarung nach Abs. 5 nicht bedacht.** Die Aufhebung führt nicht ohne Weiteres zum staatlichen Rechtsweg.
- **Rechtsprechung erfunden.** Jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
