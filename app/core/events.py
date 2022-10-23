from typing import Callable

from fastapi import FastAPI
from loguru import logger

from app.core.settings.app_settings import AppSettings


def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:
    async def start_app() -> None:
        # db connect
        pass

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    @logger.catch
    async def stop_app() -> None:
        # db close
        pass

    return stop_app
