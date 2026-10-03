# OGH Case Law Presentation Guide

> **Standard format for citing Austrian Supreme Court (OGH) and other high court decisions across all skills.**

---

## When to Include Case Law

Include OGH/VfGH/VwGH case law when:
- A legal claim depends on court interpretation (not just statute text)
- The statute is ambiguous and case law clarifies it
- The user's situation involves a contested legal doctrine
- A recent decision has changed established practice
- The user asks about litigation strategy (success probability depends on Judikatur)

Do NOT pad analysis with irrelevant case law. Only cite decisions that directly affect the user's situation.

---

## Presentation Format

### Single Decision

```markdown
**OGH [Geschäftszahl]** ([Datum])
- **Leitsatz:** [1-2 sentence holding in plain German]
- **Relevanz:** [Why this decision matters for the user's specific situation]
- **Gewicht:** Hoch / Mittel / Gering
```

### Example

```markdown
**OGH 4 Ob 87/12k** (19.06.2012)
- **Leitsatz:** Eine Vertragsstrafe von 10% des Auftragswerts ist bei einem Werkvertrag zwischen Unternehmern nicht sittenwidrig iSd §879 ABGB.
- **Relevanz:** Die vereinbarte Vertragsstrafe von 15% liegt über dem vom OGH als noch zulässig beurteilten Maß — ein Gericht könnte sie nach §1336 Abs 2 ABGB mäßigen.
- **Gewicht:** Hoch
```

---

## Grouping by Context

### In `/recht claim` — Group by Claim

```markdown
### Relevante Judikatur zu Anspruch 1: Schadenersatz nach §1295 ABGB

**OGH [GZ1]** ([Datum])
- **Leitsatz:** [...]
- **Relevanz:** Stützt den Anspruch — [warum]
- **Gewicht:** Hoch

**OGH [GZ2]** ([Datum])
- **Leitsatz:** [...]
- **Relevanz:** Mögliche Einwendung der Gegenseite — [warum]
- **Gewicht:** Mittel
```

### In `/recht strategy` — Group by Position

```markdown
### Judikaturlage zu [Streitfrage]

**Für den Kläger spricht:**
- **OGH [GZ]** ([Datum]): [Leitsatz + Relevanz]

**Für den Beklagten spricht:**
- **OGH [GZ]** ([Datum]): [Leitsatz + Relevanz]

**Uneinheitliche Linie:**
- **OGH [GZ]** ([Datum]): [Leitsatz + warum die Lage unklar ist]

**Einschätzung:** [Welche Linie überwiegt? Trend erkennbar?]
```

---

## Selection Criteria

When multiple decisions exist, select 3-5 per issue based on:

1. **Leitentscheidung** — Is this THE leading case on the issue? Always include.
2. **Verstärkter Senat / Großer Senat** — Maximum authority. Always include.
3. **Recency** — Prefer recent decisions, but don't drop classic leading cases.
4. **Factual similarity** — Does the fact pattern closely match the user's situation?
5. **Clarity** — Does the decision state a clear rule, or is it hedged/limited?

**Cap at 5 decisions per issue.** More than 5 adds noise, not signal.

Mark one as `Leitentscheidung` if it's clearly the central authority:

```markdown
**OGH [GZ]** ([Datum]) — ⭐ Leitentscheidung
```

---

## Court Hierarchy

When citing, use the correct court designation:

| Court | Abbreviation | Authority Level |
|-------|-------------|-----------------|
| Oberster Gerichtshof | OGH | Highest civil/criminal court |
| Verfassungsgerichtshof | VfGH | Constitutional court |
| Verwaltungsgerichtshof | VwGH | Highest administrative court |
| Oberlandesgericht | OLG | Appellate court |
| Landesgericht | LG | First instance (>€15.000) |
| Bezirksgericht | BG | First instance (≤€15.000) |

Only cite OGH/VfGH/VwGH as authoritative. Lower court decisions may be mentioned for illustration but carry less weight.

---

## Geschäftszahl Format

Always use the correct format:
- OGH: `[Senat] Ob [Nr]/[Jahr][Suffix]` → e.g., `4 Ob 87/12k`
- VfGH: `G [Nr]/[Jahr]` or `E [Nr]/[Jahr]` → e.g., `G 212/2021`
- VwGH: `Ra [Jahr]/[Fachgebiet]/[Nr]` → e.g., `Ra 2021/09/0123`

Never invent Geschäftszahlen. If you cannot verify a decision via RIS, do not cite it. State instead:
> "Die Judikatur zu [Thema] ist [established/evolving/unclear]. Eine RIS-Recherche wird empfohlen."

---

## Verification

All case law citations MUST follow the RIS Verification Protocol (`references/ris-protocol.md`):
- If RIS MCP is available: search by Geschäftszahl and verify
- If not available: use web fallback but flag as `OFFICIAL_WEB_VERIFIED` or `SECONDARY_SOURCE_ONLY`
- **Never cite a Geschäftszahl you cannot verify** — fabricated case citations destroy credibility
