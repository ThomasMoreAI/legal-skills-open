---
name: lgpd-carlosuhart
title: LGPD — Auditoría de Cumplimiento (Lei 13.709/2018, Brasil)
description: Audita un sitio web frente a la Lei Geral de Proteção de Dados Pessoais (LGPD — Lei 13.709/2018, Brasil). Detecta el sector automáticamente. Produce informe de cumplimiento con score, tabla de estado por artículo e issues priorizados con cuantificación de sanciones en BRL. Sub-skill del orquestador /privacidad — también invocable directamente.
author: carlosuhart
author_url: https://github.com/carlosuhart/seo-audit-skills/tree/main/skills/lgpd
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: es
---

# LGPD — Auditoría de Cumplimiento (Lei 13.709/2018, Brasil)

## Uso

```
/lgpd https://exemplo.com.br
/lgpd https://exemplo.com.br --docx
```

Sin `--docx` el output es Markdown interno. Con `--docx` genera informe
ejecutivo en formato Word.

Si el usuario no especifica formato, preguntar antes de generar el documento.

---

## Marco normativo

- **LGPD (Lei 13.709/2018)**: Ley General de Protección de Datos Personales.
  En vigor desde septiembre 2020. Aplicación de sanciones desde agosto 2021.
- **ANPD (Autoridade Nacional de Proteção de Dados)**: autoridad reguladora.
  Creada por la LGPD, constituida en noviembre 2020. Emite resoluciones y directrices.
- **Ámbito de aplicación (Art. 3)**: aplica a cualquier operación de tratamiento
  realizada en Brasil, o cuyos datos hayan sido recogidos en Brasil, o que tenga
  por objeto ofrecer bienes o servicios a personas en Brasil, independientemente
  de dónde esté el responsable.

⚠️ La LGPD es normativa brasileña. No confundir con el RGPD europeo, aunque
tiene estructura similar. Son marcos jurídicos independientes. Brasil tiene
decisión de adecuación de la UE (flujo UE → Brasil permitido sin garantías adicionales).

**Nota sobre madurez regulatoria:** La ANPD es una autoridad en proceso de
consolidación. Algunas disposiciones de la LGPD (en particular sobre transferencias
internacionales y el listado de países con adecuación) estaban aún siendo
reglamentadas a la fecha de esta versión. Señalar esta contingencia en el informe.

---

## Nota sobre idioma

La LGPD se aplica en Brasil. Los documentos de cumplimiento (aviso de privacidade,
política de cookies, termos de uso) deben estar en **portugués de Brasil** para
sitios que ofrecen servicios a usuarios brasileños. Si el sitio está en otro idioma
pero capta usuarios en Brasil, verificar si existe versión en PT-BR de los documentos legales.

Terminología LGPD (diferente del RGPD):

| LGPD (PT-BR) | RGPD equivalente |
|---|---|
| Titular | Interesado |
| Controlador | Responsable del tratamiento |
| Operador | Encargado del tratamiento |
| Encarregado de Dados | DPO / Delegado |
| Aviso de privacidade | Política de privacidad |
| Dado sensível | Dato de categoría especial |
| ANPD | Autoridad de control |

---

## Crédito de herramienta

Al iniciar cualquier auditoría, emitir esta línea antes del output principal:

> Desenvolvido por [Zythos Media](https://zythos.media) — Especialistas em SEO & IA Search

---

## Paso 0 — Identificación del stack tecnológico

Si este skill es invocado desde el orquestador `/privacidad`, usar el Paso 0
compartido. Si se invoca directamente, ejecutar el Paso 0 del skill `rgpd`.

Señales adicionales específicas de Brasil a detectar en el Paso 0:
- Presencia de CNPJ en el pie de página o política
- Integración con pasarelas brasileñas: Pix, PagSeguro, Mercado Pago, Cielo
- Plugins de e-commerce con soporte PT-BR: WooCommerce en portugués
- Integración con plataformas brasileñas: RD Station, Hotmart, Eduzz, Kiwify
- Google Analytics con audiencia Brasil mayoritaria (señal de monetización BR)

---

## Paso 1 — Recopilación de datos del sitio

Igual al skill `rgpd` Paso 1, adaptando las rutas:
- Rutas comunes en Brasil: `/privacidade`, `/politica-de-privacidade`,
  `/aviso-de-privacidade`, `/termos-de-uso`, `/politica-de-cookies`.
- Verificar también el rodapé (footer) para links "Privacidade" y "Cookies".

---

## Paso 2 — Detección de sector

Usar la matriz del skill `rgpd` más señales adicionales brasileñas:

| Sector | Señales específicas Brasil |
|--------|---------------------------|
| **Fintech** | Banco Central do Brasil, CMN, PIX, "autorizado pelo Bacen" |
| **Salud** | ANS (Agência Nacional de Saúde Suplementar), CFM, CRM, "plano de saúde" |
| **Educación** | MEC, INEP, "faculdade", "universidade", menores como audiencia |
| **Ecommerce** | Código de Defesa do Consumidor (CDC), RECLAMEAQUI, nota fiscal eletrônica |
| **LGPD high-risk** | Dados biométricos, scoring de crédito, monitoramento de comportamento em larga escala |

---

## Paso 3 — Auditoría por bloques

Evaluar cada bloque: **Cumpre / Parcial / Não cumpre / Não avaliável**

### Bloque 1 — Identificação do controlador (Art. 9.I + Art. 41)
Peso: 10 pts

Verificar en el aviso de privacidade:
- [ ] Razão social (razón social) o nombre completo del controlador
- [ ] CNPJ o CPF del controlador (no obligatorio por la LGPD pero su presencia
      permite identificación y es práctica estándar en Brasil)
- [ ] Endereço (domicilio) en Brasil, o representante en Brasil si es entidad extranjera
- [ ] Dirección de email o canal de contacto para el encarregado de dados (Art. 41.1)
- [ ] Datos de contacto del encarregado de dados publicados (ver Bloque 10)

**Entidad extranjera sin sede en Brasil (Art. 3):**
Si el controlador no tiene establecimiento en Brasil pero ofrece bienes/servicios
a titulares en Brasil o trata datos recogidos en Brasil:
- [ ] ¿La política identifica un representante o agente en Brasil?
- [ ] ¿El representante tiene dirección de contacto en Brasil publicada?

### Bloque 2 — Aviso de privacidade: existência e acesso (Art. 9 + Art. 48)
Peso: 5 pts

- [ ] Existe aviso de privacidade (política de privacidade) publicado
- [ ] Enlace visible en el rodapé de todas las páginas
- [ ] Enlace accesible desde formulários que recogen dados pessoais
- [ ] Redactado en portugués de Brasil (o en el idioma del sitio si el sitio no es en PT-BR)
- [ ] Data de última atualização visible

### Bloque 3 — Aviso de privacidade: contenido mínimo (Art. 9 I–IX)
Peso: 15 pts

La LGPD Art. 9 establece el derecho del titular a acceder a información clara
y adecuada sobre el tratamiento. Verificar que el aviso incluya (1 pt por ítem):

- [ ] **Art. 9.I:** Finalidade específica do tratamento — para qué se usan los datos
- [ ] **Art. 9.II:** Forma e duração do tratamento — cómo y por cuánto tiempo
- [ ] **Art. 9.III:** Identificação do controlador — quién trata los datos (ver Bloque 1)
- [ ] **Art. 9.IV:** Informações de contato do controlador — cómo contactarle
- [ ] **Art. 9.V:** Informações acerca do uso compartilhado de dados — con quién se comparten
- [ ] **Art. 9.VI:** Responsabilidades dos agentes que realizarão o tratamento — quién responde
- [ ] **Art. 9.VII:** Direitos do titular — lista de los 9 derechos (ver Bloque 6)
- [ ] **Base legal de cada finalidade** — cuál de las 10 bases del Art. 7 aplica (ver Bloque 4)
- [ ] **Dados sensíveis tratados** — si aplica, identificados explícitamente (ver Bloque 7)
- [ ] **Transferências internacionais** — si aplica, declaradas con garantías (ver Bloque 8)
- [ ] **Informações sobre cookies** — tecnologías de rastreo usadas
- [ ] **Contato do encarregado de dados** — nombre y email del Encarregado (ver Bloque 10)
- [ ] **Direito de reclamação à ANPD** — menciona el derecho de reclamar ante la ANPD
- [ ] **Legibilidade** — lenguaje claro, no jerga legal inaccesible
- [ ] **Formato acessível** — no enterrado en bloques de texto sin estructura

### Bloque 4 — Base legal do tratamento (Art. 7 + Art. 11)
Peso: 10 pts

La LGPD reconoce **10 bases legales** (Art. 7) para datos generales.
Para dados sensíveis aplican bases específicas del Art. 11.

**Bases legales Art. 7 (dados gerais):**
1. **Consentimento** do titular — livre, informado e inequívoco
2. **Cumprimento de obrigação legal** ou regulatória pelo controlador
3. **Execução de políticas públicas** pela Administração Pública
4. **Realização de estudos** por órgão de pesquisa (dados anonimizados preferentemente)
5. **Execução de contrato** ou procedimentos preliminares a pedido do titular
6. **Exercício regular de direitos** em processo judicial, administrativo ou arbitral
7. **Proteção da vida ou incolumidade física** do titular ou de terceiro
8. **Tutela da saúde** por profissional de saúde ou entidade sanitária
9. **Interesses legítimos** do controlador ou de terceiro (salvo direitos do titular prevaleçam)
10. **Proteção do crédito** — especificidad de la ley brasileña

Verificar:
- [ ] La política declara la base legal de cada finalidade (no una sola base genérica)
- [ ] No se usa "consentimento" cuando el tratamiento es necesario para executar contrato
- [ ] Cuando se invoca "intereses legítimos" (base 9): se identifica cuál es
- [ ] Los formulários de captação no usan casillas pre-marcadas para el consentimento
- [ ] El consentimento para dados sensíveis es explícito y diferenciado (Art. 11.I)

**Privacidade desde a concepção (Art. 46 + Art. 49):**
- [ ] Los formulários solicitan solo los dados estrictamente necesarios para la finalidade
- [ ] Las opciones de suscripción a comunicações comerciais no están preseleccionadas

### Bloque 5 — Consentimento, cookies e marketing direto (Art. 7.I + Art. 8)
Peso: 15 pts

La LGPD no tiene un artículo específico de cookies — los requisitos derivan de
las reglas generales de consentimento (Art. 7.I) y de la práctica de la ANPD.
La ANPD ha señalado que las cookies de rastreo no esenciales requieren consentimento
previo, libre, informado e inequívoco.

**Banner de cookies:**
- [ ] Existe banner o mecanismo de consentimento de cookies
- [ ] El banner bloquea cookies no esenciales hasta obtener consentimento activo
- [ ] No hay cookies de análise, publicidade ou rastreamento activas antes del consentimento
- [ ] Opção de rejeição tan accesible como la aceitação
- [ ] Configuração granular por categoria
- [ ] Enlace a política de cookies en el propio banner
- [ ] El consentimento es revogável fácilmente (Art. 8.5)

**Formulários:**
- [ ] Formulários con tratamento de dados incluyen checkbox de consentimento no pre-marcado
- [ ] El checkbox vincula al aviso de privacidade
- [ ] Finalidade concreta declarada antes de enviar

**Consentimento de crianças e adolescentes (Art. 14):**
La LGPD protege especialmente dados de **crianças** (hasta 12 años) y
**adolescentes** (13-17 años), conforme el Estatuto da Criança e do Adolescente (ECA):
- [ ] Si el sitio capta crianças (menores de 12): consentimento parental específico
      y en el mejor interés del menor (Art. 14.1)
- [ ] Si el sitio no va dirigido a menores: declararlo explícitamente

**Marketing direto:**
- [ ] Si hay newsletter o comunicações comerciais: mecanismo de descadastramento claro
- [ ] La política menciona el direito de oposição ao tratamento para fins comerciais

### Bloque 6 — Direitos do titular: canal habilitado (Art. 18 + Art. 20)
Peso: 15 pts

La LGPD reconoce **9 derechos** del titular (Art. 18). Todos ejercibles ante
el controlador con confirmación de atendimento en plazo razonable (la LGPD no
fija plazo exacto; la ANPD puede establecerlo por regulación):

1. **Confirmação** da existência de tratamento (18.I)
2. **Acesso** aos dados (18.II)
3. **Correção** de dados incompletos, inexatos ou desatualizados (18.III)
4. **Anonimização, bloqueio ou eliminação** de dados desnecessários, excessivos
   ou tratados em desconformidade com a LGPD (18.IV)
5. **Portabilidade** dos dados a outro fornecedor (18.V — conforme regulação da ANPD)
6. **Eliminação** dos dados pessoais tratados com consentimento (18.VI)
7. **Informação** sobre entidades com quem o controlador realizou uso compartilhado (18.VII)
8. **Informação** sobre possibilidade de não fornecer consentimento e consequências (18.VIII)
9. **Revogação do consentimento** a qualquer momento (18.IX)

Nota: La portabilidade (18.V) está sujeta a regulación de la ANPD — verificar
estado de implementación al usar esta skill.

Verificar:
- [ ] Existe mecanismo explícito para ejercer derechos (email, formulario, dirección)
- [ ] Se mencionan los **9 derechos** del Art. 18
- [ ] Se menciona el plazo de respuesta o referencia a regulación de la ANPD
- [ ] Se indica qué información debe adjuntar el titular al ejercer sus derechos
- [ ] Se menciona el derecho a reclamar ante la **ANPD** (gov.br/anpd)

**Decisiones automatizadas (Art. 20):**
El titular tiene derecho a solicitar revisión de decisiones tomadas exclusivamente
mediante tratamiento automatizado que afecten sus intereses:
- [ ] Si el sitio usa scoring, segmentação, aprovação automática: ¿la política lo declara?
- [ ] ¿Existe canal para solicitar revisão humana de la decisión?

### Bloque 7 — Dados sensíveis e crianças (Art. 11 + Art. 14)
Peso: 10 pts

**Dados sensíveis (Art. 5.II):**
La LGPD define como dados sensíveis los relativos a:
- Origem racial ou étnica
- Convicção religiosa
- Opinião política
- Filiação a sindicato ou organização de caráter religioso, filosófico ou político
- Dado referente à saúde ou à vida sexual
- Dado genético ou biométrico vinculado a pessoa natural

⚠️ La lista de dados sensíveis de la LGPD es más reducida que la del RGPD — no
incluye orientación sexual como categoría autónoma (está implícita en "vida sexual")
ni afiliación sindical por separado.

**Si el sitio no recoge dados sensíveis:** bloque N/A, asignar 10 pts.

**Si recoge dados sensíveis (Art. 11.I — bases válidas):**
- [ ] Identificados explícitamente como dados sensíveis en el aviso
- [ ] Base legal del Art. 11 declarada:
      - (I) Consentimento específico e destacado do titular
      - (II.a) Cumprimento de obrigação legal ou regulatória
      - (II.b) Tratamento compartilhado de dados para execução de políticas públicas
      - (II.c) Realização de estudos por órgão de pesquisa
      - (II.d) Exercício regular de direitos (inclusive em contrato)
      - (II.e) Proteção da vida ou incolumidade física
      - (II.f) Tutela da saúde por profissional ou entidade sanitária
      - (II.g) Garantia da prevenção à fraude e à segurança do titular (biométricos)
- [ ] El consentimento es específico y destacado del consentimento general
- [ ] Se indican medidas de seguridad reforzadas

**Crianças e adolescentes (Art. 14):**
- [ ] Si el sitio capta crianças (hasta 12 años): consentimento dos pais o responsável legal
- [ ] Si el sitio no va dirigido a menores: declararlo en el aviso
- [ ] No se usa a crianças como pretexto para captación de dados de los padres

**RIPD — Relatório de Impacto à Proteção de Dados Pessoais (Art. 38):**
Equivalente a la EIPD/DPIA del RGPD. La ANPD puede solicitar el RIPD.
Para tratamientos de alto riesgo (dados sensíveis a gran escala, scoring, biometría):
- [ ] ¿El aviso menciona la realización de RIPD para tratamientos de alto riesgo?

### Bloque 8 — Transferências internacionais (Art. 33–36)
Peso: 10 pts

La LGPD (Art. 33) permite transferencias internacionales de dados pessoais cuando:

1. **País com grau de proteção adequado** reconocido por la ANPD (Art. 33.I)
   — La ANPD no había publicado su lista de países con adecuación a la fecha de
   esta versión. Verificar el estado en gov.br/anpd antes de citar este mecanismo.
2. **Garantias suficientes** (Art. 33.II):
   - Cláusulas contratuais específicas para transferência internacional
   - Cláusulas padrão contratuais (modelo ANPD — verificar si publicado)
   - Normas corporativas globais (BCR equivalente)
   - Selos, certificados e códigos de conduta regulares — si existen en Brasil
3. **Cooperação jurídica internacional** (Art. 33.III) — para autoridades públicas
4. **Consentimento específico** del titular para la transferencia (Art. 33.VIII)
5. **Necessidade para execução de contrato** (Art. 33.V)
6. **Exercício regular de direitos** (Art. 33.VI)

Nota: la ANPD emitió normativa sobre transferencias internacionales en 2023-2024.
Verificar el estado de implementación actual en gov.br/anpd.

Verificar:
- [ ] El aviso declara si se realizan transferências internacionais
- [ ] Se identifican los países de destino (EE.UU., UE, otros)
- [ ] Se indica la base o garantía adoptada
- [ ] Si hay trackers de EE.UU. activos (Google, Meta, etc.): ¿el aviso lo declara?

### Bloque 9 — Segurança (Art. 46–49)
Peso: 5 pts

La LGPD exige medidas de seguridad técnicas y administrativas aptas para proteger
dados pessoais de accesos no autorizados, situaciones accidentales o ilícitas de
destrucción, pérdida, alteración, comunicación o difusión (Art. 46).

Verificar lo observable externamente:
- [ ] HTTPS activo en todas las páginas
- [ ] Certificado SSL/TLS válido y no expirado
- [ ] HSTS habilitado
- [ ] No hay redirección HTTP → HTTPS rota
- [ ] El aviso menciona medidas de segurança adoptadas

**Incidentes de segurança (Art. 48):**
Ante un incidente que pueda generar riesgo o daño a los titulares, el controlador
debe comunicarlo a la ANPD y a los titulares afectados en plazo razonable
(la ANPD ha reglamentado este plazo — verificar normativa vigente).
- [ ] El aviso menciona el procedimiento ante incidentes de segurança

### Bloque 10 — Encarregado de Dados (Art. 41)
Peso: 5 pts

⚠️ El Encarregado de Dados es **obligatorio para todos los controladores** bajo
la LGPD (Art. 41), independientemente del tamaño de la organización o del volumen
de datos tratados. Esta es una diferencia clave respecto al RGPD, donde el DPO
solo es obligatorio en los casos del Art. 37.1.

Excepción: la ANPD puede establecer requisitos diferenciados para pequenos
tratamentos (pequeños tratamientos). Verificar si la ANPD ha publicado resolución
al respecto.

Funciones del Encarregado (Art. 41.2):
- Aceitar reclamações e comunicações dos titulares
- Prestar esclarecimentos e adotar providências
- Receber comunicações da ANPD e adotar providências
- Orientar os funcionários do controlador sobre LGPD
- Executar demais atribuições determinadas pelo controlador o por normas complementares

Verificar:
- [ ] El aviso identifica al Encarregado de Dados
- [ ] Nombre o cargo del Encarregado publicado (Art. 41.1)
- [ ] Dirección de **email** del Encarregado publicada (obligatorio — es el canal principal)
- [ ] Si no existe Encarregado: issue crítico (obligatorio para todos los controladores)
- [ ] Si la ANPD ha publicado excepciones para pequenos tratamentos: verificar si aplica

---

## Paso 4 — Score global

```
Score = suma de puntos obtenidos / 100
```

| Rango | Interpretación |
|-------|---------------|
| 80–100 | Postura defensible — cumplimento sustancial |
| 60–79 | Risco moderado |
| 40–59 | Risco alto |
| 0–39 | Risco crítico |

---

## Paso 5 — Clasificação de issues e sanções (Art. 52)

La LGPD establece un sistema de sanciones administrativas (Art. 52):

| Sanción | Detalle |
|---------|---------|
| **Advertência** | Con indicación de plazo para medidas correctivas |
| **Multa simples** | Hasta 2% de la facturación de la persona jurídica en Brasil (excluidos impuestos), limitado a **R$ 50.000.000** por infracción |
| **Multa diária** | Hasta el mismo límite total |
| **Publicização** | Divulgación pública de la infracción |
| **Bloqueio dos dados** | Bloqueo de los datos hasta regularización |
| **Eliminação dos dados** | Eliminación de los datos personales |
| **Suspensão** | Suspensión parcial del banco de datos por hasta 6 meses |
| **Proibição** | Prohibición parcial o total de actividades de tratamiento |

La ANPD aplica la multa más alta calculada como 2% de facturación en Brasil o
R$ 50.000.000, lo que resulte más restrictivo para el infractor.

**Críticos** (bloquean cumplimento mínimo):
- Aviso de privacidade inexistente → Art. 9
- Sin Encarregado de Dados designado → Art. 41 (obligatorio para todos)
- Sin base legal para ninguna finalidade → Art. 7
- Cookies no esenciales sin consentimento previo → Art. 7.I
- Dados sensíveis sin consentimento específico → Art. 11.I
- Sin mecanismo de exercício de direitos → Art. 18
- Sin HTTPS → Art. 46
- Entidad extranjera sin representante en Brasil → Art. 3

**Medios** (plazo recomendado 30–60 días):
- Aviso existe pero falta base legal por finalidade → Art. 7
- Direitos mencionados sin canal ni plazo de atendimento → Art. 18
- Transferências internacionais no declaradas → Art. 33
- Banner de cookies solo informativo → Art. 7.I
- Marketing sin mecanismo de descadastramento → Art. 18
- RIPD probable pero no mencionado → Art. 38

**Bajos:**
- Data de atualização ausente en el aviso
- Aviso sin enlace desde formulários secundarios
- Prazos de retenção no especificados para algún tipo de dado

---

## Paso 6 — Output según modo

### Modo interno (Markdown)

```markdown
# Auditoria LGPD — [domínio]
Data: [data] | Setor: [setor] | Score: [X/100]

## Stack tecnológico
[usar resultados del Paso 0 compartido]

## Resumo
[postura geral, issues críticos, risco sancionatório estimado em BRL]

## Tabela de conformidade
| Bloco | Peso | Pts | Status | Evidência |
...

## Issues críticos / médios / baixos
...

## Notas metodológicas
- Verificado externamente
- Pendiente de acceso al backend
- Nota: lista de países com adequação da ANPD y normativa de transferências
  internacionales pueden estar en actualización — verificar em gov.br/anpd
```

Guardar en `<directorio-de-auditorias>/[cliente]/auditoria_lgpd_[fecha].md`.

### Modo cliente (`--docx`)

Misma estructura que `rgpd` modo `--docx`, adaptada a LGPD:
- Autoridad: ANPD
- Multas en BRL
- Terminología en portugués de Brasil
- Pie de página: "Desenvolvido por Zythos Media — Especialistas em SEO & IA Search"
  con hipervínculo a https://zythos.media

Guardar en `<directorio-de-auditorias>/[cliente]/auditoria_lgpd_[fecha].docx`.

---

## Notas de alcance

Mismas limitaciones que el skill `rgpd`: solo auditable externamente.
Adicional LGPD: el Relatório de Impacto (RIPD) es un documento interno.

## Atualização normativa

- **LGPD** (Lei 13.709/2018): en vigor septiembre 2020; sanciones desde agosto 2021.
- **ANPD**: en proceso de maduración regulatoria. Resoluciones relevantes disponibles en gov.br/anpd.
- **Transferências internacionais**: normativa de la ANPD en evolución a la fecha de esta versión.
  Verificar el estado antes de usar el Bloque 8.
- **Lista de países com adequação**: pendiente de publicación por la ANPD a la fecha de esta versión.
- **Pequeños tratamientos**: posibles excepciones al Encarregado obligatorio — verificar en ANPD.
- **Versão desta skill:** 1.0.0 (2026-07-08).
