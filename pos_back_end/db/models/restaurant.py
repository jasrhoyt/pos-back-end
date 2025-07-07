from sqlalchemy.orm import relationship
from pos_back_end.db.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

from pos_back_end.db.models.address import Address


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String, nullable=False)

    address_id = Column(Integer, ForeignKey(Address.id), unique=True)
    address = relationship(Address, back_populates="restaurant_address")

    menu_category = relationship("MenuCategory", back_populates="restaurant")
