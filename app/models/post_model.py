from .base_model import BaseModel
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship


class Post(BaseModel):
    __tablename__ = "post"

    title = Column(String, nullable=False)
    description = Column(Text)
    user_id = Column(
        Integer, ForeignKey("user.id", ondelete="CASCADE"), primary_key=True
    )

    user = relationship("user")
