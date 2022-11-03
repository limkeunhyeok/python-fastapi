from app.database.session import Base
from sqlalchemy import Column, Integer, TIMESTAMP
from sqlalchemy.sql.expression import text


class BaseModel(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
