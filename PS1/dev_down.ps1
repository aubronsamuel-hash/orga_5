Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

docker compose -f deploy/dev/compose.yaml down -v
