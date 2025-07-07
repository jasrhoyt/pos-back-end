from pos_back_end.db.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
