from fastapi import APIRouter
from app.api.routes import auth, users, posts

router = APIRouter()

router.include_router(auth.router, tags=["auth"], prefix="/auth")
router.include_router(users.router, tags=["users"], prefix="/users")
router.include_router(posts.router, tags=["posts"], prefix="/posts")
