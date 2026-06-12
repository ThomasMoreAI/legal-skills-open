---
name: compliance-check
title: Verificación de cumplimiento normativo
description: 'Usar para verificar cumplimiento RGPD, NIS2 y CRA. También: verificar RGPD, cumplimiento normativo, NIS2, CRA, Cyber Resilience Act, protección de datos, regulación europea.'
author: 686f6c61
author_url: https://github.com/686f6c61/alfred-dev/tree/main/skills/seguridad/compliance-check
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: eu
practice: regulatory
language: es
---

# Verificación de cumplimiento normativo

## Resumen

Este skill evalúa el proyecto contra tres marcos regulatorios europeos fundamentales: RGPD (protección de datos), NIS2 (ciberseguridad de infraestructuras) y CRA (Cyber Resilience Act, seguridad de productos con elementos digitales). El resultado es un informe de conformidad con el estado actual del proyecto frente a cada requisito y las acciones necesarias para alcanzar el cumplimiento.

No se trata de un dictamen jurídico, sino de una evaluación técnica que identifica las lagunas y orienta las acciones de desarrollo necesarias.

## Proceso

1. **Determinar qué normativas aplican.** No todos los proyectos están sujetos a las tres:

   - **RGPD:** aplica si el software trata datos personales de personas en la UE.
   - **NIS2:** aplica si la organización opera en sectores críticos o es proveedor de servicios digitales.
   - **CRA:** aplica a productos con elementos digitales comercializados en la UE (incluyendo software open source con uso comercial).

2. **Checklist RGPD:**

   - [ ] Base jurídica para el tratamiento de datos (consentimiento, interés legítimo, contrato, etc.).
   - [ ] Minimización de datos: solo se recogen los datos estrictamente necesarios.
   - [ ] Evaluación de impacto (DPIA) para tratamientos de alto riesgo.
   - [ ] Registro de actividades de tratamiento documentado.
   - [ ] Derecho de acceso: el usuario puede consultar sus datos.
   - [ ] Derecho de rectificación: el usuario puede corregir sus datos.
   - [ ] Derecho al olvido: el usuario puede solicitar la eliminación de sus datos.
   - [ ] Portabilidad: el usuario puede exportar sus datos en formato estándar.
   - [ ] Notificación de brechas en 72 horas.
   - [ ] Cifrado de datos personales en tránsito y en reposo.
   - [ ] Delegado de Protección de Datos (DPO) designado si aplica.

3. **Checklist NIS2:**

   - [ ] Gestión de riesgos de ciberseguridad documentada.
   - [ ] Política de seguridad de la información aprobada por la dirección.
   - [ ] Notificación de incidentes: alerta temprana en 24h, informe completo en 72h.
   - [ ] Seguridad de la cadena de suministro: evaluación de proveedores.
   - [ ] Gobernanza: responsabilidades de ciberseguridad asignadas.
   - [ ] Plan de continuidad de negocio y recuperación ante desastres.
   - [ ] Formación en ciberseguridad para el personal.
   - [ ] Gestión de vulnerabilidades y actualizaciones.
   - [ ] Autenticación multifactor para accesos críticos.

4. **Checklist CRA (Cyber Resilience Act):**

   - [ ] SBOM (Software Bill of Materials) generado y mantenido.
   - [ ] Actualizaciones de seguridad disponibles durante todo el ciclo de vida.
   - [ ] Diseño seguro por defecto (secure by default).
   - [ ] Documentación técnica del producto disponible.
   - [ ] Gestión de vulnerabilidades con proceso de reporte.
   - [ ] Notificación de vulnerabilidades activamente explotadas en 24h a ENISA.
   - [ ] Evaluación de conformidad (autoevaluación o certificación según categoría).
   - [ ] Marcado CE para productos conformes.

5. **Generar informe de conformidad.** Para cada requisito: estado (cumple/no cumple/parcial), evidencia, acciones necesarias y prioridad.

## Criterios de éxito

- Se han identificado las normativas aplicables al proyecto.
- Cada checklist se ha revisado punto por punto con estado documentado.
- Las acciones necesarias están priorizadas por riesgo e impacto.
- El informe es accionable: un desarrollador puede tomar cada acción y ejecutarla.
- El estado de cumplimiento se ha registrado en la memoria del proyecto.

## Paso final: registro en memoria

Registrar el estado de cumplimiento en la memoria del proyecto con `memory_log_decision` para seguimiento entre sesiones. Esto permite comparar la evolución del cumplimiento a lo largo del tiempo y detectar regresiones normativas.

## Nota de versión

Este skill se basa en RGPD (Reglamento 2016/679), NIS2 (Directiva 2022/2555) y CRA (Reglamento 2024/2847). Verificar si han entrado en vigor actualizaciones posteriores a estas referencias antes de dar por válida la evaluación.

## Qué NO hacer

- No tratar esta evaluación como sustituto de asesoría legal. Es una evaluación técnica que identifica lagunas, pero las decisiones jurídicas requieren un profesional cualificado.
- No marcar un requisito como cumplido sin evidencia técnica que lo respalde (código, configuración, documentación verificable).
- No ignorar el CRA por tratarse de software open source. El CRA aplica a OSS con uso comercial; la exención solo cubre al software libre sin ánimo de lucro ni actividad comercial.
- No dar por cerrada la evaluación sin documentar los requisitos que no aplican y la justificación de por qué no aplican.
