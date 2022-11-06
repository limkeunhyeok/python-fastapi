from app.database.session import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.sql.expression import text
from app.models.base import BaseModel


class User(Base, BaseModel):
    __tablename__ = "user"

    email = Column(String(30), nullable=False, unique=True)
    password = Column(String(120), nullable=False)
    username = Column(String(30), nullable=False)
