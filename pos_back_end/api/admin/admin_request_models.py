from pydantic import BaseModel, Field, ConfigDict

from pos_back_end.api.address.address_models import AddressRequestAndResponse
from pos_back_end.db.models.address import Address


class LoginRequestBody(BaseModel):
    email: str
    password: str


class LoginResponseBody(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    company_name: str
    email: str
    phone_number: str
    address: AddressRequestAndResponse

    model_config = ConfigDict(from_attributes=True)


class PostAdminRequestBody(BaseModel):
    first_name: str
    last_name: str
    company_name: str
    email: str
    password: str
    address: AddressRequestAndResponse
    phone_number: str


class PostAdminResponseBody(LoginResponseBody):
    message: str
