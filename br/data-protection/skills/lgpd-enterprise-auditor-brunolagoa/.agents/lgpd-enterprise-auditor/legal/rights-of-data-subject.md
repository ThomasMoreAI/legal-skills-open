# Direitos do titular e transparência (arts. 9º, 18 e 19, LGPD)

## Objetivo
Padronizar avaliação dos direitos do titular (arts. 17 a 22 da LGPD) e da transparência devida a ele (art. 9º).

## Quando o auditado é operador
Os direitos do titular e a transparência são obrigações do **controlador**. Se o auditado for só operador do fluxo, os itens deste módulo ficam `NAO_APLICAVEL` para aquele fluxo; avalia-se apenas se ele tem processo para apoiar o controlador no atendimento (`legal/legal-bases-engine.md`, seção "Papel do auditado").

## Direitos mínimos a validar (art. 18)
- confirmação da existência de tratamento (I);
- acesso aos dados (II);
- correção de dados incompletos, inexatos ou desatualizados (III);
- anonimização, bloqueio ou eliminação de dados desnecessários, excessivos ou tratados em desconformidade (IV);
- portabilidade (V);
- eliminação dos dados tratados com consentimento (VI);
- informação sobre entidades públicas e privadas com as quais houve uso compartilhado (VII);
- informação sobre a possibilidade de não fornecer consentimento e as consequências da negativa (VIII);
- revogação do consentimento, nos termos do art. 8º, §5º (IX);
- oposição a tratamento fundado em hipótese de dispensa de consentimento, em caso de descumprimento da Lei (§2º);
- revisão de decisões tomadas unicamente com base em tratamento automatizado (art. 20) — ver [[llm-audit]].

## Prazos e forma de atendimento
- Requerimento expresso do titular ou de representante legalmente constituído, atendido **sem custos** (art. 18, §§3º e 5º).
- Confirmação de existência ou acesso (art. 19): **imediatamente**, em formato simplificado; ou por declaração clara e completa (origem dos dados, inexistência de registro, critérios e finalidade) em até **15 dias** contados do requerimento.
- Se não for possível adotar a providência de imediato, responder indicando as razões de fato ou de direito, ou o agente de tratamento efetivo quando o destinatário não o for (art. 18, §4º).
- Comunicar de imediato correção, eliminação, anonimização ou bloqueio aos agentes com quem os dados foram compartilhados (art. 18, §6º).

## Transparência e política de privacidade (art. 9º)
O titular tem direito ao acesso facilitado às informações sobre o tratamento, disponibilizadas de forma clara, adequada e ostensiva. Validar na política de privacidade (ver [[privacy-policy-template]]):
- finalidade específica do tratamento (I);
- forma e duração do tratamento (II);
- identificação e contato do controlador (III e IV);
- uso compartilhado e sua finalidade (V);
- responsabilidades dos agentes que realizarão o tratamento (VI);
- direitos do titular, com menção explícita aos do art. 18 (VII);
- base legal por finalidade e política de retenção;
- identidade e contato do encarregado (art. 41, §1º);
- cookies e transferência internacional, quando houver;
- linguagem acessível e indicação de versão/data de atualização.

Quando o consentimento é requerido, ele é nulo se as informações tiverem conteúdo enganoso ou abusivo ou não tiverem sido apresentadas previamente com transparência (art. 9º, §1º).

## Checklist atômico
Itens do catálogo (regras em `core/scoring-engine.md`, "Catálogo de itens"): avaliar todos, cada um com sua `applicability`. A revogação do consentimento é avaliada em `CS-05` (`legal/legal-bases-engine.md`) e, para cookies, em `CK-03`; `DT-08` só se aplica quando há decisão automatizada que afete o titular: a que define perfil ou decide acesso, preço, crédito ou atendimento por pontuação ou modelo. Regra fixa de validação (campo obrigatório, bloqueio por idade) não é decisão automatizada do art. 20.

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `DT-01` | Existe canal de atendimento claro e funcional para o exercício dos direitos do art. 18? | 3 | `ALTO` | — | `DOCUMENTAL` | art. 18 |
| `DT-02` | Há fluxo que responda aos pedidos sem custos e no prazo do art. 19 (confirmação ou acesso imediato em formato simplificado, ou declaração completa em até 15 dias)? | 3 | `MEDIO` | — | `DOCUMENTAL` | arts. 18, §§3º a 5º, e 19 |
| `DT-03` | Há política ou aviso de privacidade publicado, de acesso fácil e ostensivo? | 4 | `ALTO` | — | `DOCUMENTAL` | art. 9º |
| `DT-04` | A política traz o conteúdo do art. 9º (finalidade específica, forma e duração, controlador e contato, uso compartilhado, responsabilidades dos agentes e direitos do art. 18), além da base legal por finalidade e da retenção? | 4 | `MEDIO` | — | `DOCUMENTAL` | art. 9º, I a VII |
| `DT-05` | A política usa linguagem clara e acessível e indica versão e data de atualização? | 4 | `BAIXO` | — | `DOCUMENTAL` | arts. 6º, VI e 9º |
| `DT-06` | Há processo operacional para correção, anonimização, bloqueio, eliminação e portabilidade dos dados? | 3 | `MEDIO` | — | `TECNICO` | art. 18, III a VI |
| `DT-07` | O titular consegue saber com quem os dados foram compartilhados e, quando o consentimento é a base, que pode negá-lo e com que consequências? | 3 | `MEDIO` | — | `DOCUMENTAL` | art. 18, VII e VIII |
| `DT-08` | Há meio de pedir a revisão de decisões tomadas unicamente por tratamento automatizado, com informação sobre os critérios usados? | 3 | `MEDIO` | — | `TECNICO` | art. 20 |
| `DT-09` | Correções, eliminações, anonimizações e bloqueios são comunicados aos agentes com quem os dados foram compartilhados? | 3 | `MEDIO` | — | `TECNICO` | art. 18, §6º |
| `DT-10` | Há trilha auditável dos pedidos (data, tipo, resposta e confirmação da execução)? | 3 | `MEDIO` | — | `DOCUMENTAL` | arts. 6º, X e 18 |

Dependências (contagem única de `core/scoring-engine.md`): com o segundo item `NAO_CONFORME`, o primeiro fica `NAO_APLICAVEL`.
- `DT-09` depende de `DT-06`: não há correção ou eliminação a comunicar sem processo que as execute.

## Critérios de conformidade
- canal de atendimento claro e funcional;
- prazo de resposta definido e compatível com o art. 19;
- trilha de atendimento auditável;
- confirmação de execução da solicitação.

## Não conformidade comum
- ausência de canal de solicitação;
- falta de processo para exclusão/portabilidade;
- revogação de consentimento não operacional;
- política de privacidade genérica, sem finalidade e base legal por operação.

## Mapeamento para severidade e score
- Ausência de canal para exercício de direitos: `ALTO`.
- Revogação de consentimento não operacional: `ALTO`.
- Ausência de política de privacidade: `ALTO`.
- Resposta fora do prazo do art. 19 ou inexistência de fluxo de exclusão/portabilidade: `MEDIO`.
- Política de privacidade incompleta frente ao art. 9º: `MEDIO`.
- Problemas de clareza ou linguagem da política: `BAIXO`.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `direitos_titular` (domínios 3 e 4) para todos os itens deste módulo. A criticidade de cada item está na tabela acima.
