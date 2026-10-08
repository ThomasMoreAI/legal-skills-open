# Exemplos Práticos — Tutorial Oficial PJE-Calc (CSJT)

Fonte: Tutorial oficial do PJE-Calc, wiki CSJT (arquivado em 12/08/2022).

---

## Exemplo 1 — Cálculo básico com verbas rescisórias

**Parâmetros:**
- Admissão: 23/03/2011 | Demissão: 12/08/2013 | Ajuizamento: 30/10/2013
- Maior Remuneração: R$ 1.200,00 | Última Remuneração: R$ 1.000,00

**Verbas:** Saldo de Salário, Aviso Prévio, 13º Salário Proporcional, Férias Proporcionais + 1/3, FGTS + 40%, Multa Art. 477 CLT.

**Resolução resumida:**
1. Novo Cálculo → Parâmetros → preencher dados → Salvar.
2. Férias → verificar sugestão do sistema → Salvar.
3. Histórico Salarial → sistema cria automaticamente com base na Última Remuneração.
4. Verbas → Expresso → marcar todas as verbas → Salvar.
5. Verbas Reflexas → clicar Exibir em cada verba principal → marcar reflexas deferidas.
6. FGTS → marcar Multa 40% → Salvar.
7. Contribuição Social → conferir parâmetros → Salvar.
8. Imposto de Renda → marcar Apurar IR → Salvar.
9. Correção, Juros e Multa → conferir índices → Salvar.
10. Operações → Liquidar → informar data → Liquidar.
11. Operações → Imprimir → selecionar relatórios → Imprimir.

---

## Exemplo 2 — Diferença Salarial, Adicional de Periculosidade e Horas Extras

**Parâmetros:**
- Admissão: 23/03/2011 | Demissão: 12/08/2013 | Ajuizamento: 30/10/2013
- Maior Remuneração: R$ 1.200,00 | Última Remuneração: R$ 1.000,00

**Faltas:**
- 11/06/2012 a 13/06/2012 (injustificadas)
- 25/09/2012 a 28/09/2012 (injustificadas)
- 10/05/2013 (justificada — Doação de Sangue)

**Férias:** 2011/2012 gozadas de 18/06/2012 a 17/07/2012 (pagas no contracheque de 06/2012, valor R$ 829,33).

**Verbas:** Diferença Salarial, Adicional de Periculosidade 30%, Horas Extras 50% (50h mensais) + reflexos em Aviso Prévio, 13º, Férias + 1/3, FGTS + 40% e RSR.

**Pontos-chave:**
- Lançar **dois** históricos salariais: "Salário Pago" (incidência CS) e "Salário Devido" (sem incidência).
- Parâmetros da Verba Diferença Salarial: Base = Salário Devido; Valor Pago = Calculado sobre Salário Pago.
- Parâmetros da Verba Adicional de Periculosidade: Base = Salário Pago + Diferença Salarial (Integralizar: Não).
- Parâmetros da Verba HE 50%: Base = Salário Pago + Diferença Salarial (Integralizar: Sim) + Adicional de Periculosidade (Integralizar: Sim); Quantidade = 50.
- Ocorrências da CS: ajustar 06/2012 somando R$ 829,33 (férias gozadas pagas no contracheque).
- Após alterar Parâmetros da Verba → clicar **Regerar**.

---

## Exemplo 3 — Contribuição Social por Atividade Econômica, Previdência Privada e Pensão Alimentícia

**Base:** Cálculo do Exemplo 1.

**Alterações:**
- CS: apurar sobre Salários Pagos; Atividade Econômica: Condomínios Prediais.
- Previdência Privada: 12% sobre Saldo de Salário e 13º Salário.
- Pensão Alimentícia: 10% sobre Saldo de Salário e 13º Salário + incidir sobre juros.
- IR: incidir sobre juros de mora; Aposentado > 65 anos; 2 dependentes.

**Resolução resumida:**
1. CS → marcar "Apurar CS sobre Salários Pagos" → Salvar.
2. CS → Ocorrências → Regerar → selecionar "Por Atividade Econômica" → buscar "prediais" → selecionar "Condomínios Prediais" → Confirmar.
3. Verbas → Parâmetros do Saldo de Salário → marcar Previdência Privada e Pensão Alimentícia → Salvar. Repetir para 13º Salário.
4. Previdência Privada → marcar Apurar → informar 12% → Adicionar → Salvar.
5. Pensão Alimentícia → marcar Apurar → informar 10% → marcar Incidir sobre Juros → Salvar.
6. IR → marcar Apurar → marcar Incidir sobre Juros, Aposentado > 65, Dependentes (2) → Salvar.

---

## Exemplo 4 — Multas, Indenizações, Honorários e Custas Judiciais

**Base:** Cálculo do Exemplo 2.

**Multas e Indenizações:**
- Multa por Litigância de Má-Fé 10% (Reclamante/Reclamado, Calculada sobre Principal).
- Indenização R$ 1.000,00 vencida em 15/01/2016 (Terceiro: Fundo de Amparo ao Trabalhador / Reclamado, Informada).

**Honorários:**
- Advocatícios 20% sobre Bruto (Reclamante deve ao advogado Fulano de Tal).
- Periciais R$ 5.000,00 vencidos em 08/12/2015 (Reclamado deve ao perito Beltrano).

**Custas:**
- Liquidação: Calculada 0,5%.
- Atos OJ Urbana: 2 atos, vencimento 28/01/2016.
- Autos de Arrematação: bem avaliado em R$ 4.000,00, vencimento 05/02/2016.

---

## Exemplo 5 — Alteração de Índices de Correção e Juros

**Base:** Cálculo do Exemplo 2.

**Alterações:**
- Índice de correção das Verbas: Tabela JT Única Mensal.
- Base dos Juros: Verbas.
- Correção do FGTS: Índice JAM.
- CS Salários Devidos: desmarcar Lei 11.941/2009 (usar apenas Atualização Trabalhista).

**Resolução:**
1. Correção, Juros e Multa → Dados Gerais → selecionar "Tabela Única JT Mensal" → Salvar.
2. Dados Específicos → Base de Juros: "Verba" → FGTS: marcar "Utilizar Índice JAM" → CS/Salários Devidos: desmarcar Lei 11.941/2009 → Salvar.

---

## Exemplo 6 — Cálculo com Data Inicial Limitada e FGTS com Saldo

**Parâmetros:**
- Admissão: 14/11/2011 | Demissão: 12/08/2013 | Ajuizamento: 30/10/2013
- Data Inicial/Limitar Cálculos: 01/06/2013
- Maior Remuneração: R$ 800,00 | Última Remuneração: R$ 700,00

**Férias:** 2011/2012 gozadas de 18/03/2013 a 16/04/2013 (alterar de Indenizadas para Gozadas).

**Verbas:** Multa Art. 477, Salário Retido (a partir de jun/2013), Aviso Prévio, 13º Proporcional 2013, Férias Proporcionais + 1/3, FGTS + 40% sobre Salários Pagos + Salário Retido + Aviso Prévio + 13º.

**FGTS depositado:** R$ 735,60 em 10/10/2013.

**Pontos-chave:**
- Histórico Salarial: desmarcar FGTS e CS para os meses de Salário Retido (jun, jul, ago/2013).
- FGTS → marcar Multa 40% → informar Saldo (10/10/2013, R$ 735,60) → Adicionar → marcar Deduzir do FGTS → Salvar.
- Ocorrências do FGTS: ajustar bases de 12/2011 (R$ 816,67), 12/2012 (R$ 1.400,00) e 03/2013 (R$ 1.330,00) para incluir 13º e férias pagas durante o contrato.

---

## Exemplo 7 — Adicional Noturno com Valor Pago

**Parâmetros:**
- Admissão: 01/06/2006 | Demissão: 07/06/2013 | Ajuizamento: 29/06/2014
- Maior Remuneração: R$ 1.718,82 | Última Remuneração: R$ 1.600,00

**Verbas:** 120 Adicionais Noturnos 20% + reflexos em Aviso Prévio, 13º, Férias + 1/3, FGTS + 40% e RSR.

**Adicional Noturno pago nos contracheques:** R$ 80,00/mês de 10/2006 a 01/2013.

**Pontos-chave:**
- Histórico Salarial: criar "Adicional Noturno Pago" (incidência CS; competências 10/2006 a 01/2013; valor R$ 80,00).
- Parâmetros da Verba Adicional Noturno 20%:
  - Base = Última Remuneração; Proporcionalizar: NÃO → Adicionar.
  - Quantidade = 120; Proporcionalizar: SIM.
  - Valor Pago = Calculado; Base = Histórico Salarial "Adicional Noturno Pago"; Proporcionalizar: SIM → Adicionar.
- Regerar as ocorrências após alterar os parâmetros.

---

## Exemplo 8 — Liquidação, Atualização com Pagamentos Parciais

**Base:** Cálculo do Exemplo 6.

**Liquidação inicial:** 31/05/2015.

**Atualização:**
- Pensão Alimentícia: 10% sobre Salário Retido e 13º Salário, a partir de 17/07/2015, incidir sobre juros (ID0125847).
- Pagamento 1: R$ 3.000,00 em 10/09/2015 (ID0125789) — sem retenção de CS e pensão.
- Pagamento 2: R$ 1.000,00 em 13/10/2015 (ID0125841) — com retenção de CS e pensão.
- Multa: 5% sobre saldo devedor em 16/03/2016 (ID0125915).
- Honorários: 15% sobre saldo devedor em 16/03/2016 (ID0125915) + IR (IRPF) — credor Fulano de Tal.
- Custas: 1 ato OJ Urbana em 13/07/2015 (ID0125687) + 1 Embargos à Execução em 23/09/2015 (ID0125692).
- Liquidar Atualização: data corrente, ID0125642.

---

## Exemplo 9 — Horas Extras pelo Critério Mais Favorável, Intervalo Intra e Interjornadas

**Parâmetros:**
- Admissão: 25/08/2016 | Demissão: 09/03/2017 | Ajuizamento: 19/04/2017
- Última Remuneração: R$ 2.850,00 | Carga Horária: 220h

**Jornadas:**
- Até dez/2016: seg-sex 07:30-13:00 e 13:45-21:00; sáb 07:30-13:00.
- Jan/2017 em diante: seg-qua 07:30-13:00 e 13:45-18:30; qui-sáb 07:30-13:00.
- Fechamento do cartão: dia 20.

**Verbas:** HE 50% (critério mais favorável) + Intervalo Intrajornada + Intervalo Interjornadas + reflexos em AP, 13º, Férias + 1/3, RSR e FGTS + 40%.

**Pontos-chave:**
- Cartão de Ponto: lançar dois períodos com as respectivas jornadas; marcar checkboxes de intervalos.
- Apurar Cartão de Ponto (fechamento dia 20).
- Parâmetros das Verbas: Quantidade = "Importada do Cartão de Ponto".
- Ao liquidar: sistema alerta sobre Férias + 1/3 sem período de gozo → desmarcar incidências de CS e IR nas verbas reflexas Férias + 1/3.

---

## Exemplo 10 — Adicional Noturno, HE Diurnas e Noturnas, Domingos e Feriados em Dobro

**Parâmetros:**
- Admissão: 14/01/2015 | Demissão: 20/04/2017 | Ajuizamento: 23/05/2017
- Última Remuneração: R$ 3.200,00 | Carga Horária: 220h

**Jornada:** Seg a dom (inclusive feriados) — 19:00 às 07:00. Não aplicar horário prorrogado (Súmula 60 TST).

**Férias gozadas:** 2015/2016 de 14/03 a 12/04/2016; remuneração férias + 1/3 em 03/2016 = R$ 4.266,66.

**Verbas:** Adicional Noturno 20% + HE diurnas 50% + HE noturnas 60% + HE domingos/feriados 100% + Domingos em Dobro + Feriados em Dobro + reflexos.

**Pontos-chave:**
- Cartão de Ponto: jornada noturna 19:00-07:00; desmarcar "Aplicar horário prorrogado (Súmula 60 TST)".
- Lançar múltiplas verbas de HE com diferentes adicionais.
- Ocorrências do FGTS: ajustar 03/2016 somando R$ 4.266,66 (férias gozadas + 1/3 pagas no contracheque).
