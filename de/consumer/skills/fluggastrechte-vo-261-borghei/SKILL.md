---
name: fluggastrechte-vo-261-borghei
title: /reise-fluggastrecht:fluggastrechte-vo-261
description: Ansprüche des Fluggastes nach der VO (EG) 261/2004 – Anwendungsbereich Art. 3, Ausgleichszahlung Art. 7 (250/400/600 EUR nach Entfernung), Annullierung Art. 5, große Verspätung am Endziel, Nichtbeförderung Art. 4, außergewöhnliche Umstände Art. 5 Abs. 3, Betreuungsleistungen Art. 9, Erstattung und anderweitige Beförderung Art. 8, Anrechnung Art. 12, Gerichtsstand Art. 7 Nr. 1 EuGVVO und Verjährung §§ 195, 199 BGB. Use when ein Flug annulliert, überbucht oder erheblich verspätet war und Ausgleichs-, Betreuungs- oder Erstattungsansprüche gegen das ausführende Luftfahrtunternehmen geprüft und beziffert werden sollen.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/reise-fluggastrecht/skills/fluggastrechte-vo-261
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /reise-fluggastrecht:fluggastrechte-vo-261

## Zweck

Der Skill prüft die Ansprüche eines Fluggastes gegen das ausführende Luftfahrtunternehmen vollständig — Anwendungsbereich, Störungsart, Ausgleich, Betreuung, Erstattung, Einwand außergewöhnlicher Umstände, Zuständigkeit und Verjährung — und erzeugt die bezifferte Zahlungsaufforderung. Er ist bewusst gegen die Massenpraxis gebaut: Serienbriefe ohne Prüfung des Art. 3 und ohne Verjährungsrechnung erzeugen unbegründete Forderungen und Kostenrisiken.

## Eingaben

- Flugdaten: Flugnummer, Datum, Abflug- und Ankunftsflughafen, ausführendes Luftfahrtunternehmen
- Buchungsart: einheitliche Buchung mit Anschlussflügen? Codeshare? Endziel
- Bestätigte Buchung und rechtzeitige Abfertigung nachgewiesen (Bordkarte, Buchungsbestätigung)?
- Störung: Annullierung, Nichtbeförderung, Verspätung — mit Ist-Ankunftszeit am Endziel
- Vom Luftfahrtunternehmen genannter Grund und angebotene Ersatzbeförderung
- Erbrachte Betreuungsleistungen (Verpflegung, Hotel, Transfer, Kommunikation)
- Angefallene Zusatzkosten und Belege
- Anzahl der Fluggäste und etwaige Abtretungen an Dritte

## Sub-Agent-Architektur

Ein Researcher bestimmt Vertragstyp und Anspruchsgegner, holt Verordnungstext und EuGH-Rechtsprechung und markiert die streitige Kasuistik. Ein Drafter prüft in fester Reihenfolge Anwendungsbereich, Störungsart, Ausgleich, Einwand und Nebenansprüche, beziffert und entwirft die Zahlungsaufforderung. Ein Reviewer kontrolliert die Verjährung nach der Ultimo-Regel, die Zuständigkeit und die Beweislastverteilung des Art. 5 Abs. 3 und markiert jede nicht bestätigte Entscheidung mit `[unverifiziert - prüfen]`. Keine Rolle erfindet ein Aktenzeichen.

## Ablauf

### 1. Anwendungsbereich ([Art. 3 VO (EG) 261/2004](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32004R0261))

Kumulativ zu prüfen:

- **Räumlich**: Abflug von einem Flughafen im Hoheitsgebiet eines Mitgliedstaats — **oder** Abflug aus einem Drittstaat mit Ziel in einem Mitgliedstaat, wenn das ausführende Luftfahrtunternehmen ein **Gemeinschaftsluftfahrtunternehmen** ist (Art. 3 Abs. 1).
- **Bestätigte Buchung** und, außer bei Annullierung, **rechtzeitige Abfertigung** (Art. 3 Abs. 2) — regelmäßig 45 Minuten vor der veröffentlichten Abflugzeit, soweit keine andere Zeit angegeben ist.
- **Kein Ausschluss**: kostenlose oder zu einem nicht öffentlich verfügbaren Sondertarif erlangte Beförderung (Art. 3 Abs. 3); Vielfliegerprämien sind erfasst.
- **Anspruchsgegner ist das ausführende Luftfahrtunternehmen** (Art. 2 lit. b) — nicht das vermarktende Codeshare-Unternehmen, nicht das Reisebüro, nicht der Reiseveranstalter.

Ist der Anwendungsbereich nicht eröffnet, bleiben nur vertragliche Ansprüche und das Montrealer Übereinkommen.

### 2. Störungsart bestimmen ([Art. 4](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32004R0261), [Art. 5](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32004R0261), [Art. 6](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32004R0261))

| Störung | Norm | Ausgleich |
|---|---|---|
| **Nichtbeförderung** (Überbuchung, Verweigerung ohne vertretbaren Grund) | Art. 4 Abs. 3 | ja, nach Art. 7 |
| **Annullierung** (Nichtdurchführung des geplanten Fluges) | Art. 5 Abs. 1 lit. c | ja, nach Art. 7, mit den Ausnahmen der Unterrichtungsfristen |
| **Große Verspätung** am Endziel | richterrechtlich aus Art. 5–7 entwickelt | ja, nach Art. 7 |

**Abgrenzung Annullierung / Verspätung**: Maßgeblich ist, ob die ursprüngliche Flugplanung aufgegeben wurde. Änderung der Flugnummer, Rückkehr zum Abflugort oder Streichung aus dem Flugplan sprechen für Annullierung.

**Unterrichtungsfristen bei Annullierung** (Art. 5 Abs. 1 lit. c): Kein Ausgleich, wenn die Unterrichtung mindestens zwei Wochen vorher erfolgte; bei Unterrichtung zwischen zwei Wochen und sieben Tagen bzw. weniger als sieben Tagen nur bei Einhaltung der dort genannten engen Zeitkorridore für die Ersatzbeförderung. Die Darlegungslast für die rechtzeitige Unterrichtung trägt nach Art. 5 Abs. 4 das Luftfahrtunternehmen.

### 3. Große Verspätung ab drei Stunden ([Art. 7 VO (EG) 261/2004](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32004R0261))

Der Verordnungstext sieht für die Verspätung selbst **keinen** Ausgleichsanspruch vor. Der Anspruch ist **richterrechtlich** entwickelt: Fluggäste, die ihr **Endziel** mit einer Verspätung von **drei Stunden oder mehr** erreichen, werden annullierten Fluggästen gleichgestellt (EuGH, Urt. v. 19.11.2009 – verb. Rs. C-402/07 und C-432/07 „Sturgeon u.a.", NJW 2010, 43 = EuZW 2009, 890 = Slg. 2009, I-10923, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2009-11-19&Aktenzeichen=C-402/07); bestätigt durch EuGH, Urt. v. 23.10.2012 – verb. Rs. C-581/10 und C-629/10 „Nelson u.a.", NJW 2013, 671 = EuZW 2012, 906, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2012-10-23&Aktenzeichen=C-581/10)). Diese Gleichstellung steht **nicht** im Verordnungstext; sie ist Auslegungsergebnis des EuGH und als solches zu kennzeichnen, wenn sie gegenüber Gericht oder Gegenseite verwendet wird.

Zwei praktische Folgerungen:

- Maßgeblich ist die **Ankunft am Endziel**, nicht der Abflug und nicht der Zubringer. Bei einheitlicher Buchung mit Anschlussflug zählt die Gesamtverspätung (EuGH, Urt. v. 26.02.2013 – Rs. C-11/11 „Air France/Folkerts", NJW 2013, 1291 = EuZW 2013, 434, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2013-02-26&Aktenzeichen=C-11/11)).
- Ankunftszeit ist der Zeitpunkt, zu dem mindestens eine Flugzeugtür geöffnet wird und den Fluggästen das Verlassen des Flugzeugs gestattet ist — nicht das Aufsetzen und nicht das Erreichen der Parkposition (EuGH, Urt. v. 04.09.2014 – Rs. C-452/13 „Germanwings", NJW 2015, 221 = EuZW 2014, 873, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2014-09-04&Aktenzeichen=C-452/13)).

### 4. Höhe der Ausgleichszahlung ([Art. 7 VO (EG) 261/2004](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32004R0261))

| Entfernung | Betrag |
|---|---|
| bis 1.500 km | **250 EUR** |
| innergemeinschaftlich über 1.500 km; alle sonstigen Flüge zwischen 1.500 und 3.500 km | **400 EUR** |
| alle übrigen Flüge | **600 EUR** |

Die Entfernung wird nach der **Großkreismethode** zwischen Abflugort und **Endziel** berechnet (Art. 7 Abs. 4). Nach Art. 7 Abs. 2 kann der Betrag um 50 % gekürzt werden, wenn eine anderweitige Beförderung angeboten wurde und die Ankunftsverspätung die dort genannten Grenzen (2, 3 bzw. 4 Stunden) nicht überschreitet. Der Anspruch besteht **pro Fluggast**, auch für Kinder mit eigenem Sitzplatz.

### 5. Außergewöhnliche Umstände ([Art. 5 Abs. 3 VO (EG) 261/2004](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32004R0261))

Der Ausgleichsanspruch entfällt, wenn die Störung auf außergewöhnliche Umstände zurückgeht, die sich **auch dann nicht hätten vermeiden lassen, wenn alle zumutbaren Maßnahmen ergriffen worden wären**. Der Einwand hat damit **zwei** Stufen — Ereignis **und** zumutbare Maßnahmen. Darlegungs- und Beweislast liegen vollständig beim Luftfahrtunternehmen.

Die Kasuistik ist streitig und in Bewegung. Die mit Fundstelle und Primärquelle belegten Linien sind verifiziert; die Punkte **Wetter** und **Vorfeldfolgen** beruhen auf instanzgerichtlicher Praxis ohne belegte Leitentscheidung und sind vor Verwendung im Einzelfall zu recherchieren `[unverifiziert - prüfen]`:

- **Technischer Defekt**: grundsätzlich **kein** außergewöhnlicher Umstand, weil der Wartungs- und Betriebsbereich zur normalen Tätigkeit gehört (EuGH, Urt. v. 22.12.2008 – Rs. C-549/07 „Wallentin-Hermann", NJW 2009, 347 = EuZW 2009, 111, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2008-12-22&Aktenzeichen=C-549/07); EuGH, Urt. v. 17.09.2015 – Rs. C-257/14 „van der Lans", NJW 2015, 3427, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2015-09-17&Aktenzeichen=C-257/14)). Anders bei verstecktem Fabrikationsfehler oder Sabotage.
- **Wilder Streik der eigenen Belegschaft**: **kein** außergewöhnlicher Umstand (EuGH, Urt. v. 17.04.2018 – verb. Rs. C-195/17 u.a. „Krüsemann u.a.", NJW 2018, 1592 = EuZW 2018, 457, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2018-04-17&Aktenzeichen=C-195/17)). Streiks Dritter (Fluglotsen, Flughafenbetreiber) werden anders beurteilt.
- **Wetter**: nur, wenn es den konkreten Flug tatsächlich hinderte; der pauschale Verweis auf „Unwetter" genügt nicht. Auch die Frage der zumutbaren Umplanung ist zu prüfen.
- **Störender Fluggast**: kann außergewöhnlicher Umstand sein, sofern das Luftfahrtunternehmen darlegt, alle zumutbaren Maßnahmen ergriffen zu haben (EuGH, Urt. v. 11.06.2020 – Rs. C-74/19 „Transportes Aéreos Portugueses", NJW-RR 2020, 871 = EuZW 2020, 617, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2020-06-11&Aktenzeichen=C-74/19)).
- **Vorfeldfolgen**: Beruht die Verspätung auf einem früheren Umlauf, muss die Ursachenkette bis zum konkreten Flug durchgehalten werden.

Fundstellen verifiziert; die jeweilige Kernaussage ist im Volltext gegenzulesen.

### 6. Betreuung und Erstattung ([Art. 8](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32004R0261), [Art. 9](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32004R0261))

**Diese Ansprüche bestehen auch bei außergewöhnlichen Umständen.** Sie sind vom Ausgleichsanspruch strikt zu trennen:

- **Art. 9**: Mahlzeiten und Erfrischungen in angemessenem Verhältnis zur Wartezeit, Hotelunterbringung und Transfer bei erforderlicher Übernachtung, zwei Telefonate oder gleichwertige Kommunikation. Hat der Fluggast selbst gebucht, ist der Aufwand zu erstatten, soweit er angemessen war.
- **Art. 8**: Wahlrecht zwischen vollständiger Erstattung des Flugpreises (binnen sieben Tagen) nebst gegebenenfalls Rückflug zum ersten Abflugort und anderweitiger Beförderung zum Endziel — zum frühestmöglichen Zeitpunkt oder zu einem späteren Termin nach Wahl des Fluggastes. Das ergibt sich unmittelbar aus Art. 8 Abs. 1 lit. a bis c.
- **Grenzen und Reichweite des Art. 8 in Krisenlagen**: Ein im Rahmen einer konsularischen Unterstützungsmaßnahme organisierter **Repatriierungsflug ist keine anderweitige Beförderung** iSd Art. 8 Abs. 1 lit. b; die Kosten eines solchen Fluges sind vom Luftfahrtunternehmen nach der Verordnung nicht zu erstatten. Zugleich kennt die Verordnung **keine** Kategorie „besonders außergewöhnlicher" Umstände, die von den Unterstützungsleistungen des Art. 8 vollständig befreien würde; verletzt das Unternehmen diese Pflicht, kann der Fluggast Erstattung der Beträge verlangen, die sich im Einzelfall als notwendig, angemessen und zumutbar erweisen (EuGH, Urt. v. 08.06.2023 – Rs. C-49/22 „Austrian Airlines (Rückholflug)", NJW 2023, 2629 = EuZW 2023, 815, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2023-06-08&Aktenzeichen=C-49/22)).

### 7. Weitergehender Schadensersatz und Anrechnung ([Art. 12 VO (EG) 261/2004](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32004R0261))

Die Verordnung lässt weitergehende Schadensersatzansprüche unberührt; die Ausgleichszahlung kann jedoch **angerechnet** werden. Weitergehende Ansprüche folgen aus dem Beförderungsvertrag, aus dem Pauschalreisevertrag (`/reise-fluggastrecht:pauschalreise-maengel`) oder aus dem Montrealer Übereinkommen (Art. 19 für Verspätungsschaden; Art. 35 mit einer **zweijährigen Ausschlussfrist**).

### 8. Zuständigkeit und Durchsetzung ([Art. 7 Nr. 1 EuGVVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32012R1215))

- **International**: Bei Luftbeförderung kann am Ort des **Abflugs** oder am Ort der **Ankunft** geklagt werden — beides sind Erfüllungsorte iSd Art. 7 Nr. 1 lit. b EuGVVO (EuGH, Urt. v. 09.07.2009 – Rs. C-204/08 „Rehder", EuZW 2009, 569 = NJW 2009, 487 (Ls.), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2009-07-09&Aktenzeichen=C-204/08)). Der Verbrauchergerichtsstand der Art. 17 ff. EuGVVO greift bei reinen Beförderungsverträgen regelmäßig **nicht**.
- **National**: § 29 ZPO; sachliche Zuständigkeit nach Streitwert, bei den typischen Beträgen das Amtsgericht.
- **Außergerichtlich**: Schlichtung bei der söp und Durchsetzungsstelle nach Art. 16 (in Deutschland das Luftfahrt-Bundesamt) — die Durchsetzungsstelle setzt den individuellen Anspruch allerdings nicht titelfähig durch.

### 9. Verjährung ([§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html))

Die Verordnung enthält keine eigene Verjährungsregel; es gilt nationales Recht. In Deutschland ist das die **Regelverjährung von drei Jahren** ab Schluss des Jahres, in dem der Anspruch entstanden ist und der Gläubiger Kenntnis erlangt hat (**Ultimo-Regel**). Die zweijährige Ausschlussfrist des Art. 35 Montrealer Übereinkommen gilt für die Ansprüche **aus dem Übereinkommen**, nicht für den Ausgleichsanspruch nach Art. 7.

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur die Arithmetik** der §§ 195, 199 BGB einschließlich der Ultimo-Regel. Entstehung, Kenntnis und etwaige Hemmung nach § 203 BGB bleiben juristische Eingaben und sind gesondert zu belegen.

```bash
# Flug am 10.03.2023, Kenntnis der anspruchsbegründenden Umstände am 05.07.2023
python -m scripts.legal_calc.cli verjaehrung --entstehung 10.03.2023 --kenntnis 05.07.2023

# Frist zur Zahlungsaufforderung: 14 Tage ab Zugang des Schreibens
python -m scripts.legal_calc.cli frist --ereignis 21.07.2026 --menge 14 --einheit tage --land BY
```

`--json` liefert die Rechenschritte samt Normzitat. § 193 BGB ist auf die Verjährung nach h.M. **nicht** anwendbar — die Frist läuft auch an einem Samstag, Sonntag oder Feiertag ab. Die Entfernung nach Art. 7 Abs. 4 und die Minderungsquote sind **nicht** Gegenstand des Rechners.

## Quellen

### Statute

- [VO (EG) Nr. 261/2004](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32004R0261) — Art. 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16
- [VO (EU) Nr. 1215/2012 (EuGVVO)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32012R1215) — Art. 7 Nr. 1, Art. 17–19
- [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html), [§ 203 BGB](https://www.gesetze-im-internet.de/bgb/__203.html), [§ 286 BGB](https://www.gesetze-im-internet.de/bgb/__286.html), [§ 288 BGB](https://www.gesetze-im-internet.de/bgb/__288.html)
- [§ 29 ZPO](https://www.gesetze-im-internet.de/zpo/__29.html)
- Montrealer Übereinkommen, Art. 19, 22, 29, 35

### Kommentare

- Staudinger/Keiler, Fluggastrechte-Verordnung, Art. 5 Rn. 1 ff., Art. 7 Rn. 1 ff.
- Führich, Reiserecht, Kap. Fluggastrechte.
- Bergmann/Blankenburg, Fluggastrechte, Art. 3 Rn. 1 ff.
- Tonner, in: MüKo-BGB, Vor § 651a Rn. 1 ff. (Verhältnis Pauschalreise / VO 261/2004).

### Rechtsprechung

1. EuGH, Urt. v. 19.11.2009 – verb. Rs. C-402/07 und C-432/07, Sturgeon u.a., NJW 2010, 43 = EuZW 2009, 890 = Slg. 2009, I-10923 (Gleichstellung großer Verspätung ab drei Stunden), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2009-11-19&Aktenzeichen=C-402/07)
2. EuGH, Urt. v. 23.10.2012 – verb. Rs. C-581/10 und C-629/10, Nelson u.a., NJW 2013, 671 = EuZW 2012, 906 (Bestätigung der Sturgeon-Linie), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2012-10-23&Aktenzeichen=C-581/10)
3. EuGH, Urt. v. 22.12.2008 – Rs. C-549/07, Wallentin-Hermann, NJW 2009, 347 = EuZW 2009, 111 (technischer Defekt grundsätzlich kein außergewöhnlicher Umstand), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2008-12-22&Aktenzeichen=C-549/07)
4. EuGH, Urt. v. 17.09.2015 – Rs. C-257/14, van der Lans, NJW 2015, 3427 (Bestätigung und Fortführung für unerwartete technische Defekte), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2015-09-17&Aktenzeichen=C-257/14)
5. EuGH, Urt. v. 17.04.2018 – verb. Rs. C-195/17 u.a., Krüsemann u.a., NJW 2018, 1592 = EuZW 2018, 457 (wilder Streik der eigenen Belegschaft), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2018-04-17&Aktenzeichen=C-195/17)
6. EuGH, Urt. v. 11.06.2020 – Rs. C-74/19, Transportes Aéreos Portugueses, NJW-RR 2020, 871 = EuZW 2020, 617 (störender Fluggast; zumutbare Maßnahmen), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2020-06-11&Aktenzeichen=C-74/19)
7. EuGH, Urt. v. 26.02.2013 – Rs. C-11/11, Air France/Folkerts, NJW 2013, 1291 = EuZW 2013, 434 (Endziel bei Anschlussflug), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2013-02-26&Aktenzeichen=C-11/11)
8. EuGH, Urt. v. 04.09.2014 – Rs. C-452/13, Germanwings, NJW 2015, 221 = EuZW 2014, 873 (Ankunftszeit = Öffnen mindestens einer Flugzeugtür), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2014-09-04&Aktenzeichen=C-452/13)
9. EuGH, Urt. v. 09.07.2009 – Rs. C-204/08, Rehder, EuZW 2009, 569 = NJW 2009, 487 (Ls.) (Gerichtsstand Abflug- oder Ankunftsort), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2009-07-09&Aktenzeichen=C-204/08)
10. EuGH, Urt. v. 08.06.2023 – Rs. C-49/22, Austrian Airlines (Rückholflug), NJW 2023, 2629 = EuZW 2023, 815 (Repatriierungsflug ist keine anderweitige Beförderung; Reichweite des Art. 8), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2023-06-08&Aktenzeichen=C-49/22)
11. BGH, Urt. v. 09.12.2014 – X ZR 147/13, NJW-RR 2015, 618 = MDR 2015, 447 — **Achtung, Themen-Mismatch:** Datum, Aktenzeichen und Fundstelle sind bestätigt, die Entscheidung betrifft jedoch die **Anzahlungsklausel im Reisevertrag** (Anzahlung von nicht mehr als 20 % des Reisepreises in AGB ist wirksam), **nicht** die einheitliche Buchung von Anschlussflügen, als die sie hier ursprünglich geführt wurde, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2014-12-09&Aktenzeichen=X%20ZR%20147/13). Für die einheitliche Buchung mit Anschlussflug ist die belegte Grundlage Folkerts (Nr. 7); eine BGH-Entscheidung hierzu ist gesondert zu recherchieren `[unverifiziert - prüfen]`

## Ausgabeformat

```
FLUGGASTRECHTE VO (EG) 261/2004 — <Mandat> — <Datum>

I.   Sachverhalt
     Flug:                    <Nr. / Datum / Strecke>
     Ausführendes LFU:        <…>       Endziel: <…>
     Ist-Ankunft am Endziel:  <…>       Verspätung: <hh:mm>

II.  Anwendungsbereich (Art. 3)
     Räumlich:                [+ / –] <Abflug EU / EU-LFU>
     Bestätigte Buchung:      [+ / –]
     Rechtzeitige Abfertigung:[+ / –]
     Ausschluss Art. 3 Abs. 3:[nein / ja]

III. Störungsart
     [Nichtbeförderung Art. 4 / Annullierung Art. 5 / große Verspätung]
     Unterrichtung bei Annullierung: <Datum / Frist Art. 5 Abs. 1 lit. c>

IV.  Ausgleichszahlung (Art. 7)
     Entfernung (Großkreis):  <km>
     Betrag je Fluggast:      <250 / 400 / 600> EUR
     Kürzung Art. 7 Abs. 2:   [nein / ja — 50 %]
     Anzahl Fluggäste:        <N>        Gesamt: <Betrag> EUR

V.   Einwand außergewöhnlicher Umstände (Art. 5 Abs. 3)
     Behaupteter Umstand:     <…>
     Ereignis außergewöhnlich:[+ / – / streitig]
     Zumutbare Maßnahmen:     [dargelegt / nicht dargelegt]
     Beweislast:              Luftfahrtunternehmen

VI.  Nebenansprüche
     Betreuung Art. 9:        <Verpflegung / Hotel / Transfer / Kommunikation>
     Erstattung / Umbuchung Art. 8: <…>
     Weitergehender Schaden Art. 12: <… abzüglich Anrechnung>

VII. Durchsetzung
     Gerichtsstand:           <Abflug- / Ankunftsort; AG <Ort>>
     Verjährung:              Ablauf am <Datum> (§§ 195, 199 BGB)
     Fristsetzung:            <Datum>

VIII.Risiko: 🟢 / 🟡 / 🔴 <Begründung>
IX.  Quellenverzeichnis
```

### Formulierungshilfe — Ausgleichsforderung an die Airline (Gerüst)

```
An <Luftfahrtunternehmen>, Kundenservice

Ausgleichszahlung nach Art. 7 VO (EG) Nr. 261/2004
Flug <Nr.> am <Datum>, Buchungsreferenz <…>
Fluggäste: <Name 1>, <Name 2>

Sehr geehrte Damen und Herren,

ich zeige die Vertretung der o. g. Fluggäste an. Der Flug <Nr.>
sollte am <Datum> um <hh:mm> Uhr von <Abflug> nach <Endziel> führen.
Tatsächlich <wurde er annulliert / erreichten die Fluggäste das
Endziel erst am <Datum> um <hh:mm> Uhr, mithin mit einer Verspätung
von <hh:mm> Stunden>.

1. Der Anwendungsbereich der Verordnung ist nach Art. 3 Abs. 1
   eröffnet; eine bestätigte Buchung lag vor, die Abfertigung
   erfolgte rechtzeitig (Anlagen 1 und 2).
2. Ihr Unternehmen ist ausführendes Luftfahrtunternehmen iSd
   Art. 2 lit. b der Verordnung.
3. Die Entfernung zwischen <Abflug> und <Endziel> beträgt nach der
   Großkreismethode <…> km. Der Ausgleichsanspruch beläuft sich
   damit nach Art. 7 Abs. 1 lit. <a/b/c> auf <Betrag> EUR je
   Fluggast, insgesamt <Gesamtbetrag> EUR.
4. Soweit Sie sich auf außergewöhnliche Umstände nach Art. 5 Abs. 3
   berufen, weise ich vorsorglich darauf hin, dass Sie sowohl den
   Umstand selbst als auch die Ergreifung aller zumutbaren Maßnahmen
   darzulegen und zu beweisen haben.
5. Daneben mache ich die Erstattung folgender Aufwendungen nach
   Art. 9 geltend: <Positionen mit Belegen>.

Ich fordere Sie auf, den Gesamtbetrag von <…> EUR bis zum <Datum>
auf das Konto <…> zu zahlen. Nach fruchtlosem Fristablauf tritt
Verzug ein (§ 286 BGB); weitere Kosten der Rechtsverfolgung sind
dann ebenfalls zu erstatten.
```

## Risiken / typische Fehler

- **Anwendungsbereich nicht geprüft.** Bei Abflug aus einem Drittstaat mit einer Nicht-EU-Airline ist die Verordnung nicht anwendbar — die häufigste unbegründete Serienforderung.
- **Falscher Anspruchsgegner.** Anspruchsgegner ist das ausführende Luftfahrtunternehmen, nicht der Vermarkter, das Reisebüro oder der Veranstalter.
- **Verspätung am Abflug statt am Endziel gemessen.** Maßgeblich ist ausschließlich die Ankunftsverspätung am Endziel.
- **Entfernung falsch berechnet.** Großkreismethode zwischen Abflugort und Endziel, nicht Summe der Teilstrecken.
- **Außergewöhnliche Umstände ungeprüft akzeptiert.** Das Luftfahrtunternehmen muss Ereignis **und** zumutbare Maßnahmen darlegen und beweisen.
- **Betreuungsansprüche vergessen.** Art. 8 und Art. 9 bestehen unabhängig vom Ausgleichsanspruch, auch bei außergewöhnlichen Umständen.
- **Verjährung nicht gerechnet.** Es gilt die Ultimo-Regel der §§ 195, 199 BGB; die zweijährige Frist des Art. 35 Montrealer Übereinkommen wird häufig fälschlich auf den Ausgleichsanspruch übertragen.
- **Aktenzeichen erfunden** — jede Entscheidung verifizieren oder als `[unverifiziert - prüfen]` kennzeichnen.
