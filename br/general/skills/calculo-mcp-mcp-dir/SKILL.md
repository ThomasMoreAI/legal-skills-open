---
name: calculo-mcp-mcp-dir
title: Calculadora Jurídica — REST API skill
description: 'Skill da REST API do Calculadora Jurídica na MCP.AI: 16 endpoints em /api/calculo. Calculadoras jurídicas automáticas: atualização monetária e liquidação de débitos (correção por IPCA, INPC, IGP-M, SELIC, TR e outros índices oficiais + juros, multa e honorários), com índices buscados ao vivo no BACEN e IBGE. Sem credencial; hospedado pela plataforma. Ideal para liquidação de sentença, execução, ação de cobrança e atualização de aluguel/pensão. Autentique com workspace API key (sk_live) gerada em app.mcp.ai/settings/api-keys. Use quando o usuário pedir algo coberto pelos endpoints.'
author: mcp-dir
author_url: https://github.com/mcp-dir/calculo-mcp/tree/main/skills/calculo-mcp
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# Calculadora Jurídica — REST API skill

Você tem acesso à **Calculadora Jurídica** REST API na MCP.AI.

> Calculadoras jurídicas automáticas: atualização monetária e liquidação de débitos (correção por IPCA, INPC, IGP-M, SELIC, TR e outros índices oficiais + juros, multa e honorários), com índices buscados ao vivo no BACEN e IBGE. Sem credencial; hospedado pela plataforma. Ideal para liquidação de sentença, execução, ação de cobrança e atualização de aluguel/pensão.

## Base URL

```
https://api.mcp.ai/api/calculo
```

Todo endpoint é um **POST** na Base URL + o path abaixo. Os parâmetros vão no corpo JSON.

## Autenticação

Inclua em toda request:

```
Authorization: Bearer sk_live_...
Content-Type: application/json
```

> Gere sua chave em **https://app.mcp.ai/settings/api-keys** (workspace API key `sk_live_…`, não expira, revogável). Uma única chave serve pra todos os seus MCPs.

## Formato de resposta

```json
{ "ok": true, "tool": "<tool_id>", "result": <payload> }
```

## Exemplo cURL

```bash
curl -X POST https://api.mcp.ai/api/calculo/aluguel \
  -H "Authorization: Bearer sk_live_..." \
  -H "Content-Type: application/json" \
  -d '{"aluguel_inicial":0,"inicio_contrato":"...","inicio_atraso":"...","fim_atraso":"..."}'
```

## Reportar problemas

Se um endpoint retornar erro, vazio ou dado inesperado, reporte (não desista calado): **POST /api/calculo/report** com `{ "message": "...", "context"?: "...", "conversation"?: [...] }`. Isso notifica o time da MCP.AI.

## Endpoints (16)

#### `calculo_aluguel`

Aluguéis em atraso (Lei 8.245/91): reajusta o aluguel ao longo do contrato pelo índice, corrige cada mês atrasado até hoje, aplica juros de mora (1% a.m.) e multa moratória. _(POST /api/calculo/aluguel)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `aluguel_inicial` | number | Sim | Valor inicial do aluguel (R$). |
| `inicio_contrato` | string | Sim | Início do contrato (dd/mm/yyyy) — base dos reajustes. |
| `inicio_atraso` | string | Sim | Início do atraso (dd/mm/yyyy). |
| `fim_atraso` | string | Sim | Fim do atraso (dd/mm/yyyy). |
| `data_calculo` | string | Não | Default = fim do atraso. |
| `indice` | string | Não | Índice de reajuste/correção (default IGP-M). (NENHUM, IPCA, IPCA-E, IPCA-15, INPC, IGP-M, IGP-DI, INCC, IPC-FIPE, SELIC, CDI, TR, POUPANCA, POUPANCA-ANTIGA) |
| `periodicidade_meses` | integer | Não | Periodicidade do reajuste (12=anual, default). |
| `juros` | number | Não | % a.m. de mora (default 1). |
| `multa` | number | Não | % multa moratória sobre o aluguel (default 10). |

#### `calculo_atualizar`

Atualização monetária / liquidação de débito judicial: corrige parcelas por um índice oficial (IPCA, INPC, IGP-M, SELIC, TR…) e aplica juros, multa e honorários. _(POST /api/calculo/atualizar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `parcelas` | object[] | Sim | Parcelas a atualizar (mínimo 1). |
| `indice` | string | Não | Índice de correção (default NENHUM). (NENHUM, IPCA, IPCA-E, IPCA-15, INPC, IGP-M, IGP-DI, INCC, IPC-FIPE, SELIC, CDI, TR, POUPANCA, POUPANCA-ANTIGA) |
| `data_calculo` | string | Não | Data final do cálculo (dd/mm/yyyy; default hoje). |
| `taxa_juros` | number | Não | Juros em % (ex.: 1 = 1%). Default 0. |
| `periodicidade_juros` | string | Não | Default MENSAL. (MENSAL, ANUAL) |
| `juros_tipo` | string | Não | Default simples. (simples, composto) |
| `multa` | number | Não | Multa em %. Default 0. |
| `multa_incide_sobre_juros` | boolean | Não | Default false. |
| `honorarios` | number | Não | Honorários: % se PERCENTUAL, R$ se FIXO. Default 0. |
| `honorarios_tipo` | string | Não | Default PERCENTUAL. (PERCENTUAL, FIXO) |
| `pro_rata` | boolean | Não | Correção pró-rata die no mês final. Default true. |

#### `calculo_dosimetria`

Dosimetria da pena (art. 68 CP, sistema trifásico): pena-base pelas circunstâncias judiciais (art. 59), pena intermediária por atenuantes/agravantes (Súmula 231 STJ), pena definitiva por causas de aum _(POST /api/calculo/dosimetria)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `pena_min_anos` | number | Sim | Pena mínima abstrata (anos). |
| `pena_max_anos` | number | Sim | Pena máxima abstrata (anos). |
| `circunstancias_desfavoraveis` | integer | Não | Nº de circunstâncias do art. 59 desfavoráveis (0..8). |
| `atenuantes` | integer | Não |  |
| `agravantes` | integer | Não |  |
| `causas_aumento` | object[] | Não | Causas de aumento (3ª fase), ex.: [{frac:0.166}]. |
| `causas_diminuicao` | object[] | Não | Causas de diminuição/tentativa, ex.: [{frac:0.333}]. |
| `fracao_fase1` | number | Não | Fração do intervalo por circunstância (default 1/8). |
| `fracao_fase2` | number | Não | Quantum por atenuante/agravante (default 1/6). |

#### `calculo_fgts`

Correção do FGTS (tese TR → INPC/IPCA-E, STF): por depósito calcula a diferença entre corrigir pelo índice de inflação vs pela TR, com juros de 3% a.a. _(POST /api/calculo/fgts)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `depositos` | object[] | Sim | Depósitos do FGTS (data + valor). |
| `data_calculo` | string | Não |  |
| `indice` | string | Não | Índice substituto (default INPC). (NENHUM, IPCA, IPCA-E, IPCA-15, INPC, IGP-M, IGP-DI, INCC, IPC-FIPE, SELIC, CDI, TR, POUPANCA, POUPANCA-ANTIGA) |
| `incluir_juros_3aa` | boolean | Não | Aplica 3% a.a. sobre a diferença (default true). |

#### `calculo_indice`

Consulta de índice oficial: fator de correção acumulado entre duas datas (mês inicial excluído, mês final incluído — convenção BACEN/IBGE). _(POST /api/calculo/indice)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `indice` | string | Sim | Índice (ex.: IPCA, INPC, IGP-M, SELIC, TR). (NENHUM, IPCA, IPCA-E, IPCA-15, INPC, IGP-M, IGP-DI, INCC, IPC-FIPE, SELIC, CDI, TR, POUPANCA, POUPANCA-ANTIGA) |
| `data_inicial` | string | Sim | Data inicial (dd/mm/yyyy). |
| `data_final` | string | Não | Data final (dd/mm/yyyy; default hoje). |
| `valor` | number | Não | Valor a corrigir (R$). Opcional. |
| `pro_rata` | boolean | Não | Pró-rata die no mês final. Default true. |
| `incluir_valores` | boolean | Não | Se true, retorna as variações mensais do índice. |

#### `calculo_partilha`

Partilha de bens no divórcio por regime (Código Civil): apura a massa partilhável (bens − dívidas conforme o regime) e a quota de cada cônjuge, com torna por desequilíbrio. _(POST /api/calculo/partilha)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `regime` | string | Sim | Regime de bens. (COMUNHAO_PARCIAL, COMUNHAO_UNIVERSAL, SEPARACAO_TOTAL, PARTICIPACAO_FINAL_AQUESTOS) |
| `bens` | object[] | Sim | Bens do casal. |
| `dividas` | object[] | Não |  |
| `nomes` | object | Não |  |

#### `calculo_pensao`

Pensão alimentícia em atraso (art. _(POST /api/calculo/pensao)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `forma` | string | Sim | Forma de estipulação. (PERCENTUAL_SM, VALOR_FIXO, PERCENTUAL_REMUNERACAO) |
| `referencia` | number | Sim | % (se PERCENTUAL_*) ou valor R$ (se VALOR_FIXO). |
| `inicio_atraso` | string | Sim | dd/mm/yyyy. |
| `fim_atraso` | string | Sim | dd/mm/yyyy. |
| `data_calculo` | string | Não |  |
| `indice` | string | Não | Default INPC. (NENHUM, IPCA, IPCA-E, IPCA-15, INPC, IGP-M, IGP-DI, INCC, IPC-FIPE, SELIC, CDI, TR, POUPANCA, POUPANCA-ANTIGA) |
| `juros` | number | Não | % a.m. (default 1). |
| `pagamentos` | object[] | Não | Pagamentos parciais por mês. |
| `remuneracoes` | object[] | Não | Remuneração do alimentante por mês (p/ PERCENTUAL_REMUNERACAO). |

#### `calculo_progressao`

Progressão de regime (LEP art. _(POST /api/calculo/progressao)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `pena_anos` | number | Sim | Pena total (anos). |
| `inicio_cumprimento` | string | Sim | dd/mm/yyyy. |
| `reincidente` | boolean | Não |  |
| `hediondo` | boolean | Não |  |
| `violencia` | boolean | Não | Crime comum com violência/grave ameaça. |
| `resultado_morte` | boolean | Não |  |
| `dias_trabalhados` | integer | Não | Remição: 1 dia por 3 trabalhados. |
| `horas_estudo` | number | Não | Remição: 1 dia por 12h. |
| `dias_detracao` | integer | Não | Prisão provisória abatida. |

#### `calculo_restituicao_inss`

Restituição de descontos indevidos no INSS (fraude associativa, códigos 280/304/310/378): soma as parcelas descontadas corrigidas. _(POST /api/calculo/restituicao/inss)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `descontos` | object[] | Sim | Descontos indevidos (código + mês + valor). |
| `indice` | string | Não | Default INPC. (NENHUM, IPCA, IPCA-E, IPCA-15, INPC, IGP-M, IGP-DI, INCC, IPC-FIPE, SELIC, CDI, TR, POUPANCA, POUPANCA-ANTIGA) |
| `data_calculo` | string | Não |  |

#### `calculo_revisional`

Revisional de contrato bancário: recalcula o financiamento pela taxa média de mercado do BACEN (busca ao vivo por modalidade+mês) e apura o excedente por parcela (Price ou SAC). _(POST /api/calculo/revisional)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `valor_financiado` | number | Sim | Principal financiado (PV). |
| `num_parcelas` | integer | Sim | Número de parcelas. |
| `taxa_contratada_am` | number | Sim | Taxa contratada (% a.m.). |
| `parcela_paga` | number | Sim | Valor pago por parcela (R$). |
| `sistema` | string | Não | Default PRICE. (PRICE, SAC) |
| `modalidade` | string | Não | Modalidade BACEN (busca a taxa média ao vivo). (PF_CREDITO_PESSOAL_NAO_CONSIGNADO, PF_AQUISICAO_VEICULOS, PF_CHEQUE_ESPECIAL, PF_TOTAL) |
| `data_contrato` | string | Não | dd/mm/yyyy (mês da taxa BACEN). |
| `taxa_bacen_am` | number | Não | Alternativa: informar a taxa BACEN (% a.m.) direto. |

#### `calculo_rmc_rcc`

RMC/RCC — reserva de margem consignável de cartão (INSS, códigos 217/268): limites de 5% e restituição corrigida dos descontos. _(POST /api/calculo/rmc/rcc)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `beneficio_mensal` | number | Sim | Valor do benefício (R$). |
| `descontos` | object[] | Sim | Descontos mensais de RMC/RCC. |
| `indice` | string | Não | Default INPC. (NENHUM, IPCA, IPCA-E, IPCA-15, INPC, IGP-M, IGP-DI, INCC, IPC-FIPE, SELIC, CDI, TR, POUPANCA, POUPANCA-ANTIGA) |
| `data_calculo` | string | Não |  |
| `tipo` | string | Não | Default RMC (cód.217). (RMC, RCC) |

#### `calculo_rmi`

RMI — Renda Mensal Inicial (pós-reforma EC 103/2019): média dos salários de contribuição × coeficiente (60% + 2% por ano acima de 20H/15M), com piso (salário mínimo) e teto (INSS). _(POST /api/calculo/rmi)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `sexo` | string | Sim |  (H, M) |
| `media_salarios` | number | Sim | Média dos salários de contribuição (R$). |
| `tempo_contribuicao_anos` | number | Sim | Tempo de contribuição (anos). |
| `salario_minimo` | number | Não | Piso (default fallback 2026). |
| `teto_inss` | number | Não | Teto (default fallback 2026). |

#### `calculo_salario_minimo`

Salário mínimo nacional vigente de um ano (dinâmico, IPEADATA). _(POST /api/calculo/salario/minimo)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ano` | integer | Não | Ano de referência (default ano atual). |

#### `calculo_superendividamento`

Superendividamento (Lei 14.181/2021): % da renda comprometida, mínimo existencial (R$600, parametrizável), renda disponível e capacidade de pagamento de um plano de até 5 anos. _(POST /api/calculo/superendividamento)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `renda_liquida` | number | Sim | Renda líquida mensal (R$). |
| `dividas` | object[] | Sim | Dívidas (parcela mensal e saldo). |
| `minimo_existencial` | number | Não | Default R$600. |
| `prazo_meses` | integer | Não | Prazo do plano (default 60). |

#### `calculo_tempo_contribuicao`

Tempo de contribuição (CNIS): soma os vínculos contando concomitância uma vez e converte atividade especial em comum (fatores EC 103/2019, só até 13/11/2019). _(POST /api/calculo/tempo/contribuicao)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `sexo` | string | Sim | Sexo do segurado. (H, M) |
| `vinculos` | object[] | Sim | Vínculos do CNIS. |

#### `calculo_trabalhista`

Verbas rescisórias / liquidação trabalhista (CLT): saldo de salário, aviso prévio indenizado (Lei 12.506/2011), 13º proporcional, férias proporcionais + 1/3, férias vencidas, multa de 40%/20% do FGTS, _(POST /api/calculo/trabalhista)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `salario` | number | Sim | Remuneração mensal (R$). |
| `admissao` | string | Sim | dd/mm/yyyy. |
| `demissao` | string | Sim | dd/mm/yyyy. |
| `motivo` | string | Não | Default sem_justa_causa. (sem_justa_causa, pedido_demissao, justa_causa, acordo) |
| `aviso` | string | Não | Default indenizado. (indenizado, trabalhado, dispensado) |
| `saldo_fgts` | number | Não | Saldo do FGTS do contrato (p/ multa 40%/20%). |
| `dependentes` | integer | Não | Nº de dependentes (IRRF). |
| `ferias_vencidas` | boolean | Não | Há período aquisitivo vencido não gozado? |
| `projetar_aviso` | boolean | Não | Projeta o aviso indenizado nos avos (default true). |

---

Este MCP também funciona via **conexão MCP** (Claude / Cursor) em `https://api.mcp.ai/p_calculo` — veja o [README](../../README.md). A skill acima é pra consumir a **REST API** direto (agente próprio / código).
