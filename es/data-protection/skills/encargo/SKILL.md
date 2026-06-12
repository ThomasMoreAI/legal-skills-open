---
name: encargo
title: /encargo
description: Revisor de encargos de tratamiento — revisa un contrato de encargado del tratamiento contra el playbook configurado (como responsable o como encargado). Comprueba las cláusulas obligatorias del art. 28 RGPD, identifica gaps y genera tabla de cláusulas con posición, contrato y recomendación. Usar cuando el usuario diga "revisa este encargo", "DPA del proveedor", "contrato de encargado" o adjunte un DPA.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/privacidad/skills/encargo
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: es
practice: data-protection
language: es
---

# /encargo

1. Cargar `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md` → playbook de encargos.
2. Obtener el contrato. Determinar dirección: ¿somos responsable o encargado? Preguntar si es ambiguo.
3. Revisar cláusula por cláusula contra el playbook.
4. Comprobar coherencia con la política de privacidad.
5. Generar memo de revisión con tabla de cláusulas.

```
/privacidad:encargo contrato-encargo-proveedor.pdf
```

---

## Propósito

Los encargos de tratamiento llegan en dos direcciones y la revisión es casi opuesta para cada una. Cuando un cliente nos envía su contrato, defendemos flexibilidad operativa. Cuando enviamos uno a un proveedor, protegemos los datos. Este skill aplica la mitad correcta del playbook.

---

## Dirección: ¿responsable o encargado?

Antes de nada, establecer:

- **Somos responsable** → revisamos contrato de nuestro encargado/proveedor → fila "como responsable" del playbook
- **Somos encargado** → un cliente nos envía su contrato → fila "como encargado" del playbook

Si no queda claro, preguntar. Invertir la dirección invierte cada recomendación.

---

## Cláusulas obligatorias art. 28 RGPD

Verificar que el contrato incluye **todas** las cláusulas obligatorias:

| # | Cláusula obligatoria | Art. 28 RGPD | ¿Presente? | Observaciones |
|---|---|---|---|---|
| 1 | Objeto, duración, naturaleza y finalidad del tratamiento | 28.3 | | |
| 2 | Tipo de datos y categorías de interesados | 28.3 | | |
| 3 | Tratar solo siguiendo instrucciones documentadas del responsable | 28.3.a | | |
| 4 | Confidencialidad del personal autorizado | 28.3.b | | |
| 5 | Medidas de seguridad art. 32 RGPD | 28.3.c | | |
| 6 | Régimen de subencargados | 28.3.d, 28.2 | | |
| 7 | Asistencia al responsable en derechos de los interesados | 28.3.e | | |
| 8 | Asistencia en EIPD y consulta previa | 28.3.f | | |
| 9 | Devolución o supresión de datos al finalizar | 28.3.g | | |
| 10 | Poner a disposición información para auditoría | 28.3.h | | |

---

## Revisión término por término

Para cada término, comparar lo que dice el contrato con la posición del playbook:

| Término | Posición playbook | Lo que dice el contrato | Gap | Riesgo | Recomendación |
|---|---|---|---|---|---|
| **Subencargados** | [del playbook] | | | | |
| **Transferencias internacionales** | [del playbook] | | | | |
| **Notificación de brechas** | [del playbook] | | | | |
| **Derecho de auditoría** | [del playbook] | | | | |
| **Devolución/destrucción** | [del playbook] | | | | |
| **Responsabilidad** | [del playbook] | | | | |
| **Medidas de seguridad** | [del playbook] | | | | |
| **Localización de datos** | [del playbook] | | | | |

### Puntos críticos como responsable (revisión protectora)

| Cláusula | Gap habitual | Acción |
|---|---|---|
| Sin lista de subencargados | No sabemos quién trata los datos | Exigir lista + notificación previa |
| "Medidas de seguridad adecuadas" sin anexo | Promesa vacía | Exigir anexo con controles o referencia a ISO 27001 / SOC 2 |
| Sin plazo de notificación de brechas | Nos avisan cuando quieren | Exigir plazo concreto (ej. 24-48h) dentro de las 72h del art. 33 RGPD |
| Proveedor usa datos para "mejora del servicio" | Posible tratamiento para fines propios | Eliminar; tratamiento limitado a las instrucciones del responsable |
| Sin mecanismo de transferencia internacional | Transferencia ilícita | Exigir CCT / decisión de adecuación / BCR |
| Sin compromiso de supresión | Datos retenidos indefinidamente | Exigir supresión + certificado al finalizar |

### Puntos críticos como encargado (revisión defensiva)

| Cláusula | Riesgo | Acción |
|---|---|---|
| Derecho de veto sobre subencargados | Bloquea cambios de infraestructura | Negociar autorización general con derecho de oposición |
| Auditoría presencial sin preaviso | Inviable a escala | Limitar a informes independientes + presencial con preaviso razonable |
| Notificación de brechas <24h | Antes de saber qué ha pasado | Negociar "sin dilación indebida" con plazo razonable |
| Responsabilidad ilimitada como encargado | Riesgo existencial | Someter a cap del contrato principal |
| Supresión en plazos muy cortos | Backups y logs lo impiden | Documentar carveout de rotación de backups |

---

## Comprobación de coherencia con política de privacidad

- Si el encargo limita el tratamiento a fines X, Y, Z → ¿la política de privacidad los recoge?
- Si la política dice "no vendemos datos" → ¿alguna cláusula del encargo parece una cesión?
- Si la política nombra categorías de encargados → ¿coincide con la lista de subencargados?

Marcar desajustes — normalmente es la política la que está desactualizada.

---

## Formato de salida

```markdown
# Revisión de encargo de tratamiento: [Contraparte]

**Dirección:** [Somos responsable / Somos encargado]
**Fecha de revisión:** [fecha]
**Vinculado a:** [contrato principal / standalone]

---

## Conclusión

[Dos frases. ¿Se puede firmar? ¿Qué debe cambiar?]

**Hallazgos:** [N] Conforme [N] Riesgo medio [N] Riesgo alto [N] Bloqueante

---

## Tabla de cláusulas

| Cláusula | Posición playbook | Contrato | Gap | Riesgo | Recomendación |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

---

## Coherencia con política de privacidad

[Conforme | Desajustes: lista]

---

## Redlines recomendados

[Consolidado — listo para enviar]

---

## Si no aceptan

[Para cada issue: el fallback del playbook o escalado]
```

---

## Legislación de referencia

- RGPD art. 28 (encargado del tratamiento — cláusulas obligatorias)
- RGPD art. 32 (seguridad del tratamiento)
- RGPD art. 33 (notificación de brechas — 72h)
- RGPD arts. 44-49 (transferencias internacionales)
- LOPDGDD arts. 33-35 (encargado del tratamiento)
- Guía de la AEPD sobre contratos de encargado del tratamiento
- Cláusulas contractuales tipo de la Comisión Europea (Decisión 2021/914)

---

## Lo que este skill NO hace

- No redacta un encargo de tratamiento desde cero — para eso, usar la plantilla house de los documentos semilla.
- No realiza la evaluación de impacto de transferencias (TIA) — marca cuándo es necesaria.
- No decide si aceptar términos fuera del playbook — escala según la tabla de escalado.
