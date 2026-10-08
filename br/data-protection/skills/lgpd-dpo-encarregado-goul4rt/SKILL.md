---
name: lgpd-dpo-encarregado-goul4rt
title: Encarregado / DPO (Art. 41 LGPD + Res. 18/2024)
description: Designate and publish the Encarregado (DPO) per LGPD Art. 41 + Resolução CD/ANPD nº 18/2024. Use when user asks 'designar DPO', 'encarregado LGPD', 'quem é o DPO', or as part of audit pipeline. Note ATPP exemption (Res. 2/2022 Art. 11) but recommend designation anyway as best practice.
author: goul4rt
author_url: https://github.com/goul4rt/lgpd-skills/tree/main/skills/lgpd-dpo-encarregado
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# Encarregado / DPO (Art. 41 LGPD + Res. 18/2024)

## Quem pode ser

- **Pessoa natural OU pessoa jurídica** (Res. 18/2024, Art. 3º + 12)
- Não precisa de certificação formal
- Não precisa residir no Brasil
- Pode ser interno ou externo (outsourced DPO é prática comum em ATPP)
- **Vedado conflito de interesse** (Res. 18/2024, Art. 2º, II) — diretor jurídico ou de TI pode ter conflito; avaliar

## Atribuições mínimas (Art. 41, § 2º)

1. Aceitar reclamações e comunicações dos titulares
2. Receber comunicações da ANPD
3. Orientar funcionários e contratados sobre práticas
4. Executar demais atribuições do controlador

## Atribuições expandidas (Res. 18/2024, Arts. 15-16)

- Auxiliar na elaboração de ROPA, RIPD, DPAs
- Auxiliar na comunicação de incidentes
- Auxiliar em transferência internacional
- Auxiliar no programa de governança em privacidade (Art. 50 LGPD)
- Promover privacy-by-design

## Divulgação obrigatória

- **No site, em local de destaque** (Res. 18/2024, Art. 9º)
- Nome completo (se PF) ou nome empresarial + responsável técnico (se PJ)
- Canal de contato (e-mail é o mínimo; portal é melhor)
- Em PT-BR (Res. 18/2024, Art. 13)
- Não é necessário comunicar a ANPD proativamente — ato formal deve estar disponível "quando solicitado" (Res. 18/2024, Art. 3º, § 2º)

## ATPP — dispensa formal

Res. 2/2022, Art. 11 dispensa designação para ATPP de baixo risco, mas exige **canal de comunicação**. Recomendação: designar mesmo assim — custo baixo, proteção alta.

## Template — `.lgpd/encarregado.md`

```markdown
# Encarregado pela Proteção de Dados

**Designado por**: {ato formal — ata, contrato, resolução}
**Data de designação**: {data}
**Tipo**: PF / PJ
**Nome**: {nome completo ou nome empresarial}
**Responsável técnico** (se PJ): {nome}
**Contato**:
- E-mail: encarregado@dominio.com.br
- Telefone: (XX) XXXX-XXXX
- Portal: https://dominio.com.br/encarregado

**Atribuições conferidas**: ver Res. 18/2024 + atribuições internas definidas no anexo

**Conflito de interesse avaliado em**: {data}
**Conclusão**: sem conflito identificado

**Divulgação**: publicada em https://dominio.com.br/privacidade#encarregado
```

## Status update

```markdown
## F11 — Encarregado ✓
- Designado: {nome}
- Tipo: PF/PJ
- Publicado em: {URL}
- Canal ativo: {e-mail}
- Próximo: lgpd-ripd (se alto risco) ou lgpd-vendor-audit
```
