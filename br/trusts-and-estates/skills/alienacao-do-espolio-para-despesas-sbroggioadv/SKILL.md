---
name: alienacao-do-espolio-para-despesas-sbroggioadv
title: Alienação do espólio para despesas
description: Prepara o incidente de alienação pelo inventariante para despesas do inventário, pelos seis requisitos da Resolução CNJ 35, art. 11-A. Use para venda de bens do espólio destinada a despesas, distinguindo cessão por herdeiro e direitos do incapaz.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/alienacao-do-espolio-para-despesas
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: trusts-and-estates
language: pt
---

# Alienação do espólio para despesas

## Entrada

Receba nomeação documentada do inventariante, bem/título/localização, interessados/capacidade, pesquisas reais sobre indisponibilidade, preço e vinculação proposta, despesas discriminadas, guias de todos os impostos de transmissão e valores, orçamentos das serventias e garantia real/fidejussória proposta. Confira data de venda e cronograma, sem inventar documento ou valor.

## Âncoras

Leia `context/res-cnj-35-compilada.md`, arts. 11, §§1º–2º, 11-A, caput/I–VI/§§1º–3º, 12-A, §1º, e 15; `context/cc-familia-sucessoes.md`, art. 1.793, §§2º–3º, para distinguir disposição por herdeiro. Não atribuir poderes bancários ao 11-A, §2º.

## Matriz obrigatória dos seis requisitos

| Requisito R35 11-A | Prova a conferir | Pendência impeditiva |
|---|---|---|
| I — discriminação das despesas do inventário | impostos de transmissão, honorários, emolumentos notariais/registrais e outros tributos/despesas devidos pela escritura | rubrica/valor sem lastro |
| II — parte ou todo o preço vinculado às despesas do I | valor, destinação e mecanismo propostos, com documentos reais | preço livre sem vinculação |
| III — ausência de indisponibilidade de bens de quaisquer herdeiros ou cônjuge/convivente sobrevivente | fontes/documentos de pesquisa, sujeitos abrangidos e alcance temporal | ausência presumida ou indisponibilidade constatada |
| IV — menção de guias de todos os impostos de transmissão apresentadas e valores | guias reais e respectivos valores | guia/valor faltante |
| V — valores estimados dos emolumentos e serventias que orçaram | orçamentos reais notariais/registrais e identificação das emitentes | orçamento ou serventia inventados |
| VI — garantia real ou fidejussória do inventariante para destinação do produto | proposta/documentos de garantia para qualificação humana | garantia ausente/não comprovada |

Para cada linha, acrescente arquivo/trecho, responsável e situação; requisitos são cumulativos. Bloquear proposta de apresentação até prova de todos. Não fabricar certidão, guia, orçamento ou aceitação de garantia. A autorização por escritura é ato externo do tabelião, não resultado do plugin.

## Procedimento e limites

1. R35 11-A permite autorização ao inventariante por escritura para móveis/imóveis do espólio, independentemente de autorização judicial, sob as condições acima. Não converter em alienação genérica, planejamento ou poder de qualquer herdeiro. Distinguir da disposição pelo herdeiro sob CC 1.793, §§2º–3º; não prometer conciliação irrestrita.
2. A vedação de disposição de bens/direitos do incapaz (12-A, §1º) permanece: 11-A não a dispensa. Identifique alcance sobre quinhão/meação ideal e bloqueie proposta incompatível; MP favorável não elimina a vedação.
3. §1º: pagamento das despesas em até um ano contado da venda, admitido prazo inferior pelas partes. Registrar venda comprovada e prazo pactuado; não tratar como prazo fiscal universal, prorrogação de ITCMD ou contagem da nomeação do inventariante.
4. §2º: cumprimento da obrigação de pagar despesas extingue a garantia. Exigir comprovantes de cumprimento antes de afirmar extinção no caso. Poder de informações bancárias/fiscais e levantamento para despesas está em 11, §2º, para o inventariante nomeado nos termos do §1º; não está em 11-A, §2º.
5. §3º: relacionar bem vendido no acervo para emolumentos, quinhões e ITCMD; não o incluir como objeto da partilha. Consignar proposta de menção da venda prévia com prova, sem declarar venda inexistente ou retirar o bem dos cálculos.
6. R35 15, redação 695/2026, não justifica apagar guias e valores expressamente exigidos por 11-A, IV. Distinguir apresentação de guias da prova de recolhimento prévio; não criar dispensa ou obrigação além do texto. Tributos e cronograma local seguem fonte oficial da UF.

## Entrega específica

Matriz de seis requisitos, despesas/preço/garantia, cronograma de até um ano, prova da venda quando ocorrida e controle de inclusão nos cálculos/exclusão da partilha; proposta identificada para revisão humana ou mapa de impedimentos.

## Controle de entrada e limites comuns

Atue pelo advogado dos interessados. Confirme ato, interessado assistido, consenso/divergências, UF(s), datas do óbito e do negócio, capacidade, nascituro, testamento, regime patrimonial, modalidade e documentos recebidos/faltantes. Guarde dados do caso apenas na pasta privada escolhida pelo operador, separados por cliente/matéria, nunca no source compartilhado. Não presuma assinatura, anuência, pagamento, protocolo, registro ou decisão.

Antes da proposta, execute `anti-alucinacao-familia-extrajudicial` e `validador-familia-extrajudicial`. Confira os anexos locais e seus trechos literais; use somente norma presente no corpus, preservando negadores, incisos, revogações e ressalvas. Na comparação literal, normalize apenas espaços/quebras. Registre diploma/dispositivo, arquivo/trecho, URL de origem do anexo, versão/captura, data do fato e do ato, alcance e pendência. Ausência de fonte, atualização ou decisão oficial é pendência, não prova negativa.

Menor/incapaz: só preparar proposta após prova de partes ideais em cada bem e MP favorável (R35 12-A, caput); representação comprovada (B2 / prova civil do representante); eficácia depende do MP e o envio cabe ao tabelião. Disposição de bens/direitos do incapaz é vedada (§1º). Nascituro do autor da herança: aguardar registro de nascimento com parentalidade ou prova de não nascimento com vida (§2º). Impugnação do MP/terceiro vai ao juízo (§4º). Sem provas, entregar apenas mapa de pendências. Não eliminar a tensão 🔴 CPC 610/CC 2.016 × R35 12-A/12-B, inclusive III × IV do 12-B.

Testamento: encaminhar à skill `inventario-com-testamento` e exigir condições da R35 12-B, I–V/§§1º–2º, inclusive autorização judicial expressa transitada, certidão e exame do conteúdo; reconhecimento de filho/outra declaração irrevogável impede escritura. A combinação de testamento com incapaz fica bloqueada para proposta enquanto não houver conciliação oficial específica comprovada e análise humana registrada; não basta cumprir uma lista formal. Nunca emitir negativa falsa de testamento (tensão 🔴 R35 21 × 12-B). Divergência ou demanda litigiosa: interromper proposta consensual e orientar encaminhamento, sem criar ação judicial. Bem no exterior não recebe escritura de inventário/partilha (R35 29).

Base federal não substitui lei, prazo, alíquota, rito, tabela ou prova da UF. R35 15 na redação 695/2026 dispensa prova prévia de ITCMD no inventário, não o tributo devido nem as condições próprias do incidente. Não declarar atualização exaustiva, cabimento inquestionável ou aprovação de serventia. Qualificação, lavratura, manifestação MP, decisão judicial, apuração fiscal e registro pertencem aos responsáveis externos.

## Saída e revisão obrigatória

Entregue quadro `requisito → prova → arquivo/trecho → responsável → situação`, fatos confirmados separados de hipóteses, fundamentos com selos ✅/🟡/🔴, documentos faltantes, minuta identificada como proposta quando permitida, próxima providência e impedimento. Use um estado: `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`. Lacuna impeditiva bloqueia minuta para apresentação; não basta um aviso junto de texto utilizável incompatível.

Ao final, chame nesta ordem `anti-alucinacao-familia-extrajudicial`, `validador-familia-extrajudicial` e `suprema-corte-familia-extrajudicial`, R1→R4 default-on: fatos/provas/consenso/ator; fundamentos/vigência/tensões; documentos/cálculos/UF/condições externas; postura/sigilo/encaminhamento. Corrija ou retire trechos reprovados antes da entrega. Se qualquer dependência estiver ausente ou não puder ser executada, registre a revisão pendente e não entregue proposta como revisada. Controles por instrução (guidance only), sem enforcement por hook. Suporte: luis@sbroggio.io.
