---
name: deliberacao-juridica-sensdiego
title: Deliberação jurídica
description: Conduzir a decisão do advogado entre uma análise madura e a próxima ação, com opções, recomendação, entrevista e registro próprio. Use quando o advogado perguntar o que fazer ou quando outra skill encaminhar uma escolha estratégica pendente. Não use como primeira rota para um pedido de redação; não pesquisa, não aprofunda tese e não redige.
author: sensdiego
author_url: https://github.com/sensdiego/codigo-aberto/tree/main/skills/deliberacao-juridica
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# Deliberação jurídica

Conduza a decisão sem absorver análise, aprofundamento ou redação. Observe a
[disciplina compartilhada](../../references/disciplina.md), o
[contrato de handoff](../../references/handoff.md) e o
[protocolo de deliberação](../../references/deliberacao.md).

## Pré-requisito

Consuma análise madura para a decisão em jogo: mapa jurídico confirmado ou,
para decisão pré-contenciosa simples, análise documental confirmada. Verifique
caso, lente, fontes, escopo, estados, confirmação e decisões pendentes.

Se o material estiver bruto ou a análise necessária estiver incompleta,
encaminhe somente a etapa ausente. Não delibere sobre hipótese nem promova
conteúdo marcado como `[verificar]`.

## Execução

Siga os seis passos do protocolo: apresentação decisória, opções, recomendação,
entrevista, registro e rota de saída. Reaproveite as alternativas do mapa em vez
de criar outro mapa. Preserve a fronteira com `aprofundamento-juridico`: ele
produz conhecimento; esta skill registra a decisão do advogado.

Na primeira resposta, termine com exatamente uma pergunta decisória de maior
valor. Não agrupe outras perguntas antes de receber essa resposta.

## Resultado

Produza o handoff de tipo `decisão` somente quando o advogado encerrar a
deliberação ou quando as respostas permitirem registrar escolhas, rejeições,
condições, razões, prioridades, pendências e condição de reabertura.

Se a próxima rota for redação, encaminhe ao briefing da skill adequada. A
decisão registrada informa esse briefing e nunca autoriza a minuta.

## O que esta skill não faz

- Não interpreta documentos brutos nem substitui análise documental ou jurídica.
- Não pesquisa legislação, jurisprudência, pessoas, patrimônio ou fatos externos.
- Não aprofunda teses nem simula audiência, reunião ou negociação.
- Não escolhe pelo advogado nem apaga opções rejeitadas ou condicionais.
- Não redige peça, parecer, relatório ou comunicação.
- Não pratica ação externa.

> Documento gerado com suporte de inteligência artificial. Conteúdo sujeito à
> revisão e validação obrigatória pelo advogado responsável antes de qualquer
> uso profissional ou processual.
