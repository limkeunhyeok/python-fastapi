from fastapi import APIRouter

router = APIRouter()


@router.post("/sign-in")
def sign_in():
    pass


@router.post("/sign-up")
def sign_up():
    pass


@router.post("/refresh-token")
def refresh_token():
    pass


@router.get("/me")
def get_user_by_token():
    pass
