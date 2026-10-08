# Seguridad, incidentes, DPIA y decisiones automatizadas

## Seguridad — artículos 3 f) y 14 quinquies

La seguridad debe ser **adecuada al riesgo**, no una lista fija de productos. Evalúa estado de la técnica, costos de aplicación, naturaleza, alcance, contexto, finalidades y probabilidad/gravedad del impacto sobre titulares.

La evidencia debe cubrir, según el riesgo:

- confidencialidad, integridad, disponibilidad y resiliencia;
- control de acceso y privilegio mínimo;
- seudonimización y cifrado cuando correspondan;
- capacidad de restaurar disponibilidad y acceso tras incidentes físicos o técnicos;
- backups y restauraciones probadas;
- gestión de vulnerabilidades y cambios;
- logging y detección sin exponer datos innecesarios;
- revisión periódica de eficacia de medidas técnicas y organizativas;
- seguridad de terceros/encargados;
- formación y confidencialidad del personal.

**Regla de evidencia:** ante un incidente y en controversia judicial o administrativa, el responsable debe poder acreditar que las medidas existían y funcionaban en relación con el riesgo y la tecnología disponible. “Tenemos una política” no basta.

## Vulneraciones de seguridad — artículo 14 sexies

### Paso 1: clasificar el evento

Determina si hubo destrucción, filtración, pérdida, alteración accidental o ilícita, comunicación o acceso no autorizado a datos personales.

### Paso 2: evaluar el umbral legal

Si existe **riesgo razonable para los derechos y libertades de los titulares**, el responsable debe reportar la vulneración a la Agencia por los medios más expeditos posibles y **sin dilaciones indebidas**.

**Guardrail:** no conviertas esto en “72 horas” por analogía con GDPR. La Ley 21.719 no fija aquí un plazo general de 72 horas. Revisa si una ley sectorial o instrucción vigente añade otro plazo.

### Paso 3: registrar el incidente

Mantén un registro que permita reconstruir:

- naturaleza de la vulneración;
- cronología y detección;
- sistemas/activos afectados;
- categorías de datos;
- número aproximado de titulares;
- efectos o consecuencias posibles;
- medidas de contención, solución y mitigación;
- medidas para prevenir recurrencia;
- decisión y fundamento sobre notificación.

### Paso 4: evaluar comunicación a titulares

Además de la comunicación a la Agencia, la ley exige comunicación a titulares —por sus representantes cuando corresponda— cuando la vulneración se refiere a:

- datos personales sensibles;
- datos de niños y niñas **menores de 14 años**;
- datos relativos a obligaciones económicas, financieras, bancarias o comerciales.

La comunicación debe ser clara y sencilla, identificar los datos afectados, posibles consecuencias y medidas de solución/resguardo. Debe dirigirse a cada titular afectado; si no es posible, se usa el mecanismo de difusión previsto por la ley.

### Salida de incidente

Produce siempre:

1. hecho confirmado vs supuesto;
2. datos/titulares/sistemas afectados;
3. régimen temporal aplicable;
4. umbral de notificación y fundamento;
5. obligaciones a Agencia/titulares/otros reguladores;
6. medidas inmediatas;
7. evidencia preservada;
8. causa raíz y acciones preventivas;
9. decisiones aún pendientes.

No expongas datos personales del incidente en el informe más allá de lo necesario.

## Protección de datos desde el diseño y por defecto — artículo 14 quáter

Integra privacidad en requisitos, no al final del proyecto. Antes de producción verifica:

- campos estrictamente necesarios;
- defaults restrictivos;
- finalidades explícitas;
- retención y purga/anonimización;
- segregación de datos y ambientes;
- accesibilidad limitada;
- canal de derechos y capacidad real de ejecutar supresión/rectificación/bloqueo/portabilidad;
- terceros y transferencias conocidos;
- telemetría/logs minimizados;
- evaluación de automatización/perfilamiento.

## Evaluación de impacto en protección de datos — artículo 15 ter

Realiza una DPIA **antes del inicio** cuando, por naturaleza, alcance, contexto, tecnología o fines, el tratamiento pueda producir un alto riesgo para derechos de los titulares.

La ley exige DPIA siempre, entre otros, para:

1. evaluación sistemática y exhaustiva basada en tratamiento o decisiones automatizadas/perfilamiento con efectos jurídicos significativos;
2. tratamiento masivo o a gran escala;
3. observación o monitoreo sistemático de una zona de acceso público;
4. tratamiento de datos sensibles y especialmente protegidos en las hipótesis de excepción del consentimiento.

La Agencia debe publicar una lista orientativa de operaciones que requieren o no DPIA y orientaciones mínimas. **Antes de usar esa lista, verifica su versión vigente; si no está verificada, marca `PENDIENTE DE VERIFICACIÓN REGULATORIA`.**

### Contenido mínimo operativo de una DPIA

La ley exige que las orientaciones consideren al menos:

- descripción de las operaciones;
- finalidad;
- necesidad y proporcionalidad;
- evaluación de riesgos;
- medidas de mitigación.

Para hacerla útil añade: titulares afectados, datos, escala, ciclo de vida, actores, sistemas/ubicaciones, transferencias, amenazas, controles existentes, riesgo inherente, riesgo residual, owner, plazo y evidencia de cierre.

Si el resultado sigue mostrando alto riesgo, la ley permite consultar a la Agencia para obtener recomendaciones. No presentes esa consulta como aprobación automática del tratamiento.

## Decisiones automatizadas y perfilamiento — artículo 8 bis

El titular tiene derecho a oponerse y a no ser objeto de decisiones basadas en tratamiento automatizado —incluido perfilamiento— que produzcan efectos jurídicos o le afecten significativamente, sujeto a las excepciones legales.

Las excepciones incluyen, bajo sus condiciones:

- necesidad para celebrar o ejecutar un contrato;
- consentimiento previo y expreso;
- autorización legal con salvaguardas.

Incluso cuando una excepción permite la decisión automatizada, diseña salvaguardas para:

- información y transparencia;
- explicación significativa;
- intervención humana;
- posibilidad de expresar el punto de vista;
- revisión de la decisión.

### Checklist para sistemas de IA

Antes de aprobar un uso con datos personales pregunta:

- ¿la IA toma o sólo recomienda una decisión?
- ¿hay efecto jurídico o impacto significativo?
- ¿qué datos y variables derivadas usa?
- ¿se generan perfiles, scores, embeddings o inferencias personales?
- ¿cuál es la base de licitud por finalidad?
- ¿hay datos sensibles, biométricos o de NNA?
- ¿el proveedor recibe datos como encargado o como responsable independiente?
- ¿dónde se procesan y transfieren los datos?
- ¿puede explicarse la lógica relevante sin revelar secretos innecesarios?
- ¿existe intervención humana real, con autoridad para cambiar el resultado?
- ¿hay mecanismo de revisión y trazabilidad?
- ¿se activa una DPIA por alto riesgo o por un supuesto obligatorio?

No uses “human in the loop” como etiqueta vacía: verifica tiempo, competencia, información disponible y autoridad real de la persona revisora.
