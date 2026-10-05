---
name: sobrepartilha-negativo-e-adjudicacao-sbroggioadv
title: Sobrepartilha, inventário negativo e adjudicação
description: Prepara sobrepartilha, inventário negativo ou adjudicação pelo advogado dos interessados, com requisitos distintos e revisão humana. Use quando o pedido envolver bens descobertos após inventário, ausência de acervo ou herdeiro único.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/sobrepartilha-negativo-e-adjudicacao
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: trusts-and-estates
language: pt
---

# Sobrepartilha, inventário negativo e adjudicação

## Entrada

Identifique a variante. Receba inventário/partilha anterior e prova de encerramento, títulos dos bens novos/omitidos e sua localização; para negativo, documentos e diligências informados sobre ausência de acervo; para adjudicação, prova do herdeiro único e do direito à totalidade. Confirme dívidas/credores e capacidade atual, não apenas na data do óbito. Ausência de documento não prova ausência de bens ou de outros herdeiros.

## Âncoras

Leia `context/res-cnj-35-compilada.md`, arts. 25, 26, 27, 28, 29 e, quando pertinentes, 12-A/12-B/15; `context/cpc-familia-extrajudicial.md`, art. 610; `context/cc-familia-sucessoes.md`, art. 2.016. Remissões são localizadores, não transcrições.

## Procedimento e limites

1. Sobrepartilha (R35 25): conferir inventário anterior e bens objeto do complemento. A regra admite escritura inclusive após inventário judicial findo e quando o herdeiro hoje maior/capaz era menor/incapaz antes. Não estender a frase a incapacidade atual sem filtro do 12-A e análise humana da tensão. Não criar novo inventário judicial.
2. Negativo (R35 28): preparar proposta limitada à ausência de acervo demonstrada pelo dossiê. Registrar alcance das diligências e alegações, não emitir certidão universal de inexistência patrimonial. Não deduzir isenção fiscal geral, inexistência de dívidas ou quitação de credores.
3. Adjudicação (R35 26): somente um herdeiro com direito à totalidade; distinguir meação, dívidas e direitos de terceiros. Não produzir partilha entre vários sob esse nome. Para herdeiro menor/incapaz, preservar expressamente 12-A.
4. Credores não impedem por si só inventário/partilha/adjudicação (R35 27), mas isso não dispensa apuração de dívidas. Dúvidas sobre totalidade, bens omitidos, interessados ou controvérsia suspendem a proposta correspondente.

## Entrega específica

Dossiê e minuta da variante correta, vínculo documental com o ato anterior quando houver, quadro de bens/ausência declarada, interessados, dívidas, condições especiais e lacunas fiscais/locais. Explicite por que as outras variantes não correspondem ao pedido, sem ampliar o recorte.

## Controle de entrada e limites comuns

Atue pelo advogado dos interessados. Confirme ato, interessado assistido, consenso/divergências, UF(s), datas do óbito e do negócio, capacidade, nascituro, testamento, regime patrimonial, modalidade e documentos recebidos/faltantes. Guarde dados do caso apenas na pasta privada escolhida pelo operador, separados por cliente/matéria, nunca no source compartilhado. Não presuma assinatura, anuência, pagamento, protocolo, registro ou decisão.

Antes da proposta, execute `anti-alucinacao-familia-extrajudicial` e `validador-familia-extrajudicial`. Confira os anexos locais e seus trechos literais; use somente norma presente no corpus, preservando negadores, incisos, revogações e ressalvas. Na comparação literal, normalize apenas espaços/quebras. Registre diploma/dispositivo, arquivo/trecho, URL de origem do anexo, versão/captura, data do fato e do ato, alcance e pendência. Ausência de fonte, atualização ou decisão oficial é pendência, não prova negativa.

Menor/incapaz: só preparar proposta após prova de partes ideais em cada bem e MP favorável (R35 12-A, caput); representação comprovada (B2 / prova civil do representante); eficácia depende do MP e o envio cabe ao tabelião. Disposição de bens/direitos do incapaz é vedada (§1º). Nascituro do autor da herança: aguardar registro de nascimento com parentalidade ou prova de não nascimento com vida (§2º). Impugnação do MP/terceiro vai ao juízo (§4º). Sem provas, entregar apenas mapa de pendências. Não eliminar a tensão 🔴 CPC 610/CC 2.016 × R35 12-A/12-B, inclusive III × IV do 12-B.

Testamento: encaminhar à skill `inventario-com-testamento` e exigir condições da R35 12-B, I–V/§§1º–2º, inclusive autorização judicial expressa transitada, certidão e exame do conteúdo; reconhecimento de filho/outra declaração irrevogável impede escritura. A combinação de testamento com incapaz fica bloqueada para proposta enquanto não houver conciliação oficial específica comprovada e análise humana registrada; não basta cumprir uma lista formal. Nunca emitir negativa falsa de testamento (tensão 🔴 R35 21 × 12-B). Divergência ou demanda litigiosa: interromper proposta consensual e orientar encaminhamento, sem criar ação judicial. Bem no exterior não recebe escritura de inventário/partilha (R35 29).

Base federal não substitui lei, prazo, alíquota, rito, tabela ou prova da UF. R35 15 na redação 695/2026 dispensa prova prévia de ITCMD no inventário, não o tributo devido nem as condições próprias do incidente. Não declarar atualização exaustiva, cabimento inquestionável ou aprovação de serventia. Qualificação, lavratura, manifestação MP, decisão judicial, apuração fiscal e registro pertencem aos responsáveis externos.

## Saída e revisão obrigatória

Entregue quadro `requisito → prova → arquivo/trecho → responsável → situação`, fatos confirmados separados de hipóteses, fundamentos com selos ✅/🟡/🔴, documentos faltantes, minuta identificada como proposta quando permitida, próxima providência e impedimento. Use um estado: `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`. Lacuna impeditiva bloqueia minuta para apresentação; não basta um aviso junto de texto utilizável incompatível.

Ao final, chame nesta ordem `anti-alucinacao-familia-extrajudicial`, `validador-familia-extrajudicial` e `suprema-corte-familia-extrajudicial`, R1→R4 default-on: fatos/provas/consenso/ator; fundamentos/vigência/tensões; documentos/cálculos/UF/condições externas; postura/sigilo/encaminhamento. Corrija ou retire trechos reprovados antes da entrega. Se qualquer dependência estiver ausente ou não puder ser executada, registre a revisão pendente e não entregue proposta como revisada. Controles por instrução (guidance only), sem enforcement por hook. Suporte: luis@sbroggio.io.
