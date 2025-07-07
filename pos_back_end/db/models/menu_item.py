from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pos_back_end.db.base import Base
from pos_back_end.db.models.menu_category import MenuCategory


class MenuItem(Base):
    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)

    menu_category_id = Column(Integer, ForeignKey(MenuCategory.id), nullable=False)
    menu_category = relationship(MenuCategory, back_populates="menu_item", uselist=False)
