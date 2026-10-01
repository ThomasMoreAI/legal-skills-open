---
name: recht-verkehr-momarcode1
title: /recht verkehr — Verkehrsrechtliche Analyse
description: Austrian traffic and transport law analysis — traffic accidents (EKHG, ABGB), driver's license (FSG), traffic violations (StVO), vehicle registration (KFG), insurance claims, drunk driving, speeding, and parking fines.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-verkehr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: regulatory
language: de
---

# /recht verkehr — Verkehrsrechtliche Analyse

When the user describes a traffic-related situation (accident, fine, license suspension, insurance dispute, drunk driving, speeding), presents documents (Strafverfuegung, Bescheid, Unfallbericht, Versicherungskorrespondenz), or asks about Austrian traffic law obligations, follow these steps.

---

## Step 1: Read the Facts / Documents

Read everything the user has provided. You need:

1. **What happened?** — Traffic accident (Verkehrsunfall)? Traffic violation (Verwaltungsuebertretung)? License suspension? Insurance dispute?
2. **Who is the user?** — Lenker (driver), Halter (registered owner), Fussgaenger (pedestrian), Radfahrer (cyclist), Beifahrer (passenger)?
3. **When did it happen?** — Exact date and time. Critical for Verjaehrung (§31 VStG: 1 year for Verwaltungsstrafsachen; §1489 ABGB: 3 years for Schadenersatz) and for Fristen (Einspruchsfristen).
4. **Where did it happen?** — Autobahn, Landesstrasse, Ortsgebiet, Privatgrund? Determines applicable speed limits and jurisdiction.
5. **Were there injuries?** — Determines: Verwaltungsstrafverfahren (StVO) vs. gerichtliches Strafverfahren (StGB §§80, 81, 88, 89).
6. **Police involvement?** — Polizeibericht, Alkotest, Anzeige? Was a Unfallaufnahme done?
7. **Insurance?** — Haftpflichtversicherer, Kaskoversicherung, other party's insurer? Claim filed?
8. **Documents?** — Strafverfuegung, Anonymverfuegung, Lenkererhebung, Bescheid, Gutachten, Unfallskizze?

If critical facts are missing, ask. Be specific:
> "Waren Sie der Lenker oder der Halter des Fahrzeugs? Das ist entscheidend, weil die Gefaehrdungshaftung nach EKHG den Halter trifft, nicht den Lenker."

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references (OGH, VwGH, LVwG), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

Search RIS Justiz for relevant OGH/VwGH decisions on the specific traffic law question. Present using format from `references/ogh-case-presentation.md`.

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

## Step 3: Classify the Traffic Law Situation

Determine which legal framework applies. Check each category:

### A: Verkehrsunfall — Haftung und Schadenersatz

**Two parallel liability regimes:**

| Haftungsgrundlage | Gesetz | Anspruchsgegner | Verschulden noetig? |
|-------------------|--------|-----------------|---------------------|
| Verschuldenshaftung | §1295ff ABGB | Lenker (Schaediger) | Ja — Verschulden muss bewiesen werden |
| Gefaehrdungshaftung | §1 EKHG | Halter des KFZ | Nein — verschuldensunabhaengig |
| Vertragliche Haftung | §1295 ABGB | z.B. Befuerderer | Je nach Vertrag |

**Gefaehrdungshaftung nach EKHG — Pruefungsschema:**
1. **Betrieb eines KFZ** (§1 Abs 1 EKHG) — Unfall muss "beim Betrieb" passiert sein
   - Weiter Betriebsbegriff: auch Parken, Be-/Entladen, Tuere oeffnen (OGH-Judikatur)
   - Ausnahmen: §3 EKHG — unbefugte Benuetzung (Diebstahl)
2. **Halter** (§5 EKHG) — Wer das KFZ auf eigene Rechnung in Betrieb hat
   - Nicht zwingend der Zulassungsbesitzer!
   - Halter vs. Eigentuemer vs. Lenker unterscheiden
3. **Haftungshoechstbetraege** (§15 EKHG):
   - Personenschaden: unbegrenzt (seit EKHG-Novelle 2007)
   - Sachschaden: Betrag laut KHVG-Mindestversicherungssummen
4. **Haftungsausschluss** (§9 EKHG):
   - Unabwendbares Ereignis (strenger Massstab!)
   - Hoeherer Gewalt (§9 Abs 1 EKHG)
   - Alleiniges Verschulden eines Dritten oder des Geschaedigten (§7 EKHG)
5. **Mitverschulden** (§7 EKHG):
   - Betriebsgefahr des gegnerischen KFZ
   - Eigenes Verschulden des Geschaedigten (§1304 ABGB)
   - Quotelung: z.B. 1/3 zu 2/3, je nach Verschuldensgrad und Betriebsgefahr

**Verschuldenshaftung nach ABGB — Pruefungsschema:**
1. **Rechtswidrigkeit** — Verstoss gegen StVO, KFG, oder allgemeine Sorgfaltspflicht
2. **Verschulden** — Fahrlässigkeit genuegt (§1294 ABGB: leichte, grobe Fahrlässigkeit, Vorsatz)
3. **Kausalitaet** — Adaequater Kausalzusammenhang
4. **Schaden** — Personenschaden und/oder Sachschaden
5. **Beweislast** — Grundsaetzlich beim Geschaedigten (§1296 ABGB), ABER:
   - Prima-facie-Beweis bei typischen Verkehrsunfaellen
   - Beweislastumkehr bei Schutzgesetzverletzung (§1311 ABGB): Verstoss gegen StVO ist Schutzgesetzverletzung!

**Halter vs. Lenker — Doppeltes Haftungssystem:**
- Halter: haftet nach EKHG (Gefaehrdungshaftung) + nach ABGB wenn eigenes Verschulden (z.B. mangelnde Fahrzeugwartung)
- Lenker: haftet nach ABGB (Verschuldenshaftung), NICHT nach EKHG
- In der Praxis: Versicherung reguliert ueber Haftpflicht des Halters (KHVG)
- Regressanspruch des Halters/Versicherers gegen den Lenker moeglich (§11 EKHG, §11 KHVG)

### B: Schadenersatz im Detail

**1. Personenschaden:**

| Schadensposition | Rechtsgrundlage | Berechnung |
|------------------|-----------------|------------|
| Schmerzensgeld | §1325 ABGB | Nach OGH-Schmerzensgeldtabelle, Globalbemessung |
| Verdienstentgang | §1325 ABGB | Differenzmethode: Einkommen ohne Unfall minus tatsaechliches Einkommen |
| Heilungskosten | §1325 ABGB | Tatsaechliche Kosten (Arzt, Medikamente, Therapie, Reha) |
| Pflegekosten | §1325 ABGB | Professionelle Pflege + Angehoerigenpflege (OGH: abstrakter Anspruch) |
| Verunstaltungsentschaedigung | §1326 ABGB | Bei dauerhafter Verunstaltung, wenn besseres Fortkommen beeintraechtigt |
| Trauerschmerzengeld | §1327 ABGB (OGH-Judikatur) | Bei Toetung: Hinterbliebene, wenn besondere Naehe |
| Unterhaltsentgang | §1327 ABGB | Bei Toetung: Unterhaltsberechtigte (Ehegatte, Kinder) |
| Bestattungskosten | §1327 ABGB | Angemessene Kosten |

**Schmerzensgeld-Orientierung (OGH-Richtwerte, grobe Einordnung):**
- Leichte Verletzung (Prellung, Verstauchung, <2 Wochen): ca. 500-3.000 EUR
- Mittlere Verletzung (Bruch, laengere Heilung): ca. 3.000-15.000 EUR
- Schwere Verletzung (Dauerschaden, langwierig): ca. 15.000-80.000 EUR
- Schwerste Verletzung (Querschnitt, Hirnschaden): ca. 80.000-350.000+ EUR
- Immer OGH-Schmerzensgeldkatalog als Referenz heranziehen

**2. Sachschaden:**

| Schadensposition | Berechnung | Hinweis |
|------------------|------------|---------|
| Reparaturkosten | Kostenvoranschlag / Gutachten | Nur bei wirtschaftlicher Reparaturwuerdigkeit |
| Totalschaden | Wiederbeschaffungswert minus Restwert | Wenn Reparaturkosten > 100-130% des Zeitwerts |
| Merkantile Wertminderung | Sachverstaendigengutachten | Bei reparierten Fahrzeugen, die am Markt weniger wert sind |
| Mietwagenkosten / Nutzungsausfall | Tatsaechliche Mietwagenkosten oder Nutzungsausfallentschaedigung | Nur fuer notwendige Dauer, Schadenminderungspflicht (§1304 ABGB)! |
| Abschleppkosten | Tatsaechliche Kosten | Angemessenheit |
| Rettungs-/Bergungskosten | Tatsaechliche Kosten | |
| Sachverstaendigenkosten | Tatsaechliche Kosten | Zweckmaessig und angemessen |
| Anwaltskosten (vorprozessual) | §1333 Abs 2 ABGB | Nur bei Verschulden des Gegners, angemessene Kosten |

**Schadenminderungspflicht (§1304 ABGB analog):**
- Geschaedigter muss Schaden gering halten
- Mietwagen: kein Luxusfahrzeug wenn eigenes Auto Mittelklasse
- Reparatur: zuegig beauftragen, nicht monatelang warten
- Verletzung: aerztliche Behandlung wahrnehmen

### C: Fuehrerscheinrecht (FSG)

**Fuehrerscheinentzug (§24 FSG):**

| Entzugsgrund | §§ FSG | Mindest-Entzugsdauer |
|-------------|--------|----------------------|
| 0,5-0,79 Promille (erstmalig) | §26 Abs 2 Z 1 FSG | 1 Monat |
| 0,8-1,19 Promille (erstmalig) | §26 Abs 2 Z 2 FSG | 3 Monate |
| 1,2-1,59 Promille (erstmalig) | §26 Abs 2 Z 3 FSG | 4 Monate |
| Ab 1,6 Promille (erstmalig) | §26 Abs 2 Z 4 FSG | 6 Monate |
| Verweigerung Alkotest | §26 Abs 2 Z 4 FSG | 6 Monate (= wie ab 1,6 Promille) |
| Verkehrsunfall unter Alkohol mit Personenschaden | §26 Abs 2 FSG | Verlängerung je nach Schwere |
| Mehr als 40 km/h im Ortsgebiet zu schnell | §26 Abs 3 Z 1 FSG | 2 Wochen |
| Mehr als 50 km/h im Ortsgebiet zu schnell | §26 Abs 3 Z 2 FSG | 6 Wochen |
| Mehr als 60 km/h ausserorts zu schnell | §26 Abs 3 Z 2 FSG | 6 Wochen |
| Fahrerflucht (§4 StVO) | §26 Abs 3 Z 3 FSG | 6 Wochen |

**Begleitende Massnahmen (§24 Abs 3 FSG):**
- [ ] Nachschulung (§4 Abs 3 FSG-GV): bei Alkohol, Drogen, Geschwindigkeit
- [ ] Verkehrspsychologische Untersuchung (§17 FSG-GV): ab 1,6 Promille, Wiederholung
- [ ] Amtsaerztliches Gutachten (§8 FSG): Fahreignungspruefung
- [ ] Erste-Hilfe-Kurs (in bestimmten Faellen)

**Probefahrerschein (§4 FSG):**
- Dauer: 3 Jahre ab Erteilung
- Alkohollimit: 0,1 Promille (§14 Abs 8 FSG)!
- Bei Verstoss: Probezeit-Verlängerung um 1 Jahr + Nachschulung
- Zweiter Verstoss: weiterer Entzug + Verkehrspsychologische Untersuchung
- Delikte die Probezeitverlängerung ausloesen (§4 Abs 6 FSG):
  - Alkohol/Drogen
  - Erhebliche Geschwindigkeitsueberschreitung
  - Vorrangverletzung mit Unfall
  - Fahrerflucht

### D: Alkohol und Drogen im Strassenverkehr

**Stufenmodell der Rechtsfolgen:**

| Promille | Verwaltungsstrafe (StVO) | Fuehrerschein (FSG) | Strafrecht (StGB) |
|----------|--------------------------|---------------------|--------------------|
| 0,1-0,49 (Probelenker) | §14 Abs 8 FSG: Verwaltungsstrafe | Probezeit-Verlängerung + Nachschulung | Nein (ausser Unfall) |
| 0,5-0,79 | §99 Abs 1b StVO: 300-3.700 EUR | §26 Abs 2 Z 1 FSG: 1 Monat Entzug | Nein (ausser Unfall) |
| 0,8-1,19 | §99 Abs 1a StVO: 800-3.700 EUR | §26 Abs 2 Z 2 FSG: 3 Monate | Nein (ausser Unfall) |
| 1,2-1,59 | §99 Abs 1 StVO: 1.200-4.400 EUR | §26 Abs 2 Z 3 FSG: 4 Monate + Nachschulung | Moeglich bei Unfall (§81 StGB) |
| Ab 1,6 | §99 Abs 1 StVO: 1.600-5.900 EUR | §26 Abs 2 Z 4 FSG: 6 Monate + Nachschulung + VPU + Amtsarzt | §81 StGB bei Unfall, §316 StGB |
| Verweigerung Alkotest | §99 Abs 1 StVO: 1.600-5.900 EUR | §26 Abs 2 Z 4 FSG: 6 Monate (wie ab 1,6 Promille) | — |

**Strafrechtliche Relevanz:**
- **§81 Abs 1 Z 2 StGB:** Fahrlässige Toetung unter besonders gefaehrlichen Verhaeltnissen (Alkohol) — bis 3 Jahre Freiheitsstrafe
- **§88 Abs 3 StGB:** Fahrlässige Koerperverletzung unter besonders gefaehrlichen Verhaeltnissen (Alkohol) — strengerer Strafrahmen
- **§316 StGB:** Gefaehrdung der koerperlichen Sicherheit — Lenken in einem durch Alkohol/Drogen beeintraechtigten Zustand, wenn dadurch Gefahr fuer Leib oder Leben entsteht; bis 1 Jahr Freiheitsstrafe

**Drogen:**
- §99 Abs 1 StVO: Lenken unter Drogeneinfluss = gleichgestellt mit Alkohol ab 0,8 Promille
- §14 Abs 8 FSG: Suchtmittelbeeintraechtigung, klinische Untersuchung oder Speicheltest
- Fuehrerscheinentzug: wie bei Alkohol ab 0,8 Promille, mindestens 3 Monate
- Zusaetzlich: Suchtmittelgesetz (SMG) kann zu Anzeige fuehren

### E: Geschwindigkeitsuebertretung

**Verfolgungsschritte der Behoerde:**

| Instrument | §§ | Frist | Kosten | Rechtsmittel |
|------------|-----|-------|--------|-------------|
| Organstrafverfuegung | §50 VStG | Sofort (an Ort und Stelle) | Max 90 EUR | Keine — Zustimmung = Erledigung |
| Anonymverfuegung | §49a VStG | 4 Wochen Zahlungsfrist | Bis 365 EUR | Keine — bei Nichtzahlung folgt Strafverfuegung/Verfahren |
| Strafverfuegung | §47 VStG | 2 Wochen Einspruchsfrist | Variabel | Einspruch (§49 VStG) — 2 Wochen ab Zustellung! |
| Straferkenntnis | §44a VStG | 4 Wochen Beschwerdefrist | Variabel | Beschwerde an LVwG (§7 VwGVG) |

**Lenkererhebung (§103 Abs 2 KFG):**
- Behoerde fragt Zulassungsbesitzer: Wer hat das Fahrzeug zum Tatzeitpunkt gelenkt?
- Auskunftspflicht: Zulassungsbesitzer MUSS innerhalb von 2 Wochen antworten
- Verweigerung/falsche Auskunft: eigene Verwaltungsstrafe bis 5.000 EUR (§134 Abs 1 KFG)
- Lenkererhebung ist KEINE Einladung zur Stellungnahme — es ist eine Pflicht!
- Auch juristische Personen sind auskunftspflichtig (letztverantwortlicher Disponent)

**Messgeraete und Anfechtbarkeit:**
- Radargeraete: geeicht? Aufstellort korrekt? Messtoleranz abgezogen?
- Section Control: Durchschnittsgeschwindigkeitsmessung, eigene Rechtsgrundlage
- Laser: Einzelmessung, haeufigste Fehlerquelle bei der Messung
- Nachfahrmessung (ProViDa): Videoaufzeichnung, Strecke/Zeit-Berechnung
- Toleranzabzuege: 5% bei Messung >100 km/h, 5 km/h bei Messung bis 100 km/h (StVO-Toleranzen)
- Anfechtung: Eichschein, Schulungsnachweise des Beamten, korrekte Aufstellung, Zuordnung zum Fahrzeug

### F: Parkstrafen

**Kurzparkzonen (§25 StVO):**
- Parkschein/Handyparken erforderlich
- Parkdauer gemaess Verordnung (meist 1,5 oder 3 Stunden)
- Ueberziehung: Verwaltungsstrafe (Organstrafverfuegung §50 VStG oder Anonymverfuegung §49a VStG)

**Halte-/Parkverbote (§§23, 24 StVO):**
- Absolutes Halteverbot: Anhalten nicht erlaubt (ausser verkehrsbedingt)
- Eingeschraenktes Halteverbot (Parkverbot): kurzes Halten zum Ein-/Aussteigen erlaubt
- Behindertenparkplatz: Missbrauch — strenge Strafen
- Geh-/Radwege, Schutzwege: absolutes Halte- und Parkverbot

**Abschleppen:**
- Behoerdliche Anordnung (§89a StVO): wenn Fahrzeug den Verkehr beeintraechtigt
- Kosten traegt der Lenker/Halter
- Rechtsschutz: Beschwerde gegen Abschleppanordnung (Massnahmenbeschwerde an LVwG)

### G: KFZ-Versicherung

**Haftpflichtversicherung (KHVG):**
- Pflichtversicherung (§59 KFG): jedes zugelassene KFZ muss haftpflichtversichert sein
- Mindestversicherungssumme (§7 KHVG): 7,6 Mio EUR Personenschaden, 1,52 Mio EUR Sachschaden (EU-Minimum)
- Direktanspruch (§26 KHVG): Geschaedigter kann DIREKT gegen den Versicherer des Schädigers klagen
- Obliegenheitsverletzung (§6 KHVG): z.B. Alkohol, Fahrerflucht — Versicherer reguliert, nimmt aber Regress beim VN
- Regress (§11 KHVG): bei grober Fahrlässigkeit oder Vorsatz des VN/Lenkers
- Risikoerhoehnungsoption des Lenkers

**Kaskoversicherung:**
- Freiwillig, privatrechtlicher Vertrag
- Vollkasko: alle Schaeden am eigenen Fahrzeug
- Teilkasko: Diebstahl, Hagel, Wildunfall, Brand, Glasbruch
- Selbstbehalt je nach Vertrag
- Obliegenheiten: Schadenmeldung fristgerecht, keine Reparatur vor Freigabe, Mitwirkungspflicht
- Deckungsklage gegen eigenen Kaskoversicherer bei Ablehnung (Bezirksgericht/Landesgericht je nach Streitwert)

**Versicherungsregress:**
- §11 KHVG: Regress des Haftpflichtversicherers gegen VN oder Lenker
- Regressgruende: Alkohol (ab 0,8 Promille), Fahrerflucht, fehlende Lenkerberechtigung, Vorsatz
- Hoehe: begrenzt auf maximal Versicherungssumme, in der Praxis oft capped
- Gegen Regress wehren: Deckungsklage, Einwand der Verhaeltnismaessigkeit

### H: Fahrerflucht (§4 StVO)

**Pflichten nach einem Verkehrsunfall:**

| Pflicht | §§ StVO | Inhalt |
|---------|---------|--------|
| Anhalte- und Hilfeleistungspflicht | §4 Abs 1 StVO | Bei Unfall anhalten, Verletzte versorgen, Rettung rufen |
| Verstaendigungspflicht (Polizei) | §4 Abs 2 StVO | WENN Personenschaden ODER Identitaetsfeststellung nicht moeglich |
| Nachweis-/Austauschpflicht | §4 Abs 5 StVO | Identitaet und Beteiligung am Unfall nachweisen |
| Meldepflicht (ohne Personenschaden) | §4 Abs 5 StVO | Bei Sachschaden ohne Personenschaden: wenn kein Nachweis erfolgte, naechste Polizeidienststelle UNVERZUEGLICH verstaendigen |

**Rechtsfolgen Fahrerflucht:**
- Verwaltungsstrafe (§99 Abs 2 lit a StVO): 36-2.180 EUR (bei Personenschaden), 72-2.180 EUR bei Verletzung der Meldepflicht
- Fuehrerscheinentzug (§26 Abs 3 Z 3 FSG): mindestens 6 Wochen
- Versicherungsregress (§11 KHVG): Versicherer kann Regress nehmen
- Strafrechtliche Konsequenzen: §94 StGB (Im-Stich-Lassen eines Verletzten) — bis 3 Jahre Freiheitsstrafe!
- Nachteilige Beweiswuerdigung: Flucht wird als Indiz fuer Verschulden gewertet

---

## Step 4: Determine Mitverschulden / Haftungsquote

Bei Verkehrsunfaellen fast immer relevant:

**Mitverschulden (§1304 ABGB):**
- Verschuldensquote wird nach Schwere des beiderseitigen Verschuldens aufgeteilt
- Betriebsgefahr (EKHG): auch ohne Verschulden haftet der Halter anteilig fuer die Betriebsgefahr seines KFZ
- Typische Quoten (OGH-Judikatur als Orientierung):
  - Vorrangverletzung: Vorrangverletzer 75-100%
  - Auffahrunfall: Auffahrender meist 100% (Anscheinsbeweis)
  - Alkohol + Unfall: deutlich hoeherer Verschuldensanteil
  - Fussgaenger auf Schutzweg: KFZ-Lenker haftet hoeher (§9 EKHG Betriebsgefahr)
  - Nicht angegurtet (§106 Abs 2 KFG): Mitverschulden ca. 25-33% am eigenen Personenschaden

**Haftungsbefreiung/-minderung prufen:**
- §7 EKHG: Mitverschulden des Geschaedigten
- §9 EKHG: Unabwendbares Ereignis
- §1311 ABGB: Schutzgesetzverletzung (Beweislastumkehr bei StVO-Verstoss!)
- Tierhalterhaftung (§1320 ABGB) bei Wildunfaellen: Jagdausuebungsberechtigter

---

## Step 5: Quantify the Claim / Exposure

Where the user has provided concrete information, calculate:

**Bei Unfallschaeden:**
1. **Sachschaden:** Reparaturkosten oder Totalschaden (Wiederbeschaffungswert - Restwert) + Wertminderung + Mietwagen/Nutzungsausfall + Sachverstaendigenkosten + Abschleppen
2. **Personenschaden:** Schmerzensgeld (OGH-Tabelle) + Heilungskosten + Verdienstentgang + Pflegekosten
3. **Mitverschuldensquote** anwenden
4. **Abzug:** bereits geleistete Zahlungen der Versicherung

**Bei Verwaltungsstrafen:**
1. **Strafe:** Hoehe nach §99 StVO / §134 KFG / jeweiliger Strafnorm
2. **Verfahrenskosten:** 10% Kostenbeitrag (§64 VStG), mindestens 10 EUR
3. **Fuehrerscheinentzug:** Dauer, wirtschaftliche Konsequenzen
4. **Folgekosten:** Nachschulung (ca. 500-600 EUR), VPU (ca. 400-500 EUR), Amtsarzt (ca. 30-50 EUR)

---

## Step 6: Present Findings

```markdown
# Verkehrsrechtliche Analyse

**Sachverhalt:** [Kurzbeschreibung: Unfall, Verwaltungsuebertretung, etc.]
**Beteiligte:** [Lenker/Halter/Fussgaenger/Radfahrer]
**Datum/Ort:** [Datum, Ort, Strassentyp]
**Rechtsgebiet:** [Verwaltungsstrafrecht / Zivilrecht / Strafrecht / Fuehrerscheinrecht]

## Zusammenfassung
[2-3 Saetze: Was ist die rechtliche Ausgangslage, welche Ansprueche/Risiken bestehen]

## Rechtliche Einordnung

### Haftungsgrundlage
| Anspruch | Rechtsgrundlage | Anspruchsgegner | Erfolgsaussicht |
|----------|----------------|-----------------|-----------------|
| [z.B. Schadenersatz] | [z.B. §1295 ABGB + §1 EKHG] | [z.B. Halter des gegnerischen KFZ] | [Hoch/Mittel/Gering] |

### Haftungsquote
| Partei | Verschulden | Rechtsgrundlage | Quote |
|--------|-------------|-----------------|-------|
| Gegner | [z.B. Vorrangverletzung] | [z.B. §19 StVO] | [x]% |
| User | [z.B. ueberhoeht Geschwindigkeit] | [z.B. §20 StVO] | [x]% |

### Schadenberechnung
| Schadensposition | Bruttobetrag | Nach Mitverschulden ([x]%) |
|------------------|-------------|---------------------------|
| Reparaturkosten | EUR [x] | EUR [x] |
| Wertminderung | EUR [x] | EUR [x] |
| Mietwagen ([x] Tage) | EUR [x] | EUR [x] |
| Schmerzensgeld | EUR [x] | EUR [x] |
| **Gesamt** | **EUR [x]** | **EUR [x]** |

### Verwaltungsstrafrechtliche Konsequenzen
| Massnahme | Rechtsgrundlage | Hoehe/Dauer |
|-----------|----------------|-------------|
| Geldstrafe | [§99 StVO / §134 KFG] | EUR [x] |
| Fuehrerscheinentzug | [§26 FSG] | [x] Monate |
| Nachschulung | [§24 Abs 3 FSG] | Pflicht: Ja/Nein |

## Versicherung
| Versicherung | Deckung | Naechster Schritt |
|-------------|---------|-------------------|
| Gegnerische Haftpflicht | Sachschaden + Personenschaden | Schadensmeldung an [Versicherer] |
| Eigene Kasko | Eigener Sachschaden | Schadensmeldung, Selbstbehalt EUR [x] |
| Rechtsschutzversicherung | Rechtsanwaltskosten | Deckungszusage einholen |

## Naechste Schritte
1. [Konkrete Handlung mit Frist]
2. [Konkrete Handlung]
3. [Rechtsanwalt / Versicherung kontaktieren fuer ...]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | Verfuegbar / Nicht verfuegbar | [connection status] |
| Gesetze | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Normen geprueft |
| Judikatur | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Pruefdatum | [YYYY-MM-DD] | |

---
Keine Rechtsberatung. Diese Analyse dient der rechtlichen Ersteinschaetzung und ersetzt nicht die Beratung durch einen Rechtsanwalt. Insbesondere bei Verkehrsunfaellen mit Personenschaden, Fuehrerscheinentzug oder strafrechtlichen Vorwuerfen wird dringend anwaltliche Vertretung empfohlen. Aktuelle Gesetzestexte auf [ris.bka.gv.at](https://www.ris.bka.gv.at) pruefen.
```

---

## Critical Rules

1. **Always cite specific §§ with Gesetzesname** — Never "laut Verkehrsrecht" without §19 Abs 4 StVO, §1 EKHG, §26 Abs 2 Z 3 FSG, etc.
2. **Distinguish Halter vs. Lenker** — Gefaehrdungshaftung (EKHG) trifft den Halter, Verschuldenshaftung (ABGB) den Lenker. Verwechslung fuehrt zu falschen Ergebnissen.
3. **Always check for Mitverschulden** — Bei Verkehrsunfaellen ist fast immer eine Quotelung vorzunehmen. Betriebsgefahr beider KFZ beruecksichtigen.
4. **Fristen sind HEILIG** — Einspruch gegen Strafverfuegung: 2 Wochen (§49 VStG). Beschwerde gegen Straferkenntnis: 4 Wochen (§7 VwGVG). Verjaehrung Schadenersatz: 3 Jahre (§1489 ABGB). Verjaehrung Verwaltungsstrafe: 1 Jahr Verfolgungsverjaehrung (§31 Abs 1 VStG).
5. **Alkohol: Stufenmodell korrekt anwenden** — Die Rechtsfolgen haengen exakt vom Promillewert ab. 0,79 vs. 0,80 macht einen enormen Unterschied. Probelenker: 0,1 Promille!
6. **StVO-Verstoss ist Schutzgesetzverletzung** — §1311 ABGB: Beweislastumkehr zugunsten des Geschaedigten. Das ist ein wichtiger Vorteil in der Praxis.
7. **Direktanspruch gegen Haftpflichtversicherer** — §26 KHVG: Der Geschaedigte muss nicht den Schaediger verklagen, sondern kann direkt den Versicherer belangen.
8. **Lenkererhebung ernst nehmen** — §103 Abs 2 KFG: Nichtbeantwortung ist eigene Verwaltungsuebertretung (bis 5.000 EUR). Falsche Auskunft ebenso.
9. **Use RIS if connected** — Verify statute citations, especially OGH-Schmerzensgeldrichtwerte und aktuelle FSG-Entzugsgrenzen.
10. **Match user's language** — German in, German out. English in, English out. Gesetze immer in deutscher Form (§24 FSG, nicht "Section 24 FSG").
