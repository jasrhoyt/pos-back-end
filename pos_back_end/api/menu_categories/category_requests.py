from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from pos_back_end.db.dependencies import get_db

router = APIRouter()

@router.get("/categories")
def get_menu_categories(restaurant_id: int, db: Session = Depends(get_db)):
