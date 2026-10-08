# Entregables y formatos

Cinco archivos bajo `docs/privacidad/`. Los tres primeros son de trabajo; los dos
últimos son los que la organización conserva.

```
docs/privacidad/
  inventario.md                    ← el más valioso a largo plazo
  auditoria/
    superficies.md                 ← F1: qué hay que revisar
    estado.json                    ← progreso, para reanudar
    hallazgos.jsonl                ← una línea por hallazgo
    informe.md                     ← para dirección y legal
    plan-remediacion.md            ← para el equipo
```

## `estado.json` — reanudar

Una auditoría de repositorio grande no cabe en una sesión. Sin este archivo, una
interrupción obliga a empezar de nuevo.

```json
{
  "proyecto": "nombre",
  "commit": "sha",
  "rama": "auditoria/privacidad-2026-08-21",
  "iniciada": "2026-08-21",
  "alcance": "repositorio completo",
  "fuera_de_alcance": ["app móvil (repo separado)", "historial anterior a 2024"],
  "dominios": {
    "D1": {"estado": "completo", "revisadas": 34, "total": 34, "hallazgos": 7},
    "D2": {"estado": "completo", "revisadas": 12, "total": 12, "hallazgos": 3},
    "D3": {"estado": "en_curso", "revisadas": 41, "total": 118, "hallazgos": 5},
    "D4": {"estado": "pendiente"}
  },
  "proximo_paso": "D3: endpoints de /api/documentos en adelante"
}
```

Actualízalo al terminar cada dominio, no al final. `proximo_paso` debe ser lo
bastante concreto para retomar sin releer todo.

## `hallazgos.jsonl` — una línea por hallazgo

JSON Lines porque se **anexa** sin releer el archivo: puedes escribir hallazgos
durante horas sin cargar en contexto los que ya escribiste.

```json
{"id":"H-014","dominio":"D3","severidad":"CRITICA","veredicto":"CONFIRMADO","titulo":"GET /api/documentos/:id no filtra por organización","ubicaciones":["src/controllers/documentos.ts:42"],"evidencia":"const doc = await Documento.findByPk(req.params.id);","escenario":"Un usuario de la empresa A cambia el id en la URL y descarga la licencia médica de un empleado de la empresa B.","datos_afectados":["SENSIBLE:salud","PERSONAL:rut","PERSONAL:nombres"],"titulares_afectados":"todos los del sistema","correccion":"Filtrar por organization_id del usuario autenticado; responder 404 ante acceso cruzado; test de acceso cruzado.","lote":"L1","estado":"abierto","revision_legal":false}
```

Campos obligatorios: `id`, `dominio`, `severidad`, `veredicto`, `titulo`,
`ubicaciones`, `evidencia`, `escenario`, `correccion`, `lote`, `estado`.

- `veredicto`: `CONFIRMADO` | `PROBABLE` | `DESCARTADO` (con `motivo_descarte`)
- `estado`: `abierto` | `corregido` | `parcial` | `bloqueado` | `descartado`
- `ubicaciones`: todas las del mismo problema — agrupa, no multipliques
- `evidencia`: el fragmento real, **enmascarado si contiene datos**

> **Nunca pongas valores reales** de datos personales en la evidencia. Un RUT o un
> diagnóstico de ejemplo tomado de la base convierte el informe en una brecha.
> Enmascara: `12345***-*`, `<diagnóstico>`.

## `informe.md` — para dirección y legal

Audiencia no técnica. Abre con lo que más importa; la metodología va al final o no va.

```markdown
# Auditoría de protección de datos — <proyecto>
> <fecha> · rama <rama> · commit <sha>
> Alcance: <qué se revisó> · Fuera de alcance: <qué no, y por qué>

## Resumen

<Tres a cinco frases. Si hay un CRÍTICO, va en la primera.
 Qué datos trata el sistema, cuál es la exposición principal,
 qué requiere atención antes del 1 de diciembre de 2026.>

**Nivel de riesgo: CRÍTICO / ALTO / MEDIO / BAJO**

| Severidad | Confirmados | Probables |
|---|---|---|
| CRÍTICA | | |
| ALTA | | |
| MEDIA | | |
| BAJA | | |

## Qué datos trata este sistema

<Resumen del inventario, en lenguaje llano. Destaca los sensibles y los de NNA.
 Esta sección suele ser una revelación para la dirección.>

## Hallazgos críticos y altos

<Uno por bloque: qué pasa, a quién afecta, cómo se corrige, cuánto cuesta.
 Sin jerga. El escenario de explotación en una frase.>

## Lo que requiere decisión legal

<Lista de REVISIÓN LEGAL REQUERIDA. Cada uno con la decisión concreta.
 No son hallazgos técnicos: son preguntas que alguien debe responder.>

## Lo que requiere decisión de negocio

<Períodos de retención, qué se deja de recolectar, si se cambia de proveedor.>

## Cobertura

| Dominio | Revisado | Total | % |
|---|---|---|---|

<Y qué quedó sin revisar. Un límite declarado es información.>

## Nota de alcance

Esta auditoría evalúa **controles técnicos**. No constituye asesoría legal ni una
declaración de cumplimiento de la Ley 21.719; esa conclusión requiere revisión
profesional. El marco legal aplicado y su fecha de verificación están en
`marco-legal.md` del skill utilizado.
```

Esa nota final no es formalidad: es lo que impide que el informe se cite como
certificado de cumplimiento en una reunión donde nadie leyó la letra chica.

## `plan-remediacion.md` — para el equipo

```markdown
# Plan de remediación
> Generado <fecha> · <N> hallazgos en <M> lotes

## L0 — Contención (inmediato)
| # | Hallazgo | Ubicación | Acción | Estado |
|---|---|---|---|---|
| H-002 | Clave de API de SendGrid versionada | .env:12, historial | **Rotar**, luego mover a variable de entorno | ⬜ |

## L1 — Aislamiento y autorización
> ⚠ Requiere test previo por hallazgo. Puede romper flujos legítimos.

| # | Hallazgo | Ubicación | Acción | Esfuerzo | Estado |
|---|---|---|---|---|---|

<... L2 a L7 ...>

## Bloqueados
| # | Hallazgo | Bloqueado por | Quién decide |
|---|---|---|---|
```

Estimación de esfuerzo en `S` / `M` / `L`, no en horas: una cifra en horas se lee
como compromiso y no lo es.

## `inventario.md`

Formato en `plantillas.md` del skill hermano, sección 4. Es el entregable que
sobrevive a la auditoría: se actualiza en cada PR de ahí en adelante, y es de donde
sale la respuesta a una solicitud de acceso o a una fiscalización.

Para muchos equipos vale más que la lista de hallazgos —los hallazgos se corrigen y
se olvidan; el inventario se usa cada semana.

## Higiene de los entregables

- **Ningún dato personal real** en ningún archivo de auditoría. Ni de ejemplo.
- Todo enmascarado, incluidos los fragmentos de log y las filas de muestra.
- Si el informe describe una exposición ya ocurrida, adviértelo arriba: pasa a
  gestión de incidentes y probablemente no debería circular por los canales
  habituales.
- Commitea los entregables en la rama de auditoría, no en la principal, hasta que
  el equipo decida qué se publica.
