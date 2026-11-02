from datetime import datetime
from typing import Optional

from sqlalchemy import (
    String,
    Integer,
    Boolean,
    DateTime,
    ForeignKey,
    UniqueConstraint
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Room(Base):
    __tablename__ = "rooms"

    __table_args__ = (
        UniqueConstraint(
            "hotel_id",
            "room_number",
            name="uq_rooms_hotel_room_number"
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    hotel_id: Mapped[int] = mapped_column(
        ForeignKey("hotels.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    room_type_id: Mapped[int] = mapped_column(
        ForeignKey("room_types.id", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )

    room_number: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    floor: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="available",
        nullable=False
    )

    housekeeping_status: Mapped[str] = mapped_column(
        String(30),
        default="clean",
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
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

    room_type = relationship(
        "RoomType",
        back_populates="rooms"
    )