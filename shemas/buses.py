from pydantic import BaseModel


class Park(BaseModel):
    name: str

class Bus(BaseModel):
    number: int
    park: Park