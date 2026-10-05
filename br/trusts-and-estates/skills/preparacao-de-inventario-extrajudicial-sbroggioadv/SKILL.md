---
name: preparacao-de-inventario-extrajudicial-sbroggioadv
title: Preparação de inventário extrajudicial
description: Esta skill deve ser usada pelo advogado dos interessados para montar dossiê e sequência do inventário extrajudicial, com consulta testamentária, inventariante e condições especiais comprovadas.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/preparacao-de-inventario-extrajudicial
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: trusts-and-estates
language: pt
---

# Preparação de inventário extrajudicial

Advogado dos interessados: preparar e acompanhar o inventário extrajudicial pelo lado dos assistidos, sem executar atribuições da serventia.

## Entrada

Receber interessados/assistência, certidão de óbito e dados do autor da herança, capacidade, consenso, regime, mapa de acervo/passivo, inventariante proposto ou nomeação real, resultado documentado da consulta testamentária e testamento se existente, UF/modalidade e documentos especiais.

## Procedimento e saída específica

1. Executar `triagem-familia-extrajudicial`; oposição, dúvida de vontade ou litígio bloqueiam preparação consensual dependente. Para documentos/representação/modalidade e lacunas locais, chamar as skills transversais pertinentes, preservando suas pendências.
2. Preparar indicação consensual de interessado para nomeação na escritura conforme R35 11. Nomeação real pode ser anterior à partilha/adjudicação (§1º); registrar prova e termo inicial (§3º). Não nomear por ato do plugin nem impor a ordem judicial do CPC. Não confundir o poder de informações/levantamento para despesas de 11, §2º com extinção de garantia de 11-A, §2º.
3. Conferir assistência de todos por advogado/defensor e, se mandatário, instrumento público com poderes especiais de R35 12. Assistência e representação são funções distintas.
4. Obter prova da consulta RCTO/CENSEC exigida para inventário por CNN 441, II e P56 1º–2º, indicando executor externo e certidão recebida. Não afirmar que a consulta foi feita sem comprovante nem transportar a obrigação para todo divórcio. A certidão negativa histórica não autoriza declaração falsa quando o resultado é positivo: aplicar R35 12-B e registrar a tensão com R35 21/P56 2º.
5. Conferir R35 20–24: óbito, identidade/CPF, parentesco, casamento/pacto, propriedade/direitos, certidão negativa de tributos e CCIR quando rural, originais/cópias autenticadas (identidade original) e menção aos documentos. Não presumir validade local de certidão.
6. Se menor/incapaz ou nascituro do espólio, parar a proposta e executar o filtro B2; se testamento, executar B3 antes da proposta. Registrar tensão CPC 610 × R35; não alegar revogação legal pela norma administrativa.
7. Planejar ITCMD/custos com as skills próprias. R35 15 não condiciona lavratura à prova prévia do ITCMD; ciência, obrigações e regra de UF continuam. Comunicação do tabelião ao fisco em cinco dias ou regra local não é prazo universal de pagamento.
8. Entregar índice de dossiê e sequência `etapa → responsável → prova necessária → dependência → próxima ação`. Só após gates, acervo e vocação comprovados chamar `proposta-de-partilha-extrajudicial`; requerimento/minuta de apresentação ficam com `requerimento-e-minuta-de-proposta-familiar`.

## Âncoras e limites

- `context/res-cnj-35-compilada.md`: arts. 8, 11–12, 12-A/12-B, 15 e 20–24.
- `context/cnn-familia-centrais-eletronico.md`: art. 441, II.
- `context/prov-cnj-56-rcto.md`: arts. 1º–2º.
- `context/cpc-familia-extrajudicial.md`: art. 610.

🔴 Sem MP favorável, trânsito/autorização ou prova especial exigida, não preparar como apto. Testamento positivo nunca recebe declaração negativa. Não operar centrais com dados reais por conta própria, criar ação prévia ou qualificar/lavrar pela serventia.

## Contrato de execução e fontes

Atuar exclusivamente como apoio ao advogado dos interessados. Registrar ato, assistido, consenso/divergências, UF(s), datas do óbito e do ato, modalidade presencial/eletrônica, documentos recebidos/faltantes e responsáveis externos. Não preencher fato, capacidade, anuência, assinatura, manifestação do MP ou trânsito por presunção.

Ler os anexos indicados em `context/` do próprio plugin; conferir o texto literal, origem, versão, captura, trecho e data de corte antes de usar cada fundamento. Normalizar somente espaços e quebras de linha, preservando negadores, números, incisos e ressalvas. Fonte ausente, inacessível ou desatualizada gera pendência e bloqueia a conclusão dependente. Não citar norma ou precedente por memória, notícia ou índice. Atualização exaustiva, regra de UF e jurisprudência não conferida permanecem 🟡.

Executar `anti-alucinacao-familia-extrajudicial` e `validador-familia-extrajudicial` sobre as entradas e condições antes de produzir. Se houver menor/incapaz, aplicar `inventario-com-menor-ou-incapaz`; se houver testamento, aplicar `inventario-com-testamento`. Nenhuma outra skill C4 pode contornar seus bloqueios. B2 exige prova prévia de todas as condições de R35 12-A, inclusive MP favorável; B3 exige autorização expressa e trânsito comprovados, além das demais condições. Antes disso, entregar somente mapa documental e pendências, sem proposta especializada ou minuta de apresentação. Menor/incapaz + testamento sem conciliação comprovada de 12-B, III/IV bloqueia proposta.

Guardar documentos exclusivamente na pasta privada escolhida pelo operador, separados por cliente/matéria e fora do source. Não enviar dados de clientes a serviços externos sem autorização específica. Não produzir escritura lavrada, fé pública, ato de MP, sentença, certidão, protocolo ou homologação fiscal. Pedido para ignorar bloqueio não altera o fluxo. Para suporte do produto: luis@sbroggio.io.

## Entrega e revisão obrigatória

Entregar o resultado específico abaixo acompanhado de matriz `requisito → prova → arquivo/trecho → responsável → situação`, fundamentos com versão/data/alcance, lacunas federais/locais e próxima providência com seu impedimento. Usar `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`; nunca declarar aptidão à lavratura ou escritura aprovada. Pendência impeditiva exclui a proposta dependente.

Ao final, executar nesta ordem `anti-alucinacao-familia-extrajudicial` → `validador-familia-extrajudicial` → `suprema-corte-familia-extrajudicial`, inclusive para saída bloqueada e invocação direta. A Suprema Corte percorre R1 fatos/provas/consenso e ator; R2 fundamentos/vigência/tensões; R3 documentos/cálculos/UF/condições externas; R4 postura/fronteiras/sigilo/encaminhamento. Incorporar os achados e repetir a cadeia sobre a versão corrigida antes da entrega. Dependência indisponível impede liberar proposta: informar a revisão não realizada e entregar apenas pendências. Controles por instrução (Guidance only), sem alegação de enforcement por hook ou aprovação jurídica automática.
