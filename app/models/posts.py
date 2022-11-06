from .base import BaseModel
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from app.database.session import Base
from sqlalchemy.orm import relationship


class Post(Base, BaseModel):
    __tablename__ = "post"

    title = Column(String(30), nullable=False)
    description = Column(Text(1000000))
    user_id = Column(
        Integer, ForeignKey("user.id", ondelete="CASCADE"), primary_key=True
    )

    user = relationship("User")
