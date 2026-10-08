---
name: acuerdos-piloto-ariel-gonzaguer
title: 'Skill: Acuerdos de piloto para productos digitales'
description: Crea acuerdos claros de piloto, beta, prueba controlada o acceso gratuito temporal para aplicaciones, SaaS y productos digitales. Úsala siempre que el usuario necesite formalizar expectativas, duración, acceso, soporte, feedback, datos, testimonios, terminación o continuidad pagada con participantes; también cuando pida convertir un acuerdo de piloto existente en una plantilla reutilizable.
author: Ariel-GonzAguer
author_url: https://github.com/Ariel-GonzAguer/skills-and-agents/tree/main/skills/acuerdos-piloto
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cr
practice: contracts
language: es
sources:
- title: Revision Legal
  path: references/revision-legal.md
---

# Skill: Acuerdos de piloto para productos digitales

Diseña documentos de participación en pilotos que sean claros para personas no especialistas, suficientemente completos para reducir malentendidos y fáciles de adaptar por proyecto. Incluye un modo de revisión legal preventiva para detectar riesgos, campos críticos y anexos que deben revisarse. El resultado sigue siendo un borrador operativo, no asesoría legal ni una conclusión sobre validez o exigibilidad.

## Modos de trabajo

- **Modo operativo:** redacta el acuerdo y sus anexos con expectativas, responsabilidades y campos pendientes.
- **Modo revisión legal:** úsalo por defecto cuando haya datos personales, empresas, personas consumidoras, pagos, testimonios, firma digital, limitación de responsabilidad, propiedad intelectual o una jurisdicción específica. Además del acuerdo, entrega supuestos, riesgos, bloqueos y fuentes oficiales consultadas.

Si el usuario pide “contrato”, “acuerdo legal”, “que sea válido”, “cumplimiento”, “protección de datos”, “firma electrónica” o una expresión equivalente, activa el modo revisión legal. No prometas que el documento será válido o suficiente sin revisión profesional.

## Flujo de trabajo

1. Lee el contexto del proyecto y localiza términos generales, política de privacidad, documentación de funcionalidades, límites de planes y canales de soporte existentes.
2. Extrae primero los hechos ya confirmados. No inventes nombre legal, registro tributario, precios, límites, funcionalidades, jurisdicción, plazos de conservación o garantías.
3. Clasifica el escenario: jurisdicción, proveedor y participante; B2B, B2C o mixto; persona física o persona jurídica; datos propios o datos de terceros; gratuito, pago o conversión posterior.
4. Haz preguntas agrupadas y concretas sobre las partes, el alcance, la duración, el acceso, el soporte, el uso esperado, el feedback, la privacidad, los testimonios, la terminación y la firma.
5. Ejecuta los criterios de bloqueo antes de cerrar el borrador. Pregunta o deja un bloqueo explícito si falta un dato que cambia materialmente el riesgo.
6. En modo revisión legal, consulta fuentes oficiales y vigentes de la jurisdicción cuando la cuestión dependa de leyes, reglamentos o autoridades que puedan cambiar. Registra fuente, fecha de consulta y tema; no presentes una inferencia como una conclusión jurídica.
7. Redacta un acuerdo independiente de los términos generales cuando el piloto tenga condiciones especiales. Explica la relación entre ambos documentos y cuál prevalece en caso de contradicción limitada.
8. Separa obligaciones obligatorias de autorizaciones opcionales. En especial, no mezcles el acceso al piloto con autorización de testimonios, logos, fotografías, audios o videos.
9. Incluye siempre expectativas prácticas: funcionalidades incluidas, límites, dependencia de Internet y proveedores, soporte, tiempo objetivo de respuesta, capacitación, mantenimiento, cambios y lo que no se garantiza.
10. Incluye el ciclo de datos: propiedad, roles de tratamiento, acceso de soporte, responsabilidad por datos de terceros, exportación, continuidad, incidentes y eliminación.
11. Incluye terminación, aviso previo, causas de suspensión, continuidad pagada, descuentos y obligaciones que sobreviven a la terminación.
12. Revisa consistencia con el proyecto: duración, precio, plan, límites, roles, canales, nombres, correo, teléfonos y política de privacidad.
13. Al entregar, separa el documento que verá la contraparte de la nota interna de riesgos, supuestos, bloqueos y revisión recomendada.

## Criterios de bloqueo legal

Detén el cierre como “listo para firmar” y pregunta o marca un bloqueo si falta cualquiera de estos datos cuando sea relevante:

- Identidad de la persona o entidad que contrata y capacidad para firmar.
- Jurisdicción aplicable y lugar de notificaciones.
- Si el participante es empresa, persona consumidora o ambos.
- Quién decide los fines del tratamiento de datos personales y quién presta el servicio.
- Qué datos de terceros se ingresarán, con qué finalidad, durante cuánto tiempo y cómo se atenderán solicitudes de titulares.
- Qué ocurre con los datos al terminar, incluyendo exportación, retención y eliminación.
- Precio, impuestos, renovación o descuento cuando exista continuidad pagada.
- Mecanismo de firma o aceptación y evidencia que se conservará.
- Límites de responsabilidad que puedan afectar derechos irrenunciables.

Si el usuario no puede responder todavía, conserva `[ completar ]`, explica el riesgo y no inventes una solución.

## Clasificación B2B, B2C y mixta

- **B2B:** exige datos de la empresa, representante y facultades; separa la relación comercial de los datos personales de empleados o clientes.
- **B2C:** usa lenguaje especialmente claro; identifica derechos imperativos, información precontractual, cancelación, renovación y posibles cláusulas abusivas según la jurisdicción.
- **Mixta:** redacta un núcleo común y marca las cláusulas que deben variar para cada tipo de participante. No asumas que una cláusula válida entre empresas aplica igual a consumidores.

## Revisión de datos personales

Cuando la aplicación almacene datos de clientes, empleados, proveedores o visitantes, analiza como mínimo:

1. Categorías de datos y si existe información sensible.
2. Finalidad y base jurídica comunicada a las personas titulares.
3. Rol de cada parte: responsable, encargado/proveedor u otra categoría local equivalente.
4. Instrucciones de tratamiento y acceso de soporte.
5. Proveedores, subencargados, almacenamiento extranjero y transferencias.
6. Medidas de seguridad, incidentes, copias, exportación y eliminación.
7. Derechos de acceso, rectificación, oposición, supresión o equivalentes locales.
8. Necesidad de aviso de privacidad, consentimiento, anexo de tratamiento o registro ante una autoridad.

No concluyas que una empresa queda liberada de sus deberes de privacidad porque el proveedor aloje los datos. No concluyas que el proveedor puede revisar libremente el contenido solo porque puede dar soporte.

## Revisión de firma y aceptación

Distingue entre:

- Firma manuscrita.
- Firma digital certificada.
- Firma electrónica simple.
- Aceptación dentro de una aplicación con registro de versión, identidad, fecha y evidencia.
- Aceptación por correo o mensajería.

Describe qué evidencia se conservará y evita afirmar equivalencia jurídica automática. Si el usuario necesita una firma con efectos específicos, remite a la legislación local y a asesoría profesional.

## Matriz de riesgos

En modo revisión legal entrega una tabla como esta fuera del contrato:

| Riesgo | Nivel | Evidencia o causa | Acción recomendada | Bloquea firma |
| --- | --- | --- | --- | --- |
| Identidad o representación incompleta | Alto/Medio/Bajo | Dato faltante | Completar datos o revisar facultades | Sí/No |
| Datos personales de terceros | Alto/Medio/Bajo | Tipo de dato y rol inciertos | Aviso, anexo de tratamiento o revisión legal | Sí/No |
| Firma o aceptación | Alto/Medio/Bajo | Mecanismo elegido | Definir evidencia y consultar ley local | Sí/No |
| Pago, renovación o descuento | Alto/Medio/Bajo | Condición ambigua | Completar precio, impuestos y vigencia | Sí/No |
| Responsabilidad o garantía | Alto/Medio/Bajo | Limitación amplia | Revisión de cláusulas imperativas | Sí/No |

Usa nivel **Alto** cuando falte un dato que pueda invalidar la identificación de una parte, afectar derechos irrenunciables, exponer datos personales o cambiar sustancialmente el costo o la responsabilidad.

## Estructura recomendada

Usa esta estructura salvo que el proyecto tenga una plantilla mejor:

1. Título, versión y nota de revisión legal.
2. Partes y datos para notificaciones.
3. Propósito y relación con términos generales y privacidad.
4. Inicio, duración y alcance del piloto.
5. Acceso, gratuidad, plan y límites.
6. Funcionalidades incluidas y dependencias.
7. Capacitación y soporte.
8. Compromisos del proveedor.
9. Compromisos de la persona participante.
10. Feedback, recomendaciones y mejoras.
11. Testimonios, reseñas y uso de marca como autorización separada.
12. Datos, privacidad y confidencialidad.
13. Seguridad, uso aceptable y reportes legales.
14. Exportación, continuidad y eliminación.
15. Continuidad pagada o conversión a plan comercial.
16. Disponibilidad, cambios y limitación de responsabilidad.
17. Terminación anticipada.
18. Propiedad intelectual.
19. Notificaciones.
20. Ley aplicable, firmas y anexos.

## Reglas de redacción

- Usa español claro, directo y neutral; define los términos que se repitan.
- Evita prometer disponibilidad, resultados comerciales, corrección inmediata o seguridad absoluta.
- Distingue un objetivo de atención de una garantía contractual.
- No presentes un nombre comercial como si fuera una persona jurídica inscrita. Si el operador aún no está constituido, identifica a la persona física y menciona el nombre comercial como tal.
- Para datos de terceros, deja claro quién recopila la información, quién decide para qué se usa y quién debe obtener permisos o informar a los titulares.
- No conviertas el feedback en una obligación de ceder propiedad intelectual sobre la empresa participante. Autoriza únicamente el uso de ideas y sugerencias necesarias para mejorar el producto.
- Mantén separadas las autorizaciones de marketing, testimonios, logos, fotos, audio y video.
- Si se permite aceptación digital, no afirmes que cualquier mensaje informal tiene automáticamente la misma fuerza que una firma digital certificada. Describe el mecanismo y deja su validez a la legislación aplicable.
- Si el piloto se ofrece a empresas y personas físicas, contempla ambos casos y exige facultades de representación cuando alguien firme por una empresa.
- No inventes un plazo de eliminación. Usa el plazo de la política de privacidad o deja un campo para confirmarlo.
- Evita incluir precios o límites actuales en el cuerpo si cambian con frecuencia; usa una ficha de incorporación o anexo por participante.

## Revisión antes de entregar

Comprueba que:

- [ ] La duración se calcula desde el evento correcto.
- [ ] El piloto es realmente gratuito y se indica qué ocurre después.
- [ ] El plan y sus límites quedan registrados por participante.
- [ ] Las obligaciones de uso y feedback son medibles y razonables.
- [ ] Se distingue feedback voluntario de cualquier encuesta obligatoria.
- [ ] El soporte indica canal, horario y expectativa realista.
- [ ] El proveedor no promete funciones o niveles de servicio que el proyecto no ofrece.
- [ ] La empresa conserva sus registros internos y recibe una salida de datos utilizable.
- [ ] La responsabilidad por datos personales de clientes y empleados está descrita.
- [ ] Suspensión, terminación y aviso previo son coherentes.
- [ ] La continuidad pagada y los descuentos no son ambiguos.
- [ ] Testimonios y uso de marca tienen aceptación separada.
- [ ] El documento tiene campos de firma, fecha y notificaciones.
- [ ] Se advierte que debe revisarse conforme a la ley local.

### Revisión legal adicional

- [ ] Se identificó la jurisdicción y se consultaron fuentes oficiales vigentes cuando correspondía.
- [ ] Se clasificó el escenario como B2B, B2C o mixto.
- [ ] Se distinguió persona física, persona jurídica y nombre comercial.
- [ ] Se documentaron roles, finalidades y responsabilidades sobre datos personales.
- [ ] Se revisaron terceros, proveedores, transferencias, seguridad, incidentes y eliminación.
- [ ] Se distinguió el tipo de firma o aceptación y la evidencia que se conservará.
- [ ] Se revisaron precio, impuestos, renovación, descuentos y cancelación.
- [ ] Se preparó una matriz de riesgos fuera del documento.
- [ ] Se marcaron bloqueos que requieren datos o revisión profesional.

## Entregables

Entrega como mínimo:

- `acuerdo-piloto-[duracion].md`: plantilla principal con campos editables.
- Una ficha o anexo para datos específicos de cada participante y su plan.
- Un anexo opcional para testimonios y uso de marca cuando el piloto pida reseñas públicas.

En modo revisión legal entrega además:

- `revision-legal.md`: jurisdicción, clasificación B2B/B2C, fuentes consultadas, supuestos, riesgos, bloqueos y preguntas para un profesional.
- Un anexo de tratamiento de datos cuando una parte procese datos personales por cuenta de la otra.
- Un checklist de aceptación y conservación de evidencia cuando se use firma digital o aceptación electrónica.

Antes de terminar, indica los supuestos materiales, los campos pendientes y cualquier contradicción encontrada entre el acuerdo y la documentación del producto.
