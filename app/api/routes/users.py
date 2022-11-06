from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_users():
    pass


@router.put("/")
def update_user():
    pass


@router.delete("/")
def delete_user():
    pass


@router.get("/{user_id}")
def get_user():
    pass
