from pos_back_end.db.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    ingredient_name = Column(String, unique=True, nullable=False)

    menu_item_ingredient_joins = relationship("MenuItemIngredientJoin", back_populates="ingredient")
    menu_items = relationship(
        "MenuItem",
        secondary="menu_item_ingredient_joins",
        back_populates="ingredients",
        overlaps="menu_item_ingredient_joins"
    )
