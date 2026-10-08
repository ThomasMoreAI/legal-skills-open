# F3 — Verificación adversarial

Los patrones de detección de la F2 producen falsos positivos **por diseño**: buscan
la ausencia de un control, y el control puede estar en otra capa. Si reportas todo
lo que el grep encontró, el equipo descarta el informe entero al tercer falso
positivo — incluidos los tres CRÍTICOS reales que estaban dentro.

Esta fase es lo que separa una auditoría de una lista de coincidencias.

## El método

Por cada hallazgo candidato, **intenta refutarlo**. La postura por defecto es
"probablemente hay una explicación"; solo si no la encuentras, el hallazgo sube.

Cuatro preguntas, en orden:

```
1. ¿Existe un control en otra capa?
   middleware global · guard de clase o de módulo · política de fila (RLS)
   scope por defecto del ORM · proxy o WAF · validación en el gateway

2. ¿Este código está vivo?
   ¿lo importa alguien? ¿la ruta está registrada? ¿es un test, un seed,
   un ejemplo, código muerto, una migración antigua?

3. ¿El dato es realmente personal?
   `user_id` de un usuario interno del sistema no es lo mismo que del titular.
   `name` puede ser el nombre de un producto. Ábrelo y verifica.

4. ¿Es alcanzable?
   ¿un usuario externo puede llegar a esa ruta, o solo un job interno
   detrás de la red privada?
```

**Refutar cuesta abrir el archivo.** No verifiques leyendo el resultado del grep:
lee el contexto, sigue el import, busca dónde se registra el middleware. Un
hallazgo verificado sin abrir código no está verificado.

## Los tres veredictos

| Veredicto | Cuándo | Qué hacer |
|---|---|---|
| `CONFIRMADO` | Viste la ausencia del control y la ruta alcanzable | Va al informe |
| `PROBABLE` | No pudiste descartarlo, pero tampoco confirmarlo | Va al informe, con la duda escrita |
| `DESCARTADO` | Encontraste el control o el código está muerto | No va al informe |

Ante duda genuina: `PROBABLE` con la duda explícita, **nunca** `CONFIRMADO` de más.
Un `PROBABLE` bien redactado —"no encontré middleware de tenant en esta ruta; puede
existir un guard global que no localicé"— es honesto y útil. Un `CONFIRMADO` falso
destruye el informe.

Deja constancia de los `DESCARTADO` en `hallazgos.jsonl` con su motivo. Sirve para
dos cosas: que nadie vuelva a levantarlos en la próxima auditoría, y que se note
que el barrido pasó por ahí.

## Catálogo de falsos positivos

Los más frecuentes, con su forma de descarte.

### Autorización y tenant

| Detección | Cómo se descarta |
|---|---|
| `findByPk(req.params.id)` sin filtro | Buscar un guard, un `@UseGuards`, un middleware en el router padre, o RLS en la base. En Rails, un `default_scope`; en Laravel, un `Global Scope`; en Prisma, una extensión de cliente |
| Ruta sin middleware de auth aparente | El middleware puede aplicarse al router completo (`app.use('/api', auth)`) o por decorador de clase. Revisa el registro del router |
| `tenant_id` en el body | Puede usarse solo para validar contra el del token, no para filtrar. Lee qué hace con él |

### Salidas

| Detección | Cómo se descarta |
|---|---|
| `res.json(usuario)` | El modelo puede tener `toJSON()`, `@Exclude()`, `hidden`, `serializer` o `select` que ya recorta. Verifica la definición |
| Asignación masiva | El ORM puede tener `fillable`/`guarded`, o un DTO con validación estricta antes |
| Búsqueda sin paginación | Puede haber un límite por defecto en el ORM o en el gateway |

### Registro

| Detección | Cómo se descarta |
|---|---|
| `logger.info({ user })` | Puede haber un serializador con redacción configurado en el logger (pino `redact`, winston format). Revisa la configuración |
| Sentry sin `beforeSend` | Puede estar en un archivo de inicialización distinto, o venir del SDK del framework |

### Datos

| Detección | Cómo se descarta |
|---|---|
| Campo `nombre` marcado como PII | Puede ser nombre de producto, de rol, de archivo. Abre el modelo |
| Campo `plan` como socioeconómico | Puede ser plan de suscripción, no plan de salud. Verifica el dominio |
| `email` en un job de campañas | Puede ser correo transaccional bajo base contractual, no marketing |

## Lo que no es falso positivo

No descartes por estas razones — son las racionalizaciones habituales:

- "Es código antiguo" → sigue desplegado.
- "Solo los administradores pueden llegar ahí" → sigue siendo acceso sin control
  sobre datos sensibles, y los administradores también filtran.
- "Está detrás de una VPN" → mitiga, no elimina; bájale severidad y **anótalo**.
- "El equipo ya lo sabe" → si no está corregido, es un hallazgo.
- "Nunca ha pasado nada" → no es un control.
- "Es un caso teórico" → si puedes escribir el escenario concreto de explotación,
  no es teórico. Si no puedes escribirlo, entonces sí descártalo.

## Prueba de exposición

Antes de marcar `CONFIRMADO`, escribe en una línea **cómo se explota**:

```
Un usuario autenticado de la empresa A cambia el id en
GET /api/documentos/812 y recibe la licencia médica de un empleado
de la empresa B.
```

Si no puedes escribir esa frase con actores y datos concretos, el hallazgo es
`PROBABLE` o no existe. Esta frase va al campo `escenario` del hallazgo y es lo que
hace que el equipo lo entienda en cinco segundos.

## Agrupación

Cincuenta ocurrencias del mismo problema son **un hallazgo con cincuenta
ocurrencias**, no cincuenta hallazgos. Agrupa cuando la causa y el arreglo son los
mismos, y lista las ubicaciones dentro del hallazgo.

Excepción: si una ocurrencia tiene severidad mayor que las demás —la misma falta de
DTO, pero una expone datos de salud— sepárala y déjala con su severidad propia.

## Segunda opinión

Cuando la auditoría sea de alto riesgo o el repositorio grande, verifica con un
subagente independiente: entrégale el hallazgo y el código, **pídele que lo
refute**, y acepta el hallazgo solo si no lo consigue. Un verificador con el
encargo explícito de refutar encuentra lo que uno con el encargo de confirmar no ve.

Los hallazgos CRÍTICOS merecen esa segunda opinión siempre: son los que van a
detonar trabajo urgente, y un CRÍTICO falso cuesta la credibilidad de todo el resto.
