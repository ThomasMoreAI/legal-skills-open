# Módulo AppSec — segurança de aplicações web e APIs (OWASP)

## Escopo
Auditar segurança de aplicação web e APIs com foco em riscos LGPD, incluindo cookies/tracking no front-end e dados pessoais em logs de aplicação.

## Checklist atômico
Itens do catálogo (regras em `core/scoring-engine.md`, "Catálogo de itens"): avaliar todos, cada um com sua `applicability`.

Fronteira com o módulo `cloud`: `SE-02` avalia o que a aplicação define no código do servidor (redirecionamento para HTTPS, HSTS, CSP e demais cabeçalhos). Cabeçalhos definidos na configuração da hospedagem, e os das páginas que ela serve sem passar pela aplicação, são avaliados em `IN-01`.

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `SE-01` | Senhas e credenciais de usuários são armazenadas com hash forte e salgado (ex.: Argon2id, bcrypt), nunca em texto puro ou com cifra reversível? | 6 | `CRITICO` | — | `TECNICO` | art. 46 |
| `SE-02` | Todo tráfego usa HTTPS, com HSTS e cabeçalhos de segurança (CSP, entre outros) configurados? | 6 | `ALTO` | — | `TECNICO` | art. 46 |
| `SE-03` | A autorização impede acesso indevido a dados de outros usuários ou clientes (RBAC/ABAC, isolamento entre contas)? | 6 | `ALTO` | `CRITICO` com falha explorável que permita ler ou extrair dados pessoais de terceiros | `TECNICO` | art. 46 |
| `SE-04` | A autenticação é robusta (política de senha, bloqueio de tentativas e MFA quando o risco pede)? | 6 | `ALTO` | — | `TECNICO` | art. 46 |
| `SE-05` | Há proteção contra XSS, CSRF, SSRF e SQL Injection? | 6 | `ALTO` | `CRITICO` com falha explorável que permita ler ou extrair dados pessoais de terceiros | `TECNICO` | art. 46 |
| `SE-06` | Os logs da aplicação evitam registrar dados pessoais e sensíveis (CPF, e-mail, telefone, tokens, senhas, payloads completos) ou os mascaram antes da gravação? | 11 | `ALTO` | `CRITICO` com senhas ou tokens em texto puro nos logs | `TECNICO` | arts. 6º, III e 46 |
| `SE-07` | Há trilha de auditoria dos acessos a dados pessoais no backend (quem acessou, o quê e quando)? | 6 | `ALTO` | — | `TECNICO` | arts. 6º, X e 46 |
| `SE-08` | Sessões de navegador têm proteção adequada (cookie de sessão com `HttpOnly`, `Secure` e `SameSite`, expiração e rotação)? | 6 | `ALTO` | — | `TECNICO` | art. 46 |
| `SE-09` | Há segregação de ambientes (produção, homologação, desenvolvimento) e de funções de quem acessa dados pessoais? | 6 | `MEDIO` | — | `TECNICO` | art. 46 |
| `SE-10` | Entradas e saídas são validadas e sanitizadas? | 6 | `MEDIO` | — | `TECNICO` | art. 46 |
| `AP-01` | As APIs validam tokens corretamente (JWT: assinatura, algoritmo, expiração e audiência) e usam OAuth com escopos mínimos? | 9 | `ALTO` | — | `TECNICO` | art. 46 |
| `AP-02` | As respostas das APIs expõem só os campos necessários, sem exposição excessiva de dados pessoais? | 9 | `ALTO` | — | `TECNICO` | arts. 6º, III e 46 |
| `AP-03` | Há rate limiting e proteção contra abuso nas APIs e na autenticação? | 9 | `MEDIO` | — | `TECNICO` | art. 46 |
| `AP-04` | A comunicação com integrações e entre serviços é criptografada em trânsito? | 9 | `ALTO` | — | `TECNICO` | art. 46 |
| `AP-05` | As APIs públicas estão inventariadas (rotas, dados expostos, responsável)? | 9 | `MEDIO` | — | `DOCUMENTAL` | arts. 37 e 46 |
| `AP-06` | As API keys ficam fora do código, dos repositórios e do front-end? | 9 | `ALTO` | `CRITICO` se a chave exposta der acesso a dados pessoais | `TECNICO` | art. 46 |

## Cookies, tracking e consentimento no front-end
Aplicável a toda aplicação web que use cookies, pixels, tags ou SDKs de terceiros (ex.: Google Analytics, Meta Pixel, Hotjar, Google Ads).

Sem cookies, pixels, tags ou SDKs de terceiros, os itens `CK` ficam `NAO_APLICAVEL`, com a evidência.

Fronteira entre os itens: o disparo de rastreador antes da escolha, ou antes de a escolha salva ser reaplicada numa nova visita, é contado em `CK-02`. `CK-03` avalia o mecanismo de revisão e revogação e a limpeza do que já foi gravado. `CK-08` só se aplica quando há cookies classificados em categorias.

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `CK-01` | Rejeitar está disponível na primeira camada do banner, com o mesmo destaque de aceitar? | 5 | `MEDIO` | — | `TECNICO` | art. 8º, caput |
| `CK-02` | Cookies e scripts não essenciais ficam bloqueados até o aceite, sem requisições a terceiros de analytics ou publicidade antes do consentimento — salvo outra base legal documentada (ex.: legítimo interesse com LIA para medição estritamente agregada)? | 5 | `ALTO` | — | `TECNICO` | arts. 7º, I e 8º |
| `CK-03` | O usuário consegue revisar e revogar as preferências a qualquer momento, com efeito real sobre os scripts já carregados? | 5 | `ALTO` | — | `TECNICO` | art. 8º, §5º |
| `CK-04` | As escolhas ficam registradas (data, versão do banner, categorias aceitas) como prova do consentimento? | 5 | `MEDIO` | — | `TECNICO` | art. 8º, §2º |
| `CK-05` | O consentimento é granular por finalidade (desempenho, funcionalidade, publicidade)? | 5 | `MEDIO` | `ALTO` com categorias pré-marcadas | `TECNICO` | art. 8º, §4º |
| `CK-06` | Existe banner ou CMP funcional, com informação clara sobre finalidades e terceiros? | 5 | `MEDIO` | — | `TECNICO` | arts. 8º e 9º |
| `CK-07` | Pixels, fingerprinting e identificadores persistentes de terceiros estão inventariados e cobertos pela política de cookies? | 5 | `MEDIO` | — | `DOCUMENTAL` | arts. 9º e 37 |
| `CK-08` | Os cookies classificados como estritamente necessários são de fato necessários (a categoria não mascara analytics ou publicidade)? | 5 | `MEDIO` | `BAIXO` se for só imprecisão de classificação na política, sem rastreamento indevido | `TECNICO` | art. 6º, III |

Fundamento: art. 7º, I e art. 8º (consentimento livre, informado, inequívoco, por finalidade e revogável), art. 9º (transparência) e art. 6º, III (necessidade). Referência orientativa, não vinculante: Guia Orientativo da ANPD sobre cookies e proteção de dados pessoais. Usar [[cookie-policy-template]].

## Critérios de evidência
- configuração de headers e políticas de segurança;
- evidências de controles de autenticação/autorização;
- logs de tentativas de abuso e bloqueio;
- exemplos de validação/sanitização de entrada;
- política de logging/mascaramento e amostras de log da aplicação;
- captura de rede (HAR/DevTools) antes e depois do aceite do banner;
- configuração do CMP e registro de consentimentos.

## Mapeamento para severidade e score
- Falha explorável que permite ler ou extrair dados pessoais de terceiros: `CRITICO`. "Explorável" é a falha evidenciada no código ou na configuração; não exige exploração real nem incidente (`core/severity-model.md`).
- Senhas ou tokens em texto puro nos logs: `CRITICO`.
- Falha de autenticação ou autorização que não dá acesso a dados pessoais de terceiros: `ALTO`.
- Ausência de HTTPS em rotas com dados pessoais, API sem autenticação adequada ou com exposição excessiva de dados pessoais: `ALTO`.
- Logs da aplicação com dados pessoais sem mascaramento: `ALTO`.
- Cookies/pixels de publicidade ou analytics de terceiros disparados antes do aceite, sem outra base legal documentada: `ALTO`.
- Categorias de cookies pré-marcadas ou ausência de mecanismo de revogação: `ALTO`.
- Rejeição sem destaque equivalente, consentimento pouco granular ou ausência de registro das escolhas: `MEDIO`.
- Ausência parcial de hardening e validações: `MEDIO`.
- Imprecisões na classificação de cookies da política: `BAIXO`.
- Área de score (mapa por domínio de `core/scoring-engine.md`): itens `SE` em `seguranca` (domínios 6 e 11); itens `AP` em `apis_integracoes` (domínio 9); itens `CK` em `bases_legais` (domínio 5). A criticidade de cada item está nas tabelas acima.
