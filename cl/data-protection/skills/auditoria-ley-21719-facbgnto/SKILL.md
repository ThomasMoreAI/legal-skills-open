---
name: auditoria-ley-21719-facbgnto
title: Auditoría de cumplimiento — Ley 21.719 (Chile)
description: Audita una aplicación completa contra la Ley 19.628 modificada por la Ley 21.719 (Chile) y remedia los hallazgos por lotes aprobados. Úsalo para auditar privacidad, revisar un repositorio completo, evaluar cumplimiento antes del 1 de diciembre de 2026, o levantar el inventario de datos personales — p. ej. "revisa toda la app", "cuánto nos falta para cumplir", "audita punto por punto la 21.719". No lo uses para un cambio puntual ni un PR (usa chile-datos-personales), construir la infraestructura que falte (usa implementar-ley-21719), responder a una brecha en curso (usa incidente-datos-personales), un resumen ejecutivo en porcentaje (usa preparacion-ley-21719), ni para redactar documentos legales de cara al titular (usa generar-politicas-privacidad).
author: facbgnto
author_url: https://github.com/facbgnto/Chile-data-protection-21719/tree/main/skills/auditoria-ley-21719
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: data-protection
language: es
sources:
- title: Barrido
  path: references/barrido.md
- title: Dominios
  path: references/dominios.md
- title: Entregables
  path: references/entregables.md
- title: Remediacion
  path: references/remediacion.md
- title: Verificacion
  path: references/verificacion.md
---

# Auditoría de cumplimiento — Ley 21.719 (Chile)

Barrido completo de un repositorio contra la ley chilena de datos personales, con
evidencia verificable y remediación controlada. Produce un informe defendible ante
un tercero, no una lista de impresiones.

Dos reglas que gobiernan todo lo demás:

1. **Sin evidencia no hay hallazgo.** Todo hallazgo cita `archivo:línea` y el
   fragmento real. Si no puedes señalar el código, no lo reportes: una auditoría con
   hallazgos inventados es peor que ninguna, porque quema la confianza del equipo en
   todas las demás.
2. **Auditar y corregir son fases separadas por una compuerta.** Las fases 1–4 son
   de **solo lectura**. No modificas una línea hasta que el usuario apruebe qué
   corregir.

## Relación con los otros skills

`chile-datos-personales` (mismo plugin) es para el día a día: un cambio, un PR, una
funcionalidad. Este es el barrido completo. Comparten el marco legal —este skill
**no** redefine la ley, la lee de:

```
${CLAUDE_PLUGIN_ROOT}/skills/chile-datos-personales/references/
    marco-legal.md              vigencia, definiciones, sanciones, reverificación
    clasificacion-datos.md      catálogo de datos y particularidades chilenas
    bases-y-consentimiento.md   bases de licitud, consentimiento, NNA
    derechos-y-ciclo-de-vida.md derechos, retención, eliminación, anonimización
    terceros-y-ia.md            proveedores, transferencias, IA, telemetría
    plantillas.md               formato de hallazgo y severidades
```

Léelos cuando necesites el criterio legal. Aquí está el **método de auditoría**.

Los controles de seguridad genéricos se delegan a `facbgnto-security-review` y
`security-storage`. Este skill audita el subconjunto cuya falla **expone datos
personales**; si esos skills están disponibles, invócalos en paralelo y cita sus
hallazgos en la sección correspondiente del informe.

Los otros cuatro skills del plugin entran en momentos distintos del ciclo:

- `implementar-ley-21719` — cuando la compuerta F5 se aprueba y lo que falta no
  es un parche puntual sino infraestructura completa (no existe forma de
  responder un derecho ARCO+, no hay `auditService`, no hay registro de
  consentimiento por finalidad). F6/L6 de este skill corrige lo que ya existe;
  `implementar-ley-21719` construye lo que no existe, con la arquitectura
  estándar de `shared/arquitectura/`.
- `incidente-datos-personales` — cuando un hallazgo deja de ser "esto podría
  exponer datos" y pasa a "esto ya expuso datos". Ver la sección final de este
  archivo.
- `preparacion-ley-21719` — cuando lo que se necesita no es el informe
  detallado por hallazgo sino un resumen ejecutivo de una vista: tabla de
  categorías con ✅/⚠️/❌ y un porcentaje de preparación técnica. Consume
  `hallazgos.jsonl` y `informe.md` de esta auditoría como su fuente
  principal — no vuelve a auditar desde cero.
- `generar-politicas-privacidad` — cuando el objetivo deja de ser encontrar
  o medir y pasa a ser redactar el texto público (política de privacidad,
  avisos, consentimientos). El inventario y el RAT que produce D1 de esta
  auditoría son su fuente principal de evidencia.

## Antes de empezar

Confirma con el usuario, en una sola pregunta:

- **Alcance**: ¿repositorio completo, o un subconjunto (un servicio, un módulo)?
- **Accesos disponibles**: ¿hay base de datos de desarrollo inspeccionable? ¿acceso
  al historial de git? ¿a la infraestructura?
- **Profundidad**: barrido rápido (dominios 1–5) o auditoría completa (1–10).

Si trabajas sin supervisión, asume repositorio completo, solo lo que esté en disco,
auditoría completa — y dilo al inicio del informe.

Crea la rama de trabajo antes de tocar nada: `auditoria/privacidad-<fecha>`.

## Fases

```
F1 Barrido      →  F2 Auditoría  →  F3 Verificación  →  F4 Informe
   (superficies)    (10 dominios)    (refutar)           (+ backlog)
                                                            ↓
                                                    ╔═══════════════╗
                                                    ║  APROBACIÓN   ║
                                                    ╚═══════════════╝
                                                            ↓
                                        F6 Remediación  ←  F5 Plan por lotes
                                           (por lotes)
```

### F1 — Barrido de superficies

**No explores libremente: enumera.** Una auditoría que "recorre el código" deja
huecos que nadie puede identificar después. Construye primero la lista completa de
superficies, y esa lista es tu unidad de cobertura.

Sigue `references/barrido.md`, que trae los comandos y patrones por stack. Produce
`docs/privacidad/auditoria/superficies.md` con:

```
modelos/tablas          N          endpoints              N
formularios de entrada  N          exportaciones/reportes N
integraciones externas  N          jobs y procesos batch  N
puntos de logging       N          manejo de archivos     N
```

Al final del barrido, declara explícitamente **qué quedó fuera de alcance y por
qué**. Un límite declarado es información; un límite silencioso es un hueco que
alguien va a descubrir en el peor momento.

### F2 — Auditoría por dominio

Diez dominios, cada uno con su método de detección en `references/dominios.md`:

| # | Dominio | Qué busca |
|---|---|---|
| 1 | Inventario de datos | qué datos personales existen realmente |
| 2 | Bases de licitud y consentimiento | por qué se tratan |
| 3 | Exposición y autorización | quién puede verlos (tenant, IDOR, auth) |
| 4 | Salidas y minimización | qué sale en respuestas, exportaciones, búsquedas |
| 5 | Terceros, transferencias e IA | a dónde salen del sistema |
| 6 | Registro: logs y telemetría | dónde se copian sin que nadie lo decida |
| 7 | Ciclo de vida | retención, eliminación, anonimización, backups, ambientes |
| 8 | Derechos del titular | si el esquema permite ejercerlos |
| 9 | Infraestructura, secretos e historial | configuración, regiones, secretos versionados |
| 10 | Sensibles y NNA | transversal, prioridad máxima |

Recorre en orden. **Escribe cada hallazgo a disco apenas lo confirmes**, en
`docs/privacidad/auditoria/hallazgos.jsonl` (una línea JSON por hallazgo, formato en
`references/entregables.md`). No acumules hallazgos en memoria: una auditoría de
repositorio grande excede el contexto, y lo que no está en disco se pierde.

Actualiza `docs/privacidad/auditoria/estado.json` al terminar cada dominio. Si la
sesión se corta, retomas desde ahí en vez de empezar de nuevo.

Los dominios 1 y 10 alimentan además `docs/privacidad/inventario.md`, que es un
entregable por sí mismo: para muchos equipos, tener el inventario es más valioso
que la lista de hallazgos.

### F3 — Verificación adversarial

**El paso que separa una auditoría útil de una lista de ruido.** Los patrones de
detección producen falsos positivos por diseño; reportarlos todos hace que el equipo
descarte el informe completo.

Para cada hallazgo, intenta **refutarlo** antes de confirmarlo:

- ¿Existe un control en otra capa que ya lo mitiga? Middleware global, política de
  fila en la base de datos, guard heredado, filtro en el ORM, proxy que lo bloquea.
- ¿El código está realmente en uso, o es muerto, un ejemplo, un test, un seed?
- ¿El dato es realmente personal, o parece serlo por el nombre del campo?
- ¿La ruta es alcanzable por un usuario, o solo por un proceso interno?

Marca cada hallazgo como `CONFIRMADO` (viste el control ausente) o `PROBABLE` (no
pudiste descartarlo) y **descarta el resto**. Ante duda genuina, `PROBABLE` con la
duda escrita, nunca `CONFIRMADO` de más.

Ver `references/verificacion.md`, que incluye el catálogo de falsos positivos
frecuentes con su forma de descarte.

### F4 — Informe y backlog

Dos documentos con audiencias distintas —no los mezcles:

- `docs/privacidad/auditoria/informe.md` — para dirección y legal: nivel de riesgo,
  qué datos trata el sistema, exposición principal, qué falta para el 1 de diciembre
  de 2026, qué requiere decisión legal.
- `docs/privacidad/auditoria/plan-remediacion.md` — para el equipo: hallazgos
  agrupados en lotes ejecutables, con esfuerzo y orden.

Formatos en `references/entregables.md`.

El informe abre con las **tres cosas que más importan**, no con la metodología.
Si hay un hallazgo CRÍTICO, va en la primera línea.

### F5 — Compuerta de aprobación

**Detente aquí.** Presenta los lotes y pide aprobación explícita de cuáles ejecutar.
No continúes por iniciativa propia, aunque el arreglo parezca obvio: un cambio en
autorización puede romper un flujo legítimo que la auditoría no vio.

Excepción única: si encuentras **secretos activos versionados** o **datos personales
accesibles sin autenticación en producción**, díselo al usuario de inmediato,
apenas lo detectes, sin esperar al informe. Eso no es un hallazgo de auditoría: es
un incidente en curso — cambia al skill `incidente-datos-personales` para
contenerlo antes de seguir auditando.

Si trabajas sin supervisión, **no remedies**. Deja el plan listo y dilo.

### F6 — Remediación por lotes

Un lote = un tipo de arreglo = un commit. Nunca mezcles tipos: un commit que
sanitiza logs y además cambia autorización es irrevisable e irreversible.

Orden en `references/remediacion.md`, con las recetas concretas. Resumen:

```
L0  contención        secretos, endpoints abiertos       inmediato
L1  aislamiento       tenant, IDOR, autorización         alto riesgo → tests primero
L2  minimización      DTOs, mass assignment              medio
L3  registro          logs, telemetría, monitoreo        bajo riesgo
L4  ciclo de vida     retención, borrado, anonimización  requiere decisiones
L5  licitud           consentimiento, bases              requiere decisiones
L6  derechos          acceso, portabilidad, bloqueo      requiere desarrollo
L7  documentación     inventario, anotaciones            sin riesgo
```

L4, L5 y L6 son, casi siempre, el punto donde este skill entrega el trabajo a
`implementar-ley-21719`: no son parches sobre código existente, son
infraestructura que hay que construir desde `shared/arquitectura/`. Preséntalo
como una fase aparte al usuario en vez de intentar resolverlo dentro de un lote
de remediación.

Por cada lote: escribe primero un test que falle demostrando el problema, aplica el
arreglo, verifica que el test pase y que la suite existente siga pasando, y haz un
commit descriptivo que referencie el id del hallazgo. Si no hay suite de tests,
dilo: es en sí mismo un hallazgo, y significa que cada arreglo es más riesgoso.

Actualiza el estado de cada hallazgo en `hallazgos.jsonl` a medida que avanzas.

### F7 — Cierre

Vuelve a correr las detecciones de los dominios remediados y confirma que los
hallazgos ya no aparecen. Actualiza el informe con lo corregido, lo pendiente y lo
que quedó bloqueado por decisión legal o de producto.

## Qué no debe hacer esta auditoría

- **No emitir conclusiones jurídicas.** "Este sistema cumple la Ley 21.719" no es una
  frase que puedas escribir. Puedes decir qué controles técnicos existen y cuáles
  faltan; la conclusión de cumplimiento la firma un abogado. Usa
  `REVISIÓN LEGAL REQUERIDA` para cada decisión normativa.
- **No inflar el conteo.** Cincuenta hallazgos BAJOS con tres CRÍTICOS enterrados
  entre ellos es un informe que falla en su único trabajo. Agrupa lo repetitivo en un
  hallazgo con N ocurrencias.
- **No exfiltrar datos.** Si inspeccionas una base de datos, trabaja con conteos,
  tipos y patrones. **Nunca copies valores reales al informe** —ni de ejemplo—: un
  informe de privacidad que contiene datos personales reales es, él mismo, una
  brecha. Enmascara siempre.
- **No tocar producción.** Solo lectura sobre cualquier entorno con datos reales.
- **No reescribir la aplicación.** El objetivo es cerrar brechas dentro de la
  arquitectura existente, no proponer una nueva.

## Si la auditoría revela exposición ya ocurrida

Si el hallazgo indica que datos personales **ya fueron expuestos** —no que podrían
serlo—, cambia de modo: deja de auditar, informa de inmediato, y pasa al skill
`incidente-datos-personales`, que tiene el runbook completo (contener, preservar
evidencia, dimensionar, evaluar riesgo, notificar). Lo que este skill reúne antes
de entregar:

```
qué datos · de cuántos titulares · en qué ventana de tiempo
cómo se detectó · si hay evidencia de acceso efectivo · estado de contención
```

Si el sistema no tiene auditoría de accesos y por eso no puedes responder "de
cuántos titulares", esa incapacidad es un hallazgo CRÍTICO por sí sola: un sistema
que no puede dimensionar una brecha tampoco puede notificarla.
