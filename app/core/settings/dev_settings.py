import logging
from app.core.settings.app_settings import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    title: str = "Python boilerplate for dev"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = ".env.development"
