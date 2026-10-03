---
name: recht-steuer-momarcode1
title: /recht steuer — Steuerrechtliche Analyse
description: Austrian tax law analysis — income tax (EStG), corporate tax (KStG), VAT (UStG), municipal tax (KommStG), tax procedure (BAO), and fiscal criminal law (FinStrG). Analyzes tax obligations, deductions, exemptions, and identifies optimization opportunities within legal bounds.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-steuer
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: tax
language: de
sources:
- title: Ogh case presentation
  path: references/ogh-case-presentation.md
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht steuer — Steuerrechtliche Analyse

When the user describes a tax situation, presents documents (Bescheide, Steuererklärungen, Verträge), or asks about Austrian tax obligations, follow these steps.

---

## Step 1: Read the Facts / Documents

Read everything the user has provided. You need:

1. **Who is the taxpayer?** — Natürliche Person or juristische Person (GmbH, AG, Verein, Stiftung)?
2. **What type of income/transaction?** — Employment, business, capital gains, rental, sale of property?
3. **What is the time period?** — Which Veranlagungsjahr? Are prior years affected?
4. **What is the user's goal?** — Understand obligations? Optimize taxes? Check a Bescheid? Prepare a Steuererklärung?
5. **Relevant numbers?** — Income amounts, expenses, asset values, dates of transactions

If critical facts are missing, ask. Be specific:
> "Sind Sie als natürliche Person oder als Gesellschaft (GmbH, etc.) betroffen? Das bestimmt, ob EStG oder KStG anwendbar ist."

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references (VwGH, BFG), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

Search RIS Justiz for relevant VwGH/BFG decisions on disputed legal questions. Present using format from `references/ogh-case-presentation.md` (adapted for VwGH/BFG Geschäftszahlen).

---

## Step 3: Classify the Tax Situation

Determine what taxes and which legal framework apply. Check each:

### A: Subjekt — Who is the taxpayer?

| Subjekt | Anwendbares Gesetz | Steuersatz |
|---------|-------------------|------------|
| Natürliche Person (unselbständig) | EStG — Lohnsteuer (§§47ff) | Progressiv 0-55% |
| Natürliche Person (selbständig) | EStG — Einkommensteuer (§§1ff) | Progressiv 0-55% |
| Natürliche Person (Einkünfte aus Kapitalvermögen) | EStG §27, §27a | KESt 27,5% |
| GmbH | KStG (§§1ff) | 23% (ab 2024, zuvor 24% in 2023, 25% bis 2022) |
| AG | KStG (§§1ff) | 23% |
| Privatstiftung | KStG §13 (Zwischenbesteuerung) | Zwischensteuer 25%, KESt bei Zuwendung |
| Verein | KStG §§1, 5 | 23% auf nicht-begünstigte Einkünfte |
| Personengesellschaft (OG, KG) | EStG — transparent, Gewinn wird Gesellschaftern zugerechnet | Progressiv beim Gesellschafter |

### B: Einkunftsart (§2 EStG)

Determine which of the 7 Einkunftsarten applies. This controls Gewinnermittlung, Verlustausgleich, and Sozialversicherung:

| Einkunftsart | §§ EStG | Gewinnermittlung | SVA-pflichtig? |
|-------------|---------|------------------|----------------|
| 1. Land- und Forstwirtschaft | §21 | §4 Abs 1 oder Pauschalierung | Ja (SVS) |
| 2. Selbständige Arbeit | §22 | §4 Abs 3 (EAR) oder §4 Abs 1 | Ja (SVS) |
| 3. Gewerbebetrieb | §23 | §4 Abs 1, §4 Abs 3, oder §5 (UGB) | Ja (SVS) |
| 4. Nichtselbständige Arbeit | §25 | Arbeitgeber berechnet LSt | Ja (ASVG) |
| 5. Kapitalvermögen | §27 | KESt-Abzug oder Veranlagung | Nein |
| 6. Vermietung und Verpachtung | §28 | Überschussrechnung (§§15-16) | Nein (außer gewerblich) |
| 7. Sonstige Einkünfte | §29 | Überschussrechnung | Nein |

**Abgrenzungsfragen:**
- Gewerbebetrieb vs. Vermögensverwaltung: OGH/VwGH-Judikatur zur Gewerblichkeit (Nachhaltigkeit, Gewinnabsicht, Beteiligung am wirtschaftlichen Verkehr)
- Gewerbebetrieb vs. selbständige Arbeit: §22 EStG — wissenschaftliche, künstlerische, schriftstellerische, unterrichtende, erzieherische Tätigkeit = §22
- Sonstige Einkünfte §29: Spekulationsgeschäfte (§30 — Grundstücke 30% ImmoESt, §31 — Beteiligungen KESt 27,5%)

---

## Step 4: Systematic Tax Analysis

For each identified tax, work through the full analysis:

### 4A: Einkommensteuer / Lohnsteuer (EStG)

**Progressionsstufen (§33 Abs 1 EStG, ab Veranlagung 2024):**

| Einkommensstufe | Steuersatz |
|----------------|------------|
| bis €12.816 | 0% |
| €12.816 – €20.818 | 20% |
| €20.818 – €34.513 | 30% |
| €34.513 – €66.612 | 40% |
| €66.612 – €99.266 | 48% |
| €99.266 – €1.000.000 | 50% |
| über €1.000.000 | 55% |

**Check Absetzbeträge (§§33 Abs 3ff EStG):**
- [ ] Verkehrsabsetzbetrag (§33 Abs 5 Z 1): €463 (Arbeitnehmer)
- [ ] Zuschlag zum Verkehrsabsetzbetrag bei niedrigem Einkommen
- [ ] Pensionistenabsetzbetrag (§33 Abs 6)
- [ ] Alleinverdiener-/Alleinerzieherabsetzbetrag (§33 Abs 4): €572 + Kinderzuschlag
- [ ] Unterhaltsabsetzbetrag (§33 Abs 4 Z 3)
- [ ] Familienbonus Plus (§33 Abs 3a): bis €2.000/Kind (bis 18 J.) bzw. €700 (ab 18 J.)
- [ ] SV-Rückerstattung (§33 Abs 8): bei geringem Einkommen

**Check Sonderausgaben (§18 EStG):**
- [ ] Kirchenbeitrag (§18 Abs 1 Z 5): max €400/Jahr
- [ ] Steuerberatungskosten
- [ ] Spenden an begünstigte Organisationen (§18 Abs 1 Z 7): max 10% des Gesamtbetrags der Einkünfte
- [ ] Nachkauf von Versicherungszeiten (§18 Abs 1 Z 1a)
- [ ] Verlustabzug (§18 Abs 6-7): Vorjahresverluste aus betrieblichen Einkünften, 75%-Grenze

**Check Werbungskosten (§16 EStG) bei nichtselbständiger Arbeit:**
- [ ] Pauschale Werbungskosten: €132/Jahr automatisch (§16 Abs 3)
- [ ] Pendlerpauschale (§16 Abs 1 Z 6): klein (ab 20km, Öffi zumutbar) oder groß (ab 2km, Öffi unzumutbar)
- [ ] Arbeitsmittel (§16 Abs 1 Z 7): Computer, Telefon, Fachliteratur
- [ ] Fortbildungskosten (§16 Abs 1 Z 10)
- [ ] Doppelte Haushaltsführung und Familienheimfahrten (§16 Abs 1 Z 6)
- [ ] Homeoffice-Pauschale (§16 Abs 1 Z 7a): max €3/Tag, max 100 Tage = €300/Jahr

**Check Pauschalierung (§17 EStG):**
- Basispauschalierung: 12% der Umsätze (max €220.000 Umsatz), bei bestimmten Tätigkeiten 6%
- Branchenpauschalierungen: Gastronomie, Lebensmittel, Drogisten etc. (§17 Abs 4 + VO)
- Kleinunternehmerpauschalierung (§17 Abs 3a): bis €220.000 Umsatz, pauschal 45% (DL) bzw. 20% Betriebsausgaben

**Check Veranlagung:**
- Pflichtveranlagung (§41 Abs 1 EStG): mehrere Dienstgeber, Nebeneinkünfte >€730, etc.
- Antragsveranlagung (§41 Abs 2 EStG): freiwillig, wenn Erstattung zu erwarten
- Frist: Papiererklärung bis 30.4. des Folgejahres, FinanzOnline bis 30.6. (§134 BAO)
- Frist mit Steuerberater: automatisch bis 31.3. des übernächsten Jahres (Quotenregelung)

### 4B: Körperschaftsteuer (KStG)

- **Steuersatz:** 23% (§22 Abs 1 KStG, ab 2024)
- **Mindestkörperschaftsteuer:** €500/Quartal für GmbH (§24 Abs 4 KStG), anrechenbar auf künftige KöSt
- **Gruppenbesteuerung (§9 KStG):**
  - Voraussetzung: finanzielle Verbindung >50% + Gruppenantrag beim Finanzamt
  - Wirkung: Verluste der Gruppenmitglieder werden beim Gruppenträger verrechnet
  - Auslandsverluste: nur im Ausmaß der Beteiligung, Nachversteuerung bei Verwertung im Ausland
- **Privatstiftung (§13 KStG):**
  - Zuwendungen der Stiftung an Begünstigte: KESt 27,5% (§27 Abs 5 Z 7 EStG)
  - Zwischenbesteuerung (§13 Abs 3 KStG): 25% auf bestimmte Kapitaleinkünfte
  - Substiftungsmodelle: VwGH-Judikatur beachten
- **Verdeckte Gewinnausschüttung:**
  - GmbH-Gesellschafter-Geschäftsführer: Angemessenheitsprüfung der Bezüge
  - Vorteil an Gesellschafter, der einem Fremden nicht gewährt worden wäre = verdeckte Ausschüttung
  - Steuerfolge: bei GmbH keine Betriebsausgabe + KESt 27,5% beim Gesellschafter

### 4C: Umsatzsteuer (UStG)

**Steuersätze (§10 UStG):**
| Satz | Anwendung | §§ |
|------|-----------|-----|
| 20% | Normalsteuersatz | §10 Abs 1 |
| 10% | Ermäßigt: Lebensmittel, Bücher, Personenbeförderung, Miete (Wohnen), Medikamente | §10 Abs 2 |
| 13% | Ermäßigt: Pflanzen, Kunstgegenstände, Beherbergung, Filmvorführungen | §10 Abs 3 |
| 0% | Echt steuerbefreit: Ausfuhrlieferungen, ig. Lieferungen | §6 Abs 1, §7 |

**Kleinunternehmerregelung (§6 Abs 1 Z 27 UStG):**
- Umsatzgrenze: €42.000/Jahr netto (ab 2025, zuvor €35.000)
- Wirkung: unecht steuerbefreit = keine USt in Rechnung stellen, KEIN Vorsteuerabzug
- Option zur Regelbesteuerung möglich (§6 Abs 3 UStG) — bindet für 5 Jahre
- Einmalige Überschreitung um max 15% unschädlich

**Vorsteuerabzug (§12 UStG):**
- Voraussetzung: Unternehmer, Leistung für das Unternehmen, ordnungsgemäße Rechnung (§11)
- Rechnungsmerkmale §11 prüfen: Name, Adresse, UID, Datum, Leistungsbeschreibung, Entgelt, Steuersatz, Steuerbetrag
- Vorsteuerberichtigung (§12 Abs 10-12): bei Änderung der Verhältnisse, 5 Jahre (beweglich) bzw. 20 Jahre (Grundstücke)
- Vorsteuerausschluss: §12 Abs 3 — Repräsentation, PKW (außer Fahrschulfahrzeuge, Taxis etc.)

**Innergemeinschaftlicher Erwerb / Lieferung:**
- ig. Lieferung (§6 Abs 1 Z 1, Art 7 UStG): steuerbefreit mit Vorsteuerabzug, wenn UID des Empfängers, Gelangensnachweis
- ig. Erwerb (Art 1 UStG): Erwerbsteuer im Bestimmungsland
- Zusammenfassende Meldung (§21 Abs 3 UStG): monatlich/quartalsweise

**Reverse Charge (§19 Abs 1 zweiter Satz UStG):**
- Steuerschuldnerschaft geht auf Leistungsempfänger über
- Bei Bauleistungen (§19 Abs 1a), Schrott (§19 Abs 1d), wenn ausländischer Unternehmer leistet
- Empfänger schuldet und kann gleichzeitig Vorsteuer abziehen

**Fristen:**
- UVA monatlich (Umsatz >€100.000 Vorjahr) oder quartalsweise: bis 15. des zweitfolgenden Monats
- USt-Jahreserklärung: bis 30.4. (Papier) / 30.6. (FinanzOnline) des Folgejahres

### 4D: Kommunalsteuer (KommStG)

- **Steuersatz:** 3% der Bemessungsgrundlage (§9 KommStG)
- **Steuerschuldner:** Arbeitgeber (§5 KommStG)
- **Bemessungsgrundlage (§5 KommStG):** Summe der Arbeitslöhne = Bruttobezüge iSd §25 EStG
  - Inklusive: Gehälter, Löhne, Sonderzahlungen, Sachbezüge, freie DN-Geschäftsführer-Bezüge
  - Exklusive: echte Reisekosten, Abfertigung Neu (BMSVG-Beiträge)
- **Freibetrag:** €1.460/Monat (§7 KommStG, ab 2024)
- **Erklärung:** jährlich bis 31.3. des Folgejahres bei der Gemeinde
- **Vorauszahlung:** monatlich bis 15. des Folgemonats

### 4E: Weitere Steuern und Abgaben — Check

- [ ] **Grunderwerbsteuer (GrEStG):** 3,5% (2% bei nahen Angehörigen), Anteilsvereinigung beachten
- [ ] **Immobilienertragsteuer (§30 EStG):** 30% auf Veräußerungsgewinn (Neuvermögen ab 1.4.2012)
- [ ] **Kapitalertragsteuer (§27a EStG):** 27,5% auf Dividenden, Zinsen, Kursgewinne
- [ ] **Normverbrauchsabgabe (NoVAG):** bei Kfz-Zulassung
- [ ] **Dienstgeberbeitrag (DB) zum FLAF:** 3,7% der Bruttolöhne (§41 FLAG)
- [ ] **Zuschlag zum DB (DZ):** je nach Bundesland 0,34-0,42%
- [ ] **Kammerumlage (§122 WKG):** Zuschlag zur Vorsteuer

---

## Step 5: Calculate Tax Implications

Where the user has provided concrete numbers, calculate:

1. **Steuerbemessungsgrundlage** — Einkünfte minus Freibeträge, Sonderausgaben, Werbungskosten
2. **Steuerschuld** — nach Tarif (§33 EStG) oder Flat Rate (KStG)
3. **Absetzbeträge** — abziehen von der Steuerschuld
4. **Vorsteuer** — gegen USt-Schuld aufrechnen
5. **Effektive Steuerbelastung** — Gesamtsteuer / Gesamteinkünfte in %

Show the calculation step by step. Use tables for clarity.

**Optimierungsmöglichkeiten prüfen:**
- Gewinnfreibetrag (§10 EStG): bis 15% des Gewinns, max €46.400 (Grundfreibetrag €33.000 ohne Nachweis)
- Investitionsfreibetrag (§11 EStG): 10% (bzw. 15% für Ökologisierung) der Anschaffungskosten
- Forschungsprämie (§108c EStG): 14% der Forschungsaufwendungen
- 13./14. Gehalt: begünstigt besteuert (6% Lohnsteuer bis €620 frei, dann 6% bis Jahressechstel §67 EStG)
- Zukunftssicherung (§3 Abs 1 Z 15 EStG): AG-Beiträge bis €300/Jahr steuerfrei
- Mitarbeitergewinnbeteiligung (§3 Abs 1 Z 35 EStG): bis €3.000/Jahr steuerfrei
- Gruppenbesteuerung bei Konzernen prüfen
- Timing: Vorauszahlungen anpassen (§45 EStG), Investitionen vorziehen/verschieben

---

## Step 6: Present Findings

```markdown
# Steuerrechtliche Analyse

**Steuerpflichtiger:** [natürliche/juristische Person, Bezeichnung]
**Veranlagungszeitraum:** [Jahr(e)]
**Einkunftsart(en):** [§§ EStG]
**Betroffene Steuern:** [EStG, KStG, UStG, KommStG, etc.]

## Zusammenfassung
[2-3 Sätze: Welche Steuern fallen an, grobe Höhe, wichtigstes Optimierungspotenzial]

## Steuerliche Einordnung
| Kriterium | Einordnung |
|-----------|-----------|
| Steuersubjekt | [natürliche/juristische Person] |
| Einkunftsart | [§x EStG] |
| Gewinnermittlungsart | [§4/1, §4/3, §5 EStG] |
| USt-Status | [Regelbesteuerung / Kleinunternehmer] |
| SV-Pflicht | [ASVG / SVS / keine] |

## Steuerberechnung
| Position | Betrag |
|----------|--------|
| Einkünfte | €[x] |
| - Sonderausgaben (§18) | -€[x] |
| - Werbungskosten/Betriebsausgaben | -€[x] |
| - Gewinnfreibetrag (§10) | -€[x] |
| **Steuerbemessungsgrundlage** | **€[x]** |
| ESt/KSt laut Tarif | €[x] |
| - Absetzbeträge | -€[x] |
| **Steuerschuld** | **€[x]** |
| Effektiver Steuersatz | [x]% |

## Umsatzsteuer
| Position | Betrag |
|----------|--------|
| Umsätze 20% | €[x] |
| Umsätze 10% | €[x] |
| USt gesamt | €[x] |
| - Vorsteuer | -€[x] |
| **USt-Zahllast** | **€[x]** |

## Optimierungsmöglichkeiten
| Maßnahme | Ersparnis | Grundlage | Umsetzung |
|----------|-----------|-----------|-----------|
| [Maßnahme 1] | €[x] | §[x] | [Beschreibung] |
| [Maßnahme 2] | €[x] | §[x] | [Beschreibung] |

## ⚠️ Risiken und Warnungen
[Verdeckte Gewinnausschüttung? Liebhaberei (§1 LiebhabereiVO)? Finanzstrafrechtliche Risiken?]

## Fristen
| Pflicht | Frist | §§ |
|---------|-------|----|
| ESt-Erklärung | 30.6. (FinanzOnline) | §134 BAO |
| USt-Voranmeldung | 15. des 2. Folgemonats | §21 UStG |
| KommSt-Erklärung | 31.3. des Folgejahres | §11 KommStG |

## Nächste Schritte
1. [Konkrete Handlung]
2. [Konkrete Handlung]
3. [Steuerberater konsultieren für ...]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | [connection status] |
| Gesetze | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---
⚠️ **Keine Steuerberatung.** Diese Analyse dient der steuerrechtlichen Ersteinschätzung und ersetzt nicht die Beratung durch einen Steuerberater oder Wirtschaftsprüfer. Steuersätze und Grenzbeträge können sich jährlich ändern — aktuelle Werte auf [bmf.gv.at](https://www.bmf.gv.at) und [ris.bka.gv.at](https://www.ris.bka.gv.at) prüfen.
```

---

## Critical Rules

1. **Always cite specific §§ with Gesetzesname** — Never "laut Steuerrecht" without §18 Abs 1 Z 5 EStG, §12 UStG, etc.
2. **Distinguish EStG vs. KStG** — Natürliche Person = EStG, juristische Person = KStG. Never apply the wrong Tarif.
3. **Check the Veranlagungsjahr** — Steuersätze, Freibeträge und Grenzbeträge ändern sich jährlich. Immer das korrekte Jahr verwenden. Im Zweifel nachfragen.
4. **Keine aggressive Steuerplanung** — Only recommend optimization within clear legal bounds. Flag anything that approaches §22 BAO (Missbrauch von Formen) or FinStrG territory.
5. **Kleinunternehmergrenze prüfen** — €42.000 ab 2025, vorher €35.000. Überschreitung hat massive USt-Nachfolgen.
6. **Verdeckte Gewinnausschüttung bei GmbH immer prüfen** — Gesellschafter-Geschäftsführer-Bezüge, Privatnutzung, Darlehen an Gesellschafter.
7. **Sozialversicherung mitdenken** — SVS-Pflichtversicherung bei selbständigen Einkünften, ASVG bei Dienstnehmern. SV ist oft höher als die Steuer bei kleinen Einkünften.
8. **USt-Rechnungsmerkmale (§11 UStG) ernst nehmen** — Fehlende Merkmale = kein Vorsteuerabzug für den Empfänger.
9. **Use RIS if connected** — Verify statute citations are current, especially Steuersätze and Freibeträge.
10. **Match user's language** — German in → German out. English in → English out. Gesetze immer in deutscher Form (§33 EStG).
