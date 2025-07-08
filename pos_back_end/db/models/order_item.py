from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from pos_back_end.db.base import Base
from pos_back_end.db.models.menu_item import MenuItem
from pos_back_end.db.models.order import Order


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)

    order_id = Column(Integer, ForeignKey(Order.id), nullable=False)
    order = relationship("Order", back_populates="order_items")

    menu_item_id = Column(Integer, ForeignKey(MenuItem.id), nullable=False)
    menu_item = relationship("MenuItem", back_populates="order_items")

    order_instructions = Column(String)
    is_complete = Column(Boolean, default=False)
