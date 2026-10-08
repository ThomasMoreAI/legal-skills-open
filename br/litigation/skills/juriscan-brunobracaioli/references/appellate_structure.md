# Estrutura de Instâncias — Referência para Rastreamento

## Hierarquia Judiciária Brasileira

```
STF (Supremo Tribunal Federal)
 ↑ RE, ADPF, ADI, ADC
STJ (Superior Tribunal de Justiça)
 ↑ REsp, Recurso Ordinário
TJ (Tribunal de Justiça Estadual) / TRF (Federal) / TRT (Trabalho)
 ↑ Apelação, Agravo de Instrumento
1ª Instância (Varas / Juizados)
```

## Classificação de Instância por Peça

### 1ª Instância
- Peças: PETIÇÃO INICIAL, CONTESTAÇÃO, RÉPLICA, RECONVENÇÃO, SENTENÇA, DESPACHO, ATA DE AUDIÊNCIA, LAUDO PERICIAL, CUMPRIMENTO DE SENTENÇA, PENHORA, ALVARÁ, TUTELA, LIMINAR/CAUTELAR
- Indicadores no texto: "Vara", "Juiz de Direito", "Juiz Federal", "Juiz do Trabalho", "Foro"

### TJ / TRF / TRT (2ª Instância)
- Peças: APELAÇÃO, CONTRARRAZÕES, ACÓRDÃO, AGRAVO, EMBARGOS
- Indicadores: "Desembargador", "Des.", "Relator", "Câmara", "Turma", "Seção", "TJ", "TRF", "TRT"

### STJ
- Peças: RECURSO ESPECIAL, ACÓRDÃO (STJ), AGRAVO (STJ)
- Indicadores: "Ministro", "Min.", "Superior Tribunal de Justiça", "STJ", "Turma do STJ"

### STF
- Peças: RECURSO EXTRAORDINÁRIO, ACÓRDÃO (STF)
- Indicadores: "Supremo Tribunal Federal", "STF", "Plenário", "Turma do STF"

## Padrões de Detecção (Regex)

```
1ª Instância:  (?i)(?:Vara|Juiz(?:a)?\s+de\s+Direito|Juiz(?:a)?\s+Federal|Foro\s+(?:Central|Regional))
TJ/TRF:        (?i)(?:Des(?:embargador)?\.?\s|Câmara|Turma\s+(?:Cível|Criminal)|Tribunal\s+de\s+Justiça|TRF\d)
STJ:           (?i)(?:Min(?:istro)?\.?\s|Superior\s+Tribunal|STJ|Turma\s+do\s+STJ)
STF:           (?i)(?:Supremo\s+Tribunal|STF|Plenário|Turma\s+do\s+STF)
```

## Peças por Polo em Cada Instância

| Instância | Polo Ativo | Polo Passivo | Juízo |
|---|---|---|---|
| 1ª | Petição Inicial, Réplica, Tutela | Contestação, Reconvenção | Sentença, Despacho |
| TJ | Apelação (apelante), Memoriais | Contrarrazões (apelado) | Acórdão |
| STJ | Recurso Especial (recorrente) | Contrarrazões (recorrido) | Acórdão |
| STF | Recurso Extraordinário (recorrente) | Contrarrazões (recorrido) | Acórdão |
