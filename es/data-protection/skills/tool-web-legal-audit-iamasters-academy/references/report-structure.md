# Estructura del informe .docx

Usa esta estructura exacta. El script `scripts/generate-docx.mjs` la implementa; si lo modificas, mantén las secciones.

## Secciones

1. **Portada**
   - Título "Auditoría Legal y de Cumplimiento"
   - Subtítulo con las normas cubiertas
   - Nombre del sitio / organización auditada
   - Fecha de la auditoría
   - Metodología: "análisis black-box (sin acceso al código fuente)"

2. **Resumen ejecutivo**
   - URLs auditadas (lista)
   - Agravantes económicos si los hay (cifra + relevancia)
   - Tabla-semáforo por URL con nivel de riesgo RGPD, LSSI, Cookies

3. **Metodología y alcance**
   - Herramientas usadas
   - Qué se pudo verificar externamente y qué no

4. **Secciones por URL** (una por cada URL)
   - Descripción funcional y stack
   - Copy relevante (citas textuales)
   - Formulario y datos tratados
   - Hallazgos de cumplimiento (tabla)
   - Trackers detectados (tabla)
   - Encuadre normativo específico

5. **Comparativa entre URLs** (si hay más de una)

6. **Riesgo sancionador**
   - Horquillas legales por norma
   - Precedentes AEPD relevantes
   - Escenarios conservador / medio / agravado por URL y agregado

7. **Recomendaciones y plan de acción**
   - Por URL (críticas/altas/medias)
   - Transversales (RAT, contratos encargado, EIPD, etc.)

8. **Anexo técnico — evidencias**
   - Peticiones de red literales por URL
   - Campos de formularios
   - Citas textuales de políticas detectadas
   - URLs rotas detectadas

9. **Sección de alerta legal consolidada** (opcional pero recomendada)
   - Tabla con todas las normas incumplidas
   - Horquillas aplicables
   - Precedentes reales
   - Escenario de exposición económica
   - Otros riesgos asociados
   - Urgencia

10. **Nota final**
    - Limitaciones del black-box
    - Documentación que requiere aportar el responsable

## Tonos

- Portada y secciones técnicas: neutro
- Sección de alerta: directa, con énfasis en color rojo (C00000) para los agravantes
- Nunca sensacionalista ni especulativo

## Detalles de formato

- Papel A4 (11906 × 16838 DXA)
- Margen 1440 DXA (1 pulgada)
- Fuente Calibri 11pt body, headings en azul corporativo (1F3864 / 2E74B5)
- Numeración en pie de página: "Página X de Y"
- Header: texto gris pequeño con el título del informe + "Confidencial"
- Tablas con bordes suaves, header con fondo azul y texto blanco
- Citas literales en blockquote con borde izquierdo rojo

## Personalización

Cuando llames a `generate-docx.mjs`, pasa el JSON de findings. El script adapta el contenido pero mantiene estructura y estilo.
