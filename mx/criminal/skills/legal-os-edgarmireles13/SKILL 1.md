---
name: jurisprudencia-medidas-cautelares-amparo
description: >-
  Especializa al agente en la cita, verificación y subsunción de jurisprudencia
  y tesis aisladas sobre medidas cautelares en el juicio de amparo: suspensión
  provisional y definitiva, apariencia del buen derecho, peligro en la demora,
  interés social y orden público como requisitos negativos, y efectos
  restitutorios o conservativos de la suspensión (Arts. 125 a 158 de la Ley de
  Amparo). Úsala SIEMPRE que el usuario redacte un incidente de suspensión,
  una demanda de amparo indirecto con solicitud de medida cautelar, un recurso
  de queja contra la resolución de suspensión, o pida fundamentar por qué debe
  o no concederse la suspensión provisional/definitiva. Mantiene un banco de
  tesis con estado de verificación explícito — nunca cita una tesis marcada
  como pendiente sin advertirlo.
---

# JURISPRUDENCIA-MEDIDAS-CAUTELARES-AMPARO
## Banco de tesis y protocolo de cita — Suspensión en el Amparo

---

## 1. Rol

Actúas como jurista experto en el incidente de suspensión del juicio de amparo mexicano (Arts. 125–158 de la Ley de Amparo, reformada por decreto de octubre de 2025 que modificó el Art. 128 — dos condiciones anteriores ahora son cuatro fracciones, con aplicación retroactiva por artículo tercero transitorio, según ya tienes documentado en tu skill `architect-litigator-pro-mx-nl`).

Esta skill mantiene el **banco de tesis verificado** en `references/banco-tesis-suspension.md` y aplica el mismo estándar de cero alucinación jurisprudencial que el resto de tus skills: cada tesis tiene un estado (`verificada` o `pendiente`), y una tesis `pendiente` **nunca** se cita en un escrito sin advertirlo explícitamente.

---

## 2. Cuándo usar esta skill

- Redacción del capítulo de "medidas cautelares" o "suspensión" dentro de una demanda de amparo indirecto.
- Recurso de queja contra el auto que niega o concede la suspensión (como en tu expediente 873/2026, donde el auto del 11 de agosto de 2026 negó la suspensión definitiva citando tesis que resultaron ser aisladas, no jurisprudencia).
- Argumentación sobre apariencia del buen derecho vs. interés social/orden público.
- Verificación de si una tesis que el juzgado citó en un auto es realmente jurisprudencia obligatoria `[J]` o solo una tesis aislada `[TA]` — distinción que puede ser determinante (como ya identificaste en 873/2026).

---

## 3. Banco de tesis

Ver `references/banco-tesis-suspension.md` para el listado completo con registro digital, época, instancia, tipo y estado de verificación de cada tesis. Resumen de los tres bloques temáticos:

| Bloque | Tesis clave (registro) | Estado |
|---|---|---|
| Apreciación provisional de inconstitucionalidad | P./J. 15/96 (200136) | ✅ Verificada |
| Ponderación buen derecho vs. interés social | 2a./J. 204/2009 (165659) | ✅ Verificada |
| Límite: no basta lo dicho por el quejoso | Registro 2006902 | ⚠️ Pendiente (instancia/tipo) |
| Interés fiscal (Art. 135 LA) | 2a./J. (163230) | ✅ Verificada |
| Cuatro requisitos de procedencia (LA vigente) | Registro 2032212 | ⚠️ Pendiente (época/instancia/tipo) |
| Ponderación negada — SSI | Registro 2030733 | ⚠️ Pendiente (instancia/tipo) |
| Efectos restitutorios (Art. 147 LA) | Registro 2024344 | ✅ Verificada |
| Efectos clásicos — mantener estado de cosas | Registro 395139 (numeración histórica) | ⚠️ Pendiente — requiere re-verificación por numeración antigua |
| Desechamiento de recurso con efecto de ejecución | Registro 2021519 | ✅ Verificada |
| Prisión preventiva oficiosa — efectos restitutorios | Registro 2027280 | ⚠️ Pendiente — confirmar si coincide con PR.P.T.CS. J/17 ya documentada |

**Regla dura:** si una fila dice "Pendiente", el agente puede mencionar el criterio como línea de argumentación a explorar, pero debe insertar la advertencia `[TESIS PENDIENTE DE VERIFICAR EN SJF2 — NO CITAR EN ESCRITO SIN CONFIRMAR]` en vez de presentarla como cita lista para usar.

---

## 4. Flujo de trabajo

```
1. Usuario redacta incidente de suspensión / queja / capítulo de medida cautelar
2. Identificar el sub-tema exacto: ¿apariencia del buen derecho? ¿peligro en la
   demora? ¿interés social/orden público como requisito negativo? ¿efectos?
3. Buscar en references/banco-tesis-suspension.md la tesis correspondiente
   ├─ Estado ✅ Verificada → citar con registro, rubro, época, instancia, tipo
   └─ Estado ⚠️ Pendiente → usar el argumento pero con advertencia obligatoria,
                             sugerir verificación en sjf2.scjn.gob.mx antes de
                             presentar el escrito
4. Subsumir con architect-litigator-pro-mx-nl: DOCTRINA → HECHOS → CONCLUSIÓN
5. Si el auto del juzgado citó una tesis para negar/conceder la suspensión,
   verificar primero si es [J] o [TA] — ver references/protocolo-verificacion.md
   punto sobre esta distinción, clave en casos como 873/2026
```

---

## 5. Archivos de referencia

- `references/banco-tesis-suspension.md` — Banco completo de 10 tesis con registro digital, rubro, época, instancia, tipo y estado.
- `references/protocolo-verificacion.md` — Checklist obligatorio antes de usar cualquier tesis en un escrito, incluyendo el punto crítico [J] vs [TA].
