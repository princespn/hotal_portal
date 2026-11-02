from datetime import datetime

from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Hotel(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    slug: Mapped[str] = mapped_column(
        String(180),
        unique=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    phone: Mapped[str] = mapped_column(
        String(30),
        nullable=True
    )

    address: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )

    state: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )

    country: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )

    pincode: Mapped[str] = mapped_column(
        String(20),
        nullable=True
    )

    timezone: Mapped[str] = mapped_column(
        String(100),
        default="Asia/Kolkata"
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="INR"
    )

    status: Mapped[bool] = mapped_column(
        Boolean,
        default=True
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

    hotel_members = relationship(
        "HotelUser",
        back_populates="hotel",
        cascade="all, delete-orphan"
    )