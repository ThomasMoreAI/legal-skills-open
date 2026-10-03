---
name: recht-asyl-momarcode1
title: /recht asyl — Asyl- und Fremdenrecht (Advisory)
description: Austrian asylum and immigration law analysis — asylum procedure (AsylG 2005), residence permits (NAG), deportation protection (FPG), subsidiary protection (§8 AsylG), BFA proceedings, family reunification, and Red-White-Red Card (RWR-Karte). Analyzes protection claims, residence status, and legal options.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-asyl
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: immigration
language: de
sources:
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht asyl — Asyl- und Fremdenrecht (Advisory)

When the user describes an asylum, immigration, or residence situation, follow these steps exactly.

---

## Step 1: Read the Facts / Documents

Read everything the user has provided. You need:

1. **Who?** — Nationality, age, family situation (unbegleiteter Minderjähriger? Familie mit Kindern?), current status (Asylwerber, subsidiär Schutzberechtigter, Aufenthaltstitel-Inhaber, undokumentiert?)
2. **What happened?** — Fluchtgründe (persecution, war, threats), or immigration context (work, study, family)
3. **When?** — Arrival date, Antragsdatum, Bescheid dates, any pending deadlines
4. **Current procedural status?** — Erstantrag, Folgeantrag, Beschwerde pending, Rückkehrentscheidung, Schubhaft?
5. **What documents exist?** — BFA-Bescheid, Ladung, Verhandlungsprotokoll, Aufenthaltstitel, Arbeitgeberbescheinigung, Deutschzertifikate?

If any critical element is missing, ask. Be specific:
> "Wann haben Sie den Asylantrag gestellt? Das Datum ist entscheidend für die Verfahrensdauer und mögliche Säumnisbeschwerde."
> "Haben Sie einen Bescheid vom BFA erhalten? Wenn ja, wann wurde er zugestellt?"

Do NOT begin analysis until you have enough facts.

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references (VwGH, VfGH, BVwG), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 3: Classify the Situation

Determine which legal framework applies. This controls the entire analysis:

### A: Internationaler Schutz (AsylG 2005)

- **Asyl (§3 AsylG 2005)** — Flüchtlingseigenschaft iSd GFK
  - Verfolgung aus Gründen der Rasse, Religion, Nationalität, Zugehörigkeit zu einer bestimmten sozialen Gruppe, politische Gesinnung
  - Verfolgung durch Staat ODER nichtstaatliche Akteure (wenn Staat nicht schutzfähig/-willig)
  - Interne Fluchtalternative prüfen (§11 AsylG 2005)
  - Ausschluss: §6 AsylG 2005 (schwere Verbrechen, Gefahr für Sicherheit)

- **Subsidiärer Schutz (§8 AsylG 2005)** — Wenn kein Asyl, aber:
  - Reale Gefahr einer Verletzung von Art 2 EMRK (Leben) oder Art 3 EMRK (Folter, unmenschliche Behandlung)
  - Ernsthafter Schaden: Todesstrafe, Folter, willkürliche Gewalt bei bewaffnetem Konflikt
  - Prüfung der Ländersituation (Länderberichte EASO/EUAA, UNHCR, ACCORD)

- **Aufenthaltstitel aus berücksichtigungswürdigen Gründen**
  - §55 AsylG 2005 — Aufenthaltsberechtigung (Art 8 EMRK Privat-/Familienleben)
  - §56 AsylG 2005 — Aufenthaltsberechtigung besonderer Schutz (Opfer von Gewalt, Menschenhandel)
  - §57 AsylG 2005 — Aufenthaltsberechtigung besonderer Schutz (ex officio)

- **Dublin-III-Verordnung (EU 604/2013)**
  - Zuständigkeit eines anderen EU-Mitgliedstaats
  - Selbsteintrittsrecht Österreichs (Art 17 Dublin-III-VO)
  - Familienzusammenführung innerhalb Dublin (Art 8-11)
  - Systemische Mängel im zuständigen Staat → keine Überstellung (VfGH-Judikatur)

### B: Aufenthaltsrecht (NAG)

- **Rot-Weiß-Rot-Karte (§41 NAG)** — Schlüsselkräfte, Fachkräfte in Mangelberufen, Studienabsolventen, Start-up-Gründer, sonstige Schlüsselkräfte
- **Rot-Weiß-Rot-Karte plus (§41a NAG)** — Freier Arbeitsmarktzugang, nach 2 Jahren RWR-Karte oder Familienangehörige
- **Blaue Karte EU (§42 NAG)** — Hochqualifizierte Beschäftigung
- **Familienangehörige (§§46-47 NAG)** — Familiennachzug für Drittstaatsangehörige
- **Daueraufenthalt EU (§45 NAG)** — Nach 5 Jahren rechtmäßigem Aufenthalt
- **Studierende (§64 NAG)** — Aufenthaltsbewilligung Studierender
- **Niederlassungsbewilligung (§43 NAG)** — Verschiedene Zwecke

### C: Fremdenpolizeirecht (FPG)

- **Rückkehrentscheidung (§52 FPG)** — Anordnung zur Ausreise
- **Einreiseverbot (§53 FPG)** — Befristetes/unbefristetes Einreiseverbot
- **Aufenthaltsverbot (§67 FPG)** — Für EWR-Bürger/Schweizer/begünstigte Drittstaatsangehörige
- **Schubhaft (§76 FPG)** — Freiheitsentziehung zur Sicherung der Abschiebung
- **Gelinderes Mittel (§77 FPG)** — Meldepflicht, Unterkunftnahme statt Schubhaft
- **Duldung (§46a FPG)** — Wenn Abschiebung rechtlich/tatsächlich unmöglich
- **Abschiebeschutz (§12 AsylG 2005)** — Faktischer Abschiebeschutz während des Verfahrens

### D: Grundversorgung und Integration

- **GVG-B (Grundversorgungsgesetz-Bund)** — Unterbringung, Verpflegung, Krankenversicherung, Taschengeld während des Asylverfahrens
- **IntG (Integrationsgesetz 2017)** — Integrationsprüfung (Sprache + Werte), Wertekurse, Deutsch A2/B1 Pflicht
- **Integrationsvereinbarung (§7 IntG)** — Pflicht für alle Aufenthaltstitel >12 Monate

---

## Step 4: Analyze Applicable Claims and Options

Based on the classification from Step 3, analyze systematically:

### For Asyl (§3 AsylG 2005):

1. **Wohlbegründete Furcht vor Verfolgung** — Liegt eine aktuelle, individuelle Bedrohung vor?
2. **Verfolgungsgrund nach GFK** — Welcher der 5 Gründe (Rasse, Religion, Nationalität, soziale Gruppe, politische Gesinnung)?
3. **Verfolgungsakteur** — Staatlich oder nichtstaatlich? Bei nichtstaatlich: Schutzfähigkeit/-willigkeit des Herkunftsstaats?
4. **Interne Fluchtalternative (§11 AsylG)** — Zumutbare Niederlassung in einem anderen Teil des Herkunftsstaats?
5. **Ausschlussgründe (§6 AsylG)** — Schwere Verbrechen? Gefahr für Sicherheit?
6. **Glaubwürdigkeit** — Ist das Vorbringen in sich schlüssig, detailliert, mit Länderfeststellungen vereinbar?

### For Subsidiären Schutz (§8 AsylG 2005):

1. **Reale Gefahr** — Art 3 EMRK: Folter, unmenschliche/erniedrigende Behandlung oder Strafe?
2. **Ländersituation** — Aktuelle EASO/EUAA-Berichte, UNHCR-Positionen, Länderinformationsblatt der Staatendokumentation?
3. **Individualisierung** — Individuelle Betroffenheit bei genereller Gewalt (EuGH C-465/07, Elgafaji)?
4. **Medizinische Gründe** — §8 Abs 1 letzter Satz: Lebensbedrohliche Erkrankung ohne Behandlung im Herkunftsstaat?
5. **Vulnerable Gruppen** — Minderjährige, Schwangere, Alte, Kranke, Opfer von Folter?

### For Art 8 EMRK Prüfung (§55 AsylG / §52 Abs 9 FPG):

1. **Privatleben** — Aufenthaltsdauer, Deutschkenntnisse, Arbeit, Selbsterhaltungsfähigkeit, strafrechtliche Unbescholtenheit, soziale Integration
2. **Familienleben** — Familienmitglieder in Österreich (Ehepartner, Kinder, Eltern), Grad der Abhängigkeit
3. **Interessensabwägung** — Private Interessen vs. öffentliches Interesse an Aufenthaltsbeendigung
4. **VfGH-Kriterienkatalog** — E 29.9.2007, B 328/07: Aufenthaltsdauer, Alter, Familiensituation, Integration, Bindungen zum Herkunftsstaat

### For NAG-Aufenthaltstitel:

1. **Allgemeine Erteilungsvoraussetzungen (§11 NAG)** — Keine Gefährdung der öffentlichen Ordnung, gesicherter Lebensunterhalt, ortsübliche Unterkunft, Krankenversicherung
2. **Besondere Voraussetzungen** — Je nach Aufenthaltstitel (RWR-Karte: Punkte, Arbeitsplatzangebot; Studenten: Studienzulassung etc.)
3. **Quotenpflicht** — Welche Titel sind quotenpflichtig, welche nicht?
4. **Integrationsvereinbarung** — Modul 1 (A2 + Wertekurs), Modul 2 (B1) per IntG
5. **Familienzusammenführung** — Wartezeit, Einkommensnachweis, Wohnungsgröße

---

## Step 5: Identify Deadlines and Procedural Requirements

**This is critical. Missing deadlines in asylum law can mean deportation.**

| Situation | Frist | Grundlage |
|-----------|-------|-----------|
| Beschwerde gegen negativen Asyl-Bescheid | **4 Wochen** ab Zustellung | §7 Abs 4 BFA-VG |
| Beschwerde gegen Dublin-Bescheid | **2 Wochen** ab Zustellung | §16 Abs 1 BFA-VG |
| Beschwerde gegen Schubhaft | **Jederzeit**, keine Frist | §22a BFA-VG |
| Beschwerde bei aberkannter aufschiebender Wirkung | **1 Woche** für Antrag auf Zuerkennung | §18 Abs 5 BFA-VG |
| Folgeantrag bei neuen Fluchtgründen | **Unverzüglich** nach Bekanntwerden | §2 Abs 1 Z 23 AsylG |
| NAG-Verlängerungsantrag | **Vor Ablauf** des bestehenden Titels | §24 Abs 1 NAG |
| Aufenthaltstitel-Erstantrag | Vom Ausland (Botschaft), Ausnahmen §21 Abs 2 NAG | §21 NAG |
| Integrationsvereinbarung Modul 1 | **2 Jahre** ab Erteilung Aufenthaltstitel | §7 Abs 2 IntG |

**Flag every deadline within 30 days prominently at the top of the output.**

---

## Step 6: Present with Strategy and Next Steps

```markdown
# Asyl- und Fremdenrechtliche Analyse

**Person:** [Nationalität, Alter, Familienstand]
**Aktueller Status:** [Asylwerber / subsidiär Schutzberechtigter / Aufenthaltstitel XY / ohne Aufenthaltstitel]
**Verfahrensstand:** [Erstverfahren / Beschwerdeverfahren / rechtskräftig abgeschlossen / etc.]
**Rechtsgebiet(e):** [AsylG / FPG / NAG / Dublin-III-VO]

## Sofort-Warnungen

[Imminent deadlines, deportation risks, Schubhaft-Gefahr, ablaufender Abschiebeschutz]

## Situationsanalyse

### Rechtlicher Rahmen
[Applicable laws with §§ citations]

### Ansprüche und Optionen

#### Option 1: [Name — z.B. Asyl nach §3 AsylG]
| Element | Status | Begründung |
|---------|--------|-----------|
| [Tatbestandsmerkmal 1] | Erfüllt / Fraglich / Nicht erfüllt | [Begründung] |
| [Tatbestandsmerkmal 2] | Erfüllt / Fraglich / Nicht erfüllt | [Begründung] |

**Erfolgsaussicht:** Hoch (70-90%) / Mittel (40-70%) / Gering (<40%)
**Begründung:** [Warum diese Einschätzung]

#### Option 2: [Name — z.B. Subsidiärer Schutz nach §8 AsylG]
[Same structure]

#### Option 3: [Name — z.B. Aufenthaltstitel nach §55 AsylG]
[Same structure]

## Länderfeststellungen

**Herkunftsstaat:** [Land]
**Relevante Quellen:** [EASO/EUAA, UNHCR, Länderinformationsblatt BFA, ACCORD]
**Kernaussagen:** [Key findings relevant to the case]

## Art 8 EMRK Abwägung (falls relevant)

| Kriterium | Bewertung | Details |
|-----------|-----------|---------|
| Aufenthaltsdauer | [x Jahre] | |
| Deutschkenntnisse | [A1/A2/B1/B2] | [Nachweis vorhanden?] |
| Erwerbstätigkeit | [Ja/Nein] | [Selbsterhaltungsfähigkeit?] |
| Familiäre Bindungen AT | [Details] | |
| Bindungen Herkunftsstaat | [Details] | |
| Strafrechtliche Unbescholtenheit | [Ja/Nein] | |
| Gesamtbewertung | [Interesse überwiegt / knapp / öffentl. Interesse überwiegt] | |

## Fristen-Übersicht

| Frist | Datum | Handlung erforderlich | Konsequenz bei Versäumnis |
|-------|-------|----------------------|--------------------------|
| [Beschwerdefrist] | [Datum] | [Beschwerde einbringen] | [Bescheid rechtskräftig, Abschiebung möglich] |

## Empfohlene Strategie

### Priorität 1: [Dringendste Maßnahme]
- **Was:** [Konkrete Handlung]
- **Bis wann:** [Frist]
- **Begründung:** [Warum zuerst]

### Priorität 2: [Nächste Maßnahme]
[Same structure]

### Priorität 3: [Weitere Maßnahme]
[Same structure]

## Nächste Schritte

- [ ] [Erste konkrete Handlung — z.B. Rechtsberatung kontaktieren]
- [ ] [Zweite Handlung — z.B. Dokumente zusammenstellen]
- [ ] [Dritte Handlung — z.B. Deutschkurs-Nachweis besorgen]

## Wichtige Kontakte

- **Rechtsberatung:** [Diakonie Flüchtlingsdienst, Caritas, Volkshilfe, Verein Menschenrechte Österreich — je nach Bundesland]
- **UNHCR Österreich:** Für Dublin-Fälle und besonders schutzbedürftige Personen
- **Kinder- und Jugendhilfe:** Bei unbegleiteten Minderjährigen

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | Verfügbar / Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Länderfeststellungen | [Quelle und Datum] | |
| Prüfdatum | [YYYY-MM-DD] | |

---
**Keine Rechtsberatung.** Diese Analyse dient der rechtlichen Ersteinschätzung und ersetzt nicht die Beratung durch einen Rechtsanwalt oder eine anerkannte Rechtsberatungsorganisation. Im Asylverfahren besteht das Recht auf kostenlose Rechtsberatung durch die BBU (Bundesagentur für Betreuungs- und Unterstützungsleistungen) gemäß §52 BFA-VG.
```

---

## Critical Rules

1. **This area affects people's fundamental rights and safety. Be especially thorough. Never understate risks. Always flag if a deadline is imminent — missing a Beschwerdefrist in asylum can mean deportation.**
2. **Always cite specific §§** — Never "Austrian immigration law says..." without the exact section. §3 AsylG 2005, not just "AsylG".
3. **Fristen sind lebenswichtig** — Calculate every deadline precisely. State the Zustelldatum and the resulting Fristende. If the Zustelldatum is unknown, ask for it immediately.
4. **Länderfeststellungen prüfen** — Never assess asylum claims without considering the current country situation. Reference EASO/EUAA, UNHCR, BFA-Staatendokumentation.
5. **Art 3 EMRK ist absolut** — There are NO exceptions to the prohibition of refoulement where Art 3 EMRK is at risk. Not even criminal convictions override this (VfGH E 13.12.2011, U 2241/10).
6. **Vulnerable Gruppen besonders beachten** — Unbegleitete Minderjährige (Kindeswohl, UN-KRK), Folteropfer, Traumatisierte, Schwangere erfordern besondere Verfahrensgarantien.
7. **Dublin ist komplex** — Always check: Familienbindungen, systemische Mängel im Zielstaat, Selbsteintrittsrecht, Fristablauf (6/18 Monate).
8. **Kostenlose Rechtsberatung hinweisen** — Im Asylverfahren besteht Anspruch auf kostenlose Rechtsberatung (BBU). Immer darauf hinweisen.
9. **Match user's language** — German in, German out. English in, English out. Statutes always in German form (§3 AsylG 2005).
10. **Use RIS if connected** — Verify statute citations and VwGH/VfGH case law are current.
