# Rubrica de Scoring de Risco Litigioso

## Dimensão 1: Risco Processual (0-10)

| Fator | Peso | Critério Alto Risco (0-3) | Critério Médio (4-6) | Critério Baixo Risco (7-10) |
|---|---|---|---|---|
| Prazos | 30% | Prazo vencido identificado | Prazos em curso, < 3 dias restantes | Todos os prazos cumpridos ou com margem |
| Nulidades | 25% | Nulidade absoluta detectada (citação, competência) | Nulidade relativa possível | Nenhuma nulidade identificada |
| Peças faltantes | 20% | Peça essencial ausente (contestação sem justa causa) | Peça secundária ausente | Todas as peças esperadas presentes |
| Pressupostos | 15% | Ilegitimidade ou falta de interesse | Questão de competência | Pressupostos regulares |
| Integridade doc. | 10% | OCR confidence < 0.5, lacunas críticas | OCR 0.5-0.7, anomalias menores | OCR > 0.7, sem anomalias |

## Dimensão 2: Indicadores de Mérito (0-10)

| Fator | Peso | Favorável ao Autor (7-10) | Neutro (4-6) | Favorável ao Réu (0-3) |
|---|---|---|---|---|
| Provas documentais | 25% | Documentos contundentes, não impugnados | Documentos parciais, contestados | Sem prova documental relevante |
| Provas testemunhais | 15% | Testemunhas consistentes, corroboram fatos | Testemunhas divergentes | Sem testemunhas ou contraditórias |
| Prova pericial | 20% | Laudo favorável, sem impugnação eficaz | Laudo parcial ou impugnado | Laudo desfavorável ou ausente |
| Jurisprudência | 25% | Precedentes vinculantes favoráveis | Jurisprudência dividida | Precedentes contra |
| Contradições | 15% | Contradições exploráveis no polo adverso | Ambos os polos têm contradições | Contradições no próprio polo |

## Dimensão 3: Exposição Monetária

| Cenário | Cálculo |
|---|---|
| Otimista (para autor) | Valor integral dos pedidos + correção + juros |
| Realista | Média entre o concedido em sentença/acórdão (se houver) e o pleiteado |
| Pessimista (para autor) | Valor mínimo reconhecido + custas + honorários de sucumbência |
| Custas estimadas | 1-2% do valor da causa (estadual) ou tabela TRF (federal) |
| Honorários sucumbência | 10-20% do valor da condenação (CPC Art. 85 §2º) |

## Score Composto

```
risk_level = weighted_average(processual * 0.3, mérito * 0.5, monetário_normalizado * 0.2)

ALTO:   score < 4.0
MÉDIO:  4.0 ≤ score < 7.0
BAIXO:  score ≥ 7.0
```

Nota: scores são do ponto de vista do polo ativo (autor). Para avaliar risco do polo passivo, inverter.
