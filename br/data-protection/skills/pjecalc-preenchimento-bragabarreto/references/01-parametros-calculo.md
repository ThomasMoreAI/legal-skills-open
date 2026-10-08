# Parâmetros do Cálculo — Detalhamento Completo

A página **Parâmetros do Cálculo** é a primeira e mais importante do fluxo. Todos os demais módulos dependem das configurações aqui definidas.

---

## Campos Obrigatórios

| Campo | Formato | Instrução |
|---|---|---|
| Estado | Seleção (UF) | UF do local de prestação dos serviços |
| Município | Seleção | Município do local de prestação dos serviços (carregado após Estado) |
| Admissão | dd/mm/aaaa | Data de admissão do reclamante |
| Ajuizamento | dd/mm/aaaa | Data do ajuizamento da ação trabalhista |
| Demissão **ou** Data Final | dd/mm/aaaa | Pelo menos um dos dois é obrigatório |

---

## Campos Opcionais com Impacto Relevante

| Campo | Impacto |
|---|---|
| Data Inicial | Limita o início do período de cálculo (prescrição quinquenal manual) |
| Maior Remuneração | Usada como base do Aviso Prévio e da Multa Art. 477 CLT |
| Última Remuneração | Cria automaticamente um Histórico Salarial com incidência na CS |
| Carga Horária | Divisor padrão para cálculo de horas (padrão: 220h) |
| Comentários | Texto livre (até 255 caracteres) que aparece no Resumo do Cálculo |

---

## Parâmetros de Aviso Prévio

| Opção | Comportamento |
|---|---|
| Não Apurar | Aviso Prévio não é calculado |
| Calculado | Sistema calcula o prazo conforme Lei 12.506/2011 (30 dias + 3 dias por ano completo, máximo 90 dias) |
| Informado | Usuário informa manualmente o prazo em dias |

**Projetar Aviso Prévio Indenizado:** Quando marcado, o sistema projeta os avos de férias e 13º considerando o período do aviso prévio indenizado como trabalhado.

---

## Parâmetros de Prescrição

| Parâmetro | Comportamento |
|---|---|
| Prescrição Quinquenal | Limita as verbas ao período de 5 anos anteriores ao ajuizamento |
| Prescrição FGTS | Aplica a prescrição específica ao FGTS (30 anos antes de 2015; 5 anos após EC 72/2014) |
| Limitar Avos ao Período | Exclui avos vencidos antes da Data Inicial ou da prescrição |

---

## Parâmetros de Regime de Trabalho

| Regime | Dias de Férias |
|---|---|
| Tempo Integral | 30 dias (padrão) |
| Tempo Parcial | 18 dias (para contratos com jornada reduzida) |

---

## Parâmetros de Dias Úteis

Relevantes para verbas com divisor "Dias Úteis" (ex.: Adicional de Transferência):

| Parâmetro | Comportamento |
|---|---|
| Considerar Feriado Estadual | Inclui feriados estaduais do município selecionado na contagem de dias úteis |
| Considerar Feriado Municipal | Inclui feriados municipais do município selecionado |
| Sábado como Dia Útil | Padrão: marcado (sábado conta como dia útil) |

---

## Parâmetros de Valores

| Parâmetro | Comportamento |
|---|---|
| Zerar Valor Negativo | Zera automaticamente ocorrências com valor negativo (padrão: desmarcado) |

---

## Relação entre Campos e Módulos Dependentes

| Campo | Módulos que dependem |
|---|---|
| Admissão + Demissão | Férias (períodos aquisitivos), Verbas (período de apuração), FGTS (período) |
| Data Inicial | Verbas (limita início), FGTS (limita início), CS (limita início) |
| Data Final | Verbas com vencimento após demissão |
| Maior Remuneração | Aviso Prévio, Multa Art. 477 CLT |
| Última Remuneração | Histórico Salarial automático (incidência CS) |
| Estado + Município | Feriados estaduais/municipais, Piso Salarial |
| Carga Horária | Divisor de horas em todas as verbas |
| Prazo do Aviso Prévio | Avos de férias e 13º (se Projetar marcado) |

---

## Erros Comuns

| Erro | Causa | Solução |
|---|---|---|
| "Data de admissão posterior à demissão" | Datas invertidas | Corrigir os campos |
| "Município não encontrado" | Estado não selecionado antes do Município | Selecionar Estado primeiro e aguardar carregamento |
| Verbas com período zerado | Data Inicial posterior à Demissão | Verificar se Data Inicial está correta |
| FGTS com base zerada | Histórico Salarial sem incidência no FGTS | Marcar checkbox "incidência no FGTS" no Histórico |
| Aviso Prévio não calculado | Prazo = "Não Apurar" | Alterar para "Calculado" ou "Informado" |
