# F5–F6 — Plan y remediación por lotes

Solo se entra aquí **después de la aprobación explícita del usuario**. Si trabajas
sin supervisión, deja el plan listo y detente.

## Por qué lotes

Un lote = un tipo de arreglo = un commit = una decisión de revertir. Un commit que
sanitiza logs y además cambia autorización es irrevisable: si algo se rompe, hay que
revertir las dos cosas y se pierde el arreglo bueno junto con el malo.

## Orden de los lotes

El orden no es por severidad, sino por **riesgo de romper algo** cruzado con
urgencia. Lo urgente y peligroso primero, con tests; lo inocuo al final.

### L0 — Contención (inmediato, antes que todo)

Secretos versionados, almacenamiento público con documentos personales, endpoints
con datos personales sin autenticación.

Esto no espera aprobación de lote: se avisa al usuario apenas se detecta. Y el
arreglo no es del repositorio:

```
1. Rotar la credencial. Un secreto en el historial está comprometido
   aunque hoy no aparezca en el árbol: alguien pudo clonar el repo.
2. Recién después, quitarlo del código y llevarlo a variables de entorno.
3. Agregar el patrón a .gitignore.
4. Evaluar reescritura del historial — decisión del equipo, no tuya:
   rompe clones y forks existentes.
```

> **Quitar el secreto del código sin rotarlo no arregla nada** y crea la ilusión de
> que sí. Si el equipo solo puede hacer una cosa, que sea rotar.

### L1 — Aislamiento y autorización (alto riesgo de romper)

Tenant, IDOR, autorización a nivel de objeto. Son los CRÍTICOS, y también los que
más fácilmente rompen un flujo legítimo que la auditoría no vio.

**Nunca los apliques sin test previo.** El orden es:

```
1. Escribe un test que falle: usuario A accede al recurso de B y hoy recibe 200.
2. Aplica el filtro.
3. El test ahora espera 404 (no 403 — 403 confirma que el recurso existe).
4. Corre la suite completa. Si algo se rompe, probablemente había un flujo
   legítimo cruzando tenants: eso es información, no un error del arreglo.
   Repórtalo antes de forzar.
```

Receta base, con la forma del ORM que corresponda:

```js
// antes
const doc = await Documento.findByPk(req.params.id);

// después
const doc = await Documento.findOne({
  where: { id: req.params.id, tenantId: req.user.tenantId },
});
if (!doc) return res.status(404).end();   // 404, no 403
```

Prefiere el arreglo **estructural** al puntual cuando el problema se repite: un
scope por defecto en el ORM, una política de fila en la base, un guard en el router
padre. Cincuenta endpoints parchados a mano tendrán un cincuenta y uno sin parchar.

### L2 — Minimización de salida (riesgo medio)

DTOs, asignación masiva, campos de más en respuestas.

Rompe contratos de API: puede haber un cliente consumiendo un campo que estás
quitando. Antes de aplicar, busca los consumidores; si hay app móvil desplegada,
plantea una transición en vez de un corte.

```js
// DTO explícito por audiencia
export const UsuarioPublicoDTO = (u) => ({
  id: u.id, nombres: u.nombres, avatarUrl: u.avatarUrl,
});
```

Asignación masiva: lista blanca, siempre.

```js
const { nombres, telefono } = req.body;
await usuario.update({ nombres, telefono });
```

### L3 — Registro (bajo riesgo, alto rendimiento)

Sanitización de logs y telemetría. Rara vez rompe algo y elimina una fuga continua
— suele ser el lote con mejor relación beneficio/riesgo de toda la auditoría.

Hazlo como middleware o configuración central, nunca campo por campo en cada
llamada:

```js
// pino
const logger = pino({
  redact: {
    paths: ['req.body.password', 'req.body.rut', 'req.headers.authorization',
            'req.headers.cookie', '*.diagnostico', '*.tramoRenta'],
    censor: '****',
  },
});

// Sentry
Sentry.init({
  sendDefaultPii: false,
  beforeSend(event) {
    delete event.request?.data;
    delete event.request?.cookies;
    if (event.request?.headers) {
      delete event.request.headers.authorization;
      delete event.request.headers.cookie;
    }
    event.user = event.user?.id ? { id: event.user.id } : undefined;
    return event;
  },
});
```

Y agrega un test que falle si un campo prohibido aparece en la salida del logger.
Sin ese test, la lista de redacción se desactualiza en el primer campo nuevo.

### L4 — Ciclo de vida (requiere decisiones del negocio)

Retención, eliminación efectiva, anonimización, ambientes.

No lo ejecutes solo: cuánto tiempo conservar es una decisión de negocio y a veces
legal. Tu aporte es **preparar la infraestructura** y dejar los períodos como
parámetro:

1. Implementa el proceso de eliminación que cubre derivados (archivos, índices,
   caches, exportaciones), aunque nadie lo invoque todavía.
2. Deja la política de retención como configuración explícita, no incrustada.
3. Implementa el job de purga, desactivado, con modo de simulación que reporte
   qué eliminaría.
4. Marca los períodos como `REVISIÓN LEGAL REQUERIDA`.

Para ambientes: reemplaza el volcado de producción por generación sintética. Ese
cambio suele ser rechazado por incómodo — insiste con el argumento correcto: cada
copia multiplica la superficie de brecha y ninguna tiene los controles de la
original.

### L5 — Licitud y consentimiento (requiere decisiones)

Migrar de un booleano global a un registro por finalidad. Es una migración de datos
con implicancia legal: **no puedes inferir a qué consintió alguien** que solo marcó
"acepto los términos".

Lo defendible es: implementar el modelo nuevo, registrar los consentimientos futuros
correctamente, y marcar los existentes como `origen: migrado, finalidad: por
determinar` con `REVISIÓN LEGAL REQUERIDA`. No inventes retroactivamente un
consentimiento granular que nadie otorgó.

### L6 — Derechos del titular (desarrollo nuevo)

Acceso, portabilidad, bloqueo, eliminación. Normalmente es un proyecto propio, no un
arreglo. Entrégalo como propuesta dimensionada, no como parche.

Un orden que rinde: primero la consulta de descubrimiento (localizar todo lo de un
titular), porque de ella dependen los otros cinco derechos.

### L7 — Documentación (sin riesgo)

Inventario, anotaciones de clasificación en el esquema, registro de terceros y
transferencias. Cero riesgo técnico, y es lo que queda cuando el equipo tenga que
demostrar diligencia.

## Reglas durante la remediación

- **Un commit por lote**, con el id del hallazgo en el mensaje:
  `fix(privacidad): aísla por tenant en documentos [H-014, H-015]`
- **Corre la suite completa entre lotes**, no solo al final.
- **Si no hay tests**, dilo y trátalo como hallazgo: cada arreglo es a ciegas.
- **Actualiza `hallazgos.jsonl`** con el estado real: `corregido`, `parcial`,
  `descartado`, `bloqueado` — nunca marques corregido lo que no verificaste.
- **Si un arreglo rompe algo, no lo fuerces.** Revierte, documenta qué rompió y
  por qué, y devuélvelo al usuario. Un flujo legítimo que cruzaba tenants es un
  hallazgo de arquitectura, más grande que el que estabas arreglando.
- **No aproveches para refactorizar.** El diff debe contener solo el arreglo: si
  además reordenas imports y renombras variables, nadie puede revisarlo.

## Cierre

Vuelve a correr las detecciones de los dominios remediados y confirma que los
hallazgos ya no aparecen. Actualiza el informe con tres listas: corregido,
pendiente, y bloqueado por decisión legal o de producto.

Lo bloqueado importa tanto como lo corregido: es lo que el equipo tiene que llevar a
alguien que pueda decidir.
