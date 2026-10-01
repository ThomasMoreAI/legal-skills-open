---
name: recht-plain-momarcode1
title: /recht plain — Klartext-Ubersetzung
description: Translates Austrian legal language (Juristendeutsch) into plain German (Klartext). Every clause explained in simple terms.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-plain
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: contracts
language: de
---

# /recht plain — Klartext-Ubersetzung

Translates Juristendeutsch into plain language anyone can understand. This skill performs a systematic, clause-by-clause translation of Austrian legal documents, preserving legal accuracy while making every obligation, right, risk, and deadline comprehensible to a non-lawyer.

---

## Step 1: Read the Document Completely

Read the entire document from start to finish before producing any output. During this initial read:

- Identify the **Vertragstyp** (contract type): Kaufvertrag, Mietvertrag, Werkvertrag, Dienstvertrag, AGB, Gesellschaftsvertrag, Vergleich, Bescheid, Gerichtsurteil, etc.
- Identify the **parties** and their legal designations (AG = Auftraggeber, AN = Auftragnehmer, Vermieter/Mieter, Verkaufer/Kaufer, etc.)
- Note the **governing law** — confirm it is Austrian law (ABGB, UGB, KSchG, etc.). If it references German BGB or another jurisdiction, flag this immediately.
- Count the total number of clauses/paragraphs/Punkte.
- Note the document language (German or English) — your output language must match.

Do NOT start translating yet. You need the full picture before assessing any individual clause.

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

Before translating, establish context by asking (or inferring from the user's request) these three questions:

### 3A: Who is the user?

Determine which party position the user holds:
- "Sind Sie der/die [Parteibezeichnung A] oder der/die [Parteibezeichnung B]?"
- Example: "Sind Sie der Mieter oder der Vermieter?" / "Sind Sie der Auftraggeber oder der Auftragnehmer?"
- If the user provided this already, confirm it. If they said "I received this contract," infer they are the non-drafting party.

This is critical because the same clause can be vorteilhaft for one party and nachteilig for the other.

### 3B: What is their legal knowledge level?

Assess from the user's language:
- **Laie** (layperson): No legal background. Use everyday language. Explain every legal term.
- **Grundkenntnisse** (basic knowledge): Some familiarity with contracts. Explain only specialized terms.
- **Fachkundig** (knowledgeable): Business or legal background. Focus on Austrian-specific nuances and risk flags.

If unclear, default to **Laie** — it is better to over-explain than to assume knowledge.

### 3C: What matters most to them?

Ask or infer their primary concern:
- Signing decision: "Soll ich das unterschreiben?"
- Specific clause: "Was bedeutet Punkt 7?"
- Risk overview: "Wo sind die Fallen?"
- Comparison: "Ist das fair/marktublich?"
- Negotiation: "Was sollte ich andern?"

This determines how you weight the "Was Sie wissen mussen" summary in Step 6.

If the user says "just translate it" or provides no context, proceed with: party = non-drafting party, knowledge = Laie, concern = signing decision.

---

## Step 4: Identify and Prioritize Clauses for Translation

Create an internal working list of every clause. Prioritize in this order:

### Priority A — Obligations and Deadlines (Pflichten und Fristen)

These are translated first because missing a deadline can cause immediate legal harm:
- Payment obligations (Zahlungspflichten, Falligkeiten)
- Performance deadlines (Leistungsfristen, Fertigstellungstermine)
- Notice periods (Kundigungsfristen, Rucktrittsfrist)
- Response deadlines (Rugefristen, Einspruchsfristen, Nachfrist)
- Statute of limitations triggers (Verjahrungsfristen, Gewahrleistungsfristen)

For EVERY Frist found, extract:
- What the deadline is
- When it starts running (ab wann)
- What happens if the user misses it (Rechtsfolge bei Fristversaumnis)

### Priority B — Risk Clauses (Risikoklauseln)

Clauses that expose the user to financial or legal risk:
- Liability limitations or exclusions (Haftungsbeschrankung, Haftungsausschluss)
- Penalty clauses (Vertragsstrafe, Ponale)
- Indemnification (Schadloshaltung, Freistellung)
- Warranty limitations (Gewahrleistungseinschrankung)
- Termination triggers and consequences (Auflosung, Verfall)
- Non-compete / exclusivity (Wettbewerbsverbot, Exklusivitat)
- Automatic renewal (automatische Verlangerung)
- Jurisdiction and venue (Gerichtsstand, Schiedsklausel)

### Priority C — Legal Terms of Art (Juristische Fachbegriffe)

Austrian legal terms that have specific meanings different from everyday German or from German (BGB) law:

| Term | Common Misunderstanding | Correct Austrian Meaning |
|------|------------------------|--------------------------|
| Gewahrleistung | Often confused with Garantie | Gesetzliche Mangelhaftung nach ABGB §§922ff — verschuldensunabhangig, kraft Gesetzes, nicht dasselbe wie eine freiwillige Garantie |
| Schadenersatz | Often confused with Gewahrleistung | Verschuldensabhangiger Anspruch auf Ersatz des Schadens (ABGB §§1293ff) |
| Verzug | "Delay" | Rechtlich qualifizierte Nichtleistung trotz Falligkeit und Mahnung (oder Entbehrlichkeit der Mahnung) |
| Gewahrleistungsfrist | "Warranty period" | Keine Verjahrungsfrist im technischen Sinn, aber Frist fur Mangelhaftungsanspruche: 2 Jahre beweglich, 3 Jahre unbeweglich (§933 ABGB) |
| Vertragsstrafe | "Fine" | Pauschalisierter Schadenersatz, fallig ohne Schadensnachweis, gerichtlich maßigbar (§1336 ABGB) |
| Rucktritt | "Cancellation" | Ruckwirkende Aufhebung des Vertrags, nicht dasselbe wie Kundigung (ex tunc vs ex nunc) |
| Kundigung | "Cancellation" | Beendigung fur die Zukunft (ex nunc), keine Ruckabwicklung |
| Irrtumsanfechtung | "Mistake" | Anfechtung wegen Geschaftsirrtum (§871 ABGB) — strenge Voraussetzungen |
| Abtretung | "Transfer" | Ubertragung einer Forderung an einen Dritten (Zession, §§1392ff ABGB) |
| Aufrechnung | "Offset" | Einseitige Tilgung durch Gegenrechnung gleichartiger Forderungen (§§1438ff ABGB) |
| Gesamtschuldnerisch | "Joint" | Jeder Schuldner haftet fur die GESAMTE Schuld, nicht nur seinen Anteil |

Always flag these terms when encountered. Never silently translate them to an everyday word without explanation.

### Priority D — Standard/Boilerplate Clauses

Lower priority but still translated:
- Severability (Salvatorische Klausel)
- Entire agreement (Vollstandigkeitsklausel)
- Written form requirements (Schriftformklausel)
- Applicable law (Rechtswahlklausel)
- Definitions (Begriffsbestimmungen)

---

## Step 5: Systematic Translation

Process EACH clause following sub-steps 4A through 4D. Do not skip any clause.

### Step 5A: Extract, Translate, Explain

For each clause, produce three elements:

1. **Juristendeutsch** — Quote the original text (abbreviated if very long, but include the legally operative language verbatim)

2. **Klartext** — Translate to plain language following these rules:
   - Replace passive constructions with active ones: "Es wird vereinbart, dass..." becomes "Sie vereinbaren, dass..." or "Sie mussen..."
   - Replace nominalizations with verbs: "Die Erbringung der Leistung" becomes "Wenn [Partei] die Leistung erbringt"
   - Replace double negatives with positive statements: "nicht ohne vorherige Zustimmung" becomes "nur mit vorheriger Zustimmung"
   - Replace legal references with their content: "gemaß §1162b ABGB" becomes "gemaß §1162b ABGB (= sofortige Entlassung aus wichtigem Grund)"
   - Use "Sie" (the user) and the other party's name/role, not abstract legal designations
   - Keep sentences under 20 words where possible
   - NEVER oversimplify to the point where a legal nuance is lost. If the original says "grob fahrlassig" do NOT translate as just "fahrlassig" — the distinction matters enormously.

3. **Praktische Konsequenz** — One sentence explaining what this means for the user's daily life or business:
   - "Das heißt: Wenn Sie nicht innerhalb von 14 Tagen schriftlich widersprechen, verlangert sich der Vertrag automatisch um ein weiteres Jahr."
   - "Das heißt: Wenn die Lieferung zu spat kommt, mussen Sie dem Lieferanten erst eine angemessene Nachfrist setzen, bevor Sie vom Vertrag zurucktreten konnen."

### Step 5B: Flag User Impact

Assign each clause one of three flags:

- **Vorteilhaft** — The clause benefits the user or is better than what the law would provide without it
- **Neutral** — The clause restates the default legal position (dispositives Recht) or affects both parties equally
- **Nachteilig** — The clause disadvantages the user compared to the default legal position, limits their rights, or creates additional obligations

When flagging, consider:
- What would the legal default be WITHOUT this clause? (dispositives Recht nach ABGB/UGB/KSchG)
- Is the clause better or worse than the default for the user?
- If the user is a Verbraucher (consumer), check against KSchG §6 — a nachteilig clause may actually be UNWIRKSAM (void) under consumer protection law. Flag this: "Nachteilig — aber moglicherweise unwirksam nach §6 Abs 1 Z [X] KSchG"

### Step 5C: "Das bedeutet konkret..." Explanations

For any clause involving a complex legal concept, add a concrete explanation with a real-world example:

**Trigger this sub-step when the clause involves:**
- Gewahrleistung or Garantie
- Schadenersatz (especially the verschuldensabhangig/verschuldensunabhangig distinction)
- Vertragsstrafe
- Haftungsbeschrankung (especially "Haftung fur leichte Fahrlassigkeit ausgeschlossen")
- Gesamtschuldnerische Haftung
- Rucktrittsrecht vs Kundigungsrecht
- Aufrechnung or Zuruckbehaltungsrecht
- Sicherungsabtretung or Eigentumsvorbehalte
- Wettbewerbsverbot / Konkurrenzklausel
- Schiedsklausel (arbitration)

**Format:**

> **Das bedeutet konkret:** [Real-world scenario in 2-3 sentences]
>
> *Beispiel:* "Sie beauftragen einen Handwerker mit der Badsanierung fur EUR 15.000. Nach 6 Monaten zeigt sich ein Mangel (undichte Fliesen). Ohne diese Klausel hatten Sie 3 Jahre Gewahrleistung. MIT dieser Klausel haben Sie nur 1 Jahr — Ihr Anspruch ware bereits verfallen."

### Step 5D: Identify Hidden Obligations

Specifically scan for obligations that a non-lawyer would likely overlook:

- **Automatische Verlangerung**: Contracts that auto-renew unless cancelled within a specific Frist before the end date. Flag the exact date by which the user must act.
- **Vertragsstrafe-Trigger**: Conditions under which a penalty becomes payable — especially if the trigger is something the user might do routinely (e.g., late delivery, minor breach).
- **Verzichtserklarungen**: Clauses where the user waives rights they might not know they have (Rugerecht, Aufrechnungsrecht, Zuruckbehaltungsrecht, Wandlungsrecht).
- **Mitwirkungspflichten**: Obligations to cooperate that, if breached, shift liability or delay responsibility to the user (Obliegenheiten, Beistellungspflichten).
- **Formvorschriften**: Requirements that notices must be sent by eingeschriebener Brief (registered mail) or that verbal agreements are invalid — the user might assume an email or phone call suffices.
- **Kostenuberwälzung**: Hidden cost-shifting clauses (e.g., "Kosten der Vertragserrichtung tragt der Kaufer," which means the user pays for the seller's lawyer).
- **Abtretungsverbote**: Clauses preventing the user from transferring their rights to someone else.
- **Konkurrenz-/Wettbewerbsklauseln**: Post-contractual restrictions that limit the user's future business activities.

For each hidden obligation found, output:

> **Versteckte Pflicht:** [Description]
> **Wo im Vertrag:** [Clause reference]
> **Was passiert, wenn Sie es ubersehen:** [Consequence]

---

## Step 6: "Was Sie wissen mussen" Summary

After completing the clause-by-clause translation, create a summary of the 5-7 most important things the user should understand before signing or agreeing.

### Selection Criteria

Include items in this priority order:
1. Any clause that could cost the user significant money (Vertragsstrafe, Haftung, Kostenklauseln)
2. Any deadline the user must meet (Fristen, Kundigungstermine)
3. Any right the user is waiving (Verzicht auf Gewahrleistung, Aufrechnungsverbot)
4. Any clause that is potentially unwirksam under KSchG (if the user is a consumer)
5. Any clause that deviates significantly from the gesetzliche Regelung to the user's disadvantage
6. Any hidden obligation from Step 5D
7. Any clause where the plain reading differs from the legal reading (flag under §915 ABGB Unklarheitenregel: "bei einseitig vorformulierten Vertragsbedingungen werden Unklarheiten zulasten des Verwenders ausgelegt")

### Format

```
## Was Sie wissen mussen

1. **[Kurztitel]:** [One plain-language sentence explaining the issue and what the user should do about it]

2. **[Kurztitel]:** [...]

...

5-7. **[Kurztitel]:** [...]
```

Each item must be actionable — not just "this clause exists" but "this clause means X, and you should Y."

---

## Step 7: Present the Translation in Structured Format

### Output Structure

```markdown
# Klartext-Ubersetzung: [Document Title / Type]

**Vertragstyp:** [e.g., Werkvertrag nach ABGB §§1165ff]
**Ihre Position:** [e.g., Auftraggeber / Mieter / Kaufer]
**Anzahl Klauseln:** [X]
**Gesamtbewertung:** [Kurze Einschatzung: "Uberwiegend fair / Deutlich zulasten des [Partei] / Marktublich mit einigen problematischen Klauseln"]

---

## Klausel-fur-Klausel-Ubersetzung

| # | Klausel | Juristendeutsch | Klartext | Fur Sie |
|---|---------|----------------|----------|---------|
| 1 | [Titel] | "[Originaltext, ggf. gekurzt]" | [Klartext-Ubersetzung] | [Flag] |
| 2 | ... | ... | ... | ... |

### Detailanalyse der wichtigsten Klauseln

#### Klausel [#]: [Titel]

**Original:** "[Volltext]"

**Klartext:** [Ausfuhrliche Ubersetzung]

**Praktische Konsequenz:** [Was das fur Sie heißt]

> **Das bedeutet konkret:** [Beispiel, wenn zutreffend]

**Bewertung:** [Vorteilhaft/Neutral/Nachteilig] — [Begrundung]

[Repeat for each Priority A and Priority B clause]

### Versteckte Pflichten

[List from Step 5D, if any found]

---

## Was Sie wissen mussen

[Summary from Step 6]

---

## Fristen-Ubersicht

| Frist | Dauer | Beginnt ab | Wenn versaumt |
|-------|-------|-----------|---------------|
| [e.g., Rugeobliegenheit] | [e.g., 14 Tage] | [e.g., Entdeckung des Mangels] | [e.g., Gewahrleistungsanspruch geht verloren] |

---

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---

Diese Ubersetzung dient dem Verstandnis des Dokuments.
Sie ersetzt KEINE Rechtsberatung durch einen Rechtsanwalt.
```

### Formatting Rules

- The summary table gives a quick overview; the Detailanalyse section provides depth for important clauses. Always include both.
- Use the table for ALL clauses (even boilerplate).
- Use the Detailanalyse for Priority A and B clauses only (obligations, deadlines, risks).
- The Fristen-Ubersicht table collects ALL deadlines in one place for easy reference.
- If the document is very long (>20 clauses), group related clauses in the table under section headers.

---

## Critical Rules

These rules are non-negotiable and override all other instructions:

### Rule 1: Never Oversimplify at the Cost of Legal Accuracy

- "Haftung fur leichte Fahrlassigkeit ist ausgeschlossen" must NOT become "Sie haften nicht." It must become something like: "Sie konnen keinen Schadenersatz verlangen, wenn der Vertragspartner einen Fehler gemacht hat, der ihm nur leicht vorwerfbar ist (leichte Fahrlassigkeit). Bei grober Fahrlassigkeit oder Vorsatz haftet er aber weiterhin."
- "Gewahrleistung wird auf 12 Monate verkurzt" must NOT become "12 Monate Garantie." The distinction between Gewahrleistung and Garantie must be preserved and explained.

### Rule 2: Keep and Explain Untranslatable Legal Terms

When a German legal term has no adequate plain equivalent, keep the term and explain it in parentheses:

- "Gewahrleistung (= gesetzliche Mangelhaftung nach ABGB, nicht dasselbe wie eine freiwillige Garantie des Herstellers)"
- "Schadenersatz (= Ersatz fur Schaden, den der andere VERSCHULDET hat — also absichtlich oder fahrlassig verursacht)"
- "Verzug (= Sie sind nicht einfach 'spat dran', sondern rechtlich in Verzug — das hat Konsequenzen wie Verzugszinsen und Rucktrittsrecht der anderen Seite)"

### Rule 3: Flag Divergence Between Plain Reading and Legal Reading

If a clause could be read differently by a layperson than by a lawyer, flag this explicitly:

> **Achtung — Unterschied zwischen Alltagsverstandnis und juristischer Bedeutung:**
> Ein Laie wurde diese Klausel wahrscheinlich so verstehen: [Alltagslesung].
> Juristisch bedeutet sie aber: [juristische Bedeutung].
> Hinweis: Nach §915 ABGB (Unklarheitenregel) werden unklare Klauseln in AGB zulasten desjenigen ausgelegt, der sie formuliert hat.

### Rule 4: Match Input Language

- German document with German request --> German Klartext output
- German document with English request --> English explanation, but keep all legal terms in German with English explanations in parentheses
- English document --> English output
- Never mix languages within a single explanation

### Rule 5: Highlight Every Frist (Deadline)

Every deadline found in the document must be:
1. Listed in the clause-by-clause translation where it appears
2. Collected in the Fristen-Ubersicht table at the end
3. Flagged with what happens if it is missed (Rechtsfolge bei Fristversaumnis)

Format for deadlines within the text:

> **FRIST:** [Duration] ab [trigger event] — bei Versaumnis: [consequence]

---

## Special Cases

### AGB (Allgemeine Geschaftsbedingungen)

When the document is AGB:
- Check EVERY clause against §879 Abs 3 ABGB (groblich benachteiligende Klauseln in AGB)
- If the user is a consumer, additionally check against §6 KSchG (Unzulassige Vertragsbestimmungen) — go through the catalogue of §6 Abs 1 Z 1-15 and §6 Abs 2 Z 1-7 systematically
- Flag any clause that is potentially unwirksam with: "Moglicherweise unwirksam: Diese Klausel konnte gegen §[X] verstoßen und daher nichtig sein."

### Bescheide (Administrative Decisions)

When the document is a Bescheid:
- Identify the Behorde (authority) and Rechtsgrundlage (legal basis)
- Translate the Spruch (operative part) and Begrundung (reasoning) separately
- Highlight the Rechtsmittelbelehrung (appeal instructions): which Rechtsmittel, to which Behorde/Gericht, within which Frist
- Flag if the Frist for appeal is running NOW

### Gerichtsurteile (Court Decisions)

When the document is a court judgment:
- Translate the Spruch (holding), Kostenentscheidung (costs), and Begrundung separately
- Highlight: Can the user appeal? To which court? Within what Frist?
- Explain the practical consequences of the judgment (What must the user do/pay/stop doing?)
