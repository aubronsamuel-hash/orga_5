from fastapi.testclient import TestClient
from app.main import app
from app.auth import Role

client = TestClient(app)

def test_login_returns_token():
    resp = client.post("/auth/login", json={"role": "admin"})
    assert resp.status_code == 200
    assert resp.json() == {"token": Role.admin}

def test_admin_access_denied_for_non_admin():
    resp = client.get("/admin", headers={"Authorization": "Bearer planner"})
    assert resp.status_code == 403

def test_admin_access_allowed_for_admin():
    resp = client.get("/admin", headers={"Authorization": "Bearer admin"})
    assert resp.status_code == 200
    assert resp.json() == {"status": "admin"}
