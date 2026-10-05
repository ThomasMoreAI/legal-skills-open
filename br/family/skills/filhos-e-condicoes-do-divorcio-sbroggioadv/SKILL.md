---
name: filhos-e-condicoes-do-divorcio-sbroggioadv
title: Filhos e condições do divórcio
description: Confere, pelo advogado dos interessados, filhos comuns, gravidez, decisões prévias e condições da preparação de divórcio consensual extrajudicial. Esta skill deve ser usada quando o advogado mencionar filhos menores ou incapazes, guarda, visitação, alimentos já decididos, nascituro ou declaração sobre filhos no divórcio em cartório. Não cria acordo judicial nem decide cabimento incontroverso.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/filhos-e-condicoes-do-divorcio
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Filhos e condições do divórcio

Atuar como apoio ao advogado dos interessados, produzindo quadro de provas e limites da preparação. A qualificação e a lavratura pertencem ao tabelião; decisões judiciais pertencem ao juízo.

## Quando usar e o que ler

Acionar antes de qualquer proposta de divórcio extrajudicial, mesmo se o relato disser “sem filhos”. Identificar ator e casamento; não aplicar este fluxo como autorização para dissolução de união estável, inventário ou atuação do delegatário. Pedido de ação de guarda/alimentos ou divórcio litigioso é `FORA DO RECORTE`.

Ler `context/res-cnj-35-compilada.md`, art. 34, caput e §§1º–3º, e art. 35, junto de `context/cpc-familia-extrajudicial.md`, art. 733. Usar trechos literais e metadados, verificando versão, corte documental, datas e limitações com o validador. Não usar notícia, memória ou remissão não conferida como norma. Fonte ausente/inacessível gera pendência do fundamento e impede conclusão dependente.

## Entrada

Receber interessado assistido, partes, certidão de casamento, consenso, capacidade dos cônjuges, UF(s), datas, modalidade e pasta privada. Identificar todos os filhos comuns: nome, nascimento, idade e eventual incapacidade comprovada. Reunir declarações reais e documentos dos filhos. Separar filho menor, filho maior incapaz e incapacidade do próprio cônjuge; a última não recebe autorização por uma norma relativa a filhos.

Receber declaração real sobre gravidez/conhecimento dessa condição, sem escrever como se tivesse sido prestada ao tabelião. R35 34, §1º prevê declaração de ausência de estado gravídico ou de desconhecimento; não impor exame clínico universal nem sugerir desconhecimento artificial diante de gravidez conhecida. Dado ausente deve permanecer ausente.

Havendo filho comum menor/incapaz, receber decisão judicial prévia completa e documentos pertinentes às três matérias: guarda, visitação e alimentos. Não tratar termo particular, acordo verbal ou decisão apenas de alimentos como prova de resolução de todos os temas. Registrar identidade dos abrangidos, juízo, processo, data, dispositivo e alcance atual demonstrado, sem inventar vigência da decisão por falta de notícia de alteração.

## Conferência e interrupções

1. Montar por filho a matriz `tema → solução judicial → arquivo/trecho → data/alcance → dúvida → responsável → situação`. Exigir prova da resolução judicial prévia de todas as questões de guarda, visitação e alimentos (R35 34, §2º). Lacuna de um tema impede proposta especializada; entregar `PENDENTE DE PROVA` e providência para obtenção do documento, sem produzir ação judicial.
2. Exigir registro de concordância das partes com a regulamentação judicial e vontade firme/consciente (R35 35), sem certificação de vontade pelo agente. Indícios de coação, hesitação ou divergência impedem tratar o caso como consensual. Não negociar nova decisão dos filhos no corpo da proposta cartorária.
3. Preservar explicitamente a tensão 🔴: o CPC 733 contém a condição de inexistência de nascituro ou filhos incapazes; R35 34, §2º admite a hipótese de filhos comuns menores/incapazes com resolução judicial prévia. A resolução não será descrita como revogação do CPC nem como solução definitiva da hierarquia normativa.
4. Antes de orientar cabimento ou liberar proposta especializada nessa hipótese, exigir análise jurídica humana registrada: responsável, data, fatos/documentos examinados, dois textos confrontados, conclusão fundamentada, alcance e ressalva da qualificação notarial. Sem esse registro, manter `PENDENTE DE PROVA`. Sua presença não elimina a tensão nem garante aceitação da serventia.
5. Não inventar trânsito em julgado geral como requisito textual do R35 34, §2º. Se requisito adicional depender de fonte, decisão ou norma local, identificar a origem e pendência específicas; não transportar autorização/trânsito do inventário com testamento para divórcio.
6. Dúvida de interesse do menor/incapaz deve ficar explícita. R35 34, §3º atribui ao tabelião submeter a questão ao juiz prolator; o advogado organiza documentos e identifica a dependência, sem fabricar manifestação judicial, MP favorável ou protocolo. Não importar manifestação obrigatória do MP do inventário para este fluxo.
7. Nascituro/gravidez conhecida: `BLOQUEADO` para preparação neste produto, com requisito e encaminhamento humano. Não transplantar CNN sobre união estável, regra de nascituro do espólio ou declaração negativa fictícia. Estado desconhecido/relatos incompatíveis gera pendência de esclarecimento real, sem conclusão de inexistência.

## Saída

Entregar ato, ator, UF(s), datas/modalidade, fontes/corte, recebidos/faltantes, declarações com sua origem, quadro por filho, matriz `requisito → prova → arquivo/trecho → responsável → situação`, registro humano quando exigível, tensão preservada e próxima providência com impedimento.

Sem filho comum declarado, registrar o relato e seu suporte, sem atribuir prova absoluta de inexistência. Com condições comprovadas e análise humana exigível registrada, retornar a `preparacao-de-divorcio-extrajudicial` com estado `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`. Demais saídas: `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`. Não entregar minuta de apresentação enquanto houver impedimento; não declarar “apto à lavratura”.

Preservar dados mínimos e sigilo. Material do caso fica exclusivamente na pasta privada escolhida, separado por cliente/matéria, sem cópia no source ou divulgação externa automática.

## Revisão final obrigatória

Executar sempre ao final, inclusive por comando direto e em saída de pendências:

1. `anti-alucinacao-familia-extrajudicial` sobre fatos, provas, declarações, decisão e registro humano; remover afirmações sem suporte.
2. `validador-familia-extrajudicial` sobre redação, vigência, alcance, UF e tensão; fonte não conferida não recebe selo positivo.
3. `suprema-corte-familia-extrajudicial`, default-on: R1 fatos/provas/consenso/ator → R2 fundamentos/vigência/tensões → R3 documentos/UF/condições externas → R4 postura/sigilo/fronteira/encaminhamento.

Registrar achados de cada rodada e repetir a cadeia após correções. Revisão indisponível ou pedido de ignorar requisito impede entrega especializada; manter o quadro de pendências com controle faltante identificado. Não afirmar revisão executada apenas por existir esta instrução. Guidance only: são instruções ao agente, sem enforcement por hook nem decisão jurídica automática.
