from sqlalchemy.orm import Session

from pos_back_end.db.models.menu_category import MenuCategory
from pos_back_end.db.models.menu_item import MenuItem


class MenuCategoryServices:

    @staticmethod
    def get_menu_categories(restaurant_id, db):
        categories = (db.query(MenuCategory)
                      .join(MenuItem)
                      .where(MenuCategory.restaurant_id == restaurant_id)
                      .all())
        menu_categories = [MenuCategory.model_validate(category) for category in categories]

