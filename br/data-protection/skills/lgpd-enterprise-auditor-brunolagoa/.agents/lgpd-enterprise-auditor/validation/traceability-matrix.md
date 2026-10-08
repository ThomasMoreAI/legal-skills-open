# Validação — matriz de rastreabilidade (domínios → módulos)

Cada domínio de auditoria, a área de score em que pontua, os módulos que trazem seus itens e os itens do catálogo. Um prefixo sozinho (ex.: `CK`) indica todos os itens daquele prefixo.

| Código | Domínio de auditoria | Área de score | Módulos | Itens do catálogo |
|---|---|---|---|---|
| `BL` | Bases legais (arts. 7º e 11), dados de acesso público e dados de crianças (art. 14) | `bases_legais` | `legal` | `BL`, `CA`, `DP`, `OP-02` |
| 1 | Mapeamento de dados | `governanca` | `governance` | `GV-01` |
| 2 | Consentimento | `bases_legais` | `legal` | `CS` |
| 3 | Direitos do titular | `direitos_titular` | `legal`, `mobile` | `DT-01` e `DT-02`, `DT-06` a `DT-10`, `MB-12` |
| 4 | Política de privacidade (inclui transparência, art. 9º) | `direitos_titular` | `legal`, `mobile` | `DT-03` a `DT-05`, `MB-11` |
| 5 | Cookies e tracking | `bases_legais` | `appsec`, `mobile` | `CK`, `MB-06`, `MB-08` |
| 6 | Segurança da informação | `seguranca` | `appsec` | `SE-01` a `SE-05`, `SE-07` a `SE-10` |
| 7 | Cloud security (inclui PaaS e hospedagem) | `infraestrutura` | `cloud` | `IN-01` a `IN-12`, `IN-14` a `IN-16` |
| 8 | Mobile security | `seguranca` | `mobile` | `MB-01` a `MB-05`, `MB-07`, `MB-10`, `MB-13` |
| 9 | APIs e integrações | `apis_integracoes` | `appsec` | `AP` |
| 10 | DevSecOps | `seguranca` | `devsecops` | `DS` |
| 11 | Logs e observabilidade | `seguranca` | `appsec` | `SE-06` |
| 12 | IA/LLM | `ai_llm` | `ai-llm` | `IA` |
| 13 | Governança (encarregado, RIPD, incidentes, políticas) | `governanca` | `governance` | `GV-02` e `GV-03`, `GV-05` a `GV-08`, `GV-10` e `GV-11`, `GV-15` a `GV-17` |
| 14 | Compartilhamento de dados (inclui transferência internacional) | `governanca` | `cloud`, `governance`, `legal` | `GV-09`, `IN-13`, `OP-01`, `OP-03` a `OP-06`, `TI` |
| 15 | Retenção e exclusão | `governanca` | `governance` | `GV-04`, `GV-12` a `GV-14` |
| 16 | Proteção de crianças e adolescentes no ambiente digital — ECA Digital (deveres de produto) | `eca_digital` | `eca-digital`, `mobile` | `ECA`, `MB-09` |
| 17 | Plataformas digitais e conteúdo de terceiros | `plataformas_digitais` | `plataformas-digitais` | `PD` |

## Observações
- A área de score de cada domínio vem do mapa por domínio de `core/scoring-engine.md`.
- Logs e observabilidade (domínio 11): os logs de aplicação são o item `SE-06`; os logs e a observabilidade do provedor (`IN-06`, `IN-12`) e a guarda de registros de acesso (`IN-04`) são avaliados no módulo `cloud` e pontuam no domínio 7.
- Os deveres gerais de provedor de aplicações (Decreto nº 8.771/2016, art. 16-A, I e II) são os itens `GV-06` e `GV-07`, do domínio 13, avaliados com o módulo `plataformas-digitais` ativo ou não.
- Esta matriz deve ser atualizada sempre que um item mudar de domínio ou de módulo. `scripts/tests/test-framework.sh` confere que ela cita todos os prefixos do catálogo.
