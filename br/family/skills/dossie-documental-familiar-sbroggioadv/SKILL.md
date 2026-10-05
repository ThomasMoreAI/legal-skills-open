---
name: dossie-documental-familiar-sbroggioadv
title: Dossiê documental familiar
description: Esta skill deve ser usada quando o advogado pedir documentos para divórcio, união estável ou inventário extrajudicial, checklist de certidões, organização de acervo ou documento faltante. Produz índice rastreável por ato, sem presumir validade ou condição externa.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/dossie-documental-familiar
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Dossiê documental familiar

> C1 · Atuação do advogado dos interessados; preparação e acompanhamento, sem atribuições da serventia.

## Entradas e fontes

Fixar operação (inclusive qual escritura de união estável), partes, vínculos, capacidade, filhos/nascituro, testamento, bens, UF(s), modalidade e datas. Receber inventário dos documentos com origem, emissor, data, formato, arquivo e trecho; distinguir declaração do cliente de documento e de prova de ato externo.

Ler `context/res-cnj-35-compilada.md`, arts. 20–24, 33–34, e `context/cnn-familia-centrais-eletronico.md`, art. 541. Para os gates, ler CPC 610/733 em `context/cpc-familia-extrajudicial.md`, R35 12-A/12-B/15/38/46-A e, se houver testamento, `context/prov-cnj-56-rcto.md`, arts. 1º–2º. Não ampliar consulta obrigatória RCTO a divórcio sem sucessão.

Para a tensão da partilha judicial com incapaz, conferir também `context/cc-familia-sucessoes.md`, art. 2.016; sua captura não resolve a conciliação normativa.

## Execução

1. Criar índice com identificador, categoria, titular pseudonimizado, origem, emissão, formato, arquivo/trecho e finalidade. Não marcar autenticidade a partir de simples digitalização.
2. No inventário, mapear qualificação das partes/cônjuges e do falecido (20–21); documentos do art. 22: óbito, identidade oficial/CPF, parentesco, casamento e pacto quando houver, propriedade imobiliária, titularidade de móveis/direitos se houver (art. 22, f), certidão negativa de tributos e CCIR se imóvel rural. Conferir originais/cópias autenticadas e identidade original pelo art. 23; vincular cada documento à menção prevista no art. 24.
3. No divórcio, mapear o art. 33: casamento, identidade/CPF, pacto se houver, nascimento/identidade dos filhos, propriedade de imóveis/direitos e titularidade de móveis/direitos se houver. Pelo art. 34, identificar filhos, incapacidade e informação gravídica real. Declaração não substitui prévia resolução judicial de guarda, visitação e alimentos quando exigida pelo §2º; não criar declaração artificial de inexistência de gravidez.
4. Para união estável, separar declaração/reconhecimento, convenção e dissolução. Examinar a aplicação no que couber do art. 46-A, sem importar automaticamente todos os documentos de casamento. Vias registrais recebem apenas orientação.
5. Classificar por item: recebido, ausente, incompleto, divergente, não aplicável com fundamento ou dependente de fonte local. Indicar responsável e etapa impedida. Acionar `assistencia-e-representacao-familiar` para instrumentos/poderes e `lacunas-estaduais-do-procedimento` para adicionais locais; não criar exigência por costume.

## Travas específicas

- CNN 541 trata do registro quando o título não indica estado civil/assentos: 15 dias para apresentar certidões de outra serventia e certidão expedida há, no máximo, 90 dias (critério de atualidade no registro de união estável, CNN 541, parágrafo único). Não universalizar esses números para escrituras ou todos os documentos. Validade sem fonte aplicável fica pendente.
- R35 22, g, não restabelece prova prévia de recolhimento de ITCMD abolida para inventário pela redação atual do art. 15; isso não dispensa tributo devido nem elimina o art. 38 para divórcio.
- Menor/incapaz: o caput do art. 12-A exige parte ideal em cada um dos bens e manifestação favorável do MP; sem prova de qualquer condição, limitar a coleta/pendências, sem proposta especializada.
- Separadamente, conferir prova da representação legal do incapaz (B2); o mandato do interessado capaz segue R35 12. Sem prova da representação aplicável, manter coleta/pendências, sem proposta especializada. Testamento: certidão, conteúdo e autorização expressa transitada do art. 12-B são provas externas, não campos presumidos.
- 🔴 CPC 610/CC 2.016 × R35 12-A/12-B, III–IV; CPC 733 × R35 34; nascituro na dissolução; R35 21 × 12-B: preservar tensões e análise humana registrada. Nunca exigir negativa falsa de testamento. Nascituro no espólio tem condição própria no art. 12-A, §2º.

## Saída específica

Entregar índice e checklist: documento/requisito | ato | fundamento/trecho | origem/arquivo | formato | validade e fonte | situação | responsável | próxima ação/etapa impedida. Destacar contradições documentais e condições externas sem confundi-las com arquivos meramente faltantes.

## Controles e contrato de entrega

Aplicar, inclusive em chamada direta, `anti-alucinacao-familia-extrajudicial` e `validador-familia-extrajudicial` antes de produzir conclusão. Conferir cada fundamento no anexo literal indicado: dispositivo, trecho, versão/captura, data do fato e alcance federal/local. Se faltar arquivo, prova ou controle, declarar pendência e não substituir por memória. São instruções ao agente (guidance only), não enforcement por hook nem automação comprovada.

Finalizar com `suprema-corte-familia-extrajudicial`, R1→R4 default-on: R1 fatos/provas/consenso e ator; R2 fundamentos/vigência/tensões; R3 documentos, UF e condições externas; R4 sigilo, postura, fronteira e encaminhamento. Não afirmar revisão executada sem registrar seus achados.

Identificar ato/operação, interessado assistido, consenso/divergências, UF(s), datas, modalidade, fontes/data de corte, documentos recebidos/faltantes, condição federal/local, responsável externo, próxima providência e impedimento. Usar quadro **requisito → prova → arquivo/trecho → responsável → situação**. Separar ausência de prova de impedimento jurídico.

Emitir `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`, com motivo e etapa afetada. Não certificar aptidão à lavratura, aprovação da escritura ou cabimento inquestionável. Guardar dados somente na pasta privada escolhida, separados por cliente/matéria; nunca no source nem em exemplos identificáveis. Não enviar documentos a serviços externos sem autorização específica. Suporte: luis@sbroggio.io.
