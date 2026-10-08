---
name: schoenheitsreparaturen-rueckgabe-borghei
title: /mietrecht:schoenheitsreparaturen-rueckgabe
description: Schönheitsreparaturen und Rückgabeabwicklung im Wohnraummietrecht – Erhaltungspflicht des Vermieters § 535 Abs. 1 S. 2 BGB, Rückgabepflicht § 546 BGB, AGB-Kontrolle starrer Fristenpläne und Endrenovierungsklauseln §§ 307, 309 BGB, unrenoviert übergebene Wohnung und hälftige Kostenteilung, Rückbau- und Wiederherstellungspflicht, Schadensersatz statt der Leistung §§ 280, 281 BGB, sechsmonatige Verjährung § 548 BGB. Use when eine Schönheitsreparaturklausel geprüft, eine Wohnung zurückgegeben oder eine Renovierungs- bzw. Schadensersatzforderung nach Mietende geltend gemacht oder abgewehrt wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/mietrecht/skills/schoenheitsreparaturen-rueckgabe
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /mietrecht:schoenheitsreparaturen-rueckgabe

## Zweck

Schönheitsreparaturen schuldet von Gesetzes wegen der **Vermieter** (§ 535 Abs. 1 S. 2 BGB). Nur eine wirksame formularvertragliche Abwälzung dreht das um — und ein erheblicher Teil der verwendeten Klauseln ist unwirksam, mit der Folge, dass die gesetzliche Lage vollständig wiederauflebt. Diese Skill prüft die Klausel, ordnet die Rückgabeabwicklung und stellt an den Anfang jeder Fristenplanung die **sechsmonatige Verjährung des § 548 BGB** — den schärfsten Fallstrick der Rückgabeabwicklung.

## Eingaben

- **Mietvertragsklauseln** im Wortlaut: Schönheitsreparaturen, Fristenplan, Endrenovierung, Quotenabgeltung, Farbwahl
- **Zustand bei Übergabe**: renoviert / unrenoviert / renovierungsbedürftig; Übergabeprotokoll
- Ob für die Übernahme einer unrenovierten Wohnung ein **angemessener Ausgleich** gewährt wurde
- **Zustand bei Rückgabe**, Rückgabeprotokoll, Fotos, Datum des **Rückerhalts**
- Vom Mieter vorgenommene **bauliche Veränderungen** (Einbauten, Wanddurchbrüche, Bodenbeläge, Farbwahl)
- Geltend gemachte Forderungen: Renovierungskosten, Kostenvoranschlag, Schadensersatz
- Kautionshöhe und -stand

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention). Ein **Verjährungs-Wächter** ermittelt **zuerst** den Ablauf der Frist des § 548 BGB — ist sie abgelaufen, erübrigt sich jede weitere Prüfung. Ein **Klausel-Prüfer** unterzieht jede Klausel der Inhaltskontrolle nach §§ 307 ff. BGB und beachtet das Verbot der geltungserhaltenden Reduktion. Ein **Zustands-Prüfer** klärt Übergabe- und Rückgabezustand und trennt vertragsgemäße Abnutzung von Schäden. Ein **Anspruchs-Prüfer** baut den Schadensersatzanspruch nach §§ 280, 281 BGB auf und prüft die Fristsetzung. Ein **Rückbau-Prüfer** behandelt Einbauten und Wegnahmerecht.

## Ablauf

### 1. Verjährung zuerst ([§ 548 BGB](https://www.gesetze-im-internet.de/bgb/__548.html))

Die **Ersatzansprüche des Vermieters wegen Veränderungen oder Verschlechterungen der Mietsache verjähren in sechs Monaten**. Die Frist beginnt mit dem **Rückerhalt** der Sache — dem Zeitpunkt, in dem der Vermieter die tatsächliche Sachherrschaft und die Möglichkeit zur Untersuchung erlangt, nicht mit dem rechtlichen Mietende. Erfasst sind auch Ansprüche auf Schadensersatz wegen **unterlassener Schönheitsreparaturen**. Die kurze Frist ist **nicht** durch AGB verlängerbar. Umgekehrt verjähren Ansprüche des **Mieters** auf Ersatz von Aufwendungen und sein Wegnahmerecht ebenfalls in sechs Monaten ab Beendigung des Mietverhältnisses (§ 548 Abs. 2 BGB). Praxis: Rückgabetermin, Untersuchungstermin und Verjährungsende gehören am Tag der Rückgabe in den Fristenkalender; eine Hemmung nach § 203 BGB durch Verhandlungen ist zu dokumentieren.

### 2. Gesetzliche Ausgangslage ([§ 535 Abs. 1 S. 2 BGB](https://www.gesetze-im-internet.de/bgb/__535.html))

Der Vermieter hat die Mietsache in einem zum vertragsgemäßen Gebrauch geeigneten Zustand zu überlassen und sie während der Mietzeit in diesem Zustand **zu erhalten**. Schönheitsreparaturen — Tapezieren, Anstreichen oder Kalken der Wände und Decken, Streichen der Fußböden, Heizkörper, Innentüren, Fenster und Außentüren von innen — sind Teil dieser Erhaltungspflicht. Ohne wirksame Abwälzung schuldet der Mieter **nichts**.

### 3. AGB-Kontrolle der Abwälzungsklausel ([§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html))

Die formularvertragliche Abwälzung ist im Grundsatz zulässig, scheitert aber an folgenden Konstellationen:

- **Starrer Fristenplan** — feste Fristen ohne Rücksicht auf den tatsächlichen Renovierungsbedarf („spätestens nach drei/fünf/sieben Jahren") benachteiligen den Mieter unangemessen und sind unwirksam. Zulässig ist nur ein **weicher** Fristenplan („im Allgemeinen", „in der Regel", „üblicherweise").
- **Endrenovierungsklausel** — die Verpflichtung, unabhängig vom Zustand bei Auszug zu renovieren, ist unwirksam.
- **Quotenabgeltungsklausel** — die anteilige Kostenbeteiligung für noch nicht fällige Schönheitsreparaturen ist unwirksam, weil der Mieter die Belastung bei Vertragsschluss nicht abschätzen kann.
- **Enge Farbwahlklausel für die Mietzeit** — Vorgaben zur Farbgestaltung während des laufenden Mietverhältnisses sind unwirksam; für die Rückgabe ist eine Beschränkung auf neutrale, hell deckende Farbtöne zulässig.
- **Fachhandwerkerklausel** — die zwingende Vorgabe, einen Fachbetrieb zu beauftragen, ist unwirksam; der Mieter darf fachgerecht selbst renovieren.

Eine unwirksame Klausel wird **nicht** auf das zulässige Maß zurückgeführt (**Verbot der geltungserhaltenden Reduktion**); sie entfällt ersatzlos, und es gilt § 535 Abs. 1 S. 2 BGB. Enthält der Vertrag mehrere Klauseln zum selben Regelungsgegenstand, kann die Unwirksamkeit einer Klausel den gesamten Komplex erfassen (Summierungseffekt).

### 4. Unrenoviert übergebene Wohnung und Kostenteilung

Wird die Wohnung dem Mieter **unrenoviert oder renovierungsbedürftig** überlassen, ist die formularvertragliche Abwälzung der Schönheitsreparaturen **unwirksam**, sofern der Vermieter dem Mieter keinen **angemessenen Ausgleich** gewährt (BGH, Urt. v. 18.03.2015 – VIII ZR 185/14, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2015-03-18&Aktenzeichen=VIII%20ZR%20185/14). Der Mieter müsste sonst eine Wohnung in besserem Zustand zurückgeben, als er sie erhalten hat.

Kehrseite: Ist die Klausel unwirksam, schuldet der **Vermieter** die Schönheitsreparaturen — er muss aber nur den **Zustand bei Vertragsbeginn** wiederherstellen, nicht den einer frisch renovierten Wohnung. Verlangt der Mieter die Durchführung, hat er sich daher **hälftig an den Kosten zu beteiligen** (BGH, Urt. v. 08.07.2020 – VIII ZR 163/18 und VIII ZR 270/18, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2020-07-08&Aktenzeichen=VIII%20ZR%20163/18). Die Quote ist im Einzelfall anzupassen.

### 5. Rückgabepflicht und vertragsgemäße Abnutzung ([§ 546 BGB](https://www.gesetze-im-internet.de/bgb/__546.html), [§ 538 BGB](https://www.gesetze-im-internet.de/bgb/__538.html))

Der Mieter hat die Mietsache **zurückzugeben** — besenrein und geräumt. **Veränderungen oder Verschlechterungen, die durch den vertragsgemäßen Gebrauch herbeigeführt werden, hat der Mieter nicht zu vertreten** (§ 538 BGB). Abzugrenzen sind daher:

- **vertragsgemäße Abnutzung** — Laufspuren, verblasste Tapeten, übliche Dübellöcher in angemessener Zahl: nicht ersatzpflichtig;
- **Schäden** — Brandlöcher, Wasserschäden, zerbrochene Sanitärobjekte, exzessive Dübellöcher, Tierschäden: ersatzpflichtig nach §§ 280 Abs. 1, 823 BGB.

Ein gemeinsames **Rückgabeprotokoll** mit Fotos ist das entscheidende Beweismittel für beide Seiten.

### 6. Rückbau- und Wiederherstellungspflicht ([§ 539 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__539.html))

Vom Mieter vorgenommene bauliche Veränderungen — Einbauküche, Trennwand, Parkett, Wanddurchbruch, Satellitenschüssel — sind bei Rückgabe grundsätzlich **zurückzubauen** und der ursprüngliche Zustand wiederherzustellen, sofern nichts anderes vereinbart ist. Der Mieter ist umgekehrt berechtigt, eine **Einrichtung wegzunehmen**, mit der er die Sache versehen hat (§ 539 Abs. 2 BGB); der Vermieter kann die Ausübung durch Zahlung einer **angemessenen Entschädigung** abwenden, sofern der Mieter kein berechtigtes Interesse an der Wegnahme hat (§ 552 BGB). Hat der Vermieter der Maßnahme **zugestimmt**, ist im Zweifel auszulegen, ob damit auch auf den Rückbau verzichtet wurde — Zustimmungen daher stets schriftlich mit Rückbauregelung.

### 7. Schadensersatz statt der Leistung ([§ 280 Abs. 1](https://www.gesetze-im-internet.de/bgb/__280.html), [§ 281 BGB](https://www.gesetze-im-internet.de/bgb/__281.html))

Kommt der Mieter einer **wirksam** übernommenen Renovierungspflicht nicht nach, kann der Vermieter Schadensersatz verlangen. Voraussetzung ist grundsätzlich eine **Fristsetzung** zur Nacherfüllung (§ 281 Abs. 1 BGB); nach Rückgabe der Wohnung ist sie nach h.M. entbehrlich, wenn der Mieter die Leistung endgültig verweigert oder der Vermieter bereits anderweitig vermietet hat. Der Schaden bemisst sich nach den **erforderlichen** Renovierungskosten; ein Kostenvoranschlag genügt zur Bezifferung, ein Abzug „neu für alt" ist zu prüfen. Anstelle der Renovierung kann der Vermieter den **Mietausfall** für die Renovierungszeit geltend machen — nicht beides kumulativ.

### 8. Abwicklung über die Kaution

Die Forderungen werden regelmäßig gegen die Kaution aufgerechnet. Dabei ist die Frist des § 548 BGB **vor** der Kautionsabrechnung zu prüfen: Eine verjährte Forderung kann nur unter den Voraussetzungen des [§ 215 BGB](https://www.gesetze-im-internet.de/bgb/__215.html) zur Aufrechnung gestellt werden. Vertiefung: `/mietrecht:kaution-mietsicherheit`.

## Deterministische Berechnung

Die sechsmonatige Verjährung des § 548 Abs. 1 BGB ist eine **Ereignisfrist** nach [§ 187 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__187.html) mit Fristende nach [§ 188 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__188.html); nach h.M. gilt [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html) bei der Verjährung **nicht** — die Frist läuft auch an einem Samstag, Sonntag oder Feiertag ab. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur die Arithmetik**; der maßgebliche **Rückerhalt** (tatsächliche Sachherrschaft und Untersuchungsmöglichkeit) und eine Hemmung nach § 203 BGB bleiben juristische Eingaben.

```bash
# § 548 Abs. 1 BGB: Rückerhalt der Wohnung am 31.03.2026
python -m scripts.legal_calc.cli frist --ereignis 31.03.2026 --menge 6 --einheit monate

# Monatsende-Überlauf (§ 188 Abs. 3 BGB): Rückerhalt am 31.08.2026
python -m scripts.legal_calc.cli frist --ereignis 31.08.2026 --menge 6 --einheit monate

# § 548 Abs. 2 BGB: Ansprüche des Mieters ab Beendigung des Mietverhältnisses
python -m scripts.legal_calc.cli frist --ereignis 31.03.2026 --menge 6 --einheit monate
```

`--json` liefert die Rechenschritte samt Normzitat. Das Ergebnis ist ein **Rechenergebnis**, kein Rechtsrat: Ob überhaupt Rückerhalt vorlag (Schlüsselübergabe an einen Boten genügt regelmäßig nicht) und ob Verhandlungen die Frist gehemmt haben, entscheidet die rechtliche Würdigung.

## Quellen

### Statute

- [§ 535 BGB](https://www.gesetze-im-internet.de/bgb/__535.html), [§ 538 BGB](https://www.gesetze-im-internet.de/bgb/__538.html), [§ 539 BGB](https://www.gesetze-im-internet.de/bgb/__539.html), [§ 546 BGB](https://www.gesetze-im-internet.de/bgb/__546.html), [§ 548 BGB](https://www.gesetze-im-internet.de/bgb/__548.html), [§ 552 BGB](https://www.gesetze-im-internet.de/bgb/__552.html)
- [§ 280 BGB](https://www.gesetze-im-internet.de/bgb/__280.html), [§ 281 BGB](https://www.gesetze-im-internet.de/bgb/__281.html), [§ 215 BGB](https://www.gesetze-im-internet.de/bgb/__215.html), [§ 203 BGB](https://www.gesetze-im-internet.de/bgb/__203.html)
- [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html), [§ 309 BGB](https://www.gesetze-im-internet.de/bgb/__309.html) (AGB-Inhaltskontrolle)
- [§ 187 BGB](https://www.gesetze-im-internet.de/bgb/__187.html), [§ 188 BGB](https://www.gesetze-im-internet.de/bgb/__188.html)

### Kommentare

- Langenberg, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 538 BGB Rn. 1 ff. (Schönheitsreparaturen)
- Bieber, in: MüKoBGB, 9. Aufl. 2023, § 535 Rn. 1 ff.; § 548 Rn. 1 ff.
- Weidenkaff, in: Grüneberg, BGB, 84. Aufl. 2025, § 535 Rn. 1 ff.; § 548 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 18.03.2015 – VIII ZR 185/14 (formularmäßige Überwälzung bei unrenoviert überlassener Wohnung ohne angemessenen Ausgleich unwirksam) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2015-03-18&Aktenzeichen=VIII%20ZR%20185/14
- BGH, Urt. v. 08.07.2020 – VIII ZR 163/18 und VIII ZR 270/18 (Anspruch des Mieters einer unrenoviert überlassenen Wohnung auf Durchführung von Schönheitsreparaturen; hälftige Kostenbeteiligung) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2020-07-08&Aktenzeichen=VIII%20ZR%20163/18
- Zur Unwirksamkeit starrer Fristenpläne und von Quotenabgeltungsklauseln ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.

## Formulierungshilfe — Zurückweisung einer Renovierungsforderung

```
Sehr geehrte Damen und Herren,

Ihre Forderung vom <Datum> auf Zahlung von <Betrag> EUR für angeblich
unterlassene Schönheitsreparaturen weise ich zurück.

1. Die Wohnung wurde mir am <Datum> unrenoviert übergeben. Das
   Übergabeprotokoll weist <Beschreibung: vergilbte Tapeten in allen
   Räumen, Laufspuren> aus. Ein angemessener Ausgleich für die Übernahme
   in diesem Zustand wurde mir nicht gewährt. Die formularvertragliche
   Abwälzung der Schönheitsreparaturen in § <…> des Mietvertrags ist daher
   unwirksam; es bleibt bei der Erhaltungspflicht des Vermieters nach
   § 535 Abs. 1 S. 2 BGB.

2. Unabhängig davon enthält § <…> des Mietvertrags einen starren
   Fristenplan ("spätestens nach drei Jahren"). Auch dies führt zur
   Unwirksamkeit; eine geltungserhaltende Reduktion findet nicht statt.

3. Die von Ihnen beanstandeten Gebrauchsspuren sind vertragsgemäße
   Abnutzung im Sinne des § 538 BGB und nicht zu vertreten.

4. Die Wohnung wurde Ihnen am <Datum> zurückgegeben. Etwaige Ansprüche
   wegen Veränderungen oder Verschlechterungen der Mietsache verjähren
   gemäß § 548 Abs. 1 BGB sechs Monate nach Rückerhalt, mithin mit Ablauf
   des <Datum>. Auf die Einrede der Verjährung berufe ich mich
   ausdrücklich.

Ich fordere Sie auf, die Kaution nebst Zinsen bis zum <Datum>
abzurechnen und auszuzahlen.

Mit freundlichen Grüßen
```

## Ausgabeformat

```
SCHÖNHEITSREPARATUREN / RÜCKGABE — Prüfung — <Mandat-ID> — <Datum>

I.    Verjährung (§ 548 BGB) — ZUERST
      Rückerhalt am                      <Datum>
      Fristende                          <Datum>   [offen / abgelaufen ✅ Einrede]
      Hemmung § 203 BGB                  [keine / Verhandlungen von–bis]
II.   Zustand bei Übergabe               [renoviert / unrenoviert / renovierungsbedürftig]
      Angemessener Ausgleich gewährt     [ja / nein]
III.  Klauselprüfung (§§ 307 ff. BGB)
      - Abwälzung Schönheitsreparaturen  [wirksam / unwirksam]
      - Starrer Fristenplan              [N/A / unwirksam]
      - Endrenovierungsklausel           [N/A / unwirksam]
      - Quotenabgeltungsklausel          [N/A / unwirksam]
      - Farbwahl- / Fachhandwerkerklausel [N/A / unwirksam]
      Summierungseffekt                  [nein / ja]
      Folge                              [Mieterpflicht / § 535 Abs. 1 S. 2 BGB lebt auf]
IV.   Kostenteilung bei Unwirksamkeit    Anspruch des Mieters auf Durchführung
                                         Eigenanteil: <ca. 50 % / angepasst>
V.    Rückgabezustand
      - Vertragsgemäße Abnutzung (§ 538) <Aufzählung>
      - Schäden                          <Aufzählung> → <Betrag>
      - Protokoll / Fotos                [vorhanden / fehlt ⚠️]
VI.   Rückbau (§ 539 Abs. 2, § 552)      <Einbauten>  [Rückbau geschuldet / Verzicht /
                                          Wegnahmerecht / Entschädigung]
VII.  Schadensersatz (§§ 280, 281)       Fristsetzung: [erfolgt / entbehrlich / fehlt ❌]
                                         Betrag: <…>  [Kostenvoranschlag / Mietausfall]
VIII. Abwicklung über Kaution            Aufrechnung [zulässig / § 215 BGB / gesperrt]

Ergebnis: <Forderung begründet / teilweise / unbegründet>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Verjährung § 548 BGB übersehen** — sechs Monate ab Rückerhalt, nicht ab Mietende; die Frist ist der schärfste Fallstrick der Rückgabeabwicklung und lässt sich nicht durch AGB verlängern. Auf Mieterseite muss die Einrede ausdrücklich erhoben werden.
- **Klausel für teilwirksam gehalten** — es gibt keine geltungserhaltende Reduktion; eine unwirksame Klausel entfällt vollständig und § 535 Abs. 1 S. 2 BGB lebt auf.
- **Unrenovierte Übergabe nicht dokumentiert** — ohne Übergabeprotokoll trägt der Mieter das Beweisrisiko für den Zustand bei Einzug.
- **Hälftige Kostenteilung übersehen** — der Mieter, der bei unwirksamer Klausel Renovierung verlangt, muss sich regelmäßig zur Hälfte an den Kosten beteiligen.
- **Vertragsgemäße Abnutzung als Schaden abgerechnet** — § 538 BGB schließt den Ersatz aus.
- **Fristsetzung nach § 281 BGB versäumt** — ohne Fristsetzung oder anerkannten Entbehrlichkeitsgrund kein Schadensersatz statt der Leistung.
- **Renovierungskosten und Mietausfall kumuliert** — beides nebeneinander ist nicht ersatzfähig.
- **Rückbaupflicht bei genehmigten Einbauten nicht geregelt** — Zustimmungen ohne Rückbauklausel führen regelmäßig zum Streit über den Verzicht.
