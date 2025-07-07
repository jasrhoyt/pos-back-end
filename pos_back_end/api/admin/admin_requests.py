from fastapi import APIRouter
from .admin_request_models import AdminRequestBody
router = APIRouter()


@router.post("/admin")
def get_admin(request: AdminRequestBody):

    user_id = request.user_id
    password = request.password

    return {"admin": "This is admin info"}
