---
name: triaje
title: /triaje
description: Triaje de tratamiento de datos — decide si un tratamiento necesita EIPD, consulta previa a la AEPD, o puede proceder directamente. Árbol de decisión basado en art. 35 RGPD + lista obligatoria de la AEPD. Usar cuando el usuario pregunte "¿necesito EIPD?", "¿puedo tratar estos datos?", "nuevo tratamiento" o "¿qué trámites necesito?".
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/privacidad/skills/triaje
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: data-protection
language: en
---

# /triaje

1. Cargar `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md` → criterios de EIPD, proceso, registro de actividades.
2. Recopilar información mínima del tratamiento.
3. Ejecutar el árbol de decisión.
4. Emitir decisión con justificación y siguiente paso.

```
/privacidad:triaje
Queremos usar un algoritmo de scoring para evaluar la solvencia de los
solicitantes de crédito.
```

---

## Propósito

No todo tratamiento requiere una EIPD completa, pero todo tratamiento requiere una evaluación previa de si la EIPD es necesaria. Este skill es el filtro previo: rápido, documentado y con decisión clara sobre el siguiente paso.

---

## Información mínima necesaria

Antes de decidir, necesitar al menos:

1. **¿Qué datos se tratan?** (categorías: identificativos, financieros, salud, biométricos, menores...)
2. **¿A cuántas personas afecta?** (escala: decenas, cientos, miles, millones)
3. **¿Para qué?** (finalidad concreta)
4. **¿Se usa tecnología innovadora?** (IA, biometría, geolocalización sistemática, IoT)
5. **¿Se elaboran perfiles o se toman decisiones automatizadas?**
6. **¿Hay datos de personas vulnerables?** (menores, empleados, pacientes)
7. **¿Hay transferencia internacional?**
8. **¿Hay combinación de conjuntos de datos?**

Si falta información, preguntar antes de decidir.

---

## Árbol de decisión

### Nivel 1: ¿Está en la lista obligatoria de la AEPD?

Si el tratamiento coincide con alguno de los 14 tipos de la lista de la AEPD (2019), la EIPD es **obligatoria**. Pasar directamente a `/privacidad:eipd`.

### Nivel 2: ¿Cumple supuestos del art. 35.3 RGPD?

- **Perfilado con efectos jurídicos/significativos** → EIPD obligatoria
- **Datos especiales a gran escala** (art. 9 o art. 10) → EIPD obligatoria
- **Observación sistemática de zonas públicas a gran escala** → EIPD obligatoria

### Nivel 3: Regla de los dos criterios (CEPD / WP248)

Contar cuántos de los 9 criterios del Grupo de Trabajo del Artículo 29 se cumplen:

| # | Criterio | ¿Cumple? |
|---|---|---|
| 1 | Evaluación o scoring (incluido perfilado) | |
| 2 | Toma de decisiones automatizadas con efectos jurídicos o significativos | |
| 3 | Observación sistemática | |
| 4 | Datos sensibles o altamente personales | |
| 5 | Tratamiento a gran escala | |
| 6 | Asociación o combinación de conjuntos de datos | |
| 7 | Datos de personas vulnerables | |
| 8 | Uso innovador de tecnologías | |
| 9 | Tratamiento que impida ejercer derechos o usar un servicio/contrato | |

- **2 o más criterios** → EIPD obligatoria (recomendación del CEPD)
- **1 criterio** → EIPD recomendable pero no obligatoria; documentar la decisión
- **0 criterios** → Puede proceder sin EIPD; documentar el análisis

### Nivel 4: ¿Procede consulta previa?

Si la EIPD concluye que el riesgo residual es alto tras las medidas de mitigación → **consulta previa a la AEPD** obligatoria (art. 36 RGPD).

---

## Formato de salida

```markdown
# Triaje de tratamiento

**Tratamiento:** [nombre/descripción breve]
**Fecha:** [fecha]

---

## Decisión

| Resultado | Decisión |
|---|---|
| **¿EIPD obligatoria?** | [Sí / No / Recomendable] |
| **¿Consulta previa AEPD?** | [Pendiente de EIPD / No procede / Obligatoria] |
| **¿Puede proceder?** | [Sí / Sí con condiciones / No hasta completar EIPD] |

---

## Justificación

**Lista AEPD:** [Coincide con tipo X / No coincide]
**Art. 35.3 RGPD:** [Cumple supuesto X / No cumple]
**Criterios CEPD cumplidos:** [N] de 9 — [listar cuáles]

---

## Siguiente paso

[Una de las tres opciones:]
1. **Proceder** — documentar este triaje en el RAT y proceder con el tratamiento.
2. **Realizar EIPD** — ejecutar `/privacidad:eipd` con la información recopilada.
3. **Consulta previa** — preparar documentación para la AEPD (art. 36 RGPD).
```

---

## Legislación de referencia

- RGPD art. 35 (evaluación de impacto)
- RGPD art. 36 (consulta previa)
- Lista de tratamientos que requieren EIPD (AEPD, 2019)
- Directrices del CEPD (WP248 rev.01) sobre EIPD y criterios de alto riesgo
- LOPDGDD art. 28 (obligaciones del responsable)

---

## Lo que este skill NO hace

- No realiza la EIPD completa — para eso, usar `/privacidad:eipd`.
- No sustituye el criterio del DPO — la decisión final es suya.
- No tramita la consulta previa ante la AEPD — indica cuándo es necesaria.
