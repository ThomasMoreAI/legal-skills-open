---
name: cessao-hereditaria-na-via-extrajudicial-sbroggioadv
title: Cessão hereditária na via extrajudicial
description: Prepara cessão do direito à sucessão aberta ou quinhão hereditário, com análise de preferência dos coerdeiros e limites sobre bens singulares. Use para cessão hereditária, ingresso de cessionário no inventário ou preferência sucessória.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/cessao-hereditaria-na-via-extrajudicial
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: trusts-and-estates
language: pt
---

# Cessão hereditária na via extrajudicial

## Entrada

Identifique cedente, coerdeiros, cessionário e relação com a sucessão; óbito/abertura, direito/quinhão/título, indivisibilidade do acervo, preço e condições, gratuidade ou onerosidade efetivamente documentadas, comunicações e ciência dos coerdeiros, data da transmissão, casamento/regime e títulos dos bens. Não inferir doação pela mera palavra cessão.

## Âncoras

Leia `context/cc-familia-sucessoes.md`, arts. 1.793, caput/§§1º–3º, 1.794 e 1.795, caput e parágrafo único; `context/res-cnj-35-compilada.md`, arts. 16/17/11-A/12-A, §1º; `context/lc-227-2026-itcmd.md`, arts. 147 e 151 apenas nas hipóteses concretamente comprovadas. Não usar CC 1.911 como se fosse a disciplina da cessão.

## Procedimento e limites

1. CC 1.793, caput: direito à sucessão aberta e quinhão do coerdeiro podem ser cedidos por escritura pública. Confirmar abertura; não vender sucessão futura por este módulo. Delimitar objeto, fração e título, sem atribuir titularidade exclusiva de bem ainda indiviso.
2. §1º: direitos por substituição ou acrescimento presumem-se não abrangidos por cessão anterior. Identificar a cronologia e não acrescentar tais direitos automaticamente ao objeto.
3. §2º: cessão pelo coerdeiro de direito hereditário sobre bem singular é ineficaz. §3º: disposição por herdeiro de bem do acervo, sem prévia autorização do juiz da sucessão e pendente indivisibilidade, também é ineficaz. Não preparar proposta que prometa livre eficácia; registrar obstáculo e análise/encaminhamento humano.
4. CC 1.794: coerdeiro tem preferência tanto por tanto quando a quota é cedida a estranho. Documentar preço/condições e conhecimento, sem inventar prazo nacional de notificação. CC 1.795: quem não soube pode haver a quota cedida a estranho, depositando o preço e requerendo em até 180 dias após a transmissão. Registrar prova da transmissão e marco do prazo, não da ciência; se vários exercerem preferência, distribuição proporcional às quotas (parágrafo único). Disputa exige encaminhamento, sem peça contenciosa.
5. R35 16: inventário extrajudicial promovido por cessionário, inclusive cessão parcial do acervo, exige todos os herdeiros presentes e concordes. Distinguir isso da validade/eficácia da cessão civil: anuência no inventário não elimina §§2º–3º ou preferência. R35 17 rege comparecimento dos cônjuges no inventário/partilha com transmissão, salvo separação absoluta; conferir enquadramento e prova do regime.
6. Alienação pelo inventariante sob R35 11-A é incidente distinto, tratado por `alienacao-do-espolio-para-despesas`. Não usá-lo para contornar CC 1.793, §3º, ou R35 12-A, §1º. A tensão entre disposição do herdeiro e autorização regulamentar do inventariante exige análise humana, sem conciliação irrestrita.
7. Classificar civil e fiscalmente o negócio real; somente aplicar LC227 147/151 ao alcance comprovado. Onerosidade, tipo de direito, competência, base e tributos locais dependem de documentos e fonte da UF; sem isso não prometer ITCMD/ITBI, alíquota ou isenção.

## Entrega específica

Proposta de cessão de direito/quinhão para revisão humana, quadro do objeto/título/preço, preferência e prova de comunicação/transmissão, concordância no inventário, cônjuges, ineficácias e lacunas fiscais. Se impeditivo, apenas diagnóstico e pendências, sem minuta incompatível.

## Controle de entrada e limites comuns

Atue pelo advogado dos interessados. Confirme ato, interessado assistido, consenso/divergências, UF(s), datas do óbito e do negócio, capacidade, nascituro, testamento, regime patrimonial, modalidade e documentos recebidos/faltantes. Guarde dados do caso apenas na pasta privada escolhida pelo operador, separados por cliente/matéria, nunca no source compartilhado. Não presuma assinatura, anuência, pagamento, protocolo, registro ou decisão.

Antes da proposta, execute `anti-alucinacao-familia-extrajudicial` e `validador-familia-extrajudicial`. Confira os anexos locais e seus trechos literais; use somente norma presente no corpus, preservando negadores, incisos, revogações e ressalvas. Na comparação literal, normalize apenas espaços/quebras. Registre diploma/dispositivo, arquivo/trecho, URL de origem do anexo, versão/captura, data do fato e do ato, alcance e pendência. Ausência de fonte, atualização ou decisão oficial é pendência, não prova negativa.

Menor/incapaz: só preparar proposta após prova de partes ideais em cada bem e MP favorável (R35 12-A, caput); representação comprovada (B2 / prova civil do representante); eficácia depende do MP e o envio cabe ao tabelião. Disposição de bens/direitos do incapaz é vedada (§1º). Nascituro do autor da herança: aguardar registro de nascimento com parentalidade ou prova de não nascimento com vida (§2º). Impugnação do MP/terceiro vai ao juízo (§4º). Sem provas, entregar apenas mapa de pendências. Não eliminar a tensão 🔴 CPC 610/CC 2.016 × R35 12-A/12-B, inclusive III × IV do 12-B.

Testamento: encaminhar à skill `inventario-com-testamento` e exigir condições da R35 12-B, I–V/§§1º–2º, inclusive autorização judicial expressa transitada, certidão e exame do conteúdo; reconhecimento de filho/outra declaração irrevogável impede escritura. A combinação de testamento com incapaz fica bloqueada para proposta enquanto não houver conciliação oficial específica comprovada e análise humana registrada; não basta cumprir uma lista formal. Nunca emitir negativa falsa de testamento (tensão 🔴 R35 21 × 12-B). Divergência ou demanda litigiosa: interromper proposta consensual e orientar encaminhamento, sem criar ação judicial. Bem no exterior não recebe escritura de inventário/partilha (R35 29).

Base federal não substitui lei, prazo, alíquota, rito, tabela ou prova da UF. R35 15 na redação 695/2026 dispensa prova prévia de ITCMD no inventário, não o tributo devido nem as condições próprias do incidente. Não declarar atualização exaustiva, cabimento inquestionável ou aprovação de serventia. Qualificação, lavratura, manifestação MP, decisão judicial, apuração fiscal e registro pertencem aos responsáveis externos.

## Saída e revisão obrigatória

Entregue quadro `requisito → prova → arquivo/trecho → responsável → situação`, fatos confirmados separados de hipóteses, fundamentos com selos ✅/🟡/🔴, documentos faltantes, minuta identificada como proposta quando permitida, próxima providência e impedimento. Use um estado: `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`. Lacuna impeditiva bloqueia minuta para apresentação; não basta um aviso junto de texto utilizável incompatível.

Ao final, chame nesta ordem `anti-alucinacao-familia-extrajudicial`, `validador-familia-extrajudicial` e `suprema-corte-familia-extrajudicial`, R1→R4 default-on: fatos/provas/consenso/ator; fundamentos/vigência/tensões; documentos/cálculos/UF/condições externas; postura/sigilo/encaminhamento. Corrija ou retire trechos reprovados antes da entrega. Se qualquer dependência estiver ausente ou não puder ser executada, registre a revisão pendente e não entregue proposta como revisada. Controles por instrução (guidance only), sem enforcement por hook. Suporte: luis@sbroggio.io.
