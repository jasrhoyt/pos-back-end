from typing import Optional
from pydantic import BaseModel
from pos_back_end.api.address.address_models import AddressRequestAndResponse


class PostRestaurantRequestBody(BaseModel):
    restaurant_name: str
    use_address_on_file: Optional[bool] = False
    address: Optional[AddressRequestAndResponse] = None
