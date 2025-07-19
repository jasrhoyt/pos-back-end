from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from pos_back_end.api.restaurant.restaurant_models import PostRestaurantRequestBody
from pos_back_end.db.dependencies import get_db
from pos_back_end.db.models.restaurant import Restaurant

router = APIRouter()


@router.get('/restaurants')
def get_restaurants(admin_id: int, db: Session = Depends(get_db)):
    return db.query(Restaurant).where(Restaurant.admin_id == admin_id).all()


@router.post('/restaurants')
def post_restaurant(request: PostRestaurantRequestBody, db: Session = Depends(get_db)):

    if request.address is None and not request.use_address_on_file:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

