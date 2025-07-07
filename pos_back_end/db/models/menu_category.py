from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pos_back_end.db.base import Base
from pos_back_end.db.models import Restaurant


class MenuCategory(Base):
    __tablename__ = 'menu_category'

    id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False)

    restaurant_id = Column(Integer, ForeignKey(Restaurant.id), nullable=False)
    restaurant = relationship(Restaurant, back_populates="menu_category", uselist=False)

    menu_item = relationship("MenuItem", back_populates="menu_category", uselist=False)
