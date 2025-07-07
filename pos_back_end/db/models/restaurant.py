from pos_back_end.db.base import Base
from sqlalchemy import Column, Integer, String


class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)

    restaurant_name = Column(String, nullable=False)
    test_column = Column(String)
