from typing import List

from pydantic import ConfigDict

from pos_back_end.api.common_services import CommonBaseModel


class MenuCategoryItems(CommonBaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    restaurant_name: str
    restaurant_email: str
    phone_number: str


class RestaurantsResponseBody(CommonBaseModel):
    restaurants: List[MenuCategoryItems]