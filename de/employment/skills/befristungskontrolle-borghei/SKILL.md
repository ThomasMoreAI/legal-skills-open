---
name: befristungskontrolle-borghei
title: /arbeitsrecht:befristungskontrolle
description: Wirksamkeitskontrolle befristeter Arbeitsverträge nach dem TzBfG – Schriftformerfordernis § 14 Abs. 4 TzBfG, Sachgrundbefristung § 14 Abs. 1 TzBfG mit dem Katalog Nr. 1–8, sachgrundlose Befristung § 14 Abs. 2 TzBfG (zwei Jahre, dreimalige Verlängerung) und das Vorbeschäftigungsverbot § 14 Abs. 2 S. 2 TzBfG nach der Entscheidung des BVerfG von 2018, Sonderregeln § 14 Abs. 2a und Abs. 3 TzBfG, Entfristungsklage § 17 TzBfG und Rechtsfolge § 16 TzBfG. Use when eine Befristung gestaltet oder eine auslaufende Befristung auf Unwirksamkeit geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/arbeitsrecht/skills/befristungskontrolle
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /arbeitsrecht:befristungskontrolle

## Zweck

Befristungen scheitern in der Praxis fast nie an der Sachgrundfrage, sondern an drei banalen Punkten: fehlende Schriftform **vor** Arbeitsantritt, eine unzulässige Vorbeschäftigung und eine „Verlängerung", die in Wahrheit ein Neuvertrag war. Dieser Skill prüft diese drei zuerst und geht erst dann in die Sachgrundprüfung.

## Eingaben

- Vertragskette: **alle** Verträge mit Datum des Abschlusses, Datum des Arbeitsbeginns, Laufzeit, geänderte Bedingungen
- Wurde der befristete Vertrag **vor** Arbeitsaufnahme unterzeichnet? (Kritischster Einzelpunkt)
- Vorbeschäftigung bei demselben Arbeitgeber: wann, wie lange, welche Tätigkeit? Auch Leiharbeit, Praktikum, Ausbildung, geringfügige Beschäftigung?
- Sachgrund vorhanden und dokumentiert?
- Alter des Arbeitnehmers bei Beginn (§ 14 Abs. 3 TzBfG), Unternehmensgründung < 4 Jahre (§ 14 Abs. 2a TzBfG)
- Tarifvertrag mit abweichenden Regelungen zu Verlängerungszahl oder Höchstdauer (§ 14 Abs. 2 S. 3, 4 TzBfG)
- Bei Prüfung auf Arbeitnehmerseite: **vereinbartes Ende** der Befristung — der Fristauslöser des § 17 TzBfG

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert §§ 14, 16, 17 TzBfG mit URL, die Richtlinie 1999/70/EG samt EGB-UNICE-CEEP-Rahmenvereinbarung und die BVerfG-/BAG-Linien zum Vorbeschäftigungsverbot.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Befristungsabrede, Verlängerungsvereinbarung oder Entfristungsklage.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Schriftform, Vertragskette, Fristen und Antragsfassung.

## Ablauf

### 1. Schriftform ([§ 14 Abs. 4 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__14.html))

Die **Befristungsabrede** — nicht der gesamte Vertrag — bedarf der Schriftform nach § 126 BGB. Konsequenzen:

- Die Unterzeichnung muss **vor** der Arbeitsaufnahme erfolgen. Wird zunächst mündlich vereinbart und erst nach Arbeitsbeginn unterschrieben, ist bereits ein **unbefristetes** Arbeitsverhältnis entstanden; die spätere Unterschrift ist eine nachträgliche Befristung, für die ein eigener Sachgrund erforderlich wäre.
- **Textform genügt nicht.** Die durch das Bürokratieentlastungsgesetz für den Nachweis nach § 2 NachwG geöffnete Textform ändert an § 14 Abs. 4 TzBfG nichts.
- Ein Verstoß führt nach [§ 16 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__16.html) zum **unbefristeten** Arbeitsverhältnis; der Arbeitgeber kann es frühestens zum vereinbarten Ende ordentlich kündigen, sofern die ordentliche Kündigung nicht vertraglich ausgeschlossen ist.

### 2. Sachgrundbefristung ([§ 14 Abs. 1 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__14.html))

Der Katalog ist **nicht abschließend** („insbesondere"), praktisch aber maßgeblich:

| Nr. | Sachgrund | Prüfschwerpunkt |
|---|---|---|
| 1 | Nur vorübergehender betrieblicher Bedarf | Prognose bei Vertragsschluss, konkret und belegbar |
| 2 | Anschluss an Ausbildung oder Studium | Nur **einmalig** zur Erleichterung des Übergangs |
| 3 | Vertretung | Kausalzusammenhang zwischen Ausfall und Einstellung; unmittelbare, mittelbare oder gedankliche Zuordnung |
| 4 | Eigenart der Arbeitsleistung | Rundfunk, Bühne, Profisport |
| 5 | Erprobung | Dauer muss der Tätigkeit angemessen sein (regelmäßig ≤ 6 Monate) |
| 6 | In der Person liegende Gründe | Eigener Wunsch, Aufenthaltstitel, Rentennähe |
| 7 | Haushaltsmittel | Mittel müssen **haushaltsrechtlich** für befristete Beschäftigung bestimmt und der AN entsprechend eingesetzt sein |
| 8 | Gerichtlicher Vergleich | Nur echter Vergleich unter Mitwirkung des Gerichts |

**Kettenbefristung:** Auch mit Sachgrund kann eine lange Kette rechtsmissbräuchlich sein ([§ 242 BGB](https://www.gesetze-im-internet.de/bgb/__242.html) i.V.m. der unionsrechtlichen Missbrauchskontrolle nach Paragraf 5 der Rahmenvereinbarung zur Richtlinie 1999/70/EG). Die Rechtsprechung arbeitet mit einer Gesamtwürdigung aus Dauer und Zahl der Verträge; ab etwa acht Jahren oder mehr als zwölf Verlängerungen wird eine Missbrauchsprüfung indiziert (EuGH- und BAG-Rspr. zur institutionellen Rechtsmissbrauchskontrolle bei Kettenbefristungen `[unverifiziert – prüfen]`).

### 3. Sachgrundlose Befristung ([§ 14 Abs. 2 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__14.html))

Zulässig bis zu **zwei Jahren**, innerhalb derer höchstens **dreimal verlängert** werden darf.

**Was eine „Verlängerung" ist:** Die Verlängerungsvereinbarung muss

1. **vor** Ablauf des laufenden Vertrages schriftlich geschlossen werden,
2. **nahtlos** anschließen (keine Unterbrechung, auch nicht um einen Tag),
3. **ausschließlich die Vertragsdauer** ändern. Wird gleichzeitig eine andere Bedingung geändert — Entgelt, Arbeitszeit, Tätigkeit —, liegt ein **Neuvertrag** vor, der nach § 14 Abs. 2 S. 2 TzBfG an der Vorbeschäftigung mit demselben Arbeitgeber scheitert.

Ausnahme zu Nr. 3: Eine gleichzeitige Anpassung ist unschädlich, wenn der Arbeitnehmer ohnehin einen Anspruch darauf hatte (z. B. tarifliche Entgelterhöhung).

**Tariföffnung:** Durch Tarifvertrag können Zahl der Verlängerungen und Höchstdauer abweichend geregelt werden (§ 14 Abs. 2 S. 3 TzBfG); nicht tarifgebundene Parteien können die Anwendung vereinbaren (S. 4). Die Öffnung ist nicht grenzenlos — sie muss sich in einem unionsrechtlich vertretbaren Rahmen halten.

### 4. Vorbeschäftigungsverbot ([§ 14 Abs. 2 S. 2 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__14.html))

Wortlaut: Die sachgrundlose Befristung ist **nicht zulässig, wenn mit demselben Arbeitgeber bereits zuvor ein befristetes oder unbefristetes Arbeitsverhältnis bestanden hat.**

Die Entwicklung in drei Schritten:

1. Das BAG legte die Norm zeitweise dahin aus, dass nur Vorbeschäftigungen innerhalb der letzten **drei Jahre** schädlich seien `[unverifiziert – prüfen]`.
2. Das **BVerfG** verwarf diese Auslegung mit Beschl. v. 06.06.2018 – 1 BvL 7/14 und 1 BvR 1375/14, BVerfGE 149, 126 = NZA 2018, 774 ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=06.06.2018&Aktenzeichen=1%20BvL%207/14)) als Überschreitung der Grenzen richterlicher Rechtsfortbildung: Der Wortlaut sei eindeutig, ein starres Drei-Jahres-Modell mit dem erkennbaren Willen des Gesetzgebers nicht vereinbar.
3. Zugleich verlangte das BVerfG in derselben Entscheidung eine **verfassungskonforme Einschränkung** für Fälle, in denen das Verbot unzumutbar wäre. Anerkannte Fallgruppen: die Vorbeschäftigung liegt **sehr lange** zurück, war **ganz anders geartet** oder von **sehr kurzer Dauer** — genannt werden geringfügige Nebenbeschäftigungen während Schule oder Studium, Werkstudententätigkeiten und Beschäftigungen im Rahmen der Berufsausbildung.

**Praxisfolge:** „Sehr lange" ist nicht mit den früheren drei Jahren gleichzusetzen; in der nachfolgenden Instanzrechtsprechung wurden Zeiträume im Bereich von etwa zwei Jahrzehnten als ausreichend, deutlich kürzere als nicht ausreichend angesehen `[unverifiziert – prüfen]`. Für die Gestaltung heißt das: **Bei jeder sachgrundlosen Befristung ist die Personalhistorie vollständig abzufragen**, einschließlich Aushilfs-, Ferien- und Praktikantenverhältnissen. Der Arbeitgeber, der auf eine Selbstauskunft vertraut, trägt das Risiko; eine bewusst falsche Antwort des Arbeitnehmers kann allerdings den Einwand des Rechtsmissbrauchs begründen.

„Derselbe Arbeitgeber" ist der **Vertragsarbeitgeber**, nicht der Konzern. Vorbeschäftigung bei einer anderen Konzerngesellschaft ist unschädlich; die Zwischenschaltung eines Verleihers zur Umgehung ist es nicht.

### 5. Sonderfälle

- **[§ 14 Abs. 2a TzBfG](https://www.gesetze-im-internet.de/tzbfg/__14.html) — Existenzgründung:** In den ersten vier Jahren nach Gründung ist die sachgrundlose Befristung bis zu vier Jahren und mit mehrfacher Verlängerung zulässig. Nicht bei Umstrukturierungen bestehender Unternehmen. Maßgeblich ist die Anzeige der Erwerbstätigkeit nach § 138 AO.
- **[§ 14 Abs. 3 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__14.html) — ältere Arbeitnehmer:** Sachgrundlose Befristung bis zu fünf Jahren bei Vollendung des 52. Lebensjahres und mindestens viermonatiger vorangegangener Beschäftigungslosigkeit.
- **Auflösende Bedingung** (§ 21 TzBfG): unterliegt denselben Anforderungen; die Klagefrist des § 17 TzBfG läuft ab Zugang der schriftlichen Unterrichtung über den Bedingungseintritt.
- **Wissenschaftszeitvertragsgesetz (WissZeitVG)** und **§ 21 BEEG** enthalten eigenständige Befristungsregime, die § 14 TzBfG verdrängen.

### 6. Entfristungsklage ([§ 17 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__17.html))

**Drei Wochen nach dem vereinbarten Ende** des befristeten Arbeitsvertrages ist Klage auf Feststellung zu erheben, dass das Arbeitsverhältnis aufgrund der Befristung nicht beendet ist. Zu beachten:

- Fristbeginn ist das **vereinbarte Ende**, nicht der Zugang einer Mitteilung. Wird das Arbeitsverhältnis darüber hinaus fortgesetzt, beginnt die Frist mit Zugang der schriftlichen Erklärung des Arbeitgebers, dass das Arbeitsverhältnis beendet sei (§ 17 S. 3 TzBfG).
- **§§ 5 bis 7 KSchG gelten entsprechend** (§ 17 S. 2 TzBfG): nachträgliche Zulassung, verlängerte Anrufungsfrist und — vor allem — die **Präklusion**. Wer die drei Wochen versäumt, kann die Unwirksamkeit der Befristung nicht mehr geltend machen.
- Die Klage kann **vor** dem Ende erhoben werden und ist dann bereits zulässig.

**Formulierungshilfe — Klageantrag:**

```
1. Es wird festgestellt, dass das Arbeitsverhältnis der Parteien
   aufgrund der im Arbeitsvertrag vom <Datum> vereinbarten
   Befristung nicht mit Ablauf des <Datum> beendet worden ist,
   sondern zu unveränderten Bedingungen fortbesteht.

2. Hilfsweise für den Fall des Obsiegens mit dem Antrag zu 1.:
   Die Beklagte wird verurteilt, den Kläger zu unveränderten
   Bedingungen als <Funktion> bis zum rechtskräftigen Abschluss
   des Verfahrens weiterzubeschäftigen.
```

### 7. Rechtsfolge ([§ 16 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__16.html))

Ist die Befristung unwirksam, gilt der Vertrag als auf **unbestimmte Zeit** geschlossen. Der Arbeitgeber kann ihn frühestens zum vereinbarten Ende ordentlich kündigen — bei Unwirksamkeit wegen Formmangels sogar erst zu diesem Zeitpunkt. Ist die ordentliche Kündigung vertraglich oder tariflich ausgeschlossen, bleibt nur § 626 BGB.

## Quellen

### Statute

- [§ 14 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__14.html), [§ 15 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__15.html), [§ 16 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__16.html), [§ 17 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__17.html)
- [§ 126 BGB](https://www.gesetze-im-internet.de/bgb/__126.html), [§ 242 BGB](https://www.gesetze-im-internet.de/bgb/__242.html), [§ 623 BGB](https://www.gesetze-im-internet.de/bgb/__623.html)
- [§ 5 KSchG](https://www.gesetze-im-internet.de/kschg/__5.html), [§ 7 KSchG](https://www.gesetze-im-internet.de/kschg/__7.html)
- [§ 2 NachwG](https://www.gesetze-im-internet.de/nachwg/__2.html) (Nachweis der Befristungsdauer)
- Richtlinie 1999/70/EG (EGB-UNICE-CEEP-Rahmenvereinbarung über befristete Arbeitsverträge)

### Kommentare

- Müller-Glöge, in: ErfK, 24. Aufl. 2024, § 14 TzBfG Rn. 1 ff.
- Backhaus, in: APS, 6. Aufl. 2021, § 14 TzBfG Rn. 100 ff. (Vorbeschäftigungsverbot)
- Hesse, in: MüKoBGB, 9. Aufl. 2023, § 14 TzBfG Rn. 1 ff.
- Preis / Greiner, in: ErfK, § 17 TzBfG Rn. 1 ff. (Entfristungsklage)

### Rechtsprechung

- BVerfG, Beschl. v. 06.06.2018 – 1 BvL 7/14 und 1 BvR 1375/14, BVerfGE 149, 126 = NZA 2018, 774 (verfassungsrechtliche Grenze der Auslegung des § 14 Abs. 2 S. 2 TzBfG: Verwerfung der Drei-Jahres-Rechtsprechung des BAG; verfassungskonforme Einschränkung bei sehr lange zurückliegender, ganz anders gearteter oder sehr kurzer Vorbeschäftigung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=06.06.2018&Aktenzeichen=1%20BvL%207/14)
- st. Rspr. des BAG zu § 14 Abs. 4 TzBfG (Schriftform der Befristungsabrede vor Arbeitsaufnahme) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zum Verlängerungsbegriff des § 14 Abs. 2 S. 1 TzBfG (nahtloser Anschluss, ausschließlich Änderung der Vertragsdauer) `[unverifiziert – prüfen]`
- EuGH- und BAG-Rspr. zur institutionellen Rechtsmissbrauchskontrolle bei Kettenbefristungen `[unverifiziert – prüfen]`

> Die BVerfG-Entscheidung von 2018 ist vor Verwendung mit Aktenzeichen und Fundstelle in der [BVerfG-Entscheidungsdatenbank](https://www.bundesverfassungsgericht.de/) zu verifizieren; Aktenzeichen werden hier bewusst nicht angegeben.

## Ausgabeformat

```
BEFRISTUNGSKONTROLLE — <Mandat-ID> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

Gesamtbefund: [🟢 wirksam / 🟡 angreifbar / 🔴 unwirksam → § 16 TzBfG]

⚠️ FRISTBLOCK
    Vereinbartes Ende:            <Datum>
    Klagefrist § 17 TzBfG endet:  <Datum>   (3 Wochen, §§ 5–7 KSchG analog)

I.    Vertragskette
      Nr. | Abschluss | Beginn | Ende | geänderte Bedingungen
      <…>
II.   Schriftform § 14 Abs. 4 TzBfG
      Unterschrift vor Arbeitsantritt:   [🟢 / 🔴]
III.  Befristungstyp                     [Sachgrund § 14 I Nr. <N> /
                                          sachgrundlos § 14 II /
                                          § 14 IIa / § 14 III]
IV.   Bei Sachgrund
      Grund und Dokumentation:           <…>
      Prognose bei Vertragsschluss:      [🟢 / 🔴]
V.    Bei sachgrundloser Befristung
      Gesamtdauer:                       <…> / max. 2 Jahre
      Zahl der Verlängerungen:           <N> / max. 3
      Nahtlosigkeit:                     [🟢 / 🔴 Unterbrechung <…>]
      Nur Dauer geändert:                [🟢 / 🔴 → Neuvertrag]
      Vorbeschäftigung § 14 II 2:        [keine / <Art, Zeitraum>]
      Verfassungskonforme Ausnahme:      [greift / greift nicht — Begründung]
VI.   Tarifliche Abweichung § 14 II 3    [N/A / <TV, Regelung>]
VII.  Missbrauchskontrolle (Ketten)      Dauer <N> Jahre, <N> Verträge  [🟢 / 🔴]
VIII. Rechtsfolge § 16 TzBfG             <…>
IX.   Kündigungsmöglichkeit              <frühestens zum <Datum>>

Offene Tatsachenfragen: <Personalhistorie vollständig?>
Empfehlung: <…>
```

## Risiken / typische Fehler

- **Befristungsabrede erst nach Arbeitsantritt unterschrieben** — häufigster und praktisch nicht heilbarer Fehler; das Arbeitsverhältnis ist bereits unbefristet entstanden.
- **„Verlängerung" mit gleichzeitiger Änderung anderer Bedingungen** — Entgelterhöhung oder Stundenanpassung im selben Dokument macht aus der Verlängerung einen Neuvertrag und lässt ihn am Vorbeschäftigungsverbot scheitern.
- **Lücke zwischen zwei Verträgen** — auch ein einziger Tag Unterbrechung zerstört die Verlängerungskette.
- **Vorbeschäftigung nicht vollständig ermittelt** — Ferienjobs, Werkstudententätigkeit und Aushilfen bei demselben Vertragsarbeitgeber zählen; die frühere Drei-Jahres-Grenze existiert nicht mehr.
- **Auf die alte Drei-Jahres-Rechtsprechung vertraut** — sie ist durch die BVerfG-Entscheidung von 2018 überholt; die Ausnahme ist eng und einzelfallbezogen.
- **Klagefrist § 17 TzBfG ab Zugang einer Mitteilung gerechnet** statt ab dem vereinbarten Ende.
- **Präklusion nach § 17 S. 2 TzBfG i.V.m. § 7 KSchG übersehen** — nach drei Wochen ist die Befristung nicht mehr angreifbar, auch wenn sie evident formunwirksam war.
- **Sachgrund erst im Prozess nachgeschoben** — der Sachgrund muss bei Vertragsschluss objektiv vorgelegen haben; er muss allerdings nicht im Vertrag genannt sein.
- **Ordentliche Kündigung im befristeten Vertrag nicht vorbehalten** — ohne Vorbehalt ist sie nach § 15 Abs. 4 TzBfG ausgeschlossen; nach § 16 TzBfG wirkt sich das bei unwirksamer Befristung erheblich aus.
