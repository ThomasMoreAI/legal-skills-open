# Documentos legales: cuáles crear y cómo

Todos son Markdown en `src/content/legal/<idioma>/` con este frontmatter (schema de
`src/content.config.ts`):

```markdown
---
title: Aviso de privacidad
description: Cómo tratamos tus datos personales cuando visitas este sitio o nos escribes.
updatedAt: 2026-10-01
translationKey: privacidad
---
```

- El nombre del archivo es la URL: `privacidad.md` → `/privacidad`.
- Sin marcadores de borrador: el documento se publica al pasar la verificación final de la
  skill.
- Con varios idiomas, cada traducción comparte `translationKey`.
- Al crear o quitar un documento: enlázalo en `footer.links` de `src/content/site/<idioma>.yaml`
  y corre `pnpm bsi:sync`.

<!-- check:docs ejemplos: src/content/legal/es/cookies.md src/content/legal/es/aviso-legal.md -->

## Cuándo aplica cada uno

| Documento                        | Archivo                                          | Cuándo                                                |
| -------------------------------- | ------------------------------------------------ | ----------------------------------------------------- |
| Aviso de privacidad integral     | `privacidad.md`                                  | Siempre (el sitio al menos recibe correos)            |
| Aviso simplificado               | `legal.formNotice` en `site/<idioma>.yaml`       | Si hay formularios activos (México: obligatorio)      |
| Términos y condiciones de uso    | `terminos.md`                                    | Siempre                                               |
| Términos de venta y devoluciones | `terminos.md` (sección) o `terminos-de-venta.md` | Si se vende en línea                                  |
| Política de cookies              | `cookies.md`                                     | Si hay medición, píxeles o terceros que dejan cookies |
| Aviso legal                      | `aviso-legal.md`                                 | Si la ley del país lo exige (por ejemplo, España)     |

Si se crea `cookies.md`, define `legal.cookiesHref: /cookies` en `site/<idioma>.yaml` para que el
banner enlace ahí.

## Aviso de privacidad integral: estructura

1. **Responsable:** nombre o razón social, domicilio y correo de privacidad.
2. **Datos que recabamos:** por formulario y por herramienta (tabla si son varios). Señala los
   sensibles si los hay.
3. **Finalidades:** primarias (necesarias) y secundarias (requieren consentimiento, por ejemplo
   newsletter o publicidad), con cómo negarse a las secundarias.
4. **Encargados y transferencias:** proveedores que tratan datos por cuenta del responsable
   (alojamiento, envío de correo, medición, publicidad), con su país. Distingue encargados
   (tratan por encargo) de transferencias (terceros con fines propios), según la ley aplicable.
5. **Cookies y tecnologías de rastreo:** resumen y enlace a la política de cookies.
6. **Conservación:** plazo real dado por el cliente.
7. **Derechos y cómo ejercerlos:** procedimiento, requisitos de la solicitud, plazos legales,
   medio de respuesta; revocación del consentimiento y opciones para limitar el uso.
8. **Cambios al aviso:** dónde y cómo se avisan.
9. **Autoridad:** ante quién reclamar (según el país).
10. **Fecha de última actualización** (la pone `updatedAt`).

## Política de cookies: estructura

1. Qué son las cookies y tecnologías similares (breve).
2. **Tabla de herramientas** con lo que el sitio usa de verdad: nombre, proveedor, finalidad
   (medición o publicidad), si requiere consentimiento y enlace a la política del proveedor. No
   listes nombres de cookies concretos salvo que los hayas verificado: cambian con frecuencia.
3. Cómo se pide el consentimiento: modo (`opt-in` u `opt-out`), categorías, cada cuánto se
   vuelve a preguntar (`consent.renewal`) y cuánto se recuerda un rechazo.
4. Cómo cambiar la decisión: botón "Configurar cookies" en el pie de página y configuración del
   navegador.
5. Fecha de actualización. Si cambia la lista de herramientas, sube `consent.version` en
   `src/config/consent.ts` para volver a preguntar.

## Términos y condiciones: estructura

1. Titular del sitio y contacto.
2. Objeto y aceptación.
3. Uso permitido del sitio y del contenido; propiedad intelectual.
4. Exactitud de la información y limitación de responsabilidad (sin prometer lo que el cliente
   no ofrece).
5. Enlaces a terceros.
6. Si hay venta: precios, impuestos, formas de pago, envíos, cancelaciones, devoluciones y
   garantías, según la ley de consumo del país.
7. Ley aplicable y jurisdicción (la que indique el cliente).
8. Cambios a los términos.

## Estilo

- Claro, en segunda persona ("tus datos"), frases cortas, sin latinismos innecesarios.
- Nada de datos inventados: si falta un dato, pregúntalo. No entregues documentos con huecos.
- Cita la ley por su nombre la primera vez; no copies artículos completos.
