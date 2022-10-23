import logging
from app.core.settings.app_settings import AppSettings


class LocalAppSettings(AppSettings):
    debug: bool = True

    title: str = "Python boilerplate for local"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = ".env.local"
