---
name: itcmd-como-efeito-do-ato-sbroggioadv
title: ITCMD como efeito do ato
description: Qualifica fatos geradores, contribuintes e pendências fiscais de inventário, divórcio ou união estável. Use quando o pedido mencionar ITCMD, excesso de meação ou quinhão, declaração fiscal ou recolhimento vinculado à escritura.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/itcmd-como-efeito-do-ato
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: tax
language: pt
---

# ITCMD como efeito do ato

> Camada C6. Preparação e acompanhamento pelo advogado dos interessados.

## Entrada

Ato e data pretendida; óbito e data comprovada; negócio gratuito/oneroso e respectivas provas; interessados, domicílios e UF(s); localização e natureza dos bens; frações civis justificadas, valores e documentos; normas e formulários oficiais locais disponíveis; guias e recibos reais. Não presumir uma única UF para todo o acervo.

## Âncoras a ler

- `context/lc-227-2026-itcmd.md`: arts. 146–164 e 182, III, com rodapé de publicação.
- `context/res-cnj-35-compilada.md`: arts. 15, 38 e 46-A; `context/res-cnj-695-2026.md`: redação alteradora do art. 15.
- `context/cf-itcmd.md` e `context/ctn-itbi-contraste.md`: somente no alcance literal capturado, para distinguir competência e tributo; CTN 35–42 não fornecem regra geral de ITCMD atual.

- `context/lei-15040-seguro.md`: art. 116 para qualificação civil do capital segurado por morte; vigência e demais saldos/reservas seguem `acervo-dividas-e-valores-do-inventario`.

## Procedimento

1. Qualificar transmissão e fração civil antes de falar em imposto: LC227 147/148. Distinguir meação, herança, excesso gratuito e negócio oneroso. Não chamar toda diferença de ITCMD; qualificação de eventual outro tributo fica pendente de base específica, sem cálculo por analogia.
2. Separar fatos geradores: transmissão causa mortis na data do óbito (151, I, a), independente da instauração do inventário (148, §3º); excesso extrajudicial na lavratura da escritura de partilha/adjudicação (151, II, f). Não situar toda incidência na escritura.
3. Identificar sucessor/donatário (157) e ente competente por bem/domicílio, preservando condições dos arts. 158–159. Caso internacional exige bases adicionais e fica fora de planejamento autônomo. Conferir temporalidade: efeitos do Livro II desde a publicação de 14/01/2026 (182, III), não desde a sanção de 13/01; não aplicar retroativamente a óbito anterior por automatismo.
4. Examinar imunidade e não incidência (149–150) sem confundir isenção local. Renúncia em benefício do monte exige todas as condições de 150, I; renúncia dirigida tem hipótese distinta em 151, II, d. ITCMD não incide sobre benefício de previdência complementar, seguro, pecúlio e similares (LC227 150, III). Inclusão ou exclusão no acervo é qualificação civil separada: capital segurado por morte, SEG 116; demais saldos/reservas 🟡 e tratados por `acervo-dividas-e-valores-do-inventario`.
5. Organizar valor de mercado, dívidas comprovadas e premissas (152–155); progressividade e data da alíquota (156). Sem norma local e base documental, entregar matriz de pendências, sem valor final, vencimento, multa ou isenção. Homologação cabe à administração tributária (160).
6. Inventário: R35 15 dispensa comprovação de pagamento prévio para lavratura, sem extinguir obrigação principal/acessória; as partes devem ser orientadas, e a declaração pertence ao ato do tabelião. Se não pago previamente, comunicação do tabelião ao fisco em cinco dias ou conforme legislação tributária (15, §2º): não é prazo de pagamento do contribuinte.
7. Divórcio: preservar R35 38, comprovação do tributo devido sobre fração transferida; art. 15 não afasta essa regra. União estável: examinar 46-A no que couber, sem extensão automática de dispensa.
8. Separar obrigações das partes, advogado, fisco e serviços. LC227 161–163 não autorizam o plugin a acessar base fiscal; art. 163, II destina obrigação aos titulares dos serviços.

## Saída

Quadro por transmissão: fato/prova/data, bem/fração, natureza, contribuinte, UF/critério, fundamento/alcance, documentos, obrigações e responsável, base/valor comprovado, lacuna local e etapa impedida. Anexar roteiro condicionado de declaração/recolhimento e evidência de pagamento quando existente.

## Limites

Sem legislação estadual/distrital conferida, nenhuma conclusão final de cálculo ou prazo. Não emitir guia, simular pagamento, homologar cálculo ou criar planejamento tributário. 🔴 Tensões de cabimento com incapazes/testamento e de dissolução com nascituro não são resolvidas por enquadramento fiscal; preservar bloqueios da triagem.

## Fontes, sigilo e revisão obrigatória

Leia os anexos indicados em `context/` e o trecho literal antes de aplicar qualquer fundamento. Ausência de arquivo, redação, versão ou prova impede selo favorável; registre a lacuna. Use exclusivamente o corpus aprovado, sem Jusbrasil, Escavador, norma estadual presumida ou artigo conhecido apenas de memória. Data de captura não prova vigência atual: declare atualização/suspensão não conferida. Preserve números, negadores, ressalvas e marcadores de revogação; normalize apenas espaços e quebras de linha na comparação.

Guarde documentos e resultados somente na pasta privada escolhida pelo advogado, separados por cliente e matéria, fora do source compartilhado. Não transmita dados nem pratique ato externo por iniciativa própria. Estas instruções são guidance only, executadas pelo agente; não equivalem a enforcement por hook ou a aprovação de autoridade.

Ao final, inclusive em saída bloqueada, execute nesta ordem:
1. `anti-alucinacao-familia-extrajudicial`: conferir cada fato/citação e a prova de eventos externos; retirar afirmações sem lastro.
2. `validador-familia-extrajudicial`: registrar selo por fundamento com diploma/dispositivo, arquivo e trecho, versão/captura, data do fato/ato, destinatário, alcance e pendência; 🟡/🔴 nunca são aprovação automática.
3. `suprema-corte-familia-extrajudicial`: R1 fatos, provas, consenso e ator → R2 fundamentos, vigência e tensões → R3 documentos, cálculos, UF e condições externas → R4 postura, sigilo, fronteiras e encaminhamento.
Se qualquer controle estiver ausente ou não executado, declarar revisão pendente e bloquear entrega como pronta. Não converter revisão interna em fé pública, homologação fiscal ou confirmação de cartório.
