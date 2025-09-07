from pydantic import BaseModel
from datetime import date

class HealthOut(BaseModel):
    status: str

class UserOut(BaseModel):
    id: int
    email: str
    full_name: str
    avatar_url: str | None = None
    class Config:
        from_attributes = True

class MissionOut(BaseModel):
    id: int
    title: str
    date: date
    location: str | None = None
    assignee_id: int | None = None
    class Config:
        from_attributes = True
