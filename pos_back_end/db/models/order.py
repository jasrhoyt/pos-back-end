from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pos_back_end.db.base import Base
from pos_back_end.db.models.menu_category import MenuCategory


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
