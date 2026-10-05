---
name: negativacao-indevida-e-cadastro-sbroggioadv
title: Negativação indevida e cadastro de inadimplentes
description: 'Trata negativação indevida em cadastro de proteção ao crédito (arts. 43 e 44, CDC) — dever de notificação prévia (Súmula 359/STJ), dispensa de aviso de recebimento (Súmula 404/STJ, Tema 59), efeito da inscrição preexistente legítima sobre o dano moral (Súmula 385/STJ, Tema 922), prazo de 5 anos e baixa após pagamento. Declara a pendência do Tema 1.404/STJ sobre comercialização de dados por bureaus de crédito. Aciona: quando o usuário relata nome negativado sem aviso, negativação mantida após quitação, ou questiona o efeito de uma inscrição anterior sobre o pedido de dano moral.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/negativacao-indevida-e-cadastro
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Negativação indevida e cadastro de inadimplentes

## Quando esta skill entra

Nome do consumidor inscrito em SPC/Serasa (ou cadastro equivalente) sem aviso prévio,
com dívida já paga, com dado incorreto, ou o consumidor precisa entender se uma
inscrição anterior sua, ainda ativa, afasta o pedido de indenização pela nova.

## Base normativa

- **Art. 43, CDC** — direito de acesso aos dados; § 1º exige objetividade, clareza,
  veracidade e prazo máximo de **5 anos** de informação negativa; § 2º exige comunicação
  por escrito da abertura de cadastro não solicitado pelo consumidor; § 3º dá **5 dias
  úteis** para correção de inexatidão após reclamação do consumidor; § 5º veda ao SPC
  fornecer, após a **prescrição** da dívida, informação que impeça novo acesso a
  crédito.
- **Art. 44, CDC** — órgãos públicos de defesa do consumidor mantêm cadastro de
  reclamações fundamentadas, aplicando-se a ele, no que couber, as mesmas regras do
  art. 43 e do parágrafo único do art. 22.

## O teste

1. Identificar **quem tinha o dever de notificar previamente** — é do órgão
   **mantenedor** do cadastro (Súmula 359/STJ), não necessariamente do credor
   originário.
2. Checar a forma da notificação: **aviso de recebimento (AR) é dispensável**
   (Súmula 404/STJ, também firmada como Tema 59) — basta prova do envio da
   correspondência ao endereço correto do consumidor. Notificação **exclusivamente por
   e-mail não supre** a exigência (entendimento do STJ de 2023, invocando a própria
   Súmula 359 para exigir correspondência a endereço físico).
3. Verificar se, no momento da inscrição questionada, já havia **outra inscrição
   preexistente e legítima** em nome do consumidor. Se sim, a **Súmula 385/STJ (=
   Tema 922)** afasta o dano moral pela nova inscrição — mas **não afasta o direito ao
   cancelamento** da inscrição irregular. Vale mesmo que a inscrição preexistente esteja
   sendo discutida em outra ação (o STJ já decidiu que questionar judicialmente a
   primeira inscrição não garante, por si só, o dano moral pela segunda).
4. Checar o prazo de 5 anos (art. 43, § 1º) e a obrigação de baixa após o pagamento
   integral, por analogia ao dever de correção do § 3º.
5. Se a matéria envolver venda/compartilhamento de dados cadastrais por bureaus a
   terceiros, **declarar a pendência** — ver Armadilhas.

## Tese do consumidor

Ausência de notificação prévia por escrito a endereço físico gera dano moral **in re
ipsa** (não precisa provar o abalo). Notificação só por e-mail não é válida. Inscrição
preexistente sub judice, ainda ativa, não afasta a Súmula 385 para efeito do dano moral
da nova inscrição — mas o consumidor mantém o direito de exigir o cancelamento da
inscrição irregular.

## Tese do fornecedor

A notificação foi enviada e comprovada ao endereço correto, dispensado o AR
(Súmula 404/STJ) — a Súmula 404 já é a flexibilização máxima admitida a favor do
credor, não comporta nova flexibilização (ex.: notificação só por e-mail). Havia
inscrição preexistente e legítima no momento da nova inscrição, o que afasta o dano
moral pela Súmula 385/STJ, restando no máximo o cancelamento.

## Armadilhas

Não existe base para exigir prova de recebimento (AR) da notificação — a Súmula 404 é
literal ao dispensá-lo; exigir AR além do que a súmula pede é pedir mais do que a lei
garante. A Súmula 385 protege o fornecedor **apenas quanto ao dano moral** — nunca
aplicá-la para negar também o cancelamento da inscrição irregular, que é direito
autônomo expressamente ressalvado no próprio enunciado. **Tema 1.404/STJ (comercialização
de dados pessoais não sensíveis por bureaus de crédito) está PENDENTE de julgamento**
(afetado em janeiro de 2026) — qualquer peça sobre venda/compartilhamento de dados
cadastrais deve declarar a divergência atual nos tribunais de origem, nunca afirmar
posição do STJ como pacífica. Se a cobrança de fundo da negativação também for indevida,
articular com `pratica-e-clausula-abusiva` e `cobranca-indevida-repeticao-dobro`.

## Fronteira

Negativação decorrente de dívida bancária (cartão, empréstimo, financiamento):
`bancario-adv-os`. LGPD/tratamento de dados fora do escopo estrito do CDC: fora deste
plugin. Execução após reconhecimento judicial do dano: `execucao-adv-os`.
