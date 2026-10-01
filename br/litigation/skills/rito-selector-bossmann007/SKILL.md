---
name: rito-selector-bossmann007
title: /rito-selector
description: 'Decision tree para "qual rito/procedimento para meu caso": juizado especial cível (Lei 9.099/1995, até 40 SM, até 20 SM sem advogado [verified: https://www.planalto.gov.br/ccivil_03/leis/l9099.htm]), juizado especial da Fazenda (Lei 12.153/2009 [verified: https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/lei/l12153.htm]), procedimento comum (CPC), ação monitória (CPC arts. 700-702 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]), execução de título extrajudicial (CPC art. 784 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]), tutela de urgência/evidência (CPC arts. 300/311 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]). Interview do usuário → recomenda rito + sinaliza requisitos + aponta template. Inclui skeleton breve por rito.'
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/litigation-legal/skills/rito-selector
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# /rito-selector

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, decision posture, jurisdiction.
2. If matter workspaces enabled, confirm or select active matter; load `matter.md`.
3. Interview user on: claim value, party types, dispute category, jurisdiction.
4. Apply decision tree to recommend procedure.
5. Flag key requirements (jurisdiction, value limits, mandatory representation, etc.).
6. Offer template skeleton for recommended procedure.

---

# Rito — Seletor de Procedimento

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗`, skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` — parties, dispute category, jurisdiction. Write outputs to the matter's `case-analysis/` folder if a matter is active; otherwise the practice-level `case-analysis/` folder.

---

## Purpose

Before drafting a complaint, you need to know which procedure controls. A contract dispute for R$ 50,000 between two companies is not a juizado especial cível case — it's a procedimento comum in the normal courts. A consumer dispute for R$ 5,000 with a clear debt document can run through a monitória. This skill asks the facts and recommends the procedure.

---

## Jurisdiction assumption / Premissa de jurisdição (Brasil)

Brazilian civil procedure offers multiple tracks:

**Value / jurisdiction gatekeepers:**
- **Juizado Especial Cível** (Lei 9.099/1995 [verified: https://www.planalto.gov.br/ccivil_03/leis/l9099.htm]) — up to 40 salários mínimos (SM). Natural persons and microenterprises (ME) can sue/defend without a lawyer up to 20 SM; above 20 SM but below 40 SM, lawyer is mandatory.
- **Juizado Especial da Fazenda Pública** (Lei 12.153/2009 [verified: https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/lei/l12153.htm]) — disputes with government up to 60 SM. Above 60 SM, goes to common procedure.
- **Procedimento Comum** (CPC arts. 318-369 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]) — unbounded value. Used for all disputes above juizado ceilings, disputes involving corporations, and disputes involving certain matters (family, estate, property title) even if value is low.
- **Ação Monitória** (CPC arts. 700-702 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]) — applies when you have written evidence without executory-title force; the CPC provision does not set a 100 SM cap. Faster if defendant doesn't object. `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]`
- **Execução de Título Extrajudicial** (CPC art. 784 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]) — applies when you have final judgment, negotiable instrument, mortgage, or other executory title. Skip litigation; go straight to enforcement.
- **Tutela de Urgência** (CPC arts. 300-310 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]) / **Tutela da Evidência** (CPC art. 311 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]) — interim relief, not standalone. Available within any main action. Tutela de urgência: irreparable harm. Tutela da evidência: claim is so clear that withholding relief is unjust.

**Special procedure gatekeepers (not covered in full here; skill flags and refers):**
- **Property disputes** — CPC art. 282 § único specifies procedures for real property disputes. If your dispute involves real property, flag and refer to specialist.
- **Family matters** — separate codes. Not covered; route to specialist.
- **Labor disputes** — Justiça do Trabalho, specialized. Not covered; route to specialist.

**Mandatory representation [verified: https://www.planalto.gov.br/ccivil_03/leis/l9099.htm]:**
- **Natural person in common procedure:** Lawyer mandatory unless value < 20 SM.
- **Corporation:** Always requires lawyer.
- **Government:** Always represented by Attorney General or public defender.
- **ME up to 20 SM in juizado:** Can appear without lawyer if owner in person.

---

## Load the playbook / Load context

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, decision posture, jurisdiction.
- Active matter's `matter.md` — parties, jurisdiction, claim description.

---

## Workflow

### Step 1: Interview

Ask the user:

> **Qual tipo de caso?**
>
> 1. **Valor (aproximado) da ação:** Claim value in R$ (or in SM if easier)?
>
> 2. **Partes:** You are [plaintiff | defendant]? The other party is [natural person | ME/EPP | corporation | government]? Multiple parties on either side?
>
> 3. **Natureza:** Contract breach? Consumer? Property/real estate? Loan/debt? Other?
>
> 4. **Documentação:** Do you have a court judgment (título executivo judicial), promissory note, invoice, check, contract, mortgage, or other executory title?
>
> 5. **Urgência:** Is delay unacceptable? Would delay cause irreparable harm? Is the claim so obvious that waiting is unjust?

### Step 2: Decision tree

Apply the tree below. Cite every gate.

---

### DECISION TREE

```
START: "Which procedure fits my case?"

├─ Do you have an EXECUTORY TITLE (prior judgment, promissory note, 
│  negotiable instrument, mortgage, sales contract)?
│  └─ YES → EXECUÇÃO DE TÍTULO EXTRAJUDICIAL (CPC art. 784)
│
│  └─ NO → proceed
│
├─ Are you suing / being sued BY THE GOVERNMENT?
│  └─ YES → Value > 60 SM?
│           ├─ YES → Procedimento Comum
│           └─ NO → Juizado Especial da Fazenda Pública
│
│  └─ NO → proceed
│
├─ Is this FAMILY, SUCCESSION, EMPLOYMENT, IP, or PROPERTY-TITLE 
│  dispute?
│  └─ YES → [Specialist procedure required. Refer to specialist.]
│
│  └─ NO → proceed
│
├─ MONITÓRIA CANDIDATE? Liquidated, undisputed debt (documented) 
│  AND value ≤ 100 SM.
│  └─ YES → AÇÃO MONITÓRIA (CPC arts. 700-702)
│
│  └─ NO → proceed
│
├─ Do you need INTERIM RELIEF (prevent construction, freeze assets, 
│  preserve evidence, or claim is so clear that withholding relief 
│  is unjust)?
│  └─ YES → [TUTELA DE URGÊNCIA or TUTELA DA EVIDÊNCIA — supplement 
│           to main procedure.]
│         Proceed to choose main procedure below.
│
│  └─ NO → proceed
│
├─ CLAIM VALUE ≤ 40 SM AND all parties natural persons or ME?
│  └─ YES → JUIZADO ESPECIAL CÍVEL (Lei 9.099/1995)
│
│  └─ NO → PROCEDIMENTO COMUM (CPC arts. 318-369)

```

---

### Step 3: Key requirements per procedure

| Procedure | Value limit | Parties | Representation | Timeline (rough) | Filing court |
|---|---|---|---|---|---|
| **Juizado Especial Cível** | ≤ 40 SM | Natural persons, ME/EPP only | None if ≤ 20 SM; mandatory if 20–40 SM | 6 mo–2 yr | Domicílio or tort situs |
| **Juizado Especial Fazenda** | ≤ 60 SM | Government only | Same as Cível | 6 mo–2 yr | Capital or county |
| **Ação Monitória** | ≤ 100 SM [verify] | Any (liquidated debt) | Mandatory for corporations | 1–3 mo (no objection); then common if objected | Domicílio of defendant |
| **Execução Título** | Unlimited | Any (with executory title) | Mandatory for corporations | 3 mo–2 yr | Domicílio of defendant |
| **Procedimento Comum** | Unlimited | Any | Mandatory for corporations | 2–4 yr | Domicílio or special forum |
| **Tutela de Urgência** | Supplementary | Any | Same as main | Hours–days | Same as main |
| **Tutela da Evidência** | Supplementary | Any | Same as main | Hours–days | Same as main |

---

### Step 4: Representation / jurisdictional checks

1. **Representation barrier:** Corporation or large business defendant? Lawyer mandatory. Government as party? Government attorney mandatory.
2. **Value in SM:** Confirm current SM value (updates periodically). Verify claim fits the ceiling for recommended procedure.
3. **Jurisdiction:** Domicílio of defendant is default (CPC art. 46). Special forum may apply (property → forum of property; alimony → creditor's home). Parties can elect forum in contracts (CPC art. 63) but not in consumer contracts.

---

## Template skeletons per procedure

### A. Juizado Especial Cível (Lei 9.099/1995)

```markdown
## Juizado Especial Cível — Petição Inicial (Skeleton)

[HEADER — work product]

**JUIZADO ESPECIAL CÍVEL**
Comarca: [county]
Juizado: [specific juizado]

**PETIÇÃO INICIAL**

Autor(a): [name], [ID], [address]
Réu(é): [name], [ID], [address]

### I. Fatos

[Narrative of facts. Keep it concise.]

### II. Fundamentos Jurídicos

[Applicable law(s). E.g., "breach of contract under Código Civil art. 389" or "CDC art. 6º".]

### III. Pedido

[What you seek. E.g., "condemnation to pay R$ [amount] plus interest and fine".]

### IV. Valor da Causa

R$ [amount]. [Breakout: principal + interest to filing date.]

Respectfully submitted,

[Signature]
[Name, ID]
[Address]
[Contact]
```

### B. Ação Monitória (CPC arts. 700-702)

```markdown
## Ação Monitória — Petição Inicial (Skeleton)

[HEADER — work product]

**AÇÃO MONITÓRIA**
Tribunal: [Justiça Estadual / Justiça Federal]
Comarca: [county]
Vara Cível: [specific court]

**PETIÇÃO INICIAL**

Credor(a) [Petitioner]: [name], [ID], [address]
Devedor(a) [Defendant]: [name], [ID], [address]

### I. Fatos

[Brief narrative: how did debt arise? When? Documentary proof?]

### II. Fundamentos Jurídicos

[CPC art. 700 — ação monitória. Type of evidence: nota, cheque, contrato, recibo, etc.]

### III. Pedido

["Condemnation of defendant to pay R$ [amount], or if defendant objects, proceed as common procedure."]

### IV. Prova Documental

[Attach the document evidencing debt: invoice, promissory note, bank statement, check, contract, receipt.]

### V. Valor da Causa

R$ [value]. [Breakout: principal, interest accrued to filing date.]

Respectfully submitted,

[Signature]
[Name, ID]
[Address]
[Contact]
```

### C. Procedimento Comum (CPC arts. 318–369)

```markdown
## Procedimento Comum — Petição Inicial (Skeleton)

[HEADER — work product]

**AÇÃO [Description — Breach of Contract / Damages / etc.]**
Tribunal: [Justiça Estadual / Justiça Federal]
Comarca: [county]
Vara Cível: [specific court]

**PETIÇÃO INICIAL**

Autor(a): [name], [ID], [address]
Réu(é): [name], [ID], [address]
Advogado(a) do(a) Autor(a): [name], OAB [state] [number]

### I. Fatos

[Detailed narrative: dates, parties, what was promised, what happened, how damaged, damages amount.]

### II. Fundamentos Jurídicos

[Applicable law. E.g., CC art. 389 (breach); CC arts. 927, 942 (damages); CDC art. 6º (consumer); etc.]

### III. Pedido

[What you seek: condemnation to pay, specific performance, declaratory relief, etc.]

### IV. Valor da Causa

R$ [amount]. [Breakout.]

### V. Documentos

[Attach all evidence: contract, emails, invoices, receipts, expert reports, declarations, etc.]

Respectfully submitted,

[Signature]
[Name, Advogado OAB]
[Address]
[Contact]
```

### D. Execução de Título Extrajudicial (CPC art. 784)

```markdown
## Execução de Título Extrajudicial (Skeleton)

[HEADER — work product]

**EXECUÇÃO DE TÍTULO EXTRAJUDICIAL**
Tribunal: [Court]
Comarca: [county — of defendant's domicile per CPC art. 783]
Vara de Execução: [specific execution court]

**PETIÇÃO INICIAL**

Exeqüente [Creditor]: [name], [ID]
Executado(a) [Debtor]: [name], [ID], [address]
Advogado(a) do(a) Exeqüente: [name], OAB [state] [number]

### I. Fatos

[Brief: I have a title to execute. Debt is R$ [amount]. Due on [date]. No payment made.]

### II. Fundamentos Jurídicos

[CPC art. 784 — execution of extrajudicial title. Title is [type], evidencing debt of R$ [amount].]

### III. Pedido

["Execution of the attached title, with attachment of assets (penhora) and coercive measures up to judicial sale (leilão)."]

### IV. Título Executivo

[Attach original or certified copy of: judgment, promissory note, negotiable instrument, mortgage, or other title.]

### V. Cálculo da Dívida

Principal: R$ [amount]
Interest to [filing date]: R$ [amount]
Penalties / fees (if any): R$ [amount]
**Total: R$ [due]**

Respectfully submitted,

[Signature]
[Name, Advogado OAB]
[Address]
[Contact]
```

---

## No silent supplement

If facts described require a special procedure (property, family, labor, IP) outside this skill's scope, explicitly flag and route:

> "Your case involves [family/property/labor/IP] matters with specialized procedures under [specific code]. Consult a specialist in [area] to confirm the right procedure."

---

## Consequential-action gate

**Who's using this?** If Role is Non-lawyer:

> This analysis recommends a procedure based on facts you described. Before filing, a licensed attorney in your jurisdiction should review your dispute, confirm the procedure fits, and review local rules (regimento interno) for the filing tribunal. This recommendation is not legal advice; it is a framework for attorney review.
>
> Take this recommendation and facts to an attorney for confirmation.

---

## What this skill does not do

- **It does not draft complaints.** Template skeletons are outlines; actual complaints require facts, law, and evidence specific to your case.
- **It does not handle special procedures.** Family, succession, labor, IP, property-title disputes have their own codes — this skill routes those to specialists.
- **It does not account for local-rule variations.** Every tribunal (TJ, TRF) has its own regimento interno, provimentos, practices. Before filing, confirm with local rules and outside counsel.
- **It does not guarantee success.** Choosing the right procedure is necessary, not sufficient. A well-pleaded case in the right procedure can still lose on merits.
- **It does not calculate SM values in real time.** Before filing, confirm current minimum wage and whether your claim value fits the recommended procedure's ceiling.
