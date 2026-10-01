---
name: recht-compare-momarcode1
title: /recht compare -- Vertragsvergleich
description: Side-by-side comparison of two contract versions under Austrian law. Flags additions, removals, and dangerous changes.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-compare
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: contracts
language: de
---

# /recht compare -- Vertragsvergleich

Compares two contract versions and identifies every legally significant change. Assesses each change under Austrian law (ABGB, KSchG, UGB, UWG, MRG, DSGVO, etc.), classifies risk, analyzes cumulative effects, and provides actionable recommendations with Formulierungsvorschlaege.

---

## Step 1: Read Both Documents Completely

1. Read **both** contract versions in full before beginning any comparison.
2. For each document, note:
   - Title, date, version identifier (if present)
   - Total number of sections/clauses/Paragraphen
   - Governing law clause and Gerichtsstand
   - Language(s) used
   - Parties named and their roles
   - Overall contract type (Kaufvertrag, Werkvertrag, Mietvertrag, Dienstleistungsvertrag, Lizenzvertrag, Gesellschaftsvertrag, AGB, Rahmenvertrag, etc.)
3. If documents are provided as file paths, read them via the Read tool. If provided as pasted text, confirm you have received both versions completely.
4. If only one document is provided, STOP and ask for the second version before proceeding.

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 3: Clarifying Questions

Before beginning the comparison, ask the user the following if not already clear from context:

1. **Baseline version:** "Welches Dokument ist die Ausgangsfassung (Baseline), gegen die verglichen werden soll?" -- This determines the direction of the diff (what was added TO vs. removed FROM).
2. **User's party:** "Welche Vertragspartei vertreten Sie?" -- This determines whose perspective risk is evaluated from. If the user is the Auftragnehmer, a clause limiting the Auftragnehmer's liability is beneficial; if they are the Auftraggeber, it is a risk.
3. **B2B or B2C:** "Handelt es sich um einen Vertrag zwischen Unternehmern (B2B, UGB) oder mit einem Verbraucher (B2C, KSchG)?" -- This fundamentally changes which mandatory law provisions apply. If B2C, the full KSchG analysis (especially Paragraph 6 KSchG) is mandatory.
4. **Known context:** "Gibt es einen konkreten Anlass fuer die Aenderungen (z.B. Gesetzesaenderung, Streitfall, Neuverhandlung)?" -- Optional but helps interpret intent behind changes.

If the user has already provided this context (e.g., "Ich bin der Mieter, vergleiche den alten und neuen Mietvertrag"), skip the questions that are already answered and proceed.

---

## Step 4: Structural Mapping

Map the structure of both versions against each other before comparing content.

### 4A: Build a Section Index for Each Version

For each document, create an internal index:
- Section/clause number
- Section title or subject matter
- Page or line reference (if available)

### 4B: Map Corresponding Sections

Create a mapping table linking sections in Version A to their counterpart in Version B:
- **Matched sections** -- same subject matter, possibly renumbered
- **Added sections** -- present in Version B but not in Version A (entirely new clauses)
- **Removed sections** -- present in Version A but not in Version B (deleted clauses)
- **Split sections** -- one clause in Version A became multiple in Version B
- **Merged sections** -- multiple clauses in Version A combined into one in Version B
- **Reordered sections** -- same content, different position in the document

### 4C: Flag Structural Changes

Structural changes themselves can be legally significant:
- **Removed sections** are always at least gelb-klassifiziert -- a deletion removes rights or obligations
- **Added sections** require careful reading -- they may introduce entirely new obligations, restrictions, or liability shifts
- **Reordering** that moves a clause from a prominent position to a buried position (e.g., from the main body into an Annex) may reduce its practical enforceability or visibility, even if the text is identical
- **Splitting** a single clear obligation into multiple sub-clauses may introduce ambiguity or carve-outs

---

## Step 5: Systematic Comparison

Work through every mapped section pair. For each section, execute sub-steps 4A through 4D.

### Step 5A: Text-Level Changes

For each matched section pair, identify every textual difference:

1. **Additions** -- new sentences, phrases, defined terms, conditions, carve-outs, or qualifiers added to the clause
2. **Deletions** -- text removed from the clause (words, sentences, entire paragraphs)
3. **Modifications** -- changed wording (e.g., "angemessene Frist" changed to "14 Tage", "Gewaehrleistung" changed to "Garantie", "grob fahrlassig" changed to "vorsaetzlich")
4. **Numeric changes** -- altered amounts, percentages, time periods (Fristen), liability caps, penalties
5. **Defined term changes** -- if a defined term was modified in the definitions section, trace its impact through every clause that uses it

Record each change with:
- Exact old text (from Version A)
- Exact new text (from Version B)
- Location (section/clause number in both versions)

### Step 5B: Legal Impact Assessment

For EACH change identified in 5A, assess the following:

1. **Risk shift:** Does this change shift risk from one party to the other? Which party benefits, which party bears additional risk?
2. **Protection removal:** Does this change remove a protection that the user's party previously had? (e.g., removing a Ruecktrittsrecht, shortening a Gewaehrleistungsfrist, deleting a Poenale for the other party's delay)
3. **New obligations:** Does this change add new obligations for the user's party? (e.g., new Mitwirkungspflichten, reporting duties, non-compete clauses, audit rights for the counterparty)
4. **Mandatory law compliance:** Does this change bring the clause into conflict with mandatory Austrian law?
   - For B2C: Check against Paragraph 6 Abs 1 KSchG (list of void clauses), Paragraph 6 Abs 2 KSchG (clauses void unless individually negotiated), Paragraph 6 Abs 3 KSchG (transparency requirement), Paragraph 9 KSchG (Gewaehrleistung), Paragraph 8 KSchG (Ruecktrittsrecht)
   - For B2B: Check against Paragraph 879 Abs 3 ABGB (groe blich benachteiligende AGB-Klauseln), Paragraph 864a ABGB (ueberraschende Klauseln), Paragraph 934 ABGB (laesio enormis)
   - For Mietrecht: Check MRG mandatory provisions (Paragraph 27, Paragraph 16, Paragraph 29, Paragraph 30 MRG)
   - For Arbeitsrecht: Check AngG, AVRAG, AZG, UrlG mandatory provisions
   - For Datenschutz: Check DSGVO and DSG compliance
5. **Liability cap changes:** Does this change alter Haftungsbeschraenkungen or Haftungsausschluesse? Note: exclusion of liability for Vorsatz or grobe Fahrlaessigkeit is void under Paragraph 6 Abs 1 Z 9 KSchG (B2C) and generally also under Paragraph 879 ABGB (B2B)
6. **Deadline/Frist changes:** Does this change alter any deadlines (Gewaehrleistungsfristen, Ruecktrittsfrist, Kuendigungsfristen, Nachfrist, Verjaehrung)? Compare against statutory defaults and mandatory minimums
7. **Gerichtsstand/Rechtswahl changes:** Does this change alter jurisdiction or choice of law? For B2C: consumer Gerichtsstand protections under Paragraph 14 KSchG cannot be waived
8. **Vertragsstrafe/Poenale changes:** Added, removed, or modified? Proportionality under Paragraph 1336 ABGB? Richterliches Maessigungsrecht?

For each change, cite the specific Paragraph(en) that make it legally relevant. Example: "Die Aenderung der Gewaehrleistungsfrist von 3 Jahren auf 1 Jahr verstoesst bei einem B2C-Vertrag gegen Paragraph 9 Abs 1 KSchG iVm Paragraph 933 ABGB (zwingende 2-Jahres-Frist fuer bewegliche Sachen)."

### Step 5C: Risk Classification

Classify each change into one of three categories:

- **Rot -- Kritisch** -- The change creates a new legal risk, removes an important protection, violates mandatory law, or could render the clause (or broader contract) void or unenforceable. Examples:
  - Exclusion of Gewaehrleistung in a B2C contract (void under Paragraph 9 KSchG)
  - Shortening Gewaehrleistungsfrist below statutory minimum
  - Adding a Haftungsausschluss for grobe Fahrlaessigkeit
  - Removing a Ruecktrittsrecht that exists by mandatory law
  - Adding a Gerichtsstand abroad in a B2C contract
  - Inserting a Verfallsklausel that circumvents Verjaehrungsrecht

- **Gelb -- Wichtig** -- The change materially alters rights or obligations but does not directly violate mandatory law. Requires careful consideration and likely negotiation. Examples:
  - Shortening a contractual (not statutory) deadline significantly
  - Adding substantial new Mitwirkungspflichten
  - Changing payment terms from 30 to 14 days
  - Reducing a liability cap from 100% to 50% of contract value
  - Adding a non-compete clause
  - Broadening a Freistellungsklausel (indemnification)
  - Changing from Gesamtschuldnerische to anteilige Haftung

- **Gruen -- Neutral** -- The change is cosmetic, clarifying, beneficial to the user's party, or legally immaterial. Examples:
  - Renumbering without content change
  - Correcting typos or improving grammar
  - Adding a clause that restates existing statutory law
  - Changes beneficial to the user's party
  - Updated addresses or contact details

### Step 5D: Cumulative Effect Analysis

After classifying individual changes, analyze whether the changes collectively create a pattern:

1. **Systematic risk shift:** Do multiple changes, each perhaps gelb individually, together create a systematic shift of risk to the user's party? Example: shortening the Gewaehrleistungsfrist AND limiting Schadenersatz AND adding a Haftungsausschluss AND removing the Ruecktrittsrecht -- individually important, collectively devastating.

2. **Salami tactics:** Are mandatory-law protections being gradually eroded through multiple small changes rather than one obvious violation? Example: not removing Gewaehrleistung outright (which would be obviously void) but combining Ruegepflicht + Beweislastumkehr + shortened Frist + exclusion of Folgeschaeden to achieve a similar practical effect.

3. **Balance assessment:** Overall, does the revised version shift the Vertragsbalance in favor of one party? Quantify roughly: "Von 12 materiellen Aenderungen beguentstigen 9 den Auftraggeber und 3 den Auftragnehmer."

4. **Verschlechterung der Verhandlungsposition:** Do the changes lock in terms that will be harder to renegotiate later (e.g., adding automatic renewal with long Kuendigungsfristen, adding Vertragsstrafe for early termination)?

---

## Step 6: Prioritize Changes by Legal Significance

Rank all identified changes in order of legal significance:

1. **First:** All Rot/Kritisch changes -- these require immediate attention and should be addressed before signing
2. **Second:** Changes that affect mandatory law compliance, even if currently classified as Gelb -- these may become Rot upon closer examination
3. **Third:** Gelb/Wichtig changes with the highest financial or practical impact
4. **Fourth:** Remaining Gelb changes
5. **Last:** Gruen/Neutral changes (listed for completeness)

Within each priority tier, order by:
- Financial impact (higher amounts first)
- Likelihood of the risk materializing (common scenarios first)
- Reversibility (irreversible consequences first)

---

## Step 7: Present the Comparison Report

Present the full comparison in the following structured format. Match the user's language (German if they wrote in German, English if English; default to German for Austrian legal analysis).

```markdown
# Vertragsvergleich

**Ausgangsfassung (Baseline):** [document name / version]
**Vergleichsfassung:** [document name / version]
**Datum der Analyse:** [date]
**Perspektive:** [user's party]
**Vertragstyp:** [contract type]
**Rechtsrahmen:** [B2B (UGB/ABGB) | B2C (KSchG/ABGB) | Sonstige]

---

## Aenderungs-Uebersicht

| Art der Aenderung | Anzahl | Davon Rot | Davon Gelb | Davon Gruen |
|--------------------|--------|-----------|------------|-------------|
| Neue Klauseln      | [n]    | [n]       | [n]        | [n]         |
| Gestrichene Klauseln | [n] | [n]       | [n]        | [n]         |
| Geaenderte Klauseln | [n]  | [n]       | [n]        | [n]         |
| Strukturelle Aenderungen | [n] | [n]  | [n]        | [n]         |
| **Gesamt**         | **[n]**| **[n]**   | **[n]**    | **[n]**     |

**Gesamtbewertung:** [1-2 sentence summary: e.g., "Die ueberarbeitete Fassung verschiebt das Risiko erheblich zugunsten des Auftraggebers. 4 Aenderungen sind rechtlich kritisch und beduerfen dringender Korrektur vor Unterzeichnung."]

---

## Kritische Aenderungen (Rot)

### Rot 1: [Clause title / subject]
- **Klausel:** [section number in both versions]
- **Vorher:** [exact or summarized old text]
- **Nachher:** [exact or summarized new text]
- **Rechtliche Auswirkung:** [detailed legal impact assessment with Paragraph-citations]
- **Betroffenes Gesetz:** [e.g., Paragraph 6 Abs 1 Z 9 KSchG, Paragraph 933 ABGB]
- **Risiko fuer Sie:** [concrete description of what could happen to the user's party]
- **Empfehlung:** [Ablehnen / Aendern / Akzeptieren nur wenn...]
- **Formulierungsvorschlag:**
  > [Concrete alternative wording that addresses the legal concern while remaining commercially reasonable. Written in Austrian legal German, ready to propose to the counterparty.]

[Repeat for each Rot change]

---

## Wichtige Aenderungen (Gelb)

### Gelb 1: [Clause title / subject]
- **Klausel:** [section number]
- **Vorher:** [old text]
- **Nachher:** [new text]
- **Rechtliche Auswirkung:** [impact with Paragraph-citations]
- **Risiko fuer Sie:** [practical impact]
- **Empfehlung:** [Verhandeln / Akzeptieren mit Vorbehalt / Akzeptieren]
- **Formulierungsvorschlag:** (if recommending a change)
  > [Alternative wording]

[Repeat for each Gelb change]

---

## Neutrale Aenderungen (Gruen)

| Nr. | Klausel | Art der Aenderung | Anmerkung |
|-----|---------|-------------------|-----------|
| 1   | [ref]   | [Klarstellung / Redaktionell / Zu Ihren Gunsten] | [brief note] |

---

## Kumulative Analyse

[Analysis from Step 5D: patterns, systematic shifts, overall balance assessment]

---

## Empfohlene Vorgehensweise

1. [Prioritized list of actions: which changes to reject, which to negotiate, which to accept]
2. [Suggested negotiation sequence]
3. [Any clauses the user should propose adding that are missing from both versions]

---

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---

Keine Rechtsberatung -- Diese Analyse ersetzt nicht die Beratung durch einen Rechtsanwalt. Bei kritischen Aenderungen (Rot) wird die Konsultation eines Rechtsanwalts dringend empfohlen.
```

---

## Critical Rules

1. **Always cite specific Paragraphen.** Every legal assessment must reference the relevant Austrian statute and section. Do not say "this might be problematic" without citing WHY (e.g., "verstoesst gegen Paragraph 6 Abs 1 Z 9 KSchG"). If you are uncertain of the exact Paragraph, say so explicitly and recommend verification.

2. **Flag compliance regression.** If a change transforms a previously-compliant clause into a non-compliant one, this is ALWAYS Rot. State clearly: "Die Ausgangsfassung war mit [Gesetz] konform. Die geaenderte Fassung verstoesst gegen [Paragraph], wodurch die Klausel nichtig/anfechtbar wird."

3. **Detect mandatory-law circumvention.** If a change appears designed to achieve indirectly what mandatory law prohibits directly, flag it explicitly. Example: "Die Kombination aus verkuerzter Ruegefrist (Paragraph X) und Beweislastumkehr (Paragraph Y) bewirkt de facto einen Gewaehrleistungsausschluss, der nach Paragraph 9 KSchG unzulaessig waere."

4. **Provide a Formulierungsvorschlag for every Rot change.** The user needs a concrete counter-proposal, not just a warning. The Formulierungsvorschlag must be legally sound, commercially reasonable, and written in proper Austrian contract German.

5. **Match the user's language.** If the user communicates in German, the entire report is in German. If in English, the report is in English but all Paragraph citations and Formulierungsvorschlaege remain in German (as they reference Austrian statutes and would be inserted into a German-language contract).

6. **Never invent Paragraph numbers.** If you are unsure of the exact statutory reference, state the legal principle and note that the specific section should be verified. Use the RIS MCP server if available to confirm current statutory text.

7. **Distinguish between nichtig and anfechtbar.** A clause that is nichtig (void, e.g., Paragraph 879 ABGB) has different practical consequences than one that is anfechtbar (voidable). State which applies.

8. **Consider Vertragsauslegung.** If a change introduces ambiguous language, note that under Paragraph 915 ABGB unclear provisions in AGB are interpreted contra proferentem (against the drafter) -- this may actually benefit the user if the counterparty drafted the change.

9. **Do not skip Gruen changes.** Even neutral changes should be listed for completeness. The user needs to know that you reviewed the entire document, not just the problematic parts.

10. **Track defined terms across the document.** A change to a definition in Paragraph 1 may have cascading effects in Paragraph 12, 15, and 22. Always trace defined term changes through every clause that references them.
