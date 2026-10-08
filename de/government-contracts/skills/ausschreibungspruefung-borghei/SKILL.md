---
name: ausschreibungspruefung-borghei
title: /vergaberecht:ausschreibungspruefung
description: Prüfung der Vergabeunterlagen einer EU-weiten Ausschreibung auf Vergaberechtskonformität (Bieterperspektive) – Eignungsanforderungen §§ 122–124 GWB, Mindestanforderungen, Zuschlagskriterien § 127 GWB und deren Gewichtung, Diskriminierungsverbot § 97 Abs. 2 GWB, Leistungsbeschreibung § 31 VgV, Losaufteilung § 97 Abs. 4 GWB. Use when ein Bieter vor Angebotsabgabe (oder ein Auftraggeber vor Bekanntmachung) klären muss, ob die Vergabeunterlagen rügefest sind.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vergaberecht/skills/ausschreibungspruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: government-contracts
language: de
---

# /vergaberecht:ausschreibungspruefung

## Zweck

Vergabeunterlagen müssen den Grundsätzen Wettbewerb, Transparenz und Gleichbehandlung (§ 97 Abs. 1, 2 GWB) genügen. Bieter, denen aus Bekanntmachung oder Vergabeunterlagen ein Verstoß **erkennbar** ist, müssen ihn spätestens bis Ablauf der Angebots-/Teilnahmefrist rügen — sonst Präklusion (§ 160 Abs. 3 S. 1 Nr. 2, 3 GWB). Dieser Skill prüft systematisch die Vergaberechtskonformität der Vergabeunterlagen und identifiziert Rügepunkte.

> **⚠️ Aktualität (Stand 2026-07):** Zwei neue Bundesgesetze verändern die Prüfung der Vergabeunterlagen.
>
> **1. Bundestariftreuegesetz (BTTG)** — vom Bundestag am **26.02.2026** beschlossen, verkündet in **BGBl. 2026 I Nr. 119 vom 30.04.2026**, **in Kraft seit 01.05.2026**. Es gilt für **Aufträge des Bundes ab einem Auftragsvolumen von 50.000 EUR netto**. **Ausgenommen sind Lieferaufträge und Aufträge der Bundeswehr.** Bei einschlägigen Bundesausschreibungen gehört die **Tariftreueerklärung** künftig zu den Angebotsunterlagen; ihr Fehlen ist ein Angebotsmangel, eine unzutreffende Bestimmung des einschlägigen Tarifvertrags durch den Auftraggeber ist ein Rügepunkt (siehe Schritt 5a).
>
> **2. Vergabebeschleunigungsgesetz** — Referentenentwurf 24.07.2025, Bundesrat **08.05.2026**, Verkündung **18.05.2026**, **in Kraft seit 01.07.2026**. Es verschiebt Direktauftragsgrenzen und Wertgrenzen, lockert bzw. verlagert Dokumentationspflichten zur Losaufteilung und verlangt angepasste Vergabevermerk-Vorlagen (siehe Schritt 5b).
>
> **Namensfalle:** Das Gesetz heißt **Vergabebeschleunigungsgesetz**. Der ältere Arbeitstitel aus der Ampel-Legislatur — „Vergaberechtstransformationsgesetz" — ist **nicht** die Bezeichnung des geltenden Gesetzes und darf nicht zitiert werden.
>
> Die konkreten Paragrafenzuordnungen beider Gesetze sind vor mandantengerichteter Verwendung am verkündeten Text zu verifizieren. `[unverifiziert - prüfen]`

## Eingaben

- Bekanntmachung (TED-Nummer, Auftraggeber, Verfahrensart, Auftragsgegenstand)
- Vergabeunterlagen (Auftragsbeschreibung / Leistungsbeschreibung, Eignungskriterien, Zuschlagskriterien, Wichtungsmatrix, Vertragsentwurf)
- Position des Mandanten (Bieter / Auftraggeber, der prüft)
- Angebotsfrist / Teilnahmefrist
- Etwaige bereits bestehende Auffälligkeiten oder Bieterfragen

## Sub-Agent-Architektur

Researcher liefert Statute (§§ 97, 122–124, 127 GWB; §§ 29, 31, 58 VgV), EuGH-Rspr. zu Eignungs- und Zuschlagskriterien sowie OLG-Vergabesenate-Rspr. zur Konkretisierung. Drafter führt die Prüfung in den unten dargestellten Schritten (1–7 nebst 5a Tariftreue/BTTG und 5b Vergabebeschleunigungsgesetz) durch und liefert eine priorisierte Rügeliste. Reviewer prüft, ob die Rügefrist (Ablauf Angebotsfrist § 160 Abs. 3 S. 1 Nr. 3 GWB) im Frist-Kalender abgebildet ist und ob die einzelnen Beanstandungen substanziell genug für eine wirksame Rüge sind.

## Ablauf

### 1. Bekanntmachung § 37 VgV

Pflichtangaben § 37 VgV i. V. m. Anhang V Teil C RL 2014/24/EU: Auftraggeber, Auftragsgegenstand, CPV-Code, Auftragswert (geschätzt), Verfahrensart, Eignungs- und Zuschlagskriterien (Mindestangaben), Fristen.

Prüfpunkte:

- [ ] CPV-Code korrekt?
- [ ] Auftragswert dem Schwellenwertregime entsprechend?
- [ ] Verfahrensart begründet (z. B. Verhandlungsverfahren nur bei Tatbestand § 14 Abs. 3, 4 VgV)?
- [ ] Eignungs- und Zuschlagskriterien wenigstens grundsätzlich benannt?
- [ ] Angebotsfrist § 15 ff. VgV gewahrt (offenes Verfahren: i. d. R. 35 Tage)?

### 2. Leistungsbeschreibung § 31 VgV

- **Eindeutigkeit** § 121 GWB, § 31 Abs. 1 VgV
- **Produktneutralität** § 31 Abs. 6 VgV: Verbot von Bezeichnungen, die bestimmte Erzeugnisse, Patente, Marken bevorzugen, außer "oder gleichwertig"
- **Funktional vs. konstruktiv** § 31 Abs. 2 VgV
- **Technische Anforderungen** § 31 Abs. 3 VgV (Normen, Spezifikationen)

Rspr.: EuGH, Urt. v. 25.10.2018 – Rs. C-413/17, Roche Lietuva (technische Spezifikationen, Diskriminierungsverbot) (https://curia.europa.eu/juris/liste.jsf?language=en&num=C-413/17).

### 3. Eignungsanforderungen §§ 122–124 GWB, §§ 44–47 VgV

#### 3.1 Eignungskriterien

- **Befähigung zur Berufsausübung** § 44 VgV
- **Wirtschaftliche und finanzielle Leistungsfähigkeit** § 45 VgV (Bilanzen, Umsatz, Versicherung)
- **Technische und berufliche Leistungsfähigkeit** § 46 VgV (Referenzen, Personal, Ausstattung)

Maßstab Verhältnismäßigkeit: § 122 Abs. 4 GWB — Eignungsanforderungen müssen in **Bezug** und **angemessenem Verhältnis** zum Auftragsgegenstand stehen.

#### 3.2 Eignungsleihe § 47 VgV / § 122 Abs. 2 GWB

Bieter kann Kapazitäten anderer Unternehmen in Anspruch nehmen. AG darf Eignungsleihe nur unter den Voraussetzungen § 47 VgV einschränken (z. B. § 47 Abs. 5 VgV für kritische Aufgaben).

#### 3.3 Ausschlussgründe

| Norm | Inhalt |
|---|---|
| § 123 GWB | Zwingende Ausschlussgründe (Straftaten, Steuerstraftaten, Mindestlohn) |
| § 124 GWB | Fakultative Ausschlussgründe (schwerwiegendes berufliches Fehlverhalten, Mängel früherer Aufträge) |
| § 125 GWB | Selbstreinigung (Maßnahmen, die Wiederherstellung der Zuverlässigkeit belegen) |

EuGH zur Selbstreinigung: EuGH, Urt. v. 24.10.2018 – Rs. C-124/17, Vossloh Laeis (https://curia.europa.eu/juris/liste.jsf?language=en&num=C-124/17).

### 4. Zuschlagskriterien § 127 GWB

- **Wirtschaftlichstes Angebot** § 127 Abs. 1 GWB — nicht zwingend niedrigster Preis
- **Bekanntgabe** § 127 Abs. 5 GWB — Zuschlagskriterien **und** Gewichtung müssen in Bekanntmachung oder Vergabeunterlagen genannt sein
- **Transparenz und Diskriminierungsfreiheit** — Bewertungsmethode muss reproduzierbar sein
- **Keine vermischten Eignungs-/Zuschlagskriterien** — Eignung ist binär (Ja/Nein), Zuschlag ist Bewertung

EuGH, Urt. v. 14.07.2016 – Rs. C-6/15, TNS Dimarso (Bekanntgabe Bewertungsmethode) (https://curia.europa.eu/juris/liste.jsf?language=en&num=C-6/15).

### 5. Losaufteilung § 97 Abs. 4 GWB

- Grundsatz Losaufteilung (§ 97 Abs. 4 S. 1 GWB)
- Verzicht nur bei **wirtschaftlichen oder technischen Gründen** dokumentiert im Vergabevermerk (§ 97 Abs. 4 S. 3 GWB)
- Quasi-Verbot für mittelstandsfeindliches Bündeln

OLG-Rspr.: OLG Düsseldorf, Beschl. v. 11.07.2018 – Verg 1/18, NZBau 2018, 638 (strenge Begründungspflicht) `[unverifiziert – prüfen]`.

### 5a. Tariftreue nach dem BTTG (Bundesaufträge ab 50.000 EUR netto)

Das **Bundestariftreuegesetz (BTTG)**, BGBl. 2026 I Nr. 119 vom 30.04.2026, gilt seit dem **01.05.2026**.

**Anwendungsbereich prüfen (Vorfrage):**

- [ ] Ist der Auftraggeber ein **Auftraggeber des Bundes**? Das BTTG bindet den Bund; Landes- und Kommunalaufträge unterliegen weiterhin den **Landesvergabe-/Tariftreuegesetzen**, die eigene, oft niedrigere Schwellen und abweichende Tarifbezüge vorsehen. Beide Regime nebeneinander prüfen, nicht vermengen.
- [ ] Erreicht das Auftragsvolumen **50.000 EUR netto**? Darunter greift das BTTG nicht.
- [ ] Liegt eine **Ausnahme** vor? **Lieferaufträge** und **Aufträge der Bundeswehr** sind vom BTTG **ausgenommen**. Bei gemischten Aufträgen ist der Schwerpunkt der Leistung zu bestimmen.

**Prüfpunkte in den Vergabeunterlagen:**

- [ ] Ist der vom Auftraggeber als einschlägig bezeichnete **Tarifvertrag** (Branche, fachlicher und räumlicher Geltungsbereich, Entgeltgruppen, Stand) benannt — und trifft die Zuordnung für die ausgeschriebene Leistung zu? Eine sachfremde Tarifzuordnung verzerrt die Kalkulation aller Bieter und ist rügefähig.
- [ ] Enthalten die Unterlagen ein **Formblatt zur Tariftreueerklärung**? Ist es widerspruchsfrei zu Leistungsbeschreibung und Vertragsentwurf?
- [ ] Verlangt der Vertragsentwurf die **Weitergabe der Tarifbedingungen an Nachunternehmer und Verleiher** (Flow-down) und eine Erklärung dieser Unternehmen?
- [ ] Sind **Kontroll-, Nachweis- und Auskunftsrechte** des Auftraggebers sowie **Sanktionen** (Vertragsstrafe, Kündigung, Ausschluss) verhältnismäßig ausgestaltet?

**Bieterseitige Handlungspflichten** (auch ohne Rügepunkt abzuarbeiten):

1. Einschlägigen Tarifvertrag je Bundesausschreibung ≥ 50.000 EUR netto bestimmen und die Zuordnung intern dokumentieren.
2. **Tariftreueerklärung mit dem Angebot einreichen** — Fristversäumnis oder Fehlen ist ein Angebotsmangel.
3. Tarifbedingungen an die gesamte Nachunternehmerkette weitergeben und die eigene **Kontrolle dokumentieren**.
4. Auf **Kontrollen und Nachweisverlangen** des Auftraggebers fristgerecht reagieren; Nachweisunterlagen für die Vertragslaufzeit vorhalten.

Die Einzelnormen des BTTG sind vor Verwendung am verkündeten Text zu verifizieren. `[unverifiziert - prüfen]`

### 5b. Vergabebeschleunigungsgesetz (seit 01.07.2026)

Das **Vergabebeschleunigungsgesetz** ist am **18.05.2026** verkündet worden und seit **01.07.2026 in Kraft**. Bei jeder Prüfung von Vergabeunterlagen sind daher neu abzugleichen:

- [ ] **Direktauftrags- und Wertgrenzen** — bei Unterschwellenvergaben und Bagatellbeschaffungen nicht aus dem Gedächtnis, sondern gegen die geltende Fassung prüfen.
- [ ] **Dokumentationspflichten zur Losaufteilung** (§ 97 Abs. 4 GWB) — Umfang und Verortung der Begründung wurden angepasst; ein Verzicht auf Lose bleibt begründungsbedürftig, der Begründungsmaßstab ist jedoch neu zu bestimmen.
- [ ] **Vergabevermerk-Vorlagen** — Muster, die vor dem 01.07.2026 erstellt wurden, sind veraltet.

Angesichts der jungen Rechtslage existiert zu diesem Gesetz noch **keine gefestigte Vergabesenats-Rechtsprechung**; Argumentationen sind entsprechend vorsichtig zu formulieren. `[unverifiziert - prüfen]`

### 6. Vertragsentwurf / AGB-Kontrolle

Im Oberschwellenbereich wird zunehmend Vertragsbedingungen geprüft (Risikoallokation, Vertragsstrafen, Haftungsklauseln). Maßstab: §§ 305 ff. BGB ist im Vergabeverhältnis grundsätzlich anwendbar, BGH, Urt. v. 19.05.2011 – VII ZR 24/08, NZBau 2011, 615 `[unverifiziert – prüfen]`.

### 7. Rügeliste und Frist-Strategie

Priorisierte Rügeliste:

| Priorität | Rügepunkt | Norm | Erkennbarkeit | Frist |
|---|---|---|---|---|
| 🔴 Hoch | <…> | <z. B. § 127 GWB> | aus Vergabeunterlagen | bis Angebotsfrist § 160 Abs. 3 S. 1 Nr. 3 GWB |
| 🟡 Mittel | <…> | <…> | aus Bekanntmachung | bis Angebotsfrist § 160 Abs. 3 S. 1 Nr. 2 GWB |

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 97 GWB](https://www.gesetze-im-internet.de/gwb/__97.html) (Grundsätze, Losaufteilung)
- [§ 121 GWB](https://www.gesetze-im-internet.de/gwb/__121.html) (Leistungsbeschreibung)
- [§ 122 GWB](https://www.gesetze-im-internet.de/gwb/__122.html) (Eignung)
- [§ 123 GWB](https://www.gesetze-im-internet.de/gwb/__123.html) (Zwingende Ausschlussgründe)
- [§ 124 GWB](https://www.gesetze-im-internet.de/gwb/__124.html) (Fakultative Ausschlussgründe)
- [§ 125 GWB](https://www.gesetze-im-internet.de/gwb/__125.html) (Selbstreinigung)
- [§ 127 GWB](https://www.gesetze-im-internet.de/gwb/__127.html) (Zuschlag)
- [§ 29 VgV](https://www.gesetze-im-internet.de/vgv_2016/__29.html) (Vergabeunterlagen)
- [§ 31 VgV](https://www.gesetze-im-internet.de/vgv_2016/__31.html) (Leistungsbeschreibung)
- [§ 37 VgV](https://www.gesetze-im-internet.de/vgv_2016/__37.html) (Bekanntmachung)
- [§§ 44–47 VgV](https://www.gesetze-im-internet.de/vgv_2016/) (Eignung, Eignungsleihe)
- [§ 58 VgV](https://www.gesetze-im-internet.de/vgv_2016/__58.html) (Zuschlag)
- [Art. 18 RL 2014/24/EU](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014L0024) (Grundsätze)
- [Art. 58 RL 2014/24/EU](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014L0024) (Eignungskriterien)
- [Art. 67 RL 2014/24/EU](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014L0024) (Zuschlagskriterien)
- **Bundestariftreuegesetz (BTTG)**, BGBl. 2026 I Nr. 119 vom 30.04.2026, in Kraft seit 01.05.2026 — Volltext über [gesetze-im-internet.de](https://www.gesetze-im-internet.de/) bzw. das [Bundesgesetzblatt](https://www.recht.bund.de/) abrufen; Einzelnormen `[unverifiziert - prüfen]`
- **Vergabebeschleunigungsgesetz**, verkündet 18.05.2026, in Kraft seit 01.07.2026 (Änderungen u. a. an GWB Teil 4 und VgV) — BGBl.-Fundstelle am verkündeten Text verifizieren `[unverifiziert - prüfen]`

### Kommentare

- Burgi, Vergaberecht, 4. Aufl. 2022, § 14 Rn. 1 ff. (Leistungsbeschreibung), § 16 Rn. 1 ff. (Eignung), § 18 Rn. 1 ff. (Zuschlag)
- Mertens, in: Ziekow/Völlink, Vergaberecht, 5. Aufl. 2024, § 122 GWB Rn. 1 ff.
- Opitz, in: Beck'scher Vergaberechtskommentar, 4. Aufl. 2022, § 127 GWB Rn. 1 ff.
- Pünder, in: Pünder/Schellenberg, Vergaberecht, 4. Aufl. 2022, § 97 GWB Rn. 50 ff. (Lose)

### Rechtsprechung (`[unverifiziert – prüfen in Beck-Online/juris/eur-lex]`)

1. EuGH, Urt. v. 14.07.2016 – Rs. C-6/15, TNS Dimarso (Bewertungsmethode bekannt geben)
2. EuGH, Urt. v. 24.10.2018 – Rs. C-124/17, Vossloh Laeis (Selbstreinigung § 125 GWB)
3. EuGH, Urt. v. 25.10.2018 – Rs. C-413/17, Roche Lietuva (Produktneutralität)
4. BGH, Urt. v. 19.05.2011 – VII ZR 24/08, NZBau 2011, 615 (AGB-Kontrolle im Vergabevertrag)
5. OLG Düsseldorf, Beschl. v. 11.07.2018 – Verg 1/18, NZBau 2018, 638 (Losaufteilung)
6. OLG München, Beschl. v. 02.11.2012 – Verg 26/12, NZBau 2013, 261 (Vermischung Eignung/Zuschlag)

## Ausgabeformat

```
AUSSCHREIBUNGSPRÜFUNG
Mandat: <…>
Auftraggeber: <…>
Verfahren / TED-Nr.: <…>
Angebotsfrist: <…>
Stand: <Datum>

I. Verfahrensrahmen
   - Verfahrensart: <…>
   - Anwendbares Regelwerk: <VgV / SektVO / KonzVgV>
   - Geschätzter Auftragswert: <EUR>

II. Bekanntmachung § 37 VgV
    Befund: <✅ / ⚠️ / 🔴>
    Punkte:
      - <…>

III. Leistungsbeschreibung § 31 VgV
     Eindeutigkeit:        <…>
     Produktneutralität:   <…>
     Technische Specs:     <…>

IV. Eignungsanforderungen §§ 122–124 GWB
    Anforderung 1: <…> — verhältnismäßig? Bezug zum Auftrag?
    Anforderung 2: <…>
    Eignungsleihe § 47 VgV: <unzulässig eingeschränkt?>
    Ausschlussgründe § 123/124: <…>

V. Zuschlagskriterien § 127 GWB
   Kriterium / Gewichtung / Bewertungsmethode
   Vermischung mit Eignung?
   Transparenz / Reproduzierbarkeit?

VI. Losaufteilung § 97 Abs. 4 GWB
    Lose vorgesehen? Begründung des Verzichts?
    Maßstab nach Vergabebeschleunigungsgesetz (seit 01.07.2026) abgeglichen? <ja/nein>

VI-a. Tariftreue BTTG (seit 01.05.2026)
    Bundesauftrag?                      <ja / nein — bei nein: Landesvergabegesetz prüfen>
    Volumen ≥ 50.000 EUR netto?         <ja / nein>
    Ausnahme (Lieferauftrag/Bundeswehr)? <ja / nein>
    Einschlägiger Tarifvertrag benannt / zutreffend? <…>
    Tariftreueerklärung im Angebot vorgesehen?       <…>
    Nachunternehmer-Flow-down + Kontrolldokumentation? <…>

VII. Vertragsentwurf
     AGB-rechtliche Risiken §§ 305 ff. BGB

VIII. Rügeliste (priorisiert)
      🔴 1. <…> — Norm — Rügefrist <Datum>
      🟡 2. <…> — Norm — Rügefrist <Datum>
      🟢 3. <…>

IX. Risiken / offene Punkte
    🟢/🟡/🔴
    Frist-Kalender:
      Angebotsfrist:                 <Datum>
      Rüge erkennbarer Punkte:       bis Angebotsfrist § 160 Abs. 3 S. 1 Nr. 2/3 GWB
      Rüge nicht-erkennbarer Punkte: 10 KT ab Kenntnis § 160 Abs. 3 S. 1 Nr. 1 GWB

X. Quellenverzeichnis
   <gem. references/zitierweise.md>
```

## Beispiele

### Beispiel — Zuschlagskriterien ohne Gewichtung

> **Sachverhalt:** Vergabeunterlagen einer Landesbehörde benennen vier Zuschlagskriterien (Preis, Qualität, Konzept, Termin), aber **keine Gewichtung**. Auftragswert 800.000 EUR netto, offenes Verfahren VgV.
>
> **Bewertung:** Nach § 127 Abs. 5 GWB i. V. m. § 58 Abs. 3 VgV muss die **Gewichtung** der Zuschlagskriterien in Bekanntmachung oder Vergabeunterlagen genannt sein. Fehlt sie, ist die Bewertungsmethode intransparent und verstößt gegen Art. 67 RL 2014/24/EU; EuGH, Urt. v. 14.07.2016 – Rs. C-6/15, TNS Dimarso (https://curia.europa.eu/juris/liste.jsf?language=en&num=C-6/15).
>
> **Rügeempfehlung:** 🔴 Erkennbarkeit aus Vergabeunterlagen → Frist § 160 Abs. 3 S. 1 Nr. 3 GWB = bis Ablauf Angebotsfrist. Rügeschreiben empfehlen mit konkreter Forderung: Nachreichung einer Gewichtung; andernfalls Nachprüfungsantrag.

## Risiken / typische Fehler

- **Erkennbarer Verstoß nicht bis Ablauf Angebotsfrist gerügt** → Präklusion § 160 Abs. 3 S. 1 Nr. 2/3 GWB.
- **Vermischung Eignung und Zuschlag** — Eignung ist binär (Mindestanforderung), Zuschlag ist Bewertung. OLG-Rspr. streng.
- **Eignungsanforderungen unverhältnismäßig** (z. B. Umsatzgrenzen weit über § 45 Abs. 4 VgV; Referenzwerte unangemessen).
- **Produktbezeichnung ohne "oder gleichwertig"** § 31 Abs. 6 VgV — Diskriminierung.
- **Losaufteilung ohne ordnungsgemäße Begründung** im Vergabevermerk § 8 VgV i. V. m. § 97 Abs. 4 S. 3 GWB.
- **Bewertungsmethode nachträglich verändert** — Verstoß gegen Transparenzgrundsatz § 97 Abs. 1 GWB.
- **Rügeschreiben pauschal** ("verstößt gegen Vergaberecht") — unsubstanziiert, schadet im späteren Nachprüfungsantrag.
- **Falscher Gesetzesname: „Vergaberechtstransformationsgesetz"** — das ist der Arbeitstitel eines Vorhabens der Ampel-Legislatur, nicht das geltende Recht. Das seit **01.07.2026** geltende Gesetz heißt **Vergabebeschleunigungsgesetz**. Die falsche Bezeichnung in einer Rüge oder einem Nachprüfungsantrag beschädigt die Glaubwürdigkeit des Vortrags.
- **Tariftreueerklärung nach dem BTTG nicht mit dem Angebot eingereicht** — bei Bundesaufträgen ab **50.000 EUR netto** ein Angebotsmangel; die Erklärung wird regelmäßig übersehen, weil sie nicht in klassischen Eignungsformblättern steht.
- **BTTG-Anwendungsbereich überdehnt** — **Lieferaufträge** und **Aufträge der Bundeswehr** sind ausgenommen, und das BTTG bindet den **Bund**. Wer es auf Landes- oder Kommunalaufträge anwendet, prüft am falschen Gesetz vorbei; dort gelten die Landesvergabe-/Tariftreuegesetze mit eigenen Schwellen.
- **BTTG-Schwelle mit dem EU-Schwellenwert verwechselt** — die 50.000 EUR netto sind eine eigenständige, deutlich niedrigere Auslöseschwelle und gelten auch im Unterschwellenbereich.
- **Tarifbedingungen nicht an Nachunternehmer weitergegeben** oder die Kontrolle nicht dokumentiert — die Flow-down- und Dokumentationspflicht trifft den Auftragnehmer während der gesamten Vertragslaufzeit, nicht nur bei Angebotsabgabe.
- **Vergabevermerk- und Losdokumentations-Muster von vor dem 01.07.2026 weiterverwendet** — das Vergabebeschleunigungsgesetz hat die Dokumentationsanforderungen und Wertgrenzen verändert.
