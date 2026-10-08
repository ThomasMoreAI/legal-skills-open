# Patrones de extracción de citas jurídicas

## Jurisprudencia española

### Tribunal Supremo
- Patrón: `(STS|ATS)\s+(núm\.?\s*)?(\d+/\d{4}|\d{4})?\s*(de\s+)?(\d{1,2}\s+de\s+\w+\s+de\s+\d{4})?`
- Ejemplos válidos:
  - "STS 1234/2024, de 15 de marzo"
  - "STS de 15 de marzo de 2024"
  - "ATS 567/2023"
- Datos a extraer: número de recurso, fecha, sala (si aparece), ponente (si aparece)

### Tribunal Constitucional
- Patrón: `(STC|ATC)\s+(\d+/\d{4})`
- Ejemplos:
  - "STC 124/2023"
  - "ATC 45/2024, de 12 de febrero"

### Audiencia Nacional, TSJ, AP
- Patrones similares al TS con prefijos SAN, STSJ, SAP
- TSJ requiere identificar Comunidad Autónoma cuando aparece
- AP requiere identificar provincia/sección cuando aparece

## Jurisprudencia europea

### TJUE
- Patrón: `(STJUE|Sentencia\s+del\s+TJUE).*[Aa]sunto\s+C-\d+/\d{2,4}`
- Ejemplos:
  - "STJUE de 5 de junio de 2018, asunto C-673/16"
  - "Sentencia del Tribunal de Justicia, asunto C-311/18 (Schrems II)"

### TEDH
- Patrón: similar, con prefijo STEDH o referencia al asunto Vs. Estado

## Normativa estatal

### Ley
- Patrón: `(Ley|L)\s+(Orgánica\s+)?(\d+/\d{4})`
- Ejemplos: "Ley 40/2015", "Ley Orgánica 3/2018"

### Real Decreto / Real Decreto-Ley
- Patrón: `(RD|RDL|Real\s+Decreto(-[Ll]ey)?)\s+(\d+/\d{4})`

### Artículo concreto
- Patrón: `(art\.?|artículo)\s+(\d+(?:\.\d+)?(?:\.[a-z])?)\s+(?:de\s+(?:la|el)\s+)?(.+?)(?=[,.;]|$)`
- IMPORTANTE: para verificación de vigencia hay que extraer el artículo concreto + redacción específica si el escrito la transcribe

## Normativa europea

### Reglamento
- Patrón: `Reglamento\s+\(UE\)\s+\d{4}/\d+`
- Ejemplo: "Reglamento (UE) 2016/679" (RGPD)

### Directiva
- Patrón: `Directiva\s+\d{4}/\d+/(UE|CE)`

## Doctrina académica

- Patrón heurístico: apellidos seguidos de:
  - obra entre comillas o cursiva
  - "p." o "pp." con número
  - año de publicación
  - editorial reconocida (Aranzadi, Tirant, Civitas, Marcial Pons, etc.)
- Esto es más impreciso; pasar al sub-agente de doctrina cualquier candidato que cumpla al menos tres de los cuatro elementos.

## Doctrina administrativa

- Consultas vinculantes DGT: patrón `V\d{4}-\d{2}` o referencia explícita
- Resoluciones AEPD, CNMV, CNMC: por número de procedimiento o fecha

## Heurística general

Si una expresión PARECE cita pero no encaja en ningún patrón:
- Marcarla como candidata.
- Pasarla al sub-agente más probable según contexto.
- Si nadie la reconoce, listarla en informe como "cita no estructurada, revisión humana recomendada".

NUNCA descartar silenciosamente una posible cita por no encajar en patrón conocido.
