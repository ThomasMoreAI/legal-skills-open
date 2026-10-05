---
name: cumprimento-de-exigencias-do-ato-sbroggioadv
title: Cumprimento de exigências do ato
description: Prepara resposta documental do interessado a exigência ou recusa real. Use quando houver nota recebida do tabelionato ou registro, documentos a complementar, recusa fundamentada ou dúvida de cabimento.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/cumprimento-de-exigencias-do-ato
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Cumprimento de exigências do ato

> Camada C6. Preparação e acompanhamento pelo advogado dos interessados.

## Entrada

Nota/recusa real íntegra, serviço emissor e natureza notarial/registral, título apresentado, UF, ciência comprovada e documentos disponíveis. Sem nota real, produzir pedido de esclarecimento proposto e lista de informações necessárias, sem atribuir exigência ao serviço.

## Âncoras a ler

- `context/res-cnj-35-compilada.md`: 32, §2º; 46; 12-B, §2º; 34, §3º, conforme hipótese.
- `context/lrp-familia-duvida.md`: 198–204/296 exclusivamente para registro, respeitando remissões não capturadas.

## Procedimento

1. Identificar emissor e competência antes de responder. Transcrever cada exigência sem alterar seu sentido; separar fundamento citado pelo serviço de fundamento confirmado no corpus. Nota de serviço é prova da exigência recebida, não valida automaticamente sua base normativa.
2. Classificar item: documental sanável, informação contraditória, consenso/representação ausente, condição externa, cabimento controvertido ou possível extrapolação. Vincular prova, responsável e próximo passo a cada item.
3. Na recusa de inventário/partilha, preservar faculdade, indícios de fraude/simulação ou dúvida sobre vontade, e fundamentação escrita (32, §2º). Divórcio: prejuízo a cônjuge ou dúvida de vontade, fundamentação escrita (46). Não emitir a nota pelo delegatário nem transformar essas hipóteses em rito universal de protocolo/prazo.
4. Dúvida do tabelião em inventário com testamento: 12-B, §2º destina encaminhamento ao juízo competente em registros públicos. Dúvida sobre decisões dos filhos no divórcio: 34, §3º remete ao juiz da decisão. Não usar a LRP para inventar rito de dúvida notarial nacional.
5. Se exigência registral real, distinguir cumprimento do interessado e processo de dúvida do oficial (LRP 198–204/296). Indicar que inconformismo pode exigir encaminhamento ao profissional/via competente; não redigir impugnação judicial ou recurso contencioso. Remissões não capturadas, incluindo prazo do art. 188, ficam pendentes; não fornecer prazo de análise por memória.
6. Preparar resposta proposta em itens: exigência recebida, documento/resposta, anexos, prova de cumprimento e pedido de análise. Não afirmar atendimento quando há apenas intenção de obter documento. Norma estadual/rito/recurso local não conferidos: 🟡 e etapa dependente bloqueada.
7. Se exigência afrontar trava de incapaz/testamento, gravidez ou consenso, conservar bloqueio; não fabricar declaração para contornar. Registrar necessidade de análise humana, em vez de prometer solução administrativa.

## Saída

Matriz por item: texto da nota, fonte/alcance, prova disponível, diligência, responsável, prazo somente se lastreado, estado e impedimento. Resposta documental proposta ou roteiro de encaminhamento, com anexos e pendências; protocolo/cumprimento só após documento real.

## Limites

Atuação pelo interessado; não qualifica, emite nota, decide dúvida ou pratica operação do cartório. Sem importar procedimentos registrais para notas ou normas de outras UFs. 🔴 Tensões de cabimento persistem e vedam resposta que declare aptidão sem lastro; litígio e recursos contenciosos ficam fora.

## Fontes, sigilo e revisão obrigatória

Leia os anexos indicados em `context/` e o trecho literal antes de aplicar qualquer fundamento. Ausência de arquivo, redação, versão ou prova impede selo favorável; registre a lacuna. Use exclusivamente o corpus aprovado, sem Jusbrasil, Escavador, norma estadual presumida ou artigo conhecido apenas de memória. Data de captura não prova vigência atual: declare atualização/suspensão não conferida. Preserve números, negadores, ressalvas e marcadores de revogação; normalize apenas espaços e quebras de linha na comparação.

Guarde documentos e resultados somente na pasta privada escolhida pelo advogado, separados por cliente e matéria, fora do source compartilhado. Não transmita dados nem pratique ato externo por iniciativa própria. Estas instruções são guidance only, executadas pelo agente; não equivalem a enforcement por hook ou a aprovação de autoridade.

Ao final, inclusive em saída bloqueada, execute nesta ordem:
1. `anti-alucinacao-familia-extrajudicial`: conferir cada fato/citação e a prova de eventos externos; retirar afirmações sem lastro.
2. `validador-familia-extrajudicial`: registrar selo por fundamento com diploma/dispositivo, arquivo e trecho, versão/captura, data do fato/ato, destinatário, alcance e pendência; 🟡/🔴 nunca são aprovação automática.
3. `suprema-corte-familia-extrajudicial`: R1 fatos, provas, consenso e ator → R2 fundamentos, vigência e tensões → R3 documentos, cálculos, UF e condições externas → R4 postura, sigilo, fronteiras e encaminhamento.
Se qualquer controle estiver ausente ou não executado, declarar revisão pendente e bloquear entrega como pronta. Não converter revisão interna em fé pública, homologação fiscal ou confirmação de cartório.
