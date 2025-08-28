from sqlalchemy import Column, Integer, String

from pos_back_end.db.base import Base

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)

    state_name = Column(String, unique=True)
    state_code = Column(String, unique=True)