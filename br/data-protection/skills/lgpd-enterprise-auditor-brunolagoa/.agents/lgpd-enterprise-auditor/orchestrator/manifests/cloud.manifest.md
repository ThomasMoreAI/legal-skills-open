# Manifesto — `cloud`

- `module`: cloud
- `required`: false
- `files`: `cloud/cloud-audit.md`
- `inputs`: provedor cloud, storage, IAM, rede, trilha de auditoria
- `prerequisites`: core, legal
- `activates_when`: AWS/Azure/GCP, Firebase, dados em storage cloud
- `primary_outputs`: riscos de exposição, IAM, hardening e observabilidade cloud, incluindo retenção, acesso e exportação de logs a terceiros
