from fastapi import APIRouter
from app.database.repositories.users import UsersRepository

router = APIRouter()
usersRepository = UsersRepository()


@router.get("/")
def get_users():
    entities = usersRepository.find_all()
    return entities


@router.put("/")
def update_user():
    pass


@router.delete("/")
def delete_user():
    pass


@router.get("/{user_id}")
def get_user():
    pass
