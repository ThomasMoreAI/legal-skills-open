---
name: assistencia-e-representacao-familiar-sbroggioadv
title: Assistência e representação familiar
description: Esta skill deve ser usada quando o pedido envolver advogado assistente, procurador, mandato, poderes especiais, assinaturas ou representação de interessado em ato familiar extrajudicial. Distingue assistência técnica de substituição da parte e entrega quadro de representação para conferência humana.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/assistencia-e-representacao-familiar
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Assistência e representação familiar

> C1 · Atuação do advogado dos interessados; preparação e acompanhamento, sem atribuições da serventia.

## Entradas e fontes

Identificar ato/operação, assistidos, capacidade e eventual representante legal, cônjuges, consenso, domicílios, presença/modalidade, instrumento integral e data, poderes, cláusulas, prazo expresso e prova de autoria. Não presumir que advogado também é mandatário ou que pessoa acompanhante representa incapaz.

Ler `context/cpc-familia-extrajudicial.md`, arts. 610, §2º, e 733, §2º; `context/res-cnj-35-compilada.md`, arts. 8, 12, 17, 36 (e 12-A/12-B/46-A conforme hipótese); `context/cc-familia-sucessoes.md`, arts. 657/661. Se analisar assistência conjunta/conflito, ler `context/codigo-etica-oab.md`, arts. 19–22; ausência de fonte ou dúvida na aplicação exige revisão humana.

## Execução

1. Separar, por pessoa, parte interessada, advogado assistente, defensor público, mandatário, representante legal e inventariante. Exigir instrumento/prova para a qualidade invocada, sem inferir poderes de inventariante para representar qualquer herdeiro.
2. Registrar assistência técnica e qualificação/assinatura do profissional exigidas pelo CPC. R35 8 dispensa procuração para a presença do advogado assistente; isso não dispensa mandato quando ele substitui a parte.
3. Em inventário/partilha, R35 12 admite viúvo/herdeiro capaz, inclusive emancipado, representado por instrumento público com poderes especiais. Não aplicar essa regra como autorização de representação de incapaz; conferir representação legal e condições do art. 12-A separadamente.
4. Em divórcio, R35 36 exige instrumento público, poderes especiais, descrição das cláusulas essenciais e validade de trinta dias para o mandatário do divorciando. Conferir data e termo do instrumento frente à data prevista do ato; dúvidas de contagem ficam pendentes. **Não estender trinta dias a toda procuração**, inventário ou assistência técnica. Na dissolução de união estável, examinar art. 46-A no que couber e registrar aplicação humana, sem automatismo.
5. Confrontar forma com CC 657 e extensão com CC 661: mandato geral só administra; atos que exorbitem exigem poderes especiais e expressos. Não criar texto de procuração pública nem reconhecer assinatura ou autenticidade.
6. Em renúncia/partilha transmissiva, identificar comparecimento dos cônjuges dos herdeiros nos termos de R35 17, com exceção de separação absoluta; não dispensar por mera afirmação sem prova do regime. Não extrapolar essa regra a toda operação familiar.
7. Mapear interesses e conflito concretos. CED 19–22 não autorizam assistência conjunta presumida: registrar análise do advogado, conflito superveniente, sigilo e eventual impedimento. Não escolher unilateralmente quem continuará assistido nem produzir mandato fictício.

## Bloqueios e saída específica

Falta de instrumento integral, poder, forma, validade ou representante comprovado → `PENDENTE DE PROVA` na assinatura/representação afetada; conflito não resolvido → `BLOQUEADO` na preparação conjunta. Litígio/peça judicial → `FORA DO RECORTE`.

Entregar quadro: interessado | capacidade/prova | papel | assistente | signatário previsto | instrumento/arquivo/trecho | forma/poderes/cláusulas | prazo e alcance | conflito | condição externa | ação/responsável. Não afirmar assinatura realizada ou mandato válido sem exame/prova.

Declarar 🔴 a tensão CPC 610/CC 2.016 × R35 12-A/12-B, III–IV, e CPC 733 × R35 34 quando incidentes. B2 exige prova das condições, inclusive MP favorável, antes da proposta; B3 exige autorização expressa transitada, certidão e conteúdo examinados. Não tratar capacidade/representação comprovada como solução automática do cabimento nem ocultar nascituro na dissolução.

## Controles e contrato de entrega

Aplicar, inclusive em chamada direta, `anti-alucinacao-familia-extrajudicial` e `validador-familia-extrajudicial` antes de produzir conclusão. Conferir cada fundamento no anexo literal indicado: dispositivo, trecho, versão/captura, data do fato e alcance federal/local. Se faltar arquivo, prova ou controle, declarar pendência e não substituir por memória. São instruções ao agente (guidance only), não enforcement por hook nem automação comprovada.

Finalizar com `suprema-corte-familia-extrajudicial`, R1→R4 default-on: R1 fatos/provas/consenso e ator; R2 fundamentos/vigência/tensões; R3 documentos, UF e condições externas; R4 sigilo, postura, fronteira e encaminhamento. Não afirmar revisão executada sem registrar seus achados.

Identificar ato/operação, interessado assistido, consenso/divergências, UF(s), datas, modalidade, fontes/data de corte, documentos recebidos/faltantes, condição federal/local, responsável externo, próxima providência e impedimento. Usar quadro **requisito → prova → arquivo/trecho → responsável → situação**. Separar ausência de prova de impedimento jurídico.

Emitir `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`, com motivo e etapa afetada. Não certificar aptidão à lavratura, aprovação da escritura ou cabimento inquestionável. Guardar dados somente na pasta privada escolhida, separados por cliente/matéria; nunca no source nem em exemplos identificáveis. Não enviar documentos a serviços externos sem autorização específica. Suporte: luis@sbroggio.io.
