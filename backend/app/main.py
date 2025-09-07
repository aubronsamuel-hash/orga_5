from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, crud
from .schemas import UserOut
from .deps import db_dep

app = FastAPI(title="Orga5 API")

@app.on_event("startup")
def seed():
    from .db import SessionLocal
    with SessionLocal() as db:
        crud.seed_minimal(db)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/users", response_model=list[UserOut])
def list_users(db: Session = Depends(db_dep)):
    return db.query(models.User).all()
