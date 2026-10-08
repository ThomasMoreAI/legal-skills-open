# Sistema de diseño del portal

Este documento define la dirección visual, los componentes y las reglas de experiencia de usuario del portal público de **Normativa Educativa Canaria**.

Su objetivo es mantener una interfaz coherente, accesible y trazable cuando una persona o un agente de IA cree o modifique páginas del portal. No sustituye las reglas editoriales de `AGENTS.md` ni cambia el formato del corpus Markdown/YAML.

## 1. Alcance

Este sistema se aplica a:

- la portada pública de GitHub Pages;
- futuras páginas de consulta de normativa, currículos y relaciones;
- buscadores, filtros, listados y fichas de detalle;
- componentes reutilizables del portal;
- documentación visual y ejemplos de uso del corpus.

No se aplica al contenido normativo original ni obliga a introducir un framework frontend concreto.

## 2. Objetivos del producto

El portal debe permitir que una persona pueda:

1. identificar rápidamente qué contiene el corpus;
2. buscar una norma, currículo o materia;
3. reconocer el estado de vigencia y la fecha de consulta;
4. acceder a la fuente oficial sin ambigüedad;
5. comprender las relaciones entre normas y currículos;
6. copiar recursos preparados para sistemas de IA;
7. distinguir hechos, interpretación, hipótesis y datos pendientes.

## 3. Principios de diseño

### 3.1 Institucional, no burocrático

La interfaz debe transmitir rigor y pertenencia al contexto educativo de Canarias sin reproducir la densidad visual de un boletín oficial.

### 3.2 Legibilidad antes que decoración

La tipografía, el contraste, el ancho de lectura y la jerarquía de contenido tienen prioridad sobre ilustraciones, efectos o animaciones.

### 3.3 La fuente oficial siempre es visible

Toda ficha normativa debe presentar el acceso a la fuente oficial como una acción principal, no como un enlace secundario oculto al final de la página.

### 3.4 El estado no depende solo del color

Los estados como `Vigente`, `Derogada` o `Pendiente de verificación` deben incluir texto e iconografía o forma diferenciada. El color es un refuerzo, no el único indicador.

### 3.5 Personas y máquinas comparten la misma fuente de verdad

El portal transforma el corpus en una experiencia navegable, pero Markdown, YAML, `llms.txt`, `llms-full.txt` y `SKILL.md` continúan siendo recursos públicos de primer nivel.

### 3.6 Mejora progresiva

El contenido esencial debe ser accesible sin JavaScript. La búsqueda, el filtrado, la copia al portapapeles y otras interacciones pueden añadirse como mejora progresiva.

### 3.7 Densidad informativa controlada

Las fichas pueden contener muchos metadatos, pero deben agruparse por relevancia y mostrarse mediante divulgación progresiva cuando sea necesario.

## 4. Arquitectura de información

La navegación principal debe utilizar conceptos comprensibles para personal docente y técnico:

- Inicio
- Normativa
- Currículos
- Relaciones
- Buscar
- Uso con IA
- Metodología

Los identificadores internos como `NOR-001`, `CUR-001` o `REL-001` deben ser visibles, pero no sustituir al título humano de la entidad.

## 5. Identidad visual

### 5.1 Paleta base

La identidad actual del portal se mantiene como punto de partida.

| Token | Valor de referencia | Uso |
| --- | --- | --- |
| `--color-surface` | `#FFFFFF` | Fondo principal |
| `--color-surface-muted` | `#F5F7FA` | Fondos secundarios |
| `--color-text` | `#0E1A2E` | Texto principal |
| `--color-text-secondary` | `#2C3A52` | Texto secundario |
| `--color-text-muted` | `#6B7791` | Metadatos y ayudas |
| `--color-primary` | `#0072CE` | Azul institucional y acciones principales |
| `--color-accent` | `#F0AB00` | Acentos, avisos y referencia a Canarias |
| `--color-border` | `#DCE1E8` | Separadores y bordes |
| `--color-code-surface` | `#0E1A2E` | Bloques técnicos |
| `--color-code-text` | `#F2F5FA` | Texto en bloques técnicos |

Los valores pueden ajustarse tras una auditoría de contraste. Los componentes deben consumir tokens semánticos y no colores hexadecimales dispersos.

### 5.2 Colores de estado

| Estado semántico | Uso |
| --- | --- |
| Positivo | Norma vigente o validación completada |
| Informativo | Contenido histórico, relación o dato auxiliar |
| Advertencia | Pendiente de verificación, revisión necesaria o fecha antigua |
| Crítico | Norma derogada, error o fuente no disponible |
| Neutral | Sustituida, obsoleta o sin clasificación concluyente |

Cada estado debe incluir una etiqueta textual completa.

### 5.3 Tipografía

La jerarquía recomendada es:

- **Sans serif:** navegación, cuerpo, formularios, tablas y botones.
- **Serif:** títulos editoriales de alto nivel, si se mantiene la identidad actual.
- **Monoespaciada:** IDs, rutas, fragmentos YAML, prompts y datos técnicos.

La carga de fuentes externas no debe impedir la lectura. Siempre se deben definir alternativas del sistema.

Escala orientativa:

| Nivel | Tamaño mínimo orientativo |
| --- | --- |
| Título principal | `clamp(2.5rem, 7vw, 4.25rem)` |
| Título de sección | `clamp(1.75rem, 4vw, 2.25rem)` |
| Título de ficha | `clamp(1.5rem, 3vw, 2rem)` |
| Cuerpo | `1rem` |
| Metadatos | `0.875rem` |
| Etiquetas | `0.75rem` |

El cuerpo no debe bajar de `16px` en páginas de lectura normativa.

### 5.4 Espaciado

Usar una escala consistente basada en múltiplos de cuatro:

```css
:root {
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
}
```

No introducir valores arbitrarios cuando exista un token equivalente.

### 5.5 Bordes, radios y sombras

- Radio pequeño: `4px`, para etiquetas y controles compactos.
- Radio medio: `8px`, para botones, avisos y bloques técnicos.
- Radio grande: `12px`, para tarjetas principales.
- Las sombras deben ser discretas y no sustituir a un borde visible.
- Los elementos interactivos deben conservar un contorno de foco claro.

### 5.6 Ancho de contenido

- Contenedor general: máximo aproximado de `1180px`.
- Texto normativo: entre `65ch` y `78ch`.
- Tablas y diagramas pueden ocupar el ancho completo del contenedor.
- Las líneas de texto no deben extenderse a todo el ancho en pantallas grandes.

## 6. Componentes

### 6.1 Cabecera del sitio

Debe incluir:

- nombre del portal;
- enlace a inicio;
- navegación principal;
- acceso visible a búsqueda;
- enlace al repositorio o a los recursos para IA cuando corresponda.

En móvil, la navegación debe seguir siendo utilizable mediante teclado y lector de pantalla.

### 6.2 Hero de portada

Debe responder en pocos segundos a:

- qué es el portal;
- a quién sirve;
- qué se puede hacer;
- por qué no sustituye a la fuente oficial.

La portada no debe depender de un código QR para su acción principal.

### 6.3 Buscador

El buscador es un componente prioritario. Debe admitir:

- texto libre;
- búsqueda por ID;
- búsqueda por título o nombre corto;
- filtrado por ámbito, etapa, tipo y estado de vigencia;
- ordenación comprensible;
- URL compartible con los filtros aplicados, cuando sea técnicamente posible.

Debe mostrar el número de resultados y ofrecer un estado vacío útil.

### 6.4 Barra de filtros

Los filtros deben:

- tener etiqueta visible;
- permitir limpiar todos los criterios;
- mostrar los filtros activos;
- evitar controles personalizados si un elemento HTML nativo resuelve el caso;
- mantenerse utilizables en pantallas estrechas.

### 6.5 Tarjeta normativa

Contenido mínimo:

- ID estable;
- título o nombre corto;
- tipo de norma;
- ámbito;
- estado de vigencia;
- fecha de publicación o consulta relevante;
- breve resumen;
- enlace a la ficha;
- enlace a la fuente oficial cuando no genere ruido excesivo.

La tarjeta completa no debe convertirse en un único enlace si contiene varias acciones distintas.

### 6.6 Tarjeta curricular

Contenido mínimo:

- ID estable;
- etapa;
- materia, área o ámbito;
- estado de extracción;
- norma de referencia;
- fecha de consulta;
- enlace a la ficha.

### 6.7 Etiqueta de estado

La etiqueta debe combinar:

- texto explícito;
- color semántico;
- borde o forma reconocible;
- ayuda contextual cuando el estado sea complejo.

Ejemplos:

- `Vigente`
- `Derogada`
- `Sustituida`
- `Pendiente de verificación`
- `Histórica`

No abreviar estados en interfaces dirigidas al público general.

### 6.8 Bloque de fuente oficial

Debe destacar:

- autoridad;
- título de la fuente;
- fecha de consulta;
- formato disponible;
- acción `Consultar fuente oficial`;
- advertencia cuando el HTML no sea la versión oficial y el PDF sí lo sea.

### 6.9 Tabla de metadatos

Usar una lista de definición en pantallas estrechas y una tabla cuando exista comparación entre varias entidades.

Los valores vacíos no deben mostrarse como cadenas vacías. Utilizar `No disponible`, `No aplica` o `Pendiente`, según corresponda.

### 6.10 Relaciones normativas

Las relaciones deben indicar siempre:

- entidad de origen;
- tipo de relación;
- entidad de destino;
- evidencia;
- nivel de evidencia;
- fecha de registro.

En una primera versión puede usarse una lista estructurada. Un grafo visual solo debe añadirse si mantiene accesible una alternativa textual equivalente.

### 6.11 Aviso normativo

El aviso de que el resumen no sustituye la fuente oficial debe:

- aparecer antes del contenido interpretativo;
- usar `role="note"` cuando resulte apropiado;
- ser visible sin dominar toda la página;
- mantener el mismo texto base en todas las fichas.

### 6.12 Bloque técnico o de prompt

Se utiliza para:

- prompts;
- fragmentos YAML;
- comandos;
- rutas;
- ejemplos de integración con IA.

Debe incluir una acción de copia accesible y mostrar confirmación sin depender únicamente de un cambio de color.

### 6.13 Estados de interfaz

Toda vista dinámica debe definir:

- cargando;
- sin resultados;
- error recuperable;
- error no recuperable;
- datos incompletos;
- contenido desactualizado.

Los mensajes deben explicar la siguiente acción disponible.

### 6.14 Pie de página

Debe incluir:

- propósito del corpus;
- advertencia sobre fuentes oficiales;
- enlace al repositorio;
- metodología;
- recursos para IA;
- información de mantenimiento o fecha de actualización cuando aporte valor.

## 7. Plantillas de página

### 7.1 Inicio

Orden recomendado:

1. propuesta de valor;
2. búsqueda principal;
3. accesos a normativa y currículos;
4. estado del corpus;
5. ejemplos de consulta;
6. uso con IA;
7. metodología y advertencia.

### 7.2 Listado de normativa

Debe incluir:

1. título y descripción;
2. buscador y filtros;
3. resumen de resultados;
4. tarjetas o filas;
5. paginación o carga progresiva;
6. acceso a datos estructurados.

### 7.3 Ficha normativa

Orden recomendado:

1. ID, título y estado;
2. fuente oficial y advertencia;
3. resumen;
4. objeto y ámbito;
5. fechas y metadatos;
6. artículos, disposiciones o anexos clave;
7. relaciones;
8. impacto en Canarias;
9. dudas abiertas;
10. archivos Markdown/YAML y recursos para IA.

### 7.4 Ficha curricular

Orden recomendado:

1. ID, etapa y materia;
2. norma de referencia;
3. estado de extracción;
4. competencias y criterios;
5. saberes básicos;
6. relaciones normativas;
7. fuente oficial;
8. archivos Markdown/YAML.

### 7.5 Página de búsqueda

Debe permitir conservar y compartir la consulta. Los resultados deben mostrar por qué coinciden cuando sea posible.

## 8. Diseño adaptable

Puntos de control orientativos:

- compacto: menos de `640px`;
- intermedio: `640px` a `959px`;
- amplio: `960px` o más.

Reglas:

- no ocultar contenido esencial en móvil;
- convertir rejillas de varias columnas en una sola columna;
- permitir desplazamiento horizontal controlado en tablas;
- mantener objetivos táctiles de al menos `44px`;
- evitar encabezados fijos que ocupen una parte excesiva de la pantalla;
- conservar visibles el título, el estado y la fuente oficial de cada ficha.

## 9. Accesibilidad

El objetivo mínimo es WCAG 2.2 nivel AA.

Requisitos:

- HTML semántico antes que componentes genéricos;
- enlace para saltar al contenido principal;
- navegación completa mediante teclado;
- foco visible;
- contraste suficiente;
- etiquetas asociadas a controles;
- mensajes de error vinculados al campo correspondiente;
- encabezados en orden lógico;
- texto alternativo útil;
- tablas con encabezados correctos;
- respeto a `prefers-reduced-motion`;
- no transmitir información solo mediante color, posición o icono;
- idioma de la página declarado como español.

## 10. Movimiento e interacción

- Las transiciones deben ser breves y funcionales.
- Evitar animaciones continuas salvo que comuniquen estado.
- No desplazar contenido inesperadamente al cargar.
- Los botones deben describir la acción: `Copiar prompt`, `Consultar fuente oficial`, `Limpiar filtros`.
- Los enlaces deben describir el destino y no usar textos genéricos como `Más información` cuando exista una alternativa clara.

## 11. Reglas de contenido

- Usar español claro y directo.
- Mantener la denominación oficial de normas, autoridades y etapas.
- No presentar una interpretación como hecho.
- Mostrar `[INTERPRETACIÓN]`, `[HIPÓTESIS]` y `[PENDIENTE]` cuando existan en el corpus.
- No ocultar la fecha de consulta.
- No afirmar vigencia si el corpus indica que está pendiente de verificación.
- Mantener la advertencia de que el resumen no sustituye la fuente oficial.
- Evitar párrafos introductorios largos antes de los datos relevantes.

## 12. Implementación técnica

### 12.1 Fuente de verdad

El portal debe consumir o transformar los archivos existentes sin duplicar manualmente sus datos:

- `02_normativa/`;
- `03_curriculos/`;
- `05_relaciones/`;
- `06_indices/`;
- `07_corpus_ia/`.

### 12.2 Primera fase

La portada estática puede continuar en `docs/`, pero debe evolucionar hacia esta separación:

```text
docs/
├── index.html
└── assets/
    ├── css/
    │   ├── tokens.css
    │   ├── base.css
    │   ├── components.css
    │   └── pages.css
    └── js/
        └── site.js
```

### 12.3 Fase de portal navegable

Cuando se incorporen fichas generadas y búsqueda, se recomienda un generador estático que:

- lea Markdown y YAML locales;
- valide esquemas;
- genere HTML estático;
- preserve las URLs de `llms.txt`, `llms-full.txt` y `SKILL.md`;
- no requiera base de datos ni servidor de aplicaciones;
- permita indexación estática y filtros.

La elección del generador debe documentarse en una decisión editorial o técnica antes de su implantación.

### 12.4 JavaScript

- JavaScript no debe ser necesario para leer el contenido principal.
- Evitar dependencias grandes para interacciones simples.
- No insertar HTML con datos sin escapar.
- Mantener los eventos en archivos separados cuando el código deje de ser trivial.
- Proporcionar estados y mensajes accesibles para acciones de copia y filtrado.

### 12.5 CSS

- Utilizar propiedades personalizadas semánticas.
- Evitar estilos en línea salvo excepciones justificadas.
- Organizar estilos por tokens, base, componentes y páginas.
- No acoplar un componente a una única página mediante selectores excesivamente específicos.
- Comprobar estados `hover`, `focus-visible`, `active` y `disabled`.

## 13. Reglas para agentes de IA

Antes de modificar la interfaz, un agente debe:

1. leer `README.md`, `AGENTS.md` y este `DESIGN.md`;
2. identificar el componente o plantilla afectada;
3. reutilizar tokens y componentes existentes;
4. conservar el contenido y las URLs públicas salvo requisito explícito;
5. comprobar la experiencia sin JavaScript cuando aplique;
6. revisar teclado, foco, contraste y diseño adaptable;
7. evitar introducir un framework o dependencia sin decisión documentada;
8. incluir en el PR capturas o una descripción verificable de los cambios visuales cuando sea posible.

Un agente no debe:

- copiar la identidad visual de otro producto;
- inventar datos normativos para completar una maqueta;
- sustituir IDs por slugs inestables;
- eliminar enlaces a fuentes oficiales;
- ocultar estados de vigencia o fechas de consulta;
- usar color como único indicador;
- introducir animaciones o efectos sin utilidad funcional;
- convertir el portal en una aplicación cliente compleja sin necesidad demostrada.

## 14. Criterios de aceptación visual

Antes de cerrar un cambio de interfaz, verificar:

- [ ] La jerarquía de encabezados es correcta.
- [ ] La fuente oficial es visible y comprensible.
- [ ] El estado de vigencia incluye texto.
- [ ] El contenido principal funciona sin JavaScript, cuando corresponde.
- [ ] La navegación es utilizable con teclado.
- [ ] El foco es visible.
- [ ] Los controles tienen etiquetas.
- [ ] El diseño funciona a `320px` de ancho.
- [ ] Las tablas no rompen la página.
- [ ] Los contrastes cumplen el objetivo AA.
- [ ] Los recursos `llms.txt`, `llms-full.txt` y `SKILL.md` conservan sus URLs.
- [ ] No se han duplicado manualmente datos que ya existen en YAML o Markdown.
- [ ] El PR explica cualquier nueva dependencia.

## 15. Evolución prevista

Orden recomendado:

1. formalizar tokens y componentes a partir de la portada existente;
2. separar CSS y JavaScript del HTML;
3. crear componentes de tarjeta, estado y fuente oficial;
4. generar listados de normativa y currículos desde los índices;
5. incorporar búsqueda estática y filtros;
6. generar fichas de detalle;
7. representar relaciones con alternativa textual accesible;
8. auditar accesibilidad, rendimiento y enlaces.

Este documento debe actualizarse cuando cambien decisiones visuales o patrones reutilizables. Los cambios puntuales de contenido no requieren modificarlo.