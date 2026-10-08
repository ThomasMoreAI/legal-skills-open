# 12: Transparência Radical (Portal /transparencia + Inventário Público + Geração Programática)

> **Tese:** Política de Privacidade é o **piso legal**. Portal de Transparência é o **teto competitivo**. Você entrega o que o concorrente esconde, não porque é obrigado, mas porque é honesto.

## Diferença Política × Portal de Transparência

| | Política de Privacidade | Portal de Transparência |
|---|---|---|
| Forma | Texto jurídico corrido | Estruturado, navegável, filtrável |
| Público | Advogado/regulador | Usuário curioso, jornalista, investidor, auditor |
| Atualização | Quando muda algo material | Continuamente (gerada do código) |
| Versionamento | Histórico de versões | Diff vivo + relatório anual |
| Obrigatoriedade | LGPD art. 9º | Voluntária, vira diferencial |

A Política é o "piso". O Portal é o "teto": diferencia você do concorrente que esconde.

---

## 1. Anatomia do Data Inventory público

Estrutura mínima (Apple Nutrition Labels + Google Data Safety + DCAT):

```yaml
categoria: "Identificadores"
itens:
  - nome: "E-mail"
    finalidade: ["autenticação", "comunicação transacional"]
    base_legal_lgpd: "execução de contrato (art. 7º V)"
    obrigatorio: true
    coletado_de: "formulário de cadastro"
    armazenado_em: "Postgres (provedor X, região UE)"
    retencao: "até exclusão da conta + 5 anos (CDC art. 27)"
    compartilhado_com:
      - terceiro: "Resend"
        finalidade: "envio de e-mail transacional"
        pais: "UE (Dublin)"
        salvaguarda: "Decisão de adequação ANPD Res. 32/2026"
        link_politica: "https://resend.com/legal/privacy-policy"
    sensibilidade: "baixa"
    pii: true
    visivel_para:
      - "próprio titular"
      - "admin (auditoria)"
    historico:
      - "2026-02-10: adicionado"
      - "2026-04-03: passou a ser compartilhado com Resend (antes: SMTP próprio)"
```

**Campos obrigatórios:**

1. **O quê**, nome técnico + nome humano (`user.email_hash` → "Hash do e-mail pra deduplicação")
2. **Por quê**, finalidade específica, não genérica
3. **Base legal**: LGPD art. 7º ou 11, explícita
4. **Quanto tempo**, em dias/anos, não "pelo tempo necessário"
5. **Com quem**, operadores + link pra política deles
6. **Sensibilidade**, baixa/média/alta/crítica
7. **Onde mora fisicamente**, datacenter + país
8. **Quem dentro da empresa enxerga**, role-based
9. **Histórico**, toda mudança datada

**Filtragem por persona**, "sou visitante anônimo" / "usuário logado" / "admin" / "titular menor". User escolhe, vê só o aplicável.

**Indicação visual de risco:** semáforo por categoria. Verde = só operacional. Amarelo = identifica indiretamente. Vermelho = dado sensível ou de menor. Roxo = perfil/inferência algorítmica.

---

## 2. Formato Apple Privacy Nutrition Labels: adaptado pro BR

Apple força declaração em **3 buckets**:

- **Data Used to Track You**, usado pra te seguir entre apps/sites
- **Data Linked to You**, vinculado à identidade no app
- **Data Not Linked to You**, coletado mas não vinculado (anônimo)

Dentro disso, **14 categorias canônicas**: Contact Info, Health & Fitness, Financial Info, Location, Sensitive Info, Contacts, User Content, Browsing History, Search History, Identifiers, Purchases, Usage Data, Diagnostics, Other Data.

### Replicar fora da App Store

Componente `<NutritionLabel>` que renderiza grid 3×N no topo de `/transparencia`. Cada célula clicável → leva pro item detalhado. Iconografia universal (Lucide ou Apple HIG).

**Adaptação BR:**
- Adicionar bucket **"Dados Sensíveis LGPD"** (art. 11), exige consentimento específico
- Adicionar bucket **"Dados de Crianças e Adolescentes"** (art. 14)
- Substituir "Data Used to Track You" por **"Dados Compartilhados com Anunciantes/Trackers"**, mais inteligível ao leigo BR

**Versão honesta:** se o app não coleta nada de uma categoria, mostra **bucket vazio com checkmark verde** "Nada coletado aqui". Concorrente que coleta vai parecer pesado ao lado do seu vazio.

---

## 3. Formato Google Play Data Safety

Schema similar, 3 eixos:
- **Data collected**, o que pega
- **Data shared**, o que passa adiante (subset com terceiros nomeados)
- **Security practices**, declarações auditáveis:
  - [x] Dados criptografados em trânsito (TLS 1.3)
  - [x] Dados criptografados em repouso (AES-256)
  - [x] Você pode pedir exclusão (link pro endpoint)
  - [x] Auditoria independente realizada (link pro report)
  - [x] Aderente ao MASVS / OWASP ASVS

Cada checkbox tem **prova** (link pro report, screenshot SSL Labs A+, endpoint `/api/conta/exclusao`). Sem prova → não marca.

---

## 4. Transparency Report Anual

Modelo Google/Meta/Twitter/GitHub. Uma vez por ano (ou semestral). URL `/transparencia/relatorio-2026`.

### Seções

**1. Requisições de autoridades**
- Quantas (Polícia, MP, Justiça, Receita)
- Atendidas / Recusadas / Parciais
- Por motivo (ordem judicial, requisição administrativa, ofício)
- Quantos titulares afetados
- Política do app: notifica titular? (recomendado: sim, salvo sigilo judicial)

**2. Exercício de direitos do titular (LGPD art. 18)**

| Direito | Recebidas | Atendidas | Tempo médio | Recusadas |
|---|---|---|---|---|
| Confirmação | 12 | 12 | 2,3d | 0 |
| Acesso | 8 | 8 | 4,1d | 0 |
| Correção | 3 | 3 | 1,5d | 0 |
| Anonim./Bloq./Eliminação | 47 | 45 | 6,2d | 2 (litígio) |
| Portabilidade | 1 | 1 | 9,0d | 0 |
| Revogação consentimento | 22 | 22 | <1d | 0 |

**3. Incidentes de segurança**
Lista pública: **mesmo os não comunicados à ANPD**. Pra cada: data, duração, vetor, dados afetados, n. titulares, ação, comunicação ANPD (sim/não, processo), comunicação aos titulares, lições aprendidas.

**4. Conteúdo removido (se UGC)**
Por categoria de motivo (notice & takedown, DMCA, ordem judicial, denúncia, moderação proativa).

**5. IA e decisões automatizadas**
- Quantas decisões automatizadas no ano
- Quantas revisadas após pedido
- Em quantas a revisão mudou resultado
- Taxa de erro estimada

**6. Métricas de operação**
- Uptime
- MTTR de incidentes
- % de dependências com CVE crítica patcheada em <7 dias
- Resultado da última auditoria de pentest

---

## 5. Data Card por Dataset Publicado

Quando o app publica **dados abertos** (govtech, acadêmico). Padrão híbrido: **DCAT W3C + Google Dataset Search + Datasheets for Datasets** (Gebru et al., 2018).

```yaml
dataset_id: "cobertura-vacinal-municipios-2015-2024"
titulo: "Cobertura vacinal por município, 2015-2024"
descricao: "Dados do SI-PNI agregados por município e imunobiológico (...)"
fonte_primaria:
  - nome: "SI-PNI/DATASUS"
    url: "https://datasus.saude.gov.br/..."
    data_extracao: "2026-03-15"
schema:
  - campo: "municipio_ibge"
    tipo: "string(7)"
    descricao: "Código IBGE do município"
    completude: 100.0
  - campo: "cobertura_pct"
    tipo: "float"
    descricao: "% da população-alvo imunizada"
    completude: 99.7
granularidade_temporal: "anual"
granularidade_espacial: "municipal"
periodicidade_atualizacao: "anual (até abril do ano seguinte)"
ultima_atualizacao: "2026-04-12"
proxima_atualizacao: "2027-04-15"
licenca: "CC-BY 4.0"
citacao_sugerida: "{{AUTOR}} (2026). Cobertura vacinal por município (...). DOI:..."
anonimizacao:
  metodo: "agregação municipal (k-anonymity, k>=5)"
  risco_reidentificacao: "baixo"
limitacoes_conhecidas:
  - "Cobertura do SI-PNI <95% em alguns municípios do Norte"
  - "Mudança metodológica em 2019 (...)"
contato_responsavel: "dados@exemplo.com.br"
versao: "1.2.0"
formato_disponivel: ["CSV", "Parquet", "JSON", "API REST"]
endpoints:
  download: "https://app.com/dados/cobertura-vacinal.csv"
  api: "https://app.com/api/v1/cobertura-vacinal"
  documentacao: "https://app.com/api/docs"
```

Renderizar cada Data Card como **página dedicada + JSON-LD embedded** (schema.org/Dataset), aparece em Google Dataset Search e catálogos FAIR.

---

## 6. Estrutura de URLs do portal

```
/transparencia                          # hub
  /inventario                           # data inventory navegável
  /nutrition-label                      # versão Apple-style
  /terceiros                            # lista de operadores + DPAs
  /cookies                              # categorização + controles
  /ia                                   # model cards + system cards
  /retencao                             # política de retenção tabular
  /incidentes                           # histórico
  /seguranca                            # práticas + certificados
  /dados-abertos                        # data cards (se publica datasets)
  /relatorio/{ano}                      # transparency report
  /direitos                             # como exercer + endpoint
  /governanca                           # DPO, organograma, comitê
  /mudancas                             # changelog global
```

**Versionamento:** tudo em git público (pasta `transparencia/` no repo principal ou repo separado `<projeto>-transparencia`). Cada mudança = commit + entrada no `/mudancas`. URL com permalink: `/transparencia/inventario?v=2026-04-12`.

**Acessibilidade (WCAG 2.1 AA):** tabelas com headers, contraste 4.5:1, navegável por teclado, ARIA labels, modo escuro, fonte ≥16px, sem dependência de cor (semáforo = cor + ícone + texto).

**PDF anual:** gerar um one-pager executivo + versão completa. PDF tem **prazo de validade visível** ("válido pro exercício 2026").

---

## 7. Estudos de caso BR

| Empresa | Pontos fortes | Pontos fracos |
|---|---|---|
| **Nubank, "Tudo sobre seus dados"** | Navegável por categoria, linguagem direta, histórico visível, link pra parceiros | Sem model cards, sem report quantitativo anual |
| **Mercado Livre, "Centro de Privacidade"** | Bom em controles do titular (toggles) | Fraco em explicar terceiros caso a caso |
| **iFood, "Privacidade"** | Melhorou em 2023 | Ainda juridiquês; sem report quantitativo |
| **Stone / Pagar.me** | Publica SOC 2 e relatórios de segurança | - |
| **Gov Federal: Portal da Transparência + dados.gov.br** | Padrão LAI bem implementado | Focado em orçamento, não PII de usuário |
| **IBGE** | Padrão ouro de metadados/dicionário/licenciamento | - |
| **ANPD** | Publica sancionados pelo nome (vergonha pública é parte da política) | - |

**Lição:** quem cumpre LGPD pode usar isso a favor (selo, marketing).

---

## 8. Riscos da transparência radical (honestidade obriga)

1. **Engenharia social facilitada.** Atacante sabe quais dados você tem. Mitigação: descrever **categorias**, não **segredos operacionais**; nunca expor versão exata de tecnologia não patcheada.
2. **Concorrência usar contra você.** "Olha quanto eles coletam!" mesmo o seu sendo menor. Mitigação: comparativo lado a lado quando concorrente publicar; narrativa clara do *porquê* coleta.
3. **Manutenção contínua (drift).** Código muda, declaração não acompanha → mentira pública = passivo maior. **Mitigação central: automação CI/CD** (seção 10).
4. **Compromisso difícil de reverter.** Prometeu 30d e precisa de 90 → trabalho de comunicação. Mitigação: margem de segurança + `/mudancas` justificando.
5. **Sobrecarga cognitiva.** Info demais = ninguém lê. Mitigação: **camadas** (nutrition label → inventário → raw data).
6. **Aumento de pedidos de titular.** Facilitar = mais gente pede. Mitigação: **automatize** endpoints (Parte 1 LGPD já faz); ver como sinal de saúde.

---

## 9. Princípios FAIR aplicados

Pra dados publicados, seguir **FAIR**:

- **F**indable: JSON-LD schema.org, sitemap, catalogado em DCAT
- **A**ccessible, formato aberto (CSV, JSON, Parquet), licença clara, endpoint estável
- **I**nteroperable, padrões abertos, sem vendor lock-in
- **R**eusable, licença permissiva (CC-BY 4.0 default), documentação completa

Vale pra qualquer projeto que publique dados abertos.

---

## 10. Geração programática (a parte que diferencia amador de pro)

**Manifesto à mão envelhece em duas sprints.** O manifesto tem que ser **gerado pelo código**, não pelo jurídico.

### 10.1. Anotação no código

Cada campo de PII no schema ganha **anotação estruturada**.

**Postgres (`COMMENT ON COLUMN`):**

```sql
COMMENT ON COLUMN users.email IS
  '@pii @finalidade=auth,transacional @base=contrato @retencao=conta+5y @sensibilidade=baixa @compartilha=resend';
```

**Python (decorator):**

```python
from lgpd_compliance import pii

class User(Base):
    @pii(
        finalidade=["auth", "transacional"],
        base_legal="contrato",
        retencao="conta+5y",
        sensibilidade="baixa",
        compartilha_com=["resend"]
    )
    email: Mapped[str] = mapped_column(String(255))
```

**TypeScript (decorator via JSDoc ou comment):**

```typescript
// @pii(finalidade=[auth,transacional], base=contrato, retencao=conta+5y, sensibilidade=baixa, compartilha=resend)
email: string;
```

### 10.2. Extrator → inventário

Script `scripts/gerar-inventario.py` (ou TS) que:

1. Lê schema do banco (`COMMENT ON COLUMN ...`)
2. Lê anotações de código (decorators, comments)
3. Lê `transparencia/terceiros.yaml` (operadores)
4. Lê `transparencia/finalidades.yaml`
5. Gera `transparencia/inventario.json` (canônico)
6. Renderiza páginas estáticas a partir do JSON

Template em `templates/transparencia/automation/`.

### 10.3. CI/CD validando drift

GitHub Action `transparency-check.yml` (template em `templates/transparencia/automation/`):

- Roda em todo PR
- **Falha** se existe campo no schema sem anotação `@pii` (em tabela `@contains_pii`)
- **Falha** se `@compartilha=X` onde X não está em `terceiros.yaml`
- **Falha** se versão do inventário não foi bumped quando PR mexe em schema
- **Posta comentário** no PR com diff do inventário público

### 10.4. Detecção de drift em runtime

Job semanal:
- Compara inventário declarado com:
  - **Logs reais** de requisição (egress: `resend.com`, `stripe.com`, todos no inventário?)
  - **Egress de rede** do container
  - Schema vivo do banco vs schema declarado
- Abre **issue automática** se houver drift

### 10.5. Endpoint vivo

```
GET /api/transparencia/inventario.json
```

Retorna inventário canônico. Permite ferramentas externas (auditor ANPD, jornalista, agregador) consumir. JSON-LD com schema.org pra SEO.

### 10.6. Tests as documentation

Testes nomeados `test_lgpd_*` verificam comportamento prometido:

- `test_lgpd_email_nao_compartilhado_com_meta`, bloqueia regressão futura
- `test_lgpd_exclusao_conta_remove_dados_em_30d`
- `test_lgpd_exportacao_inclui_todos_campos_pii`

Cada teste = **prova viva** da promessa pública.

---

## Síntese: o diferencial

Concorrente brasileiro médio:
- Política copiada de template
- Banner genérico que aceita tudo no X
- Esconde lista de terceiros
- Não publica incidente
- Não tem transparency report
- Não anota código

Com esse playbook:
- Nutrition Label de PII na home `/transparencia`
- Inventário navegável **gerado do código**
- Lista pública de terceiros com link pra DPA de cada
- Transparency report anual com números
- Data cards DCAT pra cada dataset publicado
- Model cards pra cada feature de IA
- Endpoints LGPD funcionais e medidos
- **CI/CD travando drift**
- PDF anual one-pager pra diretoria/comitê/ANPD

Vira **selo de marca**. Diferença visível em 30 segundos. E quando ANPD bater, **defesa já está construída, datada, versionada em git público**.

## Referências externas

- [Apple App Privacy Details](https://developer.apple.com/app-store/app-privacy-details/)
- [Google Play Data Safety](https://support.google.com/googleplay/android-developer/answer/10787469)
- [Datasheets for Datasets (Gebru et al. 2018)](https://arxiv.org/abs/1803.09010)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [FAIR Principles](https://www.go-fair.org/fair-principles/)
- [Schema.org Dataset](https://schema.org/Dataset)
- [Portal da Transparência (Gov BR)](https://portaldatransparencia.gov.br/)
- [dados.gov.br](https://dados.gov.br/)
- [Nubank (Privacidade)](https://nubank.com.br/transparencia/)
