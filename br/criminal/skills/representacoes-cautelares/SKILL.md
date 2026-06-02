---
name: representacoes-cautelares
title: Representacoes Cautelares
description: Redacao de representacoes cautelares policiais e pedidos judiciais investigativos, com organizacao de fatos, indicios, fundamentos legais e pedidos delimitados. Use quando Codex precisar produzir peca para o Juizo envolvendo prisao preventiva, busca e apreensao, quebra de sigilo telefonico/telematico/bancario, medidas cautelares diversas, sequestro ou bloqueio de bens, sigilo processual, ou combinacao dessas medidas, a partir de autos, relatorios, PDFs, DOCX, TXT, planilhas e outros elementos da investigacao.
author: diegocamara89
author_url: https://github.com/diegocamara89/ai-skills-hub/tree/main/all-skills/representacoes-cautelares
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: criminal
language: pt
---

# Representacoes Cautelares

Redija pecas cautelares dirigidas ao Juizo, com foco em necessidade, adequacao, proporcionalidade e delimitacao objetiva dos pedidos.
Use esta skill para pedir medida investigativa ou constritiva. Nao use como template de relatorio final de inquerito.

## Fluxo de trabalho

1. Identificar a medida principal e as medidas acessorias.
2. Montar a base fatico-probatoria minima antes de redigir.
3. Delimitar alvos, locais, contas, linhas, aparelhos, IPs, e-mails, objetos e periodo.
4. Fundamentar cada medida com requisitos proprios e elementos concretos dos autos.
5. Formular pedidos objetivos, executaveis e individualizados.
6. Revisar risco de nulidade, excesso ou pedido generico.
7. Gerar a versao final em `.docx`, salvo se o usuario pedir expressamente apenas texto.

## Escolha da variante

- Para prisao preventiva, busca e apreensao, medidas cautelares diversas ou peca combinada, ler `references/modelo-prisao-busca-cautelares.md`.
- Para quebra de sigilo telefonico, telematico, bancario ou fiscal, ler `references/modelo-quebra-sigilo.md`.
- Para decidir a estrutura da peca e quando combinar capitulos, ler `references/variantes.md`.
- Para geracao e padrao visual do Word, ler `references/formatacao-docx.md`.
- Antes de entregar, ler `references/checklist-qualidade.md`.
- Se precisar de pedidos secundarios recorrentes, ler `references/pedidos-acessorios.md`.

## Estrutura base da peca

Adote, em regra, esta sequencia:

1. Enderecamento ao Juizo competente.
2. Identificacao do procedimento, investigados, vitima e tipificacao provisoria.
3. Preambulo com a autoridade policial, base legal de atuacao e medidas requeridas.
4. Sumario dos fatos, em ordem cronologica, com prejuizo e modus operandi quando relevantes.
5. Investigados e diligencias executadas, destacando a ligacao entre prova e alvo.
6. Fundamentacao juridica por medida requerida, em subtitulos separados.
7. Pedidos, em lista clara, na mesma ordem da fundamentacao.
8. Fechamento com local, data e assinatura.

Inclua capitulo autonomo de indiciamento apenas quando houver utilidade pratica para a peca, suporte probatorio suficiente e alinhamento com a estrategia do caso. Nao transforme toda representacao em mini-relatorio final.

## Regras de redacao

- Enderecar ao Juizo, nao ao Ministerio Publico.
- Narrar apenas os fatos necessarios para justificar a medida pedida.
- Individualizar a situacao de cada investigado e de cada medida.
- Delimitar periodo, provedores, numeros, contas, aparelhos, enderecos e objetos.
- Distinguir dado preterito armazenado de interceptacao em tempo real.
- Relacionar cada pedido a um objetivo investigativo concreto.
- Evitar fundamento abstrato sem apoio em fato contemporaneo dos autos.
- Evitar transcrever longos blocos de lei ou jurisprudencia; citar e aplicar.
- Pedir sigilo judicial, contraditorio diferido ou cumprimento inaudita altera pars somente com justificativa concreta.
- Em busca e apreensao, definir o que se busca e por que esses itens interessam a investigacao.
- Em cautelares pessoais, justificar por que a prisao e necessaria ou por que medida menos gravosa e suficiente.

## Base probatoria minima

Antes de redigir, confirmar pelo menos:

- resumo objetivo dos fatos investigados;
- indicios de autoria e materialidade;
- vinculacao entre alvo e medida;
- recorte temporal relevante;
- elementos que demonstrem necessidade e adequacao;
- dados identificadores dos alvos e objetos do pedido.

Se os autos forem volumosos, primeiro faca inventario de arquivos, linha do tempo e matriz simples de prova -> alvo -> medida -> pedido. So depois redija a representacao.

## Saida

Entregue, conforme o caso:

- minuta-base em Markdown ou TXT, quando necessario para revisao;
- minuta final em DOCX, por padrao, quando a peca estiver madura para entrega;
- resumo dos pedidos ao final, quando a peca combinar varias medidas.

## Geracao obrigatoria de DOCX

Quando a representacao estiver suficientemente consolidada:

1. usar a minuta textual como fonte;
2. aplicar a formatacao definida em `references/formatacao-docx.md`;
3. gerar `.docx` por meio do script `scripts/gerar_docx_representacao.py`, salvo se houver ferramenta mais adequada ja disponivel no ambiente;
4. confirmar ao usuario o caminho do arquivo entregue.

## Limites

- Nao usar esta skill como template principal de relatorio final de inquerito.
- Nao pedir medida sem suporte minimo nos autos.
- Nao copiar automaticamente capitulos defensaveis em uma peca e inadequados em outra.
