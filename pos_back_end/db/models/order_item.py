from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pos_back_end.db.base import Base
from pos_back_end.db.models.menu_category import MenuCategory


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)