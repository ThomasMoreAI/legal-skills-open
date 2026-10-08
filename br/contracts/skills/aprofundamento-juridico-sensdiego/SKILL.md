---
name: aprofundamento-juridico-sensdiego
title: Aprofundamento jurídico
description: Estressar teses, explorar casos, simular perspectivas, preparar interações e planejar investigações usando material jurídico já disponível. Use para aprofundamento dinâmico, preparação de audiência, negociação, reunião ou teste adversarial sem pesquisar nem redigir. Não use quando o pedido for decidir o que fazer com a análise; use `deliberacao-juridica`.
author: sensdiego
author_url: https://github.com/sensdiego/codigo-aberto/tree/main/skills/aprofundamento-juridico
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
sources:
- title: Audiencia Civel
  path: references/audiencia-civel.md
- title: Modos
  path: references/modos.md
---

# Aprofundamento jurídico

Explore o que já foi analisado sem substituir a análise jurídica. Observe a
[disciplina compartilhada](../../references/disciplina.md), o
[contrato de handoff](../../references/handoff.md) e a
[biblioteca do CPC](../../references/legislacao/cpc/README.md).

## Entrada

Defina objeto, objetivo, material disponível, lente e decisão que o
aprofundamento pretende informar. Preserve fatos, inferências, hipóteses e
lacunas nos estados recebidos.

Escolha um modo em [modos.md](references/modos.md): estressar tese, explorar
caso, simular perspectivas, preparar interação ou planejar investigação. Para
audiência civil, carregue também
[audiencia-civel.md](references/audiencia-civel.md).

## Motor comum

```text
objeto e objetivo
  -> mapa inicial de hipóteses
  -> fragilidade mais séria
  -> pergunta de maior valor informacional
  -> resposta ou novo material
  -> atualização das hipóteses
  -> pressão adversarial
  -> síntese proporcional
```

Em cada rodada, registre o que foi confirmado, contraditado, mantido como
hipótese, alterado e qual pergunta pode destravar o problema. Comece pela
fragilidade mais séria, não pela defesa da posição preferida.

Uma tese pode resistir. Não fabrique discordância ou risco apenas para produzir
um resultado dramático.

## Saída

Entregue premissa central, hipóteses examinadas, pontos resistentes, pontos
quebrados ou condicionados, melhor argumento contrário, lacunas, perguntas e
diligências prioritárias, perspectivas simuladas e decisões humanas pendentes.
Acrescente somente o artefato próprio do modo.

Se nova informação ainda não foi analisada documental ou juridicamente, marque
`[verificar]` e encaminhe a etapa adequada antes de promovê-la.

Ao fechar com decisões humanas pendentes, ofereça `deliberacao-juridica`; não
conduza a decisão nesta skill. A deliberação também pode encaminhar um novo
aprofundamento. Nenhuma etapa absorve a outra.

## O que esta skill não faz

- Não pesquisa legislação, jurisprudência, pessoas, patrimônio ou fatos externos.
- Não substitui `analise-documental` nem `analise-juridica-civel`.
- Não transforma hipótese simulada em fato, prova ou posição de terceiro.
- Não redige peça, parecer ou comunicação.
- Não conduz a decisão do advogado sobre o que fazer com a análise; oferece
  `deliberacao-juridica` ao fechar.
- Não simula que audiência, reunião, negociação ou diligência aconteceu.

> Documento gerado com suporte de inteligência artificial. Conteúdo sujeito à
> revisão e validação obrigatória pelo advogado responsável antes de qualquer
> uso profissional ou processual.
