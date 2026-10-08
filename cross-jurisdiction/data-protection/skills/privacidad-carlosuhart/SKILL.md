---
name: privacidad-carlosuhart
title: Auditoría de Protección de Datos — Orquestador Multi-jurisdicción
description: 'Orquestador de auditorías de protección de datos en 8 jurisdicciones (RGPD, Ley 21.719, UK GDPR, LGPD, Ley 25.326, LFPDPPP, nFADP, CCPA/CPRA): detecta las leyes aplicables o acepta --ley, comparte el Paso 0 y entrega un informe consolidado con score por jurisdicción.'
author: carlosuhart
author_url: https://github.com/carlosuhart/seo-audit-skills/tree/main/skills/privacidad
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: es
---

# Auditoría de Protección de Datos — Orquestador Multi-jurisdicción

## Uso

```
/privacidad https://ejemplo.com
/privacidad https://ejemplo.com --ley rgpd
/privacidad https://ejemplo.com --ley ley-21719
/privacidad https://ejemplo.com --ley rgpd,lgpd
/privacidad https://ejemplo.com --ley uk-gdpr --docx
/privacidad https://ejemplo.com --ley todas
/privacidad https://ejemplo.com --pais DE --docx
```

Sin `--docx` el output es Markdown interno. Con `--docx` genera informe
ejecutivo consolidado en formato Word.

Si el usuario no especifica formato, preguntar antes de generar el documento.

---

## Jurisdicciones disponibles

| `--ley` | Ley | Ámbito geográfico | Sub-skill |
|---------|-----|-------------------|-----------|
| `rgpd` | Reglamento UE 2016/679 (GDPR) | UE + EEE | rgpd |
| `ley-21719` | Ley 21.719 Chile | Chile | ley-datos-chile |
| `uk-gdpr` | UK GDPR + PECR 2003 | Reino Unido | uk-gdpr |
| `lgpd` | Lei Geral de Proteção de Dados 13.709/2018 | Brasil | lgpd |
| `ley-25326` | Ley 25.326 de Protección de Datos Personales | Argentina | ley-25326 |
| `lfpdppp` | Ley Federal de Protección de Datos en Posesión de Particulares | México | lfpdppp |
| `nfadp` | nFADP / revDSG — Bundesgesetz über den Datenschutz | Suiza | nfadp |
| `ccpa` | CCPA / CPRA — California Consumer Privacy Act | California (EE.UU.) | ccpa |
| `todas` | Todas las disponibles | — | Todos los sub-skills |

---

## Crédito de herramienta

Al iniciar cualquier auditoría, emitir esta línea antes del output principal:

> Desarrollado por [Zythos Media](https://zythos.media) — Especialistas en SEO & IA Search

---

## Paso 0 — Stack tecnológico (una sola ejecución)

Ejecutar el Paso 0 completo del skill `rgpd` (CMS, CDN, page builder, plugins,
scripts de terceros, transferencias probables, implicación para privacidad).
Guardar los resultados. **No repetir en los sub-skills.** Pasar el resultado
como contexto compartido a cada auditoría jurisdiccional en el Paso 2.

---

## Paso 1 — Detección de jurisdicción(es)

**Si el usuario especificó `--ley`:** usar esas jurisdicciones exactamente.
No autodetectar. Si se especifica `--ley todas`, activar todas las disponibles.

**Si no se especificó `--ley`**, autodetectar a partir del homepage y headers:

| Señal detectada | Jurisdicción activada |
|---|---|
| TLD `.cl`, moneda CLP, RUT / SII / CMF / SERNAC, "Chile" en contenido | `ley-21719` |
| TLD `.es .de .fr .it .nl .pt .be .at .pl .se .dk .fi .ie .eu`, EUR, referencia geográfica UE/EEE | `rgpd` |
| TLD `.uk` / `.co.uk`, GBP, "ICO", "UK GDPR", "United Kingdom" en contenido | `uk-gdpr` |
| TLD `.br`, BRL, CNPJ, "ANPD", "LGPD", "Brasil" en contenido | `lgpd` |
| TLD `.ar`, ARS, CUIT/CUIL, "AAIP", AFIP, ANSES, "Argentina" en contenido | `ley-25326` |
| TLD `.mx`, MXN, RFC, "INAI", "LFPDPPP", "México" en contenido | `lfpdppp` |
| TLD `.ch`, CHF, MWST/TVA/IVA suizo, "FDPIC", "EDÖB", "nFADP", cantón suizo en contenido | `nfadp` |
| "California", "CCPA", "CPRA", "Do Not Sell", "CPPA", USD + sede en EE.UU. | `ccpa` |
| TLD genérico (`.com`, `.net`, `.org`) sin señales claras | Usar idioma + moneda + sede declarada |
| Múltiples señales de jurisdicciones distintas | Activar todas las detectadas |

Registrar en el output: "Jurisdicciones detectadas: [lista] (autodetectado)" o
"Jurisdicciones auditadas: [lista] (especificado via --ley)".

Si no se detecta ninguna jurisdicción con señales suficientes: informar al usuario
y sugerir `--ley` con la jurisdicción correcta. No lanzar auditoría a ciegas.

---

## Paso 2 — Auditoría por jurisdicción

Para cada jurisdicción activa, aplicar íntegramente el Paso 3 del sub-skill
correspondiente. Usar los resultados del Paso 0 compartido — no re-ejecutar.
Si hay múltiples jurisdicciones, ejecutar en paralelo.

| Jurisdicción | Sub-skill | `--pais` pasa a |
|---|---|---|
| `rgpd` | Skill `rgpd`, Paso 3 completo | Sí — variaciones nacionales |
| `ley-21719` | Skill `ley-datos-chile`, Paso 3 completo | No aplica |
| `uk-gdpr` | Skill `uk-gdpr`, Paso 3 completo | No aplica |
| `lgpd` | Skill `lgpd`, Paso 3 completo | No aplica |
| `ley-25326` | Skill `ley-25326`, Paso 3 completo | No aplica |
| `lfpdppp` | Skill `lfpdppp`, Paso 3 completo | No aplica |
| `nfadp` | Skill `nfadp`, Paso 3 completo | No aplica |
| `ccpa` | Skill `ccpa`, Paso 3 completo | No aplica |

---

## Paso 3 — Issues transversales

Después de completar todas las auditorías jurisdiccionales, identificar issues
que incumplen múltiples leyes simultáneamente. Consolidar en una sola entrada —
no repetir el mismo problema en cada sección.

Patrones de issues transversales frecuentes:

| Issue | RGPD | Ley 21.719 | UK GDPR | LGPD | Ley 25.326 | LFPDPPP | nFADP | CCPA/CPRA |
|-------|------|-----------|---------|------|-----------|---------|-------|----------|
| Política / aviso inexistente | Art. 13/14 | Art. 14 | Art. 13/14 | Art. 9 | Art. 6.2 | Art. 15-16 | Art. 19 | § 1798.130 |
| Sin base jurídica declarada | Art. 6 | Art. 12 | Art. 6 | Art. 7 | Art. 5-6 | Art. 8-10 | Art. 6 | § 1798.110 |
| Cookies sin consentimiento previo | Art. 7 + ePrivacy | Art. 12 | PECR Reg. 6 | Art. 7.I | Art. 5.1 | Art. 8 | Art. 6 + DSG-Praxis | § 1798.120/121 (opt-out) |
| Sin canal de ejercicio de derechos | Art. 12 | Art. [derechos] | Art. 12 | Art. 18 | Art. 14-16 | Art. 22-27 | Art. 25-32 | § 1798.130 |
| Transferencias int. no declaradas | Art. 44 | Art. 26 | Art. 44 UK | Art. 33 | Art. 12 | Art. 36-37 | Art. 16-17 | § 1798.115 |
| Datos sensibles sin consentimiento explícito | Art. 9 | Art. 16 | Art. 9 | Art. 11 | Art. 7 | Art. 9 | Art. 31 | § 1798.121 (SPI) |
| Sin identificación del responsable | Art. 13.1(a) | Art. 5 | Art. 13.1(a) | Art. 9.I | Art. 6.2(a) | Art. 16.I | Art. 19.2(a) | § 1798.130 |
| Sin HTTPS | Art. 32 | Art. 19 | Art. 32 | Art. 46 | Art. 9 | Art. 19 | Art. 8 | § 1798.150 (riesgo acción privada) |

Formato de issue transversal:
```
**[Nombre del issue]** (transversal — múltiples jurisdicciones)
Evidencia: [qué se encontró o qué falta]
Referencias: [RGPD Art. X] · [Ley 21.719 Art. Y] · [UK GDPR Art. Z] · [LGPD Art. W]
Riesgo combinado: [estimación del mayor riesgo sancionador entre las jurisdicciones]
→ Acción: [una sola acción que resuelve en todas las jurisdicciones]
```

---

## Paso 4 — Score consolidado y output

### Scores

```
| Jurisdicción | Score | Estado                |
|---|---|---|
| RGPD          | X/100 | Cumple / Riesgo moderado / Riesgo alto / Riesgo crítico |
| Ley 21.719    | X/100 | ...                   |
| UK GDPR       | X/100 | ...                   |
| LGPD          | X/100 | ...                   |
| Ley 25.326    | X/100 | ...                   |
| LFPDPPP       | X/100 | ...                   |
| nFADP         | X/100 | ...                   |
| CCPA/CPRA     | X/100 | ...                   |
| Score global  | X/100 | Promedio de jurisdicciones auditadas |
```

### Output sin `--docx` (Markdown)

```
# Auditoría de Privacidad — [dominio]
Fecha: [fecha] | Jurisdicciones: [lista] | Score global: X/100

## Stack tecnológico  ← una sola sección, compartida
...

## [Jurisdicción 1] — Score: X/100   ← una sección por cada jurisdicción auditada
[tabla de bloques + issues críticos + issues medios]

## [Jurisdicción 2] — Score: X/100
[tabla de bloques + issues críticos + issues medios]

## ...  ← repetir para todas las jurisdicciones activas

## Issues transversales
[issues que afectan a múltiples jurisdicciones — consolidados]

## Próximos pasos priorizados
[top 5 acciones — priorizadas por impacto combinado entre jurisdicciones]
```

Nombres de sección por jurisdicción: RGPD · Ley 21.719 (Chile) · UK GDPR · LGPD (Brasil) · Ley 25.326 (Argentina) · LFPDPPP (México) · nFADP (Suiza) · CCPA/CPRA (California)

### Output con `--docx`

Preguntar primero: "¿El informe es para uso interno o para entregar al cliente?"

Estructura del .docx:
1. Portada: dominio, fecha, jurisdicciones auditadas, score global
2. Resumen ejecutivo: un párrafo por jurisdicción + top 5 acciones urgentes
3. Stack tecnológico (sección única compartida)
4. Una sección por jurisdicción con tabla de cumplimiento, issues críticos y medios
5. Issues transversales: issues que afectan a múltiples jurisdicciones
6. Próximos pasos priorizados por impacto combinado
7. Nota metodológica: alcance, qué no se auditó, incertidumbres normativas
8. Pie de página en todas las páginas: "Desarrollado por Zythos Media — Especialistas
   en SEO & IA Search" con hipervínculo a https://zythos.media

Guardar en `<directorio-de-auditorias>/[cliente]/auditoria_privacidad_[fecha].md` o `.docx`.

---

## Integración con `/seo audit`

`/seo audit <url>` lanza este orquestador automáticamente cuando detecta señales
de privacidad relevantes en cualquier jurisdicción. El stack tecnológico detectado
por seo-audit se pasa al orquestador — no repetir Paso 0 si ya está disponible.

---

## Añadir nuevas jurisdicciones

Para incorporar una nueva ley al orquestador:
1. Crear `.claude/skills/[nombre]/SKILL.md` con estructura de 10 bloques
2. Añadir fila en la tabla de jurisdicciones de este skill (sección "Jurisdicciones disponibles")
3. Añadir señales de detección en la matriz del Paso 1
4. Añadir fila en la tabla del Paso 2
5. Añadir columna en la tabla de issues transversales del Paso 3
6. Añadir fila en la tabla de scores del Paso 4
7. Añadir el nombre de sección en la nota de nombres de la plantilla Markdown del Paso 4
8. Actualizar `scripts/patch_claude_seo.py`: añadir nuevo caso OLD (la línea anterior) → NEW (8+1 jurisdicciones) si la línea de seo-audit cambia
9. Actualizar `CLAUDE.md` (sección skills + descripción de patch_claude_seo.py)
10. Actualizar memoria `project_privacidad_suite.md`
