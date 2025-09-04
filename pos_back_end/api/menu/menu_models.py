from typing import List
from pydantic import ConfigDict
from pos_back_end.api.common_services import CommonBaseModel


class Ingredients(CommonBaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class MenuItem(CommonBaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    item_price: float
    ingredients: List[Ingredients]


class MenuCategoryItems(CommonBaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    category_name: str


class MenuCategoriesResponseBody(CommonBaseModel):
    categories: List[MenuCategoryItems]


class PostMenuCategoryRequestBody(CommonBaseModel):
    restaurant_id: int
    category_name: str


class PostMenuItemRequestBody(CommonBaseModel):
    item_name: str
    item_price: float
    ingredients: List[Ingredients]


class PostMenuCategoryResponseBody(CommonBaseModel):
    category_name: str
    restaurant_id: int


class PostMenuItemResponseBody(CommonBaseModel):
    category_id: int
