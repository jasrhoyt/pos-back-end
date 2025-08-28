from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
def get_user_info():
    return {"user": "This is user info"}