---
name: preparacao-de-divorcio-extrajudicial-sbroggioadv
title: Preparação de divórcio extrajudicial
description: Prepara, pelo advogado dos interessados, quadro de cláusulas e pendências do divórcio consensual extrajudicial. Esta skill deve ser usada quando o advogado pedir preparação do divórcio em cartório, documentos de casamento, acordo sobre nome, alimentos ou proposta para revisão humana. Não atua como tabelião nem prepara litígio.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/preparacao-de-divorcio-extrajudicial
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Preparação de divórcio extrajudicial

Atuar como apoio ao advogado dos interessados, organizando provas e proposta consensual para revisão humana. Não qualificar nem lavrar escritura com fé pública.

## Acionamento e fontes

Acionar para casamento confirmado e pedido de divórcio consensual. Pedido ambíguo exige identificar ator, vínculo e objetivo; não converter união estável em casamento. Separação judicial nova, litígio, tutela e recurso são `FORA DO RECORTE`; encaminhar à assistência jurídica competente sem gerar peça judicial.

Ler os trechos literais de `context/cpc-familia-extrajudicial.md` (arts. 731 e 733) e `context/res-cnj-35-compilada.md` (arts. 33–36 e 40–44). Conferir redação, metadados, data do fato/ato e limitações do recorte com o validador. O art. 731 entra por remissão de conteúdo do art. 733; não cria rito nacional de petição notarial. Não preencher artigo ou norma estadual por memória. Fonte ausente ou inacessível impede a afirmação dependente e gera pendência, sem interromper a organização documental permitida.

## Entrada e condições anteriores à proposta

1. Identificar interessado assistido, partes, objetivo, consenso livre, capacidade, UF(s), datas relevantes, modalidade presencial/eletrônica e pasta privada do caso. Registrar divergência e quem a apresentou; não presumir anuência por silêncio.
2. Reunir certidão de casamento, identidade oficial e CPF, pacto antenupcial se houver, documentos dos filhos e títulos de bens/direitos quando existentes, conforme R35 art. 33. Vincular cada dado ao arquivo e trecho; ausência de certidão não autoriza inventar assento ou regime.
3. Receber vontade real de cada parte, eventual alteração/manutenção do nome, posição sobre alimentos entre cônjuges, bens e partilha. Declarações do art. 35 são das partes; não redigir declaração como já assinada ou prestada.
4. Acionar `filhos-e-condicoes-do-divorcio` em todo caso, inclusive declaração de inexistência de filhos. Sem seu quadro de provas e, quando houver filhos menores/incapazes, análise jurídica humana registrada da tensão CPC 733 × R35 34, não produzir proposta especializada ou minuta de apresentação. Nascituro/gravidez conhecida bloqueia preparação neste fluxo; nunca simular declaração negativa.
5. Acionar `acordo-patrimonial-do-divorcio` se houver bens ou transferências. Sem patrimônio, registrar a declaração e seu alcance; não inferir inexistência de bens de falta de anexos. Partilha diferida exige distinção expressa entre vínculo e patrimônio, sem converter disputa patrimonial em acordo fictício.
6. Conferir assistência de advogado/defensor (CPC 733, §2º). Havendo mandatário, acionar `assistencia-e-representacao-familiar`: R35 36 requer instrumento público com poderes especiais, cláusulas essenciais e validade de trinta dias. Não generalizar esse prazo a toda procuração nem produzir instrumento público. Modalidade eletrônica demanda `preparacao-de-ato-eletronico`; UF demanda `lacunas-estaduais-do-procedimento` quando necessária à etapa.

## Procedimento e saída

Montar quadro `tema → manifestação de cada parte → documento/trecho → cláusula proposta → pendência → responsável`. Separar nome, alimentos dos cônjuges, questões dos filhos já resolvidas judicialmente e patrimônio. Não alterar guarda, visitação ou alimentos dos filhos por acordo cartorário novo. R35 44 admite retificação consensual de obrigações alimentares ajustadas no divórcio; não transformar isso em ação de revisão ou regra para substituir decisão judicial dos filhos.

Entregar identificação do ato/ator/UF/datas/modalidade, fontes e corte documental, índice de recebidos/faltantes, quadro `requisito → prova → arquivo/trecho → responsável → situação`, cláusulas propostas somente se condições comprovadas, ressalvas federais/locais e próxima providência com seu impedimento. Usar um estado: `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`.

Havendo lacuna impeditiva, entregar somente mapa documental e de providências, sem minuta de apresentação. Com condições demonstradas, encaminhar o quadro a `requerimento-e-minuta-de-proposta-familiar`; marcar qualquer texto como proposta sujeita à revisão humana. Não afirmar “apto à lavratura” ou aprovação cartorária.

Orientar futura apresentação do traslado real ao RCPN do assento de casamento para averbação (R35 40/43), distinguindo a atribuição registral de nome (41) e registros patrimoniais. Não fabricar traslado, assinatura, protocolo, averbação ou prazo local. R35 42 não autoriza divulgar o dossiê: preservar sigilo e dados mínimos; guardar material por cliente/matéria na pasta privada, nunca no source. Não exigir consulta de testamento universal no divórcio sem sucessão.

## Revisão final obrigatória

Executar ao final, inclusive no acionamento direto e na entrega de pendências:

1. `anti-alucinacao-familia-extrajudicial`: enviar proposta, fontes e provas; retirar afirmações sem suporte e bloquear a etapa dependente.
2. `validador-familia-extrajudicial`: conferir dispositivos, versão, temporalidade, alcance e UF; conservar tensão crítica e lacunas explícitas.
3. `suprema-corte-familia-extrajudicial`: executar R1 fatos/provas/consenso/ator → R2 fundamentos/vigência/tensões → R3 documentos/cálculos/UF/condições externas → R4 postura/sigilo/fronteira/encaminhamento, default-on.

Se houver correção, repetir a cadeia sobre a saída corrigida. Controle indisponível ou pedido para ignorá-lo impede entrega especializada: registrar o controle faltante e manter somente pendências. Registrar achados de cada rodada; não chamar instrução de revisão de teste executado. Estas travas são orientação ao agente (Guidance only), sem enforcement por hook ou garantia de decisão notarial.
