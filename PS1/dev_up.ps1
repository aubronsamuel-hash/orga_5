Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

param()

$root = Resolve-Path "$PSScriptRoot/.."
$envFile = Join-Path $root '.env'
$envExample = Join-Path $root '.env.example'
if (-not (Test-Path $envFile)) {
    Copy-Item $envExample $envFile
}

Write-Host "Starting dev environment inside WSL Ubuntu..."
# Always run docker compose from Ubuntu where Docker Engine is installed
wsl -d Ubuntu -- bash -lc "cd /mnt/c/Users/samue/orga_5 && docker compose up -d --build"
Start-Sleep -Seconds 5
