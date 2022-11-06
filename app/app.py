from fastapi import Depends, FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware

from app.core.config import get_app_settings
from app.common.exception.http_exception import http_exception_handler
from app.common.exception.validation_exception import http_validation_exception_handler
from app.database.session import create_tables
from app.api.routes.api import router as api_router


def get_application() -> FastAPI:
    settings = get_app_settings()

    settings.configure_logging()

    create_tables()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_exception_handler(HTTPException, http_exception_handler)
    application.add_exception_handler(
        RequestValidationError, http_validation_exception_handler
    )

    application.include_router(api_router)

    return application


app = get_application()


@app.get("/")
def test():
    return {"message": "hello world"}
