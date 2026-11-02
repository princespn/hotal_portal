
from datetime import datetime

from sqlalchemy import (
    BigInteger, String, DateTime, ForeignKey,
    UniqueConstraint, CheckConstraint, func
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class HotelUser(Base):
    __tablename__ = "hotel_users"

    __table_args__ = (
        UniqueConstraint(
            "hotel_id", "user_id",
            name="uq_hotel_users_hotel_user"
        ),
        CheckConstraint(
            "role IN ('owner', 'manager', 'receptionist', 'staff')",
            name="chk_hotel_users_role"
        ),
    )

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True
    )

    hotel_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("hotels.id", ondelete="CASCADE"),
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    role: Mapped[str] = mapped_column(
        String(30), default="staff", nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )

    hotel: Mapped["Hotel"] = relationship(back_populates="memberships")
    user: Mapped["User"] = relationship(back_populates="hotel_memberships")
