# Núcleo — cálculo do score

## Objetivo
Padronizar cálculo e classificação do score LGPD em escala 0-100.

## Pesos por área
- `bases_legais`: 12%
- `seguranca`: 20%
- `direitos_titular`: 12%
- `governanca`: 12%
- `infraestrutura`: 8%
- `apis_integracoes`: 8%
- `ai_llm`: 8%
- `eca_digital`: 10%
- `plataformas_digitais`: 10%

Somatório obrigatório: 100%.

As sete primeiras áreas guardam entre si a proporção 15 : 25 : 15 : 15 : 10 : 10 : 10. Quando `eca_digital` e `plataformas_digitais` são `NAO_APLICAVEL` (o caso mais comum), a redistribuição devolve exatamente esses pesos.

## Cálculo do score (obrigatório)
O cálculo é fechado para que duas execuções sobre as mesmas evidências cheguem ao mesmo número.

1. **Valor do item** pelo status: `CONFORME` = 1; `PARCIAL` = 0,5; `NAO_CONFORME` = 0.
2. **Peso do item** pela `criticality` (criticidade do item no catálogo, já considerados os agravantes da linha do item e a modulação por porte de `core/severity-model.md`): `CRITICO` = 4; `ALTO` = 3; `MEDIO` = 2; `BAIXO` = 1.
3. **Score da área** (0-100): `score_area = 100 * SUM(valor * peso) / SUM(peso)`, somando os itens `APLICAVEL` cuja `score_area` é aquela área. Itens `NAO_APLICAVEL` e `NAO_VERIFICADO` ficam fora das somas.
4. **Score global**: aplicar o peso de cada área (ajustado quando houver área `NAO_APLICAVEL`) e somar.

Fórmula:
`score_global = SUM(score_area * peso_area)`

Calcular com valores exatos; exibir o score de cada área com uma casa decimal e arredondar só o score global, para o inteiro mais próximo. Fração de exatamente 0,5 sobe (84,5 vira 85).

**Contagem única:** cada item é avaliado pelo seu próprio requisito, e uma mesma falha não é contada duas vezes:
- quando parte do requisito de um item repete uma falha que é o requisito de outro, essa parte é citada na evidência e o item pontua pelo que resta (ex.: `SE-04` não é reprovado pela falta de limitação de tentativas no login, que é o requisito de `AP-03`);
- quando o item **depende** de outro e esse outro está `NAO_CONFORME`, o dependente fica `NAO_APLICAVEL`, com a referência ao item que conta a falha (se o outro está `NAO_VERIFICADO`, o dependente também fica). As dependências são **só as que os módulos listam**, em linhas no formato "`GV-05` depende de `GV-02`", logo abaixo das tabelas; fora dessa lista não há dependência, e o item é avaliado pelo próprio requisito. Critério para incluir um par na lista: o item não poderia ser atendido enquanto o outro controle continuar ausente;
- quando o requisito inteiro do item falha, ele é reprovado, ainda que a causa seja a mesma de outro item: no catálogo, cada item é uma obrigação distinta (ex.: o mesmo pixel viola o consentimento de cookies, `CK-02`, e também configura transferência internacional sem mecanismo, `TI-02`).

Uma área aplicável sem nenhum item avaliado indica cobertura insuficiente: avaliar ao menos um item dela; se não for possível, declarar "cobertura insuficiente" em `score_lgpd` e redistribuir seu peso como na regra de `NAO_APLICAVEL`, sem chamá-la assim.

## Catálogo de itens
Os itens do checklist são fixos. Cada módulo traz, na seção "Checklist atômico", a tabela dos seus itens:

`ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento`

- **ID**: identificador estável (ex.: `SE-03`). Nunca é renumerado nem reaproveitado; item retirado deixa o número vago.
- **Domínio**: código do domínio no mapa abaixo (`BL` ou `1` a `17`); define a área de score.
- **Criticidade**: a `criticality` padrão do item.
- **Agravante ou atenuante**: única condição que muda a criticidade padrão, além da modulação por porte.
- **Controle**: `control_type` do item (`TECNICO` ou `DOCUMENTAL`).
- **Fundamento**: dispositivo que o achado cita.

Regras:
- a auditoria avalia **todos** os itens do catálogo de cada módulo ativo; cada um recebe `applicability` (`APLICAVEL`, `NAO_APLICAVEL` ou `NAO_VERIFICADO`), e nenhum é omitido;
- o `id` do `check_item` é o ID do catálogo; o texto do item é o do catálogo, que pode ganhar um complemento de contexto sem mudar o requisito;
- a `criticality` é a do catálogo. Só muda pelo agravante ou atenuante escrito na linha do item, quando a condição está presente no escopo, ou pela modulação por porte; a evidência registra a condição aplicada. Nunca é escolhida caso a caso;
- problema real sem item correspondente entra como **item extra**, com ID `EX-nn`, domínio, criticidade pela regra de `core/severity-model.md` e a justificativa de não caber em nenhum item do catálogo. O item extra entra no score e aparece identificado como tal no relatório;
- perguntas de enquadramento dos módulos (ex.: "o serviço é de acesso provável por menores?") decidem a ativação e a aplicabilidade; não são itens e não pontuam.
- nos agravantes, **dado sensível** é o do art. 5º, II, e também o dado que revele informação sensível e possa causar dano ao titular (art. 11, §1º) — ex.: o registro de que alguém agendou consulta numa clínica. A extensão vale para todos os itens, não só para os de operador;
- o agravante só se aplica quando a condição está no **objeto do item** (o tratamento, o fluxo, o operador ou o ativo que o item avalia), não por existir dado sensível em outra parte do sistema.

## Aplicabilidade do item e cobertura
Cada `check_item` tem uma `applicability`:
- `APLICAVEL`: o requisito vale para o escopo e foi avaliado; recebe `status` e entra no score.
- `NAO_APLICAVEL`: o objeto do item não existe no escopo, com evidência `ENCONTRADA` da inexistência (ex.: item de Kubernetes em projeto sem containers), ou a obrigação é de outro agente (ex.: coleta de consentimento quando o auditado é só operador daquele fluxo). Fica fora do score, com a justificativa.
- `NAO_VERIFICADO`: o requisito vale, mas a verificação depende de acesso que o auditor não tem (ambiente de produção, painel do provedor, sistema de terceiro). Fica fora do score, com o motivo e o acesso necessário.

Limites:
- falta de evidência **não** é `NAO_APLICAVEL` nem `NAO_VERIFICADO`: documento, contrato, política ou registro que o auditado deveria apresentar e não apresentou é `AUSENTE` e reduz o score;
- a aplicabilidade decorre dos **fatos do tratamento**, não do que o auditado documentou: item cujo objeto existe no sistema é `APLICAVEL`, ainda que nenhum documento o mencione (ex.: se o sistema coleta consentimento num formulário, os itens de consentimento valem, mesmo sem base legal registrada);
- `NAO_VERIFICADO` só cabe em controle `TECNICO` fora do alcance do auditor; controle `DOCUMENTAL` nunca é `NAO_VERIFICADO`;
- controle que **não tem representação em arquivo do repositório** e só existe na configuração de um serviço (ex.: retenção de logs, backup, MFA e membros do painel, proteção de branch) é `NAO_VERIFICADO`;
- controle que **costuma ser declarado em arquivo do repositório** (ex.: varredura de dependências, de segredos ou de código no CI, rate limiting da aplicação, cabeçalhos em `vercel.json` ou equivalente) e não está lá é `NAO_CONFORME`, ainda que o provedor ofereça uma alternativa por painel; a confiança é a que a evidência permitir, e a alternativa vira verificação pendente;
- item com elementos verificáveis e elementos fora do alcance: se algum elemento verificável falha, o status segue a régua de `core/evidence-engine.md` (a falha é certa); se todos os verificáveis atendem, o item fica `NAO_VERIFICADO`, registrando o que já foi comprovado e o acesso que falta. `CONFORME` exige que tudo o que o item pede esteja comprovado, sem exceção para item verificado pela metade. Está fora do alcance o elemento cuja evidência não tem representação em arquivo do repositório e só existe na configuração de um serviço ou em produção;
- cada item `NAO_VERIFICADO` gera uma verificação pendente no relatório.

**Cobertura** = itens com `status` ÷ (itens com `status` + itens `NAO_VERIFICADO`), global e por área; itens `NAO_APLICAVEL` não entram na conta. Cobertura global abaixo de 80% obriga a marcar o resultado como **score parcial** ao lado da classificação. Área com cobertura abaixo de 50% recebe a marca **cobertura baixa** ao lado do seu score: itens não verificados saem da conta e podem elevar a nota da área. Área em que todos os itens são `NAO_VERIFICADO` cai na regra de cobertura insuficiente acima.

Quando o agravante de um item depende do estado da evidência (ex.: `TI-02`, mecanismo de transferência internacional não evidenciado pesa `ALTO`; comprovadamente ausente, `CRITICO`), vale o estado atual. Se uma verificação pendente puder mudar a criticidade, o relatório lista esse item entre as verificações pendentes que podem alterar o score.

## Mapa de áreas por domínio
Cada `check_item` pontua em **exatamente uma** área, definida pelo seu domínio. Módulos não escolhem a área caso a caso.

| Código | Domínio de auditoria | Área de score |
|---|---|---|
| `BL` | Bases legais (arts. 7º e 11), dados de acesso público e dados de crianças (art. 14) | `bases_legais` |
| `1` | Mapeamento de dados | `governanca` |
| `2` | Consentimento | `bases_legais` |
| `3` | Direitos do titular | `direitos_titular` |
| `4` | Política de privacidade (inclui transparência, art. 9º) | `direitos_titular` |
| `5` | Cookies e tracking | `bases_legais` |
| `6` | Segurança da informação | `seguranca` |
| `7` | Cloud security (inclui PaaS e hospedagem) | `infraestrutura` |
| `8` | Mobile security | `seguranca` |
| `9` | APIs e integrações | `apis_integracoes` |
| `10` | DevSecOps | `seguranca` |
| `11` | Logs e observabilidade | `seguranca` |
| `12` | IA/LLM | `ai_llm` |
| `13` | Governança (encarregado, RIPD, incidentes, políticas) | `governanca` |
| `14` | Compartilhamento de dados (inclui transferência internacional) | `governanca` |
| `15` | Retenção e exclusão | `governanca` |
| `16` | Proteção de crianças e adolescentes no ambiente digital — ECA Digital (deveres de produto) | `eca_digital` |
| `17` | Plataformas digitais e conteúdo de terceiros | `plataformas_digitais` |

## Score técnico e score documental (informativos)
Além do score global, o relatório mostra dois subtotais com a mesma fórmula dos passos 1 a 3, aplicada a todos os itens de cada natureza (`control_type`):
- `score_tecnico`: itens `TECNICO`;
- `score_documental`: itens `DOCUMENTAL`.

Os subtotais **não** entram na classificação final; servem para mostrar, por exemplo, um núcleo técnico forte com documentação ausente.

## Riscos aceitos
Item com `risk_acceptance` registrado continua pontuando pelo seu status. Aceitar um risco não torna o item conforme.

## Áreas não aplicáveis
Além da aplicabilidade de cada item, uma **área de score** inteira pode ser `NAO_APLICAVEL`. O `status` do `check_item` continua restrito a `CONFORME | PARCIAL | NAO_CONFORME`; a aplicabilidade é um campo à parte.

Uma área só pode ser `NAO_APLICAVEL` quando o objeto que ela avalia não existe no escopo auditado, com evidência `ENCONTRADA` da inexistência — nunca por falta de evidência, que é `AUSENTE` e reduz o score, e nunca só porque o cenário não ativou o módulo.

Como a inexistência é comprovada:
- módulo ativo (ex.: `full_audit`): todos os itens da área ficam `NAO_APLICAVEL`, com a evidência (ex.: nenhum SDK ou chamada a provedor de LLM no código e nenhum fluxo de IA declarado);
- módulo não ativado pelo cenário: o roteador confere os gatilhos de `orchestrator/router.md` e registra a mesma evidência no "escopo excluído explicitamente".

Se o objeto existe, ou a inexistência não foi comprovada, e mesmo assim o módulo ficou de fora (ex.: o usuário restringiu o escopo), a área **não** é `NAO_APLICAVEL`: é área sem item avaliado, declarada como "cobertura insuficiente" com o motivo "fora do escopo", e seu peso é redistribuído sem chamá-la de não aplicável.

Áreas sempre aplicáveis, nunca `NAO_APLICAVEL`: `bases_legais`, `seguranca`, `direitos_titular` e `governanca`.

`eca_digital` é aplicável quando o módulo `eca-digital` está ativo (cenário ou gatilho normativo de público infantojuvenil); `plataformas_digitais`, quando o módulo `plataformas-digitais` está ativo (cenário ou gatilho normativo de plataformas digitais). Sem o gatilho, a área é `NAO_APLICAVEL`, com a evidência registrada pelo roteador.

Redistribuição proporcional entre as áreas aplicáveis:
`peso_ajustado_area = peso_area / SUM(peso das áreas aplicáveis)`
`score_global = SUM(score_area * peso_ajustado_area)`

Exemplo: `saas_web` sem uso de IA, sem público infantojuvenil e sem conteúdo de terceiros → `ai_llm`, `eca_digital` e `plataformas_digitais` são `NAO_APLICAVEL`; as seis áreas restantes somam 72% e cada peso é dividido por 0,72 (`seguranca` passa de 20% para 27,8%).

O relatório deve declarar em `score_lgpd` as áreas `NAO_APLICAVEL`, a justificativa e os pesos ajustados.

## Classificação final canônica
- `0-49`: `CRITICO`
- `50-69`: `BAIXO_NIVEL`
- `70-84`: `PARCIALMENTE_CONFORME`
- `85-94`: `ALTA_CONFORMIDADE`
- `95-100`: `EXCELENTE`

## Teto de classificação
Havendo ao menos um `finding` de severidade `CRITICO` (já considerada a modulação por porte), a classificação final não passa de `PARCIALMENTE_CONFORME`, qualquer que seja o score. O número do score não muda. Quando o teto de fato reduz a classificação (o score cairia em `ALTA_CONFORMIDADE` ou `EXCELENTE`), o relatório mostra ao lado dela a marca **classificação limitada por achado crítico** e os achados que a causam; com o score já em `PARCIALMENTE_CONFORME` ou abaixo, o teto não muda nada e a marca não aparece.

O aceite de risco não afasta o teto. Corrigido o achado, a classificação volta a seguir só a faixa do score.

## Escopo do score
O score mede o que o cenário auditou. Só o `full_audit` cobre os 17 domínios.

Em qualquer outro cenário, o relatório mostra ao lado da classificação a marca **escopo direcionado**, com o ID do cenário, e lista em `score_lgpd` os domínios que ficaram fora da auditoria. A classificação usa os mesmos rótulos canônicos, mas vale para o escopo auditado, não para a organização inteira.

## Normalização de rótulos
Para evitar ambiguidades, os relatórios devem usar exatamente os rótulos canônicos acima.

## Convenção de identificadores
- IDs de módulo usam kebab-case (ex.: `ai-llm`).
- IDs de área de score usam snake_case (ex.: `ai_llm`).
- Mapeamento obrigatório:
  - `ai-llm` (módulo) -> `ai_llm` (área de score);
  - `eca-digital` (módulo) -> `eca_digital` (área de score);
  - `plataformas-digitais` (módulo) -> `plataformas_digitais` (área de score).
