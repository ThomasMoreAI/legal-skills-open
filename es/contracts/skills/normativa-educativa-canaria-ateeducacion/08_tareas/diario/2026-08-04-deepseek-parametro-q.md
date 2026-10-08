# Diario — 2026-08-04: DeepSeek soporta prefill por URL (`?q=`)

## Hecho

- Revisado el soporte de parámetro de prompt en URL para las IA que seguían en flujo manual (`docs/index.html`).
- **DeepSeek**: confirmado que `https://chat.deepseek.com/?q=` precarga el prompt.
  - Evidencia en el bundle JS de la web (`main.*.js`): constante `chat_url_prefill` y lista de params `["q","prompt","mode","search","thinking"]`.
  - Lee `q` (o fallback `prompt`), lo guarda en `sessionStorage` y lo aplica al chat al estar autenticado.
  - Verificado en navegador: al abrir `/?q=TEST_PROMPT_DEEPSEEK_Q_PARAM`, `sessionStorage.chat_url_prefill` queda `{"prompt":"TEST_PROMPT_DEEPSEEK_Q_PARAM"}`.
- Actualizado el botón DeepSeek de `data-manual-launch` a `data-launch="https://chat.deepseek.com/?q="`.
- **Copilot**: sigue sin soportar prefill por URL. Al abrir `https://copilot.microsoft.com/?q=...` la query se descarta y el textarea no se rellena. Se mantiene el modal manual.
- Gemini sigue usando el workaround de Google Search AI Mode (`udm=50`), sin cambio.

## Pendiente

- Copilot: reevaluar cuando Microsoft documente o implemente un parámetro de prompt en URL.
