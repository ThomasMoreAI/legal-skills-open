---
name: recht-verkehr-verfahren-momarcode1
title: /recht verkehr-verfahren — Verkehrsrechtliche Verfahren und Rechtsmittel
description: Austrian traffic law procedures — appeals against traffic fines (Einspruch, Beschwerde an LVwG), challenging license suspensions, accident damage claims in court, direct claims against insurers (§26 KHVG), Lenkererhebung obligations, and criminal proceedings for traffic offences (§81, §88, §89 StGB, Diversion).
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-verkehr-verfahren
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: litigation
language: de
sources:
- title: Ogh case presentation
  path: references/ogh-case-presentation.md
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht verkehr-verfahren — Verkehrsrechtliche Verfahren und Rechtsmittel

When the user has received a traffic fine (Strafverfuegung, Anonymverfuegung), faces a license suspension (Fuehrerscheinentzug), wants to claim damages after a traffic accident, or faces criminal charges related to traffic, follow these steps.

---

## Step 1: Read the Facts / Documents

Read everything the user has provided. You need:

1. **What document was received?** — Anonymverfuegung, Strafverfuegung, Straferkenntnis, Lenkererhebung, Mandatsbescheid (Fuehrerscheinentzug), Strafantrag/Strafverfuegung des Gerichts?
2. **When was it received (zugestellt)?** — The exact date of Zustellung starts the Frist. If unclear, ask immediately:
   > "Wann wurde Ihnen das Schreiben zugestellt? Das genaue Datum ist entscheidend — der Einspruch gegen eine Strafverfuegung muss innerhalb von 2 Wochen ab Zustellung erfolgen."
3. **What is the alleged offence?** — Geschwindigkeitsuebertretung, Alkohol, Fahrerflucht, Rotlichtverstoss, Parkverstoss, Unfall mit Personenschaden?
4. **What does the user want?** — Fine anfechten? Fuehrerschein zurueckbekommen? Schadenersatz fordern? Gegen Versicherung vorgehen?
5. **Evidence available?** — Radarfoto, Dashcam, Zeugen, Unfallprotokoll, aerztliche Befunde, Kostenvoranschlag, Sachverstaendigengutachten?
6. **Financial situation?** — Relevant for Ratenzahlung der Strafe, Verfahrenshilfe, Streitwertberechnung

If the user mentions criminal charges (§81 StGB, §88 StGB, §316 StGB) or Anklage/Strafantrag, immediately assess severity and flag Anwaltspflicht.

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references (OGH, VwGH, LVwG), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

Search RIS Justiz for relevant VwGH/LVwG/OGH decisions on the specific procedural question. Present using format from `references/ogh-case-presentation.md`.

---

## Step 3: Classify the Procedural Situation

Determine which procedural path applies. Check each option:

### A: Verwaltungsstrafverfahren (VStG) — Verkehrsstrafen

**Verfahrensstadien und Rechtsmittel:**

| Stadium | Dokument | Frist | Rechtsmittel | §§ |
|---------|----------|-------|-------------|-----|
| 1. Organstrafverfuegung | Am Ort und Stelle | Sofort | KEINES — Zustimmung = rechtskraeftig | §50 VStG |
| 2. Anonymverfuegung | Per Post an Zulassungsbesitzer | 4 Wochen Zahlungsfrist | KEINES — bei Nichtzahlung folgt Verfahren | §49a VStG |
| 3. Lenkererhebung | Per RSa-Brief an Zulassungsbesitzer | 2 Wochen Antwortfrist | KEINE — Pflicht zur Auskunft (§103 Abs 2 KFG) | §103 Abs 2 KFG |
| 4. Strafverfuegung | Per RSa-Brief | **2 Wochen Einspruchsfrist** | **Einspruch** (§49 VStG) | §47 VStG |
| 5. Straferkenntnis | Per RSa-Brief | **4 Wochen Beschwerdefrist** | **Beschwerde an LVwG** (§7 VwGVG) | §44a VStG |
| 6. LVwG-Erkenntnis | Per Zustellung | 6 Wochen | Revision an VwGH (Art 133 Abs 4 B-VG) | §25a VwGG |

**Einspruch gegen Strafverfuegung (§49 VStG):**
- **Frist: 2 Wochen ab Zustellung** — NICHT versaeumen!
- Kein formales Begruendungserfordernis (aber Begruendung empfehlenswert)
- Wirkung: Strafverfuegung tritt ausser Kraft, ordentliches Ermittlungsverfahren wird eingeleitet
- WICHTIG: Im ordentlichen Verfahren kann die Strafe hoeher ausfallen als in der Strafverfuegung (Verschlechterungsverbot gilt NICHT beim Einspruch gegen Strafverfuegung!)
- Teileinspruch moeglich (z.B. nur gegen die Strafe, nicht gegen den Schuldspruch)

**Beschwerde gegen Straferkenntnis (§7 VwGVG):**
- **Frist: 4 Wochen ab Zustellung**
- Einbringung bei der Behoerde, die das Straferkenntnis erlassen hat (NICHT direkt beim LVwG)
- Inhalt (§9 VwGVG):
  - [ ] Bezeichnung des angefochtenen Straferkenntnisses
  - [ ] Beschwerdepunkte (Schuldspruch und/oder Strafe)
  - [ ] Begruendung
  - [ ] Begehren (Aufhebung, Herabsetzung der Strafe, Einstellung)
- Aufschiebende Wirkung: JA, grundsaetzlich (§13 VwGVG), kann von der Behoerde aberkannt werden
- LVwG-Verhandlung: auf Antrag oder von Amts wegen (§44 VwGVG)
- LVwG entscheidet in der Sache selbst (meritorische Entscheidung, §50 VwGVG)
- Verschlechterungsverbot (reformatio in peius): §42 VwGVG — LVwG darf die Strafe nicht erhoehen, wenn nur der Beschuldigte Beschwerde erhoben hat!
- Kostenersatz: bei Erfolg der Beschwerde kein Kostenbeitrag; bei Abweisung: Kostenbeitrag 20% der verhaengten Strafe (§52 VwGVG)

**Verfahrensrechtliche Besonderheiten im Verkehrsstrafrecht:**
- Verfolgungsverjaehrung (§31 Abs 1 VStG): 1 Jahr ab Tatbegehung — wenn innerhalb eines Jahres keine Verfolgungshandlung gesetzt wird, darf nicht mehr bestraft werden
- Strafbarkeitsverjaehrung (§31 Abs 3 VStG): 3 Jahre ab Tatbegehung
- Verfolgungshandlung (§32 Abs 2 VStG): jede nach aussen erkennbare Amtshandlung gegen den Beschuldigten
- Lenkererhebung als Verfolgungshandlung: NEIN (staendige VwGH-Judikatur), ABER die anschliessende Aufforderung zur Rechtfertigung schon

### B: Fuehrerscheinentzug anfechten

**Verfahren:**
1. Entzug erfolgt durch Mandatsbescheid der BH/Magistrat (§57 AVG)
2. **Vorstellung** gegen Mandatsbescheid: 2 Wochen ab Zustellung (§57 Abs 2 AVG)
   - Wirkung: Mandatsbescheid tritt ausser Kraft, ordentliches Ermittlungsverfahren
   - KEIN aufschiebende Wirkung — Fuehrerschein bleibt waehrend des Verfahrens entzogen!
3. Neuer Bescheid der Behoerde im ordentlichen Verfahren
4. **Beschwerde an LVwG** gegen diesen Bescheid: 4 Wochen (§7 VwGVG)
5. **Aufschiebende Wirkung der Beschwerde:**
   - Grundsaetzlich JA (§13 VwGVG)
   - ABER: Behoerde kann aufschiebende Wirkung ausschliessen wegen Gefahr im Verzug (§13 Abs 2 VwGVG)
   - Bei Alkohol/Drogen: Ausschluss der aufschiebenden Wirkung nahezu immer (Verkehrssicherheit)
   - Antrag auf Zuerkennung der aufschiebenden Wirkung beim LVwG moeglich (§22 VwGVG)

**Argumentationsmuster gegen Fuehrerscheinentzug:**
- Messfehler beim Alkotest (Geraet nicht geeicht, Mundalkohol, 15-Minuten-Wartezeit nicht eingehalten)
- Verhaeltnismaessigkeit der Entzugsdauer (persoenliche Umstaende, Beruf erfordert Fuehrerschein)
- Begruendungsmaengel im Bescheid
- Gesundheitliche Fahreignung — Gutachten anfechten
- Dauer: nur Mindestdauer oder laenger? Begruendung fuer laengere Dauer erforderlich

### C: Schadenersatzklage nach Verkehrsunfall

**Zustaendigkeit:**

| Streitwert | Gericht | Anwaltspflicht | §§ |
|------------|---------|----------------|-----|
| Bis 15.000 EUR | Bezirksgericht (BG) | Nein (aber empfohlen) | §49 JN |
| Ueber 15.000 EUR | Landesgericht (LG) | Ja (§27 ZPO) | §49 JN |
| Arbeitsunfall | ASG (Arbeits- und Sozialgericht) | Nein (Arbeitnehmer) | §65 ASGG |

**Oertliche Zustaendigkeit (Wahlrecht des Klaegers):**
- Allgemeiner Gerichtsstand des Beklagten (§66 JN): Wohnsitz des Schädigers/Halters
- Unfallort (§92a JN): Gerichtsstand der unerlaubten Handlung (Schadenersatzklagen!)
- Sitz des Versicherers bei Direktklage (§26 KHVG + §92a JN)

**Verfahrensablauf Schadenersatzklage:**

| Schritt | Aktion | Dauer (ca.) |
|---------|--------|-------------|
| 1. Vorprozessual | Schadensmeldung an gegnerische Haftpflichtversicherung | 2-4 Wochen |
| 2. Aussergerichtliche Regulierung | Verhandlung mit Versicherer, Anwalt einschalten | 1-6 Monate |
| 3. Klage | Wenn Regulierung scheitert oder zu gering | — |
| 4. Klagebeantwortung | 4 Wochen ab Zustellung der Klage | 4 Wochen |
| 5. Vorbereitende Tagsatzung | Gericht klaert Streitpunkte, Beweisbeschluesse | 2-4 Monate |
| 6. Sachverstaendigengutachten | KFZ-Sachverstaendiger (Schaden), medizinischer SV (Verletzung) | 3-6 Monate |
| 7. Streitverhandlung(en) | Beweisaufnahme, Vergleichsgespraech | 3-12 Monate |
| 8. Urteil | Entscheidung des Erstgerichts | 2-4 Wochen nach Schluss |
| 9. Berufung | 4 Wochen ab Zustellung des Urteils (§464 ZPO) | — |

**Beweismittel im Verkehrsprozess:**
- Unfallbericht der Polizei (Urkundsbeweis §292 ZPO)
- KFZ-technisches Sachverstaendigengutachten: Unfallhergang, Geschwindigkeit, Bremsspuren
- Medizinisches Sachverstaendigengutachten: Verletzungsfolgen, Schmerzensgeld
- Unfallrekonstruktion: technischer Sachverstaendiger
- Dashcam-Aufnahmen: zulaessig als Beweismittel in Oesterreich (OGH 6 Ob 109/18f), aber DSGVO-Bedenken
- Zeugen: Mitfahrer, andere Verkehrsteilnehmer, Ersthelfer
- Messfotos (Radar/Laser): bei Geschwindigkeitsdisputen

**Prozesskostenrisiko (GGG + RATG):**
- Pauschalgebuehr (GGG): abhaengig vom Streitwert, Tarifpost 1
- Rechtsanwaltskosten (RATG): nach Bemessungsgrundlage (= Streitwert)
- Bei Unterliegen: eigene + gegnerische Kosten
- Kostenschaetzung mit `/recht costs` Skill durchfuehren

### D: Direktklage gegen Haftpflichtversicherer (§26 KHVG)

**Voraussetzungen:**
1. Verkehrsunfall mit KFZ-Beteiligung
2. Haftpflichtversicherung des Schädigers besteht
3. Haftungsanspruch gegen den Versicherungsnehmer/Lenker besteht

**Besonderheiten der Direktklage:**
- Geschaedigter klagt den Versicherer DIREKT (nicht den Schaediger/Halter)
- Versicherer kann alle Einwendungen des VN geltend machen (§26 Abs 2 KHVG)
- Gerichtsstand: Wohnsitz des Geschaedigten oder Unfallort (§26 Abs 4 KHVG, §92a JN)
- Vorteil: Versicherer ist zahlungsfaehig (kein Exekutionsrisiko)
- Es ist auch moeglich, Schaediger UND Versicherer gemeinsam zu klagen (§11 ZPO Streitgenossenschaft)

**Verjährung des Direktanspruchs:**
- §26 Abs 5 KHVG: Direktanspruch verjaehrt nicht vor dem Anspruch gegen den VN
- §1489 ABGB: 3 Jahre ab Kenntnis von Schaden und Schaediger (subjektive Frist)
- §1489 ABGB: 30 Jahre absolute Frist

### E: Lenkererhebung (§103 Abs 2 KFG)

**Pflichten:**
- Zulassungsbesitzer MUSS auf Verlangen der Behoerde binnen 2 Wochen Auskunft erteilen
- Auskunft: Wer hat das Fahrzeug zu einem bestimmten Zeitpunkt gelenkt?
- Gilt auch fuer juristische Personen (Geschaeftsfuehrer/Disponent auskunftspflichtig)
- Pflicht besteht auch bei Gefahr der Selbstbelastung (VfGH hat dies als verfassungskonform beurteilt: VfSlg 10.394/1985)

**Rechtsfolgen bei Verstoss:**
- Nichtbeantwortung: Verwaltungsstrafe bis 5.000 EUR (§134 Abs 1 KFG)
- Falsche Auskunft: ebenso strafbar (bis 5.000 EUR)
- Verspätete Auskunft: ebenfalls strafbar
- Unvollständige Auskunft: z.B. "jemand aus der Familie" reicht NICHT

**Verteidigungsstrategien:**
- Pruefen ob Lenkererhebung formell korrekt (zugestellt? Frist korrekt berechnet?)
- Pruefen ob Verfolgungsverjaehrung (§31 VStG) der Grundtat eingetreten ist — wenn ja, ist auch die Lenkererhebung sinnlos und anfechtbar
- Begruendete Unmöglichkeit der Auskunft (z.B. Firmenfahrzeug, kein Fahrtenbuch, tatsaechlich unbekannt) — geringe Erfolgschancen, strenger Massstab der Judikatur

### F: Strafverfahren bei Verkehrsdelikten

**Relevante Straftatbestaende:**

| Delikt | §§ StGB | Strafrahmen | Voraussetzungen |
|--------|---------|-------------|-----------------|
| Fahrlässige Toetung | §80 StGB | Bis 1 Jahr | Tod durch fahrlässiges Verhalten |
| Fahrlässige Toetung unter bes. gef. Verh. | §81 Abs 1 Z 1 StGB | Bis 3 Jahre | Tod + Alkohol >0,8 Promille oder andere besonders gefaehrliche Verhaeltnisse |
| Grob fahrlässige Toetung | §81 Abs 2 StGB | 6 Monate bis 5 Jahre | Tod durch besonders leichtsinniges/ruecksichtsloses Verhalten |
| Fahrlässige Koerperverletzung | §88 Abs 1 StGB | Bis 3 Monate | Verletzung durch Fahrlässigkeit |
| Fahrlässige Koerperverletzung (schwer) | §88 Abs 4 StGB | Bis 6 Monate (schwere KV), bis 2 Jahre (Dauerfolge) | Schwere Koerperverletzung |
| Fahrlässige KV unter bes. gef. Verh. | §88 Abs 3 StGB | Bis 6 Monate | Verletzung + Alkohol >0,8 Promille |
| Gefaehrdung der koerperlichen Sicherheit | §89 StGB | Bis 3 Monate (Ermaechtigung) | Fahrlässige Gefaehrdung ohne Verletzung |
| Gefaehrdung durch Alkohol/Drogen | §316 StGB | Bis 1 Jahr | Lenken im beeintraechtigten Zustand + Gefaehrdung |
| Im-Stich-Lassen eines Verletzten | §94 StGB | Bis 3 Jahre | Unterlassene Hilfeleistung nach Unfall |
| Imstichlassen mit Todesfolge | §94 Abs 2 StGB | 6 Monate bis 5 Jahre | Wenn der Verletzte stirbt |
| Unbefugter Gebrauch von KFZ | §136 StGB | Bis 6 Monate | Fahren ohne Einwilligung des Berechtigten |

**Diversion (§§198ff StPO):**
- Bei vielen Verkehrsdelikten moeglich (besonders §§80, 81, 88, 89 StGB)
- Voraussetzungen (§198 Abs 1 StPO):
  1. Sachverhalt hinreichend geklaert
  2. Strafrahmen bis 5 Jahre (bei den meisten Verkehrsdelikten gegeben)
  3. Schuld nicht als schwer anzusehen
  4. Diversionsmassnahme genuegt
  5. Kein Freispruch wahrscheinlicher
- Formen:
  - Zahlung eines Geldbetrags (§200 StPO): Tagessaetze, max 360 Tagessaetze
  - Gemeinnuetzige Leistung (§201 StPO): max 240 Stunden
  - Probezeit (§203 StPO): 1-2 Jahre, mit oder ohne Bewaehrungshilfe
  - Tatausgleich (§204 StPO): Ausgleich mit dem Opfer (ATA)
- Vorteil: keine Vorstrafe, keine Verurteilung, kein Strafregistereintrag
- Zustimmung des Beschuldigten erforderlich
- Opfer muss gehoert werden (hat kein Vetorecht)

**Privatbeteiligtenanschluss (§67 StPO):**
- Geschaedigter kann sich dem Strafverfahren als Privatbeteiligter anschliessen
- Geltendmachung von Schadenersatzanspruechen direkt im Strafprozess
- Kostenguenstig: keine gesonderte Klage noetig
- Gericht kann Privatbeteiligten auf den Zivilrechtsweg verweisen (§366 StPO)

### G: Versicherungsansprueche durchsetzen

**Vorprozessualer Ablauf:**

| Schritt | Aktion | Frist |
|---------|--------|-------|
| 1. Schadenmeldung | An gegnerische Haftpflichtversicherung (oder eigene Kasko) | Unverzueglich (VersVG §33) |
| 2. Aufforderung | Anwaltliches Forderungsschreiben mit Fristsetzung | Angemessene Frist (2-4 Wochen) |
| 3. Angebot/Ablehnung | Versicherer bietet an oder lehnt ab | — |
| 4. Klagsdrohung | Wenn Angebot unzureichend | — |
| 5. Klage | Direktklage §26 KHVG oder Deckungsklage (Kasko) | Innerhalb Verjaehrungsfrist |

**Haeufige Streitpunkte mit Versicherungen:**
- Totalschaden vs. Reparatur: Versicherer stuft als Totalschaden ein, Geschaedigter will Reparatur (OGH: 130%-Grenze)
- Wertminderung: Versicherer verweigert oder kuerzt merkantile Wertminderung
- Schmerzensgeld: Versicherer bietet zu wenig an (OGH-Schmerzensgeldrichtwerte als Argument)
- Mietwagenkosten: Versicherer kuerzt Dauer oder Klasse
- Mitverschulden: Versicherer behauptet hoeheres Mitverschulden als gerechtfertigt
- Obliegenheitsverletzung: Versicherer verweigert Deckung (Kasko) wegen Obliegenheitsverletzung (z.B. verspätete Meldung)

---

## Step 4: Check ALL Deadlines (CRITICAL)

**Fristversaeumnis im Verkehrsstrafrecht ist in der Regel IRREPARABEL.**

Calculate ALL relevant deadlines. For each:

| Frist | Grundlage | Beginn | Ablauf | Status |
|-------|-----------|--------|--------|--------|
| Einspruch Strafverfuegung | §49 VStG | Zustellung | +2 Wochen | offen/kritisch/abgelaufen |
| Beschwerde Straferkenntnis | §7 VwGVG | Zustellung | +4 Wochen | offen/kritisch/abgelaufen |
| Vorstellung gegen Mandatsbescheid (FSE) | §57 Abs 2 AVG | Zustellung | +2 Wochen | offen/kritisch/abgelaufen |
| Lenkerauskunft | §103 Abs 2 KFG | Zustellung | +2 Wochen | offen/kritisch/abgelaufen |
| Beschwerde LVwG-Erkenntnis (Revision VwGH) | §25a VwGG | Zustellung | +6 Wochen | offen/kritisch/abgelaufen |
| Schadenersatz-Verjaehrung | §1489 ABGB | Kenntnis Schaden+Schaediger | +3 Jahre | offen/kritisch/abgelaufen |
| Verfolgungsverjaehrung VStG | §31 Abs 1 VStG | Tatbegehung | +1 Jahr | offen/kritisch/abgelaufen |

**Fristberechnung:**
- Wochenfrist: §33 Abs 2 AVG — Ende am selben Tag der Woche (z.B. Montag → Montag)
- Monatsfrist: §33 Abs 2 AVG — Ende am gleichen Tag des entsprechenden Monats
- Faellt Ende auf Sa/So/Feiertag: naechster Werktag (§33 Abs 2 AVG)
- Postaufgabe am letzten Tag genuegt (§33 Abs 3 AVG)

**Wiedereinsetzung in den vorigen Stand (§71 AVG / §46 VwGVG):**
- Moeglich bei minderem Grad des Versehens
- Antrag binnen 2 Wochen ab Wegfall des Hindernisses (§71 Abs 2 AVG)
- Gleichzeitig versaeumte Handlung nachholen
- Geringe Erfolgschancen — strenger Massstab der Judikatur

---

## Step 5: Draft the Appropriate Filing

Based on the classification, draft the relevant Schriftsatz. Always in proper Austrian legal format.

### Einspruch gegen Strafverfuegung (§49 VStG) — Template:

```
An die
[zustaendige Behoerde: Bezirkshauptmannschaft / Magistrat / Landespolizeidirektion]
[Adresse]

[Name, Adresse des Beschuldigten]

[Ort], am [Datum]

EINSPRUCH
gegen die Strafverfuegung vom [Datum], GZ: [Geschaeftszahl],
zugestellt am [Datum]

Innerhalb offener Frist erhebe ich gegen die oben bezeichnete
Strafverfuegung wegen [Uebertretung, z.B. "Uebertretung des §20 Abs 2 StVO
(Geschwindigkeitsueberschreitung)"]

E I N S P R U C H

und begruende diesen wie folgt:

I. SACHVERHALT

[Darstellung des Sachverhalts aus Sicht des Beschuldigten.
Z.B.: "Am [Datum] um [Uhrzeit] lenkte ich das Kraftfahrzeug [Kennzeichen]
auf der [Strasse] in [Ort]. Mir wird vorgeworfen, die zulaessige
Hoechstgeschwindigkeit von [x] km/h um [y] km/h ueberschritten zu haben."]

II. BEGRUENDUNG

[Rechtliche und tatsaechliche Argumentation, warum die Strafverfuegung
unrichtig ist.

Moegliche Argumente:
- Messfehler (Geraet nicht geeicht, falsche Aufstellung, keine Zuordnung
  zum Fahrzeug)
- Lenker war nicht der Beschuldigte
- Kein Verschulden (§5 Abs 1 VStG)
- Verfolgungsverjaehrung (§31 VStG)
- Fehlerhafte Zustellung
- Unrichtige Sachverhaltsfeststellung

z.B.: "Die vorgeworfene Geschwindigkeitsueberschreitung ist unrichtig.
Das verwendete Radargeraet [Typ] mit der Geraete-Nr. [x] weist laut
Eichschein eine Toleranz von [x]% auf. Nach Abzug dieser Toleranz
betraegt die tatsaechlich gemessene Geschwindigkeit maximal [x] km/h,
was innerhalb der zulaessigen Hoechstgeschwindigkeit liegt."]

III. BEWEISANTRAEGE

Zum Beweis fuer das Vorbringen werden folgende Beweismittel angeboten:
1. [z.B. Einvernahme des Beschuldigten]
2. [z.B. Vorlage des Eichscheins des Messgeraets]
3. [z.B. Zeuge [Name, Adresse]]
4. [z.B. Dashcam-Aufzeichnung vom [Datum]]

IV. ANTRAG

Ich beantrage,
1. das ordentliche Ermittlungsverfahren einzuleiten,
2. das Verwaltungsstrafverfahren einzustellen,
[hilfsweise: die Strafe schuld- und tatangemessen herabzusetzen.]

Mit vorzueglicher Hochachtung

[Unterschrift]
```

### Beschwerde gegen Straferkenntnis (§7 VwGVG) — Template:

```
An die
[Behoerde, die das Straferkenntnis erlassen hat]
[Adresse]

[Name, Adresse des Beschwerdefuehrers]

[Ort], am [Datum]

BESCHWERDE
gemaess §7 VwGVG

gegen das Straferkenntnis vom [Datum], GZ: [Geschaeftszahl],
zugestellt am [Datum],

wegen Uebertretung des [z.B. §20 Abs 2 StVO iVm §99 Abs 3 lit a StVO]

Innerhalb offener Frist erhebe ich gegen das oben bezeichnete
Straferkenntnis

B E S C H W E R D E

an das Landesverwaltungsgericht [Bundesland].

I. ANGEFOCHTENE PUNKTE

Das angefochtene Straferkenntnis wird
[  ] seinem gesamten Inhalt nach (Schuld und Strafe) angefochten.
[  ] hinsichtlich des Strafausmasses angefochten.
[  ] hinsichtlich folgender Punkte angefochten: [konkret]

II. BEGRUENDUNG

1. Sachverhalt:
[Chronologische Darstellung]

2. Rechtswidrige Beweiswuerdigung:
[Warum die Behoerde den Sachverhalt falsch festgestellt hat]

3. Unrichtige rechtliche Beurteilung:
[Warum die rechtliche Subsumtion falsch ist — §§-Zitate]

4. Fehlerhafte Strafbemessung:
[Warum die Strafe unangemessen hoch ist — §19 VStG: Erschwerungs-
und Milderungsgruende, Einkommenslage, Unbescholtenheit]

III. BEWEISANTRAEGE

1. [Beweismittel]
2. [Beweismittel]

IV. ANTRAEGE

1. Der Beschwerde wird stattgegeben und das angefochtene
   Straferkenntnis aufgehoben und das Verfahren eingestellt.

   Hilfsweise: Die Strafe wird auf ein tat- und schuldangemessenes
   Mass herabgesetzt.

2. Es wird die Durchfuehrung einer muendlichen Verhandlung
   gemaess §44 VwGVG beantragt.

[Unterschrift]
```

### Schadenersatzklage nach Verkehrsunfall — Template:

```
An das
[Bezirksgericht / Landesgericht] [Ort]

Klaeger/in: [Name, Adresse]
vertreten durch: [RA Name, Adresse] (bei LG Pflicht)

Beklagte/r: [Haftpflichtversicherer gemaess §26 KHVG]
             [Name der Versicherung, Adresse]

Streitwert: EUR [Gesamtforderung]

KLAGE
wegen Schadenersatz aus einem Verkehrsunfall

I. SACHVERHALT

1. Am [Datum] um [Uhrzeit] ereignete sich auf der [Strasse] in [Ort]
   ein Verkehrsunfall zwischen dem vom Klaeger gelenkten PKW
   [Marke, Kennzeichen] und dem bei der Beklagten haftpflichtversicherten
   PKW [Marke, Kennzeichen], gelenkt von [Name des Lenkers].

2. [Detaillierte Unfallschilderung: Wer fuhr wohin, was geschah, wie
   kam es zum Zusammenstoss]

3. [Unfallfolgen: Verletzungen, Fahrzeugschaden]

4. [Polizeiliche Unfallaufnahme: GZ der Anzeige]

II. HAFTUNG

1. Der Lenker des bei der Beklagten versicherten Fahrzeugs hat den
   Unfall verschuldet, indem er [z.B. "den Vorrang des Klaegers
   gemaess §19 Abs 4 StVO missachtet hat"].

2. Dieser Verstoss gegen §[x] StVO stellt eine Schutzgesetzverletzung
   iSd §1311 ABGB dar, weshalb die Beweislast fuer das Nichtverschulden
   den Schaediger trifft.

3. Die Beklagte haftet als Haftpflichtversicherer gemaess §26 KHVG
   direkt dem Geschaedigten.

III. SCHADEN

A. Sachschaden:
| Position | Betrag |
|----------|--------|
| Reparaturkosten (lt. SV-Gutachten ./A) | EUR [x] |
| Merkantile Wertminderung (lt. SV-Gutachten ./A) | EUR [x] |
| Mietwagenkosten ([x] Tage, ./B) | EUR [x] |
| Abschleppkosten (./C) | EUR [x] |
| Sachverstaendigenkosten | EUR [x] |
| **Sachschaden gesamt** | **EUR [x]** |

B. Personenschaden:
| Position | Betrag |
|----------|--------|
| Schmerzensgeld (§1325 ABGB) | EUR [x] |
| Heilungskosten (./D) | EUR [x] |
| Verdienstentgang (./E) | EUR [x] |
| **Personenschaden gesamt** | **EUR [x]** |

**Gesamtschaden: EUR [x]**

[Bei Mitverschulden: "Unter Beruecksichtigung eines Mitverschuldens
des Klaegers von [x]% (§1304 ABGB) reduziert sich der Anspruch auf
EUR [x]."]

IV. ZINSEN

Es werden Zinsen in Hoehe von 4% p.a. ab [Datum des Unfalls / Mahnung]
gemaess §1333 Abs 1 ABGB begehrt.

V. RECHTLICHE BEGRUENDUNG

[§1295 ABGB Verschuldenshaftung, §1 EKHG Gefaehrdungshaftung,
§1311 ABGB Schutzgesetzverletzung, §26 KHVG Direktanspruch,
§1325 ABGB Koerperliche Schaeden, §1332 ABGB Sachschaden]

VI. BEWEIS

1. Polizeilicher Unfallbericht, GZ [x] (./F)
2. KFZ-technisches Sachverstaendigengutachten (./A)
3. Medizinisches Sachverstaendigengutachten (zu bestellen)
4. Zeugeneinvernahme: [Name, Adresse]
5. Einvernahme des Klaegers als Partei
6. Urkunden: [Kostenvoranschlag, Rechnungen, Krankenunterlagen]

VII. ANTRAG

Der/Die Klaeger/in stellt den Antrag, die Beklagte schuldig zu
erkennen, dem/der Klaeger/in den Betrag von EUR [x] samt 4% Zinsen
ab [Datum] sowie die Kosten dieses Rechtsstreits binnen 14 Tagen
bei sonstiger Exekution zu bezahlen.

Beilagen:
./A — KFZ-Sachverstaendigengutachten
./B — Mietwagenrechnung
./C — Abschlepprechnung
./D — Aerztliche Befunde und Rechnungen
./E — Verdienstentgangsberechnung
./F — Polizeilicher Unfallbericht

[Unterschrift RA]
```

---

## Step 6: Present with Timeline and Next Steps

```markdown
# Verkehrsverfahren — Analyse und Handlungsempfehlung

**Verfahrensart:** [Einspruch / Beschwerde / Klage / Strafverfahren / etc.]
**Gegenstand:** [Strafverfuegung / Fuehrerscheinentzug / Schadenersatz / etc.]
**Zugestellt am:** [Datum]
**Zustaendige Behoerde/Gericht:** [BH/Magistrat/BG/LG]

## Fristenuebersicht
| Frist | Ablauf | Verbleibend | Status |
|-------|--------|-------------|--------|
| [Einspruch / Beschwerde / etc.] | [Datum] | [x] Tage | offen/kritisch/abgelaufen |
| [weitere Fristen] | [Datum] | [x] Tage | offen/kritisch/abgelaufen |

## Sachverhalt
[Zusammenfassung: Was ist passiert, was ist strittig]

## Rechtliche Beurteilung
[Analyse: Warum ist die Bestrafung/der Bescheid anfechtbar / Was sind die Erfolgsaussichten]
- §§-Zitate
- Relevante VwGH/LVwG/OGH-Judikatur

## Empfohlene Vorgehensweise

### Sofort-Massnahmen
1. [z.B. "Einspruch gegen Strafverfuegung einreichen bis [Datum]"]
2. [z.B. "Vorstellung gegen Mandatsbescheid (Fuehrerscheinentzug) bis [Datum]"]

### Verfahrensablauf (Timeline)
| Schritt | Frist | Aktion |
|---------|-------|--------|
| 1. [Einspruch/Beschwerde/Klage] | bis [Datum] | [Einbringung bei Behoerde/Gericht] |
| 2. Ordentliches Verfahren | ca. [x] Wochen | Behoerde ermittelt |
| 3. Straferkenntnis / Bescheid | ca. [x] Wochen | Entscheidung |
| 4. ggf. Beschwerde an LVwG | 4 Wochen nach Zustellung | Rechtsmittel |
| 5. ggf. Revision an VwGH | 6 Wochen nach LVwG-Erk. | Nur bei Rechtsfrage |

## Erfolgsaussichten
| Szenario | Wahrscheinlichkeit | Konsequenz |
|----------|-------------------|------------|
| Vollstaendiger Erfolg | [x]% | Einstellung / Aufhebung / voller Schadenersatz |
| Teilweiser Erfolg | [x]% | Reduktion der Strafe / teilweiser Schadenersatz |
| Kein Erfolg | [x]% | Strafe rechtskraeftig / Klage abgewiesen + Kosten |

## Entwurf des Schriftsatzes
[Hier den konkreten Einspruch / Beschwerde / Klage einfuegen]

## Risiken
- [z.B. "Beim Einspruch gegen Strafverfuegung: im ordentlichen Verfahren kann die Strafe HOEHER ausfallen"]
- [z.B. "Verschlechterungsverbot gilt NUR bei Beschwerde an LVwG (§42 VwGVG), NICHT beim Einspruch"]
- [z.B. "Prozesskostenrisiko bei Klage: EUR [x]"]

## Naechste Schritte
- [ ] [Konkreter erster Schritt mit Datum]
- [ ] [Zweiter Schritt]
- [ ] [Rechtsanwalt konsultieren fuer ...]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | Verfuegbar / Nicht verfuegbar | [connection status] |
| Gesetze | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Normen geprueft |
| Judikatur | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Pruefdatum | [YYYY-MM-DD] | |

---
Keine Rechtsberatung. Diese Analyse dient der verfahrensrechtlichen Ersteinschaetzung und ersetzt nicht die Beratung durch einen Rechtsanwalt. Insbesondere bei Fuehrerscheinentzug, Strafverfahren und hohen Schadenersatzanspruechen wird dringend anwaltliche Vertretung empfohlen. Aktuelle Gesetzestexte auf [ris.bka.gv.at](https://www.ris.bka.gv.at) pruefen.
```

---

## Critical Rules

1. **Fristen sind HEILIG** — Einspruch gegen Strafverfuegung: 2 Wochen (§49 VStG). Beschwerde gegen Straferkenntnis: 4 Wochen (§7 VwGVG). Vorstellung gegen Mandatsbescheid: 2 Wochen (§57 Abs 2 AVG). Immer als ERSTES die Frist berechnen und prominent anzeigen.
2. **Zustelldatum ist entscheidend** — Die Frist beginnt mit der Zustellung (RSa-Sendung!), nicht mit dem Bescheiddatum. Immer nach dem Zustelldatum fragen.
3. **Einspruch vs. Beschwerde nicht verwechseln** — Einspruch gegen Strafverfuegung (§49 VStG, 2 Wochen) ist KEIN Rechtsmittel im eigentlichen Sinn — es bewirkt das ordentliche Verfahren. Beschwerde gegen Straferkenntnis (§7 VwGVG, 4 Wochen) ist das eigentliche Rechtsmittel.
4. **Verschlechterungsverbot differenzieren** — Beim Einspruch gegen Strafverfuegung: KEIN Verschlechterungsverbot (Strafe kann hoeher werden). Bei Beschwerde an LVwG: Verschlechterungsverbot (§42 VwGVG), wenn nur Beschuldigter Beschwerde erhebt. Das MUSS dem User mitgeteilt werden.
5. **Fuehrerscheinentzug: aufschiebende Wirkung klaeren** — Vorstellung gegen Mandatsbescheid hat KEINE aufschiebende Wirkung. Beschwerde an LVwG grundsaetzlich JA, aber oft ausgeschlossen bei Alkohol/Drogen.
6. **Direktklage §26 KHVG immer erwaehnen** — Bei Verkehrsunfaellen kann der Geschaedigte direkt den Haftpflichtversicherer klagen. Das ist oft der bessere Weg (Zahlungsfaehigkeit!).
7. **Lenkererhebung: Pflicht, kein Wahlrecht** — §103 Abs 2 KFG ist eine Auskunftspflicht. Verweigerung ist eigene Verwaltungsuebertretung bis 5.000 EUR. Das muss der User wissen.
8. **Diversion im Strafverfahren prufen** — Bei §§80, 81, 88, 89 StGB immer Diversionsmoeglichkeit ansprechen — keine Vorstrafe!
9. **§§ immer mit Gesetzesname** — §49 VStG, nicht nur "§49". §26 KHVG, nicht "§26". §7 VwGVG, nicht "§7".
10. **Match user's language** — German in, German out. English in, English out. Gesetze immer in deutscher Form.
