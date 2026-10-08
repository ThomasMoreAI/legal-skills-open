---
name: beamtenstatusrecht-borghei
title: /beamten-disziplinarrecht:beamtenstatusrecht
description: Statusfragen des Beamtenverhältnisses – Ernennung und ihre Fehler §§ 11, 12 BeamtStG, Probezeit, Abgrenzung Umsetzung / Abordnung § 14 BeamtStG / Versetzung § 15 BeamtStG, Dienstunfähigkeit und Zurruhesetzung § 26 BeamtStG, Dienstunfall § 45 BeamtVG und die Meldefrist, Beihilfe, Nebentätigkeit § 40 BeamtStG, Fürsorgepflicht § 45 BeamtStG, Remonstration § 36 BeamtStG. Use when eine beamtenrechtliche Statusmaßnahme (Ernennung, Versetzung, Zurruhesetzung, Nebentätigkeitsversagung, Dienstunfallanerkennung) geprüft oder angegriffen werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/beamten-disziplinarrecht/skills/beamtenstatusrecht
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /beamten-disziplinarrecht:beamtenstatusrecht

## Zweck

Der Skill ordnet eine beamtenrechtliche Maßnahme statusrechtlich ein und bestimmt den zutreffenden Rechtsbehelf. Die entscheidende Vorfrage ist stets dieselbe: **Handelt es sich um einen Verwaltungsakt?** Von ihrer Beantwortung hängen Klageart, Frist und Eilrechtsschutz ab — und an ihr scheitern die meisten Verfahren, insbesondere bei der Umsetzung. Der Skill deckt Ernennung, ortsbezogene Maßnahmen, Dienstunfähigkeit, Unfallfürsorge, Nebentätigkeit, Fürsorge und Remonstration ab.

## Eingaben

- Dienstherr (Bund / Land / Kommune), Statusamt, Dienstzeit
- Konkrete Maßnahme mit Datum, Wortlaut und Rechtsbehelfsbelehrung
- Bei Ernennung: Urkundeninhalt, Aushändigung, etwaige Fehler (Zuständigkeit, Form, Rückwirkung)
- Bei ortsbezogener Maßnahme: bisheriger und neuer Dienstposten, Amt im abstrakt-funktionellen Sinn, Behördenwechsel, Ortswechsel
- Bei Dienstunfähigkeit: amtsärztliches Gutachten, Untersuchungsanordnung, Restleistungsfähigkeit
- Bei Dienstunfall: Ereignis, Meldedatum, Kausalverlauf, Vorschäden
- Bei Nebentätigkeit: Art, Umfang, Vergütung, Genehmigungsantrag und Bescheid
- Bevorstehende Fristen

## Sub-Agent-Architektur

Ein Researcher bestimmt den Rechtskreis (BeamtStG plus Landesbeamtengesetz oder BBG) und beschafft die Normen, das einschlägige Versorgungs- und Beihilferecht sowie die Rechtsprechung des 2. Senats des BVerwG. Ein Drafter ordnet die Maßnahme als Verwaltungsakt oder innerdienstliche Weisung ein, wählt Klageart und Rechtsbehelf und entwirft Widerspruch, Klage oder Remonstration. Ein Reviewer prüft Fristen — insbesondere § 74 VwGO und die Meldefrist des § 45 BeamtVG —, die Klageartwahl und jede Fundstelle; nicht bestätigte Entscheidungen werden mit `[unverifiziert - prüfen]` markiert.

## Ablauf

### 1. Anwendbares Recht bestimmen ([§ 1 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__1.html))

**Erster Schritt, ohne Ausnahme.**

| Dienstherr | Statusrecht | Versorgung / Beihilfe |
|---|---|---|
| Bund | [BBG](https://www.gesetze-im-internet.de/bbg_2009/) | [BeamtVG](https://www.gesetze-im-internet.de/beamtvg/), BBhV |
| Land, Kommune | [BeamtStG](https://www.gesetze-im-internet.de/beamtstg/) + Landesbeamtengesetz | Landesbeamtenversorgungsgesetz, Landesbeihilfeverordnung |

Das BeamtStG ist Rahmenrecht des Bundes für die Länder; es gilt **nicht** für Bundesbeamte. Für Bundesbeamte ist stets die Parallelnorm des BBG zu zitieren. Landesbeamtenversorgung und Beihilfe sind seit der Föderalismusreform I **vollständig landesrechtlich** und dürfen nicht durch BeamtVG-Zitate ersetzt werden `[unverifiziert - prüfen]` je Land.

### 2. Ernennung, Nichtigkeit und Rücknahme ([§ 11 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__11.html), [§ 12 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__12.html))

Die Ernennung erfolgt durch Aushändigung der Urkunde ([§ 8 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__8.html)) mit den gesetzlich vorgeschriebenen Wörtern; sie ist ein mitwirkungsbedürftiger Verwaltungsakt und wirkt nicht zurück.

- **Nichtigkeit § 11 BeamtStG** — insbesondere bei sachlicher Unzuständigkeit der ernennenden Behörde oder fehlender Rechtsfähigkeit des Dienstherrn. Die Nichtigkeit tritt kraft Gesetzes ein; die Feststellung ist deklaratorisch.
- **Rücknahme § 12 BeamtStG** — insbesondere bei arglistiger Täuschung, Drohung oder Bestechung, bei nicht erkannter Verurteilung oder bei fehlender Verfassungstreue; die Rücknahme ist fristgebunden ausgestaltet und wirkt zurück.

Nach vollzogener Ernennung eines Konkurrenten greift der Grundsatz der Ämterstabilität: `/beamten-disziplinarrecht:konkurrentenstreit`.

**Probezeit** — Beamte auf Probe können nach [§ 23 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__23.html) entlassen werden, unter anderem wegen mangelnder Bewährung. Die Bewährungsprognose unterliegt einem Beurteilungsspielraum mit derselben eingeschränkten Kontrolldichte wie die dienstliche Beurteilung.

### 3. Umsetzung, Abordnung, Versetzung ([§ 14 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__14.html), [§ 15 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__15.html))

Die praktisch wichtigste Abgrenzung des Statusrechts:

| Maßnahme | Inhalt | Rechtsnatur | Rechtsbehelf |
|---|---|---|---|
| **Umsetzung** | Wechsel des Dienstpostens **innerhalb** derselben Behörde; Amt im statusrechtlichen und abstrakt-funktionellen Sinn bleibt unberührt | **kein Verwaltungsakt** — innerdienstliche Weisung nach § 35 BeamtStG | allgemeine Leistungs- bzw. Feststellungsklage; Eilrechtsschutz § 123 VwGO |
| **Abordnung** ([§ 14](https://www.gesetze-im-internet.de/beamtstg/__14.html)) | vorübergehende Tätigkeit bei anderer Behörde oder anderem Dienstherrn, Zugehörigkeit bleibt | Verwaltungsakt | Widerspruch / Anfechtungsklage; § 80 Abs. 5 VwGO |
| **Versetzung** ([§ 15](https://www.gesetze-im-internet.de/beamtstg/__15.html)) | dauerhafter Wechsel zu anderer Behörde oder anderem Dienstherrn | Verwaltungsakt | Widerspruch / Anfechtungsklage; § 80 Abs. 5 VwGO |

Die Umsetzung ist nur auf **Ermessensfehler** überprüfbar; der Dienstherr hat ein weites Organisationsermessen, begrenzt durch die Fürsorgepflicht und das Willkürverbot. Wer gegen eine Umsetzung Anfechtungsklage erhebt, verliert wegen fehlender Statthaftigkeit — die zentrale Klageartfalle des Gebiets.

### 4. Dienstunfähigkeit und Zurruhesetzung ([§ 26 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__26.html))

Dienstunfähig ist, wer wegen des körperlichen Zustands oder aus gesundheitlichen Gründen zur Erfüllung der Dienstpflichten dauernd unfähig ist. Prüfungsreihenfolge:

1. **Untersuchungsanordnung** — sie muss Anlass und Umfang der Untersuchung aus sich heraus erkennen lassen; eine pauschale Anordnung ist rechtswidrig, und ihre Nichtbefolgung darf dann nicht zulasten des Beamten gewertet werden.
2. **Amtsärztliches Gutachten** — es muss die tragenden Feststellungen und den Weg zur Prognose offenlegen; der Dienstherr darf sich nicht auf das Ergebnis beschränken (BVerwG, Urt. v. 05.06.2014 – 2 C 22.13, BVerwGE 150, 1 = NVwZ 2014, 1319).
3. **Suche nach anderweitiger Verwendung** — Vorrang von Weiterverwendung vor Zurruhesetzung (§ 26 Abs. 1 S. 3, Abs. 2, 3 BeamtStG). Die Suche ist **behördenübergreifend** und zu dokumentieren; ihr Unterlassen macht die Zurruhesetzung rechtswidrig.
4. **Begrenzte Dienstfähigkeit** ([§ 27 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__27.html)) vor der Zurruhesetzung prüfen.
5. Die Zurruhesetzung ist ein Verwaltungsakt: Widerspruch und Anfechtungsklage, Frist [§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html).

### 5. Dienstunfall und Unfallfürsorge ([§ 45 BeamtVG](https://www.gesetze-im-internet.de/beamtvg/__45.html))

Dienstunfall ist ein auf äußerer Einwirkung beruhendes, plötzliches, örtlich und zeitlich bestimmbares, einen Körperschaden verursachendes Ereignis in Ausübung oder infolge des Dienstes ([§ 31 BeamtVG](https://www.gesetze-im-internet.de/beamtvg/__31.html)).

**§ 45 BeamtVG setzt Meldefristen, die materielle Ausschlussfristen sind.** Unfälle sind innerhalb der gesetzlichen Frist zu melden; nach Fristablauf ist die Unfallfürsorge nur unter engen Voraussetzungen zu gewähren. Die konkrete Fristenstruktur ist im Normtext nachzulesen und für Landesbeamte durch die landesrechtliche Parallelnorm zu ersetzen. Der Kausalitätsmaßstab ist die **wesentliche Mitverursachung**; eine bloße Gelegenheitsursache bei vorbestehendem Leiden genügt nicht `[unverifiziert - prüfen]`.

**Beihilfe** ist Ausfluss der Fürsorgepflicht und richtet sich nach der BBhV bzw. der jeweiligen Landesbeihilfeverordnung. Ablehnungsbescheide sind Verwaltungsakte; Widerspruch und Verpflichtungsklage sind statthaft.

### 6. Nebentätigkeit ([§ 40 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__40.html))

Nebentätigkeiten sind je nach Ausgestaltung genehmigungspflichtig oder anzeigepflichtig. Die Genehmigung ist zu versagen, wenn die Nebentätigkeit dienstliche Interessen beeinträchtigen kann — insbesondere bei Beeinträchtigung der Arbeitskraft, Interessenkollision, Ansehensschädigung oder Inanspruchnahme über den zulässigen zeitlichen Umfang hinaus. Die Versagung ist ein Verwaltungsakt; die Genehmigungserteilung wird mit der Verpflichtungsklage verfolgt. Für Bundesbeamte gelten §§ 97 ff. BBG mit eigener Systematik. Nach Beendigung des Beamtenverhältnisses greift die Anzeigepflicht des [§ 41 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__41.html).

### 7. Fürsorgepflicht ([§ 45 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__45.html))

Der Dienstherr hat für das Wohl der Beamten und ihrer Familien zu sorgen und sie bei ihrer amtlichen Tätigkeit sowie in ihrer Stellung zu schützen. Die Fürsorgepflicht ist Auffangnorm und Ermessensdirektive zugleich: Sie begründet selten einen unmittelbaren Zahlungsanspruch, verdichtet aber das Ermessen bei Versetzung, Umsetzung, Teilzeit, Urlaub und Konfliktlagen am Arbeitsplatz. Ihre Verletzung kann Schadensersatzansprüche aus dem Beamtenverhältnis auslösen.

### 8. Remonstration ([§ 36 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__36.html))

Beamte tragen für die Rechtmäßigkeit ihrer dienstlichen Handlungen die **volle persönliche Verantwortung**. Bei Bedenken gegen die Rechtmäßigkeit einer Weisung gilt ein dreistufiges Verfahren:

1. Bedenken **unverzüglich** beim unmittelbaren Vorgesetzten geltend machen.
2. Bleibt die Weisung bestehen: Bedenken beim **nächsthöheren** Vorgesetzten geltend machen.
3. Bestätigt auch dieser die Weisung, ist sie auszuführen; die Verantwortung geht auf den Vorgesetzten über. Die Bestätigung ist auf Verlangen schriftlich zu erteilen.

**Ausnahme**: Bei Weisungen, deren Befolgung erkennbar strafbar oder ordnungswidrig wäre oder die Menschenwürde verletzt, entfällt die Gehorsamspflicht **vollständig**. Für Bundesbeamte gelten §§ 62, 63 BBG parallel. Die Remonstration ist stets schriftlich zu dokumentieren — sie ist zugleich das wirksamste Verteidigungsmittel in einem späteren Disziplinarverfahren (`/beamten-disziplinarrecht:disziplinarverfahren`).

## Quellen

### Statute

- [§ 8 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__8.html), [§ 11 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__11.html), [§ 12 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__12.html), [§ 14 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__14.html), [§ 15 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__15.html), [§ 23 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__23.html), [§ 26 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__26.html), [§ 27 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__27.html), [§ 35 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__35.html), [§ 36 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__36.html), [§ 40 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__40.html), [§ 41 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__41.html), [§ 45 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__45.html)
- [BBG](https://www.gesetze-im-internet.de/bbg_2009/) — insbesondere §§ 44 f., 62, 63, 78, 97 ff.
- [§ 31 BeamtVG](https://www.gesetze-im-internet.de/beamtvg/__31.html), [§ 45 BeamtVG](https://www.gesetze-im-internet.de/beamtvg/__45.html)
- [§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html), [§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html), [§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html), [§ 123 VwGO](https://www.gesetze-im-internet.de/vwgo/__123.html)
- Landesbeamtengesetze, Landesbeamtenversorgungs- und Landesbeihilferecht `[unverifiziert - prüfen]`

### Kommentare

- Plog/Wiedow, BBG / BeamtVG, Loseblatt, § 45 BeamtVG Rn. 1 ff.
- von Roetteken, in: von Roetteken/Rothländer, BeamtStG, §§ 14, 15, 26 Rn. 1 ff.
- Battis, BBG, §§ 27 ff., 44 ff. Rn. 1 ff.
- Reich, BeamtStG, § 26 Rn. 1 ff.
- Schnellenbach/Bodanowitz, Beamtenrecht in der Praxis, Kap. Umsetzung, Abordnung, Versetzung.

### Rechtsprechung

1. BVerwG, Urt. v. 05.06.2014 – 2 C 22.13, BVerwGE 150, 1 = NVwZ 2014, 1319 (Anforderungen an das ärztliche Gutachten bei Dienstunfähigkeit) ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=2014-06-05&Aktenzeichen=2%20C%2022.13))
2. BVerwG, Urt. v. 04.11.2010 – 2 C 16.09, BVerwGE 138, 102 = NJW 2011, 695 (Ernennung und Ämterstabilität) ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=2010-11-04&Aktenzeichen=2%20C%2016.09))
3. Zur Abgrenzung Umsetzung / Versetzung und zur Kausalität im Dienstunfallrecht ist die Senatsrechtsprechung im Einzelfall zu recherchieren `[unverifiziert - prüfen]`

## Ausgabeformat

```
BEAMTENSTATUSRECHT — <Mandat> — <Datum>

I.   Anwendbares Recht
     Dienstherr:              <Bund / Land <X> / Kommune>
     Statusrecht:             <BBG | BeamtStG + LBG <X>>
     Versorgung / Beihilfe:   <BeamtVG + BBhV | Landesrecht <X>>

II.  Maßnahme
     Gegenstand:              <Ernennung / Umsetzung / Abordnung / Versetzung /
                               Zurruhesetzung / Dienstunfall / Nebentätigkeit>
     Datum / Zugang:          <…>
     Rechtsbehelfsbelehrung:  [vorhanden / fehlt / unrichtig]

III. Rechtsnatur
     Verwaltungsakt:          [ja / nein]  Begründung: <…>
     Statthafte Klageart:     <Anfechtung / Verpflichtung / allg. Leistungsklage>
     Eilrechtsschutz:         <§ 80 Abs. 5 VwGO / § 123 VwGO / entbehrlich>

IV.  Materielle Prüfung
     Ermächtigungsgrundlage:  <§ N BeamtStG / BBG>
     Formelle Rechtmäßigkeit: <Zuständigkeit / Anhörung / Form>
     Materielle Rechtmäßigkeit: <Tatbestand / Ermessen / Fürsorge § 45 BeamtStG>
     Besonderheiten:          <Suche nach anderweitiger Verwendung /
                               Untersuchungsanordnung / Interessenkollision>

V.   Fristen
     Widerspruch / Klage:     bis <Datum>
     Meldefrist § 45 BeamtVG: [gewahrt / versäumt / offen]

VI.  Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VII. Quellenverzeichnis
```

### Formulierungshilfe — Remonstration nach § 36 BeamtStG (Gerüst)

```
An <unmittelbare Vorgesetzte / unmittelbaren Vorgesetzten>
nachrichtlich: <nächsthöhere Vorgesetzte>

Remonstration nach § 36 Abs. 2 BeamtStG
Betr.: Weisung vom <Datum>, <Gegenstand>

Sehr geehrte Frau / sehr geehrter Herr <…>,

gegen die Rechtmäßigkeit der o. g. Weisung mache ich hiermit
unverzüglich Bedenken geltend.

1. Inhalt der Weisung
   <wörtliche oder sinngemäße Wiedergabe, Datum, Form>

2. Rechtliche Bedenken
   Die Ausführung verstieße gegen <Norm>, weil <…>.

3. Folge
   Ich bitte um Prüfung und um Mitteilung, ob die Weisung
   aufrechterhalten wird. Für den Fall der Aufrechterhaltung bitte
   ich um schriftliche Bestätigung (§ 36 Abs. 2 S. 3 BeamtStG) und
   werde die Weisung sodann ausführen; die Verantwortung geht auf
   die Vorgesetzte bzw. den Vorgesetzten über.

Hinweis: Sollte die Ausführung ein Straftat- oder
Ordnungswidrigkeitstatbestand erfüllen, entfällt die Gehorsamspflicht
nach § 36 Abs. 3 BeamtStG vollständig.
```

## Risiken / typische Fehler

- **Umsetzung als Verwaltungsakt behandelt.** Die Anfechtungsklage gegen eine Umsetzung ist unstatthaft; statthaft sind allgemeine Leistungsklage und § 123 VwGO.
- **BeamtStG auf Bundesbeamte angewandt.** Das BeamtStG gilt für die Länder; für Bundesbeamte ist stets die BBG-Parallelnorm zu zitieren.
- **Landesbeihilfe- und Landesversorgungsrecht durch BeamtVG ersetzt.** Beides ist seit der Föderalismusreform I landesrechtlich geregelt.
- **Meldefrist § 45 BeamtVG versäumt.** Es handelt sich um eine materielle Ausschlussfrist, nicht um eine Ordnungsvorschrift.
- **Suche nach anderweitiger Verwendung nicht gerügt.** Ihr Unterlassen macht die Zurruhesetzung rechtswidrig und ist der wirksamste Angriffspunkt.
- **Untersuchungsanordnung ungeprüft befolgt oder verweigert.** Eine pauschale Anordnung ist rechtswidrig; eine rechtmäßige Anordnung darf nicht folgenlos verweigert werden.
- **Remonstration nicht dokumentiert.** Ohne schriftliche Remonstration fehlt im späteren Disziplinarverfahren das entscheidende Entlastungsmittel.
- **Aktenzeichen erfunden** — jede Entscheidung verifizieren oder als `[unverifiziert - prüfen]` kennzeichnen.
