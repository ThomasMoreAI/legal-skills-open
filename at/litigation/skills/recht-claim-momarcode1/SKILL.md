---
name: recht-claim-momarcode1
title: /recht claim — Anspruchsprüfung
description: Identifies all legal claims (Anspruchsprüfung) from facts under Austrian law. Maps each claim to specific §§, checks Tatbestandsmerkmale, Einwendungen, Beweislast, and Verjährung.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-claim
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: litigation
language: de
---

# /recht claim — Anspruchsprüfung

When the user describes a factual situation and wants to know their legal options, follow these steps.

---

## Step 1: Gather the Facts

Read what the user has provided. You need:

1. **What happened?** — Chronological sequence of events
2. **Who is involved?** — Parties, their roles, consumer or business?
3. **When did it happen?** — Dates are critical for Verjährung
4. **What does the user want?** — Money, performance, rescission, injunction?
5. **What evidence exists?** — Documents, witnesses, correspondence?

If any of these is missing, ask. Be specific:
> "Wann genau ist das passiert? Das Datum ist wichtig für die Verjährungsprüfung."

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 3: Identify ALL Possible Claims

Go through this checklist systematically. Check every category — users often miss claims they didn't know they had.

### A: Vertragliche Ansprüche (check first — these are strongest)

Ask yourself: Was there a contract (even oral)?

If yes, check each of these:

1. **Erfüllung (§918 ABGB)** — Can the user demand performance?
   - Requirements: Valid contract + obligation due + no performance yet
   - Check: Did user set a Nachfrist? (required per §918 unless entbehrlich)

2. **Gewährleistung (§§922-933b ABGB)** — Is there a Mangel (defect)?
   - Requirements: Contract + Mangel at time of delivery + within Frist
   - Check: Was it a Sachmangel or Rechtsmangel?
   - Check: Did user assert it in time? (2 years movable, 5 years immovable per §933)
   - Check B2B: Did user comply with §377 UGB Rügepflicht? (unverzüglich = within ~14 days)
   - Remedies: First Verbesserung/Austausch → then Preisminderung/Wandlung (§932 ABGB Stufenmodell)

3. **Schadenersatz aus Vertrag (§§1295ff ABGB)** — Did the other side cause damage by breaching?
   - Requirements: Pflichtverletzung + Verschulden + Schaden + Kausalität + Rechtswidrigkeit
   - Note: §1298 ABGB shifts burden of proof for Verschulden to the breaching party!
   - Check: Positives Vertragsinteresse (Erfüllungsinteresse) or negatives (Vertrauensinteresse)?

4. **Rücktritt (§918 ABGB)** — Can the user rescind?
   - Requirements: Other party in default + Nachfrist set (or entbehrlich)
   - Note: In B2C, also check §3 KSchG (Haustürgeschäft) and FAGG (Fernabsatz) — 14 day right

5. **Irrtumsanfechtung (§§870-875 ABGB)** — Was the user misled?
   - Requirements: Wesentlicher Irrtum + caused by other party or erkennbar
   - Frist: Anfechtung within 3 years (§1487 ABGB)

6. **Laesio enormis (§934 ABGB)** — Was the price grossly unfair?
   - Requirements: Value of one side less than half of other's at time of contract
   - Excludable in B2B by agreement, NOT in B2C

### B: Außervertragliche Ansprüche (if no contract, or additional claims)

7. **Deliktischer Schadenersatz (§1295 Abs 1 ABGB)**
   - Requirements: Rechtswidrigkeit + Verschulden + Schaden + Kausalität
   - Burden of proof: User must prove ALL elements (unlike contract!)

8. **Gefährdungshaftung** — Was a dangerous activity involved?
   - EKHG: Motor vehicles, railways
   - PHG: Defective product
   - No Verschulden needed — strict liability

9. **Bereicherung (§§1431-1437 ABGB)** — Did the other side get enriched without legal basis?
   - Subsidiär — only if no other claim works
   - Frist: 30 years (but 6 months for Irrtumsbereicherung per §1487)

### C: Sachenrechtliche Ansprüche

10. **Eigentumsfreiheitsklage (§523 ABGB)** — Is user's property being interfered with?
11. **Besitzstörungsklage (§339 ABGB)** — Was user's possession disturbed?
    - ⚠️ **30 TAGE FRIST** ab Kenntnis der Störung (§454 ZPO)! Flag this urgently.
12. **Unterlassungsklage (§364 ABGB)** — Ongoing or threatened interference?

### D: Arbeitsrechtliche Ansprüche (if employment context)

13. **Kündigungsanfechtung (§105 ArbVG)** — Was dismissal socially unjustified or motivated by prohibited reason?
    - ⚠️ **2 Wochen Frist** for Klage at Gericht!
14. **Entlassungsanfechtung (§106 ArbVG)** — Was there no valid Entlassungsgrund?
15. **Entgeltansprüche** — Unpaid wages, Sonderzahlungen, Überstunden?
16. **Abfertigung** — Alt (AngG) or Neu (BMSVG)?
17. **Urlaubsersatzleistung (§10 UrlG)** — Unused vacation days upon termination?

---

## Step 4: For Each Identified Claim, Run the Full Check

For every claim that looks viable, complete this analysis:

### Tatbestandsmerkmale (Elements)
List each element. For each, state:
- ✅ Met — with reference to which fact supports it
- ❌ Not met — explain why
- ❓ Unclear — what additional information or evidence is needed

### Einwendungen (Defenses)
Think like the opposing lawyer. What could they argue?
- Verjährung?
- Mitverschulden (§1304 ABGB)?
- Vertragsausschluss?
- Force majeure?
- Already fulfilled?

### Beweislast (Burden of Proof)
State who must prove what:
- Default: Each party proves facts favorable to them
- Exception: §1298 ABGB — in contract breach, the breaching party must disprove fault
- Exception: §1296 ABGB — fault is presumed if a Schutzgesetz was violated

### Verjährung
Calculate the limitation period. State:
- Which Frist applies and why
- When it started running (Kenntnis for §1489 ABGB)
- When it expires
- Status: 🟢 Offen / 🟡 Kritisch (< 3 months) / 🔴 Verjährt

---

## Step 5: Identify Counterclaims

Think: What could the OTHER side claim against the user?
- Gegenrechte that could be set off (Aufrechnung §1438 ABGB)
- Counterclaims that could be filed (Widerklage)
- Zurückbehaltungsrecht (§1052 ABGB)

---

## Step 6: Present Results

```markdown
# Anspruchsprüfung

**Sachverhalt:** [2-3 sentence summary]
**Ihre Position:** [role]
**Rechtsgebiet(e):** [identified areas]

## Identifizierte Ansprüche

### Anspruch 1: [Name] — [§ Grundlage]
| Element | Status | Begründung |
|---------|--------|-----------|
| [element 1] | ✅ | [fact that supports it] |
| [element 2] | ❓ | [what's missing] |

**Einwendungen des Gegners:** [what they could argue]
**Beweislast:** [who proves what]
**Verjährung:** [status with date]
**Erfolgsaussicht:** 🟢 Hoch (70-90%) / 🟡 Mittel (40-70%) / 🔴 Gering (<40%)

[Repeat for each claim]

## Gegenrechte des Gegners
[Potential counterclaims]

## Priorisierte Empfehlung
1. [Best claim to pursue and why]
2. [Secondary claim]
3. [What to do first — Mahnschreiben? Beweissicherung? Sofort klagen?]

## ⚠️ Dringende Fristen
[Any deadlines within 30 days — Besitzstörung, Kündigungsanfechtung, etc.]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---
⚠️ Keine Rechtsberatung. Von einem Rechtsanwalt bestätigen lassen.
```
