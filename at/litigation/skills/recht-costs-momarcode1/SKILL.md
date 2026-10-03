---
name: recht-costs-momarcode1
title: /recht costs — Kostenrechner
description: Calculates Austrian court fees (GGG) and attorney fees (RATG) for any Streitwert. Full cost/risk matrix including Sachverständigengebühren and Prozessrisiko.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-costs
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: litigation
language: de
sources:
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht costs — Kostenrechner

When the user asks about litigation costs, follow these steps.

---

## Step 1: Determine the Streitwert

The Streitwert controls everything — court fees, attorney fees, jurisdiction.

If the user provides a number, use it. If not, help them calculate:
- **Geldforderung** → the claimed amount
- **Räumungsklage** → Jahresmietzins (§58 JN)
- **Feststellungsklage** → economic interest of the declaration
- **Arbeitsrecht** → often the Monatsentgelt × relevant factor

Ask if unclear:
> "Wie hoch ist der Streitwert (die eingeklagte Summe)? Das bestimmt die Kosten."

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 3: Look Up GGG Gerichtsgebühr

Use this table. Find the row matching the Streitwert:

| Streitwert | Pauschalgebühr 1. Instanz |
|------------|--------------------------|
| bis €150 | €26 |
| €150–€300 | €53 |
| €300–€700 | €79 |
| €700–€2.000 | €132 |
| €2.000–€3.500 | €186 |
| €3.500–€7.000 | €335 |
| €7.000–€35.000 | €743 |
| €35.000–€70.000 | €1.459 |
| €70.000–€140.000 | €2.919 |
| €140.000–€210.000 | €4.295 |
| €210.000–€280.000 | €5.672 |
| €280.000–€350.000 | €7.049 |
| über €350.000 | 1,2% + €2.849 |

**Special cases:**
- Mahnverfahren (Zahlungsbefehl): halbe Pauschalgebühr
- Berufung: volle Pauschalgebühr again
- Arbeitsrecht 1. Instanz: gebührenbefreit (ASGG)
- Außerstreitverfahren: eigene Gebührenordnung

⚠️ Warn user: "Diese Sätze können sich ändern. Aktuelle Sätze auf ris.bka.gv.at prüfen."

---

## Step 4: Estimate RATG Attorney Fees

RATG fees depend on Streitwert and Tarifpost (TP). Calculate:

1. **Determine the Bemessungsgrundlage** — the Streitwert
2. **Look up TP 3A** (for Klage, Klagebeantwortung, Tagsatzung) — this is the base rate
3. **Add Einheitssatz:**
   - BG: +60% (covers letters, phone, copies)
   - LG: +80%
4. **Multiply by expected number of Leistungen:**
   - Klage: 1× TP 3A
   - Klagebeantwortung: 1× TP 3A
   - Each Tagsatzung: 1× TP 3A
   - Typical case: 3-5 Leistungen

Provide a **range**, not a single number. Typical:
- Streitwert €5.000–€15.000 → RA-Kosten ca. €2.000–€5.000
- Streitwert €15.000–€50.000 → RA-Kosten ca. €4.000–€10.000
- Streitwert €50.000–€150.000 → RA-Kosten ca. €8.000–€20.000

Note: Many Austrian lawyers charge Honorarvereinbarung (agreed fees) instead of RATG. RATG is the minimum for Kostenersatz from the losing party.

---

## Step 5: Estimate Additional Costs

Consider:
- **Sachverständigengebühren:** If technical questions → €2.000–€10.000+ depending on complexity
- **Dolmetscherkosten:** If foreign-language documents or parties
- **Reisekosten:** If witnesses must travel
- **Pauschalgebühr Berufung:** Same as 1. Instanz if appeal is likely

---

## Step 6: Calculate Scenarios

Build the cost/risk matrix:

**Scenario A: 100% Obsiegen (Win)**
- User pays: GGG (refunded via Kostenersatz) + own RA temporarily
- Net cost: Minimal (user gets Kostenersatz per §41 ZPO)

**Scenario B: 100% Unterliegen (Loss)**
- User pays: GGG + own RA + opponent's RA (RATG) + SV-Gebühren
- This is the maximum financial risk

**Scenario C: 50% Teilobsiegen (Partial Win)**
- Costs split proportionally per §43 ZPO
- Often the most realistic scenario

**Scenario D: Vergleich (Settlement)**
- Each side typically bears own costs (unless agreed otherwise)
- No SV costs if settled before Beweisaufnahme

---

## Step 7: Present Results

```markdown
# Kostenabschätzung

**Streitwert:** €[amount]
**Zuständiges Gericht:** [BG/LG] (Streitwert [≤/>] €15.000)
**Verfahrensart:** [Streitig / Mahnverfahren]

## Kostenaufstellung
| Posten | Betrag |
|--------|--------|
| Gerichtsgebühr (GGG) | €[x] |
| Eigene Anwaltskosten (RATG-Basis) | €[range] |
| Gegnerische Anwaltskosten (bei Unterliegen) | €[range] |
| Sachverständigengebühren (falls nötig) | €[range] |

## Kostenszenarien
| Szenario | Wahrscheinl. | Ihre Kosten (netto) |
|----------|-------------|-------------------|
| 100% Obsiegen | [x]% | €[x] (Kostenersatz!) |
| 75% Obsiegen | [x]% | €[x] |
| 50% Obsiegen | [x]% | €[x] |
| Unterliegen | [x]% | €[x] |
| Vergleich | [x]% | €[x] |
| **Erwartungswert** | | **€[weighted]** |

## 💡 Mahnverfahren möglich?
[If Geldforderung ≤ €75.000: "Ja — Zahlungsbefehl beantragen. Halbe Gebühr (€[x]). Wenn kein Einspruch → vollstreckbar in 4 Wochen."]

## 💡 Verfahrenshilfe möglich?
[If user might qualify: "Bei geringem Einkommen: Verfahrenshilfe per §§63ff ZPO beantragen. Befreiung von GGG und RA-Kosten."]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---
⚠️ Gebührensätze ohne Gewähr. Aktuelle Sätze auf ris.bka.gv.at prüfen.
```
