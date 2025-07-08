from pos_back_end.db.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from pos_back_end.db.models import MenuItem
from pos_back_end.db.models.ingredient import Ingredient


class MenuItemIngredientJoin(Base):
    __tablename__ = 'menu_item_ingredient_joins'

    id = Column(Integer, primary_key=True)

    menu_item_id = Column(Integer, ForeignKey(MenuItem.id))
    menu_item = relationship("MenuItem", back_populates="menu_item_ingredient_joins")
    ingredient_id = Column(Integer, ForeignKey(Ingredient.id))
    ingredient = relationship("Ingredient", back_populates="menu_item_ingredient_joins")

