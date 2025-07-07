from pos_back_end.db.base import Base
from sqlalchemy import Column, Integer, String


class RestaurantAddress(Base):
    __tablename__ = 'restaurant_addresses'
    id = Column(Integer, primary_key=True)

    address = Column(String)
    city = Column(String)
