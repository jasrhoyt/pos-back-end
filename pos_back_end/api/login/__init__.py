
from fastapi import APIRouter
from .login_requests import router as get_login_router

router = APIRouter()
router.include_router(get_login_router)