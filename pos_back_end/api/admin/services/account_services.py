from sqlalchemy.orm import Session

from pos_back_end.db.models.state import State


class AccountServices:

    @staticmethod
    def get_states(db: Session):
        return db.query(State).all()


