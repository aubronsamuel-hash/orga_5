from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db import engine, Base
from . import models, crud
from .schemas import HealthOut, UserOut
from .deps import db_dep

app = FastAPI(title="Orga5 API")

# Create tables on startup (simple bootstrap; Alembic later)
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def seed():
    from .db import SessionLocal
    with SessionLocal() as db:
        crud.seed_minimal(db)

@app.get("/health", response_model=HealthOut)
def health():
    return {"status": "ok"}

@app.get("/users", response_model=list[UserOut])
def list_users(db: Session = Depends(db_dep)):
    return db.query(models.User).all()
