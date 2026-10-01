---
name: prazos-cpc-bossmann007
title: /prazos-cpc
description: 'Calculadora de prazos em dias úteis (CPC art. 219 [model knowledge — verify]). Computa: feriados forenses, recesso 20/dez–20/jan (art. 220 [verify]), dobra para Fazenda/MP/Defensoria (arts. 180/183/186 [verify]), litisconsortes com procuradores distintos em autos físicos (art. 229 [verify]), suspensão/prorrogação por indisponibilidade de sistema (art. 224 §1º [verify]). Estrutura e explica o cômputo; advogado confirma tabla de feriados para seu tribunal. Parse intimação em: tipo de ato, prazo aplicável, data-limite. Scaffold, não cálculo final (attorney-confirmed only).'
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/litigation-legal/skills/prazos-cpc
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# /prazos-cpc

Prazos processuais em Brasil são contados em **dias úteis** (segunda a sexta, excluídos feriados forenses e recesso judiciário). Contar errado = morosidade processual imputada a você, ou contar para cima = prazo vencido antes da data esperada. Esta skill estrutura o cômputo — você confirma a tabela de feriados para seu tribunal (porque varia por comarca) e eu produzo a data-limite.

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → jurisdiction (comarca / tribunal).
2. Ask: is this about (a) an intimação (order/notice with a deadline), or (b) a standalone prazo calculation?
3. If intimação: parse the text → tipo de ato (petição, contestação, apelação), prazo indicado (15 dias, 30 dias), calculate deadline.
4. If prazo: intake start date, number of dias úteis, apply adjustments (dobra, suspensão, recesso).
5. Output: step-by-step calculation, clearly flagged for attorney confirmation, with note on tribunal-specific feriados table (you must confirm with the local court).

---

# Prazos Processuais — Calculation Scaffold

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (default for in-house), skip — skills use practice-level context and the matter machine is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` — jurisdiction (comarca / tribunal), phase, parties (to check if Fazenda/MP/Defensoria is a party), and any known suspensions. Write outputs to matter folder if active; otherwise to practice-level `prazos/` folder.

---

## Purpose

A missed deadline can waive a right (contestação fica inconteste, apelação é inadmitida, moção fica indeferida ex officio), prejudice your client's case, and subject you to sanctions (CPC arts. 79–81 má-fé, or Estatuto da OAB art. 34 — breach of duty). Calculating the deadline correctly is non-negotiable.

Brazilian procedure uses **dias úteis** (business days Monday–Friday, excluding court closures and holidays), with several adjustments:

1. **Feriados forenses** — national holidays, state holidays, local holidays (varies by tribunal / comarca)
2. **Recesso judiciário** — 20 Dec–20 Jan (holidays close the courts; any act served during that window gets an automatic extension when the court reopens) `[model knowledge — verify]`
3. **Dobra de prazo** — automatic doubling of deadline if the party is Fazenda (government), MP (prosecutor), or Defensoria (public defender) `[model knowledge — verify]`
4. **Litisconsortes com procuradores distintos** (co-defendants with separate lawyers in physical case files) — prazo dobra para ambos `[model knowledge — verify]`
5. **Suspensão por indisponibilidade de sistema** — if the tribunal's e-filing system (PJe, etc.) is down, the deadline is automatically extended until the system is back up, plus a reasonable time `[model knowledge — verify]`

---

## Jurisdiction assumption / Premissa de jurisdição (Brasil)

**CPC arts. 219–224** `[model knowledge — verify]` govern prazo calculation:

- **Art. 219:** Prazos são contados em dias úteis (Monday–Friday). [model knowledge — verify]
- **Art. 220:** Recesso judiciário: 20 Dec–20 Jan. Any act served during that window has the prazo extended (a automatic extension kicks in when the court reopens). `[model knowledge — verify]`
- **Art. 224:** Na contagem, exclui-se o dia do começo e inclui-se o do vencimento; o prazo só começa a correr no primeiro dia útil seguinte à publicação/intimação (art. 224, §§2º-3º). `[model knowledge — verify]`
- **Art. 224 §1º:** Se o dia do começo ou o vencimento cair em dia não útil (feriado, fim de semana, dia sem expediente), prorroga-se para o próximo dia útil. `[model knowledge — verify]`
- **Art. 231:** Fixa o termo inicial conforme o meio da intimação (carta, oficial de justiça, edital, meio eletrônico). `[model knowledge — verify]`
- **Arts. 180, 183, 186:** Fazenda Pública, MP, and Defensoria Pública get automatic doubling of prazos (dobra de prazo) — whatever prazo applies to a private party, they get 2× `[model knowledge — verify]`.
- **Art. 229:** If there are multiple defendants with separate counsel in a physical case file, the prazo for ALL defendants is extended (dobra) because not all can be served simultaneously. For electronic service (now standard), this is less commonly invoked. `[model knowledge — verify]`
- **Art. 224 §1º:** Suspensão por indisponibilidade de sistema — if PJe or other required system is down, deadlines don't run. `[model knowledge — verify]`

**Feriados forenses (varies by tribunal and state).** National holidays (Ano Novo, Tiradentes, Dia do Trabalho, Corpus Christi, Finados, Proclamação da República, Consciência Negra, Natal, etc.) are universal. But states add state-level holidays, and some comarcas add local holidays (Dia da Padroeira, etc.). This varies by TJ. **You must confirm with the local court or tribunal website which holidays apply in your specific comarca / tribunal.**

---

## Load the playbook / Load context

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → jurisdiction (comarca, tribunal), parties (is one party Fazenda/MP/Defensoria?)
- Active matter's `matter.md` — phase, parties, any known system suspensions or court closures
- Tribunal website or local rules for: feriados forenses calendar, sistem downtime notices

If `CLAUDE.md` has `[PLACEHOLDER]` for jurisdiction or parties, ask:

> Qual é o tribunal / comarca para esse prazo? E qual é a parte (Fazenda, MP, Defensoria, ou privada)? Isso determina se há dobra de prazo e qual é a tabela de feriados.

---

## Workflow

### Step 1: Intake — intimação or standalone prazo

Ask:

> **O que você quer calcular?**
>
> A. **Uma intimação (edital, aviso, ordem do juiz)** — I'll parse the text to extract: tipo de ato, prazo indicado, data-limit. Cole a intimação e eu extraio.
>
> B. **Um prazo standalone** — você sabe o prazo (15 dias, 30 dias) e a data de início. Diga: "15 dias úteis a contar de 01 de julho de 2026" e eu calculo.

---

### Step 2a: If intimação — parse and extract

If the user pastes an intimação, extract:

| Field | Example |
|---|---|
| **Tipo de ato** | "Contestação da ação [#XXXXX]" |
| **Prazo indicado** | "Prazo de 15 dias úteis" |
| **Data de referência** | "A contar da intimação" (or "intimado em 01/07/2026") |
| **Dobra?** | "Dobro para Fazenda Pública" (yes/no) |
| **Foro** | "TJSP 1ª Vara Empresarial da Capital" (or extracted from the header) |

---

### Step 2b: If standalone — intake the components

If standalone, ask:

> **Quantos dias úteis?** (P. ex., 15, 30, 90)
>
> **Data de início?** (P. ex., "01 de julho de 2026" ou "intimado em 03/07/2026, segunda-feira")
>
> **Qual é a parte / qual é o tribunal?** (Verifica se há dobra e feriados aplicáveis.)
>
> **Há suspensão ou recesso?** (P. ex., "entrego em 28 de dezembro" — aí o recesso de 20/dez–20/jan afeta. Ou "PJe estava fora do ar em [data]".)

---

### Step 3: Calculate the deadline — step-by-step

Build a **calculation table** showing each dia útil:

**Example: 15 dias úteis starting 01 July 2026, tribunal TJSP (São Paulo)**

| # | Data | Dia da semana | Útil? | Observação | Dias úteis acumulados |
|---|---|---|---|---|---|
| 0 | 01/07/2026 | Quarta | Sim | Data de início | — (conta começa no dia útil SEGUINTE) |
| 1 | 02/07/2026 | Quinta | Sim | — | 1 |
| 2 | 03/07/2026 | Sexta | Sim | — | 2 |
| 3 | 04/07/2026 | Sábado | Não | Fim de semana | — |
| 4 | 05/07/2026 | Domingo | Não | Fim de semana | — |
| 5 | 06/07/2026 | Segunda | Sim | — | 3 |
| 6 | 07/07/2026 | Terça | Sim | Feriado de Corpus Christi (TJSP)? | [check] 4 or — |
| ... | ... | ... | ... | ... | ... |
| 15 | ??/??/2026 | ??? | Sim | 15º dia útil | 15 |

**Output: "Data-limite: [DATE]"**

---

### Step 4: Apply adjustments

For each adjustment, apply in order:

**Adjustment A: Dobra de prazo (Fazenda, MP, Defensoria, or co-defendants with separate counsel)**

If applicable, double the number of dias úteis:

| Without dobra | With dobra |
|---|---|
| 15 dias úteis | 30 dias úteis |
| 30 dias úteis | 60 dias úteis |

Recalculate the table with 2× the dias úteis.

**Adjustment B: Recesso judiciário (20 Dec–20 Jan)**

CPC art. 220 **suspends the running of prazos processuais** from 20 Dec to 20 Jan (inclusive). "Suspends," not "postpones the deadline": the days inside the window simply do not count. The clock stops on 20 Dec and resumes on the first dia útil on/after 21 Jan. `[model knowledge — verify]`

- The days between 20 Dec and 20 Jan are **not counted** as dias úteis — subtract them and continue the count after reopening.
- **Filing (protocolo) is still possible during recesso**, especially electronically (PJe stays open). An act filed during recesso is **valid on the actual date it was filed** — it is NOT deemed filed on 21 Jan. What is suspended is the *running of the prazo against you*, which only helps; it never invalidates an early filing.
- Urgent measures (tutelas de urgência, plantão) are decided during recesso — recesso suspends prazos, not the court's emergency function.

Example: prazo of 15 dias úteis whose count reaches its 10th dia útil on 19 Dec 2026. The clock stops on 20 Dec; the remaining 5 dias úteis resume on the first dia útil on/after 21 Jan 2027. If the lawyer files on 08 Jan 2027 (during recesso), the filing is valid on 08 Jan — the recesso only means the deadline hadn't run out. `[model knowledge — verify]`

**Adjustment C: Suspensão por indisponibilidade de sistema**

If PJe / e-filing system is down, the deadline is automatically extended. The extension is:

- From the time the system goes down until it's restored, plus
- A "reasonable time" (usually 1–2 days) for filing after restoration. `[model knowledge — verify]`

Example: System down 10–12 July. Your prazo deadline would have been 11 July. The deadline is extended to 13 July (restoration date + 1 day). [Check the tribunal notice for the actual extension.]

**Adjustment D: Feriados forenses (tribunal-specific calendar)**

For each dia in the calculation table, check: is it a feriado forense in [tribunal]? If yes, mark it as "Não" (not useful).

National holidays (apply everywhere): Ano Novo (01/01), Tiradentes (21/04), Dia do Trabalho (01/05), Independência (07/09), Nossa Senhora Aparecida (12/10), Finados (02/11), Proclamação da República (15/11), Consciência Negra (20/11), Natal (25/12). Corpus Christi (móvel, ~maio/junho) e Sexta-feira Santa costumam ser ponto facultativo/feriado forense — confirme no calendário do tribunal. `[model knowledge — verify]`

State-level holidays (vary by TJ):
- **SP:** Corpus Christi, Dia de Zumbi (20/11), Consciência Negra (20/11 — often observed on a Friday).
- **RJ:** Diferentes — check TJRJ calendar.
- **Local holidays:** Dia da Padroeira (some comarcas), Aniversário da cidade (some), Folga compensatória (some tribunals give days off in lieu of holidays).

**No silent supplement:** If you don't know the feriados for [tribunal], flag it:

> Feriados forenses para TJSP em 2026 — não tenho a tabela oficial. Os feriados nacionais estão incorporados (Tiradentes, Dia do Trabalho, Corpus Christi, Finados, Consciência Negra, Natal). Mas TJSP pode ter feriados estaduais ou de calendário forense específicos. **Você precisa confirmar a tabela de feriados com [TJSP website] ou notificação do tribunal antes de confiar nessa data-limite.**

---

### Step 5: Output the final calculation

Present the final deadline with caveats:

```
CÔMPUTO DE PRAZO — SCAFFOLD PARA CONFIRMAÇÃO PELO ADVOGADO

Ato: Contestação da ação [#12345678]
Tribunal: TJSP — 1ª Vara Empresarial da Capital (comarca: SP Capital)
Intimado em: 01 de julho de 2026 (quarta-feira)
Prazo: 15 dias úteis
Parte: Pessoa jurídica privada (não há dobra de prazo)

Cálculo:
[Table with all dias úteis — see Step 3 above]

Feriados forenses aplicáveis (TJSP — calendário 2026):
- Tiradentes: 21/04 (segunda) ✓ (antes do prazo)
- Corpus Christi: 04/06 (quinta) ✓ (antes do prazo)
- Finados: 02/11 (segunda) ✓ (após o prazo — irrelevante)
- Consciência Negra: 20/11 (sexta) ✓ (após o prazo — irrelevante)
- Natal: 25/12 (sexta) — SEM IMPACTO (prazo vence antes do recesso)

DATA-LIMITE CALCULADA: 22 de julho de 2026 (terça-feira)

⚠️ Confirmações necessárias:
- [ ] Tabela de feriados forenses para TJSP 2026 foi conferida com o tribunal / site oficial?
- [ ] Não há suspensão de sistema (PJe indisponível) em [data do prazo]?
- [ ] A parte tem procurador único (em autos físicos), ou há dobra por litisconsortes com procuradores distintos?
- [ ] Recesso judiciário (20/dez–20/jan) afeta esse prazo? Nesse caso, simule com 20 dez como data-limite.

Se tudo confirmado: **PRAZO VENCE EM 22/07/2026.**

Se há dúvida: **Submeta com 1–2 dias de antecedência (p. ex., 20 de julho) para ter margem.**
```

---

### Step 6: Parse intimação — complete walkthrough

If the user pasted an intimação, walk through the parsing:

**Example intimação:**

```
PODER JUDICIÁRIO
Tribunal de Justiça do Estado de São Paulo
1ª Vara Empresarial da Capital — São Paulo

INTIMAÇÃO E NOTIFICAÇÃO

Processo nº 0021234-56.2024.8.26.0100
Ação: Cobrança de Duplicata
Autor: Empresa A Ltda.
Réu: Empresa B Ltda.
Juiz: [Nome]

Intimação datada de 01/07/2026 (quarta-feira)

DESPACHO:

Defiro a produção de prova pericial contábil [art. 464, CPC]. Nomeio perito Dr. João da Silva, com registro no CRC [#]. As partes têm prazo de 10 (dez) dias úteis para indicar assistentes técnicos e formular quesitos complementares.

Prazo para resposta: 15 (quinze) dias úteis.

Rua [X], São Paulo, SP
[Signature]
```

**Parse:**

| Elemento | Valor |
|---|---|
| Tipo de ato | Indicação de assistente técnico + formulação de quesitos suplementares (10 dias); Contestação / resposta (15 dias) |
| Data da intimação | 01/07/2026 |
| Tribunal | TJSP, 1ª Vara Empresarial da Capital |
| Prazos | 10 dias úteis (quesitos) + 15 dias úteis (contestação) |
| Dobra? | Não indicado — assume-se parte privada |
| Recesso? | Não afeta (prazo termina antes de 20 dez) |

**Data-límite para assistente técnico:** [10 dias úteis from 01/07 = data X]
**Data-límite para contestação:** [15 dias úteis from 01/07 = data Y]

---

## Consequential-action gate

O resultado desta skill é um **cálculo-scaffold** — a data-limite é calculada, mas **você (o advogado) deve confirmar** a tabela de feriados forenses e qualquer suspensão de sistema antes de confiar.

A responsabilidade de calcular o prazo corretamente é sua. Se você erra:
- Morosidade processual (CPC art. 369 / Código de Ética — negligência)
- Direito waivado (contestação não contestada, apelação inadmitida, etc.)
- Possível sanção sob má-fé (CPC arts. 79–81)
- Censura profissional (Estatuto da OAB, art. 34)

Essa skill reduz o risco de erro de cálculo, mas não elimina a sua obrigação de conferência.

---

## What this skill does not do

- **Não acessa o calendário forense do tribunal.** Você acessa (site do tribunal, avisos de suspensão, calendário local). Eu estruturo o cômputo; você confirma os feriados e suspensões.
- **Não monitora suspensões de sistema.** Se PJe fica fora do ar, você sabe (tribunal avisa). Eu calculo com a informação que você passa; você atualiza se houver notícia de suspensão.
- **Não conta para prazo eventual** ("se acontecer X, prazo é Y"). Eu calculo para o cenário que você descrever; se as circunstâncias mudam, recalculamos.
- **Não produz documentação da data-limite para o tribunal.** A data-limite é para você saber quando submeter. Se o tribunal pede "prova de que o ato foi feito dentro do prazo", você guarda o timestamp do e-filing ou a certidão do cartório.
- **Não substitui conferência manual.** Contar nos dedos — 01, 02, 03, [skip weekend], 06, 07 — é um backup útil. Se sua versão manual conflita com a calculadora, **pare e recount.**

---

## Relationship to other skills

- `litigation-legal:demand-draft` — se você está enviando uma demand letter com prazo para resposta, essa skill calcula o prazo para resposta.
- `litigation-legal:deposition-prep` — se uma audiência de instrução foi marcada com um prazo de pré-audiência (p. ex., 10 dias antes para apresentar rol de testemunhas), essa skill calcula.
- `litigation-legal:matter-intake` — durante a intake, prazos críticos (contestação, apelação, prescrição) são flagados; essa skill calcula as datas.

---

## Next steps decision tree

**What next? Pick one and I'll help you build it out:**

1. **Confirm feriados para o seu tribunal.** Você me dá o link do tribunal / a tabela, eu reprocess a data-limite com os feriados confirmados.
2. **Monitore uma data-limite crítica.** Você diz "meu prazo para apelação vence em [data]" — eu adiciono um reminder para você via [calendario/task list] com 5 dias de antecedência.
3. **Simule cenários.** Se houver incerteza (p. ex., "o tribunal pode dar uma extensão por [razão]?"), eu recalculo com a extensão e te mostro os dois cenários.
4. **Integre ao matter.md.** Eu adiciono a data-limite ao seu `matter.md` com um `[DEADLINE: data-limite]` tag, com link para esse cálculo.
5. **Something else** — tell me what you'd do with this.

---

*Last updated: [DATE]*
