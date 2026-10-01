---
name: recht-evidence-momarcode1
title: /recht evidence — Beweiswürdigung
description: Evaluates evidence strength under Austrian civil procedure (ZPO). Assesses Urkunden, Zeugen, Sachverständige, Augenschein, Parteienvernehmung. Flags gaps and admissibility issues.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-evidence
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: litigation
language: de
---

# /recht evidence — Beweiswürdigung

When the user provides evidence or describes what evidence they have, follow these steps.

---

## Step 1: List All Available Evidence

Go through everything the user has mentioned or uploaded. For each item, determine:

1. **What is it?** (contract, email, photo, invoice, witness, etc.)
2. **What does it prove?** (which fact?)
3. **Classify it** into one of the 5 ZPO evidence types (see Step 2)

If the user hasn't listed their evidence, ask:
> "Welche Beweise haben Sie? (Verträge, E-Mails, Fotos, Rechnungen, Zeugen, Gutachten, etc.)"

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 3: Classify Each Piece by ZPO Type

Austrian civil procedure recognizes 5 types of evidence, in this hierarchy of strength:

**1. Öffentliche Urkunden (§§292-294 ZPO)** — STRONGEST
- Court judgments, Grundbuchauszüge, Firmenbuchauszüge, notarielle Urkunden
- Effect: Full proof (volle Beweiskraft) — opponent must prove they are false
- If the user has one of these for a key fact, that fact is essentially proven

**2. Privaturkunden (§§294-319 ZPO)** — STRONG
- Signed contracts, invoices, receipts, letters, faxes
- Effect: Prove the declaration was made, IF the signature is undisputed
- If opponent disputes signature → Schriftvergleichung (§314 ZPO)
- E-Mails, WhatsApp messages, screenshots: Treated as Privaturkunden BUT opponent can more easily dispute authenticity
- Tip: Advise user to have screenshots notarized or certified if key evidence is digital

**3. Zeugen (§§320-350 ZPO)** — MODERATE
- Any person who perceived relevant facts
- Weaknesses: Memory fades, bias, Parteinähe (closeness to a party)
- Check: Does the witness have a Zeugnisverweigerungsrecht? (§321 ZPO — close family; §322 — professional secrecy)
- The court evaluates credibility freely (freie Beweiswürdigung §272 ZPO)

**4. Sachverständige (§§351-367 ZPO)** — MODERATE (but decisive for technical questions)
- Court-appointed experts (gerichtliche Sachverständige) — this is what counts
- Privatgutachten (private expert reports) = only qualified Parteivorbringen, NOT evidence
- When needed: Medical questions, construction defects, valuations, technical disputes
- Cost: Sachverständigengebühren can be significant — warn the user

**5. Parteienvernehmung (§§371-383 ZPO)** — WEAKEST
- Testimony by one of the parties themselves
- Only admissible as subsidiary evidence (subsidiäres Beweismittel) — when no other evidence available
- Very low evidentiary weight — courts are skeptical
- If the user's ONLY evidence for a key fact is their own testimony, flag this as a Beweisnotstand

---

## Step 4: Assess Strength for Each Key Fact

For each fact that needs to be proven in the case:

1. **What evidence exists for this fact?**
2. **How strong is it?** Rate: 🟢 Strong / 🟡 Moderate / 🔴 Weak
3. **Can the opponent challenge it?** How?
4. **Is there a gap?** If yes, how could it be filled?

Apply these rules:
- Öffentliche Urkunde for a fact → 🟢 essentially proven
- Signed private document (undisputed) → 🟢 strong
- Email/digital evidence → 🟡 moderate (authenticity can be disputed)
- Single witness with no connection to parties → 🟡 moderate
- Witness who is friend/family of user → 🟡 weak-moderate (Parteinähe)
- Only party testimony → 🔴 weak (Beweisnotstand)
- No evidence at all → 🔴 gap — flag immediately

---

## Step 5: Check Burden of Proof

Determine who must prove what:

**Default rule:** Each party proves facts favorable to their position.

**Key exceptions in Austrian law:**
- **§1298 ABGB** — In contractual claims, the breaching party must disprove fault (Verschulden). This is a MAJOR advantage for the user if they are claiming contractual Schadenersatz.
- **§1296 ABGB** — If a Schutzgesetz (protective statute) was violated, fault is presumed.
- **§924 ABGB** — In Gewährleistung, defects appearing within 6 months after delivery are presumed to have existed at delivery (Vermutung). After 6 months, user must prove.
- **PHG §5** — Product liability: Geschädigter must prove defect, damage, and causation. But NOT fault.
- **GlBG** — In discrimination cases, burden shifts to employer once prima facie case is made (Glaubhaftmachung).

State clearly for each claim: **"Sie müssen beweisen: [X]. Der Gegner muss beweisen: [Y]."**

---

## Step 6: Identify Gaps and Recommend Actions

For each evidence gap:

1. **Urkundenvorlage (§303 ZPO)** — Can the user request the court to order the opponent to produce a document they're holding?
2. **Sachverständigengutachten** — Should a court expert be requested? For what question?
3. **Zeugen** — Are there witnesses the user hasn't thought of? (neighbors, colleagues, bystanders)
4. **Beweissicherung (§384ff ZPO)** — Is evidence at risk of being lost? File for preservation.
5. **Digital evidence** — Advise: screenshot everything NOW, get notarized if possible.

---

## Step 7: Present Results

```markdown
# Beweiswürdigung

**Anzahl Beweismittel:** [n]
**Beweislage gesamt:** 🟢 Stark / 🟡 Ausreichend / 🔴 Schwach

## Beweislage-Übersicht
| # | Beweis | Typ (ZPO) | Beweist | Stärke | Angriffspunkte |
|---|--------|-----------|---------|--------|---------------|
| 1 | [item] | Privaturkunde | [fact] | 🟢 | Keine wesentlichen |
| 2 | [item] | Zeuge | [fact] | 🟡 | Parteinähe |
| 3 | FEHLT | — | [fact] | 🔴 | Beweisnotstand |

## Beweislast-Verteilung
| Tatsache | Beweislast | Beweis vorhanden | Stärke |
|----------|-----------|-----------------|--------|
| [fact 1] | Sie (Kläger) | ✅ Beilage ./A | 🟢 |
| [fact 2] | Gegner (§1298 ABGB) | — | 🟢 (Beweislastumkehr!) |
| [fact 3] | Sie | ❌ | 🔴 Lücke |

## ⚠️ Beweislücken
| Tatsache | Problem | Empfehlung |
|----------|---------|-----------|
| [fact] | Nur Parteienvernehmung | Zeugen suchen / Urkundenvorlage beantragen |

## Empfohlene Maßnahmen
1. [Most urgent evidence action]
2. [Second]
3. [Third]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---
⚠️ Keine Rechtsberatung.
```
