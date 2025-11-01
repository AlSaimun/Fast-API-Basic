from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float, Text
from app.db.config import Base
from datetime import datetime, timezone


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))