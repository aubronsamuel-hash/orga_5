from enum import Enum
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

class Role(str, Enum):
    admin = "admin"
    planner = "planner"
    tech = "tech"

class LoginRequest(BaseModel):
    role: Role

bearer = HTTPBearer(auto_error=False)

def get_current_role(credentials: HTTPAuthorizationCredentials | None = Depends(bearer)) -> Role:
    if credentials is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        return Role(credentials.credentials)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN) from exc

def require_role(required: Role):
    def verifier(role: Role = Depends(get_current_role)):
        if role != required:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return verifier
