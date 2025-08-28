
from fastapi import APIRouter
from .address_requests import router as get_address_router

router = APIRouter()
router.include_router(get_address_router)