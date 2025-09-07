import os
import sys
from uuid import uuid4

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ["DATABASE_URL"] = "sqlite:///test.db"

from fastapi.testclient import TestClient

from app.core.security import hash_password
from app.db import Base, SessionLocal, engine
from app.main import app
from app.models import User


def setup_db() -> None:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        db.add(
            User(id=str(uuid4()), email="admin@example.com", password_hash=hash_password("ChangeMe123!"))
        )
        db.commit()


def test_login_success() -> None:
    setup_db()
    client = TestClient(app)
    res = client.post(
        "/auth/login",
        json={"email": "admin@example.com", "password": "ChangeMe123!"},
    )
    assert res.status_code == 200
    data = res.json()
    assert data["user"]["email"] == "admin@example.com"
    assert data["access_token"]


def test_login_failure() -> None:
    setup_db()
    client = TestClient(app)
    res = client.post(
        "/auth/login",
        json={"email": "admin@example.com", "password": "wrong"},
    )
    assert res.status_code == 401
