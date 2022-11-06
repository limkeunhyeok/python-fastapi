from app.database.repositories.base import BaseRepository
from app.database.session import Session
from app.models.posts import Post


class PostsRepository(BaseRepository):
    def __init__(self) -> None:
        session = Session()
        super().__init__(session, Post)
