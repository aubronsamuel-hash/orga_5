Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$root = Resolve-Path "$PSScriptRoot/.."
$envFile = Join-Path $root '.env'
$envExample = Join-Path $root '.env.example'
if (-not (Test-Path $envFile)) {
    Copy-Item $envExample $envFile
}

Set-Location $root
docker compose up -d --build
Start-Sleep -Seconds 5
