from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from pos_back_end.db.dependencies import get_db
from pos_back_end.api.admin.admin_models import PostAdminRequestBody, PostAdminResponseBody, \
    AddressRequestAndResponse
from pos_back_end.api.address.address_services import AddressServices
from pos_back_end.api.admin.admin_services import AdminServices
from pos_back_end.api.login.login_services import LoginServices
from ...db.models.admin import Admin

router = APIRouter()


@router.post("/admin")
def post_admin(request: PostAdminRequestBody, db: Session = Depends(get_db)):

    existing_admin: Admin = LoginServices().validate_admin_email(
        request.email,
        db
    )

    if existing_admin:
        return JSONResponse(
            status_code=409,
            content={
                "statusCode": 409,
                "errorMessage": "That email is already in use.",
            }
        )

    new_address = AddressServices().create_address(request.address)

    db.add(new_address)
    db.flush()

    new_admin = AdminServices().create_admin(request)
    new_admin.address_id = new_address.id

    db.add(new_admin)
    db.flush()

    db.commit()

    return PostAdminResponseBody(
        user_id=new_admin.id,
        first_name=new_admin.first_name,
        last_name=new_admin.last_name,
        company_name=new_admin.company_name,
        email=new_admin.email,
        phone_number=new_admin.phone_number,
        address=AddressRequestAndResponse(
            street_address=new_address.street_address,
            city=new_address.city,
            state=new_address.state,
            zipcode=new_address.zipcode
        ),
        message=f"Account with email {new_admin.email} successfully create!"
    )


