from fastapi import APIRouter
from .user_requests import router as get_user_requests

router = APIRouter()
router.include_router(get_user_requests)
