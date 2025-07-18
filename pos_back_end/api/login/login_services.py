from fastapi import APIRouter
from sqlalchemy.orm import Session
from pos_back_end.db.models.admin import Admin


router = APIRouter()


class LoginServices:

    @staticmethod
    def get_admin_data(email: str, password: str, db: Session):
        return db.query(Admin).filter(Admin.email == email, Admin.password == password).one_or_none()

    @staticmethod
    def validate_admin_email(email: str, db: Session):
        return db.query(Admin).filter(Admin.email == email).first()

