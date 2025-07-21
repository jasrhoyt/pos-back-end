from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from pos_back_end.api.address.address_models import AddressRequestAndResponse
from pos_back_end.api.common_services import CommonServices


class PostRestaurantRequestBody(BaseModel):
    admin_id: int
    restaurant_name: str
    restaurant_email: str
    use_address_on_file: Optional[bool] = False
    address: Optional[AddressRequestAndResponse] = None
    phone_number: str


class RestaurantItem(BaseModel):
    id: int
    restaurant_name: str
    restaurant_email: str
    phone_number: str

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=CommonServices().to_camel_case,  # creates camel case aliases
        populate_by_name=True  # lets you use snake or camel case
    )


class RestaurantsResponseBody(BaseModel):
    restaurants: List[RestaurantItem]