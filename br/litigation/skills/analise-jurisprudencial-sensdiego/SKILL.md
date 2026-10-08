---
name: analise-jurisprudencial-sensdiego
title: Análise jurisprudencial
description: Pesquisar e analisar precedentes brasileiros e comentário jurídico exclusivamente pelo conector Silo, com cobertura, aderência e verificação da íntegra. Use quando o usuário aceitar ou pedir pesquisa jurisprudencial estruturada, com tribunais, período, comparação com os fatos e distinção entre precedente e comentário.
author: sensdiego
author_url: https://github.com/sensdiego/codigo-aberto/tree/main/skills/analise-jurisprudencial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
sources:
- title: Resultado
  path: references/resultado.md
- title: Roteamento Silo
  path: references/roteamento-silo.md
---

# Análise jurisprudencial

Produza análise de aplicabilidade, não lista de ementas. A pesquisa é opcional e
usa somente o conector autenticado do Silo. Observe a
[disciplina compartilhada](../../references/disciplina.md) e o
[contrato de handoff](../../references/handoff.md).

## Entrada

Delimite questão jurídica, fatos comparáveis, tribunais ou órgãos relevantes,
período e finalidade. Prefira mapa jurídico confirmado; se faltar, registre a
limitação sem inventar enquadramento.

Se o usuário dispensar a pesquisa, registre `pesquisa dispensada` e encerre sem
bloquear análise ou redação posterior. Não atribua entendimento a tribunal.

## Execução pelo Silo

Leia [roteamento-silo.md](references/roteamento-silo.md). Descubra as
capabilities reais em runtime e execute a cadeia necessária sem gates por
consulta, plano, anonimização, logging ou consentimento por sessão.

Não chame diretamente web, navegador ou serviço externo. Capability ausente ou
cobertura insuficiente limita somente o resultado dependente; não autoriza
suplementação silenciosa.

## Análise

Para cada resultado, diferencie questão decidida, fundamento, autoridade,
situação processual, semelhanças, diferenças e distinguishing possível. Ementa
não equivale a inteiro teor. Comentário editorial não equivale a precedente.

Use [resultado.md](references/resultado.md) para a saída proporcional. Uma
questão simples pode receber resposta curta.

Se a pesquisa fechar com decisão humana pendente, ofereça
`deliberacao-juridica`; não conduza a decisão nesta skill.

## O que esta skill não faz

- Não pesquisa fora do Silo.
- Não transforma ausência no corpus em inexistência de precedente.
- Não usa comentário secundário para provar dispositivo, súmula ou julgamento.
- Não converte estatística histórica em chance numérica do caso concreto.
- Não inventa citação nem permite em peça resultado `não confirmado`.
- Não decide estratégia nem redige documento.

Resultado sem íntegra ou fundamento verificado recebe `[verificar]` e o estado
correspondente.

> Documento gerado com suporte de inteligência artificial. Conteúdo sujeito à
> revisão e validação obrigatória pelo advogado responsável antes de qualquer
> uso profissional ou processual.
