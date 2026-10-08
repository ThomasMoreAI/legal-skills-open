---
name: triaje-privacidad-betobetico
title: /triaje
description: Triaje de tratamiento de datos — decide si conviene realizar una EIPD (voluntaria, salvo que la ANTAI la ordene) o si puede proceder directamente. Árbol de decisión basado en la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021. Usar cuando el usuario pregunte "¿necesito EIPD?", "¿puedo tratar estos datos?", "nuevo tratamiento" o "¿qué trámites necesito?".
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/privacidad/skills/triaje
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: data-protection
language: es
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

### Nivel 1: ¿La EIPD es obligatoria?

En Panamá la EIPD **NO es obligatoria con carácter general** para los tratamientos de alto riesgo (no rige el modelo del art. 35 del RGPD). Es una **buena práctica voluntaria** del responsable (art. 8 de la Ley 81 de 2019) y **solo deviene exigible si la ANTAI la ordena** (art. 41 del Decreto Ejecutivo 285 de 2021). No existe una lista cerrada de "supuestos de alto riesgo" que obliguen a EIPD: el Decreto Ejecutivo 285 de 2021 fija **9 factores de evaluación del riesgo (art. 36)**.

### Nivel 2: Factores de riesgo a valorar (art. 36 del Decreto Ejecutivo 285 de 2021)

- **Perfilado con efectos jurídicos/significativos** → EIPD muy recomendable
- **Datos sensibles a gran escala** → EIPD muy recomendable
- **Observación sistemática de zonas públicas a gran escala** → EIPD muy recomendable

### Nivel 3: Conteo de factores de riesgo (art. 36 del Decreto Ejecutivo 285 de 2021)

Contar cuántos de los factores de riesgo se cumplen:

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

- **2 o más factores** → EIPD muy recomendable; documentar la decisión
- **1 factor** → EIPD recomendable; documentar la decisión
- **0 factores** → Puede proceder sin EIPD; documentar el análisis

En todo caso, la ANTAI puede ordenar la realización de una EIPD en función de la gravedad del riesgo o la novedad tecnológica (art. 41 del Decreto Ejecutivo 285 de 2021).

### Nivel 4: Riesgo residual

Si la EIPD concluye que el riesgo residual sigue siendo alto tras las medidas de mitigación, refuerza las medidas y documéntalo. En Panamá **NO existe** la "consulta previa" a la ANTAI del art. 36 del RGPD; lo que sí puede ocurrir es que la ANTAI ordene una EIPD (art. 41 del Decreto Ejecutivo 285 de 2021).

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
| **¿EIPD recomendable?** | [Muy recomendable / Recomendable / No necesaria] (voluntaria, salvo orden de la ANTAI ex art. 41 del Decreto Ejecutivo 285 de 2021) |
| **¿Puede proceder?** | [Sí / Sí con condiciones / Sí, completando antes la EIPD recomendada] |

---

## Justificación

**Factores de riesgo (art. 36 del Decreto Ejecutivo 285 de 2021):** [N] de 9 — [listar cuáles]

---

## Siguiente paso

[Una de las dos opciones:]
1. **Proceder** — documentar este triaje en el RAT y proceder con el tratamiento.
2. **Realizar EIPD** — ejecutar `/privacidad:eipd` con la información recopilada (recordando que la EIPD es voluntaria, salvo que la ANTAI la ordene ex art. 41 del Decreto Ejecutivo 285 de 2021).
```

---

## Legislación de referencia

- Ley 81 de 2019, art. 8 — la EIPD es una buena práctica voluntaria del responsable
- Decreto Ejecutivo 285 de 2021 — reglamento de la Ley 81 de 2019 (art. 36: factores de evaluación del riesgo; art. 41: la ANTAI puede ordenar la EIPD)
- Guías y resoluciones de la ANTAI sobre evaluaciones de impacto
- Referencia comparada (no vinculante en Panamá): directrices del CEPD (WP248 rev.01) sobre criterios de alto riesgo, como criterio internacional orientativo

---

## Lo que este skill NO hace

- No realiza la EIPD completa — para eso, usar `/privacidad:eipd`.
- No sustituye el criterio del encargado de protección de datos — la decisión final es suya.
- No tramita consultas previas ante la ANTAI (esa figura del RGPD no existe en Panamá); indica cuándo la ANTAI podría ordenar una EIPD (art. 41 del Decreto Ejecutivo 285 de 2021).
