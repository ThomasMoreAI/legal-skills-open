---
name: recht-negotiate-momarcode1
title: /recht negotiate — Verhandlungsstrategie
description: Generates counter-proposals with replacement language (Formulierungsvorschlaege) for unfavorable contract clauses under Austrian law.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-negotiate
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

# /recht negotiate — Verhandlungsstrategie

Generates a complete negotiation strategy with specific counter-proposals, replacement clause text, fallback positions, and tactical sequencing for every unfavorable clause in an Austrian contract.

---

## Step 1: Read the Document Completely

Read the entire contract or document provided by the user. As you read:

- Identify the contract type (Kaufvertrag, Werkvertrag, Dienstleistungsvertrag, Mietvertrag, Lizenzvertrag, Gesellschaftsvertrag, AGB, Rahmenvertrag, etc.)
- Note the governing law clause (should be Austrian law — if not, flag immediately)
- Identify all parties and their roles
- Note the contract language (German or English — your output must match)
- Flag any clauses that appear non-standard, one-sided, or legally problematic
- Build a mental map of the contract's overall balance: does it heavily favor one party?

Do NOT skip appendices, schedules, or referenced AGB. These often contain the most problematic clauses.

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

Before generating any strategy, you MUST ask the user these questions. Do not proceed without answers:

### Mandatory Questions

1. **Welche Vertragspartei sind Sie?** (Which party are you?)
   - Are you the drafter or the recipient of this contract?
   - Which named party do you represent?

2. **B2B oder B2C?** (Business-to-business or business-to-consumer?)
   - If B2C: the user is a Verbraucher under the KSchG, which triggers mandatory consumer protection. Many clauses are automatically void under §6 KSchG regardless of what the contract says.
   - If B2B: KSchG does not apply (except §1 KSchG for certain sole traders). Focus shifts to UGB, ABGB, and market standards.
   - If unclear: ask for the user's legal form (GmbH, AG, Einzelunternehmer, Privatperson, etc.)

3. **Wie ist Ihre Verhandlungsposition?** (What is your negotiation leverage?)
   - Are you the only supplier/provider, or easily replaceable?
   - Is the counterparty a large company with non-negotiable standard terms, or a peer you can negotiate with?
   - Is there competitive pressure (other bidders)?
   - Rate the power dynamic: User dominant / Balanced / Counterparty dominant

4. **Was sind Ihre Must-haves vs. Nice-to-haves?** (What are your non-negotiables vs. desirables?)
   - Which terms are absolute deal-breakers if not changed?
   - Which terms would you like improved but could live with?
   - Are there specific commercial terms (price, payment terms, duration) that are fixed vs. flexible?

5. **Was ist Ihre BATNA?** (What is your Best Alternative To Negotiated Agreement?)
   - What happens if this deal falls through? Do you have alternatives?
   - How urgently do you need this contract?
   - Would walking away cause significant harm?

### Optional but Valuable Questions

6. **Gibt es eine bestehende Geschaeftsbeziehung?** (Is there an existing business relationship?)
   - First deal or renewal? Prior contracts to reference?
   - Relationship tone: collaborative or adversarial?

7. **Gibt es branchenspezifische Standards?** (Are there industry-specific standards?)
   - IT-Branche: oesterreichische IT-AGB, OENORM A 2060
   - Bau: OENORM B 2110, B 2118
   - Handel: Handelsbrauch nach §346 UGB

Wait for the user's responses before proceeding to Step 4.

---

## Step 4: Classify All Clauses by Negotiability

Go through the contract clause by clause. Classify each into one of four categories:

### Category A: Non-Negotiable — Mandatory Law Violations (MUST change)

These clauses violate zwingendes Recht (mandatory Austrian law) and are void or voidable regardless of what the parties agree. The counterparty CANNOT legitimately refuse these changes because the clause is legally unenforceable.

Check specifically for:

**If B2C (KSchG applies):**
- §6 Abs 1 KSchG — list of clauses that are automatically void in consumer contracts:
  - Z 1: exclusion/limitation of Gewaehrleistung or Schadenersatz for personal injury
  - Z 2: shifting Beweislast to the consumer's disadvantage
  - Z 3: denying the consumer the right to offset (Aufrechnung)
  - Z 5: excessive Vertragsstrafe (contractual penalty)
  - Z 9: allowing unilateral contract changes by the business
  - Z 14: unreasonably short Ruegefrist (notice period for defects)
  - Z 15: Gerichtsstandvereinbarung away from consumer's domicile
- §6 Abs 2 KSchG — clauses that are void unless specifically negotiated (individually ausgehandelt)
- §6 Abs 3 KSchG — the general Sittenwidrigkeits-clause for consumer contracts
- §9 KSchG — Gewaehrleistung cannot be excluded in consumer contracts
- §8 KSchG — Ruecktrittsrecht limitations

**General (B2B and B2C):**
- §879 Abs 1 ABGB — Sittenwidrigkeit (grossly unfair terms)
- §879 Abs 3 ABGB — groe blich benachteiligende AGB-Klauseln (the Austrian equivalent of the German AGB-Kontrolle, but under ABGB)
- §864a ABGB — unusual AGB clauses the other party could not reasonably expect (Ungewoehnliche Klauseln / "Ueberraschungsklauseln")
- §934 ABGB — laesio enormis (lesion beyond moiety, gross disproportion >50%)
- Mandatory provisions of specific contract types (e.g., Mietrechtsgesetz for rent, AVRAG/AngG for employment)

**Data Protection:**
- DSGVO Art 28 — if the contract involves Auftragsverarbeitung, mandatory processor agreement content
- DSG requirements

For each violation found, note:
- The specific clause
- The specific statute violated
- Why it is void/voidable
- What the law requires instead

### Category B: High Negotiability

Clauses where Austrian market standard, dispositives Recht (default law), or OGH case law supports the user's preferred position. The law does not mandate a change, but industry practice and legal defaults are on the user's side.

Examples:
- Zahlungsziel (payment terms) significantly below the 30-day default (§907a ABGB) or the industry norm
- Gewaehrleistungsfrist shorter than the statutory 2 years (§933 ABGB) in a B2B context
- Haftungsbeschraenkung that goes beyond what is standard in the industry
- Kuendigungsfrist (notice period) significantly shorter than market standard
- IP-Rechte clauses that transfer more than necessary for the contract's purpose
- Wettbewerbsverbot (non-compete) that is overly broad in scope, geography, or duration

### Category C: Medium Negotiability

Clauses where both positions have legal merit. Neither side has a clear statutory or case-law advantage. The outcome depends on commercial leverage and negotiation skill.

Examples:
- Haftungshoechtsbetrag (liability cap amount) — the existence of a cap is standard, but the specific amount is negotiable
- Vertragsdauer and Verlaengerungsklausel — automatic renewal terms
- Geheimhaltungsklausel scope and duration
- Schiedsklausel vs. ordentliche Gerichtsbarkeit
- Vertragsstrafe amount (in B2B where §1336 ABGB allows judicial reduction but does not set a specific limit)

### Category D: Low Negotiability

Clauses that are standard market practice, legally sound, and unlikely to be changed. Pushing on these wastes negotiation capital.

Examples:
- Salvatorische Klausel (severability clause) — standard boilerplate
- Schriftformerfordernis for amendments — reasonable and standard
- Standard Gerichtsstand at the defendant's domicile (§§65ff JN)
- Standard Gewaehrleistung mirroring statutory provisions
- Applicable law clause choosing Austrian law (if both parties are Austrian)

### Output for Step 4

Present the classification as a summary table:

```
| Klausel | Kategorie | Grund |
|---------|-----------|-------|
| §X Haftung | A — Zwingend | Verstoesst gegen §6 Abs 1 Z 1 KSchG |
| §Y Zahlung | B — Hoch | Marktstandard ist 30 Tage, nicht 14 |
| §Z Laufzeit | C — Mittel | Beide Positionen vertretbar |
| §W Salvatorisch | D — Gering | Marktstandard |
```

---

## Step 5: Systematic Negotiation Strategy

### Step 5A: Priority Ranking

Rank all unfavorable clauses (Categories A, B, C) by priority using this formula:

**Prioritaet = Finanzielle Auswirkung x Akzeptanzwahrscheinlichkeit x Rechtliche Staerke**

Score each factor 1-5:
- **Finanzielle Auswirkung**: How much does this clause cost the user if triggered? (1 = minimal, 5 = existential)
- **Akzeptanzwahrscheinlichkeit**: How likely is the counterparty to accept the change? (1 = very unlikely, 5 = very likely). Category A clauses automatically get 5 here (they have no choice — it is mandatory law).
- **Rechtliche Staerke**: How strong is the legal argument? (1 = pure commercial preference, 5 = mandatory law / clear OGH case law)

Present the priority ranking:

```
| Rang | Klausel | Finanz. | Akzeptanz | Recht | Score | Kategorie |
|------|---------|---------|-----------|-------|-------|-----------|
| 1    | Haftungsausschluss | 5 | 5 | 5 | 125 | A |
| 2    | Zahlungsziel | 4 | 4 | 3 | 48 | B |
| 3    | Kuendigungsfrist | 3 | 3 | 2 | 18 | C |
```

### Step 5B: Individual Clause Analysis

For EACH unfavorable clause (working down the priority list), provide ALL of the following:

#### Template per Clause:

```markdown
### Prioritaet [N]: [Clause Name / Section Reference]

**Aktuelle Formulierung:**
> "[Exact quote of the current clause from the contract]"

**Problem:**
[Clear explanation of why this clause is unfavorable to the user. Be specific: what risk does it create? What scenario would harm the user?]

**Rechtslage:**
[Cite the relevant Austrian statute(s) and, if available, OGH case law. Explain what the default legal position would be WITHOUT this clause. Example: "Ohne diese Klausel wuerde die gesetzliche Gewaehrleistungsfrist von 2 Jahren gemaess §933 Abs 1 ABGB gelten."]

**Formulierungsvorschlag (Primaer):**
> "[Complete replacement clause text in proper Austrian legal German. This must be copy-paste ready — full sentences, proper legal terminology, correct paragraph structure. NOT a summary or description of what the clause should say, but the ACTUAL TEXT.]"

**Verhandelbarkeit:** [Hoch / Mittel / Gering]

**Begruendung fuer die Verhandlung:**
[The specific argument to make to the counterparty. This should be persuasive, not just legally correct. Frame it in terms the counterparty can accept:
- For Category A: "Diese Klausel ist nach [§] unwirksam. Eine Berufung darauf wuerde im Streitfall scheitern. Es ist im Interesse beider Seiten, eine wirksame Formulierung zu verwenden."
- For Category B: "Der oesterreichische Marktstandard sieht [X] vor. Unsere Formulierung entspricht der gaengigen Praxis und schafft Rechtssicherheit fuer beide Seiten."
- For Category C: "Wir schlagen einen Kompromiss vor, der beiden Seiten gerecht wird: [X]."
]

**Fallback-Position (wenn Primaervorschlag abgelehnt wird):**
> "[Alternative replacement text that represents the MINIMUM the user should accept. This is the compromise position — less favorable than the primary proposal but still acceptable.]"

**Fallback-Begruendung:**
[Why this fallback is the floor. What happens if the user accepts less than even this? What risk remains?]

**Walk-away-Schwelle:**
[At what point should the user refuse to sign? Under what circumstances is this clause a deal-breaker even in its fallback form?]
```

**Rules for Formulierungsvorschlaege:**

1. Write in proper Austrian legal German (Rechtssprache). Use Austrian terminology:
   - "Gewaehrleistung" not "Gewaehrleistungsrecht" as a heading
   - "Schadenersatz" (Austrian spelling, one 's')
   - "Verbraucher" not "Konsument" in statutory references
   - "Bezirksgericht" / "Landesgericht" not "Amtsgericht"
   - "ABGB" not "BGB"

2. Each Formulierungsvorschlag must be a complete, self-contained clause. It must work if copy-pasted directly into the contract without any editing.

3. Include internal cross-references where necessary (e.g., "im Sinne des Punktes X dieses Vertrages").

4. If the contract is in English, write the Formulierungsvorschlag in English but note Austrian legal terms in parentheses where relevant.

5. Never write a Formulierungsvorschlag that itself violates mandatory Austrian law.

6. For Category A clauses (mandatory law violations), the Formulierungsvorschlag must bring the clause into full compliance. There is no room for a "lite" version that still violates the statute.

### Step 5C: Package Strategy

After analyzing individual clauses, design the overall negotiation package:

**Sequencing:**
1. **Lead with Category A (mandatory law violations).** These are non-negotiable. Present them as corrections that benefit both parties ("diese Klauseln sind ohnehin unwirksam — wir schlagen wirksame Formulierungen vor"). This establishes legal credibility and creates momentum.
2. **Follow with Category B (strong position).** The user has market standard and/or dispositives Recht on their side. Present these as reasonable adjustments to align with standard practice.
3. **Negotiate Category C (balanced) last.** These are the clauses where real give-and-take happens.

**Concession Bundles:**
Identify which Category C or lower-priority Category B clauses the user can concede on, and what to ask for in return:

```
Angebot: Wir akzeptieren [Klausel X in aktueller Form], wenn im Gegenzug [Klausel Y] wie folgt angepasst wird: [...]
```

Design 2-3 specific trade packages. Each package should give up something of lower value to the user in exchange for something of higher value.

**Tonfall-Empfehlung:**
Based on the power dynamic identified in Step 3:
- **User dominant:** Firm but professional. Present changes as requirements.
- **Balanced:** Collaborative. Frame as "gemeinsame Optimierung des Vertrages."
- **Counterparty dominant:** Diplomatic. Frame changes as risk-reduction for both sides. Lead with mandatory law fixes to establish that changes are legally necessary, not just preferences.

### Step 5D: BATNA Analysis

Based on the user's answers in Step 3, provide a structured BATNA assessment:

```markdown
**Best Alternative To Negotiated Agreement (BATNA):**

Ihre BATNA: [Description of what happens if the user walks away]
BATNA-Staerke: [Stark / Mittel / Schwach]

Bewertung: [If the user has a strong BATNA (other suppliers, no urgency), they can push harder. 
If the BATNA is weak (no alternatives, urgent need), they should prioritize must-haves 
and accept more on nice-to-haves.]

Walk-away-Punkt: [The specific combination of terms below which the deal is worse than the BATNA. 
Be concrete: "Wenn die Haftungsobergrenze unter EUR [X] bleibt UND die Zahlungsfrist 
unter 14 Tagen bleibt, ist die BATNA vorzuziehen."]

Reservation Price: [If applicable — the worst acceptable deal on key commercial terms]
```

---

## Step 6: Negotiation Script

Create concrete, ready-to-use communication text for the top 3 priority issues. Provide both an email/letter version and talking points for a meeting.

### Email/Brief Version

Write a complete, send-ready text (in the contract's language) that the user can use as the basis for their response to the counterparty. Structure:

```markdown
**Betreff:** Anmerkungen zum Vertragsentwurf [Vertragsbezeichnung] vom [Datum]

Sehr geehrte Damen und Herren, / Sehr geehrte Frau [Name] / Sehr geehrter Herr [Name],

vielen Dank fuer die Uebermittlung des Vertragsentwurfs. Wir haben diesen eingehend geprueft 
und moechten zu folgenden Punkten Aenderungen vorschlagen:

**1. [Clause Name] ([Section Reference])**
[Brief explanation of the issue — 1-2 sentences, professional tone]
Wir schlagen folgende Formulierung vor:
> "[Formulierungsvorschlag from Step 5B]"

**2. [Clause Name] ([Section Reference])**
[...]

**3. [Clause Name] ([Section Reference])**
[...]

Die uebrigen Bestimmungen des Vertragsentwurfs koennen wir in der vorliegenden Form akzeptieren. 
[Or: "Zu den uebrigen Punkten behalten wir uns weitere Anmerkungen vor."]

Wir freuen uns auf Ihre Rueckmeldung und stehen fuer ein Gespraech gerne zur Verfuegung.

Mit freundlichen Gruessen
[User]
```

### Gespraechsleitfaden (Meeting Talking Points)

For each of the top 3 issues, provide:

```markdown
**Thema [N]: [Clause Name]**

Eroeffnung: "[How to introduce the topic — suggested wording]"

Kernargument: "[The strongest argument in 1-2 sentences]"

Wenn Widerstand kommt: "[How to respond to pushback — anticipated objection and counter]"

Fallback anbieten: "[When and how to pivot to the fallback position]"

Ueberleitung zum naechsten Thema: "[How to bridge to the next issue]"
```

---

## Step 7: Present the Full Strategy

Compile the complete output in this structure:

```markdown
# Verhandlungsstrategie: [Contract Title / Type]

**Vertragstyp:** [e.g., Dienstleistungsvertrag]
**Vertragsparteien:** [Party A] (Auftraggeber) / [Party B] (Auftragnehmer)
**Perspektive:** [Which party the user represents]
**B2B/B2C:** [B2B / B2C — mit/ohne KSchG]
**Verhandlungsposition:** [Dominant / Ausgewogen / Schwaecher]
**Anzahl problematischer Klauseln:** [N] (davon [X] zwingend zu aendern)

---

## Klausel-Uebersicht

[Classification table from Step 4]

## Prioritaetsreihung

[Priority ranking table from Step 5A]

---

## Detailanalyse und Formulierungsvorschlaege

[All individual clause analyses from Step 5B, in priority order]

---

## Verhandlungspaket

### Sequenzierung
[Sequencing strategy from Step 5C]

### Tauschpakete (Concession Bundles)
[Trade packages from Step 5C]

### Tonfall
[Tone recommendation from Step 5C]

---

## BATNA-Analyse

[BATNA assessment from Step 5D]

---

## Verhandlungsschreiben (Entwurf)

[Email draft from Step 6]

---

## Gespraechsleitfaden

[Meeting talking points from Step 6]

---

## Zusammenfassung der Aenderungen

| # | Klausel | Aenderung erforderlich | Formulierungsvorschlag | Fallback |
|---|---------|----------------------|----------------------|----------|
| 1 | [...]   | Zwingend / Empfohlen | Siehe oben Prio 1    | Siehe oben |
| 2 | [...]   | [...]                | Siehe oben Prio 2    | Siehe oben |

---

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---

Hinweis: Diese Analyse dient der Vorbereitung auf Vertragsverhandlungen und stellt 
keine Rechtsberatung dar. Fuer verbindliche rechtliche Beurteilungen konsultieren Sie 
bitte einen oesterreichischen Rechtsanwalt.
```

---

## Critical Rules

1. **Always write actual Formulierungsvorschlaege.** Every unfavorable clause must get a complete, copy-paste-ready replacement text. Never just describe what the clause should say — write the actual clause.

2. **Distinguish "must fix" from "should fix."** Category A (mandatory law violations) requires a fundamentally different negotiation approach than Categories B/C. For Category A, the message is: "This clause is void as a matter of law. We are proposing a valid alternative." For Categories B/C, the message is: "This clause is unfavorable to us. We propose a fairer alternative."

3. **Never suggest accepting a clause that violates mandatory Austrian law.** Even as a fallback, the minimum position must comply with zwingendes Recht. You cannot "compromise" on a KSchG violation — the clause is void regardless of what the parties agree.

4. **Provide fallback positions for every negotiable clause.** The user needs to know their floor. A fallback is not optional — real negotiations require knowing when to concede and what the minimum acceptable position is.

5. **Cite specific statutes.** Every legal argument must reference the specific Austrian statute and paragraph (e.g., "§933 Abs 1 ABGB", "§6 Abs 1 Z 9 KSchG", "§879 Abs 3 ABGB"). If OGH case law is available and strengthens the argument, cite the Geschaeftszahl (e.g., "OGH 4 Ob 221/06p").

6. **Match the user's language.** If the user writes in German, the entire output is in German. If in English, output in English. The Formulierungsvorschlaege must match the contract's language.

7. **Be strategically honest about weak positions.** If a clause is Category D (low negotiability) or the user's position is weak, say so. Do not manufacture arguments where none exist. Wasting negotiation capital on unwinnable points weakens the user's position on important ones.

8. **Account for the Gesamtbild (overall picture).** A contract that is 90% favorable with one bad clause may still be a good deal. Do not recommend walking away from an overall favorable contract over a minor Category C issue. Conversely, a contract with multiple Category A violations signals a counterparty that is either legally unsophisticated or deliberately overreaching — both are red flags.

9. **Consider enforceability.** A clause that is theoretically unfavorable but practically unenforceable may be lower priority than a moderately unfavorable but highly enforceable clause. Factor this into the priority ranking.

10. **RIS verification.** If you cite a specific statute, verify the current wording via RIS if the RIS MCP Server is available. Statutes change — especially the KSchG, which has been amended frequently.
