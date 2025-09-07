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

#### Si le DB ne demarre pas
- Purger le volume local: `docker volume rm orga_5_db_data -f`
- Recréer le fichier .env: `Copy-Item .env.example .env -Force`
- Relancer: `pwsh PS1/dev_up.ps1`

## Endpoints attendus
- `/` : frontend React
- `/api/health` : `{ "api": "ok" }`
- `/api/ping/db` : `{ "db": 1 }`
- `/api/ping/redis` : `{ "redis": "ok" }`
