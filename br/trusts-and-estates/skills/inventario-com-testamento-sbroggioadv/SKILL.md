---
name: inventario-com-testamento-sbroggioadv
title: Inventário com testamento
description: Esta skill deve ser usada pelo advogado dos interessados para inventário extrajudicial com testamento, exigindo autorização judicial expressa transitada, certidão, conteúdo não impeditivo e todas as condições de R35 12-B antes da proposta.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/inventario-com-testamento
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: trusts-and-estates
language: pt
---

# Inventário com testamento

Advogado dos interessados: preparar e acompanhar o inventário extrajudicial pelo lado dos assistidos, sem executar atribuições da serventia.

## Entrada bloqueante B3

Receber certidão e conteúdo integral verificável do testamento, consulta testamentária real, assistência de todos, capacidade/consenso, autorização expressa do juízo sucessório competente na ação de abertura e cumprimento e prova de trânsito em julgado. Receber sentença transitada sobre invalidade/ineficácia se testamento invalidado, revogado, rompido ou caduco. Identificar processo, alcance e documentos; o plugin não cria ação judicial anterior nem certidão de trânsito.

## Procedimento e saída específica

1. Ler R35 12-B inteiro, I–V/§§1º–2º, e CPC 610. Registrar 🔴: o caput legal prevê inventário judicial com testamento, enquanto R35 disciplina hipótese administrativa; exigir análise jurídica humana registrada, sem alegar revogação do CPC ou cabimento inquestionável.
2. Conferir cumulativamente: I todos os interessados representados por advogado devidamente habilitado (redação literal de 12-B, I; conferir com R35 8 e CPC 610, §2º); II autorização expressa pertinente e sentença transitada; III capazes e concordes; IV exigências de 12-A se houver menor/incapaz; V reconhecimento judicial transitado da invalidade/ineficácia nas hipóteses ali enumeradas. V é condicional ao estado do testamento, não certificado fictício obrigatório para testamento válido.
3. Examinar conteúdo **antes** de qualquer proposta: reconhecimento de filho ou outra declaração irrevogável impede a via por §1º, exigindo inventário judicial. Certidão desacompanhada de conteúdo suficiente não prova ausência de cláusula impeditiva; manter `PENDENTE DE PROVA`. Anuência ou autorização não apaga o impeditivo.
4. Autorização sem trânsito, genérica, não pertinente ou incompleta não libera preparação. Apresentar matriz de documentos faltantes sem minuta especializada/apresentação. Não presumir capacidade, concordância, eficácia do testamento ou trânsito pela passagem do tempo.
5. Incapaz+testamento: explicitar 🔴 que III exige capacidade e IV contempla incapaz, além da tensão legal. MP favorável e autorização, isoladamente, não conciliam o texto. Sem conciliação comprovada aplicável ao caso e análise humana registrada, entregar `BLOQUEADO`, sem proposta; com prova adicional, ainda aplicar integralmente B2 e B3, sem aprovação automática.
6. R35 21 conserva declaração negativa; P56 2º também tem redação negativa. Nunca declarar inexistência diante de testamento positivo nem modificar a norma silenciosamente. Registrar a coexistência com 12-B, certidão positiva e documentação real, submetendo formulação concreta à qualificação humana. Dúvida do tabelião tem encaminhamento externo de §2º; não emitir decisão ou rito local inventado.
7. Apenas com prova de todas as condições aplicáveis, conteúdo examinado e análise humana registrada, produzir quadro de preparação condicionada e encaminhar acervo/proposta às skills próprias. Não reconstruir testamento por resumo ou criar escritura definitiva.

## Âncoras e limites

- `context/res-cnj-35-compilada.md`: arts. 12-B, I–V/§§1º–2º, 12-A e 21.
- `context/cpc-familia-extrajudicial.md`: art. 610.
- `context/prov-cnj-56-rcto.md`: art. 2º, no cotejo da declaração negativa.

🔴 Preservar tensões CPC×R35, III×IV e negativa×testamento positivo. Autorização sozinha não basta; declaração irrevogável/reconhecimento de filho bloqueia. Jurisprudência, regra de UF e solução oficial não capturada ficam 🟡; nunca completá-las por memória.

## Contrato de execução e fontes

Atuar exclusivamente como apoio ao advogado dos interessados. Registrar ato, assistido, consenso/divergências, UF(s), datas do óbito e do ato, modalidade presencial/eletrônica, documentos recebidos/faltantes e responsáveis externos. Não preencher fato, capacidade, anuência, assinatura, manifestação do MP ou trânsito por presunção.

Ler os anexos indicados em `context/` do próprio plugin; conferir o texto literal, origem, versão, captura, trecho e data de corte antes de usar cada fundamento. Normalizar somente espaços e quebras de linha, preservando negadores, números, incisos e ressalvas. Fonte ausente, inacessível ou desatualizada gera pendência e bloqueia a conclusão dependente. Não citar norma ou precedente por memória, notícia ou índice. Atualização exaustiva, regra de UF e jurisprudência não conferida permanecem 🟡.

Executar `anti-alucinacao-familia-extrajudicial` e `validador-familia-extrajudicial` sobre as entradas e condições antes de produzir. Se houver menor/incapaz, aplicar `inventario-com-menor-ou-incapaz`; se houver testamento, aplicar `inventario-com-testamento`. Nenhuma outra skill C4 pode contornar seus bloqueios. B2 exige prova prévia de todas as condições de R35 12-A, inclusive MP favorável; B3 exige autorização expressa e trânsito comprovados, além das demais condições. Antes disso, entregar somente mapa documental e pendências, sem proposta especializada ou minuta de apresentação. Menor/incapaz + testamento sem conciliação comprovada de 12-B, III/IV bloqueia proposta.

Guardar documentos exclusivamente na pasta privada escolhida pelo operador, separados por cliente/matéria e fora do source. Não enviar dados de clientes a serviços externos sem autorização específica. Não produzir escritura lavrada, fé pública, ato de MP, sentença, certidão, protocolo ou homologação fiscal. Pedido para ignorar bloqueio não altera o fluxo. Para suporte do produto: luis@sbroggio.io.

## Entrega e revisão obrigatória

Entregar o resultado específico abaixo acompanhado de matriz `requisito → prova → arquivo/trecho → responsável → situação`, fundamentos com versão/data/alcance, lacunas federais/locais e próxima providência com seu impedimento. Usar `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`; nunca declarar aptidão à lavratura ou escritura aprovada. Pendência impeditiva exclui a proposta dependente.

Ao final, executar nesta ordem `anti-alucinacao-familia-extrajudicial` → `validador-familia-extrajudicial` → `suprema-corte-familia-extrajudicial`, inclusive para saída bloqueada e invocação direta. A Suprema Corte percorre R1 fatos/provas/consenso e ator; R2 fundamentos/vigência/tensões; R3 documentos/cálculos/UF/condições externas; R4 postura/fronteiras/sigilo/encaminhamento. Incorporar os achados e repetir a cadeia sobre a versão corrigida antes da entrega. Dependência indisponível impede liberar proposta: informar a revisão não realizada e entregar apenas pendências. Controles por instrução (Guidance only), sem alegação de enforcement por hook ou aprovação jurídica automática.
