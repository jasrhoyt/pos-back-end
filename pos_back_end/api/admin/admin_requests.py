from fastapi import APIRouter

router = APIRouter()


@router.get("/admin/info")
def get_admin_info():
    return {"admin": "This is admin info"}
