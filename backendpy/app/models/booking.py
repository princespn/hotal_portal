from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import (
    BigInteger,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    __table_args__ = (
        UniqueConstraint(
            "hotel_id",
            "booking_number",
            name="uq_bookings_hotel_number",
        ),
    )

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    hotel_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("hotels.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    booking_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    guest_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("guests.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    check_in: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    check_out: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    adults: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )

    children: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="pending",
    )

    source: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="direct",
    )

    subtotal: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=Decimal("0.00"),
    )

    tax: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=Decimal("0.00"),
    )

    discount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=Decimal("0.00"),
    )

    total: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=Decimal("0.00"),
    )

    paid_amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=Decimal("0.00"),
    )

    due_amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=Decimal("0.00"),
    )

    special_requests: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    # Relationships

    hotel = relationship(
        "Hotel",
        back_populates="bookings",
    )

    guest = relationship(
        "Guest",
        back_populates="bookings",
    )

    booking_rooms: Mapped[List["BookingRoom"]] = relationship(
        "BookingRoom",
        back_populates="booking",
        cascade="all, delete-orphan",
    )
