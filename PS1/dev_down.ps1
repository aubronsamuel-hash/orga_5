$ErrorActionPreference = "Stop"
$repo = "C:\Users\samue\orga_5"
if (-not (Test-Path $repo)) { throw "Repo path not found: $repo" }
Set-Location $repo
if (-not (Test-Path "$repo\docker-compose.yml")) { throw "docker-compose.yml not found at $repo" }

wsl -d Ubuntu -- bash -lc "cd /mnt/c/Users/samue/orga_5 && docker compose down -v"
