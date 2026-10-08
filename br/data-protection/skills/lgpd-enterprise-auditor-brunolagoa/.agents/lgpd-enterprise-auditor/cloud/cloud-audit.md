# Módulo Cloud — cloud, PaaS e hospedagem

## Escopo
Avaliar postura de segurança e privacidade de onde a aplicação roda:
- **IaaS** (AWS, Azure, GCP);
- **PaaS e serverless** (ex.: Vercel, Netlify, Render, Heroku, Cloudflare);
- **hospedagem compartilhada** (ex.: Hostinger, Locaweb, HostGator).

Os itens abaixo usam termos de IaaS; em PaaS e hospedagem, aplicar o equivalente do painel do provedor. O que o provedor não expõe ao cliente e o que só pode ser conferido com acesso ao painel ou à produção fica `NAO_VERIFICADO`, com o acesso necessário; o que não existe no escopo (ex.: VPC e security groups em hospedagem compartilhada) fica `NAO_APLICAVEL` (`core/scoring-engine.md`).

Quando a configuração da hospedagem está no próprio repositório (`vercel.json`, `netlify.toml`, `_headers` e equivalentes), ela é evidência como qualquer outro arquivo: o item é avaliado por ela, e a coleta das respostas de produção serve para elevar a confiança, não para adiar a avaliação.

Em PaaS e hospedagem gerenciada:
- `IN-06` avalia os logs, o analytics e as métricas nativos do provedor; `IN-12`, só as ferramentas contratadas além deles (sem nenhuma, `NAO_APLICAVEL`);
- `IN-09` avalia as regras de exposição que ficam com o cliente, como a lista de IPs e o acesso público do banco gerenciado, que só aparecem no painel (`NAO_VERIFICADO`); fica `NAO_APLICAVEL` só quando não há nenhum recurso de rede sob controle do cliente;
- `IN-16` avalia a parte do cliente: a versão do runtime e das imagens que ele escolhe e o processo para atualizá-las. Runtime fora de suporte fixado no repositório é `NAO_CONFORME`; o sistema operacional e a plataforma são do provedor.

`IN-08` trata só de armazenamento de objetos e de arquivos enviados: sem nenhum dos dois, fica `NAO_APLICAVEL`. A exposição de outros ativos é avaliada em `IN-09` (rede e banco) e em `IN-05` (painéis e tokens).

## Checklist atômico
Itens do catálogo (regras em `core/scoring-engine.md`, "Catálogo de itens"): avaliar todos, cada um com sua `applicability`.

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `IN-01` | A camada da hospedagem ou CDN preserva o que a aplicação envia (cabeçalhos de segurança e CSP, sem cache de páginas com dados pessoais, sem scripts ou analytics injetados pelo provedor)? Validar as respostas de **produção**, não só o código. | 7 | `ALTO` | — | `TECNICO` | art. 46 |
| `IN-02` | Variáveis de ambiente e segredos ficam no cofre do provedor, fora do repositório e de builds ou previews públicos? | 7 | `CRITICO` | — | `TECNICO` | art. 46 |
| `IN-03` | Bancos de dados com dados pessoais têm criptografia em repouso, controle de acesso e segregação? | 7 | `ALTO` | — | `TECNICO` | art. 46 |
| `IN-04` | Provedor de aplicações de internet: os registros de acesso (IP, porta lógica de origem, data e hora) são guardados por 6 meses e eliminados após o prazo, salvo requisição cautelar? | 7 | `MEDIO` | `ALTO` se os registros ficarem sem sigilo ou fora de ambiente controlado | `TECNICO` | MCI art. 15; Decreto nº 8.771/2016, art. 15-A; LGPD arts. 7º, II e 16, I |
| `IN-05` | As permissões de acesso ao provedor (IAM, membros do painel, tokens de deploy) seguem privilégio mínimo, com MFA? | 7 | `ALTO` | — | `TECNICO` | art. 46 |
| `IN-06` | Analytics, logs de acesso e métricas nativos do provedor que coletam dados pessoais têm retenção, acesso e base legal definidos? | 7 | `MEDIO` | `ALTO` se a plataforma injetar rastreamento sem base legal | `TECNICO` | arts. 6º, III, 7º e 46 |
| `IN-07` | Há firewall ou WAF, detecção de intrusão e monitoramento centralizado (SIEM ou equivalente) capazes de detectar acesso indevido a dados pessoais? | 7 | `MEDIO` | — | `TECNICO` | art. 46 |
| `IN-08` | Os serviços de armazenamento de objetos (buckets) e de arquivos enviados por usuários estão livres de exposição pública indevida? | 7 | `CRITICO` | — | `TECNICO` | art. 46 |
| `IN-09` | A segmentação de rede e as regras de exposição externa estão adequadas? | 7 | `MEDIO` | — | `TECNICO` | art. 46 |
| `IN-10` | Backups e réplicas são criptografados, têm acesso restrito e seguem a política de retenção (a eliminação também os alcança)? | 7 | `ALTO` | — | `TECNICO` | arts. 16 e 46 |
| `IN-11` | Os logs de auditoria da conta cloud ou do painel estão ativos e protegidos contra alteração? | 7 | `ALTO` | — | `TECNICO` | art. 46 |
| `IN-12` | As ferramentas de logs e observabilidade além das nativas do provedor de hospedagem (CloudWatch, Datadog, Sentry, ELK etc.) têm retenção definida, acesso por privilégio mínimo e mascaramento de dados pessoais? | 7 | `MEDIO` | — | `TECNICO` | arts. 6º, III e 46 |
| `IN-13` | A exportação de logs a ferramentas de terceiros está coberta por contrato de operador e, se os dados saírem do País, por mecanismo do art. 33? | 14 | `ALTO` | — | `DOCUMENTAL` | arts. 33 e 39 |
| `IN-14` | Chaves e segredos de produção ficam em serviço dedicado (KMS, Secrets Manager ou equivalente), com rotação? | 7 | `MEDIO` | — | `TECNICO` | art. 46 |
| `IN-15` | A divisão de responsabilidades com o provedor está documentada (o que é do provedor e o que é do auditado: certificados, DNS, CDN, backups, atualizações)? | 7 | `BAIXO` | — | `DOCUMENTAL` | arts. 46 e 50 |
| `IN-16` | Há processo de hardening e de gestão de vulnerabilidades da infraestrutura? | 7 | `MEDIO` | — | `TECNICO` | art. 46 |

Avaliados em outros módulos, sem item próprio aqui:
- contrato de operador (DPA) com o provedor de hospedagem: `GV-09` (`governance/dpo-framework.md`);
- transferência internacional pela região de hospedagem ou de armazenamento: itens `TI` (`legal/international-transfer.md`);
- dados pessoais reais em ambientes não produtivos: `DS-11` (`devsecops/ci-cd-security.md`).

## Critérios de evidência
- políticas IAM e evidências de revisão;
- configuração de bucket/object storage;
- evidência de uso de KMS/secret manager;
- trilhas de auditoria cloud habilitadas;
- configuração de retenção, acesso e destino das ferramentas de logs/observabilidade;
- regras de firewall/security groups;
- cabeçalhos HTTP coletados das respostas de produção (ex.: `curl -I`) comparados com a configuração do código;
- configurações e termos do provedor de PaaS ou hospedagem (analytics nativo, logs, região, DPA).

## Mapeamento para severidade e score
- Exposição pública de dado pessoal/sensível: `CRITICO`.
- Hospedagem ou CDN que remove ou enfraquece cabeçalhos de segurança configurados no código, ou injeta rastreamento sem base legal: `ALTO`.
- Acesso excessivo e ausência de trilha de auditoria: `ALTO`.
- Banco de dados, backup ou réplica com dados pessoais sem criptografia em repouso: `ALTO`.
- Logs com dados pessoais exportados a terceiros sem contrato de operador ou sem mecanismo do art. 33: `ALTO`.
- Logs de observabilidade sem política de retenção: `MEDIO`.
- Registros de acesso a aplicações sem guarda de 6 meses, sem porta lógica ou retidos além do prazo sem base legal: `MEDIO`.
- Falhas pontuais de hardening: `MEDIO`.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `infraestrutura` (domínio 7); `IN-13` pontua em `governanca` (domínio 14). A criticidade de cada item está na tabela do checklist.
