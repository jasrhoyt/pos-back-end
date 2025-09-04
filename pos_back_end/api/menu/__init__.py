
from fastapi import APIRouter
from .menu_requests import router as get_category_router

router = APIRouter()
router.include_router(get_category_router)