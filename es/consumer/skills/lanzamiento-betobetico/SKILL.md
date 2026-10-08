---
name: lanzamiento-betobetico
title: /lanzamiento
description: 'Revisor de lanzamiento de producto — analiza un producto o servicio antes de su lanzamiento al mercado contra la calibración del perfil de práctica. Checklist de etiquetado, garantías, desistimiento, condiciones generales y publicidad. Clasificación de riesgo: bajo/medio/alto/bloqueo. Usar cuando el usuario diga "vamos a lanzar", "revisión de producto", "¿podemos vender esto?" o "lanzamiento".'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/consumo/skills/lanzamiento
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
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

El lanzamiento de un producto o servicio al consumidor final en España requiere cumplir un entramado normativo amplio: desde el etiquetado hasta las condiciones generales de contratación, pasando por el derecho de desistimiento y la publicidad. Este skill ejecuta la revisión pre-lanzamiento para detectar riesgos antes de que se conviertan en reclamaciones o sanciones.

---

## Checklist de revisión

### 1. Información precontractual (art. 60 LGDCU)

- [ ] Identidad del empresario (nombre, CIF, dirección, contacto)
- [ ] Características esenciales del producto/servicio
- [ ] Precio total (impuestos incluidos, costes adicionales)
- [ ] Procedimientos de pago, entrega y ejecución
- [ ] Existencia del derecho de desistimiento y condiciones
- [ ] Duración del contrato y condiciones de resolución (si aplica)
- [ ] Garantía legal y comercial

### 2. Derecho de desistimiento (arts. 102-108 LGDCU)

| Aspecto | Requisito | ¿Cumple? | Riesgo |
|---|---|---|---|
| Plazo | 14 días naturales desde recepción (bienes) o contratación (servicios) | | |
| Información | Formulario modelo de desistimiento facilitado | | |
| Devolución del precio | 14 días desde comunicación del desistimiento | | |
| Costes de devolución | Informar quién los asume | | |
| Excepciones | Identificar si aplica alguna del art. 103 LGDCU | | |

**Excepciones habituales al desistimiento (art. 103 LGDCU):**
- Bienes personalizados o confeccionados a medida
- Bienes perecederos o de caducidad rápida
- Bienes precintados no aptos para devolución por salud/higiene (desprecintados)
- Contenido digital sin soporte material (si comenzó la ejecución con consentimiento)
- Servicios completamente ejecutados (con consentimiento previo)

### 3. Garantía legal (arts. 114-126 LGDCU)

| Aspecto | Requisito | ¿Cumple? | Riesgo |
|---|---|---|---|
| Plazo de garantía | 3 años desde entrega (bienes nuevos); 1 año (segunda mano, mín.) | | |
| Presunción de falta de conformidad | 2 años desde entrega: carga de prueba en vendedor | | |
| Jerarquía de remedios | Reparación o sustitución → rebaja de precio o resolución | | |
| Información al consumidor | Garantía legal informada claramente | | |

### 4. Etiquetado y presentación

- [ ] Etiquetado conforme a normativa sectorial (alimentación, textil, electrónica, juguetes...)
- [ ] Instrucciones en castellano
- [ ] Información obligatoria del producto visible
- [ ] Marcado CE si procede

### 5. Publicidad

- [ ] Sin claims engañosos (LCD art. 5)
- [ ] Publicidad comparativa conforme (LCD art. 10)
- [ ] Precios completos (impuestos, gastos de envío)
- [ ] Ofertas y promociones con condiciones claras

### 6. Condiciones generales de contratación

- [ ] Legibilidad y accesibilidad
- [ ] Ausencia de cláusulas abusivas (arts. 82-91 LGDCU)
- [ ] Control de inclusión (LCGC art. 5)
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
**Mercado objetivo:** [España / UE / internacional]

---

## Resultado global: [BAJO / MEDIO / ALTO / BLOQUEO]

---

## Hallazgos por área

| # | Área | Hallazgo | Riesgo | Acción requerida |
|---|---|---|---|---|
| 1 | Desistimiento | [Ej., No se facilita formulario modelo] | Alto | Incluir formulario art. 102 |
| 2 | Garantía | [Ej., Web indica garantía de 2 años] | Alto | Actualizar a 3 años |
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

- LGDCU (RDL 1/2007) — Ley General para la Defensa de los Consumidores y Usuarios
- LCD (Ley 3/1991) — Ley de Competencia Desleal
- LCGC (Ley 7/1998) — Ley sobre Condiciones Generales de la Contratación
- LSSI-CE (Ley 34/2002) — comercio electrónico
- Directiva 2011/83/UE — derechos de los consumidores
- Directiva (UE) 2019/2161 — modernización de la protección de consumidores

---

## Lo que este skill NO hace

- No revisa normativa sectorial específica (alimentaria, cosmética, sanitaria) en detalle — marca cuándo es necesaria.
- No valida claims publicitarios — para eso, usar `/consumo:claims`.
- No redacta las condiciones generales — para eso, usar `/consumo:condiciones-generales`.
