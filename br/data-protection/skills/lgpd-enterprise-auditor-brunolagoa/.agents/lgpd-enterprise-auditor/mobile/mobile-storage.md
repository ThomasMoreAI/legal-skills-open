# Módulo Mobile — privacidade e segurança em aplicativos

## Escopo
Avaliar riscos de privacidade e segurança em apps iOS/Android/Flutter/React Native.

## Checklist atômico
Pergunta de enquadramento (não pontua): o app é classificado ou acessível a menores de 18 anos nas lojas (App Store, Google Play)? Se sim, ativar [[eca-digital]]; o consumo do sinal de idade da loja ou do sistema e o bloqueio próprio são avaliados lá (`ECA-07`). Sem menores entre os usuários, `MB-09` fica `NAO_APLICAVEL`.

Itens do catálogo (regras em `core/scoring-engine.md`, "Catálogo de itens"): avaliar todos, cada um com sua `applicability`.

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `MB-01` | Dados pessoais e credenciais ficam em armazenamento seguro do dispositivo (Keychain, Keystore, banco cifrado), nunca em arquivo ou preferência em claro? | 8 | `ALTO` | `CRITICO` com dado sensível exposto sem proteção | `TECNICO` | art. 46 |
| `MB-02` | As permissões solicitadas seguem a necessidade mínima, pedidas no momento do uso? | 8 | `MEDIO` | — | `TECNICO` | art. 6º, III |
| `MB-03` | Há prevenção de vazamento por área de transferência, log local e captura de tela em telas com dados sensíveis? | 8 | `MEDIO` | — | `TECNICO` | art. 46 |
| `MB-04` | O app detecta jailbreak ou root e reduz a exposição de dados pessoais nesses dispositivos? | 8 | `BAIXO` | — | `TECNICO` | art. 46 |
| `MB-05` | Deep links e app links são validados, sem expor dados ou ações sensíveis por URL? | 8 | `MEDIO` | — | `TECNICO` | art. 46 |
| `MB-06` | SDKs de tracking e analytics só são iniciados depois do consentimento, com controle por finalidade? | 5 | `ALTO` | — | `TECNICO` | arts. 7º, I e 8º |
| `MB-07` | As regras de acesso do backend mobile (ex.: Firebase rules) são restritivas, sem leitura ou escrita aberta? | 8 | `ALTO` | `CRITICO` com regras abertas que exponham dados pessoais | `TECNICO` | art. 46 |
| `MB-08` | Identificadores de dispositivo e de publicidade (IDFA, AAID) são usados com base legal adequada, respeitando o consentimento pedido pelo sistema quando ele for a base? | 5 | `MEDIO` | — | `TECNICO` | arts. 7º e 8º |
| `MB-09` | SDKs de publicidade deixam de receber identificadores de usuários menores de 18 anos? | 16 | `ALTO` | `CRITICO` se os identificadores alimentarem perfilamento para publicidade | `TECNICO` | Lei nº 15.211/2025, arts. 22 e 26; LGPD art. 14 |
| `MB-10` | O tráfego do app usa TLS com validação de certificado, sem exceção para tráfego em claro, e com fixação de certificado (pinning) quando o risco justificar? | 8 | `ALTO` | — | `TECNICO` | art. 46 |
| `MB-11` | As declarações de privacidade nas lojas (rótulos de privacidade, seção de segurança dos dados) batem com a coleta e o compartilhamento reais do app e dos SDKs? | 4 | `MEDIO` | — | `DOCUMENTAL` | arts. 6º, VI e 9º |
| `MB-12` | O app oferece caminho para pedir a eliminação da conta e dos dados (no próprio app ou por canal indicado nele), e a eliminação alcança o backend? | 3 | `MEDIO` | — | `TECNICO` | arts. 16 e 18, IV e VI |
| `MB-13` | Os backups do sistema (iCloud, Auto Backup do Android) excluem credenciais e dados pessoais sensíveis do app? | 8 | `MEDIO` | — | `TECNICO` | art. 46 |

## Critérios de evidência
- configuração de storage seguro;
- manifesto de permissões e justificativa;
- inventário de SDKs terceiros;
- regras de acesso backend para mobile;
- fluxo de consentimento para tracking;
- configuração de rede (TLS, tráfego em claro, pinning) e de backup do sistema;
- declarações de privacidade publicadas nas lojas, comparadas com o inventário de SDKs;
- fluxo de eliminação de conta e seu efeito no backend.

## Mapeamento para severidade e score
- Exposição local de dado sensível sem proteção: `CRITICO`.
- Tracking sem consentimento granular: `ALTO`.
- Permissões excessivas sem exploração direta: `MEDIO`.
- Tráfego do app sem TLS ou sem validação de certificado: `ALTO`.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `seguranca` (domínio 8); `MB-06` e `MB-08` pontuam em `bases_legais` (domínio 5); `MB-11` e `MB-12`, em `direitos_titular` (domínios 4 e 3); `MB-09`, em `eca_digital` (domínio 16). A criticidade de cada item está na tabela do checklist.
