---
name: preparacao-de-ato-eletronico-sbroggioadv
title: Preparação de ato eletrônico
description: Esta skill deve ser usada quando o advogado pedir preparação de participação no e-Notariado, escritura familiar eletrônica ou híbrida, videoconferência, assinatura digital ou conferência de competência remota. Produz mapa de dependências sem lavrar ou operar a plataforma pela serventia.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/preparacao-de-ato-eletronico
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Preparação de ato eletrônico

> C1 · Atuação do advogado dos interessados; preparação e acompanhamento, sem atribuições da serventia.

## Entradas e fonte literal

Fixar ato/operação, interessados, capacidade/representação, domicílios comprovados, localização dos bens, identificação do adquirente se pertinente, serventia cogitada, UF(s), datas, modalidade eletrônica/híbrida, documentos e recursos de acesso. Não coletar senhas, certificados privados ou biometria.

Ler `context/cnn-familia-centrais-eletronico.md`, arts. 286/287/289/292/302–306/313/318/319; para fronteira presencial/condições familiares, `context/res-cnj-35-compilada.md`, arts. 1º/12-A/12-B/34/46-A, e `context/cpc-familia-extrajudicial.md`, arts. 610/733. O CNN é recorte da compilação de 20/08/2026, capturado em 30/09/2026, não prova atualização exaustiva nem inexistência de suspensão judicial. Art. 284 ficou fora do recorte: não transcrever por memória.

Para a tensão da partilha judicial com incapaz, conferir também `context/cc-familia-sucessoes.md`, art. 2.016; sua captura não resolve a conciliação normativa.

## Execução

1. Conferir primeiro condições do ato familiar. Modalidade eletrônica não sana ausência de MP favorável, autorização judicial transitada, representação, consenso ou prova. Sem gate, produzir somente mapa de pendências, nunca proposta especializada.
2. Pelo art. 286, distinguir videoconferência notarial para captar consentimento, concordância com os termos, assinatura digital das partes exclusivamente no e-Notariado, assinatura do tabelião com ICP-Brasil e formato de longa duração. Informar requisitos ao advogado; não atestar capacidade, consentimento ou gravação em lugar do notário.
3. Pelo art. 287, atribuir ao notário a lavratura no e-Notariado, videoconferência e coleta das assinaturas. Pelo art. 292, mapear acesso/perfis e certificado notarizado/biometria no alcance literal, distinguindo mera conferência de autenticidade de assinatura de ato. Cadastro ou acesso não prova assinatura.
4. Criar matriz de competência por hipótese: art. 289 (circunscrição/delegação); art. 302 (imóvel/domicílio do adquirente e seus parágrafos); art. 303 (ata e procuração eletrônica, somente fronteira); art. 304 (prova do domicílio). **Não oferecer algoritmo universal para divórcio, união estável e inventário**, nem aplicar o critério da ata ou procuração a toda escritura. Não transportar a livre escolha presencial de R35 1º como liberdade irrestrita remota. Exigir conferência humana da hipótese e confirmação externa da serventia, sem tratar resposta administrativa como norma.
5. Separar arquivo digitalizado de cópia autenticada/desmaterializada: arts. 305/306 reservam os atos próprios ao notário. Registrar arquivo, original disponível e verificação pendente; não autenticar, certificar autoria ou desmaterializar pelo plugin.
6. Para ato híbrido, art. 313 admite assinatura física de uma parte e remota de outra nos termos do CNN; não concluir que isso afasta competência/gates. Art. 318 veda recepção remota de assinaturas fora do e-Notariado: não indicar assinatura avulsa por outra plataforma como substituto. Atendimento por mensagem não equivale a lavratura.
7. Conferir art. 319 completo, inclusive exceções dos parágrafos, para selo estadual/distrital quando exigido. Encaminhar à `lacunas-estaduais-do-procedimento`; não emitir selo nem afirmar cobertura de todas as UFs.

## Limites e saída específica

Marcar 🟡 atualização/suspensões, competência concreta, selo da UF, fidelidade final do recorte e operação real não comprovada. Fonte oficial ausente não recebe selo de vigência; não navegar nem transmitir dados do cliente por conta própria para concluir a operação.

Declarar 🔴 tensões de menor/incapaz/testamento (CPC 610/CC 2.016 × R35 12-A/12-B) e filhos incapazes (CPC 733 × R35 34); **nascituro na dissolução bloqueia preparação** mesmo que seja alegada decisão judicial sob CNN 537, §6º. Manter hipótese do nascituro do espólio separada.

Entregar: requisito eletrônico | artigo/arquivo/trecho | hipótese concreta | prova | responsável externo | situação | próxima providência/etapa impedida. Incluir mapa de competência, assinaturas/videoconferência, originais/autenticação, selo e condições familiares. Nunca declarar operação testada ou ato eletrônico concluído apenas porque o checklist está preenchido.

## Controles e contrato de entrega

Aplicar, inclusive em chamada direta, `anti-alucinacao-familia-extrajudicial` e `validador-familia-extrajudicial` antes de produzir conclusão. Conferir cada fundamento no anexo literal indicado: dispositivo, trecho, versão/captura, data do fato e alcance federal/local. Se faltar arquivo, prova ou controle, declarar pendência e não substituir por memória. São instruções ao agente (guidance only), não enforcement por hook nem automação comprovada.

Finalizar com `suprema-corte-familia-extrajudicial`, R1→R4 default-on: R1 fatos/provas/consenso e ator; R2 fundamentos/vigência/tensões; R3 documentos, UF e condições externas; R4 sigilo, postura, fronteira e encaminhamento. Não afirmar revisão executada sem registrar seus achados.

Identificar ato/operação, interessado assistido, consenso/divergências, UF(s), datas, modalidade, fontes/data de corte, documentos recebidos/faltantes, condição federal/local, responsável externo, próxima providência e impedimento. Usar quadro **requisito → prova → arquivo/trecho → responsável → situação**. Separar ausência de prova de impedimento jurídico.

Emitir `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`, com motivo e etapa afetada. Não certificar aptidão à lavratura, aprovação da escritura ou cabimento inquestionável. Guardar dados somente na pasta privada escolhida, separados por cliente/matéria; nunca no source nem em exemplos identificáveis. Não enviar documentos a serviços externos sem autorização específica. Suporte: luis@sbroggio.io.
