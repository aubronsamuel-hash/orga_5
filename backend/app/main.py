from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select, text
from sqlalchemy.orm import Session
from pydantic import BaseModel

from .core.security import create_access_token, verify_password
from .db import engine, get_session
from .models import User

app = FastAPI(title="Orga5 API")


class LoginIn(BaseModel):
    email: str
    password: str


@app.get("/health")
def health() -> dict:
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except Exception as exc:  # pragma: no cover - passthrough
        raise HTTPException(status_code=500, detail="db_down") from exc
    return {"status": "ok", "db": "up"}


@app.post("/auth/login")
def login(data: LoginIn, db: Session = Depends(get_session)) -> dict:
    email = data.email.lower()
    user = db.scalar(select(User).where(User.email == email))
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="invalid_credentials")
    token = create_access_token({"sub": user.id, "email": user.email})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {"id": user.id, "email": user.email},
    }
