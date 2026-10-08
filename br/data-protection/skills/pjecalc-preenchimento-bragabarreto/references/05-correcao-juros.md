# Índices de Correção Monetária e Juros de Mora — PJE-Calc

---

## Índices de Correção Monetária Disponíveis

| Índice | Descrição | Disponível desde |
|---|---|---|
| Tabela Única JT Diário | Taxas diárias da Tabela Única para Atualização de Débitos Trabalhistas | — |
| Tabela Única JT Mensal | Taxas mensais da Tabela Única para Atualização de Débitos Trabalhistas | — |
| TR | Taxa Referencial | — |
| IGP-M | Índice Geral de Preços do Mercado (FGV) | jun/1989 |
| INPC | Índice Nacional de Preços ao Consumidor (IBGE) | abr/1979 |
| IPC | Índice de Preços ao Consumidor (FIPE) | jan/1975 |
| IPCA | Índice de Preços ao Consumidor Amplo (IBGE) | jan/1980 |
| IPCA-E | IPCA Especial (IBGE) | dez/1991 |
| IPCA-E/TR | IPCA-E até 09/12/2009 + TR a partir de 10/12/2009 | dez/1991 |
| JAM | Juros e Atualização Monetária (correção + juros remuneratórios 3% a.a.) | jun/1967 |
| UFIR | Unidade Fiscal de Referência | jan/1992 a dez/2000 |
| Coeficiente UFIR | Para débitos previdenciários anteriores a jan/1995 | — |

---

## Tabelas de Juros de Mora

### Juros Padrão (débitos trabalhistas em geral)

| Período | Tipo | Alíquota |
|---|---|---|
| Até 26/02/1987 | Simples | 0,5% a.m. |
| 27/02/1987 a 03/03/1991 | Composto (capitalizado) | 1% a.m. |
| A partir de 04/03/1991 | Simples | 1% a.m. |

### Juros Fazenda Pública

| Período | Tipo | Alíquota |
|---|---|---|
| Até 03/05/2012 | Simples | 0,5% a.m. |
| A partir de 04/05/2012 | Simples | 70% da taxa SELIC |

### Juros SELIC Contribuição Social

Composição histórica das taxas SELIC aplicadas a débitos previdenciários. Disponível desde mar/1967.

---

## Regras de Atualização por Parcela

| Parcela | Correção Padrão | Juros Padrão | Observações |
|---|---|---|---|
| Verbas | Índice Trabalhista (Dados Gerais) | Juros Padrão | Automático |
| Salário-família | Índice Trabalhista | Juros Padrão | Automático |
| Seguro-desemprego | Índice Trabalhista | Juros Padrão | Automático |
| FGTS | Índice Trabalhista (padrão) ou JAM | Juros Padrão (se não JAM) | JAM já contempla correção + juros |
| CS Salários Devidos | Trabalhista ou Previdenciária | Conforme opção | Lei 11.941/2009: Trabalhista + Previdenciária |
| CS Salários Pagos | Trabalhista ou Previdenciária | Conforme opção | Igual à CS Salários Devidos |
| Previdência Privada | Índice Trabalhista (padrão) ou Outro | Opcional | Checkbox Juros |
| Custas Judiciais | Sem atualização (padrão) | Opcional | Marcar para atualizar |
| Honorários | Definido por lançamento | Definido por lançamento | Índice Trabalhista ou Outro |
| Multas/Indenizações | Definido por lançamento | Definido por lançamento | Índice Trabalhista ou Outro |
| Pensão Alimentícia | — | — | Devida na data da liquidação |
| Imposto de Renda | — | — | Apurado na data da liquidação |

---

## Atualização da Contribuição Social

### Opção 1 — Atualização Trabalhista (padrão)
- Considera que a CS é devida no **dia 2 do mês seguinte à liquidação**.
- Aplica apenas correção monetária (índice dos Dados Gerais).
- Juros: opcional (marcar checkbox).

### Opção 2 — Atualização Previdenciária
- Considera que a CS é devida **desde a prestação do serviço**.
- Corrige pela tabela **Coeficiente UFIR** + aplica **Juros SELIC**.
- Habilita campo de **Multa Previdenciária** (Urbana/Rural; Integral/Reduzido).

### Opção 3 — Trabalhista + Previdenciária (Lei 11.941/2009)
- Atualização Trabalhista até a data da liquidação da sentença (informar no campo "Aplicar até").
- Atualização Previdenciária a partir do dia 2 do mês seguinte.

---

## Acumulação dos Índices de Correção (na Liquidação)

| Critério | Descrição |
|---|---|
| A partir do mês subsequente ao vencimento | Para todas as verbas: correção inicia no mês seguinte ao vencimento |
| A partir do mês de vencimento | Para todas as verbas: correção inicia no próprio mês de vencimento |
| Misto | Verbas mensais: mês subsequente; Verbas anuais/rescisórias: mês de vencimento |

---

## Combinação de Índices

Para aplicar dois índices em períodos distintos:
1. Marcar checkbox **Combinar com Outro Índice**.
2. Selecionar o segundo índice.
3. Informar a data de início do segundo índice no campo **A partir de**.

Exemplo: IPCA-E até 10/11/2021 + SELIC a partir de 11/11/2021 (conforme ADC 58 STF).
