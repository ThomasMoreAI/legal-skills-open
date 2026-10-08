---
name: abogacia-argentina-bitcoindefi
title: Abogacía Argentina · Router del sistema Agente Smith
description: 'Punto de entrada para práctica jurídica argentina: fija las reglas de operación (jurisdicción primero, fuente primaria SAIJ, marcadores de verificación pendiente, alerta normativa, cómputo diferenciado de plazos) y rutea por área del derecho (laboral, civil, penal, familia, consumidor, societario, administrativo, previsional, tributario, tránsito, faltas municipales, protección de datos) hacia sus ejes normativos y las sub-skills plazos/diagnóstico/bucles. Usar en cualquier consulta o trabajo de abogacía bajo derecho argentino.'
author: Bitcoindefi
author_url: https://github.com/Bitcoindefi/agente-smith/tree/main/skills/abogacia-argentina
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ar
practice: regulatory
language: es
---

# Abogacía Argentina · Router del sistema Agente Smith

Skill original de Agente Smith (MIT). El sistema asiste el análisis jurídico; **no
reemplaza el juicio ni la firma del abogado** y no constituye asesoramiento legal.

## Reglas de operación (siempre, no negociables)

1. **Jurisdicción primero.** Nacional/federal ≠ CABA ≠ provincias: cambian el código
   procesal, los plazos y la autoridad competente. Si el fuero no está definido,
   preguntarlo antes de computar plazos o citar procedimiento. Si el workspace tiene
   fichas de jurisdicción (`jurisdicciones/`), leer la que corresponda.
2. **Fuente primaria antes de afirmar.** Toda norma o fallo se verifica en SAIJ (MCP
   `saij`: `saij_buscar_legislacion`, `saij_buscar_jurisprudencia`, `saij_documento`)
   leyendo el texto real. La norma se cita por lo que dice, no por lo que se recuerda.
3. **Verificación pendiente.** Jamás inventar jurisprudencia, carátulas, números de
   fallo o citas. Lo no verificado se marca 🔲 y se dice qué falta confirmar.
4. **Alerta normativa.** En zonas de reforma reciente o discusión de vigencia, marcar
   ⚠️ con la fecha de corte del conocimiento y verificar el texto actualizado.
5. **Plazos diferenciados.** Hábiles judiciales ≠ hábiles administrativos ≠ corridos.
   Todo vencimiento pasa por la skill `argentina-plazos`.
6. **Casos privados.** El contenido de `casos/` es local y confidencial: nunca va a
   repos, memoria persistente ni servicios externos.
7. **La pieza manda el formato.** Antes de redactar, identificar el TIPO de
   presentación y el órgano destinatario, y usar el molde de la skill
   `argentina-formatos` — un descargo de faltas NO es una demanda con petitorio.
   Si el tipo de pieza no surge del pedido, preguntar antes de redactar.

## Ruteo por área — ejes normativos de partida

Puntos de entrada para la búsqueda (verificar SIEMPRE el texto vigente en SAIJ; no
son citas listas para usar):

| Área | Ejes normativos de partida |
|------|---------------------------|
| Laboral | LCT 20.744 · riesgos del trabajo 24.557 · empleo 24.013 · reformas recientes ⚠️ |
| Civil y comercial | CCCN (Ley 26.994): contratos, daños, prescripción |
| Familia | CCCN Libro Segundo · protección integral 26.061 · violencia 26.485 |
| Consumidor | LDC 24.240 y modificatorias · lealtad comercial |
| Societario | LGS 19.550 · normativa del registro público de la jurisdicción |
| Administrativo | LNPA 19.549 y reglamento (nacional) · ley de procedimiento local ⚠️ por jurisdicción |
| Previsional | Ley 24.241 (SIPA) · regímenes especiales · normativa ANSES |
| Concursos | LCQ 24.522 |
| Tributario | Ley 11.683 (nacional) · códigos fiscales locales |
| Tránsito | Ley 24.449 · Ley 26.363 (ANSV) · adhesiones y códigos de faltas locales ⚠️ |
| Protección de datos | Ley 25.326 · normativa AAIP ⚠️ reforma en discusión |
| Penal | CP · CPPF (federal, implementación progresiva ⚠️) · CPP de cada provincia |

## Sub-perfil: Faltas Municipales / Contravencional

La mecánica de faltas municipales (ej. multas de estacionamiento o tránsito local) difiere del área "tránsito" nacional. Las ordenanzas locales **casi nunca están en SAIJ**, por lo que deben verificarse en fuentes oficiales del municipio.

- **Procedimiento típico**: Acta → Notificación → Pago voluntario reducido → Juzgamiento (Descargo).
- **Advertencia normativa ⚠️**: Verificar siempre el Código de Faltas y las ordenanzas locales aplicables en portales municipales.
- **Prescripción**: Cotejar el plazo local de prescripción vs. el art. 89 de la Ley Nacional de Tránsito 24.449 (evaluando el texto original vs. la reforma de la Ley 26.363 y el grado de adhesión local).
- **Pago voluntario**: Evaluar conveniencia y procedencia.

### Checklist de defensa frecuente:
- [ ] **Falta de notificación** (afecta el debido proceso y derecho de defensa).
- [ ] **Atipicidad de zona o conducta** (ej. zona no señalizada, excepción de carga y descarga).
- [ ] **Nulidad del acta** (art. 70 LNT o incumplimiento de requisitos formales del código local).
- [ ] **Prescripción** (tiempo transcurrido desde la infracción o última actuación).
- [ ] **Procedencia de pago voluntario**.

## Sub-skills

- **`argentina-formatos`** — anatomía de cada tipo de presentación (demanda, descargo,
  recurso, nota, etc.): el molde se elige ANTES de redactar.
- **`argentina-plazos`** — cómputo de todo plazo, prescripción o caducidad.
- **`argentina-diagnostico`** — auditoría de un escrito ya redactado, antes de presentar.
- **`argentina-bucles`** — construcción de un escrito nuevo desde cero, con fuentes.
- **`saij-argentina`** — documentación del conector SAIJ (búsquedas y texto completo).

## Flujo de trabajo sobre un caso

1. Leer `FICHA.md` del caso (y su archivo maestro si lo indica) + reglas estratégicas.
2. Confirmar jurisdicción/fuero y leer su ficha en `jurisdicciones/`.
3. Identificar el área y sus ejes normativos; verificar los textos en SAIJ.
4. Trabajar con la sub-skill que corresponda (plazos / diagnóstico / bucles).
5. Registrar fuentes verificadas (uuid + URL) en la carpeta del caso.
6. Toda decisión estratégica o irreversible vuelve al abogado.
