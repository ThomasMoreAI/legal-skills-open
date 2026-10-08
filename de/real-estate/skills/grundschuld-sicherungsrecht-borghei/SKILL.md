---
name: grundschuld-sicherungsrecht-borghei
title: /immobilien-grundbuchrecht:grundschuld-sicherungsrecht
description: Grundschuld als Kreditsicherheit – Bestellung und Inhalt §§ 1191 ff. BGB, Sicherungsabrede als schuldrechtliches Band zwischen Grundschuld und Darlehen, Unterwerfung unter die sofortige Zwangsvollstreckung § 794 Abs. 1 Nr. 5 ZPO nebst Klauselerteilung § 726 ZPO und Rechtsnachfolgeklausel § 727 ZPO, Abtretung §§ 1192, 1154 BGB, Einredeschutz des Eigentümers gegen den Zessionar nach § 1192 Abs. 1a BGB, Rückgewähranspruch und Löschungsbewilligung, Abgrenzung zur akzessorischen Hypothek § 1113 BGB. Use when eine Grundschuld bestellt, eine Sicherungszweckerklärung geprüft, eine Grundschuld abgetreten oder zurückgefordert oder gegen die Vollstreckung aus einer Grundschuld vorgegangen wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/immobilien-grundbuchrecht/skills/grundschuld-sicherungsrecht
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /immobilien-grundbuchrecht:grundschuld-sicherungsrecht

## Zweck

Die Grundschuld ist das mit Abstand häufigste Grundpfandrecht der deutschen Kreditpraxis — und die einzige, deren Verbindung zur gesicherten Forderung **nicht im Gesetz, sondern im Vertrag** liegt. Wer diesen Bruch nicht versteht, unterschätzt systematisch die Risiken: Die Grundschuld besteht fort, wenn das Darlehen getilgt ist, und sie kann isoliert abgetreten werden. Dieser Skill gestaltet und prüft Grundschuldbestellung, Sicherungsabrede und Vollstreckungsunterwerfung und ordnet die Verteidigungslinien des Eigentümers ein.

## Eingaben

- **Rolle**: Kreditgeberin, Sicherungsgeberin (Eigentümerin), Käuferin mit Belastungsvollmacht, Drittsicherungsgeberin
- **Grundstück** und aktueller Grundbuchstand in Abteilung III (Rang, valutierende und nicht valutierende Rechte)
- **Grundschuldbetrag**, Zinssatz (grundbuchlich meist 12–18 % p. a.), Nebenleistung
- **Gesicherte Forderung**: Darlehensvertrag, Kontokorrent, weiter oder enger Sicherungszweck
- Vorliegende **Sicherungszweckerklärung** im Wortlaut; Formular oder Individualvereinbarung
- **Unterwerfungsklausel**: nur dingliche Unterwerfung oder zusätzlich persönliche Schuldübernahme?
- Bei Abtretung: Zessionar, Zeitpunkt, Kenntnis vom Sicherungscharakter, Stand der Valutierung
- Bei Rückabwicklung: Tilgungsstand, bereits erteilte Löschungsbewilligung, weitere Sicherungsnehmer

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) beschafft §§ 1113–1192 BGB, §§ 726–727, 794, 797 ZPO mit URL sowie Kommentarstellen (Grüneberg, MüKoBGB, Clemente Recht der Sicherungsgrundschuld).
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Bestellungsurkunde, Zweckerklärung oder Verteidigungsschriftsatz.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Sicherungszweck, Unterwerfungsumfang, Klauselgrundlage und Rückgewährregelung.

## Ablauf

### 1. Abgrenzung Grundschuld / Hypothek ([§ 1113 BGB](https://www.gesetze-im-internet.de/bgb/__1113.html), [§ 1191 BGB](https://www.gesetze-im-internet.de/bgb/__1191.html))

Die **Hypothek** ist **akzessorisch**: Sie setzt eine Forderung voraus, folgt ihr in Bestand und Höhe und geht mit ihrer Tilgung in eine Eigentümergrundschuld über. Die **Grundschuld** ist **nicht akzessorisch** (§ 1192 Abs. 1 BGB): Sie belastet das Grundstück auf Zahlung einer bestimmten Geldsumme, unabhängig davon, ob eine Forderung besteht. Praktische Folgen:

- Die Grundschuld bleibt bei Tilgung des Darlehens **in voller Höhe bestehen**; sie kann für ein neues Darlehen wiederverwendet werden — das ist ihr wirtschaftlicher Vorteil.
- Der Eigentümer hat gegen die Gläubigerin einen schuldrechtlichen **Rückgewähranspruch**, keinen automatischen Rechtsübergang.
- Das Bindeglied zur Forderung ist allein die **Sicherungsabrede**. Fällt sie weg oder wird sie überschritten, wirkt das nur schuldrechtlich — als Einrede, nicht dinglich.

### 2. Bestellung und Inhalt ([§ 1191 BGB](https://www.gesetze-im-internet.de/bgb/__1191.html), [§ 873 BGB](https://www.gesetze-im-internet.de/bgb/__873.html))

Die Grundschuld entsteht durch **Einigung und Eintragung**. Einzutragen sind Gläubiger, Geldbetrag, Zinssatz und Nebenleistung sowie der Rang. Regelmäßig wird die **Buchgrundschuld** gewählt: Die Erteilung des Briefs wird nach [§ 1192 BGB](https://www.gesetze-im-internet.de/bgb/__1192.html) i. V. m. [§ 1116 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__1116.html) ausgeschlossen, weil der Briefverlust die Abwicklung blockiert. Der eingetragene **Zinssatz** liegt bewusst über dem Vertragszins; er ist kein Darlehenszins, sondern eine dingliche Reserve für Verzugsschaden und Kosten. Wird die Grundschuld vom Käufer vor Eigentumsumschreibung bestellt, geschieht das aufgrund **Belastungsvollmacht** des Verkäufers; deren Zweckbindung ist zwingend. Vertiefung: `/immobilien-grundbuchrecht:grundstueckskaufvertrag`.

### 3. Sicherungsabrede und Sicherungszweck

Die **Sicherungsabrede** (Sicherungszweckerklärung) verknüpft die abstrakte Grundschuld mit der zu sichernden Forderung. Sie ist der eigentliche Prüfungsgegenstand:

- **Enger Sicherungszweck**: Gesichert ist nur die im Vertrag konkret bezeichnete Forderung. Für Drittsicherungsgeber der einzig zumutbare Zuschnitt.
- **Weiter Sicherungszweck**: Gesichert sind alle bestehenden und künftigen Ansprüche der Gläubigerin aus der Geschäftsverbindung. In Formularen gegenüber dem persönlichen Schuldner verbreitet; gegenüber einem **Drittsicherungsgeber** ist eine formularmäßige Erstreckung auf fremde und künftige Verbindlichkeiten überraschend und benachteiligend (§§ 305c, 307 BGB).
- Aus der Sicherungsabrede folgt die **Einrede der Nichtvalutierung** und der Übersicherung: Der Eigentümer kann der Inanspruchnahme entgegenhalten, dass die gesicherte Forderung nicht oder nicht mehr besteht.
- Sie begründet ferner den **Rückgewähranspruch** und die Pflicht der Gläubigerin, freigewordene Sicherheiten freizugeben.

### 4. Unterwerfung unter die sofortige Zwangsvollstreckung ([§ 794 Abs. 1 Nr. 5 ZPO](https://www.gesetze-im-internet.de/zpo/__794.html))

In der Bestellungsurkunde unterwirft sich der Eigentümer wegen des Grundschuldbetrags nebst Zinsen der **sofortigen Zwangsvollstreckung in das Grundstück** (dingliche Unterwerfung); zusätzlich übernimmt der Schuldner regelmäßig die **persönliche Haftung** für den Betrag und unterwirft sich auch insoweit der Vollstreckung in sein gesamtes Vermögen. Damit entsteht ein vollstreckbarer Titel **ohne Gerichtsverfahren** — der Grund, weshalb Grundschuldvollstreckung so schnell läuft.

Prüfpunkte:

- Die formularmäßige Unterwerfung unter die sofortige Zwangsvollstreckung aus einer Sicherungsgrundschuld ist nicht ohne Weiteres unwirksam; ihre AGB-rechtliche Beurteilung bei freier Abtretbarkeit von Darlehensforderung und Grundschuld hat der BGH behandelt (BGH, Urt. v. 30.03.2010 – XI ZR 200/09 — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2010-03-30&Aktenzeichen=XI%20ZR%20200/09).
- Umfang der Unterwerfung genau lesen: nur dinglich oder auch persönlich? Nur der Sicherungsgeber oder auch der Ehegatte?
- Die vollstreckbare Ausfertigung erteilt der Notar; bei Abhängigkeit von einer Bedingung greift [§ 726 ZPO](https://www.gesetze-im-internet.de/zpo/__726.html), bei Rechtsnachfolge auf Gläubiger- oder Schuldnerseite [§ 727 ZPO](https://www.gesetze-im-internet.de/zpo/__727.html).
- Verteidigung: Einwendungen gegen den titulierten Anspruch mit der **Vollstreckungsabwehrklage** ([§ 767 ZPO](https://www.gesetze-im-internet.de/zpo/__767.html), bei notariellen Urkunden ohne Präklusion nach [§ 797 Abs. 4 ZPO](https://www.gesetze-im-internet.de/zpo/__797.html)); Einwände gegen die Klausel mit der Klauselerinnerung [§ 732 ZPO](https://www.gesetze-im-internet.de/zpo/__732.html). Vertiefung: `/prozessrecht:vollstreckungsabwehrklage` und `/zwangsvollstreckung:vollstreckungsvoraussetzungen`.

### 5. Abtretung ([§ 1192 BGB](https://www.gesetze-im-internet.de/bgb/__1192.html), [§ 1154 BGB](https://www.gesetze-im-internet.de/bgb/__1154.html))

Die Grundschuld wird nach § 1192 Abs. 1 BGB i. V. m. § 1154 BGB übertragen: bei der Buchgrundschuld durch **Einigung und Eintragung** (§ 1154 Abs. 3 BGB), bei der Briefgrundschuld durch schriftliche Abtretungserklärung und Briefübergabe. Weil die Grundschuld nicht akzessorisch ist, kann sie **isoliert von der Darlehensforderung** übertragen werden — genau darin lag das Risiko der Kreditverkäufe: Der Erwerber konnte aus dem Titel vollstrecken, ohne an die Sicherungsabrede gebunden zu sein.

### 6. Einredeschutz gegen den Zessionar ([§ 1192 Abs. 1a BGB](https://www.gesetze-im-internet.de/bgb/__1192.html))

Auf diese Lücke hat der Gesetzgeber mit § 1192 Abs. 1a BGB reagiert: Bei einer Grundschuld, die zur Sicherung eines Anspruchs verschafft worden ist (**Sicherungsgrundschuld**), können Einreden aus dem Sicherungsvertrag **auch jedem Erwerber der Grundschuld entgegengesetzt** werden; § 1157 S. 2 BGB findet keine Anwendung. Ein **gutgläubiger einredefreier Erwerb** ist damit bei der Sicherungsgrundschuld **ausgeschlossen**. Praktische Konsequenzen:

- Der Eigentümer behält die Einrede der Nichtvalutierung auch gegenüber dem Zessionar.
- Der Erwerber muss den Valutastand ermitteln; ein Vertrauen auf das Grundbuch hilft ihm insoweit nicht.
- Der Ausschluss gilt nur für **Sicherungs**grundschulden; bei der isolierten Grundschuld ohne Sicherungszweck bleibt es beim allgemeinen Gutglaubensschutz.
- Die persönliche Unterwerfung folgt eigenen Regeln — hier kann die Rechtsnachfolgeklausel nach § 727 ZPO gesondert angegriffen werden.

### 7. Rückgewähranspruch und Löschungsbewilligung

Ist die gesicherte Forderung erloschen oder der Sicherungszweck entfallen, hat der Sicherungsgeber aus der Sicherungsabrede einen **Rückgewähranspruch**. Er ist ein **Wahlrecht** mit drei Optionen: Löschungsbewilligung (Erlöschen des Rechts), Verzicht der Gläubigerin mit der Folge einer **Eigentümergrundschuld** ([§ 1168 BGB](https://www.gesetze-im-internet.de/bgb/__1168.html) i. V. m. § 1192 BGB), oder **Abtretung** der Grundschuld an den Eigentümer oder einen Dritten. Wirtschaftlich ist die Löschung oft der schlechteste Weg: Nachrangige Rechte rücken auf, und der freie Rang geht verloren. Wer refinanzieren will, lässt sich die Grundschuld **abtreten**. Der Rückgewähranspruch ist selbst pfändbar und wird von Zweitgläubigern regelmäßig gepfändet — vor jeder Rückabwicklung ist Abteilung III auf Pfändungsvermerke zu prüfen.

## Deterministische Berechnung

Rückständige Darlehensraten und Zinsen auf die gesicherte Forderung sind Arithmetik; der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur diese**. Ob Verzug eingetreten ist, ob eine wirksame Kündigung des Darlehens vorliegt und welcher Zinssatz gilt, bleiben juristische Eingaben. Der **Basiszinssatz ist Pflichteingabe** und gegen die Veröffentlichung der Deutschen Bundesbank zu prüfen; der grundbuchlich eingetragene Grundschuldzins ist **nicht** der Verzugszins.

```bash
# Verzugszinsen auf eine fällig gestellte Darlehensrestforderung
python -m scripts.legal_calc.cli verzugszinsen --betrag 180000 \
    --verzug-ab 01.02.2026 --bis 21.07.2026 --basiszins 01.01.2026:1.10

# Kosten eines Rechtsstreits über den Rückgewähranspruch (Geschäftswert 180.000 EUR)
python -m scripts.legal_calc.cli rvg --wert 180000 --posten verfahren termin
python -m scripts.legal_calc.cli gkg --wert 180000 --faktor 3.0
```

`--json` liefert die Rechenschritte samt Normzitat maschinenlesbar.

## Quellen

### Statute

- [§ 1113 BGB](https://www.gesetze-im-internet.de/bgb/__1113.html) (Hypothek), [§ 1116 BGB](https://www.gesetze-im-internet.de/bgb/__1116.html), [§ 1154 BGB](https://www.gesetze-im-internet.de/bgb/__1154.html), [§ 1157 BGB](https://www.gesetze-im-internet.de/bgb/__1157.html), [§ 1168 BGB](https://www.gesetze-im-internet.de/bgb/__1168.html)
- [§ 1191 BGB](https://www.gesetze-im-internet.de/bgb/__1191.html), [§ 1192 BGB](https://www.gesetze-im-internet.de/bgb/__1192.html) (einschließlich Abs. 1a), [§ 873 BGB](https://www.gesetze-im-internet.de/bgb/__873.html)
- [§ 305c BGB](https://www.gesetze-im-internet.de/bgb/__305c.html), [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html) (AGB-Kontrolle der Zweckerklärung)
- [§ 726 ZPO](https://www.gesetze-im-internet.de/zpo/__726.html), [§ 727 ZPO](https://www.gesetze-im-internet.de/zpo/__727.html), [§ 732 ZPO](https://www.gesetze-im-internet.de/zpo/__732.html), [§ 767 ZPO](https://www.gesetze-im-internet.de/zpo/__767.html), [§ 794 ZPO](https://www.gesetze-im-internet.de/zpo/__794.html), [§ 797 ZPO](https://www.gesetze-im-internet.de/zpo/__797.html)

### Kommentare

- Herrler, in: Grüneberg, BGB, 84. Aufl. 2025, § 1191 Rn. 1 ff.; § 1192 Rn. 1 ff.
- Lieder, in: MüKoBGB, 9. Aufl. 2023, § 1191 Rn. 1 ff.; § 1192 Rn. 1 ff.
- Clemente, Recht der Sicherungsgrundschuld, 5. Aufl. 2019, Rn. 1 ff.
- Schöner/Stöber, Grundbuchrecht, 16. Aufl. 2020, Rn. 1 ff. (Grundpfandrechte)

### Rechtsprechung

- BGH, Urt. v. 30.03.2010 – XI ZR 200/09 (formularmäßige Unterwerfung unter die sofortige Zwangsvollstreckung aus einer Sicherungsgrundschuld bei freier Abtretbarkeit; §§ 305c, 307 BGB, §§ 727, 732 ZPO) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2010-03-30&Aktenzeichen=XI%20ZR%20200/09
- Zur Inhaltskontrolle formularmäßiger weiter Sicherungszweckerklärungen gegenüber Drittsicherungsgebern ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.
- Zum Inhalt und zur Ausübung des Rückgewähranspruchs sowie zu dessen Pfändbarkeit ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`. Kein Aktenzeichen ohne eigene Verifikation in juris / Beck-Online übernehmen.

## Formulierungshilfe — Bestellung, Zweckerklärung, Rückgewähr

```
§ __ Grundschuldbestellung
Der Eigentümer bestellt hiermit zugunsten der <Gläubigerin> eine Grundschuld
ohne Brief über <Betrag> EUR nebst <…> % Jahreszinsen seit heute und einer
einmaligen Nebenleistung von <…> % an dem Grundbesitz <Gemarkung, Blatt>.
Die Erteilung eines Grundschuldbriefs ist ausgeschlossen (§ 1116 Abs. 2 BGB).
Die Eintragung im Rang nach <…> und im Übrigen an erster Rangstelle in
Abteilung III wird bewilligt und beantragt.

§ __ Unterwerfung unter die sofortige Zwangsvollstreckung
Der Eigentümer unterwirft sich wegen des Grundschuldbetrags nebst Zinsen und
Nebenleistung der sofortigen Zwangsvollstreckung in den belasteten Grundbesitz
in der Weise, dass die Zwangsvollstreckung gegen den jeweiligen Eigentümer
zulässig ist (§ 800 ZPO). Der Schuldner übernimmt zugleich die persönliche
Haftung für die Zahlung des Grundschuldbetrags nebst Zinsen und unterwirft
sich insoweit der sofortigen Zwangsvollstreckung in sein gesamtes Vermögen
(§ 794 Abs. 1 Nr. 5 ZPO). Vollstreckbare Ausfertigung kann jederzeit ohne
Nachweis der die Fälligkeit begründenden Tatsachen erteilt werden.

§ __ Sicherungszweckerklärung (enger Zweck)
Die Grundschuld dient ausschließlich der Sicherung der Ansprüche der
Gläubigerin aus dem Darlehensvertrag vom <Datum>, Konto-Nr. <…>, nebst
Zinsen und Kosten. Eine Erstreckung auf sonstige bestehende oder künftige
Forderungen aus der Geschäftsverbindung ist ausdrücklich ausgeschlossen.
Die Gläubigerin ist verpflichtet, die Grundschuld nach vollständiger
Rückführung der gesicherten Forderung nach Wahl des Sicherungsgebers zu
löschen, auf ihn zu übertragen oder auf sie zu verzichten.

Aufforderung zur Rückgewähr
Die gesicherte Forderung ist durch Zahlung vom <Datum> vollständig erloschen.
Namens der Sicherungsgeberin fordere ich Sie auf, die Grundschuld bis zum
<Datum> an die Sicherungsgeberin abzutreten; die Wahl des Rückgewährwegs
wird hiermit ausdrücklich in diesem Sinne ausgeübt. Eine Löschung wird
ausdrücklich nicht gewünscht.
```

## Ausgabeformat

```
GRUNDSCHULD / SICHERUNGSRECHT — <Bestellung / Prüfung / Rückgewähr> — <Datum>

I.    Rolle / Grundstück            <…>
II.   Rechtsnatur                   Grundschuld § 1191 BGB (nicht akzessorisch)
      Abgrenzung Hypothek § 1113    [N/A / relevant]
III.  Bestellung                    Betrag <…>  Zins <…> %  Rang <…>
      Brief ausgeschlossen          [✅ Buchgrundschuld / Briefgrundschuld]
      Belastungsvollmacht           [N/A / zweckgebunden ✅ / 🔴 ungebunden]
IV.   Sicherungsabrede              [enger / weiter Zweck]
      Drittsicherungsgeber          [N/A / 🔴 weiter Zweck unwirksam §§ 305c, 307]
      Valutastand                   <Betrag>   Übersicherung [nein / ja]
V.    Unterwerfung § 794 I Nr. 5    dinglich [✅]  persönlich [✅ / ❌]
      § 800 ZPO gegen Rechtsnachf.  [✅ / ❌]
VI.   Abtretung §§ 1192, 1154       [N/A / erfolgt am <Datum> an <…>]
      Einredeschutz § 1192 Abs. 1a  [greift — kein gutgläubig einredefreier
                                     Erwerb / nicht einschlägig]
VII.  Rückgewähranspruch            Wahl: [Löschung / Abtretung / Verzicht]
      Pfändung des Rückgewähranspr. [keine / 🔴 eingetragen]
VIII. Rechtsbehelfe                 §§ 732, 767, 797 Abs. 4 ZPO — <…>
IX.   Zinsen / Kosten               s. Deterministische Berechnung

Ergebnis: <bestellungsreif / Zweckerklärung nachbessern / Vollstreckung angreifbar>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Akzessorietät unterstellt** — die Grundschuld erlischt nicht mit der Tilgung; wer nach Rückzahlung nichts unternimmt, lässt eine vollwirksame Sicherheit im Grundbuch stehen.
- **Weiter Sicherungszweck beim Drittsicherungsgeber** — die formularmäßige Erstreckung auf fremde und künftige Verbindlichkeiten ist überraschend und benachteiligend (§§ 305c, 307 BGB).
- **Umfang der Unterwerfung nicht gelesen** — die persönliche Schuldübernahme nach § 794 Abs. 1 Nr. 5 ZPO öffnet die Vollstreckung in das gesamte Vermögen, nicht nur in das Grundstück.
- **Rückgewähranspruch als Löschung ausgeübt** — nachrangige Rechte rücken auf und der freie Rang geht verloren; wirtschaftlich richtig ist meist die Abtretung.
- **Pfändung des Rückgewähranspruchs übersehen** — Zweitgläubiger haben ihn gepfändet; eine Rückabwicklung an den Eigentümer geht dann ins Leere.
- **Einredeschutz § 1192 Abs. 1a BGB verkannt** — er gilt nur für Sicherungsgrundschulden und schützt nicht gegen die persönliche Unterwerfung; die Rechtsnachfolgeklausel § 727 ZPO ist gesondert zu prüfen.
- **Grundschuldzins mit Verzugszins verwechselt** — der eingetragene Zinssatz ist eine dingliche Reserve, kein Anspruch auf Vertragszinsen.
