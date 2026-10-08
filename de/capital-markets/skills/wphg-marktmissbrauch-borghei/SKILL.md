---
name: wphg-marktmissbrauch-borghei
title: /kapitalmarktrecht:wphg-marktmissbrauch
description: Prüfung von Insiderhandel und Marktmanipulation nach MAR (VO (EU) 596/2014) iVm WpHG – Insiderinformation Art. 7, Verbote Art. 14/15, Ausnahme Legitimate Behaviour Art. 9, Ad-hoc-Publizität Art. 17 (inkl. Selbstaufschub Abs. 4), Insiderliste Art. 18, Directors' Dealings Art. 19, Sanktionen Art. 30 MAR und §§ 38, 119 WpHG. Use when ein Emittent vor einer transaktions- oder informationsbedingten Marktmissbrauchsfrage steht (M&A, Restrukturierung, vorzeitige Bilanzdaten, Vorstandsgeschäfte).
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/kapitalmarktrecht/skills/wphg-marktmissbrauch
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: capital-markets
language: de
---

# /kapitalmarktrecht:wphg-marktmissbrauch

## Zweck

Der Skill prüft die zentralen Marktmissbrauchstatbestände nach der **Marktmissbrauchsverordnung (VO (EU) 596/2014 — MAR)**, insbesondere das Verbot des Insiderhandels (Art. 14 MAR), das Verbot der Marktmanipulation (Art. 15 MAR), die Ad-hoc-Publizitätspflicht (Art. 17 MAR) einschließlich des Selbstaufschubs nach Art. 17 IV, die Pflicht zur Insiderliste (Art. 18 MAR) und die Meldepflicht für Eigengeschäfte von Führungskräften (Directors' Dealings, Art. 19 MAR). Er klärt die Sanktionsfolgen nach Art. 30 MAR sowie §§ 119, 38 WpHG.

> **⚠️ Aktualität (Stand 2026-07): Art. 17 MAR ist durch das EU-Listing-Act-Paket materiell geändert.** Das Paket — **RL (EU) 2024/2811** und **VO (EU) 2024/2809** — galt gestuft; die **letzte Stufe ist am 05.06.2026 anwendbar geworden**.
>
> **Die tragende Änderung:** Bei einem **zeitlich gestreckten Vorgang** ist nur noch das **Endereignis** ad hoc zu veröffentlichen. **Zwischenschritte lösen keine Ad-hoc-Pflicht mehr aus.** Eine seit dem 05.06.2026 geltende **Delegierte Verordnung der Kommission** benennt **35 zeitlich gestreckte Vorgänge in 7 Kategorien** samt dem jeweils maßgeblichen Endereignis. Fundstelle der Delegierten Verordnung und der Katalog im Einzelnen `[unverifiziert - prüfen]`.
>
> **Damit ist die bisherige deutsche Praxis überholt.** Die auf EuGH *Geltl/Daimler* gestützte Zwischenschritt-Linie trägt die Ad-hoc-Pflicht **nicht mehr**. Sie bleibt allein für den **Insiderbegriff** des Art. 7 MAR und damit für Handelsverbot (Art. 14), Insiderliste (Art. 18) und Closed Periods relevant — die Entkopplung von Insiderinformation und Veröffentlichungspflicht ist der eigentliche Praxisumbruch.
>
> **Praktische Aufgabe im Mandat:** **Ad-hoc-Richtlinien und Insiderverzeichnis-Prozesse neu fassen; Ad-hoc-Gremien gegen die 35er-Liste neu schulen.**
>
> Weiter im Paket enthalten: ESG-Angaben im Prospekt, ein **verbindliches standardisiertes Prospektformat mit vorgegebener Reihenfolge**, Reduzierung der geprüften Historienabschlüsse auf **ein Jahr**, neue gesetzliche Prüfungs- und Billigungsfristen sowie angepasste Meldungen zu Eigengeschäften von Führungskräften und zu Rückkauf-/Stabilisierungsmaßnahmen.

## Eingaben

- Emittent (idR börsennotierte AG / SE) und ISIN / Handelsplatz (regulierter Markt iSv § 32 BörsG, Freiverkehr, MTF)
- konkrete Information / Vorhaben (M&A, Restrukturierung, Bilanzkennzahlen, Vorstandswechsel, behördliche Verfahren)
- Stand der Information (Verhandlungsstufe, Term Sheet, LOI, Vertragsschluss, Closing)
- bekannter Personenkreis (Vorstand, Aufsichtsrat, Berater) und ggf. bestehende Insiderliste
- Zweck der Anfrage: präventive Compliance-Beratung, Aufschub-Entscheidung, Reaktion auf BaFin-Verfahren, Verteidigung gegen Anlegerklagen

## Sub-Agent-Architektur

Researcher liefert MAR-Artikel in der seit dem 05.06.2026 geltenden Fassung, die Delegierte Verordnung mit dem Katalog der zeitlich gestreckten Vorgänge, WpHG-Sanktionsnormen, EuGH-Rspr. (Geltl/Daimler zur "präzisen Information" in mehrstufigen Prozessen — **nur noch für Art. 7 MAR**, Lafonta zur Kursrelevanz), BGH-Rspr. (IKB, EM.TV) und BaFin-Emittentenleitfaden. Drafter prüft im Gutachtenstil, entwirft ggf. Ad-hoc-Mitteilung und Aufschub-Dokumentation. Reviewer prüft, ob das maßgebliche **Endereignis** zutreffend bestimmt, der Aufschub Art. 17 IV dokumentiert und die Insiderliste angesprochen wurde.

## Ablauf

### 1. Anwendungsbereich (Art. 2 MAR)

MAR gilt für Finanzinstrumente, die zum Handel an einem geregelten Markt (Art. 4 I Nr. 21 MiFID II) zugelassen sind oder für die ein Antrag gestellt wurde, sowie für Finanzinstrumente, die an einem MTF/OTF gehandelt werden (Art. 2 I MAR). Bei reinem Freiverkehr außerhalb MTF (open market in engem Sinne) ist die Anwendung im Einzelfall zu prüfen.

### 2. Insiderinformation (Art. 7 MAR) – vier Kriterien

| Kriterium | Inhalt |
|---|---|
| **Präzise** | Konkreter Umstand, der eingetreten ist oder bei dem mit hinreichender Wahrscheinlichkeit angenommen werden kann, dass er eintreten wird (Art. 7 II MAR; EuGH, **Geltl/Daimler**, Rs. C-19/11 `[unverifiziert]`) |
| **Nicht öffentlich** | Information ist (noch) nicht der allgemeinen Anlegeröffentlichkeit zugänglich |
| **Direkter/indirekter Bezug** | Bezug zu einem oder mehreren Emittenten oder einem oder mehreren Finanzinstrumenten |
| **Kursrelevant** | Geeignet, im Falle des öffentlichen Bekanntwerdens den Kurs erheblich zu beeinflussen ("verständiger Anleger"-Maßstab; EuGH, **Lafonta**, Rs. C-628/13 `[unverifiziert]` — Richtungsangabe nicht erforderlich) |

**Zwischenschritte** in gestreckten Sachverhalten (Verhandlungsstadien einer M&A-Transaktion) können weiterhin **Insiderinformation** sein, wenn der einzelne Zwischenschritt selbst die vier Kriterien erfüllt (Geltl-Linie, Art. 7 III MAR).

> **Wichtig — Entkopplung seit 05.06.2026:** Die Zwischenschritt-Eigenschaft als Insiderinformation begründet **keine Ad-hoc-Pflicht mehr** (dazu Nr. 5). Ist der Zwischenschritt für sich genommen präzise und kursrelevant, löst er aber unverändert aus: **Handelsverbot** Art. 14, **Weitergabeverbot** Art. 10, **Insiderlisten-Pflicht** Art. 18 und faktische Handelsbeschränkungen für Führungskräfte. Wer aus dem Wegfall der Ad-hoc-Pflicht auf einen Wegfall der Insiderqualität schließt, begeht den zentralen Fehler der neuen Rechtslage.

### 3. Verbot des Insiderhandels (Art. 14 iVm Art. 8 MAR)

Verboten: (a) Erwerb/Veräußerung unter Verwendung von Insiderinformationen für eigene oder fremde Rechnung; (b) Empfehlung oder Verleitung Dritter; (c) unrechtmäßige Offenlegung (Art. 10 MAR).

**Legitimate Behaviour (Art. 9 MAR):** Bestimmte Verhaltensweisen sind ausdrücklich kein Insidergeschäft, namentlich Geschäfte aufgrund eines vor Erlangen der Insiderinformation gefassten und dokumentierten Plans (Art. 9 III) sowie der **klassische M&A-Erwerbsprozess** (Art. 9 IV: Geschäfte zur Durchführung einer übernahmebezogenen Akquisition, deren Insiderinformation gerade in der Übernahme selbst besteht — sog. Front Running im Rahmen der eigenen Übernahme bleibt erlaubt, soweit Art. 9 IV-Voraussetzungen vorliegen).

### 4. Verbot der Marktmanipulation (Art. 15 iVm Art. 12 MAR)

Drei Haupt-Tatbestände: handelsgestützte Manipulation (Art. 12 I lit. a, b), informationsgestützte Manipulation (Art. 12 I lit. c — falsche oder irreführende Signale), Manipulation durch Benchmarks (Art. 12 I lit. d). Praxis-Beispiele: pump-and-dump, wash trades, spoofing, gezielte Pressemitteilungen ohne sachliche Grundlage.

### 5. Ad-hoc-Publizitätspflicht (Art. 17 MAR)

- **Art. 17 I MAR:** Der Emittent gibt **unverzüglich** Insiderinformationen bekannt, die ihn unmittelbar betreffen. „Unverzüglich" = ohne schuldhaftes Zögern, in der BaFin-Praxis idR innerhalb von Stunden, in komplexen Sachverhalten enger Bearbeitungspuffer.

- **Zeitlich gestreckter Vorgang — nur das Endereignis (Fassung seit 05.06.2026):** Liegt ein gestreckter Vorgang vor, ist **allein das Endereignis** ad hoc zu veröffentlichen; die vorgelagerten Zwischenschritte sind **nicht** veröffentlichungspflichtig. Prüfschritte im Mandat:

  1. **Gestreckter Vorgang?** Abgleich mit dem Katalog der **35 Vorgänge in 7 Kategorien** der Delegierten Verordnung (in Kraft seit 05.06.2026) `[unverifiziert - prüfen]`.
  2. **Endereignis bestimmen.** Für die katalogisierten Vorgänge gibt die Delegierte Verordnung das maßgebliche Endereignis vor (bei M&A typischerweise die verbindliche Einigung/Signing statt bereits des Term Sheet) `[unverifiziert - prüfen]`.
  3. **Nicht katalogisierter Vorgang?** Das Endereignis ist nach der Systematik des Art. 17 MAR zu bestimmen; der Katalog ist der Auslegungsmaßstab. Im Zweifel dokumentierte Vorstandsentscheidung.
  4. **Vertraulichkeit bis zum Endereignis sichern** — Art. 17 IV UAbs. 1 lit. c gilt entsprechend; ein Leck vor dem Endereignis kann die Veröffentlichung vorziehen.

  **Folge für die Praxis:** Die Ad-hoc-Entscheidung verlagert sich von der laufenden Zwischenschritt-Bewertung auf die **einmalige, saubere Bestimmung des Endereignisses**. Ad-hoc-Richtlinien, Eskalationswege und Insiderverzeichnis-Prozesse sind entsprechend **neu zu fassen**; Ad-hoc-Gremien sind **gegen die 35er-Liste neu zu schulen**.
- **Art. 17 IV MAR (Selbstaufschub):** Aufschub auf eigene Verantwortung zulässig, wenn **kumulativ**:
  1. **Berechtigtes Interesse** des Emittenten (z. B. laufende Verhandlungen, deren Ergebnis durch sofortige Veröffentlichung gefährdet würde — ESMA Guidelines on Delay of Disclosure of Inside Information).
  2. **Aufschub voraussichtlich nicht geeignet, die Öffentlichkeit irrezuführen** (kein Widerspruch zu bereits veröffentlichten Aussagen).
  3. **Vertraulichkeit der Insiderinformation gewährleistet** (Insiderliste, Need-to-know-Verteiler).

  Nach der Veröffentlichung ist die BaFin nach Art. 17 IV UAbs. 3 MAR über den Aufschub und seine Gründe zu informieren.

- **Dokumentation des Aufschubs** ist zwingend (Art. 4 I DurchführungsVO (EU) 2016/1055): Zeitpunkt der Entstehung der Insiderinformation, Zeitpunkt der Aufschub-Entscheidung, verantwortliche Personen, laufende Vertraulichkeitskontrolle.

### 6. Insiderliste (Art. 18 MAR)

Emittent (und in dessen Auftrag handelnde Personen) führt eine Insiderliste mit allen Personen, die Zugang zu Insiderinformationen haben. Format nach DurchführungsVO (EU) 2016/347. Aktualisierung **unverzüglich** bei Personen- oder Statusänderung. Aufbewahrung mindestens 5 Jahre nach Erstellung/Aktualisierung.

### 7. Directors' Dealings (Art. 19 MAR)

Führungskräfte (Vorstand, Aufsichtsrat sowie ihnen "eng verbundene Personen" iSv Art. 3 I Nr. 26 MAR) melden Eigengeschäfte mit Aktien/Schuldverschreibungen des Emittenten oder darauf bezogenen Derivaten **innerhalb von 3 Geschäftstagen** an Emittent und BaFin (Art. 19 I MAR), sobald ein Schwellenwert von 5.000 EUR/Kalenderjahr überschritten ist (Art. 19 VIII MAR; angehoben durch nationale Option in der WpHG-Erleichterungsverordnung möglich). Veröffentlichung durch Emittent unverzüglich.

**Geschlossene Zeiträume (Closed Periods, Art. 19 XI MAR):** 30 Kalendertage vor Veröffentlichung des Halbjahres- bzw. Jahresfinanzberichts dürfen Führungskräfte grundsätzlich keine Eigengeschäfte tätigen — Ausnahmen nach Art. 19 XII MAR (außergewöhnliche Umstände, vorbestimmte Programme).

### 8. Sanktionen

| Norm | Sanktion |
|---|---|
| Art. 30 MAR + § 120 WpHG | Verwaltungssanktion: natP bis 5 Mio. EUR bzw. dreifacher Gewinn; jurP bis 15 Mio. EUR / 15 % Jahresumsatz Konzern |
| § 119 WpHG | Ordnungswidrigkeit (Bußgeld) |
| § 38 WpHG | Strafvorschrift Insiderhandel / Manipulation – Freiheitsstrafe bis 5 Jahre (qualifiziert nach § 38 V WpHG) |
| §§ 826, 823 II BGB iVm § 38 WpHG / Art. 17 MAR | Anlegerschadensersatz – BGH-Linie IKB, EM.TV `[unverifiziert]` |
| BaFin Naming and Shaming, Art. 34 MAR | Veröffentlichung der Sanktion auf bafin.de |

### 9. Strafrechtliche Schwelle § 38 WpHG

Die strafrechtliche Sanktion setzt nach BGH-Rspr. einen wirtschaftlichen Vorteil bzw. ein bedeutendes Umsatzvolumen voraus; bei geringfügigen Verstößen verbleibt es bei der Ordnungswidrigkeit nach § 119 WpHG. Im Mandat: subjektiver Tatbestand (Vorsatz / Leichtfertigkeit) sorgfältig prüfen.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Unmittelbar anwendbares Unionsrecht

- [VO (EU) 596/2014 (MAR)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596) – Art. 7, 8, 9, 10, 12, 14, 15, 17, 18, 19, 23, 30, 34
- DurchführungsVO (EU) 2016/1055 (Aufschub-Dokumentation)
- DurchführungsVO (EU) 2016/347 (Insiderliste)
- ESMA Guidelines on Delay of Disclosure of Inside Information (MAR/2016/1478) — **auf Vereinbarkeit mit der Fassung seit 05.06.2026 prüfen** `[unverifiziert - prüfen]`
- **EU Listing Act:** [RL (EU) 2024/2811](https://eur-lex.europa.eu/eli/dir/2024/2811/oj) und [VO (EU) 2024/2809](https://eur-lex.europa.eu/eli/reg/2024/2809/oj) — gestufte Geltung, **letzte Stufe anwendbar seit 05.06.2026**
- **Delegierte Verordnung der Kommission** zum Katalog der zeitlich gestreckten Vorgänge (35 Vorgänge / 7 Kategorien), in Kraft seit 05.06.2026 — Fundstelle `[unverifiziert - prüfen]`

### Deutsches Recht

- [§§ 33 ff. WpHG](https://www.gesetze-im-internet.de/wphg/__33.html) (Stimmrechtsmeldungen)
- [§ 38 WpHG](https://www.gesetze-im-internet.de/wphg/__38.html) (Strafvorschriften)
- [§ 119 WpHG](https://www.gesetze-im-internet.de/wphg/__119.html) (Bußgeldvorschriften)
- [§ 120 WpHG](https://www.gesetze-im-internet.de/wphg/__120.html) (Bußgeldhöhe)
- BaFin-Emittentenleitfaden Modul C (Marktmissbrauch / Ad-hoc-Publizität)

### Kommentare

- Klöhn, in: Klöhn, MAR, 1. Aufl. 2018, Art. 7 Rn. 1 ff.; Art. 17 Rn. 1 ff.
- Mülbert/Sajnovits, in: Assmann/Schneider/Mülbert, WpHG/MAR, 8. Aufl. 2024, Art. 7 MAR Rn. 1 ff.
- Pawlik, in: KapMRK (Schwark/Zimmer), 5. Aufl. 2020, Art. 17 MAR Rn. 1 ff.
- Just, in: Just/Voß/Ritz/Becker, WpHG, 1. Aufl. 2015, § 38 Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in curia.europa.eu / juris / bafin.de]`)

1. EuGH, Urt. v. 28.06.2012 – Rs. C-19/11, ECLI:EU:C:2012:397 (Geltl/Daimler – präzise Information in Zwischenschritten). **Reichweite seit 05.06.2026 eingeschränkt:** trägt weiterhin den Insiderbegriff des Art. 7 MAR, **nicht mehr** die Ad-hoc-Pflicht bei gestreckten Vorgängen.
2. EuGH, Urt. v. 11.03.2015 – Rs. C-628/13, ECLI:EU:C:2015:162 (Lafonta – Richtungsangabe nicht erforderlich)
3. BGH, Urt. v. 13.12.2011 – XI ZR 51/10, BGHZ 192, 90 (IKB – Anlegerschadensersatz Ad-hoc)
4. BGH, Urt. v. 19.07.2004 – II ZR 217/03, BGHZ 160, 134 (EM.TV)
5. BaFin-Sanktionsentscheidungen – veröffentlicht auf bafin.de (Naming and Shaming Art. 34 MAR)

## Ausgabeformat

```
GUTACHTEN — Marktmissbrauch MAR / WpHG
Emittent: <anonymisiert>  |  Vorgang: <M&A / Restrukturierung / Bilanz / …>

I. Sachverhalt (knapp)
II. Frage(n)
III. Kurzantwort
     – Insiderinformation: [ja / nein / Zwischenschritt (Art. 7 — ohne Ad-hoc-Folge)]
     – Gestreckter Vorgang: [ja — Endereignis: <…> / nein]
     – Ad-hoc-Pflicht: [erst mit Endereignis / unverzüglich / Aufschub Art. 17 IV zulässig]
     – Empfehlung: [Veröffentlichung / Aufschub mit Doku / Handelsverbot]

IV. Rechtliche Bewertung
    1. Anwendungsbereich MAR (Art. 2)
    2. Insiderinformation (Art. 7) – vier Kriterien
    3. Verbote (Art. 14, 15) – ggf. Legitimate Behaviour (Art. 9)
    4. Ad-hoc-Pflicht (Art. 17 I)
       a) Gestreckter Vorgang? Abgleich 35er-Katalog (DelVO, seit 05.06.2026)
       b) Endereignis – Bestimmung und Begründung
       c) Zwischenschritte: KEINE Ad-hoc-Pflicht
       d) Aufschub (Art. 17 IV) – drei Voraussetzungen
    5. Insiderliste (Art. 18) – Pflichten Emittent (auch für Zwischenschritte!)
    6. Directors' Dealings (Art. 19) – Closed Period
    7. Sanktionsrisiko (Art. 30 MAR, §§ 119, 38 WpHG)

V. Fristtabelle
   - Ad-hoc unverzüglich               (Art. 17 I MAR)
   - Aufschub-Doku + BaFin-Mitteilung  (Art. 17 IV MAR + DVO 2016/1055)
   - Directors' Dealings 3 Geschäftstage (Art. 19 I MAR)
   - Insiderliste Aktualisierung unverzüglich (Art. 18)

VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VII. Entwurf Ad-hoc-Mitteilung (optional)
     [sachliche Pressemitteilungs-Form, faktentreu, keine Werbung]

VIII. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Aufschub Art. 17 IV ohne Dokumentation** der drei Voraussetzungen — BLOCKER, Verstoß führt zu Bußgeld und Anlegerklagen-Exposition.
- **Insiderliste nicht aktualisiert**, wenn neue Berater eingebunden werden — Verstoß Art. 18 MAR.
- **Closed Period übersehen**, weil Vorstandsmitglied auf "vorbestimmten Plan" verweist, dessen Voraussetzungen nach Art. 19 XII MAR nicht erfüllt sind.
- **Zwischenschritt nach überholter Geltl-Linie ad hoc veröffentlicht** — BLOCKER. Seit dem **05.06.2026** ist bei einem zeitlich gestreckten Vorgang **nur das Endereignis** veröffentlichungspflichtig. Wer aus Vorsicht weiter auf Term Sheet oder LOI hin veröffentlicht, gibt Insiderinformationen ohne Rechtsgrund preis, verletzt Vertraulichkeitsinteressen und schafft selbst Manipulations- und Haftungsexposition. Muster-Ad-hoc-Richtlinien vor Juni 2026 sind **durchweg veraltet**.
- **Zwischenschritt umgekehrt für rechtlich irrelevant gehalten** — der spiegelbildliche Fehler. Der Wegfall der Ad-hoc-Pflicht lässt die **Insiderqualität nach Art. 7 MAR unberührt**: Handelsverbot Art. 14, Weitergabeverbot Art. 10 und Insiderlisten-Pflicht Art. 18 greifen ab dem Zwischenschritt unverändert.
- **Endereignis nicht dokumentiert bestimmt** — ohne Abgleich mit dem 35er-Katalog der Delegierten Verordnung und ohne protokollierte Vorstandsentscheidung ist der Veröffentlichungszeitpunkt gegenüber der BaFin nicht verteidigungsfähig. `[unverifiziert - prüfen]`
- **Ad-hoc-Gremium nicht nachgeschult** — die Neufassung verlagert die Entscheidung von laufender Zwischenschritt-Bewertung auf die Endereignis-Bestimmung. Ad-hoc-Richtlinien und Insiderverzeichnis-Prozesse sind neu zu fassen, die Gremien gegen die 35er-Liste neu zu schulen.
- **Marktmanipulations-Risiko bei Pressemitteilungen** ohne ausreichende Tatsachengrundlage — Art. 15 iVm Art. 12 I lit. c MAR.
- **Selbst-Bewertung ohne Insider-Check** in eilbedürftigen Sachverhalten (Vorstandskäufe vor Bilanzveröffentlichung) — BLOCKER.
- **Bankaufsichtsrechtliche Ebene** (KWG-Erlaubnis Wertpapierdienstleistung) nicht hier — Querverweis Plugin `bankrecht`.
