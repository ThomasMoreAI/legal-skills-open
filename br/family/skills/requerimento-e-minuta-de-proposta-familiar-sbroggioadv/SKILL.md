---
name: requerimento-e-minuta-de-proposta-familiar-sbroggioadv
title: Requerimento e minuta de proposta familiar
description: Consolida dossiê e propostas especializadas em requerimento e minuta para revisão humana. Use para preparar apresentação ao tabelionato em inventário, divórcio ou união estável após conferência das condições.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/requerimento-e-minuta-de-proposta-familiar
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Requerimento e minuta de proposta familiar

> Camada C6. Preparação e acompanhamento pelo advogado dos interessados.

## Entrada

Dossiê rastreável, ato escolhido, destinatário e UF; propostas das skills especializadas, consentimento real, representação comprovada, valores/patrimônio e fundamentos; selos e decisões humanas sobre tensões; condições externas já documentadas. Não preencher dados desconhecidos com exemplos identificáveis.

## Âncoras a ler

- `context/cpc-familia-extrajudicial.md`: arts. 610 e 733, §2º; conteúdo do 731 por remissão, sem importar rito judicial.
- `context/res-cnj-35-compilada.md`: 8, 11–12-B, 18–24/32 para inventário; 33–39/43/46-A para divórcio e dissolução, conforme ato.
- `context/cc-familia-sucessoes.md`: art. 215 como fronteira da escritura lavrada pelo tabelião; demais bases materiais apenas se aplicáveis e conferidas nas propostas especializadas.

## Procedimento e travas de apresentação

1. Conferir compatibilidade entre ato, fatos e propostas. Documento faltante com efeito impeditivo bloqueia minuta de apresentação: produzir apenas quadro de pendências, sem pacote marcado como apto. Litígio ou dissenso encaminham à revisão humana/via adequada, sem peça contenciosa.
2. Menor/incapaz: exigir prova de representação, parte ideal em cada bem e MP favorável (12-A), sem disposição de bens/direitos. Nascituro do espólio exige prova do §2º. Preservar 🔴 CPC 610/CC 2.016 × R35; análise humana registrada não dispensa condições nem resolve a tensão por si.
3. Testamento: certidão, conteúdo, autorização expressa e trânsito comprovados, demais condições de 12-B; reconhecimento de filho/declaração irrevogável bloqueiam. Incapaz + testamento sem conciliação comprovada de III/IV bloqueia; nunca declarar inexistência artificial de testamento.
4. Divórcio com filhos incapazes: comprovar decisão sobre guarda, visitação e alimentos (34, §2º), exigir análise jurídica humana registrada de CPC 733 × R35 34 antes da orientação de cabimento; não inventar trânsito como requisito geral daquele parágrafo. Gravidez/nascituro não desaparece por declaração falsa. Gravidez conhecida no divórcio: a declaração do R35 34, §1º não pode ser prestada e o CPC 733 exclui o caso; saída BLOQUEADO, com encaminhamento humano. Dissolução de união estável com nascituro permanece 🔴 e bloqueada.
5. Conferir documentos e assinaturas por ato: CPC 610, §2º (inventário) / 733, §2º (divórcio e união) e R35 8; assistência não equivale a mandato da parte. Proposta patrimonial exige base civil completa e classificação fiscal. Não aplicar comunhão parcial indistintamente nem fixar frações sucessórias por memória.
6. Consolidar requerimento com destinatário confirmado, qualificação mínima necessária, objeto, síntese factual com fonte, pedido de análise/lavratura pelo serviço, índice dos anexos e pendências. Sem rito nacional notarial derivado de CPC 731.
7. Minuta: título destacado **MINUTA DE PROPOSTA — PARA REVISÃO HUMANA**; organizar cláusulas propostas de acordo com o ato, indicando fonte de cada fato, vontade e cálculo. Divórcio: bens, alimentos, nome e situação dos filhos conforme remissão aplicável; inventário: interessados, meação/acervo, quinhões e condições; união: operação escolhida e seus limites. Não forjar declarações de comparecimento, leitura, assinatura, fé pública, recolhimento ou lavratura.
8. Conferir anexos, coerência de nomes/datas/valores e mapa de responsabilidades. Só após gates sem pendência impeditiva emitir rascunho para conferência pelo advogado; qualificação final e lavratura são do serviço.

## Saída

Requerimento proposto + minuta marcada + índice de anexos + quadro de fatos/fundamentos/provas + demonstrativos rastreáveis + selos/pendências e providências posteriores. Se bloqueada, entregar pendências e etapa impedida, sem minuta de apresentação apta.

## Limites

Não é escritura, certidão, assinatura, protocolo ou decisão real. Lacuna impeditiva não é removida por campo vazio. Nenhum ato de fé pública, ação judicial prévia, fraude documental ou promessa de aceitação. 🔴 Tensões normativas permanecem declaradas, mesmo após decisão humana.

## Fontes, sigilo e revisão obrigatória

Leia os anexos indicados em `context/` e o trecho literal antes de aplicar qualquer fundamento. Ausência de arquivo, redação, versão ou prova impede selo favorável; registre a lacuna. Use exclusivamente o corpus aprovado, sem Jusbrasil, Escavador, norma estadual presumida ou artigo conhecido apenas de memória. Data de captura não prova vigência atual: declare atualização/suspensão não conferida. Preserve números, negadores, ressalvas e marcadores de revogação; normalize apenas espaços e quebras de linha na comparação.

Guarde documentos e resultados somente na pasta privada escolhida pelo advogado, separados por cliente e matéria, fora do source compartilhado. Não transmita dados nem pratique ato externo por iniciativa própria. Estas instruções são guidance only, executadas pelo agente; não equivalem a enforcement por hook ou a aprovação de autoridade.

Ao final, inclusive em saída bloqueada, execute nesta ordem:
1. `anti-alucinacao-familia-extrajudicial`: conferir cada fato/citação e a prova de eventos externos; retirar afirmações sem lastro.
2. `validador-familia-extrajudicial`: registrar selo por fundamento com diploma/dispositivo, arquivo e trecho, versão/captura, data do fato/ato, destinatário, alcance e pendência; 🟡/🔴 nunca são aprovação automática.
3. `suprema-corte-familia-extrajudicial`: R1 fatos, provas, consenso e ator → R2 fundamentos, vigência e tensões → R3 documentos, cálculos, UF e condições externas → R4 postura, sigilo, fronteiras e encaminhamento.
Se qualquer controle estiver ausente ou não executado, declarar revisão pendente e bloquear entrega como pronta. Não converter revisão interna em fé pública, homologação fiscal ou confirmação de cartório.
