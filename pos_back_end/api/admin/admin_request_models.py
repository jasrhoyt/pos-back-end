from pydantic import BaseModel


class AdminRequestBody(BaseModel):
    email: str
    password: str

