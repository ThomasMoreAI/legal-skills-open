# Diario — 2026-08-05: URLs rotas y preparación de la extracción de descriptores (TAREA-070, TAREA-071)

## Fuentes con URL rota (TAREA-070)

Tres de las cuatro localizadas y verificadas por contenido:

- **`FTE-045`** y **`FTE-048`**: el BOC abandonó la numeración por boletín (`001.html`,
  `005.html`) y pasó a numeración anual. Los anuncios están en
  `/boc/2026/046/751.html` y `/boc/2025/107/2005.html`.
- **`FTE-049`**: la ruta del portal desapareció, pero la Resolución conjunta 73/2025 sigue
  publicada como PDF y su primera página confirma el título.

Las tres pasan a `Activa` y `confirmado-fuente-primaria`, con fecha de consulta 2026-08-05.

**`FTE-051` sigue pendiente.** Declara una «Resolución de 20 de junio de 2025, IOF Escuelas
Infantiles» que no aparece en el portal. Lo que sí hay es la Resolución Conjunta n.º 24/2024, de
16 de julio, sobre el Primer Ciclo de Educación Infantil: **otro documento**. No se dan por
equivalentes. `url_oficial` apunta provisionalmente a la página de normativa clasificada de la
Inspección, que sí resuelve, y la fuente queda en `Pendiente de verificación`.

## Descriptores operativos: por qué no se han extraído (TAREA-071)

El plan era ejecutar `TAREA-066` a `TAREA-069` y volcar los descriptores operativos en las 32
fichas parciales. El texto oficial del Decreto 30/2023 está en local, y el patrón del bloque
competencial es inequívoco:

```
Competencia específica
N. <enunciado oficial>
Descriptores operativos de las
competencias clave. Perfil de salida
<códigos>
Criterios de evaluación
```

Se escribió el extractor y se validó contra las 18 fichas de ESO que ya tenían descriptores,
como conjunto de control. Salieron 75 coincidencias exactas de 101 competencias.

Al investigar las discrepancias apareció que **la causa no era el extractor**.

### Los descriptores varían por curso

La misma competencia específica tiene descriptores distintos según el curso. En Biología y
Geología, competencia 2:

| Curso | Texto oficial |
| --- | --- |
| 1.º ESO | CCL3, CD1, CD2, CD4, CPSAA4 |
| 3.º ESO | CCL3, STEM4, CD1, CD2, CD3, CD4, CD5, CPSAA4 |
| 4.º ESO | CCL3, STEM4, CD1, CD2, CD3, CD4, CD5, CPSAA4 |

El modelo guarda una lista plana por competencia. No puede representarlo.

### Y las fichas dadas por completas tienen errores

Comparando `CUR-001` con el texto oficial, solo la primera de sus seis competencias coincide
exactamente. En la competencia 5, donde los tres cursos coinciden en la fuente, la ficha declara
`CC2` —que no aparece— y omite `CPSAA1` —que sí—.

De las 18 fichas `completado`, 8 declaran varios cursos. De las 32 `parcial`, ninguna declara
`cursos`, así que ni siquiera se sabe a qué curso referir la extracción.

### Decisión

No se aplica la extracción. Volcar ahora habría consolidado el mismo defecto en 32 fichas más y
añadido datos normativos que no reproducen la fuente, contra R1. `PREG-008` recoge la evidencia
y `TAREA-066` a `TAREA-069` pasan a `Bloqueada`, conservando el trabajo de preparación para
quien las retome.

Es un resultado peor de lo previsto y mejor de lo que parece: la alternativa era 32 fichas más
con datos que no se sostienen contra la fuente.

## IDs consumidos

`TAREA-070`, `TAREA-071`, `PREG-008`.

## Pendiente

- `PREG-008`: decidir cómo se modela la dimensión de curso y qué se hace con las 18 fichas ya
  marcadas `completado`.
- `TAREA-070`: localizar la resolución exacta de `FTE-051`.
