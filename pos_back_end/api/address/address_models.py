from typing import List
from pydantic import BaseModel, ConfigDict


class StateItem(BaseModel):
    id: int
    state_name: str
    state_code: str

    model_config = ConfigDict(from_attributes=True)


class StateResponseBody(BaseModel):
    states: List[StateItem]


class AddressRequestAndResponse(BaseModel):
    street_address: str
    city: str
    state: str
    zipcode: str

    model_config = ConfigDict(from_attributes=True)

