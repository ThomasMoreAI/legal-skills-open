---
name: pp-triangulacion-cespial
title: pp-triangulacion — Paso 9 (F3) · Triangulación adversarial
description: 'Triangulación adversarial de datos, conclusiones y vigencia normativa de la propuesta: extrae toda afirmación cuantitativa (cifras, fechas, montos, métricas, citas normativas) y toda conclusión estratégica, y enfrenta cada una a varios escépticos independientes que intentan refutarla contra las fuentes. Verifica además que toda cita normativa esté vigente (no derogada, no modificada en lo citado, no superada por jurisprudencia) contra fuente oficial. Marca cada afirmación como confirmada, refutada o [VERIFICAR], y cada norma como vigente, modificada o derogada con fuente y fecha de consulta. Úsala tras el pulido para garantizar que ningún dato del documento sea inventado, inconsistente ni jurídicamente caduco.'
author: Cespial
author_url: https://github.com/Cespial/propuestas-secop/tree/main/skills/pp-triangulacion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: co
practice: general
language: es
---

# pp-triangulacion — Paso 9 (F3) · Triangulación adversarial

Verificación final antes del cierre. Operacionaliza el principio de **cero invención**
del PLAYBOOK §0 y los anti-patrones §8 ("inventar datos", "acumular promesas sin
sustento metodológico", "dejar `[VERIFICAR]` sin tag visual").

Doctrina: ninguna cifra, fecha, monto, cita normativa o conclusión estratégica entra
al PDF final sin sustento trazable. Lo que no se confirma contra fuente → `[VERIFICAR]`
escalado a P0. Lo que se refuta → corrección obligatoria antes del cierre. **Una norma
derogada citada como vigente es un hallazgo P0**: riesgo de credibilidad ante el
evaluador y, según el peso de la cita, riesgo de rechazo.

Lee siempre primero `references/SPEC.md` (contrato de carpetas y salidas).

## Cuándo corre

- Tras `pp-pulido` (capa 3 / editor jefe). Es el último filtro antes de `pp-cierre`.
- Recibe de `pp-pulido` el inventario de `[VERIFICAR]` de capa 3 como insumo: cada uno
  entra a esta triangulación con dueño y fecha de cierre ya asignados.

## Insumos (LEE)

- `00-estado/ESTADO.md` — fase actual, cifras canónicas declaradas, P0 abiertos.
- `04-propuesta/Propuesta_<id>.html` ensamblado + `04-propuesta/sections/*.html`.
- `02-investigacion/15_QA_EDITORIAL_CAPA3.md` — frente D (inventario `[VERIFICAR]`)
  y frente A (coherencia de cifras canónicas) de `pp-pulido`.
- `02-investigacion/00_..14_*.md` — dossiers con fuentes citadas (la base de evidencia).
  Incluye el dossier normativo (`07_..13_*` según numeración del proceso).
- `01-pliego/` — pliego, anexo técnico, adendas (fuente de verdad para montos,
  plazos, UNSPSC, equipo mínimo, criterios de evaluación, normas marco del proceso).
- `references/PLAYBOOK.md` (§0 filosofía, §7.5 cifras, §7.6 citación, §8 anti-patrones).
- `references/roster/<empresa>.md` (ficha de capacidades de la empresa que recomendó
  `pp-proponente`) y `references/perfiles-equipo.template.md` — fuente de verdad para
  datos del proponente seleccionado (NIT, RUP, EEFF, métricas de productos, perfiles).
  Si el proponente es consorcio o unión temporal, la ficha de cada empresa del roster.

## Salida (ESCRIBE)

- `02-investigacion/16_TRIANGULACION.md` — tabla maestra de verificación (tres niveles:
  datos, conclusiones, vigencia normativa).
- `00-estado/ESTADO.md` — actualización: fase, P0 nuevos (refutadas + `[VERIFICAR]` +
  normas modificadas/derogadas), próximo paso.

## Workflow que invoca

Lanza `workflows/triangulacion-adversarial.js`. El workflow:

1. **Extrae** del documento ensamblado tres inventarios separados:
   - **Datos** — toda afirmación cuantitativa: cifras, fechas, montos (COP, SMMLV),
     plazos, porcentajes, códigos UNSPSC, AIU, métricas de productos, estadísticas (α, W, IQR),
     conteos de experiencia, indicadores financieros.
   - **Conclusiones** — toda tesis, eje diferenciador y afirmación de capacidad
     ("acreditamos", "garantizamos", "nuestra experiencia demuestra", "el modelo logra").
   - **Citas normativas** — toda norma invocada: leyes, decretos, acuerdos PCSJA,
     resoluciones, circulares de Colombia Compra Eficiente, sentencias. Se extrae la cita
     literal y el fragmento citado (artículo/numeral/inciso), porque la verificación es
     sobre lo citado.
2. **Refuta** — por cada afirmación lanza varios subagentes `triangulador` (agentType,
   ver `agents/`) que NO colaboran entre sí. Cada uno intenta REFUTARLA contra las
   fuentes declaradas (dossiers `02-investigacion/`, pliego, KB). El prompt es
   adversarial: "encuentra la fuente que contradice esta afirmación o demuestra que no
   existe sustento". Prompt autocontenido (PLAYBOOK §5.3): rutas absolutas, afirmación
   literal, fuente declarada, criterio de refutación.
3. **Verifica vigencia** (nivel normativo) — por cada cita normativa un `triangulador`
   confirma vigencia contra **fuente oficial** vía `WebSearch` (ver "Nivel vigencia normativa").
4. **Veredicto por mayoría** — consolida los verdictos de los escépticos por afirmación:
   - **confirmada** — fuente verificable concuerda; cita exacta registrada.
   - **refutada** — fuente contradice el dato, o la cifra es inconsistente con su uso
     en otra sección, o no existe la fuente declarada → corrección obligatoria.
   - **`[VERIFICAR]`** — sin fuente concluyente; queda con dueño y fecha de cierre.

Empate o disenso entre escépticos → degrada a `[VERIFICAR]` (nunca asume confirmada).

```bash
# Lanzar la triangulación adversarial sobre el documento ensamblado
node "$PLUGIN/workflows/triangulacion-adversarial.js" \
  --workspace "<WORKSPACE>" \
  --doc "<WORKSPACE>/04-propuesta/Propuesta_<id>.html" \
  --verificar-in "<WORKSPACE>/02-investigacion/15_QA_EDITORIAL_CAPA3.md" \
  --out "<WORKSPACE>/02-investigacion/16_TRIANGULACION.md"
```

## Tres niveles, sin mezclar

Triangula en tres pasadas separadas (pasos 8-10 del proceso). No se promedian.

- **Nivel datos** — cada cifra/fecha/monto/cita contra su fuente atómica. Verifica
  además **coherencia interna**: la misma cifra canónica idéntica en todas sus menciones
  (presupuesto, SMMLV, universos, muestras, plazos, UNSPSC, AIU). Discrepancia entre dos
  menciones del mismo dato = refutada, aunque la fuente exista.
- **Nivel conclusiones** — cada tesis/eje/afirmación de capacidad contra su sustento
  metodológico o documental. Regla dura: **una conclusión sin sustento metodológico
  declarado es un hallazgo** (PLAYBOOK §8). No basta con que "suene cierta": debe apuntar
  a un método, un instrumento, un precedente o una fuente. Si no lo hace → refutada o
  `[VERIFICAR]`.
- **Nivel vigencia normativa** — cada cita normativa contra fuente oficial. No verifica
  si el dato existe (eso es nivel datos), sino si la norma **sigue vigente en lo citado**.

## Nivel vigencia normativa (detalle)

Toda cita normativa del documento se verifica contra **fuente oficial**, no contra
agregadores ni blogs jurídicos. Jerarquía de fuente:

- Leyes y decretos: Diario Oficial / `funcionpublica.gov.co` (Gestor Normativo) /
  `secretariasenado.gov.co` con su nota de vigencia. Para el régimen de contratación
  estatal: Decreto 1082/2015 y sus modificaciones.
- Circulares, conceptos y guías de contratación: portal de Colombia Compra Eficiente
  (`colombiacompra.gov.co`).
- Sentencias: Relatoría de la Corte Constitucional / Consejo de Estado / Corte Suprema.
- Acuerdos PCSJA y resoluciones sectoriales: portal de la entidad emisora.

Cada cita recibe uno de tres estados, **siempre con fuente oficial + fecha de consulta**:

- **vigente** — la norma y el fragmento citado siguen produciendo efectos; sin nota de
  derogatoria ni modificación sobre el artículo/numeral citado.
- **modificada** — la norma existe pero el fragmento citado fue reformado, sustituido o
  adicionado, de modo que el texto invocado ya no coincide con el vigente. Hallazgo:
  corregir la cita al texto vigente o re-anclar el argumento. **P0.**
- **derogada** — la norma (o el artículo citado) fue derogada expresa o tácitamente, o la
  tesis fue superada por jurisprudencia posterior. Citarla como vigente es **P0**:
  corrección obligatoria antes del cierre.

Reglas de la verificación:

- Verificar **el fragmento citado**, no solo la norma marco. Una ley vigente puede tener
  el artículo invocado derogado.
- Distinguir derogatoria de **inexequibilidad** (control constitucional) y de **suspensión
  provisional**: ambas se tratan como "modificada/derogada" según el alcance, con la
  providencia citada.
- Para jurisprudencia: verificar que no haya **cambio de precedente** ni unificación
  posterior que invierta la tesis citada.
- Sin fuente oficial concluyente sobre la vigencia → `[VERIFICAR]` (nunca asumir vigente).

```bash
# Patrón de búsqueda por cita (vía tool WebSearch en el subagente triangulador)
#   "Ley 1581 de 2012 vigencia derogada modificada site:funcionpublica.gov.co"
#   "Decreto 1082 de 2015 art 2.2.1.2.1.3.2 nota vigencia"
#   "Sentencia T-323 de 2024 cambio de precedente unificación"
```

## Formato de `16_TRIANGULACION.md`

Encabezado con semáforo global y conteo por nivel:
- datos: confirmadas / refutadas / `[VERIFICAR]`
- conclusiones: confirmadas / refutadas / `[VERIFICAR]`
- vigencia normativa: vigentes / modificadas / derogadas / `[VERIFICAR]`

Tabla maestra (una fila por afirmación):

```markdown
| # | Nivel | Afirmación / cita (literal + sección) | Fuente declarada | Verdicto | Evidencia (cita + ruta/URL + fecha consulta) | Acción |
|---|-------|---------------------------------------|------------------|----------|----------------------------------------------|--------|
| 1 | dato  | "COP 3.344.902.352" (s05)             | pliego §4.1      | confirmada | "...presupuesto oficial..." 01-pliego/pliego.pdf p.12 | — |
| 2 | dato  | "1.910,38 SMMLV" (s12)                | cálculo interno  | refutada  | inconsistente con s05 (montos no cuadran) | corregir s12 |
| 3 | concl | "garantizamos cobertura 100%" (s08)   | —                | [VERIFICAR] | sin método de medición declarado | owner+fecha |
| 4 | norma | "Ley 1581/2012 art. 6" (s09)          | dossier normativo | vigente   | nota de vigencia sin derogatoria, funcionpublica.gov.co, consulta 2026-05-29 | — |
| 5 | norma | "Decreto X/AAAA art. N" (s09)         | dossier normativo | derogada  | derogado por Decreto Y/AAAA art. M, Diario Oficial, consulta 2026-05-29 | corregir cita s09 / re-anclar |
```

- **Evidencia** siempre con cita textual + ruta absoluta o URL **con fecha de consulta**.
  En el nivel normativo, la URL es la fuente oficial.
- **Acción** concreta: sección exacta a corregir, o dueño + fecha de cierre del `[VERIFICAR]`.

## Escalamiento a P0

Toda fila **refutada**, **`[VERIFICAR]`**, **modificada** o **derogada** se escala a P0
en `00-estado/ESTADO.md`:

- Refutadas — corrección obligatoria en la sección antes de que `pp-cierre` genere el PDF.
- Normas **derogadas** — corrección obligatoria: eliminar la cita, sustituirla por la
  norma vigente o re-anclar el argumento. Bloquea el cierre.
- Normas **modificadas** — ajustar la cita al texto vigente del fragmento. Bloquea el cierre
  si el argumento depende del texto reformado.
- `[VERIFICAR]` — dueño y fecha de cierre; visible con su tag (anti-patrón §8: nunca
  `[VERIFICAR]` sin tag visual).

`pp-cierre` no debe correr con refutadas ni con normas derogadas/modificadas abiertas. Es
la regla de gating de esta fase: cero dato inventado, cero conclusión sin sustento, cero
cita normativa caduca en el documento final.

## Coordinación con pp-pulido

- Insumo de entrada: el inventario de `[VERIFICAR]` de capa 3 (`15_QA_EDITORIAL_CAPA3.md`,
  frente D). Esta skill lo absorbe y lo somete a refutación, no lo re-descubre.
- El frente A de `pp-pulido` (coherencia de cifras canónicas) se valida aquí de forma
  adversarial: lo que el editor jefe marcó como consistente, los escépticos intentan romper.
- Si la triangulación obliga correcciones de redacción no triviales, devolver a
  `pp-pulido`/`pp-propuesta` antes de cerrar.

## Cierre de la skill

1. Escribe `02-investigacion/16_TRIANGULACION.md` con la tabla maestra y el semáforo (tres niveles).
2. Actualiza `00-estado/ESTADO.md`: fase = "F3 · triangulación completada", lista los P0
   abiertos (refutadas + `[VERIFICAR]` + normas modificadas/derogadas), próximo paso =
   corregir P0 → `pp-cierre`.
3. Reporta al usuario (sin emojis, bullets): conteo por verdicto y nivel,
   afirmaciones refutadas con su corrección, normas derogadas/modificadas con la cita
   vigente de reemplazo, `[VERIFICAR]` pendientes con dueño y fecha.
