from pydantic import BaseModel, ConfigDict, field_validator
from typing import Any

from pos_back_end.api.address.address_models import AddressRequestAndResponse
from pos_back_end.api.common_services import CommonBaseModel


class LoginRequestBody(CommonBaseModel):
    email: str
    password: str


class LoginResponseBody(CommonBaseModel):
    user_id: int
    first_name: str
    last_name: str
    company_name: str
    email: str
    phone_number: str
    address: AddressRequestAndResponse


class PostAdminRequestBody(CommonBaseModel):
    first_name: str
    last_name: str
    company_name: str
    email: str
    password: str
    address: AddressRequestAndResponse
    phone_number: str


class PostAdminResponseBody(LoginResponseBody):
    message: str
