---
name: peticao-analyzer-ma-serra
title: Peticao Analyzer — Analise Estruturada de Pecas Processuais
description: 'Usar quando o usuario precisar analisar, resumir ou extrair informacoes-chave de pecas processuais — peticoes iniciais, contestacoes, recursos, laudos periciais ou manifestacoes. Tambem usar para preparar despachos saneadores, pautas de audiencia ou mapear pontos controvertidos. Triggers: "peticao", "contestacao", "recurso", "analisar processo", "resumir autos", "pontos controvertidos", "saneamento", "laudo pericial", "peca processual".'
author: ma-serra
author_url: https://github.com/ma-serra/lex-intelligentia-skills/tree/main/skills/core/peticao-analyzer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Peticao Analyzer — Analise Estruturada de Pecas Processuais

## Overview

Transforma pecas processuais densas em mapas de informacao estruturados usando o framework **CAPPD** (Causas, Argumentos, Pedidos, Provas, Defesas). Acelera a analise judicial e a preparacao de decisoes. A saida desta skill alimenta diretamente a `sentenca-judicial-br` para geracao de minutas.

## When to Use

- Analisar peticao inicial, contestacao, replica ou recurso
- Resumir autos para preparacao de decisao
- Mapear pontos controvertidos para despacho saneador (art. 357, CPC)
- Preparar pauta de audiencia de instrucao
- Extrair e classificar pedidos (principal, subsidiario, acessorio)
- Analisar laudo pericial e impugnacoes

**When NOT to Use:**
- Redigir a sentenca (usar `sentenca-judicial-br`)
- Analisar audiencias ja transcritas (usar `audiencia-analyzer`)
- Validar teses juridicas isoladas (usar `tese-juridica-validator`)

---

## Framework de Analise: CAPPD

| Elemento | O que extrair |
|----------|---------------|
| **C**ausas de pedir | Fatos narrados + fundamentos juridicos |
| **A**rgumentos | Teses principais e subsidiarias |
| **P**edidos | Principais, subsidiarios, cumulados, alternativos |
| **P**rovas | Documentais juntadas + requeridas + periciais |
| **D**efesas/Excecoes | Preliminares, prejudiciais, merito, reconvencao |

---

## Analise de Peticao Inicial

### Output Estruturado

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANALISE DA PETICAO INICIAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[PARTES]
- Autor: [nome + qualificacao]
- Reu: [nome + qualificacao]

[NATUREZA DA ACAO]
- Tipo: [acao declaratoria / condenatoria / constitutiva]
- Rito: [comum / especial / sumario / JEC]
- Valor da causa: R$ [valor]

[CAUSA DE PEDIR]
Fatica:
- [sintese dos fatos materiais narrados]

Juridica:
- Normas invocadas: [arts. e diplomas]
- Teses juridicas: [sintese]

[PEDIDOS]
Principal:
- [transcricao/sintese do pedido principal]

Subsidiarios/Acessorios:
- [pedidos secundarios]
- Tutela de urgencia: [Sim/Nao — fundamento]
- Honorarios: [percentual pleiteado]

[PROVAS JUNTADAS]
- Documentos: [lista]
- Requerimentos probatorios: [testemunhal / pericial / inspecao]

[PONTOS DE ATENCAO]
- [Questao processual relevante]
- [Possivel litisconsorcio necessario nao chamado]
- [Prescricao/decadencia a verificar]
- [Competencia — eventual vicio]

[SINTESE]
[2-3 linhas resumindo o nucleo da demanda]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Analise de Contestacao

### Output Estruturado

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANALISE DA CONTESTACAO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[PRELIMINARES]
- [lista de preliminares suscitadas com sintese]
- Carencia de acao: [sim/nao — fundamento]
- Inepcia: [sim/nao — fundamento]
- Prescricao/decadencia: [sim/nao — prazo e marco]

[DEFESAS DE MERITO]
- Fatos impugnados especificamente: [lista]
- Fatos admitidos: [lista]
- Teses defensivas: [sintese por ponto]

[ARGUMENTOS CENTRAIS DO REU]
1. [Argumento 1 — tese + norma + precedente citado]
2. [Argumento 2]
3. [Argumento 3]

[PROVAS DO REU]
- Documentos juntados: [lista]
- Requerimentos: [testemunhal / pericial / outra]

[FATOS ADMITIDOS — ART. 341, CPC]
(Fatos NAO impugnados especificamente pelo reu sao considerados
admitidos e dispensam prova — onus de impugnacao especificada)
- [Fato 1 admitido por ausencia de impugnacao]
- [Fato 2 admitido]
- [Fato 3 admitido]

[RECONVENCAO]
- Sim / Nao
- Se sim: [pedidos reconvencionais]

[PONTOS CONTROVERTIDOS]
[Quadro: Alegacao do Autor x Contestacao do Reu x Prova necessaria]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Analise Consolidada — Peticao Inicial + Contestacao

Para uso direto pelo magistrado: visao unificada que cruza os argumentos de ambas as partes e identifica o que precisa ser decidido.

### Output Estruturado

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANALISE CONSOLIDADA — PARA DECISAO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[PARTES E OBJETO]
- Autor: [nome + qualificacao]
- Reu: [nome + qualificacao]
- Natureza: [tipo da acao]
- Valor da causa: R$ [valor]

[PEDIDOS vs. DEFESAS — QUADRO COMPARATIVO]
| # | Pedido do Autor | Defesa do Reu | Questao a decidir |
|---|----------------|---------------|-------------------|
| 1 | [Pedido 1]     | [Defesa 1]    | [Ponto juridico]  |
| 2 | [Pedido 2]     | [Defesa 2]    | [Ponto juridico]  |
| 3 | [Pedido 3]     | [Defesa 3]    | [Ponto juridico]  |

[PRELIMINARES A RESOLVER]
| Preliminar | Suscitada por | Fundamento | Procedencia provavel |
|-----------|---------------|------------|---------------------|
| [Tipo]    | [Reu/oficio]  | [Sintese]  | [Sim/Nao — motivo]  |

[FATOS INCONTROVERSOS — ART. 341, CPC]
(Dispensam prova — podem ser usados diretamente na fundamentacao)
1. [Fato admitido por ambas as partes]
2. [Fato nao impugnado especificamente pelo reu]
3. [Fato nao impugnado especificamente pelo reu]

[FATOS CONTROVERTIDOS — NECESSITAM PROVA]
| # | Fato | Autor alega | Reu alega | Prova necessaria |
|---|------|-------------|-----------|-----------------|
| 1 | [Fato] | [Versao] | [Versao] | [Meio de prova] |
| 2 | [Fato] | [Versao] | [Versao] | [Meio de prova] |

[PROVAS PRODUZIDAS E PENDENTES]
- Documentais do autor: [lista resumida]
- Documentais do reu: [lista resumida]
- Pericia: [realizada / pendente / dispensada]
- Testemunhal: [ouvidas X testemunhas / pendente]

[QUESTOES JURIDICAS CENTRAIS]
1. [Questao 1]: [norma aplicavel] — [posicao aparente do STJ/STF]
2. [Questao 2]: [norma aplicavel] — [posicao aparente do STJ/STF]

[SUGESTAO DE ORDEM DE JULGAMENTO]
1. Preliminar(es): [resolver primeiro]
2. Merito — questao [X]: [resolver antes de Y por ser prejudicial]
3. Merito — questao [Y]: [resolver por ultimo]
4. Pedidos acessorios: [honorarios, custas, tutela]

[SINTESE PARA O MAGISTRADO]
[3-5 linhas com o nucleo do conflito, os pontos-chave a decidir
e eventuais alertas processuais]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Quando Usar a Analise Consolidada

- **Apos ler** peticao inicial E contestacao
- **Antes de redigir** sentenca ou despacho saneador
- **Quando o processo** ja esta pronto para julgamento (sem provas pendentes)
- **Para preparar** a pauta de decisoes em lote

**Nota:** Esta analise substitui a necessidade de fazer duas analises separadas. Se apenas uma peca estiver disponivel, usar os templates individuais acima.

---

## Mapeamento de Pontos Controvertidos

Para uso no despacho saneador (art. 357, CPC):

```
QUESTOES DE FATO CONTROVERTIDAS:
1. [Fato 1]: Autor alega X; Reu nega/alega Y -> Prova: [meio de prova]
2. [Fato 2]: [mesma estrutura]

QUESTOES DE DIREITO CONTROVERTIDAS:
1. [Tese juridica 1]: Autor sustenta X; Reu sustenta Y -> Posicao da jurisprudencia: [sintese]
2. [Tese juridica 2]

QUESTOES INCONTROVERSES (dispensam prova):
1. [Fato admitido]
2. [Fato notorio]
```

---

## Analise de Recursos

### Apelacao

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANALISE DA APELACAO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[OBJETO DO RECURSO]
- Impugna: [parte da sentenca / sentenca toda]
- Tipo de vicio alegado: [error in judicando / error in procedendo]

[RAZOES RECURSAIS]
Capitulo 1: [tema] -> Argumento: [sintese] -> Pedido: [reformar/anular]
Capitulo 2: [tema] -> Argumento: [sintese] -> Pedido: [reformar/anular]

[QUESTOES PROCESSUAIS]
- Tempestividade: [verificar prazo]
- Preparo: [recolhido / dispensado / custas]
- Legitimidade: [verificar]

[SINTESE PARA CONTRARRAZOES]
[Pontos que o apelado precisara rebater]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Preparacao de Pauta de Audiencia

### Template para Audiencia de Instrucao e Julgamento

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PAUTA — AUDIENCIA DE INSTRUCAO E JULGAMENTO
Processo n: [numero]
Data: [data / horario]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. PRESENCA DAS PARTES
   [ ] Autor / Advogado do Autor
   [ ] Reu / Advogado do Reu
   [ ] Testemunhas: [lista com nomes]

2. TENTATIVA DE CONCILIACAO (art. 359, CPC)
   [ ] Realizada — [resultado]

3. INQUIRICAO DAS TESTEMUNHAS
   Testemunha 1 — [nome]: [pontos a questionar]
   Testemunha 2 — [nome]: [pontos a questionar]

4. DEPOIMENTO PESSOAL DAS PARTES (se requerido)
   [ ] Autor: [pontos relevantes]
   [ ] Reu: [pontos relevantes]

5. QUESTOES-CHAVE A ESCLARECER NA AUDIENCIA
   - [Questao 1 — fato controvertido especifico]
   - [Questao 2]

6. ENCERRAMENTO
   [ ] Memoriais / debates orais (prazo de [X] dias)
   [ ] Julgamento em audiencia
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Extracao Automatica de Pedidos

Para cada pedido identificado, classificar como:

| Tipo | Criterio | Exemplo |
|------|----------|---------|
| **Principal** | Objeto central da demanda | Rescisao do contrato |
| **Subsidiario** | Alternativa ao principal | Se nao rescisao, reducao do valor |
| **Acessorio** | Decorrente do principal | Juros, correcao, honorarios |
| **Cumulado** | Independente, mas reunido | Dano material + dano moral |
| **Antecipado** | Tutela de urgencia | Liminar / antecipacao de tutela |

---

## Analise de Laudo Pericial

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANALISE DO LAUDO PERICIAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PERITO: [nome + especialidade]
QUESITOS DO AUTOR: [sintese das respostas]
QUESITOS DO REU: [sintese das respostas]
QUESITOS DO JUIZO: [sintese das respostas]

CONCLUSAO DO PERITO: [sintese]

IMPUGNACOES AO LAUDO:
- Autor: [pontos impugnados]
- Reu: [pontos impugnados]

ANALISE JUDICIAL:
- O laudo e: [suficiente / incompleto / contraditorio]
- Necessidade de esclarecimentos: [sim/nao — quais]
- Conclusao pericial favorece: [autor / reu / neutro]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Common Mistakes

| Erro | Como evitar |
|------|------------|
| Confundir causa de pedir fatica com juridica | Fatica = fatos; Juridica = normas e teses. Separar sempre no CAPPD |
| Ignorar pedidos implicitos | Verificar se ha pedido de tutela antecipada, gratuidade, ou honorarios nao destacados |
| Nao mapear fatos incontroversos | Fatos nao impugnados especificamente sao ADMITIDOS (art. 341, CPC) — preencher o campo [FATOS ADMITIDOS] obrigatoriamente |
| Misturar analise de merito com preliminares | Preliminares primeiro (art. 337, CPC); merito so depois de superadas |
| Ignorar reconvencao | Verificar se a contestacao contem pedido reconvencional (art. 343, CPC) |
| Nao cruzar provas com pontos controvertidos | Cada ponto controvertido deve ter um meio de prova associado |
| Produzir resumo sem estrutura | Sempre usar framework CAPPD — analise solta perde informacao |

---

## Integracao com Outras Skills

| Etapa | Skill |
|-------|-------|
| Analise da peca processual | **peticao-analyzer** (esta skill) |
| Transcricao e analise de audiencia | `audiencia-analyzer` |
| Validacao de teses juridicas | `tese-juridica-validator` |
| Redacao da sentenca | `sentenca-judicial-br` |
| Proposta de acordo | `conciliacao-assistant` |

---

## Workflow de Uso

1. **Receber** o texto da peca (ou extrato relevante)
2. **Identificar** o tipo de peca (inicial / contestacao / recurso / laudo)
3. **Aplicar** o template CAPPD correspondente
4. **Mapear** os pontos controvertidos
5. **Gerar** o output estruturado para uso na decisao ou preparacao de audiencia
6. **Sinalizar** questoes de atencao especial (prescricao, litisconsorcio, nulidades)
7. **Encaminhar** para a skill adequada (sentenca, audiencia, conciliacao)
