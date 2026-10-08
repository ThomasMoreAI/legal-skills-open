---
name: servico-publico-e-continuidade-sbroggioadv
title: Serviço público essencial e continuidade
description: 'Trata corte de serviço público essencial (água, energia, telefonia fixa) por débito — atual ou pretérito — à luz do dever de continuidade (art. 22 e art. 6º, X, CDC). Corrige a citação fantasma da "Súmula 194/STJ" para a matéria (a súmula real trata de prescrição contra construtor) e delimita o alcance real do Tema 699/STJ, restrito ao subcaso de fraude no medidor. Aciona: quando o usuário relata corte de fornecimento de serviço público essencial por falta de pagamento, com ou sem aviso prévio.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/servico-publico-e-continuidade
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Serviço público essencial e continuidade

## Quando esta skill entra

Corte (ou ameaça de corte) de fornecimento de serviço público essencial — água,
energia, telefonia fixa — por débito, seja ele do período corrente ou de período
antigo já vencido, com ou sem aviso prévio.

## Base normativa

- **Art. 22, CDC** — os órgãos públicos, por si ou por suas empresas, concessionárias,
  permissionárias ou qualquer outra forma de empreendimento, são obrigados a fornecer
  serviços adequados, eficientes, seguros e, quanto aos essenciais, **contínuos**.
  Parágrafo único: o descumprimento, total ou parcial, compele a pessoa jurídica a
  cumprir a obrigação e a reparar os danos causados, na forma do CDC.
- **Art. 6º, X, CDC** — direito básico à adequada e eficaz prestação dos serviços
  públicos em geral.

## O teste

1. Classificar o débito que motivou (ou motivaria) o corte: **atual** (do próprio
   período/mês de fornecimento em curso) ou **pretérito** (dívida antiga, já vencida há
   tempo, relativa a período anterior).
2. Débito **atual**, com aviso prévio ao consumidor: a jurisprudência do STJ admite o
   corte como meio de cobrança regular do serviço essencial.
3. Débito **pretérito**: a jurisprudência do STJ, de forma pacífica e reiterada, **veda**
   o corte como meio de cobrança — a via cabível é a **ação de cobrança judicial
   ordinária**, não a autotutela do corte.
4. Hipótese específica de **fraude no medidor** apurada com contraditório e ampla
   defesa: aplica-se o **Tema 699/STJ** (ver Base normativa e Armadilhas) — corte
   admitido, mas **limitado** ao consumo recuperado nos 90 dias anteriores à constatação
   da fraude, mediante prévio aviso, e executado em até 90 dias após o vencimento do
   débito recuperado — sem prejuízo de a concessionária ainda cobrar judicialmente o
   que exceder essa janela.
5. Em qualquer hipótese de corte, checar se houve **aviso prévio** — sua ausência, por
   si, já é fundamento autônomo de ilicitude.

## Tese do consumidor

Corte por débito pretérito é ilegal: o serviço é essencial e contínuo (art. 22), e o
meio próprio para o fornecedor cobrar dívida antiga é a ação de cobrança, não a
autotutela do corte. A ausência de aviso prévio, isoladamente, já torna o corte ilícito,
independentemente da natureza do débito. Fora da hipótese estrita de fraude no medidor
apurada com contraditório (Tema 699), não há amparo para o corte por débito antigo.

## Tese do fornecedor

O débito é atual (do período de fornecimento corrente), o corte foi precedido de aviso e
seguiu procedimento regular — hipótese em que a jurisprudência do STJ admite o corte
como meio legítimo de cobrança. Alternativamente, na hipótese de fraude apurada com
contraditório, o corte se limita ao consumo recuperado dentro da janela temporal do
Tema 699 e observou o aviso prévio exigido.

## Armadilhas

**T2 — esta é a trava central da skill.** A citação **"Súmula 194/STJ"** para
fundamentar a vedação do corte por débito pretérito **não existe com esse conteúdo** e
**nunca deve ser usada nesta matéria**. A Súmula 194/STJ real trata de prescrição de
**vinte anos** para ação de indenização contra construtor por defeito de obra — assunto
totalmente diferente e sem qualquer relação com corte de serviço público. Essa citação é
a mais repetida encontrada na pesquisa deste corpus, propagada por fontes secundárias
que copiam umas das outras sem checar a fonte oficial. **A regra do corte por débito
pretérito é jurisprudência reiterada do STJ — não é sumulada.** O único precedente
qualificado (repetitivo) sobre corte de serviço essencial é o **Tema 699/STJ**, e ele
cobre **apenas** o subcaso de fraude no medidor com recuperação de consumo — não a tese
geral de vedação do corte por débito antigo comum. Fundamentar a tese geral em
jurisprudência reiterada e doutrina, nunca em súmula inexistente, e citar o Tema 699
apenas quando o fato for, de fato, fraude no medidor.

## Fronteira

Revisão de tarifa ou reajuste regulatório de concessionária: fora do escopo desta
skill (matéria administrativo-regulatória). Cobrança judicial do débito antigo pela
concessionária: `execucao-adv-os`. Cálculo do valor do débito ou da recuperação de
consumo: `calculosjudiciais-adv-os`.
