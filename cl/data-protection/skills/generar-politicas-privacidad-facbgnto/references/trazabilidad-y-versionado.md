# Trazabilidad y versionado

## Por qué la trazabilidad es obligatoria, no una buena práctica

Un abogado revisando un borrador de política de privacidad no puede validar
"¿esto es cierto?" sin saber de dónde salió cada afirmación. Sin
trazabilidad, la revisión legal se convierte en releer todo el sistema desde
cero — exactamente el trabajo que este skill existe para evitar.

## Regla de cita por afirmación

Cada párrafo del **borrador de trabajo** (antes de la limpieza final para
publicación) lleva un comentario HTML con su fuente, invisible al
renderizar pero visible en el markdown crudo:

```markdown
Compartimos tus datos de contacto con nuestro proveedor de envío de
correos transaccionales.
<!-- fuente: privacy_processors id=3 (SendGrid), proveedores-registro.md -->
```

```markdown
Conservamos tus datos de cuenta por 18 meses desde tu última interacción.
<!-- fuente: privacy_retention_rules categoria_dato="datos_cuenta" -->
```

```markdown
[[REVISIÓN LEGAL REQUERIDA: no se encontró privacy_retention_rules para la
categoría "historial_compras" — completar antes de publicar]]
<!-- fuente: ausente — F0 no encontró regla de retención para esta categoría -->
```

El doble corchete `[[ ]]` (no `< >`) es la convención de placeholder de
este skill — ver `SKILL.md`, F2, para por qué: un solo grep sobre el
documento generado tiene que poder confirmar que no quedó ninguno sin
completar, sin confundirse con HTML, JSX o blockquotes de markdown.

Al entregar la versión final para revisión legal, **conserva los
comentarios de fuente** — no los quites para "limpiar" el documento. Son
exactamente lo que permite que la revisión sea rápida en vez de una
re-auditoría completa. Quítalos solo si el usuario pide explícitamente una
versión de publicación final, y aun así dilo: "generé también la versión sin
comentarios de trazabilidad para publicación, después de que la anterior
esté aprobada".

## Qué hacer cuando la evidencia es ambigua

```
Fuente parcial       → redacta con lo que hay, marca el resto como
                        REVISIÓN LEGAL REQUERIDA con la brecha específica.
Fuente contradictoria → no elijas una versión por criterio propio.
                        Repórtalo al usuario antes de redactar ese punto:
                        "el inventario dice retención de 12 meses para
                        datos de contacto, pero privacy_retention_rules
                        registra 18 — ¿cuál es la vigente?"
Fuente ausente         → REVISIÓN LEGAL REQUERIDA explícito, con qué
                          archivo se esperaba encontrar y no se encontró.
```

Nunca resuelvas una ambigüedad por plausibilidad ("18 meses es un plazo
razonable, lo uso"). Eso es exactamente inventar, solo que con apariencia de
buen juicio.

## Versionado — el contrato con `consentimiento.md`

`shared/arquitectura/consentimiento.md` (skill `implementar-ley-21719`)
exige que `privacy_consents.version_texto` corresponda a un texto real que
se pueda recuperar tal como estaba cuando el titular lo aceptó. Esto impone
tres reglas duras a este skill:

1. **Cada documento tiene una versión (`v1`, `v2`, ...), nunca "la versión
   actual" como identificador.** Un enlace que apunta siempre al documento
   más reciente no sirve para reconstruir qué aceptó alguien hace ocho
   meses.
2. **Los documentos anteriores no se borran ni se sobrescriben.** Cuando se
   regenera `politica-privacidad.md` por un cambio real (nuevo proveedor,
   nueva finalidad), la versión anterior se archiva —
   `docs/privacidad/legal/historial/politica-privacidad.v1.md`— y
   `registro-versiones.md` (formato en `SKILL.md`, F4) registra el cambio.
3. **El motivo del cambio se registra**, no solo la fecha. "v2 — se agregó
   la finalidad de scoring crediticio, nuevo proveedor de analítica" es
   trazable; "actualización" no lo es.

## Cuándo subir de versión vs. cuándo corregir la misma versión

```
Sube de versión (v1 → v2)     Cambia lo que el titular aceptó: nueva
                               finalidad, nuevo proveedor, nueva
                               transferencia internacional, cambio de
                               plazo de retención.

Corrige la misma versión       Error de redacción, tipografía, formato —
                                nada que cambie lo que el titular está
                                aceptando en sustancia. Documenta igual en
                                registro-versiones.md como "corrección
                                menor, v1", sin subir el número.
```

Ante duda entre las dos categorías, sube de versión — es la opción
defendible: nunca vas a necesitar justificar por qué versionaste de más,
pero sí por qué un cambio sustantivo quedó bajo el mismo texto que alguien
ya había aceptado antes de que existiera.

## Vínculo con el consentimiento en frontend

Los textos de `docs/privacidad/legal/frontend/` son los que efectivamente
se muestran en la interfaz — cuando `consentService.grant()` (ver
`consentimiento.md`) registra `version_texto`, ese valor tiene que ser la
versión exacta del archivo correspondiente en `frontend/`, no de la política
completa. Un checkbox de registro apunta a
`consentimiento-registro.md` versión `v2`, no a `politica-privacidad.md`
versión `v3` — son documentos versionados de forma independiente porque
cambian en momentos distintos.
