# Checklist de intake

Lista completa de datos necesarios para generar cada documento. Sirve para dos cosas: guiar la reunión de arranque con el cliente y saber qué preguntar antes de generar.

Está ordenada por bloques. Los marcados **[cliente]** hay que definirlos con el cliente; los marcados **[propio]** los decide el proveedor.

---

## Bloque A — Partes (todos los documentos)

| Variable | Qué es | Fuente |
|---|---|---|
| `PROVEEDOR_NOMBRE` | Nombre o razón social del proveedor | [propio] |
| `PROVEEDOR_CUIT` | CUIT del proveedor | [propio] |
| `PROVEEDOR_DOMICILIO` | Domicilio del proveedor | [propio] |
| `PROVEEDOR_EMAIL` | Correo para notificaciones | [propio] |
| `CLIENTE_RAZON_SOCIAL` | Razón social exacta, no nombre de fantasía | [cliente] |
| `CLIENTE_CUIT` | CUIT del cliente | [cliente] |
| `CLIENTE_DOMICILIO` | Domicilio legal | [cliente] |
| `CLIENTE_FIRMANTE` | Quién firma | [cliente] |
| `CLIENTE_FIRMANTE_CARGO` | Con qué carácter firma | [cliente] |
| `FECHA_LARGA` | Fecha de celebración, en letras | [propio] |

> Verificar que el firmante sea titular, socio gerente, presidente o apoderado. Un empleado sin poder no obliga a la sociedad. Pedir CUIT antes de redactar.

---

## Bloque B — Alcance técnico (Anexo I, contrato de implementación)

| Variable | Qué es |
|---|---|
| `DESCRIPCION_SISTEMA` | Qué hace el sistema, en dos o tres frases |
| `ALCANCE_INCLUIDO` | Lista de tareas y funcionalidades comprendidas |
| `ENTREGABLES` | Qué se entrega concretamente (flujos, documentación, accesos) |
| `INTEGRACIONES` | Canales y sistemas con los que se integra |
| `PLATAFORMAS_TERCEROS` | Servicios de terceros que usa el sistema |
| `ROLES_IA` | Roles que cumplen los modelos dentro del flujo |
| `ACCIONES_DETERMINISTICAS` | Acciones automatizadas que no dependen de un modelo |
| `METRICAS_GARANTIZADAS` | Solo lo que está bajo control operativo propio |
| `CRITERIOS_ACEPTACION` | Qué debe cumplirse para tener el sistema por entregado |
| `CRONOGRAMA` | Fases y duración estimada |
| `EXCLUSIONES_ADICIONALES` | Lo que el cliente mencionó y no se va a hacer |

Sobre `ROLES_IA` y `ACCIONES_DETERMINISTICAS`: la partición es la que sostiene la cláusula de desempeño. Los roles de IA verificables (clasificación de intención, extracción de datos, decisión del paso siguiente) quedan bajo el umbral. Las acciones determinísticas (crear registros, agendar, notificar, escribir en sistemas del cliente) no admiten umbral y deben funcionar. La redacción de respuestas queda fuera de toda medición.

Sobre `METRICAS_GARANTIZADAS`: si no hay una métrica que se pueda medir y esté bajo control propio, escribir que no se garantizan métricas específicas. Nunca comprometer facturación, ventas ni conversiones.

---

## Bloque C — Accesos (Anexo II)

| Variable | Qué es |
|---|---|
| `ACCESOS_REQUERIDOS` | Lista específica de credenciales y permisos |
| `INTERLOCUTOR_NOMBRE` | Persona con capacidad de decisión |
| `INTERLOCUTOR_EMAIL` | Su correo |

Ser específico: no "acceso al CRM" sino "usuario administrador de HubSpot con permisos de API". Esta lista es la que dispara la suspensión de plazos, así que la vaguedad juega en contra.

---

## Bloque D — Plazos y precio (implementación)

| Variable | Qué es |
|---|---|
| `PLAZO_EJECUCION` | Duración estimada total |
| `PRECIO_TOTAL` | Monto con moneda |
| `PRECIO_LETRAS` | El mismo monto en letras |
| `ESQUEMA_PAGOS` | Hitos y porcentajes |
| `MEDIO_PAGO` | Transferencia, plataforma, etc. |
| `TRATAMIENTO_IMPOSITIVO` | Según condición fiscal |
| `CLAUSULA_MONEDA` | Solo si el precio es en moneda extranjera |
| `TARIFA_HORARIA` | Para el soporte posterior a la garantía |

Si el precio está en dólares, `CLAUSULA_MONEDA` debe fijar el tipo de cambio de referencia y el momento de conversión. Si es en pesos y el proyecto se extiende, considerar un mecanismo de actualización.

---

## Bloque E — Mantenimiento (solo si contrata abono)

| Variable | Qué es |
|---|---|
| `FECHA_CONTRATO_IMPLEMENTACION` | Fecha del contrato base |
| `FECHA_INICIO_MANTENIMIENTO` | Normalmente la fecha de aceptación |
| `ABONO_MENSUAL` / `ABONO_LETRAS` | Monto del abono |
| `HORAS_INCLUIDAS` | Horas mensuales comprendidas |
| `DURACION_INICIAL` | Plazo inicial antes de la renovación automática |
| `SERVICIOS_ADICIONALES` | Lo que se agregue al alcance estándar |

---

## Bloque F — Orden de trabajo (solo intervenciones puntuales)

| Variable | Qué es |
|---|---|
| `NUMERO_OT` | Numeración correlativa |
| `FECHA_CONTRATO_IMPLEMENTACION` | Contrato al que se apoya |
| `DESCRIPCION_TAREAS` | Qué se pidió, en concreto |
| `MODALIDAD_PRECIO_OT` | Por hora o precio cerrado |
| `HORAS_ESTIMADAS` / `TOTAL_OT` | Estimación y total |
| `CONDICIONES_PAGO_OT` | Cuándo se paga |
| `PLAZO_OT` | Plazo estimado |

---

## Variables con valor por defecto

Estas ya vienen resueltas en `assets/defaults.json` y no hace falta preguntarlas salvo que el caso lo justifique: plazos procesales (accesos, silencio, inactividad, aceptación, subsanación), garantía, confidencialidad, no solicitación, interés moratorio, tope de responsabilidad, umbral de IA, mínimos facturables, y los parámetros estándar de mantenimiento (horario, tiempo de respuesta, preavisos, tope).
