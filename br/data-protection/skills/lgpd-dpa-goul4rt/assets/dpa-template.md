# Template de DPA — Acordo de Tratamento de Dados Pessoais (Art. 39 LGPD)

> ⚠️ **Não é peça jurídica pronta.** Este é um esqueleto para acelerar a redação e a revisão. Antes de assinar, submeta a revisão jurídica. Substitua todos os campos `{...}`. As 12 cláusulas seguem a ordem do `SKILL.md`.

---

**ACORDO DE TRATAMENTO DE DADOS PESSOAIS**

Anexo ao Contrato Principal nº `{NUMERO_CONTRATO}`, celebrado entre:

- **CONTROLADOR**: `{RAZAO_SOCIAL_CONTROLADOR}`, CNPJ `{CNPJ}`, doravante "Controlador"; e
- **OPERADOR**: `{RAZAO_SOCIAL_OPERADOR}`, `{CNPJ_OU_REGISTRO_ESTRANGEIRO}`, doravante "Operador".

Regido pela Lei nº 13.709/2018 (LGPD) e resoluções da ANPD aplicáveis.

---

## Cláusula 1 — Identificação das partes e papéis
O Controlador define as finalidades e os meios essenciais do tratamento. O Operador realiza o tratamento **em nome e conforme instruções** do Controlador. Cada parte é responsável pelo cumprimento das obrigações que a LGPD lhe atribui em razão de seu papel.

## Cláusula 2 — Objeto e finalidade
O Operador tratará dados pessoais exclusivamente para: `{DESCREVER FINALIDADE — ex.: hospedagem em nuvem, envio transacional de e-mail}`.
- **Categorias de titulares**: `{ex.: clientes, usuários finais}`
- **Categorias de dados**: `{ex.: nome, e-mail, IP, dados de pagamento}`
- **Dados sensíveis (Art. 11)?** `{sim/não — se sim, detalhar e justificar}`
- **Duração**: enquanto vigente o Contrato Principal.

## Cláusula 3 — Instruções do Controlador (Art. 39)
O Operador tratará os dados **somente** mediante instruções documentadas do Controlador, inclusive quanto a transferências internacionais. Caso seja obrigado por lei a tratar fora das instruções, informará o Controlador previamente, salvo proibição legal. O Operador comunicará imediatamente se, em sua opinião, uma instrução violar a LGPD.

## Cláusula 4 — Confidencialidade
O Operador garante que todas as pessoas autorizadas a tratar os dados estejam sob obrigação de confidencialidade (contratual ou legal), limitando o acesso ao estritamente necessário (need-to-know).

## Cláusula 5 — Medidas de segurança (Art. 46)
O Operador adotará medidas técnicas e administrativas aptas a proteger os dados, incluindo, no mínimo: `{criptografia em trânsito (TLS) e em repouso, controle de acesso, segregação de ambientes, registro de logs, backup, gestão de vulnerabilidades}`. As medidas detalhadas constam do **Anexo I**.

## Cláusula 6 — Sub-operadores
O Operador não contratará sub-operadores sem **autorização prévia** (específica ou geral com direito de objeção) do Controlador. O sub-operador ficará sujeito às mesmas obrigações deste Acordo, permanecendo o Operador **responsável solidário** perante o Controlador. Lista de sub-operadores autorizados no **Anexo II**.

## Cláusula 7 — Auxílio aos direitos do titular (Art. 18)
O Operador auxiliará o Controlador a atender requisições de titulares (acesso, correção, eliminação, portabilidade, etc.) dentro do **SLA do Controlador**, repassando qualquer requisição que receba diretamente em até `{ex.: 2 dias úteis}`, sem respondê-la por conta própria.

## Cláusula 8 — Incidentes de segurança (Art. 48 + Res. CD/ANPD nº 15/2024)
O Operador notificará o Controlador sobre qualquer incidente que possa acarretar risco aos titulares **imediatamente e em no máximo `{recomendado: 24 horas}`** da ciência, fornecendo as informações necessárias para que o Controlador cumpra o prazo de **3 dias úteis** de comunicação à ANPD. O Operador colaborará na investigação e mitigação.

## Cláusula 9 — Devolução e eliminação ao término
Encerrado o tratamento ou o Contrato Principal, o Operador, conforme escolha do Controlador, devolverá ou eliminará os dados e cópias em até `{ex.: 30 dias}`, fornecendo **atestado de eliminação**, salvo retenção exigida por lei (Art. 16).

## Cláusula 10 — Auditoria e demonstração de conformidade
O Operador disponibilizará informações necessárias para demonstrar conformidade e permitirá auditorias/inspeções pelo Controlador ou auditor por ele indicado, com `{ex.: 15 dias}` de aviso prévio. Relatórios de certificação independente (SOC 2, ISO 27001/27701) podem ser aceitos como evidência.

## Cláusula 11 — Responsabilidade (Art. 42)
As partes respondem nos termos dos Arts. 42 a 45 da LGPD. `{Definir limites de responsabilidade e ressarcimento entre as partes, sem prejuízo dos direitos dos titulares.}`

## Cláusula 12 — Transferência internacional (Arts. 33–36 + Res. CD/ANPD nº 19/2024)
Havendo tratamento fora do Brasil, aplica-se: `{base do Art. 33 — ex.: Cláusulas-Padrão Contratuais da Res. 19/2024}`. Países de destino: `{listar}`. As Cláusulas-Padrão aplicáveis integram o **Anexo III**.

---

## Anexo I — Medidas técnicas e administrativas
`{Listar: criptografia, MFA, RBAC, segregação, logging imutável, retenção de logs, plano de continuidade, testes de segurança, treinamento.}`

## Anexo II — Sub-operadores autorizados
| Sub-operador | Finalidade | País | Salvaguarda |
|---|---|---|---|
| `{nome}` | `{ex.: CDN}` | `{país}` | `{DPA/SCC}` |

## Anexo III — Transferência internacional
`{Anexar Cláusulas-Padrão Contratuais (Res. 19/2024) ou outra base do Art. 33.}`

---

**Assinaturas**

Controlador: ______________________  Data: ___/___/______
Operador:    ______________________  Data: ___/___/______
