# Checklist Accesibilidad (WCAG 2.2 AA + EAA / EN 301 549)

Desde el 28 de junio de 2025, el European Accessibility Act (Directiva 2019/882) es exigible en todos los Estados miembro UE. Afecta a sitios y apps comerciales de comercio electrónico, servicios bancarios, transporte, audiolibros, comunicaciones, y más. Spain transpone via Ley 11/2023 y RD 193/2023. El estándar técnico de referencia es **EN 301 549** que se alinea con **WCAG 2.2 AA**.

Las herramientas automáticas detectan solo ~30-40% de las violaciones WCAG. El resto requiere verificación manual. Marca claramente en el informe qué checks son automáticos y cuáles requieren auditoría humana.

## Herramientas a usar

Intenta este orden:

### Lighthouse (viene con Chrome/Node)

```bash
# Si tienes node y lighthouse instalado
npx lighthouse <URL> --only-categories=accessibility --output=json --output-path=<output-dir>/lighthouse.json
```

### axe-core (cli)

```bash
npx @axe-core/cli <URL> --dir <output-dir>/axe
```

### Pa11y

```bash
npx pa11y <URL> --standard WCAG2AA --reporter json > <output-dir>/pa11y.json
```

Si ninguna herramienta está disponible, haz un subset manual navegando con Claude in Chrome.

## A11Y-001 — Contraste de color (WCAG 1.4.3)

Texto normal: ratio ≥ 4.5:1. Texto grande (≥18pt o ≥14pt bold): ratio ≥ 3:1.

Lighthouse/axe lo detectan automáticamente.

**Severidad**: MEDIA a ALTA.

## A11Y-002 — Alt text en imágenes (WCAG 1.1.1)

Todas las imágenes informativas deben tener `alt` descriptivo. Decorativas: `alt=""`.

**Severidad**: MEDIA.

## A11Y-003 — Labels en formularios (WCAG 1.3.1, 3.3.2)

Cada input con su `<label for="...">` asociado o `aria-label`. Placeholder no sustituye label.

**Severidad**: ALTA. Impacta también usabilidad.

## A11Y-004 — Navegación por teclado (WCAG 2.1.1)

Todo elemento interactivo debe ser accesible con tab. Focus visible. No debe haber trampas de foco (modal que no se puede cerrar con Esc).

**Verificación**: manual — navega con tab por la página.

**Severidad**: ALTA.

## A11Y-005 — Jerarquía de encabezados (WCAG 1.3.1)

Un solo `<h1>`, secuencia lógica h1→h2→h3.

**Severidad**: MEDIA.

## A11Y-006 — `<html lang>` correcto (WCAG 3.1.1)

Atributo lang presente y correcto. Si el contenido es en español, `lang="es"`. Hallazgo típico: páginas creadas en constructores internacionales quedan con `lang="en"` por defecto.

**Severidad**: MEDIA.

## A11Y-007 — Tamaños táctiles mínimos (WCAG 2.5.8, nuevo en 2.2)

Botones y enlaces clicables: al menos 24×24 px (WCAG AA) idealmente 44×44 (AAA).

**Severidad**: MEDIA.

## A11Y-008 — Zoom y reflow (WCAG 1.4.10)

Al hacer zoom al 400% en viewport 320px CSS, el contenido se reordena sin pérdida.

**Verificación**: manual con resize de viewport.

**Severidad**: MEDIA.

## A11Y-009 — Focus Appearance (WCAG 2.2 nuevo)

El indicador de foco debe ser visible y distinguible. Ratio contraste ≥ 3:1 vs estado no enfocado.

**Severidad**: MEDIA.

## A11Y-010 — Declaración de accesibilidad

La ley española (RD 1112/2018 + RD 193/2023) exige para sector público — y recomienda para comercio electrónico afectado por EAA — publicar una **Declaración de Accesibilidad** accesible desde el footer indicando:
- Nivel de conformidad
- Contenidos no accesibles (si los hay) con justificación
- Mecanismo de reclamación

**Severidad**: ALTA para entidades del sector público. MEDIA para privadas afectadas por EAA.

## Sanciones EAA en España

La transposición (Ley 11/2023) prevé sanciones por incumplimiento:
- Leves: hasta 30.000 €
- Graves: 30.001-100.000 €
- Muy graves: 100.001-600.000 €

Aplicable desde 28-jun-2025 a productos/servicios dentro del alcance del anexo I de la Directiva.
