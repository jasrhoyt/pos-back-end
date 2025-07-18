from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from sqlalchemy.orm import Session
from pos_back_end.db.dependencies import get_db
from pos_back_end.api.admin.models.admin_request_models import LoginRequestBody, LoginResponseBody, PostAdminRequestBody, PostAdminResponseBody, \
    AddressRequestAndResponse
from .models.state_models import StateResponseBody, StateItem
from .services.address_services import AddressServices
from .services.admin_services import AdminServices
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


@router.post("/admin")
def create_admin(request: PostAdminRequestBody, db: Session = Depends(get_db)):

    existing_admin: Admin = LoginServices().validate_admin_email(
        request.email,
        db
    )

    if existing_admin:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already in use.",
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


@router.get("/states")
def get_states(db: Session = Depends(get_db)):

    states = AddressServices().get_states(db)

    state_items = [StateItem.from_orm(state) for state in states]

    return StateResponseBody(states=state_items)
