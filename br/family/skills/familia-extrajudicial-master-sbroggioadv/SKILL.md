---
name: familia-extrajudicial-master-sbroggioadv
title: Master — advogado dos interessados
description: Esta skill deve ser usada pelo advogado dos interessados quando pedir condução de divórcio, união estável ou inventário extrajudicial, jornada até o pós-ato, escolher o fluxo ou /familia-extrajudicial-master. Coordena as 32 skills e exige provas, guard, validador e revisão R1→R4; não qualifica nem lavra escrituras.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/familia-extrajudicial-master
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Master — advogado dos interessados

## Entrada e cadeia obrigatória

Identificar ato/operação, interessado assistido, consenso/dissenso, capacidade, filhos/nascituro, testamento, bens, UFs, datas dos fatos/ato e modalidade. Solicitar somente informação ausente e necessária; não repetir dado documentado. Sem perfil, oferecer `familia-extrajudicial-install`, sem confundir instalação com análise de caso.

Executar nesta ordem: `triagem-familia-extrajudicial` → `anti-alucinacao-familia-extrajudicial` → `validador-familia-extrajudicial` → matriz de provas/dependências → especializadas permitidas → guard e validador sobre o resultado → `suprema-corte-familia-extrajudicial` **R1→R4** → entrega. Ler o SKILL.md de cada destino antes de executar. A instalação é administrativa; toda saída jurídica, inclusive quadro de pendências e comando direto, passa pelos três controles finais. Ausência de skill/fonte impede a etapa dependente: não simular sua execução. Os controles são **Guidance only**, instruções ao agente, sem garantia mecânica por hook.

## Roteamento do rol completo — 32 nomes

| Quando | Skill a carregar |
|---|---|
| Primeiro uso/configuração | `familia-extrajudicial-install` |
| Coordenar jornada | `familia-extrajudicial-master` (esta skill; não recursar) |
| Classificar ato e provas | `triagem-familia-extrajudicial` |
| Rastrear afirmações/fatos | `anti-alucinacao-familia-extrajudicial` |
| Conferir norma/alcance | `validador-familia-extrajudicial` |
| Revisar saída final | `suprema-corte-familia-extrajudicial` |
| Organizar documentos | `dossie-documental-familiar` |
| Assistência, mandato e assinaturas | `assistencia-e-representacao-familiar` |
| Participação eletrônica | `preparacao-de-ato-eletronico` |
| Fonte/rito estadual pendente | `lacunas-estaduais-do-procedimento` |
| Preparar divórcio consensual | `preparacao-de-divorcio-extrajudicial` |
| Filhos/decisão prévia no divórcio | `filhos-e-condicoes-do-divorcio` |
| Meação/transferência no divórcio | `acordo-patrimonial-do-divorcio` |
| Declaração/reconhecimento da união | `declaracao-e-reconhecimento-de-uniao-estavel` |
| Convenção e cronologia patrimonial | `convencao-patrimonial-de-uniao-estavel` |
| Dissolução consensual da união | `dissolucao-consensual-de-uniao-estavel` |
| Registro/averbação e alternativas RCPN | `orientacao-das-vias-registrais-de-uniao-estavel` |
| Interessados, meação e vocação | `interessados-meacao-e-heranca` |
| Acervo/passivo e valores | `acervo-dividas-e-valores-do-inventario` |
| Sequência do inventário | `preparacao-de-inventario-extrajudicial` |
| Quinhões e proposta consensual | `proposta-de-partilha-extrajudicial` |
| Interessado menor/incapaz | `inventario-com-menor-ou-incapaz` |
| Testamento no inventário | `inventario-com-testamento` |
| Sobrepartilha, negativo ou herdeiro único | `sobrepartilha-negativo-e-adjudicacao` |
| Renúncia | `renuncia-hereditaria-na-via-extrajudicial` |
| Cessão | `cessao-hereditaria-na-via-extrajudicial` |
| Alienação para despesas do espólio | `alienacao-do-espolio-para-despesas` |
| ITCMD vinculado ao ato | `itcmd-como-efeito-do-ato` |
| Custos/gratuidade | `custos-emolumentos-e-gratuidade` |
| Consolidar apresentação | `requerimento-e-minuta-de-proposta-familiar` |
| Responder a nota real | `cumprimento-de-exigencias-do-ato` |
| Após escritura real | `orientacao-pos-escritura-familiar` |

O rol define destinos, não prova instalação. Verificar `skills/<nome>/SKILL.md`; destino ainda ausente gera dependência explícita. Não produzir seu conteúdo por improviso. Não acionar outra especialidade só porque está no rol; selecionar pela operação e provas.

## Filtros que antecedem produtoras

- Menor/incapaz: sem representação comprovada, parte ideal em **cada bem**, MP favorável e demais condições de R35 12-A, somente coleta/matriz; nenhuma proposta especializada. Proibir disposição de bens/direitos do incapaz. Nascituro do espólio depende da prova específica do §2º. Preservar tensão CPC 610/CC 2.016 × R35 e análise humana registrada, mesmo com documentos.
- Testamento: exigir autorização judicial **expressa e transitada**, certidão/conteúdo e todas as condições de R35 12-B; autorização isolada não basta. Reconhecimento de filho/outra declaração irrevogável bloqueia. Testamento+incapaz sem conciliação comprovada de III×IV e análise humana bloqueia proposta. Nunca fabricar declaração negativa sob R35 21.
- Dissolução com nascituro: **BLOQUEADO** no produto; CNN 537, §6º não elimina CPC 733 × R35 34/46-A. Filhos incapazes no divórcio exigem decisão prévia sobre guarda, visitação e alimentos e análise jurídica humana registrada; não inventar exigência geral de trânsito no art. 34, §2º.
- Litígio/oposição ou pedido de lavratura/ato de MP/juiz/SEFAZ: fora da entrega do advogado; orientar encaminhamento sem construir peça judicial. Bem situado no exterior não é incluído por esta via (R35 29); separar esse bem, sem declarar automaticamente proibido todo acervo misto.
- UF/fonte local ausente: permitir somente mapa federal identificado; suspender cálculo final, prazo e apresentação dependentes da regra local. R35 15 dispensa comprovação prévia universal no inventário, não tributo devido nem requisito próprio do art. 38 no divórcio.

## Fontes e fechamento

Usar exclusivamente os textos literais distribuídos em `context/`, especialmente `cpc-familia-extrajudicial.md` (610/733), `cc-familia-sucessoes.md` (2.016), `res-cnj-35-compilada.md` (8/11/12/12-A/12-B/15/29/34/38/46-A), `cnn-familia-centrais-eletronico.md` (537). Conferir manifesto/versão/trecho no validador; arquivo ausente ou atualização não comprovada gera pendência, nunca artigo de memória. Não consultar Jusbrasil/Escavador nem importar direito do modelo de estrutura.

Entregar ato, assistido, UFs/datas/modalidade, fontes/data de corte, documentos recebidos/faltantes, matriz **requisito → prova → arquivo/trecho → responsável → situação**, próximos passos e impedimentos; registrar guard, validador e resultado individual de R1, R2, R3 e R4. Manter dados na matéria privada. Fechar com `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`. Mesmo entrega completa não significa “apto à lavratura” ou aprovação de escritura. Sem rascunho, revisar a própria pendência; não simular revisão de minuta inexistente.
