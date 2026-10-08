# Derechos del titular y ciclo de vida del dato

Los derechos del titular no son una pantalla de configuración: son una propiedad
del esquema. Si la base de datos no permite *localizar todo lo de una persona*,
ningún formulario arregla eso después.

## Los seis derechos y su traducción técnica

| Derecho | Qué debe poder hacer el sistema | Falla habitual |
|---|---|---|
| **Acceso** | Reunir todo lo asociado a una persona, en todas las tablas, archivos y logs | Datos dispersos sin clave común; copias en sistemas satélite |
| **Rectificación** | Corregir y propagar la corrección a derivados y caches | Se corrige el maestro y quedan reportes y snapshots con el valor viejo |
| **Supresión** | Eliminar o anonimizar de forma efectiva | `deleted_at` que no borra nada |
| **Oposición** | Detener un tratamiento específico sin destruir la cuenta | Todo o nada |
| **Bloqueo** | Suspender el tratamiento conservando el dato | No existe estado intermedio |
| **Portabilidad** | Entregar en formato estructurado y reutilizable | Solo se ofrece un PDF |

Existe un plazo legal de respuesta; no lo cites de memoria (ver `marco-legal.md`).
Lo que sí puedes afirmar como ingeniería: es corto en relación con el trabajo
manual que implica. Un proceso que exige a un ingeniero escribir consultas a mano
no lo cumple. Automatízalo o, al menos, deja el procedimiento documentado en
`docs/privacidad/`.

### Bloqueo y portabilidad

Son los dos que casi nunca están soportados y por eso merecen atención específica.

**Bloqueo** requiere un estado distinto de "activo" y de "eliminado". Modela el
ciclo de vida explícitamente en vez de acumular banderas:

```
estado_titular: ACTIVO | BLOQUEADO | ANONIMIZADO | ELIMINADO
```

Cada estado con semántica escrita: qué se puede leer, qué se puede procesar, si
aparece en búsquedas, si entra en reportes, si recibe comunicaciones. Un
`deleted_at`, un `is_active` y un `blocked` conviviendo sin definición es una
fuente garantizada de tratamiento indebido.

**Portabilidad** exige formato estructurado y reutilizable —JSON, CSV, ZIP— cuando
la finalidad es portar. Un PDF sirve para leer, no para portar. La exportación
misma es una operación sensible: autenticada, autorizada, auditada y limitada en
frecuencia.

## Prueba de diseño

Antes de dar por buena una arquitectura, respóndelas con una consulta concreta,
no con una intuición:

1. ¿Puedo listar **todo** lo de una persona? Incluye tablas satélite, archivos en
   almacenamiento, colas, caches, índices de búsqueda, backups y logs.
2. ¿Puedo **eliminarlo** sin romper integridad referencial ni perder agregados
   legítimos?
3. ¿Puedo **bloquear** sin eliminar?
4. ¿Puedo **exportarlo** en formato reutilizable?
5. ¿Puedo decir **qué se hizo** con esos datos y quién los vio?

Si alguna respuesta es no, es un hallazgo de severidad MEDIA como mínimo —y ALTA
si hay datos sensibles de por medio.

## Eliminación

Borrar la fila principal casi nunca elimina los datos personales. Trata la
eliminación como un proceso, no como un `DELETE`.

```
solicitud de eliminación
      ↓
verificación de identidad del solicitante
      ↓
descubrimiento: dónde está realmente ese titular
      ↓
verificación de retención: ¿alguna norma obliga a conservar algo?
      ↓
ejecución: eliminar / anonimizar / bloquear, según el caso
      ↓
propagación a terceros y encargados que recibieron el dato
      ↓
registro en auditoría (sin volver a copiar el dato eliminado)
```

Dónde queda el rastro que se olvida: archivos adjuntos, avatares, exportaciones
generadas, correos enviados con datos incrustados, índices de búsqueda, caches,
colas de mensajes, réplicas de lectura, data warehouse, herramientas de soporte y
CRM, y logs de aplicación.

### Retención puede vencer a eliminación

Algunas obligaciones exigen conservar. Cuando ocurre, la salida correcta no es
eliminar ni ignorar la solicitud: es **bloquear** el dato —conservado, no
tratado— y explicarlo. Si no puedes nombrar la norma que obliga a conservar,
entonces no hay obligación: `REVISIÓN LEGAL REQUERIDA` para confirmarlo.

## Anonimización y seudonimización

No son sinónimos y confundirlas produce falsos cumplimientos.

```
SEUDONIMIZACIÓN   reversible con información adicional.
                  Sigue siendo dato personal. Sigue bajo la ley.
                  Ej.: reemplazar el RUT por un token con tabla de equivalencia.

ANONIMIZACIÓN     irreversible por medios razonables.
                  Deja de ser dato personal.
                  Ej.: agregación con umbral mínimo de grupo, supresión de
                       cuasi-identificadores, adición de ruido.
```

No llames anonimización a algo que se revierte con un `JOIN`. Prueba de humo:
hashear el RUT **no** es anonimizar —el espacio de RUT es enumerable y el hash se
revierte por fuerza bruta en minutos.

Cuidado con los cuasi-identificadores: comuna + fecha de nacimiento + sexo
reidentifica a una fracción sustantiva de la población, y en comunas pequeñas
bastan dos.

Usa un criterio verificable en vez de contar columnas: exige un **k mínimo
declarado** —cada combinación de cuasi-identificadores debe corresponder a al menos
`k` personas del conjunto, con `k` fijado explícitamente (5 es un piso habitual)—.
Si no puedes calcular ese `k`, no afirmes que el conjunto está anonimizado.

## Retención

Todo dato personal necesita una política declarada. Sin ella, el valor efectivo es
"para siempre", y eso es un hallazgo.

```
categoria_dato        p. ej. datos de contacto de clientes
finalidad             para qué se conservan
periodo_retencion     18 meses desde la última interacción
fundamento            contractual | legal | interés legítimo documentado
accion_al_vencer      ELIMINAR | ANONIMIZAR | ARCHIVAR | BLOQUEAR
responsable           quién ejecuta
```

Regístralo en `docs/privacidad/inventario.md` y, cuando sea posible, impleméntalo
como job programado. Una política escrita que nadie ejecuta no protege a nadie.

Preguntas que la definen: ¿por qué este período y no otro? ¿desde qué evento se
cuenta —creación, última interacción, término de contrato? ¿qué pasa con los
derivados (reportes, agregados, exportaciones)?

## Backups

La eliminación choca con los backups y conviene ser honesto al respecto.

Documenta: período de retención de backups, si están cifrados, procedimiento de
restauración, y qué ocurre con un dato eliminado que reaparece al restaurar.

**No prometas eliminación instantánea de copias técnicas si la arquitectura no
puede garantizarla.** La postura defendible es: el dato se elimina de los sistemas
activos de inmediato; los backups expiran en su ciclo normal, están cifrados y
tienen acceso restringido; y si se restaura un backup, existe un procedimiento que
vuelve a aplicar las eliminaciones pendientes. Si ese procedimiento no existe,
créalo o repórtalo como hallazgo.

## Auditoría de accesos

Sin registro de accesos no se puede responder un derecho de acceso completo ni
dimensionar una brecha. Registra las operaciones sensibles:

```
actor_id, actor_rol        quién
accion                     LOGIN, LOGIN_FALLIDO, VER_DATO_SENSIBLE,
                           EXPORTAR_DATOS, DESCARGAR_DOCUMENTO,
                           CAMBIAR_PERMISO, ELIMINAR_TITULAR
recurso, recurso_id        sobre qué
tenant_id                  en qué contexto
timestamp, ip, user_agent  cuándo y desde dónde
resultado                  PERMITIDO | DENEGADO
```

Dos reglas que se olvidan:

1. **El log de auditoría no guarda el dato sensible.** Registra que se accedió al
   diagnóstico, no el diagnóstico. De lo contrario creaste una segunda base de
   datos sensible, con menos controles que la primera.
2. **Debe ser inmutable en la práctica.** Usuarios y administradores funcionales no
   deben poder editar el histórico. Según el riesgo: append-only, almacenamiento
   inmutable, o destino externo.

## Logs de aplicación

Distintos del log de auditoría, y la fuente de fuga más frecuente porque nadie los
considera una base de datos —aunque lo sean, replicada en cada agregador.

Nunca deben contener: contraseñas, tokens, cookies, cabeceras de autorización,
RUT completo, datos de salud, datos socioeconómicos, números de tarjeta,
contenido de documentos personales, ni cuerpos de request de formularios con PII.

Implementa la sanitización como middleware con lista de campos prohibidos, no como
disciplina individual. Enmascara: `12345***-*`, `ana***@***.cl`, `****`.

Y revisa el mismo criterio en telemetría y monitoreo de errores: ver
`terceros-y-ia.md`.
