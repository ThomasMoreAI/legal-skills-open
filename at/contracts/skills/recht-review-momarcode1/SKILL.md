---
name: recht-review-momarcode1
title: /recht review — Vertragsprüfung (Full Review)
description: Full contract and legal document review for Austrian law with 5 parallel agents. Returns a Vertragssicherheits-Score, clause-by-clause analysis, risk flagging, KSchG/DSGVO compliance, and prioritized recommendations.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-review
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

# /recht review — Vertragsprüfung (Full Review)

When the user triggers this skill, follow these steps exactly.

---

## Step 1: Read the Document

Read the entire uploaded document. If it's a PDF, extract all text. If it's a DOCX, parse it.
If no document is uploaded, ask the user to provide one.

Do NOT begin analysis until you have read the full document.

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

Before analysis, you MUST know these three things. Check the document first — often you can infer them. Only ask if truly unclear:

1. **Which party is the user?** Look at the document context. If unclear, ask:
   > "Welche Vertragspartei sind Sie? (z.B. Käufer/Verkäufer, Mieter/Vermieter, Arbeitnehmer/Arbeitgeber)"

2. **Is this B2B or B2C?** This determines if KSchG applies. Check if one party is clearly a consumer (natürliche Person, kein Unternehmer). If unclear, ask.

3. **What is the approximate contract value (Streitwert)?** Often stated in the contract. If not, ask.

---

## Step 4: Classify the Document

Determine the contract type. This controls which legal framework applies:

- **Kaufvertrag** → §§1053ff ABGB, check Gewährleistung §§922ff
- **Werkvertrag** → §§1151ff ABGB (Werk), check Abnahme, Gewährleistung
- **Mietvertrag** → Check if MRG applies (§1 MRG). If yes: MRG controls. If no: ABGB §§1090ff
- **Dienstvertrag / Arbeitsvertrag** → AngG, ArbVG, applicable KollV, AZG, UrlG
- **GmbH-Vertrag / Gesellschaftervereinbarung** → GmbHG, §§3-5 (notwendiger Inhalt)
- **NDA / Geheimhaltungsvereinbarung** → ABGB allgemein, UWG §11
- **Lizenzvertrag** → UrhG or PatG + ABGB
- **AGB** → §864a ABGB, §879 Abs 3, KSchG §§6,9
- **Freier Dienstvertrag** → Check if disguised Arbeitsvertrag (§539a ASVG)

---

## Step 5: Run the 5-Agent Analysis

Go through the entire document systematically for each of these.

### 5A: Clause Identification

Go clause by clause. For EACH clause:
1. **Name it** — What does this clause regulate?
2. **Locate it** — Which section/paragraph?
3. **Summarize it** — One sentence.
4. **Map to Austrian law** — Which §§ govern this? Be specific.
5. **Extract key terms** — Amounts, dates, caps, conditions.

Focus especially on: Haftung, Gewährleistung, Kündigung, Gerichtsstand, Vertragsstrafe, Konkurrenzklausel, Geheimhaltung, IP/Nutzungsrechte, Datenschutz, Schiedsklausel.

### 5B: Risk Scoring

For EACH clause from 4A, assign a risk level:

**🔴 Kritisch** — assign if ANY of these is true:
- Violates mandatory Austrian law (zwingendes Recht) → void or voidable
- Creates unlimited or uncapped liability for user
- Allows other party to unilaterally change essential terms
- Waives rights that cannot be waived in B2C

**🟡 Wichtig** — assign if ANY of these is true:
- Deviates significantly from Austrian market standard
- Is one-sided but not void
- Creates meaningful financial risk
- Has unusually short/long Frist

**🟢 Standard** — if clause matches normal Austrian practice.

For each 🔴 and 🟡, estimate **financial exposure in €**.

### 5C: Compliance Check

Run these checks based on contract type:

**Always check:**
- [ ] §864a ABGB — Unusual clauses hidden in AGB?
- [ ] §879 Abs 1 ABGB — Anything sittenwidrig?
- [ ] §879 Abs 3 ABGB — Gröbliche Benachteiligung in AGB?
- [ ] DSGVO Art 28 — Personal data processed without Auftragsverarbeitervertrag?

**If B2C (KSchG applies), check EACH clause against:**
- [ ] §6 Abs 1 Z 1 — Einseitige Leistungsbestimmung → nichtig
- [ ] §6 Abs 1 Z 2 — Unangemessen lange Bindungsfrist → nichtig
- [ ] §6 Abs 1 Z 5 — Einseitige Preisänderung → nichtig
- [ ] §6 Abs 1 Z 9 — Haftungsausschluss Vorsatz/grobe Fahrlässigkeit → nichtig
- [ ] §6 Abs 1 Z 11 — Beweislastumkehr → nichtig
- [ ] §6 Abs 2 Z 3 — Einseitige Änderung Vertragsgegenstand → nichtig wenn nicht individuell
- [ ] §6 Abs 3 — Transparenzgebot verletzt?
- [ ] §14 — Gerichtsstand außerhalb Verbraucher-Wohnsitz?
- [ ] §617 ZPO — Schiedsklausel in Verbrauchervertrag → nichtig
- [ ] §3 KSchG / FAGG — Fehlendes Rücktrittsrecht bei Haustür-/Fernabsatz?

**If Mietvertrag (MRG):**
- [ ] §§15-16 MRG — Mietzins zulässig?
- [ ] §29 MRG — Befristung min 3 Jahre?
- [ ] §30 MRG — Nur taxative Kündigungsgründe?
- [ ] §27 MRG — Verbotene Ablösen?

**If Arbeitsvertrag:**
- [ ] KollV korrekt referenziert und eingestuft?
- [ ] AZG Grenzen eingehalten?
- [ ] §20 AngG Kündigungsfristen korrekt?
- [ ] §36 AngG Konkurrenzklausel: max 1 Jahr, Entgeltgrenze?
- [ ] All-in-Klausel transparent, Grundlohn ausgewiesen?

### 5D: Obligations Mapping

Extract ALL obligations, deadlines, triggers. For each:
1. **Who** must do it?
2. **What** must they do?
3. **When** (Frist)?
4. **Consequence** of missing it?

Flag: automatic renewals, notice periods, Vertragsstrafe triggers, payment terms.

### 5E: Recommendations

For EACH 🔴 and 🟡 finding:
1. State the problem in one sentence
2. Cite the Austrian law (§§)
3. Write a **Formulierungsvorschlag** — actual replacement clause text in Austrian legal German
4. Rate **Verhandelbarkeit**: Hoch / Mittel / Gering
5. Provide a **Fallback** if primary proposal is rejected

Then list MISSING clauses (use checklists from `skills/recht-missing/SKILL.md`).

---

## Step 6: Calculate the Vertragssicherheits-Score

Score = 100 minus penalty points:

| Finding | Penalty |
|---------|---------|
| Each 🔴 Kritisch | -12 |
| Each 🟡 Wichtig | -5 |
| Each missing critical clause | -8 |
| Each missing recommended clause | -3 |
| Each KSchG violation | -10 |

Minimum score is 0. Grade: A (90-100), B (75-89), C (60-74), D (40-59), F (0-39).

---

## Step 7: Present the Report

Use this structure:

```markdown
# Vertragsprüfung: [Document Name]

**Vertragstyp:** [type]
**Ihre Position:** [user's party]
**Gegenpartei:** [counterparty]
**Vertragssicherheits-Score:** [score]/100 ([grade])
**Anwendbares Recht:** Österreichisches Recht

## ⚠️ Sofort-Warnungen
[Blank fields, missing signatures, void clauses]

## Risiko-Dashboard
| Stufe | Anzahl |
|-------|--------|
| 🔴 Kritisch | [n] |
| 🟡 Wichtig | [n] |
| 🟢 Standard | [n] |

## Zusammenfassung
[2-3 sentences: contract type, overall risk, #1 issue]

## Wesentliche Vertragspunkte
| Punkt | Inhalt | Fundstelle |
|-------|--------|-----------|

## Risikoanalyse

### 🔴 Kritisch
**[Clause name]** (§[x] des Vertrags)
- **Problem:** [one sentence]
- **Rechtslage:** [§§ with law name]
- **Formulierungsvorschlag:** "[replacement text]"
- **Verhandelbarkeit:** Hoch / Mittel / Gering

### 🟡 Wichtig
[Same structure]

## Fehlende Klauseln
| Klausel | Warum nötig | Risiko ohne |
|---------|-------------|-------------|

## KSchG-Prüfung (if B2C)
| Klausel | Prüfung | Ergebnis |
|---------|---------|----------|

## Pflichten-Zeitleiste
| Frist | Wer | Was | Konsequenz |
|-------|-----|-----|-----------|

## Verhandlungsprioritäten
1. [Most important — with Formulierungsvorschlag]
2. [Second]
3. [Third]

## Nächste Schritte
- [ ] [Actionable items]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---
⚠️ **Keine Rechtsberatung.** Ersetzt nicht die Beratung durch einen Rechtsanwalt.
```

---

## Critical Rules

1. **Always cite specific §§** — Never "Austrian law says..." without the exact section.
2. **Always write Formulierungsvorschläge** — Don't just say "change this", write the replacement.
3. **Never skip KSchG check** for B2C — this is where the biggest findings are.
4. **Void clauses go in Sofort-Warnungen** — nichtig per KSchG or §879 ABGB = top of report.
5. **Use RIS if connected** — Verify statute citations are current.
6. **Match user's language** — German in → German out. English in → English out. Statutes always in German form (§922 ABGB).
