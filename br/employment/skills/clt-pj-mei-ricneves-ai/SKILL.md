---
name: clt-pj-mei-ricneves-ai
title: CLT / PJ / MEI
description: 'Orienta sobre os regimes de contratação brasileiros: CLT, PJ (Pessoa Jurídica),

  MEI, CLT Flex e estágio. Analisa riscos de vínculo empregatício, compara custos

  reais de cada modalidade e orienta na escolha adequada para cada situação.'
author: ricneves-ai
author_url: https://github.com/ricneves-ai/flowgrammers-skills/tree/main/operacoes-rh/clt-pj-mei
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: employment
language: pt
tags: [clt, pj, mei, contratacao, vinculo-empregaticio, trabalhista]
---

# CLT / PJ / MEI

Especialista em regimes de contratação para o mercado brasileiro. Navegar corretamente entre CLT, PJ e MEI é fundamental para evitar passivos trabalhistas.

## Comparativo de Custos (Salário Bruto R$ 10.000)

| Regime | Custo para Empresa | Recebe Líquido | Risco |
|--------|-------------------|----------------|-------|
| CLT | ~R$ 13.500-15.000 | ~R$ 7.400 | Baixo |
| PJ (Simples) | ~R$ 10.600-11.200 | ~R$ 9.000-9.500 | Alto se mal estruturado |
| MEI | ~R$ 10.100-10.300 | ~R$ 9.700-9.900 | Muito alto — MEI não pode ter vínculo |

*Inclui: FGTS, INSS patronal, 13º, férias, VR/VT estimado*

## Quando Usar Cada Regime

**CLT** — Quando: trabalho subordinado, habitual, pessoal e contínuo; risco alto de vínculo empregatício; empresa quer proteger colaborador e ter compliance trabalhista

**PJ** — Quando: trabalho eventual, sem subordinação direta, com possibilidade de substituição; prestador tem outros clientes; atividade intelectual ou especializada

**MEI** — Quando: pessoa física empreendedora com faturamento até R$ 81k/ano; NÃO usar para mascarar relação de emprego

## Exemplos de Uso

```
Use clt-pj-mei para analisar a situação de um designer gráfico que trabalha:
40h/semana exclusivamente para minha empresa, segue meu processo criativo,
tem horário fixo das 9h às 18h, recebe R$ 7.000/mês como PJ há 14 meses.
Qual o risco de reconhecimento de vínculo empregatício? O que devo fazer?
Qual seria o custo de regularizar via CLT vs. manter o risco?
```

## Regras

1. AVISO: decisões de enquadramento trabalhista devem ser validadas por advogado trabalhista
2. Os 4 elementos do vínculo (art. 3º CLT): pessoalidade, habitualidade, subordinação, onerosidade
3. Contrato PJ não protege a empresa se os 4 elementos estiverem presentes — na Justiça do Trabalho o juiz analisa a realidade dos fatos
4. Ação trabalhista prescreve em 2 anos após a demissão mas abrange 5 anos retroativos
5. Trabalhador pode ser PJ para múltiplos clientes — a exclusividade aumenta muito o risco de vínculo
