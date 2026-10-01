---
name: recht-schulden-momarcode1
title: /recht schulden — Schulden- und Insolvenzrecht (Advisory)
description: Austrian debt and insolvency law — debt management, Mahnverfahren, payment plans (Ratenzahlung), wage garnishment (Lohnpfaendung), existenzminimum, personal insolvency (Schuldenregulierungsverfahren), Schuldnerberatung, and debt collection (Inkasso).
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-schulden
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: bankruptcy
language: de
---

# /recht schulden — Schulden- und Insolvenzrecht (Advisory)

When the user has debt problems — unpaid bills, collection letters, wage garnishment, or needs information about personal insolvency — follow these steps exactly.

---

## Step 1: Gather the Facts

Read everything the user has provided. You need:

1. **What is the debt situation?** — Einzelne offene Rechnung, mehrere Glaeubiger, Mahnverfahren laufend, Exekution bereits eingeleitet, Inkassobuero involviert?
2. **How much?** — Gesamtschuldenhoehe, einzelne Forderungen aufschluesseln. Hauptforderung vs. Zinsen vs. Kosten.
3. **Who are the creditors?** — Private Glaeubiger, Banken, Finanzamt, Sozialversicherung, Vermieter?
4. **Income and assets** — Monatliches Nettoeinkommen, Sonderzahlungen (13./14. Gehalt), Vermoegenswerte (Immobilien, Fahrzeuge, Sparguthaben), Unterhaltspflichten (Kinder, Ehepartner)
5. **Employment status** — Unselbstaendig (Lohnpfaendung relevant), selbstaendig, arbeitslos, pensioniert?
6. **What has already happened?** — Mahnungen erhalten? Zahlungsbefehl? Exekutionsbewilligung? Lohnpfaendung laeuft bereits? Inkassoschreiben?
7. **Existing measures?** — Ratenzahlungsvereinbarung laeuft? Stundung beantragt? Schuldnerberatung kontaktiert?
8. **Personal situation** — Unterhaltspflichten (Anzahl und Alter der Kinder), Wohnsituation (Miete, Eigentum), gesundheitliche Einschraenkungen?

If critical information is missing, ask:
> "Wie hoch sind Ihre Gesamtschulden und bei wie vielen Glaeubigern? Das entscheidet, ob eine Einzelloesung oder ein Insolvenzverfahren sinnvoller ist."
> "Erhalten Sie bereits Lohnpfaendungen? Dann muessen wir das Existenzminimum berechnen."

Do NOT begin analysis until you have enough facts.

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references (OGH, OLG), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 2b: Evidence Assessment (if evidence provided)

If the user has provided documents, photos, emails, witness statements, or other evidence, follow the **Evidence Protocol** (`references/evidence-protocol.md`):
1. Classify each piece of evidence by ZPO hierarchy (Urkunden > Zeugen > Sachverstaendige > Augenschein > Parteienvernehmung)
2. Assess Beweiskraft (probative value) of each piece
3. Identify evidence gaps — what is missing to prove the claim?
4. Determine Beweislast — who must prove what in this situation?
5. Recommend what additional evidence to gather
6. Flag any Beweisnotstand or evidence at risk of loss

If no evidence is provided, skip this step.

---

## Step 3: Classify the Situation

Determine the phase and legal context of the debt problem. Go through this systematically:

### A: Mahnung und Verzug (§§1333-1335 ABGB)

**Verzug:** Der Schuldner kommt in Verzug, wenn er die faellige Leistung nicht zum Faelligkeitstermin erbringt (§1334 ABGB).

**Mahnung:**
- Mahnung ist grundsaetzlich NICHT erforderlich, wenn ein Faelligkeitstermin bestimmt ist (§1334 ABGB: "dies interpellat pro homine")
- Bei unbestimmter Faelligkeit: Mahnung setzt Verzug in Gang
- Mahnkosten: Nur die tatsaechlich entstandenen Kosten sind ersatzfaehig. Pauschale "Mahnspesen" in AGB muessen angemessen sein (§6 KSchG).

**Verzugszinsen:**
- Gesetzlich: 4% p.a. (§1333 Abs 1 ABGB)
- Unternehmergeschaeft (B2B): 9,2% ueber Basiszinssatz (§456 UGB)
- Vertragliche Verzugszinsen: zulaessig, aber Wuchergrenzen (§879 Abs 2 Z 4 ABGB) und bei B2C §6 KSchG beachten

### B: Inkassounternehmen und Inkassokosten

**Zulaessigkeit von Inkasso:**
- Glaeubiger darf ein Inkassobuero beauftragen
- Inkassokosten sind grundsaetzlich als Verzugsschaden ersatzfaehig — ABER nur im angemessenen Rahmen

**Inkassokostenbegrenzung:**
- §1333 Abs 2 ABGB: Verbraucher schuldet nur die zur zweckentsprechenden Betreibung notwendigen Kosten
- BGBLA 2013/IIO Nr. 100 — Standesregeln fuer Inkassobüros
- OGH-Judikatur: Ueberhöhte Inkassokosten sind nicht erstattungsfaehig
- Haeufige unzulaessige Positionen: "Bearbeitungsgebuehr" vor erster Mahnung, ueberhöhte Mahnpauschalen, "Kontoführungsgebuehr"

**Was tun bei Inkassoschreiben:**
1. Pruefen: Besteht die Forderung ueberhaupt?
2. Pruefen: Sind die Inkassokosten angemessen?
3. Pruefen: Ist die Forderung vielleicht verjaehrt?
4. NICHT ignorieren — aber auch nicht vorschnell alles zahlen

### C: Mahnverfahren (§§244ff ZPO)

**Ablauf:**
1. Glaeubiger stellt Antrag auf Zahlungsbefehl (§244 ZPO)
2. Gericht erlässt Zahlungsbefehl OHNE Prüfung der Berechtigung der Forderung (§247 ZPO)
3. Zustellung an den Schuldner
4. **Einspruchsfrist: 4 Wochen** ab Zustellung (§252 Abs 1 ZPO)

**KRITISCH — Einspruch:**
- Einspruch muss innerhalb von **4 Wochen** beim Gericht einlangen (§252 ZPO)
- Einspruch braucht KEINE Begruendung (§252 Abs 1 ZPO) — aber Begruendung ist sinnvoll
- Bei Einspruch: ordentliches Verfahren (Klage)
- **Ohne Einspruch: Zahlungsbefehl wird RECHTSKRAEFTIG und ist Exekutionstitel!**
- Versaeumter Einspruch → Wiedereinsetzung in den vorigen Stand (§146 ZPO) nur bei unverschuldetem Versaeumnis

**Versaeumnisurteil (§396 ZPO):**
- Wenn der Beklagte zur muendlichen Verhandlung nicht erscheint
- Auch ein Versaeumnisurteil wird Exekutionstitel

### D: Lohnpfaendung / Gehaltspfaendung (§§290ff EO, ExGEO)

**Ablauf:**
1. Glaeubiger hat Exekutionstitel (rechtskraeftiger Zahlungsbefehl, Urteil, etc.)
2. Glaeubiger beantragt Forderungsexekution (§294 EO)
3. Gericht erlässt Exekutionsbewilligung
4. Drittschuldner (Arbeitgeber) wird angewiesen, den pfaendbaren Teil des Gehalts an den Glaeubiger abzufuehren

**Existenzminimum (Unpfaendbarer Freibetrag):**
- Geregelt in der **Existenzminimum-Verordnung (ExGEO)** — wird jaehrlich angepasst
- Berechnung abhaengig von:
  - Nettoeinkommen (inkl. Sonderzahlungen anteilig)
  - Anzahl der Unterhaltspflichten (unterhaltsberechtigte Personen)
  - Art des Einkommens (Arbeitseinkommen, Pension, etc.)
- **Unpfaendbare Bezuege (§290a EO):**
  - Familien-/Kinderbeihilfe
  - Pflegegeld
  - Wohnbeihilfe
  - Aufwandsentschaedigungen (soweit nicht Einkommen)
- **Erhöhter Pfaendungsschutz:** Bei besonderem Bedarf (z.B. Krankheit, Behinderung) kann das Gericht den unpfaendbaren Betrag erhoehen (§292a EO)

**Berechnung des pfaendbaren Betrags:**
- Grundbetrag (unpfaendbar) + Unterhaltsstaffeln (je unterhaltsberechtigte Person)
- Der Betrag ueber dem Existenzminimum ist zu je einem Drittel pfaendbar ("Drittelloesung"):
  - Unteres Drittel: pfaendbar fuer alle Forderungen
  - Mittleres Drittel: pfaendbar fuer privilegierte Forderungen (Unterhalt, Schadenersatz aus Koerperverletzung)
  - Oberes Drittel: unpfaendbar (Anreizteil)
- Aktuelle ExGEO-Tabellen muessen herangezogen werden — Werte aendern sich jaehrlich!

### E: Verbraucherinsolvenz / Schuldenregulierungsverfahren (§§181ff IO)

**Wann sinnvoll:**
- Schuldner ist zahlungsunfaehig (nicht bloss in voruebergehender Zahlungsstockung)
- Mehrere Glaeubiger
- Keine realistische Moeglichkeit, die Schulden durch Einzelvereinbarungen zu tilgen
- Bereitschaft, 3 Jahre lang den pfaendbaren Einkommensteil abzugeben

**Ablauf:**

1. **Vorbereitung (Schuldnerberatung)**
   - Kontakt mit staatlich anerkannter Schuldnerberatung (kostenlos!)
   - Erstellen eines Glaeubiger-/Schuldenverzeichnisses
   - Zusammenstellung aller Unterlagen

2. **Aussergerichtlicher Ausgleichsversuch (§183 IO)**
   - MUSS vor dem Insolvenzantrag versucht werden (Voraussetzung!)
   - Vorschlag an alle Glaeubiger (z.B. Quotenvergleich)
   - Scheitert, wenn auch nur ein Glaeubiger ablehnt
   - Schuldnerberatungsstelle stellt Bestaetigung ueber das Scheitern aus

3. **Insolvenzantrag (§183 IO)**
   - Einbringung beim zustaendigen Bezirksgericht (als Insolvenzgericht)
   - Dem Antrag beizufuegen: Vermoegensverzeichnis, Glaeubigerverzeichnis, Einkommensnachweise, Bestaetigung ueber gescheiterten aussergerichtlichen Ausgleich

4. **Zahlungsplan (§193 IO) — Option 1 (bevorzugt)**
   - Schuldner bietet den Glaeubigern eine Quote an (z.B. 30% innerhalb von 5 Jahren)
   - Annahme: Mehrheit der Glaeubiger (Kopf- UND Summenmehrheit, §147 Abs 1 IO analog)
   - Mindestquote: KEINE gesetzliche Mindestquote mehr (seit Novelle)
   - Bei Annahme: Restschuld erlischt nach Erfuellung des Zahlungsplans
   - Maximale Laufzeit: 7 Jahre (§194 Abs 1 IO)

5. **Abschoepfungsverfahren (§199 IO) — Option 2 (wenn Zahlungsplan scheitert)**
   - Schuldner tritt den pfaendbaren Teil seines Einkommens fuer **3 Jahre** an einen Treuhänder ab (§199 Abs 2 IO — seit Novelle 2021, zuvor 5 Jahre, dann 3 Jahre gemäss Umsetzung der RL (EU) 2019/1023)
   - Keine Mindestquote erforderlich
   - Obliegenheiten waehrend des Abschoepfungsverfahrens (§210 IO):
     - Angemessene Erwerbstaetigkeit ausueben oder sich darum bemuehen
     - Kein neues Vermoegen verheimlichen
     - Erbschaften zur Haelfte herausgeben
     - Wohnortwechsel und Arbeitgeberwechsel dem Gericht melden
     - Keine neuen Schulden eingehen
   - Verletzung der Obliegenheiten → Einstellung des Verfahrens (§211 IO)

6. **Restschuldbefreiung (§213 IO)**
   - Nach Abschluss des Zahlungsplans oder Abschoepfungsverfahrens
   - Gericht erteilt Beschluss ueber Restschuldbefreiung
   - Restschuld erlischt — Neustart (fresh start)
   - Ausnahme: Bestimmte Forderungen sind von Restschuldbefreiung ausgenommen (z.B. Forderungen aus vorsaetzlich begangenen unerlaubten Handlungen, §215 Abs 2 IO)

### F: Schuldnerberatung (Landesberatungsstellen)

**Staatlich anerkannte Schuldnerberatungsstellen:**
- In jedem Bundesland vorhanden
- **Kostenlos** fuer Betroffene
- Leistungen:
  - Erstberatung und Schuldenanalyse
  - Haushaltsbudget erstellen
  - Verhandlung mit Glaeubigern (Ratenzahlung, Stundung, Vergleich)
  - Begleitung durch das Insolvenzverfahren
  - Praevention und Nachbetreuung
- Dachverband: ASB Schuldnerberatungen GmbH (asb-gmbh.at)

**Kontakt:**
- Wien: Schuldenberatung Wien
- Niederoesterreich: Schuldnerberatung NOE
- Oberoesterreich: Schuldnerberatung OOE
- Und so weiter — in jedem Bundesland

---

## Step 4: Analyse and Prioritize

For the identified situation, determine:

### Sofort-Analyse:
1. **Verjaehrung pruefen** — Ist eine Forderung vielleicht verjaehrt?
   - Allgemeine Verjaehrung: 3 Jahre (§1489 ABGB — Schadenersatz), 30 Jahre (§1478 ABGB — allgemein)
   - Kurzfristige Forderungen: 3 Jahre fuer rueckstaendige Zinsen, Mietzins, wiederkehrende Leistungen (§1480 ABGB)
   - Verjaehrte Forderung → Einrede erheben! Gericht prueft Verjaehrung NICHT von Amts wegen.

2. **Forderung berechtigt?**
   - Besteht die Forderung ueberhaupt?
   - Stimmt die Hoehe?
   - Sind die Nebenforderungen (Zinsen, Inkassokosten, Mahnspesen) angemessen?

3. **Existenzminimum sichern**
   - Bei Lohnpfaendung: Ist das Existenzminimum korrekt berechnet?
   - Sind alle Unterhaltspflichten beruecksichtigt?
   - Werden unpfaendbare Bezuege dennoch gepfaendet? (rechtswidrig!)

4. **Insolvenz sinnvoll?**
   - Gesamtschulden vs. realistisch tilgbare Summe in 3-5 Jahren
   - Mehrere Glaeubiger → Insolvenz oft effizienter als Einzelverhandlungen
   - Einzelner Glaeubiger → Ratenzahlung/Vergleich direkt verhandeln

---

## Step 5: Present Results

```markdown
# Schuldenrechtliche Analyse

**Sachverhalt:** [2-3 Saetze Zusammenfassung]
**Gesamtschulden:** EUR [Betrag]
**Anzahl Glaeubiger:** [n]
**Aktuelles Nettoeinkommen:** EUR [Betrag] / Monat
**Unterhaltspflichten:** [n] Personen

## Schuldenübersicht

| Glaeubiger | Forderung | Zinsen/Kosten | Gesamt | Status | Verjaehrung |
|-----------|-----------|---------------|--------|--------|-------------|
| [Name] | EUR [x] | EUR [x] | EUR [x] | [offen/Exekution/etc.] | [Datum] |
| **Summe** | | | **EUR [x]** | | |

## Existenzminimum-Berechnung

| Position | Betrag |
|----------|--------|
| Nettoeinkommen | EUR [x] |
| Unpfaendbarer Grundbetrag (ExGEO) | EUR [x] |
| + Unterhaltsstaffel (x Personen) | EUR [x] |
| = Existenzminimum | **EUR [x]** |
| Pfaendbarer Betrag | **EUR [x]** |

Hinweis: Die aktuellen ExGEO-Werte muessen geprueft werden — sie werden jaehrlich angepasst.

## Rechtliche Beurteilung

### Einzelforderungs-Pruefung
[Fuer jede wesentliche Forderung:]
- **Berechtigung:** Forderung besteht / besteht nicht / teilweise
- **Hoehe:** Angemessen / ueberhoeht (Inkassokosten, Zinsen)
- **Verjaehrung:** Nicht verjaehrt / moeglicherweise verjaehrt (§[x] ABGB)
- **Status:** Offen / tituliert / in Exekution

### Gesamteinschaetzung
[Realistisch: Koennen die Schulden ohne Insolvenz getilgt werden?]

## Handlungsempfehlung

### Sofortige Schritte
1. [z.B. "Schuldnerberatung kontaktieren — kostenlos und vertraulich"]
2. [z.B. "Existenzminimum ueberpruefen lassen — moeglicherweise zu viel gepfaendet"]
3. [z.B. "Einspruch gegen Zahlungsbefehl — Frist laeuft am [Datum] ab!"]

### Empfohlener Weg
| Option | Vorteile | Nachteile |
|--------|----------|-----------|
| Ratenzahlung (einzeln) | Kein Insolvenzverfahren | Nur bei wenigen Glaeubigern praktikabel |
| Aussergerichtlicher Ausgleich | Schneller, diskreter | Alle Glaeubiger muessen zustimmen |
| Zahlungsplan (§193 IO) | Gerichtlich bindend | Erfordert Insolvenzantrag |
| Abschoepfungsverfahren (§199 IO) | Restschuldbefreiung nach 3 Jahren | 3 Jahre Pfaendung, Obliegenheiten |

### Anlaufstellen
- **Schuldnerberatung [Bundesland]:** [Kontakt] — ERSTER Schritt, kostenlos!
- **Arbeiterkammer:** Arbeitsrechtliche Beratung bei Lohnpfaendungsfragen
- **Bezirksgericht:** Insolvenzantrag
- **Rechtsanwalt:** Bei Streit ueber Forderungsbestand oder Exekutionsbeschwerden

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | Verfuegbar / Nicht verfuegbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprueft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Pruefdatum | [YYYY-MM-DD] | |

---
Keine Rechtsberatung. Diese Analyse dient der rechtlichen Ersteinschaetzung und ersetzt nicht die Beratung durch eine staatlich anerkannte Schuldnerberatung oder einen Rechtsanwalt. Insbesondere vor Einleitung eines Insolvenzverfahrens wird die Beratung durch eine Schuldnerberatungsstelle dringend empfohlen — diese ist kostenlos.
```

---

## Critical Rules

1. **Schuldnerberatung IMMER empfehlen** — Die staatlich anerkannten Schuldnerberatungsstellen sind kostenlos und muessen als ERSTE Anlaufstelle genannt werden. Nicht erst den Rechtsanwalt empfehlen.
2. **Existenzminimum ist HEILIG** — Das Existenzminimum darf NICHT unterschritten werden. Wenn eine Pfaendung das Existenzminimum verletzt, sofort darauf hinweisen und Massnahmen empfehlen (Antrag nach §292a EO).
3. **Einspruchsfrist 4 Wochen** — Bei Zahlungsbefehl: 4 Wochen Einspruchsfrist (§252 ZPO). Versaeumnis fuehrt zur Rechtskraft. IMMER prominent warnen.
4. **Abschoepfungsverfahren: 3 Jahre** — Seit der Novelle (Umsetzung der RL (EU) 2019/1023) betraegt die Laufzeit des Abschoepfungsverfahrens 3 Jahre (§199 Abs 2 IO). NICHT mehr 5 oder 7 Jahre. Aktuelle Rechtslage anwenden.
5. **Aussergerichtlicher Ausgleich ist Pflicht** — Vor dem Insolvenzantrag MUSS ein aussergerichtlicher Ausgleichsversuch unternommen werden (§183 IO). Ohne diesen wird der Antrag zurueckgewiesen.
6. **Inkassokosten kritisch pruefen** — Viele Inkassoforderungen enthalten ueberhöhte oder unzulaessige Kostenpositionen. Immer darauf hinweisen, dass nur die notwendigen und angemessenen Betreibungskosten geschuldet werden (§1333 Abs 2 ABGB).
7. **Verjaehrung NICHT von Amts wegen** — Das Gericht prueft die Verjaehrung NICHT von Amts wegen. Der Schuldner muss die Verjaehrungseinrede aktiv erheben, sonst geht das Recht verloren.
8. **Obliegenheiten im Abschoepfungsverfahren** — Verletzung der Obliegenheiten (§210 IO) fuehrt zur Einstellung und zum Verlust der Restschuldbefreiung. IMMER darauf hinweisen.
9. **§§ immer mit Gesetzesname** — §199 IO, §290 EO, §1333 ABGB, §252 ZPO. Nie ohne Gesetzesangabe.
10. **Match user's language** — German in = German out. English in = English out. Gesetze immer in deutscher Originalform zitieren.
