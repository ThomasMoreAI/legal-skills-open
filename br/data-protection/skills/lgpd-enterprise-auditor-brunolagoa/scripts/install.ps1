# LGPD Enterprise Auditor — instalador local, por projeto (Windows PowerShell 5.1+ e PowerShell 7+).
# Equivalente ao scripts/install.sh: mesmas ações, opções, destinos e formato de manifesto.

param(
  [Parameter(Position = 0)]
  [ValidateSet("install", "update", "uninstall", "check")]
  [string]$Action = "install",
  [ValidateSet("claude", "cursor", "vscode", "opencode", "agents")]
  [string]$Target,
  [switch]$WithSkill,
  [switch]$NoSkill,
  [string]$ProjectDir,
  [string]$Version,
  [string]$Repo = "BrunoLagoa/lgpd-enterprise-auditor",
  [switch]$NonInteractive,
  [switch]$Help
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"

$script:SchemaVersion = "1"
$script:FrameworkRel = ".agents/lgpd-enterprise-auditor"
$script:StateRel = "$script:FrameworkRel/.install"
$script:SkillName = "lgpd-enterprise-auditor"
$script:ExitNotFound = 2
$script:SupportedTargets = @("claude", "cursor", "vscode", "opencode", "agents")
$script:Utf8NoBom = New-Object System.Text.UTF8Encoding $false

$script:SourceRoot = ""
$script:SourceRef = ""
$script:SourceVersion = ""
$script:TmpRoot = ""
$script:Skill = ""
if ($WithSkill -and $NoSkill) { Write-Host "[ERROR] Use apenas uma: -WithSkill ou -NoSkill." -ForegroundColor Red; exit 1 }
if ($WithSkill) { $script:Skill = "1" }
if ($NoSkill) { $script:Skill = "0" }

# ---------------------------------------------------------------------------
# Saída e interação
# ---------------------------------------------------------------------------

function Write-Info([string]$Message) { Write-Host "[INFO] $Message" -ForegroundColor Cyan }
function Write-Ok([string]$Message) { Write-Host "[OK] $Message" -ForegroundColor Green }
function Write-WarnLog([string]$Message) { Write-Host "[WARN] $Message" -ForegroundColor Yellow }

function Stop-WithError([string]$Message, [int]$Code = 1) {
  Write-Host "[ERROR] $Message" -ForegroundColor Red
  Remove-TempRoot
  exit $Code
}

function Read-Answer([string]$Prompt) {
  $answer = Read-Host $Prompt
  if ($null -eq $answer) { Stop-WithError "Entrada interativa indisponível. Use -NonInteractive." }
  return $answer
}

function Confirm-Choice([string]$Question, [string]$Default = "y") {
  $suffix = if ($Default -eq "y") { "[Y/n]" } else { "[y/N]" }
  $answer = Read-Answer "$Question $suffix"
  if ([string]::IsNullOrWhiteSpace($answer)) { $answer = $Default }
  return @("y", "yes", "s", "sim") -contains $answer.Trim().ToLowerInvariant()
}

function Select-Index([string]$Question, [string[]]$Options) {
  Write-Host $Question
  for ($i = 0; $i -lt $Options.Count; $i++) {
    Write-Host ("  {0}) {1}" -f ($i + 1), $Options[$i])
  }
  while ($true) {
    $answer = Read-Answer ("Selecione uma opção [1-{0}]" -f $Options.Count)
    $number = 0
    if ([int]::TryParse($answer, [ref]$number) -and $number -ge 1 -and $number -le $Options.Count) {
      return $number
    }
    Write-WarnLog "Opção inválida. Tente novamente."
  }
}

function Show-Banner([string]$Title) {
  Write-Host @"
 _     ____ ____  ____
| |   / ___|  _ \|  _ \
| |  | |  _| |_) | | | |
| |__| |_| |  __/| |_| |
|_____\____|_|   |____/
"@
  Write-Host ""
  Write-Host "LGPD Enterprise Auditor $Title"
  Write-Host ""
  Write-Host "Framework de auditoria de conformidade LGPD orientado a evidências, para usar com o seu"
  Write-Host "assistente de IA (Claude Code, Cursor, VS Code + Copilot, OpenCode, Codex, Gemini CLI)."
  Write-Host "A instalação é local: tudo fica dentro do projeto auditado."
  Write-Host ""
}

function Show-Usage {
  Write-Host @"
LGPD Enterprise Auditor — instalador

Uso:
  install.ps1 [install|update|uninstall|check] [opções]

Ações:
  install     Instala o framework e os comandos da ferramenta escolhida (padrão)
  update      Reinstala as ferramentas já instaladas na versão escolhida
  uninstall   Remove a instalação de uma ferramenta (ou de todas)
  check       Verifica a instalação do projeto

Opções:
  -Target <claude|cursor|vscode|opencode|agents>  Ferramenta (obrigatória com -NonInteractive no install)
  -WithSkill              Instala também a skill
  -NoSkill                Não instala a skill (padrão)
  -ProjectDir <dir>       Projeto de destino (padrão: raiz git do diretório atual)
  -Version <ref|local>    Tag, branch ou "local" (padrão: última tag publicada)
  -Repo <owner/repo>      Repositório GitHub (padrão: BrunoLagoa/lgpd-enterprise-auditor)
  -NonInteractive         Executa sem perguntas
  -Help                   Exibe esta ajuda
"@
}

# ---------------------------------------------------------------------------
# Ambiente
# ---------------------------------------------------------------------------

function Get-OsName {
  if ($PSVersionTable.PSVersion.Major -lt 6) { return "windows" }
  if ($IsWindows) { return "windows" }
  if ($IsMacOS) { return "macos" }
  return "linux"
}

function Get-IsoTimestamp { return (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ") }

# PowerShell 7 converte datas ISO do JSON em DateTime; o 5.1 mantém string.
function Format-Stamp($Value) {
  if ($Value -is [datetime]) { return $Value.ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ") }
  return [string]$Value
}

function Get-FullPath([string]$Path) {
  return [System.IO.Path]::GetFullPath((Resolve-Path -LiteralPath $Path).ProviderPath).TrimEnd('\', '/')
}

function Join-Rel([string]$Base, [string]$Rel) {
  return [System.IO.Path]::Combine($Base, ($Rel -replace '/', [System.IO.Path]::DirectorySeparatorChar))
}

function Resolve-ProjectDir {
  if ($ProjectDir) {
    if (-not (Test-Path -LiteralPath $ProjectDir -PathType Container)) { Stop-WithError "Diretório do projeto não encontrado: $ProjectDir" }
    $script:ProjectRoot = Get-FullPath $ProjectDir
  } else {
    $current = Get-FullPath (Get-Location).Path
    $script:ProjectRoot = $current
    while ($current) {
      if (Test-Path -LiteralPath (Join-Path $current ".git")) {
        $script:ProjectRoot = $current
        break
      }
      $parent = Split-Path -Parent $current
      if (-not $parent -or $parent -eq $current) { break }
      $current = $parent
    }
  }

  $homeDir = Get-FullPath $HOME
  $isRoot = ([System.IO.Path]::GetPathRoot($script:ProjectRoot).TrimEnd('\', '/') -eq $script:ProjectRoot)
  if ($isRoot -or $script:ProjectRoot -eq $homeDir) {
    Stop-WithError "Recusado instalar em $($script:ProjectRoot). Rode na raiz do projeto ou use -ProjectDir."
  }
}

function Remove-TempRoot {
  if ($script:TmpRoot -and (Test-Path -LiteralPath $script:TmpRoot)) {
    Remove-Item -LiteralPath $script:TmpRoot -Recurse -Force -ErrorAction SilentlyContinue
  }
}

# ---------------------------------------------------------------------------
# Ferramentas (targets)
# ---------------------------------------------------------------------------

function Get-TargetLabel([string]$Name) {
  switch ($Name) {
    "claude" { return "claude (Claude Code)" }
    "cursor" { return "cursor (Cursor)" }
    "vscode" { return "vscode (VS Code + GitHub Copilot)" }
    "opencode" { return "opencode (OpenCode)" }
    "agents" { return "agents (outra ferramenta: Codex, Gemini CLI e similares)" }
  }
}

function Get-TargetCommandsDir([string]$Name) {
  switch ($Name) {
    "claude" { return ".claude/commands" }
    "cursor" { return ".cursor/commands" }
    "vscode" { return ".github/prompts" }
    "opencode" { return ".opencode/commands" }
    default { return "" }
  }
}

function Get-TargetCommandFile([string]$Name, [string]$Stem) {
  if ($Name -eq "vscode") { return "$Stem.prompt.md" }
  return "$Stem.md"
}

function Get-TargetSkillDir([string]$Name) {
  if ($Name -eq "claude") { return ".claude/skills/$script:SkillName" }
  return ".agents/skills/$script:SkillName"
}

function Show-NextSteps([string]$Name, [string]$Skill) {
  Write-Host ""
  Write-Host "Próximos passos"
  switch ($Name) {
    "claude" { Write-Host "  Abra o Claude Code na raiz do projeto (claude) e rode /lgpd-saas, /lgpd-full-audit etc." }
    "cursor" { Write-Host "  No chat do Cursor, digite /lgpd-saas, /lgpd-full-audit etc." }
    "vscode" { Write-Host "  No Copilot Chat do VS Code, digite /lgpd-saas, /lgpd-full-audit etc." }
    "opencode" { Write-Host "  Rode opencode na raiz do projeto e use /lgpd-saas, /lgpd-full-audit etc." }
    "agents" { Write-Host "  Peça ao seu agente: `"faça uma auditoria LGPD deste projeto`" — ele carrega a skill $script:SkillName." }
  }
  if ($Skill -eq "1" -and $Name -ne "agents") {
    Write-Host "  Com a skill instalada, você também pode pedir a auditoria em linguagem natural."
  }
  Write-Host "  Coloque política de privacidade, RIPD, contratos (DPA) e nomeação do DPO dentro do projeto"
  Write-Host "  (ex.: docs/lgpd/) para que contem como evidência documental."
}

function Write-TextFile([string]$Path, [string[]]$Lines) {
  [System.IO.File]::WriteAllText($Path, (($Lines -join "`n") + "`n"), $script:Utf8NoBom)
}

# Claude e OpenCode leem o frontmatter como está.
# Cursor: remove o frontmatter e promove a description para a primeira linha.
# VS Code: mantém só os campos aceitos em .prompt.md (name, description) e roda em modo agent.
function Write-Command([string]$Name, [string]$Source, [string]$Destination) {
  if ($Name -ne "cursor" -and $Name -ne "vscode") {
    Copy-Item -LiteralPath $Source -Destination $Destination -Force
    return
  }

  $lines = [System.IO.File]::ReadAllLines($Source, $script:Utf8NoBom)
  $nameLine = ""
  $descLine = ""
  $bodyStart = 0
  if ($lines.Count -gt 0 -and $lines[0] -eq "---") {
    for ($i = 1; $i -lt $lines.Count; $i++) {
      if ($lines[$i] -eq "---") { $bodyStart = $i + 1; break }
      if ($lines[$i] -match '^name:') { $nameLine = $lines[$i] }
      if ($lines[$i] -match '^description:') { $descLine = $lines[$i] }
    }
  }
  $body = @()
  if ($bodyStart -lt $lines.Count) { $body = $lines[$bodyStart..($lines.Count - 1)] }

  $output = New-Object System.Collections.Generic.List[string]
  if ($Name -eq "cursor") {
    $desc = ($descLine -replace '^description:\s*', '').Trim().Trim('"', "'")
    if ($desc) { $output.Add("> $desc"); $output.Add("") }
    $skipBlank = $true
    foreach ($line in $body) {
      if ($skipBlank -and [string]::IsNullOrWhiteSpace($line)) { continue }
      $skipBlank = $false
      $output.Add($line)
    }
  } else {
    $output.Add("---")
    if ($nameLine) { $output.Add($nameLine) }
    if ($descLine) { $output.Add($descLine) }
    $output.Add("agent: agent")
    $output.Add("---")
    foreach ($line in $body) { $output.Add($line) }
  }
  Write-TextFile $Destination $output.ToArray()
}

# ---------------------------------------------------------------------------
# Origem dos arquivos (local ou GitHub)
# ---------------------------------------------------------------------------

function Get-LocalSourceRoot {
  if (-not $PSScriptRoot) { return "" }
  $root = Join-Path $PSScriptRoot ".."
  if ((Test-Path -LiteralPath (Join-Rel $root $script:FrameworkRel)) -and
      (Test-Path -LiteralPath (Join-Path $root "SKILL.md")) -and
      (Test-Path -LiteralPath (Join-Path $root "commands"))) {
    return Get-FullPath $root
  }
  return ""
}

function Get-SkillVersion([string]$Path) {
  foreach ($line in [System.IO.File]::ReadAllLines($Path, $script:Utf8NoBom)) {
    if ($line -match '^\s*version:\s*"?([^"]*)"?\s*$') { return $Matches[1] }
  }
  return ""
}

function Enable-Tls12 {
  try {
    [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
  } catch { }
}

# Devolve a última tag publicada; "" se o repositório não tem tag v*;
# $null se a consulta falhou (sem rede, limite da API do GitHub ou modo offline).
function Get-LatestTag {
  if ($env:LGPD_AUDITOR_OFFLINE -eq "1") { return $null }
  try {
    Enable-Tls12
    $tags = Invoke-RestMethod -Uri "https://api.github.com/repos/$Repo/tags?per_page=100" -TimeoutSec 10 -UseBasicParsing
    $best = $null
    $bestTag = ""
    foreach ($tag in @($tags)) {
      if ($tag.name -match '^v(\d+(\.\d+){1,3})$') {
        $parsed = [version]$Matches[1]
        if ($null -eq $best -or $parsed -gt $best) { $best = $parsed; $bestTag = $tag.name }
      }
    }
    return $bestTag
  } catch {
    return $null
  }
}

function Resolve-Ref {
  if (-not $Version) {
    if (Get-LocalSourceRoot) {
      $script:Version = "local"
    } else {
      $latest = Get-LatestTag
      if ($latest) {
        $script:Version = $latest
      } else {
        if ($null -eq $latest) {
          # Falha de consulta não é "sem versão publicada": a branch main pode ter mudanças não lançadas.
          Write-WarnLog "Não foi possível consultar a última versão publicada (sem rede ou limite da API do GitHub)."
          if ($NonInteractive) { Stop-WithError "Informe a versão com -Version (ex.: -Version vX.Y.Z) ou tente de novo mais tarde." }
          if (-not (Confirm-Choice "Instalar a partir da branch main, que pode conter mudanças ainda não publicadas?" "n")) {
            Stop-WithError "Instalação cancelada. Informe a versão com -Version (ex.: -Version vX.Y.Z)."
          }
        } else {
          Write-WarnLog "Nenhuma tag publicada encontrada; usando a branch main."
        }
        $script:Version = "main"
      }
    }
  }
  $script:SourceRef = $script:Version

  if ($script:SourceRef -eq "local") {
    $script:SourceRoot = Get-LocalSourceRoot
    if (-not $script:SourceRoot) { Stop-WithError "-Version local exige rodar o script a partir de um clone do repositório." }
    $script:SourceVersion = Get-SkillVersion (Join-Path $script:SourceRoot "SKILL.md")
  }
}

function Get-RefLabel {
  if ($script:SourceRef -eq "local") { return "v$($script:SourceVersion) (cópia local em $($script:SourceRoot))" }
  return $script:SourceRef
}

function Get-Source {
  if ($script:SourceRoot) { return }
  Enable-Tls12
  $archive = Join-Path $script:TmpRoot "source.zip"
  $url = "https://codeload.github.com/$Repo/zip/$($script:SourceRef)"
  Write-Info "Baixando $Repo@$($script:SourceRef)..."
  try {
    Invoke-WebRequest -Uri $url -OutFile $archive -UseBasicParsing
  } catch {
    Stop-WithError "Falha ao baixar $url. Verifique a versão (-Version) e a conexão."
  }
  $extractDir = Join-Path $script:TmpRoot "source"
  Expand-Archive -LiteralPath $archive -DestinationPath $extractDir -Force
  $extracted = Get-ChildItem -LiteralPath $extractDir -Directory | Select-Object -First 1
  if (-not $extracted -or
      -not (Test-Path -LiteralPath (Join-Rel $extracted.FullName $script:FrameworkRel)) -or
      -not (Test-Path -LiteralPath (Join-Path $extracted.FullName "SKILL.md")) -or
      -not (Test-Path -LiteralPath (Join-Path $extracted.FullName "commands"))) {
    Stop-WithError "Conteúdo baixado inválido para $($script:SourceRef)."
  }
  $script:SourceRoot = $extracted.FullName
  $script:SourceVersion = Get-SkillVersion (Join-Path $script:SourceRoot "SKILL.md")
}

function Assert-NotSourceRepo {
  if ($script:SourceRoot -and $script:SourceRoot -eq $script:ProjectRoot) {
    Stop-WithError "O destino é o próprio repositório do framework. Use -ProjectDir para apontar o projeto a ser auditado."
  }
}

# ---------------------------------------------------------------------------
# Manifestos (um por ferramenta, em .agents/lgpd-enterprise-auditor/.install/)
# ---------------------------------------------------------------------------

function Get-ManifestPath([string]$Name) {
  return Join-Rel $script:ProjectRoot "$script:StateRel/$Name.json"
}

function Read-Manifest([string]$Name) {
  $path = Get-ManifestPath $Name
  if (-not (Test-Path -LiteralPath $path)) { return $null }
  return [System.IO.File]::ReadAllText($path, $script:Utf8NoBom) | ConvertFrom-Json
}

function Get-InstalledTargets {
  $result = @()
  foreach ($name in $script:SupportedTargets) {
    if (Test-Path -LiteralPath (Get-ManifestPath $name)) { $result += $name }
  }
  return ,$result
}

function ConvertTo-JsonString([string]$Value) {
  return '"' + ($Value -replace '\\', '\\' -replace '"', '\"') + '"'
}

# Mesmo layout do install.sh (uma chave por linha) para os dois instaladores lerem o mesmo arquivo.
function Write-Manifest([string]$Name, [string]$Skill, [string[]]$Files, [string]$SkillDir) {
  $path = Get-ManifestPath $Name
  New-Item -ItemType Directory -Force -Path (Split-Path -Parent $path) | Out-Null
  $skillJson = if ($Skill -eq "1") { "true" } else { "false" }

  $lines = New-Object System.Collections.Generic.List[string]
  $lines.Add("{")
  $lines.Add("  `"schemaVersion`": $(ConvertTo-JsonString $script:SchemaVersion),")
  $lines.Add("  `"project`": `"lgpd-enterprise-auditor`",")
  $lines.Add("  `"version`": $(ConvertTo-JsonString $script:SourceVersion),")
  $lines.Add("  `"ref`": $(ConvertTo-JsonString $script:SourceRef),")
  $lines.Add("  `"repo`": $(ConvertTo-JsonString $Repo),")
  $lines.Add("  `"target`": $(ConvertTo-JsonString $Name),")
  $lines.Add("  `"withSkill`": $skillJson,")
  $lines.Add("  `"os`": $(ConvertTo-JsonString (Get-OsName)),")
  $lines.Add("  `"frameworkDir`": $(ConvertTo-JsonString $script:FrameworkRel),")
  $lines.Add("  `"commandsDir`": $(ConvertTo-JsonString (Get-TargetCommandsDir $Name)),")
  $lines.Add("  `"skillDir`": $(ConvertTo-JsonString $SkillDir),")
  $lines.Add("  `"installedAt`": $(ConvertTo-JsonString (Get-IsoTimestamp)),")
  if ($Files.Count -eq 0) {
    $lines.Add("  `"files`": []")
  } else {
    $lines.Add("  `"files`": [")
    for ($i = 0; $i -lt $Files.Count; $i++) {
      $comma = if ($i -lt $Files.Count - 1) { "," } else { "" }
      $lines.Add("    $(ConvertTo-JsonString $Files[$i])$comma")
    }
    $lines.Add("  ]")
  }
  $lines.Add("}")
  Write-TextFile $path $lines.ToArray()
}

# ---------------------------------------------------------------------------
# Instalação e remoção
# ---------------------------------------------------------------------------

function Test-SafeRelPath([string]$Path) {
  return ($Path -and -not [System.IO.Path]::IsPathRooted($Path) -and $Path -notmatch '\.\.')
}

# Outra ferramenta (diferente de $Name) usa a mesma pasta de skill?
function Test-SkillDirShared([string]$Name, [string]$SkillDir) {
  foreach ($other in (Get-InstalledTargets)) {
    if ($other -eq $Name) { continue }
    $manifest = Read-Manifest $other
    if ($manifest.withSkill -and $manifest.skillDir -eq $SkillDir) { return $true }
  }
  return $false
}

function Remove-EmptyDirs {
  foreach ($dir in @(".claude/commands", ".claude/skills", ".claude", ".cursor/commands", ".cursor", ".github/prompts", ".github",
      ".opencode/commands", ".opencode", ".agents/skills", ".agents")) {
    $path = Join-Rel $script:ProjectRoot $dir
    if ((Test-Path -LiteralPath $path -PathType Container) -and -not (Get-ChildItem -LiteralPath $path -Force | Select-Object -First 1)) {
      Remove-Item -LiteralPath $path -Force
    }
  }
}

function Remove-TargetFiles([string]$Name) {
  $manifest = Read-Manifest $Name
  if ($null -eq $manifest) { return }

  foreach ($file in @($manifest.files)) {
    if (-not (Test-SafeRelPath $file)) { continue }
    $path = Join-Rel $script:ProjectRoot $file
    if (Test-Path -LiteralPath $path) { Remove-Item -LiteralPath $path -Force }
  }

  $skillDir = [string]$manifest.skillDir
  if ($manifest.withSkill -and (Test-SafeRelPath $skillDir) -and $skillDir.EndsWith("/$script:SkillName") -and
      -not (Test-SkillDirShared $Name $skillDir)) {
    $path = Join-Rel $script:ProjectRoot $skillDir
    if (Test-Path -LiteralPath $path) { Remove-Item -LiteralPath $path -Recurse -Force }
  }
}

function Copy-RelPath([string]$Rel, [string]$BackupDir) {
  $source = Join-Rel $script:ProjectRoot $Rel
  if (-not (Test-Path -LiteralPath $source)) { return }
  $destination = Join-Rel $BackupDir $Rel
  New-Item -ItemType Directory -Force -Path (Split-Path -Parent $destination) | Out-Null
  Copy-Item -LiteralPath $source -Destination $destination -Recurse -Force
}

function Backup-Existing([string]$Name) {
  $backupDir = Join-Rel $script:ProjectRoot ".lgpd-auditor-backup/$(Get-Date -Format 'yyyyMMddHHmmss')"
  New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
  Copy-RelPath $script:FrameworkRel $backupDir
  $manifest = Read-Manifest $Name
  if ($null -ne $manifest) {
    foreach ($file in @($manifest.files)) {
      if (Test-SafeRelPath $file) { Copy-RelPath $file $backupDir }
    }
    if (Test-SafeRelPath ([string]$manifest.skillDir)) { Copy-RelPath ([string]$manifest.skillDir) $backupDir }
  }
  Write-Info "Backup criado em $backupDir"
  Write-Info "Dica: adicione .lgpd-auditor-backup/ ao .gitignore do projeto."
}

function Install-Framework {
  $frameworkDir = Join-Rel $script:ProjectRoot $script:FrameworkRel
  $stateDir = Join-Path $frameworkDir ".install"
  $savedState = Join-Path $script:TmpRoot "install-state"

  if (Test-Path -LiteralPath $stateDir) {
    if (Test-Path -LiteralPath $savedState) { Remove-Item -LiteralPath $savedState -Recurse -Force }
    Move-Item -LiteralPath $stateDir -Destination $savedState
  }
  if (Test-Path -LiteralPath $frameworkDir) { Remove-Item -LiteralPath $frameworkDir -Recurse -Force }
  New-Item -ItemType Directory -Force -Path (Split-Path -Parent $frameworkDir) | Out-Null
  Copy-Item -LiteralPath (Join-Rel $script:SourceRoot $script:FrameworkRel) -Destination $frameworkDir -Recurse -Force
  if (Test-Path -LiteralPath $stateDir) { Remove-Item -LiteralPath $stateDir -Recurse -Force }
  Get-ChildItem -LiteralPath $frameworkDir -Recurse -Force -Filter ".DS_Store" | Remove-Item -Force
  if (Test-Path -LiteralPath $savedState) { Move-Item -LiteralPath $savedState -Destination $stateDir }
}

function Install-Target([string]$Name, [string]$Skill) {
  Remove-TargetFiles $Name
  Install-Framework

  $files = New-Object System.Collections.Generic.List[string]
  $commandsDir = Get-TargetCommandsDir $Name
  if ($commandsDir) {
    New-Item -ItemType Directory -Force -Path (Join-Rel $script:ProjectRoot $commandsDir) | Out-Null
    $sources = Get-ChildItem -LiteralPath (Join-Path $script:SourceRoot "commands") -Filter "*.md" -File | Sort-Object Name
    foreach ($source in $sources) {
      $rel = "$commandsDir/$(Get-TargetCommandFile $Name $source.BaseName)"
      Write-Command $Name $source.FullName (Join-Rel $script:ProjectRoot $rel)
      $files.Add($rel)
    }
    if ($files.Count -eq 0) { Stop-WithError "Nenhum comando encontrado em $(Join-Path $script:SourceRoot 'commands')." }
  }

  $skillDir = ""
  if ($Skill -eq "1") {
    $skillDir = Get-TargetSkillDir $Name
    $skillPath = Join-Rel $script:ProjectRoot $skillDir
    New-Item -ItemType Directory -Force -Path $skillPath | Out-Null
    Copy-Item -LiteralPath (Join-Path $script:SourceRoot "SKILL.md") -Destination (Join-Path $skillPath "SKILL.md") -Force
  }

  Write-Manifest $Name $Skill $files.ToArray() $skillDir
  Remove-EmptyDirs
  Write-Ok "$(Get-TargetLabel $Name) instalado (v$($script:SourceVersion))."
}

function Show-VersionDrift([string]$Name) {
  foreach ($other in (Get-InstalledTargets)) {
    if ($other -eq $Name) { continue }
    $installedVersion = (Read-Manifest $other).version
    if ($installedVersion -ne $script:SourceVersion) {
      Write-WarnLog "Os comandos de $other estão na v$installedVersion, mas o framework agora está na v$($script:SourceVersion). Rode a ação update para alinhar."
    }
  }
}

# ---------------------------------------------------------------------------
# Ações
# ---------------------------------------------------------------------------

function Invoke-Install {
  Resolve-Ref
  Assert-NotSourceRepo

  if (-not $NonInteractive) {
    Show-Banner (Get-RefLabel)
    Write-Info "Sistema operacional: $(Get-OsName)"
    Write-Info "Projeto: $($script:ProjectRoot)"
    Write-Host ""
  }

  $name = $Target
  if (-not $name) {
    if ($NonInteractive) { Stop-WithError "Informe -Target no modo -NonInteractive." }
    $labels = @($script:SupportedTargets | ForEach-Object { Get-TargetLabel $_ })
    $choice = Select-Index "1 - Selecione a ferramenta" $labels
    $name = $script:SupportedTargets[$choice - 1]
  } elseif (-not $NonInteractive) {
    Write-Host "1 - Ferramenta"
    Write-Host "  > $(Get-TargetLabel $name)"
  }

  if ($name -eq "agents") {
    if ($script:Skill -eq "0") { Stop-WithError "A opção agents não tem slash commands: a skill é obrigatória (remova -NoSkill)." }
    $script:Skill = "1"
    if (-not $NonInteractive) { Write-Host "2 - Skill"; Write-Host "  > sim (obrigatória para agents: é a forma de acionar a auditoria)" }
  } elseif (-not $script:Skill) {
    $script:Skill = "0"
    if (-not $NonInteractive) {
      Write-Host "2 - Instalar também a skill?"
      Write-Host "    Permite acionar a auditoria em linguagem natural, sem slash command."
      if (Confirm-Choice "    Instalar a skill?" "n") { $script:Skill = "1" }
    }
  }

  $commandsDir = Get-TargetCommandsDir $name
  $skillLabel = "não"
  if ($script:Skill -eq "1") { $skillLabel = "sim → $(Join-Rel $script:ProjectRoot (Get-TargetSkillDir $name))" }

  Write-Host ""
  Write-Host "Resumo da instalação"
  Write-Host "  Ferramenta: $(Get-TargetLabel $name)"
  Write-Host "  Versão:     $(Get-RefLabel)"
  Write-Host "  Framework:  $(Join-Rel $script:ProjectRoot $script:FrameworkRel)"
  if ($commandsDir) { Write-Host "  Comandos:   $(Join-Rel $script:ProjectRoot $commandsDir)" }
  Write-Host "  Skill:      $skillLabel"
  $existing = Read-Manifest $name
  if ($null -ne $existing) {
    Write-Host "  Atenção:    já existe uma instalação para $name (v$($existing.version)); ela será substituída."
  }
  Write-Host ""

  if (-not $NonInteractive) {
    if (-not (Confirm-Choice "Confirmar instalação?" "y")) { Write-WarnLog "Instalação cancelada."; return }
    if ((Test-Path -LiteralPath (Join-Rel $script:ProjectRoot $script:FrameworkRel)) -and
        (Confirm-Choice "Instalação existente detectada. Criar backup antes de substituir?" "y")) {
      Backup-Existing $name
    }
  }

  Get-Source
  Assert-NotSourceRepo
  Install-Target $name $script:Skill
  Show-VersionDrift $name
  Show-NextSteps $name $script:Skill
}

function Invoke-Update {
  if ($Target) {
    if ($null -eq (Read-Manifest $Target)) { Stop-WithError "Nenhuma instalação de $Target encontrada em $($script:ProjectRoot)." $script:ExitNotFound }
    $targets = @($Target)
  } else {
    $targets = Get-InstalledTargets
    if ($targets.Count -eq 0) { Stop-WithError "Nenhuma instalação encontrada em $($script:ProjectRoot). Use a ação install." $script:ExitNotFound }
  }

  Resolve-Ref
  Assert-NotSourceRepo
  Write-Host ""
  Write-Host "Resumo da atualização"
  Write-Host "  Projeto: $($script:ProjectRoot)"
  Write-Host "  Versão:  $(Get-RefLabel)"
  foreach ($name in $targets) {
    Write-Host "  - $(Get-TargetLabel $name) (atual: v$((Read-Manifest $name).version))"
  }
  Write-Host ""

  if (-not $NonInteractive -and -not (Confirm-Choice "Confirmar atualização?" "y")) { Write-WarnLog "Atualização cancelada."; return }

  Get-Source
  Assert-NotSourceRepo
  foreach ($name in $targets) {
    $skill = if ((Read-Manifest $name).withSkill) { "1" } else { "0" }
    if ($script:Skill -and $Target -and $name -ne "agents") { $skill = $script:Skill }
    Install-Target $name $skill
  }
}

function Invoke-Uninstall {
  $installed = Get-InstalledTargets
  if ($installed.Count -eq 0) { Stop-WithError "Nenhuma instalação encontrada em $($script:ProjectRoot)." $script:ExitNotFound }

  if ($Target) {
    if ($installed -notcontains $Target) { Stop-WithError "Nenhuma instalação de $Target encontrada em $($script:ProjectRoot)." $script:ExitNotFound }
    $targets = @($Target)
  } elseif ($NonInteractive -or $installed.Count -eq 1) {
    $targets = $installed
  } else {
    $choice = Select-Index "Qual instalação remover?" (@($installed) + @("todas"))
    if ($choice -gt $installed.Count) { $targets = $installed } else { $targets = @($installed[$choice - 1]) }
  }

  Write-Host ""
  Write-Host "Resumo da remoção"
  Write-Host "  Projeto: $($script:ProjectRoot)"
  foreach ($name in $targets) { Write-Host "  - $(Get-TargetLabel $name)" }
  Write-Host ""

  if (-not $NonInteractive -and -not (Confirm-Choice "Confirmar remoção?" "n")) { Write-WarnLog "Remoção cancelada."; return }

  foreach ($name in $targets) {
    Remove-TargetFiles $name
    Remove-Item -LiteralPath (Get-ManifestPath $name) -Force
    Write-Ok "$(Get-TargetLabel $name) removido."
  }

  if ((Get-InstalledTargets).Count -eq 0) {
    $frameworkDir = Join-Rel $script:ProjectRoot $script:FrameworkRel
    if (Test-Path -LiteralPath $frameworkDir) { Remove-Item -LiteralPath $frameworkDir -Recurse -Force }
    Write-Ok "Framework removido de $frameworkDir."
  }
  Remove-EmptyDirs
}

function Invoke-Check {
  $installed = Get-InstalledTargets
  if ($installed.Count -eq 0) { Stop-WithError "Nenhuma instalação encontrada em $($script:ProjectRoot)." $script:ExitNotFound }

  $broken = $false
  if (-not (Test-Path -LiteralPath (Join-Rel $script:ProjectRoot "$script:FrameworkRel/core/auditor-core.md"))) {
    Write-Host "[ERROR] Framework incompleto em $(Join-Rel $script:ProjectRoot $script:FrameworkRel)." -ForegroundColor Red
    $broken = $true
  }

  $installedVersion = ""
  foreach ($name in $installed) {
    $manifest = Read-Manifest $name
    $installedVersion = $manifest.version
    $missing = $false
    foreach ($file in @($manifest.files)) {
      if (-not (Test-Path -LiteralPath (Join-Rel $script:ProjectRoot $file))) {
        Write-Host "[ERROR] ${name}: arquivo ausente $file" -ForegroundColor Red
        $missing = $true
      }
    }
    if ($manifest.withSkill -and -not (Test-Path -LiteralPath (Join-Rel $script:ProjectRoot "$($manifest.skillDir)/SKILL.md"))) {
      Write-Host "[ERROR] ${name}: skill ausente em $($manifest.skillDir)" -ForegroundColor Red
      $missing = $true
    }
    if ($missing) {
      $broken = $true
    } else {
      $skillText = if ($manifest.withSkill) { "true" } else { "false" }
      Write-Ok "$(Get-TargetLabel $name) — v$($manifest.version), skill: $skillText, instalado em $(Format-Stamp $manifest.installedAt)"
    }
  }

  $newest = Get-LatestTag
  if ($newest -and "v$installedVersion" -ne $newest) {
    Write-Info "Versão publicada mais recente: $newest. Rode a ação update para atualizar."
  }

  if ($broken) { Stop-WithError "Instalação com problemas. Rode a ação install novamente para corrigir." }
}

if ($Help) { Show-Usage; exit 0 }
if ($Repo -notmatch '^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+$') { Stop-WithError "Repositório inválido: $Repo (use owner/repo)" }

Resolve-ProjectDir
$script:TmpRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("lgpd-auditor-" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Force -Path $script:TmpRoot | Out-Null

try {
  switch ($Action) {
    "install" { Invoke-Install }
    "update" { Invoke-Update }
    "uninstall" { Invoke-Uninstall }
    "check" { Invoke-Check }
  }
} finally {
  Remove-TempRoot
}
