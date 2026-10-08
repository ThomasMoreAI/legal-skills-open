# Plantillas — hallazgo, severidades, Privacy Review, inventario

Cuatro formatos que usa este skill en el trabajo del día a día. El skill
hermano `auditoria-ley-21719` tiene los suyos propios para barridos completos
(`hallazgos.jsonl`, `informe.md`) en su propio `references/entregables.md` —
no los mezcles: son audiencias y volúmenes distintos.

## 1. Formato de hallazgo

Para un hallazgo puntual, encontrado revisando un modelo, un endpoint o un PR.
No necesita el aparato de `hallazgos.jsonl` (pensado para cientos de hallazgos
por auditoría); esto es una sola nota, autocontenida:

```markdown
**[SEVERIDAD] Título corto del problema**

Ubicación: `archivo:línea`
Dato afectado: clasificación (PERSONAL / SENSIBLE:categoría / NNA)
Escenario: cómo se explota o qué falla, en una frase con actores concretos.
Corrección: qué cambio lo resuelve.
```

Ejemplo real:

```markdown
**[CRÍTICA] Endpoint de documentos no filtra por organización**

Ubicación: `src/controllers/documentos.ts:42`
Dato afectado: SENSIBLE:salud (licencias médicas adjuntas)
Escenario: un usuario autenticado de la empresa A cambia el id en
GET /api/documentos/812 y descarga la licencia médica de un empleado
de la empresa B.
Corrección: filtrar por organization_id del usuario autenticado;
responder 404 ante acceso cruzado; test de acceso cruzado.
```

La frase de escenario es obligatoria, no decorativa: si no puedes escribirla
con actores y datos concretos, el hallazgo es dudoso — revísalo de nuevo antes
de reportarlo.

**Nunca pongas valores reales** de datos personales en la evidencia, ni de
ejemplo. Enmascara: `12345***-*`, `<diagnóstico>`, `ana***@***.cl`.

## 2. Severidades

Mismo criterio en todo el skill, para que un CRÍTICA en una revisión de
endpoint signifique lo mismo que un CRÍTICA en una auditoría completa.

| Severidad | Criterio |
|---|---|
| **CRÍTICA** | Exposición efectiva o inminente de datos sensibles o de NNA a quien no debería verlos; secreto activo versionado; tratamiento de datos sensibles sin base de licitud identificable |
| **ALTA** | Falla de autorización o minimización sobre datos personales; consentimiento inválido o no verificable; ausencia de mecanismo para un derecho del titular; transferencia no identificada |
| **MEDIA** | Falta documentación (finalidad, retención, base de licitud) sin exposición directa; falla que requiere una condición adicional para explotarse |
| **BAJA** | Mejora de higiene sin riesgo directo identificado; deuda de documentación |

Reglas de ajuste:

- **Sube un nivel** si el dato involucrado es sensible o de NNA, incluso si la
  falla en sí es genérica (p. ej., una falta de paginación se ve MEDIA en un
  listado de productos y ALTA en un listado de pacientes).
- **Baja un nivel, y anótalo explícitamente**, si existe una mitigación real
  que reduce pero no elimina el riesgo (p. ej., el endpoint solo es alcanzable
  desde una red interna). No lo descartes: documenta la mitigación y la
  severidad ajustada.
- Ante duda genuina entre dos niveles, usa el más alto y dilo: "podría ser
  MEDIA si existe un control que no localicé" es información útil; subirlo
  sin decirlo no lo es.

## 3. Formato de Privacy Review (para el PR)

Cuando un cambio pasó el triaje con algún dato `PERSONAL` o superior, cierra la
revisión con esto en la descripción del PR (el checklist completo de origen
está en `revisiones.md`, sección C):

```markdown
## Privacy Review — Ley 21.719

Datos personales nuevos: sí / no
Clasificación: INTERNO / PERSONAL / SENSIBLE:<categoría> / NNA
Base de licitud: <cuál, o REVISIÓN LEGAL REQUERIDA>
Finalidad documentada: sí / no
Minimización aplicada: sí / no
Autorización verificada en backend: sí / no / n.a.
Retención definida: <período> / REVISIÓN LEGAL REQUERIDA
Terceros / transferencia internacional: <cuáles, o "ninguno">
Derechos del titular siguen ejercibles: sí / no
Inventario actualizado: sí / no

Hallazgos abiertos: <ninguno, o enlace a los hallazgos con su severidad>
```

No lo redactes desde cero cada vez: cópialo, complétalo, y deja en blanco lo
que no aplique explicando por qué — un campo vacío sin explicación se lee como
que no se revisó.

## 4. Formato de `docs/privacidad/inventario.md`

El entregable que sobrevive a cualquier revisión puntual: se actualiza en cada
PR que toque datos personales, y es de donde sale la respuesta a una solicitud
de acceso o a una fiscalización. Vale más a largo plazo que cualquier lista de
hallazgos — los hallazgos se corrigen y se olvidan, el inventario se consulta
cada semana.

```markdown
# Inventario de datos personales — <proyecto>
> Última actualización: <fecha> · Mantenido por: equipo de desarrollo

## Datos tratados

| Campo | Tabla/sistema | Clasificación | Finalidad | Base de licitud | Retención |
|---|---|---|---|---|---|
| email | usuarios.email | PERSONAL | autenticación y contacto | contrato | mientras la cuenta esté activa + 18 meses |
| diagnostico | pacientes.diagnostico | SENSIBLE:salud | atención clínica | consentimiento expreso | ver política clínica, REVISIÓN LEGAL REQUERIDA |

## Datos de NNA

<Si el sistema trata datos de menores: qué datos, cómo se acredita la
 representación legal, y si hay autorizaciones por finalidad separadas.
 Si no trata datos de NNA, dilo explícitamente — es información, no un
 casillero vacío.>

## Terceros y transferencias

<Tabla o lista según el formato de `terceros-y-ia.md`: proveedor, propósito,
 región, respaldo de transferencia.>

## Bases de licitud registradas

<Tabla o lista según el formato de `bases-y-consentimiento.md`: tratamiento,
 base, evidencia.>

## Ejercicio de derechos

<Cómo se ejerce cada derecho hoy: proceso, quién lo atiende, plazo objetivo.
 Marca los que no tienen soporte implementado.>

## Pendientes

<Lista de REVISIÓN LEGAL REQUERIDA y de brechas conocidas, con quién las
 sigue.>
```

Higiene del inventario, igual que en cualquier entregable de este skill:
**ningún dato personal real**, ni de ejemplo — solo nombres de campo y
categorías. Un inventario con valores reales es, él mismo, una base de datos
sensible con menos control de acceso que el original.
