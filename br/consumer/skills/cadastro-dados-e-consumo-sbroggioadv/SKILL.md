---
name: cadastro-dados-e-consumo-sbroggioadv
title: Cadastro, dados e consumo
description: 'Trata o acesso, a retificação e o compartilhamento de dados do consumidor em cadastros de consumo (CDC arts. 43 e 44) na fronteira com proteção de dados, e declara a pendência do Tema 1.404/STJ (afetado, não julgado) sobre comercialização de dados "não sensíveis" por bureaus de crédito, sem escolher lado. Cobre compartilhamento sem consentimento e a dupla face consumidor × arquivista/fornecedor de cadastro. Aciona: consumidor quer acessar ou corrigir dado em cadastro de consumo, empresa vendeu ou compartilhou dado cadastral sem autorização, dúvida sobre se banco de dados de consumo é "público", defesa de arquivista de cadastro questionado sobre origem do dado.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/cadastro-dados-e-consumo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Cadastro, dados e consumo

## Quando esta skill entra
Acesso, correção ou compartilhamento indevido de dados do consumidor em cadastro, ficha,
registro de consumo — banco de dados de proteção ao crédito e congêneres.

## Base normativa
CDC (Lei 8.078/1990), arts. 43 e 44.

## Acesso e retificação — art. 43
O consumidor tem acesso às informações existentes em cadastros, fichas, registros e dados
pessoais e de consumo arquivados sobre ele **e sobre as respectivas fontes** (caput). Os cadastros
devem ser objetivos, claros, verdadeiros e em linguagem de fácil compreensão, sem informação
negativa referente a período superior a **5 anos** (§1º). Abertura de cadastro não solicitada pelo
consumidor deve ser comunicada por escrito (§2º). Encontrada inexatidão, o consumidor pode exigir
correção imediata; o arquivista tem **5 dias úteis** para comunicar a alteração aos destinatários
das informações incorretas (§3º). Consumada a prescrição da cobrança, o sistema de proteção ao
crédito **não pode** fornecer informação que impeça ou dificulte novo acesso a crédito (§5º).
Informações devem estar em formato acessível à pessoa com deficiência, mediante solicitação (§6º).

**Natureza pública do cadastro (§4º):** bancos de dados e cadastros de consumidores, serviços de
proteção ao crédito e congêneres são considerados **entidades de caráter público** — isso significa
sujeição ao regime de transparência e correção do art. 43, não que sejam órgãos estatais.

## Cadastro de reclamações fundamentadas — art. 44
Órgãos públicos de defesa do consumidor mantêm cadastro atualizado de reclamações fundamentadas
contra fornecedores, com divulgação pública e anual, indicando se a reclamação foi atendida. O
acesso é facultado a qualquer interessado para orientação e consulta (§1º). Aplicam-se, no que
couber, as mesmas regras do art. 43 (§2º).

## Tema 1.404/STJ — AFETADO, NÃO JULGADO — declarar a pendência
🟡 Segunda Seção do STJ, REsps 2.226.946/SP e 2.226.097/SP, afetação em janeiro de 2026. Questão
submetida a julgamento: (i) se é lícita a comercialização a terceiros de dados pessoais "não
sensíveis" sem consentimento do titular; (ii) se há dano moral *in re ipsa* na hipótese de
ilicitude. **Não escolher lado.** Enquanto pendente, qualquer peça sobre venda/compartilhamento de
dados cadastrais por SPC/Serasa e similares precisa **declarar a divergência atual** — o acórdão de
afetação já aponta julgados de origem pela ilicitude, mas não há tese do STJ firmada.

## Compartilhamento sem consentimento
A base do CDC continua sendo o art. 43: dado incorreto ou origem não identificável é motivo de
correção imediata (§3º); abertura de cadastro sem solicitação do consumidor exige comunicação
por escrito (§2º) — sua ausência é indício de irregularidade na coleta ou repasse. A fronteira
entre a norma consumerista (dado de consumo) e a proteção de dados pessoal em sentido amplo é
tratada abaixo.

## Tese do consumidor
Exigir a fonte do dado (caput do art. 43); exigir correção em 5 dias úteis e cobrar a comunicação
da alteração a todos os destinatários que receberam a informação incorreta (§3º); diante de
compartilhamento sem base legal ou consentimento, apontar a ausência de comunicação prévia (§2º)
como falha do arquivista; enquanto o Tema 1.404/STJ estiver pendente, sustentar a tese de
ilicitude com base nos julgados de origem já favoráveis, sem afirmar que é entendimento pacífico
do STJ.

## Tese do fornecedor/arquivista
Demonstrar cumprimento do dever de comunicação prévia (§2º) e do prazo de correção (§3º);
demonstrar que a informação negativada respeita o teto de 5 anos (§1º); diante do Tema 1.404/STJ
pendente, sustentar a tese de licitude da comercialização de dado "não sensível" apontando a
própria pendência como ausência de vedação legal expressa e específica — sem afirmar que o STJ já
decidiu nesse sentido.

## Armadilhas
Não confundir a "natureza de caráter público" do §4º do art. 43 (regime de transparência) com
órgão público estatal. Não citar o Tema 1.404/STJ como se já tivesse tese firmada — está
**afetado e pendente**; declarar a divergência, nunca escolher lado como se fosse jurisprudência
consolidada.

## Fronteira
Dano moral por inclusão indevida em cadastro de inadimplentes e Súmula 385/STJ →
`negativacao-indevida-e-cadastro`. Dado pessoal puro fora de relação de consumo (LGPD em sentido
amplo, sem fornecedor/consumidor envolvido) não é deste plugin — apontar, não duplicar.
