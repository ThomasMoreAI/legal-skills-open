---
name: esrs-berichtspflicht-borghei
title: /csrd:esrs-berichtspflicht
description: Bestimmung der Nachhaltigkeitsberichtspflicht nach CSRD-RL (EU) 2022/2464 und ihrer HGB-Umsetzung – wer ab welchem Geschäftsjahr nach welchen ESRS-Standards berichtet (Anwendungsbereich, Größenkriterien, Konzernebene, Zeitplan). Use when geklärt werden muss, ob und ab wann ein Unternehmen einen Nachhaltigkeitsbericht erstellen muss und welchen Inhalt dieser hat.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/csrd/skills/esrs-berichtspflicht
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: de
---

# /csrd:esrs-berichtspflicht

## Zweck

Diese Skill klärt die Eingangsfrage jeder CSRD-Beratung: **Ist das Unternehmen berichtspflichtig, ab wann, und welchen Inhalt schuldet es?** Die Pflicht folgt aus der **RL (EU) 2022/2464** (CSRD) und ihrer Umsetzung in das HGB (Nachhaltigkeitsangaben im Lagebericht). Anwendungsbereich und Zeitplan sind seit dem EU-Omnibus-Verfahren stark in Bewegung — eine falsche Einordnung führt entweder zu unnötigem Aufwand oder zu einer Pflichtverletzung mit Prüfungs- und Haftungsfolgen.

> **⚠️ Aktualität (Stand 2026-07) — Anwendungsbereich massiv verengt, Schwellenprüfung neu durchführen:** Das **Omnibus-I-Paket** ist geltendes Recht. Die **Änderungsrichtlinie (EU) 2026/470** wurde am **26.02.2026** im Amtsblatt veröffentlicht und ist am **18.03.2026** in Kraft getreten. Sie **ersetzt** die frühere „Stop-the-Clock"-RL (EU) 2025/794.
>
> | Punkt | Stand nach Omnibus I |
> |---|---|
> | **CSRD-Schwelle** | **> 1.000 Beschäftigte UND > 450 Mio. EUR Nettoumsatz** (kumulativ) |
> | Vorschlag des EP (1.750 Beschäftigte) | **abgelehnt** — nicht Gesetz geworden |
> | **Umsetzungsfrist** | **19.03.2027** |
> | Drittstaatenunternehmen | Mutter **> 450 Mio. EUR** EU-Umsatz; Tochter/Zweigniederlassung **> 200 Mio. EUR** |
> | Wave-1-Unternehmen unter der neuen Schwelle | **für GJ 2025 und GJ 2026 nicht berichtspflichtig** (vorbehaltlich nationaler Umsetzung) |
> | ESRS-Überarbeitung | **läuft noch** — Inhalte im Fluss `[unverifiziert - prüfen]` |
> | Wertschöpfungsketten-Cap | Unternehmen dürfen Datenanfragen an kleinere Geschäftspartner ablehnen, soweit sie die gesetzliche Obergrenze überschreiten |
>
> **Wichtigste Beratungsaufgabe ist jetzt die erneute Schwellenprüfung.** Ein erheblicher Teil der bisherigen Berichtspflichtigen — insbesondere Wave-1-Unternehmen, die für das **Geschäftsjahr 2024 bereits berichtet haben** — fällt aus dem Anwendungsbereich heraus. Die Betroffenheit ist deshalb **nicht** aus der bisherigen Berichtspraxis, aus der Wellenzuordnung oder aus der alten NFRD-Schwelle (500 Beschäftigte) abzuleiten, sondern **neu und kumulativ** an > 1.000 Beschäftigten **und** > 450 Mio. EUR zu messen.
>
> **Deutschland hat die CSRD bislang nicht umgesetzt** (Regierungsentwurf eines CSRD-Umsetzungsgesetzes vom 03.09.2025, Anhörung im Rechtsausschuss 13.04.2026). Bis zur Umsetzung gilt für das nationale Recht weiter das NFRD-Regime der §§ 289b ff. HGB. Der Stand des deutschen Verfahrens ist `[unverifiziert - prüfen]`.

## Eingaben

- Rechtsform, Kapitalmarktorientierung
- Beschäftigtenzahl (Jahresdurchschnitt), Bilanzsumme, Nettoumsatz — Einzel- und Konzernebene
- Konzernstruktur (Mutter-/Tochterunternehmen, Befreiungstatbestände)
- Bisherige Berichtspraxis (NFRD-Erklärung, freiwilliger Bericht)
- Geschäftsjahr (kalender- oder abweichend)

## Sub-Agent-Architektur

Die Bearbeitung folgt einer Kette spezialisierter Rollen. Ein **Scoping-Agent** prüft den Anwendungsbereich und die Größenkriterien auf Einzel- und Konzernebene und ermittelt das maßgebliche Erstanwendungs-Geschäftsjahr. Ein **Inhalts-Agent** leitet aus der Wesentlichkeitsanalyse die zu berichtenden ESRS-Datenpunkte ab und ordnet sie den §§ 289b–289e HGB (bzw. künftig den neuen HGB-Vorschriften) zu. Ein **Konzern-Agent** prüft Befreiungs- und Einbeziehungstatbestände nach § 315b HGB. Ein **Verifikations-Agent** gleicht jede Schwellenwert- und Datumsangabe gegen EUR-Lex und den aktuellen Gesetzesstand ab und markiert Unsicheres mit `[unverifiziert - prüfen]`.

## Ablauf

### 1. Anwendungsbereich und Größenkriterien — Schwellenprüfung neu durchführen

**Dies ist der erste und wichtigste Schritt.** Die Schwellen sind durch die Änderungs-RL (EU) 2026/470 angehoben worden; jede Betroffenheitsaussage aus der Zeit vor dem 18.03.2026 ist neu zu erheben.

- **Kumulative Prüfung:** **> 1.000 Beschäftigte (Jahresdurchschnitt) UND > 450 Mio. EUR Nettoumsatz**. Beide Kriterien müssen erfüllt sein; ein Unternehmen mit 1.100 Beschäftigten und 400 Mio. EUR Umsatz ist **nicht** berichtspflichtig.
- Die vom Europäischen Parlament diskutierte Schwelle von **1.750 Beschäftigten wurde abgelehnt** und ist nicht anzuwenden.
- **Drittstaatenunternehmen:** Mutterunternehmen **> 450 Mio. EUR** EU-Nettoumsatz; Tochterunternehmen oder Zweigniederlassung **> 200 Mio. EUR**.
- **Wave-1-Rückfall:** Unternehmen, die für das **Geschäftsjahr 2024** bereits nach CSRD berichtet haben, aber die neuen Schwellen nicht erreichen, sind für die **Geschäftsjahre 2025 und 2026 nicht berichtspflichtig** — vorbehaltlich der nationalen Umsetzung. Eine freiwillige Fortführung ist möglich, aber als solche zu kennzeichnen.
- **Wellendenken aufgeben:** Die alte Einteilung in Wave 1 / Wave 2 / Wave 3 taugt nicht mehr als Betroffenheitsmaßstab. Maßgeblich ist allein der aktuelle Schwellentest.
- **Umsetzungsfrist** der Änderungs-RL: **19.03.2027**.
- Übergang vom NFRD-Regime: Solange Deutschland die CSRD nicht umgesetzt hat, gelten national weiterhin die **nichtfinanzielle Erklärung** nach **§ 289b HGB** / **§ 315b HGB** für große kapitalmarktorientierte Unternehmen sowie Kredit- und Versicherungsinstitute mit mehr als 500 Beschäftigten.
- Ergebnis und maßgebliches Geschäftsjahr mit Datum und Datengrundlage festhalten.

### 2. Nichtfinanzielle Erklärung / Nachhaltigkeitsbericht (§ 289b HGB)

- **§ 289b HGB** verankert die Pflicht zur (nichtfinanziellen) Erklärung bzw. zum Nachhaltigkeitsbericht im **Lagebericht**.
- Ort: gesonderter Abschnitt des Lageberichts (CSRD verlangt Integration in den Lagebericht, nicht mehr den gesonderten Bericht der NFRD).
- Befreiung der Tochter bei Einbezug in einen Konzernbericht.

### 3. Inhalt der Berichterstattung (§ 289c HGB)

- **§ 289c HGB** bestimmt die inhaltlichen Mindestangaben (Umwelt-, Arbeitnehmer-, Sozialbelange, Achtung der Menschenrechte, Korruptionsbekämpfung).
- Unter der CSRD treten die **ESRS-Standards** an die Stelle der freien Rahmenwahl: **ESRS 1** (allgemeine Anforderungen) und ESRS 2 (allgemeine Angaben) sind verpflichtend, die themenbezogenen Standards E1–E5 / S1–S4 / G1 nach Maßgabe der Wesentlichkeitsanalyse.
- **Die ESRS-Überarbeitung im Rahmen von Omnibus I ist noch nicht abgeschlossen.** Zahl und Zuschnitt der Datenpunkte werden voraussichtlich deutlich reduziert. Datenpunkt-Listen sind daher nur unter dem Vorbehalt `[unverifiziert - prüfen]` zu verwenden; von einer frühzeitigen Vollimplementierung des ESRS-Set-1-Datenkatalogs ist derzeit abzuraten.
- **Wertschöpfungsketten-Cap:** Berichtspflichtige dürfen von kleineren Geschäftspartnern nur Daten bis zur gesetzlichen Obergrenze verlangen; umgekehrt dürfen kleinere Unternehmen darüber hinausgehende Anfragen zurückweisen. Datenanforderungsprozesse und Lieferantenfragebögen sind entsprechend zu begrenzen.

### 4. Konzernebene (§ 315b HGB)

- **§ 315b HGB** regelt die **Konzern**-Nachhaltigkeitsberichterstattung im Konzernlagebericht.
- Befreiungstatbestände für Tochterunternehmen prüfen (Einbezug in den Konzernbericht der Mutter, auch Drittstaaten-Mutter mit gleichwertigem Bericht).

### 5. ESRS-Datenpunkte und Anhang

- Pflicht- und wesentlichkeitsabhängige Datenpunkte aus den **ESRS** ableiten.
- Digitales Format (XHTML/iXBRL-Tagging) und maschinenlesbare Auszeichnung berücksichtigen.

### 6. Prüfung und Zeitplan

- **Limited assurance** durch unabhängige Prüfer ab Erstanwendung; spätere Anhebung diskutiert.
- Zeitplan und Schwellenwerte abschließend mit dem Stand des CSRD-Umsetzungsgesetzes abgleichen.

## Risiken / typische Fehler

- **Mandant plant gegen aufgehobenes Recht** — Beratung auf Basis der alten CSRD-Wellen und -Schwellen. Der **Omnibus**-Prozess ist abgeschlossen: seit dem 18.03.2026 gilt die Änderungs-RL (EU) 2026/470 mit **> 1.000 Beschäftigten UND > 450 Mio. EUR**. Wer noch nach Wave 1/2/3 berät, erzeugt Berichtspflichten, die es nicht gibt.
- **Schwellenprüfung nicht neu durchgeführt** — der häufigste und teuerste Fehler. Die Betroffenheit wird aus der bisherigen Berichtspraxis fortgeschrieben, statt neu gemessen zu werden; dadurch berichtet ein Unternehmen freiwillig mit vollem Prüfungs- und Haftungsrisiko.
- **Kriterien alternativ statt kumulativ geprüft** — Beschäftigtenzahl **und** Nettoumsatz müssen beide überschritten sein.
- **1.750-Schwelle verwendet** — die Parlamentsposition wurde **abgelehnt**; maßgeblich sind 1.000 Beschäftigte.
- **Wave-1-Rückfall übersehen** — Unternehmen, die für GJ 2024 berichtet haben und nun unter der Schwelle liegen, sind für **GJ 2025 und GJ 2026** nicht berichtspflichtig; unnötiger Aufwand und unnötige Prüfungskosten.
- **Drittstaaten-Schwellen verwechselt** — 450 Mio. EUR für die Mutter, **200 Mio. EUR** für Tochter/Zweigniederlassung.
- **ESRS-Katalog als final behandelt** — die ESRS-Überarbeitung läuft noch; Vollimplementierung des alten Datenkatalogs ist verfrüht `[unverifiziert - prüfen]`.
- **Konzernebene übersehen** — Befreiung auf **Konzernebene** nach § 315b HGB nicht geprüft, dadurch Doppelberichterstattung oder Lücke.
- **NFRD/CSRD-Übergang verwechselt** — für das Geschäftsjahr 2025 gilt in Deutschland noch das NFRD-Regime, nicht die ESRS.
- **Wesentlichkeit nicht vorgeschaltet** — ESRS-Datenpunkte ohne doppelte Wesentlichkeitsanalyse (siehe `/csrd:wesentlichkeitsanalyse-doppelt`) ausgewählt.
- **Erstanwendungstermin geschätzt** — Datum ohne Quelle angegeben statt mit `[unverifiziert - prüfen]` gekennzeichnet.

## Quellen

### EU-Rechtsakte

- [RL (EU) 2022/2464 (CSRD)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2464)
- [Delegierte VO (EU) 2023/2772 (ESRS Set 1)](https://eur-lex.europa.eu/eli/reg_del/2023/2772/oj)
- **Änderungs-RL (EU) 2026/470 (Omnibus I)** — Amtsblatt 26.02.2026, in Kraft 18.03.2026, Umsetzungsfrist 19.03.2027; ersetzt die Stop-the-Clock-RL (EU) 2025/794. ELI-Fundstelle `[unverifiziert - prüfen]`
- [Stop-the-Clock-RL (EU) 2025/794](https://eur-lex.europa.eu/eli/dir/2025/794/oj) — durch RL (EU) 2026/470 überholt, nur noch historisch

### Deutsches Recht

- [§ 289b HGB](https://www.gesetze-im-internet.de/hgb/__289b.html), [§ 289c HGB](https://www.gesetze-im-internet.de/hgb/__289c.html), [§ 315b HGB](https://www.gesetze-im-internet.de/hgb/__315b.html)
- CSRD-Umsetzungsgesetz (Regierungsentwurf 03.09.2025) — im Verfahren, `[unverifiziert - prüfen]`

## Ausgabeformat

```
ESRS-BERICHTSPFLICHT — <Unternehmen> — <Geschäftsjahr>

I.    Schwellenprüfung NEU (RL (EU) 2026/470, in Kraft 18.03.2026)
      Beschäftigte (Jahresdurchschnitt): <…>   > 1.000?  [Ja / Nein]
      Nettoumsatz:                       <…>   > 450 Mio. EUR? [Ja / Nein]
      Kumulativ erfüllt: [Ja / Nein]
      Drittstaatenbezug: Mutter > 450 Mio. / Tochter o. Zweigndl. > 200 Mio.: <…>
      Vorbefund (bisherige Berichtspraxis / Welle): <…> — NICHT maßgeblich
II.   Erstanwendung
      Maßgebliches Geschäftsjahr: <…>
      Wave-1-Rückfall (GJ 2024 berichtet, jetzt unter Schwelle → GJ 2025/2026 raus): [Ja / Nein]
      Übergang NFRD → CSRD: <…>   Umsetzungsfrist DE: 19.03.2027
III.  Berichtsort (§ 289b HGB)
      Lagebericht / Konzernlagebericht: <…>
IV.   Inhalt (§ 289c HGB / ESRS)
      Pflicht: ESRS 1, ESRS 2
      Wesentlich: <E…/S…/G…>
V.    Konzernebene (§ 315b HGB)
      Befreiung Tochter: [Ja / Nein]
VI.   Prüfung
      limited assurance: <Prüfer / Umfang>
VII.  Offene Punkte / tagesaktuell zu prüfen
      <… [unverifiziert - prüfen]>

Restrisiko: <…>
Wiedervorlage: vor Aufstellung des Lageberichts
```
