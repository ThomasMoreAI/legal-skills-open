---
name: imovel-na-planta-e-distrato-sbroggioadv
title: Imóvel na planta e distrato
description: 'Trata a rescisão (distrato) de compra e venda de imóvel na planta submetida ao CDC: devolução das parcelas pagas em caso de culpa do incorporador × culpa do adquirente, percentual de retenção, atraso de obra e prazo de tolerância, e a discussão sobre comissão de corretagem e taxa SATI. Aplica a Súmula 543/STJ e o Tema 577/STJ (tese firmada em repetitivo) como base central, com a trava de que a Lei 13.786/2018 (Lei do Distrato) é posterior, tem regime próprio de retenção percentual e não retroage a contratos anteriores à sua vigência. Escreve os dois lados: tese do adquirente e tese da incorporadora. Fronteira: matéria registral e de posse do imóvel pertence ao `direito-imobiliario-adv-os` — esta skill só aponta, não duplica. Aciona quando o usuário trouxer distrato de imóvel na planta, rescisão de promessa de compra e venda, atraso de obra, retenção de parcelas pagas, corretagem/SATI, ou defesa de incorporadora nesses casos.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/imovel-na-planta-e-distrato
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Imóvel na planta e distrato

## Quando esta skill entra

Rescisão (distrato) de contrato de promessa de compra e venda de imóvel em
construção submetido ao CDC — seja por iniciativa do adquirente (desistência,
inadimplência) seja por descumprimento do incorporador (atraso de obra além da
tolerância, alteração de projeto, entrega de unidade diversa da contratada).

## Base normativa

- **Súmula 543/STJ:** "Na hipótese de resolução de contrato de promessa de compra
  e venda de imóvel submetido ao Código de Defesa do Consumidor, deve ocorrer a
  imediata restituição das parcelas pagas pelo promitente comprador —
  integralmente, em caso de culpa exclusiva do promitente vendedor/construtor, ou
  parcialmente, caso tenha sido o comprador quem deu causa ao desfazimento."
- **Tema 577/STJ (tese firmada em repetitivo, mesma matéria):** "Em contratos
  submetidos ao Código de Defesa do Consumidor, é abusiva a cláusula contratual
  que determina a restituição dos valores devidos somente ao término da obra ou
  de forma parcelada, na hipótese de resolução de contrato de promessa de compra e
  venda de imóvel, por culpa de qualquer dos contratantes."
- **CDC art. 51, I e IV** — nulidade de cláusula que exonere responsabilidade do
  fornecedor ou coloque o consumidor em desvantagem exagerada.
- **CDC art. 35** — se o incorporador recusar cumprimento à oferta, o adquirente
  pode exigir cumprimento forçado, aceitar equivalente ou rescindir com
  restituição e perdas e danos.

## O teste / passo a passo

1. **Quem deu causa ao desfazimento?** Culpa do incorporador (atraso além da
   tolerância, descumprimento de especificação) → devolução **integral e
   imediata**. Culpa do adquirente (desistência, inadimplência sem justa causa) →
   devolução **parcial**, mas sempre **imediata** — nunca condicionada ao término
   da obra ou parcelada (é isso que o Tema 577 declara abusivo).
2. **O contrato é anterior ou posterior à Lei 13.786/2018 (Lei do Distrato)?**
   Anterior → aplica-se a Súmula 543 e o Tema 577 puros, sem o regime percentual
   fixo da lei nova (irretroatividade já reconhecida em tribunal — ver
   Armadilhas). Posterior → soma-se o regime específico de retenção percentual
   trazido pela Lei 13.786/2018, que esta skill não detalha em número fixo —
   conferir o percentual e o prazo de carência da lei diretamente, e marcar
   `[VERIFICAR — não confirmado no corpus]` antes de citar percentual exato.
3. **Houve atraso de obra?** Verificar se ultrapassou o prazo de tolerância
   contratual (praxe de mercado, tipicamente contratual — não há prazo fixo neste
   corpus; conferir a cláusula do contrato concreto).
4. **Há corretagem/SATI cobrada do adquirente?** Registrar a controvérsia como
   ponto de discussão contratual — este corpus não traz o número de tema
   repetitivo específico sobre corretagem/SATI; marcar `[VERIFICAR — não
   confirmado no corpus]` antes de citar precedente sobre o tema em peça.

## Tese do adquirente (consumidor)

- Devolução imediata é regra em qualquer hipótese de culpa — a diferença entre
  culpa do incorporador e culpa do adquirente está só no percentual retido, nunca
  no momento da devolução (Súmula 543 + Tema 577).
- Cláusula que condiciona a devolução ao término da obra, ou a parcela em
  prestações longas, é **nula de pleno direito** por abusividade (CDC art. 51, I
  e IV; Tema 577).
- Atraso de obra além da tolerância contratual é culpa do incorporador — abre a
  via da devolução integral e imediata, sem necessidade de provar dolo.

## Tese da incorporadora

- Se a rescisão foi por desistência do adquirente sem justa causa, cabe retenção
  do percentual cabível (contratual ou da Lei 13.786/2018, conforme a data do
  contrato) — mas a devolução do saldo remanescente continua sendo **imediata**,
  nunca condicionada ao término da obra.
- Para contrato anterior à Lei 13.786/2018, invocar a irretroatividade da lei nova
  — o regime de retenção aplicável é o da Súmula 543/Tema 577, não o percentual
  fixo da lei posterior.
- Atraso dentro do prazo de tolerância contratual não configura culpa — a defesa
  deve provar a data de entrega efetiva contra o prazo contratado mais a
  tolerância.

## Armadilhas

- **Não aplicar a Lei 13.786/2018 a contrato anterior à sua vigência.**
  Jurisprudência de tribunal (TJDFT) já reconheceu a irretroatividade — aplicar o
  regime percentual novo a um contrato antigo é erro de data de corte.
- Não confundir a **imediatidade** da devolução (sempre devida, seja qual for a
  culpa) com o **percentual** retido (que varia conforme a culpa e a lei
  aplicável) — são dois eixos diferentes da mesma súmula.
- Corretagem e taxa SATI: não citar número de súmula/tema sobre o assunto sem
  verificar — não está confirmado neste corpus.

## Fronteira

**Matéria registral e de posse do imóvel (registro do distrato, cancelamento de
averbação, reintegração de posse, usucapião) pertence ao `direito-imobiliario-adv-os`
— aponte, não duplique.** Cálculo de correção monetária e juros sobre o valor a
devolver → `calculosjudiciais-adv-os`. Rito comum fora do JEC (valor da causa acima
da alçada) → `civel-adv-os`. Validação de citação de jurisprudência →
`juris-adv-os`.
