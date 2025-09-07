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

# Wait for API health
Write-Host "Waiting for API health at http://localhost:8000/health ..."
$max = 40
for ($i=0; $i -lt $max; $i++) {
  try {
    $r = Invoke-WebRequest -Uri "http://localhost:8000/health" -UseBasicParsing -TimeoutSec 3
    if ($r.StatusCode -eq 200) { Write-Host "API is healthy."; break }
  } catch {}
  Start-Sleep -Seconds 2
}

Write-Host "Open front-end: http://localhost:8080"
Start-Process "http://localhost:8080"
