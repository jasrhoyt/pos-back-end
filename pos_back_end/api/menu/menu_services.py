from pkg_resources import require
from sqlalchemy.orm import selectinload

from pos_back_end.api.menu.menu_models import MenuCategoryItems, MenuCategoriesResponseBody, Ingredients, \
    PostMenuCategoryRequestBody, PostMenuCategoryResponseBody, PostMenuItemRequestBody
from pos_back_end.db.models.ingredient import Ingredient
from pos_back_end.db.models.menu_category import MenuCategory
from pos_back_end.db.models.menu_item import MenuItem


class MenuServices:

    @staticmethod
    def get_menu_categories(restaurant_id, db):

        categories = (db.query(MenuCategory)
                      .options(
            selectinload(MenuCategory.menu_items)
            .selectinload(MenuItem.ingredients)
        )
                      .where(MenuCategory.restaurant_id == restaurant_id)
                      .all())

        menu_categories_data = []

        for category in categories:

            menu_items = []
            for item in category.menu_items:

                ingredients = [Ingredients.model_validate(ingredient) for ingredient in item.ingredients]

                menu_item = MenuItem(
                    id=item.id,
                    item_price=item.item_price,
                    ingredients=ingredients
                )
                menu_items.append(menu_item)

            category_response = MenuCategoryItems(
                id=category.id,
                category_name=category.restaurant.name,
            )

            menu_categories_data.append(category_response)

        return MenuCategoriesResponseBody(categories=menu_categories_data)


    @staticmethod
    def create_menu_category(request: PostMenuCategoryRequestBody):

        return MenuCategory(
            category_name=request.name,
            restaurant_id=request.restaurant_id
        )


    @staticmethod
    def create_menu_item(request: PostMenuItemRequestBody):

        return MenuItem(
            item_name=request.item_name,
            item_price=request.item_price,
            ingredients=request.ingredients # adding a comment to test
        )