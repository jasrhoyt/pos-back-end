from fastapi import FastAPI
from pos_back_end.api.user import router as user_router
from pos_back_end.api.admin import router as admin_router
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pos_back_end.db.base import Base
from pos_back_end.db.models import Admin, User, Restaurant
import os

app = FastAPI()
os.makedirs('pos_back_end/db', exist_ok=True)
engine = create_engine('sqlite:///pos_back_end/db/pos_system_database.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(admin_router)
