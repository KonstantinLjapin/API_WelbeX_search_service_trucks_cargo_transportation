from __future__ import annotations
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Location(Base):
    __tablename__ = "location"
    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(index=True)
    state: Mapped[str] = mapped_column(index=True)
    latitude: Mapped[str] = mapped_column(index=True)
    longitude: Mapped[str] = mapped_column(index=True)


class Cargo(Base):
    __tablename__ = "cargo"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(index=True)
    pick_up: Mapped[int] = mapped_column(ForeignKey("location.id"))
    delivery: Mapped[int] = mapped_column(ForeignKey("location.id"))
    weight: Mapped[int] = mapped_column(index=True)


class Car(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    reg_number: Mapped[str] = mapped_column(index=True)
    pick_up: Mapped[int] = mapped_column(ForeignKey("cargo.id"))
    location: Mapped[int] = mapped_column(ForeignKey("location.id"))
    load_weight: Mapped[str] = mapped_column(index=True)



