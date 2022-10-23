import logging
import os
import sys
from typing import Any, Dict, List, Tuple
from loguru import logger
from app.core.settings.base_settings import BaseAppSettings
from app.core.logging import InterceptHandler


class AppSettings(BaseAppSettings):
    debug: bool = False
    docs_url: str = "/api-docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "Python boilerplate"
    description: str = "Python boilplate server with fastapi"
    version: str = "0.1.0"

    database_url: str = f"mongodb://{os.getenv('MONGODB_USER')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_IP')}:{os.getenv('MONGODB_PORT')}"

    app_host: str = os.getenv("APP_HOST")
    app_port: int = os.getenv("APP_PORT")

    secret_key: str = os.getenv("SECLET_KEY")
    salt_round: int = os.getenv("SALT_ROUND")

    api_prefix: str = "/"

    jwt_token_prefix: str = "Token"

    allowed_hosts: List[str] = ["*"]

    logging_level: int = logging.INFO
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    class Config:
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "description": self.description,
            "version": self.version,
        }

    def configure_logging(self) -> None:
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=self.logging_level)]

        logger.configure(handlers=[{"sink": sys.stderr, "level": self.logging_level}])