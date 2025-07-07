from pos_back_end.db.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from pos_back_end.db.models.restaurant import Restaurant


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)

    street_address = Column(String)
    city = Column(String)
    state = Column(String)
    zipcode = Column(String)

    restaurant_address = relationship(Restaurant, back_populates="address", uselist=False)
    corporate_address = relationship(Restaurant, back_populates="address", uselist=False)
