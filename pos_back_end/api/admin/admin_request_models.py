from typing import Optional

from pydantic import BaseModel

from pos_back_end.db.models.address import Address


class LoginRequestBody(BaseModel):
    email: str
    password: str


class AddressResponse(BaseModel):
    street_address: str
    city: str
    state: str
    zipcode: str

    class Config:
        from_attributes = True  # Allows mapping from SQLAlchemy objects


class LoginResponseBody(BaseModel):
    first_name: str
    last_name: str
    company_name: str
    email: str
    address: Optional[AddressResponse] = None

    class Config:
        from_attributes = True  # Allows mapping from SQLAlchemy objects


class PostAdminRequestBody(BaseModel):
    email: str
    password: str
    first_name = str
    last_name = str
    company_name = str


class PostAdminResponseBody(LoginResponseBody):
    message: str
