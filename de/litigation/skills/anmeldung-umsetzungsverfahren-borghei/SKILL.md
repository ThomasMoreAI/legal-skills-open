---
name: anmeldung-umsetzungsverfahren-borghei
title: /verbandsklage-vdug:anmeldung-umsetzungsverfahren
description: Anmeldung zum Verbandsklageregister und Umsetzungsverfahren nach dem VDuG – Anmeldung § 46 binnen drei Wochen nach Schluss der mündlichen Verhandlung mit ausdrücklicher Nichtanwendung des § 193 BGB, Pflichtangaben und Richtigkeitsversicherung § 46 Abs. 2, Eintragung ohne inhaltliche Prüfung § 46 Abs. 3, Rücknahme § 46 Abs. 4, Register und Bekanntmachung §§ 43–45, 48, Eröffnungsbeschluss nach Zahlung § 24, Bestellung des Sachwalters § 23, Umsetzungsfonds § 25 mit Trennungspflicht und Pfändungsschutz, Teilnahme § 26, Aufgaben des Sachwalters § 27, Widerspruchsverfahren § 28 mit vier Wochen Widerspruch und zwei Wochen für den Antrag auf gerichtliche Entscheidung, Zwangsmittel §§ 29, 30, Schlussrechnung und Schlussbericht §§ 33–36 sowie nicht abgerufene Beträge § 37. Use when ein Verbraucher seinen Anspruch anmelden will oder ein Abhilfeendurteil umzusetzen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verbandsklage-vdug/skills/anmeldung-umsetzungsverfahren
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /verbandsklage-vdug:anmeldung-umsetzungsverfahren

## Zweck

Der Skill deckt die beiden Verfahrensteile ab, in denen der einzelne Verbraucher tatsächlich zu seinem Geld kommt: die **Anmeldung** zum Verbandsklageregister und das **Umsetzungsverfahren** unter einem Sachwalter. Er behandelt die Frist, deren Versäumung den Anspruch praktisch entwertet — drei Wochen nach Schluss der mündlichen Verhandlung, **ohne** die Wohltat des § 193 BGB.

## Eingaben

- Aktenzeichen der Verbandsklage, zuständiges OLG, Datum der Registerbekanntgabe
- Datum des **Schlusses der mündlichen Verhandlung**
- Anspruch des Verbrauchers: Gegenstand, Grund, Höhe; ob als kleines Unternehmen nach § 1 Abs. 2 angemeldet wird
- Ob eine Individualklage anhängig ist und wann sie erhoben wurde
- Bei Umsetzung: Abhilfeendurteil, vorläufig festgesetzte Kosten, kollektiver Gesamtbetrag, Sachwalter
- Mitteilung des Sachwalters nach § 28 Abs. 1 mit Zugangsdatum

## Sub-Agent-Architektur

Der Researcher beschafft VDuG, die Registerpraxis des Bundesamts für Justiz und die Verordnung nach § 49. Der Drafter erstellt die Anmeldung oder den Widerspruch und prüft die Nachweislage gegen die Urteilsformel nach § 16 Abs. 2. Der Reviewer rechnet jede Frist nach und kontrolliert insbesondere, dass § 193 BGB nicht angewandt wurde.

## Ablauf

### 1. Anmeldung — Frist zuerst ([§ 46 VDuG](https://www.gesetze-im-internet.de/vdug/__46.html))

**Dieser Schritt steht vor allem anderen.** Verbraucher können Ansprüche oder Rechtsverhältnisse, die Gegenstand einer Verbandsklage sind, **bis zum Ablauf von drei Wochen nach dem Schluss der mündlichen Verhandlung** zur Eintragung in das Verbandsklageregister anmelden.

> **[§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html) findet keine Anwendung** (§ 46 Abs. 1 S. 2).

Das heißt: Fällt das Fristende auf einen Samstag, Sonntag oder Feiertag, gibt es **keine** Verlängerung auf den nächsten Werktag. Dieselbe Anordnung gilt für die **Rücknahme** der Anmeldung (§ 46 Abs. 4 S. 2). Das ist die schärfste Falle des gesamten Verbandsklagerechts und in jeder Mandantenkommunikation ausdrücklich zu benennen.

**Pflichtangaben (§ 46 Abs. 2):** Die Anmeldung ist nur wirksam, wenn sie **frist- und formgerecht** erfolgt und enthält:

1. Name und Anschrift des Verbrauchers,
2. Angabe, ob die Anmeldung **als kleines Unternehmen** iSd § 1 Abs. 2 erfolgt,
3. Bezeichnung des Gerichts und Aktenzeichen,
4. Bezeichnung des Beklagten,
5. **Gegenstand und Grund** des Anspruchs oder Rechtsverhältnisses,
6. **Versicherung der Richtigkeit und Vollständigkeit** der Angaben.

Bei einem Zahlungsanspruch **soll** die Anmeldung auch Angaben zur **Höhe** enthalten.

**§ 46 Abs. 3:** Die Angaben werden **ohne inhaltliche Prüfung** eingetragen. Die Eintragung sagt also nichts über die Berechtigung — der Nachweis folgt erst im Umsetzungsverfahren.

**Form:** [§ 47 VDuG](https://www.gesetze-im-internet.de/vdug/__47.html) regelt die Formvorschriften; die Einzelheiten des Registers ergeben sich aus [§§ 43 bis 45](https://www.gesetze-im-internet.de/vdug/__43.html), [§ 48](https://www.gesetze-im-internet.de/vdug/__48.html) und der Verordnung nach [§ 49 VDuG](https://www.gesetze-im-internet.de/vdug/__49.html).

### 2. Folgen der Anmeldung ([§ 11 VDuG](https://www.gesetze-im-internet.de/vdug/__11.html))

Die Anmeldung ist der Schalter, der die Wirkungen auslöst — sie ist Vor- und Nachteil zugleich:

| Wirkung | Inhalt |
|---|---|
| **Abs. 1 Aussetzung** | Eine **vor** der Registerbekanntgabe erhobene Individualklage wird bis zur rechtskräftigen Entscheidung, sonstigen Erledigung oder wirksamen Rücknahme der Anmeldung **ausgesetzt** |
| **Abs. 2 Klageverbot** | Während der Rechtshängigkeit der Verbandsklage kann der angemeldete Verbraucher **keine** Klage über denselben Streitgegenstand erheben |
| **Abs. 3 Bindungswirkung** | Das rechtskräftige Urteil **bindet** das Gericht im Folgeprozess — **nicht** jedoch bei Abhilfeendurteilen nach § 18 |

Die Beratung des einzelnen Verbrauchers muss beides abwägen: Anmeldung bedeutet Verzicht auf den eigenen Prozessweg für die Dauer des Verfahrens, aber Teilhabe an Titel und Fonds ohne eigenes Kostenrisiko.

### 3. Umsetzungsverfahren eröffnen ([§ 22](https://www.gesetze-im-internet.de/vdug/__22.html), [§ 23](https://www.gesetze-im-internet.de/vdug/__23.html), [§ 24 VDuG](https://www.gesetze-im-internet.de/vdug/__24.html))

Das Abhilfeendurteil ordnet das Umsetzungsverfahren an (§ 18 Abs. 1 Nr. 1). Sodann:

- **§ 23** — Bestellung des **Sachwalters** durch das Gericht.
- **§ 24** — Das Gericht beschließt die **Eröffnung**, **sobald der Unternehmer gezahlt hat**: den vorläufig festgesetzten Kostenbetrag (§ 18 Abs. 1 Nr. 2) **und**, soweit dazu verurteilt, den kollektiven Gesamtbetrag (§ 18 Abs. 2) — jeweils **zu Händen des Sachwalters**.

Die Eröffnung hängt also an der Zahlung. Zahlt der Unternehmer nicht, greifen die Zwangsmittel des [§ 29 VDuG](https://www.gesetze-im-internet.de/vdug/__29.html).

### 4. Umsetzungsfonds ([§ 25 VDuG](https://www.gesetze-im-internet.de/vdug/__25.html))

Der Sachwalter **errichtet einen Umsetzungsfonds**, in den der Kostenbetrag, der kollektive Gesamtbetrag und eine etwaige Erhöhung nach § 21 einzuzahlen sind. Wesentliche Merkmale:

- **Trennungsgebot** — der Fonds ist vom Vermögen des Sachwalters getrennt zu führen (Abs. 2);
- **Direktzahlung** — berechtigte Zahlungsansprüche erfüllt der Sachwalter **unmittelbar aus dem Fonds** (Abs. 3 S. 1);
- **Entnahmeschranke** — Kosten und Vorschüsse darf der Sachwalter nur **nach Anordnung des Gerichts** entnehmen, insgesamt höchstens den vorläufig festgesetzten Kostenbetrag (Abs. 3 S. 2, 3);
- **Pfändungsschutz** — die Gelder des Fonds unterliegen **nicht der Pfändung** (Abs. 4). Gläubiger des Unternehmers oder des Sachwalters greifen ins Leere.

### 5. Teilnahme, Prüfung und Widerspruch ([§ 26](https://www.gesetze-im-internet.de/vdug/__26.html), [§ 27](https://www.gesetze-im-internet.de/vdug/__27.html), [§ 28 VDuG](https://www.gesetze-im-internet.de/vdug/__28.html))

Der Sachwalter prüft die angemeldeten Ansprüche anhand der in der Urteilsformel bestimmten **Berechtigungsnachweise** (§ 16 Abs. 2 Nr. 2) und teilt **dem Verbraucher und dem Unternehmer in Textform** mit, ob der Anspruch ganz oder teilweise berechtigt ist (§ 28 Abs. 1).

**Fristenkette des Widerspruchsverfahrens:**

| Schritt | Frist | Form |
|---|---|---|
| **Widerspruch** von Verbraucher oder Unternehmer | **vier Wochen** ab Zugang der Mitteilung — vorbehaltlich einer Verlängerung nach § 18 Abs. 3 | Textform an den Sachwalter, **begründet** |
| Entscheidung des Sachwalters über den Widerspruch | — | Textform an beide |
| **Antrag auf gerichtliche Entscheidung** beim Prozessgericht des Abhilfeverfahrens | **zwei Wochen** ab Zugang der Widerspruchsentscheidung | soweit durch sie beschwert; Entscheidung durch Beschluss |

### 6. Abschluss ([§§ 29 bis 40 VDuG](https://www.gesetze-im-internet.de/vdug/__29.html))

- **§ 29** — Zwangsmittel gegen den Unternehmer; **§ 30** — gerichtliche Aufsicht und Zwangsmittel gegen den Sachwalter.
- **§ 31** — Haftung des Sachwalters; **§ 32** — dessen Ansprüche.
- **§§ 33 bis 36** — Schlussrechnung, Schlussbericht, deren Prüfung und die Feststellung der Beendigung.
- **§ 37** — **nicht abgerufene Beträge**; **§ 40** — Herausgabeanspruch des Unternehmers. Für den Unternehmer ist das die Rückflussfrage: Was nicht abgerufen wird, ist nach Maßgabe dieser Vorschriften zu behandeln und nicht automatisch verloren.
- **§ 38** — Insolvenz des Unternehmers und Restrukturierung; **§ 39** — offene Verbraucheransprüche.

## Deterministische Berechnung

Alle Fristen dieses Skills sind kurz, und die wichtigste kennt **keine** Wochenend- oder Feiertagsverschiebung. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# § 46 Abs. 1 VDuG: 3 Wochen ab Schluss der mündlichen Verhandlung am 14.03.2026.
# ACHTUNG: § 193 BGB ist ausgeschlossen - das Ergebnis gilt auch, wenn es auf
# einen Samstag, Sonntag oder Feiertag fällt. --kein-rollover schaltet die
# Verschiebung nach § 193 BGB im Rechner ab.
python -m scripts.legal_calc.cli frist --ereignis 14.03.2026 --menge 3 --einheit wochen --land BY --kein-rollover

# § 28 Abs. 2 VDuG: 4 Wochen Widerspruch ab Zugang der Sachwaltermitteilung
python -m scripts.legal_calc.cli frist --ereignis 06.07.2026 --menge 4 --einheit wochen --land BY

# § 28 Abs. 4 VDuG: 2 Wochen für den Antrag auf gerichtliche Entscheidung
python -m scripts.legal_calc.cli frist --ereignis 20.08.2026 --menge 2 --einheit wochen --land BY
```

`--json` liefert die Rechenschritte. Der **Schluss der mündlichen Verhandlung** ist eine Tatsachenfeststellung aus dem Protokoll und gesondert zu belegen.

## Quellen

### Statute

- [§ 1 VDuG](https://www.gesetze-im-internet.de/vdug/__1.html) (kleine Unternehmen), [§ 11](https://www.gesetze-im-internet.de/vdug/__11.html), [§ 16 VDuG](https://www.gesetze-im-internet.de/vdug/__16.html), [§ 18](https://www.gesetze-im-internet.de/vdug/__18.html), [§ 21](https://www.gesetze-im-internet.de/vdug/__21.html), [§ 22](https://www.gesetze-im-internet.de/vdug/__22.html), [§ 23](https://www.gesetze-im-internet.de/vdug/__23.html), [§ 24](https://www.gesetze-im-internet.de/vdug/__24.html), [§ 25](https://www.gesetze-im-internet.de/vdug/__25.html), [§ 26](https://www.gesetze-im-internet.de/vdug/__26.html), [§ 27](https://www.gesetze-im-internet.de/vdug/__27.html), [§ 28](https://www.gesetze-im-internet.de/vdug/__28.html), [§ 29](https://www.gesetze-im-internet.de/vdug/__29.html), [§ 37](https://www.gesetze-im-internet.de/vdug/__37.html), [§ 43](https://www.gesetze-im-internet.de/vdug/__43.html), [§ 46](https://www.gesetze-im-internet.de/vdug/__46.html), [§ 47](https://www.gesetze-im-internet.de/vdug/__47.html), [§ 48](https://www.gesetze-im-internet.de/vdug/__48.html), [§ 49 VDuG](https://www.gesetze-im-internet.de/vdug/__49.html)
- [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html), [§ 204 BGB](https://www.gesetze-im-internet.de/bgb/__204.html)
- Verbandsklageregister des Bundesamts für Justiz

### Kommentare und Literatur

- Röthemeyer, VDuG, Kommentar, §§ 22–40, § 46.
- Nordholtz/Mekat, Musterfeststellungsklage und Verbandsklage, Kap. Umsetzungsverfahren.
- Beiträge zum Sachwalteramt und zum Umsetzungsfonds in NZI und VuR 2024–2026 (Fundstelle vor Verwendung prüfen) `[unverifiziert – prüfen]`

### Rechtsprechung

Zum Umsetzungsverfahren liegt bislang praktisch keine veröffentlichte Rechtsprechung vor — die ersten Abhilfeendurteile ergehen erst. Jede Entscheidung ist vor Verwendung in juris oder Beck-Online zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
ANMELDUNG / UMSETZUNGSVERFAHREN — <Mandat> — <Datum>

I.   Anmeldung § 46
     Verbandsklage:           OLG <…>, Az. <…>
     Registerbekanntgabe:     <Datum>
     Schluss der mündlichen Verhandlung: <Datum>
     Anmeldefrist endet:      <Datum>   § 193 BGB: NICHT anwendbar
     Pflichtangaben Abs. 2:   Nr. 1 <…> | Nr. 2 kleines Unternehmen [ja/nein] |
                              Nr. 3 <…> | Nr. 4 <…> | Nr. 5 <…> | Nr. 6 Versicherung [enthalten]
     Höhe (Soll-Angabe):      <Betrag>
     Hinweis:                 Eintragung ohne inhaltliche Prüfung (Abs. 3)

II.  Folgen der Anmeldung § 11
     Abs. 1 Aussetzung laufender Individualklage: [ja — Klage vom <Datum> / nein]
     Abs. 2 Klageverbot:      <…>
     Abs. 3 Bindungswirkung:  <…>  (nicht bei Abhilfeendurteil § 18)
     Empfehlung an den Mandanten: [anmelden / Individualweg — Begründung]

III. Umsetzungsverfahren
     Abhilfeendurteil vom:    <Datum>
     Sachwalter § 23:         <…>
     Eröffnung § 24:          [Zahlung erfolgt am <Datum> / ausstehend — § 29 Zwangsmittel]
     Umsetzungsfonds § 25:    <Betrag>  Pfändungsschutz Abs. 4: ja
     Berechtigungsnachweise:  <aus der Urteilsformel § 16 Abs. 2 Nr. 2>

IV.  Widerspruchsverfahren § 28
     Mitteilung des Sachwalters zugegangen am: <Datum>
     Widerspruchsfrist (4 Wochen, ggf. verlängert nach § 18 Abs. 3): bis <Datum>
     Widerspruchsentscheidung zugegangen am:   <Datum>
     Antrag auf gerichtliche Entscheidung (2 Wochen): bis <Datum>

V.   Abschluss
     Schlussrechnung / Schlussbericht §§ 33–35: <Stand>
     Nicht abgerufene Beträge § 37 / Herausgabe § 40: <…>
     Insolvenzszenario § 38:  <…>

VI.  Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VII. Quellenverzeichnis
```

### Formulierungshilfe — Anmeldung nach § 46 VDuG (Gerüst)

```
An das Verbandsklageregister beim Bundesamt für Justiz

Anmeldung eines Anspruchs zur Eintragung in das Verbandsklageregister
(§ 46 VDuG)

1. Verbraucher:      <Name, Anschrift>
2. Anmeldung als kleines Unternehmen im Sinne des § 1 Abs. 2 VDuG:
                     [ja / nein]
3. Gericht / Az.:    Oberlandesgericht <…>, Az. <…>
4. Beklagte:         <Firma, Anschrift>
5. Gegenstand und Grund des Anspruchs:
                     <Vertrag vom <Datum>, beanstandete Klausel/Vorgang,
                      daraus folgender Anspruch>
   Höhe des Zahlungsanspruchs: <Betrag> (Angabe nach § 46 Abs. 2 S. 2)
6. Ich versichere die Richtigkeit und Vollständigkeit dieser Angaben.

<Ort, Datum, Unterschrift>
```

## Risiken / typische Fehler

- **§ 193 BGB angewandt.** § 46 Abs. 1 S. 2 und Abs. 4 S. 2 VDuG schließen ihn aus — ein Fristende am Samstag oder Feiertag verschiebt sich **nicht**.
- **Frist ab Registerbekanntgabe statt ab Schluss der mündlichen Verhandlung gerechnet.**
- **Versicherung der Richtigkeit vergessen.** Ohne sie ist die Anmeldung nach § 46 Abs. 2 Nr. 6 VDuG unwirksam.
- **Angabe zum kleinen Unternehmen weggelassen** (§ 46 Abs. 2 Nr. 2 VDuG).
- **Eintragung für eine Anspruchsprüfung gehalten.** Sie erfolgt nach Abs. 3 ohne inhaltliche Prüfung.
- **Klageverbot des § 11 Abs. 2 übersehen** und nach Anmeldung Individualklage erhoben.
- **Eröffnung des Umsetzungsverfahrens ohne Zahlung erwartet.** § 24 VDuG knüpft sie an die Zahlung zu Händen des Sachwalters.
- **Widerspruchsfrist des § 28 Abs. 2 VDuG versäumt** oder die Zweiwochenfrist des Abs. 4 mit ihr verwechselt.
- **Widerspruch ohne Begründung eingelegt** — § 28 Abs. 2 S. 2 VDuG verlangt sie.
- **Fonds für pfändbar gehalten.** § 25 Abs. 4 VDuG stellt das Gegenteil klar.
- **Rechtsprechung erfunden.** Zum Umsetzungsverfahren gibt es sie noch kaum; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
