# Activación precisa en sistemas

La skill debe intervenir temprano cuando sea útil, sin activarse por cualquier mención casual de Chile o seguridad.

## Regla principal

Activa el flujo completo si se cumple al menos una de estas rutas:

- **Petición directa:** el usuario pide aplicar o revisar privacidad, protección de datos o las leyes chilenas N.º 19.628 o N.º 21.719.
- **Petición tecnológica inferida:** concurren un nexo chileno y tratamiento real o razonablemente previsible de datos personales.

La segunda ruta requiere ambos elementos. Si uno es incierto, realiza sólo el cribado y declara el supuesto o formula una pregunta decisiva.

## Elemento A: nexo chileno

Son señales fuertes:

- responsable o encargado establecido o constituido en Chile;
- usuarios, trabajadores u otros titulares ubicados en Chile;
- oferta de bienes o servicios dirigida a personas en Chile, con o sin pago;
- monitoreo, análisis, rastreo, perfilamiento o predicción de personas en Chile;
- contrato o norma que someta el tratamiento a legislación chilena.

Son señales de apoyo, no concluyentes por sí solas:

- dominio `.cl`, precios en CLP o despacho dentro de Chile;
- RUT, direcciones, regiones, comunas o teléfonos chilenos;
- autenticación con ClaveÚnica u otra integración local;
- campañas o interfaz dirigidas explícitamente al público chileno.

Bajo el régimen reformado, contrasta el alcance con el artículo 1 bis. Para el régimen anterior, analiza el vínculo aplicable sin atribuirle retroactivamente ese artículo.

## Elemento B: datos personales

Existe tratamiento previsible si una función necesita o normalmente genera información vinculada o referida a una persona natural identificada o identificable.

Señales frecuentes:

- registro, inicio de sesión, perfil, recuperación de cuenta o autenticación;
- compra, pago, facturación, despacho, reserva o suscripción;
- RUT, cédula, pasaporte, nombre, correo, teléfono o dirección;
- cookies, IDs persistentes, IP vinculable, dispositivo, logs o historial;
- soporte, tickets, conversaciones, llamadas o grabaciones;
- RR. HH., postulaciones, control de asistencia o evaluaciones;
- imagen, voz, geolocalización, biometría o vigilancia;
- salud, perfil biológico, solvencia, deuda, afiliación o infracciones;
- recomendaciones, puntuaciones, inferencias, perfiles o decisiones automatizadas;
- prompts, archivos, embeddings, datasets, entrenamiento o salidas de IA asociados a personas;
- datos de producción reutilizados en pruebas, analítica o desarrollo.

No evalúes el dato aislado: considera combinaciones y medios razonablemente disponibles para identificar.

## Cribado de baja fricción

Cuando la petición diga sólo “crea una aplicación para Chile”, no despliegues automáticamente una auditoría jurídica extensa. Revisa primero:

1. ¿La función descrita implica usuarios, clientes, trabajadores u otras personas naturales?
2. ¿Recolectará o generará identificadores, contacto, transacciones, actividad o contenido de esas personas?
3. ¿El producto se dirige realmente a personas en Chile o Chile sólo aparece como ejemplo incidental?

Si 1 y 2 son sí y existe nexo, activa. Si el sistema es una calculadora local sin cuentas, telemetría ni datos de personas, no actives. Si falta un hecho decisivo y cambia materialmente el trabajo, pregunta de forma breve.

## Intensidad

| Nivel | Condición | Acción |
| --- | --- | --- |
| Base | Cualquier dato personal con nexo chileno. | Inventario, finalidad, licitud, información, derechos, conservación, seguridad, terceros y evidencia. |
| Reforzada | Sensibles, salud, biometría, menores, geolocalización, solvencia, infracciones, vigilancia, perfiles, decisiones automatizadas, tratamiento masivo, IA, transferencias o incidente. | Evaluación de alto riesgo, controles adicionales, revisión jurídica y posible evaluación de impacto. |
| Incidente | Pérdida, filtración, destrucción, alteración, acceso o comunicación no autorizada, incluso sospechada. | Contención, evidencia, régimen temporal, riesgo, comunicaciones y remediación. |

El RUT y una IP vinculable activan la revisión base porque pueden identificar, pero no son automáticamente sensibles. Pueden elevar el riesgo por uso masivo, exposición, combinación, autenticación indebida o efectos para la persona.

## Ejemplos de activación

| Petición | Decisión | Razón |
| --- | --- | --- |
| “Construye el onboarding de un marketplace chileno con RUT y despacho.” | Activar: construcción. | Mercado chileno y datos personales necesarios. |
| “Revisa esta API que devuelve fichas de pacientes en Chile.” | Activar: auditoría reforzada. | Nexo, salud y código existente. |
| “Una llave pública dejó expuesto un bucket con RUT y contratos.” | Activar: incidente y auditoría. | Posible acceso o filtración de datos personales. |
| “¿Qué exige la Ley 21.719?” | Activar: consulta. | Petición normativa directa. |
| “Diseña una calculadora offline de IVA chileno, sin cuentas ni telemetría.” | No activar el flujo completo. | Chile está presente, pero no hay tratamiento de personas. |
| “Revisa vulnerabilidades de una librería de compresión.” | No activar, salvo impacto demostrado en datos personales. | Ciberseguridad genérica sin nexo material. |
| “Analiza estadísticas públicas agregadas e irreversiblemente anónimas.” | No activar, salvo riesgo de reidentificación. | No hay datos personales si la anonimización es efectiva. |

## Momento dentro del ciclo de vida

### Requisitos

- Define titulares, finalidades, operaciones y datos necesarios.
- Identifica la fuente de licitud por finalidad.
- Determina categorías especiales y riesgo.
- Redacta criterios de aceptación de privacidad y seguridad.

### Arquitectura

- Traza flujos, roles, países, límites de confianza y terceros.
- Diseña mínimo privilegio, segregación, cifrado según riesgo y trazabilidad.
- Define retención, supresión, respaldos y atención de derechos.
- Decide si se requiere evaluación de impacto antes de implementar.

### Desarrollo y pruebas

- Revisa formularios, APIs, esquemas, logs, errores y permisos.
- Prefiere datos sintéticos o efectivamente anónimos.
- Prueba autorización por rol y organización, minimización y borrado.
- Evita datos personales en repositorios, fixtures y herramientas externas no aprobadas.

### Lanzamiento

- Verifica avisos, licitud, contratos, transferencias y canales de derechos.
- Comprueba configuración efectiva, restauración y respuesta a incidentes.
- Bloquea el lanzamiento si queda una exposición activa o falta un requisito esencial.

### Operación y cambios

- Reabre la revisión al cambiar finalidad, dato, modelo, proveedor, país, volumen, retención o población.
- Monitorea controles, accesos, trabajos de eliminación e incidentes.
- Conserva evidencia de decisiones y pruebas.

## Resultado del cribado

Entrega una ficha breve:

| Campo | Resultado |
| --- | --- |
| Activación | Sí, no o pendiente; ruta y fundamento. |
| Nexo chileno | Hechos y régimen temporal relevante. |
| Tratamiento | Operaciones y datos confirmados o previsibles. |
| Nivel | Base, reforzada o incidente. |
| Modo | Construcción, auditoría, incidente o consulta. |
| Supuestos | Lo inferido y qué lo cambiaría. |
| Siguiente paso | Referencia y artefactos que se revisarán. |
