from fastapi import FastAPI, Depends
from .auth import LoginRequest, Role, require_role
from .planning import router as planning_router

app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/auth/login")
def login(data: LoginRequest):
    return {"token": data.role}

@app.get("/admin", dependencies=[Depends(require_role(Role.admin))])
def admin_area():
    return {"status": "admin"}

app.include_router(planning_router, prefix="/v1/planning")
