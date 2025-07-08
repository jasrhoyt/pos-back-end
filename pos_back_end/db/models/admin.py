from pos_back_end.db.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pos_back_end.db.models.address import Address


class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    company_name = Column(String, nullable=False)

    address_id = Column(Integer, ForeignKey(Address.id), unique=True)
    address = relationship(Address, back_populates="corporate_address")

    restaurants = relationship("Restaurant", back_populates="admin")
