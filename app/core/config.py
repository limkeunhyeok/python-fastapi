from functools import lru_cache
from typing import Dict, Type

from app.core.settings.base_settings import BaseAppSettings, AppEnvTypes
from app.core.settings.app_settings import AppSettings
from app.core.settings.local_settings import LocalAppSettings
from app.core.settings.dev_settings import DevAppSettings
from app.core.settings.prod_settings import ProdAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.local: LocalAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()
