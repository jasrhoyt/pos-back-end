from fastapi import FastAPI
from pos_back_end.api.user import router as user_router
from pos_back_end.api.admin import router as admin_router

app = FastAPI()

app.include_router(user_router)
app.include_router(admin_router)