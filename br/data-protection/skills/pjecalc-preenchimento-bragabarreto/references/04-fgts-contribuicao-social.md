# FGTS e Contribuição Social — Detalhamento

---

## FGTS

### Parâmetros Principais

| Parâmetro | Opções | Padrão |
|---|---|---|
| Destino | Pagar ao reclamante / Recolher em conta vinculada | Pagar ao reclamante |
| Compor Principal | Sim / Não | Sim |
| Alíquota | 8% (geral) / 2% (aprendiz) | 8% |
| Período | Todo o contrato (Admissão–Demissão) | Todo o contrato |

### Multa do FGTS

| Parâmetro | Opções |
|---|---|
| Apurar Multa | Checkbox |
| Tipo | Calculada / Informada |
| Percentual (se Calculada) | 40% (padrão — demissão sem justa causa) ou 20% (estabilidade provisória: CIPA, gestante, acidentário). Na extração: `fgts.multa_40=true` sempre; `fgts.multa_20=true` somente quando sentença determina 20%. |
| Base (se Calculada) | Devido / Diferença / Saldo e/ou Saque / Devido (-) Saldo / Devido (+) Saldo |
| Valor (se Informada) | Valor na data da demissão |
| Multa Art. 467 CLT | Checkbox `multaDoArtigo467` (50% sobre verbas incontroversas). **Dependente** do checkbox `multa` estar marcado. Além do checkbox FGTS, a Multa 467 também aparece como **reflexa automática** sob cada verba principal na aba Verbas (ex: "MULTA DO ARTIGO 467 DA CLT SOBRE SALDO DE SALÁRIO", "... SOBRE FÉRIAS + 1/3", etc.). |

### Saldo e/ou Saque

Registrar depósitos e saques da conta vinculada do FGTS:

| Campo | Instrução |
|---|---|
| Data | Data do depósito/saque |
| Valor | Montante |
| Ação | Clicar em **Adicionar** |
| Deduzir do FGTS | Marcar para abater do FGTS devido |

### Contribuições LC 110/2001

| Contribuição | Alíquota | Quando usar |
|---|---|---|
| Contribuição Social 10% | 10% sobre FGTS | Demissões sem justa causa (vigência: 01/10/2001 a 05/2013) |
| Contribuição Social 0,5% | 0,5% sobre FGTS | Todos os empregadores (vigência: 01/10/2001 a 05/2013) |

### Ocorrências do FGTS

A base de cada ocorrência é composta por:
- **Base (Histórico):** valores do Histórico Salarial com "incidência no FGTS" marcada.
- **Base (Verba):** valores das verbas com "incidência no FGTS" marcada nos Parâmetros da Verba.

**Ajustes manuais necessários:**
- Meses com 13º Salário pago: acrescentar o valor do 13º à base do mês de dezembro.
- Meses com férias gozadas + 1/3 pagas: acrescentar o valor à base do mês em que foram pagas.
- Meses de Salário Retido: desmarcar incidência no FGTS no Histórico Salarial para esses meses.

### Regerar Ocorrências do FGTS

1. FGTS → clicar em **Ocorrências**.
2. Clicar em **Regerar**.
3. Alterar Data Inicial, Data Final e/ou Alíquota conforme necessário.
4. Escolher entre **Manter** ou **Sobrescrever** alterações manuais.
5. Clicar em **Confirmar**.

---

## Contribuição Social (INSS)

### Parâmetros Principais

| Parâmetro | Opções | Padrão |
|---|---|---|
| Apurar CS sobre Salários Devidos | Checkbox | Marcado |
| Apurar CS sobre Salários Pagos | Checkbox | Desmarcado |
| Alíquota Segurado Empregado | Fixa (tabela progressiva) / Por Atividade Econômica | Fixa |
| Alíquota Empregador | Fixa 20% / Por Atividade Econômica | Fixa 20% |
| SAT (Seguro de Acidente de Trabalho) | 1%, 2% ou 3% | 3% |
| Terceiros | Apurar / Não apurar | Não apurar |
| Cobrar do Reclamante | Checkbox | Marcado |

### Alíquota por Atividade Econômica

Para alterar a alíquota do empregador por atividade:
1. Clicar em **Ocorrências** → **Regerar**.
2. Selecionar **Alíquota Empregador Por Atividade Econômica**.
3. Digitar palavra-chave no campo **Atividade Econômica**.
4. Selecionar a categoria na lista.
5. Escolher entre Manter/Sobrescrever → **Confirmar**.

### Base de Cálculo da CS

A base é montada **automaticamente** pelo sistema a partir de:
- Ocorrências do Histórico Salarial com "incidência na CS" marcada.
- Verbas Principais e Reflexas com "incidência na CS" marcada nos Parâmetros da Verba.

**Exclusões automáticas na montagem da base:**
- Períodos de férias gozadas (excluídos do salário mensal).
- Faltas não justificadas (deduzidas proporcionalmente).

**Inclusões automáticas:**
- 13º Salário (adicionado ao mês de dezembro ou desligamento).

**Ajuste manual necessário:**
- Férias gozadas pagas no contracheque de outro mês: acrescentar o valor de férias + 1/3 à coluna `Salários Pagos (Histórico)` da ocorrência do mês em que foram pagas.

### Alíquotas do Segurado Empregado (tabela progressiva)

| Faixa Salarial | Alíquota |
|---|---|
| Até R$ 1.412,00 | 7,5% |
| De R$ 1.412,01 a R$ 2.666,68 | 9% |
| De R$ 2.666,69 a R$ 4.000,03 | 12% |
| De R$ 4.000,04 a R$ 7.786,02 | 14% |

> Valores de referência (2024). O sistema usa a tabela histórica cadastrada, atualizada pelo Gestor Nacional.

---

## Relação entre FGTS e CS na Automação

Para garantir que as bases estejam corretas:

1. **Histórico Salarial:** marcar corretamente os checkboxes de incidência no FGTS e na CS para cada base lançada.
2. **Parâmetros da Verba:** verificar incidências de cada verba principal e reflexa.
3. **Ocorrências do FGTS:** revisar e ajustar manualmente os meses com 13º e férias.
4. **Ocorrências da CS:** revisar e ajustar manualmente os meses com férias gozadas pagas fora do período.
5. **Ordem de operações:** sempre liquidar **após** todos os ajustes manuais nas ocorrências.
