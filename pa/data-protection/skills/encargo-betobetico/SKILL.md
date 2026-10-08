---
name: encargo-betobetico
title: /encargo
description: Revisor de encargos de tratamiento — revisa un contrato de encargado del tratamiento contra el playbook configurado (como responsable o como encargado). Comprueba las cláusulas obligatorias del encargo conforme a la Ley 81 de 2019, identifica gaps y genera tabla de cláusulas con posición, contrato y recomendación. Usar cuando el usuario diga "revisa este encargo", "DPA del proveedor", "contrato de encargado" o adjunte un DPA.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/privacidad/skills/encargo
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
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

## Cláusulas obligatorias del encargo de tratamiento (Ley 81 de 2019)

Verificar que el contrato incluye **todas** las cláusulas obligatorias:

| # | Cláusula obligatoria | Referencia | ¿Presente? | Observaciones |
|---|---|---|---|---|
| 1 | Objeto, duración, naturaleza y finalidad del tratamiento | Ley 81 de 2019 | | |
| 2 | Tipo de datos y categorías de titulares | Ley 81 de 2019 | | |
| 3 | Tratar solo siguiendo instrucciones documentadas del responsable | Ley 81 de 2019 | | |
| 4 | Confidencialidad del personal autorizado | Ley 81 de 2019 | | |
| 5 | Medidas de seguridad técnicas y organizativas | Ley 81 de 2019 | | |
| 6 | Régimen de subencargados | Ley 81 de 2019 | | |
| 7 | Asistencia al responsable en derechos del titular | Ley 81 de 2019 | | |
| 8 | Asistencia en la evaluación de impacto | Ley 81 de 2019 | | |
| 9 | Devolución o supresión de datos al finalizar | Ley 81 de 2019 | | |
| 10 | Poner a disposición información para auditoría | Ley 81 de 2019 | | |

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
| Sin plazo de notificación de brechas | Nos avisan cuando quieren | Exigir plazo concreto (ej. 24-48h), coherente con el plazo de notificación a la ANTAI de la Ley 81 de 2019 |
| Proveedor usa datos para "mejora del servicio" | Posible tratamiento para fines propios | Eliminar; tratamiento limitado a las instrucciones del responsable |
| Sin mecanismo de transferencia internacional | Transferencia ilícita | Exigir cláusulas contractuales de protección de datos / país con nivel adecuado / consentimiento del titular conforme a la Ley 81 de 2019 |
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

- Ley 81 de 2019 — encargado del tratamiento, cláusulas obligatorias, seguridad y transferencias internacionales (las transferencias requieren que el destino ofrezca un nivel de protección equivalente o superior, o que concurran condiciones como consentimiento o contrato; Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021)
- Decreto Ejecutivo 285 de 2021 — reglamento de la Ley 81 de 2019
- Guías y resoluciones de la ANTAI sobre contratos de encargado del tratamiento
- Ley 23 de 2015 — prevención de blanqueo (conservación de datos por sujetos obligados ante la UAF)

---

## Lo que este skill NO hace

- No redacta un encargo de tratamiento desde cero — para eso, usar la plantilla house de los documentos semilla.
- No realiza la evaluación de las transferencias internacionales — marca cuándo es necesaria.
- No decide si aceptar términos fuera del playbook — escala según la tabla de escalado.
