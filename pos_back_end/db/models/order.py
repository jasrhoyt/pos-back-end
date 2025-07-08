from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Relationship

from pos_back_end.db.base import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    order_location = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    order_items = Relationship("OrderItem", back_populates="order")

