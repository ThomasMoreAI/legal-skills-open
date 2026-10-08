# Incidentes, infracciones y consecuencias

Usa este archivo ante pérdida, destrucción, alteración, filtración, divulgación o acceso no autorizado a datos personales, y para relacionar hallazgos con el régimen sancionatorio. No confundas una debilidad, un incidente, una vulneración de seguridad y una infracción jurídica: pueden coincidir, pero requieren hechos distintos.

## Respuesta inmediata a un incidente

1. **Proteger a las personas.** Contén el acceso o exposición sin destruir evidencia; rota secretos y revoca sesiones cuando corresponda.
2. **Preservar evidencia.** Registra tiempos en UTC y local, fuentes, hashes o copias forenses, decisiones, responsables y cadena de custodia.
3. **Delimitar.** Identifica sistemas, ambientes, datos, titulares, cantidad aproximada, período, actor, países y terceros.
4. **Confirmar qué ocurrió.** Distingue posibilidad de acceso, acceso confirmado, extracción, comunicación, alteración, pérdida, destrucción e indisponibilidad.
5. **Evaluar consecuencias.** Considera suplantación, fraude, discriminación, daño físico, reputacional o económico, pérdida de confidencialidad y afectación a derechos.
6. **Fijar el régimen temporal.** Usa la norma vigente en la fecha del hecho y revisa obligaciones sectoriales, contractuales o de ciberseguridad concurrentes.
7. **Decidir comunicaciones.** Documenta destinatario, umbral, canal, contenido, plazo, fundamento y aprobador.
8. **Recuperar y prevenir.** Corrige la causa, verifica restauración, monitorea recurrencia y conserva un plan de acciones.

No pidas que el usuario pegue bases filtradas, credenciales o datos identificables. Solicita conteos, categorías, muestras redactadas o acceso controlado cuando sea imprescindible.

## Régimen anterior a la reforma

Antes de la entrada finalmente aplicable de la Ley N.º 21.719, la Ley N.º 19.628 vigente exige, entre otros puntos:

- secreto respecto de datos provenientes o recolectados de fuentes no accesibles al público, en los términos del artículo 7;
- uso para la finalidad y calidad de datos conforme a los artículos 6 y 9;
- debida diligencia en el cuidado de los datos almacenados y responsabilidad por daños, artículo 11;
- indemnización del daño patrimonial y moral causado por tratamiento indebido, artículo 23.

La versión anterior de la Ley N.º 19.628 no contiene un deber general de notificación de brechas equivalente al futuro artículo 14 sexies ni el régimen general de multas administrativas de los artículos 34 a 40 reformados. No concluyas por ello que nunca debe notificarse: verifica normas sectoriales, obligaciones contractuales, órdenes de autoridad y cualquier otra ley aplicable al responsable o incidente.

## Régimen reformado: artículo 14 sexies

Desde la entrada en vigencia finalmente aplicable, el responsable debe reportar a la Agencia, por los medios más expeditos posibles y **sin dilaciones indebidas**, una vulneración que:

1. ocasione destrucción, filtración, pérdida o alteración accidental o ilícita de datos, o comunicación o acceso no autorizado; y
2. genere un riesgo razonable para los derechos y libertades de los titulares.

El responsable debe registrar estas comunicaciones, incluyendo naturaleza, efectos, categorías de datos, número aproximado de titulares y medidas adoptadas para gestionar y prevenir incidentes futuros.

Además, debe comunicar a los titulares afectados cuando la vulneración se refiera a:

- datos personales sensibles;
- datos de niños o niñas menores de catorce años; o
- datos sobre obligaciones económicas, financieras, bancarias o comerciales.

La comunicación a titulares debe ser clara y sencilla, individualizar los datos afectados, indicar posibles consecuencias y medidas adoptadas. Se realiza a cada afectado y, si no es posible, mediante aviso en un medio de comunicación social masivo y de alcance nacional.

El tercero mandatario o encargado debe reportar la vulneración al responsable, conforme al artículo 15 bis. Define contractualmente un canal y plazo operacional que permitan al responsable cumplir, pero no presentes ese plazo contractual como el plazo legal de la Agencia.

La ley publicada no fija una regla general de 72 horas. No la importes del RGPD. Verifica las instrucciones vigentes de la Agencia y las reglas sectoriales aplicables al caso.

## Árbol de decisión para una vulneración

Responde y documenta:

| Pregunta | Consecuencia |
| --- | --- |
| ¿Hay datos personales y nexo jurídico aplicable? | Si no, documenta por qué queda fuera; si sí, continúa. |
| ¿Hubo destrucción, filtración, pérdida, alteración, comunicación o acceso no autorizado? | Si sólo existe una debilidad no explotada, trátala como vulnerabilidad y remédiala; si ocurrió, continúa. |
| ¿Qué régimen estaba vigente al ocurrir? | Separa obligaciones actuales, futuras y sectoriales. |
| ¿Existe riesgo razonable para derechos y libertades? | Bajo la reforma, determina si se activa el reporte a la Agencia; justifica factores y evidencia. |
| ¿Incluye sensibles, menores de 14 o datos económicos/financieros/bancarios/comerciales? | Bajo la reforma, evalúa la comunicación adicional obligatoria a titulares. |
| ¿Intervino un encargado? | Activa su reporte al responsable, cooperación, evidencia y obligaciones contractuales. |
| ¿Hay otros países, sectores o contratos? | Analiza notificaciones concurrentes sin asumir que una sustituye a otra. |

Ante duda razonable en un incidente activo de alto impacto, prioriza escalamiento jurídico y técnico urgente; no retrases contención por esperar certeza total.

## Registro mínimo de incidente

| Campo | Contenido |
| --- | --- |
| Identificador | Código estable y nombre neutro. |
| Detección y período | Fecha/hora, zona, fuente y ventana estimada. |
| Sistemas | Activos, ambientes, propietarios y terceros. |
| Evento | Acceso, extracción, divulgación, alteración, pérdida, destrucción o indisponibilidad. |
| Datos y titulares | Categorías, sensibilidad legal, edades y número aproximado. |
| Confirmación | Confirmado, probable, posible o descartado, con evidencia. |
| Contención | Acción, responsable, hora y efecto verificado. |
| Riesgo para titulares | Escenarios, probabilidad, gravedad y factores mitigantes. |
| Régimen | Norma vigente, futura o sectorial y fecha de corte. |
| Comunicaciones | Agencia, titulares, terceros u otra autoridad; decisión y fundamento. |
| Recuperación | Restauración, validación y monitoreo. |
| Prevención | Causa raíz, acciones, dueño, fecha y prueba. |

## Infracciones del régimen reformado

Las siguientes categorías rigen desde la entrada finalmente aplicable de la reforma. Son un mapa de investigación, no una declaración automática de culpabilidad.

### Artículo 34 bis: leves

- incumplir total o parcialmente información y transparencia del artículo 14 ter;
- carecer de un domicilio, correo o medio equivalente actualizado y operativo para contacto y derechos;
- omitir, responder incompletamente o fuera de plazo solicitudes de titulares;
- omitir comunicaciones obligatorias a la Agencia previstas por ley o reglamento;
- incumplir instrucciones generales de la Agencia cuando la conducta no sea grave o gravísima;
- otras infracciones no calificadas como graves o gravísimas.

### Artículo 34 ter: graves

- tratar sin consentimiento o fundamento legal, o con finalidad distinta;
- comunicar o ceder sin consentimiento cuando sea necesario, o para finalidad distinta;
- tratar datos innecesarios frente a la finalidad;
- tratar datos inexactos, incompletos o desactualizados, con la excepción legal indicada;
- impedir u obstaculizar derechos de acceso, rectificación, supresión, oposición o portabilidad;
- omitir, retrasar o denegar sin causa una solicitud fundada de bloqueo temporal;
- infringir las reglas sobre niños, niñas y adolescentes;
- infringir los requisitos especiales para ciertas personas jurídicas sin fines de lucro;
- vulnerar secreto o confidencialidad;
- vulnerar las obligaciones de seguridad del artículo 14 quinquies;
- omitir comunicaciones o registros exigibles ante vulneraciones de seguridad;
- usar medidas de calidad o seguridad insuficientes en investigación histórica, estadística o científica de interés público;
- efectuar transferencias internacionales contrarias a la ley;
- incumplir una resolución o requerimiento específico y directo de la Agencia.

### Artículo 34 quáter: gravísimas

- tratar datos fraudulentamente;
- destinar maliciosamente los datos a una finalidad distinta;
- comunicar o ceder a sabiendas información falsa, incompleta, inexacta o desactualizada;
- vulnerar secreto o confidencialidad de datos sensibles o relativos a infracciones;
- tratar, comunicar o ceder a sabiendas datos sensibles o de menores en contra de la ley;
- omitir deliberadamente la comunicación de vulneraciones de seguridad que puedan afectar confidencialidad, disponibilidad o integridad;
- tratar masivamente registros electrónicos públicos de infracciones sin autorización legal;
- realizar a sabiendas transferencias internacionales contrarias a la ley;
- incumplir una resolución de la Agencia sobre derechos de un titular;
- entregar a sabiendas información falsa, incompleta o manifiestamente errónea para registrar o certificar un modelo de prevención;
- incumplir la evaluación de impacto cuando corresponda.

Para usar estas categorías, compara todos los elementos, incluidos términos como “a sabiendas”, “maliciosamente”, “deliberadamente”, “sin fundamento” o “alto riesgo”. Una evidencia técnica aislada rara vez acredita por sí sola el elemento subjetivo.

## Sanciones y otras consecuencias del régimen reformado

El artículo 35 contempla:

| Categoría | Sanción general máxima |
| --- | --- |
| Leve | Amonestación escrita o multa de hasta 5.000 UTM. |
| Grave | Multa de hasta 10.000 UTM. |
| Gravísima | Multa de hasta 20.000 UTM. |

No calcules una multa probable a partir del máximo. Considera la conducta, diligencia, perjuicio, cantidad de titulares, beneficio, datos sensibles o de menores, capacidad económica, antecedentes, atenuantes y agravantes de los artículos 36 y 37.

La ley también contempla, entre otras consecuencias:

- recargo de 50 % si no se adoptan oportunamente las medidas de subsanación ordenadas;
- hasta tres veces la multa por reincidencia;
- para ciertas empresas que no sean de menor tamaño y reincidan en infracciones graves o gravísimas, el monto más gravoso entre la regla de reincidencia y hasta 2 % o 4 % de ingresos anuales, respectivamente;
- posible suspensión temporal de operaciones de tratamiento por infracciones gravísimas reiteradas, artículo 38;
- anotación pública en el Registro Nacional de Sanciones y Cumplimiento, artículo 39;
- responsabilidad civil por daño patrimonial y extrapatrimonial, artículo 47;
- otras responsabilidades civiles o penales que puedan concurrir, artículo 34.

Verifica la redacción vigente, el tipo de sujeto y las normas transitorias antes de citar una consecuencia.

## Prevención y modelo voluntario

El artículo 48 reformado obliga a adoptar acciones para prevenir las infracciones de los artículos 34 bis, 34 ter y 34 quáter. Los artículos 49 a 53 regulan un modelo voluntario de prevención y su certificación.

El Decreto N.º 662, publicado el 9 de septiembre de 2026, desarrolla ese modelo. Entre sus elementos incluye caracterización de tratamientos, matriz de riesgos de infracción, protocolos, reporte interno y externo, mecanismos de denuncia, sanciones internas y un delegado con medios y facultades. La certificación del modelo no reemplaza el cumplimiento real ni impide que existan infracciones.

No describas al delegado como universalmente obligatorio para todo responsable: su designación es obligatoria dentro del modelo voluntario certificado, sin perjuicio de otras normas que puedan exigirlo para un sujeto específico.

## Cómo informar un posible encaje sancionatorio

Para cada conducta indica:

1. hecho observado y fuente de evidencia;
2. artículo sustantivo posiblemente vulnerado;
3. tipo del artículo 34 bis, 34 ter o 34 quáter que podría corresponder;
4. elementos acreditados y elementos faltantes;
5. régimen temporal y sujeto al que se aplicaría;
6. medidas inmediatas para cesar, mitigar y preservar evidencia;
7. necesidad de revisión jurídica.

Usa “podría encuadrar” cuando no estén acreditados todos los elementos. No declares una multa exacta, dolo, responsabilidad administrativa, civil o penal ni reincidencia sin antecedentes suficientes y una decisión competente.
