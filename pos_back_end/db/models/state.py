from sqlalchemy import Column, Integer, String

from pos_back_end.db.base import Base

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)

    state_name = Column(String)
    state_code = Column(String)