# Catálogo de Verbas Padrão — PJE-Calc

Verbas disponíveis no Lançamento Expresso, com seus parâmetros padrão sugeridos pelo sistema. Todos os parâmetros podem ser alterados via **Parâmetros da Verba**.

---

## Verbas Rescisórias e Mensais Comuns

| Verba | Característica | Ocorrência | Incidência FGTS | Incidência CS | Incidência IR | Observações |
|---|---|---|---|---|---|---|
| Saldo de Salário | Comum | Desligamento | Sim | Sim | Sim | Base: Histórico Salarial |
| Aviso Prévio | Aviso Prévio | Desligamento | Sim | Sim | Sim | Base: Maior Remuneração; Quantidade: Prazo do Aviso |
| Multa Art. 477 CLT | Comum | Desligamento | Não | Não | Não | Base: Maior Remuneração; Alíquota: 100% |
| 13º Salário Integral | 13º Salário | Dezembro | Sim | Sim | Sim | Quantidade: Avos |
| 13º Salário Proporcional | 13º Salário | Desligamento | Sim | Sim | Sim | Quantidade: Avos |
| Férias + 1/3 (Indenizadas) | Férias | Período Aquisitivo | Não | Não | Sim | Quantidade: Avos |
| Férias + 1/3 (Gozadas) | Férias | Período Aquisitivo | Não | Não | Sim | Período: data do gozo |
| Férias Proporcionais + 1/3 | Férias | Desligamento | Não | Não | Sim | Quantidade: Avos |
| Diferença Salarial | Comum | Mensal | Sim | Sim | Sim | Base: Salário Devido; Valor Pago: Salário Pago |
| Salário Retido | Comum | Mensal | Sim | Sim | Sim | Período: meses retidos |

---

## Adicionais

| Verba | Característica | Ocorrência | FGTS | CS | IR | Observações |
|---|---|---|---|---|---|---|
| Adicional de Periculosidade 30% | Comum | Mensal | Sim | Sim | Sim | Base: Histórico Salarial; Alíquota: 30% |
| Adicional de Insalubridade | Comum | Mensal | Sim | Sim | Sim | Grau: Mínimo 10%, Médio 20%, Máximo 40% |
| Adicional Noturno 20% | Comum | Mensal | Sim | Sim | Sim | Divisor: Carga Horária; Quantidade: horas noturnas |
| Adicional de Transferência 25% | Comum | Mensal | Sim | Sim | Sim | Base: Histórico Salarial |

---

## Horas Extras

| Verba | Adicional | FGTS | CS | IR | Observações |
|---|---|---|---|---|---|
| Horas Extras 50% | 50% | Sim | Sim | Sim | Divisor: Carga Horária; Quantidade: horas extras |
| Horas Extras 60% (noturnas) | 60% | Sim | Sim | Sim | Para HE em jornada noturna |
| Horas Extras 100% | 100% | Sim | Sim | Sim | Para HE em domingos/feriados |
| Intervalo Intrajornada | — | Sim | Sim | Sim | Quantidade: horas de intervalo suprimido |
| Intervalo Interjornadas | — | Sim | Sim | Sim | Quantidade: horas de intervalo suprimido |

---

## Verbas Reflexas Comuns

| Verba Reflexa | Sobre Verba Principal | Comportamento Padrão |
|---|---|---|
| Aviso Prévio sobre [Verba] | Qualquer principal | Média pelo Valor Absoluto |
| 13º Salário sobre [Verba] | Qualquer principal | Média pelo Valor Absoluto |
| Férias + 1/3 sobre [Verba] | Qualquer principal | Média pelo Valor Absoluto |
| RSR sobre [Verba] | HE, Adicional Noturno | Valor Mensal |
| FGTS sobre [Verba] | — | Configurado via "incidência no FGTS" nos Parâmetros da Verba |

> **Atenção:** FGTS + 40% **não** é uma verba reflexa cadastrada. É apurado automaticamente quando a verba principal tem "incidência no FGTS" marcada e a Multa do FGTS está habilitada na página FGTS.

---

## Multas Específicas

| Verba | Base | Alíquota | Observações |
|---|---|---|---|
| Multa Art. 467 CLT | Verbas rescisórias não pagas | 50% | **NÃO é verba Expresso/Manual.** Aparece como: (1) checkbox `multaDoArtigo467` na aba FGTS (sub-checkbox da Multa 40%); (2) reflexa automática sob cada verba principal na aba Verbas (ex: "MULTA DO ARTIGO 467 DA CLT SOBRE SALDO DE SALÁRIO"). Mapear via `fgts.multa_467 = true`. |
| Multa Art. 477 CLT | Maior Remuneração | 100% | Atraso no pagamento das verbas rescisórias |
| Multa Art. 479 CLT | Remuneração | 50% | Rescisão antecipada de contrato por prazo determinado |

---

## Regras de Incidência por Natureza

| Natureza da Verba | FGTS | CS | IR |
|---|---|---|---|
| Salarial (mensal) | Sim | Sim | Sim |
| Rescisória indenizatória | Não | Não | Não |
| Férias indenizadas | Não | Não | Sim |
| 13º Salário | Sim | Sim | Sim (tributação exclusiva) |
| Aviso Prévio indenizado | Sim | Sim | Não (isento) |
| Horas Extras | Sim | Sim | Sim |
| Adicional de Periculosidade | Sim | Sim | Sim |
| Adicional Noturno | Sim | Sim | Sim |
| Multas (Art. 467, 477, 479) | Não | Não | Não |
| FGTS (principal) | — | Não | Não |
| Multa do FGTS (40%) | — | Não | Não |

> Estas são as incidências **padrão sugeridas pelo sistema**. O usuário pode alterar conforme a decisão judicial.
