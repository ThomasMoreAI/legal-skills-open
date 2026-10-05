---
name: renuncia-hereditaria-na-via-extrajudicial-sbroggioadv
title: Renúncia hereditária na via extrajudicial
description: Prepara proposta de renúncia hereditária, distinguindo renúncia pura de transferência dirigida e verificando proibição de parcialidade, irrevogabilidade e efeitos civis e fiscais. Use para renúncia à herança ou ao legado na via extrajudicial.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/renuncia-hereditaria-na-via-extrajudicial
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: trusts-and-estates
language: pt
---

# Renúncia hereditária na via extrajudicial

## Entrada

Receba vontade informada, histórico de aceitação e atos já praticados, título sucessório, eventuais legados/quinhões sob títulos diversos, outros herdeiros e filhos, casamento/regime e documentos do cônjuge, destinatário pretendido, contraprestação e credores. Não presumir que ausência de instrumento de aceitação equivale a ausência de atos de aceitação.

## Âncoras

Leia `context/cc-familia-sucessoes.md`, arts. 1.806 e 1.808–1.813; `context/res-cnj-35-compilada.md`, arts. 17 e 12-A, §1º; `context/lc-227-2026-itcmd.md`, arts. 150, I, alíneas a–b, 151, II, d, e 182, III. São sínteses abaixo, não citações literais.

## Procedimento e limites

1. Antes de redigir, alertar e registrar ciência do interessado: aceitação e renúncia são irrevogáveis (CC 1.812). Se há aceitação anterior, não propor sua revogação por renúncia; submeter fatos e enquadramento ao advogado.
2. CC 1.808 proíbe aceitar/renunciar herança em parte, sob condição ou a termo. Bloquear pedido de percentual escolhido, prazo ou condição. §1º distingue legados de herança; §2º permite deliberar sobre quinhões chamados por títulos sucessórios diversos. Exigir prova desses títulos; não usar os parágrafos como permissão de renúncia parcial livre.
3. Forma expressa: instrumento público ou termo judicial (1.806). Aqui, preparar proposta do instrumento público para revisão, nunca termo judicial pronto ou renúncia formalizada fictícia.
4. Na sucessão legítima, acrescimento aos demais da mesma classe; sendo único, devolução à classe subsequente (1.810). Não generalizar à sucessão testamentária. Pelo 1.811, ninguém sucede representando renunciante; sendo único legítimo da classe ou renunciando todos os demais dela, filhos podem suceder por direito próprio e por cabeça. Demonstrar configuração, sem representação automática. Se herdeiro faleceu antes da aceitação, analisar hipótese e condições do 1.809 antes de definir quem decide.
5. R35 17 exige comparecimento dos cônjuges dos herdeiros na escritura de inventário/partilha com renúncia, salvo separação absoluta. Não transformar isso em dispensa geral de consentimento em outros negócios.
6. Separar renúncia em benefício do monte, sem ressalva/condição e sem ato demonstrativo de aceitação (LC227 150, I, a–b), da renúncia em favor de pessoa determinada, cujo marco de doação está em 151, II, d. Pedido dirigido não recebe rótulo de renúncia pura nem promessa de não incidência; encaminhar ao exame de cessão/negócio e fiscal da UF. Efeitos dos demais dispositivos em 182, III, vinculam-se à publicação, não à data de sanção de 13/01/2026.
7. Prejuízo aos credores exige ressalva: CC 1.813 admite aceitação por eles com autorização judicial; habilitação em 30 dias do conhecimento, e remanescente preserva renúncia após dívidas. Não orientar burla nem produzir pedido judicial. Disposição de direitos do incapaz fica bloqueada pelo 12-A, §1º.

## Entrega específica

Proposta de instrumento, quando permitida, com advertência prévia e quadro da vontade, forma, histórico, sucessores/efeitos, cônjuge, credores e enquadramento fiscal condicionado; nunca assinatura ou vontade certificada pelo plugin.

## Controle de entrada e limites comuns

Atue pelo advogado dos interessados. Confirme ato, interessado assistido, consenso/divergências, UF(s), datas do óbito e do negócio, capacidade, nascituro, testamento, regime patrimonial, modalidade e documentos recebidos/faltantes. Guarde dados do caso apenas na pasta privada escolhida pelo operador, separados por cliente/matéria, nunca no source compartilhado. Não presuma assinatura, anuência, pagamento, protocolo, registro ou decisão.

Antes da proposta, execute `anti-alucinacao-familia-extrajudicial` e `validador-familia-extrajudicial`. Confira os anexos locais e seus trechos literais; use somente norma presente no corpus, preservando negadores, incisos, revogações e ressalvas. Na comparação literal, normalize apenas espaços/quebras. Registre diploma/dispositivo, arquivo/trecho, URL de origem do anexo, versão/captura, data do fato e do ato, alcance e pendência. Ausência de fonte, atualização ou decisão oficial é pendência, não prova negativa.

Menor/incapaz: só preparar proposta após prova de partes ideais em cada bem e MP favorável (R35 12-A, caput); representação comprovada (B2 / prova civil do representante); eficácia depende do MP e o envio cabe ao tabelião. Disposição de bens/direitos do incapaz é vedada (§1º). Nascituro do autor da herança: aguardar registro de nascimento com parentalidade ou prova de não nascimento com vida (§2º). Impugnação do MP/terceiro vai ao juízo (§4º). Sem provas, entregar apenas mapa de pendências. Não eliminar a tensão 🔴 CPC 610/CC 2.016 × R35 12-A/12-B, inclusive III × IV do 12-B.

Testamento: encaminhar à skill `inventario-com-testamento` e exigir condições da R35 12-B, I–V/§§1º–2º, inclusive autorização judicial expressa transitada, certidão e exame do conteúdo; reconhecimento de filho/outra declaração irrevogável impede escritura. A combinação de testamento com incapaz fica bloqueada para proposta enquanto não houver conciliação oficial específica comprovada e análise humana registrada; não basta cumprir uma lista formal. Nunca emitir negativa falsa de testamento (tensão 🔴 R35 21 × 12-B). Divergência ou demanda litigiosa: interromper proposta consensual e orientar encaminhamento, sem criar ação judicial. Bem no exterior não recebe escritura de inventário/partilha (R35 29).

Base federal não substitui lei, prazo, alíquota, rito, tabela ou prova da UF. R35 15 na redação 695/2026 dispensa prova prévia de ITCMD no inventário, não o tributo devido nem as condições próprias do incidente. Não declarar atualização exaustiva, cabimento inquestionável ou aprovação de serventia. Qualificação, lavratura, manifestação MP, decisão judicial, apuração fiscal e registro pertencem aos responsáveis externos.

## Saída e revisão obrigatória

Entregue quadro `requisito → prova → arquivo/trecho → responsável → situação`, fatos confirmados separados de hipóteses, fundamentos com selos ✅/🟡/🔴, documentos faltantes, minuta identificada como proposta quando permitida, próxima providência e impedimento. Use um estado: `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`. Lacuna impeditiva bloqueia minuta para apresentação; não basta um aviso junto de texto utilizável incompatível.

Ao final, chame nesta ordem `anti-alucinacao-familia-extrajudicial`, `validador-familia-extrajudicial` e `suprema-corte-familia-extrajudicial`, R1→R4 default-on: fatos/provas/consenso/ator; fundamentos/vigência/tensões; documentos/cálculos/UF/condições externas; postura/sigilo/encaminhamento. Corrija ou retire trechos reprovados antes da entrega. Se qualquer dependência estiver ausente ou não puder ser executada, registre a revisão pendente e não entregue proposta como revisada. Controles por instrução (guidance only), sem enforcement por hook. Suporte: luis@sbroggio.io.
