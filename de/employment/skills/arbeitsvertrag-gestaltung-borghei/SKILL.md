---
name: arbeitsvertrag-gestaltung-borghei
title: /arbeitsrecht:arbeitsvertrag-gestaltung
description: Gestaltung und AGB-Kontrolle des Arbeitsvertrages – Anwendung der §§ 305–310 BGB im Arbeitsrecht mit der Besonderheit des § 310 Abs. 4 S. 2 BGB, Transparenzgebot § 307 Abs. 1 S. 2 BGB und Verbot der geltungserhaltenden Reduktion, zweistufige Ausschlussfrist mit der zwingenden Ausnahme für den Mindestlohn (§ 3 MiLoG) und weitere unabdingbare Ansprüche, Widerrufs- und Freiwilligkeitsvorbehalte, Vertragsstrafe, Nachweispflichten § 2 NachwG in der Fassung seit 01.08.2022 samt Bußgeld § 4 NachwG, Verhältnis von Textform (Nachweis) und Schriftform (§ 623 BGB, § 14 Abs. 4 TzBfG). Use when ein Arbeitsvertrag oder ein Vertragsmuster entworfen, überarbeitet oder auf Unwirksamkeit einzelner Klauseln geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/arbeitsrecht/skills/arbeitsvertrag-gestaltung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /arbeitsrecht:arbeitsvertrag-gestaltung

## Zweck

Arbeitsverträge sind Allgemeine Geschäftsbedingungen. Seit der Schuldrechtsreform unterliegen sie der Inhaltskontrolle der §§ 305 ff. BGB — mit der für den Verwender unangenehmsten aller Rechtsfolgen: Eine unwirksame Klausel wird **nicht** auf das zulässige Maß zurückgeführt, sondern ersatzlos gestrichen. Dieser Skill entwirft Klauseln, die diese Kontrolle überstehen, und prüft bestehende Verträge auf die Klauseln, die es typischerweise nicht tun.

## Eingaben

- Vertragstyp: unbefristet / befristet / Teilzeit / geringfügig / leitender Angestellter
- Tarifbindung (beiderseits, OT-Mitgliedschaft, Bezugnahmeklausel?), Betriebsvereinbarungen
- Vergütungsstruktur: Fixum, variable Bestandteile, Boni, Sonderzahlungen, Sachbezüge
- Gewünschte Flexibilisierungen: Versetzung, Widerruf von Zulagen, Überstundenabgeltung, Vertragsstrafe, nachvertragliches Wettbewerbsverbot
- Verwendungsabsicht: Einzelvertrag oder **Vertragsmuster** (dann ist die AGB-Kontrolle in jedem Fall eröffnet)

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert §§ 305–310 BGB, NachwG, MiLoG mit URL sowie die BAG-Linien zu Ausschlussfristen und Widerrufsvorbehalten.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) formuliert die Klauseln und die Nachweis-Checkliste.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Transparenz, Unabdingbarkeitsgrenzen und Formerfordernisse.

## Ablauf

### 1. Eröffnung der AGB-Kontrolle ([§ 305 BGB](https://www.gesetze-im-internet.de/bgb/__305.html), [§ 310 BGB](https://www.gesetze-im-internet.de/bgb/__310.html))

Der Arbeitnehmer ist **Verbraucher** im Sinne des § 13 BGB; Arbeitsverträge sind Verbraucherverträge. Daraus folgt:

- **Einmalbedingungen** unterliegen nach § 310 Abs. 3 Nr. 2 BGB der Inhaltskontrolle, auch wenn sie nur für eine Verwendung bestimmt sind. Der Einwand „das war ein individuell ausgehandelter Vertrag" trägt praktisch nie.
- **Aushandeln** (§ 305 Abs. 1 S. 3 BGB) erfordert, dass der Verwender den Kerngehalt ernsthaft zur Disposition stellt. Bloßes Verhandeln über das Gehalt macht die übrigen Klauseln nicht zu Individualabreden.
- **§ 310 Abs. 4 S. 2 BGB:** Bei der Anwendung auf Arbeitsverträge sind die **im Arbeitsrecht geltenden Besonderheiten angemessen zu berücksichtigen**. Praktische Folge: Die Klauselverbote der §§ 308, 309 BGB gelten nicht schematisch; § 309 Nr. 6 BGB (Vertragsstrafenverbot) ist im Arbeitsrecht nicht anwendbar, die Vertragsstrafe unterliegt aber der Angemessenheitskontrolle nach § 307 BGB.
- **Keine Kontrolle** unterliegen Tarifverträge, Betriebs- und Dienstvereinbarungen (§ 310 Abs. 4 S. 1, 3 BGB) — auch nicht, wenn sie durch Bezugnahme in Kraft gesetzt werden.

### 2. Die drei scharfen Kontrollmaßstäbe

| Maßstab | Norm | Wirkung |
|---|---|---|
| Überraschende Klausel | § 305c Abs. 1 BGB | Wird nicht Vertragsbestandteil (z. B. Wettbewerbsverbot unter „Sonstiges") |
| Unklarheitenregel | § 305c Abs. 2 BGB | Zweifel gehen zulasten des Verwenders |
| Transparenzgebot | [§ 307 Abs. 1 S. 2 BGB](https://www.gesetze-im-internet.de/bgb/__307.html) | Unklare Klausel ist **allein deshalb** unwirksam |

**Verbot der geltungserhaltenden Reduktion:** Eine zu weit gefasste Klausel wird nicht auf das zulässige Maß gestutzt, sondern fällt vollständig weg; an ihre Stelle tritt das dispositive Gesetzesrecht (§ 306 Abs. 2 BGB). Ein **Blue-Pencil-Test** rettet nur, was sprachlich und inhaltlich abtrennbar ist. **Salvatorische Klauseln** helfen im AGB-Recht nicht.

### 3. Ausschlussfristen — die wichtigste Einzelklausel

Zulässig ist eine **zweistufige** Ausschlussfrist:

- **Stufe 1:** schriftliche bzw. textförmliche Geltendmachung gegenüber der anderen Partei,
- **Stufe 2:** gerichtliche Geltendmachung nach Ablehnung oder Schweigen.

Grenzen, die jede Stufe einhalten muss:

1. **Mindestdauer je Stufe: drei Monate.** Kürzere Fristen benachteiligen unangemessen (§ 307 Abs. 1 S. 1 BGB) — st. Rspr. des BAG zur Mindestlänge arbeitsvertraglicher Ausschlussfristen `[unverifiziert – prüfen]`.
2. **Form der ersten Stufe:** Für nach dem 30.09.2016 geschlossene Verträge darf **keine strengere Form als Textform** verlangt werden ([§ 309 Nr. 13 BGB](https://www.gesetze-im-internet.de/bgb/__309.html)). Eine Klausel, die „Schriftform" fordert, ist insgesamt unwirksam.
3. **Mindestlohn-Ausnahme:** Der Anspruch auf den gesetzlichen Mindestlohn ist nach [§ 3 MiLoG](https://www.gesetze-im-internet.de/milog/__3.html) unabdingbar; eine Ausschlussfrist, die ihn nicht ausdrücklich ausnimmt, ist nach der Rechtsprechung **intransparent und damit insgesamt unwirksam** — nicht etwa nur bezogen auf den Mindestlohn `[unverifiziert – prüfen]`. Das ist der häufigste Totalausfall in Altverträgen.
4. Weitere Ansprüche, die **nicht** erfasst werden dürfen: Haftung für Vorsatz ([§ 202 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__202.html)), Ansprüche aus vorsätzlicher unerlaubter Handlung, tariflich unabdingbare Ansprüche, Ansprüche nach dem AEntG und dem AÜG.

**Formulierungshilfe — zweistufige Ausschlussfrist:**

```
§ <N> Ausschlussfristen

(1) Alle Ansprüche aus dem Arbeitsverhältnis und solche, die mit
    dem Arbeitsverhältnis in Verbindung stehen, verfallen, wenn
    sie nicht innerhalb von drei Monaten nach Fälligkeit
    gegenüber der anderen Vertragspartei in Textform geltend
    gemacht werden.

(2) Lehnt die andere Vertragspartei den Anspruch in Textform ab
    oder erklärt sie sich nicht innerhalb von drei Monaten nach
    Geltendmachung, verfällt der Anspruch, wenn er nicht
    innerhalb von drei Monaten nach der Ablehnung oder dem
    Fristablauf gerichtlich geltend gemacht wird.

(3) Von den Absätzen 1 und 2 ausgenommen sind:
    a) Ansprüche auf den gesetzlichen Mindestlohn nach dem
       Mindestlohngesetz sowie auf Vergütung nach dem
       Arbeitnehmer-Entsendegesetz und dem
       Arbeitnehmerüberlassungsgesetz,
    b) Ansprüche, die auf einer vorsätzlichen oder grob
       fahrlässigen Pflichtverletzung oder auf einer
       vorsätzlichen unerlaubten Handlung beruhen,
    c) Ansprüche wegen der Verletzung des Lebens, des Körpers
       oder der Gesundheit,
    d) Ansprüche, die kraft Gesetzes oder Tarifvertrags
       unabdingbar sind.
```

### 4. Widerrufs- und Freiwilligkeitsvorbehalt

Beide Instrumente werden regelmäßig verwechselt, obwohl sie Gegensätzliches leisten:

| Instrument | Zweck | Anforderungen |
|---|---|---|
| **Freiwilligkeitsvorbehalt** | Verhindert, dass durch wiederholte Leistung eine **betriebliche Übung** entsteht — es soll gar kein Anspruch entstehen | Nur bei echten Sonderzahlungen ohne Entgeltcharakter; darf nicht mit einer verbindlichen Zusage im selben Vertrag kombiniert werden (Widerspruch → intransparent) |
| **Widerrufsvorbehalt** | Ein bestehender Anspruch soll später einseitig entzogen werden können | Widerrufsgründe müssen **im Vertrag konkret benannt** sein (wirtschaftliche Gründe, Leistung, Verhalten); der widerrufliche Teil darf **nicht mehr als etwa 25 – 30 %** der Gesamtvergütung ausmachen und nicht in den Tariflohn eingreifen `[unverifiziert – prüfen]` |

Ein Vorbehalt, der **beides** kombiniert („freiwillig und jederzeit widerruflich"), ist widersprüchlich und nach § 307 Abs. 1 S. 2 BGB unwirksam — mit der Folge, dass die Leistung unbedingt geschuldet ist.

**Weitere Standardklauseln und ihre Fallhöhe:**

- **Versetzungsklausel:** Zulässig, soweit sie das Direktionsrecht des § 106 GewO nicht überschreitet; eine Klausel, die eine Zuweisung geringerwertiger Tätigkeiten erlaubt, ist unwirksam.
- **Überstundenabgeltungsklausel:** „Mit dem Gehalt sind alle Überstunden abgegolten" ist intransparent und unwirksam. Zulässig ist eine Abgeltung bis zu einer konkret bezifferten Stundenzahl; bei sehr hohen Vergütungen (oberhalb der Beitragsbemessungsgrenze) kann eine pauschale Abgeltung wirksam sein `[unverifiziert – prüfen]`.
- **Vertragsstrafe:** Erforderlich sind konkrete Tatbestände (etwa Nichtantritt, vertragswidrige Beendigung) und eine der Höhe nach angemessene Sanktion — Obergrenze regelmäßig ein Bruttomonatsgehalt, bei Nichtantritt in der Probezeit das der verkürzten Kündigungsfrist entsprechende Entgelt `[unverifiziert – prüfen]`.
- **Rückzahlungsklausel für Fortbildungskosten:** Bindungsdauer muss zur Fortbildungsdauer und zum geldwerten Vorteil in Verhältnis stehen; die Rückzahlungspflicht darf nicht an Beendigungsgründe aus der Sphäre des Arbeitgebers anknüpfen.
- **Nachvertragliches Wettbewerbsverbot:** §§ 74 ff. HGB — ohne Karenzentschädigung von mindestens der Hälfte der zuletzt bezogenen Bezüge ist es nichtig, nicht bloß unverbindlich, wenn die Entschädigung ganz fehlt.
- **Schriftformklausel:** Doppelte Schriftformklauseln sind gegenüber Individualabreden wirkungslos (§ 305b BGB) und in AGB unwirksam, soweit sie den Eindruck erwecken, mündliche Abreden seien stets unbeachtlich.

### 5. Nachweispflichten ([§ 2 NachwG](https://www.gesetze-im-internet.de/nachwg/__2.html))

Seit der Umsetzung der Richtlinie (EU) 2019/1152 zum **01.08.2022** ist der Katalog der nachzuweisenden wesentlichen Vertragsbedingungen auf **15 Punkte** erweitert (§ 2 Abs. 1 S. 7 Nr. 1–15 NachwG) und gestaffelt zu erfüllen (§ 2 Abs. 1 S. 9 NachwG):

| Frist | Angaben |
|---|---|
| **Spätestens am ersten Tag der Arbeitsleistung** | Nr. 1 (Parteien), Nr. 7 (Zusammensetzung und Höhe des Arbeitsentgelts einschließlich Überstundenvergütung, Zuschlägen, Zulagen, Prämien und Sonderzahlungen, jeweils getrennt, Fälligkeit und Auszahlungsart), Nr. 8 (Arbeitszeit, Ruhepausen, Ruhezeiten, Schichtsystem) |
| **Spätestens am siebten Kalendertag** | Nr. 2–6 (Beginn, Befristungsende, Arbeitsort, Tätigkeitsbeschreibung, Probezeit), Nr. 9 (Arbeit auf Abruf), Nr. 10 (Überstundenanordnung) |
| **Spätestens einen Monat nach Beginn** | Nr. 11 (Urlaubsdauer), Nr. 12 (Fortbildungsanspruch), Nr. 13 (betriebliche Altersversorgung / Versorgungsträger), Nr. 14 (Kündigungsverfahren, mindestens Schriftformerfordernis, Kündigungsfristen **und die Frist zur Erhebung der Kündigungsschutzklage**), Nr. 15 (anwendbare Tarifverträge und Betriebsvereinbarungen) |

**Form — die zentrale Unterscheidung:**

- § 2 Abs. 1 S. 1 NachwG verlangt im Ausgangspunkt weiterhin die **Schriftform**: niederlegen, unterzeichnen, aushändigen.
- Seit dem Vierten Bürokratieentlastungsgesetz (BEG IV) lässt § 2 Abs. 1 S. 2 NachwG die **Textform** ([§ 126b BGB](https://www.gesetze-im-internet.de/bgb/__126b.html)) und die elektronische Übermittlung zu — **unter drei kumulativen Bedingungen**: das Dokument muss für den Arbeitnehmer zugänglich sein, gespeichert und ausgedruckt werden können, und der Arbeitgeber muss mit der Übermittlung zur Erteilung eines **Empfangsnachweises** auffordern.
- Auf Verlangen des Arbeitnehmers ist die Niederschrift unverzüglich in Schriftform nachzureichen (§ 2 Abs. 1 S. 3 NachwG).
- **Die Textform-Öffnung gilt nicht** für Arbeitnehmer in den Wirtschaftsbereichen des § 2a Abs. 1 SchwarzArbG (§ 2 Abs. 1 S. 6 NachwG) — Bau, Gaststätten, Speditions- und Logistikgewerbe, Fleischwirtschaft u. a.
- Der Nachweis in **elektronischer Form** im Sinne des § 126a BGB bleibt ausgeschlossen (§ 2 Abs. 1 S. 8 NachwG).

**Abgrenzung, die man nicht verwechseln darf:** Die Textform-Öffnung betrifft **ausschließlich den Nachweis**. Unberührt bleiben:

- **[§ 623 BGB](https://www.gesetze-im-internet.de/bgb/__623.html) — Kündigung und Aufhebungsvertrag** bedürfen weiterhin der **Schriftform**; die elektronische Form ist ausdrücklich ausgeschlossen. Eine per E-Mail oder Messenger erklärte Kündigung ist nichtig.
- **§ 14 Abs. 4 TzBfG** — Befristungsabrede: Schriftform.
- **§ 74 Abs. 1 HGB** — nachvertragliches Wettbewerbsverbot: Schriftform und Aushändigung.

**Bußgeld:** Der Verstoß gegen die Nachweispflicht ist seit dem 01.08.2022 eine Ordnungswidrigkeit nach [§ 4 NachwG](https://www.gesetze-im-internet.de/nachwg/__4.html) und kann mit einer Geldbuße **bis zu zweitausend Euro** geahndet werden — je Verstoß, also potenziell je Arbeitnehmer.

Der Nachweis entfällt, soweit ein **schriftlicher Arbeitsvertrag** ausgehändigt wurde, der die Angaben enthält (§ 2 Abs. 5 NachwG). Der praktisch sicherste Weg bleibt daher ein vollständiger, unterschriebener Arbeitsvertrag.

## Quellen

### Statute

- [§ 305 BGB](https://www.gesetze-im-internet.de/bgb/__305.html), [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html), [§ 308 BGB](https://www.gesetze-im-internet.de/bgb/__308.html), [§ 309 BGB](https://www.gesetze-im-internet.de/bgb/__309.html), [§ 310 BGB](https://www.gesetze-im-internet.de/bgb/__310.html)
- [§ 126b BGB](https://www.gesetze-im-internet.de/bgb/__126b.html), [§ 202 BGB](https://www.gesetze-im-internet.de/bgb/__202.html), [§ 611a BGB](https://www.gesetze-im-internet.de/bgb/__611a.html), [§ 623 BGB](https://www.gesetze-im-internet.de/bgb/__623.html)
- [§ 2 NachwG](https://www.gesetze-im-internet.de/nachwg/__2.html), [§ 4 NachwG](https://www.gesetze-im-internet.de/nachwg/__4.html)
- [§ 3 MiLoG](https://www.gesetze-im-internet.de/milog/__3.html), [§ 1 MiLoG](https://www.gesetze-im-internet.de/milog/__1.html)
- [§ 106 GewO](https://www.gesetze-im-internet.de/gewo/__106.html), [§ 14 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__14.html)
- Richtlinie (EU) 2019/1152 über transparente und vorhersehbare Arbeitsbedingungen

### Kommentare

- Preis, in: ErfK, 24. Aufl. 2024, §§ 305–310 BGB Rn. 1 ff. (AGB-Kontrolle im Arbeitsrecht)
- Preis, Der Arbeitsvertrag, 7. Aufl. 2022, II A 10 (Ausschlussfristen), II W 10 (Widerrufsvorbehalt)
- Basedow, in: MüKoBGB, 9. Aufl. 2022, § 310 Rn. 100 ff.
- Kliemt, in: HWK, 11. Aufl. 2024, § 2 NachwG Rn. 1 ff.

### Rechtsprechung

- st. Rspr. des BAG zu § 307 BGB (Ausschlussfrist unter drei Monaten je Stufe benachteiligt unangemessen) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zu § 3 MiLoG i.V.m. § 307 Abs. 1 S. 2 BGB (Ausschlussfrist ohne Mindestlohnausnahme ist intransparent und insgesamt unwirksam) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zum Widerrufsvorbehalt (Widerrufsgründe im Vertrag zu benennen; Widerrufsvolumen begrenzt) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zur pauschalen Überstundenabgeltungsklausel (Intransparenz bei unbezifferter Abgeltung) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zur Vertragsstrafe im Arbeitsvertrag (§ 309 Nr. 6 BGB nicht anwendbar, aber Angemessenheitskontrolle nach § 307 BGB) `[unverifiziert – prüfen]`

> Aktenzeichen sind vor Verwendung in juris, Beck-Online oder der [BAG-Entscheidungsdatenbank](https://www.bundesarbeitsgericht.de/entscheidungen/) zu ermitteln.

## Ausgabeformat

```
ARBEITSVERTRAG — GESTALTUNG / KLAUSELPRÜFUNG — <Mandat-ID> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

Gesamtbefund: [🟢 tragfähig / 🟡 Anpassung empfohlen / 🔴 Klausel unwirksam]

I.    AGB-Eröffnung                       [Muster / Einmalbedingung
                                           § 310 III Nr. 2 BGB]
II.   Klauselprüfung
      Klausel | § | Befund | Rechtsfolge bei Unwirksamkeit
      Ausschlussfrist        | 307 I | [🟢/🔴] | ersatzlos, §§ 195 ff. BGB
      Widerrufsvorbehalt     | 307 I | [🟢/🔴] | Leistung unbedingt geschuldet
      Freiwilligkeitsvorbehalt| 307 I | [🟢/🔴] | betriebliche Übung entsteht
      Versetzungsklausel     | 307   | [🟢/🔴] | § 106 GewO gilt
      Überstundenabgeltung   | 307 I 2| [🟢/🔴] | Vergütungspflicht § 612 BGB
      Vertragsstrafe         | 307   | [🟢/🔴] | ersatzlos
      Fortbildungsrückzahlung| 307   | [🟢/🔴] | ersatzlos
      Wettbewerbsverbot      | 74 HGB| [🟢/🔴] | nichtig / unverbindlich
III.  Transparenzprüfung § 307 I 2 BGB    <auffällige Formulierungen>
IV.   Blue-Pencil-Test                    <abtrennbare Teile>
V.    Nachweispflichten § 2 NachwG
      Tag 1 (Nr. 1, 7, 8):                [🟢 / 🔴]
      Tag 7 (Nr. 2–6, 9, 10):             [🟢 / 🔴]
      Monat 1 (Nr. 11–15):                [🟢 / 🔴]
      Form:                               [Schriftform / Textform § 2 I 2
                                           mit Empfangsnachweis]
      SchwarzArbG-Branche § 2a I:         [nein / 🔴 ja → nur Schriftform]
      Bußgeldrisiko § 4 NachwG:           bis 2.000 EUR je Verstoß
VI.   Formerfordernisse unberührt          § 623 BGB (Kündigung),
                                           § 14 IV TzBfG, § 74 I HGB

Empfohlene Neufassungen:
  <Klausel + Wortlaut>
Empfehlung: <…>
```

## Risiken / typische Fehler

- **Ausschlussfrist ohne Mindestlohnausnahme** — die Klausel fällt insgesamt weg, nicht nur bezogen auf den Mindestlohn; alle Ansprüche unterliegen dann der Regelverjährung.
- **Ausschlussfrist verlangt Schriftform** — Verstoß gegen § 309 Nr. 13 BGB; zulässig ist höchstens Textform.
- **Geltungserhaltende Reduktion erwartet** — eine „bis zu drei Bruttomonatsgehälter"-Vertragsstrafe wird nicht auf ein Gehalt gekürzt, sondern fällt weg.
- **Salvatorische Klausel als Sicherheitsnetz** eingesetzt — im AGB-Recht wirkungslos.
- **Freiwilligkeits- und Widerrufsvorbehalt kombiniert** — widersprüchlich, intransparent, Leistung unbedingt geschuldet.
- **Widerrufsvorbehalt ohne benannte Widerrufsgründe** oder mit einem Volumen weit über einem Viertel der Gesamtvergütung.
- **Pauschale Überstundenabgeltung** ohne Bezifferung — intransparent; die Überstunden sind dann nach § 612 BGB zu vergüten.
- **Textform des § 2 NachwG mit der Kündigungsform verwechselt** — § 623 BGB verlangt unverändert Schriftform; eine per E-Mail erklärte Kündigung ist nichtig.
- **Textform in einer SchwarzArbG-Branche verwendet** — § 2 Abs. 1 S. 6 NachwG nimmt diese Bereiche von der Öffnung aus.
- **Empfangsnachweis nicht angefordert** — ohne die Aufforderung ist die Textform-Variante des § 2 Abs. 1 S. 2 NachwG nicht erfüllt.
- **Nachweisfristen gestaffelt übersehen** — Entgelt und Arbeitszeit sind bereits **am ersten Tag** nachzuweisen, nicht binnen eines Monats.
- **Hinweis auf die Klagefrist des § 4 KSchG vergessen** (§ 2 Abs. 1 S. 7 Nr. 14 NachwG) — die Nachweispflicht besteht, ändert aber nichts an der Präklusion nach § 7 KSchG.
