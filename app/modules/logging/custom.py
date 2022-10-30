import os
from logging import *
from logging.handlers import TimedRotatingFileHandler
from app.core.config import get_app_settings


class CustomLogger:
    @classmethod
    def get_logger(cls, *, logger_name="logger") -> Logger:
        logging_config = cls.load_logging_config()

        logger = getLogger(logger_name)
        logger.setLevel(logging_config.logging_level)

        cls.create_file_path()

        format = Formatter(logging_config.logging_format)

        stream_handler = StreamHandler()
        timed_rotating_file_handler = TimedRotatingFileHandler(
            filename=logging_config.file_path + logger_name,
            when="midnight",
            interval=1,
            encoding="utf-8",
        )

        timed_rotating_file_handler.suffix = "log-%Y%m%d"  # log-YYYYMMdd

        stream_handler.setFormatter(format)
        timed_rotating_file_handler.setFormatter(format)

        logger.addHandler(stream_handler)
        logger.addHandler(timed_rotating_file_handler)
        return logger

    @classmethod
    def load_logging_config(cls):
        app_settings = get_app_settings()

        logging_config = {
            "logging_level": app_settings.logging_level,
            "file_path": app_settings.file_path,
            "logging_format": app_settings.logging_format,
        }
        return logging_config

    @classmethod
    def create_file_path(cls) -> None:
        logging_config = cls.load_logging_config()

        if not os.path.exists(logging_config.file_path):
            os.makedirs(logging_config.file_path)
