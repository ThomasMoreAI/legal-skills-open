---
name: contrato-rede-credenciada-saude-sbroggioadv
title: Contrato e rede credenciada
description: 'Estrutura a disputa sobre rede credenciada — descredenciamento e substituição de hospital (dever de comunicação e equivalência, Lei 9.656 art. 17), reembolso dentro e fora da rede (art. 12, VI, e a linha jurisprudencial do STJ), home care como previsão contratual e reembolso (sem entrar no mérito clínico, que é do direito-medico-adv-os), e autogestão sob o CDC (Súmula 608). Ótica do beneficiário, não do prestador. Aciona: descredenciamento de hospital, hospital saiu da rede, reembolso negado, plano não paga reembolso, home care contratual, autogestão e CDC.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/contrato-rede-credenciada-saude
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# Contrato e rede credenciada

## Quando esta skill entra

Toda disputa entre beneficiário e operadora sobre a rede credenciada — descredenciamento,
substituição de prestador, reembolso (dentro ou fora da rede) e a previsão contratual de
home care — pela ótica do **beneficiário**, nunca a relação B2B prestador × operadora.

## Descredenciamento e substituição de hospital

**Lei 9.656/1998, art. 17**: a inclusão de qualquer prestador gera compromisso de
manutenção durante a vigência do contrato. Substituição **é facultada**, desde que por
prestador **equivalente** e mediante comunicação **aos consumidores e à ANS com 30 dias de
antecedência** — ressalvado esse prazo nos casos de rescisão por fraude ou infração de
normas sanitárias/fiscais (§ 1º).

- **§ 2º**: se a substituição do estabelecimento hospitalar ocorrer **por vontade da
  operadora durante internação**, o estabelecimento é obrigado a **manter a internação** e
  a operadora a **pagar as despesas até a alta** (a critério médico).
- **§ 3º**: exceção — se a substituição decorrer de **infração às normas sanitárias**
  durante a internação, a operadora responde pela **transferência imediata** para
  estabelecimento equivalente, **sem ônus adicional** ao consumidor.

**Indisponibilidade de leito** (art. 33): sem leito na rede própria/credenciada, é
garantido acesso a acomodação em **nível superior**, sem ônus adicional.

## Reembolso

Base legal: **art. 12, VI** — reembolso em urgência/emergência, quando inviável a rede
própria/contratada, nos limites da tabela de preços do produto, pagável em até **30 dias**
após a entrega da documentação.

| Situação | Regra |
|---|---|
| Regra geral fora da rede | Reembolso só em hipóteses **excepcionais**: inexistência/insuficiência de prestador credenciado no local, ou urgência/emergência |
| Urgência em hospital de alto custo não credenciado | Reembolso devido, mas **limitado ao valor da rede própria** |
| Omissão da operadora em indicar prestador da rede | Reembolso **integral** |
| Descumprimento do dever de atendimento no mesmo município | Reembolso **integral**, incluindo transporte, em até 30 dias |
| Fora da rede mesmo em caso coberto | Pode ser **limitado ao "preço de tabela"** da operadora, mesmo em caso urgente — sem enriquecimento indevido do beneficiário |
| Prazo para pedir reembolso não pago | **10 anos** (CC, art. 205) — não confundir com a prescrição trienal de repetição de indébito por reajuste nulo |
| Cessão do crédito de reembolso a clínica não credenciada, sem desembolso prévio | **Não é possível** — reembolso pressupõe pagamento prévio pelo beneficiário |

## Home care — previsão contratual e reembolso, sem mérito clínico

A Lei 9.656 **não tem artigo autônomo** sobre home care. A base é o Anexo da RN 465/2021,
que define atenção/internação domiciliar: **quando a atenção domiciliar não substitui a
internação hospitalar**, ela fica sujeita a **previsão contratual ou negociação entre as
partes** — não há obrigação legal automática fora da hipótese de substituição. Esta skill
trata apenas do **contrato** (o que foi previsto, o reembolso quando não há rede própria de
home care) — **não** entra no mérito de qual paciente "precisa" de home care (isso é
clínico). **Não cite** precedente específico não confirmado neste corpus sobre home care —
use `[VERIFICAR — não confirmado no corpus]` se precisar de um número de acórdão para essa
matéria.

## Autogestão e o CDC

**Súmula 608/STJ** (vigente): aplica-se o CDC a todo contrato de plano de saúde —
individual, familiar, coletivo empresarial ou por adesão — **exceto** os administrados por
entidades de **autogestão**. Mesmo em autogestão, onde o CDC não incide, a lógica de
razoabilidade do reajuste por faixa etária (Tema 952/STJ) continua se aplicando, só que
pela via da própria Lei 9.656/normas ANS, não pelo CDC.

## Tese do beneficiário × tese da operadora

**Beneficiário**: exige comunicação regular de 30 dias na substituição; se internado no
momento da troca, exige manutenção até a alta com despesas por conta da operadora (§ 2º);
cobra reembolso pelas hipóteses excepcionais da tabela acima; se autogestão, não invoca CDC
— usa diretamente a Lei 9.656 e as normas da ANS.

**Operadora**: sustenta a faculdade de substituir por equivalente com aviso regular; nega
reembolso fora das hipóteses excepcionais, alegando rede própria suficiente e disponível na
região; se autogestão, invoca a exceção da Súmula 608 para afastar o CDC (mas não a
razoabilidade do Tema 952).

## Armadilhas

- **T1** — não citar Súmula 469 (cancelada); a base é a **608**, com a exceção de
  autogestão já no enunciado.
- Não reproduza número de precedente de home care não confirmado neste corpus.

## Fronteira

Relação B2B prestador × operadora (credenciamento/descredenciamento do lado do
prestador): `credenciamento-plano-saude` (`direito-medico-adv-os`) — é relação jurídica
distinta, o beneficiário não é parte desse contrato. Mérito clínico de indicação de home
care: `acao-home-care` (`direito-medico-adv-os`). Negativa de cobertura por rol:
`negativa-cobertura-saude-suplementar`.
