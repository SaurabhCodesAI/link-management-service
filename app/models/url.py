from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
class Link(Base):
    __tablename__ = "links"
    alias: Mapped[str] = mapped_column(primary_key=True) 
    target_url: Mapped[str]