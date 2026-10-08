---
name: jus-mcp-mcp-dir
title: Jus MCP — REST API skill
description: 'Stack jurídica brasileira completa num MCP só: busca de processos por nome/CPF/CNPJ/número, movimentações (CNJ/DataJud), publicações e intimações (DJEN), jurisprudência e súmulas, 16 cálculos judiciais, licitações (PNCP), acórdãos do TCU, certidões de regularidade, marcas e patentes (INPI), compliance/sanções e mais de 150 consultas em órgãos oficiais. Use sempre que o usuário citar número de processo, OAB, CPF/CNPJ em contexto jurídico, pedir andamento, jurisprudência, cálculo judicial, certidão ou checagem de sanções. Sem login; fontes públicas grátis, consultas pagas por crédito pré-pago. Servidor remoto em https://api.mcp.ai/jus.'
author: mcp-dir
author_url: https://github.com/mcp-dir/jus-mcp/tree/main/skills/jus-mcp
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Jus MCP — REST API skill

Você tem acesso à **Jus MCP** REST API na MCP.AI.

> Todo o jurídico brasileiro numa conexão só: processos por nome/CPF/CNPJ/número, publicações e intimações do DJEN, jurisprudência, cálculos judiciais, licitações do PNCP e acórdãos do TCU, certidões de regularidade, sanções e compliance, e mais de 150 consultas em fontes e órgãos oficiais. Hospedado pela plataforma, sem login, com as fontes públicas grátis e crédito pré-pago só nas consultas pagas.

## Base URL

```
https://api.mcp.ai/api/jus
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
curl -X POST https://api.mcp.ai/api/jus/calculo/aluguel \
  -H "Authorization: Bearer sk_live_..." \
  -H "Content-Type: application/json" \
  -d '{"aluguel_inicial":0,"inicio_contrato":"...","inicio_atraso":"...","fim_atraso":"..."}'
```

## Reportar problemas

Se um endpoint retornar erro, vazio ou dado inesperado, reporte (não desista calado): **POST /api/jus/report** com `{ "message": "...", "context"?: "...", "conversation"?: [...] }`. Isso notifica o time da MCP.AI.

## Endpoints (270)

#### `calculo_aluguel`

Aluguéis em atraso (Lei 8.245/91): reajusta o aluguel ao longo do contrato pelo índice, corrige cada mês atrasado até hoje, aplica juros de mora (1% a.m.) e multa moratória. _(POST /api/jus/calculo/aluguel)_

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

Atualização monetária / liquidação de débito judicial: corrige parcelas por um índice oficial (IPCA, INPC, IGP-M, SELIC, TR…) e aplica juros, multa e honorários. _(POST /api/jus/calculo/atualizar)_

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

Dosimetria da pena (art. 68 CP, sistema trifásico): pena-base pelas circunstâncias judiciais (art. 59), pena intermediária por atenuantes/agravantes (Súmula 231 STJ), pena definitiva por causas de aum _(POST /api/jus/calculo/dosimetria)_

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

Correção do FGTS (tese TR → INPC/IPCA-E, STF): por depósito calcula a diferença entre corrigir pelo índice de inflação vs pela TR, com juros de 3% a.a. _(POST /api/jus/calculo/fgts)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `depositos` | object[] | Sim | Depósitos do FGTS (data + valor). |
| `data_calculo` | string | Não |  |
| `indice` | string | Não | Índice substituto (default INPC). (NENHUM, IPCA, IPCA-E, IPCA-15, INPC, IGP-M, IGP-DI, INCC, IPC-FIPE, SELIC, CDI, TR, POUPANCA, POUPANCA-ANTIGA) |
| `incluir_juros_3aa` | boolean | Não | Aplica 3% a.a. sobre a diferença (default true). |

#### `calculo_indice`

Consulta de índice oficial: fator de correção acumulado entre duas datas (mês inicial excluído, mês final incluído — convenção BACEN/IBGE). _(POST /api/jus/calculo/indice)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `indice` | string | Sim | Índice (ex.: IPCA, INPC, IGP-M, SELIC, TR). (NENHUM, IPCA, IPCA-E, IPCA-15, INPC, IGP-M, IGP-DI, INCC, IPC-FIPE, SELIC, CDI, TR, POUPANCA, POUPANCA-ANTIGA) |
| `data_inicial` | string | Sim | Data inicial (dd/mm/yyyy). |
| `data_final` | string | Não | Data final (dd/mm/yyyy; default hoje). |
| `valor` | number | Não | Valor a corrigir (R$). Opcional. |
| `pro_rata` | boolean | Não | Pró-rata die no mês final. Default true. |
| `incluir_valores` | boolean | Não | Se true, retorna as variações mensais do índice. |

#### `calculo_partilha`

Partilha de bens no divórcio por regime (Código Civil): apura a massa partilhável (bens − dívidas conforme o regime) e a quota de cada cônjuge, com torna por desequilíbrio. _(POST /api/jus/calculo/partilha)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `regime` | string | Sim | Regime de bens. (COMUNHAO_PARCIAL, COMUNHAO_UNIVERSAL, SEPARACAO_TOTAL, PARTICIPACAO_FINAL_AQUESTOS) |
| `bens` | object[] | Sim | Bens do casal. |
| `dividas` | object[] | Não |  |
| `nomes` | object | Não |  |

#### `calculo_pensao`

Pensão alimentícia em atraso (art. _(POST /api/jus/calculo/pensao)_

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

Progressão de regime (LEP art. _(POST /api/jus/calculo/progressao)_

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

Restituição de descontos indevidos no INSS (fraude associativa, códigos 280/304/310/378): soma as parcelas descontadas corrigidas. _(POST /api/jus/calculo/restituicao/inss)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `descontos` | object[] | Sim | Descontos indevidos (código + mês + valor). |
| `indice` | string | Não | Default INPC. (NENHUM, IPCA, IPCA-E, IPCA-15, INPC, IGP-M, IGP-DI, INCC, IPC-FIPE, SELIC, CDI, TR, POUPANCA, POUPANCA-ANTIGA) |
| `data_calculo` | string | Não |  |

#### `calculo_revisional`

Revisional de contrato bancário: recalcula o financiamento pela taxa média de mercado do BACEN (busca ao vivo por modalidade+mês) e apura o excedente por parcela (Price ou SAC). _(POST /api/jus/calculo/revisional)_

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

RMC/RCC — reserva de margem consignável de cartão (INSS, códigos 217/268): limites de 5% e restituição corrigida dos descontos. _(POST /api/jus/calculo/rmc/rcc)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `beneficio_mensal` | number | Sim | Valor do benefício (R$). |
| `descontos` | object[] | Sim | Descontos mensais de RMC/RCC. |
| `indice` | string | Não | Default INPC. (NENHUM, IPCA, IPCA-E, IPCA-15, INPC, IGP-M, IGP-DI, INCC, IPC-FIPE, SELIC, CDI, TR, POUPANCA, POUPANCA-ANTIGA) |
| `data_calculo` | string | Não |  |
| `tipo` | string | Não | Default RMC (cód.217). (RMC, RCC) |

#### `calculo_rmi`

RMI — Renda Mensal Inicial (pós-reforma EC 103/2019): média dos salários de contribuição × coeficiente (60% + 2% por ano acima de 20H/15M), com piso (salário mínimo) e teto (INSS). _(POST /api/jus/calculo/rmi)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `sexo` | string | Sim |  (H, M) |
| `media_salarios` | number | Sim | Média dos salários de contribuição (R$). |
| `tempo_contribuicao_anos` | number | Sim | Tempo de contribuição (anos). |
| `salario_minimo` | number | Não | Piso (default fallback 2026). |
| `teto_inss` | number | Não | Teto (default fallback 2026). |

#### `calculo_salario_minimo`

Salário mínimo nacional vigente de um ano (dinâmico, IPEADATA). _(POST /api/jus/calculo/salario/minimo)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ano` | integer | Não | Ano de referência (default ano atual). |

#### `calculo_superendividamento`

Superendividamento (Lei 14.181/2021): % da renda comprometida, mínimo existencial (R$600, parametrizável), renda disponível e capacidade de pagamento de um plano de até 5 anos. _(POST /api/jus/calculo/superendividamento)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `renda_liquida` | number | Sim | Renda líquida mensal (R$). |
| `dividas` | object[] | Sim | Dívidas (parcela mensal e saldo). |
| `minimo_existencial` | number | Não | Default R$600. |
| `prazo_meses` | integer | Não | Prazo do plano (default 60). |

#### `calculo_tempo_contribuicao`

Tempo de contribuição (CNIS): soma os vínculos contando concomitância uma vez e converte atividade especial em comum (fatores EC 103/2019, só até 13/11/2019). _(POST /api/jus/calculo/tempo/contribuicao)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `sexo` | string | Sim | Sexo do segurado. (H, M) |
| `vinculos` | object[] | Sim | Vínculos do CNIS. |

#### `calculo_trabalhista`

Verbas rescisórias / liquidação trabalhista (CLT): saldo de salário, aviso prévio indenizado (Lei 12.506/2011), 13º proporcional, férias proporcionais + 1/3, férias vencidas, multa de 40%/20% do FGTS, _(POST /api/jus/calculo/trabalhista)_

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

#### `capivara_dossie`

Raio-X cadastral 360º de uma PESSOA (por CPF) OU EMPRESA (por CNPJ) — consolidado num relatório por seção. _(POST /api/jus/capivara/dossie)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Nome completo do investigado (melhora antecedentes/sanções; obrigatório p/ processos). |
| `cpf` | string | Não | CPF do investigado (pessoa física). Informe cpf OU cnpj. |
| `cnpj` | string | Não | CNPJ (pessoa jurídica). Informe cpf OU cnpj. |
| `nivel` | string | Não | Profundidade/preço do dossiê: basico (R$39, ~15s), medio (R$149, ~30-60s), avancado (R$249, o mais demorado). Default basico. (basico, medio, avancado) |
| `formato` | string | Não | **resumo** (default): devolve um digest (status de cada fonte + destaques) e o dossiê INTEIRO vai num arquivo .md, aberto por seção com `arquivo_ler(file_id, secao)`. É o modo certo pra conversa: o completo passa de 100 mil tokens e estoura o contexto. **completo**: todas as seções na resposta (use só se for processar o JSON inteiro por programa, ex.: integração REST). (resumo, completo) |
| `autorizacao_titular_scr` | boolean | Não | Declara que o usuário tem AUTORIZAÇÃO do titular para dados sob sigilo (SCR/Bacen e relatório de crédito positivo). Só marque true após confirmar com o usuário. Sem isso, esses itens são pulados (o resto do dossiê roda normalmente). |

#### `capivara_registrar_consentimento`

Registra, de forma auditável (LGPD), a finalidade e a base legal de uma investigação — e, quando aplicável, a DECLARAÇÃO do usuário de que tem autorização do titular para dados sob sigilo (SCR/Bacen, _(POST /api/jus/capivara/registrar/consentimento)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | CPF do titular investigado (informe cpf OU cnpj). |
| `cnpj` | string | Não | CNPJ investigado (informe cpf OU cnpj). |
| `finalidade` | string | Sim | Finalidade da consulta (ex.: 'prevenção à fraude em contratação', 'due diligence de fornecedor'). |
| `base_legal` | string | Sim | Base legal LGPD que ampara o tratamento. (prevencao_fraude, obrigacao_legal, legitimo_interesse, exercicio_de_direitos, consentimento_do_titular, protecao_ao_credito) |
| `autorizacao_titular` | boolean | Não | Declara que o usuário tem autorização do titular para dados sob sigilo (SCR/cadastro positivo). Marque true só após confirmar com o usuário. |
| `observacao` | string | Não | Observação livre (ex.: nº do contrato/processo que justifica). |

#### `capivara_resolver`

CAMADA 1 (descoberta de identidade): a partir do que você SABE da pessoa em TEXTO LIVRE (nome, cidade, emprego, empresa, qualquer pista), descobre o CPF mais provável e devolve um PERFIL NORMALIZADO ( _(POST /api/jus/capivara/resolver)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `texto` | string | Não | Tudo que você sabe da pessoa, em texto livre: nome completo, cidade, emprego, empresa, cônjuge, qualquer pista. Quanto mais informação, maior a precisão. |
| `cnpj` | string | Não | CNPJ de uma empresa da pessoa, se você já tiver (atalho: pula a busca na web). |
| `seguir_dossie` | boolean | Não | Se true e o CPF for confirmado, já emite o `capivara_dossie` 360º na sequência (cobra o nível por cima). |
| `nivel` | string | Não | Nível do dossiê quando seguir_dossie=true (default basico). (basico, medio, avancado) |

#### `cnpj_consultar`

Consulta cadastral de um CNPJ (grátis): razão social, nome fantasia, situação cadastral, CNAE principal, porte, município/UF e SÓCIOS (QSA). _(POST /api/jus/cnpj/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Sim | CNPJ (14 dígitos), com ou sem máscara. |

#### `cnpj_processos`

DESCOBERTA por CNPJ: resolve o CNPJ em razão social (e sócios) e busca os processos por NOME no Diário (DJEN) — grátis, com número de processo completo. _(POST /api/jus/cnpj/processos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Sim | CNPJ (14 dígitos), com ou sem máscara. |
| `incluir_socios` | boolean | Não | Se true, também busca os processos de cada sócio (QSA). Default false. |

#### `cpf_processos`

DESCOBERTA por CPF: busca os processos da pessoa por NOME no Diário (DJEN), grátis. _(POST /api/jus/cpf/processos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Sim | CPF (11 dígitos), com ou sem máscara. |
| `nome` | string | Não | Nome completo do titular (recomendado — CPF→nome não é público). |

#### `cpf_validar`

Valida os dígitos verificadores de um CPF (mod 11) e informa se há broker de identidade disponível. _(POST /api/jus/cpf/validar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Sim | CPF (11 dígitos), com ou sem máscara. |

#### `datajud_get_processo`

Busca um processo pelo número único do CNJ (com ou sem máscara) em um tribunal. _(POST /api/jus/datajud/get/processo)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tribunal` | string | Sim | Alias do tribunal no CNJ (índice api_publica_<alias>). Ex.: tjsp, trf1, stj, trt2, tre-sp. Obrigatório — cada tribunal é um índice separado. (tst, stj, tse, stm, trf1, trf2, trf3, trf4, trf5, trf6, tjac, tjal, tjam, tjap, tjba, tjce, tjdft, tjes, tjgo, tjma, tjmg, tjms, tjmt, tjpa, tjpb, tjpe, tjpi, tjpr, tjrj, tjrn, tjro, tjrr, tjrs, tjsc, tjse, tjsp, tjto, trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8, trt9, trt10, trt11, trt12, trt13, trt14, trt15, trt16, trt17, trt18, trt19, trt20, trt21, trt22, trt23, trt24, tre-ac, tre-al, tre-am, tre-ap, tre-ba, tre-ce, tre-df, tre-es, tre-go, tre-ma, tre-mg, tre-ms, tre-mt, tre-pa, tre-pb, tre-pe, tre-pi, tre-pr, tre-rj, tre-rn, tre-ro, tre-rr, tre-rs, tre-sc, tre-se, tre-sp, tre-to, tjmmg, tjmrs, tjmsp) |
| `numero_processo` | string | Sim | Número único do processo (CNJ), com ou sem máscara. |

#### `datajud_movimentos`

Retorna apenas a timeline de movimentações (+ metadados) de um processo — ideal pra detectar se houve movimentação nova. _(POST /api/jus/datajud/movimentos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tribunal` | string | Sim | Alias do tribunal no CNJ (índice api_publica_<alias>). Ex.: tjsp, trf1, stj, trt2, tre-sp. Obrigatório — cada tribunal é um índice separado. (tst, stj, tse, stm, trf1, trf2, trf3, trf4, trf5, trf6, tjac, tjal, tjam, tjap, tjba, tjce, tjdft, tjes, tjgo, tjma, tjmg, tjms, tjmt, tjpa, tjpb, tjpe, tjpi, tjpr, tjrj, tjrn, tjro, tjrr, tjrs, tjsc, tjse, tjsp, tjto, trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8, trt9, trt10, trt11, trt12, trt13, trt14, trt15, trt16, trt17, trt18, trt19, trt20, trt21, trt22, trt23, trt24, tre-ac, tre-al, tre-am, tre-ap, tre-ba, tre-ce, tre-df, tre-es, tre-go, tre-ma, tre-mg, tre-ms, tre-mt, tre-pa, tre-pb, tre-pe, tre-pi, tre-pr, tre-rj, tre-rn, tre-ro, tre-rr, tre-rs, tre-sc, tre-se, tre-sp, tre-to, tjmmg, tjmrs, tjmsp) |
| `numero_processo` | string | Sim | Número único do processo (CNJ). |

#### `datajud_raw_query`

Avançado: envia um corpo de query Elasticsearch cru pro índice do tribunal (escape hatch). _(POST /api/jus/datajud/raw/query)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tribunal` | string | Sim | Alias do tribunal no CNJ (índice api_publica_<alias>). Ex.: tjsp, trf1, stj, trt2, tre-sp. Obrigatório — cada tribunal é um índice separado. (tst, stj, tse, stm, trf1, trf2, trf3, trf4, trf5, trf6, tjac, tjal, tjam, tjap, tjba, tjce, tjdft, tjes, tjgo, tjma, tjmg, tjms, tjmt, tjpa, tjpb, tjpe, tjpi, tjpr, tjrj, tjrn, tjro, tjrr, tjrs, tjsc, tjse, tjsp, tjto, trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8, trt9, trt10, trt11, trt12, trt13, trt14, trt15, trt16, trt17, trt18, trt19, trt20, trt21, trt22, trt23, trt24, tre-ac, tre-al, tre-am, tre-ap, tre-ba, tre-ce, tre-df, tre-es, tre-go, tre-ma, tre-mg, tre-ms, tre-mt, tre-pa, tre-pb, tre-pe, tre-pi, tre-pr, tre-rj, tre-rn, tre-ro, tre-rr, tre-rs, tre-sc, tre-se, tre-sp, tre-to, tjmmg, tjmrs, tjmsp) |
| `query` | string | Sim | Objeto Elasticsearch Query DSL (ex.: { match_all: {} }). |
| `size` | integer | Não |  |
| `from` | integer | Não |  |
| `sort` | string | Não | Array de sort do Elasticsearch. |
| `search_after` | string | Não | Cursor (valor sort do último hit) pra paginação profunda. |

#### `datajud_search`

Busca processos em um tribunal por classe, órgão julgador e/ou assunto (códigos das tabelas do CNJ), paginada e ordenada por data de ajuizamento. _(POST /api/jus/datajud/search)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tribunal` | string | Sim | Alias do tribunal no CNJ (índice api_publica_<alias>). Ex.: tjsp, trf1, stj, trt2, tre-sp. Obrigatório — cada tribunal é um índice separado. (tst, stj, tse, stm, trf1, trf2, trf3, trf4, trf5, trf6, tjac, tjal, tjam, tjap, tjba, tjce, tjdft, tjes, tjgo, tjma, tjmg, tjms, tjmt, tjpa, tjpb, tjpe, tjpi, tjpr, tjrj, tjrn, tjro, tjrr, tjrs, tjsc, tjse, tjsp, tjto, trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8, trt9, trt10, trt11, trt12, trt13, trt14, trt15, trt16, trt17, trt18, trt19, trt20, trt21, trt22, trt23, trt24, tre-ac, tre-al, tre-am, tre-ap, tre-ba, tre-ce, tre-df, tre-es, tre-go, tre-ma, tre-mg, tre-ms, tre-mt, tre-pa, tre-pb, tre-pe, tre-pi, tre-pr, tre-rj, tre-rn, tre-ro, tre-rr, tre-rs, tre-sc, tre-se, tre-sp, tre-to, tjmmg, tjmrs, tjmsp) |
| `classe_codigo` | integer | Não | Código da classe processual (tabela CNJ). |
| `orgao_julgador_codigo` | integer | Não | Código do órgão julgador. |
| `assunto_codigo` | integer | Não | Código do assunto (tabela CNJ). |
| `numero_processo` | string | Não | Filtra por número de processo (dígitos). |
| `size` | integer | Não | Resultados por página (default 10, máx 100). |
| `from` | integer | Não | Offset de paginação (janela ES limitada a ~10k). |
| `sort_desc` | boolean | Não | Ordenar por dataAjuizamento decrescente (default crescente). |

#### `djen_get_certidao`

Retorna a URL da certidão (PDF) de uma comunicação do DJEN pelo seu hash (campo `hash` retornado na busca). _(POST /api/jus/djen/get/certidao)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `hash` | string | Sim | Hash da comunicação (campo hash da busca). |

#### `djen_processos_por_parte`

DESCOBERTA por NOME de parte (grátis, sem captcha): busca o DJEN por quem figura no processo e agrupa por número — devolve a lista de processos da pessoa/empresa, com partes e tribunal. _(POST /api/jus/djen/processos/por/parte)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome_parte` | string | Sim | Nome da parte (pessoa ou razão social) a procurar. |
| `sigla_tribunal` | string | Não | Restringe a um tribunal (ex.: TJSP). |
| `data_inicio` | string | Não | Data inicial (AAAA-MM-DD). |
| `data_fim` | string | Não | Data final (AAAA-MM-DD). |
| `itens_por_pagina` | integer | Não | Comunicações a varrer por página (default 100). |
| `pagina` | integer | Não | Página (default 1). |

#### `djen_search_comunicacoes`

Busca publicações/intimações no Diário de Justiça Eletrônico Nacional (DJEN) por OAB, nome de advogado, número de processo, tribunal e data. _(POST /api/jus/djen/search/comunicacoes)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_oab` | string | Não | Número da OAB (ex.: 21076). |
| `uf_oab` | string | Não | UF da OAB (ex.: SP). |
| `nome_advogado` | string | Não | Nome do advogado. |
| `nome_parte` | string | Não | Nome da PARTE (pessoa ou empresa) — busca por quem figura no processo, não pelo advogado. Use para descobrir processos de alguém pelo nome. |
| `numero_processo` | string | Não | Número do processo (dígitos). |
| `sigla_tribunal` | string | Não | Sigla do tribunal (ex.: TJSP, TRT5, TST, CJF). |
| `data_inicio` | string | Não | Data de disponibilização inicial (AAAA-MM-DD). |
| `data_fim` | string | Não | Data de disponibilização final (AAAA-MM-DD). |
| `meio` | string | Não | Meio: "D" (Diário) ou "E" (Edital). |
| `texto` | string | Não | Busca por termo no texto. |
| `pagina` | integer | Não | Página (default 1). |
| `itens_por_pagina` | integer | Não | Itens por página (default ~100; mín. efetivo 5). |

#### `jurisprudencia_buscar`

Busca jurisprudência (acórdãos, súmulas, OJs) no acervo público LexML por termo/tese — cobre tribunais superiores e demais. _(POST /api/jus/jurisprudencia/buscar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Sim | Termo, tese ou assunto (ex.: 'dano moral negativação indevida'). |
| `tipo` | string | Não | Filtra por tipo de documento (ex.: "Acórdão", "Súmula"). |
| `max` | integer | Não | Resultados (default 10, máx 50). |

#### `jurisprudencia_sumulas`

Busca SÚMULAS (incluindo vinculantes) por termo no acervo LexML. _(POST /api/jus/jurisprudencia/sumulas)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Sim | Termo/assunto da súmula. |
| `max` | integer | Não | Resultados (default 10). |

#### `legal_checar_novidades`

Checa AGORA se há novidade nos monitoramentos (sem esperar o ciclo automático). _(POST /api/jus/legal/checar/novidades)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `watch_id` | string | Não | Id de um monitoramento específico (opcional). |
| `watch_ids` | string[] | Não | Bulk mode: multiple values for watch_id |

#### `legal_dossie`

Raio-X jurídico de uma pessoa ou empresa: descobre os processos e (opcional) o andamento, num relatório consolidado. _(POST /api/jus/legal/dossie)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Nome de pessoa ou razão social a investigar. |
| `cnpj` | string | Não | CNPJ (14 dígitos) — resolve a empresa e busca por nome. |
| `cpf` | string | Não | CPF (11 dígitos) — exige também `nome_titular` (CPF→nome não é público). |
| `nome_titular` | string | Não | Nome do titular do CPF (obrigatório quando usar `cpf`). |
| `numero_processo` | string | Não | Número CNJ de um processo específico (pula a descoberta). |
| `incluir_andamento` | boolean | Não | Se true, enriquece cada processo com classe + nº de movimentações (mais lento). Default false. |
| `incluir_socios` | boolean | Não | Para CNPJ: também busca os processos dos sócios. Default false. |
| `incluir_sancoes` | boolean | Não | Anexa sanções (compliance) quando houver CPF/CNPJ no alvo. Default false. |
| `incluir_mencoes_municipais` | boolean | Não | Anexa menções em diários municipais (por nome). Default false. |
| `max_processos` | integer | Não | Máximo de processos no relatório (default 10). |
| `sigla_tribunal` | string | Não | Restringe a um tribunal (ex.: TJSP). |

#### `legal_listar_monitoramentos`

Lista os monitoramentos ativos do workspace. _(POST /api/jus/legal/listar/monitoramentos)_

#### `legal_monitorar`

Cria um monitoramento: avisa quando houver NOVIDADE — nova movimentação (numero_processo), novo processo de uma pessoa/empresa (nome/cnpj), ou nova publicação/intimação de uma OAB (oab+uf). _(POST /api/jus/legal/monitorar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Não | Número CNJ a monitorar (andamento). |
| `nome` | string | Não | Nome de pessoa/empresa a monitorar (novos processos). |
| `cnpj` | string | Não | CNPJ a monitorar (resolve a razão social e monitora novos processos). |
| `oab` | string | Não | Número da OAB a monitorar (novas publicações/intimações). Requer `uf`. |
| `uf` | string | Não | UF da OAB (ex.: SP), usado com `oab`. |
| `sigla_tribunal` | string | Não | Restringe a um tribunal (ex.: TJSP). |
| `intervalo_horas` | integer | Não | De quantas em quantas horas checar (default 6). |
| `label` | string | Não | Rótulo amigável pro monitoramento. |

#### `legal_remover_monitoramento`

Remove (desativa) um monitoramento pelo seu id (`watch_id`). _(POST /api/jus/legal/remover/monitoramento)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `watch_id` | string | Sim | Id do monitoramento (wch_…) de legal_listar_monitoramentos. |
| `watch_ids` | string[] | Não | Bulk mode: multiple values for watch_id |

#### `pncp_arquivos`

Documentos de uma licitação/edital (edital, termo de referência, anexos) com o LINK de download de cada arquivo (em geral PDF). _(POST /api/jus/pncp/arquivos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Sim | CNPJ do órgão (com ou sem máscara). |
| `ano` | string|number | Sim | Ano da contratação (ex.: 2026). |
| `sequencial` | string|number | Sim | Número sequencial da contratação no órgão. |

#### `pncp_atas`

Lista atas de registro de preços vigentes num período (referência de preços praticados pelo governo), opcionalmente por órgão (CNPJ). _(POST /api/jus/pncp/atas)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `data_inicial` | string | Sim | Data inicial (AAAA-MM-DD). |
| `data_final` | string | Sim | Data final (AAAA-MM-DD). |
| `cnpj` | string | Não | CNPJ do órgão. Opcional. |
| `pagina` | integer | Não | Página (default 1). |
| `tamanho_pagina` | integer | Não | Itens por página (default 20, máx 50). |

#### `pncp_buscar`

Busca licitações por PALAVRA-CHAVE no objeto (cobertura NACIONAL ampla, índice full-text), em editais, atas ou contratos. _(POST /api/jus/pncp/buscar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Não | Palavra-chave do objeto (ex.: 'material de informática', 'merenda escolar'). Use isto OU `termos[]`. |
| `termos` | string[] | Não | VÁRIAS palavras-chave: cada uma vira uma busca full-text independente, disparadas com um pequeno intervalo entre si (evita rate limit da fonte) e os resultados são fundidos e deduplicados. Ex.: ['notebook','ultrabook','laptop']. Prefira isto a repetir a tool termo a termo. |
| `tipo` | string | Não | Tipo de documento a buscar. Default edital. (edital, ata, contrato) |
| `ordenacao` | string | Não | Ordenação (ex.: '-data' mais recentes primeiro, 'data' mais antigos). Default '-data'. |
| `status` | string | Não | Filtro de situação (ex.: 'todos', 'recebendo_proposta', 'encerradas'). Default 'todos'. |
| `pagina` | integer | Não | Página (default 1). |
| `tam_pagina` | integer | Não | Itens por página (default 20, máx 50). |

#### `pncp_contratos`

Lista contratos públicos firmados num período, opcionalmente filtrando por órgão (CNPJ). _(POST /api/jus/pncp/contratos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `data_inicial` | string | Sim | Data inicial (AAAA-MM-DD). |
| `data_final` | string | Sim | Data final (AAAA-MM-DD). |
| `cnpj_orgao` | string | Não | CNPJ do órgão. Opcional. |
| `pagina` | integer | Não | Página (default 1). |
| `tamanho_pagina` | integer | Não | Itens por página (default 20, máx 50). |

#### `pncp_detalhe`

Detalhe completo de uma licitação/contratação a partir de cnpj+ano+sequencial (a referência devolvida pela pncp_buscar). _(POST /api/jus/pncp/detalhe)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Sim | CNPJ do órgão (com ou sem máscara). |
| `ano` | string|number | Sim | Ano da contratação (ex.: 2026). |
| `sequencial` | string|number | Sim | Número sequencial da contratação no órgão. |
| `itens` | boolean | Não | Se true, também traz os itens com preços. Default false. |
| `resultado` | boolean | Não | Se true, anexa o bloco `resultado` com o(s) vencedor(es) homologado(s) (CNPJ, valor real, natureza jurídica, porte). Default false. Ou use pncp_resultado direto. |

#### `pncp_historico`

Arquivo histórico de licitações: consulta editais que a plataforma acumulou ao longo do tempo (inclusive os que já encerraram ou saíram do ar), por PALAVRA-CHAVE no objeto, estado (UF), modalidade, si _(POST /api/jus/pncp/historico)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Não | Palavra-chave no objeto (ex.: 'software'). Opcional. |
| `uf` | string | Não | Sigla do estado (ex.: SP). Opcional. |
| `modalidade` | string | Não | Modalidade (ex.: 'Pregão'). Opcional. |
| `situacao` | string | Não | Situação (ex.: 'Divulgada'). Opcional. |
| `valor_min` | number | Não | Valor estimado MÍNIMO em R$ (opcional). |
| `valor_max` | number | Não | Valor estimado MÁXIMO em R$ (opcional). |
| `desde` | string | Não | Publicação a partir de (AAAA-MM-DD). Opcional. |
| `ate` | string | Não | Publicação até (AAAA-MM-DD). Opcional. |
| `pagina` | integer | Não | Página (default 1). |
| `tam_pagina` | integer | Não | Itens por página (default 20, máx 100). |

#### `pncp_listar`

Busca PRINCIPAL de licitações abertas por palavra-chave, faixa de VALOR, estado, modalidade e período. _(POST /api/jus/pncp/listar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termos` | string[] | Não | Palavras-chave/frases no objeto (casa QUALQUER uma = OR). SEMPRE expanda o conceito em VÁRIOS sinônimos, NUNCA um termo só. Ex.: pra 'software' use ['software','saas','licença de uso','licenciamento de software','sistema de informação','aplicativo','software como serviço']. PREFIRA termos específicos/frases curtas pra não casar boilerplate (evite 'sistema' sozinho). |
| `data_inicial` | string | Não | Data inicial (AAAA-MM-DD). Opcional (default: 7 dias atrás). |
| `data_final` | string | Não | Data final (AAAA-MM-DD). Opcional (default: hoje). |
| `modalidade` | integer | Não | Código da modalidade (ex.: 6 = Pregão Eletrônico). Opcional: omita pra varrer as comuns. |
| `apenas_abertas` | boolean | Não | Se true, só licitações ainda recebendo proposta (abertas pra participar). |
| `uf` | string | Não | Sigla do estado (ex.: SP, MG). |
| `municipio` | string | Não | Código IBGE do município (7 dígitos). Opcional. |
| `cnpj` | string | Não | CNPJ do órgão. |
| `valor_min` | number | Não | Valor estimado MÍNIMO em R$. |
| `valor_max` | number | Não | Valor estimado MÁXIMO em R$. |
| `ordenacao` | string | Não | Ordenar por: data (recentes 1º) ou prazo (fecha 1º). Por padrão já vem ranqueado por VALOR (maior 1º) quando incluir_valor está ligado. (data, valor, prazo) |
| `tamanho_pagina` | integer | Não | Quantos retornar (default 20, máx 50). |
| `pagina` | integer | Não | Página (1-based, 20 por página). Default 1. A resposta traz `total_paginas`; chame de novo com pagina=2, 3... pra pegar mais. |
| `incluir_valor` | boolean | Não | Enriquecer cada item com o VALOR estimado e ranquear por valor (default TRUE). Passe false pra uma lista mais rápida/barata sem valor. |
| `expandir` | boolean | Não | Expandir os termos em sinônimos automaticamente (default TRUE). Passe false pra buscar só os termos exatos que você mandou. |

#### `pncp_oportunidades`

Busca de OPORTUNIDADES de licitação (editais/pregões) com filtros ricos por palavra-chave, FAIXA DE VALOR da compra, UFs, modalidades, portais, registro de preço, participação exclusiva ME/EPP e super _(POST /api/jus/pncp/oportunidades)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termos` | string[] | Não | Palavras-chave/frases no objeto (casa QUALQUER uma = OR). SEMPRE expanda em VÁRIOS sinônimos, NUNCA um só. Ex.: pra 'software' use ['software','saas','licença de uso','licenciamento de software','sistema de informação','software como serviço']. Mesmo formato de pncp_listar. |
| `termo` | string | Não | Alternativa a `termos`: palavra(s)-chave numa string só (separe várias por ';'). Opcional. |
| `excluir` | string | Não | Palavras-chave a EXCLUIR do resultado. Opcional. |
| `data_inicial` | string | Não | Data inicial do período (AAAA-MM-DD). Opcional. |
| `data_final` | string | Não | Data final do período (AAAA-MM-DD). Opcional. |
| `tipo_periodo` | string | Não | A qual data o período se refere. Default 'abertura'. (abertura, publicacao, encerramento) |
| `valor_min` | number | Não | Valor MÍNIMO estimado da compra em R$ (0 = sem mínimo). |
| `valor_max` | number | Não | Valor MÁXIMO estimado da compra em R$ (0 = sem máximo). |
| `ufs` | string[] | Não | Estados (siglas, ex.: ['SP','MG']). Vazio = todos. |
| `modalidades` | integer[] | Não | Códigos de modalidade (ex.: 6 = Pregão Eletrônico). Vazio = todas. |
| `portais` | string[] | Não | Filtra por portais específicos. Opcional. |
| `superoportunidades` | boolean | Não | Se true, só as marcadas como superoportunidade. |
| `participacao_exclusiva` | boolean | Não | Se true, só licitações exclusivas para ME/EPP. |
| `excluir_registro_preco` | boolean | Não | Se true, exclui licitações de registro de preço. |
| `somente_sigilosos` | boolean | Não | Se true, só com valores sigilosos. |
| `itens_desertos` | boolean | Não | Se true, inclui itens desertos. |
| `tipo_item` | string | Não | Filtra por tipo de item. Opcional. (, MATERIAL, SERVICO) |
| `pesquisa_ampla` | boolean | Não | Busca ampla no objeto (default true). |
| `expandir` | boolean | Não | Expandir os termos em sinônimos automaticamente (default TRUE). false = só os termos exatos. |
| `pagina` | integer | Não | Página (1-based, 20 por página). Default 1. |

#### `pncp_orgaos`

Busca de ÓRGÃOS/entidades compradoras por nome, UF e/ou portal. _(POST /api/jus/pncp/orgaos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Não | Nome (parte) do órgão. Termo amplo demais falha, refine. Use isto OU `termos[]`. |
| `termos` | string[] | Não | Vários nomes de órgão: cada um vira uma busca independente, disparadas com um intervalo entre si (evita rate limit da fonte), resultados fundidos e deduplicados. Opcional. |
| `uf` | string | Não | Sigla do estado (ex.: SP). Opcional. |
| `portais` | string[] | Não | Portais (ex.: ['CN']). Opcional. |
| `antecipagov` | boolean | Não | Se true, consulta a base do AntecipaGov (hierarquia órgão superior). |
| `pagina` | integer | Não | Página (1-based). Default 1. |

#### `pncp_pca`

Plano anual de contratações (PCA) por ano e classificação superior do catálogo: o que os órgãos planejam contratar no ano. _(POST /api/jus/pncp/pca)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ano_pca` | integer | Sim | Ano do PCA (ex.: 2026). |
| `codigo_classificacao_superior` | integer | Sim | Código da classificação superior do item no catálogo. |
| `pagina` | integer | Não | Página (default 1). |
| `tamanho_pagina` | integer | Não | Itens por página (default 20, máx 50). |

#### `pncp_processo`

Detalhe de oportunidade(s) por `id` (de pncp_listar/pncp_oportunidades). _(POST /api/jus/pncp/processo)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `id` | string|number | Não | id de UMA oportunidade → detalhe completo com itens. Use `id` OU `ids`. |
| `ids` | string|number[] | Não | LOTE: vários `id` (de pncp_listar/pncp_oportunidades). Detalha todos numa chamada e devolve RANKING por valor (maior 1º). Ideal pra 'ranquear por valor'. Máx 50. |

#### `pncp_resultado`

Quem GANHOU a licitação: o(s) fornecedor(es) vencedor(es) homologado(s) a partir de cnpj+ano+sequencial (a referência da pncp_buscar). _(POST /api/jus/pncp/resultado)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Sim | CNPJ do órgão (com ou sem máscara). |
| `ano` | string|number | Sim | Ano da contratação (ex.: 2026). |
| `sequencial` | string|number | Sim | Número sequencial da contratação no órgão. |
| `numero_item` | integer | Não | Número de um item específico. Omita pra agregar todos os itens da compra. |

#### `pncp_texto`

Texto INTEIRO do edital em markdown (com marcadores '## Página N'), pra você RESUMIR ou ler o documento todo. _(POST /api/jus/pncp/texto)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Sim | CNPJ do órgão (com ou sem máscara). |
| `ano` | string|number | Sim | Ano da contratação (ex.: 2026). |
| `sequencial` | string|number | Sim | Número sequencial da contratação no órgão. |
| `documento` | string|number | Não | Sequencial de um anexo específico. Default: o edital principal. |
| `de_pagina` | integer | Não | Página inicial (pra editais grandes). Opcional. |
| `ate_pagina` | integer | Não | Página final. Opcional. |

#### `processos_buscar_por_documento`

DESCOBERTA por CPF ou CNPJ. O serviço resolve o documento em nome(s) (CNPJ→razão social/sócios; CPF→nome) e então busca os processos por nome nos portais. ASSÍNCRONO: retorna { job_id }; faça o pollin _(POST /api/jus/processos/buscar/por/documento)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `documento` | string | Sim | CPF (11 dígitos) ou CNPJ (14 dígitos), com ou sem máscara. |
| `platforms` | string[] | Não | Plataformas a varrer (parser por plataforma, não por TJ): esaj, pje, eproc, projudi. Vazio = todas. Restrinja (ex.: ['esaj']) para resultado mais rápido/barato. (esaj, pje, eproc, projudi) |
| `tribunais` | string[] | Não | Restringe a tribunais específicos (ex.: ['tjsp']). Vazio = todos os órgãos das plataformas escolhidas. Quanto mais amplo, mais lento (captcha por órgão). |
| `max_results` | integer | Não | Limite de processos a retornar (default decidido pelo engine). |

#### `processos_buscar_por_nome`

DESCOBERTA: busca processos pelo NOME de uma parte (pessoa ou empresa) raspando os portais públicos dos tribunais (ESAJ/PJe/eproc/Projudi) — o gap que datajud (só por número) e djen (OAB/advogado) não _(POST /api/jus/processos/buscar/por/nome)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Sim | Nome completo da parte (pessoa ou razão social) a procurar. |
| `platforms` | string[] | Não | Plataformas a varrer (parser por plataforma, não por TJ): esaj, pje, eproc, projudi. Vazio = todas. Restrinja (ex.: ['esaj']) para resultado mais rápido/barato. (esaj, pje, eproc, projudi) |
| `tribunais` | string[] | Não | Restringe a tribunais específicos (ex.: ['tjsp']). Vazio = todos os órgãos das plataformas escolhidas. Quanto mais amplo, mais lento (captcha por órgão). |
| `max_results` | integer | Não | Limite de processos a retornar (default decidido pelo engine). |

#### `processos_get_resultado`

Polling de um job de busca (de processos_buscar_por_nome/documento). _(POST /api/jus/processos/get/resultado)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `job_id` | string | Sim | ID do job retornado por processos_buscar_por_nome/documento. |
| `job_ids` | string[] | Não | Bulk mode: multiple values for job_id |

#### `processos_obter_pecas`

DOWNLOAD das DECISÕES PÚBLICAS de um processo (acórdãos/inteiro teor): busca as decisões públicas do processo, baixa o PDF e converte em Markdown (o teor da decisão), com link temporário. _(POST /api/jus/processos/obter/pecas)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_cnj` | string | Sim | Número CNJ completo do processo (20 dígitos, com ou sem máscara). |
| `tribunal` | string | Não | Sigla do tribunal (ex.: tjsp), ajuda a rotear o portal certo. Opcional. |
| `peca_ids` | string[] | Não | Restringe a peças específicas (ids vindos de um resultado anterior). Vazio = todas as peças públicas. |
| `formato` | string | Não | markdown (default, texto da peça) ou pdf (só o link do arquivo). (markdown, pdf) |

#### `querido_diario_buscar`

Busca em diários oficiais MUNICIPAIS (milhares de prefeituras) por termo/nome — útil pra menções fora do Judiciário: licitações, nomeações, contratos, sanções municipais. _(POST /api/jus/querido/diario/buscar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Sim | Termo/nome a buscar (ex.: "Fulano de Tal" ou "licitação saúde"). |
| `territory_ids` | string[] | Não | Códigos IBGE de municípios a restringir (vazio = todos). |
| `data_inicio` | string | Não | Publicado desde (AAAA-MM-DD). |
| `data_fim` | string | Não | Publicado até (AAAA-MM-DD). |
| `size` | integer | Não | Resultados (default 10, máx 50). |

#### `tcu_acordaos_recentes`

Lista os acórdãos mais recentes do TCU (dados abertos oficiais), paginado, sem palavra-chave: sumário, relator, colegiado, data da sessão e links. _(POST /api/jus/tcu/acordaos/recentes)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `inicio` | integer | Não | Offset de paginação (default 0). |
| `quantidade` | integer | Não | Quantidade (default 10, máx 50). |

#### `tcu_buscar`

Busca textual (por palavra-chave) na jurisprudência do TCU. _(POST /api/jus/tcu/buscar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Sim | Palavra-chave/tema (ex.: 'fraude em licitação', 'dispensa indevida'). |
| `base` | string | Não | Base a pesquisar. Default 'acordaos'. (acordaos, jurisprudencia, sumulas) |
| `inicio` | integer | Não | Offset de paginação (default 0). |
| `tamanho` | integer | Não | Quantidade por página (default 10, máx 50). |

#### `transparencia_despesas_documentos`

Documentos de despesa (Empenho, Liquidação ou Pagamento) emitidos pelo Governo Federal para um favorecido (CPF/CNPJ) num ano, item-a-item: data, documento, espécie, valor, órgão, elemento de despesa e _(POST /api/jus/transparencia/despesas/documentos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf_cnpj` | string | Sim | CPF (11) ou CNPJ (14) do favorecido, com ou sem máscara. |
| `ano` | integer | Não | Ano de emissão (AAAA). Opcional (default: ano atual). |
| `fase` | string | Não | Fase da despesa. Default 'pagamento'. (empenho, liquidacao, pagamento) |
| `ordenacao` | integer | Não | 1=valor asc, 2=valor desc (default), 3=data asc, 4=data desc. |
| `pagina` | integer | Não | Página (1-based). Default 1. |

#### `transparencia_despesas_favorecido`

DESPESAS recebidas por uma empresa ou pessoa (CPF/CNPJ) do Governo Federal num período: 'quanto a empresa recebeu da União'. _(POST /api/jus/transparencia/despesas/favorecido)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf_cnpj` | string | Sim | CPF (11) ou CNPJ (14) do favorecido, com ou sem máscara. |
| `mes_ano_inicio` | string | Não | Início do período no formato MM/AAAA. Opcional (default: 12 meses atrás). |
| `mes_ano_fim` | string | Não | Fim do período no formato MM/AAAA. Opcional (default: mês atual). |

#### `transparencia_pep`

Verifica se um CPF é de Pessoa Exposta Politicamente (PEP) e retorna função/órgão/período. _(POST /api/jus/transparencia/pep)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Sim | CPF (11 dígitos), com ou sem máscara. |

#### `transparencia_sancoes`

Consulta sanções de uma pessoa ou empresa por CPF/CNPJ no Portal da Transparência (consolida CEIS — inidôneas/suspensas, CNEP — empresas punidas, e CEPIM — entidades impedidas). _(POST /api/jus/transparencia/sancoes)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf_cnpj` | string | Sim | CPF (11) ou CNPJ (14) do sancionado, com ou sem máscara. |

#### `jus_cenprot_sp_protestos_consultar`

CENPROT SP: Protestos, consulta em fonte oficial. _(POST /api/jus/cenprot/sp/protestos/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |

#### `jus_certidoes_cndt`

Consulta a Certidão Negativa de Débitos Trabalhistas (CNDT) por CNPJ ou CPF. _(POST /api/jus/certidoes/cndt)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Não | CNPJ (informe cnpj OU cpf). |
| `cpf` | string | Não | CPF (informe cnpj OU cpf). |

#### `jus_certidoes_fgts`

Consulta a regularidade do empregador perante o FGTS (Certificado de Regularidade — CRF) por CNPJ. _(POST /api/jus/certidoes/fgts)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Sim | CNPJ do empregador. |

#### `jus_certidoes_pgfn`

Emite/consulta a Certidão de débitos relativos a Tributos Federais e à Dívida Ativa da União (CND Federal/PGFN) por CNPJ ou CPF. _(POST /api/jus/certidoes/pgfn)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Não | CNPJ (informe cnpj OU cpf). |
| `cpf` | string | Não | CPF (informe cnpj OU cpf). |

#### `jus_cnj_improbidade_consultar`

Conselho Nacional de Justiça: Improbidade Administrativa e Inelegibilidade, consulta em fonte oficial. _(POST /api/jus/cnj/improbidade/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |

#### `jus_cnj_mandados_prisao_consultar`

Conselho Nacional de Justiça: Mandados de Prisão, consulta em fonte oficial. _(POST /api/jus/cnj/mandados/prisao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `nome_mae` | string | Não | Parâmetro de consulta "nome_mae". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |

#### `jus_cnj_seeu_processos_consultar`

Conselho Nacional de Justiça SEEU: Processos, consulta em fonte oficial. _(POST /api/jus/cnj/seeu/processos/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome_parte` | string | Não | Parâmetro de consulta "nome_parte". |
| `nome_mae` | string | Não | Parâmetro de consulta "nome_mae". |
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |

#### `jus_cnj_serventias_extrajud_lista_consultar`

Conselho Nacional de Justiça: Serventias Extrajudiciais (Lista), consulta em fonte oficial. _(POST /api/jus/cnj/serventias/extrajud/lista/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `uf` | string | Sim | Parâmetro de consulta "uf". |
| `municipio` | string | Sim | Parâmetro de consulta "municipio". |

#### `jus_cnj_serventias_extrajudiciais_consultar`

Conselho Nacional de Justiça: Serventias Extrajudiciais (Detalhes), consulta em fonte oficial. _(POST /api/jus/cnj/serventias/extrajudiciais/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cns` | string | Sim | Parâmetro de consulta "cns". |

#### `jus_compliance_antecedentes_civil`

Antecedentes criminais (Polícia Civil) por CPF/nome/UF. _(POST /api/jus/compliance/antecedentes/civil)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `RG` | string | Não | O parâmetro RG pode ser enviado com ou sem formatação. |
| `NOMEMAE` | string | Não | O parâmetro NOMEMAE pode ser enviado com qualquer outro. |
| `NOME` | string | Não | O parâmetro NOME pode ser enviado com qualquer outro. |
| `DATANASCIMENTO` | string | Não | O parâmetro DATANASCIMENTO deve ser fornecido, com ou sem formatação. |
| `GENERO` | string | Não | GENERO |
| `UF` | string | Sim | UF |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_antecedentes_pf`

Antecedentes criminais (Polícia Federal) por CPF/nome. _(POST /api/jus/compliance/antecedentes/pf)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `NOME` | string | Não | O parâmetro NOME deve ser enviado de forma completa. |
| `DATANASCIMENTO` | string | Não | O parâmetro DATANASCIMENTO deve ser enviado nestes formatos: dd/mm/aaaa ou dd-mm-aaaa. |
| `NOMEMAE` | string | Não | O parâmetro NOMEMAE deve ser enviado de forma completa. |
| `NOMEPAI` | string | Não | O parâmetro NOMEPAI deve ser enviado de forma completa. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_antt`

Regularidade de transportadora na ANTT por CPF/CNPJ/RNTRC. _(POST /api/jus/compliance/antt)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `RNTRC` | string | Não | O parâmetro RNTRC é um conjunto de 9 números. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_bacen_inabilitados`

Banco Central — quadro geral de inabilitados, por CPF/CNPJ. _(POST /api/jus/compliance/bacen/inabilitados)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_bacen_proibidos`

Banco Central — quadro geral de proibidos, por CPF/CNPJ. _(POST /api/jus/compliance/bacen/proibidos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_cadin`

CADIN estadual (inadimplentes com a Fazenda) por CPF/CNPJ/UF. _(POST /api/jus/compliance/cadin)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `UF` | string | Não | UF |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_carf`

Processos no CARF (Conselho Administrativo de Recursos Fiscais) por CPF/CNPJ. _(POST /api/jus/compliance/carf)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_ceaf`

CEAF — expulsões da administração federal, por CPF. _(POST /api/jus/compliance/ceaf)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_ceis`

CEIS — empresas inidôneas e suspensas, por CNPJ/CPF. _(POST /api/jus/compliance/ceis)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_cepim`

CEPIM — entidades privadas impedidas, por CNPJ. _(POST /api/jus/compliance/cepim)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_cgu`

Consulta de penalidades CGU por CPF/CNPJ. _(POST /api/jus/compliance/cgu)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `TIPO` | string | Sim | O parâmetro TIPO deve ser escolhido. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_cnd_municipal`

Certidão Negativa de Débitos Municipal por CNPJ/CPF (informe o município). _(POST /api/jus/compliance/cnd/municipal)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `IM` | string | Não | O parâmetro IM (Inscrição Municipal) pode ser enviado com ou sem formatação. |
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `MUNICIPIO` | string | Sim | O parâmetro MUNICIPIO deve ser informado juntamente com a Unidade Federativa (MUNICIPIO-UF). |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_cnep`

CNEP — empresas punidas, por CNPJ/CPF. _(POST /api/jus/compliance/cnep)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_confea_crea`

Registro profissional no CONFEA/CREA (engenharia/agronomia). _(POST /api/jus/compliance/confea/crea)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `REGISTRONACIONAL` | string | Não | O parâmetro REGISTRONACIONAL pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_cvm`

Cadastro na CVM (Comissão de Valores Mobiliários) por CPF/CNPJ. _(POST /api/jus/compliance/cvm)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_cvm_sancionadores`

Processos administrativos sancionadores da CVM por CPF/CNPJ. _(POST /api/jus/compliance/cvm/sancionadores)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_fbi`

Busca na lista FBI Most Wanted por nome. _(POST /api/jus/compliance/fbi)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NOME` | string | Não | O parâmetro NOME pode ser enviado em maiúsculo ou minúsculo. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_fincen`

Busca na lista FINCEN por nome. _(POST /api/jus/compliance/fincen)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NOME` | string | Não | O parâmetro NOME pode ser enviado em maiúsculo ou minúsculo. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_ibama_debitos`

Certidão negativa de débitos do IBAMA por CPF/CNPJ. _(POST /api/jus/compliance/ibama/debitos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_improbidade`

CNIA — condenações por improbidade administrativa e inelegibilidade, por CNPJ/CPF. _(POST /api/jus/compliance/improbidade)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_interpol`

Busca na lista da INTERPOL por nome. _(POST /api/jus/compliance/interpol)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NOME` | string | Não | O parâmetro NOME pode ser enviado em maiúsculo ou minúsculo. |
| `SOBRENOME` | string | Não | O parâmetro SOBRENOME pode ser enviado em maiúsculo ou minúsculo. |
| `DATANASCIMENTO` | string | Não | O parâmetro DATANASCIMENTO deve ser fornecido, com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_leniencia`

Acordos de leniência por CNPJ. _(POST /api/jus/compliance/leniencia)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_mandados_prisao`

CNJ — mandados de prisão em aberto, por CPF/nome. _(POST /api/jus/compliance/mandados/prisao)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `NOME` | string | Não | O parâmetro NOME pode ser enviado com qualquer outro. |
| `NOMEMAE` | string | Não | O parâmetro NOMEMAE pode ser enviado com qualquer outro. |
| `NOMEPAI` | string | Não | O parâmetro NOMEPAI pode ser enviado com qualquer outro. |
| `ALCUNHA` | string | Não | O parâmetro ALCUNHA pode ser enviado com qualquer outro. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_ofac`

Busca em listas de sanções OFAC (EUA) por nome. _(POST /api/jus/compliance/ofac)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NOME` | string | Não | O parâmetro NOME pode ser enviado em maiúsculo ou minúsculo. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_onu`

Busca na lista consolidada de sanções da ONU por nome. _(POST /api/jus/compliance/onu)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NOME` | string | Não | O parâmetro NOME pode ser enviado em maiúsculo ou minúsculo. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_pep`

Verifica se um CPF é Pessoa Exposta Politicamente (PEP). _(POST /api/jus/compliance/pep)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_pep_parentescos`

PEP estendida — pessoa exposta politicamente + parentescos. _(POST /api/jus/compliance/pep/parentescos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_pix`

Antifraude de chave PIX — valida o titular de uma chave PIX. _(POST /api/jus/compliance/pix)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `DOCUMENTO` | string | Sim | O parâmetro DOCUMENTO pode ser enviado com ou sem formatação. |
| `CHAVE` | string | Sim | O parâmetro CHAVE pode ser enviado com qualquer outro. |
| `TIPO` | string | Não | O parâmetro TIPO deve ser enviado. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_trabalho_forcado`

Verificação de empregador em lista de trabalho forçado/escravo, por CNPJ/CPF. _(POST /api/jus/compliance/trabalho/forcado)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_ue`

Busca na lista de sanções financeiras da União Europeia por nome. _(POST /api/jus/compliance/ue)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NOME` | string | Não | O parâmetro NOME pode ser enviado em maiúsculo ou minúsculo. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_compliance_uk`

Busca na lista de sanções do Reino Unido (HM Treasury) por nome. _(POST /api/jus/compliance/uk)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NOME` | string | Não | O parâmetro NOME pode ser enviado com qualquer outro. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_ieptb_protestos_consultar`

IEPTB (CENPROT): Protestos, consulta em fonte oficial. _(POST /api/jus/ieptb/protestos/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `login_cpf` | string | Não | Parâmetro de consulta "login_cpf". |
| `login_senha` | string | Não | Parâmetro de consulta "login_senha". |
| `pkcs12_cert` | string | Não | Parâmetro de consulta "pkcs12_cert". |
| `pkcs12_pass` | string | Não | Parâmetro de consulta "pkcs12_pass". |

#### `jus_ieptb_protestos_detalhes_sp_consultar`

IEPTB (CENPROT) Protestos: Detalhes SP, consulta em fonte oficial. _(POST /api/jus/ieptb/protestos/detalhes/sp/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `obter_detalhes` | string | Sim | Parâmetro de consulta "obter_detalhes". |
| `login_cpf` | string | Não | Parâmetro de consulta "login_cpf". |
| `login_senha` | string | Não | Parâmetro de consulta "login_senha". |
| `pkcs12_cert` | string | Não | Parâmetro de consulta "pkcs12_cert". |
| `pkcs12_pass` | string | Não | Parâmetro de consulta "pkcs12_pass". |

#### `jus_inpi_marcas_busca`

Busca marcas no INPI pelo nome/termo (anterioridade/colidência). _(POST /api/jus/inpi/marcas/busca)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `marca` | string | Sim | Nome/termo da marca a buscar. |
| `ncl` | string | Não | Classe de Nice (NCL), ex.: 35. Opcional, restringe a busca à classe. |
| `pesquisa_textual` | string | Não | Tipo de pesquisa textual: exata ou radical (raiz do termo). Opcional. |
| `pedidos_vivos` | string | Não | Restringe a processos vivos (não extintos/arquivados). Opcional. |
| `tipo` | string | Não | Tipo de busca/apresentação da marca. Opcional. |
| `pagina` | string | Não | Página de resultados (paginação). Opcional. |

#### `jus_inpi_marcas_processo`

Detalhes completos de um processo de registro de marca no INPI pelo número do processo (situação, depósito, concessão, vigência, titulares, classes Nice/Viena, petições, publicações). _(POST /api/jus/inpi/marcas/processo)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Número do processo da marca no INPI. |

#### `jus_inpi_marcas_processo_resumido`

Resumo de um processo de registro de marca no INPI pelo número do processo (marca, titular, classe, situação). _(POST /api/jus/inpi/marcas/processo/resumido)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Número do processo da marca no INPI. |

#### `jus_inpi_marcas_titular`

Marcas registradas no INPI por titular (CPF ou CNPJ). _(POST /api/jus/inpi/marcas/titular)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Não | CNPJ do titular (informe cnpj OU cpf). |
| `cpf` | string | Não | CPF do titular (informe cnpj OU cpf). |

#### `jus_inpi_patentes`

Patentes registradas no INPI por titular (CPF ou CNPJ). _(POST /api/jus/inpi/patentes)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Não | CNPJ do titular (informe cnpj OU cpf). |
| `cpf` | string | Não | CPF do titular (informe cnpj OU cpf). |

#### `jus_investigacao_aml`

Rede de vínculos societários para prevenção à lavagem de dinheiro, por CPF. _(POST /api/jus/investigacao/aml)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_beneficiario_final`

Beneficiário final (UBO) de uma empresa ou pessoa. _(POST /api/jus/investigacao/beneficiario/final)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_beneficios_sociais`

Benefícios sociais recebidos por um CPF (Bolsa Família, BPC, etc.). _(POST /api/jus/investigacao/beneficios/sociais)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_cnh`

Dados da CNH (Carteira Nacional de Habilitação) por CPF. _(POST /api/jus/investigacao/cnh)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_enriquecimento`

Descobre a pessoa por trás de um celular e/ou email (enriquecimento reverso). _(POST /api/jus/investigacao/enriquecimento)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CELULAR` | string | Não | O parâmetro CELULAR pode ser enviado com ou sem formatação. |
| `EMAIL` | string | Não | O parâmetro EMAIL deve possuir formatação válida. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_historico_veicular`

Histórico veicular (SP) por CPF ou CNPJ. _(POST /api/jus/investigacao/historico/veicular)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_localizacao`

Localização de uma pessoa (nome, endereço, telefone, email). _(POST /api/jus/investigacao/localizacao)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. Este parâmetro não é obrigatório, mas caso não utilizado, enviar os parâmetros 'NAME', 'SURNAME' e 'DOB'. |
| `NAME` | string | Não | O parâmetro NAME pode ser enviado com qualquer outro. |
| `SURNAME` | string | Não | O parâmetro SURNAME pode ser enviado com qualquer outro. |
| `DOB` | string | Não | DATA DE NASCIMENTO - Ex: yyyy/MM/dd. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_obito`

Verificação de óbito por CPF. _(POST /api/jus/investigacao/obito)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_participacoes`

QSA + participações societárias de um CNPJ (sócios e empresas ligadas). _(POST /api/jus/investigacao/participacoes)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_pessoa_fisica`

Dados cadastrais completos de um CPF: nome, contato (telefone/email), endereço, renda estimada e faixa salarial. _(POST /api/jus/investigacao/pessoa/fisica)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_pessoa_juridica`

Dados cadastrais completos de um CNPJ. _(POST /api/jus/investigacao/pessoa/juridica)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_pis`

PIS vinculado a um CPF. _(POST /api/jus/investigacao/pis)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_prf_infracoes`

Infrações da Polícia Rodoviária Federal por placa + RENAVAM. _(POST /api/jus/investigacao/prf/infracoes)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `PLACA` | string | Sim | O parâmetro PLACA pode ser enviado com ou sem formatação. |
| `RENAVAM` | string | Sim | O parâmetro RENAVAM deve ser informado juntamente com seus 11 dígitos numéricos. |
| `TIPO` | string | Sim | O parâmetro TIPO deve ser escolhido. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_propriedade_veicular`

Veículos no nome de uma pessoa ou empresa (frota) por CPF/CNPJ. _(POST /api/jus/investigacao/propriedade/veicular)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_renda`

Nível socioeconômico e renda estimada de um CPF. _(POST /api/jus/investigacao/renda)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_situacao_eleitoral`

Situação eleitoral de uma pessoa (TSE). _(POST /api/jus/investigacao/situacao/eleitoral)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NOME` | string | Não | O parâmetro NOME deve ser enviado de forma completa. Caso informado, enviar também DATANASCIMENTO nestes formatos: dd/mm/aaaa ou dd-mm-aaaa. |
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `NUMEROTITULOELEITORAL` | string | Não | O parâmetro NUMEROTITULOELEITORAL pode ser enviado com ou sem formatação. |
| `DATANASCIMENTO` | string | Não | O parâmetro DATANASCIMENTO deve ser enviado nestes formatos: dd/mm/aaaa ou dd-mm-aaaa. Caso informado, enviar também NOME de forma completa. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_titulo_eleitoral`

Título e local de votação (TSE). _(POST /api/jus/investigacao/titulo/eleitoral)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NOME` | string | Não | O parâmetro NOME deve ser enviado de forma completa. |
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `NUMEROTITULOELEITORAL` | string | Não | O parâmetro NUMEROTITULOELEITORAL pode ser enviado com ou sem formatação. |
| `DATANASCIMENTO` | string | Sim | O parâmetro DATANASCIMENTO deve ser enviado nestes formatos: dd/mm/aaaa ou dd-mm-aaaa. |
| `NOMEMAE` | string | Sim | O parâmetro NOMEMAE deve ser enviado de forma completa. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_veiculo_placa`

Dados e débitos de um veículo pela placa (não exige RENAVAM). _(POST /api/jus/investigacao/veiculo/placa)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `PLACA` | string | Não | O parâmetro PLACA pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_vinculo_empregaticio`

Vínculos empregatícios. _(POST /api/jus/investigacao/vinculo/empregaticio)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_investigacao_vinculos_societarios`

Vínculos/relacionamentos societários de uma pessoa ou empresa. _(POST /api/jus/investigacao/vinculos/societarios)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CNPJ` | string | Não | O parâmetro CNPJ pode ser enviado com ou sem formatação. |
| `CPF` | string | Não | O parâmetro CPF pode ser enviado com ou sem formatação. |
| `completo` | boolean | Não | Opcional. Por padrão (false) listas longas vêm resumidas aos primeiros itens, com a contagem total preservada. Use true para a resposta COMPLETA na mesma consulta. |

#### `jus_mp_sp_inquerito_civil_consultar`

Ministério Público SP: Inquérito Civil, consulta em fonte oficial. _(POST /api/jus/mp/sp/inquerito/civil/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `nome_exato` | string | Não | Parâmetro de consulta "nome_exato". |
| `pagina` | string | Não | Parâmetro de consulta "pagina". |
| `numero_mp` | string | Não | Parâmetro de consulta "numero_mp". |

#### `jus_mpf_amazonia_protege_consultar`

MPF: Amazônia Protege, consulta em fonte oficial. _(POST /api/jus/mpf/amazonia/protege/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |

#### `jus_mpf_certidao_negativa_consultar`

MPF: Certidão Negativa, consulta em fonte oficial. _(POST /api/jus/mpf/certidao/negativa/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |

#### `jus_mpf_processos_consultar`

MPF: Processos, consulta em fonte oficial. _(POST /api/jus/mpf/processos/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `query` | string | Sim | Parâmetro de consulta "query". |

#### `jus_mpt_ac_cnf_consultar`

MPT AC e RO: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/ac/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_al_cnf_consultar`

MPT AL: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/al/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_am_cnf_consultar`

MPT AM e RR: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/am/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_ap_cnf_consultar`

MPT AP e PA: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/ap/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_ba_cnf_consultar`

MPT BA: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/ba/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_ce_cnf_consultar`

MPT CE: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/ce/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_cnf_unificada_consultar`

MPT Unificada: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/cnf/unificada/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `uf` | string | Sim | Parâmetro de consulta "uf". |

#### `jus_mpt_df_cnf_consultar`

MPT DF e TO: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/df/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_es_cnf_consultar`

MPT ES: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/es/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_go_cnf_consultar`

MPT GO: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/go/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_ma_cnf_consultar`

MPT MA: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/ma/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_mg_cnf_consultar`

MPT MG: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/mg/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_ms_cnf_consultar`

MPT MS: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/ms/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_mt_cnf_consultar`

MPT MT: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/mt/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_pb_cnf_consultar`

MPT PB: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/pb/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_pe_cnf_consultar`

MPT PE: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/pe/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_pi_cnf_consultar`

MPT PI: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/pi/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_pr_cnf_consultar`

MPT PR: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/pr/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_rj_cnf_consultar`

MPT RJ: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/rj/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_rn_cnf_consultar`

MPT RN: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/rn/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_rs_cnf_consultar`

MPT RS: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/rs/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_sc_cnf_consultar`

MPT SC: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/sc/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_se_cnf_consultar`

MPT SE: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/se/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_sp_campinas_cnf_consultar`

MPT SP Campinas: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/sp/campinas/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_mpt_sp_cnf_consultar`

MPT SP: Certidão Negativa de Feitos, consulta em fonte oficial. _(POST /api/jus/mpt/sp/cnf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_onr_mapa_registro_imoveis_consultar`

ONR: Mapa do Registro de Imóveis, consulta em fonte oficial. _(POST /api/jus/onr/mapa/registro/imoveis/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `camada` | string | Sim | Parâmetro de consulta "camada". |
| `hash_endereco` | string | Não | Parâmetro de consulta "hash_endereco". |
| `car` | string | Não | Parâmetro de consulta "car". |

#### `jus_registradores_certid_download_consultar`

Registradores (ARISP) Certidão: Download de Certidão Digital, consulta em fonte oficial. _(POST /api/jus/registradores/certid/download/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `email` | string | Não | Parâmetro de consulta "email". |
| `senha` | string | Não | Parâmetro de consulta "senha". |
| `pkcs12_cert` | string | Não | Parâmetro de consulta "pkcs12_cert". |
| `pkcs12_pass` | string | Não | Parâmetro de consulta "pkcs12_pass". |
| `tipo_login` | string | Não | Parâmetro de consulta "tipo_login". |
| `numero_pedido` | string | Não | Parâmetro de consulta "numero_pedido". |

#### `jus_registradores_certid_pedido_consultar`

Registradores (ARISP) Certidão: Novo Pedido de Certidão Digital, consulta em fonte oficial. _(POST /api/jus/registradores/certid/pedido/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `email` | string | Não | Parâmetro de consulta "email". |
| `senha` | string | Não | Parâmetro de consulta "senha". |
| `pkcs12_cert` | string | Não | Parâmetro de consulta "pkcs12_cert". |
| `pkcs12_pass` | string | Não | Parâmetro de consulta "pkcs12_pass". |
| `tipo_login` | string | Não | Parâmetro de consulta "tipo_login". |
| `uf` | string | Sim | Parâmetro de consulta "uf". |
| `municipio` | string | Sim | Parâmetro de consulta "municipio". |
| `cartorio` | string | Sim | Parâmetro de consulta "cartorio". |
| `tipo_certidao` | string | Sim | Parâmetro de consulta "tipo_certidao". |
| `matricula` | string | Sim | Parâmetro de consulta "matricula". |

#### `jus_registradores_certid_recibo_consultar`

Registradores (ARISP) Certidão: Download de Recibo, consulta em fonte oficial. _(POST /api/jus/registradores/certid/recibo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `email` | string | Não | Parâmetro de consulta "email". |
| `senha` | string | Não | Parâmetro de consulta "senha". |
| `pkcs12_cert` | string | Não | Parâmetro de consulta "pkcs12_cert". |
| `pkcs12_pass` | string | Não | Parâmetro de consulta "pkcs12_pass". |
| `tipo_login` | string | Não | Parâmetro de consulta "tipo_login". |
| `numero_pedido` | string | Não | Parâmetro de consulta "numero_pedido". |

#### `jus_registradores_info_conta_consultar`

Registradores (ARISP): Consulta de Informações da Conta, consulta em fonte oficial. _(POST /api/jus/registradores/info/conta/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `email` | string | Não | Parâmetro de consulta "email". |
| `senha` | string | Não | Parâmetro de consulta "senha". |
| `pkcs12_cert` | string | Não | Parâmetro de consulta "pkcs12_cert". |
| `pkcs12_pass` | string | Não | Parâmetro de consulta "pkcs12_pass". |
| `tipo_login` | string | Não | Parâmetro de consulta "tipo_login". |

#### `jus_registradores_matric_download_consultar`

Registradores (ARISP) Matrícula: Download de Matrícula, consulta em fonte oficial. _(POST /api/jus/registradores/matric/download/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `email` | string | Não | Parâmetro de consulta "email". |
| `senha` | string | Não | Parâmetro de consulta "senha". |
| `pkcs12_cert` | string | Não | Parâmetro de consulta "pkcs12_cert". |
| `pkcs12_pass` | string | Não | Parâmetro de consulta "pkcs12_pass". |
| `tipo_login` | string | Não | Parâmetro de consulta "tipo_login". |
| `numero_pedido` | string | Não | Parâmetro de consulta "numero_pedido". |

#### `jus_registradores_matric_lista_consultar`

Registradores (ARISP) Matrícula: Lista de Pedidos, consulta em fonte oficial. _(POST /api/jus/registradores/matric/lista/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `email` | string | Não | Parâmetro de consulta "email". |
| `senha` | string | Não | Parâmetro de consulta "senha". |
| `pkcs12_cert` | string | Não | Parâmetro de consulta "pkcs12_cert". |
| `pkcs12_pass` | string | Não | Parâmetro de consulta "pkcs12_pass". |
| `tipo_login` | string | Não | Parâmetro de consulta "tipo_login". |

#### `jus_registradores_matric_pedido_consultar`

Registradores (ARISP) Matrícula: Novo Pedido de Visualização de Matrícula, consulta em fonte oficial. _(POST /api/jus/registradores/matric/pedido/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `email` | string | Não | Parâmetro de consulta "email". |
| `senha` | string | Não | Parâmetro de consulta "senha". |
| `pkcs12_cert` | string | Não | Parâmetro de consulta "pkcs12_cert". |
| `pkcs12_pass` | string | Não | Parâmetro de consulta "pkcs12_pass". |
| `tipo_login` | string | Não | Parâmetro de consulta "tipo_login". |
| `matricula` | string | Sim | Parâmetro de consulta "matricula". |
| `uf` | string | Sim | Parâmetro de consulta "uf". |
| `municipio` | string | Sim | Parâmetro de consulta "municipio". |
| `cartorio` | string | Sim | Parâmetro de consulta "cartorio". |
| `finalidade` | string | Sim | Parâmetro de consulta "finalidade". |

#### `jus_registradores_matric_recibo_consultar`

Registradores (ARISP) Matrícula: Download de Recibo, consulta em fonte oficial. _(POST /api/jus/registradores/matric/recibo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `email` | string | Não | Parâmetro de consulta "email". |
| `senha` | string | Não | Parâmetro de consulta "senha". |
| `pkcs12_cert` | string | Não | Parâmetro de consulta "pkcs12_cert". |
| `pkcs12_pass` | string | Não | Parâmetro de consulta "pkcs12_pass". |
| `tipo_login` | string | Não | Parâmetro de consulta "tipo_login". |
| `numero_pedido` | string | Não | Parâmetro de consulta "numero_pedido". |

#### `jus_registro_civil_val_cert_eletr_consultar`

Registro Civil: Validar Certidão Eletrônica, consulta em fonte oficial. _(POST /api/jus/registro/civil/val/cert/eletr/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_certidao` | string | Sim | Parâmetro de consulta "codigo_certidao". |

#### `jus_tribunal_stj_certidao_negativa_consultar`

Tribunal STJ: Certidão Negativa, consulta em fonte oficial. _(POST /api/jus/tribunal/stj/certidao/negativa/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_tjba_primeiro_grau_consultar`

Tribunal TJBA: Certidão do 1º Grau, consulta em fonte oficial. _(POST /api/jus/tribunal/tjba/primeiro/grau/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `naturalidade` | string | Não | Parâmetro de consulta "naturalidade". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `rg` | string | Não | Parâmetro de consulta "rg". |
| `orgao_expedidor` | string | Não | Parâmetro de consulta "orgao_expedidor". |
| `estado_civil` | string | Não | Parâmetro de consulta "estado_civil". |
| `endereco` | string | Não | Parâmetro de consulta "endereco". |
| `filiacao_1` | string | Não | Parâmetro de consulta "filiacao_1". |
| `razao_social` | string | Não | Parâmetro de consulta "razao_social". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `tipo_certidao` | string | Não | Parâmetro de consulta "tipo_certidao". |
| `tipo_participacao` | string | Não | Parâmetro de consulta "tipo_participacao". |

#### `jus_tribunal_tjdf_nada_consta_consultar`

Tribunal TJDF: Nada Consta, consulta em fonte oficial. _(POST /api/jus/tribunal/tjdf/nada/consta/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `primeiro_nome` | string | Não | Parâmetro de consulta "primeiro_nome". |
| `nome_mae` | string | Não | Parâmetro de consulta "nome_mae". |
| `nome_pai` | string | Não | Parâmetro de consulta "nome_pai". |
| `tipo_certidao` | string | Sim | Parâmetro de consulta "tipo_certidao". |

#### `jus_tribunal_tjgo_nada_consta_consultar`

Tribunal TJGO: Nada Consta, consulta em fonte oficial. _(POST /api/jus/tribunal/tjgo/nada/consta/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipo_certidao` | string | Sim | Parâmetro de consulta "tipo_certidao". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `razao_social` | string | Não | Parâmetro de consulta "razao_social". |
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `nome_mae` | string | Não | Parâmetro de consulta "nome_mae". |
| `birthdate` | string | Não | Parâmetro de consulta "birthdate". |

#### `jus_tribunal_tjma_nada_consta_consultar`

Tribunal TJMA: Nada Consta, consulta em fonte oficial. _(POST /api/jus/tribunal/tjma/nada/consta/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `instancia` | string | Sim | Parâmetro de consulta "instancia". |
| `natureza` | string | Sim | Parâmetro de consulta "natureza". |
| `cpf` | string | Sim | Parâmetro de consulta "cpf". |
| `nome` | string | Sim | Parâmetro de consulta "nome". |
| `birthdate` | string | Sim | Parâmetro de consulta "birthdate". |
| `nome_mae` | string | Sim | Parâmetro de consulta "nome_mae". |
| `nome_pai` | string | Não | Parâmetro de consulta "nome_pai". |

#### `jus_tribunal_tjmg_processo_consultar`

Tribunal TJMG: Processo, consulta em fonte oficial. _(POST /api/jus/tribunal/tjmg/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome_parte` | string | Não | Parâmetro de consulta "nome_parte". |
| `nome_advogado` | string | Não | Parâmetro de consulta "nome_advogado". |

#### `jus_tribunal_tjms_obter_certidao_consultar`

Tribunal TJMS: Conferência de Certidão, consulta em fonte oficial. _(POST /api/jus/tribunal/tjms/obter/certidao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_pedido` | string | Sim | Parâmetro de consulta "numero_pedido". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `data_pedido` | string | Sim | Parâmetro de consulta "data_pedido". |

#### `jus_tribunal_tjms_pedido_cert_consultar`

Tribunal TJMS: Cadastro de Pedido de Certidão (1º grau), consulta em fonte oficial. _(POST /api/jus/tribunal/tjms/pedido/cert/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `comarca` | string | Sim | Parâmetro de consulta "comarca". |
| `modelo` | string | Sim | Parâmetro de consulta "modelo". |
| `nome_razao_social` | string | Sim | Parâmetro de consulta "nome_razao_social". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `rg` | string | Não | Parâmetro de consulta "rg". |
| `genero` | string | Não | Parâmetro de consulta "genero". |
| `nome_pai` | string | Não | Parâmetro de consulta "nome_pai". |
| `nome_mae` | string | Não | Parâmetro de consulta "nome_mae". |
| `birthdate` | string | Não | Parâmetro de consulta "birthdate". |
| `email` | string | Sim | Parâmetro de consulta "email". |

#### `jus_tribunal_tjmt_primeiro_grau_pf_consultar`

Tribunal TJMT: Certidão do 1º Grau (Pessoa Física), consulta em fonte oficial. _(POST /api/jus/tribunal/tjmt/primeiro/grau/pf/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Sim | Parâmetro de consulta "cpf". |
| `birthdate` | string | Sim | Parâmetro de consulta "birthdate". |
| `tipo_certidao` | string | Sim | Parâmetro de consulta "tipo_certidao". |

#### `jus_tribunal_tjpa_cert_criminal_consultar`

Tribunal TJPA: Certidão Criminal, consulta em fonte oficial. _(POST /api/jus/tribunal/tjpa/cert/criminal/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome_requerente` | string | Sim | Parâmetro de consulta "nome_requerente". |
| `nome_mae` | string | Sim | Parâmetro de consulta "nome_mae". |
| `endereco` | string | Sim | Parâmetro de consulta "endereco". |
| `rg` | string | Não | Parâmetro de consulta "rg". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `orgao_emissor_rg` | string | Não | Parâmetro de consulta "orgao_emissor_rg". |
| `uf_emissor_rg` | string | Não | Parâmetro de consulta "uf_emissor_rg". |

#### `jus_tribunal_tjpr_processo_consultar`

Tribunal TJPR: Processo, consulta em fonte oficial. _(POST /api/jus/tribunal/tjpr/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |
| `nome_juizo` | string | Não | Parâmetro de consulta "nome_juizo". |
| `instancia` | string | Não | Parâmetro de consulta "instancia". |
| `tipo_competencia` | string | Não | Parâmetro de consulta "tipo_competencia". |
| `orgao_julgador` | string | Não | Parâmetro de consulta "orgao_julgador". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome_comarca` | string | Não | Parâmetro de consulta "nome_comarca". |
| `nome_parte` | string | Não | Parâmetro de consulta "nome_parte". |
| `nome_advogado` | string | Não | Parâmetro de consulta "nome_advogado". |
| `oab` | string | Não | Parâmetro de consulta "oab". |
| `oab_complemento` | string | Não | Parâmetro de consulta "oab_complemento". |
| `oab_uf` | string | Não | Parâmetro de consulta "oab_uf". |

#### `jus_tribunal_tjrj_obter_certidao_consultar`

Tribunal TJRJ: Visualizar Certidão, consulta em fonte oficial. _(POST /api/jus/tribunal/tjrj/obter/certidao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_requerimento` | string | Sim | Parâmetro de consulta "numero_requerimento". |

#### `jus_tribunal_tjrj_pedido_cert_consultar`

Tribunal TJRJ: Cadastro de Pedido de Certidão, consulta em fonte oficial. _(POST /api/jus/tribunal/tjrj/pedido/cert/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Sim | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `email` | string | Sim | Parâmetro de consulta "email". |
| `tipo_certidao` | string | Sim | Parâmetro de consulta "tipo_certidao". |
| `comarca` | string | Sim | Parâmetro de consulta "comarca". |
| `finalidade` | string | Sim | Parâmetro de consulta "finalidade". |
| `inscricao_imovel` | string | Não | Parâmetro de consulta "inscricao_imovel". |
| `endereco` | string | Não | Parâmetro de consulta "endereco". |
| `numero_endereco` | string | Não | Parâmetro de consulta "numero_endereco". |
| `complemento_endereco` | string | Não | Parâmetro de consulta "complemento_endereco". |
| `bairro` | string | Não | Parâmetro de consulta "bairro". |

#### `jus_tribunal_tjrj_processo_consultar`

Tribunal TJRJ: Processo, consulta em fonte oficial. _(POST /api/jus/tribunal/tjrj/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `oab` | string | Não | Parâmetro de consulta "oab". |
| `nome_advogado` | string | Não | Parâmetro de consulta "nome_advogado". |
| `origem` | string | Não | Parâmetro de consulta "origem". |
| `comarca_regional` | string | Não | Parâmetro de consulta "comarca_regional". |
| `competencia` | string | Não | Parâmetro de consulta "competencia". |
| `ano_inicial` | string | Não | Parâmetro de consulta "ano_inicial". |
| `ano_final` | string | Não | Parâmetro de consulta "ano_final". |
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |

#### `jus_tribunal_tjrj_processo_eproc_consultar`

Tribunal TJRJ: Processo (eproc), consulta em fonte oficial. _(POST /api/jus/tribunal/tjrj/processo/eproc/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `oab` | string | Não | Parâmetro de consulta "oab". |

#### `jus_tribunal_tjrs_primeiro_grau_consultar`

Tribunal TJRS: Certidão do 1º Grau, consulta em fonte oficial. _(POST /api/jus/tribunal/tjrs/primeiro/grau/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipo_certidao` | string | Sim | Parâmetro de consulta "tipo_certidao". |
| `nacionalidade` | string | Não | Parâmetro de consulta "nacionalidade". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `rg` | string | Não | Parâmetro de consulta "rg". |
| `orgao_expedidor_rg` | string | Não | Parâmetro de consulta "orgao_expedidor_rg". |
| `uf_rg` | string | Não | Parâmetro de consulta "uf_rg". |
| `genero` | string | Não | Parâmetro de consulta "genero". |
| `nome_mae` | string | Não | Parâmetro de consulta "nome_mae". |
| `nome_pai` | string | Não | Parâmetro de consulta "nome_pai". |
| `birthdate` | string | Não | Parâmetro de consulta "birthdate". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `estado_civil` | string | Não | Parâmetro de consulta "estado_civil". |
| `nome` | string | Sim | Parâmetro de consulta "nome". |
| `endereco` | string | Sim | Parâmetro de consulta "endereco". |

#### `jus_tribunal_tjsc_obter_certidao_consultar`

Tribunal TJSC: Visualizar Certidão, consulta em fonte oficial. _(POST /api/jus/tribunal/tjsc/obter/certidao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `numero_pedido` | string | Sim | Parâmetro de consulta "numero_pedido". |

#### `jus_tribunal_tjsc_pedido_certidao_consultar`

Tribunal TJSC: Pedido de Certidão, consulta em fonte oficial. _(POST /api/jus/tribunal/tjsc/pedido/certidao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `instancia` | string | Sim | Parâmetro de consulta "instancia". |
| `tipo` | string | Sim | Parâmetro de consulta "tipo". |
| `finalidade_certidao` | string | Não | Parâmetro de consulta "finalidade_certidao". |
| `nome` | string | Sim | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `rg` | string | Não | Parâmetro de consulta "rg". |
| `orgao_expedidor` | string | Não | Parâmetro de consulta "orgao_expedidor". |
| `uf` | string | Sim | Parâmetro de consulta "uf". |
| `municipio` | string | Sim | Parâmetro de consulta "municipio". |
| `email` | string | Sim | Parâmetro de consulta "email". |
| `nome_mae` | string | Não | Parâmetro de consulta "nome_mae". |
| `nome_pai` | string | Não | Parâmetro de consulta "nome_pai". |
| `birthdate` | string | Não | Parâmetro de consulta "birthdate". |
| `login_cpf` | string | Não | Parâmetro de consulta "login_cpf". |
| `login_senha` | string | Não | Parâmetro de consulta "login_senha". |
| `pkcs12_cert` | string | Não | Parâmetro de consulta "pkcs12_cert". |
| `pkcs12_pass` | string | Não | Parâmetro de consulta "pkcs12_pass". |

#### `jus_tribunal_tjsc_processo_consultar`

Tribunal TJSC: Processo, consulta em fonte oficial. _(POST /api/jus/tribunal/tjsc/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `oab` | string | Não | Parâmetro de consulta "oab". |

#### `jus_tribunal_tjsp_colegio_recursal_consultar`

Tribunal TJSP: Colégio Recursal e Turma de Uniformização, consulta em fonte oficial. _(POST /api/jus/tribunal/tjsp/colegio/recursal/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |
| `nome_parte` | string | Não | Parâmetro de consulta "nome_parte". |
| `rg` | string | Não | Parâmetro de consulta "rg". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `nome_advogado` | string | Não | Parâmetro de consulta "nome_advogado". |
| `oab` | string | Não | Parâmetro de consulta "oab". |
| `secao` | string | Não | Parâmetro de consulta "secao". |
| `pagina` | string | Não | Parâmetro de consulta "pagina". |

#### `jus_tribunal_tjsp_eproc_lista_consultar`

Tribunal TJSP: Lista de Processos (eproc), consulta em fonte oficial. _(POST /api/jus/tribunal/tjsp/eproc/lista/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome_parte` | string | Não | Parâmetro de consulta "nome_parte". |
| `oab` | string | Não | Parâmetro de consulta "oab". |

#### `jus_tribunal_tjsp_eproc_unificada_consultar`

Tribunal TJSP: Consulta Processual Unificada (Eproc), consulta em fonte oficial. _(POST /api/jus/tribunal/tjsp/eproc/unificada/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |

#### `jus_tribunal_tjsp_obter_cert_1grau_consultar`

Tribunal TJSP: Download da Certidão de 1º Grau, consulta em fonte oficial. _(POST /api/jus/tribunal/tjsp/obter/cert/1grau/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `numero_pedido` | string | Sim | Parâmetro de consulta "numero_pedido". |

#### `jus_tribunal_tjsp_obter_certidao_consultar`

Tribunal TJSP: Visualizar Certidão, consulta em fonte oficial. _(POST /api/jus/tribunal/tjsp/obter/certidao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_pedido` | string | Sim | Parâmetro de consulta "numero_pedido". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `pedido_data` | string | Não | Parâmetro de consulta "pedido_data". |

#### `jus_tribunal_tjsp_pedido_certidao_consultar`

Tribunal TJSP: Cadastro de Pedido de Certidão, consulta em fonte oficial. _(POST /api/jus/tribunal/tjsp/pedido/certidao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `modelo` | string | Sim | Parâmetro de consulta "modelo". |
| `email_envio` | string | Sim | Parâmetro de consulta "email_envio". |
| `nome_completo` | string | Não | Parâmetro de consulta "nome_completo". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `rg` | string | Não | Parâmetro de consulta "rg". |
| `cin` | string | Não | Parâmetro de consulta "cin". |
| `razao_social` | string | Não | Parâmetro de consulta "razao_social". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `genero` | string | Não | Parâmetro de consulta "genero". |
| `nome_mae` | string | Não | Parâmetro de consulta "nome_mae". |
| `nome_pai` | string | Não | Parâmetro de consulta "nome_pai". |
| `birthdate` | string | Não | Parâmetro de consulta "birthdate". |
| `naturalidade_municipio` | string | Não | Parâmetro de consulta "naturalidade_municipio". |
| `naturalidade_uf` | string | Não | Parâmetro de consulta "naturalidade_uf". |

#### `jus_tribunal_tjsp_pedido_civel_consultar`

Tribunal TJSP: Certidão Cível de 1º Grau, consulta em fonte oficial. _(POST /api/jus/tribunal/tjsp/pedido/civel/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `razao_social` | string | Não | Parâmetro de consulta "razao_social". |
| `instancia` | string | Não | Parâmetro de consulta "instancia". |
| `email` | string | Sim | Parâmetro de consulta "email". |
| `finalidade` | string | Sim | Parâmetro de consulta "finalidade". |
| `pais` | string | Não | Parâmetro de consulta "pais". |
| `uf` | string | Não | Parâmetro de consulta "uf". |
| `municipio` | string | Não | Parâmetro de consulta "municipio". |
| `login_cpf` | string | Não | Parâmetro de consulta "login_cpf". |
| `login_senha` | string | Não | Parâmetro de consulta "login_senha". |
| `pkcs12_cert` | string | Não | Parâmetro de consulta "pkcs12_cert". |
| `pkcs12_pass` | string | Não | Parâmetro de consulta "pkcs12_pass". |

#### `jus_tribunal_tjsp_pedido_criminal_consultar`

Tribunal TJSP: Certidão Criminal de 1º Grau, consulta em fonte oficial. _(POST /api/jus/tribunal/tjsp/pedido/criminal/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `razao_social` | string | Não | Parâmetro de consulta "razao_social". |
| `email` | string | Sim | Parâmetro de consulta "email". |
| `finalidade` | string | Sim | Parâmetro de consulta "finalidade". |
| `pais` | string | Não | Parâmetro de consulta "pais". |
| `uf` | string | Não | Parâmetro de consulta "uf". |
| `municipio` | string | Não | Parâmetro de consulta "municipio". |
| `login_cpf` | string | Não | Parâmetro de consulta "login_cpf". |
| `login_senha` | string | Não | Parâmetro de consulta "login_senha". |
| `pkcs12_cert` | string | Não | Parâmetro de consulta "pkcs12_cert". |
| `pkcs12_pass` | string | Não | Parâmetro de consulta "pkcs12_pass". |

#### `jus_tribunal_tjsp_primeiro_grau_consultar`

Tribunal TJSP: Processos do 1º Grau, consulta em fonte oficial. _(POST /api/jus/tribunal/tjsp/primeiro/grau/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `processo` | string | Não | Parâmetro de consulta "processo". |
| `parte` | string | Não | Parâmetro de consulta "parte". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `rg` | string | Não | Parâmetro de consulta "rg". |
| `advogado` | string | Não | Parâmetro de consulta "advogado". |
| `oab` | string | Não | Parâmetro de consulta "oab". |
| `carta_precatoria` | string | Não | Parâmetro de consulta "carta_precatoria". |
| `documento_delegacia` | string | Não | Parâmetro de consulta "documento_delegacia". |
| `cda` | string | Não | Parâmetro de consulta "cda". |
| `pagina` | string | Não | Parâmetro de consulta "pagina". |

#### `jus_tribunal_tjsp_segundo_grau_consultar`

Tribunal TJSP: Processos do 2º Grau, consulta em fonte oficial. _(POST /api/jus/tribunal/tjsp/segundo/grau/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |
| `nome_parte` | string | Não | Parâmetro de consulta "nome_parte". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `rg` | string | Não | Parâmetro de consulta "rg". |
| `advogado` | string | Não | Parâmetro de consulta "advogado". |
| `oab` | string | Não | Parâmetro de consulta "oab". |
| `carta_precatoria` | string | Não | Parâmetro de consulta "carta_precatoria". |
| `documento_delegacia` | string | Não | Parâmetro de consulta "documento_delegacia". |
| `pagina` | string | Não | Parâmetro de consulta "pagina". |

#### `jus_tribunal_tjsp_selo_digital_consultar`

Tribunal TJSP: Selo Digital, consulta em fonte oficial. _(POST /api/jus/tribunal/tjsp/selo/digital/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `selo` | string | Sim | Parâmetro de consulta "selo". |

#### `jus_tribunal_tjto_cert_judicial_consultar`

Tribunal TJTO: Certidão Judicial, consulta em fonte oficial. _(POST /api/jus/tribunal/tjto/cert/judicial/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `competencia` | string | Não | Parâmetro de consulta "competencia". |
| `nome` | string | Não | Parâmetro de consulta "nome". |

#### `jus_tribunal_trf_cert_unificada_consultar`

Tribunal TRF: Certidão Unificada da Justiça Federal, consulta em fonte oficial. _(POST /api/jus/tribunal/trf/cert/unificada/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipo` | string | Sim | Parâmetro de consulta "tipo". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome_social` | string | Não | Parâmetro de consulta "nome_social". |
| `email` | string | Sim | Parâmetro de consulta "email". |

#### `jus_tribunal_trf1_certidao_consultar`

Tribunal TRF1: Certidão Negativa Cível e Criminal, consulta em fonte oficial. _(POST /api/jus/tribunal/trf1/certidao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `tipo` | string | Sim | Parâmetro de consulta "tipo". |
| `orgao` | string | Não | Parâmetro de consulta "orgao". |
| `considera_filiais` | string | Não | Parâmetro de consulta "considera_filiais". |

#### `jus_tribunal_trf1_processo_consultar`

Tribunal TRF1: Processo, consulta em fonte oficial. _(POST /api/jus/tribunal/trf1/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `processo` | string | Não | Parâmetro de consulta "processo". |
| `parte` | string | Não | Parâmetro de consulta "parte". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `advogado` | string | Não | Parâmetro de consulta "advogado". |
| `oab` | string | Não | Parâmetro de consulta "oab". |

#### `jus_tribunal_trf2_certidao_consultar`

Tribunal TRF2: Certidão Negativa Cível e Criminal, consulta em fonte oficial. _(POST /api/jus/tribunal/trf2/certidao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `birthdate` | string | Não | Parâmetro de consulta "birthdate". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `tipo_certidao` | string | Sim | Parâmetro de consulta "tipo_certidao". |

#### `jus_tribunal_trf2_processo_consultar`

Tribunal TRF2: Processo, consulta em fonte oficial. _(POST /api/jus/tribunal/trf2/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |
| `oab` | string | Não | Parâmetro de consulta "oab". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome_parte` | string | Não | Parâmetro de consulta "nome_parte". |

#### `jus_tribunal_trf2_processo_eproc_consultar`

Tribunal TRF2: Processo (eproc), consulta em fonte oficial. _(POST /api/jus/tribunal/trf2/processo/eproc/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |
| `oab` | string | Não | Parâmetro de consulta "oab". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome_parte` | string | Não | Parâmetro de consulta "nome_parte". |

#### `jus_tribunal_trf3_certidao_distr_consultar`

Tribunal TRF3: Certidão de Distribuição, consulta em fonte oficial. _(POST /api/jus/tribunal/trf3/certidao/distr/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `abrangencia` | string | Não | Parâmetro de consulta "abrangencia". |
| `tipo` | string | Não | Parâmetro de consulta "tipo". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `razao_social` | string | Não | Parâmetro de consulta "razao_social". |
| `nome_social` | string | Não | Parâmetro de consulta "nome_social". |
| `nome_mae` | string | Não | Parâmetro de consulta "nome_mae". |
| `birthdate` | string | Não | Parâmetro de consulta "birthdate". |
| `tipo_documento` | string | Não | Parâmetro de consulta "tipo_documento". |
| `documento` | string | Não | Parâmetro de consulta "documento". |
| `endereco` | string | Não | Parâmetro de consulta "endereco". |
| `tipo_telefone` | string | Não | Parâmetro de consulta "tipo_telefone". |
| `telefone` | string | Não | Parâmetro de consulta "telefone". |

#### `jus_tribunal_trf3_consulta_publica_consultar`

Tribunal TRF3: Consulta Pública, consulta em fonte oficial. _(POST /api/jus/tribunal/trf3/consulta/publica/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |
| `nome_parte` | string | Não | Parâmetro de consulta "nome_parte". |
| `nome_advogado` | string | Não | Parâmetro de consulta "nome_advogado". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trf3_obter_certidao_consultar`

Tribunal TRF3: Obter Certidão de Distribuição, consulta em fonte oficial. _(POST /api/jus/tribunal/trf3/obter/certidao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `numero_certidao` | string | Sim | Parâmetro de consulta "numero_certidao". |

#### `jus_tribunal_trf3_processo_consultar`

Tribunal TRF3: Processo, consulta em fonte oficial. _(POST /api/jus/tribunal/trf3/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |
| `processo_origem` | string | Não | Parâmetro de consulta "processo_origem". |
| `uf_origem` | string | Não | Parâmetro de consulta "uf_origem". |
| `cidade_origem` | string | Não | Parâmetro de consulta "cidade_origem". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome_parte` | string | Não | Parâmetro de consulta "nome_parte". |
| `oab` | string | Não | Parâmetro de consulta "oab". |
| `nome_advogado` | string | Não | Parâmetro de consulta "nome_advogado". |
| `data_inicio_autuacao` | string | Não | Parâmetro de consulta "data_inicio_autuacao". |
| `data_final_autuacao` | string | Não | Parâmetro de consulta "data_final_autuacao". |

#### `jus_tribunal_trf4_certidao_consultar`

Tribunal TRF4: Certidão Negativa Cível e Criminal, consulta em fonte oficial. _(POST /api/jus/tribunal/trf4/certidao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `birthdate` | string | Não | Parâmetro de consulta "birthdate". |
| `tipo` | string | Sim | Parâmetro de consulta "tipo". |

#### `jus_tribunal_trf5_certidao_consultar`

Tribunal TRF5: Certidão Negativa Cível e Criminal, consulta em fonte oficial. _(POST /api/jus/tribunal/trf5/certidao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipo_certidao` | string | Sim | Parâmetro de consulta "tipo_certidao". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `birthdate` | string | Não | Parâmetro de consulta "birthdate". |
| `orgao` | string | Não | Parâmetro de consulta "orgao". |

#### `jus_tribunal_trf5_processo_consultar`

Tribunal TRF5: Processo, consulta em fonte oficial. _(POST /api/jus/tribunal/trf5/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `processo` | string | Não | Parâmetro de consulta "processo". |
| `originario` | string | Não | Parâmetro de consulta "originario". |
| `parte_advogado` | string | Não | Parâmetro de consulta "parte_advogado". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `oab` | string | Não | Parâmetro de consulta "oab". |
| `oab_uf` | string | Não | Parâmetro de consulta "oab_uf". |

#### `jus_tribunal_trf6_certidao_consultar`

Tribunal TRF6: Certidão Negativa Cível e Criminal, consulta em fonte oficial. _(POST /api/jus/tribunal/trf6/certidao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipo_certidao` | string | Sim | Parâmetro de consulta "tipo_certidao". |
| `orgao` | string | Não | Parâmetro de consulta "orgao". |
| `considera_filiais` | string | Não | Parâmetro de consulta "considera_filiais". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trf6_processo_consultar`

Tribunal TRF6: Processo, consulta em fonte oficial. _(POST /api/jus/tribunal/trf6/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |
| `nome_parte` | string | Não | Parâmetro de consulta "nome_parte". |
| `nome_advogado` | string | Não | Parâmetro de consulta "nome_advogado". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt_processo_consultar`

Tribunal TRT: Consulta Processual Unificada, consulta em fonte oficial. _(POST /api/jus/tribunal/trt/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt1_ceat_consultar`

Tribunal TRT1: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt1/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt1_processo_consultar`

Tribunal TRT1: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt1/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt10_ceat_consultar`

Tribunal TRT10: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt10/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt10_ceat_digital_consultar`

Tribunal TRT10: Certidão Eletrônica de Ações Trabalhistas (CEAT) - Processos Digitais, consulta em fonte oficial. _(POST /api/jus/tribunal/trt10/ceat/digital/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt10_processo_consultar`

Tribunal TRT10: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt10/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt11_ceat_consultar`

Tribunal TRT11: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt11/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt11_processo_consultar`

Tribunal TRT11: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt11/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt12_ceat_consultar`

Tribunal TRT12: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt12/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt12_processo_consultar`

Tribunal TRT12: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt12/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt13_ceat_consultar`

Tribunal TRT13: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt13/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt13_processo_consultar`

Tribunal TRT13: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt13/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt14_ceat_consultar`

Tribunal TRT14: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt14/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt14_processo_consultar`

Tribunal TRT14: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt14/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt15_ceat_consultar`

Tribunal TRT15: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt15/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome` | string | Não | Parâmetro de consulta "nome". |

#### `jus_tribunal_trt15_processo_consultar`

Tribunal TRT15: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt15/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt16_ceat_consultar`

Tribunal TRT16: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt16/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt16_processo_consultar`

Tribunal TRT16: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt16/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt17_ceat_consultar`

Tribunal TRT17: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt17/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome_completo` | string | Não | Parâmetro de consulta "nome_completo". |

#### `jus_tribunal_trt17_processo_consultar`

Tribunal TRT17: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt17/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt18_ceat_consultar`

Tribunal TRT18: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt18/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome_requerente` | string | Sim | Parâmetro de consulta "nome_requerente". |
| `cpf_requerente` | string | Sim | Parâmetro de consulta "cpf_requerente". |

#### `jus_tribunal_trt18_processo_consultar`

Tribunal TRT18: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt18/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt19_ceat_consultar`

Tribunal TRT19: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt19/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt19_processo_consultar`

Tribunal TRT19: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt19/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt2_ceat_consultar`

Tribunal TRT2: Certidão Eletrônica de Ações Trabalhistas (CEAT) - Processos Físicos, consulta em fonte oficial. _(POST /api/jus/tribunal/trt2/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Sim | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt2_ceat_digital_consultar`

Tribunal TRT2: Certidão Eletrônica de Ações Trabalhistas (CEAT) - Processos Digitais, consulta em fonte oficial. _(POST /api/jus/tribunal/trt2/ceat/digital/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj_raiz` | string | Não | Parâmetro de consulta "cnpj_raiz". |

#### `jus_tribunal_trt2_processo_consultar`

Tribunal TRT2: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt2/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt20_ceat_consultar`

Tribunal TRT20: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt20/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt20_processo_consultar`

Tribunal TRT20: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt20/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt21_ceat_consultar`

Tribunal TRT21: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt21/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt21_processo_consultar`

Tribunal TRT21: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt21/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt22_processo_consultar`

Tribunal TRT22: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt22/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt23_ceat_consultar`

Tribunal TRT23: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt23/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt24_ceat_consultar`

Tribunal TRT24: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt24/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `cpf_solicitante` | string | Sim | Parâmetro de consulta "cpf_solicitante". |

#### `jus_tribunal_trt24_processo_consultar`

Tribunal TRT24: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt24/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt3_ceat_consultar`

Tribunal TRT3: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt3/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt4_ceat_consultar`

Tribunal TRT4: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt4/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt4_processo_consultar`

Tribunal TRT4: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt4/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt5_ceat_consultar`

Tribunal TRT5: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt5/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt5_processo_consultar`

Tribunal TRT5: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt5/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt6_certidao_consultar`

Tribunal TRT6: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt6/certidao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt6_processo_consultar`

Tribunal TRT6: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt6/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt7_ceat_consultar`

Tribunal TRT7: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt7/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome` | string | Não | Parâmetro de consulta "nome". |

#### `jus_tribunal_trt7_ceat_digital_consultar`

Tribunal TRT7: Certidão Eletrônica de Ações Trabalhistas (CEAT) - Processos Digitais, consulta em fonte oficial. _(POST /api/jus/tribunal/trt7/ceat/digital/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt7_processo_consultar`

Tribunal TRT7: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt7/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt8_ceat_consultar`

Tribunal TRT8: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt8/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |

#### `jus_tribunal_trt8_processo_consultar`

Tribunal TRT8: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt8/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_trt9_ceat_consultar`

Tribunal TRT9: Certidão Eletrônica de Ações Trabalhistas (CEAT), consulta em fonte oficial. _(POST /api/jus/tribunal/trt9/ceat/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `nome_completo` | string | Não | Parâmetro de consulta "nome_completo". |

#### `jus_tribunal_trt9_processo_consultar`

Tribunal TRT9: Consulta Processual, consulta em fonte oficial. _(POST /api/jus/tribunal/trt9/processo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Sim | Parâmetro de consulta "numero_processo". |
| `grau` | string | Não | Parâmetro de consulta "grau". |

#### `jus_tribunal_tse_certidao_consultar`

Tribunal TSE: Certidão de Quitação Eleitoral, consulta em fonte oficial. _(POST /api/jus/tribunal/tse/certidao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `name` | string | Sim | Parâmetro de consulta "name". |
| `birthdate` | string | Sim | Parâmetro de consulta "birthdate". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `titulo_eleitoral` | string | Não | Parâmetro de consulta "titulo_eleitoral". |
| `mother` | string | Não | Parâmetro de consulta "mother". |
| `father` | string | Não | Parâmetro de consulta "father". |

#### `jus_tribunal_tse_doador_fornecedor_consultar`

Tribunal TSE: Doadores e Fornecedores, consulta em fonte oficial. _(POST /api/jus/tribunal/tse/doador/fornecedor/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Não | Parâmetro de consulta "nome". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `ano` | string | Sim | Parâmetro de consulta "ano". |

#### `jus_tribunal_tse_pje_consultar`

Tribunal TSE: Processo Judicial Eletrônico (PJe), consulta em fonte oficial. _(POST /api/jus/tribunal/tse/pje/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `classe_judicial` | string | Não | Parâmetro de consulta "classe_judicial". |
| `objeto` | string | Não | Parâmetro de consulta "objeto". |
| `orgao` | string | Não | Parâmetro de consulta "orgao". |
| `uf` | string | Não | Parâmetro de consulta "uf". |
| `municipio` | string | Não | Parâmetro de consulta "municipio". |
| `ano_eleicao` | string | Não | Parâmetro de consulta "ano_eleicao". |
| `data_inicial_autuacao` | string | Não | Parâmetro de consulta "data_inicial_autuacao". |
| `data_final_autuacao` | string | Não | Parâmetro de consulta "data_final_autuacao". |
| `nome_parte` | string | Não | Parâmetro de consulta "nome_parte". |
| `nome_advogado` | string | Não | Parâmetro de consulta "nome_advogado". |
| `oab` | string | Não | Parâmetro de consulta "oab". |

#### `jus_tribunal_tse_situacao_consultar`

Tribunal TSE: Situação Eleitoral, consulta em fonte oficial. _(POST /api/jus/tribunal/tse/situacao/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `name` | string | Não | Parâmetro de consulta "name". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `titulo_eleitoral` | string | Não | Parâmetro de consulta "titulo_eleitoral". |
| `birthdate` | string | Não | Parâmetro de consulta "birthdate". |

#### `jus_tribunal_tse_titulo_consultar`

Tribunal TSE: Título Eleitoral, consulta em fonte oficial. _(POST /api/jus/tribunal/tse/titulo/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `birthdate` | string | Sim | Parâmetro de consulta "birthdate". |
| `mother` | string | Não | Parâmetro de consulta "mother". |
| `father` | string | Não | Parâmetro de consulta "father". |
| `name` | string | Não | Parâmetro de consulta "name". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `titulo_eleitoral` | string | Não | Parâmetro de consulta "titulo_eleitoral". |

#### `jus_tribunal_tst_banco_falencias_consultar`

Tribunal TST: Banco de Falências, consulta em fonte oficial. _(POST /api/jus/tribunal/tst/banco/falencias/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `razao_social` | string | Não | Parâmetro de consulta "razao_social". |
| `numero_processo` | string | Não | Parâmetro de consulta "numero_processo". |

#### `jus_tribunal_tst_cndt_consultar`

Tribunal TST: CNDT, consulta em fonte oficial. _(POST /api/jus/tribunal/tst/cndt/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `cpf` | string | Não | Parâmetro de consulta "cpf". |

#### `jus_tribunal_tst_validacao_cndt_consultar`

Tribunal TST: Validação de CNDT, consulta em fonte oficial. _(POST /api/jus/tribunal/tst/validacao/cndt/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Não | Parâmetro de consulta "cpf". |
| `cnpj` | string | Não | Parâmetro de consulta "cnpj". |
| `numero_certidao` | string | Sim | Parâmetro de consulta "numero_certidao". |
| `ano` | string | Sim | Parâmetro de consulta "ano". |

---

Este MCP também funciona via **conexão MCP** (Claude / Cursor) em `https://api.mcp.ai/jus` — veja o [README](../../README.md). A skill acima é pra consumir a **REST API** direto (agente próprio / código).
