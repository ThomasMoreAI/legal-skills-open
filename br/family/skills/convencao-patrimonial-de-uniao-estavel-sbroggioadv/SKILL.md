---
name: convencao-patrimonial-de-uniao-estavel-sbroggioadv
title: Convenção patrimonial de união estável
description: Prepara, pelo advogado dos interessados, proposta convencional e cronologia patrimonial da união estável. Use para pacto, regime atual ou desejado e bens; alteração registral recebe somente orientação, com proteção de terceiros e efeitos temporais.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/convencao-patrimonial-de-uniao-estavel
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Convenção patrimonial de união estável

Advogado dos interessados: preparação e orientação no recorte extrajudicial, sujeitas à revisão humana.

## Entrada

Receba conviventes, interessado assistido, consenso e capacidade, datas da convivência/pactos/registros, instrumentos completos, regime atual e pretendido, títulos e origem/data de aquisição de cada bem, dívidas/credores/terceiros, eventual partilha, interdições, UF(s), modalidade e data prevista. Regime alegado sem pacto/registro não vira fato provado.

## Âncoras obrigatórias

- `context/cc-familia-sucessoes.md`: CC 1.725; 1.658–1.659 — regime supletivo no que couber e exclusões da comunhão parcial; 108 — reserva de escritura pública quando incidente.
- `context/cnn-familia-centrais-eletronico.md`: CNN 547, caput/§§1º–6º/8º, e 548 — alteração registral, proteção de terceiros, interdição, assistência, efeitos e documentos. Esses dispositivos não instituem retroatividade geral de contrato privado.

## Execução

1. Monte requisito → prova → arquivo/trecho → responsável → situação e uma cronologia separando início da união, aquisição de bens, contrato, registro e averbação. Não assuma que convenção nova altera todo patrimônio anterior.
2. Aplique CC 1.725 no alcance literal: salvo contrato escrito, comunhão parcial no que couber. Confira contrato e origem dos bens; CC 1.659 preserva bens anteriores, doação/herança e sub-rogação, entre outras exclusões. Toda qualificação concreta é inferência identificada para revisão; ausência de meação não decide direito sucessório.
3. Distinga proposta convencional por escritura de procedimento de alteração de regime no RCPN. Para este, entregue apenas orientação: requerimento conjunto e forma de apresentação do art. 547; documentos específicos do 548. Não produza requerimento registral autônomo, averbação ou certidão.
4. Declare que alteração registral protege terceiros de boa-fé, inclusive credores anteriores (547, §1º). Certidão de interdições positiva leva a alteração ao processo judicial (§2º); não redija a ação. Partilha e/ou certidões positivas enumeradas no §3º exigem assistência ali prevista; não transforme assistência condicional em dispensa geral da análise jurídica.
5. Confira 547, §4º, integralmente: efeitos desde a averbação e ausência de retroação aos bens anteriores em virtude da alteração; preserve a ressalva da comunhão universal sobre bens existentes, com direitos de terceiros. Não transponha automaticamente essa regra registral para eficácia retroativa de qualquer convenção por escritura.
6. Prepare proposta convencional somente com premissas essenciais e consenso comprovados, separando regime desejado, bens por origem, efeitos pretendidos, ressalvas, direitos de terceiros e dependências de forma/registro. Se o objetivo exigir retroatividade ou tese jurisprudencial não conferida, não produza cláusula que realize essa pretensão; entregue pendência e encaminhamento humano.

## Saída e limites

Entregue cronologia, inventário documental dos bens/pactos, quadro de condições, proposta permitida para revisão humana e mapa de riscos/atos posteriores por responsável. Sem UF/norma local, não calcule tributos, custos ou prazos.

🔴 Não prometer retroatividade, apagamento de direitos de terceiros ou efeitos de alteração registral antes da averbação. 🟡 STF Tema 1236 e REsp 1.845.416/MS: nenhum inteiro teor/alcance validado foi fornecido nesta lane; não atribua tese, modulação, repetitividade ou solução automática. Fonte jurisprudencial ausente bloqueia a afirmação dependente. Litígio patrimonial, incapacidade sem solução documental ou conflito de assistência impedem proposta correspondente; não faça planejamento sucessório ou tributário autônomo.

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
