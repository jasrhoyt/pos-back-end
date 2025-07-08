from sqlalchemy.orm import Session

from pos_back_end.db.models.admin import Admin


class LoginServices:

    @staticmethod
    def get_user_data(email: str, password: str, db: Session):
        return db.query(Admin).filter(Admin.email == email, Admin.password == password).one_or_none()
