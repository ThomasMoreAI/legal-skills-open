CONFIDENCIAL — uso interno

> **Exemplo público com dados fictícios.** Este relatório foi produzido sobre o projeto fictício e intencionalmente falho de `examples/saas-demo/` para demonstrar o LGPD Enterprise Auditor. Empresa, pessoas, CNPJ, domínios e dados são inventados. Relatórios reais são confidenciais e não devem ser versionados em repositório público; este arquivo foge da regra só por ser um exemplo público.

# Relatório de auditoria LGPD — AgendaFácil

| Campo | Valor |
|---|---|
| Projeto auditado | `examples/saas-demo/` — AgendaFácil (fictício) |
| Data da análise | 2026-10-03 |
| Comando | `/lgpd-saas` |
| Cenário | `saas_web` (escopo direcionado) |
| Framework | LGPD Enterprise Auditor 1.8.1, base canônica `.agents/lgpd-enterprise-auditor/` |
| Método | leitura estática dos arquivos do repositório; sem acesso ao ambiente de produção, aos painéis da Vercel, do banco e do GitHub, nem a contratos fora do repositório |

## Contexto e escopo

### O que foi inferido dos arquivos do projeto

Antes de qualquer pergunta, foram lidos `README.md`, `docs/`, `package.json`, `vercel.json`, `.env.example`, `.github/workflows/ci.yml`, `db/schema.sql` e o código de `api/`, `src/` e `public/`.

| Entrada do roteador | Contexto inferido | Fonte |
|---|---|---|
| Natureza do agente | Pessoa jurídica com fins econômicos; microempresa do Simples Nacional, 3 sócios | `README.md:13-14` |
| Papel em cada fluxo | Operadora dos dados dos pacientes; controladora das contas das clínicas e do rastreamento que ela mesma instalou (detalhe abaixo) | `README.md:9` e `:16`, `db/schema.sql:11-39`, `public/index.html:7-15` |
| Stack | Node.js 20 + Express 5, JWT; front-end estático | `README.md:20-21`, `package.json:15-22` |
| Hospedagem e banco | Vercel (funções em `gru1`, CDN para estáticos); Postgres gerenciado em `sa-east-1` | `vercel.json:3-4`, `.env.example:5-6`, `README.md:22-23` |
| Integrações | Meta Pixel na página pública de agendamento, para campanhas da própria AgendaFácil | `public/index.html:7-15`, `README.md:24` |
| IA/LLM | Nenhuma: sem SDK de IA nas dependências e nenhum fluxo de IA declarado | `package.json:15-25`, `README.md:18-25` |
| DevSecOps | GitHub Actions com lint, testes e deploy; sem varreduras de segurança | `.github/workflows/ci.yml` |
| Faixa etária do público | Serviço B2B para clínicas que atendem só adultos; o agendamento bloqueia menores de 18 anos pela data de nascimento informada | `README.md:15`, `src/routes/agendamentos.js:23-27` |
| Dados tratados | Nome, CPF, telefone, e-mail, data de nascimento e motivo da consulta (texto livre) dos pacientes; e-mail e hash de senha dos usuários das clínicas | `db/schema.sql:11-39`, `README.md:29` |

Confirmações pedidas ao fim do levantamento (respostas simuladas para este exemplo). A fundadora:

- confirmou o porte, a ausência de IA e que o Meta Pixel foi instalado por decisão da AgendaFácil, para suas próprias campanhas;
- informou que `docs/lgpd/` reúne toda a documentação de privacidade que a empresa tem;
- informou que não há contrato de proteção de dados assinado com clínicas nem com provedores, e que os termos padrão aceitos no cadastro da Vercel, do banco e da Meta não foram reunidos para análise.

### Natureza e papel do agente de tratamento

- **Pessoa jurídica com fins econômicos**, portanto sujeita à LGPD (a exclusão do art. 4º, I, não se aplica).
- **Agente de tratamento de pequeno porte** (microempresa, Res. CD/ANPD nº 2/2022).
- **Há tratamento de alto risco.** O motivo da consulta (`db/schema.sql:37`, `public/index.html:35`) é **dado pessoal sensível referente à saúde** (art. 5º, II). Pelos critérios da Res. CD/ANPD nº 2/2022 (art. 4º), o uso de dados sensíveis é um critério específico de alto risco. O critério geral também está presente, pelo impacto significativo (`core/severity-model.md`): o dado de saúde é parte da atividade-fim do serviço, e o CPF guardado junto com os contatos permite fraude se exposto. A larga escala não foi presumida nem é necessária para a conclusão.

**Papel em cada fluxo de dados** (`legal/legal-bases-engine.md`, seção "Papel do auditado"):

| Fluxo | Papel da AgendaFácil | Consequência na auditoria |
|---|---|---|
| Dados dos pacientes inseridos no agendamento (nome, CPF, contato, data de nascimento, motivo da consulta) | **Operadora**. As clínicas são as controladoras | Base legal, consentimento, política dirigida aos pacientes e canal de direitos são obrigações das clínicas e ficam `NAO_APLICAVEL`. Valem os itens de operador (OP-01 a OP-06), a segurança própria e o registro das operações. Os itens `CS`, `CA` e `DP` ficam `NAO_APLICAVEL` |
| Rastreamento da página de agendamento pelo Meta Pixel, instalado pela AgendaFácil para suas campanhas | **Controladora** dessa finalidade própria | Precisa de base legal própria; os itens de cookies, transparência, direitos e transferência internacional ficam `APLICAVEL` |
| Contas dos usuários das clínicas (e-mail e senha) e, quando existirem, cobrança e dados de uso do produto | **Controladora** | Base legal, transparência, direitos, retenção e incidentes são obrigações da AgendaFácil. O repositório não tem código de cobrança |

Hoje nenhum documento registra essa divisão (ver OP-01).

**Consequências do porte e do alto risco:**

1. **Nenhuma severidade foi modulada.** O `core/severity-model.md` só permite reduzir a severidade em um nível quando as três condições são verdadeiras ao mesmo tempo: pequeno porte, **ausência** de tratamento de alto risco e ausência de exposição explorável confirmada. A segunda condição falha, então todas as severidades e `criticality` deste relatório são as originais.
2. **As dispensas do pequeno porte não se aplicam.** O tratamento de alto risco está entre as exclusões da Res. CD/ANPD nº 2/2022 (art. 3º). A indicação de encarregado é facultativa para o operador, mas a AgendaFácil também é controladora (contas e rastreamento) e, sem a dispensa, precisa indicá-lo. O registro das operações deve ser o completo, não o simplificado (`governance/dpo-framework.md`). Recomenda-se confirmar o enquadramento com a assessoria jurídica.

### Módulos ativados (saída do roteador)

| Módulo | Ativado | Justificativa |
|---|---|---|
| `core` | sim | obrigatório em todo cenário |
| `legal` | sim | obrigatório em todo cenário; inclui bases legais, papel do auditado, direitos do titular e transferência internacional |
| `governance` | sim | cenário `saas_web` |
| `appsec` | sim | cenário `saas_web`; há API pública (`/api/agendamentos`) |
| `cloud` | sim | cenário `saas_web`; hospedagem em PaaS e banco gerenciado |
| `devsecops` | sim | cenário `saas_web`; CI/CD ativo |

**Escopo excluído explicitamente:**

- `eca-digital`: módulo não ativado. O único controle etário é a data de nascimento **autodeclarada** (`src/routes/agendamentos.js:23-27`). Pelo `orchestrator/router.md`, a autodeclaração não afasta o gatilho quando existe qualquer outro indício da lista. Aqui não existe nenhum: o serviço é B2B, contratado por clínicas que atendem só adultos (`README.md:15`); a página de agendamento não é direcionada a menores nem tem atrativo para eles; não há jogos, itens virtuais, monetização por engajamento nem aplicativo em loja. Sem outro indício, o módulo não é ativado e a decisão fica registrada aqui. Se alguma clínica passar a atender menores, ativar `eca-digital` e reavaliar o art. 14 da LGPD.
- `plataformas-digitais`: não há conteúdo de terceiros com difusão pública, venda de anúncios ou impulsionamento, nem IA que gere ou altere imagem ou som. Como a AgendaFácil é provedora de aplicações de internet, os deveres gerais do art. 16-A do Decreto nº 8.771/2016 foram verificados por `governance` (GV-06 e GV-07). A guarda de registros de acesso (MCI, art. 15) é avaliada uma única vez, como item de `cloud` (IN-04).
- `ai-llm`: não há IA no produto. Evidência da inexistência: nenhuma dependência de SDK ou provedor de IA (`package.json:15-25`) e nenhuma chamada a modelo no código; o gatilho técnico do roteador não é acionado (ver área `ai_llm` em `score_lgpd`).
- `mobile`: não há aplicativo móvel (`package.json:15-25`; só páginas web em `public/`).

**Escopo do score:** o cenário `saas_web` é direcionado. O relatório traz a marca **escopo direcionado**, e os domínios 8 (mobile), 12 (IA/LLM), 16 (ECA Digital) e 17 (plataformas digitais) ficaram fora da auditoria, pelas razões acima. Como o produto trata dados de saúde, vale repetir a auditoria com `/lgpd-full-audit` quando houver acesso aos painéis.

### Limitações e convenções

- **Aplicabilidade** (`core/scoring-engine.md`): cada item é `APLICAVEL`, `NAO_APLICAVEL` ou `NAO_VERIFICADO`. Só o item `APLICAVEL` tem status e entra no score.
  - `NAO_APLICAVEL`: o objeto não existe no projeto, com evidência da inexistência, ou a obrigação é de outro agente (aqui, das clínicas controladoras).
  - `NAO_VERIFICADO`: controle técnico que só pode ser conferido na produção ou no painel de um provedor. Gera uma verificação pendente.
  - Documento que deveria existir e não foi apresentado é `AUSENTE` e reduz o score; nunca é `NAO_VERIFICADO`.
  - Item com elementos verificáveis e elementos fora do alcance: se um verificável falha, vale a falha; se todos atendem, o item fica `NAO_VERIFICADO`, com o que já foi comprovado registrado (casos de IN-02, SE-09 e DS-11). `CONFORME` exige tudo comprovado.
- **Achados** (`core/auditor-core.md`): todo item `NAO_CONFORME` ou `PARCIAL` gera um achado em `nao_conformidades`.
  - No `NAO_CONFORME`, a severidade do achado é a `criticality` do item.
  - No `PARCIAL`, a severidade é um nível abaixo da `criticality`.
- **Status** (`core/evidence-engine.md`): `NAO_CONFORME` quando o controle não existe, quando existe mas a análise encontrou a violação que ele deveria impedir (caso de SE-03) ou quando menos da metade dos elementos do item está atendida (casos de DT-04, CK-04, CK-06 e SE-04); `PARCIAL` quando o controle existe, não há violação e falta parte.
- **Contagem única** (`core/scoring-engine.md`): cada item é avaliado pelo seu próprio requisito, e uma mesma falha não é contada duas vezes. Quando parte do requisito repete a falha de outro item, o item a cita e pontua pelo que resta; quando o requisito inteiro falha, o item é reprovado, mesmo com causa comum. Neste relatório:
  - O Meta Pixel reprova quatro itens, por quatro obrigações distintas: OP-02 (operadora que usa dados dos pacientes para finalidade própria, art. 39), CK-02 (rastreamento antes do consentimento, arts. 7º, I e 8º), TI-02 (transferência internacional sem mecanismo, art. 33) e TI-05 (dado que revela informação de saúde enviado ao exterior sem proteção, art. 11). CK-03 cita a mesma falha e só pontua pela lacuna própria da revogação.
  - A CSP enfraquecida pela hospedagem reprova só IN-01; SE-02 a cita e pontua pelo que resta do seu requisito.
  - A falta de limitação de tentativas no login reprova só AP-03; SE-04 a cita.
  - A falta de contrato com as clínicas reprova só OP-01; BL-02 e GV-01 a citam.
  - A falta de processo de incidentes reprova OP-04 (aviso às clínicas) e GV-08 (comunicação à ANPD e aos titulares nos dados próprios): são dois requisitos, cada um inteiro sem atendimento.
  - Itens que dependem de um controle inexistente ficam `NAO_APLICAVEL`, com a referência ao item que conta a falha: GV-05 e GV-10 (dependem de GV-02), GV-13 (depende de GV-12), BL-01 (depende de BL-02), DT-09 (depende de DT-06) e TI-03 (depende de TI-02). As dependências são só as que o catálogo lista.
- **Evidência:** formato `GRAU (ORIGEM), confiança NIVEL: descrição`, com caminho e linha dos arquivos do projeto; várias evidências são separadas por ponto e vírgula. Confiança, pela escala de `core/evidence-engine.md`:
  - `ALTA`: prova direta e rastreável do que o item exige;
  - `MEDIA`: prova direta de um lado só (por exemplo, o código sem confirmação em produção, ou a ausência constatada no repositório e declarada pela fundadora);
  - `BAIXA`: prova indireta ou incompleta.
- **Prazos:** `IMEDIATO` significa até 7 dias. `IMEDIATO` e `30_DIAS` entram no curto prazo, `90_DIAS` no médio e `180_DIAS` no longo.
- **Itens do checklist:** são os do catálogo dos módulos ativos (`core/scoring-engine.md`, "Catálogo de itens"), todos avaliados: 109 itens. O ID, o texto, a área, a `criticality` e o `control_type` vêm do catálogo; quando a `criticality` usa o agravante da linha do item, a evidência diz qual. Prefixos: `BL` bases legais, `OP` obrigações de operador, `DP` dados de acesso público, `CS` consentimento, `CA` crianças e adolescentes, `CK` cookies, `SE` segurança, `DS` DevSecOps, `DT` direitos do titular e transparência, `GV` governança, `TI` transferência internacional, `IN` infraestrutura, `AP` APIs e integrações.

---

## 1. Resumo executivo

### Nível geral de conformidade

**Score LGPD: 20/100. Classificação: `CRITICO`, com escopo direcionado (cenário `saas_web`).** Cobertura da análise: 82,9% (63 de 76 itens verificáveis), acima do mínimo de 80%; o score não é parcial.

O AgendaFácil tem pontos técnicos bem feitos (senhas com bcrypt, HTTPS, consultas parametrizadas, segredos fora do código). Três problemas puxam o resultado para baixo:

1. **A AgendaFácil usa dados de pacientes para fim próprio.** Ela é operadora das clínicas, mas instalou um pixel de publicidade na página em que os pacientes marcam consulta. É um dos dois achados `CRITICO`.
2. **A rota pública de agendamento expõe pacientes.** Quem souber o CPF de um paciente consegue, sem login, ver o nome e a data de nascimento dele e trocar o telefone e o e-mail cadastrados. É o outro achado `CRITICO`.
3. **Quase nenhum documento existe.** Não há contrato com as clínicas nem com os provedores, registro das operações, encarregado, processo de incidentes ou aviso de privacidade publicado. O score documental é 3,8; o técnico, 29,6.

Como o produto trata **dados de saúde**, nenhuma severidade pôde ser reduzida pelo porte da empresa. Por outro lado, o papel de operadora tira da AgendaFácil obrigações que são das clínicas: a base legal dos dados dos pacientes, o consentimento, a política dirigida a eles e o canal de direitos ficaram fora do cálculo. O teto de classificação por achado crítico não muda nada aqui, porque o score já está na faixa `CRITICO`.

As cinco ações abaixo custam pouco e atacam os riscos mais graves. Três delas se resolvem em menos de uma semana.

### Síntese de riscos por severidade

| Severidade | Achados | Itens |
|---|---|---|
| `CRITICO` | 2 | OP-02, SE-03 |
| `ALTO` | 24 | BL-02, CK-02, SE-04, SE-06, SE-07, DS-02, DS-08, DT-01, DT-03, OP-01, OP-03, OP-04, GV-01, GV-02, GV-03, GV-06, GV-08, GV-09, TI-02, TI-04, TI-05, IN-01, AP-01, AP-02 |
| `MEDIO` | 22 | CK-03, CK-04, CK-05, CK-06, CK-07, DS-07, DS-09, DT-02, DT-04, DT-06, DT-07, DT-10, OP-06, GV-04, GV-12, GV-14, GV-15, GV-16, TI-01, IN-16, AP-03, AP-05 |
| `BAIXO` | 6 | SE-10, DS-03, DT-05, OP-05, GV-17, IN-15 |

Dos 109 itens do catálogo avaliados, 63 são `APLICAVEL` (9 `CONFORME`, 4 `PARCIAL` e 50 `NAO_CONFORME`), 33 são `NAO_APLICAVEL` e 13 são `NAO_VERIFICADO`.

### O que fazer agora

| # | Ação, em linguagem simples | Por que importa | Esforço | Prazo | Itens |
|---|---|---|---|---|---|
| 1 | Tirar o Meta Pixel da página de agendamento. Se ele for necessário para marketing, usá-lo só no site institucional, e só depois do "Aceitar". | A AgendaFácil trata os dados dos pacientes em nome das clínicas. Usar a visita e o agendamento deles para a própria publicidade foge desse papel, revela que a pessoa procura atendimento de saúde e envia isso à Meta, nos EUA, antes de qualquer escolha. | P | `IMEDIATO` | OP-02, CK-02, CK-03, TI-02, TI-05 |
| 2 | Parar de gravar CPF e e-mail nos logs e apagar os logs antigos da Vercel. | Qualquer pessoa com acesso aos logs vê CPF e e-mail de pacientes. | P | `IMEDIATO` | SE-06 |
| 3 | Corrigir a rota pública de agendamento, que hoje troca os contatos de um paciente já cadastrado e entrega os dados dele; fazer a confirmação devolver só data e horário; dar validade de 8 horas ao login (JWT); corrigir a CSP do `vercel.json`. | Quem souber o CPF de um paciente consegue ver nome e data de nascimento e trocar os contatos dele, sem login; a confirmação devolve CPF e motivo da consulta a quem tiver o código; um token de login vazado vale para sempre; a CSP atual desliga a proteção contra scripts maliciosos. | P | `IMEDIATO` | SE-03, AP-02, AP-01, IN-01 |
| 4 | Formalizar os contratos: termos com as clínicas (quem é controlador, quem é operador, instruções, aviso de incidentes) e contratos de proteção de dados com a Vercel e o provedor do banco, conferindo se trazem as cláusulas-padrão da ANPD. | Sem contrato, a AgendaFácil responde junto com as clínicas por qualquer problema e não consegue demonstrar a base dos envios de dados ao exterior. | M | `30_DIAS` | OP-01, OP-03, OP-04, GV-08, GV-09, TI-02 |
| 5 | Publicar um aviso de privacidade da própria AgendaFácil (contas das clínicas e cookies), com canal para pedidos e contato do encarregado, e deixar claro que os dados dos pacientes são de responsabilidade das clínicas. | O link do rodapé não leva a página nenhuma, não há canal para pedidos e o texto atual confunde os papéis. | M | `30_DIAS` | DT-01, DT-03, DT-04, DT-07, TI-04, GV-02 |

### Riscos aceitos

Nenhum risco `CRITICO` foi aceito. Há um risco `ALTO` aceito (GV-03, RIPD do rastreamento para fins próprios), detalhado em `nao_conformidades` e em `riscos_identificados`. O aceite não altera o score.

### Pontos fortes

Senhas com bcrypt (SE-01), HTTPS com HSTS (SE-02), consultas parametrizadas e saída escapada (SE-05), segredos do pipeline em secrets do CI (DS-01), TLS com o banco (AP-04), nenhuma chave no código nem no front-end (AP-06), sede e contato no País publicados (GV-07) e banner com botão "Rejeitar" tão visível quanto "Aceitar" (CK-01). Os dados em repouso ficam no Brasil (`sa-east-1`).

---

## 2. Score LGPD

### Resultado

| Indicador | Valor |
|---|---|
| **Score global** | **20/100** |
| **Classificação final** | **`CRITICO`** (faixa 0-49) |
| Marcas da classificação | **escopo direcionado** (cenário `saas_web`): a classificação vale para o que o cenário auditou. O teto por achado crítico (OP-02, SE-03) não altera a classificação, que já está na faixa `CRITICO` |
| Domínios fora do escopo | 8. Mobile security: não há aplicativo móvel; 12. IA/LLM: não há IA no produto; 16. ECA Digital: sem indício de público infantojuvenil; 17. Plataformas digitais: sem conteúdo de terceiros, anúncios pagos nem IA que gere imagem ou voz |
| Cobertura global | 82,9% (63 itens com status ÷ 76 verificáveis); acima de 80%, o score **não** é parcial |
| `score_tecnico` (informativo) | 29,6 |
| `score_documental` (informativo) | 3,8 |
| Natureza do agente | pessoa jurídica com fins econômicos, de pequeno porte, com tratamento de alto risco (dados de saúde) |
| Papel do agente | operadora dos dados dos pacientes; controladora das contas das clínicas e do rastreamento para fins próprios |
| Modulação de severidade | nenhuma: a condição "sem tratamento de alto risco" de `core/severity-model.md` não é atendida |

### Regras aplicadas (`core/scoring-engine.md`)

- Os itens são os do catálogo dos módulos ativos, todos avaliados. Só itens `APLICAVEL` entram nas somas; `NAO_APLICAVEL` e `NAO_VERIFICADO` ficam fora.
- Valor do item: `CONFORME` = 1; `PARCIAL` = 0,5; `NAO_CONFORME` = 0.
- Peso do item pela `criticality` do catálogo: `CRITICO` = 4; `ALTO` = 3; `MEDIO` = 2; `BAIXO` = 1 (sem modulação por porte). Agravantes da linha do item aplicados: OP-02 (`CRITICO`, dado sensível), SE-03 (`CRITICO`, falha explorável com exfiltração), OP-03, GV-01 e GV-09 (`ALTO`, dado sensível), GV-03 (`ALTO`, tratamento de alto risco) e DS-02 (`ALTO`, nenhuma varredura no pipeline).
- `score_area = 100 × Σ(valor × peso) / Σ(peso)`. Cada item pontua em uma única área, definida pelo domínio, e cada falha é contada uma única vez.
- `score_global = Σ(score_area × peso_ajustado_area)`.
- O cálculo usa valores exatos. O score de cada área aparece com uma casa decimal, e só o score global é arredondado, para o inteiro mais próximo (fração de 0,5 sobe).
- Teto de classificação: achados `CRITICO` abertos: 2 (OP-02, SE-03). O teto limitaria a classificação a `PARCIALMENTE_CONFORME`; como o score já está na faixa `CRITICO`, ele não altera o resultado.
- Escopo: cenário `saas_web`, direcionado. A classificação vale para o que o cenário auditou.

### Áreas não aplicáveis

| Área | Status | Justificativa |
|---|---|---|
| `ai_llm` | `NAO_APLICAVEL` | Objeto inexistente, com evidência: nenhuma dependência de SDK ou provedor de IA (`package.json:15-25`), nenhuma chamada a modelo no código (`src/`, `api/`) e nenhum fluxo de IA declarado (`README.md:18-25`). O gatilho técnico de `ai-llm` em `orchestrator/router.md` não é acionado, e a exclusão está registrada no escopo excluído. |
| `eca_digital` | `NAO_APLICAVEL` | Sem indício de público infantojuvenil: serviço B2B para clínicas que atendem só adultos (`README.md:15`), sem jogos, itens virtuais, monetização por engajamento nem aplicativo em loja. O gatilho normativo de `eca-digital` não é acionado, e a decisão está registrada no escopo excluído. |
| `plataformas_digitais` | `NAO_APLICAVEL` | Objeto inexistente: não há conteúdo de terceiros com difusão pública, venda de anúncios ou impulsionamento, nem IA que gere ou altere imagem ou som (`src/routes/`, `public/`). O gatilho normativo de `plataformas-digitais` não é acionado. Os deveres gerais de provedor de aplicações são avaliados em GV-06, GV-07 e IN-04. |

### Cálculo e cobertura por área

| Área | Itens com status | Σ(valor × peso) | Σ(peso) | `score_area` | Peso original | Peso ajustado | `NAO_VERIFICADO` | Cobertura | `NAO_APLICAVEL` |
|---|---|---|---|---|---|---|---|---|---|
| `bases_legais` | 10 | 5,5 | 25 | 22,0 | 12% | 16,67% | 0 | 100% | 19 |
| `seguranca` | 14 | 15,0 | 40 | 37,5 | 20% | 27,78% | 3 | 82,4% | 4 |
| `direitos_titular` | 8 | 0,5 | 17 | 2,9 | 12% | 16,67% | 0 | 100% | 2 |
| `governanca` | 22 | 3,0 | 55 | 5,5 | 12% | 16,67% | 0 | 100% | 6 |
| `infraestrutura` | 3 | 0,0 | 6 | 0,0 | 8% | 11,11% | 10 | 23,1% | 2 |
| `apis_integracoes` | 6 | 6,0 | 16 | 37,5 | 8% | 11,11% | 0 | 100% | 0 |
| `ai_llm` | — | — | — | `NAO_APLICAVEL` | 8% | — | — | — | — |
| `eca_digital` | — | — | — | `NAO_APLICAVEL` | 10% | — | — | — | — |
| `plataformas_digitais` | — | — | — | `NAO_APLICAVEL` | 10% | — | — | — | — |
| **Total** | **63** | **30,0** | **159** | | **100%** | **100%** | **13** | **82,9%** | **33** |

**Score global = 20** (valor exato 19,649…, arredondado para o inteiro mais próximo).

Cobertura = itens com status ÷ (itens com status + itens `NAO_VERIFICADO`). A área `infraestrutura` recebe a marca **cobertura baixa** (23,1%, abaixo de 50%): seu score (0,0) se apoia em só 3 dos 13 itens verificáveis e deve ser lido com cautela até as verificações pendentes serem feitas.

**Memória de cálculo** (valor × peso de cada item, na ordem do checklist; frações exatas):

- `bases_legais`: BL-02 0×3 + BL-04 1×2 + OP-02 0×4 + CK-01 1×2 + CK-02 0×3 + CK-03 0,5×3 + CK-04 0×2 + CK-05 0×2 + CK-06 0×2 + CK-07 0×2 = **5,5 / 25**
- `seguranca`: SE-01 1×4 + SE-02 1×3 + SE-03 0×4 + SE-04 0×3 + SE-05 1×3 + SE-06 0×3 + SE-07 0×3 + SE-10 0,5×2 + DS-01 1×4 + DS-02 0×3 + DS-03 0×1 + DS-07 0×2 + DS-08 0×3 + DS-09 0×2 = **15 / 40**
- `direitos_titular`: DT-01 0×3 + DT-02 0×2 + DT-03 0×3 + DT-04 0×2 + DT-05 0,5×1 + DT-06 0×2 + DT-07 0×2 + DT-10 0×2 = **0,5 / 17**
- `governanca`: OP-01 0×3 + OP-03 0×3 + OP-04 0×3 + OP-05 0,5×2 + OP-06 0×2 + GV-01 0×3 + GV-02 0×3 + GV-03 0×3 + GV-04 0×2 + GV-06 0×3 + GV-07 1×2 + GV-08 0×3 + GV-09 0×3 + GV-12 0×2 + GV-14 0×2 + GV-15 0×2 + GV-16 0×2 + GV-17 0×1 + TI-01 0×2 + TI-02 0×3 + TI-04 0×3 + TI-05 0×3 = **3 / 55**
- `infraestrutura`: IN-01 0×3 + IN-15 0×1 + IN-16 0×2 = **0 / 6**
- `apis_integracoes`: AP-01 0×3 + AP-02 0×3 + AP-03 0×2 + AP-04 1×3 + AP-05 0×2 + AP-06 1×3 = **6 / 16**
- **Global:** [12 × (550/25) + 20 × (1500/40) + 12 × (50/17) + 12 × (300/55) + 8 × (0/6) + 8 × (600/16)] / 72 = 1414,75 / 72 = 19,649… → **20 → `CRITICO`**

As seis áreas aplicáveis somam 72%. Cada peso foi dividido por 0,72: `peso_ajustado_area = peso_area / 0,72`.

### Score técnico e score documental (informativos)

Mesma fórmula, aplicada a todos os itens `APLICAVEL` de cada `control_type`. Não entram na classificação final.

| Subtotal | Itens | Σ(valor × peso) | Σ(peso) | Score |
|---|---|---|---|---|
| `score_tecnico` (`TECNICO`) | 35 | 27,5 | 93 | **29,6** |
| `score_documental` (`DOCUMENTAL`) | 28 | 2,5 | 66 | **3,8** |

Itens `DOCUMENTAL`: BL-02, CK-07, DT-01, DT-02, DT-03, DT-04, DT-05, DT-07, DT-10, OP-01, OP-03, OP-04, GV-01, GV-02, GV-03, GV-04, GV-07, GV-08, GV-09, GV-14, GV-15, GV-16, GV-17, TI-01, TI-02, TI-04, IN-15, AP-05. Todos os demais são `TECNICO`. Leitura: o código tem falhas pontuais e corrigíveis, mas a lacuna maior é documental. Quase nada do que a LGPD pede por escrito existe hoje.

### Verificações pendentes que podem alterar o score

**Itens `NAO_VERIFICADO`** (fora do cálculo até a verificação; cada um pode entrar como `CONFORME`, `PARCIAL` ou `NAO_CONFORME`):

| Item | O que falta conferir | Justificativa e acesso necessário |
|---|---|---|
| SE-09 | Há segregação de ambientes (produção, homologação, desenvolvimento) e de funções de quem acessa dados pessoais? (`criticality` `MEDIO`) | Verificado: as funções são segregadas por papel (`api/index.js:40-41`, `db/schema.sql:16`) e as credenciais de cada ambiente vêm de variáveis (`src/db.js:4`, `.env.example:1-9`). Fora do alcance: se produção, preview e desenvolvimento têm banco e variáveis próprios, o que só aparece nos painéis. Acesso necessário: painéis da Vercel e do banco |
| DS-10 | A branch de produção é protegida, com revisão obrigatória antes do deploy? (`criticality` `MEDIO`) | A proteção da branch `main` e a revisão obrigatória são configurações do repositório no GitHub; o código só mostra que todo push na `main` vai para produção (`.github/workflows/ci.yml:20-26`). Acesso necessário: configurações do repositório no GitHub |
| DS-11 | Ambientes de teste, homologação e CI usam dados sintéticos ou mascarados, sem cópia de dados pessoais reais de produção? (`criticality` `ALTO`) | Verificado: o CI não usa banco de dados (`.github/workflows/ci.yml:9-18`), o repositório não traz cópia de dados de produção e o `README.md:33` orienta o uso de dados fictícios. Fora do alcance: qual banco os deploys de preview usam, definido no painel. Acesso necessário: variáveis de ambiente por ambiente no painel da Vercel |
| IN-02 | Variáveis de ambiente e segredos ficam no cofre do provedor, fora do repositório e de builds ou previews públicos? (`criticality` `CRITICO`) | Verificado: o `.gitignore` exclui o `.env` (`.gitignore:2-4`), o código lê os segredos de variáveis de ambiente (`src/auth.js:26`, `src/db.js:4`) e nenhuma credencial aparece nos arquivos do repositório. Fora do alcance: se as variáveis estão no cofre da Vercel e fora de builds e previews públicos. Acesso necessário: painel da Vercel |
| IN-03 | Bancos de dados com dados pessoais têm criptografia em repouso, controle de acesso e segregação? (`criticality` `ALTO`) | Configuração visível só no painel do provedor do Postgres. O repositório mostra apenas a região e o TLS (`.env.example:5-6`, `src/db.js:5`). Acesso necessário: painel do provedor do banco. Backups e réplicas são avaliados em IN-10 |
| IN-04 | Provedor de aplicações de internet: os registros de acesso (IP, porta lógica de origem, data e hora) são guardados por 6 meses e eliminados após o prazo, salvo requisição cautelar? (`criticality` `MEDIO`) | A retenção e a exportação dos logs são configuradas no painel da Vercel, não no `vercel.json`. O código não mantém guarda própria. Acesso necessário: painel da Vercel |
| IN-05 | As permissões de acesso ao provedor (IAM, membros do painel, tokens de deploy) seguem privilégio mínimo, com MFA? (`criticality` `ALTO`) | Membros, papéis e MFA só aparecem nos painéis. Acesso necessário: painéis da Vercel, do banco e do GitHub |
| IN-06 | Analytics, logs de acesso e métricas nativos do provedor que coletam dados pessoais têm retenção, acesso e base legal definidos? (`criticality` `MEDIO`) | Configuração do painel da Vercel. O código não inclui o script de analytics da plataforma (`public/index.html:1-56`). Acesso necessário: painel da Vercel |
| IN-07 | Há firewall ou WAF, detecção de intrusão e monitoramento centralizado (SIEM ou equivalente) capazes de detectar acesso indevido a dados pessoais? (`criticality` `MEDIO`) | Regras e alertas ficam no painel da Vercel. Acesso necessário: painel da Vercel |
| IN-09 | A segmentação de rede e as regras de exposição externa estão adequadas? (`criticality` `MEDIO`) | Em PaaS não há rede gerida pelo cliente (`vercel.json:1-20`), mas as regras de exposição do banco gerenciado (lista de IPs, acesso público) ficam com a AgendaFácil e só aparecem no painel do provedor; o repositório mostra apenas o TLS (`src/db.js:5`). Acesso necessário: painel do provedor do banco |
| IN-10 | Backups e réplicas são criptografados, têm acesso restrito e seguem a política de retenção (a eliminação também os alcança)? (`criticality` `ALTO`) | Criptografia, acesso e retenção dos backups e das réplicas são configurados no painel do provedor do Postgres; o repositório não os mostra. Acesso necessário: painel do provedor do banco |
| IN-11 | Os logs de auditoria da conta cloud ou do painel estão ativos e protegidos contra alteração? (`criticality` `ALTO`) | Os registros de auditoria das contas (quem alterou configurações, variáveis e membros) ficam nos painéis. Acesso necessário: painéis da Vercel, do banco e do GitHub |
| IN-14 | Chaves e segredos de produção ficam em serviço dedicado (KMS, Secrets Manager ou equivalente), com rotação? (`criticality` `MEDIO`) | Os segredos estão no cofre de variáveis da Vercel e do GitHub (IN-02, DS-01), mas a rotação e o controle de acesso a eles só aparecem nos painéis. Acesso necessário: painéis da Vercel e do GitHub |

**Itens cuja severidade ou status dependem de verificação ainda não feita:**

| Item | Situação atual | O que pode mudar | Verificação |
|---|---|---|---|
| TI-02 | `NAO_CONFORME`, `ALTO` (peso 3): mecanismo de transferência não evidenciado; confiança `BAIXA` | Sobe para `CRITICO` (peso 4) se os termos não tiverem CPC nem outro mecanismo; passa a `CONFORME` se as CPC estiverem incorporadas. Com o mecanismo evidenciado, TI-03 deixa de ser `NAO_APLICAVEL` e passa a ser avaliado | Examinar os termos da Meta, da Vercel e do provedor do banco |
| GV-09 | `NAO_CONFORME`, `ALTO`: contratos com os provedores não evidenciados; confiança `BAIXA` | Passa a `PARCIAL` ou `CONFORME` se os termos padrão já trouxerem DPA | Reunir os DPAs e os termos aceitos no cadastro |
| DS-02 | `NAO_CONFORME`, `ALTO`: sem varredura no pipeline; confiança `MEDIA` | Passa a `PARCIAL` se os alertas do Dependabot estiverem ligados nas configurações do repositório | Configurações de segurança do GitHub |
| DS-08 | `NAO_CONFORME`, `ALTO`: sem varredura de segredos no pipeline; confiança `MEDIA` | Passa a `PARCIAL` ou `CONFORME` se a proteção contra segredos do GitHub estiver ligada | Configurações de segurança do GitHub |
| DS-07 | `NAO_CONFORME`, `MEDIO`: sem SAST no pipeline; confiança `MEDIA` | Passa a `PARCIAL` se o CodeQL estiver ligado pela configuração padrão do GitHub | Configurações de segurança do GitHub |
| AP-03 | `NAO_CONFORME`, `MEDIO`: sem limitação de taxa no código; confiança `MEDIA` | Passa a `PARCIAL` ou `CONFORME` se houver limitação no firewall da plataforma | Painel da Vercel |
| IN-01 | `NAO_CONFORME`, `ALTO`: CSP fraca no `vercel.json`; confiança `MEDIA` | A coleta dos cabeçalhos confirma o achado e mostra qual política vale nas respostas da API | `curl -I` na página e na API em produção |
| DT-03 | `NAO_CONFORME`, `ALTO`: página da política ausente do deploy; confiança `MEDIA` | Passa a `PARCIAL` se a página existir em produção por outro meio | `curl -I https://<domínio>/privacidade` |
| SE-02 | `CONFORME`, confiança `MEDIA`: HSTS comprovado no código da API | Passa a `PARCIAL` se as páginas estáticas não receberem HSTS | `curl -I` na página em produção |
| OP-02 | `NAO_CONFORME`, `CRITICO`; confiança `MEDIA` | Não muda a severidade; mostra a extensão do que a Meta recebe (por exemplo, campos do formulário pela correspondência avançada automática) | Captura de rede (HAR) antes e depois do aceite; configuração do pixel no Gerenciador de Eventos da Meta |

### Efeito do risco aceito

O item GV-03 (RIPD) tem aceite de risco registrado e continua `NAO_CONFORME`, com valor 0 e peso 3 em `governanca`. Com ou sem o aceite, `governanca` = 3 / 55 = 5,5 e o score global = 20. Aceitar um risco não torna o item conforme, e não afasta o teto de classificação.

---

## 3. Checklist de conformidade

O checklist traz todos os itens do catálogo dos módulos ativos. As tabelas por área listam só os itens `APLICAVEL`. Na coluna **Item**: ID do catálogo · `criticality` (define o peso) · `control_type` — requisito. Os itens `NAO_APLICAVEL` e `NAO_VERIFICADO` estão na tabela "Itens fora do cálculo", logo depois.

### `bases_legais`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **BL-02** · `ALTO` · `DOCUMENTAL` — Cada finalidade de tratamento está ligada a uma base legal do artigo aplicável (7º ou 11), comprovável por evidência técnica ou documental? | `bases_legais` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: nenhum documento indica a base legal dos tratamentos próprios (contas dos usuários das clínicas): o rascunho da política não traz base por finalidade (`docs/lgpd/politica-de-privacidade.md:22-26`), não há registro das operações e a fundadora confirmou que não existem outros documentos. A relação contratual que sustentaria o art. 7º, V, só aparece de forma indireta (`README.md:16`; `db/schema.sql:11-18`). O objeto do item são dados cadastrais, não sensíveis: a `criticality` fica em `ALTO`. A falta de termos com as clínicas é contada em OP-01 | Base legal não demonstrável numa fiscalização | Nomear a base de cada tratamento próprio no registro e no aviso de privacidade |
| **BL-04** · `MEDIO` · `TECNICO` — Os dados coletados em cada formulário, cadastro ou integração se limitam ao necessário para a finalidade, sem campo obrigatório que ela não exija? | `bases_legais` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `ALTA`: nos tratamentos próprios, a coleta é mínima: a conta do usuário da clínica guarda só e-mail, hash da senha e papel (`db/schema.sql:11-18`), e o login pede só e-mail e senha (`src/auth.js:11-16`). Os campos do formulário de agendamento, com CPF e data de nascimento obrigatórios (`public/index.html:29-35`), são do fluxo em que as clínicas são controladoras: a revisão deles vai para as recomendações. O rastreamento pelo pixel é contado em OP-02 e CK-02 | — | Manter; sugerir às clínicas rever a obrigatoriedade do CPF e da data de nascimento no agendamento |
| **OP-02** · `CRITICO` · `TECNICO` — O tratamento se limita às instruções documentadas do controlador, sem uso dos dados para finalidade própria? | `bases_legais` | `NAO_CONFORME` | `AUSENTE (TECNICA + DOCUMENTAL)`, confiança `MEDIA`: o Meta Pixel da própria AgendaFácil ("campanhas de aquisição", `public/index.html:7-15`; `README.md:24`) registra a visita à página da clínica e o evento de agendamento (`public/js/agendar.js:23`); nenhuma instrução ou autorização das clínicas documentada; sem captura de rede em produção | Operadora usa dados dos pacientes para publicidade própria; a visita e o agendamento revelam busca por atendimento de saúde (art. 11, §1º) | Remover o pixel da página de agendamento |
| **CK-01** · `MEDIO` · `TECNICO` — Rejeitar está disponível na primeira camada do banner, com o mesmo destaque de aceitar? | `bases_legais` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `ALTA`: botões lado a lado, com o mesmo elemento e o mesmo estilo (`public/index.html:41-45` e `:22`); ambos gravam a escolha (`public/js/consent.js:24-25`) | — | Manter |
| **CK-02** · `ALTO` · `TECNICO` — Cookies e scripts não essenciais ficam bloqueados até o aceite, sem requisições a terceiros de analytics ou publicidade antes do consentimento — salvo outra base legal documentada (ex.: legítimo interesse com LIA para medição estritamente agregada)? | `bases_legais` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: `public/index.html:8-15` carrega `fbevents.js` e dispara `PageView` no `<head>`, antes de `consent.js` rodar (`public/index.html:53`); nenhuma outra base legal documentada | Rastreamento sem consentimento válido, inclusive de quem clica em "Rejeitar" | Carregar qualquer rastreador só após o aceite |
| **CK-03** · `ALTO` · `TECNICO` — O usuário consegue revisar e revogar as preferências a qualquer momento, com efeito real sobre os scripts já carregados? | `bases_legais` | `PARCIAL` | `PARCIAL (TECNICA)`, confiança `ALTA`: o link "Preferências de cookies" reabre o banner (`public/index.html:50`, `public/js/consent.js:26-29`) e a recusa chama `fbq('consent', 'revoke')` (`consent.js:6-9`), o que interrompe os eventos seguintes, mas não remove o cookie `_fbp` nem o script já carregado; o `PageView` enviado antes da escolha é a falha de CK-02 e não é contado de novo aqui | Identificador da Meta continua no navegador depois da revogação | Na revogação, apagar `_fbp` e não recarregar o pixel |
| **CK-04** · `MEDIO` · `TECNICO` — As escolhas ficam registradas (data, versão do banner, categorias aceitas) como prova do consentimento? | `bases_legais` | `NAO_CONFORME` | `PARCIAL (TECNICA)`, confiança `ALTA`: dos três elementos do registro (data, versão do banner e categorias aceitas), só a data é gravada, e apenas no navegador do visitante (`public/js/consent.js:11-13`); não há versão do banner, categorias nem cópia do lado da empresa. Menos da metade: `NAO_CONFORME` | A AgendaFácil não consegue provar o consentimento | Registrar no servidor data, versão do banner e categorias |
| **CK-05** · `MEDIO` · `TECNICO` — O consentimento é granular por finalidade (desempenho, funcionalidade, publicidade)? | `bases_legais` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: o banner oferece apenas aceitar ou rejeitar tudo, sem separar finalidades (`public/index.html:41-45`); a falta de informação sobre finalidades e terceiros é contada em CK-06 | Não há como aceitar medição e recusar publicidade | Separar categorias (necessários, medição, publicidade) |
| **CK-06** · `MEDIO` · `TECNICO` — Existe banner ou CMP funcional, com informação clara sobre finalidades e terceiros? | `bases_legais` | `NAO_CONFORME` | `PARCIAL (TECNICA)`, confiança `ALTA`: dos três elementos do item, só um está atendido: o banner existe, aparece na primeira visita e grava a escolha (`public/index.html:41-45`, `public/js/consent.js:17-25`). O texto não informa as finalidades (diz só "melhorar sua experiência") nem os terceiros (não cita a Meta) (`public/index.html:42`). Menos da metade: `NAO_CONFORME` | Consentimento sem informação prévia adequada | Nomear finalidades e terceiros no banner, com link para a política de cookies |
| **CK-07** · `MEDIO` · `DOCUMENTAL` — Pixels, fingerprinting e identificadores persistentes de terceiros estão inventariados e cobertos pela política de cookies? | `bases_legais` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: não há política de cookies nem inventário de rastreadores; o rascunho diz só que o site usa cookies (`docs/lgpd/politica-de-privacidade.md:28-30`) | Rastreadores de terceiros sem transparência nem controle | Política de cookies com cada cookie ou SDK, finalidade e prazo |

### `seguranca`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **SE-01** · `CRITICO` · `TECNICO` — Senhas e credenciais de usuários são armazenadas com hash forte e salgado (ex.: Argon2id, bcrypt), nunca em texto puro ou com cifra reversível? | `seguranca` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `ALTA`: bcrypt com custo 12 (`src/auth.js:5-8`), comparação em `src/auth.js:19`; coluna `senha_hash` (`db/schema.sql:15`) | — | Manter |
| **SE-02** · `ALTO` · `TECNICO` — Todo tráfego usa HTTPS, com HSTS e cabeçalhos de segurança (CSP, entre outros) configurados? | `seguranca` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `MEDIA`: redirecionamento para HTTPS (`api/index.js:14-19`) e HSTS de 1 ano (`api/index.js:32`) no código da API; cabeçalhos das páginas estáticas não coletados em produção; a CSP enfraquecida pela hospedagem é contada em IN-01 | — | Manter; conferir o HSTS das páginas estáticas com `curl -I` |
| **SE-03** · `CRITICO` · `TECNICO` — A autorização impede acesso indevido a dados de outros usuários ou clientes (RBAC/ABAC, isolamento entre contas)? | `seguranca` | `NAO_CONFORME` | `PARCIAL (TECNICA)`, confiança `ALTA`: nas rotas autenticadas o controle funciona: `/api/admin` exige token e papel `admin` (`api/index.js:41`, `src/auth.js:43-50`) e as rotas da clínica filtram pelo `clinica_id` do token (`src/routes/clinica.js:13` e `:28`). Mas a rota pública de agendamento, quando o CPF já existe naquela clínica, atualiza o telefone e o e-mail do paciente (`ON CONFLICT … DO UPDATE`, `src/routes/agendamentos.js:31-38`) e devolve um código; com ele, `GET /api/agendamentos/:codigo` entrega o cadastro que já existia (`:51-61`). Quem souber o CPF de um paciente e o endereço da página da clínica obtém o nome e a data de nascimento dele, confirma que é paciente e troca os contatos pelos seus. É falha explorável com exfiltração de dados pessoais (agravante do item: `CRITICO`). Os campos em excesso na resposta são contados em AP-02 | Qualquer pessoa consulta e altera dados de pacientes sem autenticação; a clínica passa a contatar o invasor no lugar do paciente | Não atualizar cadastro existente pela rota pública; tratar paciente já cadastrado sem revelar nem alterar seus dados |
| **SE-04** · `ALTO` · `TECNICO` — A autenticação é robusta (política de senha, bloqueio de tentativas e MFA quando o risco pede)? | `seguranca` | `NAO_CONFORME` | `PARCIAL (TECNICA)`, confiança `ALTA`: o login por e-mail e senha existe (`src/auth.js:11-29`), mas, dos elementos do item, nenhum dos dois que restam está atendido: não há segundo fator, embora o painel dê acesso a dados de saúde, e não há política de senha (o repositório não tem rota de criação ou troca de senha nem validação de complexidade; `src/auth.js:7-9` só gera o hash). O bloqueio de tentativas é contado em AP-03 e sai da conta | Conta de clínica protegida só por uma senha sem regra mínima | MFA para usuários de clínica e de administração e política de senha |
| **SE-05** · `ALTO` · `TECNICO` — Há proteção contra XSS, CSRF, SSRF e SQL Injection? | `seguranca` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `ALTA`: todas as consultas usam parâmetros (`src/routes/agendamentos.js:31-45` e `:52-58`, `src/routes/clinica.js:9-30`); a confirmação usa `textContent` (`public/js/agendar.js:28`); o token vai no cabeçalho `Authorization`, não em cookie (`src/auth.js:32`) | — | Manter; acrescentar validação de formato (CPF, datas) |
| **SE-06** · `ALTO` · `TECNICO` — Os logs da aplicação evitam registrar dados pessoais e sensíveis (CPF, e-mail, telefone, tokens, senhas, payloads completos) ou os mascaram antes da gravação? | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: `src/routes/agendamentos.js:29` grava nome, CPF e e-mail do paciente no console, que vira log da Vercel; `src/auth.js:20` grava o e-mail em logins que falham | Dados pessoais legíveis por quem acessa os logs | Registrar só IDs internos; expurgar os logs existentes |
| **SE-07** · `ALTO` · `TECNICO` — Há trilha de auditoria dos acessos a dados pessoais no backend (quem acessou, o quê e quando)? | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: nenhum registro de quem consultou ou alterou dados de pacientes (`api/index.js:38-41`, `src/routes/clinica.js:8-33`) | Impossível investigar acesso indevido ou dimensionar um incidente | Registrar usuário, rota, paciente e horário, sem dados pessoais no log |
| **SE-10** · `MEDIO` · `TECNICO` — Entradas e saídas são validadas e sanitizadas? | `seguranca` | `PARCIAL` | `PARCIAL (TECNICA)`, confiança `ALTA`: o agendamento confere a presença dos campos obrigatórios (`src/routes/agendamentos.js:20-22`), o corpo é limitado a 50 kB (`api/index.js:36`) e a saída usa `textContent` (`public/js/agendar.js:28`); não há validação de formato de CPF, e-mail, telefone nem datas | Dados inválidos entram no cadastro das clínicas | Validar formato e tamanho de cada campo no servidor |
| **DS-01** · `CRITICO` · `TECNICO` — Os segredos do pipeline estão protegidos (cofre do CI) e não aparecem em logs nem em artefatos? | `seguranca` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `ALTA`: token e IDs da Vercel vêm de secrets do GitHub (`.github/workflows/ci.yml:27-30`), sem eco em log | — | Manter; restringir o deploy ao ambiente protegido da `main` |
| **DS-02** · `ALTO` · `TECNICO` — Há varredura de dependências no pipeline e política de atualização? | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `MEDIA`: o pipeline roda só `install`, `lint` e `test` (`.github/workflows/ci.yml:16-18`); não há `npm audit` nem configuração do Dependabot, e o pipeline não tem nenhuma outra varredura de segurança (agravante do item: `ALTO`); as configurações de segurança do GitHub não foram vistas | Biblioteca vulnerável chega à produção sem aviso | `npm audit` no CI e Dependabot |
| **DS-03** · `BAIXO` · `TECNICO` — O SBOM é gerado e armazenado? | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: nenhum SBOM gerado no pipeline (`.github/workflows/ci.yml:9-30`) | Resposta lenta a vulnerabilidades novas | Gerar SBOM CycloneDX a cada build |
| **DS-07** · `MEDIO` · `TECNICO` — SAST e DAST são executados em estágio apropriado do pipeline? | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `MEDIA`: o pipeline roda só `install`, `lint` e `test` (`.github/workflows/ci.yml:16-18`); não há análise estática de segurança (SAST) nem dinâmica (DAST), nem fluxo de CodeQL no repositório; as configurações de segurança do GitHub não foram vistas | Falhas de código como a de AP-02 passam sem alerta | CodeQL ou equivalente no CI |
| **DS-08** · `ALTO` · `TECNICO` — Há varredura de segredos no repositório e no histórico do git, com rotação do que já foi exposto? | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `MEDIA`: nenhuma etapa de varredura de segredos no pipeline (`.github/workflows/ci.yml:9-30`); o `.gitignore:2-4` exclui o `.env` e nenhuma credencial foi encontrada nos arquivos atuais; a proteção nativa do GitHub contra segredos não foi vista | Segredo enviado por engano fica no histórico sem alerta | Proteção contra segredos do GitHub e varredura do histórico no CI |
| **DS-09** · `MEDIO` · `TECNICO` — O token do pipeline tem permissões mínimas, e as actions ou imagens de terceiros usadas nele estão fixadas por versão imutável (hash)? | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: o workflow não declara `permissions`; as actions usam a tag `v4` (`.github/workflows/ci.yml:12-13`, `:25`) e o deploy baixa a CLI da Vercel sem versão (`:26`) | Action ou pacote comprometido roda com acesso aos segredos de deploy | Declarar permissões mínimas e fixar actions por hash |

### `direitos_titular`

Valem só para os tratamentos em que a AgendaFácil é controladora: contas dos usuários das clínicas e rastreamento para fins próprios.

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **DT-01** · `ALTO` · `DOCUMENTAL` — Existe canal de atendimento claro e funcional para o exercício dos direitos do art. 18? | `direitos_titular` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: nenhum canal nem lista de direitos (`docs/lgpd/politica-de-privacidade.md:36`, TODO pendente); o rodapé só oferece um e-mail genérico (`public/index.html:48`) | Usuários das clínicas e visitantes rastreados não conseguem exercer direitos do art. 18 | Publicar canal específico, com prazo de resposta |
| **DT-02** · `MEDIO` · `DOCUMENTAL` — Há fluxo que responda aos pedidos sem custos e no prazo do art. 19 (confirmação ou acesso imediato em formato simplificado, ou declaração completa em até 15 dias)? | `direitos_titular` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum procedimento escrito em `docs/lgpd/` para receber, responder e confirmar pedidos, com prazo e responsável; a fundadora declarou não haver outros documentos. A falta de recurso no sistema é contada em DT-06 e a falta de registro dos pedidos, em DT-10 | Pedidos sem prazo nem responsável | Procedimento simples, com prazo e registro de cada pedido |
| **DT-03** · `ALTO` · `DOCUMENTAL` — Há política ou aviso de privacidade publicado, de acesso fácil e ostensivo? | `direitos_titular` | `NAO_CONFORME` | `PARCIAL (TECNICA + DOCUMENTAL)`, confiança `MEDIA`: há um rascunho em `docs/lgpd/politica-de-privacidade.md`, mas nenhuma página em `public/`, que é a pasta publicada (`vercel.json:4`), nem rota para `/privacidade`; o link do rodapé e do banner aponta para um endereço inexistente (`public/index.html:49`); produção não consultada | Quem recebe o banner de cookies não tem onde ler sobre o tratamento | Publicar a página e conferir o link em produção |
| **DT-04** · `MEDIO` · `DOCUMENTAL` — A política traz o conteúdo do art. 9º (finalidade específica, forma e duração, controlador e contato, uso compartilhado, responsabilidades dos agentes e direitos do art. 18), além da base legal por finalidade e da retenção? | `direitos_titular` | `NAO_CONFORME` | `PARCIAL (DOCUMENTAL)`, confiança `ALTA`: dos oito elementos do item, o rascunho atende dois: identificação e contato do controlador (`politica-de-privacidade.md:7-9`) e a finalidade do agendamento (`:22-25`). Faltam forma e duração do tratamento, uso compartilhado (a Meta como destinatária), responsabilidades dos agentes, direitos do art. 18, base legal por finalidade e retenção; além disso, o texto fala aos pacientes como se a AgendaFácil fosse a controladora (`:11-26`). Menos da metade dos elementos: `NAO_CONFORME`. A falta de informação sobre transferência internacional é contada em TI-04 | Transparência insuficiente; consentimento sem informação prévia é nulo (art. 9º, §1º) | Reescrever com `templates/privacy-policy-template.md`, separando os papéis |
| **DT-05** · `BAIXO` · `DOCUMENTAL` — A política usa linguagem clara e acessível e indica versão e data de atualização? | `direitos_titular` | `PARCIAL` | `PARCIAL (DOCUMENTAL)`, confiança `MEDIA`: dos três elementos, dois estão atendidos: o rascunho usa linguagem simples e traz a data de atualização (`docs/lgpd/politica-de-privacidade.md:3`). Falta a indicação de versão. A falta de publicação é contada em DT-03 e as lacunas de conteúdo, em DT-04 | Não dá para saber qual texto valia em cada data | Numerar as versões e manter o histórico ao publicar |
| **DT-06** · `MEDIO` · `TECNICO` — Há processo operacional para correção, anonimização, bloqueio, eliminação e portabilidade dos dados? | `direitos_titular` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: não há rota nem tela para consultar, corrigir, exportar ou excluir uma conta de usuário (`src/routes/clinica.js:1-55`, `api/index.js:38-41`) | Pedidos de correção, eliminação e portabilidade dependem de alteração manual no banco | Rotas autenticadas para ver, corrigir, exportar e excluir a própria conta |
| **DT-07** · `MEDIO` · `DOCUMENTAL` — O titular consegue saber com quem os dados foram compartilhados e, quando o consentimento é a base, que pode negá-lo e com que consequências? | `direitos_titular` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: nenhum documento ou tela informa os destinatários dos dados; o próprio rascunho registra a pendência (`docs/lgpd/politica-de-privacidade.md:36`) e o banner não cita a Meta (`public/index.html:42`) | O titular não tem como saber que a Meta, a Vercel e o provedor do banco recebem dados | Listar destinatários e finalidades no aviso e responder a esse pedido pelo canal de direitos |
| **DT-10** · `MEDIO` · `DOCUMENTAL` — Há trilha auditável dos pedidos (data, tipo, resposta e confirmação da execução)? | `direitos_titular` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum registro de pedidos de titulares em `docs/lgpd/`; a fundadora declarou não haver outros documentos | Impossível provar que um pedido foi atendido e quando | Planilha ou sistema de chamados com data, tipo, resposta e execução |

### `governanca`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **OP-01** · `ALTO` · `DOCUMENTAL` — Há contrato ou termo com o controlador que defina objeto, instruções, segurança, suboperadores e devolução ou eliminação dos dados ao fim? | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: a contratação é on-line (`README.md:16`), mas não há termos de uso em `public/` nem contrato em `docs/lgpd/`; a fundadora confirmou que não existe contrato; o rascunho da política apresenta a AgendaFácil como responsável, sem distinguir papéis (`politica-de-privacidade.md:9`) | Operadora de dados de saúde sem instruções documentadas; responsabilidade solidária | Termos de uso com cláusulas de operador |
| **OP-03** · `ALTO` · `DOCUMENTAL` — Os suboperadores (hospedagem, e-mail, analytics) são informados ao controlador? | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nada informa os suboperadores às clínicas, já que não há contrato (OP-01); só o `README.md:22-23` identifica a Vercel e o provedor do banco. Os contratos com esses provedores são contados em GV-09 | As clínicas não sabem quem mais trata os dados de saúde dos seus pacientes (`ALTO`) | Listar os suboperadores nos termos com as clínicas |
| **OP-04** · `ALTO` · `DOCUMENTAL` — Existe processo para avisar o controlador sem demora em caso de incidente? | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum plano, runbook ou modelo de aviso às clínicas no repositório; a fundadora declarou não haver outros documentos. A comunicação dos dados próprios à ANPD é contada em GV-08 | As clínicas não seriam avisadas a tempo de cumprir o prazo da Res. CD/ANPD nº 15/2024 | Adotar `templates/incident-response-template.md`, com o aviso às clínicas |
| **OP-05** · `MEDIO` · `TECNICO` — Existe processo para apoiar o controlador no atendimento a pedidos de titulares? | `governanca` | `PARCIAL` | `PARCIAL (TECNICA)`, confiança `ALTA`: a clínica corrige nome, telefone e e-mail (`src/routes/clinica.js:21-33`); não há rota nem rotina para exportar ou eliminar os dados de um paciente | A clínica depende de pedidos manuais à AgendaFácil para atender o paciente | Rotas autenticadas de exportação e eliminação por paciente |
| **OP-06** · `MEDIO` · `TECNICO` — Ao fim do contrato, os dados são devolvidos ou eliminados conforme instrução do controlador? | `governanca` | `NAO_CONFORME` | `AUSENTE (TECNICA + DOCUMENTAL)`, confiança `MEDIA`: o esquema não tem campo de expiração ou exclusão (`db/schema.sql:20-39`); não há rotina de exportação em lote ou de expurgo no código, nem agendamento no `vercel.json` ou no CI; nenhum procedimento escrito | Dados de saúde permanecem depois do fim do contrato; a base só cresce | Rotina de devolução e de expurgo, com registro da execução |
| **GV-01** · `ALTO` · `DOCUMENTAL` — Existe registro das operações de tratamento atualizado, com inventário e classificação de dados, ciclo de vida, compartilhamentos e retenção, sem dados órfãos (sem finalidade ou responsável)? Agente de pequeno porte pode usar a forma simplificada. | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: `docs/lgpd/` contém só o rascunho da política; o `README.md:27-29` lista dados, sem finalidade, papel, base, retenção nem compartilhamentos; a fundadora declarou não haver outros documentos | Sem mapa do que é tratado, nada mais se sustenta; com dados sensíveis, `ALTO` | Elaborar o registro completo (a forma simplificada não vale com alto risco) |
| **GV-02** · `ALTO` · `DOCUMENTAL` — Existe encarregado indicado por ato escrito, datado e assinado? | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: nenhum ato de indicação; o próprio rascunho registra a pendência do contato do encarregado (`politica-de-privacidade.md:36`); rodapé sem o contato (`public/index.html:47-51`) | Exigível: a AgendaFácil também é controladora, e a dispensa do pequeno porte não vale com alto risco (Res. CD/ANPD nº 2/2022, art. 3º) | Indicar encarregado (pode ser serviço externo) e divulgar o contato |
| **GV-03** · `ALTO` · `DOCUMENTAL` — Existe RIPD para as operações de maior risco? | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum RIPD em `docs/lgpd/`; a fundadora declarou não haver outros documentos | Rastreamento que revela busca por atendimento de saúde, sem análise de impacto | Encerrar o tratamento (OP-02) ou elaborar o RIPD (risco aceito até 2026-12-31) |
| **GV-04** · `MEDIO` · `DOCUMENTAL` — Existe política de retenção aprovada e aplicada, com prazo por categoria de dado e a hipótese do art. 16 que justifica cada conservação? | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhuma política de retenção em `docs/lgpd/`; o rascunho da política não fala de prazos | Contas e logs guardados indefinidamente | Definir prazos por categoria |
| **GV-06** · `ALTO` · `TECNICO` — Provedor de aplicações: há canal de denúncia permanente e de fácil acesso, que preveja a notificação de conteúdos criminosos ou ilícitos? | `governanca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: não há canal de denúncia: o rodapé traz só um e-mail de contato geral (`public/index.html:48`), sem página, formulário ou endereço que preveja a notificação de conteúdo criminoso ou ilícito | Descumprimento de dever vigente desde 20/07/2026 | Página simples de denúncia, que pode ser a mesma do canal de privacidade |
| **GV-07** · `MEDIO` · `DOCUMENTAL` — Provedor de aplicações: há sede e representante legal pessoa jurídica no País, com contato acessível no site? | `governanca` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `ALTA`: razão social, CNPJ, endereço em São Paulo/SP e contato no rodapé (`public/index.html:48`); a AgendaFácil é pessoa jurídica brasileira (`README.md:13`) | — | Manter |
| **GV-08** · `ALTO` · `DOCUMENTAL` — Existe processo de resposta a incidentes com responsáveis definidos e comunicação à ANPD e aos titulares em até 3 dias úteis? | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum plano, runbook ou modelo de comunicação à ANPD e aos titulares para os dados próprios (contas das clínicas e rastreamento); a fundadora declarou não haver outros documentos. O aviso às clínicas é contado em OP-04 | Sem como comunicar a ANPD e os titulares em 3 dias úteis | Incluir a comunicação dos dados próprios no processo de incidentes |
| **GV-09** · `ALTO` · `DOCUMENTAL` — Operadores e suboperadores, inclusive o provedor de hospedagem, têm contrato com cláusulas de proteção de dados (DPA)? | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `BAIXA`: nenhum DPA com a Vercel nem com o provedor do banco em `docs/lgpd/` (`README.md:22-23` identifica os provedores); os termos padrão aceitos no cadastro não foram reunidos nem examinados | Operadores que tratam dados de saúde sem obrigações demonstradas (`ALTO`) | Reunir e arquivar os DPAs dos provedores |
| **GV-12** · `MEDIO` · `TECNICO` — A eliminação ou anonimização ao fim do prazo é automática e alcança réplicas, backups e operadores? | `governanca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: nenhuma rotina de expurgo de contas ou de logs no código (`package.json:7-11`, `src/`), e as tabelas não têm campo de desativação nem de exclusão (`db/schema.sql:11-18`). A eliminação dos dados dos pacientes é contada em OP-06 | Contas e logs acumulados sem fim | Agendar o expurgo depois de definir os prazos (GV-04), incluindo backups |
| **GV-14** · `MEDIO` · `DOCUMENTAL` — As retenções legais (ex.: fiscais, trabalhistas, registros de acesso do MCI art. 15) estão identificadas e limitadas ao prazo legal? | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum documento identifica as retenções legais (registros de acesso do MCI, documentos fiscais) e seus prazos; nada em `docs/lgpd/`; a fundadora declarou não haver outros documentos | Risco de apagar o que a lei manda guardar ou de guardar além do prazo | Listar as retenções legais na política de retenção |
| **GV-15** · `MEDIO` · `DOCUMENTAL` — Existe trilha de auditoria e evidência documental contínua das decisões de privacidade (versões de políticas, atas, revisões)? | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: `docs/lgpd/` contém um único rascunho, sem versões anteriores, atas ou registro de decisões; a fundadora declarou não haver outros documentos | A empresa não consegue demonstrar as medidas que adota | Versionar os documentos de privacidade e registrar as decisões |
| **GV-16** · `MEDIO` · `DOCUMENTAL` — Existe política de segurança da informação aprovada e conhecida por quem trata dados pessoais? | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhuma política de segurança da informação em `docs/`; a fundadora declarou não haver outros documentos | Práticas de segurança dependem da memória de cada pessoa | Política curta, proporcional a uma equipe de três pessoas |
| **GV-17** · `BAIXO` · `DOCUMENTAL` — Há treinamento periódico de quem trata dados pessoais, com registro de participação? | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum registro de treinamento ou orientação da equipe em `docs/`; a fundadora declarou não haver outros documentos | Erros como o do pixel e o dos logs tendem a se repetir | Sessão anual registrada sobre papel de operadora, logs e incidentes |
| **TI-01** · `MEDIO` · `DOCUMENTAL` — O fluxo de dados para o exterior está mapeado (destino, provedor, finalidade)? | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum documento mapeia os envios ao exterior; os destinos só aparecem no código (`public/index.html:13-15`, Meta) e no `README.md:22` (Vercel); a fundadora declarou não haver outros documentos | Novos envios ao exterior surgem sem controle | Tabela de destinos, provedores, dados e mecanismo no registro das operações |
| **TI-02** · `ALTO` · `DOCUMENTAL` — Há mecanismo do art. 33 documentado para cada transferência: adequação reconhecida (União Europeia, Res. CD/ANPD nº 32/2026) ou, nos demais destinos, as CPC da Res. CD/ANPD nº 19/2024 incorporadas ao contrato, ou outro mecanismo aprovado? | `governanca` | `NAO_CONFORME` | `AUSENTE (TECNICA + DOCUMENTAL)`, confiança `BAIXA`: o fluxo é comprovado no código, pois `public/index.html:13-15` e `public/js/agendar.js:23` enviam dados do navegador do paciente à Meta, nos EUA, sem adequação reconhecida (a mesma evidência de OP-02 e CK-02, reprovada aqui por obrigação distinta, o art. 33); os logs das funções ficam com a Vercel Inc., nos EUA; o mecanismo não está evidenciado, porque os termos desses provedores não foram localizados nem examinados; a falta de informação ao titular é contada em TI-04 | Dados saem do País sem base demonstrada | Remover o pixel; examinar os termos e incorporar as CPC da Res. CD/ANPD nº 19/2024 onde faltarem |
| **TI-04** · `ALTO` · `DOCUMENTAL` — O titular é informado sobre a transferência internacional na política de privacidade? | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: o rascunho da política não menciona transferência internacional nem destinatários (`docs/lgpd/politica-de-privacidade.md:22-36`) | O titular não sabe que seus dados vão para os EUA | Informar destinos, provedores e mecanismo no aviso de privacidade |
| **TI-05** · `ALTO` · `TECNICO` — Dados sensíveis transferidos têm hipótese do art. 11 e proteção reforçada (criptografia, restrição de acesso)? | `governanca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `MEDIA`: o pixel envia à Meta, nos EUA, a visita e o agendamento na página de uma clínica (`public/index.html:13-15`, `public/js/agendar.js:23`), dado que revela busca por atendimento de saúde (art. 11, §1º), sem hipótese do art. 11 nem proteção; é a mesma evidência de OP-02, reprovada aqui por obrigação distinta. O banco, com o motivo da consulta, fica no Brasil (`.env.example:5-6`) | Informação sensível fora do País, sem proteção | Remover o pixel da página de agendamento (OP-02) |

### `infraestrutura`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **IN-01** · `ALTO` · `TECNICO` — A camada da hospedagem ou CDN preserva o que a aplicação envia (cabeçalhos de segurança e CSP, sem cache de páginas com dados pessoais, sem scripts ou analytics injetados pelo provedor)? Validar as respostas de **produção**, não só o código. | `infraestrutura` | `NAO_CONFORME` | `PARCIAL (TECNICA)`, confiança `MEDIA`: o código define CSP restritiva (`api/index.js:22-34`), mas as páginas de `public/` são servidas direto pela CDN com a CSP do `vercel.json:12-15` (`default-src * 'unsafe-inline' 'unsafe-eval'`), que libera scripts de qualquer origem e não impede o enquadramento da página por outros sites; respostas de produção não coletadas | A página que coleta CPF e dados de saúde fica sem defesa contra XSS e clickjacking | Igualar a CSP do `vercel.json` à do código e conferir com `curl -I` |
| **IN-15** · `BAIXO` · `DOCUMENTAL` — A divisão de responsabilidades com o provedor está documentada (o que é do provedor e o que é do auditado: certificados, DNS, CDN, backups, atualizações)? | `infraestrutura` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum documento define o que cabe à Vercel e ao provedor do banco e o que cabe à AgendaFácil; nada em `docs/` nem em `README.md:18-25`; a fundadora declarou não haver outros documentos | Lacunas como a CSP do `vercel.json` (IN-01) passam despercebidas | Quadro de uma página com as responsabilidades de cada parte |
| **IN-16** · `MEDIO` · `TECNICO` — Há processo de hardening e de gestão de vulnerabilidades da infraestrutura? | `infraestrutura` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `MEDIA`: o projeto fixa o Node.js 20 no CI (`.github/workflows/ci.yml:15`) e aceita qualquer versão a partir dela (`package.json:12-14`; `README.md:20`); essa linha deixou de receber correções de segurança em abril de 2026, e não há rotina de atualização do runtime no repositório. A versão em uso na produção depende do painel da Vercel, não conferido. A atualização de dependências é contada em DS-02 | A aplicação roda sobre um runtime sem correções de segurança | Migrar para uma linha do Node.js com suporte e rever a versão a cada ciclo |

### `apis_integracoes`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **AP-01** · `ALTO` · `TECNICO` — As APIs validam tokens corretamente (JWT: assinatura, algoritmo, expiração e audiência) e usam OAuth com escopos mínimos? | `apis_integracoes` | `NAO_CONFORME` | `PARCIAL (TECNICA)`, confiança `ALTA`: a assinatura é verificada, mas `jwt.sign` não define `expiresIn`, `algorithm` nem `audience` (`src/auth.js:24-27`) e `jwt.verify` não restringe algoritmos (`src/auth.js:36`) | Token vazado dá acesso permanente à agenda da clínica | Expiração curta, algoritmo fixo, audiência e revogação |
| **AP-02** · `ALTO` · `TECNICO` — As respostas das APIs expõem só os campos necessários, sem exposição excessiva de dados pessoais? | `apis_integracoes` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: `GET /api/agendamentos/:codigo` é público e devolve `SELECT a.*, p.*` (`src/routes/agendamentos.js:51-61`), com CPF, telefone, e-mail, data de nascimento e motivo da consulta; a tela usa só `data_hora` e `nome` (`public/js/agendar.js:25-30`) | Quem tiver o código (link compartilhado, histórico do navegador) lê dados de saúde e CPF | Selecionar só data, horário e primeiro nome |
| **AP-03** · `MEDIO` · `TECNICO` — Há rate limiting e proteção contra abuso nas APIs e na autenticação? | `apis_integracoes` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `MEDIA`: nenhuma limitação em `/api/login` nem em `POST /api/agendamentos` (`api/index.js:36-41`; nada em `package.json:15-22`); regras do firewall da plataforma não foram vistas | Força bruta no login e agendamentos falsos em massa | `express-rate-limit` nas rotas públicas |
| **AP-04** · `ALTO` · `TECNICO` — A comunicação com integrações e entre serviços é criptografada em trânsito? | `apis_integracoes` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `ALTA`: a conexão com o banco exige TLS com verificação de certificado (`src/db.js:5`; `sslmode=require` em `.env.example:6`); front-end e API usam HTTPS (`api/index.js:14-19`) | — | Manter |
| **AP-05** · `MEDIO` · `DOCUMENTAL` — As APIs públicas estão inventariadas (rotas, dados expostos, responsável)? | `apis_integracoes` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: as rotas públicas (`/api/agendamentos` e `/api/login`) só aparecem no código (`api/index.js:38-41`); nenhum inventário em `README.md` nem em `docs/` | Rotas e campos expostos crescem sem revisão | Tabela de rotas, autenticação, dados e responsável |
| **AP-06** · `ALTO` · `TECNICO` — As API keys ficam fora do código, dos repositórios e do front-end? | `apis_integracoes` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `ALTA`: nenhuma chave no código nem no front-end: os segredos são lidos de variáveis de ambiente (`src/auth.js:26`, `src/db.js:4`); o ID do pixel em `public/index.html:14` é identificador público, não credencial | — | Manter |

### Itens fora do cálculo

| Item | Área | Aplicabilidade | Justificativa ou acesso necessário |
|---|---|---|---|
| **BL-01** — O dado sensível é tratado só com hipótese do art. 11, sem legítimo interesse, execução de contrato ou proteção do crédito como base? | `bases_legais` | `NAO_APLICAVEL` | Obrigação do controlador. Nesse fluxo a AgendaFácil é operadora, e as clínicas decidem a base legal (em regra, tutela da saúde, art. 11, II, "f"). O uso para finalidade própria é avaliado em OP-02. Nos tratamentos próprios, nenhuma base foi indicada (BL-02), então não há base incompatível a apontar: `NAO_APLICAVEL` por dependência |
| **BL-03** — O uso de legítimo interesse tem justificativa formal e teste de balanceamento (LIA) documentados? | `bases_legais` | `NAO_APLICAVEL` | Objeto inexistente: nenhum tratamento próprio é sustentado em legítimo interesse; o rascunho da política não invoca essa base (`docs/lgpd/politica-de-privacidade.md:22-26`). A falta de base legal nomeada é contada em BL-02 |
| **DP-01** — A origem pública de cada conjunto de dados está identificada (fonte, data de coleta, finalidade original da divulgação)? | `bases_legais` | `NAO_APLICAVEL` | Objeto inexistente: o sistema não usa dado obtido de fonte pública; todos os dados vêm do formulário de agendamento e do cadastro das clínicas (`public/index.html:28-37`, `db/schema.sql:11-39`) |
| **DP-02** — A finalidade do tratamento é compatível com a que justificou a divulgação, ou a nova finalidade é legítima e específica, com análise documentada? | `bases_legais` | `NAO_APLICAVEL` | Objeto inexistente: o sistema não usa dado obtido de fonte pública; todos os dados vêm do formulário de agendamento e do cadastro das clínicas (`public/index.html:28-37`, `db/schema.sql:11-39`) |
| **DP-03** — Há base legal documentada para o dado público (a dispensa do §4º é só do consentimento) e, para dado sensível, enquadramento no art. 11? | `bases_legais` | `NAO_APLICAVEL` | Objeto inexistente: o sistema não usa dado obtido de fonte pública; todos os dados vêm do formulário de agendamento e do cadastro das clínicas (`public/index.html:28-37`, `db/schema.sql:11-39`) |
| **DP-04** — Os dados públicos são minimizados e os direitos do titular (correção, oposição, eliminação quando cabível) seguem atendidos? | `bases_legais` | `NAO_APLICAVEL` | Objeto inexistente: o sistema não usa dado obtido de fonte pública; todos os dados vêm do formulário de agendamento e do cadastro das clínicas (`public/index.html:28-37`, `db/schema.sql:11-39`) |
| **CS-01** — O consentimento é fornecido por escrito ou por outro meio que demonstre a manifestação de vontade (opt-in explícito, sem checkbox pré-marcado)? | `bases_legais` | `NAO_APLICAVEL` | O sistema não coleta consentimento fora do banner de cookies, avaliado nos itens CK: o formulário de agendamento e o login não têm caixa de aceite, termo nem opt-in de comunicação (`public/index.html:28-37`, `src/auth.js:11-29`), e nenhum tratamento próprio depende só de consentimento. Nos dados dos pacientes, a base legal e um eventual consentimento são das clínicas |
| **CS-02** — Em contrato escrito, o consentimento consta de cláusula destacada das demais? | `bases_legais` | `NAO_APLICAVEL` | O sistema não coleta consentimento fora do banner de cookies, avaliado nos itens CK: o formulário de agendamento e o login não têm caixa de aceite, termo nem opt-in de comunicação (`public/index.html:28-37`, `src/auth.js:11-29`), e nenhum tratamento próprio depende só de consentimento. Nos dados dos pacientes, a base legal e um eventual consentimento são das clínicas |
| **CS-03** — Há registro que permita ao controlador provar a obtenção regular do consentimento? | `bases_legais` | `NAO_APLICAVEL` | O sistema não coleta consentimento fora do banner de cookies, avaliado nos itens CK: o formulário de agendamento e o login não têm caixa de aceite, termo nem opt-in de comunicação (`public/index.html:28-37`, `src/auth.js:11-29`), e nenhum tratamento próprio depende só de consentimento. Nos dados dos pacientes, a base legal e um eventual consentimento são das clínicas |
| **CS-04** — O consentimento se refere a finalidades determinadas, sem autorizações genéricas? | `bases_legais` | `NAO_APLICAVEL` | O sistema não coleta consentimento fora do banner de cookies, avaliado nos itens CK: o formulário de agendamento e o login não têm caixa de aceite, termo nem opt-in de comunicação (`public/index.html:28-37`, `src/auth.js:11-29`), e nenhum tratamento próprio depende só de consentimento. Nos dados dos pacientes, a base legal e um eventual consentimento são das clínicas |
| **CS-05** — A revogação é possível a qualquer momento, por procedimento gratuito e facilitado? | `bases_legais` | `NAO_APLICAVEL` | O sistema não coleta consentimento fora do banner de cookies, avaliado nos itens CK: o formulário de agendamento e o login não têm caixa de aceite, termo nem opt-in de comunicação (`public/index.html:28-37`, `src/auth.js:11-29`), e nenhum tratamento próprio depende só de consentimento. Nos dados dos pacientes, a base legal e um eventual consentimento são das clínicas |
| **CS-06** — Alterações de finalidade, forma, duração ou compartilhamento são informadas com destaque, permitindo revogar? | `bases_legais` | `NAO_APLICAVEL` | O sistema não coleta consentimento fora do banner de cookies, avaliado nos itens CK: o formulário de agendamento e o login não têm caixa de aceite, termo nem opt-in de comunicação (`public/index.html:28-37`, `src/auth.js:11-29`), e nenhum tratamento próprio depende só de consentimento. Nos dados dos pacientes, a base legal e um eventual consentimento são das clínicas |
| **CS-07** — Quando o tratamento é condição para o serviço, o titular é informado com destaque sobre isso e sobre como exercer seus direitos? | `bases_legais` | `NAO_APLICAVEL` | O sistema não coleta consentimento fora do banner de cookies, avaliado nos itens CK: o formulário de agendamento e o login não têm caixa de aceite, termo nem opt-in de comunicação (`public/index.html:28-37`, `src/auth.js:11-29`), e nenhum tratamento próprio depende só de consentimento. Nos dados dos pacientes, a base legal e um eventual consentimento são das clínicas |
| **CS-08** — O consentimento para dado sensível é específico e destacado, para finalidades específicas? | `bases_legais` | `NAO_APLICAVEL` | O sistema não coleta consentimento fora do banner de cookies, avaliado nos itens CK: o formulário de agendamento e o login não têm caixa de aceite, termo nem opt-in de comunicação (`public/index.html:28-37`, `src/auth.js:11-29`), e nenhum tratamento próprio depende só de consentimento. Nos dados dos pacientes, a base legal e um eventual consentimento são das clínicas; para o motivo da consulta, em regra a tutela da saúde (art. 11, II, "f") |
| **CA-01** — O tratamento de dados de crianças tem consentimento específico e em destaque de pelo menos um dos pais ou do responsável legal? | `bases_legais` | `NAO_APLICAVEL` | Obrigação do controlador no fluxo dos pacientes. Além disso, o agendamento recusa menores de 18 anos (`src/routes/agendamentos.js:23-27`) e as clínicas atendem só adultos (`README.md:15`) |
| **CA-02** — Há verificação de idade confiável, que não dependa só de autodeclaração, e esforço razoável para confirmar que o consentimento veio do responsável? | `bases_legais` | `NAO_APLICAVEL` | Obrigação do controlador no fluxo dos pacientes. Além disso, o agendamento recusa menores de 18 anos (`src/routes/agendamentos.js:23-27`) e as clínicas atendem só adultos (`README.md:15`) |
| **CA-03** — A coleta respeita a minimização, sem condicionar jogo, aplicação ou atividade ao fornecimento de dados além do necessário? | `bases_legais` | `NAO_APLICAVEL` | Obrigação do controlador no fluxo dos pacientes. Além disso, o agendamento recusa menores de 18 anos (`src/routes/agendamentos.js:23-27`) e as clínicas atendem só adultos (`README.md:15`) |
| **CA-04** — As informações sobre os dados coletados, o uso e o exercício de direitos estão públicas e acessíveis? | `bases_legais` | `NAO_APLICAVEL` | Obrigação do controlador no fluxo dos pacientes. Além disso, o agendamento recusa menores de 18 anos (`src/routes/agendamentos.js:23-27`) e as clínicas atendem só adultos (`README.md:15`) |
| **CK-08** — Os cookies classificados como estritamente necessários são de fato necessários (a categoria não mascara analytics ou publicidade)? | `bases_legais` | `NAO_APLICAVEL` | O item só se aplica quando há cookies classificados em categorias, e o banner não tem nenhuma (`public/index.html:41-45`); a falta de categorias é contada em CK-05. O único armazenamento feito sem depender do aceite é a própria escolha do visitante (`public/js/consent.js:3`, `:12`) |
| **SE-08** — Sessões de navegador têm proteção adequada (cookie de sessão com `HttpOnly`, `Secure` e `SameSite`, expiração e rotação)? | `seguranca` | `NAO_APLICAVEL` | Objeto inexistente: a aplicação não usa cookie de sessão; a autenticação é por token JWT no cabeçalho `Authorization` (`src/auth.js:31-36`), avaliado em AP-01 |
| **SE-09** — Há segregação de ambientes (produção, homologação, desenvolvimento) e de funções de quem acessa dados pessoais? | `seguranca` | `NAO_VERIFICADO` | Verificado: as funções são segregadas por papel (`api/index.js:40-41`, `db/schema.sql:16`) e as credenciais de cada ambiente vêm de variáveis (`src/db.js:4`, `.env.example:1-9`). Fora do alcance: se produção, preview e desenvolvimento têm banco e variáveis próprios, o que só aparece nos painéis. Acesso necessário: painéis da Vercel e do banco |
| **DS-04** — As imagens Docker passam por varredura de vulnerabilidades? | `seguranca` | `NAO_APLICAVEL` | Objeto inexistente: não há `Dockerfile` nem arquivo de composição no repositório; o deploy é feito pela Vercel a partir do código (`.github/workflows/ci.yml:26`) |
| **DS-05** — A infraestrutura como código (Terraform, CloudFormation, Helm etc.) passa por varredura de configuração? | `seguranca` | `NAO_APLICAVEL` | Objeto inexistente: nenhum arquivo de IaC no repositório. A única configuração de plataforma é o `vercel.json`, avaliado em IN-01 |
| **DS-06** — O ambiente Kubernetes segue controles de RBAC e hardening? | `seguranca` | `NAO_APLICAVEL` | Objeto inexistente: nenhum manifesto de orquestração; a aplicação roda em funções da Vercel (`vercel.json:1-7`) |
| **DS-10** — A branch de produção é protegida, com revisão obrigatória antes do deploy? | `seguranca` | `NAO_VERIFICADO` | A proteção da branch `main` e a revisão obrigatória são configurações do repositório no GitHub; o código só mostra que todo push na `main` vai para produção (`.github/workflows/ci.yml:20-26`). Acesso necessário: configurações do repositório no GitHub |
| **DS-11** — Ambientes de teste, homologação e CI usam dados sintéticos ou mascarados, sem cópia de dados pessoais reais de produção? | `seguranca` | `NAO_VERIFICADO` | Verificado: o CI não usa banco de dados (`.github/workflows/ci.yml:9-18`), o repositório não traz cópia de dados de produção e o `README.md:33` orienta o uso de dados fictícios. Fora do alcance: qual banco os deploys de preview usam, definido no painel. Acesso necessário: variáveis de ambiente por ambiente no painel da Vercel |
| **DT-08** — Há meio de pedir a revisão de decisões tomadas unicamente por tratamento automatizado, com informação sobre os critérios usados? | `direitos_titular` | `NAO_APLICAVEL` | Objeto inexistente: o sistema não toma decisão automatizada que defina perfil ou afete interesses do titular; não há pontuação, perfilamento nem recomendação (`src/routes/`, `db/schema.sql:1-39`) |
| **DT-09** — Correções, eliminações, anonimizações e bloqueios são comunicados aos agentes com quem os dados foram compartilhados? | `direitos_titular` | `NAO_APLICAVEL` | Objeto inexistente: os dados das contas não são compartilhados com outros controladores; hospedagem e banco tratam a mesma base, como operadores. O efeito da revogação sobre a Meta é avaliado em CK-03 |
| **GV-05** — A identidade e o contato do encarregado são divulgados publicamente, de forma clara e objetiva, preferencialmente no site? | `governanca` | `NAO_APLICAVEL` | Não há encarregado indicado cujo contato divulgar; a falta da indicação é contada em GV-02. O rodapé traz só o contato geral (`public/index.html:48`) |
| **GV-10** — O encarregado tem autonomia técnica, acesso à alta direção e ausência de conflito de interesses? | `governanca` | `NAO_APLICAVEL` | Não há encarregado indicado cuja autonomia avaliar; a falta da indicação é contada em GV-02 |
| **GV-11** — Agente de pequeno porte sem encarregado indicado: existe canal de comunicação com titulares e com a ANPD, divulgado? | `governanca` | `NAO_APLICAVEL` | O item vale para agente de pequeno porte dispensado de indicar encarregado. A dispensa não se aplica à AgendaFácil, que faz tratamento de alto risco (Res. CD/ANPD nº 2/2022, art. 3º); a falta do encarregado é contada em GV-02 |
| **GV-13** — O descarte de dados e mídias é seguro e registrado? | `governanca` | `NAO_APLICAVEL` | Não há eliminação em curso cujo descarte e registro avaliar: nada é eliminado hoje (falha contada em GV-12), e em PaaS não há mídia física sob controle da empresa (`vercel.json:1-7`) |
| **TI-03** — As CPC ou o mecanismo adotado cobrem os operadores e subprocessadores internacionais, inclusive os de segundo nível? | `governanca` | `NAO_APLICAVEL` | Depende de TI-02: o mecanismo de transferência não está evidenciado (os termos da Meta, da Vercel e do provedor do banco não foram reunidos), então não há mecanismo cuja cobertura de subprocessadores avaliar. A falha é contada em TI-02 |
| **IN-13** — A exportação de logs a ferramentas de terceiros está coberta por contrato de operador e, se os dados saírem do País, por mecanismo do art. 33? | `governanca` | `NAO_APLICAVEL` | Objeto inexistente: nenhuma integração envia logs a ferramenta de terceiros (`package.json:15-25`, `vercel.json:1-20`); os logs ficam na própria Vercel, cujo contrato e cuja transferência são contados em GV-09 e TI-02 |
| **IN-02** — Variáveis de ambiente e segredos ficam no cofre do provedor, fora do repositório e de builds ou previews públicos? | `infraestrutura` | `NAO_VERIFICADO` | Verificado: o `.gitignore` exclui o `.env` (`.gitignore:2-4`), o código lê os segredos de variáveis de ambiente (`src/auth.js:26`, `src/db.js:4`) e nenhuma credencial aparece nos arquivos do repositório. Fora do alcance: se as variáveis estão no cofre da Vercel e fora de builds e previews públicos. Acesso necessário: painel da Vercel |
| **IN-03** — Bancos de dados com dados pessoais têm criptografia em repouso, controle de acesso e segregação? | `infraestrutura` | `NAO_VERIFICADO` | Configuração visível só no painel do provedor do Postgres. O repositório mostra apenas a região e o TLS (`.env.example:5-6`, `src/db.js:5`). Acesso necessário: painel do provedor do banco. Backups e réplicas são avaliados em IN-10 |
| **IN-04** — Provedor de aplicações de internet: os registros de acesso (IP, porta lógica de origem, data e hora) são guardados por 6 meses e eliminados após o prazo, salvo requisição cautelar? | `infraestrutura` | `NAO_VERIFICADO` | A retenção e a exportação dos logs são configuradas no painel da Vercel, não no `vercel.json`. O código não mantém guarda própria. Acesso necessário: painel da Vercel |
| **IN-05** — As permissões de acesso ao provedor (IAM, membros do painel, tokens de deploy) seguem privilégio mínimo, com MFA? | `infraestrutura` | `NAO_VERIFICADO` | Membros, papéis e MFA só aparecem nos painéis. Acesso necessário: painéis da Vercel, do banco e do GitHub |
| **IN-06** — Analytics, logs de acesso e métricas nativos do provedor que coletam dados pessoais têm retenção, acesso e base legal definidos? | `infraestrutura` | `NAO_VERIFICADO` | Configuração do painel da Vercel. O código não inclui o script de analytics da plataforma (`public/index.html:1-56`). Acesso necessário: painel da Vercel |
| **IN-07** — Há firewall ou WAF, detecção de intrusão e monitoramento centralizado (SIEM ou equivalente) capazes de detectar acesso indevido a dados pessoais? | `infraestrutura` | `NAO_VERIFICADO` | Regras e alertas ficam no painel da Vercel. Acesso necessário: painel da Vercel |
| **IN-08** — Os serviços de armazenamento de objetos (buckets) e de arquivos enviados por usuários estão livres de exposição pública indevida? | `infraestrutura` | `NAO_APLICAVEL` | Objeto inexistente: nenhuma dependência nem uso de armazenamento de objetos (`package.json:15-25`); o sistema não recebe arquivos |
| **IN-09** — A segmentação de rede e as regras de exposição externa estão adequadas? | `infraestrutura` | `NAO_VERIFICADO` | Em PaaS não há rede gerida pelo cliente (`vercel.json:1-20`), mas as regras de exposição do banco gerenciado (lista de IPs, acesso público) ficam com a AgendaFácil e só aparecem no painel do provedor; o repositório mostra apenas o TLS (`src/db.js:5`). Acesso necessário: painel do provedor do banco |
| **IN-10** — Backups e réplicas são criptografados, têm acesso restrito e seguem a política de retenção (a eliminação também os alcança)? | `infraestrutura` | `NAO_VERIFICADO` | Criptografia, acesso e retenção dos backups e das réplicas são configurados no painel do provedor do Postgres; o repositório não os mostra. Acesso necessário: painel do provedor do banco |
| **IN-11** — Os logs de auditoria da conta cloud ou do painel estão ativos e protegidos contra alteração? | `infraestrutura` | `NAO_VERIFICADO` | Os registros de auditoria das contas (quem alterou configurações, variáveis e membros) ficam nos painéis. Acesso necessário: painéis da Vercel, do banco e do GitHub |
| **IN-12** — As ferramentas de logs e observabilidade além das nativas do provedor de hospedagem (CloudWatch, Datadog, Sentry, ELK etc.) têm retenção definida, acesso por privilégio mínimo e mascaramento de dados pessoais? | `infraestrutura` | `NAO_APLICAVEL` | Objeto inexistente: nenhuma ferramenta de observabilidade além dos logs nativos da Vercel (`package.json:15-25`), avaliados em IN-06; o mascaramento na origem é contado em SE-06 |
| **IN-14** — Chaves e segredos de produção ficam em serviço dedicado (KMS, Secrets Manager ou equivalente), com rotação? | `infraestrutura` | `NAO_VERIFICADO` | Os segredos estão no cofre de variáveis da Vercel e do GitHub (IN-02, DS-01), mas a rotação e o controle de acesso a eles só aparecem nos painéis. Acesso necessário: painéis da Vercel e do GitHub |

---

## 4. Não conformidades

Todos os 54 itens `NAO_CONFORME` ou `PARCIAL` do checklist estão detalhados abaixo, em ordem de severidade. **Nenhum achado teve severidade modulada**, porque há tratamento de alto risco (ver "Natureza e papel do agente de tratamento"). Os prazos seguem `IMEDIATO` (até 7 dias), `30_DIAS`, `90_DIAS` e `180_DIAS`.

### `CRITICO`

#### NC-01 · OP-02 — Operadora usa dados dos pacientes para publicidade própria

- **Problema:** a AgendaFácil trata os dados dos pacientes em nome das clínicas. Mesmo assim, instalou na página de agendamento um pixel de publicidade para as próprias campanhas. O pixel registra a visita à página de uma clínica específica e o evento de agendamento, e associa tudo a um identificador do navegador. Não há instrução nem autorização das clínicas para isso.
- **Severidade:** `CRITICO`. Pelo `legal/legal-bases-engine.md`, o operador que usa os dados para finalidade própria sem base legal é `ALTO`, e `CRITICO` quando há dado sensível. A visita e o agendamento em uma clínica revelam que a pessoa busca atendimento de saúde. O art. 11, §1º, aplica o regime dos dados sensíveis a qualquer tratamento que revele dado sensível e possa causar dano. Na dúvida entre os dois níveis, vale o mais alto (`core/severity-model.md`).
- **Fundamento LGPD:** art. 39 (tratamento segundo as instruções do controlador); art. 5º, VI e VII; art. 11, I e §1º; art. 42, §1º, I.
- **Evidência:** `AUSENTE (TECNICA + DOCUMENTAL)`, confiança `MEDIA`: o uso próprio está no código: `public/index.html:7-15` ("campanhas de aquisição"), `public/js/agendar.js:23` e `README.md:24`. Nenhuma instrução das clínicas documentada. Verificação que elevaria a confiança: captura de rede em produção e configuração do pixel no Gerenciador de Eventos da Meta.
- **Impacto técnico:** dados de navegação dos pacientes saem do controle das clínicas e da AgendaFácil e passam a alimentar perfis de publicidade.
- **Impacto jurídico:** ao decidir essa finalidade, a AgendaFácil deixa de ser só operadora e responde como controladora, sem base legal válida; responde também de forma solidária perante as clínicas.
- **Correção recomendada (esforço P):** remover o pixel da página de agendamento. Publicidade própria só no site institucional, depois do aceite. Se algum uso próprio de dados dos pacientes for mantido, ele precisa de autorização das clínicas no contrato (OP-01), base legal do art. 11 e RIPD (GV-03).
- **Responsável e prazo:** desenvolvedor líder (CTO), com decisão da sócia-fundadora (CEO) · `IMEDIATO`.

#### NC-02 · SE-03 — Rota pública permite consultar e alterar dados de pacientes

- **Problema:** a página de agendamento é pública. Quando alguém agenda com um CPF que já existe naquela clínica, o sistema troca o telefone e o e-mail do paciente pelos informados e devolve um código; com o código, a rota de confirmação entrega o cadastro que já existia. Basta saber o CPF de um paciente para descobrir o nome e a data de nascimento dele, confirmar que é paciente da clínica e passar a receber os contatos no lugar dele.
- **Severidade:** `CRITICO`. `ALTO` no catálogo; `CRITICO` pelo agravante do item: falha explorável com exfiltração de dados pessoais (`appsec/owasp-api.md`). O controle de acesso existe nas rotas autenticadas, mas a análise encontrou a violação que ele deveria impedir, então o item é `NAO_CONFORME` (`core/evidence-engine.md`). É também exposição explorável confirmada, nos termos de `core/severity-model.md`.
- **Fundamento LGPD:** art. 46; art. 6º, V (qualidade dos dados) e VII (segurança); art. 11, §1º (revela que a pessoa é paciente).
- **Evidência:** `PARCIAL (TECNICA)`, confiança `ALTA`: `src/routes/agendamentos.js:31-38` (atualização em caso de conflito) e `:51-61` (consulta pelo código); nas rotas autenticadas o controle funciona (`api/index.js:40-41`, `src/routes/clinica.js:13`, `:28`).
- **Impacto técnico:** dados de pacientes lidos e alterados sem autenticação; contatos sequestrados; o registro de novos agendamentos falsos polui a agenda das clínicas.
- **Impacto jurídico:** acesso não autorizado a dados pessoais que revelam condição de paciente: é o tipo de incidente que exige comunicação à ANPD e aos titulares (art. 48) e que as clínicas, como controladoras, teriam de comunicar.
- **Correção recomendada (esforço P):** na rota pública, não atualizar cadastro existente: criar o agendamento sem alterar o paciente e deixar a correção de contatos para a clínica, autenticada (`PATCH /api/clinica/pacientes/:id`). A confirmação deve devolver só data e horário (AP-02).
- **Responsável e prazo:** CTO · `IMEDIATO`.

### `ALTO`

#### NC-03 · CK-02 — Meta Pixel disparado antes do consentimento

- **Problema:** o pixel é carregado e envia `PageView` no `<head>` da página, antes de o banner aparecer. Quem clica em "Rejeitar" já foi rastreado.
- **Severidade:** `ALTO`. Mapeamento de `appsec/owasp-api.md`: pixels de publicidade de terceiros disparados antes do aceite, sem outra base legal documentada. É uma obrigação distinta da de OP-02: mesmo em uma página institucional, o rastreador não pode disparar antes da escolha.
- **Fundamento LGPD:** art. 7º, I; art. 8º; art. 6º, III (necessidade).
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `public/index.html:8-15`; `consent.js` só roda no fim da página (`public/index.html:53`).
- **Impacto técnico:** cookie `_fbp` gravado e dados enviados à Meta em toda visita.
- **Impacto jurídico:** tratamento sem base legal; consentimento posterior não convalida a coleta anterior.
- **Correção recomendada (esforço P):** carregar qualquer rastreador de forma dinâmica, só depois de "Aceitar" (ver `recomendacoes_tecnicas`).
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-04 · TI-02 — Dados enviados ao exterior sem mecanismo legal demonstrado

- **Problema:** a página de agendamento envia à Meta, nos EUA, identificadores do navegador (cookie `_fbp`, IP, user agent), a URL da clínica e o evento de agendamento. Os logs das funções, que hoje contêm CPF e e-mail (SE-06), ficam com a Vercel Inc., também nos EUA. Os termos desses provedores não foram localizados nem examinados.
- **Severidade:** `ALTO`. Os EUA não têm adequação reconhecida pela ANPD. Pelo `legal/international-transfer.md`, o mecanismo **não evidenciado** (termos não examinados) é `ALTO`, com evidência `AUSENTE`, até a verificação. A falta de informação ao titular é contada em TI-04. Se o exame dos termos comprovar que não há CPC nem outro mecanismo, o item passa a `CRITICO` (peso 4).
- **Fundamento LGPD:** arts. 33 a 36; Res. CD/ANPD nº 19/2024 (prazo das CPC encerrado em 23/08/2025).
- **Evidência:** `AUSENTE (TECNICA + DOCUMENTAL)`, confiança `BAIXA`: o fluxo está comprovado em `public/index.html:13-15` e `public/js/agendar.js:23`. O mecanismo não está: nenhum contrato, termo ou CPC em `docs/lgpd/`. Verificação que eleva a confiança: examinar os termos da Meta, da Vercel e do provedor do banco.
- **Impacto técnico:** dados ligados a agendamentos de saúde ficam sob controle de terceiros no exterior.
- **Impacto jurídico:** transferência internacional sem base demonstrada, tema prioritário de fiscalização da ANPD no biênio 2026-2027 (Res. CD/ANPD nº 30/2025); sujeita às sanções do art. 52.
- **Correção recomendada (esforço M):**
  1. Remover o pixel da página de agendamento, o que elimina o fluxo para a Meta (OP-02).
  2. Mapear as transferências que restarem (Vercel, provedor do banco, ferramentas futuras).
  3. Examinar os termos padrão aceitos; se incorporarem as CPC, arquivá-los como evidência; se não incorporarem, assiná-las.
- **Responsável e prazo:** CEO, com assessoria jurídica externa · `30_DIAS`.

#### NC-05 · SE-06 — CPF e e-mail gravados nos logs

- **Problema:** cada agendamento grava nome, CPF e e-mail do paciente no console, e cada login com falha grava o e-mail. Na Vercel, o console vira log da plataforma. Exemplo do que aparece hoje: `[agendamento] novo paciente nome=Paciente Exemplo cpf=123.456.789-09 email=paciente@exemplo.example clinica=fisio-exemplo`.
- **Severidade:** `ALTO`. Logs da aplicação com dados pessoais sem mascaramento (`appsec/owasp-api.md`).
- **Fundamento LGPD:** art. 46; art. 6º, III e VII.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `src/routes/agendamentos.js:29`; `src/auth.js:20`.
- **Impacto técnico:** os dados se espalham para um sistema sem controle de acesso fino nem retenção definida.
- **Impacto jurídico:** medida de segurança inadequada, exigível também do operador; agrava qualquer incidente.
- **Correção recomendada (esforço P):** registrar só IDs internos (`paciente_id`, `clinica`); para login, registrar o ID do usuário ou um hash do e-mail; expurgar os logs existentes no painel.
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-06 · AP-02 — API de confirmação devolve o cadastro completo do paciente

- **Problema:** a rota pública de confirmação devolve todas as colunas do agendamento e do paciente, incluindo CPF, telefone, e-mail, data de nascimento e motivo da consulta. A tela usa apenas data, horário e nome. Qualquer pessoa com o código (link repassado, histórico do navegador, ferramenta de suporte) obtém tudo.
- **Severidade:** `ALTO`. API com exposição excessiva de dados pessoais (`appsec/owasp-api.md`). Não há exploração confirmada; se houver, a falha se enquadra em "falha explorável com exfiltração" (`CRITICO`).
- **Fundamento LGPD:** art. 6º, III (necessidade); art. 46.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `src/routes/agendamentos.js:51-61`; uso parcial em `public/js/agendar.js:25-30`.
- **Impacto técnico:** dado de saúde exposto por um endpoint sem autenticação.
- **Impacto jurídico:** potencial incidente com dado sensível, que a AgendaFácil teria de avisar às clínicas.
- **Correção recomendada (esforço P):** selecionar só `a.data_hora` e o primeiro nome; nunca devolver `observacoes`, CPF ou contato em rota pública.
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-07 · AP-01 — Token de login sem expiração

- **Problema:** os tokens JWT são emitidos sem validade, algoritmo fixo nem audiência. Um token vazado dá acesso permanente à agenda da clínica, inclusive aos motivos de consulta.
- **Severidade:** `ALTO`. Falha de autenticação sem exploração confirmada (`appsec/owasp-api.md`).
- **Fundamento LGPD:** art. 46; art. 6º, VII.
- **Evidência:** `PARCIAL (TECNICA)`, confiança `ALTA`: `src/auth.js:24-27` (emissão); `src/auth.js:36` (verificação sem `algorithms`).
- **Impacto técnico:** não há como encerrar sessões nem limitar o uso de um token roubado, a não ser trocando o segredo de todos.
- **Impacto jurídico:** medida de segurança inadequada para dados sensíveis.
- **Correção recomendada (esforço P):** `expiresIn: '8h'`, `algorithm: 'HS256'` e `audience` na emissão; `algorithms` e `audience` na verificação; em seguida, avaliar token de renovação com revogação.
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-08 · IN-01 — `vercel.json` anula a CSP definida no código

- **Problema:** o Express define uma CSP restritiva, mas as páginas estáticas, entre elas a que coleta CPF e dados de saúde, são servidas pela CDN da Vercel sem passar pelo Express. O único CSP que recebem é o do `vercel.json`, que permite scripts de qualquer origem, `unsafe-inline` e `unsafe-eval`, e não restringe o enquadramento da página. Para as respostas da API, qual cabeçalho prevalece depende da plataforma.
- **Severidade:** `ALTO`. Hospedagem que remove ou enfraquece cabeçalhos de segurança configurados no código (`cloud/cloud-audit.md`). Pela contagem única, a falha é reprovada só aqui; SE-02 a cita.
- **Fundamento LGPD:** art. 46; art. 6º, VII e VIII.
- **Evidência:** `PARCIAL (TECNICA)`, confiança `MEDIA`: `vercel.json:12-15` contra `api/index.js:22-34`. Respostas de produção não coletadas; `curl -I` na página e na API elevaria a confiança.
- **Impacto técnico:** um XSS ou script de terceiro comprometido conseguiria ler o formulário de agendamento; a página pode ser embutida por outros sites (clickjacking).
- **Impacto jurídico:** medida técnica de segurança neutralizada pela configuração da hospedagem.
- **Correção recomendada (esforço P):** substituir o valor no `vercel.json` pela mesma política do código (`default-src 'self'; script-src 'self'; connect-src 'self'; frame-ancestors 'none'`), acrescentar `Strict-Transport-Security` e conferir com `curl -I`. A política restritiva só funciona depois de retirar o pixel inline (OP-02).
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-09 · OP-01 — Sem contrato com as clínicas controladoras

- **Problema:** não há termos de uso nem contrato que estabeleça que a clínica é controladora dos dados dos pacientes e que a AgendaFácil trata esses dados por instrução dela. O rascunho da política apresenta a AgendaFácil como responsável por tudo.
- **Severidade:** `ALTO`. Ausência de contrato com o controlador (`legal/legal-bases-engine.md`, seção "Papel do auditado").
- **Fundamento LGPD:** art. 5º, VI e VII; art. 39; art. 42, §1º, I.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: `README.md:16`; nenhum termo em `public/` nem em `docs/lgpd/`; declaração da fundadora; `docs/lgpd/politica-de-privacidade.md:9`.
- **Impacto técnico:** não há instruções formais sobre retenção, eliminação, suboperadores e atendimento a pedidos.
- **Impacto jurídico:** sem instruções documentadas, a AgendaFácil pode ser tratada como controladora dos dados de saúde e responde solidariamente por danos.
- **Correção recomendada (esforço M):** termos de uso com cláusulas de operador: objeto, instruções, confidencialidade, segurança, lista de suboperadores, aviso de incidentes, apoio a pedidos de titulares e ao RIPD da clínica, devolução e eliminação ao fim do contrato. Pode partir de `templates/dpa-template.md`.
- **Responsável e prazo:** CEO e assessoria jurídica · `30_DIAS`.

#### NC-10 · OP-03 — Suboperadores não informados às clínicas

- **Problema:** a Vercel processa as requisições com o motivo da consulta, e o provedor do banco armazena esses dados. As clínicas não são informadas de que esses suboperadores existem.
- **Severidade:** `ALTO`. Suboperador não informado é `MEDIO`, e `ALTO` quando trata dado sensível (`legal/legal-bases-engine.md`). Os contratos com os provedores são contados em GV-09.
- **Fundamento LGPD:** art. 39.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: `README.md:22-23` identifica os provedores; não há contrato nem lista de suboperadores entregue às clínicas (OP-01).
- **Impacto técnico:** as clínicas não sabem por onde passam os dados dos pacientes.
- **Impacto jurídico:** a AgendaFácil não consegue demonstrar às clínicas as garantias que deve oferecer como operadora.
- **Correção recomendada (esforço P):** listar os suboperadores nos termos com as clínicas (OP-01) e avisá-las antes de trocar de provedor.
- **Responsável e prazo:** CEO · `30_DIAS`.

#### NC-11 · OP-04 — Sem processo de aviso de incidentes às clínicas

- **Problema:** não há procedimento, responsáveis nem modelo de aviso para incidentes de segurança. Nos dados dos pacientes, a AgendaFácil precisa avisar as clínicas sem demora, para que elas comuniquem a ANPD e os titulares. A comunicação dos dados próprios é contada em GV-08.
- **Severidade:** `ALTO`. Ausência de processo de aviso de incidente ao controlador (`legal/legal-bases-engine.md`). O dever não é modulado por porte.
- **Fundamento LGPD:** art. 39; art. 48; Res. CD/ANPD nº 15/2024 (comunicação em 3 dias úteis, complementável em 20 dias úteis).
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum plano ou runbook no repositório; declaração da fundadora.
- **Impacto técnico:** reação improvisada, perda de evidências e contenção lenta.
- **Impacto jurídico:** as clínicas perderiam o prazo de comunicação por falta de aviso; incidentes são tema prioritário de fiscalização (Res. CD/ANPD nº 30/2025).
- **Correção recomendada (esforço M):** adotar `templates/incident-response-template.md`, definir quem decide e quem avisa, e fixar no contrato o prazo de aviso às clínicas (por exemplo, 24 horas).
- **Responsável e prazo:** CEO e CTO · `30_DIAS`.

#### NC-12 · SE-07 — Sem trilha de auditoria de acessos a dados de pacientes

- **Problema:** não há registro de qual usuário consultou a agenda ou alterou dados de qual paciente.
- **Severidade:** `ALTO`. Ausência de trilha de auditoria (`cloud/cloud-audit.md`), agravada por envolver dados de saúde.
- **Fundamento LGPD:** art. 46; art. 6º, X; art. 37.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `api/index.js:38-41`; `src/routes/clinica.js:8-33`.
- **Impacto técnico:** acesso indevido por funcionário de clínica ou token vazado passa despercebido.
- **Impacto jurídico:** sem trilha, não se consegue avaliar a extensão de um incidente para avisar as clínicas no prazo.
- **Correção recomendada (esforço M):** middleware que registre usuário, clínica, rota, ID do paciente e horário, sem dados pessoais, em armazenamento com retenção definida.
- **Responsável e prazo:** CTO · `30_DIAS`.

#### NC-13 · DS-02 — Sem varredura de dependências e sem nenhuma outra varredura no CI

- **Problema:** o pipeline não verifica vulnerabilidades em dependências, e não há nenhuma outra varredura de segurança.
- **Severidade:** `ALTO`. `MEDIO` no catálogo; `ALTO` pelo agravante do item: o pipeline não tem nenhuma varredura de segurança (`devsecops/ci-cd-security.md`). A análise estática é contada em DS-07.
- **Fundamento LGPD:** art. 46; art. 49.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `MEDIA`: `.github/workflows/ci.yml:16-18`; nenhum `dependabot.yml` no repositório. As configurações de segurança do GitHub não foram vistas.
- **Impacto técnico:** vulnerabilidade conhecida em `express`, `jsonwebtoken` ou `pg` chega à produção sem alerta.
- **Impacto jurídico:** sistemas devem atender a requisitos de segurança desde a concepção (art. 49).
- **Correção recomendada (esforço P):** `npm audit --audit-level=high` no job `build` e Dependabot semanal.
- **Responsável e prazo:** CTO · `30_DIAS`.

#### NC-14 · DT-01 — Sem canal para exercício de direitos nos tratamentos próprios

- **Problema:** nos tratamentos em que é controladora (contas dos usuários das clínicas e rastreamento), a AgendaFácil não informa os direitos nem como exercê-los. O único contato é um e-mail comercial genérico.
- **Severidade:** `ALTO`. Ausência de canal para exercício de direitos (`legal/rights-of-data-subject.md`).
- **Fundamento LGPD:** arts. 18 e 19; art. 9º, VII.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: `docs/lgpd/politica-de-privacidade.md:36`; `public/index.html:48`.
- **Impacto técnico:** pedidos chegam por canais não monitorados e se perdem.
- **Impacto jurídico:** descumprimento dos arts. 18 e 19. O canal dos pacientes é obrigação das clínicas, mas um pedido que chegue à AgendaFácil precisa ser encaminhado a elas (OP-05).
- **Correção recomendada (esforço P):** endereço ou formulário específico de privacidade no aviso e no rodapé, com prazo de resposta (imediato em formato simplificado ou até 15 dias, art. 19).
- **Responsável e prazo:** CEO · `30_DIAS`.

#### NC-15 · DT-03 — Aviso de privacidade não publicado

- **Problema:** o rodapé e o banner de cookies apontam para `/privacidade`, mas não existe página nesse endereço. O único texto é um rascunho dentro do repositório.
- **Severidade:** `ALTO`. Ausência de política de privacidade (`legal/rights-of-data-subject.md`): para quem acessa o site, ela não existe. O conteúdo do rascunho é avaliado em DT-04.
- **Fundamento LGPD:** art. 9º, caput (acesso facilitado e ostensivo).
- **Evidência:** `PARCIAL (TECNICA + DOCUMENTAL)`, confiança `MEDIA`: `public/index.html:49`; nenhuma página em `public/`, que é a pasta publicada (`vercel.json:4`); rascunho em `docs/lgpd/politica-de-privacidade.md`. Produção não consultada.
- **Impacto técnico:** link quebrado no rodapé.
- **Impacto jurídico:** o consentimento de cookies é pedido sem que o titular tenha acesso às informações do tratamento.
- **Correção recomendada (esforço P):** publicar o aviso revisado (DT-04) em `public/privacidade.html` e testar o link em produção.
- **Responsável e prazo:** CTO · `30_DIAS`.

#### NC-16 · GV-01 — Sem registro das operações de tratamento

- **Problema:** não existe inventário com finalidade, papel, base legal, categorias de titulares, compartilhamentos, retenção e medidas de segurança. O operador também deve manter o registro das operações que realiza.
- **Severidade:** `ALTO`. Ausência de registro com tratamento de dados sensíveis (`governance/dpo-framework.md`).
- **Fundamento LGPD:** art. 37.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: `docs/lgpd/` contém só o rascunho da política; `README.md:27-29` lista dados, sem os demais elementos; declaração da fundadora.
- **Impacto técnico:** sem mapa de dados, não há como garantir eliminação, responder a pedidos nem dimensionar incidentes.
- **Impacto jurídico:** obrigação legal descumprida. Por haver alto risco, a forma simplificada da Res. CD/ANPD nº 2/2022 não está disponível (art. 3º).
- **Correção recomendada (esforço M):** registro versionado em `docs/lgpd/`, separando o que a AgendaFácil trata como operadora (pacientes) do que trata como controladora (contas, logs, rastreamento).
- **Responsável e prazo:** CEO, com o encarregado · `30_DIAS`.

#### NC-17 · GV-02 — Encarregado não indicado

- **Problema:** não há encarregado indicado nem contato divulgado.
- **Severidade:** `ALTO`. Pelo `governance/dpo-framework.md`, a falta de encarregado quando ele é exigível é `ALTO`. Para o operador a indicação é facultativa, mas a AgendaFácil também é controladora (contas e rastreamento), e a dispensa do pequeno porte não vale para quem faz tratamento de alto risco (Res. CD/ANPD nº 2/2022, art. 3º).
- **Fundamento LGPD:** art. 41; Res. CD/ANPD nº 18/2024.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: `docs/lgpd/politica-de-privacidade.md:36`; `public/index.html:47-51`.
- **Impacto técnico:** nenhum direto.
- **Impacto jurídico:** falta o canal formal com titulares e ANPD.
- **Correção recomendada (esforço P):** indicar encarregado por ato escrito, datado e assinado (pode ser pessoa jurídica, como um serviço de DPO externo) e divulgar o contato no site.
- **Responsável e prazo:** CEO · `30_DIAS`.

#### NC-18 · GV-03 — Sem RIPD para o uso próprio de dados da página de agendamento (risco aceito)

- **Problema:** como controladora do rastreamento para fins próprios, a AgendaFácil faz um tratamento de alto risco (revela busca por atendimento de saúde, em escala relevante) sem relatório de impacto. O RIPD dos dados de saúde inseridos no agendamento é das clínicas.
- **Severidade:** `ALTO`. Ausência de RIPD em tratamento de alto risco pelos critérios da Res. CD/ANPD nº 2/2022 (`governance/dpo-framework.md`).
- **Fundamento LGPD:** art. 38; art. 5º, XVII.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum RIPD em `docs/lgpd/`; declaração da fundadora.
- **Impacto técnico:** os riscos do rastreamento não foram analisados.
- **Impacto jurídico:** se a ANPD solicitar o RIPD, a AgendaFácil não terá como apresentá-lo.
- **Correção recomendada (esforço G):** encerrar o tratamento, removendo o pixel da página de agendamento (OP-02). Encerrado o uso próprio, o item deixa de ser aplicável. Se algum uso próprio for mantido, elaborar o RIPD com `templates/ripd-template.md`.
- **Aceite de risco:**
  - `accepted_by`: Ana Exemplo, sócia-administradora e CEO (pessoa fictícia);
  - `accepted_at`: 2026-10-03;
  - `justification`: o pixel será removido da página de agendamento em até 7 dias (ação 1), o que encerra o tratamento. Elaborar um RIPD, com esforço de mais de uma semana, para um tratamento em extinção não se justifica para uma equipe de 3 pessoas. Se em 90 dias ainda houver qualquer uso próprio de dados da página de agendamento, o RIPD será elaborado;
  - `deadline_suggestion`: `30_DIAS` (mantido);
  - `accepted_deadline`: `90_DIAS`;
  - `review_at`: 2026-12-31.
  - O aceite **não** altera status, severidade nem score: o item segue `NAO_CONFORME`, `ALTO`, com valor 0 e peso 3.
- **Responsável e prazo:** CEO, com o encarregado · `30_DIAS` (adiado pelo aceite para `90_DIAS`).

#### NC-19 · GV-06 — Sem canal de denúncia de provedor de aplicações

- **Problema:** não há canal permanente de denúncia, exigido de todo provedor de aplicações de internet desde 20/07/2026. O rodapé traz só um e-mail de contato geral.
- **Severidade:** `ALTO`. Ausência de canal de denúncia permanente: `ALTO` no catálogo (`GV-06`, `governance/dpo-framework.md`). Um e-mail geral não é o controle exigido, então o item é `NAO_CONFORME`.
- **Fundamento LGPD:** decreto nº 8.771/2016, art. 16-A, II (redação do Decreto nº 12.975/2026). Correlato LGPD: art. 6º, VI (transparência).
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `public/index.html:48`.
- **Impacto técnico:** nenhum, além da criação de um canal.
- **Impacto jurídico:** descumprimento de dever geral fiscalizado pela ANPD (Decreto nº 8.771/2016, art. 19-A).
- **Correção recomendada (esforço P):** página "Fale conosco sobre privacidade e denúncias" com formulário ou e-mail monitorado, que preveja expressamente a notificação de conteúdo ilícito.
- **Responsável e prazo:** CEO · `30_DIAS`.

#### NC-20 · BL-02 — Base legal dos tratamentos próprios não documentada

- **Problema:** a AgendaFácil é controladora dos dados das contas dos usuários das clínicas, mas nenhum documento diz qual base legal sustenta esse tratamento.
- **Severidade:** `ALTO`. Nenhuma base legal indicada (`legal/legal-bases-engine.md`): pela régua de status de `core/evidence-engine.md`, o controle não existe e o item é `NAO_CONFORME`, com a `criticality` do catálogo. O agravante de dado sensível não se aplica, porque o objeto do item são dados cadastrais das contas. A falta do contrato em si é contada em OP-01.
- **Fundamento LGPD:** art. 7º; art. 6º, X.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: nenhum documento nomeia a base: `docs/lgpd/politica-de-privacidade.md:22-26`; declaração da fundadora. A relação contratual só aparece de forma indireta (`README.md:16`; `db/schema.sql:11-18`).
- **Impacto técnico:** nenhum direto.
- **Impacto jurídico:** base legal não demonstrável numa fiscalização.
- **Correção recomendada (esforço P):** indicar a base de cada tratamento próprio no registro das operações (GV-01) e no aviso de privacidade (DT-04).
- **Responsável e prazo:** CEO e assessoria jurídica · `30_DIAS`.

#### NC-21 · SE-04 — Login sem segundo fator nem política de senha

- **Problema:** o acesso ao painel, que mostra dados de saúde dos pacientes, depende só de e-mail e senha. Não há segundo fator nem regra mínima para a senha.
- **Severidade:** `ALTO`. Dos elementos que restam no item (política de senha e segundo fator), nenhum está atendido; com menos da metade, o item é `NAO_CONFORME` (`core/evidence-engine.md`) e o achado tem a `criticality` do catálogo. A falta de limitação de tentativas é contada em AP-03 e sai da conta.
- **Fundamento LGPD:** art. 46.
- **Evidência:** `PARCIAL (TECNICA)`, confiança `ALTA`: `src/auth.js:11-29` (login só com e-mail e senha); `src/auth.js:7-9` (gera o hash, sem validar a senha); não há rota de criação ou troca de senha.
- **Impacto técnico:** senhas fracas ou reutilizadas dão acesso à agenda.
- **Impacto jurídico:** medida de segurança aquém do adequado para dado sensível.
- **Correção recomendada (esforço M):** segundo fator (TOTP) para usuários de clínica e de administração e política de senha (tamanho mínimo e bloqueio de senhas vazadas).
- **Responsável e prazo:** CTO · `30_DIAS`.

#### NC-22 · TI-04 — Transferência internacional não informada ao titular

- **Problema:** o rascunho do aviso de privacidade não diz que dados de navegação vão para a Meta e que os logs ficam com a Vercel, ambas nos EUA.
- **Severidade:** `ALTO`. Transferência sem informação ao titular (`legal/international-transfer.md`). É obrigação distinta da de TI-02: mesmo com mecanismo válido, o titular precisa ser informado.
- **Fundamento LGPD:** art. 9º, V; art. 33.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: `docs/lgpd/politica-de-privacidade.md:22-36` não menciona transferência nem destinatários.
- **Impacto técnico:** nenhum direto.
- **Impacto jurídico:** falta de transparência sobre o envio de dados ao exterior, tema prioritário de fiscalização (Res. CD/ANPD nº 30/2025).
- **Correção recomendada (esforço P):** informar no aviso os destinos, os provedores e o mecanismo adotado; nos dados dos pacientes, informar as clínicas.
- **Responsável e prazo:** CEO e assessoria jurídica · `30_DIAS`.

#### NC-23 · TI-05 — Dado que revela busca por atendimento de saúde enviado ao exterior sem proteção

- **Problema:** o pixel envia à Meta, nos EUA, a visita e o agendamento na página de uma clínica, o que revela que a pessoa procura atendimento de saúde (art. 11, §1º). Não há hipótese do art. 11 nem medida de proteção para esse envio.
- **Severidade:** `ALTO`. Dado sensível transferido sem hipótese do art. 11 nem proteção reforçada (`TI-05`). O banco, com o motivo da consulta, fica no Brasil; o problema está no pixel.
- **Fundamento LGPD:** arts. 11, 33 e 46.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `MEDIA`: `public/index.html:13-15` e `public/js/agendar.js:23` (mesma evidência de OP-02); `.env.example:5-6` e `vercel.json:3` mostram o banco e as funções em São Paulo.
- **Impacto técnico:** informação sensível fora do controle das clínicas e da AgendaFácil.
- **Impacto jurídico:** tratamento de dado sensível sem hipótese legal, agravado pela saída do País.
- **Correção recomendada (esforço P):** remover o pixel da página de agendamento (OP-02); com isso o item deixa de ter objeto.
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-24 · GV-08 — Sem processo de comunicação de incidentes nos dados próprios

- **Problema:** nos dados em que a AgendaFácil é controladora (contas das clínicas e rastreamento), cabe a ela comunicar a ANPD e os titulares em até 3 dias úteis. Não há procedimento, responsáveis nem modelo para isso.
- **Severidade:** `ALTO`. Ausência de processo capaz de comunicar em 3 dias úteis (`governance/dpo-framework.md`). O dever não é modulado por porte. É obrigação distinta do aviso às clínicas (OP-04), embora o mesmo documento resolva as duas.
- **Fundamento LGPD:** art. 48; Res. CD/ANPD nº 15/2024.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum plano ou runbook no repositório; declaração da fundadora.
- **Impacto técnico:** reação improvisada, perda de evidências e contenção lenta.
- **Impacto jurídico:** perder o prazo de comunicação sujeita a empresa a processo sancionador (art. 52).
- **Correção recomendada (esforço M):** no mesmo documento de OP-04, definir quem avalia o risco, quem comunica a ANPD e os titulares e em que prazo.
- **Responsável e prazo:** CEO e CTO · `30_DIAS`.

#### NC-25 · GV-09 — Operadores sem contrato de proteção de dados demonstrado

- **Problema:** a Vercel processa as requisições com o motivo da consulta, e o provedor do banco armazena esses dados. Não foram localizados contratos de proteção de dados (DPA) com eles.
- **Severidade:** `ALTO`. Operador sem DPA é `MEDIO`, e `ALTO` quando trata dado sensível (`governance/dpo-framework.md`).
- **Fundamento LGPD:** art. 39; art. 46.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `BAIXA`: nenhum DPA em `docs/lgpd/`; os termos padrão aceitos no cadastro não foram examinados. Verificação que eleva a confiança: reunir os DPAs e os termos da Vercel e do provedor do banco.
- **Impacto técnico:** não há garantia contratual de segurança, aviso de incidentes nem eliminação ao fim do serviço.
- **Impacto jurídico:** a AgendaFácil não consegue demonstrar as garantias dos seus operadores. É uma obrigação distinta do mecanismo de transferência internacional (TI-02), embora os dois costumem estar no mesmo instrumento.
- **Correção recomendada (esforço P):** baixar e arquivar os DPAs que os provedores oferecem e verificar a cobertura de CPC (TI-02).
- **Responsável e prazo:** CEO · `30_DIAS`.

#### NC-26 · DS-08 — Sem varredura de segredos no repositório

- **Problema:** nada verifica se uma senha, token ou chave foi parar no código ou no histórico do git.
- **Severidade:** `ALTO`. Ausência de varredura de segredos (`devsecops/ci-cd-security.md`). Nenhuma credencial foi encontrada nos arquivos atuais, então não vale o agravante de credencial exposta.
- **Fundamento LGPD:** art. 46.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `MEDIA`: `.github/workflows/ci.yml:9-30` não tem etapa de varredura de segredos; `.gitignore:2-4` exclui o `.env`. A proteção nativa do GitHub contra segredos não foi vista.
- **Impacto técnico:** um segredo enviado por engano fica no histórico sem que ninguém seja avisado.
- **Impacto jurídico:** medida de segurança básica ausente num sistema com dados de saúde.
- **Correção recomendada (esforço P):** ligar a proteção contra segredos do GitHub e rodar uma varredura do histórico (por exemplo, gitleaks) no CI.
- **Responsável e prazo:** CTO · `30_DIAS`.

### `MEDIO`

#### NC-27 · CK-03 — Revogação que não apaga o identificador da Meta

- **Problema:** o usuário consegue rever a escolha, e a recusa chama `fbq('consent', 'revoke')`, o que interrompe os eventos seguintes. Mas o cookie `_fbp` e o script já carregado permanecem no navegador.
- **Severidade:** `MEDIO`. O item é `PARCIAL` (`criticality` `ALTO`), então o achado fica um nível abaixo: `MEDIO` (`core/auditor-core.md`). O mecanismo de revogação existe e funciona, e falta a limpeza do identificador já gravado. O disparo do `PageView` antes da escolha, e antes de a escolha salva ser reaplicada, é a falha de CK-02 e não é contado de novo aqui.
- **Fundamento LGPD:** art. 8º, §5º; art. 18, IX.
- **Evidência:** `PARCIAL (TECNICA)`, confiança `ALTA`: `public/js/consent.js:6-9` e `:26-29`; `public/index.html:50`.
- **Impacto técnico:** o identificador persistente da Meta segue disponível após a revogação.
- **Impacto jurídico:** revogação incompleta.
- **Correção recomendada (esforço P):** na revogação, apagar o cookie `_fbp` e não recarregar o pixel.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-28 · CK-04 — Escolha de cookies sem prova

- **Problema:** a escolha fica apenas no navegador, sem versão do banner nem categorias.
- **Severidade:** `MEDIO`. Dos três elementos do registro (data, versão do banner e categorias), só a data é gravada, e apenas no navegador; com menos da metade, o item é `NAO_CONFORME` (`core/evidence-engine.md`).
- **Fundamento LGPD:** art. 8º, §2º.
- **Evidência:** `PARCIAL (TECNICA)`, confiança `ALTA`: `public/js/consent.js:12`.
- **Impacto técnico:** limpar o navegador apaga a prova.
- **Impacto jurídico:** o ônus de provar o consentimento é do controlador.
- **Correção recomendada (esforço M):** registrar no servidor um identificador aleatório, data, versão do banner e categorias aceitas.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-29 · CK-05 — Consentimento de cookies sem categorias

- **Problema:** o banner oferece só "Aceitar" ou "Rejeitar" tudo, sem separar finalidades.
- **Severidade:** `MEDIO`. Consentimento pouco granular (`appsec/owasp-api.md`).
- **Fundamento LGPD:** art. 8º, §4º.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `public/index.html:41-45`.
- **Impacto técnico:** não há como aceitar medição e recusar publicidade.
- **Impacto jurídico:** autorização genérica é nula (art. 8º, §4º).
- **Correção recomendada (esforço M):** categorias separadas (necessários, medição, publicidade), sem pré-marcação.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-30 · DT-02 — Sem fluxo para atender pedidos nos tratamentos próprios

- **Problema:** não há procedimento escrito, com prazo, responsável e confirmação, para atender pedidos sobre os dados de uma conta de usuário de clínica. A falta de recurso no sistema é contada em DT-06.
- **Severidade:** `MEDIO`. Resposta sem prazo definido, em desacordo com o art. 19 (`legal/rights-of-data-subject.md`).
- **Fundamento LGPD:** art. 18, §§3º a 5º; art. 19.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum procedimento em `docs/lgpd/`; declaração da fundadora.
- **Impacto técnico:** cada pedido é tratado de improviso.
- **Impacto jurídico:** risco de descumprir o prazo do art. 19.
- **Correção recomendada (esforço P):** procedimento de uma página (quem recebe, como executa, prazo, registro), suficiente para o volume atual.
- **Responsável e prazo:** CEO · `90_DIAS`.

#### NC-31 · DT-04 — Aviso de privacidade incompleto e com papéis trocados

- **Problema:** o rascunho identifica a empresa e menciona cookies de forma genérica. Faltam o tratamento das contas das clínicas, a Meta como destinatária, base legal, retenção, direitos e encarregado. Além disso, o texto fala aos pacientes como se a AgendaFácil fosse a controladora dos dados do agendamento.
- **Severidade:** `MEDIO`. O rascunho atende dois dos oito elementos que o item enumera; com menos da metade, o item é `NAO_CONFORME` (`core/evidence-engine.md`) e o achado tem a `criticality` do catálogo.
- **Fundamento LGPD:** art. 9º; art. 6º, I (finalidade específica).
- **Evidência:** `PARCIAL (DOCUMENTAL)`, confiança `ALTA`: `docs/lgpd/politica-de-privacidade.md:3-36`.
- **Impacto técnico:** nenhum direto.
- **Impacto jurídico:** consentimento obtido sem informação prévia transparente é nulo (art. 9º, §1º); assumir por escrito o papel de controladora dos dados dos pacientes amplia a responsabilidade da AgendaFácil.
- **Correção recomendada (esforço M):** reescrever com `templates/privacy-policy-template.md`: tratar das contas e dos cookies e explicar que, nos agendamentos, a controladora é a clínica.
- **Responsável e prazo:** CEO e assessoria jurídica · `30_DIAS`.

#### NC-32 · GV-04 — Sem política de retenção dos dados próprios

- **Problema:** não há prazo definido para manter contas de usuários das clínicas e logs, nem fundamento do art. 16 para o que é conservado. Os prazos dos dados dos pacientes são definidos pelas clínicas e entram no contrato (OP-01) e na rotina de expurgo (OP-06).
- **Severidade:** `MEDIO`. Retenção sem prazo definido (`governance/dpo-framework.md`).
- **Fundamento LGPD:** arts. 15 e 16.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nada em `docs/lgpd/`; declaração da fundadora.
- **Impacto técnico:** acúmulo indefinido de contas inativas e de logs.
- **Impacto jurídico:** conservação além da finalidade viola os arts. 15 e 16.
- **Correção recomendada (esforço P):** prazos por categoria. Exemplos:
  - contas: até o fim do contrato, mais o prazo legal;
  - logs de aplicação: 90 dias;
  - registros de acesso: 6 meses (MCI, art. 15; ver IN-04).
- **Responsável e prazo:** CEO · `90_DIAS`.

#### NC-33 · OP-06 — Sem devolução ou eliminação dos dados ao fim do contrato

- **Problema:** o sistema não tem rotina para devolver ou eliminar os dados de uma clínica que encerra o contrato, nem para expurgar registros nos prazos que a clínica definir.
- **Severidade:** `MEDIO`. O módulo não traz regra própria para este item; por analogia com a retenção sem prazo definido (`governance/dpo-framework.md`), `MEDIO`.
- **Fundamento LGPD:** arts. 15 e 16; art. 39.
- **Evidência:** `AUSENTE (TECNICA + DOCUMENTAL)`, confiança `MEDIA`: `db/schema.sql:20-39`; nenhuma rotina no código nem agendamento no `vercel.json` ou no CI; nenhum procedimento escrito.
- **Impacto técnico:** a base só cresce, e com ela o impacto de um vazamento.
- **Impacto jurídico:** conservação de dados de saúde sem instrução do controlador.
- **Correção recomendada (esforço M):** exportação em lote por clínica e job agendado que elimine ou anonimize registros vencidos, gravando o que foi feito e alcançando os backups conforme a política do provedor.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-34 · AP-03 — APIs sem limitação de taxa

- **Problema:** login e agendamento público aceitam requisições ilimitadas, o que também deixa o login sem proteção contra força bruta.
- **Severidade:** `MEDIO`. Ausência parcial de hardening (`appsec/owasp-api.md`). Item mais específico para essa falha; SE-04 o cita.
- **Fundamento LGPD:** art. 46.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `MEDIA`: `api/index.js:36-41`; `package.json:15-22`. As regras do firewall da plataforma não foram vistas.
- **Impacto técnico:** força bruta de senhas e criação massiva de agendamentos falsos.
- **Impacto jurídico:** medida de segurança insuficiente.
- **Correção recomendada (esforço P):** `express-rate-limit` em `/api/login` e `POST /api/agendamentos`, ou o firewall da plataforma.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-35 · TI-01 — Envios de dados ao exterior não mapeados

- **Problema:** nenhum documento lista para onde os dados saem do País, por qual provedor e para quê. Os destinos só aparecem no código e na fala da fundadora.
- **Severidade:** `MEDIO`. Fluxo internacional não mapeado (`TI-01`, `legal/international-transfer.md`).
- **Fundamento LGPD:** arts. 33 e 37.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nada em `docs/lgpd/`; `public/index.html:13-15` (Meta) e `README.md:22` (Vercel) são as únicas pistas; declaração da fundadora.
- **Impacto técnico:** novos envios podem surgir sem que ninguém perceba.
- **Impacto jurídico:** sem o mapa, não há como escolher nem demonstrar o mecanismo de cada transferência.
- **Correção recomendada (esforço P):** incluir no registro das operações (GV-01) uma tabela de destinos, provedores, dados e mecanismo do art. 33.
- **Responsável e prazo:** CEO, com o encarregado · `30_DIAS`.

#### NC-36 · DT-06 — Sistema sem recurso para corrigir, exportar ou excluir contas

- **Problema:** não há rota nem tela para consultar, corrigir, exportar ou excluir os dados de uma conta de usuário de clínica. Qualquer pedido depende de alteração manual no banco.
- **Severidade:** `MEDIO`. Inexistência de fluxo de exclusão e portabilidade (`legal/rights-of-data-subject.md`).
- **Fundamento LGPD:** art. 18, III a VI.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `src/routes/clinica.js:1-55` e `api/index.js:38-41` não têm rota de conta.
- **Impacto técnico:** alterações manuais, sem registro e sujeitas a erro.
- **Impacto jurídico:** direitos de correção, eliminação e portabilidade sem meio de execução.
- **Correção recomendada (esforço M):** rotas autenticadas para ver, corrigir, exportar e excluir a própria conta; exclusão com confirmação.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-37 · DT-07 — Titular não tem como saber com quem os dados são compartilhados

- **Problema:** nenhum documento ou tela informa que a Meta recebe dados de navegação nem que a Vercel e o provedor do banco tratam os dados das contas.
- **Severidade:** `MEDIO`. Informação sobre uso compartilhado ausente (`legal/rights-of-data-subject.md`).
- **Fundamento LGPD:** art. 18, VII; art. 9º, V.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: `docs/lgpd/politica-de-privacidade.md:36` (pendência registrada no próprio rascunho); `public/index.html:42`.
- **Impacto técnico:** nenhum direto.
- **Impacto jurídico:** direito de informação sobre uso compartilhado não atendido.
- **Correção recomendada (esforço P):** listar destinatários e finalidades no aviso de privacidade e responder a esse pedido pelo canal de direitos (DT-01).
- **Responsável e prazo:** CEO e assessoria jurídica · `30_DIAS`.

#### NC-38 · DT-10 — Pedidos de titulares sem registro

- **Problema:** não existe registro dos pedidos recebidos, das respostas e da confirmação de execução.
- **Severidade:** `MEDIO`. Trilha de atendimento ausente (`legal/rights-of-data-subject.md`).
- **Fundamento LGPD:** art. 6º, X; art. 18.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nada em `docs/lgpd/`; declaração da fundadora.
- **Impacto técnico:** impossível provar que um pedido foi atendido e quando.
- **Impacto jurídico:** sem prova de atendimento numa reclamação à ANPD.
- **Correção recomendada (esforço P):** planilha ou sistema de chamados com data, tipo de pedido, resposta e data de execução.
- **Responsável e prazo:** CEO · `90_DIAS`.

#### NC-39 · GV-12 — Dados próprios nunca são eliminados

- **Problema:** não há rotina que elimine contas inativas e logs ao fim de um prazo, nem rota de exclusão. A eliminação dos dados dos pacientes é contada em OP-06.
- **Severidade:** `MEDIO`. Eliminação não automática ao fim do prazo (`governance/dpo-framework.md`).
- **Fundamento LGPD:** arts. 15 e 16.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: nenhuma rotina de expurgo no código (`package.json:7-11`, `src/`); `db/schema.sql:11-18` não tem campo de desativação nem de exclusão.
- **Impacto técnico:** acúmulo indefinido de dados.
- **Impacto jurídico:** conservação além da finalidade.
- **Correção recomendada (esforço M):** depois de definir os prazos (GV-04), agendar o expurgo e incluir backups e provedores.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-40 · GV-14 — Retenções legais não identificadas

- **Problema:** nenhum documento identifica o que precisa ser guardado por lei e por quanto tempo, como os registros de acesso do MCI (6 meses) e os documentos fiscais.
- **Severidade:** `MEDIO`. Retenção sem fundamento identificado no art. 16 (`governance/dpo-framework.md`).
- **Fundamento LGPD:** art. 16, I; MCI, art. 15.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nada em `docs/lgpd/`; declaração da fundadora.
- **Impacto técnico:** risco de apagar o que a lei manda guardar ou de guardar além do prazo.
- **Impacto jurídico:** conservação sem hipótese do art. 16 demonstrada.
- **Correção recomendada (esforço P):** listar as retenções legais na política de retenção (GV-04), com o prazo e a norma de cada uma.
- **Responsável e prazo:** CEO · `90_DIAS`.

#### NC-41 · GV-15 — Sem histórico das decisões de privacidade

- **Problema:** a pasta `docs/lgpd/` tem só um rascunho de política. Não há versões anteriores, atas nem registro de quem decidiu o quê.
- **Severidade:** `MEDIO`. Falha de prestação de contas de materialidade média (`governance/dpo-framework.md`).
- **Fundamento LGPD:** art. 6º, X; art. 50.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: `docs/lgpd/` contém um único arquivo; declaração da fundadora.
- **Impacto técnico:** nenhum direto.
- **Impacto jurídico:** a empresa não consegue demonstrar as medidas que adota.
- **Correção recomendada (esforço P):** manter os documentos de privacidade versionados no repositório e registrar as decisões (por exemplo, a remoção do pixel).
- **Responsável e prazo:** CEO, com o encarregado · `90_DIAS`.

#### NC-42 · GV-16 — Sem política de segurança da informação

- **Problema:** não há documento que defina regras de acesso, senhas, uso de dados de produção e resposta a falhas.
- **Severidade:** `MEDIO`. Política de segurança ausente (`governance/dpo-framework.md`).
- **Fundamento LGPD:** arts. 46 e 50.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nada em `docs/`; declaração da fundadora.
- **Impacto técnico:** as práticas dependem da memória de cada pessoa.
- **Impacto jurídico:** faltam as medidas administrativas que o art. 46 pede ao lado das técnicas.
- **Correção recomendada (esforço M):** política curta, de uma ou duas páginas, proporcional a uma equipe de três pessoas.
- **Responsável e prazo:** CEO e CTO · `90_DIAS`.

#### NC-43 · CK-06 — Banner de cookies sem informação clara

- **Problema:** o banner aparece e funciona, mas diz apenas que os cookies servem para "melhorar sua experiência". Não informa a finalidade real (publicidade) nem o terceiro que recebe os dados (Meta).
- **Severidade:** `MEDIO`. Dos três elementos (banner funcional, informação sobre finalidades e informação sobre terceiros), só o primeiro está atendido; com menos da metade, o item é `NAO_CONFORME` (`core/evidence-engine.md`).
- **Fundamento LGPD:** art. 8º; art. 9º, I e V.
- **Evidência:** `PARCIAL (TECNICA)`, confiança `ALTA`: `public/index.html:41-45`.
- **Impacto técnico:** nenhum direto.
- **Impacto jurídico:** consentimento sem informação prévia adequada é nulo (art. 9º, §1º).
- **Correção recomendada (esforço P):** texto que nomeie as finalidades e os terceiros, com link para a política de cookies.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-44 · CK-07 — Pixel e identificadores sem inventário nem política de cookies

- **Problema:** não há política de cookies nem lista dos rastreadores usados. O rascunho da política diz só que o site usa cookies.
- **Severidade:** `MEDIO`. Inventário e política de cookies ausentes (`appsec/owasp-api.md`).
- **Fundamento LGPD:** art. 9º; art. 37.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: `docs/lgpd/politica-de-privacidade.md:28-30`; nenhum outro documento em `docs/lgpd/`.
- **Impacto técnico:** novos rastreadores entram sem controle.
- **Impacto jurídico:** transparência insuficiente sobre identificadores de terceiros.
- **Correção recomendada (esforço P):** política de cookies com `templates/cookie-policy-template.md`, listando cada cookie ou SDK, finalidade e prazo.
- **Responsável e prazo:** CEO e CTO · `30_DIAS`.

#### NC-45 · AP-05 — APIs públicas sem inventário

- **Problema:** as rotas abertas à internet (`/api/agendamentos` e `/api/login`) não estão listadas em documento algum, com os dados que cada uma expõe.
- **Severidade:** `MEDIO`. Inventário de APIs públicas ausente (`appsec/owasp-api.md`).
- **Fundamento LGPD:** arts. 37 e 46.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: `api/index.js:38-41` é a única fonte; nada em `README.md` nem em `docs/`.
- **Impacto técnico:** rotas e campos expostos crescem sem revisão, como ocorreu em AP-02.
- **Impacto jurídico:** dificulta demonstrar quais dados saem do sistema.
- **Correção recomendada (esforço P):** tabela com rota, autenticação, dados recebidos e devolvidos e responsável, revisada a cada mudança.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-46 · DS-07 — Sem análise estática nem dinâmica de segurança

- **Problema:** o pipeline roda lint e testes, mas nenhuma análise de segurança do código (SAST) nem da aplicação em execução (DAST).
- **Severidade:** `MEDIO`. Cobertura parcial de varredura (`devsecops/ci-cd-security.md`).
- **Fundamento LGPD:** art. 46; art. 49.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `MEDIA`: `.github/workflows/ci.yml:16-18`; nenhum fluxo de CodeQL no repositório. As configurações de segurança do GitHub não foram vistas.
- **Impacto técnico:** falhas como a de AP-02 passam sem alerta.
- **Impacto jurídico:** sistemas devem atender a requisitos de segurança desde a concepção (art. 49).
- **Correção recomendada (esforço P):** codeQL (ou equivalente) no CI; DAST básico antes de mudanças grandes.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-47 · DS-09 — Pipeline com permissões padrão e actions sem versão fixa

- **Problema:** o workflow não declara `permissions`, então o token roda com as permissões padrão do repositório. As actions usam a tag `v4`, que pode ser movida, e o deploy baixa a CLI da Vercel sem versão.
- **Severidade:** `MEDIO`. Permissões e versões do pipeline (`devsecops/ci-cd-security.md`).
- **Fundamento LGPD:** art. 46.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `.github/workflows/ci.yml:12-13` e `:25-26`; nenhum bloco `permissions`.
- **Impacto técnico:** uma action ou pacote comprometido roda com acesso aos segredos de deploy.
- **Impacto jurídico:** risco de cadeia de suprimentos num sistema com dados de saúde.
- **Correção recomendada (esforço P):** declarar `permissions: contents: read`, fixar as actions pelo hash do commit e a CLI por versão.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-48 · IN-16 — Runtime fora de suporte fixado no projeto

- **Problema:** o projeto está preso ao Node.js 20, linha que deixou de receber correções de segurança em abril de 2026, e não tem rotina para atualizar o runtime.
- **Severidade:** `MEDIO`. Falha pontual de hardening (`cloud/cloud-audit.md`). Em PaaS, a versão do runtime é escolha do cliente, não do provedor.
- **Fundamento LGPD:** art. 46.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `MEDIA`: `.github/workflows/ci.yml:15`; `package.json:12-14`; `README.md:20`. A versão efetiva em produção depende do painel da Vercel, não conferido.
- **Impacto técnico:** vulnerabilidades do runtime deixam de ser corrigidas.
- **Impacto jurídico:** medida de segurança básica ausente num sistema com dados de saúde.
- **Correção recomendada (esforço P):** migrar para uma linha do Node.js com suporte, fixá-la no CI e no `package.json` e rever a versão a cada ciclo de suporte.
- **Responsável e prazo:** CTO · `90_DIAS`.

### `BAIXO`

#### NC-49 · OP-05 — Apoio incompleto às clínicas nos pedidos dos pacientes

- **Problema:** a clínica consegue corrigir dados cadastrais, mas não há como gerar cópia, exportar ou eliminar o cadastro de um paciente.
- **Severidade:** `BAIXO`. O item é `PARCIAL` (`criticality` `MEDIO`), então o achado fica um nível abaixo: `BAIXO` (`core/auditor-core.md`). A correção de dados pela clínica existe, e faltam a exportação e a eliminação por paciente.
- **Fundamento LGPD:** art. 39; art. 18, II, V e VI.
- **Evidência:** `PARCIAL (TECNICA)`, confiança `ALTA`: `src/routes/clinica.js:21-33`.
- **Impacto técnico:** cada pedido exige uma consulta manual no banco pela equipe da AgendaFácil.
- **Impacto jurídico:** a clínica pode perder o prazo do art. 19 por depender da operadora.
- **Correção recomendada (esforço M):** rotas autenticadas para a clínica exportar (JSON ou CSV) e eliminar ou anonimizar um paciente, com registro da execução.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-50 · DS-03 — Sem SBOM

- **Problema:** não há inventário das dependências gerado a cada build.
- **Severidade:** `BAIXO`. Melhoria com baixo risco imediato.
- **Fundamento LGPD:** art. 46; art. 6º, X.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `.github/workflows/ci.yml:9-30`.
- **Impacto técnico:** diante de uma vulnerabilidade nova, leva mais tempo saber se o projeto é afetado.
- **Impacto jurídico:** baixo; reforça a prestação de contas.
- **Correção recomendada (esforço P):** gerar SBOM CycloneDX no CI e guardá-lo como artefato.
- **Responsável e prazo:** CTO · `180_DIAS`.

#### NC-51 · SE-10 — Validação de entrada incompleta no agendamento

- **Problema:** o agendamento confere se os campos obrigatórios vieram e limita o tamanho do corpo, mas não valida o formato de CPF, e-mail, telefone e datas.
- **Severidade:** `BAIXO`. O item é `PARCIAL` (`criticality` `MEDIO`), então o achado fica um nível abaixo: `BAIXO` (`core/auditor-core.md`). A presença dos campos e o tamanho do corpo são conferidos, e falta a validação de formato.
- **Fundamento LGPD:** art. 46; art. 6º, V.
- **Evidência:** `PARCIAL (TECNICA)`, confiança `ALTA`: `src/routes/agendamentos.js:20-22`; `api/index.js:36`; a saída usa `textContent` (`public/js/agendar.js:28`).
- **Impacto técnico:** dados inválidos entram no cadastro das clínicas.
- **Impacto jurídico:** afeta a qualidade dos dados (art. 6º, V).
- **Correção recomendada (esforço P):** validar formato e tamanho de cada campo no servidor.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-52 · GV-17 — Equipe sem treinamento de privacidade

- **Problema:** não há registro de orientação ou treinamento dos três sócios sobre proteção de dados.
- **Severidade:** `BAIXO`. Treinamento ausente (`governance/dpo-framework.md`).
- **Fundamento LGPD:** art. 41, §2º, III; art. 50.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nada em `docs/`; declaração da fundadora.
- **Impacto técnico:** erros como o do pixel e o dos logs tendem a se repetir.
- **Impacto jurídico:** boa prática de governança não demonstrada.
- **Correção recomendada (esforço P):** uma sessão anual, registrada, sobre o papel de operadora, logs e incidentes.
- **Responsável e prazo:** encarregado · `180_DIAS`.

#### NC-53 · IN-15 — Divisão de responsabilidades com os provedores não documentada

- **Problema:** nenhum documento diz o que cabe à Vercel e ao provedor do banco e o que cabe à AgendaFácil (certificados, backups, atualizações, cabeçalhos).
- **Severidade:** `BAIXO`. Falha documental de baixa materialidade (`cloud/cloud-audit.md`).
- **Fundamento LGPD:** arts. 46 e 50.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nada em `docs/` nem no `README.md:18-25`; declaração da fundadora.
- **Impacto técnico:** lacunas como a CSP do `vercel.json` (IN-01) passam despercebidas.
- **Impacto jurídico:** dificulta demonstrar quem responde por cada medida de segurança.
- **Correção recomendada (esforço P):** quadro de uma página com as responsabilidades de cada parte.
- **Responsável e prazo:** CTO · `180_DIAS`.

#### NC-54 · DT-05 — Política sem indicação de versão

- **Problema:** o rascunho da política traz a data de atualização, mas não um número de versão nem o histórico das mudanças.
- **Severidade:** `BAIXO`. O item é `PARCIAL` (`criticality` `BAIXO`), então o achado fica um nível abaixo: `BAIXO` (`core/auditor-core.md`). Dois dos três elementos estão atendidos (linguagem simples e data); falta a versão.
- **Fundamento LGPD:** art. 6º, VI; art. 9º.
- **Evidência:** `PARCIAL (DOCUMENTAL)`, confiança `MEDIA`: `docs/lgpd/politica-de-privacidade.md:3`.
- **Impacto técnico:** nenhum direto.
- **Impacto jurídico:** sem versão, não dá para demonstrar qual texto valia quando um titular foi informado.
- **Correção recomendada (esforço P):** numerar as versões e manter o histórico ao publicar o aviso.
- **Responsável e prazo:** CEO e assessoria jurídica · `180_DIAS`.

---

## 5. Itens obrigatórios ausentes

Requisitos sem nenhuma evidência (`AUSENTE`) que a LGPD, a ANPD ou o MCI exigem de forma direta da AgendaFácil:

| Requisito | Norma | Item |
|---|---|---|
| Contrato com as clínicas controladoras | LGPD, art. 39 | OP-01 |
| Contratos com os suboperadores e sua indicação às clínicas | LGPD, art. 39 | OP-03, GV-09 |
| Tratamento limitado às instruções do controlador | LGPD, art. 39 | OP-02 |
| Processo de incidentes, com aviso às clínicas | LGPD, arts. 39 e 48; Res. CD/ANPD nº 15/2024 | OP-04, GV-08 |
| Rotina de devolução ou eliminação ao fim do contrato | LGPD, arts. 15 e 16 | OP-06 |
| Registro das operações de tratamento (forma completa) | LGPD, art. 37; Res. CD/ANPD nº 2/2022, art. 3º | GV-01 |
| Encarregado indicado e contato divulgado | LGPD, art. 41; Res. CD/ANPD nº 18/2024 | GV-02 |
| RIPD do tratamento de alto risco próprio (risco aceito até 2026-12-31) | LGPD, arts. 5º, XVII e 38 | GV-03 |
| Política de retenção dos dados próprios | LGPD, arts. 15 e 16 | GV-04 |
| Mecanismo de transferência internacional (não evidenciado) e informação ao titular | LGPD, arts. 33 e 9º; Res. CD/ANPD nº 19/2024 | TI-02, TI-04 |
| Canal de exercício de direitos e fluxo de atendimento nos tratamentos próprios | LGPD, arts. 18 e 19 | DT-01, DT-02, DT-10 |
| Aviso de privacidade publicado | LGPD, art. 9º | DT-03 |
| Canal de denúncia de provedor de aplicações | Decreto nº 8.771/2016, art. 16-A, II | GV-06 |
| Bloqueio de rastreamento antes do consentimento | LGPD, arts. 7º, I e 8º | CK-02 |
| Mascaramento de dados pessoais em logs | LGPD, art. 46 | SE-06 |
| Mapa dos envios de dados ao exterior | LGPD, arts. 33 e 37 | TI-01 |
| Política de cookies com inventário dos rastreadores | LGPD, arts. 9º e 37 | CK-07 |
| Política de segurança da informação | LGPD, arts. 46 e 50 | GV-16 |
| Retenções legais identificadas e histórico das decisões de privacidade | LGPD, arts. 6º, X e 16, I | GV-14, GV-15 |

A guarda dos registros de acesso por 6 meses (MCI, art. 15) não está nesta lista porque não pôde ser verificada (IN-04).

---

## 6. Riscos identificados

### Técnicos

- Consulta e alteração de dados de pacientes sem autenticação pela rota pública de agendamento, a partir do CPF (SE-03).
- Exposição de CPF, contato e motivo da consulta pela API pública de confirmação (AP-02).
- Tokens de login sem validade: um vazamento dá acesso permanente (AP-01).
- Dados pessoais espalhados nos logs da plataforma (SE-06).
- Página de coleta sem CSP efetiva, vulnerável a XSS e clickjacking (IN-01).
- Dependências vulneráveis sem detecção (DS-02, DS-03).
- Acesso indevido sem rastro (SE-07); contas protegidas só por senha e sem limite de tentativas (SE-04, AP-03).
- Treze controles ainda não verificados (SE-09, DS-10, DS-11, IN-02, IN-03, IN-04, IN-05, IN-06, IN-07, IN-09, IN-10, IN-11, IN-14): a proteção real do banco, dos backups, dos painéis, dos logs, dos segredos e dos ambientes é desconhecida.
- Runtime Node.js 20 fora de suporte desde abril de 2026 (IN-16).
- Pipeline sem varredura de segredos, com permissões padrão e actions sem versão fixa (DS-08, DS-09).

### Jurídicos

- Uso de dados dos pacientes para publicidade própria: a AgendaFácil sai do papel de operadora, passa a responder como controladora sem base legal e responde solidariamente perante as clínicas, art. 42, §1º, I (OP-02).
- Operadora de dados de saúde sem contrato com os controladores nem com os suboperadores (OP-01, OP-03).
- Transferência internacional sem mecanismo do art. 33 demonstrado, tema prioritário de fiscalização. Pode subir a `CRITICO` se o exame dos termos comprovar ausência de CPC (TI-02).
- Rastreamento sem consentimento válido (CK-02, CK-03, CK-05).
- Obrigações documentais básicas ausentes, agravadas pela perda das dispensas do pequeno porte: registro completo, encarregado, processo de incidentes, retenção, canal de direitos, aviso de privacidade e canal de denúncia (seção 5).
- Exposição às sanções do art. 52 da LGPD (advertência; multa de até 2% do faturamento, limitada a R$ 50 milhões por infração; publicização; bloqueio e eliminação dos dados), com dosimetria pela Res. CD/ANPD nº 4/2023. Some-se a isso o MCI (art. 12) para os deveres de provedor de aplicações.

### Operacionais

- Equipe de 3 pessoas sem processo de incidentes: um vazamento pararia o produto e deixaria as clínicas sem aviso dentro do prazo (OP-04).
- Pedidos de pacientes atendidos à mão, a pedido das clínicas, sem rotina de exportação ou eliminação (OP-05, OP-06).
- Base de dados crescendo sem limite (OP-06, GV-04).
- Clínicas mais estruturadas devem exigir contrato de operador e evidências de segurança na contratação; sem eles, vendas travam (OP-01, OP-03).
- Contas e logs nunca eliminados, sem prazos nem retenções legais definidas (GV-12, GV-14).

### Reputacionais

- Pixel de publicidade em página de agendamento de saúde é o tipo de caso que costuma virar notícia e afastar clínicas e pacientes (OP-02, CK-02, TI-02).
- Um vazamento de motivos de consulta atinge a confiança das clínicas, que respondem perante seus pacientes e conselhos profissionais (AP-02, SE-06).

### Riscos aceitos

| Item | Severidade | Aceito por | Data do aceite | Justificativa | Prazo sugerido | Prazo aceito | Revisão |
|---|---|---|---|---|---|---|---|
| GV-03 — Sem RIPD para o uso próprio de dados da página de agendamento (risco aceito) | `ALTO` | Ana Exemplo, sócia-administradora e CEO (pessoa fictícia) | 2026-10-03 | o pixel será removido da página de agendamento em até 7 dias (ação 1), o que encerra o tratamento. Elaborar um RIPD, com esforço de mais de uma semana, para um tratamento em extinção não se justifica para uma equipe de 3 pessoas. Se em 90 dias ainda houver qualquer uso próprio de dados da página de agendamento, o RIPD será elaborado | `30_DIAS` | `90_DIAS` | 2026-12-31 |

O aceite fica registrado para prestação de contas. O item continua pontuando como `NAO_CONFORME` e deve ser reavaliado na data de revisão.

---

## 7. Plano de adequação

Esforço: `P` até 1 dia; `M` até 1 semana; `G` mais de 1 semana. `IMEDIATO` significa até 7 dias. `IMEDIATO` e `30_DIAS` ficam no curto prazo, `90_DIAS` no médio e `180_DIAS` no longo.

### Curto prazo (0-30 dias)

| # | Ação | Itens | Responsável sugerido | Esforço | Prazo |
|---|---|---|---|---|---|
| 1 | Remover o Meta Pixel da página de agendamento; se mantido no site institucional, carregar só após o aceite e apagar `_fbp` na revogação | OP-02, CK-02, CK-03, TI-02, TI-05 | CTO | P | `IMEDIATO` |
| 2 | Retirar CPF, nome e e-mail dos logs e expurgar os logs existentes | SE-06 | CTO | P | `IMEDIATO` |
| 3 | Parar de atualizar cadastro existente pela rota pública de agendamento e reduzir a resposta da confirmação a data e horário | SE-03, AP-02 | CTO | P | `IMEDIATO` |
| 4 | Expiração, algoritmo e audiência no JWT | AP-01 | CTO | P | `IMEDIATO` |
| 5 | Corrigir a CSP e acrescentar HSTS no `vercel.json`; conferir com `curl -I` | IN-01 | CTO | P | `IMEDIATO` |
| 6 | Fazer as verificações pendentes nos painéis da Vercel, do banco e do GitHub e guardar as evidências | SE-09, DS-10, DS-11, IN-02, IN-03, IN-04, IN-05, IN-06, IN-07, IN-09, IN-10, IN-11, IN-14, DS-02, DS-07, DS-08, AP-03 | CTO | P | `30_DIAS` |
| 7 | Termos de uso com cláusulas de operador para as clínicas, com a lista de suboperadores | OP-01, OP-03 | CEO + jurídico | M | `30_DIAS` |
| 8 | Reunir e arquivar os DPAs da Vercel e do provedor do banco; examinar os termos e incorporar CPC onde faltarem | GV-09, TI-02 | CEO + jurídico | M | `30_DIAS` |
| 9 | Processo de incidentes, com prazo de aviso às clínicas e comunicação à ANPD e aos titulares nos dados próprios | OP-04, GV-08 | CEO + CTO | M | `30_DIAS` |
| 10 | Indicar encarregado (interno ou serviço externo) | GV-02 | CEO | P | `30_DIAS` |
| 11 | Reescrever e publicar o aviso de privacidade dos tratamentos próprios e a política de cookies, com destinatários, transferência internacional, canal de direitos e canal de denúncia | DT-01, DT-03, DT-04, DT-07, TI-04, CK-07, BL-02, GV-06, DT-05 | CEO + jurídico; publicação pelo CTO | M | `30_DIAS` |
| 12 | Registro das operações de tratamento, na forma completa, separando os papéis e com o mapa dos envios ao exterior | GV-01, TI-01, BL-02 | CEO + encarregado | M | `30_DIAS` |
| 13 | `npm audit`, Dependabot, análise estática e varredura de segredos no CI | DS-02, DS-07, DS-08 | CTO | P | `30_DIAS` |
| 14 | Trilha de auditoria de acessos a dados de pacientes | SE-07 | CTO | M | `30_DIAS` |
| 15 | MFA e limitação de tentativas no login e nas rotas públicas | SE-04, AP-03 | CTO | M | `30_DIAS` |

### Médio prazo (30-90 dias)

| # | Ação | Itens | Responsável sugerido | Esforço | Prazo |
|---|---|---|---|---|---|
| 16 | Confirmar que não resta uso próprio de dados da página de agendamento; se restar, elaborar o RIPD (prazo sugerido `30_DIAS`, adiado pelo aceite de risco) | GV-03 | CEO + encarregado | P (G, se o RIPD for necessário) | `90_DIAS` |
| 17 | Rotas de exportação e eliminação por paciente, para uso das clínicas | OP-05 | CTO | M | `90_DIAS` |
| 18 | Devolução em lote e expurgo automático conforme os prazos das clínicas; expurgo de contas e logs próprios | OP-06, GV-12 | CTO | M | `90_DIAS` |
| 19 | Política de retenção dos dados próprios, com as retenções legais, e procedimento de atendimento a pedidos, com registro de cada um | GV-04, GV-14, DT-02, DT-10 | CEO | P | `90_DIAS` |
| 20 | Banner com categorias, texto que nomeie finalidades e terceiros e registro das escolhas no servidor | CK-04, CK-05, CK-06 | CTO | M | `90_DIAS` |
| 21 | Corrigir o que as verificações pendentes revelarem (por exemplo, exportar os registros de acesso para guarda de 6 meses) | SE-09, DS-10, DS-11, IN-02, IN-03, IN-04, IN-05, IN-06, IN-07, IN-09, IN-10, IN-11, IN-14 | CTO | M | `90_DIAS` |
| 22 | Rotas para ver, corrigir, exportar e excluir a conta do usuário da clínica | DT-06 | CTO | M | `90_DIAS` |
| 23 | Política de segurança da informação e pasta versionada com as decisões de privacidade | GV-15, GV-16 | CEO + CTO | M | `90_DIAS` |
| 24 | Validar o formato dos campos do agendamento; inventário das rotas públicas | SE-10, AP-05 | CTO | P | `90_DIAS` |
| 25 | Declarar `permissions` mínimas no workflow e fixar actions e CLI por versão | DS-09 | CTO | P | `90_DIAS` |
| 26 | Migrar para uma linha do Node.js com suporte e definir a rotina de atualização do runtime | IN-16 | CTO | P | `90_DIAS` |

### Longo prazo (90-180 dias)

| # | Ação | Itens | Responsável sugerido | Esforço | Prazo |
|---|---|---|---|---|---|
| 27 | Gerar SBOM a cada build | DS-03 | CTO | P | `180_DIAS` |
| 28 | Revisar o aceite de risco do RIPD e repetir esta auditoria (`/lgpd-saas`), agora com acesso aos painéis, para medir a evolução | GV-03 e todos | CEO + encarregado | P | `180_DIAS` |
| 29 | Revisão semestral do aviso, dos contratos e do registro; treinamento básico de privacidade para a equipe, com registro; quadro de responsabilidades com os provedores; orientação às clínicas sobre o aviso delas na página de agendamento | DT-04, GV-01, OP-01, GV-17, IN-15 | Encarregado | M | `180_DIAS` |

---

## 8. Recomendações técnicas

**Logs sem dados pessoais** (`src/routes/agendamentos.js:29`, `src/auth.js:20`):

```js
console.log(`[agendamento] criado paciente_id=${paciente.rows[0].id} clinica=${clinica}`);
console.warn('[login] falha de autenticação', { usuarioEncontrado: Boolean(usuario) });
```

**JWT com validade, algoritmo e audiência** (`src/auth.js:24-27` e `:36`):

```js
const OPCOES = { algorithm: 'HS256', expiresIn: '8h', audience: 'agendafacil-painel' };
const token = jwt.sign({ sub: usuario.id, clinica: usuario.clinica_id, papel: usuario.papel },
  process.env.JWT_SECRET, OPCOES);

req.usuario = jwt.verify(token, process.env.JWT_SECRET, {
  algorithms: ['HS256'], audience: 'agendafacil-painel',
});
```

**Confirmação com o mínimo necessário** (`src/routes/agendamentos.js:53`):

```sql
SELECT a.data_hora, split_part(p.nome, ' ', 1) AS primeiro_nome
  FROM agendamentos a JOIN pacientes p ON p.id = a.paciente_id
 WHERE a.codigo = $1
```

**Pixel fora da página de agendamento.** Remover o bloco `public/index.html:7-16` e a chamada de `public/js/agendar.js:23`. Em páginas institucionais, carregar o script a partir de `aplicar('aceito')` em `consent.js`, por um arquivo próprio (não inline), para manter a CSP restritiva. Na revogação, apagar o cookie `_fbp` (`document.cookie = '_fbp=; Max-Age=0; path=/'`, com o domínio usado pelo pixel).

**CSP coerente entre código e hospedagem** (`vercel.json:12-15`):

```json
{ "key": "Content-Security-Policy",
  "value": "default-src 'self'; script-src 'self'; connect-src 'self'; frame-ancestors 'none'" },
{ "key": "Strict-Transport-Security", "value": "max-age=31536000; includeSubDomains" }
```

Validar em produção: `curl -sI https://<domínio>/ | grep -i -E 'content-security|strict-transport'` e o mesmo para `/api/agendamentos/<código-de-teste>`.

**Varreduras no CI** (`.github/workflows/ci.yml`, job `build`):

```yaml
      - run: npm audit --audit-level=high
      - run: npx @cyclonedx/cyclonedx-npm --output-file sbom.json
```

Acrescentar `.github/dependabot.yml` (ecossistema `npm`, frequência semanal) e, se possível, CodeQL.

**Limitação de taxa:** `express-rate-limit` com janela de 15 minutos em `/api/login` (ex.: 10 tentativas) e em `POST /api/agendamentos` (ex.: 20 por IP).

**Trilha de auditoria:** middleware nas rotas `/api/clinica` e `/api/admin` que registre `usuario`, `clinica`, `metodo`, `rota`, `paciente_id` e horário em tabela própria, com retenção definida na política (GV-04).

**Apoio às clínicas e fim de contrato:** rotas `GET /api/clinica/pacientes/:id/exportar` e `DELETE /api/clinica/pacientes/:id`, restritas à clínica do token; rotina administrativa de exportação em lote por clínica; job agendado que execute, conforme os prazos instruídos pelas clínicas, `DELETE` ou anonimização (`nome = 'removido'`, `cpf = NULL`, `observacoes = NULL`) e grave quantos registros foram afetados.

**Aviso da clínica na página de agendamento:** campo configurável por clínica para o aviso de privacidade dela, exibido junto ao formulário e ao campo "Motivo da consulta". A obrigação é da clínica; oferecer o espaço é uma boa prática da operadora.

**Minimização no formulário de agendamento** (`public/index.html:29-35`): CPF e data de nascimento são obrigatórios para marcar uma consulta. A escolha dos campos é das clínicas, como controladoras (BL-04), mas vale oferecer a elas a opção de tornar esses campos opcionais ou de pedi-los só no atendimento (art. 6º, III).

**Em monitoramento (norma não vigente, não gera não conformidade):** a revisão da Res. CD/ANPD nº 1/2021 (fiscalização e processo sancionador) está em consulta pública até 26/10/2026. Até a publicação da norma final, a Res. CD/ANPD nº 1/2021 segue vigente e é a referência de risco sancionatório deste relatório.

---

## Glossário

- **ANPD:** Agência Nacional de Proteção de Dados, que regula e fiscaliza a LGPD.
- **Agente de pequeno porte:** microempresa, empresa de pequeno porte, startup e equivalentes, com regras simplificadas pela Res. CD/ANPD nº 2/2022, salvo nas exclusões da própria resolução, como o tratamento de alto risco.
- **Tratamento de alto risco:** tratamento em larga escala ou com impacto significativo para os titulares, combinado com fatores como dados sensíveis; impede as simplificações do pequeno porte.
- **Controlador:** quem decide por que e como os dados são tratados e responde por base legal, transparência, direitos e comunicação de incidentes (aqui, a clínica, para os dados dos pacientes; a AgendaFácil, para as contas das clínicas e para o rastreamento que instalou).
- **Operador:** quem trata dados em nome do controlador e segundo as instruções dele (aqui, a AgendaFácil, para os dados dos pacientes).
- **Suboperador:** fornecedor contratado pelo operador para tratar os mesmos dados (aqui, a Vercel e o provedor do banco).
- **Finalidade própria:** uso que o operador faz dos dados por decisão sua, fora das instruções do controlador; nesse uso ele passa a ser controlador.
- **Dado pessoal sensível:** dado sobre saúde, origem racial, religião, vida sexual, biometria e outros do art. 5º, II, com regras mais rígidas.
- **Base legal:** hipótese da lei que autoriza um tratamento (arts. 7º e 11).
- **Encarregado (DPO):** pessoa ou empresa que faz a ponte entre a organização, os titulares e a ANPD.
- **Registro das operações de tratamento:** inventário do que é tratado, para quê, com qual base, por quanto tempo e com quem é compartilhado (art. 37).
- **RIPD:** relatório de impacto à proteção de dados, documento do controlador que analisa riscos e salvaguardas de um tratamento.
- **DPA (contrato de operador):** contrato que fixa as obrigações de proteção de dados de quem trata dados em nome de outro.
- **CPC (cláusulas-padrão contratuais):** cláusulas aprovadas pela ANPD que autorizam enviar dados a países sem adequação reconhecida.
- **Transferência internacional:** envio ou acesso a dados pessoais a partir de outro país.
- **Mecanismo não evidenciado:** contrato ou termos não localizados ou não examinados; diferente de mecanismo comprovadamente ausente, que é mais grave.
- **Aplicabilidade:** situação de cada item do checklist: aplicável (avaliado e pontuado), não aplicável ou não verificado.
- **Não aplicável (`NAO_APLICAVEL`):** item cujo objeto não existe no projeto ou cuja obrigação é de outro agente; também vale para uma área inteira do score (aqui, IA). Fica fora do cálculo.
- **Não verificado (`NAO_VERIFICADO`):** controle técnico que só pode ser conferido na produção ou no painel de um provedor, a que a auditoria não teve acesso; fica fora do cálculo e vira verificação pendente.
- **Cobertura:** parcela dos itens verificáveis que a auditoria conseguiu avaliar; abaixo de 80%, o score é parcial.
- **Confiança da evidência:** quão direta e completa é a prova de um item (alta, média ou baixa); não muda o score.
- **Contagem única:** regra pela qual uma mesma falha reprova um só item, o mais específico; outros itens só a repetem se forem uma obrigação legal diferente.
- **Aceite de risco:** decisão registrada do controlador de adiar ou não corrigir um item; não muda o score.
- **Meta Pixel:** script da Meta que registra visitas e eventos para campanhas de publicidade.
- **Banner de cookies:** aviso que pede a escolha do visitante sobre cookies e rastreadores não essenciais.
- **CSP:** cabeçalho que diz ao navegador de onde a página pode carregar scripts e outros recursos.
- **HSTS:** cabeçalho que obriga o navegador a usar sempre HTTPS.
- **JWT:** token assinado que identifica o usuário logado em cada chamada à API.
- **RBAC:** controle de acesso por papel (ex.: `admin`, `clinica`).
- **bcrypt:** algoritmo próprio para guardar senhas de forma irreversível.
- **Exposição excessiva de dados:** API que devolve mais campos do que a tela precisa.
- **Mascaramento:** ocultar parte de um dado (ex.: `***.456.***-**`) antes de gravá-lo ou exibi-lo.
- **Trilha de auditoria:** registro de quem acessou ou alterou o quê, e quando.
- **Limitação de taxa (rate limiting):** limite de requisições por período, contra abuso e força bruta.
- **MFA:** autenticação com mais de um fator (senha e código do celular, por exemplo).
- **Varredura de dependências:** verificação automática de vulnerabilidades conhecidas nas bibliotecas usadas.
- **SAST:** análise automática do código-fonte em busca de falhas de segurança.
- **SBOM:** lista de todos os componentes de software de uma versão.
- **MCI:** Marco Civil da Internet (Lei nº 12.965/2014).
- **Registros de acesso a aplicações:** data, hora, IP e porta lógica de cada acesso, que o provedor guarda por 6 meses (MCI, art. 15).
- **PaaS:** plataforma que hospeda e executa a aplicação sem que a empresa administre servidores (aqui, a Vercel).
- **`score_tecnico` e `score_documental`:** subtotais informativos do score, só com itens de código e infraestrutura ou só com itens de documentos e processos.
- **Catálogo de itens:** lista fixa dos itens do checklist, com ID, criticidade e fundamento; a auditoria avalia todos os itens dos módulos ativos.
- **Escopo direcionado:** marca do relatório quando o cenário não é a auditoria completa; o score vale para o que foi auditado.
- **Teto de classificação:** com achado `CRITICO` aberto, a classificação não passa de `PARCIALMENTE_CONFORME`, qualquer que seja o score.

---

> Este relatório foi gerado com apoio de IA pelo LGPD Enterprise Auditor, a partir das evidências disponíveis no momento da análise. Ele apoia, mas não substitui, a avaliação do encarregado (DPO) e a assessoria jurídica especializada. As conclusões dependem da completude e da atualidade das evidências fornecidas.
