
from datetime import datetime, date
from decimal import Decimal

from sqlalchemy import (
    BigInteger, Integer, Numeric, Date, DateTime,
    ForeignKey, CheckConstraint, func
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class BookingRoom(Base):
    __tablename__ = "booking_rooms"

    __table_args__ = (
        CheckConstraint("rate >= 0", name="chk_booking_rooms_rate"),
        CheckConstraint("adults >= 1", name="chk_booking_rooms_adults"),
        CheckConstraint("children >= 0", name="chk_booking_rooms_children"),
        CheckConstraint(
            "check_out > check_in",
            name="chk_booking_rooms_dates"
        ),
    )

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True
    )

    booking_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("bookings.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    room_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("rooms.id", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )

    rate: Mapped[Decimal] = mapped_column(
        Numeric(12, 2), nullable=False
    )

    adults: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    children: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    check_in: Mapped[date] = mapped_column(Date, nullable=False)
    check_out: Mapped[date] = mapped_column(Date, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    booking: Mapped["Booking"] = relationship(
        back_populates="booking_rooms"
    )

    room: Mapped["Room"] = relationship(
        back_populates="booking_rooms"
    )
