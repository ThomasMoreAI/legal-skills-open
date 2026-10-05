---
name: lacunas-estaduais-do-procedimento-sbroggioadv
title: Lacunas estaduais do procedimento
description: Esta skill deve ser usada quando houver dúvida sobre normas da UF, rito de exigência ou recusa, prazo local, emolumentos, ITCMD ou selo de escritura familiar. Entrega matriz federal e de lacunas estaduais sem preencher regra por analogia.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/lacunas-estaduais-do-procedimento
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Lacunas estaduais do procedimento

> C1 · Atuação do advogado dos interessados; preparação e acompanhamento, sem atribuições da serventia.

## Entradas e âncoras

Identificar UF(s) de cada dependência, ato, etapa, bens/domicílios, data relevante, tema (tributo, custo, selo, documentos, exigência, recusa ou registro), nota real se houver e fontes oficiais efetivamente fornecidas. UF do advogado não define automaticamente competência tributária ou registral.

Ler `context/res-cnj-35-compilada.md`, arts. 15/32/46; `context/lei-10169-emolumentos.md`, arts. 1º–4º; `context/lrp-familia-duvida.md`, arts. 198–204/296 **somente na matéria registral**. CNN 319/541 em `context/cnn-familia-centrais-eletronico.md` apenas nos seus âmbitos. B5 é decisão de escopo, não diploma jurídico.

## Execução

1. Construir mapa federal identificado como tal, separado de resposta local: obrigação federal | destinatário | condição | prova | etapa. R35 15 distingue obrigação fiscal de prova prévia de ITCMD no inventário; não presumir dispensa do tributo, prazo estadual ou extensão ao divórcio. O dever do tabelião de informar o fisco em cinco dias ou conforme legislação tributária não vira prazo do advogado para recolher.
2. Para cada UF/tema, listar fonte oficial necessária, órgão competente, dispositivo a conferir, versão/ano da tabela, vigência, alcance, documento disponível e consulta ainda necessária. Não criar arquivo estadual vazio com aparência de cobertura; fonte ainda não fornecida permanece lacuna.
3. Conferir tabela/lei estadual de emolumentos diante de EMOL 1º–4º: Estados/DF fixam valores; tabela e base são locais. Não transformar parâmetros federais em orçamento, percentual, isenção ou valor nacional. Orçamento de serventia é documento de caso, não prova suficiente da lei local.
4. Preservar exigência/recusa real e sua ciência. R35 32 distingue declaração de valores pelo inventariante e recusa fundamentada por escrito no §2º; R35 46 trata da recusa de divórcio por indícios de prejuízo/dúvida de vontade. O advogado analisa e encaminha; não emite recusa com fé pública.
5. Separar lavratura notarial de registro do título. LRP 198–204/296 disciplina dúvida registral no alcance capturado; não criar rito nacional de dúvida notarial por analogia, nem importar os quinze dias de impugnação para toda nota notarial. Remissões não capturadas, inclusive art. 188 e alcance literal de art. 1º, §1º, ficam pendentes quando essenciais; não citar conteúdo não capturado.
6. No registro de união estável, CNN 541 tem hipótese própria: título sem estado civil/assentos, certidões de outra serventia em quinze dias e certidão expedida há, no máximo, 90 dias (critério de atualidade no registro de união estável, CNN 541, parágrafo único). Não tornar esse prazo de apresentação ou critério de atualidade universais. No eletrônico, CNN 319 exige exame de regra estadual/distrital e exceções, sem presumir selo existente.
7. Marcar impacto de cada lacuna: apenas orçamento, recebimento/apresentação, representação, assinatura, tributo, registro ou outra etapa identificada. Se local essencial faltar, impedir conclusão dessa etapa e entregar mapa federal útil. Ausência em busca parcial não prova inexistência nacional de regra; silêncio do corpus não autoriza analogia com UF vizinha.

## Proibições e saída específica

**Nunca preencher regra estadual por analogia**: nem prazo, rito, tabela, alíquota, multa, isenção ou competência. Não prometer cobertura nacional nem usar norma administrativa como revogação da lei. Litígio/peça judicial ou planejamento tributário autônomo fica `FORA DO RECORTE`.

Entregar matriz: UF/tema | base federal e arquivo/trecho | fonte local necessária/recebida | versão/data | lacuna | órgão/responsável | situação | etapa impedida | próxima providência. Diferenciar 🟡 fonte local ainda não verificada de 🔴 extrapolação vedada; dúvida notarial sem rito comprovado fica pendente, não declaração absoluta de inexistência. Tensões de cabimento permanecem com a triagem/validador; uma tabela estadual não resolve CPC × R35.

## Controles e contrato de entrega

Aplicar, inclusive em chamada direta, `anti-alucinacao-familia-extrajudicial` e `validador-familia-extrajudicial` antes de produzir conclusão. Conferir cada fundamento no anexo literal indicado: dispositivo, trecho, versão/captura, data do fato e alcance federal/local. Se faltar arquivo, prova ou controle, declarar pendência e não substituir por memória. São instruções ao agente (guidance only), não enforcement por hook nem automação comprovada.

Finalizar com `suprema-corte-familia-extrajudicial`, R1→R4 default-on: R1 fatos/provas/consenso e ator; R2 fundamentos/vigência/tensões; R3 documentos, UF e condições externas; R4 sigilo, postura, fronteira e encaminhamento. Não afirmar revisão executada sem registrar seus achados.

Identificar ato/operação, interessado assistido, consenso/divergências, UF(s), datas, modalidade, fontes/data de corte, documentos recebidos/faltantes, condição federal/local, responsável externo, próxima providência e impedimento. Usar quadro **requisito → prova → arquivo/trecho → responsável → situação**. Separar ausência de prova de impedimento jurídico.

Emitir `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`, com motivo e etapa afetada. Não certificar aptidão à lavratura, aprovação da escritura ou cabimento inquestionável. Guardar dados somente na pasta privada escolhida, separados por cliente/matéria; nunca no source nem em exemplos identificáveis. Não enviar documentos a serviços externos sem autorização específica. Suporte: luis@sbroggio.io.
