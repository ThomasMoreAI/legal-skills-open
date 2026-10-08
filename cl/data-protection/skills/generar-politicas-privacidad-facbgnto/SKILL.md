---
name: generar-politicas-privacidad-facbgnto
title: Generación de políticas de privacidad — Ley 21.719 (Chile)
description: Redacta los documentos de privacidad de cara al usuario —política de privacidad, avisos de tratamiento, textos de consentimiento, avisos de cookies, de NNA, de proveedores— a partir de la evidencia real que los otros skills de este plugin ya reunieron (RAT/ROPA, inventario, registro de proveedores, registro de IA, consentimientos). Úsalo cuando el usuario pida "genera la política de privacidad", "necesito el aviso de tratamiento de datos para el registro", "redacta el texto de consentimiento para datos de salud", "genera todas las políticas según lo que encontró la auditoría", o cualquier documento legal de cara al titular. No inventa servicios, proveedores ni plazos que no estén en la evidencia — si falta, ejecuta primero auditoria-ley-21719, implementar-ley-21719 o pide el inventario a chile-datos-personales. No lo uses para revisar código (esos son los otros cinco skills) ni para tomar la decisión de publicar sin revisión legal, que este skill nunca autoriza.
author: facbgnto
author_url: https://github.com/facbgnto/Chile-data-protection-21719/tree/main/skills/generar-politicas-privacidad
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: data-protection
language: es
sources:
- title: Trazabilidad Y Versionado
  path: references/trazabilidad-y-versionado.md
---

# Generación de políticas de privacidad — Ley 21.719 (Chile)

Los otros cinco skills de este plugin trabajan hacia adentro: código,
arquitectura, hallazgos, incidentes, un porcentaje. Este trabaja hacia
afuera — produce el texto que un titular real va a leer antes de aceptar,
o que un fiscalizador va a comparar contra lo que el sistema hace de verdad.

Por eso la regla que domina sobre todas las demás de este plugin se vuelve
todavía más estricta aquí:

**Cada afirmación del documento tiene que salir de evidencia verificable, o
no se escribe.** Una política de privacidad que dice "no compartimos tus
datos con terceros" cuando el registro de proveedores muestra seis
integraciones no es un error de redacción — es una declaración falsa de
cara al público, y este skill existe justamente para que eso no pase.

## Lo que este skill nunca hace

1. **No inventa.** Ni proveedores, ni finalidades, ni plazos de retención,
   ni mecanismos de transferencia que no estén registrados en la evidencia
   de F0. Si algo no está registrado, el documento lo deja como
   `REVISIÓN LEGAL REQUERIDA` o como un vacío explícito ("no se identificó
   evidencia de X — completar antes de publicar"), nunca como una frase
   plausible sin respaldo.
2. **No publica nada.** Todo lo que produce es un **borrador para revisión
   legal**. Cada documento generado abre con el aviso de la sección final de
   este archivo. Este skill redacta; no decide que el texto está listo para
   ir al sitio.
3. **No emite conclusiones jurídicas dentro del texto que redacta más allá
   de lo que la evidencia sostiene** — igual que el resto del plugin, marca
   `REVISIÓN LEGAL REQUERIDA` en vez de afirmar un plazo, una excepción o un
   corte etario que no esté confirmado en `marco-legal.md` o
   `bases-y-consentimiento.md`.

## Relación con los otros cinco skills

Este skill es **consumidor de evidencia**, no productor — en eso se parece a
`preparacion-ley-21719`, pero en vez de un puntaje produce texto legal:

```
chile-datos-personales / auditoria-ley-21719
        │  producen docs/privacidad/inventario.md y el RAT/ROPA
        ▼
implementar-ley-21719
        │  produce privacy_processing_activities, privacy_processors,
        │  privacy_ai_usage, privacy_retention_rules, privacy_consents
        ▼
generar-politicas-privacidad (este skill)
        │  redacta el texto público a partir de esa evidencia
        ▼
docs/privacidad/legal/   ← entregable, en el proyecto auditado, nunca aquí
```

Si ninguna de esas fuentes existe todavía, **no redactes desde cero**: dilo
explícitamente y ofrece dos caminos — ejecutar primero el skill que falta, o
redactar solo lo que la evidencia disponible permite, dejando el resto como
brecha declarada. Un documento completo construido sobre huecos rellenados a
criterio no es un borrador útil, es un riesgo con formato de política.

## F0 — Reunir evidencia

En orden de preferencia:

```
1. docs/privacidad/inventario.md          → qué datos, clasificación
2. docs/privacidad/rat.md (o equivalente)  → tratamientos, finalidad, base legal
3. privacy_processors / proveedores-registro.md → terceros, transferencias
4. privacy_ai_usage / registro-ia.md        → uso de IA, decisión automatizada
5. privacy_retention_rules / retencion-ejecutable.md → plazos de retención
6. privacy_consents / consentimiento.md      → finalidades que ya piden
                                                consentimiento, versión vigente
7. Modelo de representación legal (NNA), si existe → bases-y-consentimiento.md
8. Uso de almacenamiento de archivos/fotos → almacenamiento-archivos.md
```

Por cada fuente, registra si existe, está completa, o falta — esto alimenta
directamente qué documentos de F1 se pueden redactar con evidencia sólida y
cuáles quedan con brechas declaradas.

## F1 — Decidir qué documentos aplican

No generes los doce documentos por inercia. Cada uno tiene una condición de
activación — actívalo solo si la evidencia de F0 lo justifica:

```
política de privacidad         siempre, si hay al menos un tratamiento en el RAT
aviso de registro               si existe un flujo de registro/alta de cuenta
cookies/tracking                 solo si registro-ia.md o analytics-tracking.md
                                  muestran herramientas activas
consentimiento de finalidad       por cada finalidad que use consentimiento
                                   como base legal (privacy_legal_basis)
datos sensibles                   solo si el inventario marca alguna categoría
                                   SENSIBLE tratada
NNA                                solo si el RAT o el inventario indican
                                    titulares que pueden ser menores de edad
proveedores y transferencias        si hay al menos un proveedor o una
                                     transferencia internacional registrada
aviso de formulario                 por cada formulario que capture datos
                                     PERSONAL o superior identificado en F0
aviso de fotografías/documentos      solo si almacenamiento-archivos.md
                                      muestra captura de imágenes/documentos
aviso de IA                          solo si registro-ia.md tiene al menos
                                      un uso activo
```

Presenta la lista de documentos a generar, con la condición que la activó,
**antes** de redactar — permite que el usuario corrija si algo se activó por
error de interpretación de la evidencia.

## F2 — Redactar desde las plantillas

Cada plantilla vive en `${CLAUDE_PLUGIN_ROOT}/shared/templates/legal/` con
extensión `.template.md`. Contienen placeholders entre **`[[ ]]`** (doble
corchete, no `< >`) con una nota de qué fuente de F0 debe llenarlos — no los
completes con contenido plausible si la fuente indicada no tiene el dato:
dejar `[[REVISIÓN LEGAL REQUERIDA: plazo de retención no registrado para
esta categoría]]` es el resultado correcto, no un fallo del skill.

El doble corchete es la convención deliberada de este skill, distinta del
`< >` que el resto del plugin usa para ejemplos de formato: un placeholder
sin rellenar tiene que poder detectarse con un solo grep sin falsos
positivos contra HTML, JSX o un blockquote de markdown — ver F2.5.

```
shared/templates/legal/
    politica-privacidad.template.md
    aviso-privacidad.template.md
    cookies.template.md
    tratamiento-datos-sensibles.template.md
    tratamiento-nna.template.md
    proveedores-y-transferencias.template.md
    consentimiento-registro.template.md
    consentimiento-datos-sensibles.template.md
    consentimiento-nna.template.md
    aviso-formulario.template.md
    aviso-fotografias.template.md
    aviso-ia.template.md
```

Ver `references/trazabilidad-y-versionado.md` para el criterio exacto de
cómo citar la fuente de cada afirmación y cómo versionar.

## F2.5 — Verificar que no quedaron placeholders sin completar

Antes de entregar cualquier documento, corre esto sobre el archivo
generado (no sobre la plantilla):

```bash
grep -n '\[\[' docs/privacidad/legal/<documento>.md
```

Cualquier coincidencia es un placeholder que quedó sin rellenar — o bien
lo completas con el dato real de la evidencia de F0, o lo dejas como
`[[REVISIÓN LEGAL REQUERIDA: ...]]` a propósito. Lo que no puede pasar es
entregar un documento con `[[nombre de la organización]]` literal porque
se te olvidó completarlo — eso no es un hueco declarado, es un descuido, y
el disclaimer de borrador no lo cubre: el disclaimer avisa que falta
revisión legal, no que el documento esté a medio rellenar.

Si el grep no devuelve nada, el documento está completo en el sentido de
"todo lo que podía llenarse desde evidencia, se llenó" — puede seguir
teniendo secciones `REVISIÓN LEGAL REQUERIDA` dentro de los corchetes, y
eso está bien: son huecos declarados, no placeholders olvidados.

## F3 — Entregar

```
docs/privacidad/legal/
    politica-privacidad.md
    aviso-privacidad.md
    cookies.md                        (si aplica)
    tratamiento-datos-sensibles.md    (si aplica)
    tratamiento-nna.md                (si aplica)
    proveedores-y-transferencias.md   (si aplica)
    registro-versiones.md             ← ver F4
    frontend/
        consentimiento-registro.md
        consentimiento-datos-sensibles.md  (si aplica)
        consentimiento-nna.md              (si aplica)
        aviso-formulario-<nombre>.md       (uno por formulario relevante)
        aviso-fotografias.md               (si aplica)
        aviso-ia.md                        (si aplica)
```

Nunca dentro de este plugin — estos son entregables del proyecto auditado,
igual que el inventario o el informe de auditoría.

## F4 — Versionado y registro de aceptación

Todo documento público que un titular acepta necesita versión, porque
`consentimiento.md` (skill `implementar-ley-21719`) exige que
`privacy_consents.version_texto` corresponda a un texto real y recuperable
— no a "la política actual", que cambia.

Crea o actualiza `docs/privacidad/legal/registro-versiones.md`:

```markdown
# Registro de versiones — documentos de privacidad
| Documento | Versión | Fecha | Cambios | Vigente |
|---|---|---|---|---|
| politica-privacidad.md | v1 | 2026-08-22 | Versión inicial | sí |
| consentimiento-registro.md | v1 | 2026-08-22 | Versión inicial | sí |
```

Cuando se regenera un documento por un cambio real en el sistema (nuevo
proveedor, nueva finalidad), sube la versión y **no reescribas la fila
anterior** — los consentimientos otorgados bajo v1 siguen siendo válidos
para lo que v1 decía, igual que explica `consentimiento.md`.

## Disclaimer obligatorio — va en cada documento generado

Encabeza **todo** documento de `docs/privacidad/legal/` con esto, sin
excepción y sin resumir:

```markdown
> **BORRADOR — pendiente de revisión legal.** Este documento fue generado a
> partir de la evidencia técnica reunida en `docs/privacidad/` (inventario,
> RAT/ROPA, registro de proveedores, registro de IA, consentimientos) el
> <fecha>. No está listo para publicarse: requiere revisión de un abogado
> antes de usarse de cara a un titular. Los puntos marcados
> `REVISIÓN LEGAL REQUERIDA` son huecos deliberados, no omisiones — no los
> completes sin esa revisión.
```

## Qué no debe hacer este skill

- **No inventar contenido plausible.** Ver la sección "Lo que este skill
  nunca hace" arriba — es la regla central, no una entre varias.
- **No presentar el borrador como publicable.** El disclaimer va siempre.
- **No mezclar versiones.** Un documento regenerado sube de versión; no
  sobrescribe silenciosamente el historial de qué decía antes.
- **No usar datos personales reales como ejemplo** en ningún documento —
  mismo criterio que el resto del plugin.
- **No generar un documento cuya condición de activación (F1) no se
  cumple** — un aviso de cookies en un sistema sin ninguna herramienta de
  tracking registrada es ruido, no protección.
