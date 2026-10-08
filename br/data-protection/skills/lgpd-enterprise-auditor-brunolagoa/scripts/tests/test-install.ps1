# Testes de regressão do scripts/install.ps1. Rodam offline, a partir do clone (-Version local),
# em projetos temporários. Uso: pwsh -File scripts/tests/test-install.ps1 (ou powershell -File no 5.1)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$RepoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot "../.."))
$Installer = Join-Path $RepoRoot "scripts/install.ps1"
$Shell = (Get-Process -Id $PID).Path
$WorkDir = Join-Path ([System.IO.Path]::GetTempPath()) ("lgpd-auditor-test-" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Force -Path $WorkDir | Out-Null
$env:LGPD_AUDITOR_OFFLINE = "1"

$CommandCount = @(Get-ChildItem -LiteralPath (Join-Path $RepoRoot "commands") -Filter "*.md" -File).Count
$script:Failures = 0
$script:Current = ""
$script:LastLog = ""

function Test-Check([string]$Description, [bool]$Condition) {
  if ($Condition) { Write-Host "  ok   $Description" } else { Write-Host "  FAIL $Description"; $script:Failures++ }
}

function New-Project([string]$Name) {
  $script:Current = Join-Path $WorkDir $Name
  New-Item -ItemType Directory -Force -Path (Join-Path $script:Current ".git") | Out-Null
  Set-Content -LiteralPath (Join-Path $script:Current "app.txt") -Value "keep"
}

function Invoke-Installer {
  # Erros esperados do instalador vão para o stderr; no 5.1, com Stop, isso viraria exceção.
  $ErrorActionPreference = "Continue"
  $output = & $Shell -NoProfile -ExecutionPolicy Bypass -File $Installer @args -ProjectDir $script:Current 2>&1
  $script:LastLog = ($output | Out-String)
  return $LASTEXITCODE
}

function Install-Quiet {
  return Invoke-Installer install -NonInteractive -Version local @args
}

# Roda uma cópia do instalador fora do clone, onde não existe a origem local.
function Invoke-InstallerCopy([string]$Path) {
  $ErrorActionPreference = "Continue"
  $output = & $Shell -NoProfile -ExecutionPolicy Bypass -File $Path @args -ProjectDir $script:Current 2>&1
  $script:LastLog = ($output | Out-String)
  return $LASTEXITCODE
}

function Get-ProjectPath([string]$Rel) { return Join-Path $script:Current $Rel }
function Test-Exists([string]$Rel) { return Test-Path -LiteralPath (Get-ProjectPath $Rel) }
function Get-Count([string]$Dir, [string]$Pattern) {
  $path = Get-ProjectPath $Dir
  if (-not (Test-Path -LiteralPath $path)) { return 0 }
  return @(Get-ChildItem -LiteralPath $path -Filter $Pattern -File).Count
}
function Get-Lines([string]$Rel) { return [System.IO.File]::ReadAllLines((Get-ProjectPath $Rel)) }
function Test-Contains([string]$Rel, [string]$Pattern) { return [bool](@(Get-Lines $Rel) -match $Pattern) }
function Test-AppUntouched { return ((Get-Content -LiteralPath (Get-ProjectPath "app.txt")) -eq "keep") }

try {
  Write-Host "== install por ferramenta (sem skill)"
  $dirs = @{ claude = @(".claude/commands", "lgpd-*.md"); cursor = @(".cursor/commands", "lgpd-*.md");
    vscode = @(".github/prompts", "lgpd-*.prompt.md"); opencode = @(".opencode/commands", "lgpd-*.md") }
  foreach ($target in @("claude", "cursor", "vscode", "opencode")) {
    New-Project "plain-$target"
    Install-Quiet -Target $target | Out-Null
    $dir = $dirs[$target][0]
    Test-Check "${target}: framework instalado" (Test-Exists ".agents/lgpd-enterprise-auditor/core/auditor-core.md")
    Test-Check "${target}: modelo do relatório em HTML instalado" (Test-Exists ".agents/lgpd-enterprise-auditor/reports/html-report-template.html")
    Test-Check "${target}: $CommandCount comandos em $dir" ((Get-Count $dir $dirs[$target][1]) -eq $CommandCount)
    Test-Check "${target}: manifesto criado" (Test-Exists ".agents/lgpd-enterprise-auditor/.install/$target.json")
    Test-Check "${target}: sem skill" (-not (Test-Exists ".agents/skills"))
    Test-Check "${target}: sem skill do Claude" (-not (Test-Exists ".claude/skills"))
    Test-Check "${target}: arquivo do projeto intacto" (Test-AppUntouched)
  }

  Write-Host "== agents (skill obrigatória)"
  New-Project "agents"
  Install-Quiet -Target agents | Out-Null
  Test-Check "agents: skill em .agents/skills" (Test-Exists ".agents/skills/lgpd-enterprise-auditor/SKILL.md")
  Test-Check "agents: manifesto sem comandos" (Test-Contains ".agents/lgpd-enterprise-auditor/.install/agents.json" '"files": \[\]')
  Test-Check "agents: -NoSkill é recusado" ((Install-Quiet -Target agents -NoSkill) -eq 1)

  Write-Host "== skill por ferramenta"
  New-Project "skill-claude"
  Install-Quiet -Target claude -WithSkill | Out-Null
  Test-Check "claude: skill em .claude/skills" (Test-Exists ".claude/skills/lgpd-enterprise-auditor/SKILL.md")
  Test-Check "claude: skill tem frontmatter" ((Get-Lines ".claude/skills/lgpd-enterprise-auditor/SKILL.md")[0] -eq "---")
  New-Project "skill-cursor"
  Install-Quiet -Target cursor -WithSkill | Out-Null
  Test-Check "cursor: skill em .agents/skills" (Test-Exists ".agents/skills/lgpd-enterprise-auditor/SKILL.md")

  Write-Host "== transformações de formato"
  New-Project "formats"
  Install-Quiet -Target cursor | Out-Null
  Install-Quiet -Target vscode | Out-Null
  Test-Check "cursor: description na primeira linha" ((Get-Lines ".cursor/commands/lgpd-saas.md")[0] -match '^> Executa auditoria')
  Test-Check "cursor: frontmatter removido" (-not (Test-Contains ".cursor/commands/lgpd-saas.md" '^license:'))
  Test-Check "vscode: frontmatter na primeira linha" ((Get-Lines ".github/prompts/lgpd-saas.prompt.md")[0] -eq "---")
  Test-Check "vscode: modo agent" (Test-Contains ".github/prompts/lgpd-saas.prompt.md" '^agent: agent$')
  Test-Check "vscode: mantém name" (Test-Contains ".github/prompts/lgpd-saas.prompt.md" '^name: lgpd-saas$')
  Test-Check "vscode: remove campos não suportados" (-not (Test-Contains ".github/prompts/lgpd-saas.prompt.md" '^license:'))
  Test-Check "arquivos sem BOM" ([System.IO.File]::ReadAllBytes((Get-ProjectPath ".cursor/commands/lgpd-saas.md"))[0] -ne 0xEF)

  Write-Host "== reinstalação e update"
  New-Project "reinstall"
  Install-Quiet -Target claude -WithSkill | Out-Null
  Install-Quiet -Target claude -WithSkill | Out-Null
  Test-Check "reinstalação não duplica comandos" ((Get-Count ".claude/commands" "lgpd-*.md") -eq $CommandCount)
  Install-Quiet -Target claude -NoSkill | Out-Null
  Test-Check "reinstalar sem skill remove a skill" (-not (Test-Exists ".claude/skills"))
  $manifestPath = Get-ProjectPath ".agents/lgpd-enterprise-auditor/.install/claude.json"
  $content = [System.IO.File]::ReadAllText($manifestPath) -replace '"version": "[^"]*"', '"version": "0.0.1"'
  [System.IO.File]::WriteAllText($manifestPath, $content)
  Invoke-Installer update -NonInteractive -Version local | Out-Null
  Test-Check "update restaura a versão atual" (-not (Test-Contains ".agents/lgpd-enterprise-auditor/.install/claude.json" '"version": "0.0.1"'))
  New-Project "empty-update"
  Test-Check "update sem instalação retorna 2" ((Invoke-Installer update -NonInteractive -Version local) -eq 2)

  Write-Host "== várias ferramentas e uninstall"
  New-Project "multi"
  New-Item -ItemType Directory -Force -Path (Get-ProjectPath ".claude/commands"), (Get-ProjectPath ".github/prompts") | Out-Null
  Set-Content -LiteralPath (Get-ProjectPath ".claude/commands/meu-comando.md") -Value "meu"
  Set-Content -LiteralPath (Get-ProjectPath ".github/prompts/meu.prompt.md") -Value "meu"
  Install-Quiet -Target claude | Out-Null
  Install-Quiet -Target vscode -WithSkill | Out-Null
  Install-Quiet -Target agents | Out-Null
  Invoke-Installer uninstall -NonInteractive -Target vscode | Out-Null
  Test-Check "uninstall vscode remove os prompts" ((Get-Count ".github/prompts" "lgpd-*.prompt.md") -eq 0)
  Test-Check "uninstall vscode mantém prompt do usuário" (Test-Exists ".github/prompts/meu.prompt.md")
  Test-Check "skill compartilhada com agents é mantida" (Test-Exists ".agents/skills/lgpd-enterprise-auditor/SKILL.md")
  Test-Check "framework mantido enquanto houver ferramentas" (Test-Exists ".agents/lgpd-enterprise-auditor/core/auditor-core.md")
  Invoke-Installer uninstall -NonInteractive | Out-Null
  Test-Check "uninstall total remove o framework" (-not (Test-Exists ".agents"))
  Test-Check "uninstall total remove comandos do Claude" ((Get-Count ".claude/commands" "lgpd-*.md") -eq 0)
  Test-Check "uninstall total mantém comando do usuário" (Test-Exists ".claude/commands/meu-comando.md")
  Test-Check "arquivo do projeto intacto" (Test-AppUntouched)

  Write-Host "== check"
  New-Project "check"
  Test-Check "check sem instalação retorna 2" ((Invoke-Installer check) -eq 2)
  Install-Quiet -Target opencode | Out-Null
  Test-Check "check com instalação íntegra retorna 0" ((Invoke-Installer check) -eq 0)
  Remove-Item -LiteralPath (Get-ProjectPath ".opencode/commands/lgpd-saas.md")
  Test-Check "check com arquivo ausente retorna 1" ((Invoke-Installer check) -eq 1)

  Write-Host "== proteções"
  New-Project "guards"
  Test-Check "-NonInteractive sem -Target retorna 1" ((Install-Quiet) -eq 1)
  Test-Check "ferramenta inválida falha" ((Install-Quiet -Target emacs) -ne 0)
  $script:Current = $RepoRoot
  Test-Check "instalar no próprio repositório é recusado" ((Install-Quiet -Target claude) -eq 1)
  Test-Check "nada foi instalado no repositório" (-not (Test-Path -LiteralPath (Join-Path $RepoRoot ".claude/commands/lgpd-saas.md")))

  Write-Host "== última versão não consultável"
  # Fora de um clone e sem conseguir consultar a última versão, o instalador não cai na branch main sozinho.
  $solo = Join-Path $WorkDir "solo"
  New-Item -ItemType Directory -Force -Path $solo | Out-Null
  $soloInstaller = Join-Path $solo "install.ps1"
  Copy-Item -LiteralPath $Installer -Destination $soloInstaller
  New-Project "no-tag"
  Test-Check "modo não interativo sem -Version retorna 1" ((Invoke-InstallerCopy $soloInstaller install -NonInteractive -Target claude) -eq 1)
  Test-Check "modo não interativo sem -Version: nada é instalado" (-not (Test-Exists ".agents"))
} finally {
  Remove-Item -LiteralPath $WorkDir -Recurse -Force -ErrorAction SilentlyContinue
}

Write-Host ""
if ($script:Failures -gt 0) {
  Write-Host "$($script:Failures) teste(s) falharam. Último log:"
  Write-Host $script:LastLog
  exit 1
}
Write-Host "Todos os testes passaram."
exit 0
