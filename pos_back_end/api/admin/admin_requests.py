from fastapi import APIRouter
from .admin_request_models import AdminRequestBody
router = APIRouter()


@router.post("/login")
def login(request: AdminRequestBody):

    email = request.email
    password = request.password

    return {"admin": f"This is admin info: ${email}"}
