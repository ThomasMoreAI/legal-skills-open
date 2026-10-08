# Precedentes Vinculantes — Referência para Detecção

## Tipos de Precedentes Vinculantes no Brasil

### 1. Súmula Vinculante (STF)
- **Fundamento:** CF Art. 103-A
- **Efeito:** Vincula todos os órgãos do Poder Judiciário e Administração Pública
- **Regex:** `(?i)Súmula\s+Vinculante\s+(?:n[°º.]?\s*)?\d+`

### 2. IRDR (Incidente de Resolução de Demandas Repetitivas)
- **Fundamento:** CPC Art. 976-987
- **Efeito:** Vincula todos os juízes e tribunais na área de jurisdição
- **Regex:** `(?i)(?:Incidente\s+de\s+Resolução\s+de\s+Demandas\s+Repetitivas|IRDR)\s*(?:n[°º.]?\s*)?\d*`

### 3. IAC (Incidente de Assunção de Competência)
- **Fundamento:** CPC Art. 947
- **Efeito:** Vinculante para juízes e órgãos fracionários
- **Regex:** `(?i)(?:Incidente\s+de\s+Assunção\s+de\s+Competência|IAC)\s*(?:n[°º.]?\s*)?\d*`

### 4. Repercussão Geral (STF)
- **Fundamento:** CF Art. 102, §3º; CPC Art. 1.035
- **Efeito:** Tese vinculante para todos os tribunais
- **Regex:** `(?i)(?:Repercussão\s+Geral|Tema\s+\d+\s+(?:do\s+)?STF|RG\s+Tema\s+\d+)`

### 5. Recurso Repetitivo (STJ/STF)
- **Fundamento:** CPC Art. 1.036-1.041
- **Efeito:** Tese vinculante para tribunais e juízes
- **Regex:** `(?i)(?:Recurso\s+(?:Especial\s+)?Repetitivo|Tema\s+\d+\s+(?:do\s+)?STJ|Tema\s+\d+\s+(?:do\s+)?STF)`

## Súmulas Mais Citadas (Referência Rápida)

### STJ — Direito Civil/Consumidor
- **Súmula 479:** Instituições financeiras respondem por fortuito interno (fraudes)
- **Súmula 54:** Juros moratórios em ilícito extracontratual desde o evento danoso
- **Súmula 362:** Correção monetária do dano moral desde o arbitramento
- **Súmula 37:** Cumulação de danos morais e materiais de mesmo fato
- **Súmula 227:** PJ pode sofrer dano moral

### STJ — Processo Civil
- **Súmula 7:** Reexame de provas inviável em REsp
- **Súmula 83:** Divergência jurisprudencial superada (REsp inadmissível)
- **Súmula 568:** Relator pode dar provimento a REsp por jurisprudência dominante

### STF — Súmulas Vinculantes Frequentes
- **SV 10:** Violação da reserva de plenário (Art. 97 CF)
- **SV 11:** Uso de algemas
- **SV 25:** Depositário infiel — prisão ilícita
- **SV 56:** Execução penal — falta de vagas
