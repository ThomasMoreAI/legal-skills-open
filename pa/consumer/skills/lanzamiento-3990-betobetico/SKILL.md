---
name: lanzamiento-3990-betobetico
title: /lanzamiento
description: 'Revisor de lanzamiento de producto — analiza un producto o servicio antes de su lanzamiento al mercado contra la calibración del perfil de práctica. Checklist de etiquetado, garantías, retracto, condiciones generales y publicidad. Clasificación de riesgo: bajo/medio/alto/bloqueo. Usar cuando el usuario diga "vamos a lanzar", "revisión de producto", "¿podemos vender esto?" o "lanzamiento".'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/consumo/skills/lanzamiento
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: consumer
language: es
---

# /lanzamiento

1. Cargar `~/.claude/plugins/config/claude-para-abogados/consumo/CLAUDE.md` → calibración de riesgo, tipo de productos, canal de venta.
2. Recopilar información del producto/servicio.
3. Ejecutar checklist de revisión.
4. Clasificar riesgo por área.
5. Generar informe con hallazgos y acciones.

```
/consumo:lanzamiento
Vamos a lanzar una suscripción mensual de alimentación ecológica con venta
online y envío a domicilio.
```

---

## Propósito

El lanzamiento de un producto o servicio al consumidor final en Panamá requiere cumplir un entramado normativo amplio: desde el etiquetado hasta las condiciones generales de contratación, pasando por el derecho de retracto y la publicidad. La norma central es la Ley 45 de 2007 y la autoridad de aplicación es la ACODECO. Este skill ejecuta la revisión pre-lanzamiento para detectar riesgos antes de que se conviertan en reclamaciones o sanciones.

---

## Checklist de revisión

### 1. Información al consumidor (Ley 45 de 2007)

- [ ] Identidad del proveedor (nombre, RUC, dirección, contacto)
- [ ] Características esenciales del producto/servicio
- [ ] Precio total (impuestos incluidos —ITBMS—, costes adicionales)
- [ ] Procedimientos de pago, entrega y ejecución
- [ ] Existencia del derecho de retracto y condiciones (ventas a distancia) [verificar]
- [ ] Duración del contrato y condiciones de resolución (si aplica)
- [ ] Garantía legal y comercial

### 2. Derecho de retracto en ventas a distancia (Ley 45 de 2007)

| Aspecto | Requisito | ¿Cumple? | Riesgo |
|---|---|---|---|
| Plazo | Plazo legal de retracto desde recepción (bienes) o contratación (servicios) [verificar] | | |
| Información | Formulario o mecanismo de retracto facilitado | | |
| Devolución del precio | Reembolso dentro del plazo legal desde la comunicación del retracto [verificar] | | |
| Costes de devolución | Informar quién los asume | | |
| Excepciones | Identificar si aplica alguna excepción al retracto [verificar] | | |

**Excepciones habituales al retracto:** [verificar]
- Bienes personalizados o confeccionados a medida
- Bienes perecederos o de caducidad rápida
- Bienes precintados no aptos para devolución por salud/higiene (desprecintados)
- Contenido digital sin soporte material (si comenzó la ejecución con consentimiento)
- Servicios completamente ejecutados (con consentimiento previo)

### 3. Garantía legal (Ley 45 de 2007)

| Aspecto | Requisito | ¿Cumple? | Riesgo |
|---|---|---|---|
| Plazo de garantía | Plazo de garantía legal conforme a la Ley 45 de 2007 | | |
| Responsabilidad por defectos | El proveedor responde por bienes/servicios defectuosos [verificar] | | |
| Jerarquía de remedios | Reparación o sustitución → rebaja de precio o resolución | | |
| Información al consumidor | Garantía legal informada claramente | | |

### 4. Etiquetado y presentación

- [ ] Etiquetado conforme a la reglamentación técnica panameña aplicable (alimentación, textil, electrónica, juguetes...) [verificar]
- [ ] Instrucciones en español
- [ ] Información obligatoria del producto visible
- [ ] Cumplimiento de normas técnicas / etiquetado obligatorio si procede [verificar]

### 5. Publicidad

- [ ] Sin claims engañosos (Ley 45 de 2007)
- [ ] Publicidad comparativa conforme (Ley 45 de 2007)
- [ ] Precios completos (impuestos —ITBMS—, gastos de envío)
- [ ] Ofertas y promociones con condiciones claras

### 6. Condiciones generales de contratación

- [ ] Legibilidad y accesibilidad
- [ ] Ausencia de cláusulas abusivas (Ley 45 de 2007)
- [ ] Control de inclusión del contrato de adhesión [verificar]
- [ ] Aceptación expresa del consumidor

---

## Clasificación de riesgo

| Nivel | Significado | Acción |
|---|---|---|
| **Bajo** | Cumple requisitos; ajustes menores recomendables | Proceder con ajustes |
| **Medio** | Gaps identificados que deben corregirse antes del lanzamiento | Corregir en plazo |
| **Alto** | Riesgo de sanción o reclamación significativa | No lanzar sin corregir |
| **Bloqueo** | Incumplimiento grave; riesgo de sanción o retirada del producto | Detener lanzamiento |

---

## Formato de salida

```markdown
# Revisión de lanzamiento: [Producto/Servicio]

**Fecha:** [fecha]
**Canal de venta:** [online / físico / mixto]
**Mercado objetivo:** [Panamá / regional / internacional]

---

## Resultado global: [BAJO / MEDIO / ALTO / BLOQUEO]

---

## Hallazgos por área

| # | Área | Hallazgo | Riesgo | Acción requerida |
|---|---|---|---|---|
| 1 | Retracto | [Ej., No se facilita mecanismo de retracto] | Alto | Incluir mecanismo de retracto (Ley 45 de 2007) |
| 2 | Garantía | [Ej., Web indica un plazo de garantía inferior al legal] | Alto | Ajustar al plazo legal de la Ley 45 de 2007 |
| ... | ... | ... | ... | ... |

---

## Acciones bloqueantes (resolver antes de lanzar)

[Lista de acciones con riesgo Alto o Bloqueo]

---

## Acciones recomendadas (resolver en plazo)

[Lista de acciones con riesgo Medio o Bajo]
```

---

## Legislación de referencia

- Ley 45 de 2007 — normas de protección al consumidor y defensa de la competencia (norma central)
- ACODECO — Autoridad de Protección al Consumidor y Defensa de la Competencia
- Código de Comercio de Panamá — obligaciones de los comerciantes
- Reglamentación técnica panameña de etiquetado y normas técnicas (según sector) [verificar]
- Ley 81 de 2019 — protección de datos personales (para políticas de privacidad)

---

## Lo que este skill NO hace

- No revisa normativa sectorial específica (alimentaria, cosmética, sanitaria) en detalle — marca cuándo es necesaria.
- No valida claims publicitarios — para eso, usar `/consumo:claims`.
- No redacta las condiciones generales — para eso, usar `/consumo:condiciones-generales`.
