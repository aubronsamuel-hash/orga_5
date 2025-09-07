from fastapi import FastAPI
import os
import psycopg
import redis.asyncio as redis

app = FastAPI()

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/api/health")
def api_health() -> dict[str, str]:
    return {"api": "ok"}

@app.get("/api/ping/db")
def ping_db() -> dict[str, int]:
    conn = psycopg.connect(
        host=os.getenv("POSTGRES_HOST", "db"),
        port=os.getenv("POSTGRES_PORT", "5432"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        dbname=os.getenv("POSTGRES_DB"),
    )
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
            row = cur.fetchone()
    conn.close()
    return {"db": row[0]}

@app.get("/api/ping/redis")
async def ping_redis() -> dict[str, str]:
    client = redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=int(os.getenv("REDIS_PORT", "6379")),
    )
    try:
        await client.ping()
        return {"redis": "ok"}
    finally:
        await client.close()
