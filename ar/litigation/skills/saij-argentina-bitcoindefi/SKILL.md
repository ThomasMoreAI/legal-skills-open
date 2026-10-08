---
name: saij-argentina-bitcoindefi
title: SAIJ Argentina · Consulta de fuentes jurídicas en vivo
description: 'Consulta en vivo el derecho argentino en SAIJ (Sistema Argentino de Información Jurídica, Ministerio de Justicia): jurisprudencia, legislación y doctrina nacional, federal y provincial (Jujuy, Salta y todas las provincias), con texto completo y permalink de citación. Usar cuando se necesite buscar o verificar un fallo, una ley/decreto/resolución o doctrina argentina, o citar fuente primaria. Incluye un servidor MCP propio de cero dependencias.'
author: Bitcoindefi
author_url: https://github.com/Bitcoindefi/agente-smith/tree/main/skills/saij-argentina
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ar
practice: litigation
language: es
---

# SAIJ Argentina · Consulta de fuentes jurídicas en vivo

Da acceso a los **899K+ documentos de SAIJ** (jurisprudencia, legislación y doctrina de
Argentina) desde Claude, para trabajar sobre fuente primaria y no inventar citas.

## Instalación del conector (una vez)

Este skill trae un servidor MCP propio (`server.mjs`, Node, sin dependencias). Registralo:

```bash
# Requiere Node.js >= 22 y Claude Code
claude mcp add saij --scope user -- node --use-system-ca "<ruta a este skill>/server.mjs"
```

> El flag `--use-system-ca` es necesario: los sitios .gob.ar sirven una cadena TLS
> incompleta y así se usa el almacén de certificados del sistema (sin desactivar la
> verificación).

Reiniciá Claude Code y verificá con `/mcp` que `saij` figure conectado.

## Herramientas que expone

| Tool | Qué hace |
|------|----------|
| `saij_buscar_jurisprudencia` | Busca sumarios y fallos (nacional, federal, provincial). |
| `saij_buscar_legislacion` | Busca leyes, decretos y resoluciones, con estado de vigencia. |
| `saij_buscar_doctrina` | Busca doctrina jurídica. |
| `saij_documento` | Trae el texto completo de un documento por su `uuid`. |

Parámetros de búsqueda: `consulta` (texto libre), `limite` (1–25), `pagina`.

## Cómo usarlo bien

1. Buscá con lenguaje natural: *"despido discriminatorio ley 23592"*, *"código procesal civil Salta"*.
2. Para filtrar por provincia, incluí su nombre en la consulta (ej. *"...Jujuy"*, *"...Salta"*).
   Los resultados provinciales vienen con jurisdicción `Local`.
3. Tomá el `uuid` de un resultado y pedí `saij_documento` para leer el texto completo
   antes de citar.
4. **Verificá siempre** la vigencia y el texto en la fuente oficial: `https://www.saij.gob.ar/<uuid>`.

## Notas

- Solo lectura. Fuente pública (Ministerio de Justicia de la Nación). Sin API key.
- El campo interno `totalSearchResults` de SAIJ no es un conteo real; paginá con `pagina`
  hasta que un resultado devuelva menos ítems que el `limite`.
- Código propio bajo licencia MIT. No constituye asesoramiento legal.
