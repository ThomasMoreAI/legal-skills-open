# Roteamento de Skills Filhas

| Skill | Quando invocar | Outputs em `.lgpd/` |
|---|---|---|
| `lgpd-legal-basis` | Decidir base legal de cada atividade de tratamento | `legal-basis.md` |
| `lgpd-data-mapping` | Inventariar fluxos de dados pessoais | `data-map.md` |
| `lgpd-ropa` | Consolidar Registro de Operações (Art. 37) | `ROPA.md` |
| `lgpd-ripd` | Avaliação de impacto para alto risco (Art. 38) | `RIPD/ripd-{slug}.md` |
| `lgpd-consent-schema` | Modelar consent ledger no banco (Prisma) | `consent/schema.prisma`, `consent/spec.md` |
| `lgpd-dsar` | Implementar endpoints de exercício de direitos (Art. 18) | `dsar/workflow.md`, `dsar/endpoints.md` |
| `lgpd-audit-logging` | Log imutável encadeado | `audit-logging.md` |
| `lgpd-encryption-keys` | TDE, KMS, rotação | `security/encryption.md` |
| `lgpd-anonymization` | Técnicas de anonimização e pseudonimização | `security/anonymization.md` |
| `lgpd-retention-erasure` | Políticas de retenção + crypto-shredding | `retention.md` |
| `lgpd-incident-response` | Runbook + comunicação ANPD (3 dias úteis) | `incidents/runbook.md`, `incidents/log.md` |
| `lgpd-privacy-policy` | Política conforme Art. 9 | `policies/privacy-policy-v{N}.md` |
| `lgpd-dpo-encarregado` | Designar e publicar Encarregado | `encarregado.md` |
| `lgpd-dpa` | DPA com operadores (Art. 39) | `vendors/dpa-template.md`, `vendors/{vendor}.md` |
| `lgpd-international-transfer` | Cláusulas-padrão (Res. 19/2024) | `transfers/{vendor}.md` |
| `lgpd-vendor-audit` | Due diligence em operadores | `vendors/audit-{date}.md` |
| `lgpd-eca-digital-minors` | Plataformas com menores (Lei 15.211/2025) | `eca-digital.md` |
| `lgpd-legacy-retrofit` | Gap analysis em sistema legado | `gaps.md` |

## Ordem de prioridade (se tempo for limitado)

1. `lgpd-legal-basis` — sem base legal não há tratamento legítimo
2. `lgpd-data-mapping` — sem mapa não há ROPA, RIPD, nem retenção
3. `lgpd-privacy-policy` — exposição imediata ao titular
4. `lgpd-dsar` — direitos do titular = topo da agenda ANPD
5. `lgpd-incident-response` — pode ser acionado a qualquer momento
6. `lgpd-dpo-encarregado` — comunicação com ANPD e titulares
7. Resto

## Dependências entre skills

- `lgpd-ropa` requer `lgpd-data-mapping` + `lgpd-legal-basis`
- `lgpd-ripd` requer `lgpd-ropa` + identificação de alto risco
- `lgpd-dpa` requer `lgpd-vendor-audit`
- `lgpd-international-transfer` requer `lgpd-vendor-audit`
- `lgpd-eca-digital-minors` é independente mas afeta `lgpd-privacy-policy` e `lgpd-consent-schema`
