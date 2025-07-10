from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from sqlalchemy.orm import Session
from pos_back_end.db.dependencies import get_db
from .admin_request_models import LoginRequestBody, LoginResponseBody, PostAdminRequestBody, PostAdminResponseBody, \
    AddressResponse
from .services.account_services import AccountServices
from .services.login_services import LoginServices
from ...db.models.admin import Admin

router = APIRouter()


@router.post("/login")
def login(request: LoginRequestBody, db: Session = Depends(get_db)):

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
        first_name=admin.first_name,
        last_name=admin.last_name,
        company_name=admin.company_name,
        email=admin.email,
        address=AddressResponse(
            street_address=address.street_address,
            city=address.city,
            state=address.state,
            zipcode=address.zipcode
        ) if address is not None else None
    )


@router.post("/admin")
def login(request: PostAdminRequestBody, db: Session = Depends(get_db)):

    service = LoginServices()

    existing_admin: Admin = service.validate_admin_email(
        request.email,
        db
    )

    if existing_admin:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already in use.",
        )

    new_admin = service.create_admin(request, db)

    address = new_admin.address

    return PostAdminResponseBody(
        first_name=new_admin.first_name,
        last_name=new_admin.last_name,
        company_name=new_admin.company_name,
        email=new_admin.email,
        address=AddressResponse(
            street_address=address.street_address,
            city=address.city,
            state=address.state,
            zipcode=address.zipcode
        ) if address is not None else None,
        message=f"Account with email {new_admin.email} successfully create!"
    )


@router.get("/states")
def get_states(db: Session = Depends(get_db)):

    service = AccountServices()
    states = service.get_states(db)

    return states
