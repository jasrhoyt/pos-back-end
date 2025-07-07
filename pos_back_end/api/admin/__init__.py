from fastapi import APIRouter
from .admin_requests import router as get_admin_router

router = APIRouter()
router.include_router(get_admin_router)
