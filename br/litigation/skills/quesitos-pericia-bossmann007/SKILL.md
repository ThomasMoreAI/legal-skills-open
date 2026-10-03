---
name: quesitos-pericia-bossmann007
title: 'Quesitos pericia'
description: 'Entrevista o advogado sobre a tese e gera quesitos de perícia (CPC arts. 464-480 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]) + checklist de assistente técnico, por área (médica, contábil, engenharia, grafotécnica, ambiental). Quesito ruim = perícia perdida. Inclui guidance para quesitos suplementares e impugnação ao laudo.'
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/litigation-legal/skills/quesitos-pericia
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# /quesitos-pericia

Perícia técnica (ou perícia contábil, médica, etc.) é a terceira voz em um litígio — a do perito, um terceiro neutro (em princípio) designado pelo juiz. Os quesitos que você formular para o perito **determinam o escopo da perícia**. Quesito ruim = perícia que não responde à pergunta que importa, ou responde de um jeito que a outra parte explora facilmente. Esta skill ajuda você a formular quesitos agudos e a estruturar a resposta do perito via assistente técnico.

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → case theory, pivot fact.
2. Ask the user which expert domain (médica, contábil, engenharia, grafotécnica, ambiental, outro).
3. Interview: What is the thesis? What is the pivot fact that the expert can establish? What evidence / testing / calculation does the expert need to do?
4. Produce: A set of quesitos (organized, numbered, gated by admissibility under CPC 464-480), assistente técnico checklist, and guidance for supplemental questions and impeaching the expert's final report.

---

# Quesitos Periciais — Interview & Structure

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (default for in-house), skip — skills use practice-level context and the matter machine is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` — especially case theory, side, and the phase. Write outputs to the matter folder if a matter is active; otherwise to the practice-level `quesitos-pericia/` folder.

---

## Purpose

Quesitos periciais set the frame for what the expert will investigate and opine on. A poorly framed quesito:
- Asks for a legal conclusion rather than technical clarification (CPC art. 464, § 1º lets the judge deny expert evidence when proof of the fact does not depend on special technical knowledge, is unnecessary in view of other evidence, or is impracticable) `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]`
- Is ambiguous (expert interprets it their way, not yours)
- Omits the logical sequence (expert skips steps, making it hard for the judge to follow the reasoning)
- Opens the door to a crushing counter-opinion (because you didn't ask the right follow-up)

Good quesitos are **nested, specific, sequenced, and tied to the case theory.** This skill helps you build them.

---

## Jurisdiction assumption / Premissa de jurisdição (Brasil)

**CPC arts. 464–480** `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]` govern perícia in Brazilian civil procedure:
- Art. 464: The expert is appointed by the judge (on motion of a party or ex officio) and owes a duty of impartiality to the court, not to the parties. The expert's report is a deposition to the judge, not advocacy.
- Arts. 465–468: Appointment procedure, conflict of interest, challenge of the expert.
- Arts. 469–472: The expert produces a written report (laudo pericial). The parties may name assistentes técnicos (party-retained experts) to critique the laudo and propose counter-opinion.
- Arts. 473–480: Examination of the expert and assistentes at the audiência de instrução (trial or evidence hearing), including cross-examination.

**Key constraint: quesito must ask for fact, not legal conclusion.** Art. 464, parágrafo único says the expert opines on "fact regarding science, art, or trade" — the judge will then apply law to that fact. A quesito that says "the defendant is liable for damages" violates this — it's asking the expert for a legal conclusion. A quesito that says "what is the causal relationship between [fact A] and [fact B]" is fine — it's asking for expert fact.

**Regional variation:** Some TJs and specialized chambers (varas de saúde, varas de engenharia) have local guidelines or standard quesito formats. If your jurisdiction is SP, RJ, or a specialized channel, flag whether you know of one.

---

## Load the playbook / Load context

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → case theory, pivot fact, side (plaintiff / defendant)
- Active matter's `matter.md` — the thesis, the phase, the jurisdiction (comarca / tribunal)
- `references/quesito-templates-by-area.md` if it exists in this skill's directory (baseline quesito language by expert domain)

If `CLAUDE.md` has `[PLACEHOLDER]` markers, DON'T bounce and wait — run against generic defaults (TJ padrão, quesitos genéricos por área) **imediatamente**, tagueie `[PROVISIONAL]`, e avise uma vez no topo:

> ⚠️ Rodando contra defaults genéricos — seu perfil ainda não foi configurado. Rode `/litigation-legal:cold-start-interview` (2 min) para calibrar a estrutura de quesitos ao seu estilo. Saída abaixo tagueada `[PROVISIONAL]`.

Não espere o usuário pedir — o valor aparece no primeiro run; a entrevista melhora, não desbloqueia.

---

## Workflow

### Step 1: Area and domain selection

Ask:

> **Qual é a área de perícia?**
>
> 1. **Médica** — lesões corporais, nexo causal lesão/acidente, invalidez permanente, capacidade laborativa.
> 2. **Contábil** — apropriação indébita, desvio de valores, análise de fluxo de caixa, reconstrução de livros.
> 3. **Engenharia** — defeito construtivo, vício de obra, inadequação do projeto, responsabilidade pelo dano material.
> 4. **Grafotécnica** — autenticidade de assinatura, autoria de documento.
> 5. **Ambiental** — dano ambiental, conformidade com legislação ambiental, recuperação de área.
> 6. **Outro** — (telemetria, paisagismo, aviação, marítima, etc.) — diga qual.

This determines the template, the domain-specific quesito language, and the assistente técnico checklist.

---

### Step 2: Intake — the thesis and the pivot fact

Ask:

> **Qual é sua tese nesse litígio?** (Uma frase — p. ex., "o réu construiu a obra fora de especificação, causando infiltração e dano estrutural" ou "o laboratório forneceu diagnóstico errado, retardando o tratamento e agravando a lesão.")

> **Qual é o pivô — o fato que a perícia DEVE estabelecer para você ganhar?** (P. ex., "que a infiltração é causada por um defeito específico no projeto / na execução, não por uso inadequado." Ou: "que há nexo causal entre o diagnóstico tardio e o agravamento da doença.")

> **Você é autor ou réu?** Se réu: "Você está disputando a causa ou o quantum?" Se ambos, ambos.

> **Qual é a evidência atual que você TEM?** (Documentos, fotos, testes, diagnósticos iniciais, testemunhos — o que o perito terá disponível para trabalhar?)

> **Qual é a evidência que você NÃO TEM, mas que a perícia pode PRODUZIR?** (P. ex., "o juiz ordenou que o perito teste a resistência da estrutura", ou "o perito pode revisar o projeto original e o as-built".)

---

### Step 3: Branch by area and build the quesito structure

For each domain, outline:

**A. Foundational quesitos (the "what" and "why")**

These are the uncontroversial fact-gathering questions. They establish the baseline:

**Example for engenharia (building defect):**

| # | Quesito | Type | Why it matters |
|---|---|---|---|
| 1 | Qual é a composição material das paredes / da fundação / da cobertura na unidade do autor? | Fact-finding | Baseline — establish the construction materials |
| 2 | O projeto executivo especificava [particular specification]? Se sim, transcrevam o trecho. | Document review | Lock in the contractual spec vs. the as-built |
| 3 | Qual é o estado atual de [structure] conforme vistoria do perito em [data]? (Descrição técnica, com fotos.) | Observation | Document the damage |

**B. Causal quesitos (the "did X cause Y")**

These ask the expert to establish the causal chain:

| # | Quesito | Type | Why it matters |
|---|---|---|---|
| 4 | A composição material efetiva [actual materials] ATENDE aos requisitos técnicos da NBR [número] `[unverified: not found in primary source]`? Se não, descrever o desvio. | Standard compliance | Is there a defect by code? |
| 5 | Qual é a causa técnica da infiltração / dano / falha observada? Descrever o mecanismo. | Root cause | Nail down causation |
| 6 | A causa identificada decorre de (a) erro no projeto / na execução, (b) vício de material, ou (c) uso inadequado / falta de manutenção? | Attribution | Who is at fault? |

**C. Quantum quesitos (if you're litigating damages)**

| # | Quesito | Type | Why it matters |
|---|---|---|---|
| 7 | Qual é o custo de reparação / mitigação da falha para restaurar [condition]? Detalhar o escopo de trabalho e o orçamento. | Damages | Lock in the repair cost |
| 8 | Há dano estrutural adicional causado pela infiltração / falha? Se sim, descrever e estimar custo. | Consequential harm | Secondary damages |

**Example for medicina (injury causation):**

| # | Quesito | Type | Why it matters |
|---|---|---|---|
| 1 | Qual foi a lesão inicial sofrida pela vítima no acidente de [data e local]? | Baseline | Establish the injury |
| 2 | Qual é o diagnóstico atual da lesão, conforme exame pericial em [data]? | Current state | What is the damage now? |
| 3 | Há nexo causal entre a lesão inicial e o estado atual? | Causation | Did the injury cause the current condition? |
| 4 | A vítima perdeu permanentemente capacidade laborativa? Se parcial, qual é o percentual? | Quantum | Economic impact |
| 5 | O atraso no tratamento (de [data] a [data]) agravou a lesão? Se sim, descrever o agravamento. | Contributory fact | Did procedural delay matter? |

---

### Step 4: Admissibility gate — check CPC art. 464

Before finalizing, screen each quesito:

| Quesito | Admissible? | Fix if not |
|---|---|---|
| "O réu é responsável pelos danos?" | ❌ No — legal conclusion | Rephrase: "Qual é o mecanismo causal entre [ato] e [dano]?" |
| "Qual é a composição material da estrutura conforme vistoria?" | ✅ Yes — fact | Keep |
| "Qual é a negligência do réu?" | ❌ No — characterization of culpability | Rephrase: "O projeto / execução desviou da norma técnica [NBR / standard]? Se sim, em que aspecto?" |
| "É tecnicamente possível que [X] causou [Y]?" | ✅ Yes — factual possibility | Keep |

**Rule of thumb:** If the quesito can be answered without the expert opining on "what the law means," it's admissible. If the expert has to read a statute, interpret contract language, or conclude "therefore liable," that's legal — strike it.

---

### Step 5: Sequence and number the quesitos

Organize them in a logical flow:

1. **Background / baseline** (what is the physical state, what is the document, what is the standard)
2. **Observation / measurement** (what did the expert find when they inspected / tested / analyzed)
3. **Comparison** (how does the actual state differ from the spec / from the standard / from the normal)
4. **Causation** (what caused the difference)
5. **Attribution** (who is responsible for the cause — design error, execution error, material defect, user error, act of God)
6. **Quantum** (what is the cost of remediation / the extent of damage)
7. **Supplemental** (are there other related facts the expert should address)

**Numbering:** Use a decimal structure — 1, 1.1, 1.2 (sub-questions under the main question) — or just 1, 2, 3, … if linear. Parties will refer to "quesito 3.2" in their assistente técnico responses, so stability matters.

---

### Step 6: Assistente técnico checklist

When you name an assistente técnico (your party's expert counterpart), they will review the perito's laudo and file a written response (parecer técnico) `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]`. Prepare them for:

**Pre-laudo tasks:**
- [ ] Review the quesitos you (the party's lawyer) formulated — confirm they're tight and not waivable.
- [ ] Gather all documentary evidence the perito will see (contracts, specs, invoices, photos, prior evaluations, emails). Organize by relevance.
- [ ] If it's a complex case, commission a preliminary expert review BEFORE the perito is appointed — that way you know what the perito will find and can prepare counter-arguments.
- [ ] Identify the assigned perito (usually published by the judge ~2 weeks after appointment order). Research their track record — have they written reports in similar cases? Do they have a published tendency (if case law / jurisprudência indexes this)?

**Post-laudo tasks:**
- [ ] Read the laudo in full. Flag every statement that seems:
  - Factually wrong (perito misread a document, miscalculated, misunderstood the baseline)
  - Incomplete (perito didn't answer a quesito, or answered with "insufficient information" when info was available)
  - Subjective (perito's "opinion" on something that should be factual)
  - Self-interested (does the perito have a financial stake in the outcome, e.g., the perito is from a company that would benefit from their own conclusion)
- [ ] For each flag, prepare a written response (parecer técnico) with:
  - The specific passage from the laudo
  - Your expert's critique (fact-based, with citations to documents the perito had / should have reviewed)
  - An alternative fact / calculation
- [ ] If the laudo is deeply flawed on a pivot point, consider requesting new expert examination under art. 480 when the matter is not sufficiently clarified; supplemental quesitos are governed by art. 469 during the diligence. `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]`

---

### Step 7: Supplemental quesitos and impeachment

**CPC art. 480** `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]` allows the judge to determine, ex officio or on a party's request, a new expert examination (nova perícia) when the matter was not sufficiently clarified. For supplemental quesitos, use CPC art. 469 during the diligence. Draft any follow-up with the same rigor as the originals — it may be your last chance to reframe an unfavorable finding.

**Common impeachment angles:**

| Scenario | Impeachment quesito |
|---|---|
| Perito says "insufficient data to opine" | "What specific data or testing would be necessary to reach a conclusion? If that data is available, can the perito access it?" Pins the perito down on excuses. |
| Perito's calculation has a step that seems wrong | "In calculating [quantity], did the perito consider [variable]? If not, why not? If yes, what value did they assign?" Forces the perito to explain, and the explanation (or non-explanation) becomes part of the record. |
| Perito relied on a source that is itself disputed | "The perito based their opinion on [document]. Is that document authentic? Is it the current version? [Show conflicting version if you have one.]" Undercuts the foundation. |
| Perito's standard is outdated | "The perito applied NBR XXXX / standard YYYY dated [year]. Has that standard been superseded? If so, what does the current standard require?" If the perito used old law / old standard, you've got a credibility problem for them. |

---

## Consequential-action gate

Quesitos that you formulate are submitted to the court (usually in response to the judge's order to produce perícia). They become **part of the judicial record** — they're official notice to the other party of what you're asking the expert to find.

Once quesitos are filed:
- The other party will file their own quesitos, often contradicting yours ("investigate whether the plaintiff's claim is exaggerated," etc.)
- The judge will synthesize or choose between the sets
- The perito is bound by the final quesitos that the judge approves

**Your quesitos are evidence of your case theory.** If your quesitos are sloppy, ambiguous, or omit critical facts, the judge reads that as weakness. If they're tight and specific, the judge reads that as confidence and precision.

**The output of this skill — your drafted quesitos — is work product.** It's attorney-written, attorney-specific, and privilege-able under sigilo profissional do advogado (Estatuto da OAB, art. 7º, inciso II). Once you file them in court, they become part of the public record (if the case is open court) or privileged (if sealed). Store them in your privileged matter folder, mark them as work product, and make the filing decision deliberately.

---

## What this skill does not do

- **Não executa a perícia.** Você contrata o perito ou o juiz designa. Esta skill estrutura as perguntas; o perito as responde.
- **Não opina sobre o laudo.** Quando o perito retorna com o laudo, a assistente técnico (ou você, consultando a sua assessora técnica) critica. Esta skill ajuda a formular a resposta, mas não a faz.
- **Não substitui um expert real em sua equipe.** Se você tem um engenheiro / médico / contador / grafotécnico interno, envolva-o ao usar esta skill — ele / ela conhece os gaps, sabe o que a perícia pode produzir, e pode refinar os quesitos com jargão técnico certo.
- **Não garante que a perícia vai favorecer você.** Quesitos bem-formulados aumentam a chance de que a perícia seja clara e útil — mas não determinam o resultado. A perícia pode concluir contra você.
- **Não dispensa conformidade com CPC 464–480.** Se a sua jurisdição tem jurisprudência ou provimentos locais sobre formato, admissibilidade, ou sequência de quesitos, confirme que os quesitos estão em conformidade antes de filiar.

---

## Relationship to other skills

- `litigation-legal:claim-chart` — the elements of your case (from claim-chart) are often what the perícia needs to establish. "Quesitos periciais" makes those elements operationalized for the expert.
- `litigation-legal:deposition-prep` — the assistente técnico's cross-examination of the perito at trial uses the same techniques as deposition prep. A tight quesito becomes a tight cross-examination question.
- `litigation-legal:brief-section-drafter` — your trial brief's factual section often relies on the laudo (if favorable) or the parecer técnico (if you're attacking the laudo). Quesitos periciais frame that factual narrative.

---

## Next steps decision tree

**What next? Pick one and I'll help you build it out:**

1. **Refine the quesitos.** You bring back your initial draft, I'll tighten language, flag admissibility issues, and re-sequence for maximum clarity.
2. **Draft assistente técnico guidelines.** I'll produce a checklist and a template for what your technical expert should watch for in the perito's laudo, and how to structure a parecer técnico rebuttal.
3. **Research perito tendencies.** If you know the assigned perito's name, I can help you research their track record (prior laudos, jurisprudência citing their work, any flagged credibility issues in case law). This informs your assistente técnico's critique strategy.
4. **Escalate for specialist review.** Your engineer / accountant / doctor should review these quesitos and provide domain-specific language. I can produce a memo to brief them on what you're trying to establish and what you need from them.
5. **Something else** — tell me what you'd do with this.

---

*Last updated: [DATE]*
