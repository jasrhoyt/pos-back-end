from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pos_back_end.db.dependencies import get_db
from pos_back_end.db.models.restaurant import Restaurant

router = APIRouter()


@router.get('/restaurants')
def get_restaurants(db: Session = Depends(get_db)):
    return db.query(Restaurant).all()

