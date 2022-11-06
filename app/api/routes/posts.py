from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_posts():
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
