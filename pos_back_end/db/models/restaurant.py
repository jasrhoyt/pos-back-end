from sqlalchemy.orm import relationship
from pos_back_end.db.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

from pos_back_end.db.models.address import Address
from pos_back_end.db.models.admin import Admin


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String, nullable=False)

    admin_id = Column(Integer, ForeignKey(Admin.id))
    admin = relationship(Admin, back_populates="restaurants")

    address_id = Column(Integer, ForeignKey(Address.id), unique=True)
    address = relationship(Address, back_populates="restaurant_address")

    menu_categories = relationship("MenuCategory", back_populates="restaurant")
