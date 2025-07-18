from pos_back_end.api.admin.admin_request_models import PostAdminRequestBody
from pos_back_end.db.models.admin import Admin


class AdminServices:

    @staticmethod
    def create_admin(request: PostAdminRequestBody):
        new_admin = Admin(
            email=request.email,
            password=request.password,
            first_name=request.first_name,
            last_name=request.last_name,
            company_name=request.company_name,
            phone_number=request.phone_number
        )

        return new_admin


