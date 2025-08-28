from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pos_back_end.api.address.address_services import AddressServices
from pos_back_end.api.admin.admin_services import AdminServices
from pos_back_end.api.restaurant.restaurant_models import PostRestaurantRequestBody, RestaurantItem
from pos_back_end.api.restaurant.restaurant_services import RestaurantServices
from pos_back_end.db.dependencies import get_db
from pos_back_end.db.models.address import Address

router = APIRouter()


@router.get('/restaurants')
def get_restaurants(admin_id: int, db: Session = Depends(get_db)):

    return RestaurantServices.get_restaurants(admin_id, db)


@router.post('/restaurants')
def post_restaurant(request: PostRestaurantRequestBody, db: Session = Depends(get_db)):

    admin = AdminServices().get_admin(request.admin_id, db)

    new_address: Address | None = None

    if request.address is not None:
        new_address = AddressServices().create_address(request.address)
        db.add(new_address)
        db.flush()

    address_id = admin.address_id if request.use_address_on_file else new_address.id

    new_restaurant = RestaurantServices.post_restaurant(request.restaurant_name, request.restaurant_email, request.phone_number, request.admin_id, address_id)
    db.add(new_restaurant)
    db.flush()

    db.commit()

    return RestaurantItem.from_orm(new_restaurant)
