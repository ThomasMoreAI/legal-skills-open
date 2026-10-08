# Histórico Salarial — Regras de Lançamento

---

## Conceito

O Histórico Salarial armazena as **bases de cálculo** utilizadas nas verbas, no FGTS e na Contribuição Social. Cada "base" é um histórico independente (ex.: "Salário", "Adicional Noturno Pago", "Salário Devido").

O sistema pode criar automaticamente um histórico com base na **Última Remuneração** informada nos Parâmetros do Cálculo. Nesse caso, o histórico terá incidência na CS marcada por padrão.

---

## Tipos de Base

| Tipo | Quando usar |
|---|---|
| Informado | Valores fixos ou variáveis informados mês a mês |
| Calculado | Valor calculado automaticamente com base no Salário Mínimo ou Piso Salarial |

---

## Regras de Lançamento

### Regra 1 — Valor Integral do Mês

Sempre lançar o valor **integral** do mês, mesmo que o trabalhador tenha trabalhado apenas parte do mês. O sistema proporcionaliza automaticamente conforme:
- Faltas não justificadas.
- Período de férias gozadas.
- Meses de admissão e demissão (proporcional).

**Exceção:** Para bases variáveis pagas pelo número de horas (ex.: Adicional Noturno, HE), informar o valor **efetivamente pago** no contracheque.

### Regra 2 — Incidência no FGTS e na CS

Marcar os checkboxes de incidência conforme a natureza da base:
- **Incidência no FGTS:** marcar para bases que compõem a base do FGTS (salário, adicionais, HE).
- **Incidência na CS:** marcar para bases que compõem a base da Contribuição Social.

**Atenção:** Para meses de Salário Retido (não pago), desmarcar ambos os checkboxes nas ocorrências desses meses.

### Regra 3 — Múltiplos Históricos

Lançar um histórico separado para cada natureza de remuneração:
- "Salário Pago" (com incidência CS) — para diferença salarial.
- "Salário Devido" (sem incidência CS) — base do valor devido.
- "Adicional Noturno Pago" (com incidência CS) — para apurar diferença.

### Regra 4 — Gerar Ocorrências

Após preencher os campos do histórico, clicar em **Gerar Ocorrências** antes de salvar. O sistema cria uma linha para cada competência no período informado.

### Regra 5 — Grade de Ocorrências

Usar a **Grade de Ocorrências** para editar todos os históricos simultaneamente. Útil para:
- Ajustar valores de meses específicos.
- Verificar se os valores estão corretos antes de liquidar.

---

## Campos da Grade de Ocorrências

| Coluna | Descrição |
|---|---|
| Competência | Mês/ano da ocorrência |
| Valor Base | Valor informado para a competência |
| Incidência FGTS | Checkbox por competência |
| Incidência CS | Checkbox por competência |
| FGTS Recolhido | Valor já recolhido (para abater) |
| CS Recolhida | Valor já recolhido (para abater) |

---

## Situações Especiais

### Férias Gozadas Pagas no Contracheque

Quando as férias gozadas + 1/3 foram pagas no contracheque de um determinado mês:
1. O sistema **exclui** o período de férias do salário mensal automaticamente.
2. O usuário deve **acrescentar** o valor de férias + 1/3 à coluna `Salários Pagos (Histórico)` na página de Ocorrências da CS para o mês em que foram pagas.

### 13º Salário Pago Durante o Contrato

O sistema não inclui automaticamente o 13º na base do FGTS. O usuário deve:
1. Acessar FGTS → Ocorrências.
2. Acrescentar o valor do 13º pago à base do mês de dezembro (ou do mês do desligamento).

### Reajustes Salariais

Para cada período de reajuste, lançar uma nova faixa no mesmo histórico:
- Competência Inicial: primeiro mês do novo salário.
- Competência Final: último mês antes do próximo reajuste (ou data da demissão).
- Valor: novo salário.

Clicar em **Adicionar** para cada faixa, depois **Gerar Ocorrências** e **Salvar**.

---

## Erros Comuns no Histórico Salarial

| Erro | Causa | Solução |
|---|---|---|
| FGTS zerado | Histórico sem "incidência no FGTS" | Marcar checkbox e regerar FGTS |
| CS zerada | Histórico sem "incidência na CS" | Marcar checkbox e regerar CS |
| Verba com base errada | Parâmetros da Verba apontando para histórico incorreto | Alterar Base de Cálculo nos Parâmetros da Verba |
| Ocorrências não geradas | Esqueceu de clicar em "Gerar Ocorrências" | Clicar em Gerar Ocorrências antes de Salvar |
| Valores duplicados | Dois históricos com a mesma natureza e incidência | Revisar e consolidar históricos redundantes |
