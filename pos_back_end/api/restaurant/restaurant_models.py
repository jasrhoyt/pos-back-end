from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from pos_back_end.api.address.address_models import AddressRequestAndResponse
from pos_back_end.api.common_services import CommonServices, CommonBaseModel


class PostRestaurantRequestBody(CommonBaseModel):
    admin_id: int
    restaurant_name: str
    restaurant_email: str
    use_address_on_file: Optional[bool] = False
    address: Optional[AddressRequestAndResponse] = None
    phone_number: str


class RestaurantItem(CommonBaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    restaurant_name: str
    restaurant_email: str
    phone_number: str


class RestaurantsResponseBody(CommonBaseModel):
    restaurants: List[RestaurantItem]