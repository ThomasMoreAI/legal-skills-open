---
name: rescisao-cancelamento-plano-saude-sbroggioadv
title: Rescisão e cancelamento de plano de saúde
description: 'Estrutura a defesa e a ação contra rescisão/cancelamento de plano de saúde — individual (RN 593/2023 + RN 617/2024: notificação até o 50º dia, cura de 10 dias, mínimo de duas mensalidades em 12 meses, vedação absoluta durante internação), coletivo com 30 ou mais beneficiários (rescisão imotivada com aviso de 60 dias e Tema 1.082/STJ) e coletivo com menos de 30 (Tema 1.047/STJ, 20/03/2026: válida com motivação idônea), além da continuidade do demitido sem justa causa e do aposentado (Lei 9.656 arts. 30 e 31). Aciona: cancelamento de plano de saúde, rescisão unilateral, plano cancelado por inadimplência, demissão e plano de saúde, aposentadoria e manutenção do plano.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/rescisao-cancelamento-plano-saude
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Rescisão e cancelamento de plano de saúde

## Quando esta skill entra

Toda rescisão, suspensão ou cancelamento de plano de saúde — por iniciativa da operadora
(inadimplência, rescisão imotivada de coletivo) ou como direito do beneficiário de se
manter no plano após demissão/aposentadoria — como evento contratual geral.

## Base normativa e o teste por regime

### Individual/familiar — vedado, salvo fraude ou inadimplência

**Lei 9.656/1998, art. 13, parágrafo único, II**: vedada a rescisão unilateral, salvo
fraude ou inadimplência superior a **60 dias** (consecutivos ou não, nos últimos 12 meses),
desde que o consumidor seja notificado **até o 50º dia** de inadimplência. **Inciso III**:
vedada em qualquer hipótese durante internação do titular.

Operacionalizado hoje pela **RN 593/2023**, alterada pela **RN 617/2024**:
- Notificação **até o 50º dia** de não pagamento; se chegar depois, ainda é válida desde
  que garanta **10 dias** de cura a partir dela.
- Exclusão só após **10 dias corridos** da notificação, sem pagamento.
- Exige-se, no mínimo, **2 mensalidades não pagas** (consecutivas ou não) **em 12 meses**.
- **Vedação absoluta** de suspensão/rescisão durante internação — só após a alta, com novo
  prazo de 10 dias.
- Meio de notificação sem comprovação inequívoca de ciência (e-mail com confirmação de
  leitura, SMS/app com confirmação, ligação gravada, carta com AR) **invalida** o
  cancelamento.

### Coletivo com 30 ou mais beneficiários

Jurisprudência consolidada (não há RN de rescisão coletiva nomeada): admite-se a
**rescisão unilateral imotivada** após 12 meses de vigência, mediante notificação com
**antecedência mínima de 60 dias**.

**Tema 1.082/STJ** (tese firmada): "A operadora, mesmo após o exercício regular do direito
à rescisão unilateral de plano coletivo, deverá assegurar a continuidade dos cuidados
assistenciais prescritos a usuário internado ou em pleno tratamento médico garantidor de
sua sobrevivência ou de sua incolumidade física, até a efetiva alta, desde que o titular
arque integralmente com a contraprestação devida."

### Coletivo empresarial com menos de 30 beneficiários

**Tema 1.047/STJ**, decidido em **20/03/2026** (recentíssimo — qualquer peça escrita antes
dessa data está desatualizada aqui): "A resilição unilateral, pela operadora, do contrato
de plano de saúde coletivo empresarial com menos de trinta beneficiários é válida, desde
que apresentada **motivação idônea**." O STJ reafirmou que o **CDC** se aplica a esses
coletivos pequenos (natureza híbrida + vulnerabilidade do grupo), mas não proíbe de modo
absoluto a extinção — a exigência é de motivação idônea, não rescisão puramente imotivada.

### Continuidade do demitido sem justa causa e do aposentado (art. 30 e art. 31)

**Lei 9.656/1998, art. 30**: ao consumidor que contribuir para plano coletivo em
decorrência de vínculo empregatício, em caso de rescisão/exoneração **sem justa causa**, é
assegurado o direito de manter a condição de beneficiário, nas **mesmas condições de
cobertura**, desde que assuma o pagamento integral. Prazo: **um terço do tempo de
permanência** no plano, mínimo de **6 meses**, máximo de **24 meses** (§ 1º). Extensivo a
todo o grupo familiar (§ 2º); em morte do titular, o direito passa aos dependentes (§ 3º);
não exclui vantagem de negociação coletiva (§ 4º); cessa com **admissão em novo emprego**
(§ 5º).

**Art. 31**: ao aposentado que contribuiu por vínculo empregatício por **10 anos ou mais**,
o direito é **assegurado sem prazo** (mesmas condições, pagamento integral). Contribuição
**inferior a 10 anos**: manutenção à razão de **1 ano por ano de contribuição** (§ 1º),
observadas as mesmas condições dos §§ 2º a 6º do art. 30 (§§ 2º e 3º).

### Cancelamentos em massa 2024–2026

O que está confirmado: a proteção do beneficiário vem da combinação **RN 593/617**
(processual, contra inadimplência) + **Tema 1.082** (continuidade em tratamento/internação
mesmo em rescisão coletiva regular) + **Tema 1.047** (motivação idônea nos coletivos
pequenos). Não há, nos anexos deste plugin, uma RN nomeada especificamente como resposta
regulatória a cancelamentos em massa de um grupo de pacientes específico — não afirme a
existência de norma batizada para isso; use o conjunto de proteções gerais acima.

## Tese do beneficiário × tese da operadora

**Beneficiário**: no individual, ataca vício na notificação (fora do 50º dia sem os 10 dias
de cura, meio sem comprovação, menos de 2 mensalidades) ou cancelamento durante internação;
no coletivo, exige aviso de 60 dias e continuidade se estiver em tratamento (Tema 1.082); no
coletivo pequeno, exige motivação idônea (Tema 1.047); pós-demissão/aposentadoria, invoca
art. 30/31 e o pagamento integral já ofertado.

**Operadora**: no individual, junta a prova de notificação regular e o histórico de
inadimplência; no coletivo 30+, sustenta o exercício regular do direito potestativo com
aviso de 60 dias; no coletivo pequeno, junta a motivação (queda de sinistralidade do grupo,
inviabilidade financeira) exigida pelo Tema 1.047; contra o art. 30/31, alega admissão em
novo emprego ou descumprimento do pagamento integral.

## Armadilhas

- **T1** — não citar Súmula 469 (cancelada); a base de CDC é a **608**.
- O **Tema 1.047** é de **20/03/2026** — qualquer conhecimento anterior a essa data trata a
  matéria como lacuna/repetitivo pendente, o que hoje é erro.

## Fronteira

O `direito-medico-adv-os` tem `acao-rescisao-coletivo`, focada no caso do paciente em
**tratamento grave em curso** (ótica assistencial, tempo-crítica). Esta skill cobre o
evento contratual **geral** (individual e coletivo, motivado e imotivado, continuidade
pós-emprego) — cross-link nos dois sentidos quando o caso envolver tratamento em curso.
Precisa de liminar: `tutela-urgencia-cobertura-saude`.
