# Diario — 2026-05-01: botones IA con parametros URL

## Trabajo realizado

- Mantenidos visibles los botones de Copilot y DeepSeek en `docs/index.html` con un modal previo de advertencia.
- El modal copia el prompt y avisa de que hay que pegarlo manualmente porque esas plataformas no permiten precargarlo por URL.
- Anadido Grok a la lista de IA con icono y apertura mediante `https://grok.com/?q=`.
- Mantenido visible Gemini usando la URL de Google Search AI Mode, con comentario en codigo porque Gemini todavia no ofrece parametro directo equivalente para precargar el prompt.
- Anotado el pendiente en `TODO.md`.

## Incidencias y limites

- El parametro de Grok no se ha encontrado documentado oficialmente en la documentacion de xAI; se usa el patron publico `?q=` observado para `grok.com`.
- Copilot y DeepSeek quedan activos, pero como flujo manual hasta que soporten parametro directo de prompt.
- No se han tocado fichas normativas, fuentes, curriculos, relaciones ni indices YAML.
