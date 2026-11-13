from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.models.user import User
class Link(Base):
    __tablename__ = "links"
    alias: Mapped[str] = mapped_column(primary_key=True) 
    target_url: Mapped[str]
    owner_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))