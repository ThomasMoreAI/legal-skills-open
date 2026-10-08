# DPIA — Data Protection Impact Assessment

## ¿Cuándo es obligatoria? (Art. 35)

Si el procesamiento de datos personales puede resultar en **alto riesgo** para los derechos y libertades de las personas.

### Trigger de DPIA (si alguno aplica → DPIA obligatoria)

| Trigger | ¿Tu proyecto lo tiene? |
|--|--|
| Monitorización sistemática a gran escala (CCTV, tracking de comportamiento) | ☐ |
| Tratamiento a gran escala de datos sensibles (salud, biometría, orientación sexual) | ☐ |
| Perfiles automatizados con efectos legales o significativos (crédito, empleo, seguros) | ☐ |
| Reconocimiento facial o biométrico a gran escala | ☐ |
| Datos de menores a gran escala | ☐ |
| Combina conjuntos de datos a gran escala | ☐ |
| Uso de tecnología nueva a gran escala | ☐ |
| Tratamiento que impida a las personas ejercer sus derechos | ☐ |

### Exenciones (NO necesita DPIA)

- Datos seudonimizados o encriptados a pequeña escala
- Datos de contacto de clientes para facturación
- Datos públicos de contactos comerciales (B2B)
- Procesamiento con base legal de obligación legal

---

## Template DPIA

Usa este template como comentario al inicio del archivo que implementa el procesamiento:

```typescript
/**
 * DPIA — Data Protection Impact Assessment
 * ==========================================
 * Project: [nombre del sistema]
 * Version: 1.0
 * Date: [fecha]
 * Author: [nombre]
 *
 * ---
 * Article 35 GDPR — Evaluation of processing likely to result in high risk
 * ---
 *
 * 1. Descripción del tratamiento
 * ===============================
 * Responsable: [nombre, contacto del DPO si aplica]
 * Finalidad: [por qué se procesan los datos personales]
 * Datos personales: [qué datos específicos se recogen]
 * Categoría de interesados: [quienes son los sujetos de los datos]
 * Base legal: [Art. 6(1)(X)]
 * Destinatarios: [a quién se comparten los datos]
 * Transferencias internacionales: [sí/no, a dónde, garantías]
 * Retención: [cuánto tiempo, criterio de eliminación]
 *
 * 2. Necesidad y proporcionalidad
 * ================================
 * ¿El tratamiento es necesario para la finalidad declarada?
 *   [sí/no + justificación]
 *
 * ¿Existen alternativas menos intrusivas?
 *   [sí/no + listar alternativas consideradas]
 *
 * ¿Se minimizan los datos al mínimo necesario?
 *   [sí/no + cómo se aplica el principio de minimización]
 *
 * 3. Evaluación de riesgos
 * =========================
 * Para cada riesgo identificado, evaluar probabilidad y severidad:
 *   Probabilidad: Bajo / Medio / Alto
 *   Severidad: Bajo / Medio / Alto / Crítico
 *
 * | Riesgo | Probabilidad | Severidad | Descripción |
 * |--------|------|------|----|
 * | [ej: Acceso no autorizado] | [B/M/A] | [B/M/A/C] | [descripción] |
 * | [ej: Discriminación algorítmica] | [B/M/A] | [B/M/A/C] | [descripción] |
 * | [ej: Revelación de datos sensibles] | [B/M/A] | [B/M/A/C] | [descripción] |
 *
 * 4. Medidas de mitigación
 * =========================
 * Para cada riesgo, indicar los controles existentes o a implementar:
 *
 * | Riesgo | Control | Implementación | Responsable | Deadline |
 * |--------|---------|--------------|------|--------|
 * | [ej: Acceso no autorizado] | Cifrado | AES-256 en reposo, TLS 1.3 en tránsito | [nombre] | [fecha] |
 * | [ej: Discriminación] | Auditorías | Revisiones trimestrales de sesgo | [nombre] | [fecha] |
 * | [ej: Revelación] | Acceso mínimo | RBAC + logging de acceso | [nombre] | [fecha] |
 *
 * 5. Consulta a interesados (si aplica)
 * ======================================
 * ¿Se han consultado los interesados o sus representantes? [sí/no]
 * [Resultados de la consulta]
 *
 * 6. Conclusión
 * =============
 * ¿El riesgo residual es aceptable tras las medidas de mitigación?
 *   [sí/no]
 *
 * Si NO → Se requiere consulta previa con la autoridad de control
 * (Art. 36 — consultar AEPD en España)
 *
 * ¿Se revisará esta DPIA periódicamente? [sí/no, frecuencia]
 *
 * Firmado por: ___________________  Fecha: _______
 */
```

---

## Relación con el AI Act

### Sobreposición con Fundamental Rights Impact Assessment

Si tu sistema activa **ambas** regulaciones (IA + datos personales), puedes usar **una sola evaluación** que cubra ambas obligaciones:

| Obligation | GDPR Art. 35 (DPIA) | AI Act Art. 27 (FRIA) |
|--|--|------|
| Descripción del sistema | ✅ Sección 1 | ✅ |
| Análisis de riesgos | ✅ Sección 3 | ✅ |
| Medidas de mitigación | ✅ Sección 4 | ✅ |
| Evaluación de impacto en derechos | ✅ Sección 3 | ✅ |
| Consulta a autoridades | ✅ Art. 36 | ✅ |
| Documentación | ✅ | ✅ |
| Actualización periódica | ✅ | ✅ |

**Puedes fusionar ambas en un solo documento** si incluyes todos los puntos de ambas.

---

## Frecuencia de actualización

| Trigger | ¿Actualizar DPIA? |
|--|------|
| Cambio en la finalidad del tratamiento | **Sí** |
| Nuevo tipo de dato personal | **Sí** |
| Nuevo destinatario de datos | **Sí** |
| Cambio tecnológico significativo | **Sí** |
| Nueva amenaza de seguridad | **Sí** |
| Revisión periódica | **Cada 12 meses mínimo** |
| Queja de interesado sobre privacidad | **Sí** |

---

## Proceso completo DPIA

```
¿El procesamiento implica alto riesgo?
  ├── No → No necesitas DPIA
  └── Sí
      ├── 1. Documentar el tratamiento (Sección 1-2)
      ├── 2. Identificar y evaluar riesgos (Sección 3)
      ├── 3. Definir medidas de mitigación (Sección 4)
      ├── 4. Consultar interesados (Sección 5, si aplica)
      ├── 5. Evaluar riesgo residual (Sección 6)
      ├── 6. Si riesgo NO aceptable → Consultar autoridad (AEPD)
      └── 7. Implementar y monitorizar
```

---

## Recursos

- [Art. 35 GDPR — Evaluación de impacto](https://www.twobirds.com/-/media/new-website-content/pdfs/capabilities/artificial-intelligence/european-union-artificial-intelligence-act-guide.pdf)
- [Guía AEPD sobre DPIA](https://www.aepd.es/es/guias-y-recomendaciones/guias-proteccion-datos)
- [EDPB Guidelines on DPIA](https://www.edpb.europa.eu/edpb-secretariat/plenaries/plenary-04-2020/es)
