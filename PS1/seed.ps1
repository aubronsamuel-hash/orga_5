$ErrorActionPreference = "Stop"
wsl -d Ubuntu -- bash -lc "docker exec orga5_api python -m app.seed"
