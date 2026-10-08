# Entidades Jurídicas Brasileiras — Referência para NER

## Tribunais e Órgãos

### Justiça Estadual
- TJSP, TJRJ, TJMG, TJRS, TJPR, TJSC, TJBA, TJPE, TJCE, TJGO, TJDF, TJES, TJMA, TJPA, TJPB, TJPI, TJRN, TJSE, TJAL, TJAM, TJAP, TJMT, TJMS, TJRO, TJRR, TJTO, TJAC

### Justiça Federal
- TRF1 (Brasília), TRF2 (Rio), TRF3 (São Paulo), TRF4 (Porto Alegre), TRF5 (Recife), TRF6 (Belo Horizonte)

### Tribunais Superiores
- STF (Supremo Tribunal Federal)
- STJ (Superior Tribunal de Justiça)
- TST (Tribunal Superior do Trabalho)
- TSE (Tribunal Superior Eleitoral)
- STM (Superior Tribunal Militar)

### Justiça do Trabalho
- TRT1 a TRT24 (por região)

### Órgãos
- CNJ (Conselho Nacional de Justiça)
- CNMP (Conselho Nacional do Ministério Público)
- DPE / DPU (Defensoria Pública)
- MPE / MPF (Ministério Público)
- OAB (Ordem dos Advogados do Brasil)
- AGU (Advocacia-Geral da União)
- PGE (Procuradoria-Geral do Estado)
- PGR (Procuradoria-Geral da República)

## Sistemas Eletrônicos

- PJe (Processo Judicial Eletrônico) — CNJ
- e-SAJ — TJs de SP, SC, AM, BA, CE, MS, etc.
- PROJUDI — TJs de PR, GO, etc.
- e-Proc — TRF4
- SEEU — Execução penal unificada
- TUCUJURIS — TJAP
- THEMIS — TJRS

## Legislação Principal (Patterns)

### Códigos
- CC / Código Civil (Lei 10.406/2002)
- CPC / Código de Processo Civil (Lei 13.105/2015)
- CP / Código Penal (Decreto-Lei 2.848/1940)
- CPP / Código de Processo Penal (Decreto-Lei 3.689/1941)
- CDC / Código de Defesa do Consumidor (Lei 8.078/1990)
- CLT / Consolidação das Leis do Trabalho (Decreto-Lei 5.452/1943)
- CTN / Código Tributário Nacional (Lei 5.172/1966)
- ECA / Estatuto da Criança e do Adolescente (Lei 8.069/1990)
- CF / Constituição Federal (1988)

### Citação Patterns (regex)
```
Art\.\s*\d+[\w§°,\s]*(?:do|da|dos|das)?\s*(?:CF|CC|CPC|CP|CPP|CDC|CLT|CTN|ECA|Lei\s+[\d.]+/\d{4})
§\s*\d+[°º]?\s*(?:do|da)?\s*[Aa]rt\.\s*\d+
[Ii]nciso\s+[IVXLCDM]+\s*(?:do|da)?\s*[Aa]rt\.\s*\d+
[Aa]línea\s+[a-z]\s*(?:do|da)?\s*[Aa]rt\.\s*\d+
Súmula\s+(?:Vinculante\s+)?\d+\s*(?:do|da)?\s*(?:STF|STJ|TST)
```

### Jurisprudência Patterns (regex)
```
(?:REsp|RE|AI|AgInt|AgRg|HC|MS|RMS|RHC|Rcl|ADI|ADC|ADPF|IF)\s*(?:n[°º.]?\s*)?\d[\d./\-]+
(?:Apelação|Agravo|Embargos|Recurso)\s+(?:Cível|Criminal)?\s*(?:n[°º.]?\s*)?\d[\d./\-]+
```

## Classes Processuais (CNJ — Tabela Unificada)

### Processo de Conhecimento
- Ação Civil Pública
- Ação Popular
- Mandado de Segurança
- Habeas Corpus
- Habeas Data
- Procedimento Comum Cível
- Procedimento do Juizado Especial Cível
- Ação de Alimentos
- Ação de Divórcio
- Inventário
- Ação Trabalhista

### Processo de Execução
- Execução de Título Extrajudicial
- Execução de Título Judicial
- Execução Fiscal
- Cumprimento de Sentença

### Processo Cautelar / Tutela
- Tutela Antecipada Antecedente
- Tutela Cautelar Antecedente
- Produção Antecipada de Provas

## Qualificações de Partes

### Polo Ativo
- Autor, Requerente, Impetrante, Reclamante, Exequente, Embargante, Apelante, Agravante, Recorrente

### Polo Passivo
- Réu, Requerido, Impetrado, Reclamado, Executado, Embargado, Apelado, Agravado, Recorrido

### Terceiros
- Assistente, Litisconsorte, Amicus Curiae, Opoente, Chamado ao Processo, Denunciado à Lide
