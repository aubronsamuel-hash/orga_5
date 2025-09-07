#!/usr/bin/env sh
set -e

cd /app

if [ -f /app/alembic.ini ] && [ -d /app/migrations ]; then
  echo "[entrypoint] Alembic config found. Running migrations..."
  alembic upgrade head
else
  echo "[entrypoint] No Alembic config found. Skipping migrations."
fi

exec uvicorn app.main:app --host 0.0.0.0 --port 8000
