---
name: assess-ip-landscape-pjt222
title: Assess IP Landscape
description: Mapear el panorama de propiedad intelectual para un dominio tecnológico o área de producto. Cubre análisis de clústeres de patentes, identificación de espacios en blanco, evaluación del portafolio de PI de competidores, examen preliminar de libertad de operación, y recomendaciones estratégicas de posicionamiento de PI. Usar antes de iniciar I+D en una nueva área tecnológica, al evaluar la entrada al mercado contra incumbentes con portafolios de patentes fuertes, al preparar la debida diligencia de inversión, al informar una estrategia de solicitud de patentes, o al evaluar el riesgo de libertad de operación para un nuevo producto.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/es/skills/assess-ip-landscape
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: es
---

# Assess IP Landscape

Mapear el panorama de propiedad intelectual para un área tecnológica — identificar clústeres de patentes, espacios en blanco, actores clave y riesgos de libertad de operación. Produce una evaluación estratégica que informa la dirección de I+D, decisiones de licenciamiento y estrategia de solicitud de PI.

## Cuándo Usar

- Antes de iniciar I+D en una nueva área tecnológica (¿qué ya está reclamado?)
- Evaluar la entrada a un mercado donde los incumbentes tienen portafolios de patentes fuertes
- Preparar la debida diligencia de inversión (evaluación de activos de PI)
- Informar una estrategia de solicitud de patentes (dónde solicitar, qué reclamar)
- Evaluar el riesgo de libertad de operación para un nuevo producto o funcionalidad
- Monitorear la actividad de PI de competidores para posicionamiento estratégico

## Entradas

- **Requerido**: Dominio tecnológico o área de producto a evaluar
- **Requerido**: Alcance geográfico (EE.UU., UE, global)
- **Opcional**: Competidores específicos en los que enfocarse
- **Opcional**: Portafolio de patentes propio (para análisis de brechas y FTO)
- **Opcional**: Horizonte temporal (últimos 5 años, últimos 10 años, todo el tiempo)
- **Opcional**: Códigos de clasificación (IPC, CPC) si se conocen

## Procedimiento

### Paso 1: Definir el Alcance de Búsqueda

Establecer los límites del análisis del panorama.

1. Definir el dominio tecnológico con precisión:
   - Área tecnológica central (ej., "modelos de lenguaje basados en transformers" no "IA")
   - Áreas adyacentes a incluir (ej., "mecanismos de atención, tokenización, optimización de inferencia")
   - Áreas a excluir explícitamente (ej., "transformers de visión por computadora" si el enfoque es NLP)
2. Identificar códigos de clasificación relevantes:
   - IPC (Clasificación Internacional de Patentes) — amplia, usada mundialmente
   - CPC (Clasificación Cooperativa de Patentes) — más específica, estándar de EE.UU./UE
   - Buscar en la publicación IPC de WIPO o el navegador CPC de USPTO
3. Definir el alcance geográfico:
   - EE.UU. (USPTO), UE (EPO), WIPO (PCT), oficinas nacionales específicas
   - La mayoría de los análisis comienzan con EE.UU. + UE + PCT para cobertura amplia
4. Establecer la ventana temporal:
   - Actividad reciente: últimos 3-5 años (panorama competitivo actual)
   - Historial completo: 10-20 años (áreas tecnológicas maduras)
   - Buscar patentes expiradas que abren espacio de diseño
5. Documentar el alcance como la **Carta del Panorama**

**Esperado:** Un alcance claro y delimitado que es suficientemente específico para producir resultados accionables pero suficientemente amplio para capturar el panorama competitivo relevante. Códigos de clasificación identificados para búsqueda sistemática.

**En caso de fallo:** Si el dominio tecnológico es demasiado amplio (miles de resultados), reducir agregando especificidad técnica o enfocándose en un área de aplicación específica. Si es demasiado estrecho (pocos resultados), ampliar a tecnologías adyacentes. El alcance correcto típicamente produce 100-1000 familias de patentes.

### Paso 2: Recopilar Datos de Patentes

Recolectar los datos de patentes dentro del alcance definido.

1. Consultar bases de datos de patentes usando la Carta del Panorama:
   - **Bases de datos gratuitas**: Google Patents, USPTO PatFT/AppFT, Espacenet, WIPO Patentscope
   - **Bases de datos comerciales**: Orbit, PatSnap, Derwent, Lens.org (freemium)
   - Combinar búsqueda por palabras clave + códigos de clasificación para la mejor cobertura
2. Construir consultas de búsqueda sistemáticamente:

```text
Query Construction:
+-------------------+------------------------------------------+
| Component         | Example                                  |
+-------------------+------------------------------------------+
| Core keywords     | "language model" OR "LLM" OR "GPT"       |
| Technical terms   | "attention mechanism" OR "transformer"    |
| Classification    | CPC: G06F40/*, G06N3/08                  |
| Date range        | filed:2019-2024                          |
| Assignee filter   | (optional) specific companies            |
+-------------------+------------------------------------------+
```

3. Descargar resultados en formato estructurado (CSV, JSON) incluyendo:
   - Número de patente/solicitud, título, resumen, fecha de solicitud
   - Titular/solicitante, inventor(es)
   - Códigos de clasificación, datos de citación
   - Estado legal (concedida, pendiente, expirada, abandonada)
4. Deduplicar por familia de patentes (agrupar solicitudes nacionales de la misma invención)
5. Registrar el conteo total de familias de patentes y las bases de datos fuente

**Esperado:** Un conjunto de datos estructurado de familias de patentes dentro del alcance, deduplicado y con marcas de tiempo. El conjunto de datos es la base para todo el análisis posterior.

**En caso de fallo:** Si el acceso a bases de datos es limitado, Google Patents + Lens.org (gratis) proporcionan buena cobertura. Si la consulta devuelve demasiados resultados (>5000), agregar especificidad técnica. Si muy pocos (<50), ampliar palabras clave o agregar códigos de clasificación.

### Paso 3: Analizar el Panorama

Mapear los clústeres de patentes, actores clave y tendencias.

1. **Análisis de clústeres**: Agrupar patentes por sub-tecnología:
   - Usar códigos de clasificación o agrupamiento por palabras clave para identificar 5-10 sub-áreas
   - Contar familias de patentes por clúster
   - Identificar qué clústeres están creciendo (oleadas recientes de solicitudes) vs. maduros (planos o en declive)
2. **Análisis de actores clave**: Identificar los 10 principales titulares por:
   - Conteo total de familias de patentes (amplitud del portafolio)
   - Tasa de solicitud reciente (últimos 3 años — actividad actual)
   - Conteo promedio de citaciones (proxy de calidad de patente)
   - Amplitud de solicitud geográfica (solo EE.UU. vs. solicitudes globales)
3. **Análisis de tendencias**: Graficar tendencias de solicitud sobre la ventana temporal:
   - Volumen total de solicitudes por año
   - Volumen de solicitudes por clúster por año
   - Nuevos entrantes (titulares que solicitan por primera vez en el dominio)
4. **Red de citaciones**: Identificar las patentes más citadas (PI fundacional):
   - Altas citaciones hacia adelante = muy dependida por solicitudes posteriores
   - Estas son probablemente patentes bloqueadoras o arte previo esencial
5. Producir el **Mapa del Panorama**: clústeres, actores, tendencias y patentes clave

**Esperado:** Una imagen clara de quién posee qué, dónde se concentra la actividad, y cómo evoluciona el panorama. Patentes bloqueadoras clave identificadas. Espacios en blanco (áreas con pocas solicitudes) visibles.

**En caso de fallo:** Si el conjunto de datos es demasiado pequeño para agrupamiento significativo, combinar clústeres en grupos más amplios. Si un titular domina (>50% de las solicitudes), analizar su portafolio como un sub-panorama separado.

### Paso 4: Identificar Espacios en Blanco y Riesgos

Extraer perspectivas estratégicas del panorama.

1. **Análisis de espacios en blanco** (oportunidades):
   - Áreas tecnológicas dentro del alcance con pocas o ninguna solicitud de patente
   - Familias de patentes expiradas donde el espacio de diseño se ha reabierto
   - Áreas activas donde solo un actor ha solicitado (primer movedor pero sin competencia)
   - Espacios en blanco adyacentes a clústeres en crecimiento (próxima frontera)
2. **Examen de riesgo FTO** (amenazas) — adaptado de la matriz de triaje `heal`:
   - **Crítico**: Patentes concedidas que cubren directamente tu producto/funcionalidad planificado
   - **Alto**: Solicitudes pendientes con probabilidad de concesión con reivindicaciones relevantes
   - **Medio**: Patentes concedidas en áreas adyacentes que podrían interpretarse ampliamente
   - **Bajo**: Patentes expiradas, reivindicaciones estrechas o solicitudes geográficamente irrelevantes
3. **Posicionamiento competitivo**:
   - ¿Dónde se sitúa tu portafolio (si existe) respecto a los competidores?
   - ¿Qué competidores tienen posiciones bloqueadoras en tus áreas objetivo?
   - ¿Qué competidores podrían estar interesados en licencias cruzadas?
4. Producir la **Evaluación Estratégica**: espacios en blanco, riesgos FTO, posicionamiento y recomendaciones

**Esperado:** Recomendaciones estratégicas accionables: dónde solicitar, qué evitar, a quién vigilar y qué riesgos necesitan análisis detallado de FTO.

**En caso de fallo:** Si se identifican riesgos de FTO, este examen es preliminar — NO reemplaza una opinión formal de FTO de un abogado de patentes. Señalar riesgos críticos para revisión legal. Si los espacios en blanco parecen demasiado buenos (un área valiosa sin solicitudes), verificar que el alcance de búsqueda no excluyó accidentalmente solicitudes relevantes.

### Paso 5: Documentar y Recomendar

Empaquetar la evaluación del panorama para los tomadores de decisiones.

1. Escribir el **Informe del Panorama** con secciones:
   - Resumen ejecutivo (1 página: hallazgos clave, principales riesgos, recomendaciones principales)
   - Alcance y metodología (términos de búsqueda, bases de datos, rango de fechas)
   - Visión general del panorama (clústeres, tendencias, actores clave con visualizaciones)
   - Análisis de espacios en blanco (oportunidades clasificadas por valor estratégico)
   - Evaluación de riesgos (preocupaciones de FTO clasificadas por severidad)
   - Recomendaciones (estrategia de solicitud, objetivos de licenciamiento, alertas de monitoreo)
2. Incluir datos de soporte:
   - Lista de familias de patentes (estructurada, ordenable)
   - Mapa de clústeres (visual)
   - Gráficos de tendencias de solicitud
   - Resúmenes de patentes clave (las 10-20 patentes más relevantes)
3. Configurar monitoreo continuo:
   - Definir consultas de alerta para nuevas solicitudes en áreas críticas
   - Establecer cadencia de revisión (trimestral para áreas activas, anual para estables)

**Esperado:** Un informe de panorama completo que permite decisiones estratégicas de PI. El informe está basado en evidencia, claramente delimitado y es accionable.

**En caso de fallo:** Si el informe es demasiado extenso, producir primero el resumen ejecutivo y ofrecer secciones detalladas bajo demanda. El resumen ejecutivo siempre debe ser autosuficiente como documento de decisión.

## Validación

- [ ] La Carta del Panorama define alcance, clasificación, geografía y ventana temporal
- [ ] Conjunto de datos de patentes recopilado de múltiples bases de datos y deduplicado
- [ ] Clústeres identificados con conteos de solicitudes y dirección de tendencia
- [ ] Los 10 principales actores clave perfilados con métricas de portafolio
- [ ] Espacios en blanco identificados y clasificados por valor estratégico
- [ ] Riesgos de FTO examinados y clasificados por severidad
- [ ] Patentes bloqueadoras clave identificadas con análisis de citaciones
- [ ] Las recomendaciones son específicas y accionables
- [ ] Limitaciones reconocidas (examen preliminar vs. opinión formal de FTO)
- [ ] Alertas de monitoreo definidas para seguimiento continuo del panorama

## Errores Comunes

- **Alcance demasiado amplio**: "Patentes de IA" no es un panorama — es un océano. Ser específico sobre la tecnología y la aplicación
- **Dependencia de una sola base de datos**: Ninguna base de datos de patentes tiene cobertura completa. Usar al menos dos fuentes
- **Ignorar familias de patentes**: Contar solicitudes individuales en lugar de familias infla los números. Una invención solicitada en 10 países es una familia de patentes, no diez
- **Confundir solicitudes con concesiones**: Una solicitud pendiente no es un derecho ejecutable. Distinguir entre patentes concedidas y solicitudes publicadas
- **Mala interpretación de espacios en blanco**: Un área vacía podría significar "nadie lo intentó" o "todos lo intentaron y fallaron." Investigar antes de asumir oportunidad
- **Panorama como opinión legal**: Esta habilidad produce inteligencia estratégica, no asesoría legal. Los riesgos de FTO señalados aquí necesitan análisis formal por parte de un abogado de patentes

## Habilidades Relacionadas

- `search-prior-art` — Búsqueda detallada de arte previo para invenciones específicas o desafíos de validez de patentes
- `security-audit-codebase` — La metodología de evaluación de riesgos es paralela al examen de riesgos de PI
- `review-research` — Las habilidades de revisión de literatura se aplican al análisis de arte previo
- `conduct-gxp-audit` — La metodología de auditoría es paralela a la documentación sistemática del panorama de PI
- `screen-trademark` — cribado de conflictos de marcas y análisis de distintividad para el lado de marcas de los paisajes de PI
- `file-trademark` — procedimientos de registro de marcas para la EUIPO, la USPTO y el Protocolo de Madrid
