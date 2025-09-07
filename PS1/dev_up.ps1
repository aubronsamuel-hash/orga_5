param(
  [switch]$Rebuild
)

$ErrorActionPreference = "Stop"

# Ensure we are at repo root where docker-compose.yml lives
$repo = "C:\Users\samue\orga_5"
if (-not (Test-Path $repo)) { throw "Repo path not found: $repo" }
Set-Location $repo
if (-not (Test-Path "$repo\docker-compose.yml")) { throw "docker-compose.yml not found at $repo" }

# Use WSL Ubuntu to run docker compose
$composeCmd = "docker compose up -d"
if ($Rebuild) { $composeCmd = "docker compose up -d --build" }

wsl -d Ubuntu -- bash -lc "cd /mnt/c/Users/samue/orga_5 && $composeCmd"

& "$PSScriptRoot/seed.ps1"
& "$PSScriptRoot/smoke.ps1"
