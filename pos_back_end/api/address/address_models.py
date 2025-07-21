from typing import List
from pydantic import BaseModel, ConfigDict

from pos_back_end.api.common_services import CommonBaseModel


class StateItem(CommonBaseModel):
    id: int
    state_name: str
    state_code: str

    model_config = ConfigDict(from_attributes=True)


class StateResponseBody(CommonBaseModel):
    states: List[StateItem]


class AddressRequestAndResponse(CommonBaseModel):
    street_address: str
    city: str
    state: str
    zipcode: str

    model_config = ConfigDict(from_attributes=True)

