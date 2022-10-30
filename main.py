import uvicorn
from app.core.config import get_app_settings


if __name__ == "__main__":
    settings = get_app_settings()
    uvicorn.run(
        app="app:app",
        host=settings.app_host,
        port=settings.app_port,
        log_level="info"
    )
