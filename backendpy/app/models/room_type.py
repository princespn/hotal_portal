from datetime import datetime

from sqlalchemy import (
    String,
    Text,
    Integer,
    Numeric,
    Boolean,
    DateTime,
    ForeignKey,
    UniqueConstraint
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class RoomType(Base):
    __tablename__ = "room_types"

    __table_args__ = (
        UniqueConstraint(
            "hotel_id",
            "name",
            name="uq_room_types_hotel_name"
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

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    max_adults: Mapped[int] = mapped_column(
        Integer,
        default=2
    )

    max_children: Mapped[int] = mapped_column(
        Integer,
        default=1
    )

    base_price: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=0
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

    hotel = relationship(
        "Hotel",
        back_populates="room_types"
    )

    rooms = relationship(
        "Room",
        back_populates="room_type"
    )