---
name: recht-missing-momarcode1
title: /recht missing -- Fehlende Klauseln
description: Finds clauses that SHOULD be in a contract under Austrian law but are missing. Checks against type-specific requirements.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-missing
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: contracts
language: en
sources:
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht missing -- Fehlende Klauseln

Identifies missing clauses based on Austrian law requirements for the specific contract type. Goes beyond listing -- explains legal consequences, cites applicable default rules, and drafts replacement language.

---

## Procedure

### Step 1: Read the Document Completely

Read the entire contract or AGB document from start to finish. Do NOT start checking against checklists yet. During this read:

- Note the document title, date, and parties
- Identify the language used (German or English) -- match it in your output
- Get a general sense of scope, structure, and completeness
- Note any explicit references to Austrian statutes (ABGB, KSchG, UGB, MRG, etc.)
- Note any choice-of-law or Gerichtsstand clauses
- Flag if the document is an AGB (Allgemeine Geschaeftsbedingungen) vs. an individual contract (Individualvertrag)

### Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

### Step 3: Clarifying Questions

Before proceeding with analysis, ask the user the following if not already clear from context:

1. **Welche Partei sind Sie?** -- Which party is the user? (Kaeufer/Verkaeufer, Mieter/Vermieter, Arbeitgeber/Arbeitnehmer, Auftraggeber/Auftragnehmer, Gesellschafter?) This determines which missing clauses matter most and from whose perspective the Formulierungsvorschlaege should be drafted.
2. **B2B oder B2C?** -- Is this a contract between two businesses (Unternehmer iSd KSchG), or between a business and a consumer (Verbraucher iSd KSchG)? This is critical because B2C triggers KSchG requirements.
3. **Zweck und Kontext?** -- What is the contract's purpose? Any special circumstances? (e.g., "Wohnungsmiete in Wien Altbau" triggers full MRG; "Bueroflaeche > 500m2" may be MRG-exempt; "IT-Freelancer" suggests Werkvertrag, not Dienstvertrag.)

If the user has already provided this context (e.g., in a prior `/recht review` run), skip the questions and proceed.

### Step 4: Classify the Contract Type

Determine which checklist(s) apply based on the document content and user context.

**4A: Identify the primary contract type:**
- Kaufvertrag (Sale of goods) -- ABGB Kauf, ggf. UGB
- Mietvertrag (Lease/Rental) -- ABGB Bestandvertrag, MRG, WGG
- Dienstvertrag (Employment) -- AngG, AZG, UrlG, AVRAG
- GmbH-Vertrag (Articles of association) -- GmbHG
- Werkvertrag (Service/Work agreement) -- ABGB Werkvertrag
- AGB (General terms and conditions) -- KSchG, ABGB

**4B: Check for hybrid contracts:**
- If the contract combines types (e.g., Kauf + Wartung = Kaufvertrag + Werkvertrag), apply BOTH checklists
- If a Lizenzvertrag includes support services, apply Werkvertrag checklist alongside IP-specific checks
- If a Mietvertrag includes facility management services, add Werkvertrag items

**4C: Layer additional checklists as needed:**
- If the document is AGB (or contains AGB-like standard clauses): ALWAYS add the AGB checklist on top of the base contract type checklist
- If B2C (Verbrauchergeschaeft): ALWAYS add KSchG requirements (especially SS6 KSchG) to every checklist
- If online/Fernabsatz: add FAGG/Fernabsatz requirements
- If data processing is involved: add DSGVO/DSG requirements

### Step 5: Systematic Missing Clause Analysis

This is the core of the skill. Work through the following sub-steps methodically.

#### Step 5A: Run the Applicable Checklist(s)

Go through the relevant checklist(s) item by item. For each item, check whether the contract contains a clause addressing that topic. Mark each item:

- Present and adequate = Vorhanden
- Missing entirely = Fehlt
- Partially covered or vague = Teilweise/unklar

Use the checklists below. If multiple checklists apply, run each one separately, then merge the results.

---

#### Checklist: Kaufvertrag (Sale)

- [ ] Gewaehrleistungsregelung (SS922ff ABGB)
- [ ] Haftungsbegrenzung
- [ ] Eigentumsvorbehalt (S358 ABGB)
- [ ] Gefahrtragung (S1048 ABGB)
- [ ] Ruecktrittsrecht / Wandlung
- [ ] Gerichtsstand / Rechtswahl

#### Checklist: Mietvertrag (Lease)

- [ ] MRG-Anwendbarkeit klargestellt
- [ ] Mietzins + Betriebskosten (SS15-17 MRG)
- [ ] Kaution (max 6 Monatsmieten)
- [ ] Befristung (min 3 Jahre bei MRG, S29 MRG)
- [ ] Erhaltungspflichten (SS3, 8 MRG)
- [ ] Kuendigungsgruende (S30 MRG)
- [ ] Weitergaberecht
- [ ] Investitionsersatz (S10 MRG)

#### Checklist: Dienstvertrag (Employment)

- [ ] Kollektivvertrag-Verweis
- [ ] Einstufung + Gehalt
- [ ] Arbeitszeit (AZG-konform)
- [ ] Urlaubsanspruch (UrlG)
- [ ] Kuendigungsfristen (S20 AngG)
- [ ] Konkurrenzklausel (S36 AngG -- max 1 Jahr, Entgeltgrenze)
- [ ] Diensterfindungen
- [ ] Datenschutzhinweis (DSGVO)
- [ ] Nebenbeschaeftigung

#### Checklist: GmbH-Vertrag (Articles)

- [ ] Stammkapital (min EUR35.000 / S6 GmbHG)
- [ ] Gesellschafteranteile
- [ ] Geschaeftsfuehrerbestellung
- [ ] Gewinnverteilung
- [ ] Abtretung von Geschaeftsanteilen (Notariatsakt S76 GmbHG)
- [ ] Aufgriffsrecht / Vorkaufsrecht
- [ ] Wettbewerbsverbot
- [ ] Tag-along / Drag-along
- [ ] Abfindungsklausel
- [ ] Deadlock-Regelung

#### Checklist: Werkvertrag (Service Agreement)

- [ ] Leistungsbeschreibung
- [ ] Abnahme / Uebergabe
- [ ] Gewaehrleistung (SS922ff ABGB)
- [ ] Haftung + Haftungsobergrenze
- [ ] Zahlungsbedingungen
- [ ] IP / Nutzungsrechte
- [ ] Geheimhaltung
- [ ] Subunternehmer

#### Checklist: AGB (General Terms)

- [ ] KSchG S6 Abs 1 Konformitaet (B2C)
- [ ] S864a ABGB -- keine ungewoehnlichen Klauseln
- [ ] S879 Abs 3 ABGB -- keine groebliche Benachteiligung
- [ ] DSGVO-Hinweis
- [ ] Widerrufsbelehrung (FAGG bei Fernabsatz)
- [ ] Impressum + Kontakt

---

#### Step 5B: Classify Each Missing Clause by Severity

For every item marked as "Fehlt" or "Teilweise/unklar", assign a severity:

- **Kritisch fehlend** -- The clause is legally required (zwingendes Recht), or its absence creates a serious unregulated risk that could cause significant harm to the user's position. Examples: missing Gewaehrleistungsregelung in a Kaufvertrag, missing Befristungsregelung in a MRG-Mietvertrag, missing Stammkapital in a GmbH-Vertrag.

- **Empfohlen** -- The clause is Austrian market standard and strong best practice. Its absence does not violate mandatory law, but it leaves the user exposed to avoidable risk or reliant on unfavorable default rules. Examples: missing Eigentumsvorbehalt for a seller, missing Haftungsobergrenze in a Werkvertrag.

- **Optional** -- Nice to have for completeness or specific situations, but not essential. Its absence does not create meaningful legal risk. Examples: Drag-along clause in a two-person GmbH, Nebenbeschaeftigung clause when already covered by KollV.

#### Step 5C: Detailed Analysis of Each Missing Clause

For EACH missing clause (kritisch and empfohlen; optionally for optional), provide:

1. **Warum noetig**: Cite the specific Austrian statutory provision(s) (SS). Explain what the law requires or what the clause would regulate.

2. **Dispositives Recht / ABGB-Default**: Explain what rule applies BY DEFAULT when this clause is missing. This is critical -- many ABGB rules are dispositiv (can be contracted around), and the default may be unfavorable to the user. For example:
   - Missing Gewaehrleistungsregelung in B2B Kaufvertrag: Default is SS922ff ABGB (2 years, Verbesserung vor Austausch). Cannot be shortened below the mandatory minimum in B2C.
   - Missing Gefahrtragung: Default is S1048 ABGB -- Gefahr goes to buyer upon Uebergabe.
   - Missing Kuendigungsfrist in employment: Default is S20 AngG -- may be more generous than intended.

3. **Risiko ohne diese Klausel**: Concrete, practical consequence. What happens when a dispute arises and this clause is missing? Paint the scenario. E.g., "Ohne Eigentumsvorbehalt verliert der Verkaeufer bei Zahlungsverzug die Moeglichkeit, die Ware zurueckzufordern. Im Insolvenzfall des Kaeufers faellt die Ware in die Insolvenzmasse."

4. **Formulierungsvorschlag**: Draft the actual clause text in German (unless the contract is in English). The draft should:
   - Be written from the perspective of the user's party (as identified in Step 3)
   - Be compliant with mandatory Austrian law
   - Follow Austrian legal drafting conventions
   - Be ready for insertion into the contract (though the user should have a Rechtsanwalt review it)
   - Include the relevant SS references in parentheses

#### Step 5D: Check Austrian-Specific Requirements Beyond the Checklists

After running the standard checklists, check for these additional Austrian-specific requirements that may apply regardless of contract type:

- **DSGVO/DSG**: If the contract involves processing personal data (and almost all do), check for:
  - Datenschutzhinweis or Datenschutzklausel
  - Auftragsverarbeitervertrag (Art 28 DSGVO) if one party processes data on behalf of the other
  - Rechtsgrundlage for data processing identified

- **FAGG / Fernabsatz**: If the contract is concluded online or at a distance (Fernabsatzvertrag):
  - Widerrufsbelehrung (14-Tage Ruecktrittsrecht, S11 FAGG)
  - Muster-Widerrufsformular (Anhang I FAGG)
  - Vorvertragliche Informationspflichten (S4 FAGG)

- **WEG**: If the contract relates to Wohnungseigentum:
  - WEG 2002 compliance
  - Zustimmungserfordernisse
  - Nutzungsregelungen

- **KollV**: For employment contracts:
  - Is the applicable Kollektivvertrag correctly identified?
  - Does the contract meet minimum KollV standards (Mindestgehalt, Sonderzahlungen)?
  - Are there KollV-specific requirements not covered in the checklist (e.g., Reisekostenpauschale, Bildungsfreistellung)?

- **UGB requirements**: For B2B commercial contracts:
  - Unternehmensbezogene Geschaefte (S343 UGB)
  - Ruegepflicht bei Maengeln (S377 UGB) -- critical for Kaufvertraege between Unternehmer
  - Unternehmerischer Verkehr exceptions to KSchG

### Step 6: Gap Severity Assessment

After completing the clause-by-clause analysis, provide an overall assessment:

1. **Count**: How many critical, recommended, and optional clauses are missing?
2. **Usability verdict**: Is the contract usable as-is, or does it need significant additions before signing?
   - **Unterschriftsreif (mit Vorbehalt)**: Few or no critical gaps, some recommended additions. Contract can be signed with awareness of the gaps.
   - **Ueberarbeitung empfohlen**: Multiple recommended clauses missing, 1-2 critical gaps. Contract should be revised before signing.
   - **Erhebliche Luecken**: Multiple critical clauses missing. Contract should NOT be signed without substantial revision.
3. **Priority list**: Rank the missing clauses by urgency -- which should be added first?

### Step 7: Present Findings

Present the complete analysis in the following structured format:

```markdown
# Fehlende Klauseln: [Document Name]

**Vertragstyp:** [primary type, e.g., Werkvertrag] [+ additional types if hybrid]
**Anwendbare Checklisten:** [list which checklists were applied]
**Perspektive:** [which party the user is]
**B2B/B2C:** [classification]
**Geprueft gegen:** Oesterreichisches Recht + Branchenstandard

---

## Checklisten-Ergebnis

### [Checklist Name, e.g., Werkvertrag-Checkliste]

| # | Klausel | Status |
|---|---------|--------|
| 1 | [clause name] | [Vorhanden / Fehlt / Teilweise] |
| 2 | ... | ... |

[Repeat for each applicable checklist]

---

## Kritisch fehlend (rechtlich erforderlich oder hohes Risiko)

### 1. [Missing Clause Name]

**Rechtsgrundlage:** [SS citation]
**ABGB-Default ohne Klausel:** [what applies by default]
**Risiko:** [concrete practical consequence]

**Formulierungsvorschlag:**
> [Draft clause text in German, ready for insertion]

### 2. [Next missing clause...]
[...]

---

## Empfohlen (Best Practice)

### 1. [Missing Clause Name]

**Rechtsgrundlage:** [SS citation]
**ABGB-Default ohne Klausel:** [what applies by default]
**Risiko:** [practical consequence]

**Formulierungsvorschlag:**
> [Draft clause text]

### 2. [Next...]
[...]

---

## Optional (Nice to Have)

| # | Klausel | Warum ueberlegenswert |
|---|---------|----------------------|
| 1 | [clause] | [brief reason] |

---

## Gesamtbewertung

**Kritisch fehlend:** [count]
**Empfohlen:** [count]
**Optional:** [count]

**Bewertung:** [Unterschriftsreif (mit Vorbehalt) / Ueberarbeitung empfohlen / Erhebliche Luecken]

**Prioritaetenliste:**
1. [Most urgent missing clause]
2. [Second most urgent]
3. [...]

---

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---
Keine Rechtsberatung -- Konsultieren Sie einen oesterreichischen Rechtsanwalt.
```

---

## Critical Rules

1. **Always explain the ABGB default rule** when a clause is missing. The user must understand what dispositives Recht fills the gap and whether that default is favorable or unfavorable to them.
2. **Flag mandatory law violations.** If a missing clause means a requirement of zwingendes Recht is unmet (e.g., missing Widerrufsbelehrung in a B2C Fernabsatzvertrag), say so explicitly and mark it as kritisch.
3. **Write Formulierungsvorschlaege** for ALL kritisch and empfohlen missing clauses. These must be substantive draft clause texts, not one-line placeholders.
4. **Don't just list what's missing -- explain the practical consequence.** Paint the dispute scenario. What happens if things go wrong and this clause is absent?
5. **Match the user's language.** If the contract and conversation are in German, write everything in German. If in English, write in English. Always cite statutes in their official German form regardless.
6. **Cite specific sections.** Never say "gemaess ABGB" without a section number. Always cite SS[number] [Gesetz].
7. **Consider the user's party perspective.** A missing Eigentumsvorbehalt is kritisch for a seller but irrelevant for a buyer. A missing Haftungsobergrenze is kritisch for the service provider but favorable for the client.
