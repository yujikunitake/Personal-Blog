from pydantic import BaseModel


class CreatePublisherRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    