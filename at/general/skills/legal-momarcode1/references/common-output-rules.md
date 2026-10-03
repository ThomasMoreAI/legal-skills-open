# Common Output Rules

> **Standards that apply to ALL skill outputs.** Every skill should follow these rules for consistency across the Austrian Legal Skill.

---

## Language Rules

1. **Match the user's language** — German input → German output. English input → English output.
2. **Statutes always in German form** — §922 ABGB, not "Section 922 Civil Code"
3. **Court names in German** — OGH, not "Supreme Court"; BG, not "District Court"
4. **Legal terms with German original** — "statute of limitations (Verjährung)", "warranty (Gewährleistung)"
5. **Austrian German, not German German** — Gewährleistung not Mängelrecht, Schadenersatz not Schadensersatz, Vertragsstrafe stays Vertragsstrafe

---

## Citation Rules

1. **Always cite specific §§** — Never "Austrian law says..." without the exact section
2. **Include Absatz and Ziffer when relevant** — §6 Abs 1 Z 9 KSchG, not just "§6 KSchG"
3. **Use "idF" for amended versions** — §922 ABGB idF BGBl I 2025/xxx
4. **Cite the correct law** — ABGB for civil, KSchG for consumer, UGB for commercial, MRG for tenancy
5. **Never cite German BGB, Swiss OR, or US law** as Austrian law

---

## Risk Level Icons

Use consistently across all skills:

| Icon | Level | German | Meaning |
|------|-------|--------|---------|
| 🔴 | Critical | Kritisch | Mandatory law violation, void/voidable, uncapped liability |
| 🟡 | Important | Wichtig | Deviates from market standard, one-sided, significant risk |
| 🟢 | Standard | Standard | Normal Austrian practice, acceptable |

---

## Formulierungsvorschläge

Every risk finding (🔴 and 🟡) MUST include:

1. **Problem statement** — what's wrong, in one sentence
2. **Legal basis** — §§ citation
3. **Formulierungsvorschlag** — actual replacement text in proper Austrian legal German, copy-paste ready
4. **Verhandelbarkeit** — Hoch / Mittel / Gering
5. **Fallback** — alternative if primary proposal is rejected

Never just say "this clause is problematic" without providing replacement text.

---

## Quellenstatus Block

**Every output MUST include this block** before the disclaimer:

```markdown
## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | [connection status] |
| Gesetze | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |
```

If ALL citations are unverified, add:
```markdown
⚠️ **RIS nicht verfügbar.** Alle zitierten Normen basieren auf Trainingsdaten. Aktualität bitte selbst auf [ris.bka.gv.at](https://www.ris.bka.gv.at) prüfen.
```

---

## Disclaimer

**Every output MUST end with:**

```markdown
---
⚠️ **Keine Rechtsberatung.** Diese Analyse dient der rechtlichen Ersteinschätzung und ersetzt nicht die Beratung durch einen Rechtsanwalt.
```

For English outputs:
```markdown
---
⚠️ **Not legal advice.** This analysis is for informational purposes only and does not replace consultation with a licensed Austrian attorney (Rechtsanwalt).
```

---

## Report Structure

All skill outputs should follow this general order:

1. **Header** — document name, type, user's party, date
2. **Score/Summary** — overall score or key finding (if applicable)
3. **Sofort-Warnungen** — immediate warnings (void clauses, mandatory law violations) — only if present
4. **Dashboard/Overview** — risk counts, compliance summary, cost overview (if applicable)
5. **Detailed Analysis** — the core analysis section (varies by skill)
6. **Recommendations** — prioritized action items with Formulierungsvorschläge
7. **Nächste Schritte** — concrete next steps for the user
8. **Quellenstatus** — RIS verification status
9. **Disclaimer** — Keine Rechtsberatung

---

## Formatting Standards

- Use markdown tables for structured data
- Use headers (##, ###) for sections — never go deeper than ####
- Use bold for emphasis, not ALL CAPS
- Use `code blocks` for statute references in running text only when needed for clarity
- Use blockquotes (>) for Formulierungsvorschläge (replacement text)
- Number action items and recommendations
- Use checkboxes (- [ ]) for next steps

---

## Quality Gates

Before presenting output, verify:

- [ ] Every §§ citation includes the law name (not just "§922" but "§922 ABGB")
- [ ] Every 🔴 and 🟡 finding has a Formulierungsvorschlag
- [ ] No German BGB/Swiss OR/US law cited as Austrian
- [ ] Quellenstatus block is present
- [ ] Disclaimer is present
- [ ] Language matches user's input language
- [ ] No Geschäftszahlen cited without verification status
