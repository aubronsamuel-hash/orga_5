Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$root = Resolve-Path "$PSScriptRoot/.."
$envPath = Join-Path $root '.env'
Get-Content $envPath | ForEach-Object {
    if ($_ -match '^([^#=]+)=([^#]+)$') {
        [Environment]::SetEnvironmentVariable($matches[1], $matches[2])
    }
}

$base = "http://localhost:$([Environment]::GetEnvironmentVariable('WEB_PORT'))"
Invoke-RestMethod "$base/" | Out-Null
Invoke-RestMethod "$base/api/health" | Out-Null
Invoke-RestMethod "$base/api/ping/db" | Out-Null
Invoke-RestMethod "$base/api/ping/redis" | Out-Null
