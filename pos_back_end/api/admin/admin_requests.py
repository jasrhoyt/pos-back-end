from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from sqlalchemy.orm import Session
from pos_back_end.db.dependencies import get_db
from .admin_request_models import LoginRequestBody, LoginResponseBody
from .services.login_services import LoginServices
from ...db.models.admin import Admin

router = APIRouter()


@router.post("/login")
def login(request: LoginRequestBody, db: Session = Depends(get_db)):

    service = LoginServices()

    admin: Admin = service.get_user_data(
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
        first_name=admin.first_name,
        last_name=admin.last_name,
        company_name=admin.company_name,
        street_address=address.street_address if address is not None else None,
        city=address.city if address is not None else None,
        state=address.state if address is not None else None,
        zipcode=address.zipcode if address is not None else None
    )
