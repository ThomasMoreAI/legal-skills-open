---
name: grundrechtspruefung-borghei
title: /verfassungsrecht:grundrechtspruefung
description: 3-Stufen-Grundrechtsprüfung nach Schutzbereich, Eingriff und verfassungsrechtlicher Rechtfertigung inkl. Verhältnismäßigkeit und neuer Formel zu Art. 3 GG. Use when ein Hoheitsakt am Maßstab eines Freiheits- oder Gleichheitsrechts (Art. 1–19 GG) zu prüfen ist – ob als Vorstufe einer Verfassungsbeschwerde, im verwaltungsrechtlichen Klageverfahren oder in einem Gutachten zur Gesetzesfolgenabschätzung.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verfassungsrecht/skills/grundrechtspruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: constitutional
language: de
---

# /verfassungsrecht:grundrechtspruefung

## Zweck

Die Grundrechtsprüfung folgt dem **3-Stufen-Schema**: Schutzbereich → Eingriff → Verfassungsrechtliche Rechtfertigung. Bei Gleichheitsrechten greift die **neue Formel** zu Art. 3 Abs. 1 GG. Dieser Skill stellt sicher, dass die einzelnen Stufen, ihre Spezialfälle (Drittwirkung, Schutzpflicht, Leistungsrechte) und die Schranken-Schranken (insbesondere Verhältnismäßigkeit) vollständig durchlaufen werden.

## Eingaben

- gerügter Hoheitsakt (Gesetz, Verwaltungsakt, Urteil oder schlichtes Verwaltungshandeln)
- benanntes Grundrecht (Art. 1–19 GG) oder grundrechtsgleiches Recht
- betroffene Person(en); juristische Person? Ausländer?
- Schrankentyp (qualifizierter Gesetzesvorbehalt, einfacher Gesetzesvorbehalt, verfassungsimmanente Schranken)

## Sub-Agent-Architektur

Researcher liefert Statute, Standardkommentare und einschlägige BVerfG-Leitentscheidungen zum Grundrecht. Drafter führt das 3-Stufen-Schema im Gutachtenstil durch. Reviewer prüft Vollständigkeit der Stufen, Verhältnismäßigkeit und die neue Formel bei Art. 3 GG.

## Ablauf

### 1. Schutzbereich

| Dimension | Inhalt |
|---|---|
| **Persönlich** | Jedermannsgrundrecht oder Deutschengrundrecht (Art. 8, 9, 11, 12, 16 GG nur Deutsche)? Juristische Person (Art. 19 Abs. 3 GG)? |
| **Sachlich** | Welche Verhaltensweisen / Zustände sind erfasst? |

Bei Freiheitsrechten: weit auszulegen, im Zweifel **in dubio pro libertate**. Bei der Auslegung des Schutzbereichs sind die vier klassischen Methoden anzuwenden.

### 2. Eingriff

Klassischer Eingriffsbegriff (final, unmittelbar, rechtsförmig, mit Befehl und Zwang) **vs.** moderner Eingriffsbegriff (jede dem Staat zurechenbare Beeinträchtigung des grundrechtlichen Schutzguts). Heutige h.M. folgt dem modernen Begriff — vgl. Sachs, in: Sachs GG, vor Art. 1 Rn. 78 ff.

Sonderkonstellationen:

- **Mittelbare Drittwirkung** (BVerfG, Urt. v. 15.01.1958 – 1 BvR 400/51, BVerfGE 7, 198 – „Lüth", [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1958-01-15&Aktenzeichen=1%20BvR%20400/51)): Grundrechte als objektive Wertordnung wirken durch zivilrechtliche Generalklauseln (§§ 138, 242 BGB).
- **Schutzpflichten**: Grundrechte als Schutzauftrag ([BVerfGE 39, 1](https://www.servat.unibe.ch/dfr/bv039001.html)); Untermaßverbot.
- **Leistungsrechte**: nur ausnahmsweise originäre Teilhabeansprüche (Existenzminimum, BVerfG, Urt. v. 09.02.2010 – 1 BvL 1/09 u.a., BVerfGE 125, 175, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2010-02-09&Aktenzeichen=1%20BvL%201/09)).

### 3. Verfassungsrechtliche Rechtfertigung

#### 3.1 Schranke

- **Einfacher Gesetzesvorbehalt** (z. B. Art. 8 Abs. 2, Art. 12 Abs. 1 S. 2 GG)
- **Qualifizierter Gesetzesvorbehalt** (z. B. Art. 11 Abs. 2 GG)
- **Verfassungsimmanente Schranken** (vorbehaltlos gewährleistete Grundrechte wie Art. 4 GG, Art. 5 Abs. 3 GG, Art. 8 Abs. 1 GG für Versammlungen unter freiem Himmel — Achtung Sonderfall Abs. 2)

#### 3.2 Schranken-Schranken

- **Zitiergebot** Art. 19 Abs. 1 S. 2 GG
- **Einzelfallgesetz-Verbot** Art. 19 Abs. 1 S. 1 GG
- **Wesensgehaltsgarantie** Art. 19 Abs. 2 GG
- **Verhältnismäßigkeit** (siehe 3.3)
- bei Art. 5 GG: **Wechselwirkungslehre** (BVerfGE 7, 198 — „Lüth", [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1958-01-15&Aktenzeichen=1%20BvR%20400/51))

#### 3.3 Verhältnismäßigkeit

| Stufe | Maßstab |
|---|---|
| **Legitimer Zweck** | Mit der Verfassung vereinbares öffentliches Interesse |
| **Geeignetheit** | Maßnahme fördert den Zweck (Einschätzungsprärogative des Gesetzgebers) |
| **Erforderlichkeit** | Kein gleich wirksames, milderes Mittel verfügbar |
| **Angemessenheit (i.e.S.)** | Abwägung Schwere des Eingriffs ↔ Gewicht des Zwecks |

Bei Art. 12 GG: **Drei-Stufen-Theorie** (BVerfG, Urt. v. 11.06.1958 – 1 BvR 596/56, BVerfGE 7, 377 — „Apotheken-Urteil", [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1958-06-11&Aktenzeichen=1%20BvR%20596/56)) — Berufsausübungs-, subjektive Berufswahl-, objektive Berufswahlregelung.

### 4. Gleichheitsrechte (Art. 3 GG) — neue Formel

| Test | Maßstab |
|---|---|
| **Ungleichbehandlung von wesentlich Gleichem (oder umgekehrt)** | tatsächlich vergleichbare Sachverhalte |
| **Rechtfertigung** | Je nach Differenzierungsgrund: vom bloßen Willkürverbot bis zur strengen Verhältnismäßigkeit (insbes. personenbezogene Differenzierung) — BVerfG, Beschl. v. 07.10.1980 – 1 BvL 50/79 u.a., BVerfGE 55, 72 (neue Formel), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1980-10-07&Aktenzeichen=1%20BvL%2050/79) |

Spezielle Gleichheitssätze: Art. 3 Abs. 2, 3, Art. 6 Abs. 5, Art. 33 Abs. 1–3, Art. 38 Abs. 1, Art. 6 Abs. 1 GG.

### 5. Praxisrelevante Tipps

- Bei vorbehaltlosen Grundrechten zunächst prüfen, ob nicht **schon der Schutzbereich** durch eine engere Definition den Konflikt löst (Bsp. künstlerische Werbung – Art. 5 Abs. 3 GG).
- Bei doppelter Grundrechtsbetroffenheit: **Spezialitätsverhältnis** prüfen (z. B. Art. 14 GG vor Art. 12 GG bei Vermögenseingriffen).
- § 31 BVerfGG ist die einzige zulässige Stelle, an der mit Bindung an BVerfG-Rspr. argumentiert werden darf.

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [Art. 1 GG](https://www.gesetze-im-internet.de/gg/art_1.html) (Menschenwürde)
- [Art. 2 GG](https://www.gesetze-im-internet.de/gg/art_2.html) (allgemeine Handlungsfreiheit, Leben/körperliche Unversehrtheit)
- [Art. 3 GG](https://www.gesetze-im-internet.de/gg/art_3.html) (Gleichheit)
- [Art. 5 GG](https://www.gesetze-im-internet.de/gg/art_5.html) (Meinungs-/Pressefreiheit, Kunst und Wissenschaft)
- [Art. 12 GG](https://www.gesetze-im-internet.de/gg/art_12.html) (Berufsfreiheit)
- [Art. 14 GG](https://www.gesetze-im-internet.de/gg/art_14.html) (Eigentum)
- [Art. 19 GG](https://www.gesetze-im-internet.de/gg/art_19.html) (Zitiergebot, Wesensgehaltsgarantie, juristische Person)
- [Art. 20 GG](https://www.gesetze-im-internet.de/gg/art_20.html) (Verhältnismäßigkeit als Ausfluss Rechtsstaatsprinzip)

### Kommentare

- Herdegen, in: Maunz/Dürig GG, Loseblatt (Stand: aktuelle Lieferung), Art. 1 Abs. 1 Rn. 1 ff.
- Murswiek/Rixen, in: Sachs GG, 9. Aufl. 2021, Art. 2 Rn. 1 ff.
- Jarass, in: Jarass/Pieroth GG, 18. Aufl. 2024, Art. 3 Rn. 1 ff. (neue Formel)
- Scholz, in: Maunz/Dürig GG, Art. 12 Rn. 1 ff. (Drei-Stufen-Theorie)
- Schlaich/Korioth, Das Bundesverfassungsgericht, 12. Aufl. 2021, Rn. 442 ff. (Grundrechtsprüfung)

### Rechtsprechung

1. BVerfG, Urt. v. 15.01.1958 – 1 BvR 400/51, BVerfGE 7, 198 („Lüth"; Grundrechte als objektive Wertordnung, Ausstrahlung auf § 826 BGB), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1958-01-15&Aktenzeichen=1%20BvR%20400/51)
2. BVerfG, Urt. v. 11.06.1958 – 1 BvR 596/56, BVerfGE 7, 377 („Apotheken-Urteil", Drei-Stufen-Theorie zu Art. 12 GG), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1958-06-11&Aktenzeichen=1%20BvR%20596/56)
3. BVerfG, Urt. v. 16.01.1957 – 1 BvR 253/56, BVerfGE 6, 32 („Elfes"; Ausreiseverbot, weites Verständnis der verfassungsmäßigen Ordnung, Art. 2 I GG), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1957-01-16&Aktenzeichen=1%20BvR%20253/56)
4. BVerfG, Urt. v. 15.12.1983 – 1 BvR 209/83 u.a., BVerfGE 65, 1 („Volkszählung", informationelle Selbstbestimmung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1983-12-15&Aktenzeichen=1%20BvR%20209/83)
5. BVerfG, Beschl. v. 07.10.1980 – 1 BvL 50/79 u.a., BVerfGE 55, 72 (neue Formel zu Art. 3 GG; Verfahrensgegenstand ist die zivilprozessuale Präklusion nach § 528 III ZPO a.F.), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1980-10-07&Aktenzeichen=1%20BvL%2050/79)
6. BVerfG, Beschl. v. 16.05.1995 – 1 BvR 1087/91, BVerfGE 93, 1 („Kruzifix"; Art. 4 I, 6 II, 7 I GG, praktische Konkordanz), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1995-05-16&Aktenzeichen=1%20BvR%201087/91)
7. BVerfG, Urt. v. 09.02.2010 – 1 BvL 1/09 u.a., BVerfGE 125, 175 („Hartz IV-Regelleistungen"; menschenwürdiges Existenzminimum, Art. 1 I iVm Art. 20 I GG), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2010-02-09&Aktenzeichen=1%20BvL%201/09)

## Ausgabeformat

```
GUTACHTEN GRUNDRECHTSPRÜFUNG
<Datum> — <Skill-Mandat-ID>

A. Sachverhalt
   <knapp>

B. Frage
   Verletzt <Hoheitsakt> den/die Betroffenen in Art. … GG?

C. Kurzantwort
   <1 Satz>

D. Prüfung

   I.   Schutzbereich
        1. Persönlich (Jedermannsgrundrecht / Deutschengrundrecht /
           juristische Person Art. 19 III GG)
        2. Sachlich

   II.  Eingriff
        (klassisch / modern; ggf. mittelbare Drittwirkung,
        Schutzpflicht, Leistungsrecht)

   III. Verfassungsrechtliche Rechtfertigung
        1. Schranke
           (einfacher / qualifizierter Gesetzesvorbehalt /
           verfassungsimmanent)
        2. Schranken-Schranken
           a) Zitiergebot Art. 19 I 2 GG
           b) Wesensgehaltsgarantie Art. 19 II GG
           c) Verhältnismäßigkeit
              aa) Legitimer Zweck
              bb) Geeignetheit
              cc) Erforderlichkeit
              dd) Angemessenheit
           d) ggf. Wechselwirkungslehre / Drei-Stufen-Theorie

E. Bei Art. 3 GG
   I.   Ungleichbehandlung wesentlich Gleicher
   II.  Rechtfertigung (Willkürverbot ↔ Verhältnismäßigkeit nach
        Differenzierungsgrund — „neue Formel")

F. Ergebnis
   Grundrechtsverletzung ✅/❌

G. Risiken / offene Punkte

H. Quellenverzeichnis
```

## Beispiel (Auszug, Gutachtenstil)

> **B. Frage** Verletzt § X LandesHeilprG den Beschwerdeführer in seiner Berufsfreiheit aus Art. 12 Abs. 1 GG? **D.I.** Der Schutzbereich des Art. 12 Abs. 1 GG erfasst jede auf Dauer angelegte und erlaubte Tätigkeit zum Zweck der Schaffung und Erhaltung einer Lebensgrundlage; der Beschwerdeführer übt eine solche Tätigkeit als Heilpraktiker aus. **D.II.** In dieser Tätigkeit ist er durch den Erlaubnisvorbehalt unmittelbar und final betroffen — Eingriff bejaht. **D.III.1.** Schranke ist Art. 12 Abs. 1 S. 2 GG. **D.III.2.c)** Verhältnismäßigkeit ist nach der Drei-Stufen-Theorie zu prüfen (BVerfGE 7, 377, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1958-06-11&Aktenzeichen=1%20BvR%20596/56)): Es handelt sich um eine subjektive Berufswahlregelung; legitimer Zweck ist der Patientenschutz; geeignet; erforderlich, da ein milderes Mittel (Anzeigepflicht) den Zweck nicht gleich wirksam erreicht; angemessen, soweit die Erlaubnisvoraussetzungen die Tätigkeit nicht überproportional erschweren.

## Risiken / typische Fehler

- **Schutzbereich zu schmal definiert** — führt dazu, dass die spätere Verhältnismäßigkeitsprüfung umgangen wird.
- **Eingriff bejaht ohne Zurechnung** — bei privatem Handeln zunächst Drittwirkung prüfen.
- **Verhältnismäßigkeit unvollständig** — Erforderlichkeit und Angemessenheit werden häufig zusammengezogen.
- **Art. 3 GG mit bloßem Willkürtest** statt neuer Formel, obwohl personenbezogenes Differenzierungskriterium vorliegt.
- **Wechselwirkungslehre vergessen** bei Art. 5 Abs. 1 GG i.V.m. allgemeinem Gesetz.
- **§ 31 BVerfGG fehlinterpretiert** — Bindungswirkung umfasst nur tragende Gründe, nicht obiter dicta.
