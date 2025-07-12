from pydantic import BaseModel, Field, ConfigDict

from pos_back_end.db.models.address import Address


class LoginRequestBody(BaseModel):
    email: str
    password: str


class AddressRequestAndResponse(BaseModel):
    street_address: str
    city: str
    state: str
    zipcode: str

    model_config = ConfigDict(from_attributes=True)


class LoginResponseBody(BaseModel):
    first_name: str
    last_name: str
    company_name: str
    email: str
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
