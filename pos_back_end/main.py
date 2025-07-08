from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from pos_back_end.api.user import router as user_router
from pos_back_end.api.admin import router as admin_router
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
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
engine = create_engine('sqlite:///pos_back_end/db/pos_system_database.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


app.include_router(user_router)
app.include_router(admin_router)
