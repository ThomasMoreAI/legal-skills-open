---
name: revisar-datos-personales-carlos-dominguez-faber
title: Revisar datos personales (Ley 21.719)
description: Audita un proyecto de software frente a la Ley 21.719 de proteccion de datos personales de Chile. Levanta el inventario de datos personales que trata el sistema, revisa diez puntos de cumplimiento con evidencia de archivo y linea, y entrega un reporte que separa lo verificado de lo que no se pudo comprobar. Usar cuando alguien pida revisar cumplimiento, privacidad, proteccion de datos, GDPR, RGPD, 21.719, minimizacion, consentimiento, derecho de supresion o portabilidad en un repositorio.
author: Carlos-Dominguez-faber
author_url: https://github.com/Carlos-Dominguez-faber/revisar-datos-personales
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: data-protection
language: es
sources:
- title: Checklist 21719
  path: references/checklist-21719.md
- title: Evaluacion Proveedores
  path: references/plantillas/evaluacion-proveedores.md
- title: Registro Tratamiento
  path: references/plantillas/registro-tratamiento.md
- title: Runbook Brecha
  path: references/plantillas/runbook-brecha.md
---

# Revisar datos personales (Ley 21.719)

Auditoría de cumplimiento sobre un repositorio real. No es asesoría legal: es un
inventario técnico con evidencia, para que una persona sepa qué preguntarle a su
abogado.

## La regla que manda sobre todas las demás

**Nunca afirmes que algo cumple.** Este trabajo se entrega en tres estados y
solo tres:

| Estado | Cuándo usarlo |
|---|---|
| `ENCONTRADO` | Viste el problema en el código. Va con ruta y línea. |
| `CORRECTO` | Viste la implementación que lo resuelve. Va con ruta y línea. |
| `NO VERIFICABLE` | No pudiste comprobarlo leyendo el repo. Di por qué. |

Una afirmación sin `archivo:línea` no entra al reporte. Si la evidencia está
fuera del código —en un panel de Supabase, en un contrato con un proveedor, en
la configuración de un servicio— eso es `NO VERIFICABLE`, y se dice así.

`NO VERIFICABLE` no es un fracaso: es el resultado honesto y es la parte más útil
del reporte, porque es la lista de lo que la persona tiene que ir a mirar con sus
propios ojos.

## Procedimiento

### Paso 1 — Inventario antes que juicio

Antes de evaluar nada, levanta qué datos personales trata el sistema. Busca en
este orden:

1. Migraciones y definiciones de esquema (`*.sql`, `schema.prisma`, `models.py`,
   `migrations/`, `CREATE TABLE`).
2. Formularios y validadores del frontend.
3. Tipos e interfaces que crucen la frontera de la red.
4. Payloads que se envían a terceros.

Para **cada campo** que identifique o haga identificable a una persona natural,
llena una fila:

```
tabla.campo | qué es | finalidad declarada | base de licitud | retención | quién más lo ve
```

Si no puedes deducir la finalidad de un campo leyendo el código, escribe
`finalidad no evidente en el código`. Esa frase es el hallazgo más valioso de
todo el paso: un campo cuya razón de existir nadie puede explicar es exactamente
lo que el principio de proporcionalidad prohíbe.

Marca aparte los **datos sensibles**: salud, origen racial, afiliación política,
convicciones religiosas, vida sexual, identidad de género, biométricos y perfil
biológico. Ojo con los que se disfrazan: un campo `notas` u `observaciones` de
texto libre suele contener datos de salud. Revisa los datos reales si tienes
acceso, no solo el nombre de la columna.

### Paso 2 — Los diez puntos

Recorre `references/checklist-21719.md`. Cada punto trae qué buscar, los patrones
que delatan el problema y el artículo que lo respalda.

### Paso 3 — Verificación contra datos, no contra código

Leer el código no prueba que el sistema se comporte como el código sugiere.
Cuando tengas acceso a un entorno de desarrollo, propón —y ejecuta si te
autorizan— al menos esta comprobación:

1. Crea un registro de prueba con un valor único y rastreable.
2. Ejerce el borrado por el camino que usa una persona real.
3. Busca ese valor único en **todas** partes: tablas, tablas de auditoría, logs,
   colas de trabajos, caché, exports, sistemas de terceros.

Si el valor sobrevive en algún lado, el borrado no borra. Repórtalo como
`ENCONTRADO` aunque el código diga `DELETE`.

Cuando no tengas ese acceso, dilo: *"la lógica de borrado se ve correcta en
`ruta:línea`, pero no se verificó contra una base real"*. No lo des por bueno.

### Paso 4 — El reporte

Entrega en este orden:

1. **Resumen** — cuántos puntos en cada estado. Sin adjetivos.
2. **Inventario de datos** — la tabla del paso 1.
3. **Hallazgos** — ordenados por gravedad, cada uno con: qué encontraste,
   `archivo:línea`, por qué importa, el artículo, y el arreglo concreto.
4. **No verificable** — qué falta mirar y dónde.
5. **Fuera de alcance** — lo que necesita un abogado: redacción de la política de
   privacidad, contratos con proveedores, evaluación de impacto, decisión sobre
   la base de licitud aplicable.

Cierra siempre con el recordatorio de que esto no es asesoría legal.

## Cómo no fallar

**No inventes la política de privacidad.** Si te piden generar el texto del
artículo 14 ter, constrúyelo desde el inventario real del paso 1. Redactar una
política que promete algo que el sistema no hace es publicar una afirmación falsa
sobre el propio sistema, y eso es peor que no tenerla.

**No confundas ausencia de evidencia con cumplimiento.** No encontrar un endpoint
de exportación significa que no lo encontraste, no que la portabilidad esté
resuelta en otro lado.

**Pide la segunda opinión.** Al terminar, sugiere que otro modelo audite el mismo
repo. Un modelo no encuentra sus propios puntos ciegos.

**Sé específico con el arreglo.** "Mejorar el manejo del consentimiento" no sirve.
"Reemplazar la columna `acepto_todo` por una tabla `consentimientos` con
`finalidad`, `version_texto`, `otorgado_en` y `revocado_en`" sí.

## Alcance territorial

Antes de empezar, verifica si la ley aplica: alcanza a quien esté establecido en
Chile, y también a quien —desde donde sea— ofrezca bienes o servicios a personas
que están en Chile, aunque sean gratis, o monitoree su comportamiento. Un SaaS
gratuito con usuarios chilenos entra.

Si el proyecto no toca usuarios chilenos, la auditoría sigue sirviendo: casi todo
esto es común al RGPD europeo y a las leyes que vienen en el resto de la región.
Dilo así en el reporte.

## Archivos de apoyo

- `references/checklist-21719.md` — los diez puntos en detalle.
- `references/plantillas/registro-tratamiento.md` — inventario para llenar.
- `references/plantillas/runbook-brecha.md` — qué hacer las primeras horas.
- `references/plantillas/evaluacion-proveedores.md` — antes de conectar un tercero.

---

Esta skill no da asesoría legal. Produce un inventario técnico y una lista de
preguntas. La revisión legal la hace un abogado.
