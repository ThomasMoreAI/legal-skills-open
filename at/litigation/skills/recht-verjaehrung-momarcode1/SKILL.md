---
name: recht-verjaehrung-momarcode1
title: /recht verjaehrung — Verjährungsprüfung
description: Checks all applicable statutes of limitation (Verjährungsfristen) under Austrian law. Flags imminent deadlines, considers Hemmung and Unterbrechung.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-verjaehrung
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: litigation
language: de
---

# /recht verjaehrung — Verjährungsprüfung

When the user wants to know if their claim is still enforceable, follow these steps.

---

## Step 1: Identify the Claims

What claims does the user have (or face)? List each one.
If `/recht claim` was already run, use those results.

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 3: For Each Claim, Determine the Correct Frist

Go through this table. Find the matching row for each claim:

| Frist | Applies To | Grundlage | Starts Running When |
|-------|-----------|-----------|-------------------|
| **30 Tage** | Besitzstörungsklage | §454 ZPO | Ab Kenntnis der Störung |
| **14 Tage** | Kündigungsanfechtung (Klage bei ASG) | §105 Abs 4 ArbVG | Ab Zugang der Kündigung |
| **6 Wochen** | Entlassungsanfechtung | §106 ArbVG | Ab Zugang der Entlassung |
| **14 Tage** | Fernabsatz-Rücktritt | §11 FAGG | Ab Erhalt der Ware / Vertragsschluss (DL) |
| **2 Monate** | Mängelrüge B2B | §377 UGB | Ab Ablieferung (unverzüglich = ~14 Tage!) |
| **3 Monate** | Mietzinsüberprüfung | §16 Abs 8 MRG | Ab Mietvertragsende |
| **6 Monate** | Bereicherung aus Irrtum | §1487 ABGB | Ab Kenntnis des Irrtums |
| **1 Jahr** | Irrtumsanfechtung | §1487 ABGB | Ab Vertragsschluss |
| **2 Jahre** | Gewährleistung (beweglich) | §933 Abs 1 ABGB | Ab Übergabe/Ablieferung |
| **3 Jahre** | Allgemeine Verjährung | §1486 ABGB | Ab Fälligkeit |
| **3 Jahre** | Schadenersatz (subjektiv) | §1489 Satz 1 ABGB | Ab Kenntnis von Schaden UND Schädiger |
| **5 Jahre** | Gewährleistung (unbeweglich) | §933 Abs 1 ABGB | Ab Übergabe |
| **10 Jahre** | Bereicherung (allgemein) | §1478 ABGB analog | Ab Entstehung |
| **30 Jahre** | Schadenersatz (objektiv) | §1489 Satz 2 ABGB | Ab schädigendem Ereignis |
| **30 Jahre** | Sachenrechtliche Ansprüche | §1478 ABGB | Ab Entstehung |
| **40 Jahre** | Vorsätzliche Tötung/schwere KV | §1489 ABGB | Ab Ereignis |

**⚠️ Common traps:**
- Gewährleistung: Frist ist eine PRÄKLUSIVFRIST (Ausschlussfrist), keine Verjährungsfrist. Kein Einwand des Gerichts — Geltendmachung muss innerhalb der Frist erfolgen.
- Schadenersatz §1489: Die 3-Jahres-Frist beginnt erst, wenn der Geschädigte SOWOHL den Schaden ALS AUCH den Schädiger kennt. Kennen-Müssen genügt (grobe Fahrlässigkeit).
- B2B Rügepflicht §377 UGB: Versäumte Rüge = Verlust ALLER Gewährleistungs- und Schadenersatzansprüche wegen Mangel!

---

## Step 4: Calculate the Dates

For each claim:
1. **Fristbeginn:** When did the limitation period start?
2. **Fristende:** When does it expire?
3. **Status today:**
   - 🟢 **Offen** — More than 3 months remaining
   - 🟡 **Kritisch** — Less than 3 months remaining
   - 🔴 **Verjährt/Präkludiert** — Frist abgelaufen

---

## Step 5: Check for Hemmung or Unterbrechung

Has anything stopped or restarted the clock?

**Hemmung (clock pauses, remaining time preserved):**
- §1494 ABGB: Minderjährigkeit (until 2 years after Volljährigkeit)
- §1494 ABGB: Höhere Gewalt (force majeure)
- §1495 ABGB: Between spouses during marriage
- OGH-Judikatur: Ernsthafter Vergleichsverhandlungen (settlement negotiations) can cause Hemmung — but this is case-by-case and risky to rely on
- COVID-Sonderregelungen: Check if still applicable

**Unterbrechung (clock resets to zero):**
- Klageeinbringung (filing suit)
- Schriftliches Anerkenntnis by debtor
- Zahlung (partial payment = acknowledgment)

If any applies, recalculate the remaining time.

---

## Step 6: Present Results

```markdown
# Verjährungsprüfung

**Prüfungsdatum:** [today]

## Fristen-Übersicht
| Anspruch | Frist | Beginn | Ablauf | Verbleibend | Status |
|----------|-------|--------|--------|------------|--------|
| [claim 1] | 3 J. (§1489 ABGB) | [date] | [date] | [x] Tage | 🟢 |
| [claim 2] | 2 J. (§933 ABGB) | [date] | [date] | [x] Tage | 🟡 |
| [claim 3] | 30 T. (§454 ZPO) | [date] | [date] | ABGELAUFEN | 🔴 |

## ⚠️ DRINGENDE FRISTEN
[Any deadline within 30 days — highlight prominently]

> **SOFORT HANDELN:** [Claim X] verjährt am [date]. Sie müssen bis dahin
> Klage einreichen oder eine verjährungsunterbrechende Handlung setzen.

## Hemmung/Unterbrechung
[If any applies — explain effect on calculation]

## Empfehlung
1. [Most urgent action — e.g., "Sofort Klage einbringen wegen drohender Verjährung"]
2. [Other actions]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---
⚠️ Verjährungsfristen unbedingt von einem Rechtsanwalt bestätigen lassen.
Eine falsche Berechnung kann zum Verlust des Anspruchs führen.
```
