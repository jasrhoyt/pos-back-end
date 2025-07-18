
from fastapi import APIRouter
from .restaraunt_requests import router as get_restaurant_router

router = APIRouter()
router.include_router(get_restaurant_router)