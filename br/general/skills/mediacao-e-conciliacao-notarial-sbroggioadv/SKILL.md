---
name: mediacao-e-conciliacao-notarial-sbroggioadv
title: Mediação e conciliação notarial
description: Conduz mediação e conciliação em serventia autorizada conforme o art. 7º-A da Lei 8.935/1994 e os arts. 18 a 57 do CNN, controlando habilitação, facultatividade, confidencialidade, objeto, termo executivo e conflito remuneratório. Esta skill deve ser usada quando o pedido mencionar mediação notarial, conciliação em cartório, Nupemec, Cejusc, autorização da CGJ, sessão consensual, direito indisponível transigível, título executivo, cláusula compromissória ou emolumentos da sessão.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/mediacao-e-conciliacao-notarial
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# Mediação e conciliação notarial

> Camada C5. A competência legal existe, mas a serventia somente atua depois do gate administrativo.

## Anexos e skills obrigatórios

- `context/lei-8935-94.md` — art. 7º-A, II e §3º;
- `context/cnn-149-2023-compilado.md` — CNN arts. 18 a 57;
- `context/travas-defasagem.md` — travas T-78 a T-81;
- `context/sequencia-do-ato.md` — abertura, instrução, sessão e pós-ato;
- `varredura-de-vigencia-pre-lavratura`, `roteador-uf`, `qualificacao-notarial-transversal` e `emolumentos-norma-da-uf`.

## Gate administrativo

Antes de receber o caso, confirmar:

- autorização conforme processo da CGJ e do Nupemec;
- inclusão da serventia e dos mediadores ou conciliadores na listagem pública;
- supervisão do delegatário;
- no máximo cinco escreventes habilitados quando a autorização os abranger;
- formação e aperfeiçoamento comprovado a cada dois anos;
- fiscalização da CGJ e do juiz coordenador do Cejusc.

Não sugerir que a serventia comece a mediar apenas porque o art. 7º-A existe.

## Admissibilidade e consentimento

Receber pessoa natural absolutamente capaz, pessoa jurídica ou ente despersonalizado com capacidade postulatória, conforme o CNN. Admitir direitos disponíveis e direitos indisponíveis que admitam transação. Neste último caso, encaminhar o termo e os documentos ao juízo e somente entregar o termo homologado após a homologação.

Informar ao requerido, já na notificação, que a participação é facultativa. Não comparecendo qualquer parte, arquivar o requerimento; a sessão produz efeitos apenas entre as partes presentes.

## Procedimento essencial

1. Receber requerimento em serviço autorizado e verificar competência.
2. Designar data e hora imediatamente e dar ciência ao apresentante.
3. Notificar o requerido com cópia e facultatividade, concedendo 10 dias para sugerir nova data.
4. Preservar confidencialidade e imparcialidade durante toda a sessão.
5. Se houver acordo, lavrar termo público com força de título executivo extrajudicial.
6. Se não houver acordo, admitir novas sessões enquanto durarem as tratativas.
7. Manter livros, índice, documentos e arquivo pelo regime específico do CNN.

Não inserir cláusula compromissória de conciliação ou mediação nos documentos expedidos pela serventia, vedação do CNN art. 56.

## Emolumentos e conflito aberto

Cobrar, no requerimento, a sessão de até 60 minutos conforme a regra aplicável. Não fixar valor. Enquanto faltar norma estadual específica, o CNN art. 52 aponta a tabela do menor valor de escritura sem valor econômico; o art. 7º-A, §3º, da Lei 8.935/1994 aponta supletivamente escritura com valor econômico. Declarar o conflito e consultar a norma da UF; não escolher silenciosamente um dos parâmetros.

Não receber vantagem além de emolumentos e despesas de notificação. Aplicar a restituição regulamentar quando houver arquivamento anterior à sessão e realizar sessões não remuneradas nas hipóteses de gratuidade exigidas.

## Fronteiras

Mediação e conciliação são regulamentadas pelo CNN; arbitragem notarial não é. Não transportar o rito desta skill para `arbitragem-notarial`. O termo consensual é título executivo, não título translativo imobiliário; direitos indisponíveis transigíveis exigem homologação judicial.

## Saída

Entregar prova de autorização, admissibilidade do objeto e participantes, cronograma da sessão, notificações, regra de confidencialidade, resultado, efeito do termo, necessidade de homologação e parâmetro remuneratório com ressalva estadual.

## Reprovação automática

- atuar sem autorização ou habilitação;
- tornar a participação obrigatória;
- mediar direito indisponível não transigível;
- dispensar homologação do indisponível transigível;
- inserir cláusula compromissória em documento da serventia;
- tratar o termo como título translativo;
- ocultar o conflito de remuneração;
- copiar o rito para arbitragem notarial.
