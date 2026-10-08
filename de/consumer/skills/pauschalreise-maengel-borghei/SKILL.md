---
name: pauschalreise-maengel-borghei
title: /reise-fluggastrecht:pauschalreise-maengel
description: Mängelrechte des Reisenden bei einer Pauschalreise – Pauschalreisevertrag § 651a BGB, Reisemangel § 651i BGB, Abhilfe § 651k BGB, Minderung § 651m BGB, Kündigung § 651l BGB, Schadensersatz § 651n BGB einschließlich entgangener Urlaubsfreude nach § 651n Abs. 2 BGB, Abhilfeverlangen und Anzeigeobliegenheit § 651o BGB, Frankfurter Tabelle als bloße Orientierung, Verjährung § 651j BGB. Use when ein Reisender während oder nach einer Pauschalreise Mängel geltend macht und Minderung, Kündigung und Schadensersatz gegen den Reiseveranstalter beziffert werden sollen.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/reise-fluggastrecht/skills/pauschalreise-maengel
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /reise-fluggastrecht:pauschalreise-maengel

## Zweck

Der Skill prüft die Mängelrechte des Reisenden nach Reiseantritt und beziffert sie. Er erzwingt die beiden Obliegenheiten, an denen die meisten Ansprüche scheitern — **Mängelanzeige** und **Abhilfeverlangen** — und trennt sauber zwischen der gesetzlichen Rechtsfolge (§ 651m BGB) und den in der Praxis herangezogenen Tabellenwerten, die keinerlei Bindungswirkung haben.

## Eingaben

- Reiseveranstalter, Buchungsnummer, Reisezeitraum, Gesamtreisepreis
- Leistungsbeschreibung aus Katalog, Buchungsbestätigung und vorvertraglicher Information
- Mängelbeschreibung je Position mit Beginn, Ende und Beweismitteln (Fotos, Zeugen, Mängelprotokoll)
- Zeitpunkt und Form der Mängelanzeige, Adressat (Reiseleitung, Notrufnummer, Veranstalter)
- Reaktion des Veranstalters, angebotene Abhilfe, Ersatzleistungen
- Etwaige Kündigung mit Datum und Rückreisekosten
- Nutzlose Aufwendungen und immaterielle Beeinträchtigung
- Vertraglich vereinbartes Reiseende (für die Verjährung)

## Sub-Agent-Architektur

Ein Researcher ordnet den Vertrag als Pauschalreisevertrag ein, bestimmt den Veranstalter und sammelt Normen, EuGH- und BGH-Rechtsprechung sowie Kommentarstellen. Ein Drafter subsumiert jede Mangelposition unter § 651i Abs. 2 BGB, prüft Anzeige und Abhilfeverlangen, berechnet die Minderung tageweise und entwirft Mängelanzeige und Forderungsschreiben. Ein Reviewer kontrolliert die Verjährung nach § 651j BGB, die Kennzeichnung von Tabellenwerten als bloße Orientierung sowie jede Fundstelle und markiert Unbestätigtes mit `[unverifiziert - prüfen]`.

## Ablauf

### 1. Pauschalreisevertrag und Anspruchsgegner ([§ 651a BGB](https://www.gesetze-im-internet.de/bgb/__651a.html))

Ein Pauschalreisevertrag liegt vor, wenn der Unternehmer dem Reisenden eine **Gesamtheit von mindestens zwei verschiedenen Arten von Reiseleistungen** für den Zweck derselben Reise verschafft (§ 651a Abs. 1, 2 BGB). Anspruchsgegner ist der **Reiseveranstalter**, nicht der Leistungsträger (Hotel, Airline) und nicht das vermittelnde Reisebüro.

Abzugrenzen sind:

- **verbundene Reiseleistungen** ([§ 651w BGB](https://www.gesetze-im-internet.de/bgb/__651w.html)) — kein Reisevertragsrecht, nur Insolvenzschutz und Information;
- **bloße Vermittlung** ([§ 651v BGB](https://www.gesetze-im-internet.de/bgb/__651v.html)) — Haftung nur für eigenes Vermittlerverschulden.

Vertiefung: `/reise-fluggastrecht:reisevermittlung-informationspflichten`.

### 2. Reisemangel feststellen ([§ 651i BGB](https://www.gesetze-im-internet.de/bgb/__651i.html))

Der Veranstalter schuldet die **Verschaffung einer mangelfreien Pauschalreise** (§ 651i Abs. 1 BGB). Ein Mangel liegt vor, wenn die Reise nicht die vereinbarte Beschaffenheit hat oder sich nicht für den vertraglich vorausgesetzten bzw. den gewöhnlichen Nutzen eignet (§ 651i Abs. 2 BGB).

Maßstab ist der **Vertragsinhalt**: Katalogangaben, Buchungsbestätigung und die vorvertraglichen Informationen nach Art. 250 EGBGB werden Vertragsbestandteil. Nicht jede Unannehmlichkeit ist ein Mangel — landesübliche Verhältnisse, allgemeines Lebensrisiko und geringfügige Abweichungen bleiben außer Betracht.

Die Rechte des Reisenden zählt § 651i Abs. 3 BGB abschließend auf: Abhilfe, Selbstabhilfe, Beistand, Minderung, Kündigung, Schadensersatz und Ersatz vergeblicher Aufwendungen.

### 3. Anzeigeobliegenheit ([§ 651o BGB](https://www.gesetze-im-internet.de/bgb/__651o.html))

Der Reisende hat dem Veranstalter einen Mangel **unverzüglich anzuzeigen**. Unterlässt er die Anzeige schuldhaft, kann er nach § 651o Abs. 2 BGB Minderung und Schadensersatz nicht verlangen, soweit Abhilfe möglich gewesen wäre.

Praxis: Anzeige gegenüber der **Reiseleitung** oder unter der vom Veranstalter benannten Kontaktstelle, nicht gegenüber dem Hotelpersonal. Immer schriftlich oder in Textform nachziehen und den Zugang dokumentieren; das Mängelprotokoll der Reiseleitung ist gegenzuzeichnen und in Kopie zu verlangen.

### 4. Abhilfe und Selbstabhilfe ([§ 651k BGB](https://www.gesetze-im-internet.de/bgb/__651k.html))

Der Veranstalter hat Abhilfe zu schaffen (§ 651k Abs. 1 BGB); er kann sie verweigern, wenn sie unmöglich ist oder unter Berücksichtigung des Ausmaßes des Mangels und des Werts der betroffenen Reiseleistung unverhältnismäßige Kosten verursacht.

- **Selbstabhilfe** (§ 651k Abs. 2 BGB): Der Reisende kann selbst Abhilfe schaffen und Ersatz der erforderlichen Aufwendungen verlangen, wenn der Veranstalter eine **angemessene Frist** hat verstreichen lassen. Die Fristsetzung ist entbehrlich, wenn die Abhilfe verweigert wird oder sofortige Abhilfe erforderlich ist.
- **Erhebliche Vertragswidrigkeit** (§ 651k Abs. 3 BGB): Der Veranstalter hat angemessene Ersatzleistungen anzubieten; sind sie minderwertiger, ist die Minderung von sich aus zu gewähren.
- **Beistandspflicht** ([§ 651q BGB](https://www.gesetze-im-internet.de/bgb/__651q.html)) bei Schwierigkeiten des Reisenden.

### 5. Minderung ([§ 651m BGB](https://www.gesetze-im-internet.de/bgb/__651m.html))

Für die Dauer des Mangels mindert sich der Reisepreis **kraft Gesetzes** — ein Minderungsverlangen ist nicht erforderlich, wohl aber die Anzeige nach § 651o BGB. Der Reisepreis ist in dem Verhältnis herabzusetzen, in dem der Wert der mangelfreien zur mangelhaften Reise gestanden hätte; die Minderung ist gegebenenfalls durch Schätzung zu ermitteln (§ 651m Abs. 1 S. 2, 3 BGB). Zu viel Gezahltes ist zu erstatten (§ 651m Abs. 2 BGB).

**Die Frankfurter Tabelle ist kein Gesetz.** Sie ist eine 1985 vom LG Frankfurt am Main veröffentlichte Orientierungshilfe ohne Bindungswirkung; sie ist weder Rechtsnorm noch Verwaltungsvorschrift noch verbindliche Rechtsprechung. Sie darf als Verhandlungsanker und zur Plausibilisierung genannt, aber **niemals als Rechtsgrundlage der Minderung** ausgewiesen werden. Rechtsgrundlage ist allein § 651m BGB; entscheidend bleibt die Bewertung des Einzelfalls.

Berechnungsweg:

```
Tagesreisepreis   = Gesamtreisepreis / Anzahl der Reisetage
Minderung je Tag  = Tagesreisepreis × Quote der betroffenen Position
Minderungsbetrag  = Summe über alle Positionen und Tage
```

Mehrere Mängel werden **positionsweise** bewertet; eine schlichte Addition der Quoten über 100 % hinaus ist ausgeschlossen. Die Quoten sind zu begründen, nicht aus einer Tabelle abzuschreiben.

### 6. Kündigung ([§ 651l BGB](https://www.gesetze-im-internet.de/bgb/__651l.html))

Wird die Reise durch einen Mangel **erheblich beeinträchtigt**, kann der Reisende den Vertrag kündigen — grundsätzlich erst nach fruchtlosem Ablauf einer angemessenen Abhilfefrist (§ 651l Abs. 1 BGB). Folgen: Der Veranstalter verliert den Anspruch auf den Reisepreis, kann aber eine Entschädigung für erbrachte und noch zu erbringende Leistungen verlangen, soweit diese für den Reisenden von Interesse waren (§ 651l Abs. 2 BGB). Er hat die zur Vertragsaufhebung erforderlichen Maßnahmen zu treffen und den Reisenden zurückzubefördern (§ 651l Abs. 3 BGB); die Mehrkosten der Rückbeförderung trägt der Veranstalter.

### 7. Schadensersatz und entgangene Urlaubsfreude ([§ 651n BGB](https://www.gesetze-im-internet.de/bgb/__651n.html))

- **§ 651n Abs. 1 BGB**: Schadensersatz neben der Minderung, es sei denn, der Mangel ist vom Reisenden verschuldet, von einem Dritten verursacht, der weder Leistungserbringer noch sonst in die Leistungserbringung eingebunden war, oder durch unvermeidbare außergewöhnliche Umstände verursacht.
- **§ 651n Abs. 2 BGB — entgangene Urlaubsfreude**: Wird die Reise **vereitelt oder erheblich beeinträchtigt**, kann der Reisende auch wegen nutzlos aufgewendeter Urlaubszeit eine **angemessene Entschädigung in Geld** verlangen. Der Anspruch ist immateriell und setzt eine erhebliche Schwelle voraus; die Bemessung orientiert sich am Tagesreisepreis und an der Dauer und Intensität der Beeinträchtigung. Unionsrechtliche Grundlage ist die Anerkennung des immateriellen Schadens im Reiserecht (EuGH, Urt. v. 12.03.2002 – Rs. C-168/00 „Leitner", NJW 2002, 1255 = EuZW 2002, 339, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2002-03-12&Aktenzeichen=C-168/00); ergangen noch zur Pauschalreise-RL 90/314/EWG).
- **§ 651n Abs. 3 BGB** verweist für Haftungsbeschränkungen auf internationale Übereinkommen; [§ 651p BGB](https://www.gesetze-im-internet.de/bgb/__651p.html) erlaubt eine vertragliche Begrenzung auf den dreifachen Reisepreis nur für nicht körperliche Schäden und nur bei fehlendem Vorsatz und grober Fahrlässigkeit.

Vergebliche Aufwendungen (Visa, Impfungen, Ausrüstung, gebuchte Ausflüge) sind gesondert zu beziffern.

### 8. Verjährung ([§ 651j BGB](https://www.gesetze-im-internet.de/bgb/__651j.html))

Ansprüche des Reisenden nach § 651i Abs. 3 BGB verjähren in **zwei Jahren** ab dem Tag, an dem die Reise nach dem Vertrag **enden sollte**. Anknüpfungspunkt ist damit das vertraglich vereinbarte Reiseende — nicht die tatsächliche Rückkehr, nicht die Kenntnis und nicht der Schluss des Jahres. Verhandlungen hemmen nach [§ 203 BGB](https://www.gesetze-im-internet.de/bgb/__203.html).

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur die Arithmetik**. Das vertraglich vereinbarte Reiseende, die Hemmung durch Verhandlungen und die Bewertung der Mangelquoten bleiben juristische Eingaben.

```bash
# Verjährung § 651j BGB: vertragliches Reiseende 24.08.2024, zwei Jahre
python -m scripts.legal_calc.cli frist --ereignis 24.08.2024 --menge 2 --einheit jahre --land BY

# Kontrollrechnung Regelverjährung (nur für Ansprüche außerhalb § 651i Abs. 3 BGB)
python -m scripts.legal_calc.cli verjaehrung --entstehung 24.08.2024 --kenntnis 24.08.2024

# Abhilfefrist § 651k Abs. 2 BGB: angemessene Frist ab Anzeige
python -m scripts.legal_calc.cli frist --ereignis 12.08.2024 --menge 2 --einheit tage --land BY
```

`--json` liefert die Rechenschritte samt Normzitat. **Nicht** mit dem Rechner zu ermitteln sind Minderungsquoten und Werte der Frankfurter Tabelle — die Quotenbildung ist eine Wertung, keine Rechnung.

## Quellen

### Statute

- [§ 651a BGB](https://www.gesetze-im-internet.de/bgb/__651a.html), [§ 651i BGB](https://www.gesetze-im-internet.de/bgb/__651i.html), [§ 651j BGB](https://www.gesetze-im-internet.de/bgb/__651j.html), [§ 651k BGB](https://www.gesetze-im-internet.de/bgb/__651k.html), [§ 651l BGB](https://www.gesetze-im-internet.de/bgb/__651l.html), [§ 651m BGB](https://www.gesetze-im-internet.de/bgb/__651m.html), [§ 651n BGB](https://www.gesetze-im-internet.de/bgb/__651n.html), [§ 651o BGB](https://www.gesetze-im-internet.de/bgb/__651o.html), [§ 651p BGB](https://www.gesetze-im-internet.de/bgb/__651p.html), [§ 651q BGB](https://www.gesetze-im-internet.de/bgb/__651q.html), [§ 651v BGB](https://www.gesetze-im-internet.de/bgb/__651v.html), [§ 651w BGB](https://www.gesetze-im-internet.de/bgb/__651w.html), [§ 651y BGB](https://www.gesetze-im-internet.de/bgb/__651y.html)
- [§ 203 BGB](https://www.gesetze-im-internet.de/bgb/__203.html), [§ 286 BGB](https://www.gesetze-im-internet.de/bgb/__286.html)
- [Art. 250 § 1 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_250__1.html), [Art. 250 § 3 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_250__3.html)
- [Richtlinie (EU) 2015/2302](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32015L2302)

### Kommentare

- Tonner, in: MüKo-BGB, § 651i Rn. 1 ff., § 651m Rn. 1 ff., § 651n Rn. 1 ff.
- Führich, Reiserecht, Kap. Reisemängel und Minderung.
- Steinrötter, in: BeckOGK BGB, § 651i Rn. 1 ff.
- Geib, in: BeckOK BGB, § 651n Rn. 1 ff.

### Rechtsprechung

1. EuGH, Urt. v. 12.03.2002 – Rs. C-168/00, Leitner, NJW 2002, 1255 = EuZW 2002, 339 (immaterieller Schaden im Reiserecht; RL 90/314/EWG), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2002-03-12&Aktenzeichen=C-168/00)
2. EuGH, Urt. v. 08.06.2023 – Rs. C-407/21, UFC-Que choisir und CLCV, EuZW 2023, 709 = MDR 2023, 964 (Rücktritt wegen unvermeidbarer außergewöhnlicher Umstände in der COVID-19-Pandemie; Erstattungspflicht des Veranstalters nach RL (EU) 2015/2302 — kein Gutschein gegen den Willen des Reisenden), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2023-06-08&Aktenzeichen=C-407/21)
3. Zur Bemessung der Minderungsquote und zur Erheblichkeitsschwelle des § 651n Abs. 2 BGB ist die instanzgerichtliche Praxis einzelfallbezogen zu recherchieren `[unverifiziert - prüfen]`

## Ausgabeformat

```
PAUSCHALREISE — MÄNGELPRÜFUNG — <Mandat> — <Datum>

I.   Vertrag
     Veranstalter:            <…>       Buchungsnr.: <…>
     Reisezeitraum:           <von – bis>  Reisetage: <N>
     Gesamtreisepreis:        <Betrag> EUR   Tagespreis: <Betrag> EUR
     Vertragstyp:             [Pauschalreise § 651a / verbunden § 651w / Vermittlung]

II.  Obliegenheiten
     Mängelanzeige § 651o:    <Datum / Form / Adressat>   [gewahrt / versäumt]
     Abhilfeverlangen § 651k: <Datum / Frist>             [gestellt / nicht]

III. Mangelpositionen (§ 651i Abs. 2)
     1. <Position>  Dauer: <N> Tage  Quote: <%>  Betrag: <…> EUR
     2. <Position>  Dauer: <N> Tage  Quote: <%>  Betrag: <…> EUR
     Hinweis: Quoten sind einzelfallbezogen begründet; Tabellenwerte
     dienen nur der Orientierung und sind keine Rechtsgrundlage.

IV.  Rechtsfolgen
     Minderung § 651m:        <Betrag> EUR
     Selbstabhilfe § 651k:    <Betrag> EUR
     Kündigung § 651l:        [erklärt am <Datum> / nicht erklärt]
     Schadensersatz § 651n Abs. 1: <Betrag> EUR
     Entgangene Urlaubsfreude § 651n Abs. 2: <Betrag> EUR
     Vergebliche Aufwendungen: <Betrag> EUR
     GESAMTFORDERUNG:         <Betrag> EUR

V.   Verjährung § 651j
     Vertragliches Reiseende: <Datum>   Ablauf: <Datum>
     Hemmung § 203 BGB:       [ja seit <Datum> / nein]

VI.  Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VII. Quellenverzeichnis
```

### Formulierungshilfe — Mängelanzeige und Forderungsschreiben (Gerüst)

```
An <Reiseveranstalter>

Mängelanzeige und Zahlungsaufforderung
Pauschalreise <Buchungsnr.>, Reisezeitraum <von – bis>
Reisende: <Name 1>, <Name 2>

Sehr geehrte Damen und Herren,

ich zeige die Vertretung der o. g. Reisenden an und mache Rechte
wegen Reisemängeln nach § 651i Abs. 3 BGB geltend.

1. Vertragsinhalt
   Gebucht war ausweislich der Buchungsbestätigung vom <Datum>
   <Leistungsbeschreibung>.

2. Mängel (§ 651i Abs. 2 BGB)
   a) <Position>, vom <Datum> bis <Datum>. Nachweis: <Anlage>.
   b) <Position>, vom <Datum> bis <Datum>. Nachweis: <Anlage>.

3. Anzeige und Abhilfeverlangen
   Die Mängel wurden der Reiseleitung am <Datum> angezeigt
   (§ 651o BGB) und mit Schreiben vom <Datum> unter Fristsetzung
   bis zum <Datum> Abhilfe verlangt (§ 651k BGB). Abhilfe erfolgte
   nicht.

4. Minderung (§ 651m BGB)
   Bei einem Gesamtreisepreis von <…> EUR und <N> Reisetagen ergibt
   sich ein Tagesreisepreis von <…> EUR. Für die Position a)
   erscheint eine Quote von <…> % über <N> Tage angemessen, mithin
   <…> EUR; für Position b) <…> EUR. Insgesamt: <…> EUR.
   Die herangezogenen Vergleichswerte dienen ausschließlich der
   Orientierung; maßgeblich ist die Bewertung nach § 651m BGB.

5. Schadensersatz (§ 651n BGB)
   Ferner werden <nutzlose Aufwendungen> in Höhe von <…> EUR sowie
   eine angemessene Entschädigung wegen nutzlos aufgewendeter
   Urlaubszeit nach § 651n Abs. 2 BGB in Höhe von <…> EUR verlangt.

Ich fordere Sie auf, den Gesamtbetrag von <…> EUR bis zum <Datum>
zu zahlen. Nach fruchtlosem Fristablauf tritt Verzug ein (§ 286 BGB).
```

## Risiken / typische Fehler

- **Mängelanzeige unterblieben oder nicht beweisbar.** § 651o Abs. 2 BGB sperrt Minderung und Schadensersatz, soweit Abhilfe möglich gewesen wäre; die Anzeige gegenüber dem Hotelpersonal genügt nicht.
- **Abhilfefrist nicht gesetzt.** Selbstabhilfe und Kündigung setzen grundsätzlich den fruchtlosen Ablauf einer angemessenen Frist voraus.
- **Frankfurter Tabelle als Rechtsgrundlage zitiert.** Sie ist eine Orientierungshilfe ohne Bindungswirkung; Rechtsgrundlage ist § 651m BGB.
- **Minderungsquoten addiert.** Positionen sind einzeln zu bewerten; eine Summe über 100 % ist ausgeschlossen.
- **Falscher Anspruchsgegner.** Anspruchsgegner ist der Reiseveranstalter, nicht das Hotel, nicht die Airline, nicht das Reisebüro.
- **Verjährung § 651j BGB verkannt.** Die Zweijahresfrist läuft ab dem **vertraglich vereinbarten** Reiseende, nicht ab Kenntnis und nicht nach der Ultimo-Regel.
- **Entgangene Urlaubsfreude ohne Erheblichkeitsschwelle verlangt.** § 651n Abs. 2 BGB setzt Vereitelung oder erhebliche Beeinträchtigung voraus.
- **Aktenzeichen erfunden** — jede Entscheidung verifizieren oder als `[unverifiziert - prüfen]` kennzeichnen.
