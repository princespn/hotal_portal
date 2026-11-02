from datetime import datetime
from typing import Optional

from sqlalchemy import (
    String,
    Text,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Guest(Base):
    __tablename__ = "guests"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    hotel_id: Mapped[int] = mapped_column(
        ForeignKey("hotels.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    last_name: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True
    )

    email: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True
    )

    phone: Mapped[Optional[str]] = mapped_column(
        String(30),
        nullable=True
    )

    address: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True
    )

    city: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True
    )

    country: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True
    )

    id_type: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True
    )

    id_number: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    hotel = relationship("Hotel")