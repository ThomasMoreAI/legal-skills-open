# RNE — National Business Register (Tunisia)

## What it is

The **RNE** (*Registre National des Entreprises*) is the official Tunisian register that centralizes company registrations. It was created by **Law 2018-52**, which unified the older commercial registers. Every business — patente, SUARL, SARL — must be registered here.

[REQUIRES MANUAL LEGAL VERIFICATION: exact Law 2018-52 number + later amendments — confirm in the JORT]

URLs:
- registre-entreprises.tn (public portal)
- rne.tn (variant seen in the wild)

[REQUIRES MANUAL LEGAL VERIFICATION: confirm the canonical RNE URL in force in 2026]

## Types of RNE registrations

| Type | Underlying legal status | Indicative timing |
|---|---|---|
| Trader individual | Patente | 1–3 days |
| SUARL | Single-shareholder commercial company | 5–15 days |
| SARL | Multi-shareholder commercial company | 7–21 days |
| SA / SCA / others | Depending on status | Variable |

## Documents required for a SUARL

[src: proservy.com/creation-dentreprise/suarl + RNE — confirm against the up-to-date 2026 list]

1. **Articles of association** drafted in French — 3 signed original copies (template in `statuts-suarl-clauses.md`).
2. **Investment declaration** (if applicable, API form).
3. **Capital blocking certificate** issued by the depositary Tunisian bank.
4. **National ID card** of the sole shareholder (certified copy).
5. **Proof of registered office:**
   - Commercial lease, OR
   - Property title, OR
   - Domiciliation contract with a licensed domiciliation company.
6. **Receipt for setup fees** (fiscal stamp + RNE fees).
7. **RNE registration form** fully filled in (the local equivalent of a Cerfa).
8. **Declaration of existence** with the relevant BCI (Bureau de Contrôle des Impôts).
9. **JORT publication** of an incorporation notice (legal insertion).

## Documents required for a patente (individual)

1. Certified copy of **national ID card**.
2. **Proof of activity domiciliation** (lease / property / domiciliation contract).
3. **RNE registration form for individuals**.
4. **Declaration of existence** with the relevant BCI.
5. **Tax ID card** (matricule fiscal, issued when the declaration of existence is filed).
6. **Specific authorization** if the activity is regulated (e.g. medical, legal, security).

## Indicative costs

[REQUIRES MANUAL LEGAL VERIFICATION: 2026 RNE pricing]

| Item | Patente (TND) | SUARL (TND) |
|---|---|---|
| RNE registration | 70–150 | 100–200 |
| Fiscal stamp on declaration | 30 | 30–50 |
| JORT publication | 0 | 200–300 |
| Notary / expert-accountant fees (if outsourced) | 0–200 | 500–1 500 |
| **Approximate total** | **~100–380** | **~830–2 050** |

## RNE clerk friction points — how to prevent them

[From Phase 2 OSINT — freelancer anxieties]

### Friction #1 — Insufficiently justified domiciliation
- **Cause:** informal lease, sworn statement, residential address not clearly separated from professional.
- **Prevention:** commercial lease registered with the tax receivership, OR domiciliation contract with a licensed company.

### Friction #2 — Non-compliant articles of association
- **Cause:** ambiguous clauses, capital not clearly paid in, object clause too vague or outside the nomenclature.
- **Prevention:** use the template in `statuts-suarl-clauses.md`, which follows the canonical CSC requirements.

### Friction #3 — Tax ID still pending
- **Cause:** the BCI declaration of existence must come before or alongside the RNE filing.
- **Prevention:** file the declaration of existence in parallel with the RNE procedure — the matricule typically arrives within 1–3 days.

### Friction #4 — Capital not paid in correctly
- **Cause:** "1/3 paid in" wording poorly documented, bank certificate with missing exact wording.
- **Prevention:** ask the bank for a **blocking certificate** stating the exact amount, currency, and a "to be released upon RNE registration" clause.

### Friction #5 — Regulated activity not checked
- **Cause:** the object clause implicitly covers an activity needing a license (e.g. IT services for the medical sector).
- **Prevention:** draft a precise object clause and explicitly exclude regulated activities if you are not licensed.

## Step-by-step procedure (SUARL)

```
D-7   : Pick a firm / expert-accountant / notary (or DIY) + company name
D-5   : Reserve the name with the RNE (non-similarity certificate)
D-3   : Draft articles + open the bank account + deposit capital
D0    : File the complete dossier with the RNE (online or in person)
        File the declaration of existence with the BCI
D+3   : Receive the tax ID
D+5-15: Receive the RNE extract (Tunisian Kbis equivalent)
D+10  : JORT publication
D+15  : Manager CNSS affiliation
D+20  : Operational bank accounts activated
```

## Legal basis

- **Law 2018-52:** creation of the RNE [REQUIRES VERIFICATION: exact number + promulgation date]
- **Application decree:** registration procedures [REQUIRES VERIFICATION]
- **Code des Sociétés Commerciales** (Law 2000-93, as amended): articles on SUARL / SARL → see `code-societes.md`

## Sources

- `data/sources.json` → `rne-portail`, `proservy-suarl`, `proservy-patente`
- `code-societes.md` (underlying legal framework)
- `statuts-suarl-clauses.md` (ready-to-use template)
