from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field, field_validator, model_validator
from sqlalchemy import DateTime, Enum, ForeignKey, Index, String, Text, select
from sqlalchemy.orm import Mapped, Session, mapped_column, relationship

from .db import Base, get_session

class Assignment(Base):
    __tablename__ = "assignments"

    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), index=True)
    person_id: Mapped[int] = mapped_column()
    role: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(Enum("TENTATIVE", "CONFIRMED", "CANCELED", name="assignment_status"))
    created_at_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    updated_at_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    org_id: Mapped[int] = mapped_column(index=True)
    project_id: Mapped[int | None] = mapped_column(nullable=True)
    title: Mapped[str] = mapped_column(String)
    start_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    end_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    location: Mapped[str | None] = mapped_column(String, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    updated_at_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    assignments: Mapped[list[Assignment]] = relationship("Assignment", backref="event", cascade="all, delete-orphan")

    __table_args__ = (
        Index("ix_events_org_start", "org_id", "start_utc"),
    )

class AssignmentOut(BaseModel):
    id: int
    person_id: int
    role: str
    status: Literal["TENTATIVE", "CONFIRMED", "CANCELED"]

    class Config:
        from_attributes = True

class EventOut(BaseModel):
    id: int
    org_id: int
    project_id: int | None
    title: str
    start_utc: datetime
    end_utc: datetime
    location: str | None
    notes: str | None
    assignments: list[AssignmentOut] = []

    class Config:
        from_attributes = True

    @field_validator("start_utc", "end_utc")
    @classmethod
    def utc(cls, v: datetime) -> datetime:
        if v.tzinfo is None:
            return v.replace(tzinfo=timezone.utc)
        if v.tzinfo != timezone.utc:
            raise ValueError("must be UTC")
        return v

class EventQuery(BaseModel):
    from_: datetime
    to: datetime
    project_id: int | None = None

    model_config = {"populate_by_name": True}

    @field_validator("from_", "to")
    @classmethod
    def utc(cls, v: datetime) -> datetime:
        if v.tzinfo != timezone.utc:
            raise ValueError("must be UTC")
        return v

    @model_validator(mode="after")
    def check_range(self) -> "EventQuery":
        if self.to <= self.from_:
            raise ValueError("invalid range")
        return self

router = APIRouter()

def _event_query(from_: datetime = Query(alias="from"), to: datetime = Query(), project_id: int | None = None) -> EventQuery:
    return EventQuery(from_=from_, to=to, project_id=project_id)


@router.get("/events", response_model=list[EventOut])
def list_events(params: EventQuery = Depends(_event_query), session: Session = Depends(get_session)):
    stmt = select(Event).where(Event.start_utc >= params.from_, Event.start_utc < params.to)
    if params.project_id is not None:
        stmt = stmt.where(Event.project_id == params.project_id)
    return session.execute(stmt).scalars().all()

@router.get("/events/{event_id}", response_model=EventOut)
def get_event(event_id: int, session: Session = Depends(get_session)):
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404)
    return event
