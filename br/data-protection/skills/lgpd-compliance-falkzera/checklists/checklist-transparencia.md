# Checklist: Portal de Transparência (Parte 3)

> Validação do `<projeto>/transparencia/` antes de publicar. Cruzar com `references/11-taxonomia-dados.md`, `12-transparencia-radical.md`, `13-ia-ml-transparencia.md`, `14-analytics-tracking.md`.

## A. Inventário público

- [ ] `transparencia/inventario.yaml` existe e tem `meta.versao`, `meta.data_atualizacao`, `meta.dpo_contato`
- [ ] Pra cada categoria coletada: `itens` preenchido com finalidade, base legal, retenção, sensibilidade
- [ ] Categoria **não coletada** marcada com `aplicavel: false` + `declaracao_publica` explicando
- [ ] Cada item tem `finalidade` que existe em `finalidades.yaml`
- [ ] Cada `compartilhado_com` existe em `terceiros.yaml`
- [ ] Versão bumped a cada mudança material

## B. Lista de terceiros

- [ ] `transparencia/terceiros.yaml` existe com TODOS os operadores
- [ ] Pra cada: `nome_legal`, `finalidade`, `dados_compartilhados`, `pais_processamento`, `base_transferencia`, `link_dpa`, `link_politica_privacidade`, `data_dpa_assinado`, `contato_incidente`
- [ ] Base de transferência declarada explicitamente:
  - [ ] UE → "Decisão de adequação ANPD Res. 32/2026"
  - [ ] EUA / outros → "SCC ANPD (Res. 19/2024)"
  - [ ] BR → "Não aplicável"
- [ ] DPA assinado **antes** do go-live de cada operador
- [ ] Revisão trimestral agendada

## C. Catálogo de finalidades

- [ ] `transparencia/finalidades.yaml` existe
- [ ] Cada finalidade tem `nome_publico`, `descricao`, `base_legal_lgpd`
- [ ] Finalidades de **legítimo interesse** têm `teste_balanceamento` (link pro RIPD)
- [ ] Finalidades de **consentimento** têm `requer_opt_in: true`

## D. Portal /transparencia

- [ ] Rota `/transparencia` publicada e linkada do rodapé
- [ ] Hub com `<NutritionLabel>` no topo (Apple-style)
- [ ] Grade de sub-páginas habilitadas conforme escopo do app
- [ ] Cada sub-página renderiza a partir do YAML correspondente
- [ ] **Endpoint vivo:** `GET /api/transparencia/inventario.json` retorna o canônico
- [ ] Versão e data de atualização visíveis no header
- [ ] Acessibilidade WCAG 2.1 AA (contraste, ARIA, navegação por teclado)

## E. Nutrition Label

- [ ] 3 buckets: Não Vinculados, Vinculados, Sensíveis (LGPD art. 11)
- [ ] Bucket vazio mostra **checkmark verde** "Nada coletado aqui"
- [ ] Cada categoria com ícone, nome, contagem de itens, indicador de sensibilidade (cor + texto)
- [ ] Clique leva pra `/transparencia/inventario#categoria`

## F. Transparência sobre IA (se app usa IA)

- [ ] `/transparencia/ia` listando cada modelo usado
- [ ] **Model card** por modelo em `transparencia/ia/{provedor}-{modelo}.md`
- [ ] Política de treinamento/retenção de cada provedor declarada:
  - [ ] **OpenAI API:** não treina; 30d retenção (ou ZDR Enterprise)
  - [ ] **Anthropic Claude API:** nunca treina; 7d retenção
  - [ ] **Gemini API tier pago:** não treina
  - [ ] **Gemini free tier:** ⚠️ TREINA + revisão humana, migrar pro pago OU consentimento específico
- [ ] DPA assinado com cada provedor de IA
- [ ] Sanitização de PII antes de enviar (Microsoft Presidio ou similar) declarada
- [ ] `<AIBadge>` ou `<AIDisclosure>` em todo output de IA
- [ ] Botão "Contestar esta decisão" visível em decisões automatizadas (art. 20)
- [ ] Endpoint `POST /decisoes/{id}/contestar` implementado
- [ ] Disclaimer "não usar pra diagnóstico/parecer/decisão financeira" presente

## G. Dados abertos (se publica datasets)

- [ ] `/transparencia/dados-abertos` com lista de datasets
- [ ] **Data Card** por dataset em `transparencia/datasets/{id}.yaml` (formato DCAT + Datasheets)
- [ ] JSON-LD `schema.org/Dataset` embedded em cada página de dataset (pra Google Dataset Search)
- [ ] Licença declarada (CC-BY 4.0 default)
- [ ] Citação sugerida + DOI quando aplicável
- [ ] Anonimização documentada (método + risco de re-identificação)

## H. Transparency Report anual

- [ ] `/transparencia/relatorio/{ANO}` publicado anualmente
- [ ] Cobre: requisições de autoridades, exercício de direitos do titular, incidentes, takedowns, IA, métricas operacionais
- [ ] Números gerados a partir das tabelas (`consent_log`, `dsr_request`, `audit_log`, `notice_takedown`) por script
- [ ] Pra categorias com <5 ocorrências: suprimir ou agregar (k-anonimato k=5)
- [ ] Compromissos pro próximo exercício listados

## I. Geração programática

- [ ] **Convenção de anotação `@pii`** publicada em `transparencia/PII_CONVENTION.md` (cópia de `pii-convention.md`)
- [ ] Schema do banco anotado com `COMMENT ON COLUMN ... '@pii ...'` em cada tabela `@contains_pii`
- [ ] (Se Python) decorator `@pii(...)` e `@contains_pii` aplicados
- [ ] `scripts/gerar-inventario.py` instalado e funcional
- [ ] `.github/workflows/transparency-check.yml` ativo no repo
- [ ] CI falha PR que:
  - [ ] tem campo sem `@pii` em tabela `@contains_pii`
  - [ ] usa `@compartilha=X` onde X não está em `terceiros.yaml`
  - [ ] usa `@finalidade=X` onde X não está em `finalidades.yaml`
  - [ ] mexe em schema sem bump de `inventario.yaml#versao`
- [ ] Job semanal de **detecção de drift em runtime** (compara declarado vs egress real)

## J. Stack default privacy-first

Pra projeto novo (ou auditoria de existente), checar se está usando defaults recomendados:

- [ ] **Analytics web:** Plausible (não GA4), sem cookie, sem consentimento de cookie
- [ ] **Product analytics:** PostHog EU sem replay (default), com masking se replay
- [ ] **Error tracking:** Sentry EU com `beforeSend` agressivo, sem PII em stack
- [ ] **Logs/APM:** Grafana Cloud EU ou BetterStack
- [ ] **E-mail transacional:** Postmark ou Resend EU
- [ ] **CRM/marketing:** RD Station (brasileira, cláusulas ANPD nativas)
- [ ] **Chat:** Crisp (Amsterdam) ou Chatwoot self-hosted
- [ ] **CMP:** GoAdopt (BR) ou klaro (open-source)

Se está usando GA4/Hotjar/Intercom-US, plano de migração documentado.

## K. Tests as documentation

- [ ] Testes nomeados `test_lgpd_*` verificam promessas públicas:
  - [ ] `test_lgpd_email_nao_compartilhado_com_meta`
  - [ ] `test_lgpd_exclusao_conta_remove_dados_em_30d`
  - [ ] `test_lgpd_exportacao_inclui_todos_campos_pii`
  - [ ] `test_lgpd_ip_truncado_antes_de_log`
  - [ ] `test_lgpd_pii_redaction_antes_de_enviar_pra_ai`

## L. Auditoria periódica

A cada **trimestre**:

- [ ] Rodar **DevTools** em aba anônima, navegar fluxos críticos, identificar hosts third-party
- [ ] Rodar scanner (**Cookiebot scanner**, **Blacklight**, **PrivacyScore**)
- [ ] Comparar **diff trimestral** da lista de processadores vs scan
- [ ] Revisar `beforeSend` / `sanitize` se houve release que adicione campo no DOM
- [ ] **Testar fluxo "rejeitar todos"**, nenhum script third-party pode disparar

A cada **release que mexe em schema**:

- [ ] CI valida automaticamente (já garantido pelo workflow)
- [ ] PR atualiza `inventario.yaml#versao` + entrada em `/mudancas`

A cada **ano**:

- [ ] Publicar transparency report
- [ ] Auditoria de segurança independente (pentest, SOC 2 se cabível)
- [ ] Revisão geral de todos os DPAs

## M. Output final

Quando tudo estiver marcado:

- [ ] **Repositório:**
  - `<projeto>/transparencia/inventario.yaml`
  - `<projeto>/transparencia/terceiros.yaml`
  - `<projeto>/transparencia/finalidades.yaml`
  - `<projeto>/transparencia/PII_CONVENTION.md`
  - `<projeto>/transparencia/ia/*.md` (se aplica)
  - `<projeto>/transparencia/datasets/*.yaml` (se aplica)
  - `<projeto>/transparencia/relatorios/*.md`
  - `<projeto>/app/(transparencia)/page.tsx`
  - `<projeto>/components/transparencia/NutritionLabel.tsx`
  - `<projeto>/components/transparencia/AIDisclosure.tsx`
  - `<projeto>/scripts/gerar-inventario.py`
  - `<projeto>/.github/workflows/transparency-check.yml`
- [ ] **URL canônica:** `https://app.com/transparencia` indexável
- [ ] **Link no footer** em todas as páginas
- [ ] **Mencionado na Política de Privacidade** ("Para detalhes técnicos, ver Portal de Transparência")
- [ ] **Mencionado nos Termos de Uso** quando referencia ferramentas
- [ ] **Commit:** `chore(legal): publica Portal de Transparência vYYYY-MM-DD`
