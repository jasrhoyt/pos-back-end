from pydantic import BaseModel


class AdminRequestBody(BaseModel):
    user_id: str
    password: str

