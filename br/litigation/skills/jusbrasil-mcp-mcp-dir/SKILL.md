---
name: jusbrasil-mcp-mcp-dir
title: Legal MCP (alternativa ao Jusbrasil) — REST API skill
description: 'Pesquisa jurídica brasileira via Legal MCP (alternativa ao Jusbrasil): raio-X de processos por nome/CPF/CNPJ/número, publicações no DJEN, sanções e jurisprudência. Use quando o usuário perguntar sobre processos, intimações, andamento, OAB ou consulta jurídica em geral.'
author: mcp-dir
author_url: https://github.com/mcp-dir/jusbrasil-mcp/tree/main/skills/jusbrasil-mcp
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Legal MCP (alternativa ao Jusbrasil) — REST API skill

Você tem acesso à **Legal MCP (alternativa ao Jusbrasil)** REST API na MCP.AI.

> Alternativa ao **Jusbrasil** pensada para IA. Descubra processos por nome, CPF, CNPJ ou número CNJ e monte um raio-X jurídico consolidado: processos, publicações no DJEN, sanções, menções municipais e jurisprudência — fontes públicas oficiais, sem login. **Não afiliado ao Jusbrasil.**

## Base URL

```
https://api.mcp.ai/api/legal
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
curl -X POST https://api.mcp.ai/api/legal/cnpj/consultar \
  -H "Authorization: Bearer sk_live_..." \
  -H "Content-Type: application/json" \
  -d '{"cnpj":"..."}'
```

## Reportar problemas

Se um endpoint retornar erro, vazio ou dado inesperado, reporte (não desista calado): **POST /api/legal/report** com `{ "message": "...", "context"?: "...", "conversation"?: [...] }`. Isso notifica o time da MCP.AI.

## Endpoints (20)

#### `cnpj_consultar`

Consulta cadastral de um CNPJ (grátis): razão social, nome fantasia, situação cadastral, CNAE principal, porte, município/UF e SÓCIOS (QSA). _(POST /api/legal/cnpj/consultar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Sim | CNPJ (14 dígitos), com ou sem máscara. |

#### `cnpj_processos`

DESCOBERTA por CNPJ: resolve o CNPJ em razão social (e sócios) e busca os processos por NOME no Diário (DJEN) — grátis, com número de processo completo. _(POST /api/legal/cnpj/processos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Sim | CNPJ (14 dígitos), com ou sem máscara. |
| `incluir_socios` | boolean | Não | Se true, também busca os processos de cada sócio (QSA). Default false. |

#### `cpf_processos`

DESCOBERTA por CPF: busca os processos da pessoa por NOME no Diário (DJEN), grátis. _(POST /api/legal/cpf/processos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Sim | CPF (11 dígitos), com ou sem máscara. |
| `nome` | string | Não | Nome completo do titular (recomendado — CPF→nome não é público). |

#### `cpf_validar`

Valida os dígitos verificadores de um CPF (mod 11) e informa se há broker de identidade disponível. _(POST /api/legal/cpf/validar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Sim | CPF (11 dígitos), com ou sem máscara. |

#### `djen_get_certidao`

Retorna a URL da certidão (PDF) de uma comunicação do DJEN pelo seu hash (campo `hash` retornado na busca). _(POST /api/legal/djen/get/certidao)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `hash` | string | Sim | Hash da comunicação (campo hash da busca). |

#### `djen_processos_por_parte`

DESCOBERTA por NOME de parte (grátis, sem captcha): busca o DJEN por quem figura no processo e agrupa por número — devolve a lista de processos da pessoa/empresa, com partes e tribunal. _(POST /api/legal/djen/processos/por/parte)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome_parte` | string | Sim | Nome da parte (pessoa ou razão social) a procurar. |
| `sigla_tribunal` | string | Não | Restringe a um tribunal (ex.: TJSP). |
| `data_inicio` | string | Não | Data inicial (AAAA-MM-DD). |
| `data_fim` | string | Não | Data final (AAAA-MM-DD). |
| `itens_por_pagina` | integer | Não | Comunicações a varrer por página (default 100). |
| `pagina` | integer | Não | Página (default 1). |

#### `djen_search_comunicacoes`

Busca publicações/intimações no Diário de Justiça Eletrônico Nacional (DJEN) por OAB, nome de advogado, número de processo, tribunal e data. _(POST /api/legal/djen/search/comunicacoes)_

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

Busca jurisprudência (acórdãos, súmulas, OJs) no acervo público LexML por termo/tese — cobre tribunais superiores e demais. _(POST /api/legal/jurisprudencia/buscar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Sim | Termo, tese ou assunto (ex.: 'dano moral negativação indevida'). |
| `tipo` | string | Não | Filtra por tipo de documento (ex.: "Acórdão", "Súmula"). |
| `max` | integer | Não | Resultados (default 10, máx 50). |

#### `jurisprudencia_sumulas`

Busca SÚMULAS (incluindo vinculantes) por termo no acervo LexML. _(POST /api/legal/jurisprudencia/sumulas)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Sim | Termo/assunto da súmula. |
| `max` | integer | Não | Resultados (default 10). |

#### `legal_checar_novidades`

Checa AGORA se há novidade nos monitoramentos (sem esperar o ciclo automático). _(POST /api/legal/checar/novidades)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `watch_id` | string | Não | Id de um monitoramento específico (opcional). |
| `watch_ids` | string[] | Não | Bulk mode: multiple values for watch_id |

#### `legal_dossie`

Raio-X jurídico de uma pessoa ou empresa: descobre os processos e (opcional) o andamento, num relatório consolidado. _(POST /api/legal/dossie)_

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

Lista os monitoramentos ativos do workspace. _(POST /api/legal/listar/monitoramentos)_

#### `legal_monitorar`

Cria um monitoramento: avisa quando houver NOVIDADE — nova movimentação (numero_processo), novo processo de uma pessoa/empresa (nome/cnpj), ou nova publicação/intimação de uma OAB (oab+uf). _(POST /api/legal/monitorar)_

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

Remove (desativa) um monitoramento pelo seu id (`watch_id`). _(POST /api/legal/remover/monitoramento)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `watch_id` | string | Sim | Id do monitoramento (wch_…) de legal_listar_monitoramentos. |
| `watch_ids` | string[] | Não | Bulk mode: multiple values for watch_id |

#### `processos_buscar_por_documento`

DESCOBERTA por CPF ou CNPJ. O serviço resolve o documento em nome(s) (CNPJ→razão social/sócios; CPF→nome) e então busca os processos por nome nos portais. ASSÍNCRONO: retorna { job_id }; faça o pollin _(POST /api/legal/processos/buscar/por/documento)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `documento` | string | Sim | CPF (11 dígitos) ou CNPJ (14 dígitos), com ou sem máscara. |
| `platforms` | string[] | Não | Plataformas a varrer (parser por plataforma, não por TJ): esaj, pje, eproc, projudi. Vazio = todas. Restrinja (ex.: ['esaj']) para resultado mais rápido/barato. (esaj, pje, eproc, projudi) |
| `tribunais` | string[] | Não | Restringe a tribunais específicos (ex.: ['tjsp']). Vazio = todos os órgãos das plataformas escolhidas. Quanto mais amplo, mais lento (captcha por órgão). |
| `max_results` | integer | Não | Limite de processos a retornar (default decidido pelo engine). |

#### `processos_buscar_por_nome`

DESCOBERTA: busca processos pelo NOME de uma parte (pessoa ou empresa) raspando os portais públicos dos tribunais (ESAJ/PJe/eproc/Projudi) — o gap que datajud (só por número) e djen (OAB/advogado) não _(POST /api/legal/processos/buscar/por/nome)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Sim | Nome completo da parte (pessoa ou razão social) a procurar. |
| `platforms` | string[] | Não | Plataformas a varrer (parser por plataforma, não por TJ): esaj, pje, eproc, projudi. Vazio = todas. Restrinja (ex.: ['esaj']) para resultado mais rápido/barato. (esaj, pje, eproc, projudi) |
| `tribunais` | string[] | Não | Restringe a tribunais específicos (ex.: ['tjsp']). Vazio = todos os órgãos das plataformas escolhidas. Quanto mais amplo, mais lento (captcha por órgão). |
| `max_results` | integer | Não | Limite de processos a retornar (default decidido pelo engine). |

#### `processos_get_resultado`

Polling de um job de busca (de processos_buscar_por_nome/documento). _(POST /api/legal/processos/get/resultado)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `job_id` | string | Sim | ID do job retornado por processos_buscar_por_nome/documento. |
| `job_ids` | string[] | Não | Bulk mode: multiple values for job_id |

#### `querido_diario_buscar`

Busca em diários oficiais MUNICIPAIS (milhares de prefeituras) por termo/nome — útil pra menções fora do Judiciário: licitações, nomeações, contratos, sanções municipais. _(POST /api/legal/querido/diario/buscar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Sim | Termo/nome a buscar (ex.: "Fulano de Tal" ou "licitação saúde"). |
| `territory_ids` | string[] | Não | Códigos IBGE de municípios a restringir (vazio = todos). |
| `data_inicio` | string | Não | Publicado desde (AAAA-MM-DD). |
| `data_fim` | string | Não | Publicado até (AAAA-MM-DD). |
| `size` | integer | Não | Resultados (default 10, máx 50). |

#### `transparencia_pep`

Verifica se um CPF é de Pessoa Exposta Politicamente (PEP) e retorna função/órgão/período. _(POST /api/legal/transparencia/pep)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string | Sim | CPF (11 dígitos), com ou sem máscara. |

#### `transparencia_sancoes`

Consulta sanções de uma pessoa ou empresa por CPF/CNPJ no Portal da Transparência (consolida CEIS — inidôneas/suspensas, CNEP — empresas punidas, e CEPIM — entidades impedidas). _(POST /api/legal/transparencia/sancoes)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf_cnpj` | string | Sim | CPF (11) ou CNPJ (14) do sancionado, com ou sem máscara. |

---

Este MCP também funciona via **conexão MCP** (Claude / Cursor) em `https://api.mcp.ai/legal` — veja o [README](../../README.md). A skill acima é pra consumir a **REST API** direto (agente próprio / código).
