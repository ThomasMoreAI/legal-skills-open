---
name: incidente-datos-personales-facbgnto
title: Respuesta a incidentes de privacidad — Ley 21.719 (Chile)
description: Runbook de respuesta cuando datos personales ya fueron o pudieron ser expuestos — una brecha detectada, un hallazgo que revela exposición ya ocurrida, un reporte externo. Úsalo ante "creemos que hubo una filtración", "un cliente reporta que vio datos de otro", "encontramos un bucket público con documentos", "hay que evaluar si esto se notifica", o cuando otro skill de este plugin encuentre exposición ya ocurrida y no solo posible. No lo uses para una auditoría preventiva (usa auditoria-ley-21719) ni para revisar un cambio antes de desplegarlo (usa chile-datos-personales) — este skill entra cuando el incidente ya está en curso o ya ocurrió, no antes.
author: facbgnto
author_url: https://github.com/facbgnto/Chile-data-protection-21719/tree/main/skills/incidente-datos-personales
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: data-protection
language: es
---

# Respuesta a incidentes de privacidad — Ley 21.719 (Chile)

La diferencia con los otros cinco skills de este plugin: ahí se audita,
revisa, construye, mide o redacta con tiempo para hacerlo bien. Aquí no —
cada hora que pasa sin contener la exposición es exposición adicional, y
cada hora sin dimensionarla es una hora menos para cumplir un eventual plazo
de notificación.

Una regla que domina sobre cualquier otra de este skill:

**Contener primero, documentar en paralelo, nunca documentar en vez de
contener.** Un informe perfecto de un incidente que sigue abierto es un
informe sobre una filtración que continuó mientras se escribía.

## Cuándo se activa este skill

```
evidencia de acceso efectivo a datos personales por quien no debía —
  no "era posible", sino "ocurrió" o hay indicio razonable de que ocurrió

un secreto activo versionado que pudo haber sido usado

un hallazgo de chile-datos-personales o auditoria-ley-21719 que revela
  exposición ya ocurrida, no solo un riesgo (ver revisiones.md sección F
  y verificacion.md del skill auditoria-ley-21719)

un reporte externo: un titular, un cliente, un investigador de seguridad
```

Si lo que hay es solo una vulnerabilidad sin evidencia de explotación, ese es
un hallazgo normal de `chile-datos-personales` o `auditoria-ley-21719` — no
actives el modo incidente para eso. La distinción importa porque el modo
incidente tiene su propio ritmo y sus propias obligaciones, y activarlo de
más le resta seriedad a cuando de verdad se necesita.

## Relación con los otros skills

Un incidente abierto, y uno cerrado recientemente sin lecciones aplicadas,
afectan el resultado de `preparacion-ley-21719` en su categoría
"Incidentes" — ver `matriz-readiness.md` de ese skill.

Si el incidente revela que un documento público (política de privacidad,
un aviso) describía el tratamiento de forma incorrecta, la corrección de
ese texto es trabajo de `generar-politicas-privacidad`, no de este
runbook — este skill se detiene en el paso 9 (corregir el sistema); no
redacta ni actualiza documentos legales.

## El runbook

```
1. Detectar
2. Contener
3. Preservar evidencia
4. Clasificar datos afectados
5. Determinar afectados
6. Evaluar riesgo
7. Notificar
8. Documentar
9. Corregir
```

Los pasos 3 y 4 pueden correr en paralelo con la contención — no son
estrictamente secuenciales, pero **la contención nunca espera** a que los
otros pasos terminen.

### 1. Detectar

Registra el momento y la fuente de detección en `privacy_incidents`
(`breachService.report`, ver `arquitectura-privacidad.md`) apenas haya
indicio razonable — no esperes confirmación completa para abrir el registro.
Se puede cerrar como falso positivo después; abrirlo tarde no se puede
corregir.

```
detectado_en, tipo, sistemas_afectados (lo que se sepa hasta ahora)
```

### 2. Contener

La acción más urgente, antes que cualquier análisis extenso:

```
credencial comprometida        rotarla YA — ver remediacion.md, lote L0,
                                del skill auditoria-ley-21719: quitarla del
                                código sin rotarla no arregla nada

endpoint expuesto sin auth      desactivar o restringir el acceso de
                                inmediato, aunque sea con una solución
                                temporal más agresiva de lo normal

almacenamiento público           bloquear el acceso público al bucket/
                                  carpeta de inmediato

acceso indebido en curso          revocar la sesión o el acceso del actor,
                                    si es identificable
```

Avisa al usuario **de inmediato** al confirmar que hay contención pendiente,
sin esperar al informe completo — esta es la misma excepción que
`auditoria-ley-21719` define en su compuerta F5 para secretos activos o
datos expuestos sin autenticación.

### 3. Preservar evidencia

Antes de "limpiar" nada:

```
- Copia de logs relevantes (accesos, errores) de la ventana del incidente,
  antes de que roten o expiren.
- Estado del sistema en el momento de la detección, si es posible sin
  interferir con la contención.
- No alteres ni borres registros que puedan ser evidencia, aunque
  contengan datos personales — enmascáralos al reportar, no al preservar.
```

Sin esto, el paso 5 (determinar afectados) puede volverse imposible de
reconstruir después.

### 4. Clasificar datos afectados

Usa `clasificacion-datos.md` (skill `chile-datos-personales`) sobre lo que
efectivamente estuvo expuesto — no sobre todo lo que el sistema comprometido
podría tocar en abstracto. La pregunta es "¿qué vio o pudo ver quien no
debía?", no "¿qué hay en esta tabla en general?".

```
categorías_datos: [...]
incluye_sensibles: sí/no — cuáles categorías del art. 2 letra g)
incluye_nna: sí/no
```

`incluye_sensibles` o `incluye_nna` en `sí` eleva la prioridad de todo lo que
sigue — la notificación a los propios titulares es especialmente exigible
cuando la brecha afecta datos sensibles, de NNA, o datos económicos/
financieros/bancarios/comerciales (ver `marco-legal.md`).

### 5. Determinar afectados

```sql
-- ejemplo: usando privacy_data_access_log para dimensionar el acceso real
-- durante la ventana del incidente
SELECT DISTINCT recurso_id
FROM privacy_data_access_log
WHERE recurso = 'documentos'
  AND ocurrido_en BETWEEN :ventana_desde AND :ventana_hasta
  AND resultado = 'PERMITIDO'
  AND actor_id NOT IN (:actores_legitimos_conocidos);
```

**Si el sistema no tiene auditoría de accesos, esta pregunta no tiene
respuesta exacta — y esa incapacidad es en sí misma un hallazgo CRÍTICO**,
no un obstáculo que se resuelve estimando a ojo. Documenta el límite:
"no es posible determinar con precisión cuántos titulares fueron afectados
porque el sistema no registraba accesos antes de esta fecha" es la respuesta
correcta, no una omisión.

Cuando no hay auditoría, la estimación conservadora (asumir el universo
completo de registros alcanzables, no el mínimo posible) es la postura
defendible mientras no haya evidencia que acote el número.

### 6. Evaluar riesgo

No es una conclusión legal — es el insumo técnico para que quien decida
tenga con qué decidir:

```
riesgo_para_titulares    ¿qué daño concreto podría seguir? (fraude,
                          discriminación, daño reputacional, riesgo físico
                          si son datos de ubicación o de NNA)
probabilidad_de_uso_indebido   ¿hay indicio de que el dato ya se usó, o
                                 solo de que fue accedido/expuesto?
factores_agravantes             sensibles, NNA, volumen, si ya hay
                                  evidencia de uso indebido
```

### 7. Notificar

**Plazos y destinatarios exactos: `REVISIÓN LEGAL REQUERIDA`.** Este skill no
decide si corresponde notificar a la Agencia o a los titulares, ni en qué
plazo — ver `marco-legal.md` para lo que sí está confirmado (deber de
reportar "por los medios más expeditos posibles y sin dilaciones indebidas"
cuando exista riesgo para los derechos y libertades de los titulares, y
notificación a titulares especialmente exigible con datos sensibles, de NNA,
o económicos/financieros/bancarios/comerciales).

Lo que este skill sí prepara, para que la decisión legal no tenga que
esperar a que alguien arme el insumo desde cero:

```
qué datos, de cuántos titulares, en qué ventana de tiempo   (pasos 4-5)
cómo se detectó
si hay evidencia de acceso efectivo, o solo de exposición posible
estado de contención
riesgo evaluado (paso 6)
```

`breachService.notify(incidentId, destinatarios)` registra que la
notificación ocurrió y a quién — no la redacta ni la envía por sí solo; el
contenido y la decisión de enviarla son de quien tiene la autoridad legal
para hacerlo.

### 8. Documentar

Un documento, no disperso en el chat de la conversación:

```markdown
# Incidente — <id> — <fecha de detección>

## Resumen
<Tres frases: qué pasó, a quién afectó, estado actual.>

## Cronología
<detectado_en · contenido_en · notificado_en (si aplica) · cerrado_en>

## Qué se expuso
<categorías de datos, cuántos titulares, ventana de tiempo>

## Causa raíz
<qué falló — técnico, sin conclusiones legales>

## Contención aplicada
<qué se hizo, cuándo>

## Determinación de afectados
<método usado, o la limitación si no había auditoría>

## Evaluación de riesgo
<ver paso 6>

## Notificación
<a quién, cuándo, o REVISIÓN LEGAL REQUERIDA si aún no se decide>

## Corrección
<ver paso 9 — enlaza a los hallazgos y al plan de remediación>
```

Guárdalo en `docs/privacidad/incidentes/<id>.md`. Mismas reglas de higiene
que cualquier entregable de este plugin: **ningún dato personal real**, todo
enmascarado.

### 9. Corregir

La causa raíz del incidente entra al flujo normal de remediación —
`remediacion.md` (skill `auditoria-ley-21719`) si es un hallazgo que se
parcha, o `implementar-ley-21719` si revela que falta infraestructura
completa (por ejemplo, el incidente ocurrió porque no existía
`auditService` y por eso no se pudo contener a tiempo).

## Matriz de responsables en incidentes SaaS/multitenant

Si la plataforma es encargada de tratamiento respecto del tenant afectado
(ver `proveedores-registro.md`), la obligación de notificar a los titulares
finales suele recaer en el tenant (responsable), con la plataforma obligada a
notificarle a él primero y sin demora. No asumas que la plataforma notifica
directamente a los titulares del tenant sin que el tenant lo sepa o decida —
`REVISIÓN LEGAL REQUERIDA` sobre el mecanismo contractual exacto.

## Qué no debe hacer este skill

- **No decidir si hay que notificar ni a quién.** Prepara el insumo,
  no la decisión.
- **No demorar la contención por documentar primero.** Ver regla inicial.
- **No estimar a la baja cuando no hay evidencia que lo justifique.** Ante
  incertidumbre sobre el alcance, la postura conservadora es la defendible.
- **No exponer más datos al documentar el incidente.** El informe del
  incidente no puede convertirse en un segundo incidente — enmascara
  siempre, sin excepción.
