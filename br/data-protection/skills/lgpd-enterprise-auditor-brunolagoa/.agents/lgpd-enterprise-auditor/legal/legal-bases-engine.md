# Bases legais do tratamento (arts. 7º e 11, LGPD)

## Objetivo
Definir validação de base legal por operação de tratamento, distinguindo dados pessoais (art. 7º) de dados pessoais sensíveis (art. 11).

## Bases legais para dados pessoais (art. 7º, LGPD)
- consentimento (art. 7º, I);
- obrigação legal/regulatória (art. 7º, II);
- execução de políticas públicas pela administração pública (art. 7º, III);
- estudos por órgão de pesquisa, com anonimização sempre que possível (art. 7º, IV);
- execução de contrato ou de procedimentos preliminares a contrato (art. 7º, V);
- exercício regular de direitos em processo judicial, administrativo ou arbitral (art. 7º, VI);
- proteção da vida ou incolumidade física do titular ou de terceiro (art. 7º, VII);
- tutela da saúde, em procedimento realizado por profissionais/serviços de saúde (art. 7º, VIII);
- legítimo interesse do controlador ou de terceiro (art. 7º, IX);
- proteção do crédito (art. 7º, X).

## Bases legais para dados sensíveis (art. 11, LGPD)
Dados sensíveis (art. 5º, II: dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural) possuem rol **próprio e mais restrito**:
- consentimento específico e destacado, para finalidades específicas (art. 11, I);
- sem consentimento, apenas nas hipóteses do art. 11, II: obrigação legal/regulatória; políticas públicas; estudos por órgão de pesquisa (anonimizando quando possível); exercício regular de direitos; proteção da vida/incolumidade física; tutela da saúde por profissionais de saúde; garantia da prevenção à fraude e à segurança do titular.

As regras de dado sensível valem também para o dado que **revele** informação sensível e possa causar dano ao titular (art. 11, §1º) — ex.: o registro de que alguém agendou consulta numa clínica, ou a visita à página de agendamento dela. A extensão vale em todo o framework (`core/scoring-engine.md`, "Catálogo de itens").

### Regra crítica de dados sensíveis
- **Legítimo interesse (art. 7º, IX) NÃO é base legal válida para dados sensíveis.** Seu uso para tratar dado sensível deve ser classificado como `NAO_CONFORME` com severidade `CRITICO`.
- "Proteção ao crédito" e "execução de contrato" também não constam do rol do art. 11; tratar dado sensível com essas bases é não conformidade.

## Regras de auditoria
- toda finalidade deve mapear para ao menos uma base legal do artigo aplicável (7º ou 11);
- antes de validar a base, classificar se a operação envolve dado pessoal comum ou sensível;
- base legal deve ser comprovável por evidência técnica e/ou documental;
- consentimento (art. 7º) deve ser específico, granular e revogável; consentimento para dado sensível (art. 11, I) deve ser, ainda, específico e destacado;
- uso de legítimo interesse deve ter justificativa formal documentada e teste de proporcionalidade/balanceamento (LIA).

## Checklist atômico
Itens do catálogo (regras em `core/scoring-engine.md`, "Catálogo de itens"): avaliar todos, cada um com sua `applicability`.

### Bases legais
Para o teste de balanceamento de `BL-03`, usar [[lia-template]].

Como ler estes itens sem contar a mesma falha duas vezes:
- `BL-02` avalia os tratamentos em que o auditado é controlador por decisão própria (contas, cobrança, uso do produto). O uso, para finalidade própria, de dados recebidos como operador é contado só em `OP-02`; `BL-02` o cita e pontua pelo que resta.
- `BL-01` avalia base **indicada** que não serve para dado sensível. Sem dado sensível nos tratamentos próprios, fica `NAO_APLICAVEL`.
- `BL-03` só se aplica quando o legítimo interesse é a base indicada.
- `BL-04` avalia os dados que o auditado decide coletar. Nos fluxos em que ele é só operador, a escolha dos campos é do controlador: o item é avaliado pelos tratamentos próprios, e o excesso percebido no fluxo do controlador vai para as recomendações.

Dependências (contagem única de `core/scoring-engine.md`): com o segundo item `NAO_CONFORME`, o primeiro fica `NAO_APLICAVEL`.
- `BL-01` depende de `BL-02`: não há base incompatível a apontar sem nenhuma base indicada.

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `BL-01` | O dado sensível é tratado só com hipótese do art. 11, sem legítimo interesse, execução de contrato ou proteção do crédito como base? | BL | `CRITICO` | — | `DOCUMENTAL` | art. 11 |
| `BL-02` | Cada finalidade de tratamento está ligada a uma base legal do artigo aplicável (7º ou 11), comprovável por evidência técnica ou documental? | BL | `ALTO` | `CRITICO` se faltar base para dado sensível ou de crianças e adolescentes | `DOCUMENTAL` | arts. 7º e 11 |
| `BL-03` | O uso de legítimo interesse tem justificativa formal e teste de balanceamento (LIA) documentados? | BL | `MEDIO` | — | `DOCUMENTAL` | arts. 7º, IX e 10 |
| `BL-04` | Os dados coletados em cada formulário, cadastro ou integração se limitam ao necessário para a finalidade, sem campo obrigatório que ela não exija? | BL | `MEDIO` | `ALTO` se o excesso for de dado sensível ou de crianças e adolescentes | `TECNICO` | art. 6º, III |

## Papel do auditado: controlador ou operador
Antes de exigir base legal, identificar o papel do auditado **em cada fluxo de dados** (art. 5º, VI e VII):
- **Controlador**: decide sobre o tratamento. Responde por base legal, transparência, direitos do titular e comunicação de incidentes.
- **Operador**: trata dados em nome do controlador e segundo as instruções dele (art. 39). Um SaaS B2B costuma ser operador dos dados que seus clientes inserem (ex.: pacientes de uma clínica) e controlador dos dados das contas, de cobrança e de uso do próprio produto.
- Quem usa os dados recebidos para **finalidade própria** (ex.: analytics de produto, treino de modelo, marketing) passa a ser controlador dessa finalidade e precisa de base legal própria.

Quando o auditado é operador de um fluxo, **não** são achado dele, e ficam `NAO_APLICAVEL` com essa justificativa: a escolha da base legal, a coleta de consentimento, a política de privacidade dirigida aos titulares, o canal de direitos, o relatório de impacto (art. 38) e a comunicação de incidente à ANPD e aos titulares (art. 48) — obrigações do controlador. Agente com papel misto segue as regras do controlador nos fluxos em que é controlador (inclusive encarregado e RIPD) e as do operador nos demais. Continuam exigíveis do operador os itens abaixo, aplicáveis quando o auditado é operador em algum fluxo (sem fluxo de operador, ficam `NAO_APLICAVEL`):

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `OP-01` | Há contrato ou termo com o controlador que defina objeto, instruções, segurança, suboperadores e devolução ou eliminação dos dados ao fim? | 14 | `ALTO` | — | `DOCUMENTAL` | art. 39 |
| `OP-02` | O tratamento se limita às instruções documentadas do controlador, sem uso dos dados para finalidade própria? | BL | `ALTO` | `CRITICO` com dado sensível ou de crianças e adolescentes | `TECNICO` | arts. 7º, 11 e 39 |
| `OP-03` | Os suboperadores (hospedagem, e-mail, analytics) são informados ao controlador? | 14 | `MEDIO` | `ALTO` com dado sensível ou de crianças e adolescentes | `DOCUMENTAL` | art. 39 |
| `OP-04` | Existe processo para avisar o controlador sem demora em caso de incidente? | 14 | `ALTO` | — | `DOCUMENTAL` | arts. 39 e 48 |
| `OP-05` | Existe processo para apoiar o controlador no atendimento a pedidos de titulares? | 14 | `MEDIO` | — | `TECNICO` | arts. 18 e 39 |
| `OP-06` | Ao fim do contrato, os dados são devolvidos ou eliminados conforme instrução do controlador? | 14 | `MEDIO` | — | `TECNICO` | arts. 16 e 39 |

A segurança (art. 46) e o registro das operações (art. 37) do operador são avaliados nos itens de segurança e em `GV-01`; o contrato com suboperadores, em `GV-09` (DPA com operadores, `governance/dpo-framework.md`). Não há item próprio para eles aqui.

A indicação de encarregado pelo operador é facultativa (Res. CD/ANPD nº 18/2024). O operador responde solidariamente quando descumpre a LGPD ou as instruções lícitas do controlador (art. 42, §1º, I).

Severidade (já refletida na tabela): operador que usa os dados para finalidade própria sem base legal: `ALTO` (`CRITICO` com dado sensível ou de crianças e adolescentes). Ausência de contrato com o controlador ou de processo de aviso de incidente: `ALTO`. Suboperador não informado ou sem contrato: `MEDIO` (`ALTO` com dado sensível ou de crianças e adolescentes). Sem processo de apoio ao controlador nos pedidos de titulares, ou sem devolução ou eliminação definida para o fim do contrato: `MEDIO`. Conta como dado sensível também o dado que **revele** informação sensível (art. 11, §1º), como em todo o framework. Área de score: `governanca` (domínio 14); o uso para finalidade própria pontua em `bases_legais`.

## Dados de acesso público e dados manifestamente públicos (art. 7º, §§ 3º, 4º e 7º)
Dado público não é dado livre: estar acessível muda a análise, mas não afasta a LGPD.
- **Dados de acesso público** (ex.: diários oficiais, portais de transparência, dados abertos de órgãos como o TSE): o tratamento deve considerar a finalidade, a boa-fé e o interesse público que justificaram sua disponibilização (art. 7º, §3º).
- **Dados tornados manifestamente públicos pelo próprio titular**: dispensa-se apenas o **consentimento**, resguardados os direitos do titular e os princípios do art. 6º (art. 7º, §4º). Documentar qual base legal sustenta o tratamento (com frequência o legítimo interesse, com teste de balanceamento).
- **Tratamento posterior para novas finalidades** é possível se houver propósito legítimo e específico e se forem preservados os direitos do titular, os fundamentos e os princípios (art. 7º, §7º).
- **Dado sensível de acesso público** (ex.: filiação partidária ou dados de candidatos divulgados pelo TSE): não presumir dispensa. Enquadrar em uma hipótese do art. 11 e demonstrar compatibilidade com a finalidade da divulgação oficial (art. 7º, §3º); reutilização alinhada a essa finalidade, como transparência e controle social, com minimização, tende a ser legítima. Perfilamento ou combinação com outras bases para fins diversos exige avaliação de risco (RIPD).

Itens, aplicáveis quando o auditado trata dados obtidos de fonte pública (sem esse uso, ficam `NAO_APLICAVEL`):

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `DP-01` | A origem pública de cada conjunto de dados está identificada (fonte, data de coleta, finalidade original da divulgação)? | BL | `MEDIO` | — | `DOCUMENTAL` | art. 7º, §3º |
| `DP-02` | A finalidade do tratamento é compatível com a que justificou a divulgação, ou a nova finalidade é legítima e específica, com análise documentada? | BL | `MEDIO` | `ALTO` se o uso for incompatível com a finalidade da divulgação; `CRITICO` com perfilamento discriminatório ou exposição indevida de dado sensível | `DOCUMENTAL` | art. 7º, §§ 3º e 7º |
| `DP-03` | Há base legal documentada para o dado público (a dispensa do §4º é só do consentimento) e, para dado sensível, enquadramento no art. 11? | BL | `ALTO` | `CRITICO` com perfilamento discriminatório ou exposição indevida de dado sensível | `DOCUMENTAL` | arts. 7º, §4º e 11 |
| `DP-04` | Os dados públicos são minimizados e os direitos do titular (correção, oposição, eliminação quando cabível) seguem atendidos? | BL | `MEDIO` | — | `TECNICO` | arts. 6º, III e 7º, §4º |

Severidade: reutilização compatível e minimizada **não é achado por si só**. Ausência de análise documentada da compatibilidade: `MEDIO`. Uso incompatível com a finalidade da divulgação ou sem base legal: `ALTO`. `CRITICO` apenas com perfilamento discriminatório ou exposição indevida de dado sensível.

## Consentimento (art. 8º)
A aplicabilidade decorre dos fatos, não do que foi documentado. Os itens `CS` são `APLICAVEL` quando ocorre ao menos uma destas situações, fora de cookies e tracking:
- o auditado indica o consentimento (art. 7º, I ou art. 11, I) como base legal de algum tratamento;
- o sistema coleta consentimento na prática (caixa de aceite, termo, opt-in de comunicação), ainda que nenhum documento nomeie a base;
- o tratamento só pode se apoiar em consentimento: dado sensível sem hipótese do art. 11, II; dado de criança (art. 14, §1º); comunicação de marketing a quem não é cliente.

Fora dessas situações, os itens ficam `NAO_APLICAVEL`, com a evidência de que o sistema não coleta consentimento; a falta de base legal documentada é contada em `BL-02`, e não tira os itens `CS` da conta por si só. O consentimento exigido por cookie ou rastreador no front-end é avaliado só nos itens `CK` de [[owasp-api]], inclusive quando o dado rastreado revela informação sensível: `CS-08` não se aplica a ele.

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `CS-01` | O consentimento é fornecido por escrito ou por outro meio que demonstre a manifestação de vontade (opt-in explícito, sem checkbox pré-marcado)? | 2 | `ALTO` | — | `TECNICO` | art. 8º, caput |
| `CS-02` | Em contrato escrito, o consentimento consta de cláusula destacada das demais? | 2 | `MEDIO` | — | `DOCUMENTAL` | art. 8º, §1º |
| `CS-03` | Há registro que permita ao controlador provar a obtenção regular do consentimento? | 2 | `MEDIO` | — | `TECNICO` | art. 8º, §2º |
| `CS-04` | O consentimento se refere a finalidades determinadas, sem autorizações genéricas? | 2 | `ALTO` | `MEDIO` se as finalidades estiverem determinadas, mas agrupadas num único aceite (pouco granular) | `TECNICO` | art. 8º, §4º |
| `CS-05` | A revogação é possível a qualquer momento, por procedimento gratuito e facilitado? | 2 | `ALTO` | — | `TECNICO` | arts. 8º, §5º e 18, IX |
| `CS-06` | Alterações de finalidade, forma, duração ou compartilhamento são informadas com destaque, permitindo revogar? | 2 | `MEDIO` | — | `DOCUMENTAL` | arts. 8º, §6º e 9º, §2º |
| `CS-07` | Quando o tratamento é condição para o serviço, o titular é informado com destaque sobre isso e sobre como exercer seus direitos? | 2 | `MEDIO` | — | `DOCUMENTAL` | art. 9º, §3º |
| `CS-08` | O consentimento para dado sensível é específico e destacado, para finalidades específicas? | 2 | `ALTO` | — | `TECNICO` | art. 11, I |

## Mapeamento para severidade e score
- Legítimo interesse ou outra base do art. 7º aplicada a dado sensível: `CRITICO`.
- Consentimento genérico ou com checkbox pré-marcado: `ALTO`.
- Ausência de mecanismo de revogação do consentimento: `ALTO`.
- Ausência de registro que prove o consentimento ou consentimento pouco granular: `MEDIO`.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `bases_legais` (domínios `BL` e 2); os itens `OP`, salvo `OP-02`, pontuam em `governanca` (domínio 14). A criticidade de cada item está nas tabelas acima.

## Resultado da validação
- `CONFORME`: base legal válida para o tipo de dado + evidência suficiente.
- `PARCIAL`: base legal indicada, mas sem comprovação robusta.
- `NAO_CONFORME`: nenhuma base legal indicada, base incompatível com a finalidade, ou base do art. 7º aplicada indevidamente a dado sensível.
