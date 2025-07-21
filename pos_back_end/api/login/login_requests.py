from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from pos_back_end.api.admin.admin_models import LoginRequestBody, LoginResponseBody, AddressRequestAndResponse
from pos_back_end.api.login.login_services import LoginServices
from pos_back_end.db.dependencies import get_db
from pos_back_end.db.models.admin import Admin

router = APIRouter()


@router.post("/login")
def login(request: LoginRequestBody, db: Session = Depends(get_db)):
    print('test value:', request)

    service = LoginServices()

    admin: Admin = service.get_admin_data(
        request.email,
        request.password,
        db
    )

    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    address = admin.address

    return LoginResponseBody(
        user_id=admin.id,
        first_name=admin.first_name,
        last_name=admin.last_name,
        company_name=admin.company_name,
        email=admin.email,
        phone_number=admin.phone_number,
        address=AddressRequestAndResponse(
            street_address=address.street_address,
            city=address.city,
            state=address.state,
            zipcode=address.zipcode
        ) if address is not None else None
    )

