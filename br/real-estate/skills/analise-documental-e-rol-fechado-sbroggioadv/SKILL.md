---
name: analise-documental-e-rol-fechado-sbroggioadv
title: Análise documental e rol fechado
description: Monta o dossiê documental do ato sem inventar checklist, aplicando o rol fechado da Lei 7.433/1985 e do Decreto 93.240/1986, a validade de 30 dias da certidão imobiliária, a camada rural e os documentos próprios de inventário e divórcio. Esta skill deve ser usada quando o pedido mencionar documentos para escritura, certidões, matrícula, feitos ajuizados, CND ou CPEN, CCIR, ITR, validade de certidão, inventário, divórcio, documento faltante ou nota de exigências.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/analise-documental-e-rol-fechado
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: real-estate
language: pt
---

# Análise documental e rol fechado

> Camada C3. Exigir somente documento previsto em lei ou norma aplicável. Não completar lista por costume.

## Anexos e skills obrigatórios

- `context/escritura-corpus-federal.md` — leis federais da escritura imobiliária;
- `context/res-cnj-35-2007-com-571-2024.md` — documentos e gates de inventário/divórcio;
- `context/cc-notarial.md` — capacidade, representação, outorga e forma;
- `context/precedentes-notariais.md` — certidão fiscal como informação;
- `context/travas-defasagem.md` — validade, rural e expressões revogadas;
- `roteador-uf` para acréscimos estaduais.

## Entradas

Fixar UF, ato, modalidade, bem, qualidade das partes, representação, data do ato e eventual regra municipal/estadual. Trabalhar com nomes de categorias documentais; não reproduzir dados pessoais do caso.

## Regra do rol fechado

Aplicar a Lei 7.433/1985, art. 1º: além da identificação das partes, somente apresentar documentos expressamente determinados em lei. Detalhar o Decreto 93.240/1986, art. 1º, I-V:

1. identificação das partes e intervenientes;
2. comprovante do ITBI, salvo pagamento posterior autorizado;
3. certidões fiscais do imóvel urbano ou CCIR e prova de ITR no rural;
4. certidão de ações reais/reipersecutórias e de ônus reais, com validade de 30 dias;
5. demais documentos expressamente exigidos em lei.

Não reintroduzir “feitos ajuizados” como fórmula legal vigente. Não transformar a escritura em arquivo indiscriminado de cópias.

## Camadas específicas

### Imóvel urbano

Conferir matrícula/titularidade, descrição, ônus, ações reais, ITBI e certidões exigíveis. Admitir dispensa de certidões fiscais municipais pelo adquirente somente nos termos do Decreto, com responsabilidade e declarações cabíveis.

Tratar CND/CPEN como informação, não condição genérica para lavrar. Não fundir a questão não fechada da CNDT com o precedente fiscal.

### Imóvel rural

Exigir CCIR e prova relativa ao ITR conforme as hipóteses legais. Classificar CCIR ausente como sanável no balcão, mas impedir lavratura enquanto faltar: a Lei 4.947/1966 comina nulidade. Não atribuir ao tabelião de notas a solidariedade que a Lei 9.393/1996 nomina para o Registro de Imóveis.

### Inventário e divórcio

Aplicar os documentos dos arts. 22 e 23 da Resolução 35/2007 e os gates acrescentados pela Resolução 571/2024. Preservar identificação original quando exigida e distinguir documento de gate externo, como sentença transitada ou manifestação do MP.

### Procuração, testamento e ata

Carregar somente os documentos e formalidades da skill do ato. Não importar o rol imobiliário para ato sem imóvel. Verificar poderes, testemunhas e prova do fato por sua disciplina própria.

## Classificação da falta

- documento legalmente exigido e suprível → Categoria C, nota de exigências;
- prova de ato externo ainda inexistente → Categoria B, aguardar evento;
- certidão fiscal usada apenas como informação → Categoria D, consignar sem recusar;
- ausência que torna a via impossível → Categoria A;
- matéria para juízo/MP/registro → Categoria E.

Acionar `travas-do-ato-cinco-categorias` e aplicar a forma estadual da nota.

## Saída

| Documento/requisito | Fonte | Aplicável | Validade | Estado | Categoria | Ação |
|---|---|---|---|---|---|---|

Separar “apresentado”, “ausente”, “dispensado por norma”, “não aplicável” e “depende de regra local”. Não marcar dispensa por declaração sem base.

## Reprovação automática

- inventar documento por prudência ou costume;
- usar rol aberto;
- exigir “feitos ajuizados” pela redação antiga;
- bloquear ato somente por CND/CPEN;
- lavrar imóvel rural sem CCIR;
- atribuir solidariedade do ITR ao destinatário errado;
- usar certidão vencida sem conferir o evento de validade;
- tratar ato externo como documento comum;
- omitir acréscimo estadual depois de fixar a UF.
