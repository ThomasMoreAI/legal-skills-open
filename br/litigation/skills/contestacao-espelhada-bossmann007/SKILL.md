---
name: contestacao-espelhada-bossmann007
title: 'Contestacao espelhada'
description: 'Decompõe a petição inicial (elemento por elemento, pedido por pedido, causa de pedir por causa de pedir) em uma matriz: alegação do autor → defesa possível (preliminar CPC 337 / mérito) → prova necessária → ônus. Força ônus da impugnação especificada (CPC art. 341 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm] — fato não impugnado presume-se verdadeiro). Sinaliza prescrição/decadência e preliminares. Produz scaffold de defesa, não contestação final (consequential-action gate applies).'
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/litigation-legal/skills/contestacao-espelhada
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# /contestacao-espelhada

Uma contestação bem estruturada não discute; ela mapeia. Para cada alegação do autor, você diz: (a) se é fato (impugnável) ou direito (não impugnável), (b) se está impugnando, qual é a defesa (é falso, é incompleto, é irrelevante, é prescricionário, é insuficiente), (c) que prova você tem / precisa, (d) quem tem o ônus. Esta skill constrói esse mapa — o scaffold da contestação — deixando o advogado preencher com a defesa específica do seu caso.

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → case theory (sua versão dos fatos), side (você é réu), decision posture.
2. Ask the user to paste or describe the petição inicial (or key excerpts).
3. Decompose: each causa de pedir, each pedido, flagging the factual vs. legal elements.
4. Produce: a matrix — "alegação do autor | defesa (preliminar / mérito) | prova | ônus" — with gaps and open questions marked for the attorney to fill in.

---

# Contestação Espelhada — Strategy Map

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (default for in-house), skip — skills use practice-level context and the matter machine is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` — especially your case theory (sua versão dos fatos), your side (você é réu), the jurisdiction, and the phase. Write outputs to the matter folder if active; otherwise to the practice-level `contestacoes/` folder.

---

## Purpose

A contestação (answer) is a structural document. It admits or denies each factual allegation (CPC art. 341 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]), then either rests (no defense on the merits) or mounts affirmative defenses (preliminares or mérito). The structure matters because:

- **Failing to deny a factual allegation = admission.** Art. 341 says "fato não impugnado presume-se verdadeiro" — if the author alleges "réu received the shipment on Jan. 1" and you don't deny it, the court presumes it's true. You can't later say "actually, we got it on Jan. 15" without opening yourself to a charge of surprise / lack of candor.
- **Preliminary defenses stop the case before merits (CPC art. 337).** If the author sued in the wrong forum, or there's res judicata, or the statute of limitations has run, you raise that first — it may end the case without a trial on the facts.
- **Affirmative defenses shift the burden.** Once you raise them (estoppel, laches, force majeure, release, accord and satisfaction, comparative negligence), the author has to rebut or concede. The judge doesn't award them to you automatically; you have to plead and prove them. But if you don't plead them, they're waived.
- **Ônus allocation is non-trivial.** Some defenses are on the defendant (most affirmative defenses — you have to prove comparative negligence, for example). Some shift to the plaintiff after you raise them (prescription is often on the defendant, but the plaintiff can affirmatively prove the obligation is still alive; depende). The matrix makes ônus explicit.

This skill builds the scaffold — the structure. You fill in the specifics (your facts, your evidence, your legal theories).

---

## Jurisdiction assumption / Premissa de jurisdição (Brasil)

**CPC arts. 336–353** `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]` govern contestação:
- Art. 336: Réu must file dentro do prazo (usually 15 dias úteis after service, doubled for Fazenda/MP per arts. 180/183/186 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]).
- Art. 337: Preliminary defenses (13 of them listed) can be raised in limine, in the contestação, or in certain cases at trial (depende the defense type). Common ones: lack of jurisdiction, res judicata, prescription, lack of capacity.
- Art. 341: "Fact not denied is presumed true" (presunção de verdade) — but only facts, not legal conclusions or abstract allegations.
- Art. 356: Reply (tréplica) by the plaintiff within 15 dias úteis if the defendant raises new facts in the contestação that weren't in the petition.

**Key constraint: you must be specific.** A blanket denial ("everything is false") is no defense — you must say which facts you deny, which you partially admit, which you do not know enough to admit or deny. This is called "impugnação especificada" (specified denial / rebuttal).

**Prescription & limitation periods.** If a right is prescribed or time-barred, raising prescription is a defense — it's usually on the defendant to plead and prove, but varies by obligation type. Some statute-of-limitations rules are mandatory (the judge can raise them ex officio) `[unverified: not found in primary source]`; others require a party to plead. Flag which in the matrix.

**Affirmative defenses common in contract / commercial litigation:**
- Prescription (prazo prescricional)
- Accord and satisfaction (transação, rescisão bilateral, quitação)
- Force majeure / impossibility of performance (força maior, caso fortuito)
- Breach by the other party (inadimplemento recíproco — "you breached first, so I was justified in not performing")
- Comparative negligence or fault (culpa concorrente, culpa exclusiva da vítima)
- Estoppel / waiver (venire contra factum proprium, preclusão)
- Lack of consideration (falta de causa, ou causa ilícita/imoral)

---

## Load the playbook / Load context

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → your case theory, risk calibration, decision posture, side (you're defense), core jurisdictions
- Active matter's `matter.md` — your version of events, the other side's allegations, the jurisdiction, the phase

If `CLAUDE.md` has `[PLACEHOLDER]` markers, DON'T bounce and wait — run against generic defaults (TJ padrão, critérios de defesa genéricos) **imediatamente**, tagueie `[PROVISIONAL]`, e avise uma vez no topo:

> ⚠️ Rodando contra defaults genéricos — seu perfil ainda não foi configurado. Rode `/litigation-legal:cold-start-interview` (2 min) para calibrar a estrutura de contestação ao seu estilo. Saída abaixo tagueada `[PROVISIONAL]`.

Não espere o usuário pedir — o valor aparece no primeiro run; a entrevista melhora, não desbloqueia.

---

## Workflow

### Step 1: Load the petição inicial

Ask:

> **Cole a petição inicial ou diga qual é a causa de pedir e os pedidos.** Se for um documento grande, posso ler em chunks — comece pelas primeiras 5 páginas (fatos essenciais) e vou pedindo mais conforme necessário.

If the user pastes a full petition, parse the structure:

```
[Cabeçalho / Partes]
[Causa de pedir — fatos que fundamentam o pedido]
[Fundamento jurídico — lei/contrato que sustenta o direito]
[Pedido — o que o autor quer: condenação, execução, restituição, etc.]
```

For each causa de pedir, extract:

| Fato alegado | Sou I | Fonte (prova indicada) |
|---|---|---|
| "Réu recebeu a encomenda em 01/01/2024" | Allegation | "conforme rastreamento (anexo 3)" |
| "Prazo para devolução era 30 dias" | Allegation | "conforme contrato (anexo 1, cláusula 5)" |
| "Réu não devolveu" | Allegation | — |

---

### Step 2: Fact vs. law — the initial gate

For each allegation, ask yourself (and flag in the matrix):

| Allegation | Type | Impugnable? | How to respond |
|---|---|---|---|
| "Contrato de compra e venda foi celebrado" | Fact | ✅ Yes | Admit, deny, or say "don't know" |
| "Lei 10.406/2002 (CC) art. 427 allows rescission" | Law / legal conclusion | ❌ No | Don't deny; instead, distinguish or argue the law applies differently; note that CC art. 427 addresses when a proposal binds the proponent, not rescission `[verified: https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm]` |
| "Prazo para performance was 30 dias" | Fact (what the contract said) | ✅ Yes | Admit or deny; may quote the contract |
| "Réu was negligent" | Legal characterization | ❌ No — it's shorthand for facts you deny | Counter: deny the underlying facts ("I took all reasonable care") |

**Rule:** Deny facts. On legal conclusions, either (a) don't address them (the law doesn't require you to respond to legal conclusions), or (b) affirmatively argue ("even if the court finds [fact], the law doesn't support [legal conclusion because …]").

---

### Step 3: Decompose and flag

Create a **full-record matrix** — one row per allegation, organized by causa de pedir then pedido. For each:

| # | Causa de pedir | Fato alegado | Sua posição | Tipo de defesa | Prova (sua) | Prova (author, likely) | Ônus | Flags |
|---|---|---|---|---|---|---|---|---|
| 1.1 | Celebração de contrato | "Partes celebraram contrato de venda em 01/01/2024" | Admito | Fact (yes/no) | [your evidence] | Nota fiscal, email, rastreamento | Ônus do autor de alegar; ônus seu se impugnar | — |
| 1.2 | Causa de pedir | "Preço acordado era R$ 10.000" | Admito parcialmente — preço era R$ 8.500; author inflated | Fact (quantified dispute) | Nota fiscal da venda, email citando preço | Nota fiscal do author | Ônus seu de provar o preço correto se impugna | **Precisão crítica — conflito de números** |
| 1.3 | Causa de pedir | "Prazo para devolução era 30 dias" | Nega — contrato dizia "90 dias" | Fact | Contrato (anexo 1) | — | Ônus seu se nega | **Contrato disponível — checar cláusula de prazo** |
| 2.1 | Pedido | "Condenação de réu ao pagamento de R$ 10.000" | Nega fundamentalmente — não há dano comprovado / há quitação / há prescrição | Defesa múltipla (mérito + preliminar) | Quitação (se houver), documentos de conformidade | Laudo de dano, notas de falha | Ônus seu na prescrição (levanta-la é como levanta uma defesa afirmativa); ônus do author em provar dano | **Prescrição de 5 anos (prazo comum) — data crítica: quando a obrigação nasceu?** |

---

### Step 4: Preliminares — raise them now or waive

For each preliminary defense that applies, create a row:

| # | Defesa preliminar (CPC 337) | Sua defesa | Prova | Impacto se aprovada |
|---|---|---|---|---|
| P.1 | Falta de jurisdiction / incompetência (art. 337, inciso II) `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]` | "A vara competente é a de [comarca], não essa" (CPC art. 46 — domicílio do réu) | Comprovação do seu domicílio em outra comarca | Remessa ao foro competente, conforme o caso |
| P.2 | Res judicata / coisa julgada (art. 337, inciso VII) `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]` | "Esse conflito já foi julgado em [another case, docket #]" | Cópia da sentença anterior (coisa julgada) | Extinção sem julgamento do mérito |
| P.3 | Prescrição (CPC art. 487, II — se aplicável) `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]` | "Prazo prescricional de 5 anos expirou em [date]" | Documentos que mostram quando a obrigação nasceu | Resolução de mérito por prescrição, se acolhida |

**Critical point:** Preliminares are waived if not raised in the contestação or in the first motion if the defendant chooses to file a moção to dismiss (demanda prévia) instead. After you file the contestação, you can't later say "oh, there's also a jurisdiction problem." Raise all preliminares NOW or lose them.

---

### Step 5: Mérito — identify affirmative defenses

For each affirmative defense that applies (and that isn't a preliminary), create a row:

| # | Defesa de mérito | Sua alegação | Fatos necessários para provar | Ônus | Prova (sua) |
|---|---|---|---|---|---|
| D.1 | Inadimplemento recíproco (você breached first, so my non-performance was justified) | "Author failed to [X], so I was justified in not [Y]" | (1) Author was obligated to do [X]. (2) Author failed. (3) Failure was material. (4) Author's failure released my obligation or justified my delay. | Seu ônus — você raise it, you prove it | Documentos showing author's failure |
| D.2 | Culpa exclusiva do author / comparative negligence | "Harm resulted from author's negligence, not mine" | (1) Author had a duty. (2) Author breached. (3) Breach caused the harm. (4) I exercised reasonable care / I'm not at fault. | Seu ônus — you prove comparative fault or exclusive fault of author | Documento, testimony, causation |
| D.3 | Force majeure / impossibility | "Performance was impossible due to [event beyond my control]" | (1) Event occurred. (2) Event was unforeseeable. (3) Event was beyond my control. (4) Event made performance impossible (not merely harder / more expensive). | Seu ônus — you prove the elements | Documentação of the force majeure event |
| D.4 | Quitação / Accord and satisfaction | "Author accepted [payment/performance] as full discharge" | (1) Parties agreed that [X] would discharge the obligation. (2) [X] was rendered. (3) Author accepted [X] as full discharge (not as partial / on account). | Seu ônus — you prove the agreement and acceptance | Quitação (receipt), email accepting the discharge, cancelled check |
| D.5 | Estoppel / Venire contra factum proprium | "Author's prior conduct estops them from now claiming [right]" | (1) Author engaged in conduct [Y]. (2) I relied on that conduct. (3) My reliance was reasonable. (4) Allowing author to now claim the right would cause me injustice. | Seu ônus — you prove the elements | Your reliance documents |

---

### Step 6: Build the matrix

Put it all together into a single matrix, organized:

**Section 1: Defesas preliminares**

| # | Defesa | Sua alegação | Prova | Status |
|---|---|---|---|---|
| P.1 | [preliminary] | — | — | — |

**Section 2: Facts / impugnações**

| # | Causa de pedir | Fato do author | Sua resposta | Impugna? | Tipo de impugnação | Prova (sua) | Ônus |
|---|---|---|---|---|---|---|---|
| 1 | [first cause] | [author allegation] | [admit / deny / partial] | [y/n] | [type] | [what you have] | [who bears burden] |
| 2 | [second cause] | [author allegation] | — | — | — | — | — |

**Section 3: Defesas de mérito (affirmative defenses)**

| # | Defesa | Sua alegação | Elementos necessários | Prova (sua) | Ônus |
|---|---|---|---|---|---|
| D.1 | [defense name] | — | — | — | — |

---

### Step 7: Ônus allocation — flag the critical burden calls

At the bottom, create a summary table:

| Fact / element | Ônus normal | Sua posição | Impacto |
|---|---|---|---|
| "Contract was formed" | Author (alegante) | You admit | No impact — author's burden is met |
| "Price was R$ 10K" | Author (alegante) | You deny and say R$ 8.5K | You now carry the burden of proving R$ 8.5K (because you contradict the author's allegation with specificity) |
| "Dano comprovado" | Author (alegante) | You deny and say "no proof of damages" | Author carries burden of proving damages; you just contest the evidence |
| "Prescrição ocorreu" | You (if you raise it) | — | Your burden to prove the date the obligation arose and that >5 anos has passed |
| "Force majeure" | You (if you raise it) | — | Your burden to prove all elements |

---

## Consequential-action gate

A contestação espelhada que você draftar é **work product** — é attorney-written, attorney-opinion, privileged under sigilo profissional do advogado (Estatuto da OAB, art. 7º). Once you file it in court, it becomes part of the public record.

The output of this skill is a **scaffold**, not the final contestação. You will:

1. Fill in the specifics (your facts, your evidence, your legal theories)
2. Consult with your client (they must confirm the allegations you're denying / admitting — client sign-off is essential)
3. Have the final contestação reviewed by a senior lawyer or partner before filing
4. File it in the correct court, in the correct format, within the correct deadline

**Filing a false or misleading contestação violates CPC arts. 79–81 (litigância de má-fé — bad faith litigation).** Denying a fact you know to be true, omitting an affirmative defense you could prove, or raising a defense you don't actually intend to pursue can result in sanctions (multa, indenização) against you personally or your firm.

---

## What this skill does not do

- **Não redige a contestação final.** Eu produzo o scaffold — a estrutura. Você redige o texto, com o estilo, as citações jurisprudenciais, a argumentação de mérito, etc.
- **Não substitui a conferência do cliente.** O cliente (a empresa, a pessoa) deve confirmar cada fato que você está admitindo / negando. Você não pode negar um fato que o cliente sabe que é verdadeiro.
- **Não garante que os preliminares serão acolhidos.** Se você levanta uma questão de jurisdiction / prescription / res judicata, o juiz decide. Jurisprudência local pode ter posição diferente da sua.
- **Não opina sobre qual defesa você DEVE levantar.** Às vezes, levantar uma defesa e perder prejudica você na apelação (porque você concedeu certas premissas). Às vezes, omitir uma defesa é mais estratégico. É escolha sua — eu estruturo as opções.
- **Não redige a contestação em conformidade com as práticas locais.** Alguns tribunais têm provimentos ou costumes sobre formato (índice de quesitos, estrutura de seções, linguagem de preliminares). Confirme a prática local da sua vara antes de filiar.

---

## Relationship to other skills

- `litigation-legal:claim-chart` — the elements of the author's claim (from their petition) are what you're impugning via contestação. The chart structures the case theory; contestação espelhada operationalizes your defense against that theory.
- `litigation-legal:brief-section-drafter` — once the contestação is filed and evidence is gathered, your trial brief's argument section may rely on the denials and affirmative defenses raised in the contestação.
- `litigation-legal:deposition-prep` — your cross-examination of the author's witnesses at trial will pin down the facts you denied in contestação or develop the facts underlying your affirmative defenses.

---

## Next steps decision tree

**What next? Pick one and I'll help you build it out:**

1. **Refine the matrix.** We iterate on the defenses, the ônus allocation, and the evidence you need to gather — making sure you're not waiving anything and that your burden is clear.
2. **Draft affirmative defenses.** Pick the strongest 2–3 affirmative defenses and I'll help you structure the facts and the legal theory you'll use to support them.
3. **Evidence inventory.** For each fact you're denying or each defense you're raising, let's inventory what documents / testimony / expert reports you have and what gaps remain.
4. **Escalate for client sign-off.** I'll produce a memo to your client explaining each admission / denial and each affirmative defense — they need to confirm you've got the facts right before you file.
5. **Draft the preliminary defenses section.** If you're raising jurisdiction, res judicata, or prescription, I'll draft the legal argument for that section of the contestação.
6. **Something else** — tell me what you'd do with this.

---

*Last updated: [DATE]*
