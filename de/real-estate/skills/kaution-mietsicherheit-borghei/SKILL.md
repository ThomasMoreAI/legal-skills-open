---
name: kaution-mietsicherheit-borghei
title: /mietrecht:kaution-mietsicherheit
description: Mietsicherheit im Wohnraummietrecht – Höchstbetrag von drei Nettokaltmieten und Ratenzahlungsrecht § 551 Abs. 1, Abs. 2 BGB, insolvenzfeste Anlagepflicht getrennt vom Vermietervermögen § 551 Abs. 3 BGB, Unwirksamkeit abweichender Vereinbarungen § 551 Abs. 4 BGB, Kündigung wegen Kautionsverzugs § 569 Abs. 2a BGB, Abrechnung und Zurückbehaltung nach Rückgabe, Verwertung und Aufrechnung, Verjährung § 548 BGB. Use when eine Kaution vereinbart, angelegt, verwertet oder nach Mietende abgerechnet und zurückgefordert wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/mietrecht/skills/kaution-mietsicherheit
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /mietrecht:kaution-mietsicherheit

## Zweck

Die Kaution ist wirtschaftlich klein und rechtlich scharf reguliert: Jede Abweichung zulasten des Mieters ist nach § 551 Abs. 4 BGB unwirksam. Die beiden Streitpunkte der Praxis sind die **Anlagepflicht** — sie macht die Kaution insolvenzfest und gibt dem Mieter ein Zurückbehaltungsrecht an der Miete — und die **Abrechnung nach Rückgabe**, für die das Gesetz gerade keine feste Frist nennt. Diese Skill führt beides sauber durch und verzahnt es mit der kurzen Verjährung des § 548 BGB.

## Eingaben

- **Kautionsvereinbarung**: Höhe, Form (Barkaution, Bürgschaft, Verpfändung, Sparbuch), Fälligkeit
- **Nettokaltmiete** bei Vertragsschluss (Bezugsgröße für den Höchstbetrag)
- **Zahlungsverlauf** der Kaution (Raten, Termine)
- **Anlagenachweis**: Konto, Trennung vom Vermietervermögen, Zinsgutschriften
- **Rückgabedatum** der Mietsache und Rückgabeprotokoll
- Offene Forderungen des Vermieters: Mietrückstand, Betriebskostennachzahlung, Schadensersatz
- Ob der Vermieter **gewechselt** hat oder Zwangsverwaltung bzw. Insolvenz eingetreten ist

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention). Ein **Vereinbarungs-Prüfer** kontrolliert Höhe, Form und Ratenrecht und verwirft nach § 551 Abs. 4 BGB unwirksame Klauseln. Ein **Anlage-Prüfer** untersucht die getrennte Anlage und die daraus folgenden Rechte des Mieters. Ein **Abrechnungs-Prüfer** bestimmt Zeitpunkt und Umfang der Rückzahlung sowie den Umfang zulässiger Zurückbehaltung. Ein **Verwertungs-Prüfer** klärt, gegen welche Forderungen aufgerechnet werden darf. Ein **Verjährungs-Prüfer** spiegelt alle Vermieterforderungen gegen die Sechsmonatsfrist des § 548 BGB.

## Ablauf

### 1. Höchstbetrag und Ratenzahlung ([§ 551 Abs. 1, Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__551.html))

Hat der Mieter Sicherheit zu leisten, darf diese **das Dreifache der auf einen Monat entfallenden Miete ohne Betriebskosten** — also drei **Nettokaltmieten** — nicht übersteigen. Eine höhere Vereinbarung ist in Höhe des Überschusses unwirksam; der Mehrbetrag ist zurückzuzahlen. Der Mieter ist zu **drei gleichen monatlichen Teilzahlungen** berechtigt; die erste Rate ist zu Beginn des Mietverhältnisses fällig, die weiteren mit den folgenden Mietzahlungen. Eine Klausel, die die Kaution vollständig vorab verlangt, ist nach Abs. 4 unwirksam. Der Höchstbetrag gilt für **alle** Sicherheiten zusammen — eine zusätzliche Bürgschaft neben drei Nettokaltmieten ist grundsätzlich unzulässig; anders bei einer vom Dritten **freiwillig und unaufgefordert** angebotenen Bürgschaft.

### 2. Anlagepflicht und Insolvenzfestigkeit ([§ 551 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__551.html))

Der Vermieter hat eine ihm als Sicherheit überlassene Geldsumme bei einem Kreditinstitut zu dem für **Spareinlagen mit dreimonatiger Kündigungsfrist üblichen Zinssatz** anzulegen. Die Parteien können eine andere Anlageform vereinbaren; in beiden Fällen muss die Anlage **vom Vermögen des Vermieters getrennt** erfolgen. Die **Erträge stehen dem Mieter zu** und erhöhen die Sicherheit.

Die Trennungspflicht ist der Kern: Sie macht die Kaution **insolvenzfest** — in der Insolvenz des Vermieters steht dem Mieter ein Aussonderungsrecht zu, in der Zwangsvollstreckung ein Widerspruchsrecht. Verletzt der Vermieter die Anlagepflicht, kann der Mieter Anlage verlangen und die **Miete bis zur Höhe der Kaution zurückbehalten** ([§ 273 BGB](https://www.gesetze-im-internet.de/bgb/__273.html)); ferner kommt Schadensersatz in Betracht. Zur Herausgabepflicht des **Zwangsverwalters** auch bei nicht weitergeleiteter Kaution: BGH, Urt. v. 09.03.2005 – VIII ZR 330/03, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2005-03-09&Aktenzeichen=VIII%20ZR%20330/03.

### 3. Formen der Mietsicherheit

- **Barkaution** — Regelfall; unterliegt vollständig § 551 Abs. 3 BGB.
- **Verpfändetes Sparbuch** — auf den Namen des Mieters, verpfändet an den Vermieter; erfüllt die Trennung von Haus aus.
- **Bürgschaft** (Bank oder Privatperson) — ersetzt die Barkaution; die Anlagepflicht entfällt, der Höchstbetrag gilt fort. Auf Verzicht auf die Einrede der Vorausklage achten.
- **Verpfändung von Wertpapieren / Kautionsversicherung** — nur bei ausdrücklicher Vereinbarung.

Abweichende Vereinbarungen zum Nachteil des Mieters sind nach **§ 551 Abs. 4 BGB unwirksam**.

### 4. Kautionsverzug und Kündigung ([§ 569 Abs. 2a BGB](https://www.gesetze-im-internet.de/bgb/__569.html))

Ein **wichtiger Grund** im Sinne des § 543 Abs. 1 BGB liegt auch vor, wenn der Mieter mit einer Sicherheitsleistung nach § 551 BGB in Höhe eines Betrages in Verzug ist, der der **zweifachen Monatsmiete** entspricht. Die Kündigung ist ausgeschlossen, wenn die Sicherheit vor Zugang der Kündigung geleistet wird. Eine Abmahnung ist nach § 569 Abs. 2a S. 2 BGB entbehrlich. Vertiefung: `/mietrecht:fristlose-kuendigung-543`.

### 5. Verwertung während des Mietverhältnisses

Der Vermieter darf sich aus der Kaution **während** des laufenden Mietverhältnisses grundsätzlich **nicht** befriedigen — die Sicherheit dient der Absicherung am Ende. Ausnahme: rechtskräftig festgestellte oder unstreitige Forderungen. Greift der Vermieter unberechtigt zu, kann der Mieter Wiederauffüllung verlangen. Umgekehrt darf der **Mieter nicht** die letzten Mieten „abwohnen", indem er sie mit der Kaution verrechnet — das begründet Zahlungsverzug und Kündigungsrisiko.

### 6. Abrechnung nach Rückgabe

Nach Beendigung und Rückgabe der Mietsache ist die Kaution **abzurechnen und der Überschuss auszuzahlen**. Das Gesetz nennt **keine** feste Frist; dem Vermieter steht eine angemessene **Überlegungs- und Prüfungsfrist** zu, die je nach Umfang der Abwicklung regelmäßig mit **drei bis sechs Monaten** angesetzt wird. Der Anspruch des Mieters auf Rückzahlung wird erst mit Ablauf dieser Frist **fällig**. Der Vermieter darf einen Teil der Kaution **zurückbehalten**, soweit noch nicht abgerechnete **Betriebskosten** zu erwarten sind — der Einbehalt muss der Höhe nach an der zu erwartenden Nachforderung orientiert und darf nicht pauschal sein. Nach Erteilung der Abrechnung ist der Einbehalt unverzüglich abzuwickeln.

### 7. Aufrechnung und Verjährung ([§ 548 BGB](https://www.gesetze-im-internet.de/bgb/__548.html))

Der Vermieter kann mit fälligen Gegenforderungen gegen den Rückzahlungsanspruch **aufrechnen**: Mietrückstand, Nutzungsentschädigung nach § 546a BGB, Betriebskostennachforderung, Schadensersatz wegen Verschlechterung der Mietsache. Für **Ersatzansprüche wegen Veränderungen oder Verschlechterungen** gilt die **sechsmonatige Verjährung** des § 548 Abs. 1 BGB ab **Rückerhalt** der Mietsache. Die Aufrechnung mit einer bereits verjährten Forderung ist nach § 215 BGB zulässig, wenn sich die Forderungen zu einem Zeitpunkt aufrechenbar gegenüberstanden, in dem die Forderung noch nicht verjährt war. Der Rückzahlungsanspruch des Mieters verjährt regelmäßig nach §§ 195, 199 BGB in drei Jahren. Vertiefung zur Rückgabeabwicklung: `/mietrecht:schoenheitsreparaturen-rueckgabe`.

### 8. Vermieterwechsel ([§ 566a BGB](https://www.gesetze-im-internet.de/bgb/__566a.html))

Wird das vermietete Wohnraumgrundstück veräußert, tritt der **Erwerber** in die Rechte und Pflichten aus der Sicherheit ein. Er haftet dem Mieter auf Rückgewähr auch dann, wenn ihm die Kaution nicht ausgehändigt wurde; der Veräußerer haftet **subsidiär** fort (§ 566a S. 2 BGB). Der Mieter sollte den Erwerber daher stets in Anspruch nehmen und den Veräußerer hilfsweise in Anspruch behalten.

## Quellen

### Statute

- [§ 551 BGB](https://www.gesetze-im-internet.de/bgb/__551.html), [§ 566a BGB](https://www.gesetze-im-internet.de/bgb/__566a.html), [§ 569 BGB](https://www.gesetze-im-internet.de/bgb/__569.html)
- [§ 548 BGB](https://www.gesetze-im-internet.de/bgb/__548.html), [§ 546a BGB](https://www.gesetze-im-internet.de/bgb/__546a.html), [§ 215 BGB](https://www.gesetze-im-internet.de/bgb/__215.html), [§ 273 BGB](https://www.gesetze-im-internet.de/bgb/__273.html)
- [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html), [§ 556 BGB](https://www.gesetze-im-internet.de/bgb/__556.html) (Betriebskosteneinbehalt)

### Kommentare

- Blank, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 551 BGB Rn. 1 ff.
- Bieber, in: MüKoBGB, 9. Aufl. 2023, § 551 Rn. 1 ff.; § 566a Rn. 1 ff.
- Weidenkaff, in: Grüneberg, BGB, 84. Aufl. 2025, § 551 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 09.03.2005 – VIII ZR 330/03 (Herausgabepflicht des Zwangsverwalters auch bei nicht weitergeleiteter Kaution) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2005-03-09&Aktenzeichen=VIII%20ZR%20330/03
- Zur Länge der Abrechnungs- und Überlegungsfrist nach Rückgabe und zum zulässigen Betriebskosteneinbehalt ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.
- Zur Unzulässigkeit einer zusätzlichen Bürgschaft neben der Höchstkaution ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.

## Formulierungshilfe — Rückforderung der Kaution nach Mietende

```
Sehr geehrte Damen und Herren,

das Mietverhältnis über die Wohnung <Anschrift> endete am <Datum>. Die
Wohnung wurde am <Datum> übergeben; das Übergabeprotokoll liegt vor.

Ich habe zu Mietbeginn eine Barkaution in Höhe von <Betrag> EUR geleistet.
Seit der Rückgabe sind mehr als <…> Monate vergangen. Eine angemessene
Prüfungs- und Überlegungsfrist ist damit abgelaufen; der Anspruch auf
Rückzahlung ist fällig.

Ich fordere Sie auf, bis zum <Datum>

1. die Kaution nebst der nach § 551 Abs. 3 S. 3 BGB dem Mieter zustehenden
   Zinsen abzurechnen und den Überschuss auf das Konto <IBAN> zu zahlen,
2. den Anlagenachweis vorzulegen (getrennte Anlage vom Vermietervermögen,
   § 551 Abs. 3 S. 3 BGB).

Etwaige Ersatzansprüche wegen Veränderungen oder Verschlechterungen der
Mietsache sind gemäß § 548 Abs. 1 BGB sechs Monate nach Rückerhalt, also
mit Ablauf des <Datum>, verjährt.

Ein Einbehalt für noch nicht abgerechnete Betriebskosten ist allenfalls in
Höhe der konkret zu erwartenden Nachforderung zulässig und der Höhe nach
zu begründen.

Mit freundlichen Grüßen
```

## Ausgabeformat

```
MIETSICHERHEIT § 551 BGB — Prüfung — <Mandat-ID> — <Datum>

I.    Vereinbarung
      - Form                             [Barkaution / Bürgschaft / Sparbuch / …]
      - Höhe                             <Betrag>   Nettokaltmiete: <Betrag>
      - Höchstbetrag 3 Nettokaltmieten   [gewahrt / überschritten um <Betrag>]
      - Ratenzahlungsrecht (Abs. 2)      [gewahrt / Klausel unwirksam § 551 Abs. 4]
II.   Anlage (§ 551 Abs. 3)              [getrennt angelegt / nicht nachgewiesen ❌]
      Zinsen dem Mieter gutgeschrieben   [✅ / ❌ <Betrag>]
      Insolvenzfestigkeit                [gegeben / gefährdet]
      Zurückbehaltungsrecht § 273 BGB    [nein / ja bis <Betrag>]
III.  Kautionsverzug (§ 569 Abs. 2a)     [N/A / Kündigungsrisiko ab 2 Monatsmieten]
IV.   Rückgabe                           Datum: <…>   Protokoll: [ja / nein]
V.    Abrechnung nach Rückgabe           Prüfungsfrist Ende: <Datum>  [fällig / offen]
      Einbehalt Betriebskosten           <Betrag>  [begründet / pauschal ⚠️]
VI.   Gegenforderungen des Vermieters
      - Mietrückstand / § 546a           <Betrag>
      - Betriebskostennachforderung      <Betrag>
      - Schadensersatz Mietsache         <Betrag>
      Verjährung § 548 BGB Ende          <Datum>   [offen / verjährt]
      Aufrechnung § 215 BGB              [möglich / ausgeschlossen]
VII.  Vermieterwechsel (§ 566a)          [N/A / Erwerber haftet, Veräußerer subsidiär]
VIII. Auszahlungsbetrag                  <Betrag> nebst Zinsen

Ergebnis: <…>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Kaution nicht getrennt angelegt** — der Mieter kann Miete nach § 273 BGB zurückbehalten, die Insolvenzfestigkeit entfällt, Schadensersatz droht.
- **Höchstbetrag überschritten** — mehr als drei Nettokaltmieten oder zusätzliche Bürgschaft neben der Vollkaution; der Überschuss ist zurückzuzahlen.
- **Ratenzahlungsrecht ausgeschlossen** — die Klausel ist nach § 551 Abs. 4 BGB unwirksam, die Kaution bleibt aber geschuldet.
- **Kaution abgewohnt** — der Mieter, der die letzten Mieten mit der Kaution verrechnet, gerät in Zahlungsverzug und riskiert die fristlose Kündigung.
- **Verjährung § 548 BGB übersehen** — Ersatzansprüche wegen Verschlechterung verjähren sechs Monate nach Rückerhalt; danach hilft nur noch § 215 BGB.
- **Pauschaler Betriebskosteneinbehalt** — der Einbehalt muss sich an der konkret zu erwartenden Nachforderung orientieren.
- **Beim Vermieterwechsel den Falschen in Anspruch genommen** — nach § 566a BGB haftet primär der Erwerber, der Veräußerer nur subsidiär.
- **Rückzahlung zu früh gefordert** — vor Ablauf der angemessenen Prüfungsfrist ist der Anspruch nicht fällig; eine Klage wäre kostenpflichtig abzuweisen.
