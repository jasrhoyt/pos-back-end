from sqlalchemy.orm import Session

from pos_back_end.api.admin.models.admin_request_models import PostAdminRequestBody
from pos_back_end.db.models.admin import Admin


class LoginServices:

    @staticmethod
    def get_admin_data(email: str, password: str, db: Session):
        return db.query(Admin).filter(Admin.email == email, Admin.password == password).one_or_none()

    @staticmethod
    def validate_admin_email(email: str, db: Session):
        return db.query(Admin).filter(Admin.email == email).first()

    @staticmethod
    def create_admin(request: PostAdminRequestBody):
        new_admin = Admin(
            email=request.email,
            password=request.password,
            first_name=request.first_name,
            last_name=request.last_name,
            company_name=request.company_name
        )

        return new_admin

