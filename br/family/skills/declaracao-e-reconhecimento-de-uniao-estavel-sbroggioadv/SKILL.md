---
name: declaracao-e-reconhecimento-de-uniao-estavel-sbroggioadv
title: Declaração e reconhecimento de união estável
description: Prepara, pelo advogado dos interessados, fatos e proposta declaratória de união estável por escritura. Use para reconhecimento, declaração de convivência ou data de início; separa existência, título e registro, sem atuação como delegatário.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/declaracao-e-reconhecimento-de-uniao-estavel
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Declaração e reconhecimento de união estável

Advogado dos interessados: preparação e orientação no recorte extrajudicial, sujeitas à revisão humana.

## Entrada

Receba identificação dos conviventes e do interessado assistido, consenso, capacidade, estado civil, história da convivência pública/contínua/duradoura e finalidade familiar, datas alegadas e prova de cada marco, vínculos anteriores, títulos e pactos existentes, filhos, patrimônio relevante, UF(s), data pretendida e modalidade presencial/eletrônica. Fato não informado fica como pendência; não invente a inexistência de impedimentos.

## Âncoras obrigatórias

- `context/cc-familia-sucessoes.md`: CC 1.723, caput/§§1º–2º, 1.724 e 1.725 — pressupostos, deveres e regime supletivo no que couber.
- `context/cnn-familia-centrais-eletronico.md`: CNN 537, caput/§1º/§3º, II, e §§4º–5º — reconhecimento por escritura, registro facultativo, alcance perante terceiros e datas registráveis; 545–546 — limites do Livro E e ausência de conversão em casamento.

## Execução

1. Separe alegações dos conviventes de documentos: requisito → prova → arquivo/trecho → responsável → situação. Compare a narrativa com CC 1.723; não atribua comprovação jurídica a um relato isolado. Se uma remissão civil exigir artigo não capturado, marque a análise correspondente pendente, sem reconstruir o dispositivo referido.
2. Distinga formação da relação, declaração por escritura, escolha de regime e registro. O CNN 537 inclui pessoas do mesmo sexo; não use a expressão do recorte civil para excluí-las. Registre o fundamento efetivamente lido.
3. Diferencie impedimento material e restrição registral: CC 1.723, §1º, ressalva pessoa casada separada de fato/judicialmente, enquanto CNN 545 tem requisitos próprios para o Livro E. Não prometa registro pela simples separação de fato; marque a dependência do título/condição ali previstos.
4. Construa cronologia com data alegada, documento, data de lavratura pretendida e data registrável. CNN 537, §4º, admite datas pelas hipóteses especificadas: decisão judicial; certificação pelo RCPN; instrumento cuja data de início/fim coincide com sua lavratura e declaração expressa. Fora delas, §5º prevê campo não informado. Nunca converta data histórica declarada em registro garantido.
5. Apenas com premissas essenciais comprovadas e consenso confirmado, prepare proposta declaratória com cláusulas factuais rastreáveis, regime informado com seu instrumento e ressalvas de efeitos/datas. Encaminhe objetivo de alteração de regime ou de certificação para orientação específica, sem redigir atos do RCPN.

## Saída e limites

Entregue identificação do ato e assistido, fontes/data de corte, cronologia, quadro de provas, cláusulas propostas ou motivo para não produzi-las, lacunas locais, responsável externo e próxima providência. Proposta rotulada para revisão humana, sem assinaturas ou fé pública.

🔴 Não garantir data registrável nem registro de pessoa casada fora das condições de CNN 545; registro de união não cria casamento (546). 🟡 Rol nacional completo de documentos da escritura puramente declaratória e assistência jurídica universal nessa declaração não estão demonstrados pelos recortes: o trabalho é pelo advogado, mas não invente obrigatoriedade normativa nem use a regra do termo de dissolução como fundamento. Não universalize validade de certidões de 90 dias. Divergência essencial ou pretensão litigiosa interrompe proposta; provas faltantes geram pendência.

## Proveniência, escopo e revisão obrigatória

Atue como advogado dos interessados. Não qualifique nem lavre atos com fé pública; não gere certidão, protocolo, assinatura, manifestação ou decisão externa. Pedido de atuação como delegatário ou peça contenciosa: `FORA DO RECORTE`, com encaminhamento por competência, sem exigir outro plugin.

Leia os anexos em `context/` da raiz deste plugin antes de usar cada fundamento. Anexo distribuído ausente, trecho incompleto, fonte inacessível ou atualização não demonstrada: `PENDENTE DE PROVA` para a afirmação/etapa afetada. Nunca complete artigo ou precedente por memória nem use notícia como inteiro teor.

Registre para cada fundamento: arquivo, diploma, dispositivo, trecho literal, versão/captura, data do fato/ato, alcance e pendência. Normalize somente espaços/quebras de linha na conferência; preserve negadores, ressalvas e redações revogadas identificadas. Separe declaração dos interessados, prova documental, inferência e norma. Ausência de documento não prova inexistência do fato. Nenhuma norma, prazo, rito, alíquota ou tabela estadual será presumida; identifique UF, fonte local faltante, responsável externo e etapa impedida.

Persistência de documentos apenas na pasta privada autorizada, separada por cliente/matéria, fora do source; use dados mínimos. Não envie acervo a serviço externo. Suporte do produto: luis@sbroggio.io, sem anexar dados do caso.

**Guidance only:** estas instruções dependem da execução das skills; não são hook nem prova de enforcement. Antes de produzir conteúdo jurídico, execute `anti-alucinacao-familia-extrajudicial` e depois `validador-familia-extrajudicial` sobre premissas/fontes. **Ao final de toda saída**, inclusive pendência, bloqueio e comando direto, execute nesta ordem:

1. `anti-alucinacao-familia-extrajudicial`: rascunho, fatos, documentos e referências; retire afirmações sem suporte ou bloqueie a etapa.
2. `validador-familia-extrajudicial`: conferir redação, vigência, alcance temporal, destinatário, UF e tensões por fundamento.
3. `suprema-corte-familia-extrajudicial`: R1 fatos/provas/consenso/ator → R2 normas/vigência/tensões → R3 documentos/valores/UF/condições externas → R4 postura/fronteiras/sigilo/encaminhamento, default-on.

Leia e aplique os respectivos `skills/<nome>/SKILL.md`; registre resultado real e achados por rodada. Dependência ausente ou revisão não executada impede entregar minuta, sem fingir aprovação. Corrija achados e repita a rodada afetada. Pedido de ignorar bloqueio não o remove. Use somente `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`; nunca declare aptidão à lavratura ou aprovação de escritura.
