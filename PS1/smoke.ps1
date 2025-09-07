$ErrorActionPreference = "Stop"

$health = Invoke-RestMethod -Uri "http://localhost:8000/health"
if ($health.status -ne 'ok' -or $health.db -ne 'up') { throw 'health failed' }

$body = @{ email = 'admin@example.com'; password = 'ChangeMe123!' } | ConvertTo-Json
$login = Invoke-RestMethod -Method Post -Uri "http://localhost:8000/auth/login" -ContentType 'application/json' -Body $body
if (-not $login.access_token) { throw 'login failed' }
