---
name: prescricao-decadencia-bossmann007
title: /prescricao-decadencia
description: 'Entrevista sobre fatos da causa → matriz de prazos prescricionais e decadenciais aplicáveis por verba. Output por reivindicação: prazo, termo inicial (actio nata), causas interruptivas/suspensivas, status (corrente/prescrito/a vencer). Scaffold + flags para advogado confirmar; não é opinião legal. Use quando o usuário pede "monta o quadro de prescrição" ou "quais são os prazos prescritivos para cada verba".'
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/litigation-legal/skills/prescricao-decadencia
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# /prescricao-decadencia

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → jurisdição, cabeçalho work product.
2. Entrevista: fatos da causa, data do evento danoso/contrato/delito, data da ação/demanda, prazos já vencidos?
3. Estruture matriz com: verba/reivindicação, prazo legal, termo inicial (actio nata), eventos interruptivos (ação, confissão, reconhecimento), suspensivos (incapacidade, mora do credor).
4. Output = markdown table + CSV com status (corrente, prescrito, aviso — a vencer em X dias).
5. Heavy disclaimer: prazos mudam por jurisprudência — advogado confirma e calcula datas exatas.

---

# Matriz de Prescrição e Decadência

## Matter context

Prescrição extingue ação (não direito material); decadência extingue direito (não ação). A confusão entre as duas é a armadilha mais comum. Esta skill estrutura os prazos — advogado calcula as datas e valida contra jurisprudência recente.

---

## Purpose

Montar uma **matriz de prazos prescritivos** que o advogado preenche com:
- Para cada **verba / reivindicação** da causa: qual é o prazo legal (10 anos geral, 5 anos especiais, bienal/quinquenal trabalhista, 5 anos CDC, etc.)
- **Termo inicial (actio nata):** quando começou a correr o prazo? (data da lesão, data do vencimento do contrato, data da entrega do produto defeituoso, data do ato delituoso, etc.)
- **Causas interruptivas:** o que interrompe a prescrição (ação, confissão, reconhecimento, protesto) e reinicia a contagem
- **Causas suspensivas:** o que paralisa o prazo sem reiniciar (incapacidade legal, mora do credor, impossibilidade material)
- **Status:** prazo corrente (X dias restantes), prescrito (Y dias passados desde o vencimento), ou aviso crítico (vence em 30 dias)

**Output:** markdown table + CSV com cada reivindicação + prazo + termo inicial + eventos + data de vencimento. Sem cálculos de data, só scaffolding. Advogado confirma datas e jurisprudência recente.

---

## Jurisdiction assumption / Premissa de jurisdição (Brasil)

- **Prescrição (extinção da ação, não do direito):** CC arts. 205-206 (prescrição) + CC arts. 202-203 (causas interruptivas/suspensivas) `[model knowledge — verify]`
- **Decadência (extinção do direito):** CC arts. 207-209 — mais rara, aplica-se a prazos de exercício de direitos potestivos (p.ex., rescisão contratual, anulabilidade de negócio jurídico, revogação de doação) `[model knowledge — verify]`
- **Prescrição geral (residual):** 10 anos (CC art. 205, caput) — só quando a lei não fixa prazo menor `[model knowledge — verify]`
- **Prescrições especiais (CC art. 206):** os prazos abaixo são os do rol; confira o § e inciso na fonte antes de usar `[model knowledge — verify]`:
  - **1 ano** (§1º): hospedagem, alimentos fornecidos, segurado/segurador, tabeliães/serventuários
  - **3 anos** (§3º): aluguéis; juros/dividendos; ressarcimento de enriquecimento sem causa; **reparação civil (inc. V)** — extracontratual e contratual
  - **5 anos** (§5º): dívidas líquidas de instrumento público/particular (inc. I); honorários; vencedor contra vencido por custas
  - Não confundir com **decadência** de 2 anos da **ação rescisória** (CPC art. 975 — é decadência, não prescrição do art. 206) [model knowledge — verify]
- **Prescrição trabalhista:** CF art. 7º, XXIX + CLT art. 11 — 5 anos na **constância do vínculo**, limitado a 2 anos **após a extinção do vínculo** (Súmula 308 TST para a quinquenal) `[model knowledge — verify]`
- **Prescrição CDC:** Lei 8.078/1990 art. 26 (decadência — 30 dias produto/serviço não durável, 90 dias durável, do vício aparente; oculto conta da evidência) e art. 27 (prescrição — 5 anos, fato do produto/serviço) `[model knowledge — verify]`
- **Prescrição tributária:** CTN art. 173 (decadência — 5 anos para constituir/lançar); CTN art. 150 §4º (homologação — 5 anos); CTN art. 174 (prescrição — 5 anos para cobrar o crédito já constituído) `[model knowledge — verify]`
- **Causas interruptivas (CC art. 202):** ação judicial, confissão da dívida, reconhecimento de responsabilidade, protesto `[model knowledge — verify]`
- **Causas impeditivas/suspensivas (CC arts. 197-201):** ex. entre cônjuges na constância do casamento, contra incapazes (art. 198, I), pendência de condição/prazo. **Atenção: art. 203 trata de QUEM pode interromper, não de causa suspensiva** `[model knowledge — verify]`

---

## Load context

Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → decision posture, work-product header.

If `[PLACEHOLDER]` appears, suggest `/litigation-legal:cold-start-interview` (2 minutes).

---

## Workflow

### Step 1: Triage da causa

Antes de estruturar, confirme:

- **Causa é trabalhista, cível, tributária, ou consumidor?** (Regime de prescrição diferente para cada)
- **Qual é a reivindicação principal?** (Salário não pago, indenização por dano, lucros cessantes, dívida contratual, defeito de produto, delito, etc.)
- **Qual é a data de origem?** (Data da demissão, data da lesão, data do vencimento da dívida, data do fornecimento do produto, data do ato delituoso, etc.)
- **Houve ações, confissões, reconhecimentos, ou contatos de cobrança que possam ter interrompido o prazo?** (Ação anterior, confissão de dívida, e-mail de cobrança, protesto, etc.)
- **Há incapacidade legal ou impossibilidade material que suspenda o prazo?** (Menoridade, alienação mental, impossibilidade de agir, morte durante execução, etc.)

Confirme cada antes de estruturar — datas erradas propagam por toda matriz.

### Step 2: Estrutura de reivindicação

Para cada **verba / reivindicação**, abre-se uma FILA na matriz com colunas:

| Verba / Reivindicação | Regime | Prazo | Termo Inicial (Actio Nata) | Data Efetiva do Início | Eventos Interruptivos | Eventos Suspensivos | Data de Vencimento | Status |
|---|---|---|---|---|---|---|---|---|
| [Nome da verba] | [CLT / CC / CDC / CTN] | [10 anos / 5 anos / 2 anos / 30 dias, etc.] | [Lei/jurisprudência] | [DD.MM.YYYY] | [Ação em DD.MM.YYYY; Confissão em DD.MM.YYYY; ...] | [Incapacidade; Impossibilidade; ...] | [DD.MM.YYYY] | Corrente / Prescrito / A vencer em X dias |

---

#### Reivindicações Trabalhistas (CF art. 7º, XXIX + CLT art. 11 / Súmula 308 TST)

**Regra geral:** 5 anos na **constância do vínculo** (durante o trabalho), limitado a 2 anos **após a extinção do vínculo** (após rescisão).

**Aplicação prática:**
- **Salário, 13º, férias não pagos:** prazo é 5 anos se o vínculo ainda existe (pode cobrar atraso de até 5 anos passados — quinquenal, Súmula 308 TST). Após a rescisão, ajuizamento deve ocorrer em até 2 anos da data da rescisão (bienal, CF art. 7º XXIX) `[model knowledge — verify]`.
- **FGTS não recolhido:** 5 anos durante vínculo, 2 anos após. Lei 8.036/1990 art. 23 pode ter prazos especiais — flag para advogado.
- **Dano moral trabalhista:** CC arts. 186, 927 (prescrição geral 10 anos) OU CLT prazo especial? Jurisprudência em conflito — **flag como incerto** `[model knowledge — verify]`.
- **Horas extras:** 2 anos da rescisão se já rescindido; 5 anos se vínculo ativo.
- **Aviso prévio indenizado:** 2 anos da rescisão.
- **Rescisão indireta / estabilidade:** regra pode diferir — flag para advogado.

**Termo inicial:** data da rescisão do vínculo (para pós-vínculo). Para crédito durante vínculo, cada mês vencido é um termo inicial separado (aplicação de prescrição progressiva/parcial).

**Causas interruptivas:** ação judicial (protesto, demanda), confissão de dívida, reconhecimento de responsabilidade, contato de cobrança (exigindo dívida) — cada interrupção reinicia a contagem.

**Causas suspensivas:** incapacidade legal do reclamante (menoridade, alienação mental), impossibilidade de agir (morte durante execução), mora do credor (se credor deixa de cobrar, prazo não para — não há suspensão por inação).

---

#### Reivindicações Cíveis — Responsabilidade Civil (CC art. 206 §3º V + arts. 202-203)

**Regra que mais erra na prática:** reparação civil **não** prescreve em 10 anos. Os 10 anos do art. 205 são **residuais** — só quando nenhum prazo menor se aplica. [model knowledge — verify]

**Prazos do art. 206 (confirme § e inciso na fonte):**
- **3 anos (§3º):** **reparação civil — inciso V** (extracontratual E contratual, entendimento hoje predominante); aluguéis (inc. I); juros/dividendos (inc. III); ressarcimento por enriquecimento sem causa (inc. IV) `[model knowledge — verify]`.
- **1 ano (§1º):** hospedagem; alimentos fornecidos; segurado contra segurador (e vice-versa); tabeliães/serventuários. **Não** há prazo de 1 ano para possessórias (isso é "força nova"/ano-e-dia do CPC art. 558 — instituto diverso) `[model knowledge — verify]`.
- **5 anos (§5º):** dívidas líquidas de instrumento (inc. I); honorários (inc. II) `[model knowledge — verify]`.

**Decadência que costuma ser confundida:** ação **rescisória** = 2 anos (CPC art. 975 — decadência); anulação de negócio jurídico por vício = 4 anos (CC art. 178).

**Aplicação a dano material / lucros cessantes / dano moral:**
- **Dano material (emergente / lucros cessantes) e dano moral por ato ilícito:** CC art. 206, **§3º V** — **3 anos**, salvo lei especial (CDC: 5 anos, art. 27; Fazenda: 5 anos, Dec. 20.910/1932) `[model knowledge — verify]`.

**Termo inicial (actio nata):** data em que a pretensão nasce — regra geral, data da lesão; teoria da actio nata em sentido subjetivo (STJ): conta da ciência inequívoca do dano e de sua autoria (relevante em dano oculto/continuado) `[model knowledge — verify]`. Confirme o marco no caso concreto.

**Causas interruptivas:** ação judicial (protesto, denúncia, demanda), confissão da dívida, reconhecimento de responsabilidade (escrito), protesto contra responsabilidade.

**Causas suspensivas:** incapacidade legal (menoridade, alienação mental do lesado), impossibilidade material (morte durante execução testamentária, desaparecimento da pessoa, etc.).

---

#### Reivindicações Cíveis — Responsabilidade Contratual (CC arts. 389-475)

**Prescrição para cobranças contratuais:**
- **Dívida de compra e venda / contrato de prestação:** 10 anos (prescrição geral, CC art. 205) se não houver lei especial `[model knowledge — verify]`.
- **Dívida de aluguel:** 5 anos (CC art. 206, I, "b") `[model knowledge — verify]`.
- **Dívida de mútuo (empréstimo em dinheiro):** 10 anos (prescrição geral); se contrato mostra vencimento, 10 anos contados do vencimento.
- **Cláusula penal:** prazo o mesmo da obrigação principal (CC art. 410) `[model knowledge — verify]`.
- **Lucros cessantes / resolução do contrato:** 10 anos (prescrição geral) ou 5 anos especiais se aplicável (depende da verba — flag para advogado).

**Termo inicial:** data do vencimento da obrigação (prazo contratual ou data de execução acertada).

**Causas interruptivas:** ação judicial, confissão da dívida, reconhecimento escrito de responsabilidade, protesto.

**Causas suspensivas:** incapacidade legal, impossibilidade material.

---

#### Reivindicações Consumidor (Lei 8.078/1990 arts. 26-27)

**Lei 8.078/1990 — Código de Defesa do Consumidor:**

- **Art. 26 — Decadência (extinção do direito do consumidor):**  [model knowledge — verify]
  - **30 dias** (produto/serviço **não durável**) / **90 dias** (produto/serviço **durável**) para reclamar do vício aparente ou de fácil constatação — contados da entrega efetiva (art. 26, I-II) `[model knowledge — verify]`.
  - Vício **oculto**: o prazo (30 ou 90 dias, conforme durabilidade) conta-se do momento em que ficar evidenciado o defeito (art. 26, §3º) `[model knowledge — verify]`.
  - **Importante:** Decadência extingue o DIREITO (não apenas a ação) — após 30 dias, consumidor não pode reclamar de vício (não há ação rescisória ou reparação).

- **Art. 27 — Prescrição:** 5 anos (contados da lesão) para ações de responsabilidade por produto defeituoso ou serviço inadequado (reparação, substituição, indenização) `[model knowledge — verify]`.

**Aplicação:**
- **Vício de produto (aparente):** 30 dias para devolver/trocar; se não feito, direito de reparação decai. **MAS** se há dano à pessoa/patrimônio, ação por dano (art. 27) prescreve em 5 anos a partir da lesão. [model knowledge — verify]
- **Vício oculto:** 30 dias desde a descoberta para reclamar do vício; se descobrir após 30 dias, decadência consumada — mas ação por dano ainda corre (5 anos desde lesão).
- **Responsabilidade por defeito (vício que causa dano):** prescrição de 5 anos para ação de indenização.

**Termo inicial (decadência art. 26):** data da aquisição (vício aparente) ou data da descoberta (vício oculto) — data inicial é **descoberta**, não consumo.

**Termo inicial (prescrição art. 27):** data do evento danoso (quando a lesão se produziu).

**Causas interruptivas:** ação judicial, confissão, reconhecimento.

**Causas suspensivas:** incapacidade legal, impossibilidade material.

---

#### Reivindicações Tributárias (CTN arts. 150, 173-175)

**CTN art. 173 — Decadência (direito de constituir/lançar o crédito):** [model knowledge — verify]
- Prazo de **5 anos** para a Fazenda **constituir o crédito** pelo lançamento, contados do **1º dia do exercício seguinte** àquele em que o lançamento poderia ter sido efetuado (art. 173, I) `[model knowledge — verify]`.

**CTN art. 150, §4º — Decadência no lançamento por homologação:**
- **5 anos** a contar do **fato gerador**; findo o prazo sem manifestação da Fazenda, considera-se homologado. Ressalva de dolo, fraude ou simulação `[model knowledge — verify]`.

**CTN art. 174 — Prescrição (cobrança do crédito já constituído):**
- Crédito **já lançado** prescreve em **5 anos** contados da constituição definitiva; interrompida por despacho que ordena a citação em execução fiscal, protesto judicial, ato de constituição em mora, reconhecimento do débito (art. 174, p.u.) `[model knowledge — verify]`.

**CTN art. 151 — Suspensão da exigibilidade:** moratória, depósito integral, reclamação/recurso administrativo, liminar/tutela, parcelamento `[model knowledge — verify]`. *(CTN art. 175 trata de EXCLUSÃO do crédito — isenção e anistia — não de suspensão.)*

---

### Step 3: Matriz com scaffold e flags

Exemplo de estrutura CSV pronta para preenchimento:

```csv
Verba/Reivindicação,Regime,Prazo,Termo Inicial (Actio Nata),Data Efetiva Início,Eventos Interruptivos,Eventos Suspensivos,Data Vencimento (DD.MM.YYYY),Status,Notas
Salário janeiro/2020,CLT,2 anos pós-rescisão,Data da rescisão (Súmula 161 TST),01.02.2022,Ação ajuizada em 15.05.2023 (reinicia contagem desde essa data),Nenhum,01.02.2024,Prescrito — venceu 01.02.2024,Ação ajuizada APÓS vencimento — prescrição já consumada. Reivindica valor prescrito. Flag para confirmar data exata de ajuizamento com autos.
Horas extras 2020-2021,CLT,2 anos pós-rescisão,Data da rescisão,01.02.2022,Ação em 15.05.2023 (se dentro do prazo; se não; prescrito),Nenhum,01.02.2024,Prescrito ou Corrente (depende de data exata ação),Confirmar data exata da ação nos autos.
13º 2021,CLT,2 anos pós-rescisão,Data da rescisão,01.02.2022,Ação em 15.05.2023,Nenhum,01.02.2024,Prescrito,Idem acima.
Dano moral trabalho,CLT,? (10 anos CC art. 205 vs. 5 anos CC art. 206 III vs. prazo CLT especial),Data da lesão (quando ocorrida discriminação/assédio),Indefinido,Indefinido,Nenhum,Indefinido,INCERTO — Flag crítico,Jurisprudência em conflito: STF/STJ não unificou se prescrição é 5 ou 10 anos para dano moral trabalhista. Tema 905 STJ aborda termo inicial de juros (não prescrição direta). Advogado deve pesquisar Tema mais recente ou posição do tribunal competente (TRT regional).
FGTS não recolhido,CLT,5 anos na constância / 2 anos pós-rescisão,Data da rescisão (para pós-vínculo),01.02.2022,Confissão de débito em 10.03.2024 (interrompe; reinicia contagem),Nenhum,01.02.2024 (ou 10.03.2024 + 2 anos = 10.03.2026 se confissão válida),Corrente se confissão válida; prescrito se confissão não reconhecida,Exigir cópia de confissão; validar se reconhecimento válido conforme CC art. 202 I b.
Indenização dano material (civil RCC),CC,5 anos (art. 206 III),Data da lesão / evento danoso,01.01.2020,Ação ajuizada em 15.05.2023 (reinicia contagem),Nenhum,01.01.2025,Prescrito — venceu 01.01.2025,Ação ajuizada 15.05.2023 — após prescrição (01.01.2025 = 5 anos). Prescrição já consumada.
Lucros cessantes,CC,5 anos (art. 206 III),Data do evento danoso / rescisão contratual,01.01.2020,Ação ajuizada em 15.05.2023,Nenhum,01.01.2025,Prescrito,Idem dano material.
Dano moral (civil),CC,? (5 vs. 10 anos),Data da lesão,Indefinido,Ação em 15.05.2023,Nenhum,Indefinido,INCERTO — Flag crítico,Conflito jurisprudência: 5 anos (CC art. 206 III) ou 10 anos (CC art. 205 geral)? Tema 905 STJ aborda termo inicial (não prescrição per se). Flag para advogado pesquisar posição da corte competente.
Dívida contratual (compra/venda),CC,10 anos (prescrição geral CC art. 205),Data do vencimento da obrigação,01.06.2014,Nenhum,Nenhum,01.06.2024,Prescrito — venceu 01.06.2024,Prescrito há [data atual - 01.06.2024 = X meses/anos].
Aluguel (dívida),CC,5 anos (CC art. 206 I b),Data do vencimento de cada mês,Múltiplas (cada mês),Ação em 15.05.2023,Nenhum,Última cota vence em 01.06.2024,Status depende de quanto tempo passado — se ação 15.05.2023 interrompe, reinicia contagem,Contabilizar cada mês de aluguel separadamente (prescrição progressiva).
Defeito de produto (CDC),CDC,30 dias para vício aparente (decadência) ou 5 anos para dano (prescrição art. 27),Vício aparente: data da compra; Vício oculto: data da descoberta; Dano: data do evento,01.03.2023 (compra) / 01.09.2023 (descoberta),Reclamação de vício em 15.04.2023 (dentro dos 30 dias — não decai),Nenhum,01.04.2023 (30 dias desde 01.03.2023),Aviso crítico — prazo curto (30 dias) expira em X dias,Decadência é extinção do DIREITO — após 30 dias, não há reparação por vício. MAS se há dano (lesão), ação de indenização (art. 27) prescreve em 5 anos desde lesão.
Débito tributário (lançado),CTN,5 anos (CTN art. 173),Data do vencimento do tributo,01.01.2020,Nenhum,Moratória concedida em 01.06.2023 — suspende prazo,01.01.2025 (ou estendido se moratória ativa),Depende de status moratória,Se moratória ativa, prazo suspenso — reinicia quando moratória vencer.
```

---

## Consequential-action gate

Uma matriz de prescrição errada vira perda de direitos. Erro de um dia em um prazo bienal (2 anos) é perda total — não há rescisão de prescrição consumada (é ato de força maior na execução das obrigações).

**Check Role:**
- **Lawyer:** proceda — este é draft de análise.
- **Non-lawyer:** "Uma matriz de prescrição deve ser revista e validada por advogado OAB antes de qualquer ação, recurso, ou cálculo de prazos críticos. Prescrição perdida é direito perdido — não cabe rescisão ou moção posterior."

**Antes de usar para decisão:**
- Advogado valida data efetiva de início (actio nata) — data da lesão, rescisão, vencimento, descoberta (para vício oculto), etc.
- Advogado valida eventos interruptivos (ação anterior, confissão, reconhecimento) com cópias dos autos/documentos — confissão deve ser válida conforme CC art. 202, I, "b" (escrita ou reconhecida) `[model knowledge — verify]`.
- Advogado calcula data exata de vencimento (alguns contam dias corridos, outros úteis — CPC art. 219 especifica "corridos"; prazo começado no último dia útil continua no próximo útil) `[model knowledge — verify]`.
- Advogado confirma jurisprudência recente (Tema STJ, Súmula TST, OJ, Súmula STF — prazos e termo inicial mudam com jurisprudência).
- **Especial cuidado:** Dano moral trabalhista, dano moral cível — conflito de prescrição (5 vs. 10 anos) — advogado pesquisa Tema mais recente antes de usar prazo.

---

## No silent supplement

Se a jurisprudência sobre prescrição muda (novo Tema STJ sobre dano moral, mudança em Súmula TST sobre bienal trabalhista, EC alterar prazos), avise — não preenche de modelo sem flag. Exemplo: "Uso prescrição 5 anos para dano moral (CC art. 206, III), mas há corrente de 10 anos (CC art. 205 geral) — **jurisprudência conflitante, flag crítica.** Advogado pesquisa Tema / Súmula recente do tribunal competente (TJ/TRF/TST/STJ) antes de usar este prazo."

---

## What this skill does not do

- **Não calcula datas.** Você estrutura os prazos; advogado calcula as datas exatas (com cuidado para dias corridos vs. úteis).
- **Não opina sobre prescrição.** A tabela aponta qual prazo a Lei estabelece — casos concretos (termo inicial, interrupção, suspensão, decadência vs. prescrição) dependem de fatos concretos e jurisprudência.
- **Não substitui pesquisa jurisprudencial.** Jurisprudência recente (Tema STJ, Súmulas TST/STF, OJ) pode ter mudado — advogado verifica com autoridade competente.
- **Não resolve conflito jurisprudencial.** Dano moral: 5 ou 10 anos? Jurisprudência divergente. Advogado pesquisa posição do tribunal onde será julgada a causa.
