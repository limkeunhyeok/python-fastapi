from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import get_app_settings

app_settings = get_app_settings()

Base = declarative_base()

engine = create_engine(app_settings.database_url, echo=True)
Session = sessionmaker(bind=engine)


def get_db() -> Session:
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        logger.error(f"Database Error: {e}")
        session.rollback()
        raise e
    finally:
        session.close()
