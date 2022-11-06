from fastapi import APIRouter
from app.database.repositories.posts import PostsRepository

router = APIRouter()
# postsRepository = PostsRepository()


@router.get("/")
def get_posts():
    # entities = postsRepository.find_all()
    # return entities
    pass


@router.put("/")
def update_post():
    pass


@router.delete("/")
def delete_post():
    pass


@router.get("/{post_id}")
def get_post():
    pass
