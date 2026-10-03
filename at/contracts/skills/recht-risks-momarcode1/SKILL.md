---
name: recht-risks-momarcode1
title: /recht risks -- Risikoanalyse (Deep Risk Analysis)
description: Deep risk analysis for contracts and legal situations under Austrian law. Severity scoring per clause, financial exposure estimation, Austrian market standard comparison.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-risks
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

# /recht risks -- Risikoanalyse (Deep Risk Analysis)

When the user triggers this skill, follow these steps exactly.

---

## Step 1: Read the Document

Read the entire uploaded document. If it's a PDF, extract all text. If it's a DOCX, parse it.
If no document is uploaded, ask the user to provide one.

Do NOT begin analysis until you have read the full document, including any annexes, appendices, or referenced AGB.

Note: This skill differs from `/recht review` in focus. While review gives a balanced clause-by-clause overview, `/recht risks` goes deep on **risk quantification and financial exposure**. Every clause is examined through the lens of "what can go wrong, how badly, and how likely."

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 3: Ask Clarifying Questions (only if needed)

Before analysis, you MUST know these things. Check the document first -- often you can infer them. Only ask if truly unclear:

1. **Which party is the user?** Look at the document context. If unclear, ask:
   > "Welche Vertragspartei sind Sie? (z.B. Kaeufer/Verkaeufer, Mieter/Vermieter, Auftraggeber/Auftragnehmer)"

2. **Is this B2B or B2C?** This determines if KSchG applies. Check if one party is clearly a consumer (natuerliche Person, kein Unternehmer iSd §1 KSchG). If unclear, ask.

3. **What is the approximate contract value (Streitwert/Auftragswert)?** Often stated in the contract. If not, ask:
   > "Wie hoch ist der ungefaehre Vertragswert? (Fuer die Berechnung der finanziellen Exposition)"

4. **Contract duration?** Needed for recurring obligations. Check the contract. If not stated, ask.

5. **Any known disputes or concerns?** If the user mentions specific worries, note them for priority analysis.

---

## Step 4: Classify Document and Identify Applicable Mandatory Law

### 4A: Determine the Contract Type

Classify the contract. This controls which mandatory law regime applies:

- **Kaufvertrag** -- ABGB Drittes Hauptstueck, Gewährleistung §§922-933b ABGB
- **Werkvertrag** -- §§1151, 1165-1171 ABGB, Gewährleistung, Prüf-/Rügepflicht (UGB §377 if B2B)
- **Mietvertrag** -- MRG (if applicable per §1 MRG) or ABGB §§1090ff
- **Arbeitsvertrag** -- AngG, AVRAG, AZG, UrlG, applicable Kollektivvertrag, ArbVG
- **Dienstvertrag (frei)** -- ABGB §§1151ff, check Scheinselbststaendigkeit (§539a ASVG)
- **GmbH-Vertrag** -- GmbHG, insb. §§3-5 (notwendiger Inhalt), §39 (Beschlussfassung)
- **Lizenzvertrag** -- UrhG oder PatG + ABGB allgemeine Vertragsregeln
- **AGB / Nutzungsbedingungen** -- §864a ABGB, §879 Abs 3 ABGB, KSchG §§6, 9
- **Bauvertrag** -- ABGB Werkvertrag + OENORM B 2110/2118 (if referenced)
- **Franchisevertrag** -- kein eigenes Gesetz, ABGB + UWG + KartG

### 4B: Map the Mandatory Law Framework

List ALL mandatory law (zwingendes Recht) that applies to this contract type. This becomes the checklist for Step 5D.

**Always applicable:**
- §879 Abs 1 ABGB -- Sittenwidrigkeit
- §879 Abs 3 ABGB -- groebliche Benachteiligung in AGB
- §864a ABGB -- ungewoehnliche AGB-Klauseln
- §6 ABGB -- Auslegung gegen den Verwender (AGB)
- DSGVO + DSG -- if personal data is processed

**B2C additional (KSchG):**
- §6 Abs 1 KSchG -- nichtige Klauseln (Z 1-15, geschlossener Katalog)
- §6 Abs 2 KSchG -- nichtige Klauseln in AGB (Z 1-7)
- §6 Abs 3 KSchG -- Transparenzgebot
- §9 KSchG -- Gewährleistungsbeschraenkungen nichtig
- §14 KSchG -- Gerichtsstand
- §3 KSchG / FAGG -- Ruecktrittsrecht bei Fernabsatz/Haustuere

**Contract-type-specific** -- list the applicable sections from Step 4A.

---

## Step 5: Systematic Clause-by-Clause Risk Analysis

Go through the ENTIRE document. Do not skip standard-looking clauses -- even seemingly harmless formulations can create risk under Austrian law.

### 5A: Identify ALL Clauses That Create Obligations, Liability, or Risk

For EACH clause or provision in the document:

1. **Identify it** -- Section number, heading, page
2. **Classify its function:**
   - Leistungspflicht (obligation to perform)
   - Haftung / Gewährleistung (liability / warranty)
   - Schadenersatz (damages)
   - Vertragsstrafe (penalty clause)
   - Kuendigung / Ruecktritt (termination / withdrawal)
   - Fristen / Termine (deadlines)
   - Geheimhaltung / NDA
   - Wettbewerbsverbot (non-compete)
   - Gerichtsstand / Schiedsklausel (jurisdiction / arbitration)
   - Abtretung / Uebertragung (assignment)
   - Aenderungsklausel (modification rights)
   - Automatische Verlaengerung (auto-renewal)
   - Force Majeure / Hoehere Gewalt
   - Salvatorische Klausel
   - IP / Nutzungsrechte
   - Datenschutz
3. **Extract risk-relevant terms:** amounts, caps, time limits, conditions precedent, triggers
4. **Note asymmetries:** Does this clause bind both parties equally, or is it one-sided?

### 5B: 3-Tier Risk Scoring Per Clause

For EACH clause identified in 5A, apply this scoring:

#### 🔴 Kritisch -- assign if ANY of these is true:

| Criterion | Example |
|-----------|---------|
| Violates mandatory law (zwingendes Recht) | Clause excludes liability for Vorsatz/grobe Fahrlaessigkeit (§6 Abs 1 Z 9 KSchG in B2C; §879 ABGB in B2B) |
| Clause is void (nichtig) or voidable (anfechtbar) | Hidden AGB clause per §864a ABGB, sittenwidrig per §879 ABGB |
| Creates unlimited or uncapped liability for user | "unbeschraenkte Haftung fuer alle Schaeden" without any cap |
| Allows counterparty to unilaterally change essential terms | Price, scope, or duration changeable at sole discretion |
| Waives rights that cannot legally be waived | Gewährleistung in B2C (§9 KSchG), Ruecktrittsrecht (§3 KSchG) |
| Creates existential financial risk | Liability exceeds contract value by 10x+ or is uncapped |
| Contains verbotene Ablöse (§27 MRG) or exceeds Richtwertmietzins | In Mietrecht only |
| Konkurrenzklausel exceeds §36 AngG limits | Longer than 1 year, or below Entgeltgrenze |

#### 🟡 Wichtig -- assign if ANY of these is true:

| Criterion | Example |
|-----------|---------|
| Deviates significantly from Austrian market standard | Zahlungsziel 7 Tage (standard: 30 Tage), Gewährleistung 6 Monate (standard: 24) |
| One-sided but not void | Asymmetric Kuendigungsfristen, only one party has Ruecktrittsrecht |
| Creates significant financial risk (quantifiable) | Vertragsstrafe of 20% contract value (market: 5-10%) |
| Unusually short or long Fristen | 3-day Ruegefrist (standard: 14 days), 5-year Bindungsfrist |
| Missing limitation of liability (Haftungsobergrenze) | B2B contract without any liability cap |
| Problematic Gerichtsstand | Far from user's location (though valid in B2B) |
| Unclear or ambiguous formulation creating interpretation risk | Scope definitions, "nach billigem Ermessen" without criteria |
| Automatic renewal without adequate notice period | Auto-renewal with 3-month Kuendigungsfrist (short window) |

#### 🟢 Standard -- assign if:

| Criterion | Example |
|-----------|---------|
| Clause matches normal Austrian legal practice | Standard Gewährleistung per ABGB, standard Kuendigungsfristen |
| Balanced between parties | Mutual obligations, symmetric termination rights |
| Within typical market ranges | Payment terms 14-30 days, standard Gerichtsstand |
| Contains standard salvatorische Klausel, Schriftformklausel | Boilerplate that is balanced |

### 5C: Financial Exposure Estimation Per Clause

For EACH clause scored 🔴 or 🟡, estimate financial exposure in three scenarios:

**Best Case (Guenstigster Fall):**
- Clause is struck by court as nichtig, reformed to dispositives Recht
- User successfully challenges the clause (Verbandsklage, Individualklage)
- Exposure: typically EUR 0 + own legal costs

**Expected Case (Wahrscheinlicher Fall):**
- Realistic outcome if this clause is invoked in a dispute
- Consider Austrian court practice (OGH Rechtsprechung) on similar clauses
- Consider likelihood of the risk actually materializing (0-100%)
- Calculate: exposure amount x probability = expected value

**Worst Case (Schlimmster Fall):**
- Counterparty enforces clause to maximum extent
- Court upholds the clause as valid
- Full financial impact on user
- Include consequential damages if clause allows (Folgeschaeden)

Express exposure as: **EUR [amount] (Best) / EUR [amount] (Expected) / EUR [amount] (Worst)**

When calculating, consider:
- Contract value as baseline
- Duration-based multipliers for recurring obligations
- Vertragsstrafe amounts (check against §1336 Abs 2 ABGB -- richterliches Maessigungsrecht)
- Liability caps or lack thereof
- Opportunity costs (Konkurrenzklausel: lost income during restriction period)
- Legal costs if enforcement leads to litigation (GGG + RATG based on Streitwert)

### 5D: Mandatory Law Violation Check

For EACH clause, run through the applicable mandatory law framework from Step 4B.

**§879 ABGB Check (always):**
- Abs 1: Is the clause contra bonos mores? Would it shock the conscience of a reasonable person?
- Abs 3: If this is an AGB clause -- does it groeblich benachteiligen the other party without sachliche Rechtfertigung? Apply the OGH test: compare clause effect against dispositives Recht, assess deviation severity.

**§864a ABGB Check (if AGB):**
- Is this clause unusual (ungewoehnlich) in the context of this contract type?
- Is it hidden in a way that the other party would not expect it?
- OGH standard: Would the clause surprise a reasonable person familiar with this contract type?

**§6 KSchG Check (if B2C) -- check EACH applicable Ziffer:**
- Z 1: Einseitige Leistungsbestimmung -- can counterparty define or change the service unilaterally?
- Z 2: Unangemessen lange Bindung -- is the contract duration unreasonably long?
- Z 3: Kuendigungsverzicht -- does the consumer waive termination rights?
- Z 5: Einseitige Preisaenderung -- can counterparty raise price without objective criteria?
- Z 9: Haftungsausschluss -- does it exclude liability for Vorsatz or grobe Fahrlaessigkeit?
- Z 11: Beweislastumkehr -- does it shift burden of proof to consumer's disadvantage?
- Z 14: Aufrechnungsverbot -- does it prohibit set-off of undisputed claims?
- Z 15: Klagsverbot -- does it limit the consumer's right to sue?

**§9 KSchG Check (if B2C):**
- Any limitation of Gewährleistung (shortening Frist, excluding Verbesserung/Austausch) = nichtig

**§1336 ABGB Check (Vertragsstrafe):**
- Is the penalty grossly excessive relative to the interest of the creditor?
- OGH regularly reduces penalties exceeding 5-10% of contract value in B2B

**§36 AngG Check (if Arbeitsvertrag):**
- Konkurrenzklausel: Max 1 year, only if monthly Entgelt exceeds threshold (2024: EUR 3.895,50 brutto)
- Konventionalstrafe must be maessigungsfaehig

**MRG Checks (if Mietvertrag in MRG-Vollwanwendungsbereich):**
- §16 MRG: Mietzins within Richtwert or Kategoriemietzins?
- §27 MRG: Any verbotene Ablöse or Provision?
- §29 MRG: Befristung minimum 3 years?
- §30 MRG: Only taxative Kuendigungsgruende?

**UGB §348 Check (if B2B with AGB):**
- Do the AGB comply with Unternehmer-AGB rules?
- §377 UGB: Is the Ruegefrist for Maengel reasonable?

For each violation found, note:
- **Rechtsfolge:** nichtig / anfechtbar / teilnichtig / richterliche Mässigung
- **Rechtsgrundlage:** exact §§
- **Practical consequence:** What happens if the clause is struck? What dispositives Recht fills the gap?

### 5E: Austrian Market Standard Comparison

For EACH clause scored 🔴 or 🟡, compare against what is standard in Austria for this contract type.

**Use these Austrian market benchmarks:**

| Clause Type | Austrian Standard | Unusual / Risky |
|-------------|-------------------|-----------------|
| Zahlungsziel | 14-30 Tage | <7 oder >90 Tage |
| Gewaehrleistung (B2B Kauf) | 24 Monate ab Uebergabe | <12 Monate, Ausschluss Wandlung |
| Gewaehrleistung (B2C) | 24 Monate, nicht einschraenkbar | Jede Einschraenkung = nichtig |
| Gewaehrleistung (B2B Werk) | 3 Jahre (§1167 ABGB analog) | <12 Monate |
| Kuendigungsfrist (B2B Dauerschuld) | 1-3 Monate | >6 Monate |
| Kuendigungsfrist (Arbeitsvertrag AG) | per §20 AngG (6 Wochen bis 5 Monate) | Kuerzere Fristen als gesetzlich |
| Vertragsstrafe (B2B) | 5-10% Auftragswert, gedeckelt | >15% oder ungedeckelt |
| Haftungsobergrenze (B2B) | 1-2x Auftragswert | Keine Obergrenze / >5x |
| Haftungsausschluss | Leichte Fahrlaessigkeit, Folgeschaeden | Grobe Fahrlaessigkeit ausgeschlossen |
| Konkurrenzklausel | 6-12 Monate, sachlich + raeumlich begrenzt | >12 Monate, unbeschraenkt |
| Schiedsklausel (B2B) | VIAC Wien, selten unter EUR 50.000 | Bei kleinen Streitwerten, in B2C |
| Gerichtsstand (B2B) | Sitz des Beklagten oder Erfuellungsort | Weit entfernt ohne sachliche Anknuepfung |
| Geheimhaltung (NDA) | 2-5 Jahre, mit Ausnahmen | Unbefristet, ohne Ausnahmen |
| Automatische Verlaengerung | 12 Monate, mit 3-Monats-Kuendigungsfrist | >24 Monate, kurze Kuendigungsfenster |

For each deviation, state:
- **Was ist ueblich:** Austrian market standard
- **Was steht im Vertrag:** Actual clause content
- **Abweichung:** How far does it deviate and in whose favor

---

## Step 6: Calculate Overall Risk Score

### 6A: Aggregate Risk Count

Count findings per tier:
- Total 🔴 Kritisch findings
- Total 🟡 Wichtig findings
- Total 🟢 Standard findings

### 6B: Aggregate Financial Exposure

Sum the financial exposure across all 🔴 and 🟡 clauses:

| | Best Case | Expected Case | Worst Case |
|---|-----------|---------------|------------|
| 🔴 Kritisch Total | EUR [sum] | EUR [sum] | EUR [sum] |
| 🟡 Wichtig Total | EUR [sum] | EUR [sum] | EUR [sum] |
| **Gesamt** | **EUR [sum]** | **EUR [sum]** | **EUR [sum]** |

### 6C: Risk Ratio

Calculate:
- **Risiko-Vertragswert-Verhaeltnis** = Worst Case Exposition / Vertragswert
  - < 1.0x = proportional risk
  - 1.0-3.0x = elevated risk
  - > 3.0x = disproportionate risk -- **flag as overall Kritisch**

### 6D: Overall Risk Rating

Based on the aggregate findings, assign an overall rating:

| Rating | Criteria |
|--------|----------|
| **HOHES RISIKO** | Any 🔴 finding, or total expected exposure > 50% of contract value, or mandatory law violation |
| **MITTLERES RISIKO** | No 🔴 but multiple 🟡 findings, or total expected exposure 10-50% of contract value |
| **NIEDRIGES RISIKO** | Only 🟢 and minor 🟡, total expected exposure < 10% of contract value |

---

## Step 7: Present the Report

Use this structure exactly:

```markdown
# Risikoanalyse: [Document Name]

**Vertragstyp:** [type]
**Ihre Position:** [user's party]
**Gegenpartei:** [counterparty]
**B2B / B2C:** [B2B or B2C -- KSchG applicable: ja/nein]
**Vertragswert:** EUR [amount]
**Vertragsdauer:** [duration]
**Anwendbares Recht:** Oesterreichisches Recht
**Gesamtrisiko-Rating:** [HOHES RISIKO / MITTLERES RISIKO / NIEDRIGES RISIKO]

---

## Risiko-Uebersicht

| Stufe | Anzahl | Geschaetzte Exposition (Worst Case) |
|-------|--------|-------------------------------------|
| 🔴 Kritisch | [n] | EUR [amount] |
| 🟡 Wichtig | [n] | EUR [amount] |
| 🟢 Standard | [n] | -- |
| **Gesamt** | **[n]** | **EUR [amount]** |

**Risiko-Vertragswert-Verhaeltnis:** [x.x]x

## Finanzielle Gesamtexposition

| Szenario | Exposition | Erlaeuterung |
|----------|------------|-------------|
| Guenstigster Fall | EUR [amount] | [brief explanation] |
| Wahrscheinlicher Fall | EUR [amount] | [brief explanation] |
| Schlimmster Fall | EUR [amount] | [brief explanation] |

---

## Sofort-Warnungen (Zwingendes Recht)

[List any clauses that violate mandatory law. These are void/voidable and must be addressed before signing.]

| # | Klausel | Rechtsgrundlage | Rechtsfolge |
|---|---------|-----------------|-------------|
| 1 | [clause] | [§§] | nichtig / anfechtbar |

---

## Detailanalyse

### 🔴 R1: [Risk Name]
**Fundstelle:** §[x] / Punkt [x] des Vertrags
**Klauseltext:** "[relevant text from clause]"
**Risikokategorie:** [Haftung / Vertragsstrafe / Kuendigung / etc.]
**Problem:** [What is wrong and why it matters -- one to two sentences]
**Oesterreichische Rechtslage:**
- Zwingendes Recht: [§§ and what they require]
- Dispositives Recht (ohne Klausel): [what would apply if clause were struck]
- OGH-Rechtsprechung: [relevant Geschaeftszahl if known, e.g. "OGH 4 Ob 221/18k"]
**Marktvergleich:** [Austrian standard vs. this clause]
**Finanzielle Exposition:**
- Guenstigster Fall: EUR [amount] -- [reason]
- Wahrscheinlicher Fall: EUR [amount] -- [reason]
- Schlimmster Fall: EUR [amount] -- [reason]
**Eintrittswahrscheinlichkeit:** [Hoch / Mittel / Gering] -- [brief rationale]
**Empfehlung:** [specific action]
**Formulierungsvorschlag:** "[replacement clause text in Austrian legal German]"

[Repeat for each 🔴 risk, numbered R1, R2, R3...]

---

### 🟡 R[n]: [Risk Name]
[Same structure as above]

[Repeat for each 🟡 risk]

---

### 🟢 Standard-Klauseln
[Brief list confirming which clauses are standard and unproblematic. No detailed analysis needed.]

| Klausel | Beurteilung |
|---------|-------------|
| [clause] | Marktkonform, kein Handlungsbedarf |

---

## Fehlende Risikobegrenzungen

[Clauses that SHOULD be in the contract but are missing, creating risk by omission.]

| Fehlende Klausel | Risiko ohne | Empfohlener Inhalt |
|------------------|-------------|-------------------|
| Haftungsobergrenze | Unbeschraenkte Haftung | "Die Haftung ist mit [x]x des Auftragswerts begrenzt." |
| [etc.] | [risk] | [suggested text] |

---

## Verhandlungsprioritaeten

Ranked by financial exposure and likelihood:

1. **[Hoechste Prioritaet]:** [clause] -- EUR [worst case] Exposition
   - **Verhandelbarkeit:** Hoch / Mittel / Gering
   - **Formulierungsvorschlag:** "[text]"
   - **Fallback-Position:** "[alternative if primary is rejected]"

2. **[Zweite Prioritaet]:** [clause] -- EUR [worst case] Exposition
   [same structure]

3. **[Dritte Prioritaet]:** [clause]
   [same structure]

---

## Naechste Schritte

- [ ] [Actionable items in priority order]
- [ ] [e.g. "Haftungsobergrenze verhandeln (Prioritaet 1)"]
- [ ] [e.g. "Klausel §X streichen lassen -- nichtig per §6 Abs 1 Z 9 KSchG"]
- [ ] [e.g. "Rechtsanwalt fuer Verhandlung beiziehen"]

---

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---
⚠️ **Keine Rechtsberatung.** Diese Analyse ersetzt nicht die Beratung durch einen zugelassenen oesterreichischen Rechtsanwalt. Alle Betraege sind Schaetzungen auf Basis der Vertragsinformationen.
```

---

## Critical Rules

1. **Every risk needs a EUR amount.** Do not flag a risk without quantifying it. If exact amounts are not determinable, estimate ranges and state your assumptions. "Financial exposure unclear" is not acceptable -- estimate based on contract value, duration, and market data.

2. **Always cite specific §§.** Never write "Austrian law prohibits this" without the exact section. Correct: "nichtig per §6 Abs 1 Z 9 KSchG." Wrong: "this violates consumer protection law."

3. **Always provide Formulierungsvorschlaege.** For every 🔴 and 🟡 finding, write actual replacement clause text in Austrian legal German. The user should be able to copy-paste into a redline.

4. **Distinguish nichtig from merely nachteilig.** A clause violating zwingendes Recht (nichtig/anfechtbar) is fundamentally different from a clause that is simply unfavorable. The report must make this clear -- nichtigkeit goes in Sofort-Warnungen, unfavorable terms go in Detailanalyse.

5. **Never skip the B2C check.** If KSchG applies, check EVERY clause against §6 KSchG systematically. This is where the most critical findings come from in Austrian consumer contracts.

6. **Apply §879 Abs 3 ABGB rigorously in B2B.** Even without KSchG, AGB in B2B contracts are subject to the groebliche Benachteiligung test. Compare each AGB clause against dispositives Recht and assess deviation severity per OGH methodology.

7. **Account for richterliches Maessigungsrecht.** When scoring Vertragsstrafen, note that Austrian courts regularly reduce excessive penalties per §1336 Abs 2 ABGB. The "expected case" should reflect likely judicial reduction, not the contractual amount.

8. **Check for Scheinvertraege.** If a freier Dienstvertrag looks like an Arbeitsvertrag (fixed hours, personal dependency, integration into organization), flag the Scheinselbststaendigkeit risk per §539a ASVG. This changes the entire legal framework.

9. **Use RIS if connected.** Verify statute citations are current. Look up relevant OGH decisions for disputed clause types. Cite Geschaeftszahlen where possible.

10. **Match user's language.** German input = German output. English input = English output. Statute citations always in German form (§922 ABGB, §6 Abs 1 Z 9 KSchG).

11. **Three-scenario exposure is mandatory.** Never give a single EUR number. Always give Best/Expected/Worst, with brief reasoning for each. The expected case is the most important -- it should reflect realistic Austrian court outcomes.

12. **Flag missing clauses as risks.** The absence of a Haftungsobergrenze, Kuendigungsrecht, or Gerichtsstandsvereinbarung is itself a risk. Include missing protections in the analysis with their own exposure estimates.
