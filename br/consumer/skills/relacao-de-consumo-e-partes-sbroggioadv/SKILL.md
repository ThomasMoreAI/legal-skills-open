---
name: relacao-de-consumo-e-partes-sbroggioadv
title: Relação de Consumo e Partes
description: 'Identifica se há relação de consumo e quem são as partes: consumidor (art. 2º, CDC) e fornecedor (art. 3º, CDC), a distinção entre destinatário final fático e econômico, as três teorias (finalista, maximalista, finalista mitigada), o consumidor por equiparação (coletividade, vítimas do evento, expostos a práticas comerciais) e a solidariedade na cadeia de fornecimento. Aciona: quando a peça precisa fundamentar a incidência do CDC, quando há dúvida se uma pessoa jurídica é consumidora, quando é preciso identificar o fornecedor correto para responsabilizar ou para defender, ou quando a tese depende de equiparação (bystander, vítima de publicidade, cadastro negativo).'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/relacao-de-consumo-e-partes
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Relação de Consumo e Partes

## Quando esta skill entra
Toda peça consumerista começa aqui: sem relação de consumo, não há CDC. Use esta skill para
fundamentar a incidência do Código antes de discutir vício, defeito, prazo ou dano — e para checar
se a parte que você quer processar (ou defender) é, de fato, fornecedor da cadeia.

## Base normativa
- **Consumidor (art. 2º, CDC):** "toda pessoa física ou jurídica que adquire ou utiliza produto ou
  serviço como destinatário final." Parágrafo único: equipara-se a consumidor a coletividade de
  pessoas, ainda que indetermináveis, que haja intervindo nas relações de consumo.
- **Fornecedor (art. 3º, CDC):** pessoa física ou jurídica, pública ou privada, nacional ou
  estrangeira, e entes despersonalizados, que produzem, montam, criam, constroem, transformam,
  importam, exportam, distribuem ou comercializam produtos, ou prestam serviços. §1º: produto é
  qualquer bem, móvel ou imóvel, material ou imaterial. §2º: serviço é qualquer atividade
  remunerada no mercado de consumo, inclusive bancária, financeira, de crédito e securitária —
  salvo relação trabalhista.
(fonte: `context/cdc-lei-8078.md`)

## O teste: as três teorias sobre "destinatário final"
O art. 2º não define "destinatário final" — coube à doutrina e à jurisprudência decidir se ele é
fático ou também econômico. Três correntes disputam o critério; nenhum enunciado sumular
localizado no corpus resolve a disputa em definitivo, então a skill apresenta as três e o teste
prático de cada uma.

1. **Teoria finalista (majoritária):** destinatário final é quem retira o bem do mercado para uso
   próprio, pessoal ou familiar, encerrando a cadeia produtiva — sem reintroduzi-lo na cadeia de
   produção ou revenda.
2. **Teoria maximalista (minoritária):** basta o destinatário final **fático** — quem adquire e
   retira o bem do mercado, ainda que para uso profissional/insumo de sua atividade.
3. **Teoria finalista mitigada (a que prevalece na prática dos tribunais superiores):** parte da
   finalista, mas admite a incidência do CDC quando a pessoa física ou jurídica, mesmo adquirindo
   o produto/serviço para sua atividade profissional, demonstra **vulnerabilidade** (técnica,
   jurídica, informacional ou econômica) em face do fornecedor — sem relação de insumo direto com
   o objeto social e sem expertise no bem contratado.

`[VERIFICAR — não confirmado no corpus]` número de precedente líder do STJ sobre finalismo
mitigado — não citar REsp específico sem conferir na fonte oficial antes de usar em peça.

## Consumidor por equiparação (quem mais entra pela porta do CDC)
- **Art. 2º, parágrafo único** — coletividade de pessoas, ainda que indetermináveis, que
  intervierem na relação de consumo (proteção coletiva/difusa).
- **Art. 17** — "equiparam-se aos consumidores todas as vítimas do evento", na Seção de
  responsabilidade pelo **fato** do produto/serviço (bystander: quem sofre o acidente de consumo
  sem ter contratado nada — ex.: pedestre atropelado por defeito de freio).
- **Art. 29** — "equiparam-se aos consumidores todas as pessoas determináveis ou não, expostas às
  práticas" do Capítulo V (oferta, publicidade, práticas abusivas, cobrança, bancos de dados) —
  quem foi alvo de publicidade enganosa ou negativado indevidamente, mesmo sem ter comprado nada.

## Cadeia de fornecimento e solidariedade
- **Art. 7º, parágrafo único** — havendo mais de um autor da ofensa, todos respondem
  **solidariamente** pela reparação.
- **Art. 25, §§1º e 2º** — é vedada cláusula que exonere a obrigação de indenizar; havendo mais de
  um responsável, todos respondem solidariamente (§1º); dano causado por componente ou peça
  incorporada responsabiliza solidariamente fabricante/construtor/importador **e** quem incorporou
  (§2º).
- Combinado com os arts. 12/13/18 (ver `vicio-defeito-e-responsabilidade`), a cadeia inteira —
  fabricante, importador, distribuidor, comerciante — pode ser chamada a responder; a defesa
  individual de cada elo está em provar que **não integra** a cadeia daquele produto/serviço.

## Tese do consumidor × Tese do fornecedor
- **Tese do consumidor:** buscar a equiparação (arts. 2º § único, 17, 29) sempre que não houver
  contrato direto, e apontar a solidariedade da cadeia inteira para ampliar o polo passivo e o
  patrimônio executável.
- **Tese do fornecedor:** quando o réu for pessoa jurídica adquirente, atacar a finalidade do
  negócio — provar que o bem é insumo direto da atividade-fim, sem vulnerabilidade técnica, para
  afastar o CDC e cair no regime geral do Código Civil (prazos, ônus da prova e cláusulas
  limitativas mais favoráveis ao fornecedor). Na cadeia, provar que não fabricou, não identificou
  o produto sem rótulo, ou não incorporou o componente defeituoso.

## Armadilhas
- **T13** — ao conferir citação de artigo contra os anexos deste `context/`, normalize espaço em
  branco antes de comparar; o HTML do Planalto quebra linha no meio da frase e um grep literal
  pode dar falso negativo.
- Não confundir consumidor por equiparação (arts. 17/29, que dependem do fato/prática) com
  consumidor "por analogia" fora de qualquer hipótese legal — a equiparação é numerus clausus dos
  artigos citados, não uma cláusula aberta.

## Fronteira
Discussão de mérito sobre revisão de contrato bancário, juros e capitalização: `bancario-adv-os`.
Rito comum não-consumerista (quando a PJ não se enquadra em nenhuma teoria): `civel-adv-os`.
Validação de citação de precedente antes de usar em peça: `juris-adv-os`.
