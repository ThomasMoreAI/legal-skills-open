---
name: analise-documental-sensdiego
title: Análise documental
description: Interpretar documentos de caso civil em fatos, atos, cronologia, relações probatórias, contradições e lacunas, sempre com fonte e localizador. Use depois do intake ou quando o usuário pedir análise factual e documental sem escolher estratégia nem redigir.
author: sensdiego
author_url: https://github.com/sensdiego/codigo-aberto/tree/main/skills/analise-documental
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
sources:
- title: Avaliacao Probatoria
  path: references/avaliacao-probatoria.md
- title: Contrato Saida
  path: references/contrato-saida.md
---

# Análise documental

Transforme fontes inventariadas em material interpretado que outra skill possa
usar. Observe a [disciplina compartilhada](../../references/disciplina.md), o
[contrato de handoff](../../references/handoff.md) e a
[biblioteca do CPC](../../references/legislacao/cpc/README.md).

## Entrada

Verifique identidade do caso, lente representada, fontes, cobertura e
localizadores. Se o intake estiver ausente ou insuficiente, repare somente o
inventário necessário antes de analisar; não simule completude.

Defina o escopo da rodada: primeira análise, módulo específico ou atualização
por documento novo. Para a estrutura de saída, leia
[contrato-saida.md](references/contrato-saida.md). Para relacionar fatos e
provas, leia [avaliacao-probatoria.md](references/avaliacao-probatoria.md).

## Pacote adaptado

Se a entrada declarar `case-adaptation-v1`, valide recibo, identidade, lente,
elegibilidade e intake obrigatório. `bloqueado` não autoriza análise;
`parcial_utilizavel` limita cada conclusão à cobertura declarada; `integral`
exige recibo positivo expresso.

Consuma o handoff opcional de análise documental somente quando cada achado
trouxer proposição, fonte, localizador, estado, frente, cobertura, conflito e
alcance da confirmação. Sem esses elementos, trate o conteúdo como material de
intake e analise apenas as fontes efetivamente acessíveis. Preserve frentes,
deltas e conflitos; fonte posterior não controla apenas por ser mais recente.
Sem recibo de adaptação, aplique normalmente o contrato comum.

## Módulos

Execute somente os módulos materiais ao pedido:

- **fatos:** proposições verificáveis, relato, fonte e localizador;
- **atos e efeitos:** declarações, contratos, comunicações, decisões,
  intimações e efeitos expressos no próprio material;
- **cronologia:** quando ordem, intervalo ou sequência mudar a compreensão;
- **avaliação probatória:** relação entre fato material, suporte, oposição e
  lacuna;
- **contradições e lacunas:** versões incompatíveis, ausência material e limite
  de cobertura.

Identifique o estágio processual ou contexto extrajudicial demonstrado pelas
fontes, sem escolher tese, recurso, providência ou estratégia.

## Disciplina de leitura

- Toda afirmação material aponta para fonte e localizador reproduzível.
- Reabra o original antes de usar aspas; paráfrase não recebe aspas.
- OCR inseguro recebe `[verificar]`; não complete o texto por contexto.
- Preserve separadamente fato documental, informação do usuário, inferência,
  hipótese, conteúdo contraditado e item pendente.
- Busca sem resultado e arquivo ausente não provam inexistência.
- Contradição bloqueia somente a conclusão dependente dela.

## Atualização documental

Documento novo não reinicia automaticamente a análise. Compare cada achado
afetado e classifique o delta usando exatamente estes rótulos, sem sinônimos:
`confirma`, `complementa`, `contradiz`, `substitui` ou `não afeta`. Preserve o
restante e devolva à confirmação humana somente conteúdo novo ou materialmente
alterado.

## Saída

Produza handoff de tipo `análise documental` com os dez campos comuns, matriz
fato-prova, cronologia quando útil, estágio demonstrado, contradições, lacunas e
itens para confirmação humana. Informe fontes não lidas ou parcialmente lidas.

O resultado pode encerrar a tarefa. Não force análise jurídica ou redação.

## O que esta skill não faz

- Não pesquisa legislação, jurisprudência ou comentário jurídico.
- Não decide mérito, suficiência jurídica final, estratégia ou chance de êxito.
- Não redige peça, parecer, relatório jurídico conclusivo ou comunicação.
- Não resolve contradição apagando uma versão.
- Não transforma documento derivado em fonte original sem registrar a cadeia.

> Documento gerado com suporte de inteligência artificial. Conteúdo sujeito à
> revisão e validação obrigatória pelo advogado responsável antes de qualquer
> uso profissional ou processual.
