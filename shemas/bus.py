from pydantic import BaseModel
from shemas.park import Park


class Bus(BaseModel):
    number: int
    park: Park