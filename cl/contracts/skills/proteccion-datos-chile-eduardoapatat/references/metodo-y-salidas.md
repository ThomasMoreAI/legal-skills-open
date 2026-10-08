# Método y plantillas de salida

Elige la plantilla según el modo. Separa siempre obligación vigente, preparación para una norma publicada pero diferida, proyecto legislativo y buena práctica.

## Reglas comunes

- Declara fecha de corte, período de los hechos y alcance material revisado.
- Distingue hechos observados, hechos informados, supuestos e inferencias.
- Cita artículos sólo después de verificar la versión oficial aplicable.
- Usa **no verificado** cuando no exista evidencia suficiente.
- No conviertas recomendaciones técnicas en citas literales de la ley.
- No declares cumplimiento total ni ausencia de vulnerabilidades.

## Guía de construcción

Entrega en este orden:

1. **Decisión de activación:** nexo, tratamiento previsto, nivel y régimen temporal.
2. **Mapa del flujo objetivo:** titulares, datos, origen, servicios, bases, terceros, países y eliminación.
3. **Matriz de finalidad y licitud:** una fila por finalidad, con datos necesarios y evidencia prevista.
4. **Requisitos de diseño:** controles funcionales, técnicos, contractuales y organizativos.
5. **Historias o tareas:** propietario y dependencia de cada acción.
6. **Criterios de aceptación:** prueba reproducible que debe pasar antes de producción.
7. **Bloqueos de lanzamiento:** riesgos o decisiones que impiden liberar.
8. **Asuntos jurídicos abiertos:** interpretación, regulación pendiente o revisión profesional.

Formato recomendado:

| ID | Requisito | Fundamento | Implementación esperada | Prueba de aceptación | Responsable | Estado |
| --- | --- | --- | --- | --- | --- | --- |

Un requisito puede estar en estado pendiente, en curso, implementado, verificado o no aplica. “Implementado” no equivale a “verificado”.

## Auditoría de sistema existente

### Resumen

Incluye:

- alcance y limitaciones;
- decisión de activación;
- régimen y fecha de corte;
- cantidad de hallazgos por prioridad;
- riesgos que requieren acción inmediata;
- conclusión: listo dentro del alcance, listo con condiciones, bloqueado o no evaluable.

### Matriz de hallazgos

| ID | Hallazgo y evidencia | Datos/titulares | Estado | Régimen y norma | Riesgo técnico | Encaje jurídico | Corrección | Prueba |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Usa:

- **Estado:** cumple, parcial, no cumple, no verificado, no aplica.
- **Riesgo técnico:** crítico, alto, medio, bajo.
- **Encaje jurídico:** confirmado, probable, posible o no determinado.

Explica el criterio de prioridad. Usa crítico sólo ante exposición activa, riesgo inmediato significativo, tratamiento manifiestamente ilícito, incidente grave en curso o plazo inminente que pueda causar daño serio.

### Cobertura

Termina con:

- controles comprobados;
- artefactos examinados;
- componentes y ambientes no revisados;
- pruebas no ejecutadas;
- evidencia faltante para cerrar hallazgos.

No uses una tasa porcentual de “cumplimiento” salvo que exista un universo de controles definido, ponderación explicada y alcance homogéneo.

## Consulta jurídica puntual

1. **Respuesta breve:** conclusión condicionada en dos o tres frases.
2. **Régimen aplicable:** fecha de hechos, fecha de corte y versión normativa.
3. **Hechos y supuestos:** sólo los que cambian el resultado.
4. **Norma:** ley, artículo, elementos y excepción.
5. **Aplicación:** hecho por hecho, sin saltos inferenciales.
6. **Incertidumbre:** antecedente faltante, regulación pendiente o interpretación discutible.
7. **Acciones:** inmediatas, de transición y estructurales.
8. **Fuentes oficiales.**

## Inventario o evaluación de tratamiento

| Campo | Contenido esperado |
| --- | --- |
| Actividad | Operación concreta, no una categoría vaga. |
| Titulares | Grupos de personas y edades relevantes. |
| Datos | Entregados, observados, derivados e inferidos. |
| Finalidad | Específica y separada por actividad. |
| Necesidad | Justificación por dato y alternativa menos invasiva. |
| Licitud | Artículo, requisitos, ponderación y evidencia. |
| Roles | Responsable, encargado, cesionario, subencargado. |
| Sistemas | Aplicaciones, bases, logs, respaldos y ambientes. |
| Transparencia | Aviso, punto de entrega y versión. |
| Conservación | Plazo/criterio, evento inicial y eliminación. |
| Destinatarios | Terceros, países, finalidad y mecanismo. |
| Derechos | Canal, autenticación, ejecución y prueba. |
| Riesgos | Escenario, controles y riesgo residual. |
| Evaluación de impacto | Requerida, recomendable o no; fundamento. |

## Incidente de seguridad

1. **Situación y alcance confirmado.**
2. **Cronología.**
3. **Datos, titulares, sistemas, terceros y países.**
4. **Contención y preservación de evidencia.**
5. **Evaluación del riesgo para personas.**
6. **Régimen temporal y obligaciones concurrentes.**
7. **Matriz de comunicaciones:** destinatario, umbral, decisión, canal, plazo verificado, contenido y responsable.
8. **Recuperación, causa raíz y prevención.**
9. **Hechos desconocidos y plan para resolverlos.**

Nunca afirmes un plazo general de 72 horas sin una fuente chilena vigente para el caso. No incluyas datos personales o secretos reales en el informe cuando baste una referencia redactada.

## Evaluación de impacto

Incluye:

1. alcance, contexto y responsables;
2. descripción sistemática de operaciones y tecnología;
3. finalidades y fuentes de licitud;
4. necesidad y proporcionalidad;
5. titulares y consecuencias plausibles;
6. amenazas, vulnerabilidades, probabilidad y gravedad;
7. medidas existentes y previstas;
8. riesgo residual;
9. consulta a interesados o justificación de su omisión, si corresponde;
10. decisión, condiciones, aprobador y fecha de reevaluación.

No reduzcas la evaluación a una puntuación. Explica los escenarios y la razón de la decisión.

## Política o aviso de privacidad

Antes de redactar, exige o marca como pendiente:

- identidad y contacto del responsable;
- datos y fuentes;
- titulares y edades;
- finalidades y fuentes de licitud;
- destinatarios y transferencias;
- conservación;
- derechos, procedimiento y canal;
- decisiones automatizadas o perfiles;
- fecha y versión.

No produzcas texto genérico que esconda información faltante. Usa marcadores visibles y una tabla de validación contra el comportamiento real.

## Contrato con encargado

Revisa al menos:

- roles reales;
- objeto, duración, naturaleza y finalidad;
- categorías de datos y titulares;
- instrucciones documentadas;
- confidencialidad y accesos;
- medidas de seguridad y evidencia;
- notificación y cooperación en incidentes;
- asistencia en derechos y evaluaciones;
- subencargados y autorización escrita;
- ubicaciones y transferencias;
- auditoría y entrega de información;
- devolución o supresión al término;
- responsabilidad y coordinación regulatoria.

No importes una cláusula RGPD sin adaptarla a la norma chilena y al flujo real. Bajo el régimen reformado, contrasta el contrato con el artículo 15 bis.

## Plan de transición

| Obligación/control | Estado temporal | Situación actual | Evidencia | Brecha | Acción | Responsable | Fecha objetivo | Dependencia |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Usa como estado temporal:

- vigente y exigible;
- futura confirmada por norma publicada;
- propuesta legislativa;
- pendiente de reglamento o instrucción;
- buena práctica o decisión interna.

El plan debe ser útil incluso si cambia la fecha de vigencia: prioriza inventario, finalidad, roles, seguridad, derechos, contratos, retención e incidentes, que requieren trabajo previo.

## Cierre estándar

Concluye con una frase calibrada:

> Esta revisión cubre los componentes y evidencias indicados a la fecha de corte. No constituye certificación de cumplimiento ni prueba de ausencia de vulnerabilidades; los puntos marcados como no verificados requieren la evidencia señalada.

Adapta la frase al alcance. No uses la limitación como sustituto de hallazgos concretos.
