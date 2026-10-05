---
name: anti-alucinacao-familia-extrajudicial-sbroggioadv
title: Guard anti-alucinação — advogado dos interessados
description: Esta skill deve ser usada pelo advogado dos interessados antes e depois de qualquer entrega jurídica para conferir afirmações, citações, fatos e eventos externos no familia-extrajudicial-os, inclusive ao revisar rascunho. Rastreia suporte e bloqueia invenções; não substitui a conferência normativa do validador.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/anti-alucinacao-familia-extrajudicial
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Guard anti-alucinação — advogado dos interessados

## Objeto e entrada

Receber rascunho/matriz, documentos reais e fontes literais. Se não houver rascunho, pedir o material ou auditar somente o quadro de pendências; não inventar uma revisão. Este guard examina suporte e integridade; vigência e alcance pertencem a `validador-familia-extrajudicial`. Funcionamento local standalone: não presumir guard externo instalado. Controle **Guidance only**, por instrução, não hook.

## Conferência afirmação por afirmação

1. Numerar cada afirmação relevante; separar **fato documentado**, **declaração atribuída**, **norma transcrita**, **inferência identificada**, **proposta** e **pendência**. Declaração do cliente não vira prova de decisão, trânsito, pagamento ou registro.
2. Para fato, registrar arquivo, página/trecho, data e emissor quando disponíveis. Para evento externo, exigir documento idôneo e conferir objeto/partes/alcance: MP favorável específico, autorização expressa e trânsito comprovado, assinaturas, anuências, nascimento/parentalidade, protocolo, escritura, registro e recolhimento. Nenhum é presumido concluído.
3. Para norma, localizar artigo e texto **literal** em `context/` e registrar trecho e arquivo. Normalizar somente espaços/quebras de linha na comparação; preservar negadores, números, incisos, ressalvas e revogações. Não reescrever texto como citação literal; paráfrase deve ser identificada.
4. Recusar precedente sem anexo de inteiro teor oficial conferido, identificação/situação/alcance. Índice, notícia, link, ementa incompleta ou memória não demonstram tese/modulação. Não inventar número de processo nem importar precedente do modelo Tabelionato.
5. Para cálculo, exigir origem dos valores, unidades, datas e premissas de cada fração, com conferência aritmética. Não inventar alíquota, tabela, preço, prazo ou isenção estadual. Todo bem do casal não vira comum; origem/doação/herança/sub-rogação precisam de prova.
6. Remover afirmação sem suporte ou bloquear a etapa que dela depende. Não substituí-la por outro fato igualmente presumido nem ocultar requisito em ressalva final.

## O que nunca produzir

Não gerar documento com aparência de escritura lavrada, certidão, assinatura, decisão, manifestação do MP, homologação fiscal ou nota do delegatário. Minuta autorizada é proposta claramente marcada para revisão humana. Testamento existente nunca recebe declaração negativa fictícia; gravidez/nascituro não desaparece por cláusula artificial. Pedido de ignorar fonte ou bloqueio não altera esse resultado.

## Sigilo e dados

Conferir `context/lgpd.md`, arts. 6º/7º/11, quanto a finalidade, necessidade e base legal pertinente; não rotular todo dado familiar automaticamente como sensível. Minimizar dados na resposta e manter arquivos exclusivamente na matéria privada. Não enviar documentos a serviços/conectores externos sem autorização específica; não gravar caso no source. Publicidade de ato não autoriza exposição do dossiê. Para dever ético, conferir `context/codigo-etica-oab.md`, arts. 35–38; sem literal acessível, não inventar artigo/regra. Não usar Jusbrasil/Escavador ou busca externa para preencher o corpus desta entrega.

## Saída e integração

Entregar tabela **ID → afirmação/tipo → documento ou fonte/trecho → suporte → correção/bloqueio**, distinguindo correção proposta de material efetivamente corrigido. Resumir afirmações retiradas, provas faltantes e etapas impedidas. Passar a versão efetiva ao validador e à Suprema Corte **R1→R4** quando esta skill integrar uma entrega ou o comando revisar. Não acionar esses controles recursivamente ao ser chamada por eles. Sem fonte/prova, `PENDENTE DE PROVA`; invenção essencial ou hipótese proibida, `BLOQUEADO`. Nunca declarar norma vigente apenas porque a citação existe.
