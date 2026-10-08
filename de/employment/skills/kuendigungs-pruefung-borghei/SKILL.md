---
name: kuendigungs-pruefung-borghei
title: /arbeitsrecht:kuendigungs-pruefung
description: Rechtliche Vollprüfung einer ordentlichen oder außerordentlichen Kündigung im deutschen Arbeitsrecht – KSchG (allgemeiner und besonderer Kündigungsschutz), § 102 BetrVG (BR-Anhörung), §§ 622 und 626 BGB (Fristen und wichtiger Grund), Sozialauswahl § 1 Abs. 3 KSchG, Sonderkündigungsschutz (MuSchG, BEEG, SGB IX, § 15 KSchG). Use when ein Arbeitgeber eine Kündigung plant oder ein Arbeitnehmervertretender eine empfangene Kündigung auf Klagewert prüft.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/arbeitsrecht/skills/kuendigungs-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /arbeitsrecht:kuendigungs-pruefung

## Zweck

Die meisten Kündigungen sind rechtlich unproblematisch. Einige sind Klagen, die noch nicht eingereicht wurden. Dieser Skill identifiziert die Hochrisikofälle, **bevor** die 3-Wochen-Frist des [§ 4 KSchG](https://www.gesetze-im-internet.de/kschg/__4.html) zu laufen beginnt: Sonderkündigungsschutz, fehlende BR-Anhörung, mangelhafte Sozialauswahl, unzureichende Dokumentation, vergessene Massenentlassungsanzeige.

## Eingaben

- **Kündigungsanlass:** betriebsbedingt / verhaltensbedingt / personenbedingt
- **Arbeitnehmer-Daten:** Beschäftigungsdauer, Position, Familienstand (für Sozialauswahl), Schwerbehinderung, BR-Mandat, Schwangerschaft / Elternzeit / Pflegezeit
- **Betriebs-Daten:** Anzahl AN nach § 23 KSchG, BR vorhanden? Tarifbindung?
- **Vorhistorie:** Vorherige Abmahnungen (für verhaltensbedingte Kündigung)? BEM durchgeführt (für personenbedingte / krankheitsbedingte)?
- **Geplante Maßnahme:** ordentlich vs. außerordentlich, Frist, Abfindungsangebot § 1a KSchG?

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert Statute mit URL, einschlägige Kommentarstellen (ErfK, APS, KR), bis zu drei BAG-Entscheidungen pro Frage (mit `[unverifiziert]`-Markern wo nötig).
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt die Prüfung im Gutachtenstil mit eingebauter Anspruchsgrundlagen-Reihenfolge (KSchG → BGB → BetrVG → Sonderschutz → Massenentlassung).
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Fristen, Sonderschutzlücken, Quellenmarker, Berufsrecht und gibt das finale Pass/Fix.

## Ablauf

### 1. Anwendungsbereich KSchG ([§ 23 KSchG](https://www.gesetze-im-internet.de/kschg/__23.html))

**Schwellenwert:** KSchG (Erster Abschnitt) gilt für AN, die länger als 6 Monate beschäftigt sind ([§ 1 Abs. 1 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html)), wenn im Betrieb **mehr als 10 AN** i.S.d. § 23 KSchG beschäftigt sind (für AN mit Beschäftigungsbeginn nach 31.12.2003 — Altbestand: > 5 AN):

- Vollzeitkräfte → 1,0
- Teilzeitkräfte bis 20 h/Woche → 0,5
- Teilzeitkräfte bis 30 h/Woche → 0,75
- **Leiharbeitnehmer** zählen im Entleiherbetrieb mit, wenn ihr Einsatz auf regelmäßigem Beschäftigungsbedarf beruht (BAG, Urt. v. 24.01.2013 – 2 AZR 140/12, NZA 2013, 726 `[unverifiziert – prüfen in juris]`).

**Kleinbetrieb (≤ 10 AN):** Kein allgemeiner KSchG-Schutz, aber Grundrechtsschutz. Eine Kündigung im Kleinbetrieb darf kein verkapptes Diskriminierungsmittel sein (BVerfG, Beschl. v. 27.01.1998 – 1 BvL 15/87, NJW 1998, 1475 — [unverifiziert – prüfen in juris]).

### 2. Sonderkündigungsschutz-Check (vor allem anderen)

Beim Vorliegen eines der folgenden Tatbestände: **🔴 BLOCKER – sofortige Eskalation an Mandantenanwalt.**

| Schutztatbestand | Norm | Anforderung |
|---|---|---|
| Schwangerschaft / Mutterschutz | [§ 17 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__17.html) | Behördliche Zustimmung (Amt für Arbeitsschutz) **vor** Ausspruch |
| Elternzeit | [§ 18 BEEG](https://www.gesetze-im-internet.de/beeg/__18.html) | Behördliche Zustimmung; Ausnahme bei schwerwiegenden Gründen § 18 Abs. 1 S. 2 BEEG |
| Schwerbehinderte / Gleichgestellte | [§ 168 SGB IX](https://www.gesetze-im-internet.de/sgb_9_2018/__168.html) | Zustimmung Inklusionsamt **vor** Ausspruch; 3-Wochen-Antragsfrist |
| BR-Mitglied, Wahlvorstand u.a. | [§ 15 KSchG](https://www.gesetze-im-internet.de/kschg/__15.html) | Ordentliche Kündigung **ausgeschlossen**; außerordentliche nur mit BR-Zustimmung [§ 103 BetrVG](https://www.gesetze-im-internet.de/betrvg/__103.html) |
| Datenschutzbeauftragter | [§ 38 Abs. 2 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__38.html) i.V.m. § 6 Abs. 4 BDSG | Kündigungsschutz während Amtszeit + 1 Jahr danach |
| Pflegezeit | [§ 5 PflegeZG](https://www.gesetze-im-internet.de/pflegezg/__5.html) | Schutz wie BEEG |

### 3. BR-Anhörung ([§ 102 BetrVG](https://www.gesetze-im-internet.de/betrvg/__102.html))

Bei Vorhandensein eines BR: **jede** Kündigung vor Ausspruch anhören. Ohne ordnungsgemäße Anhörung ist die Kündigung unwirksam (§ 102 Abs. 1 S. 3 BetrVG).

Checkliste:

- [ ] Schriftliche Information des BR (E-Mail genügt)
- [ ] Inhalt vollständig: Personalien, Art der Kündigung (ord./ao.), Kündigungsfrist, Kündigungsgründe konkret (nicht bloß Schlagworte)
- [ ] Frist abgewartet: 1 Woche bei ordentlicher, 3 Tage bei außerordentlicher Kündigung (§ 102 Abs. 2 BetrVG)
- [ ] BR-Bedenken protokolliert (keine Vetorechte bei ordentlicher Kündigung, aber Widerspruch § 102 Abs. 3 BetrVG gibt Weiterbeschäftigungsanspruch § 102 Abs. 5 BetrVG)

Detail-Skill: `/arbeitsrecht:betriebsrat-anhoerung` (geplant; aktuell als Stub).

Belege:

- Becker/Wolff, in: APS, 6. Aufl. 2021, § 102 BetrVG Rn. 12 ff.
- BAG, Urt. v. 22.09.1994 – 2 AZR 31/94, NZA 1995, 363 (Vollständigkeit der Anhörung) `[unverifiziert – prüfen in juris]`

### 4. Kündigungsgrund ([§ 1 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html))

#### A — Betriebsbedingte Kündigung

1. **Unternehmerische Entscheidung** vom AG frei, aber dringend erforderlich (keine andere zumutbare Beschäftigung). Vgl. BAG, Urt. v. 29.03.2007 – 2 AZR 31/06, NZA 2007, 912 Rn. 21 `[unverifiziert – prüfen]`.
2. **Wegfall des Arbeitsplatzes** konkret und dauerhaft (bloße Umsatzrückgänge genügen nicht).
3. **Weiterbeschäftigung auf vergleichbarem Arbeitsplatz** ausgeschlossen (§ 1 Abs. 2 S. 2 KSchG).
4. **Sozialauswahl** (siehe Ziff. 5).
5. **Massenentlassung** ([§§ 17–18 KSchG](https://www.gesetze-im-internet.de/kschg/__17.html)): Schwellen je nach Betriebsgröße; **Anzeige an Agentur für Arbeit VOR Ausspruch** der Kündigungen. Fehler → Unwirksamkeit. Vgl. BAG, Urt. v. 22.11.2012 – 2 AZR 371/11, NZA 2013, 437 `[unverifiziert – prüfen]`.

#### B — Verhaltensbedingte Kündigung

1. **Abmahnung** grundsätzlich vorausgegangen, außer bei schwerwiegenden Pflichtverletzungen. BAG-Leitentscheidung „Emmely": BAG, Urt. v. 10.06.2010 – 2 AZR 541/09, NZA 2010, 1227 `[unverifiziert – prüfen]`.
2. **Abmahnung hinreichend bestimmt:** konkrete Schilderung, klare Verhaltenserwartung, Sanktionsandrohung. BAG, Urt. v. 19.11.2015 – 2 AZR 217/15, NZA 2016, 540 `[unverifiziert – prüfen]`.
3. **Interessenabwägung:** Schwere der Pflichtverletzung vs. Dauer der Beschäftigung, Wiederholungsgefahr, Sozialdaten.

Detail-Skill: `/arbeitsrecht:abmahnung`.

#### C — Personenbedingte Kündigung (insb. krankheitsbedingt)

1. **Negative Prognose:** weitere erhebliche Fehlzeiten zu erwarten?
2. **Erhebliche betriebliche Beeinträchtigung** (Entgeltfortzahlung > 6 Wochen p.a., Betriebsablaufstörung).
3. **Interessenabwägung.** BAG, Urt. v. 13.05.2015 – 2 AZR 565/14, NZA 2016, 116 `[unverifiziert – prüfen]`.
4. **BEM** (Betriebliches Eingliederungsmanagement) nach [§ 167 Abs. 2 SGB IX](https://www.gesetze-im-internet.de/sgb_9_2018/__167.html) vor Kündigung durchführen, andernfalls erhöhte Darlegungslast. BAG, Urt. v. 12.07.2007 – 2 AZR 716/06, NZA 2008, 173 `[unverifiziert – prüfen]`.

### 5. Sozialauswahl ([§ 1 Abs. 3 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html))

Zentraler Prüfpunkt der betriebsbedingten Kündigung. Unter vergleichbaren AN müssen die **sozial am wenigsten schutzwürdigen** entlassen werden.

Kriterien (§ 1 Abs. 3 S. 1 KSchG):

- Betriebszugehörigkeit
- Lebensalter
- Unterhaltsverpflichtungen
- Schwerbehinderung

Prüfschema:

1. **Vergleichsgruppe bilden** (gleiche Hierarchieebene, Austauschbarkeit durch Einarbeitung ≤ 3 Monate).
2. **Sozialpunkte berechnen** — gesetzliche Punktetabelle gibt es **nicht**; Betriebsvereinbarung / Interessenausgleich mit Punkteschema empfohlen.
3. **Leistungsträger-Herausnahme** (§ 1 Abs. 3 S. 2 KSchG) restriktiv: nur wenn Weiterbeschäftigung im berechtigten betrieblichen Interesse. BAG, Urt. v. 07.07.2011 – 2 AZR 476/10, NZA 2012, 150 `[unverifiziert – prüfen]`.

### 6. Kündigungsfristen ([§ 622 BGB](https://www.gesetze-im-internet.de/bgb/__622.html))

| Beschäftigungsdauer | Frist (§ 622 Abs. 2 BGB) |
|---|---|
| 0–2 Jahre | 4 Wochen zum 15. oder Monatsende |
| 2–5 Jahre | 1 Monat zum Monatsende |
| 5–8 Jahre | 2 Monate |
| 8–10 Jahre | 3 Monate |
| 10–12 Jahre | 4 Monate |
| 12–15 Jahre | 5 Monate |
| 15–20 Jahre | 6 Monate |
| > 20 Jahre | 7 Monate |

**Tarifvertragliche Abweichungen** vorrangig prüfen.

**Außerordentliche Kündigung** ([§ 626 BGB](https://www.gesetze-im-internet.de/bgb/__626.html)): Wichtiger Grund + **2-Wochen-Frist ab Kenntnis** des Kündigungsberechtigten (§ 626 Abs. 2 BGB). BAG, Urt. v. 21.06.2012 – 2 AZR 694/11, NZA 2013, 199 `[unverifiziert – prüfen]`.

### 7. Abfindungsangebot ([§ 1a KSchG](https://www.gesetze-im-internet.de/kschg/__1a.html))

AG kann mit der betriebsbedingten Kündigung eine Abfindung anbieten (0,5 × Monatsgehalt × Beschäftigungsjahre), sofern AN keine Klage erhebt. Steuerliche Behandlung: [§ 34 EStG](https://www.gesetze-im-internet.de/estg/__34.html) (ermäßigter Steuersatz, „Fünftelregelung").

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md). Methodik: [`../../references/methodik.md`](../../references/methodik.md).

### Wesentliche Statute (verifiziert via gesetze-im-internet.de)

- [§ 1 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html), [§ 1a KSchG](https://www.gesetze-im-internet.de/kschg/__1a.html), [§ 4 KSchG](https://www.gesetze-im-internet.de/kschg/__4.html), [§ 15 KSchG](https://www.gesetze-im-internet.de/kschg/__15.html), [§ 17 KSchG](https://www.gesetze-im-internet.de/kschg/__17.html), [§ 18 KSchG](https://www.gesetze-im-internet.de/kschg/__18.html), [§ 23 KSchG](https://www.gesetze-im-internet.de/kschg/__23.html)
- [§ 102 BetrVG](https://www.gesetze-im-internet.de/betrvg/__102.html), [§ 103 BetrVG](https://www.gesetze-im-internet.de/betrvg/__103.html)
- [§ 622 BGB](https://www.gesetze-im-internet.de/bgb/__622.html), [§ 626 BGB](https://www.gesetze-im-internet.de/bgb/__626.html)
- [§ 17 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__17.html)
- [§ 18 BEEG](https://www.gesetze-im-internet.de/beeg/__18.html)
- [§ 168 SGB IX](https://www.gesetze-im-internet.de/sgb_9_2018/__168.html), [§ 167 SGB IX](https://www.gesetze-im-internet.de/sgb_9_2018/__167.html)
- [§ 5 PflegeZG](https://www.gesetze-im-internet.de/pflegezg/__5.html)
- [§ 38 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__38.html)
- [§ 34 EStG](https://www.gesetze-im-internet.de/estg/__34.html)

### Kommentare

- Linck, in: ErfK, 24. Aufl. 2024, § 1 KSchG Rn. 100 ff. (Sozialauswahl)
- Preis, in: ErfK, 24. Aufl. 2024, § 626 BGB Rn. 1 ff. (außerordentliche Kündigung)
- Dörner / Vossen, in: KR, 13. Aufl. 2022, § 1 KSchG Rn. 350 ff.
- Becker / Wolff, in: APS, 6. Aufl. 2021, § 102 BetrVG Rn. 12 ff.
- Berkowsky, in: MüKoBGB, 9. Aufl. 2023, § 622 Rn. 1 ff.

### Rechtsprechung (alle `[unverifiziert – prüfen in Beck-Online/juris]`)

1. BAG, Urt. v. 10.06.2010 – 2 AZR 541/09, NZA 2010, 1227 („Emmely")
2. BAG, Urt. v. 19.11.2015 – 2 AZR 217/15, NZA 2016, 540 (Abmahnungsbestimmtheit)
3. BAG, Urt. v. 07.07.2011 – 2 AZR 476/10, NZA 2012, 150 (Leistungsträger)
4. BAG, Urt. v. 22.11.2012 – 2 AZR 371/11, NZA 2013, 437 (Massenentlassung)
5. BAG, Urt. v. 12.07.2007 – 2 AZR 716/06, NZA 2008, 173 (BEM)
6. BAG, Urt. v. 21.06.2012 – 2 AZR 694/11, NZA 2013, 199 (§ 626 Abs. 2 BGB)
7. BAG, Urt. v. 29.03.2007 – 2 AZR 31/06, NZA 2007, 912 (betriebsbedingte Kündigung)
8. BAG, Urt. v. 13.05.2015 – 2 AZR 565/14, NZA 2016, 116 (krankheitsbedingt)
9. BAG, Urt. v. 22.09.1994 – 2 AZR 31/94, NZA 1995, 363 (BR-Anhörung)
10. BVerfG, Beschl. v. 27.01.1998 – 1 BvL 15/87, NJW 1998, 1475 (Kleinbetrieb)

> **Verifizierung:** Vor jeder Verwendung in mandantsbezogenen Schriftsätzen sind die obigen Az. in [openjur](https://openjur.net), [BAG-Datenbank](https://www.bundesarbeitsgericht.de/entscheidungen/) oder Beck-Online / juris zu prüfen.

## Ausgabeformat

```
KÜNDIGUNGSPRÜFUNG — <Mandat-ID/Position> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

Gesamtbefund: [🟢 Möglich / 🟡 Möglich mit Auflagen / 🔴 Nicht empfohlen]

⚠️ Verifikationshinweis: Alle BAG-Zitate dieser Prüfung sind mit
[unverifiziert] markiert und in Beck-Online/juris zu prüfen.

I.   KSchG-Anwendungsbereich         [🟢 / 🟡 / N/A]
     Begründung: <…>
II.  Sonderkündigungsschutz-Check    [🟢 / 🔴 Flag: <Tatbestand>]
III. Betriebsratsanhörung            [🟢 / 🔴 ausstehend / N/A kein BR]
IV.  Kündigungsgrund (§ 1 KSchG)     [🟢 / 🟡 / 🔴]
     Typ: <betriebsbedingt / verhaltensbedingt / personenbedingt>
     Begründung: <…>
V.   Sozialauswahl (nur bei bb)      [🟢 / 🟡 / 🔴]
     Vergleichsgruppe: <N AN>
     Sozialpunkte: <Tabelle oder Verweis auf Anlage>
VI.  Kündigungsfrist                 <Frist nach § 622 BGB oder TV>
VII. Massenentlassungsanzeige        [N/A / 🟢 erstattet / 🔴 fehlt]
VIII. Abfindungsangebot § 1a KSchG    <Betrag>  oder  keine Empfehlung

Offene Tatsachenfragen:
  - <…>

Offene Verifizierungen:
  - <BAG-Az.> in juris / openjur prüfen
  - <Kommentarstelle> aktuelle Auflage bestätigen

Empfehlung: <konkret, ohne Mandatsentscheidung vorzugreifen>
Eskalation: <ja/nein — Begründung>

Quellen: siehe references/zitierweise.md
```

## Beispiel — Betriebsbedingte Kündigung mit Sozialauswahl (Urteilsstil)

**Sachverhalt.** Mandantin betreibt Maschinenbauunternehmen mit 35 AN, kein BR. Plant Streichung einer von drei Stellen im Vertriebsinnendienst. Drei AN in Vergleichsgruppe:

- A: 10 Jahre, 45 Jahre alt, verheiratet, 2 Kinder
- B: 3 Jahre, 30 Jahre alt, ledig, anerkannt schwerbehindert (GdB 50)
- C: 8 Jahre, 55 Jahre alt, geschieden, 1 Kind

**Bewertung (Urteilsstil).** Die beabsichtigte Kündigung ist am ehesten gegenüber C zu rechtfertigen. In der Sozialauswahl nach § 1 Abs. 3 KSchG sind alle drei AN in eine Vergleichsgruppe einzustellen (gleiche Funktion, Austauschbarkeit gegeben). B genießt Sonderkündigungsschutz nach § 168 SGB IX; eine Kündigung erfordert Zustimmung des Inklusionsamts (🔴 Blocker). A und C stehen im direkten Auswahlvergleich: Die längere Betriebszugehörigkeit von A (10 J.), das Lebensalter (45 J.) und die zwei Unterhaltsverpflichtungen überwiegen die Schutzwürdigkeit von C (8 J., 55 J., ein Kind). C ist nach Sozialpunkten am wenigsten schutzwürdig — Kündigung sozialauswahl-konform, wenn der Auswahlvorgang schriftlich dokumentiert wird.

**🟠 Empfehlung.** Vor Ausspruch: (1) Sozialauswahldokumentation in der Personalakte hinterlegen, (2) Abfindungsangebot § 1a KSchG erwägen (4 BMG), (3) Massenentlassungsschwelle nicht erreicht (1/35 < 6 % bei < 60 AN), Anzeige nicht erforderlich, (4) bei Klagerisiko Vergleichsoption (etwa Aufhebungsvertrag, siehe `/arbeitsrecht:aufhebungsvertrag`) prüfen.

## Risiken / typische Fehler

- **Massenentlassungsanzeige vergessen** ([§§ 17–18 KSchG](https://www.gesetze-im-internet.de/kschg/__17.html)) — führt zur Unwirksamkeit aller Kündigungen. Schwellen ab 5 AN bei kleinen, ab 30 AN bei großen Betrieben innerhalb 30 Tagen.
- **BR-Anhörung inhaltlich unvollständig** — fehlende Angaben zu Person oder Grund machen Anhörung unwirksam (§ 102 Abs. 1 S. 3 BetrVG).
- **Sonderkündigungsschutz übersehen** — insbesondere bei BR-Mitgliedern, Schwangeren, Elternzeitnehmenden, Schwerbehinderten.
- **Sozialauswahl ohne Dokumentation** — bei Klagefrist-Ablauf nach § 4 KSchG kaum nachrüstbar.
- **2-Wochen-Frist § 626 Abs. 2 BGB** — beginnt mit positiver Kenntnis des Kündigungsberechtigten, nicht mit vager Vermutung.
- **BEM nicht durchgeführt** — vor krankheitsbedingter Kündigung erhöht die Darlegungslast.
- **Anwendung auf Kleinbetrieb übersehen** — bei ≤ 10 AN gilt KSchG nicht; Prüfung nur an Grundrechten + AGG.
