from pos_back_end.db.base import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
