from .base_model import BaseModel
from sqlalchemy import Column, String


class User(BaseModel):
    __tablename__ = "user"

    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    username = Column(String, nullable=False)
