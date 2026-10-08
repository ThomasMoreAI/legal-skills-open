---
name: chile-datos-personales-facbgnto
title: Privacidad desde el diseño — Ley 21.719 (Chile)
description: Aplica privacidad desde el diseño a un cambio puntual bajo la Ley 19.628 modificada por la Ley 21.719 (Chile) — un modelo o migración, un endpoint, un PR. Úsalo para revisar código nuevo, clasificar un campo, o verificar base de licitud o consentimiento — p. ej. "¿este campo es sensible?", "revisa este endpoint para privacidad". No lo uses para auditar un repositorio completo (usa auditoria-ley-21719), construir infraestructura de privacidad desde cero (usa implementar-ley-21719), responder a una brecha ya ocurrida (usa incidente-datos-personales), un resumen ejecutivo en porcentaje (usa preparacion-ley-21719), ni para redactar la política de privacidad o textos de consentimiento (usa generar-politicas-privacidad).
author: facbgnto
author_url: https://github.com/facbgnto/Chile-data-protection-21719/tree/main/skills/chile-datos-personales
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: data-protection
language: es
sources:
- title: Bases Y Consentimiento
  path: references/bases-y-consentimiento.md
- title: Clasificacion Datos
  path: references/clasificacion-datos.md
- title: Derechos Y Ciclo De Vida
  path: references/derechos-y-ciclo-de-vida.md
- title: Marco Legal
  path: references/marco-legal.md
- title: Plantillas
  path: references/plantillas.md
- title: Revisiones
  path: references/revisiones.md
- title: Terceros Y Ia
  path: references/terceros-y-ia.md
---

# Privacidad desde el diseño — Ley 21.719 (Chile)

Revisión de privacidad para un cambio concreto: rápida cuando el cambio no
toca datos de personas, exhaustiva cuando sí. El objetivo es que revisar
privacidad sea parte normal de escribir código, no un trámite aparte que el
equipo aprende a saltarse.

Dos reglas que gobiernan todo lo demás:

1. **Clasifica antes de revisar.** Un cambio que solo toca datos `INTERNO` no
   necesita Privacy Review ni entra al inventario. Recorrer todo el checklist
   en cada PR es la forma más rápida de que el equipo deje de hacerlo — la
   salida rápida existe para que la revisión completa se reserve para lo que
   de verdad la necesita.
2. **No emitas conclusiones jurídicas.** Puedes decir qué controles técnicos
   existen y cuáles faltan; si algo "cumple la ley" lo firma un abogado. Usa
   `REVISIÓN LEGAL REQUERIDA` para cada punto que dependa de una calificación
   normativa — plazos exactos, excepciones, corte etario de NNA, vías de
   transferencia internacional.

## Relación con los otros skills

`auditoria-ley-21719` (mismo plugin) es para el barrido completo de un
repositorio, con fases separadas por una compuerta de aprobación y
remediación por lotes. Este skill es para el día a día y no reemplaza esa
auditoría — úsalos juntos: lo que este skill va encontrando en el camino
alimenta la próxima auditoría, y el inventario que este skill mantiene es
insumo directo del dominio D1 de esa auditoría.

`implementar-ley-21719` construye la arquitectura estándar (servicios,
tablas, API de derechos ARCO+) que este skill exige tener antes de declarar
un cambio terminado (fase 4, condición 4 y 5 abajo). Cuando el triaje
descubre que el proyecto no tiene dónde registrar un consentimiento o una
base de licitud, la salida no es inventar un registro ad hoc para ese PR: es
proponer construir la pieza con ese skill.

`incidente-datos-personales` entra cuando lo que se encuentra en la revisión
no es un riesgo sino una exposición ya ocurrida — ver la sección F más abajo.

`preparacion-ley-21719` consume el inventario y los Privacy Review que este
skill produce como parte de su evidencia para el resumen ejecutivo en
porcentaje — no hace falta invocarlo desde aquí, pero mantener el inventario
al día es lo que hace que ese resumen sea preciso.

`generar-politicas-privacidad` consume el mismo inventario, más el RAT/ROPA
y el registro de consentimientos, para redactar la política de privacidad y
los avisos de cara al titular — la finalidad y base de licitud que este
skill exige registrar en cada PR son, literalmente, el texto que ese skill
va a citar.

Comparten el marco legal — este skill **no** lo redefine, vive en
`references/`:

```
references/
    marco-legal.md              vigencia, definiciones, sanciones, reverificación
    clasificacion-datos.md      catálogo de datos y particularidades chilenas
    bases-y-consentimiento.md   bases de licitud, consentimiento, NNA
    derechos-y-ciclo-de-vida.md derechos, retención, eliminación, anonimización
    terceros-y-ia.md            proveedores, transferencias, IA, telemetría
    plantillas.md               formato de hallazgo, severidades, Privacy Review, inventario
    revisiones.md               las seis listas de revisión (A–F)
```

Los controles de seguridad genéricos (XSS, CSRF, inyección, CSP, rate
limiting, dependencias) se delegan a `facbgnto-security-review` y
`security-storage`, si están disponibles. Este skill revisa el subconjunto
cuya falla **expone datos personales**.

## Flujo

```
Triaje  →  ¿toca datos > INTERNO?  →  no  →  fin, sin Privacy Review
              │
              sí
              ↓
        Revisión (A/B/C según qué se tocó)
              ↓
        ¿dispara evaluación de impacto?  →  sí  →  márcalo (D)
              ↓
        Antes de declarar terminado (E)
              ↓
        Privacy Review + inventario actualizado
```

### 1. Triaje

Antes de leer código en profundidad, identifica qué toca el cambio:

- ¿Agrega o modifica un campo, tabla o archivo que contenga datos de una
  persona natural?
- ¿Agrega o modifica un endpoint que lea o escriba esos datos?
- ¿Agrega una integración, un job, una exportación, o un punto de logging
  que los toque?

Clasifica cada dato involucrado con `clasificacion-datos.md`:
`INTERNO` / `PERSONAL` / `SENSIBLE:<categoría>` / con o sin `NNA`.

**Si todo lo tocado es `INTERNO`, termina aquí** y dilo explícitamente: "este
cambio no toca datos personales, no requiere Privacy Review". No generes una
revisión de privacidad para una migración que solo agrega una columna de
configuración.

Si hay algo `PERSONAL` o superior, continúa.

### 2. Revisión — checklists A, B, C

Sigue `revisiones.md`. Elige la sección según lo que se tocó — no las
recorras todas si el cambio solo tocó una cosa:

- **A — Modelo o migración**: campo por campo, clasificación, finalidad, base
  de licitud, minimización, cifrado, retención.
- **B — Endpoint**: autenticación, autorización, pertenencia (IDOR/BOLA),
  tenant, validación de entrada, asignación masiva, salida minimizada,
  auditoría, rate limit.
- **C — Checklist de PR**: la lista final que se copia a la descripción del
  PR cuando el cambio toca datos personales (formato completo en
  `plantillas.md`, sección 3).

Para cada hallazgo, usa el formato de `plantillas.md` sección 1, con severidad
de la sección 2 del mismo archivo. Un hallazgo sin la frase de escenario
concreto ("quién, qué dato, cómo") no está listo para reportarse — vuelve a
revisarlo.

Cuando el cambio involucre base de licitud o consentimiento, consulta
`bases-y-consentimiento.md`. Cuando involucre terceros, transferencias o un
modelo de IA, consulta `terceros-y-ia.md` (y registra el uso formal en
`shared/arquitectura/registro-ia.md` si el proyecto ya tiene esa tabla).
Cuando involucre retención, eliminación, anonimización o los derechos del
titular, consulta `derechos-y-ciclo-de-vida.md`.

Cuatro reglas transversales que no viven en `revisiones.md` pero aplican
igual cuando el cambio las toca: `shared/rules/autenticacion-y-sesiones.md`
(login, tokens, cookies de sesión), `shared/rules/cifrado-y-pseudonimizacion.md`
(qué técnica usar para proteger un campo sensible), `shared/rules/no-datos-en-url.md`
(cualquier dato personal en query string o path), y
`shared/rules/analytics-tracking.md` (SDKs de analítica o tracking nuevos).

### 3. Cuándo escalar (D)

Revisa la lista de disparadores de evaluación de impacto en `revisiones.md`,
sección D (biometría, scoring, decisiones automatizadas relevantes,
tratamiento masivo de NNA, uso de IA a escala, entre otros). Si alguno aplica,
no la redactes tú: identifica el disparador, descríbelo en términos técnicos,
y marca `REVISIÓN LEGAL REQUERIDA` para que el equipo la entregue a quien
corresponda.

### 4. Antes de declarar terminado (E)

Aplica a todo cambio que pasó el triaje con algún dato `PERSONAL` o superior.
Las cinco condiciones de `revisiones.md` sección E tienen que cumplirse: base
de licitud registrada, sin hallazgos CRÍTICOS ni ALTOS abiertos, derechos del
titular siguen ejercibles, retención definida, inventario actualizado.

Si alguna falla, dilo explícitamente en vez de marcar la tarea como completa:
reporta el hallazgo antes que cualquier resumen de avance, propone la
corrección mínima que desbloquea, y deja claro que la funcionalidad no debe
considerarse terminada con eso abierto.

### 5. Cierre

Actualiza `docs/privacidad/inventario.md` (formato en `plantillas.md`, sección
4) y deja el Privacy Review (sección 3 del mismo archivo) en la descripción
del PR.

## Si encuentras algo fuera del alcance del cambio (F)

Mientras revisas un endpoint vas a encontrar problemas preexistentes que no
son parte de este cambio. Repórtalos igual — no los ignores porque no están en
el ticket, y no sigas construyendo encima como si no existieran. Ver
`revisiones.md`, sección F, para el formato.

Si el hallazgo indica que **ya hubo exposición** de datos —no solo que era
posible—, deja de revisar y pasa al skill `incidente-datos-personales`: eso
deja de ser una revisión de código y pasa a ser un incidente en curso.

## Qué no debe hacer este skill

- **No emitir conclusiones jurídicas.** Ver regla 2 arriba.
- **No inflar el Privacy Review.** Un cambio que toca un solo campo `PERSONAL`
  sin complicaciones no necesita cinco párrafos: el formato de
  `plantillas.md` cabe en un bloque corto.
- **No exfiltrar datos.** Nunca copies valores reales de datos personales al
  hallazgo, al Privacy Review ni al inventario — ni de ejemplo. Enmascara
  siempre.
- **No reemplazar la auditoría completa.** Si el usuario pide revisar "toda la
  app" o "cuánto falta para cumplir", ese es el skill `auditoria-ley-21719`,
  no este.
- **No construir infraestructura desde una revisión de PR.** Si falta un
  servicio o una tabla entera, repórtalo y remite a `implementar-ley-21719`
  en vez de improvisar una versión mínima solo para ese cambio.
