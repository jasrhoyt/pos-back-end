from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Relationship

from pos_back_end.db.base import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    order_location = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    order_items = Relationship("OrderItem", back_populates="order")


# def get_the_time():
#     print("test value:", datetime.now())
#
#
# get_the_time()
