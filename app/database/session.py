from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import get_app_settings

app_settings = get_app_settings()

Base = declarative_base()
db = f"mysql+pymysql://{app_settings.db_user}:{app_settings.db_pass}@{app_settings.db_url}:{app_settings.db_port}/{app_settings.db_name}"
engine = create_engine(db, echo=True)
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


def create_tables():
    Base.metadata.create_all(bind=engine)
