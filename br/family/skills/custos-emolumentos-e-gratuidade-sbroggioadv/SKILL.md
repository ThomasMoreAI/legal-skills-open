---
name: custos-emolumentos-e-gratuidade-sbroggioadv
title: Custos, emolumentos e gratuidade
description: Organiza orçamento condicionado e pedido de gratuidade nos atos familiares. Use quando houver dúvida sobre custas de escritura, tabela da UF, emolumentos, despesas documentais ou declaração de insuficiência.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/custos-emolumentos-e-gratuidade
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Custos, emolumentos e gratuidade

> Camada C6. Preparação e acompanhamento pelo advogado dos interessados.

## Entrada

Ato e serviço destinatário; UF e data; conteúdo econômico e documentos; tabela oficial com edição e rubrica; declaração verdadeira dos interessados; despesas comprovadas e contratação de honorários se fornecida. Sem tabela, orçamento fica incompleto, com valores não determinados.

## Âncoras a ler

- `context/lei-10169-emolumentos.md`: arts. 1º–4º, incluindo regras de faixas, vedações e publicação oficial.
- `context/res-cnj-35-compilada.md`: arts. 4º–7º.
- `context/cnn-familia-centrais-eletronico.md`: arts. 538, §6º e 547, §7º, exclusivamente no âmbito registral descrito.

## Procedimento

1. Separar emolumentos notariais, emolumentos registrais, tributos, certidões/documentos e honorários. Não transformar honorários em emolumentos nem promessa de gratuidade da escritura em dispensa tributária.
2. Conferir UF, tabela oficial e espécie do ato (EMOL 1º/2º/4º); registrar base documental, faixa e rubrica. A natureza econômica não autoriza percentual livre: EMOL 3º, II e R35 5 vedam fixação percentual sobre o negócio. Não inventar tabela nacional, taxas adicionais ou rubricas fora de tabela (3º, III). Não importar regras de garantias rurais para atos familiares.
3. Separar retificação por erro imputável ao serviço (EMOL 3º, IV) de nova alteração pretendida pelos interessados, sem presumir que toda retificação é gratuita.
4. R35 6 abrange as escrituras dos atos ali enumerados; R35 7 estabelece que basta simples declaração de impossibilidade de arcar com emolumentos, mesmo com advogado constituído. Preparar declaração somente com fato confirmado pelos interessados; não exigir prova adicional como requisito federal inventado e não garantir decisão concreta do serviço. Escritura meramente declaratória de reconhecimento de união estável não recebe extensão automática do rol.
5. CNN 538, §6º prevê, enquanto ausente legislação específica estadual/distrital, 50% da habilitação de casamento para termo declaratório e certificação eletrônica. CNN 547, §7º trata da alteração registral de regime pelo valor da habilitação, na mesma condição. Esses parâmetros não tarifam escritura pública. Verificar hipótese, legislação específica e tabela antes de qualquer estimativa; vias registrais permanecem orientação.
6. Apontar o que depende de fonte local e quem obterá orçamento oficial. Soma somente de rubricas comprovadas; havendo lacuna, informar subtotal conhecido e total não determinado.

## Saída

Tabela: serviço/ato, rubrica, tabela/edição/dispositivo, faixa/base, valor comprovado ou pendente, responsável e condição de gratuidade. Entregar declaração proposta para revisão humana quando solicitada e lastreada, orçamento condicionado e lacunas separadas.

## Limites

Não emitir recibo, declarar concessão ou pagamento sem prova, nem usar regra do RCPN para precificar escritura. 🔴 Tensão de cabimento é independente do custo: orçamento não torna apto ato bloqueado. Sem tabela/UF, não apresentar total final ou percentual fictício.

## Fontes, sigilo e revisão obrigatória

Leia os anexos indicados em `context/` e o trecho literal antes de aplicar qualquer fundamento. Ausência de arquivo, redação, versão ou prova impede selo favorável; registre a lacuna. Use exclusivamente o corpus aprovado, sem Jusbrasil, Escavador, norma estadual presumida ou artigo conhecido apenas de memória. Data de captura não prova vigência atual: declare atualização/suspensão não conferida. Preserve números, negadores, ressalvas e marcadores de revogação; normalize apenas espaços e quebras de linha na comparação.

Guarde documentos e resultados somente na pasta privada escolhida pelo advogado, separados por cliente e matéria, fora do source compartilhado. Não transmita dados nem pratique ato externo por iniciativa própria. Estas instruções são guidance only, executadas pelo agente; não equivalem a enforcement por hook ou a aprovação de autoridade.

Ao final, inclusive em saída bloqueada, execute nesta ordem:
1. `anti-alucinacao-familia-extrajudicial`: conferir cada fato/citação e a prova de eventos externos; retirar afirmações sem lastro.
2. `validador-familia-extrajudicial`: registrar selo por fundamento com diploma/dispositivo, arquivo e trecho, versão/captura, data do fato/ato, destinatário, alcance e pendência; 🟡/🔴 nunca são aprovação automática.
3. `suprema-corte-familia-extrajudicial`: R1 fatos, provas, consenso e ator → R2 fundamentos, vigência e tensões → R3 documentos, cálculos, UF e condições externas → R4 postura, sigilo, fronteiras e encaminhamento.
Se qualquer controle estiver ausente ou não executado, declarar revisão pendente e bloquear entrega como pronta. Não converter revisão interna em fé pública, homologação fiscal ou confirmação de cartório.
