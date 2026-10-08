# Checklist: Prova Digital

> Referência para avaliação de provas em formato eletrônico.
> Base legal: CPP arts. 158-A a 158-F, Marco Civil (Lei 12.965/2014), LGPD (Lei 13.709/2018).

## Hierarquia de Confiabilidade

| Nível | Tipo | Confiabilidade |
|-------|------|----------------|
| 1 | Extração forense completa (imagem forense com hash) | Máxima |
| 2 | Ata notarial (Lei 8.935/94, art. 7º, III) | Alta |
| 3 | Registro em blockchain | Alta |
| 4 | Plataformas de registro (Verifact, OriginalMy) | Boa |
| 5 | Print/screenshot simples | Mínima |

## Checklist de Avaliação

### A. Autenticidade
- [ ] Hash calculado no momento da coleta?
- [ ] Algoritmo de hash (SHA-256 preferido, MD5 complementar)?
- [ ] Hash registrado em ata ou documento formal?
- [ ] Certificação digital ou assinatura eletrônica?
- [ ] Metadados (criação, modificação, autor) consistentes?

### B. Integridade
- [ ] Hash verificado antes da análise pericial?
- [ ] Comparação de hash entre coleta e análise?
- [ ] Imagem forense (clonagem bit a bit) realizada?
- [ ] Dispositivo original preservado?

### C. Cadeia de Custódia Digital
- [ ] Coleta por perito qualificado?
- [ ] Passos de manuseio documentados?
- [ ] Registro de quem acessou, quando e o quê?
- [ ] Dispositivos/mídias lacrados e armazenados adequadamente?
- [ ] Quebra na cadeia? Impacto?

### D. Licitude da Obtenção
- [ ] Respeitou direitos fundamentais (privacidade, sigilo)?
- [ ] Autorização judicial (quando necessária)?
- [ ] Legislação aplicável (Lei 9.296/96, Marco Civil, LGPD)?
- [ ] Consentimento do titular (quando aplicável)?

### E. Por Tipo Específico
- [ ] Mensagens de app: extração forense ou mero print?
- [ ] Print: ata notarial ou plataforma verificável?
- [ ] E-mail: headers preservados?
- [ ] Geolocalização: margem de precisão?
- [ ] Gravação: indicação de edição ou corte?

### F. Classificação

| Classificação | Critério |
|---------------|----------|
| **ALTA** | Extração forense + hash + cadeia íntegra + lícita |
| **MÉDIA** | Ata notarial OU plataforma de registro + sem quebra |
| **BAIXA** | Print simples OU cadeia comprometida OU sem hash |
| **INADMISSÍVEL** | Obtida ilicitamente sem exceção aplicável |

## Referências
- Lei 13.964/2019 (cadeia de custódia digital)
- Marco Civil da Internet (Lei 12.965/2014)
- LGPD (Lei 13.709/2018)
- STJ, decisões sobre prints de WhatsApp (2026)
