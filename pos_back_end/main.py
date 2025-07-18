from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware

from pos_back_end.api.exception_handlers import validation_exception_handler
from pos_back_end.api.user import router as user_router
from pos_back_end.api.admin import router as admin_router
from pos_back_end.api.address import router as address_router
from pos_back_end.api.login import router as login_router
from pos_back_end.api.restaurant import router as restaurant_router
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs('pos_back_end/db', exist_ok=True)


app.include_router(user_router)
app.include_router(admin_router)
app.include_router(address_router)
app.include_router(login_router)
app.include_router(restaurant_router)

app.exception_handler(RequestValidationError)(validation_exception_handler)