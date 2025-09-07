# Orga 5

## Prerequis
- Docker Desktop
- PowerShell 7

## Demarrage local
```
copy .env.example .env
pwsh PS1/dev_up.ps1
pwsh PS1/smoke.ps1
```

## Endpoints attendus
- `/` : frontend React
- `/api/health` : `{ "api": "ok" }`
- `/api/ping/db` : `{ "db": 1 }`
- `/api/ping/redis` : `{ "redis": "ok" }`
