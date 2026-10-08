---
name: check-relocation-documents-pjt222
title: Check Relocation Documents
description: Verificar la completitud de documentos para cada paso burocrático de una reubicación UE/DACH, señalando elementos faltantes y requisitos de traducción. Usar después de crear un plan de reubicación y antes de comenzar procedimientos burocráticos, al prepararse para una cita específica (Buergeramt, Finanzamt), cuando no se está seguro de qué documentos necesitan traducción certificada o apostilla, después de recibir un rechazo o solicitud de documentos adicionales, o como verificación periódica durante el proceso de reubicación para asegurar que nada se haya pasado por alto.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/es/skills/check-relocation-documents
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: es
---

# Check Relocation Documents

Verificar que todos los documentos requeridos estén presentes, vigentes y debidamente preparados para cada paso burocrático de una reubicación UE/DACH, generando una lista accionable de elementos faltantes y necesidades de traducción.

## Cuándo Usar

- Después de crear un plan de reubicación y antes de comenzar procedimientos burocráticos
- Al prepararse para una cita específica (Buergeramt, Finanzamt, oficina de seguros)
- Cuando no se está seguro de qué documentos necesitan traducción certificada o apostilla
- Después de recibir un rechazo o solicitud de documentos adicionales de una autoridad
- Cuando un miembro del hogar tiene una nacionalidad diferente que requiere pistas documentales separadas
- Como verificación periódica durante el proceso de reubicación para asegurar que nada se haya pasado por alto

## Entradas

### Requerido

- **Plan de reubicación**: Salida de la habilidad plan-eu-relocation o equivalente, listando todos los pasos burocráticos
- **País de destino**: Alemania, Austria, Suiza u otro país de la UE
- **Nacionalidad(es)**: Para todos los miembros del hogar
- **Inventario de documentos**: Lista de documentos actualmente en posesión (originales y copias)

### Opcional

- **País de origen**: Para determinar qué documentos necesitan apostilla o legalización según la Convención de La Haya
- **Contrato de empleo**: Para determinar documentos proporcionados por el empleador (ej., Arbeitgeberbescheinigung)
- **Idioma de documentos existentes**: Para identificar necesidades de traducción
- **Experiencia previa de reubicación**: Registros previos en la UE que pueden simplificar requisitos
- **Circunstancias especiales**: Refugiados reconocidos, titulares de Tarjeta Azul UE, trabajadores desplazados (requisitos documentales diferentes)

## Procedimiento

### Paso 1: Listar Todos los Pasos Burocráticos

Extraer cada paso de registro, solicitud y notificación del plan de reubicación.

1. Analizar el plan de reubicación para todos los elementos de acción que requieren envío de documentos
2. Categorizar pasos por tipo de autoridad:
   - Oficinas de registro municipal (Buergeramt, Meldeamt, Einwohnerkontrolle)
   - Autoridades fiscales (Finanzamt)
   - Proveedores de seguro de salud (Krankenkasse, OeGK, aseguradora suiza)
   - Oficinas de seguridad social (Rentenversicherung, Sozialversicherung, AHV)
   - Oficina de inmigración/extranjería (Auslaenderbehorde) si aplica
   - Bancos e instituciones financieras
   - Escuelas e instalaciones de cuidado infantil
   - Registro de vehículos (Kfz-Zulassungsstelle)
   - Otros (importación de mascotas, reconocimiento de licencia profesional)
3. Ordenar pasos según la cadena de dependencias del plan de reubicación
4. Anotar qué pasos comparten los mismos documentos (para evitar preparación redundante)

**Esperado:** Una lista numerada de todos los pasos burocráticos, categorizados y ordenados, con notas sobre requisitos documentales compartidos.

**En caso de fallo:** Si el plan de reubicación es incompleto o no está disponible, construir la lista de pasos desde el checklist oficial de reubicación del país de destino (ej., Alemania: make-it-in-germany.com, Austria: migration.gv.at, Suiza: ch.ch/en/moving-switzerland).

### Paso 2: Mapear Documentos Requeridos por Paso

Para cada paso burocrático, identificar cada documento que la autoridad requiere.

1. Para registro municipal (Anmeldung/Meldezettel):
   - Pasaporte válido o documento nacional de identidad (todos los miembros del hogar)
   - Wohnungsgeberbestaetigung / contrato de alquiler / escritura de propiedad
   - Certificado de matrimonio (si se registra como pareja)
   - Partidas de nacimiento (para hijos)
   - Confirmación de registro previo (si se muda dentro del país)
2. Para registro fiscal:
   - Confirmación de registro de residencia (Meldebestaetigung/Meldezettel)
   - Contrato de empleo o registro de empresa
   - ID fiscal del país de origen (para coordinación transfronteriza)
   - Certificado de matrimonio (para asignación de clase fiscal en Alemania)
3. Para inscripción en seguro de salud:
   - Contrato de empleo o prueba de trabajo autónomo
   - Confirmación de seguro previo o EHIC (Tarjeta Sanitaria Europea)
   - Formulario S1 (para trabajadores desplazados o situaciones transfronterizas)
   - Confirmación de registro de residencia
4. Para coordinación de seguridad social:
   - Documento portátil A1 (para trabajadores desplazados)
   - Formularios E o formularios S para transferencia de beneficios
   - Documentación de historial laboral
   - Número de seguridad social del país de origen
5. Para apertura de cuenta bancaria:
   - Pasaporte válido o documento nacional de identidad
   - Confirmación de registro de residencia
   - Prueba de ingresos (contrato de empleo o nóminas recientes)
   - ID fiscal o Steueridentifikationsnummer (Alemania)
6. Para permisos de inmigración/residencia (nacionales no-UE):
   - Pasaporte válido con al menos 6 meses de validez restante
   - Fotos biométricas (formato específico por país)
   - Contrato de empleo o carta de oferta de trabajo
   - Prueba de medios financieros
   - Confirmación de seguro de salud
   - Título universitario con reconocimiento (para Tarjeta Azul UE)
   - Certificado de antecedentes penales (puede requerir apostilla)
7. Para re-matriculación de vehículo:
   - Documento de registro del vehículo (Fahrzeugbrief/Zulassungsbescheinigung Teil II)
   - Prueba de seguro (número eVB en Alemania)
   - Certificado de inspección TUeV/Pickerl/MFK
   - Confirmación de registro de residencia
8. Para inscripción escolar/guardería:
   - Partidas de nacimiento
   - Registros de vacunación (Impfpass)
   - Informes escolares previos con traducciones
   - Confirmación de registro de residencia

**Esperado:** Una matriz que mapea cada paso burocrático a sus documentos requeridos, con especificaciones del documento (original requerido, copia aceptable, traducción certificada necesaria).

**En caso de fallo:** Si los requisitos para un paso específico no son claros, verificar el sitio web de la autoridad directamente o llamar a su línea de servicio. Los requisitos pueden cambiar; no confiar únicamente en guías de terceros con más de 12 meses de antigüedad.

### Paso 3: Verificar el Estado Actual de Documentos

Comparar los documentos requeridos contra el inventario actual para identificar brechas.

1. Para cada documento requerido, verificar:
   - **Tiene (original)**: El documento original está en posesión y accesible
   - **Tiene (solo copia)**: Solo existe una copia; puede ser necesario solicitar el original
   - **Vencido**: El documento existe pero el período de validez ha expirado
   - **Faltante**: El documento no existe y debe obtenerse
   - **No aplica**: El documento no es necesario para este caso específico
2. Para documentos que están en "Tiene (original)", verificar:
   - El documento no está dañado ni es ilegible
   - Los nombres coinciden en todos los documentos (atención a diferencias de transliteración, apellidos de soltera, segundos nombres)
   - El documento seguirá siendo válido al momento de su uso (pasaportes, documentos de identidad, tarjetas de seguro)
3. Para documentos vencidos, determinar:
   - Tiempo de procesamiento de renovación en la autoridad emisora
   - Si un documento vencido es aceptado temporalmente (algunos sí, la mayoría no)
   - Costo de renovación
4. Para documentos faltantes, determinar:
   - Autoridad emisora y su tiempo de procesamiento
   - Documentos de respaldo requeridos para obtener el documento faltante (verificación recursiva)
   - Costo y método de pago
   - Si puede solicitarse remotamente o requiere presencia en persona
5. Señalar cualquier documento donde los nombres no coincidan (ej., pasaporte tiene apellido de soltera, certificado de matrimonio tiene apellido de casada) — estos probablemente requerirán explicación o prueba adicional de cambio de nombre

**Esperado:** Una tabla de estado para cada documento requerido: estado (tiene/solo-copia/vencido/faltante/N-A), fecha de validez, y notas sobre cualquier problema.

**En caso de fallo:** Si el estado del documento no puede confirmarse (ej., documentos están en almacenamiento o con otra persona), marcar como "sin confirmar" y tratar como potencialmente faltante para propósitos de planificación.

### Paso 4: Identificar Requisitos de Traducción y Apostilla

Determinar qué documentos necesitan traducción certificada, apostilla u otra legalización.

1. Verificar requisitos de idioma del país de destino:
   - Alemania: Los documentos generalmente deben estar en alemán o acompañados de traducción certificada
   - Austria: Igual que Alemania; algunas oficinas aceptan inglés para documentos de la UE
   - Suiza: Depende del cantón (área de alemán, francés, italiano o romanche)
2. Identificar qué documentos están exentos de traducción:
   - Formularios estándar multilingües de la UE (Regulación 2016/1191) para nacimiento, matrimonio, defunción y otros documentos de estado civil entre estados miembros de la UE
   - Pasaportes y documentos nacionales de identidad (universalmente aceptados sin traducción)
   - EHIC (Tarjeta Sanitaria Europea)
3. Para documentos que requieren traducción:
   - Debe ser realizada por un traductor jurado/certificado (beeidigter Uebersetzer)
   - El traductor debe estar certificado en el país de destino (no el país de origen)
   - Tiempo de entrega típico: 3-10 días hábiles
   - Costo: 30-80 EUR por página dependiendo del par de idiomas y la complejidad
4. Determinar requisitos de apostilla o legalización:
   - Documentos de países de la Convención de La Haya: apostilla de la autoridad competente del país emisor
   - Documentos de países no-Haya: cadena completa de legalización (notario local, ministerio de asuntos exteriores, embajada)
   - Documentos intra-UE: frecuentemente exentos de apostilla bajo regulaciones de la UE, pero verificar por tipo de documento
   - Suiza es miembro de la Convención de La Haya pero no miembro de la UE; las reglas difieren
5. Verificar si el país de destino acepta apostillas digitales o electrónicas
6. Notar que algunos documentos requieren tanto apostilla COMO traducción certificada (la apostilla misma puede también necesitar traducción)

**Esperado:** Una matriz de traducción/legalización mostrando para cada documento: traducción necesaria (sí/no), apostilla necesaria (sí/no), costo estimado y tiempo de procesamiento estimado.

**En caso de fallo:** Si hay incertidumbre sobre si un documento específico necesita apostilla, contactar a la autoridad de destino directamente. Sobre-prepararse (obtener una apostilla innecesaria) es mejor que sub-prepararse (ser rechazado en la cita).

### Paso 5: Generar Lista de Acciones

Compilar todos los hallazgos en una lista de acciones priorizada y consciente de plazos.

1. Fusionar todas las brechas (faltantes, vencidos, traducción necesaria, apostilla necesaria) en una única lista de acciones
2. Para cada elemento de acción, incluir:
   - Nombre del documento
   - Acción requerida (obtener, renovar, traducir, apostillar, reemplazar)
   - Autoridad emisora o proveedor de servicio
   - Tiempo de procesamiento estimado
   - Costo estimado
   - Plazo (derivado de cuándo el documento se necesita primero en el cronograma de reubicación)
   - Prioridad (crítica / alta / media / baja)
3. Asignar prioridad basada en:
   - **Crítica**: Bloquea el primer paso burocrático (ej., pasaporte para Anmeldung) o tiene un plazo no negociable
   - **Alta**: Necesario dentro de las primeras 2 semanas después de la llegada; largo tiempo de procesamiento
   - **Media**: Necesario dentro del primer mes; tiempo de procesamiento razonable
   - **Baja**: Necesario eventualmente; sin presión de plazo inmediata
4. Ordenar la lista por:
   - Primero: Elementos críticos ordenados por mayor tiempo de procesamiento (comenzar estos primero)
   - Luego: Elementos altos ordenados por plazo
   - Luego: Elementos medios y bajos
5. Calcular costo total estimado para toda la preparación de documentos
6. Agregar un checklist de "carpeta de documentos" para el día de cada cita, listando exactamente qué originales, copias y traducciones llevar

**Esperado:** Una lista de acciones priorizada con plazos, costos y tiempos de procesamiento, más listas de empaque por cita para documentos.

**En caso de fallo:** Si los tiempos de procesamiento son inciertos (común para documentos de países con burocracias más lentas), usar estimaciones de peor caso y comenzar el proceso lo antes posible. Señalar elementos donde el procesamiento acelerado está disponible a costo adicional.

## Validación

- Cada paso burocrático del plan de reubicación tiene al menos un documento mapeado
- Ningún documento está listado como "estado desconocido" -- todos deben estar confirmados como tiene/faltante/vencido/N-A
- Los requisitos de traducción referencian los requisitos oficiales de idioma del país de destino
- Los requisitos de apostilla están verificados contra la membresía en la Convención de La Haya del país emisor
- Los plazos en la lista de acciones se alinean con el cronograma de reubicación de plan-eu-relocation
- Las asignaciones de prioridad son consistentes (ningún elemento de prioridad "baja" que bloquee un paso "crítico")
- El costo total estimado está calculado y presentado
- Los checklists de documentos por cita están generados para al menos los primeros tres pasos burocráticos

## Errores Comunes

- **Asumir que los documentos de la UE no necesitan preparación**: Aunque las regulaciones de la UE simplifican la aceptación transfronteriza de documentos, la mayoría de oficinas aún requieren traducciones y algunas requieren apostillas incluso entre estados de la UE
- **Discrepancias de nombre entre documentos**: La transliteración de escrituras no latinas, el uso de apellido de soltera vs. de casada, e inconsistencias de segundo nombre son la razón más común de rechazo en citas
- **Confiar en fotocopias**: La mayoría de autoridades DACH requieren documentos originales para inspección y conservan copias certificadas; llevar originales incluso si se piensa que las copias serán suficientes
- **Solicitar traducciones demasiado tarde**: Los traductores jurados frecuentemente tienen retrasos de 1-2 semanas, y esto se extiende durante la temporada alta de reubicación (agosto-septiembre)
- **Olvidar la apostilla en la traducción**: Algunas autoridades requieren la apostilla en el documento original Y una traducción certificada separada del documento apostillado
- **No verificar períodos de validez de documentos**: Un pasaporte válido por 2 meses más puede ser rechazado si la autoridad requiere 6 meses de validez restante
- **Ignorar los formularios multilingües de la UE**: Para documentos de estado civil entre países de la UE, los formularios estándar multilingües (disponibles en la autoridad emisora) pueden eliminar la necesidad de traducción completamente — pero deben solicitarse explícitamente
- **Asumir que los documentos digitales son aceptados**: La mayoría de oficinas gubernamentales DACH aún requieren documentos físicos; las impresiones PDF de documentos exclusivamente digitales pueden no ser aceptadas sin verificación adicional

## Habilidades Relacionadas

- [plan-eu-relocation](../plan-eu-relocation/SKILL.md) -- Crear el plan de reubicación que alimenta esta verificación de documentos
- [navigate-dach-bureaucracy](../navigate-dach-bureaucracy/SKILL.md) -- Guía detallada para los procedimientos para los cuales estos documentos son necesarios
