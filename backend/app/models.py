from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .db import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    avatar_url: Mapped[str | None] = mapped_column(String(512))

    missions: Mapped[list["Mission"]] = relationship("Mission", back_populates="assignee")

class Mission(Base):
    __tablename__ = "missions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    date: Mapped[Date] = mapped_column(Date, nullable=False)
    location: Mapped[str | None] = mapped_column(String(255))
    assignee_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))

    assignee: Mapped['User' | None] = relationship("User", back_populates="missions")

class Planning(Base):
    __tablename__ = "plannings"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
