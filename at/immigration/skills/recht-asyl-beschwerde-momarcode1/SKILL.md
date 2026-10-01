---
name: recht-asyl-beschwerde-momarcode1
title: /recht asyl-beschwerde — Asyl-Beschwerde und Rechtsmittel (Procedural)
description: Austrian asylum and immigration appeals — drafting Beschwerde against BFA decisions, BVwG proceedings, VfGH/VwGH appeals, Schubhaftbeschwerde, Folgeantrag strategy, and aufschiebende Wirkung applications.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-asyl-beschwerde
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: immigration
language: de
---

# /recht asyl-beschwerde — Asyl-Beschwerde und Rechtsmittel (Procedural)

When the user has received a negative BFA decision or needs to draft an asylum/immigration appeal, follow these steps exactly.

---

## Step 1: Read the BFA-Bescheid / Situation

Read the entire decision or situation description. Extract:

1. **Bescheid-Typ** — Was wurde entschieden?
   - Asylantrag abgewiesen (§3 AsylG)?
   - Subsidiärer Schutz nicht zuerkannt (§8 AsylG)?
   - Aufenthaltstitel nicht erteilt (§55-57 AsylG)?
   - Rückkehrentscheidung erlassen (§52 FPG)?
   - Einreiseverbot verhängt (§53 FPG)?
   - Aufschiebende Wirkung aberkannt (§18 BFA-VG)?
   - Abschiebung angeordnet?
   - Schubhaft verhängt (§76 FPG)?
   - Dublin-Bescheid (Zuständigkeit anderer Staat)?
   - Aberkennung des Status (§7 oder §9 AsylG)?

2. **Zustelldatum** — Wann wurde der Bescheid zugestellt? **FRIST BERECHNEN!**
   - Persönliche Zustellung: Tag der Übergabe
   - RSa-Brief: Tag der Übernahme, bei Hinterlegung: Tag der Hinterlegung beim Postamt
   - Ohne Zustellnachweis: Wenn bestritten, Beweislast beim BFA

3. **Begründung des BFA** — Wie hat das BFA argumentiert?
   - Beweiswürdigung (Glaubwürdigkeit des Vorbringens)
   - Länderfeststellungen (welche Quellen, wie aktuell?)
   - Rechtliche Beurteilung

4. **Verfahrensmängel** — Gibt es offensichtliche Fehler?
   - Fehlende oder fehlerhafte Einvernahme
   - Veraltete Länderfeststellungen
   - Fehlender Dolmetscher oder falscher Dolmetscher
   - Kein Parteiengehör (§45 Abs 3 AVG)
   - Relevantes Vorbringen nicht behandelt (Begründungsmangel)

5. **Persönliche Umstände** — Neue Fakten seit dem Antrag?

If the Zustelldatum is unclear, ask IMMEDIATELY:
> "Wann wurde Ihnen der Bescheid zugestellt? Das genaue Datum ist entscheidend — die Beschwerdefrist läuft ab Zustellung!"

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references (VwGH, VfGH, BVwG), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

Search RIS Justiz for relevant VwGH/VfGH-Entscheidungen zu den zentralen Rechtsfragen. Present using format from `references/ogh-case-presentation.md` (adapted for VwGH/VfGH).

---

## Step 3: Classify the Procedural Situation and Calculate Deadlines

**THIS IS THE MOST CRITICAL STEP. Get the deadline wrong and the person may be deported.**

### Beschwerdefristen

| Bescheid-Typ | Frist | Grundlage | Berechnung |
|-------------|-------|-----------|------------|
| Negativer Asyl-Bescheid (inhaltliche Entscheidung) | **4 Wochen** | §7 Abs 4 BFA-VG | Ab Zustellung, Fristende = gleicher Wochentag 4 Wochen später |
| Dublin-Bescheid | **2 Wochen** | §16 Abs 1 BFA-VG | Ab Zustellung |
| Bescheid mit aberkannter aufschiebender Wirkung | **4 Wochen** Beschwerde, aber **1 Woche** für Antrag auf aufschiebende Wirkung | §18 Abs 5 BFA-VG | 1-Wochen-Frist ist die dringendere! |
| Schubhaftbeschwerde | **Keine Frist** (solange Schubhaft andauert) | §22a Abs 1 BFA-VG | Sofort einbringen! |
| Mandatsbescheid (Abschiebung) | **2 Wochen** | §57 Abs 2 AVG | Ab Zustellung |
| Verfahrensanordnung (nicht Bescheid) | **Nicht beschwerdefähig** | — | Ggf. Maßnahmenbeschwerde prüfen |

### Fristberechnung

Berechne das genaue Fristende:
- **Zustelldatum:** [vom Nutzer angegeben]
- **Fristende:** [berechnet]
- **Verbleibende Tage:** [Anzahl]
- **Fällt auf Wochenende/Feiertag?** → Nächster Werktag (§33 Abs 2 AVG)

**Wenn weniger als 7 Tage verbleiben: SOFORTIGE WARNUNG.**
**Wenn Frist bereits abgelaufen: Wiedereinsetzung prüfen (§33 VwGVG).**

### Rechtsmittelkette

```
BFA-Bescheid
    ↓ Beschwerde (§7 BFA-VG)
Bundesverwaltungsgericht (BVwG)
    ↓ Revision (Art 133 Abs 4 B-VG)        ↓ Beschwerde (Art 144 B-VG)
Verwaltungsgerichtshof (VwGH)               Verfassungsgerichtshof (VfGH)
```

---

## Step 4: Identify Grounds for Appeal

Systematically check ALL possible Beschwerdegründe:

### A: Verfahrensmängel (§§37ff AVG)

1. **Mangelhaftes Ermittlungsverfahren (§37 AVG)**
   - Hat das BFA den Sachverhalt vollständig ermittelt?
   - Wurden alle relevanten Beweismittel aufgenommen?
   - Wurde der Antragsteller ordnungsgemäß einvernommen?

2. **Fehlende/mangelhafte Einvernahme**
   - Einvernahme ohne qualifizierten Dolmetscher (falsche Sprache/Dialekt)
   - Suggestivfragen, unzureichende Befragung zu Fluchtgründen
   - Keine kindgerechte Einvernahme bei Minderjährigen
   - Einvernahme trotz offensichtlicher Traumatisierung ohne psychologische Unterstützung

3. **Verletzung des Parteiengehörs (§45 Abs 3 AVG)**
   - Länderfeststellungen nicht vorgehalten
   - Beweisergebnisse nicht mitgeteilt
   - Keine Möglichkeit zur Stellungnahme

4. **Begründungsmangel (§60 AVG)**
   - Bescheid enthält keine nachvollziehbare Beweiswürdigung
   - Relevantes Vorbringen wird nicht behandelt
   - Widersprüche in der Begründung

### B: Mangelhafte Beweiswürdigung

1. **Unschlüssige Beweiswürdigung**
   - BFA stützt Unglaubwürdigkeit auf periphere Details, nicht auf den Kernvortrag
   - Kulturelle Missverständnisse als Widersprüche gewertet
   - Unzulässige Anforderungen an Detailgenauigkeit (VwGH Ra 2018/19/0123)
   - Fehlende Auseinandersetzung mit vorgelegten Beweismitteln

2. **Glaubwürdigkeitsbeurteilung**
   - Plausibilitätsprüfung vs. tatsächliche Widersprüche unterscheiden
   - Trauma-bedingte Erinnerungslücken berücksichtigen (UNHCR-Handbuch Rz 219)
   - Verspätetes Vorbringen nicht automatisch unglaubwürdig (VwGH Ra 2019/14/0153)

### C: Mangelhafte Länderfeststellungen

1. **Veraltete Quellen** — Länderfeststellungen älter als 6-12 Monate?
2. **Einseitige Quellenauswahl** — Nur Staatendokumentation, keine UNHCR/EASO/NGO-Berichte?
3. **Fehlende Individualisierung** — Generelle Lage vs. spezifische Gefährdung des Antragstellers
4. **Neue Entwicklungen** — Hat sich die Lage seit dem Bescheid verschlechtert?
5. **Aktuelle Quellen einbringen** — EASO/EUAA COI, UNHCR-Positionen, Amnesty, HRW, ACCORD

### D: Rechtliche Fehler

1. **Falscher Prüfungsmaßstab** — Asyl: "wohlbegründete Furcht" (nicht: Beweis der Verfolgung)
2. **Fehlende Prüfung des subsidiären Schutzes** — Muss auch bei Asyl-Ablehnung geprüft werden
3. **Art 8 EMRK nicht/unzureichend geprüft** — Alle Kriterien des VfGH-Katalogs abzuarbeiten
4. **Interne Fluchtalternative (§11 AsylG)** — Zumutbarkeit nicht hinreichend geprüft
5. **Refoulement-Verbot nicht beachtet** — Art 3 EMRK ist absolut, keine Abwägung

---

## Step 5: Draft the Beschwerde

### Structure of a Beschwerde an das BVwG (§9 VwGVG):

```
An das
Bundesverwaltungsgericht
über das
Bundesamt für Fremdenwesen und Asyl
Regionaldirektion [Ort]

Beschwerdeführer/in:  [Vollständiger Name]
                      geb. am [Datum]
                      StA: [Staatsangehörigkeit]
                      IFA-Zahl: [Zahl]
                      [Adresse / Unterkunft]
                      [vertreten durch: Rechtsberatung/RA Name, Adresse]

wegen:                Beschwerde gegen den Bescheid des BFA vom [Datum],
                      Zl. [Geschäftszahl],
                      zugestellt am [Zustelldatum]

                      B E S C H W E R D E

I. ANFECHTUNGSERKLÄRUNG

Der Bescheid des Bundesamtes für Fremdenwesen und Asyl vom [Datum],
Zl. [Geschäftszahl], wird zur Gänze [ODER: in seinen Spruchpunkten
[I., II., III., ...]] angefochten.

II. BESCHWERDEGRÜNDE

Die Beschwerde wird auf folgende Gründe gestützt:

1. Mangelhaftigkeit des Verfahrens (§§37ff AVG)

[Konkret darlegen, welche Verfahrensvorschriften verletzt wurden.
Für jeden Mangel angeben, warum bei Vermeidung des Mangels ein
anderes Ergebnis möglich gewesen wäre.]

a) [Verfahrensmangel 1 — z.B. fehlende Einvernahme zu bestimmtem Punkt]

   Das BFA hat es unterlassen, [konkreter Mangel]. Bei Durchführung
   [der unterlassenen Ermittlung] hätte sich ergeben, dass [Relevanz
   für das Ergebnis].

b) [Verfahrensmangel 2]

2. Unrichtige Beweiswürdigung

[Das BFA hat die Glaubwürdigkeit des Beschwerdeführers zu Unrecht
verneint, weil...]

a) [Konkreter Punkt der Beweiswürdigung, der angegriffen wird]

   Das BFA führt aus, [Zitat aus dem Bescheid]. Diese Beurteilung
   ist verfehlt, weil [Begründung]. Der VwGH hat in [GZ] klargestellt,
   dass [relevanter Rechtssatz].

b) [Weiterer Punkt]

3. Mangelhafte/veraltete Länderfeststellungen

[Die im Bescheid herangezogenen Länderfeststellungen sind unvollständig/
veraltet. Insbesondere...]

   Beweis: [Aktuelle EASO/EUAA-Berichte, UNHCR-Position, ACCORD-
   Anfragebeantwortung — als Beilage beifügen]

4. Unrichtige rechtliche Beurteilung

[Das BFA hat §[x] unrichtig angewendet, weil...]

III. ANTRÄGE

Der Beschwerdeführer stellt daher die

                      A N T R Ä G E,

das Bundesverwaltungsgericht möge

1.  der Beschwerde Folge geben und den angefochtenen Bescheid dahingehend
    abändern, dass dem Beschwerdeführer der Status des Asylberechtigten
    gemäß §3 Abs 1 AsylG 2005 zuerkannt wird;

    in eventu

2.  den angefochtenen Bescheid dahingehend abändern, dass dem
    Beschwerdeführer der Status des subsidiär Schutzberechtigten
    gemäß §8 Abs 1 AsylG 2005 zuerkannt wird;

    in eventu

3.  den angefochtenen Bescheid dahingehend abändern, dass dem
    Beschwerdeführer ein Aufenthaltstitel aus berücksichtigungswürdigen
    Gründen gemäß §55 AsylG 2005 erteilt wird;

    in eventu

4.  den angefochtenen Bescheid beheben und die Angelegenheit zur
    neuerlichen Verhandlung und Entscheidung an das BFA zurückverweisen;

5.  der Beschwerde die aufschiebende Wirkung zuerkennen [falls aberkannt];

6.  eine mündliche Verhandlung durchführen.

[Ort], am [Datum]

                      ____________________
                      [Unterschrift]
                      [Name / Rechtsvertretung]


BEILAGENVERZEICHNIS:
./1  Bescheid des BFA vom [Datum], Zl. [GZ]
./2  [Aktuelle Länderberichte — EASO/EUAA, UNHCR, etc.]
./3  [Weitere Beweismittel — Arztbriefe, Fotos, Dokumente]
./4  [Vollmacht — falls vertreten]
```

### Beschwerde-Varianten

#### Für Dublin-Beschwerde (2-Wochen-Frist!):

Zusätzliche Punkte:
- Systemische Mängel im Zielstaat (VfGH E 4.10.2017, E 2407/2017)
- Familienzusammenführung (Art 8-11 Dublin-III-VO)
- Selbsteintrittsrecht (Art 17 Dublin-III-VO)
- Fristablauf der Überstellungsfrist (6 Monate, 18 Monate bei Untertauchen)
- Besondere Vulnerabilität (EuGH C-163/17, Jawo; C-578/16, C.K.)

#### Für Schubhaftbeschwerde (§22a BFA-VG):

```
An das
Bundesverwaltungsgericht

                      BESCHWERDE GEGEN DIE SCHUBHAFT
                      gemäß §22a Abs 1 BFA-VG

[...Rubrum...]

Der Beschwerdeführer befindet sich seit [Datum] in Schubhaft im
[Polizeianhaltezentrum / Ort].

Beschwerdegründe:

1.  Unverhältnismäßigkeit der Schubhaft (§76 Abs 2 FPG)
    - Gelinderes Mittel (§77 FPG) wäre ausreichend
    - Keine Fluchtgefahr / Fluchtgefahr nicht hinreichend begründet

2.  [Keine realistische Möglichkeit der Abschiebung innerhalb
    der gesetzlichen Frist]

3.  [Besondere Umstände: Minderjährigkeit, Krankheit, Familie]

ANTRÄGE:
1.  Die Schubhaft für rechtswidrig zu erklären;
2.  Die Anhaltung in Schubhaft aufzuheben;
3.  Den Bund zum Kostenersatz gemäß §35 VwGVG zu verpflichten.
```

#### Für Antrag auf aufschiebende Wirkung (§18 Abs 5 BFA-VG):

**FRIST: 1 Woche ab Zustellung!** Separat oder in der Beschwerde:

```
ANTRAG AUF ZUERKENNUNG DER AUFSCHIEBENDEN WIRKUNG
gemäß §18 Abs 5 BFA-VG

Die aufschiebende Wirkung der Beschwerde wurde im angefochtenen
Bescheid gemäß §18 Abs 1 Z [X] BFA-VG aberkannt.

Die Zuerkennung der aufschiebenden Wirkung ist geboten, weil:

1.  Dem Beschwerdeführer bei einer Abschiebung eine reale Gefahr
    einer Verletzung von Art [2/3/8] EMRK droht, weil [Begründung].

2.  Die Beschwerde nicht aussichtslos ist, weil [kurze Darlegung
    der Erfolgsaussichten].

3.  Die Interessensabwägung zugunsten des Beschwerdeführers ausfällt,
    weil [Begründung — irreversibler Schaden vs. öffentliches Interesse].
```

---

## Step 6: Present with Timeline, Next Steps, and Risk Assessment

```markdown
# Beschwerde-Analyse: Asyl-/Fremdenrecht

**Bescheid:** BFA-Bescheid vom [Datum], Zl. [GZ]
**Zustellung:** [Datum]
**Beschwerdefrist:** [Fristende mit Berechnung]
**Verbleibende Tage:** [n] Tage

## DRINGENDE WARNUNG

[NUR wenn Frist <7 Tage oder bereits abgelaufen — in großer Schrift]
[Bei abgelaufener Frist: Wiedereinsetzungsantrag prüfen, §33 VwGVG]

## Bescheid-Zusammenfassung

**Entscheidung des BFA:**
- Spruchpunkt I: [Was wurde entschieden]
- Spruchpunkt II: [Was wurde entschieden]
- Spruchpunkt III: [Was wurde entschieden]

**Zentrale Begründung des BFA:**
[Zusammenfassung der BFA-Argumentation in 3-5 Sätzen]

## Beschwerdegründe — Erfolgsaussichten

### Verfahrensmängel
| Mangel | Schwere | Relevanz | Erfolgsaussicht |
|--------|---------|----------|-----------------|
| [Mangel 1] | Hoch/Mittel/Gering | [Auswirkung auf Ergebnis] | [Einschätzung] |

### Beweiswürdigung
| Angegriffener Punkt | BFA-Argumentation | Gegenargument | Erfolgsaussicht |
|---------------------|-------------------|---------------|-----------------|
| [Punkt 1] | [BFA sagt...] | [Dagegen spricht...] | [Einschätzung] |

### Länderfeststellungen
| Problem | Details | Aktuelle Gegenquellen |
|---------|---------|----------------------|
| [Veraltet/Einseitig/Fehlend] | [Details] | [EASO/UNHCR/ACCORD — Datum] |

### Rechtliche Beurteilung
| Rechtsfehler | §§ | Relevante Judikatur |
|-------------|-----|---------------------|
| [Fehler 1] | §[x] AsylG/FPG | VwGH [GZ]: [Rechtssatz] |

## Gesamteinschätzung

**Erfolgsaussicht der Beschwerde:** Hoch (70-90%) / Mittel (40-70%) / Gering (<40%)

**Begründung:** [2-3 Sätze, warum diese Einschätzung]

**Wahrscheinlichstes Ergebnis beim BVwG:**
- [x]% Stattgebung (Status zuerkannt)
- [x]% Zurückverweisung an BFA (neues Verfahren)
- [x]% Abweisung (dann Revision/VfGH prüfen)

## BVwG-Verhandlung

**Mündliche Verhandlung:** [Wahrscheinlich ja — BVwG muss grundsätzlich verhandeln, §21 Abs 7 BFA-VG]
**Vorbereitung:**
- [ ] Dolmetscher in der richtigen Sprache sicherstellen
- [ ] Aktuelle Länderfeststellungen vorbereiten
- [ ] Beweismittel ordnen und Beilagenverzeichnis erstellen
- [ ] Konsistentes Vorbringen mit dem Beschwerdeführer besprechen
- [ ] Ggf. Sachverständigengutachten beantragen (medizinisch, länderspezifisch)

## Weitere Rechtsmittel (falls BVwG abweist)

### Revision an VwGH (Art 133 Abs 4 B-VG)
- **Frist:** 6 Wochen ab Zustellung des BVwG-Erkenntnisses
- **Voraussetzung:** Grundsätzliche Bedeutung einer Rechtsfrage
- **Anwaltspflicht:** Ja (§24 Abs 2 VwGG)
- **Verfahrenshilfe:** Möglich (§61 VwGG)
- **Typische Revisionsgründe:**
  - BVwG weicht von VwGH-Rechtsprechung ab
  - Fehlende Rechtsprechung zu einer entscheidenden Frage
  - Uneinheitliche Rechtsprechung des BVwG

### Beschwerde an VfGH (Art 144 B-VG)
- **Frist:** 6 Wochen ab Zustellung des BVwG-Erkenntnisses
- **Voraussetzung:** Verletzung in verfassungsgesetzlich gewährleisteten Rechten
- **Anwaltspflicht:** Ja (§17 Abs 2 VfGG)
- **Verfahrenshilfe:** Möglich (§64 ZPO analog)
- **Typische Beschwerdegründe:**
  - Art 3 EMRK — Refoulement-Verbot
  - Art 8 EMRK — Privat- und Familienleben
  - Art 13 EMRK — Recht auf wirksame Beschwerde
  - Gleichheitsgrundsatz (Art 7 B-VG, Art 2 StGG)
  - Willkürverbot

## Folgeantrag-Strategie (falls alle Rechtsmittel erschöpft)

**Voraussetzung (§68 Abs 1 AVG):** Neuer Sachverhalt (nova producta oder nova reperta), der die Rechtskraft durchbricht.

| Möglicher neuer Sachverhalt | Typ | Tauglichkeit |
|-----------------------------|-----|-------------|
| [Verschlechterung der Lage im Herkunftsstaat] | nova producta | [Einschätzung] |
| [Neue persönliche Umstände (Krankheit, Familie)] | nova producta | [Einschätzung] |
| [Aufgetauchte Beweismittel] | nova reperta | [Einschätzung] |

**Achtung:** Folgeantrag ohne tauglichen neuen Sachverhalt → faktischer Abschiebeschutz kann aberkannt werden (§12a AsylG 2005)!

## Säumnisbeschwerde (§8 VwGVG)

**Wenn BFA nicht entscheidet:** Nach 6 Monaten ab Antragstellung kann Säumnisbeschwerde an das BVwG erhoben werden.
- Frist: Frühestens 6 Monate nach Antrag
- Wirkung: BVwG entscheidet selbst oder trägt dem BFA Entscheidung auf

## Zeitplan

| Schritt | Frist | Datum |
|---------|-------|-------|
| Beschwerde einbringen | [4 Wochen / 2 Wochen] | [Datum] |
| Antrag aufschiebende Wirkung | [1 Woche — falls nötig] | [Datum] |
| BVwG-Entscheidung (erwartet) | ca. 3-12 Monate | [geschätzt] |
| Revision/VfGH (falls nötig) | 6 Wochen nach BVwG | [abhängig] |

## Nächste Schritte

- [ ] [DRINGEND: Beschwerdefrist beachten — Beschwerde bis [Datum] einbringen]
- [ ] [Rechtsberatung/Rechtsvertretung kontaktieren (BBU, Diakonie, Caritas, RA)]
- [ ] [Beweismittel sammeln und ordnen]
- [ ] [Aktuelle Länderfeststellungen recherchieren]
- [ ] [Ggf. Antrag auf aufschiebende Wirkung SOFORT einbringen]
- [ ] [Ggf. Verfahrenshilfe beantragen]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | Verfügbar / Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Länderfeststellungen | [Quelle und Datum] | |
| Prüfdatum | [YYYY-MM-DD] | |

---
**Keine Rechtsberatung.** Diese Analyse dient der rechtlichen Ersteinschätzung und ersetzt nicht die Beratung durch einen Rechtsanwalt oder eine anerkannte Rechtsberatungsorganisation. Im Asylverfahren besteht das Recht auf kostenlose Rechtsberatung und Rechtsvertretung im Beschwerdeverfahren durch die BBU (Bundesagentur für Betreuungs- und Unterstützungsleistungen) gemäß §52 BFA-VG. Bei Revision an den VwGH oder Beschwerde an den VfGH besteht Anwaltspflicht — Verfahrenshilfe ist möglich.
```

---

## Critical Rules

1. **Fristen sind das Allerwichtigste. Eine versäumte Beschwerdefrist bedeutet Rechtskraft des negativen Bescheids und ermöglicht die Abschiebung.** Berechne jede Frist auf den Tag genau. Frage IMMER nach dem Zustelldatum, wenn es nicht angegeben ist.
2. **This area affects people's fundamental rights and safety. Be especially thorough. Never understate risks. Always flag if a deadline is imminent — missing a Beschwerdefrist in asylum can mean deportation.**
3. **Aufschiebende Wirkung sofort prüfen** — Wenn die aufschiebende Wirkung aberkannt wurde (§18 BFA-VG), ist der Antrag auf Zuerkennung innerhalb von 1 Woche die dringendste Handlung. Ohne aufschiebende Wirkung kann die Abschiebung sofort vollzogen werden.
4. **Always cite specific §§** — §7 BFA-VG, §9 VwGVG, §18 Abs 5 BFA-VG. Never vaguely reference "the law."
5. **Eventualanträge in der Beschwerde** — Immer gestaffelt: Asyl → subsidiärer Schutz → §55 AsylG → Zurückverweisung. Nie nur einen Antrag stellen.
6. **Länderfeststellungen sind zentral** — Die meisten erfolgreichen Beschwerden greifen veraltete oder einseitige Länderfeststellungen an. Immer aktuelle EASO/EUAA-, UNHCR- und ACCORD-Quellen einbringen.
7. **Art 3 EMRK ist absolut** — Keine Ausnahmen, keine Abwägung. Auch bei straffälligen Personen gilt das Refoulement-Verbot uneingeschränkt.
8. **Mündliche Verhandlung beantragen** — Das BVwG muss grundsätzlich verhandeln. Den Antrag immer in die Beschwerde aufnehmen (§21 Abs 7 BFA-VG, Art 47 GRC).
9. **Kostenlose Rechtsvertretung hinweisen** — Im Beschwerdeverfahren besteht Anspruch auf kostenlose Rechtsvertretung durch die BBU. Bei VwGH/VfGH: Verfahrenshilfe beantragen.
10. **Match user's language** — German in, German out. English in, English out. Statutes always in German form.
11. **Use RIS if connected** — Verify VwGH/VfGH case law and statute citations are current.
12. **Wiedereinsetzung bei versäumter Frist** — Wenn die Frist abgelaufen ist, sofort §33 VwGVG prüfen. Voraussetzung: unabwendbares oder unvorhergesehenes Ereignis, kein grobes Verschulden. Frist für Wiedereinsetzungsantrag: 2 Wochen ab Wegfall des Hindernisses.
