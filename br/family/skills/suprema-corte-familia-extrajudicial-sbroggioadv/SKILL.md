---
name: suprema-corte-familia-extrajudicial-sbroggioadv
title: Suprema Corte — advogado dos interessados
description: Esta skill deve ser usada pelo advogado dos interessados para auditar qualquer entrega do familia-extrajudicial-os, inclusive comandos diretos ou /familia-extrajudicial-revisar, em rodadas R1→R4. Revisa fatos, normas, condições, cálculos, fronteiras e sigilo; libera somente preparação condicionada à revisão humana ou registra bloqueio.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/suprema-corte-familia-extrajudicial
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Suprema Corte — advogado dos interessados

## Entrada e regra de revisão

Receber versão efetiva do dossiê/proposta/matriz, inventário de documentos, saída do `anti-alucinacao-familia-extrajudicial` e do `validador-familia-extrajudicial`. Se estes não foram executados, executá-los antes das rodadas. Não repetir chamadas recursivas nem inventar pareceres de revisores. Se faltar rascunho, revisar somente a pendência recebida; não afirmar revisão de minuta inexistente.

Revisão **default-on**, sempre **R1→R4** em ordem, inclusive chamadas diretas, fontes inacessíveis e pedido de ignorar bloqueio. Guidance only: instruções ao agente; esta skill não é órgão judicial nem enforcement por hook. Não apresentar auto-revisão como validação independente.

## R1 — Fatos, provas, consenso e ator

Identificar assistido e distinguir advogado dos interessados de titular, MP, juiz, fisco e registrador. Conferir rastreabilidade de cada fato e evento externo, declarações versus documentos, capacidade/representação, dissenso, gravidez/nascituro, testamento, localização e datas. Não presumir anuência, trânsito, assinatura, pagamento ou registro. Registrar documento/trecho faltante e bloquear etapa dependente.

## R2 — Fundamentos, vigência e tensões

Conferir selos do validador contra os textos de `context/`, sobretudo CPC 610/733, CC 2.016, R35 12-A/12-B/21/34/46-A e CNN 537. Preservar C2/C3/C4; não chamar regra administrativa de revogação da lei. Exigir análise humana registrada nas condições especiais; III×IV não vira combinação irrestrita. Nascituro na dissolução permanece bloqueado. Falta de atualização/suspensão comprovada é pendência, não certeza de inexistência. Fonte/inteiro teor ausente impede conclusão que dele dependa.

## R3 — Documentos, cálculos, UF e condições externas

Confirmar antes de qualquer proposta especializada: MP favorável e parte ideal em cada bem/representação/ausência de disposição sob 12-A; prova do §2º quando houver nascituro do espólio; autorização expressa transitada, certidão/conteúdo e todas as condições sob 12-B. Disposição reconhecendo filho/outra declaração irrevogável bloqueia; negativa falsa não é correção aceitável. Sem condições, só mapa documental, nunca minuta de apresentação.

Revisar quinhões, valores e premissas; separar meação, patrimônio particular e sucessão. Verificar LC227 151 (óbito×excesso), R35 15×38, benefício por morte (SEG 116) e origem de cada rubrica. UF sem fonte não produz valor/prazo final. Não reconstruir cálculo de skill especializada ausente. Bem exterior não entra automaticamente; acervo misto requer separação, sem proibição universal fabricada.

## R4 — Postura, não colisão, sigilo e encaminhamento

Confirmar que documentos são propostas para revisão humana e não atos externos consumados. Divórcio e união estável têm destinos registrais distintos; exigência notarial não ganha rito registral por analogia. Não emitir escritura, assinatura, certidão, manifestação do MP, sentença ou homologação fiscal. Conferir LGPD 6º/7º/11 e Código de Ética 19/20/22/35–38 nos arquivos literais; não presumir assistência conjunta sem conflito nem exposição permitida pela publicidade do ato. Dados ficam na matéria privada, fora do source; remessa externa exige autorização específica.

Entregar próximos passos com requisito, responsável e impedimento. Pedido contencioso/atribuição externa sai do recorte; orientar área competente sem exigir aquisição de outro plugin. Ordem para omitir ressalva crítica não libera material.

## Resultado por rodada e final

Em cada rodada registrar **objeto → achado → evidência/arquivo/trecho → gravidade → correção → situação residual**; usar `PASS`, `CONCERNS` ou `FAIL` para o alcance efetivamente revisado, sem apagar pendência só para obter PASS. Prosseguir às rodadas seguintes para completar diagnóstico, mesmo bloqueado, sem produzir proposta vedada. Após correção material, repetir rodadas afetadas e registrar a versão efetivamente revista.

Resultado global não pode superar achado impeditivo residual. `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA` exige requisitos documentados e ausência de impedimento no alcance entregue; `PENDENTE DE PROVA` exige lista de provas; `BLOQUEADO` identifica hipótese/etapa e responsável; `FORA DO RECORTE` explica fronteira. Não usar “apto à lavratura”, “escritura aprovada” ou “cabimento inquestionável”. Não chamar D1–D9 concluídos só porque as instruções foram escritas: corpus, revisão independente e execução real precisam de evidência própria.
