---
name: recht-compliance-momarcode1
title: /recht compliance — Compliance-Pruefung
description: Compliance gap analysis for Austrian law — KSchG, DSGVO/DSG, MRG, UGB, GewO, ArbVG, FAGG. For contracts, websites, and business operations.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-compliance
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: regulatory
language: de
sources:
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht compliance — Compliance-Pruefung

Checks documents, websites, or business operations against Austrian regulatory requirements. Performs a systematic, framework-by-framework compliance gap analysis with scoring, violation details, Rechtsfolgen, and prioritized remediation.

---

## Procedure

### Step 1: Read and Understand the Input

Read the entire document, URL, or business description provided by the user. Identify:
- What type of input is it? (contract, AGB, website, business operation description, Datenschutzerklaerung, Mietvertrag, Arbeitsvertrag, combination)
- Who are the parties? (natural persons, legal entities, consumers, entrepreneurs)
- What is the subject matter? (sale of goods, services, tenancy, employment, data processing, e-commerce)
- What jurisdiction indicators are present? (Gerichtsstand clauses, applicable law clauses, Austrian addresses, .at domain)

If the input is a URL, fetch and read the page content. For websites, also check for Impressum and Datenschutzerklaerung pages.

If the input is a file, read it completely before proceeding.

### Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

### Step 3: Ask Clarifying Questions

Before running the analysis, determine the following. Ask the user if not clear from the document:

1. **Entity type of the provider/drafter:** Einzelunternehmer, GmbH, AG, OG, KG, Verein, or other?
2. **B2B or B2C?** Is the counterparty a Verbraucher (consumer) per §1 KSchG? If the document could apply to both, assume B2C (worst case).
3. **Industry/sector:** Is the business in a regulated sector? (Finanzdienstleistungen, Gesundheit, Telekommunikation, Immobilien, Gastronomie, Handel, IT/Software, etc.)
4. **Scope of check:** Is this a contract review, website compliance check, business operation check, or all three?
5. **Online/Fernabsatz?** Is this an online business, distance selling, or Haustuergeschaeft? (triggers FAGG/ECG)
6. **Employees?** Does the entity have employees? (triggers Arbeitsrecht)
7. **Personal data processing?** Does the entity process personal data? (triggers DSGVO/DSG — almost always yes)

If the document clearly answers these questions, state your assumptions and proceed. Only ask the user when genuinely ambiguous.

### Step 4: Determine Applicable Frameworks

Based on Step 3, select which frameworks apply. Not all frameworks apply to every document:

| Situation | Applicable Frameworks |
|---|---|
| B2C contract or AGB | KSchG (always), FAGG (if online/Fernabsatz), ABGB |
| Any document/operation with personal data | DSGVO + DSG |
| Mietvertrag (tenancy agreement) | MRG (check §1 MRG Anwendungsbereich first!), ABGB |
| Arbeitsvertrag (employment contract) | AngG, AZG, UrlG, ArbVG, GlBG, applicable KollV |
| B2B contract | UGB (§377 Ruegepflicht, §347 Sorgfalt), ABGB |
| Business operation | GewO (Gewerbeberechtigung) |
| Website or App | ECG (Impressum §5), DSGVO (Datenschutzerklaerung), FAGG (if e-commerce), TKG 2021 (cookies) |
| E-Commerce / Online-Shop | FAGG (§§1-18), ECG, PrAG (Preisauszeichnung), VGG (Verbrauchergewinnspielgesetz if applicable) |

List the applicable frameworks explicitly before proceeding. For each, state WHY it applies.

### Step 5: Run Each Applicable Framework Systematically

For each applicable framework, run the sub-step below. Skip frameworks that do not apply (state "not applicable" with reason). For each check within a framework, assign one of:
- **Konform** — requirement is met
- **Luecke** (gap) — requirement is not addressed but no active violation
- **Verstoss** (violation) — active breach of mandatory law

---

#### Step 5A: KSchG Compliance (if B2C)

**Prerequisite:** Confirm the counterparty is a Verbraucher per §1 Abs 1 KSchG (person for whom the transaction is not part of their business). If B2B, skip this framework entirely.

Check EACH of the following provisions against the document:

**§6 Abs 1 — Nichtige Vertragsbestimmungen (absolute Nichtigkeit):**
For each Ziffer, check if any clause in the document violates it:

- Z 1: Clauses allowing the entrepreneur to withdraw or modify without important reason
- Z 2: Clauses giving entrepreneur alone the right to determine whether performance is contract-conforming
- Z 3: Clauses setting unreasonably short deadlines for consumer's claims (Gewaehrleistung, Schadenersatz)
- Z 4: Clauses allowing entrepreneur to set unreasonably long performance deadlines
- Z 5: Clauses allowing unlimited price increases within 2 months of contract conclusion
- Z 6: Clauses limiting consumer's right to withhold payment (Zurueckbehaltungsrecht)
- Z 7: Clauses excluding entrepreneur's liability for agents (Erfuellungsgehilfen)
- Z 8: Clauses requiring disproportionate penalties from consumer
- Z 9: Clauses making consumer's declarations irrevocable without equivalent entrepreneur commitment
- Z 10: Clauses deeming silence as acceptance by consumer
- Z 11: Clauses restricting consumer's right to offset (Aufrechnung) with undisputed or court-confirmed claims
- Z 12: Clauses shifting burden of proof to consumer's disadvantage
- Z 13: Clauses requiring consumer to accept unknown contract terms
- Z 14: Clauses waiving consumer's right to choose a Rechtsanwalt
- Z 15: Clauses creating exclusive jurisdiction (Gerichtsstandsvereinbarung) disadvantageous to consumer
- Z 16: Clauses shortening Verjaeherungsfrist for Gewaehrleistung below statutory minimum
- Z 17: Clauses making consumer's rights dependent on fulfilling special formalities beyond statutory requirements
- Z 18: Clauses restricting consumer's rights under Gewaehrleistung (§§922ff ABGB)

For each Ziffer: state **konform / Verstoss / nicht anwendbar**. If Verstoss, quote the offending clause and explain.

**§6 Abs 2 — Bedingt nichtige Klauseln (void unless individually negotiated):**
Check for clauses that are void unless the entrepreneur proves individual negotiation:
- Z 1: Clauses in AGB or Vertragsformblatt that are unusual (ueberraschende Klauseln)
- Z 2: Clauses deviating from dispositives Recht to consumer's disadvantage (geltungserhaltende Reduktion does NOT apply)
- Z 3: Clauses unclear or ambiguous (contra proferentem / Unklarheitenregel)

**§6 Abs 3 — Transparenzgebot:**
Check if ALL clauses are clear, understandable, and transparent. Intransparente Klauseln are void even if substantively permissible. Look for:
- Overly complex or legalistic language
- Internal contradictions
- Hidden disadvantages buried in dense text
- References to other documents not provided

**§9 — Geltungskontrolle:**
Check if AGB/Vertragsformblatt as a whole is grossly disadvantageous (groeblich benachteiligend) to the consumer.

**§14 — Gerichtsstand:**
Check if a Gerichtsstandsvereinbarung exists. For consumers, §14 KSchG limits permissible Gerichtsstand to consumer's Wohnsitz, gewoehnlicher Aufenthalt, Arbeitsort, or the Erfuellungsort per §905 ABGB.

**Rechtsfolge for KSchG violations:** Absolute Nichtigkeit per §6 Abs 1 (clause is void, rest of contract remains). Relative Nichtigkeit per §6 Abs 2 (void unless individually negotiated). The consumer can invoke Nichtigkeit; the entrepreneur cannot.

---

#### Step 5B: DSGVO / DSG Compliance (if personal data is processed)

**Prerequisite:** Identify what personal data is processed (names, email, IP addresses, payment data, location data, biometric data, health data, etc.) and who the data subjects are (customers, employees, website visitors, etc.).

Check each of the following:

**Art 6 DSGVO — Rechtsmaessigkeit der Verarbeitung:**
- Is a lawful basis identified for each processing activity?
- If consent (Art 6 Abs 1 lit a): Is it freely given, specific, informed, unambiguous? Can it be withdrawn as easily as given (Art 7 Abs 3)?
- If contract (Art 6 Abs 1 lit b): Is the processing genuinely necessary for contract performance?
- If legitimate interest (Art 6 Abs 1 lit f): Is the balancing test documented?
- Are special categories of data involved (Art 9)? If so, is there an Art 9 Abs 2 exception?

**Art 13/14 DSGVO — Informationspflichten:**
Check the Datenschutzerklaerung (privacy policy) for ALL mandatory elements:
- Identity and contact details of the Verantwortlicher (controller)
- Contact details of the Datenschutzbeauftragter (DPO), if appointed
- Purposes and lawful basis for each processing activity
- Legitimate interests pursued (if Art 6 Abs 1 lit f)
- Recipients or categories of recipients
- Transfer to third countries and safeguards (Art 44-49)
- Retention periods (Speicherdauer) or criteria to determine them
- Data subject rights (Auskunft, Berichtigung, Loeschung, Einschraenkung, Datenportabilitaet, Widerspruch)
- Right to withdraw consent (if consent-based)
- Right to lodge a complaint with the Datenschutzbehoerde (dsb.gv.at)
- Whether provision of data is statutory/contractual requirement and consequences of non-provision
- Automated decision-making including profiling (Art 22)

**Art 28 DSGVO — Auftragsverarbeitung:**
- Are third-party processors used (hosting providers, analytics, email services, payment processors)?
- Is there a written Auftragsverarbeitervertrag (AVV) for each processor?
- Does the AVV contain all mandatory elements per Art 28 Abs 3?

**Art 30 DSGVO — Verarbeitungsverzeichnis:**
- Does the entity maintain a record of processing activities? (mandatory for >250 employees, or if processing is not occasional, or if it involves special categories or criminal data)

**Art 35 DSGVO — Datenschutz-Folgenabschaetzung (DSFA/DPIA):**
- Is the processing likely to result in high risk? (e.g., systematic monitoring, large-scale processing of special categories, profiling with legal effects)
- If yes, has a DPIA been conducted?

**§12 DSG — Bildverarbeitung:**
- Is image/video data processed (CCTV, photos)?
- If yes, is there a lawful basis? Are the specific Austrian requirements per §12 DSG met?
- Kennzeichnungspflicht (signage obligation) for video surveillance?

**§2 Abs 4 DSG — Austrian exemptions:**
- Check if any Austrian-specific exemptions apply (household exemption, journalistic purposes, etc.)

**TKG 2021 §165 — Cookies and Tracking:**
- Does the website use cookies or tracking technologies?
- Is there a cookie banner with opt-in for non-essential cookies?
- Are analytics tools (Google Analytics, etc.) configured to comply?

**Rechtsfolgen for DSGVO violations:**
- Art 83 DSGVO: Bussgelder up to EUR 20 Mio or 4% of global annual turnover
- Art 82 DSGVO: Schadenersatzanspruch der Betroffenen (including immaterieller Schaden)
- §30 DSG: Verwaltungsstrafen
- Bescheide der Datenschutzbehoerde: Verarbeitungsverbote, Loeschungsanordnungen

---

#### Step 5C: MRG Compliance (if tenancy)

**Prerequisite — §1 MRG Anwendungsbereich:**
First determine if the MRG applies at all:
- Is the object a Mietgegenstand (Wohnung, Geschaeftsraum)?
- Check §1 Abs 2 MRG exclusions: Zweitwohnungen in Haeusern mit max 2 Mietgegenstaenden, Dienstwohnungen, Ferienwohnungen (certain), Genossenschaftswohnungen (WGG applies instead)
- Check §1 Abs 4 MRG: Neubauten after 30.06.1953? Dachgeschossausbau/Zubau after 31.12.2001? These may fall under Teilanwendung (only certain sections apply)
- Vollausnahme, Teilanwendung, or Vollanwendung? This determines which checks below are relevant.

If MRG applies (Voll- or Teilanwendung), check:

**§§15-16 MRG — Mietzins:**
- Vollanwendung: Is the Mietzins within Richtwertmietzins (§16 Abs 2) or angemessener Mietzins (§16 Abs 1)? Check Richtwert for the applicable Bundesland.
- Are Betriebskosten correctly itemized per §21 MRG?
- Are Zuschlaege/Abschlaege per §16 Abs 2 Z 1-6 correctly applied?

**§29 MRG — Befristung:**
- If the Mietvertrag is befristet: minimum duration is 3 years (§29 Abs 1 Z 3 lit a)
- Befristung must be in writing (schriftlich)
- After expiry, if tenant stays and landlord does not object within 14 days, contract renews for 3 years (Erneuerungsfiktion)

**§30 MRG — Kuendigung:**
- Are Kuendigungsgruende limited to the taxative list in §30 Abs 2 Z 1-16?
- Does the contract contain Kuendigungsgruende beyond the statutory list? (void if so)
- Kuendigungsfrist for landlord: at minimum as per §560 ZPO (1 month to Monatsletzten for Wohnung)

**§§3, 8 MRG — Erhaltungspflichten:**
- Does the contract improperly shift Erhaltungspflichten to the tenant?
- §3 MRG: Landlord must maintain the building's general parts, eliminate serious Schaeden, maintain communal facilities
- §8 MRG: Tenant's Erhaltungspflicht is limited to minor maintenance (Bagatellreparaturen are disputed)

**§27 MRG — Verbotene Ablösen:**
- Does the contract require Abloesen (key money, Investitionsablöse beyond justified amounts)?
- Verbotene Ablösen are void and recoverable for 10 years (§27 Abs 3 MRG)

**Rechtsfolgen for MRG violations:**
- Mietzinsueberschreitung: Mieter can challenge at Schlichtungsstelle/BG within 3 years (laufender Mietzins) or any time (vereinbarter Mietzins above Kategoriemietzins)
- Void Kuendigungsgruende: Kuendigung ist unwirksam
- Verbotene Ablösen: Rueckforderung innerhalb von 10 Jahren
- §37 MRG Ausserstreitverfahren at BG

---

#### Step 5D: Arbeitsrecht Compliance (if employment)

**Prerequisite:** Confirm this is an Arbeitsvertrag (not a freier Dienstvertrag or Werkvertrag). Check for personal dependency (persoenliche Abhaengigkeit) indicators: fixed working hours, integration in employer's organization, duty to follow instructions, use of employer's equipment.

If it is an employment relationship, check:

**Applicable KollV (Kollektivvertrag):**
- Identify the applicable Kollektivvertrag based on the employer's Fachgruppe (WKO membership)
- Common KollVs: IT-KV, Handel-KV, Metallindustrie, Gastgewerbe-KV, etc.
- Check if the contractual salary meets or exceeds the KollV minimum for the relevant Verwendungsgruppe and Verwendungsgruppenjahr

**AZG (Arbeitszeitgesetz) — Working time:**
- Normalarbeitszeit max 8h/day, 40h/week (unless KollV says 38.5h)
- Maximum including Ueberstunden: 12h/day, 60h/week (Durchrechnungszeitraum: average 48h/week over 17 weeks)
- Check for Gleitzeitvereinbarung validity (requires BV or individual agreement per §4b AZG)
- Check for All-in clauses: must specify base salary above KollV minimum, Ueberstundenpauschale must be identifiable

**UrlG (Urlaubsgesetz) — Leave:**
- Minimum 5 weeks (30 Werktage) per year
- After 25 Dienstjahre: 6 weeks (36 Werktage)
- Any clause reducing statutory leave is void

**AngG §20 — Kuendigungsfristen:**
- Kuendigung durch Arbeitgeber: 6 weeks (first 2 years), increasing to 5 months (after 25 years), zum Quartalsende (or per KollV: zum 15. or Monatsletzten)
- Kuendigung durch Arbeitnehmer: 1 month zum Monatsletzten (unless longer contractually agreed, but never longer than employer's)
- Check if contractual Kuendigungsfristen meet or exceed statutory minimums

**AngG §36 — Konkurrenzklausel:**
- Only valid if monthly salary at time of termination exceeds 20x daily ASVG Hoechstbeitragsgrundlage (check current value, approx. EUR 3,900/month in 2024)
- Maximum duration: 1 year after end of employment
- Must be reasonable in scope (sachlich, oertlich)
- Cannot apply if employer terminates without wichtiger Grund or if employee terminates for wichtiger Grund

**AngG §2 — Dienstzettel / Arbeitsvertrag:**
- Must contain all elements per §2 Abs 2 AngG (name, start date, Kuendigungsfrist, Einstufung, Gehalt, Arbeitszeit, Urlaub, KollV, etc.)
- New: EU Transparenzrichtlinie requires additional information

**ArbVG §§96-97 — Betriebsvereinbarungspflichtige Massnahmen:**
- Does the contract include provisions that require a Betriebsvereinbarung? (e.g., Leistungskontrolle, Kamerasysteme, Personalinformationssysteme per §96 Abs 1 Z 3)

**GlBG (Gleichbehandlungsgesetz):**
- Any discriminatory clauses based on Geschlecht, ethnische Zugehoerigkeit, Religion, Weltanschauung, Alter, sexuelle Orientierung?
- Equal pay provisions?

**Rechtsfolgen for Arbeitsrecht violations:**
- Unzulaessige Klauseln: Teilnichtigkeit (clause void, contract otherwise valid, statutory provisions apply instead)
- KollV-Unterschreitung: Nachzahlung + Verwaltungsstrafe per LSDB-G
- AZG-Verstoss: Verwaltungsstrafe per §28 AZG (up to EUR 3,626 per employee, repeat offenders up to EUR 7,252)
- GlBG-Verstoss: Schadenersatz + immaterieller Schadenersatz

---

#### Step 5E: UGB Compliance (if B2B)

**Prerequisite:** Both parties are Unternehmer per §1 UGB.

**§377 UGB — Ruegepflicht (Maengelruege):**
- Does the contract address Untersuchungs- and Ruegepflicht for delivered goods?
- If not mentioned: statutory §377 applies — buyer must inspect and notify defects "without undue delay" (unverzueglich) or loses Gewaehrleistung rights
- If modified by contract: is the modification reasonable? Excessively short inspection periods may be sittenwidrig even in B2B

**§347 UGB — Sorgfalt eines ordentlichen Unternehmers:**
- Are liability limitations in the contract reasonable for B2B context?
- Note: B2B allows broader Haftungsausschluss than B2C, but excluding liability for Vorsatz is still void per §879 Abs 1 ABGB
- Excluding Gewaehrleistung entirely is permissible in B2B (unlike B2C)

**Firmenbuchpflichten:**
- Is the Firmenbuchnummer on business documents?
- Are required disclosures per §14 UGB included? (Firma, Rechtsform, Sitz, Firmenbuchnummer, Firmenbuchgericht)

**Rechtsfolgen for UGB violations:**
- §377 Ruege versaeumt: Verlust der Gewaehrleistungsansprueche
- Fehlende Firmenbuchoffenlegung: Zwangsstrafen per §24 FBG

---

#### Step 5F: GewO Compliance (if business operation)

**Prerequisite:** Is a Gewerbeberechtigung required for the described activity?

**Gewerbeberechtigung:**
- Is the activity a freies Gewerbe (only Anmeldung required) or reglementiertes Gewerbe (Befaehigungsnachweis required)?
- Common reglementierte Gewerbe: Baumeister, Elektrotechnik, Gas- und Sanitaertechnik, Versicherungsvermittlung, Immobilientreuhaender, Sicherheitsgewerbe, Gastgewerbe, Reisebuero, etc.
- Is the Gewerbeberechtigung vorhanden and aktuell?

**Standort:**
- Is the Betriebsstandort korrekt gemeldet?
- Standortverlegung requires Ummeldung per §46 GewO

**Gewerberechtlicher Geschaeftsfuehrer:**
- If required (e.g., for juristische Personen): is a gewerbrechtlicher Geschaeftsfuehrer bestellt per §39 GewO?

**Rechtsfolgen for GewO violations:**
- Gewerbeausuebung ohne Berechtigung: Verwaltungsstrafe per §366 GewO (up to EUR 3,600)
- Wiederholte Uebertretung: Entziehung der Gewerbeberechtigung

---

#### Step 5G: ECG Compliance (if website/app)

**§5 ECG — Impressumspflicht (Offenlegungspflicht):**
Check for all mandatory elements:
- Name or Firma
- Geographic address (not just a PO box)
- Email address (including contact form is not sufficient alone per OGH)
- Firmenbuchnummer and Firmenbuchgericht (if registered)
- UID-Nummer (if applicable)
- Zustaendige Aufsichtsbehoerde (if applicable)
- Kammer/Berufsverband and berufsrechtliche Vorschriften (if reglementiertes Gewerbe)
- Leicht und unmittelbar zugaenglich (easily and directly accessible — max 2 clicks from any page)

**§9 ECG — Kommerzielle Kommunikation:**
- Is advertising clearly identifiable as such?
- Is the Auftraggeber erkennbar?

**Rechtsfolgen for ECG violations:**
- §26 ECG: Verwaltungsstrafe up to EUR 3,000
- Wettbewerbsrechtliche Abmahnung per UWG durch Mitbewerber oder Schutzverband

---

#### Step 5H: FAGG Compliance (if e-commerce / Fernabsatz)

**Prerequisite:** Is this a Fernabsatzvertrag per §3 FAGG or ausserhalb von Geschaeftsraeumen geschlossener Vertrag per §3 Z 2 FAGG? Check exclusions in §1 Abs 2 FAGG.

**Vorvertragliche Informationspflichten (§4 FAGG):**
Check for ALL mandatory information per §4 Abs 1:
- Wesentliche Eigenschaften der Ware/Dienstleistung
- Identitaet des Unternehmers (Name, Anschrift, Telefon, E-Mail)
- Gesamtpreis inkl. Steuern und Abgaben
- Zahlungs-, Liefer- und Leistungsbedingungen
- Ruecktrittsrecht: Bestehen, Bedingungen, Frist, Ausuebung (or Ausschlussgruende per §18 FAGG)
- Kosten der Ruecksendung bei Ruecktritt
- Gewaehrleistung und Garantie
- Laufzeit und Kuendigungsbedingungen (bei Dauerschuldverhaeltnissen)
- Funktionalitaet und Interoperabilitaet digitaler Inhalte

**§11 FAGG — Ruecktrittsrecht:**
- 14 Tage Ruecktrittsfrist (Widerrufsfrist)
- Fristbeginn: bei Waren ab Uebernahme, bei Dienstleistungen ab Vertragsschluss
- Bei nicht erfolgter Belehrung: Frist verlaengert sich um 12 Monate (§12 FAGG)
- Muster-Widerrufsformular beigefuegt oder verlinkt?

**§8 FAGG — Bestaetigung:**
- Bestaetigung des Vertrags auf dauerhaftem Datentraeger
- Einschliesslich Bestaetigung der Zustimmung und Kenntnisnahme bei Ausschluss des Ruecktrittsrechts (§18 FAGG Faelle)

**Button-Loesung (§8 Abs 2 FAGG):**
- "Zahlungspflichtig bestellen" oder aehnlich klarer Hinweis auf die Zahlungspflicht

**Rechtsfolgen for FAGG violations:**
- Fehlende Widerrufsbelehrung: Ruecktrittsfrist verlaengert sich auf 12 Monate + 14 Tage
- Fehlende vorvertragliche Information: Verwaltungsstrafe per §19 FAGG
- Verstoss gegen Button-Loesung: Vertrag nicht wirksam geschlossen

---

### Step 6: Calculate Compliance Score

Calculate the compliance score as follows:

**Starting score: 100**

Deductions:
- Each **Verstoss** (violation of mandatory law / zwingend): **-15 points**
- Each **Luecke** (gap — required element missing but no active illegality): **-5 points**  
- Each **missing mandatory element** (e.g., missing Impressum element, missing DSGVO Art 13 element): **-10 points**

**Minimum score: 0**

**Grade assignment:**
| Score | Grade | Meaning |
|-------|-------|---------|
| 90-100 | A | Weitgehend rechtskonform — geringe Risiken |
| 75-89 | B | Ueberwiegend konform — einzelne Luecken zu schliessen |
| 60-74 | C | Erhebliche Maengel — zeitnahe Nachbesserung erforderlich |
| 40-59 | D | Schwerwiegende Verstoesse — dringender Handlungsbedarf |
| 0-39 | F | Massiv rechtswidrig — sofortige Ueberarbeitung notwendig |

List every deduction with its reason to make the score transparent and traceable.

---

### Step 7: Present the Compliance Report

Use the following structure. Match the user's language (German or English).

```markdown
# Compliance-Pruefung: [Document/URL/Description]

**Datum:** [Date]
**Geprueft von:** Claude AI (keine Rechtsberatung)
**Dokumenttyp:** [Contract / AGB / Website / Business Operation / etc.]
**Parteien:** [Party A] (Unternehmer) — [Party B] (Verbraucher/Unternehmer)
**Anwendbare Rechtsordnung:** Oesterreichisches Recht

---

## Compliance-Score: [Score]/100 — Grade [A/B/C/D/F]

[One-sentence summary of overall compliance status]

---

## Anwendbare Frameworks

| # | Framework | Anwendbar? | Begruendung |
|---|-----------|------------|-------------|
| 1 | KSchG | Ja/Nein | [reason] |
| 2 | DSGVO/DSG | Ja/Nein | [reason] |
| 3 | MRG | Ja/Nein | [reason] |
| 4 | Arbeitsrecht | Ja/Nein | [reason] |
| 5 | UGB | Ja/Nein | [reason] |
| 6 | GewO | Ja/Nein | [reason] |
| 7 | ECG | Ja/Nein | [reason] |
| 8 | FAGG | Ja/Nein | [reason] |

---

## Ergebnisse nach Framework

| Framework | Status | Verstoesse | Luecken | Score-Abzug |
|-----------|--------|-----------|---------|-------------|
| KSchG | [status emoji] | [n] | [n] | -[n] |
| DSGVO/DSG | [status emoji] | [n] | [n] | -[n] |
| [etc.] | ... | ... | ... | ... |

Status: Konform = no violations or gaps / Lueckenhaft = gaps but no hard violations / Verstoss = one or more violations of mandatory law

---

## Detailergebnisse

### [Framework 1, e.g., KSchG]

| Pruefpunkt | Norm | Ergebnis | Details |
|------------|------|----------|---------|
| [Check item] | §[x] Abs [y] Z [z] [Gesetz] | Konform/Luecke/Verstoss | [Explanation] |
| ... | ... | ... | ... |

[Repeat table for each applicable framework]

---

## Verstoesse im Detail

### Verstoss 1: [Short title]
- **Norm:** §[x] Abs [y] Z [z] [Gesetz]
- **Betroffene Klausel:** "[Quote the offending clause or describe the missing element]"
- **Problem:** [Detailed explanation of what is wrong and why]
- **Rechtsfolge:** [Legal consequence — e.g., Nichtigkeit der Klausel, Verwaltungsstrafe bis EUR [x], Schadenersatz, DSGVO-Bussgeld bis EUR [x], Verlaengerung der Ruecktrittsfrist]
- **Risikobewertung:** [Hoch/Mittel/Niedrig — how likely is enforcement and how severe are consequences?]
- **Behebung:** [Specific remediation step]
- **Formulierungsvorschlag:** "[Suggested replacement clause or action in correct legal German]"

[Repeat for each Verstoss, ordered by severity]

---

## Luecken (Gaps)

### Luecke 1: [Short title]
- **Norm:** §[x] [Gesetz]
- **Problem:** [What is missing]
- **Empfehlung:** [What to add]
- **Formulierungsvorschlag:** "[Suggested addition]"

[Repeat for each Luecke]

---

## Empfohlene Massnahmen (priorisiert)

### Sofort (innerhalb 1 Woche)
1. [Highest priority action — typically fixing violations of mandatory law]
2. [...]

### Kurzfristig (innerhalb 1 Monat)
3. [Close gaps, add missing elements]
4. [...]

### Mittelfristig (innerhalb 3 Monate)
5. [Structural improvements, process changes]
6. [...]

---

## Score-Berechnung

| # | Abzugsgrund | Norm | Abzug |
|---|-------------|------|-------|
| 1 | [reason] | §[x] [Gesetz] | -[n] |
| 2 | [reason] | §[x] [Gesetz] | -[n] |
| ... | ... | ... | ... |
| | **Ausgangswert** | | **100** |
| | **Gesamtabzug** | | **-[n]** |
| | **Endwert** | | **[score]** |

---

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---

Keine Rechtsberatung. Diese Analyse ersetzt nicht die Beratung durch einen oesterreichischen Rechtsanwalt.
Bei Fragen wenden Sie sich an die zustaendige Rechtsanwaltskammer oder einen spezialisierten Rechtsanwalt.
```

---

## Critical Rules

1. **Always check KSchG for B2C** — this is where the majority of violations occur in Austrian contracts. Do NOT skip it.
2. **Cite specific paragraphs** — every finding must reference the exact §, Absatz, and Ziffer. Never make vague claims like "this might violate consumer protection law."
3. **State the Rechtsfolge** for every violation — the user needs to know what happens if the violation is not fixed (Nichtigkeit, Verwaltungsstrafe, Schadenersatz, DSGVO-Bussgeld, Fristverlaengerung, etc.).
4. **Provide Formulierungsvorschlaege** — do not just say "fix this." Provide a concrete replacement clause or recommended action in proper Austrian legal German.
5. **If RIS MCP is available, verify statute text** — before citing a specific provision, look it up on RIS to confirm it is current (statutes are amended frequently).
6. **Match the user's language** — if the user writes in German, respond in German. If in English, respond in English. Always cite statutes in their official German form regardless.
7. **When in doubt, flag it** — if a clause is borderline, flag it as a Luecke with explanation rather than ignoring it. False negatives are worse than false positives in compliance checking.
8. **Check MRG applicability before applying MRG** — §1 MRG has complex Anwendungsbereich rules. Many tenancy agreements fall under Teilanwendung or Vollausnahme. State which regime applies and why.
9. **Distinguish between zwingendes and dispositives Recht** — violations of mandatory law (zwingendes Recht) are true Verstoesse. Deviations from default rules (dispositives Recht) are permissible but worth noting if disadvantageous.
10. **Do not invent violations** — if a provision is compliant, say so. Credibility depends on accuracy in both directions.

---

## Compliance Frameworks Reference

### KSchG (Konsumentenschutzgesetz) — B2C
- §6 Abs 1: Closed list of void clauses (18 categories)
- §6 Abs 2: Clauses void unless individually negotiated
- §6 Abs 3: Transparency requirement (Transparenzgebot)
- §9: AGB-Kontrolle — unconscionable terms
- §3: Ruecktrittsrecht (Haustuergeschaefte)
- §5a-5j: Fernabsatz / FAGG
- §14: Gerichtsstandsbeschraenkung

### DSGVO / DSG (Data Protection)
- Art 6 DSGVO: Lawful basis for processing
- Art 13/14: Information obligations (Datenschutzerklaerung)
- Art 28: Auftragsverarbeitervertrag (if processors involved)
- Art 30: Verarbeitungsverzeichnis
- Art 35: DSFA (impact assessment if high risk)
- §12 DSG: Bildverarbeitung (image processing)
- §2 Abs 4 DSG: Austrian-specific exemptions

### MRG (Mietrechtsgesetz)
- §§15-16: Mietzinsobergrenzen (Richtwertmietzins / angemessener Mietzins)
- §29: Befristungsregeln (min 3 Jahre)
- §30: Taxative Kuendigungsgruende
- §§3, 8: Erhaltungspflichten
- §27: Verbotene Abloesen

### Arbeitsrecht
- AZG: Arbeitszeitgrenzen (max 12h/Tag, 60h/Woche)
- UrlG: Min 5 Wochen Urlaub
- AngG §20: Kuendigungsfristen
- AngG §36: Konkurrenzklausel (salary threshold, max 1 year)
- ArbVG §§96-97: Betriebsvereinbarungspflicht
- GlBG: Gleichbehandlung, Diskriminierungsverbot

### UGB (Unternehmensrecht)
- §377: Ruegepflicht im B2B-Verkehr
- §347: Sorgfalt eines ordentlichen Unternehmers
- Firmenbuchpflichten

### GewO (Gewerbeordnung)
- Gewerbeberechtigung vorhanden?
- Standortgebundenheit
- Reglementiertes vs freies Gewerbe

### ECG (E-Commerce-Gesetz)
- §5: Impressumspflicht / Offenlegungspflicht
- §9: Kommerzielle Kommunikation

### FAGG (Fern- und Auswaertsgeschaefte-Gesetz)
- §4: Vorvertragliche Informationspflichten
- §11: Ruecktrittsrecht (14 Tage)
- §12: Fristverlaengerung bei fehlender Belehrung
- §8: Bestaetigung auf dauerhaftem Datentraeger
